# Transformation Dock

## One idea
At a busy cargo dock laid out on a coordinate grid, the crane operator, Kemi (made up, labeled "illustration"), needs an L-shaped cargo tile set down exactly on its painted outline, and the child steers it with moves added to a route list (slide by (3, -2), flip over the y-axis, turn 90 degrees about the origin, resize by 2 from the origin) while the tile's corner coordinates update and measuring tools show that lengths, angles and parallel sides survive every slide, flip and turn; before each move plays the child predicts where the corner (2, 5) lands (the turn sends it to (-5, 2), the flip to (-2, 5), the slide to (5, 3), the resize to (4, 10)) and writes the rule, such as (x, y) to (-y, x); match rounds decide which docks hold a congruent outline (only slides, flips and turns are needed) and which hold one only similar (a resize is needed too), and the replayed route is the proof; in the last yard copies of one triangle slide and turn to tile the floor, and the three angles (50, 60 and 70 degrees in the first one) meet on a straight edge to make 180, a crane rail crossing two parallel tracks shows equal angles, and a resized triangle keeps its angles, so two matching angles are enough for similar; at the end the child sees that rigid moves keep size and shape, a resize keeps only shape, and a list of moves is an argument, so an eighth grader learns the properties of rotations, reflections, translations and dilations, uses them to show congruence and similarity, describes their effect with coordinates, and argues angle facts about triangles and parallel lines.

## Not like
- rigid-motion-twins (10, spec): fewest-move proofs, same transformations engine. Here moves and coordinates first.
- image-transformer (12, spec): matrices. Here moves by rule.
- shrink-ray (5, spec): scaling by fractions. Here dilation as a move.
- blueprint-studio (7, spec): scale drawings. Here similarity by moves.

## Who and how
- Grade 8, Math, module "Transformations". Standards: 8.G.1 (verify experimentally the properties of rotations, reflections, and translations: lines are taken to lines, and line segments to line segments of the same length; angles are taken to angles of the same measure; parallel lines are taken to parallel lines), 8.G.2 (understand that a two-dimensional figure is congruent to another if the second can be obtained from the first by a sequence of rotations, reflections, and translations; given two congruent figures, describe a sequence that exhibits the congruence between them), 8.G.3 (describe the effect of dilations, translations, rotations, and reflections on two-dimensional figures using coordinates), 8.G.4 (understand that a two-dimensional figure is similar to another if the second can be obtained from the first by a sequence of rotations, reflections, translations, and dilations; given two similar two-dimensional figures, describe a sequence that exhibits the similarity between them), 8.G.5 (use informal arguments to establish facts about the angle sum and exterior angle of triangles, about the angles created when parallel lines are cut by a transversal, and the angle-angle criterion for similarity of triangles).
- Format: studio. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Eight landing routes, eight predict rounds, six match docks, three floor-pattern yards. Extra: Call the route (a route plays on the projector; the class calls out the rules). tool.json `modes: ["Dock", "Call the route"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 8.G.1 | Move the tile; measure before and after | lengths, angles, parallels unchanged | 2 |
| 8.G.3 | Predict a corner; write the rule | (2, 5) to (-5, 2) | 2 |
| 8.G.2, 8.G.4 | Land tiles; decide congruent or similar | the route as the proof | 3 |
| 8.G.5 | Tile triangles; cross parallel tracks | three angles on a straight edge | 4 |

## Screens and modes
Header (kit): title "Transformation Dock"; `Dock`, `Call the route`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A harbor dock from above on a coordinate grid, stacked containers, an L-shaped tile hanging from a crane, a painted outline, and Kemi in the crane cab. The welcome is queued (`welcomeAfter: true`): "Set it down right on the outline. Tap a move to add it to the route." First hint: "Tap Slide, Flip, Turn or Resize."

**Route (focus: the dock).** At 1366x768 the grid fills the left with the route list and corner table right; at 680x425 the table is a tab. Each move asks its numbers (slide amounts, flip line, turn angle and center, resize factor and center). `Play` runs the route; corners update. A ruler and protractor measure any side or angle before and after.

**Predict.** Before a move plays, the child types where a marked corner goes and the rule in (x, y) form.

**Match.** Six docks, each with an outline. The child builds a route, then labels the pair "congruent" or "similar" and taps `Replay` to show the proof.

**Floor pattern.** Copies of a triangle tile the yard; the child marks three angles meeting on a line. A crane rail crosses two parallel tracks; the child marks equal angles. A resized triangle is checked angle by angle.

**A route is a reason (the aha).** Kemi: "Slides, flips and turns keep it the same size. A resize keeps only the shape. Your route proves it."

**The end.** The dock log of routes. `Print` prints it.

**Call the route (extra).** Projector play.

## Content
- Tiles and outlines with lattice corners, all readable with `Read`.
- Dock sounds are original; no music.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Moves can be reordered, edited or deleted until `Set it down`.
- Keyboard: Tab to move buttons, the route list (arrows reorder), number boxes, Play, the ruler and protractor, and the corner table; Enter adds or plays.
- With Motion off the tile jumps to each step.

## Look
- Accent `--brand` #0e6470 harbor teal (header, the crane, buttons); gold #f4c542 (the tile in hand, the outline when matched); paper #ebf5f6; ink #03191d; muted #4a5759.
- Contrast (WCAG 2.1, computed): white on brand 6.83:1; brand on paper 6.15:1; ink on paper 16.30:1; muted on paper 6.76:1; ink on gold 11.12:1.
- Never color alone: matched outlines show "landed"; congruent and similar carry their words.
- Different from this batch (puzzle plum, glacier blue, timber olive, cranberry).

## Art
- People (illustrated): Kemi, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the harbor dock from above (1, 16:9), the crane cab (1, 4:3).
- Drawn in code: the grid, tiles, outlines, routes and angle marks.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as Kemi; `bright-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.move + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `move`: "Tap a move, then type its numbers."
- how `play`: "Tap Play."
- how `predict`: "Type where the corner lands."
- how `label`: "Tap Congruent or Similar."
- how `angles`: "Tap the three angles that meet."
- event, whole, a route is a reason.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
transformations (`kit/transformations.js`), as described in rigid-motion-twins' spec. Uses `Motion.translate`, `.rotate`, `.reflect`, `.dilate`, `then` to compose, `fnText` for rules, `isRigid`, `classify` and `matches`. Tool-only code: the crane and route list, predict checks, the floor tiler and angle marks.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Landing | Add moves at random | The route must land exactly; the predict boxes are checked first. |
| Match | Call every pair congruent | Docks with a resize catch it, checked by `isRigid`. |
| Angles | Tap any three | They must meet at one point on a straight edge. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `move`; `play`.
2. `predict`.
3. `label`; `angles`.
4. A route is a reason (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 8.G.1 to 8.G.5 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Congruence and similarity defined by transformations | Common Core Standards Writing Team (2016), "Progressions for the CCSS, Geometry, 7-8" | Wu (2013), "Teaching Geometry According to the Common Core Standards", University of California, Berkeley | yes |
| Tiled triangles show the angle sum | Common Core Standards Writing Team (2016), "Progressions for the CCSS, Geometry, 7-8" | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", grades 6-8 geometry | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s21, 2026-11-10): (2, 5) turns to (-5, 2), flips over the y-axis to (-2, 5), slides by (3, -2) to (5, 3), and resizes by 2 to (4, 10); 50 + 60 + 70 = 180; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 grid, route and table; at 680x425 table as a tab.
2. Eight routes land with measures kept, and corners are predicted with rules. (8.G.1, 8.G.3)
3. Six docks are labeled congruent or similar with a replayed route. (8.G.2, 8.G.4)
4. Three floor yards show the angle sum, parallel-line angles and angle-angle similarity. (8.G.5)
5. Uses the transformations engine unchanged.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the tile jumps; no network requests.

## Open questions
None.
