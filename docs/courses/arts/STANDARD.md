# Arts: the standard, made usable

Status: DRAFT, for Cory's yes; fixed 2026-11-19 after a cold read (docs/reviews/prework-arts-read-2026-11-19.md).

Written 2026-11-16 as pre-work for the arts (visual arts, music, theater, dance, media arts; 20 courses, five
disciplines by four bands). It answers the arts row of "Before a scope and sequence in this subject" in
docs/ADOPTION-BAR-SUBJECTS.md. The bar is the arts part of that page. The lens is docs/agents/lenses/arts.md. The
approach page is docs/courses/arts/APPROACH.md (draft).

| Piece | State | Where |
|---|---|---|
| Which standard and edition | Done | Section 1 |
| Read the reuse terms | Done 2026-11-16, read at source | Section 2 |
| A written rule placing each grade's standards, and the three high school levels, in a band year | Done as a rule; high school levels, the music strand and pacing decided (Cory 2026-11-16, Desk card q-later-arts-health-pe); id count table added 2026-11-19 | Section 3 |
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
- scripts/standards.py checks NCAS codes by a closed pattern on discipline, process and anchor, and accepts the
  strand letter and the grade or level (read 2026-11-19). It does not check that an id exists in the file.
  Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-arts-1): the standards gate that checks a plan's ids
  against the file's lines is a worker's job, owed; until it exists, each scope and sequence states its id count
  against the table in section 3.2 and a reader spot-checks ten.
- Music is loaded for pre-kindergarten to grade 8 general music only. The 63 ids of the high school composition
  and theory strand load by hand when the high school music frame is written (section 3.3).

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
- A plan names a performance standard by id and states its action in one line of our own words. It never quotes
  the performance standards. The eleven anchors may be quoted in their real wording. Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-arts-1):
  the one-line words file for the 1,114 taught ids and the 63 strand ids (id, tab, at most 14 words of what the
  student does, written by one agent and read by a second) waits on Cory, who decides it because the repo is
  public. Until it is written, a plan cites the id and writes the action in its own one line.

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
  and assessed in that year. The unit of count is the lettered id, one statement (`DA:Cr1.1.2a`); the table in
  3.2 gives each year's count. A year may revisit the year before's ids as practice that returns, but it claims
  only its own grade.
- Pre-kindergarten ids are not taught. A kindergarten unit may use one as a readiness reference.
- Mixed-grade classes are common in the arts. A school that teaches a band as one mixed class runs the three
  years in turn. Each year still claims only its grade's ids, so a student's record shows which grade's standards
  they met. The scope and sequence says this once, on its first page.

### 3.2 Grades 9 to 12: levels, not grades (Cory 2026-11-16, Desk card q-later-arts-health-pe)

The high school standards come in three levels, defined by what a student has done, not by grade (NAfME's
appendix to the music standards, read 2026-11-16, our words): Proficient is what most students reach in one high
school arts course of about 120 hours beyond good pre-kindergarten to grade 8 learning; Accomplished takes a
further sequence of courses; Advanced goes well past Accomplished, at honors or first-year college depth. The
evidence for the structure below is docs/reviews/arts-hs-music-and-levels-2026-11-16.md: no peer-reviewed study
compares sequenced and survey high school arts courses, so the structure follows the national descriptors and the
state frameworks that turn them into yearlong courses.

| Year of the 9 to 12 band | Level taught | Ids |
|---|---|---|
| Level 1 | Proficient | `.Ia` |
| Level 2 | Accomplished | `.IIa` |
| Level 3 | Advanced, at honors depth | `.IIIa` |
| Level 4 (optional) | Advanced, deepened: a portfolio or production year the student leads | `.IIIa`, assessed again on new, self-directed work |

- The 9 to 12 band is one course per discipline, as every other band is; its years are levels. A level is a
  full 160-day year, which is about the 120 hours the descriptor names.
- Entry: a student new to a discipline starts at Level 1, whatever their grade. The scope and sequence names the
  level, never a grade. Level 1's first unit assumes no earlier arts learning.
- Each level requires the one before, or a placement showing: the student shows work scored against the previous
  level's end-of-course assessment, and starts at the next level if it meets it.
- Advanced is claimed by assessed work, not by finishing Level 3. A student who ends Level 3 at "partly" has
  Level 4 to reach it.
- One level is a complete course and is enough for Proficient. The bar does not ask a school to offer all four.
- Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-arts-1): a short path for high school levels waits on
  Cory. Proposal: each level's scope and sequence marks an 80-day path (a semester or a rotation) that keeps every
  unit and every id by merging the marked days. Level 1 opens with a bridge unit of at most 12 days that teaches the
  discipline's grade 8 ids; Levels 2 and 3 open with a review unit of at most 6 days that doubles as placement.
  Bridge and review days count as inside the standards for the bar's 10 percent limit and are listed as bridge or
  review days in the frame. The numbers 12 and 6 are ours, untested.

### Ids owned by each course-year (counted from the id file, 2026-11-19; pre-kindergarten excluded)

| Discipline | K to 2 (K, 1, 2) | 3 to 5 | 6 to 8 | 9 to 12, per level (`.Ia`, `.IIa`, `.IIIa`; Level 4 repeats `.IIIa`) |
|---|---|---|---|---|
| Visual arts (VA) | 15 + 15 + 15 = 45 | 45 | 45 | 15 |
| Music (MU) | 19 + 20 + 20 = 59 | 63 | 63 | 21 each, strand `.C`, 63 in all, not in the file |
| Theater (TH) | 17 + 24 + 24 = 65 | 72 | 72 | 24 |
| Dance (DA) | 21 + 21 + 21 = 63 | 63 | 63 | 21 |
| Media arts (MA) | 18 + 18 + 18 = 54 | 54 | 54 | 18 |

An id is one lettered statement (`DA:Cr1.1.2a`). A year's scope and sequence claims every id of its grade in its
discipline, counted in this table. The file holds 1,202 ids: 1,114 taught (K to 8 and the high school levels) and 88
pre-kindergarten, not taught. Totals of taught ids: visual arts 180, music 185, theater 281, dance 252, media arts
216. The header's "per grade" figures are unlettered standards and are not the count. Music and theater
kindergarten are uneven (music K 19, grades 1 and 2 20, grades 3 to 8 21; theater K 17, grade 1 on 24), so no
year is counted by an even spread. High school music is one of the 20 courses, not an extra one; its 63 ids are
not in the file.

### 3.3 Music in high school: composition and theory (Cory 2026-11-16, Desk card q-later-arts-health-pe)

Music 9 to 12 is a full composition and theory course on the national composition and theory strand, not a stub
(settled 2026-11-16, Cory, Desk card q-later-followups-1).
The reasons and sources are in docs/reviews/arts-hs-music-and-levels-2026-11-16.md.

- The strand starts at Proficient (no Novice or Intermediate levels), so Level 1 follows grade 8 general music
  directly. It runs to Advanced in the same three levels as 3.2.
- It needs no instrument: work is shared by notation, performance or technology, and performances may be live
  or recorded. Days use the voice (singing, sight-singing), body and found percussion, a free keyboard on any
  device or a Curio Class tool, and the student's own instrument when they have one.
- Ensemble, harmonizing instrument and music technology ids are not claimed. Those strands assume instruments,
  a group or production tools and a teacher who hears technique in the room.
- An ensemble companion page sits inside the course (no days, no ids, not a counted course): how to find a
  school or community ensemble, a practice log and self-check, how an assignment can be written for the
  student's own instrument or section, and a plain note that ensemble standards are met and assessed by that
  ensemble.
- Ids: 21 per level, 63 in all, format `MU:Cr1.1.C.Ia` (the strand letter `C` before the level).
  scripts/standards.py accepts the strand letter (read 2026-11-19). They load into the id file by hand, ids only,
  when the high school music frame is written.

### 3.4 Pacing (settled 2026-11-16)

The bar fails a plan that needs a daily arts period (criterion 9). A K to 8 arts year is 64 course days (two
sessions a week over 32 weeks, docs/courses/CALENDAR.md). Session length is 40 minutes (ours, untested); every
section plan states the set-up and clean-up minutes inside it. A school that meets once a week keeps every unit and
every standard on 32 days by merging the days each unit marks. High school levels are 160 course days (3.2). The
160 in docs/GLOSSARY.md is the school year, not a course's days, so nothing there changes.

On the 32-session path each unit keeps four things, in this order and no fewer: the demonstration with a step card,
one making or rehearsal day with a critique, the showing (the check), and one respond day. Fluency days fold into
the openers. The frame marks which days merge.

**The ordinary room (bar criterion 14).** A class of thirty needs a clear floor or tables, paper, pencils, found
material and the voice; nothing is bought, and every unit lists a cheap stand-in. A tool day has a printed version
that does the same job. The teacher needs no training in the discipline: each unit's teacher page says what to look
and listen for, in plain words. One child at home is the second room: the parent is the audience and the critique
partner, a showing is to the family or a recorded take, and a duet or group piece has a solo or doubled version.

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

- What a school may leave out. Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-arts-1): a school or
  family may leave out a unit or a work for its community's reasons (for example, a unit that uses dance, masks or
  play-acting); each course page states which units stand alone. This waits on Cory.
- Pre-kindergarten ids: no pre-kindergarten courses.
- The high school ensemble, harmonizing instrument and music technology strands (3.3).
- Enduring understandings, essential questions, model cornerstone assessments and the glossary: permission
  needed to reproduce (section 2); we write our own.
- State arts standards: one national set is the reference. A state's own grade placement may differ; the course
  page says the national set is ours to follow.

## 6. Leans on the core progressions

These are places where an arts unit leans on, or gives to, a core course. Each is checked against the core
progression when the arts frame is written; the arts unit does not reteach the core skill.

- Music and math: beat, note values and measures lean on fractions (grade 3 and 4 math). A music unit on note
  values is placed after the math week that teaches fractions (data/plans/calendar.csv), or uses beat counts
  only.
- Visual arts and math: shape, symmetry, scale and proportion lean on geometry and ratio (grades 4 to 7).
- Theater and ELA: script reading and character lean on the reading literature standards; performing leans on the
  speaking and listening standards. Responding in every art uses ELA's claim-and-evidence writing.
- Dance and physical education: locomotor and nonlocomotor movement lean on the PE motor skills (SHAPE.S1). Dance
  in arts is the art: making, performing, responding to and connecting dance. Dance in physical education is
  movement skill, fitness and teamwork. Arts dance units do not teach the motor skill; PE dance units do not teach
  choreography, performing for an audience or response to dance. Each pair of units names the other in its
  connections line.
- Media arts and computer science: media arts teaches the one idea of privacy or copyright its unit needs, in a
  short step of the unit, and notes the computer science unit that goes deeper; it does not wait for it.
- All arts and social studies: works are taught with their time and place (bar criterion 7), using social
  studies' sourcing habits.
