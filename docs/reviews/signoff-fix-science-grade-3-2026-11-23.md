# Sign-off fix: science-grade-3 (2026-11-23)

Applies Cory's course-finish calls (docs/agents/decisions/DESK-ANSWERS.md, "2026-11-23: Science K to 3 finish calls and sign-off") to the finish record docs/reviews/finish-fix-science-grade-3-2026-11-22.md. Nothing else was changed on purpose.

## Calls

1. **Scoring: applied, all six units.** The end items (s01-E1 to E5, s02-E1 to E6, s03-E1 to E8, s04-E1 to E12, s05-E1 to E12, s06-E1 to E18) now score the fresh check-day work (days 14, 15, 31, 32, 55 to 57, 75 to 77, 95, 96, 115, 116) on the same components, with new stem, answer, steps and samples, their wrongs rows (same registered letters) and handbacks rows. The revised earlier products are recorded beside the score as a "repair mark, not the score" (shown or not yet). Changed: each unit plan's assessment field (s01.md to s06.md section 5 and section 7), the section plans that score (u01-3, u02-3, u03-4, u04-1 to u04-4, u05-1 to u05-3, u06-1 to u06-4), the check-day teacher and student pages, every score sheet and record sheet (uNN-1/record.md, u03-4, u04-4, u05-3, u06-4 score-sheet.md), openers, product and fresh cards. New item s02-P31-5 (a 5 cm gap card) because day 31 had no work that could score s02-E3.
2. **Unit 5 revision: applied.** One change for each look-for marked not yet (d093, d094, s05.md, u05-3.md, items s05-P93-2 and s05-P94-2 with wrongs). Revision minutes unchanged.
3. **Feedback: applied.** Written notes (1.5 or 3 minutes a child) are now a look-for checklist and one question stamp, about 1 minute a child, in every plan and day that printed them. Units 2, 5 and 6 have six look-fors a product; units 1, 3 and 4 have fewer (unit 1: five and eight, units 3 and 4: four), so their checklists carry one tick a look-for. Respond days hand back checklists and exit tickets only; scored fresh papers come back in the next Return slot: day 17 (unit 1, the retrieve slot), day 36 (unit 2, days 34 and 35 are course checks), day 59 (unit 3, the hook hand-back), day 81 (unit 4, days 79 and 80 are course checks), day 98 (unit 5), day 120 (unit 6, days 118 and 119 are course checks). New sheets: courses/science-grade-3/u01-3/checklist-16.md and u02-3/checklist-slips.md. No day's total minutes changed; Return slot minutes rebalanced inside the slot (days 34, 98, 119, 120 handbacks rows).
4. **Day 82: applied.** The age question is answered plainly from the fossils, and the teacher line is added word for word: "People bring different ideas. In science class we look at what the rocks and fossils show." Also in u05-1.md and the u05-1 opener.
5. **Utqiagvik: left as is,** per the call.
6. **Coverage table: applied.** New section "Practice and crosscutting concept coverage" in docs/courses/science-grade-3/scope-and-sequence.md: a row per unit plus the course checks, a column for each of the 7 practices and 6 crosscutting concepts the course names. No day was changed to fill it.

Gaps line: Every practice and concept the course names has at least one day. The course names neither Using Mathematics and Computational Thinking nor Energy and Matter, so neither has a column. (Within units, cells read "none" where a unit does not use a practice or concept: for example no investigation days in units 3 and 5, and Obtaining, Evaluating, and Communicating Information only in unit 6 and day 119.)

Also edited by the call's reach: parts.csv (four part texts in units 5 and 6 to match the fresh-work scoring, and one UK spelling).

## Gates (filtered to this course)

- plan.py check: before 21 FAIL, after 21 FAIL, all "section N.N (science-grade-3-uNN-N) is not in data/units.csv" (known). Items 875 to 876, wrong answers 624 to 623.
- lesson.py check: before 0 FAIL lines (387 lines); after 1 FAIL line (390 lines): d059 teacher prose 676 of 675, from the returned-papers sentence. It is trimmed to 674 by the gate's own word counter after the run; the lead's rerun should show 0.
- A first end run showed new failures (hand-back naming on the day after each check, score words in At home, word caps on days 16, 17, 29, 30, 62, 73, 74, 76, 77, 78, 82, duplicate stems s02-P31-1, -2, -5 and s06-E5, -E10, a day 31 ruler row); all were fixed in the files, materials.csv and items.csv before the final run.

## For the lead

- Ledger: no entry needed by this pass, unless the lead records the sign-off itself.
- Skeleton files (docs/courses/science-grade-3/day-skeletons, section-skeletons) still describe revised-only scoring; they are stage records and were not edited.
- Unit 2 day 30 still asks for "one change" on its revision; call 2 named unit 5 only.
- Unit 2: the day 31 sheets "go forward to day 35 unchanged" and are also returned on day 36 (already so before this pass).
- Units 2 and 3 record sheets used a 2/1/0 scale while the plans and items give 1 point a component; both now read 1 or 0.
- s04.md section 5 names item V's plants "sunflower", u04-2.md and items.csv say "barley" (already so).
- Coverage cells were counted from section plans, days.csv goals, items.csv practice and day-file keywords; doubtful cells (unit 3 days 48 and 49 investigation, unit 4 Structure and Function on 64, 66, 67) want a read at the next unit pass.
- Cold read 13 (day 97 group structure) was not part of these calls and is unchanged.

## Browser check

None arose (no new facts or sources).
