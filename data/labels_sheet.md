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

## 2. R795DD2  (growth_curve)

```
Run a liquid growth assay for each of our Aspergillus isolates in a 96‑well plate to generate growth curves that will later be analysed with the BEAST package.

**Experimental design**

1. **Samples and replicates**  
   • We have 5 isolates.  
   • For each isolate prepare 3 technical replicates.  
   • Use a fresh 96‑well plate for each isolate.  
   • Plate layout:  
     - Replicate 1 in wells A1–H12,  
     - Replicate 2 in the same positions on the next plate,  
     - Replicate 3 on the third plate.  
   • Keep the well positions identical across replicates (A5 must stay A5, B2 stays B2, etc.).

2. **Media and inoculum**  
   • Use liquid minimal medium (MM) supplemented with 1 % glucose.  
   • Prepare a spore suspension at 1 × 10⁶ spores mL⁻¹ in sterile PBS.  
   • Add 200 µL of inoculum + 800 µL of MM to each well to give 1 mL total volume (final spore concentration 1 × 10⁵ spores mL⁻¹).

3. **Incubation**  
   • Incubate plates at 37 °C with shaking at 120 rpm.  
   • Measure optical density at 600 nm (OD₆₀₀) at 6‑hour intervals from 0 to 30 h (i.e., 0, 6, 12, 18, 24, 30 h).  
   • Record OD values immediately after reading; do not disturb the plate during measurement.

4. **Data recording**  
   • For each well record the OD₆₀₀ value at each time point.  
   • Export the data as a plain‑text file (tab‑delimited) with the following structure:  

     ```
     Time    Well    OD600
     0       A1      0.015
     0       A2      0.016
     …
     6       A1      0.102
     …
     ```

   • Name the files exactly as:  
     - plate1-Rep1.txt  
     - plate1-Rep2.txt  
     - plate1-Rep3.txt  
     - plate2-Rep1.txt  
     - plate2-Rep2.txt  
     - plate2-Rep3.txt  
     - plate3-Rep1.txt  
     - plate3-Rep2.txt  
     - plate3-Rep3.txt  
     - plate4-Rep1.txt  
     - plate4-Rep2.txt  
     - plate4-Rep3.txt  
     - plate5-Rep1.txt  
     - plate5-Rep2.txt  
     - plate5-Rep3.txt

   • Ensure that the well names (e.g., “A1”, “B2”) and the order of columns match exactly across all files.

5. **Deliverables**  
   • Provide the 15 text files listed above in a single ZIP archive.  
   • Include a short README stating the incubation temperature, shaking speed, and measurement schedule.  
   • If possible, provide a copy of the R script that reads these files and produces the `myDataList` object (the script is supplied in the attached PDF).  
   • Also provide a single PDF showing all growth curves plotted together (use the `plot(beastRun)` command as described; name the file `beast_plot_fungal_data.pdf`).

Once you have completed the incubations and collected the OD measurements, please send the ZIP archive to our email address. This will allow us to perform the BEAST analysis as outlined in the protocol.
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

## 7. R166B69  (elisa)

```
We need you to generate bone‑marrow‑derived macrophages (BMDMs) from C57BL/6J mice and run the following panels on the cells we will provide:

1. **BMDM differentiation (5 days)**
   - Harvest femurs/tibias, flush marrow into ice‑cold complete DMEM (DMEM + 10 % FBS + 1 % Pen/Strep).  
   - Lyse red cells with ACK buffer (2–5 min, RT), wash with PBS, filter through a 40 µm strainer.  
   - Resuspend in complete DMEM, add M‑CSF to a final 20–40 ng/mL, and seed 25–35 × 10⁶ cells per 15 cm dish in 20 mL.  
   - Incubate 37 °C, 5 % CO₂ for 5 days.  
   - On day 5 detach with cold detachment buffer (PBS + 10 % FBS + 4 mL 0.2 M EDTA per 500 mL), incubate 4 °C 20 min, collect, count, and re‑plate at the densities listed below (rest 16–18 h in complete DMEM without M‑CSF before any stimulation):
     * 24‑well: 5 × 10⁵ cells in 500 µL  
     * 12‑well: 1 × 10⁶ cells in 1 mL  
     * 6‑well: 2 × 10⁶ cells in 2 mL  

2. **Surface/endosomal TLR stimulation (bacterial/fungal mimics)**
   - Prepare fresh working solutions in complete DMEM: LPS 100 ng/mL, LTA 1 µg/mL, Pam3CSK4 100 ng/mL, Zymosan 10 µg/mL, R848 5 µg/mL, CpG 500 nM.  
   - Aspirate media, add 1 mL (12‑well) or 500 µL (24‑well) of the stimulation mix.  
   - Incubate 8–24 h at 37 °C.  
   - Collect supernatants after 8 h for ELISA (store −20 °C) and cell lysates after 8 h for RNA (350 µL RLT + β‑ME per well, store −20 °C).  
   - For flow‑cytometry readouts, harvest after 24 h.

3. **NOD2 agonist (MDP)**
   - Reconstitute MDP to 5 mg/mL in sterile water, make 20 µL aliquots at −20 °C.  
   - Prepare working concentrations 1–10 µg/mL in complete DMEM (titrate).  
   - Stimulate BMDMs alone or together with sub‑maximal LPS/Pam3CSK4 for 8–24 h.  
   - Collect supernatants for IL‑6, TNF, IL‑1β ELISA and cells for RNA/qPCR as above.

4. **Cytosolic nucleic‑acid/STING activation (viral mimic)**
   - Reconstitute ISD, poly(dG:dC) and 2′3′‑cGAMP to 1 mg/mL (store 20 µL aliquots, −20 °C).  
   - Use final concentrations: ISD 1 µg/mL, poly(dG:dC) 1 µg/mL, 2′3′‑cGAMP 5 µg/mL.  
   - One day before stimulation, let BMDMs rest 16–18 h to reach ~80 % confluence.  
   - Prepare lipid complexes (e.g., Lipofectamine‑type reagent): per 24‑well, 50 µL Opti‑MEM + ligand (0.5 µg ISD or poly(dG:dC); 2.5 µg cGAMP) mixed with 50 µL Opti‑MEM + 1.5 µL transfection reagent. Incubate 15 min at RT, then add to 400 µL fresh complete DMEM (no M‑CSF) for a total of 500 µL.  
   - Include mock (Opti‑MEM only) controls.  
   - Incubate 1–24 h (depending on downstream assay).  
   - Harvest for ELISA (type I IFN), RT‑qPCR (ISGs), and Western blot as needed.

5. **Alternative activation (wound‑healing)**
   - Seed BMDMs as in step 1, rest 16–18 h.  
   - Add IL‑4 10–20 ng/mL (optional IL‑13 10–20 ng/mL) in complete DMEM (no M‑CSF).  
   - Incubate 8–24 h (up to 48 h for functional assays).  
   - Read out Arg1, Retnla, Chil3, Mrc1 by RT‑qPCR and Arg1/CD206/PD‑L1 by flow cytometry.

6. **Apoptotic cell clearance (tolerance)**
   - We will supply thymocytes; induce apoptosis by either 40 Gy irradiation + 6 h culture (RPMI + 1 % BSA) or 1 µM staurosporine 4–6 h. Verify Annexin V⁺/PI⁻ > 80 % by flow.  
   - Co‑culture apoptotic cells with BMDMs at 5:1 or 10:1 ratio in complete DMEM (no M‑CSF).  
   - Incubate 2–4 h for efferocytosis assay (fluorescently labeled targets) and 8–24 h for tolerogenic gene expression.  
   - Measure uptake by flow, expression of Arg1, IL‑10, PD‑L1, MerTK, CD36 (flow) and Il10, Tgfb1, Ahr targets (RT‑qPCR). ELISA for IL‑10 and TGF‑β in supernatants.

7. **Tumor microenvironment mimics**
   - **Tumor‑conditioned media (TCM):** we will provide frozen TCM (20 % final). Add to BMDMs (12‑ or 24‑well) to reach 20 % v/v, incubate 8 h for RNA or 24 h for flow cytometry.  
   - **Tumor cell supernatant (TCS):** we will provide TCS (50 % final). Add to BMDMs to reach 50 % v/v, same incubation times as TCM.  

8. **Readouts**
   - ELISA for cytokines (IL‑6, TNF‑α, IL‑1β, IL‑10, TGF‑β, IFN‑β) from supernatants.  
   - RNA extraction (RLT + β‑ME) and RT‑qPCR for the gene panels listed above.  
   - Flow cytometry panels for surface markers (F4/80, CD11b, MHC‑I, CD40, CD86, Arg1, CD206, PD‑L1, MerTK, CD36) and intracellular cytokines as needed.  
   - Optional Western blot for phospho‑STING/TBK1 and total IRF3 on the nucleic‑acid stimulation samples.  

Please use the reagent stock solutions listed in the original protocol (LPS 10 mg/mL in DPBS, CpG 5 µM, Pam3CSK4 1 mg/mL, Poly I:C 20 mg/mL, LTA 2.5 mg/mL, Zymosan 10 mg/mL, R848 1 mg/mL, ISD 1 mg/mL, poly(dG:dC) 1 mg/mL, MDP 5 mg/mL, 2′3′‑cGAMP 200 µg/mL) and keep aliquots at the temperatures indicated.  

Let us know if any of the reagents need to be ordered or if additional controls are required. We will send the bone‑marrow samples, thymocytes for apoptosis, and frozen TCM/TCS shortly. Thank you.
```

label: 

defect_types: 

notes: 

---

## 8. RB8E5C7  (growth_curve)

```
Please perform vibriocidal assays on our provided serum samples using V. cholerae (O1 Ogawa or Inaba) according to the following protocol:

1. Streak V. cholerae onto a blood agar plate and incubate overnight at 37 °C.
2. Inoculate 10 mL of sterile BHI broth (equilibrated to room temperature for at least 1 hour) with 1-2 colonies from the blood agar plate. 
3. Incubate the culture in an orbital shaker-incubator at 37 °C and 220 rpm for 3 to 4 hours.
4. While the bacteria are growing, heat-inactivate the native complement system in our serum samples by aliquoting 20 µL of each sample into Eppendorf tubes and placing them in a 56 °C water bath for 30 minutes.
5. Prepare a 1:10 initial dilution of the heat-inactivated sera (15 µL serum + 135 µL of 0.9% NaCl saline) to achieve a starting titer of 10, and keep on ice.
6. Thaw an aliquot of guinea pig complement serum (300 µL per plate) at 4 °C.
7. Transfer the grown bacterial culture to a 15 mL centrifuge tube and centrifuge at 3000 rpm for 10 minutes at room temperature (22 °C–25 °C). Discard the supernatant into a 1:10 bleach solution or biohazard waste.
8. Wash the cell pellet twice by resuspending in 10 mL of saline, centrifuging at 3000 rpm for 10 minutes at room temperature, and discarding the supernatant.
9. After the second wash, resuspend the cell pellet in 1 mL of 0.9% NaCl. Transfer 200 µL into a 96-well plate and measure the OD at 600 nm (OD600). Prepare 1 mL of a working bacterial dilution in saline adjusted to an OD600 of approximately 0.3.
10. Prepare the 96-well assay plates as follows:
    - Add 25 µL of saline to all wells in columns 1 through 12, EXCEPT for column 2.
    - Add 50 µL of the 1:10 diluted serum samples to column 2 in duplicate (e.g., Sample 1 in 2A/2B, Sample 2 in 2C/2D, etc.).
    - Add 50 µL of V. cholerae monoclonal antibody in PBS (1 µg/mL) to wells 2G and 2H as assay controls.
11. Using a multichannel pipettor, perform 2-fold serial dilutions starting from column 2 down to column 12 by transferring 25 µL through the columns and discarding 25 µL from column 12. Ensure uniform volumes across wells.
12. Prepare the Growth Indicator solution (per 96-well plate): combine 2.85 mL saline, 150 µL of the diluted bacteria working solution, and 300 µL guinea pig complement serum in a 25 mL reservoir.
13. Add 25 µL of the Growth Indicator solution to wells 1A–1D (Growth Controls) and to all sample dilution wells (columns 2–12). Add 25 µL of saline to wells 1E–1H (Negative Controls). Take care not to cross-contaminate and change tips between columns.
14. Incubate the plate on an orbital shaker-incubator at 37 °C and 50 rpm for 1 hour.
15. Remove the plate from the shaker and add 150 µL of BHI to all wells (including controls), avoiding cross-contamination.
16. Incubate the plate at 37 °C without shaking for 2 hours, then read the OD at 595 nm (OD595). 
17. Check the Growth Control wells; their OD595 must fall between 0.20 and 0.28. If below 0.20, continue incubating and measuring every 30 minutes (up to 4 hours total). 
18. Validate the monoclonal antibody controls: the 50% kill titer must fall within 0.0625–0.03125 (Col 5 or 6) for Ogawa, and 0.125–0.0625 (Col 4 or 5) for Inaba. Reject the plate if controls are out of range.
19. Calculate the 50% kill OD by taking the average OD of the four Growth Controls and dividing by 2. (If ≥2 growth control wells are out of the 0.2–0.28 range, reject the plate; if only one is out, exclude it and average the remaining three).
20. Blank the plate by subtracting the average OD of the 4 negative control wells from all wells (set any negative values to zero).
21. Determine sample titers by taking the reciprocal of the highest dilution factor where the OD595 reading is less than the 50% kill OD. Assign a titer value of 5 for samples that do not reach this threshold (below limit of detection).
22. Check technical replicates: they must agree within one 2-fold dilution. If they differ by more than one dilution, reject the sample; if they differ by one dilution, assign the lower of the two titers.
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

## 10. R4846A8  (viability)

```
We need you to run the full biofilm and RNase‑adjuvant assays on our A. baumannii isolates using the Calgary Biofilm Device (CBD) as described below. Please use the same reagents and concentrations listed, and run all steps in triplicate.

1. **Materials**  
   - A. baumannii strain (CECT 452; ATCC 15308) – use our stock culture.  
   - E. coli BL21 (DE3) transformed with pET11c‑RNase 3/1‑v1 and pET11c‑RNase 3/1‑v3 for protein production.  
   - Recombinant RNases (RNase 3/1‑v1, RNase 3/1‑v3, RNase 1, RNase 3) – we will provide plasmids; you will express and purify as described.  
   - Antibiotics: colistin, tobramycin, moxifloxacin (all from Apollo Scientific).  
   - Moxifloxacin (Acros Organics).  
   - Mueller–Hinton broth (MHB), Terrific Broth (TB), resazurin (16 µg mL⁻¹ final), crystal violet (0.1 % w/v), 33 % acetic acid, IPTG (1 mM), ampicillin (400 µg mL⁻¹), lysozyme (40 µg mL⁻¹), Triton X‑100 (1 %), urea (1 M), guanidine‑HCl (6 M), L‑glutathione (80 mM), oxidized glutathione (2 mM), L‑arginine‑HCl (0.5 M), sodium acetate (150 mM, pH 5).  
   - Buffers: Tris‑HCl 10 mM pH 8.5, Tris‑HCl 100 mM pH 8.5, HBS (10 mM HEPES, 150 mM NaCl, pH 7.4).  
   - CBD (Innovotech), polypropylene 96‑well plates, PBS, LB agar, Spark® plate reader (Tecan).  

2. **Biofilm formation**  
   - Grow an overnight culture of A. baumannii in MHB.  
   - Dilute to OD₆₀₀ = 0.02 in fresh MHB.  
   - Add 150 µL of the diluted culture to each well of a polypropylene 96‑well plate; fill outer wells with 150 µL PBS to prevent evaporation.  
   - Place the CBD lid so that the pegs are immersed, incubate 37 °C, 100 rpm shaking for 24 h to obtain mature biofilms.  

3. **Resazurin viability assay**  
   - After any treatment, rinse pegs three times with PBS.  
   - Transfer pegs to a fresh 96‑well plate containing 200 µL MHB + 16 µg mL⁻¹ resazurin.  
   - Incubate 37 °C, orbital shaking, and read fluorescence (exc 530 nm, em 590 nm) every 10 min for 12 h on the Spark®.  
   - Determine the time to reach half‑maximal fluorescence (t½).  
   - To generate a standard curve, prepare five‑fold serial dilutions of an overnight planktonic culture in the same resazurin‑MHB, run the kinetic fluorescence assay, and plate each dilution on LB agar for CFU counts. Use the curve to convert t½ values from biofilm samples into an equivalent CFU estimate.  

4. **Crystal violet (CV) biomass assay**  
   - Following treatment, rinse pegs three times with PBS and move them to a dry 96‑well plate.  
   - Fix at 60 °C for 1 h.  
   - Stain with 200 µL 0.1 % CV for 15 min, rinse three times with PBS, dry at 37 °C for 30 min.  
   - Elute CV with 200 µL 33 % acetic acid and read absorbance at 595 nm on the Spark®.  

5. **Recombinant RNase expression & purification**  
   - Transform BL21(DE3) with each pET11c construct, select on ampicillin (400 µg mL⁻¹).  
   - Grow in TB + ampicillin at 37 °C, 250 rpm to OD₆₀₀ = 0.6.  
   - Induce with 1 mM IPTG for 4 h, harvest cells by centrifugation.  
   - Resuspend pellet in 10 mM Tris‑HCl pH 8.5, 2 mM EDTA, add lysozyme (40 µg mL⁻¹), incubate 30 min, sonicate, centrifuge 22,000 g.  
   - Wash pellet repeatedly with buffer containing 1 % Triton X‑100 and 1 M urea until supernatant is clear.  
   - Remove Triton X‑100 with Tris‑HCl pH 8.5, 2 mM EDTA washes.  
   - Solubilize inclusion bodies in 100 mM Tris‑HCl pH 8.5, 2 mM EDTA, 6 M guanidine‑HCl overnight with stirring.  
   - Reduce with 80 mM GSH for 2 h under nitrogen, centrifuge, and slowly add the supernatant to 2 L refolding buffer (100 mM Tris‑HCl pH 8.5, 0.5 M guanidine‑HCl, 0.5 M L‑arginine, 2 mM GSSG; GSH/GSSG = 4). Stir 48–72 h at 4 °C.  
   - Buffer‑exchange into 150 mM sodium acetate pH 5, load onto a cation‑exchange (Resource S) column, elute with a linear NaCl gradient 0–2 M.  
   - Desalt, lyophilize, and store lyophilized RNase at –20 °C.  

6. **RNase antibiofilm activity**  
   - Prepare two‑fold serial dilutions of each RNase in HBS covering 200 µM down to 0.01 µM (final volume 200 µL per well).  
   - Alternatively, use a fixed 50 µM concentration for all RNases.  
   - Transfer rinsed pegs to RNase solutions, incubate 37 °C, 100 rpm shaking for 4 h.  
   - Assess viability with the resazurin assay as in step 3.  
   - Plate 30 µL of each supernatant on LB agar to enumerate planktonic cells released from the biofilm.  

7. **Colistin‑RNase adjuvant assay**  
   - Dilute colistin in MHB to 1–12 µM (final concentrations).  
   - Prepare RNase 3/1‑v3 at 10 µM in 0.01 % acetic acid; add 20 µL to each 180 µL colistin well to obtain 1 µM RNase final concentration.  
   - Transfer rinsed pegs to the colistin + RNase mixtures, incubate 37 °C, 100 rpm for 12 h.  
   - Measure viability with the resazurin assay.  

8. **Biofilm resistance evolution (colistin exposure)**  
   - Start with mature 24 h biofilms on pegs.  
   - Prepare treatment wells: 180 µL MHB + colistin (initial 6 µM) + 20 µL 10 µM RNase 3/1‑v3 (final 1 µM RNase). Include controls: (a) MHB only, (b) MHB + 0.01 % acetic acid (no RNase).  
   - Transfer pegs to treatment wells, incubate 37 °C, 100 rpm for 12 h.  
   - Every 12 h, monitor viability with the resazurin assay and record OD₆₀₀ of the treatment well (planktonic release).  
   - After each 12 h cycle, rinse pegs, transfer to fresh treatment plates (same or increased colistin concentration depending on viability). Continue daily cycles for up to 9 days.  
   - At the end of each day, collect the bottom plate, add 15 % glycerol, and store at –80 °C for later strain isolation.  

9. **MIC and MBEC determination for evolved lineages**  
   - Thaw stored cultures from days 3, 5, 7, 9, grow them 24 h at 37 °C, 100 rpm to stationary phase.  
   - **MIC**: In polypropylene 96‑well plates, prepare colistin two‑fold dilutions in MHB (50 → 0.78 µM for low‑resistance strains; 1600 → 12.5 µM for highly resistant). Add 2 µL of a 1:150 diluted overnight culture (≈2 × 10⁷ CFU mL⁻¹) to each well. Incubate 24 h, 37 °C, 100 rpm, read growth visually. Perform each strain in triplicate.  
   - **MBEC** (only day 5 lineages): Grow fresh biofilms on CBD pegs for 24 h in MHB. Transfer pegs to colistin dilutions (1597.44 → 1.56 µM) for 24 h, 37 °C, 100 rpm. Rinse pegs, then transfer to fresh MHB + 16 µg mL⁻¹ resazurin; incubate another 24 h and assess fluorescence/visual survival.  

10. **Data analysis**  
    - Perform all assays in at least three independent replicates.  
    - Use the fluorescence‑time‑to‑half‑max data to calculate CFU equivalents via the standard curve.  
    - For dose‑response curves (antibiotic or RNase), fit non‑linear regression to obtain ED₅₀ values.  
    - Compare MIC, MBEC, and biofilm viability between groups with Mann‑Whitney U tests (non‑parametric).  
    - Correlate MIC/MBEC with biomass (CV absorbance) using Spearman’s rho.  
    - Report p < 0.05 as significant; analyses can be done in GraphPad Prism 8.  

Please let us know if any reagents are unavailable or if you need clarification on any step. Thank you.
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

## 12. R2F63E6  (qpcr)

```
Please run the CDI/R‑CDI mouse experiment on our sample set following these steps.

1. **Antibiotic mix (days –6 to –4)**  
   - Dissolve the following in sterile 0.9 % NaCl and filter‑sterilize (0.22 µm):  
     * Kanamycin sulfate 8 mg/mL (40 mg kg⁻¹)  
     * Gentamycin sulfate 0.7 mg/mL (3.5 mg kg⁻¹)  
     * Colistin sulfate 0.84 mg/mL (4.2 mg kg⁻¹)  
     * Metronidazole 4.3 mg/mL (21.5 mg kg⁻¹)  
     * Vancomycin 0.9 mg/mL (4.5 mg kg⁻¹)  
   - Calculate total volume for the cohort plus 250 µL extra per mouse to cover loss. For example, 4 mice → 1.5 mL.  
   - Administer by oral gavage each day using the volume chart:  
     22 g → 110 µL, 20 g → 100 µL, 18 g → 90 µL, 16 g → 80 µL.  

2. **Clindamycin solution (day –1)**  
   - Prepare 2.0 mg/mL clindamycin in sterile 0.9 % NaCl, filter‑sterilize.  
   - Dose intraperitoneally at 10 mg kg⁻¹ (volume per weight from the same chart).  
   - Change cages after injection.

3. **Vancomycin solution (days 3 to 7)**  
   - Prepare 10.0 mg/mL vancomycin in sterile 0.9 % NaCl, filter‑sterilize.  
   - Dose by oral gavage at 50 mg kg⁻¹ in 250 µL per mouse, using the weight chart.

4. **PBS**  
   - Make 1 L 10× PBS (80 g NaCl, 2 g KCl, 14.4 g Na₂HPO₄, 2.4 g KH₂PO₄, adjust to pH 7.4).  
   - Dilute 1 :10 to 1× PBS. Store at 24 °C; use within 12 months.

5. **CCFA/TCCFA plates (90 plates each)**  
   - For 1.8 L media:  
     * 10 % sodium taurocholate 18 mL (TCCFA only)  
     * 100 mg mL⁻¹ cycloserine 4.5 mL  
     * 16 mg mL⁻¹ cefoxitin 1.8 mL  
     * 5× salts 360 mL (prepare 5× as described)  
     * 30 % fructose 36 mL  
     * 40 g proteose peptone‑agar 1400 mL (5.14 % w/v proteose peptone, 1.54 % agar)  
   - Mix at 50 °C, pour 20–25 mL per plate, and store at 4 °C for ≤2 weeks.

6. **Proteose peptone agar**  
   - Dissolve 72 g proteose peptone in 1 L water, bring to 1.4 L, add 21.6 g agar. Autoclave 40 min, keep in 50 °C bath until use.

7. **Cycloserine & Cefoxitin**  
   - Cycloserine: 1 g in 10 mL water → 100 mg mL⁻¹, filter‑sterilize.  
   - Cefoxitin: 160 mg in 10 mL water → 16 mg mL⁻¹, filter‑sterilize.  
   - Store 4 °C ≤2 days or –20 °C ≤1 month.

8. **Spore challenge (day 0)**  
   - Prepare 10⁶ CFU mL⁻¹ C. difficile spore suspension.  
   - Give 100 µL orally (dose per weight as above).  
   - Collect fresh stool in a sterile 1.5 mL tube, bleach tube, weigh to get stool mass.

9. **Daily monitoring (days 1–2, 3–7, 8–15)**  
   - Weigh each mouse, record clinical score (see table).  
   - Collect stool (same procedure).  
   - For days 3–7 also administer vancomycin and change cages.  
   - Store one CCFA and one TCCFA plate per mouse in anaerobic chamber for next day use.

10. **Fecal sample processing**  
    - In anaerobic chamber, add 500 µL pre‑reduced sterile PBS to stool, incubate 30 min, shake.  
    - For vegetative cells: spread 100 µL on lower half of CCFA plate; for spore load: add 90 µL ethanol (1:1), incubate 30 min, spread 100 µL on TCCFA.  
    - Perform 1:10 serial dilutions (four steps) in a 96‑well plate; plate 3 µL of each dilution (and undiluted) in triplicate on CCFA/TCCFA.  
    - Incubate all plates 48 h at 37 °C anaerobically.

11. **Counting and calculation**  
    - Count colonies day 2; calculate CFU g⁻¹ stool:  
      * CCFA: CFU g⁻¹ = (CFU mL⁻¹ × PBS volume mL) × 1000 / stool mg.  
      * TCCFA: multiply by 2 to account for ethanol dilution.  

12. **Ribotyping (days 0, 3, 11)**  
    - Pick colonies from CCFA, inoculate in BHIS broth, 16 h anaerobically.  
    - Extract DNA, run PCR with primers: 16S forward “GTGCGGCTGGATCACCTCCT”, 23S reverse “CCCTGCACCCTTAATAACTTGACC”.  
    - Thermocycler: 95 °C 5 min; 35 × (95 °C 1 min, 53 °C 1 min, 68 °C 1 min); 68 °C 7 min.  
    - Run on 5 % non‑denaturing polyacrylamide gel, visualize.  
    - Document ribotype for each sample.

13. **Safety & handling**  
    - All animal work in a Class II biosafety cabinet; handler changes gloves after each mouse.  
    - Prepare PBS and ethanol in anaerobic chamber at least 16 h before use.  
    - Place CCFA/TCCFA plates in the chamber one day prior to sampling.  
    - Use sentinel mice (antibiotic‑treated, uninfected) placed alternately among cages to monitor cross‑contamination.  

Deliver all prepared solutions and plates to the animal facility. The experiment should run for 21 days, with daily data entry of weight, clinical score, and CFU counts. Let us know if any clarification or additional reagents are needed.
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

## 15. R2A62FD  (growth_curve)

```
Please run the following calibration experiment on our samples:

1. Use a black 96‑well plate with a clear flat bottom.  
2. Add 100 µL of LUDOX CL‑X (45 % colloidal silica) into wells A1, B1, C1, and D1.  
3. Add 100 µL of sterile ddH₂O into wells A2, B2, C2, and D2.  
4. Measure the absorbance at 600 nm for every well in the same measurement mode you will use for our cell OD readings. (If your plate reader has an automatic path‑length correction, turn it off to avoid distortion of highly scattering samples.)  
5. Record all absorbance values in the table below or in your notebook.  
6. After the run, please send the raw absorbance data back to us.  
7. We will use the attached “iGEM 2019 Plate Reader LUDOX Calibration.xlsx” spreadsheet to compute the conversion factor:  
   - Subtract the water reading from each LUDOX reading to get corrected Abs600.  
   - Divide the spectrophotometer’s reference OD600 value (provided in the Excel sheet) by the corrected Abs600.  
   - Multiply any future plate‑reader OD600 readings by this factor to obtain true OD600.  
8. Once completed, let us know the conversion factor you derived and confirm that the raw data have been sent.
```

label: 

defect_types: 

notes: 

---

## 16. R86F2F3  (elisa)

```
Use the following protocol for each wolf hair sample (35 mg powder):

1. **Materials & reagents**  
   - LC‑MS‑grade water, methanol, isopropanol, acetic acid, formic acid (VWR).  
   - Isotopically labeled internal standards: CORT‑D4 and CORN‑D8 (15 ng mL⁻¹ in methanol).  
   - Hormone standards: CORT and CORN (Merck).  
   - Strata‑X SPE cartridges, 30 mg sorbent, 8B‑S100‑TAK (Phenomenex).  
   - 1 mL methanol for extraction, 1 mL water for equilibrations.  
   - ELISA kit: Cortisol ELISA Kit (Cayman Chemical, Cat. No. 500360).

2. **Sample pretreatment**  
   a. Shake each hair sample with 5 mL isopropanol for 3 min, discard solution, repeat once with fresh isopropanol.  
   b. Dry overnight at room temperature, then cut into ~2 mm fragments.  
   c. Weigh 35 mg into a Falcon tube.  
   d. Homogenize with five steel balls in a Bioprep‑24R homogenizer (5 × 30 s cycles at 10 °C, cooling).  
   e. Keep homogenized powder on ice until extraction.

3. **Extraction for LC‑MS/MS**  
   a. Add 1 mL methanol containing 15 ng mL⁻¹ of each internal standard.  
   b. Rock on a SSL4 see‑saw at 70 rpm, room temperature, 24 h.  
   c. Centrifuge 10 min at 13 000 rpm.  
   d. Transfer 800 µL supernatant to a new tube.  
   e. Evaporate to dryness in an EZ‑2 Elite evaporator.  
   f. Reconstitute in 1 mL LC‑MS‑grade water, ultrasonicate 2 min.  
   g. Load 1 mL of reconstituted sample onto a conditioned Strata‑X cartridge (condition with 1 mL methanol, equilibrate with 1 mL water).  
   h. Wash cartridge with 1 mL water, elute with 1 mL methanol.  
   i. Concentrate eluate to 200 µL, transfer to a glass vial.  
   j. Perform three replicate injections per sample.

4. **LC‑MS/MS analysis**  
   a. System: Agilent 1290 Infinity UHPLC + Agilent 6460 QQQ with Jet‑Stream ESI.  
   b. Column: BEH C18 1.7 µm, 2.1 × 100 mm (Waters).  
   c. Column temperature 40 °C, flow 0.2 mL min⁻¹.  
   d. Mobile phases: A = 0.1 % formic acid in water, B = methanol.  
   e. Gradient: 0–4 min 20–60 % B, 4–5 min 60 % B, 5–7 min 60–70 % B, 7–9 min 70 % B, 9–11 min 70 % B.  
   f. Injection volume 5 µL, dMRM mode, positive ionization.  
   g. Transitions:  
      – CORN (m/z 361.1 → 163, 121)  fragmentor 160 V, CE 24/36 eV, RT 6.3 min.  
      – CORN‑D8 (m/z 369.1 → 169.1) 160 V, CE 30 eV, RT 6.3 min.  
      – CORT (m/z 363 → 121.2, 97.5) 80 V, CE 26/36 eV, RT 6.8 min.  
      – CORT‑D4 (m/z 367.1 → 121.1) 80 V, CE 26 eV, RT 6.8 min.  
   h. Source: nebulizer 35 psi, drying gas 300 °C 8 L min⁻¹, sheath gas 300 °C 10 L min⁻¹, capillary 4500 V, nozzle 300 V.  
   i. Acquire data in MassHunter Acquisition vB10.1, analyse with MassHunter Quantitative Analysis vB12.1.

5. **Calibration & QC**  
   a. Prepare matrix‑matched calibration standards (pooled low‑CORT/CORN hair) at nine concentrations: 0.144 ng mL⁻¹ (CORT) / 0.087 ng mL⁻¹ (CORN) up to 0.1 µg mL⁻¹.  
   b. Include internal standards at 15 ng mL⁻¹ each.  
   c. Run each calibration point in triplicate.  
   d. Define LOD = 3.3 × σ/slope; LLOQ = 10 × σ/slope.  
   e. QC levels:  
      – LQC ≈ LLOQ (≈0.15 ng mL⁻¹),  
      – MQC 50 ng mL⁻¹,  
      – HQC 80 ng mL⁻¹.  
   f. Evaluate precision (RSD ≤ 15 % MQC/HQC, ≤ 20 % LQC) and accuracy (85–115 % MQC/HQC, 80–120 % LQC).  
   g. Compute extraction recovery (RE) and matrix effect (ME) at each QC level.  
   h. Test autosampler stability (24 h at 25 °C) and freeze‑thaw stability (3 cycles –20 → +25 °C), accept deviations ≤ 10 % (MQC/HQC) or ≤ 15 % (LQC).

6. **ELISA comparison (nine samples)**  
   a. Weigh 35 mg powdered hair into a tube.  
   b. Add 1.8 mL methanol, vortex, incubate overnight on orbital shaker.  
   c. Centrifuge, evaporate supernatant to dryness under N₂ at 37 °C.  
   d. Reconstitute in 400 µL ELISA buffer, vortex.  
   e. Follow Cayman kit instructions: wash with ELx50 washer, incubate on ELMI DTS‑4 shaker, read at 410 nm on Synergy 2 reader.  
   f. Correct absorbance, calculate B/B₀, use calibration curve to obtain pg mL⁻¹, convert to pg mg⁻¹ hair using reconstitution volume and 35 mg hair.

7. **Documentation & Reporting**  
   a. Provide raw chromatograms, calibration curves, QC data, and ELISA absorbance tables.  
   b. Include all instrument settings, transition lists, and validation summary.  
   c. Report CORT and CORN concentrations (pg mg⁻¹ hair) for each sample.  

Please complete the above workflow and send us the quantified results and validation metrics.
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

## 19. R3AABEF  (qpcr)

```
Please perform the following on the A549 cell line we will provide:

1. **Spheroid generation (4 days)**
   - Use ultra‑low‑attachment (ULA) 96‑well plates.  
   - Prepare a single‑cell suspension at ≈ 0.5–1 × 10⁶ cells mL⁻¹ in complete RPMI‑1640 (10 % FBS, 1 % Pen/Strep).  
   - Seed 1 × 10⁴ cells per well by adding 100 µL of medium followed by 100 µL of the cell suspension (final volume 200 µL).  
   - Centrifuge the plate at 500 g for 5 min (no brake) at 20‑25 °C.  
   - Incubate 4 days in a standard 37 °C, 5 % CO₂ incubator.

2. **Initial spheroid imaging**
   - Using a bright‑field microscope with a 4× objective, capture one image per well (96 images total) and save in a single folder (numeric file names).

3. **Migration chamber setup**
   - For **morphometric analysis & RT‑qPCR**: load 12 spheroids into each 24‑well Transwell (PET membrane, 8 µm pores).  
   - For **hypoxia flow cytometry**: load 96 spheroids into a single 6‑well Transwell (same membrane).  
   - Transfer spheroids with a cut 1000 µL tip, keep the insert volume at ≈ 80‑100 µL (24‑well) or ≈ 1 mL (6‑well).  
   - Add 700 µL (24‑well) or 3 mL (6‑well) of complete medium (10 % FBS) to the lower chamber.  
   - Avoid bubbles and spheroid stacking; verify under the microscope.

4. **Migration assay**
   - Incubate the inserts for 64 h under standard culture conditions (hypoxia modulation optional).  

5. **Imaging of non‑migrated spheroids (24‑well only)**
   - At 64 h, bring the plate to a bright‑field microscope with a 2× objective.  
   - Capture four overlapping images covering the entire membrane, stitch them in Fiji (Plugins → Stitching → Grid/Collection stitching → Unknown position), and save as a JPEG.

6. **Collection of non‑migrated fraction**
   - Add 200 µL (24‑well) or 2 mL (6‑well) PBS to the insert.  
   - Gently lift spheroids with a non‑woven polyester swab, collect the suspension into a 15 mL tube (use low‑retention cut tip).  
   - Repeat PBS wash once; then a final 500 µL PBS wash with a cotton swab (discard).  
   - Centrifuge 500 g, 5 min, 20‑25 °C; aspirate supernatant, wash pellet with 2 mL (24‑well) or 4 mL (6‑well) PBS, repeat spin. Keep the pellet on ice.

7. **Processing of migrated fraction**
   - Add 700 µL (24‑well) or 2 mL (6‑well) pre‑warmed 0.25 % trypsin to the lower chamber.  
   - Shake at 37 °C for 10 min (adjust if cells remain attached).  
   - Collect the cell suspension, neutralize with 2 mL (24‑well) or 4 mL (6‑well) complete medium, spin 500 g, 5 min, wash once with PBS, spin again and keep the pellet.

8. **Optional crystal‑violet staining (24‑well)**
   - After non‑migrated collection, wash insert with 200 µL PBS, discard.  
   - Transfer insert to a well containing 700 µL 0.5 % crystal violet (methanol 20 % v/v).  
   - Stain 10 min at RT, wash repeatedly with PBS until clear, air‑dry 48 h in the dark.  
   - Image the stained insert with a 4× objective (3 × 3 grid, 9 images, 10‑20 % overlap) and stitch as in step 5.

9. **RNA extraction & RT‑qPCR (if requested)**
   - Extract total RNA from each pellet (non‑migrated & migrated) using your standard kit.  
   - Measure concentration/quality, synthesize cDNA, and run qPCR for the gene panel we will provide.

10. **Hypoxia detection with pimonidazole (6‑well only)**
    - At the 64 h endpoint, measure the volume of medium in the lower chamber and add pimonidazole stock (20 mM in PBS) to reach 200 µM final (e.g., 30 µL into 3 mL).  
    - Swirl gently, incubate 3 h at 37 °C.  
    - Collect non‑migrated and migrated fractions as in steps 6 and 7.  
    - For the non‑migrated pellet (still in spheroid fragments), dissociate with 300 µL trypsin, 5‑10 min at 37 °C, add 2 mL complete medium, spin, wash with PBS.  
    - Fix both pellets in 2 % paraformaldehyde in PBS for 48 h at 4 °C, then wash with 1 % BSA/PBS.  
    - Stain with anti‑pimonidazole (1:250) in 1 % BSA/0.05 % Triton X‑100, 16 h at 4 °C (include an FMO control).  
    - Wash, then incubate with Alexa‑647 secondary antibody (1:1000) for 1 h at RT in the dark.  
    - Wash and resuspend in 1 % BSA/PBS; acquire data on a flow cytometer equipped with a 638 nm laser (e.g., CytoFLEX S).  

11. **General notes**
    - Use multi‑channel (8‑ or 12‑channel) pipettes for all dispensing steps to minimize cell settling.  
    - All centrifugation steps: 500 g, 5 min, 20‑25 °C, no brake.  
    - Store any unused RNA pellets at ‑80 °C; store stained inserts in a dark, dust‑free box at RT.  
    - Provide us with the raw images, stitched composites, qPCR Ct values, and flow cytometry FCS files.

Please let us know if any reagents or consumables (ULA plates, Transwell inserts, pimonidazole, antibodies) need to be supplied, and confirm the anticipated timeline for completion.
```

label: 

defect_types: 

notes: 

---

## 20. R40A4EF  (elisa)

```
Please run the following assays on our provided serum samples from the clinical trial participants. We have 53 matched pairs of baseline (T0) and post-intervention (T1) samples. All specimens are anonymized and labeled with unique alphanumeric codes.

1. Serum Malondialdehyde (MDA) Assay
- Method: Colorimetric assay using a high-sensitivity kit (e.g., E-BC-K025-S, thiobarbituric acid reactive substances method).
- Measurement: Absorbance read at 532 nm using a calibrated multimode microplate reader.
- Specifications: Run samples in triplicate. Ensure the intra-assay CV remains below 10% (target <4.9%). 

2. Total Superoxide Dismutase (T-SOD) Activity Assay
- Method: Hydroxylamine method using a standardized T-SOD assay kit (e.g., E-BC-K019-S).
- Measurement: Absorbance read at 550 nm.
- Specifications: Run samples in duplicate using internal controls and water blanks. Maintain an intra-assay precision CV below 10% (target <2.8%).

3. Human Telomerase Activity Assay
- Method: Sandwich-ELISA using a standardized commercial human telomerase kit (e.g., E-EL-H0164).
- Measurement: Optical density read spectrophotometrically at 450 nm ± 2 nm.
- Specifications: Run samples in triplicate, ensuring strict adherence to the manufacturer's analytical sensitivity range (0.16–10 ng/mL).

Please return the raw optical density readings, calculated concentrations, and the respective intra-assay CVs for each triplicate/duplicate set, mapped against our sample ID codes.
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

## 24. RE9E26A  (growth_curve)

```
Please perform the following four-part experimental workflow using our provided samples and reagents:

1. Synthesize and characterize the HA-DA conjugate: Dissolve 1 g of 12 kDa HA in 100 mL PBS, activate carboxyl groups with 5 mM EDC and 10 mM NHS at pH 5.0 for 6 h, and conjugate with 10 mM dopamine under a nitrogen atmosphere for 24 h. Purify the product via dialysis against deionized water (14 kDa MWCO, 4 °C, 72 h with buffer changes every 8 h), freeze-dry to yield the spongy solid, and confirm the chemical structure and grafting efficiency using 1H NMR in D2O.

2. Express and purify the HRP-pHLIP fusion protein: Subclone the custom-synthesized HRP-pHLIP gene into the pET28a(+) vector, transform into E. coli BL21 (DE3) cells, and plate on LB agar with 60 µg/mL kanamycin. Grow an overnight starter culture, inoculate 30 mL fresh LB-kanamycin medium, and grow to mid-log phase (OD600 ≈ 0.8) at 37 °C and 200 rpm. Induce expression with 0.5 mM IPTG for 8 h at 16 °C (220 rpm). Harvest cells by centrifugation (8,000 × g, 10 min, 4 °C), resuspend in lysis buffer, and lyse via sonication (30% amplitude, 5 s on/5 s off, 15 min total) in an ice-water bath. Collect the supernatant by centrifugation (12,000 × g, 30 min, 4 °C) and purify the His-tagged protein using Ni-NTA affinity chromatography, washing with wash buffer and eluting with elution buffer. 

3. Culture and transfect HEK 293T cells and run optogenetic assays: Culture HEK 293T cells in high-glucose DMEM with 10% FBS and 1% penicillin/streptomycin. Seed cells in 6-well plates at 5 × 10^5 cells/well to reach 70%–80% confluence. Transfect each well with 2.5 µg total plasmid DNA (pYZ484 and pYH3) and 4 µL Lipo293 reagent in antibiotic-free DMEM. After 24 h, subject the cells to alternating 5 s pulses of 660 nm ("ON") and 730 nm ("OFF") light at 1 mW/cm² using a custom LED array. Replace the medium every 24 h and collect supernatant samples every 6 h over a 72 h period to monitor cytokine/SEAP secretion profiles.

4. Perform single-cell encapsulation: Harvest 1 × 10^6 HEK 293T cells, resuspend in 1 mL PBS (pH 6.5) containing 50 µg/mL purified HRP-pHLIP, and incubate at room temperature for 30 min. Wash the cells three times with PBS (pH 6.5) to remove unbound protein, then resuspend in a hydrogel precursor solution containing 2% (w/v) HA-DA and 2 mM H2O2. Gently stir for 30 min to induce HRP-catalyzed crosslinking. Collect the encapsulated cells by centrifugation (150 × g, 5 min) and wash three times with PBS (pH 7.4).
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

## 27. R1A380F  (elisa)

```
Please run a Luminex-based multiplex assay on our MenACWY-CRM197 vaccine samples using the following protocol. 

First, couple the four serotype-specific mouse monoclonal antibodies to Diasorin Luminex MagPlex-C Microspheres: use region B20 for anti-MenA (batch 28022017), B25 for anti-MenC (batch 13072017), B33 for anti-MenW (batch 04052017), and B77 for anti-MenY (batch 23082017). For each coupling reaction, wash 100 µL (1.25 million beads) in water using a protein low-binding 1.5 mL tube. Activate the beads with 80 µL of 100 mM sodium phosphate (pH 6.2), 10 µL of sNHS (50 mg/mL), and 10 µL of EDC (50 mg/mL). Mix by 360° rotation for 20 min at room temperature in the dark. Conjugate each activated bead set with its respective mAb in 500 µL of 50 mM MES buffer (pH 5.0), mixing by 360° rotation for 2 h at room temperature in the dark. Wash twice with 500 µL of 1X PBS / 0.05% Tween-20. Saturate unreacted groups with 500 µL of 1X PBS / 0.05% Tween-20 / 0.2% BSA by rotating for 30 min at room temperature in the dark. Wash twice more with 500 µL of 1X PBS / 0.05% Tween-20, and store in 1000 µL of the same buffer at a final concentration of 1.25 million beads/mL.

For the assay, reconstitute our lyophilized vaccine samples and standards in 600 µL of 9.0 g/L NaCl solution, then dilute them 1:1000 in 1X PBS / 0.05% Tween-20. Dispense samples and the standard curve in duplicate into the first column of a Greiner plate (cat. 655904), fill the remaining wells with sample diluent, and perform a 2.5-fold serial dilution. Prepare the bead mix by diluting each coupled bead set 1:10 in sample diluent, and add 10 µL of the mix to each well. Incubate the plate for 1 h at room temperature with 800 rpm agitation. Wash the plate three times with sample diluent using a magnetic washer. Add 100 µL of purified rabbit anti-CRM197 primary antiserum (Abcam ab53828, purified via Protein-G spin-trap) to each well and incubate under the same conditions. Wash three times, then add 50 µL of goat anti-rabbit IgG Fc-specific R-Phycoerythrin secondary antibody (Jackson ImmunoResearch 111-117-008, diluted 1:200) to each well. Incubate for 30 min at room temperature with 800 rpm agitation. Wash the wells, resuspend in 100 µL of 1X PBS, agitate, and read on a Bio-Plex 200 instrument (high-sensitivity setting) using Bio-Plex Manager 6.0 software to record median fluorescence intensity. 

Analyze the resulting log10(Dose)-log10(Response) curves via Parallel Line Assay using a four-point minimum linear range. Verify assay validity through ANOVA, ensuring significant regression (p < 0.05), no non-linearity (p > 0.05), and no non-parallelism (p > 0.05) before calculating final sample concentrations and confidence intervals.
```

label: 

defect_types: 

notes: 

---

## 28. R2E398F  (elisa)

```
Please run a quantitative IL‑17A ELISA on the patient serum samples we have supplied, using the following protocol and reagents:

1. Use 96‑well ELISA plates pre‑coated with a monoclonal anti‑human IL‑17 capture antibody (commercially available, same as used in the published method).  
2. Add 100 µL of each serum sample to the appropriate wells (duplicate wells preferred). Include a full set of IL‑17A standards (0, 10, 25, 50, 100, 250 pg/mL) prepared from the recombinant human IL‑17A (Bio Basic, Cat #RC212‑28, 1 mg) to generate a standard curve.  
3. Incubate the plate at room temperature for 1 h 30 min.  
4. Wash the plate 4 × with PBS containing 0.05 % Tween‑20 (PBS‑T).  
5. Add 100 µL of biotin‑conjugated anti‑human IL‑17 detection antibody to each well and incubate 1 h 30 min at room temperature.  
6. Wash the plate again 4 × with PBS‑T.  
7. Add 100 µL per well of peroxidase‑labeled streptavidin (commercial streptavidin‑HRP) and incubate 1 h at room temperature.  
8. Perform a final wash sequence (4 × PBS‑T).  
9. Add 100 µL of TMB substrate solution to each well and allow colour to develop (≈10–15 min) until the highest standard shows a clear blue colour.  
10. Stop the reaction by adding 50 µL of 2 N H₂SO₄ (or other supplied stop solution) to each well.  
11. Measure absorbance at 450 nm (reference wavelength 620 nm if your plate reader allows).  
12. Calculate IL‑17A concentrations in the serum samples from the standard curve (using a 4‑parameter logistic fit).  

Materials we will provide: patient serum aliquots (up to 200 µL each), recombinant IL‑17A standard, 96‑well filter plate with sealers (Merck Millipore, Cat #MX‑PLATE). Please source any additional reagents (biotin‑anti‑IL‑17, streptavidin‑HRP, TMB substrate, stop solution) as needed. Return the raw absorbance data and the calculated concentrations in an Excel file, along with any comments on assay performance (e.g., CVs of duplicates, any out‑of‑range standards). Thank you.
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

## 30. R864767  (growth_curve)

```
1. **Generate primary swine macrophage cultures**  
   - Use heparin‑treated blood from six 5‑6 month old Yorkshire gilts (≈250‑300 lb).  
   - Let blood sit at 37 °C for 1–2 h for RBC sedimentation, then isolate mononuclear cells by Ficoll‑Paque (SG = 1.079).  
   - Plate the monocyte fraction in Primaria flasks with RPMI‑1640 plus 30 % L929 supernatant, 20 % heat‑inactivated‑γ‑irradiated FBS, 1 X antibiotics/antimycotics, 1 X gentamicin, and 30 % autologous plasma. Incubate 24 h at 37 °C, 5 % CO₂.  
   - Detach adherent cells the next day with 10 mM EDTA in DPBS (20 min, 37 °C). Wash twice in RPMI‑1640 + antibiotics/gentamicin, resuspend in FBS, and either (a) seed into Primaria 96‑well plates for use after 24 h, or (b) cryopreserve (see step 2).

2. **Cryopreserve macrophages**  
   - After detachment, wash cells twice (240 × g, 10 min, RT) in RPMI‑1640 + antibiotics/gentamicin.  
   - Resuspend pellet in chilled 7 % DMSO / 93 % heat‑inactivated‑γ‑irradiated FBS at 1 × 10⁷ cells/mL. Aliquot into cryovials, place in Mr. Frosty™ container, freeze at –70 °C for 48 h, then transfer to liquid N₂ for long‑term storage.  
   - For each assay, thaw a vial quickly in a 37 °C water bath, wash twice in complete macrophage medium (RPMI‑1640 + 30 % L929 supernatant + 20 % FBS + antibiotics/gentamicin), count viability with Trypan blue, and seed 5 × 10⁶ cells per 96‑well plate (or 1 × 10⁶ cells per 6‑well plate for growth curves). Allow 24 h before infection.

3. **Prepare red blood cells for hemadsorption (HA) readout**  
   - From the same heparin‑treated blood used for macrophages, collect the RBC layer after the 1–2 h sedimentation step.  
   - Wash RBCs twice (240 × g, 10 min, RT) in DPBS, resuspend at 20 % v/v in DPBS, store at 4 °C (use within 7–14 days).  
   - In parallel, obtain heterologous swine RBCs (different donors) and commercially sourced porcine RBCs (Innovative Research, Inc.) prepared identically for comparison.

4. **Virus stocks**  
   - Use the following ASFV isolates (all propagated only in primary swine macrophages, ≤ 2 passages): Georgia 2007/1, Lisbon‑60, Killean‑III, Kimakia‑64, DR‑2, DR‑21, Haiti‑21, Malawi Lil‑20/1, Pretoria‑4/1.  
   - Prepare working stocks by a single passage in fresh macrophages, aliquot, and store at –70 °C.

5. **Virus titration (HA assay)**  
   - Thaw and seed fresh macrophages and 1‑month‑old cryopreserved macrophages in Primaria 96‑well plates (5 × 10⁶ cells/plate).  
   - Serially dilute each ASFV isolate 10‑fold in complete macrophage medium. Include the 24 EDTA‑treated blood samples (12 Georgia‑infected, 12 Lisbon‑60‑infected) and the 10 naïve pig blood samples as negative controls.  
   - Add 50 µL of each dilution to the corresponding well (in duplicate).  
   - Incubate 24 h at 37 °C, 5 % CO₂, then add 10 µL of the prepared RBC suspension to each well.  
   - Read HA rosettes between 7 and 10 days post‑infection. Calculate HAD₅₀/mL by Reed‑Muench; the detection limit is the lowest dilution showing HA.

6. **Growth‑curve experiment**  
   - Seed fresh macrophages and 1‑month‑old cryopreserved macrophages in Primaria 6‑well plates (1 × 10⁶ cells/well). Incubate 24 h.  
   - Infect each well in triplicate with Georgia 2007/1 or Lisbon‑60 at MOI = 0.01. After 1 h adsorption at 37 °C, remove inoculum, wash twice with complete medium, then add 2 mL fresh medium.  
   - Collect supernatants at 0 h, 1, 2, 5, 7, and 9 days post‑infection, store at –70 °C.  
   - Titrate each time point on fresh macrophages (HA assay) and report HAD₅₀/mL.

7. **Repeatability / reproducibility study**  
   - Use three macrophage sources: (a) fresh cells, (b) cryopreserved cells stored 2 months, (c) cryopreserved cells stored 6 months. Seed each in 96‑well plates (5 × 10⁶ cells/plate).  
   - Prepare ten‑fold serial dilutions of Georgia 2007/1 in triplicate and infect each plate as in the titration assay.  
   - Perform the entire experiment on three consecutive days. Record HA results, calculate HAD₅₀/mL for each day and each cell source, and assess intra‑day and inter‑day variation.

8. **Reporting**  
   - Provide raw HA readouts (positive/negative wells per dilution), calculated titers, and standard deviations across replicates and days.  
   - Summarize viability of fresh vs. cryopreserved macrophages (Trypan blue counts).  
   - Include any observations on RBC source performance (homologous vs. heterologous vs. commercial).  

Please let us know if any reagents (L929 supernatant, specific RBC sources, or virus isolates) need to be shipped from our lab, or if you have any questions about the timing or volume requirements. Thank you.
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

## 32. R4138F8  (growth_curve)

```
Please run liquid growth assays on our provided Aspergillus and filamentous fungi samples using the following protocol. 

First, harvest and dilute the spores in PBS with 0.01% Tween to a concentration of 4 x 10^5 spores/mL. Aliquot 5 uL of this spore stock into each inner well of a non-coated CytoOne 96-well plate (Starlab), yielding an absolute count of 2,000 spores per well. Overlay each well with 195 uL of liquid media to reach a total volume of 200 uL per well. 

To prevent the edge effect, fill all interstitial spaces between the wells with either media or sterile water. Seal the 96-well plate with a breathable cover to permit gas exchange. 

Set a BioTek plate reader or equivalent to 37 °C, take an initial blank reading, and run the assay for 48 hours, measuring OD 600 every 10 minutes. Finally, extract and export the resulting growth curve data in .txt format as attached in the reference files.
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

## 35. R01545D  (viability)

```
Please run an MTT cell viability assay on our provided samples using the following procedure:

1. Prepare each sample in DMSO.
2. Observe the cells on the plate and record their initial condition.
3. Perform a serial dilution of the samples in a U-type plate, mixing by suspending 40 times.
4. Remove the old medium from the cells.
5. Add 100 μl per well of the sample and DMSO control, then incubate for 48 hours at 37 °C.
6. Observe the condition of the cells following the 48-hour incubation.
7. Check for toxicity under a microscope and take photographs if any morphological changes are observed.
8. Prepare a 10% MTT solution.
9. Remove the medium from the 96-well plate.
10. Add 150 μl per well of the 10% MTT solution using a multichannel pipette, and incubate for 4 hours at 37 °C.
11. Remove the MTT solution from the well plate.
12. Add 100 μl per well of 100% DMSO to dissolve the precipitate.
13. Shake the plate for 0.5 minutes, then measure the absorbance at 560 nm and 750 nm.
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

## 37. RC87802  (qpcr)

```
Please grow the tomato seedlings, apply the mechanical wounding, collect the tissue, extract RNA, make cDNA and run SYBR‑Green qPCR exactly as described below. We will provide the seed stocks (all genotypes we need) and the primer sequences for the target genes and ACTIN2.

1. **Seed germination (3 days in the dark)**
   - Use 9 cm culture dishes with sterile germination paper at the bottom.  
   - Surface‑sterilize the seeds: 75 % ethanol, 2 min; then 5 % NaOCl, 10 min with gentle shaking; rinse 6–7 times with sterile distilled water.  
   - Spread the seeds evenly on the paper, add enough distilled water to moisten (seeds should contact water but not be submerged).  
   - Incubate in the dark until the radicle just emerges (≈2‑3 days).

2. **Transplant to pots and grow seedlings**
   - Transfer germinated seeds to 7 cm square plastic pots (or equivalent round pots) filled with a 1:1 (v/v) mix of vermiculite and peat.  
   - Grow under controlled conditions: 16 h light at 26 °C, 8 h dark at 18 °C, 60 % RH, light intensity 180–220 µmol m⁻² s⁻¹.  
   - Water sparingly to avoid excess moisture; no fertilizer is needed.  
   - Grow until the plants reach the “two‑leaf, one‑heart” stage (first true leaf fully expanded, second true leaf just emerging).  
   - For each genotype, have at least 8 seedlings; plant all genotypes together in the same tray to ensure identical conditions.

3. **Mechanical wounding**
   - Sterilize a 14 cm hemostatic forceps with 75 % ethanol and let dry completely.  
   - For each seedling, clamp the lamina of the first true leaf once with consistent pressure to produce visible drooping.  
   - Label each wounded seedling; keep a matched set of untreated seedlings as controls (grown in separate pots but under identical conditions).  
   - After wounding, keep the wounded area facing vertically downward.

4. **Tissue harvest (12 h post‑wounding)**
   - Harvest three sample types per genotype:  
     a) The wounded leaflet of the first true leaf (local tissue).  
     b) The undamaged second true leaf from the same plant (systemic tissue).  
     c) A leaf from an untreated control plant.  
   - Snap‑freeze each leaf in liquid N₂ immediately and store at –80 °C.  
   - Clearly label each tube with genotype, tissue type (control, wounded, systemic), time point (12 h) and a unique ID.  
   - Avoid any freeze‑thaw cycles; RNA extraction must be performed within 3 months.

5. **RNA extraction (column‑based)**
   - Keep all frozen tissue in a pre‑chilled mortar, add liquid N₂ and grind to a fine powder (≤500 µL powder per 1.5 mL tube).  
   - Add 1 mL Trizol to the powder, vortex, let stand at RT 5 min.  
   - Transfer the lysate to the RNA‑binding column in two portions, centrifuge 20 s at 13 500 g, 4 °C; discard flow‑through.  
   - Wash sequentially with 700 µL Buffer RW1 and twice with 500 µL Buffer RW2 (20 s spin each, 4 °C).  
   - Spin the column empty for 2 min to dry, then elute with 30 µL RNase‑free water.  
   - Measure concentration and purity (NanoDrop, A260/280 ≈ 2.0, A260/230 > 2.0) and check integrity on a 1 % agarose gel.  
   - Store RNA at –80 °C.

6. **cDNA synthesis (PrimeScript or equivalent)**
   - In a RNase‑free tube on ice, combine per 1 µg RNA: 2 µL 5× gDNA Eraser Buffer, 2 µL gDNA Eraser, 1 µL RNA, ddH₂O to 10 µL. Incubate 42 °C 2 min, chill on ice.  
   - Add 10 µL RT master mix (4 µL 5× PrimeScript Buffer, 1 µL PrimeScript RT Enzyme Mix I, 1 µL RT Primer Mix, 4 µL RNase‑free water).  
   - Incubate 37 °C 15 min, then 85 °C 5 s.  
   - Dilute or store cDNA at –80 °C.

7. **Quantitative real‑time PCR**
   - Set up 20 µL reactions (Kapa SYBR Fast qPCR kit): 2 µL cDNA, 10 µL 2× SYBR master mix, 0.5 µL 0.25 µM forward primer, 0.5 µL 0.25 µM reverse primer, add RNase‑free water to 20 µL.  
   - Run on a Roche LightCycler 480 with: 95 °C 30 s; 40 cycles of 95 °C 5 s, 59 °C 30 s (adjust annealing temperature if needed for each primer pair).  
   - Perform melt‑curve analysis from 60 °C to 95 °C (0.3 °C s⁻¹) to confirm single‑product amplification.  
   - Include no‑RT and no‑template controls.

8. **Data analysis**
   - Calculate ΔCt using ACTIN2 as the reference gene.  
   - Present relative expression (2^‑ΔΔCt) for each tissue type.  
   - Use a two‑tailed Student’s t‑test for pairwise comparisons (control vs. wounded, control vs. systemic) and one‑way ANOVA with Tukey post‑hoc for multi‑genotype data. Significance thresholds: * p < 0.05, ** p < 0.01, *** p < 0.001.

**Safety notes:**  
- Perform all Trizol and chloroform steps in a fume hood wearing nitrile gloves, goggles and a lab coat.  
- Dispose of organic waste according to institutional hazardous waste procedures.

Please let us know if you need any reagents (Trizol, columns, primers) or clarification on any step. Thank you!
```

label: 

defect_types: 

notes: 

---

## 38. R105C32  (growth_curve)

```
We need you to perform the following experiment with our bacterial isolates. Use the exact reagents, concentrations and sequencing platforms listed below. All steps should be carried out in a biosafety level 2 lab, following our safety guidelines.

1. **Bacterial strains & media**  
   - Bacillus subtilis 168 trpC2, Staphylococcus aureus ATCC 29213, Lactiplantibacillus plantarum ATCC 8014, Enterococcus faecalis ATCC 29212, Clostridioides difficile ATCC 9689, and two C. difficile clinical isolates (one erythromycin‑resistant, one susceptible).  
   - Grow B. subtilis and S. aureus aerobically at 37 °C in LB (Cat# L7275).  
   - Grow L. plantarum aerobically at 37 °C in MRS (Cat# 69966).  
   - Grow E. faecalis anaerobically at 37 °C in NYCIII.  
   - Grow C. difficile strains anaerobically at 37 °C in brain‑heart infusion (BHI).  
   - For the clinical isolates, start from a single colony, grow overnight in BHI, then dilute to OD600 = 0.05.

2. **Antibiotic growth assay**  
   - Dilute overnight cultures to OD600 = 0.005–0.05 for B. subtilis and L. plantarum; to OD600 = 0.05 for C. difficile isolates.  
   - Dispense 100 µL into a 96‑well plate (aerobic plates for the first two species, anaerobic plate for C. difficile).  
   - Add chloramphenicol at 0, 1.6, 8, or 40 µg/mL (for B. subtilis & L. plantarum).  
   - Add erythromycin at 0, 0.1, 0.5, or 2.5 µg/mL (for B. subtilis & L. plantarum).  
   - For the C. difficile isolates, add erythromycin at 0, 1, or 256 µg/mL.  
   - Incubate 18–24 h (aerobic) or 18–24 h (anaerobic).  
   - Read OD600 on a Tecan Spark (for aerobic) or Tecan Sunrise (for anaerobic) at the end of incubation. Record growth curves for analysis.

3. **RNA sample preparation for HT‑5PSeq / s5PSeq**  
   - Grow cultures to mid‑exponential phase (OD600 = 0.6–0.8).  
   - For B. subtilis & L. plantarum, take 1 mL aliquots, treat with the same antibiotic concentrations as in the growth assay for 10 min at 37 °C.  
   - For the C. difficile isolates, treat 1 mL aliquots with erythromycin (0 or 1 µg/mL) for 10 min, then add 500 µL RNAprotect Bacteria Reagent (QIAGEN) and incubate 5 min.  
   - Harvest by centrifugation at 13 000 rpm for 3 min, discard supernatant, freeze pellets on dry ice.

4. **Total RNA extraction**  
   - Resuspend each pellet in 1 mL lysis buffer containing phenol (pH 6.5) and 0.5 mm glass beads.  
   - Disrupt mechanically: 2 min in a MultiMixer or 1 min in a FastPrep.  
   - Separate aqueous phase; perform acidic phenol‑chloroform extraction twice.  
   - Precipitate RNA with ethanol (2 × volume, 1 h at –20 °C), wash with 70 % ethanol, air‑dry, resuspend in nuclease‑free water.  
   - Quantify with Nanodrop and Qubit dsDNA HS kit (Cat# Q33231).  
   - Check integrity by Agilent RNA Pico kit; accept RIN > 8.

5. **s5PSeq library preparation**  
   - Use 200 ng total RNA per sample (no DNase).  
   - **rRNA blocking**: hybridise with 0.4 µM of the 146 universal blocking oligos and 4 µM of two species‑specific oligos (targets 5′ ends of 16S/23S, see Table S1) in 50 mM NaCl.  
     - Heat 75 °C 5 min → 65 °C 5 min → ramp down 3 °C every 2 min until 35 °C.  
   - **Adapter ligation**: add 1 µM single‑stranded RNA adapter containing a 10‑nt UMI and 8‑nt sample barcode; mix with 1 mM ATP, 1× T4 RNA ligase buffer, and 10 U T4 RNA ligase 1. Incubate 25 °C 1 h.  
   - Purify ligated RNA with RNA Clean‑XP beads (1.8× volume).  
   - **First‑strand cDNA**: reverse‑transcribe with SuperScript II (Cat# 100004925) using random hexamers, 50 °C 30 min, 70 °C 15 min.  
   - Degrade RNA: 28.6 mM NaOH, 65 °C 20 min, neutralise with Tris‑HCl (pH 7.5).  
   - Purify cDNA with Ampure XP beads (1.8×).  
   - **PCR amplification**: 0.25 µM Illumina‑compatible primers (dual barcode), 2× Phusion Master Mix (Cat# F‑530L). Cycling: 98 °C 30 s; 15 cycles of 98 °C 20 s, 65 °C 30 s, 72 °C 30 s; final 72 °C 7 min.  
   - Size‑select PCR products with Ampure XP: 0.6×–0.8× to keep 400–600 bp fragments.  
   - Quantify final libraries with Qubit dsDNA HS; dilute to 650 pM.

   - **Mixed‑species library**: combine 100 ng RNA from each of B. subtilis, S. aureus, E. faecalis, and erythromycin‑treated C. difficile (equal mass), then proceed with the same s5PSeq protocol.

6. **Illumina sequencing**  
   - Load 650 pM libraries on NextSeq 2000 (paired‑end 150 bp).  
   - Demultiplex with bcl2fastq (v2.20).  
   - Trim adapters and low‑quality bases with cutadapt 4.8.  
   - Extract UMIs with UMI‑tools 1.0.0.  
   - Align to the appropriate reference genome with STAR 2.7.11a.  
   - Analyse with fivepseq v1.3.5 to generate codon‑resolution coverage and ribosome‑stalling plots.

7. **Nanopore sequencing** (reuse Illumina‑prepared libraries)  
   - Add Oxford Nanopore ligation adapters using SQK‑LSK114 kit.  
   - Load 1 µg library onto a Flongle flow cell (FLO‑FLG114) for 24 h on MinION, and onto a PromethION flow cell (FLO‑PRO114M) for 72 h on PromethION 48.  
   - Base‑call: Dorado (fast model) for Flongle, Guppy (SUP model) for PromethION.  
   - Demultiplex with minibar.py (dual Illumina barcodes).  
   - Extract UMIs (UMI‑tools) and align to the C. difficile reference with minimap2.  
   - For mixed‑species reads, align to a combined reference of B. subtilis, S. aureus, E. faecalis, and C. difficile using minimap2; keep primary alignments with MAPQ ≥ 10. Count reads per species with samtools.

8. **Data analysis & reporting**  
   - Use GraphPad Prism 10 to generate heatmaps, metagene plots, and statistical comparisons (paired two‑tailed t‑tests, Pearson correlation).  
   - Submit raw and processed data to GEO (accession GSE293532).  
   - Provide a concise summary of ribosomal stalling patterns and any AMR signatures observed.

Please confirm receipt of this request, and let us know if you need the specific sequences for the blocking and adapter oligos (Table S1). The entire workflow should be completed within 3 weeks, with sequencing data returned within 48 h of run completion.
```

label: 

defect_types: 

notes: 

---

## 39. RAA335C  (elisa)

```
Please run the following experiments on the samples we will provide:

1. **Hydrogel preparation**  
   - Dissolve 50 mg GelMA powder in 1 mL PBS containing 0.05 g LAP (photoinitiator) under dark conditions, heat and shake until fully dissolved, then filter through a 0.22 µm sterile filter.  
   - For the alogliptin‑loaded gel (Gel‑A), co‑dissolve 50 mg GelMA and 7.5 mg alogliptin in the same 1 mL LAP‑PBS solution (final alogliptin concentration 7.5 mg mL⁻¹). Filter as above.  

2. **Equilibrium water volume**  
   - Pipette 1 mL of each hydrogel (plain GelMA and Gel‑A) into separate UV‑transparent dishes, photocure, weigh immediately, then freeze‑dry for 24 h and weigh again. Perform three replicates per group.  

3. **Scanning electron microscopy**  
   - UV‑cure 1 mL of each hydrogel, place in 6‑well plates, freeze at –80 °C overnight, then lyophilize for 48 h. Cut ~1 mm³ pieces, mount on stubs, sputter‑coat with gold, and image surface morphology, pore size, and architecture.  

4. **Hydrogel release ELISA**  
   - Place 1 mL of each cured hydrogel into 15 mL tubes with 10 mL PBS (pH 7.4), incubate at 37 °C with shaking. At days 15, 17, 20 collect supernatant (centrifuge 6000 rpm, 5 min), store at –80 °C, and replace with fresh PBS. After the final collection, quantify alogliptin concentration by ELISA.  

5. **T2DM rat model**  
   - Obtain 40 male Sprague‑Dawley rats (12–13 weeks, ~300 g). Feed a high‑fat/high‑carbohydrate diet for 4 weeks, then inject STZ 35 mg kg⁻¹ i.p. Verify fasting glucose >16.7 mmol L⁻¹ for one week before use.  

6. **Group allocation (7 rats per group)**  
   - Group T: diabetic, oral saline.  
   - Group A: diabetic, oral alogliptin 10 mM (gavage).  
   - Group M: diabetic, oral metformin 10 mM (gavage).  
   - Group GelMA: diabetic, local injection of 10 µL plain GelMA into implant bed before implant placement.  
   - Group GelMA+A: diabetic, local injection of 10 µL Gel‑A into implant bed before implant placement.  

7. **Surgical implantation**  
   - Anesthetize with 1 % pentobarbital sodium (45 mg kg⁻¹ i.p.) plus local Primacaine.  
   - Expose the femoral intercondylar fossa, drill a standardized 3 mm × 1.5 mm implant bed under saline irrigation, insert a Ti implant (3 × 1.5 mm, Shandong Hengtai), close layers, and administer antibiotics for 3 days post‑op.  

8. **Drug administration**  
   - Begin 5 days post‑op. Give alogliptin or metformin (10 mM) by oral gavage daily to Groups A and M; give equivalent volume saline to Group T.  
   - For hydrogel groups, inject the specified gel (10 µL) into the implant site immediately before implant insertion (no systemic drug).  

9. **Euthanasia and sample collection** (week 8)  
   - Overdose with 3 % sodium pentobarbital (150–200 mg kg⁻¹ i.p.), harvest femurs with implants.  

10. **Micro‑CT**  
    - Scan each femur at 80 kV, 70 µA, 1440 projections, voxel size 10.425 µm, integration time 500 ms. Reconstruct a 100 µm annular ROI around each implant and calculate BV/TV, trabecular number, and trabecular thickness using VG Studio MAX 3.5.  

11. **Alizarin Red labeling**  
    - Inject 30 mg kg⁻¹ Alizarin Red i.p. 10 days before euthanasia. After harvest, cut 50 µm longitudinal sections and image fluorescence (Axio Imager M).  

12. **Histology**  
    - Dehydrate, embed, and section femurs longitudinally (250–300 µm thick) to avoid implant loss; mount on resin slides.  
    - Prepare 10 µm undecalcified paraffin sections for HE, modified Masson, Safranin O/Fast Green, Van Gieson, and Toluidine Blue staining (follow standard protocols).  

13. **Immunofluorescence** (GLP1R, β‑catenin, GSK‑3β)  
    - Permeabilize sections (0.1 % Triton X‑100, 20 min), block with 10 % normal goat serum 1 h (27 °C). Incubate primary antibodies (1:100) overnight at 4 °C, wash, then apply goat anti‑rabbit Alexa secondary (1:250) 1 h RT in dark. Counterstain with DAPI and image on Olympus inverted fluorescence microscope.  

14. **Immunohistochemistry** (RUNX2, BMP2, ALP)  
    - Deparaffinize, antigen‑retrieve in citrate buffer (95 °C, 20 min), block (10 % goat serum, 1 h, 27 °C). Incubate primary antibodies (1:100) overnight 4 °C, wash, add HRP‑conjugated goat anti‑rabbit (1:200) 1 h RT, develop with DAB, counterstain with hematoxylin, mount, and capture images (Olympus upright microscope).  

15. **VG and Toluidine Blue staining**  
    - VG: mix 9 mL solution B + 1 mL solution A, stain 3 min, rinse, dehydrate in absolute ethanol, clear in xylene (5 min), mount with neutral resin.  
    - Toluidine Blue: stain 5 min, rinse, dehydrate, clear, and mount as above.  

16. **Cell isolation & culture**  
    - Harvest bone marrow from SD rats, isolate BMSCs and BMMs. Culture BMSCs in RPMI‑1640 +10 % FBS +1 % pen/strep at 5 % CO₂, 37 °C. Culture BMMs in high‑glucose DMEM +10 % FBS, treat with M‑CSF (10 ng mL⁻¹) then LPS (200 ng mL⁻¹) to generate M1 phenotype. Obtain HUVECs (Life Technologies) and culture in Medium 200 +2 % LSGS under same conditions.  

17. **Flow cytometry phenotyping**  
    - BMSCs: CD29, CD34, CD90 (Cell Signaling).  
    - BMMs: CD11b (Cell Signaling).  
    - HUVECs: confirm VE‑cadherin expression. Analyze with FlowJo v10.  

18. **Cell viability (CCK‑8)**  
    - Seed cells in 96‑well plates, treat with alogliptin (100 nM) or metformin (200 µM) for 24 h, add CCK‑8 reagent, read OD 450 nm. Confirm non‑cytotoxic concentrations for downstream work.  

19. **BMSC ELISA** (48 h treatment)  
    - Collect supernatants after exposure to saline, alogliptin, or metformin. Measure VEGF, TNF‑α, and IL‑10 using Beyotime kits (catalog numbers PV960, PT516, PI615).  

20. **Adhesion assay**  
    - Plate 2 × 10⁵ cells cm⁻², after 24 h fix, stain for Ki‑67 and FITC‑Phalloidin, image with Nikon Eclipse Ti.  

21. **Osteogenic differentiation**  
    - Plate 2 × 10⁵ cells cm⁻², after 3 days switch to osteogenic medium (10 % FBS, 0.001 mM dexamethasone, 10 mM β‑glycerophosphate, 0.05 mM ascorbate‑2‑phosphate); change medium every 3 days.  

22. **ALP activity (day 7)**  
    - Fix cells (4 % PFA, 30 min), perform ALP staining with Jiancheng kit (A059‑2) per manufacturer’s instructions.  

23. **Alizarin Red (day 21)**  
    - Fix cells (4 % PFA, 30 min), stain with Alizarin Red S (Abcam), dissolve bound dye with cetyl‑pyridinium chloride, read absorbance at 562 nm for quantification.  

24. **HUVEC tube formation**  
    - Thaw Matrigel, coat 48‑well plates (200 µL well⁻¹), solidify 20 min at 37 °C. Seed HUVECs (experimental = alo, control = vehicle), incubate 4–6 h, capture tube networks under microscope.  

25. **qRT‑PCR (after 14 days osteogenic induction)**  
    - Extract total RNA (OD 260/280 = 1.8–2.1), reverse transcribe to cDNA, run TB Green qPCR on Applied Biosystems 7300/7500. Use GAPDH as housekeeping. Thermal cycle: 95 °C 95 s; 45 × (95 °C 5 s, 60 °C 34 s, 95 °C 15 s). Include three biological and three technical replicates. Analyze expression of osteogenic markers and Wnt/β‑catenin pathway genes (2⁻ΔΔCt method).  

26. **Data analysis**  
    - Provide raw data and processed results for all assays. Perform statistical analysis with GraphPad Prism 9: test normality and variance, then one‑way ANOVA with Tukey’s post‑hoc; significance set at two‑tailed p < 0.05.  

Please use the catalog numbers and concentrations listed above, keep all samples blinded, and return all raw images, spreadsheets, and statistical outputs. Let me know if any reagents or equipment are unavailable so we can arrange alternatives. Thanks.
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

## 42. R23C8ED  (elisa)

```
Please conduct the glucagon ELISA on the human islet extracts we have shipped to you.  
Use the Quantikine Glucagon ELISA kit (R&D Systems #DGCG0).  

**Equipment & Supplies**  
- Micropipettes (10‑100 µL, 20‑200 µL, 100‑1000 µL) and 20‑200 µL multi‑channel pipette  
- epMotion 5075 (or hand‑pipetting) with 50 µL tips (Eppendorf 30014421)  
- 20‑200 µL multi‑channel pipette tips (Eppendorf 0030014430)  
- 200 µL and 1000 µL tips (Fisher P‑200 ART, P‑1250 ART)  
- 2 mL SafeSeal tubes (Sarstedt 72.695.500)  
- 10 mL and 25 mL serological pipettes (Fisher 13‑678‑11E / 13‑678‑11)  
- Bench‑top vortex, Bench‑top shaker (Benchmark Orbi BT1502), plate washer (Fisher accuWash 5165100), microplate reader (BMG CLARIOstar Plus with MARS software)  
- Computer with Excel and GraphPad Prism  

**Kit Components**  
- Glucagon microplate (894070), standard (894072), conjugate (894071)  
- Assay diluent RD1‑110 (895967), calibrator diluent RD5‑59 (895968), wash buffer concentrate (895222)  
- Color reagents A (895000), B (895001), stop solution (895032)  
- QC set (R&D QC100)  

Store all unopened kit parts at 2‑8 °C; thaw QC samples as needed.  

**Sample Preparation**  
1. Thaw islet extracts at room temperature in a water bath, invert capped tubes 10 times.  
2. Keep extracts on ice until ready for dilution.  
3. Prepare serial dilutions of each extract in 2 mL tubes: 1:100, 1:1000, 1:2000, 1:5000, 1:10000 using calibrator diluent RD5‑59. Vortex after each dilution before the next.  

**Standard Dilutions**  
4. Prepare a 1:10 dilution of the 20 000 pg/mL standard in RD5‑59.  
5. Perform six 1:2 serial dilutions from that 1:10. Vortex each tube before the next step.  

**QC Preparation**  
6. Reconstitute QC stock in 5 mL distilled water (or thaw pre‑prepared QC).  

**Wash Buffer**  
7. Dilute wash buffer concentrate: 100 mL concentrate + 900 mL DI water to make 1× wash buffer.  

**Pre‑Assay Plate Preparation**  
8. Soak the 96‑well plate: add 800 µL diluted wash buffer to each well, wait 30 s, aspirate. Repeat wash/aspirate twice with 400 µL wash buffer.  

**Assay Steps**  
9. Add 150 µL assay diluent RD1‑110 to each well.  
10. Add 50 µL of standards (in duplicate), QC (in duplicate), and each of the five extract dilutions to appropriate wells using epMotion or hand pipetting.  
11. Seal plate, incubate 3 h at room temperature.  
12. Wash as in step 8, repeat 3 times (use plate washer).  
13. Add 200 µL ice‑cold glucagon conjugate to each well.  
14. Seal again, incubate 1 h at 4 °C (no plate stacking if multiple kits).  
15. Wash again 3 times as above.  
16. Mix color reagents A and B in equal volume, add 200 µL to each well within 15 min of mixing.  
17. Incubate 30 min at room temperature, away from light.  
18. Add 50 µL stop solution to each well.  

**Reading**  
19. Read OD at 450 nm with 540 nm correction on the CLARIOstar within 30 min of adding stop solution.  

**Data Analysis**  
20. Verify standards are within ±15 % of expected values and duplicate CV ≤20 %. If not, repeat assay.  
21. Verify QC values are within known ranges. If not, repeat assay.  
22. For each extract, average the glucagon concentrations from the four dilutions (1:100–1:5000).  
23. Normalize to islet volume: express as pg/100 IEQs/min.  
24. Use Prism to graph hormone concentrations over time, calculate stimulation index (max response / baseline) and AUC.  

**Reporting**  
25. Send us the raw OD data, calculated concentrations, and Prism graphs.  
26. Include any deviations from the protocol that could affect the results.  

Please complete the assay within 3 business days of receipt and forward the data files to our research team. Let us know if any supplies or equipment are missing. Thank you.
```

label: 

defect_types: 

notes: 

---

## 43. R41A15B  (growth_curve)

```
1. Prepare the following buffers fresh on the day of use (keep all at 4 °C unless noted).  

   * **Ni‑IDA lysis buffer (100 mL):** 50 mM Tris‑HCl pH 8.0 (5 mL 1 M), 300 mM NaCl (6 mL 5 M), 20 mM imidazole (2 mL 1 M), 1 % Triton X‑100 (1 mL), 1 mM DTT (100 µL 1 M), 1 mM PMSF (1 mL 100 mM, add just before use). Bring to 100 mL with ddH₂O.  

   * **Ni‑IDA equilibration/wash buffer (100 mL):** 50 mM Tris‑HCl pH 8.0 (5 mL 1 M), 300 mM NaCl (6 mL 5 M), 20 mM imidazole (2 mL 1 M), bring to 100 mL with ddH₂O. Store ≤ 1 month at 4 °C.  

   * **Ni‑IDA high‑imidazole wash buffer (100 mL):** 50 mM Tris‑HCl pH 8.0 (5 mL 1 M), 300 mM NaCl (6 mL 5 M), 500 mM imidazole (50 mL 1 M), bring to 100 mL with ddH₂O. Store ≤ 1 month at 4 °C.  

   * **In‑vitro LLPS stock buffer (100 mL):** 25 mM Tris‑HCl pH 7.4 (2.5 mL 1 M), 500 mM NaCl (10 mL 5 M), 10 % glycerol (10 mL), 1 mM DTT (100 µL 1 M). Add DTT just before use. Keep on ice; can store without DTT ≤ 1 week at 4 °C.  

   * **10 % (w/v) PEG‑4000 solution** in water, filter‑sterilized, keep at 20‑25 °C.  

2. **Bacterial expression of His₆‑ARID3B** (pET28a‑His6‑ARID3B).  

   a. Thaw 50 µL chemically competent *E. coli* BL21(DE3) on ice. Add 250 ng plasmid, mix, incubate 30 min on ice. Heat‑shock 42 °C for 90 s, return to ice 2 min. Add 500 µL pre‑warmed LB (no antibiotic), shake 37 °C, 200 rpm, 30 min. Plate 40 µL on LB‑Kan 50 µg/mL, incubate overnight 37 °C.  

   b. Pick one colony for a 4 mL starter culture in LB‑Kan (50 µg/mL). Grow 37 °C to OD₆₀₀ = 0.5–0.8. Induce with 0.2 mM IPTG. Split the culture: keep one at 37 °C, move the other to 15 °C (pre‑cooled) for 16 h. Harvest 1 mL each, lyse, run SDS‑PAGE to decide which temperature gives the best soluble expression.  

   c. For large scale, inoculate 2 µL glycerol stock into 10 mL LB‑Kan, grow overnight 37 °C. Dilute 1 % (v/v) into fresh LB‑Kan (e.g., 1 L total). Grow 37 °C to OD₆₀₀ = 0.6–0.8, cool to 15 °C (if that was optimal), add 0.2 mM IPTG, continue induction 16 h at the selected temperature. Harvest cells by centrifugation (≈ 5 000 g, 10 min, 4 °C).  

3. **Cell lysis and soluble fraction preparation.**  

   a. Resuspend cell pellet in 5 mL lysis buffer per gram of wet pellet. Keep on ice.  

   b. Sonicate on ice (30 %–40 % power, 3 s ON/6 s OFF) for total 20 min, avoiding overheating.  

   c. Centrifuge 13 000 g, 20 min, 4 °C. Collect supernatant (soluble fraction) and keep aliquots of total lysate, supernatant, and pellet for SDS‑PAGE analysis.  

4. **Ni‑IDA affinity purification.**  

   a. Equilibrate Ni‑IDA column with 5 column volumes (CV) equilibration buffer (20 mM imidazole).  

   b. Load cleared soluble lysate onto the column at 4 °C, collect flow‑through.  

   c. Wash with 10 CV equilibration buffer (20 mM imidazole).  

   d. Elute with 5 CV high‑imidazole wash buffer (500 mM imidazole). Collect 1 mL fractions.  

   e. Analyze elution fractions by SDS‑PAGE; pool those with the strongest ARID3B band and minimal contaminant bands.  

5. **Post‑purification processing.**  

   a. Dialyze pooled fractions against PBS pH 7.4 (2 L, change twice, 4 °C, overnight).  

   b. Filter through 0.22 µm low‑binding filter into low‑binding tubes.  

   c. Determine concentration by Bradford assay (BSA standard curve).  

   d. Aliquot (e.g., 50 µL) and store at –80 °C.  

   e. Quality control: run a final SDS‑PAGE with BSA (1 µg) lane, and a Western blot using anti‑His or a multi‑tag antibody to confirm identity.  

   f. Perform a freeze‑thaw stability test on one aliquot (thaw on ice 5 min, hold 4 °C 30 min, re‑freeze). No turbidity or precipitation indicates acceptable stability.  

6. **Size‑exclusion chromatography (optional but requested).**  

   a. Run analytical SEC on a calibrated column (include blank and molecular‑weight markers).  

   b. Load 100 µL of purified ARID3B (≈ 1 mg/mL) in PBS, record chromatogram.  

   c. Note peak retention times and relative areas to assess oligomeric state and heterogeneity.  

7. **In‑vitro phase‑separation assay** (using purified ARID3B).  

   a. Thaw an aliquot of ARID3B on ice, dilute into LLPS stock buffer to a final concentration of ~ 10 µM (adjust as needed). Clarify by centrifugation 13 000 g, 10 min, 4 °C.  

   b. Prepare reaction mixtures (final volume 20 µL) containing:  

      * ARID3B at desired concentration (e.g., 5‑15 µM)  
      * 10 % PEG‑4000 (add volume calculated from the 10 % stock)  
      * ddH₂O to bring to final volume.  

   c. Mix gently by pipetting, avoid vortexing. Incubate 20 °C–25 °C for 15–30 min to allow droplet formation.  

   d. Spot 3–5 µL on a clean glass slide, cover with a coverslip (no bubbles).  

   e. Image:  

      * For EGFP‑ARID3B (if you request the EGFP fusion), use fluorescence microscopy (488 nm excitation).  
      * For untagged ARID3B, use bright‑field. Capture representative fields.  

8. **FRAP on in‑vitro condensates (optional).**  

   a. Use the same reaction mixture as in step 7, place 3–5 µL in a glass‑bottom dish.  

   b. On a confocal with FRAP module, locate a single droplet with a 100× oil objective. Acquire 3–5 pre‑bleach frames (low laser power).  

   c. Bleach a small ROI inside the droplet (or the whole droplet) with 488 nm laser at high power for 1–3 s until fluorescence drops to ~ 60 % of initial.  

   d. Record recovery every 1–3 s for 2–5 min (or until plateau).  

9. **Cellular work (EGFP‑ARID3B in HEPM cells).**  

   a. Seed HEPM cells on sterile glass coverslips in a 6‑well plate; grow to 50‑70 % confluence.  

   b. Transient transfection (per well):  

      * Tube A: 2 µg EGFP‑ARID3B plasmid in 200 µL Opti‑MEM.  
      * Tube B: 2 µL Lipofectamine 2000 in 200 µL Opti‑MEM (5 min at RT).  

      Combine, incubate 15‑20 min, add dropwise to cells (replace medium with fresh complete medium first).  

   c. After 4 h, replace transfection medium with fresh complete medium. Incubate 24 h total post‑transfection.  

   d. **Live‑cell imaging:** Use a confocal with 488 nm laser, low power (1‑5 %). Capture images of ≥ 10 cells per condition from ≥ 3 independent transfections.  

   e. **Immunofluorescence for SMAD2/3 co‑localization:**  

      * Fix cells 24–36 h post‑transfection with 4 % PFA, 15 min RT.  
      * Wash 3× PBS, permeabilize 0.2 % Triton X‑100 (10 min RT), wash 3× PBS.  
      * Block 60 min in normal goat serum.  
      * Incubate with anti‑SMAD2/3 (1:200 in blocking buffer) overnight 4 °C.  
      * Wash 3× PBS, incubate with Alexa‑594 secondary (1 h, RT, dark).  
      * Wash, stain nuclei with DAPI (5 min, RT, dark), wash, mount with anti‑fade medium.  

   f. **Imaging:** Acquire 488 nm (EGFP), 594 nm (SMAD2/3), and 405 nm (DAPI) channels. Quantify nuclear puncta and co‑localization.  

   g. **FRAP in cells:** Select a nuclear EGFP‑ARID3B condensate, acquire 3‑5 pre‑bleach frames, bleach the condensate with high‑power 488 nm laser (1‑3 s) to ~ 60 % intensity, then record recovery every 1‑2 s for 2‑5 min.  

Please let us know if any reagents (e.g., plasmids, antibodies) need to be supplied, or if you have any questions about the timing or equipment. Thank you.
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

## 45. R3AE28C  (qpcr)

```
Please conduct the following experiment on our fibroblast samples:

1. **Cell culture** – Thaw HFF1 (ATCC SCRC‑1041) and expand in DMEM + 10 % FBS + 2 mM L‑glutamine + 1 % penicillin/streptomycin. Keep cells at 37 °C, 5 % CO₂, 95 % humidity. Use cells at the same passage number and confluence for all conditions; seed control and treatment plates in parallel.

2. **REAC CO‑IBZ treatment** – Use a BENE‑110 device (ASMED, Scandicci). Apply the built‑in CO‑IBZ protocol: nine 30‑min sessions over three days (3 sessions per day). Start each session one hour after the previous one. Keep the asymmetric conveyor probe (ACP) in contact with the culture for 30 min each session. Leave untreated wells in the same incubator as controls.

3. **Post‑treatment sampling** – After the final session, harvest cells for:
   - RNA isolation (RNeasy Mini Kit, Qiagen) – measure concentration/purity.
   - Protein extraction for immunofluorescence.
   - Medium collection for TAC, nitrite, and ROS assays (keep samples on ice, then freeze if not used immediately).

4. **RT‑qPCR** – Use Luna One‑Step RT‑qPCR Kit (NEB). Target genes: SIRT1, NOX4, VEGF, p16, p21, HAS2. Reference: GAPDH. Run in triplicate technical replicates per sample. Calculate ΔΔCt (assuming similar efficiencies) and express as fold change vs control.

5. **Immunofluorescence** – Fix cells with 4 % paraformaldehyde, permeabilize with Triton X‑100. Incubate overnight at 4 °C with primary antibodies:
   - SIRT1 (Cell Signaling, 1:100)
   - NOX4 (Santa Cruz, 1:500 from 1:50 stock)
   - PARP1 (Cell Signaling, 1:800)
   - vWF (Santa Cruz, 1:500 from 1:50 stock)
   - Collagen III (Abcam, 1:500)
   Wash, then add Alexa‑conjugated secondaries (1:500) for 1 h at 37 °C in dark. Counterstain nuclei with DAPI (1 µg/mL). Acquire images on a Leica THUNDER DMi8 microscope with identical exposure, illumination, and acquisition settings across all samples. Analyze mean fluorescence intensity per cell using ImageJ/Fiji, averaging all cells within a well, then summarizing per biological replicate.

6. **Total antioxidant capacity (TAC)** – Use the Abcam Colorimetric TAC kit. Add 100 µL Cu²⁺ working solution to each 96‑well (standard or sample), shake, incubate 90 min at room temperature in the dark. Read absorbance at 570 nm (Akribis reader). Calculate TAC as (Ts/Sv) × D, where Ts = sample TAC from standard curve (nmol), Sv = sample volume (µL), D = dilution factor. Perform 3 technical replicates per biological sample.

7. **Nitrite (NO) assay** – Use Thermo Fisher Griess Reagent Kit. Mix 20 µL Griess reagent with 150 µL sample, incubate 30 min at room temp. Read absorbance at 548 nm (Akribis reader). Analyze relative to a nitrite standard. Include 3 technical replicates per biological sample.

8. **Intracellular ROS** – Stain cells with 10 µM CM‑H₂DCFDA (reconstituted in DMSO) for 30 min at 37 °C in the dark. Wash with PBS, then measure fluorescence in PBS (exc 485 nm, em 530 nm) on an Akribis reader. Use 3 technical replicates per biological sample.

9. **Replicates** – Perform 5 biological replicates per condition (treated vs untreated). Technical replicates are for assay consistency; average them to obtain one value per biological sample.

10. **Statistics** – Use GraphPad Prism 9. Test for normality (Shapiro‑Wilk). Compare control vs CO‑IBZ using unpaired two‑tailed Welch’s t‑test at the biological‑replicate level (p < 0.05 considered significant). Report mean ± SD.

Please confirm receipt and let us know the anticipated timeline for completion.
```

label: 

defect_types: 

notes: 

---

## 46. R03182B  (elisa)

```
Please perform the α‑synuclein ELISA on our samples as follows:

1. Coat 384‑well MaxiSorp plates (Nunc) with the capturing antibody (α‑Syn, BD Biosciences 610787) at a 1:500 dilution in coating buffer (0.2 % NaN₃ in NaHCO₃, pH 9.6). Incubate overnight at 4 °C.  
2. Wash each well three times with PBS‑0.05 % Tween‑20 (PBS‑T).  
3. Block the plates for 1 h at 37 °C with blocking buffer (1.125 % fish‑skin gelatin in PBS‑T).  
4. Load our study samples in duplicate into the wells (use 20 µL per well; if your protocol uses a different volume, adjust accordingly).  
5. Incubate the plates at room temperature for 2 h.  
6. Add a biotinylated detection antibody (anti‑α‑syn, same clone as the capturing antibody, diluted as recommended) and incubate for 1 h at 37 °C.  
7. Wash five times with PBS‑T.  
8. Add ExtrAvidin phosphatase (Sigma E2636) diluted 1:200 in blocking buffer; incubate for 30 min at 37 °C.  
9. Add fast p‑nitrophenyl phosphate (Sigma N1891) as substrate, and read absorbance at 405 nm every 2.5 min for up to 60 min.  
10. From the kinetic curve, identify the time point(s) where the absorbance of each standard and our sample dilutions fall within the linear (log‑phase) portion of the curve.  
11. Use the standard curve to calculate the α‑syn concentration in each sample.  
12. Return a report with the raw absorbance values, the chosen time point(s), standard curve parameters, and calculated concentrations for each sample (duplicated).
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

## 50. R4D657A  (elisa)

```
Please run an indirect ELISA on our provided samples (chicken/layer hen IgY, rat sera, and cat sera) to test for the presence of anti-HIV antibodies, following the protocol below:

1. Coat Nunc 96-Well Polystyrene Round Bottom Microwell Plates (Thermo Fisher #260210) with 50 ng of synthetic gp-120 peptide per well in Coating Buffer (BioLegend #421701), and incubate overnight at 4°C.
2. Wash the plate 4 times with PBS-Tween-20. Block with 25 µl/well of 3% non-fat milk in PBS for 1 hour at room temperature.
3. Wash the plate 4 times with PBS-Tween-20. Add our samples in triplicate (25 µl of IgY at 1 mg/ml, or 25 µl of cat/rat sera diluted 1:16 in PBS-non-fat milk). Include human positive serum, turtle serum negative controls, and 0.9% normal saline blanks.
4. Incubate for 2 hours at room temperature, then wash the plate 4 times with PBS-Tween-20.
5. Add 25 µl per well of the secondary detection reagent, SpLAG-anti-IgY-HRP (homemade, peroxidase-labelled IgY coupled to proteins A, G, and L), diluted 1:1000 in ELISA Diluent (STEMCELL #1916). Incubate for 1 hour at room temperature.
6. Wash the plate 4 times with PBS-Tween-20. Add 50 µl of TMB substrate (MilliporeSigma #54827-17-7) to each well and incubate in the dark for 15 minutes at room temperature. 
7. Stop the reaction once positive controls develop color and blanks/negative controls remain clear. Read the plate and calculate the cut-off point as four times the mean of the negative controls.
```

label: 

defect_types: 

notes: 

---

## 51. RA5315C  (growth_curve)

```
1. Prepare TAP medium (or an equivalent algal growth medium) as described in the standard recipe and sterilize it.

2. Provide the following equipment and consumables:
   - 100 mL Erlenmeyer flasks (one per culture)
   - Orbital shaker capable of 150 rpm, 25 °C
   - Light source delivering 80 µmol m⁻² s⁻¹ white light (acceptable range 60–120 µmol m⁻² s⁻¹)
   - Black‑frame, clear‑bottom 96‑well plate (e.g., IsoPlate™ 96F, PerkinElmer catalog #6005020)
   - Plate reader that can measure absorbance at 750 nm and fluorescence at the wavelengths listed below
   - Pipettes and sterile tips for 100 µL sampling

3. Inoculation:
   - Take 1 mL of our Chlamydomonas reinhardtii culture that is in stationary phase (12–168 h old).
   - Add this inoculum to 50 mL of fresh TAP medium in a 100 mL Erlenmeyer flask.
   - Place the flask on the orbital shaker at 150 rpm, 25 °C, with a 1 cm orbital diameter and the specified light intensity.

4. Sampling schedule:
   - Immediately after inoculation (time 0), withdraw 100 µL of culture, transfer to a well of the black 96‑well plate, and measure absorbance and fluorescence as described below.
   - Continue sampling at least once per day for the next 168 h (7 days).  
   - Do not remove more than 10 % of the total culture volume over the entire experiment.  
   - For each time point, run technical replicates (minimum duplicate wells).

5. Plate‑reader settings:
   - Use the black 96‑well plate with clear bottom.
   - Measure absorbance at 750 nm (cell density proxy).
   - Fluorescence measurements:
     * Chlorophyll: excitation 440 nm, emission 680 nm, gain 70, optics position bottom
     * mVenus: excitation 500 nm, emission 530 nm, gain 120, optics position bottom
     * mCherry: excitation 583 nm, emission 613 nm, gain 150, optics position bottom

6. After the 168‑hour growth period, retain the remaining culture for downstream analyses, e.g., dry cell weight (DCW) determination by centrifugation.

Please let us know if any reagents or equipment are missing, or if you need clarification on any step. Thank you.
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

## 53. RE96E0B  (qpcr)

```
Please run the following T-cell activation, flow cytometry, and gene expression assay using our provided Jurkat E6-1 cells and test samples. 

1. Prepare complete RPMI-1640 medium (supplemented with 10% FBS and 1× penicillin-streptomycin) and Jurkat cell culture medium further supplemented with 1 mM sodium pyruvate, 1.5 g/L sodium bicarbonate, 10 mM HEPES, and 4.5 g/L glucose.

2. Ensure Jurkat E6-1 cells are in the log-growth phase with a passage number below 40 and viability above 95% before starting.

3. Reconstitute the provided recombinant human galectins (galectin-1, galectin-3, galectin-7, galectin-8 variant 1, and galectin-8 variant 2) in Milli-Q water to 500 µg/mL. Incubate on ice for 10 minutes, mixing by flicking every 2–3 minutes, and prepare 10-fold working stocks.

4. Seed Jurkat E6-1 cells in 6 cm dishes at a final density of 0.6 million cells/mL in a total volume of 5 mL. Treat the cells in technical triplicates with:
   - Untreated medium (negative control)
   - Anti-CD3/CD28 antibodies at 1 µg/mL each (positive control)
   - Recombinant human galectins at final concentrations of 10 µg/mL, 25 µg/mL, and 50 µg/mL
   Incubate at 37 °C with 5% CO2 for 16–20 hours.

5. Following incubation, observe and record cell morphology and agglutination. Harvest the cells, determine density and viability via trypan blue exclusion, and split each sample:
   - Fix 2 million cells per condition in freshly prepared 4% PFA (pH 7.4–7.6) for 15 minutes at room temperature, wash with PBS, and store in 333 µL PBS at -80 °C for flow cytometry.
   - Pellet the remaining cells and store at -80 °C for RNA extraction.

6. Perform flow cytometry for CD69 expression:
   - Seed 0.3 million fixed cells in 50 µL per well in a 96-well V-bottom plate.
   - Stain with anti-CD69-APC (1:10 dilution) and PE mouse IgG1 isotype control (1:20 dilution) to reach final working concentrations of 5 µg/mL in 100 µL total volume.
   - Incubate at 4 °C for 1 hour on an orbital shaker at 575 rpm, protected from light.
   - Wash twice with PBS, resuspend in 150 µL PBS, and acquire a minimum of 10,000 events per sample on a CytoFLEX S flow cytometer to measure CD69 mean fluorescence intensity.

7. Perform RT-qPCR for IL-2 expression:
   - Extract total RNA from the frozen cell pellets using the Zymo Quick-RNA Miniprep kit, including on-column DNase I digestion to remove genomic DNA.
   - Measure RNA concentration and purity (target A260/A280 of 1.8–2.1).
   - Perform genomic DNA removal and reverse transcription using the HiScript III RT SuperMix (+gDNA wiper) on 1 pg to 500 ng of template RNA.
   - Run real-time PCR on a StepOnePlus Real-Time PCR System using FastSYBR Mixture, 500 nM of IL-2 primers (Forward: AGAACTCAAACCTCTGGAGGAAG, Reverse: GCTGTCTCATCAGCATATTCACAC), and 500 nM of GAPDH primers (Forward: GACGCTGGGGCTGGCATTG, Reverse: GCTGGTGGTCCAGGGGTC) with an amplification profile of 95 °C for 2 min, followed by 45 cycles of 95 °C for 15 s and 60 °C for 30 s. Calculate relative IL-2 gene expression using the comparative Ct method normalized to GAPDH.
```

label: 

defect_types: 

notes: 

---

## 54. R3DE511  (elisa)

```
1. Seed our astrocyte-enriched primary cultures at 50,000 cells per well in a black-walled, clear-bottom 96-well plate. Fill all outer wells with DPBS to prevent edge effects and evaporation. 

2. After 48 hours, treat the cultures according to our experimental design:
   - For MLi-2 dose-response: prepare serial dilutions starting at 1 µM with a 1:5 ratio across wells, and treat for 90 minutes. Include a vehicle-only (DMSO) control matching the highest concentration.
   - For LLOME treatment: treat cells with either MLi-2 (100 nM), LLOME (1 mM), or co-treat with LLOME (1 mM) and MLi-2 (100 nM) for 2 hours.

3. Fix the cells using freshly prepared 4% PFA in DPBS (100 µL per well) for 20 minutes at room temperature, dispensing gently along the well edge. Perform all subsequent washes and liquid handling using a multichannel pipette and reagent reservoir, taking care not to detach the cells.

4. Wash the wells 5 times with DPBS, ensuring residual PFA is thoroughly removed to minimize background.

5. Permeabilize the cells with 0.1% Triton X-100 in DPBS (100 µL per well) for 20 minutes at RT, then block with 5% FBS in DPBS (100 µL per well) for 1 hour at RT in a humidified chamber.

6. Incubate the plates with the primary antibody diluted 1:500 in blocking solution (40 µL per well) overnight at 4°C in a humidified lidded box.

7. Wash the wells 5 times with DPBS, then incubate with goat anti-rabbit Alexa Fluor 488 (1:500) and Alexa Fluor 647 phalloidin (1:1,000) in DPBS (40 µL per well) for 1 hour at RT, protecting the samples from light from this step onward.

8. Wash 5 times with DPBS, perform nuclear staining with Hoechst (1:10,000 in DPBS, 100 µL per well) for 5 minutes at RT, and wash 3 times with DPBS. Leave the plates in DPBS with 0.05% sodium azide.

9. Acquire images on the Operetta CLS high-content imaging system using a 40x water-immersion objective (NA 1.1) across 29 randomly selected fields per well using 7 Z-stack planes. Use the following channel settings:
   - Hoechst: Ex 355–385 nm, Em 430–500 nm
   - Alexa Fluor 488 (EGFP channel): Ex 460–490 nm, Em 500–550 nm
   - Alexa Fluor 647: Ex 615–645 nm, Em 655–760 nm

10. Process and analyze the acquired images using Harmony software to quantify pRab10-positive vesicles. Apply a Gaussian smoothing filter to the Alexa 647 channel to identify cell regions, Method B for nuclear identification via Hoechst, and a Sliding Parabola filter (curvature 4) on the EGFP channel to isolate and classify pRab10-positive spots based on area, roundness, and intensity. Export the final quantification results as an Excel file.
```

label: 

defect_types: 

notes: 

---

## 55. RF831D6  (growth_curve)

```
Dear lab team,

Please run the OD600 measurements on our bacterial cultures as follows.  
Send us the final excel file and any questions in the shared drive folder.

1. **Clean work area**  
   a. Wipe the bench and all pipette tips with DNA Away and RNase Away.  
   b. Wipe the same surfaces again with 70 % ethanol.  

2. **Prepare the 96‑well plate**  
   a. Use a clear round‑bottom 96‑well plate.  
   b. In the two wells labeled BLANK (in duplicate), pipette 100 µL of sterile media blank.  

3. **Prepare sample wells**  
   a. In each well that will contain a sample (the plate map is in the attached excel sheet), pipette 90 µL of the same sterile media blank.  
   b. Mix the media in each well by pipetting up and down 5 times.  

4. **Dilute the cultures**  
   a. Thoroughly resuspend each bacterial culture by flicking or gentle vortexing.  
   b. Pipette 10 µL of each culture into its designated sample wells (in duplicate).  
   c. Add 70 µL of media to each sample well to bring the total to 100 µL.  
   d. Mix each sample well by pipetting up and down 5 times.  
   e. Set aside the remaining culture for downstream use.  

5. **Measure OD600**  
   a. Place the plate in the microplate reader.  
   b. Measure absorbance at 600 nm for every well.  
   c. Record the raw OD readings in the attached excel sheet.  

6. **Correct the data**  
   a. In the excel sheet, calculate the corrected OD for each sample as:  
      \[
      \text{OD corrected} = (\text{OD sample} - \text{average OD blanks}) \times 10
      \]  
   b. Save the completed sheet in the designated folder.  

7. **Clean up**  
   a. Dispose of the used plate in a biohazard container.  
   b. Add 10 % bleach to each well of the plate and let sit for 30 minutes.  
   c. Empty the plate into the drain with running water.  
   d. Wipe the bench and pipettes with DNA Away/RNase Away, then with 70 % ethanol.  

8. **Optional** (if a Bunsen burner is required for sterility):  
   a. Light the burner, work within its sterile field, and extinguish it after the plate is discarded.  

Please complete the run and upload the finished excel sheet to the shared drive. If you need clarification on the plate map or any other detail, let me know.
```

label: 

defect_types: 

notes: 

---

## 56. R1500F5  (qpcr)

```
1. Prepare a fresh digestion solution for each skin sample on ice: 900 µL HBSS (1×), 100 µL Collagenase P (1 mg/mL), 50 µL Dispase II (0.5 mg/mL), 8 µL DNase I (0.1 mg/mL). Keep the mix cold and use only freshly thawed enzymes.

2. Make 100 mL of both FACS buffer and MACS buffer (PBS without Ca²⁺/Mg²⁺, pH 7.2) adding 0.5 mL heat‑inactivated fetal calf serum (0.5 % final) and 0.4 mL 0.5 M EDTA (2 mM final). Filter the MACS buffer through a 0.22 µm filter, store both at 4 °C (stable up to 2 months). Keep all buffers chilled during staining.

3. For each sample, after tissue collection, place the excised dorsal foot skin in a 1.5 mL tube with 500 µL ice‑cold complete DMEM and keep on ice.

4. Add 1.058 mL of the freshly prepared digestion solution to each tube (prepare a little extra to compensate for pipetting loss). Mince the tissue with sterile scissors directly in the tube until very small fragments are visible.

5. Incubate the minced tissue at 37 °C for 50 min in a thermomixer shaking at 1100–1400 rpm. After incubation, immediately chill the tubes, add 500 µL cold complete DMEM to stop the enzymes, and place on ice.

6. Pass the suspension through a 70 µm cell strainer into a sterile 50 mL conical tube, rinsing the strainer and original tube with cold complete DMEM to recover cells.

7. Centrifuge the filtered cells at 300 × g for 5 min at 4 °C, discard supernatant, and resuspend the pellet in an appropriate volume of FACS buffer (or MACS buffer if you will proceed to magnetic enrichment).

8. **Flow cytometry staining** (use the stromal/immune panel listed below). For each sample:

   a. Transfer the cell suspension to a 96‑well round‑bottom plate; record the total cell number and aim to plate equal numbers across samples.  
   b. Wash twice with FACS buffer (300 × g, 5 min, 4 °C).  
   c. Block Fc receptors on ice for 5 min.  
   d. Add the antibody master mix (see panel) and incubate 45 min on ice in the dark.  
   e. Wash twice with PBS (300 × g, 5 min, 4 °C).  
   f. Add Zombie UV viability dye (1:50 dilution in PBS), incubate 10 min at room temperature in the dark, then wash twice with FACS buffer.  
   g. Fix cells in 4 % PFA for 30 min at RT, wash once, resuspend in FACS buffer and keep at 4 °C in the dark (stable up to 48 h) until acquisition.

   **Antibody panel (final dilutions, fluorochromes, clones):**  
   - CD45 FITC (BioLegend, 30‑F11) 1:200 – leukocytes  
   - CD11b APC (BioLegend, M1/70) 1:200 – myeloid cells  
   - MERTK APC‑Cy7 (BioLegend, 2B10C42) 1:200 – macrophages  
   - Ly‑6G BV421 (BioLegend, 1A8) 1:200 – neutrophils  
   - Vimentin APC (Biotechne, 280618) 1:200 – mesenchymal (intracellular; perform fixation/permeabilization before this antibody)  
   - CD31 PE (BioLegend, 390) 1:200 – endothelial cells  
   - CD326 (Ep‑CAM) APC‑Cy7 (BioLegend, G8.8) 1:200 – epithelial/keratinocytes  
   - CD90.2 (Thy1.2) Pacific Blue (BioLegend, 30‑H12) 1:200 – fibroblasts  
   - Podoplanin Alexa‑647 (BioLegend, PMab‑1) 1:200 – activated fibroblasts  
   - CD140a (PDGFR‑α) PE‑Cy7 (BioLegend, APA5) 1:200 – activated fibroblasts  
   - Ly‑6A/E (Sca‑1) PE (BioLegend, W18174A) 1:200 – pluripotent mesenchymal cells  
   - TOSV‑mCherry (no antibody, native fluorescence) – infected cells  
   - Zombie UV (BioLegend) – viability (1:50)

   Include appropriate single‑stained controls, FMO controls, and an uninfected skin sample for background.

9. Acquire the stained samples on a flow cytometer equipped with 405 nm (for Zombie UV), 488 nm (FITC), 561 nm (mCherry, PE, BV421), 640 nm (APC, APC‑Cy7, Alexa‑647) lasers. Perform compensation with single‑color controls or compensation beads. Gate on singlets → live cells → CD45⁺ or CD45⁻ as needed, then identify mCherry⁺ infected cells within each subpopulation.

10. **Optional magnetic enrichment of fibroblasts:** After digestion (step 7) and before staining, resuspend cells in MACS buffer (PBS + 0.5 % FBS + 2 mM EDTA). Follow the Tumour‑Associated Fibroblast Isolation Kit (Miltenyi) protocol:

    a. Adjust volume to 90 µL MACS buffer per 1 × 10⁷ cells.  
    b. Add the Non‑TAF Depletion Cocktail, incubate 15 min on ice, wash, and pass through an LD column; collect flow‑through.  
    c. Add CD90.2 MicroBeads (20 µL per 1 × 10⁷ cells), incubate 15 min on ice, wash, and apply to an MS column.  
    d. Elute CD90.2⁺ fibroblasts, count, assess viability, and confirm enrichment by a quick flow run using CD90.2 and a fibroblast marker (e.g., podoplanin).

11. **RNA extraction (if needed):**  

    a. For whole‑tissue samples, place the skin in 1 mL TRIzol with two 7 mm stainless‑steel beads, homogenize in a TissueLyser (50 Hz, 10 min).  
    b. For cell pellets (bulk or MACS‑enriched), lyse directly in the kit lysis buffer (add β‑mercaptoethanol as instructed).  
    c. Process lysates with the Zymo Quick‑RNA Microprep Kit (or PureLink kits) according to the manufacturer, including on‑column DNase treatment.  
    d. Quantify RNA by spectrophotometry; store at –80 °C.  

Please carry out the above on the set of infected foot‑skin samples we are sending (approximately 12 mice, 72 h post‑infection). Return the flow‑cytometry FCS files, a summary table of cell percentages (including % mCherry⁺ cells in each gate), and any RNA extracts you generate. Let us know immediately if any reagents are unavailable or if you encounter difficulties at any step. Thank you.
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

## 58. RF0FECF  (growth_curve)

```
1. Use the Human Protein Atlas (HPA) “Brain Atlas” to download normalized transcript levels (nTPM) and regional specificity scores (Tau) for PGR across all human brain regions. Compare these values with those from endometrium, cervix, and ovary. Also download the single‑nuclei RNA‑seq data from HPA and determine which cell types contribute most of the PGR transcripts.

2. Access TCGA data via the Xena Browser (or cBioPortal) for the following tumor types: glioma (n ≈ 153, include all GB samples), endometrium (n ≈ 180), ovary (n ≈ 419), lung (n ≈ 1011), and breast (n ≈ 1092). Remove duplicate entries, log2‑transform the expression values, and perform a Kruskal‑Wallis test followed by Dunn’s post‑hoc test to compare PGR expression across cancer types.

3. For the glioblastoma (GB) survival analysis: obtain TCGA‑GB cohort data (cBioPortal, TCGA‑GDC). Classify patients as IDH‑wildtype (no IDH mutation) and keep only those. Use the RNA‑seq Z‑score normalized values for PGR and NR3C1. Split each receptor’s expression into quartiles and define “high” (top 25 %) and “low” (bottom 25 %) groups. Limit follow‑up to 40 months, and also perform a secondary analysis restricted to survival between 10 and 40 months. Generate Kaplan‑Meier curves and run log‑rank tests for overall survival comparisons.

4. Culture the following cell lines in the indicated media with 1 % Penicillin‑Streptomycin (10 000 U/µg ml):
   - Human GB lines: U87 (ATCC HTB‑14, Lot 70016790) and U251 (ATCC HTB‑17, PCR‑validated, LDG‑INMEGEN 00451).
   - Murine glioma line: C6 (ATCC CCL‑107, Lot 58078536).
   - Breast cancer lines: T47D and HCC70 (RPMI + 10 % FBS).
   - Human ESC‑derived glial cells (as previously described, Ethical Approval 212250‑212071).  
   Maintain all cultures at 37 °C, 5 % CO₂. Verify glial differentiation by flow cytometry using anti‑MAP2 (neuronal) and anti‑GFAP (astrocytic) antibodies.

5. Treat cells with mifepristone (MF, Sigma M8046) or RU‑486 and with ulipristal acetate (UPA) as described in the supplementary methods. Use 0.01 % DMSO as the vehicle control. For the dose‑response MTT assay, seed U87, U251, and C6 cells at 1 500 cells per well in 96‑well plates, let them attach for 24 h, then add MF/UPA at concentrations ranging from 1 µM to 125 µM (final DMSO = 0.01 %). Incubate for 72 h (the optimal time point from our growth curve), add MTT (5 mg ml⁻¹), incubate 3 h, dissolve formazan crystals in 200 µL DMSO, and read absorbance at 570 nm (reference 630 nm). Plot viability versus concentration and calculate IC₅₀ and IC₂₀ values.

6. For the sphere‑formation assay: plate U251 and C6 cells in ultra‑low‑attachment 96‑well plates at 1 cell µL⁻¹ (final 100 µL per well) in serum‑free neural stem cell medium (DMEM/F12 + B27 without vitamin A 20 µL mL⁻¹, rhEGF 20 ng mL⁻¹, bFGF 20 ng mL⁻¹, antibiotics: amphotericin 0.00025 g L⁻¹, penicillin 0.0603 g L⁻¹, streptomycin 0.1 g L⁻¹). Add MF at the IC₅₀ concentration (≈ 40 µM) or vehicle at the time of seeding and repeat the treatment daily for three days. On day 10, count spheres under a 4× objective, record sphere diameters with a Neubauer chamber, and calculate Sphere Formation Efficiency = (number of spheres / seeded cells) × 100.

7. Western blotting: lyse cell samples in RIPA buffer, run 12 % SDS‑PAGE (cell lysates) and 7.5 % SDS‑PAGE (tissue lysates) at 100 V, transfer to nitrocellulose, block with 5 % BSA. Probe first with anti‑PR (Abcam ab63605) followed by HRP‑conjugated anti‑rabbit secondary. Strip membranes with acidic glycine, reprobe with anti‑α‑tubulin (Santa Cruz sc‑398103) and HRP‑conjugated anti‑mouse (Abcam ab6789). Detect chemiluminescence, capture images, and quantify PR band intensity relative to α‑tubulin using ImageJ.

8. Immunofluorescence: seed 8 000 cells per well on glass‑slide chambers, fix with 4 % paraformaldehyde, permeabilize with methanol, block with 1 % BSA. Incubate with anti‑PR (Santa Cruz sc‑166169) and anti‑GFAP (Abcam ab68428), then with Alexa‑Fluor‑488 anti‑rabbit and Alexa‑Fluor‑594 anti‑mouse secondary antibodies (Invitrogen). Counterstain nuclei with Hoechst, mount, and image on an Olympus BX43F microscope. Include a no‑primary‑antibody control for PR staining. Process images and merge channels in ImageJ.

9. Steroid extraction and LC‑MS: harvest 10 × 10⁶ U87 and 10 × 10⁶ U251 cells, remove medium, lyse by sonication (10 kHz, 10 s pulses, 1.5 min total on ice). Extract progesterone (P4) and its 5α‑reduced metabolite (5α‑DHP) using the protocol in Supplementary Table 1. Prepare calibration curves with P4 (Sigma P8783) and 5α‑DHP (MP Biomedicals 195886). Run samples on LC‑MS using the dynamic MRM method described in Supplementary Table 1 and quantify each steroid.

10. In vivo glioma model in rats (if needed): obtain male Wistar rats (170–190 g) and acclimate for 15 days. Randomize 15 animals into four groups (Untreated n=3, Vehicle n=4, MF 20 µM n=4, MF 40 µM n=4). Anesthetize with ketamine 80 mg kg⁻¹ and xylazine 7 mg kg⁻¹, place in stereotaxic frame, perform a craniotomy at AP 1.6 mm, L 3.0 mm, V 2.0 mm relative to Bregma, and inject 1 × 10⁵ C6 cells in 2 µL PBS into the motor cortex. Seal wound, give gentamicin locally and Baytril in drinking water for 3 days. Ten days post‑implantation, implant a guide cannula at the tumor site and deliver MF (20 µM or 40 µM) or 1 µL vehicle daily for 7 days. Euthanize with pentobarbital 200 mg kg⁻¹, perfuse with saline then 3.7 % PFA, embed brains in paraffin, cut 6 µm coronal sections, stain with H&E, and acquire images on an Olympus BX51‑WI microscope. Estimate tumor volume stereologically (Cavalieri principle) and calculate the Gundersen coefficient of error (must be < 0.1). Perform western blots on tumor tissue as described in step 7.

11. Data analysis: run all statistical tests in GraphPad Prism 8.0.2. Test normality with Shapiro‑Wilk; for normally distributed data use one‑way ANOVA with appropriate post‑hoc (Bonferroni for IC₅₀/IC₂₀, Tukey for protein expression, Dunnett for tumor volume). For non‑parametric data (e.g., questionnaire scores) use Friedman test. Survival curves: log‑rank (Mantel‑Cox). Consider p ≤ 0.05 significant. Report exact n for each experiment in the figure legends.
```

label: 

defect_types: 

notes: 

---

## 59. RCA6962  (growth_curve)

```
We need you to run the OD₆₀₀‑to‑CFU calibration on our four cultures (2 × Positive Control BBa_I20270 and 2 × Negative Control BBa_R0040) using the protocol below. Please follow the steps exactly and return the colony counts and the calculated CFU / mL for an OD₆₀₀ = 0.1 for each culture.

1. **Materials** – use the supplied items: 1.5 mL Eppendorf tubes, 2.0 mL Eppendorf tubes, 96‑well plate, LB broth, chloramphenicol (25 mg mL⁻¹ in EtOH). We will also provide fresh LB‑agar plates with chloramphenicol.

2. **Initial OD measurement** – measure the OD₆₀₀ of each overnight culture in a plate reader (dilute into LB + Cam if necessary to stay in the linear range; e.g., 25 µL culture + 175 µL LB + Cam in a black 96‑well plate, 200 µL total per well).

3. **Dilute to OD₆₀₀ = 0.1** – for each culture prepare three replicate tubes (1 mL total volume) of LB + Cam. Calculate the volume of culture needed using C₁V₁ = C₂V₂, where C₂ = 0.1 and V₂ = 1000 µL. Example: if the measured OD after blank subtraction and dilution factor is 1.224, add 82 µL culture to 918 µL LB + Cam. Verify the resulting OD₆₀₀ is ≈0.1 (repeat the plate‑reader measurement).

4. **Set up serial dilutions** – for each of the 12 starting samples (6 × Positive, 6 × Negative, i.e., three replicates per culture) perform a five‑step 1:10 dilution series:

   a. Prepare three 2.0 mL tubes per sample (Dilution 1, 2, 3) each containing 1900 µL LB + Cam.  
   b. Prepare two 1.5 mL tubes per sample (Dilution 4, 5) each containing 900 µL LB + Cam.  
   c. Label all tubes clearly with sample ID and dilution number.

5. **Execute the dilutions** – for each sample:

   - Transfer 100 µL of the starting 0.1 OD culture into Dilution 1, vortex 5‑10 s, discard tip.  
   - Transfer 100 µL from Dilution 1 into Dilution 2, vortex, discard tip.  
   - Repeat for Dilutions 3, 4, 5 (always using a fresh tip and vortexing after each transfer).  
   - Do not pipette up‑and‑down within the same tube.

6. **Plate the dilutions** – spread 100 µL from Dilutions 3, 4, and 5 onto separate LB‑agar + Cam plates (one plate per dilution per sample). Use aseptic technique; spread evenly and allow the drops to absorb before inverting the plate.

7. **Incubate** – place the plates in a 37 °C incubator overnight (18‑20 h).

8. **Count colonies** – after incubation, count colonies on each plate that contains fewer than 300 colonies. Record the raw count for every plate (include sample ID, replicate number, and dilution factor).

9. **Calculate CFU / mL for OD₆₀₀ = 0.1** – for each plate, multiply the colony count by the total dilution factor (e.g., Dilution 4 corresponds to 1 × 10⁶ total dilution, so CFU / mL = count × 1 × 10⁶). Use the attached Excel template if preferred.

10. **Report** – send us a spreadsheet with the following columns for each replicate: Sample ID, Replicate, Dilution plated, Colony count, Total dilution factor, Calculated CFU / mL (OD = 0.1). Also include any notes on anomalous plates (e.g., >300 colonies, contamination).

Please let us know if any reagents are missing or if you encounter problems during the run. Thank you.
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

