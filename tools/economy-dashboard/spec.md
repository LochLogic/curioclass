# Economy Dashboard

## One idea
A dashboard shows the real U.S. economy from 1948 to the latest bundled quarter as unlabeled lines (output, unemployment, inflation, consumer spending, the money supply), and the student is told "somewhere in here are 12 recessions; find them", shades the stretches they think were recessions, then sees the official dates from the National Bureau of Economic Research and a short story for each (the oil shocks of the 1970s, the deep slump of 1981 to 1982, the financial crisis of 2007 to 2009, the two-month 2020 collapse); investigation cards ask how changes in spending, production and the money supply moved the indicators (why unemployment peaked near 15 percent in April 2020, why inflation rose to about 9 percent in 2022 after big spending and fast money growth); a forecast step reads three leading indicators (the yield curve, new jobless claims, building permits) and the student forecasts the next four quarters, kept on the device and checked when the tool's data is refreshed; at the end the student writes a short "state of the economy" brief with evidence from three indicators, so a twelfth grader learns to use current data to explain how spending, production and the money supply affect the economy, and to use indicators to analyze its present and future.

## Not like
- fed-chair (12, spec): setting rates in a model. Here reading real data.
- data-desk-distributions (12, spec): describing one distribution. Here time series of a whole economy.
- stock-market-1929 (11, spec): one crash as an investor. Here twelve recessions as an analyst.
- inflation-wallet (10, spec): a family in hyperinflation. Here national indicators.

## Who and how
- Grade 12, Social Studies (Economics), module "Macroeconomics". Standards: D2.Eco.10.9-12 (use current data to explain the influence of changes in spending, production, and the money supply on various economic conditions), D2.Eco.11.9-12 (use economic indicators to analyze the current and future state of the economy).
- Format: data. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Five series from 1948, twelve recessions, six investigation cards, three leading indicators, the forecast, the brief. Extra: Class forecasts (the class compares forecasts on one chart, entered on one device). tool.json `modes: ["Dashboard", "Class forecasts"]`, `minutes: "35-45"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.11.9-12 | Shade recessions from the indicators, then compare with official dates | the unlabeled dashboard; the shaded guesses; the official bands | 2 |
| D2.Eco.10.9-12 | Answer investigation cards linking spending, production and money to indicator moves | the cards with the lines they point to | 3 |
| D2.Eco.11.9-12 (future) | Read the leading indicators, forecast four quarters and write the brief | the yield curve, claims and permits; the forecast fan; the brief | 4 |

## Screens and modes
Header (kit): title "Economy Dashboard"; `Dashboard`, `Class forecasts`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Five stacked line charts from 1948 to the latest bundled quarter, labeled only A to E. A card: "Somewhere in here are 12 recessions. Find them." The welcome is queued (`welcomeAfter: true`): "These lines are the real U.S. economy. They tell you when things went wrong, if you know how to read them. Drag across a stretch you think was a recession." First hint: "Drag across one of the charts."

**Recession spotting (D2.Eco.11.9-12).** At 1366x768 the charts fill the left with the card panel right; at 680x425 the panel is a sheet. The student shades stretches on any chart. After twelve shadings (or a press of `Reveal`), labels appear (A real GDP growth, B unemployment rate, C inflation, D real consumer spending, E M2 money supply growth) and the official recession bands from 1948 to 2020:
- 1948 to 1949, 1953 to 1954, 1957 to 1958, 1960 to 1961, 1969 to 1970, 1973 to 1975, 1980, 1981 to 1982, 1990 to 1991, 2001, 2007 to 2009, 2020.
- Each band has a short story with one human scene (generated, labeled).
- The student's hits and misses are counted, and the card asks which line gave the clearest signal.

**Investigation cards (D2.Eco.10.9-12).** Six cards, each pointing at real moves:
1. 1973 to 1975: oil prices quadrupled after the 1973 embargo; output fell while inflation rose.
2. 1981 to 1982: the Federal Reserve raised rates to fight inflation; unemployment reached 10.8 percent in late 1982 and inflation fell.
3. 2007 to 2009: housing and banks failed; spending fell; unemployment reached 10.0 percent in October 2009.
4. 2020: lockdowns cut spending and production at once; unemployment hit 14.8 percent in April 2020, then fell fast.
5. 2020 to 2021: relief spending and money growth (M2 grew about 25 percent in a year) as supply chains snarled.
6. 2022: inflation reached about 9 percent in June 2022.
- For each the student marks which force moved first (spending, production, money) and which lines followed.

**Forecast (D2.Eco.11.9-12).** Three leading indicators: the yield curve (the 10-year minus 3-month Treasury spread, which turned negative before every recession since the late 1960s), initial jobless claims, and building permits. The student drags a forecast for GDP growth and unemployment four quarters ahead; it stays on the device and the screen says so. When the tool's bundled data is refreshed, the forecast is checked against what happened.

**The brief (the aha).** "The economy right now is ___. Evidence: ___ [indicator], ___ [indicator], ___ [indicator]. In the next year I expect ___, because ___." Narrator: "Nobody gets the official date of a recession until it's over. You were reading it in real time."

**The end.** The shaded charts, the investigation marks, the forecast and the brief. `Print` prints them.

**Class forecasts (extra).** Forecasts entered on one device show as a class fan chart.

## Content
- Five FRED series from 1948 and three leading-indicator series, bundled as a data file with its pull date shown; the NBER recession dates; twelve recession stories; six investigation cards; the forecast tool; the brief template.
- The runtime makes no network requests; data refreshes come from a build script.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Shading snaps to quarters; any shading can be removed.
- Keyboard: Tab to charts, the shading tool, cards, the forecast and the brief; arrow keys move a shading edge by a quarter.
- With Motion off bands appear without fading and lines draw at once.

## Look
- Accent `--brand` #1f4e79 chart navy (header, lines, the panel); gold #f4c542 (the student's shading, the focused card); paper #eff4f9; ink #071a2b; muted #4f5862.
- Contrast (WCAG 2.1, computed): white on brand 8.66:1; brand on paper 7.83:1; ink on paper 15.93:1; muted on paper 6.53:1; ink on gold 10.83:1.
- Never color alone: official bands carry a hatch and a label; the student's shading carries an outline; lines carry letters then names.
- Different from this batch (biscuit brown, lifespan rose, Fed green, trait indigo).

## Art
- Drawn in code with kit/data-desk.js `Chart` (line) and fixed `xDomain` 1948 to the last bundled quarter; fixed `yDomain` per series.
- Local FLUX (`scripts/localart.py`): one scene per recession story without identifiable people (12, 16:9): a gas line, a closed factory, a "for sale" street, an empty downtown.
About 12 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the recession stories; `calm-professor` as the analyst guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `shade`: "Drag across a stretch you think was a recession."
- event, whole, the reveal.
- event, whole, each recession story.
- how `investigate`: "Mark which force moved first."
- how `forecast`: "Drag your forecast for the next four quarters."
- how `brief`: "Write the state of the economy with three indicators."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
data-desk (kit/data-desk.js). Uses `DataTable` for the bundled series, `t.where` for date ranges, `Chart` (line) with fixed `xDomain` and `yDomain`, and adds shading bands, the reveal and the forecast fan.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Shading | Shade everything | Hits and misses are both counted; shading all of it scores twelve hits and dozens of misses. |
| Investigation | Mark "money" every time | Each card checks against the real first mover. |
| Brief | Cite one indicator | It needs three, with a direction for each. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `shade`.
2. Reveal (whole), waits; recession stories (whole, on tap).
3. `investigate`; `forecast`.
4. `brief`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.10.9-12 and D2.Eco.11.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Twelve recessions since 1948 and their dates | National Bureau of Economic Research, "US Business Cycle Expansions and Contractions" | Federal Reserve Bank of St. Louis, FRED (USREC) | yes |
| Unemployment peaks: 10.8 percent (1982), 10.0 percent (October 2009), 14.8 percent (April 2020) | Bureau of Labor Statistics, Current Population Survey | FRED (UNRATE) | yes |
| Inflation about 9 percent in June 2022 | Bureau of Labor Statistics, CPI news release (July 2022) | FRED (CPIAUCSL) | yes |
| M2 grew about 25 percent in a year from 2020 | Federal Reserve Board, H.6 release | FRED (M2SL) | yes |
| The 1973 embargo and the oil price quadrupling | Federal Reserve History, "Oil Shock of 1973-74" | Office of the Historian, "Oil Embargo, 1973-1974" | yes |
| The yield curve inverted before each recession since the late 1960s | Federal Reserve Bank of New York, "The Yield Curve as a Leading Indicator" | Estrella and Mishkin, Review of Economics and Statistics (1998) | yes |
| Real GDP and consumer spending series | Bureau of Economic Analysis, National Income and Product Accounts | FRED (GDPC1, PCEC96) | yes |
Backed twice: 8. Cut: 0.

Checks run (Python, scratchpad r23, 2026-11-09): twelve recession bands in date order from 1948 to 2020; the 2020 recession lasted 2 months; the April 2020 peak is 4.8 points above the 2009 peak; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 charts and panel; at 680x425 sheet.
2. Shading is compared with the twelve official bands, with hits and misses counted. (D2.Eco.11.9-12)
3. Six investigation cards mark the first mover and the lines that followed. (D2.Eco.10.9-12)
4. The forecast and the brief use three indicators. (D2.Eco.11.9-12)
5. The bundled data shows its pull date; the forecast stays on the device.
6. Charts use fixed domains.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no fades; no network requests.

## Open questions
- The idea card flags a data source with a scheduled refresh (default used: FRED, BEA, BLS and NBER series bundled as one data file with its pull date shown, refreshed by a build script each quarter; the runtime makes no network requests).
