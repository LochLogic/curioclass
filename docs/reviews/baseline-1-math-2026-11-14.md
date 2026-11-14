# Baseline 1, part A: the math column (2026-11-14)

Brief: docs/pipeline/briefs/baseline-1.md, part "A subject column, subject=math". Reader: the curriculum expert
(docs/agents/EXPERT.md), run fresh. Bar: docs/RUBRIC-MATH-K8.md and docs/agents/lenses/math.md. No file but this
report was edited. ELA files were ignored, as asked.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/PRODUCTION-PATH.md steps 2 to 4, docs/GLOSSARY.md,
  docs/pipeline/briefs/frame-write.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md.
- All twelve math frames side by side: docs/courses/math-kindergarten, math-grade-1 to math-grade-8, algebra-i,
  geometry, algebra-ii (frame.md each): the brief, Seams, Models carried, the Units table (skills, days, the C3 and
  "Check set adds" columns), Course-level checks, For the lead, the Source map.
- data/progressions/math.csv: the model_in and model_out columns scripted across all 305 rows (first and last use
  of each model), and the hands_on chains for the threads named below.
- The band reads, only to avoid repeating them: docs/reviews/frame-math-*-2026-11-14.md, frame-algebra-i-*,
  frame-geometry-*, frame-algebra-ii-*, the four math fix reports and frame-cross-subject-2026-11-14.md.
- `python -X utf8 scripts/plan.py check`: 0 failures in every math frame and in progression math (305 rows).
- Outside sources: none fetched on this run. What rests on memory is marked so (the high school fluency list in
  finding 1, IM's lesson lengths).

## Verdict

Kindergarten to grade 8 climb soundly: each model enters before its first use, the fluency targets step up one
grade at a time, and the base text is kept in order with every cut and merge given a reason. The column breaks
where the band reads could not see it: the high school frames drop the fluency and spaced-practice thread that
runs through every grade below them, the treatment of unit assessments and of the year's end changes three times
across the grades with no reason given, and Geometry and Algebra II lose practices that every other course
places. None of this needs a new standard or a scope call; all of it should be fixed in the frames before the
math scope and sequence writers copy one band's pattern into another.

## Findings, most serious first

### 1. The fluency and spaced-practice thread stops at Algebra I
LAYER frame. REPEAT new (the Codex reruns deferred "fluency spacing" to later layers; no read noted that the
high school frames name no fluency at all).

- **Files:** docs/courses/algebra-i/frame.md, geometry/frame.md, algebra-ii/frame.md, "The course in brief".
- **What is wrong:** every frame from kindergarten to grade 8 has a "Fluency" bullet naming the grade's fluency
  standards, how they are built and how they are kept up in a daily opening of spaced, mixed practice (K to 5: the
  warm-up; 6 to 8: a 5-minute opening on top of IM's 45-minute lesson, which is why 6 to 8 set 50 minutes). The
  three high school frames contain the word "fluency" nowhere, name no daily spaced practice, and set "45 to 50
  minutes", a range under which the 5-minute opening disappears at 45.
- **Why it matters:** APPROACH-MATH principle 7 (a five-minute warm-up of spaced practice opens each day) binds
  every course, and the lens lists "fluency named but never given spaced, mixed practice" as a scope and sequence
  error. A writer working from these frames would build high school days with no spaced practice and no named
  fluency targets, and grade 8's equation fluency (8.EE.C.7, kept up "through units 6 to 8") would have nowhere to
  go in Algebra I.
- **Fix:** in each high school frame, replace "one lesson of 45 to 50 minutes a day" in the Days bullet with "one
  50-minute lesson a day: a 5-minute opening of spaced, mixed practice on earlier work, then the base lesson
  (written for a period of at least 45 minutes)", and add a bullet after "Modeling":
  "**Fluency without a timer.** The procedures this course expects to be fluent: <list>. Built in the units named,
  kept up in the daily opening for the rest of the year (and, for Algebra II, on the Algebra I skills Geometry
  does not use). No countdown timer is ever shown to a student." Candidate lists, from memory of the high school
  publishers' criteria fluency recommendations, to be confirmed when docs/RUBRIC-MATH-HS.md is written: Algebra I,
  A-SSE.A.1 and A.2 (reading and rewriting expressions), A-APR.A.1 (polynomial arithmetic), A-REI.B.3 (linear
  equations and inequalities in one variable), F-IF graphs of the course's families; Geometry, G-SRT.B.5
  (congruence and similarity criteria in problems), G-GPE.B.4 and B.7 (coordinates in proofs, perimeter and area),
  G-CO.D.12 (constructions); Algebra II, A-APR.D.6 (rewriting rational expressions), A-SSE.A.2, F-BF.B.3
  (transformations of graphs). If 45-minute periods must be allowed, use the grade 6 frame's line ("the spaced
  practice replaces part of the warm-up on most days and the day count stands").

### 2. What follows a unit assessment changes three times across the column
LAYER frame. REPEAT new.

- **Files:** Days bullets of all twelve frames; the source maps of grades 6 to 8 and the high school courses.
- **What is wrong:** grades 3 to 8 give every unit a respond day after its end-of-unit assessment (grades 6 to 8
  add mid-unit checks too). Kindergarten to grade 2 keep one assessment day and no respond day (IM's second
  assessment day was spent on added lessons). The three high school courses have no respond day after any unit
  assessment and no mid-unit check, but spend a whole readiness day on every unit (23 days over three courses),
  where grades 3 to 8 give a readiness check of about ten minutes (grade 4: at the end of the previous unit's
  respond day). No frame gives a reason for its pattern against its neighbours. The glossary says a respond day
  "acts on an assessment", and the rubric (3g) asks what the teacher does with results.
- **Why it matters:** a grade 8 student meets three respond days a unit-pair and a mid-unit check; the same student
  in Algebra I the next year (or the same year, on the accelerated path) meets none, in the course where gaps cost
  most. K to 2 teachers are told to gather one-to-one evidence but given no time to act on it.
- **Fix:**
  - High school (all three frames, Days bullet and source map "Readiness days" row): the readiness day becomes a
    respond day after the end-of-unit assessment; the readiness check moves to the last 10 minutes of the previous
    unit's respond day, as grade 4 does ("so it is marked before the unit's first day and can shape it"), with the
    supports-lesson reminder given there. Unit 1's check opens its first day. Day totals do not change.
    Algebra II keeps its readiness emphasis by naming, in each unit, the reminder lessons given in that respond
    day.
  - Kindergarten to grade 2 (Days bullet): add "After each end-of-unit assessment, the respond work runs in the
    center time of the next two lessons, in small groups, on what the assessment showed", the pattern grade 6
    already uses for some mid-unit checks. Day totals do not change.

### 3. Geometry and Algebra II do not place all eight practices
LAYER frame. REPEAT new (the kind, practices, was a K-8 band finding; this gap was not found).

- **Files:** docs/courses/geometry/frame.md, Units table, C3 column; docs/courses/algebra-ii/frame.md, the same.
- **What is wrong:** scripted across the C3 and "Check set adds" columns, every course from kindergarten to
  Algebra I places all eight practices. Geometry places none of MP1 or MP2; Algebra II places no MP1.
- **Why it matters:** the rubric reads the eight practices across the course (gateway 2), and a unit writer only
  plans tasks for the practices the frame names. Geometry without MP2 drops reasoning between quantities in the
  course whose units 3 to 5 are similarity, trigonometry and density.
- **Fix:** Geometry unit 4 C3 cell: "Not used in math (practices MP2, MP4, MP5)" (ratios of sides as quantities,
  in place of MP6); unit 5: "Not used in math (practices MP1, MP4, MP6)" (the density and design problems, in place
  of MP7). Algebra II unit 4 C3 cell: "Not used in math (practices MP1, MP2, MP4)" (solving for an unknown time,
  in place of MP7, which units 1 to 3, 5 and 6 already carry). Each frame then adds the line grades 2, 3 and 5
  carry: "All eight are placed: MP1 (units ...), ...".

### 4. The year's end is built three ways, and grades 6 to 8 end thinnest
LAYER frame, base text. REPEAT new.

- **Files:** Course-level checks sections of all frames; Source map last rows of grades 6 to 8; Units tables of
  kindergarten to grade 2 (last unit).
- **What is wrong:** IM's last unit of each grade ("Putting it all together") is kept as a teaching unit in
  kindergarten to grade 2, turned into seven or eight year-review days before a two-day final check in grades 3
  to 5, and cut in grades 6 to 8. The result:
  - Grades 6 to 8 end with a one-day check (one 50-minute period on eight units) on day 159 and a respond day on
    day 160, with no review. Grade 5 before them gives two check days, two respond days and seven review days;
    Algebra I after them gives two check days.
  - Kindergarten to grade 2 end with the last unit's own assessment day and then a two-day end-of-year check that
    covers the same ground (grade 1 unit 8 owns no rows at all), three assessment days in a row.
  - Only the K to 2 and high school frames hand the year-end record on to the next teacher; grades 3 to 8 do not,
    and no frame's readiness bullet says it uses the record it receives.
  - Items labelled by standard with "what to do next" (rubric gap 3) are promised in grades 3 to 8 checks only.
- **Why it matters:** the year-end check is the evidence the next grade's readiness checks rest on; in grades 6 to
  8 it is the thinnest of the column at the point where Algebra I readiness is decided.
- **Fix:**
  - Grades 6 to 8: Check 3 becomes 2 days, as in grades 3 to 5 and high school. The day comes from one unit:
    grade 6 unit 6's mid-unit respond day becomes respond work in the next two openings (the unit 3 pattern);
    grade 7 and grade 8 unit 6 each give up their mixed-practice day. Update the Days bullet, the unit day counts
    and the Check 3 row ("2, then 1 respond day").
  - Kindergarten to grade 2: the last unit's end-of-unit assessment day is folded into the end-of-year check
    (which already covers its rows: count to 100, fluency within 5, and so on), and the freed day becomes a second
    respond day after that check. State it in the Days bullet and the last Units row.
  - Every frame's last check row: "The record, with what the respond day changed, goes on to the <next course>
    teacher." Every Readiness bullet from grade 1 up: "The readiness check in unit 1 starts from the record the
    previous course hands on."
  - K to 2 and high school check sections: add "Every item names its standard and what to do next for a student
    who misses it", as grades 3 to 8 say.

### 5. One column means three things across the grades
LAYER frame. REPEAT new.

- **Files:** the Units table's C3 and "Check set adds" columns, and the "Standard" bullet, in all frames.
- **What is wrong:** kindergarten to grade 2 put the practices and an extension in "Check set adds" and call
  their Progressions check a "Check set"; grades 3 to 5 put the practices in C3 and a Progressions page pointer in
  "Check set adds" and say "there is no check set"; grades 6 to 8 write "Candidate: none beyond the CCSS codes";
  high school writes extension tasks. In the glossary sense (another state's standards), math has no check set at
  all. Grades 3 to 8 name no per-unit extension (rubric gap 4); grades 6 to 8 name extension candidates only in
  the source map.
- **Why it matters:** the math scope and sequence writers will read this column grade by grade and get a
  different job from each band; extensions for students ready for more would be planned in K to 2 and high
  school and missed in between.
- **Fix:** one rule for all twelve frames, written in each "Standard" bullet: "Math has no check set. The C3
  column names the unit's practices; the 'Check set adds' column names, as candidates, the Progressions check for
  the unit and one extension." Then: K to 2, move the practices from "Check set adds" to C3 ("None (math).
  Practices: ...") and change "Check set: each unit plan checks ..." to "Check: each unit plan checks ...";
  grades 3 to 5, add "Extension: ..." to each cell; grades 6 to 8, replace "Candidate: none beyond the CCSS codes"
  with the Progressions pointer and the extension already named in the source map's cut rows.

### 6. The trapezoid definition is stated in grades 3 to 5 and dropped where it matters
LAYER frame. REPEAT new.

- **Files:** docs/courses/math-grade-6/frame.md (unit 1, trapezoid areas); docs/courses/geometry/frame.md (unit 1,
  G-CO.A.3, symmetries that carry a trapezoid onto itself); the progression row m5-shape-hierarchy, whose note says
  pick one definition and keep it.
- **What is wrong:** grades 3, 4 and 5 state the inclusive definition (at least one pair of parallel sides).
  Grade 6 and Geometry, where the answer depends on it (a parallelogram's area as a trapezoid case; a
  parallelogram counted among trapezoids when listing symmetries), do not.
- **Fix:** grade 6 unit 1 notes cell and Geometry unit 1 notes cell: "Trapezoid keeps the inclusive definition
  of grades 4 and 5 (at least one pair of parallel sides), so a parallelogram is a trapezoid; tasks say so where
  it changes an answer."

### 7. Models carried: origin and hand-on cells disagree across frames
LAYER frame. REPEAT new.

- **Files and cells:** algebra-i/frame.md Models carried rows number-line and area-model; geometry/frame.md the
  same two rows; algebra-ii/frame.md the same two rows; math-grade-7/frame.md row net.
- **What is wrong:** the high school frames say the number line was introduced by m2-compare-three-digit and the
  area model by m3-properties; the grade 2 and grade 3 frames introduce them with m2-number-line (unit 4) and
  m3-area-multiply (unit 2), and m3-properties sits in grade 3 unit 4, after the model is in use. Grade 7 says the
  net is used again in Geometry; no Geometry row takes the net as model_in and the Geometry frame never names it.
- **Fix:** in the six high school cells, "Introduced in grade 2 (m2-number-line)" and "Introduced in grade 3
  (m3-area-multiply)". Grade 7 net row, "Used again in": "Ends here; Geometry's cross sections (geo-cross-sections-
  solids) work from solids, not nets."

### 8. Nobody plans the spread of people and places across math
LAYER process. REPEAT new.

- **Files:** every frame's last Units column and Sensitivity bullet.
- **What is wrong:** contexts come with the base text, which is fine, but only grades 3 and 4 promise "a range of
  names", and the only named cultural context in thirteen years is grade 2's saree lessons. Rubric indicator 3p
  asks for a range of people shown and for drawing on students' backgrounds; the brief asks for a fair spread over
  K to 12.
- **Fix:** one sentence in each frame's Sensitivity bullet, as grades 3 and 4 have: "Word problems use a range of
  names and settings; the unit plan lists the people and places its problems show." And one row in
  data/plans/later.csv for the math scope and sequence step: "Context spread K to 12: tally names, places and
  cultural contexts per course from the unit plans and fix any gap before days are written."

### 9. The rubric page names a start-of-year check no frame has
LAYER standard (the bar page). REPEAT new.

- **File:** docs/RUBRIC-MATH-K8.md line 35, Gateway 3 teacher supports, "Where we answer it today": "the cumulative
  checks it names (a start-of-year check and four more)". That was the old grade 4 scope. Every frame now uses a
  readiness check per unit and two or three course-level checks; none has a start-of-year check.
- **Fix:** replace that phrase with "the course-level checks each frame names (two in K to 2, three in grades 3 to
  12) and a readiness check opening each unit".

## Settled by the expert

| Choice | Reason in one line | File it touches |
|---|---|---|
| High school lesson: 50 minutes, 5 of them a spaced-practice opening | Matches grades 6 to 8 and APPROACH-MATH principle 7; Cory may reverse | algebra-i, geometry, algebra-ii frame.md, Days bullet |
| High school readiness day becomes a respond day; readiness check moves to the end of the previous respond day | Day swap inside each unit; matches grade 4's pattern; totals unchanged | the three high school frames, Days bullet and source map |
| K to 2 respond work in center time of the two lessons after each unit assessment | No day moves; the grade 6 pattern | math-kindergarten, -grade-1, -grade-2 frame.md, Days bullet |
| Geometry MP2 in unit 4, MP1 in unit 5; Algebra II MP1 in unit 4 | The units whose tasks most need them | geometry, algebra-ii frame.md, C3 cells |
| Trapezoid stays inclusive in grade 6 and Geometry | Keeps the progression row's "pick one and keep it" | math-grade-6, geometry frame.md, unit 1 notes |
| Model origin cells: m2-number-line, m3-area-multiply; grade 7 net ends in grade 7 | Match the earlier frames and the rows | algebra-i, geometry, algebra-ii, math-grade-7 frame.md |

## For Cory

1. **The accelerated path reaches further than the band reads said.** The Algebra I and grade 8 frames say a
   grade 8 student taking Algebra I needs a compression plan for the grade 8 rows. Read as a column, that plan
   also touches grades 6 and 7 (the usual way is to fold grade 8's work into grades 6 and 7 over two years), and
   neither frame mentions it. Who takes the path, and whether Curio Class offers it at all, is your call; if yes, a
   compressed grade 7 course becomes a 13th math frame. REPEAT yes (the path itself was raised; its reach into
   grades 6 and 7 is new).

## What is right and should not be touched

- The model order: no model is used before the frame that introduces it, and the reactivated ones (dot plot,
  tree diagram, scatter plot) are rebuilt on a familiar example first.
- The fluency ladder from within 5 (K) to linear equations (grade 8), each untimed, each kept up after it is built.
- The base text kept in its own order in every grade but kindergarten's ten-frame and grade 8's data move, each
  with a stated reason.

## What I could not judge

- The high school fluency list in finding 1 rests on memory of the publishers' criteria; it waits on the high
  school bar page.
- Whether contexts repeat across grades at the problem level: the frames name too few for that; the scope and
  sequence can tell.
