# Baron or Builder

## One idea
Across a Gilded Age street runs a long line, "Robber baron" at one end and "Captain of industry" at the other, and the student places five real business leaders on it (Andrew Carnegie in steel, John D. Rockefeller in oil, Cornelius Vanderbilt in railroads, George Pullman in sleeping cars and his company town, Madam C. J. Walker in hair care) using evidence cards on wages, prices, market share, rebates, strikes, new products and giving; a market panel for each industry measures how many sellers there were and how prices moved, so "monopoly" is counted, not assumed; then people their businesses touched step forward one at a time (a steelworker at Homestead in 1892, a family renting in Pullman's town in 1894, a small Cleveland refiner in 1872, a farmer paying freight rates, a kerosene customer, a Walker sales agent), each a composite labeled as such and built from real records, and challenge the placement, so the student moves the card or answers with evidence; a city map shows the millions of immigrants and rural migrants these industries drew into Pittsburgh and Chicago; at the end the student's line sits beside newspapers of the time and historians' placements across a century, and the student writes what changed and what continued from 1870 to 1900 and today, so an eleventh grader learns change and continuity in an era, how much competition really existed in specific markets, and how industry reshaped where people lived.

## Not like
- factory-floor (9, spec): running a British mill. Here judging American owners.
- the-buyout (12, spec): a modern market model. Here five real Gilded Age markets.
- muckraker-studio (11, spec): writing an expose. Here weighing a reputation.
- stock-market-1929 (11, spec): a crash lived through. Here an era judged.

## Who and how
- Grade 11, Social Studies (U.S. History), module "Industrialization and the Gilded Age". Standards: D2.His.2.9-12 (analyze change and continuity in historical eras), D2.Eco.4.9-12 (evaluate the extent to which competition among sellers and among buyers exists in specific markets), D2.Geo.7.9-12 (analyze the reciprocal nature of how historical events and the spatial diffusion of ideas, technologies, and cultural practices have influenced migration patterns and the distribution of human population).
- Format: roleplay. Driver: one student alone; the student places first, then hears the witnesses (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Five leaders, about thirty evidence cards, five market panels, six witnesses, the city map, the comparison and the note. Extra: Hardest case (the class compares lines and argues the leader with the widest spread). tool.json `modes: ["The line", "Hardest case"]`, `minutes: "35-45"`, `grades_label: "Grade 11"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.4.9-12 | Open each industry's market panel and say how many sellers and buyers there were before placing the leader | the seller count and price line per industry | 2 |
| D2.Geo.7.9-12 | Trace each industry's pull on the city map and match migrants to the jobs that drew them | the city map with population and origin layers | 3 |
| D2.His.2.9-12 | Defend or move each placement against the witnesses, then write the change and continuity note | the witnesses; the comparison; the note | 4, 5 |

## Screens and modes
Header (kit): title "Baron or Builder"; `The line`, `Hardest case`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A Gilded Age street in gaslight. A rope runs along it with two signs, "Robber baron" and "Captain of industry". Five portrait cards wait at the curb. The welcome is queued (`welcomeAfter: true`): "Were they thieves or builders? You decide first, on evidence. Then the people who worked for them get their say. Tap Carnegie's card." First hint: "Tap Carnegie's card."

**Placing (focus: the leader and the evidence).** At 1366x768 the line runs across the top with the evidence tray and market panel below; at 680x425 the tray and panel are sheets. For each leader the student opens five or six evidence cards and the market panel, then drags the portrait onto the line.
- Carnegie: the price of steel rails fell from about $160 a ton in 1875 to about $17 in 1898; twelve-hour shifts, often seven days a week; the Homestead lockout of 1892, when a battle with Pinkerton guards left about ten people dead and the union was broken; the sale to J. P. Morgan in 1901 for about $480 million; "The Gospel of Wealth" (1889) and more than 2,500 libraries.
- Rockefeller: Standard Oil founded 1870; secret railroad rebates; in early 1872 it bought out most of its Cleveland rivals in a few weeks; by about 1880 it refined about 90 percent of the nation's oil; kerosene fell from about 26 cents a gallon in 1870 to about 8 cents by 1885; broken up by the Supreme Court in 1911.
- Vanderbilt: joined lines into the New York Central; rate wars and pooling; faster, cheaper freight; farmers' anger at rates led to the Interstate Commerce Act of 1887.
- Pullman: nearly every sleeping car in the country; the town of Pullman, Illinois (1880), with company-owned housing, stores and church; in 1894 wages were cut by about a quarter while rents stayed the same; the strike and national boycott; federal troops; about thirty people killed.
- Walker: born Sarah Breedlove in 1867 to formerly enslaved parents; built a hair-care company in a crowded market with many Black-owned rivals (including her former employer Annie Turnbo Malone); trained thousands of sales agents, mostly Black women, giving them income outside domestic work; gave to the NAACP and Black schools.

**Market panel (D2.Eco.4.9-12).** For each industry: a seller count over time (from many to few, or staying many) and a price line, plus who the buyers were and whether they could go elsewhere (a farmer with one railroad, a railroad with one sleeping-car maker). The student marks each market "many sellers", "a few", or "one big seller" before placing.

**Witnesses (focus: the challenge).** Six composites, each labeled "a composite built from real records" with the records named: a Homestead steelworker (1892), a Pullman family (1894), a small Cleveland refiner (1872), a Kansas farmer (1880s), a kerosene customer, a Walker agent (1910s). Each speaks a short challenge; the student either moves the portrait or answers with one evidence card.

**City map (D2.Geo.7.9-12).** Pittsburgh and Chicago grow: Chicago from about 300,000 people in 1870 to about 1.7 million in 1900; origin layers show Europe, the rural Midwest and, after 1900, the Black South. The student matches each migrant group to the jobs that drew it (mills, packing houses, rail yards, the Walker agent network in Black neighborhoods).

**The comparison and note (the aha).** The student's line beside a newspaper's line of the time and historians' lines across a century (Josephson's "The Robber Barons" in 1934, Nevins in the 1940s, Chernow and Nasaw recently). The note: "From 1870 to 1900, ___ changed. ___ stayed the same. Today ___." Narrator: "The same facts, weighed by different people at different times, move the cards."

**The end.** The line, the market marks, the map and the note. `Print` prints them.

**Hardest case (extra).** The class compares lines; the leader with the widest spread goes up for argument.

## Content
- Five leaders, about thirty evidence cards with figures and sources, five market panels, six labeled composite witnesses, the city map, period and historians' lines, the note.
- Leaders, events and figures are real and sourced; witnesses are composites labeled so, with the real records behind each named.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A portrait can't be placed until its market panel is marked; witnesses come after all five are placed.
- Keyboard: Tab to portraits, evidence, panels, witnesses and the map; arrow keys move a portrait along the line; Enter places.
- With Motion off portraits move without sliding.

## Look
- Accent `--brand` #6b4a1b gilded bronze (header, the line, portraits); gold #f4c542 (the card in hand, a placed marker); paper #f8f4ec; ink #21170a; muted #5d564c.
- Contrast (WCAG 2.1, computed): white on brand 8.01:1; brand on paper 7.31:1; ink on paper 16.06:1; muted on paper 6.60:1; ink on gold 10.84:1.
- Never color alone: the line carries words at both ends and a number scale; market marks carry words.
- Different from this batch (archive teal, decade violet, suburb green, press red).

## Art
- Public domain photographs and cartoons (Library of Congress, ids checked at build): portraits of Carnegie, Rockefeller, Vanderbilt, Pullman and Walker; the Homestead works; the town of Pullman; a Puck cartoon of Standard Oil as an octopus (1904). Each with credit.
- People (illustrated) for the six composite witnesses, labeled "illustration" (Gemini, `people: true`, 6; cutout yes).
- Local FLUX (`scripts/localart.py`): the gaslit street (1, 16:9).
About 13 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as the narrator and hints; `warm-teacher` as the witnesses' voice, introduced each time as "a composite" with the witness's role. `Curio.voice` with `scope: () => state.mode + ':' + state.leader + ':' + state.witness + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each evidence card.
- how `market`: "Mark how many sellers this market had."
- how `place`: "Drag the portrait onto the line."
- event, whole, each witness.
- how `answer`: "Move the card, or answer with evidence."
- how `map`: "Match each group to the jobs that drew it."
- how `note`: "Write what changed and what stayed the same."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the placement line, evidence tray, market panels, witnesses, the city map, the comparison.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Market marks | Mark every market "one big seller" | Each mark checks against the seller count; Walker's market had many. |
| Witness answers | Never move and never answer | The next witness waits for a move or an evidence card. |
| Note | Write only about the past | It needs a change, a continuity and a today line. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Evidence (whole), waits; `market`; `place`.
2. Witness (whole), waits; `answer`.
3. `map`.
4. `note`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.2.9-12, D2.Eco.4.9-12 and D2.Geo.7.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Steel rail prices fell from about $160 (1875) to about $17 (1898); the 1901 sale | Nasaw, "Andrew Carnegie" (Penguin, 2006) | PBS American Experience, "The Richest Man in the World" | yes |
| Homestead (July 6, 1892): the battle and deaths | Krause, "The Battle for Homestead" (Pittsburgh, 1992) | Pennsylvania Historical and Museum Commission marker | yes |
| Standard Oil's 1872 Cleveland buyouts, rebates, about 90 percent of refining by about 1880; the 1911 breakup | Chernow, "Titan" (Random House, 1998) | Standard Oil Co. of New Jersey v. United States, 221 U.S. 1 (1911) | yes |
| Kerosene prices fell sharply, 1870 to 1885 | Chernow (1998) | U.S. Energy Information Administration, history of petroleum | yes |
| Pullman: the company town, the 1894 wage cuts with rents unchanged, the strike and troops | U.S. Strike Commission, "Report on the Chicago Strike" (1895) | National Park Service, Pullman National Historical Park | yes |
| Walker: born 1867, her agents and rivals, her giving | Bundles, "On Her Own Ground" (Scribner, 2001) | National Museum of African American History and Culture | yes |
| Chicago's population, about 300,000 (1870) to about 1.7 million (1900) | U.S. Census Bureau, population of the 100 largest cities | Encyclopedia of Chicago (Newberry Library) | yes |
| Interstate Commerce Act (1887) | National Archives, "Interstate Commerce Act" | Office of the Historian, U.S. Senate | yes |
Backed twice: 9. Cut: 0.

Checks run (Python, scratchpad r20, 2026-11-09): rail prices fell by about 89 percent; Chicago grew about 5.7 times; Standard Oil lasted 41 years from founding to breakup; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 line, tray and panel; at 680x425 sheets.
2. Each market is marked by seller count before its leader is placed. (D2.Eco.4.9-12)
3. Migrant groups are matched to jobs on the city map. (D2.Geo.7.9-12)
4. Every witness gets a move or an evidence answer. (D2.His.2.9-12)
5. The note names a change, a continuity and a today line. (D2.His.2.9-12)
6. Witnesses are labeled composites with their records named.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
None.
