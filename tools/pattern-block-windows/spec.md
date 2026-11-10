# Pattern Block Windows

## One idea
At a sunny pond a friendly frog named Pip sits by a lily pad outline and a tray of pattern blocks (green triangles, blue rhombuses, red trapezoids, yellow hexagons, orange squares), and the child drags blocks onto the lily pad until it's filled, with blocks snapping at their edges; when two green triangles make a blue rhombus Pip cheers and shows both, three triangles make a trapezoid and six make a hexagon; at the reed bank the child builds a triangle, a square and a rectangle from cattail sticks with pebbles at the corners while Pip counts the sides and corners out loud; at the stepping stones two blocks sit side by side (a big tilted square and a small straight square, a long thin triangle and a short wide one) and the child taps "same shape" or "different shape" while Pip names the sides, corners and size, and tips a block on its edge to show it's a thin solid with faces; at the end one hexagon window gets filled three ways (one hexagon, two trapezoids, six triangles), so a kindergartner learns to compare shapes of different sizes and turns by their sides and corners, to build shapes from sticks and balls, and to put small shapes together to make larger shapes.

## Not like
- shape-spy (K, concept): finding and naming shapes in the world. Here building and putting shapes together.
- picky-robot-shapes (1, concept): shapes sorted by a robot's rules. Here shapes made from smaller shapes.
- tile-the-floor (3, concept): covering a floor to find area. Here filling outlines to see shapes inside shapes.
- shape-talk (K to 2, live): describing shapes in words. Here hands-on building.

## Who and how
- Kindergarten, Math, module "Build a Shape". Standards: K.G.4 (analyze and compare two- and three-dimensional shapes, in different sizes and orientations, using informal language to describe their similarities, differences, parts and other attributes), K.G.5 (model shapes in the world by building shapes from components and drawing shapes), K.G.6 (compose simple shapes to form larger shapes).
- Format: sandbox. Driver: one child with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 64 px or more.
- Six lily pad outlines to fill, three stick shapes to build, six stone pairs to compare, the hexagon window filled three ways. Extra: Free pond (the child's own pictures with any blocks, saved as a picture on the device). tool.json `modes: ["Pond", "Free pond"]`, `minutes: "10-20"`, `grades_label: "Kindergarten"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K.G.6 | Fill lily pads and the hexagon window with smaller blocks | blocks snapping; the shape they make | 2 |
| K.G.5 | Build a triangle, a square and a rectangle from sticks and pebbles | the stick shape; Pip counting | 3 |
| K.G.4 | Compare stone pairs by sides, corners, size and turn | two blocks side by side; Pip's words | 4 |

## Screens and modes
Header (kit): title "Pattern Block Windows"; `Pond`, `Free pond`; `Read`, `Motion`, `Sound`, `Print`. Controls 64 px or more.

**On load and first tap.** A bright pond with lily pads, cattails and stepping stones. Pip the frog sits next to an empty lily pad outline shaped like a big triangle. A tray of blocks at the bottom. The welcome is queued (`welcomeAfter: true`): "Hi! I'm Pip. My lily pad has a hole in it. Can you fill it with blocks? Drag a green triangle onto the lily pad." First hint: "Drag a green triangle onto the lily pad."

**Lily pads (focus: the outline).** At 1366x768 the pond fills the screen with the tray along the bottom; at 680x425 the tray is one scrolling row and the outline is centered. Blocks snap at edges. When two triangles sit edge to edge, Pip says "Two triangles make a rhombus!" and a blue rhombus shadow appears beside them. Six outlines, from a small triangle to a big hexagon. A block that doesn't fit slides back with "Try turning it." A turn button sits on each block.

**Reed bank (K.G.5).** Cattail sticks and pebbles. The child drags sticks into a shape and drops pebbles on the corners. Pip counts: "One, two, three sides. One, two, three corners. A triangle!" Then a square (four equal sticks) and a rectangle (two long, two short).

**Stepping stones (K.G.4).** Two blocks on two stones. The child taps "Same shape" or "Different shape." Pip explains: "Both have four sides and four square corners. This one is big and tipped. Still a square!" A `Tip it` button stands a block on its edge so the child sees it's thin and solid.

**The hexagon window (the aha).** A round window shaped like a hexagon in Pip's lily pad house. The child fills it once with one hexagon, then with two trapezoids, then with six triangles. Pip: "Three ways to make the same shape!"

**The end.** Pip waves from the window with the three fills in a row. `Print` prints them as a coloring page.

**Free pond (extra).** Any blocks, any picture. `Save picture` saves an image on this device only; nothing is uploaded.

## Content
- Five block types with sides and corners, six outlines, three stick shapes, six stone pairs, the hexagon window, every line spoken.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Blocks are big (at least 64 px on their shortest side) and snap generously.
- Keyboard: Tab to tray blocks, the turn button, outlines, sticks, pebbles and stone answers; Enter picks up and places; arrows move a held block.
- With Motion off blocks jump into place and Pip doesn't hop.

## Look
- Accent `--brand` #2d6a3e pond green (header, outlines, buttons); gold #f4c542 (the block in hand, snapped edges); paper #f0f7f1; ink #0b1f10; muted #4a5a4d.
- Contrast (WCAG 2.1, computed): white on brand 6.48:1; brand on paper 5.95:1; ink on paper 15.83:1; muted on paper 6.74:1; ink on gold 10.60:1.
- Never color alone: blocks carry their shape names when held; Pip always says the shape.
- Different from this batch (skate purple, storm slate, strawberry red, wave blue).

## Art
- Local FLUX (`scripts/localart.py`): the pond scene (1, 16:9), Pip the frog in four poses (cheer, count, wave, think) (4, 1:1), Pip's lily pad house (1, 4:3).
- Drawn in code: blocks, outlines, sticks, pebbles, stones.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as Pip; `gentle-storyteller` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.place + ':' + state.item + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `fill`: "Drag a block onto the lily pad."
- how `turn`: "Tap the turn button on the block."
- how `stick`: "Drag a stick to make a side."
- how `pebble`: "Drag a pebble onto a corner."
- how `compare`: "Tap Same shape or Different shape."
- event, whole, each make (two triangles make a rhombus).
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
pattern-blocks (family "pattern-blocks"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* PATTERN-BLOCKS ENGINE: begin */ ... /* end */`: the five block shapes with sides and corners, edge snapping with turns in 30-degree steps, outline fill checks and "makes" detection (two triangles make a rhombus), so later pattern block tools reuse them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Fill | Drop blocks anywhere | Only blocks that fit snap; the rest slide back. |
| Sticks | Drop sticks in a pile | Pip counts only closed shapes. |
| Compare | Tap the same answer each time | Pip explains each pair; nothing is lost, the child tries again. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `fill`; `turn`.
2. Make (whole), waits.
3. `stick`; `pebble`.
4. `compare`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for K.G.4, K.G.5, K.G.6 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Pattern block shapes and how they combine (two triangles a rhombus, three a trapezoid, six a hexagon) | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | National Council of Teachers of Mathematics, Illuminations, "Pattern blocks" | yes |
| Young children compare shapes by sides and corners, regardless of size and turn | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | Clements and Sarama, "Learning and Teaching Early Math" (2014) | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r5, 2026-11-10): a hexagon is one hexagon, two trapezoids, three rhombuses or six triangles; triangle, square and hexagon have 3, 4 and 6 sides; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 pond and tray; at 680x425 one-row tray.
2. Six lily pads and the hexagon window are filled three ways. (K.G.6)
3. A triangle, a square and a rectangle are built from sticks and pebbles. (K.G.5)
4. Six stone pairs are compared and Pip names sides, corners and size. (K.G.4)
5. Every card is spoken and every control is 64 px or more.
6. Saved pictures stay on the device; nothing is uploaded.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: blocks jump into place; no network requests.

## Open questions
None.
