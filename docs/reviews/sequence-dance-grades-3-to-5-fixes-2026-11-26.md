# Fixes: scope and sequence of dance-grades-3-to-5, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-dance-grades-3-to-5-2026-11-26.md), done as
docs/pipeline/briefs/sequence-fix.md with build/scope-writes/ARTS-FIX.md. The Codex read waits for Codex's usage
reset (after 2026-11-30) and gets its own small fix pass then. Files changed: docs/courses/dance-grades-3-to-5/
scope-and-sequence.md, data/plans/dance-grades-3-to-5/days.csv, docs/courses/dance-grades-3-to-5/frame.md (where a
finding changes the frame: the unit 5 evidence line, the Course-level checks table and paragraph, the unit 12
once-a-week sessions). Units, their order, owned rows and day counts are unchanged.

**Counts.** Applied: expert 6 findings in full and 1 in part (finding 4), all 11 "Settled by the expert" rows; lead
calls 7 of 8 (call 4 needs nothing here); band items 0 (none touch this course); own 7. Not applied: expert 1 part
(finding 4's session move); Codex 0 (read not yet made).

## Applied

- **Expert 1** (check items ask about only part of a code). days.csv: day 33 adds one coach comment and the student's
  own alignment check to the group turn (DA:Pr5.1.3c whole) and names the music's timing and beat phrasing in the
  look-for (DA:Pr4.1.3b whole); day 51 starting point picked from three new cards; day 97 drops DA:Pr4.1.4b from its
  codes (the tempo change danced as practice; the percussion part cannot be seen for every student in a four-minute
  turn), DA:Pr5.1.4c's cue and goal parts both seen; day 115 adds the refining line (DA:Pr4.1.4c) and the drawn
  challenge card written for a partner, both halves of DA:Cr1.1.4b scored; day 163 goal line added; day 179 samples
  DA:Cn10.1.5a in place of DA:Pr4.1.5c, and material from two new sources (story and nature cards) with a source line
  each. frame.md: the six Course-level checks rows carry the same wording. Scope: the checks table names the parts; a
  new "Each part of each code" bullet; the rule 3 list updated (42 ids); For the lead item 1's option replaced with a
  unit 9 written item (DA:Pr5.1.5b), never a just-assessed unit's id; old For the lead item 3 (parts at mid-year)
  removed as fixed.
- **Expert 2** (unit 5 end showing missed parts). days.csv day 78: starts on a dancer's cue, changes on the drum or
  held card; a steady and an uneven pattern danced. frame.md unit 5 "End-of-unit evidence" line: the same two changes.
  Scope unit 5 Assessments: the same.
- **Expert 3** (year 5 fold-ins). days.csv: day 158 kept on the shorter year (note says why); day 159's frames into the
  warm-ups of days 157 and 158, never check day 160; day 167 folds, its paired-tool rounds and baseline look into the
  warm-ups of days 168 and 169 (half the groups each day). Scope: Shorter path table row 5 (142, 150, 159, 167) and
  "What was hard to settle" corrected.
- **Expert 4, settled part** (unit 12 once-a-week split). days.csv day 186 to session 29; scope once-a-week table
  (1 = days 181 to 185, 2 = 186 to 189); frame.md once-a-week bullet's unit 12 session wording.
- **Expert 5** (DA:Re7.1.5b on no check row; no responding practice). days.csv: day 177 codes add DA:Re7.1.5b; a
  five-minute responding frames run in the warm-ups of days 174 and 175. Scope unit 11 Arc and Assessments.
- **Expert 6** (mid-year notes carried a written part). days.csv days 33, 97, 163: budget as the day runs (set-up 3,
  warm-up 5, groups 24, goal lines 4 or a cool-down in year 3, cool-down and room back 4: 40). frame.md checks
  paragraph and the scope's Minutes bullet name both budgets; the 30-minute path bullet covers the mid-year checks.
- **Expert 7** (school_day convention). Settled by lead calls 5 and 8: the scope's band-long count is kept, and its
  formula and the week formula are stated once on the first page.
- **Lead call 1.** Four fold-in days a year named; the scope says no other reading of "10 days" is used.
- **Lead call 2.** "The four processes in every unit" rewritten as "The four processes, unit by unit": each year
  claims all four, a unit need not; practice touches claim no id. Checked by script: no day carries a code outside
  its unit's owned rows, and every code sits in its own year.
- **Lead call 3.** The 42 unsampled ids are named with their reason; the frame option goes under For the structure
  pass, not into frame.md.
- **Lead call 5.** school_day stays band-wide (1 to 480); stated.
- **Lead call 6.** Each check day's note says its showing is on earlier-unit work with new items, so no item repeats
  inside two weeks; a scope bullet says so; the old For the lead item 2 is removed.
- **Lead call 7.** Checked: no check re-asks items a unit gave one to three days before (each draws on units assessed
  seven or more weeks earlier); a scope bullet says so. No frame cell wording needed.
- **Lead call 8.** school_day not re-counted; every unit day and check verified on the frame's week by
  `(school_day - 160 x year index - 1) // 5 + 1`.
- **Own 1.** Day 177 note said "the style card from day 11"; now day 175.
- **Own 2.** Day 175 note said the style card is "scored after the session"; now "scored with day 177".
- **Own 3 (each part, rule 2 re-run).** Day 163: DA:Pr4.1.5b's outside-the-body rhythm (a found-sound rhythm beside
  body percussion) and DA:Pr5.1.5c's refine part (spacing refined on a coach cue) were not asked; both added, in
  days.csv and the frame row.
- **Own 4.** frame.md's mid-year rows said "Samples units 1 and 2" (5 and 6; 9 and 10) while every listed code is the
  first unit's; corrected to the first unit, with the reason.
- **Own 5.** Respond days 98 and 180 carried the old check codes; aligned to days 97 and 179.
- **Own 6 (part of expert 4).** Unit 11's six once-a-week sessions rebalanced: 1 = days 165 to 168 (Emergence's
  purpose on the hook's own dance), 2 = 169 to 171, so no session teaches four responding ids; day 168 to session 20.
- **Own 7 (rule 2 re-run, the rest).** Earlier-grade rows: all one grade back, retrieval on each unit's day 2, no
  readiness check (unchanged, table right). Every check code is taught on a day before the check (script). Collect
  once and end days: no change needed. Our words: all new text written fresh.

## Not applied

- **Expert 4, the session move** (one once-a-week session from unit 9 to unit 11 in year 5). With unit 9 at 8
  sessions the year 5 mid-year check session lands in week 17, not CALENDAR.md's week 18, and unit 11 is held at six
  sessions by the week 19 respond session and the week 26 check. The rebalance inside unit 11 (own 6) is done instead;
  the move is under For the structure pass, needing a check-week decision.
- **Band items.** None of the other arts expert reads has an "Across the band" section or names this course; the
  visual arts 6 to 8 read's note that every arts band course counts school_day band-wide agrees with this scope.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A code whose part cannot be seen for every student inside a check's minutes is not listed on the check; it is named under rule 3 with that reason | Checks claim only what they sample; each part of each code |
| A goal part (set goals from feedback) is sampled at a mid-year showing as a kept goal line written at seats from the teacher's comment, 4 minutes | Uses the minutes a written part does not, no day added |
| An invent-and-solve code is sampled by a card written in the written part and solved by the partner in the showing, both scored | Both halves seen in one check |
| A check note's task-form line: "a showing is the discipline's own evidence and may follow the unit showing; the items here are new" | Lead call 6, said on the day |
| A shorter-year fold-in never moves work into a check day's warm-up, and never folds a day that writes a scored line | Nothing assessed is cut |
| A once-a-week rebalance stays inside a unit when moving sessions between units would move a check week | Check weeks are CALENDAR.md's |

## For the structure pass

- **docs/courses/dance-grades-3-to-5/frame.md, Course-level checks, Year 5 mid-year row** (optional, lead's pick, lead
  call 3): to sample one more id, add "and one written item from a new invented dancer's card on how safe habits and
  nutrition prevent injury (DA:Pr5.1.5b, unit 9), its safe practice seen in the showing", sharing the goal-line
  minutes. Not applied here.
- **Year 5 once-a-week sessions (expert read finding 4)**: frame.md "The once-a-week path" bullet "year 5, units of 9,
  8, 6 and 5" would become "8, 8, 7 and 5" only if docs/courses/CALENDAR.md moves the dance 3 to 5 year 5 mid-year
  check to week 17 (and its respond to week 18). Lead's call; the scope is written for 9, 8, 6, 5.
- **build/scope-writes/ARTS-BRIEF.md**, "The four processes" note: old "(create; perform, present or produce; respond;
  connect) appear in every unit's days"; new "appear in every year; each unit works on at least the processes the
  frame names for it and claims only its owned ids (lead call 2)".
- **data/plans/later.csv L107**: dance 3 to 5 now names 42 unsampled ids (was 41): DA:Pr4.1.4b and DA:Pr4.1.5c added,
  DA:Cn10.1.5a now sampled (day 179).
- **docs/courses/CALENDAR.md**: document the band-wide school_day count (lead call 5); **data/plans/calendar.csv**:
  regenerate with `frame.py calendar` at commit (lead call 8). No week of this course moved.

## For Cory

Nothing. No change touches scope, money, people or audience.

## Gates

- `python -X utf8 scripts/sequence.py check dance-grades-3-to-5`: 0 failures.
- `python -X utf8 scripts/frame.py check dance-grades-3-to-5`: 0 failures (60 unit days a year, 192 days).
- `python -X utf8 scripts/frame.py calendar`: exit 0, no failure printed. The course does not break the stagger rule:
  its checks stay in weeks 17 and 26 (grades 3 and 4) and 18 and 26 (grade 5), and arts are specials in K to 5. No
  frame change moved a week.
- No em dashes in the three files; "Curio Class" in full; US spelling.
