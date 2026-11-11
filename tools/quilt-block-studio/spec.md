# Quilt Block Studio

## One idea
At a community center quilting table, Auntie Mae (made up, labeled "illustration") hands the child a half-finished quilt block and a drafting kit with point, segment, ray and line tools, and the child drafts: tools snap and name what is drawn (segment AB, ray CD), guides glow gold when two lines are parallel or perpendicular, and each corner is tagged right, acute or obtuse as it forms; in mirror mode the child draws half a block, places a mirror line and the other half appears, then hunts for lines of symmetry by dragging a candidate line and folding to test, finding that some blocks have four, some have one and a pinwheel has none; a scrap bin of cut pieces gets sorted onto pattern labels by features (has a right angle, has parallel sides, is a right triangle), not by name alone; a flag hunt sets real flags side by side (Japan with two lines, Canada with one, Switzerland's square flag with four, and the United Kingdom's, which looks symmetric but isn't, because its diagonal red stripes are offset); every finished block gets a label naming its parallel and perpendicular lines, angle types and lines of symmetry, so a fourth grader learns to draw and name points, lines, segments, rays, angles and parallel and perpendicular lines, to classify shapes by those features, and to find and draw lines of symmetry.

## Not like
- skate-park-angles (4, spec): measuring angles in degrees. Here naming angle types and lines.
- shape-family-tree (3, spec): quadrilateral families. Here sorting by lines and angles.
- transformation-dock (8, concept): reflections as transformations on a plane. Here lines of symmetry in a figure.
- tile-the-floor (3, spec): covering area. Here drawing lines.

## Who and how
- Grade 4, Math, module "Lines, Angles and Symmetry". Standards: 4.G.1 (draw points, lines, line segments, rays, angles (right, acute, obtuse), and perpendicular and parallel lines; identify these in two-dimensional figures), 4.G.2 (classify two-dimensional figures based on the presence or absence of parallel or perpendicular lines, or the presence or absence of angles of a specified size; recognize right triangles as a category, and identify right triangles), 4.G.3 (recognize a line of symmetry for a two-dimensional figure as a line across the figure such that the figure can be folded along the line into matching parts; identify line-symmetric figures and draw lines of symmetry).
- Format: studio. Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Change note (spec fix, 2026-11-10): the studio, Auntie Mae, the mirror and the flags stay. Two things changed. In Drafting the kit no longer names what the child draws: the child drags the name tags on, and then finds each kind of line and angle in Auntie Mae's block. The Scrap bin was three "has a feature" labels where a wrong drop bounced back for free; it is now four rounds of yes-or-no bins (parallel sides, perpendicular sides, an obtuse angle, right triangle), the child marks the feature on the piece as proof, and a wrong drop goes to a mending pile that must be redone. Auntie Mae sorts the first piece of each round aloud as the model.
- The drafting kit, six drafting tasks with name tags, six find-it tasks, mirror mode, eight blocks to test, a scrap bin of twelve pieces sorted four ways, six flags, the block label. Extra: Class quilt (every student's block printed into one quilt, assembled on the device, nothing uploaded). tool.json `modes: ["Studio", "Class quilt"]`, `minutes: "25-35"`, `grades_label: "Grade 4"`.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.G.1 | draw points, lines, segments, rays, angles (right, acute, obtuse), perpendicular and parallel lines; identify these in figures | the student | Draft six tasks, drag the right name tag onto each thing drawn, then tap each kind in Auntie Mae's block | 6 drafting tasks and 6 find-it tasks | the child's drawing with blank tags; glows only after `Check` | 2, 3 |
| 4.G.2 | classify figures by the presence or absence of parallel or perpendicular lines, or of angles of a given size; recognize and identify right triangles | the student | Sort all twelve scraps four ways into yes and no bins, marking the sides or the corner that prove each yes | 48 placements over 4 rounds | the piece with the child's marks; the mending pile | 4 |
| 4.G.3 | recognize and draw lines of symmetry; identify line-symmetric figures | the student | Mirror half a block; drag a line and fold to test it on blocks and flags | 8 blocks and 6 flags | the fold matching or not | 5 |

## Screens and modes
Header (kit): title "Quilt Block Studio"; `Studio`, `Class quilt`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A quilting table, fabric scraps, Auntie Mae with a pincushion and her half-finished block on a dotted grid. The welcome is queued (`welcomeAfter: true`): "Let's draft a block! Draw two parallel lines and one perpendicular to both. Tap the line tool." First hint: "Tap the line tool."

**Drafting (focus: the block grid).** At 1366x768 the block grid fills the middle with the kit left and the task card right; at 680x425 the kit is a bottom bar and the card a sheet. Six tasks: two parallel lines and a perpendicular; a ray from a point; an acute, a right and an obtuse angle; a segment that meets two others at right angles; a right triangle; a block with no parallel lines.

**Naming what you drew.** The kit draws but does not name. After each task a tray of nine tags appears (point, segment, ray, line, acute angle, right angle, obtuse angle, parallel, perpendicular) and the child drags the tags the task needs onto the drawing: for task 1, `parallel` onto the pair and `perpendicular` onto the crossing line. `Check` then tests both the drawing and the tags, and only then do the glows and angle marks show. A wrong tag is lifted off with no reason on the first miss and with the reason on the second. Auntie Mae drafts and tags one ray and one right angle first, saying what makes each ("It starts at a point and goes on one way, so it's a ray"); her example cannot be skipped and `Mae's example` reopens it.

**Find it in the block.** Auntie Mae's half-finished block fills the grid with no tags. Six cards, one at a time: tap two parallel segments; tap two perpendicular segments; tap an acute angle; tap a right angle; tap an obtuse angle; tap a line segment that is not a side of the block. Two tries each, then Mae shows it and the card comes back later on a different block.

**Mirror mode.** The child draws on half the grid, drags a mirror line, and the other half appears.

**Symmetry hunt.** Eight blocks. The child drags a candidate line and taps Fold: the halves fold and either match or show the gap. The count goes on the label (a square block: four; a heart block: one; a pinwheel: none).

**Scrap bin.** The same twelve pieces are sorted four times, each time into a yes bin and a no bin. Round 1: `has parallel sides` and `no parallel sides`. Round 2: `has perpendicular sides` and `no perpendicular sides`. Round 3: `has an obtuse angle` and `no obtuse angle`. Round 4: `right triangle`, `triangle, not right` and `not a triangle`. Auntie Mae sorts the first piece of each round aloud. To drop a piece in a yes bin the child first marks the proof on it: taps the two parallel sides, taps the two sides that meet at a square corner (a square-corner card can be dragged onto any corner to test it), or taps the obtuse corner. A no drop needs no mark. Pieces can be turned so parallel sides are not always level. A wrong drop, or a wrong mark, sends the piece to the mending pile with no reason given; when the round's other pieces are done the mending pile comes back, and this time a miss names the feature. The round ends when the pile is empty, and the label shows how many went to mending.

**Flag hunt (the aha).** Japan (two lines), Canada (one), Switzerland's square flag (four), the United Kingdom (none, though it looks symmetric), Nepal (none), and the child's own block. Auntie Mae: "A line of symmetry is just one more line you can test. Fold it and look."

**The end.** The finished block with its label. `Print` prints it.

**Class quilt (extra).** Blocks from the class laid in a quilt on one device and printed.

## Content
- Six drafting tasks, eight blocks (traditional patterns drawn plainly), six real flags drawn to their published proportions, all readable with `Read`. No brand logos.
- The twelve scraps, with parallel sides, perpendicular sides, an obtuse angle, and the round 4 bin: square (yes, yes, no, not a triangle); long rectangle (yes, yes, no, not a triangle); rhombus with 60 and 120 degree corners (yes, no, yes, not a triangle); slanted parallelogram (yes, no, yes, not a triangle); trapezoid with two equal slanted sides (yes, no, yes, not a triangle); trapezoid with one square end (yes, yes, yes, not a triangle); kite with corners 100, 110, 40 and 110 degrees (no, no, yes, not a triangle); four-sided scrap with corners 90, 80, 110 and 80 degrees (no, yes, yes, not a triangle); right triangle with three different sides (no, yes, no, right triangle); right triangle with two equal sides (no, yes, no, right triangle); triangle with three equal sides (no, no, no, triangle, not right); triangle with a 120 degree corner (no, no, yes, triangle, not right).
- Yes counts by round: parallel 6 of 12, perpendicular 6 of 12, obtuse 7 of 12; round 4 has 2 right triangles, 2 other triangles and 8 others.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Points snap to the dotted grid; lines can be moved or deleted until `Check`.
- Keyboard: Tab to tools, grid points, lines, the mirror line, Fold and the labels; arrows move a point; Enter draws or folds.
- With Motion off the fold shows the two halves overlaid at once.

## Look
- Accent `--brand` #1d3f6e quilt navy (header, the kit, buttons); gold #f4c542 (the guide that meets the rule, the line in hand); paper #eef2f8; ink #0a1626; muted #4e5663.
- Contrast (WCAG 2.1, computed): white on brand 10.56:1; brand on paper 9.40:1; ink on paper 16.17:1; muted on paper 6.59:1; ink on gold 11.17:1.
- Never color alone: parallel lines carry arrow ticks, perpendicular corners a square, angles their type in words.
- Different from this batch (craft-fair plum, brick orange, track teal, workbench olive).

## Art
- People (illustrated): Auntie Mae and two quilters, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Local FLUX (`scripts/localart.py`): the quilting room (1, 16:9).
- Drawn in code: the grid, the kit, blocks, scraps and flags (so lines stay exact).
About 4 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as Auntie Mae; `curious-librarian` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.task + ':' + state.block + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `draft`: "Pick a tool, then tap two points."
- how `mirror`: "Drag the mirror line onto the grid."
- how `fold`: "Drag a line across, then tap Fold."
- how `tag`: "Drag a name tag onto what you drew."
- how `find`: "Tap it in Auntie Mae's block."
- how `sort`: "Mark the sides or the corner, then drag the piece to a bin."
- event, whole, Mae's example and her first sort of each round.
- event, whole, flag hunt.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the drafting kit with snapping and naming, parallel and perpendicular tests, angle typing, mirror and fold. Flags sit in a marked block `/* FLAGS DATA: begin */ ... /* end */` with proportions and sources.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Drafting | Draw lines anywhere; wait for the kit to name it | Each task checks parallel, perpendicular and angle type exactly, and the kit shows no names or glows until the child's tags are checked. |
| Tags | Try tags one after another | Nine tags; a miss gives no reason the first time, and the task is not done until drawing and tags pass together. |
| Find it | Tap around the block | Two tries, then Mae shows it and the card returns on another block. |
| Symmetry | Count lines by guessing | A count is accepted only after each line is folded. |
| Sorting | Put every piece in yes; put every piece in no; alternate | A yes needs the right sides or corner marked on the piece, so a blind yes fails; all-no misses 6 or 7 pieces a round, and each one must be redone from the mending pile. Yes and no are close to even, so no fixed pick does well. |
| Right triangles | Call every triangle a right triangle | Two of the four triangles are not; the yes needs the square corner marked. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Mae's example (whole). `draft`; `tag`; `find`.
2. `mirror`; `fold`.
3. `sort`.
4. Flag hunt (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.G.1, 4.G.2, 4.G.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Flag designs: Japan, Canada, Switzerland, United Kingdom, Nepal | CIA, "The World Factbook", flag descriptions | Encyclopaedia Britannica, entries for each national flag | yes |
| The Union Flag is not mirror symmetric because the red saltire is counterchanged | UK Parliament, "The Union Flag" (House of Commons Library briefing) | Flag Institute, "Union Flag" | yes |
| Classifying by features before names | Common Core Standards Writing Team (2013), "Progressions for the CCSS, K-6 Geometry" | Clements and Sarama (2014), "Learning and Teaching Early Math: The Learning Trajectories Approach" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s13, 2026-11-10): a square has four lines of symmetry, a non-square rectangle two, a pinwheel none; six drafting tasks, eight blocks, twelve scraps and six flags; contrast as in Look.
Checks run again for the spec fix (Python, scratchpad s/fx, 2026-11-10): the twelve scraps' feature table gives 6 yes for parallel, 6 for perpendicular, 7 for obtuse, and 2, 2 and 8 in round 4; every four-sided scrap's corners add to 360 (100 + 110 + 40 + 110; 90 + 80 + 110 + 80; 60 + 120 + 60 + 120); all-yes with no marks passes 0 pieces and all-no leaves 6, 6 and 7 for mending.

## Done when
1. Focus and fold: at 1366x768 grid, kit and card; at 680x425 kit bar and card sheet.
2. Six drafting tasks are drawn and the child's own name tags are right; the kit shows no names before `Check`. (4.G.1)
3. Six find-it cards are answered on Auntie Mae's block. (4.G.1)
4. Twelve scraps are sorted four ways with proof marks on every yes; the mending pile is empty at the end of each round. (4.G.2)
5. Lines of symmetry are drawn, folded and counted on blocks and flags. (4.G.3)
6. Mae's example plays first and can be reopened; she sorts the first piece of each round.
7. Flag drawings match their published proportions.
8. Auntie Mae and the quilters are labeled illustration; no brand logos.
9. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
10. Motion off: folds overlay at once; no network requests.

## Open questions
None.
