# Skel drift census (consolidation 4.E, 2026-11-25)

Command: `python -X utf8 scripts/skel_drift.py --out docs/reviews/consolidation/step4-E/skel-drift.csv` (report only;
it re-renders each written plan's skeleton in memory from today's data and compares the `<!-- skel -->` blocks in order).

- 916 written plans carry skel blocks (397 unit plans, 519 section plans); 860 have drifted.
- 5,286 of 9,464 blocks differ; none failed to render.
- By kind of difference (blocks compared by position, so a shifted block also counts the ones after it):
  several lines changed 2,423; block count differs 1,282; the fresh render only adds lines (generator fields added
  since) 974; one line changed 591; the plan has extra lines 13; whitespace only 3.
- By subject: ELA 2,316, science 1,116, social studies 937, math 638; high school courses 12 to 36 each.

Not yet known: how many differences are hand edits inside the markers that corrected a fact (these would mean the data
is wrong and the plan right). That needs the git history of each block and is the first step of any fix.

Left on purpose: unit_skeleton.py and section_skeleton.py still print "practised"; fixing them now would add a
format-only drift line to hundreds of plans, so it waits for Cory's choice. day_skeleton.py is fixed (day skeletons
are not copied into plans).

The choice is on the Desk (q-skel-drift-1). No plans were changed.
