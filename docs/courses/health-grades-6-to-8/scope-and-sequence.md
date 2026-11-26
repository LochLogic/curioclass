# Scope and sequence: Health, grades 6 to 8

Course `health-grades-6-to-8` (catalog id `health-6-8`), one band course for grades 6, 7 and 8. Draft, 2026-11-26 (fix pass after the expert read the same day),
from the frame (docs/courses/health-grades-6-to-8/frame.md); the days are in data/plans/health-grades-6-to-8/days.csv.
Units, owned rows, day counts and check weeks are the frame's, unchanged.

## How the band runs

- **Three years, one after another.** Grade 6 is course days 1 to 48 (units 1 to 10), grade 7 days 49 to 96 (units
  11 to 21), grade 8 days 97 to 144 (units 22 to 30). Each year is 44 unit days, a mid-year check on its day 25 with a
  respond day on its day 26, and a year-end check on its day 47 with a respond day on its day 48.
- **Which standards fall in which year.** National Health Education Standards, 2024, 6-8 span: 46 indicators
  (`NHES.S<n>.8.<n>`), each owned by one row. Grade 6 claims the 13 owned by `g6-` rows, grade 7 the 17 owned by
  `g7-` rows, grade 8 the 16 owned by `g8-` rows; each is taught and assessed in its own year and placed on at least
  one day. A `~` code is practiced, never claimed (the eight sensitive rows own none). HECAT healthy behavior outcomes
  are named in each unit's first-day note (`HBO:`).
- **Meeting days and school_day.** Three 45-minute lessons every two weeks (an A week of two and a B week of one), 32
  weeks a year. `school_day` counts school days across the band, 1 to 480: course day n falls on band school day
  ceil(10n / 3), the even spread frame.py uses, so grade 6 is band school days 1 to 160, grade 7 161 to 320 and grade
  8 321 to 480. Take away 160 or 320 for the school day of that grade's own year; week = (school day - 1) // 5 + 1. A
  year's day 25 falls on school day 84 (week 17), its day 26 on 87 (week 18), its day 47 on 157 and its day 48 on 160
  (week 32, finals week), the weeks the frame and CALENDAR.md give.
- **The 45 minutes.** Opening scenario 5 minutes at most, the work, sheets collected and cards put away. A unit's
  first or second day opens with a 10-minute retrieval task (the `retrieves` column). Readiness checks take the last
  ten minutes of the day named.
- **What every unit does.** Two private self-checks (one on a practice day before the check, one on its check day), kept by
  the student. A home task goes out on its first day (English and Spanish), a talk with a trusted adult the student
  chooses; a school adult counts. Every last day is the end-of-unit assessment: two or three unseen scenarios read
  alone or aloud on request, the steps written for the character, one facts-in-use item per unit fact and one valuing
  item scored on whether the reason uses a unit fact; no cards; met, partly or not yet. Units 5, 15 and 25 end in the
  mid-year check (their last teaching day is practice with written feedback; their self-check 2 comes after the
  mid-year check, days 25, 73 and 121). Days 59 and 65 also hold a readiness check, so their end sitting is capped at two
  short scenarios (25 minutes), then self-check 2 (5 minutes) and the readiness check (10 minutes).
- **Scenarios only.** Every case is a character's. No student maps, rates or tells their own body, home, feelings or
  experiences in front of the class; goals come from the safe list (never weight, calories or shape).

## Shared cards (SEL STANDARD section 7, grades 6 to 8 form, word for word)

| Card | Words | First used here |
|---|---|---|
| Calm-down | "stop, breathe, name it, choose, go on" (grade 5 form "stop, breathe, name it, choose" retrieved in unit 3; SEL unit 3 grows it in weeks 11 to 15) | Day 10 |
| I-statement | "I feel ___ when ___ because ___. I need ___." | Day 12 |
| Refusal | three options, "a plain no, a no with a reason, a way out of the place", chosen to fit the place; health's card steps: stop and think, say no clearly, give a reason or none, offer something else or walk away | Day 19 |
| Goal steps | "goal, steps, block and plan, check" | Day 4 |
| Talk turn | "choose how to talk (in person, a call or a message)", then health's listening steps: listen, say back, ask a question | Day 13 |

Health's own cards, as the frame words them: help steps (know your helpers, pick the right one, say who, what
happened, that it matters, keep telling); source check (who made it, what they want, is there evidence, does an adult
I trust agree; grade 7 adds can I reach it); influence check (name it, say how it pushes, toward or away from a
healthy habit); decision steps (notice a careful choice, ask if it needs help, name options and results, pick the one
that supports health, look back); conflict steps (stop, calm down, each says their side, find a fair way, or walk
away and get help); boundary steps (say it, repeat it, leave, tell); speak-up plan (notice, who, say, ask).

## Readiness and retrieval (rule 2)

| Day | Kind | Row checked or retrieved | From |
|---|---|---|---|
| 1 | retrieval | g5-meh-mind-habits; g5-pa-habit-practice | grade 5 (the frame's 3 to 5 seam) |
| 59 (unit 12's last) | readiness for unit 13 | g5-fn-claims-that-hurt | grade 5, two grades back |
| 65 (unit 13's last) | readiness for unit 14 | g5-s-online-safety | grade 5, two grades back |
| 97 (unit 22's first, after the grade 7 year-end respond day) | readiness for unit 22's days 98 and 100 (`assess` readiness, last ten minutes after the hook) | g5-phw-surroundings-community; g6-phw-adult-or-professional | two or more grades back |

Every other unit retrieves from the grade before on its first or second day (the `retrieves` column): grade 6 from
grade 5 and 4, grade 7 from grade 6, grade 8 from grade 7.

## Grade 6 (course days 1 to 48, grade 6 ids)

### Unit 1. Strengths and habits

Days 1 to 5, weeks 1 to 4. Arc: a tired character's week, then the habit chain across the parts of wellness (days 1
and 2, NHES.S1.8.2), strengths for a person and a group (day 3, NHES.S1.8.1), both applied with the goal card held one
day (day 4), end check day 5 (a strength for the character's own wellness and one for the group). Why the order: the year opens on the plain cause-and-effect every later skill unit
reasons with, and strengths come after so a goal has something to build on. Assessment: day 5 end. Candidate cells:
hygiene and dental care kept as one chain line on day 2 (no added time).

### Unit 2. Getting the right help

Days 6 to 9, weeks 4 to 6. Arc: sort situations to the right helper and first sentence (day 6, NHES.S3.8.1), help
steps rehearsed in pairs (day 7, Fluency), barriers to reaching help and a way around each (day 8, NHES.S3.8.2), end
day 9. Why the order: SEL unit 1 taught the helper choice in weeks 1 to 5, and every sensitive unit after leans on
these help steps. Candidate cells: reaching emergency services kept as one scene on day 6.

### Unit 3. Stress, messages and listening

Days 10 to 15, weeks 7 to 10. Arc: stress signs and coping (day 10), messages by channel (day 11, NHES.S4.8.1),
I-statement rehearsal (day 12, Fluency), listening steps (day 13, NHES.S4.8.2, Understanding because it is the
indicator's first day), both without cards with the performance record (day 14), end day 15. Why the order: coping
first so a hard talk starts calm; saying comes before listening because the I-statement is the answer a listener
gives. Candidate cells: when stress needs help, kept inside day 10. Sensitive flag: mental health.

### Unit 4. Nicotine and pressure

Days 16 to 20, weeks 11 to 14. Arc: linked influences (day 16, NHES.S2.8.1), the nicotine norm (day 17: the share of middle school students who had
not used an e-cigarette in the past 30 days, about 96 in 100 in the 2024 national youth tobacco survey), when a
choice needs the careful steps (day 18, NHES.S5.8.2), refusal rehearsal on an offered vape (day 19, Fluency), end
day 20. Why the order: influence before decision, so the careful steps meet a real push. Candidate cells: secondhand
smoke and vapor kept as one line on day 17. Sensitive flag: substances.

### Unit 5. Preventing illness and injury

Days 21 to 24, weeks 14 to 16. Arc: prevention behaviors and their facts (day 21, NHES.S1.8.3), ranked (day 22),
alcohol and drug facts (day 23), practice with written feedback (day 24). Assessment: the mid-year check (day 25)
is the end-of-unit assessment. Candidate cells: misuse of medicine kept inside day 23. Sensitive flags: substances,
vaccines as a plain fact.

### Grade 6 mid-year check

Day 25 (school day 84, week 17), respond day 26 (week 18). See Course-level checks.

### Unit 6. Eating patterns and food choices

Days 27 to 31, weeks 18 to 21. Arc: an eating pattern that fits needs, culture and budget (day 27), a label read with
ratios and the influence check (day 28), decision steps on a menu (day 29, Fluency), quick versus step-by-step choice
(day 30, NHES.S5.8.1, Understanding because the effect on health is first taught here, with a teacher model), end
day 31. Why the order: after math grade 6 unit 2 (ratios, weeks 4 to 8), so ratio is used,
not taught; the decision steps from unit 4 return in a new topic. Candidate cells: breakfast and water instead of
sugary drinks kept as one line each on day 27. Sensitive flag: food. Supplies: color-printed invented labels.

### Unit 7. Bullying, harassment and speaking up

Days 32 to 36, weeks 22 to 24. Arc: bullying told apart from an ordinary disagreement (day 32), boundary and stop-line
rehearsal (day 33, Fluency), a response and a report (day 34), speaking up for others (day 35), end day 36. The unit
owns no indicator; it practices NHES.S4.8.1, S4.8.4 and S8.8.1. Why the order: here, before SEL unit 6 (weeks 27 to
31) builds on the row. Candidate cells: not spreading rumors or images, one line on day 34.

### Unit 8. My habits and goals

Days 37 to 41, weeks 25 to 28. Arc: supports and barriers from a log (day 37, NHES.S7.8.1), the private self-check
(day 38, NHES.S6.8.1), alone, with help or as a group (day 39, NHES.S6.8.2, Understanding because it is the
indicator's first day), a class activity goal (day 40), end day 41. Why the order: the log comes before math grade 6
unit 8, so health reads counts and a tally only; PE unit 7 (weeks 27 to 31) opens with these supports and barriers.
Candidate cells: screen time limits kept inside the self-check. Family notes for units 9 and 10 go home on days 38
and 41.

### Unit 9. Unwanted touch and getting help (sensitive, removable)

Days 42 to 43, weeks 28 to 29. Telling and helpers on scripted scenarios; end day 43. Family note day 38, leave-out
extends unit 7. Candidate cells: online sexual pressure and images, one scene kept to telling.

### Unit 10. Puberty and health (sensitive, removable)

Days 44 to 46, weeks 30 to 31. Body changes with correct terms and a question box (day 44), hygiene, respect and
relationship signs (day 45), end day 46. Family note day 41, leave-out extends unit 1 with a third chain case.
Candidate cells: where to get a reliable answer about bodies, kept in the question box.

### Grade 6 year-end check

Day 47 (school day 157, week 32), respond day 48 (school day 160).

## Grade 7 (course days 49 to 96, grade 7 ids)

### Unit 11. Support and conflict

Days 49 to 53, weeks 1 to 4. Seek and give support (day 49, NHES.S4.8.3), rehearsal (day 50, Fluency), conflict
prevented and ended (day 51, NHES.S4.8.6), both without cards with the performance record (day 52), end day 53. Why the
order: the year opens on getting help, and grade 6 unit 7's bullying-versus-conflict line is retrieved first so the
conflict steps are used for ordinary conflict only. Candidate cells: asking a counselor, kept inside day 49.

### Unit 12. Turning down risks

Days 54 to 59, weeks 4 to 8. Norm and ways to turn down a request (day 54, NHES.S4.8.5), refusal rehearsal (day 55),
rides, gear and places (day 56), ride rehearsal (day 57), the decision process alone, with help or in a group (day
58, NHES.S5.8.3, performance record), end day 59 plus unit 13's readiness check. Supplies: a helmet shown by the
teacher on a stand (borrowed from PE or a family, or $15 if bought). Candidate cells: pedestrian safety with phones,
one scene on day 56. Sensitive flag: substances, crashes.

### Unit 13. Health information you can trust

Days 60 to 65, weeks 8 to 12. Health literacy and outcomes (day 60, NHES.S1.8.5), credible sources (day 61,
NHES.S3.8.3, Understanding because product and service sources are new), traced on cards (day 62), judging claims
(day 63, NHES.S3.8.4, groups from the day 59 readiness), rated without cards (day 64), end day 65 plus unit 14's
readiness check. Why the order: before ELA grade 7 unit 6 (weeks 27 to 32), so health teaches its own source-check
questions. Candidate cells: one supplement or energy drink claim on day 63.

### Unit 14. Boundaries online and in person

Days 66 to 68, weeks 12 to 14. Boundaries and agreement (day 66, NHES.S4.8.4), rehearsal with the performance record
on an unfamiliar prompt (day 67), end day 68. Candidate cells: not sharing others' photos, kept on day 66.

### Unit 15. Living with health conditions and habits that reach others

Days 69 to 72, weeks 14 to 16. Routines with a condition (day 69, NHES.S1.8.4), a character's routine (day 70),
habits ranked by reach (day 71, NHES.S7.8.2, Understanding with a teacher model, the indicator's first day), practice with written feedback (day 72). Why the order: science grade 7
unit 3 (body systems, weeks 9 to 14) ends the week unit 15 opens. Assessment: the mid-year check (day 73). Candidate cells: the school's
asthma emergency plan, one line on day 70.

### Grade 7 mid-year check

Day 73 (school day 84 of grade 7, week 17), respond day 74 (week 18).

### Unit 16. What shapes eating and activity

Days 75 to 80, weeks 18 to 22. Five-level factors behind eating (day 75, NHES.S2.8.2), applied (day 76), the same
influences on different groups (day 77, NHES.S2.8.3), options on the five-level matrix (day 78, NHES.S5.8.4,
Understanding because it is the indicator's first day), applied (day 79), end day 80. Candidate cells: finding active
places nearby, one line on day 77. Sensitive flag: food.

### Unit 17. A goal with a plan

Days 81 to 84, weeks 22 to 24. A measurable goal and what a plan needs (day 81, NHES.S6.8.3 and S6.8.4), plan
rehearsal (day 82, Fluency), each student's own goal and plan, kept by the student (day 83), end day 84. Candidate
cells: a sleep goal fits the safe list.

### Unit 18. Speaking up for health

Days 85 to 88, weeks 25 to 27. A real chance at school and a first one-line ask (day 85, NHES.S8.8.1), alone or in a
group (day 86, NHES.S8.8.2), revision from written feedback (day 87), end day 88. Why the order: after ELA grade 7
unit 4 (argument, weeks 18 to 22), so claim and reason are used. Candidate cells: tobacco-free policies, inside day
86. Family notes for units 19, 20 and 21 go home on days 86, 87 and 90.

### Unit 19. Self-harm: helping a friend (sensitive, removable)

Days 89 to 90, week 28. Safe-messaging rules, the help card and the counselor on call. Leave-out extends unit 11.
Candidate cells: help lines and school supports on the help card.

### Unit 20. Dating and sexual harassment (sensitive, removable)

Days 91 to 92, weeks 29 to 30. Leave-out extends unit 14. The leave-out bridge applies when unit 9 was left out (the
help steps in the first ten minutes, claiming nothing of unit 9). Candidate cells: one sign of controlling behavior
online.

### Unit 21. Relationships and consent (sensitive, removable)

Days 93 to 94, weeks 30 to 31. Leave-out extends unit 11. Bridge when unit 10 was left out. Candidate cells: where to
get reliable answers, one line.

### Grade 7 year-end check

Day 95 (week 32), respond day 96.

## Grade 8 (course days 97 to 144, grade 8 ids)

### Unit 22. What shapes health, and the care that helps

Days 97 to 101, weeks 1 to 4. A hook case and the readiness check (day 97), factors at four levels (day 98,
NHES.S1.8.6), a second case (day 99), health care services (day 100, NHES.S1.8.7), end day 101. Candidate cells: dental
and vision checks kept inside day 100.

### Unit 23. Influences, false messages and tobacco

Days 102 to 108, weeks 4 to 8. Tools for influences (day 102, NHES.S2.8.4), a week's tool tried with a private log
(day 103), tobacco tactics (day 104), false messages (day 105, NHES.S3.8.5), source-check rehearsal (day 106),
fact-checks with the performance record (day 107), end day 108. Why the order: ELA grade 8 unit 2 runs beside it,
health a little ahead with its own steps. Candidate cells: how flavors target youth, inside day 104.

### Unit 24. Different views, concern and fair deals

Days 109 to 114, weeks 9 to 12. Different views (day 109, NHES.S4.8.9), rehearsal (day 110), concern for others (day
111, NHES.S4.8.10), negotiation (day 112, NHES.S4.8.8), a new scene with the performance record (day 113), end day
114. Candidate cells: respecting differences, inside day 109.

### Unit 25. Alcohol, drugs and rides

Days 115 to 120, weeks 13 to 16. The norm (day 115, NHES.S5.8.5), supports and obstacles mapped (day 116), refusal
rehearsal (day 117), the ride plan (day 118), the ride call (day 119), practice with written feedback (day 120).
Assessment: the mid-year check (day 121). Candidate cells: legal age and school rules, one line on day 116.

### Grade 8 mid-year check

Day 121 (week 17), respond day 122 (week 18).

### Unit 26. A team health project

Days 123 to 129, weeks 18 to 22. Teamwork and the team's habit and goal (day 123, NHES.S4.8.7 and S7.8.3), plan
rehearsal (day 124), three monitoring lessons with the teacher's doing record (days 125 to 127, NHES.S6.8.5), the
effect examined and the write-up revised (day 128, NHES.S6.8.6, the teacher models one effect write-up first), end
day 129 (adds an unseen team scene in a different setting and the teamwork record for NHES.S4.8.7). The habit runs in the weeks between
lessons. Supplies and space: $12 poster paper and markers; a walking group stays on school grounds under the school's
supervision rules, with water and a way for every student to take part. Candidate cells: a simple habit log (no day
cost).

### Unit 27. Advocacy that changes something

Days 130 to 135, weeks 23 to 26. Audience and setting (day 130, NHES.S8.8.3), the draft (day 131), revision and
practice (day 132, NHES.S8.8.4), delivery to a real school audience with the doing record (day 133), results and the
decision look-back (day 134, NHES.S8.8.5, S5.8.6, Understanding with a teacher model, both ideas first taught here),
end day 135 (one unseen case with a prompt for each code). Supplies: $4 flyer printing. Candidate cells:
encouraging others to be active fits the audience choice. Family notes for units 28, 29 and 30 go home on days 133,
134 and 137.

### Unit 28. Dating violence and assault (sensitive, removable)

Days 136 to 137, weeks 27 to 28. Leave-out extends unit 24; bridge when unit 20 was left out. Candidate cells: helping
a friend in an unhealthy relationship, one scene.

### Unit 29. Suicide: warning signs and help (sensitive, removable)

Days 138 to 139, weeks 28 to 29. Safe-messaging rules; leave-out extends unit 24. Candidate cells: school crisis
supports on the help card.

### Unit 30. Sexual health and prevention (sensitive, removable)

Days 140 to 142, weeks 30 to 31. Pregnancy and prevention (day 140), infections and services (day 141), end day 142.
Leave-out extends unit 27. Candidate cells: talking with a trusted adult, in the family note.

### Grade 8 year-end check

Day 143 (week 32), respond day 144.

## Course-level checks

Each is unseen written scenarios, each student working alone, scored met, partly or not yet on each step; units 1 to
4 items (and their year's equals) use new cases, never the unit checks' cases. Performance and doing records are
carried, never rescored. Each respond day re-rehearses each "not yet" step on a new scenario.

| Check | Day | Week | Samples | Codes |
|---|---|---|---|---|
| Grade 6 mid-year (unit 5's end) | 25 | 17 | units 2 to 5, one item from unit 1 | S1.8.2, S3.8.1, S3.8.2, S4.8.1, S2.8.1, S5.8.2, S1.8.3 |
| Grade 6 year-end | 47 | 32 | units 6 to 8, one item each from units 1 and 3 | S5.8.1, S4.8.1, S7.8.1, S6.8.2, S6.8.1, S4.8.2, S1.8.1 |
| Grade 7 mid-year (unit 15's end) | 73 | 17 | units 11 to 15 | S4.8.3, S4.8.6, S4.8.5, S5.8.3, S3.8.3, S3.8.4, S1.8.5, S4.8.4, S1.8.4, S7.8.2 |
| Grade 7 year-end | 95 | 32 | units 16 to 18, one item each from units 12 and 13 | S2.8.2, S2.8.3, S5.8.4, S6.8.3, S6.8.4, S8.8.2, S8.8.1, S4.8.5, S3.8.4 |
| Grade 8 mid-year (unit 25's end) | 121 | 17 | units 22 to 25 | S1.8.6, S1.8.7, S2.8.4, S3.8.5, S4.8.9, S4.8.10, S4.8.8, S5.8.5 |
| Grade 8 year-end | 143 | 32 | units 26 and 27, one item each from units 23 and 24 | S4.8.7, S6.8.5, S6.8.6, S8.8.3, S5.8.6, S8.8.5, S3.8.5, S4.8.8; S7.8.3 and S8.8.4 from the doing records |

All 46 owned indicators are sampled on at least one course-level check; none samples a sensitive unit. Stagger:
`frame.py calendar` shows no clash on school day 84 in any grade; the week 32 checks share finals week, which is
permitted.

## Sensitivity and leave-out

Sensitive flags on the day they apply: body (units 8, 10, 17, 26, 30), substances (4, 5, 12, 23, 25), safety and harm
(7, 9, 12, 14, 20, 25, 28), mental health (3, 11, 19, 29), food (6, 16). Each sensitive unit's first day carries the
leave-out note, its family note went home two weeks ahead (English and Spanish, with the outline and the opt-out
through the school), and the disclosure route (listen, no secrets, the school duty to report, the next adult named).
Rehearsal in sensitive units is from written scripts only; no student plays a person who pressures, touches, harms or
threatens. Each leave-in note also says a school that keeps the unit may add one practice day before its check. Day 118
(impaired driving) names its flags, safety and harm and substances. A school decides on a leave-out at the start of the year and adds that unit's days to the named earlier
unit when it runs, so the year's total and its check days stay put.

## Shorter path

No assessed or owned part is cut on any path.

- **A year about 10 school days short** loses about 3 lessons. Fold in, each saving 35 minutes (the day's 10-minute
  rehearsal moves to the neighbor day's opening): grade 6 days 7, 19 and 33; grade 7 days 50, 57 and 70; grade 8 days
  99, 110 and 117. Nine days, 315 minutes across the band, 135 of 144 days kept. Every folded day is a rehearsal or a
  second case whose code is taught on the day before and checked on the unit's last day. A folded day's self-check moves
  to the next day of its unit, and day 70's asthma plan line moves to day 69.
- **A shorter period** (40 minutes): the retrieval task drops to 7 minutes and the opening scenario to 3; cards are set
  out before the bell. A readiness check keeps its 10 minutes, and the end sitting on that day (days 59 and 65) keeps
  two scenarios.
- **A leave-out unit:** its days extend the unit its row names (9 to unit 7, 10 to unit 1, 19 and 21 to unit 11, 20
  to unit 14, 28 and 29 to unit 24, 30 to unit 27). The leave-out bridge: where a later unit uses a left-out unit's
  card or scene, its first ten minutes give the one-step form and claim nothing of the left-out unit (units 9, 20, 21,
  28, 29 and 30 name it).
- **The daily nine-week route** (45 sessions) can take its three reductions from the fold-ins of the year it runs, but
  the frame says the route needs its own session table, with the multiweek evidence of units 26 and 27 scheduled; that
  table is the lead's (For the lead 4).
- The frame names no once-a-week path.

## Coverage

HECAT 6 to 8 outcomes by unit (STANDARD.md section 4's 6 to 8 column, outcome numbers, checked against every unit's
HBO list in days.csv):
- Personal health and wellness, outcomes 1 to 12: units 1, 2, 4, 5, 8, 13, 15, 17, 22, 23, 26.
- Healthy eating, outcomes 1 to 9, 11 and 12: units 6, 13, 16, 27.
- Mental and emotional health, outcomes 1 to 9: units 3, 4, 11, 19, 23, 24, 26, 29.
- Physical activity, outcomes 1, 2, 5 and 7: units 8, 16, 27 (outcomes 3, 4 and 6 are taught by moving in PE).
- Safety, outcomes 1 to 8: units 2, 7, 12, 14, 18, 25, 27.
- Violence prevention, outcomes 1 to 3 and 5 to 7 in units 7, 11, 14, 24; outcomes 4 and 8 to 10 in the sensitive
  units 9, 19, 20, 28, 29.
- Tobacco, outcomes 1 to 5: units 4, 18, 23.
- Alcohol and other drugs, outcomes 1 to 4, 6 and 8: units 5, 12, 25.
- Sexual health, outcomes 1 to 10: sensitive units 10, 21, 30.

Each unit's first-day note
lists its outcomes.

NHES standards by unit owed: 1 (units 1, 5, 13, 15, 22), 2 (4, 16, 23), 3 (2, 13, 23), 4 (3, 11, 12, 14, 24, 26),
5 (4, 6, 12, 16, 25, 27), 6 (8, 17, 26), 7 (8, 15, 26), 8 (18, 27). Every year touches all eight standards in its
non-sensitive units.

## Sources not loaded

- The national youth tobacco survey (day 17): 2024, 3.5 percent of middle school students current e-cigarette users
  (CDC youth e-cigarette page, opened 2026-11-26); a later edition, if released, replaces it at the unit plan's expert
  read.
- The national survey of grade 8 students (days 54, 115): its federal summary page lists a 2025 survey released
  2025-12-17; the survey's own results site is browser check. Figures entered at the unit plan's expert read, never
  from memory.
- The national highway traffic safety agency pages (days 56 and 118): browser check, opened in Claude in Chrome at the
  safety read.
- CDC sleep page (day 2): dated 2024-05-15, both ranges given. CDC, HHS, USDA and national drug abuse institute pages
  (days 21, 23, 27, 44, 69, 140, 141): years entered at the expert read.

## For the lead

1. **Card wording.** Settled at the structure pass (2026-11-26): the frame's Models carried goal-plan and refusal
   rows now take SEL STANDARD section 7's grades 6 to 8 wording, with health's own refusal card steps kept beside
   SEL's three options, as this file already quoted them.
2. **Daily nine-week route.** The frame makes it unavailable until a session table exists; the fold-ins above are
   offered as its three reductions, but the units 26 and 27 multiweek evidence needs the lead's schedule.
3. **Gate note on day 117.** sequence.py notes a first Fluency day for `~NHES.S4.8.5`; the raw code differs from the
   owned NHES.S4.8.5, which units 12 and 25 practice from day 54. No change needed.

Settled at the fix pass (2026-11-26): the readiness check on day 97 is `assess` readiness (lead call 14); the grade 6
year-end samples units 1 and 3 and the source-check card's grade 7 step is a fifth check (frame corrected); the
sensitive units' end checks stay unseen written scenarios, at most two short ones, telling and refusal lines, read
aloud on request (expert read: the length, not the form, is the load).
