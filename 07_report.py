"""Stage 7: the tables and the figure. Every number here is computed from files
in results/ and data/; nothing is entered by hand.

    python3 07_report.py

Writes, into results/:
    table_detection.csv / .md          detection rate per defect type per checker
    table_false_positives.csv / .md    false-positive rate on clean requests
    table_defect_rate_by_model.csv     defect rate per model, from the hand labels
    figure_detection.svg               the one figure the README opens with
    summary.json                       the headline numbers, for quoting

Intervals are Wilson score intervals at 95%. They are wide where n is small,
which is the point of printing n in every row.

The tuning/test split is by source protocol, assigned by hashing the protocol
id, so a protocol's requests are all on the same side of the split and no
protocol is in both. Reported numbers are the test split. Tuning numbers are
printed too, so the gap between them is visible rather than hidden.
"""

import csv
import hashlib
import importlib.util
import json
import math
import os
import sys

RESULTS = "results"
TUNING_FRACTION = 0.30
SPLIT_SALT = "runnability-benchmark-split-v1"

_s = importlib.util.spec_from_file_location("defects", "03_defects.py")
_d = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_d)
DEFECTS = _d.DEFECTS
DEFECT_IDS = [d["id"] for d in DEFECTS]
CAVEATS = {d["id"]: d.get("caveat", "") for d in DEFECTS}

CHECKERS = ["keyword", "rules", "llm"]


def split_of(protocol_id):
    h = hashlib.sha256((SPLIT_SALT + "|" + protocol_id).encode()).digest()
    frac = int.from_bytes(h[:8], "big") / 2 ** 64
    return "tuning" if frac < TUNING_FRACTION else "test"


def wilson(k, n, z=1.96):
    """Wilson score interval. Returns (point, lo, hi) as fractions."""
    if n == 0:
        return (float("nan"),) * 3
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, max(0.0, centre - half), min(1.0, centre + half)


def pct(x):
    return "-" if x != x else f"{100*x:.1f}"


def ci_str(k, n):
    if n == 0:
        return "n=0"
    p, lo, hi = wilson(k, n)
    return f"{pct(p)}% [{pct(lo)}-{pct(hi)}] {k}/{n}"


def load_checks():
    out = {}
    for c in CHECKERS:
        path = os.path.join(RESULTS, f"checks_{c}.csv")
        if not os.path.exists(path):
            continue
        with open(path) as f:
            rows = list(csv.DictReader(f))
        for r in rows:
            r["split"] = split_of(r["protocol_id"])
            r["n_flags"] = int(r["n_flags"])
            for d in DEFECT_IDS:
                r["flag_" + d] = int(r["flag_" + d])
        out[c] = rows
    return out


def detection_table(checks, split):
    rows = []
    for d in DEFECT_IDS:
        row = {"defect_id": d, "split": split}
        for c in CHECKERS:
            sub = [r for r in checks.get(c, []) if r["true_defect"] == d and r["split"] == split]
            n = len(sub)
            k_exact = sum(r["flag_" + d] for r in sub)
            k_any = sum(1 for r in sub if r["n_flags"])
            p, lo, hi = wilson(k_exact, n)
            row[f"{c}_n"] = n
            row[f"{c}_exact_k"] = k_exact
            row[f"{c}_exact_pct"] = pct(p)
            row[f"{c}_exact_lo"] = pct(lo)
            row[f"{c}_exact_hi"] = pct(hi)
            row[f"{c}_any_k"] = k_any
            row[f"{c}_any_pct"] = pct(wilson(k_any, n)[0])
        row["caveat"] = CAVEATS[d]
        rows.append(row)
    return rows


def fp_table(checks, split):
    rows = []
    for c in CHECKERS:
        clean = [r for r in checks.get(c, []) if not r["true_defect"] and r["split"] == split]
        n = len(clean)
        k = sum(1 for r in clean if r["n_flags"])
        p, lo, hi = wilson(k, n)
        row = {"checker": c, "split": split, "n_clean": n, "flagged": k,
               "fp_pct": pct(p), "fp_lo": pct(lo), "fp_hi": pct(hi)}
        for d in DEFECT_IDS:
            kd = sum(r["flag_" + d] for r in clean)
            row["fp_" + d] = pct(wilson(kd, n)[0]) if n else "-"
        rows.append(row)
    return rows


def model_table():
    """Defect rate per model, from the hand labels. No labels, no table."""
    path = os.path.join("data", "labels.csv")
    if not os.path.exists(path):
        return None, f"{path} not found"
    with open(path) as f:
        rows = list(csv.DictReader(f))
    need = {"item_id", "model_tag", "label"}
    missing = need - set(rows[0].keys() if rows else [])
    if missing:
        return None, f"{path} is missing columns: {sorted(missing)}"
    labelled = [r for r in rows if (r.get("label") or "").strip()]
    if not labelled:
        return None, f"{path} has no filled-in labels yet"
    out = []
    for tag in sorted({r["model_tag"] for r in labelled}):
        sub = [r for r in labelled if r["model_tag"] == tag]
        k = sum(1 for r in sub if r["label"].strip().lower()
                not in ("ok", "clean", "runnable", "0", "no"))
        p, lo, hi = wilson(k, len(sub))
        out.append({"model_tag": tag, "n_labelled": len(sub), "n_with_defect": k,
                    "defect_rate_pct": pct(p), "lo": pct(lo), "hi": pct(hi)})
    return out, ""


def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def write_md(path, header, rows):
    with open(path, "w") as f:
        f.write("| " + " | ".join(header) + " |\n")
        f.write("|" + "|".join("---" for _ in header) + "|\n")
        for r in rows:
            f.write("| " + " | ".join(r) + " |\n")


BG, FG, GRID = "#ffffff", "#1f2328", "#d8dee4"
COLOURS = {"keyword": "#9a6700", "rules": "#0969da", "llm": "#1a7f37"}


def svg_figure(path, det_rows, present):
    """Horizontal grouped bars with Wilson whiskers. Written by hand so the
    repo needs no plotting dependency. Explicit white background so it reads
    the same in light and dark GitHub themes."""
    left, top, bar_h, gap, group_gap = 230, 54, 13, 3, 14
    plot_w = 430
    n_groups = len(det_rows)
    group_h = len(present) * (bar_h + gap) + group_gap
    height = top + n_groups * group_h + 46
    width = left + plot_w + 70

    def x(frac):
        return left + plot_w * frac

    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
         f'viewBox="0 0 {width} {height}" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">',
         f'<rect width="{width}" height="{height}" fill="{BG}"/>',
         f'<text x="16" y="24" font-size="14" font-weight="600" fill="{FG}">'
         f'Detection rate by defect type (test split)</text>',
         f'<text x="16" y="42" font-size="11" fill="#656d76">'
         f'bars: flagged the injected type; whiskers: 95% Wilson interval; n printed per bar</text>']

    for gx in (0, 0.25, 0.5, 0.75, 1.0):
        p.append(f'<line x1="{x(gx):.1f}" y1="{top}" x2="{x(gx):.1f}" y2="{height-34}" '
                 f'stroke="{GRID}" stroke-width="1"/>')
        p.append(f'<text x="{x(gx):.1f}" y="{height-18}" font-size="10" fill="#656d76" '
                 f'text-anchor="middle">{int(gx*100)}%</text>')

    y = top
    for row in det_rows:
        label = row["defect_id"]
        p.append(f'<text x="{left-10}" y="{y + (len(present)*(bar_h+gap))/2 + 4:.0f}" '
                 f'font-size="11" fill="{FG}" text-anchor="end">{label}</text>')
        for c in present:
            n = row[f"{c}_n"]
            if n == 0:
                p.append(f'<text x="{left+6}" y="{y+bar_h-2}" font-size="10" '
                         f'fill="#656d76">no pairs</text>')
                y += bar_h + gap
                continue
            k = row[f"{c}_exact_k"]
            pt, lo, hi = wilson(k, n)
            p.append(f'<rect x="{left}" y="{y}" width="{plot_w*pt:.1f}" height="{bar_h}" '
                     f'fill="{COLOURS[c]}" opacity="0.85"/>')
            p.append(f'<line x1="{x(lo):.1f}" y1="{y+bar_h/2:.1f}" x2="{x(hi):.1f}" '
                     f'y2="{y+bar_h/2:.1f}" stroke="{FG}" stroke-width="1"/>')
            for xx in (lo, hi):
                p.append(f'<line x1="{x(xx):.1f}" y1="{y+2}" x2="{x(xx):.1f}" '
                         f'y2="{y+bar_h-2}" stroke="{FG}" stroke-width="1"/>')
            p.append(f'<text x="{x(hi)+6:.1f}" y="{y+bar_h-2}" font-size="10" '
                     f'fill="#656d76">{100*pt:.0f}% n={n}</text>')
            y += bar_h + gap
        y += group_gap

    lx = left
    for c in present:
        p.append(f'<rect x="{lx}" y="{height-32}" width="10" height="10" '
                 f'fill="{COLOURS[c]}" opacity="0.85"/>')
        p.append(f'<text x="{lx+14}" y="{height-23}" font-size="10" fill="{FG}">{c}</text>')
        lx += 70
    p.append("</svg>")
    with open(path, "w") as f:
        f.write("\n".join(p))


def main():
    checks = load_checks()
    if not checks:
        sys.exit("no results/checks_*.csv found -- run 06_check.py first "
                 "(which needs the paired set from 04_make_pairs.py, "
                 "which needs the requests from 02_write_requests.py)")
    present = [c for c in CHECKERS if c in checks]
    missing = [c for c in CHECKERS if c not in checks]
    os.makedirs(RESULTS, exist_ok=True)

    print(f"checkers with results: {', '.join(present)}")
    if missing:
        print(f"checkers not run: {', '.join(missing)} (left out of every table)")

    counts = {}
    for c in present:
        for s in ("tuning", "test"):
            counts[(c, s)] = sum(1 for r in checks[c] if r["split"] == s)
    n_protocols = len({r["protocol_id"] for r in checks[present[0]]})
    n_test_prot = len({r["protocol_id"] for r in checks[present[0]] if r["split"] == "test"})
    print(f"\n{n_protocols} source protocols: {n_test_prot} test, "
          f"{n_protocols-n_test_prot} tuning "
          f"({int(100*TUNING_FRACTION)}% tuning by protocol-id hash)")

    for split in ("test", "tuning"):
        det = detection_table(checks, split)
        print(f"\n=== detection, {split} split "
              f"(flagged the injected type; 95% Wilson) ===")
        head = f"{'defect':<32}" + "".join(f"{c:>28}" for c in present)
        print(head)
        for row in det:
            line = f"  {row['defect_id']:<30}"
            for c in present:
                line += f"{ci_str(row[f'{c}_exact_k'], row[f'{c}_n']):>28}"
            print(line)
        if split == "test":
            write_csv(os.path.join(RESULTS, "table_detection.csv"), det)
            write_md(os.path.join(RESULTS, "table_detection.md"),
                     ["defect type"] + [f"{c} (exact, 95% CI, n)" for c in present],
                     [[r["defect_id"]] + [ci_str(r[f"{c}_exact_k"], r[f"{c}_n"])
                                          for c in present] for r in det])
            svg_figure(os.path.join(RESULTS, "figure_detection.svg"), det, present)

        fps = fp_table(checks, split)
        print(f"\n=== false positives on clean requests, {split} split ===")
        for r in fps:
            print(f"  {r['checker']:<10} {ci_str(r['flagged'], r['n_clean']):>28}"
                  f"   (any flag on a clean request)")
        if split == "test":
            write_csv(os.path.join(RESULTS, "table_false_positives.csv"), fps)
            write_md(os.path.join(RESULTS, "table_false_positives.md"),
                     ["checker", "false-positive rate on clean requests (95% CI, n)"],
                     [[r["checker"], ci_str(r["flagged"], r["n_clean"])] for r in fps])

    mt, why = model_table()
    print("\n=== defect rate per model, from the hand labels ===")
    if mt is None:
        print(f"  not computed: {why}")
        print("  (stage 5 produces the labelling sheet; this table stays empty "
              "until you have filled it in)")
    else:
        for r in mt:
            print(f"  {r['model_tag']:<28} {r['defect_rate_pct']}% "
                  f"[{r['lo']}-{r['hi']}] {r['n_with_defect']}/{r['n_labelled']}")
        write_csv(os.path.join(RESULTS, "table_defect_rate_by_model.csv"), mt)

    det_test = detection_table(checks, "test")
    summary = {
        "n_source_protocols": n_protocols,
        "n_test_protocols": n_test_prot,
        "tuning_fraction": TUNING_FRACTION,
        "checkers_run": present,
        "checkers_not_run": missing,
        "items_per_checker_split": {f"{c}/{s}": counts[(c, s)]
                                    for c in present for s in ("tuning", "test")},
        "detection_test": {
            r["defect_id"]: {c: {"k": r[f"{c}_exact_k"], "n": r[f"{c}_n"],
                                 "pct": r[f"{c}_exact_pct"],
                                 "ci": [r[f"{c}_exact_lo"], r[f"{c}_exact_hi"]]}
                             for c in present}
            for r in det_test},
        "false_positives_test": {r["checker"]: {"k": r["flagged"], "n": r["n_clean"],
                                                "pct": r["fp_pct"],
                                                "ci": [r["fp_lo"], r["fp_hi"]]}
                                 for r in fp_table(checks, "test")},
        "defect_rate_by_model": mt,
        "defect_rate_by_model_note": why,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nwrote {RESULTS}/table_detection.csv, table_false_positives.csv, "
          f"figure_detection.svg, summary.json")


if __name__ == "__main__":
    main()
