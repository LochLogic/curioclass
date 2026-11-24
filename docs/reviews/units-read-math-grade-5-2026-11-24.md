# Units read: math-grade-5, 2026-11-24

COURSE-RUN stage 4 "Reads": the ten unit plans of Math Grade 5 read together, then fixed.

## What was read

AGENTS.md; docs/COURSE-RUN.md stage 4; docs/agents/EXPERT.md; docs/agents/lenses/math.md; docs/courses/UNIT-PLAN.md
(rules, fields, caps); docs/courses/math-grade-5/scope-and-sequence.md; data/plans/math-grade-5/days.csv (kinds,
codes, goals and notes for every check, respond and evidence day); unit plans s01 to s10 (fields 2 to 7 in full);
the grade 5 rows of data/progressions/math.csv; docs/courses/math-grade-6/s01.md fields 3 and 4 (continuity out).
The frame was used through the scope and sequence and the generated skeleton lines. GLOSSARY.md was not reread
in full; the locked words were checked as they came up.

The brief asked for the last unit plan of grade 4, but its path is under math-grade-4, which the same brief
forbids. It was not opened. Continuity in was checked against the scope and sequence's settled earlier-learning
table and each unit's retrieval rows instead.

docs/reviews/lead-list-lens-pass-2026-11-17.md has no "## math-grade-5 sNN" sections, so no lead items applied.
No days are written for this course (no day skeletons, no courses/math-grade-5 folder), so there are no day faults.

## Verdict

The course reads as one sound arc: volume and expressions, fraction meaning, multiplication and division, then
decimals, conversion, unlike fractions and scaling, and the additional geometry and patterns last. Unit loads
match days.csv exactly by kind, retrieval and return entries point at real days, and grade 6 unit 1 retrieves only
rows this course teaches. The one cross-unit fault was the 5.NBT.B.5 fluency record: four units each made their own
scored multiplication sample with conflicting claims about which record stands, one inside check 2's window and
one on an end day that days.csv does not code for it. Those are fixed; the rest are small item-level repairs.

## Findings

| # | Severity | Unit | Finding | Verdict |
|---|---|---|---|---|
| 1 | Moderate | s08 | Q1, a scored 5.NBT.B.5 item, took six minutes of day 117, whose days.csv codes and goal hold no multiplication; field 5's day line had been rewritten to "multiply with the standard algorithm" to fit it. A writer would build an end day that days.csv does not describe. | Fixed: Q1 row, look-for and evidence mention removed; the day line restored to the days.csv goal; the six minutes go to independent checking; the fluency paragraph says unit 5's A1 and the course checks hold the scored record. |
| 2 | Moderate | s07 | W1 scored 5.NBT.B.5 from the day 103 warm-up, five days before check 2 collects its own untimed algorithm sample on day 108. The scope and sequence allows one collection per window, with a check within ten days reusing it. | Fixed: W1 is feedback-only maintenance; check 2 holds the window's scored sample. |
| 3 | Moderate | s06 | "Retain M1 instead of unit 5's A1" replaced the owning unit's fluency record, while units 8 to 10 treat A1 as standing and day 156 carries "the earlier unit records" into the grade 6 handoff. | Fixed: M1 joins A1 in each child's record and does not replace it. |
| 4 | Minor | s10 | The scored M1 product 1,206 x 34 was already worked as unit 9's day 124 maintenance warm-up, so the answer could be remembered rather than computed. | Fixed: 1,307 x 34 = 5,228 + 39,210 = 44,438; unshifted-row wrong answer 9,149 (L). |
| 5 | Minor | s01 | Item 7's brackets case "add 8 and 7, then multiply by 3" uses the numbers of the standard's own example, which the expression days teach from. | Fixed: add 13 and 4, then multiply by 3; 3 x [13 + 4] = 51; G is 20 from 3 + 13 + 4. |
| 6 | Minor | s07 | The day 96 goal is "choose and explain addition or subtraction", but its exit said "using subtraction", so the choice was given away. | Fixed: the exit asks the student to choose the operation and verify with the other; Goal map row updated to match. |
| 7 | Minor | s07 | Returns said unit 9 "joins fraction and decimal measurement on days 125 and 126"; those days are fraction line plots with no decimals. | Fixed: clause cut. |
| 8 | Minor | s07, days.csv | Decimal-by-decimal division is first taught on day 105, so by the plan's own rule it stays unscored; D1 uses whole-by-decimal and decimal-by-whole cases. No scored record holds a decimal-by-decimal quotient until check 3, and the day 154 note does not require one. | For the structure pass (below). |
| 9 | Minor | s03, s06 to s10 (skeleton) | The generated "Progression skills owned" line lists rows other units own (m5-expressions in s03; m5-multiply-algorithm in s06 to s10), because the skeleton reads the days.csv skills column. A reader could take unit 6 to own the algorithm. | For the structure pass (below); skeleton lines are not edited by hand. |
| 10 | Note | s09, s10 | Unit 9's M1 and unit 10's M1 sit in their end-of-unit tables though days 133 and 148 carry no 5.NBT.B.5 code. Both are collected in warm-ups on days that do carry it (130, 142) and take zero end-day minutes. | No change: consistent with the spaced fluency record once finding 3 is fixed. |
| 11 | Note | s01 | Day 1's Goal map exit is the readiness item, since the last ten minutes of day 1 are the readiness check. | No change: unit 1 rule; the practice shape still differs. |
| 12 | Note | all | Continuity: grade 6 unit 1 retrieves m5-fraction-area, m5-shape-hierarchy, m5-expressions, m5-volume-concepts, m5-volume-formulas and m5-powers-of-ten, all taught and returned to here. The earlier-learning table covers every grade 4 row the units retrieve. | No change. |

All exit and item arithmetic in the units was recomputed during the read (products, quotients, fraction tilings,
rounding); no key errors were found beyond the items changed above.

## For the structure pass

- data/plans/math-grade-5/days.csv, day 154 note: after "20 minutes four short decimal-operation entries", add
  "one of them a decimal divided by a decimal to hundredths". Reason: finding 8.
- scripts/unit_skeleton.py (or the skeleton's owned-rows source): build "Progression skills owned" from the
  frame's ownership, not from every row in the days.csv skills column, and list cited rows owned elsewhere under
  the earlier-units line. Reason: finding 9.

## Day faults

None. No days are written for this course.

## For Cory

Nothing. No scope, audience, money or people question came up.

## Lead-list items worked

0 (no math-grade-5 sections in the lead list). LEAD items: 0; CAP rejections: 0.

## Counts by outcome

Fixed 7; for the structure pass 2; no change 3; day fault 0; for Cory 0.

## Gates

- `python -X utf8 scripts/unitplan.py check math-grade-5`: PASS, all ten plans, within caps.
- `python -X utf8 scripts/sequence.py check math-grade-5`: 0 failures.
- `python -X utf8 scripts/goalmap.py audit math-grade-5`: no FAIL lines.
