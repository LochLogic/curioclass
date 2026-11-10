# Salt and Gold Caravan

## One idea
The child runs a trading house in the 1300s that sends camel caravans from the salt mines of Taghaza, deep in the Sahara, south to Timbuktu and the markets of the Mali Empire, where gold from the fields to the south changes hands; salt is plentiful in the north and scarce in the south, gold the other way round, so the desert itself makes the trade pay, while every barrier (distance, water, guides, tolls at Mali's markets, raiders) eats into the profit; each season the ledger shows cost per load and profit, guides explain how Mali's rulers controlled the gold trade, and an epilogue follows Mansa Musa's pilgrimage to Mecca in 1324, which carried so much gold through Cairo that observers there reported its value falling, so a seventh grader learns how each region's land drives trade, how barriers shape what gets traded, and how this trade tied West Africa to the wider world.

## Not like
- silk-road-traders (6, spec): ideas spreading by card trade. Here running a trading house's ledger.
- cocoa-chain (5, spec): a modern supply chain. Here a medieval one across a desert.
- border-trade-post (6, spec): tariff policy. Here tolls as one barrier among many.
- smoke-and-honey (6, spec): hidden costs in one town. Here the costs of distance.

## Who and how
- Grade 7, Social Studies (History, Economics and Geography), module "Medieval Africa". Standards: D2.His.1.6-8 (analyze connections among events and developments in broader historical contexts), D2.Eco.14.6-8 (explain barriers to trade and how those barriers influence trade among nations), D2.Geo.11.6-8 (explain how the relationship between the environmental characteristics of places and production of goods influences the spatial patterns of world trade).
- Format: tycoon. Driver: one child alone, or two rival houses (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Five trading seasons, the ledger, the barrier board, the epilogue. Extra: Rival houses (two players share the same market prices; salt prices fall when both sell). tool.json `modes: ["Trading house", "Rival houses"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.11.6-8 | Open the land layer and match each place to what it produces (salt at Taghaza, gold to the south, grain on the Niger) | the land map with each place's product; the price gap between north and south | 2 |
| D2.Eco.14.6-8 | Plan each season (camels, guides, wells, route, tolls) and read the ledger's cost per load | the ledger; the barrier board ranking which barrier cost most | 3 |
| D2.His.1.6-8 | Follow the epilogue and place it on a map of Africa, the Mediterranean and Europe | the epilogue map with Mansa Musa's route and the Catalan Atlas | 4 |

## Screens and modes
Header (kit): title "Salt and Gold Caravan"; `Trading house`, `Rival houses`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A ledger book open on a mat, a map from the Saharan salt mines south to the Niger River, and a pen of camels for hire. A purse holds 200 mithqals of gold (a mithqal is a gold coin's weight, about 4.25 grams). The welcome is queued (`welcomeAfter: true`): "Up north in the desert, salt is everywhere. Down south by the Niger, it's scarce, and gold is close by. Can a caravan make the trade pay? Tap the land map to see what each place makes." First hint: "Tap Land on the map."

**The land (focus: the map, D2.Geo.11.6-8).** At 1366x768 the map fills the left with the ledger right; at 680x425 they're tabs.
- Taghaza: a salt mine in the desert, where even houses were built of salt blocks; no food grows, so food is brought in.
- Walata and Timbuktu: desert-edge market towns.
- The Niger River valley: grain, fish, and markets of the Mali Empire.
- The gold fields far to the south and west: gold mined by local peoples and traded north through Mali's markets.
- Price card (from a traveler's account): in the 1350s a camel load of salt sold for about 8 to 10 mithqals at Walata and 20 to 30, sometimes 40, in the city of Mali.

**Seasons (focus: the planner and ledger, D2.Eco.14.6-8).** The child plans five seasons:
- Buy salt slabs at Taghaza (a camel carries two slabs).
- Hire camels and guides (a guide knows the wells; without one, a caravan can get lost).
- Pick a route: the shorter route with fewer wells or the longer route with more.
- Pay tolls at Mali's markets.
- Then the season runs on the map: days crossing, wells reached, a sandstorm or a raid card, and the arrival.
- The ledger shows cost per load (camels, guides, water, food, tolls, losses) against the price at market, and profit.
- The model (made for this game, built from the traveler's prices): a load bought for about 2 mithqals at the mine, sold for 20 to 30 at Mali; costs and losses take most of the gap; a trip without a guide or with too few wells can lose everything.
- Guide cards: Mali's rulers controlled the gold trade and taxed goods coming in and out; Timbuktu grew as a center of trade and learning.

**The barrier board (the aha).** After five seasons, the child ranks the barriers by what they cost (distance and time, water, losses to storms and raids, tolls, guides) and writes one line: "Salt and gold were worth crossing the desert for because ___, even though ___." Narrator: "The desert was the barrier, and it was also the reason. Different land makes different things."

**The plain note.** A card says caravans also carried enslaved people north across the Sahara, a cruel part of this trade for centuries, named plainly with a source; no images.

**The epilogue (D2.His.1.6-8).** In 1324 Mansa Musa, ruler of Mali, traveled to Mecca on pilgrimage with a huge caravan and so much gold that, a writer in Cairo reported years later, gold's value there fell. The child traces his route on a map, then sees the Catalan Atlas of 1375, made in Majorca, showing Mansa Musa holding a gold nugget: Europe knew of Mali's gold. Narrator: "A salt trade in the desert reached all the way to European maps."

**The end.** The ledger, the barrier board, the line and the epilogue map. `Print` prints them.

**Rival houses (extra).** Two players; when both sell lots of salt in one season, the price falls.

## Content
- Five places with products, a price card, a season model (made for this game), event cards (sandstorm, raid, well dry, good market), guide cards, the barrier board, the plain note, the epilogue with the Catalan Atlas.
- The trading house and the model are made up and labeled; places, prices from the traveler's account, Mali, Mansa Musa and the atlas are real.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The planner won't start a season until camels, salt and a route are chosen; a missing guide is allowed and named as a risk.
- Event cards draw from a fixed shuffled deck so a class sees the same mix.
- Keyboard: Tab to the planner, map, ledger and board; arrows change amounts; Enter to run.
- With Motion off the caravan jumps from stop to stop.

## Look
- Accent `--brand` #8a4b14 desert sienna (header, the ledger, the route); gold #f4c542 (gold, profit, the chosen barrier); paper #fbf4ec; ink #2d1804; muted #625245.
- Contrast (WCAG 2.1, computed): white on brand 6.78:1; brand on paper 6.22:1; ink on paper 15.48:1; muted on paper 6.85:1; ink on gold 10.38:1.
- Never color alone: profit and loss carry plus and minus signs and words; routes are solid or dashed with labels.
- Different from this batch (lapis blue, steppe olive, heraldic red, studio teal).

## Art
- Public domain: the Catalan Atlas detail of Mansa Musa (Bibliothèque nationale de France, Gallica), with credit.
- Local FLUX (`scripts/localart.py`): the salt mine at Taghaza (1, 16:9); a camel caravan in the dunes (1, 16:9); a well (1, 3:2); Timbuktu's market and the Djinguereber Mosque (1, 16:9); salt slabs on camels (1, 3:2).
- People art goes to Gemini with `people: true`: the trading house's partner, a desert guide, a Mali market official (3; cutout yes), dress checked by a fresh agent against period sources.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `upbeat-guide` as the desert guide and narrator; `friendly-dad` as the trading partner reading the ledger. `Curio.voice` with `scope: () => state.mode + ':' + state.season + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each place card.
- how `plan`: "Pick camels, salt and a route, then tap Set out."
- event, whole, each event card.
- event, whole, the ledger summary.
- how `board`: "Rank the barriers by what they cost."
- event, whole, the plain note.
- event, whole, the epilogue.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the land map, the season planner and model, event deck, the ledger, the barrier board, the epilogue map.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Seasons | Hire the most camels every time | Costs rise faster than sales when the market is full; the ledger shows the loss. |
| No guide | Skip the guide to save money | A lost-caravan card can wipe out the season, and the ledger names why. |
| Board | Rank in any order | The ranking checks against the child's own ledger totals. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Place cards (whole), each waits.
2. `plan`; events (whole); ledger summary (whole).
3. `board`; plain note (whole).
4. Epilogue (whole); `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1.6-8, D2.Eco.14.6-8 and D2.Geo.11.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Taghaza's salt mines, houses of salt blocks, food brought in | Ibn Battuta, "Travels" (Gibb translation, 1929) | Encyclopaedia Britannica, "Taghaza" | yes |
| Salt load prices at Walata and Mali in the 1350s | Ibn Battuta (Gibb, 1929) | Levtzion and Hopkins, "Corpus of Early Arabic Sources for West African History" (Cambridge, 1981) | yes |
| Mali's rulers controlled and taxed the gold trade; gold from fields to the south | Britannica, "Mali Empire" | The Met, Heilbrunn Timeline, "The Empires of the Western Sudan: Mali Empire" | yes |
| Mansa Musa's 1324 pilgrimage; gold's value in Cairo reported falling | al-Umari, as given in Levtzion and Hopkins (1981) | Britannica, "Musa I of Mali" | yes |
| The Catalan Atlas of 1375 shows Mansa Musa with gold | Bibliothèque nationale de France, "Atlas catalan" | The Met, Heilbrunn Timeline, "The Catalan Atlas" | yes |
| The trans-Saharan trade also carried enslaved people north | Britannica, "Trans-Saharan trade" | Austen, "Trans-Saharan Africa in World History" (Oxford, 2010) | yes |
| A mithqal is about 4.25 grams of gold | Britannica, "Mithqal" | Levtzion and Hopkins (1981), glossary | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: the slave trade across the Sahara is named plainly in its own card with a source and no images; Mali and Timbuktu are shown as powerful, wealthy and learned. A fresh-agent read of the plain note and people art is needed before build.

Checks run (Python, scratchpad r13, 2026-11-09): a load bought near 2 mithqals and sold at 20 to 30 leaves a gap of 18 to 28 before costs; the model's no-guide, short-route season can lose the whole purse; five seasons from 200 mithqals with sensible plans end in profit; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and ledger; at 680x425 tabs.
2. The land layer matches places and products with the price card. (D2.Geo.11.6-8)
3. Five seasons run with costs per load and profit; the barrier board ranks barriers. (D2.Eco.14.6-8)
4. The epilogue maps Mansa Musa's route and the Catalan Atlas. (D2.His.1.6-8)
5. The plain note about enslaved people shows with its source.
6. Rival houses share prices.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no moving caravan; no network requests.

## Open questions
- Sensitivity flag: the trans-Saharan slave trade (default used: one plain card with a source, no images, Mali shown in its strength, fresh-agent read before build).
