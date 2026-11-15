# Sequence read: science-grade-3 (Grade 3 science), 2026-11-14

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md, docs/GLOSSARY.md,
  docs/pipeline/briefs/sequence-read.md and sequence-write.md (rule 2), and the "Settled by the expert" tables of the
  social studies K to 5 sequence reads of today (not the Codex ones).
- Cold: docs/courses/science-grade-3/scope-and-sequence.md and data/plans/science-grade-3/days.csv (all 120 days).
- Beside them: docs/courses/science-grade-3/frame.md, the grade K to 3 rows of data/progressions/science.csv,
  data/standards/ngss-pe-dimensions.csv (grade 3 and 3-5-ETS1 rows), docs/courses/CALENDAR.md and data/plans/calendar.csv
  (grade 3 rows).
- Gates: `plan.py check` passes for this course (0 failures); it fails on biology, another course being written now.
  `frame.py calendar` places the checks in weeks 9, 20 and 30 with no stagger break. `stale.py check`: 56 files, 0 failures.
- For REPEAT: the non-Codex reads in docs/reviews/. I did not open any Codex read.

## Verdict

A sound, well-built year: six phenomenon-driven units, every grade 3 expectation and its clarification cases on a day,
each end day naming all its codes, and the readiness calls right on the days. The one serious risk is the live plant
life cycle: fast-cycling plants need hand pollination and no day carries it, so the reproduction stage of 3-LS1-1 can
fail in every classroom. Two moderate fixes (two performance assessments in one 45-minute day 15; a course-level
"carry out" claim met by an image record) and three minor ones finish it.

## Findings, most serious first

### 1. The plant life cycle has no pollination day (serious; likely)

- **LAYER** sequence, frame. **REPEAT** new. **Confidence** likely (the timing is the supplier's; the need is firm).
- **What is wrong.** Day 18 sows fast-cycling plants (school day 23). These plants are self-incompatible: they set seed
  only when a class hand-pollinates flowers, usually twice, about 14 to 18 calendar days after sowing. No day names
  pollination, its tool or its allergy note. The frame also says seed is set "by about day 58"; seeds ripen about 36 to 40
  calendar days after sowing, near course days 41 to 45.
- **Why it matters.** The life cycle model (3-LS1-1) rests on the class seeing flower to seed. A writer building days from
  this sequence would leave the step out, flowers would drop with no pods, and the unit's own data would miss the stage
  the expectation names.
- **Fix.** Add ten minutes of pollination on days 27 and 29 (cotton swab or bee stick, each flower brushed, groups swap
  plants), with "pollen: check allergies first; wash hands" in safety. The unit plan sets the exact days from the
  supplier's growing calendar. In the frame, change "set seed by about day 58" to "seed ripens about course days 41 to 45".

### 2. Day 15 holds two performance assessments in one 45-minute lesson (moderate; likely)

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **What is wrong.** Day 15 assesses 3-PS2-1 (plan and carry out a fair test of balanced and unbalanced forces) and
  3-PS2-2 (observe, record and predict a motion pattern) together. Units 2 to 6 each give their expectations two
  assessment days; unit 1 alone puts two hands-on tasks in one.
- **Why it matters.** A planned and carried-out fair test is a full lesson for eight-year-olds. Squeezed beside a second
  task, either the "carry out" or the prediction is cut, and the score no longer shows the expectation.
- **Fix (settled here, no day cost).** Day 14 becomes Check end for 3-PS2-2 (a new motion pattern observed, recorded
  and predicted); day 15 keeps 3-PS2-1 alone. Day 14's practice folds into day 13. The shorter path's "13 into 14" fold is
  replaced by "5 into 4". Day 115 (3-ESS2-1 with 3-ESS2-2) is lighter, both from supplied data: leave it and let the unit
  plan time it.

### 3. Course-level check day 34 claims "carry out" but uses an image record (moderate; firm)

- **LAYER** sequence. **REPEAT** new. **Confidence** firm.
- **What is wrong.** Day 34 lists 3-PS2-1 in full, yet the bobbing weight is met as an image record with no handling, so
  no student carries out a test.
- **Why it matters.** The course check would score planning alone and report the whole expectation as checked.
- **Fix.** Students plan and carry out a short fair test at the unit 1 box or tray stations on an object not used in
  unit 1; the bobbing weight's image record serves the 3-PS2-2 prediction item, as written. Add the stations' supplies
  and safety to day 34.

### 4. Day 119's "weather-log context from another town" is vague (minor; firm)

- **LAYER** sequence. **REPEAT** new. **Confidence** firm.
- **What is wrong.** The year-end check names no town, so a writer may reuse the class's own log or pick a town too like it.
- **Fix.** Use a desert town tied to unit 4's day 71 cactus desert (for example a Sonoran desert town) whose monthly
  temperatures stay above freezing: unseen data, a contrast with the class log, and a link back to the survival unit.

### 5. Day 80's mealworm group context is weak science (minor; likely)

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **What is wrong.** Day 80 asks whether an animal survives better in a group using mealworms, which clump but show no
  clear group survival benefit a third grader can argue from.
- **Fix.** Use unit 3's flamingos (day 50), which live and breed in large flocks, with supplied evidence cards; the
  context is earlier-unit content, as the course check needs.

### 6. The frame and progression call two readiness rows "retrieval" (minor; firm)

- **LAYER** frame, progression. **REPEAT** yes (social studies grade 5 read, finding 3). **Confidence** firm.
- **What is wrong.** The frame's seams (lines 82 and 83) and the progression notes open units with "a short retrieval
  task" for sk-push-pull (last used in grade 1) and s1-sky-patterns (no use since grade 1). The days rightly give both a
  readiness check in day 1's last ten minutes. Day 1 also retrieves pushes before checking them.
- **Fix.** In frame lines 82 and 83 and the matching data/progressions/science.csv notes, change "opening with a short
  retrieval task" to "opening with a readiness check in day 1's last ten minutes (the row sat idle across grade 2)". On
  day 1, drop the push retrieval; the readiness check covers it.

## Checked and found right (do not undo)

- Every end day lists all its unit's codes (the social studies standard).
- The weather log runs two short slots every week, weeks 1 to 30; sk-weather-watch as retrieval is right because the class
  log keeps it in use all year.
- sk-reduce-impact readiness on day 81 with its reteach on day 83, not on a first day.
- All candidate days settled; every 3-LS4-4 clarification kind is covered.
- The wood frog correction on day 69 is right.
- Calendar leans and check weeks 9, 20 and 30 are correct; the $25 a unit cost is stated.

## Lens checklist, scope and sequence layer

| Lens line | Status |
|---|---|
| Each unit's anchor is a phenomenon or design problem, not a topic | Met |
| No model used before the unit that builds it | Met |
| Engineering design in a unit | Met (the magnet design problem, 3-PS2-4; weather hazard solutions, 3-ESS3-1) |
| Equipment has a substitute or no-kit path | Met |
| End-of-unit task is a new case | Met; course check 1 partly missed (finding 3) |
| Three dimensions joined on the end days | Met |
| Living things handled humanely; safety named | Met, except pollination (finding 1) |
| Readiness rule 2 | Met on the days; frame wording off (finding 6) |
| Check days name every owned code | Met |

## Settled by the expert

| Item | Settled as |
|---|---|
| Pollination | Days 27 and 29, ten minutes each; unit plan sets the exact days from the supplier |
| Unit 1 assessments | Day 14 Check end 3-PS2-2; day 15 Check end 3-PS2-1; shorter path fold "5 into 4" |
| Day 115 | Leave as one day |
| Day 34 | Short fair test at unit 1 stations on a new object; image record for the prediction |
| Day 119 context | A Sonoran desert town, above-freezing monthly temperatures |
| Day 80 context | Flamingos from unit 3 |
| Readiness versus retrieval | Readiness on day 1 as written; frame seams and progression notes follow the days |

## For Cory

None.

## What I could not judge

- The exact pollination and harvest days, which depend on the seed supplier and room temperature.
- Whether the shorter path (90 meetings) holds every expectation at depth; the folds are named but the route is not yet
  demonstrated day by day.

## Sources

- S:\CurioClass\docs\courses\science-grade-3\scope-and-sequence.md; data\plans\science-grade-3\days.csv;
  docs\courses\science-grade-3\frame.md; data\progressions\science.csv; data\standards\ngss-pe-dimensions.csv;
  docs\courses\CALENDAR.md; data\plans\calendar.csv.
- docs\pipeline\briefs\sequence-read.md, sequence-write.md; docs\agents\EXPERT.md; docs\agents\lenses\science.md;
  docs\RUBRIC-SCIENCE.md.
- Fast-cycling plant timing from the writer's knowledge of the standard growing calendar (flowering about day 14,
  pollination days 14 to 18, seed ripe about days 36 to 40); check the supplier's sheet before the unit plan.
