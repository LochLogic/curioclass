# Garden Grid

## One idea
On an empty lot the neighborhood garden club (made up, labeled "illustration") asks the child to plan the garden in three kinds of jobs: shape orders, where the child drags corner posts to build beds from clues ("five sides", "four sides and four square corners", "a triangle") and a cube compost bin unfolds to show its six equal faces; plot grids, where the child drags row and column lines across a rectangle bed to make same-size square plots and counts them (3 rows of 5 is 15 plots); and fair shares, where identical beds get split into halves, thirds and fourths for two, three or four gardeners, and one bed split into two triangles and another into two rectangles are both called halves; at the end the club agrees that equal shares of the same bed can look different and still be fair, and the lot fills with plants, so a second grader learns to recognize and draw shapes with given attributes (triangles, quadrilaterals, pentagons, hexagons, cubes), to split a rectangle into rows and columns of same-size squares and count them, and to split circles and rectangles into two, three or four equal shares, seeing that equal shares of identical wholes need not have the same shape.

## Not like
- pizza-party (1, spec): halves and fourths only. Here thirds, plus shapes and plot grids.
- tile-the-floor (3, spec): area and multiplication. Here counting square plots.
- egg-carton-factory (4, spec): rows and columns for factors. Here first rows and columns.
- picky-robot-shapes (1, spec): defining features at a gate. Here building shapes from clues.

## Who and how
- Grade 2, Math, module "Shapes and Equal Shares". Standards: 2.G.1 (recognize and draw shapes having specified attributes, such as a given number of angles or a given number of equal faces; identify triangles, quadrilaterals, pentagons, hexagons, and cubes), 2.G.2 (partition a rectangle into rows and columns of same-size squares and count to find the total number of them), 2.G.3 (partition circles and rectangles into two, three, or four equal shares, describe the shares using the words halves, thirds, half of, a third of, etc., and describe the whole as two halves, three thirds, four fourths; recognize that equal shares of identical wholes need not have the same shape).
- Format: builder. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Eight shape orders, the cube bin, six plot grids, nine fair-share beds (round and rectangle), the finale. Extra: Seasons (the planted garden grows from spring to fall). tool.json `modes: ["Lot", "Seasons"]`, `minutes: "15-25"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 2.G.1 | Build beds from clues; unfold the cube bin | corner counts; six equal faces | 2 |
| 2.G.2 | Drag row and column lines; count plots | same-size squares; the count | 3 |
| 2.G.3 | Split beds into halves, thirds and fourths | equal shares, different shapes | 4 |

## Screens and modes
Header (kit): title "Garden Grid"; `Lot`, `Seasons`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** An empty city lot with a fence, a shed and a clipboard of orders. Mr. Diaz, the club leader, holds a seed packet. The welcome is queued (`welcomeAfter: true`): "Welcome to the garden club! Mr. Diaz wants a bed with five sides. Drag corner posts to build it." First hint: "Drag a corner post onto the lot."

**Shape orders (focus: the lot).** At 1366x768 the lot fills the screen with orders at the left; at 680x425 orders are a card above the lot. Posts snap to a light grid; a rope joins them. The bed counts its sides and corners aloud and checks the clue. The cube compost bin unfolds into six squares and folds back.

**Plot grids.** A rectangle bed. The child drags row lines and column lines; the plots must be same-size squares. "3 rows of 5. How many plots?" The child counts (plots number as tapped) and taps the total.

**Fair shares.** A round bed and rectangle beds. The child draws lines to share among 2, 3 or 4 gardeners. Each share shows its size bar. Thirds are new: "Three gardeners, three equal shares, each a third."

**Different shapes, still fair (the aha).** Two identical beds: one split into two triangles, one into two rectangles. The club votes: both are halves. Mr. Diaz: "Same bed, same amount, different shapes. Still fair!"

**The end.** The planted garden with every bed labeled. `Print` prints the plan.

**Seasons (extra).** The garden grows through the seasons.

## Content
- Eight shape clues (triangle, quadrilateral, pentagon, hexagon, four square corners), the cube bin, six grids, nine shares, five club members from different families labeled "illustration", all spoken.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Posts and lines can be dragged off at any time.
- Keyboard: Tab to posts, grid points, lines and answers; arrows move a post; Enter places.
- With Motion off the cube shows unfolded and folded side by side and plants appear grown.

## Look
- Accent `--brand` #2f6a3a garden green (header, ropes, buttons); gold #f4c542 (the post in hand, equal shares); paper #eff7f1; ink #0c1f12; muted #485a4d.
- Contrast (WCAG 2.1, computed): white on brand 6.47:1; brand on paper 5.93:1; ink on paper 15.77:1; muted on paper 6.76:1; ink on gold 10.58:1.
- Never color alone: shares carry names and size bars.
- Different from this batch (cafeteria brick, mystery violet, terracotta brown, lake teal).

## Art
- People (illustrated): five garden club members, labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Local FLUX (`scripts/localart.py`): the empty lot (1, 16:9), the planted garden in two seasons (2, 16:9), plant icons (4, 1:1).
- Drawn in code: posts, ropes, grids, shares, the cube.
About 12 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as Mr. Diaz; `upbeat-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.job + ':' + state.bed + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `post`: "Drag a corner post onto the lot."
- how `grid`: "Drag a line across the bed."
- how `count`: "Tap the plots to count, then tap the total."
- how `share`: "Draw a line to share the bed."
- event, whole, each order checked (short).
- event, whole, different shapes, still fair.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: posts and ropes on a grid, side and corner checks, row and column lines, share areas. Orders sit in a marked block `/* GARDEN-GRID DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Shape | Drop many posts | The bed must match the clue's sides and corners. |
| Grid | Draw uneven lines | Plots must be same-size squares to count. |
| Share | Draw any line | Only equal shares pass; size bars show the difference. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `post`.
2. `grid`; `count`.
3. `share`.
4. Still fair (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 2.G.1, 2.G.2, 2.G.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Partitioning rectangles into rows and columns prepares area and multiplication | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | Battista and others (1998), "Students' spatial structuring of 2D arrays of squares", Journal for Research in Mathematics Education | yes |
| Equal shares of identical wholes need not be the same shape | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r10, 2026-11-10): 3 rows of 5 make 15 plots and 4 rows of 4 make 16; a cube has 6 faces; two halves, three thirds and four fourths each make one whole; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 lot and orders; at 680x425 card above lot.
2. Eight beds match their clues and the cube shows six faces. (2.G.1)
3. Six beds are split into rows and columns and counted. (2.G.2)
4. Nine beds are shared in halves, thirds and fourths, including two different-shape halves. (2.G.3)
5. Every card is spoken; every control is 56 px or more.
6. Club members are labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still views; no network requests.

## Open questions
- The idea card flags overlap with prime-garden, now egg-carton-factory (default used: this tool counts square plots in grade 2; egg-carton-factory keeps rows and columns for factors in grade 4).
