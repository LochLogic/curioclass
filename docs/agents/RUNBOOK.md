# Runbook: running a batch (for the integrating session)

How a fresh Claude session takes Curio Class tools from concept to Cory's Review Desk. Proven on the grade 11 test
batch (2026-10-25, 10 tools; log in `docs/agents/BATCH-G11-LOG.md`). Read `docs/BUILD-PLAN.md` (the why) and
`docs/agents/STANDARDS.md` (the rules every agent follows) first.

## Start of session

1. `git pull`; `python scripts/board.py` for where every tool stands.
2. Read the open items at the bottom of this file and the newest batch log.
3. Ask Cory which tools (or pick from `data/waves.csv`). Write a short batch note, `docs/agents/BATCH-<name>.md`: the
   tools in build order, the band, anything batch-specific. Keep the standing rules in STANDARDS.md, not here.

## Wave cadence (Cory, 2026-10-27)

Small Build and Refine waves first, so Refine's findings improve the builds; big build-only waves only once a family's
builds come out clean.

1. **Small waves, about 7 tools, Build and Refine together.** Mix each wave: 4 or 5 new engines or formats, 1 or 2
   returning engines (their second tool tests the last wave's lesson), and at least one K-2 and one 9-12 tool. The
   first wave is the first tools of wave 1's new shared engines, spread across bands.
2. **After each wave, write the lessons down.** The reviewers start cold every time; the documents are what learn.
   Findings tagged general go into STANDARDS.md or BUILD.md, findings tagged with a family go into
   docs/families/<family>.md, and anything a reviewer keeps missing goes into REFINE.md.
3. **Count.** In the batch log, a table per wave: each tool's round 1 blockers and should-fixes (from refine.md's counts
   line; polish not counted), the wave average, and the average per family.
4. **Switch rule.** A family moves to big build-only waves, followed by big Refine waves, after two waves in a row where
   its tools average 0 blockers and under 1 should-fix. New families stay on small waves. A new shared engine's first
   tool is always refined right away, before its siblings are built.
5. **Cross-check.** If Cory sends a tool back from the Review Desk after Refine passed it, Refine missed something:
   fix REFINE.md, and don't count that wave toward a switch.

## The pipeline, per tool

Fresh agents (Agent tool, general-purpose), one tool each. Spec agents can run in parallel. Builds run one at a time
(they may touch kit files); the polish or exit check of tool N can run while tool N+1 builds. Keep at most about 3 to 4 agents running:
the account's session usage limit stopped 4 parallel agents once (they resume with SendMessage after the reset).

| Step | Agent | Prompt (fill in the id) |
|---|---|---|
| Spec | fresh | "You are the spec agent for ONE Curio Class tool: `<id>`. Repo: S:\CurioClass (Windows; use the Bash tool with Unix syntax, python is on PATH). Follow docs/agents/SPEC.md exactly, plus docs/agents/STANDARDS.md and the batch note docs/agents/BATCH-<name>.md. Start with `python scripts/neighbors.py <id>`. Write only tools/<id>/spec.md. No em dashes. Report: the one idea, the not-like list, voice and accent chosen, art list, open questions." |
| Spec check | you | Read all the batch's specs together: overlapping ideas, repeated images (four were caught in G11), same voice or accent as a neighbor. Fix the spec files directly. Log decisions on open questions. |
| Build | fresh | "You are the build agent for ONE Curio Class tool: `<id>`. ... Follow docs/agents/BUILD.md exactly, plus STANDARDS.md and the batch note. The spec is tools/<id>/spec.md. Quality bar: tools/collision-lab/src.html (voice queue, real-pixel stage). Do not change kit files unless truly needed (backward compatible, documented, other kit tools re-checked). Only write in tools/<id>/. Do not commit." |
| Look | 3 fresh, cold, at once (+1 sensitivity agent when rule 5 applies) | "You are the `<lens>` lens (Teaching, Play or Craft) for ONE Curio Class tool: `<id>`. Repo: S:\CurioClass (Windows; use the Bash tool with Unix syntax, python is on PATH). Follow the `<lens>` section of docs/agents/REFINE.md exactly, cold, plus STANDARDS.md and docs/agents/decisions/BASELINE.md. Recompute every number yourself. Use your own scratch folder, Chrome profile and port. Write only tools/<id>/refine/<lens>.md. Do not fix anything, do not commit." |
| Merge | you | Merge the lens files into tools/<id>/refine.md: one ranked list (blockers, should fix, accepted polish). Polish that would change the spec goes to the spec's open questions (REFINE.md, Merge). |
| Polish | the SAME build agent (SendMessage to it) | Paste refine.md's list, blockers first: "Fix every blocker and should-fix and the accepted polish items. Re-shoot your frames. Report what changed." |
| Exit check | fresh, cold | "You are the exit check for ONE Curio Class tool: `<id>`. Follow the Exit check in docs/agents/REFINE.md exactly, cold. Re-check every item in tools/<id>/refine.md and the gate. Write the verdict (PASS or ROUND 2) as refine.md's first line. Do not fix anything, do not commit." |
| Plan | fresh, after the final PASS | "You are the plan agent for ONE Curio Class tool: `<id>`. ... Follow docs/agents/PLAN.md exactly, plus docs/LESSON-PLANS.md and STANDARDS.md. Only write tools/<id>/plan.md. `python scripts/check_plans.py <id>` must pass. Do not commit." Read the plan yourself once: would a sub manage with it? |

At most two Refine rounds (REFINE.md, Rounds); round 2 runs only the lenses that had open items. Three lenses and one
build agent is four agents, the top of the limit: while a tool is in Look, don't start another build. Before 2026-10-27
the step was a single verify agent (docs/agents/archive/VERIFY.md); those tools keep their verify.md, and the board
counts either file.

## Art and voice (you, while builds run)

- **Art:** start FLUX only for an art session (it holds ~17 GB of RAM): run
  `S:\AI\koboldcpp\koboldcpp.exe` with the flags in `S:\AI\Start-FluxModel.bat` plus `--skiplauncher` (run in the
  background), wait for port 5002, then `python scripts/localart.py <id> --n 3`, look at
  `art/raw/_sheet-<name>.jpg`, and `--pick name:k`. Re-prompt with an `"sd"` field when it misfires. Stop the server
  when done. People (hands included) go to Gemini: `python scripts/art.py <id> <names>`, Cory reviews them.
- **Voice:** `S:\AI\tts\.venv\Scripts\python.exe scripts/localvoice.py <id>` clones the tool's bank voice
  (`"bank"` in voice/lines.json) for every line, then encodes. Listen for nothing (you can't); check the printed
  lengths and flag any very short clip for Cory. Then run `scripts/voice_liveliness.py <id>` (same venv), a reading,
  not a gate: it flags only clearly flat takes (pitch movement under 3 semitones, half that for short lines), which
  Cory heard as bored. Keep the fix gentle (Cory, 2026-10-27): redo a flagged line with
  `localvoice.py <id> --redo i,j --takes 5`, which keeps a normal take near the voice's home pitch, never the most
  excited one. A flag or two per tool is normal and can stay. When a fix round changes lines, record
  only the new ones, and delete clips for removed lines (localvoice never removes them).

## Going live for review

1. Rename tool.draft.json to tool.json, drop `"stage"`, add the credits to `sources` (FLUX images, Qwen3-TTS narration,
   Gemini art if any).
2. `python scripts/preview.py <id>` (card art; pass `--js=` to open a livelier screen, and look at it).
3. `python scripts/build_site.py --library --closet` (both flags on every deploy: without them the Reading Room or the Supply Closet drops off the live site), `python scripts/check_site.py`, `npx wrangler deploy`.
4. Review Desk (https://claude.ai/artifact/SVXBzgyS941dyqmEzQHgNC) with ArtifactData: set `items/<id>` to
   `{built, changed (what's new, what to check, what Refine polished, any "known, not done" items), order (next
   number), status: "ready", subject, title, url}`.
   Then refresh the desk's stats panel: `python scripts/desk_stats.py <scratch>/stats.json` and ArtifactData set
   `stats/board` from that file (pin the version you last saw). Do this too whenever a batch moves tools a stage
   (specs written, builds done, Refine passed, art or voice recorded).
5. Commit and push (Cory's standing rule). Log it in the batch log.

When Cory reviews: read `comments` where state is "new"; approvals set the item to `status: "ok"`; notes get acted on,
then the item goes back to "ready" with a reply on the comment and the comment marked "done".

## Open items (update as they close)

- **Wave cadence locked 2026-10-27** (see Wave cadence above): small mixed Build and Refine waves until a family's
  Refine counts fall, then big build-only waves for that family. Next: the first small wave (engine-first tools from
  BATCH-W1.md), on Cory's go.
- **Refine replaced Verify on 2026-10-27** (Cory's call): Build is the first solid draft; Refine is three cold lens
  agents (Teaching, Play, Craft), polish by the builder, and a cold exit check against a fixed gate
  (docs/agents/REFINE.md). It costs about 5 to 6 agent runs a tool instead of about 2. Watch the first batch: are the
  lenses finding different things, and does the Review Desk see fewer rounds?

- RESUMED 2026-10-27. Cory answered the decision board (172 of 208). Their standing rules are in
  docs/agents/decisions/BASELINE.md (answers.json beside it): every agent reads it and settles routine calls with it.
  Bring Cory only the important questions, each with full context. The board (https://claude.ai/artifact/3K6SQRTyc3VdAfbVg9ERis)
  is no longer the main channel.
  - Waves 2, 3 and 4 are specced and reviewed (W4: 42 specs, log BATCH-W4-LOG.md); wave 3 art done (ART-W3-LOG.md).
    One question for Cory is open: home-language glossaries for the ELD tools.
  - Next: the wave 1 builds, using answers.json and BASELINE.md. growing-up-q-a goes to Cory before any live push.

- **Spec wave 1: specced 2026-10-27, not built.** 75 tools outside the core subjects (CS, arts, media and careers,
  health, PE, library); note `docs/agents/BATCH-W1.md`, log and Cory's 54 open questions in
  `docs/agents/BATCH-W1-LOG.md`. Robot Mouse Mail became Snowy Mail Route
  (Cory's pick; `scripts/rename_tools.py` does any rename). Before building, each new shared engine (ml-lab, network, security, robot, dance,
  movement, stage, music-studio, fact-check, careers and others, listed in the log) is built with its first tool,
  which also writes `docs/families/<name>.md`. character-voice-booth records students (it needs the microphone allowed in the
  tool page's iframe; its Plan mode works without one). Standards coverage after the wave, with the suggested data-only
  code pass and later-wave modules: `docs/agents/overlap/wave1-gaps.md`.

- **Gap fill: merged 2026-10-27, not specced.** 176 new planned tools (586 to 762) and 108 code adds so every
  official standards list is claimed (ELA leaves 41 codes out by design). Report, coverage table and Cory's questions:
  `docs/agents/gapfill/REPORT.md` (answered 2026-10-27: keep all 176, cut a weak one only if its codes stay covered;
  cannabis and drinking fine in Weekend Substance Choices; sexual health past puberty paused; Q3 and Q5 to Q11 still open, Cory reviews them the evening of 2026-10-27). Spec the new tools in later waves like any planned tool. New standards edits go in
  data/modules/*.txt (`scripts/add_codes.py`), never modules.csv, which build_db.py regenerates; new tools go through
  a staging folder checked by `scripts/overlap/stage_check.py` and merged by `stage_merge.py`.

- **Scale plan (unlocked 2026-10-27, the CS batch is done):** `docs/agents/SCALE-PLAN.md`, covering the overlap pass,
  the shared narration helper, spec waves, art and voice nights. Start it when Cory says go.

- **Voice bank: done 2026-10-26.** All 25 recorded; Cory kept 23 (adventure-guide and calm-guide dropped).
  Listening page: `S:\AI\tts\.venv\Scripts\python.exe scripts/voicebank_sample.py` writes `shots/voice-bank.html`.
- **Voice sweep:** now step 1 of SCALE-PLAN.md (`Curio.voice`). No mass retrofit: tools move over when touched. The first four G11 tools (rollercoaster, island, outbreak,
  ferris) predate the held-click rule and may still have the first-tap race.
- **Grade 11 batch: complete** (10 tools live 2026-10-26).
- **CS batch: complete 2026-10-27.** robot-dance, computer-builder, score-keeper, game-remix and code-tracer are all
  approved. Lessons are in STANDARDS.md (two kinds of voice line, the line matches the state, preventScroll, fit
  guards, no hand-carried sharing). The plan agent is a good last check: it caught code-tracer's stuck table squeeze.
  Tool follow-ups the plans worked around (not urgent): code-tracer has no undo in Trace (Restart wipes the tally),
  the tally can't tell partners apart, and the Workbench has nowhere to rewrite a note. In game-remix, Kai's bug sits
  under "Changes Kai made", not under "No changes yet".
- **SEL batch (2026-10-26):** log in `docs/agents/BATCH-SEL-LOG.md`. Brain Gym was renamed Not Yet Gym ("Brain Gym"
  is a registered trademark), then renamed Comeback Club 2026-10-26 (id comeback-club); check every new tool name
  against trademarks at spec time.
- **Renamed or moved tools:** add the old path to `data/redirects.csv` (old,new); `build_site.py` writes
  `dist/_redirects` (Workers static assets honor it, 301) and `check_site.py` fails if a target does not resolve.
- **Voice size and level (voice.py):** lines.json `"kbps": 16` re-encodes a tool with many lines to fit the 2 MB
  bundle limit (walk-in-their-shoes, 156 lines). Watch the bundle size after voicing: game-remix reached 1.84 MB.
  `preview.py` replaces a builder's hand-drawn preview.svg with a screenshot; that is fine. `encode` now lifts a quiet take (speech RMS under 3500) toward 4500,
  capped at a 28000 peak; run `--reencode` on an older tool if a clip sounds faint.
- **Agent Chrome hygiene:** every agent that drives Chrome gets its own scratch folder, `--user-data-dir`, and private
  ports, and kills only the pids it started. One builder killed Chromes by name pattern and broke two other agents;
  two verifiers once shared a scratch folder. `scripts/drive.py` used to pass Chrome a relative profile path when
  given a relative outdir; Chrome then showed a "Failed To Create Data Directory" box on Cory's desktop and exited
  ("chrome did not start"). Fixed 2026-10-26 (the path is resolved). Any hand-launched Chrome must also get an
  absolute `--user-data-dir`. Its `--host` mode writes host.html into the tool folder: delete it after.
- **check_concepts drift:** `python scripts/check_concepts.py --write` regenerates `data/tools-concepts.csv` from the
  concept sources (`data/concepts/*.txt`) and silently reverts any row edited only in the CSV (six were lost and
  restored on 2026-10-26: line-safari, art-passport, paint-mixer, orchestra-zoo, beat-lab, fingerspell-flash). Edit
  the concept source, not the CSV (those six are now copied back into `data/concepts/electives.txt`).
- **Deploy while agents are mid-edit:** `build_site.py` (and `check_tools.py`) rebundle every tool from its src.html,
  so a deploy from the working folder ships half-built tools. Commit the finished tool, then build and deploy from a
  clean worktree of main (`git worktree add <scratch>/deploy-wt main`; robocopy `library/` across once with
  `/E /XC /XN /XO`, since its art is not in git). The build remakes every bundle from the committed src.html.
- **Bundles are not in git (2026-10-26):** `tools/<id>/<id>.html` is build output, ignored by the root `.gitignore`
  (`tools/*/*.html` except `src.html`). Each bundle inlines the tool's art and voice, which git already holds, and
  every rebuild added a new 1 to 2 MB copy to the history; at ~586 tools that would have pushed the repo past
  GitHub's recommended 1 GB. Commit src.html, art and voice; never force-add a bundle. Per-tool `.gitignore` files
  are no longer needed. Exceptions: elements-inspector and state-quest are hand-written single files (no src.html),
  so the `.gitignore` keeps their html tracked.
- **Graphics pass (2026-10-26):** people and characters from Codex (`gptart.py`; base first, pick it, then siblings
  with `"ref"` + `"ref_mode": "style"` and variants with plain `"ref"`); scenes and props from Cloudflare FLUX.2
  (`cfart.py`, free). Avoid candidates with light streaks across the key color (they break the cutout). Character
  sheets: `scripts/split_sheet.py` cuts one sheet into mood cells. Each agent driving Chrome needs its own debugging
  port, not just its own profile (two agents both on 9471 kept killing each other's runs).
- **Voice token in comments:** `bundle_tool.py` fills every `"voice:*"` in src.html, comments included, so a comment
  that quotes the token inlines every clip twice (four K-2 tools did this on 2026-10-26; one went from 1.5 to 2.8 MB).
  Write "the voice token" in comments. When a tool is still over 2 MB: `"kbps": 16`, re-save backgrounds about 1024
  wide at quality 45-55, then a small `"tempo"` (1.05) as a last step.
- **Integrator fixes:** when both fix rounds are used and one narrow should-fix remains, fixing it yourself and
  appending an "Integrator fix" note to verify.md (with what you rechecked) has worked four times. Under Refine, the
  note goes in refine.md.
- **Paused (specs done, not built):** circuit-builder, sound-studio, satire-decoder, usage-panel, stock-market-1929.
  Their specs predate STANDARDS.md (one voice, no Look section): update voice and accent before building.
- **Lesson plans (2026-10-25):** every tool gets `plan.md` (docs/LESSON-PLANS.md). Cory approved the three grade-2
  test plans, and every live tool (62) had a plan by 2026-10-25. New waves add the plan as part of going live.
- **Parked K-2 tools waiting on voice:** see the Review Desk "Parked" filter.
