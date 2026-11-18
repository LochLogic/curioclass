# Fix: english-language-arts-grade-11 unit 2 (s02.md), 2026-11-17

Findings merged: 30 (assessment 10, sources 10, sequence 10; no two named the same fault). Fixed 24 (some in part), rejected 4, lead 6 (some overlap with fixed). Held up: assessment 10 of 10, sources 9 of 10 (one sent to LEAD in part), sequence 8 of 10.

Gate: `python -X utf8 scripts/unitplan.py check english-language-arts-grade-11` PASS for s02.md (word count held at the cap by writing fixes short).

Fixed: assessment 1 to 10 (day 19 rage/indignation item and locator, day 20 key, day 33 hyperbole item with N rewritten as a figure read literally, day 25 transfer exit, day 31 two-part exit with new letter S, scored-version sentence, not-scored line, group-to-letter line, B wrong answer, 2 minutes for directions on day 33). Sources 1 to 4, 5 (Te Ara removed), 7, 8, 9 (editions as shown on each page), 10. Sequence 2, 3 (ledger placed; supplies line not extended, over cap), 4 (sentence added), 5, 6, 7, 9 (3 minutes relabelled as the word-family slot).

REJECTED: sequence 1 | Reading load: add per-block words and mode to field 2, a ten-minute limit on day 17 and 12 on day 24 | Only the minute limits were added in part; the per-block word, mode and second-pass table would add well over 100 words and the unit plan sits at the 1,250 cap, so the rest is left to section and day plans | over the word cap (UNIT-PLAN Length) and field 5 pacing left to day plans
REJECTED: sequence 8 | Add a three-minute device rule check to day 25 | Written then removed to stay inside the word cap; the W.6 rotation start is a day-plan detail | over the word cap (UNIT-PLAN Length)
REJECTED: sequence 10 | State in field 3 that unit 3 opens with retrieval only and reuses Thoreau | Written then removed to stay inside the word cap; days.csv shows unit 3 (day 35) has no readiness mark and day 34 no assess value, so the plan is already consistent | over the word cap (UNIT-PLAN Length)
REJECTED: sequence 3 (supplies part only) | Add idea chart, clause-marking copies, term trail and ledger to the field 8 supplies line | Placement of the ledger was fixed; the supplies line was not extended | over the word cap (UNIT-PLAN Length)

Also not applied from sources 3: the Gutenberg 34920 link was dropped, not kept, because its title page could not be confirmed.

LEAD:
- Sources 5: add one free museum or library page on the Alcott family's Fruitlands experiment, with the content note it supports (needs a checked link).
- Sources 6: add one free citable page each for the 1846 to 1848 war and Thoreau's night in jail (Library of Congress or National Park Service), and name which bridge sentence each supports; none could be verified here.
- Sequence 4: add ~RL.11-12.10 to the codes of days 24 and 25 in days.csv (the plan now says Alcott gives it first practice).
- Sequence 1: if the reading load cannot fit, days.csv may need a stated pre-reading assignment or a split of day 21 or 24; the word counts per block belong in section plans.
- Sequence 8: day 25 device rotation start (rule check) belongs in the section or day plan.
- Assessment 7: name the later unit and day where L.4b, SL.1a to d, L.3a, L.6, RL.10 and RI.10 are assessed (scope-and-sequence); the plan now says only that they stay formative here.
- Sources 1 to 4: the four Wikisource links return 200, but the lead should confirm the print edition each page names (Emerson edition is not yet named in field 10) before the lead copies edition data into ela-texts.csv; also ela-texts.csv edition cells now differ from field 10 (Thoreau and Alcott edition notes).
- Line endings: the file was CRLF when this stage began; it is now LF.
