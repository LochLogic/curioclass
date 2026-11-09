# Warming Evidence Desk

## One idea
Every suspect faces the same questions: line up a real record (carbon dioxide, the sun, volcanic haze, fossil fuel
burning) under global temperature, ask "what did it do during this span?", and the answers from the data sort out
which factors explain the rise of the past century and which only explain a few decades or a few dips.

## Not like
- climate-dashboard (gr 9): its Drivers mode drops markers on the temperature chart and sorts causes by time scale.
  Here each factor has its own real record on the same year axis, and the student builds questions (record times
  span) whose answers fill an evidence board and then back a claim.
- feedback-loop-builder (gr 9): the causes as a loop diagram of + and - arrows. Here measured records, no diagram.
- hazard-forecaster (gr 8, same code): filters hazard records to place sensors. Here attribution of warming.
- town-footprint (gr 8): a simulated town's resource use. Here real global records only, no simulation.
- energy-accountant (gr 9 data): a ledger that must balance. Here time series lined up and questioned.

## Who and how
Grade 8, Earth and space science (Evidence of Rising Temperatures). Students drive, solo by default, 25 to 40
minutes. Standards: MS-ESS3-5. tool.json: driver "students", minutes "25-40", modes ["Ask", "Argue"].
Explore first: Ask opens with the temperature record drawn and the year readout live; every tap is a question with
an answer at once. No points, no timer. Prompts are not personal (no disclosure note needed).

## Standards map
| Code | Student action | What they see | Done when check |
|---|---|---|---|
| MS-ESS3-5 (ask questions to clarify evidence of the factors behind the rise in global temperature over the past century) | Builds questions by picking a record and a span ("What did the sun do during the fast rise, 1975 to 2023?"), including the record that is human activity (fossil fuel burning); then in Argue picks claims for each factor and backs each with up to two of their own answers | Both records drawn on one year axis with the span shaded, a trend line on each, an answer card with both numbers and a verdict (Fits, Partly, Doesn't fit), the cell filling on the evidence board; in Argue, their claims beside the scientists' after Compare | Done when 2, 3, 4 and 7 pass: the sun's fast-rise answer reads "Doesn't fit" with -0.02 W/m² per decade, the pause answers for carbon dioxide and fossil fuels raise the haze note, and Compare shows the scientists' claims only after the student has picked their own |

## Screens and modes
Header (kit): "Warming Evidence Desk", small line "Line up the records. Ask what each one did." Modes `Ask`, `Argue`;
kit `Motion`, `Sound`, `Read`. Under the charts in Ask, one small "Data as of" line (Content).

On load: Ask mode. The temperature chart is drawn; the record chart beneath it is an empty tray with the four record
buttons shown large inside it ("Pick a record to line it up"). Question bar: "What explains the rise?" Nothing
speaks before the first tap. First hint: "Tap Carbon dioxide, Sun, Volcanoes or Fossil fuels to line it up under
temperature." First tap on a record button: that record draws under temperature, span Long run is asked at once,
its answer card appears and the cell fills on the board (the welcome may be cut; BASELINE 16). First tap on the
chart: moves the year cursor and shows the readout (temperature only). A first tap on a span button with no record
picked selects the span and shades it on the temperature chart; the hint stays on picking a record.

### Ask (default)
Focus: the two stacked charts on one year axis (1880 to 2025) with the shaded span and the answer card under them;
together they fill the stage. Records and spans sit in the panel.
Layout at 1366x768 (stage about 1000 px wide, panel 360): question bar 44 px ("What did [Sun] do during [the fast
rise, 1975 to 2023]?", the two picks in the accent); temperature chart 250 px; record chart 220 px; answer card
120 px. Panel top to bottom: `Records` (2 by 2 buttons, painted icon 48 px plus name: `Carbon dioxide`, `Sun`,
`Volcanoes`, `Fossil fuels`), `Spans` (five 44 px buttons: `Long run`, `Early rise 1910-1945`, `Pause 1945-1975`,
`Fast rise 1975-2023`, `Short dips`), the axis toggle `Zoomed` / `From zero` (shown only for Carbon dioxide and
Sun), the evidence board (4 rows by 5 cells, 30 px rows, each cell a word plus icon), the hint, `Clear desk`.
Everything above the fold. At 680x425: the charts sit side by side with a compact panel; span buttons shorten to
`Long`, `Early`, `Pause`, `Fast`, `Dips`; the board folds behind a `Board` button (a popover over the panel); the
answer card shrinks to one line (verdict plus the record's number) and the full text is in the hint and Read. At
375 wide: question bar, charts, card, then panel, stacked.
What responds: picking a record redraws the lower chart (0.4 s fade, instant with Motion off) and re-asks the current
span; picking a span shades it on both charts, draws a least squares trend line in each record's color over the span
with its slope label, and shows the answer. Long run instead draws two flat bars on each chart (the 1900 to 1919 and
2004 to 2023 averages) with their values. Short dips draws four labeled vertical lines (Krakatau 1883, Agung 1963,
El Chichón 1982, Pinatubo 1991) on both charts, and on the temperature chart a small bracket from the 3-year average
before to the year after. Each answer lands on the board (cell flips with a soft stamp sound). Tapping a filled cell
asks that record and span again. Hover or drag on either chart: a cursor through both charts and a readout ("1992:
temperature +0.22 °C, volcanic haze 0.090").

### Argue
Focus: the claim table, four rows filling the stage; the panel holds the hint and, after Compare, the scientists'
summary. Layout at 1366x768: each row 110 px: painted icon 64 px and name, a mini chart (record over temperature, 160
by 60), four claim chips, and up to two evidence chips. Under the rows: "What explains most of the rise since 1900?"
with four choice chips, then `Compare` (big button). All above the fold. At 680x425: mini charts fold away; chips wrap
to two lines; `Compare` stays visible.
Claim chips per row (multi-select): `Drove the long rise`, `Helped in some decades`, `Explains short dips`,
`Doesn't fit the record` (this last one clears the others; picking another clears it). Evidence chips: the student's
own answers for that record (from the board) as small chips "Fast rise: Doesn't fit"; tap up to two to back the
claim (a third tap swaps out the oldest). A row with no answers reads "No questions asked yet. Tap Ask to question
this record." Overall choices: `Carbon dioxide from burning fuels`, `The sun`, `Volcanoes`, `Can't tell yet`.
`Compare` is disabled until every row has at least one claim chip; its hint then says "Pick at least one claim for
every record to turn on Compare." After Compare: each row shows the scientists' chips outlined beside the student's,
the word "Same" or "Different", the scientists' one-line reason and their two evidence answers ("Scientists also
point to: Fast rise", tap to jump to Ask with that record and span). The overall line reveals the scientists' finding
(Content). The panel shows "You and the scientists agree on N of 4 records." Changing a chip after Compare updates
the comparison live.
Outcomes for each row after Compare, all different at a glance: Same (row edge in the accent, "Same" with a check
icon); Different (row edge dashed muted, "Different" with a two-arrow icon); the scientists' chips always outlined.

## Content
Data pulled at build and frozen in the tool; the builder records the pull date and checks these values. Scripts:
S:/CurioClass-codex-scratch/specs/warming-evidence-desk/load.py (loads all five), periods.py, more.py (all numbers
below). Common years 1880 to 2023; temperature and carbon dioxide run to 2025, fossil fuels to 2024.
- Temperature: NASA GISTEMP v4, global land and ocean, J-D column, °C compared with 1951 to 1980,
  https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv. Checks: 1880 -0.17, 1910 -0.44, 1945 0.09, 1964
  -0.20, 1975 -0.01, 1992 0.22, 2020 1.01, 2023 1.17, 2025 1.18. Axis label "°C compared with the 1951 to 1980 average".
- Carbon dioxide (ppm): 1880 to 1958 Law Dome ice core spline (MacFarling Meure et al. 2006, column CO2spl,
  https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/law/law2006.txt); 1959 to 2025 Mauna Loa annual means
  (https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt). Checks: 1880 289.8, 1910 299.3, 1958 315.2,
  1959 315.98, 2023 421.08, 2025 427.35. A small note at 1959: "Ice core before, Mauna Loa air after."
- Sun: total solar irradiance, NRLTSI2 annual (LASP LISIRD, https://lasp.colorado.edu/lisird/latis/dap/nrl2_tsi_P1Y.csv),
  1880 to 2023, W/m² at the top of the air. Checks: 1880 1360.46, 1889 1360.25 (lowest), 2023 1362.00 (highest, a
  solar maximum). Zoomed axis 1360.0 to 1362.2 with the note "Zoomed in: the whole swing is under 0.2 percent";
  From zero shows 0 to 1400 (a flat line).
- Volcanoes: stratospheric aerosol optical depth at 550 nm ("volcanic haze"), CMIP7 v2.2.1 (Aubry et al., University
  of Exeter) as gridded by NASA GISS, https://data.giss.nasa.gov/modelforce/strataer/data/tau_reff_CMIP7-2-2-1.nc
  (variable tau, scale 0.0001; global mean weighted by cos latitude, then yearly mean), 1880 to 2023. Axis 0 to 0.11.
  Note: "Haze 0.10 dims the direct sunbeam by about 10 percent." Checks: 1884 0.101, 1964 0.026, 1983 0.033, 1992
  0.090, 2023 0.008. The four biggest peaks since 1880 are 1884, 1992, 1983, 1964.
- Fossil fuels: CO2 from fossil fuels and cement, billion tonnes a year, Global Carbon Budget via Our World in Data
  (https://github.com/owid/co2-data, World, column co2 / 1000), 1880 to 2024. Checks: 1880 0.86, 1950 5.93, 2019
  37.09, 2020 35.16, 2024 38.60. Same file, co2_including_luc, for the "about 2,650" total.
- Data as of line: "Data as of: NASA GISTEMP v4, NOAA Mauna Loa and Law Dome, NRLTSI2, CMIP7 volcanic haze, Global
  Carbon Budget (pulled [date])."

Spans and temperature (least squares on yearly values; Long run compares 20-year averages):
- Long run, 1900 to 1919 vs 2004 to 2023: temperature -0.32 to +0.78 °C, up 1.10 °C.
- Early rise 1910 to 1945: +0.14 °C per decade. Pause 1945 to 1975: +0.02 (about flat). Fast rise 1975 to 2023: +0.20.
- Short dips: the year after each of the four biggest eruptions minus the 3 years before it.

Answer cards (verdict, then text; numbers shown exactly as written):
| Record | Long run | Early rise | Pause | Fast rise | Short dips |
|---|---|---|---|---|---|
| Carbon dioxide | Fits. Rose from 299 to 399 ppm, up a third, while temperature rose 1.10 °C. It climbed the whole way. | Fits. Rising slowly, 3.6 ppm per decade, while temperature rose 0.14 °C per decade. | Doesn't fit. Kept rising, 7.0 ppm per decade, while temperature held about flat (0.02 °C per decade). Something held temperature back. + haze note | Fits. Rose fastest of all, 18.4 ppm per decade, while temperature rose fastest, 0.20 °C per decade. | Doesn't fit. Climbed smoothly through all four eruptions. It has no dips to match. |
| Sun | Partly. Up 0.37 W/m², about 0.03 percent, most of it before 1950. Small next to its own 11-year swing of about 1 W/m². | Fits. Rose 0.11 W/m² per decade while temperature rose 0.14 °C per decade. | Fits. Dipped slightly, 0.07 W/m² per decade, while temperature held about flat. | Doesn't fit. About flat (-0.02 W/m² per decade). Averaged over each 11-year cycle it slipped from 1361.11 to 1360.94. Temperature rose fastest anyway. | Doesn't fit. Its 11-year cycle changes sunlight by less than 0.1 percent, too small to make the dips after eruptions. |
| Volcanoes | Doesn't fit. No steady trend: eruptions come and go. Haze averaged 0.007 in 1900 to 1919 and 0.005 in 2004 to 2023, both thin. | Fits. The sky cleared: haze averaged 0.014 from 1880 to 1909 and 0.005 from 1910 to 1945, so more sunlight got through. | Partly. Quiet until Agung in 1963: haze averaged 0.004 from 1945 to 1962, then 0.009 from 1963 to 1975. | Doesn't fit. Two spikes, El Chichón (1982) and Pinatubo (1991), then thin haze. Spikes can't make a steady rise. | Fits. After 3 of the 4 biggest eruptions the next year was cooler than the 3 years before: Krakatau -0.16 °C, Agung -0.22, Pinatubo -0.15. El Chichón (+0.06) was hidden by a strong El Niño. |
| Fossil fuels | Fits. Rose 12 times over, from 2.8 to 34.3 billion tonnes of CO2 a year. + source note | Fits. Rising slowly, up 0.5 billion tonnes a year each decade. | Doesn't fit. Took off, up 4.4 billion tonnes a year each decade, while temperature held about flat. + haze note | Fits. Kept climbing, up 4.7 billion tonnes a year each decade, as temperature rose fastest. | Doesn't fit. Burning fell about a quarter from 1929 to 1932 and 5 percent in 2020; temperature did not dip with it. Burning acts through CO2 that builds up for years. |
- Haze note (small, under the card): "Scientists trace much of the pause to haze from burning coal and oil, which
  reflects sunlight, plus ocean swings. That pollution haze is not a record on this desk."
- Source note (Fossil fuels, Long run): "From 1880 to 2024 people released about 2,650 billion tonnes of CO2 (fuels,
  cement and cleared land). The air gained about 1,050 billion tonnes (135 ppm): about 4 of every 10. Oceans and
  plants took up the rest."
- Dips note (Short dips, any record): "Not every dip is a volcano: El Niño and La Niña swing temperature too."

Argue, scientists' claims: Carbon dioxide {Drove the long rise}, evidence Long run + Fast rise, reason "It rose the
whole century and fastest when temperature rose fastest." Sun {Helped in some decades}, evidence Early rise + Fast
rise, reason "It helped the early rise, then went flat while temperature climbed fastest." Volcanoes {Helped in some
decades, Explains short dips}, evidence Short dips + Early rise, reason "Big eruptions cool the next year or two, and
quiet decades helped the early rise." Fossil fuels {Drove the long rise}, evidence Long run + Fast rise, reason "Burning
added the carbon dioxide that drove the rise." Overall: `Carbon dioxide from burning fuels`, with the line "Scientists
find that people caused about all of the warming since the late 1800s: about 1.07 °C of the 1.09 °C measured from
1850-1900 to 2011-2020. The sun and volcanoes together added between -0.1 and +0.1 °C."

## Interactions in detail
- Trend lines: least squares on the yearly values inside the span, endpoints included; slope labels to the decimals
  in the table, unit always shown ("+0.20 °C per decade", "-0.02 W/m² per decade"). The builder checks every computed
  number against the table at load in a test hook and fails loudly on a mismatch.
- Picking the same span or record again does nothing new. Switching record keeps the span; switching span keeps the
  record. A tap during the 0.4 s fade jumps to the new state at once (no queued animations).
- Axis toggle: CO2 and Sun only; remembered per record; never changes any number. From zero on the Sun shows the
  flat line and keeps the note.
- Year cursor: snaps to whole years; years outside a record's range read "no data" for that record. Keyboard: Tab
  reaches records, spans, the axis toggle, board cells, then the chart; arrows move the cursor 1 year (Shift: 10).
- Board: 20 cells; an empty cell is a dot; a filled cell shows its verdict word and icon (check, half, cross), never
  color alone. Filled cells and Argue picks are kept on this device (localStorage `curio-warming-evidence-desk`,
  try/catch) with "Saved on this device only." under the board. `Clear desk` asks "Tap again to clear" for 3 s, then
  empties the board and every Argue pick.
- Argue: claim chips toggle; evidence chips limited to two per row; Compare disabled until four rows have claims; the
  overall choice is optional for Compare (if none, the panel says "Pick your overall answer too" and the reveal still
  shows).
- Mode change: `V.hush()`, `Curio.stop()`; Ask keeps its record and span.
- Sound (kit, starts on): voice, a soft stamp (Curio.tone 180 Hz, 60 ms) when a cell fills, nothing else.

## Look
Desk at night. --paper #14120f, --panel #1e1a15, --sec-bg #27211a, --ink #f3ede2, --muted #bfb3a1, --line #3a332a,
--focus #ffffff (3 px ring), accent --brand #ffb36b (desk-lamp amber), --brand-ink #1a1208.
Records, each with its own color and line style so color is never the only signal: temperature #ff7a6e thick solid;
carbon dioxide #7cc8ff solid; sun #ffe066 thin with dots at each year; volcanoes #c7a6ff filled bars; fossil fuels
#a8d18d filled area with a dotted top. Span shading: accent at 14 percent. Verdict chips: Fits #b6f0bd on #24402b
(8.78:1), Partly #ffd76b on #3d3518 (8.82:1), Doesn't fit #ffaaa0 on #44201f (7.82:1), each with its icon.
Contrast on --paper: ink 16.05, muted 9.06, accent 10.61, temperature 7.36, CO2 10.29, sun 14.34, volcanoes 9.19,
fossil 10.84; on --panel all above 6.8; brand-ink on accent 10.51.
Neighbors: climate-dashboard #94c4c4 (ΔE 64), feedback-loop-builder #ffb0d9 (58), energy-accountant #d3b069 (19,
the nearest), population-dashboard #f261ce (91), water-shapes-earth #58acac (73), span-and-spire #ff6fae (68).

## Art
Painted record icons (local FLUX; no people). Each sits in a circle crop, so the subject is centered inside the inner
80 percent. Shown at 48 px (Ask record buttons, tray), 72 px (beside the record chart title) and 64 px (Argue rows);
all of it shows in each spot.
- icon-co2: Mauna Loa observatory, white domed buildings and a tall mast on black lava slopes above a sea of clouds,
  deep blue sky; 1:1; cutout no; people no.
- icon-sun: the sun's glowing orange disk through a solar filter with a few dark sunspots, black sky around; 1:1;
  cutout no; people no.
- icon-volcano: a tall gray-white eruption column rising from a green tropical volcano into a blue sky, seen from far
  away; 1:1; cutout no; people no.
- icon-fossil: a coal power plant at dusk with tall smokestacks and white steam plumes, a coal train in front; 1:1;
  cutout no; people no.
- icon-temp: a white louvered weather-station box on four legs in a green grassy field under a wide sky; 1:1; cutout
  no; people no. Used beside the temperature chart title.
Charts, board, chips and labels are drawn in code.

## Voice
Bank `friendly-dad` (Achird), restyled: "Say in a relaxed, curious way, like a science teacher sorting evidence at a
desk with a student." Neighbors: climate-dashboard hs-narrator, feedback-loop-builder clear-teacher,
energy-accountant calm-professor, molecule-forge knowing-guide, span-and-spire firm-captain. `Curio.voice`,
`scope: () => state.mode`. Answer cards are read on screen, not spoken; Read speaks the current answer card when one
is showing, else the hint.
- ask (how; Ask welcome; stale once a record is picked): "Temperature rose about one degree in a century. Tap Carbon
  dioxide, Sun, Volcanoes or Fossil fuels to line it up under temperature."
- span (how; after the first answer card; stale once a span is tapped; needs the span buttons): "Now tap a span, like
  Fast rise, to ask the same record a sharper question."
- zoom (how; first time Sun is drawn on a zoomed axis; stale when the axis toggle is used or the record changes):
  "The sun's axis is zoomed in. Tap From zero to see how big the change really is."
- dips (how; first time Short dips is asked; stale on a span change): "The four lines mark the biggest eruptions.
  Look at temperature the year after each one."
- board (how; once all four records have at least one answer; stale when Argue opens; needs the Argue button):
  "Every record has an answer on your board. Ask more, or tap Argue."
- argue (how; Argue welcome; stale once a claim chip is tapped): "For each record, tap the claims your evidence
  supports. Then tap Compare."
- evidence (how; after the first claim chip in a row that has answers; stale once an evidence chip is tapped):
  "Tap up to two of your answers to back that claim."
- agree0 to agree4 (event; on each Compare; whole): "You and the scientists agree on [none / 1 / 2 / 3 / all 4] of
  the records." Five fixed lines: "...agree on none of the records.", "...on 1 of 4 records.", "...on 2 of 4
  records.", "...on 3 of 4 records.", "...on all 4 records."
- finding (event; right after the agree line, as one sequence, whole): "Scientists find that people caused about all
  of the warming since the late 1800s."
How lines speak once per page load, then only update the hint; events speak on every Compare. No line names Compare
while it is disabled (the needCompare hint is text only).

## Family engine
none. Charts may use `kit/graphing.js` `Plane` (`g.segment`, `g.label`, `g.trace`) if it fits two stacked time
series; otherwise the tool's own SVG, laid out by real stage pixels per size.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Temperature rose 1.10 °C (1900-1919 to 2004-2023); span trends 0.14, 0.02, 0.20 °C per decade | NASA GISTEMP v4 (computed) | NOAA NCEI GlobalTemp, Climate at a Glance annual (computed: 1.04; 0.13, 0.01, 0.19) | Yes, within 0.06 |
| CO2 about 290 ppm in 1880 rising to 427 in 2025 | Law Dome, MacFarling Meure et al. 2006 + NOAA GML Mauna Loa | Scripps CO2 program (Keeling) Mauna Loa record; IPCC AR6 WG1 Ch2 | Yes |
| Sun's output about 1361 W/m²; 11-year cycle changes it by under 0.1 percent; no rise since the 1950s | NRLTSI2 (Coddington et al. 2016, BAMS) computed: cycle swings 0.68 to 1.24 W/m² (0.05 to 0.09 percent), cycle means 1361.11 to 1360.94 | Kopp and Lean 2011 (GRL 38:L01706); NASA "What Is the Sun's Role in Climate Change?" (2019); IPCC AR6 WG1 Ch2 2.2.1 | Yes |
| Four biggest eruptions since 1880: Krakatau 1883, Agung 1963, El Chichón 1982, Pinatubo 1991 | CMIP7 v2.2.1 haze peaks 1884, 1992, 1983, 1964 | GISS Sato et al. 1993 tau.line (peaks 1884, 1992, 1983, 1964 tied with 1903); Smithsonian GVP eruption dates | Yes |
| Eruptions cool the next year or two; El Chichón masked by the 1982-83 El Niño | Robock 2000, Rev. Geophys. 38:191 | NOAA NCEI dips computed (Krakatau -0.13, Agung -0.21, El Chichón +0.05, Pinatubo -0.12); USGS Pinatubo fact sheet 113-97 | Yes |
| Haze 0.10 dims the direct beam about 10 percent | Beer-Lambert: e^-0.10 = 0.905 | NASA Earth Observatory, Aerosol Optical Depth | Yes |
| Fossil and cement CO2 2.8 to 34.3 Gt a year; dips 1929-32 and 2020 | Global Carbon Budget 2024 (Friedlingstein et al. 2025, ESSD 17:965) | CDIAC/OWID series of the same; IEA Global Energy Review 2021 (2020 drop about 5.8 percent) | Yes (5.2 vs 5.8, shown as "5 percent") |
| About 4 of every 10 tonnes stays in the air | Computed: 1,052 of 2,649 Gt since 1880 = 0.40 (7.8 GtCO2 per ppm, GCB) | IPCC AR6 WG1 SPM B.4.1 (sinks took about 56 percent a year over six decades) | Roughly: 40 vs 44 percent, so "about 4 of every 10" |
| Mid-century pause linked to sulfate pollution haze plus ocean swings | IPCC AR6 WG1 Ch3 3.3.1 | Wilcox, Highwood and Dunstone 2013, ERL 8:024033 | Yes |
| Early-century warming had mixed causes (rising sun, quiet volcanoes, early greenhouse gases, ocean swings) | IPCC AR6 WG1 Ch3 3.3.1 | Hegerl et al. 2018, BAMS 99:2313 | Yes |
| People caused about 1.07 of 1.09 °C (1850-1900 to 2011-2020); natural drivers -0.1 to +0.1 | IPCC AR6 WG1 SPM A.1.3 | Forster et al. 2024, ESSD 16:2625 (human-induced 1.19 of 1.19 °C, 2014-2023) | Yes |
| El Niño and La Niña swing global temperature | NOAA Climate.gov ENSO pages | NASA Earth Observatory, El Niño | Yes |
Cut: a "combine the factors" model mode (regression fitted the sun alone at an unphysical 2.2 °C per W/m²; a fixed
one-box model needed parameters with no grade 8 meaning), methane (no clean annual record to 1880 checked here).
Number checks (Python, 2026-11-05, files pulled that day): every check value and every number in the answer table
from load.py, periods.py and more.py. Temperature dips by GISTEMP and NOAA. Rounding: haze 0.00748 shows 0.007,
0.00547 shows 0.005; fossil 4.3506 shows 4.4. Argue agreement through behaviors (argue.py): the scientists' picks 4
of 4; every chip on (claims 1 to 3) 0; every row "Doesn't fit" 0; "everything drove it" 2; "the sun drove it" 3;
"natural only" 0; volcanoes dips only 3. Nothing a student can mash scores better than reasoning. Contrasts and ΔE
computed (colors.py).

## Done when
1. First tap on `Carbon dioxide` draws it under temperature and shows the Long run card "Fits. Rose from 299 to 399
   ppm..." with both 20-year bars; the board cell fills.
2. Sun with `Fast rise 1975-2023` shows trend -0.02 W/m² per decade, temperature +0.20, verdict Doesn't fit.
3. `Pause 1945-1975` for Carbon dioxide and for Fossil fuels shows Doesn't fit plus the haze note.
4. `Short dips` draws four eruption lines and the brackets read Krakatau -0.16, Agung -0.22, El Chichón +0.06,
   Pinatubo -0.15.
5. Sun `From zero` shows a flat line; every number stays the same.
6. Hover 1992 reads temperature +0.22 °C and the shown record's 1992 value (haze 0.090).
7. Argue: Compare is disabled until four rows have claims; picking the scientists' claims gives "agree on all 4";
   the scientists' chips are not visible before Compare.
8. Focus: at 1366x768 in Ask the two charts plus answer card are the largest thing on the stage; in Argue the
   claim table is.
9. Tap while anything plays: tapping a second span during the 0.4 s fade lands on the second span's card at once.
10. Fold: at 1366x768 every Ask control (records, spans, board, Clear desk) and `Compare` are above the fold; at
    680x425 the board folds behind `Board` and text stays 10 px or more.
11. How lines once each, events on every Compare; no line names a disabled control; board saved on this device with
    the privacy line; no network, no em dashes.

## Open questions
- Settled 2026-11-05 by BASELINE rules 2 and 9 (lean to the real-world factor, teach it well): the builder adds a
  sixth record, sulfur dioxide emissions (CEDS), if it backs the yearly series with a second source (for example
  Smith et al. 2011 or the EDGAR inventory) and states its licence; it joins the Pause span like the other records.
  If no second source agrees, keep the note and say so in notes.md.
- Settled 2026-11-05: the data stays frozen at build with its "Data as of" line, refreshed with climate-dashboard at
  its yearly review.
