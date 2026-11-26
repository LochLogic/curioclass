# Fixes: scope and sequence of health-grades-9-to-12, 2026-11-26

Fix pass after the expert read (docs/reviews/sequence-health-grades-9-to-12-2026-11-26.md), per
build/scope-writes/AFTERCORE-FIX.md and docs/pipeline/briefs/sequence-fix.md. The Codex read waits for Codex's usage
reset (after 2026-11-30) and gets its own small fix pass; the brief's Codex and 2026-11-15 lead-call items are skipped.
Files changed: docs/courses/health-grades-9-to-12/scope-and-sequence.md, data/plans/health-grades-9-to-12/days.csv
(by script, build/scope-writes/scratch/health-grades-9-to-12/fix_days.py) and docs/courses/health-grades-9-to-12/frame.md
(by script, fix_frame.py in the same folder; copies of both files before the pass are kept there).

**Counts.** Expert: 11 findings and 15 "Settled by the expert" rows, all applied, 0 not applied. Lead calls (AFTERCORE-FIX):
4, 5, 6, 7, 9 and 11 applied; 3 needed nothing (frame.py check had 0 failures); 1, 2, 8, 10, 12, 13 and 14 do not
touch this course. Band items: the other health expert reads (K to 2, 3 to 5, 6 to 8) have no "Across" item that
touches grades 9 to 12, so 0. Own: 2 (below). Each expert finding is logged with `plan.py defect` (11 rows, status fixed).

## Applied

- **Expert 1 (serious), Settled 1 to 5.** days.csv: day 4 goal adds "a strength that helps the character and one that
  helps a group" and "the factors that would help or block the character's goal"; day 8 asks "the behavior's benefits
  and, apart from them, one support and one barrier by level"; day 11 adds how income and neighborhood shape the
  behaviors and results behind the gap; day 15 adds how the character's access affects their wellness and judges one
  information card, one product card and one service card; day 18 adds one habit besides condition care; day 35 and
  day 79 notes ask S1.12.7 in full and name accuracy, trustworthiness and availability for S3.12.3 (day 35 also
  S2.12.2 in full and the three source kinds for S3.12.2). frame.md (lead call 4): the unit 1, 2, 3, 4 and 5 check
  sentences and both course-level check cells take the same words. Scope: units 1 to 5 and the course-level checks.
- **Expert 2.** Option (a): g7-phw-living-with-conditions is last used in grade 8 (g8-phw-factors-shape-health's asthma
  case). days.csv: day 15 drops the readiness check (sitting 40 minutes); day 17 opens with a 5-minute retrieval and
  lists the row in `retrieves`. frame.md: Readiness bullet (two readiness rows, with the reason this one is a
  retrieval), Seams intro and row, unit 4 and unit 5 rows. Scope: earlier-row table and preamble, units 4 and 5.
- **Expert 3, Settled 6.** Goal slot 10 moves from day 51 to day 54 (both sittings 30 minutes). days.csv 51, 54, 59.
  frame.md: the slot list and its reason in the goal thread bullet. Scope: goal thread, units 13 and 14, the
  40-minute path line (the day 51 exception is gone: days 51 and 54 keep 25-minute sittings there); the scope's old
  For the lead 1 is dropped.
- **Expert 4, Settled 7 and 8.** days.csv: day 52 takes the budget meal plan (and the unit-price line); day 53 is
  stations only, with the no-sink path (nearest sink in turns or a room with one; sanitizer does not stand in for hand
  washing before food handling); day 65 adds each student's written bystander plan; day 66 delivers the team's one
  issue ask in its two forms, and the delivery record names the level each piece reaches (relationships: the bystander
  plans; community and environment: the issue ask; society: the policy or rule change asked for). frame.md: unit 14
  and unit 18 rows (lead calls 4 and 7). Scope: units 14 and 18.
- **Expert 5.** Days kept as written; frame.md changed: unit 17 row (S8.12.2 evidence is the team ask, revised on unit
  18 day 1 and scored on unit 18's check day), unit 18 row's check, the End-of-unit evidence list ("NHES.S8.12.2 in
  units 17 and 18") and the Products sentence ("across units 17 and 18"). Scope: unit 17; old For the lead 2 dropped.
- **Expert 6, Settled 9.** days.csv: "Sensitivity flag: <area>" with the private route (cases are characters'; any
  student may take another case; a student who wants help talks privately with the nurse or counselor) on days 17,
  21, 30, 42 to 44, 46 to 48, 51, 53, 54 and 55 to 57. Scope: the Sensitive units list names every flagged day.
- **Expert 7, Settled 10.** Scope preamble: the card is withdrawn on the unit's last teaching day (the day before the
  check), whatever its kind; in the units of two or three days for that day's last task. days.csv: a "Card
  withdrawn" line on days 3, 7, 10, 14, 17, 21, 25, 29, 33, 39, 43, 47, 50, 53, 57, 59, 63, 67, 71, 74 and 77.
  frame.md: the health unit shape sentence ("withdraws it on the unit's last teaching day ... whatever that day's
  kind") replaces "on the application day".
- **Expert 8, Settled 11.** The talk turn card's listening steps are quoted as the steps after its first step, choose
  how to talk: scope Shared cards, frame.md Models row, day 28 note; day 27 names the channel choice as the card's own
  first step.
- **Expert 9, Settled 12.** Day 45 note, scope unit 12 and Sources: "the latest Youth Risk Behavior Survey edition that
  reports past-month alcohol use (2023 at the expert read; check for a 2025 release at the unit plan)". frame.md norm
  sentence for unit 12 takes the same words (lead call 4, a claim a source does not support). The expert's other
  checked figures (NYTS 2025 7.1 percent; naloxone over the counter since 2023-03-29) go into the scope's Sources.
- **Expert 10, Settled 13.** Day 27 note and the scope's same-term paragraph: the one-page support map where SEL 9 to
  12 is not run.
- **Expert 11, Settled 14 and 15.** Day 72 goal adds one facts-in-use item from day 70; the scope's grade 10 to 12 path
  joins e8-delineate-argument to the day 18 check and e8-argument-writing to the day 60 check.
- **Lead call 5 (day kinds).** frame.md Day kinds bullet: "the weekly goal slot is Application" replaced by GLOSSARY's
  rule (first teaching wins; the slot sits inside its host day and does not change that day's kind). Scope old For
  the lead 6 dropped.
- **Lead call 9 (collect once) and 11.** frame.md mid-course cell now says the influence item is a two-way chain from a
  new data card and the help request a channel choice and draft repair, because units 7 and 8 checked the same forms
  within two weeks; the end-of-course cell says the boundary item is an exchange to repair. Scope old For the lead 4
  dropped.
- **Lead call 4 (leave-out wording).** frame.md goal thread bullet: a left-out sensitive unit keeps its days in weeks 14
  to 16 as extension days, so no check or slot moves. Scope old For the lead 5 dropped.
- **Lead call 6.** 11 defect rows logged (artifact days.csv 8, frame.md 1, scope-and-sequence.md 2; kinds alignment,
  sequence, timing, missing, wording, source).
- **Own 1.** Units 20 and 21 are three-day units too, so they take the short-unit withdrawal (last task) with units 3,
  5, 13, 14 and 16; the expert's list named only those five.
- **Own 2.** Day 39 carries two cards: the boundary card is withdrawn all day; the conflict card, first modeled that day,
  is withdrawn for its last task.
- **Own check of the rule 2 lists.** Earlier-grade rows and last uses re-read against the frame after finding 2: the
  remaining readiness rows are g7-s-online-boundaries (day 36) and g6-fn-eating-patterns (day 51); every other row is a
  grade 8 retrieval; no unit's first day holds a readiness check; the grade 10 to 12 path still covers
  g7-phw-living-with-conditions on day 15 (now a grade 8 last use). Check days, end days and weeks unchanged.

## Not applied

- None.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A row's last use is read from the progression's `assumes` and `hands_on` of the grade between, not from its own grade number | g7-phw-living-with-conditions is used in grade 8's asthma case (expert 2) |
| A goal slot that cannot fit a crowded check day goes to another day in the same week (week 11: day 54) | Day 51 had a 20-minute sitting |
| Card withdrawal: the unit's last teaching day, whatever its kind; in units of two or three days, that day's last task; a card first modeled on that day is withdrawn for its last task only | APPROACH "What is carried"; units without an Application day |
| A sensitivity flag names its area and the private route in the note itself | Expert 6 |
| A check goal written for a builder names every part of each code; the boilerplate "a prompt for each part" is not enough | Expert 1 |
| A survey figure is cited as "the latest edition that reports it" with the year found at the read | Expert 9 |

## For the structure pass

- data/progressions/health.csv, row g9-phw-evaluate-habits, `notes`: old "Returns to g7-phw-living-with-conditions after
  a skip: the idea is not taught in between, on purpose." new "Retrieves g7-phw-living-with-conditions, last used in
  grade 8's asthma and air quality case (g8-phw-factors-shape-health)." (expert 2).
- data/progressions/health.csv, row g9-v-advocacy-adjust, `notes`: old "demonstrate advocacy that reaches relationships,
  communities, society and the environment: a bystander plan, a school policy ask and an ask for cleaner air or more
  shade near school." new "demonstrate advocacy that reaches relationships, communities, society and the environment:
  each team delivers its one issue ask in two forms, each student's bystander plan reaches relationships, and the
  delivery record names the level each piece reaches." (expert 4).
- data/plans/calendar.csv: regenerated at commit; nothing moved a check or a unit week (slot 10 stays in week 11).
- Expert "What is right": the structure pass weighs the scope's For the lead 1 (33 owned codes no course-level check
  samples; S4.12.5 and S4.12.10 proposed for the end-of-course check).
- Source list (expert): the FDA NYTS page now lives at
  https://www.fda.gov/tobacco-products/youth-and-tobacco/results-annual-national-youth-tobacco-survey-nyts (the old
  address redirects); CDC YRBS 2025 "Youth Health in Focus" covers five topics only, so substance figures still come
  from 2023.
- Browser check (lead, Claude in Chrome): https://library.samhsa.gov/product/preventing-suicide-toolkit-high-schools/sma12-4669
  (403; is 2012 still the latest edition) and https://ods.od.nih.gov/factsheets/WYNTK-Consumer/ (403; fact confirmed on
  FDA's page).
- Lens spellings (lead call 13): docs/agents/lenses/health.md shows no UK spelling on a search for the common forms;
  nothing to list.

## For Cory

- None.

## Gates

- `python -X utf8 scripts/sequence.py check health-grades-9-to-12`: 0 failures (notes: units 19 to 21, "standard None is
  on no day", left as lead call 12 says).
- `python -X utf8 scripts/frame.py check health-grades-9-to-12`: 0 failures (notes: 21 units, 80 days, 76 in units).
- `python -X utf8 scripts/frame.py calendar`: exit 0; grades 9 to 12 have no stagger rule but finals week, and the
  end-of-course check stays in week 16, so the course breaks no calendar rule.
