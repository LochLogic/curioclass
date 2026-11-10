# Columbian Exchange

## One idea
Two coasts face each other across the Atlantic, and a pile of picture cards (potato, maize, tomato, cacao, chili pepper, horse, cattle, wheat, sugarcane, smallpox, measles, malaria) waits on the dock; the child sorts each card to the side where it began, the Americas or Afro-Eurasia, then sends it across by ship and watches three linked panels change on both sides: diets (potatoes in Europe, maize in Africa, chilies in Asia), populations (Indigenous peoples devastated by smallpox and measles, while new crops fed growing populations elsewhere) and plantations (sugar on hot, wet land, and the forced transport of enslaved Africans); some cards ask what land a crop needs, and the end is a cause-and-effect chain the child builds from one card, so a seventh grader learns the many causes and effects of the exchange, how ships and routes spread crops, animals and germs, and how the land shaped what was grown and traded.

## Not like
- colonial-trade-routes (5, spec): the triangular trade's routes. Here what crossed and what it changed.
- ship-s-log (5, spec): one voyage. Here a century of crossings.
- silk-road-traders (6, spec): overland trade in goods. Here living things and germs at sea.
- tenochtitlan-builder (7, spec): one city before 1521. Here what came after, on both sides.

## Who and how
- Grade 7, Social Studies (History), module "Age of Exploration". Standards: D2.His.14.6-8 (explain multiple causes and effects of events and developments in the past), D2.Geo.7.6-8 (explain how changes in transportation and communication technology influence the spatial connections among human settlements and affect the diffusion of ideas and cultural practices), D2.Geo.11.6-8 (explain how the relationship between the environmental characteristics of places and production of goods influences the spatial patterns of world trade).
- Format: sort. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Sort, send, panels, land questions, the chain. Extra: Trace your dinner (one meal's foods sorted by where they began). tool.json `modes: ["The exchange", "Trace your dinner"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.7.6-8 | Sort each card to its home, then drag it onto a ship to cross | the ship's route drawn; the card arriving and spreading on the far side | 2 |
| D2.Geo.11.6-8 | Answer land cards: what land each crop needs, and where it could grow | the climate band lighting up on the map; the plantation or farm growing there | 3 |
| D2.His.14.6-8 | Build a chain of at least three links from one card, each a cause leading to an effect | the chain strip with linked boxes; the effects panels | 4 |

## Screens and modes
Header (kit): title "Columbian Exchange"; `The exchange`, `Trace your dinner`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The Atlantic across the middle; the Americas on the left, Europe and Africa on the right, Asia peeking in at the far right edge. Twelve picture cards on a dock at the bottom. Three panels along the top: Diets, Populations, Plantations, empty. The welcome is queued (`welcomeAfter: true`): "After 1492, ships crossing the Atlantic carried more than people. They carried plants, animals and germs that changed the whole world. Drag a card to the side where it began." First hint: "Drag the potato to where it began."

**Sort (focus: the dock and both coasts).** At 1366x768 the map fills the middle with panels above; at 680x425 panels are tabs.
- Home of each card: from the Americas: potato (the Andes), maize (Mexico), tomato, cacao, chili pepper. From Afro-Eurasia: horse, cattle, wheat, sugarcane (first grown in New Guinea, spread through Asia), smallpox, measles, malaria.
- A wrong side plays a hint: "Horses lived in the Americas long ago, but they died out there about 10,000 years ago. Europeans brought them back."

**Send (D2.Geo.7.6-8).** The child drags a card onto a ship; the route draws across the ocean and the card spreads on the far side, with a short fact and a source:
- Potato to Europe: a cheap, filling crop for cold, wet soil; economists estimate potatoes explain about a quarter of the growth in Old World population and cities from 1700 to 1900.
- Maize to Africa: by the 1700s a main crop in West and Central Africa.
- Chili peppers to Asia: within a century in Indian and Chinese cooking.
- Horse and cattle to the Americas: Plains nations later built a new way of life on horseback; cattle ranching spread.
- Smallpox and measles to the Americas: Indigenous peoples had no immunity; across the Americas, populations fell by most of their numbers in the century after 1492. Historians' estimates vary widely, and the panel shows the range and says why.
- Malaria and yellow fever to the Americas, with enslaved people and on ships.
- Sugarcane to the Caribbean and Brazil: see the land question.

**Land questions (D2.Geo.11.6-8).** Some cards ask where the crop could grow: sugarcane needs hot, wet land and many hands (the tropical band lights: Brazil, the Caribbean); the potato grows in cool soil (northern Europe lights); wheat needs a temperate climate (the later wheat lands of North America and Argentina light).

**The panels.**
- Diets: foods that crossed appear on plates on each side.
- Populations: a range bar for the Americas (falling by most of its people) and growing populations in Europe, Africa and Asia, labeled as estimates.
- Plantations: sugar plantations appear; a plain card: "Plantation owners forced enslaved Africans to do the work. About 12.5 million Africans were put on slave ships to the Americas; about 10.7 million survived the crossing. Most were sent to grow sugar in Brazil and the Caribbean." No images of violence.

**The chain (the aha).** The child picks one card and builds a chain of at least three linked boxes from tiles (each box a cause leading to an effect), with a "because" line on each link. Example chains: sugarcane, then hot, wet land in Brazil and the Caribbean, then plantations, then the forced transport of enslaved Africans; potato, then more food in northern Europe, then population growth, then growing cities. Narrator: "One crossing, many effects, some good for some people and terrible for others."

**The end.** The map with every card moved, the three panels and the chain. `Print` prints them.

**Trace your dinner (extra).** A meal (pizza, tacos, curry, or a peanut stew) whose ingredients the child sorts by where they began.

## Content
- Twelve cards with home, route, fact and source; three land questions; three panels; chain tiles for six chains; four meals.
- Every fact is real and sourced; ranges are shown where historians disagree.
- Population collapse and slavery are told plainly with care, without images of suffering.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A card can't sail until it is on its home side.
- The chain needs at least three boxes; each link checks against an answer key that accepts several right orders.
- Keyboard: Tab to cards, coasts, ships, panels and chain tiles; Enter to pick up and drop.
- With Motion off ships jump across without sailing.

## Look
- Accent `--brand` #7a4f0e maize and sugar brown (header, ships, panels); gold #f4c542 (the card in hand, a finished link); paper #faf5ec; ink #2a1a03; muted #5f5446.
- Contrast (WCAG 2.1, computed): white on brand 7.11:1; brand on paper 6.55:1; ink on paper 15.50:1; muted on paper 6.80:1; ink on gold 10.35:1.
- Never color alone: each side has a label and its cards carry a home tag; disease cards carry a germ symbol as well as color.
- Different from this batch (atlas indigo, lake jade, purple, red).

## Art
- Public domain botanical and natural history prints for each plant and animal card (Biodiversity Heritage Library and the Met's open-access prints; picked and credited at build).
- Local FLUX (`scripts/localart.py`): the Atlantic map backdrop (1, 16:9); a cargo ship (1, 3:2); four meal plates (4, 1:1).
- People art goes to Gemini with `people: true`: a Plains rider, a European farm family with potatoes, a West African farmer with maize (3; cutout yes); no images of enslaved people suffering, and the plantation card is drawn as a field of cane with a source line.
About 20 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the narrator; `easy-coach` as the card hints. `Curio.voice` with `scope: () => state.mode + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `sort`: "Drag this card to the side where it began."
- how `send`: "Drag the card onto a ship to cross."
- event, whole, each crossing fact.
- how `land`: "Tap where this crop could grow."
- how `chain`: "Pick a card, then build a chain of causes and effects."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the two-coast sort, ship routes, three panels driven by a card table, land bands, the chain builder.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Try both sides | The hint plays on a miss; the teacher view records first tries. |
| Land | Tap everywhere | Each answer must land in the right climate band. |
| Chain | Stack random boxes | Each link checks; a broken link plays "Does this one cause the next?" |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `sort`.
2. `send`; crossing fact (whole), waits.
3. `land`; `chain`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.14.6-8, D2.Geo.7.6-8 and D2.Geo.11.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The term and the main exchanges (crops, animals, diseases) | Crosby, "The Columbian Exchange" (1972) | Nunn and Qian, "The Columbian Exchange: A History of Disease, Food, and Ideas," Journal of Economic Perspectives (2010) | yes |
| Home regions of the twelve cards (potato in the Andes, maize in Mexico, sugarcane from New Guinea, horses died out in the Americas) | Nunn and Qian (2010) | Smithsonian National Museum of Natural History and Britannica entries for each | yes |
| Potatoes explain about a quarter of Old World population growth, 1700 to 1900 | Nunn and Qian, "The Potato's Contribution to Population and Urbanization," Quarterly Journal of Economics (2011) | Nunn and Qian (2010) summary | yes |
| Indigenous populations fell by most of their numbers after 1492, with estimates that vary widely | Nunn and Qian (2010) | Koch et al., "Earth system impacts of the European arrival and Great Dying in the Americas after 1492," Quaternary Science Reviews (2019) | yes, as a range |
| About 12.5 million Africans embarked and about 10.7 million survived; most to Brazil and the Caribbean | SlaveVoyages, Trans-Atlantic Slave Trade Database (estimates) | Smithsonian National Museum of African American History and Culture | yes |
| Sugar needs hot, wet land; the potato cool soil | Britannica, "Sugarcane" | International Potato Center, "Potato facts" | yes |
| Maize spread in Africa and chilies in Asia | Nunn and Qian (2010) | McCann, "Maize and Grace" (Harvard University Press, 2005) | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: the collapse of Indigenous populations and the slave trade are named plainly with sources and ranges, without images of suffering; the effects panels avoid calling the exchange good or bad and show who gained and who suffered. A fresh-agent read of the panels and chain tiles is needed before build.

Checks run (Python, scratchpad r12, 2026-11-09): twelve cards, five from the Americas and seven from Afro-Eurasia, each with one home; 12.5 million minus 10.7 million is 1.8 million who died at sea, about 14 percent; every chain key has at least three links; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and panels; at 680x425 tabs.
2. Each card sorts and sails, with its route and fact. (D2.Geo.7.6-8)
3. Land questions light the right bands. (D2.Geo.11.6-8)
4. The chain of three or more links checks and prints. (D2.His.14.6-8)
5. The panels show ranges where estimates vary.
6. Trace your dinner sorts a meal.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sailing; no network requests.

## Open questions
- Sensitivity flag: population collapse and the slave trade are told plainly (default used: sourced facts and ranges, no images of suffering, fresh-agent read before build).
