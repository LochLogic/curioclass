# Section refine: math-grade-1 unit 7 (sections 7.1 to 7.4)

Date: 2026-11-27. The skeletons were rebuilt first (`section_skeleton.py math-grade-1 u7`) and not edited.

## Faults

| File | Fault | Fix or rejected (why) | Stage |
| --- | --- | --- | --- |
| u07-2.md, day 134 Geometry | s07-AR1-rect needs children to mark the tilted square as a rectangle, but no day taught that a square is a rectangle. The unit plan asks for "squares as rectangles". | Added: "Say that a square is a rectangle too: four straight sides and four square corners." | write |
| u07-2.md, day 135 Observations | The 16-minute observation block did not say what children 17 to 30 do. | Added: they keep making unscored flat copies at their tables. | write |
| u07-2.md, day 136 Observations | Same gap for children 1 to 16. | Added: they continue seam checks on familiar practice stock. | write |
| u07-3.md, field 1 | Said "some equal-area pieces have different shapes". That is a grade 2 idea (2.G.A.3), and the S1 rectangle leaned on it. | Every printed share now matches its partners when stacked. Different-shape equal shares are marked as waiting for grade 2. | prep |
| u07-3.md, field 3 S1 reservations and s07-AS1-r4 | The four-share rectangle used both diagonals (equal area, shapes that do not match). | Now a center line and one diagonal in each half, giving four matching triangles. The Shape line copies the new data. | prep |
| u07-3.md, field 9 | Said the four diagonal triangles "need not match". | Rewritten: one diagonal for halves, a center line and a diagonal in each half for quarters. Both diagonals stay out. | prep |
| u07-4.md, field 3 "S1 on 146" | A second, different set of S1 Shape lines (two Shape lines per item across sections). | Replaced with exact copies of 7.3's ten lines. Script check: 0 mismatches with 7.3 or items.csv. | write |
| u07-4.md, field 6 day 146 | The s07-AS1-r4 copy still said both diagonals. | Updated to match field 3. | write |
| u07-3.md, exit s07-X139a | The answer-key read found that star size cued the smaller share in the exit picture. | The fix is in the piece (exit-139.md). The plan text needed no change. | write |
| u07-1.md | Re-checked minutes (60 per day), exits, keys, wrong-answer letters, terms, owed codes and plain words. | No fault found. | none |
| All four, "gap" | A check for "gap" used to mean difference. | Rejected: every use means a physical opening in a shape or seam, not a comparison. | none |

Also checked and clean in all four plans:
- Part minutes add to each day's total.
- Turn counts suit about 30 children with a hand-back. Day 135 has 8 one-minute turns per group. Days 138 and 140 have 15 one-minute turns. R4 has 10 turns of 90 seconds per 15 minutes. The day 146 check is 5 + 20 + 16 + 15 + 4.
- Each wrong answer carries exactly one s07 register letter.
- Terms are taught before they are tested.
- Each stem has one ask.
- The unitplan.py check covers the 1,600-word cap.

## Ledger

- Fixed the note on the u07-3 row "S1 diagonal window stock and reason". It now says the rectangle quarters use a center line and a diagonal in each half, and that both diagonals wait for grade 2.
- Added a u07-2 case row, "134 a square is a rectangle too" (day blank).
- Not added: a new note on the u07-2 term row "rectangle". `ledger.py note` matches rows by course, day and entry, and blank-day "rectangle" rows exist in both 7.2 and 7.3. The new case row carries the fact instead.

## Gates

- `unitplan.py check math-grade-1`: PASS for s07 and u07-1 to u07-4.
- `ledger.py check math`: 0 problems, 0 planned-only findings, 0 unmatched citations.
- `gate.py --course math-grade-1`: 580 failing lines, the same as the baseline. 0 new failing findings.
- No em dash and no writer placeholder in the edited files.

## Plan points (unit plan or data I may not edit)

- s07 (field 5 and the U-fields) still describe the S1 four-share rectangle with both diagonals. They should say a center line and one diagonal in each half, and that different-shape equal shares are 2.G.A.3.
- s07 U3, row 136, still says "two-triangle square motif". The exit uses a band-and-panel square because kindergarten used the two-triangle join. The ledger already records this.
- s07-X145b (count the squares) is held for the 2 + 2 reuse, but exit-box-145 still prints it. This is recorded as held, and the unit plan should say whether to drop it from the piece.
- The U3 rows for 140 and 145 differ slightly from the exits as written. For 145, the count is held.

## Changed for the next unit

- Keep grade 1 equal shares congruent, so they match when stacked. Equal shares with different shapes (for example, both diagonals of a long rectangle) are 2.G.A.3.
- After any change to a wrong answer or an answer in the data, rebuild the teacher key lines. Five had drifted here.
- Keep printed marks such as stars the same size across a comparison pair.
- One Shape line per item: a later section reusing an item copies the first section's field 3 lines word for word.
- Teach "a square is a rectangle" outright before an item needs it.
- In observation blocks, say what the children not being observed are doing.
