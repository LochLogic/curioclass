# How a course gets made: the path forward (2026-11-13)

Draft for Cory. Asked 2026-11-13: fold the unit 4 reliability review into the pipeline audit and give one firm
"best path forward", judged against the end goal (FOUNDATION 1: a teacher can run any course from the first day to
the last, free, and it would stand up to a state adoption review) and the bar (quality over speed and over saved
work). Changes to existing work are allowed where they teach better.

Evidence, all in the repo: docs/reviews/pipeline-audit-2026-11-13.md (the audit), the eight unit 4 reads
(cheap-d025 to d028, day-025 to day-028), the two reliability reads (reliability-u04-d025-028 and
reliability-u02-d007-009), docs/pilots/COST.md (all token numbers), data/plans/defects.csv, and Cory's answers in
docs/agents/decisions/DESK-ANSWERS.md. Sample sizes are small (four test days, three control days); every claim
below says how sure it is.

## 1. The answer in one page

1. **Work from the widest scope down, and finish one course before starting the next.** Plan a course top-down
   (scope and sequence, units, sections, day rows), then write and read days in order. Ten of the 26 problems the
   expert reads found on the unit 4 days, and 2 of the 12 left after the fix pass, were decided above the day
   (what comes when, what each day hands on, which materials exist). A day writer cannot see those; a section plan
   can. (Firm on direction, n is small.)
2. **The section plan grows three short ledgers**, because that is where those problems live: a materials ledger
   (what is in each envelope or on each sheet, day by day), a hand-back ledger (what each day sends on, to which
   day, in which minutes), and a tool-round map (which tool rounds belong to which day). This is the one new piece
   of upstream work. (Firm.)
3. **Base texts stay, as a quality lever, brought in at the plan, not at the day.** The adapted parts carried no
   residual problem; every expert said the source helped or was neutral and nothing was lost; writing cost was the
   same as without a source (within noise). They did not cut review cost. So a base text is read when a course and
   its sections are planned (a source map per course), and the day writer gets a plan that already chose. (Firm on
   quality and cost; plan-time use is the audit's design, tested next in unit 8.)
4. **Course order is whatever teaches best.** Where a base text exists its order is the starting frame, kept unless
   the loss check finds something better for learning (science 6 to 8 takes OpenSciEd's order). Grade 4 math keeps
   its approved order: 44 days are written against it and no read found it harming learning. (Cory's rule; firm.)
5. **Every day is still read twice, and every fix is now re-read.** The expert read still finds about six problems
   a day the cheap read misses, so it stays on every day. New: a fix pass is followed by a cheap re-read of only
   what changed, its seams and its built screens, because fix passes made 3 of 12 and 6 of 13 of the problems left
   at the end. A set read per section is the last check. (Firm.)
6. **The days are reliable at the end of this process.** After both reads and a fix pass: no blocker and no wrong
   key in either set, every day teachable tomorrow with no prep, about 3 to 4 problems a day left, nearly all minor. The
   base-text set was at least as clean as the control. (Firm for these seven days; fair for the method.)

## 2. What the measurements say

### Reliability at the end (same brief, fresh reader, both sets fixed)

| | Unit 4 days 25 to 28 (base text) | Unit 2 days 7 to 9 (control, no base text) |
|---|---|---|
| Residual problems | 12 (3.0 a day) | 13 (4.3 a day) |
| Blocker / major / minor | 0 / 1 / 11 | 0 / 2 / 11 |
| Made by the fix pass | 3 | 6 |
| In source-adapted parts | 0 | (no source) |
| Teachable tomorrow, no prep | 4 of 4 | 3 of 3 |
| Keys reworked by hand | all right | all right |

Both sets were read from pages built after today's builder pass. The test set's fix pass was today's, with eight
reads behind it; the control's was the day before, under an older brief. The units differ (fractions against number
patterns) and the sets are small, so "at least as clean" is the safe reading, not "cleaner".

### Cost per fully read and fixed day (tokens, COST.md)

| | Unit 3 | Unit 4 test |
|---|---|---|
| Writer | 180,700 | 201,000 |
| Cheap read | 117,700 | 116,500 |
| Expert read | 194,700 | 190,200 |
| Fix pass share | about 13,500 (lead only) | about 64,000 |
| Total | about 540,000 (audit) | about 572,000 |

The writer was 3.6% over unit 2 (194,100), inside the plus or minus 20% day-to-day spread. The set reliability
read cost about 56,000 a day. The course-wide builder pass (263,597) is a once-only cost.

### Where the expert-only problems came from (unit 4, 26 problems)

| Where decided | Count | Examples | What prevents it |
|---|---|---|---|
| Above the day: sequence, seams, plan drift | 7 | the day 26 tool path ran into day 27's wholes; a day 28 hand-back used day 32's worked pair; the day 29 hand-off had no example of the right kind; u04-1 fields out of date | the hand-back ledger and tool-round map; a plan.py check that plan fields match the day rows |
| Above the day: materials | 3 | the day 25 hand-back needed twelfth-pieces not in the envelope; day 26 reprinted a strip sheet; a reteach needed eight fourth-pieces | the materials ledger |
| The builder (lesson.py) | 7 | display Asks after their answers; no warm-up screen; slips clipping the credit; no way to draw rings | fixed once, course-wide, 2026-11-13 |
| The day itself | 9 | a challenge stem and its teacher line disagreed; "quickly" never modelled; an Ask answered by printed labels | the writer and the reads (about 2.3 a day) |

Classification is the lead's, from the four expert reports, finding by finding (section 6).

### The go rule set before the test

Writer within 10% of unit 2: passed (+3.6%). No rights finding: passed (one wording echo, fixed). Expert-only at 3 a
day or fewer: not met (6.5 a day). Read honestly: the base text did not make the reads cheaper, and that was never
its main job. Seven of the 26 were builder faults now fixed for every course, and ten sit in the plan layer, which
is why the next change is upstream.

## 3. The path, step by step

### Step 1. Close the unit 4 test (now, running)

The 25 reliability fixes (both sets) are being applied with a re-read of each fix's sentence, seam and screens.
Then a cheap re-read of what changed. This is also the first run of the new re-read step.

### Step 2. Add the three ledgers and the source map (small, once)

- **Section plan ledgers** (UNIT-PLAN.md template, then each section plan): materials by day; hand-backs (from,
  to, what, minutes); tool rounds by day. plan.py checks that each hand-back lands in a day row with minutes for it
  and that each materials use appears in the ledger.
- **Source map** (data/plans/<course>/source-map.csv), one row per base lesson: source id, standards and goals
  (scripted from IM's prep files), our unit and days, keep / split / merge / cut / ours, leans to cut. A `base` cell
  in days.csv points each day at its source parts.
- **IM-TO-DAY card** (docs/sources/): how an IM lesson's parts become our parts (launch and explore become teaching
  first for grades 2 to 5; what to cut). Decided once, not every day.
- **IM's login-gated files** (cool-downs, assessments, teacher guides), once Cory signs in: they feed the source map
  and the exit and assessment design as evidence of what each lesson checks.

### Step 3. Continue grade 4 math in order

- **Unit 4 section 2 onward (days 29 to 38)** goes ahead now: its plan exists, the order is fixed, the base text
  passed. Add the three ledgers to u04-2 to u04-4 first, then write, read and fix as in step 5.
- **The unit 8 base-text-first test** (approved, kept small): plan unit 8 from the source map with the ledgers,
  write three days, same reads plus one set read on the unfixed days. It answers two things at once: does planning
  against the source cut expert-only problems, and can a set read on a section stand in for some per-day expert
  reads. About 2 million tokens.
- Then units 5 to 8 and 12 to 18 under what unit 8 shows. Grade 4 math is the first finished course.

### Step 4. Frames for the other courses (one batch, while days stay depth-first)

Scope and sequence plus source map for every base-text course (math K to 3, 5 to 8, Algebra 1, Geometry,
Algebra 2; ELA K to 5; science 6 to 8 redrawn to OpenSciEd's 18 units), each read cold by the expert. Courses with
no base text take the same frame from references (order, unit size, anchors), never copied. This gives the
105-course plan real sizes and catches order problems before any day is written. OpenSciEd and EL need a
once-per-unit extract from their PDFs (a scripted job).

### Step 5. The review cadence, from now

Per day: writer, cheap read, expert read, fix pass, then a cheap re-read of what the fix pass changed. Per
section: one set reliability read across its days and seams, then its fixes with the same re-read. The expert
read drops to one day in five only when expert-only problems fall to about one a day (REVIEW-CADENCE step 3); unit
8 is the first chance to see that.

### Step 6. Bring the written days up to the same bar (existing work, adjusted)

The 44 grade 4 days written before today have not had the builder fixes checked against them by a reader, nor the
re-read step, and the control set shows about 0.7 major problems a day left, both in the feedback loop around
judged work (what comes back to students, what they fix against), which the hand-back ledger partly covers. Before grade 4 math is called finished: one set reliability read per
section over those days, its fixes, and the re-read. About 56,000 tokens a day for the read (about 2.5 million for
44 days) plus fixes. Scheduled as the course's finishing pass, not now.

### Step 7. People (FOUNDATION 7.3)

The expert agent stands in as the teacher reader for now (Cory 2026-11-13). The writer and the reader are the same
kind of model, so a shared blind spot would not show in any number above. FOUNDATION still requires a working
teacher's read, a taught run and three timed students before a course is called finished; that requirement stays,
and the 11.1 pack already sent is the first comparison point when it returns.

## 4. What changes in existing work

- UNIT-PLAN.md gains the three ledgers; s04 sections 2 to 4 gain them before their days are written.
- Day writers stop reconciling a finished plan against a source: the plan carries the source choice.
- The fix pass brief gains "re-read the paragraph, the seam and the screens"; a re-read agent follows each pass.
- Grade 4's written days get a finishing pass (step 6).
- Nothing already decided by Cory changes: grade 4 order, light credit, science 6 to 8 on OpenSciEd's order,
  substitutes then no-kit, our own tools as simulations when tools are unheld.

## 5. What is not known yet

- Whether planning from the source map cuts expert-only problems (unit 8 test).
- Whether a set read can replace some per-day expert reads (unit 8 test).
- Whether the expert's findings match what a real teacher would flag (11.1 teacher read).
- Real cost of planning (never measured; the unit 8 test measures it).
- Full-catalogue cost: at about 650,000 tokens a fully read day (572,000, plus about 56,000 for the set read and
  a re-read not yet measured), about 13,300 days would be about 8.6 billion tokens before cadence savings. An estimate on assumed day counts for 49
  courses; it sets scale, not a budget.

## 6. Appendix: the 26 expert-only problems by where they were decided

| Day | Finding (expert report number) | Where decided |
|---|---|---|
| 25 | 1 twelfth-pieces not in the envelope | materials |
| 25 | 2 second strip sheet | materials |
| 25 | 3 challenge teacher line against its stem | day |
| 25 | 4 seating line after the teaching | day |
| 25 | 5 At home 1/4 on the fifths example | day |
| 25 | 6 Ada's lines at two scales | builder |
| 25 | 7 u04-1 field 8 out of date | above the day |
| 26 | 1 tool path runs into day 27 | above the day |
| 26 | 2 no figure can show a ring | builder |
| 26 | 3 butter round reason unanswered | day |
| 26 | 4 readiness reteach needs eight fourth-pieces | materials |
| 26 | 5 T26-6 key read as multiplication (unit 6) | above the day |
| 26 | 6 scoop lost its reason for a second way | day |
| 26 | 7 Lou's tool screen on the paper path | builder |
| 27 | 1 error A hand-back in the wrong form | above the day |
| 27 | 2 Ask answered by printed labels | day |
| 27 | 3 exit slip clips the credit | builder |
| 27 | 4 no screen for "one sum at a time" | builder |
| 27 | 5 u04-1 fields 1, 5, 8 drift | above the day |
| 27 | 6 challenge "every way" never ends | day |
| 27 | 7 "Facts group." on the class sheet | day |
| 28 | 1 no warm-up screen | builder |
| 28 | 2 "quickly" taught only by ones | day |
| 28 | 3 day 29 hand-off unchecked | above the day |
| 28 | 4 no room for fraction answers | builder |
| 28 | 5 hand-back spends day 32's pair | above the day |

Totals: above the day 7, materials 3, builder 7, day 9.
