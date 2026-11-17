Merged findings: **6**. Fixed **5** in `docs/courses/science-grade-7/s03.md`; **1** requires lead action outside the permitted file.

1. Calendar conflicts, assessment 1 and sequence 1: valid, unresolved. Lead must reconcile CSV days 43, 55, 58, 59, 61 and 63 to 65, update the scope and sequence, then regenerate the day list. Preserve feedback and day 66 revision before scoring.
2. Assessment 2: replaced the supplied model explanation with observations and explicitly requested the scored oxygen prediction.
3. Assessment 3: replaced repeated intestinal disruption with respiratory gas-exchange disruption and updated scoring.
4. Sources 1: replaced the acknowledgment form with professional safety guidance and required documented hazard analysis and controls.
5. Sources 2: identified the dated archive snapshot with its SHA-256.
6. Sequence 2: reserved cleanup within all four affected periods.

Findings held up: assessment **3/3**; sources **2/2**; sequence **2/2**.

Gate: `PASS docs/courses/science-grade-7/s03.md` from `python -X utf8 scripts/unitplan.py check science-grade-7`. All six course plans passed.

REJECTED: none

## Files changed outside the allowed set

- build/lessons/math-4/u03-3/d018-key.html
- build/lessons/math-4/u03-4/d023-key.html
- data/plans/unit-rejections.csv
- docs/COURSES-STATUS.md
