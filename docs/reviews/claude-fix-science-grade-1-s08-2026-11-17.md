# Fix report: science-grade-1 unit 8 (2026-11-17)

Findings merged: 12 (assessment 4, sources 3, sequence 5; no duplicates across lenses). Fixed 10, rejected 0, lead 2.
Held up per lens: assessment 4 of 4, sources 2 of 3 fixed (the third is a lead), sequence 4 of 5 fixed (the fifth is a lead).

Fixed in docs/courses/science-grade-1/s08.md: day 63 exit now uses a January 25 "light at noon" report, not the evening report (the evening report stays only on day 64); day 64 prompt no longer names the trap, look-for 4 scores pointing to the strips only; D sample re-worded and wrong-answer line splits B and D by stated reason; day 9 exit dated September 18 with the first part made new work; field 8 now has the token rule, the held-back and familiar-card preparation, and one shared class chart; day 62 row in U6 no longer repeats day 63's comparison; U3 now draws strips from the federal table and "Still to make" copies the values for every named date; Data read adds the Boston/Denver other-city rule.

Gate: unitplan.py check science-grade-1 s08.md PASS.

REJECTED: none

LEAD:
- days.csv: add the evening token (day 9 paper report card, cut flat) to day 63's supplies and a "keep out of mouths" safety line; add familiar seasonal evidence cards to day 64's supplies (sequence 1 and 2).
- Skeleton or frame: the generated "Why this unit, here" line ends mid-sentence ("returning to unit 1's sky"); regenerate or complete the frame text (sequence 5).
- Safety source in field 10 "Reads to prepare": replace the commercial sample-guide citation (page 7) with a published school science safety guide someone has actually opened; I did not name one unread (sources 1).
