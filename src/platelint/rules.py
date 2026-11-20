"""Rule checkers for plate-based assay requests.

Extracted unchanged from 06_check.py so the research pipeline and the command
line tool run the same code. Standard library only.
"""

import re


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
            hits.append(f"one step both overnight and timed ({sorted(durs)[0][0]} units)")
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
def check_rules(text):
    out = {}
    for k, fn in RULES.items():
        r = fn(text)
        if r:
            out[k] = r
    return out

