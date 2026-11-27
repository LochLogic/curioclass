# Curio Class section run

Cory set the section run cadence on November 27, 2026. One process per subject writes section plans and their data, then reviews the finished units. Day writing is a later stage of [the course run](../COURSE-RUN.md).

| Lane | Course order |
|---|---|
| ELA | English language arts grades 4 through 12 |
| Math | Math grades 1 through 8, algebra I, geometry, algebra II, precalculus, statistics, calculus |

Math kindergarten and the old `math-4` pilot are outside this run. The grade 1 pilot unit is already green. The course inventory ends at the first missing input, including a missing unit plan, frame, DEFAULTS.md or days.csv. The lane processes the units before that course and reports the reason after the review queue drains.

## Codex stages

| Stage | Model and effort | Work and resume rule |
|---|---|---|
| `texts` (ELA) | GPT-6.2 Sol, high | Before writing missing plans, settle the unit's open text rows with the text kit. Merge the side file and rebuild the skeletons. Skip a finished pass or a unit with no open texts. |
| `prep` | GPT-6.2 Astra, xhigh | Read the brief, rules, unit plan, skeletons, approach, filtered ledger and feedback. Write a note for each section under `build/sections/prep/<course>/`. Reuse completed notes. |
| `write` | GPT-6.2 Sol, high | Use the section kit, prep notes and current feedback. Write only missing section plans and their ledger rows. Gate and commit each group. If an interrupted write landed all its plans, gate and commit them on resume. |
| `crefine` | GPT-6.2 Astra, xhigh | Review every section of a unit this lane wrote, including any sections that predated a partial write. Fix the plans and ledger. Write `docs/reviews/<course>/section-crefine-<course>-u<uu>-<date>.md` with the fault table, plan points and final `## Changed for the next unit` list. Recover a complete report through the gate and commit. An existing Opus refine report satisfies this stage. |
| `texts2` (ELA) | GPT-6.2 Sol, high | After a unit write, use the second text kit to fill commissioned texts the section plans still need. Merge the rows and rebuild the skeletons. |
| `data` | GPT-6.2 Sol, high | Use the data kit for the unit's rows and shared pieces. ELA units with more than five sections use two separately gated and committed halves. Reuse completed data and retain preexisting unit items when the lane did no writing or data work on the unit. |

A unit whose plans all predate the run goes directly to data. The lane records `<course>:u<uu>:codex-done` in `done.txt` when its Codex work is complete. Prep writes local notes. The text stages commit the text files and merged rows. The other stages that edit course content run the course gate before the job to establish its baseline and again afterward. The lane hands new lines back once and commits through the shared lock, restricted to the stage's paths. A held turn delays the commit. Each commit is pushed.

## Claude review and green units

After each Codex unit, the lane takes at most one eligible unit from the front of the review queue. One background thread runs the next unit's ELA texts, if needed, and then its prep beside that review, including across a course boundary. The lane joins the thread before another foreground job. At the end of the course list it reviews the remaining queue in order.

The `claude` stage uses Opus 5.5 at high effort. In one session it solves the narrow key packet cold, checks the full section plans and ledger, and reconciles all fixes. It may edit the unit's plans, ledger rows, shared pieces and its own items, wrongs, handbacks, errors and sources rows. It writes both reports in `docs/reviews/<course>/` under the existing `section-refine-<course>-u<uu>-<date>.md` and `answer-key-<course>-u<uu>-<date>.md` names. Each ends with `## Changed for the next unit` and a list or `None.`. With an existing old-chain Opus refine report, the lane runs only the narrow `key` job. Claude receives any new gate lines in one fix call.

The packet lives at `build/sections/packets/<course>-u<uu>.md`. It contains the judged items with all columns, their wrong answers, the unit's error register, field 3 exit lines and shapes, shared-piece paths and sizes, and ELA text IDs and paths. During the key read, Opus opens a text, shared piece or day block only when an item requires it. It solves changed items cold again.

A **green** unit has all its plans, unit items and a committed answer-key report. An interrupted combined pass still owes both reports and its gate. An existing green unit needs no further model call.

## Carrying changes forward

The lane stores each nonempty Claude list once in `build/sections/<subject>/carry.json`, with its source unit, text, time and `applied_to` units. Prep and write receive the previous unit's Codex refine list (the old Opus list when it is the only one) plus same-course Claude lists awaiting prep. The lane removes duplicate lines and puts newer lists last. It records which lists a prep saw so its writer also receives them after a restart. A list that arrives while prep is running can still reach the write.

At each boundary, including during the final drain, one `sweep` job per affected course uses GPT-6.2 Sol at high effort on the Codex-complete units still awaiting review. The prompt assigns each list to its eligible units, excludes the source and any unit under review, and limits edits to those units' plans, ledger entries and data rows. The job applies a lesson where it fits, preserves content that a gate cannot judge, and passes through the gate and commit before the lane records `applied_to`. A full write that already received the list needs no sweep for it. The unit's Claude prompt names its swept lists for verification.

## Limits, stops and resume

- A Claude usage limit keeps the same unit at the front. The lane saves the reset time locally and continues Codex work. An unreadable or missing reset time gives a 60-minute cooldown. A sign-in failure stops the lane.
- A Codex usage limit switches the lane to reviewing the backlog. It honors Claude cooldowns and retries the pending Codex work at hourly intervals. When Codex is unavailable for a sweep, Opus sees outstanding lessons for its unit in the already scheduled review. A Codex denial with an empty queue writes the usual stop note. A limited attempt restores its unfinished edits to the course files it owns before another unit uses them.
- During a cooldown with no eligible work, the lane sleeps and checks the stop files at least every 30 seconds. `build/sections/STOP` stops both lanes and `build/sections/<subject>/STOP` stops one at its next check. A background job joins before exit.
- A twice-failed model job, a refused Codex model, a changed course with no gate baseline, unexpected course paths, or a script error stops the lane with a reason. The gate pileup limit is more than ten lines plus one per section written in the course, where lines means the course's failing lines now (index-reports orphans left out) minus its level when the lane first read it (`start`). A line left by several passes counts once. Its counters persist in `counts.json`.
- A stop writes `build/sections/<subject>/STOPPED` with the reason and resume command. On restart, the lane reconstructs the FIFO queue from the completed stages and files, including data finished by the old chain. Stage start and completion marks distinguish an unfinished review from a finished report. Landed outputs are gated and committed where complete. Missing outputs resume the applicable job. A limited or interrupted sweep stays eligible until its applications are recorded.

## Commands and state

    python -X utf8 scripts/section_run.py dry-run <subject> [<units>]
    python -X utf8 scripts/section_run.py run <subject>
    python -X utf8 scripts/section_run.py status

A dry run saves prompts, rendered kit jobs, packets and state under the subject's `dry/` directory. It makes no model calls, gate runs or commits. It supplies one example carry list to exercise the sweep. In a bounded preview of two or more units, if the first units all have plans, the last sample slot shows the first unit needing a write when one exists.

Each live subject has its own `RUNNING` PID and keeps the machine awake. Start it in its own terminal or detached process. An active section lane or an older `codex_lane.py` subject lane without a stop file prevents a second start. Sign in to the bundled Claude CLI before the first run. It uses a scoped tool list and a session ID so a gate fix can resume the review.

`status` reads each lane's last log line, stop reason, Codex-complete total (including green), green count, backlog length, active Claude cooldown and number of carry lists still awaiting a prep or sweep. It totals usage by stage. `usage.csv` records each model call's course, unit, stage, model, effort, result, minutes, input and output token counts, and reported Claude cost.
