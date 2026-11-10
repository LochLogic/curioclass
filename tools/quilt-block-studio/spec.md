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
- Format: studio. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- The drafting kit, six drafting tasks, mirror mode, eight blocks to test, a scrap bin of twelve pieces with three labels, six flags, the block label. Extra: Class quilt (every student's block printed into one quilt, assembled on the device, nothing uploaded). tool.json `modes: ["Studio", "Class quilt"]`, `minutes: "25-35"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.G.1 | Draft with point, segment, ray and line tools to meet a task | names; parallel and perpendicular glows; angle tags | 2 |
| 4.G.2 | Sort scrap pieces by features onto labels | the labels filling; right triangles found | 3 |
| 4.G.3 | Mirror half a block; fold to test lines on blocks and flags | the fold matching or not | 4 |

## Screens and modes
Header (kit): title "Quilt Block Studio"; `Studio`, `Class quilt`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A quilting table, fabric scraps, Auntie Mae with a pincushion and her half-finished block on a dotted grid. The welcome is queued (`welcomeAfter: true`): "Let's draft a block! Draw two parallel lines and one perpendicular to both. Tap the line tool." First hint: "Tap the line tool."

**Drafting (focus: the block grid).** At 1366x768 the block grid fills the middle with the kit left and the task card right; at 680x425 the kit is a bottom bar and the card a sheet. Six tasks: two parallel lines and a perpendicular; a ray from a point; an acute, a right and an obtuse angle; a segment that meets two others at right angles; a right triangle; a block with no parallel lines.

**Mirror mode.** The child draws on half the grid, drags a mirror line, and the other half appears.

**Symmetry hunt.** Eight blocks. The child drags a candidate line and taps Fold: the halves fold and either match or show the gap. The count goes on the label (a square block: four; a heart block: one; a pinwheel: none).

**Scrap bin.** Twelve pieces sorted onto three labels: "has a right angle", "has parallel sides", "is a right triangle". A piece can go on more than one label.

**Flag hunt (the aha).** Japan (two lines), Canada (one), Switzerland's square flag (four), the United Kingdom (none, though it looks symmetric), Nepal (none), and the child's own block. Auntie Mae: "A line of symmetry is just one more line you can test. Fold it and look."

**The end.** The finished block with its label. `Print` prints it.

**Class quilt (extra).** Blocks from the class laid in a quilt on one device and printed.

## Content
- Six drafting tasks, eight blocks (traditional patterns drawn plainly), twelve scrap pieces, six real flags drawn to their published proportions, all readable with `Read`.
- No brand logos.

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
- how `sort`: "Drag the piece onto every label it fits."
- event, whole, flag hunt.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the drafting kit with snapping and naming, parallel and perpendicular tests, angle typing, mirror and fold. Flags sit in a marked block `/* FLAGS DATA: begin */ ... /* end */` with proportions and sources.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Drafting | Draw lines anywhere | Each task checks parallel, perpendicular and angle type exactly. |
| Symmetry | Count lines by guessing | A count is accepted only after each line is folded. |
| Sorting | Put every piece on every label | Wrong placements bounce back with the missing feature named. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `draft`.
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

## Done when
1. Focus and fold: at 1366x768 grid, kit and card; at 680x425 kit bar and card sheet.
2. Six drafting tasks are drawn and named. (4.G.1)
3. Twelve scraps are sorted by features, with right triangles found. (4.G.2)
4. Lines of symmetry are drawn, folded and counted on blocks and flags. (4.G.3)
5. Flag drawings match their published proportions.
6. Auntie Mae and the quilters are labeled illustration; no brand logos.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: folds overlay at once; no network requests.

## Open questions
None.
