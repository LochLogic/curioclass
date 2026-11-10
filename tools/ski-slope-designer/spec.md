# Ski Slope Designer

## One idea
On a side view of a mountain drawn on a grid, with the top station at the origin and every meter across and down marked, the trail designer, Ana (made up, labeled "illustration"), asks the child to lay out runs for a new resort, starting with a gentle kids' run; the child drags a straight run and a skier tests it, tumbling into soft snow if it is too steep and stopping if it is too flat, with the goal set by game rating bands (green, blue, black); on a run that drops 40 m for every 100 m across, the child draws slope triangles anywhere and at any size (100 across and 40 down, 250 across and 100 down) and the tool shows they are similar, so the rise over run is the same 2/5 everywhere and the run is drop = 0.4 x distance; compare rounds rank three runs given in different forms, one as a graph (0.5), one as an equation (drop = 0.4 x distance) and one as a survey crew's table ((0, 0), (50, 15), (100, 30), so 0.3), naming each unit rate in meters of drop per meter across; lodge rounds start a run at a mid-mountain lodge 300 m below the top, so the run becomes y = -0.25x - 300, and the child sees the line shift down without changing slope (400 m across it reaches 400 m below the top); at the end the child sees that slope is one number for a whole straight line and that similar triangles are why, so an eighth grader learns to graph proportional relationships, read the unit rate as the slope, compare them across forms, and derive y = mx and y = mx + b from similar triangles.

## Not like
- two-trains (8, live): systems of lines, same graphing kit. Here slope itself.
- story-graphs (8, spec): sketching functions from stories. Here building lines from slope.
- ramp-and-roof (10, spec): trigonometry on ramps. Here rise over run and similar triangles.
- intersection-angles (7, spec): angle facts. Here triangles that share a slope.

## Who and how
- Grade 8, Math, module "Slope and Proportional Relationships". Standards: 8.EE.5 (graph proportional relationships, interpreting the unit rate as the slope of the graph; compare two different proportional relationships represented in different ways), 8.EE.6 (use similar triangles to explain why the slope m is the same between any two distinct points on a non-vertical line in the coordinate plane; derive the equation y = mx for a line through the origin and the equation y = mx + b for a line intercepting the vertical axis at b).
- Format: builder. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six runs to build, three triangle rounds, four compare sets, three lodge runs. Extra: Resort map (design a whole map and trade it with a partner to rate, one device). tool.json `modes: ["Design", "Resort map"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 8.EE.5 (graph, unit rate) | Build runs; read drop per meter across | the skier's test; the slope label | 2 |
| 8.EE.5 (compare) | Rank runs given as graph, equation, table | 0.5, 0.4, 0.3 | 3 |
| 8.EE.6 (triangles) | Draw slope triangles anywhere | similar triangles, one ratio | 2 |
| 8.EE.6 (equations) | Write y = mx, then y = mx + b from a lodge | the shifted run | 4 |

## Screens and modes
Header (kit): title "Ski Slope Designer"; `Design`, `Resort map`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A snowy mountain in side view on a faint grid, the top station at the origin, a lodge halfway down, and Ana with a clipboard and goggles. The welcome is queued (`welcomeAfter: true`): "Kids' run first: gentle. Drag the end of the run down the mountain." First hint: "Drag the end of the run."

**Build (focus: the mountain).** At 1366x768 the graph fills the left with the run card right; at 680x425 the card is a sheet. The child drags the run's end point (snapped to 10 m). `Test` sends a skier: too steep, a gentle tumble into powder; too flat, the skier stops. The run card shows rise, run and slope as a fraction and decimal; a band shows green, blue or black.

**Triangles.** On a locked run the child draws slope triangles by dragging two points; each triangle lists its legs and ratio. A `Stack` button slides them onto one corner to show they are similar.

**Compare.** Three runs in three forms; the child types each unit rate and ranks them. A fourth set adds a run with a different direction (rising toward the lift) to discuss the sign.

**Lodge.** A run starts 300 m below the top. The child writes y = mx + b and sees the run shift down without turning.

**One number (the aha).** Ana: "Pick any two points on a straight run. The triangles match, so the slope is the same everywhere."

**The end.** The finished trail map. `Print` prints it.

**Resort map (extra).** Trade and rate maps.

## Content
- Rating bands are game bands, labeled "game ranges, not an official rule", all readable with `Read`.
- Skiers of varied looks, all labeled "illustration"; tumbles are soft and funny, never injuries.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A run can be moved until `Lock run`; triangles can be removed.
- Keyboard: Tab to the run's end point (arrows move 10 m), Test, the triangle points, compare boxes and the equation box; Enter tests or checks.
- With Motion off the skier's test shows the end result as a still.

## Look
- Accent `--brand` #1c5d8a glacier blue (header, runs, buttons); gold #f4c542 (the point in hand, the slope triangle); paper #eef4f9; ink #06192a; muted #4b5562.
- Contrast (WCAG 2.1, computed): white on brand 7.04:1; brand on paper 6.35:1; ink on paper 16.05:1; muted on paper 6.83:1; ink on gold 10.94:1.
- Never color alone: bands carry their names and shapes (circle, square, diamond).
- Different from this batch (puzzle plum, timber olive, harbor teal, cranberry).

## Art
- People (illustrated): Ana and four skiers of varied looks, labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Local FLUX (`scripts/localart.py`): the mountain backdrop (1, 16:9), the lodge (1, 4:3).
- Drawn in code: the grid, runs, triangles and the skier's path.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as Ana; `lively-host` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.run + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `drag`: "Drag the end of the run."
- how `test`: "Tap Test to send a skier."
- how `triangle`: "Drag two points to draw a slope triangle."
- how `rank`: "Type each unit rate, then rank them."
- how `lodge`: "Type the equation for the lodge run."
- event, whole, one number.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
graphing (`kit/graphing.js` unchanged), as described in two-trains' spec: `Plane` with a flipped y label for drop, `g.fn` for each run with `domain`, `g.point` with `snap` for draggable ends and triangle corners, `g.segment` for triangle legs, `g.label`. Exact slopes with `Frac` as described in equation-golf's spec. Tool-only code: the skier test, rating bands, the triangle stacker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Build | Drag until the band turns green | The slope must also be typed as rise over run. |
| Triangles | Draw one triangle | Three triangles of different sizes are needed. |
| Compare | Rank by the first number seen | Each unit rate is typed and checked. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `drag`; `test`.
2. `triangle`.
3. `rank`; `lodge`.
4. One number (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 8.EE.5, 8.EE.6 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Similar slope triangles explain constant slope | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Expressions and Equations" | Lobato and Ellis (2010), "Developing Essential Understanding of Ratios, Proportions, and Proportional Reasoning, Grades 6-8", NCTM | yes |
Backed twice: 2. Cut: 1 (the claim that U.S. ratings are relative to each resort, with only one source found; the bands stay labeled game ranges).

Checks run (Python, scratchpad s21, 2026-11-10): 40/100 = 100/250 = 2/5; 15/50 = 30/100 = 3/10; -0.25 x 400 - 300 = -400; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 graph and card; at 680x425 card as a sheet.
2. Six runs are built and tested, and slope triangles show one ratio per run. (8.EE.5, 8.EE.6)
3. Four sets of runs in different forms are ranked by unit rate. (8.EE.5)
4. Lodge runs are written as y = mx + b. (8.EE.6)
5. Rating bands are labeled game ranges.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the test is a still; no network requests.

## Open questions
- Rating band numbers (default used: game ranges labeled as such, green gentle, blue middle, black steep, because no sourced national percent cutoffs were found; a sourced typical range can replace them).
