# Weather Wardrobe

## One idea
Each visit the student looks out the real window, stamps today's weather on a picture calendar (sun, clouds, rain, snow, wind, hot or cold) and dresses Leo, a made-up kid in pajamas, to match (coat, boots, sun hat, umbrella), and Leo shivers, sweats or smiles; a child who can't come back each day plays a real recorded month from a sample city one day at a time instead; a picture graph counts the stamps ("How many rainy days?") and compares a winter month with a summer month in the same city; then a TV weather forecaster says a big storm is coming, and the student picks questions to ask (When? How strong? What should we do?) and helps Leo's family get ready (bring in toys, find flashlights, stay inside), and the storm passes with Leo safe; at the end the calendar and graph show more cold, snowy days in winter and more hot, sunny days in summer, so a kindergartner learns to use weather observations to describe patterns over time, and why people forecast weather to get ready for storms.

## Not like
- climate-postcards (3, concept): climates around the world, same engine. Here one window and one month.
- sky-diary (1, concept): sun and moon patterns. Here weather.
- shade-builder (K, spec): sunlight warming the ground. Here the weather outside.
- beaver-builders (K, spec): a changing valley. Here a changing sky.

## Who and how
- Kindergarten, Science, module "Weather Watch". Standards: K-ESS2-1 (use and share observations of local weather conditions to describe patterns over time), K-ESS3-2 (ask questions to obtain information about the purpose of weather forecasting to prepare for, and respond to, severe weather).
- Format: data (the idea card proposes the change from showdown). Driver: one child with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 64 px or more.
- Daily stamps and dressing, a real recorded month for children who can't come daily, a picture graph, a winter and summer compare, the storm forecast. The calendar stays on the device and the screen says so (localStorage `weather-wardrobe-v1`, try/catch). Extra: Class vote (the class votes the stamp and Leo's outfit on the projector). tool.json `modes: ["My window", "Class vote"]`, `minutes: "5-15"`, `grades_label: "Kindergarten"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K-ESS2-1 (observe) | Stamp today's weather and dress Leo | the stamp on the calendar; Leo's face | 2 |
| K-ESS2-1 (patterns) | Count stamps in the picture graph and compare winter and summer | the graph; two months side by side | 3 |
| K-ESS3-2 | Ask the forecaster questions and help the family get ready | the forecast; the getting-ready checklist | 4 |

## Screens and modes
Header (kit): title "Weather Wardrobe"; `My window`, `Class vote`; `Read`, `Motion`, `Sound`, `Print`. Controls 64 px or more.

**On load and first tap.** A bedroom window with the curtains closed, Leo in pajamas, a row of weather stamps and a picture calendar. A line under the calendar: "Your calendar stays on this device." The welcome is queued (`welcomeAfter: true`): "Good morning! Look out your real window. What is the sky doing? Tap a stamp." First hint: "Tap a weather stamp."

**Stamp and dress (focus: the window and Leo).** At 1366x768 the window and Leo fill the left with the calendar right; at 680x425 the calendar is a sheet. The chosen stamp fills the window picture. Then the student drags clothes onto Leo; Leo shivers in shorts on a snowy day, sweats in a coat on a hot day, smiles when dressed right. The day goes on the calendar.

**A recorded month.** A `Play a real month` button for children who can't come back each day: a sample city's real recorded month plays one day at a time with the same stamp-and-dress steps.

**Patterns (K-ESS2-1).** A picture graph counts stamps ("How many rainy days? Count the umbrellas."). Then a winter month and a summer month from the same sample city sit side by side; the student taps which has more snowy days and which has more hot, sunny days.

**The storm forecast (K-ESS3-2).** A TV forecaster (made up) says: "A big thunderstorm is coming this afternoon." Three question buttons: "When?" "How strong?" "What should we do?" The answers lead to a getting-ready checklist with pictures: bring in toys, find flashlights, come inside when you hear thunder. The storm passes; Leo is safe inside.

**The end (the aha).** The calendar, the graph and the checklist. Narrator: "Weather changes every day, but over many days it makes patterns. And a forecast helps us get ready before a storm comes." `Print` prints the calendar as a coloring page.

**Class vote (extra).** The class votes the stamp and Leo's outfit together.

## Content
- Seven stamps, twelve clothing pieces, Leo's three faces, real recorded months for three sample cities (one winter and one summer month each), the forecaster and three answers, the checklist.
- The storm is gentle on screen: no damage, no scared faces beyond a short "uh oh".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The calendar saves on the device with try/catch and a clear button; nothing is sent.
- Keyboard: Tab to stamps, clothes, the calendar, graph and questions; Enter places.
- With Motion off rain and snow show as still pictures.

## Look
- Accent `--brand` #1f5f99 sky blue (header, the calendar, the graph); gold #f4c542 (today's square, the piece in hand); paper #eff6fc; ink #0a1d30; muted #4f5a66.
- Contrast (WCAG 2.1, computed): white on brand 6.66:1; brand on paper 6.10:1; ink on paper 15.64:1; muted on paper 6.45:1; ink on gold 10.49:1.
- Never color alone: stamps are pictures with spoken names; graph bars carry counts and pictures.
- Different from this batch (pond green, sun orange, snail plum, night indigo).

## Art
- People (illustrated) for Leo with three faces, the family and the forecaster, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Local FLUX (`scripts/localart.py`): the window view in six weathers (6, 4:3), a living room during the storm (1, 16:9).
- Drawn in code: stamps, clothes, the calendar, the graph.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the TV forecaster; `warm-teacher` as the guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.day + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `stamp`: "Tap a stamp for today's weather."
- how `dress`: "Drag clothes onto Leo."
- event, whole, Leo's reaction.
- how `count`: "Count the stamps in the graph."
- event, whole, the forecast.
- how `ready`: "Tap a way to get ready."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
weather (family "weather"; no engine file yet). This tool builds the weather family's shared pieces first, in a marked block `/* WEATHER DATA: begin */ ... /* end */`: the stamp set, the recorded-month format (date, high, low, sky, rain or snow) and the picture graph; climate-postcards reuses them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Stamp | Tap sun every day | Allowed for the child's own window; the recorded month checks against real records. |
| Dress | Put on everything | Leo sweats on a hot day; the hint names what to take off. |
| Forecast | Skip questions | The checklist opens after all three answers. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `stamp`; `dress`.
2. Leo's reaction (whole), waits.
3. `count`; forecast (whole); `ready`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for K-ESS2-1, K-ESS3-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Daily weather records for sample cities | NOAA National Centers for Environmental Information, Global Historical Climatology Network Daily | NOAA, "Climate Data Online" | yes |
| "When thunder roars, go indoors" and storm getting-ready steps | National Weather Service, "Lightning Safety" | Ready.gov, "Thunderstorms and Lightning" | yes |
| Forecasts help people prepare for severe weather | National Weather Service, "About the NWS" | NOAA SciJinks, "How Is Weather Forecast?" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r25, 2026-11-09): seven stamps; three cities with two months each is six recorded months; three forecast questions; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 window and calendar; at 680x425 sheet.
2. A stamp and an outfit go on the calendar each visit, or each day of a recorded month. (K-ESS2-1)
3. The picture graph counts stamps and winter and summer are compared. (K-ESS2-1)
4. The forecast questions lead to the getting-ready checklist. (K-ESS3-2)
5. The calendar stays on the device, stated on screen.
6. Every card is spoken; the storm is gentle.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still weather; no network requests.

## Open questions
- The idea card changes the format from showdown to data (default used: data, a picture-graph data desk, with the class vote as the extra).
- The idea card flags a data source (default used: NOAA GHCN-Daily records for three sample cities, Minneapolis, Seattle and Atlanta, one winter and one summer month each, bundled with the tool; no network requests).
