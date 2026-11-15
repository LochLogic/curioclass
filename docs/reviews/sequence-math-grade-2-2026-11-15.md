# Expert cold read: math-grade-2 scope and sequence, 2026-11-15

Reader: the curriculum expert (docs/agents/EXPERT.md), cold. Codex wrote the sequence; I did not. Subject lens
docs/agents/lenses/math.md, bar docs/RUBRIC-MATH-K8.md (never quoted, never claimed). Base text: Illustrative
Mathematics K to 5, grade 2 (S:\CurioClass-sources\illustrative-math, openly licensed pages only).

## What I read

- docs/courses/math-grade-2/scope-and-sequence.md and frame.md, in full.
- data/plans/math-grade-2/days.csv (160 rows, every note) and source-map.csv (160 rows: 139 keep, 14 ours, 7 cut).
- data/progressions/math.csv, the grade 1 and grade 2 rows; data/plans/math-grade-1/days.csv for the hand-off.
- docs/courses/CALENDAR.md and data/plans/calendar.csv for grade 2.
- The local IM grade 2 pages: all 146 lesson titles and purposes, compared by script with the source map and the
  goal cells.
- Earlier non-codex reads: docs/reviews/sequence-science-grade-2-2026-11-14.md and
  docs/reviews/sequence-english-language-arts-grade-2-2026-11-14.md.
- Gates: `plan.py check` 0 failures (9 units, 153 unit days, 7 course-level days); `frame.py calendar` places the
  checks in weeks 18, 19 and 29; `stale.py check` 56 files, 0 failures.

## Verdict

A strong grade 2 year in the right order: mental strategies before written ones, the ruler before the number line,
hundreds before three-digit computation, arrays before partitioned rectangles. Major work is 82.6 percent of
planned minutes, the seven cut IM lessons are all optional center or puzzle days, and grade 1 rows are retrieved,
not readiness-checked. The faults are four stacked end days and a year-end check that never asks for 2.NBT.B.5
fluency directly; both are fixed inside existing days.

## Findings, most serious first

### 1. Four end days ask for full performances on several expectations (moderate, firm)

LAYER sequence. REPEAT yes (ELA grade 2 finding 2, end days stacked).

What is wrong:
- Day 38 asks fresh for one- and two-step stories in all positions (2.OA.A.1), mixed within-100 addition and
  subtraction (2.NBT.B.5) and four two-digit addends over 100 (2.NBT.B.6); only the explanations are reused.
- Day 57 asks fresh for two-unit measurement (2.MD.A.2), length difference (2.MD.A.4) and length stories
  (2.MD.B.5).
- Day 89 asks fresh for five of its seven codes (2.NBT.A.1, A.1a, A.1b, A.3, A.4, B.8); only the day 88 counting
  record is reused.
- Day 143 asks fresh for parity with equal addends (2.OA.C.3) and arrays with equations (2.OA.C.4).

Why it matters: no one end day asks for full performances on two or more expectations. A 60-minute day with three
to six fresh performances gives thin evidence or a rushed test, and the week-before products already hold much of it.

Fix (spread over the unit's last days, no day added):
- Unit 2: retain day 37's market-inventory product as the 2.NBT.B.6 and two-step 2.OA.A.1 record. Day 38 asks
  only for mixed within-100 computation and one-step stories in the remaining positions.
- Unit 3: day 56's estimate-and-check comparison also records a two-unit measurement with its explanation
  (2.MD.A.2). Day 57 asks for length difference and length stories only.
- Unit 5: retain day 86's mental 10 and 100 product (2.NBT.B.8) and day 87's compare-and-order product
  (2.NBT.A.4) as records. Day 89 asks for the digit, zero, number-name and expanded-form parts only.
- Unit 8: retain day 136's parity-pattern explanation as the 2.OA.C.3 record (add the equal-addends prompt to it).
  Day 143 asks for arrays and their equations only, with day 142's rectangle reused.

### 2. The year-end check never asks for 2.NBT.B.5 fluency (moderate, likely)

LAYER sequence. REPEAT new.

What is wrong: 2.NBT.B.5 asks for fluent addition and subtraction within 100 by the end of grade 2. The last direct
performance is mid-year day 90 (week 18). Day 144 meets the code only through error diagnosis and connecting
drawings to written methods, and unit 9's within-100 fluency days (154 and 155) come after the check with no
record.

Why it matters: this is one of the four K to 2 fluency expectations, and the grade 3 teacher needs to know who is
fluent within 100. Diagnosing someone else's error is understanding, not fluency.

Fix: day 144 adds one independent station, about ten mixed within-100 items, untimed, where the child writes or
shows a method; the teacher reads speed and method from the paper, not a clock. Day 160's hand-off update adds a
mark for children whose day 154 to 155 work changes that record. No interview is added.

### 3. The year-end facts record is taken before the last facts teaching (low, likely)

LAYER sequence. REPEAT new.

What is wrong: the 2.OA.B.2 year-end record is taken on days 137 to 140 (week 28) and reused on day 145. Unit 9
then teaches two facts-fluency days (148 and 149) with no record update, and the hand-off goes to grade 3 from the
week 28 record.

Fix: on days 148 and 149, re-hear only the children the record marks as "quick strategy" or "counts all", in the
warm-up, and update the record for day 160's hand-off. No full-class interview.

### 4. The clock window on day 104 is not marked (low, firm)

LAYER sequence. REPEAT new.

Day 103 says to hear half the class on day 103 and half on day 104, but day 104 (a money lesson) has no observe
kind and no window note. Mark day 104 observe and copy the clock-window line into its note, or the second half of
the class will be missed.

### 5. Check days carry unit 5 response as well (low, judgment call)

LAYER sequence. REPEAT new.

Days 90 and 91 each hear 15 children for 2 minutes and also hold 10 minutes of unit 5 response groups. That is 40
teacher-led minutes in a 60-minute day. It fits if the independent tasks need no launch. Name in the note that
the response groups run first, before the independent tasks start, so the listening window is not cut.

### 6. One goal copies IM wording (low, firm)

LAYER base text. REPEAT new (grade 1 finding 1 is the serious form).

Day 21's goal is IM's lesson-purpose sentence. Other goals that keep IM's "Students ..." second sentence (days 5,
18, 20, 32, 33, 34, 42, 93, 95, 117, 151) also read as IM's purpose text. Reword them in Curio Class's own short sentence.

### 7. Frame readiness wording is stale (low, firm)

LAYER frame. REPEAT yes.

The frame still names readiness checks on units 1, 2, 3 and 5. Every row they assume was last used in grade 1, so
they are retrievals, which is what the sequence does. The lead fixes the frame's wording.

### 8. Source-map layout differs most from the band (low, firm)

LAYER process. REPEAT yes.

The columns are source, source_title, source_url, unit, days, decision, why, order_conflict, harms_learning. A
"days" range rather than one day per row also hides where a lesson lands. Adopt the band layout (below), one row
per base lesson with its single day.

## Checks the brief asks for

- **Order inside each unit:** met. The six added days (16, 26, 35, 82, 126, 128) each follow what they build on.
- **Assessments:** every end day covers every part of its codes (2.MD.D.10 both graph forms with all three
  question types; 2.G.A.3 circles and rectangles in 2, 3 and 4 shares). Response counted once. Faults in findings
  1 and 2.
- **Readiness or retrieval:** met in the sequence. Grade 1 rows are retrieved inside days; no row last used two
  grades back is assumed, so no readiness check. Frame wording stale (finding 7).
- **Checks that do not repeat:** met. Day 90 uses written tasks in earlier contexts and draws unit 5 prompts from
  earlier units; day 91 reuses the day 88 record; day 145 analyses parity and array claims in unit 1 graph and fact
  contexts instead of the unit 8 build task. The scope and sequence says so.
- **Standards in full:** met. 2.NBT.A.1a and b, and each part of 2.MD.A.1 (four tools) and 2.MD.A.3 (four units),
  are carried by named days.
- **Days by load:** met. Units 2, 5 and 7 (place value and computation) are the long ones; unit 6 spreads shapes,
  clocks and money with its windows on days 100, 103 to 104 and 110.
- **Calendar:** met. Mid-year days 90 to 91 (weeks 18 and 19), respond day 92; year-end days 144 to 145 (week 29),
  respond days 146 to 147. The science lean (plant measurement, school days 102 to 114) is met by a bridge note on
  unit 3 days.
- **Candidate cells:** each settled, with zero-day or inside-day costs and dropped items named.
- **Shorter path:** present: a 45-minute period and fold-in days (71, 80, 155 among them), nothing assessed cut.
- **Source map:** every IM lesson placed or cut, IM order kept. The seven cuts (2.1.12, 2.6.5, 2.6.10, 2.6.14,
  2.6.21, 2.8.6, 2.8.13) are IM's optional center or puzzle days; the reason holds, and the facts warm-up carries
  their practice.
- **Stale notes:** gate clean; none found by hand beyond finding 4.

## Lens checklist (scope and sequence layer)

| Line | Met? |
| --- | --- |
| Major work over the 75 percent line | Met: 82.6 percent of minutes |
| Each topic grows from the grade before | Met: grade 1 facts, within-100 and tape work retrieved where units open |
| A skill taught in part with no later day that finishes it | Met: 2.OA.A.1 one-step in unit 1, finished in unit 2 |
| Problems that join units on purpose | Met: length stories, money totals, bar-graph questions within 1000 |
| Fluency given spaced, mixed practice | Met: daily facts warm-up; written within-100 from day 30 |
| Counting checks separate from fluency checks | Met: day 88 counting record apart from facts records |
| Model used before the grade that builds it | Met: number line built from the ruler in unit 4 |
| A limit broken | Met: no standard algorithm, no within-1000 fluency claim, money without decimals |
| Practices developed on purpose, tied to tasks | Met: each end day names two practices and the task |
| Countdown timer shown to a child | Met: none; facts untimed |
| Source map row with no decision | Met |

## What is right and should not be touched

- The ruler-to-number-line order (units 3 and 4) and the clock built on halves and fourths.
- The year-long facts inventory recorded as just knows, quick strategy or counts, instead of one card set.
- Day 145's move to earlier contexts for parity and arrays; day 144's use of archived share products.
- Money in whole dollars or whole cents only, play money, no family spending.
- Day 159's embedded review observation, with no extra day.

## What I could not judge

- Whether 30 is the right planning class size (grade 1 plans for 24).
- How long ten within-100 items take a typical child; the fix in finding 2 assumes about 10 minutes.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| End-day evidence spread to days 37, 56, 86, 87, 136 | One fresh performance per end day | days.csv units 2, 3, 5, 8 |
| Day 144 adds an untimed within-100 written station | 2.NBT.B.5 fluency asked directly at year end | days.csv day 144; scope-and-sequence.md year-end |
| Days 148 to 149 update gap children's facts record | Hand-off reflects the last teaching | days.csv days 148, 149, 160 |
| Day 104 marked observe with the clock-window note | Second half of the class is heard | days.csv day 104 |
| Response groups run first on days 90 and 91 | Listening window kept whole | days.csv days 90, 91 |
| Seven optional IM lessons cut | Center and puzzle days; practice kept in warm-ups | source-map.csv |

## For Cory

Nothing. No finding touches scope, money, people or audience.

## Sources

- Illustrative Mathematics, K to 5 Math, grade 2, lesson titles and purposes, openly licensed (CC BY 4.0), local
  copy S:\CurioClass-sources\illustrative-math. Ideas and order only.
- Common Core Standards Writing Team, Progressions: K to 5 Number and Operations in Base Ten; K to 5 Operations and
  Algebraic Thinking; K to 5 Measurement and Data, geometric measurement section (draft), read for the
  ruler-to-number-line order and the 2.OA.B.2 and 2.NBT.B.5 fluency expectations.
- data/progressions/math.csv (grade 1 and grade 2 rows).

## For the source list

- None new.

## Across the band

Patterns across math kindergarten, grade 1 and grade 2, and the hand-offs between them.

**Readiness is counted right in all three.** Kindergarten has no prior grade; grades 1 and 2 retrieve one-grade-back
rows inside days and run no readiness checks. Both the grade 1 and grade 2 frames still say "readiness" where the
sequence (correctly) retrieves. The lead fixes the frames' wording, as in the science and ELA band reads.

**The hand-offs hold.**
- K to grade 1: kindergarten's days teach every row grade 1 retrieves, and the K.OA.A.5 record (K days 147 to 151)
  is what grade 1 day 1 reads. Grade 1's note that kindergarten days are missing is stale.
- Grade 1 to grade 2: the 1.OA.C.6 record (grade 1 day 148) feeds grade 2's facts inventory; the tape diagram named
  in grade 1 unit 6 is retrieved in grade 2 unit 1; grade 1 has no number line and grade 2 builds it from the ruler.
- The fluency chain runs K.OA.A.5 (within 5), 1.OA.C.6 (within 10), 2.OA.B.2 (from memory within 20) and
  2.NBT.B.5 (within 100), all untimed, all recorded as just knows, quick strategy or counts all. Its one gap is
  grade 2's year-end 2.NBT.B.5 evidence (finding 2), and in kindergarten the record starts too early (K finding 2).

**Collect once is the band's main fault, again.** Kindergarten unit 2 hears the same skills twice within twelve days;
grade 1 unit 8 re-collects the year-end counting record; grade 1 days 68 and 92 and grade 2 days 38, 57, 89 and 143
re-ask or stack performances on end days; kindergarten's day 153 asks six expectations at once. Kindergarten's own
pattern (a five-day window ending on the end day) is the model; grades 1 and 2 should spread their end days the same
way.

**Source-map layouts differ in all three.** One layout for every math course, from sequence-write rule 8:
base_lesson, base_title, course_unit, day, decision, reason, source_url, license (one row per base lesson, one day
each). Kindergarten renames title and drops day_stretch; grade 1 makes base_text and base_unit optional; grade 2
renames four columns and splits its day ranges.

**Goals copied from IM in grade 1 only.** Grade 1's 140 copied goals are the one serious finding in the band; a
handful of grade 2 goals and one kindergarten goal need the same rewrite.

**Shorter-path budgets disagree.** Kindergarten offers a 55-minute day or 45 plus 15 and says a 45-minute-only day
needs the lead; grades 1 and 2 say 45 minutes fits. The lead should set one band rule (I suggest kindergarten's: 55
minutes, or 45 plus a 15-minute block, with 45-only as a lead call), matching ELA's "match kindergarten" settlement.

**Planning class sizes disagree.** Kindergarten and grade 2 plan observation budgets for 30 children, grade 1 for 24.
Pick one (30, the cautious size) so minute budgets compare across the band.

**Review units carry an embedded observation.** Kindergarten unit 8, grade 1 unit 8 and grade 2 unit 9 each observe
inside the review unit, against the frames' "no assessment" wording, and each notes that brief rule 2 supersedes it.
The sequences are right; the frames' wording is the lead's fix.
