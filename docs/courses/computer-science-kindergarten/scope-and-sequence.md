# Scope and sequence: Computer Science, Kindergarten

Course `computer-science-kindergarten` (catalog id `cs-k12`), kindergarten, draft, written 2026-11-26 from the frame (docs/courses/computer-science-kindergarten/frame.md). The days live in data/plans/computer-science-kindergarten/days.csv.

## The course on one page

- **Units and days.** 5 units, 32 course days: units of 6, 5, 9, 4 and 4 days (28), two course-level check days
  (12 and 27) and their two respond days (13 and 28), as the frame sets them. `stretch` is the frame's unit number;
  `unit` is `<unit>.1` (no unit is split into sections at this stage). 22 days teach; days 5, 12, 21, 27 and 31 are
  check days (three end-of-unit assessments and two course-level checks) and days 6, 13, 22, 28 and 32 respond days.
- **How school_day is counted.** One session of about 30 minutes a week for 32 weeks, a specials rotation, so course
  day n falls in week n. school_day = 5n (the last school day of week n, the slot the even spread already gave), so
  week = (school_day - 1) // 5 + 1 = n. A school picks its own day of the week; the week is what CALENDAR.md reads.
  Every unit falls in the frame's weeks: unit 1 weeks 1 to 6, unit 2 7 to 11, the mid-year check week 12 (respond 13),
  unit 3 14 to 22, unit 4 23 to 26, the year-end check week 27 (respond 28), unit 5 29 to 32.
- **A session's minutes.** From day 2 every session opens with the three-minute retrieval task (the `retrieves`
  column names the row); floor-grid and device days keep their last four minutes to put cards, tape and devices away,
  so a session teaches for about 23 minutes. The floor-grid and device safety lines are copied into each such day's
  note, as the frame asks, and each day the frame flags for sensitivity carries its line in the note.
- **Trace, modify, make.** Inside each unit, understanding before modify before make: unit 2 teaches the step-card
  (day 7), modifies a working set (day 8, Fluency) and makes a set (day 11, Application); unit 3 teaches signs, the
  arrow-card program, the picture-block program, tracing and the first wrong step (days 14 to 18), modifies a path
  (day 19, Fluency) and makes one (day 20, Application). Driver and navigator roles switch at the halfway signal on
  days 15 and 20.
- **Device and paper paths.** Device days are 1 (briefly, one screen), 3 (first turn at a station), 16 and 20 (the
  picture-block path). Each is written four ways (one device per pair, stations, one screen, no device). The K to 2
  picture-block mode of our editor is queued with tool work (later.csv L148), so days 16 and 20 run on the paper path
  for now: the picture-block cards and the arrow cards laid on the floor grid. No kindergarten id needs a device to be
  met in full (frame, Devices), so nothing is marked part met.
- **Readiness and retrieval.** No course comes before kindergarten and no kindergarten row has an `assumes` cell, so
  no unit has readiness rows and no day carries a readiness check. Every retrieval is of a row taught earlier this
  year, in the `retrieves` column, spread so each unit's rows come back in later units: k-tools-jobs (days 2, 8,
  29), k-device-manners (3, 4, 7), k-public-private (6, 20), k-follow-steps (9, 10, 14, 32),
  k-sort-attributes (11, 13, 16, 23), k-people-steps (18), the unit 3 rows (15, 17, 19 and 22 inside the unit,
  where each day builds on the one before; 24 and 26 in unit 4), the unit 4 rows (25, 28) and k-devices-places (30).
  Inside unit 3, days 16, 18, 20 and 21 bring back units 1 and 2. Check days (5, 12, 21, 27, 31) open with settling and
  instructions, not a retrieval task: day 5's spoken "what is this tool's job" with the mystery bag stays as
  instructions, not scored, and is not the card match it scores.
- **Evidence.** Kindergarten answers by pointing, sorting, ordering or saying aloud; the teacher notes by exception on
  a class checklist. Each end-of-unit assessment and check is a whole-class paper task of about 15 minutes with
  unseen items, collected from every child, plus one spoken answer per child heard in five groups of six while the
  others finish. For 30 children that is about 4 minutes a group, so at every session length the groups not reached
  are heard in the first 10 minutes of the respond day (6, 13, 22, 28, 32), still one sitting's evidence, collected
  once. Spoken answers are kept short: day 12's three-part EK-ALG-IM-03 answer is prompted by three picture cards
  (choose, parts, order), one word each. Each item asks every part of its id: day 12 has each child follow a new
  picture algorithm (carry out, EK-ALG-PS-01); days 21 and 27 have a dot drawn where the robot is after each card
  (describe how, EK-PRO-RD-06); day 5 matches tool, job and person (for different users, EK-SYS-HW-11); day 31 asks
  home, school and work (EK-SOC-CE-16); day 27's placing of answer cards carries the collect part of EK-DAT-DI-09.
  No score comes from a day that first teaches a row. Response time is the respond day after each sitting, counted
  once.
- **Standards wording.** Days cite ids and state the action in our own words; the credit line "Standards: 2026 CSTA
  PK-12 Computer Science Standards (CC BY-NC-SA 4.0)" goes on each lesson that leans on a statement, and the base
  text's name only in a day's credit line.
- **Sources not yet loaded.** The archived Teach Computing Curriculum (2023) is not in the source store (later.csv
  L149), so the frame's Source map and these days stay provisional. Days leaning on it: 1, 2 and 3 ("Technology around
  us" lessons 1, 2 and 6), 10 ("Grouping data" 1, 3 and 4), 15, 16, 19 and 20 ("Moving a robot" 1 to 3, 4, 5 and 6),
  23 and 25 ("Grouping data" 2 and 5, and 6). All other days are our own. This list is the placement record;
  data/plans/computer-science-kindergarten/source-map.csv waits on the base being loaded (L149).

## Unit 1. Our tools and our rules

Days 1 to 6, weeks 1 to 6. *Who does each tool help, and how do we keep our tools, and ourselves, safe?*

The mystery bag of tools opens the year on day 1: tools matched to jobs and the people they help, and the parts of a
device children touch, pointed to on one screen. Day 2 makes the class's device rules before anyone takes a turn, so
day 3's first turn at a station runs under them (Application: the rules used at a real device). Day 4 is the
public-and-private card sort, a rule for keeping ourselves safe, with no device. The order is the frame's: rules
before the first device turn, which the base text's own order (rules last) would break.

- **End-of-unit assessment, day 5:** a new tool, job and person match, so the "for different users" part is asked
  (EK-SYS-HW-11) and a new public-and-private sort
  (EK-SYS-SE-12) on paper, and one class rule said with its reason (EK-SYS-IM-13) in the spoken groups. Respond day 6.
- **Candidate, settled:** kept, a station rotation plan for a room with three devices on day 3, zero added days.
- **Sensitivity:** days 1 and 3 (tools some people use, never about a classmate; no child is asked what is at home);
  days 4, 5 and 6 (online safety and personal information; health's "If a student tells you something" steps on the
  teacher page). The public-and-private cards come back on days 12, 13, 27 and 28, which carry the same line.

## Unit 2. Step by step

Days 7 to 11, weeks 7 to 11. *How do we tell someone exactly what to do, and who decides the steps?*

The mixed-up handwashing routine hooks day 7, which teaches the step-card and names an algorithm in context. Day 8
modifies a working game set one card at a time (Fluency: it practices day 7's following and ordering). Day 9 is the
think-aloud on how a person makes an algorithm and who made a game, the first teaching of k-people-steps (EK-ALG-IM-03,
EK-SOC-HU-15). Day 10 sorts by one attribute and places a new card (EK-ALG-ML-02), the sorting rule unit 4's graph
reuses. Day 11 is the make: pairs make a game's step-cards and a classmate follows them, opening with a re-sort of day
10's cards as retrieval.

- **End-of-unit assessment:** the mid-year course-level check on day 12 stands for it (frame), scoring all four of
  the unit's ids with unseen items. Day 11, the make session, keeps notes by exception on the class checklist.
  Respond: day 13 serves the unit and the check.
- **Candidate, settled:** kept, the base's "label first, then group" order on day 10, zero added days.
- **Lean:** k-sort-attributes on day 10 (week 10) leans on math kindergarten's mk-sort-count, taught in its unit 2
  (weeks 4 to 9 in data/plans/calendar.csv): met before; the day's note keeps the frame's bridge for a late math year.
- **Sensitivity:** school routines first, home examples only as a child's offer (days 7 to 9); food on picture cards
  only (day 9).

## Unit 3. Robot paths

Days 14 to 22, weeks 14 to 22. *How can we get our robot to the star, and what do we do when it goes the wrong way?*

Day 14 opens with the anchor (the teacher as a robot stops beside the star), then teaches signs and gestures, so the
arrows are signs before they are commands (EK-PRO-VD-05). Day 15 traces a worked path after a forward-and-back
warm-up, then pairs lay and walk the cards for that path and for the same path one square longer (the navigator holds
the cards, the driver moves); no route of a child's own choosing comes before day 19's moved star and day 20's new
star. Day 16 builds the same path in picture blocks. Day 17 traces and predicts (EK-PRO-RD-06), day 18 finds the first wrong step (EK-PRO-TR-07), day 19
modifies a path to a moved star (Fluency), and day 20 makes a path to a new star, runs it and fixes it (Application).
Trace and predict come before fix, fix before modify, modify before make. The heaviest rows (k-sequence-commands on
days 15, 16, 19 and 20, k-wrong-step on 18 to 20) carry the most days; k-symbols, a single unplugged idea, gets one
teaching day and returns in retrieval.

- **End-of-unit assessment, day 21:** on paper, a three-square strip under a new three-card program, a dot drawn
  where the robot is after each card and the end square circled (EK-PRO-RD-06) and the first wrong card in
  a new buggy path (EK-PRO-TR-07); in the spoken groups, each child arranges arrow cards for a new route and says what
  the robot will do (EK-PRO-PD-04) and says what three new signs tell us to do (EK-PRO-VD-05). The route is laid on
  a table mat, so the sitting needs no floor grid. A child's fix is noted, not scored. Respond day 22.
- **Candidate, settled:** kept, the base's forwards-and-backwards step as day 15's warm-up, zero added days.
- **Lean:** k-sequence-commands on days 15 and 16 leans on mk-shapes-positions, taught in math kindergarten unit 3
  (weeks 9 to 13): met before; forward, turn, left and right are this unit's own words, taught with hand signs.
- **Calendar:** weeks 14 to 22 include the kindergarten core check weeks 14 to 17; the unit holds no course-level
  check, as the frame places it.
- **Safety and access:** the floor-grid lines on days 14 to 20 and 22 (walk, no blindfolds, tape flat, a child who cannot
  walk the grid moves the toy or directs, a wristband and a shape, never color alone).

## Unit 4. Ask, count and decide

Days 23 to 26, weeks 23 to 26. *Which game should our class play at indoor recess, and how can we find out?*

Day 23 is the anchor: the teacher poses the recess question, each child places one dot on the floor picture graph,
and the class compares the groups. Day 24 has children pose the next question from a picture prompt, the first time
they pose one (EK-DAT-DI-09). Day 25 makes the real choice from the graph and names other decisions made from counts
(EK-DAT-IM-10); it first teaches k-data-decide, so it is Understanding by the glossary (the frame's Day kinds bullet
now says so). Day 26 is the group investigation on small graph mats (Application).

- **End-of-unit assessment:** the year-end course-level check on day 27 stands for it (frame), scoring DI-09, DC-08
  and IM-10 with unseen items. Day 26, the group investigation, keeps notes by exception on the class checklist, not
  scored, as the frame says. Respond: day 28 serves the unit and the check.
- **Candidate, settled:** kept, the base's "comparing groups" step inside day 23, zero added days.
- **Lean:** both rows lean on mk-sort-count (math kindergarten unit 2, finished by week 9): met before; the bridge
  (the class counts aloud with the teacher, who writes the numbers) is in day 23's note.
- **Sensitivity:** class data about things, never people; prompts from neutral lists, no food, pet, home or body
  question; a child's dot is not named (days 23 to 28).

## Unit 5. Computers around us, then and now

Days 29 to 32, weeks 29 to 32. *Where do people use computers, and how have the computers changed?*

The school office today and long ago hooks day 29: devices in pictures of a home, a school and a workplace, who uses
each and for what (EK-SOC-CE-16). Day 30 orders older and newer devices on a two-card strip and says what looks
different (EK-SOC-HI-14). The unit follows the year-end check because its rows need nothing after them and hand on
only to grade 1.

- **End-of-unit assessment, day 31:** three new small pictures (a home, a school, a workplace), one device circled
  in each, and one use said; order two new
  older-and-newer pairs and say one change. Respond day 32.
- **Candidate, settled:** dropped, a visit by a school worker who uses a device: the pictures carry both rows and a
  visit needs the school's own arrangement, zero days.
- **Sensitivity:** no child is asked about a family member's job or the devices at home; older devices shown with
  respect (days 29 to 31).
- **Swap or leave out:** a school may leave unit 5 out (frame); EK-SOC-CE-16 and EK-SOC-HI-14 are then not claimed.

## Course-level checks

| Check | Day | Week | Respond | What it checks |
|---|---|---|---|---|
| Mid-year, standing for unit 2's end-of-unit assessment | 12 | 12 | 13 (week 13) | Unit 2 in full with unseen items: EK-ALG-PS-01 (a new picture algorithm followed, then a new routine ordered and named) and EK-ALG-ML-02 on paper; EK-ALG-IM-03 (three picture prompts) and EK-SOC-HU-15 as two spoken look-fors. Unit 1 sampled: EK-SYS-SE-12 (a new card), EK-SYS-IM-13 (a rule scene judged) |
| Year-end, standing for unit 4's end-of-unit assessment | 27 | 27 | 28 (week 28) | Unit 4 in full with unseen items: EK-DAT-DC-08 and EK-DAT-IM-10 on paper, EK-DAT-DI-09 spoken (each child poses a question) with its collect part in the paper placing. Units 1 to 3 sampled on paper: EK-PRO-RD-06 (the dot strip), EK-PRO-TR-07, EK-PRO-PD-04 (glue three arrow cards to reach the star), EK-PRO-VD-05 (circle what a sign tells us to do), EK-SYS-SE-12 |

Each check is the end of the unit right before it, not a check after that unit's own assessment, so its items for that
unit are its own unseen items; its samples of earlier units use new cards and no task form given in the two weeks
before. Both weeks avoid the kindergarten core check weeks (14 to 17, 29 to 32). Health K to 2's kindergarten checks
also sit in weeks 12 and 27; computer science is a special and does not count against the classroom teacher's
stagger (CALENDAR.md rule 1), so this is no break.

**Codes no course-level check samples (rule 3), and why.** EK-SYS-HW-11 is scored on day 5 and carried unscored on
day 12; the mid-year paper task holds no more items. EK-SOC-CE-16 and
EK-SOC-HI-14 are taught in unit 5, after the year-end check, and are scored on day 31.

## Shorter path

**A shorter period** (20 to 25 minutes). The retrieval opener drops to 2 minutes and floor-grid and device days keep
their 4 put-away minutes, leaving about 14 to 19 teaching minutes. Teaching days keep their first task and shorten
the second (day 1's device pointing becomes the teacher at one screen; day 15's partner moves run with half the class
on the grid while the other half lays the cards; day 23's comparing runs on the floor graph only). Check days keep the
15-minute paper task; spoken answers from groups not reached are heard in the first 10 minutes of the respond day,
as at every length, so the evidence is collected once.

**A year about 10 days short, by named fold-in days.** Ten school days are two weeks, so two sessions fold. Neither is
assessed, and every id they carry is taught on another day.

| Fold-in day | Folds into | How | Saves |
|---|---|---|---|
| 8 (modify a game's step-cards) | 11 | The class changes one card of a working game set as the first 7 minutes, then pairs make their own | 30 minutes |
| 19 (modify a path to a moved star) | 20 | The star moves one square and the class changes one card as the first 7 minutes, then pairs plan to a new star | 30 minutes |

Total: 60 minutes, 2 sessions, so the year runs 30 of the frame's 32 days. A spare, folded only if the year runs
shorter still: day 16 (the picture-block path) into day 17, with the traced program given as picture-block cards that
the teacher lays beside the arrow cards (30 minutes). Never folded: any check day, a respond day after a course-level
check, the only teaching day of any id, and day 3 (the only first device turn). The shorter-year rule, the same from kindergarten to grade 5: a respond day after an end-of-unit sitting may fold into the next day's opener with a self-check; a respond day after a course-level check never folds; check days keep their weeks, and a lost week before a check moves the teaching days, never the check.

## For the lead

None. The four items of the first draft were settled in the fix pass (docs/reviews/sequence-computer-science-kindergarten-fixes-2026-11-26.md).
