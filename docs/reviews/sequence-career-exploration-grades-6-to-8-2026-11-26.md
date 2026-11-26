# Expert read: scope and sequence, Career Exploration, grades 6 to 8 (2026-11-26)

Course `career-exploration-grades-6-to-8`, placed in grade 8. A cold read by the curriculum expert (docs/agents/EXPERT.md)
of a scope written by a fresh Claude agent, done as docs/pipeline/briefs/sequence-read.md asks, with the after-core
checks of build/scope-writes/AFTERCORE-READ.md.

## What I read

- docs/courses/career-exploration-grades-6-to-8/scope-and-sequence.md and data/plans/career-exploration-grades-6-to-8/days.csv (all 96 rows), cold.
- The frame (docs/courses/career-exploration-grades-6-to-8/frame.md, whole), the grade 8 rows of data/progressions/cte.csv (all 85, with notes), the lens (docs/agents/lenses/career-education.md), part 7 and the shared core of docs/ADOPTION-BAR-SUBJECTS.md, docs/courses/career-education/STANDARD.md sections 5 to 7 and APPROACH.md, docs/pipeline/briefs/sequence-write.md, build/scope-writes/AFTERCORE-BRIEF.md, data/plans/calendar.csv for grade 8.
- To test the lean timings: the days of social-and-emotional-learning-grades-6-to-8, library-and-research-skills-grades-6-to-8 (and data/progressions/library.csv `assumes`), computer-science-grade-8, civics-government-and-civic-life and english-language-arts-grade-8.
- The frame's three reviews (frame-career-exploration-grades-6-to-8-2026-11-25.md, -codex-, -fixes-), so as not to repeat settled points.
- Gates: `sequence.py check` 0 failures; `frame.py check` 0 failures; `frame.py calendar` shows cte grade 8 in weeks 16 and 32, with no grade 8 subject's mid-year check on school day 77 (PE 73 to 74, science 75, SEL 78, library 80, health 84); `stale.py check` 0 failures. `plan.py check` fails on algebra-ii (exit questions, an assessment day's minutes), not this course.
- Sources opened 2026-11-26: https://www.bls.gov/cps/cpsaat11.htm (holds: 2025 annual averages are 11-month averages that leave out October, and sex is given as the percent who are women only); https://www.cdc.gov/niosh/talkingsafety/ (holds: Youth@Work, Talking Safety, the free curriculum, with minors' rights and hazards); https://www.osha.gov/young-workers (holds for a safe workplace and how to complain, but gives no hours or task limits: see finding 4); https://www.dol.gov/agencies/whd/youthrules and https://www.dol.gov/agencies/whd/child-labor (the federal Wage and Hour Division's pages, which point to the hours and the jobs barred under 18). Not reopened: the North Dakota practices PDF, NSTA and the Maryland extension sheet (opened by the frame reads 2026-11-25).

## Verdict

The scope is sound in shape: every unit sits on the frame's days and weeks, each cluster has explore days and a real
field task, the plan and portfolio run all year with feedback before every score, and the sensitive ground (the
pay-gap unit, the military route, Resource Extraction, disability, family privacy) is handled with the frame's guards
on the right days. The biggest risk is in the end-of-unit assessments: nine learner-goal codes are claimed on end days
with no prompt or product that asks them, and several more are carried only in part on their teaching day, so a unit
plan writer would build checks that do not reach the codes they list. The one change that matters most is to give
every code an end day claims its named prompt or product (finding 1); no day is added.

Findings: 7 (1 serious, 4 moderate, 2 minor).

## Findings, most serious first

### 1. End-of-unit assessments claim codes they never ask (serious). LAYER sequence. REPEAT yes

**What is wrong.** Each end day lists every code of its unit, but its note names a scored product or a short prompt
for only some of them. Read as a busy writer would, these codes are claimed with nothing that asks them:

| End day | Claimed, not asked | What the note does name |
|---|---|---|
| 15 (unit 1) | CD1.K2 (label the parts of a model plan); CD2.K2 (order the decision steps); CD2.K3 (why facts beat a guess, from two cases); CD3.A2 (a job study with three kinds of information, source and year) | Prompts for CD3.K4, CD3.A4, CD2.K5, CD3.K1, CD3.K2, CD3.K3, CD3.A3, CD2.K1, CD2.A1. The .md says "CD3.K1 to CD3.A3", which would include CD3.A2, but the CSV note leaves it out |
| 44 (unit 3) | CD2.K4 (four options and a likely result for an invented student); CD2.K9 (what each of two choices gives up); CD4.A3 is judged on day 34 but not named in the scored set | Prompts for CD4.K3, CD4.K4, ALL2.K5, ALL1.K7; plan lines for CD2.A9, CD2.A4 |
| 57 (unit 4) | CD1.K5 (how an outlook figure and a new interest could each change a plan) | Prompts for CD5.K1, CD5.K2, CD4.K5, ALL2.K1; plan line CD1.A5 |
| 83 (unit 6) | CD1.K4 (steering habits named with the line that shows them); CD3.A5 (the uncommon job studied through a real account) | Prompts for CD2.K7, CD3.K6, CD2.K6, CD2.K8, CD3.K5. Day 82 also lists CD1.K4 and CD3.A5 in its skills, though its goal does neither |
| 93 (unit 7) | ALL1.K5 (why a plan helps in school); ALL2.K7 (learning outside class and the skill each builds); ALL2.K3 is "recorded" by the check-in line, which asks for the step done, one figure and the next step, not why taking charge of one's own learning matters at work | Prompts for CD1.K1, ALL2.K4, ALL2.K6, ALL1.K8 |

**Why it matters.** Sequence-write rule 2 ("each part of each code") and C1 and C8 of the bar: a code with no check
item fails C1. The unit plan writer copies the end day's note into the item list, so these codes would reach the
lesson layer with no item.

**Fix.** In each end day's note, and in the matching "Assessments" line of the .md, name one short prompt per code
above, or a product that stands for it, with the product named:
- Day 15: CD1.K2 stands on the scored plan page (each part labeled), and the note says so; CD2.K2 and CD2.K3 get one
  short prompt each (put four shuffled steps in order; say which of two invented students chose better and why);
  CD3.A2 is one of the three to five data items: three kinds of information read from a new 150-word profile, each
  with its source and year. Fix the .md range to list codes one by one.
- Day 44: one prompt for CD2.K4 (an invented student's next step, four options with a likely result each) and one for
  CD2.K9 (two job cards, what each gives up); the note says CD4.A3 is scored on the practice 1 and practice 3
  attachments (dependability on the role and slip note, problem solving on the failed fix and second try).
- Day 57: one prompt for CD1.K5 (an invented worker's new interest and a dated outlook figure: how each could change
  the plan).
- Day 83: one prompt for CD1.K4 (a short invented path: one steering habit and its line); CD3.A5 stands on the day 73
  study, which joins the plan day's revision set (day 82 note: "the open-job study revised as a plan line"); drop
  CD1.K4 from day 82's skills.
- Day 93: prompts for ALL1.K5 (one reason a school plan helps) and ALL2.K7 (two kinds of learning outside class and
  the skill each builds, no cost assumed); ALL2.K3 gets its own one-line prompt instead of the check-in record.
Rough time: unit 1's day 15 then holds about thirteen short prompts plus the data items; at two to three minutes a
prompt this fits 45 minutes only because the scored pieces are already in hand, so the unit plan should write them as
one-line prompts. Confidence: firm (rule text and the rows' notes agree).

### 2. Several codes are carried in part on their teaching day (moderate). LAYER sequence. REPEAT yes

**What is wrong.** The progression row's notes split each code into a knowing and a doing part; these goals carry
only one:

| Day | Code | Part missing from the goal |
|---|---|---|
| 2 | CD2.K5 | explain how the top two values would steer a job choice (privately) |
| 9 | CD3.A3 | the fourth source: the goal says four, the note lists three (an old article, a recruiting ad, a handbook page); the row adds a worker's post |
| 11 | CD2.A1 | recall one school choice that shows the student's way of deciding |
| 12 | CD2.K3 | explain from two invented cases why a choice made with facts beats a guess |
| 51 | ALL2.K1 | explain why workers keep learning (the goal only reads the changed tasks) |
| 54 | CD5.K1 | add one job that grows from a need to the plan as a possible direction |
| 87 or 91 | ALL2.K3 | explain why taking charge of one's own learning matters at work |
| 88 | ALL2.K7 | list learning outside class and name the skill each builds (the goal writes one resume line only) |
| 91 | ALL1.K5 | explain why a plan helps in school (the goal only drafts the school plan, A5) |

**Why it matters.** "Standards in full": a part not on a day is not taught, and finding 1's prompts would then test
what no day taught.

**Fix.** Add the missing clause to each goal, in a few words, no day added (for example day 12: "...first from two
invented cases, why a choice made with facts beats a guess; then use..."; day 9's note: "and an invented worker's
post"). Confidence: firm.

### 3. Lateral reading is counted as a readiness row when the counted rule makes it retrieval (moderate). LAYER sequence. REPEAT new

**What is wrong.** Day 1 gives a readiness item on `library:g6-lateral-reading` as "last used grade 6". But library
6 to 8 uses it in grade 7: day 20 (grade 7 school day 18) retrieves it and teaches `g7-lateral-hard-cases`, whose
progression `assumes` names g6-lateral-reading (one hop, sequence-write rule 2), and days 21, 22 and the grade 7 check
(day 28) carry g7-lateral-hard-cases. The frame said exactly this case turns the item into retrieval ("Readiness and
retrieval" bullet).

**Why it matters.** It breaks the counted rule, and day 1, already the course's fullest day, spends part of its ten
minutes on the wrong treatment.

**Fix.** Day 9 opens with a five-minute retrieval task on lateral reading (who stands behind one source, checked in
two others), `retrieves` = `g6-lateral-reading`; day 1's readiness keeps APPROACH's two items only (a percent of a
total, a dated pay figure). Day 9 still teaches its three steps for a student who never took library. Update the .md
table row ("last used grade 7 by one hop; retrieval on day 9"). Confidence: firm.

### 4. The source for a first job's hours and task limits does not hold them (moderate). LAYER sequence. REPEAT new

**What is wrong.** Day 90 teaches "the hours and task limits for workers under 16 and under 18" from
https://www.osha.gov/young-workers. Opened 2026-11-26, that page covers the right to a safe workplace and how to
complain, but not hours or task limits; those belong to the federal Wage and Hour Division (YouthRules,
https://www.dol.gov/agencies/whd/youthrules, and its child labor pages, https://www.dol.gov/agencies/whd/child-labor,
which point to the hours rules and the jobs barred under 18, and say a stricter state law applies).

**Why it matters.** C3(a): a fact with the wrong source; a writer building day 90 from the named page would not find
the limits and might write them from memory.

**Fix.** Day 90's note names both: the OSHA young workers page for a safe workplace and who to ask, and the Wage and
Hour Division's YouthRules and child labor pages for hours and tasks, each with the date read, plus "a stricter state
law applies where there is one". The .md "Sources" bullet adds it. Confidence: firm (pages opened).

### 5. The ten-days-short year folds the bridge day, and unit 5's day 60 is over its load (moderate). LAYER sequence. REPEAT yes

**What is wrong.** (a) The ten fold-ins are all second explore days, said to move "about ten minutes". Day 70 is not a
plain explore day: it holds the model five-minute lesson and the point, reason, example frame, the bridge for ELA's
`e8-present-reasoning`, which ELA teaches later (ELA days 148 to 154). Folded into day 69, the hook day, the bridge
loses most of its time the day before students teach. Day 61 (Financial Services' second explore day, a comparison
and a preview of the receipts) is a plain explore day and is not on the list. (b) Day 60 carries five knowing
indicators (ALL1.K2, K3 with the habit chosen, K4, K6 from invented cases, ALL2.K2 a private reflection) plus a
ten-minute readiness reteach for flagged students: about seven minutes a part. The writer flagged it; I read it as
overloaded.

**Why it matters.** Rule 10 (nothing assessed or owned cut) and rule 7 (days by load): the lesson task on day 71 is
the unit's field task and is scored after revision.

**Fix (settled, inside the unit).** (a) Replace day 70 with day 61 in the ten-days-short list ("61 into 59");
the total stays 10 sessions, 450 minutes, 86 days. (b) Move ALL1.K6 (attitude and habits from invented cases) from day
60 to day 61's opening, using two invented bookkeepers; day 60 keeps the habit's start so its two-week run is unchanged;
day 61's skills and codes gain g8-all1-6-attitude-habits and ALL1.K6. Confidence: likely.

### 6. The two-session path overloads unit 1 and unit 7's course-choice session (moderate, Cory's). LAYER frame. REPEAT new

**What is wrong.** The scope sets the frame's folds faithfully, and in doing so shows the overload the frame warned of
(frame "For the lead" item 8). Short session 2 holds three full days: the cluster map with three options from one
interest, the parts of a model plan with near and far goals, and the first plan. Short session 9 runs four-source
lateral reading while fifteen pairs take three-minute device turns (45 minutes of rotation) that the teacher must
supervise. Short session 1 holds the hook, the inventory, the values cards and the readiness check. In unit 7 the
course choices (ALL2.K4, ALL2.A4, "the course's most consequential real choice") fold into the second packet day,
which already holds thirty one-minute check-ins.

**Why it matters.** C14 and C2: a school on two sessions a week cannot teach these as written, and the first plan,
scored on day 15, is rushed.

**Fix.** Not an item choice: it is breadth or dose, so it goes to Cory (For Cory, item 1). Meanwhile the .md's
"Unsure" can name sessions 1, 2, 9 and unit 7's session 3 as the over-full ones. Confidence: likely.

### 7. Lean timings in the notes are wrong in places (minor). LAYER sequence. REPEAT yes

**What is wrong.** Against SEL 6 to 8's days (grade 8 year = SEL school days 321 to 480): SEL unit 15 runs grade 8
school days 63 to 80, not "55 to 75"; `g8-sm-plan-and-tidy` is on school days 70 to 75, after the production line
(days 32 to 34, school days 54 to 57), not "in the same weeks"; `g8-rds-careful-thinking` is taught school days 3 to
10, before day 11 (school day 19), not "in the same weeks". The .md's "For the lead" item 2 repeats the same claims.
No day changes: each day already teaches its own steps.

**Fix.** Day 32 note: "SEL g8-sm-plan-and-tidy comes later (SEL unit 15, school days 70 to 75), so the timeline is
taught on the sheet"; day 11 note: "is taught first (SEL unit 13, school days 3 to 10)"; day 60 note: "SEL unit 15,
school days 63 to 75"; mirror in the .md unit 3 leans line and "For the lead" item 2. Confidence: firm.

## What is right and should not be touched

- The units, days, weeks and school days match the frame exactly; check 1 on school day 77 is clear of every grade 8
  mid-year check; check 2 in finals week is allowed by stagger rule 3.
- Readiness timing: unit 1 on day 1 after the hook, unit 4 on check 1's respond day, the rest on the previous respond
  day; every other unit's day 1 is clean. Math 7 leans open as retrieval on the first day that uses them, in the
  `retrieves` column.
- The checks after units 3 and 7 draw from earlier units and say so; the 93 codes not on a check are named with a
  reason, as rule 3 allows.
- Practice evidence attachments follow the frame's fix unit by unit, each revised on the plan day before scoring.
- Sensitivity on the right days: health's steps on every unit 6 day and day 51; the military route's teacher line on
  day 41; no task asks a family's money, moves, health or status; the cpsaat11 caveats (11 months, women only) hold
  as of today; the menu, scissors and seed tray safety words copied from the frame.
- The packet days alternate with skill days, and day 87 names check 2's alternate card for a student whose packet
  took Health Data and Administration.

## What it could not judge

- Whether 45 minutes holds each field task: that needs the unit plans' minute budgets.
- The accuracy of any figure: no data sheet or job card is written yet; each is built and dated at the unit plan.
- Day 86's place on the real calendar (For Cory, item 2): school registration dates vary and none is in the repo.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Lateral reading becomes a retrieval task opening day 9 (`retrieves` g6-lateral-reading); day 1's readiness keeps the two APPROACH items | Library 6 to 8 uses the row in grade 7 by one hop (counted rule) | days.csv days 1 and 9; .md readiness table |
| Ten-days-short list: day 61 into 59 replaces day 70 into 69 | Day 70 holds the presenting bridge the field task needs | .md Shorter path |
| ALL1.K6 moves from day 60 to day 61's opening (two invented bookkeepers) | Day 60 is over its load; the habit's two-week run is unchanged | days.csv days 60, 61; .md unit 5 |
| Each cluster's unseen data item on an end day is a short version of its sub-cluster's field task decision on new data (for example a new small table: one relationship and one limit; a new sales table: a restock) | The unchosen sub-clusters are otherwise sampled by an item that does not ask the row | days.csv days 29, 44, 57, 67, 83 notes |
| Day 9's four sources: an invented old article, an invented recruiting ad, an invented worker's post and a dated handbook page | The row names four kinds; the note had three | days.csv day 9 |
| Day 90's source adds the Wage and Hour Division's YouthRules and child labor pages for hours and tasks | The OSHA page holds no hours or task limits | days.csv day 90; .md Sources |
| The prompts and product notes of finding 1 and the goal clauses of finding 2 | Item-level wording inside the codes | days.csv days 2, 9, 11, 12, 15, 44, 51, 54, 57, 82, 83, 87, 88, 91, 93; .md Assessments lines |

## For Cory

1. **The two-session path (frame item 8, now tested).** Short sessions 1, 2 and 9 of unit 1, and unit 7's course-choice
   session, are over-full (finding 6). Options: (a) the two-session path gives unit 1 two more sessions by studying
   one cluster fewer at depth there (that cluster's map and cards only, its field task left out that year), or (b) the
   two-session path is 66 sessions rather than 64. Pick: (b), since (a) leaves an owned sub-cluster unscored.
2. **When the course choices fall.** Day 86 (ALL2.K4, ALL2.A4, next year's course choices) is in week 29 of 32. Many
   schools register grade 8 students for high school courses in late winter or early spring (from memory, varies by
   district), so the course's most consequential real choice may come after the school's deadline. Moving those rows
   to an earlier unit moves a standard between units, which is yours. Options: (a) keep it in unit 7 and let a school
   teach day 86 out of order on its registration week (the plan-day revision stays in unit 7); (b) move ALL2.K4 and
   ALL2.A4 into unit 5 or 6. Pick: (a), with a line on the course page.

## Sources

- https://www.bls.gov/cps/cpsaat11.htm: checked the unit 6 data sheet's caveats (opened 2026-11-26).
- https://www.cdc.gov/niosh/talkingsafety/: checked day 33's hazard source (opened 2026-11-26).
- https://www.osha.gov/young-workers: checked day 90's source; holds safe-workplace rights only (opened 2026-11-26).
- https://www.dol.gov/agencies/whd/youthrules and https://www.dol.gov/agencies/whd/child-labor: the federal pages for
  minors' hours and barred jobs (opened 2026-11-26).
- From memory: grade 8 course registration timing (For Cory, item 2); the federal rule that an employer may not ask
  disability-related questions before a conditional job offer (day 88's teacher line reads correctly).

## For the source list

- The federal Wage and Hour Division's YouthRules page (https://www.dol.gov/agencies/whd/youthrules) and child labor
  page (https://www.dol.gov/agencies/whd/child-labor): public domain, open to automated reads 2026-11-26; the source
  for minors' hours and barred tasks that the OSHA young workers page does not hold. Career Pathways will need it too.
