- Fixed major-work allocation: day 75 now counts 47 minutes, unit 5 totals 882/950, and the course totals 4,177/6,390.
- Fixed S1 scheduling: production day 88, written feedback afterward, revision day 89 and scoring after day 90. Updated calendar, scope and sequence, generated day list and shorter-year option.
- Fixed coverage: removed 7.EE.B.4a from days 85 to 87 and matching plan claims. One-step preparation remains; unit 6 supplies full coverage.

`python -X utf8 scripts/plan.py check math-grade-7`: PASS, 0 failures.
`python -X utf8 scripts/unitplan.py check math-grade-7`: PASS, all eight unit plans.

## Files changed outside the allowed set

- data/plans/unit-rejections.csv
- docs/pipeline/briefs/unit-calendar-fix.md
- scripts/unit_rejections.py
