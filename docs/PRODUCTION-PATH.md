# How a course gets made: the path as it stands, last changed 2026-11-22

The path is judged against the end goal, FOUNDATION 1 (a teacher can run any course from the first day to the last,
free, and it would stand up to a state adoption review), and the bar (quality over speed and over saved work).
Changes to existing work are allowed where they teach better. The decisions behind it are in
docs/agents/decisions/DESK-ANSWERS.md.

## 1. The answer

1. **Plan every core subject from the widest scope down, one layer at a time, before writing days.** ROADMAP's
   layers set the order: foundation, standards, approach, **progressions** (layer 4: what each grade owns, assumes
   and hands on, per subject, across all its grades), each course's frame and scope and sequence (with its map
   against the base text, where there is one), then units. Progressions and course frames are built and reviewed
   for all four core subjects together (math, ELA, science and social studies: 58 courses, 52 of them core, which
   get frames now; the 6 electives wait, see After the core subjects). Social studies then goes first through scope
   and sequence and units; the other three subjects' scopes and sequences are written together, and their units go
   one subject at a time, each reviewed from its progression down. Sections, days, lessons and tools come only after
   every core subject's units are planned and reviewed. This order replaces BASELINE rule 25 ("prove at the bottom
   before planning wider") (settled 2026-11-13, see DESK-ANSWERS). How much planning saves at the day level is not
   measured yet; the probe and the guard measure it.
2. **Test the plans against real days twice, with "on" and "off" set beforehand.** Once early, as a **probe**: a
   few days written in each subject once its units are planned, first in social studies at baseline 2, before the
   other three subjects copy the unit template. Once at the end, as the **guard**: a few days written in each
   subject once every unit is planned, before full writing starts. Each measures how far off the plans were
   (section 3, steps 4 and 7; the measures are set in P4).
3. **Learn the process on clean work first; convert old work last.** Social studies goes first because nothing of
   it had been planned, so the process is learned without bending old work into it. Science, ELA and math then move
   forward together; math's old work (a grade 4 scope and sequence, unit plans and 48 written days) is handled by
   writing blind and then reconciling, so it no longer waits for the other subjects (settled 2026-11-15, see
   DESK-ANSWERS).
4. **What crosses days goes into data, with gates, not into prose.** Hand-backs, materials, reserved examples and
   the base-text map are small CSVs that plan.py and lesson.py check against the plans and the day text (built for
   grade 4 on 2026-11-13), with a minutes-and-branches check beside them. Every subject uses them; the progressions
   use the same idea one level up.
5. **Base texts stay, for quality, where a subject has one.** IM for math, OpenSciEd for middle school science, EL
   for ELA K to 5. The gain is real but not automatic. Course order follows what teaches best: a base text's order
   is the default only where the loss check finds it at least as good for learning.
6. **A second kind of reader at each baseline, and agents in place of people.** Every reliability number is the
   model judging itself, so the expert agent was checked and strengthened first (P5), and Codex reads beside it at
   every baseline. No outside human reader is planned (settled 2026-11-14, see DESK-ANSWERS): the agent reads
   FOUNDATION 7.3 names (answer key, safety, sensitivity, the expert's text read) take those places.
7. **No spending ceiling.** Codex is used freely; be judicious with tokens, never at the cost of quality (settled
   2026-11-13, see DESK-ANSWERS).

## 2. Why this path

The path rests on the unit 4 test of 2026-11-13 (grade 4 math, days 25 to 28 on the IM base text, against days 7
to 9 of unit 2 as a control). Read safely, the base-text days came out at least as clean as the control (12 residual
problems against 13, none in the source-adapted parts) at about the same writer cost (3.6% over unit 2, inside the
day-to-day spread). Of the 26 problems only the expert caught, planning well can prevent up to about 9 (the
cross-day and stale-plan kinds); the 11 in the day itself are left to the writer and the reads whatever the plans
are. Samples are small (four test days and three control days), all judged by the same kind of model that wrote
them, and COST.md's "tokens" are probably the agent's end-of-run context size rather than billed tokens.

The numbers are in docs/reviews/pipeline-audit-2026-11-13.md, the eight unit 4 reads (cheap-d025 to d028, day-025
to day-028), the two reliability reads (reliability-u04-d025-028, reliability-u02-d007-009),
docs/reviews/plan-s04-replan-2026-11-13.md, docs/pilots/COST.md, docs/pilots/REVIEW-CADENCE.md,
data/plans/defects.csv, docs/sources/INTEGRATION-PLAN.md and docs/COURSES-STATUS.md.

## 3. The path, step by step

Where a subject has work on file it is not thrown away: it is input to the step, read against the new layer above
it (section 4).

### Pre-work (before step 1)

All pre-work is settled before step 1 starts (settled 2026-11-13, see DESK-ANSWERS).

- **P1. The social studies standard, made usable for the plan.** Option (d) of 2026-11-12 stands: C3 for skills and
  Massachusetts 2018 as the content anchor in its course order, checked unit by unit against a named few states,
  with Curio Class's own content replacing the anchor's own-state year, under the values rule (settled 2026-11-12
  and 2026-11-13, see DESK-ANSWERS; docs/reviews/social-studies-content-standard-2026-11-12.md). All five pieces
  are recorded in docs/courses/social-studies/STANDARD.md. Done 2026-11-13.
  - **P1a. The anchor.** data/standards/ma-hss-2018.txt: 997 Massachusetts 2018 ids, each with an own-words line
    (its terms allow free non-commercial copying with credit, but Curio Class pages are CC BY, so we store ids and
    our own words, as with CCSS), checked by scripts/standards.py.
  - **P1b. The course list.** data/courses.csv is redrawn to Massachusetts's order, with COURSES-STATUS rebuilt
    (Cory's yes on Desk card q-ss-course-list).
  - **P1c. The check states.** California, Tennessee and New York (California and Tennessee by ids and our own
    words only; New York for high school order). The lead names them.
  - **P1d. The replaced state-study year.** What Curio Class teaches in place of Massachusetts grade 3:
    docs/courses/social-studies/grade-3-outline.md.
  - **P1e. Psychology.** An elective, taught after the core.
  No social studies progression starts before P1a to P1d are done. Tasks set aside until a trigger are in
  data/plans/later.csv, shown on the Desk under the plan flow.
- **P2. A social studies base text.** The scout found no openly licensed social studies curriculum that fits a
  whole course, so social studies stays the clean-slate subject and science goes second
  (docs/reviews/social-studies-open-material-2026-11-13.md; the partial bases are settled on Desk card
  q-ss-partial-bases). Done 2026-11-13.
- **P3. The rule change on record.** BASELINE rule 25 is replaced by this order, and HANDOFF and ROADMAP point here,
  so no worker follows the old rule.
- **P4. The probe and guard measures, set before any plan is written.** For each probe (step 4) and the guard (step
  7): the share of day findings traced to the unit plan or above (on: about the unit 4 re-plan's level or lower;
  off: clearly higher); how many unit plans need a change; whether a change is to the template or to one unit. The
  exact thresholds are in docs/pipeline/PROBE-GUARD.md (Desk card q-probe-guard). Done 2026-11-13.
- **P5. The expert reader, made good enough for this work.** docs/agents/EXPERT.md and the briefs in
  docs/pipeline/briefs/ were built for math plans and days, so four pieces came first. Done 2026-11-13.
  - **P5a. Subject lenses** (docs/agents/lenses/): one short file per core subject the expert reads first, saying
    what good teaching of it looks like and the errors reviewers catch, with its sources read once into our own
    words.
  - **P5b. A bar for science and social studies:** docs/RUBRIC-SCIENCE.md (first draft) and the social studies
    section of docs/ADOPTION-BAR-SUBJECTS.md.
  - **P5c. Briefs for the new layers:** progression-read and frame-read.
  - **P5d. Calibration before trust.** A small test set with planted faults of known kinds (a skill owned twice, a
    handoff that skips a grade, a model used before it is taught, a standard taught in part, a values-rule miss, an
    exit that misses the goal), plus past findings whose truth is settled, read cold by the expert and by Codex.
    The line: at least 8 in 10 planted major faults caught, few false alarms, and no kind missed by both. Run 1
    (docs/reviews/calibration-2026-11-13.md): the expert caught 18 of 18 planted majors and Codex passed too; both
    are trusted for progressions, frames, scopes and sequences and unit plans (Desk card q-calibration-1).
    EXPERT.md gained a leniency rule and a severity rule. Re-run after any change to EXPERT.md or a brief; the
    re-run with fresh plantings is later.csv L10.
- **Who decides, at every review and baseline.** The expert settles item-level choices. Cory decides go or no-go
  at each baseline, at the final review and on an "off" result from a probe or the guard, and any change to scope
  (what a course or grade teaches, the course list, a subject's order).

### Step 1. Progressions for the four core subjects, then a review

One progression per subject, all its grades, kept as data with gates: data/progressions/<subject>.csv, one row per
skill, with the columns strand, grade, skill_id, standard, assumes (skill ids from earlier grades), hands_on (skill
ids the next grade assumes), model_in, model_out, words, and cross_subject.

- plan.py checks that a course's readiness items name skill ids an earlier grade owns, that every skill id is owned
  by exactly one grade, and that a carried model (number line, tape diagram, timeline, map scale) is introduced
  before a course leans on it. The gate is scripts/progression.py (inside plan.py check): ids, grades, real codes,
  every standard owned by one grade or excluded, both ends of every handoff, models handed on before use, real
  cross_subject codes, and forward cross-subject links; it notes C3 indicators in two grades, skipped handoffs and
  model gaps. A `~CODE` marks a row that starts or applies a standard another row owns.
- **Across subjects**: the cross_subject column records where one subject leans on another (graphs in grade 6
  science against grade 6 math; reading demands against ELA; timelines and number lines between social studies and
  math). A course may not lean on a skill no subject has taught by that grade. This is why all four are built
  together.
- data/sequence.csv stays as the module order (which topic follows which); the new files sit under it at skill
  level, and sequence.csv's open science errors are fixed in this step. ROADMAP layer 4's home holds the new files.
- Built from the standards and the progressions documents, with each base text's own sequence as evidence (IM K to
  12, OpenSciEd middle school, EL K to 5); the existing grades 3 to 5 math page is folded in.
- **Write blind, then reconcile** (settled 2026-11-13). Writers (docs/pipeline/briefs/progression-write.md) and the
  first read never see the subject's earlier planning. After stitching, one reconcile step
  (docs/pipeline/briefs/progression-reconcile.md) lists every difference with the old work and settles each by a
  named source, neither side winning by default, and measures the pull (how often the old work won without a
  source). Old work that loses becomes rework for its course's turn. Only the big things go to the Desk: a
  difference no source settles that moves a standard or changes what a grade teaches, or a pull that shows the old
  work steering. Order per subject: band writers, stitch, reconcile, expert and Codex reads (Codex by script,
  scripts/codex_read.py), fix.
- **Review**: the expert reads each subject cold, then one read across all four for the cross-subject column.
  Anything that changes what a grade teaches comes to Cory.

Done 2026-11-13 for all four: social studies 384 rows K to 12 (with data/progressions/social-studies-excluded.csv,
10 codes, and the band drafts in data/progressions/parts/), science 198 rows K to 11 (all 208 NGSS performance
expectations owned; grade 12 has no core course), ELA 374 rows K to 12 (all 455 grade-level codes owned once), math
305 rows K to 11 (53 (+) codes deferred to the electives). No reconcile found the old work steering (science 25
differences, old work won 19, 17 of them by a named source; ELA 18, old won 8, 5 sourced; math 43, old won 28, all
sourced). The cross-subject read's reports end with a "For the
course frames" list that step 2 takes as input (a shared calendar for same-year links, bridges budgeted as days,
the grade 12 timetable).

### Step 2. Course frames for the four core subjects, then a review: baseline 1

A course frame says what the course is: its grades, the standards and progression skills it owns, its days, its
unit list with a reason for each unit, and, where there is a base text, the source map (a section of the frame,
every base lesson placed in one of our units). The day-level data/plans/<course>/source-map.csv comes with the
scope and sequence, scripted from the source's free pages, then judged for unit edges and day counts; grade 4
math's table of 149 IM lessons is already scripted and kept outside the repo in the source store. A course frame is
the course-level summary; its scope and sequence (step 3) then sets every day in order. The 52 core courses of the
four subjects get one each (the 6 electives in these subjects wait, see After the core subjects). Scopes and
sequences already on file are read as input against the progressions, not assumed right.

Then **baseline 1**, a whole-structure review:
- every frame against its progression rows, and the frames of each subject read side by side through the grades;
- where the layers, the gates or the vocabulary need alignment or fixing;
- **the website design check**: whether the site's structure (catalog pages, topics, course and unit pages) still
  fits the hierarchy, and what changes if not. Proposals go to Cory; nothing is rebuilt during planning unless he
  says;
- a Codex read of a sample.

### Step 3. Social studies: scope and sequence for every course, then a review

Each social studies course's frame becomes its scope and sequence (every course day in order, by unit), written to
docs/pipeline/briefs/sequence-write.md: `docs/courses/<course>/scope-and-sequence.md` with one row per day in
`data/plans/<course>/days.csv` (the five day kinds in every subject; course-level check and respond days take
`stretch` = `C`). It places its days on the one school calendar, docs/courses/CALENDAR.md (school days, weeks, the
stagger rule for course-level checks across a grade), settles each "Candidate:" check-set cell and its day cost, and
reserves assessment slots without writing items or section plans. The gate is `scripts/sequence.py` (run by
`plan.py check`). The expert reads each to docs/pipeline/briefs/sequence-read.md against the progression and the
content standard P1 set, Codex reads each too, and one fix pass applies both reads. Cory's call is at the baseline,
not a yes per course.

### Step 4. Social studies: units, then a review, then the probe: baseline 2

- Every social studies unit is planned, with its cross-day files (hand-backs, materials, reserved examples, and the
  source map where a base text is used). The expert reads each.
- **The probe**: a few social studies days (one section, 3 to 5 days) are written from the unit plans and read the
  full way (writer, cheap read, expert read, fix, re-read). Measured against P4: the share of day findings traced
  back to the unit plan or above, how many unit plans need changing, and whether the unit template itself needs a
  change before three more subjects copy it.
- **Baseline 2**: a full review of social studies from the progression down, plus the probe's result. Template
  changes are made here, once, before step 5.

### Step 5. The other three subjects together: the same cycle

Step 3 runs for science, ELA and math together (settled 2026-11-14, see DESK-ANSWERS): Codex writes the 37 scopes
and sequences (scripts/codex_scopes.py). Step 4 (units, review, probe) then runs for science, ELA and math together,
after social studies' probe and baseline 2 (settled 2026-11-15, see DESK-ANSWERS), with a review from the progression
down in each subject. The probe runs in every subject: a few days each is cheap, and each subject's units can be off
in their own way.

Science 6 to 8 follows OpenSciEd's order after its loss check. ELA K to 5 and middle school science test the base
text paths that INTEGRATION-PLAN's two small trials were meant to test, so those trials fold into this step.

**Math's old work.** Math's unit plans are written blind with the other two subjects, then reconciled with the old
work. Math converts the most old work: grade 4's scope and sequence (reconciled in the 2026-11-14 run), unit plans, the
unit 4 re-plan and its source map are read against the new layers and changed where the review finds it, rather
than kept because they exist. The grade 4 source map resumes here.

### Step 6. The final review: every subject, every course

One cold read from the progressions down across all 52 core courses of the four subjects: continuity through the
grades, the cross-subject column, frames and units against their layers. Then a Codex read of a sample. This is the
last check before days.

### Step 7. Sections, days and lessons

**Superseded for running courses (2026-11-20):** sections and days now run by docs/COURSE-RUN.md, stages 5
and 6 (per grade: section plans, plan read and fix, plan data and keys, ledger-gated days, a grade-close sample,
retool). What follows is the record of how step 7 was planned before the ladder runs.

Writing starts only here, under the review cadence (step 8).

- **The guard first**: a few days in each subject written from the unit plans and read in full, measured against
  P4, before full writing. If the plans are far off, the units are corrected before the rest is written.
- Section plans stay one section ahead of writing. Days are written in course order.
- **Section boundaries come first, for every unit at once** (2026-11-16): `scripts/section_cuts.py` builds a short brief
  per course (day kinds, checks, the plan's proposed breaks), one Sonnet agent per course proposes the cuts by
  docs/pipeline/briefs/section-cuts.md (1 to 6 days, one coherent piece of learning each, no new teaching after a mid check in its
  section, investigations and writing cycles kept whole), judgement calls come up to the lead, the gates run
  (`section_cuts.py check`) and `apply` writes the days.csv `unit` column and the plan headers. Run on 216 units
  of 29 courses: 1,007 sections, none left to decide, one lead fix.
- **How section plans are authored** (planned 2026-11-16; the skeleton is built, the rest is not): a script skeleton
  per section, `scripts/section_skeleton.py` (no model; reuses `day_skeleton.py`; sidecars in
  docs/courses/<course>/section-skeletons/), filling every data field (days, kinds, checks, parts scored, source references,
  materials) and marking the judgement fields. Notes from a former one-section unit's merged plan are copied into
  each of its sections, flagged for the writer to keep or drop. Then, to keep cost down at the same quality:
  1. Codex writes a whole unit's sections in one run (shared context loaded once, handoffs seen together); capped
     at three sections a run if later sections come out weaker.
  2. The writer gets only its slice: the skeletons, that unit's plan fields, the source pages for those days, one
     short rules card and one approved example section plan.
  3. Code gates (length, fields, day numbers, em dashes, names) run before any model reads.
  4. Lens reads take the whole unit's sections at once; the fix pass patches flagged fields, never rewrites.
  5. Stable prompt parts (rules card, unit plan) come first so repeated runs reuse cached context.
  6. Claude reads on flags, a small sample, and a per-unit cohesion pass, not every section.
  The first social studies unit is the pilot: lens findings and tokens against the unit loop's numbers decide
  whether this becomes the standard path. Considered and dropped: a Haiku skeleton (a script is exact and free) and
  a Sonnet first draft before Codex (two drafters either waste the draft or anchor on it).
- Grade 4 math's 48 written days: the unit 4 days 25 to 28 hold their fixes; the six open re-read items and the
  seven backfill slips in defects.csv wait for math's units to be settled (L13). A small fix job on the other written days
  (the rebuild check of the 44 older days: rebuild, gates, one cheap print-and-screen check) may run any time.
- Each course is finished as a whole before it is called finished: course-level checks (start of year, quarterly,
  year end, each with a respond day) read as one assessment plan; a coherence pass over units and seams; English
  learner supports; claims checked against the ledger; the whole-course cold read against its rubric (for math,
  RUBRIC-MATH-K8) and ROADMAP's "What a finished course holds".

### Step 8. The review cadence (from step 7 on)

**Superseded (2026-11-20):** the checks for every stage are COURSE-RUN.md section 3; there is no per-day expert
read. Kept as the record of the earlier plan and its cost estimate.

Sections, days and lessons will use the unit plan workflow: script skeleton, Codex writes, code gates, Codex reads
every day, and Claude reads deeply on a sample and on flags (settled 2026-11-14, see DESK-ANSWERS). Its test is
shaped and run when the unit plans are done or nearly done, from what unit development teaches. Until that test
replaces it, the per-day plan below stands.

Per day: writer, cheap read, expert read, fix pass (with the re-read rule: re-read the paragraph, the seam and the
built screens changed). Per section: one fresh set read across its days and seams, then its fixes; a set read costs
about 30 to 40 percent of a per-day expert read. On the first section written, test whether the set read can stand
in for the separate cheap check of a fix pass. REVIEW-CADENCE step 3 is unchanged: the expert drops to spot checks
only when no process finding repeats from an earlier unit (19 of 26 repeated in unit 4) and expert-only findings are
about one a day; the expert agent still reads a sample. Plan as if the expert read stays on every day: about 650,000
tokens a fully read day (an estimate including the set read), which across about 13,300 days (the 105 active
courses counted on 2026-11-15; 118 are active now, so this is a floor) is about 8.6 billion, a floor. It leaves out unit-level pieces, planning, re-reads and tooling (every unit
so far has needed a lesson.py pass of 25,000 to 264,000 tokens, a recurring unit cost). Most of those day counts are
assumed until each course's frame sets them.

### Step 9. Tools

Tools stay held until days are being written; then key tools are built or rebuilt for the sections that name them,
live and verified, with print covering the rest (FOUNDATION 6.3). A key tool is never replaced by its paper path in
a finished course. Tools already live stay live as free-standing tools and claim no course coverage until a section
names them (BASELINE rule 26).

### After the core subjects

Every later subject runs by docs/COURSE-RUN.md from stage 1 (pre-work) on. The order below still stands.

First the 6 electives of the four core subjects (precalculus, statistics, calculus, earth and space science,
environmental science, psychology). Then the 49 courses of the other subjects (47 active plus the 2 shelved world
language courses): arts and music, health and PE, computer science, career and technical education, social and
emotional learning, English language development, and library and research skills; world languages stay shelved
(settled 2026-11-13, see DESK-ANSWERS). Personal finance is not a course of its own: Economics teaches it, lightly
integrated, and data/courses.csv does not flag it core (settled 2026-11-14, see DESK-ANSWERS). Where a core
progression leans on one of the later subjects (English language development with ELA; health with science), the
cross_subject column notes it for then.

**Before a new subject's scopes** (lead 2026-11-15, see DESK-ANSWERS). Every elective and every later subject passes
these before Codex writes its first scope:
1. Its data layouts are gated before any writer runs: days.csv and source-map.csv in sequence-write.md's layout,
   checked by sequence.py, and the subject's progression checked. No writer invents a column.
2. One pilot course per subject first (Codex write, both reads, fix), then the brief is frozen for the rest of that
   subject; only a finding that breaks a gate reopens it.
3. The rule 2 readiness and retrieval count runs in the scope gate (sequence.py rule2_notes) on every course, so the
   gaps show at scope stage, not at the skeleton.
4. The unit skeleton runs on the pilot course before the others are written, so its adapter needs are known early.

### People and a second reader, through all of it

- **A reader of a different model kind** at each baseline and in P5d's calibration: Codex reads cold against the
  same brief, by script with no clicks (scripts/codex_read.py), and its findings are compared with the expert's.
  Codex's weekly budget resets often and is open for large use; Pro ends 2026-11-30.
- **Reviewers are agents** (FOUNDATION 7.3). The expert agent, checked in P5, and Codex are the reviewers. The
  answer-key, safety and sensitivity agents do the content reads FOUNDATION 7.3 assigns, each cold and after
  studying its sources (docs/pipeline/briefs/sensitivity-read.md). No outside human reader is planned. Pilots are
  retired; the probe and guard replace them.

## 4. What happens to existing work

- BASELINE rule 25 is replaced by this order (P3).
- The grade 6 ELA and grade 4 science pilots, and their trigger (card q-plan-after-11-1), are retired: the probe and
  the guard take their place, and the two small base-text trials fold into step 5.
- The grade 6 ELA and grade 4 science scopes and sequences and the grades 3 to 5 math progression were input to
  steps 1 and 2 and to their subject's scope run, read against the new layers. Cory's call on any scope is at the
  baseline, not a yes per course.
- Grade 4 math's scope and sequence, unit plans (s01 to s04, s09 to s11), section plans (u04-1 to u04-4 and the
  rest), the unit 4 re-plan (days 29 to 38) with its source map and cross-day files: held, input to math's units in
  step 5 (reconciled there; rework list in L13). The cross-day files and gates are reused by every subject.
- Math unit plans, sections and days are written in step 5 with science and ELA; until then only small fixes to
  written days (not days 25 to 28).
- Section 11.1 (built, all but its tool) and its owed teacher read: held; the expert agent does that read in the
  teacher's place, and it counts toward math's finishing.
- The start-of-year check and the unit 4 readiness items (the old rule 25 exceptions): held with grade 4 math.
- Sara's list (docs/courses/NEXT-SPINES.md): input to step 2's course frames.
- The science simulations to list per unit: listed when science's units are planned.
- The Codex queue's queued builds (for example Community Plot Planner): paused with all tool work until step 9;
  Codex's budget goes to reads first.
- The 149-lesson IM table: kept in the source store for math's source map.
- Unchanged: light credit, course order by what teaches best, science 6 to 8 on OpenSciEd's order after its loss
  check, substitutes then no-kit, the expert as stand-in teacher reader, no IM login-gated material, no per-day
  `base` column.

## 5. What is not known yet

- Whether planning every unit before writing leaves few enough problems below (the probe and the guard measure it;
  planning can reach about 9 of 26 day-level problems in the unit 4 test, not the 11 in the day itself).
- The real cost of planning. Progressions cost about 1.4 to 1.6 million agent tokens a subject, reads included,
  plus Codex's own (science's reads and fix pass were about 170 thousand; its write and reconcile stages were not
  totalled); the cost of units across the 52 core courses is not yet totalled.
- How long the whole planning phase takes, so how long no new days go live. Cory accepted this (2026-11-13).
- Whether a base text helps in ELA and science as it did in math (step 5 tells).
- How well the expert reads outside math beyond the calibration set; whether its findings match a teacher's and a
  content reviewer's (only people can say).
- Whether a set read can replace any per-day read (step 8).

## 6. For Cory

No question on this path is open. Every earlier question is answered in DESK-ANSWERS.
