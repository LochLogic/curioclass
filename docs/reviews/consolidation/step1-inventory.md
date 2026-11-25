# Consolidation step 1: inventory for Cory (2026-11-24)

What the rescue found that needs a call before it moves. Everything in steps 1 to 3 is copied first and nothing is
deleted; every archive copy is hash-checked and has a row in S:\CurioClass-archive\INDEX.csv.

## Done in step 1 (no call needed)

| Item | Where it went |
|---|---|
| Earthquake Table, Tether Drift | tools/<id>/source/ untouched, notes.md (stage Build, unchecked), safety scan clean; Tether Drift is a Recess side project (later.csv L112) |
| Six Gemini sequence reads | docs/reviews/sequence-<course>-gemini-2026-11-24.md (the calibration and prework reads were already filed on 2026-11-20) |
| Time Tides data pipeline | tools/time-tides/pipeline/ (scripts untouched, README); raw GeoJSON, Cliopatria zip and .b64 data in pipeline/raw/, git-ignored |
| Raw art from S:\CurioClass-codex | 87 missing files copied into place (chess, equation-balancer, globe-theatre-stage, mole-bakery, rigid-motion-twins, star-life-story, thesis-workshop); 18 that differ from main's copy kept beside it in art/raw/_codex/. Log: step1-raw-art.csv. No other worktree had raw art main lacks |
| Class Phone Call | tools/class-phone-call/ from agy/build: Build and Self-check, a draft (tool.draft.json), off the site |
| AGY-BUILD.md, 45 research packets, RESEARCH-PACKET.md | archived; SPEC.md step 6 now says research from scratch |
| Codex generated images (2,651, 5.5 GB), three Curio skills, _runner and _scopes logs | archive copies, hash-checked; originals stay until step 3. MAP.csv ties 1,042 images in 99 sessions to 70 tools through the queue logs; the other 1,609 come from Codex sessions whose logs are gone |

## Calls for Cory

### 1. Worksheets wave 2, groups g25 to g28 (only on a branch)

origin/claude/hopeful-dirac-qck82o (2026-11-03) holds about 100 worksheets main never got: library 11 and 12, SEL K
to 12, ELD K to 12, CTE and personal finance. They add 4,436 lines to 33 sheet files that main has not touched since,
so they come in cleanly; the branch's ROADMAP.md and WORKSHEETS-PLAN.md edits are older than main's and are redone by
hand. The sheets would go live on the site with the next deploy.
**Pick:** bring them in now and run the worksheet checks (recommended; finished work, the site is not marketed yet),
or archive the branch with a later.csv row.

### 2. drafts/desk: the Desk page source

The plan said desk.html and snap.json move into the repository under desk/. The repository is public, and snap.json
is a copy of the Desk's cards and your answers (970 KB). **Recommended:** desk.html (the page code) goes to desk/
with a README on publishing it; snap.json stays out of git, since every Desk refresh rebuilds it from the Desk's own
data. desk-live.html is an older copy (2026-11-11) and goes to the archive.

### 3. _scratch/ladder/gen.py

The plan said it moves to scripts/ because HANDOFF names it. It has since been replaced: scripts/coursegen.py
(2026-11-21) makes the same job queues in COURSE-RUN order, and gen.py only works next to its own templates.
**Recommended:** archive it with the rest of _scratch/ladder and change the HANDOFF line to name coursegen.py.

### 4. Main's _scratch/ and drafts/ (git-ignored)

| Folder | Size | Newest | What it is | Recommended |
|---|---|---|---|---|
| _scratch/l87 | 101 MB | 2026-11-24 | the kit's live scratch (docs/pipeline/kit/common.txt sends agents' helper scripts to _scratch/l87/tmp/) | stays |
| _scratch/ladder, ladder2 | 405 MB | 2026-11-22 | the science, social studies and ELA ladder runs; their kit was copied into docs/pipeline/kit/ | archive |
| _scratch/scifix | 37 MB | 2026-11-22 | science K to 3 fix and finish job queues | archive |
| _scratch/goalmap | 7.6 MB | 2026-11-22 | Goal map work (later.csv L102, done) | archive |
| _scratch/probe4, probe5, kprobe | 0.5 MB | 2026-11-18 | probe job files (probes closed) | archive |
| _scratch/fo-preview | 46 MB | 2026-11-18 | a site preview build | archive |
| _scratch/gemini | 1 MB | 2026-11-22 | Gemini paste prompts and outputs (reports already filed) | archive |
| _scratch/sara-check | 4 KB | 2026-11-09 | one list | archive |
| drafts/paste-ready, drafts/private | 0.1 MB | 2026-11-12 | email drafts and private notes (never public) | stays |
| drafts/gemini/earthquake-table-prompt.txt | 8 KB | 2026-11-22 | the prompt that built Earthquake Table | tools/earthquake-table/build-prompt.txt |

### 5. The other two branch tips (nothing to rescue)

- origin/audit/states (2026-10-28): its audit_tool.py, curio.js, KIT.md and BUILD.md changes are in main in later
  form (every added line of curio.js, KIT.md and BUILD.md is on main; the 39 audit_tool.py lines that are not were
  rewritten since). Its family photo removal is in main (bc8f2520f).
- origin/codex/biased-bot: only the family photo removal, already in main.

Both are tagged archive/<branch> and removed in step 3, as planned.
