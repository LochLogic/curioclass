# Fixes: scope and sequence of library-and-research-skills-grade-5, 2026-11-26

Fix pass on the Claude expert read (docs/reviews/sequence-library-and-research-skills-grade-5-2026-11-26.md), per
build/scope-writes/AFTERCORE-FIX.md and docs/pipeline/briefs/sequence-fix.md. The Codex read waits for Codex's usage
reset (after 2026-11-30). No git.

Counts: applied 14 (expert 12, lead calls 2); not applied 1 (expert 1, under lead call 12). The other library
expert reads (kindergarten, grade 1) hold no item that crosses into grade 5.

## Applied

- Expert 1a: scope-and-sequence.md Shorter path. Fold-in 1 (day 3) replaced by day 30 folded into day 29 (reteach
  10, gaps 10, year look-back 9; fresh try dropped); fold-in 2 (day 12 into day 14) kept; day 3 stays.
- Expert 1b: scope-and-sequence.md Shorter path. 30-minute session: day 11 runs reason lines 11, lateral part 15.
- Expert 2: days.csv codes. Dropped ~AASL.I.A.1 and ~AASL.IV.B.1 from day 13; ~AASL.IV.B.1 from days 5 and 28;
  ~AASL.II.B.2 from days 19 and 28. .md unit 1 and unit 3 lines updated ("practiced, not assessed"; "begun here,
  not assessed").
- Expert 2: days.csv day 5 goal and note get "write one more question research could answer on the same topic"
  inside the sort's 8 minutes (~AASL.I.A.1); day 19 goal and note get "say which plan your notes are sorted by and
  why" inside the 13-minute notes part (~AASL.IV.B.4). .md end-of-unit lines match.
- Expert 3: days.csv day 8 note bridges to health grade 5 unit 16's source check card (weeks 5 to 9); .md unit 2
  Leans line names it.
- Expert 3 (For the lead, applied under lead call 7): frame.md Cross-subject gets a "Health, grade 5" table with the
  unit 16 row; the section's opening line now names health.
- Expert 4: days.csv day 25 kind Application, goal "Inquiry: revise the product from advice; ..."; note says why.
  Day 27 note and .md unit 4: response time day 29 alone (12 minutes).
- Expert 5: days.csv day 8 models the name-and-photo case (1 minute); day 9's retrieval adds it as a scenario card,
  and its retrieves column adds g3-safe-searching. .md readiness paragraph and unit 2 retrieval line name it.
- Expert 6: days.csv day 2 note gets the split 5 / 9 / 3 / 7 / 5.
- Expert 7 (stale item 5): .md For the lead item 5 dropped; frame.md item 5 says done.
- Expert 7 (bat set): days.csv day 1 note and .md unit 1 say the set states "most bats" echolocate.
- Expert 7 (NetSmartz): no change; the .md line "not opened" stands, as the read confirms.
- Lead call 1: frame.md placement paragraph and For the lead item 3 reworded as settled by CALENDAR.md rule 1; .md
  For the lead item 1 dropped.
- Lead calls 4 and 5: frame.md unit 3 row and Cross-subject host line name science unit 5 (weeks 21 to 25) as a later
  use; unit 4 row and the science table say science unit 6 is beside the unit's last three days (weeks 25 to 27);
  frame.md brief and check table say unit 4's response time (not "respond step"), matching GLOSSARY and day 25;
  unit 2 row quotes the widened AASL.IV.B.3 gloss. .md For the lead items 2 and 3 dropped as fixed in the frame;
  item 4 dropped as settled by lead call 10 (unit 4's codes stay off the checks with the reason named in the .md).

## Not applied

- Expert 7 and For the lead (unit 3's "None" owned cell prints "standard None is on no day"): left as is under lead
  call 12. Logged rejected.

## Settled

| Judgment | Reason | Where |
|---|---|---|
| A course-level respond day that is pure reflection can be the 10-days-short fold-in | Holds no assessment; the look-back line is itself a fresh try | .md Shorter path |
| A begun code (~ id the course does not meet) stays off assessment days | Checks claim only what they sample | days.csv 19, 28 |
| A group revision from advice before scoring is Application | GLOSSARY: drafting and revising are Application | days.csv 25 |
| Two subjects' source-judging cards in one grade get one bridge sentence on the later day | Lens: say how they relate | days.csv 8; frame Cross-subject |

## For the structure pass

- docs/agents/lenses/library.md: no UK spellings checked in this pass (lead call 13); none raised by the read.
- scripts/sequence.py or the frame cell: the "standard None is on no day" note for unit 3 (left under lead call 12;
  the lead may make the gate skip "None").
- The health grades 3 to 5 frame may add a matching line that library grade 5 unit 2 adds "leave the page" to its
  source check (expert finding 3; another course's file).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check library-and-research-skills-grade-5`: 0 failures; note "unit 3: standard
  None is on no day" (lead call 12).
- `python -X utf8 scripts/frame.py check library-and-research-skills-grade-5`: 0 failures; note 4 units, 30 days.
- `python -X utf8 scripts/plan.py check library-and-research-skills-grade-5`: passes.
- No day, unit, week or check moved, so the stagger is unchanged (library is a special, CALENDAR.md rule 1).
