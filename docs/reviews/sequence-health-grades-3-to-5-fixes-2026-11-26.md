# Fixes: scope and sequence of health-grades-3-to-5, 2026-11-26

Fix pass under build/scope-writes/AFTERCORE-FIX.md and docs/pipeline/briefs/sequence-fix.md. One read so far: the
Claude expert read docs/reviews/sequence-health-grades-3-to-5-2026-11-26.md. The Codex read waits for Codex's usage
reset and gets its own small fix pass. Files changed: docs/courses/health-grades-3-to-5/scope-and-sequence.md,
data/plans/health-grades-3-to-5/days.csv (patched by build/scope-writes/scratch/health-grades-3-to-5/fix_days.py)
and docs/courses/health-grades-3-to-5/frame.md (wording only, by fix_frame.py in the same folder). No unit, day count
or owned row moved.

Counts: applied 12 of 12 expert findings and all 10 of the expert's Settled rows; 3 frame wording items from the
read's For the lead (applied under lead calls 4 and 7); 1 band item checked (the K to 2 read has no item for this
course); 2 own items. Not applied: 0. Defect rows logged: 15.

## Applied

- **Expert 1** (days.csv): check goals on days 24, 39, 44, 49, 54, 59, 69, 74, 75, 79 and 88 now name one item per
  part: day 24 adds how to grow a strength (S1.5.1); days 69 and 75 add how finding a fact would change the
  character's choice (S1.5.5); days 54 and 59 add why a team with a clear ask is heard more (S8.5.2); days 49 and 59
  split S2.5.2 (my health and another's) from S2.5.3 (people and a community, and why) and add a product and a service
  to the claim (S3.5.3); day 44 adds the reply when a friend asks (S4.5.3, giving); days 79 and 88 ask stay out of,
  handle and settle separately (S4.5.6); days 39 and 44 ask illness and injury separately (S1.5.3) and whether a
  decision needs help as well as who (S5.5.2); days 74 and 88 ask the look-back for them and for others (S5.5.5);
  days 69, 75 and 88 ask when to get care and the reason (S1.5.7). The .md's "Each part of each code" bullet lists
  every part.
- **Expert 1, frame side** (frame.md, lead calls 4 and 7): the Course-level checks table cells for grade 4 mid-year
  and year-end and grade 5 mid-year and year-end use the same per-part wording.
- **Expert 2** (scope-and-sequence.md, Shorter path): day 41's fold keeps a five-minute ask rehearsal on day 40 and a
  five-minute listening-reply rehearsal on day 42. Grade 5 keeps day 70 whole and folds respond day 76 into day 77's
  exit and day 78's opener (day 78's retrieval repeats day 77's). The total is recounted to about 135 minutes.
- **Expert 3** (days.csv, .md): the unit 7, 14 and 21 family notes go home with the unit 6, 13 and 20 notes on days 23,
  53 and 82 (two and four weeks ahead). They are taken off days 25, 55 and 84, and the leave-out bullet says so.
- **Expert 4** (days.csv, .md rule 2 table): a bridge-form retrieval opens days 25 (g2-v-body-safety), 27
  (g2-sh-bodies-grow-respect), 55 (g3-v-body-safety), 57 (g3-sh-respect-all-people), 84 (g4-v-body-safety) and 86
  (g4-sh-body-changes, g4-v-limits-and-respect), set in `retrieves`. g4-pa-warm-up is added to day 61 as a one-line
  retrieval, and day 62 keeps it. The table lists the grade 4 and 5 rows.
- **Expert 5** (days.csv end-of-unit notes, .md): response time now works like this. The marked sheet comes back at
  the start of the next lesson and each student redoes one "not yet" step as that lesson's exit ticket, counted once.
  After units 7, 14 and 21 the sheet comes back privately on days 30, 60 and 89.
- **Expert 6** (days.csv): day 80's compare-options and W.4.1 retrievals move to day 81, and the .md table and ELA
  line follow. Day 86 opens with the puberty review as its retrieval and collects question-box slips. Day 87 answers
  them before the check. Days 40, 46 and 70 name the read's fallback if the day runs over.
- **Expert 7** (days.csv): S1.5.2 is dropped from day 9, S4.5.4 from day 58 and S4.5.6 from day 85. Days 26, 28, 56,
  58, 85 and 87 say "practiced, not scored". The progression item goes to the structure pass.
- **Expert 8** (days.csv, .md): card withdrawals. Days 13 (help-steps with decision-steps), 20 (listening steps with
  the I-statement), 38 (decision-steps for the last case) and 53 (refusal card for the team ask). The speak-up plan is
  held through day 53 and is first used unaided at the day 54 check, and the .md says so.
- **Expert 9** (days.csv days 51 and 70, .md, frame.md models and unit 12): the refusal card is quoted in SEL's grade 3
  form ("stop and think, say no clearly, give a reason, offer something else or walk away"), with health's line after
  it. The 3 to 5 card forms are cited as "SEL 3 to 5 frame, from STANDARD section 7". Day 18 names SEL unit 4 (weeks
  17 to 21) as running side by side for the talk turn card.
- **Expert 10** (days.csv, .md sources, frame.md units 1 and 10): day 3 and frame unit 1 add the vigorous days. Days 8
  and 51 cite NYTS 2024, middle school (CDC page dated 2024-10-17). Day 70 cites the national 8th-grade survey and
  marks it browser check. Day 19 cites CDC "About bullying" (dated 2024-10-28). Day 41 and frame unit 10 name the help
  line by purpose (the national crisis line, call or text 988).
- **Expert 11** (frame.md, .md, lead call 7): the frame's six "if left out, its days extend unit N" cells now say how:
  the freed days stay in their weeks as practice days on that unit's cards, with no new items, so no check moves. The
  .md's leave-out bullet says the same.
- **Expert 12** (.md, Shorter period): a course-level check gives its facts-in-use and valuing items in the first ten
  minutes of the respond day before. An end-of-unit check gives them at the start of the check day, with one scenario
  card fewer. Nothing is cut.
- **Read's For the lead / scope For the lead 1** (frame.md, lead call 4): the SEL Cross-subject rows now give unit 17
  as weeks 10 to 13 (two cells). The scope's For the lead 1 now records the fix.
- **Own, lead call 8** (days.csv): begun ids are written as `~ID` in `codes`: day 3 ~NHES.S8.5.1, days 20, 25 and 27
  ~NHES.S4.5.4, day 33 ~NHES.S7.5.2. The .md names them.
- **Band item**: the health K to 2 expert read (sequence-health-grades-k-to-2-2026-11-26.md) has no "Across" section
  and no finding that touches grades 3 to 5. Nothing to apply.
- **Lead calls checked, nothing to change**: 1 (the frame's For the lead 4 already reads as settled by CALENDAR.md
  rule 1; the scope has no special-only clash item), 2 (no source-map.csv), 3 (frame.py check had no failures), 5 (day
  kinds already follow GLOSSARY), 9 (the frame's check cells already say the records are carried), 10 (no owned code
  ends after its year's last check), 12 (the six "standard None" notes are left as they are), 14 (no readiness checks
  in this course).

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reuse |
|---|---|
| A sensitive unit's family note goes home with the one before it, on a non-removable unit's day, two and four weeks ahead | Any band with paired sensitive units |
| Response time is one "not yet" step redone as the next lesson's exit ticket. When the next lesson is a course check, the sheet comes back privately on the respond day | One-lesson-a-week courses where the opener is the retrieval |
| Sensitive units' first-day retrieval is the leave-out bridge's one-step form, so it serves classes whose earlier unit ran and classes whose unit was left out | Health and SEL bands with removable units |
| On assess rows `codes` lists only codes an item asks in full; sensitive checks add "practiced, not scored" | Any course with removable units that own nothing |
| A shorter year folds a respond day (not assessed, owns nothing) before it folds a row's only day | Fold-in lists |
| 3 to 5 shared card forms are cited as "SEL 3 to 5 frame, from STANDARD section 7" | Health and PE 3 to 5 |

## For the structure pass

- data/progressions/health.csv, row g5-v-body-safety, `standard`: old `~NHES.S4.5.6`, new `~NHES.S3.5.1` (or
  `~NHES.S4.5.3`). The conflict indicator is a weak fit for a signs-and-helpers row (expert finding 7, for the
  progression owner). Kept as is here; days.csv day 85 no longer lists S4.5.6, and day 84 still does as practice.
- docs/courses/physical-education-grades-3-to-5/frame.md, Cross-subject line for g3-pa-active-and-invite (already in
  this frame's For the lead 6): add the vigorous days, so it reads "the hour a day, aerobic most of it, some of it
  vigorous at least three days a week, with muscle-strengthening and bone-strengthening at least three days a week".
- docs/courses/social-and-emotional-learning-grades-3-to-5/frame.md, line 208 (two places): "health grade 5 unit
  17's refusal steps (weeks 10 to 14)" and "unit 17 (refusal, weeks 10 to 14)" become "weeks 10 to 13". Line 196's
  "health grade 3 unit 3 (weeks 10 to 14)" is right and stays.
- docs/APPROACH-SOURCES.md (source list): add CDC youth tobacco data
  (https://www.cdc.gov/tobacco/php/data-statistics/youth-data-tobacco/index.html) and CDC About bullying
  (https://www.cdc.gov/youth-violence/about/about-bullying.html).
- Browser check for the lead (Claude in Chrome): https://www.stopbullying.gov/bullying/what-is-bullying (403) and
  https://monitoringthefuture.org/results/annual-reports/ (403, day 70's norm).
- Lens spellings (lead call 13): docs/agents/lenses/health.md has none of the common UK spellings. Nothing to list.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check health-grades-3-to-5`: 0 failures. Notes: "standard None is on no day"
  for units 6, 7, 13, 14, 20 and 21, from the frame's "None" owned-standards cells (lead call 12, left as is).
- `python -X utf8 scripts/frame.py check health-grades-3-to-5`: 0 failures. Notes: unit days by year 3 26, 4 26, 5
  25; 21 units, 90 days.
- `python -X utf8 scripts/frame.py calendar`: no stagger-rule break for this course. Health weeks are 15/29 in grade
  3, 14/29 in grade 4 and 14/28 in grade 5, unchanged; no frame change moved a week.
