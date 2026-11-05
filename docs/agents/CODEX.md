# Codex as builder

**2026-11-04 (Cory): Codex is the primary builder and the phase 1 reviewer** (the cold CODEX-REVIEW.md pass in a new
chat); Claude's Refine lenses come after. The pilot notes below are history.

Codex does Build (step 1) and Polish (step 5) only. Everything else stays as REFINE.md: the integrator (the main Claude
session) writes the brief, three blind Claude lenses review, the integrator merges, fresh Claude agents run the exit
checks, the integrator closes, commits, pushes and deploys. First run: biased-bot, BR2 (BATCH-BR-LOG.md).

## Build-only runs Cory starts himself (2026-10-30)

One shared brief, docs/agents/CODEX-BUILD.md, needs no per-tool writing and adds rules against hanging. Cory runs Codex
interactively in the tool's own worktree, one tool at a time; the tool holds there, uncommitted, until a Claude session
has the budget for Refine. Polish is the costly round, so leave Codex budget for it.

Since 2026-10-30 Codex makes the images during the build, not after it, so art and layout fit together and later work
dials back rather than adds; people stay out and go to Gemini. Each tool then gets a cold review in a new Codex chat
(docs/agents/CODEX-REVIEW.md) that fixes what the lenses would find, one pass, to shrink Refine.
Since 2026-10-31 every chat shares one checkout, S:\CurioClass-codex on branch codex/queue, because a worktree per tool
meant 46 repo copies and each chat writes only its own tool. Cory pastes from S:\CurioClass-codex\_queue.txt, rebuilt from
what is on disk by `python scripts/codex_queue.py prompts`. A chat opened outside that project lands in Documents\Codex
and can't reach the tool, so every block tells it to stop there.
Compare Refine's finding counts on these tools with the two pilots before deciding the review step stays.

## Unattended runs (2026-11-04)

`python scripts/codex_runner.py` (Start Menu: "Codex Queue", scripts\Start-Codex-Queue.bat) does Cory's pasting while he
is away: each build and review block from _queue.txt runs as its own fresh `codex exec` session in S:\CurioClass-codex,
the same as a new chat. Reviews go first; a finished build makes its review eligible. Same limits as the paste file
(3 builds, 4 reviews, ports by slot); `--builds N --reviews N` runs fewer. Sessions start 2 minutes apart: two that
started at the same moment both failed the sandbox handshake on the first test and gave up within 3 minutes. One that
ends that fast without its file gets one fresh restart; a stall of 20 minutes gets the hung-command message and a
dropped turn gets "carry on" (both as resumes, at most 3), then it is logged FAILED for a person. A usage-limit
message stops new starts. Tools touched in the last 20 minutes and slots whose ports are busy are skipped, so it can
run beside hand-pasted chats, but it is meant for when nobody is pasting. Stop gently with an empty file
S:\CurioClass-codex\_runner\STOP. Log: _runner\summary.txt, one events file per session under _runner\<date>\.
Change a run without stopping it (from 2026-11-05 runs on): edit _runner\LIMITS.json (how many at once, and max_builds,
max_reviews, max_fixes, max_jobs; 0 means no limit). The runner re-reads it and scripts/codex_queue.py every 30 seconds,
so a raised cap or a tool added to QUEUE or FIX joins the run. Once the runner has ended, a new run is needed.

## Pulling tools in (2026-11-04)

The Codex checkout holds tools until they are reviewed. A tool with both `codex-report.md` and `codex-review.md`
moves to main: `git checkout codex/queue -- tools/<id>` in S:\CurioClass, then copy its gitignored `art/raw` and
`voice/raw` folders by hand, bundle with `CURIO_DRAFT=1` and run the checks. Skip a tool main already has at a later
stage (main's version wins). The first pull (commit 251925d9) brought in 47 tools.

A tool that is only built stays in the Codex checkout. scripts/board.py shows it in the CODEX column of the Review Desk
stats board (a concept or spec tool whose `codex-report.md` exists there), so the board counts it without pulling it.

Chrome profile folders under `_scratch` are junk and get deleted (1,226 went on 2026-11-04). The rest of a tool's
scratch evidence (screenshots, audit output) is kept until the tool ships, then may go.

Merge main into codex/queue after a pull so new builds use current engines.

## Fixes after Refine, and the brief upgrades (2026-11-04)

Measure first (docs/agents/MEASURE-FIRST.md): 4 Codex-reviewed tools still had 3 blockers and 6 to 14 should fix each
under a full Claude Refine, so Refine stays. What Codex's review missed was happy-path testing: a CPR score that rewarded
pausing, gamelan dated 1889, how-to lines never heard on the main path, a phone fix that still tangled. So, on Cory's
call, CODEX-BUILD.md and CODEX-REVIEW.md now ask for a Break it pass on every score and check, a main-path voice walk,
facts held to a named source, a Sensitivity flag, and every fix re-shot at the sizes it was seen at.

Fixes run in Codex too: `docs/agents/CODEX-FIX.md`, a third job kind in codex_runner.py (`--fixes`, two at once, ports
9920 and 9910). The tools are listed in `codex_queue.FIX`. Hand over: commit the merged refine.md in main, merge main
into codex/queue. Codex writes `polish.md`. Pull the tool back and run one Claude exit check, which re-tests every item:
Codex has claimed fixes that were not made. Round 2 renames polish.md to polish-r1.md.

Sensitivity: when a codex-review.md names something under `## Sensitivity`, run the Claude sensitivity agent before the
lenses (about 117k tokens on music-history-radio), and merge its findings with theirs.

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

- Sandbox (fixed 2026-10-28, after network-help-desk): drive.py and audit_tool.py fall back to `scripts/cdp_ws.py`
  when Codex's Python cannot see `websockets`, drive.py retries Chrome with `--in-process-gpu --no-sandbox` when it
  will not start, and audit_tool.py takes `--host-port <n>` so its iframe host fits the brief's one allowed port. The
  brief no longer needs to tell it to improvise any of these; it should say they exist.
- Tell it in the brief: start `codex-report.md` early and fill each section as its checks finish (the network-help-desk
  build lost its connection minutes before writing a report it had left to the end); keep the report under 200 lines
  (that one ran to 1406); close every Chrome and server it starts before it reports.

## Run

The build as biased-bot ran it (default model; run it in the background, timebox 2 hours):

    codex exec --json --sandbox workspace-write -C S:/CurioClass-codex-<id> --add-dir <scratch> -o <scratch>/codex-last.md - < <brief> > <scratch>/codex-events.jsonl

**Dropped streams.** "Reconnecting... 2/5" to "5/5" `error` events are normal: the next event is "Falling back from
WebSockets to HTTPS transport" and the run carries on (every resume of a long session starts this way). Do not stop a
run for them (the integrator stopped network-help-desk's first polish there by mistake and had to resume it). A turn
is lost only on a `turn.failed` event, or when the events log stops growing for about 20 minutes while no command is
in progress (the network-help-desk build sat on a hung command until its 2 hour timeout). Then stop the run and resume
the same session at once with a short prompt ("your connection dropped; carry on from where you were, finish the
report"), rather than waiting out the timebox. A `turn.failed` reading "Selected model is at capacity" (half-life-dice's
polish, 01:23) is the server, not the run: resume at once with the same short prompt naming what was left. When only
the closing audit is left, the integrator can run it instead of another Codex turn (half-life-dice's resume ran out its
hour on the audit).

The session id is the `thread_id` in the first events line (`thread.started`). Polish (and any later round) resumes the same session, so it keeps its
own context:

    codex exec resume -c sandbox_mode="workspace-write" -c 'sandbox_workspace_write.writable_roots=["<scratch>"]' --json -o <scratch>/codex-polish-last.md <session-id> - < <scratch>/polish-prompt.md

`resume` takes no `--add-dir`: without the `writable_roots` override the scratch folder is read-only on every resume
(network-help-desk's polish fell back to %TEMP% for all its evidence).

Polish prompt shape (biased-bot's, which worked): the review is `tools/<id>/refine.md`; fix every Should fix and every
Polish accepted item and apply the Settled calls; leave Spec open questions; which engine change (if any) is approved,
backward compatible, with the family doc updated and the other tools on that engine re-checked; keep voice/lines.json
equal to allLines(); re-bundle and re-check the Done-when list at the review sizes by driving the tool; write only
inside the tool folder (plus any approved engine files); don't edit refine.md; no git; then write `polish.md`, one line
per item. An exit-check FAIL goes back the same way with only the failed items.

After every run the integrator checks for Chromes left behind and stops only those whose command line holds the run's
scratch folder (PowerShell: `Get-CimInstance Win32_Process -Filter "Name='chrome.exe'" | Where-Object { $_.CommandLine
-like '*<scratch>*' } | ForEach-Object { Stop-Process -Id $_.ProcessId }`; the network-help-desk build left 18).

## Record

Tokens (input, cached, output) and wall time from the events log for each round, into the wave's log. Compare
blockers and should fix in round 1, exit rounds to PASS and integrator fixes against the wave average.

## What network-help-desk taught (2026-10-28)

- Messy run: 2 h 10 min (timeout plus a report-only resume) against biased-bot's 37 min; about 3% of the weekly Codex
  budget for the build alone (Cory). Most of the time went to sandbox workarounds (no websockets, Chrome flags, host
  port), now fixed in the scripts.
- Round 1: 0 blockers, 15 should fix after merge (Teaching 8, Play 11, Craft 6 before merge). Several of its PASS
  claims were wrong (no free sweep, status only after evidence, zero console errors, zero overlap leads). Read the
  report as claims, as before.
- Three of the biggest findings came from the spec, not the build (the kind printed on the cards, Q4 answers naming
  the cause, a free "Right cause"). Cory changed the spec after round 1.

## What biased-bot taught

- Its build was the cleanest of BR2 round 1 (0 blockers, 9 should fix), so the brief works.
- It claimed every polish item done, but exit round 2 failed and one of its fixes regressed (welcome cut). Read
  `polish.md` as claims; the exit check is still needed.
- About 14M input tokens to build and 30M a polish round, almost all cached; 37 minutes to build.
- Its states file and scratch habits are the two things to brief harder.

Cory's queue: `scripts/codex_queue.py`. Left out on purpose:
tools waiting on desk answers, tools needing a kit engine that doesn't exist yet, sensitive or cultural topics, and the
three super tools with unanswered cards.
