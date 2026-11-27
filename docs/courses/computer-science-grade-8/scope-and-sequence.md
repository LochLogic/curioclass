# Scope and sequence: Computer Science, Grade 8

Course `computer-science-grade-8` (catalog id `cs-k12`), grade 8. Draft, written 2026-11-26 from
docs/courses/computer-science-grade-8/frame.md; fixed 2026-11-26 after the expert read
(docs/reviews/sequence-computer-science-grade-8-fixes-2026-11-26.md). The days live in data/plans/computer-science-grade-8/days.csv; this
page holds the judgment. Provisional while its partial base is not loaded (later.csv L149).

## The year at a glance

- **Days.** 64 course days: units 1 to 5 run 12, 13, 13, 12 and 8 days (days 1 to 12, 13 to 25, 29 to 41, 42 to 53,
  54 to 61); the mid-year course-level check is days 26 and 27 with respond day 28; the year-end check is days 62 and
  63 with respond day 64. The frame's units, order, owned rows and day counts are unchanged.
- **Meeting days and `school_day`.** Two 45-minute lessons a week for 32 weeks, an elective. Formula, stated once:
  course day k falls in week ceil(k / 2), on that week's second school day when k is odd and its fourth when k is
  even, so school_day = 5 (ceil(k / 2) - 1) + 2 or + 4; read back, week = (school_day - 1) // 5 + 1. Six days are
  pinned to the frame's school days to keep off grade 8 core check days (CALENDAR.md rule 3): day 26 on 65, day 27 on
  68, day 28 on 70, day 62 on 155, day 63 on 158, day 64 on 160. Every unit and check sits in the frame's weeks
  (checked 2026-11-26): unit 1 weeks 1 to 6, unit 2 weeks 7 to 13, the mid-year check weeks 13 and 14, unit 3 weeks
  15 to 21, unit 4 weeks 21 to 27, unit 5 weeks 27 to 30, the year-end check weeks 31 and 32 (week 32 the finals
  week). A school may use any two days of the week; the weeks are what count.
- **The 45 minutes.** Every day from day 2 opens with the three-minute retrieval trace (APPROACH.md "How a day
  opens"); the `retrieves` column names the row where it reaches back to an earlier unit or grade 7, and a blank means
  the opener traces the day before or shows the last exit ticket's wrong example. A device day keeps three minutes at
  the start to get devices out and open the page and four at the end to save work and put devices away, so it
  teaches about 33 minutes; a paper day about 40.
- **Devices and paper.** Device days are the frame's: 4, 7, 14, 16, 17, 19, 20, 22 to 25, 30 to 33, 43, 44, 47, 50,
  51, and the year-end check's code items where devices allow. Day 13 is a paper day with the teacher's one screen for
  the live-code, so the trace the project rests on keeps about 40 minutes; pairs first open the editor on day 14. Day 21
  is unplugged (the printed program traced by hand). Each device day's note gives the four ways (STANDARD.md "Devices
  and rooms") and names its paper path; every unit keeps unplugged days. MS-DAT-DI-25 is part met on
  the no-device path; MS-ALG-PS-05 is part met where a school has no approved tool (Cory 2026-11-26). The three queued
  editor modes (L148) are not used in grade 8, so no day waits on them.
- **Safety.** Copied into every device and security day's note: cords behind the table, devices carried closed with
  two hands; day 1 (the fake message beside the map) and security days 3 to 5 run only on toy systems inside our
  pages, and their teacher page carries health's "If a student tells you something" steps word for word.
- **Debugging.** Grade 7's debugging routine (day 5) is retrieved on day 14, on the anchor game's wrong-length bug,
  worked step by step: predict, run, compare, find the first place it goes wrong, change one thing, test again (CT9);
  for a student new to the elective it is first teaching. Days 17, 23 and 49
  use it by name; grade 9 retrieves it.
- **Days outside the standards (bar C1).** One day: day 61, the year look-back, which has no progression row or
  code. That is 1 of the 52 teaching days, about 2 percent, under the 10 percent limit. On the shorter path day 61
  folds into respond day 64, so none of the 48 teaching days (42 with the spare list) falls outside the standards.
  The list work past the middle school boundary (days 13, 14 and the list parts of days 16, 17 and 20) is not counted
  here: its row uses ~MS-ALG-PS-01 and ~MS-PRO-RD-17 again, written in `codes`, so those days are standard content
  (begun and used-again ids are standard content).
- **Base text.** Partial: the archived Teach Computing Curriculum (England, key stage 3, 2023), not yet loaded
  (L149). The days that lean on it carry its credit in the note: 3, 4 and 5 (Year 9 cybersecurity lessons 2, 4 and
  5), 13, 16, 17 and 20 (Year 9 Python sequences lessons 1 and 5), 18 (Year 8 layers lesson 6), 29 to 33 (Year 9 data
  science lessons 1 to 4), 34 (lesson 5, clean it up) and 37 to 39 (lesson 6), the base's own order. Every other day is
  our own. No source-map.csv in this run: the placements stay here and in the frame's Source map until the base is
  loaded (waits on L149).
- **Concept areas (bar item 1).** Unit 1 systems and security, unit 2 programming, unit 3 data and analysis, unit 4
  algorithms and design (with machine learning and programming), unit 5 computing and society. The practices sit
  inside each unit as the frame's Units table names them.

## Readiness and retrieval (rule 2)

Every earlier-grade row the course assumes was last used in grade 7, the year before, so each opens as a retrieval
task on the day the frame's Seams name, with the id in `retrieves`. No row is two or more grades back, so by rule 2 no
readiness check is owed. Because grade 8 is an elective that never assumes grade 7 was taken (frame Course order),
the frame still gives a ten-minute readiness check on the readiness days below. Every student sits the readiness items: for a student who took grade 7 they are the year-before retrieval, and the teacher reads them to find who needs the worked example (a teacher cannot always tell who took grade 7). sequence.py may note these as "readiness
where retrieval is due"; that is this elective path, on purpose.

| Row (last used grade 7) | Retrieval day | Readiness day (elective path) |
|---|---|---|
| g7-internet-resilience | 1 | 1 |
| g7-cia-effects | 3 | 1 |
| g7-system-requirements | 6 | 1 |
| g7-access-differences | 7 | 1 |
| g7-lists; g7-analyze-code | 13 (g7-analyze-code also 49) | 12 |
| g7-design-with-variables | 15 | 12 |
| g7-reference-docs | 18 | 12 |
| g7-collab-text | 21 | 12 |
| g7-test-refine | 22 | 12 |
| g7-sort-filter-groups | 29 | 28 |
| g7-viz-choices | 29, 33 | 28 |
| g7-personal-data | 34 | 28 |
| g7-improve-training-data | 42 | 41 |
| g7-examine-algorithm-harm | 46 | 41 |
| g7-pick-approach | 48 | 41 |
| g7-when-to-use-ai | 54, 57 | 53 |
| g7-impact-history | 56, 57 | 53 |
| g7-automation-work | 60 | 53 |

Each readiness check sits in the last ten minutes of day 1 (after the hook) or of the respond day before the unit
(12, 28, 41, 53); no other unit's first day holds one. The unit's first understanding day carries the short worked
example the frame names for flagged students, inside its minutes. Earlier units of this course come back in the
openers too (for example unit 1's attacks on days 14 and 20, unit 2's game on days 30, 39, 47 and 49, unit 3's
tables on days 43 and 44, unit 4's saved code samples on day 58), so the year's rows are spaced, not met once.

Where a school left out grade 7's unit 4 (grade 7's Swap or leave out line), g7-improve-training-data,
g7-examine-algorithm-harm and g7-pick-approach were taught to no one: day 41's readiness check covers them for the
whole class, and the worked examples on the first understanding days of g8-ml-evaluate, g8-modify-for-bias and
g8-ai-tool-day (unit 4) are the bridge for every student.

## Unit 1: Systems that hold up (days 1 to 12, weeks 1 to 6)

**Arc.** A cut link on an invented district map opens the year: trace the failure, then redraw the map with a
backup link (days 1 and 2). The fake password message beside the map becomes the security days: attacks matched to
the side of the triangle they hurt (day 3), the toy inbox and preventions (day 4), a protection plan (day 5). Day 6
compares two systems against another group's requirements. The sign-up page then carries the design days: find the
barrier against four stated needs (day 7), a team design change (day 8), test it (day 9), revise and retest (day 10).
**Why this order.** Network paths before attacks, since an attack's entry point is read on the map; attacks before
preventions; the barrier is found on the device before any team designs a change, and the test precedes the revision.
Day 1 is first because it sets the year's device and toy-page rules.
**Assessments.** End-of-unit assessment day 11 (paper, about 35 minutes, unseen): a new map and failure, three new
attacks with side, prevention and reason (SE-33, both attacks and preventions), a design change for two stated needs
with its test (IM-36), and a short justification recorded for the HW-30 thread. Day 10 is observed (`observe`) for the
"collaborate" part of IM-36, with look-fors on the team product: the change on the system-diagram, which stated need
each part serves, the day 9 test record, the revision and retest, and each member's named role; IM-36 is scored on day
11's item and day 10's observed team product. Response: respond day 12, which holds unit 2's readiness check.
**Candidate.** Kept: the base's social engineering order (the trick, then its clue) inside days 3 and 4, zero days.
**Sensitivity.** Disability needs are test conditions, never acted (days 7 to 10, sensitivity read before the case cards (docs/pipeline/briefs/sensitivity-read.md)); online safety on days 3 to 5 as
above. The CISA phishing page is a browser check.

## Unit 2: Make it, credit it, hand it over (days 13 to 25, weeks 7 to 13)

**Arc.** The other class's flawed word-guess game is traced line by line on paper while the teacher live-codes on one
screen (day 13), modified in small checked steps on the pairs' first editor day, where grade 7's debugging routine is
retrieved on its wrong-length bug (day 14), then each pair designs its own game with a test-table planned first (day 15) and builds it (days 16 and
17). Credit and permission are taught unplugged (day 18) the lesson before a borrowed word-picking function enters
the project with its credit comment (day 19). The draft is finished (day 20) and handed to a partner who traces it
(day 21). The anchor game's accessibility faults are named as a worked example before classmates test each project
(day 22); refine (day 23), retest (day 24), hand in on the rubric (day 25).
**Why this order.** Trace, then modify, then make (APPROACH.md): no build before the worked game is traced and
changed. Attribution sits on the day a borrowed function enters, so the credit line is written for a real use.
Refine-for-users follows the draft so feedback has a program to act on, and reuses unit 1's stated needs.
**Assessments.** The project is scored on its rubric on day 25 (design, build, credit comment, change log), a Check
day reported with day 26. The unit's unseen-item sitting is the mid-year check day 26, the day right after the unit's
last day, which stands for the end-of-unit assessment (frame Days; sequence.py accepts it). Its TR-20 item gives a new
screen with two classmates' feedback lines to act on, since the standard is refining from feedback. Response: day 28.
No mid-unit assessment (13 days).
**Candidate.** Kept: the base's live-coding of the worked program before pairs try it, inside day 13, zero days.
**Sensitivity.** Days 22 and 24 treat disability needs as test conditions, never acted, with the sensitivity read before the case cards (docs/pipeline/briefs/sensitivity-read.md). Word lists from neutral topics; no student's name, photo or voice in a program; feedback is about
the program, never the classmate.

## Unit 3: Data that answers back (days 29 to 41, weeks 15 to 21)

**Arc.** Twelve pool days plotted by hand (day 29), then the whole table in the tool: trend, prediction and
classification by threshold (day 30). Two more sets show no relationship and a falling one, that a relationship is not
a cause, and one pool prediction outside the data is judged (day 31). Pairs run an investigation on one of three
invented sets (days 32 and 33). A park survey followed through its stages (day 34) leads to one stage decision
carried into a misleading chart (day 35) and a weaker model (day 36). A flawed summary is graded and the summary's
parts named (day 37), with possible biases named by stage and decision, before each student drafts (day 38) and
revises after partner feedback (day 39).
**Why this order.** Hand plot before the tool, so the scatter means something; the out-of-data judgment beside the
no-relationship sets, where "what the data can and cannot tell you" is the day's idea; the investigation before the
summary, so students summarize a process they ran; the stage decisions before the summary, so its biases part names a
stage and a decision instead of being written blind (MS-DAT-DI-27 names biases). This is also the base's own order
(lesson 5 before lesson 6), and the weaker model still reaches unit 4 through day 44's retrieval of
g8-biased-decisions.
**Assessments.** End-of-unit assessment day 40 (about 35 minutes, unseen): relationship, prediction, classification
and judgment (DI-25; the item runs in the table-and-scatter tool where the class has devices, one per pair or stations
while the rest is on paper, and by hand on the no-device path, marked part met); a new summary's missing part and
unsupported claim (DI-27), with day 39's revised summary scored on its full checklist; two biasing stage decisions and
what each does to a chart and a model (IM-29). Response: respond day 41, which holds unit 4's readiness check.
**Candidate.** Kept: the base's "clean it up" step as the clean stage of day 34, zero days.
**Leans.** m8-scatter-plots: math teaches it on school days 56 to 69, before day 29 (school day 72): met.
e8-produce-publish: ELA unit 3 ends on school day 88, before the summary days 37 to 39 (school days 92, 94, 97): met
before; day 37's checklist and graded summary carry the structure anyway, and day 39 uses the checklist, not an ELA
revision method.
**Sensitivity.** All data invented and about things; the survey's people invented and unnamed.

## Unit 4: AI under test (days 42 to 53, weeks 21 to 27)

**Arc.** The fruit classifier that misses green ripe fruit is the hook; students predict its misses on paper (day
42), read its test results as a table (day 43), name the feature behind the errors and its limits (day 44) and check
its model card (day 45). The lottery rule is traced and its harm named (day 46), then changed and retested (day 47).
A generated output is judged on the teacher's one screen (day 48); a saved generated sample for the unit 2 game is
traced with its first wrong line named (day 49), four samples are judged (day 50), and a written verdict picks one
for the project (day 51).
**Why this order.** A model's patterned errors are met where students can see them before they judge a tool's code;
trace before modify for the lottery rule; the worked trace on day 49 comes before the four-sample judgment.
**Assessments.** End-of-unit assessment day 52 (about 35 minutes, unseen), each part asked: features and limits
(ML-08), modify and retest (IM-11), output against the problem (PS-05), accuracy and usability (RD-18). Response:
respond day 53, which holds unit 5's readiness check.
**Candidate.** Kept: a second lottery rule with a different harm as the respond day's new form (day 53), zero days.
**Leans.** m8-function-define: math teaches it on school days 93 to 115, before day 43 (school day 107): met; the
bridge (taught in words, no function notation) stays in the note.
**Sensitivity.** Fruit drawings, never people; the lottery talk is about the rule; no student uses a live tool or an
account.

## Unit 5: New technology, our town (days 54 to 61, weeks 27 to 31)

**Arc.** The video visit case with its dated federal finding (day 54) and an invented route tool (day 55) teach how a
design decision changes the experience for different communities. The credit records history case asks what a rule
could have done earlier (day 56) and lends the debate its question. Debate preparation from a two-sided packet (day
57), the structured debate (day 58), and each student's own written claim, backing and rebuttal (day 59). A career
sketch (day 60) and the year's look-back map (day 61) close the units.
**Why this order.** Design decisions before the debate, so students argue with the units' evidence; the history case
right before the debate preparation; the career sketch and look-back last, as the year's closer.
**Assessments.** The year-end check (day 62), the day right after the unit's last day, scores the unit in full with
unseen items and stands for its end-of-unit assessment (frame Days; sequence.py accepts it). Day 59's written claim is
the debate's written practice, collected, not scored, before the unseen ET-42 item on a new question on day 62:
practice before assessment, not a repeated check form. Response: day 64.
**Leaving unit 5 out.** A school that swaps unit 5 runs day 62 as the swap unit's own check. A school that leaves it
out gives days 54 to 61 to the swapped unit or a project extension and day 62 to a second sampling lesson on units 1
and 2 with new items; the family note names MS-SOC-ET-41 and MS-SOC-ET-42 as not claimed that year.
**Candidate.** Dropped: a visit by a town planner; the packet carries both sides and a visit needs the school's own
arrangement, zero days.
**Lean.** e8-collab-discussion: met in ELA grade 8 unit 1 (weeks 1 to 6); day 57 teaches the roles and the frame
anyway.
**Sensitivity.** Day 54 stays on how the service was designed (the ASPE report is a browser check), and its teacher
note calls video visits an emerging technology at the time of the report, 2021, with days 55 and 62 carrying the
current cases; days 57 to 59
keep two sides, neither declared right; day 56 never touches a family's credit; day 60 asks nothing about a family
member's job.

## Course-level checks

| Check | Days (school days, weeks) | What it covers |
|---|---|---|
| Mid-year | 26 and 27 (65 and 68, weeks 13 and 14); respond 28 (70, week 14) | Day 26: unit 2 in full (trace, PD-14, TR-20 from two given feedback lines), about 25 minutes. Day 27: unit 1 sampled with short new items (SE-33, IM-36; IM-36's collaborate part carried from day 10's observation), about 20 minutes. Unit 2's rubric score from day 25 reported, not rescored. |
| Year-end | 62 and 63 (155 and 158, weeks 31 and 32); respond 64 (160, week 32) | Day 62: unit 5 in full (ET-41, ET-42), about 30 minutes. Day 63: units 3 and 4 sampled with four short new items, each part asked (DI-25 prediction and judgment; IM-29 one decision and what it does to a chart and a model; ML-08 one feature and one limit; RD-18 the first wrong line and one usability fault), about 30 minutes. |

Each check's second lesson draws its items from earlier units, not the unit just ended, so it does not repeat that
unit's assessment. Off every grade 8 core check day (civics 48, 49, 96, 97, 145, 146; ELA 89, 90, 125, 126; math 70,
116; science 75; finals week 32); day 28 on math's day 70 is a respond day, not a check.
**Owned codes sampled on a course-level check (rule 3, L107).** 10 of 13. Not sampled, as the frame sets the checks:
MS-DAT-DI-27 (a written summary does not fit a short item; scored on day 40 and on day 39's revised summary),
MS-ALG-IM-11 and MS-ALG-PS-05 (scored on day 52; PS-05 is part met in many schools and a check item would need the
teacher's screen). For the lead 1 offers a fix inside day 63's minutes.

## Shorter path

**A shorter period (40 minutes).** The opener and the device minutes stay; a device day teaches about 28 minutes and
a paper day 35. The cut comes from make-day build time (days 16, 17, 20, 23), never from a trace or modify day, and
the check sittings (25 plus 20, 30 plus 30 minutes) still fit.
**A year about 10 school days short** (two weeks, four sessions at two a week). Fold in the four marked "10 school
days" below: days 33, 45, 50 and 61, 180 minutes, leaving 60 of the frame's 64 course days; no modify day or worked
example is touched. The other six (days 4, 10, 17, 24, 31 and 59) are a named spare list for a year shorter still.
Each fold-in folds into a neighbor, nothing assessed and no owned part cut, 45 minutes saved each:
- Day 4 into days 3 and 5 (the inbox sort on paper inside day 3, preventions matched at the start of day 5).
- Day 10 into day 9 (test and revise in one lesson, one retest; day 9 then carries day 10's observation and
  look-fors).
- Day 17 into days 16 and 20 (one build day fewer).
- Day 24 into day 23 (retest at the end of the refine lesson).
- Day 31 into days 30 and 32 (the no-relationship and falling sets as a ten-minute contrast at the end of day 30; the
  out-of-data judgment made on each pair's own set as the prediction day 32 judges).
- (10 school days) Day 33 into days 32 and 38 (the pair's prediction judged at the end of day 32; the fairest chart drawn in the
  summary draft on day 38).
- (10 school days) Day 45 into day 44 (the model card read at the end of day 44).
- (10 school days) Day 50 into days 49 and 51 (two samples on day 49, the verdict on day 51).
- Day 59 into day 58 (the debate runs one round fewer and its last ten minutes are each student's own claim, backing
  and rebuttal on a card; ET-42 is still scored unseen on day 62).
- (10 school days) Day 61 into day 64 (the look-back map on the respond day).

Day 1 keeps its hook, its new failure and its readiness check, and day 2 stays: day 1 has no room for a fold.

Total: the four marked days save 180 minutes (60 of 64 course days); with the spare list, 450 minutes, ten lessons,
54 of 64. Every unit, check and respond day is kept on either path.

## For the lead

1. **Three owned codes not on a course-level check (L107).** Suggested frame fix: day 63 adds one 5-minute item for
   MS-ALG-IM-11 (a new rule's harm and the change) and the day 52 PS-05 and day 40 DI-27 records are named as carried,
   or the frame names the three and why, as this page does.
2. **Browser checks.** CISA phishing page (day 4) and the ASPE telehealth report (day 54), at grade close.
