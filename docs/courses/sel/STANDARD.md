# Social and emotional learning: the standard, made usable

Written 2026-11-16 as the pre-work owed for social and emotional learning (docs/ADOPTION-BAR-SUBJECTS.md, "Before a
scope and sequence in this subject", the SEL row), in the shape of docs/courses/social-studies/STANDARD.md. Core
subjects come first: nothing here starts a frame or a scope and sequence. Decisions already made by Cory
(2026-11-11 and 2026-11-15): SEL stays as separate courses, not strands; they may be smaller by nature, which means
fewer minutes a week, never fewer units; there is a sequence for each grade; the design half of the registry's
criteria is the bar, with the evidence half stated as unmet, **marked for a deeper review** (section 4 is that
review).

| Owed row (ADOPTION-BAR-SUBJECTS) | State | Where |
|---|---|---|
| Separate courses (decided); they may be small | Applied: four band catalogue rows kept; minutes a week recommended, Cory decides | Section 2; question 1 |
| Write a sequence per grade | Done as a draft, 13 grade years, every grade covering all 40 sub-skills | Section 3 |
| The design half as the bar, marked for a deeper review | Review done (criteria paper pp 23 to 35 read in full); five gaps named, additions proposed for Cory | Section 4; question 3 |
| Approach page (all ten subjects) | Draft for Cory's yes | docs/courses/sel/APPROACH.md |
| Base text scout, lens | Done | docs/reviews/sel-open-material-2026-11-16.md; docs/agents/lenses/sel.md |

## 1. The standard and its terms

- **Standard.** The CASEL 5 framework: five competencies (self-awareness, self-management, social awareness,
  relationship skills, responsible decision-making), each with example sub-skills, 40 in all. Edition: the
  framework as CASEL presents it on its current page (the 2020 wording; the page itself carries no date or version),
  read 2026-11-16. The 40 sub-skills and their order were checked against the page that day and match the file.
- **File.** data/standards/casel-5.txt: `CASEL.<Competency>.<n><TAB>our own words`, 40 lines. The numbering is
  ours (the page's order), because CASEL numbers nothing. The page calls the sub-skills examples, not a closed
  list; Curio Class treats all 40 as the course's standards, so C1 has something to trace.
- **Short codes used on this page:** SA1 to SA9 (self-awareness), SM1 to SM7 (self-management), SO1 to SO8 (social
  awareness), RS1 to RS9 (relationship skills), RD1 to RD7 (responsible decision-making). The number is the file's
  `<n>`.
- **Reuse terms, checked at source 2026-11-16.** casel.org's terms of use allow personal, non-commercial use only and
  bar copying, adapting or publishing without written permission; the framework page is marked all rights
  reserved. So: ids and our own words only, as with CCSS and Massachusetts. No CASEL sentence, graphic (the wheel)
  or name of a CASEL product appears in a student, teacher or family page. Internal docs may name CASEL as the
  source.
- **The registry's criteria paper** (Evidence-Based Social and Emotional Learning Programs: CASEL Criteria Updates
  and Rationale, December 2020, (c) CASEL) is the instrument behind the bar. Read for this page: pp 1 to 3 and 20 to
  35 in full (the design and implementation criteria and the final designation rule).
- **Not a state standard.** Many states have their own SEL standards (often built on the same five areas), and some
  states restrict SEL in schools by law or rubric (the Florida rubric was reported to ask that materials leave SEL
  out; search only, docs/reviews/bar-other-subjects-2026-11-11.md). Curio Class does not claim any state's SEL
  standards. Each course page says what a school may leave out (section 5).
- **For the lead (scripts/standards.py is not ours to edit).** The validator does not read casel-5.txt, and its
  closed pattern `CASEL\.(Self-Awareness|...)` fully matches only the five competency codes, so a plan row coded
  `CASEL.Self-Awareness.3` would fail validation. Before the first SEL scope, standards.py should read this file as
  an id list, as it does for Massachusetts (later item; the competency codes in data/modules.csv stay valid).

## 2. Courses, bands and time

- **The catalogue.** data/courses.csv has one SEL track row (`sel-k12`); docs/COURSES-STATUS.md counts four band
  courses: K to 2, 3 to 5, 6 to 8, 9 to 12. The bar asks for a sequence for each grade, and the registry gives a
  single lesson set for a band its lower design rating. So each band course holds one distinct year per grade, and
  "a band taught the same way every year" is a fail (bar, Fails if).
- **How a grade year is framed (question 1 for Cory).** Recommended: each grade year gets its own frame and scope and
  sequence (13 in all), filed under the four band rows. That raises the frame count, not the catalogue rows, but it
  may change the 107 course count depending on how a "course" is counted; that is Cory's call.
- **Minutes (question 2 for Cory; the frame states it, per the pass rule).** Recommended: two sessions a week in
  every grade, 32 weeks, so 64 sessions a year: about 20 minutes in K to 2, 30 minutes in 3 to 8, 30 to 45 minutes in
  9 to 12 (an advisory period). With 40 sub-skills a year, one session a week (32 sessions) leaves each sub-skill
  less than one session of teaching and none of the spaced practice the bar asks for. One session a week stays as
  the stated short path (C2), with named sessions to drop.
- **Units.** Six units per grade year (section 3), each with its own readiness check and end-of-unit assessment,
  sized to the minutes chosen. "Never fewer units" is met: every sub-skill is taught, practised spaced out and
  checked every year.
- **Family notes** in English and Spanish per unit (decided 2026-11-11), which also answers part of the registry's
  translation criterion (section 4).

## 3. The sequence per grade

The draft year for each grade. The theme sets the year's angle, so no two years of a band run alike. Each unit lists
the sub-skills it teaches first that year; every later unit brings earlier sub-skills back in practice (C7). In
every grade all 40 sub-skills are taught once and only once as a unit's own (checked by script, 2026-11-16). Depth
grows by grade: the same code is a picture-book scene and a rehearsed step in kindergarten, a named strategy with
reasons in grades 3 to 5, a choice weighed under real pressures in 6 to 8, and a plan the student designs and judges
in high school.

How each competency is practised (bar item 5): self-management and relationship skills by doing (rehearsing a
calming routine, acting out an invented hard moment, practising an I-statement with a partner); self-awareness,
social awareness and decision-making by reflection and talk (a private journal, partner talk about a scenario, a
choice weighed in writing).

| Grade | Year theme | Units: name, then the sub-skills taught first |
|---|---|---|
| Kindergarten | Me, my feelings, my class | 1. Hello, our class: RS1, RS2, RS8, SO2, SA1<br>2. Naming my feelings: SA3, SA5, SM1, SM2<br>3. Being me: SA2, SA4, SA7, SA8, SA9<br>4. Kind hearts: SO1, SO3, SO4, SO5, SA6<br>5. Playing together: RS3, RS4, RS5, RS6, RS7, RS9, SM3, SO6, SO7<br>6. Good choices: RD1, RD2, RD3, RD4, RD5, RD6, RD7, SM4, SM5, SM6, SM7, SO8 |
| Grade 1 | Calm and kind | 1. Our class team: RS1, RS4, SO2, SA2<br>2. Calm body, calm mind: SA3, SM1, SM2, SM3<br>3. Small problems, big problems: RD3, RD4, RS5, RS6, RS8, SM6<br>4. How do they feel?: SO1, SO3, SO4, SO5, SA5, SA6, RS9<br>5. Families, friends and me: SA1, SA4, RS2, RS3, SO6, SO7, RD1<br>6. I can try, I can help: SA7, SA8, SA9, SM4, SM5, SM7, RS7, RD2, RD5, RD6, RD7, SO8 |
| Grade 2 | Fair and friendly | 1. Rules here and there: SO6, SO7, SO8, RS1, SA4<br>2. Strong feelings, steady me: SA3, SA5, SM1, SM2, SM3<br>3. Being a good friend: RS2, RS5, RS8, SO1, SO4<br>4. Standing up, speaking up: RS6, RS9, SO3, SA6, RD4<br>5. Goals and growing: SA7, SA8, SA9, SM4, SM5, SM6, SA2, SO2, SO5<br>6. Our class helps: RS3, RS4, RS7, SM7, SA1, RD1, RD2, RD3, RD5, RD6, RD7 |
| Grade 3 | Thinking, feeling, doing | 1. Think, feel, do: SA3, SA5, SM1, SM2, RD5<br>2. Who I am and what I bring: SA1, SA2, SA4, SA9, SO2<br>3. Walking in their shoes: SO1, SO3, SO4, SO5, SA6, RS3<br>4. When friends disagree: RS1, RS2, RS5, RS8, SO7<br>5. Saying no, choosing well: RS6, RS9, RD1, RD2, RD3, RD4, SO6<br>6. Goals that stretch me: SA7, SA8, SM3, SM4, SM5, SM6, SM7, RS4, RS7, RD6, RD7, SO8 |
| Grade 4 | Working together | 1. Team rules we make: RS1, RS4, SO6, SO7, SA4<br>2. Plans and steps: SM3, SM4, SM5, SM6, SA7, RD5<br>3. Many ways to be: SA1, SA2, RS3, SO1, SO2, SA6<br>4. Feelings at work: SA3, SA5, SM1, SM2, SO3, SO4, SO5<br>5. Leading and following: RS7, RS2, RS5, RS8, RS6, RS9, SM7<br>6. Thinking it through: RD1, RD2, RD3, RD4, RD6, RD7, SA8, SA9, SO8 |
| Grade 5 | Ready for change | 1. Changes ahead: SA3, SA5, SM1, SM2, SO7<br>2. What drives me: SA7, SA8, SA9, SM3, SM4, SM5<br>3. Who shapes what we do: SO6, SO8, RD2, RD5, SA6<br>4. Friends through change: RS1, RS2, RS5, RS6, RS8, SO1, SO3, SO4<br>5. My voice, our group: SM6, SM7, RS4, RS7, RS9, SO5, SO2<br>6. Choices with reach: RD1, RD3, RD4, RD6, RD7, SA1, SA2, SA4, RS3 |
| Grade 6 | New school, new me | 1. Finding my way: SM5, SM3, SO7, RS8, SA7<br>2. Who am I now?: SA1, SA2, SA4, SA9, SA3, SA5<br>3. Stress and strong feelings: SM1, SM2, SA8, RD5<br>4. Friendships that change: RS1, RS2, RS5, RS6, SO1, SO4, SO3<br>5. Online and offline norms: SO6, SO8, RD1, RD2, RD4, SA6<br>6. Goals and our team: SM4, SM6, SM7, RS3, RS4, RS7, RS9, SO2, SO5, RD3, RD6, RD7 |
| Grade 7 | Pressure and belonging | 1. Belonging and our groups: SA1, SA2, SA9, RS2, RS3, SO2<br>2. Under pressure: RS6, SO7, SO8, RD4, SM3<br>3. Snap judgements: SA6, SO1, SO6, RD1, RD2<br>4. Big feelings, steady choices: SA3, SA5, SM1, SM2, SA4, SA7, SA8<br>5. Repair and conflict: RS1, RS5, RS8, SO3, SO4, SO5<br>6. Taking the lead: SM4, SM5, SM6, SM7, RS4, RS7, RS9, RD3, RD5, RD6, RD7 |
| Grade 8 | Choices that count | 1. How I decide: RD1, RD2, RD4, RD5, SA5<br>2. Values and integrity: SA4, SA1, SA2, SA6, RS6, SO7<br>3. Stress, focus and rest: SA3, SA8, SM1, SM2, SM3, SM5<br>4. Understanding others: SO1, SO3, SO4, SO6, RS3, SO2<br>5. Communication and conflict: RS1, RS2, RS5, RS8, SO5<br>6. Making a difference: SA7, SA9, SM4, SM6, SM7, RS4, RS7, RS9, RD3, RD6, RD7, SO8 |
| Grade 9 | Finding my footing | 1. A new start: SM5, SM3, SO7, RS8, SA7, SA9<br>2. Stress and coping: SA3, SM1, SM2, SA5, SA8<br>3. Identity and assets: SA1, SA2, SA4, SA6, RS3<br>4. Relationships that are good for me: RS1, RS2, RS5, RS6, SO3, SO4<br>5. Norms, media and influence: SO6, SO8, RD1, RD2, RD4, RD5<br>6. Goals with others: SM4, SM6, SM7, RS4, RS7, RS9, SO1, SO2, SO5, RD3, RD6, RD7 |
| Grade 10 | Respect and relationships | 1. Listening to understand: RS1, SO1, SO4, SA5<br>2. Hard conversations: RS5, RS8, SM1, SM2, SA3<br>3. Culture and respect: RS3, SO6, SA1, SA2, SA6, SO2<br>4. Healthy boundaries: RS2, RS6, SA4, SO7, RD4<br>5. Teams that work: RS4, RS7, SM3, SM4, SM5, SM6, SO3, SO5<br>6. Fair to everyone: RS9, SM7, SO8, SA7, SA8, SA9, RD1, RD2, RD3, RD5, RD6, RD7 |
| Grade 11 | Purpose and plans | 1. What matters to me: SA9, SA4, SA5, SA1, SA2<br>2. Plans and setbacks: SM4, SM5, SM3, SA7, SA8, SM2, SM1, SA3<br>3. Weighing evidence for choices: RD1, RD2, RD4, RD5, SA6<br>4. Working with others: RS1, RS3, RS4, RS5, SO1, SO2, SO7<br>5. Help, support and pressure: RS8, RS2, RS6, SO3, SO4, SO5<br>6. Acting on what matters: SM6, SM7, RS7, RS9, SO6, SO8, RD3, RD6, RD7 |
| Grade 12 | Leading and leaving | 1. Looking back, looking ahead: SA1, SA2, SA9, SA7, SA5<br>2. Steady under change: SA3, SM1, SM2, SM3, SM5, SA8<br>3. Leading well: RS7, RS4, RS1, SO2, SO7, SM6<br>4. Communities and systems: SO6, SO8, RD6, RD7, SM7, RS9, SA6, RS3<br>5. Hard choices: RD1, RD2, RD3, RD4, RD5, SA4, RS6<br>6. Support after school: RS8, RS2, RS5, SO1, SO3, SO4, SO5, SM4 |

Placement notes, by sub-skill, where the grade matters most:

- **SA6 (own snap judgements) and SO6 (norms that have been unfair)** start in kindergarten and grade 1 as fairness
  at play ("everyone can join"), and reach unfair rules of the past in grade 5 and later, taught from settled facts
  (see section 5). Grade 7 ("Snap judgements") and grade 10 ("Culture and respect") are their main years.
- **SA8 (ability grows)** is taught as "practice and help make you better", never as a promise that belief alone
  raises grades: the evidence for short mindset lessons is mixed (lens, sources).
- **SO8 (systems shape behaviour)** starts as "why our class has rules" and grows to media and online norms in grade
  6 and to communities and systems in grade 12.
- **RS6 (saying no to pressure)** is taught as a skill on invented cases. The topics where pressure matters most in
  6 to 12 (substances, sex, dating violence) are health's; SEL rehearses the refusal skill and points to the health
  unit by name in the teacher notes.
- **RS9 (speaking up for others)** stays inside school life: an upstander in bullying or exclusion, a student who
  gets help for a friend. It is not a cause the course picks (section 5).
- **Transition years** carry the theme: grade 5 "Ready for change", grade 6 "New school, new me", grade 9 "Finding
  my footing", grade 12 "Leading and leaving".

## 4. The deeper review of the design half (Cory, 2026-11-11: "mark this for a deeper review")

Read in full for this review: the criteria paper, pp 23 to 35 (design criteria, design updates, implementation
criteria, final designation). Already on file: the EEF primary SEL guidance (six recommendations, SAFE),
Durlak and others 2011 and Cipriano and others 2023 (abstracts only), Oregon's transformative SEL tool
(docs/reviews/bar-other-subjects-2026-11-11.md).

**What the paper's design half asks, against our bar (ADOPTION-BAR-SUBJECTS part 9):**

| Paper (p) | What it asks, in our words | Our bar item | State |
|---|---|---|---|
| 23 | School-based, for every student, in school hours | 3 | Covered |
| 23 | All five competencies shown in the curriculum | 1 | Covered; section 3 goes further (all 40 sub-skills a year) |
| 23 | A sequence for each grade, or guidance for running it over several years | 2 | Covered by section 3 |
| 23 to 24 | One or more of four approaches: free-standing lessons, teaching practices, SEL inside academic subjects, school-wide structures | none | Ours is free-standing lessons; see gap A |
| 24 | Real practice: self-management and relationship skills by active rehearsal, the other three by reflection | 5 | Covered |
| 24 | SAFE: sequenced, active, focused, explicit | 4, 5, 6 | Covered |
| 24 | Lower rating for missing competencies, band-only lessons, too little practice | Fails if | Covered |
| 25 | Settings rated (classroom, school, family, community) as minimal, adequate or extensive | 7 (in part) | Gap B |
| 25 | Number of sessions a year reported; tools to monitor implementation and student behaviour | none | Gap C |
| 26 to 30 | Equity strategies: translation beyond English; students as agents of change; understanding context and working with bias (adult side) | none | Gap D |
| 27 to 29, 31 to 34 | Adult SEL and training: active, modelled, with feedback, building adults' own competencies | none | Gap E |
| 35 | Final rating is the lower of evidence and design | 8, "Unsupported" | Stated; the evidence half is unmet by design |

**Gaps and proposals.** Each proposal would change ADOPTION-BAR-SUBJECTS part 9, which only Cory's yes and the lead
may edit (question 3).

- **A. Approaches.** Free-standing lessons are the approach the registry most often rates; SEL inside academic
  courses is also counted. Proposal: keep free-standing courses (decided), and add one line to the bar: each SEL
  unit names one link to that grade's core courses (an ELA discussion routine, a social studies civics row) that
  the teacher may use. This is a lean, not a strand.
- **B. Settings.** Bar item 7 asks for a way to carry the skill beyond the lesson. Proposal: make it concrete. Each
  unit has a "carry it out" line for the school day (a cue the teacher uses outside the session) and a family
  activity in the family note. Community is optional.
- **C. Sessions and monitoring.** Proposal: the scope and sequence states sessions a year (it will, section 2). For
  monitoring, promise 2 rules out tracking students; a paper fidelity checklist for the teacher (did the session
  run as planned, which part was cut) and the class record sheet of skill checks meet the purpose without
  student data. Behaviour ratings of individual children are not collected.
- **D. Equity strategies.** Translation: family notes in English and Spanish are decided; student pages in Spanish
  are not, and that is a cost and scope call (question 4). Students as agents of change: under the values rule, SEL
  gives student voice in class and school life (class norms, a school improvement the class proposes and carries
  out), and leaves the analysis of causes of inequity to social studies, where it is taught from sources and
  evidence. Working with bias: SA6 is taught as noticing and checking one's own snap judgements on invented cases,
  never as assigning guilt or innocence to a group. This is the "middle line" ADOPTION-BAR-SUBJECTS sets for C12.
- **E. Adult SEL.** Professional learning is none for now (decided 2026-11-11). Proposal: each unit's teacher page
  opens with a short "before you teach" note: the skill as an adult uses it, and one thing to model. Not training,
  and not claimed as such.

**Verdict of the review.** The design half is a sound bar for these courses: it is specific (SAFE, practice by
doing, grade sequence, all competencies) and checkable on paper. It is not enough alone in three places (B, C, D), and the
proposals close them within the promises. The evidence half stays unmet and is said so on every course page (bar
item 8): no study has tried these courses. The registry rates a program by the lower of the two halves, so
Curio Class must never call its SEL courses "evidence-based" or use the registry's rating words.

## 5. Sensitive ground: FOUNDATION's promises and the values rule

SEL touches family, identity and mental health, so these rules hold in every SEL unit, read at the Finish check by
the fresh sensitivity agent (FOUNDATION promise 7, BASELINE rules 5, 6 and 8).

**The values rule, in order** (Cory, DESK-ANSWERS 2026-11-12, as social studies applies it): (a) where a court has
ruled, side with the higher court; (b) facts and backed sources decide claims; (c) people are taught with dignity,
respect, kindness and openness, and we do not hide humanity (families of every kind appear where families appear,
LGBTQ families included, as in social studies); (d) grade level and life experience set how and when a subject is
taught. FOUNDATION's promises still bind.

Applied to SEL:

1. **Nothing personal is collected or scored.** Promise 2 (no tracking, no student analytics). A journal or
   reflection stays with the student; the teacher may read it only if the student offers it. Checks score a skill
   (naming the steps of a calming routine, choosing a fair next step in an invented case), never a feeling, a
   trait or a home life. No student surveys about feelings, family or mental health.
2. **No disclosure is asked for.** Prompts use invented characters and cases, or "a time you choose to share, or
   make one up". No activity asks a child to rank, sort or reveal their identity, family situation or past harm
   (no privilege walks, no "step forward if" games).
3. **Role play stays safe.** Students rehearse a skill in an invented, low-stakes moment. No role play that puts a
   child in a victim's or perpetrator's place, or casts a real classmate (the same rule as social studies).
4. **SEL is not therapy.** No diagnosis, no clinical words used of a child, no claim that a course treats anxiety or
   depression. Calming routines are breathing, movement and pause, taught as plain body skills with no religious or
   spiritual framing. Each unit's teacher notes say: if a child discloses harm or risk, follow the school's
   reporting policy and refer to the counselor. Suicide prevention, substances and sexual health belong to health.
5. **Hard facts plain, at the right age.** SO6 "norms that have been unfair" uses settled history the courts have
   ruled on (school segregation struck down in 1954 is the model case) and facts, not opinion; current political
   disputes are not SEL content. Grade sets the case: playground fairness in K to 2, unfair rules of the past from
   grade 5.
6. **Families.** Every family note says what the unit teaches, the words it uses and how to practise at home, in
   English and Spanish. Each SEL unit can be left out by a school without breaking the course (as health's
   sensitive units can), and the course page says so ("Acceptability is local", ADOPTION-BAR-SUBJECTS).
7. **No product names, no rating words.** No program, app or registry name in public copy; no claim of being
   reviewed, approved, "evidence-based" or rated.

## 6. Left out, and why

- **The registry's school-wide and adult parts** (organizational strategies, staff SEL, coaching): Curio Class
  makes classroom courses and offers no professional learning for now (decided 2026-11-11). Section 4, E is the
  small stand-in.
- **Measuring children's SEL** with rating scales or screeners: promise 2, and such measures are for schools and
  counselors, not curriculum.
- **Mental health topics** (disorders, crisis, suicide prevention) and risk topics (substances, sexual health,
  dating violence): health (NHES 2024 and the HECAT topics), with SEL teaching the underlying skills.
- **Informed action and analysis of systems** past what a grade's sub-skills need: social studies.
- **Pre-kindergarten**: outside the course list.

## 7. Leans on other subjects

- **Health (NHES 2024, data/standards/nhes-2024.txt).** NHES S4 (interpersonal communication), S5 (decision making)
  and S6 (goal setting) overlap RS1, RS5, RS6, RD2 to RD4 and SM4. Rule: SEL teaches the skill on everyday cases;
  health applies it to health topics. When both courses run in a grade, the health frame names the SEL unit as
  "builds on" and does not reteach the steps. To check when health's frames are written.
- **ELA (data/progressions/ela.csv).** The discussion rows (ek-discussion to e5-discussion, e6-collab-discussion to
  e8-collab-discussion, e9-sl-discussion, e10-sl-seminar and on) carry turn-taking, listening and building on
  others' ideas. SEL's RS1 uses the same norms and words, so a class meets one set of talk rules.
- **Social studies (data/progressions/social-studies.csv).** ssk-rules-why, ssk-talk-together, ss1-group-rules and
  ss1-community-problems overlap SO8, RS1 and RD3 in K and 1. SEL takes the personal side (how I act in a group);
  social studies the civic side (why a community makes rules). The K and 1 SEL frames cite those rows as
  context links.
- These leans are noted here for the frames; the core progressions are not edited.

## Questions for Cory

1. **Frames per grade or per band.** Each SEL grade year as its own frame and scope and sequence (13) under the four
   band rows (pick: the bar and the registry both want a distinct year per grade), or four band frames each holding
   three or four year plans.
2. **Minutes.** Two sessions a week in every grade, 64 a year (pick: 40 sub-skills need spaced practice), or one a
   week, 32 a year, as the main path.
3. **The bar additions from the deeper review** (section 4, A to E): add them to ADOPTION-BAR-SUBJECTS part 9 (pick),
   or keep part 9 as it stands.
4. **Spanish student pages for SEL** (the registry's translation criterion): family notes only, as decided (pick for
   now, no new cost), or student pages too, later, as a growth item.
