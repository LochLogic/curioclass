# Clay Cutting Bench

## One idea
At a pottery studio's cutting bench the potter, Mrs. Halvorsen (made up, labeled "illustration"), sets out blocks of clay shaped as right rectangular prisms and right rectangular pyramids and a taut cutting wire, and before every slice the child must sketch or pick the shape of the cut face; then the wire passes through, the two halves pull apart, and the face is compared with the prediction; parallel cuts come first (a 6 by 4 by 3 block cut parallel to its base shows a 6 by 4 rectangle, parallel to an end a 4 by 3 rectangle; a pyramid with a 6 by 6 base and height 8 cut parallel to the base halfway up shows a 3 by 3 square); then the wire tilts (a cut through two opposite edges of the block shows a 6 by 5 rectangle, longer than either face beside it; a cut slicing off a corner shows a triangle; a slanted cut through a pyramid shows a trapezoid; a vertical cut through the apex shows a triangle); challenge rounds ask for a cut that makes a given shape (can a prism give a triangle? a pentagon? a hexagon?), and the child places the wire to make it or explains why it cannot; at the end the child can predict the face of any flat cut through these solids, so a seventh grader learns to describe the two-dimensional figures that result from slicing right rectangular prisms and right rectangular pyramids.

## Not like
- slice-and-stack (10, spec): cross sections to build volume formulas. Here naming the cut face only.
- net-folder (6, spec): unfolding solids into nets. Here cutting through them.
- blueprint-studio (7, concept): scale drawings. Here plane sections at true size.
- big-wheel-small-wheel (7, concept): circles. Here flat-faced solids.

## Who and how
- Grade 7, Math, module "Cross Sections of Solids". Standards: 7.G.3 (describe the two-dimensional figures that result from slicing three-dimensional figures, as in plane sections of right rectangular prisms and right rectangular pyramids).
- Format: lab. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three prisms and two pyramids of clay, twelve predict-and-cut rounds, six challenge rounds, the face gallery. Extra: Class guess (the class votes on each face before the cut on the projector). tool.json `modes: ["Studio", "Class guess"]`, `minutes: "20-30"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.G.3 (parallel cuts) | Predict, then cut parallel to a face | rectangles and smaller squares | 2 |
| 7.G.3 (slanted and corner cuts) | Predict, then tilt the wire | a longer rectangle, a triangle, a trapezoid | 3 |
| 7.G.3 (describe) | Place a cut to make a named shape, or explain why not | the face gallery | 4 |

## Screens and modes
Header (kit): title "Clay Cutting Bench"; `Studio`, `Class guess`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A pottery studio bench, a block of gray clay, a wire cutter on two handles, and Mrs. Halvorsen with clay on her apron. The welcome is queued (`welcomeAfter: true`): "If the wire cuts here, flat across, what shape is the face? Pick a shape card." First hint: "Pick a shape card."

**Predict and cut (focus: the clay).** At 1366x768 the 3D clay fills the left with shape cards and the face gallery right; at 680x425 the gallery is a tab. The child turns the clay (drag or arrows), positions the wire (slide and tilt handles), picks a shape card, then taps `Cut`. The halves pull apart and the face turns toward the child with its side lengths. A match adds the face to the gallery; a miss shows the predicted shape outlined over the real one.

**Tilted cuts.** The tilt handle angles the wire. A cut through two opposite edges shows the 6 by 5 rectangle, and a side card shows where the 5 comes from (the diagonal of the 4 by 3 end) for those curious, not required. A corner cut shows a triangle; slanted pyramid cuts show trapezoids.

**Challenges.** "Make a triangle from the prism." "Make a pentagon." "Make a hexagon." "Make a triangle from the pyramid without cutting through its tip." "Make a pentagon from the pyramid." "Make a hexagon from the pyramid." The child sets the wire and cuts, or taps `Can't be done` and picks a reason.

**Any cut (the aha).** Mrs. Halvorsen: "Count the faces the wire crosses. That's how many sides the cut face has."

**The end.** The face gallery. `Print` prints it.

**Class guess (extra).** The class votes before each cut.

## Content
- Prisms 6 by 4 by 3, 5 by 5 by 5 and 8 by 2 by 2; pyramids with a 6 by 6 base (height 8) and a 6 by 4 base (height 6); all measures in centimeters, readable with `Read`.
- Faces are named by shape and side count; lengths are shown when they are whole.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The wire can be moved until `Cut`; `Reset` rejoins the clay.
- Keyboard: Tab to the clay (arrows turn it), the slide handle, the tilt handle (arrows move by 5 degrees), shape cards, Cut and Reset; Enter cuts.
- With Motion off the halves appear apart at once.

## Look
- Accent `--brand` #87401f clay sienna (header, the wire, buttons); gold #f4c542 (the shape card in hand, the cut face's outline); paper #f9f1eb; ink #2a1206; muted #5c524b.
- Contrast (WCAG 2.1, computed): white on brand 7.54:1; brand on paper 6.76:1; ink on paper 15.84:1; muted on paper 6.81:1; ink on gold 10.87:1.
- Never color alone: faces carry their shape name and side count; misses show "predicted" and "actual" labels.
- Different from this batch (beaker violet, asphalt slate, bike-path blue, card-table green).

## Art
- People (illustrated): Mrs. Halvorsen, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the pottery studio (1, 16:9).
- Drawn in code: 3D clay with soft lighting, the wire and every cut face, because the cut must be exact.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as Mrs. Halvorsen; `knowing-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.solid + ':' + state.round + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `predict`: "Pick a shape card."
- how `place`: "Slide or tilt the wire."
- how `cut`: "Tap Cut."
- how `challenge`: "Set the wire, or tap Can't be done."
- event, whole, any cut.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: exact plane and solid intersection (a convex polygon from the edges the plane crosses), 3D view with lighting, the wire handles, the gallery.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predictions | Pick "rectangle" every time | Corner and pyramid cuts give triangles and trapezoids. |
| Challenges | Tap Can't be done | Most challenges can be done; only the pyramid hexagon cannot (a pyramid has five faces), and it needs that reason. |
| Cuts | Cut, then predict | The shape card must be picked before Cut turns on. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `predict`; `place`; `cut`.
2. Tilted cuts repeat the three.
3. `challenge`.
4. Any cut (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.G.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Plane sections of a cube or prism can be triangles, quadrilaterals, pentagons or hexagons | Common Core Standards Writing Team (2012), "Progressions for the CCSS, 7-8 Geometry" | Hilbert and Cohn-Vossen (1952), "Geometry and the Imagination", Chelsea | yes |
| Predicting before seeing builds spatial reasoning | Sarama and Clements (2009), "Early Childhood Mathematics Education Research", Routledge | National Research Council (2006), "Learning to Think Spatially", National Academies Press | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s18, 2026-11-10): the 4 by 3 end has a diagonal of 5, so the cut through opposite 6 cm edges is a 6 by 5 rectangle; halfway up a pyramid with a 6 by 6 base the section is 3 by 3; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 clay, cards and gallery; at 680x425 gallery as a tab.
2. Parallel cuts of prisms and pyramids are predicted and checked. (7.G.3)
3. Tilted and corner cuts are predicted and checked. (7.G.3)
4. Six challenges are made or explained as impossible. (7.G.3)
5. Every face shows its shape name and side count.
6. `Read` reads every card and the wire position; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: halves appear apart; no network requests.

## Open questions
- The idea card flags overlap with slice-and-stack (default used: this tool only predicts and names plane sections of prisms and pyramids; slice-and-stack keeps cross sections for volume).
