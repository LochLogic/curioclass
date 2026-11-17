# Fix report: social-studies-grade-2 unit 1 (s01.md), 2026-11-17

Findings merged: 28 (assessment 13, sources 7, sequence 8; no two lenses named the same fault). Fixed 24, partly fixed 4, rejected 0 outright. Gate: `unitplan.py check social-studies-grade-2` PASS for s01.md (s02 and s07 fail on files that are not this unit's). Held up per lens: assessment 13 of 13, sources 7 of 7, sequence 8 of 8; four fixes are partial because of the word cap (below).

Fixed in the plan:
- Assessment 1: component-to-repair table with four groups added after field 6 (field 7 points to it); marking given as about three teacher minutes a child (ours, untested). Partial: the table is by item, not by every sub-component, and sits after field 6 because field 7 is inside the word cap.
- Assessment 2 to 5, 9, 11, 12 and sequence 1 to 3: exits for days 5, 7, 8, 9, 10, 11, 12, 13 and 16 rewritten as fresh tasks with at most two parts; day 12 now asks for five labels including a river; day 13 mark is "draw one more mark" so the wrong answer is letter O; gap reteaches cut to five minutes in the warm-up (item 1 day 2, item 2 day 3, item 3 day 6, item 4 day 5); repairs for E, J and M moved to the day 8 warm-up; the repair sentence under field 6 now says five minutes in the warm-up.
- Assessment 6, 7, 8, 10, 13: item 2 uses Map X and Map Y with a taught clue; item 3 and 4 minutes parentheticals removed, fresh counts made on day 14 in the same room or school part; owners set by section; G reworded; Willow Garden caption changed to the path sentence.
- Sources 1, 4, 6, 7: item 5 marked provisional until the imprint is read, key worded "as printed", Commons credit given with the seller left out; Tennessee row neutral; New York edition named; photograph credit pattern added (field 5, exempt from the cap).
- Sources 2, 3: Boulder margin read and rights check made a to-do before day 6's key (field 4); coastline dataset, Gall-Peters form and credit line added to the packet (field 5). Partial: the dataset is named "from memory" (Natural Earth) and still needs its licence checked, and the Boulder margin has not been read.
- Sources 5: sensitivity study list added in short form (reached and not reached). Partial: the lens asked for what the answer-key read and expert's text read study; only the reached and not reached marks fit the cap.
- Sequence 4, 5, 6, 7, 8: day 12 practice-only note added to the day 12 exit row (field 5) in place of field 2; supplies gain equal strips and the paper shell opening method; closing claim wording on day 15 and the marking line drop "each child's"; supporting question 4 now day 13; Returns line for unit 2 day 18 added in field 4.
- Sequence 2: day 1 retrieval row trimmed to the supporting-question prompt (key and directions are retrieved by check items 1 and 2), day 1 minutes added, and the first line says why it is a check.

Line endings: the file had CRLF in places; it is now LF throughout.

REJECTED: none

LEAD:
- days.csv day 1 is marked `readiness` and also carries a retrieval note; confirm which is meant.
- days.csv codes day 12 MA.2.T1.1; consider noting the check-set addition (practice only, no end-of-unit item) in its code or note.
- days.csv day 15 goal says "say which projection a world map uses"; the plan now uses unlabeled Map X and Map Y with a taught clue, so reword it.
- days.csv or any day text that still says "room counts" for day 14 should say the familiar place the map shows (same room or school part).
- A person reads the federal projection page and the Boulder and Vermont map margins; the plan marks them not reached.
- The retrieval table row in field 4 and the field 4 first line for unit 1 may need the unit-plan checker's wording reviewed if a later gate objects.
