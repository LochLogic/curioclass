# Reliability read brief (2026-11-13)

Purpose: measure how reliable a finished, fixed set of days is, as a planning number. You are a fresh expert reader
(an experienced grade 4 teacher and math educator) standing in for the teacher reader (Cory 2026-11-13). Edit
nothing; write no file. Your report is your final message.

Your set is named in your prompt. Read in this order:

1. The bar: AGENTS.md, docs/agents/EXPERT.md, docs/courses/LESSON-DAY.md, docs/GLOSSARY.md, DEFAULTS.md (find it),
   the section plan and its opener, and the unit plan row for each day in days.csv.
2. Cold read: each day file in full, its items.csv and wrongs.csv rows, and the built pages (run
   `python -X utf8 scripts/lesson.py build --pdf` if needed; look at the student PDF as images and read the display,
   key, exit and At home pages). Rework every key by hand. Read the days as a set: the seams between days (each
   Tomorrow against the next day's opening, the day before the set and the day after it or its plan).
3. Only after your own findings are written down, read the earlier reads and fix-pass rows for these days
   (docs/reviews/ and data/plans/defects.csv) to classify each finding.

For each finding give: the day; severity (blocker: a teacher could not run it or a student would learn something
wrong; major: a planned learning moment fails or misleads; minor: friction, wording, layout); layer (day, section,
process); origin (source-adapted or ours, where a base text exists; else ours); status against earlier reads
(new, missed earlier, regression from the fix pass, or known-and-left-open); and a concrete fix.

End with:
- a table of counts per day by severity, and totals by layer, origin and status;
- per day, yes or no: "teachable tomorrow with no prep by a capable teacher who has not seen it before";
- a one-paragraph verdict on the set's reliability.

Do not re-report items marked open in defects.csv unless their effect is worse than recorded.
