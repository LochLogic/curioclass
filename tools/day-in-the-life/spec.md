# Day in the Life

## One idea
The child spends one school day, morning to night, with a kid in each of four places (Wanjiru in Kenya's central highlands, Mateo in the Andes near Cusco, Aoi in the mountains of Nagano, Sigrid in Tromsø above the Arctic Circle), and at three moments in each day taps "Why like this?" to learn how a family's way of building, farming, dressing or getting around fits both their land and weather and their culture; each day ends on a dot map of the whole country where the child guesses where most people live and learns why, and a chart lines up all four friends, so a third grader sees how culture and environment shape how people live and where they live.

## Not like
- festival-parade (1, spec): celebrations that traveled. Here everyday life and land.
- pen-pal-parcels (2, spec): products and trade between countries. Here homes, food, travel and where people live.
- region-compare (6, concept): regions with data at grade 6. Here four kids' days at grade 3.
- three-towns (2, spec): three kinds of U.S. community. Here four countries and their landforms.

## Who and how
- Grade 3, Social Studies (Geography), module "Communities Around the World". Standards: D2.Geo.4.3-5 (explain how culture influences the way people modify and adapt to their environments), D2.Geo.6.3-5 (describe how environmental and cultural characteristics influence population distribution in specific places or regions).
- Driver: one child alone, or the teacher on the projector; every line can be read aloud with `Read` (tool.json `driver: "either"`). Controls 44 px or more.
- Four days (any order), each ending on a dot map, then the chart. tool.json `modes: ["Days", "Chart", "My day"]`, `minutes: "25-40"` (about 7 minutes a day), `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.4.3-5 | At three "Why like this?" moments a day, pick the reason from three: land, weather, or a family or culture way (some moments are two working together) | the scene, the reason card, and a picture of the land or weather behind it | 2, 3 |
| D2.Geo.6.3-5 | Tap where you think most people in the country live, then see the real dot map and pick why | the guess pin, the dot map, the reason cards (milder, flatter, wetter, near the coast or a capital) | 4 |
| D2.Geo.4.3-5 and D2.Geo.6.3-5 | Fill the chart: weather, land, how people adapt, where most live, for four friends | the four-column chart | 5 |

## Screens and modes
Header (kit): title "Day in the Life"; `Days`, `Chart`, `My day`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Four postcards with four kids waving, each labeled with a name, a place and a small map. The welcome is queued (`welcomeAfter: true`): "Four friends, four places, four school days. Pick a friend to spend the day with." First hint: "Tap a postcard to spend the day with that friend."

**A day (focus: the story scene).** Each day is eight short scenes along a sun-and-moon bar (wake up, get to school, at school, lunch, after school, chores, play, bedtime). `Next` moves on. At 1366x768 the scene fills the center with the line below it and the day bar on top; at 680x425 the line sits under a smaller scene. Three scenes carry a `Why like this?` button. Tapping it shows three reason cards (Land, Weather, Our way, each with an icon); the child picks one or two. Right: the reason plays with a picture. Wrong: a hint names what to look at in the scene.
- Wanjiru, near Nyeri, Kenya (central highlands, near Mount Kenya):
  - Getting to school: a crowded matatu minibus down the hill road. Why: Our way (shared minibuses are how many people get around in Kenya).
  - After school: picking tea leaves on her aunt's farm. Why: Land and Weather (tea grows well in cool highlands with lots of rain).
  - Chores: filling a bucket from the rain tank by the house. Why: Weather (the metal roof's gutter catches the rainy-season rain to save for dry months).
- Mateo, near Cusco, Peru (Andes, about 3,400 meters up):
  - Morning: his grandmother speaks Quechua at breakfast and wraps him in a warm poncho. Why: Our way and Weather (Quechua is the family's language; the mountain mornings are cold).
  - After school: helping on the family's terraced field. Why: Land and Our way (people built flat steps on steep slopes long ago, many in Inca times, so soil doesn't wash away; families still farm them).
  - Dinner: potatoes, many kinds. Why: Land and Our way (potatoes were first grown in the Andes, and farmers there grow thousands of kinds).
- Aoi, Nagano, Japan (in the mountains):
  - Getting to school: a train that runs through tunnels. Why: Land (Japan is mostly mountains, so railways tunnel through them).
  - Lunch: school lunch the class serves itself, with rice and miso soup. Why: Our way (students take turns serving lunch and cleaning up).
  - Evening: snow piled high by the door. Why: Weather (Nagano gets deep winter snow; roofs are steep so snow slides off).
- Sigrid, Tromsø, Norway (above the Arctic Circle), in December:
  - Walking to school in the dark at 8 a.m., wearing a reflector on her coat. Why: Weather and Our way (in winter the sun doesn't rise for about two months; kids wear reflectors so drivers see them).
  - Recess: playing outside in snow suits. Why: Our way (Norwegians like to say there's no bad weather, only bad clothes).
  - Home: a wooden house with thick walls and triple windows. Why: Weather and Land (long cold winters, and lots of wood from forests).

**Where people live (focus: the country map).** After bedtime, an outline map of the country appears. "Where do you think most people in [country] live? Tap the map." The child taps a guess; the real dot map fades in (each dot stands for many people). Then: "Why do most people live there?" with three to four reason cards (for example "It's milder by the coast", "The land is flat", "There's more rain for farms", "The capital is there"); the right ones (one or two) light:
- Kenya: most live in the cooler, wetter highlands of the southwest and around Lake Victoria; the north is dry. (More rain for farms; milder)
- Peru: most live on the dry coast, about a third in and around Lima. (The capital is there; flat land by the sea)
- Japan: most live on the flat coastal plains, like the big plain around Tokyo, because most of the country is mountains. (The land is flat)
- Norway: most live in the south and along the coast, where it is milder, near Oslo. (It's milder by the coast; the capital is there)

**Chart (focus: the chart).** Four columns, four rows: Weather, Land, How people adapt, Where most live. The child drags short cards (16, four per friend) into cells; cells fill from the days the child has finished. `Print` prints the chart.

**My day (extra).** A fifth column: the child picks pictures for their own weather, land, one way their family or town fits the place, and where people live in their state (their own guess). Kept only while the page is open.

## Content
- Four friends with eight scenes each, three "Why like this?" moments each with reasons; four dot maps with reasons; sixteen chart cards.
- The four friends are made up; their places, land, weather and ways are real.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Why like this?` shows only on its three scenes. The dot map shows only after a guess. `Chart` opens after one full day; cells for unfinished friends say "Spend the day with [name] first."
- Keyboard: Tab to cards, Enter to pick, arrow keys on the map to move the guess pin, Enter to place it.
- With Motion off scenes change without sliding and dots appear at once.

## Look
- Accent `--brand` #9a4a1c clay (header, the day bar, chart frames); gold #f4c542 (the sun on the day bar, the right reason, the guess pin); paper #fcf3ec; ink #2b1205; muted #6a5446.
- Contrast (WCAG 2.1, computed): white on brand 6.23:1; brand on paper 5.69:1; ink on paper 16.09:1; muted on paper 6.46:1; ink on gold 10.84:1.
- Never color alone: reasons carry icons and words; dot maps carry a legend in words.
- Different from this batch (promise navy, overlay sepia, map-maker forest green, pool aqua).

## Art
- People art goes to Gemini with `people: true`: Wanjiru, Mateo, Aoi and Sigrid with family members, 8 scenes each (32, 16:9), each checked against photographs of everyday life in that place for clothing, homes and school, and drawn without stereotype (modern phones, school uniforms where real, everyday clothes); the four postcards (4).
- Local FLUX (`scripts/localart.py`): land and weather pictures for reasons (12, 1:1: tea fields, a rain tank, terraces, potato kinds, a mountain tunnel, steep snowy roofs, a polar night street, forests).
- Drawn in code: country outlines and dot maps (from public population density data, generalized), the day bar, reason cards, the chart.
About 48 images.

## Voice
Bank voices, each unique in this batch: `curious-librarian` as the narrator; the friends use `big-sister` (Wanjiru), `easy-coach` (Mateo), `soft-breath` (Aoi), `gentle-storyteller` (Sigrid). `Curio.voice` with `scope: () => state.friend + ':' + state.scene + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Four friends, four places, four school days. Pick a friend to spend the day with."
- event, whole, each scene line in the friend's voice.
- how `why` (once): "Tap Why like this? Then pick Land, Weather or Our way. Some have two."
- event, whole, each reason.
- event `why-no`: the hint about the scene.
- how `guess`: "Where do you think most people in [country] live? Tap the map."
- event, whole, the dot map reason.
- how `chart`: "Drag each card to its friend and row."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the day bar and scenes, the reason picker (one or two right), map guess and dot map, the chart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Why like this? | Tap Weather every time | Reasons vary (Land, Weather, Our way, and pairs); wrong picks point to the scene. |
| Dot map | Tap the middle | The guess is only a guess; the reason cards need the dots read. |
| Chart | Drag at random | Cards belong to one friend and row each; wrong drops return with the friend's name. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Tap a postcard: scene 1 (whole).
2. `Next`: the next scene (whole). On a Why scene: `why` (once); picks: reason (whole) or `why-no`.
3. Bedtime: `guess`; tap; the dot map; reason picks (whole).
4. Chart: `chart`; drops.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.4.3-5 and D2.Geo.6.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Matatus (shared minibuses) are a main way people travel in Kenya | Wikipedia, Matatu (checked 2026-11-09) | World Bank, Kenya urban transport reports | yes |
| Kenyan tea grows in the cool, rainy highlands; most Kenyans live in the southwest highlands and around Lake Victoria, and the north is dry | Kenya National Bureau of Statistics, 2019 census population density | Tea Board of Kenya, growing regions | yes |
| Andean terraces (andenes), many from Inca times, are still farmed; potatoes were first grown in the Andes, and Peru grows thousands of kinds | Wikipedia, Andenes (checked 2026-11-09) | International Potato Center (CIP), "Potato facts" | yes |
| Quechua is spoken by millions in Peru, especially in the Andes | Peru INEI, 2017 census language data | Wikipedia, Quechuan languages | yes |
| Most Peruvians live on the coast; about a third live in Lima's metro area | Peru INEI, 2017 census | Wikipedia, Geography of Peru (checked 2026-11-09) | yes |
| Japan is mostly mountains, and most people live on coastal plains such as the Kanto Plain | Wikipedia, Geography of Japan (checked 2026-11-09) | Statistics Bureau of Japan, "Statistical Handbook of Japan" | yes |
| Nagano gets deep winter snow; Japanese students serve school lunch and clean their classrooms | Japan Meteorological Agency, Nagano snowfall normals | Japan MEXT, school lunch program (kyushoku) | yes |
| Tromsø has polar night from late November to mid January; Norwegian children commonly wear reflectors in the dark season | Wikipedia, Tromsø (checked 2026-11-09) | Norwegian Public Roads Administration (Statens vegvesen), reflector campaigns | yes |
| Most Norwegians live in the south and along the coast, kept milder by the North Atlantic Current | Statistics Norway (SSB), population by region | Wikipedia, Geography of Norway (checked 2026-11-09) | yes |
Backed twice: 10. Cut: 0.

Sensitivity note: four real cultures. Each friend is drawn from everyday modern life, not costume or poverty, and art is checked against photographs. A fresh-agent read of the scenes and art is needed before build.

Checks run (Python, scratchpad r5, 2026-11-09): each friend has exactly three Why moments; across the 12, Land appears 5 times, Weather 6, Our way 7, so no single answer wins; each dot map has one or two right reasons; the chart has 16 cards, one per cell; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene, line and day bar fit; at 680x425 the line sits under a smaller scene.
2. Each Why moment accepts only its reasons, including pairs. (D2.Geo.4.3-5)
3. Each friend has three Why moments with pictures. (D2.Geo.4.3-5)
4. Each country's dot map follows a guess and accepts only its reasons. (D2.Geo.6.3-5)
5. The chart takes all 16 cards in their cells. (D2.Geo.4.3-5, D2.Geo.6.3-5)
6. `Why like this?` and the dot map are never named before they show.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no slides; no network requests.

## Open questions
- Sensitivity flag (four real cultures in Kenya, Peru, Japan and Norway); fresh-agent read of scenes and art needed before build (default used: everyday modern life, no costume or poverty framing, art checked against photographs).
