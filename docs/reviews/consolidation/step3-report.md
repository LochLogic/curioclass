# Consolidation step 3: cleanup (2026-11-25)

Step 3 of docs/CONSOLIDATION-PLAN.md, run serially, one commit per sub-step. Everything moved went through
S:\CurioClass-archive (INDEX.csv rows with sha256), nothing was deleted. What can be deleted is parked in
S:\CurioClass-archive\_to-delete\ for Cory.

## Commits

| Sub-step | Commit | What |
|---|---|---|
| 3.1 stale plan docs, doc map, stashes | 97899814b | POLISH, PHASE0, PHASE1, PHASE2, BREAK-BOX-PLAN folded into their owners (TOOL-CONTRACT, VISION, APPROACH, agents/SPEC, SUPPLY-CLOSET-PLAN), then archived with ART-STATUS; MAP-RESEARCH moved to docs/reviews; artstatus.py writes only with `--write`; HANDOFF gained a doc map; 2 stashes exported as patches and dropped |
| 3.2 sibling-folder paths | fedfb3d8b | codex_scopes runs in `_scopes/` (git-ignored); budget read moved to scripts/codex_budget.py; codex queue, runner, draft and Sara-spec launchers archived; board.py no longer reads the Codex folder |
| 3.3 worktrees and branches | a92c0419c | AGENTS.md and HANDOFF drop the spec2 rule; spec2 and Codex rows gone from the folder table; briefs and kit no longer name spec2; CODEX-BUILD, CODEX-FIX, CODEX-REVIEW and GUEST-SPEC marked paused |
| 3.4 loose folders | dbcde1c68 | later.csv L113 (Ripple leftovers); CALIBRATION.md notes the Gemini folder is archived |
| 3.5 archive README and zip | (no repo change) | S:\CurioClass-archive\README.md written; old worktree folder zipped |

## Git

- One checkout now: S:\CurioClass on `main`. Every other branch was deleted locally and on GitHub after being kept as
  a tag: `archive/draft-codex`, `archive/codex-queue`, `archive/spec-sara`, `archive/electives-frames-2026-11-16`,
  `archive/agent-a137c140`, `archive/agy-build`, `archive/audit-states`, `archive/audit-states-local`,
  `archive/claude-hopeful-dirac`, `archive/codex-biased-bot` (10 tags, all pushed).
- `archive/agy-build` holds AGY-BUILD.md and 44 Flash research packets that main had archived on purpose; nothing
  there is lost work.
- Stashes: `stashes-2026-11-25\_stash-export\` holds both as patches, each checked by rebuilding the stash tree
  exactly from its base commit. The 2026-10-27 stash holds 16 closet/words webp images that never reached main;
  they were not touched (closet/words is off limits) and the patch keeps them.

## Archive buckets (INDEX.csv, 30 rows dated 2026-11-25)

| Bucket | Rows | Holds |
|---|---|---|
| plan-docs-2026-11-25 | 6 | the folded plan docs and ART-STATUS |
| stashes-2026-11-25 | 2 | stash patches |
| retired-scripts-2026-11-25 | 9 | codex queue/runner/draft, launchers, the Codex Queue Start Menu shortcut, the draft preamble |
| worktrees-2026-11-25 | 4 | CurioClass-spec2, the electives worktree, .claude/worktrees/agent-a137c140417b1a414, and the kept files of S:\CurioClass-codex (145,492 files, 32.18 GB) |
| loose-folders-2026-11-25 | 6 | CurioClass-agy, CurioClass-gemini, S:\dq, S:\tmp, S:\ladder-tmp-x, the Antigravity scratch copy |
| (skipped) | 2 | see below |
| worktrees-2026-11-12.zip | 1 | added by the zip in 3.5 |

What each loose folder held, checked against main before moving:

- **CurioClass-agy:** 4 files, all identical to main.
- **CurioClass-gemini:** the reports are already in docs/reviews (`*-gemini-<date>.md`); only the raw calibration
  replies were unique, and they are kept in the archive.
- **S:\dq:** a redundant source library; its frankenstein text is older than main's.
- **S:\tmp, S:\ladder-tmp-x:** empty.
- **Antigravity scratch** (C:\Users\Cory\.gemini\antigravity\scratch): Farlight is older than main. Ripple has touch
  mode and MP3 export that main does not have, so it is parked as later.csv **L113**, for when Recess work resumes.
- **S:\CurioClass-codex raw art and voice:** of 2,136 files, 2,118 are identical to main; the other 18 are redraws,
  kept in the archive.

## Skipped on purpose (reason in INDEX.csv)

From S:\CurioClass-codex only:

- **pydeps:** 140,912 files, 6.65 GB of Python and Node packages installed per job; reinstalled by name.
- **Browser profiles:** 1,070,344 files, 145.4 GB of headless Chrome and Edge test profiles (caches, models, crash
  data); a fresh profile is made every run.

## Left in place

- **S:\Notes:** 118 files, none of them in main; Cory's own folder (SAM.gov PDF, portfolio, a standards projects
  bank). Not archived: Cory's call.
- **S:\CurioClass\Gemini\Api.txt:** a credential, left untouched for tool work.

## For Cory to delete (S:\CurioClass-archive\_to-delete\)

- **CurioClass-codex-2026-11-25:** the browser profiles and pydeps above, plus duplicates of the kept files.
- **worktrees-2026-11-12:** the unzipped folder. worktrees-2026-11-12.zip (15.96 GB, 927,635 files) was checked
  against it (member list, sizes, CRCs) before the folder was parked; the INDEX row carries the zip's sha256.

## Leftovers for step 5 (tool records)

- tools/time-tides/pipeline/assemble_atlas.py reads Antigravity's brain folder and writes into the now-archived
  CurioClass-agy folder; it needs new paths before it runs again.
- docs/agents BATCH-* and ART-W*-LOG files are tool-era records; step 5 decides where they live.

## Lessons

- My own background size scans (du, find) held handles on folders, and Windows refused to rename them with "Access is
  denied". Wait for scans to finish, or move a folder's children one by one.
- A Codex checkout grew to 145 GB of browser profiles; any future worker folder needs those profiles in a temp folder
  or cleared after a run.
- The app's sandbox redirects C:\Users\Cory\AppData\Roaming to the Claude package's LocalCache; the INDEX row for the
  Start Menu shortcut was corrected to the real path.

## Gates

`consolidation_gates.py run step3-after`: 128 gates, 25 exited non-zero, the same 25 as step3-before (check_tools and
24 course plan gates, all known and open before step 3). `compare step3-before step3-after`: **0 new lines**. Both
runs' output is committed with this report in step3-before\ and step3-after\.

Step 3 is done. Step 4 (architecture) waits for Cory's go and the Fable read.
