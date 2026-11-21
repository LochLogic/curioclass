# Career education: the standard, made usable

**DRAFT, 2026-11-16. Read cold 2026-11-20 (docs/reviews/prework-career-education-read-2026-11-20.md) and fixed.**

Written 2026-11-16 as the subject's pre-work (docs/PRODUCTION-PATH.md, "After the core subjects"; the owed row in
docs/ADOPTION-BAR-SUBJECTS.md, "Before a scope and sequence in this subject"). The model is
docs/courses/social-studies/STANDARD.md. Two courses: Career Exploration (`cte-explore`, one year in grade 7 or 8) and
Career Pathways (`cte-pathways`, one year in grade 9 or 10), section 3. Personal finance is not a course: Economics teaches it, lightly
integrated (Cory, 2026-11-14), so it is not planned here.

## The owed row, and where it stands

| Owed | State | Where |
|---|---|---|
| Read the 2024 career-ready practices wording | Done 2026-11-16, from a state's reproduction (the publisher's page was not reachable); described in our own words | data/standards/cte-career-clusters-2024.txt header; section 1 |
| List what a school adds | Done | Section 4 |
| A learner standard for the two courses | Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library); the guidelines PDF is reachable now; the file, our own words and a read of its terms are owed | Section 2 |
| A second state's rubric (the bar's "to firm it") | Owed | docs/ADOPTION-BAR-SUBJECTS.md part 7 |
| Progression gate support | Owed: scripts/progression.py reads ids up to the first space, so every id here becomes `CTE.Career`; it also has no entry for the subject | Section 3 |
| Approach page | Draft, waiting on Cory's yes | docs/courses/career-education/APPROACH.md |

## 1. The standard and its terms

- **Which:** Advance CTE, Modernized National Career Clusters Framework, 2024 (guidebook June 2025). 14 Career
  Clusters (three cross-cutting: Digital Technology, Management and Entrepreneurship, Marketing and Sales), 72
  Sub-Clusters, and 12 Career Ready Practices, all in data/standards/cte-career-clusters-2024.txt.
- **The practices, 2024:** read 2026-11-16 in North Dakota CTE's copy of the 2024 list (dated 2025-06), because
  careertech.org's PDF is image-only and its practice page did not answer the reader. The twelve, in our words, are
  in the file header: professional contribution, clear communication, critical thinking and persistence, teamwork
  across differences, digital tools and data, resilience, managing time and space, creativity, stewardship of money
  and resources, planning one's own education and career path, environmental and social effects of decisions, and
  applying academic and technical skills. The 2024 list reframes the 2012 practices around the workplace and adds
  example tasks; numbering is by the 2024 order. To do when reachable: check the order against careertech.org itself.
- **Terms:** copyright Advance CTE, no reuse terms on the page (docs/reviews/standards-currency-2026-11-11.md). Cluster
  and practice names may be cited; the practice descriptions are never copied. Pages say "the national career
  clusters" in our own words and never claim alignment approved by anyone.

## 2. What the standard can and cannot do for these courses

The cluster framework says which fields exist and how they group; the practices say what a worker does. Neither says
what a grade 7 student should know or be able to do about planning a career. The bar (part 7) asks for a personal
plan, labour market data, career tasks (resume, interview, portfolio), hands-on work and defended choices.

**The learner goals.** Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library): the National Career
Development Guidelines (National Career Development Association, 2024 revision: three domains, goals and leveled
indicators) are the learner goals, with the clusters and practices as content. Fallback: if its terms bar ids and
our own words, Curio Class writes its own learning goals per course, marked "ours". Still owed: the guidelines file
and a read of its terms. The 2024 framework PDF is reachable (ncda.org, read in text by the cold reader 2026-11-20,
no copyright or reuse statement seen in it): three domains, eleven goals, about 228 indicators coded like `CD1.K1`,
in three stages that are not tied to an age. Its third domain is Social Emotional Learning (four goals, about a third
of the indicators), which the SEL courses already teach. So career education owns the Career Development and the
Academic and Lifelong Learning goals (seven goals), and the Social Emotional Learning goals are leans on the SEL
courses. Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-open-2) Saving the PDF and loading the file waits on Cory's yes (a download), then a read of NCDA's terms page.

## 3. How the standard maps to our courses (recommended, ours)

| Course | Clusters | Practices | Plan and tasks |
|---|---|---|---|
| Career Exploration, grade 7 or 8 | All 14 clusters surveyed, with a sub-cluster in each studied through real jobs and data | All 12 introduced, each practised in a task | An interest and strengths inventory, a first education and career plan, a job study with labour market figures, a short interview practice |
| Career Pathways, grade 9 or 10 | Two or three clusters the student picks, studied at sub-cluster depth, with a program of study (courses, training, credentials) | All 12 practised on field tasks | A full plan to a first credential, a resume, a mock interview, a portfolio, an applied project from a chosen field defended with data |

Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library): each course is one year (Career Exploration in
grade 7 or 8, Career Pathways in grade 9 or 10), at two or three sessions a week. The frames say which grade and
how many sessions.

**Pathways' width.** Pathways builds field tasks and dated data sheets for a fixed menu of six clusters, and a student
chooses two or three of them. A student may name a seventh cluster only for the general plan and portfolio pieces,
using the course's task template and the student's own sources. Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-open-2)

**Course list** (settled by the expert reader, 2026-11-20). Two courses: `cte-explore` (grades 6 to 8 in the
catalogue, taught in grade 7 or 8) and `cte-pathways` (grades 9 to 12, taught in grade 9 or 10). Personal finance is
not a course (Economics, 2026-11-14). The progression file is data/progressions/cte.csv (subject code `cte`). The
catalogue's personal finance row and the five tool modules tagged to Exploration (three personal finance, two
economics) are for Cory: the recommendation is to retag them to Economics. Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-open-2)

**Ownership** (settled by the expert reader, ours, untested). The progression has one row per owned item. For the gate,
a course's owner grade is its later grade (Exploration 8, Pathways 10), as health and physical education use the span's
last grade; the frame may place a course a year earlier with a reason. Exploration owns the 14 clusters and 14 named
sub-clusters, one per cluster, fixed in the frame. Pathways owns the sub-clusters of its six-cluster menu. Every other
sub-cluster is excluded with the reason "student choice; met only through the general task template". The 12 practices
are owned by Exploration, where each is first taught in a task, and Pathways carries each as a `~` row with the field
task that practises it at higher demand. The learner goals, once loaded, are owned the same way. Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-open-2)

**What the gate needs** (a note for the progression retool; scripts/progression.py is not edited here): ids split on
the tab only, keeping the whole first field as scripts/standards.py does (the same split also cuts the SEL competency
names, which hold spaces); `cte` in STD_FILES with this file and the learner-goals file, and in ANCHOR with the
learner-goals file; and a code_grades case that returns no grade for `CTE.` ids.

Data the courses use: the US Bureau of Labor Statistics Occupational Outlook Handbook and wage data (public domain,
credit asked) and the O*NET database (CC BY 4.0, with its required attribution in the credit line only). See the scout.

## 4. What a school adds (quality that lies outside materials)

The course page says this plainly. A school adds:
- **People:** guest speakers, workplace visits, job shadows, internships or other work-based learning, and a counselor
  for one-to-one planning.
- **Its own context:** its state's programs of study, local labour market figures, its state's required plan (many
  states mandate an individual career and academic plan, often in a state system), dual-credit and credential offers.
- **Equipment and safety:** any field lab (tools, kitchens, shops, clinical kits) and the safety training it needs.
  Curio Class supplies simulations and paper tasks, not equipment.
- **Student organisations** for the field, if it has them.
- **Time:** a period or advisory slot the course runs in.

## 5. What is left out, and why

- Technical courses inside one cluster (a welding or nursing course): not on the course list, and the bar's part 7
  notes the framework "would not fit a technical one".
- Personal finance (Economics, 2026-11-14); practice 9 leans on Economics' personal finance standards.
- The older 16-cluster framework (superseded; noted in the file).

## 6. Sensitive ground

No task asks a student about their own family income, immigration or work status, a criminal record or their health.
Job models use invented workers drawn from many groups, and a student's own resume uses a school address or none.

- **Pay and background:** pay and job gaps by sex and race are shown with a dated source, never as a verdict on a
  person; real workers from many groups counter stereotypes; first-generation, rural and tribal students, and students
  who care for family or already work, are planned for.
- **Disability at work:** disabled workers shown doing the work, with workplace rights stated plainly.
- **Paths:** no route is the default (apprenticeship, a certificate, two-year or four-year study, starting work, the
  military). The military is one real route with its costs and returns, neither promoted nor condemned, with no
  recruiter material on a student page; a teacher-page note says the school's own policy governs recruiter visits.
  Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-open-2)
- **Clusters that touch other subjects:** Behavioral and Mental Health (health's ground), Emergency Response and
  Judicial Systems and Public Safety (violence, force, trauma), Resource Extraction and Environmental Protection (a
  live public dispute), Entrepreneurship and Regulation (political), Financial Services (left to Economics).
- **Interview and resume tasks:** no question an employer may not lawfully ask, and no mock interview that asks a
  student something private.
- **Hands-on tasks:** on paper or a simulation unless the school adds the lab; the unit's tools line names the safety
  step.

**Reads.** Every unit gets the fresh-agent sensitivity read (docs/pipeline/briefs/sensitivity-read.md, kind
`sensitivity`). Units on the Military and National Security, Behavioral and Mental Health, Judicial Systems, Emergency
Response and Resource Extraction sub-clusters, and the pay-gap unit, name that community or topic in the read's
community slot.

## 7. Cross-subject leans

Exploration is placed in grade 8 for the gate, so it may lean on grade 7 and 8 core rows; Pathways is placed in grade
10 and may lean on grade 9 and 10 rows. A resume or a cover letter is informative writing aimed at a reader, not one
of the writing standards' own text types.

- **ELA:** `e8-informative-writing` and `e8-revise-purpose-audience` (resume lines, an email to an employer),
  `e8-present-reasoning` (an interview answer), `e8-collab-discussion`, `e10-w-informative`, `e10-sl-presentation` (a
  portfolio defence).
- **Math:** `m7-percent-problems` and `m7-unit-rate-fractions` (wages, a budget), `m7-compare-populations` (reading a
  data display).
- **Social studies:** `ss8-public-budget` and the grade's economics rows (labour markets); Economics carries personal
  finance.
- **Computer science:** the data strand rows, for the Digital Technology cluster.
- **Library:** judging a source by lateral reading (AASL.IV.B.3, owned in the library progression).
- **SEL:** the SEL courses' sub-skills for self-knowledge and goals (SEL STANDARD.md, self-awareness and self-management), named by progression row id when this subject's progression is written.

Each lean is rechecked against the owner grade when the career education progression is written.
