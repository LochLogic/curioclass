# Fixes: scope and sequence of health-grades-6-to-8, 2026-11-26

Fixer: after-core fix pass (build/scope-writes/AFTERCORE-FIX.md). One read so far: the Claude expert read
docs/reviews/sequence-health-grades-6-to-8-2026-11-26.md. The Codex read waits for Codex's usage reset (after
2026-11-30) and gets its own small fix pass.

Counts: applied 8 of 8 expert findings and 7 of 8 "Settled by the expert" rows (the eighth overridden by lead call
14); lead calls 4, 5, 6, 7, 9, 11, 14 applied (1, 2, 8, 10, 12, 13 have nothing to act on here); band items 0 (the
K to 2, 3 to 5 and 9 to 12 health expert reads have no "Across" section and no item that touches this course);
own 1. Not applied: 2 (both left to the lead).

## Applied

- **Expert 1 (end checks ask part of a code)**, days.csv: day 5 (a strength for the character's own wellness and
  one for the group, S1.8.1), day 47 note (strengths for one person and for a group), day 53 (a line asking for
  support and one offering it; how the conflict could have been prevented, is handled now and ended), day 80 (the
  five-level check with one health result and one fairness point), day 84 and day 95 note (the goal's link to the
  character's health, S6.8.3; day 95 also the S2.8.2 result and fairness point), day 101 (how the service helps keep
  the character healthy), day 108 (choose a tool and write how the character uses it this week; the day 107 record
  counts for S3.8.5 and, if the unit plan wants it, S2.8.4; the day 103 log stays private), day 129 (an unseen team
  scene in a different setting, and the teacher's day 123 to 127 record scored on the teamwork steps, S4.8.7),
  day 135 (one unseen case with two prompts). frame.md (call 4): the matching end cells of units 1, 11, 16, 17, 22,
  23, 26 and 27 and the course-level check cells for grade 6 year-end, grade 7 mid-year, grade 7 year-end and grade 8
  mid-year.
- **Expert 2 (first teaching on Application days)**, days.csv: days 30, 71 and 134 relabeled Understanding, each
  opening with the teacher modeling the idea on one case; day 128 stays Application with "the teacher models one
  effect write-up first". frame.md (calls 5 and 7): the Day kinds bullet now says first teaching of a row or method
  is Understanding with a teacher model and names the three days; units 6 (day 4), 15 (day 3) and 27 (day 5) cells
  relabeled; unit 26 day 6 names the modeled write-up. .md unit 6, 15, 26 and 27 arcs say so.
- **Expert 3 (self-checks)**: days 25, 73 and 121 notes add "Self-check 2 for unit 5 (15, 25) after the check";
  .md "What every unit does" says so; .md Shorter path adds "A folded day's self-check moves to the next day of its
  unit, and day 70's asthma plan line moves to day 69."
- **Expert 4 (days 59 and 65)**: both notes cap the end sitting at two short scenarios (25 minutes), then self-check 2
  (5 minutes) and the readiness check (10 minutes); .md "What every unit does" says so.
- **Expert 5 (facts)**: day 17 goal and note and .md unit 4 now read "had not used an e-cigarette in the past 30 days
  (about 96 in 100 in 2024)", NYTS 2024 3.5 percent current use from the CDC youth e-cigarette page opened by the
  reader; a later edition replaces it at the unit plan's expert read. frame.md norm bullet aligned (call 4). Day 2
  gives both CDC sleep ranges (9 to 12 for ages 6 to 12, 8 to 10 for ages 13 to 18, page dated 2024-05-15). .md
  Sources not loaded updated (the grade 8 survey's 2025 edition, results site browser check).
- **Expert 6 (40-minute path)**, .md: retrieval to 7 minutes, opening to 3, a readiness check keeps its 10 minutes
  and the end sitting on that day keeps two scenarios.
- **Expert 7 (stale lines)**: .md "The 45 minutes" now "first or second day"; self-check 1 "on a practice day before
  the check"; day 51 note PE unit 11 weeks 12 to 15; day 13 note adds "choose how to talk (in person, a call or a
  message)"; day 69 note and .md unit 15 "ends the week unit 15 opens"; .md Coverage replaces the leading counts with
  outcome numbers topic by topic (as the reader checked them), each with its units.
- **Expert 8 (sensitive lines)**: the first-day notes of units 9, 10, 19, 20, 21, 28, 29 and 30 (days 42, 44, 89,
  91, 93, 136, 138, 140) and the .md "Sensitivity and leave-out" say a school that keeps the unit may add one practice
  day before its check; day 118 note names "Sensitivity (safety and harm; substances):".
- **Settled by the expert**: relabels (30, 71, 134), days 59 and 65 cap, day 17 norm, day 2 ranges, For the lead 6
  (sensitive end checks stay unseen written scenarios, at most two short ones), For the lead 3 and 5 applied in
  frame.md (grade 6 year-end "units 1 and 3"; source-check "a fifth check") under call 7, since both are wording.
  g6-phw-adult-or-professional keeps its readiness check on day 97 (no change).
- **Lead call 14**: day 97 `assess` = readiness; the scope's For the lead 1 dropped; .md readiness table updated.
- **Lead call 3 / own**: the frame's Readiness bullet carried work-status wording ("the scope fix pass updates this
  bullet"); it now states the fact (course day 97, `assess` readiness, after the grade 7 year-end respond day).
- .md For the lead renumbered (1 card wording, 2 nine-week route, 3 day 117 gate note) with a "Settled at the fix
  pass" line for the dropped items.
- All 15 findings logged with `plan.py defect --status=fixed --made-at=scope` (data/plans/defects.csv).

## Not applied

- **Expert settled row "day 97 `assess` blank"**: overridden by lead call 14 (the gate now accepts a readiness check
  on a band year's first day after a course-level Respond day).
- **Card wording (scope For the lead 1)**: the frame's Models carried goal-plan and refusal wording differs from SEL
  STANDARD section 7's grades 6 to 8 forms. No read settled it and SEL STANDARD says health-side changes are the
  lead's, so the frame line is left; the .md quotes SEL's words.
- **Daily nine-week route (For the lead 2)**: needs the lead's session table.

## Settled (for DIGEST)

| Judgment | Reuse |
|---|---|
| A course-level check that is a unit's end carries that unit's self-check 2 in its note | Every band health course with mid-year-as-end units |
| A day with an end sitting and a readiness check caps the sitting at two short scenarios (25 + 5 + 10 minutes) | Any 45-minute course |
| First teaching of an owned idea on an end-of-unit look-back or effect day is Understanding with a teacher model, unless several lessons of the same work stand behind it (then Application with a modeled write-up) | Product and project units |
| A private log is never evidence; the in-class performance record can carry a second code if the unit plan wants it | Influence and goal units |
| Norm figures follow the survey's measure (past 30 days, current use), never "do not use" | All health norm days |

## For the structure pass

- docs/courses/health-grades-6-to-8/frame.md, Models carried: goal-plan "(pick, say why, steps, helpers and
  resources, check, look back)" to SEL's grades 6 to 8 "goal, steps, block and plan, check"; refusal-steps "SEL's
  card: stop and think, say no clearly, give a reason or none, offer something else or walk away" to SEL's "three
  options (a plain no, a no with a reason, a way out of the place), chosen to fit the place", keeping health's card
  steps as health's own. Lead's pick (scope For the lead 1).
- Lens spellings (call 13): none found in docs/agents/lenses/health.md (checked for common UK forms).
- calendar.csv regenerates as usual; no unit, day count or check day moved.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check health-grades-6-to-8`: 0 failures; notes: day 117 first Fluency day for
  `~NHES.S4.8.5` (expected, For the lead 3) and "standard None is on no day" for units 7, 9, 10, 19, 20, 21, 28, 29, 30
  (call 12, left).
- `python -X utf8 scripts/frame.py check health-grades-6-to-8`: 0 failures (unit days by year 44, 44, 44; 30 units,
  144 days).
- `python -X utf8 scripts/frame.py calendar`: health weeks 17 and 32 in grades 6, 7 and 8; no stagger break (no
  check day moved).
