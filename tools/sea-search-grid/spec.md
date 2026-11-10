# Sea Search Grid

## One idea
The child joins a harbor rescue crew under Captain Lena (made up, labeled "illustration"): on a gridded sea chart the harbor sits at the origin, x counts kilometers east and y counts kilometers north, and the radio reports positions as (east, north); in learn-the-grid rounds the child marks each radio call, names the axes and origin, and hears why (4, 7) and (7, 4) are different places; in search rounds a kayak drifts to a hidden point, the child calls a search point, and the radio answers with where the kayak is from that call ("the kayak is 3 east and 2 south of your call"), so each number in the pair becomes a distance in one direction, and fewer calls earn a better crew rating; in log rounds a drift log (hour 0 at (2, 1), hour 1 at (3, 3), hour 2 at (4, 5)) is plotted and read in context: she drifted 2 km north each hour, and if the wind holds she will be at (6, 9) at hour 4; at the end the kayaker is found and the log becomes a picture of her route, so a fifth grader learns the parts of the coordinate system and how to graph points in the first quadrant to solve real problems and interpret coordinates in context.

## Not like
- two-rule-race (5, spec): pairs from two rules, same grid engine. Here reading and searching positions.
- deep-sea-dive (6, concept): signed numbers in all four quadrants. Here the first quadrant only.
- fire-lookout-triangles (12, spec): bearings and triangle solving. Here whole-number steps east and north.
- garden-grid (2, spec): rows and columns in a garden. Here ordered pairs from an origin.

## Who and how
- Grade 5, Math, module "The Coordinate Plane". Standards: 5.G.1 (use a pair of perpendicular number lines, called axes, to define a coordinate system, with the intersection of the lines (the origin) arranged to coincide with the 0 on each line and a given point in the plane located by using an ordered pair of numbers, called its coordinates; understand that the first number indicates how far to travel from the origin in the direction of one axis, and the second number indicates how far to travel in the direction of the second axis, with the convention that the names of the two axes and the coordinates correspond (e.g., x-axis and x-coordinate, y-axis and y-coordinate)), 5.G.2 (represent real world and mathematical problems by graphing points in the first quadrant of the coordinate plane, and interpret coordinate values of points in the context of the situation).
- Format: map (changed from cards). Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six radio calls, six search rounds, three drift logs, the crew rating. Extra: Route relay (one student plots a route by coordinates, a partner follows it with the chart hidden). tool.json `modes: ["Rescue", "Route relay"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5.G.1 | Mark radio calls; name axes and origin; compare (4, 7) and (7, 4) | the boat stepping east, then north | 2 |
| 5.G.1 | Call search points and read the reply | steps from the call to the kayak | 3 |
| 5.G.2 | Plot a drift log and answer in context | the route as dots; 2 km north each hour | 4 |

## Screens and modes
Header (kit): title "Sea Search Grid"; `Rescue`, `Route relay`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A sea chart with a harbor in the lower left corner, the grid 0 to 10 each way, a rescue boat at the dock and Captain Lena at the radio. The welcome is queued (`welcomeAfter: true`): "A kayaker's last call put her at 4, 7. Four east, seven north. Tap the chart where she called from." First hint: "Tap the chart at 4 east, 7 north."

**Learn the grid (focus: the chart).** At 1366x768 the chart fills the left two thirds with the radio log right; at 680x425 the log is a sheet. Each tap places a marker, and the boat steps east first, then north, counting aloud. The child labels the x-axis (east), the y-axis (north) and the origin (the harbor). A side-by-side round marks (4, 7) and (7, 4) and asks which is farther north.

**Search rounds.** The kayak is hidden somewhere on the grid. The child taps a point and taps `Call`; the radio answers in whole steps with east or west and north or south ("3 east and 2 south of your call"). The child calls again until the boat reaches her. The crew rating counts calls (three stars at three calls or fewer). Every call stays on the chart with its reply.

**Log rounds.** A drift log card lists hours and positions. The child plots each hour, and questions follow: how far north each hour, how far east each hour, and where she will be at hour 4 if the wind holds. The child types (6, 9) and the boat heads there.

**Found (the aha).** The kayaker waves from her kayak. Captain Lena: "Every pair is two trips from the harbor: east first, then north. Plot a log and the story turns into a picture."

**The end.** The chart with every call and the route. `Print` prints it.

**Route relay (extra).** One student lists a route as coordinates; the partner follows it with only the list.

## Content
- Six radio calls, six hidden kayak points, three drift logs, all on whole numbers from 0 to 10 and readable with `Read`.
- No ships to sink, no hits and misses: every round is a rescue, and the kayaker is always found safe.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A marker can be moved until `Call` or `Check`.
- Keyboard: Tab to the chart (arrows move the cursor one step, the position is read aloud), Call, the log, axis labels and the answer box; Enter places or calls.
- With Motion off the boat jumps to each point.

## Look
- Accent `--brand` #145a7a chart sea blue (header, grid labels, buttons); gold #f4c542 (the marker in hand, the found kayak); paper #ebf4f8; ink #05202e; muted #4a575d.
- Contrast (WCAG 2.1, computed): white on brand 7.57:1; brand on paper 6.79:1; ink on paper 15.03:1; muted on paper 6.69:1; ink on gold 10.31:1.
- Never color alone: each call shows its pair and its reply in words; the found kayak shows "found".
- Different from this batch (magnifier indigo, sprout green, sign red, cardboard umber).

## Art
- People (illustrated): Captain Lena and the kayaker, labeled "illustration" (Gemini, `people: true`, 2; cutout yes).
- Local FLUX (`scripts/localart.py`): the harbor (1, 16:9), the sea chart texture (1, 16:9), the rescue boat (1, 1:1).
- Drawn in code: the grid, axes, markers, the route.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as Captain Lena; `news-reader` as the radio and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.call + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `mark`: "Tap the chart at the called point."
- how `label`: "Drag a label onto an axis."
- how `call`: "Tap a point, then tap Call."
- how `log`: "Plot the next hour on the chart."
- how `predict`: "Type where she'll be at hour 4."
- event, whole, found.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
coordinate (`kit/coordinate.js`), as described in coordinate-proof-lab's spec. Uses `CoordPlane` with `quadrant: 'first'`, range 0 to 10 and `snap: 1`, `pointAt` with `hidden: true` for the kayak, `Coord.steps(call, kayak)` for the reply in whole steps (dx as east or west, dy as north or south), and `plotPairs` with `connect: true` for the drift log. No polygons, no radicals. Tool-only code: the radio log, the crew rating.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Marks | Tap near the point | Marks snap to the grid and are checked exactly. |
| Search | Tap every point | The rating counts calls, and each reply must be read to plan the next. |
| Hour 4 | Guess from the picture | The answer is typed as a pair and checked exactly. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `mark`; `label`.
2. `call`.
3. `log`; `predict`.
4. Found (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 5.G.1, 5.G.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Students often swap the order of coordinates | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | Sarama and Clements (2009), "Early Childhood Mathematics Education Research", Routledge | yes |
| Search patterns and reported positions are core to marine rescue | U.S. Coast Guard, "National Search and Rescue Supplement" (2023) | International Maritime Organization, "IAMSAR Manual, Volume III" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s16, 2026-11-10): a call at (2, 6) with the kayak at (5, 4) replies 3 east and 2 south; the log (2, 1), (3, 3), (4, 5) rises 2 north each hour, so hour 4 is (6, 9); every point stays within 0 to 10; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 chart and log; at 680x425 log as a sheet.
2. Six calls are marked, the axes and origin are named, and (4, 7) and (7, 4) are told apart. (5.G.1)
3. Six kayaks are found by reading east or west and north or south replies. (5.G.1)
4. Three drift logs are plotted and read in context, including hour 4. (5.G.2)
5. No hits, misses or sinking; every round is a rescue.
6. `Read` reads every card and the cursor position; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the boat jumps; no network requests.

## Open questions
- The idea card changes the format from cards to map (default used: map, since the play is a search on a gridded sea chart).
