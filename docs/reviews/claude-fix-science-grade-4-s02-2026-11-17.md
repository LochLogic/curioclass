# Fix pass: science-grade-4 unit 2 (s02), 2026-11-17

Findings merged: 29 (assessment 16, sources 7, sequence 6; no two named the same fault). Fixed 25 (some in part), rejected 1, lead 3. Held up: assessment 15 of 16 (item 8 only in part), sources 6 of 7 (item 7 is a lead; item 4 and item 1 fixed in part), sequence 6 of 6 (items 2, 3 and 6 also leave lead lines).

Gate: `unitplan.py check science-grade-4` reports PASS for s02.md. The merged plan sat within a few words of its 1,800 cap, so the field 10, field 8 and field 7 fixes were kept to a few words each or placed in U3 and U6 (uncounted). Fixes that could not fit the cap: the exact table 5 values, the named hazard lines and the full cost recompute (see LEAD).

REJECTED: assessment 8 | E19 repeats day 19's warm-object-to-cool-object spoon pattern with nouns swapped, so change the stimulus to a sunlit and a shaded tin lid | the clip and lid case is a fresh pair of objects and day 19 teaches heat transfer by contact, so a sunlit-lid stimulus would move the exit onto day 18's light-warming content; the wrong-answer half of the finding was fixed (the "lid creating energy" A line is now the lid-to-clip "metal supplies warmth" arrow, no letter, confer) | none

## LEAD:
- data/plans/science-grade-4/source-map.csv has no rows for unit 2; create them from field 10 (sources 7).
- days.csv rows 18, 25, 36 (and the identical day 39 row) need the flashlight, car and heater materials, opaque card, foil strips and the "foil edges: fold smooth and adult checks" safety line (sequence 6).
- days.csv kind for day 23 may need to be Application, since the plan now marks day 22 as the first teaching of the crank conversion and day 23 as its first extended practice (sequence 3).
- Field 10: list the exact table 5 values, data year and rounding steps for the Colorado example, and name the pilot state safety guide with one line per hazard group (sources 4 and 1); no cap room in the counted fields.
- Costs: recompute circuit parts and thermometers for six sets against the $30 line (sequence 2); the plan now flags this as an open lead item in U6 day 25 only.
