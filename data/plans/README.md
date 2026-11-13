# Course plans as data

Set up 2026-11-11 (Cory: "Let's implement those architectural fixes"). A fact about a course has one home, here.
The plan files in `docs/courses/<course>/` keep prose only for judgment, and their tables are built from these
files. Nobody edits a table in a plan file: change the row here, then run the script.

Column names lag the words (docs/GLOSSARY.md): `stretch` holds the unit number, `unit` the section (`11.1`), and `kind`
`Check` marks an assessment day.

## The files, per course (`data/plans/<course>/`)

| File | One row is | Columns worth knowing |
|---|---|---|
| `parts.csv` | one part of one standard that a unit must teach and check | `code`, `part`, `verb` (the standard's own), `stretch`, `unit` |
| `days.csv` | one teaching day | `kind`, `goal`, `opens` and `opens_min`, `tool` (its folder name), `mark` (key or light), `tool_use` and `tool_min`, `exit`, `check_min`, `shows` (the goal-to-item trace, below) |
| `items.csv` | one question a student answers: on a readiness check, an end-of-unit assessment, an exit ticket, or inside a lesson day | `check` (readiness, end, exit; and for lesson days example, tool, fix, practice, challenge), `day`, `code`, `part`, `judged` (key or teacher), `stem`, `answer` (as printed), `compute`, `value` |
| `wrongs.csv` | one wrong answer we expect to an item | `shown`, `compute`, `value`, `error` (a letter in the error register), `note` |
| `errors.csv` | one lettered error of a unit | `source`, `example`, `day`, `if_many` |

`data/plans/defects.csv` is the defect ledger for all courses: what was found, by which reader, at which layer.

## The compute cell

`compute` is the working that gives the answer, and `value` is the answer as a number. The script works the
first out exactly (fractions stay fractions) and fails if it does not match the second, or if the number is not
in the printed answer. Several answers are split with `|`. Write a fraction as `F(19;8)` (a semicolon stands for
the comma). A claim can be checked as true or false: `12+7==11+8` with value `True`. Every item marked against
a key must have a compute cell. A wrong answer has one wherever the mistake can be worked out (`28-4` for the
child who subtracts), which also shows the error letter fits.

## The goal-to-item trace (`shows`)

Added 2026-11-12 after the unit 2 reads (day 8's exit and item 4 never asked for the later step the goal names).
Every written day fills `shows` in its days.csv row: each piece of the goal, then the items that show it.

    find a later step without drawing them all = s02-X8v2 s02-E4v2; follow a rule to make a shape pattern = s02-X8v2 s02-E4v2

A phrase is words copied from the goal; the ids after ` = ` are exits of that day or end-of-unit items of its
unit. The gate splits the goal at commas, "and" and "or" and fails a piece that no phrase covers, a phrase not in
the goal, an id that is not an exit of the day or an end item of the unit, and a teaching day that names no exit.
It notes a piece shown by no exit of the day (only by the assessment) and a day that names no end item (the
assessment does not see that goal). An assessment day names its own end items, and they must cover every part of
the unit in parts.csv. Naming an item is a claim that it asks for that piece: the cheap read checks the claim.

## The commands

    python -X utf8 scripts/plan.py check            the gates
    python -X utf8 scripts/plan.py tables           rebuild the tables in the plan files
    python -X utf8 scripts/plan.py pack math-4 11   one unit's reading pack for an agent
    python -X utf8 scripts/plan.py defect math-4 s11.md plan expert key "what was wrong" [where it is written up]
    python -X utf8 scripts/plan.py defects          the ledger, counted by reader and layer

The gates fail on: a key the script cannot reproduce; a part of a standard with no unit assessment item; an end-of-unit assessment
item or exit question that reuses the numbers of a taught example or of another item; a written day with no goal-to-item trace; a keyed exit, end item or fix-it with no wrongs row; a wrong answer with no letter and no note; a section whose days do not
match `data/units.csv`; day numbers with a hole; an opening plus a tool that run past the lesson; assessment-day
parts that do not add to 60 minutes; a tool with no folder or no mark; an error letter that is not in the
register; a standard code that is not in the standards file.

In a plan file a table sits between `<!-- gen:NAME -->` and `<!-- /gen -->`. Names: `parts`, `readiness`,
`end-check`, `errors`, `exits`, `days`.

## What the gates cannot see

Whether a question is a good question, whether a day teaches, whether the wording suits a nine-year-old, and any
answer that is judged by a teacher. Those stay with the expert and with people. The no-reuse gate compares sets
of numbers only; a reused story with new numbers gets past it.

## State

Grade 4 math unit 11 (the pilot unit) is in data and passes. Day 90's lesson rows went in on 2026-11-12 with
the lesson-day template (docs/courses/LESSON-DAY.md). Lesson rows count as taught: no exit or check item may reuse
their numbers. `python -X utf8 scripts/lesson.py check` gates the day files in `courses/`, and `build` makes their
print pages. Four optional item columns serve lesson days (draft 2 of the template): `path` (an exit's `tool`
or `paper`), `figure` (a labelled shape for the display, `rect w=7 l=? A=63 u=ft`; a tape picture `strip`, a number line
`line to=2 d=4 pt=7/4 / d=8` or a fraction strip `fstrip 1/2 2/4 4/8`, written out in docs/courses/LESSON-DAY.md), `steps` (worked steps split
by `|`) and `source` (the credit of an adapted item; CC BY, CC0 or public domain with a link, or the gate fails).
Units 1, 2, 3, 9 and 10 are in data too (units 2 and 3 on 2026-11-12); a unit still in prose only moves
into data when it is next opened. 
ELA will add `texts.csv`, `questions.csv` and `words.csv` per course (Cory's yes, 2026-11-12); not built yet, and the columns are fixed when the first ELA pilot plan is written.
