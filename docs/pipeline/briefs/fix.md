# Job: apply the reads of {course} unit {unit}, days {first} to {last}

Each day has a cheap read (docs/reviews/cheap-dNNN-*.md) and an expert read after it (docs/reviews/day-NNN-*.md);
use the newest dates. Model your work on the unit 2 fix pass (commit e568594c).

1. Apply every expert finding and every row of each "Settled by the expert" table (do not re-decide them). Apply
   each cheap finding the expert agreed with; skip the ones the expert disagreed with and log them rejected.
   Collect the "For Cory" lists for your report; do not act on them.
2. Process findings first, once, so they fix every day: fix scripts/lesson.py, scripts/plan.py,
   docs/courses/LESSON-DAY.md, DEFAULTS.md, docs/agents/DAY-WRITER.md or CHEAP-READ.md where a finding says the
   fault is in the process, and add a gate where a "script" finding is cheap to gate. Do not undo earlier fix
   passes' changes.
3. Then the day findings, day by day. A changed stem gets a v2 (or next) id, wrongs repointed, day files and
   pieces updated. Check every hand-off pair (day N's Tomorrow against day N+1's opening), including the seam into
   the next unit: if the next unit's first day is written, its opening must still match.
4. Log every finding: `python -X utf8 scripts/plan.py defect {course} <artifact> <layer> <expert|cheap> <kind>
   "<summary>" docs/reviews/<report>.md#<n>`, marked fixed, open or rejected. A cheap finding the expert also
   lists counts once, as cheap. Never edit data/plans/defects.csv by hand.
5. Gates to 0 failures (this job cannot end with any): `python -X utf8 scripts/plan.py check`,
   `python -X utf8 scripts/lesson.py check`, `python -X utf8 scripts/plan.py tables {course}`, then
   `python -X utf8 scripts/lesson.py build --pdf`, and look at the unit's student PDFs, displays and exit slips.

Stale notes: a note that waits on other work starts `Pending(<file>, <file>#<text> or <plan node>):` so
scripts/stale.py can tell when it lands; any other work-status wording ("not yet placed", "until it is added")
fails the gate. When your work lands something a note waits on, run `python -X utf8 scripts/stale.py check`
and rewrite each STALE note to say what is now true.

Keep teacher prose under the word caps; pay for additions with cuts. Do not commit or push; `turn.py end` does it.
Last message (under 300 words): findings fixed / open / rejected (with why), new gates, process changes, anything
for Cory.
