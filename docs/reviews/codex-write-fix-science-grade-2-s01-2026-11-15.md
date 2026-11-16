Merged findings: 3. Fixed all 3 in `docs/courses/science-grade-2/s01.md`:

1. Specified daily exit stimuli, read-aloud questions, paper responses and answer criteria. Day 7 now differs from day 8’s six-category recording task.
2. Removed the unsupported valley location from day 8’s meeting example.
3. Corrected the header to three meetings weekly, following days.csv.

Rejected: 0; no rejection reasons apply.

Findings upheld by lens: assessment 2/2; sources 0 findings; sequence 1/1.

Preserved the plan’s shape, days, standards and word cap. Verified UTF-8, LF endings and no em dashes.

Gate: `python -X utf8 scripts/unitplan.py check science-grade-2` reports **PASS docs/courses/science-grade-2/s01.md**; the course command exits 1 because s02.md through s07.md retain unfinished placeholders.
