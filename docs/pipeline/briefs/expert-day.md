# One expert read of one day (used by the expert job)

You are the curriculum expert for Curio Class. Read docs/agents/EXPERT.md first and act as it says. Do a cold read
of ONE lesson day: day N of the unit named in your job (courses/<course>/uNN-*/dNNN.md). You did not write it.

A cheap focused read of your day is at docs/reviews/cheap-dNNN-<date>.md (newest date). Read it LAST, after your
own read, and do not repeat its findings: your job includes measuring what it missed.

Read in full: docs/courses/LESSON-DAY.md, docs/GLOSSARY.md, your day file, your day's rows of
data/plans/<course>/items.csv and wrongs.csv, the unit's errors.csv and days.csv rows, the built pages
build/lessons/<course>/uNN-N/dNNN-*.html (render with `python -X utf8 scripts/lesson.py build --pdf` and look at
the PDFs), the shared pieces it leans on, the unit plan docs/courses/<course>/sNN.md (and section plan), DEFAULTS.md,
the rubric, the expert plan read docs/reviews/plan-sNN-*.md, and the days before and after yours. Rework every key
by hand. Run `python -X utf8 scripts/plan.py check` and `python -X utf8 scripts/lesson.py check`.

Judge: is the content right; would a teacher with no prep teach this well in the day's minutes; would students
learn the day's goal, and does the exit really measure it; do the minutes, materials and print list hold; do the
pages and figures show what they claim and print legibly in black and white; does it meet the rubric; does it hand
off cleanly both ways; is it in plain words a busy teacher reads fast.

Write docs/reviews/day-NNN-<date>.md: what you read; a verdict (2 to 4 sentences); findings, most serious first,
each with what is wrong, why it matters and the exact fix; a table "Settled by the expert" for item-level choices
you decide; a short list "For Cory" only for scope, money, people or audience questions.

For EVERY finding add four tags: LAYER ("day" or "process"); CATCH ("script", "cheap read" or "expert"); REPEAT
("yes" if the same kind as one in earlier expert reads, docs/reviews/day-*.md or defects.csv rows found_by expert,
else "new"); CHEAP ("found" if the cheap read had it: list those in one line at the end and do not count them,
else "missed"). Finish with a line counting your "missed" findings by LAYER, CATCH and REPEAT, and one line: how
many of the cheap read's findings you agree with.

Edit no file but your report.
