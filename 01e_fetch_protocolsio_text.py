"""Stage 1e: fetch protocols.io step text through the API.

Needs a protocols.io token in the environment (Settings > Developer on
protocols.io). The token is never stored in this repo:

    PROTOCOLS_IO_TOKEN=... python3 01e_fetch_protocolsio_text.py

The rendered protocols.io page lazy-loads steps, so scraping it returns only
the first few; the API returns all of them.
"""

import csv
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

API = "https://www.protocols.io/api/v3/protocols/{slug}"
SLEEP = 0.4
RAW = "data/raw_pio"
OUT = "data/protocols_io"

# Component types we turn into text. Anything else is counted and reported so
# content cannot vanish silently.
TYPE_DESCRIPTION = 1
TYPE_SECTION = 6


def strip_html(s):
    s = re.sub(r"<br\s*/?>", "\n", s or "")
    s = re.sub(r"</(?:p|div|li|tr)>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    return re.sub(r"\n\s*\n+", "\n", s).strip()


def fetch(slug, token):
    path = os.path.join(RAW, re.sub(r"[^A-Za-z0-9]+", "_", slug) + ".json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    req = urllib.request.Request(
        API.format(slug=slug),
        headers={"Authorization": "Bearer " + token,
                 "User-Agent": "protocol-runnability-benchmark/1.0"},
    )
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                d = json.loads(r.read())
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and i < 3:
                time.sleep(2 ** i * 2)
                continue
            raise
    os.makedirs(RAW, exist_ok=True)
    with open(path, "w") as f:
        json.dump(d, f)
    time.sleep(SLEEP)
    return d


def main():
    token = os.environ.get("PROTOCOLS_IO_TOKEN")
    if not token:
        sys.exit("PROTOCOLS_IO_TOKEN is not set; see the docstring")

    os.makedirs(OUT, exist_ok=True)
    with open("data/sources_protocolsio.csv") as f:
        rows = list(csv.DictReader(f))

    unhandled = {}
    report = []
    for r in rows:
        slug = r["doi"].split("protocols.io.", 1)[-1]
        try:
            d = fetch(slug, token)
        except Exception as e:
            report.append((r["id"], 0, f"fetch failed: {e}"))
            continue
        if d.get("status_code") != 0 or not d.get("protocol"):
            report.append((r["id"], 0, f"api status {d.get('status_code')}: {d.get('error_message','')}"))
            continue
        p = d["protocol"]

        blocks = []
        desc = strip_html(p.get("description") or "")
        if desc:
            blocks.append("ABSTRACT\n" + desc)
        for field, label in (("materials_text", "MATERIALS"),
                             ("before_start", "BEFORE START"),
                             ("guidelines", "GUIDELINES")):
            v = strip_html(p.get(field) or "")
            if v:
                blocks.append(label + "\n" + v)

        n_steps = 0
        step_lines = []
        for s in p.get("steps") or []:
            n_steps += 1
            head = str(s.get("number") or n_steps)
            body = []
            for c in s.get("components") or []:
                tid = c.get("type_id")
                src = c.get("source")
                if tid == TYPE_DESCRIPTION and isinstance(src, dict):
                    body.append(strip_html(src.get("description") or ""))
                elif tid == TYPE_SECTION and isinstance(src, dict):
                    t = strip_html(src.get("title") or "")
                    if t:
                        step_lines.append("## " + t)
                else:
                    unhandled[tid] = unhandled.get(tid, 0) + 1
                    if isinstance(src, dict):
                        for k in ("description", "body", "text", "title", "name"):
                            v = strip_html(str(src.get(k) or ""))
                            if v:
                                body.append(v)
                                break
            dur = s.get("duration") or 0
            txt = " ".join(x for x in body if x).strip()
            if dur:
                txt += f" [step duration: {dur} s]"
            if txt:
                step_lines.append(head + ". " + txt)

        text = "\n\n".join(blocks + ["STEPS\n" + "\n".join(step_lines)])
        with open(os.path.join(OUT, r["id"] + ".txt"), "w") as f:
            f.write(text)
        report.append((r["id"], n_steps, f"{len(text)} chars"))

    ok = sum(1 for _, n, _ in report if n)
    print(f"fetched {ok} of {len(rows)} protocols with at least one step")
    for pid, n, note in report:
        if not n:
            print(f"  no steps: {pid} ({note})")
    if unhandled:
        print("component type_ids kept via generic extraction:",
              dict(sorted(unhandled.items(), key=lambda kv: -kv[1])))


if __name__ == "__main__":
    main()
