# Job: reconcile the {subject} progression with earlier work

Added 2026-11-13 (Cory: write blind, then reconcile; "let the process do the work and save only the big stuff
that really needs my attention for the desk"). The {subject} progression in data/progressions/{subject}.csv was
written blind: its writers could not see earlier Curio Class planning. You now compare it with that earlier work,
so what is good in the old work comes back in on evidence, and nothing is kept only because it was written first.

## Read
- docs/pipeline/briefs/progression-write.md (how the rows were made) and docs/agents/lenses/{subject}.md.
- data/progressions/{subject}.csv (the blind rows).
- The earlier work: {old}.
- The evidence that settles a difference: the standards file, the standard's own progression or framework
  documents, the base text's own sequence ({evidence}).

## Do
1. List every difference between the blind rows and the earlier work that a unit writer would feel: a standard in a
   different grade or unit order, a handoff or prerequisite one has and the other lacks, a limit, a model, a weak
   handoff the old work flagged, a page pointer the old work checked.
2. Settle each by a named source (standard text, a progressions document page, the base text's order). Neither
   side wins by default: not the old work for being reviewed, not the new rows for being newer. Where the old work
   wins, edit the row (and both ends of any handoff); where the new rows win, leave them and log the old item as
   rework for when that course is planned. Where no source settles it, pick the reading that serves the student and
   say it is a judgment call.
3. Measure the pull: count the differences, how many each side won, and how many of the old side's wins rest on a
   named source. If the old work won most differences without a source, say so plainly in the verdict.
4. Run `python -X utf8 scripts/progression.py check {subject}` until it prints no FAIL.

## What goes to Cory
Only the big things: a difference that changes which grade or course teaches a standard, or what a grade teaches,
when no source settles it; or a pull measure that shows the old work steering. Everything else you settle and log.

## Report
docs/reviews/progression-{subject}-reconcile-{date}.md: the verdict (two or three sentences, including the pull
measure), a table of every difference (row ids, old, new, winner, source), the rework list for old files, and "For
Cory" (usually empty). Rules: no em dashes; edit only data/progressions/{subject}.csv and the report; no git.
Final message: counts (differences, old wins with source, old wins without, new wins), gate result, For Cory.
