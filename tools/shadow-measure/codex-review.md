# Codex review: shadow-measure

## Played

Played cold as a Grade 10 student before reading codex-report.md, handoff.md, notes.md or src.html. Sun and Streetlight felt direct; aligning the reflected wall top was the strongest moment. Also inspected the projector-sized and phone layouts and both bar tools.

## Findings fixed

- **blocker, general, Streetlight dilation:** k=0.21 exposed the unknown height before measurement. The actual shortcut produced 5.00/1.33, 0.8% error and positive praise. Numeric k now appears only after Reveal; triangles and point mapping remain available throughout.
- **should fix, general, Streetlight welcome:** it asked for hidden tapes without naming Measure. Added that control to the welcome and voice inventory.
- **should fix, general, Mirror voice:** setup's crosshair line could name a hidden Measure control after entering measurement. Split the event by step, hush setup speech on entry and when alignment is lost, and give the tape how-to once there.
- **should fix, general, Read:** several fixed hints were outside allLines and lines.json. All 25 fixed narration/Read strings now match; setup and measuring use separate instructions.
- **should fix, general, dilation access:** corresponding-point mapping was pointer only. Added keyboard focus, arrow keys and Home, an initial mapped pair, visible focus and resize preservation.
- **should fix, general, art:** hoop backboard was clipped. Redrew the complete hoop, retained the painted style, recalibrated the rim, and rekeyed five other cutouts with edge despill.
- **polish, general, Reveal:** a poor result gave little visual explanation. Added dotted tape-to-target gaps and arrowheads only after Reveal, without a pre-Reveal accuracy meter. Kept these clear of labels.
- **polish, general, compact dilation:** shortened the readout in compact views so the extra keyboard guidance does not cover the stick handle.

## Findings left

No tool blocker or should-fix remains. The mechanical phone-audit coverage gap is documented under Audit.

- **nit, general, art:** tiny residual colored pixels remain at some complex cutout edges at source resolution; the final scene sizes keep them unobtrusive.

## Break it

104 assertions passed before and after the first repairs, including all 45 unordered reason pairs across three methods. Evidence: break-before.json and break-after.json in Scratch.

- Record: zero, unmoved and one-tape attempts refused; duplicate Record cannot add rows.
- Why similar: wrong pairs clear the readings; trying every remaining option cannot unlock Reveal without measuring again. A single selected card gives no correctness clue. Color refusal explains that color fixes no angle.
- Reveal: direct early calls, repeated calls, retaping and setup changes cannot keep stale proof or farm a result.
- Accuracy/praise/notebook: both tapes swept to End fail accuracy; tiny 0.05/0.42 gives an honest 0.0% but neutral remeasure feedback and a marked notebook row. A 0.20 m short flag tape preserves 1.9% error.
- Mirror crosshair: a correct ratio with the tripod unaligned cannot be recorded. Moving the mirror after proof invalidates that trial.
- Dilation shortcut: confirmed passing before repair; after repair no numeric factor is exposed before Reveal. A measured 5.00/1.32 trial still gives 4.79 m, 0.3%, and k=0.21 afterward.
- No points, best score, mastery count or reflection gate exists. Notebook entries remain session evidence, including unfinished trials.

## Voice walk

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

## Facts checked

- AA gives proportional corresponding sides: [Euclid VI.4, Joyce edition](https://mathcs.clarku.edu/~djoyce/java/elements/bookVI/propVI4.html).
- Dilation center/scale, AA and similarity problem solving: [Common Core HSG-SRT.A.1, A.3, B.5](https://www.thecorestandards.org/Math/Content/HSG/SRT/). Students measure, justify matching angles and map corresponding points.
- Straight-ray model: [OpenStax College Physics 2e 25.1](https://openstax.org/books/college-physics-2e/pages/25-1-the-ray-aspect-of-light). Parallel sunlight over a yard: [NASA JSC, ISS029-E-31270](https://esrs.jsc.nasa.gov/Collections/EarthFromSpace/caption.pl?PHOTO=ISS029-E-31270).
- Equal incident/reflected angles are measured from the normal; the equal ground angles follow by complements: [OpenStax 25.2](https://openstax.org/books/college-physics-2e/pages/25-2-the-law-of-reflection).
- Rim upper edge is 10 ft above the floor: [NBA Rule 1, II.5](https://official.nba.com/rule-no-1-court-dimensions-equipment/), checked live. Exactly 3.048 m, modeled as the spec's rounded 3.05 m.
- Flagpole 8.40, tree 11.25, sign 2.40, wall 6.75, lamp 4.80, stick 1.00 and eye 1.50 m: named source is spec.md Content, invented schoolyard dimensions rather than external real-world claims.
- Three height formulas, tape rounding, percent error and k: derived from the named similarity/ray sources and independently recomputed in review-numbers.py. All specified examples agree. Worst exact-tape Sun error is 1.0048%; Streetlight is 1.2931%; k is 0.2083333 at every stick position.
- Mirror at 9 m aligns for tripod 1.9708 to 2.0301 m; 9.00/2.00 gives 6.75. Tree at 25 degrees records 2.14/24.13, estimate 11.2757, displayed 11.28 and 0.2%. The rounding is honest.

## Sensitivity

None: invented schoolyard, no people images, bodies, cultural traditions, religion or hard history. All 11 assets are marked people:false, consistent with the scene's instrument-only spec.

## Flattest moment left

Remeasuring after a refused reason pair remains mechanical. Its explanation is clear, and requiring new readings prevents free option enumeration. Added no new topic or game feature to disguise that tradeoff.

## Graphics

Inspected all 11 assets and their scene placements. Kept the layered schoolyard, silhouettes, chalk, textured tapes, night glow and notebook finish. The complete hoop and cleaned edges improve the weakest art. The post-Reveal gaps and keyboard-mapped point make the result more specific to the student's actions.
Bundle 817,846 bytes (798.7 KiB); art 543,430 bytes (530.7 KiB). Compared with Beat Lab and Snowy Mail Route. Final hoop: art/sm-hoop.webp; raw original: art/raw/sm-hoop.png. Built-in imagegen prompt: ../../_scratch/shadow-measure/review-hoop-prompt.txt. No people or missing art tokens.

## Audit

Completed once within the 40-minute limit: ../../_scratch/shadow-measure/review-audit/audit.md, 71 inspected frames, 36 leads. Twelve are 0 px header words replaced by accessible 17 px glyphs; fourteen are intentional overlays on the focusable canvas or their text containers; three are allowed first-tap welcome skips; five are current-step or unmoved-handle clicks; two are the failed phone host. Repeated taps, Motion off and resize stress reported no failures.
The phone host failed because earlier test-server children survived the LibreOffice Python launcher. Independent drive.py 375 px iframe runs covered setup, measuring, refusal and Reveal; final phone repairs were re-shot. The three exact owned hosts were closed and the scratch launcher/server lifecycle corrected. All assigned ports are closed and host.html is absent. The audit was not rerun.
After the audit, fixed the confirmed Streetlight instruction regression and rechecked the full voice path, repeated events, Sound-on-during-Measure and stale crosshair behavior. The audit snapshot predates these narrow final voice changes. Corrected phone-size keys in audit-states.json for future use.
Wave lessons rechecked: current hints and Read, preserved focus and mounted controls, 44 px targets, all six reason choices visible, no free enumeration or favorable false result, stated measuring assumptions, explicit unknown heights, distinct tape/ray/bar meanings, no infinite Motion-off animation, grayscale and resize. Keyboard-only Sun reached Reveal with 1.19/10.01, focus on New trial and scrollY zero. All STANDARDS sizes were inspected. Contrast: accent/panel 12.80:1, ink/accent 13.43:1, scene ink/pill 15.94:1, night label/pill 15.42:1, chalk/blacktop 7.83:1. Figures, hashes, counts and application-error checks are in ../../_scratch/shadow-measure/review-static.json.

## Left open

- Readout timing was unspecified while the premise requires height hidden until Reveal. Chose that premise and the explicit anti-cheat requirement: keep geometric dilation exploration available, reveal numeric k after the earned result.
- The spec explicitly publishes the hoop's regulation height in Set up. Kept that required disclosure, so Hoop is a known-height calibration case rather than a blind unknown-height test.
- The finite lantern is modeled as an ideal point source at its marked top, as the spec's calibration requires; teacher notes now state that simplification.
- No questions were asked in this unattended run. No shared kit edits or git commits. One review pass; subsequent checks only verified repairs and the required final audit.
