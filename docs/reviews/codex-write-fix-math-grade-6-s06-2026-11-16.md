Findings merged: 6. Fixed: 6, only in `docs/courses/math-grade-6/s06.md`.

1. Replaced E96 and E111 with different tasks; appended error V and its repair and retry.
2. Labelled P1’s meeting quotation as an excerpt accompanying the complete keyed record.
3. Broadened G to match its wrong answers and revised its repair.
4. Identified the science day 19 observation record, distinguished measured data from invented practice, and retained the fallback.
5. Replaced the producer abbreviation in field 3.
6. Restored the home route’s practice block to twenty minutes, totaling fifty.

Held up by lens: assessment 3/3; sources 2/2; sequence 1/1.

Gate: `python -X utf8 scripts/unitplan.py check math-grade-6` reports **PASS** for `s06.md`.
Course check still fails on existing unfinished placeholders in `s07.md` and `s08.md`.

Verified UTF-8, LF endings and no em dashes.

REJECTED: none

## Files changed outside the allowed set

- docs/COURSES-STATUS.md
- scripts/course_status.py
