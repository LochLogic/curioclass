# Road Trip Logbook

## One idea
A family sets off on a five-day road trip (a made-up route, labeled so) and the child keeps the logbook: each evening the child rounds the day's miles to estimate, then adds them to the running total in columns with the standard algorithm (Day 1: 386 miles, Day 2: 457, so far 843), and a dashboard odometer rolls its wheels while the child regroups, so carrying a ten looks like the ones wheel rolling past 9 and nudging the tens wheel; each night the child also subtracts to find the miles left to the 2,000-mile goal (2,000 - 843 = 1,157), regrouping across zeros like an odometer rolling backward; every answer is checked against the estimate, and a far-off answer makes the car's map dot land in the wrong town; on the last day the logbook total, the odometer (48,629 at the start, 50,629 at the end, rolling past 49,999) and the map all agree at 2,000 miles, so a fourth grader learns to add and subtract multi-digit whole numbers fluently with the standard algorithm and to check answers with estimates.

## Not like
- area-model-builder (4, concept): multiplying and dividing big numbers. Here adding and subtracting them.
- stadium-count (4, concept): place value and rounding. Here using place value to regroup.
- place-value-vault (2, spec): bundling tens and hundreds. Here the column algorithm.
- unit-ladder (4, concept): distance with unit changes. Here miles added in columns.

## Who and how
- Grade 4, Math, module "Adding and Subtracting Multi-Digit Numbers". Standards: 4.NBT.4 (fluently add and subtract multi-digit whole numbers using the standard algorithm).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Change note (spec fix, 2026-11-10): the trip is unchanged. Added: the sibling works the first sum as a model, each column box now says right or wrong as it is typed, and a Trip ledger stage follows the trip, twelve mixed sums and differences of four to six digits done without the odometer, so the child gets the repeated practice that "fluently" asks for.
- Five trip days, one worked sum, five column additions and five subtractions, the odometer, estimates, the map, then the Trip ledger (twelve problems). Extra: My route (the child types five day lengths and a goal). tool.json `modes: ["Road trip", "My route"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.NBT.4 (add) | add multi-digit whole numbers using the standard algorithm | the student | Add each day to the total in columns, regrouping | 4 trip sums and 6 ledger sums (3 to 6 digits; one, two and three carries) | the column sum; the odometer rolling | 2 |
| 4.NBT.4 (subtract) | subtract multi-digit whole numbers using the standard algorithm | the student | Subtract the total from the goal, regrouping across zeros | 5 trip differences and 6 ledger differences (two across zeros) | the column difference; the odometer rolling back | 3 |
| 4.NBT.4 (fluently) | fluently: accurate, and quicker with practice | the student | Work the twelve ledger problems with no odometer and no carry chips offered, against the child's own time | 12 | a ledger page; a "your time" line, never a countdown | 5 |
| 4.NBT.4 (check) | not in the standard's wording; kept as the check on each answer | the student | Estimate first and compare | 10 | the estimate beside the answer; the map dot | 4 |

## Screens and modes
Header (kit): title "Road Trip Logbook"; `Road trip`, `My route`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A car dashboard with an odometer at 48,629, a map with five day stops, and an open logbook. The welcome is queued (`welcomeAfter: true`): "Day 1 is done: 386 miles! Day 2: 457. How far so far? Round each day first. Tap Estimate." First hint: "Tap Estimate."

**The sibling goes first (the model).** Day 1's fuel stop is worked by the older sibling in the back seat: 268 + 175, said column by column ("8 and 5 is 13, write 3, carry the 1"), with the odometer rolling as she goes. It cannot be skipped and `Show me again` reopens it.

**Estimate.** The child rounds each day to the nearest hundred (386 is about 400, 457 is about 500) and writes the estimate (900).

**Columns (focus: the logbook).** At 1366x768 the logbook fills the middle with the odometer above and the map right; at 680x425 the map is a tab. The child types digits from the ones column left. When a column passes 9, a carry chip appears and the odometer's matching wheel rolls past 9 and nudges the next wheel. 386 + 457 = 843. Each column box turns green or shows a small "look again" as soon as its digit is typed; a column missed twice opens the sibling's line for that column only, and the day's sum is then followed by one extra sum of the same kind.

**Miles left.** "Our goal is 2,000 miles. How many are left?" The child subtracts 843 from 2,000 in columns; borrowing across zeros rolls the odometer wheels backward one at a time. 1,157 left.

**Check.** The estimate and answer sit side by side. If they are far apart, the map dot lands in the wrong town and the logbook asks the child to look again.

**Day five (the aha).** After 512, 298 and 347, the logbook says 2,000, the odometer reads 50,629 after rolling past 49,999, and the dot is home. Narrator: "Three ways to count the same trip, and they all agree."

**Trip ledger (after day five; on the main path).** The family adds up the trip's costs and distances on one ledger page of twelve problems, typed column by column from the right with no odometer and no carry chips unless the child asks for them. A line shows "Your time" for each problem and the best so far; there is no countdown and no penalty. A wrong column is marked when the whole answer is checked, and that problem comes back at the end with new numbers. The ledger is done when twelve are right.

**The end.** The full logbook and the ledger. `Print` prints them.

**My route (extra).** The child types five day lengths and a goal and logs the trip.

## Content
- Five days (386, 457, 512, 298, 347 miles) on a made-up route labeled so, a 2,000-mile goal, the odometer, all readable with `Read`.
- The odometer shows six digits.
- The sibling's model: 268 + 175 = 443.
- Trip ledger, sums: 1,468 + 2,375 = 3,843; 4,096 + 978 = 5,074; 27,845 + 6,389 = 34,234; 50,629 + 18,476 = 69,105; 136,507 + 48,695 = 185,202; 309,999 + 1 = 310,000. Differences: 3,402 - 1,675 = 1,727; 5,000 - 2,468 = 2,532; 34,234 - 6,389 = 27,845; 70,003 - 28,476 = 41,527; 185,202 - 48,695 = 136,507; 400,000 - 136,507 = 263,493. Replacement problems keep the digits and regrouping pattern and change the numbers.
- The logbook stays within 10,000; the ledger goes to six digits because the standard names no upper limit.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Digits are typed column by column from the right; a carry or borrow chip can be dragged too.
- Keyboard: Tab to the estimate, each column box, the carry chip and the map; Enter checks.
- With Motion off the odometer wheels jump to the new number.

## Look
- Accent `--brand` #1f6a3a highway green (header, the logbook lines, buttons); gold #f4c542 (the column in use, a carry chip); paper #eef7f1; ink #08200f; muted #4d5c52.
- Contrast (WCAG 2.1, computed): white on brand 6.60:1; brand on paper 6.04:1; ink on paper 15.70:1; muted on paper 6.47:1; ink on gold 10.55:1.
- Never color alone: carry and borrow chips show the digit; the active column has an outline.
- Different from this batch (tomato red, dungeon violet, kitchen-tile blue, soil brown).

## Art
- Local FLUX (`scripts/localart.py`): the dashboard (1, 16:9), the route map (1, 16:9), five day-stop pictures (5, 4:3: a lake, a canyon, a small town, a prairie, home).
- Drawn in code: the odometer wheels, the logbook columns, chips, the map dot.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `big-sister` as the older sibling in the back seat; `easy-coach` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.day + ':' + state.col + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `estimate`: "Tap Estimate and round each day."
- how `column`: "Type the digit for this column."
- how `carry`: "Drag the carry chip to the next column."
- how `left`: "Subtract to find the miles left."
- how `ledger`: "Type each column, starting at the ones."
- event, whole, the sibling's model.
- event, whole, day five.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the column workspace with carry and borrow chips, the odometer, the map dot.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Columns | Type the whole answer; try digits until green | Digits go in one column at a time, right to left. A column has ten digits to guess from, and two misses cost an extra sum. |
| Estimate | Skip it | The column workspace opens after the estimate. |
| Check | Ignore a far-off answer | The map dot lands in the wrong town and the day stays open. |
| Ledger | Guess; rush for a time | No per-column color in the ledger, so there is nothing to probe; a wrong answer brings a new problem, so guessing is slower than working. Time is shown, never scored. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `estimate`.
2. The sibling's model (whole). `column`; `carry`.
3. `left`.
4. Day five (whole), waits. `ledger`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.NBT.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The standard algorithm rests on place value and regrouping | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | National Research Council (2001), "Adding It Up: Helping Children Learn Mathematics" | yes |
| Estimating checks whether an answer is reasonable | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", grades 3 to 5 | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s12, 2026-11-10): 386 + 457 = 843; 2,000 - 843 = 1,157; 386 + 457 + 512 + 298 + 347 = 2,000; rounded days 400 + 500 + 500 + 300 + 300 = 2,000; 48,629 + 2,000 = 50,629; contrast as in Look.
Checks run again for the spec fix (Python, scratchpad s/fx, 2026-11-10): 268 + 175 = 443; all twelve ledger answers as listed; the five nightly miles-left values are 1,614, 1,157, 645, 347 and 0.

## Done when
1. Focus and fold: at 1366x768 logbook, odometer and map; at 680x425 map as a tab.
2. Five days are added in columns with regrouping shown on the odometer. (4.NBT.4)
3. Miles left are found by subtracting, including across zeros. (4.NBT.4)
4. Every answer is checked against an estimate. (4.NBT.4)
5. Twelve ledger problems of four to six digits are right, with no odometer, and the child's own time is shown without a countdown. (4.NBT.4, fluently)
6. The sibling's worked sum plays first and can be reopened; each trip column gives right-or-wrong at once.
7. `Read` reads every card; every control is 48 px or more.
8. The route is labeled made up.
9. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
10. Motion off: odometer jumps; no network requests.

## Open questions
None.
