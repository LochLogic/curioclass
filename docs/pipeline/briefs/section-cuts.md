# Section cuts: the job

Curio Class (a free K-12 curriculum) plans each course as units, and each unit is to be split into **sections**: short
packages of 1 to 6 days, each later given its own section plan and teacher opener. Right now each unit in your brief is
held as one placeholder section (for example 3.1 covering all 15 days). Your job is only to propose where each section
starts and ends. You write no plans and edit no repository files.

## Input

Your brief (one markdown file) lists every unit to cut: its day table (day, kind, assess, goal, note) and any lines from
the unit plan that propose breaks or name multi-day work. If a unit is unclear from the brief alone, you may read its
unit plan at `S:\CurioClass\docs\courses\<course>\sNN.md` (NN = two-digit unit number). Read nothing else in the
repository, and never write to it.

Day kinds: Understanding (new idea taught), Fluency, Application, Check (assessment), Respond (re-teach and extend after a
check). `assess` = end (end-of-unit assessment), mid (mid-unit check), readiness, observe, course (course-level check).

## What makes a good cut

1. Each section is one coherent piece of learning: one idea, skill cluster, question, text, or investigation that a
   teacher could open with one page. Cut where the goal shifts, not to hit a number.
2. 3 to 5 days is the sweet spot; 1 to 6 is allowed. A 2-day section is fine when the content really is separate.
3. No new teaching (an Understanding day) after a mid check (assess `mid`) inside the same section: the mid check
   and any Respond or Check days that follow it close their section. The end-of-unit check and its Respond day sit in
   the last section of the unit; in ELA, end parts scored across the closing weeks may sit in the last two or three
   sections.
4. Never make a section of only Respond days.
5. Keep a single investigation, lab sequence, project, debate or seminar prep, a draft-and-revise writing cycle, or
   one text read across days together when you can. If keeping it whole needs more than 6 days, either cut at its
   most natural internal seam, or keep it whole and write `why` starting with `long:` plus the reason. Use `long:`
   rarely, only when a cut would truly break the work.
6. If the unit plan already proposes breaks, follow them unless they break a rule above; say so in `why`.
7. Number sections N.1, N.2, ... in day order (N = the unit number). Every day of the unit belongs to exactly one
   section, no gaps or overlaps.

## When it is a judgement call

If you cannot decide between two reasonable cuts, or the unit does not fit the rules (for example a check falls
mid-run of a project, or every option breaks something), still write your best proposal rows, but set `status` to
`decide` on every row of that unit and put the question and the options in `why` of its first row, briefly. Otherwise
`status` is `ok`. Expect most units to be `ok`.

## Output

Write a CSV (UTF-8, comma-separated, quote fields that contain commas) to the path you were given, with this exact
header and one row per proposed section:

    course,unit,section,first,last,title,status,why

- `unit` is the unit number (e.g. 3), `section` is e.g. 3.2, `first`/`last` are the course day numbers (inclusive).
- `title`: a plain, short name for the section, 3 to 8 words, sentence case, no em dashes.
- `why`: one short clause (e.g. "goal shifts from causes to effects", "keeps the day 24 to 27 investigation whole").

Then check your own file: every unit in the brief covered, day ranges contiguous from the unit's first to last day,
section numbers in order, no section over 6 days without `long:`. Reply with only: units done, how many `decide`,
and one line per `decide` unit with its question.

Style: never use em dashes anywhere.
