# Course plans as data

Set up 2026-11-11 (Cory: "Let's implement those architectural fixes"). A fact about a course has one home, here.
The plan files in `docs/courses/<course>/` keep prose only for judgment, and their tables are built from these
files. Nobody edits a table in a plan file: change the row here, then run the script.

## The files, per course (`data/plans/<course>/`)

| File | One row is | Columns worth knowing |
|---|---|---|
| `parts.csv` | one part of one standard that a stretch must teach and check | `code`, `part`, `verb` (the standard's own), `stretch`, `unit` |
| `days.csv` | one teaching day | `kind`, `goal`, `opens` and `opens_min`, `tool` (its folder name), `mark` (key or light), `tool_use` and `tool_min`, `exit`, `check_min` |
| `items.csv` | one question on a readiness check, an end check or an exit question | `check`, `day`, `code`, `part`, `judged` (key or teacher), `stem`, `answer` (as printed), `compute`, `value` |
| `wrongs.csv` | one wrong answer we expect to an item | `shown`, `compute`, `value`, `error` (a letter in the error register), `note` |
| `errors.csv` | one lettered error of a stretch | `source`, `example`, `day`, `if_many` |

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
    python -X utf8 scripts/plan.py pack math-4 11   one stretch's reading pack for an agent
    python -X utf8 scripts/plan.py defect math-4 s11.md plan expert key "what was wrong" [where it is written up]
    python -X utf8 scripts/plan.py defects          the ledger, counted by reader and layer

The gates fail on: a key the script cannot reproduce; a part of a standard with no end-check item; an end-check
item or exit question that reuses the numbers of a taught example or of another item; a unit whose days do not
match `data/units.csv`; day numbers with a hole; an opening plus a tool that run past the lesson; check-day
parts that do not add to 60 minutes; a tool with no folder or no mark; an error letter that is not in the
register; a standard code that is not in the standards file.

In a plan file a table sits between `<!-- gen:NAME -->` and `<!-- /gen -->`. Names: `parts`, `readiness`,
`end-check`, `errors`, `exits`, `days`.

## What the gates cannot see

Whether a question is a good question, whether a day teaches, whether the wording suits a nine-year-old, and any
answer that is judged by a teacher. Those stay with the expert and with people. The no-reuse gate compares sets
of numbers only; a reused story with new numbers gets past it.

## State

Grade 4 math stretch 11 (the pilot unit) is in data and passes. Stretches 1, 2, 3, 9 and 10 are still prose only;
each moves into data when it is next opened. Lesson-day items are added to `items.csv` when the pilot is built.
