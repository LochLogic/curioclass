# Brief: write one day of grade 4 math unit 2, in order

Follow docs/agents/DAY-WRITER.md, with these changes for unit 2.

- **Where you work:** directly in S:\CurioClass (branch main), not a worktree. The days of this unit are written
  one at a time, in order (7, then 8, then 9), so no other writer is working while you are. The unit 3 reads showed
  that parallel writers break the hand-offs; that is why. Do not commit or push; the main session does.
- **Unit 2:** number patterns (4.OA.C.5), days 7 to 9, one section (2.1), folder courses/math-4/u02-1. Plan:
  docs/courses/math-4/s02.md (unit and section plan in one). Data rows are in data/plans/math-4 (ids s02-*). Your
  reading pack: `python -X utf8 scripts/plan.py pack math-4 2`. Day 9 is the assessment day (UNIT-PLAN rule 11:
  end-of-unit assessment 30, respond 20, next readiness 10); its worked case is courses/math-4/u11-1/d093.md, and
  day 24 (courses/math-4/u03-4/d024.md) is the newest one.
- **Shared pieces exist:** u02-1/readiness.md (given on day 6), opener.md, record.md, family.md and any
  recording page. Read them and name them in `leans_on` without "when it exists".
- **Hand-offs, both ways, for real:** read the day before yours in full (day 6 is courses/math-4/u01-2/d006.md;
  days 7 and 8 are the files the writers before you just wrote). Your opening branches pick up what that day's
  exit and Tomorrow line actually say. If its Tomorrow line promises something you cannot or should not do, change
  that line in the earlier day file (the one edit outside your own day you may make) and say so in your report.
  Your own Tomorrow line names only what the next day's row in days.csv and the plan's U6 row will do. Day 9's
  Tomorrow line goes to day 10 (courses/math-4/u03-1/d010.md, written and fixed): read its opening and match it.
- **Tool:** Rule Machine is not built and tool building is held. Run on print in the same minutes; name it only as
  "when it exists:" with its paper path.
- **Numbers:** unit 2's numbers must not collide with unit 1's (days 1 to 6) or with any reserved exit or
  assessment row; the gates check.
- **Gates:** `python -X utf8 scripts/plan.py check` and `python -X utf8 scripts/lesson.py check` to 0 failures
  (a failure only because a later unit 2 day is not written yet is expected; name it). Then
  `python -X utf8 scripts/lesson.py build --pdf` and look at your student PDF and exit ticket once: every box fits,
  no teacher words or stray quote marks print on the student page.

Report back (under 200 words): files changed; teacher/student words and sides from the gate; any days.csv change;
any change to the earlier day's file; anything in the plan you found wrong or had to decide; anything you could not
do.
