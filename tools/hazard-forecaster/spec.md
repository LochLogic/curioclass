# Hazard Forecaster

## One idea
A map of North America carries three hazard layers built from real records (earthquakes from the USGS catalog, hurricane tracks from NOAA, large wildfires from U.S. fire records), each with a question ("Where do big earthquakes happen?", "When is hurricane season?", "Where and when do fires spread most?"); the student filters by place, month, size and decade while charts update beside the map, and writes a pattern statement for each hazard (big earthquakes cluster along the Pacific edge and Alaska; Atlantic hurricanes come from June through November and peak in September; western fires peak in late summer in dry years); then with a budget for six sensors and sirens the student places warning tools where the patterns point (seismometers near faults, ocean buoys and a hurricane hunter route, fire weather stations and cameras), and the tool replays five held-back years (2020 to 2024) and scores how many events were caught early and how many minutes, hours or days of warning people would have had; short, careful accounts tell how real warnings helped people get ready; at the end the student finds that hurricanes and fire weather can be forecast days ahead while earthquakes can only be mapped by risk and warned in seconds, so an eighth grader learns to analyze and interpret data on natural hazards to forecast future catastrophic events and inform the development of technologies to mitigate their effects.

## Not like
- town-planner-disaster-ready (4, spec): building a safer town on a budget. Here reading the data that forecasts hazards.
- world-layers-map (4, spec): where earthquakes and volcanoes cluster. Here when, how big and how much warning.
- town-footprint (8, spec): impacts people cause. Here hazards nature causes.
- warming-evidence-desk (8, spec): records that explain warming. Here records that forecast hazards.

## Who and how
- Grade 8, Science, module "Natural Hazards and Human Impact". Standard: MS-ESS3-2 (analyze and interpret data on natural hazards to forecast future catastrophic events and inform the development of technologies to mitigate their effects).
- Format: data. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three hazard layers from bundled records, four filters, two charts per hazard, three pattern statements, six sensor slots from five tool types, five held-back years, the warning score, three real accounts. Extra: Compare plans (the class compares sensor plans on the projector). tool.json `modes: ["Forecast desk", "Compare plans"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-ESS3-2 (analyze) | Filter records and write a pattern statement per hazard | the map; month and size charts | 2 |
| MS-ESS3-2 (forecast) | Compare forecast lead times across hazards | the warning time chart | 3 |
| MS-ESS3-2 (technology) | Place six sensors and test against held-back years | the replay; the warning score | 4 |

## Screens and modes
Header (kit): title "Hazard Forecaster"; `Forecast desk`, `Compare plans`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A calm forecast office: a big map screen of North America with three layer tabs, a desk with filter dials. The welcome is queued (`welcomeAfter: true`): "Forecasters can't stop storms, but they can warn people. Find the patterns first. Tap the earthquake tab." First hint: "Tap the Earthquakes tab."

**A hazard (focus: the map).** At 1366x768 the map fills the left with filters and charts right; at 680x425 charts and filters are sheets. Dots show events; filters narrow by region, month, size (magnitude 5 and up, hurricane category, fire acres) and decade. Two charts: by month, by size. The student writes a pattern statement from a frame: "Big ___ happen most in ___ during ___." The tool checks the statement against the filtered data.

**Warning time.** A chart shows typical lead times: earthquake early warning (seconds), hurricane track forecasts (days), fire weather warnings (a day or two). A card: "Nobody can forecast the day of an earthquake. We can map where they're likely and warn seconds ahead."

**Sensors (focus: the plan).** Six slots, five tools (seismometer, ocean buoy, hurricane hunter route, fire weather station, fire camera). The student drags tools onto the map. `Replay 2020 to 2024` plays the held-back years; events caught early light up with their warning time. The score: events caught and total warning time. The student can move sensors and replay.

**Real accounts.** Three short factual cards on how warnings helped people get ready (hurricane evacuations from forecasts; ShakeAlert stopping trains and opening fire station doors; red flag warnings). No images of injured people, no death tolls in headlines.

**The aha.** Narrator: "Data shows where and when. Sensors buy time. And time is what lets people get safe."

**The end.** Three pattern statements, the sensor plan and the score. `Print` prints them.

**Compare plans (extra).** Sensor plans side by side.

## Content
- Bundled records: USGS magnitude 5 and up earthquakes 1980 to 2024, NOAA HURDAT2 Atlantic tracks 1980 to 2024, large U.S. wildfires from the national fire records, trimmed and simplified; five sensor types with stated reach; three accounts.
- A note: "These records are a sample. Real forecasters use many more."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Held-back years stay hidden on the map until the replay.
- Keyboard: Tab to tabs, filters, charts, the statement frame, sensor tools and `Replay`; Enter places; arrows move a sensor on the grid.
- With Motion off dots appear at once and the replay shows the final score.

## Look
- Accent `--brand` #3d4f5f storm slate (header, map frame, charts); gold #f4c542 (events caught early, the sensor in hand); paper #f2f4f6; ink #0f161d; muted #4e5660.
- Contrast (WCAG 2.1, computed): white on brand 8.46:1; brand on paper 7.67:1; ink on paper 16.52:1; muted on paper 6.74:1; ink on gold 11.20:1.
- Never color alone: hazard dots differ in shape (circle, triangle, flame) and carry legends.
- Different from this batch (skate purple, strawberry red, wave blue, pond green).

## Art
- Maps and charts drawn in code from bundled public domain data.
- Local FLUX (`scripts/localart.py`): the forecast office (1, 16:9), a buoy at sea (1, 4:3), a fire lookout camera on a ridge (1, 4:3).
About 3 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the forecast desk; `firm-captain` as the hurricane hunter pilot and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.hazard + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `filter`: "Turn a filter dial to narrow the dots."
- how `pattern`: "Fill in the pattern statement."
- how `sensor`: "Drag a sensor onto the map."
- how `replay`: "Tap Replay 2020 to 2024."
- event, whole, the replay score.
- event, whole, each account.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: filters, charts, the replay scorer. Records sit in a marked block `/* HAZARD DATA: begin */ ... /* end */` with each source and pull date.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Patterns | Write any month | The statement is checked against the filtered data. |
| Sensors | Place all six in one spot | Allowed; the score shows what was missed. |
| Warning time | Expect earthquake forecasts | The lead-time chart and card show why that fails. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `filter`; `pattern`.
2. `sensor`; `replay`.
3. Replay score (whole), waits.
4. Accounts (whole), each waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-ESS3-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Earthquake records and the Pacific pattern | U.S. Geological Survey, ComCat earthquake catalog | IRIS (EarthScope Consortium), "Seismic monitor" | yes |
| Atlantic hurricane season June 1 to November 30, peak around September 10 | NOAA National Hurricane Center, "Tropical cyclone climatology" | NOAA HURDAT2 best track data | yes |
| Western wildfires peak in late summer in dry years | National Interagency Fire Center, statistics | U.S. Forest Service, fire history data | yes |
| ShakeAlert gives seconds of warning; earthquakes cannot be predicted by date | U.S. Geological Survey, "ShakeAlert" | U.S. Geological Survey, "Can you predict earthquakes?" | yes |
| Hurricane track forecasts give days of warning | NOAA National Hurricane Center, forecast verification | NOAA National Weather Service, "Hurricane preparedness" | yes |
Backed twice: 6. Cut: 0.

Sensitivity note: natural disasters kill and injure people, and some students have lived through them. Accounts stay factual and calm and focus on getting ready; no injured people, no death tolls as headlines, and each account ends with a preparedness link (ready.gov).

Checks run (Python, scratchpad r5, 2026-11-10): June 1 to November 30 is 183 days; 2020 to 2024 is five held-back years; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map with filters and charts; at 680x425 sheets.
2. Each hazard is filtered and a pattern statement checked against the data. (MS-ESS3-2)
3. Lead times are compared across hazards. (MS-ESS3-2)
4. Six sensors are placed and scored on held-back years. (MS-ESS3-2)
5. Records match the cited sources and carry pull dates.
6. Accounts follow the sensitivity note.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: instant dots and final score; no network requests.

## Open questions
- The idea card flags a data source (default used: USGS ComCat magnitude 5 and up, NOAA HURDAT2 and national fire records for 1980 to 2024, trimmed and bundled with pull dates; no network).
- Sensitivity flag: deadly disasters (default used: factual, calm accounts focused on getting ready, no injured people or death tolls as headlines, ready.gov link, fresh-agent read before build).
- Code moves: the idea card moves MS-ESS3-3 and MS-ESS3-4 to town-footprint and MS-ESS3-5 to warming-evidence-desk (default used: this tool teaches MS-ESS3-2 only).
