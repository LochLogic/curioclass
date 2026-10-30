# Codex build brief, any tool (Curio Class)

You are building ONE tool for Curio Class (curioclass.org), a free, public K-12 site of interactive classroom tools.
Each tool is one self-contained HTML file that a teacher projects or a student opens on a school laptop. Three blind
reviewers will check your work later, so build it as if it ships to real students tomorrow.

The tool id is in the prompt that sent you here. `<id>` below means that id. Scratch means
`S:/CurioClass-codex-scratch/<id>`. The repo root is this worktree.

**This run is Build only.** When the report is written, stop and wait. Do not start a polish round, and do not commit.
The tool holds on this branch until review.

## Ground rules

- Write only inside `tools/<id>/`. Not `kit/`, `docs/`, `scripts/` or other tools. No git commits, branch changes or stash.
- If a kit engine needs a change, do not make it. Work around it in the tool and list the change in `handoff.md` under
  `## Engine changes wanted`: the file, the function, the exact change and why.
- If the spec is wrong or impossible, build everything else and say so in `handoff.md` and the report. Do not improvise.
- Do not draw, generate, download or record anything. `art/prompts.json` and any images already there stay as they are.
  Use `art:<name>` tokens for the names in prompts.json; draft builds show labeled placeholders for missing images.
- Write "Curio Class", never "Curio" alone. Never use an em dash anywhere: code comments, UI text, notes, lines, reports.
- The tool makes no network requests. You need no internet.
- Screenshots, Chrome profiles, shots files, audit output and temporary scripts go in Scratch or %TEMP%, never the repo.
  Your sandbox cannot delete files afterwards, so anything left in the tool folder stays.
- Chrome debugging ports 9990 to 9997 and the host server on 8795, only. Every Chrome uses `--mute-audio` (drive.py does).
  drive.py and audit_tool.py already handle a missing `websockets` and a Chrome that will not start; do not work around them.

## Do not hang

Past builds lost hours to one stuck command and to re-running every check at the end. So:

1. **Start the report early.** Create `tools/<id>/codex-report.md` as soon as the first version bundles, and fill each
   section as its check finishes. Keep it under 200 lines.
2. **Put a time limit on every command** you run: 2 minutes for a bundle, 5 for a drive.py batch, 30 for the audit.
   A command that hits its limit is stopped and retried once, smaller. If it stops again, write it under Left open and
   move on. Never wait on a command with no limit.
3. **Nothing long-lived in the foreground.** The `--host` server starts in the background and stops right after its
   shots. Keep drive.py batches to about 12 shots.
4. **Shoot once, late.** Work in small checks on the size you are fixing. Do the full run of every size only once, near
   the end. After that, re-shoot only what a fix touched. Do not re-run the whole set after a small fix.
5. **Run the audit once, last.** Answer its leads in the report. If it has not finished in 30 minutes, stop it, say so
   in the report and finish. The reviewer can run it.
6. **Close every Chrome and server you start**, each time, before the next step.
7. **If you are stuck on one problem for more than about 20 minutes,** write it under Left open and go on to the next.

## Read, in this order

1. `docs/agents/STANDARDS.md`. Where anything differs, it wins.
2. `tools/<id>/spec.md`, every line, before you write anything. It is the source of truth. Build what it says, nothing more.
3. `docs/agents/BUILD.md`, all of it, including its wave lessons. Those are the repeat review findings, so each one is a
   check you must do. It lists the files to make.
4. `docs/agents/decisions/BASELINE.md`, `docs/TOOL-CONTRACT.md`, `docs/KIT.md` (above all "Voice: Curio.voice") and `docs/POLISH.md`.
5. `kit/starter/src.html`: start from a copy. Skim `kit/curio.js` and `kit/curio.css`, and use them instead of re-implementing anything.
6. If the spec names a family: `docs/families/<family>.md` and its engine file, in full. Use the engine, do not rewrite it.
7. `python scripts/neighbors.py <id>`: open one built neighbor (`src.html`, `handoff.md`, `refine.md`) to see the level of
   care reviewers expect. Do not copy its look, scene, voice or palette.

Before building, recompute every number in the spec's Sources in a small script in Scratch. If your numbers differ,
trust the computation, say what differs in the report, and leave the spec alone.

## Files to make in `tools/<id>/`

As BUILD.md lists: `src.html`, `tool.draft.json` (`"stage": "built"`), `notes.md`, `voice/lines.json`,
`audit-states.json`, `handoff.md`, plus `codex-report.md`. Leave out `art/prompts.json` if it already exists.
`notes.md` opens with `## What it teaches`, `## Key skills` and `## Support at home`, as BUILD.md says. The bundle
`<id>.html` is generated and git-ignored. Delete `host.html` when you finish, or say you could not.

## Check your work (from the repo root)

1. `$env:CURIO_DRAFT=1; python scripts/bundle_tool.py <id>`: bundles cleanly, under 2 MB.
2. `python scripts/drive.py <id> <Scratch>/shots.json <Scratch>/frames --port 9990 --profile <Scratch>/chrome-prof`. The header
   of `scripts/drive.py` gives the shots format. Use held clicks (`"hold": 0.12`) for anything with voice and real drags
   for dragging. There must be no console errors, warnings or exceptions.
3. 375 wide: `python scripts/drive.py <id> --host 8795` in the background, then shots at `http://127.0.0.1:8795/host.html?w=375&h=812`.
4. Cover every STANDARDS size, every mode, each extreme in POLISH.md, Motion off, a grayscale frame and a keyboard-only run.
5. Open and look at every PNG you shot. Fix overlaps, clipping, unreadable text and any "Done when" that fails.
6. Voice: at a 2 s tap pace with held clicks, read `__tool.vlog` and check the STANDARDS voice rules.
7. Last: `python scripts/audit_tool.py <id> <Scratch>/audit --port 9991 --profile <Scratch>/chrome-prof-audit`.

## Report: `tools/<id>/codex-report.md`

```
# Codex report: <id>
## Built
## Numbers check
## Done when          (each spec item: PASS or FAIL, with evidence)
## Wave lessons       (each BUILD.md lesson: PASS or FAIL, and how you checked)
## Audit leads        (each lead: fixed, or why not; or "audit not finished")
## Frames looked at
## Engine changes wanted
## Left open
```

Be honest: a FAIL you report is worth more than a PASS you did not check. When the report is written, say "Build done"
and stop.
