"""Stage 4: build the paired set. For each clean request, one version per
defect type, each carrying exactly one injected defect, with a diff per pair.

    python3 04_make_pairs.py --selftest            # injectors against fixtures
    python3 04_make_pairs.py --coverage data/protocols   # how often each precondition appears
    python3 04_make_pairs.py                       # build pairs from data/requests/

Every injector returns None when the text does not contain what it needs to
edit. That is recorded, not worked around: a defect type that can only be
injected into part of the corpus has a smaller paired set, and the report has
to say so rather than quietly evaluating on fewer examples.

A pair is written only when the edit produces exactly one diff hunk. Two hunks
would mean two defects, which breaks the one-defect-per-pair design.
"""

import argparse
import csv
import difflib
import glob
import importlib.util
import os
import random
import re
import sys

OUT = "data/pairs"
REQUESTS = "data/requests"

spec = importlib.util.spec_from_file_location("defects", "03_defects.py")
_d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_d)
DEFECTS = _d.DEFECTS

# Maximum fill volume per well, microlitres, for the common flat-bottom formats
# (vendor-typical: Corning/Greiner catalogue values). The stage 6 rule checker
# uses this same table, so a volume-overflow detection is partly a check that
# the two agree. Injection therefore overshoots by 3x, well past any plausible
# disagreement about the exact maximum.
WELL_MAX_UL = {6: 3400, 12: 2400, 24: 1900, 48: 1000, 96: 360, 384: 112}

PLATE_RE = re.compile(r"\b(6|12|24|48|96|384)[-\s]?well\b", re.I)
VOL_RE = re.compile(r"(\d+(?:\.\d+)?)\s*(µL|μL|uL|ul|µl|μl|mL|ml)\b")
TEMP_RE = re.compile(r"(-?\d+(?:\.\d+)?)\s*(?:°\s?C|degrees?\s+C(?:elsius)?|\bC\b)")
DUR_RE = re.compile(
    r"\bfor\s+(?:\d+(?:\.\d+)?|a\s+few|several)\s*"
    r"(?:s|sec|secs|second|seconds|min|mins|minute|minutes|h|hr|hrs|hour|hours)\b",
    re.I,
)
CONTROL_RE = re.compile(
    r"(no[- ]template control|NTC\b|vehicle control|vehicle[- ]only|untreated control|"
    r"negative control|positive control|blank(?:\s+wells?)?|unstained control|"
    r"media[- ]only|no[- ]cell control)", re.I)
INCUBATE_RE = re.compile(
    r"\b(incubat\w*|wash\w*|develop\w*|centrifug\w*|shak\w*|rock\w*|block\w*|cycl\w*)\b", re.I)
COLORIMETRIC_RE = re.compile(r"\b(TMB|pNPP|OPD|ABTS|MTT|MTS|formazan|OD\s?600|crystal violet)\b", re.I)
INSTRUMENT_RE = re.compile(
    r"\b(plate reader|microplate reader|spectrophotometer|absorbance reader|"
    r"luminometer|fluorimeter|fluorometer|thermal cycler|thermocycler|"
    r"real[- ]time PCR (?:machine|instrument|system)|qPCR (?:machine|instrument|system))\b", re.I)
ABSORBANCE_RE = re.compile(
    r"\b(?:absorbance|optical density|OD)\s*(?:at|of)?\s*(\d{3})\s*nm\b", re.I)


def sentences(text):
    """Offsets of sentence-ish spans. Protocol prose is full of '37 °C.' and
    '0.5 mL', so split only on terminators followed by whitespace and a capital
    or a digit-plus-period list marker."""
    spans, start = [], 0
    for m in re.finditer(r"(?<=[.!?])\s+(?=[A-Z(])|\n+", text):
        spans.append((start, m.start()))
        start = m.end()
    if start < len(text):
        spans.append((start, len(text)))
    return [(a, b) for a, b in spans if b > a]


def norm_ul(value, unit):
    return value * (1000.0 if unit.lower() in ("ml",) else 1.0)


def pick(rng, items):
    return items[rng.randrange(len(items))] if items else None


# --- injectors. Each returns (new_text, precondition, note) or None. ---

def inj_well_volume(text, rng):
    pm = PLATE_RE.search(text)
    if not pm:
        return None
    fmt = int(pm.group(1))
    cap = WELL_MAX_UL[fmt]
    cands = [m for m in VOL_RE.finditer(text)
             if norm_ul(float(m.group(1)), m.group(2)) <= cap]
    m = pick(rng, cands)
    if not m:
        return None
    new_val = int(cap * 3)
    new = f"{new_val} µL"
    out = text[:m.start()] + new + text[m.end():]
    return (out, f"{fmt}-well plate named, volume {m.group(0)} present",
            f"{m.group(0)} -> {new} in a {fmt}-well plate (max fill ~{cap} µL)")


def inj_conflicting_conditions(text, rng):
    cands = []
    for a, b in sentences(text):
        tm = TEMP_RE.search(text, a, b)
        if tm and INCUBATE_RE.search(text, a, b):
            cands.append((a, b, float(tm.group(1)), tm.group(0)))
    c = pick(rng, cands)
    if not c:
        return None
    a, b, t, shown = c
    other = "4 °C" if t >= 25 else "37 °C"
    sent = text[a:b].rstrip()
    stripped = sent[:-1] if sent.endswith(".") else sent
    new_sent = f"{stripped}, and hold the plate at {other} for the whole of this step."
    out = text[:a] + new_sent + text[b:]
    return (out, f"step states {shown} and an incubation verb",
            f"added a second, incompatible temperature ({other}) to a step already at {shown}")


def inj_missing_control(text, rng):
    cands = [(a, b, CONTROL_RE.search(text, a, b).group(0))
             for a, b in sentences(text) if CONTROL_RE.search(text, a, b)]
    c = pick(rng, cands)
    if not c:
        return None
    a, b, shown = c
    out = text[:a] + text[b:]
    out = re.sub(r"[ \t]{2,}", " ", out)
    return (out, f"a sentence names '{shown}'",
            f"deleted the sentence naming '{shown}'")


UNIT_SWAPS = [("µL", "mL"), ("μL", "mL"), ("uL", "mL"), ("ul", "ml"), ("µl", "ml"),
              ("mL", "µL"), ("ml", "µl"),
              ("µg", "mg"), ("μg", "mg"), ("ug", "mg"), ("mg", "µg"),
              ("nM", "nm"), ("µM", "mM"), ("μM", "mM"), ("mM", "µM"),
              ("ng", "mg")]


def inj_unit_mismatch(text, rng):
    cands = []
    for frm, to in UNIT_SWAPS:
        for m in re.finditer(r"(\d(?:[\d.]*)\s*)" + re.escape(frm) + r"\b", text):
            cands.append((m, frm, to))
    c = pick(rng, cands)
    if not c:
        return None
    m, frm, to = c
    out = text[:m.start()] + m.group(1) + to + text[m.end():]
    return (out, f"a quantity in {frm}",
            f"{m.group(0).strip()} -> {m.group(1).strip()} {to} (unit swapped, number unchanged)")


def inj_instrument_readout(text, rng):
    inst = INSTRUMENT_RE.search(text)
    colour = COLORIMETRIC_RE.search(text)
    if not (inst or colour):
        return None
    def because():
        if inst:
            return f"the named {inst.group(0)} cannot produce it", inst.group(0)
        return (f"the assay is read colorimetrically ({colour.group(0)})",
                colour.group(0))

    am = pick(rng, list(ABSORBANCE_RE.finditer(text)))
    if am:
        out = text[:am.start()] + "luminescence" + text[am.end():]
        why, anchor = because()
        return (out, f"absorbance readout with {anchor} present",
                f"'{am.group(0)}' -> 'luminescence'; {why}")
    for word, repl in (("luminescence", "absorbance at 570 nm"),
                       ("fluorescence", "absorbance at 450 nm")):
        m = re.search(r"\b" + word + r"\b", text, re.I)
        if m:
            out = text[:m.start()] + repl + text[m.end():]
            why, anchor = because()
            return (out, f"{word} readout with {anchor} present",
                    f"'{m.group(0)}' -> '{repl}'; {why}")
    return None


def inj_temperature(text, rng):
    cands = []
    for m in TEMP_RE.finditer(text):
        t = float(m.group(1))
        if 15 <= t <= 42:
            cands.append((m, "75 °C"))
        elif -25 <= t <= 10:
            cands.append((m, "-80 °C"))
    c = pick(rng, cands)
    if not c:
        return None
    m, repl = c
    out = text[:m.start()] + repl + text[m.end():]
    return (out, f"an incubation temperature of {m.group(0)}",
            f"{m.group(0)} -> {repl}, outside the workable range for this step")


def inj_missing_duration(text, rng):
    cands = []
    for a, b in sentences(text):
        dm = DUR_RE.search(text, a, b)
        if dm and INCUBATE_RE.search(text, a, b):
            cands.append((dm, text[a:b]))
    c = pick(rng, cands)
    if not c:
        return None
    dm, _ = c
    out = text[:dm.start()] + text[dm.end():]
    out = re.sub(r"\s+([.,;])", r"\1", out)
    out = re.sub(r"[ \t]{2,}", " ", out)
    return (out, f"a step stating '{dm.group(0)}'",
            f"deleted '{dm.group(0)}', leaving the step with no duration")


OVERNIGHT_RE = re.compile(r"\bovernight\b(?!\s+(?:culture|cultures|starter|broth))", re.I)


def inj_contradictory_order(text, rng):
    on = None
    for a0, b0 in sentences(text):
        m = OVERNIGHT_RE.search(text, a0, b0)
        if m and INCUBATE_RE.search(text, a0, b0):
            on = m
            break
    if on:
        a, b = next((a, b) for a, b in sentences(text) if a <= on.start() < b)
        ins = (" Read the plate immediately, before the overnight incubation "
               "has been carried out.")
        out = text[:b] + ins + text[b:]
        return (out, "an overnight incubation is stated",
                "inserted a read that must happen before a step it also follows")
    sm = re.search(r"\badd(?:ing)?\s+(?:the\s+)?(substrate|TMB|stop solution|reagent)\b",
                   text, re.I)
    if sm:
        a, b = next((a, b) for a, b in sentences(text) if a <= sm.start() < b)
        ins = f" Take the reading before adding the {sm.group(1)}."
        out = text[:b] + ins + text[b:]
        return (out, f"a step adds {sm.group(1)}",
                f"inserted a read ordered before the {sm.group(1)} it depends on")
    return None


INJECTORS = {
    "well_volume_exceeded": inj_well_volume,
    "conflicting_conditions": inj_conflicting_conditions,
    "missing_control": inj_missing_control,
    "unit_mismatch": inj_unit_mismatch,
    "instrument_readout_mismatch": inj_instrument_readout,
    "temperature_out_of_range": inj_temperature,
    "missing_required_duration": inj_missing_duration,
    "contradictory_ordering": inj_contradictory_order,
}

assert set(INJECTORS) == {d["id"] for d in DEFECTS}, (
    "03_defects.py and the injectors disagree: "
    f"{set(INJECTORS) ^ {d['id'] for d in DEFECTS}}")


def diff_of(clean, dirty, name):
    return list(difflib.unified_diff(
        clean.splitlines(keepends=True), dirty.splitlines(keepends=True),
        fromfile=name + " (clean)", tofile=name + " (defect)", n=1))


def n_hunks(diff):
    return sum(1 for line in diff if line.startswith("@@"))


FIXTURES = {
    "elisa": (
        "Please coat a 96-well plate with the capture antibody at 2 µg/mL in "
        "carbonate buffer and incubate overnight at 4 °C.\n"
        "Wash the plate three times with PBS-T, then block with 200 µL of 1% BSA "
        "per well for 1 hour at 37 °C.\n"
        "Add 100 µL of each serum sample in duplicate, and include a blank well "
        "containing buffer only.\n"
        "Develop with TMB for 15 minutes, stop with 50 µL of 2 M sulphuric acid, "
        "and read absorbance at 450 nm on the plate reader.\n"
    ),
    "viability": (
        "Seed the cells into a 96-well plate at 5000 cells per well in 100 µL of "
        "medium and incubate for 24 hours at 37 °C.\n"
        "Treat with the compound across an eight-point dilution series, and keep a "
        "vehicle control on every plate.\n"
        "After 48 hours add 20 µL of MTT solution per well and incubate for 4 hours.\n"
        "Solubilise the formazan and read absorbance at 570 nm.\n"
    ),
    "qpcr": (
        "Set up 20 µL reactions in a 384-well plate with 10 µL of master mix, "
        "500 nM of each primer and 2 µL of cDNA.\n"
        "Include a no-template control for every primer pair.\n"
        "Run on the real-time PCR instrument for 40 cycles and read fluorescence "
        "at the end of each extension step.\n"
    ),
    "growth": (
        "Dilute the overnight culture 1:100 into fresh LB and load 150 µL per well "
        "into a 96-well plate.\n"
        "Incubate at 37 °C with shaking for 18 hours and read OD 600 every 20 minutes "
        "on the microplate reader.\n"
        "Include a media-only blank in triplicate.\n"
    ),
}


def selftest():
    print("injector self-test against built-in fixtures (test data, not results)\n")
    fails = 0
    for did in INJECTORS:
        hits = []
        for fname, text in FIXTURES.items():
            rng = random.Random(f"{fname}|{did}")
            r = INJECTORS[did](text, rng)
            if not r:
                continue
            dirty, pre, note = r
            d = diff_of(text, dirty, fname)
            h = n_hunks(d)
            ok = dirty != text and h == 1
            hits.append((fname, ok, h, note))
        if not hits:
            print(f"FAIL {did}: fired on none of the {len(FIXTURES)} fixtures")
            fails += 1
            continue
        bad = [x for x in hits if not x[1]]
        status = "ok  " if not bad else "FAIL"
        if bad:
            fails += 1
        print(f"{status} {did}: fired on {len(hits)}/{len(FIXTURES)} fixtures")
        for fname, ok, h, note in hits:
            mark = " " if ok else f" <-- {h} hunks"
            print(f"       {fname}: {note}{mark}")
    print()
    if fails:
        print(f"{fails} injector(s) failed the self-test")
        sys.exit(1)
    print(f"all {len(INJECTORS)} injectors produce exactly one hunk where they fire")


def coverage(d):
    files = sorted(glob.glob(os.path.join(d, "*.txt")))
    if not files:
        sys.exit(f"no .txt files in {d}")
    print(f"injector coverage over {len(files)} files in {d}")
    print("(how often each precondition is present; not the paired set)\n")
    counts = {k: 0 for k in INJECTORS}
    hunks_bad = {k: 0 for k in INJECTORS}
    for p in files:
        with open(p) as f:
            text = f.read()
        pid = os.path.basename(p)[:-4]
        for did, fn in INJECTORS.items():
            r = fn(text, random.Random(f"{pid}|{did}"))
            if not r:
                continue
            if n_hunks(diff_of(text, r[0], pid)) == 1:
                counts[did] += 1
            else:
                hunks_bad[did] += 1
    for did in INJECTORS:
        n = counts[did]
        extra = f"   ({hunks_bad[did]} rejected for >1 hunk)" if hunks_bad[did] else ""
        print(f"  {did:<32} {n:4d}/{len(files)}  {100*n/len(files):5.1f}%{extra}")


def build():
    tags = sorted(d for d in os.listdir(REQUESTS)
                  if os.path.isdir(os.path.join(REQUESTS, d)) and d != "raw") \
        if os.path.isdir(REQUESTS) else []
    if not tags:
        sys.exit(f"no model output directories under {REQUESTS}/ -- run stage 2 first")

    os.makedirs(os.path.join(OUT, "diffs"), exist_ok=True)
    index, rejected = [], []
    for tag in tags:
        for p in sorted(glob.glob(os.path.join(REQUESTS, tag, "*.txt"))):
            pid = os.path.basename(p)[:-4]
            with open(p) as f:
                clean = f.read()
            if not clean.strip():
                rejected.append((tag, pid, "", "clean request is empty"))
                continue
            for did, fn in INJECTORS.items():
                rng = random.Random(f"{tag}|{pid}|{did}")
                r = fn(clean, rng)
                if not r:
                    rejected.append((tag, pid, did, "precondition absent"))
                    continue
                dirty, pre, note = r
                d = diff_of(clean, dirty, f"{tag}/{pid}")
                h = n_hunks(d)
                if h != 1:
                    rejected.append((tag, pid, did, f"{h} diff hunks, not 1"))
                    continue
                pair_id = f"{tag}__{pid}__{did}"
                dp = os.path.join(OUT, tag, did, pid + ".txt")
                os.makedirs(os.path.dirname(dp), exist_ok=True)
                with open(dp, "w") as f:
                    f.write(dirty)
                diffp = os.path.join(OUT, "diffs", pair_id + ".diff")
                with open(diffp, "w") as f:
                    f.writelines(d)
                index.append({
                    "pair_id": pair_id, "model_tag": tag, "protocol_id": pid,
                    "defect_id": did, "precondition": pre, "note": note,
                    "clean_path": p, "defect_path": dp, "diff_path": diffp,
                })

    with open(os.path.join(OUT, "index.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(index[0].keys()))
        w.writeheader()
        w.writerows(index)
    with open(os.path.join(OUT, "not_injected.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["model_tag", "protocol_id", "defect_id", "reason"])
        w.writerows(rejected)

    print(f"{len(index)} pairs written, {len(rejected)} attempts not injected")
    for did in INJECTORS:
        n = sum(1 for r in index if r["defect_id"] == did)
        print(f"  {did:<32} {n:4d} pairs")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--coverage", metavar="DIR")
    a = ap.parse_args()
    if a.selftest:
        selftest()
    elif a.coverage:
        coverage(a.coverage)
    else:
        build()


if __name__ == "__main__":
    main()
