# Sequence read: science-grade-5 (Grade 5 science), 2026-11-14

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md, docs/GLOSSARY.md,
  docs/pipeline/briefs/sequence-read.md and sequence-write.md (rule 2), and the "Settled by the expert" tables of the
  social studies K to 5 sequence reads of today (not the Codex ones).
- Cold: docs/courses/science-grade-5/scope-and-sequence.md and data/plans/science-grade-5/days.csv (all 120 days).
- Beside them: docs/courses/science-grade-5/frame.md (brief, seams, units table, course-level checks), the grade 2 to 5
  rows of data/progressions/science.csv, data/standards/ngss-pe-dimensions.csv (grade 5 and 3-5-ETS1 rows),
  docs/courses/CALENDAR.md and data/plans/calendar.csv (grade 5 rows); for the band section, my grade 3 and 4 reads of today.
- Gates: `plan.py check` passes for this course (0 failures); it fails on biology, another course being written now.
  `frame.py calendar` places the checks in weeks 10, 21 and 30 with no stagger break. `stale.py check`: 56 files, 0 failures.
- For REPEAT: the non-Codex reads in docs/reviews/. I did not open any Codex read.

## Verdict

The richest of the three years: long-running evidence (weighed soil, sealed jars, a monthly shadow record from week 1)
drives real model revision, safety is careful throughout, and the balloon-buoyancy trap on day 14 is anticipated. Two
serious faults block unit plans: rule 2 is set aside for five grade 3 rows (called "content revisited" and given
retrieval), and units 2, 3, 4 and 6 assess two or three expectations, some with observed trials, on one 45-minute end
day. A moderate overreach on day 119 and two minor fixes follow.

## Findings, most serious first

### 1. Five grade 3 rows get retrieval where rule 2 needs readiness (serious; firm)

- **LAYER** sequence, frame. **REPEAT** yes (grade 4 finding 2, two rows there; the grade 3 sequence rejected this same
  exception in writing). **Confidence** firm.
- **What is wrong.** The frame's rule (lines 16 to 18: "a row from grade 3 or 4 ... opens with a retrieval task") and the
  days treat these grade 3 rows, unused in grade 4, as "content revisited":
  - s3-environment-traits (day 18) and s3-habitat-survival (day 23), unit 2;
  - s3-magnet-static (day 62) and s1-sky-patterns (day 63, last used in grade 3), unit 4;
  - s3-climates (day 85), unit 5.
  Days 17, 81 and 84 say outright "not readiness" or "No readiness for unit 5". Rule 2 gives a row last used two or more
  grades back a readiness check, with no exception.
- **Why it matters.** These rows carry the units' starting ideas (plants and environment, habitats, climate). Without the
  check the teacher learns who lacks them only when the unit's argument fails, and a writer following the frame builds
  every unit plan the same wrong way.
- **Fix.**
  - Unit 2: readiness for s3-environment-traits and s3-habitat-survival in day 17's last ten minutes; the reteach or
    extension inside day 19, as day 63 does it.
  - Unit 4: add s3-magnet-static and s1-sky-patterns to day 61's existing s1-daylight-seasons check; day 63's reteach
    covers all three. s3-balanced-forces (used in grade 4) stays retrieval.
  - Unit 5: readiness for s3-climates in day 84's last ten minutes; the reteach or extension inside day 86, not the hook day.
  - Rewrite frame lines 16 to 18 as rule 2 states it; align the seams (lines 82, 84, 88 and 91) and the progression notes;
    change the notes on days 17, 18, 23, 61, 62, 81, 84 and 85.

### 2. Four units assess two or three expectations on one end day (serious; likely)

- **LAYER** sequence. **REPEAT** yes (grade 4 finding 1). **Confidence** likely.
- **What is wrong.**
  - Day 40 (unit 2): an argument (5-LS1-1) and two models (5-LS2-1, 5-PS3-1).
  - Day 60 (unit 3): identifying an unfamiliar material from measured properties (5-PS1-3) and an observed collaborative
    fair test with three trials (5-PS1-4).
  - Day 80 (unit 4): three graph sets (5-ESS1-2) and two arguments (5-PS2-1, 5-ESS1-1).
  - Day 116 (unit 6): combining two sources (5-ESS3-1) and observed trials of two prototypes, three each (3-5-ETS1-3).
- **Why it matters.** Each pair is a full lesson on its own for ten-year-olds. The writer will cut the trials or the
  argument, and the score will claim expectations it did not see.
- **Fix (settled here, no day cost).**
  - Unit 2: day 37 folds into day 36 (day 36 takes the monthly shadow); day 37 is the soil weighing (was 38; three school
    days of drying is enough, and the jar observation moves with it); day 38 is the consensus (was 39); day 39 is Check
    end for 5-LS1-1 (argument from new plant data); day 40 is Check end for 5-LS2-1 and 5-PS3-1 (one linked model of an
    unseen ecosystem with matter and energy arrows).
  - Unit 3: day 58 folds into day 57; day 58 is the consensus (was 59); day 59 is Check end for 5-PS1-3 (new samples,
    with supplies and safety); day 60 is Check end for 5-PS1-4 (the observed fair test, as written).
  - Unit 4: day 78 folds into day 77; day 78 is the consensus (was 79); day 79 is Check end for 5-ESS1-2 (three new graph
    sets); day 80 is Check end for 5-PS2-1 and 5-ESS1-1 (two arguments).
  - Unit 6: day 114 folds into day 113; day 114 is the critique and monthly shadow (was 115); day 115 is Check end for
    5-ESS3-1 (two new sources); day 116 is Check end for 3-5-ETS1-3 (the observed runoff-catcher trials, as written).
  - Units 1 and 5 stay at one end day; the unit plan times them.
  - Each fold used here was also a shorter-path fold; the unit plan names a replacement fold in the same unit.

### 3. Day 119 asks for more than the frame's check 3 (moderate; firm)

- **LAYER** sequence. **REPEAT** new. **Confidence** firm.
- **What is wrong.** The frame's check 3 asks for "a fair test planned for an unseen prototype, with what to hold the same
  and how many trials". Day 119 has students plan and conduct three trials of each of two syringe prototypes, beside a
  5-ESS3-1 source item, in one lesson.
- **Why it matters.** It repeats finding 2's crowding on the last check of the year, and the conducted trials were
  already scored on day 116.
- **Fix.** Day 119 follows the frame: students plan (not run) a fair test of one unseen air-retaining prototype, naming
  variables held the same, the measurement and the number of trials, beside the community-sources item. Drop the syringe
  supplies from day 119.

### 4. The water shares are labelled loosely (minor; likely)

- **LAYER** sequence. **REPEAT** new. **Confidence** likely (against the USGS water-distribution table).
- **What is wrong.** Day 93 calls the 97 parts "ocean parts", but the salt-water share includes saline groundwater and
  lakes. Day 94 calls the 1 part "lakes, rivers and swamps together", but the sourced "surface and other" share also holds
  ground ice, soil moisture, the atmosphere and living things.
- **Fix.** Day 93: "about 97 salt-water parts (nearly all ocean) and 3 fresh". Day 94: "about 69 ice caps and glaciers, 30
  groundwater, and 1 surface and other fresh water (lakes, rivers and swamps among it)", with the source named on the
  table. The 5-ESS2-2 boundary (no atmosphere in assessment) stays.

### 5. The frame's calendar sentence does not match the pin (minor; firm)

- **LAYER** frame. **REPEAT** new. **Confidence** firm.
- **What is wrong.** Frame line 12 says five lessons fall "in three of weeks 8 to 10"; the stored pin gives five in weeks
  4, 7 and 10 and three in weeks 11, 17 and 24. The scope and sequence raises this itself (For the lead item 1) and follows
  the pin; check 1 still lands in week 10.
- **Fix.** Apply For the lead item 1 as its first option: rewrite the frame sentence to "five science lessons in weeks 4,
  7 and 10 and three in weeks 11, 17 and 24", and drop "the four-a-week pattern resumes after it".

## Checked and found right (do not undo)

- Reteaches avoid first days (days 2, 46, 52, 63); readiness on day 1 (s2-pieces-new-object), day 44 (three grade 2 rows)
  and day 61 (s1-daylight-seasons) is right.
- The monthly shadow record (school days 4, 24, 44, 63, 83, 104, 125, 144) is evenly spaced and starts in week 1, so
  day 80 has real seasonal data.
- Day 14 investigates lower readings rather than assuming escaped gas: the balloon's buoyancy is handled.
- Course-level checks 1, 2 and 3 match the frame's rows (except day 119, finding 3); days 43, 83 and 119 draw the
  just-assessed unit's skills from earlier units' contexts. 5-PS2-1 is in no course check, as the frame designs it.
- Check weeks 10, 21 and 30; all candidate days settled; the shorter path is named; the $30 ceiling is frame-settled.
- Sensitivity notes on water (no home-water questions) on every day that needs them.

## Lens checklist, scope and sequence layer

| Lens line | Status |
|---|---|
| Each unit's anchor is a phenomenon or design problem, not a topic | Met |
| No model used before the unit that builds it | Met (particles in unit 1 feed units 2 and 3) |
| Engineering design in a unit | Met (unit 6, 3-5-ETS1-3) |
| Equipment has a substitute or no-kit path | Met, weaker paths said plainly |
| End-of-unit task is a new case | Met |
| Three dimensions joined on the end days | Met in kind; crowded (finding 2) |
| Safety named; living things handled humanely | Met |
| Plain facts | Met; water labels (finding 4) |
| Readiness rule 2 | Missed for five rows (finding 1) |
| Check days name every owned code | Met |

## Settled by the expert

| Item | Settled as |
|---|---|
| Grade 3 rows | Readiness on days 17, 61, 84; reteach inside days 19, 63, 86; frame rule follows rule 2 |
| Unit 2 end | 37 into 36; 37 soil weigh; 38 consensus; 39 Check end 5-LS1-1; 40 Check end 5-LS2-1 and 5-PS3-1 |
| Unit 3 end | 58 into 57; 58 consensus; 59 Check end 5-PS1-3; 60 Check end 5-PS1-4 |
| Unit 4 end | 78 into 77; 78 consensus; 79 Check end 5-ESS1-2; 80 Check end 5-PS2-1 and 5-ESS1-1 |
| Unit 6 end | 114 into 113; 114 critique; 115 Check end 5-ESS3-1; 116 Check end 3-5-ETS1-3 |
| Units 1, 5 end | One day each |
| Day 119 | Plan a fair test, not run it |
| Water labels | Salt-water and "surface and other" wording, source named |
| Calendar sentence | For the lead item 1, first option |

## For Cory

None. (The frame's state-test review question is already Cory's.)

## What I could not judge

- Whether units 1 and 5 fit two expectations on one end day; the unit plan's timed task will show it.
- Whether the shorter path (90 meetings) holds every expectation at depth; the folds are named but the route is not yet
  demonstrated day by day.
- Whether bean growth and soil drying give a readable dry-weight difference in a classroom; day 38 rightly keeps
  sourced backup data.

## Across the band

**Patterns across grades 3, 4 and 5.**

- **Readiness is applied three ways.** Grade 3 follows rule 2 on its days. Grade 4 treats two grade 2 rows as kept in use.
  Grade 5 calls five grade 3 rows "content revisited". All three frames carry a rule sentence that is out of date (grade 3's
  seams, grade 4 lines 17 to 18, grade 5 lines 16 to 18). One fix for the band: each frame's brief states rule 2 word for
  word, and the progression notes for these rows say "readiness".
- **End-day load.** Grade 3 gives most expectations their own assessment day; grades 4 and 5 crowd two or three onto one.
  The settled splits bring grades 4 and 5 to grade 3's pattern without adding days.
- **Reteach placement.** Grades 3 and 5 keep reteaches off hook days; grade 4 does not (its finding 3).
- **Course-level checks.** Grade 4 re-scores unit portfolios; grade 5 day 119 re-runs trials already scored; grade 3 day 34
  under-delivers "carry out". A course check is new context, planned or done at the depth the frame names, never a
  re-scored artifact.
- **Cost ceilings.** $25 a unit in grade 3 and $30 in grades 4 and 5, each frame-settled; no change.

**Hand-offs.**

- Grade 3 force arrows to grade 4 collisions and energy: sound.
- Grade 3 fossils to grade 4 rock layers, and grade 3 weather hazards to grade 4 hazard solutions: sound (both one grade).
- Engineering: 3-5-ETS1-1 framing in grade 3, design devices and codes with 3-5-ETS1-2 comparison in grade 4, the full
  fair-test cycle with 3-5-ETS1-3 in grade 5 (day 103 retrieves the grade 4 rows): sound.
- Grade 4 energy arrows, roots and transport, water maps and design records to grade 5: consistent with grade 4's stated
  hand-offs.
- Grade 4 s2-water-where review to grade 5 water distribution (day 92 retrieval): sound.
- Grade 3 environment-traits and habitat-survival to grade 5 plant matter and ecosystems, grade 3 climates to grade 5
  Earth's systems, and grade 3 magnets and sky patterns to grade 5 gravity and sky: each skips grade 4, so each needs the
  readiness checks of finding 1.
- Grade 5 to grade 6: day 120 records particles, conserved matter, interacting systems and fair trials as retrieval needs.

## Sources

- S:\CurioClass\docs\courses\science-grade-5\scope-and-sequence.md; data\plans\science-grade-5\days.csv;
  docs\courses\science-grade-5\frame.md; data\progressions\science.csv; data\standards\ngss-pe-dimensions.csv;
  docs\courses\CALENDAR.md; data\plans\calendar.csv.
- docs\reviews\sequence-science-grade-3-2026-11-14.md and sequence-science-grade-4-2026-11-14.md (this read's companions).
- docs\pipeline\briefs\sequence-read.md, sequence-write.md; docs\agents\EXPERT.md; docs\agents\lenses\science.md;
  docs\RUBRIC-SCIENCE.md.
- USGS, "Where is Earth's water?" distribution table, from the writer's knowledge; check before the unit plan.
