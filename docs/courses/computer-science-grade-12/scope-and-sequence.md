# Scope and sequence: Computer Science, Grade 12

Course `computer-science-grade-12`, grade 12, draft scope and sequence, 2026-11-26 (fix pass the same day), written from
docs/courses/computer-science-grade-12/frame.md. The days live in data/plans/computer-science-grade-12/days.csv; this
page holds the reasons.

## The year on the calendar

- **64 course days**, two 45-minute lessons a week over 32 weeks: units 1 to 5 run 11, 11, 21, 7 and 8 days, with 4
  course-level check days and 2 respond days after them, as the frame sets. 52 teaching days (64 minus 3 end-of-unit
  sittings or products on Check days, 4 course-level check days and 5 respond days).
- **school_day formula:** course day 2k-1 sits on school day 5k-3 and course day 2k on school day 5k-1 (the second
  and fourth day of week k), so course days 2k-1 and 2k fall in week k; week = (school_day - 1) // 5 + 1.
- **Each lesson:** a five-minute retrieval trace or predict task opens every lesson from day 2 on (APPROACH.md, "How a
  day opens"); device lessons keep their last three minutes to save work to a file and shut down; paper work is
  collected in the last two minutes. About 35 to 37 teaching minutes a lesson.
- **Day kinds** follow docs/GLOSSARY.md: a standard's first day in the course is Understanding, so day 29 (first day
  of S1-SWD-PP-08), day 50 (first user round, HS-PRO-TR-20) and day 60 (first day of HS-SOC-CE-46) are Understanding,
  each with its worked example first.
- **Grade 12 calendar:** units 1 to 4 and both course-level checks end by week 28, so a senior who leaves early has sat
  them; unit 5 runs in weeks 29 to 32 and has the frame's 4-day short form (frame, "Grade 12 calendar").
- **Sources not yet loaded (later.csv L149):** none of this course's days leans on one. The archived Teach Computing
  Curriculum is the partial base for K to 8 only, and the NOAA extract is grade 11's. High school is our own, with no
  base text and so no source map.
- **Devices:** device days are 4, 32 to 43, 48 and 50 to 53 (18 lessons, as the frame counts); every unit keeps unplugged days and unit 2
  and unit 5 are wholly unplugged. Each device day's note gives the four ways (pair, stations, one screen, no device),
  the save-and-shut-down minutes and the safety lines. The three queued editor modes (later.csv L148) are not used in
  grade 12; the editor's offline version history is not built yet, so day 31 runs on paper branch cards.

## Readiness and retrieval

Grade 12 is an elective that never assumes grade 11 was taken (frame, "Course order"). Every row it owns assumes a
grade 11 row, last used the year before, so a student who took grade 11 meets it as a retrieval opening (the
`retrieves` column); a student who did not takes the same items as a ten-minute readiness check before the unit opens,
and the unit's first understanding day carries a worked example of the grade 11 idea inside its own minutes.

| Unit | Earlier-grade row | Last used | Treatment and day |
|---|---|---|---|
| 1 | g11-evaluate-generated-code | grade 11 | Retrieval days 2, 3, 6; readiness (no grade 11) day 1, last ten minutes |
| 1 | g11-build-ml-model | grade 11 | Retrieval days 4, 5; readiness day 1 |
| 1 | g11-emerging-solution | grade 11 | Retrieval days 7, 9; readiness day 1 |
| 2 | g11-algorithm-ethics | grade 11 | Retrieval day 13; readiness day 11 |
| 2 | g11-infrastructure-impact | grade 11 | Retrieval days 15, 16; readiness day 11 |
| 2 | g11-policy-change | grade 11 | Retrieval day 18; readiness day 11 |
| 2 | g11-data-scale-ethics | grade 11 | Retrieval days 18, 19, 21; readiness day 11 |
| 3 | g11-evaluate-vs-spec | grade 11 | Retrieval days 26, 27 and through the build; readiness day 25 |
| 3 | g11-multivariate-viz | grade 11 | Retrieval day 29; readiness day 25 |
| 3 | g9-modular, g9-design-with-structures, g9-det-vs-prob | grade 9 | Readiness for every student on day 22 (last ten minutes of unit 2's last day); acted on by gap on day 28; retrieved on days 32, 34, 37, 41, 44 |
| 4 | g11-evaluate-generated-code, g11-evaluate-vs-spec | grade 11 (and unit 3 here) | Retrieval days 47, 49, 51; readiness day 46 |
| 5 | g11-career-plan | grade 11 | Retrieval days 58, 59, 61; readiness day 56 |

The grade 9 readiness check sits on day 22, four course days before unit 3 opens (the frame's placement, so day 25
holds only the grade 11 items, review M7); days.csv marks day 25 as unit 3's readiness day and day 22's note carries the
grade 9 items. The children's online privacy law of grade 10 returns only as a one-minute card on day 16, not as a
claimed row.

## Unit 1. Judging what a machine says

Course days 1 to 11, weeks 1 to 6. Arc: from two saved answers to one history question (the anchor), students learn how
a generated-text system makes an answer and judge saved text, code and images for accuracy, bias and harm (days 2 and
3), count a model's errors by group and trace each limit to its source (days 4 and 5), and then apply a class checklist
to a new mixed set (day 6, the modify day). Days 7 to 9 turn to how human and artificial intelligence differ and who is
responsible, argued from the cases just judged, as the row asks. Order: output judging comes before the debate so the
debate argues from evidence students hold; the quantitative count (day 4) comes before the qualitative sources (day 5)
because the sources explain the gaps the count shows.

- Readiness: day 1, last ten minutes after the hook (grade 11 items, for students without grade 11).
- End-of-unit: day 10, a 40-minute sitting (about 35 task minutes) with unseen items on all three ids, a prompt per
  part: accuracy, bias and harm for HS-ALG-PS-05 (about 12 minutes); counted errors and their sources for S1-AIN-HR-09
  (about 10); for HS-SOC-HU-44, one difference between human and artificial intelligence the case turns on, what it
  means for a claim about consciousness, and who is responsible on what ethical ground (about 13); response on day 11.
- Practices: CT9 (days 2, 6), ESR1 (day 3), HCD12 (day 5), CT6 and IC3 (day 8). Concept areas: algorithms and design
  (machine learning), computing and society.
- Candidate: kept, a second responsibility case from a court record on day 8 (the case picked in the unit plan) for a
  class that finishes early, zero added days.
- Sensitivity: bias content (days 3 to 5) and beliefs about mind and consciousness (days 7 to 9), flagged in the notes.

## Unit 2. Who sets the rules?

Course days 12 to 22, weeks 6 to 11. Arc: from the invented bus-route program, students trace the values built into a
system (days 12 to 14), then read a law that governs systems and compare technical, legal and social approaches (days
15 to 17), then judge a data policy's efficacy with evidence in a structured debate and a written judgment (days 18 to
21). Day 22 returns written feedback on the three pieces and students revise them. Order: a design's values first, then
the law that governs designs, then a data policy whose effects are measured, so each step widens the last.

- Readiness: day 11, last ten minutes of unit 1's respond day (grade 11 items).
- End-of-unit: course-level check 1 (days 23 and 24) stands for unit 2's end-of-unit assessment; day 22's revised
  pieces are practice, not scored. Day 22's last ten minutes hold the grade 9 readiness check for unit 3.
- Lean e12-informative (day 14, week 7) comes before ELA's unit 6 (weeks 18 to 21): the bridge runs inside the day.
  The e12-seminar leans (days 8 and 20) meet ELA unit 1 (weeks 1 to 3), taught earlier.
- Practices: ESR1 (days 13, 21), IC3 (days 14, 17, 20), CT6 and ESR2 (day 16), HCD12 (day 19), HCD10 (day 21).
  Concept areas: algorithms and design, systems and security, data and analysis (all impacts).
- Candidate: kept, the Section 1201 rulemaking card on day 16 for groups that choose copying, zero added days.
- Sensitivity: disability access (day 15) and tribal data (days 18 to 21), flagged, with health's disclosure steps on
  the data policy days.

## Course-level check 1 (week 12)

Days 23 and 24, week 12; respond day 25, week 13. Day 23 scores unit 2 in full on new systems, laws and policies
(never the unit's own cases), since the check stands for unit 2's end-of-unit assessment. Day 24 samples unit 1 with
short new items, a prompt per part: a saved output judged for accuracy, bias and harm (HS-ALG-PS-05), and a new
responsibility case answered with the difference prompt and one of the two implication prompts, rotated
(HS-SOC-HU-44); unit 1's day 10 sitting was in week 5, so no task form repeats within two weeks. Day 25 reteaches by
error letter and holds unit 3's grade 11 readiness check in its last ten minutes.

## Unit 3. Build it as a team

Course days 26 to 46, weeks 13 to 23. Arc: the anchor (two halves that do not fit) opens the need for a workflow; a
finished team project is read whole (day 27), the design method is worked on it (day 28, with the grade 9 readiness
results acted on), and each team writes its design document (day 29). The review step (day 30) and version history on
paper (day 31) are taught before the build needs them. Day 32 is the modify day on a starter module; days 33 to 39
build in pairs with review steps on days 36 and 39; day 40 joins the modules; days 41 to 43 are draft, written feedback
and revision; day 44 is the presentation. Order: read, then modify, then make (trace before build on every construct).

- Readiness: day 25 (grade 11 items) and day 22 (grade 9 items, every student).
- End-of-unit: the team program scored after day 43, each member's part read from the log, with day 44's trace of each
  member's module; day 45, an individual 40-minute paper sitting (about 35 task minutes) with unseen items
  (HS-PRO-PD-15, S1-SWD-PP-08); response on day 46. 21 days, so no mid-unit assessment.
- Build-day openings (days 33 to 39) each name the row they retrieve (the `retrieves` column). The no-device path is
  written once on day 32 (the module on the printed template, traced by hand against the test-table; the HS-PRO-PD-12
  revisit marked "part met without a device") and referenced by days 33 to 43. Every paired device day carries the
  driver and navigator switch.
- Practices: IC4 (days 27, 33 to 39), IC5 (days 30, 33 to 39), CT6 (day 29), CT7 and CT8 (day 28), CT9 (build days).
  Concept area: programming.
- Candidate: kept, a fifth menu project chosen by a team with the teacher's yes if it holds no personal data, zero
  added days.
- S1-SWD-PP-08's version control part is part met for every class until the editor's offline version history exists.

## Unit 4. Credit it and test it with users

Course days 47 to 53, weeks 24 to 27. Arc: attribution on a supplied program, then on the team's own (days 47 and 48);
the intended users stated and a heuristic review run (day 49) before the team listens to users; two user rounds with
one change at a time between them (days 50 to 52); the refinement record and hand-in (day 53). Order: credits first so
users try the credited program; the heuristic review before user rounds so the team knows its users first.

- Readiness: day 46, last ten minutes of unit 3's respond day.
- End-of-unit: the refinement product handed in on day 53 and scored (each student's contribution to one implemented
  refinement, HS-PRO-TR-20, with one rubric line for S1-SWD-UX-05: the refinement judged against the intended users and
  setting the team stated on day 49), with the year-end check (days 54 and 55) for transfer; response on day 56.
- User rounds (days 50 and 52) name their roles: two users, one note-taker, one at the device, switched in round two.
- Practices: ESR2 (day 47), HCD10 (day 49), HCD11 and CT9 (day 51), HCD12 (day 52), IC3 (user rounds). Concept area:
  programming.
- Candidate: kept, an extra user round for a team whose second round still shows a blocking fault, folded into day 53,
  zero added days.

## Course-level check 2, year-end (weeks 27 and 28)

Days 54 (week 27) and 55 (week 28); respond day 56 (week 28), off the finals week. Day 54 scores unit 4 in full on new
material drawn from earlier units, as a check right after a unit's end should: its short program is a module from unit
3's supplied worked team project (day 27) and its printed screen is unit 2's invented bus-route helper. Day 55 samples
units 1 to 3 with short new items (the saved output judged for accuracy, bias and harm, a prompt for each), then
unscored mixed retrieval. Unit 3's scored program and
sitting are carried unscored. Item-level choice of this scope: day 55's workflow item includes one inclusive-norm fault,
so S1-SWD-PP-08's review part is sampled inside the same ten minutes. Day 56's last ten minutes hold unit 5's readiness
check.

## Unit 5. What our team taught us, and where I go next

Course days 57 to 64, weeks 29 to 32. Arc: the team's own log studied for moments where a different view changed a
decision (days 57 and 58), two published accounts read and analyzed (day 59), then the portfolio and field cards (day
60), the plan (day 61), written feedback and revision (day 62), the scored hand-in (day 63) and close (day 64). Order:
CE-45 first because its log comes from unit 3; CE-46 last because its portfolio is the whole year.

- Readiness: day 56.
- End-of-unit: day 63, the revised analysis and plan scored (the plan read privately) with a short unseen log item;
  response on day 64. HS-SOC-CE-45 gets a prompt per part: (a) a team and how its different views changed what it
  built, (b) how the team or person used computational thinking and a computing technology to solve a problem, (c) one
  idea the work expressed or let others express, then (d) the barrier and the opening of the field the row adds. Day
  59's reading guide asks the same four, so the item is taught before it is scored.
- Accounts: Grace Hopper's 1968 Smithsonian oral history (browser check) and Katherine Johnson in her own words in NASA
  Langley's feature "She Was a Computer When Computers Wore Skirts" (picked by this scope from search, 2026-11-26;
  checked at source in the unit plan). Each is read for the team the person worked in (Hopper's Harvard computing crew;
  Johnson's West Area Computing group and the flight-trajectory team), and the team's own unit 3 log stands beside them
  as the current case. If the Johnson feature turns out to be a profile with quotations, the unit plan swaps in a
  NASA-published interview in her own words (grades 6 to 12 frame read M1 allowed it).
- Practices: IC5 and HCD10 (day 58), CT6 (day 60), IC3 (day 62), ESR1 (day 59). Concept area: computing and society.
- Candidate: dropped, a visit by a computing professional (the standard asks for published accounts, and a visit needs a
  school's own arrangement), zero days.
- Short form if seniors leave before week 31: the frame's four days in weeks 29 and 30.
- Sensitivity: race and gender barriers in the accounts; a plan that can touch family money or status; health's
  disclosure steps on the teacher page.

## Standards and their days

| Id | Taught (course days) | Assessed |
|---|---|---|
| HS-ALG-PS-05 | 1, 2, 3, 4 (half), 6 | 10; 24; 55 |
| S1-AIN-HR-09 | 4 (half), 5 | 10; 24 |
| HS-SOC-HU-44 | 7, 8, 9 | 10; 24 |
| HS-ALG-IM-11 | 12, 13, 14, 22 | 23 |
| HS-SYS-IM-36 | 15, 16, 17, 22 | 23 |
| HS-DAT-IM-28 | 18 to 22 | 23; 55 |
| S1-DSC-PP-13 | 18 (half), 21 (half) | 23 |
| HS-PRO-PD-15 | 26 to 44 | program scored after 43; 45; 55 |
| S1-SWD-PP-08 | 29 (part), 30 (part), 31 | 45; 55 (version control part met) |
| HS-PRO-PD-14 | 47, 48 | 54 |
| HS-PRO-TR-20 | 50 to 53 | product 53; 54 |
| S1-SWD-UX-05 | 49 (and the user lens of 50 to 53) | product 53; 54 |
| HS-SOC-CE-45 | 57, 58, 59, 62 | 63 |
| HS-SOC-CE-46 | 60, 61, 62 | 63 |

Every owned code is sampled on a course-level check day except HS-SOC-CE-45 and HS-SOC-CE-46: unit 5 follows the
year-end check by the frame's senior calendar (the check sits in week 28 so early leavers have sat it), and both are
scored on their own end-of-unit product on day 63.

**Days outside the standards (bar C1).** S1 minutes by day: day 4 half, day 5 whole, day 18 half, day 21 half, day 29
about 5 minutes, day 30 about 5 minutes, day 31 whole, day 49 whole: about 4.77 day-equivalents (5 of 37 teaching minutes
each on days 29 and 30) of 52 teaching days, about 9.2 percent, under 10 percent. The frame counted 4.5; the two
five-minute parts on days 29 and 30 (the "whose needs and views" line and the review's "more than the team's own view"
question) are counted here, and the frame's C1 paragraph now says so. Day 53's S1-SWD-UX-05 rubric line adds scoring,
not teaching time. The Shorter path holds the same bar (below).
The capstone's revisit of grade 9's HS-PRO-PD-12 and HS-ALG-PS-01 sits inside the standards.

## Shorter path

**A shorter period (40 minutes).** The opening drops to three minutes, device days keep three minutes to save and paper
two to collect, leaving about 32 teaching minutes. Debates run in groups of four instead of whole class; build days
keep their pair switch and lose about five minutes of code time each; the sittings are already written as 40-minute
sittings with about 35 task minutes, so they hold.

**A year about 10 days short.** Ten fold-in days, none assessed and no owned part cut; each saves one 45-minute lesson
(about 37 teaching minutes) less the minutes moved into its neighbor:

| Fold-in day | Where its work goes | Minutes saved |
|---|---|---|
| 6 (checklist modify day) | The checklist is written as day 5's exit; the mixed set becomes day 7's opening | 37 |
| 9 (written reflection) | The "which point moved me" line is written in day 8's last 8 minutes; peer feedback goes | 29 |
| 12 (unit 2 hook) | The bus-route anchor opens day 13 in 8 minutes | 29 |
| 14 (values paragraphs) | Written as day 13's last 12 minutes, revised on day 22 | 25 |
| 17 (law evaluation) | Written in day 16's last 12 minutes, revised on day 22 | 25 |
| 19 (debate preparation) | Cards handed out on day 18's last 10 minutes; prepared in day 20's first 5 | 22 |
| 26 (unit 3 hook) | The two-halves anchor opens day 27 in 8 minutes | 29 |
| 37 (build day 5) | Teams build a smaller menu project; work spread over the other build days | 37 |
| 38 (build day 6) | Same: the smaller project needs five build days, not seven | 37 |
| 57 (unit 5 hook) | The two log entries open day 58 in 8 minutes | 29 |

Total: 10 lessons, about 299 teaching minutes, 64 course days to 54. The readiness checks keep their placements (the
last ten minutes before each unit), and the checks keep their order after units 2 and 4.

**Bar C1 on the short path** (lead call 2026-11-26: C1 holds on the Shorter path too). None of the ten fold-ins
carries S1 time, so two Specialty lessons are shortened as well, with no owned part cut and the lesson count unchanged:

- Day 5 runs as a half lesson of S1 time (about 18 minutes): both systems' limits traced to their sources in one
  combined card sort with one worked example and fewer cards per system; the other half writes and applies the class
  checklist from day 6's fold-in (HS-ALG-PS-05). Saves about 0.5 of an S1 day.
- Day 31 runs as a half lesson of S1 time (about 18 minutes, branch and merge cards); the clash card moves into day
  32's opening (about 5 minutes), since the version control part is part met anyway; the other half reads and traces
  the starter module on paper before day 32 changes it (HS-PRO-PD-15). Saves about 0.4 of an S1 day.

S1 time on the short path: about 3.9 day-equivalents of 42 teaching days, about 9.2 percent, under 10 percent.

## For the lead

1. **Katherine Johnson account.** Picked by this scope: NASA Langley's "She Was a Computer When Computers Wore Skirts"
   (nasa.gov, a 2008 interview with her words), found by search 2026-11-26, contents to check at source; if it is a
   profile, a NASA-published interview in her own words replaces it (expert read finding 8).
2. **Browser check:** the Smithsonian Hopper oral history transcript
   (si.edu/media/NMAH/NMAH-AC0196_hopp680700.pdf), 403 to automated reads, unverified until opened.
3. **Day 22 grade 9 readiness** sits four course days before unit 3 opens, one more than sequence.py's three-day reach,
   so days.csv marks day 25 as unit 3's readiness day and names the grade 9 items in day 22's note only.
4. **Rule 2 notes.** The grade 11 rows get both retrieval (for students who took grade 11) and a readiness check (for
   those who did not), by the frame's Course order (frame-write rule 32); any rule 2 note on readiness where retrieval
   is due comes from that design, not an error.
