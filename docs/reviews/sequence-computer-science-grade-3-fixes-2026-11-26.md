# Fixes: scope and sequence of computer-science-grade-3, 2026-11-26

Job: docs/pipeline/briefs/sequence-fix.md through build/scope-writes/CS-FIX.md. One read so far: the Claude expert
read docs/reviews/sequence-computer-science-grade-3-2026-11-26.md (the Codex read waits for its own pass after
2026-11-30). No other grade's expert read has an item that touches grade 3.

Counts: applied 12 expert findings (with all 8 "Settled by the expert" rows), 4 lead-call items, 1 own finding;
not applied 0.

## Applied

- **Expert 1** (days.csv day 20; frame Evidence and Units table, lead call 11): the solo build codes a
  student-created algorithm, the child's own day 11 field-day algorithm (returned with its marks on day 12) or a
  classmate pair's day 9 card set with its authors named; "or one Curio Class supplies" is dropped; the teacher picks a
  four-card version where a set is longer. Frame's "Curio Class writes" now names a teacher's guide to a four-card
  version, not supplied algorithms.
- **Expert 2** (days.csv days 20, 21; scope unit 3): few devices run the solo turns at stations through day 20 and the
  first half of day 21, five at a time; one screen through days 20 and 21, those not reached recorded on the no-device
  path; day 21 respond work for those children runs on printouts.
- **Expert 3** (days.csv day 25; scope unit 4): the sorter decides only by the class's yes or no feature questions;
  side-view spiders show fewer legs, so the first questions miss them.
- **Expert 4** (days.csv days 2, 13 to 16, 20): each note names its paper path.
- **Expert 5** (days.csv days 4, 29, 30; scope unit 5; frame unit 5 session 3): day 30 goal names three tools, the
  voice helper being the AI system; days 4, 29 and 30 name the second view's source type and say "picked and dated
  when the cards are written"; the voice helper's access claim is kept only if a dated source supports it.
- **Expert 6** (days.csv day 29; frame unit 5 session 2): paying steps are cash counted out with a written bill, a
  card run through a reader, a card or phone tapped to pay.
- **Expert 7** (days.csv days 26, 27; scope course-level checks and rule 3 list; frame year-end row): the pretend-post
  sample and E3-SYS-SE-13 / g3-share-online drop from days 26 and 27; the plan item uses a half-filled planning sheet;
  sitting split about 18 and 7 minutes; SE-13 added to "owned codes not sampled" (scored day 5, sampled day 11).
- **Expert 8** (days.csv days 20, 21; frame Evidence and Units table; scope rule 3 list): a two-minute unseen feedback
  item on day 20 scores E3-PRO-PD-05; the day 16 line is supporting evidence; day 21 gives a missed PD-05 a new
  suggestion on the child's own solo build.
- **Expert 9** (days.csv days 13, 16 to 19, 21, 23; scope unit 3): "Driver and navigator switch at the halfway
  signal" added.
- **Expert 10** (days.csv day 23; scope unit 4): two-row picture graph (windy, calm; each counting cold and warm days,
  one picture for two days); the tool opens with the table entered, about 8 minutes.
- **Expert 11** (scope Shorter path): day 13 drops its second predict program and keeps the reorder; with both folds
  the checks sit in weeks 10 and 24, the lead's calendar pass confirms them.
- **Expert 12** (scope For the lead, units 2 and 4; days.csv day 2, day 20): For the lead 1 and its two pointers
  removed; day 2 `retrieves` = g3-software and the retrieval table updated; day 20 names its rubric.
- **Lead call 1:** no `end` or `observe` mark sat on a teaching day; nothing to clear.
- **Lead call 2:** For the lead on source-map.csv now reads "waits on L149".
- **Lead call 5** (days.csv; frame Day kinds; scope): GLOSSARY wins. Days 4, 10, 16, 19, 24, 28, 29 and 30 are each a
  standard's first day in the course (or the first teaching of the feedback or debugging method) and move from
  Application to Understanding; days 9 and 15 stay Application, days 8 and 14 Fluency. The frame's Day kinds bullet is
  reworded to match, and the scope states the rule once.
- **Lead calls 4, 8, 11** (frame): Evidence bullet, Units table unit 3 end-of-unit cell and "Curio Class writes",
  unit 5 sessions 2 and 3, and the year-end Course-level checks row reworded to the read's fixes. No unit, day count
  or owned row moved.
- **Own 1** (frame Cross-subject, math row for g3-variable-trace): the lean cited "math grade 3 unit 5 (days 78 to 91,
  weeks 16 to 19)"; math-grade-3/days.csv has m3-two-step-problems from day 54 (unit 3, week 11), so the cell now
  says so and the bridge reads "Met before this unit" (the scope's old For the lead 4, now dropped).
- Rule 2 lists re-run: every earlier-grade row is grade 2 with retrieval in its first session; each check's sampled
  codes match the scope table; each owned id sits on a taught day; end days 5, 20, 31 and checks 11, 26 unchanged;
  no em dash, no UK spelling found in the three files.
- Every finding is logged in the defect ledger (`plan.py defect --status=fixed --made-at=scope`): 12 rows found_by
  expert, 4 rows found_by writer for the lead-call and own items.

## Not applied

None.

## Settled

| Judgment | Reuse |
|---|---|
| A standard's first day in the course is Understanding even when it designs, compares or weighs society cases | Every K to 5 computer science course |
| An end-of-unit "create" build codes the child's own earlier algorithm or a credited classmate's, never a supplied one | Every E-band PD id |
| A "use feedback" id gets its own short unseen item in the end sitting; the teaching-session record is supporting | Grades 3 to 5 |
| A year-end sitting does not resample an id already scored at its unit's end and sampled at mid-year | Any course with two checks |
| A pretend sorter acted by the class decides only by written feature questions, so it can err as planned | Grades 2 to 4 |

## For the structure pass

- docs/APPROACH-SOURCES.md: when a dated page from a disability organization on voice helpers used by blind and
  low-vision people is picked (before day 30's cards are written), add it beside the grade 3 entries (frame For the
  lead 6). No other shared file needs a change; data/plans/frames.csv day totals are unchanged.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check computer-science-grade-3`: 0 failures.
- `python -X utf8 scripts/frame.py check` (all frames): 0 failures, computer-science-grade-3 included.
- `python -X utf8 scripts/frame.py calendar`: grade 3 computer science stays in weeks 11 and 26; a special, not counted
  under the stagger rule (CALENDAR.md rule 1); no break caused by this pass.
- `python -X utf8 scripts/gate.py --course computer-science-grade-3`: 0 failing findings against the baseline.
