"""Command line: platelint check FILE   |   cat request.txt | platelint check -"""

import argparse
import json
import sys

from . import TAXONOMY, __version__, check

CAUTION = ("platelint is an advisory linter. On un-injected LLM-written requests its rules "
           "flagged something 84% of the time, so treat each finding as a prompt to look, "
           "not a verdict. 'noise' is the measured share of such requests a rule flagged.")


def _read(path):
    return sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()


def cmd_check(a):
    findings = []
    for path in a.files:
        for f in check(_read(path)):
            f["file"] = "<stdin>" if path == "-" else path
            findings.append(f)
    if a.format == "json":
        print(json.dumps({"version": __version__, "caution": CAUTION, "findings": findings}, indent=2))
    else:
        for f in findings:
            print(f"{f['file']}: {f['id']}: {f['evidence']}  [noise {f['false_alarm_upper_bound_pct']:g}%]")
            if a.explain:
                print(f"    why it matters: {f['objection']}")
        if not findings:
            print("no rule fired (this does not mean the request is correct)")
        elif not a.quiet:
            print(f"\n{len(findings)} finding(s). {CAUTION}", file=sys.stderr)
    return 0 if a.exit_zero or not findings else 1


def cmd_rules(a):
    for did, t in TAXONOMY.items():
        print(f"{did:30} noise {t['false_alarm_upper_bound_pct']:>5g}%  {t['name']}")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="platelint", description=__doc__)
    p.add_argument("--version", action="version", version=__version__)
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="lint one or more request files ('-' reads stdin)")
    c.add_argument("files", nargs="+")
    c.add_argument("--format", choices=["text", "json"], default="text")
    c.add_argument("--explain", action="store_true", help="print why each defect matters")
    c.add_argument("--quiet", action="store_true", help="omit the caution footer")
    c.add_argument("--exit-zero", action="store_true", help="exit 0 even when findings exist")
    c.set_defaults(fn=cmd_check)
    r = sub.add_parser("rules", help="list rules with measured noise")
    r.set_defaults(fn=cmd_rules)
    a = p.parse_args(argv)
    return a.fn(a)
