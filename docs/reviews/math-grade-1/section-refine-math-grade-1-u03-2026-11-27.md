# Section refine: math-grade-1 unit 3 (2026-11-27)

Plans: docs/courses/math-grade-1/u03-1.md to u03-6.md. I checked them against:

- section-write.md, UNIT-PLAN.md, DEFAULTS.md, APPROACH-MATH.md and s03.md
- the skeletons rebuilt by `section_skeleton.py math-grade-1 u3`, which I did not edit
- the prep notes in build/sections/prep/math-grade-1/u03-1.md to u03-6.md

For rule 4, I read units 1, 2 and 4, kindergarten, and the ledger below math-grade-1. The same session ran the unit 3 answer-key read (answer-key-math-grade-1-u03-2026-11-27.md). Its data fixes are the source for the field 3 lines here.

## Faults

| File | Fault | Fix or rejected | Stage |
|---|---|---|---|
| u03-1 | The E41 and E44 quotes differed from the printed stems ("in both pictures", "tell you"). | Both now quote the item stems. | write |
| u03-1 | E42's cards repeated the drawing, so a shape match found the answer without the swap. | The cards show the loose buttons first and then the bag. The stem is "this picture", as printed. | write |
| u03-1 | E43's quote included the teacher direction "Show a pair of pockets with dots." | The direction is outside the quote. The bullet and paper stem quote the item. | write |
| u03-2 | The E46a quote was "just one of the equal groups". | Now "one equal group". | write |
| u03-2 | E47 gave "a sleeve holding ten" with 17 squares to pack, which would make 27. | Now an empty sleeve with ten spaces. | write |
| u03-2 | The teacher read E48's total before the stem, and the stem asked "how many more". | The stem carries the total: "The box holds 13 beads. How many are in the pocket?" | write |
| u03-3 | The E50 quote was "the new label". | Now "the new packet label". | write |
| u03-3 | E52a used 16 − 3 = 13, unit 2 day 36's taught case (rule 4). | Nineteen flags, five cups and a shelf: 19 − 6 = 13. The B wrong is still four. | write |
| u03-4 | The E54 and E55 quotes differed from the printed stems. | Both now quote the item stems. | write |
| u03-5 | E61 asked for two boxes in one stem and carried two wrongs. | Split into E61 (9, F) and E61-left (0, G). Each has its own bullet, Shape line and paper stem. The day 61 exit line names both. | write |
| u03-5 | The E62 quote used number words where the stem prints numerals. | Now "How can this ten show what stays when 7 come off 14?" | write |
| u03-6 | The E65b and E66b quotes differed. E66b asked children to "show the score", but the item asks them to fix the label. | Both now quote the item stems. E66b says the flap is also labeled twelve. | write |
| u03-6 | S64b's 19 − 5 and 19 − 6 used unit 2 day 35's family (19 − 14 = 5) (rule 4). | 13 − 6 = 7 for 13 − 7 = 6, with wrong H copying 7. | write |
| u03-6 | S67b's 19 − 16 used unit 2 day 20's removal (19 − 3 = 16) (rule 4). | 17 − 10 − 1 = 6, with wrong G running four short. | write |
| u03-5, u03-6 openers | "Gap" appeared in the teacher mathematics paragraph. | Changed to "difference". | write |
| ledger | The E52a, S64, S67b and E61 rows had the old numbers or a single item. | See below. | write |
| u03-6 | Possible fault: S67b's new family {6, 11, 17} is the family of E51 (17 − 6 = 11). | Rejected. E51 is an exit in this unit, not a taught case. No teen take away teen with a ten split is free of every earlier family. | write |
| u03-5 | Possible fault: E63's 17 take away 16 and unit 2 day 33's "17 − 1". | Rejected. There it was one side of an equality, not a taught removal. | write |
| u03-6 | Possible fault: S64a's step 13 + 2 and unit 2 day 33's "15 = 13 + 2". S64b's 13 − 6 sits beside S64a's 7 + 6. | Rejected. These are middle steps, not what is asked. | write |
| u03-4 | Possible fault: E54's 8 + 2 and E56's 6 + 4, the day 56 model pair. | Rejected. These are within-ten warm-up pool facts, which the rule allows. | write |
| u03-2, u03-5 | Possible fault: X47, X49 and E61 use ten-and-ones splits. | Rejected. The split is the goal. | write |

**Checked and passing.**

- Every day sums to 60 minutes, and the hand-back slots fit.
- Each wrong has one error letter.
- One ask per stem, after the split.
- Shape lines are present for every item.
- Goals are in student words and kinds.
- Notation (□, −, the ten-stick) is taught before it is tested.
- The owed codes and items match the skeletons.
- No em dash, no writer TODO marker, and no "gap" with children.
- Words outside fields 3, 4 and 6 range from 660 to 797, under the 1,600 cap.

**Ledger.** The changes were made one call each, with the day left blank:

- `note` on "E52a and E52b two take away flag panels": "Not used. Replaced by ..."
- `add` u03-3 case "E52a nineteen flags and E52b flag panels"
- `note` on "S64 adjusted facts and subtraction count-up": "Not used. Replaced by ..."
- `add` u03-6 case "S64 adjusted facts with 13 - 6"
- `note` on "S67b independently split a teen removal": "Not used. Replaced by ..."
- `add` u03-6 case "S67b split 17 take away 11"
- `note` on "E61 folded first move", which now names both items

**Gates.**

- `unitplan.py check math-grade-1` passes u03-1 to u03-6. s03.md fails as before (see plan points).
- `ledger.py check math`: 7,448 rows, 0 problems, 0 planned-only findings, 0 unmatched citations.
- `gate.py --course math-grade-1`: no new FAIL in unit 3 files. The FAIL-NEW lines are s01 same-stem cards, s01-X6b, u01-1/family.md and s03.md:91. The baseline is commit 7ec11d3d0, and HEAD has since moved to 227ecb75a. build/gates/base-math-grade-1 holds only index-reports, so every failing line of the plan, lesson and unitplan gates shows as FAIL-NEW. The orphans were already failing.
- Lead's rerun of the gate. None of its 15 failing lines comes from this job:
  - The 12 same-stem lines and s01-X6b come from plan.py reading s01 rows in items.csv. My data script rewrote only s03 rows.
  - The two s03.md:91 lines come from unitplan.py, which compares days.csv observation codes (1.OA.C.5 on day 63, 1.OA.A.1 on day 65) with the code cells of the s03.md field 5 table. Neither file is in this job's scope.
  - The item rows already carry those codes (s03-X63 and s03-S63 have 1.OA.C.5; s03-X65a and s03-X65b have ~1.OA.A.1).
  - I fixed nothing for them. They stay as plan points.

## Plan points

- **Unit plan, s03.md:91.** unitplan fails on two lines: "observation day 63: no item row names 1.OA.C.5" and "day 65: no item row names 1.OA.A.1". The check reads the code cells of the s03.md field 5 table, not items.csv. So the fix is to name 1.OA.C.5 and 1.OA.A.1 in that table's code cells, or to drop them from the day 63 and 65 observation codes in days.csv. Both files are outside this job.
- **Data stage.** The crefine stage changed the child pieces and the data stage changed items.csv, but the two were not reconciled. Twenty-five pieces printed older numbers. The answer-key job fixed them. A gate that compares printed stems with items.csv would catch this.
- **Next unit numbers.** Unit 4 must also avoid {6, 13, 19}, {6, 7, 13} and {6, 11, 17} as reserved unit 3 checks.

## Changed for the next unit

- When the data stage changes a stem or a number, rebuild the child pieces and the teacher keys in the same job. Then quote the new stem in field 3.
- Unit 2's taught teen cases are used up: 19 − 3 = 16 (day 20), 19 − 14 = 5 (day 35) and 16 − 3 = 13 (day 36). Unit 3 now uses {6, 13, 19}, {6, 7, 13} and {6, 11, 17}. Check new numbers against all of these.
- A stem with two answer boxes is two items. Give each its own id, wrong and Shape line.
- Keep teacher directions such as "Show ..." outside the quoted stem.
- A picture must not give the answer through matching shapes, fill style or printed totals.
- Children and pieces say "difference", never "gap".
