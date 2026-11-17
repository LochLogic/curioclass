# Fix report, math-grade-6 unit 7 (s07), 2026-11-17

Findings merged: 12 (assessment 5, sources 2, sequence 5; no finding was named by two lenses). Fixed: 11 (one with a changed fix, noted below). Rejected: 0. Lead: 1. Held up per lens: assessment 5 of 5, sources 2 of 2, sequence 4 of 5 for the plan (the fifth is a days.csv fix).
Gate: `unitplan.py check math-grade-6` PASS for s07.md (s06.md fails; not mine).

Fixes:
- Assessment 1: P1 vertices C and D moved to y = -3/2. BC is 3.5 metres, edging 19 metres, area 21 square metres; P1b, P1c, their Meets and Does-not-meet samples updated. Edging and area now differ, so error O is detectable.
- Assessment 2: P1b gains a same-side item. The tree is at T(-3, 1) (not the suggested -3.5, which sat on the courtyard wall), gate at (-1, 1); answer 2 metres; wrong 4 metres (Q). Look-fors and samples added; still inside the 15 minutes.
- Assessment 3: E138 is now two parts. (a) packets from 32 and 48 only. (b) factor 40 + 56 completely, 8(5 + 7); wrong 4(10 + 14) (M). The suggested 28 + 42 was not used because the register's error M already uses 28 and 42 (rule 4). Signals case dropped from E138.
- Assessment 4: E124 cut to two pairs (dollars, underwater metres) and the zero in each; temperature pair removed; wrong answer re-pointed to the metres pair (C).
- Assessment 5: Owner column set by teaching section (7.1 to 7.5; two parent rows read "sections 7.1 and 7.2" and "sections 7.1 and 7.4"). Reused-record rows left as they were.
- Sources 1: both progression links named as unofficial mirrors of the Common Core Standards Writing Team drafts; reference-only wording kept.
- Sources 2: rights check now names the CC BY 4.0 notice on the first-edition unit overview already linked.
- Sequence 1: day 136 preview of width times a sum (6 x (3 + 4) beside 18 + 24), named factoring on day 138.
- Sequence 2: day 135 opens with ten model minutes joining and closing vertices on a supplied grid, with vertices unlike P1's.
- Sequence 3 (changed fix): the days.csv note fixes the rebuild at ten minutes, so it stays ten; the day 136 cell now splits it as five model minutes (arrays for 18, prime test for 19) and a student list of multiples of 6 in practice, leaving five model minutes for the first GCF case. Multiples of 6 were not moved to day 137.
- Sequence 4: P1 setting says a blank grid is supplied and students draw and scale both axes themselves.

REJECTED: none

LEAD:
- days.csv day 130 tools and supplies should drop coordinate-plane, array and grid paper (M1 to M7 use none of them); field 8 of s07.md is generated from days.csv and will follow once it is fixed.
