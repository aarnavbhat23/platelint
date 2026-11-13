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

# Shared with the injector by necessity: both sides need one answer for how
# much a well holds. Vendor-typical maximum fill, microlitres.
WELL_MAX_UL = {6: 3400, 12: 2400, 24: 1900, 48: 1000, 96: 360, 384: 112}

UNIT_UL = {"µl": 1.0, "μl": 1.0, "ul": 1.0, "ml": 1000.0}


def sents(text):
    parts = []
    for chunk in re.split(r"\n+", text):
        for s in re.split(r"(?<=[.!?])\s+", chunk):
            s = s.strip()
            if s:
                parts.append(s)
    return parts


def temps(s):
    out = []
    for m in re.finditer(r"(-?\d+(?:\.\d+)?)\s*(?:°\s?C|degrees?\s+C(?:elsius)?|\bC\b)", s):
        out.append((float(m.group(1)), m.group(0)))
    return out


DUR_RE = re.compile(
    r"\b(?:for\s+)?(\d+(?:\.\d+)?)\s*"
    r"(s|sec|secs|second|seconds|min|mins|minute|minutes|h|hr|hrs|hour|hours|days?)\b",
    re.I)
OVERNIGHT_RE = re.compile(r"\bovernight\b|\bO/N\b", re.I)
RANGE_RE = re.compile(r"\d+\s*(?:°\s?C)?\s*(?:-|–|—|to)\s*\d+\s*°\s?C")

INCUBATE_VERB = re.compile(r"\b(incubat|block|develop|equilibrat|cultur)\w*", re.I)
NEEDS_DURATION = re.compile(r"\b(incubat|block|develop|equilibrat)\w*", re.I)
STORAGE_CTX = re.compile(r"\b(stor|freez|frozen|aliquot|keep\s+at|long[- ]term|thaw)\w*", re.I)
THERMAL_CTX = re.compile(
    r"\b(denatur|anneal|extension|extend|cycl|melt|PCR|hot[- ]start|reverse transcri)\w*", re.I)

ASSAY = {
    "qpcr": re.compile(r"\b(qPCR|RT-qPCR|real[- ]time PCR|quantitative PCR|"
                       r"cycle threshold|Ct value|SYBR|TaqMan)\b", re.I),
    "elisa": re.compile(r"\b(ELISA|immunosorbent|capture antibody|detection antibody|TMB)\b", re.I),
    "viability": re.compile(r"\b(MTT|MTS|CellTiter|CellTitre|resazurin|viability|"
                            r"cytotoxicity|IC50)\b", re.I),
    "growth": re.compile(r"\b(OD\s?600|growth curve|optical density at 600|inoculat)\w*\b", re.I),
}
REQUIRED_CONTROL = {
    "qpcr": re.compile(r"\b(no[- ]template control|NTC|minus[- ]RT|no[- ]RT control|"
                       r"negative control)\b", re.I),
    "elisa": re.compile(r"\b(blank|standard curve|standards|negative control)\b", re.I),
    "viability": re.compile(r"\b(vehicle|untreated|negative control|DMSO control|"
                            r"media[- ]only|no[- ]cell)\b", re.I),
    "growth": re.compile(r"\b(media[- ]only|medium[- ]only|blank|uninoculated|"
                         r"sterile control|negative control)\b", re.I),
}

# What each instrument can measure. A generic "plate reader" is multimode, so it
# constrains nothing and is deliberately absent.
INSTRUMENT_CAN = [
    (re.compile(r"\b(absorbance reader|spectrophotometer)\b", re.I), {"absorbance"}),
    (re.compile(r"\bluminometer\b", re.I), {"luminescence"}),
    (re.compile(r"\b(fluorimeter|fluorometer)\b", re.I), {"fluorescence"}),
    (re.compile(r"\b(thermal cycler|thermocycler|real[- ]time PCR (?:machine|instrument|system)|"
                r"qPCR (?:machine|instrument|system))\b", re.I), {"fluorescence"}),
]
CHEMISTRY_NEEDS = [
    (re.compile(r"\b(TMB|pNPP|OPD|ABTS|MTT|MTS|formazan|crystal violet|OD\s?600)\b", re.I),
     "absorbance"),
    (re.compile(r"\b(CellTiter[- ]Glo|CellTitre[- ]Glo|luciferase|ATP[- ]based)\b", re.I),
     "luminescence"),
]
READOUT_RE = [
    (re.compile(r"\b(?:absorbance|optical density|OD)\b", re.I), "absorbance"),
    (re.compile(r"\bluminescen\w+\b", re.I), "luminescence"),
    (re.compile(r"\bfluorescen\w+\b", re.I), "fluorescence"),
]


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


# ---------- rule-based checker ----------

def plate_format(text):
    m = re.search(r"\b(6|12|24|48|96|384)[-\s]?well\b", text, re.I)
    return int(m.group(1)) if m else None


# A volume stated as per-well, allowing "of <reagent>" between the unit and the
# per-well marker: "200 uL of 1% BSA per well".
PER_WELL_VOL = re.compile(
    r"(\d+(?:\.\d+)?)\s*(µL|μL|uL|ul|µl|μl|mL|ml)\b[^.;]{0,40}?"
    r"(?:per|/|into each|in each|to each)\s*wells?\b", re.I)
ANY_VOL = re.compile(r"(\d+(?:\.\d+)?)\s*(µL|μL|uL|ul|µl|μl|mL|ml)\b")
# A sentence that is talking about what goes into the plate.
WELL_CTX = re.compile(r"\bwells?\b|\breactions?\b|\b(?:6|12|24|48|96|384)[-\s]?well\b", re.I)
# "every 20 minutes" is a sampling interval, not the length of the step.
INTERVAL_BEFORE = re.compile(r"(?:every|intervals?\s+of|each)\s*$", re.I)
# "after 48 hours", "at 24 hours": when the step happens, not how long it runs.
OFFSET_BEFORE = re.compile(r"(?:after|following|within|by|at|from)\s*$", re.I)


def step_durations(s):
    """Durations that say how long a step lasts. Sampling intervals ("every 20
    minutes") and timepoint offsets ("after 48 hours") are neither, and counting
    them as step durations both invents conflicts and hides missing ones."""
    out = []
    for m in DUR_RE.finditer(s):
        before = s[:m.start()]
        if INTERVAL_BEFORE.search(before) or OFFSET_BEFORE.search(before):
            continue
        out.append(m)
    return out


def rule_well_volume(text):
    fmt = plate_format(text)
    if not fmt:
        return ""
    cap = WELL_MAX_UL[fmt]
    # Any volume in a sentence about the plate has to fit in a well, whether or
    # not the sentence spells out "per well".
    singles = []
    for s in sents(text):
        if not WELL_CTX.search(s):
            continue
        for m in ANY_VOL.finditer(s):
            ul = float(m.group(1)) * UNIT_UL[m.group(2).lower()]
            if ul > cap:
                singles.append(f"'{m.group(0)}' = {ul:.0f} uL")
    if singles:
        return (f"{fmt}-well plate (max ~{cap} uL/well); over capacity: "
                + "; ".join(dict.fromkeys(singles)))
    total = 0.0
    n = 0
    for m in PER_WELL_VOL.finditer(text):
        total += float(m.group(1)) * UNIT_UL[m.group(2).lower()]
        n += 1
    if n >= 2 and total > cap:
        return (f"{fmt}-well plate (max ~{cap} uL/well); {n} per-well additions "
                f"sum to {total:.0f} uL")
    return ""


def rule_temperature(text):
    hits = []
    for s in sents(text):
        for t, shown in temps(s):
            if STORAGE_CTX.search(s):
                lo, hi, ctx = -85.0, 30.0, "storage"
            elif THERMAL_CTX.search(s):
                lo, hi, ctx = 4.0, 99.0, "thermocycling"
            else:
                lo, hi, ctx = 2.0, 45.0, "incubation"
            if not (lo <= t <= hi):
                hits.append(f"{shown} in a {ctx} step (expected {lo:g} to {hi:g} C)")
    return "; ".join(hits[:3])


def rule_units(text):
    hits = []
    for s in sents(text):
        # Millilitres in a step that fills a plate: the magnitude says microlitres
        # were meant. 3.4 mL is the largest well in any format here.
        if WELL_CTX.search(s):
            for m in re.finditer(r"(\d+(?:\.\d+)?)\s*(mL|ml)\b", s):
                if float(m.group(1)) > 3.4:
                    hits.append(f"'{m.group(0)}' in a plate step; more than any well holds")
        if re.search(r"\b(antibody|conjugate|antiserum|IgG|IgY)\b", s, re.I):
            for m in re.finditer(r"(\d+(?:\.\d+)?)\s*mg\s*/\s*(?:mL|ml)", s, re.I):
                hits.append(f"'{m.group(0)}' for an antibody working solution "
                            f"(normally ug/mL)")
        for m in re.finditer(r"(\d{2,4})\s*nM\b", s):
            if re.search(r"\b(read|absorbance|optical density|wavelength|emission|excitation)\b",
                         s, re.I) and 200 <= int(m.group(1)) <= 900:
                hits.append(f"'{m.group(0)}' used as a wavelength (nM is a concentration)")
        for m in re.finditer(r"(\d+(?:\.\d+)?)\s*nm\b", s):
            if re.search(r"\b(primer|probe|concentration|final|dNTP|oligo)\b", s, re.I) \
                    and not re.search(r"\b(read|absorbance|optical density|wavelength|"
                                      r"emission|excitation|filter)\b", s, re.I):
                hits.append(f"'{m.group(0)}' used as a concentration (nm is a wavelength)")
        if re.search(r"\b(primer|probe|antibody)\b", s, re.I):
            for m in re.finditer(r"(\d+(?:\.\d+)?)\s*mg\b(?!\s*/)", s, re.I):
                hits.append(f"'{m.group(0)}' of a primer or antibody (normally ng to ug)")
    return "; ".join(hits[:3])


def rule_conflicting(text):
    hits = []
    for s in sents(text):
        if not INCUBATE_VERB.search(s) or RANGE_RE.search(s):
            continue
        if len(INCUBATE_VERB.findall(s)) != 1:
            continue
        vals = {t for t, _ in temps(s)}
        if len(vals) >= 2:
            hits.append(f"one step at two temperatures: {sorted(vals)}")
        durs = {(m.group(1), m.group(2).lower()) for m in step_durations(s)}
        if OVERNIGHT_RE.search(s) and durs:
            hits.append(f"one step both overnight and timed ({durs.pop()[0]} units)")
        elif len(durs) >= 2:
            hits.append(f"one step with two durations: {sorted(durs)}")
    return "; ".join(hits[:3])


def rule_missing_control(text):
    for name, pat in ASSAY.items():
        if pat.search(text) and not REQUIRED_CONTROL[name].search(text):
            return f"looks like a {name} assay; no required control named"
    return ""


def rule_instrument_readout(text):
    asked = {kind for pat, kind in READOUT_RE if pat.search(text)}
    if not asked:
        return ""
    for pat, can in INSTRUMENT_CAN:
        m = pat.search(text)
        if m:
            bad = asked - can
            if bad:
                return (f"'{m.group(0)}' measures {'/'.join(sorted(can))}, "
                        f"but {'/'.join(sorted(bad))} is requested")
    for pat, needs in CHEMISTRY_NEEDS:
        m = pat.search(text)
        if m:
            if needs not in asked and asked:
                return (f"'{m.group(0)}' is read by {needs}, "
                        f"but {'/'.join(sorted(asked))} is requested")
    return ""


def rule_missing_duration(text):
    hits = []
    for s in sents(text):
        if not NEEDS_DURATION.search(s):
            continue
        if step_durations(s) or OVERNIGHT_RE.search(s) or re.search(r"\buntil\b", s, re.I):
            continue
        hits.append(f"'{s[:70].strip()}' has no duration")
    return "; ".join(hits[:2])


def rule_ordering(text):
    hits = []
    if re.search(r"before the overnight", text, re.I):
        hits.append("a step is ordered before an overnight incubation it also follows")
    for s in sents(text):
        if re.search(r"\b(read|measur|record)\w*", s, re.I) and \
                re.search(r"\bbefore\s+(?:adding|the addition of|you add)\b", s, re.I):
            hits.append(f"read ordered before an addition it depends on: '{s[:70].strip()}'")
    return "; ".join(hits[:2])


RULES = {
    "well_volume_exceeded": rule_well_volume,
    "conflicting_conditions": rule_conflicting,
    "missing_control": rule_missing_control,
    "unit_mismatch": rule_units,
    "instrument_readout_mismatch": rule_instrument_readout,
    "temperature_out_of_range": rule_temperature,
    "missing_required_duration": rule_missing_duration,
    "contradictory_ordering": rule_ordering,
}
assert set(RULES) == set(DEFECT_IDS), set(RULES) ^ set(DEFECT_IDS)


def check_rules(text):
    out = {}
    for k, fn in RULES.items():
        r = fn(text)
        if r:
            out[k] = r
    return out


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
