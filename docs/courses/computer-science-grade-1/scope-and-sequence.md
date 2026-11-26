# Scope and sequence: Computer Science, Grade 1

Course `computer-science-grade-1`, grade 1, draft 2026-11-26, fixed 2026-11-26 from the expert read (docs/reviews/sequence-computer-science-grade-1-fixes-2026-11-26.md), from the frame (docs/courses/computer-science-grade-1/frame.md); the days live in data/plans/computer-science-grade-1/days.csv.

## The year on the calendar

- **32 course days**, one 30-minute session a week for 32 weeks (a specials rotation), so course day n sits in week
  n. `school_day` = 5n (the last school day of week n), so week = (school_day - 1) // 5 + 1 = n for every day. Units
  1 to 5 hold 6, 6, 8, 4 and 4 days (28); the two course-level checks and their respond days are days 13, 14, 27 and
  28. Units 1 to 5 teach on 4, 6, 6, 4 and 2 sessions, as the frame sets.
- **A session.** From day 2 on, a teaching or respond session opens with a three-minute retrieval task (the
  `retrieves` column names its rows); floor-grid and device sessions keep four minutes at the end to put cards, tape
  and devices away, so a session teaches for about 23 minutes. A check sitting (days 5, 13, 21, 27, 31) has no
  retrieval opening: a retrieval opening is practice, and its three minutes settle the room and give the
  instructions. Every check is a whole-class paper task collected from every child, while the teacher hears one
  spoken answer a child in five groups of six. Early readers need cards read aloud, and a teacher who reads to the
  class cannot hear groups at the same time, so each course-level check runs on a minute plan: minutes 0 to 3 settle
  and instructions, minutes 3 to 8 the read-aloud items done together (each card read twice), minutes 8 to 26 the
  picture-only items done alone while the five groups are heard, the last four minutes to collect work and put
  objects away (days 13 and 27 name their items).
- **Device and paper paths.** Every day runs on paper, cards, tape and objects. The device days are day 3 (any
  school device, its home screen only) and days 16, 17, 19 and 20 (the picture-block tool with its "when tapped"
  event block). That K to 2 picture-block mode is queued with tool work (later.csv L148) and does not exist yet, so
  days 16 to 20 run on the block-card paper path on the floor grid until it does; each such day says so in its note.
  The paper path meets every grade 1 id in full (frame, Devices), so no id is part met for lack of the tool.
- **Kinds.** Understanding is an unplugged or trace session; Fluency is a modify session (days 9 and 19 only);
  Application is a make session (days 10, 20 and 24). Inside each unit: trace before modify before make.
- **Retrieval and readiness (rule 2).** Every earlier-grade row this course assumes is a kindergarten row, used the
  year before, so each opens as a retrieval task inside a day and no unit has a readiness check. The math lean is
  taught earlier the same year, so it is retrieval too.

| Earlier row | Last used | Treatment | Day |
|---|---|---|---|
| k-device-manners | Kindergarten | Retrieval | 1 (after the hook), 3 (before the first device turn) |
| k-tools-jobs | Kindergarten | Retrieval | 2, 6 |
| k-public-private | Kindergarten | Retrieval | 4 |
| k-follow-steps | Kindergarten | Retrieval | 7 |
| k-people-steps | Kindergarten | Retrieval | 8, 12 |
| k-sort-attributes | Kindergarten | Retrieval | 11 |
| k-symbols | Kindergarten | Retrieval | 15 |
| k-sequence-commands | Kindergarten | Retrieval | 16 |
| k-describe-sequence | Kindergarten | Retrieval | 17 |
| k-wrong-step | Kindergarten | Retrieval | 18 |
| k-ask-and-count | Kindergarten | Retrieval | 23 |
| k-data-decide | Kindergarten | Retrieval | 25 |
| k-devices-places | Kindergarten | Retrieval | 29 |
| k-then-now | Kindergarten | Retrieval | 30 |
| m1-data-three-categories (math grade 1) | Math grade 1 unit 1, weeks 1 to 4 | Retrieval (math leans open with retrieval) | 23 |

  Earlier units of this course come back as spaced retrieval too (days 9, 10, 14, 16, 19, 20, 22, 24, 26, 28, 32), chosen to space the rows the next course-level check samples.

## Unit 1. Using our tools well

Days 1 to 6, weeks 1 to 6. Concept area: systems and security. Practices: ESR1 and IC3 (why a rule helps everyone),
IC3 (each part named and its job explained), ESR2 and IC5 (a password kept private, signing out for the next pair),
HCD10 (parts that help different users). Owns g1-responsible-use, g1-hardware-parts and g1-keep-safe (E1-SYS-IM-13,
E1-SYS-HW-11, E1-SYS-SE-12).

**Arc.** The class device that "won't work" opens the year; the kindergarten rules come back and the class works out
why each rule exists, its own part in keeping it and what breaking it costs self and class (day 1). The parts get
their right words and jobs on picture cards, with adapted parts beside the usual ones (day 2), then on a real device
in the year's first device turn, which ends with the teacher signing out (day 3). Day 4 makes a password a private
key on a paper pretend login. **Why this order:** the rules come before the first device turn, the parts' names
before the device match, and the sign-out seen on day 3 is the concrete moment day 4 names.

**Assessments.** No readiness check (all assumed rows are kindergarten's). Observation on days 3 and 4: half the
class each day says why the rule on a new rule scene matters and what happens if it is broken (E1-SYS-IM-13), heard
during partner work after day 1 taught it, so day 5 holds only two spoken prompts. End-of-unit, day 5: a new
part-and-job match, a new rule scene with its consequence circled, a new pretend login with the secret and the
sign-out circled; spoken, one part and its job (E1-SYS-HW-11) and what to do if someone asks for the password
(E1-SYS-SE-12). Response time: respond day 6.

**Candidate settled.** Kept: a station rotation plan for a room with three devices, on day 3, zero added days.

## Unit 2. Plans in parts

Days 7 to 12, weeks 7 to 12. Concept area: algorithms and design, with computing and society (people and computers
compared). Practices: CT6, CT7, CT8, ESR1 and IC3, HCD10. Owns g1-split-task, g1-change-steps, g1-patterns-ai and
g1-people-or-machine (E1-ALG-PS-01, E1-ALG-IM-03, E1-ALG-ML-02, E1-SOC-HU-15).

**Arc.** The tower built from one long spoken instruction falls; the class cuts a job into parts and each part into
step-cards (day 7). Two orders of the same steps give two towers (day 8); a working plan is changed one step at a
time and checked (day 9, modify); pairs then split a new class job and a partner pair carries it out (day 10, make),
and the class keeps two plans for unit 3. The guessing game shows what a pattern-finding system does (day 11), and
the people-or-computer sort sets that beside what people do well (day 12). Day 11 plants one wrong guess from too
few examples ("a pattern-finder can guess wrong too, so people check it") and names these systems AI once; day 12's
computer card says a computer repeats a step "the same way every time without getting tired", never "without
mistakes", in the year that teaches bugs. **Why this order:** the split comes first
because every later plan builds on it; the change needs a plan to change; modify comes before make; patterns and
people-or-computer close the unit together, as the frame sets.

**Assessments.** No readiness check. Observation on days 11 and 12: fifteen children a day say why two new orders of
the same steps give different results (E1-ALG-IM-03), after days 8 and 9 taught it, recorded with day 13. The
mid-year course-level check (day 13) is the unit's end-of-unit assessment, so no separate end day sits inside the
unit; day 14 is the response time. Its E1-ALG-ML-02 item asks both parts of the code: from four pictured machines
(a light switch, a calculator, a next-book screen, a picture-making tool), circle the two that find patterns in many
examples (one decides, one makes something new), then draw a new card into the group a pattern-finder would guess.

**Candidate settled.** Kept: the partial base's "same but different" pairing of two algorithms for one goal, on
day 8, zero added days.

## Unit 3. Code that waits for a tap

Days 15 to 22, weeks 15 to 22 (across the grade 1 core check weeks 15, 16 and 19; this course holds no check there).
Concept area: programming. Practices: IC3 and CT7, CT7 and CT8, IC3 and CT6, CT6 and CT9, IC5 (driver and navigator
switching at the halfway signal). Owns g1-changing-things, g1-code-sequence, g1-explain-events and g1-fix-sequence
(E1-PRO-VD-05, E1-PRO-PD-04, E1-PRO-RD-06, E1-PRO-TR-07).

**Arc.** Things that change and things that stay the same are sorted first, so the character's moving square is a
changing value before any code runs (day 15). The rug-path plan from unit 2 becomes picture blocks under a "when
tapped" start block, traced and run as the worked example before pairs build it (day 16). A given event program is
read and predicted before it runs (day 17). A buggy program is traced on the floor grid: predict, run, find, fix
(day 18; the bug is a forward block before a turn, so the character ends on the wrong square, using only taught
blocks). The goal square moves and one block changes (day 19, modify). Pairs turn a given plan into their own block
program, run it, fix it and say what they tested (day 20, make). **Why this order:** the APPROACH order, trace and
predict before fix, fix before modify, modify before make; the code is translated from unit 2's plans, so the
step-card comes first.

**Assessments.** No readiness check. End-of-unit, day 21: lay out block cards for a new given plan (E1-PRO-PD-04,
the laid-out program is the product), circle and move the first wrong block (E1-PRO-TR-07), a new changes-or-stays
sort of worded picture cards (temperature, score, height, time, name, birthday), each word read aloud, with the word
on one changing card circled (E1-PRO-VD-05, which asks for terms); spoken, what a new event program does when tapped, block by block
(E1-PRO-RD-06). Response time: respond day 22.

**Candidate settled.** Kept: the partial base's "changing a design" step as day 19's modify task, zero added days.

## Unit 4. Counting, looking and asking

Days 23 to 26, weeks 23 to 26. Concept area: data and analysis. Practices: IC3 and CT7, CT6 and IC3, ESR1 and HCD10.
Owns g1-two-kinds-data and g1-data-questions (E1-DAT-DC-08, E1-DAT-DI-09, E1-DAT-IM-10).

**Arc.** The argument over whether the class plant has grown opens the unit; data is collected by counting,
measuring, watching and asking (day 23); groups answer the plant question with the mix (day 24, make). Then the
questions themselves (day 25): questions we answer by collecting data, counting, measuring, looking or asking everyone
(which window do most of us like best), and questions answered another way, by one person's own idea or feeling
(which window do I like best), imagination or asking someone who knows. A class survey of feelings is data, as in
kindergarten and day 23; one person's feeling is not. Then questions people in the school and
town ask to meet a need, who each helps and how one word changes it (day 26). **Why this order:** collecting first
gives children the experience the question sort needs; the community questions build on the sort.

**Leans.** m1-data-three-categories is taught in math grade 1 unit 1 (weeks 1 to 4), well before week 23, so day
23 retrieves it. Measuring in cubes meets math grade 1 unit 6 (length, weeks 23 to 26) in the same weeks, so days
23 and 24 carry the frame's bridge: cubes laid end to end and counted together with the teacher.

**Assessments.** No readiness check. On day 24 the teacher notes by exception which groups chose a way to collect
each piece; it shapes the day 28 groups. The year-end course-level check (day 27) is the unit's end-of-unit
assessment; day 28 is the response time.

**Candidate settled.** Kept: the partial base's "what is an attribute?" step inside day 23's description data, zero
added days.

## Unit 5. Computers in our town, then and now

Days 29 to 32, weeks 29 to 32. Concept area: computing and society. Practices: ESR1, IC3. Owns g1-computing-around
and g1-then-and-now (E1-SOC-CE-16, E1-SOC-HI-14).

**Arc.** A picture walk down a town street; who uses a device at home, school and in town, and for what (day 29).
One everyday activity at a time on the two-card timeline, before and after a technology, with what got easier and
what may be harder (day 30). **Why this order:** where devices are used comes before how one activity changed; the
unit gathers the year and needs nothing after it, so it follows the year-end check.

**Assessments.** No readiness check. End-of-unit, day 31: a new three-scene strip (a home, a school room, a town place),
a line drawn on paper from each scene to the device used there, and spoken, who uses one of them and for what
(E1-SOC-CE-16, each of its three settings asked); a new activity's before and after cards ordered with one difference circled or
drawn (E1-SOC-HI-14). Response time: respond day 32, which also records each child's support and gains for grade 2.

**Candidate settled.** Dropped: a visit by a school worker who uses a device; the pictures carry both rows and a
visit needs a school's own arrangement, zero days.

## Course-level checks

| Check | Course day | Week | Respond | Codes sampled |
|---|---|---|---|---|
| Mid-year, unit 2's end-of-unit assessment | 13 | 13 | Day 14, week 14 | E1-ALG-PS-01, E1-ALG-ML-02, E1-SOC-HU-15, E1-ALG-IM-03 (the day 11 and 12 record), E1-SYS-SE-12, E1-SYS-IM-13 |
| Year-end, unit 4's end-of-unit assessment | 27 | 27 | Day 28, week 28 | E1-DAT-DC-08, E1-DAT-DI-09, E1-DAT-IM-10, E1-PRO-RD-06, E1-PRO-TR-07, E1-SYS-SE-12 |

Each check is the end-of-unit assessment of the unit just before it (frame, Days), so it repeats no assessment just
given; its items for earlier units are new forms, not day 5's or day 21's. **Owned codes on no course-level check
day**, and why: E1-SYS-HW-11 (unit 1's day 5 record is carried unscored on day 13), E1-PRO-PD-04 and E1-PRO-VD-05
(unit 3's day 21 record, with the program each child laid out, is carried unscored on day 27), E1-SOC-CE-16 and
E1-SOC-HI-14 (unit 5 follows the year-end check, as the frame places it, and is checked on day 31). All five follow
the frame's Course-level checks table.

**Calendar.** The grade 1 core check weeks are 14, 15, 16 and 19 (mid-year) and 29 to 32 (year-end); this course's
checks are in weeks 13 and 27, its respond days in 14 and 28. Computer science in K to 5 is a special and does not
count against the classroom teacher's stagger (CALENDAR.md rule 1), so the course breaks no stagger rule. Week 13 is
also library grade 1's and week 27 health's, media arts' and theater's; the lead's calendar pass holds those (frame,
For the lead 1).

## Sources not yet loaded

The partial base, the archived Teach Computing Curriculum Year 2 (2023), is not in the source store (later.csv L149),
so its placement is provisional. Days that lean on it: 1 and 2 ("IT around us" lessons 5 and 1), 7 to 10 ("Robot
algorithms" lessons 1, 6, 2, 3 and 5), 16, 17, 19 and 20 ("Programming quizzes" lessons 1, 2, 4, 3 and 6), 18
("Robot algorithms" lesson 4), 23 and 24 ("Pictograms" lessons 1, 4, 3 and 6) and 29 ("IT around us" lessons 2, 3
and 4). Days 11, 12, 15, 25, 26 and 30 are our own. Check and respond days are ours. Day 30's teacher source line
(the history museum timeline the frame names) and day 11's dated sources for real pattern-finding uses are opened by
the unit writer. The base lessons left out stay as the frame's Source map gives them.

## Shorter path

**A shorter period** (25 minutes, not 30): the three-minute retrieval opening and the four put-away minutes stay, so
teaching drops from about 23 to about 18 minutes. Teaching days keep the worked example and the trace and drop the
second practice round; device days keep one device turn per pair with the switch at the halfway signal; check days
keep the 15-minute paper task with the spoken groups heard during it. Nothing assessed and no owned part is cut.

**A year about 10 school days short** is two weeks, so two sessions. Fold-in days, nothing assessed on them and no
owned part cut:

| Fold-in day | Folds into | Minutes saved |
|---|---|---|
| Day 9 (unit 2 modify: one step swapped, dropped or added) | Day 10 keeps its three-minute opening as a new pretend login card with a rule scene (g1-keep-safe and g1-responsible-use, both sampled on day 13); the five-minute one-step change to day 7's plan comes out of the make's minutes | 30 |
| Day 19 (unit 3 modify: the goal square moves) | Day 20: after each pair's first run the goal square moves and they change one block (the kept Candidate moves with it) | 30 |

Total: 60 minutes, two sessions, so the year runs 30 of the frame's 32 days. Every other day either first teaches an
owned row or holds an assessment, so a year short by more than two weeks would need the lead's call on what to drop.

## For the lead

1. **No source-map.csv.** Waits on L149: the base is not loaded, so the base lessons' landing days stay under Sources
   not yet loaded and the frame's Source map until the store folder is made.
2. **Unit 1's spoken load (item-level, decided here).** The frame's day 5 lists three spoken prompts (HW-11, IM-13,
   SE-12), more than a 30-minute sitting holds for 30 children. E1-SYS-IM-13's spoken why is heard on days 3 and 4
   (half the class each, after day 1 taught it); day 5 keeps two short spoken prompts.
3. **Device share until L148.** The frame states 5 device sessions of 32 (about 40 minutes a child). Until the
   picture-block mode exists, days 16, 17, 19 and 20 run on the paper path, so the year's real device time is day 3
   alone (about 10 minutes a pair). The frame's For the lead 6 proposed APPROACH line covers the share once the mode
   lands.
4. **Retrieval on check sittings.** This plan gives check sittings no retrieval opening (a check sitting is itself
   retrieval, and the minutes go to settling in). The expert read's APPROACH.md wording, which makes this plain, is in
   the fix report's For the structure pass.
5. **Day 13's load.** If the probe shows day 13 still over 30 minutes after the minute plan, the unit 1 rule-scene
   sample is the item to drop (E1-SYS-IM-13 was scored on days 3 to 5 and is not sampled at year-end); that is a frame
   change.

## Unsure

- Day 3's kind: the first device turn applies day 2's part names to a real device, but it also first shows the
  sign-out and the first device handling, so it is typed Understanding (first teaching wins).
