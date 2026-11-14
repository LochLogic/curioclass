# Fixes: math course frames, Algebra I, Geometry and Algebra II, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-<course>-2026-11-14.md`) and the Codex reruns
(`frame-<course>-codex-rerun-2026-11-14.md`) for algebra-i, geometry and algebra-ii to the three frames,
`data/progressions/math.csv` and the Seams table of the grade 8 frame. The older `frame-<course>-codex-2026-11-14.md`
reads were not used. Every expert finding and every "Settled by the expert" row is applied; each Codex finding was
weighed on its merits; the writers' own "For the lead" items were weighed too. F-IF.C.9 and F-LE.A.3 were settled
here, not sent to Cory.

Base-text claims were checked against the source store (S:\CurioClass-sources\illustrative-math, the "Standards by
Lesson" tables and lesson files): F-IF.C.9 is aligned only to Alg1.6.14 and Alg1.7.23 (Alg1.4.9 is aligned to
A-REI.D.11, F-IF.B.4 and F-IF.B.6); F-LE.A.3 to Alg1.5.1, 5.19 and 6.4 ("Comparing Quadratic and Exponential
Functions"); Geo.3.5 to G-CO.C.10 and G-SRT.B.4; Geo.2.13 proves the parallelogram converse; no Geometry lesson is
aligned to S-CP.B.8 (Geo.8.8 to 8.10 work the rule, 8.11 is "Probabilities in Games"); A-CED.A.1 is aligned only to
Alg2.2.20 and 2.21; Alg2.2.10 ("Multiplicity"), 4.15 and 6.17 ("Comparing Transformations") carry the F-IF.C.9
revisits; Alg2.5.5 and 5.6 carry even and odd functions. The national debt prompt's version 1 alone asks a policy
question; version 3 supplies the data.

Focus was recounted by script from those tables (each base lesson by its aligned codes, against the progression's
tagged list N-RN, N-Q, A-SSE, A-APR, A-CED, A-REI, F-IF, G-SRT.B, G-SRT.C): Algebra I 102 of 132 (77 percent,
weighted 65; 81 and 80 with F-BF and F-LE), Geometry 52 of 124 (42, weighted 25; algebra and quantity codes alone 35,
28 percent), Algebra II 73 of 120 (61, weighted 45; 74 and 68 with F-BF and F-LE), series 227 of 376 (60, weighted
45). On the Codex rerun's reading of the publishers' table (adds F-LE.A.1, F-BF.A.1, S-ID.A.2, S-ID.C.7, S-IC.A.1,
G-CO.A.1, G-CO.C.9, G-CO.C.10): 92, 57, 70, series 73 (weighted 76, 34, 50, 54). Each frame now says plainly that the
tagged list is the progression's own, not yet checked against the publishers' criteria, and gives both readings.

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check algebra-i geometry algebra-ii`
0 failures each (7 units, 160 days; 8, 160; 7, 160; 151 in units each); `scripts/progression.py check math` 305 rows,
0 failures; `scripts/stale.py check` 56 files, 0 failures. Unit counts, day counts and ownership unchanged.

## Algebra I

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | F-IF.C.9 taught in full: unit 6 starts it on base lesson 14, unit 7 finishes it on lesson 23 for linear, exponential, quadratic and absolute value functions; unit 4 says lesson 9 only prepares it; "done in full" dropped; Algebra II revisits named (Alg2.2.10, 4.15, 6.17); row alg1-vertex-form-max-min rewritten; For the lead 3 now "settled" |
| Expert | 2 | Applied | F-LE.A.3: unit 5 the linear case (lessons 1 and 19), finished in unit 6 on base lesson 4 with the added power-function activity after it; Source map rows for Alg1.5 and Alg1.6 moved; row alg1-linear-vs-exponential notes changed |
| Expert | 3 | Applied | "The bar, applied by analogy" replaced by "Focus, coherence and rigor": days-based recount per course and series, tagged-list caveat, 72 percent withdrawn |
| Expert | 4 | Applied | National debt prompt kept as version 3 (no policy question, no launch video, debt as a share of national income), its own standards F-BF.A.1, F-LE.A.1, F-LE.A.2, F-LE.B.5; savings-plan prompt a candidate extension on the right standards; For the lead 5 settled; Source map row "keep (version 3)" |
| Expert | 5 | Applied | m8-proportional-compare hands on to alg1-linear-equation-graphs (both rows); Seams row added; grade 8 Seams intro and two cells fixed |
| Expert | 6 | Applied | Unit 2 why: Biology needs it by week 13 (unit 5, weeks 12 to 15); unit 5 why: Biology unit 10, weeks 29 to 31 |
| Expert | 7 | Applied | Unit 7 F-IF.C.8a: zeros, maximum or minimum and line of symmetry; unit 4 F-BF.B.4 and 4a "taught in full for linear functions; nonlinear case Algebra II unit 3" |
| Expert | 8 | For the lead | Course id algebra-i against algebra-1 (below); data/courses.csv not edited; For the lead item 8 added |
| Expert | settled | Applied | All three rows (debt version 3; F-IF.C.9 from 6.14 to 7.23; Biology weeks) |
| Codex | 1 | Applied | Technology bullet and unit 3: each student computes the correlation coefficient on a shared or individual device without an account, checked apart from interpretation |
| Codex | 2 | Applied | As expert 7 (symmetry) |
| Codex | 3 | Applied | As expert 2 |
| Codex | 4 | Applied in part | Recount on days, not rows, per course and series; Codex's per-course reading and its list given beside it; which list and reading apply left to the bar page (For Cory) |
| Codex | 5 | Applied | As expert 1 (lesson 6.14 named) |
| Codex | 6 | Applied | For the lead 1: the uncounted shorter alternative removed; a shorter calendar needs its own counted proposal keeping a respond day after every check |
| Codex | 7 | Applied | Credit line in the BASE-TEXTS.md form |
| Codex | 8 | Applied | Cross-subject Biology rows now give Biology's units and weeks and say "taught first: retrieval" or "concurrent"; ELA 9 row gives ELA 9 unit 6, weeks 20 to 24 |
| Codex | 9 | Applied | Grade 8 Seams intro no longer calls the high school frames unwritten |
| Codex | 10 | Applied in part | Grade 8 Seams scientific notation cell fixed; the same stale claim in the grade 8 frame's For the lead item 6 is outside the allowed edit (For the lead) |
| Codex | 11 | Rejected | The stitch report is not one of this fixer's files (For the lead) |
| Codex | For Cory 1 | Rejected | F-LE.A.3 finishing in unit 6 settled here, as the lead directed |
| Codex | For Cory 2 | For Cory | Accelerated grade 8 path needs a compression plan (already For the lead 4) |
| Writer | lead 1 to 8 | Applied | 1 rewritten (Codex 6); 2 rewritten (recount); 3 and 5 settled; 4 and 7 kept for Cory; 6 kept; 8 new (course id) |

Algebra I: 18 applied (2 in part), 2 rejected, 1 for the lead, 1 for Cory (with For the lead 4 and 7 and the bar).

## Geometry

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Focus recount (42 percent, weighted 25; series 60, weighted 45) and a coherence reading; the expert's "42 percent coherence" counts the similarity and trigonometry clusters, so both figures are given: 28 percent on algebra and quantity codes alone, 42 with G-SRT.B and C; 26 and 52 percent withdrawn |
| Expert | 2 | Applied | Midsegment named in unit 3 (base lesson 5), unit 6 points back to it and names medians at base lesson 16; unit 7 bisector concurrences as review; rows geo-similar-triangle-proofs (~G-CO.C.10) and geo-coordinate-proofs changed |
| Expert | 3 | Applied | "2,000 Calories" siting task kept as a unit 1 candidate extension with no food, calorie or home content; Source map and For the lead 5 reworded |
| Expert | 4 | Applied | Unit 4 and unit 5 reasons give Chemistry's own weeks; Chemistry table rows give Chemistry units and weeks |
| Expert | 5 | Applied | G-CO.C.11 converse (base lesson 13); row geo-parallelogram-proofs notes |
| Expert | 6 | Applied | S-CP.B.8 cited as "lessons 8 to 10, without aligning the code"; assessed in unit 8 only, off the year-end check; extension replaced |
| Expert | 7 | Applied | Construction model: new as a reasoning tool; compass drawing met in IM 7.7 lessons 7 and 10 |
| Expert | settled | Applied | All four rows |
| Codex | 1 | Applied | G-CO.C.11 converse; N-Q.A.1 in full (formulas, scale and origin); S-CP.A.3 both directions; S-CP.B.8 both factorizations, interpreted; rows geo-modeling-objects-density and geo-conditional-independence changed |
| Codex | 2 | Applied | As expert 2 |
| Codex | 3 | Applied | Unit 2 readiness day adds one cylinder-volume item for "How Much Water?" with a reminder |
| Codex | 4 | Applied in part | Row-share figures withdrawn and days-based recount given with Codex's list reading (57 percent); whether focus is judged per course or across the sequence differs between the reads and goes to the bar page (For Cory) |
| Codex | 5 | Applied | As expert 6, with the two-way table and tree game as the extension |
| Codex | 6 | Applied | Credit line in the BASE-TEXTS.md form |
| Codex | 7 | Rejected | Stitch report outside this fixer's files (For the lead) |
| Codex | 8 | Rejected | Same |
| Codex | 9 | Rejected | math-4-spine is outside this fixer's files and under the blind rule (For the lead) |
| Codex | For Cory | Rejected | S-CP.B.8 keep settled by the expert (no day, unit 8 only) |
| Writer | lead 1 to 6 | Applied | 2 rewritten; 3 and 5 settled; 1 and 4 kept; 6 kept for Cory |

Geometry: 15 applied (1 in part), 4 rejected (three of them passed to the lead), 1 for Cory (the bar reading).

## Algebra II

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | F-IF.C.9 revisits inside existing days: unit 2 base lesson 10 (polynomial graph against factored form), unit 4 lesson 15 (exponential table against logarithmic equation), unit 6 lesson 17 (sine graph against equation); one comparison item on the year-end check; rows carry ~F-IF.C.9 |
| Expert | 2 | Applied | Focus recount (61 percent, weighted 45; 74 with F-BF and F-LE); 57 withdrawn |
| Expert | 3 | Applied | A-CED.A.1: unit 2 the rational case, unit 4 the exponential case solved with logarithms (finished there); row alg2-logarithms carries ~A-CED.A.1 |
| Expert | 4 | Applied | Unit 5 even, odd and neither from graphs and equations with f(-x) (base lessons 5 and 6); unit 3 added day adds the (x + 1)/(x - 1) inverse; rows alg1-inverse-functions and alg2-rational-exponents changed |
| Expert | 5 | For the lead | Course id algebra-ii against algebra-2; For the lead item 8 added |
| Expert | settled | Applied | All four rows (F-IF.C.7d assessed in unit 2 only, off the year-end check) |
| Codex | 1 | Applied | As expert 1; for unit 4 the expert's exponential-against-logarithmic comparison on lesson 15 is used, which the lesson already carries |
| Codex | 2 | Applied in part | As Algebra I Codex 4 (84 of 120 on Codex's list given beside the recount) |
| Codex | 3 | Rejected | Conflicts with expert 3: the exponential case is finished in unit 4 where the base text creates and solves exponential equations, with no new unit 2 task |
| Codex | 4 | Applied | Credit line in the BASE-TEXTS.md form (Algebra 2) |
| Codex | 5 | Applied | As expert 4 (f(-x)) |
| Codex | 6 | Applied | Alternative calendar is 152, not 150; "Unit 2 owns 13 codes across seven rows; unit 4 owns ten codes across four rows"; unit 4's "densest" claim corrected |
| Codex | 7 | Rejected | Stitch report outside this fixer's files (For the lead) |
| Codex | For Cory 1 | Rejected | F-IF.C.7d settled by the expert |
| Codex | For Cory 2 | For Cory | Shorter calendar only if one is wanted |
| Writer | lead 1 to 8 | Applied | 1 corrected to 152; 3 settled; 5 rewritten; 7 (F-IF.C.9, A-CED.A.1 settled) and 8 (course id) new; 2, 4 and 6 kept |
| Writer | Physics list | Applied | Physics leans now name m8-roots (Kepler, no rational exponents; Physics unit 3 before this unit 3); Physics unit 6 waves (weeks 16 to 19) taught first; Economics and Government rows give their units and weeks |

Algebra II: 13 applied (1 in part), 3 rejected, 1 for the lead, 1 for Cory.

## Progression changes (data/progressions/math.csv)

| Row | Change |
|---|---|
| alg1-vertex-form-max-min | Notes: F-IF.C.9 across linear, exponential, quadratic and absolute value (Alg1.6.14 starts, 7.23 finishes; 4.9 only prepares); Algebra II revisits named, ownership here |
| alg2-factors-zeros-graphs | Standard + ~F-IF.C.9; notes: Alg2.2.10 comparison |
| alg2-exp-log-graphs | Standard + ~F-IF.C.9; notes: Alg2.4.15 comparison |
| alg2-trig-functions-graphs | Standard + ~F-IF.C.9; notes: Alg2.6.17 finishes the revisits, one item on the year-end check |
| alg1-linear-vs-exponential | Notes: linear case Alg1.5.1 and 5.19; quadratic case Alg1.6.4 finishes F-LE.A.3; power activity after 6.4 |
| alg2-rational-equations | Notes: A-CED.A.1 owned here, rational case; exponential case finished in unit 4 |
| alg2-logarithms | Standard + ~A-CED.A.1; notes |
| alg1-inverse-functions | Notes: both F-BF.B.4a examples taught on Algebra II unit 3's applying day |
| alg2-rational-exponents | Notes: adds the (x + 1)/(x - 1) inverse |
| m8-proportional-compare | hands_on + alg1-linear-equation-graphs |
| alg1-linear-equation-graphs | assumes + m8-proportional-compare; notes |
| geo-similar-triangle-proofs | Standard + ~G-CO.C.10; notes: midsegment in Geo.3.5 |
| geo-coordinate-proofs | Notes: midsegment proved in unit 3, medians Geo.6.16; owns G-CO.C.10 as it completes the last theorem |
| geo-parallelogram-proofs | Notes: converse in lesson 13 |
| geo-modeling-objects-density | Notes: N-Q.A.1 in full (formulas, scale and origin) |
| geo-conditional-independence | Notes: general multiplication rule both ways, independence both directions, lessons 8 to 10 without aligning the code, unit 8 only |

m8-scientific-notation keeps an empty hands_on: no IM Algebra 1 or Geometry lesson uses scientific notation; the
grade 8 Seams cell now says it ends in core math and Chemistry retrieves it.

## Cross-subject notes (other subjects' frames, not edited)

- **ELA 9** (docs/courses/english-language-arts-grade-9/frame.md, line 156): "the biology and Algebra I frames are
  written later" is stale; its S-ID.C.9 row can say Algebra I unit 3 (weeks 10 to 12) is taught first, so unit 6
  (weeks 20 to 24) can cite it.
- **Biology**: weeks agree with the Algebra I table. Its line 181 already says its population lesson comes before
  Algebra I unit 5; it can add that Algebra I base lesson 21 calls back to it.
- **Chemistry** and **Physics**: weeks agree; no change. Algebra II's own list of Physics leans was missing m8-roots
  and is fixed here.
- **Economics** and **US Government**: weeks agree; their own bridges stand.
- **Grade 8 math**: its For the lead item 6 (m8-proportional-compare and N-Q.A.3 "has no row") is now stale; for the
  grade 8 fixer (only the Seams table was editable here).

## For the lead

1. **Course ids.** Folders and data/plans/frames.csv use `algebra-i` and `algebra-ii`; data/courses.csv and the
   frames' first lines use `algebra-1` and `algebra-2`. Pick one id per course before step 3 writes
   data/plans/<course>/ (the courses.csv ids keep data stable: rename the folders and the COURSE_ROWS entries in
   scripts/frame.py), or record the mapping. Not edited here.
2. **Stale stitch notes.** docs/reviews/progression-math-stitch-2026-11-13.md item 20 (nonlinear inverse contribution
   called unapplied) and its note that geo-constructions and geo-addition-rule assume nothing: both done in the
   data (Codex Algebra I 11, Geometry 7 and 8, Algebra II 7).
3. **math-4-spine status sentence** (Codex Geometry 9): not opened (blind rule); for whoever owns that file.
4. **Grade 8 frame For the lead item 6**: stale, see Cross-subject notes.
5. **Focus list.** The tagged list in the progression has not been checked against the publishers' Table 1; the
   Codex reruns say they read it (adding F-LE.A.1, F-BF.A.1, S-ID.A.2, S-ID.C.7, S-IC.A.1, G-CO.A.1, G-CO.C.9,
   G-CO.C.10) and that focus is judged per course. Confirm against the source when docs/RUBRIC-MATH-HS.md is
   written; add the later.csv row for that file.

## For Cory

- A high school bar page (docs/RUBRIC-MATH-HS.md), and with it which focus reading applies: per course (Codex) or
  across the sequence (expert). Recounted figures are in each frame.
- The accelerated path (Algebra I in grade 8) needs a compression plan before it opens.
- A two-year Algebra I as a separate course.
- A shorter calendar, only if wanted (none is proposed; 160 days stands).

## Settled (for DIGEST.md)

| Choice | Reason | File |
|---|---|---|
| F-IF.C.9 owned by Algebra I, taught in full there (Alg1.6.14 to 7.23), revisited in Algebra II (Alg2.2.10, 4.15, 6.17), one year-end item | The base text's alignments; finishes the standard with no day change | algebra-i and algebra-ii frames; math.csv |
| F-LE.A.3 finished in Algebra I unit 6 on base lesson 4, power activity after it | Quadratics are taught in unit 6 | algebra-i frame; math.csv |
| National debt prompt kept as version 3, no policy question | Only version 1's last question raised the values issue | algebra-i frame |
| A-CED.A.1: rational case unit 2, exponential case finished unit 4 | Where the base text creates each kind of equation | algebra-ii frame; math.csv |
| Midsegment in Geometry unit 3 (Geo.3.5), medians in unit 6 | Where the base text proves them | geometry frame; math.csv |
| S-CP.B.8 kept in full, unit 8 only; F-IF.C.7d kept, unit 2 only | No extra day; (+) codes off the year-end checks | geometry and algebra-ii frames |
| Focus reported on teaching days, per course and series, tagged list flagged as unchecked | Row shares did not measure time | all three frames |
| Credit lines in the BASE-TEXTS.md form | One source policy | all three frames |
