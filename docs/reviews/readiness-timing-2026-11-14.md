# Readiness check timing, 2026-11-14

Cory's decision (chat, 2026-11-14, confirming his Desk choice of 2026-11-11 on card q-unit-plans): a unit's readiness
check is given before the unit opens, so its results shape day 1. It takes the last ten minutes of the previous unit's
last day, or of the respond day or course-level check respond day where one sits between the two units; a unit 1
readiness check is served by the start-of-year check. A few days ahead at most, never weeks; day 1 of every unit stays
clean for the hook and the compelling question. Which units hold a readiness check is unchanged (sequence-write.md
rule 2). One timing in every course, grade 4 math included. Recorded in docs/agents/decisions/DESK-ANSWERS.md.

## Rule files

| File | What changed |
|---|---|
| docs/courses/UNIT-PLAN.md | Header note: one timing in every course, grade 4 math included (the grade 4 math exception is gone). Field 11: any day that ends with the next unit's readiness check names its ten minutes (the "Check (end-of-unit assessment 30, respond 20, next readiness 10)" form is now the general example). Field 4: "which units" kept, "when" rewritten to the new timing, with the assess marker rule, the few-days limit, unit 1 by the start-of-year check and the clean day 1; grade 4 math wording dropped. Field 4 template: "Day _ (before the unit opens ...; unit 1: the start-of-year check)". |
| docs/pipeline/briefs/sequence-write.md | Rule 2 rewritten: which rows get a check (unchanged), when it is given, how days.csv marks it (assess = readiness, or a kept assess value plus the note "plus the next unit's readiness check (10 minutes)"), unit 1 by the start-of-year check, never on a unit's first day. The gate paragraph names the new placement check. |
| docs/pipeline/briefs/sequence-read.md | The readiness bullet checks the new placement and names any check on a unit's first day or more than a few days ahead. |
| docs/pipeline/briefs/frame-write.md | Lesson 16: the same words plus the timing. |
| docs/pipeline/briefs/plan.md | The readiness check is given before the unit opens; the plan's readiness field names the day; the writer plans the next unit's ten minutes on the last day. |
| docs/pipeline/briefs/plan-read.md | The readiness question checks the new timing. |
| docs/GLOSSARY.md | "readiness check" entry rewritten to the timing (grade 4 math exception dropped); "readiness day" is the day whose last ten minutes hold the next unit's check; the "unit" entry no longer says a readiness check opens it. |
| docs/courses/CALENDAR.md | Says nothing about readiness checks; unchanged. |
| scripts/sequence.py | It had no placement check. Added one: a `readiness` day on a unit's first day fails, and a `readiness` day must be a C day, a respond day or a unit's last day, at most 3 days before a unit's first day (READINESS_AHEAD = 3). Tested against the old economics days.csv: days 1, 19, 45 and 52 fail as expected. |

Also changed, for one timing everywhere (not in the brief's list): the frames that said "on its first day" now say
"before it opens": civics-government-and-civic-life, economics (two Seams rows), social-studies-grade-5,
us-government-and-politics, us-history-ii (Days bullet and two Seams rows), world-geography-and-ancient-civilizations-i
and -ii. Frame Seams rows that say "content revisited, opens with a readiness check" (US History I, World History I)
were left: they read true under the new timing.

## Social studies days moved (45 checks)

Every previous day was a respond day with no assess value, so each now carries `assess` = `readiness` and a note line
"Last ten minutes: unit N's readiness check on ..." (the rows and reasons moved from the first day's note), and its goal
ends "then unit N's readiness check (last ten minutes)". Each first day lost the marker; its goal now opens on the
unit's content or question and its note says where the check was given. Later notes that named the old day ("day 16's
readiness check", "the day 1 readiness check") now name the new day or the start-of-year check. Day counts, units and
check weeks are unchanged.

| Course | Unit | From day | To |
|---|---|---|---|
| civics-government-and-civic-life | 2 | 16 | day 15 (unit 1 respond) |
| civics-government-and-civic-life | 6 | 77 | day 76 (unit 5 respond) |
| economics | 1 | 1 | start-of-year check |
| economics | 3 | 19 | day 18 (unit 2 respond) |
| economics | 6 | 45 | day 44 (unit 5 respond) |
| economics | 7 | 52 | day 51 (unit 6 respond) |
| social-studies-grade-3 | 1 | 1 | start-of-year check |
| social-studies-grade-3 | 2 | 25 | day 24 (unit 1 respond) |
| social-studies-grade-3 | 3 | 49 | day 48 (unit 2 respond) |
| social-studies-grade-3 | 6 | 125 | day 124 (course-level check 2 respond) |
| social-studies-grade-5 | 2 | 15 | day 14 (unit 1 respond) |
| social-studies-grade-5 | 4 | 44 | day 43 (unit 3 respond) |
| social-studies-grade-5 | 5 | 60 | day 59 (unit 4 respond) |
| social-studies-grade-5 | 10 | 147 | day 146 (course-level check 2 respond) |
| us-government-and-politics | 1 | 1 | start-of-year check |
| us-government-and-politics | 2 | 7 | day 6 (unit 1 respond) |
| us-government-and-politics | 3 | 16 | day 15 (unit 2 respond) |
| us-government-and-politics | 4 | 23 | day 22 (unit 3 respond) |
| us-government-and-politics | 5 | 38 | day 37 (course-level check 1 respond) |
| us-government-and-politics | 6 | 47 | day 46 (unit 5 respond) |
| us-government-and-politics | 7 | 56 | day 55 (unit 6 respond) |
| us-history-i | 1 | 1 | start-of-year check |
| us-history-i | 2 | 20 | day 19 (unit 1 respond) |
| us-history-i | 3 | 35 | day 34 (unit 2 respond) |
| us-history-i | 4 | 51 | day 50 (course-level check 1 respond) |
| us-history-i | 5 | 72 | day 71 (unit 4 respond) |
| us-history-i | 6 | 97 | day 96 (mid-year check respond) |
| us-history-i | 8 | 123 | day 122 (unit 7 respond) |
| us-history-ii | 1 | 1 | start-of-year check |
| us-history-ii | 3 | 26 | day 25 (unit 2 respond) |
| us-history-ii | 4 | 42 | day 41 (course-level check 1 respond) |
| us-history-ii | 5 | 57 | day 56 (unit 4 respond) |
| us-history-ii | 6 | 67 | day 66 (unit 5 respond) |
| us-history-ii | 8 | 103 | day 102 (unit 7 respond) |
| us-history-ii | 9 | 114 | day 113 (unit 8 respond) |
| us-history-ii | 11 | 135 | day 134 (unit 10 respond) |
| world-geography-and-ancient-civilizations-ii | 10 | 121 | day 119 (course-level check 2 respond; day 120, unit 8's look-back held there, sits between) |
| world-history-i | 1 | 1 | start-of-year check |
| world-history-i | 2 | 16 | day 15 (unit 1 respond) |
| world-history-i | 3 | 31 | day 30 (unit 2 respond) |
| world-history-i | 4 | 50 | day 49 (course-level check 1 respond) |
| world-history-i | 5 | 64 | day 63 (unit 4 respond) |
| world-history-i | 6 | 75 | day 74 (unit 5 respond) |
| world-history-i | 8 | 110 | day 109 (unit 7 respond) |
| world-history-ii | 8 | 108 | day 107 (unit 7 respond) |

No readiness checks in social-studies-kindergarten, grade-1, grade-2, grade-4 or
world-geography-and-ancient-civilizations-i (retrieval only); their days are unchanged.

Each course's scope-and-sequence.md was updated to match (rule statements, readiness tables in Government and US
History II, and every unit's "Readiness:" line).

## Shorter path, grades K to 5

Each K to 5 scope and sequence now has a "## Shorter path" section (sequence-write.md rule 10), before "For the lead":
a shorter-period route (K 20 minutes, grade 1 25 minutes, grade 2 30 minutes, grades 3 to 5 30 to 35 minutes, same
days) and a year about 10 days short by named fold-in days (K 54 lessons, grades 1 and 2 86, grades 3 and 4 150,
grade 5 151). Fold-in days carry no assessment and each of their codes and skills sits on another day too; grades 3
to 5 draw them from the days already marked "compressible (shorter block)".

## Item-level choices made here

- wgac II unit 10's check sits on day 119 (the course-level respond day), two days ahead, not on day 120 (a unit 8
  day held there).
- Grade 5 day 15's old note said "reteach in day 2"; it now says day 16, the unit's second day, as the scope and
  sequence already did.
- New day 1 goals where the old goal opened with the check (grade 3 days 25 and 49 open on the question with what
  students already know about rules and what the school needs).

## For the lead

1. The social studies frames name no start-of-year check (baseline-1 math review finding 9 says no frame has one).
   Six courses now point their unit 1 readiness check at it (Economics, grade 3, Government, US History I and II,
   World History I). Where and how long that check runs is not written yet; the frames and the first unit plans
   should say.
2. Economics is a semester course starting at school day 81; "start-of-year check" there means the check before its
   day 1.

## Gates

`sequence.py check` for all 15 social studies courses: 0 failures, no notes. `plan.py check`: exit 0.
`frame.py calendar`: no stagger break. `stale.py check`: 56 files, 0 failures.
