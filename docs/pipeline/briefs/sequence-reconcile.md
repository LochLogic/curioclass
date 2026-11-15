# Job: reconcile the {course} scope and sequence with earlier work

This is the scope and sequence twin of frame-reconcile.md (PRODUCTION-PATH step 3). The rule is to write blind, then
reconcile (settled 2026-11-13, see DESK-ANSWERS). docs/courses/{course}/scope-and-sequence.md and
data/plans/{course}/days.csv were written without sight of the earlier Curio Class planning for this grade. You now
compare the two, so what is good in the old work comes back in on evidence, and nothing is kept only because it was
written first or because days were already built on it. The frame was reconciled already
(docs/reviews/frame-{course}-reconcile-2026-11-14.md); the units, their order and their day totals are settled and do
not change here.

## Read
- docs/pipeline/briefs/sequence-write.md (the format and rules) and sequence-read.md, and
  docs/agents/lenses/{subject}.md.
- The new scope and sequence, its days.csv, the frame docs/courses/{course}/frame.md and the frame reconcile report
  named above.
- The earlier work: {old}.
- The evidence that settles a difference: the standards files in data/standards/, the subject's progression
  (data/progressions/{subject}.csv), docs/courses/CALENDAR.md, and the base text's own sequence and teacher notes
  where the course has one (S:\CurioClass-sources).

## Do
1. List every difference a unit writer or a teacher would feel, inside the frame's units: the order of days, days by
   load, where a standard or skill is taught, where the readiness, mid-unit and end-of-unit assessments fall and what
   they cover, a bridge or lean timing, a check-set item, a sensitivity note, a source-map placement (a base lesson
   kept, split, merged or cut), and anything the old work's own reviews found and fixed that the new work repeats.
2. Settle each by a named source. Neither side wins by default. Where the old work wins, edit the new
   scope-and-sequence.md and days.csv (never the frame, never the unit totals); where the new work wins, leave it and
   log the old item on the rework list. Where no source settles it, pick the reading that serves the student and
   mark it a judgment call.
3. Built work: where days already exist on the old plan, say for each unit whether the built days fit the new
   scope and sequence as they are, fit with named edits, or need rewriting, and why. Quality over saved work. Do not
   edit built days or old plan files; the rework list carries it.
4. Measure the pull: count the differences, how many each side won, and how many of the old side's wins rest on a
   named source. If the old work won most differences without a source, say so plainly in the verdict.
5. Gate: `python -X utf8 scripts/sequence.py check {course}` must pass when you finish.

## What goes to the lead
Only the big things, under "For Cory": a difference that changes what the grade teaches, when no source settles
it; built work that would be thrown away in bulk (a whole unit or more of written days); a pull measure that shows
the old work steering. Everything else you settle and log.

## Report
Your last message is the report, filed as docs/reviews/sequence-{course}-reconcile-{date}.md: the verdict (two or
three sentences, with the pull measure), a table of every difference (unit, day, old, new, winner, source), the
built-work table where there is built work, the rework list for old files, and "For Cory" (usually empty).
Rules: no em dashes; "Curio Class" in full; edit only docs/courses/{course}/scope-and-sequence.md,
data/plans/{course}/days.csv and data/plans/{course}/source-map.csv; no git.
