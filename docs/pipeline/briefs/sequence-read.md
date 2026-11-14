# Job: expert cold read of the scope and sequence of {course}

Added 2026-11-14 (PRODUCTION-PATH step 3). You are the curriculum expert. Read docs/agents/EXPERT.md first and act as
it says, then the subject lens docs/agents/lenses/{subject}.md and the subject's bar ({bar}). Read cold
docs/courses/{course}/scope-and-sequence.md and data/plans/{course}/days.csv; you did not write them. Read beside them
the frame docs/courses/{course}/frame.md, the progression rows for the course's grades (data/progressions/{subject}.csv),
docs/courses/CALENDAR.md and data/plans/calendar.csv for the grade. Run `python -X utf8 scripts/plan.py check` and
`python -X utf8 scripts/frame.py calendar` first; the gates settle what they check (day numbers and totals, unit day
counts, kinds, an assessment per unit, respond days, owned skills placed), so spend your read on what they cannot.

The data you must check:
- **Order inside each unit:** each day builds on the days before it; nothing is used before it is taught; the arc
  reaches the unit's compelling question or performance task.
- **Assessments:** the end-of-unit assessment covers every part of every standard the unit teaches; every
  observation, end-of-unit and check task asks about each part of each code it lists (a prompt per part, or a product
  or observed performance the day names); mid-unit assessments sit where a unit over 25 days needs one; response time
  is counted once.
- **Readiness or retrieval** (sequence-write rule 2): a row used the year before, or earlier the same year, opens as a
  retrieval task inside a day; every other earlier-grade row the unit assumes (last used two or more grades back)
  gets a readiness check, given before the unit opens: the last ten minutes of the previous unit's last day, or of
  the respond day or course-level check respond day between the two units (unit 1: the start-of-year check), never
  on a unit's first day, which stays clean for the hook and the compelling question (Cory, 2026-11-14). Check each
  assumed row's last use in the progression, and name any unit that checks a year-before row or retrieves an older
  one, and any readiness check placed on a unit's first day or more than a few days ahead.
- **Checks that do not repeat:** a course-level check right after a unit's end-of-unit assessment draws its items for
  that unit's skills from earlier units' content, and the scope and sequence says so.
- **Standards in full:** every lettered part of every owned code is carried by a day, not only named.
- **Days by load:** days follow what each part of a unit owns; a run of days far over or under its load is named
  with the counts.
- **The calendar:** the course-level checks sit on CALENDAR.md's target weeks, or the write-up says why not; each
  same-year lean meets the other subject's days in data/plans/calendar.csv, or the day carries its bridge.
- **Candidate cells:** each is settled, with its day cost inside the unit or the reason it was dropped.
- **Shorter path:** the scope and sequence has a "Shorter path" section: a shorter period, and a year about 10 days
  short by named fold-in days, with nothing assessed and no owned part cut.
- **Source map** (base-text courses only): every base lesson placed or cut with a reason; the base text's own order
  kept unless a reason is given.
- **The lens checklist** for the scope and sequence layer: each line met, missed or not applicable.
- **Stale notes:** run `python -X utf8 scripts/stale.py check`, then look for the rest.

Write docs/reviews/sequence-{course}-{date}.md: what you read; a verdict (2 to 4 sentences); findings, most serious
first, each with what is wrong, why it matters and the exact fix; a table "Settled by the expert"; a short list "For
Cory" (scope, money, people or audience only). Tag each finding LAYER (sequence, frame, progression, standard, base
text or process) and REPEAT (yes if the same kind as an earlier read in docs/reviews/, else new).

Edit no file but your report. Last message: the verdict, the finding count, the report path.
