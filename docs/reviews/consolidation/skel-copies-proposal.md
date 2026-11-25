# Proposal: stop storing data copies in written plans (draft for review, 2026-11-25)

Cory picked this on 2026-11-25 (Desk card q-skel-drift-1, option 1) after the 4.E drift census
(docs/reviews/consolidation/step4-E/skel-drift.md). Nothing is built. This draft is what the Fable review checks,
together with 4.A to 4.E as built and 4.F to 4.K as planned.

## The problem

Written unit plans (docs/courses/<course>/sNN.md, 397 with blocks) and section plans (uNN-S.md, 519 with blocks) hold
copies of data between `<!-- skel -->` and `<!-- /skel -->`. The skeleton generators wrote them; the writers kept them
and wrote judgment prose around them. 860 of 916 plans now differ from a fresh render (5,286 of 9,464 blocks).

## Who reads the blocks today (found 2026-11-25, to be checked)

- scripts/section_skeleton.py `field()` reads unit plan fields 2, 5, 6, 8 and U3 to U11, with the markers dropped, and
  slices their lines and table rows by day into each new section skeleton. Some of that text sits inside skel blocks.
- scripts/day_skeleton.py `unit_field()` reads unit plan field n the same way, for day skeletons.
- scripts/unitplan.py strips blocks before counting words (the cap excludes them) at :257 and :340.
- scripts/unit_skeleton.py defines the markers (OPEN, CLOSE) and writes them.
- Unknown: whether build_site.py, plan.py, lesson.py, Codex briefs (docs/pipeline/briefs/section-write.md and others),
  the kit, or day writers read the copied facts in plans; whether the public site shows any plan text.

## Proposed sub-step (placed after 4.G, before any course run)

1. Sort every drifted block by cause, from each plan's git history (git log -L or blame on the block's lines):
   a. data changed after the plan was written (the copy is stale; data wins);
   b. the generator changed (new fields, wording; data wins);
   c. a hand edit inside the markers after generation (could be a correction: data may be wrong, plan right).
2. For every (c), decide: back-port into the data source (days.csv, items.csv, sources.csv, frames.csv, standards
   files, progression) through rows.py, or discard as a writer mistake. A list for Cory if any are judgment calls.
3. Change the readers so they no longer read copied facts from plans: section_skeleton.py and day_skeleton.py take
   those facts from data directly (they already can, since the blocks were rendered from data), and read only the
   judgment prose from plans.
4. Remove the blocks from all 916 plans in one mechanical commit; prose outside the markers is not touched.
5. Give writers a read view: a command (or the skeleton itself, which already renders the facts) that shows a plan's
   facts from data beside its prose.
6. Flag prose that leans on a changed fact (day numbers, codes, owning section, counts named in the prose) for a read.
7. Fix the "practised" spellings in unit_skeleton.py and section_skeleton.py (free once no copies are stored).
8. Gates: unitplan.py word caps unchanged in effect (the blocks were never counted); full gate run; skel_drift.py
   retired or turned into a guard that fails if a marker reappears in a written plan.

## Open questions for the review

- Does removing the blocks lose anything a writer or reviewer needs while writing or reading a plan?
- Is the cause sort reliable from git history, given the step 2 merge and earlier union merges?
- Is "after 4.G" the right place, or should it come before 4.F (the index and reports may read plan text) or 4.H?
- What gate proves nothing was lost?
