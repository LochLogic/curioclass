# Job: reconcile the {course} frame with earlier work

Added 2026-11-14 (PRODUCTION-PATH step 2; the frame-level twin of progression-reconcile.md). Cory's rule: write
blind, then reconcile, and "let the process do the work and save only the big stuff that really needs my attention
for the desk". The frame docs/courses/{course}/frame.md was written, read twice and fixed without sight of the
earlier Curio Class planning for this grade. You now compare the two, so what is good in the old work comes back in
on evidence, and nothing is kept only because it was written first or because days were already built on it.

## Read
- docs/pipeline/briefs/frame-write.md (the format, the lessons list), frame-read.md, and
  docs/agents/lenses/{subject}.md.
- The frame, its two reads and its fix report: docs/reviews/frame-{course}-2026-11-14.md,
  frame-{course}-codex-2026-11-14.md and the band's frame-{subject}-*-fixes-2026-11-14.md.
- The earlier work: {old}.
- The evidence that settles a difference: the standards file, the subject's progression and framework documents,
  the base text's own sequence and teacher notes ({evidence}), and data/progressions/{subject}.csv.

## Do
1. List every difference a unit writer or a teacher would feel: unit edges and order, days per unit, a standard in
   a different unit, a model or representation one has and the other lacks, a pick (text, phenomenon, case, worked
   example), a check-set item, a sensitive-topic note, a source-map placement, the time a day, a lesson the old work
   cut or merged and the frame keeps (or the other way), and anything the old work's own reviews found and fixed
   that the frame repeats.
2. Settle each by a named source. Neither side wins by default: not the old work for being reviewed or built on,
   not the frame for being newer. Where the old work wins, edit the frame (and the progression rows at both ends of
   any handoff it touches); where the frame wins, leave it and log the old item on the rework list. Where no source
   settles it, pick the reading that serves the student and mark it a judgment call.
3. Built work: where days, items or pieces already exist on the old plan (for math grade 4, courses/math-4/ and
   data/plans/math-4/), say for each frame unit whether the built days fit as they are, fit with named edits, or
   need rewriting, and why. Quality over saved work: a built day is not a reason to keep a weaker unit. Do not edit
   built days or old plan files; the rework list carries it.
4. Measure the pull: count the differences, how many each side won, and how many of the old side's wins rest on a
   named source. If the old work won most differences without a source, say so plainly in the verdict.
5. Gates: `python -X utf8 scripts/frame.py sync`, `python -X utf8 scripts/frame.py check {course}` and
   `python -X utf8 scripts/progression.py check {subject}` (or the progression gate inside scripts/plan.py check)
   until they print no FAIL; `python -X utf8 scripts/stale.py check` on the frame.

## What goes to Cory
Only the big things: a difference that changes what the grade teaches or which course teaches a standard, when no
source settles it; built work that would be thrown away in bulk (a whole unit or more of written days); or a pull
measure that shows the old work steering. Everything else you settle and log.

## Report
docs/reviews/frame-{course}-reconcile-{date}.md: the verdict (two or three sentences, with the pull measure), a
table of every difference (unit, old, frame, winner, source), the built-work table (step 3) where there is built
work, the rework list for old files, and "For Cory" (usually empty).
Rules: no em dashes; "Curio Class" in full; edit only the frame, data/progressions/{subject}.csv (both ends of a
handoff), frames.csv via sync, and the report; no git.
Final message: counts (differences, old wins with source, old wins without, frame wins), built-work verdict, gate
result, For Cory.
