# The production pipeline

How lesson days are planned, written, read and fixed by several workers in one repository, one at a time.
Started 2026-11-12 for grade 4 math units 4 to 8. Written so any course can use it.

## The pieces

| Piece | What it is |
|---|---|
| [AGENTS.md](../../AGENTS.md) | The rules every worker reads first (Codex reads it on its own; CLAUDE.md points Claude to it). |
| `scripts/turn.py` | The turn lock and the queue. `start` takes the turn and prints the job brief; `end` runs the gates, commits, pushes and hands the turn back. Workers do no git themselves. |
| `data/pipeline/jobs.csv` | The queue: one row per job, with what it waits on, who took it and its commit. |
| `data/pipeline/turn.json` | Exists only while someone holds the turn. It lives in git, so a worker on another machine sees it after a pull. |
| `docs/pipeline/briefs/` | One brief per job kind, filled in by `turn.py` (course, unit, day, dates). |
| `scripts/pipeline_runner.py` | Optional: runs the queue unattended, starting each worker from `data/pipeline/workers.json`. |
| `data/pipeline/runs.csv` | One row per unattended run: worker, minutes, tries, tokens. |

## A unit's jobs, in order

`turn.py add-unit <course> <unit> <first>-<last>` queues the first three; the rest are queued when plan data ends.

| Job | Role | Who now | What |
|---|---|---|---|
| plan | planner | lead Claude | The unit plan (and section plans) in prose. |
| plan-read | expert | lead Claude (fresh agent) | A cold expert read of the plan before any day is written. |
| plan-data | planner | lead Claude | Apply the plan read; the plan into data; shared pieces. |
| write, one per day | writer | Codex | Days in order, each reading the day before. |
| cheap | cheap | Sara's Claude | A cheap focused read of every day in the unit. |
| expert | expert | lead Claude (fresh agents) | An expert cold read of every day, reading the cheap read last. |
| fix | fixer | lead Claude | Apply both reads; process fixes first; gates to 0. |
| measure | lead | lead Claude | REVIEW-CADENCE, COST, HANDOFF. |

Who does which role is a setting, not a rule: any worker can take any role with `start <name> --role <role>`.

## The gates at `end`

`end` runs `plan.py check` and `lesson.py check`, compares the failures with those at `start`, and keeps the turn
with the worker while the job added one. A fix job must leave none at all. A job that cannot clear them ends with
`--fail "why"`, which hands the turn back and leaves the job for a person.

## Taking a job by hand (paste mode)

`python -X utf8 scripts/turn.py next --role writer` prints the line to paste into a new chat, for example:

> Read AGENTS.md, then run `python -X utf8 scripts/turn.py start codex --job math-4-d025-write`, do the job it
> prints, and finish with `python -X utf8 scripts/turn.py end codex`.

One line per job; every chat starts fresh. A worker in a sandbox with no network (Codex in workspace-write) cannot
pull or push, so in paste mode a person runs `start` and `end` around the chat, or the runner does.

## Running it unattended

`python -X utf8 scripts/pipeline_runner.py` takes the next ready job whose role an enabled worker serves, starts that
worker with the brief, ends the turn, and repeats. Gate failures get one more try with the failures in the prompt,
then the job is failed and the runner stops. A worker that quits within two minutes or reports a usage limit stops
the runner. Stop it gently with an empty file `data/pipeline/runner/STOP`. `--dry` shows what it would run;
`--only writer` runs one role; `--max N` stops after N jobs.

Workers today (data/pipeline/workers.json):
- **codex** (writer): on. Uses the Codex command line already installed for the tool queue.
- **sara** (cheap reads): off until the Claude command line is installed. Sara signs in to her own account once,
  herself, in its own settings folder (`CLAUDE_CONFIG_DIR`), so her runs bill to her account. Nobody else signs in
  for her.
- **claude** (planner, expert, fixer, lead): off until the Claude command line is installed. Until then the lead
  session takes these jobs by hand.

## Beyond math

Nothing in turn.py, the runner or the job order is about math. A new course needs: its plan data in
data/plans/<course>/ (the README there), a DEFAULTS.md and a written, read pilot unit, because the gates and the
writer's brief are built from what the expert reads of that pilot find. The briefs name math files only as
examples; where a brief names a math-only file (the rubric, the progression), the course's own file takes its place.
Grade 6 English language arts and grade 4 science are the next pilots (docs/HANDOFF.md).
