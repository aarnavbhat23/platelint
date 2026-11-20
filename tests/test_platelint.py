import importlib.util
import json
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

from platelint import TAXONOMY, check  # noqa: E402
from platelint.rules import RULES  # noqa: E402

CLEAN = ("ELISA in a 96-well plate. Coat with 100 uL of capture antibody per well overnight at 4 C. "
         "Block with 200 uL of 1% BSA per well for 1 hour at 37 C. Include a blank and a standard curve. "
         "Read absorbance at 450 nm on an absorbance reader.")

CASES = {
    "well_volume_exceeded": CLEAN.replace("200 uL", "500 uL"),
    "conflicting_conditions": CLEAN.replace("for 1 hour at 37 C", "for 1 hour at 37 C and 4 C"),
    "missing_control": CLEAN.replace("Include a blank and a standard curve. ", ""),
    "unit_mismatch": CLEAN.replace("100 uL", "100 mL"),
    "instrument_readout_mismatch": CLEAN.replace("absorbance at 450 nm on an absorbance reader",
                                                  "luminescence on a spectrophotometer"),
    "temperature_out_of_range": CLEAN.replace("for 1 hour at 37 C", "for 1 hour at 95 C"),
    "missing_required_duration": CLEAN.replace(" for 1 hour", ""),
}


def ids(text):
    return {f["id"] for f in check(text)}


class Rules(unittest.TestCase):
    def test_each_defect_is_flagged(self):
        for did, text in CASES.items():
            with self.subTest(did):
                self.assertIn(did, ids(text))

    def test_clean_fixture_has_no_defect_it_was_edited_for(self):
        self.assertEqual(ids(CLEAN) & set(CASES), set())

    def test_every_rule_has_taxonomy_entry(self):
        self.assertEqual(set(RULES), set(TAXONOMY))

    def test_ordering_rule(self):
        t = CLEAN + " Read the plate before adding the stop solution."
        self.assertIn("contradictory_ordering", ids(t))

    def test_finding_shape(self):
        f = check(CASES["well_volume_exceeded"])[0]
        for k in ("id", "name", "evidence", "objection", "false_alarm_upper_bound_pct"):
            self.assertIn(k, f)


class Taxonomy(unittest.TestCase):
    def test_matches_research_pipeline(self):
        s = importlib.util.spec_from_file_location("defects", os.path.join(ROOT, "03_defects.py"))
        m = importlib.util.module_from_spec(s)
        s.loader.exec_module(m)
        src = {d["id"]: (d["name"], d["objection"]) for d in m.DEFECTS}
        mine = {k: (v["name"], v["objection"]) for k, v in TAXONOMY.items()}
        self.assertEqual(src, mine)


class Cli(unittest.TestCase):
    def run_cli(self, *args, stdin=""):
        env = dict(os.environ, PYTHONPATH=os.path.join(ROOT, "src"))
        return subprocess.run([sys.executable, "-m", "platelint", *args], input=stdin,
                              capture_output=True, text=True, env=env)

    def test_json_and_exit_code(self):
        r = self.run_cli("check", "-", "--format", "json", stdin=CASES["missing_control"])
        self.assertEqual(r.returncode, 1)
        d = json.loads(r.stdout)
        self.assertIn("missing_control", {f["id"] for f in d["findings"]})
        self.assertIn("caution", d)

    def test_exit_zero_flag(self):
        r = self.run_cli("check", "-", "--exit-zero", "--quiet", stdin=CASES["missing_control"])
        self.assertEqual(r.returncode, 0)

    def test_rules_listing(self):
        r = self.run_cli("rules")
        self.assertEqual(r.returncode, 0)
        self.assertIn("contradictory_ordering", r.stdout)


if __name__ == "__main__":
    unittest.main()
