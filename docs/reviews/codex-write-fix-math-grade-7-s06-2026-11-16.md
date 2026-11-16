Merged: 4 distinct findings. Fixed: 3. Rejected: 1.

Fixed in `docs/courses/math-grade-7/s06.md` only:

- Replaced exits 102 and 107 with different contexts and representations, with matching keys.
- Completed M3’s sample with both algebraic solution chains and arithmetic comparisons.
- Removed the product name from field 3’s teacher-facing prose.

Rejected assessment finding 1: R1 is drafted on day 115, receives written feedback, then is revised and scored on day 116. The settled rule requires creation on an earlier day than scoring, not revision on an earlier day.

Findings that held up by lens: assessment 2 of 3; sources 1 of 1; sequence reported 0 findings.

Gate: `python -X utf8 scripts/unitplan.py check math-grade-7` reports **PASS s06.md**; the course check fails on existing `TODO(writer)` placeholders in s07.md and s08.md.

UTF-8, LF endings, no em dashes, and replacement calculations verified.
