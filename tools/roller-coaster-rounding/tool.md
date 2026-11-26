# Roller Coaster Rounding: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: roller-coaster-rounding

#### Built
Built in `S:\CurioClass-codex`. Writes are confined to the named tool and its Scratch folder. No commits, publication or polish round.

Three modes: an interactive rounding hill; nine place-value arithmetic cards, four clerk checks and generated queues; train exploration and seven cards. Eight generated illustrations are embedded in one offline HTML file. Metadata remains `tool.draft.json`, stage built.

The shared number-line engine was missing. The required subset is tool-local; no shared files were changed. The close hill replaces the simultaneous ten-hill panorama. See handoff for spec conflicts and remaining engine work.

#### Numbers check
`_scratch/roller-coaster-rounding/recompute.py` independently checked every integer 0 to 1000 on both tracks, every legal addition and subtraction pair, every card, train calculation and specified text contrast.

Required drops: 44→40, 45→50, 47→50, 349→300, 350→400, 995→1000, 0→0, 1000→1000. Actual asynchronous drops also passed in `behavior-result.json`.

Line estimates/exact: 600/624, 390/391, 70/68, 230/235, 800/752, 810/802, 200/264, 900/900, 620/625. Largest absolute estimate gaps over the full legal pair space are 10/100 for addition and 9/99 for subtraction, for tens/hundreds respectively.

Train tens/seats: 24/240, 21/210, 72/720, 30/300, 16/160, 28/280, 24/240. Capacity differences are 2 spare and 38 waiting. Three hundred generated rider cards passed bounds, stretch and regroup checks.

#### Facts checked
- Rounding to tens/hundreds, place-value arithmetic within 1000 and one digit times multiples of ten: [Common Core Grade 3 NBT](https://www.thecorestandards.org/Math/Content/3/NBT/), verified live.
- Equal midpoint distances and choosing the higher benchmark by convention: [Illustrative Mathematics, Grade 3 Unit 3 Lesson 15](https://im.kendallhunt.com/k5/teachers/grade-3/unit-3/lesson-15/lesson.html), verified live. The UI calls this the park rule.
- Ten ones per ten, ten tens per hundred, every displayed equation, distance, ticket count and capacity: derived from place value and independently checked by the scripts above.
- The sensible stretch is an estimate check, not proof. Its one-station error bound was recomputed exhaustively. Clerk 4 demonstrates an incorrect answer inside the stretch.
- Hilltop Park, seats, station brakes and the ride are fictional model rules, stated in teacher notes. There is no claim about real coaster capacity or physical stopping behavior.
- Measured text contrasts: ink/paper 14.44:1, muted/paper 5.89:1, brand/paper 5.46:1, white/brand 5.88:1, white/button 7.91:1, focus/paper 4.81:1. Scene labels use pale backing or strokes over the variable painted background.

#### Break it
`audit-fixed-functional.json`: 769 assertions passed, using the real state-machine actions and independent arithmetic.
- Wrong station choices do not advance. A wrong estimate cannot open columns or clerk judgment.
- The centered estimate axis and future numeric column totals initially leaked answers. Fixed: pre-estimate ticks are always 0 to 1000, and all unentered column totals stay unknown. Copying a fixed middle tick fails every fixed card. Exact totals cannot skip the column work. Every column rejects a wrong entry. Next refuses an unbundled count of ten or more. A short Take away changes nothing, and typing a remainder before Take away is refused.
- All nine fixed cards require the right counts and trades. Replaying one cannot increase the completion set.
- An unnecessary subtraction break initially risked trapping a student with more than nine pieces. Fixed by permitting a reverse bundle after the remainder is entered; the adversarial extra-break path now continues legally.
- Makes sense on either big clerk slip is refused. Far off on either inside answer is refused. The sneaky card requires selecting tens and replacing 8 with 9; typing 391 before selecting a column cannot finish it.
- Seats entered before tens do not advance a Train card. Cars as seats, an extra zero and addition instead of multiplication are refused with distinct coaching. Both capacity cards reject the wrong judgment.
- Typed 1001 preserves the old Track value. Empty Enter does nothing. The keypad accepts at most four digits.
- The board is a count of completed activities, not a score or mastery claim. Corrective feedback deliberately allows a later correct answer after mistakes. Exhaustive answer guessing cannot be made impossible without changing the specified unrestricted practice design; this limitation is explicit in handoff.

#### Voice walk
Twenty-four fixed lines use `Curio.voice`; upbeat-guide / Zephyr is declared for later recording. No audio was recorded. Current speech uses the kit's browser fallback.

Held clicks used 0.12-second presses at a two-second tap pace. Main path heard wTrack, rollRight, wLine, estimate, cols, bundle, check and wTrains. Repeated bundle became silent after its first hearing. Deliberate mode changes cut current speech and cancel a pending lap immediately.

The long Line welcome initially delayed the station how-to past its step. Its final wording names the station action directly. The final train-card welcome uses tens instead of the exploration welcome, so it never asks for fixed steppers. Final traces heard the Line welcome and the Train card's tens then seats instructions.

Ten real held Drop clicks: rollLeft spoke twice and rollRight twice, then chimes only. `ten-drops-voice.json` retains the full log. Read/Sound interruption and lap sequencing evidence are in the final interaction files. A real live lap ended and switched mode in 2.6 milliseconds. The final keypad how-to is available through Read.

#### Feel check
Best moment: the halfway car rocks over two equal dashed distances, the park rule appears, then it rolls forward. Completing manual ticket trades earns the riders lap and the Open sign.

Flattest moment 1: the first compact panel clipped entry and reset. Rebuilt the compact controls as a small control desk, with Keys opening the keypad; all main controls now stay visible.

Flattest moment 2: ticket strips initially read as tiny orange lines and piles could clip. Changed them to ten individually painted tickets, kept the two source rows separate until entry, sized each pile from its count, and added a carried-piece tag and trade motion. Dense array labels were also shortened to 100 on compact views.

Looked at the existing Snowy Mail Route and Beat Lab bundles and their source. `bar-comparison.png` puts the tool beside Snowy Mail Route. The park is richer in painted detail and its exact controls remain readable. Long column work is a lesson activity; the missing full panorama/zoom is the clearest remaining finish gap.

#### Done when
1. PASS with documented small-screen size adaptation: stage focus and needed controls fit the required sizes, including 375 through the host. A literal 520 by 300 bin is impossible in the smaller stage.
2. PASS: first Drop takes 47 to 50 in about one second, with both distances and result.
3. PASS: all eight required actual drops passed. Halfway cases teeter with the rule; stations stay, left and right use different short bold spans.
4. PASS: all nine exact cards and trade/refusal checks passed.
5. PASS: both big slips require Far off, the correct inside card accepts Makes sense, and the sneaky card fixes to 391.
6. PASS: all seven Train cards and distinct 24/2400/46 coaching passed.
7. PASS: new values and mode changes cancel rolls; card changes cancel laps. Final live-lap interruption result is recorded separately.
8. PASS for event limits and sequencing; fixed recordings remain absent as instructed. Ten held drops produced two left and two right spoken events. The lap awaits its event promise.
9. PASS: no running animations in the Motion-off result frame. The still riders lap retains its four-second timing.
10. PASS: no score, timer, lock or saved board. Sets prevent repeat-count inflation; reload starts fresh.

#### Wave lessons
- Hint and voice: PASS with the documented fast-path stale how-to behavior. Hints update synchronously, name the next control and remain available to Read. Welcome text now contains the essential action.
- Focus and layout: PASS in keyboard Drop and tab-to-mode runs. The panel is static; scene focus is restored by id, using preventScroll. No focus is taken on load.
- Sizes: PASS in measured drive frames after increasing the narrow Line tab to 44 pixels. Controls stayed in view with no horizontal page overflow.
- No giveaways: PASS for hidden Train chain results and no correctness-specific station styling. Exact pieces are intentionally countable. Free correction remains a practice limitation, not an assessment score.
- Honest numbers: PASS. Estimates and exact answers are distinct; notes explain the stretch. Every board badge describes activity only.
- Standards: PASS for student actions covering all three standards; shared-engine/family-doc conformance remains open because of the write boundary.
- Motion off: PASS, explicit animation-none rules and zero running animations in the measured frame.
- Short choices: PASS, both station options, judgment options and capacity options fit together; long card lists use native pickers.
- Resize mid-animation: PASS: the completed audit found no resize exceptions or stuck controls. Targeted final-bundle resizing also kept the roll result and preserved an unsubmitted keypad value.
- First-tap welcome: PASS, starts after the action decision and can be cut; no welcomeAfter is used.
- Unknown stays unknown: PASS, card tens/seats and unentered current and future counts use question marks.
- One look, one meaning: PASS, warm tickets, teal cars, amber stretch and explicit labels; short distance also differs by weight, halfway by dashes.
- Badges true: PASS, no Open sign until a completed exact/card path; the completion set is not a mastery score.
- Hints change back: PASS, resetting or changing a card restores the round/count instruction immediately.
- No answer by matching words: PASS for numerical entries and regroup actions. Wrong-answer coaching explicitly teaches, as the spec requires.

#### Audit leads
The full audit completed once within the 40-minute limit, using Chrome 9991 and host 8795. It recorded 140 leads on the preserved pre-fix `audit-input.html`. It was not rerun after repairs. The initial optional launcher hit an OS execution denial; the normal bounded command then completed. Dispositions below group every duplicated lead by its cause.

- Guess station labels counted as overlap with their own hit target: fixed by putting the labels inside the control group.
- Distance labels touched generous station hit bounds at small widths: moved the spans down ten pixels.
- Rotated transparent car target bounds overlap neighboring ticks: intentional enlarged drag target; inspected pixels remain legible. Removed the redundant floating car number that really collided with the narrow Hundreds header.
- Park title behind card banners, and Welcome to touching the range heading at 760: hide the unused title in Line/Trains and narrow views.
- Result car/346 label touching a station choice at 1280: separated the station-choice row from the result line.
- Last array row touching the seat readout: reduced the row budget, preserving all 81 cars; refreshed maximum and capacity-array frames show a gap.
- Compact keypad targets were 34 to 37 pixels: changed the popup to four columns. Final measurements found no target below 44 pixels, and Close keys is uncovered and usable.
- Popup overlaps with inactive pan controls, number input, launcher and Reset: the background is now inert while entry is open. Close keys, Enter and Escape close it; the keep-region contract no longer incorrectly demands the inactive Reset during the overlay.
- SVG guess/car and Line rounding clicks lost focus: restore the stable id, or move to number entry when the completed step disappears. Guess focus and round/Next/Take focus were checked directly.
- Train stepper focus lost at the second Enter at a limit: rescue focus to an enabled neighboring stepper. Maximum/minimum checks retained useful focus and respected one-to-nine bounds.
- Sound and Hundreds controls shifted other controls: keep the Sound caption stable and put the extra ten-step row where the Tens pan row was. Final Drop movement on track switch was zero pixels.
- Line/Trains numeric keys flagged as nothing changed: these update the input value, which that audit signature misses. A held-key trace entered 600 while leaving Round unadvanced. Empty Back/Enter and Start over at the default are intentional no-ops. Explore now names the card picker if an answer is entered without a card.
- First-tap Drop/Hundreds welcomes and quick-tap welcome cuts: permitted by BASELINE rule 16. Own actions respond immediately; the premise and next action remain in hints/Read. No welcomeAfter is used.
- Five-held-click voice checks were clean. Motion-off and resize sections were clean. No console exception leads were reported.

Post-fix evidence: `audit-fix-drive.log`, `closing-drive.log`, `phone-final-keys.log`, `resize-check.log`, `resize-keypad-final.log` and `word-proof.log`. Targeted frames measured no undersized visible controls, no controls outside the window, no console errors and correct focus. The final ports 9990, 9991 and 8795 were closed; all launched drivers completed their cleanup.

#### Frames looked at
All drive PNGs in early-frames, test-frames, late-frames, phone-frames, extra-frames and final-input-frames were opened. This covers the seven standard desktop/preview sizes, phone host, three modes, 81-car extreme, tickets, midpoint, grayscale, calm result/lap, keyboard and dragging. Also opened all last-frames, audit-fix-frames, closing-frames and word-frames PNGs, both resize frames and the refreshed phone keypad. All 38 audit PNGs were inspected on audit-sheet-00 through audit-sheet-06.

#### Art made
Eight generated images, 374,510 bytes total, about 366 KB. One lead-car redraw removed an unwanted rail. All raw PNGs are retained; only free rekey processing was used. `art-contact.png` was inspected against a cream background and at UI size. The riders asset is marked people true.

Bundle: 592,237 bytes at the last static check, about 578 KB, against the 2,000,000-byte goal. Voice audio: 0 KB. Static checks confirmed all eight assets inline, no external resource/fetch requests, required metadata and no temporary host file.

#### Art still to paint
None. Voice recordings are not art and remain for the normal later workflow. The people image still needs the regular fresh/owner review before shipping.

#### Engine changes wanted
Create the missing shared number-line engine only in a separately authorized shared change. Correct the family table's reversed hill/valley language. Add a full-window, readable animated zoom if the reviewer requires it. Exact files and functions are in handoff.

#### Left open
- Full ten-hill panorama and animated Tens/Hundreds zoom are not implemented; the rendered close hill is exact and labeled by its window.
- The shared engine and family-doc row remain untouched under the two-folder write boundary.
- Browser speech is the current fallback; no recordings were requested or made.
- Unrestricted corrective practice can be completed by exhaustive guessing; it confers no score or mastery claim.
- Bar references were opened from existing bundles rather than regenerated, avoiding writes to other tools.
- Report was written last because the user required stopping immediately when it was written.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: roller-coaster-rounding

#### Played
Cold grade 3 solo play: Drop, both tracks, a complete ticket card, train exploration and a complete Train card before reading the builder's report, handoff, notes or source. The downhill model and painted park are strong; column work becomes routine.
Teacher projection: predicted the wrong station, dropped the car and compared the result. Then walked Teaching, Play and Craft in one review pass, with targeted repair checks. Working folder: `S:\CurioClass-codex`; no commits.

#### Findings fixed
- **Blocker, general, Line results:** the old incorrect clerk equation remained above the corrected answer without a historical label. Banners now distinguish the clerk claim from the original claim after correction.
- **Should fix, general, Trains re-entry:** returning to a card always asked for tens, including during seats, capacity and completion. Hints and narration now follow the actual step.
- **Should fix, general, compact capacity:** Enough / Not enough pushed Start over below the fold at 680 and 375. Fixed cards use shorter count rows; exploration keeps full-size steppers. Accepted seats remain visible during judgment.
- **Should fix, general, voice:** the long Line introduction displaced rounding instructions. Shorter role/action lines fit the two-second walk. Exploration steppers preserve their still-valid welcome; automatic Hundreds changes announce their context.
- **Should fix, general, stale coaching:** bundle/break lines check their exact current state and controls. Capacity and corrected-column instructions are recordable. The sneaky premise finishes while column selection advances, and obsolete selection instructions are discarded.
- **Should fix, family:number-line, Track:** the full window label described an absent panorama. Added a ten-hill overview with interval highlight, car marker and tested tap mapping, retaining the large close hill.
- **Should fix, general, compact Track:** four-digit values crowded step buttons, and phone guesses collided with distance labels. Reserved number space and enlarged the phone stage; distances, overview and result ticket now have separate rows.
- **Should fix, general, Track annotations:** moved the wide halfway sign clear of the car and rail labels. Compact stages show the rule in the existing caption during the teeter. Result-ticket spacing clears the overview.
- **Should fix, general, empty trade:** tapping Break strip with no strips silently failed. It now explains how to make strips from a roll. Wrong estimates, judgments and corrections also give refusal tones.
- **Polish, general, Line rounding:** correct choices blinked directly into the next question. The result is stated immediately and the miniature car rolls along the fixed number line, without changing its destination under moving labels.
- **Polish, general, graphics:** redrew the ornate station as the specified timber platform, blank signboard and brass bell. Despilled seven cutouts, improved train-row contrast and clarified hundred-group tags.

#### Findings left
- **Blocker under the review's anti-guessing rule, spec conflict:** answer-revealing retries allow enumeration to complete practice. This is explicitly required by the station and clerk instructions. Retained that design, disclosed it in notes, and made no mastery claim. Preventing it needs a changed assessment design.
- **Should fix, family:number-line, outside scope:** `kit/number-line.js` is still absent and the family table reverses hills and valleys. The two-folder write boundary prohibits those repairs. Exact requested shared changes remain in handoff.
- **Polish, Track:** switching tracks redraws immediately; the specified animated zoom remains absent. The close view and full overview retain the number correctly.

#### Break it
Evidence: `numbers.py`, `functional-exit.json` and `final-proof.json` in this tool's Scratch. The independent functional run passed **458 assertions**.
- **Rolls / guesses:** repeated Drop counts activity; either guess is unscored. A real wrong guess at 47 retained 40 and reported the landing at 50. Integer-jitter dragging reached 42; keyboard-only Drop reached 50 with focus retained.
- **Line rounding / estimate:** wrong stations and estimates do not advance; typing the exact total cannot skip column work. Trying both stations eventually succeeds through the mandated corrective hint, as disclosed above.
- **All nine column cards:** wrong counts fail; short Take away changes nothing; typing before Take away fails; Next refuses an unbundled count. Required bundles and breaks produce each independently computed answer.
- **Clerks:** Makes sense fails both outside slips; Far off fails both inside claims. Trying the opposite afterward succeeds by specified correction. The sneaky card rejects 391 before column selection, rejects a wrong column and wrong digit, then accepts tens digit 9 and shows 391.
- **Train units:** every card requires tens before seats. Cars-as-seats, extra zeros and addition instead of multiplication fail, including 24, 2400 and 46 for Train 1.
- **Capacity:** wrong Enough / Not enough judgments fail; correction succeeds. The two results are 2 seats spare and 38 riders waiting. Accepted seat totals stay visible while judging.
- **Board / boundaries:** replaying cards cannot inflate their sets. Empty Enter does nothing, 1001 preserves the Track value, and changing a value during a roll cancels the old result. The board stores no student work.

#### Voice walk
Sound on, browser fallback, held 0.12-second clicks at a two-second pace. Main path: Drop 47; enter 44 and Drop; Line Card 1 with both bundles; Trains exploration and two stepper changes. Trace: `complete-main.json`.
Spoken in order: rollRight; setNext; rollLeft; wLine; round; estimate; cols; bundle; check; wTrains. The first Drop may skip wTrack under BASELINE 16; its valley/brake premise remains in Read.
Instruction texts in the trace include "Set a new number with the arrows or the keypad, then tap Drop"; "Tap its station"; "Add the two stations. Type it, then tap Enter"; "Start with the ones. Type how many, then tap Enter"; "Tap Bundle ten."
The accepted Track entry cuts setNext after it starts; the full instruction remains in the hint and Read. The second bundle instruction was silent. Choosing Trains cuts the card's check and cancels its pending lap; an uninterrupted side path lets the check finish before the four-second lap.
Side paths: Train 7 heard tens, seats, capacity and trainsDone; Clerk 4 heard estimate, clerk, the complete sneaky premise, fixSlip and check. Read with Sound off named the current track and spoke the hint plus station brakes. Automatic Tricky drop switching announced Hundreds.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| bundle | how-to | once | 1, next occurrence silent |
| round / estimate / cols | how-to | once each | 1 each on main path |
| wTrains | welcome | once | 1, finishes through stepper changes |
| rollLeft / rollRight | limited events | twice each in ten drops | 2 each |
| sneaky | whole event | once on side path | 1, no cut |
| fixSlip / capacity | how-to | once each | 1 each on side paths |

All **28** fixed lines match the live inventory. No recordings were made; the declared upbeat-guide voice remains for the normal recording workflow.

#### Facts checked
- Rounding to tens/hundreds, place-value addition/subtraction within 1000 and multiplying a digit by a multiple of ten: [Common Core Grade 3 NBT](https://www.thecorestandards.org/Math/Content/3/NBT/), checked live.
- Nearest benchmarks and midpoint comparison: [Utah State Board of Education Grade 3 NBT Core Guide](https://schools.utah.gov/curr/mathematics/_mathematics_/_core/_math_core_guides_tab_/CoreGuidesGrade3NumberOperations.pdf), checked live.
- Choosing the larger benchmark at a tie is a convention: [Illustrative Mathematics Grade 3 Unit 3 Lesson 15](https://im.kendallhunt.com/k5/teachers/grade-3/unit-3/lesson-15/lesson.html), checked live. The UI calls it the park rule.
- `numbers.py` independently checked all 2002 integer/track rounding cases. Actual drops checked 44→40, 45→50, 47→50, 349→300, 350→400, 995→1000, 0→0 and 1000→1000; the phone check also dropped 950 to 1000 on Hundreds.
- All nine estimate/exact pairs recomputed: 600/624, 390/391, 70/68, 230/235, 800/752, 810/802, 200/264, 900/900 and 620/625. Ticket values and ten-to-one trades follow base-ten place value in the named standards.
- Every legal pair was checked against the sensible stretch: worst addition gaps 10/100 and subtraction gaps 9/99 for tens/hundreds. An inside result is not proof. Clerk claims 514 and 365 are outside; 752 and the incorrect 381 are inside.
- Train tens/seats recomputed: 24/240, 21/210, 72/720, 30/300, 16/160, 28/280 and 24/240. Against 278 riders, the capacity differences are +2 and -38.
- Hilltop Park, capacities and station brakes are fictional model rules, identified in notes. No real coaster-capacity or physics claim is made.
- Measured text pairs: ink/paper 14.44:1, muted/paper 5.89:1, brand/paper 5.46:1, white/brand 5.88:1, white/button 7.91:1 and group tags 11.69:1. Method and values are in `static_check.py` / `static-result.json`.

#### Sensitivity
No cultural, religious, hard-history or body-instruction content. The fictional riders asset is marked `people: true`; inspected faces, hands, clothing, lap bars, age and skin-tone variety. No stereotype or frightening depiction found. The normal people contact-sheet review remains appropriate before release: `review-art.png` in Scratch.

#### Flattest moment left
Repeated column entry becomes mechanical after the first few trades. The rounding result now moves and answers immediately; the empty-tens cases and capacity questions provide the later changes. Kept the prescribed nine-card curriculum.

#### Graphics
Eight painted assets retained; one station redraw at `art/station-platform.webp` with built-in imagegen, full prompt in `art/prompts.json`, seven free `art.py --rekey` edge cleanups. Art **373,266 bytes**; bundle **598,211 bytes**, about 584 KiB. The park, cars, ticket pieces and riders remain rich and consistent.
Inspected the art contact sheet, all 49 audit frames, required-size/mode frames, phone gates, 1×1 and 9×9 trains, calm, grayscale, keyboard, jitter drag, halfway and completed states. Own current frames are identified by their shots JSON; pre-existing builder frames in Scratch remain preserved.
Compared existing Snowy Mail Route and Beat Lab bundles with this tool in `review-bar-comparison.png`. Existing bundles were used to honor the write boundary. The tool keeps its own painted daytime setting and teal palette.

#### Audit
Ran `review-audit` **once**, last, with a 40-minute cap; it finished successfully, with 71 leads and 49 frames. No console exceptions, lost focus, undersized-target leads, infinite calm motion or stuck resize controls.
- 37 geometry leads: fixed the two real phone text collisions; moved the three rule-panel/rail-label intersections clear. Inspected and retained 32 car-hitbox/tick intersections, including intentional car occlusion and transparent drag bounds.
- Nine welcome leads are the first-tap and quick-tap interruptions permitted by BASELINE 16. Premise and next action remain reachable through hints and Read.
- Twenty-five apparent no-ops: twenty digit buttons update the input property omitted from the audit's signature; four empty Back/Enter actions intentionally do nothing; Reset at the initial train array restores the same array.
- Five-click voice rows were clean. Scoped rechecks repaired the compact capacity fold missed by the original listed states, preserved the complete sneaky premise and verified positive result/overview gaps at 1280, 1366 and 760.
- Added compact capacity and clerk-column states for future audits. Did not run a second full audit. Final affected-state drives had no console errors; the earlier host-only favicon 404 was removed from the temporary harness.

#### Left open
The anti-enumeration/spec conflict, shared-engine/family correction and animated zoom above remain explicit. No new assessment feature, mode or topic was added. Teacher notes distinguish completed activity from independent mastery.
Current source, voice inventory, notes, handoff, state fixtures and art are updated. All owned Chrome ports and host 8765 were verified closed; the temporary host file is removed. Project writes stayed in the two permitted folders.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: Roller Coaster Rounding

#### Built
Three modes cover rounding, place-value addition and subtraction within 1000, and multiplying tens. Nine Line cards, four clerk checks and seven Train cards are freely selectable. Generated rider cards alternate rounding place and require regrouping on at least two cards in each group of three. No student work or completion counts are saved.

#### Source map
`src.html` starts from the shared starter and retains kit CSS, Motion, Sound, Read, tones and `Curio.voice`. Tool CSS defines the fairground and compact controls. The script has the voice table, fixed cards, tool-local number-line adapter, Track rendering, Line state machine and ticket trades, Trains rendering and answer stages, and static control wiring. `window.__tool` exposes state and actions for review. Fixed voice text is in `voice/lines.json`; recordings were intentionally not made.

#### Tricky parts
- `stopAction` invalidates asynchronous rolls and laps. A mode, value or card change acts immediately. The line that opens the ride completes before the four-second lap begins.
- Addition needs a correct raw column count before a bundle is available. Next column refuses an unbundled count of ten or more. Subtraction needs a legal Take away before it accepts the remainder. Extra breaks can be reversed with a bundle, so optional correct trades cannot trap the student.
- Breakable ticket columns are large keyboard targets; painted pieces inside are countable but do not create dozens of tiny targets. A strip consists of exactly ten individual ticket images. Source rows are separate until the current count is entered.
- Fixed-card completion uses sets, so replaying a card cannot inflate the board. Practice feedback deliberately permits correction, as the spec requires. The board records activity, not independent mastery.
- Track uses an enlarged adjacent-station segment so a single rounding hill, its car and its two platforms stay readable. Cold review added a ten-hill overview, with the close interval highlighted and a live car marker. Its coordinates use the same local number-line adapter. Overview input is handled separately so it cannot also fire the close-track tap handler.
- SVG redraw preserves a focused element by id. Pointer dragging reads the persistent stage rectangle, not an SVG node that a redraw replaced. Panel controls precede scene controls in DOM tab order.

#### Decisions and contradictions
- No open questions are listed in the spec. This unattended build needed no owner response.
- The spec asks for a new shared engine and a shared family-doc correction. The user's two-folder write boundary wins. A tool-local adapter supplies the needed API instead.
- The narrative says an ordinary roll takes about 1.2 seconds; Done when says within one second. The ordinary roll is one second; a halfway roll adds the one-second teeter. Reduced motion retains those timings.
- A 520 by 300 ticket bin cannot fit the 405-pixel preview stage or a 375-pixel phone. The three columns reflow at their available pixel size while the panel controls remain visible.
- The close segment and the full ten-hill window now appear together. Animated Tens/Hundreds zoom remains open; both views redraw synchronously and retain the held value.
- The intro concept mentions 40-seat cars, but the detailed spec consistently makes each car ten seats. The build uses ten seats per car and trains with four cars for forty seats.
- The build brief requests an early report, but the user's final instruction requires stopping when that file is written. The report is therefore written only after checks, as the final build action.
- The no-score, no-lock, corrective-feedback design permits exhaustive guessing. Wrong entries cannot skip stages, and no score or mastery claim can be set by a guessed answer. Blocking all answer enumeration would contradict the specified practice behavior.

#### Art made
Eight generated images are copied into `art/raw` and processed only with the free `scripts/art.py --rekey <name>` form. All eight are used in the interface. The first lead car had a rail attached and was redrawn once. The riders image has `people: true`. Prompt provenance is in `art/prompts.json`; the contact sheet is `_scratch/roller-coaster-rounding/art-contact.png`.

#### Sensitivity
No cultural, religious, hard-history or body-learning content. The fictional riders show varied ages and skin tones. The people asset still needs the normal fresh review and owner contact-sheet review before shipping. This build makes no shipping or publication claim.

#### Engine changes wanted
- `kit/number-line.js`, new `NumberLine`: implement the complete API in `docs/families/number-line.md`, using the tool-local coordinate, marker, span and input adapter as reference. The shared file was missing at build start. Do not promote the adapter without testing it against the other family tools.
- `docs/families/number-line.md`, roller-coaster-rounding table row: replace the incorrect hills-at-tens and nearer-hill wording with stations in valleys at tens or hundreds, midpoint hilltops and the bigger-station convention at ties.
- A future engine should preserve active drag handles through redraw, provide measured tick-label spacing, and support animated zoom without shrinking labels below readable size.

#### Review focus
Record upbeat-guide / Zephyr later through the normal voice workflow; browser speech is the present fallback. The cold reviewer inspected the riders for age and skin-tone variety, natural presentation and classroom suitability. The current contact sheet is `_scratch/roller-coaster-rounding/review-art.png`. No commit or release was made.

#### Cold review changes
- Preserved the park, car art, ticket trades and halfway teeter. Redrew the station as a timber loading platform with a blank signboard and bell; rekeyed all cutouts with edge despill.
- Correct rounding choices now animate the miniature car on the fixed 0 to 1000 number line. Its destination cannot be relabeled by the next question. The hint records the rounding result, and Motion off shows the same accepted state without movement.
- Shortened the Line welcome and action lines to fit a two-second tap pace. Bundle and break narration checks the exact current step and required control. Capacity, slip selection and corrected-column instructions are recordable. Train steppers let their still-valid welcome finish. Returning to Trains restores the hint for its actual step.
- Enlarged and clarified desktop grouping tags as `10 cars = 100`; added pale row backing to make the array readable over the park. Compact tags retain `100` to preserve every car.
- Independent adversarial scripts and current review frames live only in this tool's Scratch folder. `codex-review.md` is the final disposition, including the conflict between answer-revealing retries and the review's anti-enumeration rule.
- The phone stage uses 48 percent of the available height so guesses, distances, the overview and the result ticket have separate rows. On narrow stages the halfway rule occupies the existing caption during the teeter; wide stages put its sign left of the moving car. The four-digit held value has its own compact type size.
- Wrong estimates, clerk/capacity judgments and slip corrections have a refusal tone. Trying to break an empty tens pile explains how to make strips from a roll. Automatic switches to Hundreds through Tricky drop speak the existing how-to; Read names the current track.
- Compact Train cards show their fixed counts in shorter rows, with the unusable stepper buttons hidden. This keeps Start over visible when Enough and Not enough appear. Exploration retains full-size stepper targets.
- The clerk banner explicitly labels a claim and, after correction, the original claim. It therefore cannot present the old wrong equation as the current result.
- The sneaky-card premise is an event and finishes even if the student selects the column while it speaks. Its separate selection how-to is dropped once the column has been selected. All 28 fixed lines match the voice inventory.

#### Build check fixes
The full mechanical audit finished once, with 140 leads on its preserved input bundle in Scratch. Real leads led to wider compact keypad targets, a Close keys control, inert background controls during keypad entry, explicit focus restoration, stable Hundred-track control positions and Sound labels, separated result cars/station choices, and more space under train arrays. The audit was not run a second time; changed areas have targeted drive evidence.

Adversarial checks also found two visual answer leaks. Future unentered column totals now remain question marks, and the result track uses an answer-independent 0 to 1000 range until the estimate is entered. The expanded functional run passed 769 assertions. Switching track now clears a guess made on the old track. A carried piece is outlined so its +1 annotation refers to a piece already shown.

The keypad is a temporary entry overlay. Enter or Close keys closes it, Escape closes it, and widening the window restores ordinary controls while preserving any typed number. Its extra how-to line is included in the final 24-line voice inventory. The board and all numeric answers still store nothing.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
