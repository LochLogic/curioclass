# Packaging Challenge

## One idea
Take an order ("hold 355 mL") and drag a can's radius or a box's side: the volume stays locked to the order while
the material changes, every try drops a dot on a graph of material against shape, and the dots find the
least-material package by hand; then real cans go on the same graph, and the class sees which ones are almost
perfect and which are far off on purpose.

## Not like
- optimization-workshop (gr 12 builder): the cheapest can found with a derivative. Here no calculus: you find the best shape by building and watching the graph, then compare with real products.
- slice-it, now Slice and Stack (gr 10, this group): why the volume formulas are true. Here the formulas are tools for a design with a fixed volume.
- ramp-and-roof (gr 10, this group): designs pass or fail code rules. Here every design works; the question is how much material it costs.
- model-my-world (gr 9 builder): an equation must reproduce a data record. Here the model is a shape, and the record is a shelf of real cans.

## Who and how
- Grade 10, Geometry, module Modeling with Geometry. Students drive, own laptops or pairs. 15 to 40 minutes.
- Topic line: "surface area, volume and design".
- Standards (module): G-MG.A (use shapes to describe objects; density by area and volume; design problems that meet
  constraints or minimize cost).
- CCSS clusters: Shelf serves G-MG.A.1 (cans modeled as cylinders); Orders serves G-MG.A.3; Case and the metal-per-area
  line serve G-MG.A.2.
- tool.json: driver "students", minutes "15-40", modes ["Orders", "Shelf", "Case"], grades_label "Grade 10".

## Screens and modes
Header (kit, 9-12 theme): title "Packaging Challenge", subtitle "Same volume. Less material." Modes `Orders` (opens
first), `Shelf`, `Case`. Kit buttons `Motion`, `Sound`, `Read`.
Layout: stage left on the painted workbench (art: pc-workbench), panel right: order card (with the order's picture,
art: pc-order-*), controls, readouts. Under 1000 px wide the panel goes under the stage with the controls first.
Under 900 px tall the net hides behind a `Net` toggle so the package, the graph and the slider stay in view.

### Orders (builder)
- Focus: the package and its graph, side by side across the middle of the stage at equal height, the two largest
  things on screen: the package at left (front view to true scale, drawn in code because it bends with every drag),
  the graph of material against radius or side at right. The net (the flat pieces the package is cut from) is a
  strip under the package.
- Order picker `O1` to `O6` (Content). Package type follows the order: a closed can, a closed box with a square
  base, or an open tray with a square base.
- Control: `Radius` (cans, 1.00 to 12.00 cm) or `Base side` (boxes, 2.00 to 30.00 cm); drag the handle on the
  package's edge or use the slider and number box. The height follows so the volume stays the order's volume:
  h = V ÷ (πr²) or h = V ÷ s². The package and its net redraw as you drag.
- Readouts: radius or side, height, volume (always the order's, with a lock glyph), each piece's area (top, bottom,
  side wall), total material in cm², and "Metal: 0.03 g per cm² (a practice number), so this can uses 8.33 g."
  (the grams are material × 0.03, two decimals; 8.33 g is the best O2 can).
- The graph: releasing the handle drops a dot at (radius, material). After five dots, or `Show curve`, the whole
  curve appears. `Reveal best` marks the lowest point with its numbers and the line "Best: height = 2 × radius (as
  wide as it is tall)" for closed cans, "a cube" for closed boxes, "height = half the side" for trays. `Clear dots`.
- `Lid cost` (O6 only, 1× to 4×, step 0.5): lids and bottoms cost that many times the wall per cm². The material
  readout becomes "cost in wall-cm²" and the best shape moves: height = 2 × (lid cost) × radius.
### Shelf
- Focus: the shelf of four real cans (art: pc-shelf with the can cutouts pc-can-*) across the top two thirds of the
  stage, and under it the graph where a tapped can lands.
- The four cans stand to scale from their published outside sizes (Content), each with a tag in code over its blank
  label. Tap one: it lifts a little and goes on the graph of its own volume, beside the best can for that volume,
  with the readout "Uses 4.1% more metal than the best can of the same size" and its height ÷ diameter beside the
  best (1.00).
- A discussion card under the shelf (no right answers given): "Why might a drink can be tall and thin? Think of
  hands, cup holders, machines that sell them, and the lid."
### Case (density)
- Focus: the case seen from above, center stage and large: the kraft case floor (art: pc-kraft) with 24 can tops
  (art: pc-can-top) or 24 code-drawn boxes in a 4 by 6 grid, the empty corners between cans shaded with a hatch.
- Order picker `O1` to `O6` again (same as Orders; it uses each order's current shape). `Pack the case` drops the
  24 packages in row by row (1.5 s, instant with Motion off); a second tap or an order change during the drop
  finishes it at once.
- Readouts: case inside volume, product volume, fill = product ÷ case. Cans fill π ÷ 4 = 78.5% of their case
  whatever their size; square boxes fill 100%.
- A second line for density by area: metal grams per case (24 × material × 0.03 g per cm², the practice number).

## Content
Order pictures (art) and package type: O1 soup bowl, O2 and O6 cold drink, O3 crate of tomatoes, O4 gift box, O5
seedlings.
Orders (best shapes recomputed; areas in cm², volume 1 mL = 1 cm³):
- O1 Soup can, 500 mL, closed can. Best r 4.30, h 8.60, material 348.73. (Shelf twin: No. 303 can.)
- O2 Drink can, 355 mL, closed can. Best r 3.84, h 7.67, material 277.55. Sample tries: r 2.5 → h 18.08, 323.27;
  r 3.0 → h 12.56, 293.22; r 4.5 → h 5.58, 285.01; r 5.0 → h 4.52, 299.08.
- O3 Bulk can, 3236 mL, closed can. Best r 8.02, h 16.03, material 1211.12. (Shelf twin: No. 10 can.)
- O4 Gift box, 1000 mL, closed, square base. Best: cube, side 10, material 600. A 10 by 10 by 10 beats any other
  square-base box; for comparison a 20 by 10 by 5 box (shown as a ghost) uses 700.
- O5 Seed tray, 500 mL, open top, square base. Best side 10, height 5, material 300.
- O6 Drink can again, 355 mL, with `Lid cost` 3×. Best r 2.66, h 15.96 (h = 6r), cost 400.29 wall-cm². At 1× it is
  O2's answer.
Shelf (outside sizes as published; model = a plain cylinder of that size):
- Drink can, 12 US fl oz (355 mL): 6.60 cm diameter, 12.3 cm tall. Model volume 420.8, material 323.5, best for
  420.8 is 310.9, 4.1% more; height ÷ diameter 1.86.
- No. 303 food can: 3 3/16 by 4 3/8 in (8.10 by 11.11 cm), holds 16.88 fl oz (499 mL). Model volume 572.1, material
  385.6, best 381.5, 1.1% more; 1.37.
- No. 2½ food can: 4 1/16 by 4 11/16 in (10.32 by 11.91 cm), holds 29.79 fl oz (881 mL). Model 995.7, material
  553.2, best 552.0, 0.2% more; 1.15.
- No. 10 food can: 6 3/16 by 7 in (15.72 by 17.78 cm), holds 109.43 fl oz (3,236 mL). Model 3449.2, material
  1265.9, best 1263.7, 0.2% more; 1.13.
Shelf note on screen: "Outside sizes are bigger than what the label says the can holds. Can sizes as listed
2026-10-27."

## Interactions in detail
- Formulas: closed can material 2πr² + 2πrh; closed square box 2s² + 4sh; open tray s² + 4sh; with lid cost k,
  cost = k × 2πr² + 2πrh. Best shapes from the exact formulas (r = (V ÷ 2πk)^(1/3), cube side V^(1/3), tray side
  (2V)^(1/3)); the tool never searches numerically.
- Display: lengths to 2 decimals, areas to 2 decimals in Orders and 1 decimal on the Shelf, percent to 1 decimal.
  "More than best" = (material ÷ best material − 1) × 100.
- Extremes: at r = 1.00 the can is 113.00 cm tall for O2 (159.15 for O1, 1030.05 for O3) and the stage zooms out;
  at r = 12.00 it is a flat disk (0.78 cm tall for O2). Boxes: side 2 gives a 250 cm tower for O4, side 30 a sheet
  1.11 cm thick. The graph's y axis grows to fit; a dot outside view pins to the edge with an arrow.
- Shelf cans use their own volumes, never the order's; the tag says so. Each can cutout is cropped to its content
  and scaled to its true outside height and width (a small stretch from the painted aspect is fine).
- Case: fill for cans is exactly π ÷ 4 in a square grid; the readout shows 78.5% and "same for any size". The case
  inside is (8r by 12r by h) for cans and (4s by 6s by h) for boxes.
- Live while anything moves: dragging the handle, a slider, the order picker and every mode tab act at once during
  a dot drop, the curve reveal or the case drop; the running animation finishes instantly.
- Keyboard: the handle is focusable, arrows change the radius by 0.01 cm (Shift 0.10); aria-valuetext "radius 3.84
  centimeters, height 7.67, metal 277.55 square centimeters".
- Reset: `Clear dots` per order; orders keep their last shape for the page session; nothing is saved.
- `window.__tool = {state, setMode, order(id), set(value), best(), shelf(id), lidCost(k), pack()}`.

## Look
Accent `--brand #c08a2a` (kraft cardboard), `--brand-ink #10161f`. The stage sits on the painted workbench
(pc-workbench), dimmed under the graph; code cans are brushed metal `#c9d1da` with dark outlines; box packages and
their nets are clipped fills of the kraft texture; net pieces outlined in the accent with dashed fold lines; graph
plane from the 9-12 theme (`--gr-bg`), the curve in the accent, dots `#e8edf3`, best point a ring plus label.
Contrast (computed): brand on --panel 5.70:1, on --sec-bg 5.40:1, on the bench (dimmed to `#2a2118`) 5.20:1;
brand-ink on brand 5.97:1; ink on the bench 13.42:1. Browner and darker than the grade 11 golds (#f2a93b, #f0b650)
and solid-spinner's clay.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. 13 images. One style: warm, clean painted illustration under
soft workshop light.
- pc-workbench: a wide wooden workbench top seen from the front at table height, worn maple boards, a pegboard wall
  behind with neatly hung rulers and calipers, soft warm workshop light, painted illustration; 16:9; cutout no;
  people no; full-frame stage background in Orders (dimmed to `#2a2118` average under the graph).
- pc-kraft: a flat sheet of plain brown corrugated kraft cardboard, seen straight on, soft even light, blank smooth
  surface; 1:1; cutout no; people no; tiled texture clipped to box packages, their nets and the case floor.
- pc-shelf: a long wooden pantry shelf seen straight on at eye level, a plain painted wall behind, soft daylight from
  the left, an empty shelf board across the middle, painted illustration; 16:9; cutout no; people no; Shelf background,
  the cans stand on the board.
- pc-can-drink, pc-can-303, pc-can-2half, pc-can-10 (kit of four, one shared prompt): a single plain {tall slim
  aluminum drink can with a pull tab lid | short steel food can with ribbed sides | medium steel food can with
  ribbed sides | large steel food can with ribbed sides}, brushed silver metal with a plain blank paper band around
  the middle, front view at eye level, soft daylight from the left, painted illustration, plain white background;
  9:16, 3:4, 1:1, 1:1; cutout yes; people no; Shelf. Sizing rule: crop to content, scale so the can's height and
  width are its published outside size (Content) on the shelf's shared cm scale; the tag text is code over the
  blank band.
- pc-can-top: the round top of a plain steel food can seen straight down, a smooth blank lid with two raised rings
  near the rim, soft even light, plain white background; 1:1; cutout yes; people no; Case, one per can, scaled to
  the can's diameter.
- pc-order-soup, pc-order-drink, pc-order-tomatoes, pc-order-gift, pc-order-seedlings (kit of five, one shared
  prompt): {a white bowl of steaming tomato soup | a tall glass of fizzy lemon soda with ice | a wooden crate heaped
  with ripe tomatoes | a square gift box wrapped in plain teal paper with a gold ribbon | a shallow tray of green
  seedlings sprouting from dark soil}, three quarter view, soft daylight, painted illustration, plain white
  background; 1:1; cutout yes; people no; the order card picture (O6 uses pc-order-drink), about 96 px.
Drawn in code: the package being designed (it bends with every drag), its net, the graph, the case grid lines and
hatch, every label and tag, preview.svg.

## Voice
Bank voice `hero-coach` (Puck), style "bright and encouraging, like a coach on the design team" (one line per
event, nothing more). Not used by its math 9-12 neighbors or the other specs in this batch. `Curio.voice`,
`scope: () => state.mode`. Readouts and the discussion card are read on screen; Read speaks the hint.
- wOrders (how, Orders welcome; stale on the first release): "Here's an order. Drag the handle on the package's edge, or the slider. The volume stays locked, so watch the material."
- wShelf (how, Shelf welcome; stale when a can is tapped): "Tap a real can to put it on the graph next to the best can of its size."
- wCase (how, Case welcome; stale on Pack the case): "Pick an order, then tap Pack the case. Compare how much space cans and boxes leave empty."
- curve (how, the curve first appears; stale on order change): "Your dots made a curve. Its lowest point is the best package. Tap Reveal best to check."
- best (event, a release lands within 0.5% of the best; stale on the next release or order change): "That's within half a percent of the best. Great build."
- lidShift (event, Lid cost changed in O6; stale on the next change): "Pricier lids push the best can taller and thinner."

## Family engine
none. The graph uses the kit's coordinate plane (`kit/graphing.js`, `Plane`, `g.fn`, `g.point`) as a plain helper.

## Sources
- G-MG.A text: Common Core State Standards for Mathematics, High School Geometry, Modeling with Geometry, https://www.thecorestandards.org/Math/Content/HSG/MG/
- Drink can, 12.3 cm tall and 6.60 cm at the widest point of the body: Wikipedia, "Beverage can", read 2026-10-27, https://en.wikipedia.org/wiki/Beverage_can
- Food can sizes and capacities (No. 303, No. 2½, No. 10), with the Can Manufacturers Institute's size naming: Wikipedia, "Tin can", Standard sizes table, read 2026-10-27, https://en.wikipedia.org/wiki/Tin_can
- 1 US fluid ounce = 29.5735 mL: NIST Handbook 44, Appendix C, https://www.nist.gov/pml/owm/nist-handbook-44-current-edition
- Surface area and volume of cylinders and prisms: OpenStax, Prealgebra 2e, 9.6 "Solve Geometry Applications: Volume and Surface Area", https://openstax.org/books/prealgebra-2e/pages/9-6-solve-geometry-applications-volume-and-surface-area
- The 0.03 g per cm² metal figure is a practice number, labeled so on screen.
- Checks run (Python, 2026-10-29): best cans O1 r 4.3013, h 8.6025, 348.7342; O2 3.8372, 7.6744, 277.5450; O3 8.0157,
  16.0315, 1211.1192 (the draft's 1211.2 now reads 1211.12). O2 sample tries reproduce to two decimals; on a 0.01
  grid the lowest O2 point is r 3.84, 277.545. Cube 600 and ghost 700; tray side 10, height 5, 300. Lid cost: best
  h ÷ r = 2k at every k from 1 to 4 (3×: r 2.66, h 15.96, 400.29). Shelf: drink 4.05% (shown 4.1%), No. 303 1.08%,
  No. 2½ 0.22%, No. 10 0.17%; ratios 1.86, 1.37, 1.15, 1.13; fl oz to mL 499.2, 881.0, 3236.2, 354.9. Extremes: the
  draft said 159 cm at r = 1 for O2; that is O1, O2 is 113.00 cm (fixed). Case fill π ÷ 4 = 0.7854 checked on O2's
  best case (8520 of 10848 cm³). The "within 0.5%" event band on O2 is r 3.58 to 4.11. The draft's "this can uses
  9.7 g" matched no order; the readout now computes grams from the shown material (8.33 g at O2's best).
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. O2 at r = 3.00 shows h 12.56 and 293.22; at r = 3.84 the readout is within 0.01 of 277.55 and Reveal best shows h = 2r.
2. O4 at side 10 shows 600; the 20 by 10 by 5 ghost shows 700. O5 best is side 10, height 5, 300.
3. O6 at 3× gives r 2.66, h 15.96, cost 400.29; at 1× it matches O2.
4. Shelf: the drink can shows 4.1% more and 1.86; No. 10 shows 0.2% and 1.13; each can cutout stands at its true height and width on the shared scale.
5. Case: Pack the case on any can order shows 78.5% fill; a box order shows 100%.
6. At r = 1.00 and r = 12.00 (O2 and O3) the stage and graph stay readable and nothing overflows.
7. Focus: at 1366x768 and 1000x625 the package and the graph are the two largest things on the Orders stage, the shelf on Shelf, the case on Case.
8. Tap while it plays: during the case drop or a dot drop, the order picker, a slider and the mode tabs act at once.
9. No voice line names a control that is hidden or disabled when it plays (Lid cost only on O6).
10. Keyboard alone can finish O2; every size in STANDARDS.md keeps the package, the graph and the slider visible without page scrolling.
11. Console clean, no network, no em dashes, "Curio Class" only in full.

## Open questions
- The Shelf uses real can sizes but no brands. Good, or add a cereal-style box (sizes vary by brand, so it would be
  an invented one)?
