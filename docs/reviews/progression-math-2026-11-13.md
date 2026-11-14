# Expert read: the math progression, K to 11 (2026-11-13)

A cold read of data/progressions/math.csv by the curriculum expert (docs/agents/EXPERT.md, lens
docs/agents/lenses/math.md). Read blind: no course page under docs/courses/ and no earlier review of the math
courses was opened. The reconcile and stitch reports were read last, only to see what they changed.

## What I read

| File | Rows or size | How |
|---|---|---|
| data/progressions/math.csv | 305 rows (K 20, 1 26, 2 28, 3 24, 4 27, 5 25, 6 26, 7 23, 8 24, 9 28, 10 28, 11 26; no grade 12) | Every row's ids, standards, assumes, hands_on, models, words and cross_subject; notes in full for about 45 rows, searched for the rest |
| data/progressions/math-excluded.csv | 49 codes, all (+) | In full |
| data/progressions/parts/math-*-edges.md | 4 files | Searched for model and handoff reasons only |
| data/standards/ccss-math-standards.txt, ccss-math-focus.csv | all codes; K to 8 clusters | Coverage, (+) marks, major work |
| data/progressions/ela.csv, science.csv, social-studies.csv | owners of the codes and ids math leans on | Grade check of every cross_subject entry |
| IM 9 to 12 course "lessons and standards" pages (S:\CurioClass-sources\illustrative-math\hs-*\course\) | tag counts by grep | High school ownership and the (+) codes |
| docs/agents/EXPERT.md, lenses/math.md, RUBRIC-MATH-K8.md (bar), AGENTS.md | | The bar and the rules |
| docs/reviews/progression-ela-, -science-, -social-studies-2026-11-13.md | finding headings | REPEAT tags |
| docs/reviews/progression-math-stitch- and -reconcile-2026-11-13.md | in full, last | What they changed |

`python -X utf8 scripts/plan.py check`: exit 0, "progression math: 305 rows, 0 failure(s)", with 67 skip-grade
notes and 7 model-gap notes. I checked by script that every one of the 67 skips has its reason in the notes of the
sending or receiving row, and that the model gaps are explained where the model returns (box-plot, dot-plot,
histogram, ratio-table, scatter-plot, tape-diagram, tree-diagram). Both hold. The read below is spent on what the
gate cannot see.

## Verdict

The math progression is sound and close to finished: every grade 3 to 8 code sits in its own grade, the limits,
algorithm grades and weak handoffs are written into the notes with page pointers, and the high school ownership
follows the base text's own course tags. The biggest risk is in high school: four (+) lettered parts are neither
taught nor excluded (the gate passes them because their parent is owned), and about a dozen Algebra II and
Geometry rows assume nothing or the wrong thing, so a course writer would not see what Algebra I or grade 7 already
built. The one change that matters most is to write those prerequisite links (finding 2), which is pure row edits.

**Finding count: 7** (2 moderate, 5 minor). Nothing changes what a grade teaches.

## Findings, most serious first

### 1. Four (+) lettered parts are neither named nor excluded, and the gate cannot see it (moderate; firm)

- **LAYER:** progression (the fix) and process (the gate). **REPEAT:** new.
- **Rows:** alg1-inverse-functions (owns F-BF.B.4, F-BF.B.4a), alg2-combining-functions-models (owns F-BF.A.1,
  F-BF.A.1b).
- **What is wrong:** F-BF.A.1c (compose functions), F-BF.B.4b (verify inverses by composition), F-BF.B.4c (read an
  inverse from a graph or table) and F-BF.B.4d (restrict a domain) are (+) parts. No row names them and
  math-excluded.csv does not list them. alg1-inverse-functions' notes say these "are (+) and excluded", but they
  are not. The gate counts a lettered part as covered when its parent is owned (`named = code in owners or
  parent(code) in owners`), so a parent owned by one row hides every unnamed part beneath it. The base text agrees
  they are not taught: the IM Algebra I and II standards pages tag F-BF.B.4 and 4a, and F-BF.A.1, 1a, 1b, but never
  1c or 4b to 4d.
- **Why it matters:** a coverage claim that reads "every standard named or excluded" is false for four codes, and
  the next writer of the electives has no record that they were set aside.
- **Fix (rows for math-excluded.csv):**
  - `F-BF.A.1c,"(+) standard for advanced courses, taught in the electives. IM check: no Algebra I or Algebra II lesson names this code (composition of functions is not taught)."`
  - `F-BF.B.4b,"(+) standard for advanced courses, taught in the electives. Lettered part of a standard owned by alg1-inverse-functions. IM check: Algebra I unit 4 tags F-BF.B.4 and 4a only; verifying inverses by composition is not taught."`
  - `F-BF.B.4c,"(+) standard for advanced courses, taught in the electives. Lettered part of a standard owned by alg1-inverse-functions. IM check: no lesson names this code (reading an inverse from a graph or table is not taught as its own goal)."`
  - `F-BF.B.4d,"(+) standard for advanced courses, taught in the electives. Lettered part of a standard owned by alg1-inverse-functions. IM check: no lesson names this code (restricting a domain to make a function invertible is not taught)."`
- **Process fix (scripts/progression.py, for the lead):** when a parent code is owned and one of its lettered parts
  is neither owned, contributed to nor excluded, print a FAIL (or at least a note). K to 8 has no such case today,
  so the rule costs nothing there.

### 2. High school rows that assume nothing, or miss the row that started their standard (moderate; firm)

- **LAYER:** progression. **REPEAT:** yes (science findings 1 to 3, ELA finding 2: threads with no assumes link).
- **What is wrong:** 25 high school codes are started (~) in an earlier course and owned later, but the owning row
  rarely assumes the starting row; and nine Algebra II and Geometry rows assume nothing at all. Three Algebra I
  rows (alg1-writing-equations-constraints, alg1-quadratic-patterns, alg1-vertex-form-max-min) hand on to no one,
  although a later row finishes their standard. Several owning rows' own notes say "started in Algebra I" or
  "practised in Algebra I factoring" while their assumes cell is empty.
- **Why it matters:** the Algebra II and Geometry course frames are built from these links. An Algebra II writer
  reading alg2-logarithms (assumes nothing) would not plan a readiness check on exponential functions; one reading
  alg2-exp-log-graphs would not know Algebra I already taught reading solutions where two graphs meet.
- **Fix (add to assumes, and the matching id to the other row's hands_on; where the gate then notes a skip of
  grade 10, the sending Algebra I row already carries "Skips grade 10 on purpose", or copy that sentence in):**

| Row (assumes +=) | Add | Why it is the prerequisite |
|---|---|---|
| alg2-logarithms | alg1-exponential-functions | A logarithm is the exponent that solves an exponential equation (the row's own notes) |
| alg2-number-e-continuous | alg1-exponential-functions; alg1-percent-change-interest | e arrives through compounding more often; completes F-LE.B.5 and A-SSE.A.1b started in both |
| alg2-exp-log-graphs | alg1-graph-features-rates; alg1-exponential-functions | alg1-graph-features-rates starts A-REI.D.11, which this row owns; graphs of exponentials first drawn in grade 9 |
| alg2-polynomial-identities | alg1-factoring | Notes say A-SSE.A.2 was "practised in Algebra I factoring"; difference of squares is the base |
| alg2-polynomial-division-remainder | alg1-factoring | Factors and zeros of quadratics are what the Remainder Theorem generalises |
| alg2-polynomial-arithmetic | alg1-quadratic-forms-graphs (keep geo-volume-formulas) | Expanding factored form to standard form is the arithmetic the row extends |
| alg2-complex-numbers | alg1-rational-irrational; alg1-quadratic-equations-reasoning | Extends the number system; "no real solution" is the need the row opens with |
| alg2-geometric-series | alg1-exponential-functions | Repeated multiplication by a ratio |
| alg2-periodic-modeling | geo-right-triangle-trig | Sine and cosine models rest on the ratios of grade 10 |
| alg2-experiments-significance | alg1-center-spread | Differences of means judged against spread |
| alg2-combining-functions-models | alg1-quadratic-patterns | F-BF.A.1 is started there; gives the grade 9 row a handoff |
| alg2-transformations-functions | alg1-piecewise-absolute-value | F-BF.B.3 is started there (shifting absolute value graphs) |
| alg2-rational-functions | alg1-writing-equations-constraints | A-CED.A.2 is started there; gives the grade 9 row a handoff |
| geo-slope-criteria-lines | alg1-vertex-form-max-min | A-REI.C.7 is started there (line and parabola); gives the grade 9 row a handoff |

- Leave unlinked (applications, not prerequisites): the ~N-Q.A, ~A-SSE.A.1 and ~A-SSE.B.3 contributions from
  Geometry and Algebra I rows to their later owners. Each owner's notes already say where the standard started.
- **Process idea (for the lead, optional):** a gate note when a ~CODE row at an earlier grade is not linked to the
  row that owns CODE, so the writer either links it or says it is an application.

### 3. Geometry constructions and the addition rule assume nothing, though earlier grades built them (minor; firm)

- **LAYER:** progression. **REPEAT:** yes (same kind as finding 2). **Disagrees with** the stitch, which left
  geo-constructions without assumes because "constructions are new in Geometry".
- **Rows:** geo-constructions, geo-addition-rule.
- **What is wrong:** 7.G.A.2 (m7-triangle-conditions) has students draw triangles "freehand, with ruler and
  protractor, and with technology", and the row's own words list "construct" and "compass". Compass work is not new
  in grade 10. geo-addition-rule reads the overlap "in a table or a Venn-style sketch", which is the grade 9
  two-way table.
- **Fix:** geo-constructions assumes m7-triangle-conditions (m7-triangle-conditions hands_on += geo-constructions;
  the skip of grades 8 and 9 is because neither grade has a construction standard: one sentence in the notes).
  geo-addition-rule assumes alg1-two-way-tables (alg1-two-way-tables hands_on += geo-addition-rule).

### 4. Four K to 8 links missing where the standards name the step (minor; firm)

- **LAYER:** progression. **REPEAT:** yes (social studies finding 3, science finding 5: rows that hand on to no one).
- m5-volume-additive (5.MD.C.5c, volume of two joined prisms) hands on to nothing, but 7.G.B.6 (m7-area-volume-
  composite) is the same idea with more solids. Fix: m5-volume-additive hands_on += m7-area-volume-composite and the
  reverse assumes; reason for skipping grade 6: grade 6 volume (6.G.A.2) is one prism with fraction edges.
- m5-fraction-add-sub-problems (5.NF.A.2) hands on to nothing; 7.NS.A.3 (m7-rational-problems) is the next fraction
  word-problem standard. Fix: link them; reason: grade 6 has no fraction add or subtract standard.
- m8-coordinate-distance assumes only m7-rational-add-subtract, but 6.NS.C.8 (m6-four-quadrants) is where students
  first find distances between points that share a coordinate, which is exactly the leg length in 8.G.B.8. Fix:
  assumes += m6-four-quadrants, with the skip reason "grade 7 has no coordinate distance standard".
- m2-number-line assumes nothing, though its own notes say the number line comes after rulers because it is built
  from length units. Fix: assumes += m1-measure-length-units (m1-measure-length-units hands_on += m2-number-line).
- Judgment call, same family: m8-two-way-tables assumes m7-probability-models, but 8.SP.A.4 is about relative
  frequency in data, which is 7.SP.C.6 (m7-chance-probability, a row that now hands on to no one). Swap the assumes
  to m7-chance-probability, or add it beside the current one.

### 5. British spellings in the student word lists, and two spellings of one term (minor; firm)

- **LAYER:** progression. **REPEAT:** new (earlier reads found teacher terms, not spelling).
- **Rows:** geo-rigid-motion-definitions ("centre of rotation"), geo-dilations ("centre of dilation"),
  geo-circle-parabola-equations ("centre"), geo-inscribed-circumscribed ("circumcentre", "incentre"),
  alg2-factors-zeros-graphs and alg2-rational-functions ("end behaviour"), alg2-study-design-randomness
  ("randomisation"), alg2-experiments-significance ("randomised", "randomisation").
- **Why it matters:** grade 8 teaches "center of rotation" and "center of dilation" (m8-rigid-motions,
  m8-dilations-similarity); grade 10 would then print a different spelling of the same term, and the standards a
  US teacher works from say "center" and "behavior".
- **Fix:** center, circumcenter, incenter, end behavior, randomization, randomized in those words cells. Notes may
  stay as written (teachers do not read them).

### 6. Two kindergarten leans name an ELA code no ELA row owns (minor; firm)

- **LAYER:** progression, with a process gap. **REPEAT:** yes (social studies finding 7: leans that name the wrong
  skill).
- **Rows:** mk-sort-count and mk-analyze-shapes lean on `ela:L.K.5a`. The ELA progression owns L.K.5 as a whole in
  ek-word-relationships; no ELA row names L.K.5a. The gate passes it because the code is in the standards file.
- **Fix:** `ela:ek-word-relationships (sort common objects such as shapes into categories)` in both rows.
- **Process (for the lead):** once the other subject's progression exists, the gate could require a cross_subject
  code to be owned or contributed to by a row at or before the leaning grade. Every other math lean checks out:
  the other 50 name a skill owned at or before the grade (grade 9 leans on RI.9-10.8 use the band, which ELA starts in
  grade 9).

### 7. Two fluency rows say nothing about timers or spaced practice (minor; firm)

- **LAYER:** progression. **REPEAT:** new.
- **Rows:** m3-add-sub-1000 (3.NBT.A.2, the grade 3 add and subtract fluency) and m6-decimal-operations (6.NS.B.3,
  fluent decimal algorithms). Every other fluency row (K.OA.A.5, 1.OA.C.6, 2.OA.B.2, 2.NBT.B.5, 3.OA.C.7,
  4.NBT.B.4, 5.NBT.B.5, 6.NS.B.2, 7.EE.B.4a) carries "no timer shown" and where the spaced practice runs.
- **Why it matters:** the lens names fluency without spaced, mixed practice as a scope and sequence fault, and a
  frame writer copies what the row says.
- **Fix:** add to each: "No timer shown. Fluency is kept up with short spaced, mixed practice in later units of the
  year."

## Settled by the expert

| Choice | Reason in one line | File |
|---|---|---|
| Exclude F-BF.A.1c, F-BF.B.4b, 4c, 4d with the reasons in finding 1 | (+) parts the base text never tags; the row notes already call them excluded | data/progressions/math-excluded.csv |
| The 14 high school assumes links in finding 2, and the two in finding 3 | Each is the step the standard or the row's own notes name | data/progressions/math.csv |
| The four K to 8 links in finding 4 (the m8-two-way-tables swap included) | Each is the standard the next one is written on | data/progressions/math.csv |
| US spelling in the words column (center, behavior, randomization) | One spelling for one term across grades 8 and 10, as the standards print it | data/progressions/math.csv |
| ela:L.K.5a becomes ela:ek-word-relationships in two K rows | Point at the skill that owns the code | data/progressions/math.csv |
| The timer and spaced-practice sentence on m3-add-sub-1000 and m6-decimal-operations | Matches every other fluency row | data/progressions/math.csv |

## For Cory

Nothing new. Two open scope items carried from the stitch, for completeness: whether an accelerated path (Algebra I
in grade 8) is offered (stitch item 12), and that the 49 excluded (+) codes and grade 12 math sit in electives that
have no progression rows yet (the reconcile notes grade 12 courses are not core).

## Pace through the grades

- Rows per grade run 20 to 28 with no grade far above its neighbours. Grade 12 has none by design (no core course).
- Major work by rows (K to 8, first owned code's cluster): K 15/20, 1 21/26, 2 19/28, 3 16/24, 4 15/27, 5 18/25,
  6 16/26, 7 12/23, 8 19/24. Grades 2, 4 and 7 sit lowest (68, 56 and 52 percent) because additional clusters
  are cut into more, smaller rows (grade 7 probability is three rows). Rows are not days; the stitch already sends
  the count to the course frames, where the 65 and 75 percent lines are measured by days. Not a progression defect.
- Strands that stop and start do so where the standards stop them (geometry skips Algebra I, functions skip
  Geometry, one-variable statistics skips grades 8 and 10), each with its reason in the returning row.

## Lens checklist, progression layer

| Line | Mark |
|---|---|
| A skill owned by two grades at the same depth | Met: the gate holds single ownership; every split high school code has a ~ row and says in the owner's notes what is completed |
| A handoff that skips a grade | Met: 67 skips, every one with a reason in one of its two rows |
| A model used before the grade that builds it | Met: gate clean; model gaps explained where the model returns |
| A standard algorithm expected before its fluency grade | Met: add and subtract grade 4, multiply grade 5, divide grade 6; grade 3 and 4 rows say "not required until" |
| A limit broken (grade 4 denominators, grade 3 products within 100) | Met on the rows checked (grade 3 denominators 2, 3, 4, 6, 8; grade 4 list with 100; grade 3 scale readings within 100) |
| Course frame, scope and sequence, unit and day lines | Not applicable to a progression |
| Lens gap: no high school bar | Missed, carried: the high school rows have no rubric to be read against; the Algebra I, Geometry and Algebra II frames will need one |
| Lens gap: progression pages only for grades 3 to 5 | Met by this file: K to 2, 6 to 8 and high school now have handoffs, limits and page pointers |
| Lens gap: past Algebra 2, no base text and no progression | Missed, carried (For Cory above); electives only |
| Lens gap: K to 2 fluency checked without a timer | Met in the rows (finding 7 closes the two that lack it); the how-to page is still for the course frames |

## What is right and should not be touched

- The notes: limits, expected errors, base text lessons and Progressions page pointers on nearly every row.
- High school ownership by the base text's tags (A-APR.A.1, N-RN.A, F-IF.A.3, S-ID.A.4 in Algebra II; N-Q and
  F-IF.C.7b completed in Geometry): the IM course tag counts back every placement I checked.
- One model name per idea across all grades, with the reasons for each gap.
- The grade 1 tape diagram (late in the year, from matching drawings): IM grade 1 unit 6 lessons 12 and 13 use it.

## What I could not judge

- Page pointers into the Progressions were not re-opened; I relied on the notes, the standards text and the IM tags.
  Nothing in the findings rests on a Progressions page.
- Whether F-IF.C.7d and S-CP.B.8, both (+) and owned, fit the time Algebra II and Geometry have: a frame question.

## Sources

- Common Core State Standards for Mathematics (data/standards/ccss-math-standards.txt): codes, (+) marks, standard
  text for findings 1, 3, 4.
- Student Achievement Partners focus documents (data/standards/ccss-math-focus.csv): major work counts.
- IM K-12 Math, 1st edition, CC BY 4.0, local copy: Algebra I, Geometry and Algebra II "lessons and standards"
  pages for the F-BF tags and high school ownership; grade 1 unit 6 for the tape diagram.
- No outside fetch was needed; nothing rests on memory alone.

## For the source list

Nothing new. The IM high school "lessons and standards" pages (hs-*/course/teachers__lessons_and_standards.md in
the local copy) are the fastest way to check a high school code's course: one grep per code.
