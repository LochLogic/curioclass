# Tenochtitlan Builder

## One idea
The child builds the Mexica capital on a small island in Lake Texcoco, where the city was founded around 1325: they lay chinampas (farm plots built up from lake mud) to feed a growing city, causeways to the shore, an aqueduct from the springs of Chapultepec for fresh water, and a long dike to hold back the lake's salty eastern water and floods, then run test years (a flood, a dry season, a bigger city) where weak spots fail and they rebuild; guides explain the real works (the dike built under Nezahualcoyotl, the Chapultepec aqueduct, the great market at Tlatelolco); the city works because it changes the lake on purpose, and the epilogue shows the lake drained after 1521 and Mexico City sinking today, then a gallery of Inca terraces and Maya reservoirs, so a seventh grader learns how a people's choices shaped their environment and daily life, and how one city connects to the wider Americas and to what came after.

## Not like
- river-kingdom (6, spec): river valleys of the Near East. Here a city built in a lake.
- nations-of-north-america (5, concept): a map of Native nations. Here one city's engineering.
- settle-the-valley (4, spec): settlers changing a valley. Here a city built to change its lake on purpose.
- columbian-exchange (7, spec): what crossed the ocean after 1492. Here the city before 1521.

## Who and how
- Grade 7, Social Studies (History and Geography), module "Civilizations of the Americas". Standards: D2.His.1.6-8 (analyze connections among events and developments in broader historical contexts), D2.Geo.4.6-8 (explain how cultural patterns and economic decisions influence environments and the daily lives of people in both nearby and distant places).
- Format: builder. Driver: one child alone, or teams in a build-off (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Build and test years to a city of 200,000, the epilogue and the gallery. Extra: Build-off (teams race to a target population with a fixed budget of work crews). tool.json `modes: ["Build", "Build-off"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.4.6-8 | Place chinampas, causeways, the aqueduct and the dike, then run test years | the three needs meters (food, fresh water, flood safety); the lake's fresh and salty water colors changing | 2, 3 |
| D2.Geo.4.6-8 (daily life) | Visit the market and a chinampa family after each test year | the daily-life cards that change with the build | 3 |
| D2.His.1.6-8 | Place the epilogue and gallery cards on a timeline and map of the Americas | the Americas map with Tenochtitlan, Cusco and Tikal; the timeline from 1325 to today | 4 |

## Screens and modes
Header (kit): title "Tenochtitlan Builder"; `Build`, `Build-off`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A wide lake in a valley ringed by mountains and volcanoes. A small rocky island in the western part. A population counter reads 5,000. Three needs meters: Food, Fresh water, Flood safety. A build tray with four pieces. The welcome is queued (`welcomeAfter: true`): "Around 1325, the Mexica settled on this small island in Lake Texcoco. Can you build a city that feeds, waters and protects a quarter of a million people? Drag a chinampa next to the island." First hint: "Drag a chinampa into the shallow water."

**Build (focus: the lake).** At 1366x768 the lake fills the screen with the tray left and meters right; at 680x425 the tray is a bottom strip.
- Chinampas: rectangles of mud and plants in shallow fresh water, anchored with willow trees; each feeds a number of people. They fail in salty water.
- Causeways: raised roads to the shore (north, west, south), with gaps and bridges for canoes; they bring trade and people.
- Aqueduct: from the springs of Chapultepec on the western shore; fresh drinking water for the city, because the lake around the island was brackish.
- Dike: a long wall of stone, earth and wooden posts across the lake (about 16 kilometers), separating the fresher western water from the salty east and holding back floods.
- Each piece has a guide card with the real work and a date.

**Test years.** The child taps `Run a year` and picks or draws a test:
- Flood year: without the dike, salty floodwater spreads, drowning chinampas; with it, the western lake stays fresh (based on the flood of about 1449 and the dike built after it under Nezahualcoyotl, the ruler of Texcoco).
- Dry year: without the aqueduct, the city runs short of drinking water.
- Growing city: the population jumps; without more chinampas and causeways bringing trade, the food meter falls.
- Weak spots fail with a plain reason ("Salt water reached these chinampas"), and the child rebuilds.

**Daily life cards (made for this game, built from history).** After each year: a chinampa family harvesting maize, beans and squash; a canoe trader at the market of Tlatelolco, where a Spanish visitor in 1520 counted many thousands of people a day; a water carrier at the aqueduct. Their lines change with the build.

**The epilogue.** At about 200,000 people (estimates for the city run from about 60,000 to over 200,000, and the card says so), the narrator: "Your city works because it changes the lake on purpose." Then three cards: in 1521, after a long siege and a smallpox epidemic, the city fell to Spanish forces and their Indigenous allies; over the next centuries, the colonial government and later Mexico drained most of the lake to stop floods; today Mexico City, built on the old lakebed, sinks in places by up to about 50 centimeters a year as groundwater is pumped out.

**The gallery (D2.His.1.6-8).** Others solved the same problems: Inca farming terraces and canals in the Andes; Maya reservoirs at Tikal holding rain through the dry season. The child places each card on a map of the Americas and on a timeline from 1325 to today.

**The end.** The finished city, the meters' record, the timeline and the gallery map. `Print` prints them.

**Build-off (extra).** Teams get the same number of work crews and race to 200,000 through three test years.

## Content
- Four build pieces with real-work cards, three test years, a small model (made for this game) for food, water and floods, three daily-life cards with lines per build, three epilogue cards, two gallery cards, the timeline.
- The model and the three people are made up and labeled; the works, dates and history are real.
- Religion appears as the Templo Mayor at the city's center, named and drawn plainly; the conquest is told in one plain card with care.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pieces snap to the lake grid; chinampas must touch fresh, shallow water; the dike draws along tapped points.
- A test year can't run while a piece is being placed.
- Keyboard: Tab to the tray, the lake grid and `Run a year`; arrows move a piece; Enter to place.
- With Motion off water spreads without animation and canoes stay still.

## Look
- Accent `--brand` #1f6b5a lake jade (header, tray, fresh water); gold #f4c542 (the piece in hand, a passing meter); paper #eff6f3; ink #06231c; muted #4b5b56.
- Contrast (WCAG 2.1, computed): white on brand 6.35:1; brand on paper 5.79:1; ink on paper 15.14:1; muted on paper 6.53:1; ink on gold 10.21:1.
- Never color alone: fresh water is plain, salty water is dotted and labeled "salty"; meters show numbers and words.
- Different from this batch (atlas indigo, Atlantic ochre, purple, red).

## Art
- Public domain: the 1524 Nuremberg map of Tenochtitlan (Newberry Library), and the founding page of the Codex Mendoza (Bodleian Library, image rights checked at build), each with credit.
- Local FLUX (`scripts/localart.py`): the valley and lake (1, 16:9); chinampas close-up (1, 3:2); the dike (1, 3:2); the drained lakebed and today's city (1, 16:9); Inca terraces (1, 3:2); a Maya reservoir at Tikal (1, 3:2).
- People art goes to Gemini with `people: true`: the chinampa family, the canoe trader, the water carrier (3; cutout yes); dress from the Codex Mendoza and the Florentine Codex, checked by a fresh agent.
- Drawn in code: the lake grid, pieces, meters, the timeline and the Americas map.
About 11 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as the guide; `playful-friend` as the daily-life cards' reader. `Curio.voice` with `scope: () => state.mode + ':' + state.year + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `build`: "Drag a piece onto the lake."
- event, whole, each real-work card.
- how `run`: "Tap Run a year."
- event, whole, each test-year result.
- event, whole, each daily-life card.
- event, whole, each epilogue card.
- how `gallery`: "Drag each card to its place on the map and timeline."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the lake grid with fresh and salty water, four piece types, the needs model, test years, the epilogue, the gallery map and timeline.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Build | Fill the lake with chinampas | Chinampas in salty water fail in the flood year; without the aqueduct the dry year fails. |
| Test years | Skip tests | The epilogue opens only after all three tests pass at 200,000. |
| Gallery | Drop cards anywhere | Each card must land at its place and date. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `build`; real-work cards (whole), each waits.
2. `run`; result (whole); daily-life cards (whole).
3. Epilogue cards (whole), each waits.
4. `gallery`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1.6-8 and D2.Geo.4.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Tenochtitlan founded about 1325 on an island in Lake Texcoco | Encyclopaedia Britannica, "Tenochtitlan" | Smithsonian Magazine, "Tenochtitlan" and Templo Mayor Museum (INAH) | yes |
| Chinampas built of lake mud and plants, anchored with willows | FAO, "Chinampa agricultural system of Mexico City" (GIAHS) | Britannica, "Chinampa" | yes |
| The dike of Nezahualcoyotl, about 16 km, built after the flood of about 1449, separated fresh and salty water | Britannica, "Nezahualcóyotl" | Mexico City Basin histories summarized by INAH | yes |
| The Chapultepec aqueduct brought fresh water to the city | Britannica, "Tenochtitlan" | Smithsonian Magazine | yes |
| The great market at Tlatelolco drew many thousands a day | Hernán Cortés, Second Letter (1520) | Britannica, "Tlatelolco" | yes, the letter's count is shown as one visitor's estimate |
| Population estimates range widely, up to over 200,000 | Britannica, "Tenochtitlan" | Smith, "The Aztecs" (Wiley-Blackwell, 3rd ed. 2012) | yes, as a range |
| The city fell in 1521 after a siege and a smallpox epidemic, with Indigenous allies fighting alongside the Spanish | Britannica, "Fall of Tenochtitlan" | Smithsonian Magazine | yes |
| The lake was drained over centuries; Mexico City sinks in places up to about 50 cm a year | Chaussard et al., Journal of Geophysical Research: Solid Earth (2021) | NASA Earth Observatory, "Mexico City is sinking" | yes |
| Inca terraces and Maya reservoirs at Tikal | Britannica, "Inca: agriculture" | Scarborough et al., "Water and sustainable land use at the ancient tropical city of Tikal," PNAS (2012) | yes |
Backed twice: 10. Cut: 0.

Sensitivity note: Mexica religion is shown through the Templo Mayor plainly, with no images of sacrifice; the conquest and the epidemic are told in one plain card with care; people art is checked against codex sources. A fresh-agent read is needed before build.

Checks run (Python, scratchpad r12, 2026-11-09): dates in order (1325, about 1449, 1520, 1521, today); the model reaches 200,000 only with all four piece types; each test year fails without its matching piece; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 lake, tray and meters; at 680x425 bottom tray.
2. Each piece places with its real-work card. (D2.Geo.4.6-8)
3. Three test years fail weak builds with reasons and update daily-life cards. (D2.Geo.4.6-8)
4. The epilogue and gallery place on the map and timeline. (D2.His.1.6-8)
5. Population ranges are labeled as estimates.
6. Build-off runs for teams.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no animated water; no network requests.

## Open questions
- Sensitivity flag: Mexica religion, the conquest and the epidemic (default used: Templo Mayor shown plainly with no sacrifice images, the conquest in one plain card, people art checked against codices, fresh-agent read before build).
