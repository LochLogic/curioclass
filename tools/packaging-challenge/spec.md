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
Layout: stage left: the package on a workbench (a front view to scale with its net, the flat pieces it is cut from,
beside it), and under it the graph (material against radius or side). Panel right: order card, controls, readouts.
Under 1000 px wide the panel goes under the stage with the controls first. Under 900 px tall the net hides behind
a `Net` toggle so the package, the graph and the slider stay in view.

### Orders (builder)
- Order picker `O1` to `O6` (Content). Package type follows the order: a closed can, a closed box with a square
  base, or an open tray with a square base.
- Control: `Radius` (cans, 1.00 to 12.00 cm) or `Base side` (boxes, 2.00 to 30.00 cm); drag the handle on the
  package's edge or use the slider and number box. The height follows so the volume stays the order's volume:
  h = V ÷ (πr²) or h = V ÷ s². The package and its net redraw as you drag.
- Readouts: radius or side, height, volume (always the order's, with a lock glyph), each piece's area (top, bottom,
  side wall), total material in cm², and "Metal: 0.03 g per cm² (a practice number), so this can uses 9.7 g."
- The graph: releasing the handle drops a dot at (radius, material). After five dots, or `Show curve`, the whole
  curve appears. `Reveal best` marks the lowest point with its numbers and the line "Best: height = 2 × radius (as
  wide as it is tall)" for closed cans, "a cube" for closed boxes, "height = half the side" for trays.
- `Lid cost` (O6 only, 1× to 4×): lids and bottoms cost that many times the wall per cm². The material readout
  becomes "cost in wall-cm²" and the best shape moves: height = 2 × (lid cost) × radius.
### Shelf
- Four real cans stand on a shelf, drawn to scale from their published outside sizes (Content), each with a tag.
  Tap one: it goes on the graph of its own volume, beside the best can for that volume, with the readout "Uses 4.1%
  more metal than the best can of the same size" and its height ÷ diameter beside the best (1.00).
- A discussion card under the shelf (no right answers given): "Why might a drink can be tall and thin? Think of
  hands, cup holders, machines that sell them, and the lid."
### Case (density)
- Pack 24 of the current order's cans in a 4 by 6 case, or 24 boxes. Readouts: case inside volume, product volume,
  fill = product ÷ case. Cans fill π ÷ 4 = 78.5% of their case whatever their size; square boxes fill 100%.
- A second line for density by area: metal grams per case, using the 0.03 g per cm² practice number.

## Content
Orders (best shapes recomputed; areas in cm², volume 1 mL = 1 cm³):
- O1 Soup can, 500 mL, closed can. Best r 4.30, h 8.60, material 348.73. (Shelf twin: No. 303 can.)
- O2 Drink can, 355 mL, closed can. Best r 3.84, h 7.67, material 277.55. Sample tries: r 2.5 → h 18.08, 323.27;
  r 3.0 → h 12.56, 293.22; r 4.5 → h 5.58, 285.01; r 5.0 → h 4.52, 299.08.
- O3 Bulk can, 3236 mL, closed can. Best r 8.02, h 16.03, material 1211.2. (Shelf twin: No. 10 can.)
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
- Extremes: at r = 1.00 the can is 159 cm tall for O2 and the stage zooms out; at r = 12.00 it is a flat disk
  (0.78 cm tall). The graph's y axis grows to fit; a dot outside view pins to the edge with an arrow.
- Shelf cans use their own volumes, never the order's; the tag says so.
- Case: fill for cans is exactly π ÷ 4 in a square grid; the readout shows 78.5% and "same for any size".
- Keyboard: the handle is focusable, arrows change the radius by 0.01 cm (Shift 0.10); aria-valuetext "radius 3.84
  centimeters, height 7.67, metal 277.55 square centimeters".
- Reset: `Clear dots` per order; orders keep their last shape for the page session; nothing is saved.
- `window.__tool = {state, setMode, order(id), set(value), best(), shelf(id), lidCost(k)}`.

## Look
Accent `--brand #c08a2a` (kraft cardboard), `--brand-ink #10161f`. Workbench `#2a2118` with a kraft texture on box
packages; cans brushed metal `#c9d1da` with dark outlines; net pieces outlined in the accent with dashed fold lines;
graph plane from the 9-12 theme (`--gr-bg`), the curve in the accent, dots `#e8edf3`, best point a ring plus label.
Contrast (computed): brand on --panel 5.70:1, on --sec-bg 5.40:1, on the bench 5.20:1; brand-ink on brand 5.97:1;
ink on the bench 13.42:1. Browner and darker than the grade 11 golds (#f2a93b, #f0b650) and solid-spinner's clay.

## Art
- pc-kraft: "a flat sheet of plain brown corrugated kraft cardboard, seen straight on, soft even light, blank
  surface"; 1:1; cutout no; people no; FLUX (cfart). Tiled as a texture clipped to the box packages and their nets.

## Voice
Bank voice `hero-coach` (Puck), style "bright and encouraging, like a coach on the design team" (one line per
event, nothing more). No 9-12 math tool uses it. `Curio.voice`, `scope: () => state.mode`.
- wOrders (how): "Here's an order. Drag the radius and watch the metal change. The volume stays locked."
- wShelf (how): "Tap a real can to put it on the graph next to the best can of its size."
- wCase (how): "Pack twenty four into a case. Compare how much space cans and boxes waste."
- curve (how, the curve first appears): "Your dots made a curve. Its lowest point is the best package."
- best (event, a release lands within 0.5% of the best; stale on order change): "That's within half a percent of the best. Great build."
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
- Every order and shelf number above was recomputed in Python (2026-10-27).

## Done when
1. O2 at r = 3.00 shows h 12.56 and 293.22; at r = 3.84 the readout is within 0.01 of 277.55 and Reveal best shows h = 2r.
2. O4 at side 10 shows 600; the 20 by 10 by 5 ghost shows 700.
3. O5 best is side 10, height 5, 300.
4. O6 at 3× gives r 2.66, h 15.96, cost 400.29; at 1× it matches O2.
5. Shelf: the drink can shows 4.1% more and 1.86; No. 10 shows 0.2% and 1.13.
6. Case: any can order shows 78.5% fill; a box order shows 100%.
7. At r = 1.00 and r = 12.00 the stage and graph stay readable and nothing overflows.
8. Keyboard alone can finish O2; every size in STANDARDS.md keeps the package, the graph and the slider visible without page scrolling.
9. Console clean, no network, no em dashes, "Curio Class" only in full.

## Open questions
- The Shelf uses real can sizes but no brands. Good, or add a cereal-style box (sizes vary by brand, so it would be
  an invented one)?
