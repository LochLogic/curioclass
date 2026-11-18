# Token efficiency for section plans and days (for discussion, 2026-11-18)

Cory (2026-11-17): the Claude second lens pass used two full 5-hour quotas and part of a third. Writing everything
down to the days needs far more efficiency, and the quality bar does not move. This note sets out the options for
discussion. Nothing here is decided or built.

## What the lens pass cost, and why

Each read or fix agent used about 115k to 265k tokens. Before an agent reached its unit it loaded whole course files
(MEASURED, average sizes):

| File | Size | About |
|---|---|---|
| Course frame | 48k characters | 12k tokens |
| Scope and sequence | 40k characters | 10k tokens |
| days.csv | 93k characters | 23k tokens |
| UNIT-PLAN.md, GLOSSARY.md, BASELINE.md | 65k characters | 16k tokens |

That is about 60k tokens per agent, and the full context goes back with every tool turn. Each unit loaded it twice
(read, then fix), so 186 units made about 370 full loads. Most of the pass's cost was reading in, not the work.

## Why days are different

Days cost what is written out, not what is read in.

- 52 core courses hold 7,544 planned days (data/plans/*/days.csv), in about 1,000 sections.
- The US History I 5.2 probe (5 days) produced about 70k characters across days, sources, exits, organizer, model
  and family pages: about 3,500 output tokens a day (MEASURED on one section).
- Writing every day once is then about 26M output tokens (DERIVED). Output cannot be cached or batched away; only
  writing less lowers it.
- Every rewrite of a day costs its full output again, so rework is the biggest multiplier.

Codex is already on gpt-6.1-sol (~/.codex/config.toml; Cory runs it at medium effort). GPT-6.2 Astra and Sol shipped
2026-11-17; reports put 6.2 Sol at the same price as 6.1 Sol, so switching is a like-for-like upgrade, not a saving.
Codex Pro ends 2026-11-30; Plus is much smaller.

## Options, best first

1. **The script writes everything repeated.** Measure the probe days for lines that have the same shape every day
   (headings, timing grid, materials, family page frame, exit format). Move them into scripts/day_skeleton.py or one
   shared page per unit, so the model writes only the teaching content. The only lever that shrinks the 26M figure
   itself. Free; no quality cost.
2. **Stop rework upstream.** The probes changed 88% then 42% of units. Every repeated fault becomes a gate before
   days are written, and the third social studies probe (later.csv L56) passes before anything scales. A fault caught
   in a plan costs one fix; caught in days it costs five days of output.
3. **Patch-only fixes.** Readers name lines; fixers change only those lines. No whole-day rewrites.
4. **One call per section, from a context pack.** The 2026-11-16 plan (DESK-ANSWERS, PRODUCTION-PATH step 7) made
   concrete: a script builds a pack per section (section plan, unit slice, its days.csv rows, the brief as a stable
   prefix). Reads go per section after the gates. The same packs fix the lens-pass cost: about 60k down to about
   12k of reading per agent (DERIVED), with fewer turns. Plan layers can also run one agent per course and merge
   read and fix; days keep the writer and reader separate.
5. **The Claude API with the Batch API (money).** Sonnet 5.5 is $2 in and $10 out per million tokens, with 50% off
   in Batch. Writing all 7,544 days, one read and one fix round would cost roughly $400 to $900 with thinking tokens
   (DERIVED, not measured); Opus 5.5 about double. It keeps both subscription quotas for orchestration and judgement.
   After 2026-11-30 the subscriptions alone are unlikely to carry 26M output tokens. Cory decides the spend; a
   one-section pilot gives a measured cost first.
6. **Haiku 5.5 for cheap steps** ($0.10 in, $0.50 out per million): building packs, pulling facts out of files, a
   first cheap read that passes flags up. Sonnet still writes days.
7. **Codex on section plans before 2026-11-30.** Section plans come before days, so they are what Pro can usefully
   drain now, on 6.2 Sol.

Not recommended: sampling reads in place of full reads. That lowers the bar.

## Proposed order

Options 1 and 2 first, because they shrink the job at no cost to quality. Then pilot option 4 as a one-section API
run, which also gives a real number for option 5. The first step is measuring the probe days (option 1).

## Questions for the discussion

- Measure the probe days now, before the third probe?
- Is an API spend for days on the table, and at what ceiling?
- Switch Codex to 6.2 Sol now?

Sources: 9to5Mac, "OpenAI upgrades ChatGPT and Codex with new GPT-6.2 Astra and Sol models" (2026-11-17);
munderdiffl.in, "GPT-6.2 Astra and Sol: price, context window, Codex". Claude prices from the Claude API reference,
cached 2026-11-03.
