# Expert read: scope and sequence of Health, grades 9 to 12 (2026-11-26)

Course `health-grades-9-to-12`. Cold read by the curriculum expert (PRODUCTION-PATH step 3), per
docs/pipeline/briefs/sequence-read.md and build/scope-writes/AFTERCORE-READ.md. I did not write the scope. This report
is the only file edited.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/health.md; docs/ADOPTION-BAR-SUBJECTS.md "3. Health" (items 1 to 10,
  "Fails if", "Scope and sequence states"); docs/courses/health/STANDARD.md and APPROACH.md in full; SEL STANDARD
  section 7 ("Shared steps").
- build/scope-writes/AFTERCORE-BRIEF.md (how the writer applied sequence-write.md).
- docs/courses/health-grades-9-to-12/scope-and-sequence.md in full; data/plans/health-grades-9-to-12/days.csv, all 80
  rows, every field.
- docs/courses/health-grades-9-to-12/frame.md in full; the grade 9 rows of data/progressions/health.csv and the rows
  of every assumed earlier row (to check last use); data/standards/nhes-2024.txt (the 54 `.12` lines);
  docs/courses/CALENDAR.md (rule 4 and the grade 9 table row) and the health and SEL 9 to 12 rows of
  data/plans/calendar.csv; the SEL 9 to 12 frame's Models row for the talk turn card; docs/GLOSSARY.md ("teaching
  day", "readiness check").
- Earlier reads, for REPEAT: docs/reviews/frame-health-grades-9-to-12-codex-2026-11-25.md,
  frame-health-grades-3-to-12-2026-11-25.md; DESK-ANSWERS entries of 2026-11-26 (after-core frame rules and calls,
  arts and computer science scope calls).
- Gates: `sequence.py check health-grades-9-to-12` 0 failures (notes: units 19 to 21 own no standard, as designed);
  `frame.py calendar` 0 failures for this course (21 units, 80 days, 76 in units); `plan.py check` shows no failure
  for this course; `stale.py check` 121 files, 0 failures.
- Outside pages opened (this run): CDC YRBS physical activity page; FDA National Youth Tobacco Survey results page;
  FDA press release on over-the-counter naloxone; FDA dietary supplement questions and answers; CDC YRBS "Youth
  Health in Focus" index and the Data Summary and Trends page. Two pages refused (browser check, below).

## Verdict

The scope is sound: it keeps the frame's 21 short units in a defensible order, places every one of the 54 owned
indicators on a teaching day and an end-of-unit check, puts every check on the frame's weeks, handles the three
sensitive units with the frame's guards, and its shorter paths cut nothing assessed. The biggest risk is in the check
wording: several end-of-unit and course-level items ask only part of the indicator they claim (S1.12.7 three times,
S1.12.9, S3.12.2, S1.12.1, S6.12.1), and the writer of the item bank will build from the goal text, not the
boilerplate "a prompt for each part". The one change that matters most is to reword those items (finding 1); next are
the crowded day 51 and the two overloaded hands-on days (findings 3 and 4).

11 findings: 1 serious, 6 moderate, 4 minor.

## Findings, most serious first

### 1. Check items ask only part of the indicator they claim (serious)

LAYER sequence, frame. REPEAT yes (the Codex frame read's finding 2, partial indicator demand; its fix for S1.12.7
itself dropped "supports"). Confidence: firm (nhes-2024.txt own words against the day goals).

- **What is wrong.** Each check day's note says "a prompt for each part of each code listed", but the goal, which is
  the item list a builder works from, misses parts:
  - **NHES.S1.12.7** (what a behavior gives a person and, apart from that, what helps and what gets in the way). Day 8:
    "name its benefits and two barriers" (no supports). Day 35: "one barrier" (no benefits, no supports). Day 79: "a
    barrier by level" (same). Day 6 teaches all three parts; no check asks for them together.
  - **NHES.S1.12.9** (how reaching care relates to wellness). Day 15 asks for options, blocks, a source and a route;
    nothing asks how the character's access affects wellness.
  - **NHES.S3.12.2** (information, products and services). Day 15's CSV goal: "judge one information, product or
    service source"; the .md says "one source of each kind". The CSV reading lets a builder ask one of three.
  - **NHES.S1.12.1** (strengths for individual and shared health). Day 4: "a strength that helps a group" only.
  - **NHES.S6.12.1** (assess own health and the factors that bear on a goal). Day 4 checks the character's goal, its
    process and health link, and the own sheet "for its parts"; no prompt asks for the factors bearing on the goal.
  - Smaller: day 11 and day 35 S2.12.2 "assess the gap" does not ask how income and neighborhood shape the behaviors
    and results behind it; day 18 S1.12.4 judges only condition care, not a habit that supports health; days 35 and
    79 S3.12.3 "rate a source" do not name the three criteria (accuracy, trustworthiness, availability).
- **Why it matters.** The check bank is written from these goals. A student can score "met" on S1.12.7 three times
  without once separating benefits from supports, which is the whole point of the 2024 wording.
- **Fix.** Reword the goals as in "Settled by the expert" rows 1 to 5; the frame's check table cells for S1.12.7 (both
  course-level checks) take the same words (lead).

### 2. A readiness check on a row last used the year before (moderate)

LAYER progression, frame. REPEAT new. Confidence: firm (health.csv).

- **What is wrong.** g7-phw-living-with-conditions gets a readiness check on day 15 because the frame and the grade 9
  row's note say it "returns after a skip". But g8-phw-factors-shape-health lists it in `assumes` and the grade 7
  row's `hands_on` names g8-phw-factors-shape-health (its asthma and air quality case). By rule 2 it was last used in
  grade 8, the year before, so it gets a retrieval task, not a readiness check. (g7-s-online-boundaries and
  g6-fn-eating-patterns are true skips: their hands_on names only the grade 9 row.)
- **Why it matters.** The rule is by last use in the progression; day 15 also loses 10 of its 45 minutes to it,
  leaving a 30-minute sitting for three codes.
- **Fix.** Either (a) day 17 opens with a 5-minute retrieval of condition care (retrieves
  g7-phw-living-with-conditions) and day 15 drops the readiness check (assess and note change; sitting back to 40
  minutes), with the frame's Readiness bullet and Seams row changed; or (b) the progression drops
  g7-phw-living-with-conditions from g8-phw-factors-shape-health's `assumes` if grade 8 does not in fact use it.
  I recommend (a): grade 8's asthma case does use condition care.

### 3. Day 51 holds a 20-minute check (moderate)

LAYER frame. REPEAT yes (frame read m4, the same crowding on day 36). Confidence: firm (arithmetic).

- **What is wrong.** Day 51 carries goal slot 10, unit 14's readiness check and the self-check, leaving 20 minutes to
  assess S5.12.5 and S5.12.7, each across five levels, plus facts-in-use and valuing items. The writer flagged it
  (For the lead 1) and kept it.
- **Why it matters.** Twenty minutes cannot hold a five-level trace and a supports-and-barriers judgment written
  alone; the check will be cut short or rushed.
- **Fix.** Slot 10 moves to day 54 (unit 14's check day, still week 11, after day 53's station work; its sitting
  becomes 30 minutes, as days 11 and 26 already are). Not day 52 as the writer proposed: day 52 takes the meal
  planning under finding 4. Day 56's count still follows slot 10. The frame's slot list changes (lead).

### 4. Days 53 and 66 hold more than a lesson (moderate)

LAYER sequence, frame. REPEAT new. Confidence: likely (from memory of a 45-minute class of 30).

- **Day 53.** Planning three shared meals on a budget from a flyer, then four or five practices at stations recorded
  per student for 30 students (hand washing at "one sink line", a clean serving area, safe serving, a label and
  portion, the optional assembly), plus five minutes of clean-up. Day 52 has one indicator and a 5-minute retrieval.
  Fix: the budget meal plan moves to day 52 (it is the judgment of time, money and who cooks that S7.12.2 asks), and
  day 53 is the station day only. Add a no-sink path: where the room has no sink, the hand-washing station runs at the
  nearest one in turns or the food stations move to a room with one; sanitizer is not the food-handling step.
- **Day 66.** Every team delivers "a bystander plan for friends, the school policy ask, and an ask for cleaner air or
  more shade" to real audiences, recorded per team, in one lesson, while day 65 built one issue's ask in two forms.
  Three deliveries per team cannot happen, and no line says which delivery reaches society. Fix: each team delivers
  its one issue's ask in its two forms (the one-page ask to a school leader, the poster or short talk for peers);
  each student writes the bystander plan (relationships) on day 65; the delivery record names the level each piece
  reaches: relationships (bystander plan), community and environment (the issue ask), society (the policy or rule
  change the leader is asked for). The frame's unit 18 day 2 text and the progression's g9-v-advocacy-adjust note
  take the same shape (lead).

### 5. NHES.S8.12.2 is claimed outside its owner unit (moderate)

LAYER frame. REPEAT new. Confidence: firm.

- **What is wrong.** Unit 17 owns S8.12.2, but days 65, 66 and 68 (unit 18) list it in `codes` and
  g9-s-advocacy-issue in `skills`, and unit 17's check (day 64) does not assess it. The read brief asks that no id be
  claimed outside the frame's owned rows. The writer explained why (For the lead 2): the frame's product rule says
  draft, written feedback and revision "inside the units' days", yet the frame's own unit 18 day 1 is the revision.
  The frame contradicts itself; the scope chose the workable reading.
- **Fix.** Keep the days as written and change the frame: unit 17's row says its S8.12.2 evidence is the team ask,
  revised on unit 18 day 1 and scored on unit 18's check day, and the Products sentence says "across units 17 and
  18". The alternative (revise and score on day 64) squeezes a 15-minute revision into a check day and duplicates
  day 65; I do not recommend it.

### 6. Sensitivity flags missing on days that touch substances, food, body and loss (moderate)

LAYER sequence. REPEAT new. Confidence: firm.

- **What is wrong.** The brief asks every health day touching body, substances, safety or mental health to name its
  flag in the note. Flags appear on days 3, 20, 23, 29, 41, 45, 49, 52 and the sensitive units. Missing: day 17
  (ongoing conditions, body), day 21 (posts on drugs, diets and mental health), days 42 to 44 (vaping decisions and
  quit help), days 46 to 48 (refusal of alcohol and drugs, help to stop use), day 30 (concern for a struggling
  friend), day 51 (safety case and loss), days 53 and 54 (food), days 55 to 57 (activity, injury, eating concerns).
  The scope's Sensitive units list names only the flagged days.
- **Fix.** Add "Sensitivity flag: <area>" with the frame's private route to each of those notes, and the same days to
  the scope's list (Settled row 9).

### 7. The step card's withdrawal day is not named (moderate)

LAYER sequence. REPEAT new. Confidence: likely.

- **What is wrong.** APPROACH ("What is carried") withdraws the card on the first application day and the frame says
  the same; units 1 to 18 have no Application day (GLOSSARY's kinds, correctly applied), and the scope says only that
  the card "is withdrawn before the check". A section writer cannot tell which day students first work without it.
- **Why it matters.** The check is taken without the card; if no teaching day withdraws it first, the check is the
  student's first try alone.
- **Fix.** One sentence in the scope's Grade 9 preamble: "the card is withdrawn on the unit's last teaching day (the
  day before the check), whatever its kind; in units 3, 5, 13, 14 and 16, the three-day and two-day units, it is
  withdrawn for the day's last task." Each unit's last teaching-day note says "card withdrawn". The frame's unit-shape
  sentence takes the same words (lead).

### 8. The talk turn card is misquoted (minor)

LAYER frame, sequence. REPEAT new. Confidence: likely (SEL 9 to 12 frame Models row).

- The scope and frame call the listening steps "the first three steps of SEL's talk turn card: listen, say back, ask
  a question". From grade 6 the card's first step is "choose how to talk (in person, a call or a message)", and 9 to
  12 adds a last step. Fix: "the talk turn card's listening steps (after its first step, choose how to talk): listen,
  say back, ask a question"; day 27's channel choice names the first step as the card's own. Shared-card rule:
  one wording in every course.

### 9. The YRBS alcohol figure's "latest edition" may not be 2025 (minor)

LAYER sequence. REPEAT new. Confidence: likely (pages opened).

- Day 45 cites "Youth Risk Behavior Survey, latest edition" for past-month alcohol use. CDC's 2025 "Youth Health in
  Focus" pages cover dietary behaviors, physical activity, sleep, digital behaviors and mental health only; no
  alcohol or substance page, and the Data Summary and Trends report runs 2013 to 2023. A planner told "latest
  edition" may hunt for a 2025 alcohol figure that is not published. Fix: day 45's note says "the latest YRBS
  edition that reports past-month alcohol use (2023 at this read; check for a 2025 release at the unit plan)". The
  other figures check out: YRBS 2025, 25% active at least 60 minutes daily over the past 7 days; NYTS 2025, 7.1% of
  high school students used e-cigarettes in the past 30 days (most do not); FDA approved the first over-the-counter
  naloxone nasal spray on 2023-03-29; FDA does not approve dietary supplements before they are marketed.

### 10. Day 27 has no bridge where SEL 9 to 12 is not run (minor)

LAYER sequence. REPEAT new. Confidence: firm.

- Day 27 retrieves SEL unit 1's support map (g9-rel-ask-offer-help). The lean meets SEL's days (SEL unit 1 weeks 1
  to 5, day 27 week 6), but many high schools run no SEL course. Fix: day 27's note adds "where the school does not
  run SEL 9 to 12, a one-page support map (who helps with what, at school and nearby) is handed out and filled in the
  same 5 minutes".

### 11. Small gaps in the checks and short path (minor)

LAYER sequence. REPEAT new. Confidence: firm.

- Day 72 (unit 19's check) names consent and services but no facts-in-use item on day 70's prevention facts, which
  are the unit's facts. Fix: add "one facts-in-use item from day 70 (how a method prevents infection or pregnancy)".
- The grade 10 to 12 path lists readiness host days for every grade 8 row but omits the two ELA grade 8 rows
  (e8-delineate-argument, e8-argument-writing), which are also two grades back then. Fix: join them to the day 18 and
  day 60 checks.

## Order, retrieval, calendar and paths: what holds

- **Order inside units:** each day builds on the one before; every model is used first in the unit the frame names
  (help-steps and source-check in unit 4, i-statement in 8, boundary and conflict in 10, decision in 11, refusal in
  12); the arcs reach their compelling questions. Unit 20 keeps negotiation out of abuse and supplies consent itself.
- **Readiness and retrieval:** every other assumed row is handled by rule 2 (grade 8 rows retrieved inside a day;
  g7-s-online-boundaries on the respond day 36; g6-fn-eating-patterns on unit 13's last day); no readiness check sits
  on any unit's first day; results shape day 2 or day 1 openings correctly. The only fault is finding 2.
- **Checks that do not repeat:** the mid-course check takes nothing from unit 9 and the end-of-course check nothing
  from unit 21, and both say so; task forms are changed where unit checks used them within two weeks.
- **Standards in full on teaching days:** all 54 owned ids sit on a teaching day; S1.12.7 and S1.12.8 are taught part
  by part; S6.12.4 and S6.12.5 run in ten weekly slots on the frame's days.
- **Calendar:** every unit and both course-level checks fall in the frame's and CALENDAR.md's weeks (school_day =
  course day, week formula stated); the end-of-course check is in finals week 16. Same-year leans to PE and SEL meet
  their weeks in calendar.csv.
- **Candidate cells:** all 21 settled, each with no day cost, one moved (caffeine to day 23) with its reason.
- **Shorter path:** the 40-minute path, the ten fold-in days (none holds an assessment, record, slot or readiness
  check, each code moved to a neighbor), the leave-out path, the grade 10 to 12 count and the spring and senior paths
  are all there, with nothing assessed cut.
- **Sensitive units:** leave-out notes, the family note on day 59 (two weeks before day 69), the 18-or-over rule,
  written scripts only, a card playing pressure, disclosure steps, 988 and the hotlines by purpose, safe-messaging
  rules and the counselor on call are on the right days.

## Lens checklist (scope and sequence layer)

| Line | State |
|---|---|
| Band reaches all eight standards | Met (standards table) |
| A skill standard practiced in only one topic | Met: each of 2 to 8 in two topics with units 19 to 21 out, as the frame lists |
| No coverage map, or cells with no units | Met: HECAT map by unit matches STANDARD.md's 9 to 12 column, plus an NHES table |
| A topic taught once with nothing after it | Met in this one-semester course: AOD and PA each have one unit, and each returns in the end-of-course check (S5.12.4 alcohol case; S7.12.1, S5.12.8) and in unit 6's posts or unit 2's case |
| A sensitive unit not removable | Met: no skill only there, no later unit assumes one, leave-out notes, days named to extend |
| Getting help only in a sensitive unit | Met: units 4 and 8 |
| Indicators in the wrong span | Met: all `.12` |

## What is right and should not be touched

- The ten weekly goal slots with one named step each, and unit 16 as the log's evaluation, never scored on whether
  the goal worked.
- The norm days (NYTS on day 41, YRBS on day 45) kept apart from the unit 2 activity gap, which is framed as a gap.
- Spoken-skill records at pair stations across two days, with writing or a card always allowed.
- The leave-out days kept in place (weeks 14 to 16), so no check or slot moves.
- The 33 unsampled owned codes named with their reason (For the lead 3); the structure pass should weigh the writer's
  two proposed additions (S4.12.5, S4.12.10).

## Settled by the expert

| # | Choice | Reason | File |
|---|---|---|---|
| 1 | S1.12.7 items read "the behavior's benefits, and apart from them one support and one barrier by level" on days 8, 35 and 79 | The indicator has three parts | days.csv 8, 35, 79; frame check table (lead) |
| 2 | Day 15 adds "how the character's access affects their wellness" and reads "judge one information card, one product card and one service card for what opens or blocks access" | S1.12.9 and S3.12.2 in full; matches the .md | days.csv 15 |
| 3 | Day 4 reads "a strength that helps the character and one that helps a group" and adds "the factors that would help or block the character's goal" | S1.12.1, S6.12.1 in full | days.csv 4 |
| 4 | Days 11 and 35 S2.12.2 item adds "how income and neighborhood shape the behaviors and results behind the gap"; days 35 and 79 S3.12.3 items name accuracy, trustworthiness and availability | Whole indicator | days.csv 11, 35, 79 |
| 5 | Day 18 adds one item judging a habit that supports health besides condition care | S1.12.4 in full | days.csv 18 |
| 6 | Goal slot 10 moves from day 51 to day 54 (sitting 30 minutes) | Day 51's 20-minute sitting; day 52 takes the meal plan | days.csv 51, 54; scope slot lists; frame slot list (lead) |
| 7 | Unit 14 day swap: the budget meal plan moves to day 52; day 53 is stations only, with a no-sink path | Day load | days.csv 52, 53; scope unit 14 |
| 8 | Day 65 adds each student's written bystander plan; day 66 delivers one issue's ask in two forms; the delivery record names the level each piece reaches | One deliverable a team; S8.12.5's four levels named | days.csv 65, 66; scope unit 18 |
| 9 | Sensitivity flags added on days 17, 21, 30, 42 to 44, 46 to 48, 51, 53, 54, 55 to 57 | Subject note | days.csv notes; scope Sensitive units list |
| 10 | Card withdrawn on each unit's last teaching day, named in its note | APPROACH "What is carried" | scope preamble; days.csv notes |
| 11 | Listening steps quoted as the talk turn card's steps after "choose how to talk" | One card wording | scope Shared cards; days.csv 27, 28 |
| 12 | Day 45 figure: "latest YRBS edition that reports past-month alcohol use (2023 at this read)" | No 2025 alcohol page found | days.csv 45; scope Sources |
| 13 | Day 27 bridge: a one-page support map where SEL 9 to 12 is not run | Same-year lean bridge | days.csv 27 |
| 14 | Day 72 adds one facts-in-use item from day 70 | The unit's facts | days.csv 72 |
| 15 | Grade 10 to 12 path joins the two ELA grade 8 rows to the day 18 and day 60 readiness checks | Rule 2 by grade | scope Shorter path |

## For Cory

- None. Every finding is inside the frame's scope; findings 2, 3, 5 and 7 change frame wording, which is the lead's.

## What I could not judge

- The HECAT 9 to 12 module span tables (unread, as the scope says), so whether each "Candidate kept" line is right.
- Browser check: SAMHSA, "Preventing Suicide: A Toolkit for High Schools"
  (https://library.samhsa.gov/product/preventing-suicide-toolkit-high-schools/sma12-4669, 403): whether 2012 is still
  the latest edition. NIH Office of Dietary Supplements consumer page (https://ods.od.nih.gov/factsheets/WYNTK-Consumer/,
  403); the same fact was confirmed on FDA's page.

## Sources

- CDC, YRBS physical activity (https://www.cdc.gov/yrbs/youth-health-in-focus/physical-activity.html): 2025, 25%.
- CDC, Youth Health in Focus index (https://www.cdc.gov/yrbs/youth-health-in-focus/index.html): 2025 topics, no
  alcohol page; Data Summary and Trends (https://www.cdc.gov/yrbs/dstr/index.html): 2013 to 2023.
- FDA, NYTS results (https://www.fda.gov/tobacco-products/youth-and-tobacco/results-annual-national-youth-tobacco-survey-nyts):
  2025, 7.1% of high school students.
- FDA press release (https://www.fda.gov/news-events/press-announcements/fda-approves-first-over-counter-naloxone-nasal-spray):
  2023-03-29.
- FDA, dietary supplements Q&A (https://www.fda.gov/food/information-consumers-using-dietary-supplements/questions-and-answers-dietary-supplements):
  no approval before marketing.

## For the source list

- The FDA NYTS page moved to the `-nyts` address above (the old address redirects).
- CDC YRBS 2025 "Youth Health in Focus" pages exist for five topics only; substance figures still come from 2023.
