# Codex report: roller-coaster-rounding

## Built
Built in `S:\CurioClass-codex`. Writes are confined to the named tool and its Scratch folder. No commits, publication or polish round.

Three modes: an interactive rounding hill; nine place-value arithmetic cards, four clerk checks and generated queues; train exploration and seven cards. Eight generated illustrations are embedded in one offline HTML file. Metadata remains `tool.draft.json`, stage built.

The shared number-line engine was missing. The required subset is tool-local; no shared files were changed. The close hill replaces the simultaneous ten-hill panorama. See handoff for spec conflicts and remaining engine work.

## Numbers check
`_scratch/roller-coaster-rounding/recompute.py` independently checked every integer 0 to 1000 on both tracks, every legal addition and subtraction pair, every card, train calculation and specified text contrast.

Required drops: 44→40, 45→50, 47→50, 349→300, 350→400, 995→1000, 0→0, 1000→1000. Actual asynchronous drops also passed in `behavior-result.json`.

Line estimates/exact: 600/624, 390/391, 70/68, 230/235, 800/752, 810/802, 200/264, 900/900, 620/625. Largest absolute estimate gaps over the full legal pair space are 10/100 for addition and 9/99 for subtraction, for tens/hundreds respectively.

Train tens/seats: 24/240, 21/210, 72/720, 30/300, 16/160, 28/280, 24/240. Capacity differences are 2 spare and 38 waiting. Three hundred generated rider cards passed bounds, stretch and regroup checks.

## Facts checked
- Rounding to tens/hundreds, place-value arithmetic within 1000 and one digit times multiples of ten: [Common Core Grade 3 NBT](https://www.thecorestandards.org/Math/Content/3/NBT/), verified live.
- Equal midpoint distances and choosing the higher benchmark by convention: [Illustrative Mathematics, Grade 3 Unit 3 Lesson 15](https://im.kendallhunt.com/k5/teachers/grade-3/unit-3/lesson-15/lesson.html), verified live. The UI calls this the park rule.
- Ten ones per ten, ten tens per hundred, every displayed equation, distance, ticket count and capacity: derived from place value and independently checked by the scripts above.
- The sensible stretch is an estimate check, not proof. Its one-station error bound was recomputed exhaustively. Clerk 4 demonstrates an incorrect answer inside the stretch.
- Hilltop Park, seats, station brakes and the ride are fictional model rules, stated in teacher notes. There is no claim about real coaster capacity or physical stopping behavior.
- Measured text contrasts: ink/paper 14.44:1, muted/paper 5.89:1, brand/paper 5.46:1, white/brand 5.88:1, white/button 7.91:1, focus/paper 4.81:1. Scene labels use pale backing or strokes over the variable painted background.

## Break it
`audit-fixed-functional.json`: 769 assertions passed, using the real state-machine actions and independent arithmetic.
- Wrong station choices do not advance. A wrong estimate cannot open columns or clerk judgment.
- The centered estimate axis and future numeric column totals initially leaked answers. Fixed: pre-estimate ticks are always 0 to 1000, and all unentered column totals stay unknown. Copying a fixed middle tick fails every fixed card. Exact totals cannot skip the column work. Every column rejects a wrong entry. Next refuses an unbundled count of ten or more. A short Take away changes nothing, and typing a remainder before Take away is refused.
- All nine fixed cards require the right counts and trades. Replaying one cannot increase the completion set.
- An unnecessary subtraction break initially risked trapping a student with more than nine pieces. Fixed by permitting a reverse bundle after the remainder is entered; the adversarial extra-break path now continues legally.
- Makes sense on either big clerk slip is refused. Far off on either inside answer is refused. The sneaky card requires selecting tens and replacing 8 with 9; typing 391 before selecting a column cannot finish it.
- Seats entered before tens do not advance a Train card. Cars as seats, an extra zero and addition instead of multiplication are refused with distinct coaching. Both capacity cards reject the wrong judgment.
- Typed 1001 preserves the old Track value. Empty Enter does nothing. The keypad accepts at most four digits.
- The board is a count of completed activities, not a score or mastery claim. Corrective feedback deliberately allows a later correct answer after mistakes. Exhaustive answer guessing cannot be made impossible without changing the specified unrestricted practice design; this limitation is explicit in handoff.

## Voice walk
Twenty-four fixed lines use `Curio.voice`; upbeat-guide / Zephyr is declared for later recording. No audio was recorded. Current speech uses the kit's browser fallback.

Held clicks used 0.12-second presses at a two-second tap pace. Main path heard wTrack, rollRight, wLine, estimate, cols, bundle, check and wTrains. Repeated bundle became silent after its first hearing. Deliberate mode changes cut current speech and cancel a pending lap immediately.

The long Line welcome initially delayed the station how-to past its step. Its final wording names the station action directly. The final train-card welcome uses tens instead of the exploration welcome, so it never asks for fixed steppers. Final traces heard the Line welcome and the Train card's tens then seats instructions.

Ten real held Drop clicks: rollLeft spoke twice and rollRight twice, then chimes only. `ten-drops-voice.json` retains the full log. Read/Sound interruption and lap sequencing evidence are in the final interaction files. A real live lap ended and switched mode in 2.6 milliseconds. The final keypad how-to is available through Read.

## Feel check
Best moment: the halfway car rocks over two equal dashed distances, the park rule appears, then it rolls forward. Completing manual ticket trades earns the riders lap and the Open sign.

Flattest moment 1: the first compact panel clipped entry and reset. Rebuilt the compact controls as a small control desk, with Keys opening the keypad; all main controls now stay visible.

Flattest moment 2: ticket strips initially read as tiny orange lines and piles could clip. Changed them to ten individually painted tickets, kept the two source rows separate until entry, sized each pile from its count, and added a carried-piece tag and trade motion. Dense array labels were also shortened to 100 on compact views.

Looked at the existing Snowy Mail Route and Beat Lab bundles and their source. `bar-comparison.png` puts the tool beside Snowy Mail Route. The park is richer in painted detail and its exact controls remain readable. Long column work is a lesson activity; the missing full panorama/zoom is the clearest remaining finish gap.

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
All drive PNGs in early-frames, test-frames, late-frames, phone-frames, extra-frames and final-input-frames were opened. This covers the seven standard desktop/preview sizes, phone host, three modes, 81-car extreme, tickets, midpoint, grayscale, calm result/lap, keyboard and dragging. Also opened all last-frames, audit-fix-frames, closing-frames and word-frames PNGs, both resize frames and the refreshed phone keypad. All 38 audit PNGs were inspected on audit-sheet-00 through audit-sheet-06.

## Art made
Eight generated images, 374,510 bytes total, about 366 KB. One lead-car redraw removed an unwanted rail. All raw PNGs are retained; only free rekey processing was used. `art-contact.png` was inspected against a cream background and at UI size. The riders asset is marked people true.

Bundle: 592,237 bytes at the last static check, about 578 KB, against the 2,000,000-byte goal. Voice audio: 0 KB. Static checks confirmed all eight assets inline, no external resource/fetch requests, required metadata and no temporary host file.

## Art still to paint
None. Voice recordings are not art and remain for the normal later workflow. The people image still needs the regular fresh/owner review before shipping.

## Engine changes wanted
Create the missing shared number-line engine only in a separately authorized shared change. Correct the family table's reversed hill/valley language. Add a full-window, readable animated zoom if the reviewer requires it. Exact files and functions are in handoff.

## Left open
- Full ten-hill panorama and animated Tens/Hundreds zoom are not implemented; the rendered close hill is exact and labeled by its window.
- The shared engine and family-doc row remain untouched under the two-folder write boundary.
- Browser speech is the current fallback; no recordings were requested or made.
- Unrestricted corrective practice can be completed by exhaustive guessing; it confers no score or mastery claim.
- Bar references were opened from existing bundles rather than regenerated, avoiding writes to other tools.
- Report was written last because the user required stopping immediately when it was written.
