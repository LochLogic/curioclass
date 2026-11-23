# Sign-off fixes: Science, Grade 2 (2026-11-23)

Cory's calls from docs/agents/decisions/DESK-ANSWERS.md, "2026-11-23: Science K to 3 finish calls and sign-off", applied to science-grade-2.

## Calls

- Day 12, Mount St. Helens line: applied as no change. courses/science-grade-2/u02-1/d012.md still reads "yes, some people were" with no number.
- M2 and L2 wording: applied as no change (stays as written).
- Day 46 table: applied as no change (stays).
- Day 45 minutes: applied. The scope now sets day 45 at 38 minutes (3 directions, 12 observation windows, 3 moves and pack up, 20 accounts), inside the course's 35 to 40. Files: data/plans/science-grade-2/days.csv (day 45 note names the three minutes of directions and the 38 total), docs/courses/science-grade-2/scope-and-sequence.md (observed-action paragraph), docs/courses/science-grade-2/s04.md ("Day 45 totals 38 minutes", plus the day list copy of the note), and the note's copies in docs/courses/science-grade-2/u04-2.md and day-skeletons/d045.md. The day file was already 38 minutes; no day's minutes changed. Unit 4 totals check: day files 39, 40, 39, 40, 40, 40, 38, 40, 35 minutes (days 39 to 47), all inside 35 to 40; day 45's check_min sums to 38. No item, key, wrong or hand-back changed.
- Coverage table: applied. New section "Practice and crosscutting concept coverage" in docs/courses/science-grade-2/scope-and-sequence.md: one row per unit plus the mid-year and year-end checks, eight practice and seven crosscutting concept columns (the frame's "Practices across the year" list), each cell the days that use it. No day was changed to fill it.

Coverage gaps line: none; every practice and crosscutting concept the course uses has at least one day.

## Gates (science-grade-2 lines only)

- plan.py check: 17 FAIL before and 17 after (16 known "section ... is not in data/units.csv", 1 known template point s02-E11/E12 same numbers). The only changed line is a note: s04.md prose went from 5179 to 5195 words.
- lesson.py check: 0 FAIL and 20 NOTE, before and after (no change).

## For the lead

- s04.md still says "Day 46 totals 35 minutes", but the day 46 file and check_min run 40 (5 + 12 + 3 + 5 + 15). Inside the frame; not one of Cory's calls, so left.
- The coverage table is a reading of the plans and days by one agent; asking questions and argument are the thinnest columns (one or a few days a unit).
- Ledger: no entries needed (no item or day kind changed).
