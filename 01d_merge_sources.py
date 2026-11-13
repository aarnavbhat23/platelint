"""Stage 1d: merge the two source sets into data/sources_all.csv.

Checks every protocol is plate-based, drops duplicates (protocols.io carries
"Copy of" forks and repeated iGEM calibration protocols, which would otherwise
leak the same protocol into both the tuning and test split), and records what
was dropped and why.
"""

import csv
import hashlib
import os
import re
import sys

PLATE_RE = re.compile(
    r"\b(?:6|12|24|48|96|384|1536)[- ]well\b|microplate|microtit[er]re?|plate reader|well plate",
    re.I,
)
VOLUME_RE = re.compile(r"\b\d+(?:\.\d+)?\s*(?:[µuμ]l|ul|µL|mL|ml|microlit|millilit)\b", re.I)
MIN_CHARS = 400
MIN_STEPS = 2  # a protocol with no step list is not a protocol

# Scope cap: 25 per assay class, split as evenly as the two sources allow.
# Selection is by sorted id, so it is deterministic without an RNG.
PER_CLASS = 25


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def main():
    rows, dropped = [], []

    with open("data/sources.csv") as f:
        for r in csv.DictReader(f):
            r["source"] = "europepmc"
            rows.append(r)

    with open("data/sources_protocolsio.csv") as f:
        for r in csv.DictReader(f):
            p = os.path.join("data/protocols_io", r["id"] + ".txt")
            if not os.path.exists(p):
                dropped.append((r["id"], r["assay_class"], "protocols.io", "step text not captured"))
                continue
            r["text_path"] = p
            r["n_chars"] = str(os.path.getsize(p))
            rows.append(r)

    kept, seen_hash, seen_title = [], {}, {}
    for r in rows:
        with open(r["text_path"]) as f:
            text = f.read()
        if len(text) < MIN_CHARS:
            dropped.append((r["id"], r["assay_class"], r["source"], f"text too short ({len(text)} chars)"))
            continue
        if r["source"] == "protocols.io":
            n_steps = len(re.findall(r"^\d+\. ", text, re.M))
            if n_steps < MIN_STEPS:
                dropped.append((r["id"], r["assay_class"], r["source"],
                                f"only {n_steps} numbered steps"))
                continue
        if not PLATE_RE.search(text):
            dropped.append((r["id"], r["assay_class"], r["source"], "no plate/well term in text"))
            continue

        h = hashlib.sha256(norm(text).encode()).hexdigest()[:16]
        if h in seen_hash:
            dropped.append((r["id"], r["assay_class"], r["source"], f"duplicate text of {seen_hash[h]}"))
            continue
        t = norm(re.sub(r"^\s*copy of\s*", "", r["title"], flags=re.I))
        t = re.sub(r"\bv\s*\d+\b", "", t).strip()
        if t and t in seen_title:
            dropped.append((r["id"], r["assay_class"], r["source"], f"duplicate title of {seen_title[t]}"))
            continue
        seen_hash[h] = r["id"]
        if t:
            seen_title[t] = r["id"]

        r["text_sha256_16"] = h
        r["has_explicit_volume"] = "yes" if VOLUME_RE.search(text) else "no"
        r["n_chars"] = str(len(text))
        kept.append(r)

    capped, overflow = [], []
    for a in sorted({r["assay_class"] for r in kept}):
        pool = {s: sorted((r for r in kept if r["assay_class"] == a and r["source"] == s),
                          key=lambda r: r["id"])
                for s in ("europepmc", "protocols.io")}
        take, i = [], 0
        while len(take) < PER_CLASS and any(pool.values()):
            for s in ("europepmc", "protocols.io"):
                if pool[s] and len(take) < PER_CLASS:
                    take.append(pool[s].pop(0))
        capped.extend(take)
        for s in pool:
            for r in pool[s]:
                overflow.append((r["id"], a, r["source"], f"over the {PER_CLASS}/class scope cap"))
    dropped.extend(overflow)
    kept = capped

    cols = ["id", "source", "assay_class", "title", "authors", "year", "journal",
            "doi", "pmcid", "pmid", "license", "license_url", "url",
            "text_path", "n_chars", "has_explicit_volume", "text_sha256_16"]
    kept.sort(key=lambda r: (r["assay_class"], r["source"], r["id"]))
    with open("data/sources_all.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in kept:
            w.writerow({c: r.get(c, "") for c in cols})
    with open("data/sources_all_dropped.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "assay_class", "source", "reason"])
        w.writerows(dropped)

    print(f"kept {len(kept)}, dropped {len(dropped)}")
    for s in ("europepmc", "protocols.io"):
        n = sum(1 for r in kept if r["source"] == s)
        print(f"  {s}: {n}")
    for a in sorted({r["assay_class"] for r in kept}):
        n = sum(1 for r in kept if r["assay_class"] == a)
        nv = sum(1 for r in kept if r["assay_class"] == a and r["has_explicit_volume"] == "yes")
        print(f"  {a}: {n} ({nv} state an explicit volume)")


if __name__ == "__main__":
    main()
