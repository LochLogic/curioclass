# Codex as builder (pilot)

Codex does Build (step 1) and Polish (step 5) only. Everything else stays as REFINE.md: the integrator (the main Claude
session) writes the brief, three blind Claude lenses review, the integrator merges, fresh Claude agents run the exit
checks, the integrator closes, commits, pushes and deploys. First run: biased-bot, BR2 (BATCH-BR-LOG.md).

## Set up

- Its own worktree and branch off main: `git worktree add S:/CurioClass-codex-<id> -b codex/<id> origin/main`.
- Its own scratch folder outside the repo (`S:/CurioClass-codex-scratch/<id>/`), its own Chrome ports and host port.
- Write the brief in the tool folder as `CODEX-BRIEF.md`. Model: `tools/biased-bot/CODEX-BRIEF.md` (ground rules,
  reading order, the rules quoted from BUILD.md, TOOL-CONTRACT, BASELINE, STANDARDS and POLISH, the family engine,
  the files to make, exact check commands, the BUILD.md wave lessons as a self-check list, the report format).
  Since biased-bot, also tell it to:
  - write `audit-states.json` (BUILD.md) and run `python scripts/audit_tool.py <id> <scratch>/audit --port <its
    port> --profile <its scratch>/chrome-prof`, answering every lead in `codex-report.md`;
  - keep every screenshot, Chrome profile and temporary script in its scratch folder or %TEMP%, never the tool folder
    (its sandbox cannot delete files afterwards, so anything it leaves there stays);
  - for an engine change it wants, list it under `## Engine changes wanted` in handoff.md and work around it; the
    integrator approves it in the polish prompt.

## Run

The build as biased-bot ran it (default model; run it in the background, timebox 2 hours):

    codex exec --json --sandbox workspace-write -C S:/CurioClass-codex-<id> --add-dir <scratch> -o <scratch>/codex-last.md - < <brief> > <scratch>/codex-events.jsonl

The session id is the `thread_id` in the first events line (`thread.started`). Polish (and any later round) resumes the same session, so it keeps its
own context:

    codex exec resume -c sandbox_mode="workspace-write" --json -o <scratch>/codex-polish-last.md <session-id> - < <scratch>/polish-prompt.md

Polish prompt shape (biased-bot's, which worked): the review is `tools/<id>/refine.md`; fix every Should fix and every
Polish accepted item and apply the Settled calls; leave Spec open questions; which engine change (if any) is approved,
backward compatible, with the family doc updated and the other tools on that engine re-checked; keep voice/lines.json
equal to allLines(); re-bundle and re-check the Done-when list at the review sizes by driving the tool; write only
inside the tool folder (plus any approved engine files); don't edit refine.md; no git; then write `polish.md`, one line
per item. An exit-check FAIL goes back the same way with only the failed items.

## Record

Tokens (input, cached, output) and wall time from the events log for each round, into the wave's log. Compare
blockers and should fix in round 1, exit rounds to PASS and integrator fixes against the wave average.

## What biased-bot taught

- Its build was the cleanest of BR2 round 1 (0 blockers, 9 should fix), so the brief works.
- It claimed every polish item done, but exit round 2 failed and one of its fixes regressed (welcome cut). Read
  `polish.md` as claims; the exit check is still needed.
- About 14M input tokens to build and 30M a polish round, almost all cached; 37 minutes to build.
- Its states file and scratch habits are the two things to brief harder.
