# Fixes: math course frames, kindergarten to grade 2, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-math-<course>-2026-11-14.md`) and the Codex reads
(`frame-math-<course>-codex-2026-11-14.md`) for kindergarten, grade 1 and grade 2 to the three frames,
`data/progressions/math.csv` and one row of `data/modules.csv`. Every expert finding and every "Settled by the expert"
row is applied; each Codex finding was weighed on its merits. The grade 2 Codex read withheld its verdict over a gate
failure in its own environment: it is listed as blocked, rerun pending
(`frame-math-grade-2-codex-rerun-2026-11-14.md`), and a short follow-up pass applies the rerun.

Base-text claims were checked against the source store (S:\CurioClass-sources\illustrative-math): K.5.10 is the
base text's 10-frame introduction; no K.4 lesson uses a 10-frame; K.3.13 teaches above, below, beside and next to
only; K.3.6 and 3.7 hold the two length activities; grade 1 lessons 6.12 to 6.15 and 8.6 are the Compare and
equation lessons; every grade's pacing guide says "2 days for assessments per unit".

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check math-kindergarten math-grade-1
math-grade-2` 0 failures each (K 8 units, 160 days; grade 1 8 and 160; grade 2 9 and 160, 154 in units each);
`scripts/progression.py check math` 305 rows, 0 failures (also 0 inside `plan.py check`); `scripts/stale.py check`
on the three frames and the progression, 0 failures. No unit, skill or standard moved; every unit keeps its days.

## Kindergarten

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Source map: K.4 "adapt the joining and taking activities in lessons 1 to 12 to show counters on a 10-frame"; K.5 "adapt 10: the full 10-frame and how many are missing to make 10, not an introduction"; K.2 reason and the Models table say so |
| Expert | 2 | Applied | Unit 3 reason rewritten (two base activities in 3.6 and 3.7, no lesson of their own); K.MD.A.1's several attributes of one object added to What students learn; the two added lessons renamed as settled |
| Expert | 3 | Applied | K.3 row split: 1 to 12 and 14 kept; 13 moved to the unit's start and widened to all six words; shape cards where it leans on 3.10 to 3.12; unit 3 text names the six words first; brief says three moves |
| Expert | 4 | Applied | Unit 3 adds "comparing flat shapes by their sides, corners and equal sides (K.G.B.4 for flat shapes, begun here)"; unit 7 reason rewritten; Skills unchanged |
| Expert | 5 | Applied | Cross-subject opening rewritten; K-PS2-1 science first at week 2, K-ESS2-1 at week 6, with science's bridges; unit 3 reason and the K.7 source-map row now say "one place for direct comparison, which science uses all year" |
| Expert | 6 | Applied | Unit 2: sorting owned here with two Curio Class lessons; base sorting activities stay in units 3, 7 and 8 as practice; science's weather sort (week 6) and living things (week 17) named |
| Expert | settled | Applied | All three rows (K.5.10 adapted; the two added lessons; K.3.13 first) |
| Codex | 1 | Applied in part | Conflict with the expert, who marks the line met: both are right in part. Numbers kept but labelled a provisional allocation and a tag inventory; time line added (7,200 of 9,600 minutes); unit plans record minutes by lesson part and the supporting work that practises major work; the scope and sequence confirms. No full minute table now: the lesson-part minutes do not exist before the unit plans |
| Codex | 2 | Applied | Same as expert 2; the two readers' lesson definitions match |
| Codex | 3 | Applied, for Cory | For the lead item 1 now says the 60 minutes include centers, separate centers need their own block, and a 45-minute day needs its own pacing this frame does not plan. Whether to serve 45 minutes is Cory's |
| Codex | 4 | Applied | Same as expert 5; all three other kindergarten frames (ELA included) exist and are used: ELA unit 1 (weeks 1 to 7) sorts and asks key-detail questions before math needs them |
| Codex | 5, 6 | For the lead | `docs/agents/lenses/math.md` lines 61 to 62 and 65 to 66: outside this pass's files; replacement text below |
| Codex | 7 | For the lead | `frame-social-studies-kindergarten-2026-11-13.md` dated update: outside this pass's files |
| Codex | settled | Applied | Rows agree with the expert's and with the frame's own lead items |
| Writer | lead 2 | Applied | mk-one-to-one hands on to m1-count-to-120 (both rows); K seam table row added, grade 1 seam row updated |
| Writer | lead 3 | Applied | `data/modules.csv` math-k-sort-and-count: EK-ALG-ML-02 and the CSTA-2026 framework dropped |
| Writer | lead 4 | For the lead | Lens line (with Codex 5, 6) |
| Writer | lead 5 | Applied | Kept the two added unit 3 lessons; margin labelled provisional |

Found in passing and applied in all three frames: the base text budgets two assessment days a unit, the frames one.
Each Days bullet now gives the reason and what each unit plan must name (see grade 1, Codex 2).

## Grade 1

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Source map 1.6 "adapt 12 to 15: cube and matching drawings redrawn as a tape diagram, named"; 1.8 "adapt 6" as review; Models table and unit 6 say so; m1-all-problem-types notes too |
| Expert | 2 | Applied | Unit 1's last reason sentence replaced (social studies about week 11, science about week 20); cross-subject opening rewritten; science weeks corrected (with Codex 3) |
| Expert | 3 | Applied | Unit 7: half of, fourth of, quarter of, the whole as two halves or four fourths (1.G.A.3 in full) |
| Expert | settled | Applied | Tape diagram by adapting 6.12 to 6.15, 8.6 as review, no lesson added |
| Codex | 1 | Rejected | The frame-write brief puts `source-map.csv` at step 3 and this pass may not create it; the frame's table already places all 146 lessons. The conflict with PRODUCTION-PATH step 2 is for the lead |
| Codex | 2 | Applied in part | True: the base text budgets two assessment days a unit. The Days bullet now says why one is kept (own one-period assessment; one-to-one evidence gathered in center days) and that each unit plan names its evidence, observation minutes and coverage; an extra day, if needed, goes to Cory. No days changed now |
| Codex | 3 | Applied | m1-add-take-problems lean is now `ela:e1-key-details (SL.1.2: ask and answer questions ...)`; retelling kept as a math routine. m1-data-three-categories now names `science:s1-daylight-seasons` as a later use; removed from the "needs" table, kept in the reciprocal table. Both progression cells changed |
| Codex | 4 | Applied in part | As kindergarten Codex 1: provisional labels, time line, minutes in the unit plans; sequence not changed for the percentages |
| Codex | 5 | Applied | Same as expert 2; ELA, science and social studies grade 1 frames used. Also found: the "What other subjects need" table had s1-like-parents at week 23; science places it about week 11 on its own bridge. Corrected, and lead item 3 rewritten |
| Codex | 6, 7, 8 | For the lead | Lens lines and the progression read's line 205: outside this pass's files |
| Codex | coverage note | Applied | Compressed parts written in: numeral for a collection (unit 6), explained ten more and less, range 10 to 90 with zero differences (unit 4), telling and writing time (unit 7) |
| Codex | settled | Applied | Order kept; unit 8 kept; SL.1.2 to e1-key-details; daylight as later use; length bridges kept; untimed checks kept |
| Writer | unit 8 empty Skills | Applied | Reason kept and lead item 2 adds the fluency-target reason; both readers call it justified |

## Grade 2

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Cuts justified by the day budget (146 + 9 + 6 > 160) in the Days bullet, units 6 and 8 and lead item 2; "about 71 percent" dropped; major work recounted with the guide's rule: about 150 of 160 days (only 2.G lessons 6.1 to 6.4, 6.6 to 6.9, 8.12 out), strict count 121 of 160, lessons about 121 and 131 of 139 by tags |
| Expert | 2 | Applied | 2.3.17 kept, the estimating lesson dropped; 2.3 row "1 to 18, Keep all"; unit 3 text names 3.4, 3.5, 3.8, 3.9; totals 139 placed, 7 cut, 6 Curio Class lessons; the brief now lists all six added lessons; unit 3 stays 19 days |
| Expert | 3 | Applied | Models row: grade 1 unit 6 redrawn from cube diagrams; unit 1 builds it again from the bar graph (2.1.14 to 2.1.16); unit 1 and the Readiness bullet add a Compare tape diagram |
| Expert | 4 | Applied | Unit 3 reason (erosion ruler about week 9, plants in the spring); science table and the reciprocal table rewritten from the science frame's weeks; cross-subject opening rewritten; ELA unit 1 named for both ELA leans |
| Expert | 5 | Applied | Unit 6: half of, a third of, the whole as two halves, three thirds or four fourths (2.G.A.3 in full) |
| Expert | settled | Applied | Both rows |
| Codex | 1 | Blocked, rerun pending | The read stopped at a missing Python module in its own runner and judged nothing; the full gate ran clean in the expert read and here. The rerun is applied in a follow-up pass |
| Writer | lead 4 | Applied | The "grade 3 frame reads this seam afterwards" line was stale: the grade 3 frame's seam table lists neither ending thread, as the rows say |
| Writer | unit 9 empty Skills | Applied | Reason kept; the expert calls it justified |

## Progression changes (data/progressions/math.csv, 7 rows)

| Row | Change |
|---|---|
| mk-one-to-one | hands_on m1-count-to-120; notes say so |
| m1-count-to-120 | assumes adds mk-one-to-one; notes: large collections counted one by one first, then in tens |
| m1-add-take-problems | cross_subject `ela:e1-key-details (SL.1.2: ask and answer questions about key details of a story problem read aloud)` |
| m1-data-three-categories | cross_subject `science:s1-daylight-seasons` as a later use |
| m1-all-problem-types | Notes: IM grade 1 names no tape diagram; unit 6 lessons 12 to 15 adapted, 8.6 reviews |
| mk-shapes-positions | Notes: position words are IM 3.13, moved to the unit's start, all six words |
| mk-measurable-attributes | Notes: IM 3.6, 3.7 and 7.8, 7.9 gathered in unit 3 with the two Curio Class lessons |

Grade 3 frame: not edited; no handoff with grade 3 changed. `data/modules.csv`: the one row above.

## Cross-subject notes

No other subject's frame needs a change. The math weeks now match the science, social studies and ELA frames for
kindergarten to grade 2; each other frame already carries the bridge that covers a lean it meets before math (science
K push and pull and weather, grade 1 leaf ordering and signal device, grade 2 erosion). The ELA progression could name
the math lean back on e1-key-details if it wants both ends written; nothing fails without it.

## For the lead (outside this pass's files)

- `docs/agents/lenses/math.md` lines 61 to 62: "data/progressions/math.csv now records core mathematics ownership,
  handoffs, models and limits from kindergarten through grade 11. The grades 3 to 5 narrative remains a supplementary
  explanation. Course frames check these handoffs against actual unit order." Lines 65 to 66: "The K to 2 math frames
  describe untimed fluency checks through games and individual observation, recorded as just knows, quick strategy or
  counts all. Unit plans turn these into tasks, recording guidance and response decisions. Counting checks are
  separate from arithmetic-fluency checks."
- `docs/reviews/progression-math-2026-11-13.md` line 205 and `docs/reviews/frame-social-studies-kindergarten-2026-11-13.md`
  lines 127 to 128 and 141: dated update notes as Codex grade 1 (8) and Codex K (7) give them.
- `docs/PRODUCTION-PATH.md` step 2 puts `data/plans/<course>/source-map.csv` in the frame; the frame-write brief puts it
  in step 3. One of them should change.
- `data/modules/math.txt` line 8 and `data/coverage.csv` line 1837 still carry EK-ALG-ML-02; `build_db.py` rebuilds
  `data/modules.csv` from math.txt, so the dropped tag returns on the next build unless line 8 changes too.
- The Codex runner's Python lacks the `markdown` module, which stopped the grade 2 read.

## For Cory

- **Time a day (audience).** K to 2 math at 60 minutes a day, five days a week, 160 days, centers inside. A 45-minute
  path is not planned.
- **Assessment days (audience, time).** The frames keep one assessment day a unit against the base text's two. If a
  unit plan cannot fit its evidence, is an extra day allowed?
- **The saree silk reader (people, money).** Grade 2 unit 3, base lessons 3.11 and 3.12: who reads it, and any pay.

## Settled (for docs/reviews/DIGEST.md)

| Choice | Course | Reason |
|---|---|---|
| Ten-frame introduced in unit 2; K.4 adapted to use it, K.5.10 becomes the full 10-frame and missing to 10 | K | No second introduction; the rows use it in unit 4 |
| Unit 3's two added lessons: several attributes of one object, then the endpoint error | K | The base text has two length activities, not none; K.MD.A.1 in full |
| Position-word lesson K.3.13 first in unit 3, all six words | K | Social studies uses them about week 11 |
| K.G.B.4 begins with flat shapes in unit 3, owned in unit 7 | K | Thread starts where the base lessons use it |
| mk-one-to-one hands on to m1-count-to-120 | K, 1 | Both ends of the counting thread |
| EK-ALG-ML-02 off the math sort module | K | Math is the Common Core |
| Major work figures are a provisional allocation until unit plans give minutes | K, 1, 2 | Day and tag counts are not time counts |
| One assessment day a unit, with the evidence plan named in each unit plan; an extra day goes to Cory | K, 1, 2 | Own one-period assessments; one-to-one evidence in center days |
| Tape diagram taught by adapting grade 1 lessons 6.12 to 6.15, 8.6 as review; grade 2 builds it again from the bar graph | 1, 2 | Grade 1's base text names none |
| SL.1.2 lean points at e1-key-details; daylight data is a later science use | 1 | Matches what the standards ask |
| Grade 2 cuts made for the day budget; 2.3.17 kept, the estimating lesson dropped; six Curio Class lessons | 2 | Every cut day practises major work; estimating is in four base lessons |
| 1.G.A.3 and 2.G.A.3 written in full | 1, 2 | Standards in full |
