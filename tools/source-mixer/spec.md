# Source Mixer

## One idea
Answer "What caused the Dust Bowl?" at a mixing desk: a rain chart, a radio broadcast, a government message and a photograph each get a channel strip with a fader, you route the parts of each that you will use, and the meters show how much each source strengthens or complicates your claim, warning you when the whole answer leans on one channel.

## Not like
- Research Notebook (ela 9, this group): text sources, note cards and a cited paragraph checked sentence by sentence. Here the sources are four media, and the check is the balance of the whole answer.
- Portrait in Four Media (ela 10, this group): compares four tellings of one life for emphasis and accuracy. Here the sources are weighed for one argument about a cause.
- Source Portfolio (library 9-12, this group): chooses which sources belong on a balanced shelf. Here the four sources are given; the skill is integrating them and not over-relying on one.
- Chart Narrator (ELD 9-12, wave 4): language for describing a chart. Here the chart is one channel among four and its readings are evidence for a claim.
- behind-the-documentary (social 9-12, not specced): documentary claims checked against sources on the Great Depression. Here there is no documentary; the student builds the answer.
- data-desk tools (math and science): the chart uses the data-desk table and chart, but the lesson is how a reading fits beside a speech and a photograph.

## Who and how
- Grade 11 ELA, module Integrating Sources: "Integrating sources across media".
- Topic line: "integrating sources across media".
- Standards: RI.11-12.7, W.11-12.8.
- Driver: students on their own laptops or in pairs. 25 to 40 minutes.
- tool.json: driver "students", minutes "25-40", modes [] (pure explore), grades_label "Grade 11". Kit starter with `kit:theme-912` (dark), accent and focus overrides.

## Screens and modes
Kit frame. Header: "Source Mixer", small line "What caused the Dust Bowl?"; Motion, Sound, Read. No modes.

**The desk** (stage). Across the top, the **claim selector**: three buttons, **Drought alone**, **Drought plus farming that didn't suit the Plains**, **Farming alone**. Below it, four **channel strips** side by side, each labeled with its medium icon and short name: **Chart** (rain data), **Broadcast** (radio transcript), **Message** (government text), **Photo**. Each strip has, top to bottom: a **Solo** button (opens the source in the monitor), its list of **takes** (the parts routed in, each a small lit tile with a +, - or E badge), a vertical **fader** 0 to 10 (default 5), and a **contribution LED** row: green segments for support, coral for complications, grey for effects-only, sized by fader times takes.

**The monitor** (under the strips, or a drawer at small sizes) shows the soloed source:
- Chart: a data-desk line chart of yearly rainfall (inches) with a filter bar: **Division** (Oklahoma Panhandle, Southwest Kansas, Texas High Plains), **From** and **To** years (1895 to 1960), **Average line** toggle (1895-1960 average for that division), and **Table** to see the DataTable. A **Take this reading** button turns the current view into a take (Interactions).
- Broadcast: the transcript paragraphs with a radio header ("Fireside chat, September 6, 1936"); tap a highlighted passage and **Route it**.
- Message: the document with a letterhead line ("Message to Congress, February 10, 1937"); same routing.
- Photo: the image large, with the Met caption and a note on dates; **Route it** routes the single take.

**The master section** (panel): the **claim meter** for the chosen claim (Support and Complications bars, with counts), a **Media used** row of four lamps, the **balance readout** (each channel's share of the faders as a percent, with the warning when one passes 50), and **Mixdown**.

**Mixdown** (opens over the stage): an outline of the answer. Line 1: the claim. Then one line per take, in an order the student can change (Up and Down), each with its MLA in-text citation. A **Complications** list of takes that push against the claim, each with a box "How does your answer handle this?" (private, saved in the page). **Works Cited** (MLA 9) for the sources used. **Copy outline** and **Back to the desk**.

Panel also holds `#hint`, a **Context card** button (Content; appears once the first 1950s reading is taken) and **Clear desk** (asks Yes / No).

## Content
Chart data: NOAA National Centers for Environmental Information, Climate at a Glance, divisional annual precipitation (January to December, inches), 1895 to 1960, 66 years per division: Oklahoma Climate Division 1 (Panhandle, code 3401), Kansas Climate Division 7 (Southwest, 1407), Texas Climate Division 1 (High Plains, 4101). Pulled 2026-10-27 from `https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/divisional/time-series/<code>/pcp/12/12/1895-1960/data.csv`; the build re-pulls these three files into `tools/source-mixer/data/` and the Done when numbers are rechecked against them. NOAA revises older values now and then; a change under 0.5 percentage points needs no spec change.

Readings this tool will compute (percent difference of a period's average from the 1895-1960 average of that division, rounded to whole percent in the tool):

| Division | 1895-1960 avg | 1895-1929 | 1930-39 | 1933-37 | 1952-56 | Driest year |
|---|---|---|---|---|---|---|
| Oklahoma Panhandle | 19.48 in | +3% | -21% | -32% | -30% | 1956 (11.03) |
| Southwest Kansas | 18.68 in | +2% | -21% | -28% | -32% | 1956 (8.24) |
| Texas High Plains | 18.64 in | +4% | -12% | -19% | -34% | 1956 (9.57) |

Chart takes (made by Take this reading; tags for Drought alone / Drought plus farming / Farming alone):
- A range inside 1930-1940 below average: "Drought reading" (+ / + / -).
- A range inside 1950-1960 below average: "Second drought reading" (- / + / 0) with the Context card: it shows the 1950s were as dry, while the Context card says the dust did not return at the same scale.
- A range inside 1895-1929: "Settlement years reading" (0 / 0 / 0), which also marks Message take M4 "checked: x% above average" with the computed number.
- Any other range: "Reading" (0 / 0 / 0), neutral.

Broadcast: Franklin D. Roosevelt, fireside chat, September 6, 1936 (radio address; public domain US government work), text from The American Presidency Project. Takes, quoted exactly:
- R1 "I saw drought devastation in nine States." (+ / + / -)
- R2 "I shall never forget the fields of wheat so blasted by heat that they cannot be harvested. I shall never forget field after field of corn stunted, earless and stripped of leaves, for what the sun left the grasshoppers took. I saw brown pastures which would not keep a cow on fifty acres." (E: effects)
- R3 "If, for example, in some local area the water table continues to drop and the topsoil to blow away, the land values will disappear with the water and the soil." (E)
- R4 "If over-grazing has injured range lands they are willing to reduce the grazing. If certain wheat lands should be returned to pasture they are willing to cooperate." (- / + / +)
- R5 "They stand ready to fit, and not to fight, the ways of Nature." (- / + / 0)
Context line on the strip: "A president speaking to the nation on radio after touring the drought states, two months before an election."

Message: Franklin D. Roosevelt, "Message to Congress on a Program for the Great Plains Area," February 10, 1937, sending the Great Plains Committee's report "The Future of the Great Plains." Takes, quoted exactly:
- M1 "The report indicates clearly that the problem of the Great Plains is not merely one of relief of a courageous and energetic people who have been stricken by several years of drought during a period of economic depression." (- / + / 0)
- M2 "Depression and drought have only accentuated a situation which has been long developing." (- / + / 0)
- M3 "The problem is one of arresting the decline of an agricultural economy not adapted to the climatic conditions because of lack of information and understanding at the time of settlement, and of readjusting that economy in the light of later experience and of scientific information now available." (- / + / +)
- M4 "The settlers of the Plains brought with them agricultural practices developed in the more humid regions from which they came. By historic circumstance the period of settlement was generally one of rainfall above the average, and, although water was known to be scarce, these practices then appeared to be suitable." (- / + / +)
- M5 "The long-run experience, however, has disclosed that the rainfall of the area hovers around, and, for considerable periods, falls below the critical point at which it is possible to grow crops by the agricultural methods common to humid regions." (0 / + / -)
Context line: "A message asking Congress to fund a long-term plan, written from a committee of experts' report."

Photo: Dorothea Lange, "Abandoned Farm in the Dustbowl, Coldwater District, near Dalhart, Texas," June 1938, printed ca. 1972, gelatin silver print, The Met 260387. One take, P1 (E: effects). Note on the strip: "Taken in June 1938; this print was made about 1972. Dalhart is in the Texas High Plains division on the chart." Alt text is written at build from the fetched image.

Context card (a summary, not a source to route): "Historian R. Douglas Hurt writes that the drought of the 1950s did not bring back the dust storms of the 1930s on the same scale, mainly because of soil conservation." Summarized from R. Douglas Hurt, "Dust Bowl," Encyclopedia of the Great Plains (University of Nebraska, 2011). Also: "Black Sunday, the worst single dust storm, was April 14, 1935. Congress created the Soil Conservation Service two weeks later, on April 27, 1935."

Meter rule: for the chosen claim, Support = sum over routed takes of fader x 1 for each +; Complications = the same for each -; E takes add to neither and light an **Effects** lamp ("shows what happened, not why"). Media used counts strips with at least one take. Balance: each strip's share = its fader / sum of faders of strips with takes. Readouts (text, never color alone):
- "Leaning on one channel" when any share is over 50 percent (W.11-12.8 overreliance).
- "Muted source" when a strip has takes but its fader is 0 ("You quote it but don't lean on it").
- "Unanswered complication" for each - take in the claim's Complications with an empty answer box.
- "Strong mix": Support greater than Complications, 3 or more media, no share over 50 percent, every complication answered.

Works Cited, MLA 9 (only sources with takes; the two Roosevelt entries by the same author use three hyphens for the second):
- Lange, Dorothea. Abandoned Farm in the Dustbowl, Coldwater District, near Dalhart, Texas. June 1938, printed ca. 1972, The Metropolitan Museum of Art, New York, www.metmuseum.org/art/collection/search/260387.
- National Centers for Environmental Information. "Climate at a Glance: Divisional Time Series." National Oceanic and Atmospheric Administration, www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/divisional/time-series. Accessed (build date).
- Roosevelt, Franklin D. "Fireside Chat." 6 Sept. 1936. The American Presidency Project, edited by Gerhard Peters and John T. Woolley, www.presidency.ucsb.edu/documents/fireside-chat-18.
- ---. "Message to Congress on a Program for the Great Plains Area." 10 Feb. 1937. The American Presidency Project, edited by Gerhard Peters and John T. Woolley, www.presidency.ucsb.edu/documents/message-congress-program-for-the-great-plains-area.
In-text: (National Centers for Environmental Information), (Roosevelt, "Fireside Chat"), (Roosevelt, "Message"), (Lange). A side note: "Two works by the same author: MLA adds a short title in the citation and uses three hyphens in the list." Source: MLA Handbook, 9th ed.

## Interactions in detail
- Routing: a take can be routed once; tap its tile on the strip to unroute. Each strip holds up to 5 takes (the chart up to 4 readings; a fifth asks to replace the oldest).
- Take this reading: computes the view's average and percent against the 1895-1960 average for the division and labels the tile ("OK Panhandle 1933-37: 13.26 in, -32%"). A range shorter than 3 years is refused: "Pick at least 3 years; one dry year isn't a drought."
- Faders: drag, arrow keys (1 step), Page Up and Page Down (5 steps); each shows its number. Meters and the balance readout update at once; with Motion on, meter bars ease over 200 ms; with Motion off they jump.
- Changing the claim keeps every take and fader; only the + and - badges and meters change, so the student can see one mix argue three ways.
- Mixdown: the order of lines is the student's; the claim line can be edited (kept local). Copy outline gives plain text with citations and the Works Cited.
- Store: claim, takes, faders, order and complication answers save to localStorage `sm-desk` (try/catch); Clear desk (after Yes) empties it.
- Keyboard: claim selector, then each strip (Solo, takes, fader), then the panel. Faders are `input type=range` with `aria-valuetext` ("Chart, 7 of 10"). The chart has its DataTable as the text equivalent.
- Sizes: at 1366x768 and 1280x720 the four strips and the monitor share the stage, master in the panel. At 680x425 strips shrink to two columns of two with short faders, and the monitor becomes a drawer. At 760 and 375 wide strips stack as rows with horizontal faders, the monitor opens full width, and the master section follows the strips.

## Look
- `kit:theme-912` dark, a studio console. Accent `--brand #45d4e8` (console cyan: claim selector, fader caps, Take this reading), `--btn #45d4e8` with `--brand-ink #1c1203` text; `--focus` overridden to `#ffffff` so focus never matches the cyan. Meters: support `#6fdca6`, complications `#ffb8a8`, effects `#a6b3c4`, each with its +, - or E badge. Chart: rain line `#5aa9ff` on `--gr-bg`, average line `#ffcf5c` dashed, the 1933-37 and 1952-56 bands shaded when a reading covers them.
- Strip labels in small caps, faders as long slots with cap knobs drawn in CSS, LED segments as rounded rectangles.
- Neighbors: chart-narrator (wave 4, not yet specced), satire-decoder oxblood, usage-panel ink red, boolean-builder orchid. Group siblings: Research Notebook fountain-pen blue (light), Portrait in Four Media coral (dark), Question Sharpener violet (light), Source Portfolio green (light), Enduring Questions lantern gold (dark). Cyan on dark is new among 9-12 ELA tools.
- Contrast (WCAG 2.1): brand on paper 10.59:1, on panel 9.76:1, on sec-bg 9.24:1; brand-ink on brand 10.41:1; focus white on panel 17.31:1; support on sec-bg 9.73:1; complications on sec-bg 9.90:1; rain line on gr-bg 7.46:1; average line on gr-bg 12.50:1. All pass AA.

## Art
Real public-domain photograph from The Met (Open Access, CC0), fetched with `python scripts/pd_art.py source-mixer met:260387`: Dorothea Lange, Abandoned Farm in the Dustbowl, Coldwater District, near Dalhart, Texas, June 1938, printed ca. 1972, gelatin silver print, Gift of Phyllis D. Massar, 1972 (checked 2026-10-27: isPublicDomain true with a primary image). Credit from `art/public-domain.json`. Everything else (console, strips, faders, radio and letterhead headers, preview.svg showing four strips and a meter) is drawn in code.

## Voice
Bank voice `news-reader` ("Say clearly and steadily, like a trusted radio news reader"): fits a desk built around a 1936 radio broadcast. `Curio.voice`, one scope, `welcomeAfter: true`. The tool never reads the sources aloud (Read reads the hint).
- w-desk (how, welcome): "Pick a claim. Then solo a source, route the parts you'll use, and set each fader."
- reading (how, first chart solo): "Set the years and the division, then press Take this reading."
- lean (event, each time one channel passes half the mix; stale if the faders change before it plays): "Most of this answer rests on one source."
- muted (how, first muted source): "That source is routed, but its fader is at zero."
- context (how, first 1950s reading): "The fifties were as dry. Open the context card to see what was different."
- comp (how, first complication routed): "That part pushes against your claim. Say how your answer handles it."
- strong (event, each time the mix becomes Strong): "Strong mix. Three media, and no single source carries it."

## Family engine
research (`kit/research.js`), described in full in Question Sharpener's spec. This tool uses: Source (four sources with medium, context and segments; the chart's readings are made at run time as segments), Weight (fader shares and the over-50-percent flag), Conflicts and corroboration (the + / - tags per claim), Cite (MLA 9, including same-author entries, a dataset, a radio transcript, a government message and a museum photograph) and Store (`sm-desk`). The chart uses the data-desk engine (`kit/data-desk.js`, docs/families/data-desk.md): DataTable and the line Chart with an average line.

## Sources
- Rainfall: NOAA National Centers for Environmental Information, Climate at a Glance: Divisional Time Series, precipitation, 12-month ending December, 1895-1960, divisions 3401, 1407 and 4101, https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/divisional/time-series (pulled 2026-10-27; averages and percents in Content computed from those files).
- Fireside chat, September 6, 1936: Gerhard Peters and John T. Woolley, The American Presidency Project, https://www.presidency.ucsb.edu/documents/fireside-chat-18
- Message to Congress, February 10, 1937: The American Presidency Project, https://www.presidency.ucsb.edu/documents/message-congress-program-for-the-great-plains-area
- Photograph: The Met, object 260387, https://www.metmuseum.org/art/collection/search/260387
- 1950s drought without 1930s-scale dust, mainly because of conservation: R. Douglas Hurt, "Dust Bowl," Encyclopedia of the Great Plains, University of Nebraska-Lincoln, http://plainshumanities.unl.edu/encyclopedia/doc/egp.pe.022.html (summary only).
- Black Sunday, April 14, 1935; Soil Conservation Service created April 27, 1935: Kansas Historical Society, Kansapedia, "Dust Bowl," https://www.kshs.org/kansapedia/dust-bowl/12040 ; USDA Natural Resources Conservation Service history.
- Citation forms: MLA Handbook, 9th ed. (2021).
- Standards: CCSS ELA RI.11-12.7, https://www.thecorestandards.org/ELA-Literacy/RI/11-12/ ; W.11-12.8, https://www.thecorestandards.org/ELA-Literacy/W/11-12/

## Done when
1. The three NOAA files load (66 years each) and Take this reading gives: Oklahoma Panhandle 1933-37 "13.26 in, -32%"; Southwest Kansas 1952-56 "12.78 in, -32%"; Texas High Plains 1895-1929 "19.46 in, +4%"; a 2-year range is refused.
2. The first 1950s reading shows the Context card button; a 1895-1929 reading marks M4 "checked" with its percent.
3. Every broadcast and message take matches The American Presidency Project text word for word.
4. With claim Drought plus farming, takes R1 and M3 at faders 5 and 5: Support 10, Complications 0, Media 2 of 4, no Strong mix; adding a 1933-37 reading at fader 5 gives Support 15, Media 3 and Strong mix; raising the Message fader to 10 (10 of 20, exactly half) does not warn, 11 of 21 warns "Leaning on one channel". Adding P1 lights Effects and changes neither bar.
5. Switching to Drought alone with the same takes: M3 counts as a complication and shows in Mixdown's Complications with an answer box.
6. Mixdown lists takes in the student's order with in-text citations, and Works Cited matches Content, with "---." for the second Roosevelt entry, alphabetized.
7. Reload keeps everything; Clear desk (after Yes) empties it; the photo is bundled; no network requests at run time; console clean.
8. At every size in STANDARDS.md the claim selector, the four strips' faders and the meter are visible without scrolling the page; 375 wide works in `drive.py --host`.
9. Voice: welcome once, how lines once, "Most of this answer rests on one source" every time a channel passes half; only "Curio Class" appears.

## Open questions
- [source-mixer] The concept names a "video transcript"; this uses the transcript of a 1936 radio broadcast (public domain, and the period's own medium). OK, or find a public-domain film (for example The Plow That Broke the Plains, 1936, a US government film) and use its narration instead?
- [source-mixer] The tool tags each take as support or complication for each claim. Should a teacher be able to see or change those tags, or keep them fixed?
