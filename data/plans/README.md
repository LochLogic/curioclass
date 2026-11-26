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
the goal, an id that is not an exit of the day or an end item of the unit, and a teaching day that names no exit
(a teaching day that holds unit assessment items itself, a product judged that day, needs none). It notes a piece
shown by no exit of the day (only by the assessment) and a day that names no end item (the assessment does not see
that goal). An assessment day names its own end items. A unit assessment may run over several days, so the end
items every day of the unit names must cover every part of the unit in parts.csv, read on the unit's last
assessment day (science ladder report, 2026-11-19). Course-level days (`stretch` C) sit at points across the year
and need not have consecutive numbers. Naming an item is a claim that it asks for that piece: the cheap read checks the claim. A goal piece that is set-up (start a living record, observe the class animals) and that no question can honestly show is written `phrase = none`; the gate reads it as a note, and a reader asks whether it is really set-up.

## The commands

    python -X utf8 scripts/plan.py check            the gates
    python -X utf8 scripts/plan.py tables           rebuild the tables in the plan files
    python -X utf8 scripts/plan.py pack math-4 11   one unit's reading pack for an agent
    python -X utf8 scripts/plan.py defect [--status=open|fixed|rejected] math-4 s11.md plan expert key "what was wrong" [where it is written up]
    python -X utf8 scripts/plan.py defects          the ledger, counted by reader and layer

The gates fail on: a key the script cannot reproduce; a part of a standard with no unit assessment item; an end-of-unit assessment
item or exit question that reuses the numbers of a taught example or of another item; a written day with no goal-to-item trace; a keyed exit, end item or fix-it with no wrongs row; a wrong answer with no letter and no note; day numbers with a hole; an opening plus a tool that run past the lesson; assessment-day
parts that do not add to 60 minutes; a tool with no folder or no mark; an error letter that is not in the
register; a standard code that is not in the standards file.

In a plan file a table sits between `<!-- gen:NAME -->` and `<!-- /gen -->`. Names: `parts`, `readiness`,
`end-check`, `errors`, `exits`, `days`.

## Cross-day files and the source map (added 2026-11-13, docs/PRODUCTION-PATH.md step 2)

The unit 4 test found that a third of the problems only an expert caught crossed days: a hand-back no later day
made time for, a strip sheet one day reprinted and the next assumed kept, a worked example used before its day.
A day writer sees one day; these files let the gates see across them. One row per fact, as everywhere here.

| File | One row is | Columns |
|---|---|---|
| `handbacks.csv` | one thing a day sends to a later day | `from_day`, `to_day`, `what` (an item id, or words such as "written task"), `where` (the part of the later day: warm-up, opening, Groups, exit...; `assessment` when the later day scores the item as part of its check, which gives that day the teaching word cap), `minutes`, `error` (a register letter, or blank), `note` |
| `materials.csv` | one material a day uses | `material` (a short name, the words the day's Materials section uses), `made_day` (printed, cut or first handed out), `used_days` (space separated), `kept_in` (envelope, folder, wall...), `per` (student, pair, group, room), `note` |
| `reserved.csv` | one worked example saved for its day | `day`, `numbers` (the given numbers, as an item's stem writes them), `item_id` (when it is a row in items.csv), `note` |
| `source-map.csv` | one base-text lesson, or one of our days with no base lesson | `source` (`im-g4-u3-l09`; `ours` for a day with none), `title`, `goals` (short, from the lesson's prep file), `standards`, `unit` (our section, `4.2`), `days` (space separated), `decision` (keep, split, merge, cut, ours), `why`, `order_conflict` (blank, or what the order clash is), `harms_learning` (yes, no, unclear; blank when no clash) |

| `sources.csv` | one primary source or interpretation a social studies day prints (added 2026-11-15, us-history-i probe) | `source_id` (`78B`: day and letter as the source sheet prints it), `kind`, `title`, `author`, `date`, `citation` (findable without the url), `url`, `rights` (public domain, CC BY, CC0, ours, or paraphrase only), `difficulty`, `why` (its place in the year), `days`, `use` (teach, exit, reserved, packet, background), `status` (what is checked and what is left), `note` (a reserved row ends `watch: <word>; <word>`, the words no earlier day may print). A `background` row is a history named and described in our words, never quoted (UNIT-PLAN field 10, paid-only texts), with the free secondary page it was read from as its url |

Tool rounds need no file of their own: they are already item rows with `check` tool and a `day`.

What the gates hold (plan.py; lesson.py where a written day file is read):

- **handbacks:** both days exist in days.csv; `to_day` is later; a written `to_day` file names the day it comes
  from; the minutes landing in one part of a day fit that part's minutes (a NOTE when they may not).
- **materials:** every day in `used_days` exists; a written day that is listed names the material in its Materials
  or Before class section; no day before `made_day` uses it.
- **reserved:** no item of an earlier day uses the same set of given numbers.
- **sources:** a citation, a rights line from the five, a `use` from the five, a difficulty and a why on every row;
  every day exists; a `reserved` source is printed only on a Check day. lesson.py fails a day before a reserved source's day
  that names its id or a `watch:` word.
- **source-map:** `decision` is one of the five; `cut` and `ours` rows have a `why`; every day listed exists; every
  day of a mapped section appears in at least one row; an `order_conflict` has `harms_learning` filled.

The prose plans point at these files instead of restating them.

## Scope-stage and calendar files (added 2026-11-14, docs/PRODUCTION-PATH.md step 3)

Before a unit has parts or items, a course's `days.csv` is the scope and sequence's day file
(docs/pipeline/briefs/sequence-write.md). Its columns are

    day,stretch,unit,kind,goal,skills,codes,assess,school_day,note

`stretch` is the unit number, or `C` for a course-level check day, its respond days and course-level review days.
`kind` is one of `Understanding`, `Fluency`, `Application`, `Check`, `Respond`. `assess` is `readiness`, `mid`,
`end`, `course`, `observe` (K to 2 only) or blank; it reserves the slot, and the unit plan writes the items.
`school_day` is blank for a course that meets every school day. `scripts/sequence.py` gates it, and `plan.py check`
runs that gate for a plan folder with a days.csv and no parts or items. The `days.csv` row in the first table
describes the written-day columns of a planned unit.

## The ledger (`<course>/ledger.csv`, consolidation step 4.D, 2026-11-25)

One file per course, written only through `scripts/ledger.py` (add, seed, promote, note); its commands still name a
subject and read that subject's courses in ladder order. Any other plan CSV row is written with
`python -X utf8 scripts/rows.py upsert <course> <table> --key <cols> col=value ... [--dry-run]`.

Columns: course, where, day, kind, entry, note, stage, student_word. student_word (4.L) is yes, no or blank on term rows
and blank on other kinds: yes only for a word the page teaches students as vocabulary (`ledger.py add ... --student-word`),
no for a writer's term row without the flag, blank for not judged yet (seeded rows, and the older rows migrated on
2026-11-25, Desk q-student-word-1; the rows seeded from a progression's words list were marked yes). The word backlog
(`vocabulary.py report`) counts only yes rows and prints the blank ones as undecided.

## The course list (`course-list.csv`, consolidation step 4.C, 2026-11-25)

Row order within a subject is teaching order (grade, then the order the courses are taken): ledger.py builds each
subject's ladder from it (consolidation 4.E2), so a new course goes in at its place, not at the end.

The one hand-kept list of the 120 courses. Every other course list (docs/COURSES-STATUS.md, the Desk, `frames.csv`)
is built from it. Columns:

| Column | Holds |
|---|---|
| `id` | the course id, the frame slug (`science-grade-4`, `algebra-i`, `art-grades-k-to-2`); never renamed once a course has plan files |
| `title`, `subject` | the title as shown; the subject id from data/subjects.csv (`ela`, never `english-language-arts`) |
| `grade` | `K` or `1` to `12` for a one-grade course; a band (`k-2`, `3-5`, `6-8`, `9-12`) for a band course; blank for a world language |
| `core` | `yes` for a core course |
| `catalog_id`, `catalog_key` | the tool catalog's row (data/courses.csv) and its placement key; used only to attach topic and tool counts |
| `rows` | which progression rows the course owns, `grade:K` or `prefix:bio-`; filled when its frame is written |
| `term`, `weeks`, `pins` | `year`, `fall` or `spring`; weeks a short-week course spreads over; pinned days as `course day:school day` (CALENDAR.md stagger rule) |
| `legacy_plan_id` | an old plan folder name for the course (`math-4`, the pilot, kept blind) |
| `status` | `active` or `shelved` |

A new course is a new row; its frame fills `rows`. `scripts/frame.py` and `scripts/course_status.py` read it.

The two files below hold every framed course; `python -X utf8 scripts/frame.py sync` writes both from the frames and
the course list (a join); nobody edits them:

| File | One row is | Columns |
|---|---|---|
| `frames.csv` | one course frame | `course`, `catalog_id`, `subject`, `grade`, `title`, `units`, `days`, `minutes_min`, `minutes_max`, `per_week`, `weeks`, `term`, `legacy_plan_id` |
| `calendar.csv` | one unit or course-level check of one course, on the school calendar | `course`, `grade`, `subject`, `kind`, `unit`, `label`, `first_day`, `last_day`, `first_school_day`, `last_school_day`, `first_week`, `last_week` |

`python -X utf8 scripts/frame.py calendar` prints the same placement by grade and lists stagger breaks
(docs/courses/CALENDAR.md).

## Ids: versions, retirement and day numbers (consolidation 4.H, 2026-11-25)

- **A revised item keeps its id; the version goes in the `version` column** (add the column to the course's
  items.csv the first time an item there is revised; blank means version 1). `plan.py check` fails a new item id
  ending in a version suffix (`v2`, `-v2`). The 636 suffixed ids that existed on 2026-11-25 are listed in
  item-suffix-baseline.csv; when a course is next reviewed its suffixes are stripped (the ids in its days, plans and
  CSVs, through a script with a dry run) and its rows leave that file.
- **A retired or merged id is recorded, never reused:** one row in data/ids-retired.csv (old_id, new_id or blank,
  date, reason), append-only. `python -X utf8 scripts/ids.py check` fails an id that is live again after it was
  retired; `ids.py registry` writes data/ids-registry.csv (ignored) from the index plus that file.
- **Day numbers are permanent once a course's scope and sequence is signed off.** A course changes by rewriting a day
  in place or trading content inside a section; the year has a fixed length, so an insert always removes a day
  somewhere. A true renumber is a course rewrite, planned as one.
- **An item id written in prose is a soft use.** The index (scripts/index.py) records bare item ids in plan and
  day prose as soft `mentions` edges; `uses.py <id>` lists them, marked soft, and no gate fails on one. Hard uses
  (links, leans_on, CSV id columns) are the ones a check enforces.

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
The grade 4 math `handbacks.csv` and `materials.csv` are backfilled for every written day (1 to 28 and 72 to 93) on 2026-11-13; `reserved.csv` has no row yet, since no day or plan names a worked example saved for a later day.
ELA text data live in one shared file, data/plans/ela-texts.csv (title, author, use, status; 2026-11-14); ELA questions
are rows in each course's items.csv with three more columns, `text_id`, `text_ref` and `needs_text` (UNIT-PLAN.md,
"English language arts data"); the word list is data/plans/<course>/wordlist.csv, written with the ELA unit plans.

As of 2026-11-15: every science, ELA, math and social studies course has data/plans/<course>/days.csv at the scope
stage (scripts/sequence.py gates it); social studies also has 138 unit plans. Source maps use one layout in every
subject (sequence-write.md rule 8). The grade 4 math lines above describe the older day-level data, kept as the model
for day writing.
