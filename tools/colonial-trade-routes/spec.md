# Colonial Trade Routes

## One idea
On a 1700s Atlantic map with ports lit, the child follows real cargoes along their routes (dried fish and lumber from New England, wheat and flour from the Middle Colonies, tobacco from Virginia and rice and indigo from South Carolina, sugar and molasses from the Caribbean, cloth and tools from Britain) and opens each cargo card to see the resources behind it (land, water, tools and ships, and the people who did the work: farmers, sailors, indentured servants and enslaved Africans), finds that the "triangle" was really a web of many routes, slides through the decades to watch ports, shipyards and plantations grow because of ties to faraway places and Southern colonies come to depend on slavery, and compares three working days (a ship's boy in Boston, an enslaved woman on a South Carolina rice plantation, a Philadelphia baker) with work today, so a fifth grader learns which resources made each region rich, and at whose cost.

## Not like
- ship-s-log (5, spec, this batch): one voyage in 1620. Here a hundred years of trade across the Atlantic.
- state-economy-map (4, spec): a state's economy today. Here colonial regions in the 1700s.
- silk-road-traders (6, concept): trade across Asia at grade 6. Here the Atlantic world at grade 5.
- barter-bay (4, spec): what money is. Here what resources and whose labor made goods.

## Who and how
- Grade 5, Social Studies (Economics, Geography and History), module "Colonial Economies". Standards: D2.Eco.3.3-5 (identify examples of the variety of resources, human capital, physical capital, and natural resources, that are used to produce goods and services), D2.Geo.11.3-5 (describe how the spatial patterns of economic activities in a place change over time because of interactions with nearby and distant places), D2.His.2.3-5 (compare life in specific historical time periods to life today).
- Change from the module codes: D2.Geo.9.3-5 (catastrophic events and migration) has no honest place here; it is taught in settle-the-valley, as the idea card proposes (see Open questions).
- Driver: one child alone, or the teacher on the projector (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Three parts: Cargoes, Decades, Three days. Extra: Teacher notes on the Middle Passage. tool.json `modes: ["Map", "Three days"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.3.3-5 | Open each cargo and sort its chips into Natural resources, Tools and ships (physical capital), and Workers and their skills (human capital), noting who was forced to work | the cargo card with three columns; forced labor marked plainly | 2 |
| D2.Geo.11.3-5 | Trace routes, then slide the decades (1700, 1730, 1760) and tap three changes to name the far-off tie that caused them | routes as a web; ports, shipyards and plantations growing; change rings | 3, 4 |
| D2.His.2.3-5 | Compare each of three working days with work and goods today | three day cards with a "today" column | 5 |

## Screens and modes
Header (kit): title "Colonial Trade Routes"; `Map`, `Three days`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** An Atlantic map (a public-domain 1700s map, see Art) with ports lit: Boston, Newport, New York, Philadelphia, Charleston, Kingston (Jamaica), Bridgetown (Barbados), London, Bristol, and the West African coast (Elmina, Bonny, Gorée). A ship sits at Boston. The welcome is queued (`welcomeAfter: true`): "In the 1700s, ships carried goods all around the Atlantic. A ship is loading in Boston. Tap it to see the cargo." First hint: "Tap the ship."

**Cargoes (focus: the map and the cargo card).** At 1366x768 the map fills the screen with the card at the right; at 680x425 the card opens as a sheet.
- Seven cargoes, each a ship at a port; tapping opens its card and draws its route(s):
  - New England: dried cod and lumber, to the Caribbean and Southern Europe. Natural: fish, forests. Tools and ships: boats, sawmills, salt. Workers: fishermen, sailors, sawyers.
  - Middle Colonies: wheat and flour, to the Caribbean. Natural: rich soil. Tools: plows, gristmills. Workers: farm families, indentured servants, millers, some enslaved people.
  - Virginia and Maryland: tobacco, to Britain. Natural: warm climate, soil. Tools: hoes, drying barns. Workers: enslaved Africans, and earlier many indentured servants.
  - South Carolina: rice and indigo, to Britain and Europe. Natural: tidal swamps, warm climate. Tools: dikes and gates to flood fields. Workers: enslaved Africans, many from West African rice-growing regions, whose knowledge built the rice fields.
  - The Caribbean: sugar and molasses, to Britain and New England (molasses made into rum). Natural: sugar cane climate. Tools: mills, boiling houses. Workers: enslaved Africans in very harsh conditions.
  - Britain: cloth, tools and guns, to the colonies and West Africa. Natural: wool, iron, coal. Tools: looms, forges. Workers: weavers, smiths.
  - The Middle Passage: ships carried captured Africans from West Africa to the Caribbean and the colonies. This card is not a cargo of goods: "These were people, taken from their homes by force. About 12.5 million Africans were forced onto ships across the whole slave trade, and about 1.8 million died on the way." The route is drawn as a dark line with no goods icon.
- Sorting: each card has six chips; the child drags them to the three columns. "Workers who were forced" is a fixed label on enslaved workers' chips, not a column choice.
- When all seven are open, the routes show as a web, not a triangle. Narrator: "People sometimes call this the triangle trade. Really, ships went many ways at once."

**Decades (focus: the map and a slider).** A slider at 1700, 1730 and 1760. As it moves, port dots grow (Boston and Philadelphia shipyards, Charleston's wharves), plantations spread on the Southern coast and the Caribbean, and a bar shows the share of enslaved people in each region's population rising sharply in South Carolina (a majority by the 1720s) while staying low in New England. Three gold rings mark changes; the child taps each and picks the faraway tie that caused it from three (for example, "Britain bought more rice" for Charleston's growth).

**Three days (focus: one day card at a time).** Each day card has five times (dawn, morning, midday, afternoon, night), and a "today" column the child fills from picture choices.
- Thomas, 12, a ship's boy in Boston: hauling ropes, scrubbing decks, learning knots, a bowl of salt fish.
- Phibba, a woman enslaved on a rice plantation near Charleston (Phibba is an Akan day name found often in South Carolina records), under the task system: a set task of ground to hoe or flood each day, then tending her family's garden after; her knowledge of rice growing from West Africa; her ways of keeping family, language and faith; resistance, including the 1739 Stono Rebellion nearby. The card says she is a composite drawn from records of real women, since most were not recorded by name (see Open questions).
- Johann, a baker in Philadelphia: up before dawn, flour from Middle Colonies mills, selling bread and ship's biscuit for voyages.
- The end card: "Which resources made each region rich? Who paid the cost?" The child picks one resource and one group of workers for each region from chips. `Print` prints the map, cargo cards and day cards.

**Teacher notes (extra).** A page on the Middle Passage with sources for deeper study, for teachers to use with care.

## Content
- Seven route cards (six cargoes, the Middle Passage) with six chips each; three decades; three changes; three day cards with five times; the end card.
- The three workers are composites based on records; their names are common names of their times and places.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The decade slider shows only after all seven route cards are opened. Three days opens after the decades.
- Keyboard: Tab through ports; Enter to open; arrow keys move the slider.
- With Motion off routes appear without drawing and ships don't sail.

## Look
- Accent `--brand` #1f4e5f harbor teal (header, routes, card frames); gold #f4c542 (the active ship, change rings); paper #eef4f6; ink #081a20; muted #4c585c.
- Contrast (WCAG 2.1, computed): white on brand 9.08:1; brand on paper 8.17:1; ink on paper 16.04:1; muted on paper 6.62:1; ink on gold 10.95:1.
- Never color alone: routes carry goods icons and labels; the Middle Passage line is dark with a label, never color alone.
- Different from this batch (timeline violet, ship's log wood, article red, interest green).

## Art
- Public domain (Library of Congress, credited): an 18th-century Atlantic or British America map as the base (for example Henry Popple's 1733 "A Map of the British Empire in America", checked at build).
- People art goes to Gemini with `people: true`: the three workers (2 poses each; cutout yes); the enslaved woman shown with dignity at work and with family, never in chains or being harmed.
- Local FLUX (`scripts/localart.py`): goods icons (12, 1:1); a Boston wharf, a rice field, a Philadelphia bakery (3, 16:9).
- Drawn in code: routes, dots, the slider, bars, cards.
About 22 images.

## Voice
Three bank voices, each unique in this batch: `smooth-narrator` as the narrator, who also tells the enslaved woman's day in the third person; `casual-peer` as Thomas; `friendly-dad` as Johann. `Curio.voice` with `scope: () => state.mode + ':' + state.card + ':' + state.decade`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each cargo card and the Middle Passage card.
- how `sort`: "Drag each chip to the kind of resource it is."
- event, whole, `web`.
- how `decades`: "Slide through the years and tap a gold ring."
- event, whole, each change's cause line.
- event, whole, each day card's times.
- how `today`: "Fill in what work and goods are like today."
- how `end`: "Pick a resource and the workers for each region."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: a map with ports and route drawing, cargo cards with a three-column sort, the decade slider with growth layers and bars, day cards.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Resource sort | Put all chips in one column | Each card has two chips per column; wrong drops say what kind it is. |
| Decades | Pick the first cause | Causes are shuffled; a wrong pick replays the before-and-after at that port. |
| End card | Pick any chips | Chips come from each region's own card; a wrong pick shows that region's card. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Each card: text (whole), waits; `sort`.
2. All seven: `web` (whole). `decades`; causes (whole).
3. Three days: each day (whole); `today`; `end`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.3, D2.Geo.11 and D2.His.2 (3-5) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Colonial regional exports: New England fish and lumber, Middle Colonies grain, Chesapeake tobacco, Carolina rice and indigo, Caribbean sugar and molasses | Colonial Williamsburg, "Colonial trade" | U.S. Census Bureau, Historical Statistics of the United States, Colonial Statistics (Series Z) | yes |
| About 12.5 million Africans were forced onto slave ships and about 10.7 million survived the voyage | SlaveVoyages (Trans-Atlantic Slave Trade Database), estimates | Smithsonian National Museum of African American History and Culture, "The Middle Passage" | yes |
| Enslaved West Africans' rice knowledge shaped South Carolina rice growing; enslaved people were a majority in South Carolina by the early 1700s | National Park Service, Gullah Geechee Cultural Heritage Corridor | Library of Congress, "African American Mosaic" and South Carolina colonial population | yes |
| The task system on rice plantations and the 1739 Stono Rebellion | South Carolina Encyclopedia, "Task system" and "Stono Rebellion" | National Park Service / National Register, Stono River Slave Rebellion Site | yes |
| Trade ran as a web of routes, not one triangle | Mystic Seaport Museum, "Triangular trade" teaching materials | Colonial Williamsburg, "The Atlantic world" | yes |
| Indentured servants worked in the Chesapeake and Middle Colonies | Library of Congress, "Immigration: Indentured servants" | Colonial Williamsburg, "Indentured servants" | yes |
Backed twice: 7. Cut: 0.

Sensitivity note: slavery and the Middle Passage. Enslaved people are named as people, their knowledge and resistance are shown, the composite is labeled as one, art never shows harm, and numbers are given plainly. A fresh-agent read of every card and image is needed before build.

Checks run (Python, scratchpad r8, 2026-11-09): six cargo cards have six chips each split two, two, two; 12.5 million minus 10.7 million is 1.8 million deaths, matching the card; three decades in order; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and card fit; at 680x425 the card is a sheet.
2. Each cargo's chips sort to their columns; enslaved workers' chips carry the forced label. (D2.Eco.3.3-5)
3. All routes together show a web, and the narrator says so. (D2.Geo.11.3-5)
4. The decade slider grows ports and plantations and takes the right causes. (D2.Geo.11.3-5)
5. Three day cards compare with today. (D2.His.2.3-5)
6. The Middle Passage card states the numbers and shows no goods icon.
7. The decade slider is never named before it shows.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no drawn routes or sailing; no network requests.

## Open questions
- Sensitivity flag: the enslaved woman is a composite with a common name from records, told by the narrator in the third person (default used: composite labeled as such, task system and Stono context, fresh-agent read before build).
- The module lists D2.Geo.9.3-5, which this tool can't teach honestly (default used: it moves to settle-the-valley; the module code list is Cory's to update).
