# Layers and Scales

## One idea
The student opens on two maps of the same U.S. county data (median household income) that tell opposite stories because their class breaks differ, and is asked "Which map is lying?"; then they build real thematic maps themselves from bundled public data (median income, average yearly rainfall, the share of people who speak a language other than English at home) by choosing the map type (choropleth, graduated dot, proportional symbol), the number of classes and the break method (equal interval, quantile, natural breaks) while a small histogram shows where the breaks fall; they zoom the same variable from world (countries) to United States (states) to one state (counties) and watch averages hide or reveal patterns; in a place case they stack a map with Landsat images and photographs to explain one place's economy and politics (the Mississippi River delta, the Laredo and Nuevo Laredo border crossing, the iron mining towns of Minnesota's Mesabi Range); at the end they publish one map with an honest legend and a sentence about what changes at another scale, so a ninth grader learns to make maps that show spatial patterns, to use maps and images to explain a place, and to see how patterns vary with scale.

## Not like
- region-compare (6, spec): regions compared with charts. Here maps the student builds.
- me-on-the-map (K, live): scale for a kindergartner. Here scale changing a pattern.
- where-s-my-phone-from (10, concept): flows of goods. Here thematic maps of places.
- expansion-map (8, spec): borders over time. Here data across space.

## Who and how
- Grade 9, Social Studies (Geography), module "Layers and Scales". Standards: D2.Geo.1.9-12 (use geospatial and related technologies to create maps to display and explain the spatial patterns of cultural and environmental characteristics), D2.Geo.2.9-12 (use maps, satellite images, photographs, and other representations to explain relationships between the locations of places and regions and their political, cultural, and economic dynamics), D2.Geo.3.9-12 (use geographic data to analyze variations in the spatial patterns of cultural and environmental characteristics at multiple scales).
- Format: map. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- The lying-maps opener, the map builder, the scale zoom, three place cases, the publish card. Extra: Mislead on purpose (the student makes a map that misleads with true data, prints it, and classmates spot the trick). tool.json `modes: ["Map studio", "Mislead on purpose"]`, `minutes: "30-40"`, `grades_label: "Grade 9"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.1.9-12 | Build a map: pick variable, type, classes and break method, then publish with an honest legend | the map redrawing; the histogram with break lines; the legend | 2, 5 |
| D2.Geo.3.9-12 | Zoom one variable from world to nation to counties and note what appears or vanishes | the same variable at three scales; the scale note | 3 |
| D2.Geo.2.9-12 | In a place case, stack map, Landsat image and photo, and write a caption on the place's economy and politics | the stacked layers; the caption card | 4 |

## Screens and modes
Header (kit): title "Layers and Scales"; `Map studio`, `Mislead on purpose`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Two maps of U.S. counties side by side, both median household income from the same Census survey. The left uses equal-interval breaks and looks mostly pale; the right uses quantile breaks and looks evenly split. The welcome is queued (`welcomeAfter: true`): "Same data, two maps, two stories. Which one is lying? Tap the map you trust more." First hint: "Tap a map." After the tap: "Neither is lying. Each one made a choice. Let's see the choices." Both histograms appear under the maps, showing where each set of breaks falls.

**The map builder (focus: the map and the controls, D2.Geo.1.9-12).** At 1366x768 the map fills the left with controls and the histogram right; at 680x425 the controls are a sheet.
- Variables: median household income (Census American Community Survey, 2018 to 2022), average yearly rainfall (NOAA climate normals, 1991 to 2020), share of people age 5 and up who speak a language other than English at home (ACS), and at world scale income per person (World Bank) and yearly rainfall (World Bank climate data).
- Map types: choropleth (shaded areas), graduated dots, proportional symbols. A note when a choice fits poorly (raw counts on a choropleth make big counties look important).
- Classes: 3 to 7. Break methods: equal interval, quantile, natural breaks. The histogram shows each break line as it moves.
- The legend writes itself from the choices and shows the units, the source and the year.

**The scale zoom (D2.Geo.3.9-12).** One variable at three scales: world (countries), United States (states), one state (counties, the student picks the state). A scale note asks: "What pattern did you see at the bigger scale that disappeared at the smaller one, or the other way?" Examples ready if the student is stuck: a state's average income hides a rich suburb and a poor rural county next door; a country's average rainfall hides a desert and a rainforest.

**Place cases (D2.Geo.2.9-12).** Three highlighted places, each with a map layer, a Landsat image and public domain photographs:
1. The Mississippi River delta, Louisiana: land loss on Landsat images from the 1980s to today; ports, oil and gas, fishing; levees and who decides where to build them.
2. Laredo, Texas, and Nuevo Laredo, Mexico: the busiest land port for trade between the two countries; bridges, rail yards and truck lines on the image; a border running through one metro area.
3. The Mesabi Range, Minnesota: open-pit iron mines on the image; towns that rose and shrank with steel; jobs and environmental rules argued in elections.
The student stacks the layers, slides opacity between them, and writes a two-line caption on how the place's location shapes its economy and its politics.

**Publish (the aha).** The student picks one map they made, checks the legend (title, units, source, year, break method), and writes one sentence: "At ___ scale this map shows ___; at ___ scale it would show ___." Narrator: "Every map is a set of choices. An honest one tells you what they were."

**The end.** The published map, the scale note and the caption. `Print` prints them.

**Mislead on purpose (extra).** The student uses true data and picks breaks, colors or a scale to make a misleading map, prints it with a hidden answer, and classmates find the trick.

## Content
- Bundled offline data: U.S. county and state boundaries (Census cartographic boundary files, simplified), world country boundaries (Natural Earth), ACS income and language tables, NOAA rainfall normals by county, World Bank country values; each with year and source in the legend.
- Three place cases with Landsat images (USGS, public domain) and photographs (public domain, checked at build).
- No network requests; data is trimmed to what the maps need.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Every control redraws the map at once; the histogram's break lines move with it.
- Hovering or focusing an area shows its name and value.
- Keyboard: Tab to the variable, type, classes, method, scale and map areas; arrows move between areas; Enter picks.
- With Motion off maps redraw without fades and the zoom jumps between scales.

## Look
- Accent `--brand` #1f5f8b cartographer blue (header, controls, the legend frame); gold #f4c542 (the selected area, the active break); paper #eff5f9; ink #0a1d2b; muted #4d5963.
- Contrast (WCAG 2.1, computed): white on brand 6.84:1; brand on paper 6.23:1; ink on paper 15.61:1; muted on paper 6.53:1; ink on gold 10.55:1.
- Map ramps: single-hue sequential ramps checked for color-vision deficiency; never red-green.
- Never color alone: every area's value shows on hover and focus; the legend lists ranges in words and numbers; dot and symbol maps use size.
- Different from this batch (ochre, mill soot, Atlantic indigo, field olive).

## Art
- Public domain: Landsat images from USGS EarthExplorer and NASA Earth Observatory for the three places; photographs from the Library of Congress and USGS for each place (ids checked at build). Each with credit.
- Drawn in code: every map, the histogram, the legend.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `bright-teacher` as the narrator and hints; `casual-peer` as a fellow student in the opener and the Mislead on purpose mode. `Curio.voice` with `scope: () => state.mode + ':' + state.view + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, the opener's reveal.
- how `build`: "Pick a variable, a map type, classes and a break method."
- how `zoom`: "Zoom to the next scale, then note what changed."
- how `place`: "Stack the layers, then write your caption."
- how `publish`: "Check your legend, then finish the scale sentence."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the map renderer (choropleth, dots, symbols), the break methods and histogram, the scale zoom, the layer stack, the legend writer, the publish card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Publish | Leave the legend defaults | The legend check wants a title and a break method the student names; Print waits. |
| Scale note | Write the same thing for every scale | The note must name two scales and one pattern that differs. |
| Caption | Describe only the picture | The caption must name one economic and one political link to location. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). The opener reveal (whole).
2. `build`.
3. `zoom`.
4. `place`; `publish`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.1.9-12, D2.Geo.2.9-12 and D2.Geo.3.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| County median household income and language spoken at home (ACS 2018 to 2022 5-year) | U.S. Census Bureau, data.census.gov tables B19013 and S1601 | U.S. Census Bureau, ACS handbook | yes |
| Rainfall normals, 1991 to 2020 | NOAA National Centers for Environmental Information, U.S. Climate Normals | NOAA Climate.gov, "Climate normals" | yes |
| Class breaks (equal interval, quantile, natural breaks) change what a map shows | Monmonier, "How to Lie with Maps" (Chicago, 3rd ed., 2018) | Brewer, "Designing Better Maps" (Esri Press, 2005) | yes |
| Patterns change with scale and area units (the modifiable areal unit problem) | Openshaw, "The Modifiable Areal Unit Problem" (1984) | Esri GIS Dictionary, "MAUP" | yes |
| Mississippi delta land loss | USGS, "Land area change in coastal Louisiana" (2017) | NASA Earth Observatory, delta images | yes |
| Laredo is the busiest U.S. land port for trade with Mexico | U.S. Bureau of Transportation Statistics, TransBorder freight data | U.S. Census Bureau, USA Trade port rankings | yes |
| Mesabi Range open-pit iron mining | Minnesota Department of Natural Resources, "Iron Range" | USGS, mineral resources | yes |
Backed twice: 8. Cut: 0.

Checks run (Python, scratchpad r17, 2026-11-09): on a test set of 20 values, quantile breaks with 5 classes put 4 values in each class and equal-interval breaks span equal widths; three scales and three place cases; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and controls; at 680x425 sheet.
2. The builder redraws with each type, class count and break method, and the histogram shows the breaks. (D2.Geo.1.9-12)
3. The zoom shows one variable at three scales with a scale note. (D2.Geo.3.9-12)
4. Each place case stacks map, Landsat image and photo with a caption. (D2.Geo.2.9-12)
5. Publish checks the legend and the scale sentence, then prints. (D2.Geo.1.9-12)
6. Mislead on purpose prints a map with its hidden answer.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no fades; no network requests; all data bundled.

## Open questions
None.
