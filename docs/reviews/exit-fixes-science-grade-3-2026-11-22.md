# Exit fixes, science grade 3, 2026-11-22

Ten exit faults, all applied (none rejected). Each new exit item is a new case, invented for practice, answered cold, with a key, a wrongs row tied to a registered error, and the handbacks row and card file updated.

- Day 3, applied: s01-X3 now asks the child to write Mia's plan for a toy car (change, keep the same, watch); the old fair-or-not judgment is gone. Day text, card, unit plan E3a updated.
- Day 4, applied: s01-X4 now asks the child to draw the arrows again for a boat that moved toward the left bank (the left arrow longer). Day text, card, unit plan E4a updated.
- Day 26, applied: s02-X26 now asks for two checkable criteria and the limits for a paper-sign stand problem (6 tokens, 5 minutes). Wrong: materials and a liking (E).
- Day 27, applied: s02-X27 now asks for one criterion to change after a bag-hook trial, with its reason (D wrong: three changes at once).
- Day 42, applied: s03-X42 now asks what stage comes next on a radish packet card when the class is on day 15 (roots ready on day 28, 13 days away). The Max claim became the spoken s03-X42b.
- Day 43, applied: s03-X43 now asks why three kittens are alike yet different, using trait and inherited (F wrong). The fox picture stays as the spoken s03-X43b, which now carries the G repair (2 minutes) in handbacks.
- Day 53, applied: s03-X53 is now a written revision, not a tick sheet: each child picks one record that misses a look-for and revises it in a second color. Record 3 work is 6 minutes (was 7) and the exit is 3 minutes inside the same 10-minute part; day total unchanged. Goal map row 53 in s03.md now reads "Revises one of own three records against its look-fors in a second color".
- Day 59, applied: s04-X59 now asks the child to draw a field mouse and a link line to each thing it needs in a meadow. The pond turtle question moved to a new spoken s04-X59b with the F and G repairs (2 minutes each); X59 F carries 0 minutes. Day header set to `exit: half`.
- Day 82, applied: s05-X82 now asks the child to draw the hill long ago from a fish print and a shell print and label what each shows (A wrong: always a dry hill). Header `exit: half`; day 83 repair note updated.
- Day 100, applied: s06-X100 now asks the child to draw a picture graph or bar graph, key first, for new counts (May 9, June 3, July 6). Spoken s06-X100b (bar read) unchanged. Header `exit: half`; day 101 repair example changed from umbrellas to clouds.

Files touched: data/plans/science-grade-3/items.csv, wrongs.csv, handbacks.csv; day files d003, d004, d026, d027, d042, d043, d053, d059, d082, d100, d101; the exit card files of units 1.1, 2.2, 3.2, 4.1, 5.1, 6.1; unit plans u01-1, u02-2, u03-2, u04-1, u05-1, u06-1; s03.md goal map. No sources needed (all new cases are invented for practice).

Left alone: docs/courses/science-grade-3/day-skeletons/ still holds the old exit text for these days (generated files, not regenerated here).

## Gates

- plan.py check (course filter): before 118 FAIL lines, after 118 (21 failures in the course summary both times; a one-ask failure on s02-X27 that my first stem caused was fixed).
- lesson.py check (course filter): before 0 FAIL lines, after 0 (an interim run showed word-cap and one-sentence-length failures from the longer exit paragraphs; trimmed).
