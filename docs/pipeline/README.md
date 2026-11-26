# The production pipeline

How lesson days are planned, written, read and fixed by several workers in one repository, one at a time. Any course
can use it. The build order above the day (progressions, frames, scopes and sequences, unit plans) is
docs/PRODUCTION-PATH.md; its scripts are in "Planning above the day" below.

## Planning above the day

| Step | Script and gate | Brief | Who now |
|---|---|---|---|
| Progressions | `scripts/progression.py` (in `plan.py check`) | progression-write, -read, -cross-read, -reconcile | Claude writes and reads; Codex reads |
| Course frames | `scripts/frame.py check`, `frame.py sync` (frames.csv, the calendar) | frame-write, frame-read, frame-reconcile | Claude writes and reads; Codex reads |
| Scope and sequence | `scripts/sequence.py check`; the long run `scripts/codex_scopes.py` | sequence-write, -read, -fix, -reconcile | Codex writes and fixes; Claude expert and Codex read |
| Unit plans | `scripts/unit_skeleton.py` (mechanical fields), `scripts/codex_units.py` (Codex fills the judgement fields), `scripts/unitplan.py check` | plan-codex (and -ela, -math, -science), plan-codex-read, plan-read | Codex writes and reads every plan; Claude expert reads and fix passes |
| Any Codex read | `scripts/codex_read.py <brief> <out>` | the read brief named | Codex, by script |
| Sensitivity, safety, answer key, text | | sensitivity-read | Fresh agents; there are no outside human readers (settled 2026-11-14, see DESK-ANSWERS) |

Sections, days and lessons run by docs/COURSE-RUN.md stages 5 and 6 (since 2026-11-20): per grade, section plans,
a plan read and fix, plan data and keys, ledger-gated day jobs of 4 to 6 days, a grade-close sample read and a
retool. The job templates are the versioned kit in docs/pipeline/kit/ and `scripts/coursegen.py` writes a run's
queue. The unit-jobs table below is the older day pipeline, kept as a record; it is not the current cadence.

## The pieces of the older turn queue (a record, not the current cadence)

The current cadence runs job files from `scripts/coursegen.py`; the lead launches each and commits (AGENTS.md, "Who
commits"). The pieces below belong to the turn queue, kept for the pilot that used it.

| Piece | What it is |
|---|---|
| [AGENTS.md](../../AGENTS.md) | The rules every worker reads first (Codex reads it on its own; CLAUDE.md points Claude to it). |
| `scripts/turn.py` | The turn lock and the queue. `start` takes the turn and prints the job brief; `end` runs the gates, commits, pushes and hands the turn back. Workers do no git themselves. |
| `data/pipeline/jobs.csv` | The queue: one row per job, with what it waits on, who took it and its commit. |
| `data/pipeline/turn.json` | Exists only while someone holds the turn. It lives in git, so a worker on another machine sees it after a pull. |
| `docs/pipeline/briefs/` | One brief per job kind, filled in by `turn.py` (course, unit, day, dates). |
| `scripts/pipeline_runner.py` | Optional: runs the queue unattended, starting each worker from `data/pipeline/workers.json`. |
| `data/pipeline/runs.csv` | One row per unattended run: worker, minutes, tries, tokens. |

## A unit's jobs, in order (the older day pipeline, not current)

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

`end` runs the one gate for the job's course (`scripts/gate.py --course`), compares the failures with those at
`start`, and keeps the turn with the worker while the job added one. A fix job must leave none at all. A job that cannot clear them ends with
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
data/plans/<course>/ (the README there), its frame, scope and sequence and unit plans, and a probe (a few days
written from finished unit plans and read the full way, docs/pipeline/PROBE-GUARD.md), because the gates and the
writer's brief are adapted from what the probe finds; a guard runs in every subject before full writing. The briefs
name math files only as examples; where a brief names a math-only file (the rubric, the progression), the course's
own file takes its place. Social studies runs the first probe (docs/HANDOFF.md).
