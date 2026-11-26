# Fixes: scope and sequence of career-exploration-grades-6-to-8, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-career-exploration-grades-6-to-8-2026-11-26.md), run as
build/scope-writes/AFTERCORE-FIX.md asks. The Codex read waits for Codex's usage reset (after 2026-11-30). No other
career education sequence read exists yet (Career Pathways is unread), so no "Across" item applies.

Counts: applied 6 of 7 expert findings plus all 7 rows of "Settled by the expert"; not applied 1 (finding 6, Cory's)
and For Cory item 2 (Cory's). Lead calls: 2, 3, 4, 6, 7, 11 used; 1, 8, 9, 10, 12, 13, 14 had nothing to act on here.
14 defect rows logged (status fixed, made at scope).

## Applied

- **Expert 1 (serious), days.csv and .md.** Every code an end day claims now has a named prompt or product:
  day 15 adds CD1.K2 (the plan page, each part labeled), CD2.K2 (four shuffled steps ordered), CD2.K3 (two invented
  students compared), CD3.A2 (a data item from a new 150-word profile, source and year), written as one-line prompts;
  day 44 adds CD2.K4 and CD2.K9 prompts and says CD4.A3 is scored on the practice 1 and 3 attachments; day 57 adds a
  CD1.K5 prompt; day 83 adds a CD1.K4 prompt and says CD3.A5 stands on the day 73 study revised on day 82; day 82
  drops CD1.K4 from skills and codes and revises the open-job study as a plan line; day 93 adds ALL1.K5, ALL2.K7 and
  ALL2.K3 prompts (the check-in line is now the record for ALL2.A3). Matching "Assessments" lines in the .md, unit 1's
  range listed code by code.
- **Expert 2, days.csv.** Missing parts added to goals: day 2 (how the top two values steer a choice, privately),
  day 9 (fourth source, an invented worker's post), day 11 (one school choice that shows my way of deciding), day 12
  (why facts beat a guess, from two invented cases), day 51 (why workers keep learning), day 54 (one job from a need
  added to the plan), day 87 (why taking charge of my learning matters at work), day 88 (learning outside class with
  the skill each builds), day 91 (why a plan helps in school).
- **Expert 3, days.csv, .md, frame.md.** `g6-lateral-reading` is retrieval (library 6 to 8 uses it in grade 7 by one
  hop through g7-lateral-hard-cases): day 9 opens with a five-minute retrieval task, `retrieves` = g6-lateral-reading;
  day 1's readiness keeps the two APPROACH items. .md readiness table row rewritten. Frame (call 4): the "Readiness and
  retrieval" bullet, the Models carried lateral-reading row, the library Cross-subject cell and For the lead item 5.
- **Expert 4, days.csv, .md, frame.md.** Day 90 names the OSHA young workers page for a safe workplace and who to ask,
  and the Wage and Hour Division's YouthRules and child labor pages for hours and task limits, each with date read,
  plus "a stricter state law applies where there is one". .md Sources bullet and the frame's unit 7 cell (call 4: a
  claim the source does not support) match.
- **Expert 5a, .md.** Ten-days-short list: day 61 into 59 replaces day 70 into 69; day 70 kept for the presenting
  bridge; ALL1.K6 listed as moving with day 61. Totals unchanged (10 sessions, 450 minutes, 86 days).
- **Expert 5b, days.csv, .md, frame.md.** ALL1.K6 (skill g8-all1-6-attitude-habits) moved from day 60 to day 61's
  opening with two invented bookkeepers; day 60 keeps the habit's start. .md unit 5 arc and the two-session unit 5 fold
  updated; frame unit 5 cell reworded (call 11).
- **Expert 7, days.csv, .md, frame.md.** SEL lean timings checked against SEL 6 to 8's days (grade 8 school day =
  SEL school day minus 320): day 11 careful-thinking taught first (school days 3 to 10); day 32 plan-and-tidy comes
  later (70 to 75); day 60 unit 15 school days 63 to 75. .md unit 3 and 5 leans lines; .md For the lead item 2
  dropped, since the frame's SEL Cross-subject cells for units 1 and 3 to 6 now state first or later with school days
  (call 7).
- **Settled row 4, days.csv.** Days 29, 44, 57, 67 and 83 notes say each cluster's unseen item is a short version of
  its first-look sub-cluster's field task decision on new data.
- **Expert 6 and For Cory item 2 (pending notes only).** .md Shorter path and Unsure name the over-full sessions with
  "Pending Cory"; day 86's note ends "Pending Cory" on registration timing; frame For the lead item 8 records the
  finding in a Pending(...) marker (call 3 wording).

## Not applied

- **Expert 6 (two-session path, 66 vs 64 sessions).** Breadth or dose; waits on Cory (lead note).
- **For Cory item 2 (day 86 course-choice timing).** Moves standards between units; waits on Cory (lead note).

## Settled (for DIGEST)

| Judgment | Reuse |
|---|---|
| A cross-subject row used one hop later (a later row `assumes` it) is retrieval, opened on the first day that uses it | Any lean on library rows |
| An end day's note names a prompt or product for every code it claims; a product can stand for a code when named | All career end days |
| Each cluster's unseen end-day item is a short version of its sub-cluster's field task decision on new data | Career Pathways |
| A minor's hours and task limits come from the Wage and Hour Division's YouthRules and child labor pages, not the OSHA young workers page | Career Pathways day on a first job |
| A bridge day for a later-taught lean (day 70) never folds in a short year | Short-path lists |

## For the structure pass

- Lens spellings (call 13): none found in this course's files; any UK spelling in docs/agents/lenses/career-education.md
  is the lead's.
- data/plans/calendar.csv: regenerate at commit as usual; no school day changed in this pass.
- Source list: add the Wage and Hour Division's YouthRules (https://www.dol.gov/agencies/whd/youthrules) and child
  labor (https://www.dol.gov/agencies/whd/child-labor) pages, public domain, opened 2026-11-26 (the read's "For the
  source list"); Career Pathways will need them.

## For Cory

1. **The two-session path.** Unit 1's short sessions 1, 2 and 9 and unit 7's course-choice session are over-full.
   (a) Unit 1 studies one cluster fewer at depth on that path, or (b) the path is 66 sessions, not 64. Read's pick:
   (b), since (a) leaves an owned sub-cluster unscored.
2. **When the course choices fall.** Day 86 (ALL2.K4, ALL2.A4, next year's course choices) is in week 29 of 32,
   possibly after a school's grade 8 registration deadline. (a) Keep it in unit 7 and let a school teach day 86 on its
   registration week (plan-day revision stays in unit 7), or (b) move ALL2.K4 and ALL2.A4 into unit 5 or 6. Read's
   pick: (a), with a line on the course page.

## Gates

- `python -X utf8 scripts/sequence.py check career-exploration-grades-6-to-8`: 0 failures.
- `python -X utf8 scripts/frame.py check career-exploration-grades-6-to-8`: 0 failures (note: 7 units, 96 days, 92 in
  units, 4 for checks and respond days).
- `python -X utf8 scripts/frame.py calendar`: cte grade 8 in weeks 16 and 32, unchanged; no stagger break (no school
  day moved).
