# Reserve Designer

## One idea
Design a nature reserve on a real-feeling valley split by a river, a highway, a town and farms: buy land cell by
cell inside a budget so six species each get what they need (an elk herd that can reach both summer forest and
winter meadow, a prairie dog colony, a wood frog's pond beside forest, a black bear's big range, an ovenbird's
quiet forest interior, a river otter's protected banks), then stress-test the plan by losing one protected cell at a
time to fire or a new road and refine it until it survives.

## Not like
- island-economy (sci 9, maybe renamed Lake Commons): managing harvests of a shared resource over generations.
  Here nothing is harvested; the job is the shape and connection of protected land on a map.
- design-challenge-studio (sci 12): an open engineering design process for any problem. Here one fixed problem with
  testable species rules.
- biome-atlas and population-dashboard (sci 12): where biomes are and how human numbers change. Here one valley
  and the choices that fragment or connect it.
- carrying-capacity (same group): how many of one species a habitat holds. Here which species can live there at all.
- community-project-planner (live, 6-8 social studies): budgeting a town's projects. Here the budget buys habitat
  and the test is ecological, with trade-offs against farms.
- watershed-detective (sci 12, maybe renamed Upstream): finding a pollution source. No pollution here.

## Who and how
Grade 9, science (Life Science module Biodiversity and Human Impact: "Human activities and ecosystem stability").
Driver: students on laptops in pairs, a class compares plans at the end. 25 to 45 minutes. Standards: HS-LS2-7
(design, evaluate and refine a solution for reducing the impacts of human activities on the environment and
biodiversity), HS-LS4-6 (create or revise a simulation to test a solution to mitigate adverse impacts of human
activity on biodiversity), HS-LS2-8 (evaluate evidence for the role of group behavior in survival: the Groups mode,
and the herd and colony rules).
Topic line: biodiversity and human impact.
9-12 dark theme. Header: title, `.seg` modes **Plan**, **Stress test**, **Groups**, kit buttons `motion`, `sound`,
`read`.

## Screens and modes
Shared: the valley map on the stage (12 columns by 8 rows of square cells, drawn in code, compass and scale "1 cell =
1 square km"), panel right with budget bar, species checklist, `hint`, `tip`. Under 900 px tall: map cells shrink to
fit; species checklist becomes two columns of icons with their state words.

**Plan** (opens first). Click (or Enter on) a cell to protect it; click again to sell it back at full price.
Farm cells offer **Buy and farm on** (protected, still farmed) or **Buy and restore to meadow** (+$100k, becomes
meadow after a short grow animation). Highway cells offer **Build a wildlife crossing** ($500k, a bridge icon).
Town and river cells cannot be bought (river cells count as protected habitat when a bank beside them is
protected). Panel: **Budget** bar ($4,000k), **Spent**, **Left**; **Farms still farming** (must stay at 16 or more
of 20); species checklist, each row: portrait, name, need in words, state ("needs met" with a check, or what is
missing, for example "elk: herd reaches only 2 meadow cells south of the highway, needs 4"). **Show needs** toggles
an overlay that tints the cells each species could use. **Clear plan**.

**Stress test**. Locks the plan. **Run 50 years** plays one future per protected cell: in each, that one cell is
lost (a fire, a new road or a housing lot, chosen by a fixed rule from the cell's land type: forest fire, meadow
road, wetland drained, farm lot), and the checklist is re-checked. Result grid: one small map per future with the
lost cell marked and the species lost named under it. Summary: "All six kept in N of M futures." **Weakest cells**
highlights every cell whose loss breaks a species (a dashed accent outline and a crack icon), so students can
refine: **Back to plan** keeps the plan.

**Groups** (HS-LS2-8). Two cards, each with a small model and a source. Elk herd: **Herd size** slider 1 to 20,
each elk watching for predators 20 percent of the time; readout "chance at least one elk is watching" = 1 minus 0.8
to the power of herd size, with a bar chart (1: 20 percent, 5: 67, 10: 89, 20: 99), and the real finding that each
elk spends less time watching in bigger groups (Childress and Lung 2003). Prairie dogs: a colony picture where one
alarm call (button) makes every dog in the colony dive, with the text that alarm calls differ by predator (NPS). Both
cards end with "That is why the elk rule needs a herd's worth of land and the prairie dog rule needs a colony."

## Content
Map (row 0 is north; F forest, G meadow, W wetland, A farm, T town, R river, H highway, B the highway bridge over
the river):
```
row 0  F F F F F F R F F F F F
row 1  F F F W F F R G G F F F
row 2  F F W W F G R G G A F F
row 3  H H H H H H B H H H H H
row 4  G G A A G W R A A G G G
row 5  G G A T T W R A A G G A
row 6  G A A T T A R W W G G A
row 7  A A A A A A R W W G G A
```
Counts: forest 24, meadow 20, wetland 9, farm 20, town 4, river 7, highway 11, bridge 1.
Prices ($k): forest 250, meadow 200, wetland 150, farm 300; plus 100 for any cell touching town (8 neighbors).
Restore a bought farm to meadow +100. Wildlife crossing on a highway cell 500. Budget 4,000.
Connection: cells connect through their 4 side neighbors. A river cell counts as habitat when the cell to its left
or right is protected. The bridge cell connects north and south when the river cells above and below it count.
A crossing makes its highway cell count as habitat.
Species rules (each shown in words on its row):
- Elk (herd, migrates): one connected protected area holding 4 or more forest cells north of the highway and 4 or
  more meadow cells south of it.
- Prairie dog (colony): 3 or more protected meadow cells connected to each other (restored meadow counts).
- Wood frog: a protected wetland beside (4 neighbors) a protected forest cell.
- Black bear: one connected protected area of 12 or more cells.
- Ovenbird (forest interior): 2 or more protected forest cells with no farm, town or highway among their 8
  neighbors (restored farm counts as meadow).
- River otter: 4 or more river cells with a protected bank.
Checked plans (Python, Curio Class 2026-10-27):
- Cheapest plan meeting all six, $2,950k, 14 cells: (row, column) (0,4) (1,4) (1,5) (2,3) (2,4) (2,7) (4,5) (4,10)
  (5,5) (5,10) (6,7) (6,8) (6,9) (6,10). Stress test: all six kept in 0 of 14 futures (every cell is a weak link;
  elk breaks in 13 of them).
- A refined $4,000k plan, 19 cells: (0,3) (0,4) (0,5) (1,3) (1,5) (2,3) (2,4) (2,5) (2,7) (4,4) (4,5) (5,5) (5,9)
  (6,7) (6,8) (6,9) (6,10) (7,7) (7,9). All six kept in 14 of 19 futures; the five weak cells are (4,5) (5,5) (6,7)
  (6,8) (6,9), the wetland and meadow chain that carries the herd from the bridge to the southern meadows.
- The empty map meets none.
These are not the only answers; the tool never shows them. They prove the targets can be reached.
Hints: Plan "<b>Plan.</b> Click cells to protect them. Read each species' row to see what it still needs." /
Stress "<b>Stress test.</b> Press Run 50 years. Each future loses one protected cell. Fix the weakest cells." /
Groups "<b>Groups.</b> Move the herd size slider. Why might an elk be safer in a herd?"
Tips: "Corridors join patches so animals can move between them." / "Edges let in predators, weeds and noise, so
some birds need forest interior." / "A plan that just barely works breaks when anything changes." / "Farms feed
people too: keep at least 16 farming."
Model limits line: "A real reserve also needs water rights, willing sellers, fire plans and many more species. This
valley is made up; the species needs are simplified from real ones."

## Interactions in detail
- Every cell is a button with an accessible name ("Row 2, column 4, forest, $250k, not protected"); arrow keys move
  between cells; Enter opens the cell's action menu (a small popover with one or two buttons).
- Buy is refused with the reason when it would overspend ("$150k left, this cell costs $250k") or drop farms under 16
  ("Keep 16 farms farming: undo another restore first"). Only restores count against the 16; a farm bought and
  still farmed counts as farming.
- Species rows update after every change; a row that changes state flashes once (none with Motion off).
- Stress test runs the futures one after another (200 ms each, instant with Motion off). It is deterministic: the
  same plan always gives the same result, so pairs can compare.
- **Copy plan code** writes a short text code of the plan (cells and choices) to the clipboard; **Load plan code**
  reads one back, so a class can share plans without saving anything.
- Mode change: `V.hush()`; plan kept.

## Look
Accent `--brand #ff4a2e` (survey-flag orange-red), `--brand-ink #10161f`. Map tiles: forest `#2f5d3a`, meadow
`#8fae5a`, wetland `#4f7f86`, farm `#c9b56a`, town `#7a7a80`, river `#3f7fbf`, highway `#3a3a3a`, each with a
texture (trees, grass strokes, reeds, furrows, roofs, waves, dashed lane line) so land type never depends on color.
A protected cell gets a double outline (3 px accent outside, 2 px `#10161f` inside) and a small flag icon.
Contrast (computed): brand on --panel 5.17:1, on --sec-bg 4.90:1; brand-ink on brand 5.42:1; accent on the dark
inner line 5.42:1. Accent on tiles is low (1.25 to 2.28), so the dark inner line carries the outline on light
tiles (meadow 7.24, farm 8.91, wetland 4.07, river 4.32, town 4.26) and the accent carries it on forest (accent next
to the inner line, 5.42); the flag and the cell's name back it up. Nearest 9-12 accent #ff6150 (dE 16).

## Art
Cloudflare FLUX.2 (`scripts/cfart.py`), wildlife field-guide portraits, the animal centered in its habitat, soft
daylight, no lettering, webp, 1:1, long side 512 px, cutout no, people no. Used in the species rows (40 px) and the
Groups cards (160 px).
- rd-elk: a bull elk standing in a meadow at the forest edge, side view.
- rd-prairie-dog: a black-tailed prairie dog standing upright beside its burrow mound.
- rd-wood-frog: a wood frog on wet leaves at the edge of a small woodland pond, dark eye mask visible.
- rd-bear: an American black bear walking through a forest clearing, side view.
- rd-ovenbird: an ovenbird on the forest floor among leaves, orange crown stripe visible.
- rd-otter: a North American river otter on a river bank, head raised.

## Voice
Bank `gravel-ranger` (a field ranger walking the boundary): plain, steady, a little dry. Uses `Curio.voice`,
scope = mode.
- welcomePlan (how): "Welcome to Reserve Designer. Click a cell to protect it, and read each species' row to see
  what it still needs."
- welcomeStress (how): "Stress test. Press Run fifty years. Each future loses one protected cell."
- welcomeGroups (how): "Groups. Move the herd size slider and watch how many eyes are on the lookout."
- farmChoice (how, first farm cell): "Farm land. Keep it farming, or pay a little more to restore it to meadow."
- crossing (how, first highway cell): "A wildlife crossing lets animals over the highway. It's not cheap."
- allSix (event, every time all six become met; stale on any change that breaks one): "All six species have what
  they need. Now see if it holds up. Try a stress test."
- stressDone (event, each run; stale on Back to plan): "Fifty years tested. The cracked cells are your weak links."
- overBudget (how, first refused buy): "That's over budget. Sell a cell or pick a cheaper one."

## Family engine
none. Map and rules are tool-local code (a small grid and flood-fill). No randomness.

## Sources
- Habitat fragmentation, edge effects, corridors and reserve design: OpenStax Biology 2e, sections 47.2 and 47.3
  (CC BY 4.0), https://openstax.org/books/biology-2e/pages/47-3-preserving-biodiversity (checked 2026-10-27).
- Elk vigilance falls as group size rises: Childress, M. J. and Lung, M. A. (2003), "Predation risk, gender and
  the group size effect", Animal Behaviour 66(2):389-398. "Many eyes" model: Pulliam, H. R. (1973), "On the
  advantages of flocking", Journal of Theoretical Biology 38:419-422 (the 20 percent watch time is a model value).
- Prairie dog colonies and predator-specific alarm calls: National Park Service, Wind Cave National Park,
  "Prairie Dogs" (https://www.nps.gov/wica/learn/nature/prairie-dogs.htm); Slobodchikoff et al. (1991), Animal
  Behaviour 42:713-719 (verify checks the NPS page).
- Elk seasonal migration between high summer range and lower winter range: National Park Service, Rocky Mountain
  National Park, "Elk" (https://www.nps.gov/romo/learn/nature/elk.htm).
- Wood frogs breed in small woodland pools and live in nearby forest: USGS, "Wood frog" fact sheet, Northern
  Prairie Wildlife Research Center (verify confirms the page).
- Black bears need large home ranges: National Park Service, "Black Bears" (https://www.nps.gov/subjects/bears).
- Ovenbird as a forest-interior bird sensitive to fragmentation: Cornell Lab of Ornithology, All About Birds,
  "Ovenbird" (https://www.allaboutbirds.org/guide/Ovenbird).
- Wildlife crossings on Colorado State Highway 9 cut wildlife-vehicle collisions by about 90 percent: Colorado
  Department of Transportation, "State Highway 9 Wildlife Crossings" (verify must confirm the figure before it
  ships; if not confirmed, the tip says "sharply" with no number).
- Map, prices, budget and species thresholds: model values; plans above checked in Python (Curio Class,
  2026-10-27).

## Done when
1. The empty map shows all six species unmet; protecting the $2,950k cheapest plan meets all six and shows
   $1,050k left.
2. Stress test on that plan reports "All six kept in 0 of 14 futures"; the $4,000k plan above reports 14 of 19 and
   marks exactly five weak cells.
3. A fifth Restore to meadow is refused with the 16 farms reason (Buy and farm on is always allowed, since the
   farm keeps farming); overspending is refused with the amount.
4. A river cell counts only when a bank beside it is protected; the bridge links north and south only when the river
   cells above and below it count.
5. Groups: herd size 10 reads 89 percent; the alarm call makes the whole colony dive.
6. Copy plan code then Load plan code restores the same plan.
7. Every cell reachable and buyable by keyboard with a spoken name; protected cells have the double outline and flag.
8. Main controls visible at 1366x768 and 680x425; the map fits at 375 wide (cells at least 26 px).
9. Each how-to line speaks once in five repeated actions; allSix speaks each time all six become met.
10. No network, no em dashes.

## Open questions
- [reserve-designer] The budget is $4,000k so a refined plan can reach 14 of 19 futures (at $3,000k the best plan
  found kept all six in no single-loss future). Keep $4,000k, or make the budget a teacher setting?
- [reserve-designer] The Colorado SH 9 crossing figure needs a source check; if verify cannot confirm it, the tip
  goes vague. OK?
