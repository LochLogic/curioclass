# Fix report: math-grade-8 unit 5 (2026-11-17)

Findings merged: 14 (assessment 6, sources 3, sequence 5). Fixed: 14 (some in shortened form to stay under the 1250-word cap).
Held up per lens: assessment 6 of 6, sources 3 of 3, sequence 5 of 5.
Gate: `unitplan.py check math-grade-8` PASS for s05.md.

Notes on shortened fixes: Teaching line merged sequence 1 and 2 (distribution taught early on day 75; days 76, 77, 79 teach new moves then practise; classify day 85, substitution day 86, rearranging day 87). Tools line names equation-balance and coordinate-plane as light, paper-drawing, no asks. Limits says 6.EE.A.1 serves only day 92's readiness check. Safety read now says no hazard or experiment is planned (no standard named, since none applies). Source column now names Illustrative Mathematics 8.4.x lessons.

REJECTED: none

LEAD:
- Days 75, 76, 77, 79, 86 and 87 are marked Fluency in days.csv but carry new base-lesson teaching; the kinds may need a second look.
- days.csv names equation-balance (days 73, 74) and coordinate-plane (days 83, 85, 86) as tools: either drop them from days.csv or create TOOL-ASKS.md for math-grade-8.
- Day 92 codes in days.csv carry 6.EE.A.1, so the generated standards list claims it; the plan cannot change that.
