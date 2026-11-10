# Mongol Messenger

## One idea
The child is a rider of the yam, the Mongol Empire's relay of horse stations, carrying an urgent message from Karakorum across the steppe to a governor far to the west; at each station they act fast and right (show the paiza, the metal pass that orders the station to help; pick a rested horse; read the route sign), and mistakes cost time, while a ghost rider takes the same trip the old way, with one horse, no stations and unsafe roads; after the race the same roads light up carrying merchants, missionaries and ideas (paper money, printing and gunpowder knowledge, foods, travelers like Marco Polo), and a sort board separates what the empire changed (speed, safe roads, connection across Asia) from what stayed local (rulers who paid tribute but kept their thrones, languages, religions), so a seventh grader learns to classify change and continuity and how communication technology changed connections and the spread of ideas.

## Not like
- why-the-pony-express-ended (5, spec): a mystery about another relay. Here riding the relay itself.
- silk-road-traders (6, spec): an earlier era, card trading. Here the Mongol roads that made trade safer.
- historians-disagree (7, spec): the same empire through two historians' arguments. Here a race and a sort.
- constantinople-defense (7, spec): change across centuries in one city. Here change across one empire.

## Who and how
- Grade 7, Social Studies (History and Geography), module "Medieval Asia". Standards: D2.His.2.6-8 (classify series of historical events and developments as examples of change and/or continuity), D2.Geo.7.6-8 (explain how changes in transportation and communication technology influence the spatial connections among human settlements and affect the diffusion of ideas and cultural practices).
- Format: race. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- The race (ten stages), the roads overlay, the sort board. Extra: Beat your best (the ghost is the child's own best time). tool.json `modes: ["The race", "Beat your best"]`, `minutes: "20-30"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.7.6-8 | Ride ten stages through stations, then compare days taken with the ghost's old way | the two riders' day counters; the route map with stations | 2 |
| D2.Geo.7.6-8 (ideas) | Tap each traveler and idea moving on the roads overlay | the overlay with paths for goods, people and ideas | 3 |
| D2.His.2.6-8 | Sort eight cards into Changed or Stayed the same | the sort board with reasons | 4 |

## Screens and modes
Header (kit): title "Mongol Messenger"; `The race`, `Beat your best`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The grass steppe at dawn; a station of felt tents and horse lines at Karakorum. A map strip across the top runs west to a distant governor's city with ten stations marked. A paiza hangs at the rider's belt. A day counter reads Day 0, and a faint ghost rider waits beside. The welcome is queued (`welcomeAfter: true`): "An urgent message must cross the empire. You ride the yam, a relay with fresh horses at every station. The ghost rider goes the old way. Tap Ride to set out." First hint: "Tap Ride."

**Stages (focus: the station scene).** At 1366x768 the scene fills the screen with the map strip above; at 680x425 the strip shrinks to a progress bar.
- At each station a quick choice (three seconds of thinking, no penalty for slow tapping beyond the clock in the story): show the paiza to the station keeper (wrong: show a merchant's receipt); pick a rested horse from three (a tired one is lathered and head-down); read the route sign (two forks, one marked for the governor's road). Each right pick moves on; a wrong pick costs a story hour, shown on the counter.
- Station facts on arrival: stations were spaced along main roads, often a day's ride apart for ordinary travel, with horses, food and shelter; local families supplied them as a duty; express riders wore bells so stations could ready a horse.
- The model (made for this game, from historical accounts): a yam express rider covers the 3,000-kilometer route in about 10 to 12 days; the ghost, with one horse and no stations, needs about 60 days.
- Marco Polo's account claimed express riders could cover 250 miles or more in a day; the card says historians think his numbers may be stretched.

**The roads overlay (the aha, D2.Geo.7.6-8).** After the finish, the map widens to all of Asia and Europe. The same roads light up with travelers and ideas: merchants with silk and spices; William of Rubruck, a friar sent from France (1253 to 1255); Marco Polo from Venice; paper money used in Yuan China; knowledge of printing and gunpowder moving west; foods and medicines; letters between rulers. The child taps each to read its card. Narrator: "The same roads that carried orders carried everything else."

**The sort board (D2.His.2.6-8).** Eight cards to sort: Changed (the speed of messages; safe roads for traders; one empire linking China to Persia; ideas moving across Asia) or Stayed the same (Russian princes kept their thrones but paid tribute; local languages; people's religions, which Mongol rulers generally allowed; farming villages' daily life). Each sort plays a reason line.

**The end.** Both riders' times, the overlay and the sort board. `Print` prints them.

**Beat your best (extra).** The ghost rides the child's own best time.

## Content
- Ten stages, three choice types with right and wrong picks, station facts, the yam model (made for this game), the roads overlay with eight travelers and ideas, eight sort cards with reasons.
- The rider, the message and the model are made up and labeled; the yam, paiza, travelers and ideas are real.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The race clock counts story hours, not real seconds, so slow readers aren't punished; a timed option for real seconds is off by default.
- The overlay cards open in any order; the board opens after four are read.
- Keyboard: Tab to choices, overlay paths and cards; Enter to pick.
- With Motion off the rider jumps between stations and the ghost shows as a marker.

## Look
- Accent `--brand` #4f5d1c steppe olive (header, the route, station flags); gold #f4c542 (the paiza, the right choice); paper #f4f6ec; ink #161c05; muted #555a48.
- Contrast (WCAG 2.1, computed): white on brand 7.20:1; brand on paper 6.60:1; ink on paper 16.00:1; muted on paper 6.54:1; ink on gold 10.74:1.
- Never color alone: the ghost is drawn in outline with a "ghost" label; board columns carry words and icons.
- Different from this batch (lapis blue, desert sienna, heraldic red, studio teal).

## Art
- Public domain (Met Open Access, id checked at build): the Yuan dynasty iron paiza with silver inlay, with credit.
- Local FLUX (`scripts/localart.py`): the steppe at dawn (1, 16:9); a yam station (1, 16:9); mountain pass (1, 16:9); desert edge (1, 16:9).
- People art goes to Gemini with `people: true`: the rider, a station keeper, William of Rubruck, Marco Polo, a merchant (5; cutout yes), dress checked by a fresh agent against period sources.
- Drawn in code: horses to pick, the route sign, the map strip, the overlay, the board.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as the rider's coach and narrator; `firm-captain` as the station keepers. `Curio.voice` with `scope: () => state.mode + ':' + state.stage + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `station`: "Show the paiza, pick a rested horse, then read the sign."
- event, whole, each station fact.
- event, whole, the finish and the ghost's time.
- how `overlay`: "Tap a traveler or idea on the road."
- event, whole, each overlay card.
- how `sort`: "Drag each card to Changed or Stayed the same."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the station choices, the story clock and ghost, the map strip, the roads overlay, the sort board.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Stations | Tap any choice | Wrong picks cost hours and say why; the finish shows the child's mistakes. |
| Overlay | Skip to the board | The board opens after four overlay cards are read. |
| Sort | Put everything in Changed | Each card checks; "local languages" in Changed plays "Did people stop speaking their own language?" |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `station`; station fact (whole), each waits.
2. Finish (whole).
3. `overlay`; overlay cards (whole).
4. `sort`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.2.6-8 and D2.Geo.7.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The yam relay: stations with horses, food and shelter; supplied by local households; organized under Ögedei | Encyclopaedia Britannica, "Mongol Empire: administration" | Morgan, "The Mongols" (Blackwell, 2nd ed. 2007) | yes |
| The paiza as a pass ordering officials to help the bearer | The Met, "Paiza (Passport)," Yuan dynasty | Britannica, "Paiza" or Morgan (2007) | yes |
| Marco Polo's claim of very long express rides; historians caution it may be stretched | Marco Polo, "The Travels," book 2 (Yule-Cordier translation) | Morgan (2007) | yes |
| William of Rubruck's journey, 1253 to 1255 | Britannica, "William of Rubruck" | Jackson, "The Mission of Friar William of Rubruck" (Hakluyt Society, 1990) | yes |
| Paper money in Yuan China; printing and gunpowder knowledge moving west | Britannica, "Yuan dynasty" | Allsen, "Culture and Conquest in Mongol Eurasia" (Cambridge, 2001) | yes |
| Russian princes kept their thrones but paid tribute; religions generally tolerated | Britannica, "Golden Horde" | Morgan (2007) | yes |
Backed twice: 7. Cut: 0.

Sensitivity note: the conquests that built the empire were violent; one card on the overlay says so plainly with a source, without images, so the roads aren't shown as only peaceful. A fresh-agent read of the overlay cards is needed before build.

Checks run (Python, scratchpad r13, 2026-11-09): 3,000 km in 10 to 12 days is 250 to 300 km a day; 3,000 km in 60 days is 50 km a day; four Changed and four Stayed cards; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene with map strip; at 680x425 progress bar.
2. Ten stages run with the story clock and the ghost's time. (D2.Geo.7.6-8)
3. The roads overlay shows travelers and ideas. (D2.Geo.7.6-8)
4. The sort board checks eight cards with reasons. (D2.His.2.6-8)
5. Marco Polo's claim is marked as possibly stretched.
6. Beat your best uses the child's time.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no galloping; no network requests.

## Open questions
- Sensitivity flag: the Mongol conquests were violent (default used: one plain overlay card with a source and no images, fresh-agent read before build).
