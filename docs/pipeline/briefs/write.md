# Job: write day {day} of {course}, unit {unit}

Write ONE day file, day {day}, following docs/agents/DAY-WRITER.md and the template docs/courses/LESSON-DAY.md.
Find day {day}'s section in data/plans/{course}/days.csv and docs/courses/{course}/s{uu}.md; the file is
courses/{course}/u{uu}-N/d{ddd}.md. Your reading pack: `python -X utf8 scripts/plan.py pack {course} {unit}`.

Days are written one at a time, in order. Read the day before yours in full (day {prev}, whoever wrote it): your
opening picks up what its exit and Tomorrow line actually say. If its Tomorrow line promises something you cannot
or should not do, change that line in day {prev}'s file (the one edit outside your day you may make) and say so.
If day {prev} is in another unit, also read that unit plan's carried list. Your own Tomorrow line names only what
day {next}'s row in days.csv and the plan will do; if day {next} is already written, read its opening and match it.

The shared pieces in the section folders exist; name the ones you use in `leans_on`. A tool that is not built is
named only as "when it exists:" with its paper path.

Fill your day's `shows` cell in data/plans/{course}/days.csv (the goal-to-item trace, data/plans/README.md).

Gates: `python -X utf8 scripts/plan.py check` and `python -X utf8 scripts/lesson.py check`. You may leave a failure
only if it belongs to a later day of this unit that is not written yet; name it. Then
`python -X utf8 scripts/lesson.py build --pdf` (if it cannot run where you are, say so) and look at your student
page and exit ticket once: every box fits, and no teacher words or stray quote marks print on the student page.

Do not commit or push; `turn.py end` does it. Last message (under 200 words): files changed; teacher and student
words and sides from the gate; any days.csv change; any change to day {prev}; anything in the plan you found wrong
or had to decide.
