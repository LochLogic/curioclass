# Fixes: scope and sequence of social-and-emotional-learning-grades-9-to-12, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-social-and-emotional-learning-grades-9-to-12-2026-11-26.md), done under build/scope-writes/AFTERCORE-FIX.md. The Codex read waits for Codex's usage reset (after 2026-11-30) and gets its own small pass then. The other SEL expert reads (K to 2, 3 to 5) have no "Across the band" section and no item that touches this course.

Counts: applied 12 (expert 10, own 2); not applied 2 (expert 2, both settled by the expert as no change); band items 0; lead calls applied 0 (none fit this course: no specials, no readiness checks, no source-map, no begun day with empty codes, no frame.py failures). Every finding is logged in the defect ledger (plan.py defect, made-at scope).

## Applied

- **Expert 1 (RS8 offer half)**, days.csv: day 246 goal adds an offer of help planned for a new coworker or roommate who seems stuck; day 247 adds one offer round, the partner as a newcomer who accepts; day 255's plan page adds the prompt "Write the offer you would make to a new roommate who seems stuck, and when you would make it". scope-and-sequence.md unit 24 arc and evidence line name the offer.
- **Expert 2 (SO6 different places)**, days.csv: day 225 opens with comparing the unwritten rules of a workplace break room and a dorm floor before the fairness round; day 233 adds a prompt naming one unwritten rule that differs between two settings and how a newcomer would learn it. Unit 22 evidence line updated.
- **Expert 3 (RD3 own life)**, days.csv: day 243 gives each student a fresh invented own-life problem (a part-time job schedule that clashes with a family duty), marked per student, with the community fix plan as the group part; the note says no student tells of their own life.
- **Expert 4 (fold-ins)**, days.csv: in all 16 groups of the eight two-group units (1, 3, 7, 8, 13, 15, 19, 21) the first Fluency now rehearses every sub-skill of the group and the second replays them all on a changed case (goals of days 2, 3, 6, 7, 24, 27, 28, 66, 67, 70, 71, 76, 77, 80, 81, 130, 131, 135, 151, 152, 155, 156, 195, 199, 215, 216, 219, 220 rewritten; 23, 134, 194, 198 already covered every sub-skill). Second-Fluency notes say so. scope-and-sequence.md "Kinds of day" and Shorter path claim rewritten so it is true as written.
- **Expert 5 (retrieval placement)**, days.csv: each group's assumed rows are now one opening item with a short prompt per row on the group's Understanding day (retrieves column lists them all); 97 later openings moved off Fluency and Application days, which now open with the calm start (before day 14, an item on the last session's step card). Assessed days 226, 229, 240, 248 and 251 keep the calm start. scope-and-sequence.md "Openings" bullet and every unit's Readiness and retrieval line reworded.
- **Expert 6 (checks claim only what they sample)**, days.csv: day 9 adds "Show where this week's three deadlines go in the planner and when it is checked" (SM5); day 137 adds the identity-under-pull prompt with the invented-student option (SA1), and its note says so.
- **Expert 7 (overloaded course checks)**, days.csv notes of days 30, 63, 94, 127, 158, 191, 222, 255: the unit page about 12 minutes, then the two sampled items about 4 each, one prompt per part. scope-and-sequence.md Course-level checks paragraph and the 30-minute path (page about 9, items about 3 each, unfinished rehearsals into the respond session's first 10 minutes).
- **Expert 8 (leave-out bridge)**, days.csv: day 11 bridge adds the support map's one-step form; day 32 adds it where units 1 and 2 are both left out. Shorter path's leave-out paragraph names both.
- **Expert 9a (unit 23 evidence list)**, scope-and-sequence.md: Applications RD1, SA4, RD3, RD4; Check RD2, RD5, RS6, its hidden-term page asking RD1's questions again.
- **Expert 9b (one-session carry-outs)**, days.csv: day 217's book drive is collected between sessions from day 215 and the session holds the last planning round and the closing review; day 243 sets the community fix to run between sessions, with its look-back in day 245's opening (day 244 carry-out and day 245 goal and opening changed to match, as unit 2 does). scope-and-sequence.md units 21 and 23 say so.
- **Own 1**, days.csv: day 255's sampled SO6 item asked only the fairness half; it now sets the community rule beside a second setting whose unwritten rule differs.
- **Own 2**, frame.md (calls 4 and 11, wording only): "Inside the 40 minutes" says the retrieval item sits on each group's Understanding session with a prompt per earlier card; "Kinds of day" says the first Fluency of a two-group unit rehearses every sub-skill and the second replays them all on a changed case; "Course-level checks" gives the 12 / 4 / 4 time split. No unit, day count or owned row changed.

## Not applied

- **Expert 9c (SM7 "together" in grade 12)**: no change; the expert settled that the grade 9 and 11 group proposals carry the "together" part.
- **Expert 9d (day 85 return to Brown)**: kept; the brief bars repeats within a band only, and the new depth is named.

## Settled (for DIGEST)

| Question | Pick | Why |
|---|---|---|
| Retrieval in a group with several assumed rows | One opening item on the group's Understanding day, a short prompt per row; later days in the group open with the calm start | Warms every earlier form before new depth; assessed days keep the calm start |
| Two-group units on a short year | First Fluency rehearses every sub-skill; second replays all on a changed case | Any fold of the second then cuts no only-rehearsal |
| Widened course check timing | Unit page about 12 minutes, two sampled items about 4 each; 30-minute path 9 / 3 / 3 with rehearsals spilling into the respond session | Per-part evidence fits the session |
| A two-halved code judged on a group product | Add a per-student item on an invented case for the other half; the group product stays the group part | Per-student evidence with no disclosure |
| A pilot or service task in one session | Runs between sessions; the look-back opens the Respond session | Unit 2's model, applied to units 21 and 23 |

## For the structure pass

- None. No shared file needs a change from this pass. The writer's For the lead items 4 (begun AASL ids in data/progressions/sel.csv) and 5 ("standard None is on no day", left per lead call 12) stand as written.

## For Cory

- None.

## Gates

- `python -X utf8 scripts/sequence.py check social-and-emotional-learning-grades-9-to-12`: 0 failures; notes only "standard None is on no day" for units 1 to 18 (lead call 12: left).
- `python -X utf8 scripts/frame.py check social-and-emotional-learning-grades-9-to-12`: 0 failures (24 units, 256 days; 60 unit days a year).
- `python -X utf8 scripts/frame.py calendar`: no break for this course (grades 9 to 12 keep only the finals-week rule; checks unchanged in weeks 15, 16 and 32).
- `python -X utf8 scripts/stale.py check`: 121 files, 0 failures.
