# Fix report: algebra-ii unit 7 (Claude, fix stage, 2026-11-17)

Findings merged: 23 (assessment 9, sequence 8, sources 6; no duplicates across lenses except safety, sequence 6 and sources 6, merged). Fixed: 19. Rejected: 2. LEAD: 4 lines (one finding is lead-only, others partly lead). Held up per lens: assessment 9 of 9, sequence 7 of 8 (7 is lead-only), sources 5 of 6 (one rejected, one partly). Gate: PASS docs/courses/algebra-ii/s07.md.

What changed: E5 now prints a nine-row normal table extract and the other two histograms also have mean 52 and SD 6; E3 gains the friends clause and the printed E2 estimates; E2 gains a read-the-range prompt (about 190 of 200 means lie between 1.06 and 1.54, checked against seed 701); J reworded and the tally of 7 added; E7 sample for B replaced; retrieval key for rational rewrites corrected; day 137 repair fits inside main-task minutes; support for gaps A, N, O on days 137 to 139; K, N, O repair source named; Teaching line names the table step; tools lines (simulation on day 156, spreadsheet, safety); sources (no real poll, table and stream provenance, prompt 8 licence read, full student pages exist for lessons 1 to 16, reproduction functions and seeds named).

REJECTED: sources 4 | The progression is cited from an unofficial mirror; name the official host | The official host's address cannot be verified from here and the plan already says draft licence unverified, reference only, no quoted passage | none
REJECTED: sources 6 (second half) | Confirm the safety checklist is the current edition | Over the word cap (field 8 and 10 are at the cap) and the safety read already studies it | none

LEAD:
- days.csv day 156 tools column lists statistical simulation, but no student operates it; confirm or remove.
- days.csv day 155 supplies cell is empty; add the printed random stream or eight numbered outcome slips for the reassignment.
- days.csv day 139 tools: simulation follows the hand draw; and day 140 note should say what children with sampling gap A get on days 137 to 139 (the plan now states a support card and partner).
- docs/courses/algebra-ii/TOOL-ASKS.md does not exist; create it. Also days.csv goal for day 143 does not name the table step and the conversion to standard deviations that the plan now places there.
