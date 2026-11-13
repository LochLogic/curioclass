# Brief: unit 2 of Curio Class grade 4 math into data, plus its shared pieces

You work directly in S:\CurioClass (branch main). No other agent works in this checkout while you run. Unit 2 is
number patterns (4.OA.C.5), days 7 to 9, one section (2.1), folder courses/math-4/u02-1 (create it). Day 9 is
the assessment day (end-of-unit assessment 30, respond 20, next readiness 10, UNIT-PLAN rule 11). Its readiness
check is given on day 6 (already written: courses/math-4/u01-2/d006.md names `u02-1/readiness.md` and
`u02-1/record.md` "when it exists"). The plan is docs/courses/math-4/s02.md. Read docs/GLOSSARY.md for the words.

## Part 1: the plan as data
Do for unit 2 what commit e10e3e07 did for unit 3 (`git show e10e3e07`), following data/plans/README.md and
docs/courses/UNIT-PLAN.md: parts.csv, days.csv rows for days 7 to 9, items.csv (readiness rows s02-R1 to R3
exist; add any missing readiness row, the exits, the end-of-unit assessment items, written tasks), wrongs.csv,
errors.csv, words.csv, then `python -X utf8 scripts/plan.py tables math-4` so s02.md's tables are built from
data. Keep every key as the plan has it (they were worked twice by hand after the expert read); flag anything
that looks wrong instead of changing it. Item 4 needs a drawing: use a figure kind lesson.py supports if one
fits, else say so.

## Part 2: shared pieces
Match the unit 3 pieces in courses/math-4/u03-1 and the unit 1 pieces in u01-1 and u01-2 for shape and tone.
Read docs/courses/LESSON-DAY.md (pieces and gates) and docs/courses/math-4/DEFAULTS.md first, then
`python -X utf8 scripts/plan.py pack math-4 2`.
1. `courses/math-4/u02-1/readiness.md`: the readiness sheet from the s02-R rows (key, wrong answers, what each
   miss means for days 7 and 8). Then remove "when it exists:" before it in d006.md's `leans_on`.
2. `courses/math-4/u02-1/opener.md`: the section opener (supply list from s02.md section 8, the error table).
3. `courses/math-4/u02-1/record.md`: the record sheet (readiness, exits, end-of-unit assessment, written tasks by
   look-for), one landscape side, as unit 3's. Then remove "when it exists:" before it in d006.md.
4. The student recording page s02.md section 10 says is still to make, as a `blank` piece, if the days need it.
5. `courses/math-4/u02-1/family.md`: the family note from s02.md section 9, English only (the Spanish heading
   waits for a qualified reader), as u03-1/family.md.
Rule Machine is not built and tool building is held: the unit runs on print, and pieces name the tool only as
"when it exists:" with the paper path.

## Rules
No em dashes. "Curio Class" in full. No company names. No claims of review or endorsement. Header `credit: ours`,
`version: draft 1, not ready, not yet taught`. Grade 4 student sentences 15 words at most. Do not touch
data/closet/words, closet/words, data/media-manifest.txt, S:\CurioClass-spec2, or the untracked files
docs/Curio-Class-Plan.pdf, "docs/US Curriculum Design Blueprint.pdf", docs/Return/,
docs/agents/audit/wordwall-movement-cards.jpg.

## Gates
`python -X utf8 scripts/plan.py check` and `python -X utf8 scripts/lesson.py check` to 0 failures for your
files (failures only because days 7 to 9 are not written yet are expected; list them). Then
`python -X utf8 scripts/lesson.py build --pdf` and look at each piece's PDF once.

Commit your own files only and push: `git pull -q --rebase --autostash origin main`, then
`git push -q origin HEAD:main` (a "bypassed rule violations" line is expected). Never use git stash. End the
message with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>".

## Report back (under 200 words)
Rows added by file, pieces written, anything in the plan you found wrong or had to decide, expected failures, the
commit hash.
