# Math unit plans: cold read fixes, 2026-11-24

Fix pass on docs/reviews/units-cold-read-math-2026-11-24.md (0 serious, 4 moderate, 3 minor). Scope: math
kindergarten to grade 8 (not grade 4), Algebra I, Geometry, Algebra II. Algebra II days 1 to 5 are written and were
not edited.

## Findings

| # | Severity | Outcome | What was done |
|---|---|---|---|
| 1 | moderate | fixed | Algebra II days.csv: 116 five-minute openings rewritten as a spaced rotation. Each opening is untimed: two minutes on a course fluency or the Algebra I skill it rests on (polynomial arithmetic, rational rewriting, structural rewriting, transformations, and from unit 6 exponent rules), then three minutes on an earlier strand of this course, rotating so each returns (sequences, polynomial zeros, rational equations, remainders, series, rational exponents, complex numbers, radical equations, logarithms, exponential growth, statistics, trigonometry, sampling). Each strand task is set in a widely applicable prerequisite cluster, so the focus minutes stand. Days tagged with factoring fell from 112 to 34. Unit 7 openings now serve its readiness rows (sampling, spread, association and cause). Day 87 kept its opening. s02 to s07 field 4 retrieval tables, owned and builds-on lines and day lists were regenerated, opening rows were replaced, and each plan states the rotation. The scope and sequence describes it. Prose that named the old drill was fixed (s03, s04 day 79 and day 87, s06 days 113 and 116, s07 balance line). |
| 2 | moderate | fixed, 1 logged | `~` marks in days.csv: grade 3 days 54 to 57 (3.OA.D.8); grade 7 days 52 and 55 (7.NS.A.2d, 7.EE.A.2); Algebra I day 124 (F-IF.C.9); Geometry days 41 and 44 (G-SRT.B.5); Algebra II days 15, 17, 25 and 44 (F-IF.B.4), 26 and 37 (A-REI.D.11). Field 2 regenerated with the begun part stated by verb; field 5 items in grade 7 s04, Algebra I s06, Geometry s02 and Algebra II s02 now score the begun part only. Algebra II s01 F-LE.A.2 needs the mark on days 3 to 13, and days 3 to 5 are written, so it is logged in data/plans/defects.csv and not applied. |
| 3 | moderate | checked | Already fixed in scripts/unit_skeleton.py. The regenerated owned line reads right: grade 7 s06 lists its 3 owned rows, grade 2 s06 lists 4 math rows (no ss1-saving), grade 5 s03 lists 2. |
| 4 | moderate | left for the lead | No math ledger exists. Seeding it (`ledger.py seed`) is the lead's stage call, needed before any math stage 5 job. Not seeded here. |
| 5 | minor | fixed | 65 practice shapes rewritten across 35 plans so the practice differs in kind from the exit (act out, build, sort, fix a worked error, measure, play) and the exit is a fresh transfer; no exit was edited. All five named rows are included. A similarity listing over the 1,456 rows fell from 54 rows at 0.5 or above to 3; the 3 left (grade 1 s02 day 23, s07 day 130, grade 2 s05 day 79) differ in kind already. |
| 6 | minor | fixed | Grade 3 day 79 skills add m2-one-step-problems with a retrieval note; s05 field 4 has the row and a retrieval task. Algebra I day 152 skills add m8-function-compare and its opening retrieves it, before the vertex-form work; s07 field 4 prose and table updated. |
| 7 | minor | fixed | Geometry s07 Returns line now names day 159 as the course-level check, with its respond day 160. |

Counts: 5 fixed (one with a logged part), 1 checked, 1 left for the lead.

## Gates

- `python -X utf8 scripts/unitplan.py check`: 0 FAIL.
- `python -X utf8 scripts/sequence.py check <course>`: 0 failures for each of math-kindergarten, math-grade-1,
  math-grade-2, math-grade-3, math-grade-5, math-grade-6, math-grade-7, math-grade-8, algebra-i, geometry, algebra-ii
  (notes only).
- Goal map: `scripts/goalmap.py` has no audit mode; the goal map gate is the unitplan check above (exit-kind and
  practice-shape), which passes.

## Logged

- data/plans/defects.csv: Algebra II u01, F-LE.A.2 begun mark on days 3 to 13 (written days 3 to 5).
