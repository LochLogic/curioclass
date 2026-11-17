# Fixes: Precalculus frame, 2026-11-16

Fix pass on docs/reviews/frame-precalculus-2026-11-16.md (11 findings). Files changed: docs/courses/precalculus/frame.md,
the 25 pc- rows of data/progressions/math.csv (24 changed; no other row touched), the CUR-PC lines of
data/standards/curio-math-electives.txt, and the sync outputs.

| Finding | Fix |
|---|---|
| 1 CUR-PC.13 false (serious) | Outcome (now CUR-PC.14), the pc-sequences-series-binomial note and unit 10 say "why an infinite geometric series with any other nonzero ratio has no finite sum"; the row and unit add one partial-sum table of 1 + 1/2 + 1/3 + ... beside 1 + 1/4 + 1/9 + ..., left for Calculus to tell apart. |
| 2 Days | pc-function-analysis load 7 to 5 days (1.5 review), pc-conics 9 to 11. Unit 1 16 days, unit 9 11; total 151 in units unchanged. Calendar, check days (47 to 49, 99 to 101, 158 to 160), readiness days (49, 101, 132) and Cross-subject weeks moved to match. |
| 3 L49 | Focus bullet states the shared answer: owned-outcome account plus a minutes line. Review counted (14.5 days, 725 of 7,550 unit minutes), readiness 30 minutes, openings at most half on earlier courses' rows; cap held at 15 percent of unit minutes. The "no day only reteaches" guard is replaced by "each review day reviews only what that row's new work uses that week". (+) codes stated as required. |
| 4 Uncoded work | New CUR-PC.2 (every zero of a degree 3 or 4 polynomial, factored into linear factors), owned by pc-polynomial-complex-zeros; old 2 to 15 renumbered 3 to 16 in the list, the rows and the frame. CUR-PC.6 now starts with the six functions' values from the unit circle; CUR-PC.7 names the power-reducing formulas (and the valid proof forms). |
| 5 Paper path | The logistic fit on paper added: ln(y / (L - y)) against time on grid paper. |
| 6 Modeling and MP4 | Modeling bullet and unit 4 name the tide task as F-TF.B.7's compact cycle; MP4 added to units 4, 7 and 8. |
| 7 Identity proofs | Row note, outcome and unit 5: a chain of equal expressions, one side or each side rewritten; never the same operation on both sides as if already true. |
| 8 N-VM.B.4a | Unit 6 names why the magnitude of a sum is usually less than the sum of the magnitudes. |
| 9 Source map | Notes for 7.3, 7.4 (unit none), 9.3 (Geometry owns A-REI.C.7), the order reason for chapter 9 and 8.3, and 11.5 and 12.4 written as keep, in part. |
| 10 Consistency | unit-circle used again in 5, 8; Check 2 reuses unit 6's record; the 42 codes split as 37 standards and 5 lettered parts; Calculus table: implicit differentiation reads circles and ellipses, calc-continuity also names pc-informal-limits (its calc- note is left to the Calculus side, For the lead 5). |
| 11 Shared lines | Left to the lead, as asked; For the lead items reduced to one line each. |

Also: every pc- row's re-entry line now follows the count by grade number: a retrieval task where the assumed row was
used in grade 11 or earlier this year, a readiness check only for geo-solving-right-triangles (pc-inverse-trig),
geo-rigid-motion-definitions and geo-dilations (pc-matrix-transformations), alg1-linear-systems (pc-matrix-systems) and
geo-circle-angle-relationships (pc-conics). For the lead 1 now matches the Calculus frame's route: Calculus after
Precalculus by course order through L15 (Cory's call), with Calculus straight after Algebra II and a bridge of about 20
days as the named alternative.

Gates: progression.py check math 382 rows, 0 failures; frame.py check precalculus 0 failures; stale.py check 0
failures; frame.py sync run. Self-check: 25 rows placed once, Owned standards match the rows, 16 CUR-PC codes owned
once, 151 + 9 = 160.

## Unit-level lessons pass (2026-11-16)

frame-write.md lessons 17 to 32 applied to docs/courses/precalculus/frame.md. No unit, skill placement, day total or owned standard changed.

- 17 Day kinds: new **Day kinds.** bullet; Fluency is exact values, identity rewriting, logarithm rules, rational rewriting and polar conversions, about one day in eight (units 3 to 5).
- 18 Readiness evidence: the Seams table's third column now gives each assumed row's treatment and last use (grade, core course, unit, day) from the Algebra I, Geometry and Algebra II days.csv files (one hop counted); every treatment matched the earlier wording. The Readiness bullet says the scope gate's count governs, the count starts from grade 12, and the accelerated path (L15) changes nothing.
- 19 Scored evidence: new **End-of-unit evidence.** bullet: one sitting per unit on its second-last day; unit 6 (14 codes) sits twice inside its days; modeling reports scored only after a draft, written feedback and a revision inside the unit.
- 20 Checks: the intro and all three "What it checks" cells name the units sampled, the two task forms (items, then one extended task, one per day) and the record reused unscored; check 3 no longer says "the whole course".
- 21 Inside the period: the Days bullet names handing out and collecting, ten-minute readiness, and no fold-in of feedback or revision days.
- 22 Safety: not applicable (math leaves days.csv safety empty; no hazardous supplies).
- 23 Facts sourced: each unit's last column names its data with a free source and "as of" date, or "invented for practice"; the standard atmosphere and the tide predictions are labelled as a model and as predictions.
- 24 Depth and devices: an "Out:" line in every unit's What students learn; new **Devices.** bullet (calculator class set, devices in pairs, F-TF.B.7 and CUR-PC.8 met by the calculator, A-REI.C.9 met on a shared device or recorded unfinished).
- 25 Tools, texts and costs: each unit's last column names its tools with their jobs, what Curio Class writes, and a provisional cost for 30; the ceiling is For the lead 6.
- 26 Side standards: **Side standards.** bullet, WHST.11-12.2 practised, not owned.
- 27 Source map: a paragraph saying a section is not a lesson, check days are `ours`, goals are in our words, about 600 words of adapted reading a day.
- 28 Focus method: the Focus bullet states the shared method in the same words as Statistics and Calculus (one 15 percent cap, what counts, no unit share); the plan is at most 1,130 minutes (openings on earlier courses capped at 75). For the lead 7.
- 29 Labels: unchanged, except combinations, now a bridge (S-CP.B.9 stays with Statistics).
- 30 Sensitivity by unit: no flagged unit; unchanged.
- 31 Grade 12 calendar: new bullet: teaching to day 157, check 3 on days 158 to 160, five review folds in order; For the lead 6.
- 32 Core leans only: the Statistics seam and unit 10 no longer rely on Statistics for combinations; unit 10 teaches the count as a bridge.

Gates: frame.py check precalculus 0 failures; progression.py check math 382 rows, 0 failures; stale.py check 0 failures.
