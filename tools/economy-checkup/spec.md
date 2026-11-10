# Economy Checkup

## One idea
A doctor's clipboard holds a chart of the US economy's vital signs from 1995 to 2024, three lines for unemployment, inflation and real output, and Dr. Osei, a made-up economy doctor (labeled "illustration"), gives the child a checklist to read it like a patient's chart: fever means inflation over 4 percent, weakness means unemployment rising, and shrinking means output fell; the child scrubs year by year, marks each year that fails the checkup, and then compares their marks with the recession years (2001, 2008 to 2009, 2020) and the high-inflation years (2021 to 2023); then the child picks any year and four neighbors, all made up, show how it hit them differently: Mrs. Lopez the saver, whose $1,000 in cash bought about $926 worth in 2022; Mr. Chen with a fixed-rate car loan, who paid back in cheaper dollars; Grandpa Joe on a fixed pension, whose groceries cost more each month; and Tasha the job seeker, who faced about 10 percent unemployment in late 2009; the child writes one line for each neighbor in the chosen year; at the end the child sees that the same numbers tell different stories to different people, and that inflation and unemployment do not hurt everyone the same way, so a student in grades 6 to 8 learns to read unemployment, inflation and output data and explain who they hurt.

## Not like
- economy-dashboard (12, spec): a full dashboard with forecasting. Here three vital signs and four neighbors.
- interest-rate-dial (6, spec): rates and borrowing. Here how a year hits different people.
- box-plot-builder (6, spec): statistics. Here reading real economic data.
- startup-shares (Grades 6-8, spec): investing in young companies. Here the whole economy's health.

## Who and how
- Grades 6-8, Economics (CTE explore), module "Economy Checkup". Standards: D2.Eco.11.6-8 (use economic data to evaluate employment, unemployment, inflation, production, income and growth), D2.Eco.12.6-8 (explain how inflation, deflation and unemployment affect different groups), C3 Framework.
- Format: data. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every point and card. Controls 48 px or more.
- Thirty years, three lines, the checklist, four neighbors, one line each. Extra: Year draw (the class draws a year and argues who it hurt most on the projector). tool.json `modes: ["Checkup", "Year draw"]`, `minutes: "20-30"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.11.6-8 | Scrub the years; mark failed checkups; compare | marks against recession and inflation years | 2 |
| D2.Eco.12.6-8 | Pick a year; write each neighbor's line | four different stories | 3 |

## Screens and modes
Header (kit): title "Economy Checkup"; `Checkup`, `Year draw`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The clipboard chart with three lines, the checklist, and Dr. Osei with a stethoscope. The welcome is queued (`welcomeAfter: true`): "Let's read the economy's chart. Drag the year marker to start." First hint: "Drag the year marker."

**Checkup (focus: the chart).** At 1366x768 the chart is left with the checklist right; at 680x425 the checklist is a sheet. The marker shows each line's value for the year. The child taps `Mark sick` or `Healthy`, with the failed checks named.

**Compare.** `Show the record` shades recession years and high-inflation years; the child's marks sit on top, with matches and misses named (2001 had low inflation but rising unemployment).

**Four neighbors.** The child picks a year; four cards show each neighbor's numbers for that year; the child writes one line each from chips or types.

**Same numbers, different stories (the aha).** Dr. Osei: "One chart, four patients. Inflation hurt the saver and helped the borrower. Unemployment hit the job seeker hardest."

**The end.** The marked chart and the four lines. `Print` prints them.

**Year draw (extra).** Class play.

## Content
- Annual data from FRED: unemployment rate (BLS), CPI inflation (BLS), real GDP growth (BEA), 1995 to 2024, with the series names and the date pulled shown under the chart.
- Neighbors are made up and labeled "illustration"; their numbers come from the year's data.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Marks can be changed until `Show the record`; any year can be picked for the neighbors.
- Keyboard: arrows move the year marker; Tab to mark buttons, the record, neighbor cards and chips; Enter picks.
- With Motion off lines draw at once.

## Look
- Accent `--brand` #136060 clipboard teal (header, the chart frame, buttons); gold #f4c542 (the year marker, a failed check); paper #ebf5f4; ink #052120; muted #4a5857.
- Contrast (WCAG 2.1, computed): white on brand 7.32:1; brand on paper 6.59:1; ink on paper 15.18:1; muted on paper 6.69:1; ink on gold 10.37:1.
- Never color alone: the three lines carry dash styles and labels; shaded years carry names.
- Different from this batch (late-night indigo, ski-lift red, pitch-fair green, crayon magenta).

## Art
- People (illustrated): Dr. Osei and four neighbors, labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Drawn in code: the chart, the checklist and neighbor cards.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as Dr. Osei; `news-reader` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.year + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `scrub`: "Drag the year marker."
- how `mark`: "Tap Mark sick or Healthy."
- how `record`: "Tap Show the record."
- how `year`: "Pick a year for the neighbors."
- how `line`: "Pick chips to write each neighbor's line."
- event, whole, same numbers, different stories.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the three series as a bundled JSON file, the checklist rules, recession shading, neighbor numbers from the year's data.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Marks | Mark every year sick | Each mark names the failed check, and healthy years have none. |
| Compare | Skip it | The neighbors open after the record. |
| Lines | Copy one line for all four | Each line must name that neighbor's number. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `scrub`; `mark`.
2. `record`.
3. `year`; `line`.
4. Same numbers, different stories (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 D2.Eco.11.6-8 and D2.Eco.12.6-8 wording | data/standards/c3-indicators.txt | data/modules.csv module line | yes |
| Unemployment peaked near 10 percent in October 2009 | U.S. Bureau of Labor Statistics, series UNRATE via FRED | BLS (2012), "The Recession of 2007-2009", Spotlight on Statistics | yes |
| CPI inflation was about 8 percent in 2022 | U.S. Bureau of Labor Statistics, CPI-U annual average via FRED | Congressional Budget Office (2023), "The Budget and Economic Outlook" | yes |
| Recession dates 2001, 2007 to 2009 and 2020 | National Bureau of Economic Research, "US Business Cycle Expansions and Contractions" | U.S. Bureau of Economic Analysis, real GDP (GDPC1) via FRED | yes |
| Inflation hurts savers and fixed incomes and helps fixed-rate borrowers | Federal Reserve Bank of St. Louis, "Who wins and who loses from inflation" (Page One Economics) | Federal Reserve Bank of Cleveland, inflation education resources | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad s27, 2026-11-10): $1,000 after 8.0 percent inflation buys about $926; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 chart and checklist; at 680x425 checklist as a sheet.
2. Thirty years are marked and compared with the record. (D2.Eco.11.6-8)
3. Four neighbor lines are written for a chosen year. (D2.Eco.12.6-8)
4. Series names and the date pulled show under the chart.
5. Data is bundled; nothing is fetched live.
6. `Read` reads every point and card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: lines draw at once; no network requests.

## Open questions
- Overlap with economy-dashboard (default used: keep; this one is grades 6-8 with three signs and four neighbors, no forecasting).
