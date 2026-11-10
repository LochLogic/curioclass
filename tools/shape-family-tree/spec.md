# Shape Family Tree

## One idea
At a family reunion picnic a tree banner hangs over the tables (Quadrilaterals at the top, then Rhombuses and Rectangles, with Squares where those two branches meet), every guest is a four-sided shape, and the child seats each guest on the tree, testing it first with a checker that measures sides and corners; some guests fit two branches, so the square gets a seat where Rhombuses and Rectangles meet; argument cards come up from the family ("Grandma Quad says a square isn't a rectangle"), and the child settles each one by picking the evidence (four sides, four square corners, so a square is a rectangle too); in the outsiders round the child draws a four-sided shape on a dot grid that is not a rhombus, rectangle or square (a kite, a lopsided shape) and it gets its own seat on the main branch; at the end the family photo shows that names describe what shapes share, so one shape can have several names, so a third grader learns that shapes in different categories can share attributes that define a larger category, to recognize rhombuses, rectangles and squares as examples of quadrilaterals, and to draw quadrilaterals that do not belong to any of these subcategories.

## Not like
- shape-spy (K, spec): naming shapes in scenes. Here categories that overlap.
- garden-grid (2, spec): building shapes from clues. Here sorting by shared features.
- shape-sieve (5, concept): the full shape hierarchy argued in grade 5. Here grade 3 categories only.
- picky-robot-shapes (1, spec): defining features at a gate. Here one shape with several names.

## Who and how
- Grade 3, Math, module "Quadrilaterals". Standards: 3.G.1 (understand that shapes in different categories (e.g., rhombuses, rectangles, and others) may share attributes (e.g., having four sides), and that the shared attributes can define a larger category (e.g., quadrilaterals); recognize rhombuses, rectangles, and squares as examples of quadrilaterals, and draw examples of quadrilaterals that do not belong to any of these subcategories).
- Format: sort. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Eighteen shape guests in many sizes and turns, the checker, six argument cards, the dot grid for outsiders, the family photo. Extra: Debate (a class prompt with two sides and evidence cards). tool.json `modes: ["Picnic", "Debate"]`, `minutes: "15-25"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3.G.1 (shared attributes) | Test guests with the checker; seat them | side and corner readings; the tree | 2 |
| 3.G.1 (examples of quadrilaterals) | Settle argument cards with evidence | the square on two branches | 3 |
| 3.G.1 (outsiders) | Draw a quadrilateral that fits no subgroup | its seat on the main branch | 4 |

## Screens and modes
Header (kit): title "Shape Family Tree"; `Picnic`, `Debate`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A park picnic with long tables, balloons and a big tree banner. Shape guests mill around with name tags hidden. Grandma Quad, a cheerful quadrilateral with glasses, waves. The welcome is queued (`welcomeAfter: true`): "Welcome to the family reunion! Every guest has four sides. Seat each one on the tree. Drag a guest to the checker first." First hint: "Drag a guest to the checker."

**Checking and seating (focus: the tree).** At 1366x768 the tree fills the middle with guests along the bottom and the checker at the left; at 680x425 the checker is a pop-up. The checker shows each side's length (equal sides get matching tick marks) and each corner (square corners get a small square). The child drags the guest to a branch. A wrong seat: "This guest has no square corners. Check again."

**Two branches.** A square tries the Rectangles branch and the Rhombuses branch; both accept it, and it slides to the seat where they meet.

**Argument cards.** "Grandma Quad says a square isn't a rectangle." The child picks evidence cards (four sides, four square corners, all sides equal, opposite sides equal) to settle it.

**Outsiders.** A dot grid: "Draw a four-sided shape that isn't a rhombus, rectangle or square." The child taps four dots; the checker tests it; it gets its own seat on the main Quadrilaterals branch.

**One shape, many names (the aha).** The square's name tag flips: Square, Rectangle, Rhombus, Quadrilateral. Grandma Quad: "Names tell what shapes share. One shape can have several names!"

**The end.** The family photo on the tree. `Print` prints it.

**Debate (extra).** Two sides of an argument with evidence cards for a class talk.

## Content
- Rhombuses, rectangles, squares and other quadrilaterals in many sizes and turns, six arguments, the dot grid, all readable with `Read`. Trapezoids are left out on purpose (definitions differ). Arguments are friendly family talk.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Guests can be moved between seats at any time.
- Keyboard: Tab to guests, the checker, branches, evidence cards and dots; Enter seats or picks.
- With Motion off name tags show all names at once instead of flipping.

## Look
- Accent `--brand` #a02c2c picnic red (header, the banner, buttons); gold #f4c542 (the guest in hand, the shared seat); paper #fcf0f0; ink #2a0909; muted #5e4c4c.
- Contrast (WCAG 2.1, computed): white on brand 7.26:1; brand on paper 6.52:1; ink on paper 16.52:1; muted on paper 7.22:1; ink on gold 11.31:1.
- Never color alone: equal sides carry tick marks; square corners carry small squares.
- Different from this batch (penguin navy, mural magenta, backyard green, newsletter teal).

## Art
- Local FLUX (`scripts/localart.py`): the picnic park (1, 16:9), the tree banner (1, 4:3).
- Drawn in code: every shape guest with faces, the checker, the dot grid, evidence cards.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as Grandma Quad; `big-sister` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.guest + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `check`: "Drag a guest to the checker."
- how `seat`: "Drag the guest to its branch."
- how `argue`: "Tap the evidence cards that settle it."
- how `draw`: "Tap four dots to draw a shape."
- event, whole, two branches.
- event, whole, one shape, many names.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the checker (equal sides, square corners, parallel sides), the tree with shared seats, the dot grid. Guests sit in a marked block `/* SHAPE-FAMILY DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Seat | Seat by look | Tilted squares and long thin rhombuses don't look like their branch; the checker decides. |
| Argument | Pick every card | Only true evidence settles it; a wrong card is explained. |
| Outsider | Draw a rectangle | The checker seats it on Rectangles and asks again. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `check`; `seat`.
2. Two branches (whole), waits.
3. `argue`.
4. `draw`. Many names (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 3.G.1 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Children often reject a square as a rectangle; reasoning from properties fixes it | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | Clements and Battista (1992), "Geometry and spatial reasoning", in Handbook of Research on Mathematics Teaching and Learning | yes |
| Trapezoid definitions differ (inclusive and exclusive), so grade 3 tools can leave it out | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | Usiskin and Griffin (2008), "The Classification of Quadrilaterals: A Study of Definition" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r11, 2026-11-10): a square passes both the rectangle test (four square corners) and the rhombus test (four equal sides); a kite passes neither; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 tree, guests and checker; at 680x425 checker pop-up.
2. Eighteen guests are checked and seated. (3.G.1)
3. Six arguments are settled with evidence; the square sits on two branches. (3.G.1)
4. An outsider quadrilateral is drawn and seated. (3.G.1)
5. `Read` reads every card; every control is 48 px or more.
6. Trapezoids are left out; arguments stay friendly.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: names shown together; no network requests.

## Open questions
- The idea card flags overlap with shape-courtroom, now shape-sieve (default used: this tool keeps the grade 3 categories; the full hierarchy argument stays in grade 5).
- The idea card moves 3.G.2 out (default used: it goes to tile-the-floor's painters' job; this tool teaches 3.G.1 only).
