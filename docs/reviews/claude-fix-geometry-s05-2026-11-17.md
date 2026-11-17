# Fix: geometry unit 5 (s05), 2026-11-17

Findings merged: 20 (assessment 8, sources 5, sequence 7; no fault was named by two lenses). Fixed 11, rejected 7, lead-only 2 (S2, A5 partly overlap the lead list). Held up per lens: assessment 6 of 8 (A5 is lead-only, A7 and A8 rejected on the word cap), sources 3 of 5 (S1, S5 fixed; S2 lead-only; S3, S4 rejected on the cap), sequence 4 of 7 (Q1, Q2, Q6, Q7 fixed; Q3, Q4, Q5 rejected). The plan sat at 1,229 of 1,250 counted words, so only 21 words of new text in counted fields fitted; fields 4 and 5 are uncounted and took the larger fixes.

Fixed in docs/courses/geometry/s05.md:
- A1: added a two-minute scaling item to the E4 row (key 4 and 8; 4 and 64; error B); E3b, E3e cut from 3 to 2 minutes so the ten remaining explanation and interpretation minutes still add up.
- A2: sphere in E4 now given by diameter 12 (key 288 pi unchanged), so 2304 pi is H.
- A3: E3c now supplies an oblique cylinder (base area 20, slanted edge 14, perpendicular height 11, key 220; 280 is C).
- A4: E5 prototype now gives inner and outer pairs; outer pair gives about 660.1, outside tolerance (K).
- A6: E1 rectangle rotation replaced by a rectangle with a semicircle cap (cylinder capped by a half sphere).
- Q1: Handoffs now says day 92 uses unit 4 trigonometry.
- Q2: Teaching now says day 88 teaches choosing a length multiplier, day 89 practises it.
- Q6: field 4 pipeline remark replaced by the reader-facing reason R2 and R3 sit in day 81's single window.
- Q7: "printed root tables" changed to "hand-built root tables" (students build tables on days 86 and 88), so no unlisted supply is needed.
- S1: field 10 Progressions now names PDF page 12 (E3a).
- S5: field 10 now replaces named companies and buildings in lessons 11, 15, 16 with invented cases.

Gate: `unitplan.py check geometry`: PASS docs/courses/geometry/s05.md (1,250 of 1,250 counted words).

REJECTED: assessment 7 | 7.G.B.4 has no field 5 row and the plan never says it is an unscored contribution; add a Limits sentence | A true gap, but the plan has 0 words of headroom after the higher-priority fixes and no content can be cut | over the word cap (UNIT-PLAN Length); days.csv day 90 already says "contribution, not assessed here"
REJECTED: assessment 8 | The respond groups lump seven letters into one group; say each group opens with its letters' Repair lines | Register repairs exist and the four-group cap is kept; the sentence needs about 17 words the plan cannot hold | over the word cap (UNIT-PLAN Length)
REJECTED: sources 3 | Readiness repair sources (grade 7 unit 7 lessons 11 and 12, circle and grade 8 summaries) are not listed in field 10 with address and licence | Needs about 30 words; the plan has none to spare and may not drop existing lines | over the word cap (UNIT-PLAN Length)
REJECTED: sources 4 | Day 83 and 84 safety lines (thread, scissors, string) cite no standard; add the California Department of Education tools page to Reads | Needs about 20 words; the safety agent already studies materials against the cited guide and the page was not checked here | over the word cap (UNIT-PLAN Length)
REJECTED: sequence 3 | Rotation (G-GMD.B.4 b) is taught on day 82 only; add a return on day 96 to Carried | Adds content to a day whose goal and codes (days.csv) do not carry it; moved content, and no word budget | UNIT-PLAN rule 12 is met by E1 as the check; the writer's brief (no moved content)
REJECTED: sequence 4 | F-IF.C.7b part c (piecewise, step) is taught nowhere; add a step practice on day 97 or 98 | Needs new content in days 97 or 98 (no moved content), and over the word cap; day 99 already carries it with retrieval and the Limits say the families were taught in grade 9 | the writer's brief (no new content in days)
REJECTED: sequence 5 | Days 90, 94 and 99 hold more than their minutes allow; say what yields | The unit plan does not budget minutes (section plans do) and the plan has no words left | UNIT-PLAN field 5 note that section plans budget minutes; over the word cap

LEAD:
- days.csv days 90, 94, 98 and 101 notes, and the scope-and-sequence unit 5 Evidence paragraph, say first-teaching records are "retained" and "reused" on day 101; UNIT-PLAN field 5 forbids scoring them. Change to "formative; day 100 and day 101 supply the scored fresh evidence", then regenerate the Evidence skel line (assessment 5).
- source-map.csv unit 5 title column holds our labels, not Illustrative Mathematics titles (real: L1 Solids of Rotation, L2 Slicing Solids, L3 Creating Cross Sections by Dilating, L4 Scaling and Area, L5 Scaling and Unscaling, L6 Scaling Solids, L7 The Root of the Problem, L8 Speaking of Scaling, L9 Cylinder Volumes, L10 Cross Sections and Volume, L11 Prisms Practice, L12 Prisms and Pyramids, L13 Building a Volume Formula for a Pyramid, L14 Working with Pyramids, L15 Putting All the Solids Together, L16 Surface Area and Volume, L17 Volume and Density, L18 Volume and Graphing); add a note that lessons are found by unit and number (sources 2).
- days.csv day 92 skills: add geo-right-triangle-trig (sequence 1).
- days.csv day 88: add G-MG.A.3 to codes and the length-multiplier choice to the goal (sequence 2).
- days.csv day 96: add rotation to the goal and G-GMD.B.4 to codes (sequence 3); a step or absolute value practice before day 99 (sequence 4); both may need the 1,250-word cap relaxed or other text cut to be written into the plan.
- Decide whether R2 (m7-circles) should become day 90 retrieval only, since the rule table says retrieval (sequence 6).
- Unit plan word cap: s05 is at exactly 1,250; the rejected cap items (assessment 7 and 8, sources 3 and 4, sequence 5) need room if the lead wants them.
