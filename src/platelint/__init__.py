"""platelint: advisory checks for plain-language plate-assay requests."""

from .rules import RULES, WELL_MAX_UL, check_rules
from .taxonomy import TAXONOMY

__version__ = "0.1.0"
__all__ = ["RULES", "TAXONOMY", "WELL_MAX_UL", "check_rules", "check", "__version__"]


def check(text):
    """Return a list of findings: dicts with id, name, evidence, objection and
    false_alarm_upper_bound_pct. Empty list means no rule fired, not that the
    request is correct."""
    out = []
    for did, why in check_rules(text).items():
        t = TAXONOMY[did]
        out.append({"id": did, "name": t["name"], "evidence": why,
                    "objection": t["objection"],
                    "false_alarm_upper_bound_pct": t["false_alarm_upper_bound_pct"]})
    return out
