# Scope group fixes: dance, 2026-11-26

Fix pass on docs/reviews/scope-group-dance-2026-11-26.md (build/scope-writes/GROUP-FIX.md) for dance-grades-k-to-2,
dance-grades-3-to-5, dance-grades-6-to-8 and dance-grades-9-to-12. ARTS-FIX.md lead calls held throughout. Every
days.csv was edited with the csv module (quoting and line endings kept; the round trip was checked byte for byte
first). No unit, day count or owned row moved.

## Applied

1. **Safety wording (scope).**
   - K to 2 days.csv: the hazards block ("floor cleared and checked for spills and objects; bare feet or soft-soled
     shoes, never socks on a smooth floor; spots an arm's length apart; stop cue every session") added to the first
     day of units 2 to 4, 6 to 8 and 10 to 12 (days 21, 37, 53, 83, 99, 115, 147, 163, 179). The floor rule
     ("landings only on a level, resilient floor the school confirms; otherwise low and without impact, marked met
     only in a suitable space") added to days 137, 138, 140, 145 and 161.
   - K to 2 cue name: day 1 now says "The stop cue (freeze on the drum) is taught first today" and "stop cue every
     session"; days 6, 65 and 129 say "stop cue" (goals and notes). The same rename in scope-and-sequence.md (the
     every-day safety rules and the unit 1 arc) and in frame.md's unit 1 hazards cell, so the words the days copy
     match. The goal phrase "the freeze on the drum" (the move itself) stays.
   - 6 to 8 days.csv: a "Hazards and controls" line on day 113 (capoeira's kicks and sweeps not tried, no move aimed
     at a person, floor checked, water and rest) and day 163 (the frame's unit 11 words: revisions keep every unit 9
     rule, floor checked). The footwear rule added to each year's day 1 (days 1, 65, 129).
2. **9 to 12 leave-out (frame).** frame.md Leave-out bullet now also names unit 12 (Grace is set partly to spiritual
   music; Moon Water keeps every id met) and unit 14 (Birds with Skymirrors draws on Pacific ceremony and is watched
   only; Creole Giselle and Admiring La Argentina keep every response id met).
3. **Butoh (scope).** 6 to 8 day 5 note now reads as the read's fix (white-powdered bodies named as the form's look,
   teacher previews, students wear no paint); day 69 points back to it.
4. **Tools card (scope).** 6 to 8 day 23 goal: "retrograde (the reverse of the grade 3 to 5 tools card)". 9 to 12
   day 5 keeps its four tools; its note adds "A student from dance 6 to 8 also knows accumulation; it stays a choice
   on the card." The 9 to 12 frame's bridge table (line 275) already lists the same four and needs no change.
5. **Trisha Brown (scope).** 6 to 8 day 147 goal: "Trisha Brown, one of its members (a class that took dance 3 to 5
   met her Accumulation and Roof Piece), now for group improvisation." The frame's line 92 ("met again as a member of
   Grand Union", naming 3 to 5 as the source) is a cross-band statement and stays.
6. **Reteach (scope).** "For a student new to the band or meeting this year first, the ten minutes are the reteach of
   the earlier step." added to K to 2 days 84, 100, 116, 130, 148, 164, 180 and 3 to 5 days 66, 82, 100, 118, 130,
   147, 166, 182.
7. **PE lean (scope).** 6 to 8 day 140 note and the scope's lean table now say physical education grade 8 unit 18 is
   a planned week of routines, dance among them, weeks 12 to 14 (checked against data/plans/calendar.csv: course days
   231 to 238, school days 58 to 69). The same stale fact sat twice in 6 to 8 frame.md (the unit 9 row's "Why this
   unit" cell and the lean table row, which also said course days 233 to 240); both corrected to weeks 12 to 14 and
   course days 231 to 238, since leaving the frame contradicting the days would be worse. Order still holds (dance
   unit 9 is grade 8 weeks 1 to 9).

## Rejected

- **Finding 6, K to 2 day 66 only.** The note already says "In a mixed class meeting year 1 first, it becomes a
  ten-minute reteach of the earlier steps." Nothing added; the other 15 days were fixed.

## Skipped (not this pass)

- **Finding 8** is in physical-education-grades-6-to-8 day 276; the physical education fix pass handles it. No dance
  file changes (dance 6 to 8 day 113 and its lean table already name the return correctly).
- **Finding 9** is a CALENDAR.md note the lead writes (the weekday inside a week is a placeholder). No CSV change.

## For the structure pass

- None. The read tagged no finding structure.

## For Cory

- None. The read tagged no finding Cory.

## Checks

| Course | sequence.py check | frame.py check |
|---|---|---|
| dance-grades-k-to-2 | 0 failures | 0 failures |
| dance-grades-3-to-5 | 0 failures | 0 failures |
| dance-grades-6-to-8 | 0 failures | 0 failures |
| dance-grades-9-to-12 | 0 failures | 0 failures (notes only: units 17 to 19 own no standard, by design) |

Defects logged with scripts/plan.py defect: 15 fixed, 1 rejected, across the four courses (made-at scope, found by
expert).
