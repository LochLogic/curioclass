# Box Packer

## One idea
A food-bank crate fills a layer at a time: each layer is the same rows-by-cubes array, so the cube count is one
layer times the number of layers, and turning the full crate onto another side changes the layer and the layer count
but never the total.

## Not like
- egg-carton-factory (gr 4, puzzle, spec): a fixed egg count searched for every flat rectangle (factor pairs, prime or composite). Here the box is fixed and the count is what you find, in 3D, by layers; no factor search, no prime talk, a cool concrete back room with beet accents (egg-carton is a warm daylight shed, meadow green).
- tile-the-floor (gr 3, puzzle, concept): covers flat rooms with square tiles for area, and splits L-shaped rooms. Here every count is cubes in a solid, the second multiplication is the layers, and an L-shaped shelf is two boxes with depth.
- net-folder (gr 6, sandbox, concept): unfolds boxes into nets for surface area and fills them with half-inch cubes. Here only whole cubes, no nets and no surface area; the outside squares are the common wrong answer, never a measure.
- area-model-builder (gr 4, sandbox, concept): slices flat rectangles at place-value breaks to multiply. Here the pieces are boxes and the cut only shows that volume adds.
- how-many-fit (gr 6, sandbox, concept): fraction bars in a container for division. Here nothing is fractional.
- growth-spurt (gr 4, simulator, concept): packs seedlings into flat trays with remainders. Here a crate is always packed full; empty spaces are counted, never interpreted.
- grocery-run (gr 5, builder, concept): prices food for a field day. Box Packer has no money and no budget; the food bank is only the setting.

## Who and how
Grade 5 math, module math-5-volume. Driver: students (solo by default) or teacher on a projector. 20 to 40 minutes.
Standard 5.MD.C (5.MD.3a, 5.MD.3b, 5.MD.4, 5.MD.5a, 5.MD.5b, 5.MD.5c). No personal prompts. Grace, Ruth, the food bank
and every crate size are made up; the panel footer says "Grace, Ruth and the crates are made up for practice." The
food bank is shown as a busy, cheerful place where neighbors pick up groceries; no line talks about who needs food or why.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5.MD.3a unit cube is 1 cubic unit | Pack: drop single cubes; the scale chip names the cube | the chip "1 cube = 1 inch on every edge = 1 cubic inch"; the full readout names "cubic inches" | Bean crate full reads "Volume: 60 cubic inches"; Spice box (Pack) reads "cubic centimeters" |
| 5.MD.3b n cubes, no gaps, no overlaps, is n cubic units | Pack: the counter counts empty spaces until none are left; Cube Sizes: Cans leave gaps; Shelves: Ruth's count double-counts the corner | "17 cubes packed. 43 spaces still empty."; cans with shaded gaps; the red corner "counted twice" | Cans show 12 cans and the line "cans can't measure volume"; Ruth's count shows the red corner and a total 12 too big on shelf 1 |
| 5.MD.4 count cubic cm, in, ft, improvised units | Pack crates in in, cm and ft; Cube Sizes measures one box in 1 inch cubes, 2 inch and 4 inch blocks; Puzzles level 3 | the same box: 768, 96, 12; a block opens into 8 or 64 inch cubes | Puzzle 3a (8 x 6 x 4 in, 2 inch blocks) passes only with 24 blocks and 192 cubes |
| 5.MD.5a pack, then multiply; base x height; associative property | Pack: cube, then row, then layer, then Fill it; Turn the crate; Puzzles levels 1 and 2 | layer labels "4 by 3 = 12", tally 12, 24, 36; after turns the Ways list "(4 x 3) x 5", "(4 x 5) x 3", "(3 x 5) x 4" all 60 | Turning the full Bean crate twice lists three ways, each 60; Puzzle 2 passes only with two different faces, each base x height right |
| 5.MD.5b V = l x w x h and V = B x h in real problems | Puzzles level 4: food bank bins in cubic feet (find a height from a base; build a bin for an amount under a height limit; a square-based bin) | bin edges labeled in feet; no count shown until Check | Puzzle 4b (24 cubic feet, at most 2 ft tall) passes with 4 x 3 x 2 or 6 x 4 x 1, and fails with 4 x 3 x 3 (missTall) and 5 x 5 x 1 (missBin) |
| 5.MD.5c volume adds; composite of two boxes | Shelves: cut an L-shaped shelf two ways, fill both parts, add; Puzzles level 5 | "36 + 12 = 48" and "24 + 24 = 48" in the Ways list | Shelf 1: Cut 1 and Cut 2 both total 48; Puzzle 5c rejects Ruth's total with missRuth |

## Screens and modes
Header: title, mode buttons **Pack**, **Cube Sizes**, **Shelves**, **Puzzles**, then kit Motion, Sound, Read. Grace's
portrait sits at the top of the panel beside the hint (hidden at 680x425). Panel footer: the made-up line.

On load: Pack, the Bean crate (4 long, 3 wide, 5 tall, inch cubes), empty. Nothing plays before the first tap. Hint:
"Tap the crate to drop in a cube, or tap Add a layer. Pack it full with no gaps." The first tap on the crate (or Add a
cube) drops the first cube (the main path); a first tap on Add a row, Add a layer or Fill it does that at once. The
welcome (wPack) queues after a first tap with no line of its own and may be cut (rule 16); its premise (full, no gaps)
is in the hint and Read.

**Pack** (explore). Focus: the crate, centered in the stage, drawn in code in isometric view (length runs down to the
right, width down to the left, height up). Cube size s = the smaller of 64 px and what fits (Look); the Bean crate is
61 px at 1366x768. The crate's floor and two back walls carry the kraft texture with a faint dashed 1-cube grid, the
front is open, and its three outer edges are labeled ("4 in", "3 in", "5 in"). Beside it, at the right edge of the
stage, the layer tally strip (80 px) stacks one chip per finished layer, bottom up, with running totals (12, 24, 36).
The readout sits under the crate. Panel: crate name with **Next crate**; **Length - / +** (1 to 10), **Width - / +**
(1 to 8), **Height - / +** (1 to 8), also drag handles on the three labeled edges (one cube of drag per step, arrow
keys when focused); unit buttons **Inches**, **Centimeters**, **Feet**; the scale chip; **Add a cube**, **Add a row**,
**Add a layer**, **Fill it**, **Empty**, **Turn the crate**; a **My guess** box (optional); the Ways list.
Packing order is fixed: the first cube goes in the back left corner of the floor, a row runs along the length, rows
step toward the front, and a full layer starts the next one up from the back. Tapping the crate is Add a cube. Add a
row finishes the current row; Add a layer finishes the current layer; Fill it packs layer after layer (0.3 s each, 2.4 s
at most). Cubes are colored by layer, alternating squash and sky, with dark edges. A finished row gets a bracket "a row
of 4" (first row of each layer only); a finished layer gets its label "4 by 3 = 12" and its tally chip. Full: a
chime, the crate rim turns green with a check, and the full readout. **Turn the crate** (enabled only when full) lays
the crate on its next side (600 ms; Motion off: at once): the base and the layer colors change, the cubes do not, the
readout gives the new layer and height, and the Ways list adds that way (three at most). **Empty** clears the crate.

**Cube Sizes** (explore). Focus: one box, the Giving box, 12 in long, 8 in wide, 8 in tall, center stage at the same
iso view (29 px per inch at 1366x768). Panel buttons: **1 inch cubes**, **2 inch blocks**, **4 inch blocks**, **Cans**,
and **Tea box** / **Giving box** to switch boxes (the Tea box shows only **1 cm cubes** and **2 cm blocks**). A size
tap empties the box and fills it layer by layer (0.25 s a layer). The results table in the panel fills one row per size
tried. Tap any block in a filled box: it lifts out and opens into its inch (or cm) cubes, 2 x 2 x 2 or 4 x 4 x 4, with
"1 block = 8 cubic inches" (or 64), then settles back on the next tap. Cans: 4 in across and 4 in tall, 12 of them in
3 by 2 by 2, the spaces between cans shaded in muted hatching with the readout (Content).

**Shelves** (explore). Focus: an L-shaped pantry shelf made of cube cells, center stage, iso view, edges labeled.
Two dashed cut lines sit on it, numbered 1 and 2. Panel: **Cut 1**, **Cut 2** (or tap a dashed line), **Join**,
**Fill both**, **Ruth's count**, **Next shelf**, the Ways list. A cut slides the two parts half a cube apart (400 ms),
colors them squash and sky, and labels each part's three edges. Fill both packs each part layer by layer, its label
"6 x 2 x 3 = 36" on it, then the total under the shelf. Ruth's count rejoins the shelf and draws both of Ruth's boxes
measured to the outer corner, the shared corner block in red with white hatching and the label "counted twice", and her
clipboard (painted) shows her sum in code. Join puts the shelf back whole.

**Puzzles** (the levels). Five levels of three puzzles (Content). Level tabs **Level 1** to **Level 5** across the top
of the panel, a dot per puzzle, all open (the order is a suggestion; the hint names the first unsolved one). The card
prompt sits on a painted chalkboard strip across the top of the stage; the crate, bin or shelf is center stage with
labeled or ticked edges. No count, layer tally, Ways list or readout is ever on screen in Puzzles. Answer boxes and
**Check** sit in the panel; Check is enabled once every box on the card has a whole number. Each puzzle gets two
Checks: a first miss rings the wrong boxes red, plays the reason (Content order) and keeps the typed values; a second
miss plays shown, Grace packs it layer by layer with the tally showing, fills the right answers, and the dot counts
"with Grace's help". Right: right plays, the crate fills by layers as proof (1.5 s; Motion off at once), then
**Next puzzle** appears. Counter: "Puzzles solved 5 of 15 (4 on your own)" and "Saved on this device only."
Leaving Puzzles (or switching puzzle) re-rolls an unsolved puzzle to a variant from its pool not yet shown this session.

What the picture shows for every outcome: empty crate: kraft floor and walls with the dashed grid; partial: cubes in
packing order, the empty spaces as the open dashed grid, the count of both; row done: bracket; layer done: label and
chip; full: green rim and check; turned: new layer stripes and labels; Cube Sizes: each size packed whole, the cans with
hatched gaps, an opened block; Shelves: one shape whole, cut 1, cut 2 (different parts), Ruth's red corner.

1366x768: header 52 px; stage left about 900 px, panel right about 440 px; the crate, tally strip, readout, steppers,
Add buttons, Fill it, Turn, Check and every answer box sit above the fold (panel rows 44 px). 680x425: stage and panel
stay side by side (panel 250 px); Grace hides; the tally strip becomes one line under the readout ("Layers: 12, 24,
36"); the three unit buttons fold into one **Unit** button that cycles; the Ways list and results table shrink to 12 px
type and show the last three rows; the largest crate (10 x 8 x 8) draws at 19 px a cube.

## Content
Pack crates (Next crate cycles): Bean crate 4 x 3 x 5 in (60); Spice box 5 x 4 x 2 cm (40); Soup crate 3 x 3 x 3 in
(27); Cereal crate 6 x 2 x 4 in (48); Pallet stack 4 x 3 x 2 ft (24); Juice crate 7 x 2 x 3 in (42). Next crate sets
the unit too; the unit buttons only rename the cubes. Scale chip: "1 cube = 1 inch on every edge = 1 cubic inch" (cm,
foot to match).

Pack readouts: partial "17 cubes packed. 43 spaces still empty."; full "Full, no gaps: 60 cubes. Each layer is 4 by 3 =
12, and 5 layers make 12 x 5 = 60. Volume: 60 cubic inches."; turned "Same 60 cubes, turned. Each layer is now 4 by 5 =
20, and 3 layers make 20 x 3 = 60."; guess "Your guess: 50. The crate holds 60." Ways list: "(4 x 3) x 5 = 60",
"(4 x 5) x 3 = 60", "(3 x 5) x 4 = 60". Size change: "New size. Height changes keep the full layers; length or width
changes start the crate empty."

Cube Sizes, Giving box 12 x 8 x 8 in: 1 inch cubes 12 by 8 = 96 a layer, 8 layers, 768; 2 inch blocks 6 by 4 = 24 a
layer, 4 layers, 96 blocks, "each block holds 8 inch cubes: 96 x 8 = 768 cubic inches"; 4 inch blocks 3 by 2 = 6 a layer,
2 layers, 12 blocks, "each holds 64: 12 x 64 = 768 cubic inches"; Cans "12 cans fit, with gaps between them. Cans can't
measure volume: a unit must pack with no gaps." Tea box 10 x 6 x 4 cm: 1 cm cubes 240; 2 cm blocks 5 by 3 = 15 a
layer, 2 layers, 30 blocks, "30 x 8 = 240 cubic centimeters". Table header: "Cube | How many | Volume".

Shelves (front width x height, a notch cut from the top right, depth; parts by cut; Ruth adds both arms to the corner):
- Shelf 1: 6 x 4, notch 4 x 2, depth 3 = 48. Cut 1 (across): 6x2x3 = 36 + 2x2x3 = 12. Cut 2 (down): 2x4x3 = 24 + 4x2x3 = 24. Ruth 36 + 24 = 60 (corner 12).
- Shelf 2 (steps): 5 x 3, notch 2 x 2, depth 4 = 44. Cut 1: 20 + 24. Cut 2: 36 + 8. Ruth 20 + 36 = 56 (corner 12).
- Shelf 3 (an L seen from above, height 2): 5 x 4, notch 3 x 2 = 28. Cut 1: 20 + 8. Cut 2: 16 + 12. Ruth 20 + 16 = 36 (corner 8).
- Shelf 4: 8 x 5, notch 5 x 3, depth 2 = 50. Cut 1: 32 + 18. Cut 2: 30 + 20. Ruth 32 + 30 = 62 (corner 12).
Ways list: "Cut 1: 36 + 12 = 48", "Cut 2: 24 + 24 = 48", "Ruth: 36 + 24 = 60. The corner is counted twice."

Puzzles (first variant shown first; the pool is every combination in the ranges, minus the listed exclusions; units in
brackets). Miss reasons are checked in the order listed; anything else is missOther.
- 1a How many fit? [in] A crate with one row along the length, one row along the width and a stack up the back corner packed; edges ticked, not labeled. Type the count. First 4 x 3 x 2 = 24. Pool l 3 to 5, w 2 to 3, h 2 to 4, minus 3x3x3 and 4x2x4 (16). Misses: l+w+h-2 missSeen, l+w+h missAdd, l x w missLayer, lw+lh+wh or twice it missOutside.
- 1b How many fit? [in] the same, bigger. First 6 x 4 x 3 = 72. Pool l 5 to 8, w 3 to 5, h 3 to 5 (35). Same misses.
- 1c How many more? [in] k full layers packed, edges ticked. First 5 x 3 x 4 with 1 layer: 45. Pool l 3 to 6, w 2 to 4, h 3 to 6, k with h-k at least 2 and k not h-k (96). Misses: lwh missAll, lwk missPacked, h-k missLayersLeft, lw missLayer.
- 2a, 2b, 2c Two ways [in]: a full crate with labeled edges. Tap a face to make it the base, type Base and Height; then a second, different face. First 4 x 3 x 5 (2a, bases 12, 15, 20), 3 x 5 x 6 (2b, 90), 4 x 5 x 6 (2c, 120). Pool: three different edges 2 to 7, volume 150 or less (108), split across the three cards by volume: 2a up to 60 (54 crates), 2b 61 to 100 (30), 2c over 100 (24). Misses: a base not that face's area missBase; a height equal to a base edge missHeight; the same face twice missSameFace (the second face button for the first face is marked "used" and does nothing, so this never fires by tap).
- 3a Bigger blocks [in] box with labeled edges, one 2 inch block in the corner. Type blocks and inch cubes. First 8 x 6 x 4: 24 blocks, 192 cubes. Pool L 4, 6, 8, 10; W 2, 4, 6; H 2, 4 (24). Misses: blocks equal to cubes missSame; blocks equal to cubes / 2 or / 4 missEvery; cubes wrong with blocks right missCubes.
- 3b Bigger blocks [cm] the same with 2 cm blocks. First 10 x 6 x 4: 30 blocks, 240 cubes. Same pool and misses.
- 3c Foot cubes [ft] a pallet stack with labeled feet, one 6 inch block (half a foot) in the corner. Type foot cubes and 6 inch blocks. First 4 x 3 x 2: 24 cubic feet, 192 blocks. Pool L 2 to 5, W 2 to 4, H 1 to 3 (36). Misses: blocks equal to 2x or 4x the feet missEvery; blocks equal to feet missSame.
- 4a Potato bin [ft] base edges labeled, height unlabeled; "It must hold 48 cubic feet." Type one layer's cubic feet and the height. First 4 x 3 -> 12 and 4. Pool l 2 to 6, w 2 to 5, h 2 to 8, minus l = w = 2 (136). Misses: layer typed as l + w missBase; height as V / l or V / w missHeight; layer right, height wrong missTimes.
- 4b Build a bin [ft] "Build a bin that holds exactly 24 cubic feet and is no more than 2 feet tall." Length, Width, Height steppers (1 to 10, 1 to 8, 1 to 8) redraw the bin with labeled edges. Variants (N, tallest): 24, 2; 30, 2; 36, 3; 40, 2; 48, 3; 60, 3. Misses: taller than allowed missTall; wrong volume missBin.
- 4c Square bin [ft] "Build a bin with a square base that holds exactly 72 cubic feet." Same steppers. Variants: 72, 64, 50, 48, 45, 36, 32, 27, 18. Misses: length not width missSquare; wrong volume missBin.
- 5a, 5b Two boxes [in] a shelf from the pool, edges labeled. Tap a dashed cut, type Part A, Part B and Total. Pool: front width 4 to 8, height 3 to 5, notch any size leaving both arms, depth 2 to 4, volume 200 or less, no wrong answer equal to the right one, minus Shelves 1 to 4 (632); 5a front-L, 5b steps. First 5a: 7 x 4, notch 4 x 2, depth 2 = 40 (Cut 1: 28 + 12; Cut 2: 24 + 16). First 5b: 6 x 3, notch 3 x 2, depth 3 = 36 (Cut 1: 18 + 18; Cut 2: 27 + 9). Misses: a part not from the chosen cut missParts; total not the sum missSum; total equal to Ruth's missRuth; total equal to the whole box missWhole.
- 5c Ruth's count [ft] a pantry shelf and Ruth's clipboard showing her sum. Type the real total. First 6 x 5, notch 4 x 3, depth 2 = 36 (Ruth 24 + 20 = 44). Same pool. Misses: Ruth's sum missRuth; the whole box missWhole.
Card prompts: "How many cubes fill this crate? Type it, then tap Check."; "How many more cubes will fill it?"; "Pick a face for the base. Type the base and the height. Then use a different face."; "How many big blocks fill it? How many small cubes?"; the bin texts above; "Cut it into two boxes. Type each part and the total."; "Ruth says the shelf holds 44 cubic feet. How much does it really hold?"

## Interactions in detail
- A size change mid-fill finishes the fill at once, then applies the size. Height down keeps whole layers that fit;
  height up keeps all cubes (no longer full: the rim loses its check and Turn disables). Length or width empties it.
- Add a cube on a full crate does nothing and plays fullHow once ("It's full. Tap Empty or change a size.").
- A tap during any animation (Fill it, Turn, a cut, a Cube Sizes fill, a puzzle proof) jumps it to its end state at
  once and applies the tap. A mode switch hushes speech and ends animations.
- Turn cycles three sides; the Ways list holds each way once. Next crate or Empty clears the Ways list.
- My guess takes whole numbers 0 to 999; it only adds the guess line to the full readout. No score.
- Cube Sizes: the results table keeps a row per size; switching boxes clears it. An opened block closes on any tap.
- Shelves: Fill both before a cut packs the whole shape and says "Cut it first to see two boxes." (no line).
- Puzzles: answer boxes take whole numbers 0 to 9999. In 2a to 2c a face tap turns the crate (600 ms) and the base
  stripes show; the face buttons **Top**, **Front**, **Side** in the panel do the same for keyboard use.
- Saved on this device (localStorage, try/catch): solved puzzles with or without help, the level. **Start over** in
  Puzzles clears progress after a confirm.

## Look
Back-room theme on its own `:root`: paper `#f5f2ec`, ink `#24212c` (14.14:1), muted `#5b5664` (6.35:1). Accent
`--brand #8a2a4e` beet (7.45:1 on paper, white on it 8.33:1): header rule, mode buttons, Check, Next puzzle, cut lines.
Cubes: squash `#f2b84b` and sky `#93c4e6`, alternating by layer, edges `#2e2a36` (7.82:1 and 7.52:1); the two fills are
near in lightness, so layers are told apart by hue, the dark edge between layers, the layer labels and tally numbers,
never color alone. Full rim green `#2e6b3f` (5.71:1 on paper, white on it 6.38:1). Kraft `#c49a6c` under the dashed
grid in ink (6.16:1). Overlap red `#b3261e` with white hatching and the "counted twice" label (red on paper 5.85:1).
Wrong-box ring red `#b3261e` plus the reason text. Different from egg-carton-factory (meadow green, pulp gray),
skate-park-angles violet `#5b2bb5`, estimation-station freight red `#9c3520`, which-way-is-down copper.

## Art
- backroom-bg: a food bank back room in cool morning light, gray concrete floor, metal shelves of canned goods with blank labels, a roll-up door, a long empty steel table in front; 16:9; no cutout; no people; Pack, Cube Sizes and Shelves backdrop, softened behind the stage.
- dock-bg: a food bank loading dock with a half-open roll-up door and a blank chalkboard strip on the wall above; 16:9; no cutout; no people; Puzzles backdrop (the chalkboard strip holds the card prompt in code).
- kraft-texture: corrugated brown kraft cardboard, full frame, flat even light; 1:1; no cutout; clipped to the crate floor and back walls and the bins.
- can: one soup can upright with a plain blank paper label, seen from slightly above; 1:1; cutout; the 12 Cans sprites in Cube Sizes (32 px and up, code ovals below).
- clipboard: a brown clipboard holding a blank white sheet; 3:4; cutout; Ruth's count (Shelves, bottom right of the stage) and Puzzle 5c (right of the shelf); sum in code.
- grace-portrait, grace-point, grace-thumbs, grace-think: Grace, a woman about 65, light brown skin, short silver curls, reading glasses on a beaded chain, a green volunteer apron over a cardigan; smiling head and shoulders, pointing to the side, thumbs up, hand on chin thinking; 3:4; cutouts; people: true. Panel portrait; point while she shows, thumbs on a right answer, think on a miss.
Drawn in code: crates, cubes, blocks, grids, labels, tally chips, cut lines, the shelf, bins, readouts. 9 images. Each
cutout shows whole where it appears; Grace hides at 680x425 rather than crop.

## Voice
Bank voice `knowing-guide` (Sadaltager): she is Grace. Style line: "Say in a knowledgeable, friendly way, like a food bank
volunteer who loves a good packing puzzle." (Swapped from curious-librarian at the spec check: tap-to-start-puppets in the same batch uses it.) Not used by any close neighbor (egg-carton-factory friendly-dad,
skate-park-angles big-sister, box-plot-builder news-reader; the others are unbuilt). The kit voice queue, scope = mode
plus puzzle id. No line carries a number (all recordable); readouts and cards are read on screen, and Read speaks the
hint plus the card. Welcomes and how lines are `how`: spoken once, then hint only.
- wPack (how, Pack welcome; stale once a crate is full): "I'm Grace. Every crate we pack must be full, with no gaps. Tap the crate to drop in a cube, or tap Add a layer."
- rowHow (how, first finished row; stale once a layer is done): "That's one row. Tap Add a row to finish rows faster."
- layerHow (how, first finished layer; stale when full): "One full layer. Every layer holds the same number of cubes, so now count the layers."
- full (event, every time a crate becomes full; whole): "Full, with no gaps. One layer's cubes, times the number of layers."
- turnHow (how, after the first full; needs Turn the crate enabled): "Now tap Turn the crate. Same cubes, a different bottom."
- turned (event, every turn): "A new base and new layers, but the same number of cubes."
- fullHow (how, Add a cube on a full crate): "It's full. Tap Empty, or change a size."
- wSizes (how, Cube Sizes welcome): "Same box, different cubes. Tap a cube size and see how many fit."
- sizesHow (how, after the second size; stale on box switch): "Bigger cubes, fewer of them. So always say which cube you counted."
- blockHow (how, first 2 or 4 inch fill): "Tap a block to open it and see the small cubes inside."
- cans (event, every Cans fill; whole): "See the gaps between the cans? A unit for volume has to pack with no gaps."
- wShelves (how, Shelves welcome): "This shelf isn't one box. Tap a dashed line to cut it into two boxes."
- cutHow (how, first cut; needs Fill both): "Two boxes now. Tap Fill both, then add the two parts."
- otherCut (how, after the first cut's fill; stale once both cuts are seen): "Now try the other cut. Does the total change?"
- same (event, when a second cut's total matches; whole): "A different cut, the same total. The cubes didn't change."
- ruth (event, every Ruth's count; whole): "Ruth measured both boxes out to the corner, so the corner got counted twice."
- wPuzzles (how, Puzzles welcome): "Each level gets a little harder. Read the card on the board, then work it out."
- countHow (how, first level 1 card): "Type how many cubes, then tap Check."
- twoHow (how, first level 2 card): "Tap a face to make it the base. Type the base and the height, then do it again with another face."
- unitHow (how, first level 3 card): "Type how many big ones and how many small ones fit, then tap Check."
- binTypeHow (how, first 4a card): "Type one layer's cubic feet and the height, then tap Check."
- binHow (how, first 4b or 4c card): "Set the sides with the arrows, then tap Check."
- shelfHow (how, first level 5 card): "Tap a dashed line to cut. Type each part and the total, then tap Check."
- right (event, whole): "That's it. Packed right." | levelDone (event, whole, after right on a level's last puzzle): "That level's done. Pick the next one when you're ready."
- shown (event, whole): "Here's how I'd pack it. Watch the layers."
- Miss reasons (event, whole, once per Check): missSeen "You counted the cubes you can see. More hide behind and below. Count one layer, then the layers." missAdd "Adding the sides isn't packing. Try one layer's cubes, times the layers." missLayer "That's one layer. How many layers fill it?" missOutside "That counts squares on the outside. Volume counts the cubes inside." missAll "That's the whole crate, but some layers are already packed." missPacked "That's what's packed already. How much room is left?" missLayersLeft "That's how many layers are left. How many cubes go in each one?" missBase "Check the base. It's rows times cubes in a row, on the face you picked." missHeight "The height is the edge that isn't part of the base." missTimes "Your layer is right. Check the height." missSame "Big blocks can't fit as many as small cubes." missEvery "A block is bigger every way: longer, wider and taller." missCubes "The blocks are right. Now count the small cubes." missBin "That bin doesn't hold the right amount. Multiply its three sides." missTall "That bin is too tall for this shelf." missSquare "A square base has the same length and width." missParts "One part doesn't match your cut. Count each box on its own." missSum "The parts are right. Check the total." missRuth "That's Ruth's count. The corner got counted twice." missWhole "That counts the empty corner too. Count only the shelf." missOther "Not quite. Check each number again."
No line names a disabled control: turnHow needs Turn enabled; cutHow needs Fill both; the Check line in countHow,
unitHow, binTypeHow, binHow and shelfHow is the last step, and the hint reads "Type ... then tap Check" while Check waits.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| 1a, 1b How many fit? | count the cubes you see; add the edges; one layer; count outside squares; guess; open Pack, set the same size, read the count; read a counter | each common wrong answer is its own miss (checked: none equals the right count anywhere in the pools, after the two exclusions); a typed count has no options to eliminate; no counter or tally shows in Puzzles; leaving Puzzles re-rolls to an unseen crate from 16 or 35, so a Pack answer never matches the card on return |
| 1c How many more? | type the whole crate; type what's packed; type layers left; one layer | missAll, missPacked, missLayersLeft, missLayer, none equal to the right answer in the 96-crate pool (checked) |
| 2a to 2c Two ways | the same face twice; type the volume as base and 1 as height; the height as a base edge; copy the Pack Ways list | the used face is marked and won't take a second tap; a base must equal the area of the face tapped and the height the third edge (faces of three different edges always have different areas, checked); Pack's list is for Pack's crate, and leaving re-rolls from 108 |
| 3a to 3c Bigger blocks | type the same count twice; halve the cubes; double the feet | missSame, missEvery; blocks = cubes / 8 never equals cubes / 2 or / 4 (checked); both boxes must be right |
| 4a Potato bin | add the base edges; divide by one edge; guess the height (1 in 8) | the layer box is a typed product with no options (missBase); a guessed height still needs the layer right in the same Check; V / l is caught as missHeight |
| 4b Build a bin | try steppers at random; the tallest bin allowed only; a bin that holds it but is too tall | 5 to 9 right bins in 640 settings, so two random tries pass under 3 in 100 (checked); missTall; there is no count on screen to watch while turning steppers |
| 4c Square bin | random steppers; any bin with the volume | 1 or 2 right bins in 640, under 1 in 100 for two tries; missSquare when length and width differ |
| 5a, 5b Two boxes | Ruth's way; the whole outer box; one part only; parts from the other cut | missRuth, missWhole, missParts; in the pool no wrong answer equals the right total (checked, 632 shelves); Shelves mode uses four other shelves only |
| 5c Ruth's count | type Ruth's number; the whole box | missRuth, missWhole |
| Puzzle counter "on your own" | let Grace show every puzzle; redo a solved one | shown puzzles count "with Grace's help"; each counts once |
| Pack, Cube Sizes, Shelves | none (explore, no checks) | nothing in them is scored |
Doing nothing: Check stays disabled until every box has a number. Mashing Check: each miss costs one of two tries.

## Heard in order
Grade 5: not every action speaks, but a result lands before the next step and a puzzle's feedback before the next puzzle.
1. Load, first tap on the crate: a cube drops (chime), then wPack (may be cut). Hint: "Tap the crate to drop in a cube, or tap Add a layer. Pack it full with no gaps."
2. First finished row: rowHow. First finished layer: layerHow (drops rowHow if it never started). Full: chime, then full (whole), then turnHow; a tap during full plays after it.
3. Turn: the turn animation, then turned. Cube Sizes: wSizes on entry; after a fill ends, blockHow (first block size), sizesHow (second size), cans (whole) after the Cans fill.
4. Shelves: wShelves; a cut, then cutHow; after Fill both ends, otherCut; the second cut's fill ends, then same (whole). Ruth's count: the red corner draws, then ruth (whole).
5. Puzzles: wPuzzles, then the card's how line. Check right: right (whole) plays while the proof fill runs; Next puzzle appears when both end. Level end: right, then levelDone. Miss: the reason (whole) before the boxes can be edited again; second miss: shown (whole), then Grace's fill.
No line contains a number or a bare letter; numbers are on screen and spoken by Read.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| A unit cube (edge 1) has one cubic unit of volume; a solid packed with n unit cubes, no gaps or overlaps, has volume n cubic units (5.MD.3) | CCSS Math 5.MD.C.3 (corestandards.org) | Illustrative Mathematics grade 5 unit 1 "Finding Volume" | yes |
| Volume is measured by counting cubic cm, in, ft and improvised units (5.MD.4) | CCSS Math 5.MD.C.4 | Illustrative Mathematics grade 5 unit 1 | yes |
| V = l x w x h = B x h for rectangular prisms (5.MD.5a, b) | CCSS Math 5.MD.C.5 | Math is Fun, "Cuboids, Rectangular Prisms and Cubes" | yes |
| (a x b) x c = a x (b x c): grouping does not change a product | Wikipedia, "Associative property" | Math is Fun, "Commutative, Associative and Distributive Laws" | yes |
| Volume adds for non-overlapping parts (5.MD.5c) | CCSS Math 5.MD.C.5c | Illustrative Mathematics grade 5 unit 1 (volume of figures made of two prisms) | yes |
| A cube with edge 2 holds 8 unit cubes, edge 4 holds 64 (edge cubed) | Wikipedia, "Cube" (volume a cubed) | Math is Fun, "Volume of a Cube" | yes |
| Equal circles in a square grid leave gaps (cover pi/4, about 79 percent) | Wikipedia, "Circle packing" (square packing density) | Wolfram MathWorld, "Circle Packing" | yes |
| 1 foot = 12 inches, so 6 inches is half a foot | NIST Handbook 44, Appendix C | Wikipedia, "Foot (unit)" | yes |
Cut: real crate, bin and pallet sizes (all crates are made up and labeled so); a "standard pallet" size was not used.
Number checks (Python, run 2026-11-07): every Pack crate's volume and layers; Cube Sizes counts (768, 96, 12, cans 12;
240, 30) and 96 x 8 = 12 x 64 = 768, 30 x 8 = 240; every puzzle pool against its wrong answers (1a: 3x3x3 and 4x2x4
excluded, 4x2x4's outside squares equal its 32; 1b 35 crates, no collision; 1c restricted to 96 crates after 72 collisions
in 168; 4a minus l = w = 2, where l + w = l x w; 5 pool 632 with no wrong total equal to the right one and Ruth never
equal to the whole box); the five Shelves sums and Ruth's corners; 4b solution counts (24: 8, 30: 5, 36: 9, 40: 6, 48: 9,
60: 7 of 640) and 4c (1 or 2 of 640); face areas distinct when edges differ; cube sizes (Bean crate 61 px, 10 x 8 x 8
31 px at 1366x768 and 19 px at 680x425, Giving box 29 px); contrast ratios in Look.

## Done when
1. Focus: in every mode the crate, box, shelf or bin is the biggest central thing, and at 1366x768 every control the mode needs (steppers, Add buttons, Fill it, Turn, cut buttons, answer boxes, Check) is above the fold; at 680x425 stage and panel stay side by side.
2. On load the empty Bean crate shows; tapping it drops a cube in the back left corner and reads "1 cube packed. 59 spaces still empty."
3. Add a layer on the Bean crate labels "4 by 3 = 12" and adds a tally chip; Fill it ends with "Full, no gaps: 60 cubes ... 60 cubic inches" and plays full.
4. Turn the crate twice lists three ways, each 60, and the cubes never change count.
5. A tap while anything plays acts at once: Add a cube mid Fill it, a size tap mid Cube Sizes fill, a cut tap mid Fill both, Next puzzle mid proof fill.
6. Cube Sizes: 1 inch, 2 inch, 4 inch give 768, 96, 12; a 2 inch block opens into 8 cubes; Cans show 12 cans with hatched gaps and play cans.
7. Shelves 1: Cut 1 totals 36 + 12 = 48, Cut 2 totals 24 + 24 = 48 and plays same; Ruth's count shows the red corner and 60.
8. Puzzle 1a (4 x 3 x 2): 24 passes; 7 plays missSeen; 9 missAdd; 12 missLayer; 26 missOutside; a second miss shows Grace's fill and counts "with Grace's help".
9. Puzzle 2a passes only with two different faces, each base and height right; Puzzle 3a passes only with 24 and 192 (96 blocks plays missEvery).
10. Puzzle 4b passes with 4 x 3 x 2; 4 x 3 x 3 plays missTall; 5 x 5 x 1 plays missBin. Puzzle 5c rejects 44 with missRuth.
11. No count, tally or Ways list ever shows in Puzzles; leaving Puzzles with a puzzle open re-rolls it to a variant not seen this session.
12. Voice: each how line speaks once in five repeats; full, turned, right and miss lines speak every time and finish before the next puzzle; no line names a disabled control.

## Open questions
none
