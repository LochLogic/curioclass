# Final review of a course's specs

Run once per course, after every spec in it is logged `fixed` in done.txt. Sara does the review. It answers one
question: would this course stand up to a state adoption review, standard by standard?

## Before the review (Claude, no judgment calls)

1. Read the fixed specs again with the catalog reader (`docs/agents/CATALOG-EXTRACT.md`), so each has a fresh row.
2. Rebuild: `python scripts/coverage_ledger.py`, `python scripts/catalog_maps.py`, `python scripts/spec_fixes.py`.
3. Spot-check the re-read: the top model reads one spec in five from scratch and compares its row with the re-read's.
   Below 80 percent agreement, the course is read again before anyone reviews it. (Added 2026-11-11: the first re-read
   was never checked, and the reading rule had changed the same day.)
4. Hand Sara the course's page of the map (`docs/agents/catalog/tables/map-<subject>.md`) and its fix file. Anything
   still listed in the fix file is where the review starts.

## The review, tool by tool

For every code on the spec, with the standard's full wording in front of you:

- [ ] A model: the student sees the thing done once before doing it.
- [ ] The verb: the student, not the tool, does what the standard's verb says.
- [ ] Every part: each operation, case, lettered part, and any explaining, writing or recording in the wording is
      done by the student somewhere on the path.
- [ ] Five or more items that differ in kind.
- [ ] A check where thinking is cheaper than guessing. For writing and talk: a guide while working and a self-check
      against a shown guide.
- [ ] Cannot be skipped: all of the above is on the path every student takes.
- [ ] The three hooks (README, "The end standard"): an unaided check the teacher can see, with what each wrong answer
      means; English learner supports; access by tap and keyboard, nothing by color alone.
- [ ] The role is honest: `teach`, `see why` or `practice`, and a practice tool says where the teaching happened.

For the spec as a whole:

- [ ] Facts, numbers and dates have sources; worked answers were rerun.
- [ ] Sensitive topics were read by someone fresh to the spec (BASELINE: fresh-reader sensitivity review).
- [ ] It still meets the rest of SPEC.md (art, voice, focus, kit and scope).
- [ ] Vocabulary matches the grade's standard, not the grade above.

## The review, course as a whole

- [ ] Every standard in the course is taught in full by at least one teach tool. List any that are not.
- [ ] Major work of the grade gets the most tools and the most items.
- [ ] No two tools teach the same thing the same way; where two overlap, one is the lesson and one the practice.
- [ ] The tools can be run in an order that makes sense, with nothing assumed that was never taught.

## After Sara's review (added 2026-11-11)

Sara fixed these specs, so her review cannot be the only one. A course's specs are finished on paper when she has
reviewed them. The course is not proved until the built tools have been played against their specs, a fresh agent
has read the course against docs/ADOPTION-BAR.md, and a working teacher has read one unit (docs/ROADMAP.md, step 4).

## Recording it

For each tool that passes, add a `reviewed` line to done.txt. For each that does not, write what is missing as a
note on a `fixed` line and send it back. A course is finished when every tool in it is `reviewed` and the
whole-course checks pass; say so to Cory on the Desk, with the standards still not taught in full, if any.
