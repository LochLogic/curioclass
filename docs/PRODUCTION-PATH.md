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
layer by layer, across all four subjects, down to the unit level, before any more days are written. Sections 1 and
3 to 6 are rewritten; section 2 (the unit 4 evidence) is unchanged. What the checks corrected is listed in section
7, so nothing was quietly folded in.

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
   against the base text, where there is one), then units. A layer is built and reviewed for all four core
   subjects (math, ELA, science, social studies: 56 courses) before the layer under it. Sections, days, lessons and
   tools come only after every core subject's units are planned and reviewed. This replaces BASELINE rule 25
   ("prove at the bottom before planning wider"; Cory, 2026-11-13). Cory's reasoning: well-made units in a sound
   progression leave fewer problems below, and fixing back up the chain is a cost that cannot be avoided anyway.
   (Likely: the plan-time read of unit 4 caught 11 cross-day problems before writing; how much it saves at the day
   level is not measured yet, which is what the probe and the guard are for.)
2. **Test the plans against real days twice, with "on" and "off" set beforehand.** Once early, as a **probe**: a
   few social studies days written at baseline 2, before the other three subjects copy the unit template. Once at
   the end, as the **guard**: a few days written in each subject once every unit is planned, before full writing
   starts. Each measures how far off the plans were (section 3, steps 4 and 9).
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
   itself. A reader of a different model kind (Codex) and qualified people (a teacher, content reviewers) each read
   at a baseline; who and when is Cory's (section 6).

## 2. What the measurements say

(Unchanged from draft 4. This is the unit 4 evidence the path rests on.)

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
the reads whatever the plans are. The probe and the guard (steps 4 and 9) measure whether that holds.

## 3. The path, step by step

Where a subject has work on file it is not thrown away: it is input to the step, read against the new layer above
it. On file today (COURSES-STATUS): scopes and sequences for grade 4 math (approved), grade 6 ELA and grade 4
science (drafts waiting for Cory's final yes); grade 4 math's unit plans and 48 written days; the grades 3 to 5
math progression page.

### Pre-work (before step 1; Cory, 2026-11-13: "should be a solved issue before the plan gets started")

- **P1. The social studies content standard.** Cory wants better than "pick one state": a unified set, or a "high
  watermark" (take the more demanding expectation where states differ), and the same question for values conflicts
  between state instruments (HANDOFF, card q-bar-subjects, items 1 and 5). A short options paper with a
  recommendation goes to Cory; he decides. No social studies progression starts before it is settled.
- **P2. A social studies base text.** Scout for an openly licensed social studies curriculum whose licence lets us
  adapt it (some open material bars commercial use; each licence gets a verdict, light rigor). If one fits, it is
  loaded to the source store and used like IM. If none fits, social studies stays the clean-slate subject, and
  science goes second so the base-text lessons are learned before math.
- **P3. The rule change on record.** BASELINE rule 25 is replaced by this order, and HANDOFF and ROADMAP point
  here, so no worker follows the old rule.
- **P4. The probe and guard measures, set now** (section 3, steps 4 and 9), before any plan is written.

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

### Step 2. Course frames for the four core subjects, then a review: baseline 1

A course frame says what the course is: its grades, the standards and progression skills it owns, its days, its
unit list with a reason for each unit, and, where there is a base text, the course map (every base lesson placed in
one of our units, scripted from the source's free pages, then judged for unit edges and day counts; grade 4 math's
table of 149 IM lessons is already scripted). The 56 core courses get one each. The three scopes and sequences on
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

### Step 5. Science, ELA, then math: the same cycle

Each subject in turn runs step 3 and step 4's planning and review (scope and sequence, review, units, review), with
a review from the progression down at its end. Order: science, then ELA, then math (science goes second in any
case if P2 finds no social studies base text). The probe runs once, in social studies; the other subjects run it
again only if baseline 2 changed the template a lot.

Science 6 to 8 follows OpenSciEd's order after its loss check. ELA K to 5 and middle school science test the base
text paths that INTEGRATION-PLAN's two small trials were meant to test, so those trials fold into this step.

**Math last.** Math converts the most old work: grade 4's scope and sequence, unit plans, the unit 4 re-plan and
its source map are read against the new layers and changed where the review finds it, rather than kept because
they exist. The grade 4 course map resumes here.

### Step 6. The final review: every subject, every course

One cold read from the progressions down across all 56 core courses: continuity through the grades, the
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
the set read), which across about 13,300 days is about 8.6 billion, a floor for the assumed day counts (it leaves
out unit-level pieces, planning, tooling and re-reads). The day counts for 49 courses are assumed.

### Step 9. The guard's measures (set in P4)

For the probe and the guard, before writing: what share of day findings trace to the unit plan or above (on: about
the unit 4 re-plan's level or lower; off: clearly higher); how many unit plans need a change; whether a change is to
the template or to one unit. The exact thresholds are written in P4 and shown to Cory before the probe runs.

### Step 10. Tools

Tools stay held until days are being written; then key tools are built or rebuilt for the sections that name them,
live and verified, with print covering the rest (FOUNDATION 6.3). Tools already live stay live as free-standing
tools and claim no course coverage until a section names them (BASELINE rule 26).

### After the core subjects

The 49 non-core courses (arts and music, health and PE, computer science, career and technical education, social
and emotional learning, English language development, library and research skills; world languages stay shelved)
come after the core subjects (Cory, 2026-11-13). Where a core progression leans on one of them (English language
development with ELA; health with science), the cross_subject column notes it for then.

### People and a second reader, through all of it

- **A reader of a different model kind** at each baseline: Codex reads a sample cold against the same brief, and
  its findings are compared with the expert's. Pro ends 2026-11-30; before then the most useful read is P1's
  options paper or a first progression draft. It runs through the Codex queue Cory pastes himself (section 6).
- **A social studies content reviewer** matters first now, since social studies is planned first; a math content
  reviewer is still required before grade 4 math is called finished (FOUNDATION 7.3), and a teacher reads samples.
  Cory finds the people; nothing is sent or spent without his yes.
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
  tokens for the progressions; units for 56 courses not yet sized.
- How long the whole planning phase takes, so how long no new days go live. Cory accepted this (2026-11-13).
- Whether a base text helps in ELA and science as it did in math (step 5 tells).
- Whether the expert's findings match a teacher's and a content reviewer's.
- Whether a set read can replace any per-day read (step 8).

## 6. For Cory

1. **People and timing** (FOUNDATION 7.5):
   - 1a. Who and when for a social studies content reviewer (needed first now), the grade 3 to 5 teacher, and the
     math content reviewer.
   - 1b. Whether you will paste one Codex read into your queue before 2026-11-30. Recommended: yes, on P1's options
     paper or the first progression draft, whichever is ready.
2. **P1, the social studies content standard**: comes to you as an options paper with a recommendation. Nothing to
   answer yet.
3. **The probe and guard thresholds** (P4): shown to you before the probe runs. Nothing to answer yet.

Answered on 2026-11-13 and recorded in DESK-ANSWERS: the unit 4 re-plan and the unit 8 test; the IM login; the
pause; the progression layer; this build order, its probe and guard, the rule 25 change, and the non-core courses
after the core. The earlier questions on the ELA and science pilots and on when grade 4's frame counts as built are
retired by this order.

## 7. What the independent check corrected (from draft 1)

Draft 5 replaces the path with Cory's build order (above). Draft 4's own cold check corrected: step 3's stale
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
