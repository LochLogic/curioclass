# English language development: the standard, made usable

**DRAFT, 2026-11-16.**

Written 2026-11-16 as the pre-work owed for English language development (docs/ADOPTION-BAR-SUBJECTS.md, "Before a
scope and sequence in this subject", the ELD row), in the shape of docs/courses/social-studies/STANDARD.md. Core
subjects come first. **Building waits until C11 (English learner supports inside the lesson) is proven in the core
courses** (the owed row): nothing here starts a frame or a scope and sequence. Supports for English learners inside
every other course are C11, not this course (bar part 10).

| Owed row (ADOPTION-BAR-SUBJECTS) | State | Where |
|---|---|---|
| Read the California map in full | Done: all five categories read end to end (2026-11-16); what it adds to bar part 10 is in section 4 | Section 4 |
| Open the WIDA rubric file | Done 2026-11-16: the PRIME 2020 rubric and workbook, requested by Cory, read in full; bar part 10 firmed from it | docs/RUBRIC-ELD.md |
| Build after C11 is proven in core courses | Recorded as the gate, with its test (settled 2026-11-16) | Section 6 |
| Approach page (all ten subjects) | Draft for Cory's yes | docs/courses/eld/APPROACH.md |
| Base text scout, lens | Done | docs/reviews/eld-open-material-2026-11-16.md; docs/agents/lenses/eld.md |
| How ELD leans on the ELA progression | Recorded | Section 5 |

## 1. The standard and its terms

- **Standard.** WIDA English Language Development Standards Framework, 2020 Edition. Five standards: social and
  instructional language (SI) and the language of language arts (LA), mathematics (MA), science (SC) and social
  studies (SS). Four key language uses: narrate, inform, explain, argue. Language Expectations by grade-level
  cluster (K, 1, 2-3, 4-5, 6-8, 9-12; SI uses K-3 and 4-12), each in two modes (interpretive: listening, reading,
  viewing; expressive: speaking, writing, representing). Proficiency level descriptors run from level 1 to level 6.
- **File.** data/standards/wida-2020.txt: 104 official reference codes, one Language Expectation each, ids only.
  The header says which standards, clusters and key language uses exist (WIDA writes expectations only for the most
  prominent key language uses per cluster).
- **Reuse terms, checked at source 2026-11-16.** wida.wisc.edu/policies: personal, non-commercial use only; no
  copying, changing or sharing without written permission from WCER and the University of Wisconsin Board of
  Regents. So: ids and our own words only. No Language Expectation, proficiency level descriptor or WIDA "can do"
  wording appears in any Curio Class page. Internal docs may name WIDA as the source; public pages say "English
  language development standards" with the id.
- **WIDA PRIME 2020** (the alignment review behind the bar): the rubric and portfolio workbook, requested by Cory
  through WIDA's form (Desk card q-later-sel-eld), read in full 2026-11-16 and set out in our own words in
  docs/RUBRIC-ELD.md. It reviews materials against the four framework parts (standards statements, key language
  uses, Language Expectations, proficiency level descriptors) through match, depth and breadth, each criterion
  scored 1 to 4. It judges alignment, not quality. WIDA copyright; the workbook is for local use; a planning
  reference only, and Curio Class claims no PRIME seal or alignment.
- **California** uses its own ELD standards (2012), with three levels (Emerging, Expanding, Bridging). They map only
  roughly to WIDA: Emerging about WIDA 1 and 2, Expanding about 3 and 4, Bridging about 5 and 6 (our reading,
  approximate; no official crosswalk was read). Curio Class plans to WIDA and states the rough match for California
  schools.
- **For the lead (scripts/standards.py is not ours to edit).** The validator does not read wida-2020.txt. Its
  closed pattern for WIDA fully matches only `WIDA.ELD-1` to `WIDA.ELD-5` and `WIDA.Narrate` and the other key
  language uses, as data/modules.csv uses them. A plan row coded `WIDA.ELD-LA.4-5.Argue.Expressive` would fail.
  Before the first ELD scope, standards.py should read this file as an id list (later item; the coarse codes in
  data/modules.csv stay valid). The header's note maps ELD-1 to ELD-5 onto SI, LA, MA, SC and SS.

## 2. Courses, bands and time

- **The catalogue.** data/courses.csv has one ELD track row (`eld-k12`, "WIDA grade clusters"); docs/COURSES-STATUS.md
  counts four band courses: K to 2, 3 to 5, 6 to 8, 9 to 12. WIDA's clusters do not line up with them: K to 2 spans
  clusters K, 1 and half of 2-3; 3 to 5 spans the other half of 2-3 and 4-5. Each band course plans each grade
  against its own cluster's ids, so grade 2 and grade 3 both use 2-3, at different content.
- **Course shape.** Settled 2026-11-16 (Cory, Desk card q-later-sel-eld): four band courses, each with three points
  of entry (by proficiency: levels 1 and 2, 3 and 4, 5 and 6) and a short newcomer strand for students in their first
  months in English. Students move between entry points on the school's own progress checks (bar item 7; California
  map 1.26: several levels and points of entry and exit).
- **Time.** Settled 2026-11-16 (Cory, Desk card q-later-sel-eld): a protected daily period, about 30 minutes in K to
  5 and a 45 minute period in 6 to 12, 160 days. Bar item 8 and California 1.26 both ask for designated time that is
  not ELA time.
- **Placement and exit** use the school's proficiency score (bar part 10, Unsupported). Curio Class gives no
  placement test and keeps no scores.

## 3. How the course is built (for the frames, after the gate)

- **Language through content.** Each unit takes its content from a core unit the same grade is studying that month
  (a science investigation, a social studies inquiry, a math task, an ELA text). The ELD unit teaches the language
  that content asks for: SI every unit, and the one of LA, MA, SC, SS that matches the host unit. Texts are the
  grade's own, with scaffolds, not simplified stand-ins (bar item 2; California 1.7).
- **Key language uses as the spine.** Each unit is built around one or two key language uses (narrate, inform,
  explain, argue) as the cluster's ids allow, in both modes.
- **Forms taught directly.** Words in depth (including cognates where the home language allows), sentence
  structure, word parts, and how a text is put together (bar item 3; California 1.15, 1.23).
- **Structured talk every unit,** with frames and a named routine (bar item 4; California 1.20).
- **Home language as a help** (bar item 6; California 4.1, 4.3a): cognates, contrast between the home language and
  English (where the teacher page has a note for that language), and talk in the home language before writing in
  English.
- **Newcomers and long-term English learners** get named notes in every unit (bar item 5; California 1.23).

## 4. What the California map adds to bar part 10

The map (Program Type 5, specialized ELD, grades 4 to 8; approved 2025-11-06; 91 pages; five categories) was read in
full on 2026-11-16. Our reading, in our own words. Bar items 1 to 8 hold. The map adds:

| Map criterion | What it asks | Proposal |
|---|---|---|
| 1.23 a to j | Teach to each level and each learner type (newcomer, long-term English learner, English learners with disabilities); conversational and academic language; oral language stressed | Add "English learners with disabilities" to item 5's notes |
| 1.26 | A designated period, entry and exit plans, checks built into the course, several entry points, all four modes joined, routines, texts from other subjects, at least two grades | Already items 7 and 8; adopt "all four modes in every unit" as a check |
| 2.9 to 2.12 | New information controlled per lesson; formative checks; collaborative talk guidance | Section plan fields (APPROACH.md) |
| 3.3 | Help telling a language need apart from a disability | Teacher page note per unit; shared with C11's "language gap or content gap" |
| 3.5 | Students judge their own language progress | A student self-check page per unit (kept by the student) |
| 4.1 | Scaffolds withdrawn as proficiency grows; talk about how languages work; comparing languages | Item 3 and C7's withdrawal day |
| 5.7 | Language goals stated for each lesson, with a progression | Section field 2 |
| 5.19 | Family materials in several languages | Family notes in English and Spanish (decided); more languages is a cost call |
| 5.25 | Transfer charts for the common home languages (Spanish, Mandarin, Cantonese, Vietnamese, Tagalog, Arabic, and varieties of English) | Teacher reference per language; start with Spanish |
| 5.27 | Why a skill is hard, with remedies | Unit field 6 (error register) |

**Marks Curio Class loses by choice** (FOUNDATION promise 2, no student data): the map's 2025 guidance on screening
windows, tiered support cycles, progress-monitoring systems and dyslexia monitoring (2.2, 2.10, parts of 3 and 4.5)
expects a data system. Curio Class gives paper checks the teacher keeps and leaves screening and records to the
school.

## 5. The lean on the ELA progression (data/progressions/ela.csv)

ELD does not reteach ELA. It teaches the language a grade's ELA rows ask for, one or two weeks ahead of or
alongside the ELA unit. No row of ela.csv names ELD in its cross_subject column today; this table is the record
(PRODUCTION-PATH, "After the core subjects": noted for later, ELA's progression not edited).

| WIDA part | Leans on these ELA rows (per grade) |
|---|---|
| ELD-LA Narrate | Narrative writing (ek-narrate, e1 to e5 narrative, e6 to e8 narrative-writing, e9 to e12 narrative rows) and the reading-literature rows |
| ELD-LA Inform | Informative writing (ek-inform, e1 to e5 informative, e6 to e8 informative-writing, e9 to e12 informative rows) and reading-informational rows |
| ELD-LA Argue (from 4-5) | Opinion writing in K to 5 (ek-opinion to e5 opinion) and argument writing from grade 6 (argument-writing, e9-w-argument and on) |
| ELD-SI (all four uses) | Speaking and listening: the discussion rows (ek-discussion to e5-discussion, e6 to e8 collab-discussion, e9-sl-discussion, e10 to e12 seminar) and the presenting rows |
| Forms of English (bar item 3) | The language strand: grammar, sentences and word relationships in K to 2, word strategies, forms and conventions in 3 to 5, the grade rows of 6 to 8 (pronouns, phrases and clauses, verbals), and syntax, word strategies and academic words in 9 to 12 |
| Foundational skills (K to 5) | ELD does not teach phonics; newcomers in grades 3 and up who need it use the ELA K to 2 foundational rows, with a note, as the California map's newcomer guidance allows |
| ELD-MA, ELD-SC, ELD-SS | No ELA lean: these use the host unit from the math, science or social studies progression that same month |

When the ELA frames name their units, each ELD unit names the ELA unit it pairs with. ELA's English learner
supports (C11) stay in ELA; ELD adds the protected time and the direct teaching of forms.

## 6. The C11 gate

The owed row says ELD is built after C11 is proven in the core courses. Settled 2026-11-16 (Cory, Desk card
q-later-sel-eld): C11 is proven when it passes, with no fail, in the probe and guard units of at least two core
subjects, one of them ELA. Until then, ELD work is limited to this page, the lens and the scout.

## 7. Left out, and why

- **Placement and proficiency testing:** the school supplies the score (bar, Unsupported).
- **Screening, tiered-support data systems, progress-monitoring records:** FOUNDATION promise 2.
- **Spanish language development for Spanish speakers and dual-language programs:** world languages are shelved
  (2026-11-11).
- **Home language versions of student pages:** a cost and scope call, not assumed. Family notes are in English and
  Spanish.
- **ELD for students with significant cognitive disabilities:** the 2019 open standards for them (CC BY 4.0, search
  only) are noted for later (data/plans/later.csv L54 is the lead's to update).
