# How a course gets made: the path forward (draft 5, 2026-11-13)

For Cory. Asked 2026-11-13: fold the unit 4 reliability review into the pipeline audit and give one firm "best
path forward", judged against the end goal (FOUNDATION 1: a teacher can run any course from the first day to the
last, free, and it would stand up to a state adoption review) and the bar (quality over speed and over saved work).
Changes to existing work are allowed where they teach better.

**How this was checked.** Draft 1 was read by a fresh agent that recomputed every number from the sources and
attacked the logic ("not sound as is; sound with changes"). Drafts 2 and 3 took two more rounds of fixes. Draft 4
added Cory's decisions of the morning of 2026-11-13 and the layer above the course, and was cold-checked again.
**Draft 5 (this one) replaces the path with the build order Cory set later the same day** (DESK-ANSWERS,
"the build order for the core subjects"), after two rounds of assessment in chat: every core subject is planned
top down: progressions and course frames across all four subjects together, then scope and sequence and units
subject by subject, before any more days are written. Sections 1 and 3 to 6 are rewritten; section 2 (the unit 4
evidence) keeps its numbers, with its references and two sentences updated. What the checks corrected is listed in
section 7, so nothing was quietly folded in.

Evidence, all in the repo: docs/reviews/pipeline-audit-2026-11-13.md, the eight unit 4 reads (cheap-d025 to d028,
day-025 to day-028), the two reliability reads (reliability-u04-d025-028, reliability-u02-d007-009),
docs/reviews/plan-s04-replan-2026-11-13.md, docs/pilots/COST.md, docs/pilots/REVIEW-CADENCE.md,
data/plans/defects.csv, docs/sources/INTEGRATION-PLAN.md, docs/COURSES-STATUS.md, and Cory's decisions in
docs/agents/decisions/DESK-ANSWERS.md. Samples are small: four test days and three control days, all judged by the
same kind of model that wrote them.

## 1. The answer

1. **Plan every core subject from the widest scope down, one layer at a time, before writing days.** ROADMAP's
   layers set the order: foundation, standards, approach, **progressions** (layer 4: what each grade owns, assumes
   and hands on, per subject, across all its grades), each course's frame and scope and sequence (with its map
   against the base text, where there is one), then units. Progressions and course frames are built and reviewed
   for all four core subjects together (math, ELA, science, social studies: 58 courses since the 2026-11-13 social studies redraw, 52 of them core); scope and sequence and
   units then go one subject at a time, each reviewed from its progression down. Sections, days, lessons and
   tools come only after every core subject's units are planned and reviewed. This replaces BASELINE rule 25
   ("prove at the bottom before planning wider"; Cory, 2026-11-13). Cory's reasoning, in chat: well-made units in a sound
   progression leave fewer problems below, and fixing back up the chain is a cost that cannot be avoided anyway.
   (Likely: the plan-time read of unit 4 caught 11 cross-day problems, 9 of them in the 10 planned days, before writing; how much it saves at the day
   level is not measured yet, which is what the probe and the guard are for.)
2. **Test the plans against real days twice, with "on" and "off" set beforehand.** Once early, as a **probe**: a
   few days written in each subject once its units are planned, first in social studies at baseline 2, before the
   other three subjects copy the unit template. Once at the end, as the **guard**: a few days written in each
   subject once every unit is planned, before full writing starts. Each measures how far off the plans were
   (section 3, steps 4 and 7; the measures are set in P4).
3. **Learn the process on clean work first; convert old work last.** Social studies goes first because nothing of
   it has been planned (no scope and sequence, no plan), so the process is learned without bending old work into
   it. Math goes last, because it holds the most old work (a grade 4 scope and sequence, unit plans and 48 written
   days) and gets every lesson learned before that conversion.
4. **What crosses days goes into data, with gates, not into prose.** Hand-backs, materials, reserved examples and
   the base-text map are small CSVs that plan.py and lesson.py check against the plans and the day text (built for
   grade 4 on 2026-11-13). Every subject uses them; the progressions use the same idea one level up.
5. **Base texts stay, for quality, where a subject has one.** IM for math, OpenSciEd for middle school science, EL
   for ELA K to 5. They did not change cost in the unit 4 test, and two experts named something the source offered
   that our day did not carry, so the gain is real but not automatic (section 2). Course order follows what teaches
   best: a base text's order is the default only where the loss check finds it at least as good for learning.
6. **People and a second kind of reader at each baseline.** Every reliability number here is the model judging
   itself. There are no people yet (Cory, 2026-11-13), so the expert agent is checked and strengthened first (P5)
   and Codex reads beside it at every baseline; qualified people are added when found, and nothing is called
   finished without them (FOUNDATION 7.3).

## 2. What the measurements say

(The unit 4 evidence the path rests on. Numbers as in draft 4; references and two sentences updated.)

### Reliability at the end (same brief, fresh reader, both sets fixed)

| | Unit 4 days 25 to 28 (base text) | Unit 2 days 7 to 9 (control, no base text) |
|---|---|---|
| Residual problems | 12 (3.0 a day) | 13 (4.3 a day) |
| Blocker / major / minor | 0 / 1 / 11 | 0 / 2 / 11 |
| Made by an earlier fix pass | 3 | 6 (one was the lead's own edit the same day) |
| In source-adapted parts | 0 (adapted share of each day not measured) | no source |
| Teachable tomorrow, no prep | 4 of 4 (day 26 on the paper path, with triage when several reteach groups hit) | 3 of 3 |
| Keys reworked by hand | all right | all right |

Both sets were read from pages built after the same day's builder pass. The test set's fix pass ran under today's
brief after eight reads; the control's ran a day earlier under an older one. The units differ (fractions against
number patterns). So the safe reading is "at least as clean", not "cleaner". The one unit 4 major is a time budget:
five possible reteach branches in a 5-minute slot.

### Cost per fully read and fixed day (tokens, COST.md)

Like for like (writer, cheap read, expert read, fix pass; unit-level pieces left out of both):

| | Unit 3 | Unit 4 test |
|---|---|---|
| Writer | 180,700 | 201,000 |
| Cheap read | 117,700 | 116,500 |
| Expert read | 194,700 | 190,200 |
| Fix pass share | 13,500 (lead only; section agents not measured) | 64,200 |
| Total | about 506,600 | about 572,000 |

The difference sits almost all in the fix share, and unit 3's was under-measured. The writer was 3.6% over unit 2
(194,100), inside the day-to-day spread of about 20%. A set read cost 56,000 a day (unit 4) to 78,600 a day (unit
2). Every unit so far has also needed a tooling pass on lesson.py (25,000 to 264,000), so treat that as a recurring
unit cost, not a one-off. COST.md's "tokens" are the agent's own figure, probably its end-of-run context size rather
than billed tokens.

### The go rule set before the test

| Criterion | Result |
|---|---|
| Writer within 10% of unit 2 | Passed (+3.6%) |
| No rights finding | Passed (one wording echo of the source, fixed) |
| Expert-only at 3 a day or fewer | Not measurable: unit 4's experts tagged every missed finding expert-only, where earlier units split "missed" from "expert only". Like for like, missed per day was 6.5, the lowest of any unit with a cheap read (unit 1 7.8, unit 9 7.0, unit 3 8.2, unit 2 10.7) |

Cory answered the mixed result on 2026-11-13: re-plan unit 4 sections 2 to 4 first; the unit 8 test is dropped
unless unit 4's result is unclear.

### What the 26 expert-only problems were (reclassified after the check)

| Kind | Count | Prevented by |
|---|---|---|
| Across days: sequence, hand-backs, reserved examples (d26 1; d27 1; d28 3; d28 5) | 4 | the cross-day CSVs |
| Across days: materials (d25 1; d25 2; d26 4); d25 1 and d26 4 were visible to the day writer | 3 | the materials CSV |
| Plan documents gone stale against the days (d25 7; d27 5) | 2 | a plan.py check that plan fields match the day rows |
| Builder and display (d26 2; d27 3; d27 4; d28 1; d28 4; d26 7) | 6 | lesson.py; five fixed course-wide on 2026-11-13, and the reliability read then found two more |
| The day itself (d25 3, 4, 5, 6; d26 3, 5, 6; d27 2, 6, 7; d28 2) | 11 | the writer and the reads |

The audit found only about 6% of earlier findings in the plan layer; here the cross-day share is higher because
this unit's plan predates the source and fits it worst. Read honestly, this table says planning well can prevent
up to about 9 of these 26 (the cross-day and stale-plan rows); the 11 in the day itself are left to the writer and
the reads whatever the plans are. The probe and the guard (steps 4 and 7) measure whether that holds.

## 3. The path, step by step

Where a subject has work on file it is not thrown away: it is input to the step, read against the new layer above
it. On file today (COURSES-STATUS): scopes and sequences for grade 4 math (approved), grade 6 ELA and grade 4
science (drafts waiting for Cory's final yes); grade 4 math's unit plans and 48 written days; the grades 3 to 5
math progression page.

### Pre-work (before step 1; Cory, 2026-11-13: "should be a solved issue before the plan gets started")

- **P1. Make the social studies standard usable for the plan.** The decision stands (Cory, 2026-11-13): option
  (d) of 2026-11-12, C3 for skills and Massachusetts 2018 as the content anchor in its course order, checked unit by
  unit against a named few states, with Curio Class's own content replacing the anchor's own-state year, under the
  values rule (DESK-ANSWERS 2026-11-12; docs/reviews/social-studies-content-standard-2026-11-12.md). The decision is
  sound; what is missing is the material a progression is built from. Five pieces:
  - **P1a. Load the anchor.** data/standards/ holds only C3. Load the Massachusetts 2018 standards as ids with an
    own-words line each (its terms allow free non-commercial copying with credit, but Curio Class pages are CC BY,
    so we store ids and our own words, as with CCSS), one file, gated like the others.
  - **P1b. Redraw the course list.** data/courses.csv still holds the California-order list (grade 4 state
    history, grade 8 to 1877, and so on). Redraw the 14 courses to Massachusetts's order (about 8 change), with
    COURSES-STATUS rebuilt. The list is scope: the redraw goes to Cory as one table for a yes.
  - **P1c. Name the check states.** "A named few" is not named yet. Recommended in the paper's own terms: the
    strongest sets with usable terms or a matching order (New York for high school order; California and Tennessee
    by ids and our own words only). The lead names them; recorded with P1b.
  - **P1d. Design the replaced state-study year.** What Curio Class teaches in place of Massachusetts grade 3 (a
    short outline with its standards and sources), so the grade 3 progression rows have content.
  - **P1e. Psychology and electives.** The APA high school psychology standards are cited but not loaded; load ids
    and own words, or mark psychology (an elective, not flagged core) for after the core.
  No social studies progression starts before P1a to P1d are done.
  **State 2026-11-13: all five done (P1b on Cory's yes, Desk card q-ss-course-list).** All
  five are recorded in docs/courses/social-studies/STANDARD.md (anchor file data/standards/ma-hss-2018.txt, 997 ids
  with our own words, checked by scripts/standards.py; check set California, Tennessee and New York; grade 3 outline
  docs/courses/social-studies/grade-3-outline.md; psychology after the core). Tasks set aside until a trigger are
  in data/plans/later.csv, shown on the Desk under the plan flow.
- **P2. A social studies base text.** Scout for an openly licensed social studies curriculum whose licence lets us
  adapt it (some open material bars commercial use; each licence gets a verdict, light rigor). If one fits, it is
  loaded to the source store and used like IM. If none fits, social studies stays the clean-slate subject, and
  science goes second so the base-text lessons are learned before math. **Done 2026-11-13: none fits a whole
  course, so science goes second** (docs/reviews/social-studies-open-material-2026-11-13.md; partial bases and two
  licence calls on Desk card q-ss-partial-bases).
- **P3. The rule change on record.** BASELINE rule 25 is replaced by this order, and HANDOFF and ROADMAP point
  here, so no worker follows the old rule.
- **P4. The probe and guard measures, set now, before any plan is written** (the lead's addition, agreed in chat as
  part of the probe). For each probe (step 4) and the guard (step 7): the share of day findings traced to the unit
  plan or above (on: about the unit 4 re-plan's level or lower; off: clearly higher); how many unit plans need a
  change; whether a change is to the template or to one unit. The lead writes the exact thresholds; they are shown
  to Cory before the first probe runs. **Done 2026-11-13:** docs/pipeline/PROBE-GUARD.md, on the Desk as card
  q-probe-guard.
- **P5. Make the expert reader good enough for this work** (Cory, 2026-11-13: there are no people yet, so the
  expert agent and Codex are the reviewers until there are). Today docs/agents/EXPERT.md and the briefs in
  docs/pipeline/briefs/ are built for math plans and days; rubrics are on file for math K to 8 and ELA only. Before
  step 1:
  - **P5a. Subject lenses.** One short lens file per core subject the expert reads first: what good teaching of it
    looks like and the errors reviewers catch (social studies: the C3 inquiry arc, sourcing and claims with
    evidence, historical thinking, the values rule, sensitive topics; science: the three dimensions of NGSS, a
    phenomenon that drives the unit, models and argument; ELA: text complexity, building knowledge, writing from
    sources; math: the existing pages). Each names its sources (the progressions documents, the frameworks' own
    guidance), read once into our own words.
  - **P5b. A bar for science and social studies.** A rubric file for science (named in earlier reviews, not filed)
    and the social studies part of docs/ADOPTION-BAR-SUBJECTS.md, so every read has a bar to read against.
  - **P5c. Briefs for the new layers.** Progression-read and frame-read briefs, with the data each read must check.
  - **P5d. Calibration before trust.** A small test set: copies of a progression slice and a unit plan with planted
    faults of known kinds (a skill owned twice, a handoff that skips a grade, a model used before it is taught, a
    standard taught in part, a values-rule miss, an exit that misses the goal), plus past findings whose truth is
    settled. The expert reads it cold; we count what it catches and what it flags wrongly. Codex reads the same set,
    so we see what both miss. "Good enough" is set before the run (recommended: catches at least 8 in 10 planted
    major faults with few false alarms, and no kind missed by both). Re-run after any change to EXPERT.md or a
    brief.
  **State 2026-11-13:** P5a done (docs/agents/lenses/), P5b done (docs/RUBRIC-SCIENCE.md, first draft; social
  studies section of docs/ADOPTION-BAR-SUBJECTS.md updated), P5c done (briefs progression-read and frame-read),
  P5d run 1 done (docs/reviews/calibration-2026-11-13.md): the expert passes the line (18 of 18 planted majors);
  Codex passes too; EXPERT.md gains a leniency and a severity rule; re-run is later.csv L10.
  - The FOUNDATION 7.3 rule that qualified people read a course before it is called finished still stands; with no
    people, nothing is called finished, but planning goes ahead on the expert and Codex.
- **Who decides, at every review and baseline.** The expert settles item-level choices. Cory decides go or no-go
  at each baseline, at the final review and on an "off" result from a probe or the guard, and any change to scope
  (what a course or grade teaches, the course list, a subject's order).

### Step 1. Progressions for the four core subjects, then a review

One progression per subject, all its grades, kept as data with gates: data/progressions/<subject>.csv, one row per
skill, with the columns strand, grade, skill_id, standard, assumes (skill ids from earlier grades), hands_on (skill
ids the next grade assumes), model_in, model_out, words, and cross_subject.

- plan.py checks that a course's readiness items name skill ids an earlier grade owns, that every skill id is owned
  by exactly one grade, and that a carried model (number line, tape diagram, timeline, map scale) is introduced
  before a course leans on it.
- **Across subjects**: the cross_subject column records where one subject leans on another (graphs in grade 6
  science against grade 6 math; reading demands against ELA; timelines and number lines between social studies and
  math). A course may not lean on a skill no subject has taught by that grade. This is why all four are built
  together.
- data/sequence.csv stays as the module order (which topic follows which); the new file sits under it at skill
  level, and sequence.csv's open science errors are fixed in this step. ROADMAP layer 4's home gains the new files.
- Built from the standards and the progressions documents, with each base text's own sequence as evidence (IM K to
  12, OpenSciEd middle school, EL K to 5); the existing grades 3 to 5 math page is folded in.
- **Review**: the expert reads each subject cold, then one read across all four for the cross-subject column.
  Anything that changes what a grade teaches comes to Cory.

Rough cost, not measured: about 0.5 million tokens per subject and grade band with its read, so about 6 to 8
million for the four subjects.

**Social studies done 2026-11-13** (Desk card q-ss-progression-1): 384 rows, K to 12, in
data/progressions/social-studies.csv, with data/progressions/social-studies-excluded.csv (10 codes, each with a
reason) and the band drafts in data/progressions/parts/. Gate: scripts/progression.py (inside plan.py check): ids,
grades, real codes, every Massachusetts standard owned by one grade or excluded, both ends of every handoff,
models handed on before use, cross_subject codes real; notes for C3 indicators in two grades, skipped handoffs and
model gaps. How it was made: five band writers in parallel, one stitcher, two cold reads (expert agent and Codex
by script, scripts/codex_read.py), one fix pass (19 of 22 findings applied). Measured cost: about 1.4 million
agent tokens for the subject, reads included, plus Codex's own. The other three subjects follow the same way.

### Step 2. Course frames for the four core subjects, then a review: baseline 1

A course frame says what the course is: its grades, the standards and progression skills it owns, its days, its
unit list with a reason for each unit, and, where there is a base text, the source map (data/plans/<course>/source-map.csv: every base lesson placed in
one of our units, scripted from the source's free pages, then judged for unit edges and day counts; grade 4 math's
table of 149 IM lessons is already scripted, kept outside the repo in the source store). A course frame is the course-level
summary; its scope and sequence (step 3) then sets every day in order. The 58 courses of the four core subjects get one each. The three scopes and sequences on
file are read as input against the progressions, not assumed right.

Then **baseline 1**, a whole-structure review:
- every frame against its progression rows, and the frames of each subject read side by side through the grades;
- where the layers, the gates or the vocabulary need alignment or fixing;
- **the website design check**: whether the site's structure (catalog pages, topics, course and unit pages) still
  fits the hierarchy, and what changes if not. Proposals to Cory; nothing is rebuilt during planning unless he says;
- a Codex read of a sample, and a human read if a person is found by then.

### Step 3. Social studies: scope and sequence for every course, then a review

Each social studies course's frame becomes its scope and sequence (every teaching day in order, by unit). The
expert reads each against the progression and the content standard P1 set; Cory says yes to each.

### Step 4. Social studies: units, then a review, then the probe: baseline 2

- Every social studies unit is planned, with its cross-day files (hand-backs, materials, reserved examples, and the
  source map if P2 found a base text). The expert reads each.
- **The probe**: a few social studies days (one section, 3 to 5 days) are written from the unit plans and read the
  full way (writer, cheap read, expert read, fix, re-read). Measured against the P4 definitions: the share of day
  findings traced back to the unit plan or above, how many unit plans need changing, and whether the unit template
  itself needs a change before three more subjects copy it.
- **Baseline 2**: a full review of social studies from the progression down, plus the probe's result. Template
  changes are made here, once, before step 5.

### Step 5. The other three subjects, math last: the same cycle

Each subject in turn runs step 3 and step 4's planning and review (scope and sequence, review, units, review), with
the probe, and a review from the progression down at its end. Math goes last. Science goes second if P2 finds no
social studies base text; otherwise the order of science and ELA is Cory's (section 6, question 2). The probe runs
in every subject: a few days each is cheap, and each subject's units can be off in their own way.

Science 6 to 8 follows OpenSciEd's order after its loss check. ELA K to 5 and middle school science test the base
text paths that INTEGRATION-PLAN's two small trials were meant to test, so those trials fold into this step.

**Math last.** Math converts the most old work: grade 4's scope and sequence, unit plans, the unit 4 re-plan and
its source map are read against the new layers and changed where the review finds it, rather than kept because
they exist. The grade 4 source map resumes here.

### Step 6. The final review: every subject, every course

One cold read from the progressions down across all 58 courses of the four core subjects: continuity through the grades, the
cross-subject column, frames and units against their layers. Then a Codex read of a sample and a human read where
people are found. This is the last check before days.

### Step 7. Sections, days and lessons

Writing starts only here, under the review cadence (step 8).

- **The guard first**: a few days in each subject written from the unit plans and read in full, measured against
  P4, before full writing. If the plans are far off, the units are corrected before the rest is written.
- Section plans stay one section ahead of writing. Days are written in course order.
- Grade 4 math's 48 written days: the unit 4 days 25 to 28 hold their fixes, the six open re-read items and the
  seven backfill slips in defects.csv wait for math's units to be settled. A small fix job on the other written days
  (the rebuild check of the 44 older days: rebuild, gates, one cheap print-and-screen check) may run any time.
- Each course is finished as a whole before it is called finished: course-level checks (start of year, quarterly,
  year end, each with a respond day) read as one assessment plan; a coherence pass over units and seams; English
  learner supports; claims checked against the ledger; the whole-course cold read against its rubric (for math,
  RUBRIC-MATH-K8) and ROADMAP's "What a finished course holds".

### Step 8. The review cadence (from step 7 on)

Per day: writer, cheap read, expert read, fix pass (with the re-read rule: re-read the paragraph, the seam and the
built screens changed). Per section: one fresh set read across its days and seams, then its fixes. On the first
section written, test whether the set read can stand in for the separate cheap check of a fix pass. REVIEW-CADENCE
step 3 is unchanged: the expert drops to spot checks only when no process finding repeats from an earlier unit (19
of 26 repeated in unit 4) and expert-only findings are about one a day, and a qualified teacher still reads a
sample. Plan as if the expert read stays on every day: about 650,000 tokens a fully read day (an estimate including
the set read), which across about 13,300 days (all 105 courses) is about 8.6 billion, a floor (it leaves out unit-level
pieces, planning, tooling and re-reads). Most of those day counts are assumed until each course's frame sets them.

### Step 9. Tools

Tools stay held until days are being written; then key tools are built or rebuilt for the sections that name them,
live and verified, with print covering the rest (FOUNDATION 6.3). Tools already live stay live as free-standing
tools and claim no course coverage until a section names them (BASELINE rule 26).

### Existing work: what happens to each piece

- Grade 4 math scope and sequence, unit plans (s01 to s04, s09 to s11), section plans (u04-1 to u04-4 and the
  rest), the unit 4 re-plan and its source map and cross-day files: held, input to math's turn in step 5.
- Section 11.1 (built, all but its tool) and its owed teacher read: held; the teacher read happens when a teacher is
  found and counts toward math's finishing.
- The start-of-year check and the unit 4 readiness items (the old rule 25 exceptions): held with grade 4 math.
- The grade 6 ELA and grade 4 science scopes and sequences: input to step 2 and their subject's turn; Cory's final
  yes waits until they are read against the progressions.
- Sara's list (docs/courses/NEXT-SPINES.md): input to step 2's course frames.
- The science simulations to list per unit (Cory's earlier ask): listed when science's units are planned.
- The Codex queue's queued builds (for example Community Plot Planner): paused with all tool work until step 9;
  Codex's budget goes to reads (P5d and the baselines) first.
- The 149-lesson IM table: kept in the source store for math's source map.

### After the core subjects

The 49 non-core courses (arts and music, health and PE, computer science, career and technical education, social
and emotional learning, English language development, library and research skills; world languages stay shelved)
come after the core subjects (Cory, 2026-11-13). Where a core progression leans on one of them (English language
development with ELA; health with science), the cross_subject column notes it for then.

### People and a second reader, through all of it

- **A reader of a different model kind** at each baseline and in P5d's calibration: Codex reads cold against the
  same brief, and its findings are compared with the expert's. Cory pastes the prompts himself. Codex's weekly
  budget resets often and is open for large use (Cory, 2026-11-13); Pro ends 2026-11-30.
- **People: none yet** (Cory, 2026-11-13). The expert agent, checked in P5, and Codex are the reviewers. A social
  studies content reviewer, a math content reviewer and teachers are still needed before any course is called
  finished (FOUNDATION 7.3); they are added when found.
- The expert agent stands in as the teacher reader until a teacher is found (Cory 2026-11-13).

## 4. What changes in existing work

- BASELINE rule 25 is replaced by this order (P3).
- The grade 6 ELA and grade 4 science pilots, and their trigger (card q-plan-after-11-1), are retired: the probe and
  the guard take their place, and the two small base-text trials fold into step 5.
- The three scopes and sequences on file, the grade 3 to 5 math progression and grade 4 math's unit plans become
  input to their steps, read against the new layers.
- The unit 4 re-plan (days 29 to 38), its source map and cross-day files are held for math's turn. The cross-day
  files and gates are reused by every subject.
- All math planning and writing stays paused until step 5 reaches math, except small fixes to written days
  (not days 25 to 28).
- Unchanged: light credit, course order by what teaches best, science 6 to 8 on OpenSciEd's order after its loss
  check, substitutes then no-kit, the expert as stand-in teacher reader, no IM login-gated material, no per-day
  `base` column.

## 5. What is not known yet

- Whether planning every unit before writing leaves few enough problems below (the probe and the guard measure it;
  section 2's table suggests planning can reach about 9 of 26 day-level problems, not the 11 in the day itself).
- The real cost of planning a subject (social studies measures it first). Rough guesses only so far: 6 to 8 million
  tokens for the progressions; units for 58 courses not yet sized.
- How long the whole planning phase takes, so how long no new days go live. Cory accepted this (2026-11-13).
- Whether a base text helps in ELA and science as it did in math (step 5 tells).
- How well the expert reads outside math (P5d measures it); whether its findings match a teacher's and a content
  reviewer's (only people can say).
- Whether a set read can replace any per-day read (step 8).

## 6. For Cory

1. **The redrawn social studies course list** (P1b): answered yes 2026-11-13 and done.
2. **Science or ELA second**: settled by P2 (2026-11-13). No social studies base text, so science is second. Two
   licence calls for partial bases are on the Desk as card q-ss-partial-bases.
3. **The probe and guard thresholds** (P4): on the Desk as card q-probe-guard (2026-11-13). The expert's "good
   enough" line (P5d) follows when P5 is done.

Answered on 2026-11-13 and recorded in DESK-ANSWERS: the unit 4 re-plan and the unit 8 test; the IM login; the
pause; the progression layer; this build order, its probe and guard, the rule 25 change, and the non-core courses
after the core; option (d) stands, with more pre-work to make it usable; no people yet, so the expert is made good
enough first; Codex used freely; no spending ceiling (judicious with tokens, never at the cost of quality). The earlier questions on the ELA and science pilots and on when grade 4's frame counts as built are
retired by this order.

## 7. What the independent check corrected (from draft 1)

Draft 5 replaces the path with Cory's build order (above); items 7, 9 and 11 below are superseded by it (the ELA
and science pilots are retired). Draft 5's cold check corrected: the subject order (science second only if P2 finds
no base text); the probe in every subject, not once; only progressions and frames go across all four subjects; P1
reopened a standard Cory chose on 2026-11-12, and a values question he settled; wrong step cross-references; the
"section 2 unchanged" claim; the 11 count; "49 courses" for the assumed day counts; no decision owners; "course
map" against GLOSSARY; existing work with no stated fate; section 6 missing the order, the standard and a money
question. Draft 4's own cold check corrected: step 3's stale
pre-re-plan paragraph; the cross-day count (9 in the planned days, not 11); the re-read count (6, not 7); tool
rounds listed as built; step 0 stated as settled and its data undefined; question 4 without a cost.

1. Draft 1 said ten of 26 problems were decided above the day and "a day writer cannot see those". Reclassified: 7
   cross days (3 of them materials, 2 of which the writer could see), 2 are stale plan text, and one I had called above the day
   (a key read as multiplication) is day wording. Downgraded from firm to likely.
2. Draft 1 said seven builder faults were "now fixed for every course". Five were; two were fixed in the day; the
   reliability read then found two more builder faults.
3. Draft 1 said the expert-only criterion was "not met". It was not measurable (tagging changed); like for like,
   findings were the lowest yet.
4. Draft 1 compared unit 4's 572,000 with the audit's 540,000, which included unit-level pieces. Like for like,
   unit 3 is about 506,600.
5. Draft 1 gave the set read as 56,000 a day; the control cost 78,600. Range given now.
6. Draft 1 said every expert found the source helped or was neutral and nothing was lost. Two named something the
   source offered that was not carried.
7. Draft 1 continued unit 4 sections 2 to 4 on their old plans while calling day-by-day reconciliation the thing to
   end, and treated the go rule as passed. Now re-planned first, and the go is Cory's.
8. Draft 1 put the ledgers in plan prose; now they are CSVs with gates, plus a reserved-examples ledger and a
   minutes-and-branches check, which the unit 4 evidence needed and draft 1 missed.
9. Draft 1 framed other math courses before the ELA and science pilots, against card q-plan-after-11-1, and left out
   the pilots, course-level checks, the math content reviewer and the finished-course items. All restored.
10. Draft 1 called the builder pass a once-only cost (every unit has needed one), said no read found grade 4's order
    harming learning (none was asked), and dropped REVIEW-CADENCE's no-repeat condition and teacher sample, and the
    token-definition caveat. All corrected.
11. Round 2: draft 2 said the pilots test the EL and OpenSciEd paths; neither uses a base text (grade 6 ELA is
    our own on public-domain texts; grade 4 science uses OpenSciEd elementary as reference only). The two small
    trials are now named and gate those frames.
12. Round 2: draft 2 let a key tool be replaced by its paper path in a finished course, lowering FOUNDATION 6.3's
    bar without Cory. Removed.
13. Round 2: draft 2 dropped the unit 8 test Cory approved without asking, called people "scheduled" with no
    triggers, and put question 2 without the context that points the other way. Now asked, triggered and fairly
    framed, with a third question on people.
14. Round 2: the finishing read for older days is 41 days, about 2.3 to 3.2 million (draft 2 had 2.3 to 3.5, an
    arithmetic slip carried from the first check); the set read is about 30 to 40 percent of a per-day expert read.
