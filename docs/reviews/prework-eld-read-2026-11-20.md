# English language development pre-work: cold read, 2026-11-20

Read as the curriculum expert (docs/agents/EXPERT.md) with the ELD lens (docs/agents/lenses/eld.md), as stage 1 of
docs/COURSE-RUN.md. I did not write these drafts. Nothing was edited but this file. Confidence is Firm, Likely or
Judgment call on each finding. Anything that rests on my memory is marked "from memory". The standard's id list was
checked against the framework PDF itself (see "What I counted").

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/eld.md; docs/courses/eld/STANDARD.md and APPROACH.md;
data/standards/wida-2020.txt (all 104 ids); docs/ADOPTION-BAR-SUBJECTS.md part 10 (items 1 to 14, fails-if,
unsupported, standards) and the ELD row of "Before a scope and sequence in this subject"; docs/reviews/eld-open-material-2026-11-16.md;
docs/reviews/prework-sel-read-2026-11-19.md (format); docs/courses/health/APPROACH.md and docs/courses/sel/APPROACH.md
(finished pages, for comparison); docs/courses/UNIT-PLAN.md (the field lists, lines 145 to 280); the ELD row of
data/courses.csv (line 43 only); the ELD rows of docs/COURSES-STATUS.md; scripts/progression.py lines 45 to 114
(STD_FILES, ANCHOR, SPAN, code_grades); scripts/standards.py lines 94 to 141 (for the stale-note check); one-line
id checks in data/progressions/ela.csv; docs/pipeline/briefs/sensitivity-read.md.

Outside sources opened:
- WIDA English Language Development Standards Framework, 2020 Edition, PDF, 392 pages, fetched 2026-11-20:
  https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf (Appendix C, PDF pages
  293 to 392, for every Language Expectation code; Appendix C pp 288 to 290 for the key language use tables).
- California Department of Education, Instructional Services frequently asked questions:
  https://www.cde.ca.gov/SP/ML/isfaqs.asp (time for designated ELD; read via page summary).
- Search results only, pages not opened by me, so the figures are "per search summary": Arizona structured English
  immersion model guide https://azed.gov/sites/default/files/2023/05/SEI%20Model%20Implementation%20Guide%20UPDATED%20v.9.13.24.pdf ;
  Rhode Island Department of Education, Brief 3, Dedicated ELD https://ride.ri.gov/sites/g/files/xkgbur806/files/2025-06/Brief%203%20-%20Dedicated%20ELD.pdf ;
  Montana Office of Public Instruction, recommended minutes per WIDA level (the address returned 404 when I fetched it, so unverified).
- Not re-opened: the California criteria map, the WIDA PRIME workbook, the National Academies report, the English
  Learner Success Forum guidelines, EL Education. Anything I say about them is taken from the repo pages.

## Verdict

The standard file is sound as a list: all 104 ids match the framework's own Appendix C one for one, are unique, the
counts agree everywhere they are stated, and the wording is our own. The approach page is not yet usable: it fills
about half the unit and section fields, puts the "two rooms" field to a different use from every finished page, has no
sensitive-ground section, no tool rule, no pacing, no sources and no way for a writer to say which grade owns an id,
so scripts/progression.py cannot be fed. The one change that matters most is a settled ownership and grain rule
(finding 1), then the full field block (finding 3).

## What I counted (so nobody has to again)

| Check | Result |
|---|---|
| Ids in wida-2020.txt | 104 data lines, no duplicates |
| Against the framework PDF, Appendix C (my extraction, whitespace normalised, pages 293 to 392) | 104 of 104 match, none in the PDF missing from the file, none in the file missing from the PDF |
| By standard | SI 8, LA 30, MA 20, SC 24, SS 22 (matches the header's 8 plus 96) |
| Non-SI ids | 48 cluster by key language use pairs, each in both modes: 48 Interpretive, 48 Expressive |
| By cluster, non-SI | K 12, 1 14, 2-3 16, 4-5 18, 6-8 18, 9-12 18 |
| SI ids | 4 key language uses by 2 clusters (K-3, 4-12), no mode segment; matches the framework |
| Key language use shape in the file | LA: K and 1 and 2-3 have Narrate and Inform; Argue first appears at 4-5. MA: Inform at K and 1, Explain and Argue from 2-3. SC: Inform and Explain at K and 1, Explain and Argue from 2-3. SS: Inform at K, Inform and Argue at 1, Explain and Argue from 2-3 |
| Counts as stated | STANDARD.md "104 official reference codes", "five standards", "four key language uses", "six clusters" all agree with the file and the header |
| ELA leans (STANDARD section 5) | 31 row names or families checked by one-line grep; all exist in data/progressions/ela.csv (ek-narrate, ek-inform, ek-opinion, ek-discussion; e1 to e5 narrative, informative, opinion, discussion; e6 to e8 narrative-writing, informative-writing, argument-writing, collab-discussion; e9-w-narrative, e9-w-informative, e9-w-argument, e9-sl-discussion; e10 to e12 narrative, informative, argument and seminar rows). The reading-literature, reading-informational, presenting and language rows are named by family, not id, so those are not checked |
| Validator | scripts/standards.py reads wida-2020.txt as an id list (LISTED, line 97), so a full id such as WIDA.ELD-LA.4-5.Argue.Expressive passes today |
| Progression gate | scripts/progression.py has no ELD entry in STD_FILES, ANCHOR or code_grades |
| Dose as stated | STANDARD section 2: about 30 minutes K to 5 and 45 minutes 6 to 12, 160 days; that is about 80 hours a year (K to 5) and 120 hours (6 to 12) |

## Findings, most serious first

### 1. No ownership rule, and the band courses cut across the framework's clusters

- **Where:** STANDARD.md section 2 ("each band course plans each grade against its own cluster's ids, so grade 2 and
  grade 3 both use 2-3"); section 5; docs/PRODUCTION-PATH.md layer 4 rule (every standard owned by exactly one grade
  or excluded with a reason); scripts/progression.py (STD_FILES, ANCHOR, SPAN, code_grades).
- **What is wrong:** The gate wants each id owned once. The page says two grades use the same cluster ids and never says
  which grade owns them, which grade carries them as `~`, or whether an id is excluded. The clusters do not line up with
  the bands (2-3 straddles K to 2 and 3 to 5; SI K-3 straddles the same two bands; SI 4-12 spans three bands), so a writer
  has no obvious owner for 2-3 (grade 2 or grade 3) or for the SI ids. Two writers will choose differently. Also, the
  file has each non-SI id twice (a mode each); the page does not say whether a progression row carries one id or the pair,
  and the gate counts ids.
- **Cost:** The ELD progression cannot be written, or is written two ways. Every frame after it inherits the gap.
- **Fix (add to STANDARD.md section 2, ours, untested):**

> **Ownership.** The ELD progression has one owned row per id in data/standards/wida-2020.txt, 104 rows in all. A cluster's
> owner year is its last grade: K for K, 1 for 1, 3 for 2-3, 5 for 4-5, 8 for 6-8, 12 for 9-12. The other grades of the
> cluster carry the id as `~ID`, each with a one-line note on how that year differs (a harder text or task, the next
> key language use added). The two social and instructional ranges are the exception: SI K-3 is owned by grade 3 and SI
> 4-12 by grade 4, because students need social and instructional language from the day they enter; grades 5 to 12 carry
> SI 4-12 as `~`. Grade 3 uses SI K-3 and the 2-3 cluster; grade 4 uses SI 4-12 and the 4-5 cluster. An id owned in one
> band course may be carried in another; the progression is one subject across K to 12. A row names the Interpretive id
> and the Expressive id as two ids in the standard column, so the gate counts both. No id is excluded.

  The gate would need (not mine to edit): `'eld': ['wida-2020.txt']` in STD_FILES; `'eld': 'wida-2020.txt'` in ANCHOR;
a code_grades branch for `WIDA.ELD-XX.<cluster>.` mapping the clusters K, 1, 2-3, 4-5, 6-8, 9-12 and SI K-3 and 4-12 to
their grades, with the owner rule above (a new dictionary beside SPAN, as the health branch does). Confidence: Firm that
a rule is missing; the owner choice is a Judgment call (settled below).

### 2. The course grain is not stated: four band courses of 160 days, or 13 grade years

- **Where:** STANDARD.md section 2 ("four band courses ... 160 days") and section 3 ("each unit takes its content from a
  core unit the same grade is studying that month"); data/courses.csv `eld-k12` (one row); docs/COURSES-STATUS.md (four).
- **What is wrong:** Section 3 ties each unit to a host core unit "the same grade is studying that month". A band course
  of K to 2 spans three host grades with three different core units each month. The page does not say whether a band
  course is one 160 day year repeated three times with a grade chosen by the teacher, or three grade-year frames. Entry
  points are by proficiency, not grade, so a student in grade 4 and a student in grade 5 may share a room; the host unit
  then differs. The catalogue still has one row where the status page has four, and unlike SEL no resolution is written.
- **Cost:** The frame writer cannot decide how many frames, units or host pairings to write. Dose is also unclear: 160
  days is per year, but a band is three or four years.
- **Fix (add to STANDARD.md section 2; the grain is a Question for Cory, recommended pick shown):**

> **Grain.** Each band course is written as one frame per grade year, 13 frames in all, each of 160 days at the band's
> minutes. A frame takes its host units from that grade's own core courses. A mixed-grade group uses the frame of its
> youngest grade, and the teacher page says so. The catalogue (data/courses.csv) replaces `eld-k12` with four band rows,
> `eld-k-2`, `eld-3-5`, `eld-6-8`, `eld-9-12`.

  Confidence: Firm that the grain is unstated; Likely that per-grade frames are right (they are the only form where the
host pairing is unambiguous).

### 3. APPROACH.md fills about half the fields, and one field means something else

Compared with docs/courses/UNIT-PLAN.md (unit fields 2 to 10; section fields 1 to 11) and the health and SEL pages:

| Slot | Verdict | Note |
|---|---|---|
| Unit header | Filled | days by kind, minutes, host unit |
| Unit 2 standards, what is carried | Part | ids, key language use, forms; the day the frame is withdrawn is in section field 5, not named at unit level |
| Unit 3 where it sits | Part | host unit and ELA pairing given; builds on, leads to, comes back are missing |
| Unit 4 readiness | Filled | |
| Unit 5 end-of-unit assessment | Filled | talk plus writing, two samples per level, how a student moves up |
| Unit 6 error register | Filled | with transfer as a reason |
| Unit 7 response allocation | Missing | how groups come from the sheet; a unit mixes three entry points, so groups by entry point and by form need a cap |
| Unit 8 tools and supplies | Missing | and no statement of what a tool may or may not do (finding 6) |
| Unit 9 family note | Missing | the bar and the Desk say family notes are in English and Spanish; no field |
| Unit 10 sources | Missing | no sources table, read-status, logic-model line (finding 8) |
| Section 1 | Part | before-you-teach given; the sensitive topics the section touches are not |
| Section 2 where it sits | Missing | |
| Section 3 checks | Filled | |
| Section 4 expected errors | Missing | a wrong example beside a right one, the day it is shown, what to do if many made it |
| Section 5 what is carried | Filled | model sentence, holder, withdrawal day |
| Section 6, 7 | Filled | |
| Section 8 practice that returns | Missing | bar item 13 (earlier forms return) has no field |
| Section 9 supports | Filled | the strongest part; add the leave-out for a family language (finding 4) |
| **Section 10 two rooms** | **Wrong meaning** | the page says "one teacher with a mixed group, or a pull-out group". UNIT-PLAN field 10 is a parent teaching one child at the table, and one projector. A home parent and a one-screen room are not covered |
| Section 11 not in this section | Missing | |
| Pacing | Missing from the page | in STANDARD section 2 only; health and PE state it on the approach page |

- **Cost:** C7, C10, C11, C14, C15 and C16 lose a slot each, and the home-use case (the Curio Class promise to a parent
  teaching alone) has no ELD answer.
- **Fix (replace "What ELD adds to the unit and section plan fields" with a full block; the lines that are right stay;
  add, in these words, ours, untested):**

> **Unit field 3:** builds on (the same key language use one cluster earlier, handoff strong or weak); leads to; comes
> back; the host unit and the ELA pairing as now.
> **Unit field 7:** the talk task and the writing task are judged by the teacher against the look-fors, so nothing is
> marked by hands up. Respond-day groups come from the sheet's "not yet" cells by form and by entry point, at most four
> groups; the others rehearse in pairs from the frame. Marking time is stated as minutes.
> **Unit field 8:** word cards, frames and the model text by title and record; no product or program names. A tool may
> not record a student's voice or writing, collect a name, or score a child (finding 6).
> **Unit field 9:** the family note, in English and Spanish: the language goal in plain words, the frame the class uses,
> and one thing to try at home in any language the family chooses.
> **Unit field 10:** a sources table with what was read and how much, what is from memory, no claim of effect, and a line
> pointing to the course logic model (C16).
> **Section field 2:** what comes just before and just after in the unit; the readiness items it uses.
> **Section field 4:** each expected error as a wrong sentence beside a right one, the day it is shown, and the five to
> ten minute response if many made it. Errors are never marked as faults of the home language; transfer is named as a
> reason.
> **Section field 8:** one earlier form, named, used again for three minutes on new content.
> **Section field 10:** a parent teaching one child at the table: the model sentence read together, the child says it back,
> the adult writes it, talk in the home language first; one projector: the model text on screen, the frame on the board,
> the talk routine in pairs. The pull-out versus mixed group note moves to unit field 8 as a setting.
> **Section field 11:** what is left to the host course (the content test), to ELA, or to the school's placement.
> **Pacing:** as STANDARD section 2, and finding 5.

  Confidence: Firm.

### 4. Sensitive ground is not named, and the readers do not exist for most of the home languages

- **Where:** APPROACH.md (no section); STANDARD.md section 7 and the lens (only "a home language treated as a problem" and
  "an accent corrected as an error of meaning" appear, as reviewer errors); docs/pipeline/briefs/sensitivity-read.md
  (kinds: sensitivity, safety, answer-key, text, rights, spanish).
- **What is wrong:** ELD students are children of migration, and some are refugees. The pages name nothing a unit may not do.
  Nothing says: no task asks about immigration status, how or why the family came, the home country, a parent's job, or
  the language spoken at home as a requirement; no text or writing prompt uses a migration story as an invited
  confession; a student is never asked to translate for the class or for a family; a home language is a help, never
  a ranking; an accent or dialect of English or the home language is not corrected as wrong meaning. The APPROACH asks for
  "notes for the common home languages" and STANDARD section 4 adds transfer charts for Spanish, Mandarin, Cantonese,
  Vietnamese, Tagalog and Arabic (California map 5.25), but the brief has a read only for Spanish. A note on how
  Mandarin or Arabic does the same thing is a factual claim about a language that nobody here can check.
- **Cost:** A first unit can ask a newcomer to "tell about your journey", or state a wrong rule about a home language. The
  first is harm; the second is an error a family will see.
- **Fix (add a "Sensitive ground" section to APPROACH.md, ours, untested):**

> **Sensitive ground.** A task never asks a student about immigration status, how the family came, what happened on the way,
> a parent's work, or whether the family speaks English at home. A student is never asked to translate for the class, a
> family or the teacher. Prompts about family, home and "where you are from" are offered as one of several, and a student
> may write about an invented character or a place they choose. Texts about migration, war, loss or the student's own
> group are read as a sensitivity read before a unit uses them. A home language is a resource, never a ranking; an accent or
> a dialect (of English or of the home language) is not corrected as an error of meaning. The teacher page says: a gap in
> English is not a learning disability, and slow progress is never read as one; refer to the school's team when a student
> is far below in the home language too. If a student tells you something about their home, listen, do not promise secrecy,
> and follow the school's duty to report; at home, a child's disclosure is not handled alone. Teacher notes on how a home
> language works are written for Spanish first, read as a Spanish read (brief, kind `spanish`); a second language's note
> waits until a reader for it exists, and the page says so.

  Needs a sensitivity read (brief kind `sensitivity`, community: multilingual learners and immigrant families): every
host text that is about migration or about a student's own group, the newcomer strand's first units, any family-language
note, and the family notes (kind `spanish` for Spanish). A transfer chart for any language but Spanish needs a reader
from that language; none is planned. Confidence: Firm that the section is missing; Likely on the exact rules.

### 5. The dose is stated in one place only, no time figure is cited, and our default is below every published state figure I found

- **Where:** STANDARD.md section 2 ("about 30 minutes in K to 5 and a 45 minute period in 6 to 12, 160 days"); APPROACH.md
  (no pacing); bar item 8.
- **What is wrong:** There is no national figure for ELD minutes (the federal guidance gives none; from memory). The pages
  cite none and do not say so. The states that publish a figure publish far more than our period (search summaries, not
  opened by me): Arizona's structured English immersion model sets 120 minutes a day in K to 5 and 100 in 6 to 12; Rhode
  Island's rules (2025) set a 45 minute dedicated period as a floor, with more periods at lower levels; Montana's guidance
  recommends 45 to 135 minutes by level. California sets no minimum (CDE FAQ, opened) and asks only for designated time in
  the regular day. The pages never say whether our period is the whole of an English learner's ELD or a protected add-on
  to the school's own ELD time.
- **Cost:** A school reads "30 minutes, 160 days" and takes it as a program. A student who needs more than 80 hours a year
  gets less than the state asks for. The course page would be silent on that.
- **Fix (add a Pacing paragraph to APPROACH.md, and one sentence to STANDARD section 2; ours, untested):**

> **Pacing.** Settled 2026-11-16: a protected period of about 30 minutes in K to 5 and 45 minutes in 6 to 12, 160 days,
> about 80 and 120 hours a year. There is no national figure for ELD time. States that publish one set it higher (for
> example Arizona, 120 minutes a day in K to 5 and 100 in 6 to 12; Rhode Island, a 45 minute dedicated period; California
> none), so the course page says Curio Class's period is the protected core of a student's English language development
> and not a replacement for the school's own program or for more time where a state or district asks for it. Each band frame
> may change the minutes with a reason.

  Verify the three state figures at their pages before they are published (marked "per search summary" above); the
California statement is checked. Confidence: Likely.

### 6. No statement of what a tool may and may not do

- **Where:** APPROACH.md (no section); COURSES-STATUS lists 21 ELD tools (15 spec, 1 built, 5 live). DESK-ANSWERS (line 176) records
  "English only with pictures and read-aloud; home-language glossaries later".
- **What is wrong:** Health, PE and SEL each state what a tool may and may not do. ELD does not, and ELD is where a tool is most
  tempting: voice recognition, a pronunciation score, a placement check, a translator.
- **Fix (add to APPROACH.md, ours, untested):**

> **What a tool may and may not do.** A tool may give a picture-backed word or sentence-frame practice, read a text aloud,
> let a student hear and replay a model sentence, and give a private self-check. It may not record or store a student's
> voice or writing, score a child's accent or pronunciation, place a student at a proficiency level, translate for a
> family, or stand in for talk with a partner. The talk routine is people.

  Confidence: Firm.

### 7. Stale validator notes

- **Where:** data/standards/wida-2020.txt header line 10 ("scripts/standards.py does not read this file ... would fail");
  STANDARD.md section 1 bullet "For the lead".
- **What is wrong:** scripts/standards.py line 97 builds LISTED from wida-2020.txt, so every full id is valid now. The CLOSED
  pattern for WIDA.ELD-1 to 5 and WIDA.Narrate etc. is kept for data/modules.csv.
- **Fix:** replace both with "scripts/standards.py reads this file as an id list (valid as listed); the coarse codes in
  data/modules.csv remain valid." Also in STANDARD section 1: "each in two modes" reads as if SI also had modes; add
  "(social and instructional language has no mode segment)". Confidence: Firm.

### 8. Sources and read-status are not on the approach page, and the California map is applied outside its range

- **Where:** APPROACH.md "Where the evidence is thin" (claims National Academies 2017 support for teaching language
  through content, structured talk, direct teaching of forms and protected time); the lens "Sources, read into our own
  words"; STANDARD.md section 4; bar part 10 "Rests on".
- **What is wrong:** No sources section; the National Academies, English Learner Success Forum and EL Education items are
  listed without how much was read. The claim about protected time is attributed to the National Academies without a page
  and without "from memory". The California map is for specialized ELD in grades 4 to 8 (approved 2025-11-06), but the
  courses run K to 12, and the criteria map is cited for K to 3 and 9 to 12 as if it covered them. The lens says the PRIME
  rubric was read in full later; the older lens line "the rubric file itself was not opened" is now stale (STANDARD says
  read 2026-11-16).
- **Fix:** Add an "Evidence and sources" section to APPROACH.md (read in full, read in part, from memory, no claim of effect,
  a line to the logic model); mark the protected-time claim "from memory" until a page is cited; say once that the California
  map covers 4 to 8 and is used beyond it by our own extension. Update the lens line about the PRIME file. Confidence: Likely.

### 9. Bar items 13 and 14 have no home on the approach page, and STANDARD says only items 1 to 8 hold

- **Where:** STANDARD.md section 4 ("Bar items 1 to 8 hold"); APPROACH.md last bullet (items 9 to 12); bar part 10, items 13 and 14.
- **What is wrong:** Item 13 (each key language use comes back harder, earlier forms return) needs section field 8 (finding 3)
  and a year map; item 14 (a short note the ELD teacher can share with the host teacher) has no field. The bar's own "Fails if"
  lists "a year that builds only one key language use", which the frames cannot avoid if the host units are all of one kind.
- **Fix:** Add to the APPROACH last bullet: "item 13: each key language use the cluster names returns in a later unit with a
  harder text or task; item 14: unit field 3 carries the two-line note for the host teacher: the content used and the
  language taught." Change STANDARD section 4 to "Bar items 1 to 14 hold." Confidence: Likely.

### 10. The newcomer strand and entry points have no time or exit rule

- **Where:** STANDARD.md section 2 (a short newcomer strand; entry points by proficiency); APPROACH.md ("notes for newcomers").
- **What is wrong:** "A short newcomer strand" has no length, no host unit rule, and no statement of when a student leaves it.
  The page says students move on "the school's own progress checks", but gives no rule for what a teacher with no school
  score does. The strand is the item most likely to be built twice.
- **Fix:** State in STANDARD section 2: the newcomer strand is the first 20 days of each band, runs on the K-3 or 4-12 SI ids
  only with the cluster's Inform, and a student moves to entry points 1 and 2 when the teacher judges the strand's look-fors
  "seen" on two successive days. Confidence: Judgment call.

## What is right and should not be touched

- The id file: 104 ids, exact against the framework, header licence stance, the SI no-mode note.
- Standard in our own words: no run of framework wording found; the pages name the terms (Language Expectation, key language
  use, proficiency level) and nothing else.
- Language through grade-level content with scaffolds, not simplified texts; levels change the help, never the task.
- The kinds-of-day table and the daily-evidence form (a spoken or written sample of the day's form against look-fors).
- The C11 gate and its test; the rule that placement and score keeping belong to the school.
- The lean table in STANDARD section 5: every row family named exists; the "no ELA lean for MA, SC, SS" line is right.
- The base-text scout: its no-whole-course-base finding and its item-by-item VOA caution.

## Not checked

- The California criteria map, the PRIME workbook, the National Academies report: not re-opened.
- The Arizona, Rhode Island and Montana figures: per search summary only.
- docs/RUBRIC-ELD.md, FOUNDATION.md, BASELINE rules and DESK-ANSWERS (beyond one grep line): not read.
- scripts/plan.py: not read; the plan course id for ELD is unknown.
- The reading-literature, reading-informational, presenting and language-strand rows of the ELA progression: named by family
  only, so ids not checked.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Owner year is the cluster's last grade (K, 1, 3, 5, 8, 12); SI K-3 owned by grade 3, SI 4-12 by grade 4; 104 owned rows | Fits the gate and the health and ELA band convention; SI is needed from entry | STANDARD.md section 2 |
| A row carries both mode ids | The gate counts ids | STANDARD.md section 2 |
| Section 10 "two rooms" means a parent at the table and one projector | Matches UNIT-PLAN and every finished page | APPROACH.md |
| Newcomer strand is 20 days | Gives the frame a number to plan | STANDARD.md section 2 |
| Pacing paragraph states the period as the protected core | Honest next to published state figures | APPROACH.md |

## Questions for Cory

1. **Grain (finding 2).** One frame per grade year (13 frames) under four band courses, with four catalogue rows replacing `eld-k12`? Recommended: yes. The alternative is four band frames only, which cannot pair a host unit by grade.
2. **Dose (finding 5).** Keep 30 and 45 minutes, 160 days, and have the course page say it is the protected core, not the whole program? Recommended: yes, keep. The alternative is raising the minutes toward the state figures, which doubles the days to write.
3. **Home languages beyond Spanish (finding 4).** Teacher notes on how Mandarin, Cantonese, Vietnamese, Tagalog and Arabic do the same thing need a reader from each language. Recommended: write Spanish first, add the others only when a reader is found, and say so on the course page. The alternative is to drop the other transfer notes for good.
4. **Sensitive reads (finding 4).** Run a sensitivity read on the newcomer strand and on every migration text before any unit uses it? Recommended: yes, as a pre-use read by a fresh agent (brief kind `sensitivity`).
5. **Your yes on the approach page**, once findings 3, 4, 5, 6 and 8 are in. It stays a draft until then.
