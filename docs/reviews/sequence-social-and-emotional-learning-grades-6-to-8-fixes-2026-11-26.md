# Fixes: scope and sequence of social-and-emotional-learning-grades-6-to-8, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-social-and-emotional-learning-grades-6-to-8-2026-11-26.md),
per build/scope-writes/AFTERCORE-FIX.md. The Codex read waits for Codex's usage reset (after 2026-11-30) and gets its
own small fix pass then; the 2026-11-15 lead-call items are skipped as the fix brief says.

Counts: expert findings applied 9 of 9 (every bullet of findings 1, 2, 4 and 9) and all 10 rows of the expert's Settled
table; the read's four "For the lead" frame items applied to frame.md under lead calls 4 and 7; lead calls 4, 5, 7, 8
and 11 applied; band items from the K to 2, 3 to 5 and 9 to 12 reads: none touch this course. Not applied: 0.
Scratch scripts and before-copies: build/scope-writes/scratch/social-and-emotional-learning-grades-6-to-8/.

## Applied

- **Expert 1** (days.csv, scope units 1, 13, 15, 17 and checks tables, frame unit 1, 13, 15, 17 cells and the grade 8
  mid-year check cell): unit 15 owner split, with SM1's written cost and recovery judged on day 155's class sheet and SM5
  (the cut week, the cost of each move, the folder or checklist system) on day 158's. Day 159's page is SA3, SM2, SM3
  (V.D.1), SA8 (V.D.2) and the two samples: six items, no two-part merge. SM5 dropped from day 159's codes, SM1 kept for
  the rehearsal. Day 179 plans the offer of help, and day 180's page asks both halves of RS8. Day 137 adds the one-line
  "where the clock bent the thinking" prompt and splits RD4 into weigh, choose and judge. Day 9 asks for the planner
  and the materials system with the reason. The scope's owned-codes table gains an SM1/SM5 row, and the sampled list
  drops SM5.
- **Expert 2** (days.csv 56, 109, 126, 184, 186, 187, frame unit 18 cell, scope units 6, 11, 12, 18): each student's
  own record inside the shared act: the written presentation choice (56), guides rotating by card (109), a written
  view of the cause and the solution to test (126), a written first step with its cost and an objection card (184),
  a trio rotation where each student leads one decision (186, carried onto the real decisions on 187), and each
  student's written judgment of the solution (187).
- **Expert 3** (scope Shorter path): the short year merges each group's two Fluency days into one skill-split session.
  The retrieval opening stays, the merged day keeps the second day's number (pairs listed), and the total is still 12
  sessions.
- **Expert 4** (days.csv 32, 43, 54, 60, 139; scope units 4, 5, 6, 14): unit 2 bridge on day 32, unit 3 bridge on
  day 43, unit 4 bridge on day 139; unit 6's unit 4 bridge moved from day 60 to day 54, beside unit 3's.
- **Expert 5 / lead call 8** (days.csv codes, scope band bullet): `~` on every code on days 1 to 128 (csv-module
  rewrite, codes column only). No teaching day had empty codes.
- **Expert 6 / lead call 4** (days.csv 1, scope unit 1 and Readiness bullet, frame Days bullet and unit 1 cell): day 1
  models the three sub-skills on one first-week case and quotes the goal steps card word for word (goal, steps, block
  and plan, check). Readiness moves to the last ten minutes of session 1 (rule 2). Scope For the lead 1 dropped.
- **Expert 7 / lead call 7** (frame Evidence bullet, scope Shorter path): on the once-a-week path the Application
  session marks the watched rehearsal, and codes judged on full-path Application days move to the shared Check page as
  one written part each, up to six items (inside the frame's cap). Units 6, 12 and 18 carry out one project part,
  chosen at the unit plan.
- **Expert 8 / lead note** (days.csv 164, frame Base text, unit 16 cell and For the lead 11, scope unit 16 and Sources):
  the nonexistent milestone page is replaced by two federal pages, both opened 2026-11-26:
  - ADA.gov's introduction to the ADA, https://www.ada.gov/topics/intro-to-ada/.
  - The National Archives' ADA research page, https://www.archives.gov/research/americans-with-disabilities ("Signed on
    July 26, 1990").

  The case is now the ADA. Section 504 stays only if the unit plan first opens a federal page for it (browser check if
  it blocks).
- **Expert 9** (days.csv 1, 22, 26, 54, 57, 90, 99, 185; frame unit 6 and 18 cells, the health and PE cross-subject
  tables):
  - Day 1: the ELA norms apply from day 2, and day 1 uses the teacher's own two talk rules.
  - Day 54 and the frame: health unit 8 "runs alongside, nearly done".
  - PE weeks corrected to PE 6 to 8's days.csv: unit 4 weeks 12 to 15, unit 12 weeks 17 to 21, unit 18 weeks 12 to 14.
  - Day 22: "an invented character's model".
  - AASL at grade 6 depth named on days 1 (V.D.1) and 26 (V.D.2).
  - Day 90 now cites the National Archives 19th Amendment page. It states who was still kept from the polls after 1920
    only from an opened federal source: the National Park Service's "Who was excluded?"
    (https://www.nps.gov/articles/who-was-excluded-women-s-suffrage.htm, opened 2026-11-26) says Black women were kept
    away by discrimination and intimidation, and Native American women were not citizens until 1924. The read's
    immigrant-women point was left off because that page does not state it.
- **Lead call 5**: no clash found between the frame's Kinds of day bullet and GLOSSARY; nothing to change.
- **Lead call 6**: 9 defect rows logged (made-at scope, status fixed), one per finding.
- **Lead calls 1, 2, 3, 9, 10, 12, 14**: nothing here needed them:
  - Rule 1 is K to 5 only.
  - There is no source-map.csv.
  - frame.py check shows 0 failures.
  - No check reuses a unit record.
  - Owned codes stay assessed at their unit ends, with the reasons in the .md.
  - No readiness check sits in a note with `assess` blank (days 65 and 129 open on retrieval).

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A grade 8 owner code whose row has a written part (a cost, a recovery, a look-back, an offer) gets that part on a named page or class sheet, not only in a watched rehearsal | the row is asked whole in the owner year |
| A shared class act (one vote, one leader) is never an evidence point alone; each student writes or takes a turn inside it | a class sheet marks each student |
| Short year: merge two Fluency days into one skill-split session, never fold a Fluency into the 5-minute opening | the opening is the one retrieval slot; every assessed skill keeps a rehearsal |
| A federal source for a later law is never "the milestone page" (the list ends in 1965); for the ADA use ADA.gov plus the National Archives ADA research page | opened 2026-11-26 |
| A settled-history fact on a day comes only from an opened federal page; anything else is marked browser check or left off | lead note, findings 8 and 9 |

## For the structure pass

- Lens spellings (lead call 13): a search of docs/agents/lenses/ and docs/courses/sel/STANDARD.md finds no "practise",
  "behaviour" or "judgement" left for SEL. Nothing to change, and the scope's For the lead item 2 can drop the
  "judgement" clause once the lead confirms it.
- docs/courses/sel/STANDARD.md and the source list: record the National Archives ADA research page
  (https://www.archives.gov/research/americans-with-disabilities) and the National Park Service's "Who was excluded?"
  page as opened federal sources. Also record that the milestone list stops at 1965, which the read raised for every
  frame naming a "milestone page" for a later law.
- Scope For the lead item 1 (cumulative school_day) stays open for the lead, as the read said no change is needed.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check social-and-emotional-learning-grades-6-to-8`: 0 failures.
- `python -X utf8 scripts/frame.py check social-and-emotional-learning-grades-6-to-8`: 0 failures (unit days 60 a
  year; 18 units, 192 days, 180 in units, 12 for checks and respond days).
- `python -X utf8 scripts/frame.py calendar`: no break reported. No unit, day count, school day or check week moved
  (SEL grade 6 and 7 weeks 15 and 32, grade 8 weeks 16 and 32).
