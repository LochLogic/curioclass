# Tile the Floor

## One idea
A tiler named Mr. Ito (made up, labeled "illustration") hands the child a house plan seen from above, and the child covers each room's floor with square tiles, no gaps and no overlaps, counting as they go (square inches for a dollhouse, square feet for a bedroom, square meters for a hall); as rooms grow, counting one tile at a time gets slow, so Mr. Ito offers a row tool: lay one row, count the rows, multiply, and check it matches counting; then L-shaped rooms get split into two rectangles whose areas add (4 by 6 plus 3 by 2 is 30), and a 6 by 7 kitchen splits as 6 by 5 plus 6 by 2 to show 6 times 7 as 6 times 5 plus 6 times 2; in the painters' job four painters share one 4 by 6 floor, and the child splits it into four parts with 6 tiles each, even when the parts are different shapes, and names each part 1/4 of the floor; at the end the house plan shows every room's area, so a third grader learns that area is the number of unit squares that cover a shape, to measure area by counting square units of different sizes, to relate area to multiplication and addition (including the distributive split and L-shaped rooms), and to split a shape into parts with equal areas and name each part as a unit fraction of the whole.

## Not like
- fence-builder (3, concept): perimeter, same family. Here area.
- area-model-builder (4, concept): multiplication by place value, same family. Here first area.
- garden-grid (2, spec): counting square plots. Here area as multiplication.
- equal-groups-zoo (3, concept): arrays as multiplication. Here arrays as area.

## Who and how
- Grade 3, Math, module "Area". Standards: 3.MD.5 (recognize area as an attribute of plane figures and understand concepts of area measurement: a square with side length 1 unit is "a unit square"; a plane figure covered without gaps or overlaps by n unit squares has an area of n square units), 3.MD.6 (measure areas by counting unit squares (square cm, square m, square in, square ft, and improvised units)), 3.MD.7 (relate area to the operations of multiplication and addition: tiling and multiplying side lengths; the distributive property shown with area models; area of rectilinear figures by splitting into non-overlapping rectangles and adding), 3.G.2 (partition shapes into parts with equal areas; express the area of each part as a unit fraction of the whole).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Twelve rooms (four tiled by hand, four with the row tool, two split, two L-shaped), the 6 by 7 kitchen split, three painters' floors, the house plan. Extra: Dream room (design a room and find its area). tool.json `modes: ["House", "Dream room"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3.MD.5, 3.MD.6 | Tile rooms in different square units; count | tiles covering; gap and overlap warnings | 2 |
| 3.MD.7 | Use the row tool; split the kitchen and L-shaped rooms | rows times columns; two rectangles adding | 3 |
| 3.G.2 | Split a floor into four equal-area parts | four parts of 6 tiles; "1/4 of the floor" | 4 |

## Screens and modes
Header (kit): title "Tile the Floor"; `House`, `Dream room`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A house plan from above with empty rooms, a stack of square tiles and Mr. Ito with a knee pad and a tape measure. The welcome is queued (`welcomeAfter: true`): "Hi, I'm Mr. Ito. Let's tile the dollhouse kitchen first. No gaps, no overlaps. Drag a tile onto the floor." First hint: "Drag a tile onto the kitchen floor."

**Tiling (focus: the room).** At 1366x768 the room fills the middle with tiles at the left and the area card at the right; at 680x425 the card folds under the room. Tiles snap to the floor grid; a gap shows a dashed outline, an overlap a red-and-striped corner. When covered: "How many square inches?" The child counts (tiles number as tapped) and types the area.

**The row tool.** For bigger rooms Mr. Ito offers `Lay a row`. One row of 7 drops in; `Copy row` fills the room row by row; the card writes 6 rows of 7 = 6 x 7 = 42. The child checks against counting once.

**Splits.** The 6 by 7 kitchen: a split line slides across; 6 x 5 and 6 x 2 light up; 30 + 12 = 42. L-shaped rooms: the child draws one split line and adds the two rectangles (24 + 6 = 30).

**Painters' job (3.G.2).** A 4 by 6 floor, four painters. The child draws borders so each part has 6 tiles; parts can be different shapes. Each part gets a label: 1/4 of the floor.

**Area is squares (the aha).** Mr. Ito lifts the tiles off a room and the grid stays: "Area is how many squares cover it. Multiplying side lengths just counts them all at once."

**The end.** The house plan with each room's area and unit. `Print` prints it.

**Dream room (extra).** The child draws a room on the grid and finds its area.

## Content
- Twelve rooms with sizes up to 8 by 9, four units (square inches, feet, meters and a made-up "cookie" unit), the kitchen split, three painters' floors, all read aloud with `Read`.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Tiles, rows and split lines can be removed at any time.
- Keyboard: Tab to tiles, the floor grid, row tools, split lines and the keypad; arrows move a tile; Enter places.
- With Motion off rows appear at once and tiles lift without floating.

## Look
- Accent `--brand` #7c4a24 terracotta brown (header, room walls, buttons); gold #f4c542 (the tile in hand, the split line); paper #faf4ef; ink #251307; muted #5b5049.
- Contrast (WCAG 2.1, computed): white on brand 7.34:1; brand on paper 6.73:1; ink on paper 16.39:1; muted on paper 7.16:1; ink on gold 10.99:1.
- Never color alone: gaps are dashed; overlaps are striped; painters' parts carry numbers.
- Different from this batch (cafeteria brick, garden green, mystery violet, lake teal).

## Art
- People (illustrated): Mr. Ito, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the house plan (1, 16:9), four tile textures (4, 1:1).
- Drawn in code: rooms, grids, tiles, split lines, the area card.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as Mr. Ito; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.room + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `tile`: "Drag a tile onto the floor."
- how `row`: "Tap Lay a row, then Copy row."
- how `split`: "Drag the split line across the room."
- how `paint`: "Draw borders so each painter gets the same number of tiles."
- event, whole, area is squares.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
area (family "area"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* AREA ENGINE: begin */ ... /* end */`: a unit grid with tiling, gap and overlap checks, row copying, split lines that report each rectangle's area, and region painting; fence-builder and area-model-builder reuse them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Area | Type a guess | The tiles count themselves on a miss and the room repeats with new sizes. |
| Split | Draw any line | The two areas must add to the whole; the card shows the sum. |
| Painters | Make four parts of any size | Each part must have 6 tiles. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `tile`.
2. `row`.
3. `split`.
4. `paint`. Area is squares (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 3.MD.5 to 3.MD.7 and 3.G.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Seeing rows of unit squares links area to multiplication | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-5 Geometric Measurement" | Battista and others (1998), "Students' spatial structuring of 2D arrays of squares", Journal for Research in Mathematics Education | yes |
| Area models show the distributive property | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-5 Geometric Measurement" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r10, 2026-11-10): 6 x 7 = 42 = 6 x 5 + 6 x 2; 4 x 6 + 3 x 2 = 30; a 4 by 6 floor splits into four parts of 6, each 1/4; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 room, tiles and card; at 680x425 card under room.
2. Four rooms are tiled by hand in different square units. (3.MD.5, 3.MD.6)
3. Rows times columns, the kitchen split and two L-shaped rooms are done. (3.MD.7)
4. Three painters' floors are split into four equal-area parts and named 1/4. (3.G.2)
5. `Read` reads every card; every control is 48 px or more.
6. Mr. Ito is labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
- The idea card moves 3.G.2 here from shape-family-tree (default used: this tool teaches 3.G.2 through the painters' job; shape-family-tree keeps 3.G.1).
