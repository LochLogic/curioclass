# Scope and sequence: Health, grades 3 to 5

Course `health-grades-3-to-5`, grades 3, 4 and 5 (one band course, one part per grade year). Draft, 2026-11-26;
fixed the same day from the expert read. The days are in data/plans/health-grades-3-to-5/days.csv; the frame is
docs/courses/health-grades-3-to-5/frame.md, whose units, owned rows and day counts are kept unchanged.

## How the band runs

- **Years.** Course days 1 to 30 are grade 3 (units 1 to 7), 31 to 60 grade 4 (units 8 to 14), 61 to 90 grade 5
  (units 15 to 21). Each grade's own NHES 3-5 indicators fall in its year: grade 3 owns 11 (units 1 to 5), grade 4
  owns 14 (units 8 to 12), grade 5 owns 14 (units 15 to 19). The sensitive units (6, 13, 14, 20, 21) and unit 7 own none.
- **Meeting days.** One 30-minute lesson a week, weeks 1 to 30 of each 32-week school year; weeks 31 and 32 hold
  core year-end checks and no health. `school_day` = (year - 1) x 150 + (week - 1) x 5 + 3, so each lesson sits
  midweek and week = ((school_day - 1) mod 150) // 5 + 1 within its year; 150 is the span `scripts/frame.py` gives one
  year of this band (30 meeting weeks). Grade 5 alone has one change: week 10 holds two lessons (course days 70 and
  71, school days 347 and 349) and week 15 none, because the grade 5 mid-year check is pinned to week 14
  (course-list.csv `pins`) after 14 unit days.
- **Day kinds.** Set by what the day does (GLOSSARY "teaching day"). At one lesson a week nearly every row gets one
  day of its own, so most teaching days first teach a row and are Understanding, each with a short pair rehearsal
  inside; Application marks a day that uses a known skill on new cases without the card (days 13, 33, 48, 73, 81,
  82), and the one whole Fluency day is day 41 (rehearsing the ask). Every unit's last day is its Check.
- **Step cards.** The teacher holds the model the first time a card is used, pairs hold it the next time, it is
  withdrawn on the day the note says before its unit's check, so no check is the first use without it: the help-steps
  and decision-steps cards on day 13, the I-statement and the listening steps on day 20, the decision-steps card for
  day 38's last case, the ask on day 42, the source check on days 48 and 66, the refusal card on day 53's team ask,
  the look-back on day 73, the conflict steps on day 78, and the rest as their notes say. One card is the exception: the speak-up plan is held through day 53 and first used unaided
  at the unit 12 check (day 54). The shared cards are quoted word for word in the grades 3 to 5 form, cited as "SEL 3
  to 5 frame, from STANDARD section 7" (SEL STANDARD section 7 itself gives the K to 2 and 6 to 12 forms): the
  I-statement "I feel ___ when ___ because ___. I need ___."; the calm-down card "stop, breathe, name it, choose";
  SEL's refusal card "stop and think, say no clearly, give a reason, offer something else or walk away", then
  health's own line after it, "a reason is optional, and leaving is always allowed"; the talk turn card's first three
  steps "listen, say back, ask a question" as the listening steps; the goal steps card's rungs "goal, steps, block and
  plan, check" inside health's goal plan.
- **End-of-unit checks.** Unseen short written scenarios read aloud on request, scored on the skill steps with a
  guide (met, partly, not yet), one facts-in-use item per unit fact and one valuing item scored on the reason, never
  on the choice. Response time is counted once: the marked sheet comes back at the start of the next lesson and each
  student redoes one "not yet" step as that lesson's exit ticket, so the next lesson's opener stays its retrieval
  task. After units 7, 14 and 21 the next lesson is a course-level check, so the sheet comes back privately on the
  respond day (days 30, 60, 89). The course-level respond days re-rehearse every "not yet" step. Self-check cards
  fall twice in each unit (the notes name the days). Spoken steps (units 4, 10, 12, 18) are heard across the unit's
  last two days at two or three pair stations, as the frame sets them. An assess row lists only the codes an item
  asks in full; the sensitive units' and unit 7's checks list the codes they practice and say "practiced, not scored".
- **Each part of each code.** NHES 3-5 indicators carry no lettered parts; where an indicator has two halves or more
  (own and others' health in S2.5.2; people and communities, and why, in S2.5.3; facts, products and services in
  S3.5.3; both halves of S4.5.4; giving and asking in S4.5.3; stay out of, handle and settle in S4.5.6; self and
  others in S5.5.5; illness and injury in S1.5.3; whether and who in S5.5.2; when and the reason in S1.5.7; how
  finding information helps a choice in S1.5.5; teamwork and communication in S8.5.2) the teaching day and every check
  that lists the code hold a prompt for each part (days 24, 39, 44, 49, 54, 59, 69, 74, 75, 79 and 88 name them).
- **Begun ids.** A day that begins a row a later grade owns lists it as `~ID` in `codes` (days 3, 20, 25, 27, 33).
- **Sensitivity flags.** A non-sensitive day that touches a sensitive area names it in its note as "Sensitivity flag:
  <area>" with the private route (cases are characters'; any student may take another case, and a student who wants
  help talks to the teacher or the counselor): food (days 6, 80), substances (days 8, 51), bullying, safety and harm
  (day 19), body and ongoing conditions (day 36), alcohol and other drugs (day 70). "Sensitivity read" names the
  sources the sensitivity reader checks.
- **Every day ties to a behavior outcome**, named as `HBO:` in its note (bar criterion 1). Every day sends no home
  question about the child's own home, food, body, feelings or family; scenarios are characters'.

### Readiness and retrieval (rule 2)

No readiness check: every earlier-grade row any unit assumes was last used the grade before, so each opens as a
five-minute retrieval task inside the day that needs it (the `retrieves` column). Grade 3 picks up grade 2 rows of
Health, grades K to 2 (units 12 to 16 of that frame); grades 4 and 5 pick up the band's own earlier year.

| Year | Earlier row, last used | Treatment, day |
|---|---|---|
| 3 | g2-phw-why-health-matters (grade 2) | retrieval, days 1 and 22 |
| 3 | g2-phw-stopping-germs (grade 2) | retrieval, day 2 |
| 3 | g2-pa-invite-friends-to-move (grade 2) | retrieval, day 3 |
| 3 | g2-meh-people-are-different (grade 2) | retrieval, days 5 and 18 |
| 3 | g2-fn-pick-best-snack (grade 2) | retrieval, days 6 and 12 |
| 3 | g2-t-no-thanks-smoke (grade 2) | retrieval, day 8 |
| 3 | g2-s-find-school-helpers (grade 2) | retrieval, day 10 |
| 3 | g2-phw-doctor-nurse-visit; g2-s-outdoor-and-home-safety (grade 2) | retrieval, days 11 and 13 |
| 3 | g2-meh-feelings-calm-and-talk; g2-v-settle-it-with-words; g2-v-my-limits-say-stop (grade 2) | retrieval, days 17, 19, 20 |
| 3 | g2-phw-goal-do-it (grade 2) | retrieval, day 22 |
| 3 | g2-v-body-safety; g2-sh-bodies-grow-respect (grade 2, sensitive) | retrieval in the leave-out bridge's form, days 25 (sensitive unit 6) and 27 (unit 7, one respect scene) |
| 4 | g3-phw-set-goal; g3-phw-grow-strengths; g3-phw-goal-alone-or-together (grade 3) | retrieval, days 31, 32 |
| 4 | g3-pa-active-and-invite (grade 3) | retrieval, days 33 and 53 |
| 4 | g3-phw-habits-look-closely; g3-phw-find-resources; g3-s-decide-careful (grade 3) | retrieval, days 35, 36, 37 |
| 4 | g3-meh-feelings-say; g3-s-which-helper (grade 3) | retrieval, day 40 |
| 4 | g3-phw-influences-on-health; g3-fn-added-sugar-drinks (grade 3) | retrieval, days 46, 47 |
| 4 | g3-v-my-limits-and-yours; g3-meh-listening; g3-t-tobacco-facts; g3-v-bullying (grade 3) | retrieval, days 50, 51, 52 |
| 4 | g3-v-body-safety (grade 3, sensitive); g3-sh-respect-all-people (grade 3) | retrieval in the bridge's form, day 55; retrieval, day 57 |
| 5 | g4-phw-goal-plan; g4-meh-calm-stress (grade 4) | retrieval, day 61 |
| 5 | g4-pa-warm-up (grade 4; g5-pa-habit-practice assumes it) | retrieval, day 61 (one line) and day 62 |
| 5 | g4-fn-food-claims-source-check; g4-phw-how-things-affect-us; g4-phw-routines-and-conditions (grade 4) | retrieval, days 65, 67, 68 |
| 5 | g4-t-saying-no; g4-s-get-help-emergency; g4-meh-same-thing-different-people (grade 4) | retrieval, days 70, 71 |
| 5 | g4-fn-compare-options; g4-s-decide-with-help; g4-phw-prevent-illness-injury (grade 4) | retrieval, day 72 (compare-options again on day 81) |
| 5 | g4-v-limits-and-respect; g4-meh-calm-stress (grade 4) | retrieval, days 77, 78 (and day 86) |
| 5 | g4-phw-advocacy-teams; g4-v-speak-up-notice; g4-t-saying-no (grade 4) | retrieval, days 80, 81 |
| 5 | g4-v-body-safety; g4-sh-body-changes (grade 4, sensitive) | retrieval in the bridge's form, days 84 and 86 (day 86's opener is the puberty review) |

The ELA lean of unit 19 (W.4.1, ELA grade 4 unit 3, the year before) is a retrieval inside day 81, beside the group
draft that uses it.

## Grade 3 (course days 1 to 30, weeks 1 to 30)

### Unit 1. Parts of wellness (days 1 to 4, weeks 1 to 4)

The wheel comes first because every later unit sorts by the parts of wellness. Day 1 builds the wheel (S1.5.2),
day 2 teaches the look-closely steps on four habits and who each helps (S7.5.1), day 3 adds the activity guideline (with the
vigorous days) and the invite line and has pairs use the look-closely steps on an active habit without the card, and day 4 is the
end-of-unit check (an action per part, who a habit helps, an invite line, a valuing item on skipped sleep). PE unit 1
runs the same weeks; health gives the why. Candidate settled: brushing and flossing kept as a fifth habit card on day
2, no day cost.

### Unit 2. What shapes my health (days 5 to 9, weeks 5 to 9)

Day 5 models the influence check on a character's case; days 6 and 7 carry it into food groups and added sugar,
with pairs holding the card on the drink ad; day 8 states the tobacco facts and the plain-word norm and withdraws
the card on an invented vape ad (the norm sourced to the National Youth Tobacco Survey 2025, middle school);
day 9 is the end-of-unit check. One skill across three topics, so the card is
modeled, held and withdrawn inside the unit. Candidates settled: breakfast kept as one line on day 6; "secondhand
smoke at home is never the child's fault" kept as one line on day 8; no day cost.

### Unit 3. Helpers and careful choices (days 10 to 14, weeks 10 to 14)

Helper first (day 10, S3.5.1), then resources and the "where to go" list with the medicine and alcohol rule (day
11, S3.5.2), then careful choices (day 12, S5.5.1), then deciding by place with both cards withdrawn (day 13); day 14 is the
end-of-unit check, judging S3.5.2 from the student's list. The getting-help unit of grade 3 sits in a non-sensitive
place and before the mid-year check. Candidate settled: a fire escape plan case and a pedestrian case kept inside
day 13's case set, no day cost.

### Unit 4. Saying it, hearing it, and standing up (days 17 to 21, weeks 17 to 21)

After the mid-year check. The I-statement is modeled (day 17), held by pairs while the listening steps are taught
(day 18), bullying is told apart from disagreement with the federal definition's three features (day 19, CDC "About
bullying"), and limits
are stated with the boundary steps while the I-statement is heard from a third of the class and both cards are withdrawn
(day 20). The listening record for S4.5.2 runs days 19 to 21; day 21 is the end-of-unit check and hears the rest. SEL unit
1 taught the feelings words before it; SEL unit 4 (weeks 17 to 21) runs the talk turn card side by side; SEL unit 5 grows the upstander plan after it. Candidate settled: "ways to
show care when a friend is upset" kept inside day 18's scenes, no day cost.

### Unit 5. Strengths and a goal (days 22 to 24, weeks 22 to 24)

Day 22 grows a strength and writes a goal sentence (S1.5.1, S6.5.1), day 23 sorts alone, helper or team (S6.5.2),
day 24 is the end-of-unit check on the student's own goal or a character's, with its own item on how to grow a
strength. The family note for unit 6 goes home on day 23 (two weeks ahead), so it does not ride on a
removable unit's day. Candidate settled: "name a person who can help with a goal" kept inside day 23's sort.

### Unit 6. Telling more than one adult (sensitive, removable; days 25 and 26, weeks 25 and 26)

Day 25 teaches the idea and the telling line; day 26 practices it on written scripts and holds the end-of-unit check.
Practices S3.5.1; owns nothing. If left out, its days extend unit 4. Candidate settled: an online picture request as
a reason to tell, kept as one telling scene on day 25.

### Unit 7. Respect for every person (days 27 and 28, weeks 27 and 28)

Day 27 is a story read aloud and the healthy-friendship signs; day 28 the end-of-unit check. An
ordinary unit, the way SEL's models show families of every kind: it holds no body or relationship-history
content, so it has no leave-out note and no longer family note (Cory, 2026-11-26, Desk q-health-family-1). Candidate settled: "families differ and all deserve respect" is already in day 27.

## Grade 4 (course days 31 to 60, weeks 1 to 30)

### Unit 8. A plan for a goal (days 31 to 34, weeks 1 to 4)

First in grade 4 because SEL unit 8 (weeks 6 to 10) leans on the plan. Day 31 models the plan (S6.5.3), day 32 helps
and blocks (S6.5.4), day 33 applies the plan without the card to an activity week beside PE unit 9, day 34 is the
end-of-unit check. Candidate settled: "choose activities you enjoy" kept as one line on day 33.

### Unit 9. Staying well and deciding with help (days 35 to 39, weeks 5 to 9)

Prevention with the sourced germ and vaccine fact (day 35, S1.5.3), routines and a condition case whose written
explanation is the S1.5.4 evidence (day 36), the decision step "ask if it needs help" (day 37, S5.5.2), and the
if-then chart (day 38, S5.5.3, the card withdrawn for its last case); day 39 is the end-of-unit check. Candidates settled: hearing and vision checks and
food safety at home kept as one sort card each on day 35.

### Unit 10. Help with feelings and emergencies (days 40 to 43, weeks 10 to 13)

Stress signs, the shared calm-down card and the modeled ask (day 40), the whole-class Fluency rehearsal of the ask and
the listening reply, with the national crisis line named by purpose (call or text 988) (day 41), emergencies on a paper phone with the ask heard from a third (day 42), and the
end-of-unit check with the rest heard (day 43). Before the mid-year check; SEL unit 10 opens with day 40 as
retrieval. Candidate settled: "tell an adult if a friend talks about being hurt" kept as one script on day 41, held
to telling an adult.

### Unit 11. Influences and claims (days 46 to 49, weeks 16 to 19)

Day 46 takes both influence indicators on paired cases; day 47 models the source check in week 17, the week ELA
grade 4 unit 3 opens (the day's note carries the frame's "if later" bridge, since the two run side by side); day 48
uses it on a label, a service flyer and, alone without the card, a fact sheet; day 49 is the end-of-unit check.
Candidate settled: "read the serving line on a label" kept as one item on day 48, comparing whole numbers only.

### Unit 12. Limits, no, and speaking up (days 50 to 54, weeks 20 to 24)

The heaviest grade 4 unit: limits (day 50), the refusal card from SEL with health's addition and the norm (day 51),
the refusal rehearsed and heard from a third while the speak-up plan's first two steps are taught (day 52), the whole
speak-up plan in a team ask with the refusal card withdrawn (day 53; the speak-up plan is held through it and first
unaided at the check), and the end-of-unit check with the rest heard (day 54). SEL unit 11 (weeks 21
to 25) runs beside it. The family notes for units 13 and 14 go home together on day 53. Candidate settled: secondhand smoke and
smoke-free places kept as one line on day 51.

### Unit 13. Telling works (sensitive, removable; days 55 and 56, weeks 25 and 26)

Day 55 teaches the plain words and the tell-script; day 56 practices it and holds the end-of-unit check. If left out,
its days extend unit 12. Candidate settled: the secret line is already in day 55.

### Unit 14. Growing up (sensitive, removable; days 57 and 58, weeks 27 and 28)

Day 57 teaches body changes and hygiene with wide variation in timing; day 58 answers the anonymous question box and
holds the end-of-unit check. Its family note went home on day 53, and the school offers a private nurse or counselor
route (Cory 2026-11-26). If left out, its days extend unit 11. Candidate settled: "hormones cause the changes" kept
as one plain line on day 57.

## Grade 5 (course days 61 to 90, weeks 1 to 30)

### Unit 15. Habits that last (days 61 to 64, weeks 1 to 4)

The habit log runs the unit's four weeks, one lesson a week: start (day 61, S7.5.2), track with a check-in (day 62,
S6.5.5), reflect and change a step (day 63, S6.5.6), and the end-of-unit check on the log, the check-in record and
the reflection (day 64). One log, not two, where PE unit 17 runs. Candidate settled: limiting screen time before bed
kept as one safe-list choice on day 61.

### Unit 16. Finding good information and care (days 65 to 69, weeks 5 to 9)

The source check returns with the card for one day (day 65, S1.5.5), is withdrawn on harmful claims (day 66,
S3.5.4), then surroundings (day 67, S1.5.6) and when to get care (day 68, S1.5.7); day 69 is the end-of-unit check.
Candidate settled: dental and vision checkups kept as one case on day 68.

### Unit 17. Choices under pressure, online and off (days 70 to 74, weeks 10 to 13)

Days 70 and 71 share week 10 (see How the band runs). Alcohol and drug facts with the norm and the refusal steps
(day 70), online safety and tools for influences (day 71, S2.5.4), the full decision steps (day 72, S5.5.4), the
look-back without the card (day 73, S5.5.5), and the end-of-unit check (day 74). After unit 16, so facts are judged
before they are used in a choice. Candidates settled: medicine labels and doses kept as one case on day 70 (no dose
math); gaming chat kept as one case on day 71, no app named.

### Unit 18. Getting along (days 77 to 79, weeks 17 to 19)

The full conflict steps, heard from half the class (day 77, S4.5.6), kindness when we disagree with the rest heard
(day 78, S4.5.7), and the end-of-unit check (day 79). SEL unit 16 runs beside it. Candidate settled: one online
conflict script kept on day 77.

### Unit 19. Speaking up for health (days 80 to 83, weeks 20 to 23)

Approaches and audience with the snack-day plan (day 80, S8.5.3), the group draft (day 81), written feedback and
revision (day 82), and delivery to a real audience as the end-of-unit check (day 83, S8.5.4). The product's draft
and revision days come before the scored delivery, inside the unit's four days. The family notes for units 20 and
21 go home together on day 82. Candidate settled: tobacco-free rules at school kept as one line on day 80.

### Unit 20. Signs and helpers (sensitive, removable; days 84 and 85, weeks 24 and 25)

Day 84 teaches the signs and helpers a step deeper than grade 4; day 85 practices the telling line and holds the
end-of-unit check. If left out, its days extend unit 18. Candidate settled in its narrow form: "a request to keep a
secret or send a picture is a reason to tell", no grooming detail.

### Unit 21. Consent and health (sensitive, removable; days 86 and 87, weeks 26 and 27)

Day 86 opens with the puberty review as its retrieval, teaches everyday consent and the HIV basics, and collects
question-box slips; day 87 answers them, then holds the end-of-unit check. If left out, its days extend unit 19. Candidate settled: "HIV is not spread by everyday contact" kept as one
plain line on day 86.

## Course-level checks

Every course-level check is one character's week or month told in short scenes read aloud, each scene asking for one
step, so its form differs from the end-of-unit checks' separate scenario cards given a week before. Each is followed
by a respond day that re-rehearses each "not yet" step on a new scenario, in groups from the class record sheet. No
check samples a sensitive unit, and records collected child by child (spoken steps, the listening record, the
routine record, the habit log, the delivered message) are carried, never collected again.

| Check | Day, week | Samples (codes listed on the day) | Respond |
|---|---|---|---|
| Grade 3 mid-year | day 15, week 15 | S1.5.2, S7.5.1, S2.5.1, S3.5.1; the unit 3 item (the right helper) set inside a unit 1 or 2 situation, not a unit 3 case | day 16, week 16 |
| Grade 3 year-end | day 29, week 29 | S4.5.1, S4.5.2, S6.5.1, S6.5.2, S1.5.1, S2.5.1, S5.5.1 | day 30, week 30 |
| Grade 4 mid-year | day 44, week 14 | S6.5.3, S6.5.4, S1.5.3, S5.5.2, S5.5.3, S4.5.3; the unit 10 item (the ask) set on a goal block or decision from units 8 and 9 | day 45, week 15 |
| Grade 4 year-end | day 59, week 29 | S2.5.2, S2.5.3, S3.5.3, S4.5.4, S4.5.5, S8.5.1, S8.5.2, S6.5.3, S5.5.3 | day 60, week 30 |
| Grade 5 mid-year | day 75, week 14 (pinned) | S6.5.6, S1.5.5, S3.5.4, S1.5.6, S1.5.7, S5.5.4; the unit 17 item (decision steps) set on a claim or care choice from unit 16 | day 76, week 16 |
| Grade 5 year-end | day 88, week 28 | S4.5.6, S4.5.7, S8.5.3, S1.5.7, S5.5.5, S2.5.4 | days 89 and 90, weeks 29 and 30 (the second is the band look-back) |

All six sit on the frame's weeks and the CALENDAR.md table, off each grade's core check weeks; `frame.py calendar`
shows no stagger-rule break for grades 3, 4 or 5 (grade 4's week 15 SEL check sits beside a health respond day, not a
check).

**Owned codes not sampled on any course-level check, and why** (rule 3): NHES.S3.5.2 (its evidence is the student's
own "where to go" list, judged once on day 14); NHES.S1.5.4 (the unit 9 case explanation and routine record, judged on
day 39 and carried into the grade 4 mid-year check); NHES.S7.5.2 and NHES.S6.5.5 (doing indicators met by the unit 15
log and the teacher's record of each student at school, carried into the grade 5 mid-year check); NHES.S8.5.4 (the
real-audience delivery, judged once on day 83). Each is a product or an observed performance that a sitting cannot
stand for; every other owned code is sampled at least once.

## Coverage map (STANDARD.md section 4, bar "Scope and sequence states")

HECAT 2021 healthy behavior outcomes for the 3 to 5 column, by unit; "(s)" marks a sensitive unit.

| Topic | Outcomes (3 to 5 column) | Units |
|---|---|---|
| Personal health and wellness | All (1 to 12) | 1 (1, 2, 3, 4, 7), 2 (6), 3 (5), 5 (1, 2, 7), 8 (1, 2), 9 (5, 8, 9), 11 (6), 12 (5), 15 (2), 16 (6, 10, 11, 12) |
| Food and nutrition | 1 to 8, 10, 12 | 2 (1 to 8), 9 (8, 10), 11 (8), 16 (8), 19 (12) |
| Mental and emotional health | 1 to 5, 7 to 9 | 4 (1, 7, 8), 10 (4, 5), 11 (7), 12 (8), 15 (2, 9), 17 (2, 5, 9), 18 (3, 7, 8) |
| Physical activity (with PE) | 1 to 7 | 1 (1, 2, 3, 4, 7), 8 (2, 3, 5, 6), 12 (7), 15 (1, 2, 3, 5) |
| Safety | 1, 3 to 8 | 3 (1, 3, 4, 5, 6, 7), 9 (5), 10 (7), 17 (4, 5, 6), 19 (8) |
| Violence prevention | 1, 2, 3, 5, 7; 8, 9 (s) | 4 (1, 3), 12 (3, 7), 17 (5), 18 (1, 2), 19 (7); 6, 13, 20 (s) (8, 9) |
| Tobacco | 1 to 4 | 2 (1 to 4), 12 (1, 4), 19 (3, 4) |
| Alcohol and other drugs | 1 to 3 | 3 (1, 2, 3), 17 (1, 2, 3) |
| Sexual health (s) | 1, 2, 3, 4, 6 | 7 (s) (2, 3), 14 (s) (1), 21 (s) (1, 4, 6) |

Every topic returns in at least two years of the band, none is a one-off. NHES standards by unit, owned indicators
(practice in the frame's rows aside):

| Standard | Grade 3 | Grade 4 | Grade 5 |
|---|---|---|---|
| 1 Core concepts | 1 (S1.5.2), 5 (S1.5.1) | 9 (S1.5.3, S1.5.4) | 16 (S1.5.5, S1.5.6, S1.5.7) |
| 2 Influences | 2 (S2.5.1) | 11 (S2.5.2, S2.5.3) | 17 (S2.5.4) |
| 3 Information and help | 3 (S3.5.1, S3.5.2) | 11 (S3.5.3) | 16 (S3.5.4) |
| 4 Communication | 4 (S4.5.1, S4.5.2) | 10 (S4.5.3), 12 (S4.5.4, S4.5.5) | 18 (S4.5.6, S4.5.7) |
| 5 Decisions | 3 (S5.5.1) | 9 (S5.5.2, S5.5.3) | 17 (S5.5.4, S5.5.5) |
| 6 Goals | 5 (S6.5.1, S6.5.2) | 8 (S6.5.3, S6.5.4) | 15 (S6.5.5, S6.5.6) |
| 7 Practicing behaviors | 1 (S7.5.1) | 8 (practice toward S7.5.2) | 15 (S7.5.2) |
| 8 Advocacy | 1 (practice toward S8.5.1) | 12 (S8.5.1, S8.5.2) | 19 (S8.5.3, S8.5.4) |

Every year touches all eight standards in non-sensitive units. Skill standards practiced in two or more topics with
the sensitive units out: 2 (personal health, food, tobacco, mental health), 3 (safety, personal health, alcohol and
drugs, food), 4 (mental health, violence prevention, tobacco, safety, alcohol and drugs), 5 (safety, food, mental
health), 6 (personal health, physical activity: days 33 and 62), 7 (personal health, physical activity, mental
health), 8 (physical activity, violence prevention, personal health, tobacco, safety, food). Getting help is taught
in non-sensitive units every year (units 3, 10, 16 and 17).

## Leans on the calendar

Checked against data/plans/calendar.csv: SEL 3 to 5 units 1, 4, 5, 6 (grade 3), 8, 10, 11, 12 (grade 4), 13, 14, 16,
17, 18 (grade 5) fall where the frame's SEL table says, so each named day carries "health first" or "side by side"
in its note and no bridge is needed beyond the one the frame names (where SEL did not run, day 51 teaches the refusal
card in full). PE units 1, 9 and 17 run the same weeks as health units 1, 8 and 15; PE unit 20 (grade 5 weeks 15 to
17) comes after unit 15, so health names water and leaves energy foods to PE. ELA grade 4 unit 3 opens in week 17,
the week of day 47, so days 47 and 48 carry the frame's "if later" bridge. SEL unit 4 (grade 3, weeks 17 to 21)
runs the talk turn card side by side with day 18's listening steps. Unit 17 runs weeks 10 to 13 (the frame's SEL table
now says so); SEL units 16 and 18 that lean on it come later still.

## Sources a day leans on that are not loaded

No base text and no source-map.csv. Each unit planner reads the HECAT 2021 module its unit uses, 3-5 span, before the
unit plan; the Candidate cells above were settled at one line each and that read may add time. Not yet opened (named
from memory, opened at the safety and unit reads): CDC "Clean Hands" pages (day 2), USDA food guide pages (day 6), the federal food and drug agency's label
pages (days 7, 48), CDC germ and vaccine pages (day 35), CDC school health conditions pages (day 36), the national
highway safety agency's bicycle pages and the federal Poison Help pages (days 11, 13), CDC HIV basics and a national
pediatrics association's puberty pages (days 57, 86), and the child-welfare and child traumatic stress pages for the
body safety units (days 25, 55, 84). Opened and holding: the CDC children's physical activity guideline page (dated
2025-12-04, day 3, with the vigorous days), the National Youth Tobacco Survey, middle school (2025: 2.6% current e-cigarette
use, FDA survey results page, opened 2026-11-26; 12.9% ever tried any tobacco product from 2024, the latest edition
that reports it, CDC youth tobacco data, page dated 2024-10-17; days 8 and 51) and CDC
"About bullying" (the uniform definition, page dated 2024-10-28; day 19). Browser check (the reader's fetch got 403):
the federal stopbullying page on what bullying is (day 19) and the national survey of 8th graders (Monitoring the
Future) results for day 70's alcohol and drug norm, which the unit planner confirms with its figure and year. Day 41
names the help line by purpose: the national crisis line, call or text 988.

## Shorter path

- **A year about 10 days short** (10 school days, two weekly lessons a year). Fold-in days, each holding no
  assessment and cutting no owned part:
  - Grade 3: day 3 folds into day 2 (the guideline as a sixth habit card, the invite line in the pair rehearsal),
    saving 25 minutes; day 7 folds into day 6 (the sugar line on one label beside the food groups; the drink ad joins
    day 8's vape ad), saving 25 minutes.
  - Grade 4: day 33 folds into day 32 (the activity week as the plan's example, with the warm-up reasons in one
    line), saving 25 minutes; day 41 folds into days 40 and 42 (a five-minute ask rehearsal on day 40 and a
    five-minute listening-reply rehearsal on day 42, so S4.5.3's giving half keeps its day), saving 20 minutes.
  - Grade 5: day 70 stays whole (it is the only day of g5-aod-refuse-alcohol-drugs, and day 74 assesses its
    refusal). Respond day 76 folds instead: its "not yet" re-rehearsals, grouped by step from the record sheet, go
    into day 77's exit (five minutes) and day 78's opener (day 78's retrieval repeats day 77's, so it gives way),
    saving 20 minutes; day 90 folds into the last ten minutes of day 89 (the band look-back card), saving 20 minutes.
  - Total: six fold-in days, about 135 minutes, so the band holds on 84 of the frame's 90 days with every unit and
    check kept; respond days 76 and 90 are the two folded, and respond days are not assessed and own nothing.
- **A shorter period** (20 to 25 minutes). The opener drops to three minutes and the pair rehearsal to five. A
  course-level check gives its facts-in-use and valuing items in the first ten minutes of the respond day before the
  re-rehearsal, and its scenes on the check day. An end-of-unit check gives those items at the start of the check day
  and shortens its scenario set by one card, so the day before (often a hearing-station day: 20, 42, 52, 77) is not
  squeezed and no check lands on another check's day. Nothing is cut either way.
- **Twice a week for half a year** (the frame's other path). Same order and checks; the school puts the mid-year and
  year-end checks on its own weeks off its core check weeks. Unit 15's log still runs four school weeks: its days 62
  to 64 take the first lesson of weeks 2 to 4 and unit 16 opens in the second lesson of week 2 (unit 16 assumes no
  unit 15 row).
- **A left-out sensitive unit.** Its days extend the unit its row names (6 to unit 4, 13 to unit 12, 14 to unit 11,
  20 to unit 18, 21 to unit 19), or a short year takes them as its slack (up to four days a year); no
  check changes. The freed days stay in their weeks as practice days on that unit's cards, with no new items, so no
  check moves. Every sensitive unit's family note goes home on a non-removable unit's day (day 23 for unit 6,
  day 53 for units 13 and 14, day 82 for units 20 and 21), so a left-out unit never takes the next unit's note with
  it. Leave-out bridge: no non-sensitive unit uses a card a sensitive unit makes (the help-steps and
  boundary steps are made in units 3, 4, 10 and 12). A later sensitive unit after a left-out one opens with that
  card's or idea's one-step form in its first ten minutes and claims nothing from it: unit 13 and unit 20 with
  "never a child's fault, telling works"; unit 21 with the plain body-change terms if unit 14 was left out. These
  one-step forms are also the first-day retrieval of units 6, 13, 20 and 21 (days 25, 55, 84, 86) and of unit 7
  (day 27, one respect scene from grade 2), so they run whether or not the earlier unit ran; unit 14 opens with
  unit 7's respect scene as plain retrieval (day 57).

## For the lead

1. **Grade 5 week 10 holds two lessons and week 15 none.** The pin puts the grade 5 mid-year check in week 14 after 14
   unit days, so one week must double. I doubled the first two unit 17 days (week 10) rather than week 14, so the
   unit 17 end-of-unit check (week 13) and the mid-year check (week 14) are a week apart. The frame's SEL
   Cross-subject rows now say unit 17 runs weeks 10 to 13 (fixed in the 2026-11-26 fix pass).
2. **Few Application and Fluency days.** At one lesson a week nearly every row has one day of its own, so most
   teaching days first teach a row (Understanding) with a short rehearsal inside. The frame's "at most one whole
   Fluency day a unit" holds; only unit 10 uses one. Not a change, a reading for the unit planners: each day's pair
   rehearsal is where the bar's practice step lives.
3. **Course-level check form.** The frame does not name a form that differs from the end-of-unit checks given a week
   before; this scope sets one character's story in scenes for all six. The unit planners write the items.
4. **Codes not sampled on a course-level check** (S3.5.2, S1.5.4, S7.5.2, S6.5.5, S8.5.4) are named above with their
   reasons; the frame's check table already says each record is carried.

Gate: `python -X utf8 scripts/sequence.py check health-grades-3-to-5` passes; `frame.py check` 0 failures;
`frame.py calendar` no stagger-rule break.
