# Fixes: math progression after the two cold reads (2026-11-13)

Applies `progression-math-2026-11-13.md` (expert, 7 findings) and `progression-math-codex-2026-11-13.md` (Codex, 12 findings) to `data/progressions/math.csv` and `data/progressions/math-excluded.csv`, keeping every decision of the reconcile and stitch reports except one named below. No row was added, removed or moved to another grade, and no K to 8 code changed grade. One high school code changed course: the parent F-IF.C.8 is now owned in Algebra II (alg2-exponential-growth-rational-inputs) and started (~) in Algebra I (alg1-quadratic-forms-graphs), because its exponential part F-IF.C.8b is completed in Algebra II and IM tags the parent in Alg2.5 lesson 6 and part b in Alg2.4 lesson 6; the quadratic part F-IF.C.8a stays owned in Algebra I. This refines reconcile item 41 (which placed the whole of F-IF.C.8 in Algebra I) on the reconcile's own rule that the owner completes the standard. Codex F02 (move F-LE.A.3 to Algebra II) was settled the other way: IM tags F-LE.A.3 only in Algebra I (Alg1.5 lessons 1 and 19, Alg1.6 lesson 4; no Algebra II lesson), and the Functions Progression (PDF 253, printed 247) treats the comparison inside the Algebra I linear and exponential work, so the owner stays in Algebra I and the standard's "more generally as a polynomial" case is written into that row.

Gate after the fixes: `scripts/progression.py check math` 305 rows, 0 failures (it failed 4 before, on F-BF.A.1c, F-BF.B.4b, F-BF.B.4c, F-BF.B.4d); `scripts/plan.py check` exit 0. Rows by grade (unchanged): K 20, 1 26, 2 28, 3 24, 4 27, 5 25, 6 26, 7 23, 8 24, 9 28, 10 28, 11 26. math-excluded.csv went from 49 to 53 codes. 108 rows were touched in all, 35 of them only by the re-entry pass. Skip edges went from 67 to 86, because the new prerequisite links (expert 2 to 4) add 19 long handoffs; each has its reason in the notes. Model gaps are unchanged (7 models, 9 grade runs), each now with a reactivation sentence.

## One line per finding

| Report | # | What was done | Rows touched |
|---|---|---|---|
| Expert | 1 | F-BF.A.1c, F-BF.B.4b, F-BF.B.4c, F-BF.B.4d added to math-excluded.csv with the expert's IM-check reasons (reason opening worded as below). Row notes now name the excluded parts instead of calling them excluded in general. | alg1-inverse-functions, alg2-transformations-functions, alg2-combining-functions-models |
| Expert | 2 | The 14 prerequisite links added, both ends written, each with a sentence naming what the earlier row gives; geo-slope-criteria-lines assumes alg1-vertex-form-max-min. Every grade 9 sender of a new grade 11 link carries "Skips grade 10 on purpose". alg2-polynomial-arithmetic: see Codex 9. | alg2-logarithms, alg2-number-e-continuous, alg2-exp-log-graphs, alg2-polynomial-identities, alg2-polynomial-division-remainder, alg2-polynomial-arithmetic, alg2-complex-numbers, alg2-geometric-series, alg2-periodic-modeling, alg2-experiments-significance, alg2-combining-functions-models, alg2-transformations-functions, alg2-rational-functions, geo-slope-criteria-lines, alg1-exponential-functions, alg1-percent-change-interest, alg1-graph-features-rates, alg1-factoring, alg1-quadratic-forms-graphs, alg1-rational-irrational, alg1-quadratic-equations-reasoning, geo-right-triangle-trig, alg1-center-spread, alg1-quadratic-patterns, alg1-piecewise-absolute-value, alg1-writing-equations-constraints, alg1-vertex-form-max-min |
| Expert | 3 | geo-constructions assumes m7-triangle-conditions (skip of grades 8 and 9: no construction standard there, written in both rows); geo-addition-rule assumes alg1-two-way-tables. | geo-constructions, m7-triangle-conditions, geo-addition-rule, alg1-two-way-tables |
| Expert | 4 | m5-volume-additive to m7-area-volume-composite and m5-fraction-add-sub-problems to m7-rational-problems (grade 6 skip reasons in both rows); m6-four-quadrants to m8-coordinate-distance (grade 7 has no coordinate distance standard); m1-measure-length-units to m2-number-line. Judgment link: m7-chance-probability added beside m7-probability-models on m8-two-way-tables. | m5-volume-additive, m7-area-volume-composite, m5-fraction-add-sub-problems, m7-rational-problems, m6-four-quadrants, m8-coordinate-distance, m1-measure-length-units, m2-number-line, m7-chance-probability, m8-two-way-tables |
| Expert | 5 | US spelling in words cells: center, circumcenter, incenter, end behavior, randomization, randomized; the same fix in two cross_subject reasons (center, organize). | geo-rigid-motion-definitions, geo-dilations, geo-circle-parabola-equations, geo-inscribed-circumscribed, alg2-factors-zeros-graphs, alg2-rational-functions, alg2-study-design-randomness, alg2-experiments-significance, alg1-center-spread, m1-data-three-categories |
| Expert | 6 | ela:L.K.5a became ela:ek-word-relationships in both rows. Under the tightened lean rule the two RI.9-10.8 leans now point at the ELA skill ids too: grade 9 at e9-ri-argument-evaluate (the grade 9 contributing row), grade 11 at e10-ri-argument-evaluate (the owner). | mk-sort-count, mk-analyze-shapes, alg1-correlation-causation, alg2-experiments-significance |
| Expert | 7 | "No timer shown. Fluency is kept up with short spaced, mixed practice in later units of the year." added to both rows. | m3-add-sub-1000, m6-decimal-operations |
| Expert | settled | All six accepted as written (see Settled by the expert). | as above |
| Codex | 1 | Fraction equivalence as multiplication by n/n added to m5-scaling, contrasted with the grade 4 partitioning explanation. | m5-scaling |
| Codex | 2 | Owner not moved (IM tags and the Functions Progression, see header). alg1-linear-vs-exponential now completes the general case: tables and graphs of a simple power (x cubed, x to the fourth) against an increasing exponential, no general polynomial study, no proof. alg2-factors-zeros-graphs carries a brief reminder line, not re-owned. | alg1-linear-vs-exponential, alg2-factors-zeros-graphs |
| Codex | 3 | Excluded inputs from the original denominator, removable holes told apart from vertical asymptotes, zeros only in the domain; one contrast example of a hole. | alg2-rational-functions |
| Codex | 4 | Sine and cosine with amplitude, midline and period; tangent with period, zeros, excluded inputs and asymptotes, and no amplitude. | alg2-trig-functions-graphs |
| Codex | 5 | Forms now read one solution (x = a), no solution (a = b with a and b different, such as 3 = 5), infinitely many (a = a), as 8.EE.C.7a says. | m8-linear-equations |
| Codex | 6 | Unit tracking when quantities are multiplied or divided (miles per hour examples) added; the derived-unit conversion limit kept. | m6-unit-conversion |
| Codex | 7 | Exclusions as expert 1. F-IF.C.8 parent moved to Algebra II, ~F-IF.C.8 in Algebra I (see header). The gate change was already made by the caller. | alg1-quadratic-forms-graphs, alg2-exponential-growth-rational-inputs |
| Codex | 8 | m2-line-plots no longer takes number-line (model_in empty, model_out dot-plot) and says its iterated ruler scale prepares the unit 4 number line; m2-count-skip-1000 says number-line skip counts begin only after m2-number-line. | m2-line-plots, m2-count-skip-1000 |
| Codex | 9 | alg2-polynomial-arithmetic assumes alg1-quadratic-forms-graphs in place of geo-volume-formulas (both ends updated), with the open box kept as an application. The three grade 7 probability rows assume m6-percent. | alg2-polynomial-arithmetic, geo-volume-formulas, alg1-quadratic-forms-graphs, m6-percent, m7-chance-probability, m7-probability-models, m7-compound-events |
| Codex | 10 | Lean reason now says historical BCE/CE labels have no year zero; the notes say to label a reference event as zero and not to subtract BCE labels as integers without the calendar convention. | m6-negative-numbers |
| Codex | 11 | Every receiving row of a skip handoff (66 rows, 86 edges) has a "Re-entry" sentence: recall required with a readiness check and a brief reminder when one grade is skipped, revisited (rebuilt briefly, recall not assumed) when two or more are. The two named examples written as Codex gave them. Every model gap has a "Reactivation" sentence on the first row after it: alg1-data-displays (box-plot, dot-plot, histogram), alg2-study-design-randomness (dot-plot), alg2-normal-distributions (histogram), geo-dilations (ratio-table), alg2-combining-functions-models (scatter-plot), alg1-percent-change-interest (tape-diagram), geo-sample-spaces-events (tree-diagram). No time named. | 66 receiving rows, plus the 7 reactivation rows |
| Codex | 12 | The rejected form is now 84 / 8 = 10 R 4, with divisor 8 named. | m4-divide-multidigit |
| Codex | settled | m4 example and m8 form as Codex 12 and 5; m5-scaling as Codex 1; tangent as Codex 4; m4-angle-concepts now revisits the grade 3 right-angle language; m6-dependent-variables now extends the grade 5 function-table. The edge-note count and the core route: see Skipped. | m4-angle-concepts, m6-dependent-variables |
| Both | exclusions | Every reason in math-excluded.csv (53) now opens "(+) standard for advanced courses, deferred to the electives (precalculus, statistics, calculus), which have no progression rows yet." instead of promising the electives teach them. | math-excluded.csv |

## Skipped

- **Codex 2, moving F-LE.A.3 ownership to Algebra II:** settled by the base text's tags and the Functions Progression (header); the general case is completed in the Algebra I row instead.
- **Codex 11 and Codex For Cory, teaching time for re-entry:** time budgets are reserved; re-entry and reactivation are named, not timed.
- **Codex settled, the Algebra I to Algebra II count in parts/math-hs-edges.md (18 to 19):** that file was outside the files this pass could edit. It is now stale in any case (the new links add more).
- **Expert 1 and Codex 7, the gate change:** already made by the caller before this pass.
- **Expert 2, a gate note for unlinked ~CODE rows:** scripts were out of scope. The ~N-Q.A, ~A-SSE.A.1 and ~A-SSE.B.3 contributions stay unlinked as applications, as the expert said.
- **Expert 6, the lean gate rule:** already in the gate.
- **Accelerated path (Algebra I in grade 8), elective course planning and their sources, course grades, which grade a K to 8 code sits in:** reserved.
- **The high school bar (no rubric for grades 9 to 11), raised by both readers:** a docs question outside these files; it belongs to the Algebra I, Geometry and Algebra II course frames.
- **Expert "could not judge": whether F-IF.C.7d and S-CP.B.8 fit their course time:** a course frame and time question, reserved.

## Settled by the expert

- F-BF.A.1c, F-BF.B.4b, F-BF.B.4c, F-BF.B.4d excluded with the expert's IM-check reasons, the opening reworded to "deferred". math-excluded.csv
- The 14 high school links of finding 2 and the two of finding 3, both ends written. math.csv
- The four K to 8 links of finding 4; on m8-two-way-tables m7-chance-probability was added beside m7-probability-models rather than swapped, since 7.SP.C.7b (models from observed frequencies) also feeds 8.SP.A.4. math.csv
- US spelling in the words column: center, circumcenter, incenter, end behavior, randomization, randomized. math.csv
- ela:L.K.5a becomes ela:ek-word-relationships in two kindergarten rows. math.csv
- The timer and spaced-practice sentence on m3-add-sub-1000 and m6-decimal-operations. math.csv
- Where the reports disagreed on alg2-polynomial-arithmetic (expert: keep geo-volume-formulas; Codex: replace it), Codex wins on the standards text: the open box needs only V = l x w x h (5.MD.C.5b), not the G-GMD.A.3 solids of geo-volume-formulas, which now hands on to no row. math.csv
- F-IF.C.8 owner moved to Algebra II with part b (IM Alg2.5 lesson 6, Alg2.4 lesson 6); F-LE.A.3 owner kept in Algebra I (IM tags Algebra I only; Functions Progression PDF 253, printed 247). math.csv
- Re-entry rule: one skipped grade is "recall required" (readiness check, brief reminder on a miss); two or more is "revisited" (rebuilt briefly). math.csv
- Each model gap's reactivation sentence goes on the first row of the returning grade that uses the model. math.csv
- The ELA lean ids chosen: e9-ri-argument-evaluate for grade 9 (the grade 9 contributing row), e10-ri-argument-evaluate for grade 11 (the owner). math.csv

## For Cory

None.
