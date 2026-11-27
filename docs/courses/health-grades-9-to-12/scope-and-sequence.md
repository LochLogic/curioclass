# Scope and sequence: Health, grades 9 to 12

Course `health-grades-9-to-12` (catalog id `health-9-12`), grade 9 (one semester), draft, 2026-11-26.

The frame's 21 units keep their order, owned rows and day counts (4, 4, 3, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 4,
4, 4, 3 and 3), with the mid-course check and its respond day (days 35 and 36) and the end-of-course check and its
respond day (days 79 and 80): 80 course days of 45 minutes, five a week for 16 weeks. The CSV
(data/plans/health-grades-9-to-12/days.csv) is the day map; this page gives the reasons. Each unit is one section
(`unit` = `<unit>.1`), since no unit runs over four days.

## Calendar and school days

The course meets every school day of the fall half, so `school_day` = course day (filled on every row), and week =
(school_day - 1) // 5 + 1 gives the frame's weeks. A school that teaches it in the spring half adds 80 (weeks 17 to 32)
and keeps the order. All standards in the course are the 9 to 12 span's, met in grade 9: there is one year here, and
it is headed "Grade 9" below.

End-of-unit checks fall on days 4 (week 1), 8 (2), 11 (3), 15 (3), 18 (4), 22 (5), 26 (6), 30 (6), 34 (7), 40 (8), 44
(9), 48 (10), 51 (11), 54 (11), 58 (12), 60 (12), 64 (13), 68 (14), 72 (15), 75 (15) and 78 (16). The mid-course check
is day 35 (week 7) with its respond day 36 (week 8); the end-of-course check is day 79 with its respond day 80, both in
week 16, the finals week of a half-year course. These are the frame's weeks and calendar.csv's. Grades 9 to 12 have no
stagger rule but the finals week (CALENDAR.md rule 4), so the course breaks no calendar rule.

**The goal thread.** Ten-minute goal slots sit on days 6, 11, 16, 21, 26, 31, 37, 41, 46 and 54 (week 8's slot on day
37, since day 36 holds the respond work and a readiness check; week 11's on day 54, unit 14's check day, since day 51
holds unit 13's check and unit 14's readiness check). Each is named in its day's note with its step: the
first step done, a support used, a barrier met, a count, a revision, a support from another person, a barrier a new week
brought, a second count, a second revision, the log made ready. A day that holds a slot plans 35 minutes of its own
unit. The slots practice NHES.S6.12.4 and NHES.S6.12.5, owned by unit 16; they are named in the notes and not in the
`codes` column of the host unit, which holds only what that unit works on.

**Response time** for every end-of-unit check, named once here: the last five minutes of the check day are the unit's
second self-check (the student rates their use of the steps and names a next step, bar criterion 8; the first sits on
an earlier day of the unit, named in its note), and the marked sheets come back on the next unit's second day with a
five-minute re-try of one not-yet step on a new line. The course-level respond days (36 and 80) re-rehearse the rest.
In the spoken units (8, 9, 10 and 12) every student is heard on a class record sheet across the unit's last two days, at
two or three short pair stations the teacher moves between, half on each day; any student may write or use a card.

## Earlier-grade rows and their treatment

The count starts from grade 9 (rule 2, by grade number). Every grade 8 row opens as a retrieval task (named in the
`retrieves` column and the note); the two rows last used two or more grades back get a readiness check in the last ten
minutes of the day before their unit. Band entry: every non-sensitive day that retrieves a grade 8 row says that a
student new to Curio Class health shows any gap there and the teacher reteaches that step on the card the same day
(day 1: the one-page reminder card and a one-minute self-rating stand in for a grade 8 log; the sensitive units keep
their one-page fallback). Unit 1 has no readiness rows. g7-phw-living-with-conditions is a grade 7 row, but
grade 8's g8-phw-factors-shape-health assumes it and uses it in its asthma and air quality case, so by last use it was
used the year before and opens unit 5 day 2 as a retrieval task.

| Earlier row | Last used | First needed | Treatment |
|---|---|---|---|
| g8-phw-factors-shape-health | grade 8 | unit 1, day 1 | retrieval days 1, 5, 9 |
| g8-phw-goal-monitor; g8-phw-goal-effect | grade 8 | unit 1, days 1 and 3 | retrieval days 1, 3, 59 |
| g8-phw-health-care-services | grade 8 | unit 4, day 12 | retrieval day 12 |
| g8-phw-habits-personal-community | grade 8 | unit 5, day 16 | retrieval days 16, 52, 55 |
| g7-phw-living-with-conditions | grade 8 (in g8-phw-factors-shape-health's asthma case) | unit 5, day 17 | retrieval day 17 |
| g8-phw-handle-false-messages | grade 8 | unit 6, day 19 | retrieval day 19 |
| g8-meh-tools-for-influences | grade 8 | unit 7, day 23 | retrieval day 23 |
| g8-meh-teamwork; g8-meh-express-concern | grade 8 | unit 8, day 27 | retrieval days 27, 31 |
| g8-meh-different-views | grade 8 | unit 9, day 31 | retrieval day 31 |
| g8-v-negotiate-compromise | grade 8 | unit 10, day 37 | retrieval days 37, 39 |
| g7-s-online-boundaries | grade 7 | unit 10, day 37 | readiness day 36 (the mid-course respond day) |
| g8-aod-decision-supports-obstacles; g8-t-tobacco-influences | grade 8 | unit 11, day 41 | retrieval day 41 |
| g8-aod-refusal-and-driving | grade 8 | unit 12, day 46 | retrieval day 46 |
| g8-pa-decision-look-back | grade 8 | unit 12, day 45 | retrieval days 45, 49, 55 |
| g6-fn-eating-patterns | grade 6 | unit 14, day 52 | readiness day 51 (unit 13's last day) |
| g8-s-advocacy-results | grade 8 | unit 17, day 61 | retrieval day 61 |
| g8-fn-advocacy-audience; g8-pa-advocacy-practice | grade 8 | unit 18, day 65 | retrieval day 65 |
| g8-sh-prevention-and-health; g8-v-dating-and-assault; g8-meh-suicide-help | grade 8 (sensitive) | units 19, 20, 21, first days | retrieval days 69, 73, 76; if the grade 8 unit was left out, one plain page of the facts it needs |
| ela:e8-delineate-argument (RI.8.8) | ELA grade 8 unit 2 | unit 6, day 20 | retrieval day 20 |
| ela:e8-argument-writing (W.8.1) | ELA grade 8 unit 2 | unit 17, day 63 | retrieval day 63 |

Same-term rows return the same way, in `retrieves`: unit 2's five-level map in units 3, 7, 13 and 15; unit 4's access
map and source-check in units 5, 6, 7 and 19; unit 1's goal-plan in units 2, 5, 12, 14 and 15 and the slots; unit 8's
channels in unit 9 and its help steps in units 20 and 21; unit 10's boundary and conflict steps in units 11, 19 and 20;
unit 11's decision steps in units 12 and 13; unit 6's counter line and unit 9's teams in unit 17. SEL 9 to 12 unit 1's
support map (weeks 1 to 5, the same term) is retrieved on day 27; where the school does not run SEL 9 to 12, a one-page
support map (who helps with what, at school and nearby) is handed out and filled in the same 5 minutes.

## The shared cards (SEL STANDARD section 7, the 9 to 12 form)

Quoted word for word as SEL STANDARD section 7 gives the band's form, so a student meets one card in every course:
- **I-statement:** "I feel ___ when ___ because ___. I need ___. Does that work for you?" (modeled day 27, used in
  units 8 and 9).
- **Calm-down:** the calm-down steps become a coping plan: "the five steps, a tool for each of three settings, a back-up
  tool and a review date"; the five steps are "stop, breathe, name it, choose, go on". Health uses the steps for calming
  inside the conflict steps (day 39, and day 73's calming only) and names SEL's coping plan as a resource on day 23; it
  does not teach the plan.
- **Refusal:** the frame's card, "stop and think, say no clearly, give a reason or none, offer something else or walk
  away", with the options SEL 9 to 12 adds, "the plan made ahead, the ally and the second push", the second push being
  "say it again, move away, tell" (day 46).
- **Goal steps:** SEL 9 to 12's designed plan, "the goal, dated steps, the trade-off accepted, a check date, a verdict";
  health's goal-plan card (assess, choose a process, write, steps with supports and barriers, carry out, monitor, revise,
  evaluate) uses these words for the parts it shares (days 3, 59 and the slots).
- **Talk turn:** the card's first step is "choose how to talk (in person, a call or a message)", which is day 27's
  channel choice; health's listening steps are the talk turn card's listening steps after it, "listen, say back, ask a
  question" (day 28); SEL 9 to 12 adds a last step, "check what landed, plan the next talk", which health does not need
  here.

## Grade 9 (the semester)

Every unit follows the health unit shape: day 1 retrieves its step card and the teacher models it at span-12 depth on a
new case, pairs rehearse it (a fifteen-minute rehearsal inside a day, or the one Fluency day in units 10 and 21), the
card is withdrawn on the unit's last teaching day (the day before the check), whatever its kind, and the check is taken
without it; in the units of two or three days (3, 5, 13, 14, 16, 20 and 21) it is withdrawn for that day's last task.
Each unit's last teaching-day note says "Card withdrawn". In unit 10 the boundary card is withdrawn all of day 39 and
the conflict card, modeled that day, for its last task. Kinds follow GLOSSARY "teaching day": a day that
carries an indicator for its first time in the course is Understanding, even where students apply the steps on it, so
most teaching days are Understanding (51); the Fluency days (38, 77) practice what the day before taught; the
Application days (71, 74) use taught steps on new cases in the sensitive units. Every day names its behavior outcomes
(HECAT) in the note.

### Unit 1. Wellness and a goal

Course days 1 to 4, week 1. The arc goes from how the parts of wellness move together (day 1, the hook) to strengths
that help a group (day 2) to the student's own semester goal (day 3), so the first slot (day 6) has a goal to carry out.
Days by load: the goal row owns three indicators and gets the fuller day 3; each wellness indicator gets a day. No
readiness check (all rows are grade 8 rows: retrieval on day 1). End-of-unit check day 4: an unseen case with a prompt
for each part of the five codes (a strength that helps the character and one that helps a group; the factors that would
help or block the character's goal); the student's own goal sheet scored on its parts only. Candidate (teen sleep amounts): kept,
one sourced line inside day 1, no day cost.

### Unit 2. What gets in the way

Course days 5 to 8, weeks 1 to 2. The activity gap (25 percent, CDC Youth Risk Behavior Survey 2025) opens a question,
not a norm; day 5 builds the five-level map, day 6 separates benefits from supports and barriers, day 7 the three
prompts of confidence, likelihood and seriousness, each a separate part of its code. Check day 8 covers all three codes
on a new activity case, asking the behavior's benefits and, apart from them, one support and one barrier by level. Candidate (muscle and bone activity): kept, one sourced line inside day 5.

### Unit 3. Fair chances

Course days 9 to 11, weeks 2 to 3. Two places compared (day 9) before the levels are appraised for fairness (day 10), so
the appraisal has data to work on. Check day 11 (with goal slot 2; a 30-minute sitting) asks how income and
neighborhood shape the behaviors and results behind the gap, as well as the gap itself. Candidate (environmental health):
kept, one data card on day 9.

### Unit 4. Getting care

Course days 12 to 15, week 3. Why care matters (day 12), then who and what can be reached (day 13), then what blocks
access to information, products and services (day 14), each code on its own day. Check day 15 maps a new case, asks how
the character's access affects their wellness, and judges one information card, one product card and one service card
(a 40-minute sitting). Candidate
(health history and how to share it): kept, one scene inside day 13.

### Unit 5. Habits that prevent

Course days 16 to 18, week 4. Prevention habits ranked with sources (day 16), then condition care (day 17), which opens
with a retrieval task on g7-phw-living-with-conditions and uses unit 4's care map. Check day 18 adds one item judging a
habit, besides condition care, that supports health. Candidate (screenings and self-exams by age): kept, one
habit card on day 16.

### Unit 6. Information you can trust

Course days 19 to 22, weeks 4 to 5. How information skill shapes results (day 19) comes before rating sources on the
protein powder question (day 20), so students know why the rating matters; disinformation (day 21) follows rating, since
a counter needs a traced source. Check day 22 has a prompt for each of the four codes. Candidate (energy drinks and
caffeine): dropped here, because day 20's packet keeps one question for its reading load; its sourced line moves to unit
7 day 23, where caffeine is already an influence on the character's week (no day cost).

### Unit 7. Influences and my plan

Course days 23 to 26, weeks 5 to 6. Judge the influences (day 23), design the plan (day 24), use one school resource on a
step (day 25, a doing record). Check day 26 (goal slot 5; a 30-minute sitting) carries the day 25 record. SEL's coping
unit (weeks 6 to 11) comes just after: health names it and does not teach it. Candidate (stress management): kept, one
line inside day 24.

### Unit 8. Reaching people

Course days 27 to 30, week 6. Channels (day 27), relationships (day 28), then help and concern (day 29), whose spoken
record starts that day and ends on check day 30. SEL unit 1's support map (same term) is retrieved on day 27. The help
line card names 988 by purpose. Candidate (help a friend reach a counselor): kept, one scene on day 29.

### Unit 9. Teams and other views

Course days 31 to 34, week 7. Teamwork roles (day 31; teams formed for units 17 and 18), negotiation (day 32), adapting a
message to other views (day 33). The teamwork record runs over days 33 and 34, half the teams each day; check day 34 adds
an unseen written scenario per student. Candidate (respect differences): kept, one scene on day 33.

### Unit 10. Limits, consent and conflict

Course days 37 to 40, week 8. The day 36 readiness results open day 37 (limits and consent); day 38 is the course's
Fluency day, scripted rehearsal of what day 37 modeled; conflict (day 39) follows boundaries because walking away and
saying no again come from the boundary card. Spoken record over days 39 and 40; check day 40. No sexual content.
Candidate (online harassment): kept, one scene on day 37.

### Unit 11. Nicotine decisions

Course days 41 to 44, week 9. Day 41 opens on the norm (National Youth Tobacco Survey, latest edition; most high school
students do not vape) and the viewpoints; day 42 when a careful process is needed; day 43 runs it alone, with support and
in a group, with quit help named by purpose. Check day 44. Candidate (nicotine pouches): kept, one source card on day 41.

### Unit 12. Alcohol and other drugs

Course days 45 to 48, weeks 9 to 10. The norm (the latest Youth Risk Behavior Survey edition that reports past-month
alcohol use, 2023 at the expert read; most do not drink) and weighing
options with the medicine safety facts (day 45) come before refusal (day 46), so the refusal has a decision behind it;
the action plan (day 47) closes the decision. Spoken refusal record over days 47 and 48; check day 48. Candidate (cannabis
and state law): kept, one sourced line on day 45.

### Unit 13. Safety at many levels

Course days 49 to 51, weeks 10 to 11. A driving choice traced at five levels (day 49), then supports and barriers on the
road and at a first job (day 50). Check day 51 holds unit 14's readiness check (g6-fn-eating-patterns), a 30-minute
sitting; week 11's goal slot moves to day 54. Candidate (first aid and CPR): kept, one line on day 50 naming where a
school can add training.

### Unit 14. Meals that work for a group

Course days 52 to 54, week 11. Day 52 opens on the readiness results, judges group habits and plans three shared meals
on a budget from the invented flyer (the judgment of time, money and who cooks that NHES.S7.12.2 asks); day 53 is the
station day only: several distinct practices, each recorded per student (soap and towels from school stock, reusable
trays, the optional no-cook items about $45; allergies checked first, no knives, clean-up five minutes; eating
optional). Where the room has no sink, hand washing runs at the nearest sink in turns or the food stations move to a
room with one; sanitizer does not stand in for hand washing before food handling. Check day 54 carries the station
record and holds goal slot 10 (a 30-minute sitting). Candidate (food safety at home): kept, one line at day 53's
hand-washing station.

### Unit 15. When habits get harder

Course days 55 to 58, weeks 11 to 12, after the tenth slot, so the log has ten entries to count. What makes a habit
harder (day 55), measuring with simple data (day 56), then the adapted step done once in class (day 57, a doing record).
Check day 58 carries the day 57 record. Candidate (activity for life after school): kept, one line on day 57; PE grade
12 teaches it.

### Unit 16. My goal, looked back

Course days 59 to 60, week 12. Day 59 gathers and evaluates the log; check day 60 scores the log's process entries and
the evaluation, never whether the goal worked, plus an unseen character's log. The longer family notes for units 19 to
21 go home on day 59, two weeks before day 69. Candidate (a long-term health plan): kept, one line on day 59.

### Unit 17. Taking up a health issue

Course days 61 to 64, week 13. Factors that shape advocacy (day 61), self-advocacy (day 62), then the team's written ask
(day 63) with overnight feedback. Check day 64 assesses NHES.S8.12.1 and NHES.S8.12.4; NHES.S8.12.2, a team product, is
revised on day 65 and scored on day 68 with unit 18, as the frame's product rule now says (draft, written feedback and
revision across units 17 and 18), so days 65, 66 and 68 list it beside unit 18's rows. Candidate (safe school environments): kept; it already fits the issue list.

### Unit 18. Advocacy that reaches

Course days 65 to 68, weeks 13 to 14. Revise and adjust the ask, and each student writes a bystander plan for friends
(day 65); each team delivers its one issue ask in its two forms to real audiences in the school, and the delivery record
names the level each piece reaches: relationships (the bystander plans), community and environment (the issue ask),
society (the policy or rule change the leader is asked for) (day 66, a doing record); assess the reach and study a
coalition case (day 67). Check day 68 scores the revised ask, the delivery
record and each student's written assessment. Candidate (tobacco-free policy): kept, it is day 67's coalition case.

### Unit 19. Sexual health and consent (sensitive, removable)

Course days 69 to 72, weeks 14 to 15. Consent first (day 69), then prevention facts (day 70), then confidential services
(day 71), so the facts sit between the relationship skill and getting care. Check day 72, with one facts-in-use item
from day 70 (how a method prevents infection or pregnancy). Owns no indicator; practices
NHES.S4.12.4 and NHES.S3.12.1. Candidate (reproductive rights and state laws): kept, one line on day 70 that the school
adds its state's rules.

### Unit 20. Sexual violence, abuse and dating violence (sensitive, removable)

Course days 73 to 75, week 15. Telling disagreement from abuse comes first (day 73), so no student applies the
negotiation steps to abuse; getting help and the bystander line follow (day 74). Unit 19 is not a prerequisite. Check
day 75 asks students to choose the response route. Candidate (sexting and image-sharing laws): kept, one line on day 74
with the school's state rule.

### Unit 21. Suicide and self-harm: getting help (sensitive, removable)

Course days 76 to 78, week 16. The help line and the adult plan are on the first page of day 76; day 77 practices the
lines from scripts. Check day 78. Safe-messaging rules on every day. Candidate (self-harm help-seeking): kept, held to the
help step on day 77.

## Course-level checks

- **Mid-course check, day 35 (week 7); respond day 36 (week 8).** Samples units 2 to 8 on unseen cases, each answered
  alone in writing: NHES.S1.12.6, S1.12.7, S2.12.2, S3.12.1, S3.12.2, S3.12.3, S2.12.1, S4.12.1 and S4.12.3, each item
  asking every part of its code (S1.12.7: the behavior's benefits and, apart from them, one support and one barrier by
  level; S2.12.2: how income and neighborhood shape the behaviors and results behind the gap; S3.12.3: accuracy,
  trustworthiness and availability). It comes
  the day after unit 9's end-of-unit assessment, so it asks nothing of unit 9 and carries its teamwork record. Two task
  forms are changed from the frame's plain wording because the same form was given within two weeks: the influence item
  is a two-way chain completed from a new data card (unit 7's check, day 26, judged a character's week), and the help
  request is a channel choice and the repair of a draft message (unit 8's check, day 30, wrote one fresh). Day 36's last
  ten minutes hold unit 10's readiness check.
- **End-of-course check, day 79; respond day 80 (week 16, finals week).** Samples units 10 to 15, 17 and 18, with one
  item each from units 2 and 6: NHES.S4.12.4, S4.12.6, S5.12.2, S5.12.4, S5.12.5, S7.12.1, S5.12.8, S8.12.3, S1.12.7 and
  S3.12.3, with S1.12.7 and S3.12.3 asked in full as at the mid-course check. Carried, not re-scored: S7.12.4 (unit 14's station record), S6.12.4 and S6.12.5 (unit 16's log), S8.12.5
  (unit 18's delivery record). It follows unit 21, which it never samples, so no item repeats the check just given; the
  boundary item is an exchange to repair, not a fresh line, since unit 19's check (day 72) asked for a line. Units 19 to
  21 are never sampled, so leaving one out changes no check.

**Owned codes no course-level check samples** (rule 3), 33 of 54. The frame's check table sets one 45-minute sitting
each and names its items, so these are assessed only on their own unit's end-of-unit check (and doing records where
named): NHES.S1.12.1, S1.12.2, S6.12.1, S6.12.2, S6.12.3 (unit 1; the frame does not sample the goal sheet, and the goal
process is carried by unit 16's log); S1.12.8 (unit 2); S2.12.3 (unit 3); S1.12.9 (unit 4); S1.12.3, S1.12.4 (unit 5);
S1.12.5, S3.12.4, S3.12.5 (unit 6); S2.12.4, S2.12.5 (unit 7); S4.12.2, S4.12.10 (unit 8); S4.12.7, S4.12.8 (unit 9,
record carried at the mid-course check), S4.12.9 (unit 9); S5.12.1, S5.12.3 (unit 11); S4.12.5, S5.12.6 (unit 12);
S5.12.7 (unit 13); S7.12.2 (unit 14); S7.12.3 (unit 15, a doing record); S6.12.6 (unit 16); S8.12.1, S8.12.2, S8.12.4
(unit 17); S8.12.6, S8.12.7 (unit 18). For the lead 1 proposes the frame's structure pass weigh this.

## Coverage map

Behavior outcomes (HECAT 2021) by unit, the 9 to 12 column of STANDARD.md section 4; "(s)" is a sensitive unit.

| Topic | Outcomes carried | Units |
|---|---|---|
| Personal health and wellness (PHW) | 1, 2, 5 to 7, 9 to 12 | 1 (1, 2, 7), 2 (6, 7), 3 (6), 4 (10, 11), 5 (5, 6, 9), 6 (12), 16 (2, 7) |
| Food and nutrition (FN) | 1, 8, 10, 11 | 6 (1, 8), 14 (1, 8, 10, 11) |
| Mental and emotional health (MEH) | 1 to 9 | 6 (2, 9), 7 (2, 4, 9), 8 (1, 4, 8), 9 (7, 8), 10 (3, 8), 12 (5), 21 (6) (s) |
| Physical activity (PA) | 1, 2, 5 to 7 | 15 (1, 2, 5, 6, 7) |
| Safety (S) | 1 to 6, 8 | 12 (2), 13 (1, 3, 4, 5, 6, 8), 17 (8) |
| Violence prevention (V) | 1 to 10 | 10 (1, 2, 5, 6), 17 (7), 18 (3, 7), 20 (4, 8, 9) (s), 21 (10) (s) |
| Tobacco (T) | 1, 3 to 5 | 11 (1, 3, 5), 18 (3, 4) |
| Alcohol and other drugs (AOD) | 1 to 8 | 12 (1 to 8) |
| Sexual health (SH) | 1 to 10 | 19 (1 to 10) (s) |

NHES standards by unit (owned indicators; practiced in sensitive units in brackets). Every skill standard (2 to 8) is
practiced in at least two topics with units 19 to 21 taken out, as the frame lists.

| Standard | Units |
|---|---|
| 1 Health information | 1, 2, 4, 5, 6 |
| 2 Influences | 3, 7 |
| 3 Information and services | 4, 6 (19) |
| 4 Communication | 8, 9, 10, 12 (19, 20, 21) |
| 5 Decisions | 11, 12, 13, 15 |
| 6 Goals | 1, 16 (slots in units 2 to 13) |
| 7 Healthy behaviors | 14, 15 |
| 8 Advocacy | 17, 18 |

## Sensitive units and the leave-out path

Units 19, 20 and 21 each have a leave-out note on the first page and the longer family note (English and Spanish) sent on
day 59, at least two weeks before day 69; a student 18 or over gets the note and decides. Non-sensitive days that touch a
sensitive area name it in their note as "Sensitivity flag" with the frame's private routes (cases are characters'; any
student may take another case; a student who wants help talks privately with the nurse or counselor): body and food
(days 3, 20, 52), body and ongoing conditions (day 17), mental health, substances and food (day 21), mental health (days
23, 29, 30), substances (days 41 to 48), safety and loss (days 49, 51), food (days 53, 54), body, injury and eating
concerns (days 55 to 57). No non-sensitive unit assumes a
sensitive one; getting help is taught in units 4 and 8.

A school that leaves a unit out keeps its days where they sit (weeks 14 to 16), so no check or slot moves, and uses them
to extend the unit the frame names: unit 19's four days and unit 20's three extend unit 10 (new boundary and conflict
scenarios, the spoken record re-heard for students marked not yet, nothing new owned); unit 21's three extend unit 8
(new help and concern scenarios in a new channel). A student kept out of a unit the school teaches works on the same
extension that week. Leaving any of the three out changes no course-level check.

## Shorter path

**A shorter period (40 minutes).** Every day holds. The opening scenario drops to 3 minutes and each retrieval task to
3; the fifteen-minute pair rehearsals run 12. Slot days keep the 10-minute slot and give the unit 30 minutes. Check
sittings lose 5 minutes by printing the directions and pairing facts-in-use items where one case carries two facts, so
days 51 and 54 each keep a 25-minute sitting.

**A year about 10 days short (70 course days).** Ten fold-in days, each saving a 45-minute lesson; none holds an
assessment, a doing record, a slot or a readiness check, and no owned part is cut, since each day's code moves into a
neighbor's minutes:

| Fold-in day | Folds into | What the host day gives up | Minutes saved |
|---|---|---|---|
| 10 (fairness by level, S2.12.3) | day 9, whose data cards are read on the five-level map | one of the two places is studied as a class | 45 |
| 13 (who can be reached, S3.12.1) | day 14: the town map and the access cards on one sheet | the school list is filled in as a class | 45 |
| 19 (information skill, S1.12.5) | day 20: the clear and the confusing handout are the packet's first two sources | the label comparison | 45 |
| 24 (design the plan, S2.12.4) | day 25: the plan is designed with its resource step | the private plan becomes optional homework kept by the student | 45 |
| 28 (relationships, S4.12.2) | day 27: the channel templates are written to a friend, a manager and a doctor's office | the post template | 45 |
| 32 (negotiation, S4.12.8) | day 33: the values scenes are negotiated, then reworded | the 15-minute pair rehearsal is 8 | 45 |
| 38 (boundary rehearsal, Fluency) | days 37 and 39: 10 minutes of scripted rehearsal on each | one scenario on each day | 45 |
| 42 (when a careful process is needed, S5.12.2) | day 43: "is it a careful one" is the process's second step | the viewpoint card sort is one class sort | 45 |
| 55 (what makes a habit harder, S7.12.1) | day 56: the month record is read for helps and blocks before it is counted | one chart in place of two | 45 |
| 61 (factors that shape advocacy, S8.12.1) | day 63: teams map their own issue's factors before writing the ask | the past school change case | 45 |

Total: 450 minutes, ten of the frame's 80 days, leaving 70; every check, end, respond, readiness, slot and doing-record
day stays, and the course-level checks keep their weeks if the fold-ins come before them.

**Other reduced paths the frame names.** Leaving out a sensitive unit frees its days as above (up to 10 days with all
three out), with no assessed or owned part cut. A school that teaches the course in grade 10, 11 or 12 counts from that
grade: every grade 8 row in the table above then gets a 10-minute readiness check in place of its retrieval, in the last
ten minutes of the day before the unit that first needs it (unit 1's on day 1 after the hook; then days 11, 15 (joined to its check), 18, 22, 26,
30, 36, 40, 44, 60 and 64, and 68, 72 and 75 for the sensitive units; the two ELA grade 8 rows join the day 18 check,
e8-delineate-argument, and the day 60 check, e8-argument-writing), each host day giving the 10 minutes from its own
unit; a host day that also holds a slot moves the slot to the next day. A spring school keeps the order in weeks 17 to 32
with the end-of-course check in finals week 32; if seniors leave early, the respond day folds into the check day's second
half and the sensitive units' optional days give way first. The leave-out bridge rule needs no use here: no later unit
uses a card that only a sensitive unit makes.

## Sources not loaded

No source-map.csv (no base text; health is Curio Class's own). The HECAT 2021 topic modules (9 to 12 span tables) are
not read except Sexual Health in part, so every "Candidate kept" line waits for that read at the unit plan. Only the CDC
Youth Risk Behavior Survey 2025 physical activity page (day 5) was opened (by the frame's Codex read). Named from memory
and opened at the expert, safety or sensitivity read: the National Youth Tobacco Survey (day 41; the expert read opened the
2025 results, 7.1 percent of high school students used e-cigarettes in the past 30 days) and the Youth Risk Behavior
Survey alcohol item (day 45; the 2025 "Youth Health in Focus" pages have no alcohol page, so the figure comes from the
latest edition that reports it, 2023 at the expert read, rechecked at the unit plan); the NIH and FDA supplement pages and the federal dietary guidelines (day 20); the
federal activity guidelines (day 5); CDC chronic disease and vaccine pages (days 16, 17); the federal highway traffic
safety agency's teen driving pages (day 49) and the federal labor department's youth employment pages (day 50); CDC
"Clean Hands" and the federal food safety site (day 53); SAMHSA family pages (day 45); CDC and federal family planning
pages (day 70); CDC teen dating violence pages (days 73, 74); SAMHSA, "Preventing Suicide: A Toolkit for High Schools"
(2012) and the 988 Lifeline's safe-messaging pages (days 76 to 78). A page that refuses an automated read is kept as
browser check: the SAMHSA toolkit page (whether 2012 is still the latest edition) and the NIH dietary supplement
consumer page, both 403 at the expert read; the supplement fact itself was confirmed on FDA's page.

## For the lead

1. **Course-level checks sample 21 of 54 owned codes** (33 named above). The frame's check table limits each sitting;
   the structure pass may weigh adding a refusal for a new circumstance (S4.12.5) and a concern response (S4.12.10) to
   the end-of-course check, the two spoken skills the course leans on most.

The fix pass of 2026-11-26 settled the other items in the frame (day 51's crowding, S8.12.2 across units 17 and 18,
the changed course-level task forms, the leave-out days kept in place and the day kinds); see
docs/reviews/sequence-health-grades-9-to-12-fixes-2026-11-26.md.

No calendar rule is broken (grades 9 to 12: finals week only).
