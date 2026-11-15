# Fixes: scope and sequence of science-kindergarten, 2026-11-15

**Counts, applied / not applied:** expert 6/0; Codex 4/1; lead calls 5/0; band items 5/0; own findings 4/0. **Total: 24/1.** Overlapping sources are counted separately. Shared-file work is listed below.

Changed only `docs/courses/science-kindergarten/scope-and-sequence.md`, `docs/courses/science-kindergarten/frame.md` and `data/plans/science-kindergarten/days.csv`. Six units, their order, ownership, allocations and all 64 school-day placements remain unchanged. No source map is needed or created.

## Applied

- **Expert 1:** scope and sequence, frame and days.csv: six groups of five for 30 children, individual response mats/checklists, brief spoken reasons, named independent tasks and explicit minute budgets. Shade building/exposure precedes comparison.
- **Expert 2:** days.csv and scope and sequence: all ten fold-in days now answer new-case questions. Physical cases have matching supplies and safety controls; kinds and fold-in eligibility stay unchanged.
- **Expert 3:** days 14/19 and both documents: first complete live month counted on day 14; two live months compared on day 19. Another observer’s labelled picture records are reserved for a late start.
- **Expert 4:** days 60/61, year-end record notes and both documents: each child explains an effect on one or more surroundings; the class model includes all four. This follows the [official K-ESS3-3 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-ESS3-3%20Evidence%20Statements%20June%202015%20asterisks.pdf).
- **Expert 5:** both documents and mid-year notes: toy-car stopping before the rug’s edge replaces ball-to-bin. Under Collect once, this is an unscored transfer; recent unit 3 records are carried forward.
- **Expert 6:** scope and sequence and frame: allocations of $4, $2, $5, $8, $9 and $12 total $40. Added quantities, classroom-stock assumptions and reuse; allocations are planning limits, not retail quotations.
- **Codex 1:** both documents and days 29/30: minimal-materials and mid-year paths require each child to help plan, conduct and record physical push/pull investigations. Media cannot replace participation.
- **Codex 2:** both documents and days 17/19/29/30: regional hazard likelihood, observed patterns, prediction, preparation and response are explicitly taught and assessed, consistent with the [official expectation elements](https://www.nextgenscience.org/pe/k-ess3-2-earth-and-human-activity).
- **Codex 3:** course-level rows and prose: supported weather counts and actual morning/afternoon warmth patterns are explicit.
- **Codex 4:** scope and sequence: added the six-unit materials table, using the expert’s settled allocations.
- **Lead call, readiness/math:** scope and sequence: audited all 11 `assumes` cells, all empty. Listed same-year retrievals and retained math bridges; no earlier-grade readiness row exists.
- **Lead call, assessment rules:** both documents and days.csv: recent records are reused without re-scoring; fresh check forms and exact sampled codes replace whole-year claims. Every sampled code retains its required parts.
- **Lead call, frequency:** frame and scope and sequence: three meetings per week, keeping the existing 29-week placement and 64 days.
- **Lead call, shorter path:** scope and sequence: every fold-in states saved minutes; 64 meetings/1,920 minutes become 54 meetings/1,620 minutes.
- **Lead call, our words/source map:** scope and sequence: confirmed original planning prose and no adapted base lessons; recorded why no source map applies.
- **Band item, observation load:** frame, scope and sequence and closing rows: common small-group format with individual evidence and independent work.
- **Band item, rehearsal fold-ins:** ten days now use second cases while preserving the six-minute fold-in route.
- **Band item, costs:** per-unit allocations now match the band’s costing approach.
- **Band item, time:** three-meeting capacity confirmed; no week exceeds three numbered meetings.
- **Band item, course checks:** new samples replace repeated performances; carried records and response gains remain available for the grade 1 handoff.
- **Own 1, end-day load:** split full expectations across existing days: weather/forecast 18/19; problem definition/motion results 27/28; needs/model/argument 41/42/43; warming/shade 52/53–54.
- **Own 2, shorter-period feasibility:** added four-day observation windows for 20-minute periods and narrower, explicitly named course-level samples with carried records.
- **Own 3, stale lean timing:** frame: corrected math/ELA availability, needed-by weeks, weather-unit span and unit 4’s start.
- **Own 4, gate compatibility:** frame check-set cells retain the required `Candidate:` prefix while stating settled kept/dropped decisions and day costs.

All seven expert settlements are represented above. The engineering chain, kindergarten handoffs, picture-data progression and two-check-days-plus-response structure were confirmed and preserved.

## Not applied

- **Codex 5, shared rubric corrections:** deferred because `docs/RUBRIC-SCIENCE.md` is outside the owned files. Exact edits follow.
- Source-map conversion, religious-text and timer calls have no applicable instance in this course and are excluded from counts.

## Settled, for DIGEST

| Judgment | Reuse |
|---|---|
| Kindergarten has no earlier-grade science prerequisites | No readiness checks; same-year ideas open as retrieval |
| Plan observations for 30 children | Six groups of five, individual evidence and named independent work |
| Separate full expectations across final days | Use the day assignments above; response counted once |
| Collect once | Carry recent records unchanged; list only newly sampled check codes |
| Shade needs exposure time | Build/set out before comparing covered and uncovered patches |
| K-ESS3-3 individual scope | One or more affected surroundings; class model includes all four |
| Materials allocation | $40 total, with expert-set unit limits and reuse counted once |
| Shorter route | Ten unassessed second cases fold into neighbours; owned parts remain |

## For the structure pass

1. **`data/plans/frames.csv`, row `science-kindergarten` (line 40):** change `per_week` from `2` to `3`. Keep `weeks=29` and every other field unchanged.
2. **`data/standards/ngss-pe-dimensions.csv`, `K-ESS3-3,statement` (line 76):** replace the element  
   `Share ideas, by talking or drawing, for ways people can lessen their harm to local land, water, air and living things.`  
   with  
   `Share ideas, by talking or drawing, for ways people can lessen their harm to local land, water, air and/or living things.`
3. **`docs/RUBRIC-SCIENCE.md`, Gateway 2 full-scope row (line 66):** replace  
   `**Gap:** the practices, core idea and crosscutting concept statements are in no data file; data/standards/ngss-pes.txt holds codes only, and its terms must be checked before any text goes in`  
   with  
   `data/standards/ngss-pe-dimensions.csv holds own-word expectation elements. Verify their use in instruction and assessment; data presence alone does not establish coverage.`
4. **Same file, S5 (line 104):** replace  
   `A science teacher has not read safety and materials (FOUNDATION 7.3; until there are people, the course is not called finished)`  
   with  
   `The safety agent has not read every investigation's safety and materials against published school science safety guidance (FOUNDATION 7.3)`
5. **Same file, “Questions for Cory,” lines 185–187:** replace the science-teacher-read bullet with  
   `- **Safety and materials read.** Settled in FOUNDATION 7.3: the safety agent reads every investigation against published school science safety guidance before a course is called finished.`  
   Leave separately funded human-review provisions unchanged.

No kindergarten calendar placement edit is needed.

## For Cory

None.

## Gates

| Gate | Final result |
|---|---|
| `python -X utf8 scripts/sequence.py check science-kindergarten` | Passed, 0 failures |
| `python -X utf8 scripts/frame.py check science-kindergarten` | Passed, 0 failures; expected note that frames.csv is behind |
| `python -X utf8 scripts/frame.py calendar` | Passed; science checks remain weeks 14 and 29, no kindergarten stagger break |

Additional audits passed: unchanged counts/calendar positions, teaching before assessment, unassessed fold-ins, supplies/safety completeness and wording rules.

## Files changed outside the allowed set

- CONTRIBUTING.md
- README.md
- data/plans/README.md
- data/plans/flow-status.csv
- data/plans/later.csv
- docs/ADOPTION-BAR-SUBJECTS.md
- docs/ADOPTION-BAR.md
- docs/APPROACH-ELA.md
- docs/APPROACH-MATH.md
- docs/APPROACH.md
- docs/ECOSYSTEM.md
- docs/FOUNDATION.md
- docs/GAMES.md
- docs/HANDOFF.md
- docs/PRODUCTION-PATH.md
- docs/ROADMAP.md
- docs/RUBRIC-SCIENCE.md
- docs/SITE-DESIGN.md
- docs/VISION.md
- docs/agents/CODEX.md
- docs/agents/DAY-WRITER.md
- docs/agents/EXPERT.md
- docs/agents/decisions/BASELINE.md
- docs/agents/lenses/math.md
- docs/agents/lenses/science.md
- docs/courses/CALENDAR.md
- docs/courses/LESSON-DAY.md
- docs/courses/UNIT-PLAN.md
- docs/funding/COSTS.md
- docs/funding/ONE-PAGER.md
- docs/pilots/COST.md
- docs/pilots/README.md
- docs/pipeline/README.md
- docs/pipeline/briefs/plan-codex-read.md
- docs/pipeline/briefs/sensitivity-read.md
- docs/pipeline/briefs/sequence-write.md
- docs/reviews/continuity-review-2026-11-14.md
- scripts/course_pages.py
- scripts/unit_skeleton.py
