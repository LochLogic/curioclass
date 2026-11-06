# Lunch Survey Cleanup

## One idea
Ridgeview Middle School's lunch survey (412 rows) comes back with 118 blank answers, vegetarian spelled three ways and 21 rows sent twice; every fix you try (drop, reformat or keep) moves the cafeteria's answer and changes who is counted, and the quiet catch is that dropping the blanks deletes every sixth grader, so the report you send the cafeteria manager has to say what your choices did, not only what the chart says.

## Not like
- fair-survey-kit (3-5, concept): plans a survey, then fixes plain mistakes that each have one right fix. Here the survey is already in, every problem has three fixes with real costs, a "Who's in" panel shows who each fix removes, and the work ends in a checked written report.
- catalog-column-rules (9-12, data desk, spec): writes rules that find problems and compares three checking methods. Here the problems are found for you; choosing a fix, seeing its effect and reporting it honestly is the work (the split recorded in docs/agents/audit/clashes-9-12.md).
- simulation-studio (9-12, data desk): one shifted column, ordered cleaning steps, then a simulation. Here three problems, each fix a trade-off, no simulation.
- misleading-charts (6-8 CS): a chart that lies about honest numbers. Here the chart is drawn honestly; the data under it changes with your choices.
- algorithm-audit and model-mechanic (6-8 CS): bias in a formula and in training data. Here bias comes from cleaning choices on survey rows.
- data-table-builder (4) and box-plot-builder (6), data desk: clean data, tables and summaries. Here the data starts dirty and the question is what cleaning costs.
- Dataset: a made-up Ridgeview survey, used by no sibling (Open questions).

## Who and how
- Grades 6 to 8, computer science, module Cleaning Data Honestly (Data and Analysis). Driver: students, solo by default (a teacher can project Clean for a class talk). 25 to 40 minutes (Clean 15 to 20, Report 10 to 15).
- Standards (CSTA 2026): MS-DAT-DC-24 "Analyze options to address data quality issues"; MS-DAT-DI-27 "Summarize a data investigation process, including potential biases, limitations, and supporting evidence".
- tool.json: driver "students or teacher", minutes "25-40", modes ["Clean", "Report"], grades_label "Grades 6-8". Kit starter, `kit:data-desk`.
- No personal prompts. Nothing is stored; no privacy line is needed (a page reload starts fresh).
- Teacher notes: the school, the survey and its rows are made up; the three problems are ones real surveys have (Sources).

## Standards map
| Code | Student action that teaches it | What they see | Done when |
|---|---|---|---|
| MS-DAT-DC-24 | Clean: for each of the three problems, try at least two of its three fixes and choose one; Report Part 1: pick what the chosen fix did and what it cost | the chart, the verdict strip and the Who's in panel change on each tap; under each tried fix an effect line (rows left, who dropped, Vegetarian vs Beef tacos) stays as a side-by-side comparison | 2, 3, 4, 6 |
| MS-DAT-DI-27 | Report: Part 1 (process and cost of each fix), Part 2 (who the cleaned data counts, with the numbers as evidence), Part 3 (limits: what it still can't say), Part 4 (the answer); Check my report tests each statement against the student's own cleaned data; Send prints the report and Ms. Reyes's reply | a letter to Ms. Reyes built from their picks, marks per statement, the reply that names what their fixes did | 6, 7, 8 |

## Screens and modes
Kit frame with the tool's own `:root` (Look). Header: "Lunch Survey Cleanup", small line "Clean it, then say what cleaning did"; mode buttons `Clean` (broom icon) and `Report` (letter icon); Motion, Sound, Read. Layout at 1366x768 in both modes: stage left (about 64 percent), panel right (about 36 percent). The panel top is Marcus's strip: Marcus's cutout (88 px tall) beside a speech bubble holding the hint (`#hint`). At 680x425 and 800x500 stage and panel stay side by side; Marcus's cutout folds (the bubble stays as text), the header art folds, the stage keeps at least 60 percent of the width.

On load: Clean, Chart view, raw data (no fix chosen). Above the chart a note card (Ms. Reyes's cutout, 72 px, and her note, Content) under the cafeteria header strip; a line "412 rows arrived. A made-up school and survey; the problems in it are ones real surveys have." Nothing plays before the first tap. Hint: "Tap a fix on problem 1 and watch the chart and the Who's in panel." The first tap on a fix applies it at once (the main path); a first tap anywhere else does that control's job (BASELINE rule 16). The note card collapses to one line ("Ms. Reyes's rule: vegetarian goes on the menu if more students pick it than pick the least-picked hot lunch.") after the first fix tap; tapping it opens it again.

### Clean (opens first)
Focus: the Picks bar chart, center of the stage, the largest thing (about 50 percent of the stage height at 1366x768), with the verdict strip directly above it and the Who's in panel directly below it.
- Verdict strip (always shown): the painted veg tray and tacos tray beside a menu board drawn in code (a dark green chalkboard panel listing the four menu items in code type), and one line: "Vegetarian [V] vs Beef tacos [T], the least-picked menu lunch: [Add it | Not this time]." Outcomes, each different at a glance: Add: the veg tray sits on the menu board with an "On the menu" tag (check icon), the tacos tray below it, faded; Not this time: the tacos tray on the board, the veg tray below with "Not this time" (X icon); V = 0: the veg tray faded to 40 percent with "0 picks". The least-picked item is computed (it is Beef tacos in all 27 states). Trays move 300 ms (instant with Motion off).
- View buttons over the stage: `Chart` (default), `Rows`, `Days a week`. `Split by grade` toggle in Chart view.
- Chart view: engine bar chart, counts of Pick, categories in fixed order: Chicken tenders, Cheeseburger, Pepperoni pizza, Beef tacos, then each write-in spelling still present (Vegetarian, vegetarian, veg; after Merge only Vegetarian; after Drop none). `yDomain [0, 120]` (Split by grade: `groupBy: 'grade'`, legend Grade 6, 7, 8, `yDomain [0, 50]`). The tool draws over the engine's `barRects` and `scales`: the count above each bar, a leaf tag under each vegetarian bar, a "least picked" tag under the least-picked menu bar, and a thin ghost line at each bar's previous height that stays until the next change.
- Who's in panel (under the chart, about 130 px): four rows, Grade 6 (of 118 students), Grade 7 (of 140), Grade 8 (of 133), Wrote in vegetarian (of 53). Each row is a bar from 0 to the total: counted students solid, removed students as an empty outline with "minus N" text, extra copies as a striped segment past the end with "+N twice". Text always: "Grade 6: 0 of 118". Color is never the only signal.
- Rows view: the working table, engine `renderTable`, 14 rows a page, columns Row (the original row number, never renumbered), Sent, Grade, Form, Pick, Days. Filter chips: All, Blank Days, Write-ins, Sent twice. Filled Days cells show "5" with a "filled" tag; merged Pick cells show "Vegetarian" with "was veg" tag; the second copy of a pair carries a "copy" tag. `Show dropped rows` toggle shows removed rows faded with a "dropped" tag (off by default).
- Days a week view: engine bar chart of Days (0 to 5), `groupBy` Answered / Filled in when Fill is on, `yDomain [0, 220]`; a line under it: "Blank: 118 rows" (Keep), "118 rows dropped" (Drop) or "118 filled in with 5" (Fill), and "Average: 3.1 days" (Content).
- Panel under Marcus: three problem cards, then `Report` (big button). Each card: a painted prop (56 px), title, one detail line, `Show rows` (switches to Rows with that filter), and three fix buttons in a row (a radio group, 44 px tall, about 140 px wide). Under each fix button: "Not tried yet", or once tapped its effect line (Interactions). The applied fix is pressed (filled brand color plus a check icon).
- Problem 1 card reveals Marcus's cause line after `Show rows` or any fix tap on it: "All 118 are paper forms from grade 6, whose laptops weren't handed out yet. The copier printed page 1 only, and Days was on page 2."

### Report
Opening Report before every problem has two fixes tried shows the frame greyed with one line "Try at least two fixes on each problem first." and `Back to Clean`; the hint says the same.
Focus: the letter to Ms. Reyes, the whole stage, in two columns at 1366x768 (left: Part 1 and Part 4; right: Part 2 and Part 3), everything above the fold. At 680x425 one part at a time with Part tabs 1 to 4.
- Part 1 "What we fixed, and what it cost": three rows, one per problem: the chosen fix's name (auto, with "We also tried: ..." and those fixes' effect lines in small type) and three reason chips (one pick each).
- Part 2 "Who our data counts, and what it says": three statements, one pick.
- Part 3 "What we still can't say": seven chips, pick two or more.
- Part 4 "Our answer": `Add the hot vegetarian lunch`, `Keep the menu as it is`, `Ask again first, with a taste test`; one pick, not checked.
- Panel: Marcus's strip; a compact Who's in panel and the verdict line (evidence); `Check my report`; `Send to Ms. Reyes`; after a check, "Matched your data at the first check: x of 5".
- After Send: the letter becomes a report card (the student's statements, each marked "matched", "fixed after a check" or "Marcus fixed") with Ms. Reyes's reply under it (her cutout and note). Buttons `Change my fixes` (to Clean; the next send is Draft 2) and `Copy report` (plain text to the clipboard).

## Content
**Ms. Reyes's note:** "Should we add a hot vegetarian lunch? My rule: if more students would pick it than pick our least popular hot lunch, it takes that spot. Ridgeview has 452 students; the student council ran this survey for me. Ms. Reyes, cafeteria manager."
**The survey:** online form in homerooms, Monday morning; "Which hot lunch would you pick most often?" had a list (Chicken tenders, Cheeseburger, Pepperoni pizza, Beef tacos) and "Other (write in)"; "How many days a week do you eat school lunch?" (0 to 5, required online). Grade 6 used paper forms, typed in on Wednesday.
**Students (391), Pick counts by grade:**
| Grade, form | Tenders | Cheeseburger | Pizza | Tacos | "Vegetarian" | "vegetarian" | "veg" | Total |
|---|---|---|---|---|---|---|---|---|
| 6, Paper | 30 | 22 | 28 | 12 | 11 | 9 | 6 | 118 |
| 7, Online | 38 | 34 | 36 | 18 | 6 | 5 | 3 | 140 |
| 8, Online | 34 | 33 | 35 | 18 | 5 | 4 | 4 | 133 |
Days (online only; grade 6 all blank): grade 7: 0 days 21, 1: 11, 2: 16, 3: 22, 4: 27, 5: 43; grade 8: 19, 11, 15, 22, 25, 41. Combined 40, 22, 31, 44, 52, 84; mean 844 / 273 = 3.09.
**Sent twice (21 students, all online):** grade 7: Tacos 5, Tenders 2, Cheeseburger 2, Pizza 1, "Vegetarian" 1; grade 8: Tacos 4, Tenders 2, Cheeseburger 2, Pizza 2.
**Building the rows (exact, in a build script writing `data/survey.json`):** list students grade 6, then 7, then 8, each grade's picks in the table's column order. The j-th grade 7 student (from 0) gets Days D7[(11 j) mod 140], grade 8 D8[(10 j) mod 133], where D is that grade's Days values sorted ascending. The doubled students are the first n of each (grade, pick) cell in list order. Online students (grade 7 then 8, index j from 0 to 272) go to position (97 j) mod 273; position p is sent "Mon 9:mm:ss" at 9:00:00 plus 8p seconds; a copy follows its original at plus 1 s (p even) or plus 2 s (p odd). Paper students (index j) go to position (37 j) mod 118 after all online rows, Sent "Wed, typed". Rows numbered 1 to 412 in that order. Checks: copy rows are 2, 17, 27, 32, 55, 100, 105, 111, 130, 148, 162, 172, 204, 214, 219, 227 (the "Vegetarian" pair), 235, 244, 254, 268, 291; online rows end at 9:36:16; paper rows are 295 to 412; exactly 21 adjacent pairs have identical answers less than 3 s apart.
**Problem cards:**
1. "118 blanks in Days": "118 rows have no answer for days a week." Fixes: `Drop rows with a blank` / `Fill with the most common answer` (5) / `Keep the blanks`.
2. "Vegetarian spelled three ways": "Vegetarian wasn't on the list, so students wrote it in: Vegetarian 22, vegetarian 18, veg 13. A computer counts each spelling as a different lunch." Fixes: `Drop the write-ins` / `Merge into Vegetarian` / `Keep as typed`.
3. "21 rows sent twice": "21 pairs have the same answers, sent 1 or 2 seconds apart: a double tap on Send." Fixes: `Drop both copies` / `Drop the extra copy` / `Keep both`.
**Outcomes of every state** (Blanks, Spellings, Copies; rows; Vegetarian vs Beef tacos; verdict). Drop blanks (D), Fill (F), Keep (K); Drop write-ins (D), Merge (R), Keep (K); Drop both (B), Drop extra (E), Keep (K). F and K give the same Pick counts; F rows equal K rows.
| Blanks | Spell | Copies | Rows | V vs T | Verdict |
|---|---|---|---|---|---|
| K or F | R | E | 391 | 53 vs 48 | Add |
| K or F | R | B | 370 | 52 vs 39 | Add |
| K or F | R | K | 412 | 54 vs 57 | Not |
| K or F | K | E / B / K | 391 / 370 / 412 | 22 vs 48 / 21 vs 39 / 23 vs 57 | Not |
| K or F | D | E / B / K | 338 / 318 / 358 | 0 vs 48 / 0 vs 39 / 0 vs 57 | Not |
| D | R | E / B / K | 273 / 252 / 294 | 27 vs 36 / 26 vs 27 / 28 vs 45 | Not |
| D | K | E / B / K | 273 / 252 / 294 | 11 vs 36 / 10 vs 27 / 12 vs 45 | Not |
| D | D | E / B / K | 246 / 226 / 266 | 0 vs 36 / 0 vs 27 / 0 vs 45 | Not |
Who's in, examples: raw: grades all in, +11 twice (7), +10 twice (8), write-ins 53 +1 twice; Drop blanks: Grade 6 0 of 118, write-ins 27 of 53; Drop write-ins with Keep both: Grade 6 92, Grade 7 126 +10 twice, Grade 8 120 +10 twice, write-ins 0 of 53; Drop both copies: Grade 7 129, Grade 8 123, write-ins 52. Fill: Days average 3.67 (3.71 with B, 3.63 with K; 3.61 with write-ins dropped and E), 5-day bar 84 + 118 filled; the most common answer is 5 in every state.
**Part 1 reason chips** (true first; the third chip on every row is "It gives the answer I think Ms. Reyes is hoping to hear from us."):
- Drop rows with a blank: "It removes every row with a blank, and every grade 6 answer goes with it." / "It removes only the blank cells and keeps each student's lunch pick."
- Fill: "Every row stays, but the grade 6 Days answers we filled in are guesses of 5." / "Every row stays, and the Days answers show what grade 6 really said."
- Keep the blanks: "Every row stays; the Days chart counts only the students who answered it." / "Every row stays, and each blank Days answer is counted as 0 days."
- Drop the write-ins: "It removes every vegetarian write-in, so those students' picks are gone." / "It removes only the extra spellings and keeps one Vegetarian per student."
- Merge: "It counts veg, vegetarian and Vegetarian as one meal, trusting they match." / "It deletes veg and vegetarian and keeps only rows spelled Vegetarian."
- Keep as typed: "It counts each spelling as its own lunch, splitting vegetarian three ways." / "It keeps the spellings, and the computer still counts them as one lunch."
- Drop both copies: "It removes both copies, so 21 students who did answer are not counted at all." / "It removes only the extra copies, so each of those students counts once."
- Drop the extra copy: "It keeps one copy of each pair, so each of those 21 students counts once." / "It removes both copies, so those 21 students are not counted at all."
- Keep both: "It keeps both copies, so students who sent twice are counted twice." / "It keeps both copies, but the chart still counts each student only once."
Outcome chip reason when picked: "That picks a fix for the answer it gives. Say what the fix does to the data."
**Part 2 statements:** "Counting [W], [S], and [C]: Vegetarian [V], Beef tacos [T]." W: "grades 7 and 8 only" (Drop blanks) or "all three grades". S: "with the three vegetarian spellings counted as one" (Merge), "with each vegetarian spelling counted on its own" (Keep), "with the vegetarian write-ins taken out" (Drop). C: "each student counted once" (E), "[k] students counted twice" (K; k is 21, or 20 when write-ins are dropped), "21 students who sent twice left out" (B). True: the current state. Distractor 1: W flipped. Distractor 2: C moved one step (E to K, K to B, B to E). All three carry the same V and T. Example (K, R, E): "Counting all three grades, with the three vegetarian spellings counted as one, and each student counted once: Vegetarian 53, Beef tacos 48."
**Part 3 chips:** true always: "How often grade 6 eats school lunch: their page 2 never came back" (with Fill: "How often grade 6 really eats school lunch: our 5s are guesses"); "Whether students who picked vegetarian would really buy it"; "What the 61 students who didn't take the survey think" (452 minus 391). True only with Drop blanks: "Which lunch grade 6 would pick". Always false: "Nothing: the data is clean now, so it is complete"; "How many students sent the survey twice"; "Which lunch grades 7 and 8 picked".
**Ms. Reyes's replies** (first matching rule; a second match adds "Also: " and its first sentence):
1. Drop blanks: "Where is grade 6? Their paper forms answered my question on page 1. Please put them back and send it again."
2. Drop write-ins: "No one wants vegetarian? Then who wrote it in? Check whether those rows had to go."
3. Keep both: "Some students count twice here, so tacos look bigger than they are. Fix that first."
4. Keep as typed: "Vegetarian is split three ways on this chart. Is that one meal or three?"
5. Drop both copies: "Twenty-one students lost their say because they pressed Send twice. Keep one copy of each."
6. Otherwise, by Part 4: Add: "A close race, [V] to [T], and you told me what every fix did. I'll run the hot vegetarian lunch for a month and count trays." Keep: "Your own numbers put vegetarian ahead, [V] to [T]. What would change your mind?" Ask again: "Fair. It's close, and grade 6 never told us how often they eat here. I'll run a taste test on Friday."
Every reply ends "Your report matched your data on [x] of 5 statements at the first check."

## Interactions in detail
- A fix tap applies at once: the working DataTable is rebuilt from the raw rows with the three current fixes (`t.replace`), and the chart, verdict, Who's in, Rows and Days views update in the same frame. Tapping the applied fix again does nothing. Before a problem has a fix tapped, its raw data stays in (same data as Keep), but it does not count as tried.
- Effect line under each tried fix, recomputed live with the other two problems as they are now: "[rows] rows · [who] · Veg [V] vs Tacos [T]", where [who] lists up to two Who's in rows below their total ("Grade 6 0 of 118") or "+N twice", else "Everyone counted once". Example (Drop rows with a blank, others raw): "294 rows · Grade 6 0 of 118 · +21 twice · Veg 12 vs Tacos 45".
- Animations: verdict trays 300 ms, ghost lines appear at once; with Motion off all instant. A tap during any of them acts at once on the final layout; nothing waits for an animation or a line.
- Report checks: `Check my report` is enabled once every Part 1 row, Part 2 and at least one Part 3 chip are picked (the hint names what is missing). First check: each statement (three Part 1 rows, Part 2, Part 3 as one) is marked "matches" (check icon) or "doesn't match yet" (X icon, no reason); Part 3 fails if any false chip is picked or fewer than two are picked. The count "x of 5" is set at this first check only. Second check: the statements still wrong are corrected by Marcus, with the reason shown under each (for Part 1 the true chip's text; for Part 2 the clause that differs; for Part 3 why each false chip is false), marked "Marcus fixed". `Send to Ms. Reyes` is enabled after a check where all match, or after the second check, and once Part 4 is picked.
- Changing a fix after any check marks the report "needs a fresh check": Part 1 rows for changed problems, Part 2 and Part 3 are cleared; the next send is the next draft ("Draft 2"), whose count is set at its own first check.
- Chips in each part are shuffled once per draft; Part 1 chips' lengths are within 30 percent.
- Keyboard: fix groups are radio groups (arrows move, Space applies); views and chips in tab order, panel first; the engine table is keyboard paged.
- Mode switches keep state; `V.hush()` on each switch, then the hint for the current step.
- `window.__tool = {state, setMode, fix(problem, option), view(name), split(on), report: {pick(part, row, k), check(), answer(k), send()}, outcome(), allLines, vlog}`.

## Look
Light cafeteria tile: paper `#f3f6ef`, panel `#ffffff`, header `#e3ebdd`, ink `#1c2420`, muted `#56615a`, button line `#7b857e`, focus `#1f5fd1`, warn `#a3261b`, accent `--brand #2f6a33` (lunch-tray green: pressed fixes, the Report button, the header rule) with white text. Charts: `--dd-1 #3d5a80` (menu bars, grade 6), `--dd-2 #2f6a33` (grade 7), `--dd-3 #8a4f9e` (grade 8), `--dd-ring #b45309` (least-picked tag, ghosts). Vegetarian bars take the leaf tag and the word, not a color alone.
Contrast (computed, on paper / on panel): ink 14.55 / 15.88; muted 5.91 / 6.46; brand 5.96 / 6.50; white on brand 6.50; warn 6.75 / 7.37; dd-1 6.47 / 7.06; dd-3 5.21 / 5.69; ring 4.60 / 5.02; focus 5.32 / 5.81; button line 3.50 / 3.82 (non-text); ink on header 13.0. Neighbors: misleading-charts fuchsia, algorithm-audit navy, model-mechanic lime on dark, code-kitchen copper, chore-flowcharts cyan, packet-race red, phishing-spotter cyan, catalog-column-rules purple, box-plot-builder teal; green on mint tile differs from each.

## Art
One style: warm painted illustration, soft morning light. People via Codex or Gemini (`people: true`, on Cory's contact sheet, fresh-agent representation check); the rest local FLUX. No lettering in any image; menu text, labels and names are code.
- lsc-cafeteria: "A bright middle school cafeteria serving line with steel steam trays, stacked green lunch trays and a blank chalkboard menu board, morning light"; 5:1; cutout no; people no; header strip on load (folds at 680x425).
- reyes: "A friendly school cafeteria manager in a green apron with a clipboard, warm smile, waist-up, plain light background"; 3:4; cutout yes; people yes; the note card (72 px) and the reply (96 px), fully visible.
- marcus-ask / marcus-think: "A friendly eighth grade student council member with a lanyard and a clipboard of paper surveys, {curious look, pencil raised | hand on chin, looking at the clipboard}, waist-up, plain light background"; 3:4; cutout yes; people yes; Marcus's strip (ask while waiting, think after a mismatch or a flip); same student in both.
- prop-paper: "A single loose printed survey page with an empty staple hole in the corner on a desk"; 1:1; cutout yes; problem 1 card.
- prop-notes: "Three blank sticky notes in slightly different yellows stuck side by side on a desk"; 1:1; cutout yes; problem 2 card (the three spellings typed over them in code).
- prop-double: "Two identical blank paper cards stacked slightly offset beside a computer mouse"; 1:1; cutout yes; problem 3 card.
- tray-veg: "A green school lunch tray with hot vegetable lasagna, steamed broccoli and an apple, seen from above"; 1:1; cutout yes; verdict strip.
- tray-tacos: "A green school lunch tray with two beef tacos, corn and an orange, seen from above"; 1:1; cutout yes; verdict strip.
Charts, tables, Who's in panel, chips, the letter and preview.svg are drawn in code.

## Voice
Bank voice `casual-peer` (Zubenelgenubi), "Say casually and naturally, like a friendly teenager explaining something": Marcus, the eighth grader on student council who ran the survey and asks you to help. Not used by a 6-8 CS neighbor or a group sibling (misleading-charts and box-plot-builder news-reader, algorithm-audit calm-professor, model-mechanic science-narrator, code-kitchen easy-coach, chore-flowcharts friendly-dad, packet-race firm-captain, phishing-spotter lively-host, catalog-column-rules curious-librarian, data-table-builder knowing-guide, simulation-studio gravel-ranger). `Curio.voice`, `scope: () => state.mode`. No line reads a number from the data; counts are on screen.
- wClean (how; Clean welcome; stale once any fix is tapped): "Ms. Reyes wants to know if the cafeteria should add a hot vegetarian lunch. Our survey came back messy. Tap a fix on problem one and watch the chart."
- tryTwo (how; after the first fix tap; stale once every problem has two tried): "Each problem has three fixes. Try at least two on each one, and watch who stays in the data."
- grade6Gone (how; first time Grade 6 reaches 0; stale once Grade 6 is back): "Whoa. Grade 6 just vanished from the data. Check the Who's in panel."
- flipAdd / flipNot (event; the verdict changes and holds for 600 ms; at most four flip lines per page load, then hint only): "Now vegetarian makes the menu." / "Now vegetarian misses the menu."
- ready (how; every problem has two tried; needs `#to-report`): "You've tried two fixes on every problem. Keep the ones you trust, then tap Report."
- notReady (how; Report opened before ready; stale when ready): "First try at least two fixes on each problem. Tap Back to Clean."
- wReport (how; Report welcome when ready; stale once a chip is picked): "Now tell Ms. Reyes what you did. Pick the statements that match your data, then tap Check my report."
- checkMiss (event; whole; a check with a mismatch, first check): "Some statements don't match your data yet. Change the marked ones, then check again."
- checkFixed (event; whole; second check with a mismatch): "I fixed the ones that didn't match. Read why under each one."
- checkOk (event; whole; a check where all match): with Part 4 picked "Everything matches your data. Tap Send to Ms. Reyes."; without it "Everything matches your data. Now pick your answer in Part 4." (Send is enabled only once Part 4 is picked, so the line never names it while disabled.)
- answerNext (how; after the second check when Part 4 is not yet picked; stale once it is): "Now pick your answer in Part 4, then tap Send to Ms. Reyes."
- sent (event; whole; Send): "Ms. Reyes wrote back. Her note is under your report."
- stale (how; a fix changed after a check; stale at the next check): "Your fixes changed, so your report needs a fresh check."
Event lines play every time their event happens (flips capped as above); how lines are spoken once per page load, then hint only.

## Family engine
data-desk (`kit/data-desk.js` 1.1). Uses: `DataTable` for the raw rows and the working table (`columns`: pick `type: 'text'` with `values` in the fixed order, updated when spellings merge or drop; days `type: 'number'`; grade `type: 'text'`), `t.replace` on every fix, `t.count`, `t.crosstab` (Who's in and the effect lines), `renderTable` (`page: 14`, `index: false` with the Row column, `rowClass`, `cellClass` for filled, merged, copy and dropped tags), `Chart` type `bar` (count mode, `groupBy` for Split by grade and for Days Answered / Filled in, fixed `yDomain`), and `barRects` / `scales` for the tool's own count labels, tags and ghost lines. No engine change. Dataset: the made-up Ridgeview survey, used by no other sibling.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Report gate (two fixes tried per problem) | mash every fix button | trying fixes is the activity; each tap shows its effect and leaves an effect line, so mashing produces the comparison the standard asks for |
| Verdict strip | hunt for fixes until it says Add | not a check: four states say Add, and two of them (Drop both copies) remove 21 real students; Part 1 marks the outcome chip, and the reply names the cost |
| Part 1 reason rows (3) | guess; elimination; longest or shortest chip; position; the outcome chip; copying the effect line | one first-check try counts (guess 1 in 3 each, 1 in 27 for all three); shuffled per draft; lengths within 30 percent; the outcome chip is the common wrong answer and is always marked with its reason; the wrong-fact chip for each fix is the true chip of another fix of the same problem, so only knowing which fix you applied and what it did separates them; the effect line shows numbers, not the cause or meaning the chips state |
| Part 2 statement | match the numbers on screen; pick "all three grades" and "each student counted once" (the common wrong); position; length | all three statements carry the same V and T, so the numbers decide nothing; they differ by who is counted and how copies were handled, which the student must connect to their own fixes and the Who's in panel (that link is the DI-27 skill: the panel is the evidence they cite); the common wrong clauses fit only when grade 6 is kept and one copy of each pair is kept (6 of 27 states), and then the statement holding them is the true one; shuffled; lengths within 11 percent (computed: 127 to 152 characters) |
| Part 3 limits | pick every humble-sounding chip; pick all chips; pick one | "Which lunch grade 6 would pick" sounds humble but is false unless grade 6 was dropped; "How many students sent twice" and "Which lunch grades 7 and 8 picked" are false always; picking all includes false chips; fewer than two fails |
| Answered already on screen | the verdict line or Who's in panel gives the report away | Part 2's numbers are shared by all options, Part 1 asks for meaning, Part 3 limits are not on screen anywhere |
| "x of 5" count | retry checks; change a fix to reset | only the first check of a draft counts; a new draft is labeled Draft 2 on the card and in the reply; Marcus-fixed statements never count |
| Doing nothing | open Report with no fixes tried | the gate line and greyed frame; Check stays disabled until each part has a pick |
| Ms. Reyes's best reply (6) | any path but the three honest fixes | rule order sends every state with Drop blanks, Drop write-ins, Keep both, Keep as typed or Drop both copies to the reply that names that cost; only (Keep or Fill, Merge, Drop the extra copy) reaches rule 6 |

## Heard in order
Grade 6 to 8; few lines, but results land before the next prompt:
- First fix tap: wClean is skipped or cut (BASELINE rule 16; its content stays in the hint and the note card), then tryTwo. If that tap also flips the verdict, the flip line plays first, then tryTwo.
- A fix tap that empties grade 6: grade6Gone (once), then any flip line; a newer fix tap drops lines not yet started.
- The second fix on the last problem: any flip line, then ready (needs `#to-report`, visible).
- Report: Check, then checkMiss, checkFixed or checkOk whole; marks show at once; the next how line (stale) waits for it. Send: sent whole, while the reply is already on screen.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| MS-DAT-DC-24 "Analyze options to address data quality issues" | CSTA, 2026 CSTA PK-12 Computer Science Standards, csteachers.org/2026-csta-pk-12-computer-science-standards/ | CSTA, CodeHS MS CSTA standards alignment, csteachers.org/codehs-ms_csta-standards-alignment/ | yes (one listing says "issue", one "issues") |
| MS-DAT-DI-27 "Summarize a data investigation process, including potential biases, limitations, and supporting evidence" | CSTA 2026 standards listing (as above) | CodeHS MS alignment (as above) | yes |
| Three ways to handle blanks: remove the response, fill an estimate, or flag and leave it | Sampling and Survey Techniques, ch. 7 "Data Validation", bookdown.org/dsciencelabs/sampling_and_survey_techniques | Kang H., "The prevention and handling of the missing data", Korean J Anesthesiol 2013;64(5):402-406 (PMC3668100) | yes |
| Removing rows with blanks can bias results when the blanks are not random (here: all from one group) | Kang 2013 (listwise deletion biases estimates when data are not missing completely at random) | Sampling and Survey Techniques ch. 7 ("handled thoughtfully to avoid biased results") | yes |
| Filling blanks with one typical value adds no information and makes data look surer than it is | Kang 2013 (mean substitution) | The Analysis Factor, "Mean imputation" (a last resort) | yes |
| Duplicate submissions (same answers, seconds apart) should be filtered, keeping one | Sampling and Survey Techniques ch. 7 (identical answers within a short timeframe; one should be excluded) | SightX knowledge base, "Data cleaning" (same answers flagged as duplicates) | yes |
| Text answers that mean the same thing are standardized before counting; a computer counts each spelling apart | Sampling and Survey Techniques ch. 7 ("Fixing typos and inconsistencies", standardizing labels) | OpenRefine manual, "Cluster and edit" (merging variant spellings) | yes |
Backed twice: 7. Cut: 0 used unbacked; not claimed at all: that school lunch use differs by grade, and that a survey pick predicts buying (it is listed as an unknown).
Number checks (Python 3, 2026-11-06): the rows recipe gives 412 rows, 391 students (118, 140, 133), 21 copies at the rows listed, exactly 21 adjacent identical pairs under 3 s; all 27 states' rows, V, T and verdicts in the Outcomes table (no ties; Beef tacos is least picked in every state); Who's in numbers for six states; Days mode 5 in every Fill state, averages 3.09 / 3.67 / 3.71 / 3.63 / 3.61; Part 2 statements distinct in all 27 states with lengths 127 to 152; Part 1 chip lengths within 30 percent; contrast ratios in Look.

## Done when
1. Focus: in Clean the Picks chart is the largest, central thing, with the verdict strip above and Who's in below, all above the fold at 1366x768; at 680x425 stage and panel stay side by side.
2. Each fix tap updates chart, verdict, Who's in, Rows and Days in the same frame; the 27 states match the Outcomes table (spot-check K R E 53 vs 48 Add, D R E 27 vs 36, K R K 54 vs 57, K R B 52 vs 39).
3. Drop rows with a blank shows "Grade 6: 0 of 118" and "Wrote in vegetarian: 27 of 53", plays grade6Gone once, and the tacos tray takes the board.
4. Effect lines appear under every tried fix and update live when another problem's fix changes; Report stays gated until two fixes per problem are tried, and the gate names Back to Clean.
5. Rows view: 14 a page, rows keep their original numbers, filled, merged, copy and dropped tags show text, Show rows filters per problem.
6. Part 1 marks the outcome chip with its reason; Part 2's three statements share V and T and the true one changes with the fixes; Part 3 accepts only true chips and two or more.
7. The x of 5 count is set at the first check only; the second check shows Marcus's fixes with reasons; a fix change makes the next send Draft 2.
8. Ms. Reyes's reply follows the rule order (Drop blanks gives reply 1; K R E with Add gives reply 6 Add with 53 to 48).
9. A tap during the 300 ms tray move or a playing line acts at once; no line names a disabled control; how lines once each, flip lines at most four per load.
10. Art: header, Reyes, Marcus (two poses), three props and two trays load, people fully visible in their strips, no lettering in images; no network requests, no console errors.

## Open questions
- [lunch-survey-cleanup] The data-desk family rule asks for real public data. Real student-level survey rows would be private, so this tool uses a made-up school whose problems are documented survey problems, labeled "made up" on screen. Recommend: accept as a settled exception and note it in docs/families/data-desk.md (that note is not made by this spec).
- [lunch-survey-cleanup] The idea card put the blanks in the English learners' class. This spec moves them to grade 6's paper forms (laptops not yet handed out), so the data never ties a food preference to English learners while the lesson (one fix silently deletes a whole group) stays. Recommend: keep grade 6. Restoring the English learners' class would need the sensitivity review.
