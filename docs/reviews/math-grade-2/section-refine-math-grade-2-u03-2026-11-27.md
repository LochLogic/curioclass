# Section refine: math-grade-2 unit 3 (sections 3.1 to 3.4), 2026-11-27

Fresh reader. I read u03-1.md to u03-4.md whole, s03.md, the u03-1 skeleton, the u03-2 prep notes where a line needed
them, the handbacks rows for days 39 to 57 and the ledger filtered by term and kind. The answer-key read of the same
unit ran first in this session
([answer-key-math-grade-2-u03-2026-11-27.md](answer-key-math-grade-2-u03-2026-11-27.md)). Its fixes are reconciled
here.

Checked and holding:

- Every exit, key, worked case and listed wrong is solved, with one letter per wrong.
- Minutes add to 60 on all 19 days.
- Turn counts hold: six are heard a day at 45 seconds each plus 30 seconds for notes, rotating through positions 1 to
  30, and the T conferences and the day 57 stories fit their parts.
- All 30 children get a hand-back each day.
- Each day's goal is in student words with its kind, and every exit has a Shape line.
- Owed items are given in 3.4: T, E, E2, P, C, D, L, SD, S1 to S13 and the F rows.
- Terms are taught before they are tested: centimeter on day 40, inch and foot on days 46 and 47, meter on day 43,
  difference on day 44 and line plot on day 52.
- Field 2 hand-offs use item ids.
- Assessment cues in field 3 copy items.csv word for word (checked by script).
- `unitplan.py check` passes all four plans under the cap.

## Faults

| File | Fault | Fix or rejected | Stage |
|---|---|---|---|
| u03-1.md field 3, X39 | Key rested on "Mika has only wide tiles", which was not in the line or on the page. | Line and page now say it (key read, ambiguous). | unit plan |
| u03-1.md field 3, X40 | 16 cm window, 11 cm out echoed grade 1's reserved 11 and 16 strips. | 20 cm window, 7 cm out, A 20 units, C 8 cm (key read, rule4). Ledger note updated. | write |
| u03-2.md field 3, X45 | One item held two asks (estimate and joined length). | Two cues, s03-X45-estimate then s03-X45, each keyed with its own letters (key read, two-asks). | unit plan |
| u03-2.md field 4 and day 46 | After the split, A and C first appear on day 45 for the estimate, and no repair named it. | A and C rows name day 46 Repair for s03-X45-estimate. Day 46 Repair returns it privately on a parallel card during either round. | write |
| u03-2.md field 8 | Exits 44, 49 and 50 print "Equation", but the section named no review of it. | Recall line adds "equation" and reads the Equation box as the same word. Ledger row added. | write |
| u03-2.md field 11 | Unit 2 reserved cases named by nickname ("page totals, printer removals, stamp path and star tray"). | Points to the Unit 1 and Unit 2 cases listed by id in section 3.1. | write |
| u03-3.md field 3, X51 | Same double ask. | Two cues, s03-X51-estimate then s03-X51 (key read, two-asks). | unit plan |
| u03-3.md field 4 and day 52 | No A row, which X51-estimate's A wrong answer now needs. C did not name the estimate repair. | A row added (day 51, close seams, day 52 Measure and repair). C row and day 52 name s03-X51-estimate. | write |
| u03-4.md field 3, X54, S8, SD | Keys gave the value before the equation. | Equation first: 76 − 71 = □ or 71 + □ = 76; □ + □ = 94 with one pair; 81 − 69 = □ or 69 + □ = 81. | write |
| u03-4.md day 54 | "Hear six" did not name positions. | "Hear positions 1 to 6." | write |
| u03-4.md days 55 and 57 | E and E2 keys count spans of a checked reference that the plan never set out. | Day 55 Directions and day 57 Estimate rechecks set out the checked strip for each unit. Station and recheck pieces changed in the key read. | prep |
| u03-2.md field 3, X44 | Gap ticks print too tight to count (32 lines in 37 px), so C may never show. | Rejected as a plan fault: the key holds and the line is right. Noted as a plan point for the piece. | prep |
| u03-4.md field 3, C | Forecast boxes are unscored. | Rejected: the unit plan sets C as an explanation item. The forecast is the setup. | unit plan |

Ledger (`ledger.py show math --course math-grade-2 --term ...`): case, model, routine and term rows are present and
match the plans. Fixed: the "X40 pull tab and window" note now gives 27 cm and 20 cm and retires the 16 cm window.
Added a term row: equation (u03-2, "review of math-grade-2 u02-1 [equation], planned only"). The X45 and X51 case
numbers did not change with the split. `ledger.py check math`: 8618 rows, 0 problems.

Swept rules:

- No method question uses "that one".
- Equation keys now give the equation first (the faults above were the exceptions).
- Reserved-case notes match their numbers after the X40 change.
- "Number sentence" does not appear in unit 3.
- Grade 1 cases are in plain words.
- Field 2 uses item ids, and earlier retries are named by id.
- No unit 3 exit, check, contrast or warm-up uses Unit 1's s01-S7 square tiles, s01-S8 shape box of 19, or a Unit 2
  reserved case.
- No plan tells the teacher to fix a printed piece by hand.
- Every number a key rests on is on the child's page or is the child's own measure.

Gates:

- `unitplan.py check math-grade-2` passes u03-1 to u03-4. The one FAIL is s04.md, in the baseline.
- `ledger.py check math`: 0 problems.
- `gate.py --course math-grade-2`: 0 failing findings against the baseline (435 lines), plus 9 new note lines for the
  changed pieces.
- No em dash and no TODO(writer).

## Plan points

- s03.md's goal map makes the day 45 and day 51 exits one item with an estimate box. The unit plan should list
  estimate and measure as two items (2.MD.A.3, then the measure code), as items.csv now does.
- s03.md's day 39 goal should state the "only wide tiles" limit that the key needs.
- s03.md's S prompts differ from section 3.4's fresh versions. Section 3.4 says why, but the unit plan should take
  the items.csv cases.
- The exit-44 gap ticks should print at a countable spacing in the next pieces build, or C should be dropped from
  X44's wrongs.

## Changed for the next unit

- An exit with an estimate box is two items: the estimate first, then the measure. Each has its own wrongs and handbacks
  rows, and the goal map lists both.
- Keys and every key piece give the equation first, then the value.
- A page states every limit its key relies on (X39 "Mika has only wide tiles").
- A picture drawn beside an estimate is to scale, so it does not pull toward a listed wrong answer.
- Every estimate station and recheck sets out the checked reference whose spans the key counts.
- Name earlier units' reserved cases by item id, never by nickname.
- A word printed on a child page ("Equation") needs a review row in the ledger and a field 8 mention where it first
  prints.
- Used up: grade 1's reserved 11 and 16 strips, and unit 3's reserved cases (X39 to X54 with X45-estimate and
  X51-estimate, T, E and E2 in all four units, P, C, D, L, SD, S1 to S13, and the F, D and L story rows), including
  X40's 27 cm tab and 20 cm window and its retired 16 and 15 cm windows. Later units keep off them.
