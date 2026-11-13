# Labelling sheet

60 requests written by models, model names hidden. Each is a rewrite of one published protocol.

For each one, write on the `label:` line whether a bench scientist could run it as written:

- `ok` if you would run it
- `defect` if you would send it back
- `unsure` if you cannot tell

On `defect_types:` list the ids that apply, comma separated, or leave it blank:

- `well_volume_exceeded`
- `conflicting_conditions`
- `missing_control`
- `unit_mismatch`
- `instrument_readout_mismatch`
- `temperature_out_of_range`
- `missing_required_duration`
- `contradictory_ordering`

Anything not covered by those ids goes in `notes:`. Add ids of your own if you keep meeting the same problem.

---

## 1. R103949  (viability)

```
1. Expand our supplied cell line to 50–60% confluence in a T75 flask or 15 cm dish.

2. Prepare four cell seeding densities based on the literature-recommended standard for this cell line, using 50% increments (one below and two above the standard, e.g., 500, 1000, 1500, and 2000 cells/well).

3. Prepare two media conditions to test: Condition 1 using full-serum media (per standard cell culture recommendations), and Condition 2 using media with 50–80% less serum. Also prepare a small volume of serum-free media for cell resuspension.

4. Harvest the cells using standard trypsinization (3 mL trypsin, incubate ~3 minutes at 37°C, verify detachment, and neutralize with an equal volume of Defined Trypsin Inhibitor). 

5. Pellet the cells by centrifugation at 100–300 x g for 5 minutes, aspirate the supernatant, and resuspend the pellet gently in 2 mL of serum-free media. Count the cells via hemocytometry.

6. Calculate and prepare 3 mL of cell suspension for each combination of seeding density and media condition (replicates of 12 wells per condition).

7. Seed 200 µL of each cell suspension into Greiner 96-well microplates with white opaque walls and clear bottoms (Sigma-Aldrich Cat# M0437-32EA or Greiner Cat# 655098) using an 8-channel p200 pipette. Incubate the plate overnight at 37°C to allow cell attachment.

8. On Day 2, verify cell attachment and expected density differences under a 10x microscope. 

9. Transfer the plate to the IncuCyte ZOOM live-cell imaging system. Set up a 72-hour scan using 4 images per well, phase contrast channel only, a basic analyzer processing definition, and 4-hour scan intervals.

10. After 72 hours, terminate the IncuCyte scan, remove the plate, and allow it to equilibrate to room temperature for approximately 20 minutes.

11. Apply white opaque tape to the bottom of the 96-well plate to prevent luminescence crosstalk.

12. Thaw and equilibrate CellTiter-Glo reagent to room temperature, transfer 10 mL to a reagent reservoir, and add 100 µL of CellTiter-Glo reagent to each well of the 96-well plate using an 8-channel p200 pipette.

13. Read the plate on a GloMax Explorer Multimode Microplate Reader (or compatible luminometer) using the following parameters: orbital shake at 500 cycles/min for 2 minutes (1 mm diameter), incubate in the dark for 10 minutes, and measure luminescence with a 400 ms integration time. Export the resulting luminescence and live-cell confluence data.
```

label: 

defect_types: 

notes: 

---

## 2. R0F9715  (growth_curve)

```
1. Set up 96‑well plates with the liquid growth medium we supplied and inoculate each well with the Aspergillus (or other filamentous fungus) isolates listed in the attached spreadsheet. Use the same plate layout as in the spreadsheet (e.g., A5 in the spreadsheet is A5 on the plate). Include the required number of biological replicates; each replicate must be in a separate file later.

2. Incubate the plates at the temperature and shaking speed specified in our protocol (30 °C, 200 rpm) and record optical density (or other growth read‑out) every 30 minutes for 48 hours using the plate reader. Export the raw read‑outs as tab‑delimited text files, one file per replicate, naming them exactly as follows:  
   plate1‑Rep1.txt, plate1‑Rep2.txt, plate1‑Rep3.txt, plate2‑Rep1.txt … plate5‑Rep3.txt.  
   Ensure the well identifiers in each file match the plate layout (e.g., “A5”) and that the column order is consistent across all files.

3. Using R Studio (Desktop 1.1.463 or later), run the preprocessing script we have attached. Adjust the two header lines of the script to reflect the number of plates and replicates we are using. The script will read the raw text files, merge the replicates, and create the object `myDataList` required for downstream analysis.

4. Install the BEAST R package from CRAN (https://rdrr.io/cran/beast) and load it in the same R session.

5. Run the BEAST analysis on our data:  

   ```R
   library(beast)
   # myDataList should already exist from step 3
   beastRun <- beast(myDataList = myDataList)
   print(beastRun)
   plot(beastRun, fileName = "growth_beast_plot.pdf", timeScale = 1/6,
        xlab = "hours", ylab = "growth")
   ```

   Use the default MCMC settings (70 000 iterations) unless we advise otherwise.

6. Return the following deliverables to us:  

   - The processed R object `myDataList` (saved as an .RData file).  
   - The printed BEAST output (text file).  
   - The PDF file “growth_beast_plot.pdf” containing all growth curves, clustered by change‑point groups and individual curves for each isolate.  
   - A brief note confirming that the plate layout and replicate files matched the naming convention.
```

label: 

defect_types: 

notes: 

---

## 3. R5FBEAD  (qpcr)

```
Please perform the following experiment on our samples:

1. Extract total RNA from each dry cell pellet using the Qiagen RNeasy™ kit exactly as the manufacturer’s instructions say.  Keep the RNA on ice after elution and store at –80 °C if not used immediately.

2. Measure RNA concentration and purity with a Nanodrop.  Record A260/A280 ratios.

3. For each sample, take 600 ng of RNA.  Prepare the genomic‑DNA removal mix on ice:
   - 2 µL gDNA Wipeout Buffer (×7)
   - 5 µL template RNA (adjust so total RNA = 600 ng)
   - Add RNase‑free water to a final volume of 14 µL
   Incubate 2 min at 42 °C, then immediately chill on ice.

4. Prepare the reverse‑transcription master mix on ice (per reaction):
   - 1 µL Quantiscript Reverse Transcriptase
   - 4 µL Quantiscript RT Buffer (5×)
   - 1 µL RT Primer Mix
   Add the 14 µL gDNA‑removal reaction to the master mix, mix, and keep on ice.

5. Incubate the reverse‑transcription reactions as follows:
   - 15 min at 42 °C
   - 3 min at 95 °C to inactivate the enzyme
   Immediately place on ice.  Store aliquots at –20 °C if not used immediately.

6. Set up real‑time qPCR on a 48‑well plate (use a qPCR machine that can read 48‑well plates).  For each well add:
   - 2 µL cDNA
   - 10 µL QuantiTect SYBR Green PCR Master Mix
   - 7 µL RNase‑free water
   - 1 µL primer mix (20 mM forward + reverse, 0.5 µL each)
   Include a mock well where 2 µL RNase‑free water replaces cDNA (blank).  Run all reactions in technical duplicates.

7. PCR program:
   - 95 °C for 10 min (activation)
   - 40 cycles of: 94 °C for 15 s (denature), 58 °C for 30 s (anneal), 72 °C for 30 s (extend)

8. Use the following primer sequences (Eurofins Genomics supplied).  Prepare 20 mM forward and reverse stocks:
   - **GBA1**: forward TGCTGCTCTCAACATCCTTGCC; reverse TAGGTGCGGATGGAGAAGTCAA
   - **SNCA**: forward GCCAAGGAGGGAGTTGTGGCTGC; reverse CTGTTGCCACACCATGCACCACTCC
   - **TH**: forward GCGGTTCATTGGGCGCAGG; reverse CAAACACCTTCACAG
   - **CHOP**: forward ACCAAGGGAGAACCAGGAAACG; reverse TCACCATTCGGTCAATCAGAGC
   - **GAPDH**: forward GAAGGTGAAGGTCGGAGT; reverse GAAGATGGTGATGGGATTTC

9. Perform each experiment three independent times (different cell pellet preparations).  Record C_T values and calculate ΔC_T relative to GAPDH.  Use the ΔΔC_T method to determine fold‑change in expression.

Deliver all raw data and a short summary of results.  If any reagents or steps are unclear, let me know before starting.
```

label: 

defect_types: 

notes: 

---

## 4. RC52E0B  (viability)

```
Please process our supplied dried, powdered aerial parts of Hypericum perforatum L. to extract, purify, and formulate hypericin (Hyp) into a micellar water-soluble form using Pluronic F-127, and then perform analytical characterization, stability testing, and in vitro cell studies according to the following protocol:

1. Perform continuous Soxhlet extraction on 30.0 g of the prepared biomass using 600 mL of chemically pure chloroform (CHCl3) over two consecutive 9-hour cycles, allowing the biomass to dry between cycles and after the final cycle until constant mass is achieved in a fume hood at 20–25 °C.
2. Extract Hyp from the defatted biomass residue using acetone at a 1:4 (w/w) raw material-to-extractant ratio via ultrasonic extraction in an ultrasonic bath at 25 ± 5 °C in the dark over 5 repeated 30-minute cycles, filtering under vacuum and renewing the acetone after each cycle, and concentrating the combined red extracts on a rotary evaporator.
3. Purify the concentrated Hyp by normal-phase column chromatography on silica gel 60 using a gradient elution system of acetone/methanol/dichloromethane (ranging from 1:3:10 to 1:2:20 v/v/v), monitoring separation via TLC (365 nm UV and visible light) and spectrophotometry (absorption maxima at 550 and 590 nm), and recrystallize the combined, concentrated Hyp fractions from hexane.
4. Prepare the micellar water-soluble formulation by dissolving 0.6 mg of the purified Hyp and 80.0 mg of Pluronic F-127 in 2.0 mL of methanol, removing the organic solvent on a rotary evaporator at 36.0 °C and 110 rpm for 30 min to form a uniform dry film, adding 1.919 g of 0.9% sodium chloride solution, subjecting the mixture to ultrasonic hydration at 25 °C for 10 min, resting it in the dark for 1 h, and filtering through a 0.22 μm Millipore membrane filter under aseptic conditions to yield a 0.3 mg/mL solution. Determine the encapsulation efficiency (EE) by measuring Hyp mass in the filtrate versus initial mass.
5. Characterize the micellar emulsion using dynamic light scattering (DLS) on a Zetasizer Nano ZS at 25 °C. Assess emulsion stability by measuring particle size and PDI on days 1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 40, 50, and 60, with storage in the dark at ≤4 °C between time points.
6. Culture GL261 murine glioma cells (in DMEM with L-glutamine, 10% FBS, and 100 U/mL penicillin-streptomycin at 37 °C, 5% CO2) and DF-2 human dermal fibroblasts (in DMEM/F12 under identical conditions).
7. Evaluate Hyp accumulation by seeding GL261 cells in glass-bottom Petri dishes at 5 × 10^5 cells, incubating with 10 μM micellar Hyp for 12 h, washing with Hanks' solution, staining with Hoechst 33342, and imaging using a Nikon Eclipse Ti2 confocal microscope with image processing via Fiji.
8. Assess photoinduced cytotoxicity by seeding GL261 (8 × 10^3 cells/well) and DF-2 (10 × 10^3 cells/well) in 96-well plates, treating with micellar Hyp at concentrations from 0.15 to 40 µM across incubation times of 2, 4, 6, 12, and 24 h, replacing with fresh medium, irradiating with a 580 ± 20 nm diode lamp at 20.0 mW/cm^2 to a dose of 10.0 J/cm^2, incubating for an additional 24 h, and determining cell viability via MTT and resazurin assays with four replicates and three independent experiments.
9. Evaluate dark cytotoxicity by incubating cells with Hyp in the dark at concentrations from 0.01 to 100 µM for 24 h without irradiation, assessing viability via MTT and resazurin assays, and calculating IC50 values using GraphPad Prism 8. Perform statistical analyses using the Mann-Whitney test at p ≤ 0.05.
```

label: 

defect_types: 

notes: 

---

## 5. RD7E66D  (viability)

```
Please culture our HEK293 cells (both mock and PRELID2‑stable overexpression lines) as 3D spheroids in low‑attachment 96‑well plates under two media conditions (standard DMEM and glucose‑free DMEM) and assess viability at 72 h and 168 h with the Cyto3D Live‑Dead assay. Use the IN Cell Analyzer 2000 for imaging.

1. **Cell preparation (Day 0)**  
   a. Wash adherent cells twice with pre‑warmed PBS (−).  
   b. Add 1.5 mL trypsin, incubate ≤ 5 min (≈ 3 min). Quench with 3.5 mL medium, collect cells in a 15 mL tube, and centrifuge 1 000 rpm, 5 min.  
   c. Resuspend gently, let stand 3 min, then transfer the supernatant. Adjust the suspension to 1 × 10⁶ cells/mL in the appropriate medium (standard DMEM for the “nutrient‑replete” condition, glucose‑free DMEM for the “starvation” condition).  

2. **Seeding (Day 0)**  
   a. Add 150 µL of the condition‑specific medium to each well of a low‑attachment 96‑well plate.  
   b. Add 50 µL of the cell suspension (5 × 10⁴ cells) to each well.  
   c. Centrifuge the plate at 100 × g for 5 min to promote aggregation.  

3. **Medium exchange and Live/Dead staining (72 h)**  
   a. Remove 100 µL of medium from each well and add 100 µL fresh, condition‑specific medium.  
   b. Equilibrate the Cyto3D Live‑Dead Assay Kit to room temperature. Add 2 µL of the AO/PI reagent per 100 µL of medium in each well (i.e., 2 µL per well).  
   c. Incubate 10 min at 37 °C.  
   d. Acquire bright‑field and fluorescence images (AO: Ex 494 nm/Em 517 nm; PI: Ex 535 nm/Em 617 nm).  

4. **Medium exchange and imaging (120 h)**  
   a. Remove 100 µL of medium from each well and add 100 µL fresh, condition‑specific medium.  
   b. Acquire bright‑field images to monitor spheroid morphology.  

5. **Medium exchange and Live/Dead staining (168 h)**  
   a. Remove 100 µL of medium from each well and add 100 µL fresh, condition‑specific medium.  
   b. Add 2 µL of AO/PI reagent per well (as above), incubate 10 min at 37 °C.  
   c. Acquire bright‑field and fluorescence images (same settings as at 72 h).  

Please use the same seeding density for all conditions, keep trypsinization time ≤ 5 min, and pre‑warm all media to 37 °C before use. Let us know if any reagents or equipment are unavailable. Thank you.
```

label: 

defect_types: 

notes: 

---

## 6. R545DF1  (qpcr)

```
We have 89 caecal content samples and 68 skin‑swab samples (1400 cm² each) from Danish abattoirs. For each sample do the following:

1. **Sample handling**  
   * Caecal content: weigh ~35 g, add to 9 mL buffered peptone water (BPW, CM0509, Oxoid). Vortex thoroughly. Store the 10⁻¹ dilution at –20 °C for later qPCR.  
   * Skin swab: place gauze tampon (10 × 10 cm) into a stomacher bag with 85 mL BPW. Knead 2 min. Store the 10⁻¹ dilution at –20 °C for later qPCR.

2. **Enumeration on Petrifilm**  
   * Prepare 10‑fold dilution series for each sample in 0.9 % NaCl (use 25 µL 0.9 % NaCl to the dilution when enumerating total E. coli/Enterobacteriaceae).  
   * For tetracycline‑resistant E. coli, add 25 µL of a tetracycline solution (T3383, Sigma‑Aldrich) to 1 mL of the chosen dilution to reach a final concentration of 64 mg L⁻¹ in the SEC plates.  
   * Plate 1 mL of each appropriate dilution onto:  
     - Petrifilm Select E. coli SEC (Neogen) for total E. coli.  
     - Petrifilm Enterobacteriaceae EB (Neogen) for total Enterobacteriaceae.  
     - Petrifilm Select E. coli SEC (with tetracycline) for tetracycline‑resistant E. coli.  
   * Incubate all plates at 37 °C for 16–18 h, then count colonies to obtain CFU g⁻¹ (caecal) or CFU 1400 cm² (skin swab).

3. **DNA extraction for qPCR**  
   * Thaw stored 10⁻¹ dilutions at 5 °C.  
   * For caecal: take 0.5 mL of 10⁻¹ dilution; for skin swab: take 10 mL of initial dilution.  
   * Centrifuge caecal: 5 min, 13 000 rpm (Eppendorf Mini Spin). Centrifuge skin: 5 min, 10 000 rpm (Eppendorf 5810R).  
   * Resuspend pellets in 750 µL Power Beads solution + 60 µL C1 reagent (Qiagen PowerLyzer PowerSoil Kit). Follow kit instructions, elute DNA in 100 µL, store at –20 °C.

4. **Standard curves for qPCR**  
   * Grow E. coli strains NCTC 50078 (tetA/uidA) and CSH50::Tn10 (tetB) overnight in BHI broth at 37 °C.  
   * Determine CFU mL⁻¹ by plating 10⁻ⁿ dilutions on BHI agar with 16 µg mL⁻¹ tetracycline.  
   * Extract DNA from ~8 log₁₀ CFU mL⁻¹ cultures as above.  
   * Prepare 10‑fold DNA dilutions in MilliQ water covering 1.6–7 log₁₀ CFU mL⁻¹. Use these for each run to build a standard curve for uidA, tetA, and tetB.

5. **qPCR assay**  
   * Master mix per reaction (25 µL):  
     - 1× TaqMan™ Environmental Master Mix (Applied Biosystems).  
     - 0.5 µM forward primer + 0.5 µM reverse primer.  
     - 0.2 µM probe.  
   * Primer/probe sequences:  
     - **uidA**: F‑CGGAAGCAACGCGTAAACTC, R‑TGAGCGTCGCAGAACATTACA, P‑FAM‑CGCGTCCGATCACCTGCGTC‑TAMRA.  
     - **tetA**: F‑TTGGCATTCTGCATTCACTC, R‑GAAGGCAAGCAGGATGTAGC, P‑FAM‑GATCACCGGCCCTGTAGCCG‑BHQ.  
     - **tetB**: F‑TTACGTGAATTTATTGCTTCGG, R‑ATACAGCATCCAAAGCGCAC, P‑FAM‑CGCCGACCAAATCGGTCAGA‑BHQ‑1.  
   * Add 5 µL of extracted sample DNA.  
   * Set up reactions in a 96‑well plate (Mx3000P non‑skirted plate + optical caps). Include:  
     - Duplicate reactions for each sample.  
     - Negative control (sterile water).  
     - Positive control (1 × 10⁶ CFU mL⁻¹ standard for each target).  
   * Thermocycler conditions (MX3005P, Agilent):  
     - 95 °C for 10 min (polymerase activation).  
     - 45 cycles: 95 °C for 15 s, 60 °C for 1 min.  
   * Record Ct values; calculate CFU g⁻¹ (caecal) or CFU 1400 cm² (skin swab) using the standard curves and accounting for dilution factors.

6. **Reporting**  
   * Provide CFU counts for total E. coli, total Enterobacteriaceae, and tetracycline‑resistant E. coli from Petrifilm.  
   * Provide log₁₀ CFU/g (caecal) or log₁₀ CFU/1400 cm² (skin) for each target gene (uidA, tetA, tetB) from qPCR.  
   * Include the standard curve parameters (slope, R², efficiency) for each gene.  

Please keep all samples frozen at –20 °C until processing, and submit data with sample identifiers, plate counts, and Ct values. Let me know if you need any additional reagents or clarification.
```

label: 

defect_types: 

notes: 

---

## 7. R832011  (elisa)

```
Please run the following bone marrow-derived macrophage (BMDM) differentiation and stimulation assays on our provided samples:

1. Differentiate murine BMDMs from C57BL/6J bone marrow over 5 days in complete DMEM (DMEM, 10% FBS, 1% Pen/Strep) supplemented with 20–40 ng/mL M-CSF. Seed 25–35 × 10^6 cells per 15 cm plate.

2. On Day 5, harvest the BMDMs using cold detachment buffer (PBS with 2 mM EDTA and 2% FBS) incubated at 4°C for 20 min. Do not use trypsin. 

3. Count the cells and seed them in standard cell culture plates (5.0 × 10^5 cells/well in 24-well, 1 × 10^6 cells/well in 12-well, or 2 × 10^6 cells/well in 6-well). Rest the seeded BMDMs for 16–18 hours at 37°C in complete DMEM without M-CSF before running any downstream stimulations.

4. Perform microbial/viral and inflammatory stimulations using the rested BMDMs according to the following conditions:
   - Surface and endosomal TLR ligands (8–24 h incubation): LPS (100 ng/mL), LTA (1 μg/mL), Pam3CSK4 (100 ng/mL), Zymosan (10 μg/mL), R848 (5 μg/mL), or CpG (500 nM) in complete DMEM. Collect supernatants at 8 h for ELISA or harvest cells at 8 h for RNA isolation (using 350 μL RLT lysis buffer with 20 μL/mL β-mercaptoethanol) and at 24 h for flow cytometry.
   - NOD agonist: Treat with MDP (1–10 μg/mL) alone or combined with low-dose TLR ligands for 8–24 h. Collect supernatants for ELISA and/or harvest cells for qPCR.
   - Cytosolic nucleic acids / STING activation (1–24 h incubation): Transfect BMDMs at ~80%–90% confluency using lipid-based complexes in Opti-MEM. Use final concentrations of ISD (1 μg/mL), poly(dG:dC) (1 μg/mL), or 2′3′-cGAMP (5 μg/mL) combined with transfection reagent (e.g., 1.5 μL per well in 24-well format). 
   - Wound healing / M2 polarization: Stimulate BMDMs with IL-4 (10–20 ng/mL) alone or combined with IL-13 (10–20 ng/mL) for 8–24 h (or up to 48 h for functional assays) to assess Arg1, CD206, and related markers by RT-qPCR or flow cytometry.
   - Apoptotic cell tolerance (efferocytosis): Co-culture rested BMDMs with apoptotic primary thymocytes or lymphoid cells (induced by 40 Gy radiation or 1 μM staurosporine) at a 5:1 or 10:1 ratio for 2–24 h. Assess uptake, regulatory markers, Il10/Tgfb1 transcription, and IL-10/TGF-β secretion.
   - Tumor microenvironment modeling: Stimulate BMDMs with either tumor-conditioned media (TCM at 20% final concentration) or tumor cell supernatant (TCS at 50% final concentration) for 8 h (RNA isolation) or 24 h (flow cytometry).
```

label: 

defect_types: 

notes: 

---

## 8. R3E95D0  (growth_curve)

```
We would like you to perform vibriocidal assays on our serum samples using the protocol below.  
All materials you need are listed; please let us know if any item is missing.

**Materials (to have on hand):**  
- Petri dishes (P212121, LI-PD01100)  
- 15 mL sterile Falcon tubes & rack  
- 25 mL reservoir  
- Brain Heart Infusion (BHI) broth (Oxoid CM1135-UK)  
- 0.9 % NaCl (saline)  
- 96‑well tissue‑culture plate (Bio‑Basic TCP20‑96)  
- 1.5 mL micro‑centrifuge tubes (Ambion AM12450)  
- Multichannel pipettes P1‑10, P200 and new tips for each use  
- 70 % ethanol  
- Centrifuge (Eppendorf 5810, 3000 rpm, 10 min)  
- Blood agar plates (5 % sheep blood in Tryptic Soy Agar)  
- 50 mL Falcon tubes  
- Biotek microplate absorbance reader  
- Orbital shaker‑incubator (set to 37 °C, 50–220 rpm)  
- Guinea pig complement serum (300 µL aliquots)  
- V. cholerae O1 strains (Ogawa or Inaba) on blood agar  
- Monoclonal antibody (1 µg/mL in PBS) for assay control  
- 56 °C water bath for heat inactivation  

**Procedure (one plate per batch, all samples in duplicate):**

1. **Bacterial culture:**  
   a. Streak a single colony of V. cholerae (O1 Ogawa or Inaba) onto a blood agar plate. Incubate at 37 °C overnight (~12 h).  
   b. Transfer 1–2 colonies to a 15 mL BHI culture tube. Incubate in an orbital shaker‑incubator at 37 °C, 220 rpm for 3–4 h.  
   c. After growth, transfer the culture to a 15 mL centrifuge tube, centrifuge 3000 rpm, 10 min, 22–25 °C. Discard supernatant to 1:10 bleach or biohazard waste. Repeat wash twice (resuspend pellet in 10 mL saline, centrifuge, discard supernatant).  
   d. After washes, resuspend the final pellet in 1 mL 0.9 % NaCl. Transfer 200 µL to a 96‑well plate and read OD600. Prepare 1 mL of this suspension diluted with saline to OD600 ≈ 0.3 (e.g., if OD600 = 1.0, mix 300 µL suspension + 700 µL saline).  

2. **Serum preparation:**  
   a. Aliquot 20 µL of each serum sample into separate Eppendorf tubes. Heat‑inactivate at 56 °C for 30 min.  
   b. Dilute heat‑inactivated serum 1:10 (15 µL serum + 135 µL 0.9 % NaCl) – this is the 1:10 starting titer. Keep on ice.  

3. **Plate layout:**  
   a. Add 25 µL saline to all wells except column 2.  
   b. In column 2 (rows A–H) add 50 µL of the 1:10 diluted serum (two wells per sample, e.g., Sample 1 in 2A & 2B, Sample 2 in 2C & 2D, etc.).  
   c. Add 50 µL of the 0.3 OD bacterial working dilution to each well in column 2.  
   d. Perform 2‑fold serial dilutions across columns 3–12 using a multichannel pipettor (25 µL from column n into column n+1, mix, repeat). Use new tips between columns to prevent cross‑contamination.  
   e. In wells 1A–1D (growth controls), add 25 µL saline + 25 µL bacterial suspension + 25 µL guinea pig complement serum (prepared in a 25 mL reservoir).  
   f. In wells 2G & 2H (monoclonal antibody controls) add 50 µL of 1 µg/mL mAb in PBS.  
   g. In wells 1E, 1F, 1G, 1H add 25 µL saline (negative controls).  

4. **Incubation:**  
   a. Incubate the entire plate at 37 °C, 50 rpm on the orbital shaker‑incubator for 1 h.  
   b. Remove the plate, add 150 µL BHI to all wells (including controls). Mix gently.  
   c. Incubate at 37 °C, static, for 2 h.  

5. **Reading:**  
   a. Measure OD595 for all wells with the plate reader.  
   b. Subtract the average OD of the four negative control wells (1E–1H) from each reading to obtain blanked OD values. Set any negative values to zero.  

6. **Data analysis:**  
   a. Verify that average growth‑control OD595 (1A–1D) is between 0.20–0.28. If not, reject the plate (or repeat if only one out of range).  
   b. Determine the 50 % kill OD = (average growth‑control OD) ÷ 2.  
   c. For each sample, locate the first dilution where the OD595 is less than the 50 % kill OD; the titer is the reciprocal of that dilution. If no dilution meets the criterion, assign a titer of 5 (below detection).  
   d. Technical replicates must agree within one 2‑fold dilution; otherwise reject the sample.  
   e. Report the lower titer if replicates differ by one 2‑fold step.  

**Notes:**  
- Keep all samples and reagents cold until use (except the heat‑inactivation step).  
- Use fresh tips for every column to avoid cross‑contamination.  
- Confirm that the monoclonal antibody controls fall within the acceptance range: 50 % kill titer for Ogawa 0.0625–0.03125 (col 5–6) and for Inaba 0.125–0.0625 (col 4–5). If not, reject the plate.  

Please let us know once the assay is completed and provide the titers for each serum sample.
```

label: 

defect_types: 

notes: 

---

## 9. R92A018  (growth_curve)

```
Please run the following experiment on our E. coli samples (native or synthetic systems) using a 96‑well plate (Fisher Scientific #3904, flat‑bottom, tissue‑culture treated, black wall, clear bottom) and a Synergy Mx microplate reader.

**Materials**

1. 1 L Luria‑Bertani (LB) media with the appropriate antibiotics for each strain.  
2. Bacteriophage stock in LB with known PFU ml⁻¹.  
3. 96‑well plates (Fisher Scientific #3904).  
4. Microplate reader (Synergy Mx).

**Procedure**

1. **Plate reader settings** – Pre‑heat to 37 °C.  
   • Start kinetics: runtime 15 h (HH:MM:SS), interval 4 min.  
   • Shake: 30 s per interval.  
   • Read absorbance at 600 nm (full plate), normal read speed, 100 ms delay.  

2. **Grow overnight cultures** – In LB + antibiotics, grow each sample overnight.  

3. **Measure OD₆₀₀** – Take OD₆₀₀ of each overnight culture; dilute with LB + antibiotics to OD₆₀₀ = 0.02.  

4. **Plate loading** – Pipette 180 µL of each diluted culture into the 96‑well plate.  
   • Include wells of LB + antibiotics only (no bacteria) as negative controls and for OD₀ baseline.  

5. **Begin growth** – Start the plate‑reader protocol. Allow cultures to grow until the OD₆₀₀ of each well reaches 0.11.  

6. **Phage addition** – When OD₆₀₀ = 0.11, stop the reader.  
   • Add 20 µL of the appropriate bacteriophage dilution to each well (final volume 200 µL).  
   • Use the following MOI 10 series (add to 180 µL culture + 20 µL phage):  
     – 4.0 × 10¹⁰ PFU ml⁻¹ (MOI = 10¹)  
     – 4.0 × 10⁹ PFU ml⁻¹ (MOI = 10⁰)  
     – 8.0 × 10⁸ PFU ml⁻¹ (MOI = 10⁻¹)  
     – 8.0 × 10⁷ PFU ml⁻¹ (MOI = 10⁻²)  
     – 8.0 × 10⁶ PFU ml⁻¹ (MOI = 10⁻³)  
   • Include a set of LB-only wells that receive only 20 µL LB (no phage) as a control.  

7. **Resume reader** – Restart the kinetics run and record OD₆₀₀ for the next 15 h to monitor growth and phage effect.  

Please keep us updated with the data and any deviations from the protocol.
```

label: 

defect_types: 

notes: 

---

## 10. R56C658  (viability)

```
Please use our provided *Acinetobacter baumannii* strain (CECT 452; ATCC 15308) and our supplied recombinant RNases (RNase 3/1-v1 and RNase 3/1-v3, expressed and purified via inclusion bodies from *E. coli* BL21 (DE3) as previously described) to carry out the following experimental workflow in at least triplicate.

1. Grow mature biofilms using a Calgary Biofilm Device (CBD) by diluting an overnight culture in Mueller–Hinton broth (MHB) to an OD600 of 0.02, adding 150 µL to a polypropylene 96-well plate with PBS in the outer wells, inserting the CBD lid, and incubating for 24 h at 37 °C with 100 rpm shaking.

2. Perform biofilm viability and biomass quantification:
   - For viability, rinse CBD pegs three times in PBS and transfer to a new 96-well plate containing 200 µL MHB with 16 µg/mL resazurin. Incubate for 12 h at 37 °C with orbital shaking in a Tecan Spark reader, recording fluorescence every 10 min (excitation 530 nm, emission 590 nm) to determine half-maximal fluorescence times relative to a planktonic standard curve.
   - For biomass, fix rinsed biofilms at 60 °C for 1 h, stain with 200 µL of 0.1% crystal violet for 15 min, rinse, dry, elute with 33% acetic acid, and measure absorbance at 595 nm.

3. Run antibiotic challenge assays on mature biofilms using two-fold serial dilutions of colistin, moxifloxacin, and tobramycin in MHB (200 µL final volume) for 12 h at 37 °C with 100 rpm shaking, followed by resazurin or crystal violet assessment.

4. Evaluate the bactericidal activity of the recombinant RNases (tested at 200 to 0.01 µM serial dilutions or a fixed 50 µM concentration) against rinsed biofilms in HBS for 4 h at 37 °C (100 rpm shaking), quantifying viability via resazurin and plating 30 µL supernatant on LB agar to count released planktonic bacteria.

5. Test RNases as colistin adjuvants by combining 1 µM final concentration of recombinant RNase (prepared in 0.01% acetic acid) with colistin (1 to 12 µM in MHB) and exposing rinsed biofilms for 12 h at 37 °C (100 rpm), assessing viability with the resazurin assay.

6. Conduct a biofilm resistance evolution assay over multiple cycles by exposing biofilms to colistin alone or combined with 1 µM RNase 3/1-v3 for 12 h, monitoring viability and released planktonic OD600, transferring pegs to fresh treatment plates daily, and storing lineage samples at -80 °C with 15% glycerol after each cycle. Adjust colistin starting concentrations (6 µM) upward if no viability reduction is observed.

7. Determine MIC and MBEC for the evolved bacterial lineages stored from days 3, 5, 7, and 9:
   - For MIC, incubate stationary-phase cultures in colistin dilutions (0.78 to 1600 µM depending on resistance) for 24 h at 37 °C (100 rpm) and record visual growth.
   - For MBEC, grow biofilms from day 5 lineages on CBD pegs for 24 h, treat with colistin dilutions (1.56 to 1597.44 µM) for 24 h, rinse, and assess survival using the resazurin assay in fresh MHB.

8. Perform all necessary statistical analyses (normality tests, linear/non-linear regression for ED50 and correlations, Mann–Whitney U tests, and Spearman's correlations) using GraphPad Prism 8 with significance set at p < 0.05.
```

label: 

defect_types: 

notes: 

---

## 11. R160D5B  (viability)

```
Please perform the following workflow on the pistachio material we will provide:

1. **Defatting**  
   - Chop the pistachios finely and weigh 5 g portions.  
   - Add 10 mL of n‑hexane to each portion, stir continuously at room temperature for 24 h.  
   - Let the mixture settle for 2–3 h, then carefully decant and discard the hexane layer.  
   - Vacuum‑filter the remaining solid on a Buchner funnel with filter paper to remove residual solvent.  

2. **Green (UAE) extraction**  
   - From the defatted material, weigh 1 g (analytical balance).  
   - Add enough 45 % v/v ethanol‑water to cover the sample (≈10 mL).  
   - Place in a heated ultrasonic bath (40 kHz, 120 W) set to 50 °C for 15 min.  
   - Centrifuge the suspension at 5 000 rpm, 30 min, 5 °C.  
   - Collect the supernatant and concentrate it on a rotary evaporator.  
   - Store the dried extract at –20 °C (expected yield ≈88 mg).  

3. **Classic extraction**  
   - From the defatted material, weigh 5 g.  
   - Add 50 mL methanol containing 0.1 % v/v HCl.  
   - Sonicate 15 min, then centrifuge 5 000 rpm, 10 min, 4 °C.  
   - Repeat the sonication/centrifugation two more times on the same pellet; pool the three supernatants.  
   - Evaporate the pooled methanol to dryness, dissolve the residue in 20 mL distilled water.  
   - Transfer to a separating funnel and extract four times with 20 mL ethyl acetate each.  
   - Combine the organic phases, dry over Na₂SO₄ for 20 min, then evaporate to dryness.  
   - Store the dried extract at –20 °C (expected yield ≈90 mg).  

4. **Aliquoting of extracts**  
   - Dissolve each dried extract in methanol, adjust to 1 mg per 1 mL (or any volume that gives exactly 1 mg per micro‑vial).  
   - Pipette 1 mg into individual micro‑vials, evaporate methanol completely to obtain dry, pre‑weighed aliquots for later use.  

5. **Total carbohydrate assay (phenol‑sulfuric acid)**  
   - Prepare a glucose stock (100 mg/mL) by dissolving 500 mg D‑glucose in 5 mL water.  
   - Make standards at 80, 160, 240, 320, 400 µg/mL by appropriate dilutions of the stock; to each 100 µL standard add 100 µL 5 % phenol and 500 µL concentrated H₂SO₄, bring to 5 mL with water, incubate 10 min (RT), read at 490 nm.  
   - For each extract, dissolve in methanol to 20 mg/mL, take 100 µL, treat exactly as the standards (final volume 2 mL), incubate 10 min, read at 490 nm.  
   - Perform all measurements in triplicate and calculate carbohydrate content from the glucose standard curve (y = 0.0013x + 0.0483).  

6. **HPLC‑MS phenolic profiling**  
   - Lyophilize the extracts, dissolve to 2 mg/mL in methanol.  
   - Dilute 10 µL of this solution to 1 mL with methanol (final 20 µg/mL).  
   - Filter through 0.22 µm nylon syringe filters.  
   - Inject 10 µL onto a Phenomenex Kinetex C‑18 column (100 mm × 2.1 mm, 2.6 µm) on a Thermo Vanquish HPLC.  
   - Mobile phase A: water + 0.1 % formic acid; B: acetonitrile + 0.1 % formic acid.  
   - Gradient: 0 min 10 % B → 60 min 100 % B (hold 10 min), flow 0.25 mL/min, column 40 °C.  
   - MS: LTQ XL with H‑ESI II, positive mode, spray 3 kV, capillary 250 °C, capillary voltage 20 V, tube lens 120 V, scan m/z 150–2000.  

7. **Cell culture (HCT‑116)**  
   - Grow HCT‑116 cells in McCoy’s 5A medium +10 % FBS + penicillin/streptomycin (50 µg/mL) at 37 °C, 5 % CO₂.  

8. **Viability (MTT) assay**  
   - Prepare extract solutions in 1:1 PBS (100 mM) : 70 % ethanol to give a stock of 250 ng/µL.  
   - Seed 5 000 cells/well in 96‑well plates (McCoy’s +10 % FBS, 1 % pen/strep).  
   - After overnight attachment, add 10 µL of each extract stock to the appropriate wells (final 250 ng/µL). Include untreated wells as controls.  
   - Incubate for 24, 48, and 72 h.  
   - At each time point add 10 µL MTT (5 mg/mL in PBS), incubate 3 h at 37 °C, remove supernatant, dissolve formazan in DMSO, read absorbance at 570 nm.  
   - Perform each condition in quadruplicate, repeat the whole experiment at least three independent times.  

9. **Inflammatory/metabolic pathway analysis**  
   - Seed 200 000 cells/well in 6‑well plates, overnight.  
   - Treat for 24 h with: (a) green extract, (b) classic extract (both at 250 ng/µL), (c) PB4 at 0.16 µM (half its IC₅₀), and (d) untreated control.  
   - After treatment, remove medium, lyse cells directly in the well with RLT buffer + β‑mercaptoethanol (Qiagen RNeasy kit protocol).  

10. **RNA extraction and quality control**  
    - Follow Qiagen RNeasy Mini Kit instructions.  
    - Quantify RNA with BioPhotometer D30 and Qubit RNA HS assay.  
    - Accept samples with A260/A280 1.8–2.1.  
    - Assess integrity on Agilent Bioanalyzer 2100 using RNA 6000 Nano Kit; record RIN values.  

11. **cDNA synthesis**  
    - Use 1 µg total RNA per reaction with Qiagen QuantiTect Reverse Transcription Kit (includes gDNA wipe‑out).  
    - Store cDNA at –20 °C.  

12. **RT‑qPCR**  
    - Run reactions on a LightCycler 480 II with QuantiTect SYBR Green PCR Kit.  
    - Use 50 ng cDNA per 20 µL reaction, primers as in Table 1 (GLUT2, IL‑6, IL‑10, HMOX‑1, housekeeping RPLP0).  
    - Cycling: 95 °C 15 min; 40 cycles of 94 °C 15 s, 55 °C 30 s, 72 °C 30 s (fluorescence acquisition).  
    - Include a no‑template control for each primer set.  
    - Perform each sample in triplicate.  
    - Analyze data with the ΔΔCt method, normalizing target genes to RPLP0.  

Please return all raw data (spectrophotometric reads, HPLC‑MS chromatograms and MS spectra, absorbance values for MTT, qPCR Ct values), calculated yields, and any observations on extract quality. Let us know promptly if any reagents or equipment listed are unavailable so we can adjust accordingly. Thank you.
```

label: 

defect_types: 

notes: 

---

## 12. R271589  (qpcr)

```
Please prepare and run the following mouse model of C. difficile infection and relapse on our six C57BL/6 mice (average weight ~20 g). Follow the schedule exactly and return all raw data (weights, clinical scores, CFU counts, ribotyping results) and any plates or DNA extracts for our records.

1. **Solution preparation (all in type‑1 ultrapure water, filter‑sterilize 0.22 µm):**  
   - **Antibiotic mix** (to be given by oral gavage on days –6, –5, –4): dissolve kanamycin sulfate (8 mg mL⁻¹), gentamicin sulfate (0.7 mg mL⁻¹), colistin sulfate (0.84 mg mL⁻¹), metronidazole (4.3 mg mL⁻¹) and vancomycin (0.9 mg mL⁻¹) in sterile 0.9 % NaCl. Prepare enough for 1.5 mL total (6 mice × 250 µL × 3 days + extra for two losses).  
   - **Clindamycin** (10 mg kg⁻¹ i.p. on day –1): make a 2.0 mg mL⁻¹ solution in sterile 0.9 % NaCl, filter‑sterilize. Prepare 1.5 mL total.  
   - **Vancomycin** (50 mg kg⁻¹ oral gavage days 3‑7): make a 10.0 mg mL⁻¹ solution in sterile 0.9 % NaCl, filter‑sterilize. Prepare 2 mL total (6 mice × 250 µL × 5 days + extra).  
   - **PBS** (1×, pre‑reduced). Prepare 500 mL, store at 4 °C; place in anaerobic chamber ≥16 h before use.  
   - **Ethanol 100 %** – aliquot 1 mL per day, keep in anaerobic chamber for ≥16 h.  
   - **CCFA and TCCFA agar plates** (≈90 plates each, enough for 2 plates per mouse per day). Use the published formulation (proteose peptone‑agar, 5× salts, 30 % fructose, cycloserine, cefoxitin; add 0.1 % sodium taurocholate only to TCCFA). Autoclave agar, keep molten at 50 °C, pour 20–25 mL/plate, let solidify, store at 4 °C ≤2 weeks.  

2. **Day –6 to –4 (Antibiotic mix, oral gavage):**  
   - Weigh each mouse, record weight and clinical score.  
   - Calculate gavage volume (Table: 20 g ≈ 100 µL, 22 g ≈ 110 µL, etc.).  
   - Deliver the antibiotic mix by oral gavage (250 µL per mouse).  

3. **Day –3 to –2 (Recovery):**  
   - Weigh and record clinical scores; no treatment.  

4. **Day –1 (Clindamycin, i.p.):**  
   - Weigh, record clinical score.  
   - Inject clindamycin i.p. using the same weight‑based volume as above.  
   - Change cages, move mice to clean cages.  
   - Place one pre‑reduced CCFA plate and one TCCFA plate per mouse in the anaerobic chamber for use tomorrow.  

5. **Day 0 (Spore challenge):**  
   - Weigh, record clinical score.  
   - Collect a fresh stool from each mouse into a pre‑weighed sterile 1.5 mL tube (bleach tube exterior).  
   - Prepare a spore suspension containing 1 × 10⁶ C. difficile spores per mouse in 100 µL sterile PBS.  
   - Administer 100 µL spore suspension by oral gavage (volume adjusted for mouse weight if needed).  
   - Place fresh CCFA/TCCFA plates (one each per mouse) in the anaerobic chamber for next‑day plating.  
   - Immediately process the collected stool (see step 9) to assess any pre‑existing colonization.  

6. **Days 1‑2 (Early CDI monitoring):**  
   - Daily: weigh, record clinical score; collect fresh stool (same tube procedure).  
   - Place new CCFA/TCCFA plates in the anaerobic chamber for the following day.  

7. **Days 3‑7 (Vancomycin remission induction):**  
   - Daily: weigh, record clinical score.  
   - Give vancomycin oral gavage (dose calculated from weight, 250 µL total volume).  
   - Collect stool, change cages, and set aside CCFA/TCCFA plates for the next day.  

8. **Days 8‑15 (R‑CDI monitoring):**  
   - Daily: weigh, record clinical score; collect stool.  
   - In the anaerobic chamber each morning place PBS, ethanol, and fresh CCFA/TCCFA plates (one each per mouse) for that day’s plating.  

9. **Stool processing (performed each day in the anaerobic chamber):**  
   - Record mass of tube + stool; subtract empty tube weight to obtain stool mass (mg).  
   - Add 500 µL pre‑reduced PBS, vortex 30 s to homogenize.  
   - **Vegetative cell count:** spread 100 µL of the homogenate onto the lower half of the CCFA plate; also transfer 100 µL to a 96‑well plate, perform four 1:10 serial dilutions, and spot 3 µL of each dilution (in triplicate) on CCFA.  
   - **Spore count:** to the same 96‑well plate add 90 µL 100 % ethanol (1:1 with the sample), incubate 30 min, then spread 100 µL of the undiluted ethanol‑treated mixture onto the TCCFA plate; also spot 3 µL of each ethanol‑treated dilution (in triplicate) on TCCFA.  
   - Incubate all CCFA and TCCFA plates 48 h at 37 °C in the anaerobic chamber.  

10. **Plate reading:** after 48 h, count colonies (CFU). Compute CFU per gram of feces:  
    - For CCFA: CFU g⁻¹ = (CFU count × total PBS volume × 1000) / (stool mass mg).  
    - For TCCFA: multiply the CCFA result by 2 to account for the 1:2 ethanol dilution.  

11. **Ribotyping (days 0, 3, 11):**  
    - Pick up to 10 colonies from each CCFA plate, inoculate into BHIS broth, grow 16 h anaerobically.  
    - Extract genomic DNA (any commercial kit).  
    - PCR amplify the 16S‑23S intergenic region using primers: Forward GTGCGGCTGGATCACCTCCT, Reverse CCCTGCACCCTTAATAACTTGACC.  
    - Run products on a 5 % non‑denaturing polyacrylamide gel (TAE buffer, 45 min, 150 V) and image.  
    - If you have a fluorescent PCR ribotyping platform, you may use that instead.  

12. **Data reporting:**  
    - Provide an Excel file with daily weights, clinical scores, stool masses, CFU g⁻¹ (vegetative and spore), and ribotype gel images (or electropherograms).  
    - Send back any remaining plates and DNA extracts for our archival.  

13. **Safety and handling:**  
    - Use two operators per cage: one “clean” handler (outside the BSC) moving cages in/out and recording data, and one “contaminated” handler (inside the Class II BSC) performing dosing, stool collection, and plate handling.  
    - Change gloves after each mouse; decontaminate work surfaces with bleach between cages.  
    - Keep all work with mice and feces inside the BSC or anaerobic chamber to avoid environmental contamination.  

That is all the information required to run the experiment on our samples. Let us know if any reagents or equipment are unavailable, or if you need clarification on any step. Thank you.
```

label: 

defect_types: 

notes: 

---

## 13. R19CF04  (qpcr)

```
1. Please use the following cell lines for all in‑vitro work:  
  - Rat bone marrow mesenchymal stem cells (rBMSCs) from male Sprague‑Dawley rats (Passage 5).  
  - RAW 264.7 murine macrophage cells (male BALB/c).  
  Culture media: α‑MEM + 10 % FBS + 1 % penicillin‑streptomycin for rBMSCs; high‑glucose DMEM + 10 % FBS + 1 % penicillin‑streptomycin for RAW 264.7. Keep at 37 °C, 5 % CO₂, and confirm no mycoplasma.

2. Extract Aloe vera gel as follows: wash fresh mature leaves with sterile DI water, UV‑sterilise 1 h, peel green epidermis, scrape inner gel, filter through sterile gauze, stir 2 h RT, centrifuge 8000 rpm 15 min, collect supernatant. Verify polysaccharide profile by GPC and LC‑MS. Store at 4 °C.

3. Synthesize GelMA: dissolve 10 g gelatin in 100 mL DI water (50 °C, 300 rpm). Add 4 mL methacrylic anhydride dropwise (0.5 mL min⁻¹) at 50 °C, stir 3 h, terminate with 300 mL DI water, dialyse (13 kDa cut‑off) at 37 °C for 7 days (change water 2–3×/day). Freeze in LN₂ 24 h, lyophilise 72 h. Confirm ~60 % degree of substitution by ¹H‑NMR. Store powder −20 °C, dry, light‑shielded.

4. Prepare bioinks under UV sterilisations (2 h).  
  - GelMA bioink: 0.5 g GelMA + 0.0125 g LAP in 5 mL sterile DI water, stir 37 °C 2 h → 10 wt % GelMA.  
  - GelMA/Laponite: add 0.05 g Laponite to the above, stir 37 °C 2 h → 10 wt % GelMA, 1 wt % Laponite.  
  - GelMA/Laponite/AV: disperse 0.05 g Laponite in 3 mL DI water + 0.0125 g LAP, stir 1 h 37 °C, add 2 mL sterile Aloe vera gel, stir 1 h 37 °C → final 10 wt % GelMA, 1 wt % Laponite, 40 vol % AV.

5. Print bone organoid precursors with a Regenovo Bio‑Architect SR. Load cell‑laden bioink (1 × 10⁶ cells mL⁻¹; rBMSCs detached with 0.25 % trypsin‑EDTA, centrifuge 1000 g 5 min, resuspend). Print 8‑layer rectangular grid (5 × 5 mm, 1.5 mm infill, 90° interlayer rotation). Printing parameters: 8 °C, 0.2–0.3 MPa pneumatic pressure, 4 mm s⁻¹ speed, 2 mm retraction, 21 G nozzle. Cross‑link each layer with 365 nm UV (5 % intensity, 20 mW cm⁻²) for 10 s, then post‑cure 30 s. Compute Pr and Dfr from micrographs if requested.

6. Culture constructs: first 24 h in growth medium, then switch to osteogenic induction medium (α‑MEM + 10 % FBS + 1 % penicillin‑streptomycin + 10 mM β‑glycerophosphate + 50 µg mL⁻¹ L‑ascorbic acid + 100 nM dexamethasone). Static culture for up to 28 days, change medium every 2–3 days.

7. Perform viability/proliferation assays:  
  - Calcein‑AM/PI at days 1, 4, 7, 14. Stain 1 µL Calcein‑AM + 1 µL PI + 1000 µL PBS, 30 min 37 °C dark, wash 3× PBS, image on Olympus FV3000. Quantify live/dead ratio with ImageJ.  
  - CCK‑8 at same timepoints: wash with PBS, add 10 % CCK‑8 in medium, incubate 1 h 37 °C light‑protected, transfer 100 µL supernatant to 96‑well plate, read A₄₅₀ with microplate reader.

8. ALP and Alizarin Red staining:  
  - For 2D co‑culture: seed rBMSCs in 12‑well plates with acellular scaffolds (Transwell inserts) – growth medium day 1, osteogenic medium day 2. Fix 4 % PFA 15 min day 10, ALP with BCIP/NBT (30 min), ARS (30 min).  
  - For 3D constructs: fix 4 % PFA 15 min day 14/28, embed in paraffin, section 5 µm, deparaffinise, stain with ARS or BCIP/NBT (30 min), wash PBS, image.

9. Gene expression (RT‑qPCR): lysate 500 µL Trizol per well, 5 min ice, 100 µL chloroform, vortex, 5 min ice, 12000 g 15 min 4 °C, transfer aqueous, 1 volume isopropanol, 10 min ice, 12000 g 10 min 4 °C, wash pellet 1 mL 75 % ethanol, 5 min 7500 g 4 °C, air‑dry 10 min, dissolve in DEPC water. Quantify. cDNA: 1000 ng RNA in 20 µL PrimeScript RT (37 °C 15 min, 85 °C 15 s, 4 °C hold). qPCR: 20 µL TB Green Premix Ex Taq + diluted cDNA + primers (IL‑1β, CD206, iNOS, IL‑10, RUNX2, OCN), 2 −ΔΔCt relative to GAPDH.

10. Western blot: harvest after 10 days, wash PBS, lyse 200 µL RIPA + protease/phosphatase inhibitors + EDTA, 30 min ice, centrifuge 12000 g 5 min 4 °C, BCA protein assay. Load 25 µg per lane on 10 % SDS‑PAGE, run 80 V 30 min, 120 V 60 min, transfer to PVDF 300 mA 100 min ice‑cooled. Block 15 min protein‑free buffer, primary antibodies (Collagen I, RUNX2, GAPDH; 1:1000, 1:1000, 1:2000) overnight 4 °C, wash TBST 10 min ×3, secondary HRP 1:500 1.5 h RT, visualize Omni‑ECL on Bio‑Rad.

11. Micro‑CT (SkyScan 1172/1272): scans at 65 kV, 80 µA, 9 µm voxel, 0.5 mm Al filter, 0.4° rotation step, 360°. Reconstruct with NRecon, analyze BV/TV %, Tb.Th, Tb.N with CTAn. Produce 3‑D images with CTVoX.

12. Macrophage assays:  
  - Migration: Transwell (1 × 10⁵ RAW 264.7 in upper insert, scaffold in lower chamber) 24 h, remove non‑migrated cells, fix 4 % PFA, stain 0.5 % crystal violet, count under microscope.  
  - Invasion: pre‑coat upper insert with 0.1 wt % gelatin, same procedure.  
  - Adhesion & polarization: seed 1 × 10⁴ RAW 264.7 on scaffolds, assess viability day 1/4/7 as in 7. For polarization, co‑culture on coverslips (lower chamber) and scaffold (upper insert) 24 h, fix 4 % PFA 15 min, permeabilise 0.1 % Triton X‑100 15 min, block goat serum 30 min, primary iNOS/CD206 overnight 4 °C, Alexa Fluor 488/594 secondary 30 min, DAPI 5–20 min, image FV3000.  
  - Flow cytometry: detach RAW 264.7 (trypsin‑EDTA), fix 4 % PFA 10 min, permeabilise 0.1 % Triton X‑100 10 min, stain Alexa Fluor 488‑iNOS (1:100), PE‑CD206 (1:100) 30 min, wash PBS, analyze on Beckman CytoFLEX.

13. In vivo subcutaneous implantation: eight‑week female BALB/c nude mice (≈8 weeks old). Anesthetise with isoflurane (3–5 % induction, 1–2 % maintenance). Disinfect dorsal area, midline incision, implant one bone organoid precursor subcutaneously, suture. Euthanise at 2 and 4 weeks, retrieve implants, fix 4 % PFA, decalcify 10 % EDTA (pH 7.2–7.4) for 4 weeks. Paraffin embed, cut 5 µm sections, H&E, or block 3 % BSA for immunofluorescence: overnight 4 °C primary (OCN, RUNX2, Periostin, CD31, Collagen I, Vinculin, iNOS, CD206, 1:500 in 3 % BSA), secondary 1:500, confocal imaging. Also send one set for bulk RNA‑seq: isolate RNA with Trizol, enrich mRNA, prepare Illumina library, sequence, provide differential expression and GO/KEGG results.

14. In vivo calvarial defect repair: eight‑week female Sprague‑Dawley rats (200–220 g). Anesthetise with 1 % chloral hydrate IP, shave/ disinfect, midline scalp incision, create bilateral 5 mm critical‑size defects with circular trephine under saline irrigation, avoid dura. Implant 21 bone organoid precursors into each defect, suture. Euthanise at 4 and 8 weeks (overdose pentobarbital). Harvest cranium, micro‑CT as above, decalcify 10 % EDTA, section, H&E, immunofluorescence (OCN, RUNX2, CD206, iNOS). Provide quantitative bone volume and histology.

15. Biosafety assessment: at 8 weeks post‑implantation, harvest heart, liver, spleen, lungs, kidneys from rats. Fix 4 % PFA 24–48 h, dehydrate, embed in paraffin, 5 µm sections, H&E. Blood at 4 weeks for CBC and serum chemistry (ALT, AST, BUN, CREA).

16. Deliverables:  
  - Detailed images and quantifications for viability, proliferation, ALP, ARS, micro‑CT, immunofluorescence.  
  - qPCR Ct values, relative expression tables.  
  - Western blot band densities.  
  - Flow cytometry % iNOS⁺ and CD206⁺ cells.  
  - RNA‑seq raw counts, differential expression list, GO/KEGG enrichment.  
  - Histology slides and photomicrographs for all in vivo analyses.  
  - Final report with statistical analysis (GraphPad Prism 9, Origin 2021) and interpretation.

Please confirm receipt of this request, and let us know if any reagents or equipment are unavailable so we can provide alternatives. Thank you.
```

label: 

defect_types: 

notes: 

---

## 14. R63BE1C  (viability)

```
Please run an MTT metabolic viability assay on our provided samples using the following protocol.

Culture the authenticated adherent mammalian line in its supplier-specified complete medium at 37 °C and 5% CO₂. Before starting, confirm a negative mycoplasma result, record cell line, passage, and reagent lot details, and ensure cultures are in exponential growth with at least 90% viability. 

Perform a preliminary qualification to determine the optimal cell seeding density and MTT incubation time. Test 2,500, 5,000, 10,000, and 20,000 viable cells per well in triplicate with cell-free blanks, and compare 2, 3, and 4 h MTT incubation periods. Choose conditions that yield a measurable control signal within the reader range, a proportional relationship between signal and cell number, and subconfluent controls. 

Perform range finding to establish a seven-concentration test series (T1–T7) spanning twofold dilutions that capture low, high, and transition responses. Ensure solubility in treatment medium at the highest concentration (Cmax) and keep the vehicle fraction constant across all dilutions. Use a vehicle-tolerance pilot to select this fraction, targeting $\le$0.1% v/v DMSO when feasible. 

Prepare fresh 5 mg/mL MTT stock by dissolving 50 mg MTT in sterile PBS to a final volume of 10 mL, mixing, and filtering through a 0.22 µ0m sterile filter while protecting from light. Prepare fresh Triton X-100 working solution (1% v/v in treatment medium) for the lysis control, and calculate assay-day volumes allowing a 10% excess for 60 inner wells.

For each independent run, seed 10,000 viable cells (or the qualified density) in 100 µL of complete medium per well in the 60 inner wells of a clear, flat-bottom, 96-well plate. Fill the 36 perimeter wells with 200 µL sterile PBS to reduce evaporation and exclude them from calculations. Distribute concentration positions across runs using a recorded randomization plan, using one cell line, test material, and exposure duration per plate, and plan at least three independent experiments. Include untreated cells (U), vehicle-only cells for normalization (VC), and a procedural lysis control with 0.1% Triton X-100 added during the final 15 min (PC). For every condition, include a process-matched cell-free blank (B1–B7, BU, BVC, BPC) carried through every medium exchange, MTT reaction, and solubilization step.

Allow cells to attach for 24 h at 37 °C and 5% CO₂. Gently aspirate the medium and apply 100 µL of the assigned treatment solutions (T1–T7, U, VC) or matched cell-free blanks at their final concentrations. Incubate for 24 h at 37 °C and 5% CO₂. For PC and BPC wells, replace the medium at 23 h 45 min with 90 µL treatment medium and 10 µL of 1% Triton X-100 working solution for the final 15 min.

At 24 h, inspect cells under a microscope and record any morphology changes, precipitation, contamination, or detachment. Gently remove the treatment medium from assay wells and blanks without scraping or allowing wells to dry, avoiding a PBS wash unless separately qualified. Add 90 µL of prewarmed phenol red-free assay medium and 10 µL of 5 mg/mL MTT stock to every assay well and cell-free blank to reach a final MTT concentration of 0.5 mg/mL in 100 µL. Incubate the plate protected from light for 3 h at 37 °C and 5% CO₂.

Carefully aspirate the MTT-containing medium while retaining cells and formazan crystals. Add 100 µL DMSO to every assay and blank well immediately, and mix on a gentle plate shaker for at least 10 min at 20–25 °C, protected from light, until crystals are fully dissolved. Read absorbance immediately at 570 nm with a 630 nm reference, keeping handling times consistent and disabling automatic path-length correction.

Process the data by subtracting the reference absorbance ($A_{630}$) from the primary absorbance ($A_{570}$) for each well, then subtracting the mean signal of the corresponding process-matched cell-free blanks. Normalize each corrected treatment well to the mean corrected VC signal from the same plate ($100 \times S_i / \text{mean}(S_{\text{VC}})$). Summarize replicates by reporting individual corrected signals, means, standard deviations, and technical coefficients of variation for each run, and average technical wells within each independent experiment before estimating between-experiment uncertainty. If supported by the data, fit a decreasing four-parameter logistic model to positive treatment concentrations using log-spaced doses to determine the relative $\text{IC}_{50}$ and $\text{IC}_{50}$ at 50% vehicle-normalized activity, reporting all curve-fit parameters, confidence intervals, and quality metrics.
```

label: 

defect_types: 

notes: 

---

## 15. R7D1722  (growth_curve)

```
Please run a LUDOX CL‑X calibration on our plate‑reader before we take any OD600 measurements on our bacterial cultures.

1. Use a black, clear‑bottom 96‑well plate.  
2. Add 100 µL of LUDOX CL‑X (45 % colloidal silica) to wells A1, B1, C1, and D1.  
3. Add 100 µL of sterile ddH₂O to wells A2, B2, C2, and D2 (these are the blanks).  
4. Disable any automatic path‑length correction on the plate reader (the instrument we’ll use for the cell measurements).  
5. Measure absorbance at 600 nm for all eight wells using the same measurement mode, integration time, and gain settings that we will use for the actual cell samples. Record the raw absorbance values.  
6. Send me the raw absorbance data (or fill the attached iGEM 2019 Plate Reader LUDOX Calibration spreadsheet with the values in the blue cells). I will calculate the correction factor (Reference OD600 ÷ measured Abs600) and give you the factor to apply to all subsequent OD600 readings.  

Materials you’ll need (provided by us):  
- LUDOX CL‑X (1 mL)  
- Sterile ddH₂O (enough for 4 × 100 µL)  
- 96‑well black clear‑bottom plate  

Let me know once the calibration is done or if you run into any issues. Thanks!
```

label: 

defect_types: 

notes: 

---

## 16. R3ABFA1  (elisa)

```
Please process our grey wolf hair samples to determine cortisol (CORT) and cortisone (CORN) levels using the following protocol:

1. Sample Pretreatment and Homogenization
   - Wash 35 mg of each hair sample by manually shaking with 5 mL of isopropanol for 3 min. Repeat this washing step twice using fresh isopropanol each time.
   - Leave the washed hair to dry overnight at room temperature.
   - Cut the dried hair into approximately 2 mm fragments using surgical scissors.
   - Weigh exactly 35 mg of each fragmented sample into a Falcon tube, add five steel balls, and grind using a homogenizer for 5 min (five 30 s cycles with intervals) at 10 °C with cooling.

2. Sample Preparation for UHPLC-ESI-MS/MS
   - Incubate the powdered hair samples in 1 mL of methanol containing 15 ng/mL of isotopically labelled internal standards (CORT-D4 and CORN-D8) for 24 h at 70 rpm and room temperature.
   - Centrifuge the samples for 10 min at 13,000 rpm.
   - Transfer 800 µL of the supernatant to a new tube and evaporate to dryness.
   - Reconstitute the dried residue in 1 mL of LC-MS-grade water and ultrasonicate for 2 min.
   - Purify the samples using an automated SPE system with Strata-X cartridges (30 mg): condition with 1 mL of methanol, equilibrate with 1 mL of water, load 1 mL of sample, wash with 1 mL of water, and elute analytes with 1 mL of methanol.
   - Concentrate the eluate to 200 µL, transfer to a glass chromatography vial, and analyze in triplicate injections.

3. UHPLC-ESI-MS/MS Analysis
   - Perform chromatographic separation at 40 °C using a BEH C18 1.7 µm column (2.1 x 100 mm) with a flow rate of 0.2 mL/min. Use 0.1% formic acid in water as solvent A and methanol as solvent B.
   - Run the gradient: 0–4 min, 20–60% B; 4–5 min, 60% B; 5–7 min, 60–70% B; 7–9 min, 70% B (2 min post-run).
   - Use a 5 µL injection volume and acquire data in positive ionization dMRM mode using the specified transitions and source parameters for CORT, CORT-D4, CORN, and CORN-D8.

4. CORT Determination by ELISA (Comparative Analysis)
   - Weigh 35 mg of powdered hair into a tube, mix with 1.8 mL of methanol, vortex, and incubate overnight on an orbital shaker.
   - Centrifuge the tubes and evaporate the recovered supernatant to dryness under a gentle stream of nitrogen at 37 °C.
   - Reconstitute the dried extracts in 400 µL of ELISA Buffer, vortex, and quantify CORT using the Cayman Chemical Cortisol ELISA Kit (Cat. No. 500360) according to the manufacturer's instructions, reading absorbance at 410 nm.
```

label: 

defect_types: 

notes: 

---

## 17. RA909E7  (growth_curve)

```
Please process our submitted bacterial samples using the single-bacterium RNA sequencing (MATQ-seq) and depletion of abundant sequences by hybridization (DASH) protocol as detailed below.

1. Prepare TYG medium, salt solution, calcium chloride, 10% sodium bicarbonate, and hemin solution according to the specified recipes. Filter-sterilize using 0.2 µm filters, degas TYG anaerobically for at least 4 hours, and store components as indicated.

2. Set up the FACS instrument with a 70 µm nozzle, a 4°C cooling block, and perform an automated drop delay using FACS Accudrop Beads. Allow the stream to stabilize for at least 30 minutes at a flow rate of 4.

3. Prepare the 96-well sorting plates under a sterile hood approximately 1 hour before the cultures reach the target OD600. For each well, mix 0.26 µL of Takara 10x lysis buffer, 0.03 µL of recombinant RNase inhibitor, 0.26 µL of 10x PBS, and 2.05 µL of nuclease-free water (accounting for 5 spare wells). Dispense 2.6 µL per well, spin down for 5 seconds, seal with Microseal ‘B’, and keep on ice.

4. Harvest the bacterial cell cultures at the desired OD600 (collecting 1 OD-equivalent of cells). Centrifuge for 4 minutes at 1,300 × g at ~21°C inside an anaerobic chamber, discard the supernatant, wash the pellet once with 1 mL of ice-cold 1x PBS, and resuspend in 1 mL of 50% RNAlater (1:1 v/v with 1x PBS). Keep samples on ice.

5. Dilute the cell sample 1:50 in ice-cold 1x PBS to a final volume of 1 mL in a 2 mL LoBind Eppendorf tube (alongside a negative control of 50% RNAlater in PBS). Load onto the FACS, adjust the flow rate to ~2,000 events/second, and set gates using FSC (linear, 600V), SSC (log, 500V), and FITC (log, 879V) to isolate intact cells from debris.

6. Confirm sorting accuracy using the ACDU and a sealed plate, checking for droplet deposition in target wells. Then, sort individual cells or populations into the prepared 96-well sorting plates using single-cell purity mode.

7. Immediately after sorting, seal the plate with Microseal ‘F’, spin down for 5 seconds, sonicate in a water bath at 35 kHz for 20 seconds, spin down again, and store at −80°C.

8. Perform reverse transcription and MATQ-seq amplification:
   a. Prepare the primer mix using GAT27 poly(dT), GAT27 5N3G, and GAT27 5N3T primers. Add water controls (negative) and pure RNA controls (positive) to designated wells.
   b. Perform pre-RT denaturation by adding DTT, primer mix, and dNTPs (incubate at 72°C for 3 min, then on ice for 1 min).
   c. Add the RT master mix containing SuperScript IV buffer, DTT, RNase inhibitor, and SuperScript IV reverse transcriptase. Run the multi-step RT thermal cycling program.
   d. Digest residual DNA oligonucleotides using T4 DNA polymerase with two sequential digestion (37°C) and inactivation (75°C / 80°C) cycles.
   e. Digest RNA using RNase H and RNase If at 37°C for 15 minutes, followed by 72°C for 15 minutes.
   f. Perform poly(C)-tailing using terminal transferase and dCTP at 37°C for 15 minutes, inactivated at 72°C for 15 minutes.
   g. Carry out second-strand cDNA synthesis using Thermopol buffer, dNTPs, GAT21 6N3G primer, and DeepVent (exo-) DNA polymerase with the specified thermal profile.
   h. Transfer one-quarter (6.55 µL) of each reaction to a new 96-well plate for PCR amplification, storing the remainder at −20°C as a backup.
   i. Perform PCR amplification using Thermopol buffer, dNTPs, GAT27 PCR primer, and DeepVent (exo-) polymerase for 25 cycles.
   j. Clean up the PCR products using a 1:1 ratio of AMPure XP beads, wash twice with freshly prepared 80% ethanol, air-dry briefly, and elute in 13 µL of nuclease-free water.
   k. Assess cDNA concentration using the Qubit 1x dsDNA HS kit and check fragment size distribution on a Bioanalyzer high-sensitivity DNA chip.

9. Construct Illumina sequencing libraries using a scaled-down Nextera XT protocol:
   a. Dilute cDNA samples to 0.4 ng/µL.
   b. Perform tagmentation by combining 1.25 µL of diluted cDNA with TD buffer and Amplicon Tagment Mix (ATM), incubating at 55°C for exactly 10 minutes, and neutralizing with NT buffer.
   c. Amplify libraries by adding Nextera PCR master mix (NTM) and Unique Dual Index (UDI) primers, running the specified PCR program.
   d. Clean up the libraries using a 1:1 AMPure XP bead ratio and elute in 13.1 µL of nuclease-free water.
   e. Quantify via Qubit and assess quality on a Bioanalyzer high-sensitivity chip.

10. Perform ribosomal cDNA depletion via DASH:
    a. Generate double-stranded DNA templates for sgRNAs using the oligonucleotide pool, fill-in primers, and KAPA HiFi HotStart ReadyMix, followed by Zymo Oligo Clean & Concentrator purification.
    b. Synthesize sgRNAs via in vitro transcription using the MEGAshortscript kit, treat with TURBO DNase, and purify using the Monarch Spin RNA Cleanup kit. Check size via Bioanalyzer.
    c. Calculate molarities, pool up to 12 cDNA libraries equimolarly, and prepare sgRNA-Cas9 RNP complexes at a 1:1,000:2,000 ratio (cDNA:Cas9:sgRNA).
    d. Digest ribosomal cDNA with the RNP complex at 37°C for 2 hours, digest Cas9 with Proteinase K at 37°C for 15 minutes, heat-inactivate at 95°C for 15 minutes, and clean up with a 1:1 AMPure bead ratio.
    e. Perform the final indexing PCR using DASH amplification primers, clean up with AMPure beads, quantify via Qubit, and verify library size using a Bioanalyzer.

11. Final sequencing and data analysis:
    a. Determine final library concentrations and average sizes to calculate molarity, adjust all libraries to 5 nM, and pool equimolarly.
    b. Sequence the pooled libraries on an Illumina platform in single-end mode with 100 cycles to achieve a minimum depth of ~10 million reads per library.
    c. Process the sequencing data by trimming Nextera adapters and MATQ-seq primers using BBDuk, assessing quality with FASTQC, mapping reads to the reference genome using Bowtie 2, and quantifying mapped reads using featureCounts and gff files.
```

label: 

defect_types: 

notes: 

---

## 18. R9029C3  (qpcr)

```
Please carry out the following CRISPR‑Cas9 knock‑in workflow on the Jurkat cells we are providing.  
1. Order and receive the following plasmids and oligos (all at 100 µM unless otherwise noted).  
  • pX330‑U6‑Chimeric_BB‑CBh‑hSpCas9 vector (linearized with BbsI) – 10 µg per prep.  
  • Donor plasmid (pUC57‑kan backbone with CMV‑DsRed, PolyA, left and right homology arms 1.5 kb each, GFP flanked by a short SGGS linker; blocking mutations in right arm).  
  • sgRNA oligo sense and antisense (crRNA) with the following sticky‑end sequences for BbsI cloning: sense 5′‑CACC‑[sgRNA]‑3′, antisense 5′‑AAAC‑[reverse complement]‑3′. Add an extra G at the 5′ if the target does not start with G.  
2. Phosphorylate and anneal the sgRNA oligos: combine 1 µl sense, 1 µl antisense, 1 µl 10× T4 ligation buffer, 0.5 µl T4 PNK, water to 10 µl. Incubate 30 min at 37 °C, then 15 min at 65 °C to heat‑inactivate. Dilute the duplex 1:200 in water.  
3. Digest the pX330 vector: 5–10 µg in 20 µl with BbsI, add 1 µl CIP (to prevent re‑ligation), 15 min at 37 °C, 15 min at 65 °C. Gel‑purify the linearised plasmid.  
4. Ligate the sgRNA duplex into the vector: mix 1 µl linearised vector, 1 µl annealed duplex, 1 µl 10× T4 ligation buffer, 0.5 µl T4 ligase, water to 6.5 µl. Incubate 2 h at 20 °C (or 25 °C). Heat‑inactivate 65 °C, 15 min. Set up a no‑insert control in parallel.  
5. Transform 2 µl of the ligation into 20 µl chemically competent Stbl3 E. coli by heat‑shock. Recover 1 ml LB + antibiotic (e.g., ampicillin) for 1 h at 37 °C, 200 rpm. Plate 100 µl on LB agar + antibiotic, incubate 12–16 h at 37 °C.  
6. Pick at least three colonies, inoculate 4–5 ml LB + antibiotic, grow 12–16 h at 37 °C, 200 rpm. Isolate plasmid by midi‑prep (endotoxin‑free kit). Verify sgRNA by sequencing (use the LKO.1 primer).  
7. Prepare the donor plasmid by midi‑prep (endotoxin‑free) and determine concentration.  
8. Prepare cells for nucleofection: grow Jurkat cells to 1–2×10⁶ cells per condition, spin 500 g for 5 min, wash twice with PBS. Resuspend 1×10⁶ cells in 100 µl Ingenio Nucleofector solution (or equivalent).  
9. Add plasmid mixture (equimolar amounts of donor plasmid and sgRNA plasmid; use 2–3 µg of each). Transfer to a 0.2 mm cuvette and electroporate with Amaxa program D‑23 (or test Neon or other device). Immediately add 100 µl warm RPMI + 10 % FBS from the 12‑well prep, then transfer to a 12‑well plate (1 ml per well).  
10. Incubate cells at 37 °C, 5 % CO₂. After 3 days, collect cells, wash with FACS buffer (PBS + 2 % FBS), stain with viability dye (Hoechst 33258, 1:5000).  
11. Sort live cells that are GFP⁺/DsRed⁻ into 96‑well plates containing 200 µl RPMI + 10 % FBS. Avoid outer wells; wrap plates in foil to prevent evaporation.  
12. Expand sorted cells for 3–4 weeks. Confirm GFP expression by flow cytometry.  
13. Extract genomic DNA from expanded clones (use QuickExtract or standard kit). Perform PCR with Phusion High‑Fidelity polymerase (12.5 µl H₂O to 25 µl final) using primers flanking the insertion site. Run a 2 % agarose gel to confirm a single band. Purify the PCR product and send for Sanger sequencing to verify the GFP insertion and absence of mutations.  
14. Return the validated GFP‑knock‑in clones to us; we will use them for downstream assays.  

Please keep detailed logs of reagent lot numbers, cell viability, transfection efficiencies, and any deviations from these conditions. Let us know if you need additional information or clarification.
```

label: 

defect_types: 

notes: 

---

## 19. RADA33A  (qpcr)

```
1. Generate A549 spheroids by washing a cultured flask with 10 mL PBS, adding 2 mL trypsin-EDTA, incubating for up to 3 minutes, and adding 6 mL of complete growth medium (RPMI-1640 with 10% FBS and 1% penicillin/streptomycin). 
2. Count cells and assess viability via Trypan Blue exclusion, then prepare a 10⁵ cells/mL suspension in complete medium. 
3. Dispense 100 µL of fresh medium followed by 100 µL of the cell suspension into each well of a 96-well ULA microplate to yield 10⁴ cells in 200 µL per well. 
4. Centrifuge the ULA microplate at 500 × g for 5 min at 20°C–25°C with no brake, then incubate for 4 days to form spheroids.
5. Capture one brightfield image per spheroid using a 4× objective on a microscope.
6. Set up migration chambers using 24-well TC inserts (loaded with 12 spheroids each) or 6-well TC inserts (loaded with 96 spheroids each) using a cut 1000 µL pipette tip. Adjust insert volume to ~80–100 µL (24-well) or ~1 mL (6-well), place inserts into wells containing medium with 10% FBS (~700 µL for 24-well, ~3 mL for 6-well), and ensure no air bubbles are introduced.
7. Incubate the migration chambers for 64 hours at standard conditions.
8. For 24-well inserts undergoing morphometric analysis, capture four consecutive overlapping images of the non-migrated fraction using a 2× objective, stitch them using Fiji (Grid/Collection stitching), and save as cropped JPEGs.
9. Collect the non-migrated spheroid fraction by adding PBS (200 µL for 24-well, 2 mL for 6-well) to the insert, gently lifting spheroids with a nonwoven swab, collecting the volume into a conical tube, repeating the wash, gently cleaning with a cotton swab, and pelleting at 500 × g for 5 min.
10. For crystal violet staining of the migrated fraction (24-well), wash the insert with PBS, stain in 0.5% crystal violet / 20% methanol solution for 10 min, wash with PBS and a cotton swab, air dry for 48 h, and capture a 3-by-3 grid of 4× images for stitching.
11. Alternatively, collect the migrated fraction by transferring the insert to warm trypsin, shaking for 10 min at 37°C, adding growth medium, and pelleting at 500 × g for 5 min.
12. Process collected pellets for gene expression profiling by extracting RNA, measuring concentration, and performing cDNA synthesis and RT-qPCR.
13. For intracellular hypoxia detection, add pimonidazole to the bottom well of 6-well chambers to a final concentration of 200 µM at the end of the 64-h assay, incubate for 3 h, and collect and fix the migrated and non-migrated fractions in 2% paraformaldehyde for 48 h at 4°C. (Note: trypsinize the non-migrated pellet prior to fixation).
14. Perform antibody staining on fixed pellets using anti-pimonidazole primary antibody (1:250 in 1% BSA / 0.05% Triton X-100) for 16 h at 4°C, followed by Alexa Fluor-647 secondary antibody (1:1000) for 1 h at room temperature, and analyze samples on a flow cytometer equipped with a 638 nm laser.
```

label: 

defect_types: 

notes: 

---

## 20. R135867  (elisa)

```
Please perform biochemical testing on the provided set of blinded serum samples (labeled with unique alphanumeric codes) to quantify Malondialdehyde (MDA), Total Superoxide Dismutase (T-SOD) activity, and Human Telomerase concentration according to the following protocol:

1. Serum Malondialdehyde (MDA) Assay: Quantify lipid peroxidation using the thiobarbituric acid reactive substances (TBARS) method with the Elabscience Colorimetric Assay Kit (Catalog # E-BC-K025-S). Measure absorbance at 532 nm on a calibrated microplate spectrophotometer. The expected linear detection range is 0.1 nmol/mL to 100 nmol/mL (analytical sensitivity limit of 0.38 nmol/mL). Target precision thresholds are an intra-assay CV of <4.9% and an inter-assay CV of <8.0%.

2. Total Superoxide Dismutase (T-SOD) Activity Assay: Quantify enzyme activity using the hydroxylamine method with the Elabscience T-SOD Activity Assay Kit (Catalog # E-BC-K019-S). Measure absorbance at 550 nm on a calibrated spectrophotometer. The expected linear detection range is 4.7 U/mL to 166 U/mL (analytical sensitivity limit of 4.7 U/mL). Target precision thresholds are an intra-assay CV of <2.8% and an inter-assay CV of <6.3%.

3. Human Telomerase Concentration Assay: Quantify telomerase concentration using the sandwich-ELISA method with the Elabscience Human TE ELISA Kit (Catalog # E-EL-H0164). Measure optical density at 450 nm (±2 nm) using a microplate reader. The expected linear detection range is 0.16 ng/mL to 10 ng/mL (analytical sensitivity limit of 0.09 ng/mL).

Quality Control & Deliverables:
Run all sample assays strictly in triplicate wells. Enforce an automatic re-assay protocol for any sample where the variance between replicate wells exceeds a CV of 10%. Ensure laboratory personnel remain fully blinded to sample codes and time points during testing. Provide a complete data report containing the raw absorbance/OD values, calculated biomarker concentrations/activities, intra-assay CVs, and notes on any sample re-runs.
```

label: 

defect_types: 

notes: 

---

## 21. R73EA7F  (qpcr)

```
Please run the mouse embryonic stem cell (mESC) 2‑D induction followed by 3‑D budoid generation on our samples using the protocol below.  

1. **Cell line** – Use EmbryoMax® embryonic stem cell line, strain 129/SVEV, passage 11 (CMTI‑1, RRID: CVCL_GS41).  

2. **Media preparation**  
   - **DMEM base (500 mL)**: 434 mL DMEM high‑glucose + GlutaMAX, 50 mL ES‑FBS (heat‑inactivated, aliquoted), 5 mL Pen‑Strep (10 000 U/mL), 5 mL MEM‑NEAA (100×), 5 mL 100 mM sodium pyruvate, 1 mL 50 mM 2‑mercaptoethanol. Filter‑sterilize, store 4 °C ≤ 1 month.  
   - **DMEM+++ (50 mL)**: 50 mL DMEM base, 50 µL LIF (100 µg/mL) → 100 ng/mL final, 25 µL PD0325901 (10 mM) → 1 µM, 50 µL CHIR‑99021 (10 mM) → 3 µM. Store 4 °C ≤ 1 week.  
   - **NNE medium (50 mL)**: 48 mL GMEM, 750 µL KnockOut SR, 500 µL MEM‑NEAA (100×), 500 µL 100 mM sodium pyruvate, 100 µL Normocin (10 000 U/mL) → 0.2 % v/v, 91 µL 2‑mercaptoethanol (50 mM) → 91 µM. Protect from light, store 4 °C ≤ 1 week.  
   - **Induction medium I (per 12‑well)**: 12.5 mL NNE + 12.5 µL BMP‑4 (100 µg/mL) → 100 ng/mL + 6.25 µL SB‑431542 (10 mM) → 1 µM. Prepare fresh.  
   - **Induction medium II (per 12‑well)**: 12.5 mL NNE + 12.5 µL BMP‑4 (100 ng/mL) + 12.5 µL FGF‑10 (100 µg/mL) → 100 ng/mL + 12.5 µL CHIR‑99021 (10 mM) → 3 µM. Prepare fresh.  
   - **Budoid generation medium (per 60 budoids)**: 7 mL NNE + 31.5 µL FGF‑8b (100 µg/mL) → 450 ng/mL + 21 µL Wnt‑3a (100 µg/mL) → 300 ng/mL. Prepare fresh.  

3. **2‑D induction (days 0‑7)**  
   a. Thaw and expand mESCs in DMEM+++; change medium every 2–3 days. Passage once cells reach 70‑80 % confluence. Use cells after at least two passages post‑thaw.  
   b. **Day 0 – seeding**: Coat a 12‑well plate with 0.1 % gelatin (500 µL/well, 20 min, RT). Detach 70‑80 % confluent cells from a 6‑well plate with 0.25 % trypsin‑EDTA (500 µL/well, 37 °C 1‑2 min), neutralize with 1 mL DMEM base, centrifuge 137 g 5 min RT, resuspend in NNE. Count and seed 1 mL/well at 40 000 cells/mL (≈40 000 cells per well). Incubate 5 % CO₂, 37 °C, gentle rocking, no disturbance for 24 h.  
   c. **Day 1**: Warm NNE to RT, aspirate medium, wash once with 1 mL PBS, add 1 mL fresh NNE.  
   d. **Day 3**: Prepare induction medium I. Aspirate, wash with PBS, add 1 mL induction medium I.  
   e. **Day 5**: Prepare induction medium II. Aspirate, wash twice with PBS, add 1 mL induction medium II.  
   f. **Day 7**: Cultures should show dome‑like structures. Optional immunostaining/qPCR for TP63, EPCAM, Prrx1, etc. Proceed to budoid step.  

4. **3‑D budoid generation (days 7‑12)**  
   a. Prepare budoid generation medium as above and keep on ice. Pre‑warm DMEM base and trypsin‑EDTA to 37 °C.  
   b. In a 96‑well U‑bottom plate, fill the outer ring (24 wells) with 200 µL PBS 1× to reduce evaporation; budoids will be seeded only in the inner 60 wells.  
   c. Wash each 12‑well induction well with 1 mL PBS, aspirate, then add 300 µL trypsin‑EDTA per well (37 °C 1‑2 min). Neutralize with 600 µL DMEM base, gently resuspend, collect all cells, centrifuge 400 g 5 min RT.  
   d. Resuspend pellet in budoid generation medium, count, and dilute to 90 000 cells/mL. Seed 100 µL per inner well (≈9 000 cells/well). Use a multichannel pipette, tip just above the bottom without touching.  
   e. **Day 8**: Verify clear aggregates in wells.  
   f. **Day 9**: Change half‑volume. Warm NNE to RT, remove 50 µL from each well (angled to avoid buds), add 50 µL fresh NNE gently along the side.  
   g. **Day 11**: Repeat half‑volume change as in day 9.  
   h. **Day 12**: Budoids should be elongated. Collect any for downstream analysis (use low‑attachment tips, optionally coat tips with 1‑3 % BSA).  

5. **Supplies & equipment** – Ensure we have the listed plates (6‑well, 12‑well, 96‑well U‑bottom), gelatin, PBS, trypsin‑EDTA, sterile filters, centrifuge, 5 % CO₂ incubator, biosafety cabinet, cell counter, multichannel pipettes, low‑binding tubes, and all recombinant proteins (BMP‑4, SB‑431542, FGF‑10, CHIR‑99021, FGF‑8b, Wnt‑3a) at the specified concentrations.  

6. **Timing** – The entire workflow is 12 days from seeding (day 0) to final budoid elongation (day 12). Please keep media changes at the same time each day for consistency.  

7. **Read‑out** – Confirm budoid elongation efficiency (≥ 80 % elongated buds) and optionally perform immunostaining or qPCR for limb‑bud markers as described in Skoufa et al., Sci Adv 2023.  

Let us know if any reagents are missing or if you need clarification on any step. Thanks.
```

label: 

defect_types: 

notes: 

---

## 22. R7EC537  (elisa)

```
Please run the SpL ELISA on our provided samples using the following procedure:

1. Coat the wells of a 96-well microtitre plate overnight at 4°C with unlabelled protein L (SpL) from P. magnus at 1 µl/mg per well in carbonate-bicarbonate buffer (pH 9.6).
2. Block the plate with a bovine serum albumin solution, then wash 4 times with PBS-Tween.
3. Add 50 µl of each of our animal serum samples (prepared at 1 mg/ml) to the wells, incubate for 1 hour at room temperature, and wash the plate.
4. Add 50 µl of peroxidase-labeled SpL conjugate, diluted 1:5000 in PBS-non-fat milk, to each well. Incubate for 1 hour at room temperature, then wash the plate 4 times with PBS-Tween.
5. Add 50 µl of 4 mg/ml o-phenylenediamine (OPD) solution to each well and incubate for 15 minutes at room temperature in the dark.
6. Stop the reaction by adding 50 µl of 3M H2SO4 solution.
7. Visually assess the plates for color development and read the absorbance in a microplate reader at 492 nm.
8. Calculate the cut-off point as three times the mean optical density of the negative controls.
```

label: 

defect_types: 

notes: 

---

## 23. RE8030F  (viability)

```
Please take the following steps with our SF8628 H3K27M‑pDMG cells.

1. **Cell culture** – Thaw and expand the SF8628 (SCC127) line in DMEM‑High Glucose (Sigma D6546) supplemented with 10 % FBS (R&D Systems S11150H). Maintain at 37 °C, 5 % CO₂, changing media every 3–4 days. Split when ~70‑80 % confluent, using 0.05 % Trypsin‑EDTA (Life Technologies 25300062) for 5 min at 37 °C, then quench with 2 × volume media, spin 300 × g for 5 min, resuspend in fresh media. Verify mycoplasma negativity (LookOut PCR kit) and keep cells ≤10 passages.

2. **Generate GEDI reporter line**  
   a. Clone the pMe:GC150‑p2A‑mApple cassette (gift from Finkbeiner Lab) into the pLenti‑CMV‑Puro backbone (Addgene 17452) using Invitrogen Gateway LR Clonase II (11791020).  
   b. Produce lentivirus in HEK293T cells (ATCC CRL‑3216) by co‑transfecting the pLenti‑GEDI vector with psPAX2 (Addgene 12260) and pMD2.G (Addgene 12259) using TransIT‑LT1 (Mirus 2300). Harvest supernatant at 48 h and 72 h, pool, and concentrate with Lenti‑X (Takara 631231).  
   c. Transduce SF8628 cells with the concentrated virus (MOI ~5) in the presence of 8 µg/mL polybrene. After 48 h replace media, then begin selection with 1 µg/mL puromycin.  
   d. Enrich mApple‑positive, GC150‑positive cells by FACS. Expand the sorted population for downstream assays.

3. **JQ1 stock preparation** – Dissolve JQ1 (Selleck S7110) in DMSO to 50 mM. Dilute 1:5 into 200‑proof ethanol to make a 10 mM intermediate stock (helps solubility). Store aliquots at –20 °C. Dilute this stock into cell culture media to the final concentrations indicated in our experimental plan (keep final DMSO ≤ 0.1 %).

4. **X‑ray irradiation** – Plate GEDI‑expressing SF8628 cells in clear‑bottom 96‑well optical plates (VWR 29444) at ≤5,000 cells/well in 100 µL media. Irradiate plates on the XRAD 225XL (PXI Precision X‑ray) using 225 kV, 13.3 mA, SSD = 40 cm, dose rate 2.2 Gy/min, fixed rotation. Deliver 8 Gy (≈3 min exposure). Include sham‑irradiated (0 Gy) plates that are handled identically but not exposed.

5. **Drug treatment** – Add JQ1 (or vehicle) to appropriate wells immediately after irradiation (or at the start of the experiment for drug‑only conditions) to reach the desired final concentrations. Keep total volume at 100 µL per well.

6. **Viability endpoints** – At the indicated time points (e.g., 24 h, 72 h) measure cell viability:  
   a. For caspase‑3/7 activity, add Caspase‑Glo 3/7 reagent (VWR PAG8091) per manufacturer’s protocol.  
   b. For overall ATP, add Cell‑Titer‑Glo (VWR PAG7572) per manufacturer’s protocol.  
   Record luminescence on a Biotek Synergy LX. Include media‑only wells as blanks for background subtraction.

7. **Live‑cell imaging** – Using a Biotek Lionheart FX, set up time‑lapse acquisition of the same fields in each well:  
   - 20× objective, mApple exposure 150 ms, GC150 exposure 300 ms.  
   - Capture 10 × 10 montage per well.  
   - Imaging schedule: for irradiated cells at 0, 3, 6, 12, 18, 24, 36, 72 h post‑irradiation; for drug‑treated cells at 0, 24, 72 h.  
   - Keep plates at 37 °C, 5 % CO₂ throughout imaging.

8. **Image processing** – Export raw images and process with Biotek Gen5 v3.11: background correction, deconvolution, stitching. Export the GC150 and mApple channel intensities for each cell.

9. **GEDI ratio calculation** – Use the provided ImageJ (v1.54p) macro to compute GC150/mApple ratios per cell. Determine death thresholds based on the high‑dose (≥8 Gy) or high‑drug (≥10 µM JQ1) control wells. Export the per‑cell ratio data as CSV.

10. **Cell tracking** – Run TrackMate v7.14 in ImageJ on the time‑series to link individual cells across frames (LoG detector, LAP tracker). Export the tracks with associated GEDI ratios.

11. **Data analysis** – Import the CSV files into R (v4.3.1) using the tidyverse. Plot GEDI ratio trajectories at each time point, generate summary statistics (mean ± SEM), and perform:  
    - One‑way ANOVA with Tukey post‑hoc for dose‑response within a time point.  
    - One‑way ANOVA for a single dose across time points.  
    - Two‑sample t‑test for pairwise GEDI ratio comparisons between two time points.  
    Use GraphPad Prism 8 for figures if preferred. All analyses should include at least two biological replicates (independent cell passages) and three technical replicates (wells) per condition.

Please let me know if any reagents are unavailable or if you need clarification on the imaging schedule or analysis scripts (we can provide the ImageJ macro and R markdown files). Thank you.
```

label: 

defect_types: 

notes: 

---

## 24. R4D4DDF  (growth_curve)

```
Please carry out the following experiment using the samples we provided (HEK293T cells, plasmids pYZ484 and pYH3, and a vial of the HRP‑pHLIP fusion protein we supplied). The goal is to synthesize HA‑DA, express and purify HRP‑pHLIP, transfect HEK293T cells with the optogenetic system, and encapsulate the engineered cells in an HA‑DA hydrogel using the supplied HRP‑pHLIP for crosslinking. 

**Materials you need to have on hand (all reagents are available in our inventory):**  
- E. coli BL21 (DE3) competent cells  
- HEK293T cells (high‑glucose DMEM, 10 % FBS, 1 % penicillin/streptomycin)  
- Plasmids pYZ484 and pYH3 (already provided)  
- HRP‑pHLIP fusion protein (50 µg/mL solution in PBS, already provided)  
- Hyaluronic acid (MW 12 kDa, 1 g)  
- Dopamine (DA, 10 mM final concentration)  
- EDC (5 mM final)  
- NHS (10 mM final)  
- PBS (pH 7.4)  
- Deionized water and deuterium oxide (for NMR)  
- Luria–Bertani (LB) medium, LB agar (with 60 µg/mL kanamycin), IPTG (0.5 mM), IPTG stock (1 M)  
- Lysis buffer (50 mM NaH₂PO₄, 300 mM NaCl, 10 mM imidazole)  
- Wash buffer (50 mM NaH₂PO₄, 300 mM NaCl, 20 mM imidazole)  
- Elution buffer (50 mM NaH₂PO₄, 300 mM NaCl, 250 mM imidazole)  
- Ni‑NTA resin, column (5 mL capacity)  
- 2 % (w/v) HA‑DA precursor solution (prepared after synthesis)  
- 2 mM H₂O₂ (freshly prepared)  
- PBS pH 6.5 and PBS pH 7.4 for washing  
- Lipo293 TM reagent (4 µL per 125 µL DNA mix)  
- LED array (660 nm/730 nm, 1 mW cm⁻²) for 24‑h stimulation cycles  

**Procedure**

1. **Synthesize HA‑DA conjugate**  
   1.1 Weigh 1 g HA and dissolve in 100 mL PBS (pH 7.4). Stir until fully dissolved at room temperature.  
   1.2 Add EDC to 5 mM final concentration and NHS to 10 mM final concentration. Adjust the mixture to pH 5.0 using 10 mM HCl or 10 mM NaOH. Stir at room temperature for 6 h.  
   1.3 Add DA to 10 mM final concentration. Cover the flask with a nitrogen‑tight valve and stir for 24 h at room temperature (prevent oxidation).  
   1.4 Transfer the crude product into a 14 kDa MWCO dialysis bag and dialyze against deionized water at 4 °C for 72 h. Replace dialysis water every 8 h.  
   1.5 Freeze‑dry the dialyzed product to a spongy solid.  
   1.6 Confirm grafting by ¹H NMR (dissolve in D₂O). Record spectra and integrate peaks to calculate grafting efficiency.

2. **Clone, express, and purify HRP‑pHLIP**  
   2.1 Use the sequence you already have for the pET28a‑HRP‑pHLIP plasmid. Transform BL21 (DE3) with the plasmid via heat shock (42 °C, 45 s).  
   2.2 Plate on LB agar + 60 µg/mL kanamycin; incubate 37 °C overnight. Pick a single colony and inoculate 5 mL LB + 60 µg/mL kanamycin; grow 16 h at 37 °C, 200 rpm.  
   2.3 Dilute 1 % (v/v) into 30 mL fresh LB + kanamycin; grow to OD₆₀₀ ≈ 0.8.  
   2.4 Induce with IPTG (final 0.5 mM); incubate 8 h at 16 °C, 220 rpm.  
   2.5 Harvest cells by centrifugation (8 000× g, 10 min, 4 °C). Resuspend pellet in 10 mL cold lysis buffer (1 L per 5 g pellet).  
   2.6 Lyse by sonication (30 % amplitude, 5 s on/5 s off, 15 min total) on ice.  
   2.7 Clarify lysate (12 000× g, 30 min, 4 °C). Collect supernatant.  
   2.8 Equilibrate Ni‑NTA column with 5× column volumes of lysis buffer. Load the clarified lysate, hold 2 min, then wash with 5× column volumes of wash buffer.  
   2.9 Elute with 10× column volumes of elution buffer. Collect fractions, assay for HRP activity (e.g., TMB substrate). Pool active fractions.  
   2.10 Final rinses: 3× lysis buffer, 5× water, 2× 20 % ethanol. Store the purified HRP‑pHLIP at 2–8 °C.

3. **Transient transfection of HEK293T cells**  
   3.1 Seed 5 × 10⁵ HEK293T cells per well in 6‑well plates; incubate overnight until 70–80 % confluent.  
   3.2 Replace medium with 1 mL fresh DMEM + 10 % FBS (no antibiotics).  
   3.3 For each well, prepare two tubes:  
        – Tube A: 125 µL DMEM (no serum, no antibiotics) + 2.5 µg plasmid DNA (mix pYZ484 and pYH3 in the required ratio).  
        – Tube B: 125 µL DMEM + 4 µL Lipo293 TM.  
   3.4 Gently combine the contents of tubes A and B; let sit at room temperature 15 min (or up to 6 h).  
   3.5 Add the 250 µL mixture dropwise into the corresponding well; gently mix.  
   3.6 Incubate 24 h, then stimulate with the LED array (660 nm/730 nm, 1 mW cm⁻²). Apply alternating 5 s pulses of 660 nm (“ON”) and 730 nm (“OFF”) for the duration of the 24‑h stimulation cycle.  
   3.7 Replace medium every 24 h; sample supernatant every 6 h for 72 h to assay SEAP secretion.

4. **Single‑cell encapsulation**  
   4.1 Harvest engineered HEK293T cells (1 × 10⁶ cells) by trypsinization, wash, and resuspend in 1 mL PBS pH 6.5 containing HRP‑pHLIP (50 µg/mL). Incubate 30 min at room temperature.  
   4.2 Centrifuge 150× g, 5 min; discard supernatant. Wash cells three times with PBS pH 6.5.  
   4.3 Prepare a hydrogel precursor: dissolve the HA‑DA product in PBS to make 2 % (w/v); add 2 mM H₂O₂ immediately before use.  
   4.4 Resuspend the HRP‑pHLIP‑labeled cells in 1 mL of the HA‑DA/H₂O₂ solution; stir gently for 30 min at room temperature to crosslink via HRP catalysis.  
   4.5 Collect the hydrogel‑encapsulated cells by centrifugation 150× g, 5 min. Wash three times with PBS pH 7.4 to remove excess reagents.  
   4.6 Store or assay the encapsulated cells as needed (e.g., fluorescence imaging, viability, cytokine secretion).

**Deliverables**  
- ¹H NMR spectrum of the HA‑DA conjugate with grafting efficiency annotation.  
- SDS‑PAGE (or Coomassie) of purified HRP‑pHLIP, with a protein marker lane.  
- SEAP secretion profile (concentration vs. time) for the optogenetically controlled cells.  
- Representative fluorescence images of encapsulated cells (HA‑DA shell labeled with FAM, nuclei with DAPI).  

Please confirm receipt of the sample list and let us know the estimated timeline for completion. Thank you.
```

label: 

defect_types: 

notes: 

---

## 25. R00E584  (qpcr)

```
Please process our hiPSC samples using the following targeted genome editing and amplicon sequencing workflow:

1. Maintain and prepare the hiPSC cultures (e.g., KOLF2.1J cells) in antibiotic-free complete growth medium (mTeSR Plus with 1× penicillin/streptomycin) supplemented with 1× CEPT cocktail on Geltrex-coated plates.

2. Deliver genome-editing reagents using either plasmid transfection (e.g., using Lipofectamine Stem with a 3:1 reagent-to-plasmid ratio, combining 2 μg PX458 plasmid and 1 μg Alt-R HDR donor oligo for knock-ins, or 0.5 μg pegRNA plasmid and 1.5 μg pCMV-PEmax-P2A-GFP for prime editing) or ribonucleoprotein (RNP) electroporation (e.g., Neon NxT system at 1,300 V, 10 ms, single pulse, using RNP complexes prepared by annealing 50 μM sgRNA with 19.5 μM Cas9 nuclease and adding 1 μg HDR donor oligo where applicable). 

3. Twenty-four hours post-transfection, enrich edited cells via fluorescence-activated cell sorting (FACS) using freshly prepared, sterile-filtered FACS buffer (PBS without Ca2+/Mg2+, 2% FCS, 1× CEPT). Sort GFP-positive cells and recover them in growth medium containing CEPT, maintaining antibiotics during sorting to prevent contamination.

4. Expand bulk-sorted cells or isolate single-cell clones by seeding at 1.5 cells per well in 96-well plates with CEPT-supplemented medium until colonies reach 60–80% confluency.

5. Extract genomic DNA by preparing fresh DNA lysis buffer (PBS, 1% Tween 20, 0.2 mg/mL Proteinase K), adding 50 μL to each well containing cell pellets, incubating at 56 °C for 1 h, and inactivating the enzyme at 95 °C for 15 min.

6. Perform targeted amplification of the edited locus using the first PCR mix (1× Blitz PCR buffer, 0.2 mM each dNTPs, 0.36 μM forward and reverse primers, 0.04 U/μL Blitz DNA polymerase, and 20 ng genomic DNA lysate in a 7 μL total reaction volume). Run the thermal cycler at 98 °C for 1 min; 19 cycles of 98 °C for 20 s, 60 °C for 20 s, 72 °C for 30 s; followed by 72 °C for 4 min.

7. Incorporate sample-specific barcodes and sequencing adapters via a second-round index PCR using the same mix composition and thermal cycling conditions, substituting the first PCR product as the template.

8. Pool the indexed PCR products, run them on a 1.5% agarose gel, excise the ~450 bp library band, and purify using a gel extraction kit. 

9. Quantify the purified library using a fluorometric or qPCR-based assay (e.g., Qubit or NEBNext Library Quant Kit). 

10. Sequence the libraries on the appropriate platform (such as an Illumina MiSeq i100 Plus, loading 60 to 80 pM of the final library) and extract the resulting FASTQ files for downstream analysis.
```

label: 

defect_types: 

notes: 

---

## 26. R0A00AE  (qpcr)

```
Please perform the FlipNanoLuc reporter assays on our provided samples using the following protocol:

1. Cell Culture and Reagents
- Maintain HEK293T cells in complete DMEM (high-glucose DMEM, 10% heat-inactivated FBS, 1x homemade Pen/Strep [0.626 mg/mL benzylpenicillin potassium and 1 mg/mL streptomycin sulfate in PBS]).
- Maintain BHK cells stably expressing hACE2 in complete MEM (MEM, 10% heat-inactivated FBS, 1x Pen/Strep, and 3 μg/mL puromycin).
- Prepare 1x lysis buffer: 150 mM NaCl, 50 mM Tris-HCl (pH 7.4), 1% (v/v) Triton X-100, and 1x cOmplete Mini protease inhibitor cocktail added immediately before use (1 tablet per 10 mL).

2. Generation of Stable Cell Lines via Retroviral Transduction
- Seed HEK293T packaging cells in a 3.5 cm dish at 5 × 10^5 cells/dish in 2 mL complete DMEM. Incubate overnight at 37 °C with 5% CO2.
- Prepare transfection mix in 200 μL Opti-MEM: 1.0 μg FlipNanoLuc retroviral vector, 0.7 μg gag-pol plasmid, and 0.3 μg VSV-G plasmid. Add 6 μL PEI MAX (1 mg/mL, 1:3 DNA:PEI ratio), vortex, and incubate at room temperature for 15–20 min.
- Add complexes dropwise to cells. Incubate for 48 h.
- Harvest supernatant, centrifuge at 500 × g for 5 min at 4 °C, and collect the clarified supernatant.
- Seed target HEK293T cells at 1 × 10^5 cells/dish in a 3.5 cm dish. Next day, aspirate medium, add 200 μL clarified retroviral supernatant, and bring volume to 2 mL with complete DMEM. Incubate for 48 h.
- Select stable populations using complete DMEM containing 1.0 μg/mL puromycin until non-transduced control cells die (3–5 days). Maintain thereafter without puromycin.

3. Protease Overexpression Assay
- Seed HEK293T cells in 24-well plates at 7 × 10^4 cells/well in 500 μL complete DMEM. Incubate overnight.
- Co-transfect 0.5 μg FlipNanoLuc reporter plasmid and 0.5 μg protease expression plasmid (or pCAG-empty mock control) per well using Opti-MEM and PEI MAX (1:3 DNA:PEI ratio, 3 μL per well). Do not change medium.
- Harvest by aspirating medium and lysing in 100 μL 1x lysis buffer at 48 h post-transfection for 3CLpro, or 24 h post-transfection for Caspase-3. Keep lysates on ice for no more than 10 min.

4. Apoptosis Detection Assay (Staurosporine Treatment)
- Seed HEK293T cells stably expressing Casp3A-FlipNanoLuc in 24-well plates at 7 × 10^4 cells/well. Incubate overnight.
- Treat cells with 1 μM staurosporine (diluted from 200 mM DMSO stock into complete DMEM) or an equivalent vehicle control for 6 h at 37 °C, alongside a 0-h vehicle control.
- Collect culture medium from each well into a 1.5 mL microcentrifuge tube, centrifuge at 500 × g for 5 min at 4 °C, and aspirate supernatant down to ~50 μL before removing completely.
- Add 100 μL 1x lysis buffer to the emptied well to lyse adherent cells, transfer lysate to the corresponding tube, and thoroughly resuspend the cell pellet.

5. Human Coronavirus OC43 Infection Assay
- Seed HEK293T cells stably expressing 3CLpro-SL1-FlipNanoLuc in 96-well plates at 3.0 × 10^4 cells/well in 100 μL complete DMEM. Incubate overnight.
- Infect cells with OC43 inoculum at MOI 1 (or MOI 0.5 and 1.0 for dose-response tests) in 100 μL complete DMEM, or add virus-free medium for mock controls. Incubate for 48 h at 37 °C (or 72 h where specified) without medium replacement.
- Aspirate medium and lyse cells directly in 50 μL 1x lysis buffer.

6. SARS-CoV-2 Infection Assay (BSL-3 Facility)
- Seed BHK-hACE2 cells in 24-well plates at 1.5 × 10^5 cells/well in 500 μL complete MEM. Incubate overnight.
- Transfect cells with 1.0 μg 3CLpro-SL1-FlipNanoLuc reporter plasmid using 3 μL PEI MAX in 100 μL Opti-MEM per well. Incubate for 24 h.
- Aspirate transfection medium completely, wash once with plain MEM, and infect with SARS-CoV-2 inocula at MOI 1, 3, 5, or 10 in 100 μL plain MEM (or plain MEM for mock). Adsorb for 3 h at 37 °C.
- Aspirate inoculum, add 500 μL complete MEM, and incubate for 24 h at 37 °C.
- Aspirate medium and lyse cells in 100 μL 1x lysis buffer.

7. Luminescence Measurement and Normalization
- Set up a white 384-well plate, dispensing samples into every other well to minimize crosstalk.
- For each lysate, set up two separate wells: add 10 μL lysate + 10 μL Nano-Glo reagent in one well, and 10 μL lysate + 10 μL Bright-Glo reagent in the other. Mix by pipetting three times.
- Wait 2–5 min, then measure NanoLuc and firefly luminescence on a Varioskan LUX luminometer using top reading, 1,000 ms integration time, and default gain.
- Calculate normalized activity as NanoLuc luminescence divided by firefly luminescence. Calculate fold induction relative to the appropriate control (mock-infected, empty vector, or 0-h vehicle set to 1.0).
- Perform assays with three biological replicates per condition and repeat independent experiments at least twice.
```

label: 

defect_types: 

notes: 

---

## 27. RE689A3  (elisa)

```
Please perform a Luminex multiplex immunoassay and data analysis on our submitted MenACWY-CRM197 conjugate samples using the following procedure:

1. **Bead Coupling**: Couple serotype-specific mouse monoclonal antibodies to Luminex MagPlex-C microspheres (anti-MenA to B20, anti-MenC to B25, anti-MenW to B33, and anti-MenY to B77) using EDC/sNHS chemistry. For each coupling, activate 1.25 million washed beads in 80 µL of 100 mM sodium phosphate buffer (pH 6.2) by adding 10 µL of 50 mg/mL sNHS and 10 µL of 50 mg/mL EDC. Rotate for 20 minutes at room temperature in the dark. Incubate activated beads with the corresponding mAb in 500 µL of 50 mM MES buffer (pH 5.0) for 2 hours under rotation, protected from light. Wash twice with PBS containing 0.05% Tween20, block with PBS containing 0.05% Tween20 and 0.2% BSA for 30 minutes, wash twice more, and store in PBS with 0.05% Tween20 at a final concentration of 1.25 × 10^6 beads/mL.

2. **Sample Dilution & Assay Setup**: Reconstitute the provided standard and lyophilized vaccine samples in 600 µL of 9.0 g/L NaCl solution to reach target concentrations (20 µg/mL for MenA, 10 µg/mL for MenC, MenW, and MenY). Dilute standards and test samples 1:1000 in sample diluent (PBS with 0.05% Tween20). Dispense standards and samples in duplicate in the first column of a Greiner plate and perform 2.5-fold serial dilutions across the plate in sample diluent. Prepare a bead mixture by diluting each coupled bead stock 1:10 in sample diluent, and add 10 µL of this bead mix to every well.

3. **Incubation & Detection**: Incubate the plate for 1 hour at room temperature with agitation at 800 rpm. Wash three times with sample diluent using a magnetic plate washer. Add 100 µL of purified rabbit anti-CRM197 primary antibody to each well and incubate for 1 hour at 800 rpm. Wash three times, then add 50 µL of R-PE-conjugated goat anti-rabbit Fab secondary antibody (diluted 1:200) to each well and incubate for 30 minutes at 800 rpm. Wash three times, resuspend the beads in 100 µL of 1X PBS, agitate, and measure median fluorescence intensity (MFI) on a Bio-Plex 200 system using high-sensitivity settings.

4. **Data Analysis**: Analyze the MFI data using a Parallel Line Assay (PLA) model on log10(Dose)–log10(Response) linear ranges (minimum 4 points per curve). Confirm assay validity via ANOVA (requiring regression p < 0.05, non-linearity p > 0.05, and non-parallelism p > 0.05) before calculating test sample relative concentrations and confidence intervals against the standard.

5. **HPAEC-PAD**: For orthogonal quantification, perform sample pre-treatment according to Rech et al. and run HPAEC-PAD separation following the analytical conditions described in De Ricco et al.
```

label: 

defect_types: 

notes: 

---

## 28. RC6A900  (elisa)

```
Please run the IL‑17A ELISA on our patient serum samples as follows:

1. **Coating the Plate**  
   • Take a 96‑well filter plate (Merck Millipore MX‑PLATE).  
   • Add 100 µL of the monoclonal anti‑human IL‑17 capture antibody (concentration as per manufacturer’s instructions) to each well.  
   • Incubate the plate for 1 h 30 min at room temperature (RT, ~22 °C).  
   • After incubation, wash the plate 4× with 200 µL PBS‑Tween 20 (0.05%) per well; discard wash buffer.

2. **Adding Samples**  
   • Pipette 100 µL of each patient serum sample into the designated wells.  
   • Include a blank well with PBS‑Tween 20 and a positive control well with 10 ng mL⁻¹ IL‑17 (use the IL‑17A standard from Bio Basic, Cat #RC212‑28).  
   • Incubate the plate for 1 h 30 min at RT.  
   • Wash the plate again 4× with PBS‑Tween 20.

3. **Detection Antibody**  
   • Add 100 µL of biotin‑conjugated anti‑human IL‑17 detection antibody to each well.  
   • Incubate for 1 h 30 min at RT.  
   • Wash 4× with PBS‑Tween 20.

4. **Streptavidin‑Peroxidase**  
   • Add 100 µL of peroxidase‑labeled streptavidin conjugate to each well.  
   • Incubate for 1 h at RT.  
   • Wash 4× with PBS‑Tween 20.

5. **Substrate Development**  
   • Add 100 µL of TMB substrate solution (ready‑to‑use) to each well.  
   • Allow color to develop for 10–15 min at RT (monitor; stop when controls reach ~0.5–0.8 OD₄₅₀).  
   • Stop the reaction with 50 µL of 1 N H₂SO₄ or 1 N HCl per well.

6. **Reading**  
   • Measure absorbance at 450 nm using a plate reader.  
   • Generate a standard curve from the known IL‑17 concentrations (0–50 ng mL⁻¹) to calculate patient IL‑17 levels.

Please provide the final results (ng mL⁻¹ IL‑17 per sample) and include the standard curve data. Thank you.
```

label: 

defect_types: 

notes: 

---

## 29. R41CF2F  (elisa)

```
Please process our provided iPSC samples through the complete protocol to generate mature macrophages (iMCs), characterize them, and run inflammasome activation assays. Carry out the following workflow:

1. Culture and passage the iPSCs on vitronectin-coated plates using StemFlex medium with daily media changes, following standard handling to maintain cell clumps.
2. Form embryoid bodies (EBs) by harvesting the iPSCs with PBS-EDTA, counting them, and seeding 50,000 cells per well in low-adherent U-bottom 96-well plates in StemFlex media supplemented with 50 ng/mL BMP-4 and 10 μM ROCK inhibitor, performing spins and media feeds on days 2 and 4.
3. Generate myeloid precursors by transferring the 5-day-old EBs into gelatin-coated T75 or T175 flasks using myeloid precursor base medium (X-VIVO 15, 2 mM GlutaMAX, 100 IU/mL penicillin-streptomycin, 0.1 mM β-mercaptoethanol) supplemented with 50 ng/mL M-CSF and 25 ng/mL IL-3. Maintain these cultures with weekly media changes and top-ups for 3 to 4 weeks until myeloid precursors are actively produced in suspension.
4. Harvest the floating myeloid precursors through a 70 μm cell strainer, centrifuge at 300 × g, and differentiate them into mature macrophages (iMCs) by culturing 500,000 cells in 100 mm dishes using macrophage differentiation medium (RPMI 1640, 10% heat-inactivated FBS, 2 mM L-GlutaMAX, 100 IU/mL penicillin-streptomycin) with 100 ng/mL M-CSF for 7 days, supplementing with fresh media on day 4 or 5. Harvest the iMCs on day 7 using lidocaine monohydrate in DPBS.
5. Perform flow cytometry to assess macrophage markers (CD14, CD16, CD44, CD64, and intracellular CD68) using viability dye, blocking solution, fixation/permeabilization buffers, and respective isotype controls, recording at least 10,000 events per sample.
6. Conduct a phagocytosis assay by seeding iMCs on glass coverslips in 24-well plates, incubating with 1:10 diluted fluorescent yellow-green latex amine-modified polystyrene beads in OptiMEM for 30 and 90 minutes at 37°C, staining with LysoTracker Red DND-99, fixing with 4% PFA, permeabilizing with 0.1% Triton X-100, quenching with 50 mM ammonium chloride, blocking with 0.5% BSA, and mounting with DAPI antifade medium. Image via confocal microscopy at 63X and quantify the percentage of DAPI+bead+ cells using Fiji.
7. Prepare whole cell proteomics samples by challenging iMCs (1x10^6 cells per well in 6-well plates) with 100 ng/mL LPS for 6 to 24 hours, washing and collecting cell pellets, lysing in 1% SDC lysis buffer with TCEP and CAA, and digesting via the automated protein aggregation capture (PAC) protocol on an Opentrons OT-2 using Lys-C and Trypsin. Acquire data on the timsTOF HT mass spectrometer coupled to an Evosep One system using a diaPASEF method, and process the data in Spectronaut version 19.1 against the UniProt human database.
8. Perform inflammasome activation assays by plating iMCs in 96-well and 24-well plates, switching to OptiMEM, and applying specific stimulation protocols for:
   - NLRP3: Prime with 100 ng/mL ultrapure LPS or 1 μg/mL Pam3CSK4 for 4 h; activate with 5 μM nigericin or 5 mM ATP for 2 h.
   - Non-canonical inflammasome (NCI): Prime with 1 μg/mL Pam3CSK4 for 16 h; transfect with LPS (10 μg/mL final with 0.25% Lipofectamine LTX) via centrifugation at 1000 × g for 10 min and incubate for 5 h.
   - NAIP/NLRC4: Prime for 4 h; treat with 1 ng/mL Lfn-BsaL plus 250 ng/mL Anthrax Protective Antigen for 2 h.
   - NLRP1: Prime for 4 h; treat with 10 μM Talabostat mesylate or 10 μM Anisomycin for 24 h.
9. Assess inflammasome activation readouts on the stimulated cultures and collected supernatants:
   - Measure cell death (pyroptosis) using the LDH assay kit by combining supernatants with LDH assay buffer and reading absorbance at 490 nm relative to a 100% Triton X-100 lysis control.
   - Measure cytokine release (IL-1β and TNF-α) using manufacturer ELISA kits.
   - Analyze protein expression and processing via Western blot on cell lysates using 4–20% Mini-PROTEAN TGX gels, semi-dry transfer onto nitrocellulose membranes, blocking with 5% milk in TBS-Tween, and probing with primary and secondary antibodies.
   - Quantify ASC speck formation by fixing cells with 4% PFA, staining with anti-mouse ASC primary and Alexa Fluor 488 secondary antibodies alongside DAPI, and imaging via fluorescence microscopy to calculate the percentage of DAPI+ASC+ cells.
```

label: 

defect_types: 

notes: 

---

## 30. RCC48FC  (growth_curve)

```
Please prepare primary swine macrophage cultures from heparinized blood of 6 Yorkshire females (250–300 lb, 5–6 mo old) obtained under BSL‑3 conditions. Incubate the blood at 37 °C for 1–2 h, then isolate mononuclear cells by Ficoll-Paque (specific gravity 1.079). Seed the monocyte/macrophage fraction into Primaria tissue culture flasks with RPMI 1640 + 30 % L929 supernatant + 20 % heat‑inactivated, γ‑irradiated FBS + antibiotics/antimycotics + gentamicin + 30 % complementary plasma. Incubate 24 h at 37 °C, 5 % CO₂. Detach adherent cells with 10 mM EDTA in DPBS, wash twice with macrophage wash medium (RPMI + antibiotics/antimycotics + gentamicin), then resuspend in FBS and re‑seed into Primaria plates 24 h later or cryopreserve.

For cryopreservation, wash macrophages twice in macrophage wash medium (240 × g, 10 min, RT), resuspend in pre‑chilled 7 % DMSO/93 % FBS. Aliquot at 1 × 10⁷ cells/mL into cryovials, place in Mr. Frosty for 48 h at –70 °C, then transfer to liquid nitrogen. For thawing, quickly warm vials in a 37 °C water bath, transfer cells to a 15 mL tube, wash twice with macrophage complete medium (RPMI + 30 % L929 + 20 % FBS + antibiotics/antimycotics + gentamicin), count with trypan blue, adjust concentration, and seed 5 × 10⁶ cells per 96‑well Primaria plate (or 1 × 10⁶ cells per 6‑well plate for growth curves) 24 h before use.

Prepare red blood cells for hemadsorption from the same heparinized blood: after 1–2 h sedimentation, recover 35 mL of the erythrocyte fraction, wash twice (240 × g, 10 min, RT) in DPBS, resuspend to 20 % final concentration in DPBS, store at 4 °C, and use within 7–14 days. Also provide heterologous swine RBCs from another pig and commercial porcine RBCs as alternatives.

Virus isolates to be used: ASFV Georgia 2007/1, Lisbon‑60, Killean‑III, Kimakia‑64, DR‑2, DR‑21, Haiti‑21, Malawi Lil‑20/1, Pretoria‑4/1. Each isolate should be recovered from the original material, pass once in primary swine macrophages (≤ 2 passages total) to generate stocks, and freeze at –70 °C.

Virus titration protocol: Dilute each ASFV isolate and each EDTA‑treated blood sample 10‑fold in macrophage complete medium. In 96‑well Primaria plates, seed 5 × 10⁶ cells/plate. Add 50 µL of each dilution to the wells. Incubate 1 h at 37 °C, then remove inoculum, wash twice with complete medium. Add 10 µL of the prepared RBC mixture (20 % RBC in DPBS) 24 h after inoculation. Read hemadsorption between 7–10 days p.i. Calculate HAD₅₀/mL using Reed‑Muench.

Growth‑curve experiment: Seed fresh and 1‑month cryopreserved macrophages into 6‑well Primaria plates at 1 × 10⁶ cells/well (in 2 mL medium). In triplicate, inoculate with ASFV Georgia 2007/1 or Lisbon‑60 at MOI 0.01. After 1 h at 37 °C, remove inoculum, wash twice with complete medium, then add 2 mL medium per well. Collect 2 mL supernatant at 0 h, 1, 2, 5, 7, and 9 days p.i., freeze at –70 °C. Determine titers in fresh macrophage cultures as HAD₅₀/mL.

Repeatability study: Use fresh, 2‑month, and 6‑month cryopreserved macrophage stocks. Seed 5 × 10⁶ cells/plate in 96‑well Primaria plates. Prepare 10‑fold serial dilutions of ASFV Georgia 2007/1, inoculate each dilution in triplicate. Perform the entire experiment on three consecutive days to assess repeatability/reproducibility of cryopreserved vs. fresh cells.

Materials needed: Primaria tissue culture flasks and plates, RPMI 1640, L929 cell supernatant, heat‑inactivated, γ‑irradiated FBS, antibiotics/antimycotics, gentamicin, EDTA, DPBS, 7 % DMSO, cryovials, Mr. Frosty container, liquid nitrogen, 96‑well Primaria plates, 6‑well Primaria plates, Neubauer counting chamber.  

Please perform all steps under the specified biosafety conditions and report back with the titers, growth‑curve data, and repeatability results.
```

label: 

defect_types: 

notes: 

---

## 31. RF9D69D  (qpcr)

```
Please perform the following experiments using our submitted samples, following this workflow:

1. dCas9-KRAB-mediated enhancer silencing in differentiated 3T3-L1 adipocytes:
- Seed differentiated 3T3-L1 adipocytes from 10 cm dishes into 12-well plates at 4 × 10^4 cells/well in antibiotic-free differentiation medium after washing with 1× DPBS and trypsinizing. Allow 24 h recovery at 37°C, 5% CO2.
- Perform sequential transfections per well:
  - dCas9-KRAB plasmid transfection: Mix 300 ng dCas9-KRAB plasmid, 12 μL Opti-MEM, and 0.4 μL 3T3-L1 Cell Avalanche Transfection Reagent. Incubate 15 min at 22 ± 1°C, add dropwise, and centrifuge the plate at 300 × g for 5 min. Incubate at 37°C, 5% CO2 for 4.5 h, then replace with fresh antibiotic-free differentiation medium.
  - sgRNA transfection: 4.5 h after plasmid transfection, add sgRNA transfection mix containing 15 pmol sgRNA, 50 μL Opti-MEM, and 0.4 μL 3T3-L1 Cell Avalanche Transfection Reagent (prepared fresh on ice, mixed well, and incubated 15 min at 22 ± 1°C). Centrifuge at 300 × g for 5 min. After 4.5 h, replace with fresh 3T3-L1 differentiation medium.
- Include a non-targeting scramble sgRNA control and three different target-specific sgRNAs. Always include a negative transfection control with no sgRNA added.
- Incubate for 36 h at 37°C, 5% CO2.
- Harvest cells on day 3 by washing once with cold 1× DPBS, lysing in Qiazol, and proceeding with RNA extraction or storing lysates at −80°C.

2. RNA extraction and qRT-PCR quantification of Lep expression:
- Extract total RNA using the miRNeasy or RNeasy Mini Kit with Qiazol, including an on-column DNase digestion. Elute in RNase-free water and quantify via NanoDrop.
- Set up cDNA synthesis using the High-Capacity RT Kit. Prepare the master mix on ice (2 μL 10× RT Buffer, 0.8 μL 25× dNTP Mix, 2 μL 10× RT Random Primers, 1 μL MultiScribe Reverse Transcriptase, 1 μL RNase Inhibitor, 3.2 μL nuclease-free H2O per reaction). Add 10 μL of RNA (50–100 ng/μL) per reaction.
- Run thermal cycling: 25°C for 10 min, 37°C for 120 min, 85°C for 5 min, hold at 4°C. Include no-template and no-RT controls per RNA batch.
- Dilute cDNA to 5 ng/μL in nuclease-free water.
- Set up qPCR on ice in technical duplicates using PrimeTime Master Mix (5 μL per 10 μL reaction), 0.5 μL PrimeTime qPCR assay for Lep, 0.5 μL assay for Hprt (or DEPC-water for singleplex), and 4 μL diluted cDNA. Seal, vortex, and centrifuge at 500 × g.
- Run on the QuantStudio 5 system. Apply a consistent Ct threshold across all compared samples, exclude technical replicates with standard deviation > 0.5, and export Ct values.

3. DNA isolation from adipose tissue:
- Weigh 60–100 mg of frozen adipose tissue on dry ice and transfer to a 2 mL screw-cap tube containing 3–4 cell lysis beads.
- Add Tissue Lysis Buffer (200 μL Buffer AVE, 40 μL Buffer VXL, 1 μL DX Reagent, 20 μL Proteinase K, and 4 μL RNase A per sample, prepared fresh).
- Homogenize using a bead mill (2 cycles, 15 s per cycle at high speed, 5 s pause between cycles).
- Proceed with the QIAamp Fast DNA Tissue Kit or QIAamp DNA Mini Kit following manufacturer instructions, and elute in 50 μL DEPC-treated H2O.

4. DNA quantification:
- Quantify dsDNA using the Qubit dsDNA BR Assay Kit with the Qubit 4 fluorometer, following standard calibration with S1 and S2 standards, measuring 1 μL of sample in 199 μL working solution.

5. Bisulfite conversion of genomic DNA:
- Using up to 1000 ng of genomic DNA, set up the bisulfite conversion reaction using the EpiTect Fast DNA Bisulfite Kit with appropriate volumes of DNA Protect Buffer and Bisulfite solution.
- Run thermal cycling: 95°C for 5 min, 60°C for 30 min, 95°C for 5 min, 60°C for 20 min, hold at 20°C.
- Perform all recommended clean-up, desulfonation, drying, and washing steps. For input DNA < 100 ng, add Carrier-RNA to Buffer BL. Elute in 15–50 μL Buffer EB.

6. Bisulfite PCR:
- Prepare BisPCR master mix on ice: 12.5 μL PyroMark PCR MasterMix (2×), 2.5 μL CoralLoad Concentrate (10×), 0.5 μL forward primer (10 μM), 0.5 μL reverse primer (10 μM), and 8 μL RNase-free water per reaction. Add 1 μL bisulfite-converted DNA (10–20 ng) and one H2O no-template control.
- Run thermal cycling: Initial denaturation at 95°C for 10 min; 40 cycles (mouse) or 45 cycles (human) of 94°C for 30 s, assay-specific annealing temperature (e.g., 49.5°C for mouse) for 25 s, 72°C for 25 s; final extension at 72°C for 10 min.
- Verify PCR products on a 1% agarose TAE gel with SYBR Safe (loading 4 μL product alongside a 100 bp ladder, running at 150 V for 20–25 min) and image using a ChemiDoc system. Proceed only if a single specific band is present and the no-template control is negative.

7. Pyrosequencing:
- Run pyrosequencing on the PyroMark Q48 Autoprep using the PyroMark Q48 Advanced CpG Kit and assay-specific sequencing primers.
- Load each well with 3 μL streptavidin-coated magnetic beads and 10 μL BisPCR product (15 μL for sorted adipocyte samples).
- Inspect wells, flag failures, export percentage methylation per CpG, and normalize to the standard curve.

8. In vitro methylation of pCpGL-CMV vector:
- Prepare a 1.6 mM SAM working solution (fresh 1:20 dilution in nuclease-free water).
- Set up methylation and mock reactions (omitting M.SssI and replacing with nuclease-free water) using 750–1000 ng plasmid DNA, 2 μL 10× NEB Buffer 2, 1 μL SAM, M.SssI enzyme, and nuclease-free water to 20 μL. Incubate at 37°C for 4 h, then heat-inactivate at 65°C for 20 min.
- Purify via drop dialysis on a 0.1 μm nitrocellulose membrane on Milli-Q water for ≥5 min, recover, quantify, and dilute to 50 ng/μL.

9. Transfection of HEK293T cells and luciferase measurement:
- Seed HEK293T cells in 96-well plates at 1 × 10^4 cells per well in 100 μL antibiotic-free growth medium and incubate 16 h at 37°C, 5% CO2.
- Prepare Lipofectamine 2000 mix (0.2 μL Lipofectamine 2000 + 4.8 μL Opti-MEM per well) and incubate 5 min at 22 ± 1°C.
- Prepare DNA mix per condition (2 μL methylated or mock plasmid at 50 ng/μL + 1 μL Renilla-SV40 at 1 ng/μL + 2 μL Opti-MEM per well).
- Combine equal volumes of Lipofectamine mix and DNA mix, incubate 10–20 min at 22 ± 1°C, and add 10 μL of transfection mix to each well. Incubate for 24 h at 37°C, 5% CO2.
- Perform luciferase assays using the Dual-Glo system: add 100 μL Luciferase Assay reagent per well, incubate 10 min in the dark, and measure firefly luminescence. Then add 100 μL (or 90 μL if lysate was transferred to a white plate) of Stop & Glo Reagent, incubate 10 min, and measure Renilla luminescence.
- Subtract background, calculate normalized firefly signal (FF/Ren), and normalize to the mock control group within each biological replicate.
```

label: 

defect_types: 

notes: 

---

## 32. R9B7DDD  (growth_curve)

```
Please run the following liquid growth assay for our Aspergillus spore samples:

1. **Prepare spore suspension**  
   a. Harvest spores from a fresh plate and resuspend in PBS containing 0.01 % Tween‑20.  
   b. Dilute to 4 × 10⁵ spores mL⁻¹ (approximately 2000 spores per 5 µL aliquot).  

2. **Plate setup**  
   a. Using a non‑coated Starlab CytoOne 96‑well plate, dispense 5 µL of the spore suspension into each well.  
   b. Add 195 µL of liquid growth medium (total volume 200 µL per well).  
   c. Fill the peripheral wells or the spaces between wells with sterile medium or sterile water to minimise edge effects.  
   d. Cover the plate with a breathable lid to allow gas exchange.

3. **Instrument setup**  
   a. Preheat either the Powerwave X‑2 (KC software) or a BioTek plate reader to 37 °C.  
   b. Measure a blank reading before starting the run.  
   c. Program the reader to record OD₆₀₀ every 10 minutes for a total of 48 h (time‑course will generate the growth curve).  

4. **Run the assay**  
   a. Place the plate in the reader and start the 48 h run.  
   b. After completion, export the raw OD₆₀₀ data as a TXT file (or the format specified in the attached example).  

5. **Data handling**  
   a. Perform any required data manipulation to match the format of the reference growth curves (see attached example).  
   b. Forward the processed data to us for further analysis (the next protocol covers downstream processing).  

Please confirm receipt of this request and let us know if any materials or additional details are needed. Thank you.
```

label: 

defect_types: 

notes: 

---

## 33. RBEF695  (viability)

```
Please run an MTT cell viability assay on our cell-seeded broccoli stalk scaffolds using the following procedure:

1. Use our provided 3.5 mm decellularized broccoli scaffolds in 96-well plates with at least three replicates per experimental condition. Seed mouse embryonic fibroblasts at 15,000 cells per scaffold (or adjust if using an optimized density for a different cell type). 
2. Culture the cells for 1 to 7 days.
3. Use forceps to carefully transfer the scaffolds to new wells to avoid measuring cells that attached to the original well surfaces during seeding, then add 100 µL of culture medium to each well containing a scaffold.
4. Add 100 µL of culture medium to three empty wells to serve as blanks.
5. Add 10 µL of MTT reagent (MilliporeSigma Catalog #11465007001) to every well, including the blanks.
6. Incubate the plate in the cell culture incubator for 4 hours (or up to 24 hours if needed for your cell type).
7. Add 100 µL of solubilization buffer to each well, including the blanks.
8. Incubate the plate overnight in the cell culture incubator.
9. Either use forceps to remove and discard the scaffolds or transfer a 200 µL volume from each well to a new plate so the plant tissue does not interfere with absorbance readings.
10. Measure the absorbance of each well at 570 nm using a plate reader, using a reference wavelength >650 nm if required.
```

label: 

defect_types: 

notes: 

---

## 34. RBA5959  (viability)

```
1. Process the provided Ti-6Al-4V alloy bars into discs measuring 8 mm in diameter and approximately 2.5 mm in height, and polish the surfaces with sandpaper to remove burs and debris.

2. Perform surface texturing on the titanium discs using an Nd:YVO4 laser (OEM Plus, SISMA; λ = 1064 nm, 10 ns pulse width, initial focus at 11.1 cm under normal atmospheric pressure with constant air renewal via fan and compressed air jet). Create a checkerboard pattern of grooves and ridges based on two designs: “08” (0.8 mm crest and groove length) and “025” (0.25 mm crest and groove length). Disinfect all textured samples in an isopropyl alcohol solution for 1 minute in an ultrasound bath.

3. Apply a hydroxyapatite coating to designated samples using dip coating in a 0.133 g/mL suspension of nanoXIM Hap400 powder in water. 

4. Sinter the coated samples using one of two methods:
   - Laser sintering using a CO2 laser (BD-50C, Bende Machinery; max power 50 W, λ = 1064 nm).
   - Conventional sintering in a furnace at 950 to 1175 °C for 1 h.

5. Allocate the samples into the following seven study groups:
   - TiL: Polished titanium
   - TiT025: Texturized titanium (0.25 pattern)
   - TiT025CS: Texturized titanium (0.25 pattern) + bioactive with conventional sintering
   - TiT025LS: Texturized titanium (0.25 pattern) + bioactive with laser sintering
   - TiT08: Texturized titanium (0.8 pattern)
   - TiT08CS: Texturized titanium (0.8 pattern) + bioactive with conventional sintering
   - TiT08LS: Texturized titanium (0.8 pattern) + bioactive with laser sintering

6. Perform surface roughness analysis (Ra parameter) on the uncoated metallic substrates (TiL, TiT025, and TiT08) using a contact profilometer (SurfTest SJ-201, Mitutoyo) with a 2 μm diamond stylus. Take ten random measurements per sample perpendicular to the texture direction at 0.5 mm/s scanning speed and 0.8 mm sampling length. Omit contact profilometry for coated groups to prevent damage; monitor coated surface integrity via SEM instead.

7. Measure surface wettability for all groups (TiL, TiT025, TiT08, TiT025CS, TiT025LS, TiT08CS, TiT08LS) using the sessile drop method with an optical goniometer (OCA 15 Plus, Dataphysics) and two probe liquids (deionized water and diiodomethane). Dispense 5 μL droplets at 2.5 μL/s, allow 15 s for stabilization, and take 5 measurements per sample. Clean all samples ultrasonically in isopropyl alcohol for 1 min prior to testing.

8. Culture immortalized human gingival fibroblasts (HGF hTERT-T0026, Applied Biological Materials) in DMEM supplemented with 10% fetal bovine serum, 100 U/mL penicillin, and 100 μg/mL streptomycin at 37 °C, 5% CO2, and 100% humidity. Use cells at the fifth passage.

9. Seed cells onto the sample discs in 48-well plates at a density of 1.0 × 10^4 cells/well for all biological assays.

10. Conduct cell viability and proliferation assays across eight groups (the seven sample groups plus a positive control) using the CellTiter-Blue resazurin-based assay across three independent experiments with duplicates of 5 samples per group (N = 15). Measure fluorescence intensity at 560/590 nm using a Victor Nivo plate reader after 1, 3, and 7 days of culture.

11. Perform cell morphology analysis on cells cultured on discs for 1 day. Wash with PBS, fix with 2.5% glutaraldehyde for 1 h, dehydrate using serial ethanol dilutions, and sputter-coat with gold using a JEOL JFC 1200. Image samples using a JEOL JSM5200-LV SEM at 15 kV and 25 kV acceleration voltages at 100×, 150×, 180×, and 200× magnifications to assess cell morphology, spreading, and adhesion.

12. Quantify IL-1β and IL-10 levels in the culture supernatant after 1 and 3 days of culture using DuoSet ELISA kits according to the manufacturer's instructions, reading absorbance at 540 nm and 450 nm on a Victor Nivo plate reader. Perform one experiment with duplicates of 3 samples per group (n = 6) and convert absorbance values to pg/mL using linear regression.

13. Perform statistical analysis using IBM SPSS 29.0. Test data for normality using the Shapiro-Wilk test. Analyze cell viability and interleukin quantification data using two-way ANOVA followed by Tukey’s post hoc test, setting significance at p < 0.05, and report all data as mean ± standard deviation.
```

label: 

defect_types: 

notes: 

---

## 35. RFD2BCB  (viability)

```
Please conduct an MTT viability assay on our cell samples as follows:

1. Dissolve each test compound in DMSO to a stock concentration suitable for serial dilution (e.g., 10 mM).  
2. Prepare a 40‑fold serial dilution series in a U‑type tube or plate (e.g., 10 µL of stock + 390 µL DMSO for the first dilution, then mix 10 µL into 390 µL of the previous dilution).  
3. Plate the cells in a 96‑well plate (density per your usual protocol). Observe and record the initial cell morphology.  
4. Remove the old medium from the cells.  
5. Add 100 µL of each diluted sample to the appropriate wells; keep the cells in 37 °C, 5 % CO₂ for 48 h.  
6. After 48 h, re‑inspect the cells under the microscope. Photograph any wells that show morphological changes.  
7. Prepare a fresh MTT working solution at 10 % (w/v) in PBS or culture medium.  
8. Remove the medium from the 96‑well plate.  
9. Add 150 µL of the MTT solution to each well using a multichannel pipette. Incubate for 4 h at 37 °C.  
10. Carefully remove the MTT solution.  
11. Add 100 µL of 100 % DMSO to each well to dissolve the formazan crystals.  
12. Shake the plate gently for 30 s to ensure complete dissolution.  
13. Measure absorbance at 560 nm (signal) and 750 nm (background) with a plate reader; perform a 0.5‑min pre‑scan shake before reading.  

Please report the absorbance data, calculate percent viability relative to untreated controls, and include representative cell images in the final report.
```

label: 

defect_types: 

notes: 

---

## 36. R01A2EC  (qpcr)

```
1. Grow the following cell lines in the specified media:  
   - 22Rv1 (CRISPR‑edited AR‑V7‑HiBiT knock‑in, from Promega) and C4‑2B in RPMI + 10 % FBS + 1× pen‑strep.  
   - RWPE‑1 in Keratinocyte Serum‑Free Medium with BPE and EGF (Invitrogen kit #17005‑042).  
   Use cells between passages 3‑5 and keep passage number constant for each replicate.

2. Seed cells in 384‑well black clear‑bottom plates (Greiner Bio‑One #781986) at 10 000 cells /mL (≈500 cells per 50 µL well). Allow them to attach and grow to 60‑75 % confluence (≈24 h).

3. Prepare the NPNPD natural‑product library dilutions in DMSO as follows: start from the supplied 10 µg/4 µL stock (2.5 µg µL⁻¹), perform a 5‑fold serial dilution, then a 4‑fold dilution to generate working solutions that give final assay concentrations of 50, 25, 10, 5, 2.5 and 1.25 µg mL⁻¹. Use the 1.25 µg mL⁻¹ concentration for the primary screen. Transfer 0.5 µL of each working solution into the assay wells (final volume 50 µL, 1 % DMSO final). Include vehicle (1 % DMSO) and positive control (withaferin A) wells on each plate.

4. Incubate the treated plates at 37 °C, 5 % CO₂ for 24 h.

5. For cell‑viability readout, add resazurin to a final concentration of 0.2 mg mL⁻¹, incubate another 16 h at 37 °C, then read fluorescence (Ex 560 nm/Em 590 nm). Normalize to vehicle controls and calculate % viability.

6. In parallel, for AR‑V7 quantification, plate the AR‑HiBiT 22Rv1 cells at the same density in opaque white 384‑well plates (Greiner Bio‑One #781095). After 24 h compound exposure, add Nano‑Glo HiBiT Lytic Detection Reagent (Promega #N3040) according to the manufacturer’s protocol and read luminescence on a plate reader. Use parental 22Rv1 cells (no HiBiT) as negative controls to subtract background.

7. Identify primary hits as fractions that give ≥90 % inhibition of viability in 22Rv1/C4‑2B, ≤10 % inhibition in RWPE‑1, and a Z‑score >3 relative to plate mean.

8. For each hit, perform dose‑response confirmation in 384‑well format (serial 5‑fold dilutions) to obtain IC₅₀ values using nonlinear regression (CompuSyn or equivalent).

9. For selected hits, repeat the assay in 96‑well white plates (Pierce #15042) at 3 000 cells well⁻¹ to allow larger signal windows and replicate measurements. Run both the resazurin viability assay and the HiBiT luminescence assay as above.

10. Collect protein lysates from 22Rv1 and C4‑2B cells treated at their respective IC₅₀ concentrations for 24 h. Perform Western blotting with the following primary antibodies (Cell Signaling Technology): AR (#5153), PSA (#5365S), Bcl‑2 (#15071S), PARP (#9542), and β‑actin (#5125). Use HRP‑conjugated secondary antibodies (#7074S, #7076S). Visualize on a Bio‑Rad ChemiDoc and quantify bands with ImageJ.

11. Extract total RNA from 22Rv1 and C4‑2B cells treated with vehicle or the hit compounds (e.g., isolinderanolide B) for 6 h using Qiagen RNeasy Mini Kit. DNase‑treat (Thermo EN0521), quantify (NanoDrop), and reverse‑transcribe 1 µg RNA with Bio‑Rad iScript Supermix. Perform qPCR (Bio‑Rad SsoAdvanced SYBR Green) for AR, AR‑V7, PSA and β‑actin (primer sequences as published). Run three biological replicates, each in technical triplicate, with cycling: 95 °C 30 s; 40 cycles of 95 °C 10 s/60 °C 20 s; melt curve 65‑95 °C 0.5 °C steps. Normalize to β‑actin and present as fold change.

12. Deliver the raw and normalized data for viability, luminescence, IC₅₀ curves, Western blots (images and densitometry), and qPCR (Ct values and ΔΔCt calculations). Include statistical analysis (t‑test or ANOVA as appropriate) and indicate significance levels (ns, *, **, ***, ****).
```

label: 

defect_types: 

notes: 

---

## 37. RCEBBFF  (qpcr)

```
**Lab Request – Tomato Wounding and Gene‑Expression Analysis**

1. **Safety & PPE**  
   - All work with Trizol and chloroform must be performed in a fume hood.  
   - Wear nitrile gloves and safety goggles at all times.  
   - Keep reagents refrigerated and use sterile technique to avoid contamination.  

2. **Materials & Equipment (order if not stocked)**  
   - Trizol reagent (1 L bottle), Buffer RW1, Buffer RW2 (column kit)  
   - 75 % ethanol, 5 % sodium hypochlorite solution, sterile distilled water  
   - ISTA‑compliant germination paper (9 cm diameter dishes)  
   - Small square plastic pots (7 cm side) or equivalent volume round pots  
   - Vermiculite and peat (1:1 volume ratio) for substrate  
   - 14 cm straight hemostatic forceps, 16 cm straight tweezers  
   - 1.5 mL RNase‑free centrifuge tubes, 2 mL tubes, 1.5 mL RNase‑free collection tubes  
   - 30 µL RNase‑free water, 10 µL ddH₂O, 1 µg total RNA (from each sample)  
   - 2 µL 5 × gDNA Eraser buffer, 2 µL gDNA Eraser, 1 µL PrimeScript RT Enzyme Mix I, 1 µL RT Primer Mix, 4 µL PrimeScript buffer  
   - Kapa SYBR Fast qPCR kit, 0.25 µM forward and reverse primers for target genes and ACTIN2  
   - LightCycler 480 (or compatible SYBR‑green platform)  
   - Cold mortar & pestle, liquid nitrogen, −80 °C freezer, −20 °C fridge, 4 °C centrifuge, spectrophotometer (NanoDrop), agarose gel apparatus  

3. **Seed Germination (Day 0–3)**  
   a. Surface‑sterilize tomato seeds: 2 min in 75 % EtOH, 10 min in 5 % NaOCl (gentle shaking), 6–7 washes in sterile water.  
   b. Spread seeds evenly on germination paper in 9 cm dishes, moisten with water (not submerged).  
   c. Keep dishes in dark at 26 °C until radicles appear (2–3 days).  

4. **Seedling Growth (Day 3–16)**  
   a. Mix vermiculite:peat 1:1, fill plastic pots (or round pots).  
   b. Transplant seedlings with radicle out (use 16 cm tweezers).  
   c. Grow in growth chamber: 16 h light (26 °C, 180–220 µmol m⁻² s⁻¹), 8 h dark (18 °C, 60 % RH).  
   d. Water as needed; avoid over‑watering.  

5. **Mechanical Wounding (Day 16)**  
   a. Select healthy seedlings at two‑leaf, one‑heart stage.  
   b. Sterilize 14 cm hemostatic forceps with 75 % EtOH, air dry.  
   c. Clamp the lamina of the first true leaf once with consistent pressure to induce visible drooping.  
   d. Label each wounded seedling; set up an identical untreated control group (different pots).  

6. **Sampling (12 h Post‑Wounding)**  
   a. Harvest:  
      - Wounded leaflet (only the wounded part).  
      - Undamaged second true leaf (systemic).  
      - Leaves from control seedlings.  
   b. Snap‑freeze each sample in liquid N₂, label with tissue type, time, serial number.  
   c. Store immediately in −80 °C freezer.  

7. **RNA Extraction (≤3 months after sampling)**  
   a. Retrieve frozen tissue, grind in cold mortar with liquid N₂ to fine powder (≤500 µL).  
   b. Add 1 mL Trizol, mix, 5 min RT.  
   c. Transfer to column, centrifuge 20 s at 13 500 × g, 4 °C; discard flow‑through.  
   d. Wash with 700 µL Buffer RW1 (20 s), then 500 µL Buffer RW2 (20 s, repeat once).  
   e. Final 2 min spin at 13 500 × g, 4 °C; dry column.  
   f. Elute RNA with 30 µL RNase‑free water, 1 min, spin 1 min.  
   g. Quantify with NanoDrop (260 nm, 260/280, 260/230).  
   h. Run 1% agarose gel to confirm integrity.  

8. **Reverse Transcription**  
   a. In ice‑cold tube: 2 µL 5 × gDNA Eraser buffer, 2 µL gDNA Eraser, 1 µg RNA, ddH₂O to 10 µL.  
   b. Incubate 42 °C, 2 min; cool on ice.  
   c. Add 10 µL RT master mix: 2 µL 5 × PrimeScript buffer, 4 µL PrimeScript RT Enzyme Mix I, 1 µL RT Primer Mix, 1 µL ddH₂O.  
   d. Incubate 37 °C, 15 min; terminate 85 °C, 5 s.  
   e. Store cDNA on ice or −80 °C.  

9. **qPCR Setup (20 µL per reaction)**  
   - 2 µL cDNA (equivalent to 50 ng RNA)  
   - 10 µL SYBR Fast qPCR kit (2 ×)  
   - 0.5 µL forward primer (0.25 µM)  
   - 0.5 µL reverse primer (0.25 µM)  
   - 6.5 µL ddH₂O to 20 µL.  

10. **Cycling Conditions (LightCycler 480)**  
    - 95 °C 30 s (initial)  
    - 40 cycles: 95 °C 5 s, 59 °C 30 s (optimize for each primer)  
    - Melt curve: 60–95 °C, 0.3 °C s⁻¹, continuous fluorescence.  

11. **Data Analysis**  
    - Normalize target gene Ct to ACTIN2 Ct (ΔCt).  
    - Calculate ΔΔCt (treatment vs. control).  
    - Present fold change (2^‑ΔΔCt).  
    - Use Student’s t‑test for two‑group comparisons; ANOVA + Tukey for multiple groups.  
    - Significance: * P < 0.05; ** P < 0.01; *** P < 0.001; ns = not significant.  

12. **Deliverables**  
    - Raw Ct files, melt curves, amplification plots.  
    - Fold‑change table with statistical annotations.  
    - RNA QC metrics (NanoDrop ratios, gel images).  
    - Summary of any deviations or issues encountered.  

Please proceed with the above protocol and notify us of any material shortages or timing concerns.
```

label: 

defect_types: 

notes: 

---

## 38. RA3EF2F  (growth_curve)

```
1. Grow the bacterial strains we will provide (B. subtilis 168 trpC2, L. plantarum ATCC 8014, E. faecalis ATCC 29212, S. aureus ATCC 29213, C. difficile ATCC 9689, plus the two clinical C. difficile isolates) under the same conditions as in the paper:  
   - B. subtilis and S. aureus: LB broth, aerobic, 37 °C.  
   - L. plantarum: MRS broth, aerobic, 37 °C.  
   - E. faecalis: NYCIII broth, anaerobic, 37 °C.  
   - C. difficile (all strains): BHI broth, anaerobic, 37 °C.  

2. Perform antibiotic growth assays as follows:  
   - For B. subtilis and L. plantarum, dilute overnight cultures to OD₆₀₀ = 0.005–0.05 in fresh medium, dispense 200 µL into each well of a clear 96‑well plate, and add chloramphenicol (0, 1.6, 8, or 40 µg mL⁻¹) or erythromycin (0, 0.1, 0.5, or 2.5 µg mL⁻¹). Incubate aerobically at 37 °C for 18–24 h and record OD₆₀₀ every 15 min on a Tecan Spark.  
   - For C. difficile clinical isolates, dilute overnight cultures to OD₆₀₀ = 0.05, add erythromycin (0, 1, or 256 µg mL⁻¹) in BHI, incubate anaerobically at 37 °C for 18–24 h and read on a Tecan Sunrise.  

3. Prepare RNA for HT‑5PSeq / s5PSeq:  
   a. Grow the strains to mid‑exponential phase (OD₆₀₀ = 0.6–0.8).  
   b. Take 1 mL aliquots and treat with the same antibiotic concentrations used in the growth assays for 10 min (add 500 µL RNAprotect Bacteria Reagent after the 10‑min drug exposure for the C. difficile isolates, incubate 5 min, then pellet).  
   c. Pellet cells at 13 000 rpm for 3 min, discard supernatant, and freeze pellets on dry ice.  

4. Extract total RNA (phenol‑chloroform + bead beating):  
   - Resuspend frozen pellets in phenol‑based lysis buffer with glass beads, disrupt with a MultiMixer (2 min) or FastPrep (1 min).  
   - Perform acidic phenol‑chloroform extraction, precipitate RNA with ethanol, and elute in nuclease‑free water.  
   - Quantify RNA with Nanodrop and Qubit dsDNA HS assay; assess integrity on an Agilent Bioanalyzer RNA Pico chip.  

5. Build s5PSeq libraries (use 200 ng total RNA per sample, no DNase):  
   - Block rRNA by adding 0.4 µM of the 146 universal blocking oligos + 4 µM of the two species‑specific 16S/23S oligos (Table S1) in 50 mM NaCl. Heat 75 °C 5 min → 65 °C 5 min → drop 3 °C every 2 min until 35 °C.  
   - Ligate a 5′‑RNA adapter containing a UMI and barcode (1 µM final) with T4 RNA ligase 1 (NEB M0204L) in 1 mM ATP, 1× ligation buffer, 25 °C for 1 h. Clean up with RNAClean XP beads (1.8×).  
   - Reverse‑transcribe using SuperScript II (Thermo 100004925) and random hexamers.  
   - Degrade RNA template with 28.6 mM NaOH at 65 °C for 20 min, neutralize with equal Tris‑HCl. Clean cDNA with AMPure XP beads (1.8×).  
   - PCR amplify with Illumina dual‑barcode primers (0.25 µM each) and Phusion High‑Fidelity Master Mix (F‑530L): 98 °C 30 s; 15 × (98 °C 20 s, 65 °C 30 s, 72 °C 30 s); 72 °C 7 min.  
   - Perform a two‑step size selection with AMPure XP beads (first 0.6×, then 0.8×) to retain 400–600 bp fragments.  

6. For mixed‑species libraries, combine equal masses of total RNA from B. subtilis, S. aureus, E. faecalis, and erythromycin‑treated C. difficile (100 ng each) and process as in step 5.  

7. Illumina sequencing:  
   - Quantify the final libraries with Qubit dsDNA HS assay, dilute to 650 pM, and load onto an Illumina NextSeq 2000 (paired‑end, appropriate read length).  
   - Demultiplex with bcl2fastq 2.20.0, trim adapters with cutadapt 4.8, extract UMIs with UMI‑tools 1.0.0, and align reads to the appropriate bacterial reference genomes using STAR 2.7.11a.  

8. Nanopore sequencing (optional but requested):  
   - Take the same Illumina libraries and ligate ONT adapters using the Ligation Sequencing Kit v14 (SQK‑LSK114).  
   - Load the prepared library onto a Flongle flow cell (FLO‑FLG114) for a 24‑h MinION run and onto a PromethION flow cell (FLO‑PRO114M) for a 72‑h run.  
   - Base‑call Flongle data with Dorado (Fast model) and PromethION data with Guppy (Super‑accurate model).  
   - Demultiplex using minibar.py (dual‑barcode Illumina adapters), extract UMIs with UMI‑tools, align to the C. difficile reference with minimap2 2.28‑r1209, and analyse with fivepseq 1.3.5.  

9. Provide us with the following data files for each sample:  
   - Raw fastq (Illumina) and pod5 (Nanopore) files.  
   - Alignment (BAM) files, mapped read counts, and fivepseq output (coverage matrices, stalling metrics).  
   - Summary statistics (total reads, % mapped, rRNA fraction).  

10. Reagents you will need (catalog numbers included for ordering):  
    - Chloramphenicol (Sigma C0378) and erythromycin (Sigma E5389).  
    - T4 RNA ligase 1 (NEB M0204L).  
    - SuperScript II RT (Thermo 100004925).  
    - Phusion High‑Fidelity PCR Master Mix (Thermo F‑530L).  
    - AMPure XP (Beckman A63881) and RNAClean XP (Beckman A63987).  
    - Qubit dsDNA HS assay kit (Thermo Q33231) and RNA BR assay kit (Thermo Q10211).  
    - Agilent High‑sensitivity DNA kit (Agilent 5067‑4626).  
    - ONT Ligation Sequencing Kit v14 (SQK‑LSK114), Flongle flow cells (FLO‑FLG114) and PromethION flow cells (FLO‑PRO114M).  

Please follow the steps exactly and let us know if any reagents are unavailable or if you encounter issues at any stage. Thank you.
```

label: 

defect_types: 

notes: 

---

## 39. R63A20F  (elisa)

```
Please perform the following hydrogel formulation, in vitro cell assays, and in vivo diabetic rat implant study using our provided samples and reagents according to these parameters:

1. Hydrogel Preparation and Characterization
Synthesize pure GelMA precursor solution by dissolving 50 mg GelMA powder in 1 mL PBS containing LAP photoinitiator (0.05 g LAP per 20 mL PBS) with gentle heat and dark shaking, then filter through a 0.22 μm membrane. Prepare the alogliptin-loaded hydrogel (Gel-A) by co-dissolving 50 mg GelMA and 7.5 mg alogliptin in 1 mL of the LAP/PBS solution (7.5 mg/mL final drug concentration). UV-photocure 1 mL samples of each group to measure equilibrium water content (comparing wet weight to 24-hour vacuum freeze-dried weight, n=3 per group), analyze surface structure and particle distribution via SEM (freeze-dry for 48 hours, cut into ~1 mm³ blocks, gold-sputter coat), and track in vitro release kinetics in 10 mL PBS (pH 7.4) at 37 °C, taking supernatant samples at days 15, 17, and 20.

2. In Vitro Cellular Assays
Culture provided rat BMSCs (confirming CD29+/CD90+/CD34-), BMMs (CD11b+), and HUVECs. Assess cell viability and proliferation using CCK-8 under 100 nM alogliptin and 200 μM metformin treatments. Treat BMSCs for 48 hours with saline, alogliptin, or metformin, and perform ELISAs on the supernatants for VEGF, TNF-α, and IL-10. Evaluate BMSC morphology and attachment at 24 hours via Ki-67 and FITC-Phalloidin staining. Induce osteogenic differentiation in BMSCs using standard osteogenic media (renewed every 3 days): quantify ALP activity and staining at day 7; measure mRNA expression of RUNX2, BMP2, ALP, GLP1R, β-catenin, and GSK-3β by qRT-PCR at day 14; and perform Alizarin Red S staining with cetylpyridinium chloride quantification (absorbance at 562 nm) at day 21. For anti-inflammatory testing, induce M1 phenotype in BMMs using 10 ng/mL M-CSF and 200 ng/mL LPS. For angiogenic potential, evaluate HUVEC network formation on Matrigel after 4–6 hours of culture.

3. In Vivo T2DM Rat Model and Surgical Interventions
Induce Type 2 diabetes in 35 male Sprague-Dawley rats (12–13 weeks old, ~300 g) using a 4-week high-fat/high-carbohydrate diet followed by a single IP injection of STZ (35 mg/kg). Confirm T2DM model establishment via fasting blood glucose > 16.7 mmol/L maintained for one week. Under general (1% pentobarbital sodium, 45 mg/kg) and local anesthesia, prepare a standardized implant bed in the femoral intercondylar fossa under constant cold saline irrigation, and place a 3 × 1.5 mm titanium implant. Randomize rats into 5 groups (n=7/group): 
- T group: diabetic control receiving daily oral saline gavage starting 5 days post-op
- A group: receiving daily oral alogliptin gavage (10 mM) starting 5 days post-op
- M group: receiving daily oral metformin gavage (10 mM) starting 5 days post-op
- GelMA group: receiving local injection of 10 μL blank hydrogel into the implant bed prior to implant placement
- GelMA+A group: receiving local injection of 10 μL alogliptin-loaded hydrogel (1%) into the implant bed prior to placement
Provide 3 days of post-op antibiotic prophylaxis. Administer IP Alizarin Red (30 mg/kg) 10 days before euthanasia to trace new bone formation. Euthanize all animals at week 8 and harvest femurs with implants intact.

4. Ex Vivo Micro-CT and Histological Analyses
Scan harvested femurs using micro-CT (80 kV, 70 μA, 10.425 μm resolution). Define a 100 μm annular region of interest (ROI) around the implant surface to quantify bone volume fraction (BV/TV), trabecular number (Tb.N), and trabecular thickness (Tb.Th). Prepare 250–300 μm undecalcified hard tissue sections parallel to the long axis of the femur for section analysis. Prepare 10 μm paraffin sections for HE, modified Masson, Safranin O/Fast Green, Van Gieson, and Toluidine Blue staining. Assess dynamic bone formation under fluorescence microscopy using the pre-labeled Alizarin Red. Perform immunohistochemical staining for RUNX2, BMP2, and ALP to quantify osteogenesis around the implant, and perform immunofluorescence staining for GLP1R, β-catenin, and GSK-3β to analyze pathway expression at the bone-implant interface.
```

label: 

defect_types: 

notes: 

---

## 40. R1A6066  (elisa)

```
Please run the following HIV‑antibody ELISA on our serum samples (duplicates per sample). Use the exact volumes, reagents and controls described.

1. Coat a 96‑well polystyrene microplate (U‑shaped bottom, Sigma‑Aldrich) with 50 ng of a peptide mixture in each well (peptides: HIV‑gp41 fragment 579‑601, gp120 fragments 254‑274, 308‑331, 421‑438). Incubate 4 h at 37 °C in a humidified tray.  
2. Block each well with 25 µl of 3 % non‑fat milk in PBS. Incubate 1 h at room temperature (RT).  
3. Wash the plate 4 × with PBS‑Tween‑20 (0.05 % Tween‑20). Use ~200 µl per wash and discard the wash buffer.  
4. Add 25 µl of each serum sample (1:16 dilution in PBS) in duplicate.  
5. Incubate 90 min at RT.  
6. Wash 4 × with PBS‑Tween‑20.  
7. Add 25 µl of LA‑HRP conjugate (Sigma‑Aldrich, commercial recombinant protein) diluted 1:5000 in PBS. Incubate 90 min at RT.  
8. Wash 4 × with PBS‑Tween‑20.  
9. Add 25 µl TMB substrate to each well. Incubate 15 min in the dark.  
10. Stop the reaction with 25 µl of 3 M H₂SO₄.  
11. Read absorbance at 450 nm with a plate reader (baseline correction at 540 nm optional).  
12. Include the following controls on each plate:  
    a. Positive control – pooled human serum with high titre anti‑HIV antibodies (25 µl per well).  
    b. Negative control – pooled serum from healthy individuals (25 µl per well).  
    c. Blank – 0.9 % normal saline solution (25 µl per well).  
13. Calculate the assay cut‑off as the mean OD of the negative control plus two standard deviations. Any sample OD above this value is considered positive.  

Please notify me of any deviations or issues encountered during the run.
```

label: 

defect_types: 

notes: 

---

## 41. R0F2D2F  (viability)

```
Run the CellTiter‑Glo luminescent cell viability assay on our 96‑well white‑walled plates.  

**Materials**  
- CellTiter‑Glo® Luminescent Cell Viability reagent, 10 mL (Promega #G7570).  
- Caspase Glo buffer (same buffer supplied with the kit).  

**Procedure**  

1. Treat the cells in the 96‑well plate as per our experimental design (compound exposure, time points, etc.).  
2. Equilibrate both the CellTiter‑Glo reagent and the 96‑well plate to room temperature (≈22 °C) for at least 30 minutes before adding anything.  
3. Prepare the assay reagent by mixing an equal volume of Caspase Glo buffer with the CellTiter‑Glo substrate (1:1 ratio). For each sample add 100 µL of this mixed reagent to 100 µL of the cell culture media in the corresponding well. Include a media‑only control well.  
4. After adding the reagent, place the plate on an orbital shaker for 2 minutes to ensure thorough mixing.  
5. Allow the plate to incubate at room temperature for 10 minutes (no further mixing required).  
6. Measure luminescence on a compatible plate reader.  

Please use the standard settings for the luminescence detector (integration time 1 second per well). Let me know if you need any additional information or if you encounter any issues.
```

label: 

defect_types: 

notes: 

---

## 42. RBFD3FF  (elisa)

```
Please run the glucagon ELISA on the human islet hormone extracts we have shipped to you, following the Vanderbilt HIPP SOP (HIPP‑10‑v01). Below are the specific actions we need you to perform:

1. **Materials** – Use the Quantikine Glucagon ELISA Kit (R&D Systems, Cat #DGCG0) together with the accompanying Glucagon Control Set (Cat #QC100). All kit components are within expiration; keep reagents at 2‑8 °C except the standard, which should be brought to room temperature before use. Also have on hand the 50 µL epMotion tips, 10 mL and 25 mL serological pipets, 2 mL SafeSeal tubes, and filtered 200 µL/1000 µL tips.

2. **Equipment** – The assay should be performed on your epMotion liquid‑handling workstation (or by hand if needed), using the Benchmark Orbi shaker, Fisher AccuWash plate washer, and the BMG Labtech CLARIOstar plate reader (450 nm with 540 nm correction). A vortex mixer and a multi‑channel pipette (20‑200 µL) are also required.

3. **Sample preparation**  
   a. Thaw the archived islet hormone extracts in a room‑temperature water bath; invert each capped tube ten times to mix. Keep the extracts on ice thereafter.  
   b. Prepare serial dilutions of each extract in 2 mL SafeSeal tubes using the kit’s Calibrator Diluent (RD5‑59): 1:100, 1:1,000, 1:2,000, 1:5,000, and 1:10,000. Vortex each tube thoroughly before making the next dilution.  

4. **Standard and control preparation**  
   a. Bring the Glucagon Standard (20,000 pg/mL) to room temperature. Make a 1:10 dilution with Calibrator Diluent, then perform six successive 1:2 dilutions to generate the standard curve. Vortex after each step.  
   b. Reconstitute each Quality Control stock in 5 mL distilled water (or thaw existing QC aliquots) and keep on ice.  

5. **Wash buffer** – Dilute 100 mL of Wash Buffer concentrate (provided) with 900 mL de‑ionized water.  

6. **Plate preparation**  
   a. Using the plate washer, pre‑soak the glucagon ELISA plate wells with 800 µL of diluted wash buffer for 30 s, then wash/aspirate twice with 400 µL wash buffer.  
   b. Add 150 µL of Assay Diluent (RD1‑110) to every well.  
   c. Add 50 µL of each standard, QC, and sample dilution (in duplicate) to the appropriate wells using the epMotion (or hand‑pipetting).  
   d. Cover the plate with the supplied adhesive strip and incubate 3 h at room temperature on the orbital shaker.  

7. **Detection**  
   a. Wash the plate as in step 6a (three wash cycles).  
   b. Add 200 µL of ice‑cold Glucagon Conjugate to each well, cover with a fresh adhesive strip, and incubate 1 h at 4 °C (do not stack plates).  
   c. Wash again as in step 6a (three cycles).  
   d. Within 15 min of opening, mix Color Reagent A and B 1:1, add 200 µL to each well, and incubate 30 min at room temperature protected from light.  
   e. Add 50 µL Stop Solution to each well.  

8. **Reading** – Measure absorbance on the CLARIOstar within 30 min of adding stop solution (450 nm, reference 540 nm). Export raw OD values.  

9. **Data analysis**  
   a. Verify that all standards fall within ±15 % of expected values and that duplicate CV ≤ 20 %; repeat the assay if not.  
   b. Confirm QC results are within their defined ranges; repeat if they fall outside.  
   c. Calculate glucagon concentrations for each sample dilution, then average the four dilutions to obtain the extract’s glucagon content (pg/mL).  
   d. Normalize to islet volume (pg/100 IEQ/min) and compute % content/min.  
   e. Using GraphPad Prism, generate standard curves, calculate stimulation index and AUC for any secretagogue conditions, and produce the required graphs.  

10. **Reporting**  
    a. Provide us with the raw OD data, the calculated concentrations, normalized values, and the Prism graphs (SI and AUC).  
    b. Upload all raw and processed data to the IIDP HIPP database within three business days of assay completion, and send us a confirmation email with the database entry ID.  

If any step deviates from the protocol or you encounter a problem that could affect the results, please document the deviation and notify us immediately so we can decide on next steps. Thank you.
```

label: 

defect_types: 

notes: 

---

## 43. R5A01D7  (growth_curve)

```
1. Transform the provided pET28a-His6-ARID3B and EGFP-ARID3B-pET28a plasmids into E. coli BL21(DE3) cells, plate on LB agar with 50 kB/mL kanamycin, and prepare glycerol stocks from single colonies.

2. Perform a small-scale expression test in 4 mL cultures (OD600 = 0.5–0.8) induced with 0.2 mM IPTG at 15°C and 37°C, analyzing whole cells and soluble/insoluble fractions by SDS-PAGE to determine optimal large-scale induction conditions.

3. Conduct large-scale expression in LB-kanamycin (16 h induction with 0.2 mM IPTG at the optimized temperature), harvest cells by centrifugation, and lyse the pellets in ice-cold lysis buffer (50 mM Tris pH 8.0, 300 mM NaCl, 20 mM imidazole, 1% Triton X-100, 1 mM DTT, 1 mM PMSF) via probe sonication (30–40% power, 20 min total, 3 s ON/6 s OFF).

4. Clarify the lysate by centrifugation at 13,000 × g for 20 min at 4°C and run Ni-IDA affinity chromatography on the soluble supernatant using an equilibration buffer of 50 mM Tris pH 8.0, 300 mM NaCl, 20 mM imidazole, and eluting with the same buffer supplemented to 500 mM imidazole.

5. Analyze fractions by 10–12% SDS-PAGE and Coomassie staining, pool high-purity elution fractions, dialyze into PBS (pH 7.4), filter through a 0.22 µm filter, and determine protein concentration via Bradford assay using BSA standards.

6. Perform quality control on purified ARID3B via SDS-PAGE (comparing against 1 µg BSA) and Western blot using a multi-tag antibody, followed by freeze-thaw stability testing, reconstitution testing, and size-exclusion chromatography (SEC) analysis. Repeat this expression and purification workflow for EGFP-ARID3B.

7. For the in vitro phase separation assay, dilute clarified ARID3B protein stock into LLPS stock buffer (25 mM Tris-HCl pH 7.4, 500 mM NaCl, 10% glycerol, 1 mM DTT), mix with 10% (w/v) PEG-4000 and water without vortexing, incubate at 20°C–25°C for 15–30 min, and image 3–5 µL of the reaction on a glass slide using bright-field microscopy (for unlabeled ARID3B) or 488 nm fluorescence microscopy (for EGFP-ARID3B).

8. Seed HEPM cells on sterile glass coverslips in 6-well plates to 50–70% confluency and transiently transfect with EGFP-ARID3B plasmid DNA using Lipofectamine 2000 in OPTI-MEM for 24 hours.

9. Perform live-cell confocal imaging of EGFP-ARID3B condensates in HEPM cells using a 100× oil immersion objective and 488 nm laser excitation at 1–5% power on a microscope enclosed in a 37°C environmental chamber (n ≥ 10 cells from 3 independent transfections).

10. Fix transfected HEPM cells with 4% PFA in PBS for 15 min, permeabilize with 0.1–0.3% Triton X-100, block with normal goat serum, and perform immunofluorescence staining using an anti-SMAD2/3 primary antibody (1:200 dilution, overnight at 4°C) followed by a red-fluorescent secondary antibody and DAPI nuclear staining. Mount coverslips and image on a confocal microscope (405, 488, and 594 nm laser lines) to assess co-localization of EGFP-ARID3B condensates with SMAD2/3.

11. Perform in vitro and live-cell (HEPM) FRAP assays on ARID3B condensates using a confocal microscope equipped with a FRAP module and 488 nm laser: capture 3–5 pre-bleach images, photobleach an ROI within a droplet using high-power 488 nm illumination until intensity drops to 60–80%, and record time-lapse recovery images every 1–3 s for 2–5 min.
```

label: 

defect_types: 

notes: 

---

## 44. R728648  (viability)

```
1. Seed our hiPS cell samples using Accutase and culture them for at least 2 passages on MEF- or Matrigel-coated 6-well plates prior to starting the protocol.
2. Formulate all required media (MEF, hiPS, iPS-Brew, cryopreservation, and the various Day 0 through Day 10–14 Spin EB media), buffers, and cytokine solutions (Collagenase IV, 0.5 mM EDTA, bFGF, BMP-4, SCF, TPO, VEGF, CHIR99021, LAA, MTG, and Holo-Transferrin) under sterile conditions.
3. Perform the Spin EB differentiation protocol: detach hiPS cells with Accutase, strain through a 0.70 µm strainer, centrifuge, resuspend in KO-DMEM with CEPT cocktail, count, and seed 2 x 10^6 cells in 5 mL of KO-DMEM + CEPT before pelleting (3000–5000 cells per well in a 96-well U-bottom suspension plate using Day 0 Spin EB medium). Centrifuge at 400 g with low acceleration/deceleration to form the EBs.
4. Execute the daily media changes and feeding regimen according to the timeline: top up with Day 2 Spin EB medium on Day 2, perform daily partial changes with Day 3–8 medium, transition to Day 8–10 medium for progenitor expansion, and continue daily partial changes with Day 10–14 medium through the expansion phase.
5. On Day 14, harvest the EBs and hematopoietic/megakaryocyte progenitors by gentle pipetting, wash, and resuspend at 1 x 10^6 cells/mL in Day 10–14 medium for expansion (adding 5 mL fresh medium on Day 16 and performing a full medium change on Day 18).
6. Run the CellTiter-Glo short-term drug testing assay on Day 14 harvested cells by plating 10,000 cells per well (at 115,000 cells/mL) in 96-well U-bottom plates against serial dilutions of our test compounds (100 µM to 10 nM in triplicates with DMSO controls), incubate for 66–72 hours at 37°C/5% CO2, add CellTiter-Glo reagent, and read luminescence on a plate reader.
7. Perform flow cytometry staining on Day 14 and Day 18 samples using the specified panels (CD45, CD34, CD117, CD41/61, CD42b, and CD235a) after Fc receptor blocking and appropriate starvation steps where necessary. Analyze the data using FlowJo to generate singlets gates, concatenate files, build tSNE plots, and assess megakaryocyte maturation populations.
8. Perform MACS isolation on Day 14 harvested cells using CD61 microbeads to isolate the CD61+ megakaryocyte population for downstream counting and functional characterization.
```

label: 

defect_types: 

notes: 

---

## 45. R61702F  (qpcr)

```
1. Culture human foreskin fibroblasts (HFF1, ATCC SCRC‑1041) in DMEM supplemented with 10 % FBS, 2 mM L‑glutamine, and 1 % penicillin/streptomycin. Keep cells at standard temperature, humidity, and 5 % CO₂. Seed control and experimental plates at the same confluence and passage number; aim for stable proliferation before treatment.

2. Treat the experimental plates with the REAC CO‑IBZ protocol using a BENE 110 device (ASMED). Apply the Asymmetric Conveyor Probe (ACP) directly onto the culture for nine 30‑min sessions total: three sessions per day on three consecutive days, with each session starting one hour after the previous one ends. Handle control plates in parallel under identical culture conditions but without the ACP.

3. After the final CO‑IBZ session, harvest cells from each biological replicate (n = 5 per condition). Extract total RNA using the Qiagen RNeasy Mini Kit, measure concentration and purity spectrophotometrically, and store at –80 °C until analysis.

4. Perform one‑step quantitative RT‑PCR (Luna Universal One‑Step RT‑qPCR Kit, NEB) on a Bio‑Rad CFX thermal cycler for the following targets: SIRT1, NOX4, VEGF, p16, p21, HAS2. Use GAPDH as the reference gene. Run each biological sample in technical triplicate, average the triplicates, and calculate relative expression with the 2⁻ΔΔCt method. Confirm that GAPDH Cq values do not differ between groups.

5. For immunofluorescence, fix and permeabilize cells from each replicate. Incubate overnight at 4 °C with primary antibodies at the indicated dilutions: SIRT1 (1:100, Cell Signaling), NOX4 (1:500 from a 1:50 stock, Santa Cruz), PARP1 (1:800, Cell Signaling), vWF (1:500 from a 1:50 stock, Santa Cruz), collagen III (1:500, Abcam). After washing, apply fluorescence‑conjugated secondary antibodies (Life Technologies) at 1:500 for 1 h at 37 °C in the dark. Counterstain nuclei with DAPI (1 µg/mL). Acquire images on a Leica THUNDER Imager DMi8 using identical exposure, illumination, and acquisition settings for all samples. Quantify mean fluorescence intensity with ImageJ/Fiji, collapsing technical images into one value per biological replicate.

6. Measure total antioxidant capacity (TAC) in the culture supernatant using the Abcam Total Antioxidant Capacity Colorimetric Assay Kit. Add 100 µL Cu²⁺ working solution to each well, incubate 90 min at room temperature on an orbital shaker protected from light, then read absorbance at 570 nm on an Akribis plate reader. Calculate TAC as (Ts/Sv) × D using the standard curve (Ts = nmol, Sv = µL added, D = dilution factor). Perform the assay on five independent biological replicates per condition.

7. Determine nitrite levels with the Thermo Fisher Griess Reagent Kit. Mix 20 µL Griess reagent with 150 µL sample, incubate 30 min at room temperature, and read absorbance at 548 nm on the same plate reader. Use five biological replicates per condition.

8. Assess intracellular ROS using CM‑H₂DCFDA (Thermo Fisher). After treatment, incubate cells with 10 µM dye for 30 min at 37 °C in the dark, wash with PBS, and measure fluorescence (excitation 485 nm, emission 530 nm) in fresh PBS on the plate reader. Run five biological replicates.

9. For all quantitative assays (RT‑qPCR, immunofluorescence intensity, TAC, nitrite, ROS), average technical replicates within each biological replicate before any statistical testing. Use GraphPad Prism 9 to assess normality (Shapiro–Wilk) and compare control vs. CO‑IBZ groups with an unpaired two‑tailed Welch’s t‑test. Report results as mean ± SD; consider p < 0.05 significant.

Please process our HFF1 samples according to the above workflow and return raw data files, processed results, and a brief statistical summary for each assay. Let us know promptly if any reagents or equipment are unavailable.
```

label: 

defect_types: 

notes: 

---

## 46. R66B651  (elisa)

```
Please run an alpha-Synuclein quantification ELISA on our submitted samples in duplicate using the following steps:

1. Coat 384-well MaxiSorp plates (Nunc) with the anti-α-Syn capture antibody (BD Biosciences, cat #610787) diluted 1:500 in coating buffer (NaHCO3 with 0.2% NaN3, pH 9.6) overnight at 4 °C.
2. Wash 3 times with PBS containing 0.05% Tween-20 (PBS-T).
3. Block the plates for 1 hour at 37 °C in blocking buffer (1.125% fish skin gelatin in PBS-T).
4. Load our samples along with your standard curve in duplicate into the wells.
5. Incubate at room temperature for 2 hours.
6. Add the detection antibody (diluted in blocking buffer) and incubate for 1 hour at 37 °C.
7. Wash 5 times with PBS-T.
8. Add ExtrAvidin phosphatase (Sigma, cat #E2636) diluted in blocking buffer to the wells and incubate for 30 minutes at 37 °C.
9. Perform color development using fast-p-nitrophenyl phosphate substrate (Sigma, cat #N1891), reading absorbance at 405 nm every 2.5 minutes for up to 60 minutes.
10. Determine the concentration of α-Syn in our samples by selecting the time point(s) where the standards and sample dilutions are within the linear/log phase. 

Please provide the final calculated concentration data along with the raw kinetic absorbance reads.
```

label: 

defect_types: 

notes: 

---

## 47. R20EDA4  (elisa)

```
1. Produce recombinant SOD protein in E. coli using the pET‑28a vector with an N‑terminal 6×His tag, purify it by IMAC, and verify >95 % purity by SDS‑PAGE (expected MW ≈ 18.1 kDa).  

2. Prepare two vaccine formulations:  
   a. Mix the purified SOD (100 µg per dose) 1:1 (v/v) with aluminum hydroxide to a final Al(OH)₃ concentration of 0.2 %.  
   b. Mix the same amount of SOD 1:1 (v/v) with the oil‑in‑water nano‑emulsion adjuvant AddaS03™ (InvivoGen, cat. vac‑as03‑10).  

3. Include the following controls in the immunization study:  
   - Recombinant human SOD1 (Novus, cat. NBP2‑34940) as a positive control antigen.  
   - Brucella OMP16, OMP19, L7/L12, and IalB (purified at the Research Institute for Biological Safety Problems) as heterologous antigens for cross‑reactivity checks.  
   - BSA and PBS (pH 7.2–7.4) as negative controls.  

4. Immunize a cohort of clinically healthy, brucellosis‑seronegative sheep (6–12 months old, ≥ 20 kg) under the approved protocol (Bioethics Committee No. 1, 24 May 2024). Use a prime‑boost schedule identical to Figure 1 of the source paper, administering 100 µg of SOD per injection. Collect blood on days 21, 28, 35, and 42 post‑first immunization; process serum and store at –80 °C until analysis.  

5. Perform agar gel immunodiffusion (AGID) on each serum sample:  
   - Use 1 % agarose in physiological saline with rivanol, set in a humid chamber at 24 °C.  
   - Prepare Brucella antigen (IDvet, AGID activity 1:8) as the test antigen.  
   - Run two‑fold serial dilutions of serum from 1:2 to 1:32, incubate 24–36 h, and read precipitation lines.  

6. Perform quantitative Brucella IgG ELISA on the same sera using the MyBioSource commercial kit, following the manufacturer’s protocol; read absorbance at 450 nm.  

7. Set up a single radial immunodiffusion (SRID) assay to quantify SOD:  
   - Prepare 1.5 % agarose in 0.01 M PBS (pH 7.2–7.4) containing monospecific antiserum at 15 µL/mL.  
   - Pre‑treat standard SOD and test samples with 10 % Zwittergent 3‑14 (1:10 v/v), incubate 30 min at room temperature, then dilute in PBS.  
   - Add 25 µL of each standard or sample to wells, incubate in a humid chamber at room temperature for 24 h.  
   - Wash gels five times with PBS (30–40 min each, 40–50 rpm shaking), then twice with distilled water (15 min each).  
   - Stain with 0.3 % Coomassie Brilliant Blue G‑250, destain in acetic‑ethanol until clear precipitation rings appear.  
   - Measure ring diameters (to 0.1 mm), calculate D², and generate a calibration curve from the reference standard.  

8. Validate the SRID assay as follows (run each condition in triplicate):  
   - **Specificity:** Test SOD concentrations of 20, 10, and 5 µg/mL (and serial dilutions) against unrelated proteins (OMP16, OMP19, L7/L12, IalB, BSA) and PBS. Expect rings only for SOD. Record D, D², mean, SD, and CV; accept if CV ≤ 10 % and rings are symmetric.  
   - **Sensitivity:** Perform two‑fold serial dilutions of SOD from 10 µg/mL down to 0.078 µg/mL. Determine the lowest concentration that yields reproducible rings with CV ≤ 10 %; define this as the LOD.  
   - **Linearity:** Run SOD standards from 10 to 0.625 µg/mL, plot D² versus concentration, perform linear regression, and confirm R² ≥ 0.95.  
   - **Precision (repeatability):** Test SOD at 20 µg/mL and 5 µg/mL in three independent assay runs, each with three replicates (total n = 9). Calculate D_mean, SD, and CV; accept CV ≤ 10 %.  
   - **Robustness:** Repeat the assay at 20 and 5 µg/mL while varying incubation temperature (25 ± 3 °C), agarose thickness (2.5–3.0 mm), incubation time (20–24 h), and using different operators and reagent lots. Assess D² and CV; robustness is confirmed if CV remains ≤ 10 % across conditions.  

9. Analyze all quantitative data using GraphPad Prism 10: report mean ± SD, compute CVs, perform linear regression for D² vs. concentration, and record R² values. Provide the full data set and statistical outputs in the final report.  

Please let us know if any reagents are unavailable or if adjustments to the schedule are needed. Thank you.
```

label: 

defect_types: 

notes: 

---

## 48. RCDFEE5  (elisa)

```
Please run the following workflow on the serum and dried blood spot (DBS) samples we will provide:

1. **Sample receipt and storage**  
   - Register each DBS card by scanning its barcode into the database.  
   - Store all DBS cards at –80 °C in zip‑lock bags with desiccant until processing.  
   - Store serum aliquots at –80 °C in temperature‑controlled freezers.

2. **Stability sub‑study (if applicable)**  
   - For the designated subset of DBS cards, place them under each of the six conditions for 11 days after collection:  
     a. Freezer (–18 °C to –21 °C)  
     b. Refrigerator (4 °C‑7 °C)  
     c. Room temperature (22 °C‑25 °C)  
     d. Incubator (36 °C‑38 °C)  
     e. Direct sunlight on a window ledge (full‑day exposure, room temperature)  
     f. Wet packaging (≤3 h drying before sealing)  
   - After 11 days, move the cards back to –80 °C until extraction.

3. **DBS punching and elution**  
   - Thaw DBS cards at room temperature, keeping them in sealed bags to avoid condensation.  
   - Using the Panthera‑Puncher 9 (PerkinElmer), punch three 3.2 mm discs from each card into a barcoded 96‑well plate (one plate per 96 samples).  
   - Add 80 µL of the supplied elution buffer to each well with an adjustable‑tip multichannel pipette (Integra Voyager).  
   - Incubate the plate on a temperature‑controlled shaker (MIUlab ES‑60E) for 1 h at 37 °C, 300 rpm.  
   - Transfer the eluates into Roche 13/16 micro‑sample cups (catalog 05085713001) and store at –80 °C until analysis.

4. **Roche Elecsys EBV serology**  
   - Use the Cobas e801 (Roche) to run the Elecsys EBV EBNA‑IgG and Elecsys EBV VCA‑IgG assays on both serum and DBS eluates.  
   - Run paired serum and DBS from each participant on the same day, using the same reagent lot.  
   - Record the raw Cut‑Off Index (COI) values for each sample.

5. **Dilution protocol**  
   - For DBS eluates: if anti‑EBNA‑1 COI ≥ 10 or anti‑VCA COI ≥ 80, dilute 1:10 with the assay buffer and re‑run.  
   - For serum: if anti‑VCA COI ≥ 1500 or anti‑EBNA COI ≥ 130, dilute 1:20 and re‑run.  
   - Back‑calculate the original concentrations using the dilution factor.

6. **Data linkage**  
   - Ensure the barcode from the DBS card is linked to the well position, the micro‑sample cup, and the resulting Cobas output.  
   - Export the results (raw COI and any back‑calculated values) together with the barcode into a CSV file for our analysis.

7. **Quality control**  
   - Confirm that each 96‑well plate contains a unique plate barcode and that the punching software blocks duplicate punches of the same card within a plate.  
   - Include the standard Roche quality controls for each assay run and note any out‑of‑range values.

8. **Report**  
   - Provide us with the complete dataset (barcode, sample type, raw COI, dilution factor, back‑calculated value, assay date, lot number).  
   - Include a short summary of any samples that failed QC, any deviations from the protocol, and the storage conditions used for the stability sub‑study samples.

Let us know if any reagents, consumables, or equipment listed above are unavailable, or if you need clarification on any step. Thank you.
```

label: 

defect_types: 

notes: 

---

## 49. RC261EA  (growth_curve)

```
1. Please perform codon optimization on our target DNA sequence for bacterial expression in E. coli, ensuring the insert contains an N-terminal 6x His-tag flanked by NdeI and XhoI restriction sites, and confirm the sequence via Sanger sequencing using T7 promoter primers.

2. Transform 1–10 ng of the sequence-verified plasmid into competent E. coli BL21(DE3) or Rosetta-gami(DE3) cells.

3. Set up a 150 mL overnight culture in LB or TB medium supplemented with 100 µg/mL ampicillin using a single colony or glycerol stock scrape, and incubate at 37°C and 200 rpm for approximately 16 hours.

4. The following day, dilute the overnight culture into fresh medium in a 1 L Erlenmeyer flask to an OD600 of approximately 0.5, and induce protein expression by adding IPTG to a final concentration of 1 mM. Incubate at 37°C for 4 hours (or optionally overnight at 22°C, 200 rpm).

5. Pellet the bacteria by centrifuging at ≥4000 × g for 20 minutes at 4°C, discard the supernatant, and freeze the pellets at -20°C overnight.

6. Thaw the bacterial pellets and resuspend them in an appropriate sonication/lysis buffer (such as PBS, 2–8 M urea in PBS, or 2 M urea, 20% glycerol, 1 µM EDTA, 1% Triton X-100) at 5 mL of buffer per 50 mL of original culture volume.

7. Lyse the bacteria on ice using a sonicator (e.g., 15 cycles of 20s on / 30s off at an amplitude of 22–24 microns) or a high shear homogenizer. Immediately add PMSF to a final concentration of 1 mM post-lysis, and centrifuge at ≥4000 × g for 10 minutes at 4°C to pellet the debris. Retain both supernatant and pellet to check for protein solubility.

8. Incubate the protein-containing fraction with Ni-NTA agarose beads (300–500 µL of beads per 10 mL of supernatant) on a roller bench at 2–8°C for 3 hours or overnight.

9. Pellet the Ni-NTA beads by centrifugation (1500 × g, 5 min, 4°C), wash them five times with wash buffer (1 M NaCl, PBS, 0.05% Tween-20) and once with plain PBS, then pack the resuspended beads into a syringe-based column.

10. Elute the bound protein using four consecutive column volumes of fresh 200 mM imidazole solution (containing 200 mM imidazole, 1 M NaCl, 200 mM Tris pH 8.0, 1 mM PMSF). If necessary, use buffer E (100 mM NaH2PO4, 10 mM Tris, 8 M urea, pH 4.5) or 50–500 mM EDTA as alternative elution buffers.

11. Assess the elution fractions by SDS-PAGE and Coomassie staining (using a 4:1 colloidal Coomassie to methanol mix), confirm identity via western blot or mass spectrometry, and pool fractions with compatible protein content.

12. Transfer the pooled fractions into a Slide-A-Lyzer G3 dialysis cassette and dialyze against at least 500 mL of the target buffer overnight at 4°C with multiple buffer exchanges the following day, then determine the final protein concentration using a BCA assay.

13. For murine immunizations, prepare vaccine emulsions for up to 10 mice at a time by combining the purified protein with either Freund's adjuvant or Montanide ISA 720/CpG 1826 (incorporating 50% extra volume for pipetting loss) in a 2 mL Eppendorf tube and vortexing at full speed on a Vortex Genie 2 for 30 minutes at room temperature.

14. Administer 100 µL of the vaccine emulsion subcutaneously into the left groin of each mouse within 2 hours of preparation, and collect blood samples from the tail vein or vena saphena one week after each vaccination (following an initial null serum sample).

15. Allow blood samples to coagulate overnight at 2–8°C, centrifuge at max 4500 × g for 10 minutes at 4°C to collect the serum, and store at -20°C.

16. Perform ELISAs by coating 96-well plates with the target protein (2–8 µg/mL), blocking with 4% milk in PBS, incubating with serially diluted mouse sera (pre-blocked with bacterial extract if the coating protein was produced in-house), and detecting bound antibodies using biotinylated anti-mouse Ig followed by streptavidin-HRP and TMB substrate, reading absorbance at 655 nm.
```

label: 

defect_types: 

notes: 

---

## 50. R4449B1  (elisa)

```
Please run the following ELISA on the supplied animal sera (cat, rat, and hen IgY samples) and include the indicated controls.

1. Coat each well of a Nunc 96‑well U‑shaped bottom plate with 50 ng synthetic gp‑120 peptide diluted in BioLegend Coating Buffer. Add 100 µL per well and incubate overnight at 4 °C.

2. Wash the plate 4 × with PBS + 0.05 % Tween‑20. Block by adding 25 µL per well of 3 % non‑fat dry milk in PBS. Incubate 1 h at room temperature (RT).

3. Wash 4 × with PBS‑Tween‑20. Add the following to each well in triplicate (25 µL per well):
   - 25 µL IgY (1 mg/mL) as a positive antibody control.
   - 25 µL of each test serum (cat or rat) diluted 1:16 in PBS containing 3 % non‑fat milk.
   - For negative control wells, add 25 µL turtle serum (Sigma) diluted 1:16 in the same buffer.
   - For blanks, add 25 µL 0.9 % normal saline.

   Incubate 2 h at RT.

4. Wash 4 × with PBS‑Tween‑20. Add 25 µL per well of the universal conjugate SpLAG‑anti‑IgY‑HRP (peroxidase‑labelled IgY chemically coupled to protein A, G, and L) diluted 1:1,000 in ELISA Diluent (2 × , 120 mL, STEMCELL). Incubate 1 h at RT.

5. Wash 4 × with PBS‑Tween‑20. Add 50 µL TMB substrate (3,3′,5,5′‑tetramethylbenzidine, Sigma, Cat #54827‑17‑7) to each well. Protect from light and incubate 15 min.

6. Stop the reaction when the positive human serum control wells develop a clear color while the turtle serum and blank wells remain colorless. Record absorbance at 450 nm.

7. Calculate the cut‑off: mean absorbance of the turtle serum negative controls × 4. Any sample above this value is considered positive for anti‑HIV antibodies.

Please run each sample in triplicate, include the positive human serum control (anti‑HIV antibodies) on each plate, and report the raw absorbance values together with the calculated cut‑off and positivity calls for each animal. Let me know if any reagents are missing or if additional clarification is needed.
```

label: 

defect_types: 

notes: 

---

## 51. RA6BF3C  (growth_curve)

```
Please run a growth curve and fluorescent protein expression assay on our provided Chlamydomonas reinhardtii samples using the following procedure:

1. Inoculate 1 mL of cells from a stationary phase culture (120 to 168 hours old) into a 100 mL Erlenmeyer flask containing 50 mL of TAP media. 
2. Incubate the culture on an orbital shaker at 25 °C, 150 rpm (1 cm orbit), under 80 µmol/m²s of incident white light (acceptable range 60 to 120 µmol/m²s).
3. Take an initial 100 µL sample for plate reader measurements, and continue taking 100 µL samples at least once daily for 168 hours. Ensure total volume removed for sampling does not exceed 10% of the culture, and include technical replicates at each time point.
4. Perform all plate reader measurements in black 96-well plates with clear bottoms (Perkin Elmer IsoPlate-96F or equivalent) using the following settings with bottom optics:
   - Absorbance: 750 nm
   - Chlorophyll: Ex 440 nm / Em 680 nm (Gain 70)
   - mVenus: Ex 500 nm / Em 530 nm (Gain 120)
   - mCherry: Ex 583 nm / Em 613 nm (Gain 150)
5. Retain the final culture at the end of the time course for dry cell weight determination.
```

label: 

defect_types: 

notes: 

---

## 52. RB9B831  (viability)

```
1. Synthesize N-CDs by dissolving 0.75 g citric acid and 0.75 g urea in distilled water to a 5 mL final volume. Synthesize BN-CDs using 0.75 g citric acid, 0.37 g urea, and 0.37 g boric acid dissolved in distilled water to 5 mL. 

2. Perform microwave-assisted synthesis for both mixtures in open borosilicate glass tubes using a 1000 W, 2.45 GHz microwave oven at 540 W (324 kJ) for 10 min. 

3. Dilute the resulting brown solutions 4:1 (v/v) with distilled water and sonicate in a water bath at 40 kHz and 143 W for 15 min at room temperature. 

4. Purify the crude suspensions by centrifuging at 3000 G to remove coarse precipitate, filtering the supernatant sequentially through 0.45 µm and 0.22 µm nylon syringe filters, and performing a final centrifugation of the filtrate at 1000 G. Determine the final carbon dot (CD) concentration gravimetrically by freeze-drying a 1 mL aliquot to constant weight, and prepare 5 mg/mL stock solutions in autoclaved pure water.

5. Characterize the CD suspensions using UV-Vis absorption (200–800 nm, 1 cm quartz cuvette, deionized water reference), steady-state fluorescence spectroscopy, absolute photoluminescence quantum yield (PLQY) via an integrating sphere, transmission electron microscopy (STEM-HAADF at 200 kV), and EELS (0.05 eV/channel dispersion, 200 kV).

6. Culture NIH3T3 (3T3) and KRAS-transformed NIH3T3 (KRAS) cells in DMEM High Glucose supplemented with 10% FBS, 4 mM Glutamine, and 1% Penicillin/Streptomycin at 37 °C and 5% CO2. 

7. For cellular treatments, seed cells on sterilized glass coverslips in 6-well plates at 400,000 cells/well. At 80% confluency, wash three times with PBS and incubate cells for 1 h at 37 °C and 5% CO2 with N-CDs or BN-CDs at 50 and 100 µg/mL (using 20 and 40 µL of the 5 mg/mL stock, respectively) in 2 mL growth medium.

8. Perform an MTT assay for cell viability by seeding 10,000 cells/well in 96-well plates. After 24 h, wash with PBS, treat with 50 and 100 µg/mL CDs in 1 mL growth medium for 1 h, wash with PBS, and incubate with 0.25 mg/mL MTT solution in growth medium at 37 °C for 2 h. Solubilize the resulting formazan crystals in 150 µL isopropanol and measure absorbance at 590 nm.

9. Prepare samples for scanning electron microscopy (SEM) by fixing cells treated with BN-CDs in 2.5% glutaraldehyde in PBS for 30–60 min at room temperature, dehydrating through a graded ethanol series (30% to 100%), drying, and imaging at low voltage (1–5 keV) without coating.

10. Perform laser scanning confocal microscopy (LSCM) on 3T3 and KRAS cells treated with CDs (50 or 100 µg/mL) by co-staining with organelle trackers: MitoTracker Orange-Red (0.3 µM for 15 min, fixed with 4% PFA), Golgi Tracker (CellLight Golgi-GFP, overnight incubation), LysoTracker Green DND-26 (75 nM for 30 min, live-cell), or ER-Tracker Green (1 µM for 30 min, live-cell). Image using excitation at 405 nm for CDs and appropriate matching channels for the trackers, quantifying mean fluorescence intensity per cell across approximately 5 fields per sample.

11. Conduct bioenergetic analysis using a Seahorse XFe24 analyzer and XF Cell Mito Stress Test. Seed 800 cells/mm² in XFe24 plates in XF RPMI medium supplemented with 10 mM glucose, 2 mM L-glutamine, and 1 mM sodium pyruvate. Measure OCR and ECAR baselines, followed by sequential injections of 1 µM oligomycin, 1.5 µM FCCP, and 1 µM rotenone + 1 µM antimycin A, concluding with 50 mM 2-deoxy-d-glucose for glycolysis correction, using five technical replicates per condition.
```

label: 

defect_types: 

notes: 

---

## 53. RC3780B  (qpcr)

```
Please run the following T‑cell activation assay on our Jurkat E6‑1 cells using recombinant human galectins and anti‑CD3/CD28 as controls. Use the reagents and equipment listed below and follow the steps in order.  

1. **Reagents (order if not in stock)**  
   - Jurkat E6‑1 (BCRC 60424)  
   - PE mouse IgG1, κ isotype control (BioLegend 400114)  
   - APC anti‑human CD69 (BioLegend 310910)  
   - GMP Ultra‑LEAF anti‑human CD3 SF (BioLegend 317353)  
   - CD28 monoclonal antibody (Invitrogen 16‑0288‑85)  
   - Recombinant human galectin‑3 (His tag) (GlycoGenetics PL02‑025/050/100)  
   - Recombinant human galectin‑8 variant 1 (317 aa) (GlycoGenetics PL03‑025/050/100)  
   - Recombinant human galectin‑8 variant 2 (359 aa) (GlycoGenetics PL04‑025/050/100)  
   - Recombinant human galectin‑1 (GlycoGenetics PL01‑025/050/100) – optional  
   - Recombinant human galectin‑7 (GlycoGenetics PL05‑025/050/100) – optional  
   - IL‑2 qPCR primers (forward AGAACTCAAACCTCTGGAGGAAG, reverse GCTGTCTCATCAGCATATTCACAC)  
   - GAPDH primers (forward GACGCTGGGGCTGGCATTG, reverse GCTGGTGGTCCAGGGGTC)  
   - PBS (Gibco 10010049)  
   - FBS (Corning 35‑010‑CV)  
   - Pen/Strep (Cytiva SV30010)  
   - RPMI‑1640 (Gibco 11875119)  
   - Sodium pyruvate (Gibco 11360070)  
   - Sodium bicarbonate 7.5 % (Gibco 25080094)  
   - HEPES (Gibco 15630080)  
   - Glucose 200 g/L (Gibco A2494001)  
   - Paraformaldehyde (Sigma P6148‑500G)  
   - Zymo Quick‑RNA Miniprep kit (R1055)  
   - HiScript III RT SuperMix (+gDNA wiper) (Vazyme R323‑01)  
   - FastSYBR mix (CWBIO CW2622M)  
   - Trypan blue 0.4 % (Gibco 15250061)  

2. **Media preparation**  
   - Make RPMI‑1640 complete medium: 500 mL RPMI‑1640 + 50 mL FBS + 5 mL Pen/Strep (store 4 °C, ≤3 mo).  
   - Make Jurkat culture medium: 555 mL complete medium + 5.92 mL sodium pyruvate (1 mM) + 11.84 mL sodium bicarbonate (1.5 g/L) + 5.92 mL HEPES (10 mM) + 13.32 mL glucose (4.5 g/L). Store 4 °C, ≤3 mo.  

3. **4 % PFA** – prepare as described (400 mL PBS heated to 55 °C, dissolve 20 g PFA, adjust pH to 7.4–7.6 with 1 N NaOH then HCl, bring to 500 mL, aliquot 50 mL, store at –20 °C, thaw at 37 °C before use).  

4. **Reconstitute galectins**  
   - Resuspend each lyophilized galectin at 500 µg/mL in Milli‑Q water, keep on ice ≥10 min, flick gently.  
   - Make a 10× working stock (50 µg/mL) by diluting 1:10 with water; store 2–8 °C, use within 1 wk.  

5. **Cell seeding (day –2 to –1)**  
   - Thaw Jurkat cells, culture in Jurkat medium at 37 °C, 5 % CO₂.  
   - Keep passage number <40.  

6. **Treatment setup (day 0)**  
   - Prepare 5 mL treatment media per condition in 6 cm dishes as follows (final galectin concentrations 0, 10, 25, 50 µg/mL; anti‑CD3 (1 µg/mL) + CD28 (1 µg/mL) as positive control):  

     | Condition | Add galectin/antibody (µL) | Add Jurkat medium (µL) | Total volume |
     |-----------|---------------------------|------------------------|--------------|
     | Untreated | 0 | 4000 | 4000 |
     | Anti‑CD3/28 | 5 (2.5 µL anti‑CD3 + 2.5 µL CD28) | 3995 | 4000 |
     | Gal‑3 10 µg/mL | 5 of 100 µg/mL stock | 3995 | 4000 |
     | Gal‑3 25 µg/mL | 12.5 of 100 µg/mL stock | 3987.5 | 4000 |
     | Gal‑3 50 µg/mL | 25 of 100 µg/mL stock | 3975 | 4000 |
     (Repeat same volumes for galectin‑8 V1 and V2.)  

   - Harvest Jurkat cells, count with trypan blue, adjust to 3 × 10⁶ cells/mL.  
   - Add 1 mL cell suspension to each dish (final cell density 0.6 × 10⁶ cells/mL, total 5 mL).  
   - Gently swirl to mix, then incubate 37 °C, 5 % CO₂ for 16–20 h.  

7. **Post‑treatment harvest**  
   - Examine morphology under inverted microscope; note agglutination.  
   - Collect cells, centrifuge 300 × g 5 min RT, discard supernatant, resuspend in 0.1 × original volume.  
   - Count viability; must be >95 %.  

   **For flow cytometry**:  
   - Transfer 2 × 10⁶ cells to a 1.5 mL tube.  
   - Fix: wash once with 200 µL PBS, resuspend in 200 µL 4 % PFA, incubate RT 15 min (mix gently every 3–5 min).  
   - Wash twice with PBS, final resuspension 333 µL PBS, store at –80 °C (until staining).  

   **For RNA**:  
   - Take the remaining cell suspension, centrifuge, wash once with PBS, spin again, discard supernatant, snap‑freeze pellet at –80 °C.  

8. **CD69 flow‑cytometry** (run on CytoFLEX S)  
   - Thaw fixed cells, place 0.3 × 10⁶ cells in 50 µL PBS into each well of a 96‑well V‑bottom plate (triplicate per condition).  
   - Prepare antibody mix: anti‑mouse IgG1‑PE 1:20 and anti‑CD69‑APC 1:10 in PBS (final 5 µg/mL each). Add 50 µL to each well, mix.  
   - Incubate 4 °C 1 h on orbital shaker (≈575 rpm), protected from light.  
   - Spin plate 1,500 × g 5 min RT, discard supernatant, wash with 150 µL PBS, spin again, discard, resuspend in 150 µL PBS.  
   - Acquire ≥10,000 events per sample, gate on FSC/SSC singlets, record CD69 MFI.  

9. **IL‑2 qPCR** (run on StepOne Plus)  
   - Extract RNA from frozen pellets using the Zymo Quick‑RNA kit per manufacturer (include on‑column DNase). Elute in 20–50 µL nuclease‑free water.  
   - Measure RNA at 260 nm (aim for 5–15 µg total, A260/280 = 1.8–2.1).  
   - gDNA removal: in a 0.8 µL reaction combine 4 µL 4× gDNA wiper mix, 1–500 ng RNA, nuclease‑free water to 8 µL; incubate 42 °C 2 min, hold 4 °C.  
   - Reverse transcription: add 2 µL HiScript III RT SuperMix, incubate 37 °C 15 min then 85 °C 5 s. Dilute cDNA 1:10 (e.g., 2 µL cDNA + 18 µL water). Store at –80 °C if needed.  
   - qPCR master mix per 20 µL reaction: 10 µL 2× FastSYBR, 1 µL 10 µM forward primer (500 nM final), 1 µL 10 µM reverse primer (500 nM), 6 µL water, 2 µL diluted cDNA.  
   - Run each target (IL‑2, GAPDH) in technical triplicate with the following cycling: 95 °C 2 min; 45 × (95 °C 15 s, 60 °C 30 s).  
   - Calculate ΔΔCt relative to GAPDH and untreated control.  

10. **Data handling**  
    - Provide CD69 MFI values (mean ± SEM, n = 3 technical replicates) and IL‑2 relative expression (log₂ fold change, mean ± SEM, n = 3).  
    - Flag any conditions where >50 % viability loss occurs (e.g., galectin‑3 or galectin‑8 at 50 µg/mL) – flow data may be unreliable, but qPCR should still be reported.  

Please confirm receipt of reagents, let us know if any items need to be ordered, and send the raw FCS files and qPCR export files when the run is complete. Thank you.
```

label: 

defect_types: 

notes: 

---

## 54. R9AACD8  (elisa)

```
Please execute the following experiment on our astrocyte‑enriched primary cultures and return the quantified data.

**Materials & solutions (use what is stored at –20 °C; thaw immediately before use)**  
- 4 % PFA in DPBS (prepare from 16 % stock; 10 mL per aliquot)  
- Permeabilization solution: 0.1 % Triton X‑100 in DPBS, 50 mL total (prepare fresh before use)  
- Blocking solution: 5 % FBS in DPBS, 50 mL total (prepare fresh before use)  
- Primary antibody: anti‑pRab10 (dilute 1:500 in Blocking solution; 40 µL per well)  
- Secondary antibody: goat anti‑rabbit Alexa Fluor 488 (1:500 in DPBS; 40 µL per well)  
- Phalloidin Alexa Fluor 647 (1:1 000 in DPBS; 40 µL per well)  
- Hoechst 33342 (1:10 000 in DPBS; 100 µL per well)  
- DPBS (use 30 mL per 96‑well plate for washing; 50 mL total per plate)  
- 0.05 % NaN₃ in DPBS for storage  

**Equipment**  
- Black‑walled, clear‑bottom 96‑well Greiner μClear plates (use only inner wells)  
- Operetta CLS with 40× water‑immersion objective (NA 1.1)  
- Harmony software for image analysis  

---

### 1. Cell seeding & treatment (2 days before imaging)  

1. When the astrocyte cultures in the flask reach ~80 % confluence, seed 50 000 cells per inner well (avoid outer wells to prevent edge effects). Fill outer wells with DPBS.  
2. After 48 h (cells reach confluence), treat as follows:  

   **MLi‑2 dose‑response**  
   - Prepare serial dilutions of MLi‑2 in DMEM, starting at 1 µM, 1:5 across the plate.  
   - Remove medium, add fresh DMEM containing the appropriate concentration for 90 min at 37 °C.  

   **LLOME experiment**  
   - Remove medium, add fresh DMEM containing either:  
     * MLi‑2 (100 nM) or  
     * LLOME (1 mM) for 2 h, or  
     * LLOME (1 mM) + MLi‑2 (100 nM) for 2 h.  
   - Include a vehicle control (same % DMSO as highest MLi‑2).  

   *Note:* All treatments are performed in a 37 °C incubator.  

---

### 2. Fixation and staining (start 16–18 h after treatment)  

1. **Fix** with 100 µL of 4 % PFA per well, 20 min RT. Dispense gently along the edge; use a multichannel pipette from this step onward.  
2. **Aspirate** PFA, then wash 5× with DPBS (use multichannel pipette to remove first wash; add fresh DPBS, then invert the plate to remove).  
3. Store fixed plates in DPBS + 0.05 % NaN₃ at 4 °C for up to 2 weeks (avoid >2 weeks).  
4. **Permeabilize** with 100 µL permeabilization solution, 20 min RT.  
5. **Block** with 100 µL blocking solution, 1 h RT. Place plates on moist absorbent paper inside a lidded box during steps 4–5.  
6. **Primary antibody**: add 40 µL of diluted pRab10 per well, incubate 12–16 h at 4 °C overnight.  
7. **Wash** 5× DPBS.  

---

### 3. Secondary, phalloidin, and nuclear staining  

1. **Secondary & phalloidin**: add 40 µL of a mix of secondary antibody (1:500) and phalloidin (1:1 000) in DPBS; incubate 1 h RT, protect from light.  
2. **Wash** 5× DPBS.  
3. **Hoechst**: add 100 µL Hoechst (1:10 000), incubate 5 min RT.  
4. **Wash** 3× DPBS (use DPBS + 0.05 % NaN₃).  
5. Store stained plates in DPBS + 0.05 % NaN₃ at 4 °C, protected from light, for up to 3 weeks (imaging ASAP is best).  

---

### 4. Image acquisition (Operetta CLS)  

1. Use 40× water‑immersion objective (NA 1.1).  
2. Capture 29 fields per well, 7 z‑planes per field, 1 µm step (total depth 6 µm).  
3. Channels:  
   - Hoechst (Exc 355–385 nm, Em 430–500 nm)  
   - Alexa 488 (Exc 460–490 nm, Em 500–550 nm)  
   - Alexa 647 (Exc 615–645 nm, Em 655–760 nm)  
4. Set exposure times identically for all plates; do not vary between experiments.  
5. Perform a quick test run to confirm focus, exposure, and z‑stack adequacy before full acquisition.  

---

### 5. Image analysis (Harmony)  

1. **Filter** Alexa 647 channel with Gaussian smoothing (generate “Gaussian Smoothed” channel).  
2. **Find ROI** on the smoothed channel (common threshold 0.5, adjust if needed).  
3. **Calculate morphology & intensity** for ROI; select only cell‑size objects (exclude debris).  
4. **Find nuclei** using Hoechst channel (Method B); thresholds: intensity > 0.40, area > 30 µm².  
5. **Filter EGFP (Alexa 488) channel** with Sliding Parabola (curvature 4) to isolate punctate spots.  
6. **Find spots** (Method B) with common intensity threshold; then use “Find Image Region” to identify individual vesicles.  
7. **Calculate spot properties**: area, roundness, perimeter, width, length, W/L ratio; keep spots with W/L > 0.2.  
8. **Background subtraction**: define outer border –95 % for each spot; compute background‑subtracted intensity.  
9. **Filter vesicles** by intensity & roundness; keep those meeting both criteria.  
10. **Classify by area** into four bins:  
    - < 0.3 µm²  
    - 0.3–0.8 µm²  
    - 0.8–3.5 µm² (pRab10 vesicles)  
    - > 3.5 µm²  
11. **Calculate per‑well metrics**: number of vesicles per bin, mean intensity, total intensity, morphological stats.  
12. Export all results to an Excel file.  

---

### 6. Data analysis (GraphPad Prism)  

1. For the MLi‑2 dose‑response, fit a variable‑slope log(inhibitor) vs. response curve to obtain IC₅₀.  
2. For the LLOME experiment, present normalized vesicle counts per nucleus as grouped bar graphs; use one‑way ANOVA + Tukey post‑test (p < 0.001 considered significant).  

---

**Deliverables**  
- Excel file with per‑well vesicle counts and intensities.  
- Summary statistics (mean ± SEM) for each treatment group.  
- Raw image files (TIFF) for representative fields.  

Please confirm receipt of this request and let us know if any reagents or parameters need clarification. Thank you.
```

label: 

defect_types: 

notes: 

---

## 55. RA48011  (growth_curve)

```
Please run an OD600 assay on our bacterial cultures using the following procedure:

1. Decontaminate the bench and all pipettes: wipe with DNA Away and RNase Away, then wipe again with 70 % ethanol (≈2 min).  

2. Light the Bunsen burner and work within its sterile field for the remainder of the protocol.  

3. Download the attached **OD600_analysis.xlsx** file and record the plate map for this run in the sheet (use duplicate wells for each sample and for blanks).  

4. Using a clear round‑bottom 96‑well plate, add 100 µL of sterile growth media to the two designated BLANK wells (duplicate).  

5. Add 90 µL of the same sterile media to each well that will receive a sample (duplicate per sample).  

6. Mix each bacterial culture gently to resuspend any settled cells. Pipette 10 µL of each culture into its corresponding sample wells (duplicate), creating a 1:10 dilution. After adding the culture, pipette the well up and down five times to mix thoroughly. Set the remaining culture aside for downstream work.  

7. Place the plate in the microplate reader and measure absorbance at 600 nm. Save the raw run data in the same location as the Excel sheet.  

8. Enter the blank and sample OD values into the **OD600_analysis.xlsx** file. The spreadsheet will calculate the corrected OD using:  
   **OD corrected = (OD sample – average OD blanks) × 10**.  

9. Save and file the completed Excel sheet in the designated folder.  

10. Add 10 % bleach to each well of the used plate, let it sit for 30 min, then empty the plate down the drain with water.  

11. Discard the plate in a biohazard waste container.  

12. Perform a second decontamination of the bench and pipettes (DNA Away/RNase Away followed by 70 % ethanol).  

13. Extinguish the Bunsen burner.  

Please let me know if any reagents or consumables are missing. Thanks.
```

label: 

defect_types: 

notes: 

---

## 56. R464169  (qpcr)

```
Please process our provided samples according to the following protocol.

1. Prepare fresh digestion solution on ice using Hank’s Balanced Salt Solution (900 µL), Collagenase P (100 µL at 1 mg/mL), Dispase II (50 µL at 0.5 mg/mL), and DNase I (8 µL at 0.1 mg/mL) per sample, ensuring no freeze-thawing of enzymes. 
2. Prepare FACS and MACS buffers using Ca2+/Mg2+-free PBS (pH 7.2) supplemented with 0.5% Fetal Calf Serum and 2 mM EDTA (0.4 mL of 0.5 M stock per 100 mL), keeping buffers cold and sterilizing the MACS buffer with a 0.22 µm filter.
3. Thaw frozen TOSV-mCherry working stock aliquots rapidly on ice and dilute in sterile 0.75% PBSA. For SGE groups, mix diluted virus 1:1 with SGE (prepared at 1 gland equivalent/µL) to achieve 0.5 gland equivalents/µL in the final inoculum, delivering a target dose (e.g., 10^5 PFU) in a 2 µL injection; dilute virus-only controls 1:1 with 0.75% PBSA.
4. Anesthetize the mice using isoflurane (4–5% induction, 3% maintenance via inhalation), place them in a prone position, and gently extend the left hind limb to expose the upper dorsal foot skin (avoiding the footpad).
5. Load the inoculum into a 5 µL Hamilton syringe fitted with a custom 33G microneedle, insert bevel-up at a 45° angle, and subcutaneously inject 2 µL into the upper foot skin to create a visible bleb.
6. At 72 hours post-infection, cull the mice, disinfect the dorsal foot skin with 70% ethanol, and excise the entire upper foot skin surrounding the inoculation site using consistent anatomical boundaries across all animals.
7. Place each excised skin sample into an individual microcentrifuge tube with 500 µL ice-cold complete DMEM, then transfer into tubes containing the freshly prepared enzymatic digestion solution.
8. Chop the tissue finely with sterile scissors and incubate at 37°C for 50 min with orbital shaking at 1100–1400 rpm. Stop the reaction with 500 µL chilled complete DMEM, pass the suspension through a 70 µm cell strainer, rinse, and centrifuge at 300 × g for 5 min at 4°C.
9. Resuspend skin-derived single-cell suspensions in FACS buffer, block Fc receptors on ice for 5 min, and stain with the appropriate flow cytometry antibody panel (diluted 1:200 for CD45-FITC, CD11b-APC, MERTK-APC-Cy7, Ly-6G-BV421, Ly-6C-PE, MHC-II-APC, CD11c-PE-Cy7, Vimentin-APC, CD31-PE, CD326-APC-Cy7, CD90.2-Pacific Blue, Podoplanin-AF647, CD140a-PE-Cy7, and Ly-6A/E-PE) for 45 min at 4°C in the dark.
10. Wash cells twice in PBS, stain with Ultraviolet Live/Dead fixable viability dye (1:50) for 10 min at 20–25°C in the dark, wash twice with FACS buffer, fix in 4% paraformaldehyde for 30 min, and store at 4°C in the dark prior to flow cytometric acquisition of mCherry-positive infected cells alongside unstained, FMO, and single-stained controls.
11. If performing optional fibroblast enrichment, resuspend single-cell suspensions in MACS buffer, apply the Non-Tumor-Associated Fibroblast Depletion Cocktail, run over an LD magnetic column to collect the flow-through, label with CD90.2 MicroBeads, run over an MS column, and elute the CD90.2+ fibroblasts.
12. For RNA extraction from whole skin or cell suspensions, lyse cell pellets in β-mercaptoethanol-supplemented lysis buffer and homogenize, or homogenize whole skin tissue in 1 mL TRIzol with two 7 mm stainless-steel beads using a TissueLyser (50 Hz, 10 min), followed by column-based purification (incorporating on-column DNase digestion for RT-qPCR or RNA-seq) and spectrophotometric quantification.
```

label: 

defect_types: 

notes: 

---

## 57. R9B4D2F  (viability)

```
Please run a cell viability assay on our samples using an in-house prepared resazurin solution rather than commercial alamarBlue. 

1. Prepare the 1000X stock (44 mM) by dissolving 5 grams of resazurin sodium salt (Sigma-Aldrich, Cat #R7017) in 500 mL of our provided PBS. Mix vigorously until completely dissolved, sterile filter the solution, divide into ten 50 mL aliquots, and store at -20°C protected from light using aluminum foil or a cardboard box. One 1000X stock aliquot may be kept at 4°C for convenience if assays will be run frequently.
2. Prepare the 10X working solution (440 uM) by adding 500 uL of the 1000X stock to 50 mL of PBS in a falcon tube. Wrap the tube in aluminum foil to protect it from light and store at 4°C.
3. Ensure cell seeding densities fall between 1,000 and 300,000 cells per well, keeping total culture volume at or below 200 uL per well. Include at least 4 technical replicates per condition and include blank media controls. Avoid placing any single experimental condition exclusively in the outermost wells of the plate.
4. Exactly 24 hours before the assay endpoint, add the 10X dye to each well using a multichannel pipettor and reagent cuvette (e.g., add 20 uL of 10X solution to 200 uL of culture). Return the plate to culture for 24 hours.
5. Limit light and temperature exposure by not leaving the plate out for more than 10 minutes before measurement. 
6. Using a plate reader (BIO-RAD, Cat #1681130), measure the absorbance of each well at 570 nm and 595 nm. 
7. Calculate final values by subtracting the 595 nm reading from the 570 nm reading for each well, and optionally subtract the blank media measurement from the treatment measurements. Report the final calculated values, which are proportional to the number of viable cells per well.
```

label: 

defect_types: 

notes: 

---

## 58. R254856  (growth_curve)

```
Please process our provided cell and tissue samples according to the following experimental plan:

1. Cell Culture and Treatments
- Culture human glioblastoma cell lines U87 and U251, and murine glioma cell line C6, in DMEM medium with 10% FBS and 1% antibiotic-antimycotic. Culture T47D and HCC70 breast cancer cells in RPMI medium with 10% FBS and 1% antibiotic-antimycotic. 
- Maintain all cells at 37 °C with 5% CO2.
- Treat the cells with MF/RU486 (Sigma, M8046) or UPA using 0.01% DMSO as the vehicle.

2. Western Blotting
- Prepare protein extracts from the provided cell and tissue samples. Run cell samples on 12% SDS-PAGE gels and tissue samples on 7.5% gels at 100 V, then transfer to nitrocellulose membranes and block with 5% BSA.
- Probe membranes with anti-PR primary antibody (Abcam, ab63605) followed by an HRP-conjugated anti-rabbit secondary antibody. 
- Strip the membranes with acid glycine, reprove with anti-α-tubulin antibody (Santa Cruz Biotechnologies, sc-398103), and incubate with HRP-conjugated goat anti-mouse secondary antibody (Abcam, ab6789).
- Detect chemiluminescence signals and normalize PR content to α-tubulin using ImageJ.

3. Immunofluorescence
- Plate cells on glass slides at 8,000 cells per well, fix with 4% paraformaldehyde, permeabilize with methanol, and block with 1% BSA.
- Incubate samples with anti-PR antibody (Santa Cruz Biotechnology, sc-166169) and anti-GFAP (Abcam, ab68428).
- Rinse with PBS, then incubate with anti-mouse Alexa-Fluor-594 and anti-rabbit Alexa-Fluor-488 secondary antibodies (Invitrogen) alongside a Hoechst counterstain. 
- Image the samples on an Olympus Bx43F microscope and process the merged images using ImageJ, including negative controls omitting the primary antibody.

4. Metabolite Extraction and LC/MS Analysis
- Using 10 × 10^6 U87 and U251 cells, remove the culture media and lyse the cells by sonication (Ultrasonic Processor Model GEX130) in an ice bath using 10 kHz, 10 s pulses for 1.5 min.
- Extract progesterone (P4) and 5α-reduced metabolites (5α-DHP) and identify them using Liquid Chromatography/Mass Spectrometry (LC/MS) with a dynamic multiple reaction monitoring (MRM) method, referencing standard curves generated with P4 (Sigma, P8783) and 5α-DHP (MP Biomedicals, 195886).

5. Viability and Sphere Formation Assays
- For the MTT viability assay, seed U87, U251, and C6 cells at 1,500 cells per well in 96-well plates. After 24 h, treat with MF or UPA in 0.01% DMSO across various concentrations (1–125 µM). After 72 h, add MTT solution (Sigma, M5655; 5 mg/mL) for 3 h at 37 °C, dissolve the resulting crystals in 200 µL DMSO, and record absorbance at 570 nm and 630 nm to determine IC50 and IC20 values.
- For the sphere formation assay, culture U251 and C6 cells in ultra-low-attachment 96-well plates at 1 cell/µl in serum-free neural stem cell medium supplemented with B27, rhEGF, bFGF, and antibiotics. Treat cells with 40 µM MF or vehicle upon seeding and every 24 h for three consecutive days. On day 10, determine sphere count and size distributions at 4× magnification using a Neubauer chamber to calculate Sphere Formation Efficiency (SFE).
```

label: 

defect_types: 

notes: 

---

## 59. R0637D3  (growth_curve)

```
Please run an OD 600 to CFU calibration assay on our overnight cultures, which include two biological replicates each of our positive control (BBa_I20270) and negative control (BBa_R0040) strains. Please use LB broth supplemented with 25 mg/mL chloramphenicol for all media and dilutions. 

First, measure the OD 600 of the overnight cultures, diluting into the linear range of the plate reader using black 96-well plates with clear flat bottoms (25 µL culture into 175 µL media per well). Using these readings, prepare 1 mL of starting sample at an OD 600 of 0.1 in triplicate for each of the 4 cultures, yielding 12 starting samples total. Be sure to subtract the blank and account for the initial dilution factor when calculating the required volume. Verify the final OD 600 of these starting samples in the plate reader.

Next, perform a serial dilution for each of the 12 starting samples using the following setup:
1. Prepare three 2.0 mL tubes with 1900 µL of media for Dilutions 1, 2, and 3.
2. Prepare two 1.5 mL tubes with 900 µL of media for Dilutions 4 and 5.
3. Transfer 100 µL from the starting culture into Dilution 1, avoid pipetting up and down, and vortex for 5–10 seconds.
4. Sequentially repeat this 1:20 transfer step through Dilutions 2 and 3, and then 1:10 transfers through Dilutions 4 and 5 using fresh tips each time.

For plating, use LB agar plates containing chloramphenicol. Aseptically spread 100 µL from Dilutions 3, 4, and 5 onto the plates in triplicate (36 plates total). Incubate the plates at 37 °C for 18 to 20 hours. Finally, count the colonies on plates containing fewer than 300 colonies and calculate the CFU/mL for an OD 600 = 0.1 culture by multiplying the colony counts by the appropriate final dilution factors. Please provide the raw plate counts, OD measurements, and final calculated CFU/mL values.
```

label: 

defect_types: 

notes: 

---

## 60. R886FEB  (viability)

```
Please process our supplied recombinant protein samples according to the following workflow:

1. **Buffer Optimization (DLS):**
   - Filter samples through a 0.1 µm membrane and centrifuge at 10,000 × g for 4 min. 
   - Dilute proteins to 0.5 mg/mL in the buffer conditions specified in Table S5 and dispense into a 96-well plate. 
   - Overlay with silicone oil, briefly centrifuge at 500 × g for 1 min to remove air bubbles, and run DLS measurements on a Wyatt DynaPro II Plate Reader at 25 °C over 1 week.
   - For measurements under optimal storage buffer containing 0.05% CHAPS, monitor samples at 25 °C or 37 °C for 72 h. Analyze data using Dynamics software.

2. **Uptake Studies & Cytotoxicity:**
   - Prior to cellular assays, perform an MTT assay to evaluate cytotoxicity and determine appropriate working concentrations (standard starting range: 0.5 µM to 5 µM; 8–15 µM for short motif constructs).
   - Perform live-cell fluorescence microscopy, imaging flow cytometry (IFC), and ImageXpress Pico uptake experiments using murine NIH3T3 fibroblasts (or HeLa/HEK293T cells as applicable).
   - Standard incubation: 1 h. Include a heparin wash post-incubation to remove membrane-adhering, non-internalized protein.
   - For endosomal involvement studies, coincubate with chloroquine (0.1 mM) or sucrose (80 mM). For trafficking mode studies, preincubate with amiloride, indomethacin, or chlorpromazine (0.5 mM each).

3. **Imaging Flow Cytometry (IFC):**
   - Detach adherent cells using 0.05% (v/v) trypsin (avoid prolonged exposure). Stain nuclei with Hoechst.
   - Acquire data immediately on an ImageStreamX Mark II imaging flow cytometer using 405 nm (Hoechst) and 488 nm (GFP) lasers alongside bright-field.
   - Analyze using IDEAS v6.2 and INSPIRE v201.1.0.693 software. Gate singlets using Gradient RMS_BF, AREA_BF, and Aspect ratio_BF parameters (collect 5,000 events per sample in biological triplicates). Quantify colocalization using the Bright Detail Similarity R3_MC_Ch02_Ch07_Median metric. Perform statistical analysis via ordinary one-way ANOVA with multiple comparisons in GraphPad Prism.

4. **ImageXpress Pico Analysis:**
   - Prepare samples following the live-cell imaging protocol with adjusted cell density and higher Hoechst concentration. 
   - Quantify nuclear GFP/Hoechst double-positive signals and total nuclei using CellReporterXpress software.

5. **Motif Mapping & Deletion Mutants:**
   - Scan primary sequences using CPPSite 2.0 to identify candidate CPP motifs, clone them as eGFP fusion constructs, and evaluate cellular internalization via live-cell imaging.
   - Purify generated SPΔCPP deletion mutants and assess uptake via microscopy/IFC to confirm motif functionality.

6. **Coimmunoprecipitation (CoIP):**
   - Incubate NIH3T3 cells with recombinant proteins, isolate the nuclear fraction (verifying separation using histone and β-tubulin markers), and capture complexes via Strep-beads.
   - Run samples on an acrylamide gel, transfer, and blot with anti-GFP and anti-HDAC3 antibodies (alongside markers for other interactors) to confirm CPP-FP/SP binding activity. Include a control of untreated nuclear isolates spiked with recombinant protein.
```

label: 

defect_types: 

notes: 

---

