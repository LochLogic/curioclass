# Arts: the standard, made usable

Written 2026-11-16 as pre-work for the arts (visual arts, music, theater, dance, media arts; 20 courses, five
disciplines by four bands). It answers the arts row of "Before a scope and sequence in this subject" in
docs/ADOPTION-BAR-SUBJECTS.md. The bar is the arts part of that page. The lens is docs/agents/lenses/arts.md. The
approach page is docs/courses/arts/APPROACH.md (draft).

| Piece | State | Where |
|---|---|---|
| Which standard and edition | Done | Section 1 |
| Read the reuse terms | Done 2026-11-16, read at source | Section 2 |
| A written rule placing each grade's standards, and the three high school levels, in a band year | Done as a rule; the high school music strand and the pacing wait on Cory | Section 3 |
| Watch the national revision twice a year | Set up: dates, places and what to do | Section 4 |
| What is left out, and why | Done | Section 5 |
| Leans on the core progressions | Done | Section 6 |

## 1. The standard

- National Core Arts Standards, 2014 (National Coalition for Core Arts Standards), the performance standards.
- Loaded in data/standards/ncas-performance-standards.txt as ids only, no wording: 1,202 ids across the five
  disciplines (visual arts 195, music 202, theater 298, dance 273, media arts 234), from the 2021-11 "at a glance"
  handouts, fetched 2026-10-27. Format `DIS:<process><anchor>.<standard>.<grade><letter>`, for example
  `DA:Cr1.1.2a`. High school levels are `.Ia`, `.IIa`, `.IIIa` (media arts cells with one statement carry no
  letter, as `MA:Re9.1.I`).
- Eleven anchor standards in four artistic processes: creating (Cr1 to Cr3), performing, presenting or producing
  (Pr4 to Pr6), responding (Re7 to Re9), connecting (Cn10, Cn11). The bar asks for all four processes in every
  course (criterion 1).
- scripts/standards.py checks NCAS codes by a closed pattern on discipline, process and anchor. It does not check
  the grade or the letter, so a wrong grade passes the script. A reader checks grade and letter against the file.
- Music is loaded for pre-kindergarten to grade 8 general music only. The high school music strands are not loaded
  (section 3.3).

## 2. Reuse terms (read at source, 2026-11-16)

Read on the coalition's own copyright guidelines (nationalartsstandards.org, "NCAS Copyright Guidelines", the
2025 posting of a document dated 2016). Research notes, not legal advice.

- The notice: the standards are copyright 2014 by the coalition, rights administered by Young Audiences, Inc., all
  rights reserved.
- Free and unlimited use covers only the eleven anchor standards and the blank framework matrix.
- Everything else (the performance standards, enduring understandings, essential questions, model cornerstone
  assessments, glossary) needs permission to reproduce, with set exceptions: teachers may copy the standards as
  shown on the site for their own teaching, and anyone may quote up to 250 words with the citation.
- Paraphrase is allowed in general, with the citation.
- What Curio Class does: the file and every plan carry ids and our own words only. No performance standard,
  enduring understanding or essential question is copied into a page, a day or a tool. Our own essential
  questions are written fresh. A page that names the standards gives the citation line in the notice's form.
- The model cornerstone assessments are not adapted. Our end-of-unit assessments are our own.

## 3. The band-year rule

Our arts courses are bands: one course per discipline per band (visual arts, grades K to 2, and so on). The
standards are written grade by grade to grade 8, then in three high school levels. The rule below places them.

### 3.1 Kindergarten to grade 8: the grade's own standards in the grade's own year

| Band | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| K to 2 | Kindergarten ids (`.Ka` and so on) | Grade 1 ids | Grade 2 ids |
| 3 to 5 | Grade 3 ids | Grade 4 ids | Grade 5 ids |
| 6 to 8 | Grade 6 ids | Grade 7 ids | Grade 8 ids |

- Each year's scope and sequence lists every id of its grade in the discipline, unit by unit. Each id is taught
  and assessed in that year. A year may revisit the year before's ids as practice that returns, but it claims
  only its own grade.
- Pre-kindergarten ids are not taught. A kindergarten unit may use one as a readiness reference.
- Mixed-grade classes are common in the arts. A school that teaches a band as one mixed class runs the three
  years in turn. Each year still claims only its grade's ids, so a student's record shows which grade's standards
  they met. The scope and sequence says this once, on its first page.

### 3.2 Grades 9 to 12: levels, not grades

The high school standards come in three levels. From NAfME's appendix to the music standards (read 2026-11-16, our
words): Proficient is what most students reach in one high school arts course of about 120 hours beyond good
pre-kindergarten to grade 8 learning; Accomplished takes a further sequence of courses; Advanced goes well past
Accomplished, at honors or first-year college depth. The coalition's own aim (search only, not read at source) is
that every student reaches at least Proficient in one arts discipline.

| Year of the 9 to 12 band | Level taught | Ids |
|---|---|---|
| Level 1 | Proficient | `.Ia` |
| Level 2 | Accomplished | `.IIa` |
| Level 3 | Advanced | `.IIIa` |
| Level 4 (optional) | Advanced, deepened: a portfolio or production year | `.IIIa`, assessed again on new work |

- A level is one course of 160 days, which is about the 120 hours the descriptor names.
- Levels are tied to what a student has done, not to their grade. A grade 11 student new to dance starts at
  level 1. The scope and sequence names the level, never a grade.
- One level is enough for Proficient. The bar does not ask a school to offer all four.

### 3.3 Music in high school (waits on Cory)

The general music strand stops at grade 8. The high school music standards come in strands that are not loaded:
traditional and emerging ensembles, harmonizing instruments, composition and theory, and technology. The
ensemble and harmonizing strands add two levels below Proficient (Novice, about grade 5, and Intermediate, about
grade 8). A high school music course must pick a strand before its scope and sequence. The pick is a scope call,
so it is a question for Cory. Recommended: composition and theory, because a class can do it with voices, simple
instruments and free notation on any device, and it needs no ensemble. Once picked, its ids are loaded by hand in
the same format (ids only), after checking the strand's own code letters at source.

### 3.4 Pacing (waits on Cory)

The bar fails a plan that needs a daily arts period (criterion 9). Arts in kindergarten to grade 8 often meet once
or twice a week, sometimes in rotations. Recommended: a K to 8 arts year is planned as 64 course days (two
sessions a week for 32 weeks). Every unit marks which of its days merge for a school that meets once a week, so
that school keeps every unit and every standard on 32 days. High school levels are full 160-day courses (3.2).
This changes the arts course's day count from the 160 in docs/GLOSSARY.md, so it is Cory's call.

## 4. Watching the national revision

The coalition announced a review in February 2025. Its March 2026 update (read 2026-11-16) reports a field survey
with 3,490 replies, a wish for refinement rather than a rewrite, and five aims: arts learning for all, more
concise wording, student voice and choice, technology and artificial intelligence, and readiness for life after
school. No draft date is given.

- Look twice a year, in the first week of May and the first week of November: the coalition's site (the review
  resources page and news) and its contact address for updates.
- Record each look here in one line: date, what changed, and whether any loaded id or this rule is affected.
- If revised standards are published: do not reload until the reuse terms are read again and Cory says so. Units
  already planned keep their 2014 ids, named as 2014.

| Date | What was seen | Effect |
|---|---|---|
| 2026-11-16 | March 2026 update: refinement, five aims, no draft or date | None |

## 5. Left out, and why

- Pre-kindergarten ids: no pre-kindergarten courses.
- The high school music strands, until Cory picks one (3.3).
- Enduring understandings, essential questions, model cornerstone assessments and the glossary: permission
  needed to reproduce (section 2); we write our own.
- State arts standards: one national set is the reference. A state's own grade placement may differ; the course
  page says the national set is ours to follow.

## 6. Leans on the core progressions

These are places where an arts unit leans on, or gives to, a core course. Each is checked against the core
progression when the arts frame is written; the arts unit does not reteach the core skill.

- Music and math: beat, note values and measures lean on fractions (grade 3 and 4 math). A music unit on note
  values comes after the fraction units in the same grade, or teaches note values by beat count only.
- Visual arts and math: shape, symmetry, scale and proportion lean on geometry and ratio (grades 4 to 7).
- Theater and ELA: script reading and character lean on the reading literature standards; performing leans on the
  speaking and listening standards. Responding in every art uses ELA's claim-and-evidence writing.
- Dance and physical education: locomotor and nonlocomotor movement lean on the PE motor skills (SHAPE.S1). Dance
  units and PE dance units name each other and do not double-teach.
- Media arts and computer science: digital making leans on the computer science course; privacy and copyright on
  its society strand.
- All arts and social studies: works are taught with their time and place (bar criterion 7), using social
  studies' sourcing habits.
