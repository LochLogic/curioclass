# Climate on the Move

## One idea
One long timeline runs from 1300 to today with a temperature and rainfall band beneath it and four case markers: the Little Ice Age (with the 1816 "year without a summer"), the Dust Bowl of the 1930s, the Sahel droughts from the late 1960s, and Hurricane Maria in Puerto Rico in 2017; the student opens a case, places its events (a failed harvest, a migration, a price spike, a new law) on the timeline while a linked map shows where people moved and how farming and trade shifted, and each case pairs data with one family's story (made for this game); a compare view lines up slow change (the Little Ice Age, the Sahel) against sudden shock (Dust Bowl storms, the hurricane), and the student sorts effects into migration and settlement, land use and trade, and politics; at the end the student writes how one case's effects reached people who never felt the weather themselves (grain prices, newcomers in a distant city, a new policy, a hospital short of supplies), so a tenth grader learns how long-term climate variability shapes migration, settlement and land use, how environmental change shifts trade and farming, and what catastrophes do to trade, politics and migration.

## Not like
- the-shrinking-lake (7, spec): one lake's decline. Here four cases across 700 years.
- suburb-boom (11, concept): land use shaped by policy. Here land use shaped by climate.
- independence-timeline (10, spec): a political timeline. Here a climate timeline.
- layers-and-scales (9, spec): thematic maps at many scales. Here cases moving across maps over time.

## Who and how
- Grade 10, Social Studies (Geography), module "Climate on the Move". Standards: D2.Geo.9.9-12 (evaluate the influence of long-term climate variability on human migration and settlement patterns, resource use, and land uses at local-to-global scales), D2.Geo.10.9-12 (evaluate how changes in the environmental and cultural characteristics of a place or region influence spatial patterns of trade and land use), D2.Geo.12.9-12 (evaluate the consequences of human-made and natural catastrophes on global trade, politics, and human migration).
- Format: timeline. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Four cases with about eight events each, the linked map, four family stories, the compare view, the ripple card. Extra: Our case (a group adds a local climate event with its own cards, kept on the device). tool.json `modes: ["Timeline", "Our case"]`, `minutes: "30-40"`, `grades_label: "Grade 10"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.9.9-12 | Place the slow-change cases' events and trace migration and settlement on the map from local to global | the Little Ice Age and Sahel events; the climate band; migration arrows | 2 |
| D2.Geo.10.9-12 | Sort each case's effects on farming and trade into land use and trade, and mark the shifts on the map | crop zones and trade routes moving | 3 |
| D2.Geo.12.9-12 | Follow the sudden-shock cases to effects on trade, politics and migration, then write the ripple card | the Dust Bowl and Maria events; the ripple card | 3, 4 |

## Screens and modes
Header (kit): title "Climate on the Move"; `Timeline`, `Our case`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A timeline from 1300 to today, with a band below showing reconstructed Northern Hemisphere temperature (cooler in the Little Ice Age, warming since 1900) and four case markers. A world map sits above. The welcome is queued (`welcomeAfter: true`): "Weather happens in a place. Its effects travel. Four cases, seven hundred years. Open a case." First hint: "Tap a case marker."

**The cases (focus: the timeline and the map).** At 1366x768 the map is above and the timeline below with the case card right; at 680x425 the card is a sheet. Each case has about eight event cards to place and a family story in four short scenes.
1. The Little Ice Age (about 1300 to 1850), slow change: the Great Famine in northern Europe (1315 to 1317); Norse Greenland settlements abandoned (by the 1400s); colder decades in the 1600s with failed harvests, unrest and wars across Europe and China; Alpine glaciers advancing; frost fairs on the frozen Thames (the last in 1814); the eruption of Tambora (1815) and the "year without a summer" (1816), with failed harvests in New England and Europe, food riots, and families moving west into Ohio and the American Midwest. Family: a Vermont farm family that leaves for Ohio in 1817.
2. The Dust Bowl (1930s), sudden shock on top of drought: plowed-up prairie, drought from 1930, Black Sunday (April 14, 1935); about 2.5 million people left the Plains states by 1940, hundreds of thousands to California; the Soil Conservation Service (1935) and shelterbelts. Family: an Oklahoma tenant family heading to California. Dorothea Lange's photographs, credited.
3. The Sahel droughts (late 1960s to 1980s), slow change: rainfall fell sharply for two decades; herds and harvests failed; famine in 1972 to 1974 and 1983 to 1985; people moved to cities and south to coastal countries such as Cote d'Ivoire; herding routes shifted south; Lake Chad shrank; Sahel countries formed CILSS (1973) to work on drought together. Rainfall partly recovered from the 1990s. Family: a herding family in Niger who move to Niamey and then send a son to Abidjan.
4. Hurricane Maria (September 20, 2017), sudden shock: a Category 4 landfall in Puerto Rico; the whole island lost power, and some areas waited about eleven months; an official estimate of 2,975 excess deaths; well over 100,000 people left for the U.S. mainland within a year, many to Florida; a factory that made most of the IV fluid bags used in U.S. hospitals was damaged, causing shortages far away; arguments in Congress over aid and the Jones Act. Family: a San Juan family whose daughter moves to Orlando.
- Event cards are placed on the timeline; a wrong date plays a reason line. Each placed card adds arrows or shading on the map.

**The compare view (D2.Geo.10.9-12, D2.Geo.12.9-12).** The four cases side by side, slow (Little Ice Age, Sahel) against sudden (Dust Bowl, Maria). The student sorts every effect card into migration and settlement, land use and trade, or politics. A note on the Dust Bowl: drought was the trigger, but farming choices that stripped the grass made it a disaster.

**The ripple card (the aha).** The student picks one case and writes how its effects reached people far away who never felt the weather: "In ___, the ___ caused ___, which reached ___ in ___ through ___." Narrator: "You don't have to stand in the storm for it to reach you."

**The end.** The filled timeline, the map, the sort and the ripple card. `Print` prints them.

**Our case (extra).** A group adds a local climate event (a flood, a drought, a storm) with its own cards; kept on the device.

## Content
- Four cases with about 32 event cards, four families in four scenes each, the climate band, map layers, the compare sort with about 24 effect cards, the ripple card.
- The families are made up and labeled; events, figures and dates are real and sourced; figures are rounded and labeled "about" where estimates vary.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cases open in any order; the compare view opens after three.
- Event cards snap to their decade; a wrong placement plays a reason line and returns the card.
- Keyboard: Tab to case markers, event cards, the timeline, the map and the sort; arrows move a card along the timeline; Enter places.
- With Motion off arrows and shading appear without drawing.

## Look
- Accent `--brand` #1d5a6e sea teal (header, the timeline, case cards); gold #f4c542 (the card in hand, a placed event); paper #eef5f7; ink #08202a; muted #4c5a60.
- Contrast (WCAG 2.1, computed): white on brand 7.66:1; brand on paper 6.95:1; ink on paper 15.23:1; muted on paper 6.48:1; ink on gold 10.33:1.
- The climate band uses a blue to orange ramp checked for color-vision deficiency, with values labeled.
- Never color alone: map arrows carry labels; sort columns carry words.
- Different from this batch (wallet maroon, workbench green, terracotta, circuit violet).

## Art
- Public domain photographs (Library of Congress FSA collection, NOAA, FEMA, ids checked at build): Dorothea Lange's Dust Bowl migrant photographs (1936); a dust storm approaching Stratford, Texas (1935, NOAA); a Thames frost fair print (1814); a NOAA satellite image of Hurricane Maria (2017); a FEMA photograph of repair crews in Puerto Rico. Each with credit.
- Local FLUX (`scripts/localart.py`): a Vermont farm in snow in June (1, 16:9); a Sahel village in drought (1, 16:9).
- People art goes to Gemini with `people: true`: the four families (4; cutout yes).
- Drawn in code: the timeline, the climate band, the map, the sort, the ripple card.
About 11 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the narrator; `warm-teacher` as the hints and the family scenes' teller. `Curio.voice` with `scope: () => state.mode + ':' + state.case + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each case opening.
- event, whole, each family scene.
- how `place`: "Drag each event to its place on the timeline."
- how `compare`: "Sort each effect into migration, land use and trade, or politics."
- how `ripple`: "Pick a case and write how it reached people far away."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the timeline with the climate band, the linked map, case cards and family scenes, the compare sort, the ripple card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Timeline | Drop cards anywhere | Each card snaps only to its decade. |
| Sort | Put every effect under migration | Each effect checks its column, with a reason line. |
| Ripple | Name a place in the storm | The ripple must reach a place outside the case's region. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Case opening (whole), waits; family scene (whole).
2. `place`, for each case.
3. `compare`.
4. `ripple`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.9.9-12, D2.Geo.10.9-12 and D2.Geo.12.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The Little Ice Age, the Great Famine, Greenland, the 1600s crisis | Parker, "Global Crisis" (Yale, 2013) | Fagan, "The Little Ice Age" (Basic Books, 2000) | yes |
| Tambora (1815) and the 1816 "year without a summer," with migration west from New England | NOAA Climate.gov, "1816: the year without a summer" | Wood, "Tambora: The Eruption That Changed the World" (Princeton, 2014) | yes |
| Northern Hemisphere temperature reconstruction for the band | IPCC AR6 Working Group I (2021), chapter 2 | PAGES 2k Consortium, Nature Geoscience (2019) | yes |
| The Dust Bowl: Black Sunday (April 14, 1935), about 2.5 million left the Plains by 1940, the Soil Conservation Service (1935) | National Drought Mitigation Center, "Dust Bowl" | Library of Congress, FSA collection notes; Worster, "Dust Bowl" (Oxford, 1979) | yes |
| Sahel rainfall decline from the late 1960s, famines, migration, CILSS (1973), partial recovery since the 1990s | NOAA Climate.gov, "Sahel drought" | Nicholson, "The West African Sahel: a review" (2013) | yes |
| Hurricane Maria: 2,975 excess deaths (official estimate); island-wide outage | George Washington University Milken Institute study (2018), adopted by Puerto Rico's government | NOAA National Hurricane Center, Tropical Cyclone Report AL152017 | yes |
| Out-migration from Puerto Rico after Maria, well over 100,000 in a year | Center for Puerto Rican Studies, Hunter College (2018) | U.S. Census Bureau, population estimates | yes, as a range |
| IV fluid bag shortages after Maria | U.S. Food and Drug Administration statements (2017-2018) | American Society of Health-System Pharmacists, shortage reports | yes |
Backed twice: 9. Cut: 0.

Checks run (Python, scratchpad r18, 2026-11-09): case dates in order (1315, 1816, 1935, 1972, 2017); the timeline spans 1300 to 2026; the compare view opens at three of four cases; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map, timeline and card; at 680x425 sheet.
2. Slow-change cases trace migration and settlement on the map. (D2.Geo.9.9-12)
3. The compare view sorts effects into migration, land use and trade, and politics. (D2.Geo.10.9-12, D2.Geo.12.9-12)
4. The ripple card names an effect reaching a distant place. (D2.Geo.12.9-12)
5. Each case pairs its data with one family's story.
6. Our case stays on the device.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no drawing arrows; no network requests.

## Open questions
- The idea card asks that the recent hurricane's figures be checked against current sources (default used: Hurricane Maria in 2017, the official 2,975 excess-death estimate, and out-migration given as "well over 100,000"; recheck at build).
