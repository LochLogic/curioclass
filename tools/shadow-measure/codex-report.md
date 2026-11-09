# Codex report: shadow-measure

## Built

Grade 10 geometry lab with Sun, Mirror and Streetlight, all four notebook steps, direct tape dragging, keyboard fine adjustment, AA reason pairs, calibrated painted objects, animated height comparison, mirror sighting, dilation mapping and a session notebook.

The folder is S:/CurioClass-codex. Authored project files stay in tools/shadow-measure/ and _scratch/shadow-measure/. No shared source edits, git commits, deployment or polish round. Metadata is stage built, status beta.

The offline bundle is 819,318 bytes, about 800.1 KB. Final JavaScript syntax, JSON, preview SVG, required notes headings, voice inventory and asset-token resolution pass. Final runtime hashes are in _scratch/shadow-measure/validation-manifest.json.

## Numbers check

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

## Facts checked

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

## Break it

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

## Voice walk

Bank big-sister / Leda is declared. No recordings were made, as required. Browser speech is the fallback; 17 inventory strings match allLines(). Chrome tests were muted, so this verifies queue behavior rather than listening quality.

Main path used held 120 ms clicks at about two-second action spacing, actual jittered drags and real arrow-key corrections. student.json records:
- Sun: wSun, recordReady, why, revealReady, close.
- Mirror: wMirror, crosshair, close. Shared how-to lines stay once per page.
- Streetlight: wLight, close, then book.
- Side path: refused color pair, pairRetry, Read interruption, mode switch, Sound off and back on.

The log records started lines and cuts when the student advances to a new moment. Redundant tape instructions are no longer queued after that mode's welcome was heard. Record and Reveal speech uses state validity and enabled-control checks; the tape how-to lines do not name a disabled Record.

The audit found that two quick New trial taps cut the still-valid welcome. Implemented a repair that preserves speech for an untouched setup. Its final browser retest was blocked by the later Chrome connection failures.

## Feel check

Best moment: dragging real tapes to 1.19 and 10.01, justifying the angles, then seeing the two height bars nearly coincide at 8.41 versus 8.40. Mirror's moving reflected roof and Streetlight's ghost/dilation give later trials different physical tasks.

Two flattest moments and changes:
- The tiny reference stick and tape labels initially disappeared under handles or each other. Separated the readouts, moved the object controls and kept the reference label clear.
- A positive comparison headline could sound earned even for fabricated ratios. Added the endpoint guard, neutral pre-reveal heading and remeasure marking. The guard was driven successfully; the last heading/table labels still need browser review.

Both bar tools were bundled in Scratch and opened without writing to their folders. The side-by-side comparison shows the painted field scene beside Beat Lab's instrument finish. No ten-minute retention claim was tested.

![Shadow Measure beside Beat Lab](../../_scratch/shadow-measure/bar-comparison.png)

## Done when

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

## Wave lessons

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

## Audit leads

One full audit ran, completed in about 23 minutes, with 41 leads and 67 frames. It was not rerun. Its snapshot predates the final repairs. Evidence: audit/audit.md, audit-states-before.json, corrected audit-states.json, replay-0.json, replay-1.json and replay-2.json.

- 15 zero-font leads: intentional icon rendering. Visible glyphs are 17 px, targets 44 px, and controls have accessible names.
- 9 overlap leads: implemented repairs for setup/footer, Mirror readouts, tape/footer and dilation overlays. Seven were confirmed in repaired Mirror/dilation replays; the two compact Sun setup overlaps were not re-shot.
- 8 state focus/hidden-region leads: my fixture omitted the outer return expected by the audit wrapper, so its drags did nothing. Corrected the fixture. Separate real-input replays reached Why and Reveal at all eight sizes, and populated notebooks at three, without lost focus, overlap, scroll or errors.
- 3 skipped-welcome leads: deliberate first actions speak their own tape or notebook instruction, as STANDARDS requires.
- 5 no-change leads: current Set up tabs and drag handles clicked without movement. Actual drags and arrow input work.
- 1 quick New trial welcome cut: fixed in source, final browser retest blocked.

Twenty-five corrected state replays passed. The final smaller replay batch and standard drive.py fallback later lost Chrome's CDP connection before reaching their target pages. Browser retries stopped; this is not reported as a clean final audit.

## Frames looked at

129 screenshots were inspected directly or in labeled contact sheets: bar-frames (2), early (4), focused (6), final-frames (12), last-frames (6), student (6), audit (67), repaired (25) and keyboard-entry (1).

The full size sweep ran once. Later shots targeted repairs. Coverage includes every STANDARDS size, a 375 px host on 8785, all modes, sun 25/65, all four Sun objects, near/far mirror positions, streetlight 1/8, Motion off, grayscale, notebook and keyboard-only work. Art sheets and bar comparison were also inspected.

## Art made

Eleven images made during this build with the built-in image tool: two backdrops and nine cutouts, all used. Final WebP total is 547,454 bytes, 534.6 KB. Audio is 0 KB. Bundle is 800.1 KB against the 2,048 KB goal and the opening 650 KB image budget.

Full prompts, draw provenance, raw PNGs and calibration points are present. No people appear. Tree, hoop and tripod were rekeyed for clean gaps and edges. Selected paintings were resized from their originals for large display; no redraw was needed. Original and final art contact sheets are in Scratch.

## Art still to paint

None.

## Engine changes wanted

None. Shared kit and family files were not modified.

## Left open

- Browser-verify final 680x425 setup layouts, including the hoop's longer rule text.
- Browser-verify shortened refusal feedback at 680 and 375 wide, returning to an already-proved Why step, and the final remeasure row/neutral-result labels.
- Re-run the rapid New trial welcome check. The implemented preserve-speech repair has only syntax verification after Chrome failed.
- Visually recheck the above-view marker for an extremely large estimate.
- Fixed clips remain unrecorded by instruction; actual fallback voice quality was not listened to during muted tests.

All features are implemented, but the final checks above are not claimed to pass. Final JS syntax, metadata, notes headings, SVG and asset resolution pass. Runtime hashes exclude this report because it is written last. No owned Chrome remained in the final process inventory; ports 8785 and 9980 through 9987 are closed, and host.html is absent. Build only ends here.
