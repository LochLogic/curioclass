# Where's My Phone From?

## One idea
A phone comes apart on the screen into its battery, screen, chips, case and circuit board under the question "How many countries are in your pocket?"; the student picks a part and the data desk shows the real top producers and trade flows for what goes into it (cobalt and lithium for the battery, rare earths for the speaker and camera motors, tin and tantalum on the board, advanced chips, final assembly) as a flow map and a sortable table, and a year filter shows the chain shifting; three guided investigations pair data with a short human story: why factory workers migrate to assembly cities, why cobalt and tin regions see conflict as well as income, and who earns what share of the phone's price; at the end the student builds a one-chart answer to one question and writes a caption naming effects on growth, workers, rights and the environment in two countries, so a tenth grader learns how spreading manufacturing moves people, how scarce resources bring conflict and cooperation, and what globalization does to growth, labor, rights, the environment and income across nations.

## Not like
- trade-island (12, spec): a comparative advantage model. Here a real supply chain in data.
- layers-and-scales (9, spec): thematic maps of places. Here flows between places.
- region-compare (6, spec): region statistics side by side. Here one product's chain.
- factory-floor (9, spec): one mill in 1760 to 1900. Here a global chain today.

## Who and how
- Grade 10, Social Studies (Geography and Economics), module "Globalization Today". Standards: D2.Geo.7.9-12 (analyze the reciprocal nature of how historical events and the spatial diffusion of ideas, technologies, and cultural practices have influenced migration patterns and the distribution of human population), D2.Geo.11.9-12 (evaluate how economic globalization and the expanding use of scarce resources contribute to conflict and cooperation within and among countries), D2.Eco.15.9-12 (explain how current globalization trends and policies affect economic growth, labor markets, rights of citizens, the environment, and resource and income distribution in different nations).
- Format: data. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- The exploded phone, six parts with data, the flow map and table, three investigations, the one-chart answer. Extra: 2010 and today (the same phone chain in 2010 beside today's: where assembly and chips moved). tool.json `modes: ["Phone", "2010 and today"]`, `minutes: "30-40"`, `grades_label: "Grade 10"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.7.9-12 | In the assembly-city investigation, link factory growth to migration with the data and the worker's story | migrant worker numbers; the assembly map moving over years | 3 |
| D2.Geo.11.9-12 | In the minerals investigation, sort events into conflict and cooperation within and between countries | producer shares; the conflict and cooperation sort | 3 |
| D2.Eco.15.9-12 | In the value-share investigation and the one-chart answer, name effects on growth, workers, rights and the environment in two countries | the value-share bar; the student's chart and caption | 3, 4 |

## Screens and modes
Header (kit): title "Where's My Phone From?"; `Phone`, `2010 and today`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A phone in the center; tapping it pulls it apart into labeled parts. A counter reads "Countries found: 0." The welcome is queued (`welcomeAfter: true`): "How many countries are in your pocket? Pull a part out and follow it. Tap the phone." First hint: "Tap the phone."

**Parts and data (focus: the flow map and table).** At 1366x768 the map fills the left with the table and chart right; at 680x425 the table is a tab. Six parts:
1. Battery: cobalt (the Democratic Republic of the Congo mined about three-quarters of the world's supply in 2023) and lithium (Australia, Chile and China lead).
2. Speaker and camera motors: rare earths (China mined about two-thirds and refined most).
3. Circuit board: tin (China, Indonesia, Myanmar lead) and tantalum (the DRC and Rwanda lead).
4. Chips: the most advanced chips are made mostly in Taiwan; others in South Korea, China and the United States.
5. Screen and glass: made in South Korea, China and Japan.
6. Final assembly: mostly China, growing in India and Vietnam.
- Each part's data comes from a bundled table with year and source; the flow map draws arrows from mine to refinery to factory to assembly; the year filter shows shifts. The counter climbs as countries are found. All figures are rounded and labeled "about" with the year.

**Investigations (focus: the investigation card).** Each pairs a chart with a short human story (made for this game from reporting, labeled so):
1. Assembly cities (D2.Geo.7.9-12): China's migrant workers (about 290 million people working away from their home areas in 2023); the giant assembly plant in Zhengzhou; assembly moving to India and Vietnam. Story: a young worker from a farm province.
2. Minerals (D2.Geo.11.9-12): cobalt brings income and conflict in the DRC; artisanal mines where children have worked, reported by Amnesty International and UNICEF; conflict over tin and tantalum in eastern DRC; cooperation through rules (the U.S. Dodd-Frank Act's conflict-minerals rule, 2010; the EU's regulation, 2021; company audits). The student sorts events into conflict and cooperation, within and between countries. Story: a miner's family in Kolwezi, told without images of children working.
3. Who earns what (D2.Eco.15.9-12): a study of a 2010 phone found the brand kept about 58 percent of the price as profit while assembly labor in China got under 2 percent. The student reads the bar and answers who gains, then adds a line on what it means for workers and growth in two countries.

**The one-chart answer (the aha).** The student picks one question, builds one chart (bar, dot or line) from the bundled data, and writes a caption naming effects on growth, workers, rights and the environment in two countries. Narrator: "Your phone is a map of the world. So is who gets paid for it."

**The end.** The country count, the chart and the caption. `Print` prints them.

**2010 and today (extra).** The same chain in 2010 and today side by side.

## Content
- Six parts, about twelve bundled tables (USGS mineral producers, chip and assembly shares, migrant worker counts, value shares) with year and source, the flow map, three investigations with stories, the conflict and cooperation sort, the chart builder, the caption card.
- Stories are made up from reporting and labeled; figures are real, rounded, dated and sourced; data is bundled, with no network requests.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Parts open in any order; investigations open after three parts.
- The chart builder uses fixed axes so charts compare fairly.
- Keyboard: Tab to parts, the map, the table, filters, investigations and the chart builder; Enter to pick and place; arrows move the year filter.
- With Motion off the phone comes apart without moving and arrows appear without drawing.

## Look
- Accent `--brand` #43376b circuit violet (header, the table, the chart builder); gold #f4c542 (the part in hand, a found country); paper #f3f2f9; ink #130f26; muted #56536a.
- Contrast (WCAG 2.1, computed): white on brand 10.51:1; brand on paper 9.45:1; ink on paper 16.80:1; muted on paper 6.65:1; ink on gold 11.49:1.
- Never color alone: arrows carry labels and widths; table cells carry numbers; chart series carry names.
- Different from this batch (wallet maroon, workbench green, sea teal, terracotta).

## Art
- Drawn in code: the exploded phone, the flow map, the table, every chart.
- Local FLUX (`scripts/localart.py`): a copper and cobalt mine, wide view, no children (1, 16:9); a chip fab clean room (1, 16:9); an assembly floor (1, 16:9).
- People art goes to Gemini with `people: true`: the assembly worker, the miner, the miner's spouse (3; cutout yes; adults only).
About 6 images.

## Voice
Two bank voices, each unique in this batch: `upbeat-guide` as the narrator and hints; `bright-teacher` as the reader of investigation stories and data notes. `Curio.voice` with `scope: () => state.mode + ':' + state.part + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each part's data note.
- how `part`: "Pull out a part and follow its arrows."
- event, whole, each investigation story.
- how `sort`: "Sort each event into conflict or cooperation."
- how `chart`: "Build one chart that answers your question."
- how `caption`: "Name effects in two countries in your caption."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
data desk (`kit/data-desk.js`, described in full in docs/families/data-desk.md). This tool uses: `DataTable` for each part's producer table and the investigation tables, `t.where` for the year filter, `Chart` (`bar`, `dot` and `line`, with fixed `xDomain` and `yDomain`) for the investigations and the one-chart answer, and `renderTable` for the sortable table. The exploded phone, the flow map, the conflict and cooperation sort and the caption card are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Put everything under conflict | Each event checks; the Dodd-Frank rule under conflict plays a reason line. |
| Chart | Pick any chart | The chart's variables must match the chosen question. |
| Caption | Name one country | The caption needs two countries and at least two of growth, workers, rights, environment. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `part`; data note (whole).
2. Investigation story (whole), waits; `sort` in the minerals investigation.
3. `chart`; `caption`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.7.9-12, D2.Geo.11.9-12 and D2.Eco.15.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Cobalt: the DRC mined about three-quarters of world supply in 2023 | USGS, Mineral Commodity Summaries 2024, "Cobalt" | International Energy Agency, Global Critical Minerals Outlook 2024 | yes |
| Lithium led by Australia, Chile and China; rare earths about two-thirds from China | USGS, Mineral Commodity Summaries 2024 | International Energy Agency (2024) | yes |
| Most advanced chips are made in Taiwan | U.S. Department of Commerce, semiconductor supply chain review (2021) | Semiconductor Industry Association and Boston Consulting Group, "Strengthening the Global Semiconductor Supply Chain" (2021) | yes |
| About 290 million migrant workers in China in 2023 | National Bureau of Statistics of China, Migrant Worker Monitoring Report 2023 | International Labour Organization, China country notes | yes, rounded |
| Children in artisanal cobalt mining in the DRC | Amnesty International, "This Is What We Die For" (2016) | UNICEF and U.S. Department of Labor, "List of Goods Produced by Child Labor" | yes |
| Conflict minerals rules: Dodd-Frank Section 1502 (2010), the EU regulation (2021) | U.S. Securities and Exchange Commission, conflict minerals rule | European Commission, Conflict Minerals Regulation | yes |
| Value shares of a 2010 phone: brand about 58%, China assembly labor under 2% | Kraemer, Linden and Dedrick, "Capturing Value in Global Networks" (2011) | OECD, "Interconnected Economies" (2013), citing the same study | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: child labor in artisanal mining is named with sources and shown through an adult family's story, never through images of children working; conflict in eastern DRC is told plainly. A fresh-agent read of the minerals investigation is needed before build.

Checks run (Python, scratchpad r18, 2026-11-09): producer shares in each table sum to 100 percent or less with "rest of world"; six parts with at least two countries each; the 2010 value shares add to 100 percent with the other parts; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and table; at 680x425 tab.
2. Each part shows producers and flows with year and source, and the counter climbs.
3. Three investigations run with data and stories, and the sort checks. (D2.Geo.7.9-12, D2.Geo.11.9-12, D2.Eco.15.9-12)
4. The one-chart answer and caption name effects in two countries. (D2.Eco.15.9-12)
5. Charts use fixed axes from the data desk engine.
6. 2010 and today compares the chains.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no moving parts; no network requests; data bundled.

## Open questions
- Sensitivity flag: child labor in artisanal cobalt mining and conflict over minerals (default used: named with sources, told through an adult family's story, no images of children working, fresh-agent read before build).
