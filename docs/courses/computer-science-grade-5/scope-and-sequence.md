# Scope and sequence: Computer Science, Grade 5

Course `computer-science-grade-5` (catalog id `cs-k12`), grade 5, draft, written 2026-11-26 from the frame
(docs/courses/computer-science-grade-5/frame.md). The days live in data/plans/computer-science-grade-5/days.csv; this
page holds the judgment. Standards: 2026 CSTA PK-12 Computer Science Standards (CC BY-NC-SA 4.0), cited by id only.

## On the first page

- **Meeting days.** One session a week of about 40 minutes, 32 weeks, a specials rotation. Course day n falls in
  week n. A session opens with the three-minute retrieval trace from day 2 on (check days excepted: the paper takes
  the session); device sessions keep four minutes at the end to save, close and put devices away.
- **How `school_day` is counted.** `school_day = 5 x n` for course day n, the last school day of week n, the same
  place frame.py's even spread puts it, so the week is `(school_day - 1) // 5 + 1 = n`. Every unit day, end-of-unit
  assessment and course-level check sits on the week the frame gives (checked day by day, 2026-11-26).
- **The calendar rule.** In K to 5 computer science is a special and does not count against the classroom teacher's
  stagger (docs/courses/CALENDAR.md rule 1). The two course-level checks still sit off every grade 5 core check week.
- **Kinds of day.** Set by docs/GLOSSARY.md (row "teaching day"): a day that carries an owned code for the first time,
  or first shows a method, is Understanding even where its second half is a make (days 8, 14, 15, 16, 22, 24 and 27
  to 30 among them); the frame's Day kinds bullet now says the same (fix pass, 2026-11-26). Modify days are Fluency (days 12 and 23); make days that build on earlier days of the same
  code are Application (days 7 and 17).
- **Readiness and retrieval.** Every grade 5 row assumes a grade 4 row taught the year before (grade 4 computer
  science), so no unit has a readiness check and each assumed row opens as a retrieval task (the `retrieves`
  column). Earlier-grade rows, last use and treatment:

| Row assumed | Last use | Treatment | Day |
|---|---|---|---|
| g4-troubleshoot | grade 4 unit 1 | Retrieval | 1 |
| g4-wired-wireless | grade 4 unit 1 | Retrieval | 2 |
| g4-authn-authz | grade 4 unit 1 | Retrieval | 3 |
| g4-written-algorithm | grade 4 unit 2 | Retrieval | 6 |
| g4-algorithm-groups | grade 4 unit 2 | Retrieval | 8 |
| g4-trace-values | grade 4 unit 4 | Retrieval | 11 |
| g4-debug-increment | grade 4 unit 4 | Retrieval | 13 |
| g4-compare-solutions | grade 4 unit 4 | Retrieval | 15 |
| g4-team-document | grade 4 unit 4 | Retrieval | 16 |
| g4-table-tool | grade 4 unit 3 | Retrieval | 20 |
| g4-data-explain | grade 4 unit 3 | Retrieval | 21 |
| g4-ml-learning | grade 4 unit 5 | Retrieval | 22, 29 |
| g4-data-people | grade 4 unit 3 | Retrieval | 24 |
| g4-history-limits | grade 4 unit 5 | Retrieval | 27, 29 |
| g4-resources | grade 4 unit 1 | Retrieval | 28 |
| g4-work-tools | grade 4 unit 5 | Retrieval | 30 |

  The other opening traces bring back this year's earlier units (system-diagram on 7 and 12, flowchart on 11 and 14,
  the triangle on 17 and 24, debugging on 23, design for users on 16 and 27, the model on 29, team roles on 30).
- **Devices.** Of the 726 teaching minutes (22 sessions of about 33), about 300 are at a device once the on-device
  trainer exists, a little over 40 percent, on days 1 (part), 11 to 17, 20, 21 (part), 22 and 23; about 245 now, a
  third of the teaching time, because days 22 and 23 run on the paper path until it does. The check rotations and day
  19's device items add about 32 minutes. Each device day names its paths in its note, with what a pair or team does
  with no device, and every pair device day names the driver and navigator switch at the halfway signal (day 16
  keeps its team roles). Three ids are met in full only on a device
  and are marked part met without one: E5-PRO-VD-06, E5-DAT-DC-09, E5-ALG-ML-02. The on-device sorter trainer is not
  built yet (later.csv L148), so days 22 and 23 run on the paper path for now and E5-ALG-ML-02 stays part met until it
  exists. On the paper path the model is a partner (or a card procedure) who may look only at the training cards and
  labels each test card by the training card it matches most closely on stated features (size, number of corners,
  line thickness, tilt), never by knowing the shape, so the day 20 anchor (small tilted triangles mislabeled) and day
  23's changed count both happen on paper.
- **Sources not yet loaded** (later.csv L149). The partial base, the archived Teach Computing Curriculum 2023 Year 6,
  is placed from its public unit pages only. Days that lean on it: 3, 6, 7, 11, 12, 15, 16, 17, 20, 28 and 30
  (the frame's Source map; no source-map.csv until the base is loaded, L149). Each stays provisional until the store folder exists and its third-party check is done.

## The calendar

| Unit | Course days | Weeks | Days | Concept area |
|---|---|---|---|---|
| 1. How a message travels | 1 to 5 | 1 to 5 | 5 | Systems and security |
| 2. Flowcharts for a game | 6 to 10 | 6 to 10 | 5 | Algorithms and design |
| 3. Programs that keep score | 11 to 17 | 11 to 17 | 7 | Programming |
| Mid-year check and respond | 18, 19 | 18, 19 | 2 | |
| 4. Data that trains a model | 20 to 24 | 20 to 24 | 5 | Data and analysis, with machine learning |
| Year-end check and respond | 25, 26 | 25, 26 | 2 | |
| 5. Who computing includes, and who decides | 27 to 32 | 27 to 32 | 6 | Computing and society, with systems impacts |

28 unit days and 4 course-level days, 32 in all; units and day counts are the frame's, unchanged.

## Unit 1. How a message travels

Days 1 to 5, weeks 1 to 5. Concept area: systems and security; practices IC3, CT6, CT7, HCD12, ESR2.

Arc: the anchor note typed on one device and read on another is traced first through one machine (day 1, the
four-part system-diagram, acted then typed), then across the room (day 2, the network-diagram, acted with yarn), then
asked what keeps it safe (day 3, the cia-triangle). The order is the frame's: the triangle's threats happen at places
on the network-diagram, so the network comes first. Three rows, three teaching days, one id each.

Assessments: end-of-unit paper on day 4 (about 25 minutes, unseen: a new system-diagram, new network part cards, four
new threats, at least one a side), a prompt for each part of each id (for E5-SYS-HW-12, each of the four
operations with its hardware part and its software); response time on day 5. No readiness check (grade 4 rows, retrieved).
Candidate: kept, the base's "what to share, then why" order inside day 3, zero added days. Sensitive: day 3's
passwords and personal information (paper accounts only; health's steps on the teacher page). Safety lines on days 1
to 3 as the frame gives them.

## Unit 2. Flowcharts for a game

Days 6 to 10, weeks 6 to 10. Concept area: algorithms and design; practices CT6, CT7, CT8, IC3, HCD10, ESR1.

Arc: a given step-counter flowchart is traced and its goal changed (day 6), pairs design and draw their own score game
flowchart (day 7), then human-centered design is taught on a given library catalog page and used to change one rule of
their own game for a player it leaves out (day 8). Trace, then make, then design for users, so the games handed to
unit 3 are already checked for who they serve.

Assessments: end-of-unit paper on day 9 (a new flowchart drawn and traced; a new technology read for two design ideas
and one change), response on day 10, which also fixes each pair's flowchart before it becomes unit 3's plan. The day 9
record for E5-ALG-IM-03 is carried unscored into the mid-year check. Candidate: kept, the base's design-sheet order
(player, rules, score, end) on day 7, zero added days. Math lean: m5-two-patterns comes later (math unit 10, weeks 27
to 30), so days 6 and 7 carry the frame's bridge (a counter that adds the same amount each time, no second pattern).
Sensitive: day 8's disability content.

## Unit 3. Programs that keep score

Days 11 to 17, weeks 11 to 17 (they cross the core check weeks 11, 16 and 17; the unit holds no course-level check).
Concept area: programming; practices CT7, CT8, CT9, HCD11, IC4, IC5, ESR2.

Arc: trace before modify before make on each construct. Variables are traced with paper cups and then in the editor
(day 11) and modified (day 12); debugging is taught as a method, two strategies (day 13) then a third and a pair's own
choice of two (day 14); a worked remix is traced before pairs make one (day 15); the team reads a worked timer component
with its comment and note, then builds components from a unit 2 flowchart, the movement from a partly finished shell
(day 16) and a non-author assembles and tests them (day 17). The team project comes last because it uses all
four rows.

Assessments: the mid-year check (day 18) stands for the end-of-unit assessment, with the day 17 revised project scored
there with an individual record for each student; day 17 is a teaching day, scored, not an assessment sitting. Day 14's test-tables are kept as evidence, not
scored. Response time: day 19. Candidate: kept, the base's improve-and-share step folded into day 17's test by a
non-author, zero added days.

## Unit 4. Data that trains a model

Days 20 to 24, weeks 20 to 24. Concept area: data and analysis, with machine learning; practices CT7, CT8, CT9, IC3,
ESR1, ESR2.

Arc: collect and organize (day 20), see that repeated measures differ (day 21), train and test a model (day 22),
retrain after finding what is missing (day 23), then weigh the benefits and risks of tools that learn from collected
data (day 24), right after students have made a model that was wrong for some shapes. Until the trainer exists the
model on days 20, 22 and 23 is the paper partner model (On the first page, Devices).

Assessments: the year-end check (day 25) stands for the end-of-unit assessment, with day 23's model record scored there
(the session after the row is first taught); day 23 is a teaching day, scored, not an assessment sitting. Response time: day 26. Candidate: kept, the base's
collecting-then-formatting order on day 20, zero added days. Science lean: s5-design-test comes later (science unit 6,
weeks 25 to 30), so day 21 carries the frame's bridge (the day teaches why trials differ and plans no fair test). Data is
about things, never people; no camera or microphone.

## Unit 5. Who computing includes, and who decides

Days 27 to 32, weeks 27 to 32, after the year-end check. Concept area: computing and society, with systems impacts
(E5-SYS-IM-15); practices ESR1, HCD10, HCD12, CT6, IC3.

Arc: who a tool includes or leaves out (day 27, on the timeline), how systems change culture and work (day 28), when a
person, not a computer, should decide, and how a family chooses (day 29), and how professionals share work with digital
tools (day 30). Day 27 teaches two cases whole (the name form, captions) and three by pair jigsaw. Each society day gives two views and one dated source a case, no company named.

Assessments: end-of-unit paper on day 31 (week 31, a unit assessment, not a course-level check), one prompt per id on
new cases; response on day 32. Candidate: dropped, the interview with a school worker (case cards carry the id, and a
visit needs the school's own arrangement), zero days. Sensitive: days 27 (disability, language, naming, culture; the
starting pack first), 28 (work and automation), 29 (a pictured family only).

## Course-level checks

| Check | Day | Week | Respond | What it samples |
|---|---|---|---|---|
| Mid-year, standing as unit 3's end-of-unit assessment | 18 | 18 | 19 (week 19) | Unit 3 in full (written trace and debug items, the remix rotation, the day 17 record); units 1 and 2 by three new items (E5-ALG-PS-01, E5-SYS-SE-13, E5-SYS-HW-12) |
| Year-end, standing as unit 4's end-of-unit assessment | 25 | 25 | 26 (week 26) | Unit 4 in full (the form and table rotation, variability, a data case, the day 23 record); units 1 to 3 by three new items (E5-SYS-NT-14, E5-PRO-VD-06, E5-PRO-TR-08) |

Both checks are their unit's end-of-unit assessment, so no assessment just given is repeated: the unit 3 and 4 items are
those units' own unseen items, and the earlier units' items differ in form from the day 4 and 9 papers. Each reuses its
scored record (day 17, one week before; day 23, ten school days before) and never collects it again. Day 25's data case
is answered in two sentence frames, not the benefit-risk-chart of day 24 a week earlier (an item-level choice, made here).

Codes not sampled on a course-level check, and why: E5-ALG-IM-03 is assessed on day 9 and carried unscored into day 18;
the five unit 5 ids (E5-SOC-HI-16, E5-SYS-IM-15, E5-SOC-ET-17, E5-SOC-HU-18, E5-SOC-CE-19) are taught after the
year-end check, where the frame places unit 5, and are assessed by day 31 (For the lead 1).

The check weeks 18 and 25 sit off the grade 5 core check weeks (10, 11, 16, 17, 21, 22, 29 to 32). Overlaps with other
specials in week 18 are the lead's calendar pass (frame For the lead 1).

## Shorter path

- **A shorter period (30 minutes).** The retrieval trace stays at three minutes and device put-away at four, so about
  23 minutes teach. Device days run the station path (fewer devices out, shorter set-up). Days 15 to 17 are the
  tightest: day 16's unfinished components carry into day 17's first ten minutes, and day 17's project note is finished
  on paper. The check days drop their opening and keep their written and rotation minutes; nothing assessed is cut.
- **A year about 10 school days short (two weekly sessions).** Named fold-in days, nothing assessed and no owned part
  cut:
  1. Day 12 (modify variables, Fluency) folds into day 11's last eight minutes and day 13's opening trace (a modified
     score program). Day 11 keeps the score program only; its countdown and password programs move into day 13's
     buggy set, which frees the eight minutes: saves 40 minutes.
  2. Day 5 (unit 1 respond) folds into day 4: the paper's last ten minutes are a self-check against a posted key on
     the two items the teacher expects most to miss, and the error-letter reteach becomes day 6's five-minute opening
     once the papers are marked (APPROACH.md "How a day opens", (b)): saves 40 minutes.
  3. Day 10 (unit 2 respond), the same way into day 9, only if a third session is lost; day 10's flowchart fixes move
     to day 11's opening trace (a pair's own flowchart): saves 40 minutes.

  Folds 1 and 2 take the year from 32 to 30 sessions (80 minutes saved); all three to 29 (120 minutes).

## For the lead

1. **L107 for this course.** Six of 19 ids are never sampled by a course-level check, because unit 5 follows the
   year-end check (frame placement); the expert read (2026-11-26) finds this met by L107's naming rule. If Cory wants
   every id on a check, the year-end check would need to follow unit 5, in week 31 or 32, both core check weeks.
