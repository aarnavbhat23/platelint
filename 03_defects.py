"""Stage 3: defect taxonomy. Edit this list before stage 4 uses it.

Each entry is one kind of mistake a bench scientist would reject outright, not
a style complaint. Fields:

  id          short slug, used as a column name in results/
  name        what to call it in the README
  objection   why a scientist sends the request back
  detectable  what a checker has to parse to catch it
  injection   how 04_make_pairs.py creates exactly this defect in a clean request

Keep the objections concrete. "Vague" and "underspecified" are not defects here
-- a defect has to make the request impossible or wrong to run as written.
"""

DEFECTS = [
    {
        "id": "well_volume_exceeded",
        "name": "Volume exceeds well capacity",
        "objection": "The liquid does not fit. A 96-well flat-bottom plate holds "
                     "about 360 uL per well, a 384-well about 112 uL; the request "
                     "asks the lab to put more than that in one well.",
        "detectable": "Sum the per-well volumes added across steps, compare with "
                      "the capacity of the named plate format.",
        "injection": "Scale one per-well volume up past the format's maximum, or "
                     "switch the plate format down (96 -> 384) leaving volumes alone.",
    },
    {
        "id": "conflicting_conditions",
        "name": "Conflicting incubation conditions",
        "objection": "The same step carries two conditions that cannot both hold: "
                     "37 C and 4 C, or 1 hour and overnight.",
        "detectable": "Two temperature or two duration values attached to one step.",
        "injection": "Add a second, contradictory temperature or duration to a step "
                     "that already states one.",
    },
    {
        "id": "missing_control",
        "name": "Required control missing",
        "objection": "The readout cannot be interpreted: no no-template control for "
                     "qPCR, no vehicle or untreated arm for viability, no blank for ELISA.",
        "detectable": "Assay class implies a required control; no mention of it survives "
                      "in the request.",
        "injection": "Delete the sentence naming the control, leaving the rest intact.",
    },
    {
        "id": "unit_mismatch",
        "name": "Unit mismatch or wrong magnitude",
        "objection": "The quantity is off by orders of magnitude or in the wrong "
                     "dimension: mL where uL was meant, mg/mL for a working antibody "
                     "dilution, nm where nM was meant.",
        "detectable": "Parse number plus unit, compare against the plausible range for "
                      "that quantity type.",
        "injection": "Swap a unit for its neighbour (uL <-> mL, ug <-> mg, nM <-> nm) "
                     "without changing the number.",
    },
    {
        "id": "instrument_readout_mismatch",
        "name": "Named instrument cannot produce the readout",
        "objection": "The request names an instrument and asks it for a signal it does "
                     "not measure: luminescence from an absorbance-only reader, 450 nm "
                     "absorbance from a thermocycler.",
        "detectable": "Instrument name and readout type both appear; the pair is "
                      "incompatible.",
        "injection": "Replace the readout with one the named instrument cannot produce, "
                     "or rename the instrument to one that cannot do the stated readout.",
    },
    {
        "id": "temperature_out_of_range",
        "name": "Temperature outside the workable range",
        "objection": "The step cannot be run: live cells at 95 C, an antibody incubation "
                     "at -80 C, an enzyme step above its denaturation point.",
        "detectable": "Temperature value against a per-step-type allowed range.",
        "injection": "Replace a stated temperature with one outside the range for that "
                     "step type.",
    },
    {
        "id": "plate_capacity_exceeded",
        "name": "More wells needed than the plate has",
        "objection": "Samples times replicates, plus controls and the dilution series, "
                     "exceeds the wells available on the plate the request specifies.",
        "detectable": "Multiply sample count, replicate count and dilution points; "
                      "compare with the format's well count.",
        "injection": "Raise the sample or replicate count past what the named format holds.",
    },
    {
        "id": "timing_impossible",
        "name": "Impossible or missing timing",
        "objection": "The schedule cannot be executed: a reading taken immediately after "
                     "an overnight step, cycling with no cycle count, a wash with no "
                     "incubation where one is required.",
        "detectable": "Ordering and duration of steps; essential duration absent.",
        "injection": "Delete an essential duration, or insert an ordering that contradicts "
                     "a stated one.",
    },
]

# Candidates considered and left out, so the choice is on the record rather than
# implicit. Swap one in if you prefer it to something above.
#
#   reagent_concentration_implausible -- antibody used neat, 10 M NaCl. Overlaps
#       unit_mismatch in most real cases.
#   wavelength_wrong_for_dye -- MTT formazan read at 450 nm instead of 570 nm.
#       A narrow special case of instrument_readout_mismatch.
#   centrifuge_speed_unit -- rpm given where g was meant. Real, but rare in
#       plate-based assays, which is the scope here.

if __name__ == "__main__":
    print(f"{len(DEFECTS)} defect types\n")
    for d in DEFECTS:
        print(f"{d['id']}\n  {d['name']}\n  objection:  {d['objection']}\n"
              f"  detectable: {d['detectable']}\n  injection:  {d['injection']}\n")
