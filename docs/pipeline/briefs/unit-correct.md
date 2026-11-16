# Job: correct the unit plans of {course} after the social studies probe (Codex)

[COURSE] = {course}. The first social studies probe (docs/reviews/probe-social-studies-2026-11-15.md) found faults
the Codex unit writer put into most social studies unit plans. You correct them in docs/courses/{course}/s*.md, the
course's unit plans, and nothing else. Read AGENTS.md, docs/courses/UNIT-PLAN.md fields 5 and 6 (two rules were added
on 2026-11-15) and docs/pipeline/briefs/plan-codex.md (the writer's settled rules, which still hold). {skip}

## 1. One mistake per register letter (every unit)

`python -X utf8 scripts/unitplan.py check {course}` now fails every error register row (field 6) whose error cell
joins two claims with a semicolon. For each such letter:

- Decide whether the claims are one misconception said twice (then rewrite the cell as one claim, no semicolon) or
  separate misconceptions that need different repairs (then split them).
- To split: the letter keeps its first claim; each further claim becomes a NEW letter added after the unit's last
  letter (so after G come H, I and so on). Never re-letter existing letters: section plans and other files use them.
  Give each new letter its own "What it shows" and source cell.
- Then retag every place in the unit that uses the old letter: field 5 wrong answers, the daily exit table, the
  readiness items, field 7 groups and any prose. A wrong answer goes under the letter whose text describes it; a wrong
  answer tagged with a letter whose text does not describe it is retagged (or the register gains the letter it needs).
- Where a split leaves a field 7 error group or a repair without a line, add one short line.

## 2. Scored parts and exits (named units only)

Read docs/reviews/probe-measure2-2026-11-15.md, sections K2, K3, K4, K7 and K10, and fix each entry that names this
course:

- **K2.** An end-of-unit part scored from work made on the day the topic is first taught, or from collected work with
  no feedback: either name the written feedback and the revision chance before it is scored (inside existing days and
  minutes), or make that work practice and score the part at the sitting with an item the students have not seen.
- **K3 and K4.** A day exit that rehearses an end item, or is answered from the sources just worked that day: give it a
  short new source, case or excerpt, named in the exit table (no invented quotation; invented cases are printed
  "invented for practice").
- **K7.** A wrong answer filed under a letter whose text does not describe it: retag it.
- **K10.** A sensitivity read that leaves out a community the days need: add that community and its own sources to
  field 10's study list and the flagged days.

Check the rest of the course for the same faults while you are in each file, and fix them the same way.

## Rules

Change only what these faults need: no new days, no moved content, no new standards. In data/plans/{course}/days.csv you may edit only the `note` cell of a day whose scoring or exit you changed, so it no longer gives the old instruction (keep the file's CRLF or LF endings and quoting); the plan's day list must say the same as that note. Keep the
plan's shape, voice and word cap. Write UTF-8 with LF endings; no em dashes; "Curio Class" in full; no company names
in student, teacher or family copy. Run `python -X utf8 scripts/unitplan.py check {course}` until every unit you
were given passes.

Blind rule: do not open docs/courses/ela-6/, docs/courses/ela-6-spine.md, docs/courses/math-4/,
docs/courses/math-4-spine.md, docs/courses/math-3-5-progression*.md, docs/courses/science-4-spine.md,
docs/courses/NEXT-SPINES.md, data/plans/math-4/, data/units.csv, courses/, im-g4-draft-map.csv, or
docs/reviews/*reconcile*, *math-4*, *ela-6*. No git. Leave no stray files.

Last message (under 250 words): per unit, letters rewritten as one claim, letters split (old letter, new letters),
K2 to K10 fixes made, anything you could not fix and why, and the final gate line.
