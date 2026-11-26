# Scope and sequence: Computer Science, Grade 3

Course `computer-science-grade-3`, grade 3, draft scope and sequence, 2026-11-26, written from the frame
(docs/courses/computer-science-grade-3/frame.md), and fixed 2026-11-26 from the expert read
(docs/reviews/sequence-computer-science-grade-3-fixes-2026-11-26.md). The days live in
data/plans/computer-science-grade-3/days.csv; this page holds the judgment.

**Calendar.** 32 sessions, one a week of about 40 minutes (a special, so it does not count against the classroom
teacher's stagger, CALENDAR.md rule 1). Course day n sits in week n, and `school_day` is filled as **school day = 5n**
(the last school day of week n), so week = (school_day - 1) // 5 + 1 = n. The checks fall where the frame sets them:
the mid-year course-level check on day 11 (week 11) and the year-end on day 26 (week 26), with their respond days in
weeks 12 and 27. Unit 3's end-of-unit assessment (day 20) sits in core check week 20 and unit 5's (day 31) in core
check week 31; both are unit assessments, not course-level checks.

**Every session** from day 2 on opens with the three-minute retrieval trace (day 1 opens with its hook, then its
grade 2 retrieval); device sessions keep their last four minutes to save or print, shut devices and collect papers,
and carry the frame's safety line (two hands, cords behind the table). Every device day has its paper path named in its
note; the three editor modes queued in later.csv L148 are not needed in grade 3, where the paper path meets every id
but E3-PRO-PD-04 in full (frame Devices).

**Day kinds** follow docs/GLOSSARY.md: a standard's first day in the course, or the first teaching of a method, is
Understanding, even where it designs or weighs a case (days 4, 10, 16, 19, 24, 28, 29 and 30); a modify day on a
row already taught is Fluency (days 8 and 14); the make days 9 and 15 are Application.

**Readiness and retrieval (rule 2).** Every earlier-grade row the course assumes was last used in grade 2 (the year
before), so each opens as a retrieval task inside the session that first uses it, with its id in `retrieves`, and no
unit has a readiness check:

| Grade 2 row | Last used | Treatment | Day |
|---|---|---|---|
| g2-io-parts | grade 2 unit 1 | retrieval | 1, 2, 5 |
| g2-online-consequences | grade 2 unit 1 | retrieval | 3 |
| g2-benefits-harms | grade 2 unit 1 | retrieval | 4 |
| g2-algorithm-loops | grade 2 unit 2 | retrieval | 7 |
| g2-algorithm-peers | grade 2 unit 2 | retrieval | 10 |
| g2-code-loops | grade 2 unit 3 | retrieval | 13 |
| g2-explain-build | grade 2 unit 3 | retrieval | 17 |
| g2-name-and-label | grade 2 unit 3 | retrieval | 18 |
| g2-debug-loops | grade 2 unit 3 | retrieval | 19 |
| g2-data-types | grade 2 unit 4 | retrieval | 22 |
| g2-data-questions | grade 2 unit 4 | retrieval | 24 |
| g2-ai-training-data | grade 2 unit 4 | retrieval | 25 |
| g2-interests-careers | grade 2 unit 5 | retrieval | 28 |
| g2-people-solve | grade 2 unit 5 | retrieval | 29 |

Other sessions retrieve an earlier grade 3 unit (the system-diagram trace on days 8 and 16, the network-diagram on
day 9, a choice card on days 14, 15 and 20, a trace-table on day 23, the sorter on day 30, two algorithms on day 31).

## Unit 1. Software, the internet and what we share (days 1 to 6, weeks 1 to 6)

Concept area: systems and security, with computing and society. The arc runs from inside one device to many: software
as the instructions between a click and the screen (day 1, at the device), then a message carried across a network
and the cloud as other people's computers (day 2, act-out, then one screen), then what that network carries about us
(day 3, pretend pages), then who gains and who is harmed by systems built on it (day 4). Software comes before the
internet so the cloud is read as computers running software; sharing follows the network it travels on; the
benefit-risk-chart closes the unit so unit 2 can reuse it. Four teaching days for four rows: days 1 to 3 are one
row each, and day 4 carries the two ids of g3-benefits-risks on one chart.

- **End-of-unit assessment, day 5:** a paper sitting of about 25 minutes with unseen items, one prompt per id
  (E3-SYS-HW-12, E3-SYS-NT-14, E3-SYS-SE-13, E3-SOC-ET-17, E3-SYS-IM-15). Response time: the respond day, day 6.
- **Candidate:** kept, the base's networks-of-networks order inside day 2, zero added days.
- **Sensitive:** day 3 (online safety and personal information, health's steps word for word); day 4 (location
  sharing told as something that can happen to anyone). Day 2's act-out is at a walk in a cleared room.

## Unit 2. Algorithms that choose (days 7 to 10, weeks 7 to 10)

Concept area: algorithms and design. Day 7 shows the choice card worked and traced (with the sorting tree from the
base), day 8 modifies a working game algorithm, day 9 makes the pair's own, and day 10 compares two algorithms for one
job by their effect on people, on unit 1's benefit-risk-chart. That is trace, modify, make on g3-algorithm-combo
(three days for the row that carries unit 3), then one day for g3-algorithm-effects. Day 9's card sets, with their
authors named, are the programs unit 3 builds.

- **End-of-unit assessment:** the mid-year course-level check on day 11 stands for it (frame Days), and day 12 is its
  respond day. See "For the lead" 1 on the gate.
- **Candidate:** kept, a drawing algorithm with a choice beside the game on days 8 and 9 for children who cannot do the
  moves, zero added days.
- **Sensitive:** day 10 (disability and access; invented people; talk on the rule and the route).

## Unit 3. Programs that choose (days 13 to 21, weeks 13 to 21)

Concept area: programming. In the progression's in-grade order: day 13 traces and predicts a worked program and puts
its shuffled blocks back (the block-and-text-view met here), day 14 modifies it, day 15 makes the pair's own unit 2
algorithm as blocks with its credit line, day 16 trades for feedback and improves (E3-PRO-PD-05), day 17 reads what a
part is for, day 18 names a variable and fills the first trace-table, and day 19 debugs with that trace-table. No make
comes before a trace or modify on the same construct, and debugging comes after the trace-table it uses. Seven
teaching days for four rows: g3-make-improve holds two ids and the whole trace, modify, make, feedback order (four
days); the other three rows take one each.

- **End-of-unit assessment, day 20:** the paper sitting (E3-PRO-RD-07, E3-PRO-VD-06, E3-PRO-TR-08, one prompt per id)
  and a two-minute feedback item scoring E3-PRO-PD-05 (a new short program and a partner's look-for form with one
  suggestion: the change the child would make and what they would test), with each child's five-minute solo build at
  the pair's device scoring E3-PRO-PD-04 on a short rubric (each structure present, it runs, it matches the
  algorithm, credit line present). The solo build codes a student-created algorithm: the child's own day 11
  field-day algorithm, returned with its marks on day 12, or a classmate pair's day 9 card set with its authors named;
  Curio Class supplies none, since E3-PRO-PD-04 says student-created. The day 16 line and the pair program are
  supporting evidence. With few devices the solo turns run at stations through day 20 and the first half of day 21;
  on one screen through days 20 and 21 as time allows, with those not reached recorded on the no-device path.
  Response time: day 21, at the device.
- **Pairs:** driver and navigator switch at the halfway signal on every pair device day (day 20's solo turns
  excepted). Each device day names its paper path: paper block cards with if and else cards, the printed
  block-and-text-view, and a partner who runs the cards as the computer.
- **Candidate:** kept, modifying a game (day 14) before designing one (day 15), zero added days.
- **Leans:** science s3-design-problem (day 15) and ELA e3-writing-process (day 16) are met before in calendar.csv;
  math m3-two-step-problems first appears on math day 54 (week 11), before day 18, but the day keeps the frame's
  bridge (one variable, a known start).

## Unit 4. Checking data and asking everyone (days 22 to 25, weeks 22 to 25)

Concept area: data and analysis, with machine learning. Day 22 checks a table before anything is read from it, day 23
reads two attributes on a scaled picture graph (two rows, windy days and calm days, each counting cold and warm days;
by hand, then the same graph in a tool that opens with the table entered), day 24 designs a collection everyone can
answer, and day 25 runs the class as a sorter whose training set leaves a kind out, the same idea as day 24's survey.
The sorter decides only by the yes or no feature questions the class writes from the training cards, so it makes the
predicted mistakes on side-view spiders. One day per row, as the frame sets.

- **End-of-unit assessment:** the year-end course-level check on day 26 stands for it, with day 27 as its respond day
  (see "For the lead" 1).
- **Candidate:** kept, the base's "data for answers" step inside day 23, zero added days.
- **Leans:** math m3-scaled-graphs is met before (weeks 1 to 5); science s3-weather-data comes later (from week 25), so
  day 23 uses the science weather log where a class keeps one, or a supplied table invented for practice.
- **Sensitive:** day 24 (data about people, language and disability; no names, an opt-out box, neutral topics).

## Unit 5. Computing at work, then and now (days 28 to 32, weeks 28 to 32)

Concept area: computing and society. Day 28 matches workers to tools and skills, day 29 orders one activity at three
times on the timeline, and day 30 asks why three tools were built, the last of them an AI system that ties back to
unit 4's sorter. Each society day (and day 4) gives two brief views with one dated source each; where no source is
named yet, the note says it is picked and dated when the cards are written. Day 29's paying steps are cash counted
out with a written bill, a card run through a reader, and a card or phone tapped to pay. The voice helper's use by a
person who cannot easily see a screen is kept only if a dated source supports it. One day per id.

- **End-of-unit assessment, day 31:** a paper sitting with unseen items, one prompt per id (E3-SOC-CE-19,
  E3-SOC-HI-16, E3-SOC-HU-18). Response time: day 32, kept as its own session.
- **Candidate:** dropped, a visit by a school worker who uses computing (the case cards carry the row, and a visit needs
  a school's own arrangement), zero days.
- **Sensitive:** day 28 (families' work: no child asked about a family member's job); days 29 and 30 (older ways shown
  with respect).
- A school may leave this unit out (frame Swap or leave out); the three SOC ids are then not claimed that year.

## Course-level checks

| Check | Day (week) | Respond | Samples |
|---|---|---|---|
| Mid-year, standing for unit 2's end-of-unit | 11 (11) | 12 (12) | Unit 2 in full (E3-ALG-PS-01, E3-ALG-IM-03); unit 1 by two new items (E3-SYS-HW-12, E3-SYS-SE-13) |
| Year-end, standing for unit 4's end-of-unit | 26 (26) | 27 (27) | Unit 4 in full (E3-DAT-DC-09, E3-DAT-DI-10, E3-DAT-IM-11 on a half-filled planning sheet, E3-ALG-ML-02); unit 3 by two new items (E3-PRO-VD-06, E3-PRO-TR-08) |

Each check is the end-of-unit assessment of the unit it follows, so no unit assessment comes just before it to repeat;
its samples of earlier units are drawn from those units' content with new tasks, never the day 5 or day 20 items. The
year-end plan item gives the topic and question, and the child fills whom to ask, how, how everyone can answer, the
opt-out box and one group a different plan leaves out, so the sitting holds about 18 minutes for unit 4 and 7 for
the two samples.

**Owned codes not sampled on a check day (rule 3),** each with its reason: E3-SYS-SE-13 at year-end (scored on day 5
and sampled on day 11, so the year-end sitting is not loaded with a third pretend post); E3-SYS-NT-14, E3-SOC-ET-17 and
E3-SYS-IM-15 (scored on day 5; the record is carried unscored at mid-year, since a 25-minute sitting holds the two unit
2 performances and two short samples); E3-PRO-PD-04, E3-PRO-PD-05 and E3-PRO-RD-07 (scored on day 20; PD-04 needs the
device build and PD-05 its own feedback item on day 20, with a feedback record behind it; RD-07 is carried with them so the year-end
sitting stays near 25 minutes); E3-SOC-CE-19, E3-SOC-HI-16 and E3-SOC-HU-18 (unit 5 comes after the year-end check and
is scored on day 31).

## Shorter path

**A shorter session (30 minutes).** The retrieval trace stays at three minutes and the device close at four, so a
session teaches about 23 minutes: each teaching day keeps its one worked example and its exit ticket and drops its
second example (the second sorting-tree group on day 7, the second read program on day 17, the fourth buggy program on
day 19, the third case on days 28 and 30); the check and end sittings keep one prompt per id at about 20 minutes, with
the day 20 solo builds unchanged.

**A year about 10 school days short** (two weekly sessions) folds in two modify days, nothing assessed and no owned
part cut:

| Fold-in day | Folds into | Minutes saved |
|---|---|---|
| Day 8 (modify the game algorithm) | The last 10 minutes of day 7 change one card of the worked algorithm; day 9 opens with the partner check of one changed path before the make | 40 |
| Day 14 (modify the game program) | The last 10 minutes of day 13 change the repeat count and run (day 13 drops its second predict program and keeps the shuffled reorder); day 15 opens with one changed question before the build | 40 |

Total: 80 minutes, two of the 32 sessions, 30 left. Trace still comes before modify before make in both units. Respond
days and check days are never folded. With both folds the checks sit in weeks 10 and 24 (the mid-year check becomes
session 10, the year-end session 24); the lead's calendar pass confirms them. No Specialty id is claimed, so the
Specialty share stays at zero on this path too (bar C1).

## Base text and unloaded sources

The partial base (the archived Teach Computing Curriculum, 2023) is not yet in the source store (later.csv L149), so
the days that adapt it lean on an unloaded source and are placed from its unit pages only: day 2 (Year 3 "Connecting
computers" 4 to 6; Year 4 "The Internet" 1, 2 and 4), day 3 ("The Internet" 3), day 7 (Year 3 "Branching databases" 3
and 4), days 13 to 16 (Year 4 "Repetition in games" 2, 4, 5 and 6), days 22 to 24 (Year 4 "Data logging" 1; 4 to 6
merged; 2). Each such day names its base lessons in its note; every other day is our own and says so. The frame's
source map holds the left-out lessons and their reasons. No day leans on the NOAA extract (grade 11).

## For the lead

1. **source-map.csv** waits on L149: the base is not loaded, so the base lessons and their days stay in the notes and
   the section above (lead call 2026-11-26). Write source-map.csv when the store folder is made.
2. **Device count.** The frame counts 12 device sessions; the pair-device days are 11 (1, 13 to 19, 20, 21, 23) plus
   day 2 on one screen. No change asked, only the count's wording.
3. **Stagger:** this course is a special and does not count under rule 1; week 26 also holds other specials'
   year-end checks (frame For the lead 1).
