# Expert read: scope and sequence, Career Pathways, grades 9 to 12 (2026-11-26)

Course `career-pathways-grades-9-to-12`, placed in grade 10. A cold read by the curriculum expert (docs/agents/EXPERT.md)
of a scope written by a fresh Claude agent, done as docs/pipeline/briefs/sequence-read.md asks, with the after-core
checks of build/scope-writes/AFTERCORE-READ.md and a day-by-day check that the .md and days.csv agree (the writer
reported that the .md changed on disk after its last write; the .md is stamped 11:55, the CSV 11:54).

## What I read

- docs/courses/career-pathways-grades-9-to-12/scope-and-sequence.md (whole) and data/plans/career-pathways-grades-9-to-12/days.csv (all 96 rows: goal, codes, assess, school_day, note, retrieves), cold.
- The frame (docs/courses/career-pathways-grades-9-to-12/frame.md, whole), the grade 10 rows of data/progressions/cte.csv that the checks claim, the lens (docs/agents/lenses/career-education.md), docs/pipeline/briefs/sequence-write.md (files and readiness timing), build/scope-writes/AFTERCORE-BRIEF.md, docs/courses/CALENDAR.md (grade 10 table) and data/plans/calendar.csv for this course.
- Earlier reads: frame-career-pathways-grades-9-to-12-fixes-2026-11-25.md and sequence-career-exploration-grades-6-to-8-2026-11-26.md, so as not to repeat settled points and to tag repeats.
- Gates: `sequence.py check` 0 failures; `frame.py check` 0 failures (6 units, 96 days); `frame.py calendar` files the course in weeks 14 and 32, as CALENDAR.md's table does; `plan.py check` fails only on algebra-ii, not this course; `stale.py check` names nothing in this course.
- Sources opened 2026-11-26: https://www.bls.gov/cps/cpsaat37.htm (holds: median weekly earnings of full-time wage and salary workers by sex, race and Hispanic or Latino ethnicity, 2024 and 2025, and the note that 2025 figures are 11-month averages that exclude October); https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical (holds, with a nuance: see finding 10). cpsaat11 was opened today by the Exploration read and holds; the frame reads opened NIOSH, OSHA, NSTA and the Maryland sheet on 2026-11-25, and I did not reopen them.

## Verdict

The scope is sound in shape: every unit and both course-level checks sit on the frame's school days and weeks
(checks in weeks 14 to 15 and 32), the slot table puts every sub-cluster on a session, the readiness checks sit on
the right respond days with every assumed grade 8 row named, the year-before rows are retrieval, and the guards
(pay-gap unit, military route, sensitive sub-clusters, privacy, the paper path and practice 5's device rule) are on
the days they apply. The biggest risk is in the checks: both course-level checks, and several end days, claim codes
their items do not ask whole, so a unit plan writer would build items that stop short of the codes listed. The one
change that matters most is a prompt per part on days 42 and 95 (finding 1); no day is added.

Findings: 12 (1 serious, 7 moderate, 4 minor).

## Day-by-day agreement of the .md and days.csv

Checked and in agreement: every day's number, unit and kind; the unit and check day ranges, weeks and school days
(formula ceil(n x 160 / 96) holds on every row); the slot table against the codes of days 14 to 19, 23 to 28 and 32
to 37 (all 14 clusters, all six sessions); the learner rows on sessions 3, 4, 5 and the plan days; the check-in
rounds on days 32 and 33, 35 and 36, 37 and 38; the retrieval table against the `retrieves` column; the six readiness
checks (days 1, 12, 43, 54, 67, 80) and the rows each names; the units' day lists for units 1 to 5; the device turns
on days 55 to 57; the check 2 codes. Where they disagree is finding 4.

## Findings, most serious first

### 1. Both course-level checks claim codes their items do not ask whole (serious). LAYER sequence. REPEAT yes

**What is wrong.** Read against each row's note in cte.csv:

| Day | Code claimed | What the row asks | What the item asks |
|---|---|---|---|
| 42 | CD3.R4 | sort jobs three ways and judge which grouping helps the plan | place one job on the map by training level (CD3.A4, carried) |
| 42 | CD2.R2 | make a choice both ways, compare the two, say which suits and why | run both methods, defend the choice with one figure |
| 95 | CD5.A3 | percent change for two jobs and how the plan could adjust | the percent change only |
| 95 | CD4.R5 | weigh how the place choice fits career goals | "a regional pay item" |
| 95 | CD4.A2 | resume, cover letter, application and mock interview | one resume line read against a posting |
| 95 | ALL2.A6, ALL2.R6 | program of study and its fit; how it prepares for a changing economy, with a dated outlook figure | one plan line defended with a dated figure |
| 95 | CD2.R9 | judge how well one handles the plan's trade-offs | a trade-off named (K9 and A9 level) |
| 95 | CD3.R1 | check the plan against current data and update each out-of-date line | not asked beyond "a dated figure" |

**Why it matters.** AFTERCORE-READ: "each assessment item asks the whole of the id it claims". The unit plan writer
copies these notes into the item list, so the checks would report codes they never tested.

**Fix.** A prompt per part, in the day 42 and day 95 notes and in the .md's check sections:
- Day 42: after the job is placed, "which of the three groupings (cluster, training level, work setting) helps you
  most to see where this job fits a plan, and why" (CD3.R4); after both methods, "which method suited this choice
  better, and why" (CD2.R2).
- Day 95: the percent change item adds "the one plan line this would change, and how" (CD5.A3); the regional item is
  answered for an invented student's stated goal, "would this move fit the goal, and why" (CD4.R5, private ground
  kept); drop CD4.A2 from day 95's codes (the item asks one part; unit 5 scored the whole) and keep CD4.R2 with "judge
  your line against the posting's criteria, then revise"; the plan line is the program-of-study line, given a new
  dated outlook figure that makes it out of date: the student updates it (CD3.R1), says how the program prepares
  for that change (ALL2.R6) and how it fits the plan (ALL2.A6); the trade-off item adds "how well does your plan
  handle it, and what would you change" (CD2.R9).
Time: about six short prompts on day 95 at six to seven minutes each, which fits 45 minutes. Confidence: firm (rows'
notes and the item wording agree).

### 2. End days do not name what scores several claimed codes (moderate). LAYER sequence. REPEAT yes

**What is wrong.** Day 66 claims CD3.R2, CD2.R4, ALL2.A5, ALL2.R5, ALL2.R4, CD1.R1 and CD2.R1, but its note names
only "the revised full plan", the attachments and unseen items; the fact matrix (CD3.R2), the routes and search-width
sheet (CD2.R4), the route-steps line (ALL2.A5, R5) and the readiness checklist (ALL2.R4) are separate pieces. Day 78
claims CD4.A1, R1, A4, R4, A6, R6, ALL1.A7, R7, ALL2.A7, R7 but names only the resume, cover letter, application and
"the plan's changed lines". Days 91 to 93 claim CD4.K7 and CD2.R3 but the note's scored set names neither.

**Why it matters.** A busy writer builds the scored set from the note, so these codes would reach the unit plan with
no product behind them.

**Fix.** Name the product per code in each note: day 66, "the fact matrix (CD3.R2), the routes sheet with its widened
search (CD2.R4), the route-steps line (ALL2.A5, R5), the readiness checklist (ALL2.R4), the plan's reflection lines
(CD1.R1, CD2.R1)"; day 78, "the supervisor card week and the skills plan (CD4.A1, R1), the fallback carry-over line
(CD4.A4, R4), the school-widens line (ALL1.A7, R7), the outside-class portfolio entry (ALL2.A7, R7), the
self-employment line (CD4.A6, R6)"; days 91 to 93, "the portfolio's list of ways to present oneself (CD4.K7) and the
evidence line on the project brief (CD2.R3)". Confidence: firm.

### 3. Owned reflection codes are first done on the plan day and scored the next day (moderate). LAYER sequence (frame wording behind it). REPEAT new

**What is wrong.** ALL1.R3 (study log rated) first appears on day 10 and is scored on day 11; CD1.R1 and CD2.R1 first
appear on day 65 and are scored on day 66; ALL1.R6, ALL2.R3 and ALL1.R8 first appear on day 90 and are scored on days
91 to 93. The frame's rule is that a piece is drafted on an earlier day, gets written feedback after class, and is
revised on the plan day; "no score comes from a day a topic is first taught".

**Why it matters.** These six reflections would be scored without a feedback round, the one thing the plan days exist
for.

**Fix.** Draft each a day earlier, revise on the plan day: ALL1.R3 in the last five minutes of day 9 before the collect
(the log began on school day 9 and has run a week by school day 15); CD1.R1 and CD2.R1 on day 64 after the change log;
ALL2.R3 and ALL1.R8 on day 87 (as the .md already says) and ALL1.R6 on day 88. Add the codes to those days; day 10,
65 and 90 keep them as revisions. Confidence: firm.

### 4. The .md and days.csv disagree in five places (moderate). LAYER sequence. REPEAT new

**What is wrong.**
- Day 87: the .md gives ALL2.R3 and ALL1.R8; the CSV gives ~ALL2.K3, ~ALL2.A3 and ALL1.A8, with the reflections on day 90.
- Coin-test days: the .md's "Every day" lists 16, 17, 25 and 26; the CSV also carries the card-and-coin safety line on packet days 34 and 35, which a student whose own cluster is Advanced Manufacturing runs.
- Unit titles: the .md uses "Fourteen clusters, three up close", "Who works where, and why", "One job, one full plan", "Getting hired" and "A field problem, a portfolio, a panel"; the frame and calendar.csv use "Three clusters, broad to narrow", "Who does which job, and why", "One job, the full plan", "Getting work" and "The applied project". "Fourteen clusters" misdescribes the unit (a student meets three) and "Getting hired" drops the frame's "or a client".
- Reteach timing: the .md says the reteach "opens the unit's first or second day"; the CSV opens unit 2's day 13 with it, puts units 3, 5 and 6 in the second half of their day 1 after the hook, and units 1 and 4 on day 2.
- The .md's unit sections give no compelling question and no "why the days fall in this order" (sequence-write's file rules); its check sections do not say that check 1 draws unit 2 from the shared blocks and check 2 leaves unit 6 out, though the day 42 and 95 notes do; its "not sampled" list leaves out CD4.K7.

**Fix.** Make the CSV the base: day 87 per finding 3; add 34 and 35 to the coin-day list; use the frame's titles and
quote each unit's compelling question with one line on why its days fall in that order (from the frame's "Why this
unit, here"); state the reteach timing of finding 5 once; add the non-repeat line to both check sections and CD4.K7 to
the not-sampled list. Confidence: firm.

### 5. Day 13 opens unit 2 with the reteach and is overloaded, as are days 22 and 31 (moderate). LAYER sequence. REPEAT new

**What is wrong.** Day 13 holds a ten-minute reteach, a three-minute retrieval, a worked public budget line, the data
sheet, the sub-clusters placed on the map, two jobs compared on five figures, the wage against training and a real
worker's account, in 45 minutes, and never raises the unit's compelling question. Days 22 and 31 hold the same explore
work after ten minutes of response to the mid before.

**Why it matters.** sequence-write keeps a unit's first day clean for the hook and the compelling question; the explore
day is what the six field task sessions build on, and a squeezed one leaves its map and comparison unfinished.

**Fix.** Day 13 opens with the compelling question (two minutes); the reteach moves to the first ten minutes of day 14
for the flagged students while the class starts the field task (day 14 has no five-minute fix). On days 22 and 31 the
comparison drops to three figures (pay, training time and cost, outlook), the other two read on the job card later.
Confidence: likely (minute counts are mine).

### 6. The folded paths lose the interview feedback before the scored mock interview (moderate). LAYER sequence and frame. REPEAT new

**What is wrong.** Fold 7 of the 10-days-short year moves day 76 into day 75, and the 64-session and grade 12 paths
fold the same day. Day 76 is the day the teacher hears each student once with written feedback (about 40 minutes);
day 75 cannot also hold the model answer, paired practice and 30 hearings. The frame says no fold takes a feedback
day.

**Why it matters.** The mock interview on day 79 would then be the first time the teacher hears a student answer.

**Fix.** 10-days-short year: fold day 74 (self-employment) into day 70, as the frame's 64-session path already does,
and keep day 76. 64-session and grade 12 paths (set by the frame): for the lead; pick: the hearings run over the short
path's interview day's second half and the plan day's first half, about 20 minutes each. Confidence: firm.

### 7. The family note misses sensitive sub-clusters in Energy and in students' own packets (moderate). LAYER frame and sequence. REPEAT new

**What is wrong.** Day 12's note names the sensitive sub-clusters only "if Public Service and Safety or Healthcare and
Human Services is a shared cluster". Resource Extraction, one of the six, sits in Energy and Natural Resources, and a
student's own packet (chosen on day 9) may be any of the three, with sensitive steps on days 33 to 37 and no notice
named.

**Why it matters.** The leave-out choice is the family's (or an 18-year-old's), and it needs notice before the session.

**Fix.** Day 12's note: the unit 2 family note names the sensitive sub-clusters for any shared cluster that holds one
(Public Service and Safety, Healthcare and Human Services, Energy and Natural Resources) and, per student, for an own
cluster that holds one, with the leave-out swap. The frame's family-note bullet gets the same line ("For the lead").
Confidence: firm.

### 8. The 64-session path is overloaded in units 1 and 6 and does not say what it stops claiming (moderate). LAYER frame. REPEAT new

**What is wrong.** Unit 1's short session 1 holds the hook, the six models, the dated goals (CD1.A3) and the ten-minute
readiness check. Unit 6's kept day 88 holds the second try, the evidence check, the portfolio, learning alone and the
status notes. The path cuts the second shared cluster, so each student meets two clusters, but the .md does not say
that cluster's rows are named as not claimed, and check 1 still "samples two shared blocks".

**Why it matters.** The frame's "For the lead" item 4 asked this read to test the path; it fails in unit 6 and is
tight in unit 1.

**Fix.** Unit 1: the goals move to session 2 with values (both private plan pages). Unit 6: a scope call (For Cory).
The .md adds "on the 64-session path a student meets two clusters; the second shared cluster's rows are named as not
claimed, and check 1 samples the one block". Confidence: likely.

### 9. Presenting to a panel is scored with no practice day (minor). LAYER sequence. REPEAT new

**What is wrong.** CD4.A7 first appears on panel day 91; day 89 carries only CD4.K7 and a model defense.

**Fix.** Day 89's second half: each student runs the opening minute of their defense with a partner on the panel
card; add CD4.A7 to day 89's codes. Confidence: firm.

### 10. The disability rule on day 75 needs the guidance's nuance (minor). LAYER sequence. REPEAT new

**What is wrong.** The note says "an employer may not ask about a disability before a job offer". The federal equal
employment agency's guidance (opened 2026-11-26) says no disability-related questions or medical exams before a
conditional job offer, and that an employer may ask whether the applicant can do the job's functions, with or
without reasonable accommodation.

**Fix.** Day 75's note: "before a conditional job offer an employer may not ask disability-related questions; it may
ask whether you can do the job's tasks, with or without a reasonable change", with the page and date read.
Confidence: firm (page opened).

### 11. The carried CD1.R3 part is named, not done, on the block plan days (minor). LAYER sequence. REPEAT yes

**What is wrong.** Days 20 and 29 say "goals reread"; the row asks the student to change one goal that shifted, with
the reason on the change log.

**Fix.** Days 20 and 29 goal: "goals reread, one that shifted changed with its reason on the change log".
Confidence: firm.

### 12. The 10-days-short fold 10 drops unit 4's reteach (minor). LAYER sequence. REPEAT new

**What is wrong.** Folding day 56 into day 57 leaves no place for the reteach day 56 held, and day 58 then holds the
routes, the route steps (fold 4) and five device turns.

**Fix.** The fold table says the reteach moves to day 57's first ten minutes; day 58's device turns run while the
class works the route-steps line on paper. Confidence: likely.

## What is right and should not be touched

The slot table and its codes; the readiness rows named in the note, never in `skills`; the year-before rows moved to
retrieval (the writer's "For the lead" item 1 is right by rule 2); the sensitive-session lines on every block and
packet day; the pay-gap flag on every unit 3 day; the device-turn arithmetic; the mock interview and panel minute
counts; the grade 12 early-leave path.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Prompts added to days 42 and 95, CD4.A2 dropped from day 95 | each item asks the whole of the code it claims | days.csv, .md |
| Scored products named per code on days 66, 78, 91 to 93 | the writer builds the scored set from the note | days.csv |
| Reflections drafted on days 9, 64, 87 and 88, revised on the plan days | feedback before every score | days.csv, .md |
| Unit 2's reteach moves to day 14; day 13 opens with the compelling question | first day kept clean | days.csv, .md |
| Explore days 22 and 31 compare three figures, not five | time after the mid's response | days.csv |
| 10-days-short fold 7 becomes day 74 into day 70 | keeps the interview feedback day | .md |
| Unit 1 short path: goals move to session 2 | session 1 overloaded | .md |
| Day 89 adds a paired run-through and CD4.A7 | practice before the panel | days.csv, .md |
| Day 75 disability wording | the guidance's own terms | days.csv, .md |
| Frame titles and compelling questions in the .md | match the frame and calendar.csv | .md |

## For Cory

- The 64-session path's applied project (frame "For the lead" item 4, tested here): in 9 sessions it cannot hold a
  tested option, a second try, the evidence check and the portfolio as well as three panel days. Pick: a lighter
  project on that path (one option tested and its second try on paper, the effects map dropped to one line), with
  every scored code kept.

## For the source list

- https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical: the
  pre-offer rule and the job-functions question, for unit 5's teacher page.
