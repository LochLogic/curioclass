# Climate Dashboard

## One idea
Three real records on one time axis (global temperature, carbon dioxide at Mauna Loa, September Arctic sea ice) and a
trend window you drag across them: a 5-year window can show warming or cooling, a 12-year window since 1975 never
shows cooling, and the long trend comes out of the year-to-year weather noise as the window widens.

## Not like
- which-model-wins (gr 9 math, wave 2): fitting models to data sets and reading their parameters. Here one simple
  trend line, and the question is the climate system: signal, noise and what drives each.
- feedback-loop-builder (this group): the causes as a loop diagram. Here the measurements.
- population-dashboard (gr 12 environmental, this wave): human population data. Here climate records.
- data-desk-distributions (wave 2 math): distributions and spread. Here time series and trends.
- outbreak-model (gr 11, built): a model run forward. Here the past is data, and only Futures uses models, with their
  ranges shown.

## Who and how
Grade 9, Earth and space science (Climate Systems). Students drive, 30 to 45 minutes. Explore first: Records opens
with all three records drawn and the hover readout live.
Standards: HS-ESS2-4, HS-ESS2-6, HS-ESS3-5, HS-ESS3-6.
tool.json: driver "students", minutes "30-45", modes ["Records", "Trend Window", "Drivers", "Futures"].

## Screens and modes
Header (kit, 9-12 theme): "Climate Dashboard", small line "Signal and noise, side by side." Modes `Records`, `Trend
Window`, `Drivers`, `Futures`; kit `Motion`, `Sound`, `Read`. A line under every chart: "Data as of ..." (Content).

### Records (explore, default)
Three stacked charts sharing one year axis (1880 to the latest year): temperature anomaly (°C), CO2 (ppm), September
sea ice extent (million km²). Hovering or tapping a year shows all three values on one readout ("2012: +0.65 °C,
394.1 ppm, 3.57 million km²").
Filters: Smoothing `None` / `5-year` / `10-year` (centered running mean, drawn over faint yearly bars); CO2 `Yearly` /
`Monthly` (monthly shows the seasonal sawtooth); Baseline `1951 to 1980` / `1880 to 1900` (shifts the temperature axis
by 0.22 °C and relabels it); `Zoom` brush on the year axis (double-click resets).
A `Seasons` card opens beside the monthly CO2: "CO2 peaks in May and dips in September and October each year, as
Northern Hemisphere plants grow in summer and take carbon from the air." (Content: 2026 swing 6.27 ppm.)

### Trend Window
The temperature chart (or the sea ice chart, picked with `Temperature` / `Sea ice`) with a draggable window: drag
its middle to move it, its edges to resize (3 years to the whole record). The least squares line through the window's
yearly values draws in the accent with its slope "+0.21 °C per decade". Under it:
- A strip chart of every window of the current length since 1975 (sea ice: since 1979), each a dot at its start year
  colored by slope sign. Readout: "Windows of 5 years: 10 of 47 show cooling. Slopes from −0.46 to +1.05."
- `Cherry picker` card: "Find a window that shows cooling." Accepted for any window with a negative slope; the card
  then asks "Now find one 12 years or longer." The answer since 1975 is none; the card says so after two tries.
- Sea ice: the same idea; 15-year windows ending in 2025 or 2026 show tiny rises (+0.002 and +0.042 million km² per
  decade) while the full record is −0.74 per decade. Strip: "Ice loss has slowed since 2012; the long record still
  falls."

### Drivers
For HS-ESS2-4. The temperature chart with markers that toggle on: `Volcanoes` (Agung 1963, El Chichón 1982, Pinatubo
1991; ash and sulfate haze reflect sunlight for a year or two), `El Niño` (1997 to 98, 2015 to 16, 2023 to 24; the
Pacific releases heat), `Sun` (11-year cycle; sunlight changes by about 0.1 percent). Beside the chart, "Time scale
cards" sorted by how fast each driver works: ocean cycles (years), volcanoes (one to two years), the Sun's cycle (11
years, small), greenhouse gases (decades to centuries), Earth's orbit (tens of thousands of years, the ice ages).
An "Energy in, energy out" gauge: satellites show Earth taking in more energy than it gives off, about 1 watt per
square meter around 2019, roughly double 2005.

### Futures
For HS-ESS3-5 and HS-ESS3-6. Two panels picked with `Scenarios` and `Carbon budget`.
- Scenarios: the observed record plus five shaded IPCC bars for 2081 to 2100 (Content), each named only by its
  emissions path ("very low", "low", "intermediate", "high", "very high"), with its likely range drawn as a bar, not a
  line. Strip: "Every scenario has a range. The biggest difference between them is how much CO2 is emitted."
- Carbon budget: a small box model. Emissions path slider choices: `Hold steady at 40` (billion tonnes of CO2 a
  year), `Fall to zero by 2050`, `by 2070`, `by 2100`. Outputs: total emitted from 2025 to 2100, about half staying in
  the air (ppm added), and added warming from the IPCC ratio (0.45 °C per 1,000 billion tonnes, likely 0.27 to 0.63).
  A line: "When CO2 emissions reach zero, warming from CO2 roughly stops rising."

## Content
Data pulled at build (scripts in the tool's build notes; the builder records the pull date and file version and
checks these values before shipping):
- Temperature: NASA GISS GISTEMP v4, global land and ocean, annual J-D column, base 1951 to 1980,
  https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv (pulled 2026-10-27; 1880 to 2025). Check values: 1880
  −0.17, 1910 −0.44, 1944 0.20, 1963 0.05, 1964 −0.20, 1976 −0.10, 1991 0.41, 1992 0.22, 1998 0.61, 2012 0.65, 2016 1.01,
  2020 1.01, 2023 1.17, 2024 1.28, 2025 1.18. Warmest ten: 2024, 2025, 2023, 2016, 2020, 2019, 2017, 2015, 2022, 2018.
  1880 to 1900 mean −0.218 (2024 is 1.50 above it). Ten-year means ending 2000: 0.380; 2010: 0.621; 2020: 0.833; 2025:
  1.013.
- CO2: NOAA GML Mauna Loa annual means, https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt (file of 9
  October 2026; 1959 to 2025), and monthly means co2_mm_mlo.txt (to September 2026). Check values (ppm): 1959 315.98,
  1970 325.68, 1980 338.76, 1990 354.45, 2000 369.71, 2010 390.10, 2012 394.06, 2020 414.21, 2024 424.61, 2025 427.35;
  growth 2024 +3.53, 2025 +2.74. Monthly 2026: May 432.34, September 426.07 (swing 6.27); 2025: May 430.51, September
  424.37 (6.14).
- Sea ice: NSIDC Sea Ice Index version 4 (G02135), September monthly extent, northern hemisphere,
  https://noaadata.apps.nsidc.org/NOAA/G02135/north/monthly/data/N_09_extent_v4.0.csv (file of 2 October 2026;
  1979 to 2026). Check values (million km²): 1979 7.05, 1996 7.58, 2007 4.27, 2012 3.57 (record low), 2020 4.00, 2025
  4.75, 2026 4.81; 1981 to 2010 mean 6.413.
Trends (least squares on yearly values, computed 2026-10-27):
- Temperature (°C per decade): 1880 to 2025 0.083; 1975 to 2025 0.207; 1998 to 2012 0.134; 2015 to 2025 0.296; 1940
  to 1975 −0.019; 1910 to 1945 0.14; 2015 to 2022 −0.044.
- Windows since 1975 (start 1975 or later, ending by 2025): 5 years, 10 cooling windows, slopes −0.46 to +1.05; 8
  years, 6 cooling (for example 1987 to 1994, −0.126; 2015 to 2022, −0.044); 10 years, 1 cooling (1987 to 1996,
  −0.008, after Pinatubo); 12 years or longer, none (12-year slopes 0.049 to 0.373; 20-year 0.113 to 0.316).
- CO2: 1959 to 2025, 1.672 ppm per year; 1959 to 1968, 0.755; 2016 to 2025, 2.522.
- Sea ice: 1979 to 2026, −0.741 million km² per decade (−11.6 percent of the 1981 to 2010 mean per decade); 2012 to
  2026, +0.042.
Futures:
- IPCC AR6 WG1, Table SPM.1, warming for 2081 to 2100 above 1850 to 1900 (best estimate, very likely range): very low
  (SSP1-1.9) 1.4 (1.0 to 1.8); low (SSP1-2.6) 1.8 (1.3 to 2.4); intermediate (SSP2-4.5) 2.7 (2.1 to 3.5); high
  (SSP3-7.0) 3.6 (2.8 to 4.6); very high (SSP5-8.5) 4.4 (3.3 to 5.7).
- Warming per cumulative CO2 (TCRE): 0.45 °C per 1,000 GtCO2, likely 0.27 to 0.63 (AR6 SPM D.1.1). 1 ppm CO2 = 2.124
  GtC = 7.8 GtCO2 (Global Carbon Budget). Today's emissions about 40 GtCO2 a year (Global Carbon Budget 2024: 41.6
  projected for 2024); the box model keeps about half in the air.
- Carbon budget check values (yearly emissions summed 2025 to 2100; falling paths drop in a straight line from 40 in
  2025 to 0 in the target year): hold steady 3,040 GtCO2, +1.37 °C (0.82 to 1.92), +195 ppm; zero by 2050, 520 GtCO2,
  +0.23 °C (0.14 to 0.33), +33 ppm; by 2070, 920, +0.41 (0.25 to 0.58), +59 ppm; by 2100, 1,520, +0.68 (0.41 to 0.96),
  +97 ppm. Added on top of human-caused warming so far, about 1.3 °C (2023).
- Earth's energy imbalance: about 0.5 W/m² in 2005, about 1.0 in 2019 (CERES satellites).
Model notes on screen: trend lines are straight-line fits to yearly values; the box model leaves out other gases,
aerosols and changing sinks; scenario bars are IPCC assessed ranges, not predictions of one year.

## Interactions in detail
- Smoothing is a centered running mean; the first and last 2 (5-year) or 5 (10-year) years show as faint yearly bars
  only with a note "too close to the edge to smooth".
- Trend Window: snaps to whole years; slope shown to 3 decimals with the unit; windows under 3 years refused. Sea ice
  windows start no earlier than 1979.
- Strip chart dots: tap a dot to move the window there.
- Baseline toggle changes labels and the axis only; trends never change with the baseline (a note says so).
- Futures: switching paths animates the cumulative bar; outputs to 2 decimals for °C with the range in brackets.
- Sound: off by default for data; a soft tick per window move with Sound on.
- Keyboard: arrows move the window 1 year, Shift+arrows resize; Tab reaches filters and markers.
- Layout by real stage pixels: wide (three charts stacked beside the panel), compact, stack (375 wide: one chart at a
  time with `Temperature` / `CO2` / `Sea ice` tabs).
- Mode change: `Curio.stop()`, `V.hush()`. Last filters per device (localStorage `curio-climate-dashboard`,
  try/catch), `Reset view`.

## Look
Accent (`--brand`) #94c4c4, sea glass: 9.03:1 on --panel #141b25, 8.55:1 on --sec-bg #18202b; --brand-ink #10161f on
it 9.47:1. Moved off a brighter mint (#9ee6d8) that sat close to tree-of-life's #b8ead3; nearest now speedometer
#c7d2de, city-skyline #6fd6e8 and gas-law-lab #9ec9e8 (ΔE 16 to 17).
Charts: temperature bars blue `--gr-1` below zero and `--gr-4` above, smoothed line #e8edf3; CO2 `--gr-3`; sea ice
#c8e4ff; trend line in the accent; markers volcano #c9a0ff, El Niño #ffb070, Sun #ffe08a. Calm, no red alarm
backgrounds; numbers carry the message.

## Art
none: drawn in code (charts, markers, gauge, bars, preview.svg).

## Voice
`hs-narrator` (Kore), style "Read clearly and naturally, at a moderate pace, like a calm science reporter." No 9-12
science tool uses it (news-reader went to population-dashboard, the other science data dashboard). `Curio.voice`, `scope: () => state.mode`.
- records (how, Records welcome): "Three records, one time line. Tap any year to read all three."
- window (how, Trend Window welcome): "Drag the window. Short windows can point anywhere. Then make it wider."
- cooling (event, first cooling window found; stale on a window change): "That window shows cooling. Now try one twelve years or longer."
- none (event, Cherry picker second try at 12 years; stale on a mode change): "Since 1975, no window that long shows cooling."
- drivers (how, Drivers welcome): "Turn on the markers and match each wiggle to its cause."
- futures (how, Futures welcome): "Pick an emissions path and read the range, not just the middle number."

## Family engine
none. Charts use `kit/graphing.js` `Plane` if present (`g.trace`, `g.segment`), otherwise the tool's own SVG; the
data-desk family is not used (time series only).

## Sources
- NASA GISS, GISTEMP Team, GISS Surface Temperature Analysis version 4 (GHCN-v4 and ERSST v5), pulled 2026-10-27,
  https://data.giss.nasa.gov/gistemp/
- NOAA Global Monitoring Laboratory, Mauna Loa CO2 annual and monthly means (Lan, Tans and Thoning), files of 9
  October 2026, https://gml.noaa.gov/ccgg/trends/
- NSIDC Sea Ice Index version 4 (Fetterer et al.), September extent file of 2 October 2026,
  https://nsidc.org/data/g02135
- IPCC AR6 WG1 Summary for Policymakers (2021): Table SPM.1 and D.1.1 (TCRE), https://www.ipcc.ch/report/ar6/wg1/
- Global Carbon Budget 2024 (Friedlingstein et al. 2025, Earth System Science Data 17:965): emissions and 2.124 GtC
  per ppm, https://globalcarbonbudget.org/
- Human-caused warming about 1.3 °C in 2023: Forster et al. 2024, "Indicators of Global Climate Change 2023", Earth
  System Science Data 16:2625.
- Earth's energy imbalance doubling 2005 to 2019: Loeb et al. 2021, Geophysical Research Letters 48:e2021GL093047.
- Volcano and El Niño effects; solar cycle about 0.1 percent: NASA Science, "Climate Change: Vital Signs" and NASA,
  "What Is the Sun's Role in Climate Change?" (2019), https://science.nasa.gov/climate-change/
- Seasonal CO2 cycle and plants: NOAA GML, "Trends in Atmospheric Carbon Dioxide" (seasonal cycle notes).
- Every trend and box model value computed in Python (2026-10-27).

## Done when
1. Hover 2012 reads +0.65 °C, 394.06 ppm, 3.57 million km²; data-as-of lines name the three files and dates.
2. Trend Window 1975 to 2025 reads +0.207 °C per decade; 1880 to 2025 reads +0.083.
3. 5-year windows strip: "10 of 47 show cooling", slopes −0.46 to +1.05; 12-year windows: none cooling.
4. Cherry picker accepts 2015 to 2022 (−0.044) and, at 12 years, says none exist after the second try.
5. Sea ice 1979 to 2026 reads −0.741 per decade; 2012 to 2026 reads +0.042 with the slowing note.
6. Baseline 1880 to 1900 shifts 2024 to +1.50 and leaves every trend unchanged.
7. Monthly CO2 shows the 2026 May peak 432.34 and September low 426.07.
8. Carbon budget: hold steady gives 3,040 GtCO2 and +1.37 °C (0.82 to 1.92); zero by 2050 gives +0.23.
9. How-to lines once each; event lines as listed.
10. Three charts visible at 1366x768; tabs at 375 wide; labels at least 10 px in the 680x425 preview; no network at
    run time, no images, no em dashes.

## Open questions
- [climate-dashboard] Futures names scenarios only by emissions level (very low to very high) and shows IPCC ranges;
  the carbon budget uses one ratio (TCRE). Is that the right depth and tone for grade 9, or drop the carbon budget
  panel?
- [climate-dashboard] Data is pulled at build and frozen in the tool with "data as of" lines. Refresh it once a year
  (a scheduled rebuild), or leave it frozen?
