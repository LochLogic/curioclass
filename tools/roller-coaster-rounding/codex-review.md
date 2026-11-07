# Codex review: roller-coaster-rounding

## Played
Cold grade 3 solo play: Drop, both tracks, a complete ticket card, train exploration and a complete Train card before reading the builder's report, handoff, notes or source. The downhill model and painted park are strong; column work becomes routine.
Teacher projection: predicted the wrong station, dropped the car and compared the result. Then walked Teaching, Play and Craft in one review pass, with targeted repair checks. Working folder: `S:\CurioClass-codex`; no commits.

## Findings fixed
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

## Findings left
- **Blocker under the review's anti-guessing rule, spec conflict:** answer-revealing retries allow enumeration to complete practice. This is explicitly required by the station and clerk instructions. Retained that design, disclosed it in notes, and made no mastery claim. Preventing it needs a changed assessment design.
- **Should fix, family:number-line, outside scope:** `kit/number-line.js` is still absent and the family table reverses hills and valleys. The two-folder write boundary prohibits those repairs. Exact requested shared changes remain in handoff.
- **Polish, Track:** switching tracks redraws immediately; the specified animated zoom remains absent. The close view and full overview retain the number correctly.

## Break it
Evidence: `numbers.py`, `functional-exit.json` and `final-proof.json` in this tool's Scratch. The independent functional run passed **458 assertions**.
- **Rolls / guesses:** repeated Drop counts activity; either guess is unscored. A real wrong guess at 47 retained 40 and reported the landing at 50. Integer-jitter dragging reached 42; keyboard-only Drop reached 50 with focus retained.
- **Line rounding / estimate:** wrong stations and estimates do not advance; typing the exact total cannot skip column work. Trying both stations eventually succeeds through the mandated corrective hint, as disclosed above.
- **All nine column cards:** wrong counts fail; short Take away changes nothing; typing before Take away fails; Next refuses an unbundled count. Required bundles and breaks produce each independently computed answer.
- **Clerks:** Makes sense fails both outside slips; Far off fails both inside claims. Trying the opposite afterward succeeds by specified correction. The sneaky card rejects 391 before column selection, rejects a wrong column and wrong digit, then accepts tens digit 9 and shows 391.
- **Train units:** every card requires tens before seats. Cars-as-seats, extra zeros and addition instead of multiplication fail, including 24, 2400 and 46 for Train 1.
- **Capacity:** wrong Enough / Not enough judgments fail; correction succeeds. The two results are 2 seats spare and 38 riders waiting. Accepted seat totals stay visible while judging.
- **Board / boundaries:** replaying cards cannot inflate their sets. Empty Enter does nothing, 1001 preserves the Track value, and changing a value during a roll cancels the old result. The board stores no student work.

## Voice walk
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

## Facts checked
- Rounding to tens/hundreds, place-value addition/subtraction within 1000 and multiplying a digit by a multiple of ten: [Common Core Grade 3 NBT](https://www.thecorestandards.org/Math/Content/3/NBT/), checked live.
- Nearest benchmarks and midpoint comparison: [Utah State Board of Education Grade 3 NBT Core Guide](https://schools.utah.gov/curr/mathematics/_mathematics_/_core/_math_core_guides_tab_/CoreGuidesGrade3NumberOperations.pdf), checked live.
- Choosing the larger benchmark at a tie is a convention: [Illustrative Mathematics Grade 3 Unit 3 Lesson 15](https://im.kendallhunt.com/k5/teachers/grade-3/unit-3/lesson-15/lesson.html), checked live. The UI calls it the park rule.
- `numbers.py` independently checked all 2002 integer/track rounding cases. Actual drops checked 44→40, 45→50, 47→50, 349→300, 350→400, 995→1000, 0→0 and 1000→1000; the phone check also dropped 950 to 1000 on Hundreds.
- All nine estimate/exact pairs recomputed: 600/624, 390/391, 70/68, 230/235, 800/752, 810/802, 200/264, 900/900 and 620/625. Ticket values and ten-to-one trades follow base-ten place value in the named standards.
- Every legal pair was checked against the sensible stretch: worst addition gaps 10/100 and subtraction gaps 9/99 for tens/hundreds. An inside result is not proof. Clerk claims 514 and 365 are outside; 752 and the incorrect 381 are inside.
- Train tens/seats recomputed: 24/240, 21/210, 72/720, 30/300, 16/160, 28/280 and 24/240. Against 278 riders, the capacity differences are +2 and -38.
- Hilltop Park, capacities and station brakes are fictional model rules, identified in notes. No real coaster-capacity or physics claim is made.
- Measured text pairs: ink/paper 14.44:1, muted/paper 5.89:1, brand/paper 5.46:1, white/brand 5.88:1, white/button 7.91:1 and group tags 11.69:1. Method and values are in `static_check.py` / `static-result.json`.

## Sensitivity
No cultural, religious, hard-history or body-instruction content. The fictional riders asset is marked `people: true`; inspected faces, hands, clothing, lap bars, age and skin-tone variety. No stereotype or frightening depiction found. The normal people contact-sheet review remains appropriate before release: `review-art.png` in Scratch.

## Flattest moment left
Repeated column entry becomes mechanical after the first few trades. The rounding result now moves and answers immediately; the empty-tens cases and capacity questions provide the later changes. Kept the prescribed nine-card curriculum.

## Graphics
Eight painted assets retained; one station redraw at `art/station-platform.webp` with built-in imagegen, full prompt in `art/prompts.json`, seven free `art.py --rekey` edge cleanups. Art **373,266 bytes**; bundle **598,211 bytes**, about 584 KiB. The park, cars, ticket pieces and riders remain rich and consistent.
Inspected the art contact sheet, all 49 audit frames, required-size/mode frames, phone gates, 1×1 and 9×9 trains, calm, grayscale, keyboard, jitter drag, halfway and completed states. Own current frames are identified by their shots JSON; pre-existing builder frames in Scratch remain preserved.
Compared existing Snowy Mail Route and Beat Lab bundles with this tool in `review-bar-comparison.png`. Existing bundles were used to honor the write boundary. The tool keeps its own painted daytime setting and teal palette.

## Audit
Ran `review-audit` **once**, last, with a 40-minute cap; it finished successfully, with 71 leads and 49 frames. No console exceptions, lost focus, undersized-target leads, infinite calm motion or stuck resize controls.
- 37 geometry leads: fixed the two real phone text collisions; moved the three rule-panel/rail-label intersections clear. Inspected and retained 32 car-hitbox/tick intersections, including intentional car occlusion and transparent drag bounds.
- Nine welcome leads are the first-tap and quick-tap interruptions permitted by BASELINE 16. Premise and next action remain reachable through hints and Read.
- Twenty-five apparent no-ops: twenty digit buttons update the input property omitted from the audit's signature; four empty Back/Enter actions intentionally do nothing; Reset at the initial train array restores the same array.
- Five-click voice rows were clean. Scoped rechecks repaired the compact capacity fold missed by the original listed states, preserved the complete sneaky premise and verified positive result/overview gaps at 1280, 1366 and 760.
- Added compact capacity and clerk-column states for future audits. Did not run a second full audit. Final affected-state drives had no console errors; the earlier host-only favicon 404 was removed from the temporary harness.

## Left open
The anti-enumeration/spec conflict, shared-engine/family correction and animated zoom above remain explicit. No new assessment feature, mode or topic was added. Teacher notes distinguish completed activity from independent mastery.
Current source, voice inventory, notes, handoff, state fixtures and art are updated. All owned Chrome ports and host 8765 were verified closed; the temporary host file is removed. Project writes stayed in the two permitted folders.
