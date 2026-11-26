# Shadow Measure: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: shadow-measure

#### Built

Grade 10 geometry lab with Sun, Mirror and Streetlight, all four notebook steps, direct tape dragging, keyboard fine adjustment, AA reason pairs, calibrated painted objects, animated height comparison, mirror sighting, dilation mapping and a session notebook.

The folder is S:/CurioClass-codex. Authored project files stay in tools/shadow-measure/ and _scratch/shadow-measure/. No shared source edits, git commits, deployment or polish round. Metadata is stage built, status beta.

The offline bundle is 819,318 bytes, about 800.1 KB. Final JavaScript syntax, JSON, preview SVG, required notes headings, voice inventory and asset-token resolution pass. Final runtime hashes are in _scratch/shadow-measure/validation-manifest.json.

#### Numbers check

Independent Python results: _scratch/shadow-measure/numbers.json. All prescribed examples agree with the spec.

| Case | Recorded readings, m | Estimate, m | Real, m | Off by |
|---|---|---|---|---|
| Sun, flagpole, 40 degrees | 1.19, 10.01 | 8.41 | 8.40 | 0.1% |
| Sun, tree, 25 degrees | 2.14, 24.13 | 11.28 | 11.25 | 0.2% |
| Sun, hoop, 55 degrees | 0.70, 2.14 | 3.06 | 3.05 | 0.2% |
| Sun, sign, 65 degrees | 0.47, 1.12 | 2.38 | 2.40 | 0.7% |
| Mirror, mirror at 9.00 | 9.00, 2.00 | 6.75 | 6.75 | 0.0% |
| Streetlight, stick at 5.00 | 5.00, 1.32 | 4.79 | 4.80 | 0.3% |

Tree's unrounded estimate is 11.2757009346, so its displayed error is 0.2%. A flag tape 0.20 m short records 9.81, estimates 8.24 and gives 1.9%. The longest shadow is 24.13 m. Worst exact-tape rounding error is 1.0048% over Sun's full object/angle grid and 1.2931% over Streetlight's 0.01 m positions.

Mirror's wall-top tolerance produces tripod windows 0.8759 to 0.9023 m at mirror 4 m, 1.9708 to 2.0301 at 9 m, and 2.6277 to 2.7068 at 12 m. Dilation is 1 / 4.8 = 0.208333, displayed 0.21, at every stick position.

Declared-palette contrast calculations match the spec: 12.80, 12.13, 13.43, 11.82, 7.49, 7.83 and 16.08 to one. Painted-scene labels have opaque light or dark pills; dark ink on the light pill is 15.94:1. Evidence: contrast.json.

#### Facts checked

| Student-facing fact or assumption | Named source and check |
|---|---|
| AA similarity and proportional corresponding sides | [Euclid VI.4, Joyce edition](https://mathcs.clarku.edu/~djoyce/java/elements/bookVI/propVI4.html), checked live |
| Dilations, AA and solving height problems | [Common Core HSG-SRT.A.1, A.3 and B.5](https://www.thecorestandards.org/Math/Content/HSG/SRT/), checked live |
| Light travels in straight rays | [OpenStax College Physics 2e, 25.1](https://openstax.org/books/college-physics-2e/pages/25-1-the-ray-aspect-of-light), checked live |
| Reflection has equal incident and reflected angles | [OpenStax 25.2](https://openstax.org/books/college-physics-2e/pages/25-2-the-law-of-reflection), checked live; equal ground angles follow by taking complements |
| Hoop rim is ten feet above the floor | [NBA Rule 1, Section II.5](https://official.nba.com/rule-no-1-court-dimensions-equipment/), checked live on 2026-11-05 |
| Ten feet displayed as 3.05 m | Exact conversion is 3.048 m; the spec explicitly models its rounded 3.05 m |
| Flagpole 8.40, tree 11.25, sign 2.40, wall 6.75, lamp 4.80 m | Invented dimensions from spec.md, not claims about a real schoolyard |
| Reference stick 1.00 m, eyepiece 1.50 m, setup ranges | Spec Content and Interactions; implemented and independently recomputed |
| Parallel sunlight, vertical objects, level ground, point lamp and horizontal mirror | Explicit idealizations of this spec; the sunlight parallelism is a local-yard approximation |
| Three height formulas, percent error and dilation factor | Similar-triangle derivation plus independent Python and browser checks |

Conflicts and decisions are in handoff.md: keyed image-tool art overrides local FLUX/white backgrounds; STANDARDS wins for short landscape layout; the required hoop rule line discloses its height despite the general hidden-height premise. No spec open questions are listed.

#### Break it

147/147 functional assertions passed, including all 45 unordered reason-card pairs across the three methods. Evidence: functional-final.json and functional.js. Numerical formulas and the core proof/record guards are unchanged after that run.

- Record: unmoved, one-tape, moved-zero and non-finite readings refused. Repeated Record cannot duplicate a row.
- Proof: only the specified pair works in each method. One card gives no correctness clue. After a refused pair, cycling through every pair cannot unlock Reveal without fresh readings.
- Reveal: direct calls before proof, repeated reveals and stale proof after retaping or setup changes refuse.
- Slider sweep: changes after recording invalidate the active trial, rather than retaining a favorable result.
- Mirror: a correctly proportioned reading cannot be recorded while the sight is outside the wall-top tolerance.
- Error readout: short, tiny and careless readings preserve their honest numerical error.
- Fabricated correct ratio: 0.05 and 0.42 would give 8.40 m without measuring. The runtime endpoint guard correctly withheld close praise and asked for remeasurement.
- Saved result: the final presentation also marks mismatched-endpoint rows remeasure and withholds the positive headline. These last presentation additions are syntax checked but not browser retested.
- No best score, badges or persistent mastery count exists. The notebook records evidence for this page session, including unfinished trials.

The endpoint guard permits max(0.06 m, 3% of the actual span), alongside the under-2% height condition. It does not alter the percent-error arithmetic. A finite reason-card activity can still be guessed; the repair removes free pair enumeration and partial-right feedback.

#### Voice walk

Bank big-sister / Leda is declared. No recordings were made, as required. Browser speech is the fallback; 17 inventory strings match allLines(). Chrome tests were muted, so this verifies queue behavior rather than listening quality.

Main path used held 120 ms clicks at about two-second action spacing, actual jittered drags and real arrow-key corrections. student.json records:
- Sun: wSun, recordReady, why, revealReady, close.
- Mirror: wMirror, crosshair, close. Shared how-to lines stay once per page.
- Streetlight: wLight, close, then book.
- Side path: refused color pair, pairRetry, Read interruption, mode switch, Sound off and back on.

The log records started lines and cuts when the student advances to a new moment. Redundant tape instructions are no longer queued after that mode's welcome was heard. Record and Reveal speech uses state validity and enabled-control checks; the tape how-to lines do not name a disabled Record.

The audit found that two quick New trial taps cut the still-valid welcome. Implemented a repair that preserves speech for an untouched setup. Its final browser retest was blocked by the later Chrome connection failures.

#### Feel check

Best moment: dragging real tapes to 1.19 and 10.01, justifying the angles, then seeing the two height bars nearly coincide at 8.41 versus 8.40. Mirror's moving reflected roof and Streetlight's ghost/dilation give later trials different physical tasks.

Two flattest moments and changes:
- The tiny reference stick and tape labels initially disappeared under handles or each other. Separated the readouts, moved the object controls and kept the reference label clear.
- A positive comparison headline could sound earned even for fabricated ratios. Added the endpoint guard, neutral pre-reveal heading and remeasure marking. The guard was driven successfully; the last heading/table labels still need browser review.

Both bar tools were bundled in Scratch and opened without writing to their folders. The side-by-side comparison shows the painted field scene beside Beat Lab's instrument finish. No ten-minute retention claim was tested.

![Shadow Measure beside Beat Lab](../../_scratch/shadow-measure/bar-comparison.png)

#### Done when

1. PASS: flagpole 40-degree readings, estimate, real height and 0.1% match; real-input student run and functional checks.
2. PASS: tree 25-degree readings give 11.28 and 0.2%, using the unrounded estimate.
3. PASS: mirror at 9.00 with tripod at 2.00 enters the crosshair and gives 6.75; real-input run.
4. PASS: streetlight at 5.00 gives 4.79 and 0.3%; layer shows k = 0.21.
5. PASS: all 45 pairs tested; Reveal stays locked for every wrong pair, and color is refused with its reason.
6. PASS: 0.20 m short gives an honest 1.9% error.
7. PASS: inspected 1366 and 1000 frames; 24.13 m tree shadow fits. Light paths and measuring strips remain central.
8. PASS: normalized measured points are documented and loaded by the build; silhouettes project from those points. Hoop's rim tick is distinguished from its backboard shadow. Art alignment is limited by raster resolution.
9. PASS: animation-interrupt.json confirms slider, step and tape changes act during feedback; audit resize checks found no exceptions or locked controls.
10. PASS in completed voice walks: Record/Reveal lines are guarded by current enabled controls. Later welcome-only repair remains unverified.
11. FAIL, verification incomplete: keyboard-only Sun reached Reveal with 1.19 and 10.01, focus on New trial and scrollY zero. Corrected Why/Reveal replays passed all eight sizes. The last compact setup repairs could not be re-shot after Chrome failed.
12. PASS in completed browser runs: no application console errors or HTTP requests. Final source/bundle has no em dashes, unresolved asset tokens or syntax errors; Curio Class is written in full.

#### Wave lessons

- Hint and voice: PASS for main paths and enabled-control guards; FAIL to reverify the last rapid-reset and returning-to-proof hint repairs.
- Focus and layout: PASS for real Record-to-reason-to-Reveal-to-New focus and 25 corrected replays. No load focus is taken.
- Sizes: FAIL to finish the final compact setup retest. All eight sizes, phone host, current-step screens and 44 px controls were covered in completed runs.
- No giveaways: PASS for no partial-correct card feedback, no tap correctness meter and no free repeated pair attempts.
- Honest numbers: PASS; invented heights and reference assumptions are stated, readings are rounded before calculation and percentages after it.
- Standards: PASS; the student measures, selects AA reasons and operates the dilation layer. No family engine is specified.
- Motion off: PASS; the completed audit found no infinite animation.
- Short choices stay visible: PASS; all six reason cards are in view in corrected replays at every required size.
- Resize mid-animation: PASS in the audit and separate interruption check; canvas redraw does not rebuild controls.
- No late deferred welcome: PASS; no welcomeAfter is used. A first tap with its own instruction deliberately skips the welcome.
- Unknown stays unknown: PASS; Real and Off by stay question marks until Reveal. Required hoop disclosure is documented as the exception.
- One look, one meaning: PASS; lettered tapes, chalk endpoints, distinct rays and wide/thin comparison bars.
- Badge says what is true: PASS; no success badge or stored best score. Final remeasure row label awaits browser retest.
- Hint changes back: FAIL to reverify the final already-proved Why-step hint; state-specific repair is implemented.
- No answer by copying a clue: PASS within the fixed spec cards; the action hint does not repeat a correct pair.

#### Audit leads

One full audit ran, completed in about 23 minutes, with 41 leads and 67 frames. It was not rerun. Its snapshot predates the final repairs. Evidence: audit/audit.md, audit-states-before.json, corrected audit-states.json, replay-0.json, replay-1.json and replay-2.json.

- 15 zero-font leads: intentional icon rendering. Visible glyphs are 17 px, targets 44 px, and controls have accessible names.
- 9 overlap leads: implemented repairs for setup/footer, Mirror readouts, tape/footer and dilation overlays. Seven were confirmed in repaired Mirror/dilation replays; the two compact Sun setup overlaps were not re-shot.
- 8 state focus/hidden-region leads: my fixture omitted the outer return expected by the audit wrapper, so its drags did nothing. Corrected the fixture. Separate real-input replays reached Why and Reveal at all eight sizes, and populated notebooks at three, without lost focus, overlap, scroll or errors.
- 3 skipped-welcome leads: deliberate first actions speak their own tape or notebook instruction, as STANDARDS requires.
- 5 no-change leads: current Set up tabs and drag handles clicked without movement. Actual drags and arrow input work.
- 1 quick New trial welcome cut: fixed in source, final browser retest blocked.

Twenty-five corrected state replays passed. The final smaller replay batch and standard drive.py fallback later lost Chrome's CDP connection before reaching their target pages. Browser retries stopped; this is not reported as a clean final audit.

#### Frames looked at

129 screenshots were inspected directly or in labeled contact sheets: bar-frames (2), early (4), focused (6), final-frames (12), last-frames (6), student (6), audit (67), repaired (25) and keyboard-entry (1).

The full size sweep ran once. Later shots targeted repairs. Coverage includes every STANDARDS size, a 375 px host on 8785, all modes, sun 25/65, all four Sun objects, near/far mirror positions, streetlight 1/8, Motion off, grayscale, notebook and keyboard-only work. Art sheets and bar comparison were also inspected.

#### Art made

Eleven images made during this build with the built-in image tool: two backdrops and nine cutouts, all used. Final WebP total is 547,454 bytes, 534.6 KB. Audio is 0 KB. Bundle is 800.1 KB against the 2,048 KB goal and the opening 650 KB image budget.

Full prompts, draw provenance, raw PNGs and calibration points are present. No people appear. Tree, hoop and tripod were rekeyed for clean gaps and edges. Selected paintings were resized from their originals for large display; no redraw was needed. Original and final art contact sheets are in Scratch.

#### Art still to paint

None.

#### Engine changes wanted

None. Shared kit and family files were not modified.

#### Left open

- Browser-verify final 680x425 setup layouts, including the hoop's longer rule text.
- Browser-verify shortened refusal feedback at 680 and 375 wide, returning to an already-proved Why step, and the final remeasure row/neutral-result labels.
- Re-run the rapid New trial welcome check. The implemented preserve-speech repair has only syntax verification after Chrome failed.
- Visually recheck the above-view marker for an extremely large estimate.
- Fixed clips remain unrecorded by instruction; actual fallback voice quality was not listened to during muted tests.

All features are implemented, but the final checks above are not claimed to pass. Final JS syntax, metadata, notes headings, SVG and asset resolution pass. Runtime hashes exclude this report because it is written last. No owned Chrome remained in the final process inventory; ports 8785 and 9980 through 9987 are closed, and host.html is absent. Build only ends here.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: shadow-measure

#### Played

Played cold as a Grade 10 student before reading codex-report.md, handoff.md, notes.md or src.html. Sun and Streetlight felt direct; aligning the reflected wall top was the strongest moment. Also inspected the projector-sized and phone layouts and both bar tools.

#### Findings fixed

- **blocker, general, Streetlight dilation:** k=0.21 exposed the unknown height before measurement. The actual shortcut produced 5.00/1.33, 0.8% error and positive praise. Numeric k now appears only after Reveal; triangles and point mapping remain available throughout.
- **should fix, general, Streetlight welcome:** it asked for hidden tapes without naming Measure. Added that control to the welcome and voice inventory.
- **should fix, general, Mirror voice:** setup's crosshair line could name a hidden Measure control after entering measurement. Split the event by step, hush setup speech on entry and when alignment is lost, and give the tape how-to once there.
- **should fix, general, Read:** several fixed hints were outside allLines and lines.json. All 25 fixed narration/Read strings now match; setup and measuring use separate instructions.
- **should fix, general, dilation access:** corresponding-point mapping was pointer only. Added keyboard focus, arrow keys and Home, an initial mapped pair, visible focus and resize preservation.
- **should fix, general, art:** hoop backboard was clipped. Redrew the complete hoop, retained the painted style, recalibrated the rim, and rekeyed five other cutouts with edge despill.
- **polish, general, Reveal:** a poor result gave little visual explanation. Added dotted tape-to-target gaps and arrowheads only after Reveal, without a pre-Reveal accuracy meter. Kept these clear of labels.
- **polish, general, compact dilation:** shortened the readout in compact views so the extra keyboard guidance does not cover the stick handle.

#### Findings left

No tool blocker or should-fix remains. The mechanical phone-audit coverage gap is documented under Audit.

- **nit, general, art:** tiny residual colored pixels remain at some complex cutout edges at source resolution; the final scene sizes keep them unobtrusive.

#### Break it

104 assertions passed before and after the first repairs, including all 45 unordered reason pairs across three methods. Evidence: break-before.json and break-after.json in Scratch.

- Record: zero, unmoved and one-tape attempts refused; duplicate Record cannot add rows.
- Why similar: wrong pairs clear the readings; trying every remaining option cannot unlock Reveal without measuring again. A single selected card gives no correctness clue. Color refusal explains that color fixes no angle.
- Reveal: direct early calls, repeated calls, retaping and setup changes cannot keep stale proof or farm a result.
- Accuracy/praise/notebook: both tapes swept to End fail accuracy; tiny 0.05/0.42 gives an honest 0.0% but neutral remeasure feedback and a marked notebook row. A 0.20 m short flag tape preserves 1.9% error.
- Mirror crosshair: a correct ratio with the tripod unaligned cannot be recorded. Moving the mirror after proof invalidates that trial.
- Dilation shortcut: confirmed passing before repair; after repair no numeric factor is exposed before Reveal. A measured 5.00/1.32 trial still gives 4.79 m, 0.3%, and k=0.21 afterward.
- No points, best score, mastery count or reflection gate exists. Notebook entries remain session evidence, including unfinished trials.

#### Voice walk

Held 120 ms clicks, jittered real drags, arrow corrections and about 2 seconds between actions, Sound on, default setup values. Read __tool.vlog after the full path.
Sun: wSun, tapeSun, recordReady, why, revealReady, close. Mirror: wMirror, crosshair, tapeMirror, close. Streetlight: wLight, tapeLight, close. Shared how-to lines remain once per page.

| Line kind | Expected | Heard |
|---|---:|---:|
| Each mode welcome | 1 each | 1 each |
| tapeSun, tapeMirror, tapeLight, recordReady, why, revealReady | 1 each | 1 each |
| close, three main results plus five repeated results | 8 | 8 |
| far, ratioCheck, middle, pairRetry, crosshairTape, separate repeat batch | 5 each | 5 each |
| setup crosshair, main plus four repeats | 5 | 5 |
The kept bank is big-sister/Leda; checked neighbors declare different banks. Read interrupted speech, worked with Sound off, and read the current hint twice; both strings are inventoried. Fast mode changes and Reset left no stale queued speech. Sound re-enabled during Measure spoke tapeLight, and leaving the crosshair left no stale queued event. All voice checks had no application console errors. Browser fallback speech was tested through the muted log; recordings remain unmade as instructed.

#### Facts checked

- AA gives proportional corresponding sides: [Euclid VI.4, Joyce edition](https://mathcs.clarku.edu/~djoyce/java/elements/bookVI/propVI4.html).
- Dilation center/scale, AA and similarity problem solving: [Common Core HSG-SRT.A.1, A.3, B.5](https://www.thecorestandards.org/Math/Content/HSG/SRT/). Students measure, justify matching angles and map corresponding points.
- Straight-ray model: [OpenStax College Physics 2e 25.1](https://openstax.org/books/college-physics-2e/pages/25-1-the-ray-aspect-of-light). Parallel sunlight over a yard: [NASA JSC, ISS029-E-31270](https://esrs.jsc.nasa.gov/Collections/EarthFromSpace/caption.pl?PHOTO=ISS029-E-31270).
- Equal incident/reflected angles are measured from the normal; the equal ground angles follow by complements: [OpenStax 25.2](https://openstax.org/books/college-physics-2e/pages/25-2-the-law-of-reflection).
- Rim upper edge is 10 ft above the floor: [NBA Rule 1, II.5](https://official.nba.com/rule-no-1-court-dimensions-equipment/), checked live. Exactly 3.048 m, modeled as the spec's rounded 3.05 m.
- Flagpole 8.40, tree 11.25, sign 2.40, wall 6.75, lamp 4.80, stick 1.00 and eye 1.50 m: named source is spec.md Content, invented schoolyard dimensions rather than external real-world claims.
- Three height formulas, tape rounding, percent error and k: derived from the named similarity/ray sources and independently recomputed in review-numbers.py. All specified examples agree. Worst exact-tape Sun error is 1.0048%; Streetlight is 1.2931%; k is 0.2083333 at every stick position.
- Mirror at 9 m aligns for tripod 1.9708 to 2.0301 m; 9.00/2.00 gives 6.75. Tree at 25 degrees records 2.14/24.13, estimate 11.2757, displayed 11.28 and 0.2%. The rounding is honest.

#### Sensitivity

None: invented schoolyard, no people images, bodies, cultural traditions, religion or hard history. All 11 assets are marked people:false, consistent with the scene's instrument-only spec.

#### Flattest moment left

Remeasuring after a refused reason pair remains mechanical. Its explanation is clear, and requiring new readings prevents free option enumeration. Added no new topic or game feature to disguise that tradeoff.

#### Graphics

Inspected all 11 assets and their scene placements. Kept the layered schoolyard, silhouettes, chalk, textured tapes, night glow and notebook finish. The complete hoop and cleaned edges improve the weakest art. The post-Reveal gaps and keyboard-mapped point make the result more specific to the student's actions.
Bundle 817,846 bytes (798.7 KiB); art 543,430 bytes (530.7 KiB). Compared with Beat Lab and Snowy Mail Route. Final hoop: art/sm-hoop.webp; raw original: art/raw/sm-hoop.png. Built-in imagegen prompt: ../../_scratch/shadow-measure/review-hoop-prompt.txt. No people or missing art tokens.

#### Audit

Completed once within the 40-minute limit: ../../_scratch/shadow-measure/review-audit/audit.md, 71 inspected frames, 36 leads. Twelve are 0 px header words replaced by accessible 17 px glyphs; fourteen are intentional overlays on the focusable canvas or their text containers; three are allowed first-tap welcome skips; five are current-step or unmoved-handle clicks; two are the failed phone host. Repeated taps, Motion off and resize stress reported no failures.
The phone host failed because earlier test-server children survived the LibreOffice Python launcher. Independent drive.py 375 px iframe runs covered setup, measuring, refusal and Reveal; final phone repairs were re-shot. The three exact owned hosts were closed and the scratch launcher/server lifecycle corrected. All assigned ports are closed and host.html is absent. The audit was not rerun.
After the audit, fixed the confirmed Streetlight instruction regression and rechecked the full voice path, repeated events, Sound-on-during-Measure and stale crosshair behavior. The audit snapshot predates these narrow final voice changes. Corrected phone-size keys in audit-states.json for future use.
Wave lessons rechecked: current hints and Read, preserved focus and mounted controls, 44 px targets, all six reason choices visible, no free enumeration or favorable false result, stated measuring assumptions, explicit unknown heights, distinct tape/ray/bar meanings, no infinite Motion-off animation, grayscale and resize. Keyboard-only Sun reached Reveal with 1.19/10.01, focus on New trial and scrollY zero. All STANDARDS sizes were inspected. Contrast: accent/panel 12.80:1, ink/accent 13.43:1, scene ink/pill 15.94:1, night label/pill 15.42:1, chalk/blacktop 7.83:1. Figures, hashes, counts and application-error checks are in ../../_scratch/shadow-measure/review-static.json.

#### Left open

- Readout timing was unspecified while the premise requires height hidden until Reveal. Chose that premise and the explicit anti-cheat requirement: keep geometric dilation exploration available, reveal numeric k after the earned result.
- The spec explicitly publishes the hoop's regulation height in Set up. Kept that required disclosure, so Hoop is a known-height calibration case rather than a blind unknown-height test.
- The finite lantern is modeled as an ideal point source at its marked top, as the spec's calibration requires; teacher notes now state that simplification.
- No questions were asked in this unattended run. No shared kit edits or git commits. One review pass; subsequent checks only verified repairs and the required final audit.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Shadow Measure build handoff

#### Structure
src.html starts from the kit starter, uses the kit frame and 9-12 theme, and owns the pixel-sized canvas simulation, persistent HTML controls and session notebook. The script separates geometry, transitions, voice, painting and pointer input. __tool exposes the required state and methods plus setup helpers and narration logs.

#### Tricky parts
All tapes round to 0.01 m before calculating. Percent error uses the full recorded ratio. Images are cut out by scripts/art.py --rekey only. Each cutout's normalized measured point is listed in art/prompts.json. Scratch landmarks.py derives landmarks.json, which src.html loads with a bundler token. A hoop's base is the vertical ground projection of its rim, not its offset support post. The tripod base means the projection under the eyepiece.

Sun shadow footprints preserve the cutout alpha silhouette, flattened across the measuring strip. Their longitudinal coordinate is projected from image height, so a top's shadow lands at the exact physical endpoint. The hoop backboard casts past the rim's chalk tick. The wall's broad painted facade continues off the left of the view so the measured right edge and reflection path remain central.

#### Decisions and conflicts
- No open questions are listed in the spec.
- The user and CODEX-BUILD require the built-in image tool. They override the spec's local FLUX and white-background requests. All nine cutouts use flat keyed backgrounds, with magenta for the tree. No people appear.
- The spec stacks the panel below the scene under 1000 px. STANDARDS wins in short landscape boxes: below 900 px tall, keep them side by side when at least 600 px wide. Phones and the tall 760 px view stack.
- CODEX-BUILD says to start the report as soon as the first bundle works, then stop when it is written. An in-progress report is created at first bundle; the final report is completed after the mandated checks, then the run stops.
- The two reference tools were copied and bundled in Scratch because bundling them in their own directories would violate the user's write boundary.
- A reason-card pair is evaluated together. On failure both choices and tape readings clear, and the refused notebook row stays unfinished. Remeasure before another attempt to prevent free option enumeration. There are no scores or rewards to farm.
- A fabricated pair of very short readings can accidentally produce the correct ratio. Percent error still reports the mathematical result, but close praise requires both endpoints to be within max(0.06 m, 3 percent of the real span). Otherwise feedback asks for a fresh measurement. This implements the user's explicit request to close passing cheats without hiding honest numerical error.
- Dilation controls sit over the stage to preserve the notebook's working space in compact views. Bars have wide/thin labels and an upward marker when an estimate exceeds the view.
- The 3.05 m hoop model is the spec's rounded version of exactly 3.048 m for ten feet.
- The opening premise hides real height until Reveal, while the required Hoop setup line explicitly publishes 3.05 m. The specific required hoop rule line wins; other real heights stay unknown until Reveal.

#### Sensitivity
No people, bodies, culture, religion or hard history. The schoolyard is invented.

#### Engine changes wanted
None. No shared kit edits.

#### Art still to paint
None. Eleven images generated during Build, with full prompts and raw originals in art/raw.

#### Next
The separate cold review is recorded in codex-review.md. No git commits were made.

#### Cold review changes
- Fixed Streetlight's welcome to name Measure before asking for tape movement.
- Split Mirror's crosshair narration by step, stopped setup speech on Measure, and restored the once-only tape how-to on entry.
- Put all fixed Read hints into the voice inventory, now 25 strings. No audio was recorded.
- Separated setup welcomes from tape instructions, so entering Measure or enabling Sound there never names the hidden setup button.
- Made the dilation sample point keyboard accessible with visible focus, arrow keys and Home. Its position survives resize.
- Blocked the confirmed k=0.21 shortcut by showing numeric scale only after Reveal. The spec's hidden-height premise wins over an unspecified readout timing; the full dilation layer remains usable before Reveal.
- Added post-Reveal dotted gaps from the student's tape ends to their physical targets. These introduce no pre-Reveal correctness clue.
- Redrew the clipped basketball hoop in the same painted style, recalibrated its rim, and rekeyed five other cutouts with edge despill.
- Added cold-review extremes and failed-trial audit fixtures. Source facts and independent calculations are in the cold review evidence.

#### Cold review verification
The single review audit completed with 36 leads. Twelve are hidden header words replaced by accessible 17 px glyphs;
fourteen are expected overlays on the focusable canvas or their text containers; three are first-tap welcome skips;
five are current-step or unmoved-handle clicks; two are the failed phone audit host. Repeated taps, Motion off and
resize stress reported no exceptions or stuck controls. All 71 audit frames were inspected.

The phone audit host was affected by surviving test-server children from the LibreOffice Python launcher. Independent
375 px drive.py iframe runs verified setup, measuring, refusal and Reveal, including the final dilation and tape-gap
repairs. The three exact owned server processes were identified by command line and closed. All assigned ports are
closed, and host.html is absent. Scratch now has an in-process bounded runner and server lifecycle.

After the audit, the final instruction correction was rechecked with the complete main voice walk, repeat-event
counts, phone frames and Sound-on-during-Measure. Leaving the crosshair also hushes its now-stale event. Voice
inventory and allLines match all 25 strings. The review audit is not claimed to cover those later narrow voice changes.
The audit fixture's phone size keys now use the auditor's exact 375x812 label for future runs.

#### Audit snapshot and repairs
The single complete audit is in _scratch/shadow-measure/audit/audit.md. It has 41 leads and 67 frames. Its original state drags omitted the outer return required by the audit's step wrapper, so its Why, Reveal and populated-notebook state replays did not reach those states. The corrected audit-states.json is ready for the cold reviewer. Separate real-input replays validate the repaired states without rerunning the full audit.

Audited layout repairs use two compact setup columns, two measurement readouts side by side in short notebook panels, extra clearance below the night tapes, and a right-aligned dilation control with a shorter readout. A rapid New trial tap on an untouched setup preserves the still-valid welcome instead of cutting it. The full audit predates these focused repairs; the build report identifies the follow-up evidence.

The 15 zero-font leads are the intentionally hidden words behind visible 17 px header glyphs, each with a 44 px target and an accessible name. Selecting the current Set up tab is a no-op. Clicking a drag handle without moving it is also a no-op; real drags and arrow keys are tested separately. A first action that speaks its own instruction skips the welcome, as STANDARDS requires.

#### Verification left open
Twenty-five corrected real-input replays passed, including Why and Reveal at all eight required sizes, populated notebooks at three sizes, and the repaired near-mirror and dilation layouts. Later Chrome CDP connections closed before further checks, including with the standard drive.py runner. Do not describe the final full audit as clean.

Recheck the final 680x425 Sun, Hoop, Mirror and Streetlight setup layouts; the shortened refusal feedback at 680 and 375 wide; the rapid New trial welcome repair; and the hint when returning to an already-proved Why step. These repairs are implemented and the final bundled scripts pass Node syntax checking, but their last browser retests did not run. Full main paths and keyboard-only Sun passed before these focused changes.
The final anti-cheat presentation also marks mismatched-endpoint notebook rows "remeasure" and withholds the positive headline. The earlier fabricated-ratio test passed the numerical and narration guard; these added labels need the next browser check too.

All assigned ports are closed, no owned Chrome remained in the final process inventory, and host.html was removed. No recordings, git commits or polish round were made.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
