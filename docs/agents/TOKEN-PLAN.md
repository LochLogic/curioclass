# Token plan: the same quality for fewer tokens (planned 2026-11-10)

Cory, 2026-11-10: token cost is the single biggest limit on growth. Find savings that do not reduce quality. Order and
status: docs/ROADMAP.md, Now. Nothing here is adopted yet; each change must pass the trial below first.

## What the logs show

Measured 2026-11-10 from the usage records of past Curio Class agents (`python scripts/agent_usage.py`; the newest 40
of each kind, medians, all on Opus).

| Agent | Runs | Turns | New context | Re-read context | Output |
|---|---|---|---|---|---|
| Spec | 40 | 25 | 112k | 2.1M | 33k |
| Teaching lens | 33 | 35 | 157k | 3.9M | 35k |
| Play lens | 36 | 43 | 183k | 6.1M | 34k |
| Craft lens | 33 | 48 | 221k | 7.1M | 42k |
| Sensitivity | 32 | 17 | 89k | 1.3M | 15k |
| Merge | 30 | 8 | 68k | 0.7M | 13k |
| Exit check | 15 | 63 | 410k | 10.6M | 57k |
| Finish check | 7 | 76 | 545k | 10.5M | 41k |
| Plan | 16 | 22 | 89k | 2.1M | 19k |
| Claude build (before Codex) | 40 | 165 | 1.03M | 28.1M | 240k |

- **Earlier figures count only new context.** "About 150k a lens" and "an exit check is 90k to 170k"
  (BATCH-BR-LOG.md, MEASURE-FIRST.md, docs/funding/COSTS.md) leave out re-reads. Every turn re-reads the agent's whole
  context. Re-reads are discounted, but there are so many that they are the largest share of a lens.
- **The exit check and the Finish check together cost about as much as all three lenses.**
- **Cost is turns times context size.** An average src.html is 76 KB; an agent that reads it whole carries it through
  every later turn. Lenses end near 180k to 215k of context.

## Changes to try, largest first

1. **Build in value order, and reshape before Build.** The catalog review (docs/agents/CATALOG-REVIEW.md) orders the
   bench and fixes specs early. A tool that is not built, or is fixed at spec, costs nothing downstream.
2. **Script the counting checks.** The standard voice check (repeats, stale lines, first tap, Read, order), lines.json
   against allLines(), art tokens against prompts.json, sizes, network requests, console errors, em dashes and the
   words rules are counting jobs. A script does them the same way every time. This takes most of the Craft lens and
   large parts of the Exit check and Finish check; the agent keeps what needs judgment.
3. **One evidence pack a round.** One script (after the shared audit) bundles the tool, shoots contact sheets of every
   mode and size, runs the scripted checks and lists every on-screen string and spoken line. Lenses and checks read
   the pack and make a few calls of their own, not 25 to 55.
4. **Keep heavy files out of context.** Agents get an outline of src.html and search it; they look at contact sheets,
   and open a single frame only to confirm a lead. Each lens gets the parts of STANDARDS, BASELINE and REFINE it uses.
5. **A spec pre-check for the build-first tier.** About half of Refine findings trace to the spec (MEASURE-FIRST.md).
   One short agent run on "Can it be beaten?", the worked numbers and half-taught codes, before Codex builds.
6. **Model tiers, by trial.** The plan agent and what is left of the Craft lens on Sonnet (merge already is,
   2026-11-06). Teaching, Play, sensitivity and the judgment half of the checks stay on the top model.
7. **A lighter Refine for engine siblings,** only if the counts in existing refine.md files show siblings come out
   cleaner on the engine's parts. Check that with a script before proposing it.
8. **Housekeeping.** Move closed items out of RUNBOOK.md so a new session reads less; correct the cost figures in
   docs/funding/COSTS.md from the table above.

## The quality guard

No change is adopted on argument. Each one runs beside the current flow on the same three tools (from the tools
waiting at Self-check: one K-2, one 3-8, one 9-12). It is kept only if it finds every blocker and should-fix the
current flow finds; anything it misses is fixed in the script or brief and the trial is run again. Record turns,
context and output for both flows here. Estimate before the trial: changes 2 to 4 cut a tool's Claude cost by a third
to a half.

## Not on the table

Dropping a lens, the sensitivity agent, the Exit check or the Finish check; trusting a builder's own report; fewer
frames looked at; anything that BASELINE rules 1, 2 or 5 would not allow.
