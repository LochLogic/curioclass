FIX: no blockers. The math is right on every puzzle and every Done-when. Four things should be fixed: the crash tracker can miss a crash and then claim an inverse, two crash pairs it shows are not real crashes, the 16:10 preview is too small to read and use, and the floor buttons are under 44 px at laptop size.

Method: I pulled the FUNCTION-MACHINE ENGINE block out into node and tested every part with its partner undo, the formula builder, all 12 puzzles and the gate edges. I fuzzed the interval tracker on 70,000 random chains, with and without gates, against a dense brute-force search, and invented chains to break it. In the browser I bundled the tool (CURIO_DRAFT=1) and drove it in headless Chrome with a copy of the CDP driver, collecting console errors and exceptions. Sizes: 680x425, 800x500, 1000x625, 1280x720, 1400x900, 1920x1080, 760x900, and 375 wide in an iframe host. I also checked Motion off, the keyboard paths, and a click-through of every button. No console errors or exceptions in any frame.

## Findings

1. **Engine, `pairFromSets` / `collision` (src.html 491-544): a crash that is not found is treated as no crash.** Seriousness: should fix (high: it is a false math claim).
   - **What happens:** When a machine is flagged unsafe but neither the input list nor the interval fallback finds a pair, `collision()` returns null. The verdict can then be `Undoes it`. The fallback picks its two values without checking the machines after the unsafe one, so a later Log base 2, Reciprocal or Square root can reject both values.
   - **Builder's case (Round, Square root, Subtract 7, Square root):** Run gives `Nothing got through`, because no test token survives. `Send my number` 50 with undo Square, Add 7, Square gives `Undoes it` ("Your number 50 came home"). 50 and 50.2 really do crash. No `g = f⁻¹` line appears, because it was a single number. On its own this case is mild.
   - **Worse case I found (Multiply by 10, Multiply by 10, Round, Log base 2), with undo Power of 2, Divide by 10, Divide by 10:** Run with the 8 test tokens shows `Undoes it`, "All 4 tokens that got through came home", the green `✓ g(x) = f⁻¹(x)` line, and the "Your bottom line is the inverse" voice line (frame a08-miss-round-log). But 0.5 and 0.501 both give log₂ 50. Multiply by 10, Multiply by 10, Round, Reciprocal does the same.
   - **How common:** The random fuzz found 72 missed crashes, all of this kind (Round, or a fold, followed by a domain limit). None of them let a test token through. Only hand-built chains like the one above reach the false `Undoes it` on a full Run.
   - **Scope:** Workshop only. Puzzles are not affected.
   - **Suggested fix:** When `unsafe` is non-empty and no pair is found, look for a pair at the passing token values entering the unsafe machine (for Round: v and a nearby value in the same rounding step, carried back through `invert`). Otherwise, at least do not show `Undoes it` or `g = f⁻¹`.

2. **Engine, `same()` (src.html 397), used to find crash pairs: some pairs it shows are not real crashes.** Seriousness: should fix.
   - **Cause:** `same()` treats outputs within a relative 1e-9 as equal.
   - **Example:** Power of 2, Subtract 15, Square shows "−26 and −27 both come out as 225" (frame a10). The real outputs are 224.99999955 and 224.99999978, so they are not the same. The chain does crash (2^x = 14 and 2^x = 16 both give 1), so the verdict is right but the evidence on screen is false.
   - **How common:** 96 of about 20,000 unsafe random chains got such a pair. Examples: Round, Power of 2 with gate x ≤ −10 shows "−29 and −30 both come out as 0", and Cube, Reciprocal, Multiply by 9, Add 7, Square shows 296 and 297.
   - **Suggested fix:** Use a much tighter test, or exact equality, when choosing the pair.
   - **Related nit:** Pairs found by the interval fallback show rounded irrational inputs, for example "2.3925 and 2.0914 both come out as 1" (frame a16). A student who types those numbers will not get a crash.

3. **16:10 preview (680x425 and 800x500, `compact` layout): the floor is too small to read.** Seriousness: should fix.
   - **Readability:** At 680x425 the floor is 412 px wide, so it is drawn at about 0.34 scale. Card names, tokens, readouts and the LOST text come out at about 4 to 6 px (frames z-680x425-ws and z-680x425-pz). The batch asks for about 10 px. There is also empty space above and below the floor, and the formula strip wraps to 3 lines.
   - **Parts bin out of view:** The bin starts below the fold of the panel at all three 16:10 sizes. Panel tops measured: Workshop bin at y 371 in a 425/500/625 viewport. Puzzles bin at y 466, below the fold at 680x425 and 800x500. Hint, Can't be undone and Reset puzzle are also below the fold at 680x425. A student cannot build an undo line in the preview without scrolling the panel.
   - **1000x625 and up:** Usable. Full screen (1280x720 and up) looks good.

4. **Floor buttons are below 44 px at a normal laptop size.** Seriousness: should fix.
   - **Measured at 1280x720:**

     | Button | Size |
     |---|---|
     | Top-line card − and + | 34x31 px |
     | Undo card − and + | 29x29 px |
     | Top-line remove × | 31x31 px |
     | Undo remove × | 25x26 px |

     At 1920x1080 they are 42 to 44 px.
   - **Mitigation:** The "Selected machine" panel has full-size equivalents, so nobody is locked out. The card targets themselves still fail the 44 px rule.

5. **Formula strip: the superscripts are hard to read in the readout font.** Seriousness: should fix (low).
   - In `(x + 3)²` the ² is tiny.
   - In `✓ g(x) = f⁻¹(x)` the ⁻¹ reads like "−ı". This is the key result line (crop of z-1280x720-pz).
   - A real `<sup>`, or a font that has these glyphs, would help.

6. **Hint 3 on levels 7, 8 and 10 turns the gate on as `x ≥ 0`, which already solves all three.** Seriousness: nit.
   - The tip says "Now choose its value", but 0 is already a working value. For 8 and 10 it is the answer itself.
   - This follows the spec ("Switching it on sets ≥ 0", "3 sets the gate switch to ≥"), so it may be a spec question rather than a build bug.

7. **Display nits:**
   - **Unsimplified formulas look odd in places:** Multiply by 1 or −1 shows `1x` and `−1x`. Level 12 shows `f(x) = 2((x − 1)³) + 7`. Both follow the spec's "no simplifying" and wrapping rules, but `2(x − 1)³ + 7` would read better.
   - **Space before the comma:** The gate domain shows as `(x + 3)² , for x ≥ −3`, because the flex `gap` puts a space before the comma.
   - **Symbols cover the remove button:** On cards with a negative number (`×−10`, `÷(−10)`), the symbol runs under the × remove button (frame a16).
   - **Crash chips overflow:** Wide crash chips spill past the right edge of the OUT bin (frame a16).
   - **Phone width:** At 375 px the floor scrolls sideways, as the notes say, but the undo line's first slots (on the right) start off screen.

8. **Contrast and stale text nits:**
   - The slot hint text ("drop a part", "undo parts", "+"), #6d7a8c on the plate, is about 4.0:1, below AA for 13 px text.
   - After a keyboard drop, the tip still says "Square root lifted. Tap a slot...". The tip is not cleared on place.

## Checked and fine

- **Every part and its undo:** Add/Subtract, Multiply/Divide (all a, skipping 0), Flip, Reciprocal, Cube/Cube root and Power of 2/Log base 2 all bring every test value home.
- **Folds:** Square then Square root returns |x|, as expected. Round is floor(x + 0.5) (−2.5 → −2).
- **Domain tags:** "√ needs 0 or more", "log₂ needs more than 0" (for 0 and negatives) and "1/x can't take 0" are all correct. "too big" works: Cube, Cube, Power of 2 tags 3 and 9.
- **All 10 Done-when items pass:**
  - 2 comes back as −0.6667, and swapping the undo order brings all 8 home with `g = f⁻¹`.
  - Add 3, Square shows "−2 and −4 both come out as 1". With gate x ≥ −3, −6 is blocked and the other 7 come home.
  - A lone Log base 2 rejects 4 tokens without counting them.
  - Level 9 shows 0 and 0.1. Level 2 says it can be undone.
  - Level 11 accepts Flip sign, Add 10 and Reciprocal, Flip sign. It rejects Add 3, Subtract 3 (changes nothing) and a single machine.
  - Mirror of Cube lands on Cube root. Mirror of Square shows the two-hit line and its label.
  - Motion off makes tokens jump on the same beat.
  - No network requests: the only URL is the SVG namespace.
- **All 12 puzzles:**
  - They solve with the table answers.
  - The x ≤ gate alternates also solve: 7 with ≤ −3, 8 with ≤ 0, 10 with ≤ 0.
  - Gate edges behave correctly: on level 7, ≥ −2 and ≤ −4 solve, while ≥ −4 and ≤ −2 still crash. On level 8, ≥ −1 crashes.
  - Level 5 with two machines does not solve.
  - Check marks survive a reload.
  - The crash stays hidden in Puzzles until Run or Can't be undone, so level 9 is not given away.
- **Collision tracker apart from findings 1 and 2:** It never showed a pair that does not collide at all. It never flagged a one-to-one chain (gated or not) as crashing. Chains it flags unsafe where one side is actually cut off (for example Square, Flip sign, Square root) correctly show no crash.
- **Keyboard:**
  - Tab order is: header, panel controls, parts, then floor cards.
  - Enter lifts, arrows pick, Enter drops. `=`/`-`, `[`/`]` and Delete work on cards, and the focus ring is visible.
- **Voice and words:**
  - The 11 lines are word for word the same in the code, `voice/lines.json`, `allLines()` and the spec, and all 11 clips are present.
  - No em dashes. "Curio Class" is never shortened. No art assets, and none needed.

Not verified: how the voice clips sound, and the Sound and Read audio output (no audio in headless Chrome).

## Re-verify

FIX: the five should-fix items are fixed or nearly fixed, and nothing regressed in the math, puzzles, keyboard, drag or Motion. Two things are still open. The crash finder still shows a few pairs that are not real crashes (about 1 in 3,000 pairs, far fewer than before). New: the voice lines cut each other off, against the batch voice rule. The 16:10 preview text is better but still a little under 10 px.

Method: I pulled the engine block out into node again. I fuzzed `collision()` on 100,000 random chains (5 seeds, a third of them gated) and compared it with a dense brute-force search (about 14,000 inputs per chain). I checked all 58,794 pairs it showed at 80-digit precision (mpmath). I rebundled the tool (CURIO_DRAFT=1) and drove it with my own copy of the CDP driver, collecting console errors and exceptions. Sizes: 680x425, 800x500, 1000x625, 1280x720, 1400x900, 1920x1080, 760x900, and 375 wide in a same-origin iframe host. I logged the voice clip play and pause calls during real CDP clicks. No console errors or exceptions in any frame.

### Per finding

1. **Missed crash leads to a false "Undoes it": FIXED.**
   - **Fuzz:** In 100,000 chains the engine never called a chain safe when brute force found a crash (0 misses).
   - **Verdict rule:** "Undoes it" now needs `collision()` to return null, meaning no machine is unsafe. An unsafe machine with no confirmed pair now gives **Can't confirm the undo** (`unconfirmed`).
   - **Old cases:**
     - Round, Square root, Subtract 7, Square root now shows "64 and 64.25 both come out as 1".
     - Multiply by 10, Multiply by 10, Round, Log base 2 now shows "0.01 and 0.0125 both come out as 0".
     - Both say **Can't be undone as built**, with no `g = f⁻¹` line.
   - **Nit, conservative side:** About 1 in 10 of the "Can't confirm" chains do have a real crash that the finder did not reach. Two kinds:
     - A crash found only near a rounding edge: Square root, Multiply by −8, Round, Square root. 0 and 0.0036 both give 0, but the run says "Can't confirm the undo".
     - Always 5 followed by machines that push values past 1e15 or below 1e-9, where the size check refuses every pair. Example: Always 5, Cube, Cube, Cube.
     - In other chains "Can't confirm" appears where the chain really is one-to-one on what gets through. Example: Square, Flip sign, Square root, where only 0 gets through.
     - None of these is a false claim, only a weaker one.

2. **Crash pairs that are not real crashes: MOSTLY FIXED, a few remain (nit).**
   - **Old examples fixed:**
     - Power of 2, Subtract 15, Square now shows "4 and about 3.8074 both come out as 1".
     - Round, Power of 2 with gate x ≤ −10 now shows −11 and −10.75, a real crash.
   - **What still slips through:** Of 58,794 pairs, 26 not marked "about" are false at 80 digits. About 20 of the 26 come from three causes:
     - **Fold tolerance at large values.** The fold test allows a relative error of 1e-14. Example: Cube, Subtract 12, Absolute value shows "100.0004 and −99.9996 both come out as 1e+6". The real outputs are 1000000.000048000064 and 1000000.000047999936. Also Cube, Add 1, Absolute value shows 65536 and −65536, whose real outputs are 2^48 + 1 and 2^48 − 1.
     - **Underflow counted as a real 0.** Round, Power of 2, Flip sign, Square root shows "−2048 and −2047.75 both come out as 0". In exact math 2^x is above 0, so Flip sign makes it negative and Square root rejects every input. This chain also reads **Can't be undone as built** after a Run in which no token got through.
     - **Float error at a rounding edge.** Power of 2, Square root, Log base 2, Multiply by −10, Round, Reciprocal shows 0.1 and 0.2. Exactly, 0.1 gives −0.5, which rounds to 0, so Reciprocal rejects it. Also Cube root, Log base 2, Reciprocal, Round shows 4 and 5: 4 gives exactly 1.5, which rounds to 2, not 1.
   - **How common:** about 0.04% of pairs, against 0.5% before. Every one of these chains does crash, so each verdict is right; only the evidence shown is false.
   - **Suggested fix:** Use a tighter fold test, for example compare `|ea|` and `|eb|` exactly. Treat a 0 reached by underflow as not tame. Reject a Round pair when a value entering Round is within about 1e-12 of a half step.
   - **"About" pairs:** All the "about" (approximate) pairs I checked are real crashes at the unrounded inputs. Typing the rounded inputs does not crash, as the "about" label warns.

3. **16:10 preview too small, and the parts bin out of view: LARGELY FIXED. A nit remains.**
   - **Text size:** With a short chain, the compact floor now draws card text at about 8 to 10 px at 680x425, against 4 to 6 px before. It is 9 to 10 px at 800x500 and 10 px or more at 1000x625. Some labels are still small:
     - "LOST" is 5.6 to 6.9 px at 680x425.
     - "BACK HOME" and "GATE" are about 7 to 8.8 px.
     - With a full chain (6 machines on top, 8 on the undo line), the cards at 680x425 shrink to about 5 to 6 px text and 23x36 px stepper hit areas (frame hit-680x425). This is expected for a crowded floor, but worth knowing.
   - **Bin:** The first row of parts is now in view in Puzzles, with the bin at y 282 against 466 before, and in Workshop at 680x425.
   - **Bin still pushed below the fold:**
     - When the gate is on (levels 7, 8 and 10, or Workshop with Gate), the gate box pushes the bin below the fold at 680x425 and 800x500.
     - In Workshop with a gate on, 0 of 15 parts show at 680x425 (bin top at y 405).
   - **Other sizes:**
     - Full screen at 1280x720 and 1400x900 looks good.
     - At 760x900 the stack layout is fine.
     - At 375 the floor now fits the width with every card on screen, and there is no sideways scroll (nit 7, phone width, fixed).

4. **Floor buttons under 44 px at laptop size: FIXED for full screen.**
   - **Full screen:** Invisible hit areas are at least 44x44 at 1280x720 (steppers 53x51, × 44x44), 50x50 at 1400x900 and 75x75 at 1920x1080. My elementFromPoint sampling shows each one owns 81/81 of its area, so no overlaps.
   - **Narrow and preview layouts (nit):** Below full screen the stepper hit areas are under 44 px wide with a full chain:
     - 36 to 40 px at 760x900.
     - 32 to 35 px at 1000x625.
     - At 680x425 the × hit area owns only 45/81 of its area.
   - The Selected machine panel still gives full-size buttons.

5. **Formula superscripts: FIXED.** `(x + 3)²` and `f⁻¹` now render as real superscripts.

6. **Hint 3 sets the gate to ≥ 0, which already solves levels 7, 8 and 10: unchanged.** It is still a spec question (nit).

7. **Display nits:**
   - **Fixed:**
     - The space before the comma is gone: `(x + 3)², for x ≥ −3`.
     - `×−10` and `÷(−10)` clear the × remove button.
     - Crash chips fit inside OUT.
     - The phone-width floor fits.
   - **Unchanged, as the spec allows:** `1x` and `2((x − 1)³) + 7`.

8. **Contrast and stale tip: FIXED.**
   - **Contrast:** The slot hint text is now #95a2b4, about 7:1 on the plate.
   - **Stale tip:** A keyboard drop clears the tip.

### New finding

9. **Voice lines cut each other off, against the batch voice rule.** Seriousness: should fix.
   - **Cause:** `once()` (src.html 362) calls the kit's `say()`, which stops whatever is playing. It also marks a line said when it is triggered, not when it starts playing. There is no queue.
   - **What I logged with real clicks:**
     - **Welcome cut by placing a part.** Tap Add a, then a top slot 1 s later. The workshop welcome starts, then is cut at 1.0 s by the "Press Run to send the test numbers through" line (placing the first part triggers it). The welcome never comes back.
     - **Gate as the first tap.** The gate line starts and is cut at once by the welcome, and the welcome's play is aborted. Both are marked said, so neither is heard.
     - **Lines triggered with Sound off.** These are marked said and never play after Sound is turned back on. For example, placing a part while muted uses up the "Press Run" line.
     - **Read cut off by a finishing run.** Pressing Read during a Run: when the run ends, the "Every number made it home" line stops Read's speech. In my log Read was stubbed to 3 s, so it ended first. Read's real hint text is about 10 s and the run ends at about 4.3 s, so it would be cut. The rule says nothing queued may cut Read off.
     - **Welcome cut by a level button.** Tapping a level button stops the Puzzles welcome. That is a user action, so it is acceptable.
   - **Model to copy:** ferris-wheel's narrate/hush pattern: queue lines, check Sound before marking a line said, and do not let a triggered line interrupt Read.
   - This was not in the first report and may predate it.

### Checked and fine (no regressions)

- **All 12 puzzles solve with the table answers**, and the check marks persist. Gate edges are unchanged:
  - Level 7: ≤ −3, ≥ −3, ≥ −2 and ≤ −4 solve; ≥ −4 and ≤ −2 crash.
  - Levels 8 and 10: ≥ 0 and ≤ 0 solve; ≥ −1 crashes.
  - Level 9 shows nothing before Run. Run, or pressing Can't be undone, shows "0 and 0.1".
  - Level 11 accepts Flip sign, Add 10 and Reciprocal, Flip sign. It rejects Add 3, Subtract 3 and a single machine, with the right tips.
  - Level 5 with three machines gives "asks for one machine".
- **Done-when items pass:**
  - 2 comes back as −0.6667, and swapping the undo order gives all 8 home with `g = f⁻¹`.
  - Add 3, Square shows "−2 and −4 both come out as 1". Gate ≥ −3 with Square root, Subtract 3 gives 7 home and 1 stopped by the gate.
  - A lone Log base 2 does not count 4 tokens.
- **Keyboard:**
  - Enter lifts a part. Enter drops it on the top line, Right arrow then Enter places it after the last card, and Down arrow then Enter drops it on the undo line. Escape cancels.
  - On a card, `=` `=` `]` Delete work.
  - Tab order is: header, Run, number, panel buttons, the 15 parts, then the floor cards.
- **Drag:** Dragging a part to the top line and to the undo line works at 1280x720, 1000x625 and 680x425.
- **Motion off:** A run ends in about the same time (3.3 s), with fewer distinct frames (tokens jump).
- **Voice lines:** The 11 lines in the code match `voice/lines.json` word for word, and the 11 clips are inlined.
- **Words:** No em dashes in src, notes, spec or lines.

Not verified: how the clips sound (headless Chrome).
