# Silk Road Traders

## One idea
Between about 130 BCE and 200 CE the child runs a trading company on the routes linking Han China, Central Asia and the kingdoms of northern India, moving caravans and ships between six markets to fill orders for silk, horses, spices and cotton cloth; travel cards (Bactrian camels, oasis rest, mountain passes, monsoon winds) change how long each leg takes, some deals carry an idea or skill along with the goods (Buddhist teachings, Buddha images in Gandhara's style, new crops like alfalfa and grapes, the "heavenly horses" of Ferghana), and a map lights each idea's spread faster where travel is easier, so a sixth grader learns that transport shapes how places connect and how ideas spread, and ends by sorting what the trade changed and what it left the same.

## Not like
- salt-and-gold-caravan (concept): one business across one desert. Here a network of routes and the ideas on them.
- mongol-messenger (concept): a later empire's relay riders. Here 130 BCE to 200 CE merchants.
- house-of-wisdom (concept): how knowledge was kept and translated in Baghdad. Here how ideas traveled with trade.
- colonial-trade-routes (5, spec): the Atlantic trade of the 1700s. Here Asia's overland and monsoon routes long before.

## Who and how
- Grade 6, Social Studies (World History and Geography), module "Ancient India and China". Standards: D2.His.2.6-8 (classify series of historical events and developments as examples of change and/or continuity), D2.Geo.7.6-8 (explain how changes in transportation and communication technology influence the spatial connections among human settlements and affect the diffusion of ideas and cultural practices).
- Format: cards. Driver: one child alone, or two players racing (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Three parts: Trade (fill orders over about twelve turns), the Spread map, and the Change or same sort. Extra: Two traders (two players race to fill orders on one map). tool.json `modes: ["Trade", "Two traders"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.7.6-8 | Play travel cards on each leg and choose routes; carry idea cards with goods | each leg's days change with the travel card; the spread map lights ideas faster on easy legs | 2, 3 |
| D2.Geo.7.6-8 (spread) | Compare how far Buddhism spreads by the overland route and the sea route over the same number of turns | the spread map with dated stops | 3 |
| D2.His.2.6-8 | Sort the run's events into Change, Continuity or Both | the sort board with reason lines | 4 |

## Screens and modes
Header (kit): title "Silk Road Traders"; `Trade`, `Two traders`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A route map from Chang'an in the east to Pataliputra on the Ganges in the southwest: six markets (Chang'an, Dunhuang, Kashgar, Taxila in Gandhara, Mathura, Pataliputra) on overland legs, and a sea route from Tamralipti on the Bay of Bengal to Jiaozhi, the Han's southern port. The child's hand: three goods cards (two bolts of silk, a bag of pepper) and three travel cards. An order board shows four orders. The welcome is queued (`welcomeAfter: true`): "You run a trading company two thousand years ago. Fill orders by moving goods between markets. Ideas will travel with your goods. Tap an order to start." First hint: "Tap an order on the board."

**Trade (focus: the map and the hand).** At 1366x768 the map fills the top, the hand and order board below; at 680x425 the map zooms to the current leg and the hand is a drawer.
- Orders (examples): Chang'an wants 2 Ferghana horses (from the market at Kashgar, where Ferghana horse traders come); Taxila wants 3 bolts of silk; Pataliputra wants Chinese silk and lacquer; Chang'an's court wants pepper and cotton cloth from India.
- Each leg has a base number of travel days (game days, rounded from distance at caravan pace): Chang'an to Dunhuang 55; Dunhuang to Kashgar 65; Kashgar to Taxila 45 over the mountain passes; Taxila to Mathura 25; Mathura to Pataliputra 30 by river boat; sea from Tamralipti to Jiaozhi 60 with the monsoon, or wait for the wind to turn.
- Travel cards:
  - Bactrian camels: desert legs (Dunhuang to Kashgar) take 15 fewer days and carry twice the goods.
  - Oasis rest: a stop at Dunhuang or Kashgar refreshes animals; the next leg doesn't lose goods to the desert.
  - Mountain passes: Kashgar to Taxila; without porters and yaks the leg takes 20 more days and one good may be lost.
  - Monsoon winds: the sea leg is fast only in its season; sailing out of season means waiting about four months for the wind to turn.
- Idea cards ride with some deals (the trader in Taxila gives a monk passage; a Ferghana horse trader brings alfalfa seed). Carrying an idea to a market lights it there with a date.

**The spread map (focus: the ideas).** After the trading turns, the map plays each idea's spread with real dates, sped up on legs where the child used camels or the monsoon and slowed on passes:
- Buddhist teachings: from Gandhara through the Kushan lands to Kashgar and Dunhuang; Buddhism reaches the Han court by the 1st century CE (the story of the White Horse Temple in Luoyang, 68 CE); the Parthian monk An Shigao is translating texts in Luoyang by about 148 CE.
- Buddha images in Gandhara's style (the Buddha shown as a person, with Greek-influenced robes) spread east along the same road.
- Alfalfa and grapes: brought to the Han from Ferghana after Zhang Qian's journeys (138 to 126 BCE).
- Heavenly horses: the Han fought for Ferghana's horses (104 to 101 BCE) to strengthen their cavalry.
- Silk and cotton cloth: Chinese silk flows west; Indian cotton cloth flows east and across the sea.
- A side-by-side shows the same number of turns on the overland road and the monsoon sea route: the ship carries more, faster, but only in season.

**Change or same (the aha).** A sort board with three columns (Change, Continuity, Both). Cards: Buddhism reaches China (Change); new crops in Han fields (Change); Buddha images in a new style (Change); the Han dynasty keeps ruling (Continuity, 206 BCE to 220 CE); Confucian learning stays at the center of Han government (Continuity; the Imperial Academy founded 124 BCE); most people in both lands keep farming villages much as before (Continuity); Chinese emperors' cavalry gets bigger horses (Change); Buddhism changes as it meets Chinese ideas (Both). Each card asks for a reason tile. Narrator: "Trade carried new things and new ideas, but most of daily life stayed the same for a long time."

**The end.** The map with the child's routes and lit ideas, and the sort board. `Print` prints both.

**Two traders (extra).** Two hands, one map; the first to fill three orders wins; the spread map plays for both.

## Content
- Six markets and one sea route with base days, four travel cards, about twelve goods cards, eight orders, five idea cards with real dates, eight sort cards.
- Leg days, orders and the trading company are made for this game and labeled; the markets, goods, ideas and dates are real.
- Belief systems are described by what people did and taught, with dates, and never ranked.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A turn: pick a leg, play travel cards (optional), move; trade on arrival.
- The spread map can be replayed and paused; each lit stop opens its date card.
- Keyboard: Tab to markets, cards and orders; Enter to play or move; arrows choose a leg.
- With Motion off caravans jump between markets and the spread lights stop by stop without animation.

## Look
- Accent `--brand` #7b2d5b mulberry, for silk (header, routes, order cards); gold #f4c542 (the active caravan, a lit idea); paper #f9f1f5; ink #2a0d1e; muted #5f4f58.
- Contrast (WCAG 2.1, computed): white on brand 8.87:1; brand on paper 7.99:1; ink on paper 16.11:1; muted on paper 6.89:1; ink on gold 10.99:1.
- Never color alone: overland legs are solid, sea legs dashed; ideas carry icons (a wheel for Buddhist teachings, a leaf for crops, a horse, a bolt of cloth).
- Different from this batch (agora blue, Rome crimson, border olive, farmer ochre).

## Art
- Public domain (Met Open Access, ids checked at build for the open-access flag): a Gandharan standing Buddha (Kushan period, 2nd to 3rd century CE); a Han dynasty bronze horse or a Han pottery horse; a Han silk fragment or lacquer piece. Each with credit.
- Local FLUX (`scripts/localart.py`): the route map base (1, 16:9); six market scenes (6, 3:2: Chang'an gate, Dunhuang oasis, Kashgar bazaar, Taxila, Mathura, Pataliputra on the Ganges); a monsoon ship at Tamralipti (1).
- People art goes to Gemini with `people: true`: the trader, a monk traveling with a caravan, a Ferghana horse trader (1 each; cutout yes).
- Drawn in code: cards, legs, the spread map overlay, the sort board.
About 14 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as the narrator and card reader; `casual-peer` as the company's young partner, Bao (made for this game), who reads orders. `Curio.voice` with `scope: () => state.mode + ':' + state.turn + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `order`: "Tap an order, then pick a leg to move."
- how `travel`: "Play a travel card, or tap Move."
- event, whole, each arrival and trade.
- event, whole, each idea lit.
- how `spread`: "Tap Play to watch the ideas spread."
- event, whole, each spread date card.
- how `sort`: "Drag each card to Change, Continuity or Both."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
silk-road (no engine doc and no sibling tools; the tag may be unneeded, see Open questions). Tool-only code: the route graph with leg days and travel modifiers, orders and hands, idea carrying, the spread replay and the sort.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Trade | Never play travel cards | Orders still fill, but slowly; the spread map shows ideas lagging, and the narrator names which card would have helped. |
| Sea route | Sail out of season | The ship waits about four months; the leg's days show it. |
| Sort | Put everything in Change | Each card checks; "The Han dynasty keeps ruling" in Change plays "Did that change, or keep going?" |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `order`.
2. `travel`; arrivals (whole); ideas lit (whole).
3. `spread`; date cards (whole), each waits.
4. `sort`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.2.6-8 and D2.Geo.7.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Zhang Qian's journeys (138 to 126 BCE); alfalfa and grapes brought from Ferghana; the war for Ferghana's horses (104 to 101 BCE) | Sima Qian, Shiji chapter 123 (in Burton Watson's translation) | Encyclopaedia Britannica, "Zhang Qian" and "Silk Road" | yes |
| Buddhism reached China by the 1st century CE; the White Horse Temple story; An Shigao translating in Luoyang from about 148 CE | Encyclopaedia Britannica, "Buddhism in China" and "An Shigao" | Asia Society / Met Heilbrunn Timeline, "Buddhism along the Silk Road" | yes |
| Gandharan Buddha images under the Kushans, 1st to 3rd centuries CE | Met Heilbrunn Timeline, "Kushan Empire" and "Gandhara" | Encyclopaedia Britannica, "Gandhara art" | yes |
| Monsoon winds and sea trade around India by the 1st century CE; Han sea contacts to the south | The Periplus of the Erythraean Sea (1st century CE) | Hanshu, treatise on geography (Han voyages from the southern commanderies) | yes |
| Han dynasty 206 BCE to 220 CE; Imperial Academy founded 124 BCE | Encyclopaedia Britannica, "Han dynasty" | Met Heilbrunn Timeline, "Han dynasty" | yes |
| Bactrian camels carry heavy loads across deserts; oasis towns Dunhuang and Kashgar | UNESCO, "Silk Roads Programme" | Encyclopaedia Britannica, "Silk Road" | yes |
Backed twice: 7. Cut: 0.

Sensitivity note: Buddhism is shown as teachings carried by people, with dates and what changed as it met Chinese ideas; no belief is ranked or tested. A fresh-agent read of the idea cards and sort cards is needed before build.

Checks run (Python, scratchpad r10, 2026-11-09): the overland road from Chang'an to Pataliputra is 55 + 65 + 45 + 25 + 30 = 220 base days; camels cut Dunhuang to Kashgar to 50, and a pass without porters makes Kashgar to Taxila 65; Zhang Qian (138 to 126 BCE) comes before the horse war (104 to 101 BCE) and the White Horse story (68 CE); each sort card has one right column; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map, hand and orders fit; at 680x425 the map zooms and the hand is a drawer.
2. Travel cards change each leg's days and the monsoon leg waits out of season. (D2.Geo.7.6-8)
3. The spread map lights ideas with real dates, faster where travel is easier. (D2.Geo.7.6-8)
4. The sort checks Change, Continuity and Both with reasons. (D2.His.2.6-8)
5. Every idea card shows its date and source.
6. Two traders runs two hands on one map.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no moving caravans; no network requests.

## Open questions
- Sensitivity flag: Buddhism's spread is a belief system shown in a game (default used: teachings described by what people did, with dates, no ranking; fresh-agent read before build).
- The family tag silk-road has no engine and no siblings (default used: tool-only code; the tag can be dropped to "none" if Cory agrees).
