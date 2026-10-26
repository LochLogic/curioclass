# Runbook: running a batch (for the integrating session)

How a fresh Claude session takes Curio Class tools from concept to Cory's Review Desk. Proven on the grade 11 test
batch (2026-10-25, 10 tools; log in `docs/agents/BATCH-G11-LOG.md`). Read `docs/BUILD-PLAN.md` (the why) and
`docs/agents/STANDARDS.md` (the rules every agent follows) first.

## Start of session

1. `git pull`; `python scripts/board.py` for where every tool stands.
2. Read the open items at the bottom of this file and the newest batch log.
3. Ask Cory which tools (or pick from `data/waves.csv`). Write a short batch note, `docs/agents/BATCH-<name>.md`: the
   tools in build order, the band, anything batch-specific. Keep the standing rules in STANDARDS.md, not here.

## The pipeline, per tool

Fresh agents (Agent tool, general-purpose), one tool each. Spec agents can run in parallel. Builds run one at a time
(they may touch kit files); a verify of tool N can run while tool N+1 builds. Keep at most about 3 to 4 agents running:
the account's session usage limit stopped 4 parallel agents once (they resume with SendMessage after the reset).

| Step | Agent | Prompt (fill in the id) |
|---|---|---|
| Spec | fresh | "You are the spec agent for ONE Curio Class tool: `<id>`. Repo: S:\CurioClass (Windows; use the Bash tool with Unix syntax, python is on PATH). Follow docs/agents/SPEC.md exactly, plus docs/agents/STANDARDS.md and the batch note docs/agents/BATCH-<name>.md. Start with `python scripts/neighbors.py <id>`. Write only tools/<id>/spec.md. No em dashes. Report: the one idea, the not-like list, voice and accent chosen, art list, open questions." |
| Spec check | you | Read all the batch's specs together: overlapping ideas, repeated images (four were caught in G11), same voice or accent as a neighbor. Fix the spec files directly. Log decisions on open questions. |
| Build | fresh | "You are the build agent for ONE Curio Class tool: `<id>`. ... Follow docs/agents/BUILD.md exactly, plus STANDARDS.md and the batch note. The spec is tools/<id>/spec.md. Quality bar: tools/collision-lab/src.html (voice queue, real-pixel stage). Do not change kit files unless truly needed (backward compatible, documented, other kit tools re-checked). Only write in tools/<id>/. Do not commit." |
| Verify | fresh, cold | "You are the verify agent for ONE Curio Class tool: `<id>`. ... Follow docs/agents/VERIFY.md exactly, cold, plus STANDARDS.md. Recompute every number yourself. Write tools/<id>/verify.md (verdict line first). Do not fix anything, do not commit." |
| Fix | the SAME build agent (SendMessage to it) | Paste the findings, should-fix first, with the verifier's suggested causes. |
| Re-verify | fresh, cold | "An earlier verify found ...; the builder says all are fixed. Re-check each yourself, cold, and check nothing regressed. Append '## Re-verify' to verify.md." |

At most 2 fix rounds; a third only for a narrow, well-diagnosed problem in the tool's core. After the last round with
no blocker left, look at one frame yourself (the 680x425 preview is a good one) instead of another full re-verify.

## Art and voice (you, while builds run)

- **Art:** start FLUX only for an art session (it holds ~17 GB of RAM): run
  `S:\AI\koboldcpp\koboldcpp.exe` with the flags in `S:\AI\Start-FluxModel.bat` plus `--skiplauncher` (run in the
  background), wait for port 5002, then `python scripts/localart.py <id> --n 3`, look at
  `art/raw/_sheet-<name>.jpg`, and `--pick name:k`. Re-prompt with an `"sd"` field when it misfires. Stop the server
  when done. People (hands included) go to Gemini: `python scripts/art.py <id> <names>`, Cory reviews them.
- **Voice:** `S:\AI\tts\.venv\Scripts\python.exe scripts/localvoice.py <id>` clones the tool's bank voice
  (`"bank"` in voice/lines.json) for every line, then encodes. Listen for nothing (you can't); check the printed
  lengths and flag any very short clip for Cory.

## Going live for review

1. Rename tool.draft.json to tool.json, drop `"stage"`, add the credits to `sources` (FLUX images, Qwen3-TTS narration,
   Gemini art if any).
2. `python scripts/preview.py <id>` (card art; pass `--js=` to open a livelier screen, and look at it).
3. `python scripts/build_site.py`, `python scripts/check_site.py`, `npx wrangler deploy`.
4. Review Desk (https://claude.ai/artifact/SVXBzgyS941dyqmEzQHgNC) with ArtifactData: set `items/<id>` to
   `{built, changed (what's new, what to check), order (next number), status: "ready", subject, title, url}`.
5. Commit and push (Cory's standing rule). Log it in the batch log.

When Cory reviews: read `comments` where state is "new"; approvals set the item to `status: "ok"`; notes get acted on,
then the item goes back to "ready" with a reply on the comment and the comment marked "done".

## Open items (update as they close)

- **Voice bank (not recorded yet):** 24 candidate Gemini voices (`voices/bank.json`); only warm-teacher and
  hs-narrator exist. Run `python scripts/voicebank.py` (about 69 Gemini TTS requests; the daily limit is 50 per model,
  so it may take two days; it resumes from saved takes), then
  `S:\AI\tts\.venv\Scripts\python.exe scripts/voicebank_sample.py` for `shots/voice-bank.html`. Send Cory the page;
  he picks keepers (status "kept"). Then STANDARDS.md "Variety" applies with real choices.
- **Voice sweep:** a shared kit helper (narrate, hush, read, first tap, per STANDARDS.md) in `kit/curio.js`, then
  retrofit the 10 grade 11 tools and the K-2 tools onto it. The first four G11 tools (rollercoaster, island, outbreak,
  ferris) predate the held-click rule and may still have the first-tap race.
- **Grade 11 batch: complete** (10 tools live 2026-10-26).
- **Paused (specs done, not built):** circuit-builder, sound-studio, satire-decoder, usage-panel, stock-market-1929.
  Their specs predate STANDARDS.md (one voice, no Look section): update voice and accent before building.
- **Parked K-2 tools waiting on voice:** see the Review Desk "Parked" filter.
