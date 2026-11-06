# Measure first: does Claude's Refine still find much after a Codex review? (2026-11-04)

Cory's call: full Claude Refine on 5 Codex-built, Codex-reviewed tools, run 2, then 2, then 1, with a go-ahead
between batches. Bar from the desk card (q-measure-first): no blockers and 3 or fewer should fix per tool on average
means Codex's review can replace Refine (one Claude exit check after it). Otherwise the full Refine stays.
The lenses do not read codex-report.md or codex-review.md.

| Tool | Built | Round 1 blockers | Should fix | Polish accepted | Lens tokens | Before Codex (10-28 Refine) |
|---|---|---|---|---|---|---|
| city-skyline-studio | 11-01 | 1 | 10 | 8 | 657k | 0 / 14 / 14 |
| levels-and-pathways | 11-01 | 0 | 6 | 11 | 707k | 2 / 10 / 8 |
| first-aid-responder | 10-31 | 1 | 13 | 10 | 563k | none |
| music-history-radio | 11-01 | 1 | 14 | 18 | 748k (incl. sensitivity 117k) | none |

Batch 1 (look and merge only, plus a 20 minute shared audit per tool): 1.36M lens tokens for two tools, about 20 to
25 minutes of wall time with all six lenses at once. Polish and exit check not yet run.

Batch 2: 1.31M lens tokens for two tools (music-history-radio also needed the sensitivity agent, which FAILED it on
gamelan's date and how Black musicians are credited). Both blockers are teaching errors a student would carry away
(a CPR score that rewards pausing; a living tradition dated by when Europeans heard it).

## Spec test (2026-11-05): do the new SPEC.md rules lower Refine counts?

SPEC.md gained "Lessons from ten full Refines" (commit edb985fa). Ten new specs were written under it:
safety-sweep-house, worry-size-sorter, bus-stop, letter-lanterns, line-leader-picker, bug-hunt,
warming-evidence-desk, cocoa-chain, roller-coaster-rounding, the-buyout (grades K to 12, seven subjects).

Baseline to beat (round 1 Refine on Codex-built tools from older specs, ten tools): 9 blockers (0.9 per tool),
99 should fix (9.9 per tool). About half the blockers traced to the spec (unchecked facts, scores rewarding the
wrong thing, standards half taught).

Measure: build each with Codex (build plus Codex review), run the same Claude Refine (shared audit, three lenses,
merge), and count blockers and should fix, and how many trace to the spec. Spec cost: about 140k to 210k Claude
tokens each, 7 to 15 minutes.
