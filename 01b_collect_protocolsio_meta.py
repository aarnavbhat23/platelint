"""Stage 1b: protocols.io protocol metadata via CrossRef (no API key).

CrossRef holds every protocols.io DOI (prefix 10.17504) with its licence URL,
so licence and canonical URL are recorded by script. The step text itself is
not available unauthenticated: the protocols.io page renders it from an
authenticated API call, so it is captured separately (see README).
"""

import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request

CROSSREF = "https://api.crossref.org/works"
UA = "protocol-runnability-benchmark/1.0 (plate-assay benchmark; keyless)"

# Pinned so the candidate set does not drift as new protocols are deposited.
UNTIL_CREATED = "2026-11-12"
PREFIX = "10.17504"
LICENCE_OK = re.compile(r"creativecommons\.org/(?:licenses/by/|publicdomain/zero)", re.I)

TARGET_PER_CLASS = 16
ROWS = 100
SLEEP = 1.0

ASSAYS = {
    "elisa": "ELISA enzyme-linked immunosorbent assay 96-well plate",
    "qpcr": "qPCR quantitative real-time PCR 96-well plate",
    "viability": "MTT CellTiter-Glo cell viability assay 96-well plate",
    "growth_curve": "bacterial growth curve OD600 microplate reader",
}

# Titles must look plate-based; protocols.io has plenty of unrelated deposits.
PLATE_RE = re.compile(
    r"\b(?:6|12|24|48|96|384)[- ]well\b|microplate|microtit[er]re?|plate reader|\bplate\b",
    re.I,
)
ASSAY_RE = {
    "elisa": re.compile(r"elisa|immunosorbent|immunoassay", re.I),
    "qpcr": re.compile(r"qpcr|real[- ]time pcr|quantitative pcr|rt-qpcr", re.I),
    "viability": re.compile(r"mtt|celltiter|cell ?titer|viabilit|cytotox|resazurin|mts assay|alamar", re.I),
    "growth_curve": re.compile(r"growth curve|growth kinetic|od ?600|optical density|turbidit", re.I),
}


def get_json(url, params, tries=5):
    url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503) or i == tries - 1:
                raise
            time.sleep(2 ** i * 2)
    raise RuntimeError("unreachable")


def view_url(doi):
    """protocols.io page URL, derived from the DOI suffix (no network call)."""
    slug = doi.split("protocols.io.", 1)[-1]
    return "https://www.protocols.io/view/" + slug


def main():
    accepted, skipped = [], []
    for assay, q in ASSAYS.items():
        n_ok = 0
        offset = 0
        while n_ok < TARGET_PER_CLASS and offset < 400:
            d = get_json(CROSSREF, {
                "filter": f"prefix:{PREFIX},until-created-date:{UNTIL_CREATED}",
                "query.bibliographic": q,
                "rows": str(ROWS),
                "offset": str(offset),
                "select": "DOI,title,URL,license,created,publisher,author,type",
            })["message"]
            items = d.get("items", [])
            if not items:
                break
            offset += len(items)
            for it in items:
                if n_ok >= TARGET_PER_CLASS:
                    break
                doi = it.get("DOI", "")
                title = ((it.get("title") or [""])[0] or "").strip()
                lic = [l.get("URL", "") for l in (it.get("license") or [])]
                lic_ok = next((u for u in lic if LICENCE_OK.search(u)), "")
                if not lic_ok:
                    skipped.append((assay, doi, "|".join(lic) or "(none)", "licence not CC BY/CC0"))
                    continue
                # Plate-based is confirmed against the captured step text
                # (01d), not the title: protocols.io titles rarely state the
                # plate format.
                if not ASSAY_RE[assay].search(title):
                    skipped.append((assay, doi, lic_ok, "title does not name the assay"))
                    continue
                if "protocols.io." not in doi:
                    skipped.append((assay, doi, lic_ok, "DOI is not a protocols.io protocol"))
                    continue
                vurl = view_url(doi)
                slug = doi.split("protocols.io.", 1)[-1]
                accepted.append({
                    "id": "pio_" + assay + "_" + re.sub(r"[^a-z0-9]+", "-", slug.lower())[:40],
                    "assay_class": assay,
                    "source": "protocols.io",
                    "doi": doi,
                    "title": title,
                    "authors": "; ".join(
                        " ".join(x for x in [a.get("given", ""), a.get("family", "")] if x)
                        for a in (it.get("author") or [])
                    ),
                    "year": str((it.get("created") or {}).get("date-parts", [[""]])[0][0]),
                    "license": "cc by 4.0" if "/by/" in lic_ok else "cc0",
                    "license_url": lic_ok,
                    "url": "https://doi.org/" + doi,
                    "view_url": vurl,
                    "text_path": "",
                })
                n_ok += 1
            time.sleep(SLEEP)
        print(f"{assay}: accepted {n_ok}", file=sys.stderr)

    accepted.sort(key=lambda r: (r["assay_class"], r["doi"]))
    with open("data/sources_protocolsio.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(accepted[0].keys()))
        w.writeheader()
        w.writerows(accepted)
    with open("data/sources_protocolsio_skipped.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["assay_class", "doi", "license", "reason"])
        w.writerows(skipped)
    print(f"accepted {len(accepted)}, skipped {len(skipped)}")


if __name__ == "__main__":
    main()
