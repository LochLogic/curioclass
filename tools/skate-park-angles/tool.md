# Skate Park Angles: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: skate-park-angles

#### Built

Four complete modes: Spin Deck, Ramp Shop, Jump Log and Park. Six Spin jobs with three variants each,
five Ramp jobs with three variants each, three fictional jump sessions and all nine fraction questions.
The tool uses the shared kit, exact canvas geometry, keyboard and pointer controls, local progress,
earned park pieces, whole painted characters, a saved trick and restartable rides.
Stage is built in tool.draft.json. No commits, deployment or separate polish round.
All required files are present. host.html was removed. Final size: 951,680 bytes (929.4 KiB).

#### Numbers check

PASS: check_math.py independently verified all 17 landmarks, all Spin answers, complementary ramp
readings, all nine Jump answers, maximum stacks and contrast. numbers.json preserves the result.
Answers: Low 3/8, 2, 1/8; Mid 5/8, 15/4, 9/8; Big 3/4, 9/2, 7/8.
Means: 0.425, 0.78125 and 1.125 feet. The spec's 0.78 is a rounded Mid mean, not an arithmetic defect.
Maximum stacks: 4, 5, 4. Contrast on paper: ink 14.596:1, muted 6.005:1, violet 7.642:1,
orange 4.854:1. Gray is used for a hatched unknown, with an ink label on a paper patch.
The spec lists 22 named images despite saying 20. All 22 were made. Specification tensions are in handoff.md.

#### Facts checked

- Full turns, one-degree units, additive angles, measuring and sketching:
  [CCSS Mathematics 4.MD.4-7](https://www.thecorestandards.org/Math/Content/4/MD/), checked live.
  Numerical examples were independently computed, not copied from worked answers.
- A straight angle is 180 degrees: half of the independently verified 360 degree full turn;
  the additive construction is CCSS 4.MD.7. All three rear-angle examples were recomputed.
- Read from the protractor's zero on the ground ray and use its opposing scales:
  [Math is Fun, Using a Protractor](https://www.mathsisfun.com/geometry/protractor-using.html), checked live.
- Spin names refer to rotations in degrees. The 180, 360, 540, 720 and 900 turn counts were computed.
  Tony Hawk's 1999 X Games 900 is supported by
  [Guinness World Records](https://www.guinnessworldrecords.com/world-records/first-900-on-a-skateboard)
  and the official [X Games anniversary video](https://www.youtube.com/watch?v=ItI4UWoTPCI), checked live.
- Fixed-speed ideal launch height rises with angle below ninety degrees:
  [OpenStax University Physics 4.3](https://openstax.org/books/university-physics-volume-1/pages/4-3-projectile-motion).
  The visible session data are explicitly fictional. Test-ride hop bands and the bail are story outcomes.
- Every displayed jump, skater and session total comes from the spec's fictional Curio Class dataset.
  All count, range, sum, mode and difference answers were recomputed with exact fractions.

#### Break it

62 browser assertions passed in functional-results.json; 35 additional assertions passed in
last-numeric-results.json. Positive fixtures cover every job variant; the following test the shortcuts.

- Spin fractions: 37 and 38 fail for 3/8; the full-turn reason names 360. Equivalent fractions pass.
  Jobs have no ticks or numeric readout before a result. Leaving Jobs changes the open variant.
- Total and missing-part jobs: copying known parts cannot equal their computed answers. 305 fails
  for 125 + ? = 180 and produces missAdd. The exact 55 passes. All three-part shortcut sums,
  copied labels and single subtractions tested for the first variant fail.
- Fractions: denominator zero, NaN, Infinity, expressions, negative input and trailing text are refused.
  6/16, 16/8, 3 6/8 and other equal forms are accepted for their matching questions.
- Ramp measurements: 19, 20 and 21 pass for 20. The other scale, 160, fails and loads the new 35 degree ramp.
  A second miss ends the job with help. The worked reading is highlighted on a centered protractor.
- Sketch: 24-26 pass for 25. A miss at 23 never prints 23. Explore cannot seed the job ramp.
- Dot sweeping: a wrong tick places nothing; a second wrong tap places the true height as an outlined,
  assisted dot. Taps during flight are ignored. The main walk placed all ten Low dots with real input.
- Every session question: whole numerators fail. Dot counts 4, 5 and 4 fail for the three sum questions.
  Adding denominators also fails. Assisted questions display a worked fraction equation.
- Credit: repeated checks and replays never add duplicate pieces or upgrade assisted credit.
  A ramp replay can replace its geometry while its original help flag stays true.
- Limits: real integer-pointer drags reached 720 and the 900 cap, then returned to zero backward.
  Three parts and the maximum disable Add. Arrow keys moved exactly one degree.
- Ride and Test ride are outcome displays, without checks or scores. Restart and Stop work immediately.
  Native Start over Cancel preserved two pieces; Confirm cleared them all.

#### Voice walk

Browser speech, Sound on, held presses of 120 ms and a two-second tap pace. No recorded clips were made.
Main path: wSpin, addHow, jobHow, right, wRamp, wLog, plotRight ten times, askHow, right,
missCount, right, right, sessionDone, wPark. Main-result.json records ten unassisted Low dots and three correct answers.
scaleHow became stale when that main walk left Ramp; the side walk heard it in the correct context.
Side path: wRamp, scaleHow, jobHow, missScale, sketchHow, missOther, bail, Read.
Five held correct replays: jobHow spoke once, right spoke five times. repeat-result.json preserves the log.
Mode changes may cut welcomes or obsolete instructions. First-tap Jobs speaks its own how-to, as rule 16 allows.
Read's final implementation separates readout lines into sentences and includes the current card and hint.
The inventory has 21 fixed lines and uses Curio.voice with scoped how and event kinds.
This is a scheduler and interaction check, not a listening review of a recorded big-sister voice.

#### Feel check

Played a student path through every mode, a complete Low session and its three questions, plus the wrong-scale,
sketch and bail side path. Other variants were driven as explicit fixtures.
Best moment: the Low dot stacks become the student's own record, then their session appears on the painted
park scoreboard beside the rail they earned. The dial's rotating board and joined colored wedges also feel direct.
Flattest moment one: Go at zero originally looked unchanged. It now gives Dev a ready nod, a chime and a ready cue.
Flattest moment two: dots originally appeared without a journey. They now drop into their stacks;
wrong placements shake away, and assisted placements remain visibly outlined.
The highest Big jump initially cropped the skater. The pole and figure now share a layout that keeps the whole
cutout in view, with a light measuring-pole backing for readable ticks against the painted fence.
feel-comparison.jpg puts the earned park beside Snowy Mail Route. Both named bar tools were opened.
The painted park, varied crew poses, board texture and plywood details meet the visual bar; the exact math stays clear.

#### Done when

1. PASS: focus is the stage; every standard size was shot, including the 375 iframe. Switch, card, keypad
   and Check fit. The 680 preview stays side by side. Rare phone footer actions use normal page scrolling.
2. PASS: real drag returned 135 with all four readout lines; a real arrow key returned exactly one degree.
3. PASS: 90 + 45 shows both labeled colors and the equation. Go displays 540's trick name and animates the spin.
4. PASS: 55 passes, 305 fails with missAdd, and leaving Jobs changes the variant.
5. PASS: 20 accepts 19-21; 160 fails with missScale before a new ramp. No made-angle readout appears before a result.
6. PASS: sketch 25 accepts 24-26; its miss hides the built angle.
7. PASS: Low accepts only the true dot tick. The main walk used 6/16, 16/8 and 1/8; 4 produced missCount.
8. PASS: Go and Ride restart; Stop and mode changes stop runs. Real mid-animation resizes produced no exceptions.
9. PASS: 40 shows the bail and one bail event. 30 shows the high arc and saved 540 wedge, including Motion off.
10. PASS: the 14-piece fixture has the right six props, five ramps and three scoreboard entries.
    Assisted credit is immutable, unique and labeled; privacy appears below the Park counter.
11. PASS for browser narration: once-only how lines, ten repeated plot results and five correct-check events;
    results pace the next card, and how lines use visibility and enabled-state guards. Recordings remain outside this Build.

#### Wave lessons

- Hint and voice: PASS. Hints update with state; Read includes the card. Stale scoped lines drop after a mode change.
- Focus and layout: PASS after fixes. Reused control nodes keep focus and survive rebuilding; handles stay persistent.
- Sizes: PASS for primary controls, 44 pixel HTML targets, readable diagrams and visible keypad rows.
- No giveaways: PASS. Jobs hide Explore readouts, use typed answers and reroll on leaving.
- Honest numbers: PASS. Fictional data and saved-device scope are stated. Story outcomes are identified in notes.
- Standards: PASS. Turn fractions, one-degree stepping, protractor measurement, construction, angle arithmetic
  and fraction line-plot questions all have student actions.
- Motion off: PASS. No perpetual animation runs; flight timing remains, with peak poses shown immediately.
- Short choices in view: PASS for the keypad and job navigation; compact and phone jobs use the stage pager.
- Resize mid-animation: PASS in direct CDP checks for Go, Ride and Test ride; none threw or stayed locked.
- Late welcome: PASS. No welcomeAfter queue is used; the first tap's own instruction wins.
- Unknown as unknown: PASS. Hatched unknown wedges and hidden made-angle readouts.
- One look, one meaning: PASS. Number labels identify wedges; outlined dots mean Rae placed; Low comparison uses faded rings.
- Badge truth: PASS. Help never becomes on-your-own through a replay; park counts remain unique.
- Hints change back: PASS. Clear, mode and session changes restore the appropriate next action.
- No copying words: PASS. Numeric answers are not answer choices; worked answers appear only after completion or help.

#### Audit leads

FAIL: the single full audit did not finish. It saved 140 leads, 89 frames, all size and declared-state
checks, Motion off and the first-screen control walk, then hit a 60-second mouseReleased timeout at Park's
native confirmation. The snapshot is audit-input.html, SHA256 821e9db3eeb5fe7fd8de7b192c4ace92c7d2b2902223fbcec65c42b8fdd83e37. The final bundle differs.
No second audit was run. The remaining repeat and stress stages in that partial report are not claimed complete.

Every saved lead is covered by these dispositions:
- Small Park and Read buttons: fixed with a 44 pixel floor and fixed utility widths. Final measured widths pass.
- Sound toggle shifting header controls: fixed by reserving utility widths. Sound off at 680 has zero horizontal overflow.
- Reset below the fold: compact avatar removal and phone spacing fix default Explore cases. Primary inputs and
  Check stay visible. Rare Start over and footer controls may require phone page scrolling; retained, not hidden.
- Canvas overlapping tags, readouts, pager and drag handles: intentional layered scene controls, not obscured math.
  The canvas is one full-stage input surface; its accessible name is not painted text.
- Stage tag under the compact pager: fixed by hiding that decorative tag in compact and phone Jobs.
- Move handle over the hint: fixed by moving the handle into the protractor's open center area; final boxes do not intersect.
- Hidden #hint in compact Jobs: its visible copy is #sceneHint. Read uses the same current text. Retained intentional layout.
- Canvas keep samples covered by handles: intentional controls on the same scene, not missing canvas content.
- Job/session focus fell to body and Jobs was rebuilt: fixed with stable ids and reused button/input nodes.
  Real final clicks verified object identity and focused job-3 / session-2.
- Dropped Add how-to: the audit used Add before its queued instruction played; Add then became disabled.
  That instruction correctly became stale. It was heard on the main student path.
- Welcome not heard when the first tap is Jobs: its own jobHow speaks instead, allowed by BASELINE rule 16.
- Native-confirmation timeout: app behavior retained. Direct Cancel and Confirm tests pass. Harness change requested in handoff.md.

#### Frames looked at

All 89 saved audit PNGs were inspected through audit-contact-0 to audit-contact-9.
Inspected first, matrix, retry, extra, targeted, numeric, student-walk, host, post-audit, closing and extreme
frames through full-size views and labeled contact sheets. Failed harness frames are not claimed as final evidence.
Final proof includes whole highest-jump skaters, the phone Jobs pager and full keypad, the assisted protractor
reading, the calm high arc, stable focus and the cleared confirmation result.

#### Art made

22 generated images, 11 marked people true. Finished art: 595.2 KiB. Voice files: 0 KB.
Bundle: 951,680 bytes (929.4 KiB), comfortably inside the 2 MB goal. All art uses the built-in image tool and --rekey processing.
Bench and light were redrawn once because the first attempts included park scenery instead of a clean cutout.
Final contact sheet: art-contact-final.jpg. All 22 listed assets appear in the tool.

#### Art still to paint

None. The people set still needs its independent cold-review check before shipping.

#### Engine changes wanted

No family engine changes. The audit harness should dismiss and record native dialogs during probes;
the driver should safely quote CSS selectors. Exact files, functions and reasons are in handoff.md.

#### Left open

- The full mechanical audit is incomplete after the native-confirmation timeout. Direct focused checks passed;
  a reviewer can run the remaining audit after the harness handles dialogs.
- Browser narration is implemented; no bank recordings were made because recording was explicitly out of scope.
- Secondary phone footer actions can require scrolling. Primary gameplay controls remain visible.
- The named bar-tool bundling commands wrote their ignored bundles outside the two authorized folders.
  No source in those tools was edited. Four initial read-only orientation commands also lacked an internal kill timeout;
  subsequent shell commands used explicit deadlines. These scope/process exceptions cannot be undone by later checks.
- All test Chrome processes and host servers closed; assigned ports are not listening.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: skate-park-angles
#### Played
Grade 4, solo student and projected-class views. Played every mode, real turn drag, a correct job,
Test ride and Park Ride before codex-report.md, handoff.md, notes.md or source. Later completed the
Low session and three questions with held 120 ms clicks, two-second pacing, Sound on and Motion on.
The painted world and joined arcs feel inviting. Keep them. No second full review or audit.
#### Findings fixed
- Blocker, Teaching/Play, sketch: fifteen Down presses solved its fixed offset. Starts now vary,
  remain at least ten degrees from target, and the same rhythm fails. Tested both tolerance boundaries.
- Blocker, Teaching/Play, measurement: Explore Show angle and the Park ramp label gave the next answer.
  Entering measurement Jobs avoids the current Explore angle, even with Show angle off. Both routes fail.
- Blocker, Teaching/Play, Jump questions: reload during reveal discarded assistance. Help is now saved
  before speech; a real reload retains it, and replay cannot upgrade an assisted award.
- Should fix, Craft, measure: a shared animation token could cancel a pending reroll and strand Check.
  A separate card epoch guards it. Source-found risk; fast protractor input now leaves Check available.
- Should fix, Teaching/Craft, voice: Jump misses named a nonexistent tip and resumed questions gave
  jump-placement instructions. Added missLog, resumed with askHow, and made opened job tips readable.
- Should fix, Craft, compact/phone: question hints and results slipped below the keypad. A scene copy
  and reserved axis space keep them visible. Narrow tick-step/place controls use the same scoring gate,
  have 44 px targets, wait during flight, and focus the first answer key after the last dot without scrolling.
- Should fix, Teaching/Craft, Spin: beyond 360 the disc lost the remainder. Current-lap sweep plus lap
  rings now distinguish 540 and 900 in Explore, Test and Park. A solved unknown wedge now shows its value.
- Should fix, Craft, Park: scoreboard text straddled its frame, props overlapped ramps and help tags
  lacked contrast. Separated depths, fitted the face text and added paper-backed assisted labels.
- Should fix, Craft, audit frames: compact Reset clipped, portrait Dev covered the readout, and Low
  overlay rings matched assistance in grayscale. Fitted footer controls, repositioned the whole figure,
  and dashed/labeled Low rings. Short Test figures/badges stay whole; success button now says Done.
- Polish, Play: earned dots travel from the jump to their stack over a chalk-textured plot. Dev's
  spin no longer squeezes to a thin stripe and its pose timing follows the actual turn duration.
- Should fix, Teaching/Craft, art: detached-board spin looked like a flip. Regenerated dev-spin with
  shoes on grip tape and wheels below the deck, matching the gouache crew.
#### Findings left
- Nit, Craft: fine violet edge spill on some older cutouts. Silhouettes remain readable in context.
- Production: browser speech is the fallback; recorded big-sister takes were not supplied or created.
#### Break it
203 browser assertions pass in review-score-final.json, using independently specified expected answers.
- Spin 1-2: percent-of-100, rounded percentages and copied fraction numerals fail; exact degrees pass.
- Spin 3: wrong fractions and degrees/100 fail; equal forms such as 120/360 pass.
- Spin 4-6: copied parts, addition instead of subtraction and incomplete subtraction fail.
- Measurement: all nine variants accept only +/-1 degree; opposite scales fail. Copying Explore or
  Park's angle fails through real controls; six matching-angle entry cases also pass the guard test.
- Sketch: fixed fifteen-key rhythm fails; 48 varied starts and +/-1 versus +/-2 were checked.
- Jump dots: flight mashing is ignored; wrong ticks fail; tick sweeping records Rae's help.
  Seven real-touch regressions pass, including final-dot focus, visible targets and immutable help.
- All nine questions reject counts, whole numerators and wrong operations; equivalent fractions pass.
  Help survives reload during reveal. Fourteen unique pieces cannot duplicate or upgrade assisted credit.
- Malformed input, zero denominators and expression-like entries cannot award. Ride/readouts carry no score.
Fixtures cover every variant and full Park; the main Low session used ten real placements and real keypad input.
Dial drag reached 900 and returned to zero; three-part cap, min/max ramp, bail and rotated protractor were checked.
#### Voice walk
review-main/main-result.json has seven passing checks, no console exceptions, and these spoken starts:
addHow, jobHow, right, wRamp, scaleHow, right, wLog, plotRight ten times, askHow,
right three times, sessionDone, wPark. The protractor was manually re-centered on the new 35-degree job.
Initial drag skipped wSpin under baseline rule 16; welcome content stayed in hint/Read. Mode changes
cut stale lines; a spoken start is not a claim that its whole utterance finished before the next action.
| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| jobHow | how | 1 in five replays | 1 |
| right | event | 5 in five replays | 5 |
| plotRight | event | 10 Low dots | 10 |
| addHow, scaleHow, askHow | how | 1 each on main path | 1 each |
Resumed questions speak askHow then missLog; sketchHow and bail fit their side paths. Read works with
Sound off; fast mode changes and Reset clear stale speech. Opened-tip Read was separately checked.
These are browser scheduler/log checks, not recorded-voice listening QA.
#### Facts checked
- Full turn 360 degrees, unit 1/360, n units = n degrees, angle addition and straight-line subtraction:
  [CCSS Grade 4 MD](https://www.thecorestandards.org/Math/Content/4/MD/).
- Protractor center, ground-ray zero and opposing scales:
  [Math is Fun, Using a Protractor](https://www.mathsisfun.com/geometry/protractor-using.html).
- 180/360/540/720/900 = half/one/one-and-a-half/two/two-and-a-half turns: exact arithmetic.
  Hawk's first 900, June 27, 1999, San Francisco X Games:
  [Guinness](https://www.guinnessworldrecords.com/world-records/first-900-on-a-skateboard),
  [official X Games anniversary](https://www.youtube.com/watch?v=ItI4UWoTPCI).
- Higher ideal peak at fixed launch speed as angle rises from zero to ninety, with stated assumptions:
  [OpenStax 4.3](https://openstax.org/books/university-physics-volume-1/pages/4-3-projectile-motion).
- Fictional spec datasets independently recomputed with Fraction: Low 3/8, 2, 1/8; Mid 5/8, 15/4, 9/8;
  Big 3/4, 9/2, 7/8. All 17 turn landmarks agree. Fraction plot operations follow CCSS 4.MD.4 above.
- Hop bands and Dev's bail are fictional story rules, not safety thresholds or calibrated physics.
  Teacher notes explicitly say so; no unsupported safety or medical claim was added.
#### Sensitivity
All eleven people assets independently inspected for whole framing, anatomy, identity, age and ethnic
representation. The fictional mixed-age crew remains varied and friendly; no obvious stereotype found.
Cultural reviewer: retain that range and check Dev's new spin pose in context. All people:true flags present.
There is no religion, Native history, hard history or personal-body prompt.
#### Flattest moment left
The sparse first plot still takes several jumps to become interesting. The earned dot now makes a visible
journey to its stack. No new topic or reward system was added.
#### Graphics
All 22 finished assets inspected individually and at scene sizes, including eleven people. One redraw:
dev-spin, retained raw and prompt provenance, processed only with art.py --rekey. Strong backdrops retained.
Both reference-bar tools opened from existing bundles; no other tool bundled or edited. Contact sheets
and final-size comparisons are in Scratch. Art 594.0 KiB; final self-contained bundle 934.1 KiB (956,504 bytes).
#### Audit
Audit not finished: one run, 40-minute kill deadline, Chrome 9961 / host 8765. A native-confirmation CDP
timeout stopped it after about 18.5 minutes. Partial audit.md has 136 leads and 106 inspected PNGs.
Seven nonphone STANDARDS sizes, declared states, Motion off and opening controls ran. Phone iframe lookup
failed. Remaining mode walks, repeat/resize and stress sections are incomplete; blank clean rows prove nothing.
Canvas/DOM overlay, pointer-events hit-test and keep-region leads were checked on frames: intentional
readouts, handles and captions stayed visible. Compact hidden hints had visible scene copies plus Read.
Confirmed clipping/portrait leads were fixed and re-shot at affected sizes; grayscale and saved-spin badge
checks also passed. Dropped addHow followed already-filled slots; the real main path heard it once.
First Jobs uses jobHow in place of welcome under baseline 16. Iframe/noHint errors belong to the harness;
manual 375x812 same-origin host checks covered all modes and touch. Engine requests are in handoff.md.
Audit input hashes remain in review-input-manifest.json; final hashes differ after these scoped repairs.
Targeted post-audit frames report zero app console errors. A lost concurrent Chrome connection was retried
once sequentially; the failed run is retained. No second audit was run.
#### Left open
Recorded narration and unfinished automated audit coverage remain explicit limits. Native confirmation
semantics were tested with controlled true/false returns; native Cancel/Confirm clicks are not claimed.
Secondary phone footer actions can require scrolling. No unattended deployment or owner art approval claimed.
Three initial read-only orientation commands lacked kill deadlines; subsequent commands were bounded.
The image tool retained its original in its managed cache; project references use authorized tool assets.
No commits, shared-file edits, uploads or outreach. Final report written last, once.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Skate Park Angles build handoff

Build only. No commits, deployment or separate polish round. The tool remains a draft for cold review.

#### Files and structure

`src.html` starts from the kit starter structure and imports kit:curio for the shared frame, speech,
Motion, Sound, Read and chimes. Its CSS selects desktop, short landscape and phone layouts.
The canvas draws at the stage's actual pixel size, with a device pixel ratio capped at two.

The script has four parts: fixed content and state; panel and job logic; canvas painting;
pointer and keyboard input. Images are embedded from the explicit art token map. There are no data files to fetch.
`voice/lines.json` is the complete big-sister inventory. Browser speech is the Build fallback;
no recording service was called. `tool.draft.json` has stage built. The ignored HTML is the offline bundle.

#### Tricky behavior

- Dial drag keeps a floating accumulator and rounds the complete turn, rather than rounding every mouse delta.
  This avoids drift with jittered integer input. It unwraps across zero and clamps at zero and 900 degrees.
- Explore and Jobs have separate ramps. Leaving Jobs changes the open variant. Jobs hide dial ticks,
  numeric ramp readouts and the sketch's made angle. A measure miss speaks before drawing the new ramp.
- The rear angle of a 30 degree bank is 150 degrees, but the earned ramp is stored as a 30 degree ramp.
- Every piece is recorded once. A replay never upgrades a piece initially completed with help.
  Dot assistance also carries into the session's on-your-own credit.
  Ramp geometry can still be replaced by replaying its job, so a steep bank does not permanently block the run.
- Jump placement is locked during the flight and during the result beat. Tokens cancel late callbacks
  when a mode or session changes. Dot landings are animated; Motion off keeps the pacing.
- Each plotted dot retains its jump index, skater and assistance flag. Clicking different rows of a
  completed stack inspects different jumps. Keyboard arrows select a tick; up and down select a stack row.
- The protractor uses two opposing scales. Small scenes label every twenty degrees and retain every
  one-degree tick, avoiding overlapping labels. Drag snapping is separate from two-pixel keyboard movement.
- Check is a strict number/fraction parser, not JavaScript evaluation. Zero denominators and malformed input
  do not use a try. On first completion, job results remain for their spoken beat, then the next unfinished
  job appears silently. The pager also allows immediate navigation.
- The protractor and lip use persistent HTML handles. Canvas redraws do not hide and unhide the focused handle.
  Add uses aria-disabled so reaching the third part does not drop keyboard focus.

#### Decisions and specification tensions

There are no spec Open questions. No unattended question needed an answer from the owner.

1. The Art section says 20 images but names 22. All 22 named images were made and placed.
2. A 1100 pixel plot cannot fit the stated roughly 900 pixel stage at 1366x768. All thirteen ticks
   remain; spacing follows the actual canvas width. Mathematical values do not change.
3. The generic job pager says six jobs; Ramp's content lists five. Ramp uses five, Spin uses six.
4. The generic workshop switch wording is broader than Jump Log's detailed screen. Jump Log follows
   the detailed session controls and post-session dot exploration, without an unrelated Jobs switch.
5. The command to start a report on the first bundle conflicts with the user's instruction to stop
   when codex-report.md is written. An early draft was kept in Scratch; the final report is written last.
6. The two named bar tools were bundled and opened as CODEX-BUILD requires. Those commands wrote their
   ignored generated bundles outside this tool's two allowed directories. No source in another tool was edited.
   This was an avoidable write-scope exception, preserved here rather than hidden.
7. Native image generation produced a three-to-one ground panorama for the requested four-to-one strip.
   It is framed responsively as a background. The precise ramp, protractor and jump guides are drawn in code.
8. The voice section says the lines contain no numbers, but its supplied missHundred line contains
   360 and 100. The explicit fixed reason is kept verbatim; variable card numbers are still read by Read.

#### Sensitivity

The fictional crew contains children, a teen and an older adult. Eleven assets show people and every one
is marked people true. Dev has brown skin, Mina is East Asian, Rae has red curls and freckles, and Walt has
a gray beard. All wear helmets; the children and teen have knee pads. The bail is friendly and uninjured.
The jump measurements are explicitly invented. Hop bands and the bail threshold are story rules, not
medical advice, skateboarding instruction or measured physics. There are no personal prompts, religion,
Indigenous content or hard history. Before shipping, a fresh reviewer should check the people contact sheet
for consistent identity, natural anatomy, respectful age and ethnic representation, and readable cutout edges.

The contact sheets, raw generation provenance and evidence are under `_scratch/skate-park-angles/`
and `art/raw/`. Bench and light each needed one redraw to remove scenery from the requested cutout.

#### Verification evidence

- `check_math.py` and `numbers.json`: independent fractions, sums, contrast, datasets and maxima.
- `functional-results.json`: 62 actual browser assertions over job variants, tolerances and gates.
- `last-numeric-results.json`: 35 additional assertions over all questions and common shortcut answers.
- `student-walk/main-result.json`: held-click main path, ten real dot placements, equivalent answers and voice log.
- `student-walk/side-result.json`: protractor snap, wrong scale, sketch instructions, bail and Read.
- `matrix-frames-*`, `matrix-retry-*`, `targeted-frames`, `last-frames`, `host-frames`: inspected screenshots.
- `audit/audit.md`: single bounded mechanical audit, with any leads answered in codex-report.md.

An early numeric fixture expected the fifth jump for stack row three; the correct jump was the sixth.
That test expectation was corrected and rerun. An initial scripted drag omitted the stage's header offset;
the corrected real drag reaches exactly 135 degrees. The initial host's favicon 404 belonged to the test
parent page, and was removed by an inline icon in that parent. Final host runs have no console errors.
Two concurrent screenshot batches lost their Chrome connection; successful frames were retained and missing
coverage was retried in smaller batches. These were harness failures, not claimed passing tool runs.

#### Engine changes wanted

No family engine changes. No shared files were changed.

Audit harness request: `scripts/audit_tool.py`, `press()` / `walk_mode()`, should handle
`Page.javascriptDialogOpening` during a control probe, dismiss the confirmation and record its text.
The required native Start over confirmation blocks the mouseReleased response, so the audit exits
with a 60 second CDP timeout after the first-screen walk. Keep the user's real confirmation behavior.
The final build has separate direct CDP tests for both Cancel and Confirm; the audit was not rerun.

Driver request: `scripts/drive.py`, `main()` selector evaluation, should quote selectors with `json.dumps(sel)`.
Interpolating a selector containing double quotes into a double-quoted JavaScript string breaks otherwise valid CSS.
The build's real-input fixtures use single-quoted attribute selectors to avoid that harness issue.

#### Next review

Do the cold build review, including a fresh people-art review. Recorded big-sister narration is still a
production step; this Build session was instructed not to record. Do not treat browser voice logs as
a listening review of the bank voice. Final audit dispositions and any remaining limits are in codex-report.md.

#### Cold review repairs

- Sketch starting angles now vary within 5 to 60 degrees, always at least ten degrees from the target.
  The former fixed fifteen-degree offset was reproducibly solved by fifteen arrow presses without measuring.
- Jump-question assistance is persisted before the answer reveal. Reloading during speech retains the help flag.
- Entering measurement Jobs avoids the current Explore angle, including a value copied from Park's ramp label.
  Show angle also retains its true aria-pressed state. Default first measure is now 35 after the default 20 Explore ramp.
- A card epoch, separate from the animation cancellation token, guards a pending measure-result reroll.
  Moving the protractor during a reason line must not leave Check permanently busy.
- Resuming at questions welcomes with askHow; generic wrong fraction answers use missLog, matching the plot hint.
  There is no nonexistent Rae tip control in this question path. The voice inventory includes the new fixed line.
  Opening Rae's actual job tip also updates the current hint, so Read speaks that tip.
- Compact question and wrong-answer instructions have a scene copy. Question plots reserve its space below
  the axis, rather than covering eighth labels. Spin result readouts and Dev sit above the result caption.
- Explore sweeps beyond 360 show the current lap's arc and a ring per completed turn. One-degree protractor
  ticks remain at small sizes. Snapping changes the hint to the scale instruction at once.
- Successful dots travel from the jump scene to their stacks. Motion off retains timing and the settled dot.
- Narrow layouts expose the existing tick-step/place interaction as three 44 pixel controls. Direct plotting
  remains available. They use the same plot gate, wait during flight, and transfer focus to the first answer key
  after the last dot, without scrolling or opening a phone keyboard. Selected height is a live status.
- Park props occupy the middle ground, clear of the ramp slots. All three log lines fit the scoreboard face;
  compact scoreboard wording retains each session name and count.
- Final audit leads: compact Park now keeps Reset visible; compact Jump puts reset before secondary data notes.
  Portrait Spin figures avoid the readout. Low comparison rings are dashed and labeled to distinguish assistance
  in grayscale. Test and Park spin badges use the same remainder/lap geometry as the dial, positioned beside
  the skater when an overhead badge would leave the frame. Short-screen Test figures retain their whole silhouette.
- Dev's mid-spin art was regenerated in the same style with both shoes on the grip tape and wheels below.
  Raw: art/raw/dev-spin.png. Prompt/provenance: art/prompts.json. Built-in OpenAI image tool, then art.py --rekey.
- Cold reviewer inspected all 22 final assets, including the eleven people cutouts. The varied fictional crew
  remains friendly and respectful; no obvious stereotype or frightening anatomy was found. Owner contact-sheet
  review before live shipping remains a baseline requirement, not an unattended deployment authorization.

Fresh evidence uses review-* and cheap-*-after files under Scratch. The final 203 browser assertions are in
review-score-final.json. review-main/main-result.json records seven passing real-input checks and actual voice starts.
The cold review audit did not finish: 136 leads and 106 frames survive in review-audit/. Native confirmation
blocked its held-click walk; its phone iframe lookup also failed. Audit.size() needs child-context diagnostics.
All frames were inspected and confirmed layout leads were fixed, then re-shot at their affected sizes.
Remaining audit mode walks, repetitions and stress checks were not completed. Native Cancel/Confirm semantics
were checked with controlled confirm return values in the cold review, not a claimed native-dialog click test.
The post-audit frame set, touch controls and default-voice main path had no application console errors.
The cold reviewer did not edit the spec, kit, scripts, any other tool, or make commits.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
