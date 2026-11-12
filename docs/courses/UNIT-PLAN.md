# The stretch sheet and the unit plan

**Second draft, 2026-11-11. Cory said yes to the stretch sheet, both field lists, the word caps, the mark "light
tool" and the readiness check before the stretch opens (2026-11-11, Desk card q-unit-plans). The fields are
fixed for grade 4 math; the first plan in science and in English language arts may change what those subjects
fill.**

**Changed 2026-11-11, evening (Cory, Desk card q-plans-4d-1): new word caps (see "Length"), tool asks moved
to one file per course, rule 19 ("always cover the whole standard") and the fractions wording in rule 4.**

Two documents are written before any tool for a unit is specced or built.

- **The stretch sheet** is written first, once for each stretch. It holds what belongs to the whole stretch:
  the standards and their parts, the readiness check, the end check, the errors, the respond half of the last
  day, the tools and supplies, the family note and the sources.
- **The unit plan** is written next, once for each unit. It says what the unit teaches, its exit questions,
  what each day is for and what job any tool has. It is a plan, not a lesson script.

A stretch with one unit has **one merged document**: the stretch fields, then unit fields 3 to 11.

**File names.** `docs/courses/<course>/sNN.md` for a stretch sheet and for the merged document of a one-unit
stretch. `docs/courses/<course>/uNN-N.md` for a unit plan. Examples: `math-4/s03.md`, `math-4/u03-1.md`.
`docs/courses/<course>/TOOL-ASKS.md` holds everything the course's plans ask of a tool's spec, one section
for each tool (rule 10). Example: [math-4/TOOL-ASKS.md](math-4/TOOL-ASKS.md).

The fields come from the twelve in [APPROACH.md](../APPROACH.md) and the math additions in
[APPROACH-MATH.md](../APPROACH-MATH.md). The first draft was tried on three grade 4 math units and then read
cold by the curriculum expert ([the review](../reviews/unit-plans-2026-11-11.md)). This draft follows that
review. The trial documents are [s03](math-4/s03.md) with [u03-1](math-4/u03-1.md) (a concept unit),
[s09](math-4/s09.md) with [u09-1](math-4/u09-1.md) (a procedure unit) and [s11](math-4/s11.md) (the pilot, a
one-unit stretch with a key tool). The fields have been tried on math only, and checked against the science
and ELA spines only. The first plan in each of those subjects may change what that subject fills. No plan has
been used with children.

## Facts live in data (added 2026-11-11, Cory: "Let's implement those architectural fixes")

A course is too large for any one agent to hold, and a fact written in four files drifts. So:

1. **Facts have one home: `data/plans/<course>/`** (see `data/plans/README.md`). Parts of each standard, days,
   check items, exit questions, wrong answers and the error register are rows. The tables in a sheet or a plan
   are built from them between `<!-- gen:NAME -->` markers. Nobody edits a generated table.
2. **Prose is for judgment only:** why this order, what is carried and when it is withdrawn, what to say when a
   class is stuck, what a tool is for. If a sentence states a fact that a row holds, cut the sentence.
3. **The script is the first reader.** `python -X utf8 scripts/plan.py check` must pass before any expert or
   person reads a plan. It recomputes every key, checks that every part of every standard has an end-check
   item (rule 5), that no check item reuses taught numbers (rule 4), and that days and minutes add up.
4. **Defaults are written once,** in the course's `DEFAULTS.md`. A sheet or plan writes a support, an
   accommodation or a room note only where it differs.
5. **A stretch is planned when the one before it is built** (BASELINE rule 25).
6. **A writer or reader starts from the stretch's reading pack** (`scripts/plan.py pack <course> <stretch>`),
   not from the whole course.
7. **Every defect is logged** in `data/plans/defects.csv` with who found it and at which layer.

State: stretch 11 is in data. Stretches 1, 2, 3, 9 and 10 move when each is next opened. The word caps under
"Length" still stand for prose; a generated table does not count.

Added 2026-11-12 (Cory's yes on card q-ela-piece-2): ELA adds three row files to `data/plans/<course>/`:
`texts.csv` (the text record), `questions.csv` (every question with its standard) and `words.csv` (the word
list). They are shown as generated tables and do not count toward the word cap. The columns are fixed when the
first ELA pilot plan is written. Not built yet.

## The rules

Each rule is marked **shared** (every subject) or **math fills** (the subject page sets the detail; what math
sets is given).

1. **Shared. The stretch sheet is written before any unit plan of the stretch.** Checks belong to the
   stretch and sit whole in one place.
2. **Shared. Checks are written before the days.** On the stretch sheet, fields 4 to 6 come before field 8.
   In a unit plan, fields 3 and 4 come before field 6.
3. **Shared. Every check item is real.** It has its numbers or its text, its standard code, its answer, its
   likely wrong answers and what each wrong answer shows. "A problem about area" is not an item.
4. **Shared. No end-check item or exit question reuses the numbers or the story of a worked example, a wrong
   example, a planned question or a tool item in the same stretch. Same error, new numbers.** A remembered
   answer is not evidence of the skill. (From memory: standard practice in writing checks; no source was
   opened for it.) **In fractions** (decided 2026-11-11): the rule applies to the fractions an item gives,
   not to every renaming along the way. The given pair and the answer must both be new to the stretch.
5. **Shared. The end check covers every part of each standard.** The parts are listed by verb in stretch
   field 2. Every part has at least one item before any part has two. Items are not shared out by days.
6. **Shared. At least half the readiness items serve the first unit. An item for a later unit is asked at the
   opening of that unit. The reteach takes the next day's warm-up and first five minutes, for the whole class
   if more than a third missed the item, otherwise for a small group while the rest do the warm-up.**
7. **Shared. "Many" means more than a third of the class,** everywhere in a sheet or a plan.
8. **Shared. No tool without a named job, and one job for each use.** The job is one of: show why, practise
   with feedback, check unaided. A tool may be used more than once; each use has one job. A day row names the
   part of the tool used, its job and its minutes, with at most two parts a day. A day with no tool says
   "None".
9. **Shared. Every tool is marked key or light,** written "(key)" or "(light)" in a day row. A key tool is as
   FOUNDATION defines it. A unit that runs on print has no key tool, and says so.
   "Light tool" replaced "practice tool" (decided 2026-11-11), which sounded like the job "practise with
   feedback".
10. **Shared. The ideal instrument is named first, then the spec is judged against it.** Fits, partly fits or
    does not fit, with the reason in one sentence. A tool that is wanted and does not exist is named as "does
    not exist". The sheet and the plan keep only that verdict and a link. The gaps and what the plan asks of
    the spec go in the course's one tool-asks file, `docs/courses/<course>/TOOL-ASKS.md`: a section for each
    tool, with its mark, which day uses which part for which job, and the numbered asks, each with the sheet
    or plan it came from (decided 2026-11-11).
11. **Shared. Every day has a kind, in the subject page's words.** *Math fills:* understanding, fluency, use
    or check. The last day of a stretch is written "Check (end check 30, respond 20, next readiness 10)". The counts go in the
    header.
12. **Shared. What is carried is named, with what happens to it over the unit** (math: tied and withdrawn;
    science: revised; ELA: read and returned to). *Math fills:* the model, the day it is tied to the written
    form and the day it is withdrawn.
13. **Shared. Teaching first is the default for anything new.** An opening task is allowed when students can
    attempt it and the goal is an idea. *Math fills:* ten minutes at most.
14. **Shared. No countdown timer in any tool.** *Math fills:* a fluency unit says how fluency is built
    without one.
15. **Shared. The standard's verb is quoted exactly,** and a unit says which part of the standard it carries.
16. **Shared. Nothing claims a result.** Anything written from memory is marked "from memory". A target of our
    own is marked "ours, untested". A tool that is not built is marked "spec only". Sources are listed.
17. **Shared. House rules hold:** plain words, short sentences, "Curio Class" in full, no company names in the
    body of a sheet or plan.
18. **Shared. Word caps, by count.** See "Length".
19. **Shared. Always cover the whole standard** (Cory's words, decided 2026-11-11). A plan teaches and checks
    every part of each standard it claims, in both directions where the standard has two, even where a spine
    title names only one part. Example: 4.NF.A.1 is taught and checked by multiplying both numbers and by
    dividing both numbers. Rule 5 says the same of the end check; this rule says it of the teaching days and
    the exit questions too.

## The stretch sheet: fields, in order

**1. Header.** *Shared.* Course; the stretch and its days; its units with their days; weight (major,
supporting, additional); days by kind, summed from the units.

**2. Standards, limits, and what is carried.** *Shared:* each standard with its parts listed by verb; the
limits; what is carried through the whole stretch. *Math fills:* the model, the day it is tied to the written
form, the day it is withdrawn. (Science: the phenomenon or design problem, the question board and the class
model. ELA: the text set, the word list, the main piece of writing.)

**3. Where it sits.** *Shared.* Builds on, with the handoff marked strong or weak; leads to; where it comes
back.

**4. Readiness check, whole.** *Shared.* When it is given; a table with each item, its code, its key and the
unit it serves; for each gap, the ten-minute reteach, when those ten minutes happen, and the earlier tool or
page. Rule 6 holds. The check is given before the stretch opens, so it is marked before day 1 and can shape it
(decided 2026-11-11): in the last ten minutes of the previous stretch's last day, or of the respond day where
one sits between the two stretches. Stretch 1 is served by the start-of-year check. So the last day of a
stretch is end check 30, respond 20, the next stretch's readiness check 10.

**5. End check, whole.** *Shared.* A table: number; code and practice; the part of the standard (the verb) it
tests; the item; the answer; wrong answers with their error letter; the unit that owns it. Rules 3, 4 and 5
hold. For each teacher-judged item: the look-fors and two sample answers, one that meets them and one that
does not. One line on accommodations (read aloud, large print, a scribe, an oral answer). A row for a unit
with no plan yet says "to write with unit N.N".

**6. Error register.** *Shared.* Errors and first ideas, lettered once for the stretch, each with what it
shows and its source or "from memory". Unit plans use these letters.

**7. The respond half.** *Shared.* How the end check is marked inside the period, and what each error group
does. The marking step, in these words unless the subject page changes them: "Students mark the short items
against the key on the screen, pen down, five minutes. Hands up by item sets the groups. Teacher-judged items
are read after class and answered in the next day's first five minutes." For one child: go over the missed
items together.

**8. Tools and supplies across the stretch.** *Shared:* each tool with its day, mark and job, its verdict
(rule 10) and a link to the course's TOOL-ASKS.md; the supplies list. Not here: tool gaps or asks of a spec.
(Science adds materials tiers and safety.)

**9. Family note.** *Shared.* Once for the stretch, one or two sentences.

**10. Sources and what is still to make.** *Shared.* The standards file; the progression page; the specs
read; any open course read to learn, with its licence and what was read; what was not seen; what is still to
make.

## The unit plan: fields, in order

**Header.** *Shared.* Course; the stretch, with a link to its sheet; this unit's days; days by kind; the words
"A plan, not a lesson". Not here: the length of a day (the spine holds it).

**1. Standards and practices.** *Shared:* the code; this unit's share of the standard, with the verb quoted;
the limits that bite in this unit; connections (other standards of the grade used on purpose, with the day);
what the teacher page must explain, at an adult's level. *Math fills:* strategies or the named algorithm,
where the standard sets one; one or two mathematical practices, each with its day and task. Not here: a list
of all eight practices, or the standard's full text (the stretch sheet holds it).

**2. Where it sits.** *Shared.* One or two lines: what comes just before and just after; the readiness items
it uses, and where its own results go. Not here: builds on, leads to and comes back (stretch field 3).

**3. Checks, written first.** *Shared:* the numbers of the end-check items this unit owns (the items are on
the stretch sheet); then the day's evidence in the subject's form, written out. *Math fills:* an exit
question for each day, in full, with its answer and its wrong answers by error letter. Rule 4 holds. Not
here: the end-check items, or what to do about an error.

**4. Expected errors and first ideas.** *Shared.* For each letter this unit meets: a wrong example beside a
right one, and the day it is shown; what to do if many made it. The action fits in five to ten minutes. Not
here: what the error shows, or its source (the register).

**5. What is carried, and instruments.** *Shared:* what is carried in this unit and what happens to it (rule
12); then each key moment, with the ideal instrument and the spec judged against it (rule 10); what a room
with nothing does. Not here: how the tool works inside (its spec), the tool's gaps and asks (the course's
TOOL-ASKS.md), or the supplies list (stretch field 8).

**6. Days.** *Shared:* one row a day: day; goal in student words; kind; how it opens and for how long; who
holds what is carried; tool by part, with mark, job and minutes (rule 8), or "None"; work by hand; the day's
evidence, by its number in field 3. Not here: a script, the text of the exit question, or the warm-up.

**7. Talk and writing.** *Shared.* Two or three planned questions with their days; one written task; the
look-fors the teacher judges it by. A procedure unit may have one short task and say so. Not here: a full
rubric for a short unit. (A teacher-judged check item needs look-fors and two sample answers; those sit on
the stretch sheet.)

**8. Practice that returns.** *Shared:* what earlier work is practised on each day. *Math fills:* the warm-up;
the fluency target, or "none; the standard sets none"; for a fluency unit, how fluency is built with no
timer. (In ELA "fluency" means reading fluency.)

**9. Supports and extension.** *Shared.* English learners: the words and a sentence frame. Access: what
changes for a student who cannot see, hear, fold or write small. Check accommodations for the exit questions.
Reading load: how much a student must read alone, and what is read aloud. Extension on the same standard, not
the next one. Not here: a different goal for some students.

**10. Two rooms.** *Shared.* A parent teaching one child: what to do at the table, in a few lines, with one
line on the last day of the stretch if this unit holds it. One projector: how the day runs with one screen.

**11. Not in this unit, and still to make.** *Shared.* What a reader might expect and will not find, and where
it lives. What is still to make. Whether any tool named is spec only. The "from memory" marks this plan
relies on. Not here: apologies, or the stretch's standing sources.

## A stretch with one unit

One document, named `sNN.md`. Stretch fields 1 to 10 come first, then unit fields 3 to 11, numbered U3 to
U11. Three things move so nothing is written twice:

- Stretch field 2 also holds what unit field 1 would: the unit's share, connections, strategies or algorithm,
  practices, and what the teacher page must explain.
- The error register (stretch field 6) also holds the wrong example with its day and the "if many" action.
  U4 is one line pointing to it.
- U3 holds only the exit questions. The end check is in stretch field 5.

## Length

Count words, not pages. A page depends on the screen.

Decided by Cory, 2026-11-11 (Desk card q-plans-4d-1). These replace the first caps (see "Decided").

- **Unit plan:** 1,250 words, not counting fields 3 (checks), 4 (errors) and 6 (days).
- **Stretch sheet:** 1,250 words, not counting its check tables and error register (fields 4, 5 and 6).
  (Both raised from 1,000 and 800 by Cory later on 2026-11-11, after the stretch 3 and 10 files ran over.)
- **One-unit stretch, one merged document:** 1,800 words, not counting checks, errors and days (stretch
  fields 4, 5 and 6, and U3, U4 and U6). Decided by Cory, 2026-11-11, in chat ("1,800 words is fine").
- **Tool gaps and spec asks** do not sit in a sheet or a plan, so they do not count. They go in the course's
  TOOL-ASKS.md (rule 10).

How to count: every word in the file outside the fields left out, the title and the header paragraph
included. A whole field is in or out; nothing is counted by the line.

When over, cut in this order:

1. Sentences that restate a rule of this page.
2. "Not in this unit" lines that repeat field 1.
3. The reasons behind a spec judgment, beyond one sentence.
4. Supports that repeat the course-wide ones.

Never cut: check items, exit questions, errors, day rows.

## Blank copy: stretch sheet

```
# Stretch N: Name

Course. **Days A to B.** Units: N.1 Title (days _ to _); N.2 Title (days _ to _). Weight: major, supporting
or additional. Days by kind, summed from the units: understanding _, fluency _, use _, check 1. A plan, not a
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
Day _ (the day before the stretch opens), last ten minutes.

| # | Code | The item | Key | Serves unit |
|---|---|---|---|---|

- **Gap on _.** Ten-minute reteach; when; earlier tool or page, or none.
- **Asked later.** Item _, at the opening of unit _ (day _).

## 5. End check, whole
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

## 8. Tools and supplies across the stretch
- **Tools.** Name (mark): day _, part, job. Verdict: fits, partly fits, does not fit. Asks: TOOL-ASKS.md.
- **Supplies.**

## 9. Family note

## 10. Sources and what is still to make
```

(The header paragraph is field 1.)

## Blank copy: unit plan

```
# Unit N.N: Title

Course. Stretch N, Name (days A to B): see sNN.md. **Days A to B.** Days by kind: understanding _, fluency _,
use _, check _. A plan, not a lesson: nothing here is built or tried with children. Fields follow
UNIT-PLAN.md.

## 1. Standards and practices
- **CODE, this unit's share.** The verb, quoted.
- **Limits that bite here.**
- **Connections.** CODE, day _.
- **Strategies or algorithm.** (only where the standard sets one)
- **Practices.** MP._: day _, task. MP._: day _, task.
- **What the teacher page must explain.**

## 2. Where it sits

## 3. Checks, written first
**End-check items owned:** _ (on the stretch sheet).

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
- **How fluency is built with no timer.** (fluency units)

## 9. Supports and extension
- **English learners.**
- **Access.**
- **Check accommodations.**
- **Reading load.**
- **Extension, same standard.**

## 10. Two rooms
- **Teaching one child.**
- **One projector.**

## 11. Not in this unit, and still to make
```

## What the trial changed

Each line is a change to the twelve proposed fields, with the reason. The expert read kept some, adjusted
others; its verdict follows each.

1. **A header line was added, with days by kind.** The plan is where the spine's counts are settled. *Kept;
   a fourth count, "check", was added.*
2. **Field 1 gained "this unit's share".** Units 3.1 and 9.1 each carry part of a standard. *Kept.*
3. **Strategies and practices moved from the day rows into field 1.** They were the same on every day.
   *Kept.*
4. **"Where it comes back" moved from field 9 to field 2.** *Kept; it now sits on the stretch sheet.*
5. **"End check" became "Checks".** *Adjusted: the end check sits whole on the stretch sheet. The unit plan
   lists the numbers it owns and writes out its exit questions.*
6. **Expected errors moved up and were lettered, with the response on the error.** *Kept. Letters are given
   once for the stretch.*
7. **Readiness was given only by the first unit.** *Adjusted: it moves to the stretch sheet, with rule 6.*
8. **"What is carried" became "Model and instruments", ideal instrument first.** *Kept, and renamed "What is
   carried, and instruments" so the name fits every subject.*
9. **The day row's "who holds the model" was cut to a few words.** *Kept.*
10. **"Supports and stretch" was renamed "Supports and extension".** *Kept.*
11. **Talk and writing uses look-fors, not a rubric.** *Adjusted: look-fors for a short task; each
    teacher-judged check item also has two sample answers.*
12. **"Sources" was added.** *Adjusted: standing sources move to the stretch sheet. The plan keeps its "from
    memory" marks.*
13. **Two pages was kept as the cap.** *Adjusted: the cap is counted in words. See "Length".*

## What the expert read changed

1. **The stretch sheet.** Readiness, the end check, the error letters, "where it sits", the family note and
   the sources belong to the stretch. Split across unit plans they could not be balanced or read whole, and
   the pilot had cut two end-check items to fit a page.
2. **Rule 4, no reuse.** In all three trial plans a check item repeated something already taught. Each was
   replaced.
3. **Rule 5, every part of the standard.** Items were shared out "by share of days", which spreads them by
   time and not by the parts of the standard. The pilot's end check missed perimeter with multi-digit sides.
4. **Rule 6, readiness.** Items for later units now wait for those units, and the reteach has a named slot.
5. **Rule 7, "many".** It was undefined.
6. **The marking step.** The respond half followed a thirty-minute check with no time to mark it.
7. **Shared and "math fills".** Rules and fields that were math in disguise (kinds of day, tie and
   withdrawal, the exit question, the fluency target) are marked, with shared wording.
8. **Four additions:** what the teacher page must explain; check accommodations and reading load;
   connections, for every unit and not only supporting work; "many".
9. **The four awkward points of the first draft are settled.** The last day's kind is "Check (end check 30,
   respond 20, next readiness 10)". The mark "practice tool" becomes "light tool". One job
   for each use of a tool. The checks have a home.
10. **Word caps by count,** with an order in which to cut.
11. **Teacher-judged items carry two sample answers.**

## Decided, Cory, 2026-11-11 (Desk card q-unit-plans)

- The stretch sheet and both field lists, as a whole.
- The tool mark name "light tool"; FOUNDATION's key tool wording now reads "the one a day is planned around".
- The readiness check is given before the stretch opens. Cory asked for the option with more structural
  rigor; the cost is ten minutes of the respond half on each stretch's last day.
- Unit 9.1 on days 72 to 73 and unit 9.2 on days 74 to 77 (see [s09](math-4/s09.md)); in the spine.
- The word caps. A merged one-unit document counts its 2,500 words without the two check tables, as a stretch
  sheet does. The two trial stretch sheets run about 100 to 170 words over 700; accepted for the trial, and the
  cap is looked at again after the next three sheets. **Replaced the same evening; see the next section.**
  The first caps were: unit plan 1,500 words; stretch sheet 700 words of prose plus its two check tables;
  one-unit stretch 2,500 words.

## Decided, Cory, 2026-11-11, evening (Desk card q-plans-4d-1)

The caps were looked at again after stretches 1, 2 and 3 were written. Cory's answers that change this page:

- **Word caps.** A unit plan is 1,000 words not counting its checks, errors and days fields (3, 4 and 6). A
  stretch sheet is 800 words not counting its check tables and error register (fields 4, 5 and 6). Later the
  same day Cory raised both to 1,250 ("the other files should get their cap raised again to 1250 words") and
  set the merged one-unit document at 1,800 ("1,800 words is fine").
- **Tool gaps move out.** Tool gaps and spec asks no longer sit in the sheets or plans. They go in one
  tool-asks file for each course, `docs/courses/<course>/TOOL-ASKS.md`. A sheet's tools field keeps only the
  verdict and a link (rule 10; stretch field 8; unit field 5).
- **"Always cover the whole standard"** (Cory's words). Now rule 19, and in
  [BASELINE.md](../agents/decisions/BASELINE.md) rule 23. It came from day 14 of grade 4 math, which now
  teaches the equivalence rule in both directions.
- **No reuse, in fractions.** The rule applies to the fractions an item gives, not to every renaming along
  the way; the given pair and the answer must both be new to the stretch. Now in rule 4.
