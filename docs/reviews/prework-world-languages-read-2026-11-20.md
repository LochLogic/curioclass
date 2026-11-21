# World languages pre-work: cold read, 2026-11-20

Read as the curriculum expert (docs/agents/EXPERT.md) with the world languages lens
(docs/agents/lenses/world-languages.md). World languages are SHELVED; this read covers the pre-work only and does not
propose unshelving or frames. I did not write these drafts. Nothing was edited but this file. Confidence is Firm,
Likely or Judgment call on each finding. Anything resting on my memory is marked "from memory".

## What I read

AGENTS.md; the brief; docs/courses/world-languages/STANDARD.md and APPROACH.md; data/standards/actfl-wrs.txt;
docs/reviews/world-languages-open-material-2026-11-20.md; the lens; docs/ADOPTION-BAR-SUBJECTS.md part 6 and the
"World languages (2)" row and Decided item 2 (by search of the headings, then the lines); docs/COURSE-RUN.md stage 1;
data/courses.csv rows 36, 37 and 42 only; scripts/progression.py STD_FILES, ANCHOR and code_grades (lines 51 to 112);
the Pacing section of docs/courses/health/APPROACH.md and the headings of health and SEL APPROACH.md (finished
examples); docs/reviews/prework-sel-read-2026-11-19.md (format); the heading and read-kind lines of
docs/pipeline/briefs/sensitivity-read.md; one-line id checks in data/progressions/ela.csv and social-studies.csv.
Web, read today: the ACTFL standards summary page (https://www.actfl.org/educator-resources/world-readiness-standards-for-learning-languages/standards-summary)
and the ACTFL Early Language Learning page (https://www.actfl.org/news/early-language-learning). Not opened: the
2024 Proficiency Guidelines, the CASLS hours page, the can-do page, the ASL standards (the pages say so too).

## Verdict

The standard is sound as a list and honest about what it did not read: the 11 standard ids and 11 level names are
unique and the counts agree, the titles match ACTFL's own page, the words are ours, and all 13 cross-subject skill ids
exist. It is not yet usable for a progression: the ownership rule cannot be run by the gate (levels are not grades,
two languages share one id list, the level names have no rule), the dose is stated for Level 1 only, and the approach
page leaves supports, "how a day opens" and several sensitive grounds thinner than the health and SEL pages.

## What I counted

| Check | Result |
|---|---|
| Standard ids in actfl-wrs.txt | 11, no duplicates (1.1 to 1.3, 2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 5.1, 5.2); five goal areas; matches STANDARD.md section 1 |
| Level ids | 11 (Novice, Intermediate, Advanced each Low, Mid, High, plus Superior and Distinguished); matches STANDARD.md |
| Titles against ACTFL's page, fetched today | all 11 titles match the file header; goal areas Communication, Cultures, Connections, Comparisons, Communities; the page prints no numbers |
| Rights statement on that page | "Copyright 2026 ACTFL", no reuse licence; matches STANDARD.md |
| ACTFL time figure | "more frequent than twice per week" and "at least 90 minutes per week", elementary and middle school, dated 29 July 2012; matches APPROACH.md |
| courses.csv rows | spanish (k-12), french (6-12), asl (k-12); all `n` core; the bar says two |
| Cross-subject skill ids named (13) | all 13 exist as a skill_id: ek-discussion, e3-word-strategies, e5-figurative, e6-word-strategies, e9-sl-presentation, e2-sentences (ela.csv); ss2-culture-migration, ss3-home-region, ss4-regional-cultures, ss2-nation-of-immigrants, us1-immigration, wh1-geography-shapes-contact, psy-language (social-studies.csv) |
| Option table course counts | A 6, B 8, C 10, D 12 total for Spanish plus ASL; the "(+n)" figures are net of the 2 shelved courses and the table does not say so |
| Gate support | scripts/progression.py has no world-languages entry in STD_FILES or ANCHOR; code_grades returns None for a WRS or ACTFL id |

## Findings, most serious first

### 1. The ownership rule cannot be run by the gate, and says nothing for the level names

- **Where:** STANDARD.md section 6; scripts/progression.py STD_FILES, ANCHOR, code_grades.
- **What is wrong:** The gate needs every standard owned by exactly one grade, or excluded with a reason. The page says a
  "level owns" a cell of (language, level, standard, mode or strand) and that Level 1 owns each Communication mode.
  Four gaps follow. (a) The gate's positions are grades and the page makes them levels; a map is named but not written.
  (b) Two languages share one file. If each language is its own progression, every one of the 11 ids is owned twice
  across the subject; if one progression, the 11 ids have two owners per level. The page does not say which. (c) By
  "the first level whose target needs it", all 11 standards are owned by Level 1 (the page itself says all 11 apply
  at every level), so ownership is trivial and carries no depth; the real progression is the depth ladder, which is
  not written. (d) The file also holds 11 `ACTFL.*` level ids; the gate would demand each be owned or excluded. They are
  a scale, not skills. The strand rows (Spanish sounds and spelling, seven ASL parameters) have no id file at all, so
  nothing can validate them.
- **Cost:** A progression writer would invent the rule; two writers would differ. The gate would fail on the level ids.
- **Fix (text the writer can paste into STANDARD.md section 6; ours, untested):**

> **Ownership for the gate.** Each language is its own subject key in the progression (`spanish`, `asl`), so each owns
> the 11 `WRS` ids once. A WRS id is owned by Level 1 of that language as "met at Novice depth"; Levels 2 to 4 carry it as
> `~ID` with a one-line note naming the harder function, context, text type and control (the depth ladder). The 11
> `ACTFL.*` level ids are excluded with the reason "a proficiency scale used to name each level's exit target, not a
> skill". Strands (sounds and spelling; the seven ASL parameters) get their own id file, one id each, owned by the level
> that first teaches them. For the gate, Level 1 to Level 4 map to positions 1 to 4 in a level list that replaces the grade
> list for these two subjects.

  What the gate would need: a `world-languages` entry in STD_FILES and ANCHOR (actfl-wrs.txt with the `ACTFL.*` ids
  filtered out or listed as exclusions), a per-language split, a level list in place of the grade list, and a
  code_grades rule that returns all four levels as the span for a WRS id (owner Level 1). Confidence: Firm.

### 2. The dose is stated for Level 1 only, and the cited figure does not cover high school

- **Where:** APPROACH.md "Pacing and dose"; STANDARD.md section 5 and question 7.
- **What is wrong:** Stage 1 asks for the dose by band. The page gives one draft (three sessions a week of 30 to 45
  minutes, Level 1), no weeks a year, no hours a level, and no dose for Levels 2 to 4 or for K to 5 versus 6 to 12.
  ACTFL's published figure (I read it today) is for elementary and middle school; nothing is cited for high school. The
  exit targets (Novice Mid, Novice High, Intermediate Mid, Intermediate High) are not tied to any hours figure; the
  hours-to-proficiency page was found and not opened, and the exit sublevels are from memory. "30 to 45 minutes" is a
  range, so a day count cannot be computed (the SEL read made the same point).
- **Cost:** A frame cannot set a day count or test whether a level's exit is reachable. A reader could take 90 minutes a
  week as a promise of the exit targets.
- **Fix (ours, untested):**

> **Dose by level.** Default: 36 weeks a year, three sessions a week of 35 minutes, about 63 hours a level (Levels 1 to
> 4); a K to 5 learner has the same course at the same dose. This clears ACTFL's floor for elementary and middle school
> (more than twice a week, at least 90 minutes a week; ACTFL, 29 July 2012); no national figure was found for high
> school, and none is claimed. The course page says the hours are not shown to reach the exit sublevels, and the
> exit targets are ours until the hours page is read.

  Pick one number per level and let a frame change it with a reason, as health does. Confidence: Likely.

### 3. Cross-subject leans have no grade anchor, so "taught by then" cannot be checked

- **Where:** STANDARD.md section 6 (leans); COURSE-RUN stage 2 check ("every cross-subject lean points to a skill
  taught by then").
- **What is wrong:** All 13 ids exist, which is good. But the leans point at grade-coded skills (ela e3, e5, e6, e9;
  social studies ss2, ss3, ss4, us1, wh1, psy-language at grade 12) from courses that have no grade. A grade 3 learner
  and a grade 9 learner both take Level 1. The page says a level is not placed behind a grade, which is right, but
  then the stage 2 check cannot pass or fail.
- **Cost:** The gate check is undefined; a writer might lean Level 1 on a grade 9 skill.
- **Fix (ours, untested):**

> A cross-subject lean from a language level is a pointer for the teacher, not an assumption. A lean names a core skill
> and the earliest grade at which a typical learner meets it; the unit never assumes it. A lean to a skill of grade 6
> or later is allowed only from Level 3 or 4 units. `psy-language` is a later cross-link and not part of the gate.

  Confidence: Likely.

### 4. Course list and counts: three rows, a table whose "+n" is unlabelled, and an unsettled grain

- **Where:** STANDARD.md sections 2 and 5; data/courses.csv rows 36, 37, 42; bar part 6 and the owed row.
- **What is wrong:** (a) The page reports the French mismatch correctly (catalogue three, bar two) and leaves it as a
  question; fine. (b) The option table says "6 (+4)" and "8 (+6)": the +n is the net of the 2 existing rows, but the
  table never says so, and the second "(+10)" for option D reads as 10 more. (c) The page says counts add to "the 105
  active" while the bar's own line reads "120 courses (118 active, 2 world languages shelved)". I did not open the
  other sources, so which total is current is not mine to say; the page should state which and why. (d) courses.csv
  gives Spanish and ASL as `k-12` rows and Spanish's note says "Modules keyed by level not grade"; Option B makes
  each level a course, so the CSV grain and the course grain differ, and French at 6-12 conflicts with an early start.
  (e) plan.py's course ids for levels are not named (the SEL read raised the same grain issue).
- **Cost:** The count the plan reports is ambiguous; a catalogue edit has no stated form.
- **Fix (ours, untested):** in the table header write "Courses, Spanish plus ASL (net of the 2 shelved rows in
  brackets)"; replace "(+10)" with "(+10 net, 12 in all)". Add: "If Option B is chosen, courses.csv gets rows
  `spanish-1` to `spanish-4` and `asl-1` to `asl-4`, grades `k-12` each, and the two existing rows are replaced; French
  stays one row until Question 2 is answered." Confidence: Likely.

### 5. The 90 percent target-language rule collides with the "two rooms" field and the English family note

- **Where:** APPROACH.md "What a good world language lesson does" (instructions in English are a fail), section field 10
  (a parent who may not know the language), unit field 9 (family note in English and Spanish).
- **What is wrong:** The bar fails "instructions in English" and the lens says English is used "for a purpose and said
  so". Field 10 puts a parent who "does not know the language" at the table, and the page's instructions to that adult
  are English. The page does not say which text is for the adult (English is right) and which for the learner (target
  language). For an ASL unit, a parent who cannot sign cannot run the exchange.
- **Cost:** The check "instructions in English" could flag every home-table day, or no day.
- **Fix (ours, untested):**

> Learner-facing instructions are in the target language with a picture, a gesture or a model. The adult's note (the
> "before you teach" block and the family note) is in English and Spanish and says what to say or sign. English for the
> learner is allowed only to name a word's meaning on first use, said so on the page. In ASL home-table days, the
> adult and child share the printed chart and sign together; no exchange is claimed when no one in the room signs.

  Confidence: Judgment call.

### 6. Several plan fields the finished pages fill are thin or missing

- **Where:** APPROACH.md against docs/courses/health/APPROACH.md (headings: "How a day opens", "What a health day never
  does", "Supports", "Pacing") and SEL APPROACH.md.
- **What is wrong:** The page fills unit fields 1 to 10 and section fields 1 to 11 in outline, kinds of day, daily
  evidence, sensitive ground, tool limits and sources. It is thin where the finished pages are not: (a) section field 6
  lists "opening" with no rule for how a day opens; (b) section field 9 is one line for help, extension and access, with
  nothing on reading load, check accommodations, the words taught in depth, or a learner with no home-language
  support in English or Spanish; (c) there is no "what a world language day never does" list (the lens already holds
  it, so it can be lifted); (d) the withdrawal day for help is named but no rule says how the day is chosen by level;
  (e) "Unit field 7" lacks a marking-minutes figure and a cap on respond-day groups (it names at most four).
- **Cost:** C10 and C11 (supports, access) would be scored from a page with one line; every writer fills these four ways.
- **Fix (ours, untested):**

> **How a day opens.** A day opens with a short retrieval task in the target language on one earlier structure (five
> minutes at most), then the day's model. **Supports.** Six to eight words a unit are taught in depth with a picture.
> Reading load: a text of at most the level's stated length, with a picture for every line at Level 1. Check
> accommodations: a point-or-sign or oral answer in place of writing, extra time, a partner to read the prompt. Extension
> on the same standard: a longer text, less help, a second person's view; never the next level's structure. **A
> world-language day never**: uses a word list or conjugation drill as the whole lesson, has the teacher or tool talk
> most of the time, withdraws a frame on no named day, or shows an English gloss as if it were the sign.

  Confidence: Likely.

### 7. Sensitive ground is named but five items are missing, and no read covers ASL form

- **Where:** APPROACH.md "Sensitive ground and which reads it needs"; docs/pipeline/briefs/sensitivity-read.md (kinds
  `sensitivity`, `safety`, `answer-key`, `text`, `rights`, `spanish`).
- **What is wrong:** The page names whose language, immigration status, home dialect and a deficit view of deafness; those
  are right. Missing: (a) names for the people (Hispanic, Latino, Latinx and Latine; each community's own term, with the
  choice stated); (b) Indigenous languages and colonial history in Spanish-speaking places; (c) religion and holidays
  in cultural units; (d) Deaf history that is contested (the oralism era, cochlear implants, the Deaf community's own
  words about each), and taboo or vulgar signs and name signs; (e) a learner's own deafness or hearing loss as
  something never assumed or asked. The read kinds cover cultural text (`sensitivity`), Spanish family and student copy
  (`spanish`) and authentic text (`text`), but no kind checks a sign drawing for correct form; the page rightly says a
  Deaf person must read ASL, and the agent read is not a stand-in.
- **Cost:** An agent read could pass an ASL drawing it cannot judge; a unit could take a stand on a contested term.
- **Fix (ours, untested):** add to the sensitive ground list: "Names for people use the term the community uses for
  itself and say that choices differ (Hispanic, Latino, Latine). Colonial history and Indigenous languages are named
  where they bear on the language, with the community's own words first. Religious holidays are described, never
  observed. Contested Deaf history is shown as the Deaf community tells it, with both views stated and no verdict; no
  taboo sign is taught. A learner's hearing status is never asked." Add under reads: "ASL drawings and Deaf cultural
  text: a Deaf signer reads before use; the agent `sensitivity` read checks wording only." Confidence: Likely.

### 8. Source status is mostly honest; three stale or unlike notes

- **Where:** actfl-wrs.txt header; STANDARD.md sections 1 and 7; APPROACH.md "Evidence and sources".
- **What is wrong:** (a) The file header still says the numbering is "not verified as printed in the 2015 edition",
  while STANDARD.md says it was checked (no numbers printed); both agree the numbers are not on the page, but the
  header should say they are our labels. I confirmed today that ACTFL's summary page prints no numbers. (b) The header
  cites an actfl.org PDF address and STANDARD.md cites a Utah copy of the PDF; one source should be named for the
  extracted text. (c) APPROACH.md says it "read in full" the ACTFL two-page summary and the Early Language Learning
  page, while STANDARD.md section 1 says the page and PDF were "read 2026-11-20"; the three should agree on "read
  in full". The ACTFL early-language page I fetched today does support the 90 minutes and the date. Two items still
  rest on memory and are marked: the four exit sublevels and that ACTFL has applied its guidelines to ASL.
- **Cost:** C13 (a research claim rests on a source nobody read) would be tested on any mismatch.
- **Fix (ours):** replace the header note with "the 2015 summary prints 11 titles and no numbers; the ids are our
  labels in the 2015 order" and name one PDF address. Confidence: Firm (checkable by reading the lines side by side).

## What is right and should not be touched

- The licence stance: ids, titles and our own words only; can-do statements as paraphrases with the note; nothing loaded.
- The standard text: in our own words, with no run of ACTFL's wording copied (checked page against page).
- Reporting the French mismatch without fixing it; the four options with a recommendation; marking every web fact
  "not checked" or "from memory".
- ASL graphics only, no video, no photos of people, and the Deaf-signer read rule; the heritage path inside each level.
- The scout: no CC BY ASL base text found, Spanish licences read item by item, Semillas licence conflict flagged.

## Not checked

- Whether the ACTFL 2024 guidelines keep Distinguished unchanged; the full 2015 standards volume; the can-do text; the
  Clerc, ASLTA, Indiana and Massachusetts ASL standards (403 or search only on the pages).
- The bar's other parts and the 105 versus 118 count (not opened beyond part 6 and the owed row).
- The GLOSSARY day kinds (not opened); the unit-plan field numbers (taken from the SEL read and health page).

## Questions for Cory

1. **Level split.** Option B (four levels, sublevel exits). Recommended: B. Alternatives A, C, D as on the page.
2. **French.** Recommended: keep it parked in the catalogue; correct the bar to three only when the pass opens.
3. **Ownership form (finding 1).** Recommended: each language its own progression, Level 1 owns the 11 WRS ids, the
   level names excluded as a scale. Or a single shared progression with two owners per id?
4. **ASL standard.** Recommended: World-Readiness and the ACTFL scale, plus our parameters strand; Clerc noted only.
5. **Who checks ASL pages.** Recommended: no public ASL page before a Deaf ASL teacher reads it. Yes or no?
6. **Dose (finding 2).** Recommended: 36 weeks, three sessions of 35 minutes, about 63 hours a level, with no claim that
   the hours reach the exit targets. Or higher?
7. **Early start (K to 5).** Recommended: the same course with an age note, an early-years form later.
8. **Approach page yes.** Recommended: yes after findings 1, 2, 6 and 7 are in.
9. **Can-do licence request to NCSSFL and ACTFL.** Recommended: Cory sends one short note asking whether paraphrase in a
   free tool set is acceptable.
