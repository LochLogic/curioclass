# Fix report: math-grade-1 s02 (2026-11-17)

Findings merged: 13 (assessment 7, sources 3, sequence 3; the two hook findings are different faults, so both kept). Fixed: 13. Rejected: 0. Held up: assessment 7 of 7, sources 3 of 3, sequence 3 of 3.

Item-level choices I made:
- Assessment 1, register D: used "12 - 5 = 17 with right 7" instead of the suggested "10 - 4" (10, 4, 6 repeats the day 23 exit split 6 + 4).
- Assessment 2, day 30: used "eighteen leaves and ten flowers" (difference 8, 10 + 8 = 18, 18 - 10 = 8) because fourteen/nine, thirteen/nine, fifteen/nine, sixteen/nine and seventeen/nine each repeat another exit or retained triple.
- Assessment 3, day 24: second part added; the exit stays at two parts.
- Assessment 5: 1.OA.D.7 removed from the Standard cell on days 20 and 25 only.
- Sources 3: Lotería confirmed in the local lesson 19 source; sources 1: library warm-up confirmed in lesson 1.

Gate: unitplan.py check math-grade-1: PASS for s02.md.

REJECTED: none

LEAD:
- days.csv still lists 1.OA.D.7 for days 20 and 25; the plan's exit cells no longer claim it. Lead may drop the code from days.csv if it should match.
