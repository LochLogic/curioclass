You are applying the unit 2 reads in Curio Class (repo S:\CurioClass, branch main; work directly in S:\CurioClass, not a worktree). Unit 2 is grade 4 math days 7 to 9 (number patterns, 4.OA.C.5; one section, courses/math-4/u02-1; day 9 the assessment day; plan docs/courses/math-4/s02.md). Read docs/GLOSSARY.md for the words. Each day had two reads:
- a cheap focused read: docs/reviews/cheap-d007 ... cheap-d009-2026-11-12.md;
- a full expert read after it: docs/reviews/day-007 ... day-009-2026-11-12.md. Each expert report lists only what the cheap read missed, has a "Settled by the expert" table, and says which cheap findings it agrees or disagrees with.
None are for Cory unless a report's "For Cory" list says so; collect those for the report back and do not act on them. Model your work on the unit 3 fix pass (docs/pilots/s03-reads/fix-brief-s03-reads.md and commit 75f0c406) and on defects.csv rows found_by expert and cheap.

## Do
1. Read all six reports. Apply every expert finding and every row of each "Settled by the expert" table (do not re-decide them). Apply each cheap-read finding the expert agreed with; skip the ones the expert disagreed with and log them as rejected. Where two reports conflict, prefer the one about the day that owns the item and note it.
2. Process findings first, once, so they fix every day. Fix scripts/lesson.py, scripts/plan.py, docs/courses/LESSON-DAY.md, DEFAULTS.md or docs/agents/DAY-WRITER.md where a finding says the fault is in the process, and add a gate where a "script could catch it" finding is cheap to gate. One known open bug: in section openers, a blank written as `__ ... __` renders as bold (unit 3 openers show it; unit 2's writer escaped its own). Fix it in the build if a report confirms it, and check the unit 3 openers after.
3. Known open hand-off: the plan and the unit 2 record sheet say items 3 and 5 of the end-of-unit assessment go back in day 10's first five minutes, and day 9's Tomorrow says day 10's warm-up, but day 10 (courses/math-4/u03-1/d010.md) has no such step. Add it to day 10 within its minutes and word cap, or change the promise, and log it.
4. Then the day findings, day by day, in courses/math-4/u02-1 and data/plans/math-4/{items,wrongs,errors,days,words}.csv. Follow the item id rule: a changed stem gets a v2 (or next) id, wrongs repointed, day files and pieces updated. Day 9's Tomorrow line must still match day 10 (courses/math-4/u03-1/d010.md); if a fix changes what day 10 picks up, change day 10's opening too and say so.
5. Log every finding in the ledger data/plans/defects.csv: `python -X utf8 scripts/plan.py defect math-4 <artifact> <layer> <expert|cheap> <kind> "<summary>" docs/reviews/<report>.md#<n>`, marked fixed, open or rejected the way the unit 3 rows were. A cheap finding the expert also lists counts once, as cheap.
6. Gates to 0 failures: `python -X utf8 scripts/plan.py check`, `python -X utf8 scripts/lesson.py check`, `python -X utf8 scripts/plan.py tables math-4`, then `python -X utf8 scripts/lesson.py build --pdf`. Open the student PDFs, displays and exit slips of days 7 to 9 and the record sheet (render to PNG if you can) to see that boxes and tables fit.
7. Commit your own files only (build outputs included) and push: `git pull -q --rebase --autostash origin main` then `git push -q origin HEAD:main` (a "bypassed rule violations" line is expected). Never use git stash. End the commit message with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>".

## Others in the checkout
No other agent is working in this checkout now. Do not undo earlier fix passes' changes to scripts or shared pieces.

## Rules
Never use em dashes. Write "Curio Class" in full. No company names. No claims of review or endorsement. Do not touch data/closet/words, closet/words, data/media-manifest.txt, S:\CurioClass-spec2, docs/Curio-Class-Plan.pdf, "docs/US Curriculum Design Blueprint.pdf", docs/Return/, docs/agents/audit/wordwall-movement-cards.jpg, or anything under .claude/worktrees. Keep teacher prose under the word caps the gate enforces; pay for additions with cuts.

## Report back (under 300 words)
Findings fixed / open / rejected (with why), new gates (one line each), process changes, anything for Cory, commit hash.
