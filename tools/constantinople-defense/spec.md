# Constantinople Defense

## One idea
The child guards Constantinople through four real sieges across eight centuries (626, 717 to 718, 1204, 1453), splitting each era's treasury among the land walls, the fleet and Greek fire, gold for diplomacy and allies, and trade; each siege plays out on a map, not as a battle, and then the real story shows what happened; lost lands and trade shrink the next era's treasury; a board fills with what changed (enemies, weapons, allies, the size of the empire) and what lasted (the walls, Roman law, the Church, the harbor), and at the end a causes web for 1453 (cannons, the sack of 1204, lost land and trade, a small population, too few allies) asks the child to rank and explain the causes, so a seventh grader learns to classify change and continuity and to explain many causes of a long survival and a fall.

## Not like
- rome-republic-to-empire (6, spec): the Republic's fall as a story. Here the eastern empire's long survival.
- house-of-wisdom (7, concept): knowledge kept and passed on. Here walls, gold and allies.
- mongol-messenger (7, concept): a relay race across an empire. Here one city over eight centuries.
- smoke-and-honey (6, spec): spending choices in one year. Here spending across four eras.

## Who and how
- Grade 7, Social Studies (History), module "Fall of Rome and the Byzantine Empire". Standards: D2.His.2.6-8 (classify series of historical events and developments as examples of change and/or continuity), D2.His.14.6-8 (explain multiple causes and effects of events and developments in the past).
- Format: simulator. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Four eras, the change and continuity board, the causes web. Extra: Venice's view (the 1204 siege from the Venetian side, with its trade reasons). tool.json `modes: ["Four sieges", "Venice's view"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.2.6-8 | After each era, drag that era's facts onto Changed or Lasted | the board with four era columns filling | 2 |
| D2.His.14.6-8 (survival) | Split the treasury and read why the city held in 626 and 717 | the budget bars and the real-story card naming several causes | 3 |
| D2.His.14.6-8 (fall) | Rank five causes of 1453 and write a because line for the top two | the causes web with arrows between causes | 4 |

## Screens and modes
Header (kit): title "Constantinople Defense"; `Four sieges`, `Venice's view`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The city on its peninsula: the sea on two sides, the Golden Horn harbor to the north with its great chain, and the triple land walls across the west. A treasury chest of 100 gold pieces. Four budget jars: Walls, Fleet and Greek fire, Diplomacy and allies, Trade. An era card face down. The welcome is queued (`welcomeAfter: true`): "For more than a thousand years, Constantinople was the capital of the eastern Roman Empire. Enemies came again and again. Tap the era card to see who comes first." First hint: "Tap the era card."

**Eras (focus: the map and the jars).** At 1366x768 the map fills the center, jars on the left and the era card on the right; at 680x425 jars become a strip.
1. 626: Avars and Slavs by land, a Persian army across the strait, while Emperor Heraclius fights far away in Persia. Real story: the walls held, the fleet sank the Slavic boats, and the Persians couldn't cross.
2. 717 to 718: a huge Arab army and fleet. Real story: Greek fire (a liquid fire sprayed from ships, first used about 672) burned the fleet, a harsh winter and hunger struck the besiegers, and Bulgar allies attacked them; Emperor Leo III held the city.
3. 1204: the Fourth Crusade, Western Christian knights carried by a Venetian fleet, turned against the city in a quarrel over the throne and debts. Real story: they broke in from the harbor walls and sacked the city, taking its treasures (the horses of Saint Mark's in Venice among them); the empire was split until 1261.
4. 1453: Sultan Mehmed II and a large Ottoman army with huge new cannons. Real story: the cannons broke the walls in places; the Ottomans dragged ships overland into the Golden Horn around the chain; after nearly two months, on May 29, the city fell; Emperor Constantine XI died in the fighting.
- The child splits the gold, taps `Hold the city`, and watches the map (attacks shown as arrows and tokens, no combat scenes). The result says which jars mattered, then the real story card.
- The model (made for this game): each era's treasury depends on lands and trade (100, 90, 60, then 25 gold), so by 1453 even a perfect split can't hold. The child learns that the last era can't be won.

**The board (D2.His.2.6-8).** After each era the child drags its facts onto Changed or Lasted: enemies (changed: Avars and Persians, Arabs, Crusaders, Ottomans); weapons (changed: Greek fire, then cannons); the size of the empire (changed: shrinking); the land walls (lasted, built in the 400s); Roman law (lasted); the Orthodox Church and Hagia Sophia (lasted, until 1453 when it became a mosque); the harbor and trade (lasted, but weakened after 1204).

**The causes web (the aha).** Five cause cards for 1453: huge cannons; the sack of 1204, which left the city poorer and weaker; lost lands and trade; a small population (perhaps 50,000, against a few hundred thousand at its height) and few defenders; too few allies from the West. The child ranks them, draws arrows where one led to another (1204 led to lost trade, lost trade to a small treasury), and writes because lines for the top two. Narrator: "It wasn't just the cannons. The city had been growing weaker for two hundred years."

**The end.** The board, the web, the four budgets. `Print` prints them.

**Venice's view (extra).** The 1204 story told from a Venetian merchant's side: debts owed for the fleet, trade rivals, and an offer from a prince wanting the throne.

## Content
- Four era cards with real stories, a budget model (made for this game), board facts, five causes and the web, the Venice card.
- The model and its numbers are made up and labeled; every siege, date and fact is real.
- War and religious conflict are shown without gore, with care for all sides; each side's reasons are named.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Gold moves in steps of 5; the chest must be empty before `Hold the city` works.
- The web accepts any ranking with because lines for the top two; arrows check against a list of real links.
- Keyboard: Tab to jars, the button, board facts and causes; arrows change amounts; Enter to place.
- With Motion off attack arrows appear without moving.

## Look
- Accent `--brand` #5b2a6e imperial purple (header, jars, the walls); gold #f4c542 (gold pieces, the chosen cause); paper #f6f1f8; ink #1d0c24; muted #5d5363.
- Contrast (WCAG 2.1, computed): white on brand 10.49:1; brand on paper 9.42:1; ink on paper 16.68:1; muted on paper 6.54:1; ink on gold 11.42:1.
- Never color alone: Changed and Lasted columns carry words and symbols; attacking forces carry labels, not just colors.
- Different from this batch (atlas indigo, Atlantic ochre, lake jade, red).

## Art
- Public domain (Met Open Access, ids checked at build): a gold solidus of Heraclius; a solidus of Leo III; a Byzantine icon or object; each with credit. The horses of Saint Mark's (Wikimedia Commons public domain photo, checked at build).
- Local FLUX (`scripts/localart.py`): the city on its peninsula from above (1, 16:9); the land walls (1, 3:2); a ship with Greek fire siphon, no people burning (1, 3:2); ships dragged overland (1, 3:2).
- People art goes to Gemini with `people: true`: Heraclius, Leo III, Constantine XI, Mehmed II, a Venetian merchant (5; cutout yes), drawn from coins, mosaics and portraits of the time.
- Drawn in code: the map, jars, arrows, the board, the web.
About 13 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the narrator and real-story cards; `firm-captain` as the city's commander announcing each threat. `Curio.voice` with `scope: () => state.mode + ':' + state.era + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each era threat.
- how `split`: "Drag gold into the jars, then tap Hold the city."
- event, whole, each result and real story.
- how `board`: "Drag each fact to Changed or Lasted."
- how `web`: "Rank the causes, then draw arrows between them."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the city map, the budget model, four eras, the change and continuity board, the causes web.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Budget | Put everything in Walls | 717 to 718 needs the fleet; the result names the missing jar. |
| Board | Put everything in Changed | Each fact checks; the walls in Changed plays "Were these the same walls?" |
| Web | Rank cannons alone and stop | The web needs all five ranked and because lines for the top two. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Era threat (whole), waits.
2. `split`; result and real story (whole), waits.
3. `board`, after each era.
4. `web`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.2.6-8 and D2.His.14.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The siege of 626 by Avars, Slavs and Persians while Heraclius was away | Encyclopaedia Britannica, "Heraclius" | Kaegi, "Heraclius, Emperor of Byzantium" (Cambridge, 2003) | yes |
| The Arab siege of 717 to 718: Greek fire, winter, Bulgar allies, Leo III | Britannica, "Leo III" | World History Encyclopedia, "Siege of Constantinople (717-718)" | yes |
| Greek fire first used about 672 | Britannica, "Greek fire" | World History Encyclopedia, "Greek Fire" | yes |
| The Fourth Crusade sacked the city in 1204; the empire was split until 1261; the horses of Saint Mark's taken to Venice | Britannica, "Fourth Crusade" | The Met, Heilbrunn Timeline, "The Fourth Crusade" | yes |
| 1453: Mehmed II, great cannons, ships dragged overland, the fall on May 29, Constantine XI's death | Britannica, "Fall of Constantinople" | Crowley, "1453" (Hyperion, 2005) | yes |
| The Theodosian land walls built in the 400s | Britannica, "Walls of Constantinople" | UNESCO, "Historic Areas of Istanbul" | yes |
| A small population by 1453 (perhaps 50,000) against a few hundred thousand at its height | Britannica, "Istanbul: history" | Crowley (2005) | yes, as estimates |
| Hagia Sophia made a mosque in 1453 | UNESCO, "Historic Areas of Istanbul" | Britannica, "Hagia Sophia" | yes |
Backed twice: 9. Cut: 0.

Sensitivity note: war and religious conflict (Christian and Muslim, Western and Eastern Christian) are shown as maps and arrows without gore; each side's reasons are named; leaders are drawn from period sources with respect. A fresh-agent read of the era cards is needed before build.

Checks run (Python, scratchpad r12, 2026-11-09): eras in order (626, 717, 1204, 1453); 1453 minus 626 is 827 years, "eight centuries"; treasuries 100, 90, 60, 25 fall each era; no split of 25 gold meets the 1453 need in the model; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map, jars and card; at 680x425 jars are a strip.
2. The board fills across four eras with checked facts. (D2.His.2.6-8)
3. Each era runs the budget and shows the real story with several causes. (D2.His.14.6-8)
4. The 1453 causes web ranks five causes with because lines. (D2.His.14.6-8)
5. The 1453 era can't be held and the narrator says why.
6. Venice's view loads.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no moving arrows; no network requests.

## Open questions
- Sensitivity flag: war and religious conflict across four sieges (default used: maps and arrows with no gore, each side's reasons named, fresh-agent read before build).
