# Slice and Stack
Renamed from: Slice It

## One idea
A single moving plane is the whole tool: slide it through a solid and the cut face shows the cross section's shape
and area, tilt it through a cube to find a triangle, a pentagon or a hexagon, and run it through two solids at once
to see that equal slices at every height mean equal volume, which is how a cone becomes a third of a cylinder and a
sphere two thirds.

## Not like
- solid-spinner (gr 12 explorer): spun solids cut into thin coins whose sum becomes an integral. Here no sums and no calculus: slices are compared at the same height (Cavalieri), and the spin mode only names the solid.
- cone-slicer, now Conic Focus Finder (gr 12 explorer): curves from distance rules, no solids. Here only solids.
- packaging-challenge (gr 10, this group): surface area for a fixed volume. Here volume itself, and why its formulas are true.
- size-of-everything (gr 7-9 explorer): sizes across scales. Here shapes inside one solid.

## Who and how
- Grade 10, Geometry, module Volume and Cross Sections. Students drive, own laptops or pairs; also a projector demo.
  10 to 35 minutes.
- Topic line: "cross sections and volume".
- Standards (module): G-GMD.A (informal arguments for volume formulas, Cavalieri's principle; use the volume formulas
  for cylinders, pyramids, cones and spheres), G-GMD.B (2D cross sections of 3D objects; solids made by rotating
  2D objects).
- CCSS clusters: Cut serves G-GMD.B.4 and G-GMD.A.3; Twins serves G-GMD.A.1 and A.2 (+, the sphere); Spin serves
  G-GMD.B.4.
- tool.json: driver "students or teacher", minutes "10-35", modes ["Cut", "Twins", "Spin"], grades_label "Grade 10",
  third_party ["Three.js r128 (MIT)"].

## Screens and modes
Header (kit, 9-12 theme): title "Slice and Stack", subtitle "One plane. Every shape inside." Modes `Cut` (opens
first), `Twins`, `Spin`. Kit buttons `Motion`, `Sound`, `Read`.
Layout: stage left (a real 3D view, Three.js r128, drag to turn the view, wheel or pinch to zoom, `Reset view`),
panel right (plane controls, the cross section drawn flat and true to size, readouts). Under 1000 px wide the panel
goes under the stage with the plane controls first. Under 900 px tall the flat cross section sits as an inset in the
stage's corner so the plane sliders stay in view.

Solids are glassy (see-through) with crisp edges; the cutting plane is a large glowing sheet; the cross section is
a solid filled face where plane and solid meet. `Lift` raises the part of the solid above the plane straight up so
the cut face is in plain sight.

### Cut (explore)
- Solid picker: `Cube`, `Square pyramid`, `Triangular prism`, `Cylinder`, `Cone`, `Sphere`. Size sliders for the
  solid's own measures (Content).
- Plane controls: `Height` (slides the plane along its normal through the whole solid), `Tilt` (0° to 90°, 0° is
  level), `Turn` (0° to 360°, the tilt's direction). Buttons `Level`, `Upright`.
- Readouts: the cross section's name (Content), number of sides, side lengths, angles, area, and the solid's volume
  with its formula and numbers ("V = ⅓Bh = ⅓ × 16 × 6 = 32").
- Cube only: `Find them all`, a checklist of eight cross sections (triangle, square, rectangle, rhombus,
  parallelogram, trapezoid, pentagon, hexagon) that tick when the current cut is one; `Show me one` per item sets
  an exact plane. A line under it: "No cut gives seven sides: a cube has only six faces."
### Twins (Cavalieri)
- Two solids side by side on one table, one level plane through both. Twin picker (Content). The two flat slices
  are drawn side by side in the panel with their areas, and a line "same area at every height" or not.
- `Sweep` moves the plane bottom to top over 4 s; a bar chart builds up the slice area against height for each
  solid; equal twins draw the same bars. Then the volume line: "Equal slices at every height, so equal volume."
### Spin (explore)
- A flat shape on a side panel next to a vertical axis. Shape picker (Content). Drag the shape's distance from the
  axis (0 to 3 units). `Spin` sweeps it a full turn around the axis (2 s, instant with Motion off) and the solid
  appears. The panel names the solid. A level plane in the solid shows that every level slice is a circle, a ring
  or two rings.

## Content
Cut solids (default sizes, units): cube edge 4 (V = 64); square pyramid base 4, height 6 (V = 32); triangular prism
right triangle legs 3 and 4, length 6 (V = 36); cylinder radius 2, height 5 (V = 20π ≈ 62.83); cone radius 2,
height 6 (V = 8π ≈ 25.13); sphere radius 3 (V = 36π ≈ 113.10). Size sliders 1 to 6, step 0.5.
Level cut checks: cone r 2, h 6 at height 3: circle radius 1, area π ≈ 3.14. Pyramid at height 3: square side 2,
area 4. Sphere r 3 at 2 above center: circle radius √5, area 5π ≈ 15.71.
Cube "Show me one" planes (cube from (0,0,0) to (4,4,4), plane ax + by + cz = d), results recomputed:
- Triangle: x + y + z = 2, equilateral, side 2.83, area 3.46.
- Square: z = 2, side 4, area 16.
- Rectangle: x + z = 4, 4 by 5.66, area 22.63.
- Rhombus: x + y − 2z = 0, side 4.47, angles 78.46° and 101.54°, area 19.60.
- Parallelogram: x + 2y + 4z = 12, sides 4.12 and 4.47, angles 83.77° and 96.23°, area 18.33.
- Trapezoid: 2x + 2y − z = 4, parallel sides 2.83 and 5.66, legs 4.47, area 18.00.
- Pentagon: x + y + 2z = 6, area 17.15 (two pairs of parallel sides, never regular).
- Hexagon: x + y + z = 6, regular, side 2.83, area 20.78.
Twins (each pair has equal slices at every height):
1. Straight and leaning coin stacks: 20 coins, radius 1, thickness 0.15; V = 3π ≈ 9.42 each.
2. Straight and slanted cylinder, radius 2, height 5: V = 20π ≈ 62.83 each.
3. Cone and square pyramid: cone radius 2, height 6; pyramid base side √(4π) ≈ 3.54 (base area 4π), height 6; at
   every height both slices have area 4π(1 − y ÷ 6)²; V = 8π ≈ 25.13 each, one third of the 24π cylinder.
4. Upright and leaning square pyramids, base 4, height 6: V = 32 each.
5. Hemisphere and "bowl" (a cylinder radius 3, height 3, with a cone of radius 3, height 3 hollowed out of it, point
   down): at height y the hemisphere's slice is π(9 − y²), the bowl's is 9π − πy², the same; V = 27π − 9π = 18π
   ≈ 56.55 each, so a whole sphere is 36π = (4/3)π × 27.
6. Not twins (to compare): cylinder radius 2, height 6 and cone radius 2, height 6: slices differ above the base;
   V = 24π and 8π.
Spin shapes (axis vertical): rectangle touching the axis → cylinder; right triangle with a leg on the axis → cone;
semicircle with its diameter on the axis → sphere; right trapezoid with its straight side on the axis → frustum (a
cone with its top cut off); right triangle with the hypotenuse on the axis → two cones base to base; rectangle away
from the axis → a tube (cylinder with a hole); circle away from the axis → a torus (ring doughnut shape).

## Interactions in detail
- Cross sections are computed exactly: the plane is intersected with every edge (polyhedra) or with the surface
  equation (cylinder, cone, sphere), the polygon is ordered around its centroid, and area comes from the vector
  cross product sum. Curved sections (circle, ellipse, parabola-like and hyperbola-like slices of a cone, cylinder
  ellipses) are named: "circle", "ellipse", "a curve with a straight edge" when the plane also crosses a flat base.
- Cube names use tolerances: sides parallel when their directions differ by under 0.2°, equal within 0.5%, right
  angles within 0.2°. Order of names: square, rectangle, rhombus, parallelogram, trapezoid (exactly one pair
  parallel), then by sides. Every quadrilateral from a cube has at least one parallel pair, so no "other" is needed.
- Edges: a plane that only touches a vertex or an edge shows "just touching: no area" (area 0). A plane outside the
  solid shows nothing and "The plane misses the solid." Height is clamped a little past the solid on both sides.
- Twins sweep compares slice areas computed at 50 heights; equal within 1e-9 shows "same area"; the bar charts are
  drawn from the same numbers.
- Volumes show exact forms with π and a decimal to two places.
- Keyboard: every slider works with arrows; `Turn view` buttons (left, right, up, down) replace dragging; the cut
  face's name and area are in an aria-live line.
- Reset: `Reset view` and `Reset plane`; mode states last for the page session; nothing is saved.
- `window.__tool = {state, setMode, solid(id, sizes), plane(a, b, c, d), section(), twins(n), spin(shape, dist)}`.

## Look
Accent `--brand #7cff4f` (laser green: the cutting plane is a sheet of laser light), `--brand-ink #10161f`. Stage
`#0b0f14`; solids glass `#9fb3c8` at 35% with edges `#d7e0ea`; plane accent at 20% with an accent rim; the cross
section solid accent with a dark outline; the lifted part a little brighter glass.
Contrast (computed): brand on --panel 13.41:1, on --sec-bg 12.71:1, on the stage 14.89:1; brand-ink on brand
14.07:1. Greener than zoom-to-the-limit's lime #c6f25a (gr 12) and model-my-world's #d4e65a (gr 9); different from
solid-spinner's clay #e39b6e.

## Art
none: drawn in code (Three.js solids, plane, flat sections, charts, preview.svg).

## Voice
Bank voice `playful-friend` (Laomedeia), style "playful and bright, like a fun teacher with a laser cutter". No 9-12
math tool uses it. `Curio.voice`, `scope: () => state.mode`.
- wCut (how): "Pick a solid. Slide the plane through it, then tilt it. Watch the shape of the cut."
- wTwins (how): "Two solids, one plane. Tap Sweep and compare the slices at every height."
- wSpin (how): "Pick a flat shape, set how far it sits from the axis, then tap Spin."
- hexagon (event, the cube section becomes a hexagon; stale when the plane moves): "Six sides! A cube can hide a hexagon."
- allFound (event, all eight cube sections ticked; stale on solid change): "All eight. That's every kind a cube can give."
- equal (event, a twin sweep ends on an equal pair; stale on twin change): "Same slice at every height, so the same volume."
- notEqual (event, sweep ends on pair 6; stale on twin change): "These slices differ, so the volumes can too."

## Family engine
none.

## Sources
- G-GMD text: Common Core State Standards for Mathematics, High School Geometry, Geometric Measurement and Dimension, https://www.thecorestandards.org/Math/Content/HSG/GMD/
- Cavalieri's principle: Wolfram MathWorld, "Cavalieri's Principle", https://mathworld.wolfram.com/CavalierisPrinciple.html
- Cone is a third of the cylinder (Euclid XII.10) and pyramid a third of the prism (XII.7 corollary): Euclid's Elements, D. E. Joyce edition, https://mathcs.clarku.edu/~djoyce/java/elements/bookXII/bookXII.html
- Hemisphere equals cylinder minus cone, slice by slice (the sphere example of Cavalieri's principle): Wikipedia, "Cavalieri's principle", section "Spheres", https://en.wikipedia.org/wiki/Cavalieri%27s_principle (read 2026-10-27)
- Volume formulas: OpenStax, Prealgebra 2e, 9.6 "Solve Geometry Applications: Volume and Surface Area", https://openstax.org/books/prealgebra-2e/pages/9-6-solve-geometry-applications-volume-and-surface-area
- Three.js r128, MIT license, https://github.com/mrdoob/three.js/blob/r128/LICENSE
- Every cube section and volume above was recomputed in Python (2026-10-27).

## Done when
1. Cut, cube, `Level` at height 2: "square, side 4, area 16".
2. Each `Show me one` gives its listed name and area (hexagon 20.78, rhombus 19.60, trapezoid 18.00, pentagon 17.15) and ticks the checklist.
3. Cone r 2, h 6, level cut at height 3: circle area 3.14; sphere r 3 at 2 above center: 15.71.
4. Twins 3 sweep draws equal bars and shows 25.13 for both; twins 5 shows 56.55 for both and the sphere line 36π; twins 6 draws unequal bars.
5. Spin: semicircle on the axis gives "sphere"; circle 2 units away gives "torus"; rectangle away from the axis gives "tube".
6. A plane through only one vertex of the cube shows "just touching: no area".
7. Keyboard alone can cut a hexagon and run a sweep; every size in STANDARDS.md keeps the 3D view and the plane sliders visible without page scrolling.
8. Console clean, no network, no em dashes, "Curio Class" only in full.

## Open questions
- Title: "Slice It!" is a published mobile puzzle game. This spec renames the tool "Slice and Stack". Keep it?
