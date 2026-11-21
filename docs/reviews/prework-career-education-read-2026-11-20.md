# Career and technical education pre-work: cold read, 2026-11-20

Read as the curriculum expert (docs/agents/EXPERT.md) with the career education lens (docs/agents/lenses/career-education.md),
against stage 1 of docs/COURSE-RUN.md. I did not write these drafts. Nothing was edited but this file. Confidence is Firm,
Likely or Judgment call on each finding. Anything resting on my memory is marked "from memory". Outside sources are named by link.

## What I read

AGENTS.md; docs/COURSE-RUN.md (stage 1 only); docs/agents/EXPERT.md; docs/agents/lenses/career-education.md;
docs/courses/career-education/STANDARD.md and APPROACH.md; data/standards/cte-career-clusters-2024.txt;
docs/ADOPTION-BAR-SUBJECTS.md (part 7, and the career education and SEL rows of "Before a scope and sequence in this subject");
docs/reviews/career-education-open-material-2026-11-16.md; docs/courses/health/APPROACH.md and docs/courses/sel/APPROACH.md
(finished examples); docs/reviews/prework-sel-read-2026-11-19.md (format); docs/courses/UNIT-PLAN.md (field headings only);
docs/pipeline/briefs/sensitivity-read.md. For gate checks only: scripts/progression.py lines 40 to 270 (STD_FILES, ANCHOR,
code_grades, codes, check); scripts/standards.py lines 85 to 140. Rows for this subject only in data/courses.csv, data/subjects.csv,
data/modules.csv and docs/COURSES-STATUS.md. One-line id checks in data/progressions/ela.csv, math.csv and social-studies.csv.

Outside sources opened (by link):
- Advance CTE clusters page: https://careertech.org/what-we-do/career-clusters/ (14 clusters named, 72 sub-clusters stated; practices page not listed there)
- Advance CTE clusters grid PDF (text layer, all 72 sub-clusters by cluster): https://careertech.org/wp-content/uploads/2024/12/AdvanceCTE-CareerClusters-grid121124.pdf
- Advance CTE guidebook PDF (text layer, "Sub-Clusters (72)", each sub-cluster defined): https://careertech.org/wp-content/uploads/2025/06/Guidebook-National-Career-Clusters-Framework.pdf
- Pennsylvania Department of Education page (cluster groupings, cross-cutting marks): https://www.pa.gov/agencies/education/programs-and-services/instruction/career-and-technical-education/modernized-career-clusters-framework
- North Dakota CTE copy of the twelve practices (the file's own source, titles and order): https://cte.nd.gov/sites/www/files/documents/CareerReady/New12ALL.pdf
- NCDA 2024 National Career Development Guidelines framework PDF (opened and read in text): https://ncda.org/aws/NCDA/asset_manager/get_file/896607
- careertech.org/career-ready-practices and the Career_Ready_Practices_Framework_10_2024.pdf: both 404 again, so the practices are still checked only against a state's copy.

## Verdict

The standard is a sound, honest list: all 98 lines are real, unique, match the publisher's own lists and counts, and the text is in our own words. But it cannot be used by the next stage: the progression gate cannot read the file at all (every line collapses to one id), there is no ownership rule for clusters, sub-clusters or practices, and the learner-goals file the whole design rests on is still not loaded although the source is reachable. The approach page fills fewer than half of the plan fields, has no pacing and sends three fields to the wrong places, so the single change that matters most is a written ownership and depth rule (findings 1 and 2) and a full field block in APPROACH.md (finding 4).

## What I counted (so nobody has to again)

| Check | Result |
|---|---|
| Lines in cte-career-clusters-2024.txt | 98 id lines: 14 clusters, 72 sub-clusters, 12 practices; no duplicates; no tab column (ids only, no wording column) |
| Clusters | 14, all in the publisher's list. Cross-cutting (3): Digital Technology, Management and Entrepreneurship, Marketing and Sales (PA page marks the same three) |
| Sub-clusters by cluster | Digital Technology 6, Management and Entrepreneurship 5, Marketing and Sales 4, Advanced Manufacturing 5, Agriculture 6, Arts Entertainment and Design 6, Construction 4, Education 4, Energy and Natural Resources 6, Financial Services 5, Healthcare and Human Services 6, Hospitality Events and Tourism 4, Public Service and Safety 5, Supply Chain and Transportation 6: total 72 |
| Sub-cluster names vs the grid and guidebook | All 86 cluster and sub-cluster names occur in the guidebook text. The grid's wheel uses shorter labels in places ("Data Science & AI", "Local, State, & Federal Services"); the file follows the guidebook's long forms, which is right and is what the validator needs |
| Cluster spelling | File and guidebook: "Hospitality, Events & Tourism"; the web page and PA page: "Hospitality, Events, & Tourism". The file header already says so. Any other file must use the file's spelling |
| Practices | 12, in the order and titles of the North Dakota copy (1 contributing professional, 2 communicate, 3 critical thinking, 4 collaborate across cultures, 5 digital and data, 6 resilient, 7 time and space, 8 creative, 9 steward of finances and resources, 10 education and career path, 11 environmental and social impacts, 12 academic and technical skills). Matches the file's lines 9 to 20 in meaning and order |
| Counts stated in STANDARD.md, the file header, the lens and the bar | 14 / 72 / 12 everywhere they are stated; all agree |
| Gate read of the file | I replicated `codes()` from scripts/progression.py on this file: 98 lines in, one distinct id out ("CTE.Career") |
| NCDG 2024 (not yet in the repo) | 3 domains (Career Development, Academic and Lifelong Learning, Social Emotional Learning), 11 goals (5, 2, 4), and by my line count about 228 indicators in three stages each (K, A, R), 13 pages |
| Courses for the subject | data/courses.csv: 2 rows (cte-explore 6-8, cte-pathways 9-12), core n. docs/COURSES-STATUS.md: 3 courses (adds Personal Finance). data/courses.csv also has a personal-finance row (cte, 9-12) |
| Modules tagged to the two courses | 8 for Exploration (3 career, 5 economics or personal finance), 5 for Pathways, 6 for Personal Finance: matches COURSES-STATUS topic counts |

## Findings, most serious first

### 1. The progression gate cannot read this standards file, and it has no entry for the subject

- **Where:** scripts/progression.py `codes()` (line 150 to 156: `line.split('\t')[0].split()[0]`), `STD_FILES`, `ANCHOR`, `code_grades` (lines 51 to 70, 87 to 141); data/standards/cte-career-clusters-2024.txt (ids contain spaces, for example `CTE.Career Clusters.Digital Technology`).
- **What is wrong:** The gate takes the first whitespace-separated token of each line. Every line in this file starts `CTE.Career`, so all 98 ids become the one id `CTE.Career`. Anchor coverage, duplicate and "not in the standards files" checks would all fail or pass for the wrong reason. There is also no `cte` key in `STD_FILES` or `ANCHOR`, so `check('cte')` would test nothing. (The same split bites any id with a space, including four of the five CASEL competency names.) scripts/standards.py is fine: it matches whole lines.
- **Cost:** Stage 2 cannot start. A writer would either find the gate silent or have to guess why it reports one code.
- **Fix (a note for the progression retool, ours, untested):**

> Before the career education progression is written: (a) `codes()` in scripts/progression.py splits ids on the tab only and keeps the whole first field, as scripts/standards.py does; (b) add `'career-education'` (or the subject code the progression file will use, see finding 6) to `STD_FILES` with `cte-career-clusters-2024.txt` and the learner-goals file, and to `ANCHOR` with the learner-goals file; (c) add a `code_grades` case that returns None for `CTE.` ids (they carry no grade). Cluster ids are then placed by the ownership rule in finding 2.

  Confidence: Firm (I ran the same expression on the file).

### 2. No ownership rule: the page does not say which grade owns a cluster, a sub-cluster or a practice

- **Where:** STANDARD.md sections 2 and 3; COURSE-RUN stage 2 ("every standard placed once or excluded with a reason"); scripts/progression.py `check` (owners per code, `-excluded.csv` with a reason).
- **What is wrong:** The gate wants each standard owned by exactly one grade row or excluded with a reason. The page says only: Exploration "surveys all 14 clusters, with a sub-cluster in each studied" and "introduces" all 12 practices; Pathways has the student pick "two or three clusters" studied "at sub-cluster depth" and "practises" all 12. From that a writer cannot tell: (a) who owns the 14 clusters (Exploration, presumably); (b) which 14 sub-clusters Exploration studies, and who owns the other 58 (Pathways cannot, because which ones depend on student choice, so they are neither owned nor excluded); (c) whether a practice is owned by the course that introduces it or the one that practises it, and where the `~` goes; (d) which single grade a course owns in, because the page says "grade 7 or 8" and "grade 9 or 10" while the progression needs a grade per row.
- **Cost:** Two writers will do different things, or the gate fails on 58 unplaced sub-clusters. The 12 practices have no deadline grade either.
- **Fix (add to STANDARD.md section 3; ours, untested; the choices in brackets are in Questions 1 to 3):**

> **Ownership.** The progression has one row per owned item. Exploration owns the 14 clusters and 14 named sub-clusters, one per cluster (the list is fixed in the frame and kept in the progression). Pathways owns the sub-clusters of its fixed pathway menu (Question 2); every other sub-cluster is excluded with the reason "student choice; no fixed place in the course; met only through the general task template". The 12 practices are owned by Exploration (the course that first teaches each in a task), and Pathways carries each as a `~` row with the field task that practises it at higher demand. For the gate, a course's owner grade is its later grade (8 and 10, the deadline convention health and physical education use); the frame may place the course a year earlier with a reason.

  Confidence: Firm that a rule is missing; the particular rule is a Judgment call.

### 3. The learner goals are still not loaded, and the source is reachable now

- **Where:** STANDARD.md section 2 ("Still owed: the guidelines file and a read of its terms (its framework page refused the reader on 2026-11-16...)"); lens "Sources" ("the 2024 revision not read"); the scout's last table row ("Not read, blocked (403)").
- **What is wrong:** The 2024 framework PDF opens and extracts at https://ncda.org/aws/NCDA/asset_manager/get_file/896607. It states three domains, eleven goals and indicators coded `CD1.K1`, `CD1.A1`, `CD1.R1` and so on, in three stages that "are not tied to an individual's age or level of education". The goal text is exactly the kind of wording a progression owner column would carry. Until the file is in data/standards, the part of the design that Cory settled (the guidelines are the learner goals) has no standard behind it, and the cluster file is left to do a job it cannot do (the page itself says in section 2 that neither the clusters nor the practices say what a grade 7 student should be able to do about planning a career).
  Two things the page does not know yet: (i) the third domain is named **Social Emotional Learning** (4 goals, about 93 indicators, a third of the framework) and overlaps the SEL courses' sub-skills, so owning all of them in career education would teach SEL twice; (ii) I found no copyright or reuse statement in the PDF's text, so the licence is unread and the file's terms cannot be assumed.
- **Cost:** Stage 2 has nothing to own for "make a plan", "use accurate career information" or "balance life roles", which are the points of the course.
- **Fix:** Load the goals and indicators as ids with our own wording in data/standards (new file, the model is casel-5.txt), after reading the NCDA terms page by hand; add the file to `STD_FILES` and `ANCHOR`. Until then, STANDARD.md keeps its fallback (our own goals, marked "ours"). State the SEL domain rule once: career education owns the CD and ALL goals, and the SEL goals are carried as leans on the SEL courses (Question 1).
  Confidence: Firm (source opened); Likely for the overlap reading.

### 4. APPROACH.md fills fewer than half of the plan fields, and three field numbers point at the wrong field

Compared with docs/courses/health/APPROACH.md and docs/courses/sel/APPROACH.md and UNIT-PLAN.md fields 1 to 10 (unit) and 1 to 11 (section):

| Slot | Verdict | Note |
|---|---|---|
| Kinds of day | Filled | five kinds in career words; good |
| Daily evidence | Filled | job card with source and year, practised piece, decision plus one line of data, portfolio choice |
| Unit 1 header, pacing | Missing | no sessions by kind, no sessions a week, no minutes (finding 5) |
| Unit 2 standards, carried | Part | clusters, practices, data sources named; no rule for what is carried across the year (the plan and portfolio) or the day a model is withdrawn |
| Unit 3 where it sits | Missing | no builds-on, handoff, comes-back; no named link to a core course (finding 7) |
| Unit 4 readiness | Missing | what a student must already read or compute to start a data task |
| Unit 5 end-of-unit assessment | Part | named as a rubric piece plus short data items; no rule for samples at two levels, no plan or portfolio rubric, no rule for scoring a student's plan without scoring the student's choice |
| Unit 6 error register | Missing | the common errors (a figure read as local, "highest pay" as best, one path as default) have no home |
| Unit 7 response allocation | Missing | how a rubric piece is marked and by whom, groups for the respond day |
| Unit 8 tools and supplies | Missing | no statement of what a tool may do (health has one), nothing on any inventory tool, nothing on the paper path |
| Unit 9 family note | Missing | |
| Unit 10 sources | Missing | no sources table, no read status, no logic-model line (C16), no statement that no study stands behind the course |
| Section 1 | **Wrong** | the page uses "Section field 1" for the teacher page text on the field; UNIT-PLAN field 1 is "Standards and practices" (ids, the share of the standard, the verb) |
| Section 3, 5 | Filled | evidence and "what is carried" |
| Section 7 | **Wrong** | the page puts the speaker or visit here; field 7 is "Talk and writing" |
| Section 9 | **Wrong** | the page puts privacy notes here; field 9 is "Supports and extension" |
| Section 2, 4, 6, 8, 10, 11 | Missing | where it sits; expected errors; days (how a field task day opens, who holds the model); practice that returns; two rooms (a parent teaching one child at home, one projector); not in this section |
| Supports (C10, C11) | Missing | English learners, reading load of job data, access, extension, check accommodations |
| Sensitive ground | Part | one line (finding 8) |
| Evidence and sources (C13, C16) | Missing | health and SEL both end with this |
| What a tool may and may not do | Missing | health has it; SEL has it in unit field 8 |

- **Cost:** C6 to C11, C13, C15 and C16 each lose a slot. A writer filling a section plan from this page has nothing for expected errors, supports, or two rooms, and puts the speaker in "talk and writing".
- **Fix (replace "What career education adds to the plan fields" with a full block; ours, untested). Keep the lines that are right; add:**

> **Unit field 1:** sessions by kind, sessions a week and minutes as the frame states them (pacing, section "Pacing").
> **Unit field 3:** builds on (the earlier unit's plan line); leads to; comes back (the plan and portfolio, every unit); and the one link to this grade's core courses a teacher may use (an ELA writing or speaking row, a math percent or data row, an economics row), named by its row id.
> **Unit field 4:** one short item on reading a table or a percent, and one on reading a dated figure; a ten-minute reteach is a model of the same reading.
> **Unit field 5:** a demonstration, plan piece or portfolio piece scored on a rubric with two sample pieces at different levels, plus a few data-reading items. The plan is scored on its reasoning (a choice defended with a figure), never on which path the student chose or on the student's own circumstances.
> **Unit field 6:** the expected misreadings, each with its source or "from memory": a national figure read as local; highest pay read as best; one training route (a four-year degree) read as the default; a job read as for one group of people.
> **Unit field 7:** the rubric piece is judged by the teacher against two or three look-fors; no hands-up self-marking. Respond-day groups come from the rubric cells marked "not yet", at most four.
> **Unit field 8:** a tool may give a dated job profile, a practice reading of a pay table or outlook figure, a private plan template, and a mock-interview question bank with a model answer and a feedback list; it may not store a student's plan, interests or answers off the device, score a person, or tell a student what job to do. Every tool day has a paper path (C14, C15).
> **Unit field 9:** family note in English and Spanish: what the unit explores, what a student may take home (the job card, plan page), one question to ask a family member about their own work, and a line that sharing is the student's choice.
> **Unit field 10:** a sources table (read status, what is from memory), the data sources with their year, and a line that no study stands behind the course and that the logic model is on the course page (C16).
> **Section field 1:** the id of the cluster or practice, the share of it this section carries, the verb, and the data source with its year. A teacher page note on the field (what the work is, training routes, conditions) goes in the section's before-you-teach text, not in field 1.
> **Section field 7:** talk routine for a job comparison (claim, figure, source); one written task; the interview practice set-up (the teacher or a card plays the interviewer; a model answer first).
> **Section field 9:** English learners: six to eight workplace words in depth with a picture; a sentence frame for each interview or comparison step; a key line that separates a language gap from a content gap. Access: any spoken task can be done in writing, with a card or with the teacher. Reading load: a job profile is at most 150 words at the course's reading level; the rest is read aloud. Check accommodations: read aloud, oral answer, scribe, extra time. Extension: the same task on a less familiar field, never the next course's standard.
> **Section field 10:** a parent teaching one child at the table (a paper job card, a family member as the interview practice partner); one projector (one profile shown and compared by volunteers).
> **Section field 11:** what a school adds (speakers, visits, a counselor, a lab) goes here with the paper path when a school cannot. Safety for any field lab is named here and in the unit's tools line.

  Confidence: Firm.

### 5. No dose by band: pacing is a half-line in STANDARD.md and absent from APPROACH.md

- **Where:** STANDARD.md section 3 ("each course is one year ... at two or three sessions a week"); APPROACH.md (no Pacing section); bar C2 ("stated year and period length"); COURSE-RUN stage 1 ("the dose by band").
- **What is wrong:** There is no session length, no weeks in the year, no hours total, no short path and no statement of which band, or of whether grades 7 and 8 are the same band. Two to three sessions a week over a school year is 72 to 108 sessions only if a year is 36 weeks, which no page says; at 45 minutes that is 54 to 81 hours (my arithmetic, ours, untested). A range of "two or three" cannot feed the day-count gate. The health page gives the figure, the national benchmark, and says whether the default is above or below it; this page does none of that.
- **National or professional figure:** I found none. Advance CTE, the Association for Career and Technical Education and the National Career Development Association (NCDA) publish no hours-per-year figure for a career exploration course in what I could search (web search, 2026-11-20; no page opened that gives one). The only time figures turned up were state ones and unchecked: for example, Florida's exploratory career course is described as one semester (search summary only, not opened). The NCDG say their stages "are not tied to an individual's age or level of education" and give no time at all. So the page must say "no national time figure was found" and cite none, rather than imply one.
- **Cost:** A frame writer cannot count days; C2 and the "days add up" gate have no number to test. A reader may assume the dose is backed by a body.
- **Fix (add as "Pacing" to APPROACH.md; ours, untested):**

> **Pacing.** Settled 2026-11-16 (Cory): each course is one year at two or three sessions a week. Default time, ours and untested: 36 weeks, three sessions a week of 45 minutes, so 108 sessions or 81 hours a year; a school at two sessions a week runs the short path, 72 sessions or 54 hours, which names the sessions it drops (the second field task in each unit). No national body publishes a time figure for these courses that we found, so none is cited; the course page says so. Each frame may change these numbers with a reason.

  Confidence: Firm.

### 6. The course list and course shape disagree across five files

- **Where:** data/courses.csv lines 38 and 39 (grades 6-8 and 9-12, `typical_grade` blank); STANDARD.md header and section 3 (grade 7 or 8; grade 9 or 10); lens ("6 to 8", "9 to 12"); bar part 7 headings; docs/COURSES-STATUS.md ("Career and Technical Education (3 courses)", Personal Finance included); data/subjects.csv line 10 ("Career exploration, personal finance and career pathways", grades 6-12); data/courses.csv line 40 (personal-finance, cte, 9-12, typical 11, "taught inside Economics").
- **What is wrong:** (a) Two courses in STANDARD and the lens, three in COURSES-STATUS, three course-id rows under the `cte` subject in courses.csv and subjects.csv. (b) One grade span in courses.csv, two possible grades in STANDARD; `typical_grade` is blank for both. (c) Three of the five tool modules tagged to Exploration are personal finance (`cte-6-8-interest-rate-dial`, `cte-6-8-startup-shares`, `cte-6-8-e-bike-buyer`) while STANDARD section 5 says personal finance is left out and "not planned here"; the two others (`snow-season-prices`, `economy-checkup`) are economics. (d) The subject folder is `career-education`, the subject code `cte`, the course ids `cte-explore` and `cte-pathways`: the progression file name (data/progressions/cte.csv or career-education.csv) is not stated.
- **Cost:** The progression writer does not know which file to create, which grades to put, and whether to place personal finance modules. COURSES-STATUS will report three courses when two are planned.
- **Fix (a note in STANDARD.md section 3; the catalogue edits are a decision, not mine):**

> **Course list.** Two courses: `cte-explore` (grades 6 to 8 in the catalogue, taught in grade 7 or 8) and `cte-pathways` (grades 9 to 12, taught in grade 9 or 10). `typical_grade` is 8 and 10. Personal Finance is not a course (Economics, 2026-11-14); its modules are tagged to Economics. The progression file is data/progressions/cte.csv (subject code `cte`).

  Confidence: Firm that they disagree; the choice of file name is item-level (settled by the expert, below).

### 7. Cross-subject leans name subjects, not skills; the grade ambiguity also decides what a lean may assume

- **Where:** STANDARD.md section 6 ("ELA (resume and cover writing, interview speaking: W and SL standards); math (wages, percent, budgets...)").
- **What is wrong:** Stage 1 asks each lean to name a core skill that exists. This page names no skill id, so none can be checked. The ones that probably apply do exist in the progression files (checked by one-line id searches): ELA `e8-informative-writing` (W.8.2), `e8-revise-purpose-audience` (W.8.5), `e8-present-reasoning` (SL.8.4 to 6), `e8-collab-discussion` (SL.8.1), and grade 10 `e10-w-informative`, `e10-sl-presentation`; math `m7-percent-problems` (7.RP.A.3), `m7-unit-rate-fractions`, `m7-compare-populations` (7.SP.B.3 and 4); social studies `ss8-public-budget`, `ss7-roman-economy` (economics strand). Two further faults: a resume or cover letter is not one of the W standards' text types, so "W standards" names the wrong thing (it is informative writing aimed at an audience); and Exploration in "grade 7 or 8" cannot lean on `m7-percent-problems` if the course is taught in grade 7, and Pathways in grade 9 cannot lean on the grade 10 owner rows of the ELA 9-10 band (grade 9 ELA rows are `~` only).
- **Cost:** The reader at stage 2 ("every cross-subject lean points to a skill taught by then") cannot check any lean. A grade 7 Exploration unit could assume percent work that has just been met.
- **Fix (replace section 6; ours, untested):**

> **Cross-subject leans.** Exploration is placed in grade 8 for the gate (finding 2), so it may lean on grade 7 and 8 core rows; Pathways is placed in grade 10 and may lean on grade 9 and 10 rows. ELA: `e8-informative-writing` and `e8-revise-purpose-audience` (resume lines, an email to an employer), `e8-present-reasoning` (an interview answer), `e10-sl-presentation` (a portfolio defence). Math: `m7-percent-problems` and `m7-unit-rate-fractions` (wages, a budget), `m7-compare-populations` (reading a data display). Social studies: `ss8-public-budget` and the economics rows of the grade (labour markets). Computer science: `data` strand rows for the Digital Technology cluster. SEL: the SEL courses' sub-skills for self-knowledge and goals, by row id once the SEL progression is written. Library: the AASL competency for judging a source. Each lean is rechecked against the owner grade when the career education progression is written.

  Confidence: Firm that no id is named; the particular rows are Likely (found by one-line id searches, strand and grade not read in full).

### 8. Sensitive ground is one sentence; the real hazards in this subject are unnamed

- **Where:** STANDARD.md (nothing); APPROACH.md section field 9 ("privacy notes (no student shares family income or status)"); lens (stereotypes and private income named under "Errors").
- **What is wrong:** Nothing in the two pages names the ground a career course crosses, and nothing says what needs a sensitivity read (docs/pipeline/briefs/sensitivity-read.md, "every unit gets the sensitivity read"). Hazards a writer should be told (from my reading of the cluster list and the lens, not from a source):
  - **Pay and background:** gender and racial pay and occupational gaps (shown with a dated source, not as a verdict on a person); stereotype counters with real workers from many groups; first-generation, rural and tribal students; students who care for family or already work.
  - **Money and status:** family income, immigration or work-authorization status, criminal records and hiring, and what a "gap" in a resume may hide. No task asks a student for any of these.
  - **Disability and accommodations at work:** how disabled workers are shown, with the rights stated plainly and not as a lesson for others.
  - **Paths:** the Military and National Security sub-cluster, recruiters and the military entrance test; presenting the military as one real route with its costs and returns, neither promoted nor condemned, with no recruiter material. The same for apprenticeship, two-year, four-year, certificate, starting work: none is the default.
  - **Clusters that touch other subjects:** Behavioral and Mental Health (health's ground), Emergency Response, Judicial Systems and Public Safety (trauma, violence, force), Resource Extraction and Environmental Protection (a live public dispute that practice 11 invites), Entrepreneurship and Regulation (political), Financial Services (personal finance, left to Economics).
  - **Interview and resume tasks:** personal data on a resume (a student's real address, phone, school), questions an employer may not lawfully ask, and a mock interview that asks a student something private. Use invented characters for the models; the student's own resume uses a school address or none.
  - **Safety of hands-on tasks:** the bar (item 6) requires safety taught; no page says how (a task is paper or simulation only unless a school adds a lab).
- **Cost:** The bar's "fails if" for stereotypes and for private disclosure cannot be checked; units would be sent to a sensitivity read with no list of what to read for.
- **Fix (add as a section "Sensitive ground" to STANDARD.md; ours, untested):** a short list of the above, and: "Every unit gets the sensitivity read (brief: sensitivity). Units on the Military and National Security, Behavioral and Mental Health, Judicial Systems, Emergency Response and Resource Extraction sub-clusters, and the pay-gap unit, name the community or topic in the read's {community} slot. No task asks a student about their own family income, status, record or health. Job models use invented workers drawn from many groups." Confidence: Likely.

### 9. Pathways says the student picks two or three clusters, but nothing says how a class of thirty can do that

- **Where:** STANDARD.md section 3 table (Pathways: "Two or three clusters the student picks, studied at sub-cluster depth, with a program of study"); lens ("one cluster only (Pathways)" is a listed error).
- **What is wrong:** A free course with no teacher-built field lab cannot give every pick of 72 sub-clusters a field task, a program of study and a dated data sheet. Either it ships a fixed menu of clusters (and the page should say which and why), or it ships a task template that works on any chosen cluster and defers the cluster-specific facts to the student's own research (which the lens and bar C3 forbid doing without sources). The page chooses neither. This also decides what the gate can own (finding 2).
- **Cost:** The frame writer will either build for all 14 (unaffordable) or invent a menu.
- **Fix:** Choose one and write it (Question 2). Recommended text: "Pathways builds field tasks and data sheets for a fixed menu of six clusters; a student chooses two or three of them. A student may name a seventh cluster only for the general plan and portfolio pieces, using the course's task template and the student's own sources." Confidence: Judgment call.

### 10. The bar's "fails if" items are only partly answered by the two pages

- **Where:** bar part 7 criteria 1 to 8 and "Fails if" (career quizzes with no plan; no real data; no applied task; employability as a poster).
- **What is wrong:** Criterion 1 ("grow harder") and criterion 2 ("academic, technical and employability skills taught together") have no answer in either page: no statement of how Exploration and Pathways differ in demand, or how a task teaches an academic skill and a practice together. Criterion 6 (safety taught) has none. Criterion 8 (portfolio) is answered. "Employability as a poster" is answered by the practices-in-tasks rule but the page does not say how a practice is judged ("criteria", as the lens says). A related ordering fault: "Every unit ... ends with a plan day", while the check kind is an assessment day and the respond day follows it; the page does not say which closes the unit, so the plan day could be before or after the check.
- **Cost:** C1 and C4 trace through the progression, so this is an early but small hole. The ordering fault means a unit plan could put the plan day after the check and leave the check unable to score the plan.
- **Fix (add to APPROACH.md "The kinds of day"):**

> Order of a unit's last days: field task day, plan day, assessment day (scores the unit's best piece and the revised plan), respond day. In Pathways the task is the same shape at higher demand: a real data comparison, a defended decision, and a revision of the plan from feedback. Each practice taught in a unit is judged with two or three look-fors on the piece the student produces, never on a list. Any task with equipment is on paper or a simulation unless the school adds the lab; the unit's tools line names the safety step.

  Confidence: Likely.

### 11. Own words: nothing is copied, but practices 10 and 11 keep the publisher's title nearly whole

- **Where:** data/standards/cte-career-clusters-2024.txt header lines 9 to 20; STANDARD.md section 1.
- **What I found:** No run of source text appears in STANDARD.md, APPROACH.md or the lens. The practice lines are paraphrases of titles, not of the descriptions. Practice 10 ("plan an education and career path that fits one's strengths, work style, interests and goals") keeps the publisher's title wording and its four-item list almost word for word; practice 11 ("weigh the environmental and social effects of decisions") and practice 9 are very close to their titles. The publisher's text is all rights reserved, and these are titles, so this is a Judgment call, not a defect.
- **Fix (optional rewording, ours):** 10: "choose a route through school and work that suits what you are good at, how you like to work, what interests you and what you want"; 11: "think about who and what a choice affects, for people and for the places they live"; 9: "spend and look after money and materials carefully, for an employer and for yourself". Confidence: Judgment call.

### 12. Notes that are out of date or incomplete

- STANDARD.md section 2 and the bar row say the guidelines "refused the reader" (now reachable, finding 3); the lens says "2024 revision not read" (now read in text by this review).
- The bar's "To firm it" for part 7 lists "a second state's rubric", and the STANDARD owed table omits it, so the row can be marked done with only one rubric read.
- Practice numbers and titles are checked only against a state's reproduction (North Dakota), not Advance CTE's own page; both of the publisher's practice URLs I tried return 404. The page says so, which is right; keep the "to do" line.
- STANDARD.md header says "section 3" for the courses; the course mapping table is section 3 and the course shape sentence sits in section 3 too, so the header reference is right. No change.
- docs/COURSES-STATUS.md counts three courses (finding 6).
- The bar row for career education says "Owed: the approach page's yes" and omits the progression, the learner-goals file and the field block (findings 1 to 4).
- Confidence: Firm.

## What is right and should not be touched

- The 98 ids, their order, the header's refusal to copy the publisher's descriptions, and the cluster spellings that follow the guidebook (so the validator and the publisher agree).
- The standard's honest statement (section 2) that the clusters and practices do not say what a student can do, and the decision to use the NCDG as learner goals with a fallback of our own goals.
- Section 4, what a school adds, including the paper path and the "equipment and safety" line; and section 5, what is left out and why.
- The kinds-of-day table, the daily evidence list, and the "portfolio holds the unit's best piece; students choose and say why" rule.
- The scout: public domain BLS data and CC BY O*NET data, no company named, and the plan to refresh the data sheets yearly.

## Not checked

- The NCDA copyright and reuse page (the PDF text shows no statement; I did not open the site's terms page).
- The Texas rubric and any second state's rubric behind the bar's part 7 (not opened).
- Whether BLS and O*NET licence statements in the scout still say what the scout records (not re-opened; the scout dated them 2026-11-16).
- Advance CTE's own practices page (404).
- scripts/plan.py, data/plans, and whether a career education frame or tool exists (none seen).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Owner grades for the gate: Exploration 8, Pathways 10; the frame may place a course a year earlier with a reason | The span's last grade is the deadline, as health and physical education do; leans then rest on rows already taught | STANDARD.md section 3; progression retool |
| Progression file is data/progressions/cte.csv (subject code `cte`) | Matches data/subjects.csv and data/courses.csv | STANDARD.md section 3; scripts/progression.py `STD_FILES` and `ANCHOR` |
| Default: 36 weeks, 3 sessions a week, 45 minutes (108 sessions, 81 hours); short path 2 a week (72 sessions, 54 hours) | Gives C2 a number inside Cory's "two or three sessions a week" | APPROACH.md Pacing |
| Practices owned by Exploration with `~` rows in Pathways | Mirrors the health and physical education span rule: owned where first met, carried after | STANDARD.md section 3 |
| `codes()` splits on the tab and keeps the whole first field | Needed for every id with a space | scripts/progression.py (progression retool) |

## For Cory

1. **Which NCDG goals are the learner goals?** The 2024 guidelines have three domains and its third is Social Emotional Learning, which the SEL courses already teach. Recommended: career education owns the Career Development and Academic and Lifelong Learning goals (7 goals); the SEL goals are leans on the SEL courses. Or own all 11 and accept the overlap?
2. **How wide is Pathways?** Recommended: a fixed menu of six clusters, each with field tasks and a dated data sheet, chosen by students two or three at a time; a cluster outside the menu uses the task template only. Or build all 14, or keep it open to any of the 72 sub-clusters with student-sourced data? (This is authoring cost and audience.)
3. **How many sub-clusters does Exploration own?** Recommended: 14, one per cluster, fixed in the frame, with the other 58 excluded in the progression with the reason "student choice". Or two per cluster (28), at a higher cost per cluster?
4. **Where do the five economics and personal finance tool modules tagged to Exploration live?** Recommended: retag to Economics (STANDARD section 5 already leaves personal finance out of this subject) and drop "personal finance" from the data/subjects.csv description. Or keep three personal finance modules in Exploration as a light taste?
5. **Military route and recruiter contact.** Recommended: present it as one real route with costs and returns, no recruiter material on a student page, and a teacher-page note that a school's own recruiter policy governs visits. Or stay silent and let each school decide?
6. **Your yes on the approach page**, once findings 4, 5, 8 and 10 are in. It stays a draft until then.
