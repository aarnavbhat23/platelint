"""Stage 6: the three checkers.

    python3 06_check.py --checker keyword --selftest
    python3 06_check.py --checker rules --selftest
    python3 06_check.py --checker rules            # over the paired set
    GOOGLE_API_KEY=... python3 06_check.py --checker llm --model google:gemini-...

keyword  A deliberately crude baseline: one trigger phrase per defect type, no
         parsing and no arithmetic. It exists to show what the rule checker has
         to beat, and its false-positive rate is the point.
rules    Parses plate format, volumes, temperatures, units, controls, readouts
         and step order, and applies physical constraints.
llm      Asks a model which defect types are present. Needs a provider key.

The rule checker parses the text on its own terms. It does not know how a
defect was injected and shares nothing with 04_make_pairs.py except the table
of well capacities, which both have to agree on; that overlap is recorded in
the README as a limitation for well_volume_exceeded only.
"""

import argparse
import csv
import glob
import importlib.util
import json
import os
import random
import re
import sys

RESULTS = "results"
PAIRS = "data/pairs"

_s = importlib.util.spec_from_file_location("defects", "03_defects.py")
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
DEFECTS = _d.DEFECTS
DEFECT_IDS = [d["id"] for d in DEFECTS]

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
from platelint.rules import RULES, WELL_MAX_UL, check_rules  # noqa: E402,F401
assert set(RULES) == set(DEFECT_IDS), set(RULES) ^ set(DEFECT_IDS)

# ---------- trivial keyword baseline ----------

KEYWORD_TRIGGERS = {
    "well_volume_exceeded": lambda t: bool(re.search(r"\bmL\s*(?:per|/)\s*well", t, re.I)),
    "conflicting_conditions": lambda t: bool(re.search(r"4\s*°?\s?C", t)) and bool(re.search(r"37\s*°?\s?C", t)),
    "missing_control": lambda t: not re.search(r"\bcontrol\b|\bblank\b", t, re.I),
    "unit_mismatch": lambda t: bool(re.search(r"\d\s*(?:mg|mL)\b", t)),
    "instrument_readout_mismatch": lambda t: bool(re.search(r"\bluminescen\w+", t, re.I)),
    "temperature_out_of_range": lambda t: bool(re.search(r"-80|75\s*°?\s?C|95\s*°?\s?C", t)),
    "missing_required_duration": lambda t: bool(re.search(r"\bincubat\w*", t, re.I))
                                           and not re.search(r"\bfor\s+\d", t, re.I),
    "contradictory_ordering": lambda t: bool(re.search(r"\bimmediately\b", t, re.I)),
}


def check_keyword(text):
    return {k: ("keyword trigger matched" if fn(text) else "")
            for k, fn in KEYWORD_TRIGGERS.items() if fn(text)}

# ---------- LLM judge ----------

JUDGE_PROMPT = """You are a bench scientist reviewing a request sent to your lab. \
Decide which of the following problems the request has. Report a problem only if \
it is actually present in the text.

{catalogue}

Reply with JSON only, in this form:
{{"defects": ["id", ...]}}
Use an empty list if the request has none of these problems. Use only the ids listed.

Request:
---
{text}"""


def check_llm(text, provider, model):
    _p = importlib.util.spec_from_file_location("stage2", "02_write_requests.py")
    _m = importlib.util.module_from_spec(_p)
    _p.loader.exec_module(_m)
    catalogue = "\n".join(f"- {d['id']}: {d['objection']}" for d in DEFECTS)
    prompt = JUDGE_PROMPT.format(catalogue=catalogue, text=text)
    old_prompt, old_system = _m.PROMPT, _m.SYSTEM
    _m.PROMPT, _m.SYSTEM = "{text}", "Reply with JSON only."
    try:
        res = _m.CALL[provider](model, prompt)
    finally:
        _m.PROMPT, _m.SYSTEM = old_prompt, old_system
    raw = res["text"]
    m = re.search(r"\{.*\}", raw, re.S)
    if not m:
        return {}, f"no JSON in reply: {raw[:80]}"
    try:
        ids = json.loads(m.group(0)).get("defects") or []
    except json.JSONDecodeError as e:
        return {}, f"unparseable JSON ({e}): {raw[:80]}"
    bad = [i for i in ids if i not in DEFECT_IDS]
    return ({i: "flagged by the judge" for i in ids if i in DEFECT_IDS},
            f"judge returned unknown ids: {bad}" if bad else "")


# ---------- items, scoring, output ----------

def load_items():
    idx = os.path.join(PAIRS, "index.csv")
    if not os.path.exists(idx):
        sys.exit(f"{idx} not found -- run stage 4 first")
    items, seen = [], set()
    with open(idx) as f:
        for r in csv.DictReader(f):
            if r["clean_path"] not in seen:
                seen.add(r["clean_path"])
                items.append({"item_id": f"clean__{r['model_tag']}__{r['protocol_id']}",
                              "path": r["clean_path"], "model_tag": r["model_tag"],
                              "protocol_id": r["protocol_id"], "true_defect": ""})
            items.append({"item_id": r["pair_id"], "path": r["defect_path"],
                          "model_tag": r["model_tag"], "protocol_id": r["protocol_id"],
                          "true_defect": r["defect_id"]})
    return items


def selftest_items():
    """Fixtures from stage 4 plus one injected copy per defect type. Test data,
    not results: n is 4 clean and at most 32 defective."""
    p = importlib.util.spec_from_file_location("pairs", "04_make_pairs.py")
    m = importlib.util.module_from_spec(p)
    p.loader.exec_module(m)
    items = []
    for name, text in m.FIXTURES.items():
        items.append({"item_id": f"clean__{name}", "path": "", "model_tag": "fixture",
                      "protocol_id": name, "true_defect": "", "_text": text})
        for did, fn in m.INJECTORS.items():
            r = fn(text, random.Random(f"{name}|{did}"))
            if not r:
                continue
            items.append({"item_id": f"{name}__{did}", "path": "", "model_tag": "fixture",
                          "protocol_id": name, "true_defect": did, "_text": r[0]})
    return items


def run(checker, items, provider=None, model=None):
    rows = []
    for it in items:
        text = it.get("_text")
        if text is None:
            with open(it["path"]) as f:
                text = f.read()
        note = ""
        if checker == "keyword":
            flags = check_keyword(text)
        elif checker == "rules":
            flags = check_rules(text)
        else:
            flags, note = check_llm(text, provider, model)
        row = {"item_id": it["item_id"], "model_tag": it["model_tag"],
               "protocol_id": it["protocol_id"], "true_defect": it["true_defect"],
               "n_flags": len(flags), "flagged": ";".join(sorted(flags)), "note": note}
        for d in DEFECT_IDS:
            row["flag_" + d] = 1 if d in flags else 0
            row["why_" + d] = flags.get(d, "")
        rows.append(row)
    return rows


def report(rows):
    clean = [r for r in rows if not r["true_defect"]]
    print("\ndetection, per defect type")
    print(f"{'defect':<32}{'n':>5}{'exact':>8}{'rate':>8}{'any':>7}{'rate':>8}")
    for d in DEFECT_IDS:
        sub = [r for r in rows if r["true_defect"] == d]
        if not sub:
            print(f"  {d:<30}{0:>5}{'-':>8}{'-':>8}{'-':>7}{'-':>8}")
            continue
        hit = sum(r["flag_" + d] for r in sub)
        anyf = sum(1 for r in sub if r["n_flags"])
        print(f"  {d:<30}{len(sub):>5}{hit:>8}{100*hit/len(sub):>7.1f}%"
              f"{anyf:>7}{100*anyf/len(sub):>7.1f}%")
    print("  exact = flagged the type that was injected; "
          "any = flagged at least one type")
    if clean:
        any_flag = sum(1 for r in clean if r["n_flags"])
        print(f"\nfalse positives on {len(clean)} clean requests: "
              f"{any_flag} flagged at least once ({100*any_flag/len(clean):.1f}%)")
        print(f"{'defect':<32}{'flagged':>9}{'rate':>8}")
        for d in DEFECT_IDS:
            n = sum(r["flag_" + d] for r in clean)
            print(f"  {d:<30}{n:>9}{100*n/len(clean):>7.1f}%")
    bad = [r for r in rows if r["note"]]
    if bad:
        print(f"\n{len(bad)} items had checker notes, first few:")
        for r in bad[:5]:
            print(f"  {r['item_id']}: {r['note']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checker", required=True, choices=["keyword", "rules", "llm"])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--model", help="for --checker llm: provider:model, e.g. google:gemini-x")
    a = ap.parse_args()

    provider = model = None
    if a.checker == "llm":
        if not a.model or ":" not in a.model:
            sys.exit("--checker llm needs --model provider:model")
        provider, model = a.model.split(":", 1)

    items = selftest_items() if a.selftest else load_items()
    n_clean = sum(1 for i in items if not i["true_defect"])
    print(f"{len(items)} items: {n_clean} clean, {len(items)-n_clean} with one injected defect"
          + ("   (fixtures: test data, not results)" if a.selftest else ""))
    rows = run(a.checker, items, provider, model)
    report(rows)

    if not a.selftest:
        os.makedirs(RESULTS, exist_ok=True)
        path = os.path.join(RESULTS, f"checks_{a.checker}.csv")
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {path}")


if __name__ == "__main__":
    main()
