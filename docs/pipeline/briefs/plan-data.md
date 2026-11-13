# Job: apply the plan read, then put unit {unit} of {course} into data, plus its shared pieces

1. Apply the newest docs/reviews/plan-s{uu}-*.md: every finding and every row of "Settled by the expert", to the
   plan files docs/courses/{course}/s{uu}.md and u{uu}-*.md. Do not act on its "For Cory" list; repeat it in your
   report. Log each finding with `python -X utf8 scripts/plan.py defect {course} s{uu} <layer> expert <kind>
   "<summary>" docs/reviews/<report>.md#<n>`, marked fixed, open or rejected.
2. The plan as data, following data/plans/README.md and the way unit 2 was done (commit a40b62a1): parts.csv,
   days.csv rows for days {first} to {last}, items.csv (readiness, exits, end-of-unit assessment, written
   tasks), wrongs.csv, errors.csv, words.csv, and every column the README requires. Then
   `python -X utf8 scripts/plan.py tables {course}`.
3. Shared pieces in courses/{course}/u{uu}-1 (and the other section folders): readiness.md, the section
   opener(s), record.md, family.md (English only), and any recording page or sheet the plan names. Match the
   newest units' pieces (courses/{course}/u02-1 and u03-1) for shape and tone; read docs/courses/LESSON-DAY.md
   first. Where an earlier day's file names one of your pieces with "when it exists:", remove those words.

Gates: `python -X utf8 scripts/plan.py check` and `python -X utf8 scripts/lesson.py check` (failures only because
the days are not written yet are expected; list them). When this job ends, the unit's days are queued.

Do not commit or push; `turn.py end` does it. Last message (under 200 words): rows added by file, pieces written,
plan points you decided, expected failures, anything for Cory.
