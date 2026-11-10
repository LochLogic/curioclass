# Manor Life

## One idea
The child looks after one household on an English manor from 1188 to 1194 (a peasant family who hold a few strips of land, the lord's household in the manor house, or a monk at the nearby Cistercian abbey) through the seasons, making its choices (which strips to plant, whether to pay or bargain, whom to ask for help) while its meters (food, health, standing, faith, coin) respond; big events arrive for everyone (labor days on the lord's land, the church's tithe, the Saladin tithe of 1188 for the Third Crusade, a wet harvest, the great tax of 1193 to 1194 to ransom King Richard from captivity in Germany), and then the child replays one event as a different household and compares what each person owned, owed and believed, so a seventh grader learns how many factors shaped people's perspectives and how one manor connects to crusades, kings and the Church.

## Not like
- panel-of-experts (7, spec): the Black Death through four fields. This tool stays before the plague on purpose.
- hunter-to-farmer (6, spec): the start of farming. Here a medieval farm's duties.
- mill-town (8, concept): factory work. Here a manor's seasons.
- constantinople-defense (7, spec): an empire's treasury against sieges. Here a household's purse against taxes.

## Who and how
- Grade 7, Social Studies (History), module "Medieval Europe". Standards: D2.His.1.6-8 (analyze connections among events and developments in broader historical contexts), D2.His.4.6-8 (analyze multiple factors that influenced the perspectives of people during different historical eras).
- Format: creature. Driver: one child alone, or three students running the three households side by side (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Three households, twelve seasons (1188 to 1194, two seasons a year), five meters, the replay. Extra: Three households (three students each run one household through the same events). tool.json `modes: ["One household", "Three households"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.4.6-8 | Replay one big event as a second household and fill the compare card (owned, owed, believed, felt) | the two households' cards side by side; the meters before and after | 3 |
| D2.His.4.6-8 (choices) | Make each season's choices for the household | the five meters and the reason line for each change | 2 |
| D2.His.1.6-8 | Place each big event on the wider-world strip (the Crusade, the king's capture, the Church) | the strip linking the manor to Jerusalem, Germany and Rome | 4 |

## Screens and modes
Header (kit): title "Manor Life"; `One household`, `Three households`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The manor from above: open fields divided into long strips, a meadow, woodland, the mill, the parish church, the manor house, and the abbey's gray walls across the stream. Three household portraits at the bottom: Agnes and Walter, a peasant couple with three children; Sir Hugh and Lady Matilda in the manor house; Brother Simon at the abbey. The welcome is queued (`welcomeAfter: true`): "It's 1188 on an English manor. Everyone here owes something to someone. Pick a household to look after." First hint: "Tap a household portrait."

**Seasons (focus: the household and its meters).** At 1366x768 the manor fills the left with the household card and meters on the right; at 680x425 meters become a strip.
- Each season (spring and autumn) brings one or two choices:
  - Peasants: which strips to plant (wheat for sale, oats and peas to eat); work the lord's land the required days a week or send a son; pay a fine to marry off a daughter or wait; ask the lord, the priest or neighbors for help in a hard time.
  - Lord: raise rents or keep them; send a knight to the Crusade or pay to stay home; sell wool to Flemish merchants; give to the abbey.
  - Monk: copy books or work in the fields; give alms at the gate; sell the abbey's wool; pray for the king.
- Meters: Food, Health, Standing (respect in the community), Faith, Coin. Each change has a reason line.
- Duties named plainly: peasants worked the lord's land a set number of days each week, more at harvest; one tenth of their crops went to the church as a tithe.

**Big events (for everyone).**
- 1188, the Saladin tithe: King Henry II taxed one tenth of income and movable goods to pay for the Third Crusade (crusaders were excused).
- 1190: King Richard leaves on crusade.
- A wet harvest (made for this game): grain rots in the fields.
- 1193 to 1194, the king's ransom: Richard, captured on his way home and held in Germany, was freed for a ransom of 150,000 marks; England paid with a tax of a quarter of income and goods, while the Cistercian monks gave a year's wool.
- Each event changes all three households differently, and the child sees only their own household's view at first.

**The replay (the aha, D2.His.4.6-8).** After the ransom, the child picks one event and replays it as a second household. A compare card fills: what each owned, what each owed, what each believed, how each felt. Example: the ransom takes a quarter of Agnes and Walter's few goods; Sir Hugh pays more but has more; Brother Simon's abbey gives its wool, and he prays for the king's freedom. Narrator: "Same tax, three different stories. What you owned, owed and believed shaped how you saw it."

**The wider world (D2.His.1.6-8).** A strip shows where each event came from: Jerusalem and the Crusade, Germany and the captive king, Rome and the Church's tithe, Flanders and the wool trade. The child places each event card.

**The end.** The household's meters over twelve seasons, the compare card and the strip. `Print` prints them.

**Three households (extra).** Three students run one household each through the same events, then compare cards together.

## Content
- Three households (made for this game) with seasonal choices, five meters, four big events (three real, one made for this game), the compare card, the wider-world strip.
- The people, the manor and the wet harvest are made up and labeled; the taxes, duties, dates and the ransom are real.
- No plague, battle or cruelty scenes; the Crusade is named with its purpose and cost, not shown as fighting.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each season waits for its choices; meters update with a reason line.
- A meter at zero triggers a help card (neighbors, the abbey's alms, the lord's mercy), not a game over.
- Keyboard: Tab to portraits, choices, meters and cards; Enter to choose.
- With Motion off seasons change without fading.

## Look
- Accent `--brand` #8c1d1d heraldic red (header, the household card, event banners); gold #f4c542 (the chosen option, the ransom coins); paper #fbf1ef; ink #2c0808; muted #62504d.
- Contrast (WCAG 2.1, computed): white on brand 9.10:1; brand on paper 8.20:1; ink on paper 16.53:1; muted on paper 6.82:1; ink on gold 11.27:1.
- Never color alone: meters show a number and an icon; rising and falling carry arrows and words.
- Different from this batch (lapis blue, desert sienna, steppe olive, studio teal).

## Art
- Public domain: farm-life scenes from the Luttrell Psalter (British Library, about 1330, used as later illustrations of the same kind of work and labeled so) and a calendar page of labors of the months, with credit; rights checked at build.
- Local FLUX (`scripts/localart.py`): the manor from above (1, 16:9); the strip fields in spring and autumn (2, 16:9); the abbey (1, 3:2); the manor house hall (1, 3:2).
- People art goes to Gemini with `people: true`: Agnes and Walter with their children, Sir Hugh and Lady Matilda, Brother Simon (3; cutout yes).
- Drawn in code: meters, choice cards, the compare card, the wider-world strip.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the narrator; `warm-teacher` as the household's own voice reading their cards. `Curio.voice` with `scope: () => state.mode + ':' + state.household + ':' + state.season + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `choose`: "Pick what your household does this season."
- event, whole, each season's result.
- event, whole, each big event.
- how `replay`: "Pick an event, then replay it as another household."
- how `compare`: "Fill the compare card: owned, owed, believed, felt."
- how `strip`: "Drag each event to where it came from."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: three households with seasonal choices, five meters, the event timeline, the replay and compare card, the wider-world strip.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Seasons | Pick the same choice every time | Meters fall when the season's need changes; the reason line says why. |
| Replay | Fill the compare card the same for both | Each line checks against the household's real situation. |
| Strip | Drop events anywhere | Each event must land at its source place. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `choose`; result (whole), waits.
2. Big events (whole), each waits.
3. `replay`; `compare`.
4. `strip`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1.6-8 and D2.His.4.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Open fields in strips; peasants owed labor days on the lord's land; fines to marry | Bennett, "Life on the English Manor" (Cambridge, 1937) | Dyer, "Making a Living in the Middle Ages" (Yale, 2002) | yes |
| Tithe of one tenth to the church | Encyclopaedia Britannica, "Tithe" | Dyer (2002) | yes |
| The Saladin tithe of 1188: one tenth of income and movables for the Third Crusade, crusaders excused | Britannica, "Saladin tithe" | The National Archives (UK), "Taxation: the Saladin tithe" | yes |
| Richard I captured on the way home and held in Germany; ransom of 150,000 marks | Britannica, "Richard I" | The National Archives (UK), "Richard I's ransom" | yes |
| England paid with a tax of a quarter of income and goods; the Cistercians gave a year's wool | Gillingham, "Richard I" (Yale, 1999) | Britannica, "Richard I" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r13, 2026-11-09): twelve seasons from spring 1188 to autumn 1193, with the ransom tax in the last two seasons and the 1194 release on the end card; a quarter of the peasant household's goods is a larger share of its food meter than a quarter of the lord's; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 manor and household card; at 680x425 meter strip.
2. Twelve seasons run with choices and reasons. (D2.His.4.6-8)
3. The replay fills the compare card for two households. (D2.His.4.6-8)
4. Events place on the wider-world strip. (D2.His.1.6-8)
5. A meter at zero brings a help card, not a game over.
6. Three households runs three side by side.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no fading; no network requests.

## Open questions
None.
