# Refine lens: Teaching, microscope-bench (Curiosity No. 06), round 1

Judged against CODEX-CURIOSITY.md and VISION.md "Curiosities: the second shape", plus spec.md. My frames are in
`S:/CurioClass-codex-scratch/microscope-bench/teaching/f1/` (1366x768, calm, each slide focused at 0 µm and centred on
a specimen via `__tool`). The eyepiece crops are gathered in `teaching/sheet1_0.png` to `sheet1_5.png`. Source art
converted to PNG is in `teaching/art/`.

Counts: blocker 1, should fix 7, polish 5, nit 2.

## Blocker

**B1. Published-figure lettering and furniture sit on the specimens in the eyepiece.** (family:curiosity)
- Where: `art/paramecium.webp`, `blood.webp`, `diatom.webp`, `rotifer.webp`, `wing.webp`, `plane*.webp`. Drawn by `photograph()`, src.html:1083.
- What: the crops still carry the source figures' labels and layout:
  - Paramecium: the default pond slide's swimming paramecium carries the labels "Cy" and "Ma", mirrored by the inverted image. These are the source's labels for cytopharynx and macronucleus (Kodama et al., Fig. 1 caption).
  - Blood smear: the slide is the whole published figure. It shows panel letters A to H (mirrored), white gutters between the panels and eight 5 µm scale bars.
  - Diatom: all five diatoms keep the source's pale circular vignette, which shows as a yellow disc around each one.
  - Others: the rotifer tile keeps "B", the wing keeps "2" and the colony plane keeps a corner numeral.
  - Tile edges: every tile's own background shows as a hard rectangle on the glass (the paramecium, the mat patches and the root cells).
- Why it matters: in a Curiosity the real material is the interface. A slide that shows printed figure letters is a dataset presented as something it is not. "Ma" also names a cell part before any tap, which breaks Done when 6.
- Seen: `f1/pond-para-400.png`, `pond-para-1000.png`, `blood-1000.png`, `pond-diatom-400.png`, `pond-diatom-100.png`, and `teaching/sheet.png`.
- Fix: re-crop or mask the labels, bars, gutters and vignette from the source pixels (crop inside each panel). Present the blood as eight separate fields spread across the glass. Feather the tile edges into the glass background.

## Should fix

**S1. The root-tip slide is four isolated dividing cells, one per phase, with no interphase cells and no tissue.** (general)
- Where: material.json, slide `root` (root0 to root3).
- What: at 40x and 100x total the slide shows four dots on empty glass. At 400x each one is a single mitotic figure on a grey rectangle. Tapping names the phase.
  - Things to do 13 ("hunt for a cell caught in each stage") has nothing to hunt.
  - The spec's own fact ("most cells are between divisions, so the dividing ones are rare finds") is inverted: every cell on this slide is dividing.
  - The "Metaphase" note says "Chromosomes gathered across the cell", but root1 shows a scattered squash spread, not a plate.
- Source check: Çavuşoğlu Fig. 4 really is normal control mitosis, Feulgen stain, CC BY 4.0. The images are honest; the slide built from them is not.
- Why it matters: this is the tool's whole reach into science-9-cell-division-and-differentiation.
- Seen: `f1/root-40.png`, `root-100.png`, `root-meta-400.png`, `root-pro-1000.png`.
- Fix: use a real meristem field with many cells. The spec names CIL:43552, onion root tip, public domain. Keep these four as close-ups placed inside it. Fix the metaphase note to describe what is shown.

**S2. Empty magnification on most slides, and the readouts still say the view is in focus.** (family:curiosity)
- Where: assets with coarse source sampling: sand 7.1 µm/px, wing 9.7, cheek 3.9, onion iodine 3.9, leaf 3.9, onion clear 2.1.
- What: at 400x one screen pixel is about 0.9 µm, so these photos are stretched 2 to 10 times and turn into soft blur. FOCUS reads +0 µm and nothing on the instrument says why the view is blurry.
  - The field guide names things only at 40x and above, which is exactly where these slides become blurs.
  - Things to do 9 (the fine hairs on the wing) cannot be done.
- Why it matters: a student learns that more power means more blur, the opposite of the real instrument.
- Seen: `f1/wing-400.png` vs `wing-40.png`, `sand-400.png`, `cheek-400.png`.
- Fix: add an on-instrument caption like the existing "REFLECTED-LIGHT SOURCE" one (for example "SOURCE RESOLUTION LIMIT") whenever upscaling passes about 2x. Better: find higher-resolution sources, or let the field guide answer at 10x on these slides.

**S3. Cell parts are barely visible, and MS-LS1-3 is not exercised.** (general)
- Where: the slides `cheek`, `onion`, `root`.
- What:
  - MS-LS1-1 (living things are made of cells) is exercised well: onion walls, Hosta epidermis, pond single cells, blood.
  - MS-LS1-2 (cell parts): no ordinary interphase cell shows a clear nucleus. The cheek is pale pink smudges with no nucleus (`cheek-400.png`), so Things to do 4 cannot be done. The iodine onion shows at most a faint ring (`onion-iodine-400.png`). The root tip shows only chromosomes. The only chloroplast-like bodies are the algae inside the paramecium.
  - MS-LS1-3 (body systems built from cells) is not exercised at all. The spec admits this.
- Fix: list the tool against MS-LS1-1, plus MS-LS1-2 only once a field really shows a nucleus. A cheek or onion source that resolves nuclei at 400x would earn it. MS-LS1-3 stays with the module's lesson tool.

**S4. Calibration is a no-op that can be passed without looking.** (general)
- Where: src.html:1182 (reticle spacing `d/180`), 1488-1489 (count fields filled in advance), Manual at 721.
- What:
  - The reticle is drawn at exactly the nominal factor (100 µm divided by objective power).
  - The dialog arrives already filled with the right counts (10 micrometer intervals and N reticle intervals, where N is the objective power).
  - One tap on "Store calibration" switches SCALE from "nominal" to "calibrated" with the identical number.
  - The Manual even gives the 4x answer ("ten micrometer intervals span four reticle intervals").
- Done when 4 passes only because nominal is exact. I recomputed: a red cell spans 42 source pixels × 0.1786 µm = 7.5 µm, so 7.5 divisions at 1000x. That is within 20 percent of the textbook 7 to 8 µm.
- Why it matters: the reason real microscopists calibrate (the nominal value is off) is never met, so the student learns a ritual.
- Seen: code check, and the frames `f1/micro-40-ret.png` and `micro-400-ret.png`.
- Fix: give each objective a realistic true magnification that differs from its nominal one (for example 3.9x, 9.8x, 41x, 98x), so the stored factor differs from nominal. Leave the count fields empty. Drop the worked answer from the Manual.

**S5. The iodine comparison changes the camera, the colour and the scale all at once.** (general)
- Where: material.json, slide `onion`, `objects` vs `iodine`.
- What:
  - The unstained field is strongly blue: Ogasawara Fig. 9a was lit by RGB LEDs.
  - The "iodine" field is grey, not amber, and is an 85x80 px patch.
  - Pressing Iodine therefore turns the onion from blue to grey. The spec's Look wants iodine amber-brown, and the iodine bottle on screen is amber.
- Why it matters: Things to do 3 ("compare what appears") teaches the wrong colour, and no nucleus clearly appears.
- Seen: `f1/onion-clear-400.png`, `onion-iodine-400.png`, `onion-iodine-100.png`.
- Fix: find a colour Lugol onion field (PD or CC BY), or at least caption the views on the instrument ("source colour cast", "monochrome camera").

**S6. The field-guide notes are written for a microscopist, not a grade 6 student.** (general)
- Where: material.json `note` fields, src.html:1426-1436.
- What:
  - Jargon: "Green endosymbiotic algae fill this photographed ciliate", "pennate diatom", "bdelloid rotifer", "Microcoleus-dominated freshwater mat", "erythrocytes", "Biogenic aragonite".
  - Every reused copy also carries provenance text ("Separate photographic patch, not an original contiguous pond field. Reused photographic patch.").
- Fix: open each note with a plain sentence, for example "A paramecium: one cell that swims. The green dots are algae living inside it." Then one real detail. Move provenance to the slide's Manual page, which already holds it.

**S7. "Things people have found" dropped every fact the spec listed.** (general)
- Where: src.html:747-754.
- What: the spec's entries are gone: Hooke and "cells" (1665), Leeuwenhoek's animalcules (1676), why rotifers are named for wheels, red cells 7 to 8 µm, salt cubes, dividing cells being rare in a root tip, oil index about 1.52, the flipped image. Only five instrument observations remain.
- Why it matters: the cell-history entries are where MS-LS1-1 gets its human story.
- Fix: restore the spec's entries that apply to the slides that exist. Leave out salt, which was cut from the tray.

## Polish

**P1. The tool opens at the 40x objective (400x total).** (family:curiosity)
- Where: src.html:992.
- What: the Manual says "Scan at low power before changing the objective", and real practice starts low. At 400x the swimming paramecium leaves the 0.45 mm field quickly.
- Better: open at 10x (or 4x) on the blurry pond; the first focus turn still sharpens it.

**P2. Read says "Pond water, water, none, covered."** (general)
- Where: src.html:1040.
- What: "none" (no stain) and "covered" are unclear when heard. The spec's model line is "Onion skin, iodine, one hundred times, field one point eight millimetres".
- Better: "Pond water, wet mount, no stain, cover slip on".

**P3. Names appear before a tap.** (family:curiosity)
- Where: tray descriptions in material.json and Manual 735-736.
- What: the colony card says "fixed Volvox colony" and the blood card says "malaria parasites" before anything is tapped. The Manual's motion note names paramecium and rotifer.
- Better: keep tray cards to the slide's own label ("Pond colony, fixed, focal series") and name organisms only in the field guide and the source pages.

**P4. Air bubbles are drawn as thin 1 px circles.** (general)
- Where: src.html:1100-1103.
- What: one circle even sits off the specimen. The spec asks for "thick black rings that are not cells"; these read as drawn circles, not bubbles.
- Better: a thick dark rim with a bright centre that changes with focus.
- Seen: `f1/bubbles-100.png`.

**P5. The notes.md teacher sections are written for experts.** (general)
- Where: notes.md, "What it teaches" and "Key skills".
- What: "What it teaches" never says "cells". "Key skills" uses build jargon ("nine registered planes of a fixed pond colony").
- Better: plain words: "see that onion, leaf, cheek and pond life are made of cells; measure a cell in micrometres; see chromosomes in dividing cells". The Support at home ideas are doable tonight.

## Nit

**N1. Crane-fly wing scale.** (general)
- Where: material.json, asset `wing`.
- What: the tile is 13.8 mm wide and the Manual says "about 14 mm". ZooKeys 1040 gives Tipula dechangensis wing length as 14.3-15.5 mm (males) and 15.1-16.8 mm (females). The scale bar was measured on a thumbnail, so the wing may be about 5 to 15 percent small.
- Fix: re-measure on the full-resolution file.

**N2. The 100x objective without oil is limited to aperture 0.65.** (general)
- Where: Manual 711-712, src.html:1004.
- What: the 0.65 figure is a modelling choice, but the Manual states it as a fact.
- Fix: say "modelled as".

## Done when (Teaching view)

1. PASS. No welcome screen. On the blurry pond, one coarse step down sharpens it (`audit-r1/size-1366x768.png`, `f1/pond-para-400.png`).
2. FAIL. Every choice changes the view, but several show figure furniture (B1), and the iodine view does not look like iodine (S5).
3. PASS on licences. I spot-checked the sources below. The Manual credits every image.
4. PASS, but only because nominal equals true (S4). A red cell measures 7.5 µm at 1000x.
5. PASS. The image moves opposite to the stage. 100x without oil is dim and soft (`f1/pond-1000-nooil.png`).
6. FAIL. The tool never asks a question, and a search for the lesson-creep words is clean. But "Ma" labels a part before any tap (B1), and tray text names organisms before a tap (P3).
7 to 9. Not this lens (Craft and Play).
10. Not this lens.
11. PASS. There is no score, goal, level, sticker, collection count or finish screen.

## Fact spot-check (second source or recomputed)

| Fact | Check | Result |
|---|---|---|
| FIELD 4.50 / 1.80 / 0.45 / 0.18 mm | 18 / objective power | OK |
| DEPTH 55.0 / 8.8 / 1.3 / 0.5 µm | 0.55 × n / NA² | OK |
| Oil index 1.515 | standard immersion oil 1.515 to 1.518 | OK |
| Red cell about 7.5 µm | 42 px × 5/28; OpenStax 7 to 8 µm | OK |
| Neubauer fine square 50 µm | standard 0.05 mm | OK |
| Root tip Fig. 4 is normal control mitosis, Feulgen, CC BY 4.0 | PMC10960845 caption | OK |
| Paramecium Fig. 1a labels | caption "Cy, cytopharynx; Ma, macronucleus" | the labels are in the crop (B1) |
| Blood Fig. 1: 5 µm bars, trophozoites A to F, schizont G, gametocyte H | EID 15(9) caption | OK; every cell shown is infected |
| Onion Fig. 9a brightfield, 100 µm bar | PMC6975239; lit by RGB LEDs | OK; explains the blue cast (S5) |
| Wing about 14 mm | ZooKeys 1040: 14.3 to 16.8 mm | slightly low (N1) |
| µm per pixel for all 13 sources | recomputed from each bar/px statement | all match material.json |

## Sensitivity

Nothing cultural, Native or hard-history, so no sensitivity agent is needed under rule 5. The blood slide is a published
malaria sample. It is labelled neutrally, and notes.md names it under Sensitivity. Rule 8 is met if the teacher notes
keep that line.

## Audit pilot

- Leads confirmed: none of the audit's leads are teaching items. Its layout leads (the hint over the view, covered regions in drawers) are left to Play and Craft.
- Leads wrong: none checked.
- What it missed (it cannot see pixels' meaning):
  - the figure labels on specimens (B1);
  - the empty magnification (S2);
  - the calibration that can be passed without counting (S4);
  - the root-tip slide that is all dividing cells (S1);
  - the iodine colour (S5).
- The audit's Read row ("Pond water, water, none, covered. 400 times.") did surface P2's wording and the 400x opening objective.
