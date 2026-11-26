# Fixes: scope and sequence of visual-arts-grades-6-to-8, 2026-11-26

Fix pass per build/scope-writes/ARTS-FIX.md and docs/pipeline/briefs/sequence-fix.md. One read so far: the Claude
expert read docs/reviews/sequence-visual-arts-grades-6-to-8-2026-11-26.md. The Codex read waits for Codex's usage
reset (after 2026-11-30) and gets its own small fix pass; the brief's Codex and 2026-11-15 lead-call items are skipped.
Files changed: docs/courses/visual-arts-grades-6-to-8/scope-and-sequence.md and
data/plans/visual-arts-grades-6-to-8/days.csv. frame.md is unchanged (no finding asks for a frame change).

**Counts.** Applied: expert 11 of 11 findings (every sub-item) and 15 of 15 "Settled by the expert" rows; lead calls
8 of 8 (4 needed no change); band items 2 of 2; own 3. Not applied: 0 from the expert; 1 expert item kept as the
expert's own table sets it where the read contradicts itself (see Not applied).

## Applied

- **Expert 1 (once-a-week path).** scope-and-sequence.md, each unit's "Once a week" line regrouped exactly as the
  expert's table: unit 1 (1-2, 3-4, 5-6, 7-8, 9-11, 12-14 with day 14 cut to a ten-minute look), unit 2 (27-29, day 30
  dropped), unit 5 (73-75, 76-77, 78-79, day 80 dropped), unit 6 (85-87, 88-89, 90-91, 92-94), unit 9 (135-136 with the
  drill as opener, 141-143 with day 142 cut to a ten-minute look, day 144 dropped), unit 10 (155-157, day 158 dropped),
  unit 11 (174 alone, day 175 dropped), unit 12 (179-181, 182-185, 186-188). Session counts still match the frame
  (8, 8, 6, 6; 9, 7, 6, 6; 9, 7, 7, 5). Shorter path "Once a week" bullet now says a "nothing scored" practice day is
  dropped, never folded into a check day, and no session holds more than three days. days.csv notes of days 30, 80,
  144, 158, 175 say they are dropped on the once-a-week path and the short year.
- **Expert 2 (create in show units).** days.csv notes 55, 118, 185: create is real making, checked on the same band's
  design look-for (unit 3 design brief, unit 7 hierarchy, unit 11 pictures-and-words grid) as practice of VA:Cr2.3.6a,
  .7a, .8a that returns, never a claim (no code added to those rows), with the daily evidence line "what technique I
  used and what I will change". Units 4, 8, 12 "Four processes" lines say the same.
- **Expert 3 (practice before the unseen item).** days.csv: day 45 opener (second work card, VA:Re8.1.6a); day 53 (the
  three-column chart on a second set, VA:Pr4.1.6a); day 110 last 15 minutes (VA:Re8.1.7a, VA:Re9.1.7a on a Curio Class
  card); day 184 (two works sorted, VA:Cn11.1.8a). Each partner-marked, nothing scored; each code is the unit's own, so
  it was added to that day's `codes` and its row to `skills`. Units 3, 4, 7, 12 "Assessments" lines name the slot.
- **Expert 4 (check-day budgets).** days.csv day 191: a 10-minute VA:Cr3.1.8a item and a 17-minute argued paragraph
  whose evidence carries VA:Re8.1.8a; note gives the minutes (3, 5, 27 = 10 + 17, 3, 2). Year 8 year-end section says
  the same. Shorter path "Shorter periods": the 30-minute check day is self-check the session before, set-up 2, sitting
  25, collecting 3, every prompt per part kept and sized to 25 minutes.
- **Expert 5 (first met in independent work).** days.csv day 168 kind Application to Understanding, goal opens with the
  panel-and-grid method in steps on a step card (squaring a thumbnail onto panels, edge marks, shared color plan); day
  37 goal opens with the teacher gathering four ideas aloud. Unit 3 and unit 11 sections name both.
- **Expert 6 (same-year retrieval).** days.csv day 38 `retrieves` va-g6-ideas; va-g6-revise and a ten-minute opener;
  day 105 `retrieves` va-g7-ideas and an opener. Units 3 and 7 Retrieval lines updated.
- **Expert 7 (respond-day labels).** days.csv: all 18 Respond-kind rows now open "Respond day; processes of the parts
  redone: ..." naming creating, presenting, responding or connecting per part redone (the expert counted 24; the file
  has 18 Respond days, all changed). Every unit's "Four processes" line lists the respond day apart ("respond day 16")
  and drops it from the process lists; a new "The four processes" bullet in How the course runs says a respond day is a
  day kind, not the responding process.
- **Expert 8 (logic model).** scope-and-sequence.md: column heading "Outcome sought"; the frame's not-tried sentence
  added under the table.
- **Expert 9 (parts of codes).** days.csv day 63: the student picks one of three questions or writes their own, marked
  the same (VA:Cr1.2.6a both parts). Days 134, 140, 145: the risk log adds "one thing I invented", and the day 145
  VA:Cr2.1.8a look-for names the planned risk and the invention. Year 6 year-end and unit 9 sections say so.
- **Expert 10 (rotations).** How the course runs, Rotations bullet replaced with the frame's two sentences (64 meetings
  full path; quarter rotation of about 40 meetings runs the 32-session path).
- **Expert 11 (stale items).** For the lead 2 (STANDARD.md 3.4) and 4 (school_day convention) deleted; For the lead 3
  (supplies) moved to a new "For Cory" section as a money pick; unsampled count 30 corrected to 27 (and 18 sampled
  stated above the table); day 30 note "seven weeks after its end (week 8 to week 15)"; Calendar bullet states the
  result (0 failures, no stagger break, 2026-11-26); year headings name "15 ids".
- **Lead call 1 (10 days short).** Already 4 named days a year in one reading (4 sessions, 160 minutes); the practice
  days among them (30, 80, 144, 175) now drop rather than fold into a check; drill days 10, 24, 53, 74, 103, 117, 135,
  165 fold into the next day (day 53's chart practice moves to day 54's opener).
- **Lead call 2 (four processes).** New "The four processes" bullet: every year touches all four, each unit at least
  the processes its frame row names, a unit need not claim all four, and practice of another process claims no id
  outside the unit's owned rows. No unit's claims were stretched; the expert-3 slots are practice on existing days.
- **Lead call 3 (unsampled codes).** The table names all 27 with reasons and now says naming them is enough where the
  frame's check table limits the sample. No frame change proposed.
- **Lead call 4.** No gate baseline touched.
- **Lead call 5 (school_day band-wide).** Kept 1 to 480 band-wide; the .md says so.
- **Lead call 6 (task form, two weeks).** No change needed: no course-level check is a showing, and each course check
  that samples a code given in a unit check uses new items on a new work at least seven weeks later (days 63, 97, 127,
  161, 191 checked).
- **Lead call 7 (Collect once).** No change needed: each year-end check draws on units before the show unit and carries
  the show unit's record unscored; each mid-year check carries the second unit's record (given two days before)
  unscored, as written.
- **Lead call 8 (school_day formula).** The .md states the formula once (160 x y + ceil(2.5 x n)) and the week rule
  ((school_day - 1) // 5 + 1, band-wide); every row matches the formula, and every check falls in week 17 or 32 of its
  year (checked by script).
- **Band item (visual arts 3 to 5 read, finding 7, fold days and the baseline).** Short-year bullet now says none of
  the fold or drop days holds a unit's baseline look (baseline days listed), so no rotating group goes unobserved.
- **Band item (visual arts 3 to 5 read, finding 8, one school_day count).** Settled by lead call 5; this course already
  counts band-wide.
- **Own 1 (rule 2 re-run).** Re-ran by script: all 45 codes on days of their own year only, each taught before its one
  end-of-unit check, 18 sampled on course checks, retrieval rows one grade back or same year, no readiness check
  needed, day 1 of every unit clean. No new defect.
- **Own 2.** Day 191 note says its items are new items on a new work, sized to the 27-minute sitting.
- **Own 3.** Day 110 processes line adds respond and day 184 adds connect, matching the new practice slots; units 3, 7
  and 12 process lists updated to match.

## Not applied

- **Expert 1, the "critique and revision do not share a session with the showing" clause.** The read's own table keeps
  units 3 and 7 as written (44 to 46 and 108 to 110 are critique, revision and showing in one three-day session). I
  followed the settled table and wrote the global rule as "no session holds more than three days", naming units 3 and
  7 as the expert's exception. The lead may want to settle whether units 3 and 7 should split (see For the structure
  pass).

## Settled (for DIGEST)

| Judgment | Reuse |
|---|---|
| A practice day marked "nothing scored" is dropped on the once-a-week path and the short year, never folded into a check day | every arts band scope |
| A show unit's create claim is carried by checking its presenting product on an earlier unit's design look-for of the same year, as practice with no code added | arts show units |
| A ten-minute practice slot of a unit's own code on an existing day may add that code to the day's `codes` (it is owned by the unit) | arts response codes |
| Respond-day notes name the artistic process of each part redone; respond days are listed apart from the four processes | every arts scope |
| school_day formula 160 x y + ceil(2.5 x n), week band-wide (school_day - 1) // 5 + 1 | K to 8 arts band courses |

## For the structure pass

1. docs/pipeline/briefs/sequence-write.md (or build/scope-writes/ARTS-BRIEF.md), the arts once-a-week merge rule, add:
   "On the once-a-week path and the short year a practice day marked nothing scored is dropped, never folded into a
   check day (a check day has two spare minutes); no merged session holds more than three days." (expert's For the
   lead item 2).
2. build/scope-writes/ARTS-BRIEF.md, "The four processes" bullet, old: "(create; perform, present or produce; respond;
   connect) appear in every unit's days"; new: "(create; perform, present or produce; respond; connect) appear in each
   year; each unit touches at least the processes its frame row names, and practice of another process claims no id
   outside the unit's owned rows" (lead call 2).
3. docs/courses/visual-arts-grades-6-to-8/frame.md line 188, logic model, optional for agreement with the scope: old
   "Outcome claimed:"; new "Outcome sought:" (expert finding 8 changed only the scope).
4. Lead decision: units 3 and 7 once-a-week sessions 44 to 46 and 108 to 110 hold critique, revision and showing
   together, against the expert's general fix rule but inside the expert's settled table. If they should split, the
   frame's session counts (6 each) leave no room, so the merge would move to 41-43 / 44-45 / 46 and need the frame's
   understanding-day merge rule.
5. Lead: log expert findings 1 to 11 with `plan.py defect`, found_by `expert` (the read could not).
6. docs/courses/CALENDAR.md: document the band-wide school_day count (lead call 5, the lead's own item).

## For Cory

- Supplies ceiling (money), already open from the frame: $100 a class of 30 a year, every unit with a free path.
  Nothing new.

## Gates

- `python -X utf8 scripts/sequence.py check visual-arts-grades-6-to-8`: 0 failures.
- `python -X utf8 scripts/frame.py check visual-arts-grades-6-to-8`: 0 failures (unit days 60 a year; 192 days).
- `python -X utf8 scripts/frame.py calendar`: no failure printed; this course's grade 6 to 8 arts weeks are 17 and 32
  in every year, no stagger break (frame unchanged, so the structure pass's calendar regeneration needs nothing new).
