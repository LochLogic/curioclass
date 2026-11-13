# Brief: write one lesson day of a Curio Class course

The brief handed to an agent that writes one day. First used for the pilot section 11.1 of grade 4 math (days 89
to 93); updated 2026-11-12 to the locked words (docs/GLOSSARY.md), the At home block and the expert-only checks
from units 1 and 9 (docs/pilots/REVIEW-CADENCE.md). The template is docs/courses/LESSON-DAY.md; this brief does
not repeat it, it says how to work and what to check before you hand in.

You are writing ONE day file in the Curio Class repository (your working copy is a git worktree of S:\CurioClass;
work only inside it, never in S:\CurioClass itself). Curio Class is a free K-12 curriculum site. Your token use is
measured as the cost of one day, so work directly: read what you need, write, run the gates, fix, stop. Do not
commit, push, or edit anything outside the files named below.

## Read first (in this order)

1. docs/courses/LESSON-DAY.md: the template (approved). Every rule there binds you, the At home block included.
2. courses/math-4/u11-1/d090.md: the worked case. Match its shape, headings, tone and density. Day 93 is the
   worked case for an assessment day.
3. The unit plan, `docs/courses/<course>/sNN.md` (the file name keeps its old `s`): your day's row in "U6. Days",
   and sections 2, 5, 6, U3, U7 to U10. Then the section plan and the section opener in your section folder.
4. docs/courses/<course>/DEFAULTS.md: what holds every day. Write only what differs.
5. data/plans/README.md (the data files), then `data/plans/<course>/items.csv`, wrongs.csv, errors.csv, days.csv.

## What you write

- `courses/<course>/uNN-N/dNNN.md` (the section folder keeps its old `u`), to the template.
- New rows in `items.csv` (and `wrongs.csv` for every wrong answer you expect) for every question the day uses.
  Ids keep their old letters: `sNN-K<day>-n` worked example, `-F` fix-it, `-P` practice, `-C` challenge or
  extension, `-T` tool, `-X` exit. `check` is example, fix, practice, challenge, tool or exit; `stretch` is the
  unit number and `unit` the section (both columns lag their names). Every keyed row has a compute cell that
  reproduces its value; worked examples and fix-its carry `figure` and `steps` as day 90's do. If the unit plan
  already wrote the exit rows, use them and give each its `path` (`paper`, or `tool` for the tool's own exit).
- If you change a days.csv row to make the minutes honest (as day 90 did), say so in your report.

## Fixed facts

- The day's length is in DEFAULTS.md (grade 4 math: 60 minutes, warm-up 5); the part after the warm-up matches
  days.csv `opens_min`; an assessment day's parts follow `check_min`.
- Caps: teacher prose 900 words (500 on an assessment day), Before class 80, At home 170 (apart from the 900),
  student page as DEFAULTS.md says (grade 4 math: 350 a student reads, questions included, two sides, no
  sentence over 15 words).
- Every number is new: no exit question or assessment item reuses the numbers of a taught row, and your taught
  rows do not reuse the numbers of exit, end-of-unit assessment or readiness rows, or other days' rows. Others may
  be writing the next days at the same time: pick numbers unlikely to collide.
- `version: draft 1, not ready, not yet taught`. `leans_on` names every outside piece by path (the section opener,
  the record sheet, a sheet from another unit, the tool); one that does not exist and is not needed to teach is
  `when it exists: <path>`, with the fallback said in the prose.
- No em dashes. "Curio Class" in full. No company names. No timer shown to a student. `credit: ours` unless you
  adapt CC BY, CC0 or public domain material. Word Wall cards are named in plain words under Words and supports.

## The At home block

Write it last, from your finished day: a 30 to 40 minute path for one parent and one child (an assessment day:
the assessment, then going over it one to one, about 45). LESSON-DAY.md, "The At home block", has the format; the
gate checks it. What the gate cannot check is yours:

- Same goal, same items, fewer of them. Keep a worked example, the fix-its that carry the day's errors, a little
  practice and the exit ticket; drop the warm-up sheet, the tool, the third of three, the challenge, the groups.
- Write to a parent who has never taught. Say what to do with their hands and what the child does, not why.
- Every **Say.** is the class's planned question or partner check, turned to the parent's words, with the answer
  to expect. If the class checks in pairs, the parent is the partner.
- A **Swap.** for each thing named in the materials that a home lacks: tiles become coins or paper squares, grid
  paper becomes squares ruled on plain paper, the projector becomes the page itself, a string loop a short string.

## What the expert reads found: check your own day before you hand in

The gates catch the mechanical repeats. These are the kinds only an expert caught on units 1, 9 and 3; run each on
your own day and fix what you find. Cheap reads use this list as their repeat checklist.

1. **Rework the exit with only what the examples showed.** Cover everything but the worked examples and answer
   the exit ticket from them alone. If a step is needed that no example showed, teach it or change the exit.
2. **Each item tells its errors apart.** For every question that targets two errors, work out each error's
   wrong answer. Two errors that give the same number cannot be told apart: change the numbers.
3. **A search can end.** Any "find all" or "keep going until" has a stop the child can recognize.
4. **No example builds a habit the day later undoes.** Read the examples against the fix-its and the exit: an
   example that only works because its numbers are kind teaches the shortcut the fix-it then marks wrong.
5. **The hand-offs both ways.** Your Tomorrow names what the next day picks up, and the next day's file does it;
   the day before's Tomorrow is picked up in yours.
6. **Cue words.** Practice meant to make the child choose does not give it away with "covers" or "around".
7. **Page fit and blanks.** The student page prints on two sides with room to write every answer asked for.
8. **The key against the data.** Every wrong answer the prose names has a row in wrongs.csv, with its error letter.
9. **Figures draw what the steps say.** Every cut, point or line a step names is on the display and key figure;
   the student figure holds no answer (use `then` and `ask=` for what only the key shows).
10. **Student stems are the child's words.** No plan framing ("No line given", "No drawing"), no quote marks,
    no frame that names the method, and room to write each "why" or each renaming.
11. **Numbers new to checks.** Exits, written tasks and the assessment use no pair or equivalence a taught row
    on an earlier day used; grep items.csv before keeping one.
12. **Materials named where used.** Every strip, card or sheet a part hands out is in that day's materials and
    the opener's supplies, and every opener sheet is used by a day.
13. **One letter per wrong answer.** Where two errors (D and A, D and G) give the same sign, the item asks for
    the working that tells them apart, and wrongs.csv has a row for each.

## Gates (run until 0 failures for your day)

    python -X utf8 scripts/plan.py check
    python -X utf8 scripts/lesson.py check
    python -X utf8 scripts/lesson.py build

`lesson.py check` also prints the student page with Chrome to count its sides. Open the built
`dNNN-teacher.html` and `dNNN-home.html` once and read them as the teacher and the parent would. Failures in other
days' files are not yours; leave them.

## Report back (short)

The worktree path; the files you changed; the teacher, At home and student word counts and the sides from the
gate; any days.csv change; anything in the plan you found wrong or had to decide (one line each); which of the
self-checks changed something; anything you could not do.
