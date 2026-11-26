# Expert read: scope and sequence of Computer Science, grade 12 (2026-11-26)

Job: docs/pipeline/briefs/sequence-read.md, with build/scope-writes/CS-READ.md and CS-BRIEF.md. Read cold; I did not
write the scope. Edits: this report only.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/computer-science.md, docs/ADOPTION-BAR-SUBJECTS.md section 5 and C1,
  docs/courses/computer-science/APPROACH.md ("How a day opens", fields 6 and 8), build/scope-writes/CS-BRIEF.md.
- docs/courses/computer-science-grade-12/scope-and-sequence.md and data/plans/computer-science-grade-12/days.csv, in
  full; docs/courses/computer-science-grade-12/frame.md, in full.
- data/progressions/computer-science.csv (the ten grade 12 rows); data/standards/csta-2026-statements.txt (the 14
  owned statements); docs/courses/CALENDAR.md rule 4; data/plans/calendar.csv (English language arts grade 12 units).
- docs/reviews/frame-computer-science-grades-6-to-12-2026-11-25.md (M1, M3, M7 for grade 12) and, for REPEAT tags,
  docs/reviews/sequence-dance-grades-9-to-12-2026-11-26.md. No earlier computer science scope read exists.
- Gates: `sequence.py check computer-science-grade-12` 0 failures; `plan.py check` has no grade 12 computer science
  failures (failures listed are other courses); `frame.py calendar` no grade 12 computer science line; `stale.py
  check` 6 failures, none in this course. I recomputed school_day for all 64 rows against the stated formula (course
  day 2k-1 on school day 5k-3, day 2k on 5k-1): all match; units and checks sit in the frame's weeks (unit 3 weeks 13
  to 23, check 1 week 12, respond 25 week 13, year-end days 54 to 56 weeks 27 and 28, unit 5 weeks 29 to 32).
- Sources: memory only for the case facts below (no outside page fetched on this read); marked where a finding rests
  on it.

## Verdict

The scope is sound and follows its frame closely: every owned id sits on taught days, the capstone runs read, then
design, then modify, then build, every device day carries its four ways and a paper path, the senior calendar holds,
and the sensitivity guards are copied into the days. The biggest risk is in the assessments: three check items name a
code but prompt for only some of its parts (HS-ALG-PS-05's bias on day 24, HS-SOC-HU-44's consciousness and ethics on
days 10 and 24, HS-SOC-CE-45's teams, technologies and "express ideas" on day 63), and S1-SWD-UX-05's "create" part is
never scored. The one change that matters most is to write a prompt per part on those items; second, the 10-days-short
path pushes the S1 share over bar C1's 10 percent and needs rebalancing.

## Findings, most serious first

### 1. Three check items list a code but ask only part of it

LAYER frame (the frame's check table and unit 1 and 5 evidence lines), carried into the sequence. REPEAT yes (items
that list a code but ask only some of its parts: dance 9 to 12 findings 2 and 3). Confidence: firm (the statements
in data/standards/csta-2026-statements.txt against the day notes).

- **HS-ALG-PS-05** ("bias, accuracy, and potential harms"). Day 24 asks for "accuracy and harm"; bias is dropped.
  Day 55 says only "a saved output judged". Fix: day 24's goal reads "a new saved output judged for accuracy, bias
  and harm, a prompt for each"; day 55's item names the same three prompts in its 10 minutes.
- **HS-SOC-HU-44** (differences between human and artificial intelligence, and their implications for
  consciousness, ethics and human responsibility). Days 10 and 24 ask for "a short written argument on a new
  responsibility case", which reaches one of the three implications and never asks for the difference itself.
  Day 7 teaches all three, so the gap is only in the items. Fix: day 10's HS-SOC-HU-44 part has three prompts: name
  one difference between human and artificial intelligence the case turns on; say what it means for a claim about
  consciousness (as a claim people make, no view marked right); and say who is responsible and on what ethical
  ground. Day 24 keeps its 12 minutes with the difference prompt and one of the two implication prompts, rotated.
- **HS-SOC-CE-45** (diverse teams use computational thinking and computing technologies to solve problems and
  express ideas). Day 63's prompts are "computational thinking at work, a barrier, opening the field": the barrier
  and opening the field come from the row's notes, while "teams", "computing technologies" and "express ideas" are
  never asked. Fix: day 63's prompts become (a) a team and how its different views changed what it built (the unseen
  log item already does this), (b) how the team or person used computational thinking and a computing technology to
  solve a problem, (c) one idea the work expressed or let others express, then (d) the barrier and the opening of
  the field as the row adds. Day 59's reading guide asks the same four, so the item is taught before it is scored.

Cost: a writer builds the items straight from these notes, so the end-of-unit and check scores would claim parts no
student was asked about (bar C1 "a standard lacks a check item").

### 2. S1-SWD-UX-05's "create" part is taught but never scored

LAYER sequence. REPEAT yes (a part taught and not assessed: dance 9 to 12 finding 2). Confidence: likely.

S1-SWD-UX-05 asks students to create software that serves intended users and contexts with human-centered design.
Day 49 states the users and runs the heuristic review; days 50 to 53 make the changes and judge them by the users
(the row's own note); but day 53's scored product lists HS-PRO-TR-20 only, and day 54 scores S1-SWD-UX-05 on a
heuristic review of a printed screen, which is the review half, not the creating half. Fix: day 53's codes add
S1-SWD-UX-05 and its rubric adds one line: the implemented refinement is judged against the intended users and setting
the team stated on day 49. This adds scoring, not teaching time, so the S1 count does not change. The standards table
then reads S1-SWD-UX-05: taught 49 (and the user lens of 50 to 53), assessed product 53; 54.

### 3. The 10-days-short path puts the S1 share over bar C1's 10 percent

LAYER sequence. REPEAT new. Confidence: firm (arithmetic on the scope's own numbers).

None of the ten fold-in days carries S1 time, so the short year keeps all of it on fewer days. Recounted at 5 of 37
teaching minutes for each of days 29 and 30, the S1 time is about 4.77 day-equivalents: 9.2 percent of 52 teaching
days (the scope says 4.7 and 9.0 percent; the right figure is 9.2), and 11.4 percent of the short path's 42. Bar C1
fails a course with more than 10 percent of teaching days outside its standards, and the brief asks the short path to
hold with nothing assessed and no owned part cut, not to break a door criterion. Fix, either (the writer picks): (a)
in the short path, run day 31 as a half lesson (branch and merge cards only, the clash card moved into day 32's
opening, since the version control part is part met anyway) and run day 5's source sort on one system, not two (the
other system's sources go into day 10's practice as retrieval), saving about one S1 day-equivalent (about 3.8 of 42,
9.0 percent), then keep day 14 as a full lesson so the path still saves ten; or (b) the lead rules that C1 is measured
on the full year only, and the Shorter path section states the short year's share (11.4 percent) and that ruling.
Also correct the C1 paragraph to 4.77 and 9.2 percent.

### 4. Day 22 still carries the `end` slot marker

LAYER sequence (process: the lead's sequence.py fix of 2026-11-26). REPEAT new. Confidence: firm.

sequence.py now accepts the course-level check on the day after a unit's last day as that unit's end-of-unit
assessment, so day 22's `assess` = end (For the lead 1) is no longer needed, and it misleads: a writer would score the
revision day, which the frame says is practice. Fix: clear day 22's `assess`; delete the sentence "this day carries
assess = end only to close the unit's slot ... (For the lead)" from its note; in the .md, Unit 2's End-of-unit bullet
says only that check 1 (days 23 and 24) stands for it and day 22's revised pieces are practice; drop For the lead 1.
Day 53 keeps `end` (a real scored product); unit 4 needs no change.

### 5. Build-day openings do not say what they retrieve

LAYER sequence. REPEAT new. Confidence: firm.

Days 33 to 39 all open with "a short trace from an earlier grade's construct", while the `retrieves` column names a
specific row (g11-evaluate-vs-spec on 33, 36 and 38, g9-design-with-structures on 34, g11-evaluate-generated-code on
35 and 39, g9-modular on 37). g11-evaluate-vs-spec is a spec and its test cases, not a construct trace, so the note and
the column disagree and a section writer cannot tell what to write. APPROACH.md field 8 asks for the unit named. Fix:
each note names its opening from its `retrieves` row, for example day 33 "a test case written against a short spec
(g11-evaluate-vs-spec)", day 34 "a list or a key-value record picked for a small problem and one item added
(g9-design-with-structures)", day 35 "a twenty-line saved sample traced for what it returns
(g11-evaluate-generated-code)", day 37 "a short program's two modules traced (g9-modular)", and so on.

### 6. Pair roles missing on four paired device days

LAYER sequence. REPEAT new. Confidence: likely.

Days 41, 42, 48 and 53 are device days worked in pairs or teams with no driver and navigator switch, while the other
build days carry it. The lens marks "one student at the keyboard all period". Fix: add the switch line ("Pairs switch
driver and navigator at the halfway signal, with a stretch break at the switch") to days 41, 42, 48 and 53; days 50
and 52 name the roles of a user round instead (two users, one note-taker, one at the device, switched in round two).

### 7. Small things a writer would copy wrong

LAYER sequence. REPEAT yes for the sitting length (minutes that do not fit the lesson). Confidence: firm.

- Days 10 and 45 say "a 45-minute sitting"; the lesson is 45 minutes with two for collecting paper, and checks 1 and
  2 are written as 40-minute sittings with about 35 task minutes. Fix: both read "a 40-minute sitting, about 35 task
  minutes", with minutes per code (day 10: HS-ALG-PS-05 about 12, S1-AIN-HR-09 about 10, HS-SOC-HU-44 about 13;
  day 45: HS-PRO-PD-15 workflow fault about 12, module trace about 10, review sign-off about 13).
- Day 54 follows unit 4's scored product directly. The brief asks a check right after a unit's end to draw that
  unit's items from earlier units' content. Fix: day 54's "new short program" is a module from unit 3's supplied
  worked team project (day 27), and its printed screen is the invented bus-route helper of unit 2; the .md's year-end
  paragraph says so.
- The no-device path of the build days (32 to 43) never says what the paper step is. Fix: one line in day 32's note,
  referenced by the others: on the no-device path, pairs write the module on the printed template and trace it by
  hand against the test-table; the record marks the HS-PRO-PD-12 revisit "part met without a device" (frame,
  Devices).
- Day 8's kept candidate ("a second responsibility case from a court record") names no case. Fix: name it in the
  unit plan, or say "picked in the unit plan" in the note.

### 8. Unit 5's two accounts may not carry the row on their own

LAYER sequence (the account pick), with a source check. REPEAT new. Confidence: likely (from memory; neither page
opened on this read).

The frame asks for a first-person account by Katherine Johnson and names NASA's biography as background only. "She
Was a Computer When Computers Wore Skirts" is, as I recall it, a NASA Langley profile with her quotations, not a
first-person account. Grace Hopper's 1968 oral history is, as I recall, mostly about the machines and languages she
worked on, with little on barriers. Both are individuals from mid-century, so neither alone shows a "diverse team"
(finding 1) or a current case (bar item 4). Fix, keeping the two people the frame settled: day 59's guide reads each
account for the team the person worked in (Hopper's Harvard computing crew; Johnson's West Area Computing group and
the flight-trajectory team), and the team's own log from unit 3 stands as the current case beside them; the unit plan
opens both pages at source (Hopper is already a browser check) and, if the Johnson feature turns out to be a profile,
swaps in a NASA-published interview in her own words, as the frame's For the lead and the grades 6 to 12 frame read
(M1) allowed.

## What is right and should not be touched

- Unit 3's order: worked project read whole (27), design worked (28), design document (29), review taught (30),
  version history on paper (31), modify a starter module (32), then seven build days with two review steps, join,
  draft, feedback, revision, presentation and an individual sitting. It meets trace before modify before make and
  gives each student a score of their own.
- The readiness design for an elective that never assumes grade 11 (retrieval for those who took it, a ten-minute
  check for those who did not), with the grade 9 rows checked for everyone on day 22 and acted on by gap on day 28.
- Every device day's four ways, save-and-shut-down minutes and safety lines; units 2 and 5 wholly unplugged.
- The senior calendar: units 1 to 4 and both checks done by week 28, unit 5's short form kept.
- The sensitivity lines on days 3, 7, 15, 18 to 21, 49 and 57 to 63, and the health disclosure steps.
- The case set: the Copyright Office's January 2025 copyrightability report and Thaler v. Perlmutter (D.C. Circuit,
  March 2025), the April 2024 ADA Title II web rule with its dates checked at source, FERPA with COPPA as a
  one-minute card, the October 2024 Section 1201 rulemaking, and the 2020 Census disclosure avoidance case with
  tribal nations' published views. These match my memory of the dates; all are marked for checking at source.
- No id claimed outside the frame's 14; PD-12 and PS-01 named as revisits only.

## Checks the gates cannot see, in brief

| Check | Result |
|---|---|
| Order inside units | Met in all five units; nothing used before it is taught |
| Assessments cover every part | Missed: findings 1 and 2 |
| Mid-unit assessment | Not needed (largest unit 21 days) |
| Response time counted once | Met (11, 25, 46, 56, 64) |
| Readiness and retrieval | Met by the frame's elective design (rule 32); grade 9 readiness on day 22 is unit 2's last day, allowed |
| Checks that do not repeat | Check 1 stands for unit 2 and samples unit 1 newly; day 54: finding 7 |
| Standards in full on days | Met, apart from S1-SWD-UX-05's scoring (finding 2) |
| Days by load | Met; unit 4 carries three ids in seven days, adequate for a program already built |
| Calendar | Met: weeks 12, 27 and 28, off week 32; ELA leans checked against calendar.csv (ELA unit 1 weeks 1 to 3) |
| Candidate cells | All settled at zero days or dropped with a reason |
| Shorter path | Present; finding 3 on the S1 share |
| Source map | Not applicable (no base text) |
| Stale notes | None in this course |

## The lens checklist (scope and sequence layer)

| Line | Result |
|---|---|
| All five concepts taught, not programming alone | Met (ALG 1 and 2, DAT and SYS 2, PRO 3 and 4, SOC 1 and 5) |
| Read before write, then modify, then make | Met (unit 3; unit 1 day 6 modify before the debate) |
| Unplugged teaches, plugged tests | Met; every unit has unplugged days |
| Notional machine and tracing | Met in the openings and the review step (once finding 5 is fixed) |
| Debugging as a method | Met in part (first wrong line, one change at a time on days 2, 40, 51); assumed from earlier grades |
| Practices inside content, pair roles that switch | Met, apart from finding 6 |
| Society with real, dated cases and more than one view | Met for units 1 and 2; unit 5: finding 8 |
| AI not one late unit, data under it | Met (unit 1 with the error counts by group) |
| Specialty only where the unit goes that far; no S2 | Met |
| Id claimed by a day that only mentions it | Not found |
| No claim that coding improves general thinking | Met |

## The writer's For the lead items

1. Settled by finding 4 (clear day 22's marker). 2. Agree on the recount; the right figure is 4.77 and 9.2 percent
(finding 3). 3 and 4. Agree; see finding 8. 5. Agree. 6. Agree: by the frame's design, not an error.

## What I could not judge

- The two unit 5 accounts and the dates in force of the ADA Title II rule: not opened on this read (finding 8 rests
  on memory).
- Whether four grade 11 rows fit in day 11's ten-minute readiness check: depends on the items the unit plan writes.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Clear day 22's `assess` = end and its note sentence; drop For the lead 1 | sequence.py now accepts check 1 as unit 2's end | days.csv, scope-and-sequence.md |
| Day 24 and day 55 HS-ALG-PS-05 items prompt accuracy, bias and harm | Bias is a part of the code | days.csv, scope-and-sequence.md |
| Day 10's HS-SOC-HU-44 part: difference, consciousness, ethics and responsibility prompts; day 24 rotates | Each part needs a prompt | days.csv |
| Day 63 and day 59 prompts for HS-SOC-CE-45: team, computational thinking and a technology, an idea expressed, then barrier and opening | Match the statement's parts | days.csv |
| Day 53 adds S1-SWD-UX-05 to its codes and one rubric line on the intended users | The "create" part gets a score | days.csv, scope-and-sequence.md standards table |
| Days 10 and 45 read as 40-minute sittings with minutes per code | Fit the 45-minute lesson | days.csv |
| Days 33 to 39 openings named from their `retrieves` row | Note and column agree | days.csv |
| Pair switch line on days 41, 42, 48, 53; user-round roles on 50 and 52 | No student at the keyboard all period | days.csv |
| Day 54's program from unit 3's worked project, its screen the unit 2 bus-route helper | Check after a unit's end draws on earlier content | days.csv, scope-and-sequence.md |
| No-device build step written once on day 32 | Paper path named | days.csv |
| S1 count corrected to 4.77, 9.2 percent; short path rebalanced by option (a) unless the lead rules (b) | Bar C1 on the short path | scope-and-sequence.md |
| Day 59's reading guide reads each account for its team; Johnson account swapped for one in her own words if the feature is a profile | Row and bar item 4 | days.csv (unit plan checks at source) |

## For Cory

None. Every finding is item-level or the lead's (finding 3 option (b) is a process ruling for the lead).

## Defect log (for the caller to file with `scripts/plan.py defect`, found_by expert)

1. computer-science-grade-12, days 10, 24, 55, 59, 63: check items miss parts of HS-ALG-PS-05, HS-SOC-HU-44,
   HS-SOC-CE-45 (finding 1).
2. computer-science-grade-12, day 53: S1-SWD-UX-05 "create" part not scored (finding 2).
3. computer-science-grade-12, Shorter path: S1 share 11.4 percent of 42 teaching days (finding 3).
4. computer-science-grade-12, day 22: stale `end` marker (finding 4).
5. computer-science-grade-12, days 33 to 39: openings do not match `retrieves` (finding 5).
6. computer-science-grade-12, days 41, 42, 48, 53: no pair roles (finding 6).
7. computer-science-grade-12, days 10, 45, 54, 32, 8: small items (finding 7).
8. computer-science-grade-12, day 59: accounts may not be first-person or team cases (finding 8).

## For the source list

Nothing new opened on this read.
