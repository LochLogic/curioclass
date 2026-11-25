# Job: apply three lens reads to one unit plan, {course} unit {unit} (Codex)

Three focused reads of docs/courses/{course}/s{uu}.md are in docs/reviews/: codex-write-lens-assessment-{course}-s{uu}-{date}.md,
codex-write-lens-sources-{course}-s{uu}-{date}.md and codex-write-lens-sequence-{course}-s{uu}-{date}.md. Read AGENTS.md,
docs/courses/UNIT-PLAN.md and the writer's brief {writer_brief} first.

1. Merge: list every finding once (the same fault named by two lenses is one finding).
2. Judge each: fix it, or reject it with a one-line reason (wrong, or it would break a settled rule of UNIT-PLAN or the
   writer's brief).
   A finding that a part is made, given feedback, revised and scored in one period is right (UNIT-PLAN field 5):
   never reject it. Fix it by scoring a part made on an earlier day of the unit, or by making the same-day part
   unscored practice.
3. Fix in docs/courses/{course}/s{uu}.md only. Change only what each finding needs: no new days, no moved content, no
   new standards. When you split an error letter, the new letter goes after the last one; never re-letter.
4. Run `python -X utf8 scripts/unitplan.py check {course}` until s{uu}.md passes.

Keep the plan's shape, voice and word cap. UTF-8, LF endings, no em dashes, "Curio Class" in full, no company names in
student, teacher or family copy. Same blind list as the lens reads: never open courses/, nor anything on the next line. No git.
Never open (data/homes.csv kinds never-touch, state, blind, pilot; scripts/homes.py briefs keeps this line): .claude/, docs/Return/, Gemini/, Gemini.*, data/closet/words/, closet/words/, data/media-manifest.txt, data/docs-manifest.txt, any path containing ela-6, docs/reviews/*reconcile*, any path containing math-4, docs/courses/*-spine.md, docs/courses/NEXT-SPINES.md, docs/courses/math-3-5-progression*.md, docs/reviews/*science-4-spine*.

Last message (under 200 words, plus the rejection lines): findings merged (count), fixed, per lens how many held up,
and the gate line for s{uu}.md. Then one line per rejected finding, each starting `REJECTED:` exactly:
`REJECTED: <lens> <number> | <the finding, in a sentence> | <why, in a sentence> | <the rule relied on: UNIT-PLAN field N, the writer's brief, or none>`.
The lead rules on every rejection later and may send the finding back to be fixed, so write each so it can be judged
without opening the lens report. No rejections: one line, `REJECTED: none`.
