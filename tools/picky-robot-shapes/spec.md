# Picky Robot Shapes

## One idea
A picky robot named Gizmo guards a gate with a sign ("Only triangles may pass"), and a line of shapes waits: a tall thin triangle, a blue one, an upside-down one, a shape with a rounded corner and one with a gap, so the child drags each to Yes or No and Gizmo explains ("Three straight sides, closed. A triangle, even if it's blue and upside down." "That one has a gap. Not closed. Not a triangle."); new gate signs follow (squares, then shapes with four sides), and the child draws a shape on a dot grid that Gizmo must accept; in the build yard the child makes pictures from flat shapes (two triangles make a square, a square and two half-circles make a rocket fin) and from solids (stacks of cubes, a cone on a cylinder for a tower), and then reuses a shape they built (the square made of triangles) as one piece in a bigger picture; at the end Gizmo's rule card lists what really matters (sides, corners, closed) and what never does (color, size, turn), so a first grader learns to tell defining attributes from non-defining ones, to build and draw shapes that have given attributes, and to compose flat and solid shapes into new shapes and then compose new shapes from those.

## Not like
- pattern-block-windows (K, spec): filling outlines with blocks. Here which features make a shape that shape.
- shape-spy (K, spec): naming shapes in scenes. Here rules about what makes a shape.
- pizza-party (1, spec): cutting shapes into equal shares. Here putting shapes together.
- shape-family-tree (3, concept): families of four-sided shapes. Here first defining features.

## Who and how
- Grade 1, Math, module "Shapes and Their Attributes". Standards: 1.G.1 (distinguish between defining attributes (e.g., triangles are closed and three-sided) versus non-defining attributes (e.g., color, orientation, overall size); build and draw shapes to possess defining attributes), 1.G.2 (compose two-dimensional shapes (rectangles, squares, trapezoids, triangles, half-circles, and quarter-circles) or three-dimensional shapes (cubes, right rectangular prisms, right circular cones, and right circular cylinders) to create a composite shape, and compose new shapes from the composite shape).
- Format: builder. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Four gate signs (triangles, squares, four sides, closed shapes), 32 gate shapes, a dot grid for drawing, six flat builds, four solid builds, two reuse builds, the rule card. Extra: Two robots (two players set signs for each other). tool.json `modes: ["Gate", "Two robots"]`, `minutes: "15-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1.G.1 (defining or not) | Sort gate shapes to Yes or No | Gizmo's reason; the rule card | 2 |
| 1.G.1 (build and draw) | Draw a shape on the dot grid that passes | the drawn shape at the gate | 3 |
| 1.G.2 | Build flat and solid pictures; reuse a built shape | the composite; the bigger build | 4 |

## Screens and modes
Header (kit): title "Picky Robot Shapes"; `Gate`, `Two robots`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A tidy robot workshop with a gate, Gizmo the robot holding a sign: "Only triangles may pass." Five shapes wait in line. The welcome is queued (`welcomeAfter: true`): "Beep! I'm Gizmo. I'm very picky. Only triangles may pass. Drag a shape to Yes or No." First hint: "Drag the first shape to Yes or No."

**The gate (focus: the line and gate).** At 1366x768 the line of shapes runs along the bottom, the gate in the middle, Yes and No pads on either side; at 680x425 one shape at a time sits above the two pads. Gizmo gives a reason for each: sides, corners, closed or not. Color, size and turn are named as "doesn't matter."

**Draw one.** A dot grid. "Draw a shape I'll let through." The child taps dots to draw sides; Gizmo checks it.

**Build yard (1.G.2).** Flat: the child drags shapes (rectangles, squares, trapezoids, triangles, half-circles, quarter-circles) to fill a picture outline, and two triangles snap into a square. Solid: cubes stack into a wall, a cone sits on a cylinder for a tower, prisms make a bench.

**Reuse (the aha).** The square the child built from two triangles becomes one piece; the child uses it in a house picture. Gizmo: "You made a new shape, then used it to make a bigger one!"

**The end.** Gizmo's rule card: "What matters: sides, corners, closed. What doesn't: color, size, turn." `Print` prints it and a dot grid.

**Two robots (extra).** Each player picks a sign and builds shapes for the other's gate.

## Content
- Four signs, 32 gate shapes in many colors, sizes and turns (including near-misses with a gap or a curve), flat and solid pieces from the standard, all spoken.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A shape on the wrong pad slides back with Gizmo's reason; pieces in the yard can be moved at any time.
- Keyboard: Tab to each shape, the pads, dots and build pieces; Enter places; arrows move and R turns a piece.
- With Motion off shapes jump and solids show three still views.

## Look
- Accent `--brand` #2b6650 circuit green (header, Gizmo's panel, buttons); gold #f4c542 (the shape in hand, the gate light); paper #eff7f3; ink #0a1f17; muted #47584f.
- Contrast (WCAG 2.1, computed): white on brand 6.73:1; brand on paper 6.18:1; ink on paper 15.78:1; muted on paper 6.94:1; ink on gold 10.57:1.
- Never color alone: Yes and No pads carry a check and a cross and the words.
- Different from this batch (tomato red, notebook navy, ballot violet, brass brown).

## Art
- Local FLUX (`scripts/localart.py`): the robot workshop (1, 16:9), Gizmo in three poses (sign, beep yes, beep no) (3, 1:1).
- Drawn in code: every shape and solid, the dot grid, outlines, the rule card.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as Gizmo; `big-sister` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.sign + ':' + state.item + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `gate`: "Drag the shape to Yes or No."
- how `draw`: "Tap dots to draw the sides."
- how `build`: "Drag a piece into the picture."
- how `reuse`: "Drag your new shape into the house."
- event, whole, each gate reason (short).
- event, whole, reuse.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the gate checker (sides, corners, closed), the dot grid, composite pieces that can be reused. It may reuse edge snapping from `/* PATTERN-BLOCKS ENGINE: begin */ ... /* end */` as described in pattern-block-windows' spec. Gate shapes sit in a marked block `/* PICKY-ROBOT DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Gate | Sort by color | Signs never depend on color; near-miss shapes come in every color. |
| Draw | Draw a squiggle | Gizmo checks for straight sides and a closed shape. |
| Reuse | Build with single pieces only | The reuse picture needs the composite piece. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `gate`; reasons.
2. `draw`.
3. `build`.
4. Reuse (whole), waits. `reuse`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 1.G.1, 1.G.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Children often reject true triangles that are thin or turned, so varied examples and near-misses matter | Clements and Sarama, "Learning and Teaching Early Math" (2014) | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | yes |
| Composing shapes, then composing with composites, is a grade 1 step | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | Clements and Sarama, "Learning and Teaching Early Math" (2014) | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r8, 2026-11-10): two right triangles from a square's diagonal keep square corners; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 line, gate and pads; at 680x425 one shape.
2. 32 gate shapes are sorted with reasons that name sides, corners and closed. (1.G.1)
3. A drawn shape passes each sign. (1.G.1)
4. Flat and solid builds are made and a composite is reused. (1.G.2)
5. Every card is spoken; every control is 56 px or more.
6. The rule card lists what matters and what doesn't.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps and still views; no network requests.

## Open questions
- The idea card flags overlap with pattern-block-windows (default used: this tool is about which features make a shape that shape and about reusing a composite; pattern-block-windows keeps filling outlines in kindergarten).
