# Expert read: scope and sequence, Computer Science, Grade 8 (2026-11-26)

Course `computer-science-grade-8`. Cold read by the curriculum expert (docs/agents/EXPERT.md), brief
docs/pipeline/briefs/sequence-read.md with build/scope-writes/CS-READ.md. The scope was written by a fresh Claude agent
(build/scope-writes/CS-BRIEF.md); this reader did not write it.

## What I read

- docs/courses/computer-science-grade-8/scope-and-sequence.md and data/plans/computer-science-grade-8/days.csv (all 64
  rows), cold.
- Beside them: docs/courses/computer-science-grade-8/frame.md (whole), the grade 8 rows of
  data/progressions/computer-science.csv, data/standards/csta-2026-statements.txt for the 13 owned ids,
  docs/courses/CALENDAR.md (stagger rule 3), the grade 8 math and ELA days.csv (for the leans), the lens
  docs/agents/lenses/computer-science.md, docs/ADOPTION-BAR-SUBJECTS.md part 5, docs/courses/computer-science/APPROACH.md
  ("How a day opens"), build/scope-writes/CS-BRIEF.md, and docs/reviews/sequence-computer-science-grade-6-2026-11-26.md
  for REPEAT.
- Gates: `sequence.py check computer-science-grade-8` 0 failures; `plan.py check` 0 failures for this course;
  `frame.py calendar` 0 failures for this course (64 days, 58 in units, 6 for checks and respond days); `stale.py check`
  reports nothing for this course. The gates settle day numbers, totals, kinds, an assessment per unit, respond days and
  owned ids placed, so this read spends its time elsewhere.
- Checked by hand: every `school_day` against the stated formula and the six pinned days; every unit and check inside
  the frame's weeks (unit 1 weeks 1 to 6, unit 2 weeks 7 to 13, mid-year check weeks 13 and 14, unit 3 weeks 15 to 21,
  unit 4 weeks 21 to 27, unit 5 weeks 27 to 31, year-end check weeks 31 and 32); no check on a grade 8 core check day
  (week 32 is the finals week and may hold year-end checks, CALENDAR.md rule 3); the two math leans (8.SP.A.1 taught on
  math school days 56 to 69, before day 29 at school day 72; 8.F.A.1 defined on math school days 93 and 94, before day
  43 at school day 107) and the two ELA leans (SL.8.1 from ELA day 10; W.8.5 and W.8.6 through ELA day 88).

## Verdict

The scope is sound and close to ready: it keeps the frame's units, owned ids, check weeks and readiness days exactly,
trace comes before modify before make on every programming row, every unit keeps unplugged days, and every society case
is dated and guarded. The most serious fault is order inside unit 3: students write the "possible biases" part of their
investigation summary (days 34 to 36) before the days that teach how decisions at each data stage bias a dataset (days
37 to 39), and swapping the two blocks fixes it while restoring the base text's own order and meeting the ELA lean
outright. The other changes are smaller: a scored record for the "collaborate" part of MS-SYS-IM-36, named paper paths
on the device days that lack one, the `end` marks the gate no longer needs, and one shorter-path fold that overloads day
1. Thirteen findings.

## Findings, most serious first

### 1. Unit 3 asks for a summary's biases before it teaches where biases come from

What is wrong: day 34's checklist, day 35's draft and day 36's revision ask each student to name the possible biases of
the pair's investigation (MS-DAT-DI-27 names "potential biases"). The days that teach how a decision at a data stage
(who was asked, which rows were dropped, how a label was chosen, which chart was used) produces biased data, a misleading
conclusion and a weaker model are days 37 to 39 (MS-DAT-IM-29). Grade 7's g7-personal-data, the only earlier row on
the matter, is about consent and ownership, not stage decisions, and it is retrieved only on day 37.
Why it matters: the biases part of every summary is written blind, so the scored revised summary (day 36, scored with
day 40) is weakest on the part the standard names first. A busy writer of day 35 has nothing to point students at.
The scope's reason for the current order ("the stages last, because the weaker model hands straight to unit 4's
classifier") is already carried by day 44's retrieval of g8-biased-decisions, and days 40 and 41 sit between in either
order.
Fix (settled by the expert, a day swap inside the unit): move the stage block to days 34 to 36 (day 34 the park survey
through its stages with the g7-personal-data retrieval, day 35 the misleading chart, day 36 the weaker model) and the
summary block to days 37 to 39 (day 37 the graded summary and checklist, day 38 the draft, day 39 partner feedback and
revision, scored with day 40). Keep each position's `school_day`. Day 37's checklist then says "possible biases: name
the stage and the decision". Three gains: the summary can name stage decisions; the data science base's lesson 5 (clean
it up) again comes before lesson 6, its own order, so the frame's Source map reason for moving it falls away; and the
summary days fall on school days 92, 94 and 97, after ELA grade 8 unit 3 ends (school day 88), so e8-produce-publish
is met before, not alongside. Update the unit 3 Arc, Why this order and Leans paragraphs and the day 36 note ("scored
with day 40") to day 39.
LAYER sequence (the frame's Units cell and Source map row carry the same order; For the lead). REPEAT new. Confidence:
likely (statement text; the order follows from it).

### 2. The "collaborate" part of MS-SYS-IM-36 has no scored record

What is wrong: MS-SYS-IM-36 is "collaborate to improve the design ... to meet the needs of diverse users". The team
days 8 to 10 carry the collaboration; day 10's note says the team product "stands for the together part", but day 10
has no `assess` value and no look-fors, and both scored items on it (day 11 and day 27) are individual paper items.
Why it matters: the course record shows IM-36 met on the strength of two solo items; the collaborative part is named,
not carried (the most common sequence-read fault).
Fix (settled by the expert): day 10 `assess` = `observe`, with its note naming the look-fors: the change on the
system-diagram, which stated need each part serves, the team's test record from day 9, the revision and retest, and each
member's named role. Day 11's note then reads "IM-36 scored on day 11's item and day 10's observed team product".
LAYER sequence. REPEAT yes (a part named and not carried; grade 6 finding 1). Confidence: firm.

### 3. Several device days name no paper path, and day 21 is a device day only in its note

What is wrong: the frame says every device day is written four ways and names the paper version of each owned id that
needs one (MS-PRO-TR-20: "a paper prototype of a program's screens tried by two classmates against the stated needs";
MS-ALG-ML-08: printed test results and model card; MS-PRO-RD-18: printed samples on a paper test-table). Days 4, 7, 13,
14, 16, 30, 43, 47 and 50 name their paper path. Days 19, 20, 22, 23, 24, 25, 31, 32, 33, 44 and 51 carry only the
four-ways boilerplate. Days 22 to 24 matter most: no note names the paper prototype, and "try the game by keyboard alone,
enlarged, without color, read aloud" has no stated no-device form. Day 21 carries the full device boilerplate, but
neither the frame's device list nor the scope's own list ("22 to 25") includes it, and its task (a partner traces the
key part on a trace-table) is paper work.
Why it matters: CS-READ asks that a device day always has a paper or unplugged path meeting the same ids; in a
no-device school the section writer of days 22 to 24 has to invent how TR-20 is met.
Fix (settled by the expert): add one paper-path line to each listed day: 19 (the supplied code page printed; the credit
comment and justification written on it), 20 (code finished on paper, a partner as the computer runs the test-table),
22 to 24 (the paper prototype of the game's screens, each stated need tried by two classmates on the printed screens:
keyboard order marked as numbered steps, enlarged print, a grayscale copy, the output read aloud by the partner; the
change drawn and retested on paper), 25 (the paper project and test-table handed in on the same rubric), 31 to 33 (the
printed sets plotted by hand, with the DI-25 "part met without a device" mark), 44 (the printed results table), 51 (the
printed samples and day 50's paper test-tables). Day 21: drop the device boilerplate and write "Unplugged: the printed
program traced by hand".
LAYER sequence. REPEAT yes (pair and device boilerplate where it does not fit; grade 6 finding 7). Confidence: firm
(the note text).

### 4. Days 25 and 59 carry `end`, which the gate no longer needs; For the lead 3 and 4 are stale

What is wrong: sequence.py now accepts a course-level check on the day right after a unit's last day as that unit's
end-of-unit assessment (lead fix 2026-11-26). Day 26 follows unit 2's last day and day 62 follows unit 5's, so the
`end` marks on day 25 (the rubric hand-in) and day 59 (a teaching day: each student writes a claim, backing and
rebuttal) are now workarounds. Day 59 as scored also makes For the lead 3 look like a repeated-form problem.
Why it matters: an `end` on a teaching day tells the section writer to build day 59 as an assessment eight days before
the unseen check on the same form; and the scope's For the lead 4 asks for a gate change that has landed.
Fix (settled by the expert): clear `assess` on day 59 and say in its note that it is the debate's written practice,
collected, not scored, before the unseen ET-42 item on day 62. Day 25 keeps kind Check as the scored rubric product
reported with day 26 and its `assess` is cleared (rerun sequence.py). Delete For the lead 4. For the lead 3 then needs
no frame fix: practicing the claim-backing-rebuttal form on the debate question and meeting it unseen on a new question
on day 62 is ordinary practice before assessment, not a repeat; drop it or reword it as a note.
LAYER process. REPEAT yes (grade 6 finding 5; music 3 to 5). Confidence: firm.

### 5. Day 26's MS-PRO-TR-20 item has no user feedback in it

What is wrong: TR-20 is refining a technology "based on user feedback". Day 26's item asks the student to name two
faults on a new screen, the test that finds each and the change: the student finds the faults, so no feedback is acted
on.
Why it matters: unit 2's only unseen TR-20 item tests fault-finding, which day 22 teaches, not refining from feedback,
which days 23 and 24 teach.
Fix (settled by the expert, item wording): the item gives a new small program's screen with two classmates' written
feedback lines (one usability, one accessibility); the student writes the change for each, the test that checks it and
one feedback line they would not act on and why. Same 7 minutes.
LAYER sequence. REPEAT yes (a statement's part not asked). Confidence: firm.

### 6. Day 13 is overloaded for a device day

What is wrong: day 13 holds the five-minute hook, the teacher's live-coding of the worked game, a line-by-line trace of
about twenty lines with a trace-table and a list-diagram, the two retrievals and the worked list example for students
day 12's check flagged, all inside a device day's 34 teaching minutes. For a student who did not take grade 7 this is
also their first text program of the elective.
Why it matters: the trace is the day the whole project rests on (trace before modify before make), and it is the day
most likely to be cut short.
Fix (settled by the expert, a day-level choice inside the unit): day 13 runs as a paper day with the teacher's one
screen for the live-code (the printed program and trace-table for every pair), so it teaches about 40 minutes; pairs
first open the editor on day 14. Update the scope's device-day list and the frame's list at the next frame pass (For
the lead).
LAYER sequence. REPEAT yes (a day holding more than its minutes; grade 6 finding 8). Confidence: judgment call.

### 7. The shorter path folds day 2 into a day 1 that is already full

What is wrong: the first fold-in puts day 2's backup link on day 1 as an exit task, but day 1 already holds the hook,
the retrieval, the new failure traced and redrawn and a ten-minute readiness check in its last ten minutes.
Why it matters: a teacher on the short year loses either the readiness check (the elective path's only gate) or the
backup-link task.
Fix (settled by the expert): replace that fold with day 59 into day 58: the debate runs one round fewer and its last ten
minutes are each student's own claim, backing and rebuttal on a card. Nothing assessed is cut (ET-42 is scored unseen on
day 62) and day 2 stays. The total stays ten lessons.
LAYER sequence. REPEAT yes (shorter-path folds that do not fit; grade 6 finding 2). Confidence: likely.

### 8. Day 30 holds all of MS-DAT-DI-25 in one device day; day 31 holds little

What is wrong: day 30 (34 device minutes) asks for the trend, a prediction, a classification by threshold and a judged
prediction outside the data; day 31 only adds two contrasting sets and "a relationship is not a cause".
Why it matters: the judgment of an out-of-data prediction is the part unit 4 reuses and day 40 scores, and it is the
part a rushed day 30 drops.
Fix (settled by the expert, a part moved inside the unit): the out-of-data judgment (the 45 degree day, the closed pool)
moves to day 31, beside the no-relationship and falling sets, where "what the data can and cannot tell you" is the day's
idea.
LAYER sequence. REPEAT new. Confidence: judgment call.

### 9. Day 40's MS-DAT-DI-25 item does not say the tool is used

What is wrong: DI-25 is met only on a device (STANDARD.md), and day 40 is not a device day; its note says "by hand on
the paper path" but never says where the tool comes in, so every school may record DI-25 as part met.
Fix (settled by the expert): day 40's note: "the DI-25 item runs in the table-and-scatter tool where the class has
devices (one per pair, or stations while the rest of the sitting is on paper); by hand on the no-device path, marked
part met".
LAYER sequence. REPEAT new. Confidence: likely.

### 10. Debugging is practiced but never named as the method

What is wrong: the lens and APPROACH ask that debugging be taught as a method (predict, run, compare, find the first
place it goes wrong, change one thing, test again). Unit 2 fixes the anchor game's faults on day 14 and logs "yes" or
"not yet" on day 17, and unit 4 names the "first wrong line" on days 49 to 52, but no day names the method's steps.
Fix (settled by the expert): day 14's note names the steps as the year's debugging routine on the anchor game's
wrong-length bug, and days 17, 23 and 49 say "the debugging routine from day 14".
LAYER sequence. REPEAT new. Confidence: likely.

### 11. Day 1 shows the fake password message without the security guard

What is wrong: the anchor puts a fake "reset your password" message beside the map on day 1, but only days 3 to 5 carry
the security line and health's "If a student tells you something" steps.
Fix (settled by the expert): copy the security-day line into day 1's note (the message is a toy on our page; no real
account; the teacher page carries the steps).
LAYER sequence. REPEAT new. Confidence: firm.

### 12. Leaving unit 5 out leaves day 62 with nothing to score

What is wrong: the frame lets a school leave unit 5 out. Day 62 scores unit 5 in full; the scope does not say what days
54 to 62 become.
Fix (settled by the expert): one sentence in the Shorter path or unit 5 section: a school that leaves unit 5 out runs
day 62 as the swap unit's own check when it swaps, or, when it leaves the unit out, gives day 62 to a second sampling
lesson on units 1 and 2 with new items, and days 54 to 61 to the swapped unit or project extension; the family note
names ET-41 and ET-42 as not claimed.
LAYER sequence. REPEAT yes (grade 6 finding 6). Confidence: likely.

### 13. Two small wording faults in the frame and one dated case

- The frame's Days bullet says a lesson opens with a "five-minute retrieval trace"; APPROACH.md gives a three-minute
  trace inside the five-minute opener, as the scope says. Fix at the next frame pass. LAYER frame. REPEAT new.
- Day 54's case (telehealth use in 2021, the ASPE 2022 report) is accurate as far as memory goes (video less common and
  audio-only more common among older adults, people with lower incomes and some racial and ethnic groups; Census
  Household Pulse data), but video visits are no longer new in 2026. Fix: the teacher note calls it "an emerging
  technology at the time of the report, 2021" and day 55 (route tool) and day 62 (translation tool) carry the current
  cases, as they do. Confirm the figures at the browser check. LAYER sequence. REPEAT new. Confidence: from memory.

## What is right and should not be touched

- Trace, modify, make on every programming row: 13 trace, 14 modify, 15 design, 16 and 17 make; the lottery rule traced
  (46) before it is modified (47); one worked trace of a generated sample (49) before four are judged (50, 51).
- Every owned id sits on teaching days and on its unit's assessment; no id outside the frame's 13 is claimed; the seven
  used-again ids are named with "~" and never claimed.
- The readiness design: every assumed row is a year-before row, retrieved on the day the frame's Seams name, with the
  elective path's ten-minute checks on days 1, 12, 28, 41 and 53 and never on another unit's first day. That every unit
  "checks a year-before row" is the frame's elective rule (frame-write rule 32), stated in the scope, not a fault.
- The course-level checks draw their second lesson from earlier units (unit 1 on day 27, units 3 and 4 on day 63), and
  the scope says so; the calendar is exact against the frame and off every grade 8 core check day.
- Society cases are dated and guarded: the FCRA case (1970) is accurate, the data center figures cite the December 2024
  national laboratory report, both debate sides stay open, and no task asks about a family's work, health, home or
  credit. Disability needs are test conditions throughout.
- The C1 count (list work about 4 of 52 teaching days) and the source credits per day.

## What I could not judge

- The base text's lesson files (not loaded, L149): placements rest on the frame's public-page map.
- The ASPE and CISA pages (browser checks, not fetched); the LBNL figures from memory (about 4.4 percent of US
  electricity in 2023, a projected 6.7 to 12 percent by 2028).

## Settled by the expert

| Choice | Reason in one line | File it touches |
|---|---|---|
| Swap unit 3 days 34 to 36 (summary) with 37 to 39 (stages) | Biases are taught before the summary names them; base order and the ELA lean restored | days.csv rows 34 to 39, scope unit 3 |
| Day 10 `assess` = `observe` with team look-fors | Carries IM-36's "collaborate" part | days.csv day 10, 11 |
| Paper-path line on days 19, 20, 22 to 25, 31 to 33, 44, 51; day 21 unplugged | Every device day meets its ids on paper | days.csv notes, scope device list |
| Clear `assess` on days 25 and 59; delete For the lead 4, drop For the lead 3 | The gate now accepts the following check | days.csv, scope For the lead |
| Day 26 TR-20 item gives two feedback lines to act on | The standard is refining from feedback | days.csv day 26, scope checks table |
| Day 13 a paper day with the teacher's screen; editor from day 14 | The trace day needs its 40 minutes | days.csv day 13, scope device list |
| Shorter path: day 59 into 58 replaces day 2 into 1 and 3 | Day 1 is full; day 59 is unscored practice | scope Shorter path |
| Out-of-data judgment moves from day 30 to day 31 | Balances DI-25's two tool days | days.csv days 30, 31 |
| Day 40 names the tool for the DI-25 item | DI-25 is met only on a device | days.csv day 40 |
| Day 14 names the debugging routine; 17, 23, 49 point to it | Debugging taught as a method | days.csv notes |
| Security line copied to day 1 | The fake message appears on day 1 | days.csv day 1 |
| Unit 5 leave-out sentence for day 62 | The frame allows the leave-out | scope |
| Day 54 note: "emerging at the time of the report" | Case currency | days.csv day 54 |

## For Cory

None. Every finding is item-level or a day swap inside a unit; no change of scope, audience, money or people.

## For the lead

- Finding 1 changes the frame's unit 3 Units cell and its Source map row (data science lesson 5 no longer moved);
  finding 6 changes the frame's device-day list (day 13); finding 13 the frame's opener wording. All at the next frame
  pass.
- The caller logs each finding with `plan.py defect ... --found-by expert`; this read edited no file but this report.

## Sources

- data/standards/csta-2026-statements.txt (2026 CSTA PK-12 Computer Science Standards, CC BY-NC-SA 4.0): the 13
  statements, for every part named above.
- data/plans/math-grade-8/days.csv and data/plans/english-language-arts-grade-8/days.csv: the lean dates.
- docs/courses/CALENDAR.md rule 3: finals week.
- From memory, not re-fetched: ASPE, "National Survey Trends in Telehealth Use in 2021" (2022); Lawrence Berkeley
  National Laboratory, 2024 United States Data Center Energy Usage Report; FTC page on the Fair Credit Reporting Act.
