# Codex review: microscope-bench

## Played

Cold grade-6 and adult lens: focused the pond, panned and chased photographs, changed objectives/oil/light, prepared onion mounts, calibrated, inspected depth, and drew observations. The physical bench, private book and real images are strong. Builder notes and source were opened only after the cold drive.py play batches. One review/fix pass, with targeted rechecks.

## Findings fixed

- **Blocker, general, field guide:** a fully closed iris still identified a photographed organism. It now reports the closed iris; lamp zero reports the unlit lamp. Optical/stage edits clear stale notes and their status text.
- **Should fix, general, calibration:** the modal covered the scales and locked the instrument. The existing controls now sit beside the live eyepiece; drag/arrow panning remains available. Objective changes and other drawers close it. Escape and the Calibrate button close it. The compact button row was rechecked after reducing its spacing.
- **Should fix, general, source truth:** sand was labelled transmitted light despite its reflected-light photograph. Desktop caption and an eyepiece readout now retain source contrast at compact sizes; the fixed colony also retains its darkfield label.
- **Should fix, general, attribution:** damaged author spelling and scale symbols in the Manual/metadata, and a stale 63-pixel bar value. Rebuilt credits from the canonical catalog (64 pixels), adding SPIE/Optica DOI and journal attribution. No pixels, physical sampling or specimen arrangement changed.
- **Should fix, general, mount status:** preparation changes could leave the previous unstained mount in the status readout. The status now follows water, stain, cover and bubble changes.
- **Blocker, general, keyboard transfer:** the drawer close event stole focus from the eyepiece. Real Enter/Enter reopened the tray instead of placing the selected onion. Close-to-stage workflows now preserve an explicit eyepiece focus destination.
- **Polish, general:** restored a plain engraved Motion label after kit initialization/toggles.

## Findings left

No known blocker or should fix remains. Finite isolated fields, visible photographic edges/annotations and limited source resolution remain explicit material limits. Broader contiguous tissue and unresolved ciliary/hair/wing detail need more qualifying source material, rather than invented anatomy.

## Break it

- No score, check, quiz, progress meter or finish state exists. No pass cheat applies. Calibration is the user's measurement, not an automatic correctness claim.
- Actual Home/End keys reached coarse 0/10 mm, fine -50/+50 µm and both stage axes -10/+10 mm. Lamp/iris reached 0/100; fifty rapid stage keys produced 2.50 mm. Empty glass, all eleven slide choices and resize while running produced no exceptions or nonfinite readouts.
- Closed-iris identification repro now gives only “The iris is closed”; changing objective dismisses the prior note. Dry 100× retains the declared dim/soft model; oil uses the source-based aperture/index relationship.
- Empty, zero, negative, over-range and nonfinite calibration counts disable storage. Injecting `1e999` produced Chrome's expected input-parser warning, not a tool exception.
- Swimming clock advanced from 0 to 0.316678 s, then stayed exactly 0.316678 with Motion off. A preliminary helper toggled a persisted Off setting On; its failed freeze comparison was rejected and the explicit-state check replaced it.
- Keyboard drawing and a note survived reload. All nine depth planes rendered distinctly. Pencil, label pin, eraser and Undo were exercised with real keys/clicks; counts changed [1 stroke, 1 label] → [0, 0] → [1, 1]. Print-media rendering shows only the observation, label, magnification/date and notes; a physical printer was not used.
- Evidence: `review-check/results.json`, `review-final/results.json`, `review-postfix/results.json`, `review-small.json`, `review-provenance.json`, `review-static.json` in Scratch. No automatic external requests in instrument checks. Real Enter/Enter now selects then mounts onion with focus on the eyepiece at desktop and 375 px; nine preparation states have matching status text.

## Voice walk

Held clicks, Sound on, about two-second pacing: focus knob → focus turn → Read → tray/onion/place → Read → five repeated objective taps. Log order: “Turn the focus knob” once (hushed when focus made it obsolete), pond mount/400 times/0.45 mm on Read, then onion mount/400 times/0.45 mm on Read. Actions otherwise stay quiet as the Curiosity brief requires. No untapped biological identification is narrated. Bank is science-narrator; browser speech fallback, no recorded clips. Audible quality was not assessed in muted Chrome.

## Facts checked

Review date: 2026-11-05 Denver / 2026-11-06 UTC. Each listed source remains linked with its credit/licence in the Manual and `tool.draft.json`. Existing image fetch times, raw/packed hashes, measured bars and cropping stay in `art/manifest.json`. No new photographic material was gathered.

| Material / claim | Named source, rights and check |
|---|---|
| Paramecium, algal inclusions, 20 µm bar | Kodama, Kitatani & Morita, [2024 paper Fig. 1a](https://pmc.ncbi.nlm.nih.gov/articles/PMC11246328/), CC BY 4.0. Movement is code, not recorded. |
| Rotifer identity, 50 µm bar | Zeng et al., [ZooKeys Fig. 3B](https://commons.wikimedia.org/wiki/File:Adineta_beysunae_(10.3897-zookeys.941.50465)_Figure_3.jpg), CC BY 4.0; photographic panel only, no claim of beating cilia. |
| Diatom, 20 µm bar | Sándor Bancsó, [Pinnularia viridis](https://commons.wikimedia.org/wiki/File:Bancs%C3%B3_2021_Fig_7-8_Pinnularia_viridis.jpg), CC BY 4.0. |
| Filament patch | Tee et al., [Microcoleus mat Fig. 4b](https://commons.wikimedia.org/wiki/File:41396_2020_676_Fig4b.jpg), CC BY 4.0; source plate and 20 µm bar inspected. |
| Hair and counting grid | Jeffrey M. Vinocur, [hair photograph](https://commons.wikimedia.org/wiki/File:Hemocytometer_grid_with_human_hair_100x.jpg), CC BY 2.5 selected from its multiple licences. Standard 50 µm pitch is an explicitly stated inference, checked against Marienfeld and ZEISS. |
| Sand location, composition and reflected light | Sara Beth Kopczynski / James St. John, [French Bay photograph](https://commons.wikimedia.org/wiki/File:Marine_biogenous_aragonite_sand_(modern%3B_sandy_beach_at_French_Bay,_San_Salvador_Island,_Bahamas)_(48739969587).jpg), CC BY 2.0; 2 mm bar. |
| Wing identity and 2 mm bar | Men, Starkevich & Saldaitis, [ZooKeys panel 2](https://commons.wikimedia.org/wiki/File:Tipula_dechangensis_(10.3897-zookeys.1040.64376)_Figures_1,_2.jpg), CC BY 4.0; current Commons API metadata confirms crane fly and panel scale. |
| Unstained onion, 100 µm bar | Ogasawara et al., [JBO Fig. 9a](https://pmc.ncbi.nlm.nih.gov/articles/PMC6975239/), CC BY 4.0; brightfield panel and DOI checked. |
| Iodine onion and Hosta fields | Christopher et al., [BOE Figs. 5/6](https://pmc.ncbi.nlm.nih.gov/articles/PMC11019669/), CC BY 4.0; original source preparations, 250/50 µm bars and commercial-lens crops checked. Different fields, not registered before/after cells. |
| Cheek preparation, 300 µm bar | Liu et al., [Pocket MUSE Fig. 8a](https://pmc.ncbi.nlm.nih.gov/articles/PMC7955119/), CC BY 4.0; source XML/current page confirms CytoStain plus propidium iodide and brightfield, not methylene blue. |
| Root stages and Feulgen stain | Kürşat & Dilek Çavuşoğlu, [Scientific Reports Fig. 4a-d](https://www.nature.com/articles/s41598-024-57762-z), CC BY 4.0; control phases and 10 µm bar checked against caption and independently [OpenStax cell cycle](https://openstax.org/books/biology-2e/pages/10-2-the-cell-cycle), CC BY 4.0. |
| Blood and parasites, 5 µm bar | van Hellemond et al., [CDC EID Fig. 1](https://wwwnc.cdc.gov/eid/article/15/9/09-0358_article), [public domain](https://wwwnc.cdc.gov/eid/page/copyright-and-disclaimers). Retains infected-sample context; no diagnostic inference. |
| Fixed Volvox, nine planes, 25 µm steps | Xiao et al., [Supplement Fig. S9b](https://doi.org/10.6084/m9.figshare.12964487.v3), CC BY 4.0, reconfirmed by current Figshare API. Original supplement confirms Eukitt, darkfield/pseudocolour, 100 µm bar. |

- Independent arithmetic: total MAG 40/100/400/1000×; FN 18 fields 4.50/1.80/0.45/0.18 mm; nominal reticle 25/10/2.5/1 µm. [Nikon field formula](https://www.microscopyu.com/microscopy-basics/field-of-view) and [Rice measurement](https://www.ruf.rice.edu/~bioslabs/methods/microscopy/measuring.html), copyrighted factual references only.
- Depth's declared wave term gives 55.0/8.8/1.3018/0.53328 µm, following [Nikon depth](https://www.microscopyu.com/microscopy-basics/depth-of-field-and-depth-of-focus). Full optics and photographic blur remain approximations. Oil/contrast checked against Nikon and independent Rice/ZEISS guidance; no reference text or diagrams copied.
- Blood source: 42 px × 5 µm / 28 px = 7.5 µm, within 20% of [OpenStax's 7-8 µm](https://openstax.org/books/anatomy-and-physiology-2e/pages/18-3-erythrocytes) and Clinical Methods' 7.5 µm. Rendered scale follows the same physical sampling.
- All 27 packed and original hashes match the manifest; asset sampling matches the embedded catalog. Licences are PD or CC BY individually, not inferred from NIH/Commons hosting. Evidence: `data/review-fact-evidence.json`, `data/review-{wing,stack,cheek}.txt`, `review-provenance.json`.

## Sensitivity

Human hair, cheek cells and a published malaria blood smear concern people's bodies. Retained the disease context without implying that the viewer is ill or that this is a normal-blood atlas. A later sensitivity lens should check that context and accurate author names. No person, patient portrait or culturally representative illustration appears.

## Flattest moment left

Finite photograph edges and small isolated cell fields can end a scan in empty glass. The locator and honest coverage are retained. The lifted moment is calibration: actual scales remain visible and movable instead of disappearing behind arithmetic. Keep the material, not a reward system, central.

## Short test

- **Would a kid open it unassigned? PASS:** one focus detent reveals real pond material; preparation and stage hunting answer immediately.
- **Would an adult play for fun? PASS:** the focal series, micrometry and sand texture sustain instrument exploration; the library is finite.
- **Is the real thing the interface? PASS:** photographs at physical scale and two live scales carry the activity. Model limits stay declared.
- **Does it work without score/finish? PASS:** all specimens and controls are open; the student's sketch is the only record. These are reviewer judgments, not a human usability study.

| Microscope Bench | Elements Inspector reference |
|---|---|
| ![Real sand and micrometry](../../_scratch/microscope-bench/review-audit/state-sand-source-contrast-1366x768.png) | ![Elements Inspector](../../_scratch/microscope-bench/review-small/elements-reference.png) |

## Graphics

Kept the enamel instrument, knurled knobs, physical reticle, private sketchbook and all 27 licensed crops/planes. Inspected the photographic inventory, raw scale evidence, cold frames and focused desktop/phone/grayscale frames. No generated or repainted scientific material. Bundle 1,361,131 bytes (1.361 MB). Contrast: cream/bench 7.18:1, readout 11.32:1, tray 10.91:1, links 7.32:1. Source/voice creep search finds only `im.complete`, an image-load property. No goal, score, level, quiz, kit header or finish screen.

## Audit

One complete audit, 40-minute stopper, Chrome 9951 / host 8755: `review-audit/audit.md`, **62 leads and 30 inspected frames**. All STANDARDS sizes, listed states, Motion off, held-click walks, repeated/rapid taps and mid-action resize finished. No runtime errors, stuck controls or unwanted control jumps were reported.

Disposition of every lead family: the quiet first-use hint intentionally overlays the eyepiece; its disappearance after focus is required, not a lost hint. The 375 px tray is the spec's scrolling shelf. Native modal drawers intentionally cover/inert the underlying keep regions. Calibration temporarily covers the phone arm while retaining live view panning and a visible Cancel; focus is set before measurement. The Manual's collapsed-details paragraph/summary rectangle does not paint an overlap in its inspected frame. Sound deliberately stops speech; a first Read deliberately skips the welcome.

Own frame inspection also caught the clipped compact source label; its inset now follows the circular clip. Final preparation-status and keyboard-focus corrections have targeted desktop/phone/preview rechecks in `review-postfix/`; the audit was not repeated after them. The earlier failing keyboard repro is retained in `review-keyboard-transfer/result.json`. No known blocker or should fix remains. All owned Chrome/host ports were closed before this report. Final bundle SHA-256: `76ec53c19e099c2dc1d9ec9136cd3639654a54222144f49f4df911cf87fc1b53`.

## Left open

- Spec item 8: keyboard access passes; physical school Chromebook 60 fps and human grade-6/adult feedback remain untested; desktop/headless checks are not hardware or human validation. Browser fallback voice quality and physical printing remain unverified.
- Spec's explicit curation fallback retains omissions: salt, sugar, feather and methylene-blue cheek preparation. No placeholders or fabricated substitutes added.
- Took the spec's unattended lean: preserve licensed source preparations/scales and disclose finite coverage; fix locally, no shared-kit changes or new topics. No questions, uploads, commits or out-of-scope writes.
- Initial read-only commands used yield limits before the explicit wall-clock wrapper was installed; later bundles, browser batches and the audit have 120/300/2,400-second stoppers. Nested-shell quoting and unavailable Pillow were corrected by bounded helpers/browser inspection, without installs.
- The final report was staged in Scratch until checks finished, because writing `codex-review.md` is the user's immediate stop condition.
