# Section run: unit waterfall, two courses at a time

Agreed with Cory 2026-11-26. The script is `scripts/section_run.py`; this file is its spec and the one home for its rules.
It writes section plans (stage 5 of docs/COURSE-RUN.md) and takes each unit to green on the Desk Dashboard: plan,
plan data and answer-key report. Days are not part of this run.

## What it runs

Two lanes, one per subject, each its own process: English language arts and math. Each lane works one course at a
time, unit by unit, in the order below, so two courses are always in flight (one per subject).

| Lane | Courses, in order | Starts at |
|---|---|---|
| ela | english-language-arts-grade-4 to grade-12 | grade 4: its 30 section plans exist, so its units run plan data and key read only |
| math | math-grade-1 to math-grade-8, algebra-i, geometry, algebra-ii, precalculus, statistics, calculus | math-grade-1 unit 2 (unit 1 is green from the pilot) |

Math kindergarten is green and is not in the run. math-grade-4 is in the run (Cory 2026-11-26: the hold is no longer
needed); the old pilot paths `math-4` stay untouched as the L13 reference. A course with no unit plans (precalculus,
statistics and calculus today) stops its lane with the reason "no unit plans", logged; it never fails silently.

A unit whose section plans, items rows and key report all exist is skipped. A unit with some section plans written
(english-language-arts-grade-11, algebra-ii) writes only the missing ones; the refine reads all of them.

## The stages of one unit

| # | Stage | Model, effort | Runs as | Reads | Writes | Gate after |
|---|---|---|---|---|---|---|
| 0 | Texts (ELA only) | GPT-6.2 Sol, high | Codex, kit `text.txt` | unit plan, frame, ela-texts rows | courses/<c>/texts/, texts-out side file; the script merges it and rebuilds skeletons | none |
| 1 | Prep | GPT-6.2 Astra, xhigh | Codex | brief, unit plan, DEFAULTS, frame, approach doc, filtered ledger, skeletons, the newest "Changed for the next unit" list | build/sections/prep/<c>/u<uu>-<n>.md, one note per section | none (prep writes no repo file) |
| 2 | Write | GPT-6.2 Sol, high | Codex, kit `section.txt` plus the prep notes and the last "Changed" list | as the kit says | docs/courses/<c>/u<uu>-<n>.md, ledger rows | gate.py --course, new lines handed back once |
| 3 | Refine | Opus 5.5, high | Claude CLI | the plans, unit plan, skeletons, rules, filtered ledger | the plans in place, ledger rows, docs/reviews/<c>/section-refine-<c>-u<uu>-<date>.md ending in "Changed for the next unit" | gate.py --course |
| 3b | Texts, second pass (ELA only) | GPT-6.2 Sol, high | Codex, kit `text2.txt` | the refined plans | new text rows; the script merges them | none |
| 4 | Plan data | GPT-6.2 Sol, high | Codex, kit `data.txt` (ELA units over 5 sections in two halves) | as the kit says | data/plans/<c>/ rows, courses/<c>/u<uu>-*/ shared pieces | gate.py --course, new lines handed back once |
| 5 | Key read, narrow | Opus 5.5, high | Claude CLI | the key packet only (below), opening a shared piece or text only for an item that needs it | items.csv and wrongs.csv fixes, shared piece fixes, docs/reviews/<c>/answer-key-<c>-u<uu>-<date>.md | gate.py --course |

The "Changed for the next unit" list is part of stage 3, in the same Opus pass: what the refine changed that a
later unit must also do (a routine renamed, a fault class the writer keeps making, a term fixed). It is the last
heading of the refine report.

**The key packet** (stage 5) is cut by the script, so the key read never re-reads whole plans: the unit's items.csv
rows (every column), the wrongs.csv rows of those items, the unit's errors.csv register rows, every exit line of
each section plan's field 3 with its "Shape:" line, the list of the unit's shared pieces with their sizes, and for
ELA the text_id of each item with the path of its text. Saved as build/sections/packets/<c>-u<uu>.md.

## When each stage starts

- Within a course, stages 0, 2, 3, 3b, 4 and 5 run one after another, unit by unit. Only prep may overlap.
- The next unit's texts (ELA) and prep start when the current unit enters refine (stage 3). This holds across a
  course edge: the next course's unit 1 preps while the last unit of this course refines.
- The next unit's write waits for the current unit's key read to finish.
- Prep reads the newest "Changed" list that exists when it starts (usually two units back). The write always reads
  the previous unit's list, so nothing the refine found is missed.
- A unit's commits go through the shared git lock (`codex_lane.py` gitlock), only the course's own paths, one commit
  per stage, pushed.

## Stops (every stop logs a reason and can be resumed)

The run stops a lane, never skipping a stage, when:

1. `build/sections/STOP` (both lanes) or `build/sections/<subject>/STOP` (one lane) exists, checked before each stage.
2. A usage limit is reported by Codex or Claude: the lane stops cleanly and does not retry (Cory 2026-11-26: stop
   when tokens run out).
3. A stage fails twice: a job is resumed once when it goes silent or ends with no last message; a second failure
   stops the lane.
4. A gate exit 2 (changed course with no baseline), or new gate lines past the pileup rule (more than 10 plus one per
   section written in the course).
5. A course is missing an input (unit plans, days.csv, DEFAULTS.md).
6. Files outside the stage's allowed paths change: not committed, and the lane stops.
7. Codex refuses a stage's model (`model_not_found`): the lane stops at once, before any retry.
8. Any error in the script itself: caught, logged with its traceback, and the lane stops.
9. Every course of the lane is done.

Before every gated job the course gate runs first: a clean course stores its baseline, and a changed course with no
baseline stops the lane before a model call is spent on it.

On a stop the lane writes `build/sections/<subject>/STOPPED` (the time, the reason, how to resume), after any prep
running beside the stopped stage has ended. One process per lane: `RUNNING` holds its pid, and a second start is
refused while that process lives. Each stage marks `<stage>-start` before its model call and `<stage>` after its
commit. On a rerun, a stage that started but did not finish and whose output is already there (the plans, the refine
report, the key report) is gated and committed, not run again; one whose output is missing runs again. A key or
refine report counts as done only once git tracks it. The pileup counts live in `counts.json`, so they survive a
rerun. safe_write lock and temp files (`*.lock`, `*.tmp`) are git-ignored and never committed.

## Running it

    python -X utf8 scripts/section_run.py dry-run <subject> [<n units>]   every stage's prompt and command, no model calls
    python -X utf8 scripts/section_run.py run <subject>                   run the lane until a stop
    python -X utf8 scripts/section_run.py status                          per lane: last stage, any STOPPED reason, tokens

Each lane runs detached (its own terminal or background process) with keep-awake on. It refuses to start while the
old `codex_lane.py` lane of the same subject has no STOP file, so the two never write the same course.

**Before the first run:** the Claude CLI must be signed in once (`claude` then `/login`; the lead cannot do this).
The Claude stages use the bundled CLI with `-p --model claude-opus-5-5 --effort high --output-format json
--no-session-persistence` and a scoped `--allowedTools` list (read, edit, write, search and `python -X utf8`
commands); no permission mode is weakened.

## Cost log

`build/sections/<subject>/usage.csv`, one row per stage: time, course, unit, stage, model, effort, result, minutes,
tokens in, cached in, tokens out, reasoning out, cost in US dollars (Claude stages), new gate lines. `status` sums it
per stage and per unit.
