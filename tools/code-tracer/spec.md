# Code Tracer

## One idea
Before each line of a short program runs, you write down what you think it will do in the next row of a trace table; then the line runs and writes the real value in beside your guess, so every surprise (a copy that does not follow, a swap that loses a number, an `if` that quietly skips) shows up right where you predicted it.

## Not like
- score-keeper (grade 3, same batch): variables change live while a space game runs and you watch boxes. Here there is no game and no live events: a fixed program waits for you, nothing runs until you commit a prediction, and the variables live as columns in a trace table, not boxes.
- loop-garden (grade 2, built): arrange repeat blocks to move a gardener, fewest blocks wins. Here nobody builds or arranges code; you read it and predict it. Repeat appears only as something to trace.
- robot-dance (K, same batch): find the wrong card in a dance sequence as a class. Here nothing is broken on purpose except one note (the swap), and the skill is predicting values, not spotting a wrong step.
- traffic-light-coder (grade 3): write if-then rules. Here `if` lines are already written; you predict whether each one is true.
- game-remix (grade 5, same batch): change a working game program and share it. Here the Workbench changes only numbers in tiny programs to see the trace change; no game, no sharing.
- data-table-builder (grade 4): tables of class data and charts. The trace table here records a program's steps, not collected data, and has no charts.

## Who and how
- Grade 4, computer science. Module: Trace the Code (Algorithms and Programming), "Follow how data changes variables; document programs".
- Driver: students or teacher. Pairs on laptops (one types, both argue), or the teacher on a projector with the class holding up whiteboard guesses before Run line.
- 15 to 25 minutes: levels 1 to 6 in one sitting (10 min), 7 to 12 the next (10 min), Workbench any time (5 min).
- Standards (CSTA K-12 CS Standards 2026, as listed for the module): E4-PRO-VD-06, E4-PRO-RD-07, E4-PRO-TR-08. 2017 crosswalk for teachers who still use it (matched by topic): 1B-AP-09 (create programs that use variables to store and modify data), 1B-AP-17 (describe choices made during program development using code comments), 1B-AP-15 (test and debug a program to ensure it runs as intended).
- tool.json: driver "students or teacher", minutes "15-25", modes ["Trace", "Workbench"], grades_label "Grade 4". Start from `kit/starter/src.html`.

## Screens and modes
Header (kit): title "Code Tracer", small line "Predict, then run". Mode buttons (`.seg`): **Trace** (opens first, level 1), **Workbench**. Then Motion, Sound, Read (ids `motion`, `sound`, `read`).

Stage (both modes), two parts side by side, laid out at real pixel size per window (no fixed-design scaling):
1. **Code card** (left, about 40 percent): a dark slate editor card. Line numbers in a gutter, then the program in a monospace stack (Consolas, Menlo, monospace), at least 18 px at 1366x768, 14 px minimum anywhere. Line 1 is always the note (`# ...`). Indented lines sit under `repeat` or `if` with a thin guide line. The line about to run has a lighter bar, a 4 px orange left edge and a ▶ in the gutter. Lines already run keep a faint tick in the gutter. Lines skipped by a false `if` dim and get a small "skipped" tag for that pass.
2. **Trace table** (right, about 60 percent): a graph-paper notebook page. Columns: **Step**, **Line**, one column per variable in order of first appearance (named in the header row in monospace), **Check** (for `repeat` and `if` rows), **Says**. One row per step that runs. The cell a step writes is ink, bold, 20 px; the other variables in that row show their carried value small and light grey, so the newest value of every variable is always in the bottom row. The table scrolls inside its page and auto-scrolls to the newest row. Under the table: the tally "First-try matches: 3 of 4".

Panel (kit `aside`), Trace mode:
- `#hint` (always a fixed voice line).
- **Prompt label** (on screen only, templated): "After line 3, apples will be" / "Line 5 says" / "Line 4: is temp more than 80?"
- **Keypad**: 0 to 9, **−** (sign), **⌫**, in a 3 x 4 grid; then the big **Run line** button (`.big-btn.gold`, play triangle). For an `if` step the keypad is replaced by two big buttons **Yes** and **No**.
- **Just show me** (small link-style button): runs the line without a guess.
- Level strip: 12 dots in 4 labeled sets ("One box", "Two boxes", "Repeat", "If"); a dot fills when its level is traced. Tapping a dot opens that level (all open, no locks).
- **Restart level** (circular arrow), **Next level** (right arrow; glows when this level is traced), **Print trace** (printer icon).
- After the last step of a level with a note check: the **Note check** card ("Does the note tell the truth?" with the note quoted, buttons **Yes** / **No**).

Panel, Workbench mode:
- `#hint`, then **Program** list: 13 buttons ("1 Apples" to "12 Careful lives", "13 Swap with a spare").
- **◀ Back**, **Step ▶**, **▶ Play** (becomes **⏸ Pause**), **Restart**, **Speed** (Slow / Quick), **Predict** toggle (off), **Reset numbers**, **Print trace**.
- When Predict is on, the keypad and Run line appear as in Trace (no tally).

### Mode 1: Trace (puzzle levels)
- A level opens with the program on the code card, an empty table, the ▶ on the first line that runs (line 2; the note is skipped) and the prediction cell drawn as a dashed orange box in the new row under that line's variable (or under Says, or Check).
- The student types a number and presses Run line (or Enter). The line runs: its bar pulses, a value chip slides from the right end of the code line into the dashed cell (400 ms), the guess stays visible. Then the next line that runs gets the ▶.
- `repeat` rows need no guess: the repeat line lights for 700 ms and writes "round 2 of 4" in Check, then the ▶ moves into the body.
- After the last step: the "Traced!" stamp drops onto the page with the tally, the level dot fills, and (levels 6, 9, 12) the Note check card appears. Next level glows when the note check is answered (or at once on other levels).
- After level 12: line 10, and the Workbench button glows once.

### Mode 2: Workbench (explore)
- Pick any program. The whole trace is built at once but shown one row at a time: Step adds the next row (with the same chip motion), Back removes the last row and moves the ▶ back, Play steps on its own (Slow 1200 ms, Quick 500 ms per step), Restart clears the table.
- Every literal number in the code is a dotted-underlined chip. Tap it (or focus and Enter): a small stepper pops up beside it with **−**, the value, **+**. Changing it rebuilds the trace, restarts at step 0, and puts a yellow "?" tag on the note line ("changed: still true?"). Reset numbers puts all numbers back and removes the tag.
- No tally, no stamp, no note check. Predict on makes Step wait for a guess like Trace.

## Content

Tiny language (ours, rendered from data, never parsed from typing):
- `name = value` where value is a whole number, a variable, or `x op y` with op `+`, `-`, `*` and x, y each a number or variable. The right side is worked out first, then stored on the left.
- `say x` writes the value of x in Says. `repeat N times:` runs its indented lines N times. `if x > n:` / `if x < n:` runs its indented lines only if true. `# text` is a note: shown, never run, the ▶ skips it.
- On screen and in speech: `>` is read "is more than", `<` "is less than", `*` "times".
- Store each program as data, for example `{set:'dogs', a:'cats', op:'+', b:{n:2, id:'n1'}}`, `{say:'dogs'}`, `{repeat:{n:4,id:'n2'}, body:[...]}`, `{if:['temp','>',{n:80,id:'n3'}], body:[...]}`, `{note:'...'}`. Literal numbers carry ids so Workbench can change them.

Levels (line 1 is the note; trace steps are line:result; ★ = the aha step whose why line shows in the hint after it runs):
| # | Set | Title | Program (lines 2 on) | Trace (computed) | ★ | Note check |
|---|---|---|---|---|---|---|
| 1 | One box | Apples | `# count the apples in the basket` / `apples = 3` / `apples = apples + 2` / `apples = apples - 1` / `say apples` | 2: apples 3; 3: apples 5; 4: apples 4; 5: says 4 | step 2 | none |
| 2 | One box | New value | `# the last value wins` / `steps = 2` / `steps = 7` / `steps = steps + 1` / `say steps` | 2: 2; 3: 7; 4: 8; 5: says 8 | step 2 | none |
| 3 | One box | Double up | `# coins after a trade` / `coins = 10` / `coins = coins - 4` / `coins = coins + coins` / `say coins` | 2: 10; 3: 6; 4: 12; 5: says 12 | step 3 | none |
| 4 | Two boxes | Copy, not link | `# b gets a copy of a` / `a = 4` / `b = a` / `a = 9` / `say b` | 2: a 4; 3: b 4; 4: a 9; 5: says 4 | step 4 | none |
| 5 | Two boxes | Cats and dogs | `# count the pets` / `cats = 5` / `dogs = cats + 2` / `cats = dogs - 1` / `dogs = dogs + cats` / `say dogs` | 2: cats 5; 3: dogs 7; 4: cats 6; 5: dogs 13; 6: says 13 | step 4 | none |
| 6 | Two boxes | The swap | `# swap left and right` / `left = 3` / `right = 8` / `left = right` / `right = left` / `say left` / `say right` | 2: left 3; 3: right 8; 4: left 8; 5: right 8; 6: says 8; 7: says 8 | step 4 | answer **No** |
| 7 | Repeat | Jumps | `# count 4 jumps` / `jumps = 0` / `repeat 4 times:` / `  jumps = jumps + 1` / `say jumps` | 2: 0; 3: round 1 of 4; 4: 1; round 2; 2; round 3; 3; round 4; 4; 5: says 4 | step 9 | none |
| 8 | Repeat | Doubling tower | `# the tower doubles 3 times` / `blocks = 1` / `repeat 3 times:` / `  blocks = blocks * 2` / `say blocks` | 1; round 1; 2; round 2; 4; round 3; 8; says 8 | step 7 | none |
| 9 | Repeat | Add them up | `# add 1 + 2 + 3` / `total = 0` / `n = 1` / `repeat 3 times:` / `  total = total + n` / `  n = n + 1` / `say total` | total 0; n 1; round 1; total 1; n 2; round 2; total 3; n 3; round 3; total 6; n 4; says 6 | step 10 | answer **Yes** |
| 10 | If | Fan check | `# turn the fan on when it is hot` / `fan = 0` / `temp = 75` / `if temp > 80:` / `  fan = 1` / `say fan` | fan 0; temp 75; check no (line 5 skipped); says 0 | step 3 | none |
| 11 | If | Bonus round | `# big bonus, but too big resets` / `points = 8` / `if points > 5:` / `  points = points + 10` / `if points > 15:` / `  points = 0` / `say points` | 8; check yes; 18; check yes; 0; says 0 | step 4 | none |
| 12 | If | Careful lives | `# lives never go below 0` / `lives = 3` / `repeat 4 times:` / `  if lives > 0:` / `    lives = lives - 1` / `say lives` | 3; round 1; yes; 2; round 2; yes; 1; round 3; yes; 0; round 4; no (line 5 skipped); says 0 | step 12 | answer **Yes** |

Steps and guesses per level (computed): 1-4: 4 steps, 4 guesses; 5: 5/5; 6: 6/6; 7: 10 steps, 6 guesses; 8: 8/5; 9: 12/9; 10: 4/4; 11: 6/6; 12: 13/9. Round rows need no guess.

Workbench only, program 13 "Swap with a spare": `# swap left and right, using a spare box` / `left = 3` / `right = 8` / `spare = left` / `left = right` / `right = spare` / `say left` / `say right`; trace: left 3, right 8, spare 3, left 8, right 3, says 8, says 3.

Workbench number ranges: values and `if` numbers 0 to 20; repeat counts 1 to 6; a number after `*` 0 to 5. Largest possible value is 20 x 5^6 = 312500, so cells fit 6 digits plus a minus sign (negatives happen, for example coins 0 - 4 = −4, shown with a true minus sign).

## Interactions in detail
- Typing: digits, Backspace, and `-` (sign toggle) work from the keyboard when the panel or stage has focus; max 4 digits in Trace, 6 in Workbench; leading zeros dropped ("07" is 7). The guess shows live in the dashed cell.
- Run line with an empty cell: nothing runs, the cell shakes once, line 14 plays.
- Match: the real value lands on top of the guess, a green check mark and the word "matched" appear in the cell corner, soft chime (`Curio.yes`). First match per page load: line 3.
- Miss: the real value lands bold; the guess stays in the cell, small, struck through, in muted brown, so the row shows both. Low soft tone, never a buzzer. First miss per page load: line 4. On the level's ★ step, the why line (W1 to W12) replaces the hint and is spoken if the guess missed (shown, not spoken, if it matched; Read speaks it).
- If steps: Yes/No (or Y/N keys). Right or wrong, Check gets "yes" or "no" with a check mark or the struck-through guess, same as numbers. On "no", the body lines dim with "skipped" and the ▶ jumps past them.
- Just show me: runs the line, the cell gets a small "shown" tag, it counts as not matched; line 13 once per page load.
- No going back in Trace (the prediction must come first); Restart level clears the table and tally. Opening another level or switching modes drops the current trace (each mode keeps its own level or program and numbers for the page load). Nothing is saved to localStorage except the kit's Motion setting.
- Note check (levels 6, 9, 12): one answer, right or wrong both show the feedback line (N1 to N6); a wrong answer then also shows the right answer highlighted. Line 8 is the hint while the card waits.
- Print trace: `window.print()` with a print stylesheet showing only the title, program (light background, dark text) and the full table.
- Motion off (`body.calm`): no chip slide, pulse or stamp drop; values appear in place with an orange outline for the same 400 ms. Timings stay the same.
- Keyboard: Tab order is mode buttons, header buttons, keypad, Run line, Just show me, Restart, Next, Print, level dots, then the code card's number chips (Workbench). Enter runs the line; visible focus (3 px blue ring with a white inner ring so it shows on the dark code card).
- Sizes: the code card, the newest table row and Run line are visible without scrolling at every size in STANDARDS.md. Wide (1000+): code card, table, panel in three columns; under 900 px tall the keypad and Run line come first in the panel. 680x425 and 800x500: same three columns, compact keypad (keys at least 36 px), code 14 px, table 13 px. 760 wide: code card and table side by side, panel below with the keypad in one row of 13 keys plus Run line. 375 wide (`drive.py --host`): code card, then table (max 40 percent of height, scrolls), then a sticky bottom bar with the keypad (two rows) and Run line.
- Expose `window.__tool = {state, setMode, setLevel(n), trace(programId, overrides)}`; `trace` returns the step list (line, kind, var, before, after, check, says) with no animation, for checking the Content table.
- Search the file: no `eval`, no `new Function`; the engine reads only program data. Keep it in one marked block `/* TRACE ENGINE: begin */ ... /* end */` with no DOM access.

## Look
- Band 3-5, own `:root`. A pencil-and-graph-paper notebook beside a dark code editor.
- `--paper #f6f4ec` (cream page), `--panel #ffffff`, `--ink #1f2a36`, `--muted #5d6672`, `--line #e2ddd0`, `--brand #a8461a` (pencil orange, the accent; header and Run line outline), `--btn #a8461a`, `--head-ink #ffffff`, `--focus #2f5bd3`, `--gold #ffd27a` for Run line. Table grid lines `#d9e4f0` (decoration), header row `#fde7c8`.
- Code card: slate `#22303c`; text `#e8eef3`; variable names `#ffd27a`; numbers `#8fd3ff`; keywords (`repeat`, `times`, `if`, `say`) `#ff9e7a`; notes `#a6d99f`; running-line bar `#34495c` with orange edge `#f08a4b`; skipped lines `#9aa7b4`.
- Matched green `#1f7a3d`; struck guess `#7a6a5e`; dashed prediction box `#a8461a`.
- Neighbor check: score-keeper raspberry `#a82755` on a night sky; robot-dance magenta `#b0206a` on a navy stage; loop-garden lawn green. Pencil orange on cream paper with a slate editor is unlike all of them. computer-builder and game-remix should not take pencil orange.
- Contrast (computed, WCAG): white on `#a8461a` 5.91:1; `#a8461a` on paper 5.36:1; ink on paper 13.22:1; muted on paper 5.28:1; green on paper 4.88:1; struck guess on paper 4.71:1; ink on `#fde7c8` 12.09:1; ink on gold 10.22:1; focus on paper 5.36:1. On slate `#22303c`: text 11.54, names 9.48, numbers 8.31, keywords 6.7, notes 8.38, skipped 5.5. On the running bar `#34495c`: text 7.97, names 6.55, numbers 5.74, keywords 4.63. All pass AA. Color is never the only signal: check mark, strike-through, ▶ and "skipped" tags carry the meaning.
- Calm and tidy (grade 4): no confetti; the "Traced!" stamp is the one flourish.

## Art
none: drawn in code. Code card, notebook page and grid, value chips, check marks, the "Traced!" stamp (orange rubber-stamp ring), level dots and preview.svg are SVG/CSS. preview.svg: the slate code card with level 5 and the ▶ on line 5, beside a half-filled trace table with one matched and one struck-through guess. No raster images, so nothing overlaps the batch (score-keeper's ship, rock and desert stay its own).

## Voice
Bank voice `clear-teacher` (Iapetus), style "Say clearly and kindly, like a patient elementary school teacher". Fits a careful, step-at-a-time puzzle for grade 4. Differs from every near neighbor: score-keeper friendly-dad, robot-dance lively-host, computer-builder bright-teacher, game-remix big-sister, loop-garden hero-coach; its only other user is melt-or-not (grade 2 science), not a neighbor. Queue copies collision-lab (narrate, hush, readNow, firstTap). Each line plays once per page load unless noted; Read speaks the current `#hint`, which is always one of these lines. Templated text (prompt label, "You said 6. It is 12.", the tally) is on screen only, never spoken.

1. "Welcome to Code Tracer. A program runs one line at a time. Before each line runs, predict what it will do. Then run it and check." (Trace welcome)
2. "Type your guess in the empty box, then press Run line." (hint for number steps)
3. "It matched. You traced that line just like the computer would."
4. "Not quite. Read the line again. The right side is worked out first, then stored in the variable on the left."
5. "This line asks a question. Is it true? Choose yes or no." (first if step; hint for if steps)
6. "A repeat line runs the lines tucked under it again and again. Watch the round number." (first round row)
7. "Lines that start with a hash sign are notes for people. The computer skips them." (after level 1 is traced, after 9)
8. "Now test the note. Does the note tell the truth about what happened?" (note check)
9. "Traced! Your table is a record of every step the program took." (level done)
10. "You traced all twelve programs. Try the Workbench and change the numbers."
11. "This is the Workbench. Tap a number in the code to change it, then step through and watch the table." (Workbench welcome)
12. "You changed the code. Is the note still true? Notes don't change by themselves." (first number change)
13. "Here is what that line does. Next time, try a guess first." (first Just show me)
14. "Type a guess first, or press Just show me." (every empty Run line, not once only)

Why lines (★ steps, W1 to W12):
- W1 "apples equals apples plus 2 takes the 3 already in apples, adds 2, and stores 5 back in apples."
- W2 "Setting steps to 7 throws the 2 away. A variable holds only one value at a time."
- W3 "coins plus coins is 6 plus 6. Both use the value coins holds right now."
- W4 "b equals a copied the 4. When a changed later, b kept its own 4."
- W5 "Use the newest value in each column. cats was 6 by then, so dogs becomes 7 plus 6, which is 13."
- W6 "left got the 8 first, so the 3 was gone. Then right equals left copied 8 back."
- W7 "Each round adds 1 to jumps. Four rounds, four more."
- W8 "Each round doubles blocks: 1, then 2, then 4, then 8."
- W9 "Each round, total adds the current n, then n goes up by one. 1 plus 2 plus 3 is 6."
- W10 "temp is 75. Is 75 more than 80? No, so the line inside the if is skipped and fan stays 0."
- W11 "The first if made points 18. So the second if sees 18, which is more than 15."
- W12 "In round 4, lives is 0. Is 0 more than 0? No. So lives stops at 0."

Note check feedback (N1 to N6):
- N1 (level 6, No): "Right. The note says swap, but both ended up 8. The code does not do what the note says. Try Swap with a spare on the Workbench."
- N2 (level 6, Yes): "Look at the last row. left is 8 and right is 8. Did the 3 get swapped over?"
- N3 (level 9, Yes): "Right. total ended at 6, and 1 plus 2 plus 3 is 6. The note is true."
- N4 (level 9, No): "Check the table. total ended at 6. What is 1 plus 2 plus 3?"
- N5 (level 12, Yes): "Right. Four rounds, but lives stopped at 0. The if kept it from going below 0."
- N6 (level 12, No): "Look down the lives column. Did it ever go below 0?"

Which line when: Trace entry queues 1 then 2. Workbench entry queues 11. Level done: 9, then 7 (first time), then 8 on note levels; after level 12: 10. Hint while a number step waits is 2, an if step 5, after a ★ step the W line until the next step runs, during a note check 8, after answering the N line.

## Family engine
none. No CS family engine exists. The trace engine stays inside `src.html` in its marked block (pure: program data plus number overrides in, step list out), so it could later merge with score-keeper's VARIABLES ENGINE if Cory wants one shared interpreter.

## Sources
- CSTA K-12 Computer Science Standards, 2026 PK-12 identifiers E4-PRO-VD-06, E4-PRO-RD-07, E4-PRO-TR-08 (`data/standards/csta-2026-ids.txt`, `data/modules.csv`).
- CSTA K-12 Computer Science Standards (2017), 1B-AP-09, 1B-AP-15, 1B-AP-17: https://csteachers.org/k12standards/
- Variable (a placeholder for a piece of information that can change), loop, conditional: Code.org CS Fundamentals glossary, https://code.org/curriculum/docs/k-5/glossary
- Setting a variable replaces its old value: Scratch Wiki, "Variable" (set and change blocks), https://en.scratch-wiki.info/wiki/Variable
- Assignment works out the right side first, then binds the name; `#` starts a comment the interpreter ignores: The Python Tutorial, sections 3.1 and 3.2, https://docs.python.org/3/tutorial/introduction.html
- Trace tables as a way to follow variable values line by line: Isaac Computer Science, "Trace tables" (https://isaaccomputerscience.org), and BBC Bitesize GCSE Computer Science, "Trace tables".
- Programs, values and traces are original to Curio Class and computed by the rules above (checked in Python).

## Done when
1. Every level's trace from `__tool.trace(n)` matches the Content table row for row (values, checks, skipped lines, says), and the steps/guesses counts match.
2. Level 1 played with correct guesses: each Run line writes the value into the dashed cell with the chip motion, green check and "matched"; the tally ends "4 of 4", the stamp drops, the dot fills, Next level glows.
3. Level 4 with guess 9 on step 4: the cell shows 4 bold with 9 struck through, W4 is in the hint and its clip starts in the voice log.
4. Level 10: the if step shows Yes/No instead of the keypad; after No, line 5 dims with "skipped" and the ▶ goes to line 6. Level 12 round 4 does the same.
5. Levels 6, 9, 12 show the Note check; each answer gives the right N line; Next level enables only after answering.
6. Edge cases: empty Run line (shake, line 14), Just show me ("shown" tag, not counted), leading zeros, Restart level, switching level mid-trace, mode switch keeps each mode's place.
7. Workbench: change level 8's repeat to 6 and its `* 2` to 5: trace ends at blocks 15625, the note gets the "?" tag, line 12 plays once; Back and Step walk rows both ways; Reset numbers restores 8 and removes the tag; program 13 swaps (says 8 then 3).
8. Every size in STANDARDS.md: code card, newest table row, keypad and Run line visible without scrolling; code text at least 14 px; 375 wide works in `drive.py --host` with the sticky keypad bar.
9. Keyboard only finishes level 9 (digits, Enter, Y/N) with visible focus on the dark card and the paper; held clicks give the right welcome/skip behavior; Read stops speech and speaks the hint; no line repeats except 14.
10. Motion off: no slides or stamp drop, same timing; console clean; no `eval` or `new Function`; no network requests; "Curio" appears only as "Curio Class"; Print trace shows only program and table.
