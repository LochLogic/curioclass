# Sign Shop

## One idea
At a small sign shop the owner, Rosa (made up, labeled "illustration"), takes orders for odd-shaped wooden signs and prices the paint by the square foot, and the child finds each area by cutting and sliding pieces rather than by recalling a formula: a parallelogram sign 5 feet along the base and 2 feet tall has a triangle cut from one end and slid to the other, making a 5 by 2 rectangle of 10 square feet; a triangle sign is copied, turned and joined to make a parallelogram, so it is half of base times height; a bakery's trapezoid sign with parallel sides 6 and 4 feet and height 3 feet is cut into a 4 by 3 rectangle and two triangles of 1 by 3, so 12 + 1 1/2 + 1 1/2 = 15 square feet, and at a sample $0.75 a square foot the paint costs $11.25; composite signs (a house shape, an arrow, a star badge) split into shapes the child already knows; after each cut the child writes the area rule the cut showed, and at the end the shop's price list holds rules the child made, so a sixth grader learns to find the area of right triangles, other triangles, special quadrilaterals and polygons by composing into rectangles or decomposing into triangles and other shapes, and to apply it to real problems.

## Not like
- net-folder (6, concept): nets, surface area and volume. Here flat signs and area.
- tile-the-floor (3, spec): area by counting unit squares. Here area by cutting and sliding.
- shape-sieve (5, spec): sorting quadrilaterals by properties. Here measuring them.
- blueprint-studio (7, concept): scale drawings. Here areas at true size.

## Who and how
- Grade 6, Math, module "Area of Polygons". Standards: 6.G.1 (find the area of right triangles, other triangles, special quadrilaterals, and polygons by composing into rectangles or decomposing into triangles and other shapes; apply these techniques in the context of solving real-world and mathematical problems). 6.G.2 to 6.G.4 stay with net-folder.
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Fifteen sign orders in four shelves (parallelograms, triangles, trapezoids, composites), the paint price, the price list of rules. Extra: Design a sign (the child draws a sign for a partner to price). tool.json `modes: ["Sign orders", "Design a sign"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 6.G.1 (quadrilaterals) | Cut a parallelogram or trapezoid and slide pieces | a rectangle of the same area | 2 |
| 6.G.1 (triangles) | Copy, turn and join a triangle | a parallelogram twice its size | 3 |
| 6.G.1 (polygons, real world) | Split composite signs; price the paint | the order slip with area and cost | 4 |

## Screens and modes
Header (kit): title "Sign Shop"; `Sign orders`, `Design a sign`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A sawdusty sign shop, a workbench with a blank parallelogram sign, paint cans, an order slip, and Rosa in an apron. The welcome is queued (`welcomeAfter: true`): "First order: a parallelogram sign. Paint is priced by the square foot. Tap the saw, then tap where to cut." First hint: "Tap the saw, then tap where to cut."

**Cut and slide (focus: the bench).** At 1366x768 the sign fills the bench with the order slip and price list right; at 680x425 the price list is a tab. The saw cuts only along grid lines or from a vertex straight down to the base (a right-angle mark shows the height). The child drags the cut piece; it snaps where it fits. A 5 by 2 rectangle appears, and the slip writes 5 x 2 = 10 square feet.

**Triangles.** A triangle sign gets a copy; the child turns it and joins the two into a parallelogram, then cuts that into a rectangle. The slip writes 1/2 x 6 x 4 = 12. Right triangles first, then acute and obtuse (the height may fall outside the sign, shown with a dashed line).

**Trapezoids.** The bakery sign: two cuts from the short side's ends make two triangles and a rectangle. 12 + 1 1/2 + 1 1/2 = 15 square feet. A second route (two copies make a parallelogram) is shown after.

**Composites.** A house sign (a 4 by 3 rectangle and a triangle 4 wide and 2 tall: 16 square feet), an arrow, a star badge. The child picks cuts; any correct split is accepted.

**Price it.** Paint costs a sample $0.75 a square foot; the child types each order's cost ($11.25 for the bakery).

**My rules (the aha).** The price list now shows rules the child wrote after each cut. Rosa: "You didn't memorize these. You cut them out yourself."

**The end.** Order slips and the price list. `Print` prints them.

**Design a sign (extra).** The child draws a sign on the grid; a partner prices it.

## Content
- Fifteen orders with whole and half-foot measures, a sample paint price labeled "sample price", all readable with `Read`.
- Trapezoids are inclusive (a parallelogram counts as a trapezoid), as in shape-sieve.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cuts can be undone until `Check`; pieces snap only where they fit.
- Keyboard: Tab to the saw, cut points on the sign, pieces (arrows move, R turns), the slip and the price box; Enter cuts or places.
- With Motion off pieces jump to their new spots.

## Look
- Accent `--brand` #a3262e sign red (header, cut lines, buttons); gold #f4c542 (the piece in hand, a finished rectangle); paper #fbeff0; ink #2c0a0c; muted #5f4f50.
- Contrast (WCAG 2.1, computed): white on brand 7.31:1; brand on paper 6.51:1; ink on paper 16.18:1; muted on paper 6.88:1; ink on gold 11.17:1.
- Never color alone: cut lines are dashed; heights carry a right-angle mark and a number.
- Different from this batch (magnifier indigo, chart sea blue, sprout green, cardboard umber).

## Art
- People (illustrated): Rosa, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the sign shop (1, 16:9), paint cans (1, 1:1).
- Drawn in code: every sign and cut, because the cuts must be exact.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Rosa; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.order + ':' + state.cut + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `cut`: "Tap the saw, then tap where to cut."
- how `slide`: "Drag the piece to where it fits."
- how `rule`: "Type the rule this cut showed."
- how `price`: "Type the paint cost."
- event, whole, my rules.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: shape cutting on a half-foot grid, snap-fit placement, exact areas with `Frac` as described in equation-golf's spec, cost in cents. The inclusive trapezoid test matches coordinate-proof-lab's `quad` with `{trapezoid: 'inclusive'}`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Areas | Type base times height for a triangle | The slip checks the half; the copy round shows why. |
| Rules | Copy a rule from the list | Each rule is typed only after its own cut. |
| Composites | Count squares | Slanted edges make counting fail; a split is needed. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `cut`; `slide`.
2. `rule`.
3. `price`.
4. My rules (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 6.G.1 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Area formulas come from composing and decomposing shapes | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", grades 6-8 measurement | yes |
| The inclusive trapezoid definition | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | docs/agents/audit/gaps.md, catalog fix 3 | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s16, 2026-11-10): (6 + 4) / 2 x 3 = 15 and 4 x 3 + 2 x (1/2 x 1 x 3) = 15; 5 x 2 = 10; 4 x 3 + 1/2 x 4 x 2 = 16; 1/2 x 6 x 4 = 12; 15 x $0.75 = $11.25; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bench and slip; at 680x425 price list as a tab.
2. Parallelograms and trapezoids are cut and slid into rectangles to find area. (6.G.1)
3. Triangles are doubled into parallelograms to find area as half. (6.G.1)
4. Composite signs are split and priced in real orders. (6.G.1)
5. Each rule on the price list is written by the child after a cut.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: pieces jump; no network requests.

## Open questions
- The idea card uses the inclusive trapezoid (default used: inclusive, matching shape-sieve and catalog fix 3).
