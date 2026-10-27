# Score Keeper

## One idea
While you play a tiny space game, its program runs beside it one highlighted line at a time, and every variable is a labeled box you can watch: a star drops a new value into `score`, a rock takes one from `lives`, a clock bumps `speed`, and `goal` never moves, so the class can see which values are stored and which ones change, and what makes them change.

## Not like
- loop-garden (grade 2, built): repeat blocks that move a gardener on a grid, scored by block count. Here nobody arranges blocks and there is no star rating; the program is fixed and the subject is the values it keeps.
- code-tracer (grade 4, same batch): students predict each value before a line runs, line by line, as a puzzle. Here nothing is predicted or graded; values change live because of game events (a catch, a hit, time passing) and the student measures and records what happened.
- game-remix (grade 5, same batch): changes a working program (its rules and lines) and shares it. Here the program's lines never change; the Lab only turns the starting numbers and the two "how much" numbers with dials, as the variable under test in an experiment.
- traffic-light-coder (grade 3): if-then rules the student writes. Here the two `if` lines are already written and only read.
- input-output-machine (grade 2): input turning into output. Here input matters only because it triggers lines that change stored values.
- teach-the-robot (grade 2, lab): training data for a classifier; different topic, same format only.

## Who and how
- Grade 3, computer science. Module: Variables in Programs (Algorithms and Programming), "Identify stored and changing values".
- Driver: students or teacher. Students on laptops in pairs; it also works on a projector, where the teacher runs Play and the class calls out which box will change.
- 20 to 30 minutes: Play (5), Lab (15), Notebook (5 to 10). Each mode stands alone for a 10 minute demo.
- Standards: E3-PRO-VD-06 (CSTA 2026, as listed in the catalog). Matching CSTA 2017 standard: 1B-AP-09, "Create programs that use variables to store and modify data."
- Tool header: title "Score Keeper", subtitle "Watch variables change". Modes (`.seg`): **Play**, **Lab**, **Notebook**, then kit buttons **Motion**, **Sound**, **Read**. Start from `kit/starter/src.html`.

## Screens and modes

### Layout (all modes but Notebook)
Three parts, laid out at real pixel size per window (do not scale one fixed design):
1. **Game** (the stage): a night sky with 5 lanes, the ship at the bottom, falling stars and rocks. Top strip of the game shows nothing but the game; all numbers live in the boxes, never in a game HUD, so the boxes are the only place to read them.
2. **Variable shelf**, directly under the game: five boxes in this order: `score`, `lives`, `speed`, `best`, `goal`. Each box: a drawn cardboard-style box with the name on a label on its front, an icon beside the name (score a star, lives a heart, speed a lightning bolt, best a trophy, goal a flag), one value card sitting in the box (large digits, at least 28 px at 1366x768), and under it a small line "changed 3 times" (this round).
3. **Program card**, to the right of the game: the program (see Content), in a monospace font at least 15 px, one event block per card section, the event line in bold. The line that is running gets a raspberry left bar, a pale gold background and a small ▶ marker; the line that just ran keeps a faint tint for 1 s.
- Panel (kit `aside`): hint paragraph `hint`, then controls (by mode, below), then the **Lab log**: a short scrolling list, newest on top, one line per value change, for example "Caught a star: score 3 → 4", "Rock hit: lives 2 → 1", "10 seconds: speed 1 → 2", "Game ended: best 0 → 8". Lines that ran without changing a value also log: "Rock hit: lives 3 → 3 (same value)". Max 40 lines, oldest dropped.
- Wide windows (1000 px and up): game left, program card middle, panel right; shelf under game and program card together. Under 900 px tall, panel buttons come first and the log shrinks. At 760 wide: game and shelf, then the controls row, then program card, then log. At 375: same order, shelf boxes in a 3 + 2 grid, program card scrolls on its own. Play/Pause, Step and the move buttons must be visible without scrolling at every size in STANDARDS.md.

### Play (default mode)
- Controls: **▶ Play** (becomes **⏸ Pause** while running, **▶ Resume** while paused), **Step** (enabled only while paused), **Play again** (shown after a game ends; same button slot as Play), **Code speed**: segmented **Watch** (default) / **Quick**, toggles **Autopilot** (off) and **Same sky** (off), and big **◀** and **▶** move buttons (60 px, for touch and for anyone who prefers buttons).
- The student moves the ship lane to lane (Left/Right arrows, A/D, the move buttons, or tap/click a lane). A star in the ship's lane when it lands is caught; a rock in the ship's lane hits; anything else falls past and fades.
- Every catch, hit, 10-second tick, end check and game end fires its event block, and its lines run visibly (see Interactions).

### Lab
- Same screen. Autopilot on and Same sky on by default (both still toggle; the hint says "Turn one dial with its minus and plus buttons, then press **Run**. Autopilot plays the same sky every time, so only your number makes the difference.").
- **Question card** above the program card: the current experiment question (Content), with **◀ Prev** and **Next ▶** and "Question 2 of 7".
- **Dials** appear inside the program card on the five editable numbers: in `lives = 3`, `score = 0`, `speed = 1` (the "when the game starts" lines) and the amounts in `score = score + 1` and `lives = lives - 1`. Each dial is the number with a **−** and **+** button either side (44 px), keyboard focusable, arrow keys work when focused. `best = 0` and `goal = 20` have no dials. Dials lock while a game runs.
- Buttons: **▶ Run** (Pause/Resume/Step as in Play), **Reset lab** (sets all dials back to their defaults and re-runs "when the page opens", so best goes back to 0), and after each game a **Result card** over the game: "Ended because lives is 0 or less" or "Ended because score is goal or more", then the final value of every box and "Stars caught 8, rocks hit 3". Result card buttons: **Save to notebook** and **Run again**.

### Notebook
- **Runs table** (columns in Content), one row per saved run. Buttons **Copy table** (tab separated with header, for a spreadsheet; on clipboard failure show the text in a selectable box with "Select all and copy."), **Save notebook** (localStorage), **Clear notebook** (asks "Clear all saved runs? Yes / No").
- **Score chart**: one bar per saved run, final score, run number under each bar, value on top of each bar, a dashed line at the goal (20) labeled "goal". Bars are raspberry; the label carries the number, so color is not the only signal. Drawn in SVG.
- **Stored or changing?** Five variable cards (score, lives, speed, best, goal), each showing "changed N times in your runs" (sum over saved runs). Two bins: **Stayed the same** and **Changed**. Drag a card or focus it and press 1 or 2 (or its two small buttons "Same" / "Changed"). Button **Check with my runs** gives a line per card from the evidence (Content). Needs at least one saved run; otherwise it says "Save a run from the Lab first."
- **What I found**: three short text boxes with sentence starters (Content). Saved only with Save notebook.

## Content

### The program (our own tiny language; exactly these lines)
```
when the page opens:
  best = 0
  goal = 20

when the game starts:
  score = 0
  lives = 3
  speed = 1

when you catch a star:
  score = score + 1

when a rock hits you:
  lives = lives - 1

every 10 seconds:
  if speed < 5:
    speed = speed + 1

when lives is 0 or less:
  end the game

when score is goal or more:
  end the game

when the game ends:
  if score > best:
    best = score
```
- Spoken and read as: "score equals score plus one", "if speed is less than 5".
- Store the program as data (event name, list of lines; each line an object such as `{set: 'score', from: 'score', add: 1}` or `{if: ['speed', '<', 5], then: [...]}`), and render the text from it. The dials change the numbers in that data. A small interpreter runs it. No `eval`, no `new Function`, no parsing of typed text (nothing is typed).
- "End checks" (the two `when ... is ... :` blocks) run after every catch or hit, lives check first. If a check is true its line `end the game` runs, then "when the game ends" runs, then play stops.
- "when the page opens" runs once on load (silently, boxes appear holding 0 and 20) and again on Reset lab. "when the game starts" runs at Play, Run, Play again, Run again.
- A line "changes" a box only if the new value differs from the old. The "changed N times" counter on each box resets at game start; best's change at game end counts in that game.

### Game numbers
- 5 lanes. Ship starts in lane 3.
- At speed s: a new drop appears every 1.6 − 0.2 (s − 1) seconds (1.6, 1.4, 1.2, 1.0, 0.8) and takes 3.0 − 0.4 (s − 1) seconds to fall (3.0, 2.6, 2.2, 1.8, 1.4). Both use the speed when the drop appears. First drop appears at game time 0.
- The 10-second clock counts game time only (not pauses, not Watch freezes). If a tick and a landing fall at the same instant, the tick runs first.
- **Same sky off:** each drop is a star with chance 0.7, else a rock; lane random (never the same lane as the previous drop's lane twice in a row three times).
- **Same sky on:** a 10-drop pattern that repeats: kinds S S R S S S R S R S (S star, R rock), lanes 2 4 1 3 5 2 3 1 4 3.
- **Autopilot:** in the pattern, it catches stars 1, 2, 4, 5, 8, 10, misses star 6 (arrives one lane short), dodges rock 7, and is hit by rocks 3 and 9 (it is heading for the next star). It glides one lane per 0.25 s toward its next target. With Same sky off it catches every star it can reach and is hit by every third rock.

### Reference results (Lab, Same sky and Autopilot on, after Reset lab, other dials at default; computed)
| Change | Ends at drop | Because | score | lives | speed | best | caught | hits | changes: score, lives, speed, best |
|---|---|---|---|---|---|---|---|---|---|
| none | 13 (20.8 s) | lives | 8 | 0 | 3 | 8 | 8 | 3 | 8, 3, 2, 1 |
| lives = 1 | 3 | lives | 2 | 0 | 1 | 2 | 2 | 1 | 2, 1, 0, 1 |
| lives = 9 | 32 (41.4 s) | goal | 20 | 3 | 5 | 20 | 20 | 6 | 20, 6, 4, 1 |
| star + 5 | 5 | goal | 20 | 2 | 1 | 20 | 4 | 1 | 4, 1, 0, 1 |
| star + 2 | 13 | lives | 16 | 0 | 3 | 16 | 8 | 3 | 8, 3, 2, 1 |
| rock − 0 | 32 | goal | 20 | 3 | 5 | 20 | 20 | 6 | 20, 0, 4, 1 |
| rock − 2 | 9 | lives | 5 | −1 | 2 | 5 | 5 | 2 | 5, 2, 1, 1 |
| speed = 5 | 13 (11.0 s) | lives | 8 | 0 | 5 | 8 | 8 | 3 | 8, 3, 0, 1 |
| score = 10 | 13 | lives | 18 | 0 | 3 | 18 | 8 | 3 | 8, 3, 2, 1 |
| star + 10 | 2 | goal | 20 | 3 | 1 | 20 | 2 | 0 | 2, 0, 0, 1 |
Running "none" a second time without Reset lab: same row but best stays 8 and best changes 0 times.

### Dial ranges
- lives start 1 to 9; score start 0 to 15; speed start 1 to 5; star amount 1, 2, 5, 10 (− and + step through the list); rock amount 0, 1, 2, 3. Defaults 3, 0, 1, 1, 1.

### Lab questions (question card)
Each question names the dial to turn and the button to press, then asks (STANDARDS "Say how to act").
1. "Start lives at 1: press the minus on lives until it says 1, then press Run. How long does the game last now?"
2. "Make a star worth 5: press the plus on the star line until it says 5, then press Run. What happens to score? Why does the game end so soon?"
3. "Make a rock take 0: press the minus on the rock line until it says 0, then press Run. Which box stops changing?"
4. "Start speed at 5: press the plus on speed until it says 5, then press Run. Does the speed box ever change? Look at the if line."
5. "Start score at 10: press the plus on score until it says 10, then press Run. Did Autopilot catch more stars, or did score just start higher?"
6. "Make a rock take 2: press the plus on the rock line until it says 2, then press Run. Look at lives at the end. Can a variable go below zero?"
7. "Press Run again without changing anything. Which boxes start over, and which keep their value?"

### Runs table columns
Run, Question, lives start, score start, speed start, star adds, rock takes, Ended because, score, lives, speed, best, goal, Stars caught, Rocks hit, Changes (score/lives/speed/best/goal, as "8/3/2/1/0"). Up to 30 rows; at 30, Save to notebook is disabled with "Notebook full. Copy and clear it to keep going."

### Stored or changing? feedback (Check with my runs)
- Count 0: "goal changed 0 times in your runs. It stayed the same: the program stored it and never changed it."
- Count above 0, card in Changed: "lives changed 9 times in your runs. It is a changing value."
- Card in the wrong bin: "Look again: score changed 30 times in your runs." / "Look again: goal changed 0 times in your runs."
- best with count 0: "best changed 0 times in your runs. Try a run that beats best, then check again." (Its card is never marked wrong in that case.)
- Unsorted card: "Put this card in a bin first."
- Under the bins, always: "A variable is a named box that holds one value. Some values are stored and stay the same. Others change while the program runs."

### What I found (sentence starters)
1. "A variable changes when ..."
2. "The variable that never changed was ... I know because ..."
3. "When I changed ..., the game ..."

### On-screen definitions
- Play hint: "Press **Play** to start. Move the ship with the arrow buttons or the arrow keys. Each box is a **variable**: watch which line changes it."
- Play game-over hint: "Game over. Press **Play again** and watch which boxes start over."
- Lab hint: "Turn one dial with its minus and plus buttons, then press **Run**. Autopilot plays the same sky every time, so only your number makes the difference."
- Lab result-card hint: "Press **Save to notebook** to keep this run. Then press **Run again**, or turn a dial first."
- Notebook hint: the notebook-welcome line, or with no saved runs the no-runs line.
- Pause hint: "Paused. Press Step to run one line at a time."
- First overwrite toast (once per page): "New value in, old value gone. A variable holds one value at a time."

## Interactions in detail
- **Watch** code speed: when an event fires, the game freezes (falling things hang, a light dim over the game), the event line highlights for 500 ms, then each line in the block highlights for 700 ms. On an assignment, a copy of the new value flies in an arc from the line to its box (500 ms), the old value card slides out of the box and fades (it does not go anywhere: gone), the box gives one soft bump and gold glow, its counter ticks. A "same value" line shows the card shaking once with "same" beside it, and no counter change. Then the game resumes.
- **Quick**: 200 ms per line, no freeze, value cards swap with a short glow, no flying. Lines still highlight.
- **Pause** freezes game and code mid-line. **Step** while paused: if a line is waiting, run just that line (with Watch animation) and stay paused; if not, let the game run until the next event fires, highlight its event line, and pause. Space toggles Pause/Resume, S is Step, when focus is not on a text box.
- Motion off: no flying or bumping; value cards change in place with a gold outline; highlight timing is unchanged so lines are still readable, and falling things move in steps of their lane position each 0.25 s instead of smoothly.
- Game end: a big "Game over" (lives) or "Goal!" (score) banner over the game, drawn in code, then "when the game ends" runs visibly. Play shows Play again; Lab shows the Result card.
- Second and later games: "when the game starts" lines run visibly at Play again, so score, lives and speed drop back; best and goal do not move. Voice beat 8 plays once.
- Switching modes calls `Curio.stop()`, stops the game, keeps best, and resets the round (boxes show the start values from that mode's settings). Play uses default numbers even if Lab dials were changed; the Lab keeps its dials.
- Lives below zero (rock − 2 or 3) shows the negative number in the box; the Lab log says "lives 1 → −1". No clamping.
- A started game that nobody touches in Play keeps running and ends normally (lives).
- All buttons 44 px or larger, move buttons 60 px, visible focus ring, tab order: game controls, dials, question card, log.
- Expose `window.__tool = {state, setMode, allLines, run(settings)}` where `run` plays a Lab game instantly (no animation) and returns the result row, for checking the table above.

## Look
- Scene: a calm night sky, deep indigo `#141a3a` to `#1e2650`, small drawn twinkling stars, the backdrop image along the bottom. Stars to catch are warm gold `#ffd76a` with a glow; rocks grey-brown.
- Page and panel: warm off-white `--paper:#fbf6f1`, `--panel:#ffffff`, `--ink:#2a2233`, `--muted:#5e5468`, `--line:#e6dbe0`, `--focus:#3b6fd6`.
- Accent `--brand:#a82755` (raspberry), `--btn:#a82755`, `--head-ink:#ffffff`. No other built CS tool uses it (loop-garden is green, blue, purple and orange blocks). Running-line background `#fff3cf` with ink text.
- Box icons and label colors: score gold, lives coral, speed cyan, best violet, goal green; the name and icon are always printed, so color is never the only signal.
- Contrast (computed, WCAG): white on `#a82755` 6.8:1; `#a82755` on paper 6.3:1; ink on paper 14.2:1; muted on paper 6.6:1; white on `#1e2650` 14.5:1; gold `#ffd76a` on `#1e2650` 10.5:1; dark text on `#f5b83d` glow 8.6:1; focus `#3b6fd6` on paper 4.4:1 (non-text, needs 3:1). All pass AA.
- Friendly, a little playful (grade 3): soft bumps and glows, no confetti; the "Goal!" banner gets a short gold sparkle.

## Art
- backdrop: "a quiet purple and blue alien desert horizon at night, smooth rolling dunes and two small round rock formations, soft glowing nebula low in the sky, flat vector illustration, deep indigo upper sky left plain and dark" (`scripts/cfart.py`); 16:9 (1600x900); cutout no; people no. Used as a strip along the bottom of the game behind the ship, cropped to cover; the sky above it is drawn in code.
- ship: "a small friendly round cartoon spaceship seen from the front at a slight angle, teal and cream body, one big round window, three short legs, flat vector, solid white background" (`scripts/gptart.py`, base); 1:1; cutout yes; people no. The player's ship.
- rock: "a lumpy grey-brown cartoon space rock with a few craters, flat vector, solid white background" (`scripts/gptart.py`, sibling of ship with `"ref"` and `"ref_mode": "style"`); 1:1; cutout yes; people no. Falling rocks, rotated randomly.
- Drawn in code: night sky and twinkles, the five lanes (faint), stars to catch, variable boxes, value cards, flying values, banners, chart, bins. If the art is missing, draw the ship as a teal circle with a window and the rock as a grey blob so the tool still works.
- No other tool in this batch may use a spaceship, space rock or night desert image.

## Voice
`voice/lines.json`: `"bank": "friendly-dad"`, `"voice": "Achird"`, `"style": "Say in a relaxed, friendly way, like a kind dad helping with homework"`. Fits grade 3 and a homework-help feel; differs from loop-garden (hero-coach) and from the batch (lively-host, bright-teacher, clear-teacher, big-sister). Only corner-store (grade 2 math) also uses it; not a near neighbor. On-screen text is the main channel; these are all the fixed lines. Each beat plays once per page load, except play-over, lab-result, sort-fix and sort-unsorted, which name the next action every time they apply. A game line is dropped if its moment passes before it starts. Read speaks the hint (and, in the Lab, the current question).
1. play-welcome: "This is Star Catch. Each box under the game is a variable, and it holds one value. Press Play to start, and steer with the arrow buttons or the arrow keys."
2. first-catch: "You caught a star, so the score line ran. Score got bigger by the star's points, and the old value is gone."
3. first-hit (not when a rock takes 0; first-same covers that): "Ouch, a rock. The lives line ran and took the rock's amount from lives."
4. first-speed: "Ten seconds went by, so speed went up. Nobody pressed anything. Time changed that one."
5. end-lives: "Lives got to zero or less, so the game ended."
6. end-goal: "Score reached the goal, so the game ended."
7. first-best: "Score was more than best, so best saved it."
8. play-over (Play, every game over, not once per page): "Game over. Press Play again and watch which boxes start over."
9. lab-result (Lab, every result card until the first save): "Press Save to notebook to keep this run. Then press Run again, or turn a dial first."
10. second-game: "New game. Score, lives and speed went back to their starting values. Did best change? Did goal?"
11. first-same: "That line ran, but the value stayed the same. Running a line doesn't always change a box."
12. first-pause: "Paused. Press Step to run one line at a time."
13. lab-welcome: "Welcome to the lab. Turn one dial with its minus and plus buttons, then press Run. Autopilot plays the same sky, so you can see what your change does."
14. to 20. lab-q1 to lab-q7: the seven Lab questions, word for word, as written in Content.
21. saved: "Saved to your notebook."
22. below-zero: "Look at lives. The program took away more than was left, so it went below zero."
23. notebook-welcome (with saved runs): "Here are your runs. Drag each card into a bin, or press Same or Changed on it. Then press Check with my runs."
24. notebook-empty (no saved runs): "No runs yet. Go to the Lab, press Run, then press Save to notebook."
25. sort-checked (only when every card is right): "Nice work. Your runs are the evidence."
26. sort-fix (any card marked Look again; every Check): "Some cards say Look again. Move each one to the other bin, then press Check with my runs again."
27. sort-unsorted (no Look again but a card not in a bin; every Check): "Put every card in a bin, then press Check with my runs again."
Read also speaks the Play, Play game-over, Lab and Lab result-card hints, which are recorded as lines too.

## Family engine
none. The interpreter, the game loop and the Same sky pattern live in the tool's script; keep the interpreter in one marked block `/* VARIABLES ENGINE: begin */ ... /* end */` with no DOM access (it takes the program data, the current variables and an event name, and yields one line at a time with `{line, var, old, new}`), so game-remix or code-tracer could reuse it later if Cory wants.

## Sources
- Variable as a placeholder for information that can change: Code.org CS Fundamentals glossary, "Variable". https://code.org/curriculum/docs/k-5/glossary
- Variables store and modify data in programs: CSTA K-12 Computer Science Standards (2017), 1B-AP-09. https://csteachers.org/k12standards/
- Module code E3-PRO-VD-06: CSTA PK-12 Computer Science Standards (2026), from `data/standards/csta-2026-ids.txt` and `data/modules.csv`.
- A variable holds one value and setting it replaces the old value: Scratch Wiki, "Variable" (set and change blocks). https://en.scratch-wiki.info/wiki/Variable
- All game numbers and the reference table are invented for this tool and computed from the rules above.

## Done when
1. Lab, Reset lab, default dials, Run: ends at the 13th drop with score 8, lives 0, speed 3, best 8, and the Result card says "Ended because lives is 0 or less"; `__tool.run` matches every row of the reference table.
2. Run again without Reset: same values, best still 8, best's counter "changed 0 times", goal "changed 0 times".
3. Rock takes 2: lives box shows −1 at the end and voice beat 20 plays.
4. In Watch mode each catch freezes the game, highlights `when you catch a star:` then `score = score + 1`, flies the new value into the score box and ticks its counter; the Lab log gets "Caught a star: score N → N+1".
5. Pause then Step runs exactly one line per press; Space and S work; game time (and the speed clock) does not advance while paused or frozen.
6. Speed start 5: the `if speed < 5:` line highlights every 10 seconds but speed never changes.
7. Notebook: two saved runs appear in the table and chart; Check with my runs marks goal as stayed the same and score, lives as changed, with counts that equal the table; Copy table pastes tab separated text; Save notebook survives a reload; Clear notebook empties it.
8. Every size in STANDARDS.md: Play/Pause, Step and the move buttons are visible without scrolling, the five boxes readable; 375 wide works in `drive.py --host`.
9. Keyboard only can play a game in Play, set every dial and save a run; held clicks log the right voice clips; no line plays twice; console clean.
10. Search the file: no `eval`, no `new Function`, no network requests, and "Curio" appears only as "Curio Class" in visible text.
