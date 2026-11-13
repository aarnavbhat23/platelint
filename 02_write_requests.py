"""Stage 2: have each model in MODELS rewrite each protocol as a plain-language
request to a wet lab. Raw outputs are saved untouched.

Standard library only. Two providers, both of which issue free API keys:

    google   Google AI Studio   https://aistudio.google.com/apikey   -> GOOGLE_API_KEY
    groq     Groq              https://console.groq.com/keys        -> GROQ_API_KEY

Usage:
    GOOGLE_API_KEY=... GROQ_API_KEY=... python3 02_write_requests.py --list-models
    GOOGLE_API_KEY=... GROQ_API_KEY=... python3 02_write_requests.py --probe 2
    GOOGLE_API_KEY=... GROQ_API_KEY=... python3 02_write_requests.py

Model ids are not hardcoded guesses: run --list-models, then put the ids you
want in MODELS below. --probe runs a couple of protocols and reports measured
token use and how long the full run will take under each free-tier rate limit.

The run is resumable. A protocol whose output file already exists is skipped, so
a 429 or a dropped connection costs only the requests that had not finished.

The prompt is identical for every model and says nothing about volumes, units,
controls or instruments: the point is to measure the defects models produce
unprompted. Temperature is left at each provider's default and not varied, so
runs are not seed-reproducible; every raw response is stored instead.
"""

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.request

# Fill these in from --list-models output.
MODELS = [
    # {"provider": "google", "model": "gemini-...",  "sleep": 4.0},
    # {"provider": "groq",   "model": "llama-...",   "sleep": 2.0},
]

MAX_OUTPUT_TOKENS = 4096
OUT = "data/requests"

SYSTEM = (
    "You work in a research group that commissions experiments from a contract "
    "wet lab. You write the requests the lab receives."
)

PROMPT = """Below is a published protocol. Rewrite it as a request to the lab, \
asking them to run this experiment on our samples.

Write it the way you would send it: plain language, prose or a short numbered \
list. No headings, no preamble, no commentary about the rewrite itself. Give \
the lab what they need to carry it out.

---

{text}"""


def key_for(provider):
    env = {"google": "GOOGLE_API_KEY", "groq": "GROQ_API_KEY"}[provider]
    k = os.environ.get(env)
    if not k:
        sys.exit(f"{env} is not set (needed for provider '{provider}')")
    return k


def post(url, body, headers, tries=6):
    data = json.dumps(body).encode()
    hdrs = {"content-type": "application/json", **headers}
    for i in range(tries):
        req = urllib.request.Request(url, data=data, headers=hdrs, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:300]
            if e.code in (429, 500, 502, 503, 529) and i < tries - 1:
                # Free tiers rate limit per minute; back off well past a minute.
                wait = min(90, 5 * 2 ** i)
                retry_after = e.headers.get("retry-after")
                if retry_after and retry_after.isdigit():
                    wait = max(wait, int(retry_after))
                print(f"    HTTP {e.code}, waiting {wait}s: {detail[:120]}", flush=True)
                time.sleep(wait)
                continue
            raise RuntimeError(f"HTTP {e.code}: {detail}") from None
        except urllib.error.URLError as e:
            if i < tries - 1:
                time.sleep(5 * 2 ** i)
                continue
            raise RuntimeError(f"connection failed: {e}") from None
    raise RuntimeError("unreachable")


def get(url, headers):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def call_google(model, text):
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/{model}"
           f":generateContent?key={key_for('google')}")
    body = {
        "systemInstruction": {"parts": [{"text": SYSTEM}]},
        "contents": [{"role": "user", "parts": [{"text": PROMPT.format(text=text)}]}],
        "generationConfig": {"maxOutputTokens": MAX_OUTPUT_TOKENS},
    }
    d = post(url, body, {})
    cands = d.get("candidates") or []
    out = ""
    finish = ""
    if cands:
        finish = cands[0].get("finishReason", "")
        for p in (cands[0].get("content") or {}).get("parts") or []:
            out += p.get("text", "")
    u = d.get("usageMetadata") or {}
    return {
        "text": out,
        "finish_reason": finish or d.get("promptFeedback", {}).get("blockReason", ""),
        "input_tokens": u.get("promptTokenCount", 0),
        "output_tokens": u.get("candidatesTokenCount", 0),
        "raw": d,
    }


def call_groq(model, text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    body = {
        "model": model,
        "max_tokens": MAX_OUTPUT_TOKENS,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": PROMPT.format(text=text)},
        ],
    }
    d = post(url, body, {"authorization": "Bearer " + key_for("groq")})
    ch = (d.get("choices") or [{}])[0]
    u = d.get("usage") or {}
    return {
        "text": (ch.get("message") or {}).get("content") or "",
        "finish_reason": ch.get("finish_reason", ""),
        "input_tokens": u.get("prompt_tokens", 0),
        "output_tokens": u.get("completion_tokens", 0),
        "raw": d,
    }


CALL = {"google": call_google, "groq": call_groq}


def list_models():
    if os.environ.get("GOOGLE_API_KEY"):
        d = get("https://generativelanguage.googleapis.com/v1beta/models"
                f"?key={key_for('google')}", {})
        print("google (Google AI Studio):")
        for m in d.get("models", []):
            if "generateContent" in (m.get("supportedGenerationMethods") or []):
                print(f"  {m['name'].removeprefix('models/'):<45} "
                      f"in={m.get('inputTokenLimit')} out={m.get('outputTokenLimit')}")
    else:
        print("google: GOOGLE_API_KEY not set, skipping")
    if os.environ.get("GROQ_API_KEY"):
        d = get("https://api.groq.com/openai/v1/models",
                {"authorization": "Bearer " + key_for("groq")})
        print("\ngroq:")
        for m in sorted(d.get("data", []), key=lambda x: x["id"]):
            print(f"  {m['id']:<45} context={m.get('context_window')}")
    else:
        print("\ngroq: GROQ_API_KEY not set, skipping")


def tag(spec):
    return (spec["provider"] + "_" + spec["model"]).replace("/", "-").replace(".", "")


def out_path(spec, protocol_id):
    return os.path.join(OUT, tag(spec), protocol_id + ".txt")


def run_one(spec, row):
    with open(row["text_path"]) as f:
        text = f.read()
    res = CALL[spec["provider"]](spec["model"], text)
    d = os.path.join(OUT, tag(spec))
    os.makedirs(d, exist_ok=True)
    with open(out_path(spec, row["id"]), "w") as f:
        f.write(res["text"])
    os.makedirs(os.path.join(OUT, "raw", tag(spec)), exist_ok=True)
    with open(os.path.join(OUT, "raw", tag(spec), row["id"] + ".json"), "w") as f:
        json.dump(res["raw"], f)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list-models", action="store_true",
                    help="print the model ids each key can reach, then exit")
    ap.add_argument("--probe", type=int, metavar="N",
                    help="run N protocols per model and report measured usage")
    a = ap.parse_args()

    if a.list_models:
        list_models()
        return
    if not MODELS:
        sys.exit("MODELS is empty: run --list-models, then fill in MODELS in this file")

    with open("data/sources_all.csv") as f:
        rows = list(csv.DictReader(f))
    if a.probe:
        rows = rows[:a.probe]
    print(f"{len(rows)} protocols x {len(MODELS)} models = {len(rows)*len(MODELS)} requests")

    usage_rows, failures = [], []
    for spec in MODELS:
        done = skipped = 0
        for row in rows:
            if os.path.exists(out_path(spec, row["id"])) and not a.probe:
                skipped += 1
                continue
            try:
                res = run_one(spec, row)
            except Exception as e:
                failures.append((tag(spec), row["id"], str(e)[:200]))
                print(f"  FAILED {tag(spec)} {row['id']}: {str(e)[:160]}", flush=True)
                continue
            done += 1
            usage_rows.append({
                "provider": spec["provider"], "model": spec["model"],
                "protocol_id": row["id"],
                "input_tokens": res["input_tokens"], "output_tokens": res["output_tokens"],
                "finish_reason": res["finish_reason"], "n_chars": len(res["text"]),
            })
            flag = "" if res["text"].strip() else "  EMPTY OUTPUT"
            print(f"  {tag(spec):<34} {row['id']:<32} in {res['input_tokens']:6d} "
                  f"out {res['output_tokens']:6d} {res['finish_reason']}{flag}", flush=True)
            time.sleep(spec.get("sleep", 2.0))
        print(f"{tag(spec)}: wrote {done}, skipped {skipped} already present")

    if usage_rows:
        path = os.path.join(OUT, "usage_probe.csv" if a.probe else "usage.csv")
        write_header = not os.path.exists(path) or a.probe
        with open(path, "a" if not write_header else "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(usage_rows[0].keys()))
            if write_header:
                w.writeheader()
            w.writerows(usage_rows)
        print(f"\nusage written to {path}")

        if a.probe:
            with open("data/sources_all.csv") as f:
                n_all = sum(1 for _ in csv.DictReader(f))
            print(f"\nprojected for {n_all} protocols per model:")
            for spec in MODELS:
                us = [u for u in usage_rows if u["model"] == spec["model"]]
                if not us:
                    continue
                ai = sum(u["input_tokens"] for u in us) / len(us)
                ao = sum(u["output_tokens"] for u in us) / len(us)
                mins = n_all * spec.get("sleep", 2.0) / 60
                print(f"  {spec['model']:<40} in {ai:7.0f}/req  out {ao:6.0f}/req  "
                      f"{ai*n_all/1e6:.2f}M input tokens, >= {mins:.0f} min at "
                      f"{spec.get('sleep', 2.0)}s spacing")

    empty = [u for u in usage_rows if u["n_chars"] == 0]
    if empty:
        print(f"\n{len(empty)} requests returned no text:")
        for u in empty[:10]:
            print(f"  {u['model']} {u['protocol_id']} finish_reason={u['finish_reason']}")
    if failures:
        print(f"\n{len(failures)} requests failed outright:")
        for t, pid, err in failures[:10]:
            print(f"  {t} {pid}: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
