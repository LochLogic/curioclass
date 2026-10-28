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

BR2 state, to resume from:
- song-form-builder: built (kit/music-studio.js new). refine/teaching.md done (0 blockers, 1 should fix, 2 polish). Play and Craft lenses were stopped mid-run; rerun both, then merge, polish, exit check.
- capture-the-flag: built (kit/security.js extended, data-defenders checked pixel-identical). refine/teaching.md done (2 blockers: strength meter rewards patterns, tradeoff codes untaught; 5 should fix). Play and Craft lenses stopped; rerun both. Integrator accepted the common-list line under Strength (checked accurate by Teaching).
- stage-blocker, fake-or-fact-lab, career-cluster-explorer, target-toss, biased-bot: not started.
- Neither BR2 tool is committed; their folders and engine edits are uncommitted in the working tree.

Wave-close work still owed from BR1: the counts table in BATCH-BR-LOG.md, the BR1 lessons into BUILD.md, STANDARDS.md and REFINE.md (Cory was asked whether to do this before more BR2 builds), KIT.md engine lines, and the integrator moves (Re7 codes to dance-pattern-puzzle and dance-styles-explorer, Cr3.1.1b off levels-and-pathways, fitness-circuit spec note, non-Old Faithful data notes for data-desk-distributions and data-detective).
