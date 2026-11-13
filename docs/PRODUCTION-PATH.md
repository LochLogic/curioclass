# How a course gets made: the path forward (2026-11-13)

For Cory. Asked 2026-11-13: fold the unit 4 reliability review into the pipeline audit and give one firm "best
path forward", judged against the end goal (FOUNDATION 1: a teacher can run any course from the first day to the
last, free, and it would stand up to a state adoption review) and the bar (quality over speed and over saved work).
Changes to existing work are allowed where they teach better.

**How this was checked.** Draft 1 was read by a fresh agent that recomputed every number from the sources and
attacked the logic ("not sound as is; sound with changes"). Draft 2 took its changes and was checked again by the
same reader, which asked for four more small fixes; draft 3 (this one) has them. What the checks corrected is listed
in section 7, so nothing was quietly folded in.

Evidence, all in the repo: docs/reviews/pipeline-audit-2026-11-13.md, the eight unit 4 reads (cheap-d025 to d028,
day-025 to day-028), the two reliability reads (reliability-u04-d025-028, reliability-u02-d007-009),
docs/pilots/COST.md, docs/pilots/REVIEW-CADENCE.md, data/plans/defects.csv, docs/sources/INTEGRATION-PLAN.md, and
Cory's decisions in docs/agents/decisions/DESK-ANSWERS.md. Samples are small: four test days and three control
days, all judged by the same kind of model that wrote them.

## 1. The answer

1. **Plan from the widest scope down; write, read and finish one course at a time.** A course is framed first
   (scope and sequence, unit assessments, error register, course-level checks), then units, sections and day rows,
   then days in order. This is the audit's hybrid: our frame first, a base text read at planning time, never
   reconciled day by day against a plan that did not know it. (Likely: the direction is well supported; how much it
   saves is not yet measured.)
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

### Step 1. Close the unit 4 test (now, running)

The 25 reliability fixes (both sets) are being applied with the re-read rule, then a cheap check of what changed.
Restore the expert brief's split between "missed by the cheap read" and "expert only", so REVIEW-CADENCE step 3 can
be judged again.

### Step 2. Build the cross-day data and the source map (small, once per course)

- **Cross-day CSVs** in data/plans/<course>/: materials by day; hand-backs (from day, to day, what, error and its
  form, minutes); tool rounds by day; reserved worked examples (an example and the day it belongs to). plan.py and
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
- **IM's login-gated files: not taken** (2026-11-13). IM's sign-in asks for proof of being an educator, which Cory
  does not have. Nothing is lost that a plan needs: exits and assessments were always ours, written first and held
  by the gates; what is missed is a comparison with IM's cool-downs, assessments and practice answers, and the math
  content reviewer (step 7) is the check that stands in for it.

### Step 3. Unit 4 sections 2 to 4: re-plan from the source map, then write (Cory's go, 2026-11-13)

**Held 2026-11-13 (Cory):** the re-plan is done and expert-read; writing waits for grade 4's course-level source map
and its expert read (unit edges and day counts), so the course level is settled before the unit.

Sections 2 to 4 (days 29 to 38) were planned before the source. Writing them now would repeat the day-by-day
reconciliation this path is meant to end. So: build unit 4's source map and cross-day CSVs, re-plan u04-2 to u04-4
from them, then write, read and fix. This is the plan-time test, on the hardest fit in grade 4, with two
comparisons already in hand: days 25 to 28 (written the old way; only their "missed" counts compare, and their
content differs) and days 36 to 38 (no IM lesson). Measure the
writer's conflict list, the share of each day taken from the source, planning tokens, and missed and expert-only
findings per day. It would stand in for the approved unit 8 test, which was chosen for having no order conflict and
so could not tell a good method from an easy unit; whether to keep unit 8 as well is part of question 1.

### Step 4. Rebuild check on the older days (now, cheap)

The builder pass changed how all 44 earlier days render. Rebuild, run the gates, and run one cheap print-and-screen
check across them (pages, slips, display order). Their full finishing pass waits for step 8.

### Step 5. The ELA and science pilots, then other courses (order per card q-plan-after-11-1)

Grade 4 math stays the main thread. The grade 6 ELA pilot (unit 2, five days, our own on public-domain texts) and
the grade 4 science pilot run alongside it once 11.1 has its teacher read (question 2). They measure cost and
quality in ELA and science, but neither uses a base text, so they do not test the EL or OpenSciEd paths. Those need
the two small trials INTEGRATION-PLAN proposed (an EL grade 4 lesson set on a public-domain text; one OpenSciEd 6.1
lesson run through to days); EL and OpenSciEd courses are not framed until those trials are read (Cory's call when
the pilots are under way). Science 6 to 8 is framed on OpenSciEd's order after its loss check. No other math
course is framed until the pilots are in, as the card says.

### Step 6. The review cadence

Per day: writer, cheap read, expert read, fix pass (with the re-read rule). Per section: one fresh set read across
its days and seams, then its fixes. On unit 4 section 2, test whether the set read can stand in for the separate
cheap check of a fix pass, and log what each finds. REVIEW-CADENCE step 3 is unchanged: the expert drops to spot
checks only when no process finding repeats from an earlier unit (19 of 26 repeated in unit 4) and expert-only
findings are about one a day, and a qualified teacher still reads a sample. Expert-only has not trended down
across six units, so plan as if the expert read stays on every day: about 650,000 tokens a fully read day (an
estimate including the set read), which across about 13,300 days is about 8.6 billion, a floor for the assumed day counts (it leaves out unit-level pieces, planning, tooling and re-reads). The day counts for 49 courses are assumed.

### Step 7. People and a second reader

- **11.1 teacher read** (trigger: before any grade 4 unit is called finished): a grade 3 to 5 teacher reads the 11.1 pack and marks which expert findings are real. That
  calibrates every expert number in this file.
- **A reader of a different model kind** (trigger: unit 4 section 2, once written): Codex reads it cold against the
  same brief; compare its findings with the expert's. It is the only check on a shared blind spot available before
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
- Unit 4 sections 2 to 4 are re-planned before their days are written (if Cory says go).
- The 44 written days get a rebuild check now and a finishing pass before the course is called finished.
- Unchanged: grade 4's order (now with its loss check), light credit, science 6 to 8 on OpenSciEd's order after its
  loss check, substitutes then no-kit, our own tools as simulations once tools are unheld, the expert as stand-in
  teacher reader, no per-day `base` column.

## 5. What is not known yet

- Whether planning from the source map cuts the problems the expert finds (step 3).
- Whether a set read can replace any per-day read (step 6).
- Whether the expert's findings match a teacher's (step 7).
- The real cost of planning (step 3 measures it).
- Whether a base text helps in ELA and science as it did in math (only the two small trials in step 5 can say).

## 6. For Cory

1. **Answered 2026-11-13: re-plan first, unit 8 test dropped.** **Unit 4, sections 2 to 4, and the unit 8 test.** The go rule was mixed: writer and rights passed; the expert
   criterion could not be measured, and like-for-like findings were the lowest yet. Recommended: re-plan sections 2
   to 4 from a source map first, then write (step 3), and drop the separate unit 8 test you approved, since unit 4
   is the harder and more telling case; keep unit 8 only if unit 4's result is unclear. Alternatives: write days 29
   to 38 now from the existing plans; or re-plan and also run unit 8.
2. **What starts the ELA and science pilots** (card q-plan-after-11-1 says "once 11.1 has its teacher read"). Your
   mom, a grade 2 teacher, looked at unit 11, which you judged enough to lift the planning freeze; on 2026-11-13 you
   made the expert the teacher reader for now; no grade 3 to 5 teacher is named yet, so waiting has no end date.
   Recommended (middle): start the pilots now on the expert stand-in, and call nothing finished (11.1 or either
   pilot) without a grade 3 to 5 teacher's read. Alternatives: wait for that teacher; or count the stand-in fully.
3. **People and timing** (FOUNDATION 7.5): who and when for the grade 3 to 5 teacher and the math content reviewer;
   whether you will paste the Codex different-model read into your queue (unit 4 section 2, before 2026-11-30); and
   when grade 4's frame counts as built, which unholds its key tools. Recommended for the last: when step 2's CSVs
   and source map exist for grade 4 and unit 4 is re-planned.

## 7. What the independent check corrected (from draft 1)

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
