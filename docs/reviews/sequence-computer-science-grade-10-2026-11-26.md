# Expert read: scope and sequence of Computer Science, Grade 10 (2026-11-26)

Course `computer-science-grade-10`. Cold read by the curriculum expert (PRODUCTION-PATH step 3), per
docs/pipeline/briefs/sequence-read.md and build/scope-writes/CS-READ.md. I did not write the scope. This report is
the only file edited.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/computer-science.md; docs/ADOPTION-BAR-SUBJECTS.md section
  "5. Computer science" (items 1 to 9, "Fails if", "Scope and sequence states"); docs/courses/computer-science/APPROACH.md
  (kinds of day, how a day opens, daily evidence, plan fields); STANDARD.md through the ownership and device lines the
  frame cites.
- build/scope-writes/CS-BRIEF.md (how the writer applied sequence-write.md).
- docs/courses/computer-science-grade-10/scope-and-sequence.md and data/plans/computer-science-grade-10/days.csv, all
  64 rows in full.
- docs/courses/computer-science-grade-10/frame.md in full (brief, Seams, Models, Units, Course-level checks,
  Cross-subject, For the lead).
- data/progressions/computer-science.csv: every g10 row, plus g9-operating-systems, g9-det-vs-prob and
  g8-network-failure.
- docs/courses/CALENDAR.md (rules 1, 3, 4 and the grade 10 row) and the grade 10 rows of data/plans/calendar.csv.
- The 12 owned ids' statements and boundary statements, read in the CSTA 2026 PDF in the source store
  (S:\CurioClass-sources\computer-science\csta-2026-11-21), text extracted to the scratchpad, never copied here.
- Gates first: `plan.py check` 0 failures for this course (sequence and frame); `frame.py calendar` 0 failures;
  `stale.py check` printed no line naming this course; `gate.py --course computer-science-grade-10` 0 failing
  findings against its baseline.
- No earlier computer science sequence read exists in docs/reviews/, so every REPEAT tag below is "new" unless it
  names an arts read of the same day.

Outside sources opened: the FBI Internet Crime Complaint Center announcement of April 11, 2024
(ic3.gov/PSA/2024/PSA240411, opened: "Cyber Criminals Target Victims Using Social Engineering Techniques", which
does describe criminals posing as employees to get help desk staff to change logins, so day 28's card is accurate).
The Office of Educational Technology report page (tech.ed.gov) returned 403: browser check.

## Verdict

The scope is sound: all five concept areas are taught with AI inside the algorithms unit, trace comes before modify
before make on the main programming rows, every device day carries its four paths, every unit and check falls in
the frame's weeks, and the society cases are real, dated and guarded. The biggest risk is that several assessment
days do not ask about every part of the ids they score, worst on day 10, where HS-PRO-PD-13's development-tool part
(the debugger) is taught on day 8 but never assessed. The one change that matters most is to write each Check day's
goal with a prompt per part (findings 1 and 2); close behind is the shorter path, which folds away the only practice
of three assessed performances and unit 1's only modify day (finding 3).

14 findings: 2 serious, 4 moderate, 8 minor.

## Findings, most serious first

### 1. Day 10 never assesses the development-tool part of HS-PRO-PD-13 (serious)

LAYER sequence, frame. REPEAT new.

- **What is wrong.** HS-PRO-PD-13's boundary covers documentation, libraries, simple APIs and features of the
  editor (debuggers, highlighting). Day 8 teaches the step-through debugger and highlighting; day 10, the only scored
  record of the id (it is carried unscored at both checks), asks only for a library call written from a new
  documentation page with its credit comment. The frame's end-of-unit text has the same gap.
- **Why it matters.** The record says "met" for a part no student was asked to show; the debugger is also the
  lens's "debugging as a method" and the place grade 11 assumes it.
- **Fix.** Day 10 goal: add "then use the step-through debugger to find the line where a given call returns the
  wrong value, and say what the highlighting showed". Note: the paper path is a printed step-through trace with the
  highlighted line, recorded part met without a device. For the lead: the frame's unit 1 end-of-unit text adds the
  same item.

### 2. Other assessment days do not prompt every part of their ids (serious)

LAYER sequence. REPEAT new.

- **What is wrong.** Against the boundary statements:
  - Day 40, HS-DAT-DC-23: the goal names "clean a new short messy list", but the id has four parts (inconsistencies,
    errors, structuring, saying where a pattern rule fits); structuring and the pattern rule are not named.
    HS-DAT-DC-24: "judge two verification approaches" with no named type, value and range error in the table.
  - Day 29, HS-SYS-NT-35: "compare a new local network with the internet" asks neither for the layers nor for
    routers, both in the boundary and taught on day 25. HS-SYS-SE-32 covers breaches and social engineering attacks;
    the day has one breach case only.
  - Day 51, HS-ALG-IM-09: look-fors "for each human-centered step" do not include anticipating the social and
    ethical effects of the design, which the boundary names and day 45 teaches.
  - Day 19, HS-ALG-ML-06: "justify an AI type" without naming the three things the justification weighs (data size
    and type, whether a person can follow it, the outcome wanted), all taught on day 18.
- **Why it matters.** A teacher writing the sitting from the goal will leave the parts out, and the brief requires
  a prompt per part of each code a check lists.
- **Fix.** Day 40 goal: "clean a new short messy list with the named functions (case and spaces, a misspelling, a
  duplicate, one combined field split or one date format made the same), saying each step and one place a pattern
  rule could find every case; judge two verification approaches for a new table holding a wrong type, a value not
  allowed and a value out of range, on the errors each would miss". Day 29 goal: add "naming the layers a message
  passes through and the routers' role" and "classify a new social engineering case the same way". Day 51 goal: add
  "and one social or ethical effect of the chosen option on a group of users" to the look-fors. Day 19 goal: "...in
  two sentences, weighing the data's size and type, whether a person can follow how it decides and the outcome
  wanted".

### 3. The shorter path folds away sole practice of assessed work (moderate)

LAYER sequence. REPEAT yes (the arts reads of the same day flagged fold-ins that thin an assessed skill).

- **What is wrong.** Nothing assessed or owned is cut on paper, but three fold-ins remove the only practice of a
  scored performance: day 56 (the written evaluation day 62 scores), day 60 (the "decision that mattered most" day 61
  scores) and day 18 (the justification day 19 scores, which is at least partly practiced again on day 17). Day 4
  is unit 1's only modify day, so folding it breaks trace before modify before make on g10-analyze-code. Meanwhile
  three contributing-only days stay whole (day 5, HS-PRO-RD-18 first look; day 57, HS-SOC-HI-39 first look; day 14
  has a full printed-counts path).
- **Why it matters.** In a short year the students lose rehearsal exactly before the sittings, and unit 1 goes
  straight from trace to make.
- **Fix.** Replace fold-ins 4, 56 and 60 with: 5 into 4 (the saved sample read in the last 15 minutes of the modify
  lesson), 57 into 56 (the timeline entry as its first 15 minutes), 14 into 13 (the counts from the printed table,
  its no-device path). Keep the other seven. Total stays 450 minutes, 10 days.

### 4. Day 28 still carries a gate-only `assess = end` (moderate)

LAYER process. REPEAT new.

- **What is wrong.** sequence.py now accepts a course-level check on the day after a unit's last day as that unit's
  end-of-unit assessment (lead fix 2026-11-26). Day 28 is a teaching day marked `end` only so the old gate saw a slot.
- **Why it matters.** A teacher or a report reading the CSV sees an end mark on a day where nothing is scored.
- **Fix.** Day 28 `assess` blank; drop its first note sentence ("assess = end marks the gate slot only ... (For the
  lead 1)"). In the .md, unit 3's Assessment sentence becomes "the mid-year check (days 29 and 30) is this unit's
  end-of-unit assessment and day 31 its respond day"; delete For the lead 1 and renumber.

### 5. The library row goes from reading to making with no modify day (moderate)

LAYER sequence, frame. REPEAT new.

- **What is wrong.** g10-apis-docs: day 6 reads documentation (Understanding), day 7 writes a new call to add a
  feature (Application), day 9 makes again. APPROACH's hard rule (no make before a trace or modify day on the same
  construct) is met by day 6, but its order "understanding before modify before make" skips modify for the one
  construct students have never used: a call written from documentation. Day 4's modify is on the anchor, not the
  library.
- **Why it matters.** Writing a call from documentation is the step novices fail most (argument order, return value
  unused); one modify lesson lets the error appear on a working program first.
- **Fix.** Day 7 kind Fluency, goal: "Modify: change the arguments of two supplied library calls from the
  documentation (the dice's sides, the deck's size), predict, run and compare, then add one call the page describes".
  Day 9 stays the make. For the lead: the frame's Fluency list adds unit 1 lesson 7. Confidence: a judgment call.

### 6. Day kinds and device days that differ from the frame are not all named (moderate)

LAYER sequence. REPEAT new.

- **What is wrong.** The frame's device list for unit 2 is lesson 3 only (day 14); day 15 carries the full device
  boilerplate. Days 10 and 40 are device Check days, which the frame's text implies ("write and run", "clean with the
  named functions") but its device list does not name. Only the day 35 kind change is in For the lead.
- **Why it matters.** The frame's "about half the year away from a device" count and the tool-ask timing rest on the
  device list.
- **Fix.** Day 15 note: "Paper or device" as day 16 (the buggy search fixed on a printed trace-table is the
  default), or add it to For the lead as a device day. For the lead adds: "days 10 and 40 are device sittings with a
  paper version, part met without a device for PD-13 and DC-23".

### 7. The year-end row of the checks table has the wrong school days (minor)

LAYER sequence. REPEAT new.

- **What is wrong.** The .md table says year-end "31 (152) and 32 (154); respond week 32 (157)". days.csv and the
  formula give day 62 = 154, day 63 = 157, day 64 = 159 (152 is day 61). The weeks are right.
- **Fix.** "31 (154) and 32 (157); respond week 32 (159)".

### 8. Two grade 9 review threads are said to get readiness but never do (minor)

LAYER sequence. REPEAT new.

- **What is wrong.** The .md lists g9-operating-systems and g9-det-vs-prob among rows whose items are "a ten-minute
  readiness check before each unit" for students who did not take grade 9. No readiness day carries them (days 1 and
  20), yet day 22 draws the operating system layer (a software part HS-SYS-NT-34 names) and day 7 calls the dice roll
  probabilistic.
- **Fix.** Day 22 note adds "a one-card worked example of the operating system layer first for students who did not
  take grade 9"; day 7 note adds "one line on what probabilistic means for students who did not take grade 9". The
  .md sentence lists these two as "review, with a worked example inside the day", not readiness.

### 9. Seventeen days open with an unnamed retrieval trace (minor)

LAYER sequence. REPEAT new.

- **What is wrong.** Days 5, 8, 9, 14, 15, 22, 24, 34, 35, 44, 45, 48, 49, 50, 56, 58 and 60 say only "Opens with a
  three-minute retrieval trace." APPROACH says the day row gives the opening, and field 8 names the earlier unit.
- **Fix.** Name each (a suggestion; the writer may pick others): 5 day 2's call; 8 day 7's call; 9 the anchor's
  while loop; 14 day 13's step count; 15 day 5's test-table; 22 unit 1 call with a list; 24 day 23's diagram; 34 day
  33's trim; 35 a unit 2 test case; 44 a unit 4 range check; 45 a unit 3 cause sort; 48 to 50 a unit 1 or 2 trace
  each; 56 a unit 3 impact sort; 58 a unit 2 AI task card; 60 a unit 4 verification choice.

### 10. The scope and sequence does not state each unit's concept area (minor)

LAYER sequence. REPEAT new.

- **What is wrong.** Bar part 5, "Scope and sequence states: the concept areas per unit". The frame has them; the
  .md unit paragraphs do not.
- **Fix.** Add one line to each unit: unit 1 programming; unit 2 algorithms and design (AI inside it); unit 3
  systems and security; unit 4 data and analysis; unit 5 algorithms and design (impacts), with computing and society
  (careers); unit 6 computing and society.

### 11. Day 33 uses the cleaning functions before any predict step (minor)

LAYER sequence. REPEAT new.

- **What is wrong.** Day 33 (Understanding, device) has students "make capital letters and spaces the same with a
  tool". APPROACH's Understanding day is a given program traced and predicted before it is run.
- **Fix.** Goal: "Device: predict what a supplied trim and change-case call does to five rows on a before-and-after
  table, run it, then apply both to the volunteer list".

### 12. Two society sources need a current-date check (minor)

LAYER sequence. REPEAT new.

- **What is wrong.** Day 54's teacher line cites the Office of Educational Technology's May 2023 report; the page
  refused an automated read (browser check), and from memory the office was closed in 2025, so the report may now
  live only in an archive. Day 57's FTC rule page: from memory the children's online privacy rule was amended in 2025,
  so the "dated source" should be the current rule page with its amendment date. From memory too, day 44 could note
  the 2024 Justice Department rule on web accessibility for state and local governments as a current case of a law
  setting requirements.
- **Fix.** Day 54 note: "Teacher line: ... (May 2023), with where the copy is kept and the date checked (browser
  check)". Day 57 note: "Teacher line: FTC Children's Online Privacy Protection Rule page, with the date of its latest
  amendment". Day 44: optional. Confidence: likely (from memory, to be confirmed in the browser).

### 13. Day 30's note points at the wrong days (minor)

LAYER sequence. REPEAT new.

- **Fix.** "Task forms differ from days 19 and 20" becomes "Task forms differ from days 10 and 19" (the two sittings
  whose ids day 30 samples; day 20 is a respond day).

### 14. Respond days' codes do not match what they reteach (minor)

LAYER sequence. REPEAT new.

- **What is wrong.** Day 31 reteaches the mid-year sample (HS-PRO-RD-17, HS-ALG-PS-03, HS-ALG-ML-06, its skills
  list them) but its codes list only the unit 3 ids; day 64 reteaches the year-end sample but lists only HS-SOC-HU-43
  and HS-SOC-ET-41.
- **Fix.** Day 31 codes add HS-PRO-RD-17; HS-ALG-PS-03; HS-ALG-ML-06. Day 64 codes add HS-PRO-RD-17; HS-ALG-PS-03;
  HS-DAT-DC-24; HS-ALG-IM-09.

## Checked and met

- Order inside units: each day builds on the ones before; nothing used before taught (memory use on day 13 before day
  16; the test-table's missing and empty cases on day 5 before day 15; client and server on day 25 read through unit
  1's calls); each arc reaches its compelling question.
- Owned ids: all 12 sit on teaching days and an assessment; no id claimed outside the frame's owned rows; the five
  contributing ids are marked first looks or contributing uses, never claims; no Specialty id.
- Calendar: school_day follows the stated formula on all 64 rows; every unit and check falls in the frame's weeks
  (units 1 to 6 in weeks 1 to 6, 6 to 10, 11 to 14, 16 to 21, 21 to 27, 27 to 31; mid-year week 15, respond week 16;
  year-end weeks 31 and 32, finals week 32); calendar.csv agrees. No same-year lean exists.
- Readiness: unit 1's check in day 1's last ten minutes; every other one on the previous unit's respond day or the
  mid-year respond day; none on a unit's first day. Grade 8 rows get readiness for every student; grade 9 rows,
  the year before, are retrieval for takers and readiness for non-takers, as frame rule 32 requires for an elective.
- Checks that do not repeat: each check stands for the unit before it (unit 3, unit 6 part 2), and the .md says so;
  the sampling lessons use new task forms.
- No unit over 25 days, so no mid-unit assessment; response time counted once per assessment.
- Device days carry four paths, the pair switch, save-and-close minutes and both safety lines; every security day
  carries the case-card-only line; every flagged case names its flag and health's steps.
- Candidate cells: all six settled, kept at zero added days.
- No base text, so no source map; days leaning on unloaded sources: none, as the .md says.

## Lens checklist (frame and scope and sequence layer)

| Line | Met? |
|---|---|
| All five concept areas taught, not programming alone | Met |
| AI inside the concepts, not one late unit | Met (unit 2; data and society cases in units 4 and 6) |
| Read before write, then modify, then make | Met on g10-analyze-code and g10-evaluate-algorithms; missed on g10-apis-docs (finding 5) |
| Unplugged work names its concept; every unit has an unplugged path | Met |
| Notional machine taught | Met (day 2, "exactly what is written, in order") |
| Debugging taught as a method | Met in teaching (days 8, 15); not assessed (finding 1) |
| Practices inside content (pairs, design, ethics) | Met |
| Society with real, dated cases and two views | Met; two dates to confirm (finding 12) |
| Id at its boundary depth, not below or past | Met; parts missing from prompts (finding 2) |
| Non-specialist teacher supported | Met at this layer (stuck sheet, symbol key, error-letter key); judged at unit plan |

## Settled by the expert

| Item | Settled |
|---|---|
| Day 35's kind | Understanding is right (splitting a field and one date format are first taught there); the frame's Fluency bullet drops unit 4 lesson 4 (the writer's For the lead 2 stands) |
| Memory use moved from day 16 to day 13 | Kept: it is taught before it is practiced |
| Day 5's test-table holds a missing-item and an empty-list case | Kept: day 15 becomes practice |
| Second and fourth school day of each week | Kept |
| Grade 9 rows checked as readiness although grade 9 is the year before | Kept: grade 9 is an elective (frame rule 32) |
| Day 28's end mark | Removed (finding 4), per the lead's 2026-11-26 gate fix |
| Shorter path fold-ins | Replace 4, 56, 60 with 5, 57, 14 (finding 3) |
| Day 7 as a modify lesson | Recommended (finding 5), a judgment call; the writer may keep day 7 as make if day 9 becomes the modify, but one modify day on library calls must come before a make |
| Retrieval openers named per day | The list in finding 9 is a suggestion, not binding |

## For Cory

None. Every finding is item level.

## For the source list

- FBI Internet Crime Complaint Center, PSA I-041124-PSA, April 11, 2024 (ic3.gov/PSA/2024/PSA240411): opens to an
  automated read; confirms the employee-impersonation help desk case.
- Office of Educational Technology, "Artificial Intelligence and the Future of Teaching and Learning"
  (tech.ed.gov/ai-future-of-teaching-and-learning/): 403 to an automated read, browser check.
