# Codex report: skate-park-angles

## Built

Four complete modes: Spin Deck, Ramp Shop, Jump Log and Park. Six Spin jobs with three variants each,
five Ramp jobs with three variants each, three fictional jump sessions and all nine fraction questions.
The tool uses the shared kit, exact canvas geometry, keyboard and pointer controls, local progress,
earned park pieces, whole painted characters, a saved trick and restartable rides.
Stage is built in tool.draft.json. No commits, deployment or separate polish round.
All required files are present. host.html was removed. Final size: 951,680 bytes (929.4 KiB).

## Numbers check

PASS: check_math.py independently verified all 17 landmarks, all Spin answers, complementary ramp
readings, all nine Jump answers, maximum stacks and contrast. numbers.json preserves the result.
Answers: Low 3/8, 2, 1/8; Mid 5/8, 15/4, 9/8; Big 3/4, 9/2, 7/8.
Means: 0.425, 0.78125 and 1.125 feet. The spec's 0.78 is a rounded Mid mean, not an arithmetic defect.
Maximum stacks: 4, 5, 4. Contrast on paper: ink 14.596:1, muted 6.005:1, violet 7.642:1,
orange 4.854:1. Gray is used for a hatched unknown, with an ink label on a paper patch.
The spec lists 22 named images despite saying 20. All 22 were made. Specification tensions are in handoff.md.

## Facts checked

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

## Break it

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

## Voice walk

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

## Feel check

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

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

All 89 saved audit PNGs were inspected through audit-contact-0 to audit-contact-9.
Inspected first, matrix, retry, extra, targeted, numeric, student-walk, host, post-audit, closing and extreme
frames through full-size views and labeled contact sheets. Failed harness frames are not claimed as final evidence.
Final proof includes whole highest-jump skaters, the phone Jobs pager and full keypad, the assisted protractor
reading, the calm high arc, stable focus and the cleared confirmation result.

## Art made

22 generated images, 11 marked people true. Finished art: 595.2 KiB. Voice files: 0 KB.
Bundle: 951,680 bytes (929.4 KiB), comfortably inside the 2 MB goal. All art uses the built-in image tool and --rekey processing.
Bench and light were redrawn once because the first attempts included park scenery instead of a clean cutout.
Final contact sheet: art-contact-final.jpg. All 22 listed assets appear in the tool.

## Art still to paint

None. The people set still needs its independent cold-review check before shipping.

## Engine changes wanted

No family engine changes. The audit harness should dismiss and record native dialogs during probes;
the driver should safely quote CSS selectors. Exact files, functions and reasons are in handoff.md.

## Left open

- The full mechanical audit is incomplete after the native-confirmation timeout. Direct focused checks passed;
  a reviewer can run the remaining audit after the harness handles dialogs.
- Browser narration is implemented; no bank recordings were made because recording was explicitly out of scope.
- Secondary phone footer actions can require scrolling. Primary gameplay controls remain visible.
- The named bar-tool bundling commands wrote their ignored bundles outside the two authorized folders.
  No source in those tools was edited. Four initial read-only orientation commands also lacked an internal kill timeout;
  subsequent shell commands used explicit deadlines. These scope/process exceptions cannot be undone by later checks.
- All test Chrome processes and host servers closed; assigned ports are not listening.
