# Leaf Sorter AI

## One idea
Flip four switches to decide which clues a leaf-sorting AI may look at (color, edge, shape, size), and watch the studied leaves spread out or bunch up on a clue map: color sorts the 24 schoolyard leaves perfectly and then fails on new leaves from the park two weeks later, while edge and shape together sort every new leaf right.

## Not like
- biased-bot (same family, grade 4): the lever there is whose examples the robot learned from. Here the examples never change; the lever is which clues the model may use.
- teach-the-robot (same family, grade 2): more examples make Kip better. Here the leaf set is fixed, and adding a clue can make the sorter worse.
- model-mechanic (same family, 6-8): reads a confusion matrix to fix data and settings. Here the main view is the clue map (two clues as axes), and the only setting is the clue switches.
- data-table-builder (grade 4): collect and chart data to answer a question. Here the chart is the model's own view of the data.
- kitchen-lab and the fruit version this tool replaced: no food; leaves from four real trees.

## Who and how
- Grade 5, computer science. Module: Train a Classifier (Algorithms and Programming). Topic line: "train and test a classifier".
- Driver: students (pairs on laptops), or a teacher on a projector asking which switches to try next. 15 to 30 minutes.
- Standards: E5-ALG-ML-02 (module code). CSTA 2017 crosswalk: 1B-DA-06 (organize and present data visually to highlight relationships), 1B-DA-07 (use data to predict outcomes). Reference: AI4K12 Big Idea 3 (learning: features and training data).
- Science link for the teacher: leaf traits used to identify trees.
- tool.json: driver "students or teacher", minutes "15-30", modes ["Sorter Lab", "Leaf Maker"], grades_label "Grade 5".

## Screens and modes
Kit frame. Header: title "Leaf Sorter AI" with small line "Which clues should it use?", mode buttons "Sorter Lab" (magnifier icon) and "Leaf Maker" (leaf icon), Motion, Sound, Read.

### Mode 1: Sorter Lab (opens first)
Stage, left to right on wide screens, stacked on narrow:
- The specimen sheet: the 24 studied leaves as pressed specimens on herbarium paper, four labeled rows (Sugar maple, Red oak, Paper birch, Sweetgum), each leaf drawn from its values with a tiny tag. Tap a leaf to open its scan card: the leaf large, its four clue meters (Color, Edge, Shape, Size) with words ("green to red", "smooth to toothy", "lobes: 9", "length: 21.2 cm").
- The clue map (engine `scatter`): two of the switched-on clues as the axes; each studied leaf a point with its tree's glyph and color. Axis pickers "Across" and "Up" list only switched-on clues. With one clue on, the map is a strip (one axis). With none on, the map says "Switch on a clue".
Panel:
- `#hint`.
- "The sorter may look at:" four switches with icons: Color (paint drop), Edge (saw teeth), Shape (lobed leaf), Size (ruler). All off at start.
- Scores: "Studied leaves: 24 of 24" and "New leaves: tap Field test" (shown as "-" until a field test runs).
- "Field test" (pin icon, `.big-btn`): the 16 park leaves fall onto the map one by one, each guessed (engine `knn`, k = 3, the switched-on clues); four sorting bins below the map fill, each bin labeled by tree, a wrong leaf marked with an X badge and its real tree name.
- Lab notebook: a table that adds a row per field test: clues used (icons), studied score, new score. Up to 15 rows, newest on top; "Clear notebook".
- "Start over" (circular arrow): switches off, map empty, notebook cleared.

### Mode 2: Leaf Maker
Stage: one big leaf drawn live; under it, the guess and the three studied leaves it was closest to (small specimens with their tree names), using the clues switched on in Sorter Lab.
Panel: four sliders: Lobes (0 to 11), Teeth (smooth to toothy), Length (4 to 24 cm), Color (green, yellow, orange, red). "Random leaf" (dice icon). A line "The sorter is using: Edge, Shape" with a "Change clues" link back to Sorter Lab.

## Content
Trees (shape = lobes / 11; edge 0 smooth to 1 fine teeth; size = (length cm - 4) / 20; color 0 green, 0.33 yellow, 0.67 orange, 1 red or purple):
| Tree | Lobes | Edge | Length (cm) | Studied color (schoolyard, one week) | New color (park, two weeks later) |
|---|---|---|---|---|---|
| Sugar maple | 3 to 5 | 0.10 to 0.30 | 8 to 15 | 0.85 to 1 (red) | 0.30 to 1 (yellow to red) |
| Red oak | 7 to 11 | 0.05 to 0.20 | 12 to 22 | 0 to 0.15 (still green) | 0 to 1 (green to red-brown) |
| Paper birch | 0 | 0.75 to 0.95 | 5 to 10 | 0.28 to 0.40 (yellow) | 0.20 to 0.45 (yellow-green to yellow) |
| Sweetgum | 5 to 7 | 0.55 to 0.75 | 10 to 18 | 0.60 to 0.72 (orange) | 0 to 1 (green to purple) |
On-screen tree notes (scan card footer): Sugar maple "3 to 5 lobes, few big teeth"; Red oak "7 to 11 pointed lobes with bristle tips"; Paper birch "no lobes, double-toothed edge"; Sweetgum "a star of 5 to 7 lobes, finely toothed edge".
Generation (engine `rng`): studied leaves seed 501, 6 rounds; new leaves seed 502, 4 rounds; each round makes one leaf of each tree in the order maple, oak, birch, sweetgum. Per leaf, in this order: lobes = round(uni(R, low - 0.49, high + 0.49)); edge = uni(R, edge range); length = uni(R, length range); color = uni(R, color range for that set). Store edge and color rounded to 2 decimals, shape = round(lobes / 11, 2), size = round((length - 4) / 20, 2) from the unrounded length; show length rounded to 0.1 cm.
Checked scores (studied of 24, new of 16), k = 3:
| Clues on | Studied | New | | Clues on | Studied | New |
|---|---|---|---|---|---|---|
| Color | 24 | 7 | | Edge + Shape | 24 | 16 |
| Edge | 22 | 12 | | Edge + Size | 23 | 16 |
| Shape | 22 | 15 | | Color + Shape | 24 | 8 |
| Size | 21 | 10 | | Color + Edge + Shape | 24 | 11 |
| Color + Edge | 24 | 10 | | All four | 24 | 12 |
| Color + Size | 24 | 8 | | Edge + Shape + Size | 24 | 16 |
| Shape + Size | 23 | 15 | | Color + Shape + Size | 24 | 8 |
| Color + Edge + Size | 24 | 11 | | | | |
New-leaf detail: Color alone gets 0 of 4 red oaks (green in the schoolyard, red-brown in the park). Shape alone mixes up a 5-lobed sweetgum with maple. Edge alone mixes up maples and oaks. Edge + Shape gets all 16.
Talk points on screen after the second field test (a tip card, `.tip`): "A clue can look perfect on the leaves it studied and still fail on new ones." After a 16 of 16 run: "Edge and shape belong to the tree. Color depends on the week."

## Interactions in detail
- Switching a clue retrains at once (kNN only stores leaves); the studied score updates, the map re-plots, and the new-leaf score greys out with "Run Field test again". Notebook rows are never changed.
- Studied score: each studied leaf is guessed by its 3 nearest studied leaves, itself included, so it is easy to look perfect; the tip card says so after the first field test where studied beats new by 5 or more.
- Field test: 0.35 s per leaf (about 6 s); "Skip" finishes at once. Motion off: leaves appear in their bins without falling, same pace.
- Tap any point on the map or leaf on the sheet: its scan card, and (for a new leaf after a field test) lines to its three nearest studied leaves on the map.
- Axis pickers default to the first two switched-on clues in the order Color, Edge, Shape, Size, and keep the student's choice while those clues stay on.
- Leaf Maker: sliders redraw the leaf live and re-guess within 50 ms; with no clues on, the guess reads "Switch on a clue in Sorter Lab" with that link.
- Keyboard: switches and sliders in the panel come before map points; arrow keys move between map points (nearest in that direction); Enter opens the scan card. Visible focus.
- Sizes: switches, Field test and both scores visible without scrolling at every STANDARDS.md size; at 680x425 the specimen sheet folds into a "Leaves" tab beside the map. Map labels at least 10 px.
- Nothing is saved; the notebook lasts for the page load.

## Look
- Accent `--brand #34427a` (indigo ink). Own `:root`: herbarium paper `--paper #f5f1e6`, `--ink #23261f`, `--muted #5d6255`, `--line #ddd5c2`, `--brand #34427a` (indigo ink; header and switches on), `--focus #c2410c`.
- Leaves are data colored: color value 0 #4f8a3a, 0.33 #e0b52c, 0.67 #e07a2a, 1 #a8243a, linear blend between; veins #3d3a2a at 40 percent.
- Tree glyphs on the map and bins (shape plus color): Sugar maple circle #b03a2e, Red oak square #7a5f12, Paper birch triangle #276b78, Sweetgum diamond #6c3fa0.
- Neighbors: code-tracer rust, game-remix teal, decision-tree olive, loop-garden green. Indigo ink on cream keeps the leaves the only bright colors.
- Contrast: white on #34427a 9.52:1; ink on paper 13.60:1; muted on paper 5.56:1; brand on paper 8.43:1; focus on paper 4.59:1; glyph colors on paper 5.33, 5.36, 5.38, 6.51:1. All pass AA.

## Art
none: drawn in code. Each leaf is one parametric SVG: an outline with `lobes` points around a midrib (0 lobes gives an oval), teeth along the edge spaced by `edge`, length by `size`, fill by `color`, plus a stem and veins. Herbarium paper is a CSS gradient with faint fibers. preview.svg: the clue map with edge across and shape up, four clean clusters, and two pressed leaves beside it.

## Voice
Bank voice `gravel-ranger`, style "Say warmly with a gravelly voice, like an old park ranger telling stories". A field guide feel for a nature lab; not used by neighbors (code-tracer clear-teacher, game-remix big-sister, score-keeper friendly-dad) or group siblings.
1. how, welcome Sorter Lab: "These leaves came from four kinds of trees. Switch on a clue the sorter may look at."
2. how, after the first switch: "See how the leaves spread out on the map. Then press Field test to try new leaves."
3. event, after each field test: "The sorter got N of 16 new leaves right." (sixteen fixed numbers plus zero, recorded as seventeen lines)
4. event, when studied minus new is 5 or more: "It did great on leaves it studied, and not on new ones. That clue fooled it."
5. event, first 16 of 16: "Every new leaf sorted right. Those clues belong to the tree itself."
6. how, first time Color is on with another clue that scored 16 before: "Watch what happens to the new leaves when you add color."
7. how, welcome Leaf Maker: "Slide to build a leaf. The sorter will guess its tree."
8. event: "That looks like a sugar maple." "a red oak." "a paper birch." "a sweetgum." (four lines; stale when a slider moves)
Read speaks the hint. Leaf Maker guesses are spoken only when the student pauses 1 s on a slider (drop older ones).

## Family engine
ml-lab (`kit/ml-lab.js`, full description in tools/teach-the-robot/spec.md). Uses `rng` and `uni` for both leaf sets, `knn` (k = 3, features = the switched-on subset of color, edge, shape, size), `evaluate` for studied and new scores and the per-tree bins, and the `scatter` view (tree glyphs, query lines for a picked new leaf). The leaf drawing stays in this tool.

## Sources
- Lobes, edges and leaf sizes: Virginia Tech Dendrology fact sheets for sugar maple (Acer saccharum), northern red oak (Quercus rubra), paper birch (Betula papyrifera) and sweetgum (Liquidambar styraciflua): https://dendro.cnre.vt.edu/dendrology/factsheets.cfm ; Burns and Honkala, Silvics of North America, Vol. 2 Hardwoods, USDA Agriculture Handbook 654 (1990).
- Fall colors (sugar maple yellow to red, red oak red to brown, paper birch yellow, sweetgum yellow to purple): the same fact sheets; USDA Forest Service, "Why Leaves Change Color": https://www.fs.usda.gov/visit/fall-colors/science-of-fall-colors
- Features, training and test sets: AI4K12 Big Idea 3: https://ai4k12.org ; scikit-learn "Nearest Neighbors": https://scikit-learn.org/stable/modules/neighbors.html
- CSTA K-12 Computer Science Standards (2017): https://csteachers.org/k12standards/
- The leaf values are generated from the ranges above (rounded from the sources); the scores table was computed with the engine.
- Verify agent: check each length range against the fact sheets and adjust the table and scores together if one is off.

## Done when
1. With all clues off, Field test is disabled and the map asks for a clue.
2. Color alone: studied 24, new 7, with all four red oaks wrong; line 4 plays.
3. Edge + Shape: studied 24, new 16; line 5 plays; the map shows four separate clusters.
4. All four clues: new 12; the notebook keeps every earlier row unchanged.
5. Every score in the Content table matches when that clue set is run.
6. Tapping a new leaf after a field test draws lines to its three nearest studied leaves, and they match the guess.
7. Leaf Maker with Edge + Shape: 0 lobes and toothy gives paper birch; 9 lobes and smooth gives red oak.
8. Trees are told apart by glyph shape with color off; switches, Field test and scores are on screen without scrolling at 680x425, 1366x768 and 375 wide.
