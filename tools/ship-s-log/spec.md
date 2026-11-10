# Ship's Log

## One idea
The child keeps the log of the real Mayflower voyage of 1620, and at each page faces a choice its planners faced (why these families are leaving, how much food and beer to load, whether to sail late in the year after the Speedwell leaked twice, what to do when a main beam cracks mid-ocean, where to land when shoals turn them back from the Hudson River), then reads what really happened and why; on the shore side, the log opens to the Wampanoag homeland the ship reached, where an epidemic had already killed many Wampanoag people and nearly all of the Patuxet town where the colonists built, and the child meets the choices of Wampanoag leaders; at the end a cause-and-effect map joins faith, money, winds, season and the earlier epidemic to the first year's outcomes, including that about half the passengers died that winter and that the alliance Ousamequin chose shaped what came next, so a fifth grader learns how causes stack up into effects and how land, weather and beliefs moved people.

## Not like
- colonial-trade-routes (5, spec, this batch): a century of trade. Here one voyage and its first year.
- revolution-road (concept): causes of the Revolution. Here causes and effects of a 1620 voyage.
- nations-of-north-america (concept): a map of Native nations. Here one nation's view of one arrival.
- settle-the-valley (4, spec): a made-up valley over fifty years. Here one real voyage and one year.

## Who and how
- Grade 5, Social Studies (History and Geography), module "Exploration and Colonization". Standards: D2.His.14.3-5 (explain probable causes and effects of events and developments), D2.Geo.7.3-5 (explain how cultural and environmental characteristics affect the distribution and movement of people, goods, and ideas).
- Driver: one child alone (tool.json `driver: "student"`); `Read` reads every page. Controls 44 px or more.
- Eight log pages, two shore pages, then the cause-and-effect map. Extra: Jamestown, 1607, for comparison. tool.json `modes: ["Mayflower", "Jamestown"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.7.3-5 | At pages about season, winds and route, pick a choice and read how wind, currents, autumn storms and beliefs moved the ship and its people | a route map with westerly winds and the Gulf Stream drawn; the ship's track | 2 |
| D2.His.14.3-5 | After each page, drag the page's cause chip onto the map; at the end, join causes to effects | the cause-and-effect map filling page by page; joined cords | 3, 4 |
| D2.His.14.3-5 (both sides) | Read the two shore pages and add the Wampanoag causes (the epidemic, Ousamequin's choice) to the map | Wampanoag chips on the same map | 5 |

## Screens and modes
Header (kit): title "Ship's Log"; `Mayflower`, `Jamestown`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** An open logbook on a ship's table; out the window, an English harbor. The welcome is queued (`welcomeAfter: true`): "In 1620, a ship called the Mayflower carried 102 passengers across the ocean. You'll keep its log. Why are these families leaving? Read the first page." First hint: "Tap the first page."

**Log pages (focus: one page and its choice).** At 1366x768 the logbook sits left and the route map right; at 680x425 the map folds behind a `Map` tab.
1. Why leave? Some passengers (called Separatists, later Pilgrims) wanted to worship apart from the Church of England; others came for land and work; investors in London paid for the voyage hoping for profit. Choice: sort four reasons into Faith, Money or Land. (Cause chip: faith and money.)
2. Supplies: how much to load for a long trip and a winter. Choices: little (cheap), enough for the trip, enough for the trip and the winter. Then: what they really took (hardtack, salt beef and fish, dried peas, cheese, and beer, which kept better than water), and that supplies ran low by spring.
3. Two ships: the Speedwell leaked twice and turned back; passengers crowded onto the Mayflower. Choice: wait for spring, or sail now in September. They sailed on September 6, 1620 (old calendar), late in the year. (Cause chip: a late start.)
4. Winds and currents: the route map shows westerly winds and the Gulf Stream against a ship sailing west. Choice: which way is fastest (south with the trade winds, or straight west). They went straight across against the wind, so the crossing took 66 days.
5. Storms and a cracked beam: autumn gales cracked a main beam. Choice: turn back or fix it. They raised it with a great iron screw brought from Holland and sailed on.
6. Land! They sighted Cape Cod on November 9 and turned south toward the Hudson River, where their permission to settle pointed, but dangerous shoals turned them back. Choice: keep trying south, or stay. They stayed. (Cause chip: winds, shoals and winter coming.)
7. An agreement: because they were outside their planned place, men on board signed the Mayflower Compact to make rules together.
8. A hard winter: they built on the site of Patuxet in late December; about half of the passengers died by spring from cold, hunger and sickness. (Effect chip.)

**Shore pages (focus: the other side of the log).** The book turns over to show a page from the shore, built from Wampanoag sources:
- The Wampanoag homeland: the Wampanoag had lived here for over 12,000 years, in many towns, farming, fishing and hunting with the seasons. From about 1616 to 1619 an epidemic brought by earlier European ships killed many Wampanoag people; Patuxet was left nearly empty. Tisquantum, a Patuxet man kidnapped by an English captain in 1614, had made his way home to find his town gone. (Cause chip: the epidemic.)
- Ousamequin's choice: in March 1621 the Wampanoag leader Ousamequin (also called Massasoit) met the colonists and made an alliance, weighing the newcomers' guns against his rivals, the Narragansett, and his weakened people. Tisquantum helped as a translator and showed the colonists how to plant corn with fish. (Cause chip: the alliance.)
- The child adds both chips to the cause-and-effect map.

**Cause-and-effect map (end state).** Chips from every page sit on the map. The child drags cords from causes to effects: faith and money to the voyage; the late start and autumn storms to the cracked beam and the Cape Cod landfall; winter and low supplies to the deaths; the epidemic to an empty Patuxet and a weakened Wampanoag nation; the alliance to the colony's survival and to what came next. Narrator: "Many causes stacked up. Some effects were good for one side and terrible for the other. The Wampanoag people are still here today, in Mashpee and Aquinnah and beyond." `Print` prints the log pages, shore pages and the map.

**Jamestown (extra).** A shorter log of the 1607 Jamestown voyage (three ships, a spring arrival, swampy ground and bad water, the Powhatan paramount chiefdom) with its own cause chips, to compare with the Mayflower's map.

## Content
- Eight log pages with choices and real outcomes; two shore pages; ten cause and effect chips with a set web of cords; the Jamestown extra with five pages.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pages open in order; the shore pages open after page 8. A choice never changes history: the page always shows what really happened and why.
- Keyboard: arrow keys turn pages; Tab through choices and chips.
- With Motion off pages turn without animation and the ship jumps along its track.

## Look
- Accent `--brand` #5a3825 ship's oak (header, logbook frame, the track); gold #f4c542 (the selected choice, a joined cord); paper #f8f4ef; ink #1e120a; muted #5e5349.
- Contrast (WCAG 2.1, computed): white on brand 10.36:1; brand on paper 9.46:1; ink on paper 16.73:1; muted on paper 6.83:1; ink on gold 11.27:1.
- Never color alone: winds and currents are labeled arrows; cause and effect chips carry the words "Cause" and "Effect".
- Different from this batch (timeline violet, trade harbor teal, article red, interest green).

## Art
- Public domain (credited): a 1600s map of New England (for example John Smith's 1616 "New England" map, Library of Congress, checked at build).
- People art goes to Gemini with `people: true`: passengers on deck (1 scene); Ousamequin and Tisquantum (1 scene each), drawn from Wampanoag-led museum references (Plimoth Patuxet Museums' Wampanoag Homesite) and checked by the fresh-agent read.
- Local FLUX (`scripts/localart.py`): the ship's table and harbor (1, 16:9); a storm at sea (1); the shore at Patuxet (1).
- Drawn in code: the logbook, the route map with winds and currents, chips, cords.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as the narrator, who reads the shore pages; `firm-captain` reads the log entries. `Curio.voice` with `scope: () => state.mode + ':' + state.page`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each log page (log voice).
- how `choose`: "What would you choose? Tap one."
- event, whole, each "what really happened" line.
- how `chip`: "Drag the cause to the map."
- event, whole, each shore page (narrator).
- how `cords`: "Drag a cord from a cause to its effect."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the logbook pages with choices and outcomes, the route map with wind and current layers, the cause-and-effect map with set cords.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Choices | Tap any choice | Any choice is fine; history plays the same, and the cause chip is what counts. |
| Cords | Join chips at random | Only set cause-to-effect cords hold; a wrong one asks "Did this happen first? Did it lead to that?" |
| Shore pages | Skip them | The cause-and-effect map can't finish without the two Wampanoag chips. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Each page: log (whole), waits; `choose`; outcome (whole); `chip`.
2. Shore pages (whole); `chip`.
3. Map: `cords`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.14.3-5 and D2.Geo.7.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| 102 passengers; Speedwell leaked twice; sailed September 6, 1620; 66 days; cracked beam raised with an iron screw; Cape Cod sighted November 9; shoals turned them from the Hudson; Mayflower Compact | Plimoth Patuxet Museums, "Mayflower and Mayflower Compact" | William Bradford, Of Plymouth Plantation (Massachusetts State Library / public domain text) | yes |
| About half the passengers died the first winter | Plimoth Patuxet Museums, "The first winter" | Mayflower Society, "The voyage" | yes |
| An epidemic about 1616 to 1619 killed many Wampanoag people and emptied Patuxet | Plimoth Patuxet Museums, Wampanoag Homesite and "Patuxet" | Mashpee Wampanoag Tribe, "History" | yes |
| Tisquantum was kidnapped in 1614 and returned to find Patuxet gone; Ousamequin made an alliance in March 1621 | National Museum of the American Indian, "Wampanoag" and Native Knowledge 360 Thanksgiving materials | Wampanoag Tribe of Gay Head (Aquinnah), "History" | yes |
| Westerly winds and the Gulf Stream work against westbound ships in the North Atlantic | NOAA Ocean Service, "What is the Gulf Stream?" | National Geographic Education, "Prevailing winds" | yes |
| Jamestown 1607: three ships, swampy site, Powhatan paramount chiefdom | National Park Service, Historic Jamestowne | Jamestown-Yorktown Foundation, "Powhatan Indians" | yes |
Backed twice: 7. Cut: 0.

Sensitivity note: Native history and epidemic deaths. The shore pages come from Wampanoag-led and Wampanoag nation sources, the epidemic is stated plainly without graphic detail, Wampanoag leaders are shown making choices, and the end says the Wampanoag are here today. A fresh-agent read of the shore pages and art is needed before build.

Checks run (Python, scratchpad r8, 2026-11-09): ten chips form a web with every cord running from an earlier event to a later one; eight log pages are in date order (September 6 to spring 1621); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 logbook and map fit; at 680x425 the map is a tab.
2. Wind, current and season pages show their effect on the ship's track. (D2.Geo.7.3-5)
3. Each page's chip lands on the map. (D2.His.14.3-5)
4. Only set cords hold; the finished map shows all causes and effects. (D2.His.14.3-5)
5. The two shore pages play and their chips are needed to finish. (D2.His.14.3-5)
6. Each log choice shows what really happened.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no page turns or sailing; no network requests.

## Open questions
- Sensitivity flag: Wampanoag history and the epidemic, told by the narrator from Wampanoag sources (default used: Wampanoag-led sources, plain statements, art from Wampanoag Homesite references, fresh-agent read before build).
