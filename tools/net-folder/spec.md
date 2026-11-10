# Net Folder

## One idea
Jun (made up, labeled "illustration") is designing a board game and needs a box and a set of pyramid pieces, so the child works at a cutting mat with a coordinate grid: unfold rounds open a finished box, a triangular prism and a square pyramid into nets and fold them back, and some nets fail to close and show where; grid rounds give a face by its vertices, like (1, 1), (1, 4), (6, 4), (6, 1), and the child draws it and reads side lengths from points that share an x or a y (5 by 3, so 15 square units); area rounds label each face, and a triangle face is found as half of the rectangle drawn around it, so a square pyramid with a 4 by 4 base and triangle faces 4 wide and 3 tall needs 16 + 4 x 6 = 40 square inches of cardboard; fill rounds pack the game box, 2 1/2 by 1 by 1 1/2 inches, with half-inch cubes (5 x 2 x 3 = 30 cubes, each 1/8 cubic inch), giving 3 3/4 cubic inches, the same as l x w x h, while its surface takes 15 1/2 square inches of cardboard; at the end the child sees that the cardboard outside a box and the space inside are different measures built from the same edges, so a sixth grader learns nets and surface area, volume with fractional edges, polygons on the coordinate plane, and triangle area as half a rectangle.

## Not like
- box-packer (5, spec): volume with whole cubes. Here fractional edges and surface area.
- snow-globe-maker (8, concept): curved solids. Here prisms and pyramids.
- packaging-challenge (10, spec): optimizing material. Here measuring it.
- sign-shop (6, concept): flat areas by cutting and sliding. Here faces of solids.

## Who and how
- Grade 6, Math, module "Area, Surface Area and Volume". Standards: 6.G.2 (find the volume of a right rectangular prism with fractional edge lengths by packing it with unit cubes of the appropriate unit fraction edge lengths, and show that the volume is the same as would be found by multiplying the edge lengths of the prism; apply the formulas V = l w h and V = b h to find volumes of right rectangular prisms with fractional edge lengths in the context of solving real-world and mathematical problems), 6.G.3 (draw polygons in the coordinate plane given coordinates for the vertices; use coordinates to find the length of a side joining points with the same first coordinate or the same second coordinate; apply these techniques in the context of solving real-world and mathematical problems), 6.G.4 (represent three-dimensional figures using nets made up of rectangles and triangles, and use the nets to find the surface area of these figures; apply these techniques in the context of solving real-world and mathematical problems), and the triangle part of 6.G.1 (find the area of right triangles and other triangles by composing into rectangles). The rest of 6.G.1 moves to sign-shop.
- Format: sandbox. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three solids to unfold, eight nets (two that fail), six grid faces, four surface-area builds, four fill rounds. Extra: Print and fold (any net prints at true size with glue tabs). tool.json `modes: ["Game box", "Print and fold"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 6.G.4 | Unfold and fold solids; total each face | nets; a running surface-area total | 2 |
| 6.G.1 (triangles) | Draw the rectangle around a triangle face | the triangle as half of it | 2 |
| 6.G.3 | Draw faces from vertices; read side lengths | points sharing an x or a y | 3 |
| 6.G.2 | Pack half-inch cubes; compare with l x w x h | 30 cubes of 1/8; 3 3/4 cubic inches | 4 |

## Screens and modes
Header (kit): title "Net Folder"; `Game box`, `Print and fold`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A cutting mat with a coordinate grid, a finished game box, a craft knife, glue, and Jun with a prototype board. The welcome is queued (`welcomeAfter: true`): "I need to know how much cardboard this box takes. Tap Unfold." First hint: "Tap Unfold."

**Unfold and fold (focus: the solid).** At 1366x768 the 3D view sits left and the flat net on the grid right; at 680x425 they are tabs. Unfold lays the net flat, face by face. The child refolds by tapping each fold line. Two nets in the set fail to close, and the gap glows with "these two faces overlap" or "this side has no face".

**Faces and surface area.** Each face shows its length and width; the child types its area. Triangle faces show a dashed rectangle around them, and the child types the rectangle's area, then half. The total runs at the top: the square pyramid is 16 + 4 x 6 = 40 square inches.

**Grid rounds.** Jun calls out vertices; the child taps them on the grid and the face closes. The child reads each side from coordinates (from (1, 4) to (6, 4) is 6 - 1 = 5) and types the area.

**Fill rounds.** The game box is 2 1/2 by 1 by 1 1/2 inches. The child drags half-inch cubes in layers: 5 along, 2 across, 3 up, 30 in all. A card says 8 half-inch cubes make one cubic inch, so 30 cubes is 30/8 = 3 3/4 cubic inches. The formula line writes 2 1/2 x 1 x 1 1/2 = 3 3/4.

**Inside and outside (the aha).** The box shows its 15 1/2 square inches of cardboard and its 3 3/4 cubic inches of space side by side. Jun: "Same edges, two questions: how much cardboard, and how much fits inside."

**The end.** The net sheet with every total. `Print` prints it.

**Print and fold (extra).** Nets print at true size with glue tabs.

## Content
- Three solids (box, triangular prism, square pyramid), eight nets, six vertex sets, four boxes with fractional edges, all readable with `Read`.
- Measures in inches with halves; cubes of 1/2 inch only, as the standard asks for unit fraction edges.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Folds can be undone; cubes can be removed until `Check`.
- Keyboard: Tab to Unfold, fold lines, faces, grid points (arrows move one unit), cubes and answer boxes; Enter folds, places or checks.
- With Motion off nets unfold and fold at once.

## Look
- Accent `--brand` #74501f cardboard umber (header, fold lines, buttons); gold #f4c542 (the face in hand, a filled layer); paper #f8f2e9; ink #251906; muted #5a5348.
- Contrast (WCAG 2.1, computed): white on brand 7.22:1; brand on paper 6.48:1; ink on paper 15.46:1; muted on paper 6.82:1; ink on gold 10.58:1.
- Never color alone: failing nets name the problem in words; faces carry their measures.
- Different from this batch (magnifier indigo, chart sea blue, sprout green, sign red).

## Art
- People (illustrated): Jun, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the workshop with the cutting mat (1, 16:9), the finished game (1, 4:3).
- Drawn in code: nets, folds, the 3D view and cubes, the grid, so every measure stays exact.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `upbeat-guide` as Jun; `knowing-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.solid + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `fold`: "Tap a fold line to fold it."
- how `face`: "Type this face's area."
- how `vertex`: "Tap the next vertex on the grid."
- how `fill`: "Drag a cube into the box."
- event, whole, inside and outside.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: nets and fold paths, the 3D view, cube packing, exact fractions with `Frac` as described in equation-golf's spec. Grid faces use the coordinate engine's `CoordPlane` with `quadrant: 'first'` and `poly` (coordinate-proof-lab's spec) for drawing only.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Surface area | Count only visible faces | The total checks every face of the net. |
| Triangle faces | Use the whole rectangle | The half is checked; the dashed rectangle shows why. |
| Volume | Count cubes as cubic inches | 30 is checked against 3 3/4, and the 8-cube card is needed. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `fold`; `face`.
2. `vertex`.
3. `fill`.
4. Inside and outside (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 6.G.1 to 6.G.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Packing with unit-fraction cubes links counting to l x w x h | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | Battista (2003), "Understanding students' thinking about area and volume measurement", NCTM Yearbook | yes |
| Students confuse surface area and volume | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", grades 6-8 measurement | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s16, 2026-11-10): 5 x 2 x 3 = 30 cubes and 30 x 1/8 = 3 3/4; 2 1/2 x 1 x 1 1/2 = 3 3/4; surface 2 x (2 1/2 + 3 3/4 + 1 1/2) = 15 1/2; (1, 1) to (6, 4) is 5 by 3, area 15; pyramid 16 + 4 x (1/2 x 4 x 3) = 40; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 3D view and net; at 680x425 tabs.
2. Three solids are unfolded and their surface areas totaled, with triangle faces as half a rectangle. (6.G.4, 6.G.1)
3. Six faces are drawn from vertices and their sides read from coordinates. (6.G.3)
4. Four boxes with fractional edges are packed with half-inch cubes and match l x w x h. (6.G.2)
5. Failing nets say what is wrong in words.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: nets fold at once; no network requests.

## Open questions
- The idea card moves the rest of 6.G.1 (parallelograms, trapezoids, composite polygons) out of this tool (default used: sign-shop teaches it; this tool keeps triangle faces).
