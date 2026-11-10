# Region Compare

## One idea
The child picks two world regions and a question card ("Why is South Asia crowded while North Africa is mostly empty?"), then lays real data on a world map one layer at a time (people per square kilometer, yearly rainfall, rivers, cropland, income per person, main languages, night lights), choosing for each layer how to show it (shaded map, bar chart or dot plot); a notebook asks one question per layer, and stacking rain, rivers and cropland over population shows the Nile valley and the Ganges plain pulling people in; at the end an "alike / different" board filled from the layers and one sentence on how land and water stretch or limit where people live, so a sixth grader learns to pick maps and charts that show a pattern, to compare places across cultural and environmental traits, and to explain how environment extends or limits settlement.

## Not like
- layers-and-scales (9, concept): class breaks and map scale. Here choosing a first chart or map for a layer.
- five-themes-field-trip (6, spec): one city up close. Here two whole world regions.
- where-s-my-phone-from (10, concept): trade data. Here people, land and culture.
- the-shrinking-lake (6, spec): change over time in one place. Here a snapshot of two regions.

## Who and how
- Grade 6, Social Studies (Geography), module "World Regions Today". Standards: D2.Geo.3.6-8 (use paper based and electronic mapping and graphing techniques to represent and analyze spatial patterns of different environmental and cultural characteristics), D2.Geo.8.6-8 (analyze how relationships between humans and environments extend or contract spatial patterns of settlement and movement), D2.Geo.10.6-8 (analyze the ways in which cultural and environmental characteristics vary among various regions of the world), D2.Geo.5.6-8 (analyze the combinations of cultural and environmental characteristics that make places both similar to and different from other places).
- Format: data. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- One question card (South Asia and North Africa) with seven layers, the notebook, the board and the sentence. Extra: More pairs (three more question cards: Western Europe and the Sahel, East Asia and Central Asia, the Andes and the Amazon). tool.json `modes: ["South Asia and North Africa", "More pairs"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.3.6-8 | For each layer, choose shaded map, bar chart or dot plot, and answer whether the choice shows the pattern | the layer drawn the chosen way; the notebook's "does this show it?" check | 2 |
| D2.Geo.8.6-8 | Stack rain, rivers and cropland over population and point to where people crowd and where land is empty | the stacked map with the Nile and Ganges bands lit; notebook question | 3 |
| D2.Geo.10.6-8 | Compare each layer's values for the two regions in the side-by-side table | the two-column table and bars | 4 |
| D2.Geo.5.6-8 | Drag each layer onto Alike or Different and write one sentence | the alike / different board; the sentence card | 5 |

## Screens and modes
Header (kit): title "Region Compare"; `South Asia and North Africa`, `More pairs`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A plain world map in light gray. A question card at the top: "Why is South Asia crowded while North Africa is mostly empty?" Two region pickers already set (South Asia; Middle East and North Africa, with North Africa outlined). A layer shelf down the side with seven layer tiles. The welcome is queued (`welcomeAfter: true`): "Here's a question about two parts of the world. Data can help answer it. Drag a layer onto the map to start." First hint: "Drag the People layer onto the map."

**Layers (focus: the map and the notebook).** At 1366x768 the map fills the center, the shelf left and the notebook right; at 680x425 shelf and notebook are sheets.
- People: people per square kilometer by country and a finer grid (South Asia among the most crowded regions on Earth, about ten times North Africa's average; figures from World Bank and NASA SEDAC, rounded, labeled "about").
- Rain: average yearly rainfall (monsoon rain over the Ganges plain; under 100 mm a year over most of the Sahara).
- Rivers: the Nile, Ganges, Indus and Brahmaputra drawn as blue lines.
- Cropland: share of land farmed.
- Income: income per person (GNI per capita, World Bank), shown by country.
- Languages: main languages by country (Hindi, Bengali, Urdu and many more in South Asia; Arabic across North Africa, with Berber languages), from the CIA World Factbook.
- Night lights: NASA Black Marble image, where lights trace the Nile like a thread.
- When a layer lands, a chooser asks how to show it: shaded map, bar chart (the two regions and their countries) or dot plot (each country as a dot). Some choices fit better: languages can't be a bar chart of numbers; the notebook says "Languages are names, not amounts. Try a map with labels."

**The notebook (one question per layer).** Examples: People: "Where are the darkest squares?" Rain plus People: "Do the crowded places get more rain?" Rivers plus People: "In Egypt, where do almost all the people live?" (answer: along the Nile, on a few percent of the land). Income: "Does more people mean more income? Look at both regions." (no: North Africa's average income is higher than South Asia's, which surprises many). Each answer is a tap on the map or a choice, with a reason line.

**The side-by-side table (D2.Geo.10.6-8).** A two-column table builds as layers are added: each layer's value for the two regions, with a small bar.

**The alike / different board (the aha).** The child drags each layer onto Alike or Different (and a "Both" lane for layers where parts match: rivers make the crowded strips in both regions; language families differ; deserts appear in both, the Thar and the Sahara). Then the sentence card: "People crowd where ___ and ___, and land stays empty where ___." (tiles plus a free line). Narrator: "Rivers and rain pull people in. Desert holds them back, unless a river runs through it."

**The end.** The stacked map, the table, the board and the sentence. `Print` prints them.

**More pairs (extra).** Three more question cards with the same layers.

## Content
- Seven layers for each region pair from bundled, rounded data tables (World Bank WDI, NASA SEDAC, CIA World Factbook, NASA Black Marble), seven notebook questions per pair, the board, three more pairs.
- All data are real and dated; each layer shows its source and year on the map.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Up to three layers stack at once; each has a show/hide eye and its own pattern.
- The chart chooser can be changed any time.
- Keyboard: Tab to the shelf, map regions, notebook and board; Enter to add a layer or pick; arrows move between countries on the map with the value read aloud.
- With Motion off layers appear without fading.

## Look
- Accent `--brand` #3b4a8c atlas indigo (header, shelf, notebook); gold #f4c542 (the active layer, the selected country); paper #f2f3f9; ink #0e1430; muted #535768.
- Contrast (WCAG 2.1, computed): white on brand 8.25:1; brand on paper 7.45:1; ink on paper 16.33:1; muted on paper 6.47:1; ink on gold 11.12:1.
- Never color alone: shaded maps use a single-hue light-to-dark scale with a labeled legend and the value on focus; stacked layers add dots, hatching or lines; board lanes carry words.
- Different from this batch (Atlantic ochre, lake jade, purple, red).

## Art
- Public domain: NASA Black Marble night lights (NASA Earth Observatory), with credit.
- Drawn in code: the world map from Natural Earth (public domain) outlines, all layers, charts, the table, the board.
- Local FLUX (`scripts/localart.py`): two photos for the notebook (the green Nile valley beside desert, a crowded Ganges plain town; 2, 3:2).
About 3 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the notebook; `bright-teacher` as the narrator. `Curio.voice` with `scope: () => state.mode + ':' + state.layer + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `layer`: "Drag a layer onto the map."
- how `show`: "Pick how to show it: map, bar chart or dot plot."
- event, whole, each notebook question and reason line.
- how `board`: "Drag each layer to Alike, Different or Both."
- how `sentence`: "Finish the sentence about where people crowd."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
data desk (`kit/data-desk.js`, described in full in docs/families/data-desk.md). This tool uses: `DataTable` for each region pair's country table, `t.where` for picking a region, `Chart` (`bar` and `dot`) for the chart choices, and `renderTable` for the side-by-side table. The shaded map, layer stacking, notebook, board and sentence are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Chart choice | Pick bar chart every time | Languages and rivers can't be bars; the notebook asks for another way. |
| Notebook | Tap anywhere on the map | Each answer checks the region tapped; a miss plays a pointer line ("Look along the river."). |
| Board | Put everything in Different | Each layer checks; rivers in Different plays "Look where people crowd in both." |
| Sentence | Leave blanks | Print waits for them. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `layer`; `show`.
2. Notebook question (whole), waits; reason line (whole).
3. `board`; `sentence`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.3.6-8, D2.Geo.8.6-8, D2.Geo.10.6-8 and D2.Geo.5.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| South Asia is far more densely peopled than the Middle East and North Africa | World Bank WDI, population density (EN.POP.DNST) by region | NASA SEDAC, Gridded Population of the World v4 | yes, figures rounded |
| Nearly all Egyptians live in the Nile valley and delta, a few percent of the land | Encyclopaedia Britannica, "Egypt: settlement patterns" | CIA World Factbook, Egypt (population distribution) | yes |
| Monsoon rain on the Ganges plain; under 100 mm a year over much of the Sahara | NOAA, "What is a monsoon?" and Britannica, "Ganges River" | Britannica, "Sahara: climate" | yes |
| North Africa's average income per person is higher than South Asia's | World Bank WDI, GNI per capita (Atlas method), by region | World Bank, regional country tables | yes |
| Main languages by country | CIA World Factbook, "Languages" field | Britannica country articles | yes |
| Night lights trace the Nile and the Ganges plain | NASA Earth Observatory, Black Marble (2016 and later) | NASA Worldview, VIIRS night lights | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r12, 2026-11-09): every layer has a value for both regions; at least one layer lands in each lane of the board's answer key (Alike, Different, Both); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 shelf, map and notebook; at 680x425 sheets.
2. Each layer can be shown three ways, with the notebook check. (D2.Geo.3.6-8)
3. Stacked rain, rivers and cropland over people light the river bands. (D2.Geo.8.6-8)
4. The side-by-side table fills. (D2.Geo.10.6-8)
5. The board and sentence check and print. (D2.Geo.5.6-8)
6. More pairs loads three new questions.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no fading; no network requests (all data bundled).

## Open questions
None.
