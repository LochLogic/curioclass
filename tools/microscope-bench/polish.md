# Polish: microscope-bench (Codex fix, round 2)

Round 2 is a partial repair, not an exit-gate pass. The open list was Blocker 1 and Should fix 5. The already-repaired items could not be reproduced in their original broken state; they were checked for regression, and no new repair is claimed for them. All frames below are in `_scratch/microscope-bench/`, at 1366x768 unless a size is stated. The Curiosity brief governs: no welcome screen, assessment, score, goal, level or finish was added.

## Blocker

1. **NOT FIXED overall.** Reproduced before editing with `r2-before.json` and `r2-before/` at 4x, 10x, 40x and 100x objectives, including oil for blood. The material blocker remains open despite the following improvements:
   a. **FIXED previously; retained.** The blood still has eight separately cropped fields without the journal montage. New pond cutouts also have transparent Cy/Ma masks; the third panel's scale furniture is masked. See the 37-asset manifest, `r2-cuts.json`, `r2_trim.py`, `r2-after-material/blood-100.png`, and the two new WebPs. No pixels were inpainted.
   b. **PARTIAL.** Existing pond masks remain; the new cheek source glass is alpha-masked, removing its rectangle. Compare `r2-before/cheek-40.png`, `r2-after-material/cheek-40.png` before background removal, and `r2-final/cheek-final.png` after removal. Retained RGB is unchanged. Other finite source patches still fail the broader material requirement.
   c. **NOT FIXED.** Before/after blood at 10x and 100x and root at 10x are still small patches on glass: `r2-before/{blood-10,blood-100,root-10}.png` and the same names in `r2-after-material/`. Root base width is 281.6 um; a blood field is 24.64 um. Those figures are physical source coverage, not targets for arbitrary enlargement. No tissue repetition or invented scale was used to fill the slide.
   d. **FIXED.** Before: 22 placements of four cutouts. After: six distinct cutouts, each once, including three different photographed ciliates. Original figures supplied two additional individuals, with separately measured bars. `r2-static.json` records 6 placements / 6 unique assets; compare `r2-before/pond-4.png` and `r2-after-material/pond-4.png`. `r2-after-material/pond-40.png` shows the central field. There are no stamped duplicates; the Manual discloses the assembled cultures.
   e. **PARTIAL, NOT FIXED overall.** Cheek source sampling improves from 2.377 to 0.22 um/pixel, with approximate scale explicitly stated. Wing remains 9.709, iodine and leaf 3.906 um/pixel. The wing's existing full-file bar measurement is retained; fine hairs remain unresolved. `r2-before/wing-40.png`, `r2-after-material/wing-40.png`, `r2-independent-numbers.json`. The resolution caption remains a fallback, not a claimed source repair.
   f. **NOT FIXED.** Iodine stays a real monochrome camera photograph, captioned MONOCHROME CAMERA. The colour Commons candidate contains an uncalibrated reticle, not a physical scale; it was not assigned invented units or tinted. Before `r2-before/onion-40.png`; after `r2-after-material/onion-40.png`. Its small finite field and the unstained source remain open.
   g. **NOT FIXED.** Existing CIL:43552 and the four separately scaled control close-ups remain. Broader CC0 root candidates could not be fetched: Commons redirect 429, original requests 403, and the origin candidate 410. Their stated magnification alone was not converted into a camera pixel size. The existing approximate base caption and scattered-metaphase note remain. Compare root-10 before/after; `r2-after-material/root-40.png` also shows why this is not a broad meristem hunt.
   h. **FIXED for observation, with a scale limitation.** Replaced the pink Pocket MUSE field with Daliasalloum's actual CC BY 4.0 methylene-blue cheek photograph. At 400x, dark nuclei are visible in the blue cells; observed in `r2-final/cheek-final.png` and `r2-final/preview.png` (680x425). The 0.22 um/pixel scale is inferred from a typical cell edge, not camera-calibrated. SCALE APPROXIMATE is on the eyepiece; the Manual directs precision measurements to the bar-scaled blood fields. This does not repair c or supply an unstained/stained pair of the same cheek cells.
2. **FIXED previously; reverified after the renderer change.** Start remains 10x / +50 um, blur 9.345 px at the main size. Real coarse drags: 40 px up gives +90 um / 11.898 px blur; 12 px down gives +38 um / 8.222 px; 50 px down reaches +0 / zero defocus. See `r2-final/default.png`, `r2-after-controls/focus-{up,down-small,down}.png`, and the matching JSON. Blur at absolute 50/150/250/350 um remains 9.345/14.233/16.636/18.243 px, with the same field-normalized curve. `r2-recheck/phone-default.png` at 375x812 shows FOCUS +50 um with units. No new hint lifetime or lesson flow was introduced.

## Should fix

1. **FIXED previously; retained.** Counts open empty and pressing Store with empty fields stores nothing: `r2-calibration.json` has empty stage/reticle values and `{}` calibrations. True powers remain 3.9/9.8/41/98. Independent source calculation: 42 pixels x 5/28 um/pixel = 7.50 um for the reference red cell; at the true 98x objective that is 7.35 reticle divisions x 1.020408 um/division = 7.50 um. `r2-independent-numbers.json`, `r2-after-controls/calibration-empty.png`.
2. **FIXED previously; retained.** Locator contains glass outline and field circle only, no finds. Seen in pond before/after frames and `r2-final/default.png`.
3. **FIXED previously; retained, not newly repaired.** Focal offsets differ between slides and mounts. Wet onion +12 um, dry +34, bare dry +52 at 10x; pond 0, root -18, blood +8. `r2-controls.json`. Hair's declared gradient and cached depth strips remain; `r2-after-material/hair-40.png`. The prior round's two-ended hair-depth demonstration was not repeated here.
4. **FIXED previously; retained.** Prepare mount stays non-modal beside the live view: `r2-mount.json` reports `modal:false`; `r2-after-controls/mount-live.png` and `r2-final/mount.png` show the eyepiece visible during preparation. The audit checks 375x812 too.
5. **NOT FIXED to the strict 16.7 ms p95 target.** Reproduced at 1366x768 on the headless software-raster proxy: median 15.8 ms, p95 30.6, maximum 31.5. Replaced the per-pan Gaussian blur with a downsampled optical layer and linear reconstruction; the book preview remains skipped when closed. Final same-style proxy: median 16.6 ms, p95 17.8, maximum 18.6; draw-call p95 0.60 ms. rAF timestamp cadence is median 16.7 / p95 16.8 ms, with no doubled interval in that sample, but the original callback-time metric still exceeds 16.7. `r2-before-perf.json`, `r2-perf-probe.json`, `r2-final-perf.json`. This is an improvement, not a claimed Chromebook pass or a changed benchmark threshold.
6. **FIXED previously; retained.** Modal-first Manual and mount-first taps drop the hint as stale instead of speaking over a drawer. `r2-modal-voice.json`, `r2-mount.json`; the actual focus-first walk speaks it once in `r2-voice.json`.
7. **FIXED previously; retained at 375x812.** Tray client/scroll widths both 343 px, wrapping with Place, Wash, micrometer and Sketchbook visible. `r2-phone.json`, `r2-recheck/phone-default.png`.
8. **FIXED previously; retained at 375x812.** FIELD `1.84 mm`, FOCUS `+50 um`, in the value strings and visible on the phone frame. Same evidence as 7.
9. **FIXED previously; retained.** Lamp and Iris are both 44 px high at 1366 and 375. `r2-controls.json`, `r2-phone.json`; the final audit covers short previews as well.
10. **FIXED previously; updated for the new material.** New cheek note opens "Cheek cells: flat cells from inside the mouth." New pond notes open with the animal's everyday name and one visible detail. Scale, culture and masking caveats stay in the slide's Manual source page. No duplicated arm-status note was added. `material.json` and final prepared-tray/cheek frames.
11. **FIXED previously; retained with corrected current licence labels.** All eight applicable discoveries remain, with their named references; no salt entry. Full text is saved in `r2-controls.json`. Re-checking OpenStax found that its current pages state CC BY-NC-SA 4.0, not the old CC BY labels. Those factual-reference labels are corrected in the Manual and draft metadata; no textbook pictures or text passages are bundled.

## Polish accepted

1. **FIXED previously; heard again.** Read says "Pond water, wet mount, no stain, cover slip on. 100 times. Field 1.84 millimetres." `r2-voice.json`; matching mount readout in the default frame.
2. **FIXED previously; retained.** Tray labels are neutral slide labels; no early organism/disease names were added. `r2-recheck/tray.png`, `r2-final/prepared.png`, Manual motion note. Names and original contexts remain on tapped notes and source pages.
3. **FIXED previously; retained.** Thick modelled bubble rims and focus-dependent centres remain. `r2-after-controls/mount-live.png`, final audit mount-preparation frames. Not newly reimplemented.
4. **FIXED previously; updated truthfully.** Notes still say cells, nuclei, focusing and drawing in plain words; the new approximate cheek scale and six distinct pond cutouts are explained. The old CytoStain claim was removed.
5. **FIXED previously; retained for all three swimming cutouts.** Wandering path function is unchanged. Motion off preserves every position and angle across the 500 ms comparison: exact before/after arrays in `r2-motion.json`. The new phases do not create duplicate individuals.
6. **FIXED previously; retained at 1366x768.** All five checked readout/control label groups compute to 12 px in `r2-controls.json`; default frame viewed.
7. **FIXED previously; retained.** Wrapped plate's second line starts `No. 06`, no leading dot. Viewed at 1366, 680x425 and 375x812.
8. **FIXED previously; retained.** After Sound off/on, label is plain `Sound`; `r2-voice.json`.
9. **FIXED previously; retained.** Manual says aperture is "modelled as 0.65" without oil. No new physical measurement is claimed.
10. **FIXED previously; retained.** Corner engraving clears MAG. Default and phone readout frames viewed.
11. **FIXED previously; retained.** Arm status remains available to assistive technology and visually hidden, avoiding a duplicate prose readout. Default and material frames viewed.

## Settled calls

- Real photographs only: no painted cells, tint, generated tissue, inferred fine hairs or repeated tissue tiles.
- Resolution captions remain honest fallbacks; unresolved material is still marked open above.
- First-run hint still disappears after the first focus action. It is not a dismissible welcome or a lesson instruction sequence.
- Manufacturing deviations, calibration method, find-free locator and non-modal mount tray are retained. Input counts are observations, not an assessment to pass.
- Manual, specimen tray and prepared-slide box remain dialogs. Their backdrop coverage is expected; the mount's live eyepiece remains available.
- Source labels and licence details live on source pages. Prepared slide names remain ordinary slide labels.
- Bundle remains below 2 MB; notes has the exact Size line. Blood context remains neutral and source-specific; no health inference is made.
- Turret, knobs, inverted stage, reticle, exact micrometer, oil model, nine-plane colony stack, low-power wing/sand, hair gradient, keyboard model and private sketchbook are retained.
- No curriculum-map change or new salt/sugar/feather topic. The spec's open questions remain open. With nobody available, retained the licensed finite fields and their captions, and explicitly left the material blocker open. No source dimensions were fabricated and the spec was not silently trimmed. This is an honesty fallback, not a claim that the requested broader sources were supplied.

## Cheats tried

- Store calibration immediately with both fields empty: no calibration written. Switching objectives still opens empty fields and uses a separate factor. This is an instrument calibration, not a score or automatic approval; deliberately entering a false count is still the user's false measurement, as the Manual says.
- Locator sweep at low and high power: only slide outline and field circle, no specimen marks to reveal finds.
- Motion off after focus: all six pose records stay identical over 500 ms; no hidden movement timer advances the specimen.
- Lesson-creep search: only `im.complete` (image decode state) and "Collected Letters" (a bibliography title) match the requested terms. Neither is a learning goal, tally or finish. `r2-static.json`.

## Voice walk

Held clicks, 120 ms, two seconds apart: Coarse, Read, Sound off, Sound on, Read. Actual log: "Turn the focus knob." once; then the current mount/MAG/FIELD on each Read, with no organism name. Modal-first Manual path drops the hint as stale. `allLines()` is exactly `["Turn the focus knob."]`, matching `voice/lines.json`. The new prepared cheek mount says methylene blue, not the old stain. No audio was recorded or uploaded.

## The real material

- New cheek: [Daliasalloum, Human epithelial cells stained with methylene blue dye](https://commons.wikimedia.org/wiki/File:Human_epithelial_cells_stained_with_methylene_blue_dye.jpg), CC BY 4.0, checked and raw original fetched 2026-11-06 at 19:28 UTC. Whole 908x823 field, no photographic enlargement in packing; alpha-only source-glass removal and WebP encoding. Original cells, not a synthetic stain. Raw bytes and timestamp: `data/r2-gather.json` and `data/r2-cheek.jpg`; reproducible mask: `r2_cheek_mask.py`.
- Cheek scale is a **size-based inference**, not a known camera calibration: about 250 source pixels across a cell edge, reference 55 um, giving 0.22 um/pixel. [Prasad et al. (2010), Table 1 controls](https://pmc.ncbi.nlm.nih.gov/articles/PMC3001196/) gives 54.97 um, CC BY as stated at source; independently [Romeo et al. (2006)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2732433/) describes mature buccal cells at 50-60 um on edge, author manuscript with no reuse licence stated, factual citation only. No image or text passage from either paper was copied. Individual cells vary; measuring this photograph cannot validate the inference. The blood field remains the independent micrometry reference.
- Additional pond individuals: [Kodama, Kitatani and Morita (2024), Figure 1a](https://pmc.ncbi.nlm.nih.gov/articles/PMC11246328/), CC BY 4.0, rechecked 2026-11-06. Retained original raw download, fetched in the earlier build; two additional crops from its left and right DIC panels. First two panels use 20 um / 69 pixels; right panel's own bar is 20 um / 37 pixels at row 362. Source labels and background are alpha-masked; no inpainting. The source identifies left/middle P. bursaria and right P. multimicronucleatum; field notes stay at the everyday genus name. These are cultured individuals assembled on glass, not a natural abundance survey.
- Observation cross-checks: source photographs/captions plus [OpenStax, Eukaryotic Cells](https://openstax.org/books/biology-2e/pages/4-3-eukaryotic-cells) and [Groups of Protists](https://openstax.org/books/biology-2e/pages/23-3-groups-of-protists), current CC BY-NC-SA 4.0, factual reference only. No textbook data illustration or text passage was imported. The current licence was checked rather than assuming the historical CC BY label.
- Rejected broader root candidates: [BCC apical meristem](https://commons.wikimedia.org/wiki/File:Apical_Meristem_in_Onion_Root_Tip_(34886438470).jpg) and [BCC mitotic field](https://commons.wikimedia.org/wiki/File:Mitotic_Stages_in_Apical_Meristem_of_Allium_Root_Tip_(36762516673).jpg), CC0 as stated, checked 2026-11-06; downloads failed 429/403, origin attempt 410. No failed response was packed as an image. Existing CIL:43552 remains PD, independently checked against its archive entry and the scaled control fields.
- Rejected colour iodine: [Anonymous140209, Iodine stained onion cells](https://commons.wikimedia.org/wiki/File:Iodine_stained_onion_cells.jpg), CC BY 4.0 checked 2026-11-06; prior raw download inspected. Cropable cells exist, but its reticle has no physical calibration. No fabricated um/pixel was assigned. The existing real monochrome source remains honestly labelled.
- Other photographic data and physical bar measurements are retained in `art/manifest.json`, the Manual and `tool.draft.json`; `r2-static.json` verifies all 37 packed asset hashes, scales and allowed photographic licences. Defocus, positions, focal offsets and motion are declared model settings, not new empirical datasets. Gathering stopped within the brief's bounded pass; unresolved sourcing is not claimed as repaired.

## Engine changes wanted

None. No kit or shared-engine edits.

## Audit

The single 2400 s audit finished: **57 leads**, all its mechanical leads accounted for below. Report: `_scratch/microscope-bench/fix-audit/audit.md`. All 30 audit frames were inspected on the three contact sheets, with the phone Manual and 1000x625 frame also opened individually. Required sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and the 375x812 iframe.

- Eight default-screen hint/eyepiece overlaps: the designed first-run hint on the instrument, a settled call.
- View/hint text and keep regions covered under Manual, Sketchbook, specimen/prepared dialogs: expected modal coverage. Calibration can cover the knob bank while keeping the live scales visible; the phone mount tray can cover part of the knob bank while keeping the eyepiece visible. These are the existing drawer layouts, not clipped eyepieces.
- Phone Manual's reported Reading-the-instrument / closed Making-a-mount paragraph overlap: false positive from closed details content. `fix-audit/state-manual-375x812.png` shows separate visible summary rows with no drawn paragraph overlap.
- Hint out of view after focusing in calibration, colony and sand states: correct first-action dismissal, a settled call.
- Six drawer-first taps without the hint: correct `valid` rejection. This is the Should fix 6 repair working; a Curiosity has no required spoken premise over a modal. Read speaks its current readout instead, and Sound off may cut speech.
- Five held-click repetitions and quick two-tap checks: clean. Motion off: clean. Resize and disabled-control stress checks: clean. The audit does not test tissue coverage, source resolution or a physical Chromebook; it cannot close the open items above.

One additional defect was found by looking at the audit's 680x425 frame, not by its lead counter: Rotate and Calibrate were partly below the footer. **FIXED.** A short-window-only CSS rule reduces gaps and decorative dial/text dimensions while preserving 44 px targets. Before: `fix-audit/size-680x425.png`. After: `r2-preview-recheck/preview-680x425.png`; both buttons are now 44 px high, bottom y=334 with footer y=359, leaving 25 px. Lamp/Iris have 19 px clearance. The same targeted re-check at 800x500, 1000x625 and 1366x768 has nonnegative clearance for every measured control, 44 px or larger targets, no console errors and zero network resource entries. These four frames were inspected individually. This small CSS correction was made after the audit's host snapshot; the audit was not rerun. It affects neither the material nor the 1366 performance probe.

## Left open

- Blocker 1c/e/f/g: broad real tissue fields, fine wing and leaf detail, colour iodine with defensible scale. The new cheek nuclei and unique pond individuals do not make this whole blocker fixed.
- Should fix 5: callback-time p95 still 17.8 ms against the strict 16.7 ms target; no physical Chromebook run was available.
- No new ten-minute student/adult short-test pass or model-comparison pass is claimed. The real-material failures still prevent an exit-gate pass, even though the controls remain usable and free of a score or finish.
- Spec questions about curriculum mapping and omitted tray materials remain with the spec. No external contact, upload, purchase or publish action was made.

## Verification record

Only `tools/microscope-bench/` and `_scratch/microscope-bench/` were written. No git commits; `refine.md` was not edited. Final source/asset provenance and before/after numbers are retained in Scratch. Long commands used `run.py`: bundle 120 s, drive batches 300 s (outer 320 s), audit 2400 s; downloads had 18-20 s request limits. Initial short read-only discovery commands preceded that process-tree wrapper and finished within their first tool yield.

All before, after-material, controls, final-mode and phone frames were looked at, including their contact sheets. Final cheek, phone, focus, 1000x625 and phone-Manual frames were also inspected individually. The only console error in a local shot was the Scratch host's favicon 404; the host was corrected and the same phone check rerun with no errors and zero instrument network resource entries. No product code was changed for that harness issue.

Final bundle: **1,613,120 bytes**, 37 photographic assets / 1,089,408 asset bytes. Final source tokens, asset hashes, allowed photographic licences and numeric scales agree. All owned Chrome ports 9920-9927 and host 8725 are closed. Unchanged refine SHA-256: `c0420015725a38be39c749e04f995025e4e664ae373844dcc7f5b4b0a39393bb`. The bundle and notes retain the size reason; no gate pass is claimed.
