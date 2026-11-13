# How a course gets made: the path forward (2026-11-13)

For Cory. Asked 2026-11-13: fold the unit 4 reliability review into the pipeline audit and give one firm "best
path forward", judged against the end goal (FOUNDATION 1: a teacher can run any course from the first day to the
last, free, and it would stand up to a state adoption review) and the bar (quality over speed and over saved work).
Changes to existing work are allowed where they teach better.

**How this was checked.** Draft 1 was read by a fresh agent that recomputed every number from the sources and
attacked the logic ("not sound as is; sound with changes"). Draft 2 took its changes and was checked again by the
same reader, which asked for four more small fixes; draft 3 had them. Draft 4 (this one, later on 2026-11-13) adds
Cory's decisions since: unit 4 re-planned and held, the IM login dropped, all math mapped at the course level first,
then all planning paused until this page is settled. It also adds the layer above the course (answer 1 and step 0).
What the checks corrected is listed in section 7, so nothing was quietly folded in.

Evidence, all in the repo: docs/reviews/pipeline-audit-2026-11-13.md, the eight unit 4 reads (cheap-d025 to d028,
day-025 to day-028), the two reliability reads (reliability-u04-d025-028, reliability-u02-d007-009),
docs/pilots/COST.md, docs/pilots/REVIEW-CADENCE.md, data/plans/defects.csv, docs/sources/INTEGRATION-PLAN.md, and
Cory's decisions in docs/agents/decisions/DESK-ANSWERS.md. Samples are small: four test days and three control
days, all judged by the same kind of model that wrote them.

## 1. The answer

1. **Plan from the widest scope down; write, read and finish one course at a time.** ROADMAP's layers set the
   order: foundation, standards, approach, then **progressions** (layer 4: what each grade inherits and hands on, per
   subject, across all its grades), then each course's scope and sequence with its map against the base text, then
   units, sections and day rows, then days in order. A level is settled before the one under it, and corrected by
   what is built on it. Unit and section plans stay one unit ahead of the writing (BASELINE rule 25), because each
   written unit changes the next plan. This is the audit's hybrid: our frame first, a base text read at planning
   time, never reconciled day by day against a plan that did not know it. (Likely: the direction is well supported;
   how much it saves is not yet measured.) Layer 4 is the level that keeps courses continuous through the grades,
   and it is the thinnest today: one page, math grades 3 to 5 (step 0).
2. **What crosses days goes into data, with gates, not into prose.** Some problems only show across days: a
   hand-back that answers the wrong form of an error, a worked example spent before its day, a tool round run a day
   early, materials a later day needs. Five to seven of the 26 problems only the expert read caught on the unit 4
   days were of this kind. They are cheapest to stop as small CSVs that plan.py and lesson.py check against the day
   text (section 3, step 2). (Likely; it rests on four days of the worst-fitting unit in grade 4.)
3. **Base texts stay, for quality. They did not change cost.** No residual problem sat in an adapted part, and
   fewer problems were found per day than in any earlier unit with a cheap read (like for like: 6.5 missed by the
   cheap read per day, against 7.0 to 10.7). Two experts named something the source offered that our day did not
   carry, so the gain is real but not automatic. Writer tokens showed no detectable difference. (Fair; n is 4, and
   briefs grow every unit, which confounds both numbers.)
4. **Course order follows what teaches best** (Cory). A base text's order is the default only where the loss check
   finds it at least as good for learning; science 6 to 8 moves to OpenSciEd's order after that check. Grade 4
   math keeps its approved order if it does not harm learning, so its four known order conflicts get that check
   (step 2).
5. **Every day keeps both reads; each section ends with a set read.** The expert read still catches problems the
   cheap read misses on every day, so it stays. The fresh set read across a section's days found fix-pass
   regressions and seam problems the per-day reads had missed, at about 30 to 40 percent of the cost of a per-day expert read, so
   it becomes the last check of every section. Fix passes made 3 of the 12 and 6 of the 13 problems left at the
   end, so every fix brief now says: re-read the paragraph, the seam and the built screens you changed.
6. **People and a second kind of reader are required, with a trigger each.** Every reliability number here is the
   model judging itself. A grade 3 to 5 teacher, the math content reviewer FOUNDATION requires, and a reader of a
   different model kind each have a point in the order (step 7); who and when is Cory's (question 3).

## 2. What the measurements say

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

INTEGRATION-PLAN makes a mixed result Cory's call. Question 1 in section 6 asks it.

### What the 26 expert-only problems were (reclassified after the check)

| Kind | Count | Prevented by |
|---|---|---|
| Across days: sequence, hand-backs, reserved examples (d26 1; d27 1; d28 3; d28 5) | 4 | the cross-day CSVs (step 2) |
| Across days: materials (d25 1; d25 2; d26 4); d25 1 and d26 4 were visible to the day writer | 3 | the materials CSV |
| Plan documents gone stale against the days (d25 7; d27 5) | 2 | a plan.py check that plan fields match the day rows |
| Builder and display (d26 2; d27 3; d27 4; d28 1; d28 4; d26 7) | 6 | lesson.py; five fixed course-wide on 2026-11-13, and the reliability read then found two more |
| The day itself (d25 3, 4, 5, 6; d26 3, 5, 6; d27 2, 6, 7; d28 2) | 11 | the writer and the reads |

The audit found only about 6% of earlier findings in the plan layer; here the cross-day share is higher because
this unit's plan predates the source and fits it worst. The checker would count 5 to 7 across days; this table
counts 7, three of them materials.

## 3. The path, step by step

### Step 0. The layer above the course: progressions, subject by subject (proposed 2026-11-13; question 4)

Today only grades 3 to 5 math have a progression page, and data/sequence.csv has open errors from the science
review. A course map can only be checked against its neighbours if the neighbours exist, so before any more course
maps:

- **One progression per subject, all its grades** (math K to 12 first): the strands (for math: counting and place
  value, operations, fractions to ratios to functions, measurement and data, geometry, statistics), what each grade
  owns, what it assumes from the grade before (its first readiness checks) and what the next grade assumes from it,
  the models carried across grades (number line, tape diagram, area model) with where each enters and leaves, and
  the words a student meets at each grade.
- **As data, with gates**, like the cross-day files: data/progressions/<subject>.csv, one row per skill, with the
  columns strand, grade, skill_id, standard, assumes (skill ids from earlier grades), hands_on (skill ids the next
  grade assumes), model_in, model_out, words, and cross_subject. plan.py checks that a course's readiness items name
  skill ids an earlier grade owns, that every skill id is owned by exactly one grade, and that a carried model is
  introduced before a course leans on it. data/sequence.csv stays as the module order (which topic follows which);
  the new file sits under it at skill level, and sequence.csv's open science errors are fixed when the science
  progression is built. If question 4 is yes, ROADMAP layer 4's home gains this file.
- **Across subjects, where they meet**: a science or social studies course may not lean on math or reading a
  student has not been taught yet (graphs in grade 6 science against grade 6 math; reading level against ELA).
  This is a column in the same data, filled when those courses are mapped.
- Built from the standards and the progressions documents, with the base texts' own sequences (IM K to 12) as
  evidence; read cold by the expert; Cory settles anything that changes what a grade teaches.

Then the course maps: every IM lesson of each math course placed in one of our units, scripted from IM's free
pages (grade 4's table of 149 lessons is already scripted and kept in the source store), judged for unit edges and
day counts against the progression, read by the expert. Order: grade 4 with grades 3 and 5, then the rest of K to
8, then high school. Scope and sequence changes come to Cory. Paused 2026-11-13 until this page is settled. If
question 4 is yes, this changes the Option A order: the grade 4 map waits for at least the grades 3 to 5 band of
the progression (recommended: that band first, then the grade 4 map, then the rest of K to 12 beside the other
maps).

### Step 1. Close the unit 4 test (done 2026-11-13, one item left)

The 25 reliability fixes are in, with the re-read rule: the cheap re-read of that fix pass found a builder
regression (nine class questions dropped from the screens on days nobody had re-read), fixed the same day. Left:
restore the expert brief's split between "missed by the cheap read" and "expert only", so REVIEW-CADENCE step 3 can
be judged again.

### Step 2. Build the cross-day data and the source map (small, once per course; built for grade 4 2026-11-13)

- **Cross-day CSVs** in data/plans/<course>/: materials by day; hand-backs (from day, to day, what, error and its
  form, minutes); tool rounds by day (not built yet); reserved worked examples (an example and the day it belongs to). plan.py and
  lesson.py check each against the day text: a hand-back must land in a day row with minutes for it, a material
  used must be in the ledger, a reserved example must not appear early. The prose plans point at these files
  instead of restating them.
- **A minutes-and-branches check**: a timed part that names more reteach branches than its minutes allow gets a
  NOTE (the one unit 4 major).
- **Backfill now for the 48 written grade 4 days**: the hand-back and materials CSVs scripted from existing
  Tomorrow lines and Before class sections, so the open hand-ons (days 29, 42, 78, 79, 94) are on record.
- **Source map** (data/plans/<course>/source-map.csv), one row per base lesson: source id, standards and goals
  (scripted from IM's prep files), our unit and days, keep / split / merge / cut / ours, leans to cut, and for
  grade 4 a column for the four order conflicts and whether each harms learning. This replaces the per-day `base`
  column, which stays unbuilt as recorded.
- **IM-TO-DAY card** (docs/sources/): how an IM lesson's parts become ours (launch and explore become teaching first
  for grades 2 to 5; what to cut). Decided once.
- **Done 2026-11-13:** the four cross-day files with gates (hand-backs, materials with a reverse check, reserved
  examples, source map), backfilled for 48 days, and the minutes-and-branches note.
- **IM's login-gated files: not taken** (2026-11-13). IM's sign-in asks for proof of being an educator, which Cory
  does not have. Nothing is lost that a plan needs: exits and assessments were always ours, written first and held
  by the gates; what is missed is a comparison with IM's cool-downs, assessments and practice answers, and the math
  content reviewer (step 7) is the check that stands in for it.

### Step 3. Unit 4 sections 2 to 4: re-plan from the source map, then write (Cory's go, 2026-11-13)

**Done and held (2026-11-13).** The source map, cross-day files and re-plan of days 29 to 38 are in, read by the
expert (13 findings, 11 across days, all applied) and re-read (6 small items, logged in defects.csv for when unit 4
resumes). Writing is held (Cory) until grade 4's course map and its expert read are in (and, if question 4 is yes,
the progression band it is checked against), so the course level is settled before the unit; days 25 to 28 hold
their fixes until then too. Of the expert's 11 cross-day findings at plan time, 9 were in the 10 planned days and
2 in written days 24 and 28; the test is the count the day reads find once days 29 to 38 are written, against 7
across days 25 to 28.

Sections 2 to 4 were planned before the source, so they were re-planned from the source map rather than written
and reconciled day by day. This is the plan-time test, on the hardest fit in grade 4, with two comparisons in hand:
days 25 to 28 (written the old way; only their "missed" counts compare, and their content differs) and days 36 to
38 (no IM lesson). When the days are written, they are scored on the writer's conflict list, the share of each day
taken from the source, planning tokens, and missed and expert-only findings per day. It stands in for the unit 8
test, which was chosen for having no order conflict and so could not tell a good method from an easy unit; unit 8
returns only if unit 4's result is unclear (Cory).

### Step 4. Rebuild check on the older days (cheap; fixes to written days may run during the pause)

The builder pass changed how all 44 earlier days render. Rebuild, run the gates, and run one cheap print-and-screen
check across them (pages, slips, display order), and fix the seven cross-day slips the backfill logged in
defects.csv. Days 25 to 28 wait for the grade 4 course map. Their full finishing pass waits for step 8.

### Step 5. The ELA and science pilots, then other courses (order per card q-plan-after-11-1)

Grade 4 math stays the main thread. The grade 6 ELA pilot (unit 2, five days, our own on public-domain texts) and
the grade 4 science pilot run alongside it once 11.1 has its teacher read (question 2). They measure cost and
quality in ELA and science, but neither uses a base text, so they do not test the EL or OpenSciEd paths. Those need
the two small trials INTEGRATION-PLAN proposed (an EL grade 4 lesson set on a public-domain text; one OpenSciEd 6.1
lesson run through to days); EL and OpenSciEd courses are not framed until those trials are read (Cory's call when
the pilots are under way). Science 6 to 8 is framed on OpenSciEd's order after its loss check. No other math
course is framed until the pilots are in, as the card says; the course maps of step 0 are not framing (they place a
base text's lessons and test unit edges; nothing is planned or written from them until a course opens). Whether
ELA and science build their progression (step 0) before their pilots is question 4.

### Step 6. The review cadence

Per day: writer, cheap read, expert read, fix pass (with the re-read rule). Per section: one fresh set read across
its days and seams, then its fixes. On the first section written after the pause, test whether the set read can stand in for the separate
cheap check of a fix pass, and log what each finds. REVIEW-CADENCE step 3 is unchanged: the expert drops to spot
checks only when no process finding repeats from an earlier unit (19 of 26 repeated in unit 4) and expert-only
findings are about one a day, and a qualified teacher still reads a sample. Expert-only has not trended down
across six units, so plan as if the expert read stays on every day: about 650,000 tokens a fully read day (an
estimate including the set read), which across about 13,300 days is about 8.6 billion, a floor for the assumed day counts (it leaves out unit-level pieces, planning, tooling and re-reads). The day counts for 49 courses are assumed.

### Step 7. People and a second reader

- **11.1 teacher read** (trigger: before any grade 4 unit is called finished): a grade 3 to 5 teacher reads the 11.1 pack and marks which expert findings are real. That
  calibrates every expert number in this file.
- **A reader of a different model kind** (trigger: the first section written after the pause; until then, the
  unit 4 re-plan or days 25 to 28 can stand in, so the read is not lost before 2026-11-30): Codex reads it cold
  against the same brief; compare its findings with the expert's. It is the only check on a shared blind spot available before
  people are found. It runs through the Codex queue Cory pastes himself, so it costs his time (question 3); Pro
  ends 2026-11-30.
- **Before grade 4 math is called finished** (FOUNDATION 7.3): a math content reviewer on every item and key of
  the course's checks; the pilot unit's taught run and three timed students. Cory finds the people; nothing is sent
  or spent without his yes.
- The expert agent stands in as the teacher reader until a teacher is found (Cory 2026-11-13).

### Step 8. Finish grade 4 math as a whole course

Before it is called finished, beyond the days:

- the course-level checks (start of year, quarterly, year end, each with a respond day; day 78's Check 2 waits on
  units 6 to 8) checked as one assessment plan against the standards;
- a course-level pass on coherence: every unit's reason and what it hands the next, unit-boundary seams, focus on
  the major work of the grade;
- a set read per section over the 41 older days still unread this way, with the re-read rule: about 2.3 to 3.2
  million tokens, plus fixes;
- key tools live and verified, print covering the rest (FOUNDATION 6.3); tools stay held until the frame is built,
  and when grade 4's frame counts as built is Cory's (question 3);
- English learner supports on teacher pages; claims checked against the ledger;
- the whole-course cold read against RUBRIC-MATH-K8 and the rest of ROADMAP's "What a finished course holds".

## 4. What changes in existing work

- New CSVs and gates (step 2); prose plans point at them. The fix brief gains the re-read rule. The expert brief
  restores the missed / expert-only split.
- Unit 4 sections 2 to 4 are re-planned (done) and held until grade 4's course map is read.
- All new math planning and writing is paused until this page is settled (Cory, 2026-11-13); if question 4 is
  yes, step 0 then comes before more course maps and days.
- The 44 written days get a rebuild check now and a finishing pass before the course is called finished.
- Unchanged: grade 4's order (now with its loss check), light credit, science 6 to 8 on OpenSciEd's order after its
  loss check, substitutes then no-kit, our own tools as simulations once tools are unheld, the expert as stand-in
  teacher reader, no per-day `base` column.

## 5. What is not known yet

- Whether planning from the source map cuts the problems the expert finds in the written days (step 3; the
  plan-time read found 9 cross-day items in the 10 planned days, all applied before writing; the re-read of
  that fix pass left 6 small items logged).
- Whether the course maps move any grade 4 unit's edges or day count (step 0; a rough script count puts IM's
  lessons on 4.NF.B.3 at 5 to 8 against our 14 days, not yet judged).
- Whether a set read can replace any per-day read (step 6).
- Whether the expert's findings match a teacher's (step 7).
- The real cost of planning (step 3 measures it).
- Whether a base text helps in ELA and science as it did in math (only the two small trials in step 5 can say).

## 6. For Cory

1. **Answered 2026-11-13** (unit 4 sections 2 to 4 re-planned first; unit 8 test dropped unless unit 4's result is
   unclear). Kept here for the record.
2. **What starts the ELA and science pilots** (card q-plan-after-11-1 says "once 11.1 has its teacher read"). Your
   mom, a grade 2 teacher, looked at unit 11, which you judged enough to lift the planning freeze; on 2026-11-13 you
   made the expert the teacher reader for now, which arguably already meets the card's trigger; no grade 3 to 5
   teacher is named yet, so waiting for one has no end date.
   Recommended (middle): start the pilots now on the expert stand-in, and call nothing finished (11.1 or either
   pilot) without a grade 3 to 5 teacher's read. Alternatives: wait for that teacher; or count the stand-in fully.
3. **People and timing** (FOUNDATION 7.5), three separate calls:
   - 3a. Who and when for the grade 3 to 5 teacher and the math content reviewer.
   - 3b. Whether you will paste the Codex different-model read into your queue before 2026-11-30, on the unit 4
     re-plan or days 25 to 28, since no new section will be written by then. Recommended: yes, one paste.
   - 3c. When grade 4's frame counts as built, which unholds its key tools. Recommended: when grade 4's course map
     (and, if question 4 is yes, its progression band) is read and unit 4's re-plan stands against it.
4. **The layer above the course (step 0).** You asked whether something above the course should keep continuity
   across courses and through the grades. ROADMAP already names it, layer 4, progressions, but it exists for math
   grades 3 to 5 only (one prose page plus data/sequence.csv's module order). Recommended: build it as data with
   gates (step 0), math first, grades 3 to 5 band before the grade 4 map, then the rest of K to 12 beside the other
   course maps; ELA and science build theirs before their pilots start (it is what their first readiness checks hand
   off from). Rough cost, not measured: about 0.5 million tokens and one or two working sessions per grade band
   with its expert read, so about 2 million for math K to 12; the grade 4 map waits about one session. This changes
   the Option A order. Alternatives: math only now, the others when they open; or no new data, keeping today's
   prose page and sequence.csv.

## 7. What the independent check corrected (from draft 1)

Draft 4 adds Cory's decisions of 2026-11-13 (DESK-ANSWERS) and step 0. Its own cold check corrected: step 3's
stale pre-re-plan paragraph; the cross-day count (9 in the planned days, not 11); the re-read count (6, not 7);
tool rounds listed as built; step 0 stated as settled and its data undefined; question 4 without a cost.


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
