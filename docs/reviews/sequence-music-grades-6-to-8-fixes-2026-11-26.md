# Fixes: scope and sequence of music-grades-6-to-8, 2026-11-26

Fix pass per docs/pipeline/briefs/sequence-fix.md with build/scope-writes/ARTS-FIX.md. One read so far: the Claude
expert read docs/reviews/sequence-music-grades-6-to-8-2026-11-26.md. The Codex read waits for Codex's usage reset
(after 2026-11-30) and gets its own small fix pass then; the brief's Codex and 2026-11-15 lead-call items are skipped.

Counts: applied 11 expert findings (all, with every row of "Settled by the expert"), 6 ARTS-FIX lead calls applied
or confirmed (1, 2, 3, 6, 7, 8; 4 and 5 need no change), 0 band items (none exist, see Not applied), 2 own.
Not applied: 0 expert, 0 lead calls; the expert's words-file check goes to the structure pass.

## Applied

- **Expert 1** (year-end checks miss Cr1.1 parts). days.csv day 63 goal adds the mood in one line and the A or B
  place in an ABA piece with the reason; day 127 adds the expressive aim and one decision that carries it; day 191
  adds the expressive aim and one coda decision. scope-and-sequence.md Course-level checks table samples cells
  rewritten to match.
- **Expert 2** (listening ids on one teaching day). days.csv days 12 to 15, 76 to 79 and 140 to 143: the five-minute
  opener is a rotating listening round (structure Re7.2.Xa, judge Re9.1.Xa, connection Cn11.1.Xa, setting match
  Re7.2.Xb); codes and the mu-gX-respond skill added. Days 11, 75, 139 add one structure item (Re7.2.Xa). Units 1, 5
  and 9 sections name the rounds; process lines updated.
- **Expert 3** (retrieval and reteach minutes). Every unit's day 2 note (2, 20, 40, 52, 66, 84, 104, 116, 130, 148,
  168, 180): five minutes a row, reteach in the next day's warm-up and first five minutes (UNIT-PLAN rule 6). Each
  next day (3, 21, 41, 53, 67, 85, 105, 117, 131, 149, 169, 181) carries "Reteach slot". The .md readiness table,
  its paragraph and the mixed-grade line say the same.
- **Expert 4** (Re8.1.6a creators' part). Day 21 goal adds one choice Elgar wrote into the score beside one of du
  Pre's; day 37 goal adds one choice the composer made that both performers keep. Unit 2 section says so. Words-file
  check under "For the structure pass".
- **Expert 5** (once-a-week sitting budgets). .md Shorter path adds the minute budget for the merged 16+17 sitting
  (all three setting excerpts kept), unit 9's listening-first then sight-reading order with no playback during the
  groups, and the partner-pair showing for units 3, 7, 11. The table's "one item per id" cell now points to the budget.
- **Expert 6** (baseline look on fold-in days). Fold table: days 5, 23 (and spare 56) fold the baseline look into
  the next day's first practice time; a line covers the year 7 and 8 twins (69, 87, 120, 133, 151, 184).
- **Expert 7** (connecting told, not done). Days 41, 106, 168 goals add a student connecting line, note "practice,
  not a claim". Units 3, 7, 11 process lines name them.
- **Expert 8** (year 6 range). Unit 2 Candidate reversed to kept, no day cost: day 22 adds a short take by a living
  woman performer from Africa or the Arab world; note gives the unit plan's steps. Unit 1 Candidate adds the swap line
  for a school that leaves out the powwow study.
- **Expert 9** (sensitivity flags). Notes added on days 51, 115, 183; day 61's spoken item gains the leave-out route
  (the school assembly).
- **Expert 10** (order). Day 85 note (chord names wait for unit 7); day 181 retrieves mu-g8-read, note names day 134;
  days 59, 123, 187 notes keep post-dress-rehearsal changes small. The .md same-year retrieval line adds day 181.
- **Expert 11** (stale lines). For the lead item 4 replaced with the Music 3 to 5 check and its days; the readiness
  table cites those days (144, 158, 176, 192); MU:Pr4.2.8c dropped from the not-sampled list; the writer's "unsure"
  paragraph replaced with what the fix pass settled.
- **Lead call 1.** Shorter path rewritten: ten school days is about four sessions; four fold-in days a year (5, 11,
  23, 44; 140 minutes, 12 of 192 days over the band), six more listed as spares. The "ten sessions" reading dropped.
- **Lead call 2.** .md section renamed "The four processes": each year claims all four, a unit claims what the frame
  names, practice on an existing day claims no id. Checked by script: no day carries a code outside its unit's owned
  rows.
- **Lead call 3.** Not-sampled list kept with its reason; a line says naming is enough where the frame's table
  limits the sample.
- **Lead call 6.** Days 63, 127, 191 notes say the check uses new work with its own items after the concert; the .md
  Course-level checks section adds the rule.
- **Lead call 7.** Checked: no check cell re-asks items a unit gave one to three days before (mid-year checks carry
  the showing and program records; year-end checks carry the concert record unscored). The .md Collect once line
  says so. No frame change.
- **Lead call 8.** school_day formula stated once in the .md with its read-back week formula; every unit and check
  checked against the frame's weeks by script (all hold). Not re-counted to calendar.csv.
- **Lead calls 4, 5.** No change: band-wide school_day kept; no gate baseline sought.
- **Own 1** (rule 2, each part of each code). Day 191 claims MU:Cr2.1.8a (tension and release, unity, variety,
  balance) but asked only for the tension line. Goal adds one line on what the coda brings back (unity), what is new
  (variety) and where the tension is released. The checks table matches.
- **Own 2** (rule 2 re-run). Earlier-grade rows: all one grade back, retrieval, no readiness check (unchanged).
  Sampled codes per check: day 63 (Cr1.1.6a, Cr2.1.6b, Pr4.2.6b, Re9.1.6a), day 127 (Cr1.1.7a, Cr2.1.7a, Re9.1.7a),
  day 191 (Pr4.2.8b, Cr1.1.8a, Cr2.1.8a, Re9.1.8a), each part now asked. Collect once and end days hold. Our words:
  every new goal and note written fresh.

## Not applied

- **Band items.** No other arts expert read (docs/reviews/sequence-*-2026-11-26.md) has an "Across the band"
  section. The shared points those reads raise (task form, school_day count, the 10-days-short reading) are settled
  by the ARTS-FIX lead calls and applied above.
- **Frame year-end check cells** (finding 1). The finding asks for days.csv and the scope's table only; frame.md is
  unchanged. The new frame wording is under "For the structure pass".

## Settled

| Judgment | Reuse |
|---|---|
| Listening ids spaced by rotating five-minute rounds in rehearsal openers, codes added, no day added | Any arts unit whose response ids rest on one teaching day |
| Retrieval opener five minutes a row; reteach in the next day's warm-up and first five minutes, named "Reteach slot" | Every arts retrieval day |
| A folded fluency day's baseline look moves into the next day's first practice time | Every arts 10-days-short table |
| Four fold-in days a year plus spares for K to 8 twice-a-week arts | Lead call 1 |
| Connecting in a composing unit is a student line on an existing day, practice, no claim | Lead call 2 |
| Year-end checks after a concert meet the task-form rule with new work and their own items | Lead call 6 |
| A Cr2.1.8a item asks tension, release, unity and variety, each in a short prompt | Grade 8 composing checks |

## For the structure pass

1. **data/standards/ncas-performance-standards-words.txt**, MU:Re8.1.6a and MU:Re8.1.7a lines (expert finding 4):
   check against the national music handout; if it reads "creators' and performers'", restore that part. For 6a, old
   "Describe your reading of how elements and expression, within genre and history, convey intent.", new (if
   confirmed) "Describe your reading of how creators' and performers' use of elements and expression, within genre
   and history, conveys intent." (7a likewise). The scope already teaches the creator part on days 21 and 37.
2. **docs/courses/music-grades-6-to-8/frame.md**, Course-level checks table:
   - Year 6 year-end cell, old "a four-bar answer phrase composed and notated on a given two-chord pattern (MU:Cr1.1.6a,
     MU:Cr2.1.6b, unit 3)", new "a four-bar answer phrase composed and notated on a given two-chord pattern, its mood
     in one line and its A or B place in an ABA piece with the reason (MU:Cr1.1.6a, MU:Cr2.1.6b, unit 3)".
   - Year 7 year-end cell, old "with what stays and what changes named", new "with its expressive aim at the top, one
     decision that carries it named, and what stays and what changes named".
   - Year 8 year-end cell, old "a short introduction and coda written for a given eight-bar tune with its tension
     line", new "a short introduction and coda written for a given eight-bar tune with its tension line, its
     expressive aim at the top, one coda decision that carries it named, and one line on unity, variety and where the
     tension is released".
3. **data/plans/calendar.csv**: regenerate with `frame.py calendar` at commit (lead call 8); no school_day changed in
   this pass.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check music-grades-6-to-8`: 0 failures.
- `python -X utf8 scripts/frame.py check music-grades-6-to-8`: 0 failures (unit days by year 60, 60, 60; 12 units,
  192 days).
- `python -X utf8 scripts/frame.py calendar`: no break for this course; music 6 to 8 checks stay in weeks 19 and 32
  for grades 6, 7 and 8 (no frame or school_day change made).
- gate.py not run for a baseline (lead call 4).
