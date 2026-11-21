# English language development: the standard, made usable

**DRAFT, 2026-11-16. Read cold 2026-11-20 (docs/reviews/prework-eld-read-2026-11-20.md) and fixed; second-model read fixed 2026-11-21 (docs/reviews/prework-eld-fixes-2026-11-20.md).**

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
| Approach page (all ten subjects) | Approved by Cory 2026-11-21 (Desk q-prework-open-2) | docs/courses/eld/APPROACH.md |
| Base text scout, lens | Done | docs/reviews/eld-open-material-2026-11-16.md; docs/agents/lenses/eld.md |
| How ELD leans on the ELA progression | Recorded | Section 5 |
| Progression gate support | Owed: scripts/progression.py has no ELD entry yet (ownership rule in section 2) | Section 2 |

## 1. The standard and its terms

- **Standard.** WIDA English Language Development Standards Framework, 2020 Edition. Five standards: social and
  instructional language (SI) and the language of language arts (LA), mathematics (MA), science (SC) and social
  studies (SS). Four key language uses: narrate, inform, explain, argue. Language Expectations by grade-level
  cluster (K, 1, 2-3, 4-5, 6-8, 9-12; SI uses K-3 and 4-12), each in two modes (interpretive: listening, reading,
  viewing; expressive: speaking, writing, representing; social and instructional language has no mode segment). Proficiency level descriptors run from level 1 to level 6.
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
- **Validator.** scripts/standards.py reads this file as an id list, so every full id is valid as listed; the
  coarse codes in data/modules.csv remain valid. The header's note maps ELD-1 to ELD-5 onto SI, LA, MA, SC and SS.

## 2. Courses, bands and time

- **The catalogue.** data/courses.csv holds four ELD band rows, `eld-k-2`, `eld-3-5`, `eld-6-8`, `eld-9-12` (Cory,
  2026-11-21): K to 2, 3 to 5, 6 to 8, 9 to 12. WIDA's clusters do not line up with them: K to 2 spans
  clusters K, 1 and half of 2-3; 3 to 5 spans the other half of 2-3 and 4-5. Each band course plans each grade
  against its own cluster's ids, so grade 2 and grade 3 both use 2-3, at different content.
- **Course shape.** Settled 2026-11-16 (Cory, Desk card q-later-sel-eld): four band courses, each with three points
  of entry (by proficiency: levels 1 and 2, 3 and 4, 5 and 6) and a short newcomer strand for students in their first
  months in English. Students move between entry points on the school's own progress checks (bar item 7; California
  map 1.26: several levels and points of entry and exit).
- **Time.** Settled 2026-11-16 (Cory, Desk card q-later-sel-eld): a protected daily period, 30 minutes in K to 5
  and 45 minutes in 6 to 12, 160 days (APPROACH.md, "Pacing"). Bar item 8 and California 1.26 both ask for designated time that is
  not ELA time.
- **Placement and exit** use the school's proficiency score (bar part 10, Unsupported). Curio Class gives no
  placement test and keeps no scores. The course page says that Curio Class's period is the protected core of a
  student's English language development, not a replacement for the school's own program or for more time where a
  state or district asks for it (APPROACH.md, "Pacing").
- **Grain.** Each band course is written as one frame per grade year, 13 frames in all, each of 160 days at the
  band's minutes. A frame takes its host units from that grade's own core courses. A mixed-grade group uses the frame
  of its youngest grade, and the teacher page says so.
- **Ownership** (settled by the expert reader, 2026-11-20, ours, untested). The ELD progression covers all 104 ids in
  data/standards/wida-2020.txt in 56 owned rows: 8 SI rows, one id each, and 48 content rows, each naming the
  Interpretive id and the Expressive id of one standard, cluster and key language use as two ids, so the gate counts
  all 104. No id is excluded. A cluster's owner year is its last grade: K for K, 1 for 1, 3 for 2-3, 5 for 4-5, 8 for
  6-8, 12 for 9-12, and 3 for SI K-3. The other grades of the cluster carry the ids as `~ID`, each with a one-line
  note on how that year differs (a harder text or task, the next key language use added). SI 4-12 is the one
  exception, because students need that language from the day they enter grade 4: it is owned by grade 4 and carried
  as `~` in grades 5 to 12. The gate then needs ELD in scripts/progression.py: the standards file, the anchor, and a
  cluster-to-grade map beside the span map, with the owner rule above.
- **Newcomer strand** (settled by the expert reader, ours, untested): the first 20 days of each band, on the band's
  SI ids and the cluster's Inform. From cluster 2-3 up only ELD-LA has an Inform id; ELD-MA, ELD-SC and ELD-SS have
  Inform in K and 1 only. A student moves to entry points 1 and 2 when the teacher judges the strand's
  look-fors "seen" on two days in a row, or on the school's own check where there is one.

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
- **Newcomers, long-term English learners and English learners with disabilities** get named notes in every unit
  (bar item 5; California 1.23).

## 4. What the California map adds to bar part 10

The map (Program Type 5, specialized ELD, grades 4 to 8; approved 2025-11-06; 91 pages; five categories) was read in
full on 2026-11-16. Our reading, in our own words. The map covers grades 4 to 8; Curio Class uses it in K to 3 and
9 to 12 too, as our own extension. Bar items 1 to 14 hold. The map adds:

| Map criterion | What it asks | Proposal |
|---|---|---|
| 1.23 a to j | Teach to each level and each learner type (newcomer, long-term English learner, English learners with disabilities); conversational and academic language; oral language stressed | Add "English learners with disabilities" to item 5's notes |
| 1.26 | A designated period, entry and exit plans, checks built into the course, several entry points, all four modes joined, routines, texts from other subjects, at least two grades | Already items 7, 8 and 11; adopt "all four domains (listening, speaking, reading, writing) in every unit, across both modes" as a check |
| 2.9 to 2.12 | New information controlled per lesson; formative checks; collaborative talk guidance | Section plan fields (APPROACH.md) |
| 3.3 | Help telling a language need apart from a disability | Teacher page note per unit; shared with C11's "language gap or content gap" |
| 3.5 | Students judge their own language progress | A student self-check page per unit (kept by the student) |
| 4.1 | Scaffolds withdrawn as proficiency grows; talk about how languages work; comparing languages | Item 3 and C7's withdrawal day |
| 5.7 | Language goals stated for each lesson, with a progression | Section field 1 (the section's share of the ids) and section field 6 (each day's goal in student words) |
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
| ELD-LA Narrate | Narrative writing (`ek-narrate`, `e1-narrative` to `e5-narrative`, `e6-narrative-writing` to `e8-narrative-writing`, `e9-w-narrative`, `e10-w-narrative`, `e11-narrative`, `e12-narrative`) and the reading-literature rows |
| ELD-LA Inform | Informative writing (`ek-inform`, `e1-informative` to `e5-informative`, `e6-informative-writing` to `e8-informative-writing`, `e9-w-informative`, `e10-w-informative`, `e11-informative`, `e12-informative`) and the reading-informational rows |
| ELD-LA Argue (from 4-5) | Opinion writing in grades 4 and 5 (`e4-opinion`, `e5-opinion`) and argument writing from grade 6 (`e6-argument-writing` to `e8-argument-writing`, `e9-w-argument`, `e10-w-argument`, `e11-argument`, `e12-argument`) |
| ELD-SI (all four uses) | Speaking and listening: the discussion rows (`ek-discussion` to `e5-discussion`, `e6-collab-discussion` to `e8-collab-discussion`, `e9-sl-discussion`, `e10-sl-seminar`, `e11-seminar`, `e12-seminar`) and the presenting rows. In K to 3, where ELD-LA has no Argue id, opinion writing (`ek-opinion` to `e3-opinion`) leans on ELD-SI K-3 Argue |
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
