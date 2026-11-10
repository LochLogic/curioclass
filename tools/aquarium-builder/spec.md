# Aquarium Builder

## One idea
At a neighborhood aquarium shop the owner, Dani (made up, labeled "illustration"), takes custom orders for tanks and planter boxes shaped as composite prisms, and the child plans each one twice, once for the glass or wood (surface area) and once for the water or soil (volume); the first order is an L-shaped tank whose footprint is a 24 by 12 inch rectangle joined to a 12 by 12 square, 12 inches tall, so the floor is 432 square inches, the water fills 5,184 cubic inches (about 22.4 gallons at 231 cubic inches a gallon), and with no lid the glass is the floor plus 96 inches of wall around times 12 inches high, 1,584 square inches; later orders build a triangular prism planter (a 3-4-5 right triangle end, 6 feet long: 36 cubic feet of soil, 84 square feet of wood if closed), a trapezoid-ended trough, and a stepped display tank made of cubes; each plan starts by splitting the shape into pieces the child knows, finding each piece's area or volume, and joining them, with a check that hidden faces where pieces meet are not counted as glass; at the end the child designs a tank of their own and orders both measures, so a seventh grader learns to solve real-world problems involving area, volume and surface area of two- and three-dimensional objects composed of triangles, quadrilaterals, polygons, cubes and right prisms.

## Not like
- net-folder (6, spec): nets and single boxes. Here composite prisms.
- big-wheel-small-wheel (7, spec): circles. Here polygons and prisms.
- box-packer (5, spec): volume by packing cubes. Here volume and surface together.
- snow-globe-maker (8, concept): curved solids. Here flat-faced ones.

## Who and how
- Grade 7, Math, module "Surface Area and Volume of Prisms". Standards: 7.G.6 (solve real-world and mathematical problems involving area, volume and surface area of two- and three-dimensional objects composed of triangles, quadrilaterals, polygons, cubes, and right prisms).
- Format: builder. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six shop orders (two tanks, two planters, a trough, a stepped tank), the split tool, the glass and water ledger, the design-your-own order. Extra: Shop board (the class compares designs with the same volume and different glass on the projector). tool.json `modes: ["Shop orders", "Shop board"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.G.6 (area) | Split footprints and end faces into known shapes | the L as a rectangle and a square | 2 |
| 7.G.6 (volume) | Base area times height for each piece; join | the water level rising | 2 |
| 7.G.6 (surface area) | Add exposed faces only | glass panels lighting one by one | 3 |
| 7.G.6 (problems) | Fill orders and design a tank | the ledger with both measures | 4 |

## Screens and modes
Header (kit): title "Aquarium Builder"; `Shop orders`, `Shop board`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A cozy aquarium shop with bubbling tanks, a work table with an empty L-shaped glass frame, an order slip, and Dani with a fish net. The welcome is queued (`welcomeAfter: true`): "Order one: an L-shaped tank, 12 inches tall. How much glass, and how much water? Tap Split to break the floor into shapes." First hint: "Tap Split."

**Split (focus: the shape).** At 1366x768 the 3D shape fills the left with the ledger right; at 680x425 the ledger is a sheet. `Split` draws cut lines the child chooses; each piece shows its measures. The child types each piece's area and the total.

**Water.** For each piece the child types base area times height; the tank fills to the brim in the 3D view as each piece is entered. The ledger converts cubic inches to gallons with a card (231 cubic inches is one gallon).

**Glass.** Each face lights as the child taps it and types its area. Faces where two pieces meet stay dark and say "inside, no glass". The lid toggle adds or removes the top.

**More orders.** The triangular prism planter, the trapezoid-ended trough, the stepped tank made of 1-foot cubes, and a hexagonal-ended display case.

**Your design.** The child builds a tank from pieces (cubes and prisms) to hold at least 20 gallons and types both measures; the shop board shows designs side by side.

**Two questions (the aha).** Dani: "Same tank, two orders: glass for the outside, water for the inside. Split it, and both get easy."

**The end.** The ledger and designs. `Print` prints them.

**Shop board (extra).** Designs with the same volume and different glass.

## Content
- Six orders in inches and feet, the gallon card, all readable with `Read`.
- Fish shown are common freshwater species; no live-animal care claims.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cut lines can be redrawn until `Check`; faces can be tapped in any order.
- Keyboard: Tab to the shape (arrows turn it), cut points, faces, the lid toggle, piece boxes and ledger lines; Enter cuts or checks.
- With Motion off water appears full and the shape does not spin.

## Look
- Accent `--brand` #12684f reef green (header, the ledger, buttons); gold #f4c542 (the face in hand, a counted panel); paper #ebf6f2; ink #04221a; muted #4a5853.
- Contrast (WCAG 2.1, computed): white on brand 6.73:1; brand on paper 6.09:1; ink on paper 15.21:1; muted on paper 6.76:1; ink on gold 10.34:1.
- Never color alone: counted faces carry a check and their area; inside faces say "inside".
- Different from this batch (blueprint blue, loop indigo, case-file brown, factory red).

## Art
- People (illustrated): Dani, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the aquarium shop (1, 16:9), a finished tank with fish (1, 4:3), a planter of herbs (1, 4:3).
- Drawn in code: every shape in 3D, glass and water, cut lines, the ledger, because water level and glass must read exactly.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Dani; `easy-coach` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.order + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `split`: "Tap Split, then tap where to cut."
- how `area`: "Type this piece's area."
- how `water`: "Type base area times height."
- how `glass`: "Tap a face and type its area."
- how `design`: "Drag pieces to build your tank."
- event, whole, two questions.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: composite prisms from pieces with shared-face detection, the 3D view with water level, exact areas and volumes with `Frac` as described in equation-golf's spec, the ledger.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Glass | Add every piece's full surface | Inside faces are checked and must be left out. |
| Water | Multiply the outer box | The L leaves a missing corner, and the check catches it. |
| Design | Type any numbers | Both measures are computed from the built design. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `split`; `area`.
2. `water`.
3. `glass`; `design`.
4. Two questions (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.G.6 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| One U.S. gallon is 231 cubic inches | NIST, Handbook 44, Appendix C | NIST, Special Publication 811 | yes |
| Decomposing composite solids supports surface area and volume | Common Core Standards Writing Team (2012), "Progressions for the CCSS, 7-8 Geometry" | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", grades 6-8 measurement | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s20, 2026-11-10): 24 x 12 + 12 x 12 = 432 and 432 x 12 = 5,184 cubic inches, about 22.4 gallons; the L's perimeter is 96, so walls are 1,152 and glass with no lid is 1,584; the planter is 1/2 x 3 x 4 x 6 = 36 cubic feet and 12 + 12 x 6 = 84 square feet; a trapezoid end of bases 4 and 2 and height 2 is 6, times 5 long is 30; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 shape and ledger; at 680x425 ledger as a sheet.
2. Composite footprints and ends are split into known shapes, and volumes are found piece by piece. (7.G.6)
3. Surface areas count only outside faces, with and without lids. (7.G.6)
4. Six orders and one design are filled with both measures. (7.G.6)
5. Inside faces are marked and never counted.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: water appears full; no network requests.

## Open questions
None.
