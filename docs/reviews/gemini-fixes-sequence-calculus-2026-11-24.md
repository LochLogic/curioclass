# Gemini fixes: scope and sequence of calculus, 2026-11-24

Fix pass on the outside second read S:\CurioClass-gemini\reports\sequence-calculus-gemini-read.md, after the expert read docs/reviews/sequence-calculus-2026-11-24.md and its fix pass docs/reviews/sequence-calculus-fixes-2026-11-24.md. Each finding was checked against the files (days.csv, frame.md, scope-and-sequence.md, the briefs, the lead calls and scripts/unit_skeleton.py); none rests on an outside fact or figure, so no web source was needed. Gemini's mathematical spot checks (the (cos h - 1)/h limit, the 1/x and 1/x squared swap, logistic fastest growth at K/2, the Cavalieri comparison, the circle arc to x = r/2) agree with the expert read and change nothing.

Counts: 3 findings: 1 holds, 1 partly, 1 wrong. One own fix.

## Findings

| # | Finding | Verdict | What changed |
|---|---|---|---|
| 1 | Earlier-grade retrieval ids (alg1-, geo-, alg2-) sit in `skills` on 17 days; sequence-write rule 2 forbids it | Wrong (settled) | None. The rule 2 sentence sits under "Readiness rows go in the note" and binds readiness rows. Retrieval ids in `skills` are math lead call 4 (docs/reviews/sequence-lead-calls-2026-11-15.md, Math 4: "Earlier-grade retrievals carry the row id in the skills column"), and the calculus fix pass already checked it as held. scripts/unit_skeleton.py reads such an id as an earlier row for retrieval, not as an owned row (its comments cite lead call 4 and the 2026-11-15 spot check). The settled call stays. |
| 2 | Ours days 23 and 74 carry "base" in the note (rule 8) | Partly (holds, and one day missed) | days.csv: day 23 note "Ours (CC 2.3 is not in the store)"; day 74 note "Ours (CC 8.7 has no archive copy): net change from a rate rule and a rate graph, with units." (the expert's settled wording kept apart from the one word); own: day 87, also ours, read "Ours (no base section)" and now reads "Ours (no CC section)". Day 22 keeps "base CC 2.3" because it adapts CC 2.2 in part. |
| 3 | frame.md says improper integrals trim "from 3 days to 1", saving 3 days, but days.csv gives them two teaching days (90, 91) | Holds | frame.md A tight course step 1: "from 2 teaching days to 1 (day 91 into day 90) and arc length (unit 8) from 2 days to 1 (day 117 into day 116) ... saving 2 days". Grade 12 calendar bullet: the trim order now totals 4 days, then day 7's rewrite practice into day 6 (the scope's fifth fold-in day), up to 5 days. scope-and-sequence.md Shorter path: "The first four follow the frame's trim order ..., and the fifth, day 7, is the next fold the frame's Grade 12 calendar names". No day, unit or count changed. |

## For Cory

None. No finding touches units, day counts, scope, audience, money or people.

## Gates

- `python -X utf8 scripts/sequence.py check calculus`: 0 failures (the seven expected accelerated-path rule 2 notes, unchanged).
- `python -X utf8 scripts/frame.py check calculus`: 0 failures.
- `python -X utf8 scripts/frame.py calendar`: exit 0; no calculus check or end day moved.
