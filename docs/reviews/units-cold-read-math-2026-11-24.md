# Math unit plans: cold read for the stage 4 gate, 2026-11-24

COURSE-RUN stage 4 gate, math: one cold read from the progression down. Read by a fresh agent that wrote and fixed
none of it. Scope: data/progressions/math.csv in grade order, then the core courses of frames.csv subject math in
grade order: math-kindergarten, math-grade-1, math-grade-2, math-grade-3, math-grade-5, math-grade-6, math-grade-7,
math-grade-8, algebra-i, geometry, algebra-ii (91 unit plans). math-grade-4 is another session's and was not opened.
Precalculus, statistics and calculus (grade 12, core electives) have frames and scopes but no unit plans yet, so they
were read only for progression ownership (see the note at the end). The 2026-11-24 ledgers were read after this read,
only to mark what they had already fixed.

## Verdict

The math chain holds and the core baseline is ready for owner approval once the four moderate items below are
settled or knowingly accepted. There is no serious fault. Every K to 11 progression node outside grade 4 is owned by
exactly one frame unit at its grade, appears in that unit's days and plan, and every earlier-grade row a unit assumes
is either retrieved or readiness-checked as rule 2 asks, with only two small misses. The biggest risk is Algebra II's
spaced openings: one fixed polynomial and rational rotation fills about 117 of its 160 days and never returns to
sequences, logarithms or trigonometry, so the course's later work gets almost no spaced practice before the
course-level checks.

## How the chain was checked

- **Ownership (script, frame Units tables against math.csv):** every K to 3 and 5 to 11 node owned by exactly one
  unit at its grade; no node owned at a wrong grade; no standard owned by two units across these courses (frame
  Owned standards column). Every frame-owned row is in that unit's days.csv skills and in its plan's owned line.
- **Assumed rows (script, progression assumes against days.csv skills, the readiness day before each unit, and each
  plan's field 4 table):** all present but two (finding 6). No assumes row points at a later grade; no hands_on row
  points at an earlier grade. No field 4 row's "Rule says" disagrees with its "days.csv names it".
- **Taught twice as new (script, same-grade rows used before their owner unit, then read):** 65 day rows across
  grade 2, 3, 7, 8 and Algebra I. Nearly all are begun parts that the plan says are finished later (grade 3 unit 1
  begins 3.OA.A.3, unit 3 begins 3.OA.D.8, both finished in unit 5) or spaced fluency (3.OA.C.7). None reteaches a
  skill as new; the labelling of begun standards is finding 2.
- **Review and return pointers (script):** every "Unit N, day D" in Returns and Handoffs lines lands in unit N but one
  (finding 7).
- **Gate:** `unitplan.py check` on the 11 courses: 91 PASS, 0 FAIL.
- **Read:** frames' Units tables for all 11 courses; field 2 to 4 of grade 5 s01, grade 7 s01 to s08 (owned and
  earlier lines), Algebra II s04 and s07 in full through field 4, grade 3 s01, s03 and s05 field 2 and day lists,
  grade 1 s02 and s08, grade 2 s09, all 1,456 Goal map rows by script with about 100 read.
- **Difficulty and arcs:** each course follows its base text's unit order, which matches the progression's handoff
  notes; models move as the progression says (ten-frame K to 1, tape diagram 1 to 7, double number line 6, hanger 7);
  number ranges and algorithm grades rise grade to grade (grade 3 within 1,000 with no algorithm, grade 5 standard
  multiplication algorithm from day 60). No arc fights the progression.

## Findings, most serious first

| # | Where | What | Severity | Status |
|---|---|---|---|---|
| 1 | algebra-ii days.csv and s02 to s07 field 4 retrieval tables | The five-minute spaced openings are one rotation (expand and factor, rational rewrites, structural factoring, quadratic graph transformations) on about 117 days; 112 days tag alg1-factoring or alg1-quadratic-equations-reasoning, in every unit from 2 to 7, with only the constants changing. Unit 1 sequences return on 5 days, unit 4 logarithms on 3 (110, 112, 160), unit 6 trigonometry on 2 (158, 160). In unit 7 (inference) the openings still drill factoring while the unit's own prerequisites (sampling, spread, causation) get one retrieval each. Difficulty does not rise across the year's openings, and the harder later work is not spaced before course checks 110 to 112 and 158 to 159. A day writer will build these openings as written. | moderate | open (not raised in units-read-algebra-ii) |
| 2 | field 2 standards lines: math-grade-3 s03 (3.OA.D.8), math-grade-7 s04 (7.NS.A.2d, 7.EE.A.2), algebra-i s06 (F-IF.C.9), geometry s02 (G-SRT.B.5), algebra-ii s01 (F-LE.A.2), s02 (F-IF.B.4, A-REI.D.11) | A standard the frame gives to a later unit is listed without the begun mark and with "Parts, by verb: whole standard", although the plan's own prose (or the frame) says it is only begun here. Grade 3 s03 claims 3.OA.D.8 whole while teaching only addition and subtraction two-step stories and holding no end-of-unit item for it; grade 7 s04 scores both codes whole, and units 5 and 6 own them. A section writer reading field 2 would teach and score the whole standard twice. Algebra I's A-SSE.A.1 and F-LE.A.2 had the same fault and were fixed by a `~` in days.csv. | moderate | open (Algebra I cases fixed in units-structure-pass-math; these were not raised) |
| 3 | every math plan, generated "Progression skills owned" line (scripts/unit_skeleton.py) | The line lists every same-grade row in the unit's days.csv skills, not the frame's owned rows: grade 7 s06 lists 10 rows (it owns 3), grade 3 rows appear as owned in up to 8 units, grade 5's algorithm in 6. It also takes in other subjects' ids: math-grade-2 s06 lists ss1-saving as an owned progression skill. A writer could read a later unit as owning an earlier unit's skill. | moderate | open, known: units-read-math-grade-5 finding 9; structure pass left it for the lead (generator change) |
| 4 | data/plans/ledgers/ (no math.csv) | Math has no ledger rows. COURSE-RUN stage 2 seeds the subject ledger and stage 4 adds each unit's rows at stage planned; stage 6 day jobs are ledger-gated. ledger.py's ladder lists math, but no row exists, so unit review entries point at progression rows and days.csv instead of ledger rows. Science, ELA and social studies ledgers also stop at grade 3, so this is a process gap for the lead, but stage 5 for math cannot be gated as COURSE-RUN describes until it is seeded. | moderate | open |
| 5 | Goal maps, about 80 of 1,456 rows (most in math-grade-1, algebra-ii, geometry, math-grade-5, K) | The exit shape is the practice shape again with new numbers: grade 3 s04 day 65 (exit "tell a story for a new division expression", practice "tell both stories for one division expression"), grade 1 s02 day 36, algebra-ii s03 day 66, algebra-ii s06 day 117, geometry s06 day 117. The gate passes because the strings differ. A fresh-number exit is fair evidence, but UNIT-PLAN field 5 asks that the exit not be the day's practice again; read as a busy writer would, these days get an exit that repeats the practice task. The course reads reported every practice shape as different; this read disagrees for these rows. | minor | open |
| 6 | math-grade-3 s05 field 4; algebra-i s07 field 4 | Two assumed rows are missing from the field 4 table. Grade 3 unit 5's m3-mult-div-problems assumes m2-one-step-problems; it was last retrieved on day 54 (unit 3) and is not named for unit 5, which first uses the skill on day 79. Algebra I unit 7's alg1-vertex-form-max-min assumes m8-function-compare; the retrieval is in prose only, on day 153, a day after the row is first used (day 152), and the id is not in days.csv skills, so the table cannot see it. | minor | open |
| 7 | geometry s07, Returns line | "Unit 8, day 159": day 159 is a course-level check day (stretch C), not unit 8. | minor | open |

## Open items for a fix pass

1. Algebra II openings (finding 1): rebuild the spaced-opening rotation from unit 4 on so it mixes the year's own work
   (sequences, rational functions, complex numbers, exponentials and logarithms, then trigonometry) with the
   Algebra I factoring, and give unit 7 openings that serve its readiness rows. days.csv notes and skills, then the
   field 4 retrieval tables of s04 to s07 from a fresh skeleton.
2. Begun standards (finding 2): mark each listed code `~` on its days in days.csv, as done for Algebra I, regenerate
   field 2, and state the begun part by verb; grade 3 s03 and grade 7 s04 field 5 items then score only the begun
   part.
3. Owned line (finding 3): the lead's generator decision, already on the structure pass list; build the line from the
   frame Units Skills column and drop ids from other subjects' progressions.
4. Math ledger (finding 4): the lead decides when the math ledger is seeded (`ledger.py seed`), before any math
   stage 5 job.
5. Goal map rows (finding 5): rewrite the practice shape, never the exit, for the rows where only the numbers differ;
   a similarity listing is easy to regenerate.
6. Field 4 rows (finding 6): add m2-one-step-problems to grade 3 days.csv day 79 skills and m8-function-compare to
   Algebra I day 152 (move the day 153 retrieval to day 152), then regenerate both tables.
7. Geometry s07 Returns (finding 7): say "course-level check, day 159".

## Note on the grade 12 courses

Precalculus, statistics and calculus own 75 progression nodes (pc-, stat-, calc-) and have no unit plans, so no unit
owns those nodes yet. They are core electives, outside the 52-course core this gate approves; their stage 4 waits for
their own run. Named here so the owner's approval of the math baseline is read as K to Algebra II, with grade 4 from
its own session.

## Already fixed by the 2026-11-24 ledgers

None of the seven findings above was already fixed. Related items they did fix: Algebra I A-SSE.A.1 and F-LE.A.2
begun marks (the same fault as finding 2, in other units), and the Algebra II day 121 exp-log retrieval note (one
day, not the rotation).
