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
