FIXED: Unit 03 calendar synchronization. Aligned days.csv, the scope and sequence, and s03.md with the plan’s teaching and scoring order: day 53 residual evidence, eligible device computations on days 54 to 56, feedback and revision before scoring, and an unscored day 57 report. Corrected dependent codes and regenerated the day list. Preserved all 160 days, unit boundaries, day kinds and other units’ calendar rows. CSV encoding and line endings are preserved.

For human review: the 40-minute option now allocates device cohorts of 11, 9 and 10 students; these planning budgets need classroom timing.

`python -X utf8 scripts/plan.py check algebra-i`: PASS, 0 failures.
`python -X utf8 scripts/unitplan.py check algebra-i`: PASS, all seven unit plans.
