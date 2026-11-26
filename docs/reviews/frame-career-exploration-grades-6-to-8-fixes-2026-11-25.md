# Frame fixes: Career Exploration, grades 6 to 8 (2026-11-25)

Course `career-exploration-grades-6-to-8` (subject cte), the career education pilot frame. One fix pass of COURSE-RUN
stage 3 over two reads: the fresh expert (docs/reviews/frame-career-exploration-grades-6-to-8-2026-11-25.md, E1 to
E14) and the second model (docs/reviews/frame-career-exploration-grades-6-to-8-codex-2026-11-25.md, C1 to C12).

Files changed: docs/courses/career-exploration-grades-6-to-8/frame.md; data/progressions/cte.csv (three notes, LF
endings kept); docs/courses/career-education/APPROACH.md (the skill day row, one UK spelling); frames.csv,
calendar.csv and CALENDAR.md through sync (no day moved).

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 66 courses; calendar.csv 962 rows |
| `python -X utf8 scripts/frame.py check career-exploration-grades-6-to-8` | 0 failures; 7 units, 96 days (92 in units, 4 for checks and respond days) |
| `python -X utf8 scripts/progression.py check cte` | 228 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 70 files, 0 failures |

Stagger (CALENDAR.md rule 3), checked by hand against data/plans/calendar.csv because frame.py skips the `6-8` grade
(E5): check 1 is school days 77 and 79 (week 16). No grade 8 core check day falls on either (science grade 8's
respond day is day 76); none in grade 7; in grade 6 math's mid-year check is day 80, not 77 or 79. Check 2 is school
days 159 and 160 in week 32, the finals week, beside every core year-end check (allowed). No clash with a core
check day. Clashes with other after-core subjects were not checked (those frames are not written; the lead's calendar
pass).

## Findings

| Read | # | Applied or rejected | What changed, or why not |
|---|---|---|---|
| Expert | 1 | Applied | Unit 5 Practices: "8; 12 returns; 2 practiced, not judged (its look-fors are first taught in unit 7)"; unit 6: "4, 9 and 11 return; 2 practiced, not judged (unit 7)" |
| Expert | 2 | Applied, with a different split | Added "Shorter path, unit by unit": seven rows naming each short session and each fold. Short units 9, 9, 9, 7, 7, 11, 8 (60). The expert's unit 3 at 8 is not possible (C2 agrees: 3 explore plus field tasks plus 3 closing). To reach 60 the fold rule changed: a two-day field task (the stand, the production line) runs in one session, its planning half on the explore day; APPROACH.md protects one field task day a unit, and lesson 21 protects only feedback and revision days. The protected floor is 55, so unit 1 keeps exactly 5 teaching sessions: the path has no slack, said in the Days bullet |
| Expert | 3 | Applied (named days); the day move rejected | Unit 7's ten days named in order, with day 2 holding the high school move and the course-choice draft (ALL2.A4) and the next-term school plan drafted on the field task day for plan-day feedback. No day moved from unit 2: its 14 days are all accounted (3 clusters at 2 explore plus 4 field task days, the working-for-yourself day, 3 closing), so the move would cut a field task |
| Expert | 4 | Applied as practiced; ownership to Cory | Unit 3: one production line hazard and its control, from Talking Safety; unit 7 skill day 2: a first job's rights (safe workplace, hours and task limits under 16 and 18, who to ask), from OSHA's young workers pages, practiced, not owned. Row ownership is For the lead item 6 (Cory) |
| Expert | 5 | Left for the lead | scripts/frame.py is outside this job. Frame checks paragraph now states the grade 8, grade 7 and grade 6 results checked by hand; For the lead item 1 |
| Expert | 6 | Applied | How-I-learn day is unit 5 day 2 (course day 60, school day 100); plan day course day 66, school day 110, two school weeks; Why cell reworded |
| Expert | 7 | Applied | NSTA cited "for hands-on hazards in general"; added University of Maryland Extension FS-1077 for the seed tray (opened by C10); the "not opened" sentence replaced with "Opened 2026-11-25 by the two frame reads"; unit 4 safety sentence names bagged medium, adult moistening, gloves, hand washing (C10) |
| Expert | 8 | Applied | Check 1: Network Systems and Cybersecurity; check 2: Health Data and Administration, Early Childhood Development as the alternate, both new cards and figures with the same criteria |
| Expert | 9 | Applied | g7-viz-choices is a bridge (lesson 32) in the Readiness bullet and the Cross-subject row; math 7 last uses named from data/plans/math-grade-7/days.csv (unit rate unit 4 days 47 to 68; percent to day 153 and the year-end check; compare populations unit 8 days 139 to 157) |
| Expert | 10 | Applied | Unit 7 teacher note carries the disability line; the same line added to the g8-cd4-2-job-search-steps teacher note so the scope copies it (C's note that it is a clarification is accepted; the cost is one sentence) |
| Expert | 11 | Applied in part; rest to the lead | Frame item 11 rewritten as a Pending(...) note; APPROACH.md skill day row now "Understanding on first teaching, Fluency after". ADOPTION-BAR-SUBJECTS.md is not this job's file: replacement text in For the lead item 4 |
| Expert | 12 | Applied in the frame; brief to the lead | Week 32 kept; the brief's replacement text is For the lead item 2 |
| Expert | 13 | Applied | Both check cells: "assessed two course days earlier, with its respond day between" |
| Expert | 14 | Applied | Growing guide: "a state extension service's planting calendar"; budget line: "a town's adopted budget on its own public site"; unit 6 names the federal table (cpsaat11) and its two data notes, dated 2026-11-25 |
| Codex | 1 | Applied | Scored evidence gains "Practice evidence": portfolio choice never waives a practice; a short attachment per newly taught practice the chosen piece does not show, named unit by unit, with feedback and revision on the plan day. Settled for C over the expert's "keep one piece": APPROACH.md judges each practice taught on a piece, and one chosen piece cannot carry practices taught on other pieces. No day added |
| Codex | 2 | Applied | As E2. C's minima (units 2, 6, 7 at 10, 11, 8) assumed two-day field tasks stay two days; with the one-session rule units 2 and 3 run at 9; unit 6 at 11 and unit 7 at 8 as C asks |
| Codex | 3 | Applied; access to Cory | The practices as a state reproduces them include operating digital tools. Devices bullet: practice 5 is the one owned code needing technology; each pair gets a three-minute turn at one shared device with an offline spreadsheet plus a privacy step; paper path does the table in full; a student with no device meets the digital part as begun, finished by g10-prac-5-digital-data. Row g8-prac-5-digital-data notes changed to match. For the lead item 7 (Cory) |
| Codex | 4 | Applied | As E6 |
| Codex | 5 | Applied | As E1 (the expert's wording, shorter) |
| Codex | 6 | Applied | Packet days bullet, Sensitive ground, Sensitivity reads and unit 7's last column: packets follow the school's leave-out choices with a same-cluster alternative, a sensitive packet gets its teacher note and sensitivity read, health's disclosure steps where section 6 names the topic, paper tasks only, exploration only |
| Codex | 7 | Applied | As E9, with the repair step C asks for |
| Codex | 8 | Applied | As E8 |
| Codex | 9 | Left for the lead | As E5 |
| Codex | 10 | Applied | As E7. C's point that the "not opened" line was historical is rejected: the frame is a living doc and now states the current status |
| Codex | 11 | Applied | The checks paragraph opens with C's wording (mid-year avoids core weeks; year-end uses week 32 under the finals-week rule) |
| Codex | 12 | Applied in part; rest to the lead | APPROACH.md row, g8-cd2-2-decision-steps notes ("which job the unit's field task compares first, or which sub-cluster to take for the self-directed job study") and both check cells fixed; ADOPTION-BAR row to the lead (item 4) |

Counts: 26 findings; 22 applied in full or in the frame, 2 applied in part with the rest left for the lead (E11,
C12), 2 left for the lead as script changes (E5, C9); one sub-proposal rejected (E3's day move) and one sub-claim
rejected (C10's "historical" line). Also fixed: "labour" to "labor" in APPROACH.md; For the lead cut from 12 items to
8, each current.

## Pattern notes for Career Pathways

- Build the short path from the floor up: count the sessions that never fold (closing days, one session per field
  task, one explore session per cluster, packet and skill days) before giving any unit a number, and publish the
  unit-by-unit fold table.
- Check every "returns" in the Practices column against the unit that first teaches the practice.
- One chosen portfolio piece plus a named evidence attachment for each practice it does not show.
- Practice 5 needs a device turn and a privacy step; say how a student with no device meets it.
- Leans on optional courses (computer science, library, SEL) are bridges the unit teaches; core leans give the core
  course's unit and days. Every Exploration row is two grades back for Pathways, so each gets a readiness check.
- Packets and student choices follow the leave-out and disclosure rules wherever they land.
- Name the kind of free source for every anchor, and state "as of" notes for federal tables.
- Unseen check items must be unseen for every student, packets included.

## Left for the lead

- scripts/frame.py: read a one-year range-grade course at its `rows` grade in `calendar_rows` (E5, C9).
- frame-write.md: the week 32 sentence and the Practices column sentence (frame For the lead items 2 and 3).
- ADOPTION-BAR-SUBJECTS.md career education row: replacement text in frame For the lead item 4; log decisions in
  DESK-ANSWERS.md.
- The after-core calendar pass and the reconcile with the CS 8, library 6 to 8 and SEL 6 to 8 frames (item 5).

## For Cory

- Scope: should a row own a first job's safety and rights (now practiced, not owned, in units 3 and 7)? Pick: no.
- Scope and access: practice 5's three-minute shared-device turn per pair, with a device-free student meeting it as
  begun. Pick: keep.
- Scope, only if the scope read finds the 64-session path overloaded: fewer clusters at depth or more sessions.
  Pick: keep and test.
