"""Stage 1: collect open-licence, plate-based assay protocols from Europe PMC.

No API key is needed. Every accepted protocol records its licence and URL;
anything whose licence is not plainly CC BY or CC0 is skipped and logged.
"""

import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
FULLTEXT = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
ARTICLE_URL = "https://europepmc.org/article/PMC/{pmcid}"

# Upper date bound is pinned so the candidate set does not drift as new
# articles are indexed.
DATE_RANGE = '[1990-01-01 TO 2026-11-12]'

# Licences we accept. Europe PMC reports these lowercase in the `license` field.
LICENCE_OK = {"cc by", "cc0", "cc by 4.0", "cc-by", "cc by/4.0"}

TARGET_PER_CLASS = 25
MAX_CANDIDATES_PER_CLASS = 300
SLEEP = 0.34  # polite rate limit

ASSAYS = {
    "elisa": '(ELISA OR "enzyme-linked immunosorbent assay" OR "sandwich immunoassay")',
    "qpcr": '("qPCR" OR "RT-qPCR" OR "quantitative real-time PCR" OR "quantitative PCR")',
    "viability": '("MTT assay" OR "CellTiter-Glo" OR "MTS assay" OR "resazurin" OR "cell viability assay")',
    "growth_curve": '("growth curve" OR "OD600" OR "optical density at 600" OR "bacterial growth kinetics")',
}

PLATE_TERMS = [
    "96-well", "96 well", "384-well", "384 well", "48-well", "48 well",
    "24-well", "24 well", "12-well", "12 well", "6-well", "6 well",
    "microplate", "microtiter", "microtitre", "plate reader",
]
VOLUME_RE = re.compile(r"\b\d+(?:\.\d+)?\s*(?:[µuμ]l|ul|µL|mL|ml)\b", re.I)

# Section titles that hold the bench steps. Protocol papers vary a lot, so we
# keep anything that looks procedural and fall back to the whole body.
PROC_TITLES = re.compile(
    r"procedure|protocol|method|materials|reagent|equipment|step|assay|preparation",
    re.I,
)


def get(url, params=None):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "protocol-runnability-benchmark/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def search(assay_query, cursor="*"):
    q = (
        f'{assay_query} AND (TITLE:"protocol" OR TITLE:"procedure" OR TITLE:"method" '
        f'OR JOURNAL:"Bio-protocol" OR JOURNAL:"STAR protocols" OR JOURNAL:"Methods and protocols") '
        f'AND OPEN_ACCESS:y AND HAS_FT:y AND IN_EPMC:y '
        f'AND FIRST_PDATE:{DATE_RANGE}'
    )
    raw = get(SEARCH, {
        "query": q,
        "format": "json",
        "resultType": "core",
        "pageSize": "100",
        "cursorMark": cursor,
        "sort": "P_PDATE_D desc",
    })
    return json.loads(raw)


def licence_url_from_xml(root):
    for lic in root.iter("license"):
        href = lic.get("{http://www.w3.org/1999/xlink}href")
        if href:
            return href
        for a in lic.iter("ext-link"):
            h = a.get("{http://www.w3.org/1999/xlink}href")
            if h and "creativecommons" in h:
                return h
        txt = " ".join(lic.itertext())
        m = re.search(r"https?://creativecommons\.org/\S+", txt)
        if m:
            return m.group(0).rstrip(").,")
    return ""


def flat(el):
    return re.sub(r"\s+", " ", " ".join(el.itertext())).strip()


def procedure_text(root):
    body = root.find("body")
    if body is None:
        return ""
    chunks = []
    for sec in body.findall("sec"):
        t = sec.find("title")
        title = t.text if t is not None and t.text else ""
        if PROC_TITLES.search(title):
            chunks.append(("## " + title.strip() + "\n" + flat(sec)))
    if not chunks:
        return flat(body)
    return "\n\n".join(chunks)


def main():
    os.makedirs("data/raw_xml", exist_ok=True)
    os.makedirs("data/protocols", exist_ok=True)
    accepted, skipped = [], []

    for assay, aq in ASSAYS.items():
        n_ok = 0
        seen = 0
        cursor = "*"
        while n_ok < TARGET_PER_CLASS and seen < MAX_CANDIDATES_PER_CLASS:
            res = search(aq, cursor)
            hits = res.get("resultList", {}).get("result", [])
            next_cursor = res.get("nextCursorMark")
            if not hits:
                break
            for h in hits:
                if n_ok >= TARGET_PER_CLASS or seen >= MAX_CANDIDATES_PER_CLASS:
                    break
                seen += 1
                pmcid = h.get("pmcid") or ""
                lic = (h.get("license") or "").strip().lower()
                if not pmcid:
                    skipped.append((assay, h.get("id", ""), lic, "no PMCID"))
                    continue
                if lic not in LICENCE_OK:
                    skipped.append((assay, pmcid, lic or "(none reported)", "licence not CC BY/CC0"))
                    continue

                xml_path = f"data/raw_xml/{pmcid}.xml"
                if not os.path.exists(xml_path):
                    try:
                        raw = get(FULLTEXT.format(pmcid=pmcid))
                    except Exception as e:
                        skipped.append((assay, pmcid, lic, f"fulltext fetch failed: {e}"))
                        time.sleep(SLEEP)
                        continue
                    with open(xml_path, "wb") as f:
                        f.write(raw)
                    time.sleep(SLEEP)
                try:
                    root = ET.parse(xml_path).getroot()
                except ET.ParseError as e:
                    skipped.append((assay, pmcid, lic, f"xml parse failed: {e}"))
                    continue

                lic_url = licence_url_from_xml(root)
                if "creativecommons.org" not in lic_url:
                    skipped.append((assay, pmcid, lic, "no CC licence URL in full text"))
                    continue
                if "/by/" not in lic_url and "/zero/" not in lic_url and "/publicdomain/" not in lic_url:
                    skipped.append((assay, pmcid, lic, f"licence URL not BY/CC0: {lic_url}"))
                    continue

                text = procedure_text(root)
                low = text.lower()
                found = [t for t in PLATE_TERMS if t in low]
                if not found:
                    skipped.append((assay, pmcid, lic, "no plate/well term in procedure text"))
                    continue
                if not VOLUME_RE.search(text):
                    skipped.append((assay, pmcid, lic, "no explicit volume in procedure text"))
                    continue
                if len(text) < 1500:
                    skipped.append((assay, pmcid, lic, f"procedure text too short ({len(text)} chars)"))
                    continue

                pid = f"{assay}_{pmcid}"
                tp = f"data/protocols/{pid}.txt"
                with open(tp, "w") as f:
                    f.write(text)
                ji = (h.get("journalInfo") or {}).get("journal") or {}
                accepted.append({
                    "id": pid,
                    "assay_class": assay,
                    "pmcid": pmcid,
                    "pmid": h.get("pmid", "") or "",
                    "doi": h.get("doi", "") or "",
                    "title": (h.get("title") or "").strip(),
                    "journal": ji.get("title", "") or "",
                    "year": h.get("pubYear", "") or "",
                    "authors": (h.get("authorString") or "").strip(),
                    "license": lic,
                    "license_url": lic_url,
                    "url": ARTICLE_URL.format(pmcid=pmcid),
                    "text_path": tp,
                    "n_chars": len(text),
                    "plate_terms": "|".join(sorted(set(found))),
                })
                n_ok += 1
            if not next_cursor or next_cursor == cursor:
                break
            cursor = next_cursor
        print(f"{assay}: accepted {n_ok} of {seen} candidates", file=sys.stderr)

    accepted.sort(key=lambda r: (r["assay_class"], r["pmcid"]))
    with open("data/sources.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(accepted[0].keys()))
        w.writeheader()
        w.writerows(accepted)
    with open("data/sources_skipped.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["assay_class", "id", "license_reported", "reason"])
        w.writerows(skipped)

    print(f"accepted {len(accepted)} protocols, skipped {len(skipped)} candidates")


if __name__ == "__main__":
    main()
