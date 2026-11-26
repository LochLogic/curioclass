# Fixes: scope and sequence of library-and-research-skills-grades-6-to-8, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-library-and-research-skills-grades-6-to-8-2026-11-26.md),
under build/scope-writes/AFTERCORE-FIX.md. The Codex read waits for Codex's usage reset (after 2026-11-30) and gets its
own small pass then.

Counts: applied 21 (expert 18 finding parts across all 8 findings, lead calls 3); not applied 1 (expert 8, the gate
note, by lead call 12). Band items from the other library reads: none touch this course (the K to 5 reads' cross-course
items are all K to 5 talk turn and card wording). Defects logged: 20 fixed, 1 rejected.

## Applied

- **Expert 1a** (scope-and-sequence.md, Shorter path): the 35-minute period now names where each day's 5 minutes go:
  day 5 drops its one-answer items, days 28 and 45 cut their earlier-unit sample to one item, show-me days give one
  fewer practice try; the self-check move on inquiry days stays.
- **Expert 1b** (.md): the day 52 fold is dropped; day 52 holds the change lines day 53 scores. Grade 8 keeps the day 44
  fold.
- **Expert 1c** (.md): total restated as four sessions, about 115 minutes, 54 days in 50; day 21's move is an optional
  trim, not a fold.
- **Expert 2** (.md, A left-out unit): bridges for units 1, 3, 4 and 8 added, unit 5 extended (day 31, day 38), and
  the check rule for a left-out unit (an end-of-unit check keeps only its earlier-unit samples; any check drops items
  sampling a left-out unit; the family note names the ids).
- **Expert 3** (days.csv 11, 39, 40, 45, 53; .md units 2, 7, 9; frame.md check cells 1, 5, 6 and unit 7 evidence):
  day 11's lateral item asks VI.A.3 in three prompts; days 39 and 40 add "how what I expected shaped what I looked
  for"; day 45's unit 7 sample marks four findings; day 53's views sample adds one finding per view from a short set.
- **Expert 4** (days.csv 25, 27; .md unit 5; frame.md unit 5 Days cell and the ELA grade 7 seam cell): the fishbowl
  rotates so every student practices both turns; day 27 marks two things per student, the teacher sits with each
  group about five minutes, and a turn slip (teacher-judged) covers students not heard live.
- **Expert 5** (days.csv 3, 9, 14, 21, 26, 32, 33, 39, 43, 49; .md new "skill card and the strip" bullet and unit 6
  arc): the card is withdrawn for practiced moves; the move shown last session keeps a one-line strip for that session;
  the response log strip runs through day 33's first half. Day 26 says its last-shown move (the discussion) is used on
  day 27, after the rotating fishbowl.
- **Expert 5, frame item** (frame.md unit 6 Days cell, under call 7): the response log strip through the next
  session's first half.
- **Expert 6** (days.csv 47; .md unit 9 Leans; frame.md social studies grade 8 seam cell and unit 9 "Why" cell):
  social studies teaches its own news check (civics unit 9, weeks 27 to 29) and assumes no library row; a class with
  both meets the method twice.
- **Expert 7** (days.csv 9, 11, 43; .md checks paragraph; frame.md unit 8 host): day 43 and the frame say a modern
  image is usually still under copyright unless its license or maker says otherwise (US works published before 1931
  are public domain); day 9's key records "evidence mixed", never "false"; day 11 says 11 weeks; the checks paragraph
  says 8 to 23 weeks.
- **Expert 8** (days.csv 15, 33, 47, 51; .md): day 47's team talk rules start from SEL's grades 6 to 8 talk turn card;
  teacher written feedback on days 15, 33 and 51 is written between sessions and handed back at the start.
- **Lead call 4** (frame.md units 4 and 7 host cells and the host paragraph after the Cross-subject tables): the ELA
  hosts' weeks are named and the cells say the inquiry day falls in week 6, so the stand-alone question carries it
  unless a school runs ELA's unit earlier. The scope's For the lead item 1 is dropped.
- **Lead call 5** (frame.md unit 9 Days cell): the second day reads "show-me and practice (the question sort by kind
  shown; ...)", matching GLOSSARY and day 48's Understanding kind.
- **Lead calls 2 and 12** (.md For the lead): the source-map item is answered "waits on L149" and the None note is left;
  both dropped from the list, which keeps only the grade 6 readiness record.
- **Own re-run of rule 2**: begun ids are all `~` (call 8); no grade 7 or 8 first day holds a readiness check (call 14
  needs nothing); the earlier-unit samples at checks 3 and 5 now sit 10 and 8 weeks after their sittings and the
  year-end ones about 22 to 23; Collect once holds (II.C.1 from day 27, the pair chart from day 43, the logs from
  days 33 and 52, each re-used, not re-collected, inside two weeks). No new defect found.

## Not applied

- **Expert 8, the "standard None is on no day" note**: left as it is (lead call 12); logged rejected.
- **Expert, For the lead: the g8-news-lateral row note** in data/progressions/library.csv is not this pass's file; it
  is under For the structure pass.

## Settled (for DIGEST)

| Judgment | Reuse |
|---|---|
| A strip keeps the line of the move shown last session on its first inquiry day; sittings run bare | Every low-dose inquiry course where the last show-me falls the session before the inquiry |
| A scored discussion in groups: two marks per student, a five-minute teacher visit per group, a turn slip the teacher judges | Any scored group talk with one teacher |
| Practice before a scored discussion rotates so every student takes the scored turns | Fishbowl practice days |
| A fold-in never takes the day an assessed line is written | Every reduced path |
| A leave-out bridge for every later use of a unit's card, plus the check rule (keep earlier-unit samples; drop items on the left-out unit) | Every band course |
| Modern images: "usually still under copyright, unless its license or maker says otherwise" | Fair use days in any course |
| A mixed-evidence case's key records "evidence mixed" and rewards the moves | Lateral reading keys |

## For the structure pass

- data/progressions/library.csv, row g8-news-lateral, note: old "the second course opens with a retrieval task on the
  first"; new "where library comes second, its day opens with a retrieval task on social studies' news check; social
  studies assumes no library row (lesson 32)".
- scripts/sequence.py: skip a literal "None" owned-standards cell (the unit 4 note; the grade 5 read raised the same).
  Lead call 12 says leave it; listed only so the one gate fix covers both courses if the lead takes it.
- Lens spellings (lead call 13): none checked in this pass; any UK spellings in docs/agents/lenses/library.md are the
  lead's.

## For Cory

None. The expert's fixes fit inside the 18 sessions a year (the dose option, frame For the lead item 2, is not
triggered).

## Gates

- `python -X utf8 scripts/sequence.py check library-and-research-skills-grades-6-to-8`: 0 failures; one note, "unit 4:
  standard None is on no day" (lead call 12, left).
- `python -X utf8 scripts/frame.py check library-and-research-skills-grades-6-to-8`: 0 failures; the per-unit notes to
  name begun codes in What students learn (each already named with its later owner) and the day count notes.
- `python -X utf8 scripts/frame.py calendar`: no break printed; library grades 6 to 8 sit on weeks 20/31, 18/31 and
  16/31, unchanged (no frame edit moved a unit or a check).
