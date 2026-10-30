# Model My World

## One idea
Each situation comes with its record (bills, fares, balances), and the equation you type has to reproduce every
row: rows light up as hits or show a gap bar as misses, so you fix your equation until it matches the whole record,
then use it to answer the one question the record can't (month 15, the most data under budget, which ticket mixes
are possible).

## Not like
- which-model-wins (gr 9, same group): fits three model families to noisy real data and picks by prediction. Here the record follows an exact rule; you write the rule from the words and it must hit every row.
- equation-golf (gr 9, same group): solves given equations with moves. Here you create the equation, then solve it with any method.
- phone-plan-showdown (gr 7): two plans argued in role play. Here one plan is a piecewise bill and the question is an inequality.
- two-trains (gr 8) and intersection-quest (gr 9): systems where lines meet. Here the two-variable case is a feasible region of constraints.
- unit-detective / Unit Sense (gr 9, same group): units decide claims. Units appear here only as labels.

## Who and how
- Grade 9, Algebra 1, Creating Equations. Students drive. 20 to 40 minutes.
- Topic line: "writing equations and inequalities for real situations".
- Standards (module): A-CED.A (A.1 equations and inequalities in one variable, including exponential; A.2 two-variable equations graphed; A.3 constraints and viable solutions; A.4 rearranging formulas).
- CCSS clusters: cases 1, 4, 6 serve A-CED.A.1 and A.2; case 2 A.1 (inequality); case 5 A.3; cases 3 and 7 A.4.
- tool.json: driver "students", minutes "20-40", modes ["Situations"], grades_label "Grade 9".

## Screens and modes
Header: title, subtitle "Write the rule. Match the record." One mode, `Situations`, with a case list. Kit buttons.

Focus: the equation box and the record table under it, center stage and the largest thing on screen; the rows light
up there. Layout (wide): left a narrow column with the story card (its painting on top, the words under it) and the
case list; center the equation box, the hit count and the record table; right the graph (plane from the graphing
kit), smaller. Under 1000 px wide: story card (painting cropped to a short band), equation box, record, graph, in that
order. The equation box, `Check` and the record's hit count are visible without page scrolling at every size.

For each case:
- Story card: the case's painting (Art), a short paragraph (Content) and the variable letters with units ("m = months,
  C = total paid in dollars").
- Record: a table of rows (`table.inst`). After each check, each row gets "hit" with a check glyph, or "miss" with a
  gap bar and the gap in units ("off by $12.00"). Rows mark in a quick top-to-bottom sweep of 400 ms (all at once with
  Motion off).
- Equation box: free typing; allowed: numbers, the case's letters, + − * / ^, parentheses, = < > <= >= (and ≤ ≥).
  Implicit multiplication is allowed (12m, 500(1.04)^t). `Check` (or Enter). Line under it: "6 of 6 rows hit".
- Graph: the record as points, and the student's equation drawn after each check (solved for the output letter when
  possible; inequalities shade the true side). Axes labeled with the letters and units.
- Question card (opens under the record when every row hits): one question the record doesn't answer directly, an
  answer box, and `Answer`.
- `Hint` (appears after three checks with misses; Interactions).
Case list buttons `1` to `7`, each with a small crop of its painting and its title; a met case gets a check and
"matched". Saved on this device (localStorage `curio-model-my-world`, try/catch) with `Clear progress`.

## Content
All businesses and prices are made up (labeled "made-up prices" on each story); the temperature formula is real.
1. Climbing gym. "A climbing gym charges a joining fee once, then the same price every month." Letters m, C.
   Record (m, C): (1, 37), (2, 49), (3, 61), (4, 73), (5, 85), (6, 97). Rule C = 12m + 25.
   Question: "After how many months will you have paid $205 in all?" Answer 15.
2. Phone data. "The plan costs $30 a month and includes 5 GB. Each GB over 5 costs $8 (parts of a GB are charged
   by the fraction used)." Letters g, B. Record (g, B) for g ≥ 5: (5, 30), (6, 38), (7.5, 50), (9, 62), (10, 70).
   Rule B = 30 + 8(g − 5) for g ≥ 5. The row (2, 30) appears greyed with the note "under 5 GB the bill is $30 flat;
   this case models 5 GB and up". Question (inequality): "Your budget is $60 a month. Write an inequality for g and
   find the most data you can use." Answer: 30 + 8(g − 5) ≤ 60, g ≤ 8.75 GB.
3. Ride fare (rearranging). "A ride costs a $3.50 base fare plus $2.25 a mile." Letters d, F. Record (d, F):
   (2, 8.00), (4, 12.50), (7.2, 19.70), (10, 26.00). First rule F = 2.25d + 3.5; then the card asks "Rewrite it
   to give d from F" and checks d = (F − 3.5)/2.25 against the rows the other way round. Question: "You have $30.
   How far can you ride?" Answer d ≤ 11.78 mi (to 0.01).
4. Savings. "$500 goes into an account that pays 4 percent once a year, added to the balance." Letters t, B.
   Record (t, B): (0, 500.00), (1, 520.00), (2, 540.80), (3, 562.43), (4, 584.93), (5, 608.33) (rounded to cents).
   Rule B = 500(1.04)^t. Question: "In which year does the balance first pass $700?" Answer year 9 (B(8) = 684.28,
   B(9) = 711.66).
5. Band concert (constraints). "Student tickets cost $8 and adult tickets $12. The band needs at least $2,400.
   The gym seats 250." Letters s, a. No record table; instead a ticket-mix list of five proposals (s, a): (100, 120),
   (60, 160), (150, 100), (200, 80), (0, 200). The box takes several lines, one constraint each. Target constraints:
   8s + 12a ≥ 2400, s + a ≤ 250, s ≥ 0, a ≥ 0. The graph shades the region where all of the student's constraints
   hold and marks each proposal "viable" or "not viable". Check passes when the student's region equals the target
   on every whole-number point from −50 to 300 on both axes. a ≥ 0 is already forced by the first two (they need
   a ≥ 100), so a check without it still passes, and the card then says "a ≥ 0 was already forced: the money and the
   seats need at least 100 adults." Question: "Which proposals are viable?" Answer: (60, 160), (150, 100), (0, 200).
   Not viable: (100, 120) raises $2,240; (200, 80) seats 280.
6. Garden path (quadratic). "A square garden has a path 2 ft wide all the way around it. Side s is the garden alone;
   A is the area of garden plus path." Letters s, A. Record (s, A): (2, 36), (4, 64), (6, 100), (8, 144).
   Rule A = (s + 4)². Question: "The garden and path cover 196 square feet. How long is the garden's side?"
   Answer 10 ft (the tool notes s = −18 also solves (s + 4)² = 196 but a side can't be negative).
7. Thermometer (rearranging, real formula). "A thermometer shows Celsius; the sign outside shows Fahrenheit."
   Letters C, F. Record (C, F): (0, 32), (100, 212), (37, 98.6), (−40, −40). Rule F = 1.8C + 32 (or 9/5 C + 32);
   then "Rewrite it to give C from F": C = (F − 32)/1.8. Question: "The sign says 50. What is it in Celsius?" Answer 10.
   The sign's reading ("50 °F") is drawn in code on the sign's blank panel in the painting.

## Interactions in detail
- Parsing: a small safe expression parser (no eval). Unknown letters are refused with "This case uses m and C".
- Checking an equation: for each record row, substitute the row's values into both sides; a hit when
  |left − right| ≤ 0.005 (half a cent; cases 3 and 4 use money rounded to cents). Any equivalent form hits:
  C − 25 = 12m, C = 25 + 12m, (C − 25)/12 = m.
- Rearranging steps (cases 3 and 7): the second check requires the equation solved for the asked letter: one side is
  exactly that letter and it does not appear on the other side; then rows are tested as above.
- Inequalities (case 2's question and case 5): the solution set is tested on the case's domain on a grid
  (case 2: g from 5 to 20 in steps of 0.01, plus the exact boundary 8.75) and must agree everywhere with the target;
  ≤ versus < is told apart by the boundary point. Case 5 tests every whole-number (s, a) from −50 to 300 (the
  negative strip is what makes s ≥ 0 necessary).
- Question answers: numbers within 0.01 (case 3: 11.78 or 11.77 is "about right, rides are charged by distance,
  so 11.77 keeps you under $30"); case 2 accepts g ≤ 8.75 or 8.75; case 4 accepts 9 or "year 9"; case 6 accepts 10
  and answers −18 with the note above.
- A miss never says what the right equation is. After three checks with misses, a `Hint` button names the pattern
  to look at ("Compare rows 1 and 2: what does one more month add?").
- Tap while it plays: a new Check, a case change or typing during the 400 ms row sweep or a graph redraw ends it at
  once and shows the new state.
- Graph: uses `kit/graphing.js` (Plane, fn, point, label); ranges per case fit the record with 10 percent margin.
- `window.__tool = {state, open(n), check(text), answer(text)}`.

## Look
Accent `--brand #d4e65a` (lime), `--brand-ink #1a1f03`. Story card `#1b2430` with a thin lime top rule over the
painting; record hits marked by a check glyph and "hit", misses by a gap bar `#ffb8a8` with "miss" and the gap in
words; the student's curve uses `--gr-1` with its dash pattern; feasible region `--gr-3` at 25 percent opacity with a
hatch. The paintings share one style (bright, flat-shaded gouache, daylight colors) so the seven cases read as one
town. Contrast (computed): brand on panel 12.58:1, on --sec-bg 11.92:1, brand-ink on brand 12.30:1.

## Art
Local FLUX (`scripts/localart.py`), all without people. One style: bright flat-shaded gouache illustration. Each is
the top of its story card (4:3, cropped to a short band under 1000 px) and, cropped small, its case list button.
- gym-wall: "An empty indoor climbing gym wall covered in bright colorful handholds, thick blue crash mats on the
  floor, a coiled rope and a carabiner hanging from a hook, daylight from high windows, bright gouache illustration";
  4:3; cutout no; people no; case 1.
- phone-plan: "A smartphone lying face up on a wooden desk beside a coiled charging cable, its screen a plain glowing
  teal panel, bright gouache illustration"; 4:3; cutout no; people no; case 2.
- ride-cab: "A yellow city taxi with a plain white roof sign parked at a curb on a rainy evening street, wet
  reflections of shop lights, bright gouache illustration"; 4:3; cutout no; people no; case 3.
- piggy-bank: "A pale pink ceramic piggy bank on a sunny windowsill beside a small potted plant and a short stack of
  coins, bright gouache illustration"; 4:3; cutout no; people no; case 4.
- concert-gym: "A school gym set up for a band concert, rows of empty folding chairs facing a low stage with music
  stands, a drum kit and a tuba, a ticket table by the door with a plain metal cash box, bright gouache
  illustration"; 4:3; cutout no; people no; case 5.
- garden-path: "Top-down view of a square vegetable garden bed full of lettuce and carrots, surrounded by a gravel
  path of even width and a low wooden fence, bright gouache illustration"; 4:3; cutout no; people no; case 6.
- temp-sign: "A tall outdoor time-and-temperature sign on a pole with a plain dark rectangular display panel, beside a
  glass thermometer mounted on a brick wall, blue sky, bright gouache illustration"; 4:3; cutout no; people no;
  case 7; the builder measures the panel's box once and draws the reading in code inside it.
The record table, gap bars, graph, region shading, check glyphs and preview.svg are drawn in code (they are tables,
charts and controls).

## Voice
Bank voice `casual-peer` (Zubenelgenubi, "Say casually and naturally, like a friendly teenager explaining
something"). Not used by math 9-12 neighbors, group siblings or the R02 batch. `Curio.voice`,
`scope: () => state.caseId`. Stories, rows and notes are read on screen; Read speaks the hint.
- welcome (how, first load; stale once any Check is pressed): "Pick a situation from the list. Type an equation in the box and press Check. It has to hit every row."
- miss (how, first check with a miss; stale when every row hits or the case changes): "See the gap bars? Change the equation and press Check again."
- hint (how, the first time the Hint button appears; stale when every row hits or the case changes): "Stuck? Press Hint to see which rows to compare."
- flip (how, first rearranging step in case 3 or 7; stale when that step passes): "Same rule, flipped. Get the other letter alone on one side, then press Check."
- region (how, case 5 opens; stale when its check passes): "Type one constraint per line, then press Check. The shaded part is every mix that works."
- allHit (event, every row hits; stale on case change or a new check): "Every row hits. Now type your answer under the question and press Answer."
- wrongAns (event, a question answer that misses; stale on the next answer or case change): "Not that one. Use your equation to work it out, then press Answer again."
- right (event, question answered right; stale on case change): "That's it. Your equation answered it. Pick another situation from the list."

## Family engine
none (uses `kit/graphing.js` for the plot only, with no new engine features).

## Sources
- A-CED.A: Common Core State Standards for Mathematics, High School Algebra, Creating Equations, https://www.thecorestandards.org/Math/Content/HSA/CED/
- Linear and exponential models from words; literal equations: OpenStax, Elementary Algebra 2e, 2.6 "Solve a Formula for a Specific Variable", https://openstax.org/books/elementary-algebra-2e/pages/2-6-solve-a-formula-for-a-specific-variable; compound interest: OpenStax, College Algebra 2e, 6.1 "Exponential Functions", https://openstax.org/books/college-algebra-2e/pages/6-1-exponential-functions
- Celsius and Fahrenheit (F = 1.8C + 32; −40 is the same on both): NIST, "Temperature conversions", https://www.nist.gov/pml/owm/si-units-temperature
- Gym, phone, ride, savings, concert and garden prices are made up for the tool and labeled so on screen.
- Checks run (Python, 2026-10-29): every record row reproduces from its rule; case 4 rows sit within 0.0036 of
  500 × 1.04^t (inside the 0.005 tolerance), 500 + 20t hits rows 0 and 1 only, first year over $700 is 9 (684.28,
  711.66); case 2 boundary g = 8.75; case 3 (30 − 3.5)/2.25 = 11.778, and 11.78 mi costs $30.005 while 11.77 costs
  $29.98; case 5 proposals raise 2,240, 2,400, 2,400, 2,560, 2,400 with 220, 220, 250, 280, 200 seats. Case 5 on
  the old 0 to 300 grid: leaving out s ≥ 0 gave the same region, so the old Done when 5 could never fail; on a
  −50 to 300 grid it does fail, and leaving out a ≥ 0 still passes (every point of the region has a ≥ 100), so the
  grid and the card note changed. Case 6: (s + 4)² = 196 gives s = 10 or s = −18; the old note said −24, now −18.
  Case 7: 37 °C gives 98.6 °F, 50 °F gives 10 °C.

## Done when
1. Case 1: "C = 12m + 25", "12m + 25 = C" and "(C − 25)/12 = m" all hit 6 of 6; "C = 12m" misses every row with gaps of $25.00; the question accepts 15.
2. Case 2: "B = 30 + 8(g − 5)" hits all five rows; the inequality "30 + 8(g − 5) ≤ 60" passes and "< 60" fails at the boundary.
3. Case 3: the rearranged "d = (F − 3.5)/2.25" passes; "F − 3.5 = 2.25d" is refused for the rearranging step (not solved for d) though every row hits.
4. Case 4: "B = 500(1.04)^t" hits all six rows (tolerance half a cent); "B = 500 + 20t" hits rows 0 and 1 only; the question accepts 9.
5. Case 5: the four target constraints shade the right region and mark (100, 120) and (200, 80) not viable; leaving out s ≥ 0 fails the check; leaving out a ≥ 0 passes with the "already forced" note.
6. Case 6 accepts A = (s + 4)² and A = s² + 8s + 16; the question accepts 10 and explains −18.
7. Case 7: F = 9/5 C + 32 hits all four rows; 50 °F gives 10 °C; the sign's reading sits inside the painted panel at every size.
8. Focus: at 1366x768 and 1000x625 the equation box with the record under it is the largest thing on screen, center, and the graph is beside it, smaller.
9. Tap while it plays: pressing Check again or switching case during the row sweep shows the new result at once, with no rows left half marked.
10. Every case's painting loads and matches its story; no voice line names a hidden or disabled control (Hint, Answer).
11. Unknown letters are refused with the case's letters named; no eval is used; console clean, no network; every size keeps the box and hit count visible.

## Open questions
- none.
