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

Work only courses that have been shaped (docs/agents/catalog/shape/<course>.md), so nothing is fixed that is then
cut, merged or given a new role. Each shape file ends with the spec work it leaves for that course; do that first.

1. The two proving courses: grade 4 math, then grade 6 ELA.
2. Each further course as its shape file appears, in the order the roadmap scales them.

## How far to trust the list by subject

Math and social studies: sound. ELA: the read was strict about multiple-choice checks, so expect some "close the
guessable check" items to be already closed. Science: right within one step either way. Computer science, arts,
CTE, world languages, ELD, health and PE, library, SEL: the standards are broad and their wording was not in front
of the reader, so treat each line as a prompt to look, not a verdict. These subjects will be read again once their
standard texts are wired in, and the list rebuilt.

## Questions

A question that changes a tool's shape, holds it, cuts it or adds one goes to Cory on the Desk as a question card.
Everything else is Sara's call under the standing rules (`docs/agents/decisions/DESK-ANSWERS.md`).
