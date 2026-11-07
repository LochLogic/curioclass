# Codex review: skate-park-angles
## Played
Grade 4, solo student and projected-class views. Played every mode, real turn drag, a correct job,
Test ride and Park Ride before codex-report.md, handoff.md, notes.md or source. Later completed the
Low session and three questions with held 120 ms clicks, two-second pacing, Sound on and Motion on.
The painted world and joined arcs feel inviting. Keep them. No second full review or audit.
## Findings fixed
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
## Findings left
- Nit, Craft: fine violet edge spill on some older cutouts. Silhouettes remain readable in context.
- Production: browser speech is the fallback; recorded big-sister takes were not supplied or created.
## Break it
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
## Voice walk
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
## Facts checked
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
## Sensitivity
All eleven people assets independently inspected for whole framing, anatomy, identity, age and ethnic
representation. The fictional mixed-age crew remains varied and friendly; no obvious stereotype found.
Cultural reviewer: retain that range and check Dev's new spin pose in context. All people:true flags present.
There is no religion, Native history, hard history or personal-body prompt.
## Flattest moment left
The sparse first plot still takes several jumps to become interesting. The earned dot now makes a visible
journey to its stack. No new topic or reward system was added.
## Graphics
All 22 finished assets inspected individually and at scene sizes, including eleven people. One redraw:
dev-spin, retained raw and prompt provenance, processed only with art.py --rekey. Strong backdrops retained.
Both reference-bar tools opened from existing bundles; no other tool bundled or edited. Contact sheets
and final-size comparisons are in Scratch. Art 594.0 KiB; final self-contained bundle 934.1 KiB (956,504 bytes).
## Audit
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
## Left open
Recorded narration and unfinished automated audit coverage remain explicit limits. Native confirmation
semantics were tested with controlled true/false returns; native Cancel/Confirm clicks are not claimed.
Secondary phone footer actions can require scrolling. No unattended deployment or owner art approval claimed.
Three initial read-only orientation commands lacked kill deadlines; subsequent commands were bounded.
The image tool retained its original in its managed cache; project references use authorized tool assets.
No commits, shared-file edits, uploads or outreach. Final report written last, once.
