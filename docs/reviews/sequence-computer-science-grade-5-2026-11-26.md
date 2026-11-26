# Expert read: scope and sequence, Computer Science, Grade 5 (2026-11-26)

Course `computer-science-grade-5`. Brief: docs/pipeline/briefs/sequence-read.md, through build/scope-writes/CS-READ.md.
Cold read: the scope was written by a fresh agent; this reader wrote none of it.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/computer-science.md; docs/ADOPTION-BAR-SUBJECTS.md part 5;
  docs/courses/computer-science/STANDARD.md and APPROACH.md in full; build/scope-writes/CS-BRIEF.md.
- docs/courses/computer-science-grade-5/scope-and-sequence.md and data/plans/computer-science-grade-5/days.csv in full;
  the frame docs/courses/computer-science-grade-5/frame.md in full.
- The g5 rows of data/progressions/computer-science.csv; the E5 statements in data/standards/csta-2026-statements.txt
  (planning only, not quoted here).
- data/plans/calendar.csv for grade 5 math, grade 5 science and grade 4 computer science (to check the leans and each
  assumed row's last use); the grade 5 line of `frame.py calendar`.
- The DESK-ANSWERS entry "2026-11-26: after-core frame calls"; later.csv L107, L148, L149; GLOSSARY row "teaching day";
  scripts/sequence.py (the 2026-11-26 check-after rule).
- Earlier reads, for repeats: docs/reviews/frame-computer-science-grades-1-to-5-2026-11-25.md, and today's sequence reads
  for computer science grades 6 and 11, music 3 to 5, theater 3 to 5 and visual arts 3 to 5.
- Two outside pages, for the unit 5 work case (Sources).

Gates run first: `plan.py check` (0 failures for this course), `sequence.py check computer-science-grade-5` (0
failures), `frame.py check` (frame 0 failures; 5 units, 32 days), `frame.py calendar` (grade 5 computer science weeks
18 and 25), `stale.py check` (no line in this course). What they settle is not repeated below.

## Verdict

The scope is sound and close to ready: the unit order, the trace, modify, make order, the retrieval table, the check
weeks, the leans and the id placement all hold, and every owned id is on a teaching day. The biggest risk is the
machine learning pair of days (22 and 23): they run on the paper path for the whole year until the trainer exists, the
unit's scored record comes from day 23, and the paper "pretend model" is not specified well enough for a writer to
build a day where the model's answers come from its training data. Fix that, add a worked component before the team
build, drop the `end` marks the gate no longer needs, and tighten five assessment prompts; the rest is small.

## Findings, most serious first

### 1. The paper path for training a model does not say how the pretend model decides (days 22, 23)

LAYER sequence. REPEAT new. Confidence: likely.

**What is wrong.** Until the on-device trainer exists (L148) days 22 and 23 run on paper, so the paper path is the
course for now. Day 22's note says only "the class sorts cards as a pretend model with a training set and a test set";
day 23's says "the student chooses the examples and predicts". Nothing says what rule the pretend model follows. Read by
a busy writer, the "model" is a student who looks at a test card and names the shape, which is the student classifying,
not a model trained on data. Then the day 20 anchor (a model that calls every small triangle a circle) cannot happen,
day 23's retrain cannot change the count out of ten, and the day 23 scored record measures nothing about training.

**Why it matters.** E5-ALG-ML-02 is already part met on paper; with an unspecified rule it is not met even in part, and
the lens's misconception "AI is a thinking being" is taught rather than countered.

**Fix (settled below).** Day 22 and 23 notes: the model is a partner (or a card procedure) who may look only at the
training cards and labels each test card with the label of the training card it matches most closely on stated
features (size, number of corners, line thickness, tilt), never by knowing the shape. A training set with only large,
upright, thick-lined triangles then mislabels small tilted ones, so the day 20 anchor shows on paper, and day 23's added
examples change the count. Day 20's hook: on the paper path, a printed result card of that model's wrong answers.

### 2. The team build (day 16) has no worked component or project note shown first, and one component was never traced

LAYER sequence. REPEAT yes (grade 11 read, "Day 40 reads like a make day before the make"). Confidence: likely.

**What is wrong.** Day 16 is the first day of E5-PRO-PD-05 and E5-PRO-RD-07. Students build a component and write an
inline comment and a project note, but no worked component with its comment and note is read first; the only read of
documentation is the three-minute retrieval. Of the three components, the score (days 11, 12) and the timer (day 11's
countdown) were traced this year; "the movement" was not traced or modified on any grade 5 day.

**Why it matters.** APPROACH.md: "no 'try it' on a construct before one worked example has been shown and traced"; the
lens flags a build before any trace or modify task. A writer builds day 16 as a blank-editor day for the movement
student, and a project note with no model is the weakest part of the day 17 scored record.

**Fix (settled below).** Day 16 goal opens with a worked component (a finished timer block with its comment and a
three-line project note) read in the text view and placed by following its note, about 6 minutes. The movement
component is given as a partly finished shell (as day 17's supplied variable shell is), so its student modifies before
making.

### 3. Days 17 and 23 carry `assess` = `end` on teaching days; the gate no longer needs it

LAYER sequence, process. REPEAT yes (grade 6 read finding 5, grade 11 read finding 2). Confidence: firm.

**What is wrong.** sequence.py now accepts the course-level check on the day after a unit's last day as that unit's
end-of-unit assessment (lead, 2026-11-26). Day 18 follows unit 3's last day (17) and day 25 follows unit 4's last day
(24), so both units are covered. The `end` marks on days 17 (Application) and 23 (Fluency) now tell a lesson writer
these teaching days are assessment sittings. The .md repeats it ("marked `end`, part 1" in units 3 and 4) and For the
lead 1 asks for a gate fix that has landed (stale).

**Fix (settled below).** Blank `assess` on days 17 and 23. Keep each note's scored-record sentence, reworded: "the
revised project (day 23: the training record) is scored here and carried into day 18's (day 25's) check, which is the
unit's end-of-unit assessment". Delete "marked `end`, part 1" from the .md's unit 3 and unit 4 Assessments lines and
delete For the lead 1.

### 4. Five assessment prompts miss a part of their code

LAYER sequence. REPEAT yes (music 3 to 5 finding 1, theater 3 to 5 findings 7 and 8, grade 11 finding 3). Confidence:
firm for E5-SYS-IM-15, likely for the rest.

- **Day 31, E5-SYS-IM-15** (culture and the ways people live and work): the prompt asks how a system helps and hinders
  "how people live or work"; culture, which day 28 teaches (how families keep in touch, how news spreads), is not
  asked. Fix: "one way a new system changes culture or how people live, and one way it changes work, each a help or a
  hindrance".
- **Day 31, E5-SOC-HI-16** (inclusion or exclusion shaped design, development and societal impact): "what it changed"
  lets a student answer only for people. Fix: two lines, what it changed in how the tool was made, and what it changed
  for the people who use it. Day 27's goal says the same.
- **Day 4, E5-SYS-SE-13**: four threats matched to sides can leave a side unasked. Fix: at least one threat per side,
  and the reason says why that side matters for the information in the threat.
- **Day 4, E5-SYS-HW-12** (hardware and software work together for input, output, processing and storage): the
  look-for names "hardware, software and where data is kept". Fix: for each of the four operations in the traced task,
  the hardware part and the software doing it.
- **Day 18, E5-PRO-VD-06**: the unseen trace item should hold all three of store, compare and modify (the day 17
  record holds them only for students whose component used a variable). Fix: name all three in the item.

### 5. The shorter-year folds put the response inside the paper session, before anything is marked

LAYER sequence. REPEAT yes (theater 3 to 5 finding 2, grade 11 finding 8). Confidence: likely.

**What is wrong.** Folds 2 and 3 make "the paper's last ten minutes" of days 4 and 9 the response. The teacher has not
marked the papers, so nothing can be retaught by error letter in those minutes. Fold 1 moves day 12's modify into
"day 11's last eight minutes", but day 11 is already full (hook, cups, about 20 device minutes), and a writer cannot
tell what gives way.

**Fix (settled below).** Folds 2 and 3: the last ten minutes are a self-check against a posted key on the two items
the teacher expects most to miss; the error-letter reteach becomes the next session's five-minute opening (APPROACH
"How a day opens", (b)), and day 10's flowchart fixes move to day 11's opening trace (a pair's own flowchart). Fold 1:
day 11 keeps the score program only; the countdown and the password programs move into day 13's buggy set, which frees
the eight minutes for the modify. Nothing assessed or owned is cut.

### 6. Device paths and pair roles are missing from several device days

LAYER sequence. REPEAT yes (pair roles: grade 11 finding 10). Confidence: firm.

**What is wrong.** The .md says "each device day names its four paths in its note". Day 21 (device in part) names no
paths and no no-device version; day 19 (device in part) names none; day 25 says "part met on the paper path" without
naming it; days 16 and 17 list the four paths but not what a team does with no device. Driver and navigator switching
(the frame's IC5 for unit 3) is named only on day 12, and on no unit 4 device day.

**Fix (settled below).** Day 21: "no device: the class sorts the printed ramp times by hand". Day 19: "paper version of
the missed device item". Day 25: "paper form and hand-sorted table". Days 16 and 17: "printed block strips cut and
pasted into a team sheet, the tester acting as the computer". Days 11, 13, 14, 15, 17, 20, 22 and 23: "driver and
navigator switch at the halfway signal" (day 16 keeps its team roles).

### 7. Day 27 holds the hook and five cases, each with two views and a dated source, in one 33-minute session

LAYER sequence. REPEAT new. Confidence: judgment call.

**What is wrong.** The frame's day 27 cases are a name form, a voice tool, captions, a language keyboard and an
English-like early programming language; each needs what happened, two views and a source, then a timeline place and a
list. After the hook there are about 25 minutes. The early programming language case, as written, is inclusion of
non-mathematicians, a weak fit for "diverse individuals and communities" unless its second view is said.

**Fix (settled below).** Two cases taught whole (the name form, captions); the other three as a pair jigsaw, each pair
placing one card and reporting one line. The programming language card's second view: it opened programming to people
who were not mathematicians, and it was written in English words, which left out people who did not read English.

### 8. Small fixes

LAYER sequence. REPEAT yes (stale and miscopied text, music 3 to 5 finding 9). Confidence: firm.

- Day 19 lists g5-team-project in skills but not its codes; day 26 lists g5-train-model but not E5-ALG-ML-02. Make
  skills and codes agree (drop the skill on day 19, where the project cannot be redone; add the code on day 26).
- The .md device line counts days 22 and 23 as if the trainer existed (300 minutes). Say both: about 300 of 726 when the
  trainer exists, about 245 now (a third of the teaching time), and delete the closing "Unsure" line.
- Day 28's labor source is confirmed (Sources): the federal occupational handbook's interpreter and translator page
  (modified 2026-08-27) says AI tools make the work more efficient and many jobs cannot be fully automated; its craft
  and fine artists page (modified 2026-10-29) says AI-made illustrations may compete with illustrators. Those are the
  two views of the case. The teacher source line names them with their dates; no company is named.

## What is right and should not be touched

- Unit order and reasons: systems first, flowcharts as unit 3's plan, programming with all four rows ending in the team
  project, data and the model, society last after the year-end check.
- Trace before modify before make: variables 11, 12, then 16; debugging 13, 14, applied 17; remix traced before made
  on 15; flowchart traced and modified on 6 before the make on 7.
- The retrieval table: every assumed row is a grade 4 row, and each last use checked against grade 4's calendar rows
  (unit 1 days 1 to 6, unit 2 days 7 to 10, unit 3 days 13 to 18, unit 4 days 19 to 23, unit 5 days 26 to 32) is the
  year before, so retrieval, not readiness, is right everywhere.
- All 19 E5 ids sit on teaching days; no id outside the frame is claimed; school_day = 5n puts every unit and check in
  the frame's weeks (18 and 25 for the checks, off the core weeks).
- The math and science leans are later in the year (math unit 10 weeks 27 to 30, science unit 6 weeks 25 to 30, per
  calendar.csv) and both days carry the frame's bridge.
- The kind relabels follow GLOSSARY's first-teaching rule; day 25's sentence frames keep the check from repeating day
  24's chart form.
- Privacy and sensitivity lines are on each flagged day (paper accounts, no home or body questions, invented names,
  pictured family, health's steps on day 3).

## Brief and lens checks

| Check | Result |
|---|---|
| Order inside each unit | Met, except day 16 (finding 2) |
| End-of-unit covers every part | Five gaps (finding 4) |
| Mid-unit assessments | Not applicable: no unit over 25 days |
| Response time counted once | Met |
| Readiness or retrieval | Met; no readiness check is due |
| Checks that do not repeat | Met; both checks are their unit's own assessment, and earlier units' items differ in form |
| Every owned code on a course-level check (L107) | Met by naming: six ids are named with the reason (E5-ALG-IM-03 and unit 5's five, after the year-end check by frame placement); no change asked |
| Standards in full | Met on teaching days; the gaps are in assessment prompts (finding 4) |
| Days by load | Met, apart from day 27 (finding 7); unit 5 carries five ids in four days as the frame sets |
| Calendar | Met; week 18 overlaps with other specials are the lead's calendar pass (frame For the lead 1) |
| Candidate cells | All four settled at zero days (three kept, one dropped with a reason) |
| Shorter path | Present; folds need the fixes in finding 5 |
| Source map | Matches the frame; leaning days named; base not loaded (L149) |
| Device day has a paper path meeting the same ids | Mostly; finding 6 |
| Trace, modify, make; debugging; pair roles; retrieval trace | Met, pair roles under-named (finding 6) |
| Society cases accurate, current, guarded | Met; day 28 source confirmed; day 27 second view added (finding 7) |
| Lens: all five concept areas | Met: one unit each, AI inside data and society |
| Lens: notional machine taught | Met (cups, be the computer, trace-tables, "set score to score plus 1") |
| Lens: unplugged in every unit | Met |
| Lens: no claim that coding improves thinking | Met |
| Bar 8: projects and code with rubrics | Met (day 17 rubric, day 18 debug and remix items) |
| Stale notes | For the lead 1 and the "Unsure" line (findings 3, 8) |

## What I could not judge

- The archived base lessons: not loaded (L149), so the eleven leaning days' order is checked against the frame only.
- Whether a 10-minute device rotation on day 18 gives both students of a pair a full turn; it needs a trial.

## Sources

- US Bureau of Labor Statistics, Occupational Outlook Handbook, Interpreters and Translators,
  https://www.bls.gov/ooh/media-and-communication/interpreters-and-translators.htm (last modified 2026-08-27): the
  translator view for day 28.
- US Bureau of Labor Statistics, Occupational Outlook Handbook, Craft and Fine Artists,
  https://www.bls.gov/ooh/arts-and-design/craft-and-fine-artists.htm (last modified 2026-10-29): the illustrator view
  for day 28.
- Everything else from the repository files above and from memory (the lens's PRIMM and worked-example notes).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Pretend model labels each test card by the closest training card on stated features; day 20 hook gets a printed result card on the paper path | The paper model must learn from its data, or ML-02 is not met even in part | days.csv days 20, 22, 23 |
| Day 16 opens with a worked timer component, comment and note (about 6 minutes); the movement component is a partly finished shell | Worked example before a make; movement was never traced | days.csv day 16 |
| Blank `assess` on days 17 and 23; reword their scored-record sentences; delete "marked `end`, part 1" and For the lead 1 | The gate accepts the check after the unit's last day | days.csv days 17, 23; scope-and-sequence.md |
| Day 31 IM-15 prompt names culture; HI-16 prompt asks what changed in the tool and for its users (day 27 too) | Every part of the code asked | days.csv days 27, 31 |
| Day 4: one threat or more per triangle side; each of the four operations with its hardware and software part | Every part of the code asked | days.csv day 4 |
| Day 18 trace item holds store, compare and modify | Every part of VD-06 asked of every student | days.csv day 18 |
| Shorter year folds 2 and 3: a self-check against a posted key, reteach in the next opening; fold 1: day 11 keeps the score program, the countdown and password programs move to day 13 | Response needs marked work; day 11 has no spare minutes | scope-and-sequence.md Shorter path |
| Paths named on days 16, 17, 19, 21, 25; driver and navigator switch named on days 11, 13, 14, 15, 17, 20, 22, 23 | A device day always has a paper path; pairs have roles | days.csv |
| Day 27: two cases whole, three by pair jigsaw; the programming language card gets its English-only second view | Load in 33 minutes; two views per case | days.csv day 27 |
| Day 19 drops g5-team-project from skills; day 26 adds E5-ALG-ML-02 | Skills and codes agree | days.csv days 19, 26 |
| Device minutes stated as about 300 when the trainer exists, about 245 now; "Unsure" line deleted | Honest count | scope-and-sequence.md |
| Day 28 teacher source line: the two federal handbook pages with their dates | Dated source for each view, no company | days.csv day 28 |

## For Cory

Nothing. The writer's For the lead 3 (six ids not on a course-level check) is met by L107's naming rule; it would
become a question only if Cory wants every id on a check, which would put the year-end check in core week 31 or 32.

## For the source list

- The two Bureau of Labor Statistics handbook pages above opened by automated read on 2026-11-26 (no block).
