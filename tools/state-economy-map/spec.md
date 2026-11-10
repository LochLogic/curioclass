# State Economy Map

## One idea
The child taps their own state on a U.S. map and stacks real data layers on it (land and water, then crops and livestock, mines and forests, factories, ports and rail, tech and tourism), uses a cluster finder to spot where jobs bunch together and link each bunch to the land or route that explains it (dairies near grass and water, a factory town on a river and a railroad, a port city on the coast), follows trade arrows from the state's top products out to the other states and countries that buy them and back for the goods the state buys, and flips a then-and-now toggle to see how the state's jobs changed since 1990, so a fourth grader learns why a state makes a lot of a few things and trades for the rest, and how ties to near and far places change what a state does.

## Not like
- three-towns (2, spec): three made-up kinds of community. Here the child's real state with real data.
- colonial-trade-routes (5, concept): trade in the colonial past. Here trade today.
- state-quest (concept): where places in the state are. Here what the state makes and why.
- learn-and-earn (4, spec, this batch): one person's skills and pay. Here a whole state's specialties.

## Who and how
- Grade 4, Social Studies (Economics and Geography), module "State Economy and Resources". Standards: D2.Eco.4.3-5 (explain why individuals and businesses specialize and trade), D2.Geo.11.3-5 (describe how the spatial patterns of economic activities in a place change over time because of interactions with nearby and distant places).
- Change from the module codes: the module lists D2.Geo.9.3-5 (catastrophic events and migration), which a jobs map doesn't teach; it moves to settle-the-valley (which teaches it with a flood year), and this tool teaches D2.Geo.11.3-5 instead, as the idea card proposes (see Open questions).
- Driver: one child alone, or the teacher on the projector (tool.json `driver: "either"`). `Read` reads every label. Controls 44 px or more.
- Four parts: Land, Layers and clusters, Trade, Then and now; then "My state's specialty" card. Extra: Compare two states. tool.json `modes: ["My state", "Compare"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.4.3-5 (specialize) | Turn on layers and use the cluster finder; link each cluster to a resource or route | job clusters ringed on the state map, each tied to a land feature | 2, 3 |
| D2.Eco.4.3-5 (trade) | Tap the state's top three products to send trade arrows out, then tap `What comes back?` | arrows to the top buying states and countries, and arrows in for top bought goods | 4 |
| D2.Geo.11.3-5 | Flip `1990` and `Now` on the jobs layers and pick which change came from ties to other places | two maps with the biggest job changes marked; cause cards (new trade partners, a new highway, factories moving away, more visitors) | 5 |

## Screens and modes
Header (kit): title "State Economy Map"; `My state`, `Compare`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A U.S. map with state outlines and names. The welcome is queued (`welcomeAfter: true`): "Every state makes some things better than others. Tap your state to find out what yours makes, and why." First hint: "Tap your state." Tapping a state zooms in with the Land layer on (mountains, rivers, lakes, coast, flat farmland, forests). A `Change state` button stays in the corner.

**Layers and clusters (focus: the state map and a layer stack).** At 1366x768 the map fills the left two thirds and the layer stack sits right; at 680x425 the stack becomes a bottom bar of icons with words.
- Layers, each a toggle with an icon: Crops and livestock; Mines and forests; Factories; Ports and rail; Tech and offices; Tourism. Each shows county-level dots sized by jobs (data in Build notes).
- Cluster finder: after two layers are on, `Find a cluster` rings the state's biggest bunch on an open layer and asks "Why are so many of these jobs here?" with three reason cards built from the land and route data under it (one right: "Flat land and lots of rain for crops", "A deep harbor for ships", "Two highways and a rail line meet here", "Mountains with coal and timber", "Lakes and beaches visitors love", "A big university nearby"). The child finds three clusters.
- A wrong reason: the Land layer flashes under the cluster and the narrator names what's there.

**Trade (focus: arrows).** The state's top three products (by export value, or farm sales where those lead) appear as cards. Tapping one sends arrows to its top three buyers (other countries from export data; for farm goods that mostly sell inside the U.S., the narrator says "Most of this is sold to other states"). `What comes back?` shows the state's top three bought goods with arrows in from their top sources. Narrator: "Your state makes a lot of a few things and sells them. Then it buys the things others make better or cheaper."

**Then and now (focus: two maps).** `1990` and `Now` flip the jobs layers. The two biggest changes (one up, one down) get gold rings. For each, the child picks a cause from four cards; the right ones come from the build's data notes for that state (for example, "Factories moved to other countries", "A new interstate brought warehouses", "More visitors from other states", "New trade with other countries").

**My state's specialty (end state).** A card the child fills with taps and tiles: "We make a lot of ___ because ___. We sell it to ___. We buy ___ from ___." `Print` prints the card with the state map and arrows.

**Compare (extra).** Two states side by side with the same layer on; the narrator reads one difference.

## Build notes
- Data (one file per state, built from public sources and dated in the credits): county jobs by industry from the U.S. Bureau of Labor Statistics Quarterly Census of Employment and Wages (1990 and the latest year); farm products from the USDA National Agricultural Statistics Service state agriculture overviews; state exports by product and partner country from the U.S. Census Bureau's state export data; imports by product from the same source where available; land and water from USGS and NOAA base maps.
- For each state the build writes three cluster reasons, the top three products and buyers, and the 1990-to-now change notes with their sources. Industry groups are kid-named (for example "Factories" for manufacturing).
- If a state's data is suppressed in a county (small counts), that county shows no dot and the legend says "not shown to keep businesses private".

## Content
- 50 states and the District of Columbia; six job layers plus Land; three clusters, three products and three bought goods per state; two then-and-now changes per state with cause cards; the specialty card.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Find a cluster` shows only after two layers are on. `What comes back?` shows only after a product's arrows. `1990` and `Now` show only in Then and now.
- Keyboard: Tab through states (alphabetical), Enter to open; number keys 1 to 6 toggle layers.
- With Motion off the zoom and arrows appear without moving.

## Look
- Accent `--brand` #1a5276 map blue (header, state outline, arrows); gold #f4c542 (a ringed cluster, the selected product, change rings); paper #eef4f9; ink #08192a; muted #4c5866.
- Contrast (WCAG 2.1, computed): white on brand 8.36:1; brand on paper 7.54:1; ink on paper 16.02:1; muted on paper 6.54:1; ink on gold 10.92:1.
- Never color alone: each layer has its own icon shape for dots; arrows out and in are labeled "We sell" and "We buy".
- Different from this batch (inquiry rust, learn-and-earn teal, made-for-whom slate, bill maroon).

## Art
- Drawn in code from data: all maps, dots, rings and arrows (data-accurate, per the idea card).
- Local FLUX (`scripts/localart.py`): six layer icons and twelve product icons (18, 1:1, flat style).
About 18 images. No people art.

## Voice
One bank voice, unique in this batch: `knowing-guide` as the narrator. `Curio.voice` with `scope: () => state.mode + ':' + state.state + ':' + state.part`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, the state's name and its land line.
- how `layers`: "Turn on two layers to see where jobs are."
- how `cluster`: "Tap Find a cluster."
- event, whole, each reason's yes or the land line.
- how `trade`: "Tap a product to see who buys it."
- event, whole, `trade-sum`.
- how `then`: "Tap 1990 and Now to see how jobs changed."
- how `card`: "Fill in your state's specialty card."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: a state map renderer with county dot layers, the cluster finder, trade arrows, the then-and-now flip and the specialty card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Clusters | Pick the first reason | Reasons are shuffled and only one fits the land under the cluster. |
| Then and now | Pick any cause | Cause cards come from the state's notes; wrong ones flash the map that shows why not. |
| Specialty card | Fill tiles at random | Tiles come only from the child's own clusters and arrows. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). State: name and land line (whole).
2. `layers`; `cluster`; reasons (whole).
3. `trade`; arrows; `trade-sum` (whole).
4. `then`; causes (whole); `card`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.4.3-5 and D2.Geo.11.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| County jobs by industry for 1990 and now are published for every state | U.S. Bureau of Labor Statistics, Quarterly Census of Employment and Wages (data files) | U.S. Census Bureau, County Business Patterns | yes |
| State farm products and sales are published for every state | USDA National Agricultural Statistics Service, State Agriculture Overview | USDA Economic Research Service, farm income by state | yes |
| State exports by product and partner country are published | U.S. Census Bureau, state exports data (USA Trade Online) | International Trade Administration, TradeStats Express by state | yes |
| Places specialize in what their resources and skills help them make well, and trade for the rest | Federal Reserve Bank of St. Louis, Econ Lowdown, "Specialization and trade" | Council for Economic Education, Voluntary National Content Standards in Economics, Standards 5 and 6 | yes |
| Jobs cluster near resources and transport routes such as ports, rivers and highways | National Geographic Education, "Economic activity and location" | U.S. Economic Development Administration, cluster mapping (Harvard Business School U.S. Cluster Mapping) | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r7, 2026-11-09): the layer list has six job layers plus Land; each state record needs three clusters, three products and three bought goods, and two changes; the data file schema check is a Done when item for build; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and stack fit; at 680x425 the stack is a bottom bar.
2. Every state opens with Land and six job layers from the dated data. (D2.Eco.4.3-5)
3. Each state's three clusters accept only the reason that fits the land under them. (D2.Eco.4.3-5)
4. Trade arrows show top buyers and top bought goods for the state. (D2.Eco.4.3-5)
5. Then and now shows two marked changes with source-backed causes. (D2.Geo.11.3-5)
6. The data credits show each source and year; suppressed counties say why.
7. `Find a cluster`, `What comes back?`, `1990` and `Now` are never named before they show.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no zoom or arrow motion; no network requests (data ships with the tool).

## Open questions
- The module lists D2.Geo.9.3-5, which this tool doesn't teach (default used: teach D2.Geo.11.3-5 here and D2.Geo.9.3-5 in settle-the-valley, as the idea card proposes; the module code list is Cory's to update).
