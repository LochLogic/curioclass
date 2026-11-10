# Expansion Map

## One idea
A map of North America in 1800 sits under a time slider that runs to 1860, and as the child drags it the United States grows piece by piece (the Louisiana Purchase in 1803, Florida in 1819, Texas in 1845, Oregon in 1846, the Mexican Cession in 1848, the Gadsden Purchase in 1853) while a second layer, which the child can never switch off, shows Native nations' lands shrinking through treaties and the Indian Removal Act of 1830, with the Cherokee forced west on the Trail of Tears in 1838-39; at each step the child opens a card that names what pulled settlers west (cheap land, gold in 1848, the telegraph and about 9,000 then 30,000 miles of railroad), who already lived there, and how the land changed hands (purchase, war, treaty, forced removal), and adds one tile to a cause and effect board; at the end the child writes how new technology and the idea that the nation should spread across the continent changed the land, the people and the argument over slavery in new states, so an eighth grader learns how changes in transportation and communication shaped settlement and how expansion caused and resulted from events.

## Not like
- nations-of-north-america (5, concept): today's countries. Here one country's growth from 1800 to 1860.
- revolution-road (5, spec): a road to independence. Here a nation's spread after it.
- civil-war-map-room (8, spec): campaigns on a map. Here borders on a map.
- the-shrinking-lake (7, spec): a lake shrinking. Here lands shrinking for the people who lived there.

## Who and how
- Grade 8, Social Studies (Geography and History), module "Westward Expansion". Standards: D2.Geo.7.6-8 (explain how changes in transportation and communication technology influence the spatial connections among human settlements and affect the diffusion of ideas and cultural practices), D2.His.14.6-8 (explain multiple causes and effects of events and developments in the past).
- Format: map. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Seven steps on the slider, two layers, cards, the cause and effect board, the travel-time panel, the closing card. Extra: Whose map? (the child compares an 1850s U.S. map with a map of Native nations' lands at the same date and lists what each leaves off). tool.json `modes: ["Map", "Whose map?"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.7.6-8 | Step the travel-time panel through the decades and connect new routes and lines to where people settled | days from New York to the West by wagon, steamboat, rail; telegraph lines; settlements growing along them | 3 |
| D2.His.14.6-8 | At each step, add the cause and effect tiles to the board | the board with because lines, including removal and the slavery question in new states | 2, 4 |

## Screens and modes
Header (kit): title "Expansion Map"; `Map`, `Whose map?`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A map of North America in 1800 with the United States east of the Mississippi, Spanish and British claims, and a layer of Native nations' lands, labeled with nations' own names where known. A slider runs from 1800 to 1860. The welcome is queued (`welcomeAfter: true`): "In 1800 the United States ended at the Mississippi. By 1860 it reached the Pacific. Each piece of land was already someone's home. Drag the slider to 1803." First hint: "Drag the slider to 1803."

**The steps (focus: the map and the card).** At 1366x768 the map fills the center with the card right; at 680x425 the card is a sheet. The Native lands layer stays on in every step.
1. 1803, the Louisiana Purchase from France, about doubling the country's size; Lewis and Clark (1804 to 1806) and the many nations they met.
2. 1819, Florida from Spain (the Adams-Onis Treaty).
3. 1830, the Indian Removal Act; removal of the Choctaw, Creek, Chickasaw, Seminole and Cherokee; Cherokee leader John Ross's protest to Congress; the Trail of Tears (1838 to 1839), where about 4,000 of some 16,000 Cherokee died. Shown with a map and numbers, no images of suffering.
4. 1845, Texas annexed, after Texas had broken from Mexico in 1836 in part to keep slavery, which Mexico had abolished.
5. 1846, Oregon divided with Britain at the 49th parallel; the Oregon Trail.
6. 1848, the Mexican Cession after the war with Mexico (the Treaty of Guadalupe Hidalgo), about half of Mexico's territory; gold in California; tens of thousands of California Native people die in the years after from violence, disease and starvation.
7. 1853 to 1854, the Gadsden Purchase.
- Each card names: what pulled settlers, who already lived there, how the land changed hands (purchase, war, treaty, forced removal), and a short real line (under 15 words, credited) from someone there.

**The travel-time panel (D2.Geo.7.6-8).** Days from New York to the Mississippi and to California, by wagon, by canal and steamboat (the Erie Canal 1825), and by rail; telegraph lines spreading from 1844 (Washington to Baltimore). The child connects each new line to the settlements growing along it and answers "How did this change where people lived and how fast news spread?" Railroad miles: about 9,000 in 1850 and about 30,000 in 1860, labeled "about".

**The cause and effect board (D2.His.14.6-8).** At each step the child adds tiles: causes (cheap land, gold, new transportation, the belief later called Manifest Destiny, which the card explains in plain words and labels as a belief) and effects (Native nations removed and lands lost, war with Mexico, Mexican Americans in the Southwest becoming U.S. residents, the fight over whether new states would allow slavery: the Missouri Compromise 1820, the Compromise of 1850). Each tile needs a because.

**The closing card (the aha).** "By 1860 the map of the United States had grown about three times larger than in 1800. The map of Native nations' lands had shrunk to a fraction. And every new state reopened the question of slavery." The child writes one line on how technology and the belief in expansion together changed the land and its people.

**The end.** The final map with both layers, the travel-time panel, the board and the line. `Print` prints them.

**Whose map? (extra).** An 1850s U.S. map beside a map of Native nations' lands from the same years; the child lists what each map leaves off.

## Content
- Seven steps with border changes and the Native lands layer; cards with pulls, people, how land changed hands and one real line; the travel-time panel; board tiles; the closing card; two maps for Whose map?.
- All dates, figures, treaties and quotes are real and sourced; figures are rounded and labeled "about"; Native nations named with their own names where known.
- The Native lands layer cannot be switched off.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The slider snaps to the seven steps; each step's card must be read and its tiles placed before the next.
- The child can drag back to any earlier step.
- Keyboard: Tab to the slider, the card, the panel and the board; arrows move the slider; Enter places tiles.
- With Motion off borders change at once without growing.

## Look
- Accent `--brand` #82511b prairie rust (header, the slider, cards); gold #f4c542 (the new piece of land, a placed tile); paper #faf4ec; ink #291806; muted #605346.
- Contrast (WCAG 2.1, computed): white on brand 6.68:1; brand on paper 6.12:1; ink on paper 15.65:1; muted on paper 6.81:1; ink on gold 10.52:1.
- Never color alone: each piece of land carries its name and year; the Native lands layer uses a pattern and labels as well as color.
- Different from this batch (dusk violet, map slate, claret, ballot green).

## Art
- Public domain (Library of Congress, National Archives, ids checked at build): Royce's "Indian Land Cessions in the United States" plates (1899); the Treaty of Guadalupe Hidalgo; a portrait of John Ross; an 1850s railroad map; Morse's first telegraph message strip (1844); a Disturnell map of Mexico (1847). Each with credit.
- Drawn in code: the base map, both layers, the slider, the panel, the board.
- Local FLUX (`scripts/localart.py`): a prairie with wagon ruts at dawn, no people (1, 16:9).
About 7 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the narrator; `warm-teacher` as the hints and the reader of real lines, introduced each time as "from" the speaker. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each step's card.
- event, whole, each real line.
- how `tiles`: "Add this step's causes and effects to the board."
- how `travel`: "Step the travel panel and link each line to a settlement."
- how `slide`: "Drag the slider to the next year."
- event, whole, the closing card.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the time slider, the two map layers, cards, the travel-time panel, the board, Whose map?.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Board | Drop every tile as a cause | Each tile checks its column and needs a because. |
| Travel | Link lines to random settlements | Each link checks that the settlement lies on the line. |
| Slider | Drag straight to 1860 | The slider snaps to each step and waits for its tiles. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `slide`; step card (whole), waits; real line (whole).
2. `tiles`, for each step.
3. `travel`.
4. Closing card (whole); `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.7.6-8 and D2.His.14.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Land added: Louisiana 1803, Florida 1819, Texas 1845, Oregon 1846, Mexican Cession 1848, Gadsden 1853 | National Archives, "Territorial acquisitions of the United States" | U.S. Department of State, Office of the Historian | yes |
| The Indian Removal Act (1830) and the Trail of Tears, about 4,000 of some 16,000 Cherokee died | National Archives, "Indian Removal Act" | National Park Service, Trail of Tears National Historic Trail | yes |
| John Ross's protests to Congress | Library of Congress, "Indian Removal" primary documents | Cherokee Nation, history of John Ross | yes |
| Guadalupe Hidalgo ceded about half of Mexico's territory | National Archives, Treaty of Guadalupe Hidalgo | U.S. Department of State, Office of the Historian | yes |
| California Native population fell sharply after 1848 from violence, disease and starvation | Madley, "An American Genocide" (Yale, 2016) | California Native American Heritage Commission, "Short overview of California Indian history" | yes |
| Railroad miles about 9,000 in 1850 and about 30,000 in 1860; the 1844 telegraph | Library of Congress, "Railroad maps" collection essay | Smithsonian National Museum of American History, "Morse telegraph" | yes |
| Native land loss mapped from treaties | Royce, "Indian Land Cessions in the United States" (1899, Library of Congress) | Saunt, "Invasion of America" interactive map (University of Georgia) | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: forced removal, deaths on the Trail of Tears and violence against California Native people are shown with maps, numbers and named leaders, without images of suffering; the Native lands layer is always on; "Manifest Destiny" is explained as a belief, not a fact. A fresh-agent read of the step cards is needed before build.

Checks run (Python, scratchpad r16, 2026-11-09): steps in date order (1803, 1819, 1830, 1845, 1846, 1848, 1853); about 4,000 of 16,000 is about one in four; railroad miles grew about 3.3 times from 1850 to 1860; the slider has seven stops; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and card; at 680x425 sheet.
2. Each step adds land and shrinks Native lands, with a card and tiles on the board. (D2.His.14.6-8)
3. The travel panel links routes and lines to settlements. (D2.Geo.7.6-8)
4. The board checks causes and effects with because lines. (D2.His.14.6-8)
5. The Native lands layer can't be switched off.
6. Whose map? lists what each map leaves off.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: borders change without growing; no network requests.

## Open questions
- Sensitivity flag: Native removal, the Trail of Tears and violence against California Native people (default used: maps, numbers and named leaders without images of suffering, Native layer always on, Manifest Destiny explained as a belief, fresh-agent read before build).
