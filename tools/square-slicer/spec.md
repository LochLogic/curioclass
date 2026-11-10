# Square Slicer

## One idea
A builder named Mr. Ahmadi (made up, labeled "illustration") will only trust the rule for right triangles if he sees it, so on his workbench sits a right triangle with a square on each side and a cutting tool, and the child cuts the two smaller squares into pieces and slides them until they fill the square on the long side exactly, level after level of classic dissections, then tries the same with a triangle that is not right and finds the pieces never fit; converse levels take the child to his deck frame, where corners are checked with 3-4-5, 6-8-10 and 5-12-13, and one corner measuring 6, 8 and 10.2 feet is caught as not square; missing-side levels use what the cuts proved: a 13 ft ladder with its foot 5 ft out reaches 12 ft up the wall, a TV 48 inches wide and 27 tall has a diagonal of about 55 inches, and in 3D the longest pole that fits corner to corner in a 3 by 4 by 12 ft moving truck box is 13 ft; park-map levels put two benches at (1, 2) and (7, 10) on a coordinate map and the child draws the right triangle on the grid (6 across, 8 up) to find the 10-unit shortcut; at the end the child sees that the two small squares really do fill the big one, only for right triangles, and that one fact measures distances everywhere, so an eighth grader learns to explain a proof of the Pythagorean theorem and its converse, apply it to find unknown sides in two and three dimensions, and find distances between points on the coordinate plane.

## Not like
- ramp-and-roof (10, spec): trigonometry. Here the Pythagorean theorem.
- fire-lookout-triangles (12, spec): laws of sines and cosines. Here right triangles only.
- blueprint-studio (7, spec): building triangles from measures. Here proving and using one fact.
- sea-search-grid (5, spec): plotting points on a grid. Here distance between them.

## Who and how
- Grade 8, Math, module "The Pythagorean Theorem". Standards: 8.G.6 (explain a proof of the Pythagorean Theorem and its converse), 8.G.7 (apply the Pythagorean Theorem to determine unknown side lengths in right triangles in real-world and mathematical problems in two and three dimensions), 8.G.8 (apply the Pythagorean Theorem to find the distance between two points in a coordinate system).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Five dissection levels and one non-right check, six deck corners, eight missing-side problems, six park-map shortcuts. Extra: Cut gallery (students share their own cuts on the projector). tool.json `modes: ["Workbench", "Cut gallery"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 8.G.6 (proof) | Cut and slide squares to fill the big one | pieces fitting exactly; never for a non-right triangle | 2 |
| 8.G.6 (converse) | Check deck corners by side lengths | 6, 8, 10.2 caught | 2 |
| 8.G.7 | Find missing sides in 2D and 3D | the ladder, the TV, the truck box | 3 |
| 8.G.8 | Draw grid triangles between points | the 10-unit shortcut | 4 |

## Screens and modes
Header (kit): title "Square Slicer"; `Workbench`, `Cut gallery`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A sunny workshop, a workbench with a right triangle and three squares, a cutting tool, and Mr. Ahmadi in a tool belt. The welcome is queued (`welcomeAfter: true`): "If these two squares fill that one, I'll trust the rule. Tap the cutter, then tap a square to cut it." First hint: "Tap the cutter."

**Dissect (focus: the bench).** At 1366x768 the bench fills the left with the level card right; at 680x425 the card is a sheet. Cuts follow guide lines for each level (Perigal's cut, the four-triangle rearrangement, Bhaskara's square, a 3-4-5 grid count, a free level). Pieces slide and turn; a fill meter counts uncovered area. The non-right level shows a gap or overlap that never closes.

**Deck corners.** A deck frame from above with six corners; the child measures the two sides and the diagonal and marks each "square" or "not square", with a reason using squares.

**Missing sides.** Eight problems: ladder, TV, ramp, kite string, a phone screen, a roof brace, the truck box pole (two steps: floor diagonal first, then up), a tent pole.

**Park map.** A coordinate map with benches, a fountain and a gate. The child taps two points, drags the right triangle onto the grid, and types the distance.

**Only for right ones (the aha).** Mr. Ahmadi: "The two small squares fill the big one, every time, but only when the corner is square. That one fact measures everything."

**The end.** The gallery of cuts and the measured deck. `Print` prints them.

**Cut gallery (extra).** Shared cuts.

## Content
- Lengths in feet and inches, answers rounded to a tenth when not whole, all readable with `Read`.
- Dissections named after their makers with dates in the level card.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pieces can be moved, turned and uncut until the fill meter reads zero.
- Keyboard: Tab to the cutter, squares, pieces (arrows move, R turns), deck corners, answer boxes and map points; Enter cuts, places or checks.
- With Motion off pieces jump to place.

## Look
- Accent `--brand` #5b6420 timber olive (header, the cutter, buttons); gold #f4c542 (the piece in hand, a square corner); paper #f5f6ea; ink #1a1d05; muted #53554a.
- Contrast (WCAG 2.1, computed): white on brand 6.39:1; brand on paper 5.85:1; ink on paper 15.76:1; muted on paper 6.96:1; ink on gold 10.57:1.
- Never color alone: square corners carry a corner mark and "square"; uncovered area shows a hatch.
- Different from this batch (puzzle plum, glacier blue, harbor teal, cranberry).

## Art
- People (illustrated): Mr. Ahmadi, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the workshop (1, 16:9), the deck from above (1, 4:3), the park (1, 4:3).
- Drawn in code: every square, piece, cut and grid, because cuts must fit exactly.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as Mr. Ahmadi; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.piece + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `cut`: "Tap the cutter, then tap a square to cut it."
- how `slide`: "Drag a piece into the big square."
- how `corner`: "Tap Square or Not square."
- how `side`: "Type the missing side."
- how `map`: "Tap two points, then drag the triangle onto the grid."
- event, whole, only for right ones.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: polygon cutting along guide lines, piece sliding and turning with exact area accounting, the fill meter, the deck checker. The park map uses kit:graphing `Plane` and `g.point` as described in two-trains' spec.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Dissection | Pile pieces on top | Overlap counts against the fill meter. |
| Corners | Mark every corner square | The 10.2 corner is built to catch it. |
| Truck box | Use the floor diagonal only | The answer needs the second step up. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `cut`; `slide`.
2. `corner`.
3. `side`; `map`.
4. Only for right ones (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 8.G.6 to 8.G.8 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Dissection proofs of the Pythagorean theorem (Perigal, Bhaskara) | Loomis (1968), "The Pythagorean Proposition", NCTM | Nelsen (1993), "Proofs Without Words", Mathematical Association of America | yes |
| The converse: sides with a squared + b squared = c squared meet at a right angle | Euclid, "Elements", Book I, Proposition 48 | Loomis (1968), "The Pythagorean Proposition", NCTM | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s21, 2026-11-10): 3-4-5, 6-8-10 and 5-12-13 satisfy a squared + b squared = c squared, and 6, 8, 10.2 do not; the 48 by 27 TV diagonal is about 55.1; the 3 by 4 by 12 box diagonal is 13; (1, 2) to (7, 10) is 10; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bench and card; at 680x425 card as a sheet.
2. Five dissections fill the big square, the non-right check fails, and six corners are judged by the converse. (8.G.6)
3. Eight missing sides are found, including a 3D diagonal. (8.G.7)
4. Six map distances are found from grid triangles. (8.G.8)
5. Pieces are exact; areas always add up.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: pieces jump; no network requests.

## Open questions
None.
