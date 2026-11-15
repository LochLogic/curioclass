# Expert cold read: math-kindergarten scope and sequence, 2026-11-15

Reader: the curriculum expert (docs/agents/EXPERT.md), cold. Codex wrote the sequence; I did not. Subject lens
docs/agents/lenses/math.md, bar docs/RUBRIC-MATH-K8.md (never quoted, never claimed). Base text: Illustrative
Mathematics K to 5, kindergarten (S:\CurioClass-sources\illustrative-math, openly licensed pages only).

## What I read

- docs/courses/math-kindergarten/scope-and-sequence.md and frame.md, in full.
- data/plans/math-kindergarten/days.csv (160 rows) and source-map.csv (161 rows: 136 keep, 24 ours, 1 cut).
- data/progressions/math.csv, the K rows and the grade 1 rows that retrieve them.
- docs/courses/CALENDAR.md and data/plans/calendar.csv for kindergarten.
- The local IM kindergarten pages: every lesson title and lesson-purpose line, 137 lessons, compared row by row
  against the source map by script.
- Earlier non-codex reads for the band: docs/reviews/sequence-science-grade-2-2026-11-14.md and
  docs/reviews/sequence-english-language-arts-grade-2-2026-11-14.md (their "Settled by the expert" tables and
  "Across the band" sections).
- Gates: `plan.py check` 0 failures for the sequence and frame (8 units, 148 unit days, 12 course-level days);
  `frame.py calendar` places the checks in weeks 17 and 31; `stale.py check` 56 files, 0 failures.

## Verdict

A sound kindergarten year. The counting and cardinality line is built in the right order, major work sits at about
80 percent of planned minutes, the source map follows IM's own order with three moves the frame gives reasons for,
and K.OA.A.5 gets spaced, untimed, mixed practice from day 71 onward with a child-by-child record before grade 1.
The faults are in the observation plan, not the teaching order: one unit collects the same evidence twice, the
fluency record is taken from the first day of the fluency lessons, and the last check day asks for six expectations
at once. One day swap is needed to make unit 3's measurement arc the single arc the write-up says it is.

## Findings, most serious first

### 1. Unit 2 collects counting evidence twice (moderate, firm)

LAYER sequence. REPEAT yes (ELA grade 2 finding 1, collect once).

What is wrong: the mid-unit record on days 30 to 32 takes each child's count-out, writing 0 to 10 and
rearrangement invariance. The closing window, days 40 to 44 (day 44 note), records "count out and write 0 to 10
including zero" and "order and arrangement invariance" again, 8 to 12 school days later.

Why it matters: child-by-child evidence is taken once per assessment window, and a check within ten days reuses the
record. Hearing 30 children twice on the same skills costs the teacher about an hour of center time and adds
nothing a child has not already shown.

Fix: day 44's note reuses the days 30 to 32 record for K.CC.B.5 count-out, K.CC.A.3 and K.CC.B.4b. The days 40 to
44 window hears only what is new to the unit's second half: both comparison methods (K.CC.C.6), numeral comparison
(K.CC.C.7), one more (K.CC.B.4c) and the three sorting steps (K.MD.B.3, already reused from day 41), plus children
the mid-unit record marked as gaps. Drop K.CC.B.4a from day 44's codes; day 18 holds it and days 30 to 32 refresh it.

### 2. The K.OA.A.5 record starts before the fluency lessons finish (moderate, likely)

LAYER sequence. REPEAT new.

What is wrong: the unit 8 window, days 147 to 151, hears each child's within-5 fluency from day 147, the first of
the five IM fluency lessons (K.8.12 to K.8.16). Children heard on day 147 have had one lesson of the run; children
heard on day 151 have had five. The same window also hears count to 100 by ones and tens, which puts six children
a day at about 4 minutes each, 24 of the 25 center minutes.

Why it matters: the record is what grade 1 day 1 reads to place children. A record taken unevenly across the
teaching misplaces the earliest-heard children, and 4 minutes for two separate expectations, at 5 years old, is
too tight to tell "just knows" from "quick strategy". The lens keeps counting checks apart from fluency checks.

Fix: split the window by expectation. Hear count to 100 by ones and by tens (K.CC.A.1) on days 146 to 148, about
10 children a day at about 1.5 minutes each. Hear within-5 fluency (K.OA.A.5) on days 149 to 151, 10 children a
day at 2 minutes each, untimed, recorded as just knows, quick strategy or counts all. Day 152 reuses both, as it
already says. No day is added.

### 3. Unit 3's measurement arc is split by six shape days (moderate, likely; the expert settles the swap)

LAYER sequence. REPEAT new.

What is wrong: the frame moves IM K.7.8 and K.7.9 (weight, capacity) into unit 3 so measurement is "one arc", and
the scope and sequence and source map both say so. In days.csv the arc is days 53 to 54 (several attributes, the
endpoint error), then six shape days, then days 61 to 62 (weight, capacity). The window, days 58 to 63, also
observes comparison "by length, height, weight and capacity" from day 58, before weight and capacity are taught.

Why it matters: the move only pays if the comparisons sit together, so that "which is heavier" and "which holds
more" grow from "which is longer". As placed, the window asks about weight and capacity before they are taught.

Fix: move the K.7.8 and K.7.9 days to follow day 54, so days 53 to 56 are measurement, and the shape days
(K.3.8 to K.3.14) follow in IM order. Update source-map.csv's day column for the moved rows. The window then
observes only taught content, and day 63's note stands as written.

### 4. The year-end check's second day asks for six expectations at once (moderate, likely)

LAYER sequence. REPEAT yes (ELA grade 2 finding 2, end days stacked).

What is wrong: day 153 lists K.OA.A.3, K.OA.A.4, K.MD.A.1, K.MD.A.2, K.G.A.3 and K.G.B.4 and asks each child to
record two pairs and a partner of ten, describe and compare attributes, and identify and compare flat and solid
shapes, all in display-repair form. Day 152 carries five more codes, though it reuses the days 147 to 151 record
for two of them.

Why it matters: in a kindergarten room with one teacher, a day with six full performances per child cannot be heard
child by child; the evidence will be thin or the day will run long. No days can be added.

Fix: keep day 153's six codes but change how they are gathered. K.MD.A.1, K.MD.A.2, K.G.A.3 and K.G.B.4 become an
independent paper sort-and-mark product (cut-out pictures sorted flat or solid and by attribute, a pair circled
"longer" or "heavier"), which the teacher reads after the lesson; only the partner pairs (K.OA.A.3, K.OA.A.4) are
heard aloud, in groups of five at a table. Name the small groups in the note.

### 5. Fold-in day 27 introduces the 5-frame (low, firm)

LAYER sequence. REPEAT yes (science grade 2, fold-in days).

What is wrong: the shorter path folds day 27 (IM K.2.9) into its neighbour. That lesson introduces the 5-frame,
the year's one structured model for five-and-some, which days 44, 83 and 100 to 103 lean on.

Fix: put day 29 or day 39 (practice days) on the fold-in list instead, and keep day 27.

### 6. Stale and duplicate notes (low, firm)

LAYER sequence. REPEAT yes.

- Day 87 says "Begin spaced untimed within-five" practice; it began on day 71. Change to "Continue".
- Day 44 lists K.CC.B.4a, which day 18 owns (see finding 1).

### 7. Source-map layout is not the band's (low, firm)

LAYER process. REPEAT yes (ELA grade 2 across the band).

What is wrong: the columns are base_lesson, title, source_url, license, course_unit, day, day_stretch, decision,
reason. Grade 1 and grade 2 use two other layouts.

Fix: adopt the one layout set in the grade 2 report's "Across the band" (sequence-write rule 8's columns). Here that
means renaming title to base_title and dropping day_stretch into the note or the day column.

## Checks the brief asks for

- **Order inside each unit:** met, except unit 3's split arc (finding 3).
- **Assessments:** every window covers every part of each listed code; mid-unit record in unit 2 placed correctly
  (unit over 25 days); response counted once. Faults in findings 1, 2 and 4.
- **Readiness or retrieval:** met. Kindergarten has no grade before it, so no readiness check applies; each unit
  opens with same-year retrieval. The start-of-year check is a listening and counting inventory, not a test.
- **Checks that do not repeat:** met. Day 84 draws unit 4 skills from earlier units' content and reuses the days
  79 to 83 record; day 152 reuses days 147 to 151 and uses a new task form (display repair).
- **Standards in full:** met. Every lettered part (K.CC.B.4a to c) is carried by a day. K.CC.A.3 and K.CC.B.5 are
  staged to ten in unit 2 and finished to twenty in unit 6, as the frame says.
- **Days by load:** met. Counting and cardinality and operations take the long units; geometry and measurement
  are short and partly practise counting.
- **Calendar:** met. Checks on days 84 to 85 (week 17) and 152 to 153 (week 31), on CALENDAR.md's targets.
- **Candidate cells:** each settled, with its day cost inside the unit.
- **Shorter path:** present: a 55-minute period and a 45 plus 15 split, and named fold-in days, nothing assessed
  cut. One fold-in to swap (finding 5).
- **Source map:** every IM lesson placed in IM order; the three moves (K.3.13 first, K.7.8 and K.7.9 into unit 3,
  K.3.15 cut as an optional center day) follow the frame. All titles match IM.
- **Stale notes:** gate clean; two by hand (finding 6).
- **Wording:** one goal (day 143) is close to IM's lesson-purpose sentence; reword it in Curio Class's own words.
  Every other goal is our own sentence.

## Lens checklist (scope and sequence layer)

| Line | Met? |
| --- | --- |
| Major work over the 75 percent line | Met: 80.2 percent of minutes, 77.5 percent of days |
| Each topic grows from the grade before | Not applicable (first grade); counting stages within the year met |
| A skill taught in part with no later day that finishes it | Met: K.CC.A.3 and K.CC.B.5 finished in unit 6 |
| Problems that join units on purpose | Met: tool collections and shapes feed counting and story days |
| Fluency given spaced, mixed practice | Met: K.OA.A.5 from day 71, untimed |
| Counting checks separate from fluency checks | Part: unit 8 window joins them (finding 2) |
| Model used before the grade that builds it | Met: 5-frame and 10-frame only; no number line |
| A limit broken | Met: written numerals stop at 20; addition and subtraction within 10 |
| Practices developed on purpose, tied to tasks | Met: each window names two practices and the task |
| Countdown timer shown to a child | Met: none |
| Source map row with no decision | Met |

## What is right and should not be touched

- The counting order: one-to-one and last-number meaning, then count out, then compare, then teens as ten ones and
  some more, then count to 100. This follows the counting and cardinality progression.
- K.OA.A.5 practice is untimed, recorded as just knows, quick strategy or counts all, and spaced from day 71.
- The mid-year and year-end checks reuse recent records and change the task form; this is the band's model.
- Both-addends-unknown stories handed from unit 4 to unit 5 with a named check day (103).
- The shorter path's two minute budgets.

## What I could not judge

- Whether 25 center minutes is the real kindergarten center time in most rooms; I planned from the note.
- The "planning class of thirty" is a cautious size; grade 1 plans for 24 (see the grade 2 report's band section).

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Day 44 reuses days 30 to 32 for count-out, writing and invariance | Collect once within ten days | days.csv day 44; scope-and-sequence.md unit 2 |
| Unit 8 window split: count to 100 days 146 to 148, fluency days 149 to 151 | Fluency heard after teaching; counting kept apart | days.csv days 146 to 151 |
| K.7.8 and K.7.9 days follow day 54 | One measurement arc, window asks only taught content | days.csv days 53 to 62; source-map.csv |
| Day 153 attribute and shape evidence as a paper product | Six expectations cannot be heard child by child in one day | days.csv day 153 |
| Fold day 29 or 39 in place of day 27 | Keep the 5-frame lesson | scope-and-sequence.md shorter path |
| Day 143 goal reworded | Ideas only, never wording | days.csv day 143 |

## For Cory

Nothing. No finding touches scope, money, people or audience.

## Sources

- Illustrative Mathematics, K to 5 Math, kindergarten, lesson titles and purposes, openly licensed (CC BY 4.0),
  local copy S:\CurioClass-sources\illustrative-math. Ideas and order only.
- Common Core Standards Writing Team, Progressions for the Common Core State Standards in Mathematics: K,
  Counting and Cardinality; K to 5, Operations and Algebraic Thinking (draft), read for counting stages and the
  within-5 fluency expectation.
- data/progressions/math.csv (K rows).

## For the source list

- None new.
