## What it teaches

Students ask questions of real climate records by choosing a factor and a span of years. They can use their answers
to explain why one factor fits a century of warming, another helps in some decades, and eruptions explain short dips.

## Key skills

- Compare two records over the same years.
- Separate a sustained trend from a repeating cycle or a short spike.
- Use averages and trend lines without confusing their different questions.
- Back a claim with evidence and revise it after a comparison.
- Recognize that fossil fuel burning adds carbon dioxide to the air.

## Support at home

- Ask your child why one cool year cannot settle a question about a century. Compare this with a familiar long change,
  such as how a plant grows even though a few leaves fall.
- Talk about the difference between an amount added each year and an amount that has built up. Water added to a sink
  is a useful analogy, including the drain that removes some of it.
- Ask what evidence would change a claim. Let each person name a question before offering an answer.

## A 5-minute start

1. Tap Carbon dioxide. Find the two 20-year average bars and the answer stamped on the board.
2. Tap Fast rise, then Sun. Ask whether both records rose during the same years.
3. Tap From zero. The axis changes, but the values and the answer do not.
4. Ask Pause for carbon dioxide and fossil fuels. Read the pollution-haze note.
5. Gather an answer for every record, open Argue, choose claims, select evidence and tap Compare.

## Modes

**Ask:** Four records, five questions each. Long run compares 1900-1919 with 2004-2023 averages. Early, Pause and Fast
use an ordinary least squares line with both endpoint years included. Short dips compares the year after an eruption
with the average of the three preceding years. A cursor reads individual years. There are no values invented beyond
each record's last year. Zoomed and From zero change only the vertical scale.

**Argue:** Students choose their claims before seeing the scientists' claims. Doesn't fit clears the other claims
in that row. Select at most two of your own answers per record; choosing a third replaces the oldest. Compare becomes
available after all four records have a claim; the overall answer is optional. Same and Different compare the entire
set of claims, not just whether one selected chip happens to match. Evidence choices are for discussion, not a score.
After Compare, revising a chip updates the comparison. This is an open evidence desk, not a test or mastery certificate.
The on-screen comparison explicitly checks claims only. A matching claim can still have weak or contradictory evidence;
ask students to explain the two answers they selected before treating their case as supported.

## Talk questions

- Why does carbon dioxide fit the long rise but fail to explain the mid-century pause on its own?
- What does the sun's recent record tell you that its early-century record alone would miss?
- Why is a sudden eruption a different kind of explanation from a persistent rise?
- Which two answers most strongly support your claim? Which answer could challenge it?
- How are fossil fuel emissions per year different from the concentration of carbon dioxide already in the air?

## Good to know

MS-ESS3-5 is practiced through the student's own factor-and-span questions, not only a teacher discussion.
Fits means the pattern is consistent in that span; two aligned lines alone do not prove a cause. The scientists'
attribution also draws on physical understanding and other evidence, represented by the IPCC finding after Compare.
Temperature uses the 1951-1980 baseline; the IPCC finding uses 1850-1900. These are different comparisons.

The tool saves only the asked board cells and claim/evidence choices on this device. It sends nothing anywhere.
Clear desk requires a second tap within three seconds. It empties the saved board and all Argue picks.
On phones, use the question dock for records, spans and axis scale. Scroll the workspace to reach the full board;
the header and quick controls stay in place. Short landscape windows show all claim and evidence choices in four
columns. After Compare, scroll those cards to read the scientists' reasons and inspect their evidence links.
On phones, the next-action hint stays beside the fixed controls in both modes, including while the worksheet scrolls.
Motion off removes fading, stamping and lamp movement. Sound off silences narration and the stamp; Read still reads.
Fixed voice scripts use friendly-dad (Achird). This Build has no recordings and uses the kit's browser voice fallback.

The open-question condition for sulfur dioxide is not met: no paired CEDS/independent-inventory annual series has been
validated and licensed for this build. The pollution-haze note is retained, as the spec explicitly permits. There are
four factor records plus the temperature reference. Data stays frozen and should be refreshed at the yearly review
alongside climate-dashboard.

## Data and sources

The supplied source snapshot was pulled on 2026-11-05 and independently processed during this Build on 2026-11-06.
Annual series and checks are bundled in data.json. The source-file sizes and SHA-256 values are in Scratch.
Illustrations show the type of station or facility, not documentary photographs of its exact buildings.
The facility medallion was redrawn during the cold review with the built-in OpenAI image tool, using the scientific
editorial gouache prompt in art/prompts.json. Its final asset is art/icon-fossil.webp; its original is preserved in Scratch.

- [NASA GISTEMP v4 annual global land/ocean record](https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv):
  J-D column, temperature anomalies in degrees Celsius. NASA data is public-domain US government work.
- [Law Dome ice-core record](https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/law/law2006.txt):
  MacFarling Meure et al. 2006, CO2spl through 1958, with the original research credited.
- [NOAA GML Mauna Loa annual means](https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt):
  1959-2025, parts per million. The join is marked on the chart. NOAA data is US government public data.
- [NRLTSI2 annual solar irradiance via LASP LISIRD](https://lasp.colorado.edu/lisird/latis/dap/nrl2_tsi_P1Y.csv):
  Coddington et al. 2016, watts per square meter at the top of the atmosphere, through 2023.
  The cited recent cycle means use 1976-1986 and 2008-2019, with both endpoint years included: 1361.11236 and
  1360.93515 W/m². Solar cycles are approximately eleven years, so a complete cycle need not contain eleven annual samples.
- [CMIP7 v2.2.1 volcanic aerosol record via NASA GISS](https://data.giss.nasa.gov/modelforce/strataer/data/tau_reff_CMIP7-2-2-1.nc):
  Aubry et al., University of Exeter. tau scaled by 0.0001, cosine-latitude-weighted global mean, then annual mean.
- [Global Carbon Budget via Our World in Data](https://github.com/owid/co2-data): World co2 divided by 1,000 gives
  billion tonnes of CO2 per year, including cement. co2_including_luc gives the cumulative total with cleared land.
  OWID data is CC BY 4.0 with original producers credited.
- [IPCC AR6 WG1 Summary for Policymakers, A.1.3](https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_SPM_Stand_Alone.pdf):
  human-caused 1.07 °C is to 2010-2019; observed 1.09 °C is to 2011-2020. The tool corrects the spec's shared-endpoint wording.
- [IPCC AR6 WG1 chapter 3](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-3/), section 3.3.1:
  mixed early-century drivers, pollution aerosols and ocean variability in the mid-century pause.
- [NASA on the sun's role](https://science.nasa.gov/climate-change/faq/is-the-sun-causing-global-warming/):
  an approximately 11-year cycle, with no net rise since the 1950s.
- [NASA aerosol transmission example](https://mynasadata.larc.nasa.gov/sites/default/files/2020-10/Seasonal%20Patterns%20of%20Aerosols.pdf):
  optical depth 0.10 transmits about 90.5 percent of a direct beam. Beer-Lambert calculation: exp(-0.10).
  The chart specifies a vertical sunbeam because the record is vertical optical depth; a slanted path is longer.
- [Robock 2000, Reviews of Geophysics 38:191](https://climate.envsci.rutgers.edu/pdf/ROG2000.pdf),
  for volcanic cooling and the 1982-1983 El Niño masking;
  Smithsonian Global Volcanism Program for eruption years; NOAA Climate.gov ENSO materials for ocean swings.

Numerical qualification: the actual CMIP7 snapshot's Agung annual maximum is 1963 (0.03649), followed by 1964
(0.02562). The spec's claim that 1964 is the fourth-largest annual peak is incorrect. Its four eruption events remain
Krakatau, Agung, El Chichón and Pinatubo, and all four requested temperature-dip calculations agree with the spec.
The graphs retain the real values, including the larger 1963 haze value.
