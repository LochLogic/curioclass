Findings merged: 4. Fixed: 3, all in s01.md.

- Replaced the repeated narrative case and its five scoring samples.
- Replaced E5’s repeated inference with a fresh comparison using reserved passages.
- Added error letters Z and AA, distinct repairs, exit labels and response-group routing.

Per lens: assessment 3/3 held up and were fixed; sources reported 0 findings; sequence 1/1 identified a real mismatch, but its correction conflicts with the permitted file boundary.

Gate: `python -X utf8 scripts/unitplan.py check english-language-arts-grade-12` reports `PASS docs/courses/english-language-arts-grade-12/s01.md`. The plan meets the 1,800-word cap.

REJECTED: sequence 1 | Day 8 is labeled Fluency although its main work is narrative drafting and conferences. | Correcting the classification requires changing days.csv; relabeling s01.md alone would contradict the required source data, and only s01.md may be edited. | UNIT-PLAN field 1 and the writer's brief

## Files changed outside the allowed set

- build/lessons/math-4/u03-3/d018-key.html
- build/lessons/math-4/u03-4/d023-key.html
- data/plans/unit-rejections.csv
- docs/COURSES-STATUS.md
