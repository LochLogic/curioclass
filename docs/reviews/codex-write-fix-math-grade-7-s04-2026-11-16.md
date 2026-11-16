Merged findings: **4**. Fixed all four in `docs/courses/math-grade-7/s04.md`:

1. Replaced premature successive-change scoring in M2 with separate forward changes and updated its key and look-fors.
2. Added fraction-division and equivalent-expression retrieval before first use, retaining the later required retrieval.
3. Replaced standalone readiness computation with an addition word problem, retaining subtraction and day 71 computation retrieval.
4. Preserved fifteen minutes for the interest comparison by adjusting day 62’s allocation and both saved-item timings.

Rejected: **0**.

Findings held up by lens: assessment **1/1**; sources **0 findings**; sequence **3/3**.

Gate: `python -X utf8 scripts/unitplan.py check math-grade-7` reports **PASS docs/courses/math-grade-7/s04.md**. The course check fails on existing `TODO(writer)` placeholders in s05.md through s08.md.
