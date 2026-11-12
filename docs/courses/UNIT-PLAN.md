# The unit plan and the section plan

**Second draft, 2026-11-11. Cory said yes to the unit plan, both field lists, the word caps, the mark "light
tool" and the readiness check before the unit opens (2026-11-11, Desk card q-unit-plans). The fields are
fixed for grade 4 math; the first plan in science and in English language arts may change what those subjects
fill.**

**Changed 2026-11-11, evening (Cory, Desk card q-plans-4d-1): new word caps (see "Length"), tool asks moved
to one file per course, rule 19 ("always cover the whole standard") and the fractions wording in rule 4.**

Two documents are written before any tool for a section is specced or built.

- **The unit plan** is written first, once for each unit. It holds what belongs to the whole unit:
  the standards and their parts, the readiness check, the end-of-unit assessment, the errors, the respond half of the last
  day, the tools and supplies, the family note and the sources.
- **The section plan** is written next, once for each section. It says what the section teaches, its exit questions,
  what each day is for and what job any tool has. It is a plan, not a lesson script.

A unit with one section has **one merged document**: the unit fields, then section fields 3 to 11.

**File names.** `docs/courses/<course>/sNN.md` for a unit plan and for the merged document of a one-section
unit. `docs/courses/<course>/uNN-N.md` for a section plan. Examples: `math-4/s03.md`, `math-4/u03-1.md`.
`docs/courses/<course>/TOOL-ASKS.md` holds everything the course's plans ask of a tool's spec, one heading
for each tool (rule 10). Example: [math-4/TOOL-ASKS.md](math-4/TOOL-ASKS.md).

The fields come from the twelve in [APPROACH.md](../APPROACH.md) and the math additions in
[APPROACH-MATH.md](../APPROACH-MATH.md). The first draft was tried on three grade 4 math sections and then read
cold by the curriculum expert ([the review](../reviews/unit-plans-2026-11-11.md)). This draft follows that
review. The trial documents are [s03](math-4/s03.md) with [u03-1](math-4/u03-1.md) (a concept section),
[s09](math-4/s09.md) with [u09-1](math-4/u09-1.md) (a procedure section) and [s11](math-4/s11.md) (the pilot, a
one-section unit with a key tool). The fields have been tried on math only, and checked against the science
and ELA scopes and sequences only. The first plan in each of those subjects may change what that subject fills. No plan has
been used with children.

## Facts live in data (added 2026-11-11, Cory: "Let's implement those architectural fixes")

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
5. **A unit is planned when the one before it is built** (BASELINE rule 25).
6. **A writer or reader starts from the unit's reading pack** (`scripts/plan.py pack <course> <unit>`),
   not from the whole course.
7. **Every defect is logged** in `data/plans/defects.csv` with who found it and at which layer.

State: unit 11 is in data. Units 1, 2, 3, 9 and 10 move when each is next opened. The word caps under
"Length" still stand for prose; a generated table does not count.

Added 2026-11-12 (Cory's yes on card q-ela-piece-2): ELA adds three row files to `data/plans/<course>/`:
`texts.csv` (the text record), `questions.csv` (every question with its standard) and `words.csv` (the word
list). They are shown as generated tables and do not count toward the word cap. The columns are fixed when the
first ELA pilot plan is written. Not built yet.

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
   opened for it.) **In fractions** (decided 2026-11-11): the rule applies to the fractions an item gives,
   not to every renaming along the way. The given pair and the answer must both be new to the unit.
5. **Shared. The end-of-unit assessment covers every part of each standard.** The parts are listed by verb in unit
   field 2. Every part has at least one item before any part has two. Items are not shared out by days.
6. **Shared. At least half the readiness items serve the first section. An item for a later section is asked at the
   opening of that section. The reteach takes the next day's warm-up and first five minutes, for the whole class
   if more than a third missed the item, otherwise for a small group while the rest do the warm-up.**
7. **Shared. "Many" means more than a third of the class,** everywhere in a unit plan or a section plan.
8. **Shared. No tool without a named job, and one job for each use.** The job is one of: show why, practise
   with feedback, check unaided. A tool may be used more than once; each use has one job. A day row names the
   part of the tool used, its job and its minutes, with at most two parts a day. A day with no tool says
   "None".
9. **Shared. Every tool is marked key or light,** written "(key)" or "(light)" in a day row. A key tool is as
   FOUNDATION defines it. A section that runs on print has no key tool, and says so.
   "Light tool" replaced "practice tool" (decided 2026-11-11), which sounded like the job "practise with
   feedback".
10. **Shared. The ideal instrument is named first, then the spec is judged against it.** Fits, partly fits or
    does not fit, with the reason in one sentence. A tool that is wanted and does not exist is named as "does
    not exist". The unit plan and the section plan keep only that verdict and a link. The gaps and what the plan asks of
    the spec go in the course's one tool-asks file, `docs/courses/<course>/TOOL-ASKS.md`: a heading for each
    tool, with its mark, which day uses which part for which job, and the numbered asks, each with the unit plan
    or section plan it came from (decided 2026-11-11).
11. **Shared. Every day has a kind, in the subject page's words.** *Math fills:* understanding, fluency, application
    or check. The last day of a unit is written "Check (end-of-unit assessment 30, respond 20, next readiness 10)". The counts go in the
    header.
12. **Shared. What is carried is named, with what happens to it over the section** (math: tied and withdrawn;
    science: revised; ELA: read and returned to). *Math fills:* the model, the day it is tied to the written
    form and the day it is withdrawn.
13. **Shared. Teaching first is the default for anything new.** An opening task is allowed when students can
    attempt it and the goal is an idea. *Math fills:* ten minutes at most.
14. **Shared. No countdown timer in any tool.** *Math fills:* a fluency section says how fluency is built
    without one.
15. **Shared. The standard's verb is quoted exactly,** and a section says which part of the standard it carries.
16. **Shared. Nothing claims a result.** Anything written from memory is marked "from memory". A target of our
    own is marked "ours, untested". A tool that is not built is marked "spec only". Sources are listed.
17. **Shared. House rules hold:** plain words, short sentences, "Curio Class" in full, no company names in the
    body of a unit plan or section plan.
18. **Shared. Word caps, by count.** See "Length".
19. **Shared. Always cover the whole standard** (Cory's words, decided 2026-11-11). A plan teaches and checks
    every part of each standard it claims, in both directions where the standard has two, even where a scope and sequence
    title names only one part. Example: 4.NF.A.1 is taught and checked by multiplying both numbers and by
    dividing both numbers. Rule 5 says the same of the end-of-unit assessment; this rule says it of the teaching days and
    the exit questions too.

## The unit plan: fields, in order

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
page. Rule 6 holds. The check is given before the unit opens, so it is marked before day 1 and can shape it
(decided 2026-11-11): in the last ten minutes of the previous unit's last day, or of the respond day where
one sits between the two units. Unit 1 is served by the start-of-year check. So the last day of a
unit is end-of-unit assessment 30, respond 20, the next unit's readiness check 10.

**5. End-of-unit assessment, whole.** *Shared.* A table: number; code and practice; the part of the standard (the verb) it
tests; the item; the answer; wrong answers with their error letter; the section that owns it. Rules 3, 4 and 5
hold. For each teacher-judged item: the look-fors and two sample answers, one that meets them and one that
does not. One line on accommodations (read aloud, large print, a scribe, an oral answer). A row for a section
with no plan yet says "to write with section N.N".

**6. Error register.** *Shared.* Errors and first ideas, lettered once for the unit, each with what it
shows and its source or "from memory". Section plans use these letters.

**7. The respond half.** *Shared.* How the end-of-unit assessment is marked inside the period, and what each error group
does. The marking step, in these words unless the subject page changes them: "Students mark the short items
against the key on the screen, pen down, five minutes. Hands up by item sets the groups. Teacher-judged items
are read after class and answered in the next day's first five minutes." For one child: go over the missed
items together.

**8. Tools and supplies across the unit.** *Shared:* each tool with its day, mark and job, its verdict
(rule 10) and a link to the course's TOOL-ASKS.md; the supplies list. Not here: tool gaps or asks of a spec.
(Science adds materials tiers and safety.)

**9. Family note.** *Shared.* Once for the unit, one or two sentences.

**10. Sources and what is still to make.** *Shared.* The standards file; the progression page; the specs
read; any open course read to learn, with its licence and what was read; what was not seen; what is still to
make.

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

Decided by Cory, 2026-11-11 (Desk card q-plans-4d-1). These replace the first caps (see "Decided").

- **Section plan:** 1,250 words, not counting fields 3 (checks), 4 (errors) and 6 (days).
- **Unit plan:** 1,250 words, not counting its check tables and error register (fields 4, 5 and 6).
  (Both raised from 1,000 and 800 by Cory later on 2026-11-11, after the unit 3 and 10 files ran over.)
- **One-section unit, one merged document:** 1,800 words, not counting checks, errors and days (unit
  fields 4, 5 and 6, and U3, U4 and U6). Decided by Cory, 2026-11-11, in chat ("1,800 words is fine").
- **Tool gaps and spec asks** do not sit in a unit plan or a section plan, so they do not count. They go in the course's
  TOOL-ASKS.md (rule 10).

How to count: every word in the file outside the fields left out, the title and the header paragraph
included. A whole field is in or out; nothing is counted by the line.

When over, cut in this order:

1. Sentences that restate a rule of this page.
2. "Not in this section" lines that repeat field 1.
3. The reasons behind a spec judgment, beyond one sentence.
4. Supports that repeat the course-wide ones.

Never cut: check items, exit questions, errors, day rows.

## Blank copy: unit plan

```
# Unit N: Name

Course. **Days A to B.** Sections: N.1 Title (days _ to _); N.2 Title (days _ to _). Weight: major, supporting
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
Day _ (the day before the unit opens), last ten minutes.

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

## 7. The respond half
Marking step. Then, by error group:

## 8. Tools and supplies across the unit
- **Tools.** Name (mark): day _, part, job. Verdict: fits, partly fits, does not fit. Asks: TOOL-ASKS.md.
- **Supplies.**

## 9. Family note

## 10. Sources and what is still to make
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
- **How fluency is built with no timer.** (fluency sections)

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

## What the trial changed

Each line is a change to the twelve proposed fields, with the reason. The expert read kept some, adjusted
others; its verdict follows each.

1. **A header line was added, with days by kind.** The plan is where the scope and sequence's counts are settled. *Kept;
   a fourth count, "check", was added.*
2. **Field 1 gained "this section's share".** Sections 3.1 and 9.1 each carry part of a standard. *Kept.*
3. **Strategies and practices moved from the day rows into field 1.** They were the same on every day.
   *Kept.*
4. **"Where it comes back" moved from field 9 to field 2.** *Kept; it now sits on the unit plan.*
5. **"End-of-unit assessment" became "Checks".** *Adjusted: the end-of-unit assessment sits whole on the unit plan. The section plan
   lists the numbers it owns and writes out its exit questions.*
6. **Expected errors moved up and were lettered, with the response on the error.** *Kept. Letters are given
   once for the unit.*
7. **Readiness was given only by the first section.** *Adjusted: it moves to the unit plan, with rule 6.*
8. **"What is carried" became "Model and instruments", ideal instrument first.** *Kept, and renamed "What is
   carried, and instruments" so the name fits every subject.*
9. **The day row's "who holds the model" was cut to a few words.** *Kept.*
10. **"Supports and stretch" was renamed "Supports and extension".** *Kept.*
11. **Talk and writing uses look-fors, not a rubric.** *Adjusted: look-fors for a short task; each
    teacher-judged check item also has two sample answers.*
12. **"Sources" was added.** *Adjusted: standing sources move to the unit plan. The plan keeps its "from
    memory" marks.*
13. **Two pages was kept as the cap.** *Adjusted: the cap is counted in words. See "Length".*

## What the expert read changed

1. **The unit plan.** Readiness, the end-of-unit assessment, the error letters, "where it sits", the family note and
   the sources belong to the unit. Split across section plans they could not be balanced or read whole, and
   the pilot had cut two unit assessment items to fit a page.
2. **Rule 4, no reuse.** In all three trial plans a check item repeated something already taught. Each was
   replaced.
3. **Rule 5, every part of the standard.** Items were shared out "by share of days", which spreads them by
   time and not by the parts of the standard. The pilot's end-of-unit assessment missed perimeter with multi-digit sides.
4. **Rule 6, readiness.** Items for later sections now wait for those sections, and the reteach has a named slot.
5. **Rule 7, "many".** It was undefined.
6. **The marking step.** The respond half followed a thirty-minute check with no time to mark it.
7. **Shared and "math fills".** Rules and fields that were math in disguise (kinds of day, tie and
   withdrawal, the exit question, the fluency target) are marked, with shared wording.
8. **Four additions:** what the teacher page must explain; check accommodations and reading load;
   connections, for every section and not only supporting work; "many".
9. **The four awkward points of the first draft are settled.** The last day's kind is "Check (end-of-unit assessment 30,
   respond 20, next readiness 10)". The mark "practice tool" becomes "light tool". One job
   for each use of a tool. The checks have a home.
10. **Word caps by count,** with an order in which to cut.
11. **Teacher-judged items carry two sample answers.**

## Decided, Cory, 2026-11-11 (Desk card q-unit-plans)

- The unit plan and both field lists, as a whole.
- The tool mark name "light tool"; FOUNDATION's key tool wording now reads "the one a day is planned around".
- The readiness check is given before the unit opens. Cory asked for the option with more structural
  rigor; the cost is ten minutes of the respond half on each unit's last day.
- Section 9.1 on days 72 to 73 and section 9.2 on days 74 to 77 (see [s09](math-4/s09.md)); in the scope and sequence.
- The word caps. A merged one-section document counts
 its 2,500 words without the two check tables, as a unit
  plan does. The two trial unit plans run about 100 to 170 words over 700; accepted for the trial, and the
  cap is looked at again after the next three unit plans. **Replaced the same evening; see the next section.**
  The first caps were: section plan 1,500 words; unit plan 700 words of prose plus its two check tables;
  one-section unit 2,500 words.

## Decided, Cory, 2026-11-11, evening (Desk card q-plans-4d-1)

The caps were looked at again after units 1, 2 and 3 were written. Cory's answers that change this page:

- **Word caps.** A section plan is 1,000 words not counting its checks, errors and days fields (3, 4 and 6). A
  unit plan is 800 words not counting its check tables and error register (fields 4, 5 and 6). Later the
  same day Cory raised both to 1,250 ("the other files should get their cap raised again to 1250 words") and
  set the merged one-section document at 1,800 ("1,800 words is fine").
- **Tool gaps move out.** Tool gaps and spec asks no longer sit in the unit or section plans. They go in one
  tool-asks file for each course, `docs/courses/<course>/TOOL-ASKS.md`. A unit plan's tools field keeps only the
  verdict and a link (rule 10; unit field 8; section field 5).
- **"Always cover the whole standard"** (Cory's words). Now rule 19, and in
  [BASELINE.md](../agents/decisions/BASELINE.md) rule 23. It came from day 14 of grade 4 math, which now
  teaches the equivalence rule in both directions.
- **No reuse, in fractions.** The rule applies to the fractions an item gives, not to every renaming along
  the way; the given pair and the answer must both be new to the unit. Now in rule 4.
