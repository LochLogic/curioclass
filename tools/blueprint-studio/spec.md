# Blueprint Studio

## One idea
At an architect's studio desk Ms. Ruiz (made up, labeled "illustration") hands the child graph paper with a bedroom outline drawn at 1 inch = 2 feet and a tray of furniture, and asks whether a queen bed will fit before anything is bought; the child places furniture, reads real lengths from the scale (the 6 by 5 inch outline is a 12 by 10 foot room, and a 60 by 80 inch bed draws as 2 1/2 by 3 1/3 inches), and checks the fit in a 3D preview; area rounds bring the surprise that doubling the scale makes a drawn rug four times the paper area; rescale rounds redraw the plan at 1 inch = 3 feet for a smaller printout, so the room becomes 4 by 3 1/3 inches and its paper area shrinks from 30 to 13 1/3 square inches, which is 4/9, the square of 2/3; in the triangle workshop the child builds corner-desk tops and loft braces with ruler and protractor tools from given measures, and records what happens: sides of 3, 4 and 8 feet will not close (no triangle), two sides and the angle between them make exactly one, and three angles make many sizes of the same shape; at the end the child sees that a scale multiplies every length but multiplies area by the square, and that some measures fix a triangle while others do not, so a seventh grader learns to solve problems with scale drawings, redraw at a different scale, and draw triangles from given conditions, noticing when they determine one triangle, more than one, or none.

## Not like
- clay-cutting-bench (7, spec): plane sections of solids. Here flat plans and triangles.
- shrink-ray (5, spec): scaling by fractions. Here scale drawings with real units.
- net-folder (6, spec): nets of solids. Here floor plans.
- slice-and-stack (10, spec): cross sections and solids of rotation. Here drawings at scale.

## Who and how
- Grade 7, Math, module "Scale Drawings and Constructions". Standards: 7.G.1 (solve problems involving scale drawings of geometric figures, including computing actual lengths and areas from a scale drawing and reproducing a scale drawing at a different scale), 7.G.2 (draw (freehand, with ruler and protractor, and with technology) geometric shapes with given conditions; focus on constructing triangles from three measures of angles or sides, noticing when the conditions determine a unique triangle, more than one triangle, or no triangle). 7.G.3 moves to clay-cutting-bench.
- Format: studio. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- One bedroom plan with twelve furniture pieces, the 3D preview, three rescale jobs, eight triangle orders, the conditions chart. Extra: Class room (the class lays out a classroom plan together on the projector). tool.json `modes: ["My room", "Class room"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.G.1 (lengths, areas) | Place furniture; read real sizes; find areas | scale ruler; the 3D preview | 2 |
| 7.G.1 (rescale) | Redraw at 1 inch = 3 feet | lengths times 2/3; area times 4/9 | 3 |
| 7.G.2 | Build triangles from given measures | no triangle, exactly one, many | 4 |

## Screens and modes
Header (kit): title "Blueprint Studio"; `My room`, `Class room`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A studio desk with graph paper, a room outline, a scale bar reading "1 inch = 2 feet", a furniture tray, and Ms. Ruiz with a pencil behind her ear. The welcome is queued (`welcomeAfter: true`): "Will a queen bed fit? Measure on the plan first. Drag the bed onto the plan." First hint: "Drag the bed onto the plan."

**Plan (focus: the paper).** At 1366x768 the plan fills the left with the tray and 3D preview right; at 680x425 the preview is a tab. Each piece shows its real size; the child types its drawn size before it drops. A scale ruler measures any gap. `Preview` shows the room in 3D with a door swing and a walking path.

**Area.** A rug at 1 inch = 2 feet, then the same plan at 1 inch = 1 foot: the child counts paper squares and sees four times as many.

**Rescale.** "Print it smaller, at 1 inch = 3 feet." The child computes each new length and redraws the outline; the tool overlays the result. Area on paper: 30 to 13 1/3 square inches; the child finds the factor 4/9.

**Triangle workshop.** Order cards ("corner desk: sides 3, 4 and 8 feet"; "brace: sides 4 and 6 with a 40 degree angle between"; "a 50, 60, 70 degree shelf"). The child uses the ruler, compass arc and protractor tools to build each one, then marks the result: no triangle, exactly one, or many. A chart collects which conditions do which.

**By the square (the aha).** Ms. Ruiz: "A scale stretches every length the same. Area stretches by the square. And three measures don't always fix a triangle."

**The end.** The plan, the rescaled plan and the conditions chart. `Print` prints them at true scale.

**Class room (extra).** A class layout on the projector.

## Content
- Twelve pieces with real sizes (a queen bed 60 by 80 inches, a desk, a dresser, a rug), all readable with `Read`.
- Triangle orders in feet and degrees; no orders with impossible angle sums except one marked as a trap.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pieces can be moved and turned until `Check`; drawings can be undone.
- Keyboard: Tab to tray pieces, the plan (arrows move a piece a quarter inch, R turns), the scale ruler, triangle tools and the chart; Enter places or checks.
- With Motion off the 3D preview is a still view.

## Look
- Accent `--brand` #1b4f86 blueprint blue (header, plan lines, buttons); gold #f4c542 (the piece in hand, a fitted piece); paper #edf3f9; ink #071a30; muted #4b5564.
- Contrast (WCAG 2.1, computed): white on brand 8.37:1; brand on paper 7.49:1; ink on paper 15.66:1; muted on paper 6.75:1; ink on gold 10.76:1.
- Never color alone: pieces that don't fit show "won't fit" and the overlap length.
- Different from this batch (reef green, loop indigo, case-file brown, factory red).

## Art
- People (illustrated): Ms. Ruiz, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the studio desk (1, 16:9), a finished bedroom (1, 16:9).
- Drawn in code: the plan, every piece at exact scale, the 3D preview, triangle tools.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as Ms. Ruiz; `bright-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.piece + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `place`: "Type the drawn size, then drag the piece."
- how `preview`: "Tap Preview to see it in 3D."
- how `rescale`: "Type the new length."
- how `build`: "Use the ruler and protractor to build it."
- how `result`: "Tap no triangle, one, or many."
- event, whole, by the square.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the scaled plan with exact `Frac` lengths (as described in equation-golf's spec), the 3D preview, ruler, compass arc and protractor tools, the triangle condition checker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Drawn sizes | Drag until it looks right | The drawn size is typed first and checked. |
| Rescale area | Multiply by 2/3 | Area is checked against 4/9. |
| Triangles | Mark every order "one" | 3, 4, 8 and the three-angle order are built to catch it. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `place`; `preview`.
2. `rescale`.
3. `build`; `result`.
4. By the square (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.G.1, 7.G.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| A queen mattress is 60 by 80 inches | International Sleep Products Association, mattress size standards | Consumer Reports, "Mattress Sizes and Dimensions" | yes |
| Area scales by the square of the scale factor | Common Core Standards Writing Team (2012), "Progressions for the CCSS, 7-8 Geometry" | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", grades 6-8 geometry | yes |
| Triangle inequality and SAS determine triangles | Euclid, "Elements", Book I, Propositions 4 and 20 | Common Core Standards Writing Team (2012), "Progressions for the CCSS, 7-8 Geometry" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s20, 2026-11-10): 12 by 10 feet at 1 inch = 2 feet is 6 by 5 inches; 60 by 80 inches (5 by 6 2/3 feet) draws as 2 1/2 by 3 1/3; at 1 inch = 3 feet the room is 4 by 3 1/3 and 13 1/3 / 30 = 4/9; 3 + 4 < 8; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 plan, tray and preview; at 680x425 preview as a tab.
2. Furniture is placed with real lengths and areas read from the scale. (7.G.1)
3. The plan is redrawn at a new scale with lengths and areas recomputed. (7.G.1)
4. Eight triangles are built and sorted into none, one or many. (7.G.2)
5. `Print` prints plans at true scale.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the preview is still; no network requests.

## Open questions
- The idea card moves 7.G.3 out of this tool (default used: clay-cutting-bench teaches plane sections; this tool keeps 7.G.1 and 7.G.2).
