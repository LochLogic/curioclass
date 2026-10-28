# target-toss handoff

Built 2026-10-28 (Build stage). K-2 PE, teacher led on a projector, no family engine. Draft bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py target-toss`. Voice clips are not recorded yet (`scripts/voice.py target-toss`, bank bright-teacher / Autonoe); `voice/lines.json` holds all 86 lines (after polish round 2) and matches `__tool.allLines()`.

## Layout of src.html

- Header: three mode buttons (Form, Test it, Free throw; keys 1 to 3), then Motion, Sound, Read.
- Panel (first in the DOM): `#hint`, then `#settings` (Throw: `#s-under`/`#s-over`; Hand: `#s-right`/`#s-left`), then one `.ctl` block per mode, then `.foot` (`#setup-btn` and the `#safety` tip).
  - Form: `#f-show`, `#f-next`, `#f-bo`.
  - Test it: `#tg-guess` (n-5/n-10/n-20, `#g-a`, `#g-b`, `#g-skip`, quiet `#g-back`), `#tg-round` (`#t-count`, `#t-hits`, `#t-frame`, row of `#t-short` / `#t-startb` (takes Too short's slot) / `#t-undo`, then quiet `#t-stop`), `#tg-look` (`#t-back`, `#t-answer`, `#t-again`, `#t-new`).
  - Free throw: `#r-short`, `#r-undo`, `#coach`, then quiet `#r-clear`.
- Stage: `#sv` SVG drawn at real pixel size (`lay()`); the Way banner is drawn in the SVG by `drawBanner` under the ball dots. HTML overlays: `#strip` (Test it steps), `#ask` (question cards), `#guess`, `#cues` (Form cue cards), `#answer`.
- Modals (body level, `.modal`, under the header): `#setup` (How to set up, six steps) and `#confirm` (Yes / No before throws are lost). `modalOn` makes main inert (and the header for confirm); `read` and the hint follow the open card.
- Layouts: `body.side` (default), `stack` (w < 760, or tall and under 1000 wide: controls, then settings, then foot), `short` (h < 640: tighter text, controls stay 60 px, icon above word on settings, `fitHint` steps a long hint down to 12.5 px), `narrow`/`narrowhead`/`tighthead` for the header. Under 480 px wide in stack, the settings also put the icon above the word.
- `window.__tool` exposes state, the voice log, lines, poses and the main actions for checks.

## Tricky parts

- **Bo** is a small 3D skeleton (yaw plus arm and leg direction vectors in model units) projected side on. `POSES.under` / `POSES.over` have five poses each; `poseTo` tweens 420 ms (a jump with Motion off). Left hand mirrors the whole Bo group and swaps Bo and the target. Tags are measured with `textW` so they never overlap.
- **Show me / Throw with Bo** are async runs with a token (`f.tok`); pressing the same button stops them. Each cue is `setCue(i)` (highlight plus pose) and `V.say(cue, {now, wait})` in the same tick, with a minimum beat of 1600 ms (Show me) or 1400 ms (Bo).
- **Rounds:** `roundThrow` ends Way A by queuing [wayA, hits, doneA] (doneA needs `#t-startb`) and focusing Start Way B. Way B goes to Look after 1.3 s; Undo in that beat cancels it, and Look's `#t-back` (`lookBack`) returns to Way B. `roundUndo` in an empty Way B reopens Way A and pops its last throw.
- **Small target** (`size` question, Way B): `classify` counts only gold as a hit; the outer rings draw grey with "Only the gold counts".
- **Coach** runs on every fifth Free throw over the last five (spec order: hits, above, low, side, keep). `F.log` keeps {n, text}; a line is said with now and is valid for throws n to n+4; `coachCard()` rebuilds the card after an Undo, and a Throw switch never rewrites it.
- `#cues.tight` (number hidden, smaller icon) turns on when the cue card is under 84 px tall or the page is under 560 wide.

## Deviations from the spec (for Refine to confirm)

1. **Baseline w1-49 applied** (answers the spec's Open question): the target is paper on the wall beside the screen. Added the **📋 How to set up** card and the voiced `setup` line; the safety tip and safety line now say "wall target" / "paper target on the wall beside the screen, never at the screen, a TV, a touch panel or the laptop".
2. Cue lines and `ready` are **event** lines, not how, so Show me and Throw with Bo speak them every run (a how line is spoken only once per load). `nowYou` stays how.
3. Added three lines: `tryBo` ("Now you try! Press Throw with Bo to throw together.", after Show me), `boDone` (after Throw with Bo), `again` (after Show the answer, names Test again and New question).
4. Coach has **7** lines, not the spec's "coach (9)": the spec's own Coach says table lists 7.
5. On the first tap of a mode, safety plays after a Show me run rather than before it, so the poses stay in step with the cues.
6. Stop test is also shown on the Guess step. Way B goes to Look on its own after 1.3 s.

## Checks run (2026-10-28)

- Audit (`audit_tool.py`, port 9962): first run 2 leads ("Follow through" clipped at 680x425 and 375); fixed with `#cues.tight`; re-run **0 leads**. Motion off clean, held-click walk clean, five-click checks clean.
- Done when 1 to 9: all pass (details in the build report). Form cue state, highlight and spoken line change in the same tick for all five cues, Motion on and off. Test it held-click run: counts equal the recomputed taps (A 3, B 5). Small target: gold hit, red and blue miss in Way B. Free throw: "Too high" for both throws, "Great aiming!" at 3 of 5. No how line spoken twice, no throw tap speaks. Every visible control is at least 60 px with an icon at 1366x768 and 1280x720.
- Frames looked at: every audit size (680x425 to 1920x1080, 760x900, 375 host), the Form Left hand frame, the Way B small-target frame, the Look and answer frame, the 375 setup card, the 375 settings row.
- Fixed after the audit: at 375 wide, the selected border cut the "r" of "Under"; the settings now put the icon above the word under 480 px.

## Open / next

- Record voice clips (`scripts/voice.py target-toss`).
- At a 2 s tap pace, a line still in the queue is dropped as 'newer' when the next control is pressed (for example `doneA` if Start Way B is pressed at once, or the Look counts if Show the answer is pressed while they play). That is the kit's cut-in rule; the count is always on screen.
- Refine list: not yet received.

## Polish round 1

Checked by held clicks with scratch `seq.py` runs A to E at 1366x768 (voice log, focus, rects), then `drive.py` sweeps at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 via `--host` (host.html deleted after): no control under 60 px, no horizontal scroll, no main control off screen, setup card does not scroll, answer card not clipped, 0 console errors (one favicon 404 from the host server). The only remaining flag is the guess cards' keycap emoji (3️⃣/6️⃣) line box, a false positive: the frames show them whole.

1. Fair-test lines per question: `startBstep/look/far/size` say what stays the same and the one change ("Same throwers, same order, same target. Only the line changes." on Close or far?); the far tip is now a result line ("Closer is easier to hit..."). Spec voice and question tables updated. Checked: run B (far) spoke wayB name then startBfar.
2. Coached way swapped to B on Where do you look? and Big or small? (`QS.exp`), vote signs are ☝️ one finger / ✌️ two fingers and the `guess` line says so. Checked: guess frames at every size, run B guess line.
3. Same throwers in the same order: `startA` ("Pick your throwers. Each one throws once, one at a time.") and every startB line; setup step 4; notes say the round size fits the same children throwing in both rounds. Checked: lines in the voice log, notes read.
4. Cue 3 now names the foot from Hand (`stepR` "Step with your left foot, the opposite foot." / `stepL`); the Coach says placeholder is voiced as `coach0` after wFree. Checked: run A Left hand cue 3 spoke stepL; run D voice log has coach0.
5. Setup card rebuilt as a body-level modal: three rings on the paper target, two big steps from the screen, ball pickup rule, six steps in view at every size (sized from the window); hint shows setupGo and Read reads the card. Checked: run E (setup spoken at once, hint setupGo, focus Close, main inert, Escape restores hint and focus); sweep setup frames incl. 680x425, 800x500, 760x900, 375 with `scardScroll` false.
6. Stop test and Clear the wall moved below, quiet dashed style, and ask Yes / No in `#confirm` (focus on No, Escape = No) when throws would be lost; mode buttons and keys 1 to 3 ask too. Checked: run C (No kept A=3, key 3 asked, Yes went to Free throw; Clear asked then focused Too short); confirm frames at every size.
7. Start Way B takes Too short's slot, Undo stays put and takes back Way A's 10th; Undo in an empty Way B reopens Way A. Checked: run B rects (Undo identical before and after the 10th throw), A=9 after Undo, A=9 after Undo in empty B; 375 adone frame shows Start Way B and Undo in view.
8. Look has "Undo last throw" (`#t-back`) back to Way B. Checked: run B, B went 10 to 9 and the round reopened.
9. Way banner drawn in the stage SVG under the dots (no HTML banner); misses above the target clamp below the step strip. Checked: run B above-dots frame and adone frames, every dot visible.
10. Guess step has "Other question" (`#g-back`) back to Ask. Checked: run B, Other question went to Ask with focus on the first question card.
11. Free throw welcome and hint: "Throw at the paper target! Then tap the screen where each ball hit." Checked: run C/D voice log and hint.
12. Focus moves on: question card to Way A, Way A to the stage, end of Way A to Start Way B, Stop test / New question to the first question card, Test again to Way A, Clear to Too short. Checked: run B and C focus readouts.
13. First Throw with Bo starts "Ready, aim..." at once and safety comes after boDone; first How to set up speaks setup at once with safety after. Checked: Bo run log (ready 1356 ms, five cues, boDone 20.0 s, safety 23.9 s); run E log.
14. Answer card measured when shown and placed before draw, so the tip never clips. Checked: sweep `answer` box inside the stage at every size incl. 680x425 (305 to 415) and 375.
15. Next cue's fifth says tryBo ("Now you try! Press Throw with Bo...", needs `#f-bo`); `nowYou` removed. Checked: run A hint after five Next cue taps.
16. `tipDiff` ("Our test came out different this time. Try more throws, then test again.") before the tip when the winner is not the coached way and not a tie. Checked: run B answer text, 1920x1080 look frame.
17. Look ten-frames fill hits first, then misses. Checked: look frames at every size.
18. notes.md "What to look for": K step with the opposite foot, grade 1 two cues, grade 2 all five and a start on overhand. Checked: read.
19. Overhand cue 2 card "Elbow up", line "Bring your arm way back, elbow up."; cue 5 "Follow through across your body, toward the target." Checked: lines.json and Form frames.
20. "Make a guess!" is queued right after the question title, before the Way names. Checked: run B voice log at teacher pace (guess spoken after the title).
21. Round intro says the Way name first, then the start line. Checked: run B voice log.
22. Throw with Bo beat is max(1000 ms after the line, 2200 ms a cue). Checked: Bo run, cues at 3.2, 5.9, 8.8, 12.9, 16.8 s.
23. Projector: floor tally in Test it too ("Hits n · Throw n of N", up to 38 px), question / way / answer type caps raised (34 / 27 / 24). Checked: 1920x1080 frames.
24. First coach line cuts in (now) and stays valid for five throws. Checked: run C and D at 1 tap/s, the first coach line was spoken.
25. Undo rebuilds the Coach card from the log (back to the placeholder when the throw is gone); a Throw switch never rewrites it. Checked: run C coach text after two Undos and after Over / Under switches.
26. How to set up is modal: main is inert, Show me cannot run under it, Escape closes. Checked: run E.
27. Short-box toggle labels line-height 1.15, no clip. Checked: sweep 680x425 / 800x500 frames and the clip check.
28. Spec voice table now lists cue lines, stepR/stepL, ready and boDone as events, plus every new and changed line. Checked: lines.json equals `__tool.allLines()` (84 lines, compared after the last edit).
- Settled: 60 px at every size (`body.short{--ctl:48px}` removed); sweep shows no control under 60 px at any size, 375 included. A long hint in short boxes now steps its font down (`fitHint`) so it never runs under the settings (seen at 680x425 to 1000x625, fixed and rechecked).
- Settled: catching. Spec "Who and how" and notes say the module is Throwing and Catching and catching is a later K-2 tool's job.
- Spec "Open questions" left as is. Bundle rebuilt with `CURIO_DRAFT=1`; voice clips still not recorded (lines changed).

## Polish round 2

From the exit check, round 1. Checked by held clicks (scratch `seq.py` runs F, G1 to G3 at 1366x768) and `drive.py` sweeps at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 via `--host` (host.html deleted after), fresh Chrome profiles, 9 states each incl. Look with the answer: no control under 60 px, no horizontal scroll, every main control in view (now also Skip the guess, Other question, Undo last throw, Test again, New question), answer card whole, 0 console errors (one favicon 404 from the host server).

- N1: `testAtRisk` covers every Test it step that holds throws (Look before and after the answer). Checked: run F, Form on Look asked Yes / No (No kept 10 and 10), key 3 after the answer asked; Guess with no throws switched with no card.
- N2: Yes on a mode switch focuses the new mode's first control (`firstCtl`: Show me, the first question card, Too short). Checked: run F, focus r-short after key 3 then Yes, f-show after Form then Yes; Stop test Yes still focuses the first card.
- N3: the safety line plays whole. A tool-level wrapper on `V.say` / `V.how` / `V.hush` / `V.welcome` (no kit change): a `now` line that arrives while safety plays or waits clears the rest of the queue but waits behind safety; a hush that cuts it (mode switch, Yes / No card) sets a flag and the next line that is not a Yes / No question says it again first. Checked: G1 (Test it, card at 2.1 s: safety 1.3 s, the card's title at 9.1 s, after safety ended), G2 (Hand first tap: safety, then the hand line, the Next cue line after), G3 (safety cut by the Yes / No card at 3.2 s, said again at 3.9 s after Yes, then wForm).
- P1: Skip the guess and Other question share a row; short boxes tighten the Guess gaps. Checked: both in view at 680x425 and 800x500 (sweep inview, 680x425 guess frame).
- P2: in the stacked layout the stage grows on Look (min(w x 1.1, h x .55)), with a relayout on entering or leaving Look. Checked: 375 Look cells 29 px at 20 throws (were about 10), Test again and New question still in view (bottom 794 of 812).
- P3: Hand tap says both tags (`handR` / `handL`), after safety on a first tap, never cutting a Show me cue. Checked: G2 log; lines.json now 86 lines and equal to `__tool.allLines()`.
- P4: winner box sized to its column (ten-frames, count and bar) and the column cap raised to 560 px, so ten-frames grow on a projector. Checked: 1920x1080 answer frame, cells 104 px (were 78), box ends under the bar.
- Spec updated (Voice table: handR / handL and the safety rule; Yes / No covers Look and focus after Yes; Guess row; Look stage). Bundle rebuilt with `CURIO_DRAFT=1` (108 KB). Voice clips still not recorded.
