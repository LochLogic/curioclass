# Hunter to Farmer

## One idea
The child leads a band of thirty people on a hillside in the Fertile Crescent about 11,000 years ago, where wild wheat and barley grow, gazelle herds pass and a river runs, through twenty years; each year they split the band's work among foraging and hunting, tending the wild wheat stands, and planting fields, and watch food, people, work hours, health and the camp itself change (round huts become mud-brick houses, granaries appear, the dead are buried under the floors), with two droughts to test the plan; farming feeds more people but ties the band to one place with more work and poorer health, as early farmers' skeletons show, and the end map links the child's village to separate beginnings of farming in China, the Americas, New Guinea and Africa, so a sixth grader learns how a place's plants, animals and water shaped who people became, and how one village fits a change that happened again and again around the world.

## Not like
- river-kingdom (concept): later states and laws. Here the shift to farming before any state.
- settle-the-valley (4, spec): settlers changing a valley over five decades. Here the first farmers, 11,000 years ago.
- smoke-and-honey (concept): economics of a town. Here how and why farming began.
- border-trade-post (6, spec): trade between countries. Here one band's work and food.

## Who and how
- Grade 6, Social Studies (World History and Geography), module "Early Humans and the Neolithic Revolution". Standards: D2.His.1.6-8 (analyze connections among events and developments in broader historical contexts), D2.Geo.6.6-8 (explain how the physical and human characteristics of places and regions are connected to human identities and cultures).
- Format: simulator. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Twenty years of choices, then the result board and the world map. Extra: Two bands (the child's band beside a band that never farms, run by the same years and droughts). tool.json `modes: ["One band", "Two bands"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.6.6-8 | Split work each year among foraging, tending and planting, using what the place offers (wild cereals, gazelle, river, clay for bricks) | the place card; the camp changing (homes, granaries, burials, a shrine); the place-to-life links | 2, 3 |
| D2.Geo.6.6-8 (identity) | At the end, match each place feature to the way of life it shaped | the match board: wild wheat to fields, clay to mud-brick homes, stored grain to staying put and guarding, staying put to burying the dead under the house | 4 |
| D2.His.1.6-8 | Place the child's village on a world map with other places where farming began separately, each with its first crops and dates | the world map with dated pins | 5 |

## Screens and modes
Header (kit): title "Hunter to Farmer"; `One band`, `Two bands`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A hillside camp of round brush huts above a river. Wild wheat and barley sway on the slope; gazelles graze across the valley. A season dial (spring harvest, summer, autumn, winter rains) and a year counter at 1. The band's elder, Nara (made for this game), stands by the fire. The welcome is queued (`welcomeAfter: true`): "Your band of thirty lives here, about eleven thousand years ago. Each year you choose how everyone spends their work. Drag the stones to split the work, then tap Live this year." First hint: "Drag a work stone."

**Each year (focus: the work split and the camp).** At 1366x768 the camp fills the top with the meters at the side and the work split below; at 680x425 the meters become a strip and the split is a drawer.
- Ten work stones split among three jobs: Forage and hunt (gather plants, hunt gazelle, fish), Tend wild wheat (weed and protect the wild stands, harvest with flint sickles), Plant fields (clear ground, save and sow seed, store grain).
- `Live this year` plays the season dial once and updates five meters: Food (enough or not), People (the band's size), Work (hours a day), Health (a 1 to 10 score from diet variety and work), and Camp (what's built).
- The model (made for this game, tuned to what archaeologists describe; see Checks run):
  - Foraging feeds 1.15 people per stone-share, falling once the band grows past what its range can feed (about 40 people); 5 hours of work a day; varied diet, high health.
  - Tending wild wheat feeds 1.2; 6 hours a day.
  - Fields need a year to get going and then feed 1.8; 8 hours a day; only farmers can store grain, which carries food into the next year; fields lose half in a drought while foraging loses a quarter.
  - The band grows about 4 percent in a year with plenty, holds steady with just enough, and shrinks in hunger.
  - Droughts come in years 6 and 13.
- Camp changes as fields grow: storage pits, then a granary (granaries like those at Dhra' are among the oldest known, about 11,300 years old); round huts become rectangular mud-brick houses from river clay; the dead are buried under house floors; a shrine room appears. Each change opens a short card with what it meant ("Grain in a granary must be guarded. Now you can't move with the gazelles.").
- Sample runs over twenty years (shown on the result board after the child's own run): all foraging ends at about 43 people, 5 hours a day, health 10; foraging and tending about 47 people, 5.5 hours, health 9; a mix (3 forage, 2 tend, 5 plant) about 63 people, 6.7 hours, health 7.6; all fields about 59 people, 8 hours, health 6.

**The result board (the aha).** The child's twenty-year line for each meter beside the sample runs. Narrator: "Farming won on numbers. It cost more work, and people's health got worse. Early farmers' skeletons show it: shorter people, more tooth decay, more signs of hunger in childhood. So why did farming spread? Because more people could live in one place, and a village that farmed could outnumber one that didn't." A match board asks the child to link each place feature to the way of life it shaped (D2.Geo.6.6-8).

**The world map (D2.His.1.6-8).** The child's village pins to the Fertile Crescent (wheat, barley, lentils, goats and sheep; about 11,000 to 10,500 years ago). Then pins appear one by one, each a separate beginning: China (rice along the Yangtze, millet along the Yellow River, about 9,000 years ago or earlier); Mexico (squash about 10,000 and maize about 9,000 years ago); the Andes (potatoes and quinoa, about 8,000 years ago); New Guinea (taro and bananas at Kuk Swamp, about 7,000 years ago or earlier); Africa's Sahel (sorghum and pearl millet, about 5,000 to 4,500 years ago); eastern North America (sunflower and squash, about 5,000 years ago). The child places each pin's crop card from tiles. Narrator: "No one taught the world to farm. People in different places did it on their own, with the plants their places gave them."

**The end.** The camp at year twenty, the meters, the match board and the map. `Print` prints them.

**Two bands (extra).** The child's band and a band that never farms, side by side, through the same twenty years and droughts; the board compares them.

## Content
- The place card, three jobs, the model table, two droughts, six camp-change cards, the result board with four sample runs, the match board (five features), the world map (seven pins with crops and dates).
- Nara and the band are made up and labeled; the place, crops, dates, granaries, burials and health findings are real; the model numbers are a teaching model, labeled "made for this game".
- Dates are given as "about" and as "years ago", with ranges where sources differ.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Work stones drag or tap-then-place; the split always totals ten.
- `Live this year` can be tapped once per year; `Skip five years` repeats the same split.
- Keyboard: Tab to the stones and jobs; arrows move a stone; Enter to live the year.
- With Motion off the dial jumps to the year's end and camp changes appear without building up.

## Look
- Accent `--brand` #7a5418 earth ochre (header, work stones, meters); gold #f4c542 (ripe wheat, the active stone); paper #f9f5ec; ink #261a06; muted #5e5545.
- Contrast (WCAG 2.1, computed): white on brand 6.75:1; brand on paper 6.21:1; ink on paper 15.66:1; muted on paper 6.75:1; ink on gold 10.47:1.
- Never color alone: each meter shows its number and label; drought years carry a cracked-earth icon and the word "Drought".
- Different from this batch (agora blue, silk road mulberry, Rome crimson, border olive).

## Art
- Local FLUX (`scripts/localart.py`): the hillside camp in four stages (round huts; storage pits; mud-brick houses and a granary; a village with fields; 4, 16:9); wild wheat and gazelle close-ups (2, 1:1); seven world-map crop pictures (7, 1:1).
- People art goes to Gemini with `people: true`: Nara the elder (2 poses), the band foraging, tending with sickles, and sowing (3 scenes); cutouts yes.
- Drawn in code: the season dial, work stones, meters, the result chart, the match board, the world map.
About 18 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the narrator; `big-sister` as Nara the elder, who reports how the year went. `Curio.voice` with `scope: () => state.mode + ':' + state.year + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `split`: "Drag the work stones, then tap Live this year."
- event, whole, each year's report.
- event, whole, each camp-change card.
- event, whole, each drought.
- how `match`: "Link each place feature to the way of life it shaped."
- how `map`: "Tap a pin, then place its crop."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the yearly model from a small table, the meters and camp stages, the result chart with sample runs, the match board and the dated world map.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Years | Put all stones on fields from year 1 | Fields take a year to start; year 1 is lean, and the drought halves the harvest; the result board shows the cost in work and health. |
| Match | Link features at random | Each link checks; a wrong one plays "What did the clay make possible?" |
| Map | Place any crop on any pin | Each pin takes its own crop; dates show only when placed right. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `split`.
2. Year reports (whole), each waits; camp changes and droughts (whole).
3. Result board narration (whole). `match`.
4. `map`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1.6-8 and D2.Geo.6.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Farming began in the Fertile Crescent about 11,000 to 10,500 years ago with wheat, barley, lentils, goats and sheep | Smithsonian National Museum of Natural History, Human Origins, "Agriculture" | Larson et al., "Current perspectives and the future of domestication studies," PNAS (2014) | yes |
| Separate beginnings in China, Mexico, the Andes, New Guinea, Africa's Sahel and eastern North America, with crops and dates | Larson et al., PNAS (2014), domestication centers map | Encyclopaedia Britannica, "Origins of agriculture" | yes, dates given as "about" |
| Granaries at Dhra', about 11,300 years ago | Kuijt and Finlayson, "Evidence for food storage and predomestication granaries 11,000 years ago in the Jordan Valley," PNAS (2009) | Smithsonian Magazine, "Ancient granaries" (2009) | yes |
| Round huts gave way to rectangular mud-brick houses; burials under house floors | Encyclopaedia Britannica, "Neolithic" and "Jericho" | Smithsonian Human Origins, "Agriculture" | yes |
| Early farmers were often shorter and had more tooth decay and signs of childhood stress than foragers | Larsen, "The agricultural revolution as environmental catastrophe," Quaternary International (2006) | Mummert et al., "Stature and robusticity during the agricultural transition," Economics and Human Biology (2011) | yes |
| Kuk Swamp, New Guinea, early cultivation | UNESCO World Heritage, "Kuk Early Agricultural Site" | Denham et al., Science (2003) | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r10, 2026-11-09): the yearly model over twenty years with droughts in years 6 and 13 gives all foraging 43 people, 5.0 hours, health 10.0; forage and tend 47, 5.5, 9.0; the 3-2-5 mix 63, 6.7, 7.6; all fields 59, 8.0, 6.0; farming beats foraging on people in every farming run and loses on hours and health in every one; the world-map dates sort from 11,000 to 5,000 years ago; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 camp, meters and split fit; at 680x425 meters are a strip and the split a drawer.
2. Each year's split changes the five meters by the model. (D2.Geo.6.6-8)
3. The camp changes with farming: storage, granary, mud-brick, burials, shrine. (D2.Geo.6.6-8)
4. The match board links place features to ways of life. (D2.Geo.6.6-8)
5. The world map places seven separate beginnings with crops and dates. (D2.His.1.6-8)
6. Two bands runs both bands through the same years.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no dial spinning or building up; no network requests.

## Open questions
None.
