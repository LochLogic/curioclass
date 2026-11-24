# Sequence read: Calculus, 2026-11-24

Expert cold read of the Curio Class Calculus scope and sequence (grade 12, draft of 2026-11-23/24), done under docs/pipeline/briefs/sequence-read.md with the math lens and docs/RUBRIC-MATH-HS.md (its "grade 12 courses" section stands in for focus 1a to 1c). I did not write the scope and read it cold.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/pipeline/briefs/sequence-read.md and sequence-write.md (binding), docs/RUBRIC-MATH-HS.md (headings and the grade 12 section).
- docs/courses/calculus/scope-and-sequence.md in full, including "For the lead"; docs/courses/calculus/frame.md in full; docs/courses/calculus/DEFAULTS.md.
- data/plans/calculus/days.csv (160 rows) and source-map.csv (100 rows).
- data/standards/curio-math-electives.txt, CUR-CA.1 to CUR-CA.30, clause by clause.
- data/progressions/math.csv: the 30 calc- rows (assumes, load notes) and every grade 11 and 12 row that assumes one of the earlier rows Calculus picks up (one-hop check); pc-sequences-series-binomial.
- data/plans/algebra-ii/days.csv and data/plans/precalculus/days.csv (sigma notation search only); the tools columns of both, for convention.
- docs/courses/CALENDAR.md and data/plans/calendar.csv, grade 12 rows.
- The base text's archive copy: the file listing of S:\CurioClass-sources\contemporary-calculus\archive-2016 (section numbers and titles), against the source map and every "Base CC" note. I did not read the PDFs' text.
- Earlier reads: docs/reviews/frame-calculus-2026-11-16.md (title only), sequence-algebra-ii-2026-11-15.md, the finding lists of sequence-geometry-2026-11-15.md and sequence-algebra-i-2026-11-15.md.
- Gates, filtered to this course: plan.py check (sequence calculus 0 failures, frame calculus 0 failures), sequence.py check calculus (0 failures), frame.py calendar (grade 12 has no stagger rule; calendar.csv weeks match the scope), stale.py check (0 failures overall).

## Verdict

A sound, carefully argued sequence: every clause of all 30 outcomes and G-GMD.A.2 sits on a day, understanding comes before rules in every unit (secants before derivatives, sums before antiderivatives, partial sums before tests), the day order inside unit 2 holds, and the base-text renumbering was checked against the archive copy. The biggest risk is a seam the frame placed too late: sigma notation is used on day 67 but its Precalculus row is first retrieved on day 134. The one change that matters most besides that is to settle the frame's route contradiction (accelerated or core grade count) so the readiness checks match the students Cory set the course for. Ready after the fixes below; no unit is resized and no outcome moves.

## Findings

### 1. Sigma notation is used on day 67 but not retrieved until day 134 (moderate)

- What is wrong: day 67 has students "write left, right and midpoint sums in sigma notation". Sigma notation is first taught in Precalculus unit 10 (pc-sequences-series-binomial, Precalculus day 144, "write sums in sigma notation"); Algebra II's days never use it. The frame's second Seams table ties pc-sequences-series-binomial only to calc-series-convergence (unit 10), so the scope retrieves it on day 134, 67 days after it is needed. A student who came without Precalculus gets the row's bridge pack "in the unit's openings" of unit 10, also too late.
- Why it matters: the unit planner will build day 67 assuming the notation is fresh; students who have forgotten it (or never had it) meet new notation and a new idea on the same day.
- Fix: day 67 note adds "Retrieval task (10 minutes, practice, never check evidence): pc-sequences-series-binomial (sigma notation) from Precalculus"; day 134 keeps the infinite geometric series retrieval. Frame, second Seams table: add a row "calc-riemann-sums (unit 5) | pc-sequences-series-binomial (Precalculus unit 10) | Part of a lesson: sigma notation (the rest bridged in unit 10)". Scope "Earlier rows" paragraph: add day 67 to the Precalculus seam days, and the minutes line rises by 10.
- Evidence: days.csv days 67 and 134; progression row pc-sequences-series-binomial (words: sigma notation); precalculus days.csv day 144; frame Seams. Confidence: firm. LAYER: frame. REPEAT: new.

### 2. The frame names two routes for the readiness count, and the scope follows the one Cory did not set (moderate)

- What is wrong: the frame's route bullet says "The scope writer counts on the accelerated path, the route Cory set; the scope gate's count governs", while its readiness bullet and Seams table count on the core grade numbers. The writer took the core count because the gate agrees (For the lead 3). On the accelerated path (Algebra II in grade 10, Precalculus in grade 11), which is the route the students actually take, six rows that no pc- row builds on were last used two grades back: alg2-polynomial-identities, alg1-piecewise-absolute-value, geo-arcs-sectors-radians (unit 1), alg1-quadratic-forms-graphs (unit 3), alg2-factors-zeros-graphs (unit 4), alg2-normal-distributions (unit 5). The scope retrieves all six (days 5, 8, 10, 37, 55, 66). The reverse also holds: geo-solving-right-triangles is assumed by pc-inverse-trig and pc-oblique-triangles, so on that route it was used the year before, and unit 3 checks a year-before row on day 36.
- Why it matters: the gate counts grade numbers and cannot know the route, so "the gate governs" does not settle what Cory decided; units 1, 3, 4 and 5 retrieve rows two years idle for the real students. The cost of fixing is small (two new ten-minute checks, three retrieval tasks dropped).
- Fix (lead pick; I recommend the accelerated count): frame route bullet resolves the contradiction in one sentence ("the readiness count follows the accelerated path; the gate's core count is a floor"). Then: day 1's last ten minutes hold unit 1's readiness check on alg2-polynomial-identities, alg1-piecewise-absolute-value and geo-arcs-sectors-radians (assess `readiness`), and the day 5, 8 and 10 retrieval tasks drop; move day 1's alg2-rational-functions retrieval to day 5 (holes, which suits it) so day 1 holds the hook, the lesson and one check; day 36 adds alg1-quadratic-forms-graphs and drops geo-solving-right-triangles (retrieved instead on day 41, the right-triangle related rates day); day 50 adds alg2-factors-zeros-graphs (day 55's retrieval drops); day 65 gains unit 5's readiness check on alg2-normal-distributions (assess `readiness`; day 66's retrieval drops). Day 116 and 129 keep their geo-arcs-sectors-radians retrievals (used in unit 1). The ledger table and the minutes line follow. If the lead keeps the core count instead, strike the accelerated sentence from the frame so the next writer is not told two things.
- Evidence: frame route and readiness bullets; scope For the lead 3 and ledger; progression assumes (pc-inverse-trig, pc-oblique-triangles assume geo-solving-right-triangles). Confidence: likely (the route fact is firm; which count the rule intends is the lead's). LAYER: frame. REPEAT: new.

### 3. Each check's first day repeats the unit sitting's task form two days later (moderate)

- What is wrong: rule 2 says "A course-level check never repeats a task form given in the last two weeks." Days 82, 120 and 158 are sittings of short unseen items two days after the unit sittings of short unseen items on days 80, 118 and 156. The writer names this (For the lead 4) and picks "keep" because the frame designed it so.
- Why it matters: the rule is plain, and three times a year students sit the same form twice in three days; the evidence adds little and the planner will write a second test.
- Fix (I do not agree with the pick): keep both check days and their codes, but give the first day's short items a different form from the unit sitting: critique and correct a worked solution, choose which of two claims is right and why, or sort and justify, as the Algebra II read accepted for its checks. The untimed fluency station on day 158 stays direct, with no supplied work (rule 2: never inside a critique). Scope: one sentence under Course-level checks; days 82, 120 and 158 notes name the form; For the lead 4 closes.
- Evidence: sequence-write rule 2 ("Collect once"); days.csv days 80, 82, 118, 120, 156, 158; sequence-algebra-ii-2026-11-15.md finding 1 (form change judged right). Confidence: firm. LAYER: sequence. REPEAT: yes.

### 4. Unit 7 gives slope fields a day over load and squeezes the modeling cycle and its revision (moderate)

- What is wrong: the rows' loads are 4 (calc-slope-fields-euler) and 5 (calc-separable-models) of the unit's 9 days. Slope fields get four teaching days (94 to 97, including the Fluency day 96); separable models get three (98 to 100), and day 100 holds the whole modeling cycle (fit by taking logarithms on grid paper, compute, interpret, validate, report) in one period. The revision then lands on respond day 102 beside the regrouping and unit 8's readiness check: 5 opening, 15 revision, 10 readiness and about 3 for papers leave about 17 minutes to reteach and redo two codes. Units 3, 4 and 8 each give the cycle two days.
- Why it matters: the rubric's "modeling cycle stays whole"; in one period validation is the step a busy class drops, and the respond day becomes too thin to act on the unit 7 sitting.
- Fix (lead pick, since it uses step 2 of the frame's trim order): fold day 96's slope-field matching into the Euler day now, and reorder unit 7 as 94 write and check equations, 95 slope fields, 96 Euler's method with slope-field matching beside it (Understanding), 97 separable equations and exponential growth and decay, 98 the cooling model drafted (assumptions, fit, computation, interpretation, first report; cooling needs only day 97), 99 logistic growth, 100 validation against a new reading and report revision (25 minutes) with mixed practice, 101 end, 102 respond plus readiness. Two nights for feedback, the respond day freed, separable models at four teaching days. The frame's trim order step 2 and the scope's Shorter path then need a substitute fold-in (day 63, unit 4's whole-unit practice, folding into day 62 and the openings, is the nearest like-for-like). If the lead keeps the trim step, keep the current order and say on day 102 that the regroup is 17 minutes.
- Evidence: progression load notes; days.csv days 94 to 102; RUBRIC-MATH-HS grade 12 section; frame End-of-unit evidence and A tight course. Confidence: likely. LAYER: sequence. REPEAT: new.

### 5. Units 3 and 4 give the teacher one night to write feedback on 30 reports (low)

- What is wrong: the related rates report is drafted on day 44 and revised "from the written feedback" on day 45; the design report is drafted on day 61 and revised on day 62. Unit 8 leaves three days (107 to 110).
- Why it matters: 30 written-feedback reports overnight is not what a busy teacher can do well; the likely result is thin feedback or a revision done without it.
- Fix: day swaps inside the units (settled below): unit 3 day 43 becomes the modeling draft and day 44 the related rates practice (the written-explanation candidate moves with it); unit 4 day 62 becomes the whole-unit practice and day 63 the validation and revision. Notes on days 49 and 64 update the revision day.
- Evidence: days.csv days 43 to 45, 61 to 63, 107 to 110; frame End-of-unit evidence. Confidence: likely. LAYER: sequence. REPEAT: new.

### 6. Day 89 is typed Fluency but is the first day that teaches choosing a method (low)

- What is wrong: CUR-CA.17 ends "and choose a method from the form of the integrand". Days 85 to 88 each teach one method; no earlier day teaches the choice, and day 89's goal is that choice (sort by method, then carry out). Write rule: a Fluency day practices only what an earlier day taught.
- Why it matters: a section writer reading Fluency will write a drill set and skip the explicit teaching of how to read the form of an integrand, which is the clause.
- Fix: day 89 kind Application ("using taught ideas on a new task"), goal unchanged; the frame's fluency bullet keeps choosing a method as a fluency kept up in the openings from day 90 on (settled below).
- Evidence: days.csv days 85 to 89; frame Day kinds; GLOSSARY teaching day. Confidence: likely. LAYER: sequence. REPEAT: new.

### 7. Day 74's note does not match its goal (low)

- What is wrong: the goal is net change from a rate rule and from a rate graph; the note says the day "builds the accumulation numerically from a table".
- Why it matters: the section writer will not know which the day does.
- Fix: note reads "Ours (base CC 8.7 has no archive copy): net change from a rate rule and a rate graph, with units" (settled below).
- Evidence: days.csv day 74. Confidence: firm. LAYER: sequence. REPEAT: new.

## Checks the brief asks for

- **Order inside each unit:** holds in all eleven. Unit 2's rule order (the writer's "read first") is right: power, sum and constant multiple, product and quotient, then sine and cosine (the other trigonometric functions need the quotient rule), e to the x and ln x by graph, the chain rule before inverses because the inverse derivative is the chain rule on f(g(x)) = x, ln x proved on day 28, b to the x on day 30 after the chain rule. One item-level gap: day 22 needs the limit of (cos h - 1)/h, which day 8 does not give (settled below). Unit 3's linearization before concavity is named and uses day 33's second derivative. Every arc ends at its compelling question.
- **Assessments:** every end day lists every owned code of its unit with "a prompt for each clause"; I checked each outcome's clauses against the teaching days and every clause is taught before its end day. No unit is over 25 days, so no mid-unit assessment is needed. Response time is counted once, on each respond day.
- **Readiness or retrieval:** on the core count the ledger is right and the one-hop claims hold (alg2-transformations-functions, alg2-unit-circle-radians, alg2-trig-functions-graphs, alg2-polynomial-arithmetic and alg2-factors-zeros-graphs carry the Algebra I and Geometry rows). The three readiness checks sit on respond days 36, 50 and 102, each the last ten minutes, rows named in the note, none on a unit's first day. On the accelerated route see finding 2. Unit 1 has no readiness rows on the core count, so day 1 holds none.
- **Checks that do not repeat:** each check follows an end-of-unit assessment (units 5, 8, 11), draws fresh items only from earlier units and reuses that unit's record unscored with its date; the scope says so and each day lists only its sampled codes. Task form: finding 3.
- **Standards in full:** every clause of CUR-CA.1 to CUR-CA.30 and G-GMD.A.2 is carried by a named day (no outcome has lettered parts).
- **Days by load:** per row, teaching days match the load notes within a day in units 1 to 6 and 8 to 11; unit 7 is off (finding 4).
- **The calendar:** checks on weeks 17, 24 to 25 and 32, as CALENDAR.md and calendar.csv give; grade 12 has no stagger rule; the frame has no same-year lean (Physics is grade 11), so no bridge is needed.
- **Candidate cells:** all eleven settled, each kept inside existing days with no day added, each placed on its end day.
- **Shorter path:** present: a 45-minute period (opening to three minutes, practice sets trimmed, sittings intact) and ten named fold-in days of 50 minutes each, total 500 minutes against 160 days, none assessed, none a feedback, revision, check or respond day, the first five following the frame's trim order. If finding 4's fix is taken, day 96 leaves the list and a substitute joins it.
- **Source map:** every section in the archive listing (chapters 0 to 13 and the answer pages) has a row; the archive has no CC 2.3 file (the listing goes from 2.2 to 2.4), which confirms For the lead 1. Every "Base CC" note in days.csv matches an archive title (for example 5.5 Additional Applications on day 106, 8.6 trigonometric integrals on day 88, 10.11 Taylor polynomials on days 146 to 148). Moves from the base order each carry a reason. Goals read as fresh Curio Class words in a spot check against section titles; I did not read the PDFs' text, so the copy rate is not measured.
- **Minutes line:** the 30 retrieval tasks, 3 readiness checks, the review day and 75 openings sum to 755 minutes, 10.0 percent, as stated; finding 1 adds 10 and finding 2 changes it by about minus 20.

## Lens checklist (scope and sequence layer)

- A standard taught in part with no later day that finishes it: met (CUR-CA.5 begun on day 20, finished on day 30, and the scope says so).
- No problems that join units on purpose: met (days 106, 110 and 155; the three extended check tasks on days 83, 121 and 159).
- Fluency named but never given spaced, mixed practice: met (openings from days 24, 79 and 89 to the end of the year; the untimed station on day 158 samples all five fluencies directly).
- A model used before the course builds it: met (riemann-rectangles from day 66, slope-field from day 95; vector-arrow and polar-grid retrieved from Precalculus).
- A limit broken: met (Euler at most eight steps by hand; arc length checked on a proper integral to x = r/2).
- Day kinds: one fault (finding 6).

## For the lead (the scope's own items)

1. CC 2.3 missing from the CC BY store: agree. The archive listing has no 2.3 file; days 22 and 23 stay ours.
2. Archive numbering differs from the frame's Source map: agree; the scope's numbering matches the archive listing. Update the frame's Source map in the fix pass.
3. The route: disagree with "the gate's count, as written" as the end state; see finding 2. At least strike one of the frame's two sentences.
4. Same task form within two weeks: disagree with "keep"; see finding 3 (change the first day's form, keep its codes).
5. Unit 7's revision on the respond day: true under the current order, but a better order exists; see finding 4.

## What is right and should not be touched

- Understanding before rules in every unit, and the accumulation function read from a rate graph (day 70) before the fundamental theorem.
- Unit 2's rule order and the ln x path (read from slopes on day 23, proved on day 28).
- The Cavalieri day (111) before any volume integral, and the arc length check on the circle to x = r/2.
- Improper integrals (unit 6) before the integral test (unit 10), and the ratio test (day 140) before intervals of convergence (day 150).
- The checks' reuse of the just-ended unit's record, and the direct fluency station on day 158.
- The respond-day placement of all readiness checks.

## What I could not judge

- The base text's words against our goals (copy rate): I read the archive file list, not the PDF text.
- Whether the gate would note the accelerated-route readiness rows of finding 2; the lead can run sequence.py after the fix.
- Outside sources: I reached none on this run. The ordering judgments (unit 2's rules, unit 7's load, the placement of sigma notation) rest on memory of common open calculus sequences and on the course's own files.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 3: swap days 43 and 44 (day 43 the modeling draft, day 44 related rates practice with the written-explanation candidate) | two nights for written feedback before the day 45 revision | data/plans/calculus/days.csv; scope unit 3 paragraph |
| Unit 4: swap days 62 and 63 (day 62 whole-unit practice, day 63 validation and revision); day 64 note says revision on day 63 | two nights for written feedback | data/plans/calculus/days.csv; scope unit 4 paragraph |
| Day 89 kind Fluency to Application | first day that teaches choosing a method, a CUR-CA.17 clause | data/plans/calculus/days.csv |
| Day 74 note rewritten to match its goal | note and goal disagree | data/plans/calculus/days.csv |
| Day 22 note adds that the limit of (cos h - 1)/h is derived inside the day from day 8's sin h over h | the cosine and sine derivatives need it and no earlier day gives it | data/plans/calculus/days.csv |
| Day 67 note adds a ten-minute sigma notation retrieval (pc-sequences-series-binomial) | the notation is used that day (finding 1) | data/plans/calculus/days.csv; scope Earlier rows and minutes line |

## Stale notes (for the fix pass)

- Frame Source map still on the current site's numbering (scope For the lead 2).
- Frame minutes line says about 625 minutes; the scope's 755 (with the reason) should replace it.
- Frame route bullet and readiness bullet disagree (finding 2).
- Frame prose uses British spellings (optimisation, rationalising, behaviour, centres); US spelling in the fix pass.

## For Cory

None. Every finding is inside the course's settled scope; the route itself is already Cory's decision (accelerated, 2026-11-17), and finding 2 only makes the frame follow it.

## Sources

- data/standards/curio-math-electives.txt: the outcome clauses checked day by day.
- data/progressions/math.csv: load notes, assumes and the one-hop check.
- S:\CurioClass-sources\contemporary-calculus\archive-2016 (file listing): the base text's section numbers and titles.
- data/plans/precalculus/days.csv and data/plans/algebra-ii/days.csv: where sigma notation is first taught.
- From memory: common open calculus course orders, for the unit 2 rule order and the unit 7 load judgment.

The caller logs each finding with scripts/plan.py defect (found_by expert); this read edited no other file.
