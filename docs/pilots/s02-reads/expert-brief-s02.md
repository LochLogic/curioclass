You are the curriculum expert for Curio Class (repo S:\CurioClass, branch main). Read docs/agents/EXPERT.md first and act as it says. Do a cold read of ONE lesson day of grade 4 math unit 2 (number patterns, 4.OA.C.5; days 7 to 9; one section, 2.1, in courses/math-4/u02-1; day 9 is the assessment day). You did not write it. Other experts read the other days at the same time; stay on your day, but note anything that looks shared across days.

A cheap focused read of your day has already been done: docs/reviews/cheap-d00N-2026-11-12.md (your day number). Read it LAST, after your own read, and do not repeat its findings: your job includes measuring what it missed.

Model your read on docs/reviews/day-024-2026-11-12.md. Read in full: docs/courses/LESSON-DAY.md, docs/GLOSSARY.md, your day file, your day's rows of data/plans/math-4/items.csv and wrongs.csv (ids s02-*), errors.csv and days.csv rows for unit 2, the built pages build/lessons/math-4/u02-1/d00N-*.html (render the student page: `python -X utf8 scripts/lesson.py build --pdf` writes PDFs; look at them), the shared pieces in u02-1 (opener, readiness, record, recording page, family), docs/courses/math-4/s02.md, docs/courses/math-4/DEFAULTS.md, docs/RUBRIC-MATH-K8.md, and the day before and after yours. Day 7 follows day 6 (courses/math-4/u01-2/d006.md); day 9 is followed by day 10 (courses/math-4/u03-1/d010.md, already read and fixed). Rework every key by hand. Run `python -X utf8 scripts/plan.py check` and `python -X utf8 scripts/lesson.py check`.

This unit's days were written one at a time, in order, each writer reading the day before (unit 3's were written in parallel and broke the hand-offs). Judge the hand-offs both ways with that in mind and say whether in-order writing held them.

The writers changed or decided some plan points; judge each one that falls on your day and settle it in your table: day 9 replaced assessment item s02-E6 with a new version because its numbers collided with day 7's plan-mandated rules; day 9 ruled on whether day 8's T8-2 (9 x 5 = 45) overlaps assessment item E1; Rule Machine is not built, so the unit runs on print and names the tool only as "when it exists". Also check that a pattern rule with no "explain a feature" part is not passed off as meeting 4.OA.C.5, which asks students to notice features not explicit in the rule.

Judge: is the mathematics right; would a grade 4 teacher with no prep teach this well in 60 minutes; would students learn the day's goal; do the minutes, materials and print list hold; do the pages show what they claim; does it meet the rubric; does it hand off cleanly both ways; is it in plain words a busy teacher reads fast.

Rules: never use em dashes. Write "Curio Class" in full. Do NOT edit any file except your report (build output from running the build is fine; restore other units' build files if it rewrites them). Do not commit. Do not touch data/closet/words, closet/words, data/media-manifest.txt, or S:\CurioClass-spec2.

Write your report to docs/reviews/day-00N-2026-11-12.md with: what you read; a verdict (2-4 sentences); findings, most serious first, each with what is wrong, why it matters, the exact fix; a table "Settled by the expert" for item-level choices you decide; a short list "For Cory" only for scope, money, people or audience questions (likely none).

For EVERY finding add four tags:
(a) LAYER: "day" or "process";
(b) CATCH: "script", "cheap read" or "expert";
(c) REPEAT: "yes" if the same kind as one found in the earlier expert reads (skim docs/reviews/day-001 to 024-2026-11-12.md, day-072 to 093-2026-11-12.md and defects.csv rows found_by expert), else "new";
(d) CHEAP: "found" if the cheap read already had it (then do not count it as yours, list it in one line at the end instead), else "missed".
Finish with a line counting your findings (cheap "missed" only) by LAYER, CATCH and REPEAT, and one line: how many of the cheap read's findings you agree with. Your final message: the verdict, the counts, and the report path.
