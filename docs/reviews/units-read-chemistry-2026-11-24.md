# Units read: chemistry, 2026-11-24

COURSE-RUN stage 4 (Reads), expert pass across all eleven chemistry unit plans.

## What was read

- docs/courses/chemistry/scope-and-sequence.md and s01.md to s11.md (fields 2 to 10, U3 to U11), read together.
- data/plans/chemistry/days.csv (kinds, loads, respond and end days).
- Continuity edges: docs/courses/biology/s10.md field 3 (below) and docs/courses/physics/s01.md head and field 3 (above).
- docs/reviews/codex-write-lens-assessment-chemistry-s11-2026-11-16.md (its finding 1 named the s11 transfer timing fault).
- docs/reviews/lead-list-lens-pass-2026-11-17.md: no chemistry LEAD items or CAP rejections.

## Verdict

The course arc holds: particles and the table, bonding and reactions, energy, rates and equilibrium, then Earth-system chemistry and resource decisions, with clean hand-offs from Biology's Earth-life feedback and into Physics' energy and forces. Loads match days.csv kinds, every readiness hand-back has both ends, and goal verbs line up with exits and practice. The serious fault was in the last two units, where the end-of-unit transfer case was released and drafted days before the end day, contradicting days.csv's unseen end-day response and leaving no revision before scoring. Smaller faults were one-ended return links where a later row claims to build on an earlier unit without retrieving it.

## Findings

| # | Plan | Severity | Finding | Verdict |
|---|---|---|---|---|
| 1 | s11 | High | Harbor Ridge settlement transfer released and drafted on day 152, two days before the day 154 end day that days.csv marks as an unseen-case response. | Fixed: settlement records stay unseen through day 153; item 1 drafted on day 154, revised in day 155's fifteen minutes and scored after; item 2 (resource designs) stays the day 152 product revised on day 153. Field 2, field 5 practice shapes, U6 rows 152 to 154 and field 7 aligned. |
| 2 | s10 | High | Same fault: transfer packet released and drafted on day 140, revised on days 141 and 142 before the day 142 end day. | Fixed: packet unseen through day 141; transfer drafted on day 142, revised in day 143's ten revision minutes and scored after; day 140's thirty minutes now justify claims from outputs taught on days 137 to 139; field 7 marking adds the post-day-143 scoring. |
| 3 | s05 day 62 | Low | Attraction explanation leans on unit 2's attraction model without retrieving it. | Fixed: two-minute retrieval of the unit 2 model. |
| 4 | s05 day 64 | Low | Energy-spreading collection assumes unit 3's water storing energy with no retrieval. | Fixed: one-question retrieval in the opening five minutes. |
| 5 | s09 day 122 | Low | Feedback analysis builds on unit 6's stability-change contrast without returning to it. | Fixed: added to the three-minute opening retrieval. |
| 6 | s09 day 123 | Low | Runoff feedback case relies on unit 3's stream-table runoff evidence, unretrieved. | Fixed: opening retrieval added. |
| 7 | s10 day 135 | Low | Weathering pathway in the revised model depends on unit 3's carbonate dissolution and weathering, unretrieved. | Fixed: opening retrieval added. |
| 8 | s10 day 137 | Low | Row reteaches the measurement-versus-projection distinction already taught on unit 9 day 125. | Fixed: retrieve, not reteach. |
| 9 | s04 | Note | Wording in the reaction-energy rows is uneven but accurate. | No change: meaning is clear; not worth words against the cap. |
| 10 | s03 | Note | Its draft-feedback-revise pattern differs from units 1, 4, 6 and 9. | No change: drafting and scoring days are still separate, so the scoring rule holds. |
| 11 | all | Note | Goal-verb drift between field 5 and exits checked across all plans. | No change: none beyond findings 1 and 2. |
| 12 | sequence gate | Note | 25 "reads like hands-on work but names no supplies" notes (for example days 98 to 101, 137, 142, 157, 158). | No change: these are planning, records or assessment days with no new procedure; notes are advisory and pre-existing. |

Counts: fixed 8, no change 4, day fault 0 (no day files exist), for the structure pass 0, for Cory 0.

## For the structure pass

None.

## For Cory

None.

## Lead items worked

0 (none listed for chemistry): fixed 0, no change 0, rejected 0.

## Gate results

- `scripts/unitplan.py check chemistry`: PASS on s01 to s11. Words outside the uncounted fields after edits: s01 1665, s02 1800, s03 1635, s04 1610, s05 1735, s06 1687, s07 1663, s08 1540, s09 1739, s10 1502, s11 1574, all under the 2,300 cap.
- `scripts/sequence.py check chemistry`: 0 failures, 25 advisory notes (finding 12).
- `scripts/goalmap.py audit chemistry`: ran clean (exit 0); maps read for finding 11.
