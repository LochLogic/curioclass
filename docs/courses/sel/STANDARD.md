# Social and emotional learning: the standard, made usable

**Settled calls in (Cory, 2026-11-21, Desk q-prework-open-1); stage 1 fix pass 2026-11-21
(docs/reviews/prework-sel-fixes-2026-11-20.md). Written 2026-11-16.**

Written 2026-11-16 as the pre-work owed for social and emotional learning (docs/ADOPTION-BAR-SUBJECTS.md, "Before a
scope and sequence in this subject", the SEL row), in the shape of docs/courses/social-studies/STANDARD.md. Frames are
written from 2026-11-25 (Cory, docs/DESK-ANSWERS.md); scopes, unit plans and days follow docs/COURSE-RUN.md. Decisions already made by Cory
(2026-11-11 and 2026-11-15): SEL stays as separate courses, not strands; they may be smaller by nature, which means
fewer minutes a week, never fewer units; there is a sequence for each grade; the design half of the registry's
criteria is the bar, with the evidence half stated as unmet, **marked for a deeper review** (section 4 is that
review).

| Owed row (ADOPTION-BAR-SUBJECTS) | State | Where |
|---|---|---|
| Separate courses (decided); they may be small | Applied: four band courses, one band frame each with a Year column (Cory, 2026-11-25), 64 sessions a year (settled 2026-11-16) | Section 2 |
| Write a sequence per grade | Done as a draft, 13 grade years, every grade covering all 40 sub-skills | Section 3 |
| The design half as the bar, marked for a deeper review | Review done (criteria paper pp 1 to 3 and 20 to 35 read in full); five gaps named; the additions are in bar part 9 (settled 2026-11-16) | Section 4 |
| Approach page (all ten subjects) | Approved by Cory 2026-11-21 (Desk q-prework-open-1) | docs/courses/sel/APPROACH.md |
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
- **The validator.** scripts/standards.py reads this file as an id list (valid as listed), so a plan row coded
  `CASEL.Self-Awareness.3` passes; the five competency codes in data/modules.csv remain valid.

## 2. Courses, bands and time

- **The catalog.** data/courses.csv has four SEL band rows (`sel-k-2`, `sel-3-5`, `sel-6-8`, `sel-9-12`; Cory,
  2026-11-21, "Light shelf" dropped), as docs/COURSES-STATUS.md counts them. The bar asks for a sequence for each grade, and the registry gives a
  single lesson set for a band its lower design rating. So each band course holds one distinct year per grade, and
  "a band taught the same way every year" is a fail (bar, Fails if).
- **How a grade year is framed.** Settled 2026-11-16 (Cory, Desk card q-later-sel-eld): each grade year is
  framed whole, with its own year of units. Since 2026-11-25 (Cory, docs/DESK-ANSWERS.md) a band has one frame with a
  Year column, and its scope and sequence is written one year at a time. plan.py takes one course id per band (the
  four catalog ids).
- **Sessions.** Settled 2026-11-16 (Cory, Desk card q-later-sel-eld): two sessions a week in every grade, 32 weeks,
  so 64 sessions a year. A session is 20 minutes in K to 2, 30 in grades 3 to 5, 30 in grades 6 to 8 and 40 in
  grades 9 to 12 (an advisory period); a frame may change its band's number and gives the reason. The registry's
  criteria ask that sessions a year be stated and set no number (criteria paper p 25, section 4), so the course page
  states ours with no national figure to compare. The Education Endowment Foundation's toolkit entry for social and
  emotional learning finds shorter sessions, up to 45 minutes, twice a week, the most successful structure for
  interventions (web page, read 2026-11-21); our minutes sit inside that. "Two 30-minute sessions a week" is not on
  that entry or on the primary guidance report's web page (read 2026-11-21) and is not used; the report itself is a
  file to download, unread. One session a week (32 sessions) is the stated short path (C2), and
  it never drops a unit.
- **How the sessions add up** (Cory, 2026-11-21, Desk q-fix-sel-1). Related sub-skills are taught together, so a
  unit splits its sub-skills (up to eight) into two or three groups, one section each. Each group is introduced
  (Understanding) and then rehearsed (Fluency, Application), and every session rehearses. Full year, 64 = four units
  of 11 and two of 10: a three-group unit is 3 groups of 3 sessions (Understanding, Fluency, Application) plus a
  Check and a Respond, 11; a two-group unit is 2 groups of 4 (Understanding, two Fluency, Application) plus a Check
  and a Respond, 10. The frame says which four units take three groups (most often those with the most sub-skills)
  and may move a session between units if the year stays 64. Short path, 32 = four units of 5 and two of 6, all six
  units and every group kept, fewer minutes a unit, never fewer units: each group's Understanding and Fluency share
  one session, the unit's Application sessions become one, and the Check and Respond share one. A three-group unit
  is 3 + 1 + 1 = 5; a two-group unit keeps a second rehearsal per group, 2 x 2 + 1 + 1 = 6. So the short path cuts
  Fluency and Application sessions and joins the Check with the Respond; it drops no sub-skill, group or unit.
- **Units.** Six units per grade year (section 3), each with its own readiness check and end-of-unit assessment,
  sized to the minutes chosen. "Never fewer units" is met: every sub-skill is taught, practiced spaced out and
  checked every year.
- **Spanish.** Family notes in English and Spanish per unit (decided 2026-11-11); student pages stay English only
  for now (settled 2026-11-16, Cory, Desk card q-later-sel-eld). Growing Spanish across the site is a later roadmap
  item (the lead's note).

## 3. The sequence per grade

The draft year for each grade. The theme sets the year's angle, so no two years of a band run alike. Each unit lists
the sub-skills it teaches first that year; every later unit brings earlier sub-skills back in practice (C7). In
every grade all 40 sub-skills are taught once and only once as a unit's own. No unit teaches more than eight
sub-skills first, so each has time to be rehearsed (a unit has 10 or 11 sessions, or the sizes its band frame sets to fit course-level checks, its sub-skills taught in two or
three groups of related skills, each group introduced then rehearsed: section 2, "How the sessions add up"); a sub-skill that suits a late
unit better comes back there in practice, not as a first teaching.

**Depth ladder, by band.** K to 2: a picture or story moment, one or two pictured steps, said aloud or acted with a
teacher; the skill is named. Grades 3 to 5: a named strategy with three or four steps and a reason, used on an
invented case and then in a planned class moment. Grades 6 to 8: the strategy chosen among options and weighed
against real pressures (friends, online, time), with the reason written down. Grades 9 to 12: a plan the student
designs for an invented or chosen situation, with its trade-offs and a judgement of how well it worked. Within a
band the first year uses cases from the school day, the second adds a second person's point of view, and the third
adds a cost or a pressure; grade 12, the fourth year of 9 to 12, adds a setting past school (work, community, life
after school). The progression row for each sub-skill says which step a year is.

**Ownership, for the progression** (settled 2026-11-21: Cory asked for a pedagogical check of the recommendation and
its use if it held; it held with two fixes, docs/reviews/sel-ownership-check-2026-11-21.md). One owned row per
sub-skill per band, so 40 sub-skills by four bands is 160 owned rows. A band's owner year is its last grade (2, 5, 8
and 12), the year the sub-skill is met at the band's full depth. Every grade year still has its own row for all 40
sub-skills (520 rows in all), and the other years of the band carry the id as `~ID`. A `~` row is a full teaching
row, not a lesser one: it has its own words, steps and exit ticket at its year's depth, and a one-line note on how
that year differs. Each row's `assumes` names the same sub-skill in the year before (a `~` row or an owner row;
kindergarten assumes nothing for it), so a band's later years build on its earlier ones and the first year of a band
builds on the previous band's owner row, with a note on the step up. The grade table below stays the placement, and
every year still teaches all 40 once. Other subjects' leans name the SEL row of the grade whose depth they need.
scripts/progression.py checks this form (MULTI_OWNER: one owner per id in each of grades 2, 5, 8 and 12); it has
supported SEL since 2026-11-21, and data/progressions/sel.csv passes it.

How each competency is practiced (bar item 5): self-management and relationship skills by doing (rehearsing a
calming routine, acting out an invented hard moment, practising an I-statement with a partner); self-awareness,
social awareness and decision-making by reflection and talk (a private journal, partner talk about a scenario, a
choice weighed in writing).

| Grade | Year theme | Units: name, then the sub-skills taught first |
|---|---|---|
| Kindergarten | Me, my feelings, my class | 1. Hello, our class: RS1, RS2, RS8, SO2, SA1<br>2. Naming my feelings: SA3, SA5, SM1, SM2, SM7, SM6, SM5, SM3<br>3. Being me: SA2, SA4, SA7, SA8, SA9<br>4. Kind hearts: SO1, SO3, SO4, SO5, SA6, SO8<br>5. Playing together: RS3, RS4, RS5, RS6, RS7, RS9, SO6, SO7<br>6. Good choices: RD1, RD2, RD3, RD4, RD5, RD6, RD7, SM4 |
| Grade 1 | Calm and kind | 1. Our class team: RS1, RS4, SO2, SA2<br>2. Calm body, calm mind: SA3, SM1, SM2, SM3, SM7, SM5<br>3. Small problems, big problems: RD3, RD4, RS5, RS6, RS8, SM6, RS7<br>4. How do they feel?: SO1, SO3, SO4, SO5, SA5, SA6, RS9, SO8<br>5. Families, friends and me: SA1, SA4, RS2, RS3, SO6, SO7, RD1<br>6. I can try, I can help: SA7, SA8, SA9, SM4, RD2, RD5, RD6, RD7 |
| Grade 2 | Fair and friendly | 1. Rules here and there: SO6, SO7, SO8, RS1, SA4, SO5<br>2. Strong feelings, steady me: SA3, SA5, SM1, SM2, SM3, SA1, SM7<br>3. Being a good friend: RS2, RS5, RS8, SO1, SO4, RS7<br>4. Standing up, speaking up: RS6, RS9, SO3, SA6, RD4<br>5. Goals and growing: SA7, SA8, SA9, SM4, SM5, SM6, SA2, SO2<br>6. Our class helps: RS3, RS4, RD1, RD2, RD3, RD5, RD6, RD7 |
| Grade 3 | Thinking, feeling, doing | 1. Think, feel, do: SA3, SA5, SM1, SM2, RD5, RD6<br>2. Who I am and what I bring: SA1, SA2, SA4, SA9, SO2<br>3. Walking in their shoes: SO1, SO3, SO4, SO5, SA6, RS3, SO8<br>4. When friends disagree: RS1, RS2, RS5, RS8, SO7, RS7<br>5. Saying no, choosing well: RS6, RS9, RD1, RD2, RD3, RD4, SO6, RD7<br>6. Goals that stretch me: SA7, SA8, SM3, SM4, SM5, SM6, SM7, RS4 |
| Grade 4 | Working together | 1. Team rules we make: RS1, RS4, SO6, SO7, SA4<br>2. Plans and steps: SM3, SM4, SM5, SM6, SA7, RD5<br>3. Many ways to be: SA1, SA2, RS3, SO1, SO2, SA6<br>4. Feelings at work: SA3, SA5, SM1, SM2, SO3, SO4, SO5, SO8<br>5. Leading and following: RS7, RS2, RS5, RS8, RS6, RS9, SM7<br>6. Thinking it through: RD1, RD2, RD3, RD4, RD6, RD7, SA8, SA9 |
| Grade 5 | Ready for change | 1. Changes ahead: SA3, SA5, SM1, SM2, SO7<br>2. What drives me: SA7, SA8, SA9, SM3, SM4, SM5<br>3. Who shapes what we do: SO6, SO8, RD2, RD5, SA6<br>4. Friends through change: RS1, RS2, RS5, RS6, RS8, SO1, SO3, SO4<br>5. My voice, our group: SM6, SM7, RS4, RS7, RS9, SO5, SO2, RS3<br>6. Choices with reach: RD1, RD3, RD4, RD6, RD7, SA1, SA2, SA4 |
| Grade 6 | New school, new me | 1. Finding my way: SM5, SM3, SO7, RS8, SA7<br>2. Who am I now?: SA1, SA2, SA4, SA9, SA3, SA5<br>3. Stress and strong feelings: SM1, SM2, SA8, RD5, RD6<br>4. Friendships that change: RS1, RS2, RS5, RS6, SO1, SO4, SO3, SO5<br>5. Online and offline norms: SO6, SO8, RD1, RD2, RD4, SA6, SO2, RD7<br>6. Goals and our team: SM4, SM6, SM7, RS3, RS4, RS7, RS9, RD3 |
| Grade 7 | Pressure and belonging | 1. Belonging and our groups: SA1, SA2, SA9, RS2, RS3, SO2, RS4<br>2. Under pressure: RS6, SO7, SO8, RD4, SM3<br>3. Snap judgements: SA6, SO1, SO6, RD1, RD2<br>4. Big feelings, steady choices: SA3, SA5, SM1, SM2, SA4, SA7, SA8<br>5. Repair and conflict: RS1, RS5, RS8, SO3, SO4, SO5, RS9, RS7<br>6. Taking the lead: SM4, SM5, SM6, SM7, RD3, RD5, RD6, RD7 |
| Grade 8 | Choices that count | 1. How I decide: RD1, RD2, RD4, RD5, SA5, RD7<br>2. Values and integrity: SA4, SA1, SA2, SA6, RS6, SO7, SA9, SA7<br>3. Stress, focus and rest: SA3, SA8, SM1, SM2, SM3, SM5<br>4. Understanding others: SO1, SO3, SO4, SO6, RS3, SO2, SO8<br>5. Communication and conflict: RS1, RS2, RS5, RS8, SO5<br>6. Making a difference: SM4, SM6, SM7, RS4, RS7, RS9, RD3, RD6 |
| Grade 9 | Finding my footing | 1. A new start: SM5, SM3, SO7, RS8, SA7, SA9<br>2. Stress and coping: SA3, SM1, SM2, SA5, SA8, RD3<br>3. Identity and assets: SA1, SA2, SA4, SA6, RS3<br>4. Relationships that are good for me: RS1, RS2, RS5, RS6, SO3, SO4, SO5<br>5. Norms, media and influence: SO6, SO8, RD1, RD2, RD4, RD5, RD7, RD6<br>6. Goals with others: SM4, SM6, SM7, RS4, RS7, RS9, SO1, SO2 |
| Grade 10 | Respect and relationships | 1. Listening to understand: RS1, SO1, SO4, SA5, SO8<br>2. Hard conversations: RS5, RS8, SM1, SM2, SA3, SM7<br>3. Culture and respect: RS3, SO6, SA1, SA2, SA6, SO2, SA9<br>4. Saying no, setting limits: RS2, RS6, SA4, SO7, RD4, RS9<br>5. Teams that work: RS4, RS7, SM3, SM4, SM5, SM6, SO3, SO5<br>6. Fair to everyone: SA7, SA8, RD1, RD2, RD3, RD5, RD6, RD7 |
| Grade 11 | Purpose and plans | 1. What matters to me: SA9, SA4, SA5, SA1, SA2<br>2. Plans and setbacks: SM4, SM5, SM3, SA7, SA8, SM2, SM1, SA3<br>3. Weighing evidence for choices: RD1, RD2, RD4, RD5, SA6<br>4. Working with others: RS1, RS3, RS4, RS5, SO1, SO2, SO7<br>5. Help, support and pressure: RS8, RS2, RS6, SO3, SO4, SO5, SO8<br>6. Acting on what matters: SM6, SM7, RS7, RS9, SO6, RD3, RD6, RD7 |
| Grade 12 | Leading and leaving | 1. Looking back, looking ahead: SA1, SA2, SA9, SA7, SA5<br>2. Steady under change: SA3, SM1, SM2, SM3, SM5, SA8<br>3. Leading well: RS7, RS4, RS1, SO2, SO7, SM6<br>4. Communities and systems: SO6, SO8, RD6, RD7, SM7, RS9, SA6, RS3<br>5. Hard choices: RD1, RD2, RD3, RD4, RD5, SA4, RS6<br>6. Support after school: RS8, RS2, RS5, SO1, SO3, SO4, SO5, SM4 |

Unit rules:

- **Kindergarten unit 1 assumes nothing.** Its readiness item checks only what a five-year-old arrives with
  (naming a classmate, taking a turn), and no later unit is assumed by it.
- **Cases stay in school, friend, family-chore, sport and online settings.** No invented case names self-harm, a
  diagnosis, dating, sex or a substance. The units that sit next to health, every grade 6 to 12 unit that teaches
  SM2 (coping with stress) or RS6 (saying no to pressure) first (among them "Stress and strong feelings", "Under
  pressure", "Stress and coping", "Saying no, setting limits", "Help, support and pressure" and "Steady under
  change"), name the health unit in the teacher notes and hand those topics to it.
- **Grade 10 unit 4, "Saying no, setting limits"** (retitled from "Healthy boundaries", Cory, 2026-11-21), so the
  title does not read as dating or sexual health.

Placement notes, by sub-skill, where the grade matters most:


- **SA6 (own snap judgements) and SO6 (norms that have been unfair)** start in K to 2 as fairness
  at play ("everyone can join"), and reach unfair rules of the past in grade 5 and later, taught from settled facts
  (see section 5). In grades 3 and 4 SO6 is a rule in a class, club or game that leaves someone out, on invented
  cases; SO8 is how a school's or a town's rules and signs shape what people do. Grade 7 ("Snap judgements") and grade 10 ("Culture and respect") are their main years.
- **SA8 (ability grows)** is taught as "practice and help make you better", never as a promise that belief alone
  raises grades: the evidence for short mindset lessons is mixed (lens, sources; from memory).
- **SO8 (systems shape behaviour)** starts as "why our class has rules" and grows to media and online norms in grade
  6 and to communities and systems in grade 12.
- **RS6 (saying no to pressure)** is taught as a skill on invented cases. The topics where pressure matters most in
  6 to 12 (substances, sex, dating violence) are health's; SEL rehearses the refusal skill and points to the health
  unit by name in the teacher notes.
- **Role play of refusal and standing up (RS6, RS9).** The teacher or a card plays the pressure or the unkind act; no
  student plays a person who pressures or is unkind.
- **SA1 and SA2 (groups you belong to, strengths from your culture)** use an invented character first. A child may share
  or make one up; a family or culture is never asked about by name in a check.
- **RS9 (speaking up for others)** stays inside school life: an upstander in bullying or exclusion, a student who
  gets help for a friend. It is not a cause the course picks (section 5).
- **Transition years** carry the theme: grade 5 "Ready for change", grade 6 "New school, new me", grade 9 "Finding
  my footing", grade 12 "Leading and leaving".

## 4. The deeper review of the design half (Cory, 2026-11-11: "mark this for a deeper review")

Read in full for this review: the criteria paper, pp 1 to 3 and 20 to 35 (design criteria, design updates, implementation
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
| 27 to 29, 31 to 34 | Adult SEL and training: active, modeled, with feedback, building adults' own competencies | none | Gap E |
| 35 | Final rating is the lower of evidence and design | 8, "Unsupported" | Stated; the evidence half is unmet by design |

**Gaps and additions.** Settled 2026-11-16 (Cory, Desk card q-later-sel-eld): all five are added to
ADOPTION-BAR-SUBJECTS part 9 (items 9 to 13).

- **A. Approaches.** Free-standing lessons are the approach the registry most often rates; SEL inside academic
  courses is also counted. Addition: keep free-standing courses (decided), with one line in the bar: each SEL
  unit names one link to that grade's core courses (an ELA discussion routine, a social studies civics row) that
  the teacher may use. This is a lean, not a strand.
- **B. Settings.** Bar item 7 asks for a way to carry the skill beyond the lesson. Addition: make it concrete. Each
  unit has a "carry it out" line for the school day (a cue the teacher uses outside the session) and a family
  activity in the family note. Community is optional.
- **C. Sessions and monitoring.** Addition: the scope and sequence states sessions a year (it will, section 2). For
  monitoring, promise 2 rules out tracking students; a paper fidelity checklist for the teacher (did the session
  run as planned, which part was cut) and the class record sheet of skill checks meet the purpose without
  student data. Behaviour ratings of individual children are not collected; the class sheet marks a step seen on one named day, not the child.
- **D. Equity strategies.** Translation: family notes in English and Spanish; student pages English only for now
  (section 2). Students as agents of change: under the values rule, SEL
  gives student voice in class and school life (class norms, a school improvement the class proposes and carries
  out), and leaves the analysis of causes of inequity to social studies, where it is taught from sources and
  evidence. Working with bias: SA6 is taught as noticing and checking one's own snap judgements on invented cases,
  never as assigning guilt or innocence to a group. This is the "middle line" ADOPTION-BAR-SUBJECTS sets for C12.
- **E. Adult SEL.** Professional learning is none for now (decided 2026-11-11). Addition: each unit's teacher page
  opens with a short "before you teach" note: the skill as an adult uses it, and one thing to model. Not training,
  and not claimed as such.

**Verdict of the review.** The design half is a sound bar for these courses: it is specific (SAFE, practice by
doing, grade sequence, all competencies) and checkable on paper. It is not enough alone in five places (A to E), and the
additions close them within the promises. The evidence half stays unmet and is said so on every course page (bar
item 8): no study has tried these courses. The registry rates a program by the lower of the two halves, so
Curio Class must never call its SEL courses "evidence-based" or use the registry's rating words.

## 5. Sensitive ground: FOUNDATION's promises and the values rule

SEL touches family, identity and mental health, so these rules hold in every SEL unit, read by the fresh
sensitivity agent on every unit plan and day and at the Finish check (docs/pipeline/briefs/sensitivity-read.md,
"When these reads run"; FOUNDATION promise 7, BASELINE rules 5, 6 and 8).

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
   Four sub-skills are about the inside of the child (SA3, SA4, SA7, SA9). Settled (Cory, 2026-11-21): each is checked as a skill on
   an invented case or a plan the student keeps. SA3: name a character's feeling and the clue. SA4: choose the true
   action in a case and say what it costs. SA7: name two steps a character could take and one place to ask for help.
   SA9: a private list the student keeps, checked only for "the steps were followed", never for its content. The course
   never records a student's own answer to SA7 or SA9.
2. **No disclosure is asked for.** Prompts use invented characters and cases, or "a time you choose to share, or
   make one up". No activity asks a child to rank, sort or reveal their identity, family situation or past harm
   (no privilege walks, no "step forward if" games).
3. **Role play stays safe.** Students rehearse a skill in an invented, low-stakes moment. No role play that puts a
   child in a victim's or perpetrator's place, or casts a real classmate (the same rule as social studies). Where a skill needs pressure to rehearse against (saying no,
   speaking up), the teacher or a card plays the pressure; no student plays a person who pressures or is unkind.
4. **SEL is not therapy.** No diagnosis, no clinical words used of a child, no claim that a course treats anxiety or
   depression. Calming routines are breathing, movement and pause, taught as plain body skills with no religious or
   spiritual framing. Each unit's teacher notes carry health's steps for when a child discloses harm or risk
   (docs/courses/health/APPROACH.md, "If a student tells you something": the school's duty to report and the
   counselor, and the home route for a parent teaching one child). Suicide prevention, substances and sexual health belong to health.
5. **Hard facts plain, at the right age.** SO6 "norms that have been unfair" uses settled history the courts have
   ruled on (school segregation struck down in 1954 is the model case) and facts, not opinion; current political
   disputes are not SEL content. Grade sets the case: playground fairness in K to 2, unfair rules of the past from
   grade 5.
6. **Families.** Every family note says what the unit teaches, the words it uses and how to practice at home, in
   English and Spanish. Settled (Cory, 2026-11-21): a school may leave out an SEL unit (as with health's sensitive units),
   the school is told which sub-skills that year then does not teach, a later unit never assumes the left-out one (its readiness item rests on the previous year's row for that sub-skill, or, if that unit was left out too,
   the nearest earlier year that was taught, and checks only the one-step form), and the course page and the unit's
   family note say the course does not claim those sub-skills that year ("Acceptability is local",
   ADOPTION-BAR-SUBJECTS), naming the ids, the same leave-out rule as arts (Cory, 2026-11-21, Desk q-fix-sel-1). Where a later unit uses a card the
   left-out unit made (section 7, "Shared steps"), its first Understanding session teaches the card's one-step form in
   its first ten minutes and claims none of the left-out sub-skills; each band frame lists those bridges.
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
  "builds on" and does not reteach the steps. Where health teaches a shared card first in a year, the SEL unit opens
  with it as retrieval where the school runs health, and teaches it where it does not; each band frame names the
  units and weeks.
- **Shared steps (SEL, health and PE; 2026-11-25, from the K to 2 frame reads).** One set of words, so a child meets
  one card in every course. Calm-down card: "stop, breathe" (the balloon breath) first, then count to five (grade 1),
  then a stretch or asking for a break, chosen by the moment (grade 2); PE's "three slow breaths, count to five" uses
  the same picture. I-statement: "I feel ___ when ___. I need ___." in K to 2 (health kindergarten's words); grade 2
  adds asking "What do you need?" and a fair end; grades 3 to 5 add "because" (I feel, when, because, I need).
  Refusal second push: say it again, move away, tell (health's boundary steps). Goal steps card: my goal and one step;
  then a helper and a check; then a changed step; used by health's goal plans and PE's goal cycles. Talk turn card:
  its two steps open health's listening card. Changes on the health and PE side are the lead's.
- **ELA (data/progressions/ela.csv).** The discussion rows (ek-discussion to e5-discussion, e6-collab-discussion to
  e8-collab-discussion, e9-sl-discussion, e10-sl-seminar, e11-seminar and e12-seminar) carry turn-taking, listening and building on
  others' ideas. SEL's RS1 uses the same norms and words, so a class meets one set of talk rules.
- **Social studies (data/progressions/social-studies.csv).** ssk-rules-why, ssk-talk-together, ss1-group-rules and
  ss1-community-problems overlap SO8, RS1 and RD3 in K and 1. SEL takes the personal side (how I act in a group);
  social studies the civic side (why a community makes rules). The K and 1 SEL frames cite those rows as
  context links.
- **Library and research skills (docs/courses/library/STANDARD.md section 4).** Library places three AASL ids in SEL,
  taught in every band: V.D.1 (trying again when a task gets hard) with SM3, V.D.2 (skill grows with practice and
  help) with SA8, and III.D.2 (the group's learning as one's own job) with RS4. Library research units use these
  sub-skills and do not teach them first (Cory, 2026-11-21, Desk q-fix-library-1).
- These leans are noted here for the frames; the core progressions are not edited.
