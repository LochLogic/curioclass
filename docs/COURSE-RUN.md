# Course run: from a subject to finished days

Draft 3, 2026-11-20. The repeatable process for building any subject, core or elective, from pre-work to finished
days. PRODUCTION-PATH.md keeps the record of why the core was planned top down. Decisions behind this process,
including course shape, dose and lanes, are logged in docs/agents/decisions/DESK-ANSWERS.md.

## Principles

- **In order.** Stage by stage, grade by grade, unit by unit. Speed never buys skipped order.
- **Quality and fewer tokens first.** A slower run that avoids rewrites is the better run.
- **Nothing claims what is not written.** A job waits until the work it builds on is written.
- **The kit is frozen while it is used.** Briefs, templates and gates change only between stages, or between grades
  in stages 5 and 6.

## 1. The flow

| Stage | Made once per | Runs in this order | Hands on |
|---|---|---|---|
| 1. Pre-work | subject | one pass | standard, approach, course list, dose |
| 2. Progression | subject | bands written, then stitched | who owns each skill, seeded ledger |
| 3. Course frames, then scopes and sequences | course | grade by grade, pilot course first | units and every day in order |
| 4. Unit plans | unit | grade by grade, unit by unit | goals with exits, practice and reviews |
| 5. Section plans, plan data and keys | unit | per grade, unit by unit, unit 1 probe first | items, answers, sources, pieces |
| 6. Days | 4 to 6 days | per grade, day by day, ledger-gated | finished, checked days |
| 7. Course finish | course | grade by grade | a signed-off course |

Stages 1 to 4 plan every grade before any section is written. Stages 5 and 6 then run as a pair, one grade at a
time: a grade's section plans, then its days, then a retool, then the next grade.

### The same five parts at every stage

1. **Make.** A writer job, built from the stage's brief and the frozen kit.
2. **Check,** in six kinds (section 3). Structure checks run first, then fresh readers.
3. **Fix.** Faults go back to the job that made them. A fault made at an earlier stage is fixed there, then swept
   (section 4). Checks re-run after the last fix.
4. **Retool.** At the stage's end, its findings go into the next stage's brief, templates and checks.
5. **Gate.** The stage closes only when its exit check passes. Scope, audience and cost decisions go to owner
   review.

## 2. The stages

### Stage 1. Pre-work (once per subject)

- **Make:** the standard in our own words and the approach; a base-text scout; the expert's lens and bar; the course
  list and course shape; the dose by band; cross-subject leans; sensitive ground.
- **Check:** standard codes are real; an expert read against sources and a second-model read; calibration (the
  expert catches at least 8 in 10 planted major faults cold); each cross-subject lean names a core skill; a
  sensitivity read where the subject needs one.
- **Fix:** one pass by the writer. Scope, audience and cost questions go to owner review.
- **Retool:** the progression brief takes the subject's lens and any new field it needs.
- **Gate:** open questions settled; calibration passed.

### Stage 2. Progression (once per subject, all grades)

- **Make:** the progression, written blind by band, then stitched; a reconcile step if older work exists; the
  subject's ledger, seeded at stage planned.
- **Check:** ownership and handoff rules; every assumed skill owned by an earlier grade, no skipped grade, and every
  cross-subject lean points to a skill taught by then; an expert cold read and a second-model read, with every
  standard placed once or excluded with a reason.
- **Fix:** one pass. A change to what a grade teaches goes to owner review.
- **Retool:** the frame brief takes the progression read's findings.
- **Gate:** progression and ledger checks clean.

### Stage 3. Course frames, then scopes and sequences (per course, grades in order)

- **Make:** the pilot course first, then each course grade by grade. Frames hold owned skills, dose, session count,
  units with reasons and the source map. Scopes and sequences hold every day in order, the checks and the calendar
  fit.
- **Check:** calendar, readiness and day-kind rules; frames read side by side through the grades; expert and
  second-model reads, with every owned skill in a unit; day counts match the dose and checks are spaced.
- **Fix:** one pass per course. After the pilot's reads and fixes, the brief is frozen for the subject.
- **Retool:** the unit brief and template take the frame findings.
- **Gate:** owner approves the subject's baseline (scope changes only).

### Stage 4. Unit plans (per course, grades in order, units in order)

- **Make:** each goal names its exit kind (produce or recognise, matching the goal's verb), a practice shape that
  differs from the exit, and review entries pointing at earlier ledger rows. Hand-backs, materials and reserved
  examples are written as data. The ledger gets the unit's rows at stage planned.
- **Check:** unit structure, with every goal holding an exit and a practice of a different shape; review entries
  point at real earlier rows and hand-backs have both ends; a fresh read across each grade's units; an expert read
  per unit. The lead reads `scripts/spacing.py <course>` (do owned skills come back after their unit?) and puts a
  skill that never returns into the fix.
- **Fix:** one fix per unit.
- **Retool:** the section brief, the day skeleton and the shape checks.
- **Gate:** one cold read from the progression down across every course, then owner approval of the baseline.

### Stage 5. Section plans, plan data and keys (per grade, units in order)

- **Make:** section cuts, then section plans a unit per job, then plan data per unit (items, wrong answers, sources,
  pieces, materials, hand-backs). In a subject's first grade, unit 1 goes all the way through days first (the
  probe).
- **Check:** plan structure, one-ask items, shape notes and cold check words; every review note matched to the
  ledger stage, with anything still planned marked "planned only"; a fresh read of the grade's plans; a fresh key
  read per unit that solves every item cold and checks facts against sources. A source page an agent could not open
  (a 403 or bot wall) is kept as "browser check", and the lead opens every such page in Claude in Chrome at the
  grade's close (standing rule, 2026-11-22).
- **Fix:** one fix job after the plan read. The key reader fixes keys and splits two-part questions itself.
- **Retool:** after the probe only; then the kit is frozen for the grade.
- **Gate:** plan read and key reads clean.

### Stage 6. Days (per grade, in order)

- **Make:** 4 to 6 days a job from the skeleton. A job starts only when its ledger gate is open, and it moves its
  ledger rows to stage written.
- **Check:** lesson structure, one-ask items, exit slot and marking time, turn-taking time, review claims and
  copied exit text; the lead's targeted check at every hand-back; at grade close, a sample read of 10 days by two
  fresh readers.
- **Fix:** small fixes go to the same writer, resumed. Faults across days go to one cleanup job at grade close,
  which also works the course's baselined gate lines down (the known debt, 4.L). After it is committed, the lead runs
  `gate.py --course <course> --record`, which writes the course's failing count to data/plans/debt.csv, so each grade
  close shows whether the debt shrank. At grade close the lead also reads `scripts/spacing.py <course>` (gaps, and
  words taught once and never used again) and logs what it finds in the grade report. The lead also adds the sample read's measures to data/plans/pass-marks.csv
  (`scripts/pass_marks.py add`: days sampled, serious faults a day, wrong keys, tokens a day; a measure not
  recorded stays blank) and moves the days' version lines (`scripts/day_version.py <course> grade-read <date>`).
- **Retool:** the grade report's findings go into the kit, and the next grade runs on the new version.
- **Gate:** pass marks met (section 5), then the next grade's stage 5.

### Stage 7. Course finish (per course)

- **Make:** the course's checks read as one assessment plan; a coherence pass over units and seams; art and voice; the tools the sections name.
  English learner supports are not made here: they are made in the lesson (APPROACH principle 9, section plan
  field 9, the day's sentence frames).
- **Check:** the cross-grade continuity pass (section 4); a whole-course cold read against the rubric, which also
  checks that every section fills field 9 and every day prints its frames (a gap goes to the fix pass); final
  sensitivity and safety reads.
- **Fix:** one fix pass.
- **Gate:** owner sign-off, then `scripts/day_version.py <course> signed-off <date>`, so each day file says it.

## 3. The six kinds of check, by stage

| Check | 1 Pre-work | 2 Progression | 3 Frames | 4 Units | 5 Section plans | 6 Days | 7 Finish |
|---|---|---|---|---|---|---|---|
| Structure | standard codes are real | ownership and handoff rules | calendar, readiness, day kinds | every goal has an exit and a different practice | one-ask items, shape notes, cold check words | exit timing, turn-taking time, review claims | all checks re-run |
| Continuity | leans point to core skills | assumed skills taught earlier; no skipped grade | frames read through the grades | reviews point to real earlier work; hand-backs have both ends | review notes match what is written | each job waits until what it builds on is written | cross-grade pass confirms every review claim |
| Content and accuracy | standard checked against sources | every standard placed once; expert and second-model reads | expert and second-model reads | expert read per unit | every item solved cold; facts checked against sources | lead check at hand-back; sample read | whole-course read against the rubric |
| Teaching | approach fits the ages | models come before use | dose and spacing of checks | exit matches the goal; practice differs | fresh read of the grade's plans | lead check; sample read | coherence across units |
| Sensitivity and safety | sensitive ground named | | | where flagged | where flagged | where flagged | final read |
| Cost | tokens for the stage | tokens for the stage | tokens per course | tokens per unit | tokens per unit | tokens per day and per minute | tokens per course |

Every reader is a fresh agent.

## 4. Fixing where the fault was made, and sweeping

Every finding is logged with two stages: the stage that found it and the stage that made it.

- **Made in this stage:** fixed by the job that made it.
- **Made in an earlier stage:** fixed in that stage's work, then swept: the same fault is looked for in every piece
  of that earlier stage not yet used. If a brief or template let it through, that tool is retooled too.

Example: a day's practice shares the exit's shape because the unit plan set it. The day and its plan are fixed (the
practice changes, never the exit), every unused unit plan is swept for the same clash, and a shape check is added
at stage 4.

At the end of a subject, the cross-grade continuity pass re-runs the ledger check across all grades and confirms
every review claim against the written day, with one fix job per grade for whatever moved.

## 5. Pass marks for every grade's days

- Serious faults under 1.0 a day.
- Wrong answer keys rare.
- Skills taught as new when an earlier grade taught them: rare.
- About 60k tokens a day or less, also reported per minute of class.
- Each grade close's measures are one row of data/plans/pass-marks.csv, shown on the Dashboard's quality panel.

Planning stages report tokens per stage, so the cost of planning each subject becomes known.
