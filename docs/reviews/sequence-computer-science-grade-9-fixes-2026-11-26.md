# Fixes: scope and sequence of computer-science-grade-9, 2026-11-26

Job: docs/pipeline/briefs/sequence-fix.md through build/scope-writes/CS-FIX.md. One read so far, the Claude expert read
docs/reviews/sequence-computer-science-grade-9-2026-11-26.md; the Codex read waits for after 2026-11-30.

Counts: applied 11 of 11 expert findings and all 11 rows of the expert's Settled table; lead calls 1, 3, 4, 5, 6, 7, 8,
9, 10, 11 applied (2 and 12 needed nothing here); 1 own finding; 0 cross-grade items (no neighboring grade read has an
item that touches grade 9). Not applied: 0.

## Applied

- **Expert 1** (days.csv days 11, 12, 34, 53, 63; scope units 1 and 5, checks table; frame unit 1 and 5 cells, checks
  table): day 11's rubric carries HS-PRO-VD-16's look-fors; day 12's trace becomes trace 8 plus a 4-minute write item
  (three lines that store a new record and change one value); day 34's VD-16 item ends with one written line that
  changes a value; days 53 and 63 name one cyber and one physical measure, then a trade-off prompt each for users, data
  and devices; day 53's operating system item adds a task that has to wait; day 63's HW-29 item names its parts.
- **Expert 2** (days 6 and 21; scope units 1 and 2; frame unit 1 and 2 cells): a planted bug found with predict, run,
  compare, first wrong line on day 6 (about 6 minutes) and in a module call on day 21 (about 5); CT9 named on both.
- **Expert 3** (scope Shorter path; days 1, 2, 4, 21, 31, 32 and every host day): day 32 folds into day 31's last 10
  minutes in place of day 21; the fold-in table gains a "what the host day gives up" column and each host day's note
  says it; the 40-minute day 1 drops its retrieval trace and takes the hook to 4; days 2 and 4 move the fourth
  operation into the next day's opener.
- **Expert 4** (days 27, 28; scope unit 3; frame unit 3 cell): the random pick never repeats a slot; day 28's goal is the
  conditional claim, and the key says "no faster on average" holds only when every position is equally likely.
- **Expert 5** (days 56, 62; scope unit 6, checks table, sources; frame unit 6 cell, candidate cell, checks table, For
  the lead 4): day 56's environmental factor is the natural-environment uses that drove civilian adoption (gps.gov
  applications pages), the atmosphere kept as a technical fact; the year-end unseen case is numerical weather
  forecasting by computer (noaa.gov), replacing library catalogs.
- **Expert 6 / lead call 1** (days 32 and 58; scope units 3 and 6, For the lead): `assess` cleared on both; day 32's note
  says the claim is collected for grade 11, unscored; day 58 keeps its scored-product sentence; the Assessment
  paragraphs say the check on the day after the unit's last day stands for its end-of-unit assessment; For the lead 2
  deleted.
- **Expert 7** (days 22, 23; scope unit 2; frame unit 2 cell): one object where it fits; the rubric scores PD-12 on reuse
  and readability, not the count of kinds.
- **Expert 8** (day 63; scope Course-level checks): the PD-12 debug item has a device version and is part met without a
  device on paper; the sentence now names all three device-only ids.
- **Expert 9** (day 21; frame Day kinds bullet): kind Fluency.
- **Expert 10** (days 40, 46, 47, 48, 51, 58; scope unit 5): page days open the page; day 40 has one tool line (the queue
  page fed from the editor's generator); day 51's card game carries unit 4's transit case, so `retrieves` stays; day
  58 opens with the commonest wrong point from day 57's drafts, two minutes.
- **Expert 11** (days 1, 13, 25, 35, 43, 54; scope Earlier-grade rows; frame Course order): every student sits the
  readiness items, as retrieval for grade 8 takers, read by the teacher to place the worked examples.
- **Expert Settled, day 59** (day 59; scope unit 6; frame unit 6 cell): "a qubit's state combines 0 and 1 until it is
  measured, and a measurement gives 0 or 1; it does not try every answer at once".
- **Lead call 4, 8, 11** (frame.md): the wording above carried into the frame's Units cells, Course-level checks table,
  Course order and For the lead 4. No unit, day count or owned row moved.
- **Lead call 5** (frame Day kinds): the bullet says GLOSSARY wins, first teaching of a row or method and predict-and-watch
  are Understanding; the Fluency list adds unit 2 day 21.
- **Lead calls 6 and 9** (scope C1; frame Days bullet, For the lead 5): begun ids count inside the standards; 0 days
  outside on the full year and on the short path (grade 9 has no Specialty id). Frame For the lead 5 rewritten as
  settled.
- **Lead call 10** (scope unit 1 bridge paragraph, For the lead 1): the pick written as Pending(Cory, Desk
  q-cs-entry-1), four worked-program sheets from grade 8 unit 2 beside days 1 to 6, each with a planted-bug step. The
  frame's For the lead 6 says the pick waits on that Desk card in plain words (frame.py fails a Pending marker that
  names no file).
- **Lead call 7**: one defect row per finding logged with `plan.py defect` (14 rows: 11 findings, the day 59 wording and the frame wording as expert, 1 own as writer).
- **Own** (day 63; scope checks table; frame checks table): the HS-DAT-DC-22 item asked only for a rule; it now has a
  prompt for one field's name, type and allowed values and one for a rule between fields (brief rule 2, each part of
  each code).

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reuse |
|---|---|
| Fold a begun-id day (32) rather than the only modify day of an owned programming row | A short path never removes a construct's modify day |
| Every fold-in names what its host day gives up, in the host day's note and the table | All computer science short paths |
| Every student sits an elective's readiness items; for takers they are the year-before retrieval | Grades 6 to 12 |
| A product asks for "procedures, libraries or objects" as the standard's "or"; scored on reuse and readability | HS-PRO-PD-12 wherever it is scored |
| An environmental factor for HS-SOC-HI-38 is a nontechnical force (uses in the natural environment), not a physical constraint | Every history case |
| Page days (toy pages, simulated device) open the page, not the editor file | All device days that run a page |
| A Pending marker in frame.md must name a file; a Desk wait there is written in plain words | All frames |

## For the structure pass

- None needed from this course. calendar.csv is unchanged by this pass (no unit, check or day count moved).
- Optional, lead's call: frame.py could accept `Pending(Cory, Desk <id>)` as a target, so frames and scopes use one
  marker for a Desk wait.

## For Cory

- Desk q-cs-entry-1 (lead call 10, already queued): grade 9 entry for a student with no programming at all. The pick is
  in the scope's unit 1 bridge paragraph.

## Gates

- `python -X utf8 scripts/sequence.py check computer-science-grade-9`: 0 failures.
- `python -X utf8 scripts/frame.py check computer-science-grade-9`: 0 failures; `frame.py check` (all frames): 0 FAIL lines.
- `python -X utf8 scripts/frame.py calendar`: no failure line for this course (grades 9 to 12 have no stagger rule but
  the finals week; no check moved).
- `python -X utf8 scripts/gate.py --course computer-science-grade-9`: 0 failing findings against the baseline, 1 new note
  line (the sequence note). index-reports exited non-zero before and after the edits; it is a shared check, not this
  course's.
