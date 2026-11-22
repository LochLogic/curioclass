# Expert cold read: the career education progression (grades 8 and 10)

Brief: docs/pipeline/briefs/progression-read.md, {subject} = career education, gate `cte`. Read 2026-11-21 as the
curriculum expert and as the sensitivity reader. Edits no file but this one.

## What was read

- docs/agents/EXPERT.md; docs/agents/lenses/career-education.md; docs/ADOPTION-BAR-SUBJECTS.md ("The pass rule",
  "The shared core", part 7, "Before a scope and sequence in this subject").
- docs/courses/career-education/STANDARD.md and APPROACH.md (ownership, exclusions, sections 5 to 7).
- data/progressions/cte.csv in full: 273 rows (grade 8: 85 = 14 cluster, 14 first-look sub-cluster, 12 practice,
  45 learner-goal rows; grade 10: 188 = 14 cluster carries, 14 first-look sub-cluster carries, 58 owned sub-clusters,
  12 practice carries, 45 learner-goal carries, 45 owned learner-goal rows). data/progressions/cte-edges.md;
  data/progressions/cte-excluded.csv (5 rows).
- data/standards/cte-career-clusters-2024.txt (header and clusters), ncdg-2024-words.txt (CD3 and the rows named).
- Every cross_subject lean checked by script against the owning progression file (computer-science, ela, library,
  math, sel, social-studies csv): 146 lean instances on 66 distinct rows; all 66 exist and every one is owned or
  carried at or before the leaning grade.
- scripts/progression.py lines 55 to 100 (the `cte` entry). Not opened: any earlier career education review.
- Gate: `python -X utf8 scripts/progression.py check cte`: 273 rows, 0 failures. `plan.py check`: progression cte
  0 failures. `stale.py check` on STANDARD.md and cte-edges.md: 0 failures (the stale lines below are unmarked).

## Verdict

The progression is sound in its bones: ownership follows the settled rule exactly, every cluster, sub-cluster,
practice and owned indicator has a row, all 66 leans are real and in time, and the sensitive ground is handled with
more care than most published career courses (invented workers, private plans, no family questions, a chosen group
never named). The biggest risk is pace in grade 8: every cluster row says "the unit ends with a plan line", and 14
cluster units each with APPROACH's four closing days cost 56 sessions before any teaching, which the 64-session short
path cannot hold. The one change that matters most is to group the 14 clusters into about five units in the frame
and say so in the rows; second, fold the 45 grade 10 learner-goal carry rows into their owned partners so the real
handoffs sit in `assumes` (188 rows fall to 143).

## Findings, most serious first

### 1. Grade 8: one unit per cluster does not fit the year (serious; firm, arithmetic)

LAYER progression. REPEAT new. Rows: all 14 `g8-clu-*` rows.

Each cluster row ends "The unit ends with a plan line the cluster changed", and APPROACH.md ("The kinds of day")
gives every unit a field task day, plan day, assessment day and respond day. Built literally, that is 14 units x 4
closing days = 56 sessions, plus at least 2 explore days per cluster (28) = 84 sessions for the clusters alone,
against 96 sessions (full path) or 64 (short path, which must keep all four closing days per unit). The 57 practice
and learner-goal rows, the first plan, the job study and the interview practice then have 12 sessions or fewer, and
the short path is impossible. A writer will build 14 units from these rows.

Fix (row edits, all 14 `g8-clu-*`): replace "The unit ends with a plan line the cluster changed." with "The
cluster's study ends with a plan line the cluster changed; the frame groups the clusters into units (STANDARD.md
section 3)." Add to STANDARD.md section 3, after "Ownership": "**Units in Exploration.** The 14 clusters are grouped
into about five cluster units of two to four clusters each, so each unit's closing days (APPROACH.md) are spent once
per group, not once per cluster." The grouping itself is settled below.

### 2. Grade 10 owned learner-goal rows: handoffs in notes only, and a double row per goal (serious; firm)

LAYER progression. REPEAT yes (the health read's finding 4, links held in notes only). Rows: the 45 owned grade 10
learner-goal rows (`g10-cd1-r1-steps-that-worked` to `g10-all2-in-and-out-of-class`) and the 45 carry rows
(`g10-cd1-1-plan-keeps-going` to `g10-all2-7-learning-outside-class`); the 45 grade 8 learner-goal rows.

All 45 owned rows have empty `assumes`; each names its grade 8 row only as "Builds on ..." in notes. No grade 8 row's
`hands_on` names an owned grade 10 row (0 of 45); each names only the carry row. So the R-stage indicators (judge and
revise, the course's hardest learner goals) have no recorded prerequisite, and cte-edges.md's "every handoff between
them is written at both ends" is untrue for them. The pairs also do the same work on the same plan page (for example
`g10-cd1-1-plan-keeps-going` ~CD1.K1/A1 and `g10-cd1-r1-steps-that-worked` CD1.R1 both mark which plan steps moved the
student forward), so a section writer meets two rows for one piece of student work.

Fix: merge each carry row into its owned partner of the same goal number, keeping the owned row's id and notes and
adding the carry row's one-sentence task. The gate accepts mixed cells (library rows do this). The pairs:
CD1.1 to `g10-cd1-r1-steps-that-worked`; CD1.2 to `g10-cd1-r2-revise-plan`; CD1.3 (both `g10-cd1-3-goals` and
`g10-cd1-3r-revisit-goals`) to `g10-cd1-a3-goal-steps`; CD1.4 to `g10-cd1-steering-habits`; CD1.5 to
`g10-cd1-r5-plan-keeps-up`; CD2.1 to CD2.9 to `g10-cd2-r1-decide-review`, `g10-cd2-r2-compare-models`,
`g10-cd2-r3-enough-facts`, `g10-cd2-r4-search-wide`, `g10-cd2-values-in-choice`, `g10-cd2-experience-shapes`,
`g10-cd2-stereotype-check`, `g10-cd2-luck-and-control`, `g10-cd2-r9-trade-offs`; CD3.1 to CD3.6 to
`g10-cd3-r1-check-plan-info`, `g10-cd3-r2-combine-facts`, `g10-cd3-r3-rate-sources`, `g10-cd3-r4-grouping-that-helps`,
`g10-cd3-r5-open-to-jobs`, `g10-cd3-a6-uncommon-in-plan`; CD4.1 to CD4.6 to `g10-cd4-work-skills`,
`g10-cd4-resume-interview`, `g10-cd4-r3-general-skills-evidence`, `g10-cd4-carry-over`, `g10-cd4-moving`,
`g10-cd4-self-employment-decision`; CD5.1 to CD5.3 to `g10-cd5-a1-society-needs-plan`, `g10-cd5-a2-economy-plan`,
`g10-cd5-a3-hiring-trends-plan`; ALL1.1 to ALL1.8 to `g10-all1-school-results`, `g10-all1-r2-improve-review`,
`g10-all1-r3-study-habits-review`, `g10-all1-r4-strategies-review`, `g10-all1-r5-school-plan-review`,
`g10-all1-r6-habits-review`, `g10-all1-school-widens`, `g10-all1-information-use`; ALL2.1 to ALL2.7 to
`g10-all2-changing-work`, `g10-all2-learner-moments`, `g10-all2-r3-learn-on-own`, `g10-all2-r4-ready-after-high-school`,
`g10-all2-route-steps`, `g10-all2-full-plan`, `g10-all2-in-and-out-of-class`. Example cell:
`g10-cd1-r1-steps-that-worked` standard `CD1.R1; ~CD1.K1; ~CD1.A1`, assumes `g8-cd1-1-plan-keeps-going`. On each
grade 8 row set `hands_on` to the merged row (CD1.3: `g8-cd1-3-goals` and `g8-cd1-3r-revisit-goals` both to
`g10-cd1-a3-goal-steps`). Move the carry rows' cross_subject and model columns onto the merged row (for example
sel:g10-sm-set-goal is already on both CD1.3 rows; career-plan model_in and model_out). `g10-cd4-portfolio` (CD4.K7,
CD4.A7) has no grade 8 partner and keeps empty `assumes`, with `g8-prac-12-academic-skills` (which introduces the
portfolio) added as its assumes. Grade 10 falls from 188 to 143 rows; the counts in STANDARD.md section 3 do not
change. Then rewrite STANDARD.md section 3, "Handoffs", first sentence to: "Each Pathways `~` practice row assumes
Exploration's row for that practice, each Pathways sub-cluster row assumes its cluster's row in Exploration, and each
Pathways learner-goal row assumes the Exploration row of the same goal, with the matching `hands_on` at the other
end." If the merge is not made, the lesser fix is: set each owned row's `assumes` to the grade 8 row its notes name,
and add the owned row to that grade 8 row's `hands_on`.

### 3. Grade 10 class model: who chooses the clusters (serious for teachability; judgment call)

LAYER progression. REPEAT new. Rows: the 14 `g10-clu-*` rows, the 72 `g10-sub-*` rows.

Per student the load is fine: 2 or 3 cluster units (each a data sheet plus all its sub-clusters' field tasks, about
8 to 11 sessions), the resume and interview work, the full plan and the applied project come to about 60 to 75
sessions of 96, and about 55 to 60 at two clusters on the 64-session short path. The 188 rows are not 188 days: one
student meets about 70 of them. But the rows say "students choose two or three of the 14 clusters", so one room of 25
may hold students in ten clusters at once, running different field tasks with different data sheets on the same
day. Nothing in the rows or APPROACH says how one teacher runs that (stations, self-guided packets, shared skill
days). This is the real limit on teachability, more than the row count, and it is a scope and audience choice
(Cory's "a student chooses", 2026-11-21), so it is under "For Cory". Until then the rows are right as written.

### 4. CD3.A5 and CD3.R5 in grade 10 contradict the grade 8 privacy rule (moderate; firm)

LAYER progression. REPEAT new. Rows: `g10-cd3-5-open-jobs`, `g10-cd3-r5-open-to-jobs`.

`g8-cd3-5-open-jobs` is right: the student studies a job few people of a group they choose hold and never states
their own group in class. The grade 10 carry row then says "one job ... that few people like them hold", which tells
a writer to make the student place themselves in a group. `g10-cd3-r5-open-to-jobs` ("the usual pattern for their
group", "counting the job cards they made") is kept in a private reflection, which is acceptable, but does not say
the group may stay unnamed.

Fix: `g10-cd3-5-open-jobs` notes: replace "that few people like them hold" with "that few people of a group the
student chooses hold (it may be their own, kept private; the student never states their group in class)".
`g10-cd3-r5-open-to-jobs` notes: after "checked in a private reflection" add "; the group may stay unnamed, and the
teacher checks the reflection for a reason, never for which group". (If the merge in finding 2 is made, both
sentences go on `g10-cd3-r5-open-to-jobs`.) Optional, same spirit: ncdg-2024-words.txt CD3.A5 could read "Look
seriously at a job few people in a group you belong to or choose hold."

### 5. Credential and training routes written from memory: seven wrong or inconsistent (moderate; likely, from memory of the federal job outlook handbook's typical entry levels)

LAYER progression. REPEAT new. Most of the roughly 260 job examples are right or safely generic (the federal remote
pilot certificate, a commercial driver's license, an approved school and federal certificates for aircraft mechanics,
the 150-credit rule for certified public accountants, sea time and a federal license for a ship's captain, a state
license for cosmetology, a state test for nursing assistants, graduate study for counselors and physical
therapists). These are not:

| Row | Written | Problem | Fix (notes text) |
|---|---|---|---|
| `g8-clu-adv-manufacturing` | a machine operator (certificate) | The typical route is high school and on-the-job training; `g10-sub-adv-manufacturing-machinery` already says so | "a machine operator (on-the-job training)" |
| `g8-clu-digital-tech`, `g10-sub-digital-tech-web-cloud` | web developer (two-year or self-taught) / (certificate or self-taught) | The two rows disagree, and a four-year degree is now the most common entry | both: "a web developer (self-taught, two-year or four-year study; employers vary)" |
| `g10-sub-digital-tech-web-cloud` | a cloud support associate | Reads as one company's job title | "a cloud support technician (certificate or two-year study)" |
| `g10-sub-digital-tech-networks-cyber` | a security analyst (two-year or four-year study) | Four-year study is the usual entry | "a security analyst (four-year study, often with industry certifications)" |
| `g8-clu-education`, `g10-sub-education-teaching` vs `g10-sub-education-learner-support` | teacher aide (on-the-job route) vs paraprofessional (two-year study or a state test) | Same job, two routes; in schools paid by federal funds for low-income students the second is the rule | both teacher aide rows: "a teacher aide (high school, and in many schools two years of college or a state test)" |
| `g10-sub-public-service-public-safety` | a corrections or probation officer (four-year study and training) | Two jobs merged: corrections officers usually enter from high school and an academy; probation officers need four-year study | "a corrections officer (academy training) or a probation officer (four-year study and training)" |
| `g10-sub-construction-skilled-trades` | a licensed tradesperson (apprenticeship and a state license), beside "apprentice electrician or carpenter" | Implies carpenters are state-licensed; licensing is mainly for electricians and plumbers, and varies by state | "an apprentice electrician or carpenter (apprenticeship), a licensed electrician or plumber (apprenticeship and, in most states, a license) and a contractor (license rules vary by state)" |

Smaller, same rule: `g10-sub-construction-construction-planning` "a cost estimator (two-year study)" to "(four-year
study, or years in a trade)"; `g10-sub-healthcare-human-social-services` "a social and human service assistant
(two-year study)" to "(high school and on-the-job training, sometimes two-year study)";
`g10-sub-energy-resources-utilities` "a water or power plant operator (certificate and a state license)" to "a
water plant operator (certificate and a state license) or a power plant operator (long on-the-job training)". Add to
the shared data-sheet sentence in every `g10-sub-*` row, or once in STANDARD.md section 3, "Pathways' width": "Each
training route on a job card is checked against the federal job outlook handbook's typical entry level for that
school year." That makes the remaining memory-written routes a checked fact at build time.

### 6. The military row: commitment and transfer facts missing (moderate; firm on the facts, judgment on the wording)

LAYER progression. REPEAT new. Rows: `g10-sub-public-service-military`, `g8-all2-5-routes-after-school`,
`g10-all2-route-steps`.

The comparison (enlisting, a two-year program and an apprenticeship to one skilled job, for an invented worker) is the
right design and is balanced in tone. Two facts a fair comparison needs are missing, and without them it tilts
toward enlisting on "pay while training": (a) an enlistment is a binding contract of set years of service, the job
trained for depends on the contract and the service's needs, and service can include deployment; (b) a military
credential does not always carry to the civilian one (for an aircraft mechanic, military experience can qualify a
person to sit the federal exams, but the civilian certificate still needs them). The returns (pay, housing,
education benefits) are named as "costs and returns" in STANDARD but not in the task. Also the officer route reads
"four-year study or an academy", which wrongly sets an academy against four-year study.

Fix, `g10-sub-public-service-military` notes: after "the service or work commitment" insert "(for enlisting: a
contract of set years, a job that depends on the contract and the service's needs, and possible deployment; and the
returns, pay, housing and education benefits)"; after "the credential at the end" insert ", and whether it carries
to civilian work (an aircraft mechanic still sits the federal exams)"; replace "a military officer (four-year study or
an academy)" with "a military officer (a four-year degree, through an academy, college officer training or officer
school after college)"; add "Figures come from dated public federal pages, never recruiting material; no branch is
named as a pick." In `g8-all2-5-routes-after-school` after "one dated cost and time for each" add "(for the military,
the cost is the years of service committed)". Optional teacher-page line, item-level: "Families may ask the school
not to share their contact details with recruiters; the school's own policy and notice say how."

### 7. Disability at work: "workplace rights stated plainly" has no row (moderate; firm)

LAYER progression. REPEAT new. Rows: `g10-cd4-resume-interview`, `g8-cd2-7-stereotypes`, `g8-clu-healthcare-human`.

STANDARD.md section 6 asks for disabled workers shown doing the work "with workplace rights stated plainly". Only
`g8-clu-healthcare-human` says disabled workers are shown; no row states the rights, and the resume and mock
interview row lists lawful-question limits without the disability ones. A student with a disability will meet the
interview task first.

Fix: `g10-cd4-resume-interview` teacher note, append: "The teacher page states plainly that an employer may not ask
about a disability before a job offer, that a worker may ask for a reasonable change to how the job is done, and
that a student never has to disclose a disability in a course task." `g8-cd2-7-stereotypes` notes, after "groups
seldom seen in them" add ", including disabled workers doing the work". Move the healthcare row's "Disabled workers
are shown doing the work." into the shared job-card sentence of every `g8-clu-*` row ("noting one worker from a group
seldom shown in the field, disabled workers among them across the year").

### 8. Practice 9 is owned in part, with the rest named nowhere (minor; firm)

LAYER progression. REPEAT new. Rows: `g8-prac-9-resources`, `g10-prac-9-resources`.

The 2024 practice covers money and resources "both the organisation's and one's own" (file header). The rows teach
the employer's half and say personal finance is Economics, but name no row. The rest is not lost (grade 12 social
studies owns `econ-earning-income` and `econ-spending-consumer`), it is just untraceable. Fix: in both rows replace
"(personal finance is Economics)" with "(one's own money is taught in grade 12 Economics, social-studies
`econ-earning-income` and `econ-spending-consumer`; not a lean, since it comes later)".

### 9. Smaller row faults (minor; firm)

LAYER progression. REPEAT new.

- `g10-sub-energy-resources-utilities`: "a year of use by month" cannot show "the peak hour pattern". Fix: "From an
  invented town district's year of use by month and one day's use by hour, the student finds the peak month and the
  peak hours".
- `g10-prac-10-plan-path` and `g10-all2-full-plan` both call themselves "the full plan to a first credential". Fix:
  `g10-prac-10-plan-path` notes, after "builds the full plan" add "(its home row is g10-all2-full-plan; this row judges
  practice 10 on it)".
- The applied project's home is `g10-prac-12-academic-skills`, a `~` row; six other rows refer to it. That is
  acceptable, but `g10-cd2-r3-enough-facts` should name it: after "before the applied project's defense" add
  "(g10-prac-12-academic-skills)".
- Model order in grade 8: `g8-clu-*` rows take job-card and cluster-map as model_in, but `g8-cd3-2-job-study` and
  `g8-cd3-4-cluster-map` introduce them, and `g8-cd1-2-first-plan`, `g8-cd2-2-decision-steps` and
  `g8-prac-5-digital-data` introduce the plan, decision steps and data table. Fix: cte-edges.md, add under the first
  paragraph: "Inside grade 8 the frame's first unit holds the rows that introduce a model (g8-cd1-2-first-plan,
  g8-cd2-2-decision-steps, g8-cd3-2-job-study, g8-cd3-4-cluster-map, g8-prac-5-digital-data), before any cluster
  unit."

### 10. Stale lines in STANDARD.md, cte-edges.md, the bar and the gate (minor; firm, the repository)

LAYER process. REPEAT yes (the library read's finding 13, same owed row). The exact fixes:

- STANDARD.md, owed table, row "Progression gate support": replace the State cell with "Done 2026-11-21:
  scripts/progression.py splits ids on the tab, has `cte` in STD_FILES and ANCHOR and requires every learner-goal code
  through ELECTIVE_FILES; `progression.py check cte` passes (273 rows)" and the Where cell with "scripts/progression.py;
  data/progressions/cte.csv".
- STANDARD.md section 3, "Placement rule": replace "when the 2024 National Career Development Guidelines indicators
  are loaded, each indicator is owned" with "each 2024 National Career Development Guidelines indicator is owned".
- STANDARD.md section 3, "What the gate needs": replace the whole paragraph with "**The gate.** scripts/progression.py
  checks this subject: ids are split on the tab only, the cluster file is the anchor, and every code in
  ncdg-2024.txt must be owned by a row." (The paragraph states a done retool as owed.)
- STANDARD.md section 7, Library bullet: replace with "- **Library:** judging a source by lateral reading:
  `library:g6-lateral-reading` (the method) and `library:g8-news-lateral` (Exploration); `library:g9-lateral-method`,
  `library:g9-source-log`, `library:g10-lateral-machine-text`, `library:g10-synthesis-map` and
  `library:g10-database-deep` (Pathways)."
- STANDARD.md section 7, SEL bullet: replace with "- **SEL:** self-knowledge, goals, teamwork and decisions:
  `sel:g8-sa-what-interests-me`, `g8-sa-my-strengths`, `g8-sa-who-i-am`, `g8-sa-i-can-try`, `g8-sa-skills-grow`,
  `g8-sa-snap-judgments`, `g8-sm-set-goal`, `g8-sm-plan-and-tidy`, `g8-sm-stay-on-task`, `g8-rel-teamwork`,
  `g8-rds-careful-thinking` and `g8-rds-who-is-affected` (Exploration), and the grade 10 rows of the same names plus
  `g10-rel-different-ways` (Pathways)."
- STANDARD.md section 7, Math and Computer science bullets: add the Pathways rows the progression uses: math
  "`alg1-data-displays`, `alg1-percent-change-interest` and `alg1-correlation-causation` (Pathways), and the grade 7
  rows above as prerequisites"; computer science "`g9-optimize-procedures`, `g10-breach-causes` and
  `g10-career-skills` (Pathways)".
- STANDARD.md section 7, last line "Each lean is rechecked against the owner grade when the career education
  progression is written.": replace with "Every lean in data/progressions/cte.csv was checked 2026-11-21 against its
  owner grade (66 rows, each taught at or before the leaning grade; docs/reviews/progression-career-education-2026-11-21.md)."
- STANDARD.md section 6, "If a student tells you something" and "Reads": "the pay-gap unit" names no row. Add after
  its first use: "(the unit that holds g8-cd3-6-uncommon-jobs, with g8-cd2-7-stereotypes and g8-cd3-5-open-jobs;
  in Pathways g10-cd3-a6-uncommon-in-plan)".
- cte-edges.md first paragraph, "Every handoff between them is written at both ends": true only after finding 2's
  fix; until then add "except the owned grade 10 learner-goal rows, whose grade 8 row is named in notes".
- docs/ADOPTION-BAR-SUBJECTS.md part 7, "Standards": replace "go in data/standards/ncdg-2024.txt once their terms are
  read (data/plans/later.csv L91)" with "are in data/standards/ncdg-2024.txt (terms read 2026-11-21)". The "Before a
  scope and sequence" row for career education: replace "Owed: the guidelines' terms read and file (later.csv L91),
  the gate retool (L94), the second state rubric" with "Guidelines' terms read and ids filed, gate entry written, and
  the progression drafted and read cold 2026-11-21 (docs/reviews/progression-career-education-2026-11-21.md). Owed:
  the second state rubric".
- scripts/progression.py line 77: `OPTIONAL_FILES = {'ncdg-2024.txt'}` lets the gate skip the learner goals with a
  note if the file goes missing; the file now exists. Fix: `OPTIONAL_FILES = set()` (a gate change for whoever owns
  the script).
- On the next edit of STANDARD.md, the US spelling rule applies: "labour" (sections 1, 3, 4), "organisations"
  (section 4).

## The lens checklist, at the progression layer

| Lens line | Mark |
|---|---|
| Self, then world of work, then plan, then action; plan revised through the year | Met (plan rows on every cluster row, `g8-cd1-3r-revisit-goals`, the change log in grade 10) |
| Real jobs, real figures, dated; compared on more than pay; place shown | Met (every row's data sheet sentence; `g8-cd4-5-moving-for-work`; region in grade 10) |
| Doing the work of a field | Met (a field task on each of the 72 sub-clusters, each defended with a figure) |
| Employability taught directly and judged with criteria | Met (12 practice rows with look-fors on the piece) |
| Many paths, no ranking; stereotypes countered | Met, with finding 6 for the military facts and finding 5 for route accuracy |
| Honest about what a school adds | Met (labs, recruiter policy, counselor, state plan named as school additions) |
| All 14 clusters as equal one-day slots, no depth (Exploration) | Not missed: one sub-cluster per cluster at depth; finding 1 is about units, not depth |
| No applied task; no data source | Met |
| A practice claimed with no task | Met (each has a task) |
| Wage figure with no year; national as local | Met at this layer (every row says so) |
| Interest quiz that tells a student what to do; scored instrument | Met (`g8-prac-10-plan-path`) |
| Company or product named | Met, one near miss (finding 5, "cloud support associate") |
| Four-year default; one group only | Met |
| Private family income or status asked | Met (CD2.A6, family note, moves, health all routed to invented workers) |
| Resume or interview with no model, criteria or feedback | Met (`g8-cd4-2-job-search-steps`, `g10-cd4-resume-interview`) |
| Day-layer lines | Not applicable to a progression |

## What is right and should not be touched

- The ownership split (Exploration: clusters, 14 sub-clusters, practices, 66 indicators; Pathways: 58 sub-clusters, 64
  indicators, carries) matches STANDARD.md section 3 row for row, and the five adult-only exclusions are well reasoned:
  each needs years in a job a student cannot have, and each keeps its A-stage partner.
- The invented-worker escape on every personal prompt (CD2.A6, CD2.A7, CD2.A8, CD4.K5), private plan pages, and "scored
  on reasoning, never on the path chosen".
- CD3.A5's chosen-group design in grade 8 (finding 4 only brings grade 10 into line with it).
- The learning-style handling (ALL1.K4, A4, R4): strategies and conditions, no label. This is the evidence-backed line.
- The live-dispute notes on Environmental Protection, Resource Extraction, Water Systems, Regulation and Clean Energy:
  the jobs and the work, dated facts from more than one side, no verdict.
- All paper and simulation tasks with the safety step named; nothing needs a lab.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| (a) Grade 8 first looks avoid the six sensitive sub-clusters: keep | Within the pages: section 5 lets a school leave out a sensitive unit with a same-cluster swap; a first look on a sensitive sub-cluster would make the swap remove a grade 8 owned row and break Exploration. The cluster survey still names all six on the map and in job cards (a firefighter on `g8-clu-public-service`), so breadth is kept. No Cory call | data/progressions/cte.csv (no change) |
| The 14 first-look sub-clusters: keep all 14 | Each is the most visible, cheapest-to-run part of its cluster at grade 8, with a real paper task and a grade 7 math lean where one fits; Skilled Trades and Utilities put paid-training routes early. Data Science and AI is the least concrete pick but has the best leans (computer science grades 7 and 8) | data/progressions/cte.csv (no change) |
| (b) Data Science and AI: tools described, not used by students; keep | Within the pages: APPROACH.md "What a tool may and may not do" and bar C15 (no account, no network, nothing off the device) rule out live tool use in a task; library owns checking machine-made text from supplied output (library STANDARD section 7), which `g10-sub-digital-tech-data-science-ai` already uses. No Cory call | data/progressions/cte.csv (no change) |
| (c) `g8-cd3-6-uncommon-jobs` (CD3.K6) as the pay-gap section: keep, and name it | Within the pages: K6's "hurdles" are where dated pay-gap figures belong; the unit that holds it also holds CD2.K7 and CD3.A5. STANDARD's "pay-gap unit" should name the rows (finding 10). No Cory call | STANDARD.md section 6 |
| Grade 8 cluster units: five groups | (finding 1) Cross-cutting: Digital Technology, Management and Entrepreneurship, Marketing and Sales; making and building: Advanced Manufacturing, Construction, Supply Chain and Transportation; land and energy: Agriculture, Energy and Natural Resources; serving people: Education, Healthcare and Human Services, Hospitality, Events and Tourism, Public Service and Safety; money and creative work: Financial Services, Arts, Entertainment and Design. A frame may regroup with a reason | the Exploration frame; STANDARD.md section 3 |
| Merge carry and owned learner-goal rows in grade 10 | (finding 2) One row per goal per grade, mixed owned and `~` cells as library does | data/progressions/cte.csv |
| Generic route wording where entry varies ("employers vary", "license rules vary by state") | Accurate in every state and every year; the data sheet check settles the figure | data/progressions/cte.csv |

## For Cory

1. **Who chooses the Pathways clusters, the student or the class?** The rows say each student chooses two or three of
   the 14, so one room can run ten clusters' field tasks at once. Options: (A) each student chooses freely, with
   self-guided cluster packets and stations and whole-class skill days (widest choice, hardest to teach, needs every
   cluster's packet to stand alone); (B) the class chooses three clusters together each year, and each student picks
   sub-clusters inside them (easiest to teach, narrower for one student); (C) the class studies two clusters together
   and each student adds one of their own through a self-guided packet (two thirds whole-class, one free choice).
   Pick: C. It keeps "go broad" (all 14 built, any one open to any student) while letting a teacher run most days with
   one room on one task.
2. **(d) Should Environmental Protection join the leave-out-with-swap list in STANDARD.md section 5?** Section 6 groups
   it with Resource Extraction as "a live public dispute", but only Resource Extraction may be left out. Options: (A)
   add it, so the two sides of one dispute are treated alike (Water Systems and Regulation stay off: their tasks are
   procedural); (B) leave the list at six and rely on the no-verdict note and the sensitivity read; (C) take Resource
   Extraction off instead. Pick: A. The swap costs a school nothing (Energy has four other sub-clusters), and the same
   community that objects to one side of the dispute often objects to the other. This changes what a school may leave
   out, so it is yours.

Not for Cory: the writer questions (a), (b) and (c) are inside the pages' rules and settled above.

## What it could not judge

- Credential routes were checked from memory of the federal job outlook handbook, not against the current pages; the
  fix in finding 5 makes the check part of each data sheet's build.
- Whether the 64-session short path fits grade 10 at three clusters depends on the frame's unit lengths; it fits at two.

## Sources

- docs/courses/career-education/STANDARD.md, APPROACH.md; docs/ADOPTION-BAR-SUBJECTS.md part 7 and the shared core;
  docs/agents/lenses/career-education.md (the bar, rules and lens).
- data/standards/ncdg-2024-words.txt and cte-career-clusters-2024.txt (indicator stages, practice 9's scope).
- data/progressions/*.csv for the six subjects leaned on (lean existence and owner grades).
- From memory, marked: US Bureau of Labor Statistics Occupational Outlook Handbook typical entry levels (finding 5);
  federal rules on disability questions before a job offer and on aircraft mechanic certificates (findings 6 and 7);
  the federal Title I paraprofessional rule (finding 5).

## Confidence

Findings 1, 2, 4, 7, 8, 9, 10: firm (arithmetic or the repository). Finding 5: likely (memory, one source). Finding
6: firm on the facts, judgment call on the wording. Finding 3 and For Cory: judgment calls.

## Fix pass (2026-11-21)

Findings 1, 2 and 4 to 10 applied by a fix agent; findings 3 and the Environmental Protection question (For Cory 1
and 2) went to Cory on the Desk and were not applied. STANDARD.md section 5's leave-out list is unchanged; the one row
that names the dispute (`g8-clu-energy-resources`) already says "a school may swap a section (STANDARD.md section
5)", which holds under any answer. Gate after the pass: `progression.py check cte` 228 rows (grade 8: 85, grade 10:
143), 0 failures; `check sel` and `check library` 0 failures; `stale.py check` 0 failures on every file changed.

- **1.** All 14 `g8-clu-*` rows now end their study with "The cluster's study ends with a plan line the cluster
  changed; the frame groups the clusters into units (STANDARD.md section 3)", so no row claims its own unit.
  STANDARD.md section 3 gains "Units in Exploration" with the five groups settled above (a frame may regroup with a
  reason).
- **2.** The 45 grade 10 carry rows are folded into their owned partners as the pair list says (CD1.3's two carries
  both into `g10-cd1-a3-goal-steps`): the owned row keeps its id and notes, gains the carry's `~` codes, task
  sentence, models, words and leans (deduplicated by id), and its `assumes` is the grade 8 row; each grade 8 row's
  `hands_on` and handoff note now name the merged row. `g10-cd4-portfolio` assumes `g8-prac-12-academic-skills`,
  whose `hands_on` and note add it. Every id keeps one owner and every `~` code is kept (44 merged rows carry them).
  STANDARD.md section 3 "Handoffs" and the "Carried" bullet say so; cte-edges.md's "written at both ends" is now
  true, so it needed no exception.
- **4.** Both sentences went on the merged `g10-cd3-r5-open-to-jobs` (chosen group, may be their own and kept private;
  the group may stay unnamed, checked for a reason). The optional ncdg-2024-words.txt line was not in scope and is not
  changed.
- **5.** The seven routes and the three smaller ones fixed as the table says, with generic wording where entry varies:
  the corrections and probation officer split into two jobs, the security officer's license "where the state requires
  one", the skilled trades route "a license at the end where the trade and the state require one", the
  paraprofessional on `g10-sub-education-learner-support` given the same route as the teacher aide rows, and
  `g8-clu-energy-resources`'s water plant operator given the state license `g10-sub-energy-resources-utilities` names.
  The handbook check line is in STANDARD.md section 3, "Pathways' width".
- **6.** `g10-sub-public-service-military`: the binding contract of set years, the job depending on the contract and
  the service's needs, possible deployment and the returns; whether the credential carries to civilian work; the
  officer route reworded; the federal-pages and no-branch line. `g8-all2-5-routes-after-school` states the military's
  cost as the years of service committed. The optional recruiter-contact line was not added.
- **7.** The disability rights teacher note on `g10-cd4-resume-interview`; disabled workers on `g8-cd2-7-stereotypes`;
  the healthcare row's sentence moved into every `g8-clu-*` job-card sentence.
- **8.** Both practice 9 rows name social-studies econ-earning-income and econ-spending-consumer as a grade 12 forward
  pointer in notes, not as cross_subject.
- **9.** The utilities task, the practice 10 home-row note, the applied project id on `g10-cd2-r3-enough-facts`, and
  the model-order line in cte-edges.md, all as written.
- **10.** Every listed line fixed in STANDARD.md, cte-edges.md and the bar (part 7 standards line and the "Before a
  scope and sequence" row); scripts/progression.py `OPTIONAL_FILES = set()`. US spelling in STANDARD.md: labour,
  organisations, practised and practises, defence; in the bar's part 7 list, labour and practise. Two corrections to
  the read's own text: the lean count is 52 distinct rows (142 instances after the merge), not 66, and the SEL bullet
  lists the grade 10 rows by name, since two grade 8 names (`g8-sa-my-strengths`, `g8-sa-who-i-am`) have no grade 10
  lean; the library bullet also names `library:g8-research-product`, which a grade 8 row leans on.
