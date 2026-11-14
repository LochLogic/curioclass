# Math progression stitch, 2026-11-13

The four band parts (data/progressions/parts/math-k2, math-35, math-68, math-hs) joined into
data/progressions/math.csv, and the one excluded file (math-hs-excluded.csv, 49 (+) codes) into
data/progressions/math-excluded.csv. Grade 12 has no core math course, so it has no rows.

## What the stitch did

- Rows: 305 (K 20, 1 26, 2 28, 3 24, 4 27, 5 25, 6 26, 7 23, 8 24, 9 28, 10 28, 11 26), grade order, band
  order kept inside a grade. No row's grade, standards or content changed.
- Cross-band handoffs: 151 written, both ends. 2 to 3: 35; 5 to 6: 44; 8 to 9: 30; grade 8 to Geometry
  (grade 10): 20. Longer handoffs, each with its reason in the receiving row's notes: 2 to 4 (money, unit size),
  3 to 6 (scaled graphs), 4 to 6 (factors and multiples), 4 to 7 (angles, 3), 4 to 8 (symmetry to reflections),
  5 to 7 (unlike denominators to signed numbers, shape classification), 6 to 9 (histograms), 7 to 9 (inequalities,
  percent change, one-variable statistics, 5), 7 to 10 (circles, cross sections, probability, 5), 7 to 11 (random
  samples). Grade 8 geometry goes straight to Geometry because Algebra I has no geometry unit. Every grade 3, 6
  and 9 row that builds on earlier skills now assumes one.
- The high school writer's grade 6 to 8 needs (named by standard code) are mapped to the real grade 7 and 8 rows.
- Models: no synonyms; all four bands already used one name each (bar-graph K to 3, dot-plot from grade 2,
  place-value-chart introduced in grade 3). Re-introductions turned into model_in: function-table
  (m6-dependent-variables; m5-two-patterns introduces it) and tape-diagram (m4-mixed-numbers). Where a cross-band
  target uses a model its source row carried but did not hand on, the source now hands it on (22 model_out
  additions, for example m5-decimal-operations hands on base-ten-blocks to grade 6).
- Model gaps the gate notes, with the reason added in the row where the model returns: box-plot, dot-plot and
  histogram skip grade 8 (bivariate statistics only) and grade 10 (no data unit in Geometry); ratio-table and
  tree-diagram skip grades 8 and 9; scatter-plot skips grade 10; tape-diagram skips grade 8.
- Gate: `scripts/progression.py check math` 0 failures; `scripts/plan.py check` clean on the progression line.

## Strands that stop and start

- geometry: K to 8, none in grade 9 (Algebra I), grade 10, none in grade 11.
- functions: grades 8 and 9, none in grade 10, grade 11. algebra and number-quantity: grades 9 and 11 only.
- statistics-probability: probability in grade 7, then grade 10; one-variable statistics in 6, 7, 9, 11 (not 8 or 10).
- counting-cardinality K only, fractions 3 to 5, ratios-proportions 6 and 7: these are domains ending where the
  standards end them, not gaps.

## Writers' "For the lead" items, with picks

"Changes a grade?" means: does the pick move a standard or change what a row teaches.

| # | Band | Item | Pick | Changes a grade? |
|---|------|------|------|------------------|
| 1 | K-2 | Grade 2 major work 68 percent by rows (line is 75 for K to 2) | Count by days at the course frame | No |
| 2 | K-2 | Grade 1 start-unknown and compare-opposite taught, mastered in grade 2 | Keep (Progressions) | No |
| 3 | K-2 | Grade 1 length with same-size units | Keep (1.MD.A.2) | No |
| 4 | K-2 | No hundred chart in K to 2 | Keep; checked: no grade 3 row assumes one | No |
| 5 | K-2 | Some standards split across a ~ row and an owning row, following base-text sections | Keep | No |
| 6 | 3-5 | dot-plot for line plots from grade 3 | One name from grade 2 on (m2-line-plots introduces it) | No |
| 7 | 3-5 | 5.NBT.A.2 placed with IM grade 5 unit 6 | Keep | No |
| 8 | 3-5 | m3-scaled-graphs hands on to grade 6 | Wired to m6-data-displays, reason in notes | No |
| 9 | 3-5 | Grade 4 angles to grade 7, symmetry to grade 8 | Wired (m7-angle-relationships, m7-triangle-conditions, m8-rigid-motions), reasons in notes | No |
| 10 | 3-5 | Trapezoid definition | Settle at the grade 3 to 5 course frames | No |
| 11 | 3-5 | Grade 4 major work 14 of 27 rows | Count by days at the frame | No |
| 12 | 6-8 | Standard three-year path; accelerated path (Algebra I in grade 8) | Keep; decide at the course frame. For Cory (scope) | No |
| 13 | 6-8 | New model name net | Keep | No |
| 14 | 6-8 | Grade 7 major work 13 of 23 rows | Count by days at the frame | No |
| 15 | 6-8 | m8-linear-relationships owns no code, contributes to 8.F.B.4 and 8.F.A.3 | Keep; it now hands on to alg1-linear-equation-graphs | No |
| 16 | 6-8 / 3-5 | function-table introduced in grade 5 or 6 | Grade 5 introduces it (5.OA.B.3); m6-dependent-variables uses it | No |
| 17 | HS | (+) codes excluded with reasons | Merged into math-excluded.csv | No |
| 18 | HS | F-IF.C.7d (+) owned by alg2-rational-functions | Keep (taught in IM Algebra II unit 2) | No (as written) |
| 19 | HS | S-CP.B.8 (+) owned by geo-conditional-independence | Keep (IM Geometry unit 8 uses it) | No (as written) |
| 20 | HS | F-BF.B.4a owned in Algebra I, one applying day for nonlinear inverses in alg2-rational-exponents | Keep the owner. The applying day is not yet on alg2-rational-exponents (neither ~F-BF.B.4a nor a note); add `~F-BF.B.4a` and one sentence to its notes. Not done here: it changes the row | Yes (adds a day to an Algebra II row) |
| 21 | HS | F-TF.A.3, F-TF.A.4 (+) touched but excluded | Keep excluded | No |
| 22 | HS | Algebra I carries many ~ codes Algebra II completes | Count ~ codes when judging balance | No |
| 23 | HS | Grade 9 hands on straight to grade 11 (18 handoffs) | Keep; each row gives the reason | No |
| 24 | HS | New model name construction | Keep | No |
| 25 | HS | Grade 6 to 8 needs named by standard code | Mapped to grade 7 and 8 row ids | No |

## Found at the stitch

- m8-scientific-notation hands on to nothing: the 6 to 8 writer pointed it at N-Q.A.3 (precision), but no high
  school row uses scientific notation as a skill. Left without a handoff.
- geo-constructions, geo-inscribed-circumscribed and geo-addition-rule assume nothing: constructions are new in
  Geometry, and the addition rule builds on the same-grade sample-space row. Left as written.
