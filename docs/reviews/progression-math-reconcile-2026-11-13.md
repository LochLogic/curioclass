# Math progression reconcile, 2026-11-13

The blind math progression (data/progressions/math.csv) compared with the earlier Curio Class planning: the grades 3
to 5 progression and its findings and review, the grade 4 scope and sequence and its review, the grade 4 section
plans and written days (only where they place a standard or a limit), the math rows of data/units.csv,
data/sequence.csv and data/modules.csv, and the IM grade 4 draft map. Settled by the standards text, the
Progressions (compiled 2023; "PDF n (printed m)") and the base text's own course tags (IM 9 to 12 lesson files in
S:\CurioClass-sources\illustrative-math, counted by grep).

## Verdict

43 differences. The old work won 28, every one on a named source (a Progressions page or the standard's own text);
it won none without a source. The new rows won 13 (all high school course placement, settled by the base text's
course tags and the (+) marks), and 2 are order choices the rows do not fix, so both stand. The old work's pull is
real but earned: almost all of its wins are limits, weak handoffs and grade 2 prerequisites that the blind writers
left out, and only four of them correct something a blind row stated wrongly (the standard algorithm wording on two
rows, the ban on angles where two lines cross, and whole-number-only perimeter). No edit moves a standard to
another grade or course. Gate: `scripts/progression.py check math` prints 0 failures.

## Differences

"Old" is the earlier work, "new" the blind row as written. Winner "old" means the row was edited (both ends of
every handoff written).

| # | Row ids | Old | New | Winner | Source |
|---|---|---|---|---|---|
| 1 | m4-mixed-numbers, m3-equivalent-fractions | Mixed numbers rest on whole numbers as fractions, 3.NF.A.3c (finding A1) | Assumed only m3-fractions-number-line | old | Progressions NF PDF 151 (145) |
| 2 | m4-mixed-numbers | Converting a mixed number to a fraction is addition (write 2 + 3/4) | Not said | old | Progressions NF PDF 151 (145) |
| 3 | m4-read-compare-large, m2-three-digit-place-value, m2-compare-three-digit | Base is grade 2 reading, writing, comparing (2.NBT.A.1 to A.4; finding A3), a weak handoff | Assumed m3-add-sub-1000 only | old | Standards text: grade 3 NBT.A has no read, write or compare standard |
| 4 | m4-mult-comparison, m3-two-step-problems | Weak handoff: comparison language is new; base is additive comparison (2.OA.A.1, 3.OA.D.8; finding B3) | Assumed equal groups and one-step problems only | old | 4.OA.A.2 (tell multiplicative from additive comparison); Progressions OA PDF 44 (38) |
| 5 | m4-mult-comparison, m5-expressions | Hands on to 5.OA.A.2 as well as 5.NF.B.5 (finding A7) | Hands on to m5-scaling only | old | 5.OA.A.2 text ("three times as large"); Progressions OA PDF 48 (42) |
| 6 | m4-mult-comparison | Two-step comparison problems, no remainders, inside the comparison unit (scope and sequence unit 10) | No part of 4.OA.A.3 | old | IM grade 4 unit 5 tags 4.OA.A.3; row now carries ~4.OA.A.3 |
| 7 | m4-area-perimeter-formulas | Perimeter may use any grade 4 numbers, including like-denominator fractions | "Whole-number side lengths" for both | old | Progressions GM PDF 112 (106), margin codes 4.NBT.4, 4.NF.3d, 4.OA.4 |
| 8 | m4-area-perimeter-formulas, m3-mult-div-problems | Unknown side is an unknown-factor problem (3.OA.A.4) | Assumed area and perimeter rows only | old | 4.MD.A.3 text ("viewing the area formula as a multiplication equation with an unknown factor") |
| 9 | m4-area-perimeter-formulas | "Apply the formula" is not plugging into a memorized one; length plus width error | Not said | old | Progressions GM PDF 112 (106) and 111 (105) |
| 10 | m4-multiply-multidigit | Grade 4 written methods shorten into the standard algorithm; fluency is grade 5 (finding A9) | "Not the standard algorithm" | old | Progressions NBT PDF 70 to 73 (64 to 67); 5.NBT.B.5 |
| 11 | m4-divide-multidigit | Same for division; fluency grade 6 | "Not the standard algorithm" | old | Progressions NBT PDF 72 (66); 6.NS.B.2 |
| 12 | m4-divide-multidigit | Write 84 = 8 x 10 + 4, not 8 R 4; grade 5 turns the remainder into a fraction; grade 3 has no remainders (weak) | R note only on the multistep row | old | Progressions OA PDF 45 (39), NBT PDF 72 (66) margin, NF PDF 157 (151) |
| 13 | m4-multistep-problems | No more than three steps (finding E4) | No step cap | old | Progressions OA PDF 44 (38) |
| 14 | m3-two-step-problems (and m4-multistep-problems) | Order of operations without parentheses is a grade 3 expectation | Not said | old | Standards footnote to 3.OA.D.8 (official PDF p. 23) |
| 15 | m4-additive-angles | Angles where two lines cross, on a line and around a point are found by adding parts (review finding 1) | "No facts about ... vertical angles" | old | Progressions GM PDF 113 (107), margin; 7.G.B.5 for the rule form |
| 16 | m4-additive-angles, m3-add-sub-1000 | Readiness on 3.NBT.A.2 (360 minus 125) | Assumed nothing | old | 4.MD.C.7 text (addition and subtraction problems) |
| 17 | m4-angle-concepts, m2-halves-thirds-fourths | A fraction of a circle is grade 2, weak handoff (finding D3) | Assumed m3-unit-fractions only | old | 2.G.A.3 text (circles); Progressions NF PDF 146 (140) (grade 3 leans on lengths) |
| 18 | m4-classify-shapes | Triangle sorting by sides is optional, kept out of checks (finding E3) | Taught as part of the row | old | 4.G.A.2 text (right triangles only); Progressions G PDF 132 (126) |
| 19 | m4-tenths-hundredths | Weak handoff: grade 3 gives no tenths or hundredths; base is grade 4 fractions (findings A2, B2) | Assumed m3-equivalent-fractions, no note | old | Grade 3 denominator footnote (2, 3, 4, 6, 8) |
| 20 | m4-round-any-place | Rounding beyond the leftmost one or two places need not be practised (finding E2) | Any place, no caution | old | Progressions NBT PDF 69 (63), margin |
| 21 | m4-equivalent-fractions | Not by "multiplying by 1" as n/n; no simplest form or least common denominator; a denominator met in working may be off the list | Cutting explanation only | old | Progressions NF PDF 150 (144) |
| 22 | m4-fraction-add-sub | Unit-fraction language ("two thirds", not "two over three") | Not said | old | Progressions NF PDF 140 (134) |
| 23 | m4-fraction-add-sub | Include a different-wholes problem; the tenths plus hundredths exception | Not said | old | Progressions NF PDF 153 (147); footnote to 4.NF.C.5 |
| 24 | m4-factors-multiples | No GCF, LCM or prime factorization; need not be fluent in all pairs | Limits 1 to 100 only | old | 6.NS.B.4; Progressions OA PDF 45 (39) |
| 25 | m4-patterns | The rule is given; no inferring the rule; no ordered pairs | "From a given rule" | old | Progressions OA PDF 46 (40) |
| 26 | m4-unit-conversion, m3-time | Conversions build on grade 3 time (finding B4) | Assumed mass and volume, unit size | old | 4.MD.A.1 text (hr, min, sec) |
| 27 | m4-multiply-multidigit | Facts check first; fluency may still be growing (finding D4) | Not said on the grade 4 row | old | Progressions OA PDF 37 (31) |
| 28 | m4-multiply-multidigit | Keep one area picture into grade 5 | Area model handed on, no note | old | Progressions OA PDF 39 (33), NF PDF 143 (137) |
| 29 | m4-measurement-problems | Decimals rule cites the Progressions | Same limit, no pointer | old | Progressions MD PDF 89 (83) |
| 30 | m5-volume-formulas, m4-multiply-multidigit | Volume builds on multi-digit multiplication (finding B9) | Assumed area formulas only | old | 5.MD.C.5b (V = l x w x h with whole numbers) |
| 31 | m5-decimal-operations, m4-multiply-multidigit, m4-divide-multidigit | Grade 5 decimal operations need multi-digit multiplication and division (finding B12) | Assumed adding and decimals only | old | 5.NBT.B.7 text (multiply and divide decimals) |
| 32 | alg2-polynomial-arithmetic (A-APR.A.1) | Algebra I (modules.csv) | Algebra II | new | IM tags: Algebra II 9 lessons, Algebra I 0 |
| 33 | alg2-rational-exponents (N-RN.A.1) | Algebra I | Algebra II | new | IM tags: Algebra II 17, Algebra I 0 |
| 34 | alg2-rational-exponents (N-RN.A.2) | Algebra I | Algebra II | new | IM tags: Algebra II 15, Algebra I 0 |
| 35 | alg2-sequences (F-BF.A.2) | Algebra I and II | Algebra II | new | IM tags: Algebra II 21, Algebra I 0 |
| 36 | alg2-sequences (F-IF.A.3) | Algebra I and II | Algebra II | new | IM tags: Algebra II 11, Algebra I 0 |
| 37 | alg2-normal-distributions (S-ID.A.4) | Algebra I and II | Algebra II | new | IM tags: Algebra II 13, Algebra I 0 |
| 38 | alg2-logarithms (F-LE.A.4) | Algebra I and II | Algebra II | new | IM tags: Algebra II 23, Algebra I 0 |
| 39 | alg2-radical-equations (A-REI.A.2) | Algebra I and II | Algebra II | new | IM tags: Algebra II 13, Algebra I 0 |
| 40 | alg2-geometric-series (A-SSE.B.4) | Algebra I and II | Algebra II | new | IM tags: Algebra II 9, Algebra I 0 |
| 41 | alg1-quadratic-forms-graphs (F-IF.C.8), alg1-vertex-form-max-min (F-IF.C.9) | Algebra II and electives | Algebra I | new | IM tags: Algebra I 13 and 5 |
| 42 | geo-slope-criteria-lines, ~alg1-vertex-form-max-min (A-REI.C.7) | Algebra I | Started in Algebra I, owned in Geometry | new | IM tags it in all three courses |
| 43 | 13 codes: A-CED.A.1, A.2, A-REI.A.1, D.11, A-SSE.A.1, A.2, B.3, F-IF.B.4, F-LE.A.2, B.5, N-Q.A.1 to A.3 | Algebra I only | Started (~) in Algebra I, owned where the base text completes them | new | IM tags in more than one course; the row rule that the owner completes the standard (stitch item 22) |
| 44 | 17 (+) codes (A-APR.C.5, D.7; A-REI.C.8, C.9; F-BF.B.5; F-TF.A.3, A.4, B.6, B.7, C.9; G-C.A.4; G-GMD.A.2; G-GPE.A.3; N-CN.A.3, C.8, C.9; S-CP.B.9) | Placed in core course modules | Excluded, reasons in math-excluded.csv | new | (+) marks in the standards; IM names no lesson for them |
| 45 | m4-fraction-times-whole | After adding fractions (scope and sequence unit 6) | Notes IM puts it first (unit 3, lessons 1 to 6) | both stand | 4.NF.B.4a rests on 3.NF.A.1 only; the row fixes no order, either order is sound |
| 46 | m4-unit-conversion, m4-measurement-problems | After division, so the numbers can be real (scope and sequence unit 15) | Cites IM unit 5, before multi-digit work | both stand | Scope and sequence review finding 3: IM's order is not wrong, it limits the numbers; the row fixes no order |

The table has 46 lines because rows 1 and 2, and rows 7 to 9, each split one old item into separate edits; counted
as differences they are 43 (28 old, 13 new, 2 both stand).

Also done, from the stitch (item 20): alg2-rational-exponents now carries `~F-BF.B.4a`, assumes
alg1-inverse-functions (both ends written) and its notes name the one applying day on cube roots undoing cubing.

Agreements checked and left alone (no difference): factors to grade 5 common denominators, line plots after
fraction adding, decimals before place value, lines and rays before angles, the decimals rule for money and
metric problems, the rounding day used to estimate, unit size from grade 2 skipping grade 3, grade 5 patterns
needing only 4.OA.C.5, angles needing grade 3 fractions, every grade 3 to 8 standard in the same grade as
data/modules.csv.

## Rework for old files (when the course is planned)

- data/modules.csv, high school: retag the course modules to match the progression (rows 32 to 44): N-RN.A.1, A.2,
  A-APR.A.1, F-BF.A.2, F-IF.A.3, S-ID.A.4, F-LE.A.4, A-REI.A.2, A-SSE.B.4 to Algebra II only; F-IF.C.8, C.9 to
  Algebra I; the 17 (+) codes out of the core modules (they belong to the electives). data/sequence.csv follows:
  `math-9-rational-exponents-and-real-numbers` and `math-9-polynomial-arithmetic` hold Algebra II content.
- data/modules.csv: grade 12 modules (Precalculus, Statistics, Calculus) are electives outside the core progression
  (data/courses.csv core = n); keep them for elective planning.
- data/modules.csv: non-CCSS tags on math modules (NSPFE "Earning Income" on grade 6, NSPFE "Spending" on grade 5,
  EK-ALG-ML-02 on kindergarten) have no progression row; decide at those course frames whether they stay as
  cross-links.
- docs/courses/math-4-spine.md, limits table, unit 16: add the lines-crossing statement now on m4-additive-angles
  (the progression page already has it).
- docs/courses/math-4-spine.md, unit 6: the base text teaches fraction times whole number before adding; the
  current order stays, the unit plan may note the option.
- The three side notes on data/modules.csv in docs/courses/math-3-5-progression-findings.md are still open.

## For Cory

Nothing. No difference changes which grade or course teaches a standard without a source to settle it, and the
old work's wins all rest on named sources.
