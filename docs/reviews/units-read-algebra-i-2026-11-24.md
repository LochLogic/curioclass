# Units read together: Algebra I, 2026-11-24

COURSE-RUN stage 4 "Reads" for `algebra-i` (math, grade 9). An expert read of all seven unit plans together, followed by fixes in the unit plans. The single-unit reads (2026-11-15/16 loop, 2026-11-22 Goal map pass) were not repeated.

## What was read

AGENTS.md; docs/COURSE-RUN.md stage 4; docs/agents/EXPERT.md; docs/agents/lenses/math.md; docs/courses/UNIT-PLAN.md; docs/GLOSSARY.md (headings and locked words). The course: scope-and-sequence.md in full, frame.md (ownership and Seams as cited by the plans), data/plans/algebra-i/days.csv (all 160 rows), unit plans s01 to s07 (fields 1 to 4, goal maps, field 5 item tables, error registers, response, tools and the U3 to U6 sections where they hand work across units), and the algebra-i ownership rows in data/progressions/math.csv for later owners. Continuity: math-grade-8/s08.md fields 1 and 3 (the grade below), geometry/s01.md fields 3 and 4 (the next course's unit 1). No day skeletons or written day files exist for algebra-i, so no fix is a day fault.

The lead list (docs/reviews/lead-list-lens-pass-2026-11-17.md) has no `## algebra-i sNN` sections (only algebra-ii), so no lead items or cap rejections were worked.

## Verdict

The seven units form a sound arc: statistics, linear reasoning, bivariate data, functions, exponentials, quadratic functions, quadratic equations. Begun codes are handed forward consistently, day loads match days.csv exactly, and the grade 8 and Geometry seams hold. The most serious fault was invisible to single-unit reads: every end-of-unit and mid-unit item in all seven plans named section N.1 as its owner, so section plans would have taken the wrong items. A second hand-back fault had the day 83 readiness check written two different ways, with the unit 4 version testing unit 5 teaching. Both are fixed.

## Findings

| # | Severity | Finding | Verdict |
|---|---|---|---|
| 1 | Serious | Field 5 "Owner" cells: all 98 item rows across s01 to s07 said `section N.1`, though days.csv divides each unit into 5 to 8 sections (s07 even stated "The recorded section remains 7.1"). Stage 5 section plans list "Unit assessment items owned" from this column (as algebra-ii u01-1 does), so a writer would give section N.1 every item and the later sections none. | Fixed. Each owner now names the section that teaches the part, or the section of the day whose retained record is scored. 94 cells changed (s01 3, s02 18, s03 6, s04 11, s05 24, s06 14, s07 18); cells already right stay. The s07 header sentence now says the owners name sections 7.1 to 7.8. Item-level choice, settled by the expert. |
| 2 | Serious | Day 83 readiness hand-back with two different ends. s05 field 4 (the owner) gives two single-change strip items (20 percent growth, 30 percent loss). s04 U3 set a different item for the same ten minutes: an 80-dollar amount rising and then falling 15 percent, which is successive percent change, taught in unit 5 on day 99, not the grade 7 row. | Fixed in s04 U3: the day 83 line now points to the s05 field 4 items and says successive change is day 99 teaching. |
| 3 | Moderate | s06 day 129 item 10 assessed arithmetic and geometric sequences ("L is arithmetic and E geometric"), error O and its retry named geometric sequences, and U6 day 122 said "earlier records supply construction from ... sequences". No Algebra I day teaches sequences: s02 and s05 both hand sequences to Algebra II (unit 1). Students would be scored on something untaught. | Fixed in s06: item 10 asks for linear and exponential rules from two table pairs (same numbers and key); error O, its retry and the day 122 line now say exponential rule and table pairs, and that sequences wait for Algebra II. |
| 4 | Minor | s03 field 3 "comes back" pointer said unit 6 day 114 returns to this unit's work; day 114 compares exponential and polynomial growth and holds no bivariate data. The real returns (days 79 and 80 refit lines, day 104 fits a supplied exponential) were missing. | Fixed in s03 field 3. |
| 5 | Minor | s02 field 3 said unit 4 day 79 rearranges inverse rules; the rearranging day is 78 (day 79 uses the inverse in notation). | Fixed in s02 field 3. |
| 6 | Minor | s06 field 2 lists F-LE.A.2 and s02 lists A-SSE.A.1 without the begun mark (`~`), while s02 and s05 mark F-LE.A.2 begun and s05 and s06 mark A-SSE.A.1 begun, with completion in Algebra II. These lines are generated from the frame and progression data, so the inconsistency sits in shared data, not the plan. | For the structure pass. |
| 7 | Note | Goal verbs, exit kinds and practice shapes read together: no drift found beyond what the Goal map pass settled; every practice shape differs from its exit. Day-by-kind counts in all seven headers match days.csv. Retrieval entries all point at rows already taught (grade 8 or earlier this year); the day 17 readiness hand-back (s01 U3 to s02 field 4) matches item for item. | No change. |
| 8 | Note | Continuity. In: grade 8 unit 8 hands roots and irrational numbers to alg1-center-spread, alg1-rearrange-formulas and the quadratic rows; Algebra I retrieves them on days 10, 26, 131 to 151. Out: Geometry unit 1 retrieves alg1-writing-equations-constraints and alg1-vertex-form and treats Algebra I graph shifts as not covering full plane motions, which matches s04 and s06. | No change. |

## For the structure pass

- data/progressions/math.csv (or the frame ownership feeding the skeleton): mark F-LE.A.2 as begun in algebra-i unit 6 (`~F-LE.A.2`, part: linear and exponential rules from table pairs; sequences and rational inputs to Algebra II), and A-SSE.A.1 as begun in algebra-i unit 2 (`~A-SSE.A.1`, part a, linear), so the generated standards lines in s02 and s06 agree with s05 and the scope and sequence's begun-code table. Then regenerate the skel blocks.
- The generated "Last used" cell for m8-roots in s02 field 4 reads "this course, last day 15", but the only roots retrieval in unit 1 is day 10. The cell comes from the history script; check how it counts day 15.

## For Cory

None. No finding touches scope, audience, money or people.

## Settled by the expert

- Owner sections for all field 5 items (finding 1): the teaching section of the part, or the section of the retained record's day; files s01 to s07.

## Lead-list items worked

None: the lens-pass lead list has no algebra-i sections. Count by outcome: 0 fixed, 0 settled earlier, 0 rejected.

## Gate results

- `python -X utf8 scripts/unitplan.py check algebra-i`: PASS for s01 to s07 (word caps included).
- `python -X utf8 scripts/sequence.py check algebra-i`: 0 failures (six existing notes on first fluency days, unchanged).
- `python -X utf8 scripts/goalmap.py audit algebra-i`: runs; it prints the goal maps for reading and flags nothing.
