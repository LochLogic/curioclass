Findings merged: 3:
1. Schedule conflict, assessment 1 and sequence 1.
2. Rehearsed day 6 and 17 exits, assessment 2.
3. Unsupported bubbles diagnosis, assessment 3.

Fixed: 2 fully. Replaced both exits with fresh evidence, keys and matching error letters. Added bubbling to the checkpoint and distinguished bubbles from property evidence.

The schedule finding remains valid. Added an explicit safeguard that day 20 work is unscored and only the day 21 product counts. Full alignment requires the lead to update days.csv, source-map.csv and scope-and-sequence.md, then regenerate the day list. Those changes exceed this job’s permitted file boundary.

Held up by lens: assessment 3/3; sequence 1/1; sources had no findings.

Gate: `python -X utf8 scripts/unitplan.py check science-grade-7` reports `PASS docs/courses/science-grade-7/s01.md`.

Only s01.md was edited. UTF-8 and LF endings verified.

REJECTED: none
