# The spec fix list

Every Curio Class tool, and what its spec needs before it meets the end standard. Sara owns this work (Cory,
2026-11-10): the whole spec catalog, not only the thin specs. When every spec in a course is fixed, the course gets
a final review (FINAL-REVIEW.md).

## The end standard

A spec is finished when it passes the teaching test in `docs/agents/SPEC.md` (BASELINE rule 21) for every code it
carries:

> A student alone, following the tool's lead, meets a model, does the standard's own verb on every part of its
> wording, on five or more items that differ, with a check where thinking is cheaper than guessing, and none of it
> can be skipped.

For writing and talk a tool cannot mark, a model, a guide while working and a self-check against a shown guide
count. A see-why tool lets the student set up cases and predict before each reveal, and says what the unit adds. A
practice tool says where the teaching happened. The bar behind the test is `docs/ADOPTION-BAR.md`: a course has to
stand up to a state adoption review.

Three hooks every spec also carries (added 2026-11-11 after a cold review; the full wording is in
`docs/agents/SPEC.md`, "Three hooks every spec carries"). An adoption review looks for all three, and none was in
the teaching test:

- **A check the teacher can see.** For each code, the tool ends with at least two items done with no model, hint or
  worked example on screen. The end screen shows how the student did on them, code by code, and the spec says what
  each common wrong answer means.
- **English learners.** Every spoken instruction is also on screen in short, plain sentences. Each key word of the
  standard is shown with a picture or an example the first time it is used. Any writing or talk task offers a
  sentence frame. No idioms in instructions.
- **Access.** Every action works by tap and by keyboard; a drag has a tap or key alternative. Nothing is told by
  color alone. Sound that carries meaning has text. Motion can be paused.

## What is in this folder

| File | What it is |
|---|---|
| INDEX.md | One line per course, with counts and how many are done |
| courses/<subject>-<grade>.md | Every tool in that course: the kinds of fix it needs and the exact parts found missing, code by code |
| fix-list.csv | One row per tool, one column per kind of fix. Sort or filter it in a spreadsheet |
| done.txt | The log of what is fixed. The only file here edited by hand |
| FINAL-REVIEW.md | The check each course gets after all its specs are fixed |

INDEX.md, the course files and fix-list.csv are rebuilt by `python scripts/spec_fixes.py`. Do not edit them by
hand; the next run would overwrite the edit.

## The kinds of fix

| Fix | What the read found | What to change in the spec |
|---|---|---|
| Write the spec | The spec is missing, voice-only or too thin to judge | Write it in full to SPEC.md before anything else |
| Hand the key step to the student | The tool does the standard's verb (solves, graphs, sorts, explains) and the student watches or presses on | The student does that step; the tool checks it |
| Close the guessable check | A check with a few choices and free retries | Make a wrong try cost something, widen the choices, ask for a typed or built answer, or add a second check |
| Add the missing part | A part of the standard's wording the student never does: an operation, a case, a lettered part, the explaining or writing | Add an activity for it. "Must add" parts are required; "small" parts only if cheap |
| Add a model or a guide | The student practises with no worked example and no hints | Add one, or mark the tool `practice` and say where the teaching happens |
| Add a check | Nothing tells the student whether the work is right | Add a check, or a self-check against a shown guide for writing and talk |
| Reach five items that differ | Fewer than five problems, rounds or texts for a code | Add items that differ in kind, not only in numbers |
| Put it on the main path | The code sits in an extra mode or can be skipped | Move it onto the path every student takes |
| Teach the code or drop it | The code is listed and nothing matches it | Teach it, or take the code off the spec |
| Sensitivity read | The topic needs care (hard history, identity, health, belief) | No rewrite needed for this alone; it gets a fresh reader at final review |
| Source the facts | A fact, number or date has no source | Add the source to "Sources" |

## How to work a course

1. Open the course file. Tools are listed rework first, then small addition, then fine.
2. For each tool, open its spec beside the list. Read the standard's wording, then the "To do" lines and the missing
   parts.
3. **The read can be wrong.** A spot-check found it right about four times in five, and when wrong it was more
   often too strict than too generous. If the spec already does what the list says is missing, do not change it:
   log it in done.txt with the note "read was wrong" and the section that proves it. The "unsure" lines show where
   the read doubted itself.
4. Change the spec so it passes the teaching test, keeping its idea, setting and voice where they still work. A
   rework may need a new core activity; say so plainly in the spec's change note.
5. Rerun the numbers and worked answers the change touches (SPEC.md, "Check your own numbers").
6. Add a line to done.txt.

Tools marked **built** or **LIVE** have code that follows the old spec. Fix the spec only; the code change is a
separate step Claude runs after (ROADMAP step 3 for live tools, steps 5 and 6 for the rest).

## The order

**Stopped, 2026-11-11 night (Cory): no more spec fix batches.** A spec gets work only when a section plan names its
tool (BASELINE rule 26). What follows is kept as the record of the order that was planned.

**NEXT.md in this folder was the work order, and it stopped at batch 4** (Cory, 2026-11-11):

1. Close the two proving courses (grade 4 math, grade 6 ELA), then their final review.
2. The fourteen grade 6 to 8 ELA band specs, each with a path for grades 6, 7 and 8.
3. Grade 5 math, then grade 3 math, on the splits Cory approved.

Then stop. Every course is shaped, but no other course opens until grade 4 math is proved: three tools built from
fixed specs and one full unit, read by a working teacher (docs/ROADMAP.md, step 4). If the proof changes what a
spec must hold, it changes a few dozen specs, not hundreds. NEXT.md lists the courses on hold and their sizes.

Three things from Shape change how a spec is fixed:

- A tool whose shape file says a second tool was approved keeps only the codes listed there. Drop the rest from the
  spec and spend the room on more items.
- A tool with a Desk card open waits. NEXT.md names them.
- A band tool (grades 6 to 8, say) belongs to each grade it serves. Its spec needs a path for each grade: that
  grade's texts, that grade's wording of the standard, five or more items.

## How far to trust the list by subject

Math and social studies: sound. ELA: the read was strict about multiple-choice checks, so expect some "close the
guessable check" items to be already closed. Science: right within one step either way. Computer science, arts,
CTE, world languages, ELD, health and PE, library, SEL: the standards are broad and their wording was not in front
of the reader, so treat each line as a prompt to look, not a verdict. These subjects will be read again once their
standard texts are wired in, and the list rebuilt.

## Questions

A question that changes a tool's shape, holds it, cuts it or adds one goes to Cory on the Desk as a question card.
Everything else is Sara's call under the standing rules (`docs/agents/decisions/DESK-ANSWERS.md`).
