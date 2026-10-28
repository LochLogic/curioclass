# Chart Narrator

## One idea
Your words are the only thing the second pen can see: describe a real science chart in sentences ("From 1999 to 2006, methane remained stable"), and beside the real chart a pen redraws it from your words alone, so a vague verb leaves a dashed question mark, a wrong one sends the line the wrong way, and "increased sharply" where the data barely moved draws a cliff that isn't there; then flip roles, hear a description, and draw the chart it describes.

## Not like
- climate-dashboard (science 9-12, specced): investigates global temperature, CO2 and sea ice with trend windows. Here different datasets (methane, the ozone hole, Lake Mead, daylight), and the work is the language of describing a trend, not measuring it.
- misleading-charts (cs 6-8, specced): finds the trick in a chart's design. Here every chart is honest; the student is the one who can mislead, with words.
- i-spy-science (eld K-2, built): names and describes things in a picture. Here the thing described is change over time, with verbs, adverbs and numbers.
- cer-builder (eld 6-8, not built): claim, evidence and reasoning about an experiment. Here describe first, then explain with causes and hedges; no claim to argue.
- definition-duel, historian-s-toolkit, inbox-simulator, argument-frames-pro (eld 9-12, this group): math, history, email and debate language. This is the group's science and data tool.

## Who and how
- ELD grades 9 to 12. Module: Explaining Models and Data (Language for Science).
- Driver: a student alone; in pairs, one describes and the other draws in Listen. 20 to 35 minutes.
- Standards: WIDA.ELD-4 (Language for Science) through four real science graphs and one model; WIDA.Explain taught in full: describe a trend over time with precise verbs, adverbs, time frames and numbers; compare rates ("more quickly than"); then explain the pattern with causes, using hedges (may, scientists think) when science is still unsure, and say whether a graph shows measured data or a model.
- Help setting: **Lots of help**, **Some help**, **Little help** (WIDA levels 1-2, 3-4, 5-6 in teacher notes). Default Some help.
- Topic line: "describing trends in science data".
- tool.json: driver "students", minutes "20-35", modes ["Narrate", "Listen"], grades_label "Grades 9-12". Kit starter plus `kit:data-desk` (DataTable and line Chart only).

## Screens and modes
Header: title "Chart Narrator"; mode buttons **Narrate** (opens first), **Listen**; Motion, Sound, Read. Chart picker under the header: **Methane**, **Ozone hole**, **Lake Mead**, **Daylight**. Each chart carries its title, axis labels with units, a "Measured" or "Model" tag, and its "data as of" line.

### Narrate (opens first)
- Two charts, stacked on short screens and side by side on wide ones: **The data** (real line and points) and **The pen** (same axes, empty).
- Step tabs: **Describe**, **Explain**.
- Describe: a sentence builder: "From [year] to [year], [thing] [verb] [how] (from [number] to [number])." Year pickers list the chart's x values. Verb chips: increased, decreased, remained stable, fluctuated, rose and then fell, fell and then rose; each with an arrow icon. How chips: sharply, steadily, gradually, slightly, (none). Numbers are typed. An extra frame, **Compare**, builds "[thing] [verb] more quickly / more slowly from [year] to [year] than from [year] to [year]."
- **Add sentence**: it joins the description list and the pen draws that span: direction from the verb, steepness from the how word (sharply steep, gradually and slightly shallow, steadily a straight even line, none a medium slope), anchored to the typed numbers when given. "Fluctuated" draws a zigzag; "rose and then fell" draws a hump. A vague word typed at Little help ("changed", "moved", "was different") draws a dashed flat line with "?".
- Each sentence gets a verdict chip with a word and an icon: **Fits** ✓, **Partly** ◐ (the verb fits, the how word or a number does not), **Doesn't fit** ✗. Tapping the chip shows why in one line ("From 1999 to 2006 the data moved less than 2 percent of its range. Try remained stable.").
- **Read my description** reads the list aloud. **How the pen judges** opens the rules (below) in plain words.
- Explain: cause cards for this chart (see Content), each tagged **Known** or **Still studied**. Frame: "[Phase] [verb] [because / probably because / scientists think that] [cause]." The student picks a phase from their own sentences, a cause card and a link phrase. A last question: "Is this chart measured data or a model?" with a one-line reason frame ("It is a ___ because ___.").

### Listen
- Blank axes for a chart the student has not picked yet this session if possible (they can choose any). The tool reads a description (text shown sentence by sentence, each with **Hear it**).
- The student sets a point at each marked year by dragging a handle up or down (or arrow keys); lines join the points.
- **Show the data** overlays the real line and marks each interval between marked years ✓ or ✗ for direction (up, down, flat), and points to the words that told it ("'remained stable' told you this part was flat"). A count: "5 of 6 directions match." **Try another**.

## Content
Datasets (copied in as JSON with the date pulled):

Methane (Measured). Global mean methane in the air, parts per billion (ppb), yearly mean, 1984 to 2025: 1984 1644.84, 1985 1657.29, 1986 1670.09, 1987 1682.71, 1988 1693.19, 1989 1704.53, 1990 1714.46, 1991 1724.79, 1992 1735.47, 1993 1736.48, 1994 1742.06, 1995 1748.88, 1996 1751.31, 1997 1754.51, 1998 1765.57, 1999 1772.31, 2000 1773.22, 2001 1771.29, 2002 1772.68, 2003 1777.33, 2004 1777.13, 2005 1774.25, 2006 1774.94, 2007 1781.33, 2008 1787.01, 2009 1793.54, 2010 1798.89, 2011 1803.04, 2012 1808.07, 2013 1813.43, 2014 1822.59, 2015 1834.19, 2016 1843.18, 2017 1849.62, 2018 1857.34, 2019 1866.62, 2020 1878.78, 2021 1894.87, 2022 1911.01, 2023 1921.46, 2024 1929.47, 2025 1936.03. Data as of: NOAA file of 9 October 2026.

Ozone hole (Measured). Average ozone hole area over Antarctica, 7 September to 13 October, million square kilometers: 1979 0.1, 1980 1.4, 1981 0.6, 1982 4.8, 1983 7.9, 1984 10.1, 1985 14.2, 1986 11.3, 1987 19.3, 1988 10.0, 1989 18.7, 1990 19.2, 1991 18.8, 1992 22.3, 1993 24.2, 1994 23.6, 1995 no data (the chart shows a gap and says so), 1996 22.8, 1997 22.1, 1998 25.9, 1999 23.3, 2000 24.8, 2001 25.0, 2002 12.0, 2003 25.8, 2004 19.5, 2005 24.4, 2006 26.6, 2007 22.0, 2008 25.2, 2009 22.0, 2010 19.4, 2011 24.7, 2012 17.8, 2013 21.0, 2014 20.9, 2015 25.6, 2016 20.7, 2017 17.4, 2018 22.9, 2019 9.3, 2020 23.5, 2021 23.3, 2022 23.2, 2023 23.1, 2024 19.6, 2025 18.7. Data as of: NASA Ozone Watch, pulled 27 October 2026.

Lake Mead (Measured). Water level at Hoover Dam at the end of December, feet above sea level: 1999 1213.94, 2000 1196.12, 2001 1177.37, 2002 1152.13, 2003 1139.12, 2004 1130.01, 2005 1137.52, 2006 1128.12, 2007 1114.81, 2008 1110.97, 2009 1096.30, 2010 1086.30, 2011 1132.83, 2012 1120.36, 2013 1106.73, 2014 1087.79, 2015 1080.91, 2016 1080.82, 2017 1082.52, 2018 1081.46, 2019 1090.49, 2020 1083.72, 2021 1066.39, 2022 1044.82, 2023 1068.18, 2024 1063.29, 2025 1062.24. Data as of: Bureau of Reclamation table, pulled 27 October 2026.

Daylight (Model). Hours of daylight on the 21st of each month at 40 degrees north, computed with NOAA's solar position equations (sunrise and sunset at the Sun 0.833 degrees below the horizon): Jan 9.78, Feb 10.92, Mar 12.14, Apr 13.47, May 14.54, Jun 15.02, Jul 14.62, Aug 13.57, Sep 12.26, Oct 10.97, Nov 9.82, Dec 9.33. Label: "A model: computed from equations, not measured."

Listen marked x values: Methane 1984, 1992, 1999, 2006, 2013, 2019, 2025. Ozone 1979, 1983, 1987, 1992, 1998, 2002, 2006, 2019, 2025. Lake Mead 1999, 2005, 2010, 2011, 2016, 2022, 2025. Daylight Jan, Mar, Jun, Sep, Dec.

Listen descriptions (also the model answers shown after Explain):
- Methane: "From 1984 to 1999, methane increased steadily, from about 1,645 to about 1,772 parts per billion. From 1999 to 2006, it remained stable at about 1,775. After 2006 it increased again, and after 2019 it increased more quickly. In 2025 it reached about 1,936."
- Ozone hole: "From 1979 to 1987, the ozone hole grew sharply, from almost nothing to about 19 million square kilometers. From 1987 to 1998, it kept growing, with ups and downs, to about 26. After 1998 it fluctuated between about 17 and 27, except in 2002 and 2019, when it dropped to about 12 and about 9."
- Lake Mead: "From 1999 to 2010, Lake Mead fell steadily, from about 1,214 to about 1,086 feet. In 2011 it rose sharply, to about 1,133. Then it fell again until 2022, when it reached a low of about 1,045. After that it rose a little and stayed about the same."
- Daylight: "On January 21, a place at 40 degrees north has about 10 hours of daylight. Daylight increases steadily until June, when it peaks at about 15 hours. Then it decreases steadily to about 9 hours in December."

Cause cards (Explain):
- Methane: "Methane comes from wetlands, farm animals such as cattle, rice fields, landfills, and oil, gas and coal." (Known; any rising phase). "Scientists are still working out why methane stopped rising from about 1999 to 2006." (Still studied; 1999 to 2006). "Scientists are still studying why methane rose faster after 2019." (Still studied; 2019 to 2025).
- Ozone hole: "Chemicals called CFCs, once used in spray cans and refrigerators, break down ozone high in the sky." (Known; 1979 to 1987 and 1987 to 1998). "In 1987, countries agreed to the Montreal Protocol to phase out CFCs." (Known; after 1998, why it stopped growing). "CFCs stay in the air for many years, so the hole did not shrink right away." (Known; after 1998). "In 2002 and 2019, unusually warm air high over Antarctica kept the hole small." (Known; 2002 and 2019).
- Lake Mead: "Since about 2000, the Colorado River basin has had a long drought, so less water flows into the lake." (Known; falling phases). "Cities and farms take water from the lake for drinking and crops." (Known; falling phases). "In 2011, a very large snowpack in the Rocky Mountains melted into the river." (Known; 2010 to 2011). "The winter of 2022 to 2023 brought heavy snow to the Rockies." (Known; 2022 to 2023).
- Daylight: "Earth's axis is tilted about 23.4 degrees." (Known; whole year). "In June, the Northern Hemisphere leans toward the Sun, so days are longer." (Known; the rise to June). "In December, it leans away from the Sun, so days are shorter." (Known; the fall to December).

Word bank (Little help accepts these and maps them): increased = rose, went up, grew, climbed; decreased = fell, dropped, declined, went down, shrank; remained stable = stayed about the same, leveled off, held steady; fluctuated = went up and down, varied; rose and then fell = peaked, reached a high; fell and then rose = reached a low; sharply = quickly, rapidly, steeply; gradually = slowly; steadily; slightly = a little. Hedges: may, might, probably, scientists think, one reason may be.

## Interactions in detail
How the pen judges a sentence about years a to b (R is the whole chart's range, max minus min; the screen states these as "the pen's rules"):
- net = (value at b minus value at a) / R; within = (highest minus lowest between a and b) / R; rate = |net| / (b minus a, in years or months); a swing is a step of at least 0.08 R; flips = times two swings in a row go opposite ways.
- increased fits when net ≥ 0.08; decreased when net ≤ -0.08; remained stable when |net| < 0.08 and within < 0.15; fluctuated when flips ≥ 2; rose and then fell when the highest value between a and b is at least 0.15 R above both ends; fell and then rose, the same for the lowest.
- When flips ≥ 3, increased or decreased alone is **Partly**: "It went up and down a lot. Say it fluctuated, or start with Overall." A sentence that starts with "Overall" fits.
- sharply fits when rate ≥ 0.08; steadily when there are at least 3 steps and the sum of step sizes ≤ 1.3 × |net|; gradually when rate ≤ 0.05; slightly when |net| ≤ 0.20. More than one can fit.
- Numbers fit within 3 percent of R of the real value at that year ("about" is fine). "Reached a high (low) of X" checks the highest (lowest) value in the span.
- Compare: "more quickly" fits when the first span's rate is at least 1.3 times the second's; "more slowly" the reverse.
- Checked cases (recompute at build): Methane 1984-1999 increased steadily or gradually: Fits; 1999-2006 remained stable: Fits; 2019-2025 increased sharply: Partly (rate 0.040); increased more quickly 2019-2025 than 2006-2019: Fits (0.040 against 0.024). Ozone 1979-1987 increased sharply: Fits; increased steadily: Partly (the 1986 dip); 1998-2025 fluctuated: Fits; decreased gradually: Partly (flips 13). Lake Mead 1999-2010 decreased steadily: Fits; 2010-2011 increased sharply: Fits; 2015-2018 remained stable: Fits; 2009-2013 rose and then fell: Fits. Daylight Jan-Dec rose and then fell: Fits; Jan-Jun increased sharply or steadily: Fits; May-Jul remained stable: Fits (within 0.08).
- The pen: each sentence's span is redrawn when sentences overlap (the later sentence wins that span, and the earlier chip says "Replaced from ___ to ___"). Spans no sentence covers stay empty.
- Explain checks: the cause card's phase must overlap the chosen phase, else "This card is about 2011, not 2022." A Still studied card needs a hedge (may, might, probably, scientists think, one reason may be); without one: "Scientists are not sure yet. Add may or scientists think." A Known card with a hedge is accepted with a note that a hedge is not needed. Model or measured: Daylight is a model, the other three measured; the reason frame needs computed/equations or measured/instrument/observed.
- Listen: directions per interval use the same rules with net thresholds ±0.08 for up and down. The handles snap to whole numbers on the y axis.
- Help: Lots of help shades the chart's main phases (methane 1984-1999, 1999-2006, 2006-2025; ozone 1979-1987, 1987-1998, 1998-2025; Lake Mead 1999-2010, 2010-2011, 2011-2022, 2022-2025; daylight Jan-Jun, Jun-Dec), shows icons on chips and puts numbers as chips (the values at the chosen years). Some help: no shading, numbers typed. Little help: typed verb and how word, matched to the word bank; an unknown word gets "The pen doesn't know '___'. Try a word from Words."
- Mode change calls `V.hush()`. Storage `chart-narrator:v1` (try/catch): help setting and each chart's description list. **Clear** asks first.
- Sizes: at 1366x768 both charts, the builder and Add sentence fit; at 1000x625 the charts stack with a **Data / Pen / Both** toggle; at 375 one chart at a time with the toggle and the builder under it; drag handles at least 44 px. Chart text at least 11 px at 680x425. No horizontal page scroll.

## Look
- Own dark `:root`, a lab screen: `--paper #0f1720`, `--panel #16212d`, `--ink #e8f0f7`, `--muted #a9b8c6`, `--line #2a3a4a`, accent `--brand #4dd2ff` (instrument cyan: the data line, active mode, Add sentence), `--btn #4dd2ff`, `--head-ink #0b1218`, `--focus #ffd166`. The pen line `#ffb3c7`, drawn dashed so it differs from the data line by pattern too.
- Neighbors: climate-dashboard and the data-desk tools; nearest catalog accent algebra-tile-studio #6cc4ff (dE 13.4); source-mixer #45d4e8 (dE 14.7).
- Contrast: ink on paper 15.67:1; muted on paper 8.90:1, on panel 8.03:1; brand on paper 10.29:1, on panel 9.29:1; button text on brand 10.75:1; pen on paper 10.76:1; focus on panel 11.29:1. All pass AA.

## Art
None: drawn in code with the data-desk Chart (axes, lines, handles, cards). No people.

## Voice
Bank voice `clear-teacher` (Iapetus), style "Say clearly and kindly, like a patient teacher reading a graph with a student." Not used by another ELD tool or this group. `Curio.voice`, `scope: () => state.mode`. The Listen descriptions are recorded so a student can hear them more than once.
- w-narrate (how): "Pick two years. Then choose a verb and a how word, and press Add sentence. The pen draws only what you say."
- fits (event; stale on the next sentence): "That fits the data."
- partly (event): "Partly. The direction is right. Check the how word or the number."
- nofit (event): "That doesn't fit. Look at where the line starts and ends."
- vague (event): "The pen can't draw that. Use a word like increased or remained stable."
- w-explain (how): "Now say why. Pick a phase, a cause card and a link phrase."
- hedge (event): "Scientists are not sure yet. Add may, or scientists think."
- w-listen (how): "Listen to the description. Then drag each point to where the words put it, and press Show the data."
- listen-1 to listen-4 (event, the four descriptions, each sentence a separate line).
- result (event): "Here's the data. Check which words told you each part."

## Family engine
None. The tool uses the data-desk engine's DataTable and line Chart (`docs/families/data-desk.md`) as a library, with four datasets no data-desk sibling uses; the pen line and Listen handles are its own.

## Sources
- Methane: NOAA Global Monitoring Laboratory, global monthly and annual means, https://gml.noaa.gov/webdata/ccgg/trends/ch4/ch4_annmean_gl.txt (file created 9 October 2026); sources of methane and its recent rise: https://gml.noaa.gov/ccgg/trends_ch4/ (confirm card wording at build).
- Ozone hole: NASA Ozone Watch, annual data (7 Sep to 13 Oct mean area), https://ozonewatch.gsfc.nasa.gov/statistics/annual_data.html, pulled 27 October 2026; CFCs and the Montreal Protocol: https://ozonewatch.gsfc.nasa.gov/facts/; 2019 small hole and stratospheric warming: NASA, "2019 Ozone Hole is the Smallest on Record Since Its Discovery," 21 October 2019, https://www.nasa.gov/earth/2019-ozone-hole-is-the-smallest-on-record-since-its-discovery/ (confirm the 2002 link at build).
- Lake Mead: Bureau of Reclamation, Lake Mead at Hoover Dam, end of month elevation, https://www.usbr.gov/lc/region/g4000/hourly/mead-elv.html, pulled 27 October 2026; drought and the 2011 and 2023 snowpacks: Reclamation, https://www.usbr.gov/lc/region/g4000/24mo.pdf and Colorado River basin drought pages (confirm each card at build; a news summary of the 2011 rise of more than 46 feet agrees with the table: 1086.30 to 1132.83).
- Daylight: NOAA Global Monitoring Laboratory solar calculator equations, https://gml.noaa.gov/grad/solcalc/solareqns.PDF, computed for 40° N; axis tilt: NASA Space Place, "What Causes the Seasons?", https://spaceplace.nasa.gov/seasons/.
- WIDA ELD Standards Framework, 2020 Edition (Explain, Language for Science): https://wida.wisc.edu/teach/standards/eld.

## Done when
- Every checked case in Interactions gets the verdict listed.
- The pen draws a flat dashed line with "?" for "changed" at Little help, and a zigzag for fluctuated.
- Two overlapping sentences: the later one wins the span and the earlier shows "Replaced".
- Explain rejects the 2011 snowpack card for the 2022 phase and asks for a hedge on a Still studied card; accepts "probably because".
- Daylight answers Model; the others Measured.
- Listen: drawing the methane description faithfully scores 6 of 6; a flat line scores no more than 2.
- The ozone chart shows a gap at 1995 with "No data".
- Data as of lines are on screen for all four charts.
- How lines are spoken once in five actions; verdict lines repeat each time.
- No horizontal scroll at any listed size; the toggle works at 375.

## Open questions
- None beyond the group's home-language question (see then-what-happened).
