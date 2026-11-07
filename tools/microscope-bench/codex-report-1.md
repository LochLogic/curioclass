# Codex report: microscope-bench (Curiosity No. 06)

## Built

Built a working, offline compound microscope control surface and observation book. **This is an incomplete build, not the specified biological Curiosity ready for release.** Photographic material could not be retrieved, so the bench opens on the exact stage micrometer instead of pond water. No substitute organisms, cells or specimens were painted.

The instrument fills the window with its own bench, eyepiece, enamel base, objective turret, coarse/fine focus dials, inverted X/Y stage, lamp, iris, immersion-oil switch and rotating reticle. The lower-left engraved plate reads Curio Class Curiosities · No. 06 · Microscope Bench. Manual and a separate Motion, Sound and Read power panel retain the family marks.

The sketchbook supports pointer and keyboard drawing, erasing, label pins, notes, pages, date and magnification, local saving, reload and printing. The phone book includes a live eyepiece thumbnail. Privacy is stated on screen.

The bundle is **77,598 bytes (75.8 KiB)** against the 2 MB goal. The planned roughly 4 MB photo budget was not used because its material is absent. This small result is not evidence of successful micrograph compression.

Authored files are confined to `tools/microscope-bench/` and `_scratch/microscope-bench/`. No commits, branch operations, publishing, shared-engine edits or polish round. The report was deferred until the end because the user's stop-on-report instruction takes precedence over the regular brief's early-report instruction.

## The real material

There are **zero bundled photographic datasets**. `art/manifest.json` distinguishes source candidates from accepted images. Metadata and licence pages were checked on 2026-11-05; no photographic binary was successfully fetched or sampled.

| Candidate | Source, stated licence and credit | Decision |
|---|---|---|
| Onion epidermis | [Onion Cells.jpg](https://commons.wikimedia.org/wiki/File:Onion_Cells.jpg), CC BY 2.0, kaibara87 | Not included. Download blocked; physical pixel scale not supplied. |
| Onion root tip | [CIL:43552](https://www.cellimagelibrary.org/images/43552), Public Domain, Shoba Shanti, DOI 10.7295/W9CIL43552 | Not included. Page gives a 40×/0.65 NA objective but unknown pixel sizes. Objective power alone does not establish digital µm/pixel. Download also blocked. |
| Pond organism | [Paramecium Bursaria.jpg](https://commons.wikimedia.org/wiki/File:Paramecium_Bursaria.jpg), author-released public domain, Cucumberkvp | Not included. No verified physical pixel scale or locally available photo. |

Shell requests failed with Windows socket restrictions. PowerShell retrieval also failed. The interactive browser host was unavailable. A bounded attempt through Chrome's ordinary network stack recovered its error-page sprite, not a micrograph. Those raw PNG bytes remain in Scratch under misleading requested `.jpg` names as failure evidence and are excluded from the tool. No security protections were changed to obtain data. Gathering was stopped within the 45-minute allowance.

The one material on the stage is the spec's permitted code-drawn micrometer: 1 mm, exactly 100 intervals of 0.01 mm. The 10 mm/100-division eyepiece reticle stays fixed in the eyepiece plane. Both geometries are original code. No external illustration or prose passage is reproduced.

The Manual and metadata name these factual references and their rights status:

- [Nikon MicroscopyU: objective properties](https://www.microscopyu.com/microscopy-basics/properties-of-microscope-objectives): field-number relationship and objective optics. Copyrighted reference only.
- [Nikon MicroscopyU: depth of field](https://www.microscopyu.com/microscopy-basics/depth-of-field-and-depth-of-focus): the wave-optical term implemented here. Copyrighted reference only; the readout says estimated.
- [Nikon MicroscopyU: reticle calibration](https://www.microscopyu.com/tutorials/reticlecalibration) and [Rice University: measuring with the microscope](https://www.ruf.rice.edu/~bioslabs/methods/microscopy/measuring.html): independently checked calibration method. Copyrighted references only.
- [Merck: measuring eyepiece calibration](https://www.merckmillipore.com/Web-IN-Site/en_US/-/EUR/ShowDocument-Pronet?id=201605.071): independent 0.01 mm stage-interval reference. Copyrighted reference only.

FN 18, eyepiece 10×, objective apertures, reference focus and oil index are explicit model parameters. Computed blur and illumination are approximations, not measured optics or a focal stack. Historical and biological Manual vignettes that were not independently confirmed were omitted. Its discovery entries describe observable instrument behavior instead.

Reproducibility: Scratch holds `gather.py`, `browser_gather.py`, request lists, raw failure evidence and `pack_material.py`. The packer requires an accepted licence, attribution and physical scale evidence. It correctly reports no approved images and creates no image package.

## Break the instrument

`_scratch/microscope-bench/checks.json` records PASS for the available instrument. Inputs used actual CDP keys, held clicks and a jittered whole-pixel drag, with independent Python assertions.

- One coarse ArrowDown moves the initial +50 µm defocus to 0 and removes the hint.
- Keyboard Home/End reached coarse 0/10 mm, fine -50/+50 µm, both stage axes -10/+10 mm, and lamp/iris 0/100%. No exceptions or nonfinite readouts.
- Fields independently checked as 18/objective: 4.50, 1.80, 0.45 and 0.18 mm. Nominal reticle factors: 25, 10, 2.5 and 1 µm.
- The oil model changes the 100× estimated depth from 1.3018 to 0.53328 µm; dry immersion is rendered dimmer and softer. These are model outputs, not experimental measurements.
- Fifty rapid stage keys ended at 2.50 mm. A rightward real drag produced positive slide displacement; the rendering applies negative displacement to the image.
- Washing gives an intentionally empty stage. Selecting the micrometer and pressing Enter on the eyepiece remounts it. Lamp zero intentionally darkens the field without hiding the controls.
- Calibration rejects zero counts. A 100 µm span over four reticle intervals gives 25 µm/division. Extreme small factors retain significant digits rather than displaying a misleading zero; final check showed 0.010 µm/division.
- A keyboard stroke, label and observation note survived Page.reload unchanged, with 400× captured from the turret. Print produced one page containing only observations; inspected in Chrome's PDF renderer because Poppler was unavailable.
- Local panning ran 180 frames in 2,977.3 ms, about 60.46 fps. This is the exact micrometer on this machine, not a school Chromebook or photographic-slide performance claim.
- No runtime errors or external requests in the functional run. Final isolated phone/calibration shots also reported zero errors. One earlier host-only favicon 404 was removed from the test harness; the instrument now has an inline data favicon.

Each command after the initial reads used a bounded runner or timed job. Bundle limits were 120 seconds, screenshot/check batches at most five minutes, and the single mechanical audit 20 minutes. Its full run finished. All test drivers returned and invoked their Chrome cleanup; both local host implementations shut down. Independent process inventory was denied by Windows, and socket probes were inconclusive, so no stronger process-inventory claim is made.

## Voice walk

`science-narrator` is specified in `voice/lines.json`; runtime uses the kit's browser-voice fallback without recording. One quiet hint is eligible once. Turning focus first makes that hint obsolete and suppresses it. Read announces the mount, total magnification and field, without invented feature names.

The audit's fresh-page held-click walks heard the hint after non-focus actions, skipped it for Read, and respected Sound off. Repeated-input checks were clean. The functional run pressed Read twice two seconds apart with Sound off; both current readouts appear in `__tool.vlog`. Chrome was muted throughout, so this verifies queue behavior, not a human assessment of spoken voice quality.

## Short test

**Not passed.** Operator exploration and grade-6/adult perspectives do not justify claiming a ten-minute biological hunt or month-long depth when the photographs are absent. No human study or successful ten-minute student playtest is claimed.

| Question | Honest assessment |
|---|---|
| Would a kid open it unassigned? | Not reliably yet. The controls react, but the promised pond life is missing. |
| Would an adult play for fun? | It offers useful micrometry experiments, but insufficient material for the intended sustained curiosity. |
| Is the real thing the interface? | The exact dimensional scale and optical controls are the interface. Biological material is still absent. |
| Does it work without score or finish? | Yes. Nothing evaluates, awards or ends the exploration. |

The models were opened and used before design: Beat Lab playback, Elements Inspector on iron, and both family Manual drawers. The bench borrows confidence and physical controls, not their palettes or lesson frames. This comparison makes the remaining material deficit obvious:

| Microscope Bench | Elements Inspector |
|---|---|
| ![Bench at 400 times](../../_scratch/microscope-bench/final/comparison-bench.png) | ![Elements Inspector on iron](../../_scratch/microscope-bench/models/elements.png) |

## Lesson creep check

The final `static-check.json` has zero whole-word hits in `src.html` and voice lines for score, points, level, goal, sticker, badge, correct, wrong, try again, complete, well done, what is and collected. No em dash in authored files. No lesson modes, header, questions, collection count, targets or finish screen were introduced.

## Done when

| Spec acceptance item | Result and evidence |
|---|---|
| 1. Blurry pond opening and first focus reaction | **FAIL.** Blurry micrometer opens; the focus reaction works, but pond material is absent. |
| 2. Every specimen/mount choice matches a real image | **FAIL.** Only the micrometer is offered. Biological mount preparation is absent. |
| 3. Licensed image manifest and Manual inventory | **FAIL.** Candidate licences are documented, but no required photographic slide inventory was delivered. |
| 4. Calibrated cell measurement within 20% | **FAIL.** No independently scaled cheek or blood micrograph. Exact ruler calibration is not a substitute. |
| 5. Stage inversion and dry 100× softness/dimming | **PASS** for the simulated instrument. Real drag and oil-model checks recorded. |
| 6. No questions or premature field-guide names | **PASS** for available material. Below 40× objective, inspection says Look closer; the preparation's name remains a mount label. |
| 7. Private sketchbook saves, reloads and prints | **PASS.** Stroke, label, notes and magnification persisted; one-page print inspected. |
| 8. Keyboard/value access and Chromebook full-slide 60 fps | **FAIL overall.** Keyboard/value checks pass; local ruler panning is about 60 fps; required photographic Chromebook benchmark is untested. |
| 9. Responsive layout, plate/Manual, AA, Motion stops swimmers | **FAIL overall.** Layout and contrast pass; no swimming material exists to test. |
| 10. Offline file and passed short test with comparison | **FAIL overall.** Offline behavior and comparison are present; the short test is not passed. |
| 11. No lesson/game layer | **PASS.** Source and voice search is clean. |

Things-to-do coverage: 1 pond chase FAIL; 2 rotifer FAIL; 3 onion/stain comparison FAIL; 4 cheek nuclei FAIL; 5 cover-slip bubbles FAIL; 6 salt/sugar FAIL; 7 hair FAIL; 8 feather FAIL; 9 fly wing FAIL; 10 oil comparison PASS as a model; 11 pale-cell iris comparison FAIL despite working iris; 12 reticle calibration PASS but cheek measurement FAIL; 13 root-tip division hunt FAIL; 14 sketch/label/magnification/print PASS.

## Audit leads

The one full audit finished with 69 leads in `_scratch/microscope-bench/audit/audit.md`; this is not described as a clean audit. Its repeated-input and resize checks were clean.

- Fixed: preview sketchbook tab clipping; 30 px Manual summaries; short source-link targets; 38 px sketch label field; explicit input names; desktop book extending into the footer; calibration labels crowding their fields. Final focused frames verify 44 px targets and contained drawers. The full audit was not repeated after these corrections.
- Expected: the one-time hint overlays the eyepiece; modal drawers cover underlying keep regions; the specified phone tray scrolls horizontally. These do not hide active modal controls.
- Two collapsed-details paragraph overlap leads did not reproduce in the inspected Manual frames. Source links have deliberate outbound navigation only.
- The desktop label/notes originally had proper associated HTML labels; explicit aria-labels were added as well.

Final isolated phone checks: width 375, zero horizontal document overflow, label field 44 px, calibration input 44 px, sketchbook bottom 704 within the 812 px viewport. Main controls and lower-left plate/Manual remain visible.

Contrast calculations: cream/bench 7.18:1; readout 11.32:1; button 6.48:1; plate 5.97:1; muted engraving 5.51:1; Manual link 7.32:1. Grayscale inspected. Motion off has no continuing animation; functional idle render delta was zero.

## Frames looked at

Inspected every produced screenshot in Scratch's `models/`, `initial/`, `frames/`, `fixed/`, `audit/`, `extra/`, `final/`, `phone-final/` and `performance/`. These cover all STANDARDS sizes, 375×812 through an iframe, actual input, extreme calibration, Manual, notebook, oil/reticle, grayscale, Motion off, and the printed PDF. The final phone-only pass replaced an earlier overlapping-host run; it had zero console errors.

Evidence maps: `checks.json`, `static-check.json`, `performance.json`, `validation.json`, `audit/audit.md`, and `sketch-print.pdf`. Bundle SHA-256: `eca26ee1be0e438784bdbb4e8221a63e8c2c4278d6c340fea79b4f46f14937b8` was recorded before the last tiny calibration-format/favicon edits; `validation.json` preserves that earlier snapshot rather than claiming it hashes the final file.

## Art made

Original code draws the bench instrument, glass-slide motif, knurled dials, turret, ruler and reticle. No generated bitmap or photographic specimen was included. `art/prompts.json` deliberately has no painted assets; `art/manifest.json` has no accepted image entries. The recovered error sprite is not art or data for this tool.

## Engine changes wanted

No shared changes made. The current kit exports no save/load API, so a small guarded localStorage adapter handles the book and reports failures visibly. Any later shared save API should follow the three-tool rule; this build does not require an engine edit.

## Left open

- Retrieve qualifying, genuinely scaled micrographs and photographic sprites; build the specimen and prepared-slide tray, stains, water/dry mounting, cover slips and slide-specific source pages.
- Add source-grounded pond motion, scan-worthy stitched material/detail tiles and focal stacks; validate identification regions and real-cell measurements independently.
- Restore the intended first two minutes and month-long biological depth, then conduct the required ten-minute short-test exploration and Chromebook benchmark.
- Phone eyepiece diameter is below the suggested roughly 340 px so its working controls remain on screen. The dense glass-slide shelf intentionally scrolls.
- The source's allowance to infer pixel size from stated magnification was not used where camera calibration was missing. Calibration factors below 0.1 µm retain significant digits instead of the usual one decimal to avoid displaying zero.
- Process deviation: the first read-only workspace/brief and memory-search calls used tool yield limits without an explicit wall-clock stopper. Subsequent commands were bounded. No permission questions were asked in this unattended session.

No release-readiness or completed biological Curiosity claim is made. The user's instruction to stop after writing this report ends this build session here.
