# Job: Codex second read of every unit plan of {course}

You are the second, independent reader of the unit plans of the course {course}: docs/courses/{course}/s01.md to the
last. Codex wrote them from skeletons made by scripts/unit_skeleton.py (fields between `<!-- skel -->` markers are
mechanical); a Claude expert has also read them, but do not open its report (docs/reviews/plan-{course}-{date}.md):
your read must be your own.

Read AGENTS.md, docs/agents/EXPERT.md, docs/GLOSSARY.md, docs/courses/UNIT-PLAN.md and
docs/pipeline/briefs/plan-read.md, then do the job of plan-read.md for each unit in turn, checking each plan against
docs/courses/{course}/frame.md, scope-and-sequence.md, data/plans/{course}/days.csv, the subject progression in
data/progressions/, and the bar for the subject in docs/ADOPTION-BAR-SUBJECTS.md. Across the course, also check:

- facts: is the content accurate and current as of today ({date})? Check on the web anything you are unsure of,
  including 2025 and 2026 events (court rulings, new laws, deaths of named people, changed official figures);
- sources: is anything invented passed off as a real source, and is each named source traceable;
- size: does each assessment and each day fit its minutes;
- hand-on: does each unit hand on cleanly to the next;
- text: any "?" where an apostrophe, quotation mark or accented letter should be;
- rule 2 (math, ELA, science): the field 4 table of earlier rows (last use and rule) is followed or each
  disagreement is under "For the lead"; evidence gathered one child at a time is collected once.

Gate: `python -X utf8 scripts/unitplan.py check {course}`.

Settled (do not raise): readiness timing (before the unit opens; unit 1's check in the last ten minutes of day 1, after
the hook, never before day 1); no outside human readers; 6 to 12 periods are 50 minutes; a timer only with a
grounded purpose (a pace cue, a movement game, classroom management); K to 2 at most one shared classroom device with
a paper path; no days added beyond the frame's totals; template fields that do not fit the subject may say none; some
standards codes lack an own-word line (a later pass fills them).

Report, as your final message, in Markdown: what you read; a course verdict (2 to 4 sentences); then per unit,
findings most serious first (serious, moderate, minor), each with what is wrong, why it matters and the exact fix
(file, field, old, new where short); then "For the fixer" (exact edits, in order) and "For the structure pass"
(changes to scripts, briefs, data or the template). Plain full sentences, no em dashes, "Curio Class" in full.

Blind rule: do not open docs/courses/ela-6/, docs/courses/ela-6-spine.md, docs/courses/science-4-spine.md,
docs/courses/NEXT-SPINES.md, data/units.csv, docs/reviews/*reconcile*, *ela-6*, science-4-spine*. The math blind rule
is lifted for future course-run work (Cory, DESK-ANSWERS 2026-11-20): a math run may read the old grade 4 math files and reconcile
with them; job lists made before 2026-11-20 keep their old notes.
