Findings merged: 3. Fixed: 3, in docs/courses/math-grade-6/s05.md only.

1. Corrected error C and S3 to describe using the greater decimal-place count.
2. Added an F-specific remainder-sharing retry and linked it from field 7, retaining E’s existing card.
3. Replaced the product name in field 3 with “The base-text sequence.”

Per lens, findings held up: assessment 2/2; sources 1/1; sequence 0 findings.

Gate: `python -X utf8 scripts/unitplan.py check math-grade-6` reports PASS for s05.md; the course check fails on unfinished `TODO(writer)` entries in s06.md to s08.md.

REJECTED: none
