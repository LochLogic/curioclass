You are the curriculum expert for Curio Class (repo S:\CurioClass, branch main). Read docs/agents/EXPERT.md first and act as it says. Do a cold read of ONE lesson day of grade 4 math unit 9 (adding and subtracting multi-digit whole numbers; days 72 to 77; section 9.1 days 72 and 73 in courses/math-4/u09-1, unit 9.2 days 74 to 77 in u09-2; day 77 is an assessment day). You did not write it. Other experts read the other days at the same time; stay on your day, but note anything that looks shared across days.

A cheap focused read of your day has already been done: docs/reviews/cheap-d0NN-2026-11-12.md (your day number). Read it LAST, after your own read, and do not repeat its findings: your job includes measuring what it missed.

Model your read on docs/reviews/day-084-2026-11-12.md. Read in full: docs/courses/LESSON-DAY.md, your day file, your day's rows of data/plans/math-4/items.csv and wrongs.csv (ids s09-*), errors.csv and days.csv rows for unit 9, the built pages build/lessons/math-4/u09-N/d0NN-*.html (render the student page: `python -X utf8 scripts/lesson.py build --pdf` writes PDFs; look at them), the section opener in your section folder, the shared pieces it leans on (readiness, columns, practice sheet, record), docs/courses/math-4/s09.md and your section's u09-N.md, docs/courses/math-4/DEFAULTS.md, docs/RUBRIC-MATH-K8.md, and the day before and after yours. Day 72 follows day 71 (unit 8, not written; its plan is its days.csv row). Day 77 is followed by day 78 (Check 2, not written; it needs units 6 to 8; its plan is its days.csv row). Rework every key by hand. Run `python -X utf8 scripts/plan.py check` and `python -X utf8 scripts/lesson.py check`.

Judge: is the mathematics right; would a grade 4 teacher with no prep teach this well in 60 minutes; would students learn the day's goal; do the minutes, materials and print list hold; do the pictures show what they claim; does it meet the rubric; does it hand off cleanly both ways; is it in plain words a busy teacher reads fast.

Rules: never use em dashes. Write "Curio Class" in full. Do NOT edit any file except your report (build output from running the build is fine; restore other sections' build files if it rewrites them). Do not commit. Do not touch data/closet/words, closet/words, data/media-manifest.txt, or S:\CurioClass-spec2.

Write your report to docs/reviews/day-0NN-2026-11-12.md with: what you read; a verdict (2-4 sentences); findings, most serious first, each with what is wrong, why it matters, the exact fix; a table "Settled by the expert" for item-level choices you decide; a short list "For Cory" only for scope, money, people or audience questions (likely none).

For EVERY finding add four tags:
(a) LAYER: "day" or "process";
(b) CATCH: "script", "cheap read" or "expert";
(c) REPEAT: "yes" if the same kind as one found in the earlier expert reads (skim docs/reviews/day-080 to 093-2026-11-12.md and defects.csv rows found_by expert), else "new";
(d) CHEAP: "found" if the cheap read already had it (then do not count it as yours, list it in one line at the end instead), else "missed".
Finish with a line counting your findings (cheap "missed" only) by LAYER, CATCH and REPEAT, and one line: how many of the cheap read's findings you agree with. Your final message: the verdict, the counts, and the report path.
