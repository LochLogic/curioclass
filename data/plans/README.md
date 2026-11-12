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
| `days.csv` | one teaching day | `kind`, `goal`, `opens` and `opens_min`, `tool` (its folder name), `mark` (key or light), `tool_use` and `tool_min`, `exit`, `check_min` |
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

## The commands

    python -X utf8 scripts/plan.py check            the gates
    python -X utf8 scripts/plan.py tables           rebuild the tables in the plan files
    python -X utf8 scripts/plan.py pack math-4 11   one unit's reading pack for an agent
    python -X utf8 scripts/plan.py defect math-4 s11.md plan expert key "what was wrong" [where it is written up]
    python -X utf8 scripts/plan.py defects          the ledger, counted by reader and layer

The gates fail on: a key the script cannot reproduce; a part of a standard with no unit assessment item; an end-of-unit assessment
item or exit question that reuses the numbers of a taught example or of another item; a section whose days do not
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
or `paper`), `figure` (a labelled shape for the display, `rect w=7 l=? A=63 u=ft`), `steps` (worked steps split
by `|`) and `source` (the credit of an adapted item; CC BY, CC0 or public domain with a link, or the gate fails).
Units 1, 2, 3, 9 and 10 are still prose only;
each moves into data when it is next opened. 
ELA will add `texts.csv`, `questions.csv` and `words.csv` per course (Cory's yes, 2026-11-12); not built yet, and the columns are fixed when the first ELA pilot plan is written.
