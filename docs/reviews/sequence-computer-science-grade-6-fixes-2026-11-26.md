# Fixes: scope and sequence of computer-science-grade-6, 2026-11-26

Job: docs/pipeline/briefs/sequence-fix.md through build/scope-writes/CS-FIX.md. One read so far: the Claude expert read
docs/reviews/sequence-computer-science-grade-6-2026-11-26.md (12 findings and its "Settled by the expert" table). The
Codex read waits for Codex's usage reset and gets its own small fix pass.

Counts: applied 12 of 12 expert findings (all 11 settled rows), 0 not applied; lead calls 1, 2, 4, 5, 7, 8, 11 and 12
applied where they touch this course (3, 6, 9 and 10 needed nothing here); cross-grade items: none that touch grade 6
(the other computer science reads cite grade 6 only for REPEAT tags; grade 7's leave-out readiness on its day 33 is
grade 7's own); own findings: 2.

## Applied

- **Expert 1** (days.csv, scope-and-sequence.md, frame.md): day 27's goal adds accuracy (the whole-degree log rounds
  20.4 to 20; the once-a-day log misses the afternoon high); day 33 adds a fourth question the table's granularity or
  missing header cannot answer, and its codes add MS-DAT-DC-21 and MS-DAT-DC-22; day 37's DC-21 item asks for one
  effect on accuracy. The frame's unit 3 sessions 1 and 7 and its mid-year check cell say the same.
- **Expert 2** (scope-and-sequence.md): the shorter path folds day 29 into day 28's last 10 minutes with the device
  step kept (printed panel only where there is no device). Ten folds and 54 days stay.
- **Expert 3** (days.csv, scope-and-sequence.md, frame.md): days 14, 38 and 63 procedure items add "name your procedure
  and say one way the new version is clearer or easier to reuse"; the frame's unit 1 assessment cell and both check
  cells match.
- **Expert 4** (days.csv, scope-and-sequence.md, frame.md): day 54 compares the systems with one impact of each kind
  (societal, environmental, ethical, the frame's three examples); day 55 and the day 62 item ask impacts of two
  different kinds named by kind. Frame unit 6 sessions 1 and 2, the year-end check cell and the grade 7 handoff row
  match.
- **Expert 5 / lead call 1** (days.csv, scope-and-sequence.md): `assess` cleared on days 36 and 61; the gate-slot
  parentheses dropped from both notes; the unit 3 and unit 6 end-of-unit bullets now say the check on the next day
  stands for the assessment; old For the lead 1 deleted.
- **Expert 6** (scope-and-sequence.md, days.csv, frame.md): a unit 4 leave-out bullet and a day 63 note sentence (its
  two unit 4 items become a ten-line trace, MS-PRO-VD-16, and a sort-and-summarize item on a printed table,
  MS-DAT-DC-23; days 40 to 46 stay in the calendar). Frame Swap or leave out and the year-end check cell match.
- **Expert 7** (days.csv, scope-and-sequence.md, frame.md): days 11 to 13 run teams of four on one device, driver,
  navigator, tester and recorder rotating every eight minutes, the recorder writing on paper; day 11's "which meets
  the id in full" removed; the part-met line for PD-15's shared digital tool part now on days 11 to 14. Frame Devices
  bullet and unit 1 sessions 11 to 13 name the team arrangement.
- **Expert 8** (days.csv, scope-and-sequence.md, frame.md): day 37 timed about 6, 6, 16 and 12 minutes, the DC-23
  table at most 15 rows; day 62 about 10 minutes an id. Frame check cells carry the same.
- **Expert 9** (days.csv, scope-and-sequence.md): day 49 kind Understanding; kinds now 30 Understanding, 3 Fluency, 17
  Application, 8 Check, 6 Respond.
- **Expert 10 / lead call 4** (frame.md): week ranges synced to the pins: unit 3 weeks 13 to 17 with the mid-year check
  in week 18, its sort and summarize sessions in weeks 15 and 16; unit 4 weeks 19 to 23; unit 5 weeks 23 to 26;
  Cross-subject rows unit 3 sessions 5 to 7 weeks 15 and 16, unit 5 sessions 1 to 3 weeks 23 and 24. The .md's old
  For the lead 3 is dropped (applied here).
- **Expert 11 / lead calls 4 and 8** (days.csv, frame.md): day 58 and the frame's unit 6 picks give the Vaughan wording
  the NASA biography supports (West Area Computing from 1949, first African-American manager, an expert programmer in
  the language of its electronic computers), dated 2026-11-26; day 29's photo place is invented or public; the IMLS
  card names its survey year; the ssa.gov line is marked Pending(browser check, 403).
- **Expert 12** (days.csv, scope-and-sequence.md): day 51 retrieves g6-verify-algorithm (choose the inputs that would
  test a resend); day 28 retrieves g5-collect-tools (name each column's unit); the retrieval table lists day 28.
- **Lead call 2** (scope-and-sequence.md): For the lead now holds one item, "No source-map.csv: waits on L149".
- **Lead call 5** (frame.md): the Day kinds bullet names a predict-and-watch session as Understanding (unit 5 session
  3), as GLOSSARY has it.
- **Lead call 7**: 14 defect rows logged (`plan.py defect --status=fixed --made-at=scope`), one per finding, plus the
  lead call 5 wording row.
- **Own 1** (frame.md): Cross-subject math row g6-model-algorithm said unit 2 sessions 1 to 4 run weeks 8 to 10; with
  the pins days 16 to 19 sit on school days 38 to 45, weeks 8 and 9. Fixed.
- **Own 2** (scope-and-sequence.md): the year-on-one-page pair sentence said pairs switch "on every device day"; it now
  says pair device days, with the team days and day 49's kind stated beside it.

Rule 2 lists re-run: every assumed row is a grade 5 row retrieved inside its first day (table unchanged but for day 28);
each check's sampled codes match the days' codes; MS-PRO-PD-15 the one owned code not sampled, with its reason; end
days now only Check days 14, 25, 45 and 52, with the checks on 37 and 62 standing for units 3 and 6; no company names.

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reuse |
|---|---|
| A team day of four on one device names four roles (driver, navigator, tester, recorder) rotating every eight minutes; on paper the recorder writes | Any grade's team program days |
| A predict-and-watch device day that makes nothing is Understanding | Toy network or demo days in every computer science grade |
| A check that scores four ids in 40 minutes states minutes per id and caps a table task's rows | Every computer science course-level check lesson |
| A leave-out unit names the swap items on the check that samples it, and its days stay in the calendar | Any grade with a leave-out unit sampled later |
| An id with a list of kinds (impacts, parts) asks two different kinds named by kind in a timed item, all kinds on the teaching day | All "one of" reductions |

## For the structure pass

- docs/APPROACH-SOURCES.md (frame For the lead 7, the lead's list): the NASA Dorothy Vaughan entry adds "opened
  2026-11-26; supports West Area Computing from 1949, first African-American manager, segregated facilities to 1958,
  expert FORTRAN programmer; not 'first electronic computers'"; the ssa.gov history entry adds "403 to automated reads,
  browser check".
- Browser check for the lead (Claude in Chrome): ssa.gov/history (the punched-card records of the 1930s and the move to
  electronic computers in the 1950s, from memory in the read).
- data/plans/calendar.csv: no change from this pass (no school_day moved).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check computer-science-grade-6`: 0 failures.
- `python -X utf8 scripts/frame.py check` (all courses): 0 failures; this course 6 units, 64 days.
- `python -X utf8 scripts/frame.py calendar`: no break for this course (grade 6 computer science check weeks 18, 31,
  32); no school_day changed, so no frame change of mine moves the calendar.
- `python -X utf8 scripts/gate.py --course computer-science-grade-6`: 0 failing findings against the baseline, 1 new
  note line (sequence 0 failures). The one standing lint hit is "licence" in frame.md, the proper name Open Government
  Licence, a known exception (lead call 12). The index-reports gate exits non-zero repo-wide; it names no line in this
  course.
