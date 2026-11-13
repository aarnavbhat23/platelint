"""Stage 5: the labelling sheet. 60 unedited model requests, model names hidden.

    python3 05_make_labels.py

Writes:
    data/labels_sheet.md   what you read and fill in: 60 requests, each with a
                           blank label line
    data/labels.csv        the same 60 items as rows with an empty label column,
                           if you would rather fill in a spreadsheet
    data/labels_key.csv    item code -> model and protocol. Do not open this
                           until the labels are done; stage 7 joins it then.

Nothing is pre-filled and no label is suggested. Sampling is seeded, 60 distinct
source protocols, stratified across the four assay classes and spread evenly
over the models, so one protocol never appears twice -- seeing two versions of
the same protocol would hint at which model wrote which.
"""

import csv
import glob
import hashlib
import importlib.util
import os
import random
import sys

SEED = 20261113
N_TOTAL = 60
REQUESTS = "data/requests"

_s = importlib.util.spec_from_file_location("defects", "03_defects.py")
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
DEFECT_IDS = [d["id"] for d in _d.DEFECTS]


def code_for(tag, pid):
    return "R" + hashlib.sha256(f"{SEED}|{tag}|{pid}".encode()).hexdigest()[:6].upper()


def main():
    with open("data/sources_all.csv") as f:
        sources = {r["id"]: r for r in csv.DictReader(f)}
    tags = sorted(d for d in os.listdir(REQUESTS)
                  if os.path.isdir(os.path.join(REQUESTS, d)) and d != "raw") \
        if os.path.isdir(REQUESTS) else []
    if not tags:
        sys.exit(f"no model output under {REQUESTS}/ -- run stage 2 first")

    have = {t: {os.path.basename(p)[:-4] for p in glob.glob(os.path.join(REQUESTS, t, "*.txt"))}
            for t in tags}
    every = set.intersection(*have.values()) if have else set()
    if len(every) < N_TOTAL:
        sys.exit(f"only {len(every)} protocols have a request from all {len(tags)} "
                 f"models; need {N_TOTAL}. Finish stage 2 first.")

    rng = random.Random(SEED)
    by_class = {}
    for pid in sorted(every):
        by_class.setdefault(sources[pid]["assay_class"], []).append(pid)
    classes = sorted(by_class)
    per_class = N_TOTAL // len(classes)

    chosen = []
    for i, cls in enumerate(classes):
        pool = sorted(by_class[cls])
        rng.shuffle(pool)
        n = per_class + (1 if i < N_TOTAL - per_class * len(classes) else 0)
        chosen.extend((pid, cls) for pid in pool[:n])

    # Spread the models evenly over the chosen protocols.
    order = list(tags)
    rng.shuffle(order)
    items = []
    for i, (pid, cls) in enumerate(chosen):
        tag = order[i % len(order)]
        items.append({"item_code": code_for(tag, pid), "assay_class": cls,
                      "model_tag": tag, "protocol_id": pid,
                      "path": os.path.join(REQUESTS, tag, pid + ".txt")})
    rng.shuffle(items)   # presentation order carries no model information

    os.makedirs("data", exist_ok=True)
    with open("data/labels.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item_code", "assay_class", "label", "defect_types", "notes"])
        for it in items:
            w.writerow([it["item_code"], it["assay_class"], "", "", ""])
    with open("data/labels_key.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item_code", "model_tag", "protocol_id"])
        for it in items:
            w.writerow([it["item_code"], it["model_tag"], it["protocol_id"]])

    with open("data/labels_sheet.md", "w") as f:
        f.write("# Labelling sheet\n\n")
        f.write(f"{len(items)} requests written by models, model names hidden. "
                f"Each is a rewrite of one published protocol.\n\n")
        f.write("For each one, write on the `label:` line whether a bench scientist "
                "could run it as written:\n\n")
        f.write("- `ok` if you would run it\n")
        f.write("- `defect` if you would send it back\n")
        f.write("- `unsure` if you cannot tell\n\n")
        f.write("On `defect_types:` list the ids that apply, comma separated, "
                "or leave it blank:\n\n")
        for d in DEFECT_IDS:
            f.write(f"- `{d}`\n")
        f.write("\nAnything not covered by those ids goes in `notes:`. "
                "Add ids of your own if you keep meeting the same problem.\n\n")
        f.write("---\n\n")
        for i, it in enumerate(items, 1):
            with open(it["path"]) as g:
                text = g.read().strip()
            f.write(f"## {i}. {it['item_code']}  ({it['assay_class']})\n\n")
            f.write("```\n" + text + "\n```\n\n")
            f.write("label: \n\ndefect_types: \n\nnotes: \n\n---\n\n")

    print(f"{len(items)} items sampled from {len(every)} protocols with a request "
          f"from all {len(tags)} models")
    for cls in classes:
        print(f"  {cls:<14} {sum(1 for i in items if i['assay_class'] == cls)}")
    print("\nper model (in data/labels_key.csv, not in the sheet):")
    for t in tags:
        print(f"  {t:<34} {sum(1 for i in items if i['model_tag'] == t)}")
    print("\nwrote data/labels_sheet.md, data/labels.csv, data/labels_key.csv")
    print("labels_key.csv is the unblinding key -- leave it shut until you are done")


if __name__ == "__main__":
    main()
