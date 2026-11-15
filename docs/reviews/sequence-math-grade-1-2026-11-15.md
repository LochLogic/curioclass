# Expert cold read: math-grade-1 scope and sequence, 2026-11-15

Reader: the curriculum expert (docs/agents/EXPERT.md), cold. Codex wrote the sequence; I did not. Subject lens
docs/agents/lenses/math.md, bar docs/RUBRIC-MATH-K8.md (never quoted, never claimed). Base text: Illustrative
Mathematics K to 5, grade 1 (S:\CurioClass-sources\illustrative-math, openly licensed pages only).

## What I read

- docs/courses/math-grade-1/scope-and-sequence.md and frame.md, in full.
- data/plans/math-grade-1/days.csv (160 rows) and source-map.csv (160 rows: 146 keep, 14 ours).
- data/progressions/math.csv, the K and grade 1 rows; data/plans/math-kindergarten/days.csv, to check that what
  grade 1 retrieves was taught.
- docs/courses/CALENDAR.md and data/plans/calendar.csv for grade 1.
- The local IM grade 1 pages: all 146 lesson titles and lesson-purpose lines, compared by script with the source map
  and with every goal cell in days.csv.
- Earlier non-codex reads: docs/reviews/sequence-science-grade-2-2026-11-14.md and
  docs/reviews/sequence-english-language-arts-grade-2-2026-11-14.md.
- Gates: `plan.py check` 0 failures (8 units, 153 unit days, 7 course-level days); `frame.py calendar` places the
  checks in weeks 19 and 30; `stale.py check` 56 files, 0 failures.

## Verdict

The order is right and the year is well aimed: all 146 IM lessons sit in IM's own order, major work is about
84 percent, 1.OA.C.6 gets spaced untimed practice all year with records more than ten days apart, and kindergarten
rows are retrieved, not readiness-checked, as the grade-number rule asks. One serious fault: 140 of the 160 goal
cells copy IM's lesson-purpose sentences word for word, which breaks "ideas only, never wording". The rest is the
band's usual observation load: unit 8 re-collects the year-end counting evidence, and two end days re-ask what
their closing windows already retained.

## Findings, most serious first

### 1. Goal cells copy IM's lesson-purpose wording (serious, firm)

LAYER base text. REPEAT new.

What is wrong: 140 of 146 base-lesson goal cells are IM's "Lesson Purpose" sentence with "The purpose of this
lesson is for students to" cut off. The cut leaves broken sentences: day 17 "...They also write an expression",
day 23 "write equations" in lower case after a full stop, day 45 "Introduce to a new type of story problem",
day 47 "...a ten. compose", day 132 "As draw the shapes and describe them". Kindergarten has one close match
(day 143) and grade 2 one (day 21); grade 1 is the outlier.

Why it matters: Curio Class takes ideas from the base text, never its wording. The licence allows reuse with
credit, but the project rule is stricter, and the broken sentences would reach the unit and day plans as written.

Fix: rewrite every grade 1 goal as one short teacher sentence in Curio Class's own words, in kindergarten's
pattern (a verb, the content, the limit), for example day 45: "Solve Add To stories with the start unknown within
10." Keep the meaning and the limits; do not paraphrase IM line by line. Then rerun the comparison script and
check that no goal shares a run of more than eight words with the IM purpose.

### 2. Unit 8 re-collects the year-end counting record (moderate, firm)

LAYER sequence. REPEAT yes (ELA grade 2 finding 1, collect once).

What is wrong: the unit 8 closing observation (days 157 to 160) collects 1.NBT.A.1 counting from a given start to
120, reading and writing numerals and matching a collection; day 157 says to "retain collection-to-numeral product
for the closing record". Day 148, the year-end check, took the same evidence child by child 9 to 12 school days
earlier.

Why it matters: a check within ten days reuses the record. The second collection takes unit 8's review time and
tells the grade 2 teacher nothing new.

Fix: day 160 reuses the day 148 record and the days 149 to 150 transfer tasks for 1.NBT.A.1. Drop the
collection-to-numeral retention line from day 157. The only new unit 8 evidence is the riddle explanations
(MP.1 and MP.3) on days 158 to 159.

### 3. End days 68 and 92 re-ask what the closing windows retained (moderate, likely)

LAYER sequence. REPEAT yes (ELA grade 2 finding 2, end days stacked).

What is wrong:
- Day 67 retains "a three-addend story and equation, reordering/regrouping explanations, ten ones as a ten and
  teen representations". Day 68 then "covers" 1.OA.B.3, 1.OA.A.2 and 1.NBT.B.2a and b again, beside the reused
  facts record: four expectations asked as fresh performances on one end day.
- Days 89 to 91 hear every child on every unit 4 skill in three 16-minute rotations. Day 92 adds "short
  independent products" for all six of the same skills one to three days later.

Why it matters: no one end day asks for full performances on two or more expectations, and the products duplicate
evidence the teacher took the day before.

Fix: day 68 names the day 67 products as the record for 1.OA.B.3, 1.OA.A.2 and 1.NBT.B.2a and b, and its short
task covers only 1.OA.C.6 parts the facts record does not (make-ten and decompose-to-ten written with an equation).
Day 92 asks in writing only for the parts an oral rotation cannot leave a trace of: comparison symbols with a
reason (1.NBT.B.3) and a recorded multiples-of-10 subtraction (1.NBT.C.6). Everything else reuses days 89 to 91.

### 4. Four-minute group observations are too short to record reasoning (low, likely)

LAYER sequence. REPEAT new.

What is wrong: days 126, 127 and 136 plan observations of six children in 4 minutes (indirect comparison, length
units, shape attributes). That is under a minute a child for an explanation.

Fix: three groups of eight at 8 minutes, each child leaving a paper product (the ordered strips, the drawn shape
with its attribute marked) the teacher reads after the lesson; or spread one group across two days.

### 5. Codes that do not match the goal (low, firm)

LAYER sequence. REPEAT new.

- Day 45 (Add To, start unknown) carries only 1.OA.C.6; add 1.OA.A.1.
- Day 52 (Take From stories) carries 1.NBT.B.2a and b; replace with 1.OA.A.1 and 1.OA.C.6.
- Day 65 (unknowns in all positions) carries only 1.OA.C.6; add 1.OA.A.1 and 1.OA.D.8.
- Day 114's goal reads "within 100 subtracting" under 1.MD.A.1. Subtraction within 100 is outside grade 1 apart
  from multiples of ten (1.NBT.C.6). Reword the goal in finding 1's rewrite as adding within 100 and comparing
  expressions within 20, and fix the codes to 1.NBT.C.4 and 1.OA.D.7.

### 6. Stale notes (low, firm)

LAYER sequence. REPEAT yes.

- The prerequisites section and "For the lead" item 3 say a kindergarten days.csv is not present to verify. It is
  now present. I checked it: it teaches every row grade 1 retrieves (K.CC.A.2 on days 106, 116 and 119; K.OA.A.5
  on days 147 to 151; K.CC.C.7 on days 36 to 44). Replace the note with that line.
- The frame gives unit 8 eleven days; it has ten. Fix the frame's table (lead's file).

### 7. Frame readiness wording is stale (low, firm)

LAYER frame. REPEAT yes (science grade 2 and ELA grade 2 across the band).

The frame still names readiness checks on units 1, 3, 4 and 6. Every row they assume was last used in
kindergarten, one grade back, so by the grade-number rule they are retrievals, which is what the sequence does.
The frame should say "retrieval", not "readiness". This is the lead's frame fix.

### 8. Source-map layout is not the band's (low, firm)

LAYER process. REPEAT yes.

The columns are base_text, base_unit, base_lesson, base_title, course_unit, day, decision, reason, source_url,
license. This is the closest of the three to sequence-write rule 8. Adopt the band layout set in the grade 2
report; here only base_text and base_unit become optional.

## Checks the brief asks for

- **Order inside each unit:** met. Each unit follows IM order; the 14 added days sit after the lessons they build on.
- **Assessments:** every end day covers every part of its codes across its window; mid-unit records in units over
  25 days; response counted once. Faults in findings 2 and 3.
- **Readiness or retrieval:** met in the sequence. All kindergarten rows are retrieved inside days. No readiness
  check is needed (no row assumed from two grades back). Frame wording stale (finding 7).
- **Checks that do not repeat:** met. Days 93 to 94 reuse the unit 4 record and draw unit 4 items from earlier
  units' contexts; days 147 to 148 reuse the unit 7 record the same way. "For the lead" item 2 asks whether this is
  the intended reading of collect once; it is, and kindergarten does the same.
- **Standards in full:** met. 1.NBT.B.2a to c and 1.OA.A.1's twelve situation cells are each carried by days.
- **Days by load:** met. Operations and place value take the long units; measurement, data and geometry units are short and
  practise counting and computation.
- **Calendar:** met. Days 93 to 94 (week 19) and 147 to 148 (week 30) are on target.
- **Candidate cells:** each settled with its day cost inside the unit.
- **Shorter path:** present, with fold-in days and nothing assessed cut. It says a 45-minute period fits;
  kindergarten says a 45-minute-only day needs the lead. See the grade 2 report's band section.
- **Source map:** every IM lesson placed, in IM order, titles match.
- **Stale notes:** gate clean; two by hand (finding 6).

## Lens checklist (scope and sequence layer)

| Line | Met? |
| --- | --- |
| Major work over the 75 percent line | Met: about 84.5 percent of minutes |
| Each topic grows from the grade before | Met: K counting and within-5 facts retrieved into within-10 and within-20 work |
| A skill taught in part with no later day that finishes it | Met: 1.OA.A.1 contributions in unit 2, owned in unit 6 |
| Problems that join units on purpose | Met: measurement and data days use place-value and story work |
| Fluency given spaced, mixed practice | Met: five-minute untimed retrieval every unit day |
| Counting checks separate from fluency checks | Met |
| Model used before the grade that builds it | Met: tape diagram named in unit 6; no number line (grade 2 builds it from the ruler) |
| A limit broken | Part: day 114 goal wording (finding 5) |
| Practices developed on purpose, tied to tasks | Met: all eight tied to named days in the practices table |
| Countdown timer shown to a child | Met: none |
| Source map row with no decision | Met |

## What is right and should not be touched

- 1.OA.C.6 fluency within 10: records on days 53 to 54, 66 to 67, 94 and 148, each more than ten days apart,
  untimed, recorded as just knows, quick strategy or counts all. This is the band's best fluency plan.
- The practices table, tying every practice to days.
- The course checks' reuse of recent unit records with items from earlier contexts.
- No number line in grade 1; the tape diagram named once in unit 6 and carried to grade 2.

## What I could not judge

- Whether 24 is the right planning class size; kindergarten and grade 2 plan for 30.
- The exact wording quality of the rewritten goals, which do not exist yet.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Rewrite all base-lesson goals in our own words | Ideas only, never wording | days.csv goal column |
| Day 160 reuses day 148 and days 149 to 150 | Collect once within ten days | days.csv days 157 to 160 |
| Day 68 and day 92 reuse their closing windows | End days not stacked; collect once | days.csv days 67, 68, 92 |
| Observations in groups of eight at 8 minutes with products | Time to hear reasoning | days.csv days 126, 127, 136 |
| Codes on days 45, 52, 65, 114 corrected | Codes match goals | days.csv |
| Course checks reuse unit records and change contexts | Intended reading of collect once | scope-and-sequence.md checks |

## For Cory

Nothing. No finding touches scope, money, people or audience.

## Sources

- Illustrative Mathematics, K to 5 Math, grade 1, lesson titles and purposes, openly licensed (CC BY 4.0), local
  copy S:\CurioClass-sources\illustrative-math. Ideas and order only.
- Common Core Standards Writing Team, Progressions: K to 5 Operations and Algebraic Thinking; K to 5 Number and
  Operations in Base Ten (draft), read for the within-10 fluency and the tens-and-ones stages.
- data/progressions/math.csv (K and grade 1 rows).

## For the source list

- None new.
