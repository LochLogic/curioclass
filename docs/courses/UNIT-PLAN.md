# The unit plan and the section plan

Two documents are written before any tool for a section is specced or built.

- **The unit plan** is written first, once for each unit. It holds what belongs to the whole unit:
  the standards and their parts, the readiness check, the end-of-unit assessment, the errors, the response allocation, the tools and supplies, the family note and the sources.
- **The section plan** is written next, once for each section. It says what the section teaches, its exit questions,
  what each day is for and what job any tool has. It is a plan, not a lesson script.

A unit with one section has **one merged document**: the unit fields, then section fields 3 to 11.

**File names.** `docs/courses/<course>/sNN.md` for a unit plan and for the merged document of a one-section
unit. `docs/courses/<course>/uNN-N.md` for a section plan. Examples: `math-4/s03.md`, `math-4/u03-1.md`.
`docs/courses/<course>/TOOL-ASKS.md` holds everything the course's plans ask of a tool's spec, one heading
for each tool (rule 10). Example: [math-4/TOOL-ASKS.md](math-4/TOOL-ASKS.md).

The fields come from the twelve in [APPROACH.md](../APPROACH.md) and the math additions in
[APPROACH-MATH.md](../APPROACH-MATH.md). Cory approved the unit plan, both field lists, the word caps, the mark
"light tool" and the readiness timing (settled 2026-11-11, see DESK-ANSWERS). The fields are fixed for grade 4 math
and are in use for all 138 social studies unit plans; the first science and English language arts unit plans may
change what those subjects fill. Worked examples in grade 4 math: [s03](math-4/s03.md) with [u03-1](math-4/u03-1.md)
(a concept section) and [s09](math-4/s09.md) with [u09-1](math-4/u09-1.md) (a procedure section); the expert's read
of the first draft is [the review](../reviews/unit-plans-2026-11-11.md). No plan has been used with children.

## Facts live in data

A course is too large for any one agent to hold, and a fact written in four files drifts. So:

1. **Facts have one home: `data/plans/<course>/`** (see `data/plans/README.md`). Parts of each standard, days,
   check items, exit questions, wrong answers and the error register are rows. The tables in a unit plan or a section plan
   are built from them between `<!-- gen:NAME -->` markers. Nobody edits a generated table.
2. **Prose is for judgment only:** why this order, what is carried and when it is withdrawn, what to say when a
   class is stuck, what a tool is for. If a sentence states a fact that a row holds, cut the sentence.
3. **The script is the first reader.** `python -X utf8 scripts/plan.py check` must pass before any expert or
   person reads a plan. It recomputes every key, checks that every part of every standard has an end-of-unit assessment
   item (rule 5), that no check item reuses taught numbers (rule 4), and that days and minutes add up.
4. **Defaults are written once,** in the course's `DEFAULTS.md`. A unit plan or section plan writes a support, an
   accommodation or a room note only where it differs.
5. **Unit plans follow the subject-wide order in PRODUCTION-PATH steps 3 and 4.** A preceding unit need not have
   written lessons. Section plans follow step 7, except the probe section.
6. **A writer or reader starts from the unit's reading pack** (`scripts/plan.py pack <course> <unit>`),
   not from the whole course.
7. **Every defect is logged** in `data/plans/defects.csv` with who found it and at which layer.

In grade 4 math, unit 11 is in data; units 1, 2, 3, 9 and 10 move into data when each is next opened.

### English language arts data

ELA keeps three kinds of rows (settled 2026-11-12, see DESK-ANSWERS, card q-ela-piece-2): the text record, every
question with its standard, and the word list. They are shown as generated tables and do not
count toward the word cap.

- **Text records: `data/plans/ela-texts.csv`**, one file for all thirteen ELA courses, one row per text a
  frame's text set names. It is not split into `data/plans/<course>/texts.csv` yet, because a course folder with
  no `days.csv` fails `plan.py check`; it moves into the course folders when each course has days. Columns:
  `course`, `unit`, `text_id` (g3-u1-01; gk for kindergarten), `title`, `author`, `year`, `kind` (literary or
  informational; empty for an image), `form`, `length`, `use` (anchor, paired or independent), `part` (whole,
  excerpt, selections or retold), `edition`, `measure`, `demands`, `source`, `status`, `rights_basis`,
  `rights_checked`, `todo`, `note`.
- `measure` holds a free public number only, with where it came from (the base text's module overviews give
  Lexile measures for some K to 5 texts). Otherwise "not on file", a frame target for a text still to write, or
  "none usable" for verse, drama, audio and images. No measure is ever invented.
- `demands` is the qualitative read in a line: meaning, structure, language and knowledge, and reader and task.
- `source`: el-education-k5-2017, public domain, US government work, Curio Class original, a traditional tale
  in a Curio Class retelling, other, or to decide.
- `status`: on file (the text exists and is named), to write (a Curio Class original), to choose (the frame names
  a kind or a set, the unit plan names the text) or to confirm (an edition, title or date needs checking).
- Edition and rights are filled as the units are written: the unit writer gives each text's edition and rights
  basis in field 10, and the lead copies them into `edition`, `rights_basis` and `rights_checked` after each batch
  (settled 2026-11-15, see DESK-ANSWERS). Until then the cells stay empty and the row's `todo` starts with "rights".
- **Questions: rows in the shared `data/plans/<course>/items.csv`,** not a separate file, so every gate that reads
  items (keys, no reuse, exits, assessment minutes, the day pages) works for ELA unchanged (lead 2026-11-15, see
  DESK-ANSWERS). Each ELA row fills the shared columns (`code` is the ELA standard, `judged` is key or teacher, a
  written or spoken task's look-fors go in `steps` and its samples in `samples`) and three more:
  - `text_id`: the text the question is about, from ela-texts.csv (several space separated for a paired-text
    question; empty for a question on no text);
  - `text_ref`: where in the text the answer lives (page, paragraph, lines, chapter or minutes into a read-aloud),
    so a reader can check the answer and a student can be sent back to reread;
  - `needs_text`: yes when the answer cannot be given without the text, no otherwise.
  `plan.py check` fails an ELA row whose `needs_text` is not yes or no, a yes with no `text_id`, a `text_id` with
  no row in ela-texts.csv, and a course where under 80 percent of rows need the text (plan-codex-ela.md).
- **Word list: unit plan output, not input data.** The writer draws it per unit from that unit's texts (about 8
  to 10 words a week) and writes it as `data/plans/<course>/wordlist.csv` with `unit`, `word`, `text_id`, `week`
  and `when` (before, during or after reading). The name is not `words.csv`, which `plan.py` already reads as
  each course's settled word rules.

## The rules

Each rule is marked **shared** (every subject) or **math fills** (the subject page sets the detail; what math
sets is given).

1. **Shared. The unit plan is written before any section plan of the unit.** Checks belong to the
   unit and sit whole in one place.
2. **Shared. Checks are written before the days.** On the unit plan, fields 4 to 6 come before field 8.
   In a section plan, fields 3 and 4 come before field 6.
3. **Shared. Every check item is real.** It has its numbers or its text, its standard code, its answer, its
   likely wrong answers and what each wrong answer shows. "A problem about area" is not an item.
4. **Shared. No unit assessment item or exit question reuses the numbers or the story of a worked example, a wrong
   example, a planned question or a tool item in the same unit. Same error, new numbers.** A remembered
   answer is not evidence of the skill. (From memory: standard practice in writing checks; no source was
   opened for it.) **In fractions,** the rule applies to the fractions an item gives,
   not to every renaming along the way. The given pair and the answer must both be new to the unit.
5. **Shared. The end-of-unit assessment covers every part of each standard.** The parts are listed by verb in unit
   field 2. Every part has at least one item before any part has two. Items are not shared out by days.
6. **Shared. At least half the readiness items serve the first section. An item for a later section is asked at the
   opening of that section. The reteach takes the next day's warm-up and first five minutes, for the whole class
   if more than a third missed the item, otherwise for a small group while the rest do the warm-up.** In social
   studies a repair is the warm-up and, where needed, a small group during the next pairs or alone part; it never
   takes minutes from the next day's worked example (expert read, US History I day 80, 2026-11-15).
7. **Shared. "Many" means more than a third of the class,** everywhere in a unit plan or a section plan.
8. **Shared. No tool without a named job, and one job for each use.** The job is one of: show why, practise
   with feedback, check unaided. A tool may be used more than once; each use has one job. A day row names the
   part of the tool used, its job and its minutes, with at most two parts a day. A day with no tool says
   "None".
9. **Shared. Every tool is marked key or light,** written "(key)" or "(light)" in a day row. A key tool is as
   FOUNDATION defines it. A section that runs on print has no key tool, and says so.
10. **Shared. The ideal instrument is named first, then the spec is judged against it.** Fits, partly fits or
    does not fit, with the reason in one sentence. A tool that is wanted and does not exist is named as "does
    not exist". The unit plan and the section plan keep only that verdict and a link. The gaps and what the plan asks of
    the spec go in the course's one tool-asks file, `docs/courses/<course>/TOOL-ASKS.md`: a heading for each
    tool, with its mark, which day uses which part for which job, and the numbered asks, each with the unit plan
    or section plan it came from.
11. **Shared. Every day has a kind, in the subject page's words.** *Math fills:* understanding, fluency, application
    or check. A day that ends with the next unit's readiness check names its ten minutes, as in "Check (end-of-unit
    assessment 30, respond 20, next readiness 10)" (field 4). The counts go in the header.
12. **Shared. What is carried is named, with what happens to it over the section** (math: tied and withdrawn;
    science: revised; ELA: read and returned to). *Math fills:* the model, the day it is tied to the written
    form and the day it is withdrawn.
13. **Shared. Teaching first is the default for anything new.** An opening task is allowed when students can
    attempt it and the goal is an idea. *Math fills:* ten minutes at most.
14. **Shared. No timer without a grounded purpose** (a pace cue, a movement game, classroom management; BASELINE rule 30). *Math fills:* a fluency
    section says how fluency is built without time pressure.
15. **Shared. The standard's verb is quoted exactly,** and a section says which part of the standard it carries.
16. **Shared. Nothing claims a result.** Anything written from memory is marked "from memory". A target of our
    own is marked "ours, untested". A tool that is not built is marked "spec only". Sources are listed.
17. **Shared. House rules hold:** plain words, short sentences, "Curio Class" in full, no company names in the
    body of a unit plan or section plan.
18. **Shared. Word caps, by count.** See "Length".
19. **Shared. Always cover the whole standard** (Cory's words; also BASELINE rule 23). A plan teaches and checks
    every part of each standard it claims, in both directions where the standard has two, even where a scope and sequence
    title names only one part. Example: 4.NF.A.1 is taught and checked by multiplying both numbers and by
    dividing both numbers. Rule 5 says the same of the end-of-unit assessment; this rule says it of the teaching days and
    the exit questions too.

## The unit plan: fields, in order

Math-only fields: the *Math fills* parts, which are unit plan field 2 (the model and its days) and section plan
fields 1 (strategies or the named algorithm, and the mathematical practices), 3 (an exit question for each day)
and 8 (the warm-up and the fluency target). Every other field is shared by all subjects.

**1. Header.** *Shared.* Course; the unit and its days; its sections with their days; weight (major,
supporting, additional); days by kind, summed from the sections.

**2. Standards, limits, and what is carried.** *Shared:* each standard with its parts listed by verb; the
limits; what is carried through the whole unit. *Math fills:* the model, the day it is tied to the written
form, the day it is withdrawn. (Science: the phenomenon or design problem, the question board and the class
model. ELA: the text set, the word list, the main piece of writing.)

**3. Where it sits.** *Shared.* Builds on, with the handoff marked strong or weak; leads to; where it comes
back.

**4. Readiness check, whole.** *Shared.* When it is given; a table with each item, its code, its key and the
section it serves; for each gap, the ten-minute reteach, when those ten minutes happen, and the earlier tool or
page. Rule 6 holds.

- **Which units hold one** (sequence-write.md rule 2, the rule for every course): a row used the year before, or
  earlier the same year, opens as a retrieval task inside a day, with no readiness check; every other earlier-grade
  row the unit assumes (last used two or more grades back) gets a readiness check. A unit with only retrieval tasks
  fills this field with them (the row, the day, the prompt and what the teacher does with a miss); their teacher
  notes are the before-teaching evidence (adoption bar C8).
- **When** (one timing in every course, grade 4 math included; settled 2026-11-14, see DESK-ANSWERS): the readiness
  check is given before the unit opens, so its results shape day 1. It takes the last ten minutes of the previous
  unit's last day, or of the respond day or course-level check respond day where one sits between the two units;
  that day is the one days.csv marks `assess` = `readiness` (or, when it already holds another assess value, keeps
  that value and its note says "plus the next unit's readiness check (10 minutes)"). It is given a few days ahead at
  most, never weeks, so the results stay fresh. Where the last day is a full end-of-unit assessment day, it runs
  end-of-unit assessment 30, respond 20, the next unit's readiness check 10.
- **Unit 1:** where unit 1 has readiness rows, its check takes the last ten minutes of day 1, after the hook and
  the compelling question, and days.csv marks day 1 `readiness` (lead 2026-11-14, see DESK-ANSWERS). Every other
  unit's day 1 stays clean for the hook and the compelling question: no readiness check on a unit's first day.
- **The field's first line** (the gate accepts any line of the field) is `Given:` (the day), `Retrieval only:` (the retrieval tasks) or, in unit 1,
  `Start-of-year check:`. `scripts/unitplan.py` fails a field 4 with none of the three, and a `Given:` line that names
  the unit's first day outside unit 1.

**5. End-of-unit assessment, whole.** *Shared.* A table: number; code and practice; the part of the standard (the verb) it
tests; the item; the answer; wrong answers with their error letter; the section that owns it. Rules 3, 4 and 5
hold. For each teacher-judged item: the look-fors and two sample answers, one that meets them and one that
does not. One line on accommodations (read aloud, large print, a scribe, an oral answer). A row for a section
with no plan yet says "to write with section N.N". A part scored from work made on an earlier day counts only if
that work had written feedback and a chance to revise before it is scored; work from the day a topic is first
taught is practice, never a scored part (social studies probe, 2026-11-15).

**6. Error register.** *Shared.* Errors and first ideas, lettered once for the unit, each with what it
shows and its source or "from memory". Section plans use these letters. **One mistake per letter:** a letter holds
one misconception with one repair; two claims joined by "and" or a semicolon are two letters. A wrong answer is
filed only under a letter whose text describes it (social studies probe, 2026-11-15).

**7. Response allocation.** *Shared.* Name the marking time and the response time separately. State whether response
occurs within the assessment day or on later respond days, and count it once. Then how the end-of-unit assessment is
marked, and what each error group does. The marking step, in these words unless the subject page changes them: "Students mark the short items
against the key on the screen, pen down, five minutes. Hands up by item sets the groups. Teacher-judged items
are read after class and answered in the next day's first five minutes." For one child: go over the missed
items together. **Social studies** (world-history-i probe, 2026-11-15): items are teacher-judged
by component, so nothing is self-marked by hands up. The groups come from the record sheet's 0 and 1 cells by
component, through a component-to-move table in this field (each scored component to the error letter whose move
repairs it); cap the respond day at four groups, others work in pairs from the written move; give the marking time
honestly (minutes a student times the class).

**8. Tools and supplies across the unit.** *Shared:* each tool with its day, mark and job, its verdict
(rule 10) and a link to the course's TOOL-ASKS.md; the supplies list. Not here: tool gaps or asks of a spec.
(Science adds materials tiers and safety.)

**9. Family note.** *Shared.* Once for the unit, one or two sentences.

**10. Sources and what is still to make.** *Shared.* The standards file; the progression page; the specs
read; any open course read to learn, with its licence and what was read; what was not seen; what is still to
make. **Verified or none:** a text the days will quote is named with where its words were checked (a free
primary-text archive, a park service or other government page, the publisher's own page); a passage that could not
be checked is not planned. A paraphrase of a book we have not read is never a source. **Paid-only texts:** a text
found only in paid editions (a people's own chronicle, epic or inscription) may be named and described, never
quoted, when a free secondary source we have read (a museum, UNESCO, a university or a scholar's free article) says
what it holds; the day credits what it says to that secondary source, whose link goes in sources.csv.

**Day list.** After field 10, `## Day list (from days.csv, do not edit)`: one row a day with its kind, written by
`scripts/unit_skeleton.py`. `scripts/unitplan.py` checks it against days.csv.

## The section plan: fields, in order

**Header.** *Shared.* Course; the unit, with a link to its unit plan; this section's days; days by kind; the words
"A plan, not a lesson". Not here: the length of a day (the scope and sequence holds it).

**1. Standards and practices.** *Shared:* the code; this section's share of the standard, with the verb quoted;
the limits that bite in this section; connections (other standards of the grade used on purpose, with the day);
what the teacher page must explain, at an adult's level. *Math fills:* strategies or the named algorithm,
where the standard sets one; one or two mathematical practices, each with its day and task. Not here: a list
of all eight practices, or the standard's full text (the unit plan holds it).

**2. Where it sits.** *Shared.* One or two lines: what comes just before and just after; the readiness items
it uses, and where its own results go. Not here: builds on, leads to and comes back (unit field 3).

**3. Checks, written first.** *Shared:* the numbers of the unit assessment items this section owns (the items are on
the unit plan); then the day's evidence in the subject's form, written out. *Math fills:* an exit
question for each day, in full, with its answer and its wrong answers by error letter. Rule 4 holds. Not
here: the unit assessment items, or what to do about an error.

**4. Expected errors and first ideas.** *Shared.* For each letter this section meets: a wrong example beside a
right one, and the day it is shown; what to do if many made it. The action fits in five to ten minutes. Not
here: what the error shows, or its source (the register).

**5. What is carried, and instruments.** *Shared:* what is carried in this section and what happens to it (rule
12); then each key moment, with the ideal instrument and the spec judged against it (rule 10); what a room
with nothing does. Not here: how the tool works inside (its spec), the tool's gaps and asks (the course's
TOOL-ASKS.md), or the supplies list (unit field 8).

**6. Days.** *Shared:* one row a day: day; goal in student words; kind; how it opens and for how long; who
holds what is carried; tool by part, with mark, job and minutes (rule 8), or "None"; work by hand; the day's
evidence, by its number in field 3. Not here: a script, the text of the exit question, or the warm-up.

**7. Talk and writing.** *Shared.* Two or three planned questions with their days; one written task; the
look-fors the teacher judges it by. A procedure section may have one short task and say so. Not here: a full
rubric for a short section. (A teacher-judged check item needs look-fors and two sample answers; those sit on
the unit plan.)

**8. Practice that returns.** *Shared:* what earlier work is practised on each day. *Math fills:* the warm-up;
the fluency target, or "none; the standard sets none"; for a fluency section, how fluency is built with no
timer. (In ELA "fluency" means reading fluency.)

**9. Supports and extension.** *Shared.* English learners: the words and a sentence frame. Access: what
changes for a student who cannot see, hear, fold or write small. Check accommodations for the exit questions.
Reading load: how much a student must read alone, and what is read aloud. Extension on the same standard, not
the next one. Not here: a different goal for some students.

**10. Two rooms.** *Shared.* A parent teaching one child: what to do at the table, in a few lines, with one
line on the last day of the unit if this section holds it. One projector: how the day runs with one screen.

**11. Not in this section, and still to make.** *Shared.* What a reader might expect and will not find, and where
it lives. What is still to make. Whether any tool named is spec only. The "from memory" marks this plan
relies on. Not here: apologies, or the unit's standing sources.

## A unit with one section

One document, named `sNN.md`. Unit fields 1 to 10 come first, then section fields 3 to 11, numbered U3 to
U11. Three things move so nothing is written twice:

- Unit field 2 also holds what section field 1 would: the section's share, connections, strategies or algorithm,
  practices, and what the teacher page must explain.
- The error register (unit field 6) also holds the wrong example with its day and the "if many" action.
  U4 is one line pointing to it.
- U3 holds only the exit questions. The end-of-unit assessment is in unit field 5.

## Length

Count words, not pages. A page depends on the screen.

This list is the one home of the caps (settled 2026-11-11, see DESK-ANSWERS). `scripts/unitplan.py` enforces the unit
plan cap (1,250) on every `sNN.md` and the merged cap (1,800) on any `sNN.md` with `## U3.` to `## U11.` headings,
counting U5 and U7 to U11.

- **Section plan:** 1,250 words, not counting fields 3 (checks), 4 (errors) and 6 (days).
- **Unit plan:** 1,250 words, not counting its check tables and error register (fields 4, 5 and 6).
- **One-section unit, one merged document:** 1,800 words, not counting checks, errors and days (unit
  fields 4, 5 and 6, and U3, U4 and U6).
- **Tool gaps and spec asks** do not sit in a unit plan or a section plan, so they do not count. They go in the course's
  TOOL-ASKS.md (rule 10).

How to count: every word in the file outside the fields left out, the title and the header paragraph
included. A whole field is in or out; nothing is counted by the line. A generated table, the day list and the lines
between `<!-- skel -->` markers do not count.

When over, cut in this order:

1. Sentences that restate a rule of this page.
2. "Not in this section" lines that repeat field 1.
3. The reasons behind a spec judgment, beyond one sentence.
4. Supports that repeat the course-wide ones.

Never cut: check items, exit questions, errors, day rows.

## Blank copy: unit plan

`scripts/unit_skeleton.py` writes this shape with the mechanical fields filled; the writer replaces each
`TODO(writer)` line.

```
# Unit N: Name

Course. **Days A to B** (N course days). Sections: N.1 Title (days _ to _); N.2 Title (days _ to _). Weight: major, supporting
or additional. Days by kind, summed from the sections: understanding _, fluency _, application _, check 1. A plan, not a
lesson: nothing here is built or tried with children. Fields follow UNIT-PLAN.md.

## 2. Standards, limits, and what is carried
- **CODE:** "the standard's words". Parts, by verb: (a) _; (b) _.
- **Limits.**
- **Carried.** What; tied on day _; withdrawn on day _.

## 3. Where it sits
- **Builds on (strong or weak handoff).**
- **Leads to.**
- **Comes back.**

## 4. Readiness check, whole
**Given:** day _ (before the unit opens: the last ten minutes of the previous unit's last day or of the respond day
between). In unit 1, "Start-of-year check:" the last ten minutes of day 1, after the hook. Or "Retrieval only:" with
each retrieval task's row, day and prompt.

| # | Code | The item | Key | Serves section |
|---|---|---|---|---|

- **Gap on _.** Ten-minute reteach; when; earlier tool or page, or none.
- **Asked later.** Item _, at the opening of section _ (day _).

## 5. End-of-unit assessment, whole
Day _, thirty minutes, unaided.

| # | Code, practice | Part (verb) | The item | Answer | Wrong answers (error) | Owner |
|---|---|---|---|---|---|---|

- **Item _, teacher judged.** Look-fors: _. Meets: "_". Does not: "_".
- **Accommodations.**

## 6. Error register
| | The error or first idea | What it shows | Source |
|---|---|---|---|
| A | | | |

## 7. Response allocation
Marking time: _ minutes. Response time: _ minutes, within the assessment day / on respond days _ (counted once).
Marking step. Then, by error group:

## 8. Tools and supplies across the unit
- **Tools.** Name (mark): day _, part, job. Verdict: fits, partly fits, does not fit. Asks: TOOL-ASKS.md.
- **Supplies.**

## 9. Family note

## 10. Sources and what is still to make

## Day list (from days.csv, do not edit)
| Day | School day | Kind | Goal | Codes | Note |
|---|---|---|---|---|---|
```

(The header paragraph is field 1.)

## Blank copy: section plan

```
# Section N.N: Title

Course. Unit N, Name (days A to B): see sNN.md. **Days A to B.** Days by kind: understanding _, fluency _,
application _, check _. A plan, not a lesson: nothing here is built or tried with children. Fields follow
UNIT-PLAN.md.

## 1. Standards and practices
- **CODE, this section's share.** The verb, quoted.
- **Limits that bite here.**
- **Connections.** CODE, day _.
- **Strategies or algorithm.** (only where the standard sets one)
- **Practices.** MP._: day _, task. MP._: day _, task.
- **What the teacher page must explain.**

## 2. Where it sits

## 3. Checks, written first
**Unit assessment items owned:** _ (on the unit plan).

**Exit questions.** If many miss one, the next day opens with that error's wrong example.
- **E_.** "Question." Answer. Wrong: _ (A); _ (B).

## 4. Expected errors and first ideas
| | Wrong example beside a right one; day | If many made it |
|---|---|---|
| A | | |

## 5. What is carried, and instruments
- **Carried.**
- **Key moment 1, day _: what must be seen.** Ideal instrument. Spec: fits, partly fits, does not fit; why.
  Gaps and asks: TOOL-ASKS.md.
- **A room with nothing.**

## 6. Days
| Day | Goal, in student words | Kind | Opens | Who holds it | Tool: part, mark, job, minutes | By hand | Exit |
|---|---|---|---|---|---|---|---|

## 7. Talk and writing
- Planned questions:
- Written task, day _:
- Judged by the teacher with _ look-fors:

## 8. Practice that returns
- **Warm-up.**
- **Fluency target.**
- **How fluency is built without time pressure.** (fluency sections)

## 9. Supports and extension
- **English learners.**
- **Access.**
- **Check accommodations.**
- **Reading load.**
- **Extension, same standard.**

## 10. Two rooms
- **Teaching one child.**
- **One projector.**

## 11. Not in this section, and still to make
```
