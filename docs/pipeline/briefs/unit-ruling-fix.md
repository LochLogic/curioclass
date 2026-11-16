# Job: apply the lead's rulings to one unit plan, {course} unit {unit} (Codex)

The fix step for docs/courses/{course}/s{uu}.md rejected some findings. The lead has ruled that these findings are
right and must be fixed. The rulings are final: do not argue them again.

Rulings: {rulings}

Read AGENTS.md, docs/courses/UNIT-PLAN.md and the writer's brief {writer_brief} first.

1. Fix each ruling in docs/courses/{course}/s{uu}.md only, the way its note says. Change only what each ruling needs:
   no new days, no moved content, no new standards. When you split an error letter, the new letter goes after the
   last one; never re-letter.
2. Run `python -X utf8 scripts/unitplan.py check {course}` until s{uu}.md passes.

Keep the plan's shape, voice and word cap. UTF-8, LF endings, no em dashes, "Curio Class" in full, no company names in
student, teacher or family copy. Blind list: never open docs/courses/ela-6/, math-4 paths, data/units.csv, courses/,
docs/reviews/*reconcile*, *math-4*, *ela-6*. No git.

Last message (under 150 words): each ruling and what changed for it, and the gate line for s{uu}.md.
