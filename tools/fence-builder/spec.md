# Fence Builder

## One idea
In a backyard with a roll of exactly 24 meters of fence and a happy dog named Biscuit, the child drags the four corners of a rectangular pen on a meter grid, and side lengths, the perimeter and the count of square meters inside all update live, while Biscuit runs laps in a roomy pen and squeezes sideways in a skinny one; every pen must use all 24 meters, and a log records each one tried (1 by 11 holds 11 square meters, 6 by 6 holds 36); fix-the-fence jobs ask for a missing side (three sides of a 30 meter fence are 8, 7 and 8, so the last is 7); same-room jobs flip it, asking for pens with 16 square meters inside but different fence lengths (1 by 16 needs 34 meters, 4 by 4 only 16); at the end the log shows the same fence making areas from 11 to 36 square meters and the square pen winning, so a third grader learns to solve problems with perimeters of polygons, including finding perimeter from side lengths and finding an unknown side, and to show rectangles with the same perimeter and different areas or the same area and different perimeters.

## Not like
- tile-the-floor (3, spec): area by tiling, same family. Here perimeter against area.
- optimization-workshop (12, spec): calculus and best shapes. Here counting and logging.
- area-model-builder (4, concept): multiplication by place value, same family. Here fences.
- garden-grid (2, spec): building shapes from clues. Here measuring around them.

## Who and how
- Grade 3, Math, module "Perimeter". Standards: 3.MD.8 (solve real world and mathematical problems involving perimeters of polygons, including finding the perimeter given the side lengths, finding an unknown side length, and exhibiting rectangles with the same perimeter and different areas or with the same area and different perimeters).
- Format: builder. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- The 24-meter pen with a log, two more fence rolls (20 and 30 meters), six fix-the-fence jobs (rectangles and other polygons), three same-room jobs, the log chart. Extra: Partner logs (two players compare tables). tool.json `modes: ["Yard", "Partner logs"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3.MD.8 (perimeter from sides) | Drag corners; read the perimeter | sides labeled; the fence counter | 2 |
| 3.MD.8 (unknown side) | Fix-the-fence jobs | the gap and the leftover fence | 3 |
| 3.MD.8 (same perimeter or same area) | Log pens; same-room jobs | the log; Biscuit's room | 4 |

## Screens and modes
Header (kit): title "Fence Builder"; `Yard`, `Partner logs`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A grassy backyard on a faint meter grid, a roll of fence marked 24 m, Biscuit wagging, and the dog's owner Lena (made up, labeled "illustration"). The welcome is queued (`welcomeAfter: true`): "Biscuit needs a pen! Use all 24 meters of fence. Drag a corner." First hint: "Drag a corner of the pen."

**Building (focus: the pen).** At 1366x768 the yard fills the left with the log at the right; at 680x425 the log is a tab. Corners snap to whole meters. Each side shows its length; a fence counter shows meters used out of 24; the inside shows a count of square meters (a light grid). `Log it` adds the pen to the table only when all 24 meters are used. Biscuit runs laps in a big pen and squeezes sideways in a skinny one.

**Fix the fence.** Three sides built; the counter says 23 of 30 used. "How long is the last side?" The child types it. Later jobs use an L-shaped run and a five-sided garden bed.

**Same room.** "Make pens with 16 square meters inside." The child builds 1 by 16, 2 by 8 and 4 by 4; the log shows fence needed: 34, 20, 16. "Which pen needs the least fence?"

**The square wins (the aha).** The 24-meter log as a bar chart: areas 11, 20, 27, 32, 35, 36. Lena: "Same fence, very different room. The square gives Biscuit the most!"

**The end.** The log and Biscuit's favorite pen. `Print` prints the log.

**Partner logs (extra).** Two players log pens and compare.

## Content
- Fence rolls of 20, 24 and 30 meters, pens with whole-meter sides, six fix jobs, three same-room jobs, all readable with `Read`. Biscuit is never hurt; skinny pens just look squished.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Corners can be dragged at any time; the log keeps earlier pens.
- Keyboard: Tab to each corner, `Log it`, the keypad and the log; arrows move a corner one meter.
- With Motion off Biscuit sits still and the chart appears at once.

## Look
- Accent `--brand` #3a6a1f backyard green (header, the fence counter, buttons); gold #f4c542 (the corner in hand, the best pen); paper #f2f8ee; ink #10200a; muted #4b5a45.
- Contrast (WCAG 2.1, computed): white on brand 6.44:1; brand on paper 5.96:1; ink on paper 15.76:1; muted on paper 6.83:1; ink on gold 10.47:1.
- Never color alone: the fence counter shows numbers; the best pen gets a star.
- Different from this batch (penguin navy, mural magenta, picnic red, newsletter teal).

## Art
- People (illustrated): Lena, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the backyard from above (1, 16:9), Biscuit in three poses (run, squeeze, sit) (3, 1:1).
- Drawn in code: fences, the grid, side labels, the log and chart.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `easy-coach` as Lena; `playful-friend` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.job + ':' + state.pen + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `drag`: "Drag a corner of the pen."
- how `log`: "Tap Log it."
- how `fix`: "Type the missing side."
- how `room`: "Build a pen with 16 square meters inside."
- event, whole, the square wins.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
area (family "area"). Uses the shared pieces from the marked block `/* AREA ENGINE: begin */ ... /* end */` as described in tile-the-floor's spec: the unit grid and area counts. Tool-only code: fence corners and lengths, the fence counter, the log and chart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Log | Log any pen | `Log it` stays off until all 24 meters are used, and the hint says so. |
| Missing side | Type guesses | The fence grows to the typed length and shows the gap or overlap. |
| Same room | Build any pen | The inside count must be 16. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `drag`; `log`.
2. `fix`.
3. `room`.
4. Square wins (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 3.MD.8 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Students often confuse perimeter and area, and fixed-perimeter tasks separate them | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-5 Geometric Measurement" | Kamii and Kysh (2006), "The difficulty of 'length x length': is a square the unit of measure?", Journal of Mathematical Behavior | yes |
| For a fixed perimeter, the square rectangle holds the most area | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-5 Geometric Measurement" | National Council of Teachers of Mathematics, Illuminations, "Fixed perimeter" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r11, 2026-11-10): every 24-meter rectangle with whole sides holds 11, 20, 27, 32, 35 or 36 square meters; 30 - (8 + 7 + 8) = 7; 16 square meters needs 34, 20 or 16 meters of fence; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 yard and log; at 680x425 log tab.
2. Pens are built and their perimeters read from side lengths. (3.MD.8)
3. Six missing sides are found. (3.MD.8)
4. Same-perimeter and same-area pens are logged and compared. (3.MD.8)
5. `Read` reads every card; every control is 48 px or more.
6. Lena is labeled illustration; Biscuit is never hurt.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still dog and chart; no network requests.

## Open questions
None.
