# Job: measure {course} unit {unit} (days {first} to {last}) and update the state pages

1. Count the unit's findings from docs/reviews/cheap-dNNN-*.md and day-NNN-*.md for days {first} to {last}, and its
   rows in data/plans/defects.csv (`python -X utf8 scripts/plan.py defects` gives totals).
2. Add a section to docs/pilots/REVIEW-CADENCE.md modeled on "Step 2 again: unit 2": the table, "What it shows",
   "What changes next". Compare writers: data/pipeline/jobs.csv names the worker that wrote each day.
3. Add the unit to docs/pilots/COST.md modeled on unit 2's table. Use token counts from data/pipeline/runs.csv
   where the runner logged them; write "not measured" where nothing was reported.
4. Add a "Done" bullet for the unit to docs/HANDOFF.md (after unit 2's), with its open items.

Do not commit or push; `turn.py end` does it. Last message (under 200 words): the headline numbers and what should
change before the next unit.
