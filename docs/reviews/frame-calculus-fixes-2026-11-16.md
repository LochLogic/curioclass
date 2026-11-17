# Fixes: calculus frame read, 2026-11-16

What changed for each finding in docs/reviews/frame-calculus-2026-11-16.md. Files touched: docs/courses/calculus/frame.md, the calc- rows of data/progressions/math.csv, and the CUR-CA lines of data/standards/curio-math-electives.txt.

| Finding | Fix |
|---|---|
| 1. The straight route does not fit the days | The frame is designed for Calculus after Precalculus (by course order); the brief says a student reaches it through the parked accelerated path (later.csv L15), Cory's call (For the lead 1). The straight-from-Algebra-II case is kept as a named alternative: a bridge of about 20 lessons, the topics listed, and the named cut that pays for it (unit 9 and calc-power-series, CUR-CA.25, CUR-CA.26, CUR-CA.30). The calc- rows' Precalculus pickups now open as retrieval tasks, with the bridge lesson named for the alternative only. |
| 2. Four Precalculus prerequisites unnamed; one seam misstated | pc-logarithmic-functions (Precalculus unit 3), pc-special-angles-symmetry (unit 4), pc-trig-identities and pc-trig-equations (unit 5) are named in the rows' notes and in the second Seams table. The alg2-exp-log-graphs seam now reads logarithmic graphs and intersections, with the inverse relation from pc-logarithmic-functions. |
| 3. Polar area needs sin squared and cos squared | Added to CUR-CA.17 and calc-integration-techniques (double-angle identity), used in unit 9; Source map splits 8.4 (left out, extension) from 8.5 (keep in part). |
| 4. Outcomes taught in part; clauses dropped | CUR-CA.1 (limit notation), .3 (constant for continuity), .4 (differentiable implies continuous, not the reverse), .10 (products and differences rewritten into 0/0 and infinity over infinity), .17 (sine and cosine squares), .27 (limits of sequences). Base-b exponentials and logarithms placed in calc-chain-rule-inverses for CUR-CA.5. 1 to the infinity stays an extension. |
| 5. Ideas used before taught | Concavity in unit 3 reworded to the sign of the second derivative; sector area named as geo-arcs-sectors-radians retrieval in unit 1; ln x read from slopes first, proved on the first inverse day (expert's order). |
| 6. Fallback contradicts dependencies | Fallback is now units 1 to 5 and 8, with unit 8's core integrals done by unit 5's substitution and unit 6's methods only where an item names them; named as a scope decision for Cory. |
| 7. L49 drops the time question | The Focus bullet applies the shared L49 answer: an owned-outcome account plus a minutes line (review, retrieval, readiness and just-in-time minutes counted and capped, under about 5 percent for a Precalculus class, the bridge shown separately), and the modeling cycle stays whole. |
| 8. Paper path misses four tools | Added printed polar grid paper, parametric curves from a printed t table, intersections by a table and successive approximation (A-REI.D.11), and fitting by logarithms and a line by eye. |
| 9. Orbit lean is a system | Named in one sentence as the same idea applied to two quantities, not a task; Cross-subject and calc-slope-fields-euler say so. |
| 10. Stale Seams sentence | Removed. The second Seams table gives Precalculus unit numbers (re-read against docs/courses/precalculus/frame.md after its fix: unit numbers unchanged), a bridge-size column and the rational-expressions timing (adding rational expressions first used in unit 1, retrieved in unit 6). Models carried: vector-arrow from Precalculus unit 6, polar-grid from unit 8. |
| 11. Modeling cycle leaves out steps | Now assumptions, model, computation, interpretation, validation, revision, report, with our own rubric. |

Also applied: every item in "Settled by the expert" (ln x day order, arc from 0 to r/2, napkin ring, logistic read from the equation, both improper intervals, Euler steps 0.5 then 0.25). Re-entry wording in the calc- rows now says "retrieval task" wherever the count rule makes it retrieval; readiness stays only for geo-solving-right-triangles, geo-volume-formulas, alg1-vertex-form-max-min, geo-modeling-objects-density and geo-cross-sections-solids. "Both semesters' content" kept; the read's For Cory 2 is For the lead 2.

Not done here (For the lead): geo-arcs-sectors-radians in assumes, which needs the Geometry row's hands_on; the shared lines (BASE-TEXTS, courses.csv, RUBRIC-MATH-HS, the Algebra II frame).

## Unit-level lessons pass (2026-11-16)

frame-write.md lessons 17 to 32 applied to docs/courses/calculus/frame.md. No unit, skill placement, day total or owned standard changed.

- 17 Day kinds: new **Day kinds.** bullet; Fluency is real here (rules in unit 2, antiderivatives in unit 5, methods in unit 6), always after the Understanding day.
- 18 Readiness evidence: the first Seams table's third column gives each row's treatment and last use from the core days.csv files; all treatments held. The route bullet now says which route the rows assume (core grade numbers, Precalculus first by course order) and what changes on the accelerated path: six rows become readiness (days 1, 36, 50 and 65) and geo-solving-right-triangles becomes retrieval.
- 19 Scored evidence: new **End-of-unit evidence.** bullet; one sitting per unit; modeling reports in units 3, 4, 7 and 8 scored after a draft, written feedback and a revision inside the unit.
- 20 Checks: the three "What it checks" cells name the units sampled, the two task forms and the record reused unscored; check 3 no longer samples "CUR-CA.1 to CUR-CA.30".
- 21 Inside the period: the Days bullet gives the unit day ranges, collection time, ten-minute readiness and no fold-in of feedback or revision days.
- 22 Safety: not applicable (math).
- 23 Facts sourced: new **Data and facts.** bullet: every data table invented for practice and labelled, half-lives from the National Nuclear Data Center.
- 24 Depth and devices: an "Out:" line in every unit; new **Devices.** bullet (no owned code needs a device; a calculator route for every technology value).
- 25 Tools, texts and costs: each unit's last column names tools and jobs, what Curio Class writes, and a printing cost for 30; ceiling For the lead 6.
- 26 Side standards: WHST.11-12.2 practised, not owned.
- 27 Source map: the lesson 27 paragraph added at its head.
- 28 Focus method: the shared method in the same words as Precalculus and Statistics; the plan recounted the shared way is about 8 percent (was "under about 5", which left out the openings and the Precalculus retrieval tasks); For the lead 7.
- 29 Labels: unchanged.
- 30 Sensitivity by unit: no flagged unit; unchanged.
- 31 Grade 12 calendar: new bullet: teaching to day 157, check 3 on days 158 to 160, the A tight course trim order as the five folds; For the lead 6.
- 32 Core leans only: the route bullet gives a student without Precalculus each row's bridge as a catch-up pack and parallel support; For the lead 8 raises the reliance on an optional course.

Gates: frame.py check calculus 0 failures; progression.py check math 382 rows, 0 failures; stale.py check 0 failures.
