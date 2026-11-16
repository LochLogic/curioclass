Merged: 5 distinct findings, no duplicates. Changed only `docs/courses/biology/s04.md`.

Fixed 3:
- Item 1 requires both balanced budgets for budget credit; its Meets sample now gives all outgoing atom totals.
- Item 2’s energy point requires external sunlight input, outgoing heat and no energy-return loop.
- Days 48 to 55 have complete 50-minute allocations; day 57’s remaining five minutes cover model reconciliation and collection.

Rejected 2:
- Assessment scoring history: UNIT-PLAN field 5 requires prior feedback for earlier product work. Day 56 is an independent assessment scored the following day.
- Missing daily exits: UNIT-PLAN assigns these to separate section plans. This multi-section unit plan correctly leaves them to write.

Per lens held up: assessment 2/4; sources 0 findings; sequence 1/1.

Gate: `python -X utf8 scripts/unitplan.py check biology` reports `PASS docs/courses/biology/s04.md`. The course check fails on unfinished `s05.md` through `s10.md`.
