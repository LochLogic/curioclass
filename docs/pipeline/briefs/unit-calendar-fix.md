# Job: calendar fixes for one course after its unit plans are written, {course} (Codex)

The unit loop could not fix some findings for {course} because the fix lies outside a unit plan: the course calendar
(data/plans/{course}/days.csv), the scope and sequence (docs/courses/{course}/scope-and-sequence.md), the generated
day list in a unit plan, or the course's tool asks (docs/courses/{course}/TOOL-ASKS.md). The lead has ruled each one right. They are:

{items}

Read AGENTS.md, docs/courses/UNIT-PLAN.md, docs/courses/{course}/frame.md and the writer's brief {writer_brief} first.

1. For each item, make the smallest change that fixes it: a day's kind, codes, minutes or note in days.csv, the matching
   row of the scope and sequence, and the unit plan's day list and text that depend on it. Keep the course's day count,
   unit boundaries, totals and every other unit's days as they are unless the item needs them changed; if it does,
   change the other unit's plan to match too.
2. An item that needs new text written by us (a core text or anchor passage still "to write") is not a calendar fix:
   leave it and name it in your last message.
3. Run `python -X utf8 scripts/plan.py check {course}` and `python -X utf8 scripts/unitplan.py check {course}` until
   both pass.

Edit only data/plans/{course}/days.csv, docs/courses/{course}/scope-and-sequence.md, docs/courses/{course}/s*.md and
docs/courses/{course}/TOOL-ASKS.md. CSVs stay UTF-8 without BOM with their line endings. No em dashes, "Curio Class" in full, no company names in student,
teacher or family copy. Blind list: never open courses/, nor anything on the next line. No git.
Never open (data/homes.csv kinds never-touch, state, blind, pilot; scripts/homes.py briefs keeps this line): .claude/, docs/Return/, Gemini/, Gemini.*, data/closet/words/, closet/words/, data/media-manifest.txt, data/docs-manifest.txt, any path containing ela-6, docs/reviews/*reconcile*, any path containing math-4, docs/courses/*-spine.md, docs/courses/NEXT-SPINES.md, docs/courses/math-3-5-progression*.md, docs/reviews/*science-4-spine*.

Last message (under 250 words): each item, fixed (what changed) or left (why), then the two gate lines. One line per
item left, starting `LEFT:`.
