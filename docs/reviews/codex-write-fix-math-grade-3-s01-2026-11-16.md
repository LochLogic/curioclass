Findings merged: 2. Fixed: 1. Rejected: 1 shared finding.

Added explicit modelling and guided context creation on day 11, followed by independent context creation on day 19. Only s01.md changed.

Held up for fixes within scope: assessment 0/1; sources 0 findings; sequence 1/2.

Gate: `python -X utf8 scripts/unitplan.py check math-grade-3` reports `PASS docs/courses/math-grade-3/s01.md`.

REJECTED: assessment 1; sequence 2 | The plan’s day 6 graph collection, day 7 feedback, day 8 revision and day 21 scoring conflict with authoritative records retaining days 4 and 5 construction evidence. | Reconciliation requires lead edits to days.csv, source-map.csv and the scope and sequence before regenerating the day list, which this job cannot change; the plan’s existing cycle preserves earlier-day work, feedback and revision. | the writer's brief
