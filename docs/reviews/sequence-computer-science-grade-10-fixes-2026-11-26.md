# Fixes: scope and sequence of computer-science-grade-10, 2026-11-26

Fix pass on the Claude expert read docs/reviews/sequence-computer-science-grade-10-2026-11-26.md, per
build/scope-writes/CS-FIX.md and docs/pipeline/briefs/sequence-fix.md. The Codex read waits for Codex's usage reset
(after 2026-11-30) and gets its own small pass then.

Counts: applied 17 (expert 14 of 14, lead calls 2, own 1); not applied 1 (the expert's optional day 44 item). No
cross-grade item in the neighboring grades' reads touches grade 10 (grade 11's day 54 readiness item is grade 11's own
day).

## Applied

- **Expert 1** (days.csv, frame.md): day 10's sitting adds "use the step-through debugger to find the line where a
  given call returns the wrong value and say what the highlighting showed"; paper version is a printed step-through
  trace, part met without a device. Frame unit 1 end-of-unit text adds the same item.
- **Expert 2** (days.csv, frame.md): goals of days 40, 29, 51 and 19 rewritten to prompt every part: DC-23 (named
  cleaning steps and one pattern-rule place), DC-24 (a wrong type, a value not allowed, a value out of range), NT-35
  (layers and routers), SE-32 (a new social engineering case too), IM-09 (one social or ethical effect on a group of
  users), ML-06 (data size and type, whether a person can follow it, the outcome wanted). Frame unit 2, 4 and 5
  end-of-unit texts and the mid-year check row match.
- **Expert 3** (scope-and-sequence.md): shorter path no longer folds days 4, 56 or 60; it folds 5 into 4 (last 15
  minutes), 57 into 56 (first 15 minutes), 14 into 13 (printed counts). Since finding 5 made day 7 the library modify
  day, the old fold-in of day 7 is replaced by 6 into 7 (the page read in day 7's first 15 minutes). Still 10 days,
  450 minutes.
- **Expert 4 / lead call 1** (days.csv, scope-and-sequence.md): day 28 `assess` blank, its gate-slot sentence
  dropped; unit 3's assessment sentence reworded; For the lead 1 deleted and the list renumbered.
- **Expert 5** (days.csv, frame.md): day 7 is Fluency, "Device, modify: change the arguments of two supplied library
  calls ... then add one call the page describes". Frame Fluency list adds unit 1 lesson 7 and lesson 7's text says
  modify; the .md unit 1 paragraph says so.
- **Expert 6** (days.csv, frame.md): day 15 runs on a printed trace-table by default, device optional. Frame device
  list names unit 1 lesson 10 and unit 4 lesson 9 as device sittings with a paper version, and unit 2 lesson 4 as
  paper by default.
- **Expert 7** (scope-and-sequence.md): year-end row reads "31 (154) and 32 (157); respond week 32 (159)".
- **Expert 8** (days.csv, scope-and-sequence.md): day 7 adds one line on what probabilistic means and day 22 a
  one-card worked example of the operating system layer, both for students who did not take grade 9; the .md lists
  these two threads as review with a worked example, not readiness.
- **Expert 9** (days.csv): the seventeen bare openers now name their trace (the expert's list; days 48, 49 and 50 got
  a unit 1 procedure call, a unit 2 step count and a unit 1 list trace).
- **Expert 10** (scope-and-sequence.md): each unit opens with its concept area line.
- **Expert 11** (days.csv, frame.md): day 33 predicts a supplied trim and change-case call on a before-and-after
  table, runs it, then applies it. Frame unit 4 lesson 2 matches.
- **Expert 12** (days.csv, frame.md): day 54's teacher line adds where the copy is kept and the date checked
  (browser check); day 57's FTC rule page carries the date of its latest amendment. Frame unit 6 source lines match.
- **Expert 13** (days.csv): day 30 note reads "Task forms differ from days 10 and 19".
- **Expert 14** (days.csv): day 31 codes add HS-PRO-RD-17, HS-ALG-PS-03, HS-ALG-ML-06; day 64 codes add HS-PRO-RD-17,
  HS-ALG-PS-03, HS-DAT-DC-24, HS-ALG-IM-09.
- **Lead call 5** (frame.md, scope-and-sequence.md, days.csv): frame Day kinds Fluency list drops unit 4 lesson 4
  and lesson 4's text names it the first teaching of structure; the .md's For the lead 2 is gone and day 35's note no
  longer points at it.
- **Lead call 7**: one defect row per item above logged with plan.py defect (status fixed, made at scope).
- **Own** (frame.md): unit 2 lesson 5 no longer names memory use; it sits in lesson 2 (day 13), as the scope and the
  expert's Settled table have it.

## Not applied

- Expert 12's optional day 44 note (the 2024 Justice Department web accessibility rule): offered from memory as
  optional, not confirmed at source; left for the unit writer.
- Lead calls 2, 3, 4 (beyond the items above), 6, 9 to 12: nothing in this course needed them (no source-map, frame
  check had 0 failures, no Specialty days, no grade 9 entry pick here).

## Settled

| Item | Judgment |
|---|---|
| Shorter path once day 7 is the library modify | Fold day 6 (documentation read) into day 7's first 15 minutes, not day 7 into 8 |
| Day 15 device or paper | Paper by default (printed trace-table), device optional; frame device list unchanged in count |
| Device sittings | Days 10 and 40 are device sittings with a paper version; the paper version records part met without a device |
| Retrieval openers on days 48 to 50 | A unit 1 procedure call, a unit 2 step count, a unit 1 list trace |

## For the structure pass

- None. No unit, unit order, day count or owned row changed. The frame changes are wording only (lead calls 4, 5 and
  8).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check computer-science-grade-10`: 0 failures.
- `python -X utf8 scripts/frame.py check computer-science-grade-10`: 0 failures; `frame.py check` (all frames): no
  failures.
- `python -X utf8 scripts/frame.py calendar`: no failures; grade 10 is outside the K to 8 stagger rule, and no frame
  change here moves a check.
- `python -X utf8 scripts/gate.py --course computer-science-grade-10`: 0 failing findings against its baseline (one
  new note line, the sequence check's 0-failure note; the shared index-reports gate exited non-zero both before and
  after these edits).
