# Brief: write one lesson day of a Curio Class course

For any writer of one day: a person, or an agent of any kind. Updated 2026-11-12 after the reads of units 1, 2, 3,
9, 10 and 11 (docs/pilots/REVIEW-CADENCE.md): most rules are now gates in the scripts, so this brief says how to
work, what to read, and the few checks no script can make. The template is docs/courses/LESSON-DAY.md.

You work in a checkout of the Curio Class repository on branch main, one writer at a time. Edit only the files
named under "What you write". Do not commit or push unless your job brief says so. Your token use is measured as
the cost of one day, so work directly: read what you need, write, run the gates, fix, stop.

## Read first (in this order)

1. docs/courses/LESSON-DAY.md: the template. Every rule there binds you, the At home block included.
2. courses/math-4/u11-1/d090.md: the worked case for shape, headings, tone and density; d093.md for an
   assessment day.
3. The day before yours, in full (its file and its days.csv row): your opening picks up its Tomorrow, its exit
   tickets and anything it hands on. **If yours is the first day of a unit, the day before is the last day of the
   unit before: read it the same way.** The gate fails a first day that never names it.
4. The day after yours, if it is written: your Tomorrow names only what it does.
5. The unit plan, `docs/courses/<course>/sNN.md` (the file name keeps its old `s`): your day's row in "U6. Days",
   and sections 2, 5, 6, U3, U7 to U10. Then the section plan and the section opener in your section folder.
6. docs/courses/<course>/DEFAULTS.md: what holds every day. Write only what differs.
7. data/plans/README.md (the data files and the goal-to-item trace), then `data/plans/<course>/items.csv`,
   wrongs.csv, errors.csv, days.csv.

## What you write

- `courses/<course>/uNN-N/dNNN.md` (the section folder keeps its old `u`), to the template.
- New rows in `items.csv` for every question the day uses, and in `wrongs.csv` for every wrong answer you expect,
  each with its error letter (`x` for any other wrong answer). Ids: `sNN-K<day>-n` worked example, `-F` fix-it,
  `-P` practice, `-C` challenge or extension, `-T` tool, `-X` exit. `stretch` is the unit number and `unit` the
  section (both columns lag their names). If the unit plan already wrote the exit rows, use them.
- Your day's `shows` cell in days.csv: each piece of the goal, then the exit and end-of-unit items that show it
  (data/plans/README.md). Write it before the exit, and write the exit to it.
- A days.csv change to make the minutes honest is allowed; say so in your report.

## Fixed facts

- Length and caps come from DEFAULTS.md and LESSON-DAY.md; the gate counts them.
- Every number is new: no exit or assessment item reuses a taught row's numbers, and your taught rows do not reuse
  exit, assessment or readiness numbers. Grep items.csv before keeping a pair.
- `version: draft 1, not ready, not yet taught`. `leans_on` names every outside piece by path; one that does not
  exist and is not needed to teach is `when it exists: <path>`, with the fallback said in the prose.
- No em dashes. "Curio Class" in full. No company names. No timer shown to a student. `credit: ours` unless you
  adapt CC BY, CC0 or public domain material.

## When your day has a base text

If your job brief names base-text lessons (docs/sources/BASE-TEXTS.md), read those lesson files in
`S:\CurioClass-sources\` (the `.md` and its `.prep.md`) after the plan. The plan still decides the day; the
lesson supplies moves. Keep its task ideas, the order of moves and the planned questions where they serve our
goal. Write everything in our voice and format, with new names, contexts and numbers. Cut any lean on lessons
our year has not taught yet. Fit our minutes. Take no photos, slides, links, routine labels or character names.
Credit: the short form in LESSON-DAY rule 4, once in the header and once in the Credit section, with one line
on what changed. Say in your report which parts came from the lesson and which are ours.

## The At home block

Write it last, from your finished day (format in LESSON-DAY.md; the gate checks the shape). Same goal, same
items, fewer of them. Write to a parent who has never taught: what to do with their hands and what the child
does. Every **Say.** is the class's planned question in the parent's words, with the answer to expect. A
**Swap.** for each thing a home lacks.

## What the expert reads found that no script can check

Run each on your own day before you hand in. The cheap read uses this list too.

1. **The trace is true.** Each item `shows` names really asks for that piece of the goal, a later step included.
2. **The exit from the examples alone.** Answer the exit using only the worked examples; teach any missing step.
3. **Each item tells its errors apart.** Work each targeted error's wrong answer; two that match cannot be told
   apart, so change the numbers or ask for the working.
4. **Rules are true in general.** Every rule, stop or trap you state holds beyond the day's numbers; a search can end.
5. **No example builds a habit the day later undoes**, and no example works only because its numbers are kind.
6. **Tomorrow is kept.** What your Tomorrow promises, the next day does, in its words; what the day before
   promised, yours does.
7. **No cue words** in practice meant to make the child choose, or in the exit.
8. **The key is honest.** Every wrong answer the prose names has its row; the letter really produces it; the
   accept rule takes every right form.
9. **Figures draw what the steps say**, and the student figure holds no answer.
10. **Materials agree** with the opener's supplies and the readiness branches with the opener's reteach.
11. **The minutes fit** a grade 4 class: count the questions in each part.
12. **The reason bar.** A "why" is met only when it says what the step does; the rule given back is not a reason.
13. **Asks before answers.** Each planned question comes before the screen or step that answers it.
14. **On grade.** Nothing needs a skill taught later in the scope and sequence, or a number off the grade's list.
15. **Shorter keeps the core**: never the fix-its that carry the day's errors, the trace items or the exit.

## Gates (run until 0 failures for your day)

    python -X utf8 scripts/plan.py check
    python -X utf8 scripts/lesson.py check
    python -X utf8 scripts/lesson.py build

Read the notes for your day too: each one is a question to answer, in the file or in your report. Open the built
`dNNN-teacher.html` and `dNNN-home.html` once and read them as the teacher and the parent would. Failures in
other days' files are not yours; report them and leave them.

## Report back (short)

The files you changed; the teacher, At home and student word counts and the sides from the gate; any days.csv
change; your day's notes and what you did with each; anything in the plan you found wrong or had to decide (one
line each); which of the checks above changed something; anything you could not do.
