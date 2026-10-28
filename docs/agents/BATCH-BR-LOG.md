# Log: Build and Refine waves BR1 to BR4

Batch note: `docs/agents/BATCH-BR.md`. Counts come from each tool's refine.md counts line (round 1 blockers and
should-fixes; polish not counted).

## BR1 (started 2026-10-27)

Builds started three at a time: teach-the-robot, internet-journey, data-defenders first; then levels-and-pathways,
city-skyline-studio, snowy-mail-route, simulation-studio as slots free up.

### BR1 closed 2026-10-28: all 7 PASS

| Tool | Grade | Family | Round 1 blockers | Round 1 should fix | Exit checks to PASS |
|---|---|---|---|---|---|
| teach-the-robot | 2 | ml-lab (new) | 2 | 8 | 2 |
| internet-journey | 3 | network (new) | 1 | 13 | 2 |
| data-defenders | 5 | security (new) | 2 | 10 | 2 |
| levels-and-pathways | K-2 | dance (new) | 2 | 10 | 2 |
| city-skyline-studio | 9-12 | perspective (new) | 0 | 14 | 2 |
| snowy-mail-route | 1 | robot (new) | 0 | 10 | 2 |
| simulation-studio | 9-12 | data-desk (returning, engine created) | 1 | 15 | 2 |
| **Average** | | | **1.1** | **11.4** | **2.0** |

Every tool needed a second exit check; three of the last items were narrow integrator fixes (data-defenders hint,
snowy-mail-route badge and footprint size, simulation-studio text alternatives). The repeat findings became the
wave lessons in BUILD.md, STANDARDS.md (Voice) and REFINE.md (Rounds). BR2 is the first wave built with them.

Cost (from agent reports, approximate): build 125k to 235k tokens, each lens about 150k, each exit check 90k to
170k, a scoped re-check about 100k; roughly 0.7M to 1M tokens a tool.

Known gap: levels-and-pathways misreads about 1 in 11 drawn 3- or 4-hump waves at 375 and 680x425 (stage too small).

## BR2 (started 2026-10-28)

song-form-builder and capture-the-flag built first. Teaching lens round 1: song-form-builder 0 blockers, 1 should
fix; capture-the-flag 2 blockers (strength meter rewards patterns, tradeoff codes untaught), 5 should fix.

### BR2 closed 2026-10-28: all 7 PASS, deployed

| Tool | Grade | Family | Round 1 blockers | Round 1 should fix | Exit checks to PASS |
|---|---|---|---|---|---|
| song-form-builder | 3-5 | music-studio (new) | 1 | 10 | 1 |
| capture-the-flag | 9-12 | security (returning) | 2 | 9 | 2 + integrator fixes |
| stage-blocker | 6-8 | stage (new) | 2 | 16 | 2 |
| fake-or-fact-lab | 6-8 | fact-check (new) | 1 | 17 | 1 + integrator fix |
| biased-bot (Codex builder) | 2 | ml-lab (returning) | 0 | 9 | 2 + integrator fix |
| target-toss | 1 | none (PE) | 1 | 14 | 2 + integrator fix |
| career-cluster-explorer | 6-8 | careers (new) | 3 | 12 | 1 |
| **Average** | | | **1.4** | **12.4** | **1.6** |

Against BR1 (1.1, 11.4, 2.0): round 1 findings about the same, exit checks down. Three tools passed on the first exit
check (none did in BR1); four needed a narrow integrator fix after their last exit check (BR1: three).

Codex builder pilot (biased-bot): built and polished by Codex in S:/CurioClass-codex, branch codex/biased-bot,
reviewed blind by the usual lenses. Round 1 was the best of the wave (0 blockers, 9 should fix), but exit round 2
failed and one of its round 2 fixes caused a regression (story welcome cut by cutHow), closed by an integrator fix.
Codex tokens: 62.3M in (60.9M cached), 0.30M out over two rounds. It also changed kit/ml-lab.js (zero-size host skip,
groupBars empty and size options) and left scratch files in the tool folder that its sandbox could not delete.

Audit pilot (scripts/audit_tool.py) on BR2: its clean rows hold, but its overlap and focus-lost leads are false where
markers are clipped by a stage or scroll panel, it misses anything past one click, and its 44 px target rule conflicts
with K-2's 60 px. Tuning owed before it gates anything.

Left open (in each refine.md): target-toss P5 to P7 and N4; career-cluster-explorer Hospitality, Management and
Marketing at 2 of 5 levels, trail header wrap at 1366; biased-bot Run then Skip within 4 s, headless speech stall.
Board items: career-match-quiz onto kit/careers.js; scripts/careers_data.py default --out.
