# Fix report: social-studies-grade-1 unit 6 (2026-11-17)

Findings merged: 21 (assessment 9, sources 8, sequence 4; Liberty welcome basis named by both assessment 3 and sources 1, ordering cards by assessment 6 and sequence 4, kept as separate lines). Fixed: 14. Rejected: 7. Lead: 1.
Held up per lens: assessment 9 of 9, sources 3 of 8 (1, 3 in part, 8), sequence 2 of 4 (2, 4).

Fixed: split four joined wrong answers into single letters (A1); stated paper-only and heard items with minutes per group (A2); Liberty prompt now asks who might not have felt welcome, key rests on the poem's words, fresh captions carry the key details (A3, sources 1); day 62 retrieval changed to a classroom flag and a coin eagle (A4); "custom means weather" refiled under B (A5); exit 63 ordering moved to day 63 teaching, exit 66 cut to one claim with evidence for unity and diversity on a captioned photograph (A6, sequence 4: the 62 mention removed, one use kept on 63); item 5 look-for rejects "the flag" or "the landscape" alone (A7); field 7 now has at most four groups from the record sheet and a component-to-repair line (A8); J added to the day 60 spoken check and likely miss, M added to item 6 (A9); dated "As of November 2026" bird-law line with congress.gov to confirm (sources 3, in part: no flag or White House page named, over the cap); Tennessee row and pipeline remarks deleted (sources 8); retrieval reteaches on 56, 59, 62 moved to a small group in supported practice (sequence 2).

Gate: `unitplan.py check social-studies-grade-1`: s06.md PASS (1,250 cap reached; all further source additions were cut for it).

REJECTED: sources 2 | The Pledge and four lyric phrases name no free place where their words were checked. | Over the word cap: the plan was at 1,376 words after the fix and 1,250 is the cap; naming 4 U.S.C. section 4 and a Library of Congress printing needs about 35 words and cutting existing lines is not allowed. | UNIT-PLAN length cap
REJECTED: sources 4 | Held-out photograph archive and licence class are not named, and captions are written before photographs. | Over the word cap (about 25 words needed); the plan already says to select and verify photographs so captions match their details. | UNIT-PLAN length cap
REJECTED: sources 5 | Item 6 and day 66 rest on an unnamed fresh Constitution passage. | Over the word cap (about 15 words); day 66's exit no longer uses a passage after the A6 fix, so only item 6 remains open. | UNIT-PLAN length cap
REJECTED: sources 6 | Nairobi claims and the day 57 greetings have no read source. | Over the word cap (about 25 words); the plan already says the city and ministry pages are still to read before production. | UNIT-PLAN length cap
REJECTED: sources 7 | The Sapporo winter guide is a tourism site used for the snow claim. | Over the word cap (about 20 words). | UNIT-PLAN length cap
REJECTED: sequence 1 | Days 60, 62, 63 and 65 are overloaded; field 2 should name the core and the optional parts. | Over the word cap (about 40 words), and minute budgets belong to the section plans 6.2 and 6.3. | UNIT-PLAN length cap; UNIT-PLAN section plan field 6
REJECTED: sequence 3 | Supplies omit tokens and a tune source for adults who cannot read music. | Over the word cap (about 40 words); the plan already lets a child who cannot hear a tune match title and printed lyrics. | UNIT-PLAN length cap

LEAD:
- days.csv notes for days 62 and 63 name no timeline use; the plan now uses dated symbol cards on day 63 only.
- Rejected sources 2, 4, 5, 6, 7 and sequence 3 are real gaps for source-map.csv or the section plans (6.1 to 6.3), not the unit plan.
