# Fixes: scope and sequence of computer-science-grade-8, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-computer-science-grade-8-2026-11-26.md), done to
docs/pipeline/briefs/sequence-fix.md as build/scope-writes/CS-FIX.md sets it for the computer science run. The Codex
read waits for Codex's usage reset (after 2026-11-30) and gets its own small fix pass.

Counts: applied 13 expert findings (14 parts; finding 13 has two) and all 13 rows of the expert's Settled table; lead
calls 1, 2, 3, 4, 5, 7, 8 applied (6 checked, holds; 9, 10, 11, 12 checked, nothing to do here); 1 cross-grade item
(grade 9 read finding 2, the debugging method, met by expert finding 10); 5 own findings applied. Not applied: 0.

## Applied

- **Expert 1** (days.csv rows 34 to 39; scope unit 3; frame Units cell, Seams, Models carried, Cross-subject, Source
  map): the stage block now runs days 34 to 36 (park survey with the g7-personal-data retrieval, misleading chart,
  weaker model) and the summary block days 37 to 39 (graded summary and checklist, draft, feedback and revision);
  each position keeps its `school_day`. Day 37's checklist reads "possible biases: name the stage and the decision".
  The summary falls on school days 92, 94 and 97, after ELA unit 3 ends (88), so e8-produce-publish is met before.
  Day 39's note says the revised summary is scored with day 40. Arc, Why this order, Candidate (day 34) and Leans
  rewritten; base text credits now run in the base's own order (lesson 5 on day 34, lesson 6 on days 37 to 39), and
  the frame's Source map reason for moving lesson 5 is gone.
- **Expert 2** (days.csv days 10, 11, 27; scope unit 1; frame Units cell, Evidence, checks table): day 10 `assess` =
  `observe` with the look-fors (the change on the system-diagram, the need each part serves, day 9's test record,
  revision and retest, named roles); day 11's note: IM-36 scored on day 11's item and day 10's observed team product;
  day 27 says the collaborate part is carried from day 10, not collected again.
- **Expert 3** (days.csv days 19, 20, 22 to 25, 31 to 33, 44, 51, 21; scope Devices): a paper-path line on each, as
  the expert worded it; day 21's device boilerplate dropped for "Unplugged: the printed program traced by hand".
- **Expert 4** (days.csv days 25, 59; scope units 2 and 5, For the lead): `assess` cleared on both; day 25 stays a
  Check day reported with day 26; day 59's note calls it the debate's written practice, collected, not scored, before
  the unseen ET-42 item on day 62. For the lead 3 and 4 deleted.
- **Expert 5** (days.csv day 26; scope checks table; frame checks table): the TR-20 item gives two classmates'
  feedback lines (one usability, one accessibility): the change for each, its test, and one line not acted on and
  why. Same 7 minutes.
- **Expert 6** (days.csv day 13; scope Devices; frame Devices and Units cell): day 13 is a paper day with the
  teacher's one screen for the live-code, about 40 teaching minutes; pairs open the editor first on day 14.
- **Expert 7** (scope Shorter path): the day 2 fold replaced by day 59 into day 58 (one debate round fewer, the last
  ten minutes each student's own card). Still ten lessons.
- **Expert 8** (days.csv days 30, 31; frame Units cell): the out-of-data judgment moved from day 30's goal to day
  31's, beside the no-relationship and falling sets.
- **Expert 9** (days.csv day 40; scope and frame unit 3 assessment): the DI-25 item runs in the table-and-scatter
  tool where the class has devices (one per pair or stations), by hand on the no-device path marked part met.
- **Expert 10** (days.csv days 14, 17, 23, 49; scope Debugging bullet; frame Units cell): day 14 names the routine
  (predict, run, compare, find the first place it goes wrong, change one thing, test again, CT9) on the wrong-length
  bug; days 17, 23 and 49 use it by name. This is also the grade 9 read's cross-grade item (its day 6 retrieves
  "grade 8's CT9 method").
- **Expert 11** (days.csv day 1; scope Safety; frame unit 1 sensitivity cell): the security line on day 1.
- **Expert 12** (scope unit 5): the leave-out sentence for days 54 to 62 and the family note.
- **Expert 13a** (frame Days bullet): "opens in five minutes with a three-minute retrieval trace".
- **Expert 13b** (days.csv day 54; scope unit 5 Sensitivity): teacher note calls video visits an emerging technology
  at the time of the report (2021); days 55 and 62 carry the current cases; figures wait on the browser check.
- **Lead call 1:** `end` cleared on days 25 and 59 (above); scope For the lead 4 dropped.
- **Lead call 2:** scope For the lead 1 (copy in the scratch source-map.csv) removed; the Base text bullet says no
  source-map.csv in this run, placements stay in the .md and the frame's Source map, waits on L149. The scratch draft
  stays in build/scope-writes/scratch/computer-science-grade-8/.
- **Lead call 3:** `frame.py check computer-science-grade-8` had 0 failures before and after.
- **Lead calls 4 and 8:** the frame wording the read put "at the next frame pass" applied here (unit 3 order in the
  Units cell and Source map, the device list, the opener wording), plus the checks table cells widened to every part
  (expert 5, own 4). No unit, day count or owned row moved.
- **Lead call 5** (days.csv days 14, 22, 57; frame Day kinds): by GLOSSARY, day 14 (first teaching of the debugging
  method), day 22 (first teaching of g8-refine-for-users, a worked example before testing) and day 57 (first day of
  g8-emerging-debate, roles and frame taught) are Understanding. The frame's Day kinds bullet reworded to match
  GLOSSARY, its lists corrected (adds days 21, 50, 61 to Application, day 25 as Check, drops "the five-minute retrieval
  traces" from Fluency); this also answers the scope's old For the lead 5, now removed.
- **Lead call 6 (checked):** on the shorter path day 17 folds into 16 and 20; list work is about 3.5 of 42 teaching
  days, about 8 percent, under 10. Stated in the scope's C1 bullet.
- **Lead call 7:** 14 rows logged with `plan.py defect --status=fixed --made-at=scope` (one per finding part).
- **Own 1** (days.csv day 17): it named no paper path either; "code on paper, a partner as the computer" added.
- **Own 2** (scope Shorter path): with expert 8, the old "day 31 into day 30" fold would rebuild the overloaded day 30;
  now day 31 folds into days 30 (the contrast sets, ten minutes) and 32 (the out-of-data judgment on the pair's own
  set), and day 33 folds into days 32 and 38 (the fairest chart drawn in the summary draft, now day 38).
- **Own 3** (scope readiness table; frame Seams): g7-personal-data now retrieved on day 34, after the swap.
- **Own 4** (each part of each code; days.csv day 63; scope and frame checks tables): day 63's ML-08 item asks a
  feature and a limit, RD-18 the first wrong line and one usability fault (accuracy and usability), IM-29 what the
  decision does to a chart and to a model. Same minutes.
- **Own 5** (frame Evidence bullet): unit 3 draft and revision days now 38 and 39; a "collaborate" id is evidenced
  by the observed team product beside a written item.

## Not applied

None.

## Rule 2 lists, re-run

- Earlier-grade rows: all 18 assumed rows were last used in grade 7, retrieved on the frame's Seams days (one moved,
  g7-personal-data to day 34); elective-path readiness on days 1, 12, 28, 41, 53, none on a unit's first day.
- Checks' sampled codes: mid-year PD-14, TR-20, SE-33, IM-36; year-end ET-41, ET-42, DI-25, IM-29, ML-08, RD-18 (10
  of 13; DI-27, IM-11, PS-05 named, For the lead 1).
- Collect once: day 10's observation is reused by day 11 and day 27, not collected again.
- Each part of each code: TR-20 (feedback), IM-36 (collaborate), ML-08, RD-18, IM-29 fixed above; the others hold.
- End days: day 11, 40 and 52 hold short items per code inside 35 minutes; units 2 and 5 end on the following check.
- Our words: no base wording copied (base not loaded).

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A day that first names a method on modify work is Understanding (day 14) | GLOSSARY: first explicit teaching of a method |
| A worked example of faults before peer testing is Understanding (day 22) | First teaching wins over testing |
| Debate preparation that teaches roles and the claim, backing, rebuttal frame is Understanding (day 57) | First day of the row |
| A collaborate id is carried by an `observe` day on the team product, reused by the next checks | Collect once; the part is scored, not only named |
| A shorter-path fold must not undo a read's load fix (day 31 folds into 30 and 32, not 30 alone) | Keeps DI-25's judgment off an overloaded day |
| Practice of a written form eight school days before an unseen check item on a new question is practice, not a repeat | Expert finding 4 |

## For the structure pass

- docs/courses/CALENDAR.md and data/plans/calendar.csv: no change; no `school_day` moved (the swap kept each
  position's school day).
- docs/APPROACH-SOURCES.md: no change beyond the frame's For the lead 5, already listed.
- The data/progressions/computer-science.csv rows are unchanged; no owned row moved.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check computer-science-grade-8`: 0 failures.
- `python -X utf8 scripts/frame.py check computer-science-grade-8`: 0 failures; `frame.py check` (all frames): 0
  failures.
- `python -X utf8 scripts/frame.py calendar`: no failure; grade 8 computer science weeks 13, 14, 31, 32, as before.
  No stagger break (no school day changed).
- `python -X utf8 scripts/gate.py --course computer-science-grade-8`: 0 failing findings against the baseline. The one
  standing lint hit is the UK spelling inside the Open Government license's proper name in the frame, kept (lead
  call 12). index-reports
  exits non-zero site-wide on orphaned reports (30 new across the run, this report among them), not on this course.

## Browser checks (unchanged)

The CISA phishing page (day 4) and the ASPE 2022 telehealth report (day 54), at grade close.
