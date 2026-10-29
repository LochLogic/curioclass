# Batch note: Build and Refine waves BR1 to BR4 (2026-10-27)

Cory asked for the first small wave and three more back to back, overnight. These are the first waves under the wave
cadence (RUNBOOK, Wave cadence): about 7 tools each, run through Build and Refine together (docs/agents/BUILD.md,
docs/agents/REFINE.md). Art, voice and plans come later; nothing here goes live. The log, with the counts table per
wave, is `docs/agents/BATCH-BR-LOG.md`.

## Rules for these waves (on top of BUILD.md, REFINE.md and STANDARDS.md)

- **Engines.** A tool that is the first of its family builds the shared engine in `kit/<family>.js` and writes
  `docs/families/<family>.md` (copy the shape of docs/families/data-desk.md). Its siblings come in later waves, so make
  the engine match the full description in this spec, not only what this tool uses.
- **Parallel builds.** Two or three builds may run at once overnight, so each build writes only its own tool folder,
  its own new kit file and its own family doc. Changing an existing shared kit file (curio.js, curio.css, the themes,
  data-desk.js, graphing.js) needs to be backward compatible, recorded in handoff.md, and every live tool that loads it
  re-checked. Never edit another tool's folder.
- **Art and voice placeholders.** Art is drawn after Refine: use the kit's placeholder art for every `art:` token,
  written so the real .webp drops in. Voice clips come after Refine too: the browser voice speaks until then.
- **Each agent's own scratch folder, Chrome profile and ports** (RUNBOOK, Agent Chrome hygiene). Kill only the pids
  you started.
- **Rule 5.** A tool with cultural, Native or hard-history content gets a sensitivity agent in its Look step.
- **Open questions** only Cory can answer go in handoff.md (builder) or refine.md (integrator) under "For Cory". Settle
  everything else with docs/agents/decisions/BASELINE.md.

## Waves

| Wave | Tool | Grade | Family | Engine |
|---|---|---|---|---|
| BR1 | teach-the-robot | 2 | ml-lab | new |
| BR1 | internet-journey | 3 | network | new |
| BR1 | data-defenders | 5 | security | new |
| BR1 | levels-and-pathways | K-2 | dance (+ movement figure) | new |
| BR1 | city-skyline-studio | 9-12 | perspective | new |
| BR1 | snowy-mail-route | 1 | robot | new file, lifted from live robot-dance |
| BR1 | simulation-studio | 9-12 | data-desk | returning |
| BR2 | song-form-builder | 3-5 | music-studio | new |
| BR2 | stage-blocker | 6-8 | stage | new |
| BR2 | fake-or-fact-lab | 6-8 | fact-check | new |
| BR2 | career-cluster-explorer | 6-8 | careers | new |
| BR2 | target-toss | 1 | none (PE) | none |
| BR2 | biased-bot | 2 | ml-lab | returning |
| BR2 | capture-the-flag | 9-12 | security | returning |

BR2 to BR4 are picked after each wave closes, so a family's second tool can test the last wave's lesson.

## Paused 2026-10-28 (Cory, session limit)

BR1 is closed: all 7 tools PASS and are committed (teach-the-robot round 2, internet-journey 2, data-defenders 2, city-skyline-studio 2, snowy-mail-route 2, simulation-studio 2, levels-and-pathways 3). Counts are on line 2 of each refine.md.

BR2 closed 2026-10-28: all 7 PASS, committed and deployed (counts in BATCH-BR-LOG.md). The BR1 wave-close work is
done (counts table, lessons in BUILD.md, KIT.md engine lines, the integrator spec moves).

## Resume here (new thread, after 2026-10-28)

1. Read BATCH-BR-LOG.md, BR2 and "Audit tuned after BR2": the counts, the Codex pilot verdict, the audit's state.
2. Cory's open question there: "welcome not heard after a first tap", a rule or not.
3. **Review the two single-tool tests with Cory** (done 2026-10-29, unattended overnight): network-help-desk and
   half-life-dice, both Codex-built, both Refine PASS and merged as drafts (BATCH-BR-LOG.md, "Single-tool tests").
   Bring up, in order: the counts against BR1 and BR2; the Codex cost and the two timed-out polish rounds; the audit's
   cold catch rate and its 23 to 73 minute runs; half-life-dice's two spec questions (energy-ladder student action,
   5,730 vs 5,700 years) and its two not-blocking notes; whether Codex becomes the default builder for BR3. Art,
   voice (on the Forge), Final look and Plan for both tools, and BR3, wait for that review.
4. Small fixes found after close, not yet done: see BR2 "Found by the tuned audit after close" in the log.
5. Board items: career-match-quiz onto kit/careers.js; scripts/careers_data.py writes the quiz path without --out.
6. Housekeeping in the main checkout (S:/CurioClass): docs/BUILD-BOARD.md has uncommitted changes from another chat,
   untracked docs/agents/audit/wordwall-movement-cards.jpg, stray server.pid and __pycache__. Folders to delete by
   hand: S:/CurioClass-audit, S:/CurioClass-codex, S:/CurioClass-codex-network-help-desk,
   S:/CurioClass-codex-half-life-dice, and S:/CurioClass-codex-scratch once the review is done.
