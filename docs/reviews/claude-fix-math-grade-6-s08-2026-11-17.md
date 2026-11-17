# Fix: math-grade-6 unit 8 (s08), 2026-11-17

Findings merged: 13 (assessment 6, sources 3, sequence 4). Fixed: 12. Rejected: 0. Lead: 3 items (below).
Held up per lens: assessment 6 of 6, sources 3 of 3 (two fixed in the plan, one is a lead), sequence 4 of 4 (all fixed in the plan; two also leave a days.csv lead).
Gate: `python -X utf8 scripts/unitplan.py check math-grade-6` PASS for s08.md.

Changes: field 7 marking (feedback timing made consistent); E142, E143, E152, E153, E154 rewritten as the lens asked (E154 calculations made optional); day 145 retrieval prompt labelled invented; field 2 Carried and Balance (withdrawal of dot plots corrected, units/attribute kept in use from 144, 5d on day 150 stated as a link only); field 8 day-use line added; field 10 sentence that unit 8 uses only invented data.

REJECTED: none

LEAD:
- Sources 2: remove the pointer "See 'For the lead' item 5" from the skeleton text (unit_skeleton.py or the frame row feeding the hazard cross-subject line); it sits inside a skel block.
- Sequence 2: days.csv supplies column for days 142, 144, 148, 150 and 153 (and strips on 142 and 149) should name the ruler, strips, printed dot plots, counters, data cards and number cards.
- Sequence 4: days.csv may drop 6.SP.B.5d from day 150.
