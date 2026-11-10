# Shape Sieve

## One idea
At the Shape Sieve works, a tall stack of sieves sorts shapes by their properties (a sieve for at least one pair of parallel sides, one for two pairs, one for four right angles, one for four equal sides, and for triangles, sieves for two equal sides, three equal sides and a right angle), and Ms. Okoye, the sieve keeper (made up, labeled "illustration"), hires the child to hear appeals from shapes who don't like where they landed; before each drop the child predicts where a shape will stop, then drops it and it falls until a sieve holds it back at the most specific name it earns (a square passes every quadrilateral sieve and lands in the square bin, under rectangle and rhombus); shapes appeal with near-miss claims ("I have right angles, so I can't be a rhombus!") and the child answers with the rulebook's definition; once "every square is a rectangle" is ruled, Ms. Okoye asks what else is true of every square without measuring, and the child lists the properties a square inherits from each sieve above it; triangles get their own stack (is an equilateral triangle isosceles? can a right triangle be isosceles?); each ruling pins a branch onto the hierarchy chart on the wall, and a final mystery shape described only by properties must be placed at the lowest branch it belongs to, so a fifth grader learns that properties of a category belong to all its subcategories, and to classify two-dimensional figures in a hierarchy based on properties.

## Not like
- shape-family-tree (3, spec): sorting quadrilaterals into families. Here triangles too, and inherited properties.
- courtroom-statistics (12, spec): a trial frame for p-values. Here a sieve keeper's appeals.
- quilt-block-studio (4, spec): naming lines and angles. Here using them to classify.
- picky-robot-shapes (1, spec): defining features of shapes. Here a hierarchy.

## Who and how
- Grade 5, Math, module "Classifying 2D Figures". Standards: 5.G.3 (understand that attributes belonging to a category of two-dimensional figures also belong to all subcategories of that category; for example, all rectangles have four right angles and squares are rectangles, so all squares have four right angles), 5.G.4 (classify two-dimensional figures in a hierarchy based on properties).
- Format: roleplay. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Two sieve stacks (quadrilaterals and triangles), sixteen shapes to drop, eight appeals, four inheritance rulings, the hierarchy chart, three mystery shapes, the rulebook. Extra: Jury (two students argue an appeal from opposite sides and the class rules). tool.json `modes: ["Sieve works", "Jury"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5.G.3 | List what a square inherits from each sieve above it | the inherited properties card | 2 |
| 5.G.4 (classify) | Predict and drop sixteen shapes; answer appeals | the shape stopping at its bin; the rulebook | 3 |
| 5.G.4 (hierarchy) | Pin branches; place mystery shapes at the lowest branch | the hierarchy chart | 4 |

## Screens and modes
Header (kit): title "Shape Sieve"; `Sieve works`, `Jury`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A workshop with a tall stack of labeled sieves, bins below, a chart on the wall, a square waiting at the top and Ms. Okoye with a clipboard. The welcome is queued (`welcomeAfter: true`): "Welcome to the Sieve works! Every shape falls until a sieve holds it back. Where will this square stop? Tap a bin to predict." First hint: "Tap a bin to predict."

**Drops (focus: the sieve stack).** At 1366x768 the stack fills the middle with the chart left and the rulebook right; at 680x425 the chart and rulebook are tabs. Each sieve tests one property; a shape that passes falls through and the sieve lights; the shape stops at the first sieve it can't pass, in the bin for the most specific name it earned. The child can measure sides and angles and test parallel sides before predicting.

**Appeals.** A shape objects: "I have right angles, so I can't be a rhombus!" The child picks the rule from the rulebook (a rhombus needs four equal sides, nothing about angles) and rules. Eight appeals, including a kite that wants to be a rhombus and a rectangle that refuses to be a parallelogram.

**Inheritance.** "Every square is a rectangle. What else is true of every square, without measuring?" The child drags properties from each sieve above the square bin onto the square's card.

**Triangles.** A second stack: two equal sides, three equal sides, a right angle. Rulings: an equilateral triangle is isosceles; a right triangle can be isosceles.

**The chart (the aha).** Each ruling pins a branch. Ms. Okoye: "Anything true of the big family is true of everyone inside it. The square got every property on its way down."

**Mystery shapes.** Shapes described only by properties are placed at their lowest branch.

**The end.** The finished chart. `Print` prints it.

**Jury (extra).** Two sides argue an appeal; the class rules.

## Content
- Sixteen shapes drawn with measurable sides and angles, eight appeals, the rulebook with inclusive definitions (a trapezoid has at least one pair of parallel sides) and a teacher note naming the other definition, all readable with `Read`.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Measure tools (ruler, angle checker, parallel tester) can be used before predicting.
- Keyboard: Tab to the shape, bins, measure tools, rulebook entries, property cards and chart branches; Enter drops or rules.
- With Motion off shapes appear in their bins with the passed sieves listed.

## Look
- Accent `--brand` #5a3e85 sieve purple (header, sieve frames, the chart); gold #f4c542 (the sieve that holds, the predicted bin); paper #f4f0fa; ink #1b1030; muted #585266.
- Contrast (WCAG 2.1, computed): white on brand 8.53:1; brand on paper 7.59:1; ink on paper 16.07:1; muted on paper 6.64:1; ink on gold 11.10:1.
- Never color alone: sieves carry their property in words; passed sieves carry a check.
- Different from this batch (greenhouse green, workshop copper, stadium blue, test-kitchen pink).

## Art
- People (illustrated): Ms. Okoye, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the sieve works (1, 16:9).
- Drawn in code: sieves, shapes with faces for appeals, measure tools, the chart.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as Ms. Okoye; `curious-librarian` as the shapes' appeals and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.stack + ':' + state.shape + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `predict`: "Tap a bin to predict."
- how `drop`: "Tap Drop."
- how `appeal`: "Pick the rule from the rulebook."
- how `inherit`: "Drag the properties onto the square's card."
- event, whole, the chart.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: property tests on exact coordinates (equal sides, right angles, parallel sides), the sieve stacks, the hierarchy chart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predictions | Always predict the top bin | The score counts right predictions, and most shapes fall further. |
| Appeals | Pick any rule | The rule must decide the shape's claim; wrong rules are shown not to apply. |
| Mystery | Place at the top branch | Only the lowest branch it belongs to counts. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `predict`; `drop`.
2. `appeal`.
3. `inherit`.
4. The chart (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 5.G.3, 5.G.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The inclusive trapezoid definition makes a parallelogram a trapezoid; textbooks differ | Common Core Standards Writing Team (2013), "Progressions for the CCSS, K-6 Geometry" | Usiskin and others (2008), "The Classification of Quadrilaterals: A Study of Definition", Information Age Publishing | yes |
| Students reason about classes better once they see properties inherited | Common Core Standards Writing Team (2013), "Progressions for the CCSS, K-6 Geometry" | Clements and Battista (1992), "Geometry and spatial reasoning", Handbook of Research on Mathematics Teaching and Learning | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s14, 2026-11-10): a square passes the four quadrilateral sieves, so it inherits four properties; an equilateral triangle passes the two-equal-sides sieve; a right triangle with legs 3 and 3 is isosceles; sixteen shapes and eight appeals; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 stack, chart and rulebook; at 680x425 tabs.
2. Inherited properties are listed for squares and three other shapes. (5.G.3)
3. Sixteen shapes are predicted and dropped; eight appeals are ruled. (5.G.4)
4. The hierarchy chart is built and three mystery shapes are placed at their lowest branch. (5.G.4)
5. The rulebook uses the inclusive trapezoid with a teacher note on the other definition.
6. Ms. Okoye is labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: shapes appear in bins; no network requests.

## Open questions
- The idea card asks for a trapezoid definition (default used: inclusive, at least one pair of parallel sides, so a parallelogram is a trapezoid, with a teacher note naming the exclusive definition).
