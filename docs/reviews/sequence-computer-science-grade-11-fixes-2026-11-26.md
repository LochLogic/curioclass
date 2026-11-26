# Fixes: scope and sequence of computer-science-grade-11, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-computer-science-grade-11-2026-11-26.md), by
build/scope-writes/CS-FIX.md and docs/pipeline/briefs/sequence-fix.md. The Codex read waits for Codex's usage reset
(after 2026-11-30) and gets its own small fix pass.

Counts: applied 11 of 11 expert findings, 6 of 6 expert settled rows, 7 lead calls that touch this course (1, 3, 4, 5,
6, 7, 8), 0 neighbor-grade items (none touch grade 11), 2 own findings. Not applied: 0. Lead calls 2, 9, 10, 11 and 12
have nothing in this course.

## Applied

- **Expert 1** (days.csv day 50 goal and note; .md unit 5; frame.md Sensitivity reads, unit 5 row session 3, For
  the lead 5): the EEOC source is dated "issued May 2023, removed from eeoc.gov January 2025; the Title VII duty it
  explained still stands", the removal used as a dated fact for the audit. A second view is added: a dated government
  or university source arguing that structured or algorithmic screening is more consistent than unstructured human
  judgment; candidate named from memory (the US Office of Personnel Management's structured interview guide, 2008),
  opened and dated by the unit writer. NIST SP 1270 kept.
- **Expert 2 / lead call 1** (days.csv days 28 and 61; .md units 3 and 6, For the lead): `assess` blanked on both
  days; notes keep the hand-in line and drop "End-of-unit assessment, part 1"; the .md's gate sentences and For the
  lead 1 are removed.
- **Expert 3** (days.csv days 21, 53, 62; .md units 2 and 5, year-end check; frame.md unit 2 and unit 5 end-of-unit
  cells and the year-end check cell, under lead call 4): day 21 adds two generated test suggestions kept, changed or
  dropped with the reason, and fit to the requirement; day 53 adds one thing the audit could not see; day 62 asks
  how the change encourages innovation and cuts a named risk, with one piece of evidence and who it affects.
- **Expert 4** (days.csv days 58, 59, 60; .md unit 6): two views and a dated source named on each.
- **Expert 5** (days.csv days 1, 2, 3, 6, 7, 8, 34; .md calendar and unit 1): the short Safety line added; day 3's
  "No attack steps" sentence folded into it.
- **Expert 6** (days.csv day 56; .md unit 6 Sources): about 29 percent of city water in 2021 from city records after
  the 2022 settlement, later share near a third disputed by the city, checked by search 2026-11-26, to be opened by
  the unit writer.
- **Expert 7** (days.csv days 10 and 16; .md unit 2): day 10 sets the two class values on the specification sheet,
  about five minutes; day 16 applies them.
- **Expert 8** (.md Shorter path; days.csv day 55 note): the day 56 fold keeps each student's own written link as day
  55's exit ticket.
- **Expert 9** (days.csv day 54; .md unit 6 Readiness): one page of six one-minute items as settled.
- **Expert 10** (days.csv days 40 to 43; .md unit 4): driver and navigator switch at the halfway signal (IC5).
- **Expert 11** (days.csv day 40 goal; .md unit 4): opens with "Predict which 7s the model will miss"; kind stays.
- **Expert For the lead** items (two frame.py failures, EEOC dating in the frame): applied here under lead calls 3
  and 4.
- **Lead call 2** (S1-AIN-DD-02 off the course-level checks): the .md now says it stays off, settled by the expert;
  the optional frame fix in the old For the lead 2 is dropped.
- **Lead call 3** (frame.md Cross-subject; frame.md For the lead 6): Cross-subject names the us1-progressivism lean
  (US history I unit 8, weeks 25 to 28, before day 57 in week 29, no bridge owed); the "until it is loaded" line is
  now `Pending(docs/sources/BASE-TEXTS.md#noaa-climate-data-online)`. The same marker replaces "not yet loaded" in the
  .md (top note, unit 3) and in the notes of days 23, 24, 26 and 33. The .md's old For the lead 3 is dropped.
- **Lead call 5** (frame.md Day kinds bullet): reworded to GLOSSARY (first teaching of a row or method is
  Understanding, predict and watch included, first teaching wins over modify or draft).
- **Lead call 6** (.md Shorter path): see own 2.
- **Lead call 7**: 14 defect rows logged with plan.py defect (status fixed, made-at scope).
- **Own 1** (days.csv days 4, 13, 42, 49; .md Day kinds paragraph; frame.md Day kinds bullet): relabeled
  Understanding by GLOSSARY: day 4 first teaches the flaw-report method, day 13 judging generated test suggestions,
  day 42 the training-set change, day 49 where bias comes from. sequence.py passes.
- **Own 2** (.md Shorter path; days.csv days 27, 31): on the 54-day year the Specialty share was about 4.3 of 40
  teaching days (10.8 percent). Day 27 (whole Specialty) now folds into day 28's first 15 minutes in place of day 31's
  fold; share about 3.7 of 40, 9 percent. Day 31 stays a day.
- **Rule 2 re-run**: end and check days 8, 21, 33, 34, 46, 53, 62, 63 now prompt every part of their codes; Collect
  once holds (days 28, 45, 61 products scored once outside the sittings); readiness rows and their first-use worked
  examples unchanged and sound.

## Not applied

None.

## Settled (for DIGEST)

| Choice | Reason |
|---|---|
| Hiring case second view: a dated government or university source on structured screening (candidate OPM structured interview guide, 2008, from memory) | The row asks for two views; EEOC and NIST give one |
| A withdrawn agency document is dated with issue and removal, and the removal used as a case fact | Keeps the case current without dropping a good source |
| Days that first teach a method are Understanding even when they also modify or audit (days 4, 13, 42, 49) | GLOSSARY wins (lead call 5) |
| Shorter year: fold the whole Specialty day 27 into day 28 rather than day 31 | Keeps bar C1 under 10 percent on 40 teaching days (lead call 6) |
| NOAA extract wording uses `Pending(docs/sources/BASE-TEXTS.md#noaa-climate-data-online)` | The marker resolves when BASE-TEXTS records the extract |

## For the structure pass

- docs/APPROACH-SOURCES.md: add the EEOC technical assistance dated (issued May 2023, removed from eeoc.gov
  2025-01-27; Cooley 2025-02-21, National Law Review 2026, search only); the OPM structured interview guide (2008,
  from memory, to be opened); The Dalles water use (WaterWatch of Oregon; OPB 2026-01-15 and 2026-01-23; search only);
  chapter 70A.500 RCW (checked 2026-11-26).
- docs/sources/BASE-TEXTS.md: when the NOAA extract is loaded, its row should carry the anchor text
  `noaa-climate-data-online` so the Pending markers in this course resolve (and are then rewritten).
- TOOL-ASKS.md: the five tool asks in the .md For the lead 1, unchanged.

## For Cory

Nothing.

## Gates

- `sequence.py check computer-science-grade-11`: 0 failures.
- `frame.py check computer-science-grade-11`: 0 failures (was 2).
- `stale.py check` on the frame and the .md: 0 failures.
- `frame.py calendar`: covers K to 8 only; grade 11 is not listed, so no stagger break to name. No unit or check moved.
- `gate.py --course computer-science-grade-11`: 0 failing findings against the baseline; the index-reports gate
  exits non-zero as it did before this pass.
