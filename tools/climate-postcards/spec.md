# Climate Postcards

## One idea
A world map holds six pins (Phoenix, Seattle, Singapore, Anchorage, Nairobi, Buenos Aires) and a blank postcard asks "What should you pack for July?"; the student opens a city's real monthly averages, builds a bar graph of rain and a line graph of temperature, reads the typical weather for a season off the graph and packs a suitcase for that month, then lays two cities side by side; map layers (distance from the equator, height above the sea, nearness to the ocean, mountains) help the student pick why each climate is the way it is, such as Nairobi staying mild near the equator because it sits high up, or Buenos Aires having winter in July because it is south of the equator; each city has one weather hazard (extreme heat, flash floods, heavy rain and landslides, blizzards), and the student compares two or three designs that reduce the harm (cooling centers and shade trees, bigger drains and rain gardens, warming shelters and snow routes) and makes a claim about which helps most and what it costs; at the end six postcards each hold a graph, a climate description, a reason and a hazard claim, so a third grader learns to graph data to describe the weather a season brings, to describe climates around the world and why they differ, and to judge a design that reduces a weather hazard.

## Not like
- weather-wardrobe (K, spec): daily weather at home, same engine. Here monthly averages around the world.
- ocean-conveyor (6, concept): currents and climate. Here graphs and places.
- map-maker (3, spec): making maps. Here reading data on a map.
- fossil-clues (3, spec): how a place changed over millions of years. Here what a place is like each year.

## Who and how
- Grade 3, Science and Social Studies, module "Weather and Climate". Standards: 3-ESS2-1 (represent data in tables and graphical displays to describe typical weather conditions expected during a particular season), 3-ESS2-2 (obtain and combine information to describe climates in different regions of the world), 3-ESS3-1 (make a claim about the merit of a design solution that reduces the impacts of a weather-related hazard), D2.Geo.10.3-5 (explain why environmental characteristics vary among different world regions).
- Format: data. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six cities with twelve months each, two graphs per city, the suitcase, the side-by-side view, four map layers, six hazards with designs, six postcards. Extra: Class trip (the class picks a city and packs together). tool.json `modes: ["Postcards", "Class trip"]`, `minutes: "25-35"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3-ESS2-1 | Build rain and temperature graphs from a table and pack for a month | the two graphs; the suitcase | 2 |
| 3-ESS2-2 | Compare two cities and write each climate on its postcard | the side-by-side view; the postcard | 3 |
| D2.Geo.10.3-5 | Turn on map layers and pick the reason each climate differs | the map layers; the reason card | 3 |
| 3-ESS3-1 | Compare designs for a city's hazard and make a claim with cost | the design cards; the claim | 4 |

## Screens and modes
Header (kit): title "Climate Postcards"; `Postcards`, `Class trip`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A world map with six pins and a blank postcard with a stamp. The welcome is queued (`welcomeAfter: true`): "You're going on a trip! Pick a city. What should you pack for July? Tap a pin." First hint: "Tap a pin on the map."

**A city (focus: the graphs).** At 1366x768 the graphs fill the left with the table and suitcase right; at 680x425 the table is a sheet. The student drags each month's rain into bars and taps each month's temperature to build the line. Then a season card ("July", "January") asks what the weather is usually like; the answer comes from reading the graph. The suitcase offers clothes and gear, and packing must match the graph (a raincoat for a wet month, shorts for a hot one).

**Side by side.** Two cities' graphs line up. Questions: "Which city is wet all year?" (Singapore), "Which has dry summers and wet winters?" (Seattle), "Why is July cold in Buenos Aires?"

**Why (D2.Geo.10.3-5).** Four map layers: distance from the equator, height above the sea, nearness to the ocean, mountains. The student turns them on and picks a reason for each city. Nairobi and Singapore are both near the equator, but Nairobi sits high up and stays mild. Anchorage is far from the equator. Seattle is near the ocean and has mild, rainy winters.

**Hazards (3-ESS3-1).** Each city has one hazard: Phoenix, extreme heat; Singapore, flash floods; Seattle, heavy winter rain and landslides; Anchorage, blizzards and deep cold; Nairobi, flash floods in the rainy seasons; Buenos Aires, storm flooding. Two or three designs each show what they do, what they cost (low, medium, high) and who they help. The student makes a claim: "The best design for ___ is ___ because ___."

**The postcards (the aha).** Six postcards, each with a graph, the climate in words, the reason and the hazard claim. Narrator: "Weather is today. Climate is what a place is like year after year. And where a place sits on Earth explains a lot of it."

**The end.** The stack of postcards. `Print` prints them as real postcards to cut out.

**Class trip (extra).** The class picks a city and packs together.

## Content
- Six cities with twelve monthly normals each (average high, average low, rain), four map layers, six hazards with designs and costs, the postcard template.
- Normals are bundled in the data block; no network.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Bars and points snap to the table value; a wrong value shows the table row to check.
- Keyboard: Tab to pins, table rows, bars, the suitcase, layers, designs and the postcard; arrow keys set a bar; Enter picks.
- With Motion off graphs draw at once and the postcard does not flip.

## Look
- Accent `--brand` #a3461a postcard orange (header, the stamp, rain bars); gold #f4c542 (the city in focus, the packed item); paper #fdf4ee; ink #2a1206; muted #5f534c.
- Contrast (WCAG 2.1, computed): white on brand 6.09:1; brand on paper 5.61:1; ink on paper 16.29:1; muted on paper 6.84:1; ink on gold 10.87:1.
- Never color alone: bars and the line carry numbers and a key in words; layers carry names.
- Different from this batch (magnet red, collar green, ocean navy, lane indigo).

## Art
- Local FLUX (`scripts/localart.py`): a postcard scene for each city (6, 3:2), six hazard designs (6, 4:3).
- Drawn in code: the world map and layers, the graphs, the suitcase and clothes, the postcard frame.
About 12 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the weather reporter; `warm-teacher` as the guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.city + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `graph`: "Drag each month's rain to make a bar."
- how `pack`: "Drag clothes into the suitcase for this month."
- how `compare`: "Tap a second pin to compare."
- how `why`: "Turn on a layer, then pick the reason."
- how `hazard`: "Pick the design you think helps most and say why."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
weather (family "weather"). Reuses weather-wardrobe's `/* WEATHER DATA: begin */ ... /* end */` block (the recorded-month format and the graph pieces) and adds monthly normals for six cities, a line graph and the map layers inside it.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Graphs | Drag bars anywhere | Each bar checks against the table value. |
| Packing | Pack everything | The suitcase holds six items and each must match the month. |
| Reasons | Pick the same reason for every city | Each reason checks against that city's layers. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `graph`; `pack`.
2. `compare`; `why`.
3. `hazard`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 3-ESS2-1, 3-ESS2-2, 3-ESS3-1 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| C3 wording for D2.Geo.10.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Monthly normals for Phoenix, Seattle, Anchorage | NOAA National Centers for Environmental Information, U.S. Climate Normals 1991-2020 | National Weather Service local office climate pages | yes |
| Monthly normals for Singapore, Nairobi, Buenos Aires | World Meteorological Organization, Climate Normals 1991-2020 | each country's weather service (Meteorological Service Singapore, Kenya Meteorological Department, Servicio Meteorologico Nacional) | yes |
| Height above the sea cools a place; Nairobi sits about 1,800 meters up | NOAA, "Climate and elevation" (Climate.gov) | Encyclopaedia Britannica, "Nairobi" | yes |
| Cooling centers, shade trees, drains and rain gardens reduce weather harm | U.S. Environmental Protection Agency, "Heat island reduction" and "Green infrastructure" | National Weather Service, "Heat safety" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r28, 2026-11-09): Singapore (1.35 degrees north) and Nairobi (1.29 degrees south) are both within 1.5 degrees of the equator; Buenos Aires (34.6 south) and Phoenix (33.4 north) differ by 1.2 degrees in distance from the equator; Anchorage (61.2 north) is farthest; six cities with twelve months is 72 rows; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 graphs and table; at 680x425 sheet.
2. Rain and temperature graphs are built from real normals and a suitcase is packed for a month. (3-ESS2-1)
3. Two cities are compared and each climate is described with a reason from the map layers. (3-ESS2-2, D2.Geo.10.3-5)
4. A design claim is made for each hazard with its cost. (3-ESS3-1)
5. Normals match the cited 1991-2020 sources and are bundled.
6. Hazards are shown as places preparing, without victims.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: graphs draw at once; no network requests.

## Open questions
- The idea card flags a data source (default used: NOAA 1991-2020 U.S. Climate Normals for Phoenix, Seattle and Anchorage and WMO 1991-2020 normals for Singapore, Nairobi and Buenos Aires, bundled; no network).
