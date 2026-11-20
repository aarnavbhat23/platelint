---
name: platelint
description: Lint a plain-language plate-assay request (ELISA, qPCR, cell viability, bacterial growth curve) for physical and logical defects before it goes to a lab or a robot. Use when the user pastes or writes an experiment request, protocol or plate-assay plan and wants it checked for impossible volumes, wrong units, missing controls, instrument/readout mismatches, impossible temperatures, missing durations or contradictory step order.
---

# platelint

Rule-based checker for eight defect types. It is advisory: on LLM-written requests
with no injected defect, its rules flagged something 84% of the time, and some rules
are far noisier than others.

## How to run

From a checkout of the platelint repo (no install needed, standard library only):

```bash
PYTHONPATH=src python3 -m platelint check request.txt --explain
echo "<request text>" | PYTHONPATH=src python3 -m platelint check - --format json
PYTHONPATH=src python3 -m platelint rules
```

With `pip install .` the command is just `platelint check ...`. Ask the user before installing.
Exit code 1 means at least one finding; `--exit-zero` disables that.

## How to report results

1. Save the user's request text to a file or pipe it in. Do not rewrite it first.
2. Run the check with `--format json`.
3. For each finding, quote the `evidence`, say why it matters, and read the real text yourself
   before agreeing. The noisy rules (`missing_control`, `missing_required_duration`,
   `temperature_out_of_range`, `conflicting_conditions`) are often false alarms: check the
   sentence in context. The quiet rules (`well_volume_exceeded`, `unit_mismatch`,
   `instrument_readout_mismatch`, `contradictory_ordering`) are more likely real.
4. Never say a request is correct because nothing fired. The tool does not verify protocols.
5. Suggest a concrete fix for each finding you confirm. Do not invent plate formats,
   volumes or controls the user did not state; ask.
