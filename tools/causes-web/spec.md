# Causes Web

## One idea
The student picks a problem that is both local and global (rising rents, plastic waste, a closed factory), each with a real local case and its global twin, and builds a web of causes from four lens decks (economics, geography, civics, history), where every card carries a data point or a source (zoning rules, interest rates, migration, oil prices, trade, past policy decisions); the student places cards and draws links, and the tool lays the same web out three ways, as a timeline, a cause chain and a feedback loop, flagging gaps (a link with no evidence, an order that breaks the timeline, a lens left out); a challenge step shows people who tried to fix the problem over time and what made it hard; at the end the student writes a short explanation, picks the layout that fits its purpose, and names one strength and one weakness, so a twelfth grader learns to construct explanations with sound reasoning, correct sequence and pertinent data while weighing their strengths and weaknesses, and to use several lenses to understand a problem's causes across places and the challenges of addressing it.

## Not like
- who-decides (12, spec): acting on a local problem. Here explaining one.
- claim-repair-shop (10, spec): fixing others' explanations. Here building one from data.
- alliance-web (9, spec): one historical chain. Here a web with loops across lenses.
- layers-and-scales (9, spec): reading maps at scales. Here causes at scales.

## Who and how
- Grade 12, Social Studies (Inquiry), module "Causes Web". Standards: D4.2.9-12 (construct explanations using sound reasoning, correct sequence, examples, and details with significant and pertinent information and data, while acknowledging the strengths and weaknesses of the explanation given its purpose), D4.6.9-12 (use disciplinary and interdisciplinary lenses to understand the characteristics and causes of local, regional, and global problems; instances of such problems in multiple contexts; and challenges and opportunities faced by those trying to address these problems over time and place).
- Format: builder. Driver: one student alone, or groups each owning a lens and merging webs (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Three problem cases, four lens decks of about eight cards each per case, the three layouts with gap flags, the challenge step, the explanation. Extra: Lens teams (groups each own one lens, then merge into one web). tool.json `modes: ["Build", "Lens teams"]`, `minutes: "35-45"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D4.6.9-12 | Draw cards from all four lenses for the local case and its global twin | the four lens decks; the lens counter; the local and global columns | 2 |
| D4.6.9-12 (challenges) | Read the challenge step and mark what made each attempt hard | the attempts timeline with outcomes | 3 |
| D4.2.9-12 | Link cards, view the three layouts, fix flagged gaps, and write the explanation with a strength and a weakness | the web; the timeline, chain and loop layouts; gap flags; the explanation | 4, 5 |

## Screens and modes
Header (kit): title "Causes Web"; `Build`, `Lens teams`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Three problem cards on a corkboard:
- Rents: renters in one real U.S. city (Boise, Idaho, which saw some of the fastest rent growth in the country from 2020 to 2022) and the global twin (housing costs in cities worldwide).
- Plastic: one real U.S. county's recycling program and the global twin (in 2019 the world produced about 353 million tonnes of plastic waste and recycled about 9 percent).
- A closed factory: General Motors' Janesville, Wisconsin assembly plant, which closed in December 2008 after more than 85 years, and the global twin (manufacturing moving between countries).
The welcome is queued (`welcomeAfter: true`): "Big problems have more than one cause. Pick one, and build the web that explains it. Tap a problem card." First hint: "Tap a problem card."

**Building (focus: the web).** At 1366x768 the web fills the left with the lens decks right; at 680x425 the decks are a sheet. The student draws cards from four lenses (economics, geography, civics, history), each with one data point and its source, places them in the local or global column, and draws links with a short "because" label. A lens counter shows which lenses are used.
- Rents example cards: mortgage rates from 2020 to 2023; people moving in during remote work; local zoning and housing permits; wages; past decisions on land use.
- Plastic example cards: oil and gas prices that make new plastic cheap; China's 2018 ban on importing most plastic scrap; local recycling rules; packaging trends.
- Factory example cards: the 2008 recession and falling vehicle sales; GM's bankruptcy (2009); trade and plant location decisions; the town's history around one employer.

**Three layouts (D4.2.9-12).** A switch lays the same web out as a timeline (cards by date), a cause chain (arrows in one direction) and a feedback loop (cycles). Gap flags appear: a link with no evidence, a cause dated after its effect, a lens with no card, a loop that the chain view hides. The student fixes each flag or writes why it stays.

**The challenge step (D4.6.9-12).** For each case a short timeline of real attempts to fix it (a rent rule or a housing bond; a bottle deposit law or a plastic bag ban; retraining programs and a search for a new plant), with what helped and what made it hard. The student marks one challenge and one opportunity.

**The explanation (the aha).** The student picks the layout that fits the purpose (to show order, to show the strongest push, to show a cycle) and writes: "The main causes are ___, linked by ___. I chose the ___ layout because ___. A strength of this explanation is ___. A weakness is ___." Narrator: "An explanation is a choice about what to show. A good one says what it leaves out."

**The end.** The web in the chosen layout, the fixed flags, the challenge marks and the explanation. `Print` prints them.

**Lens teams (extra).** Groups each own one lens, then merge their cards into one web; the tool flags duplicate and conflicting links.

## Content
- Three real cases with about thirty-two sourced cards each, the three layout views with gap rules, a challenge timeline per case, the explanation template.
- Every data point names its source and year; cases are checked against current data at build.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A link needs a "because" label; the layouts open after at least six cards from three lenses are linked.
- Keyboard: Tab to decks, cards, links and the layout switch; Enter to place; L starts a link from the focused card.
- With Motion off layouts switch without animating.

## Look
- Accent `--brand` #00627a web teal (header, links, the layout switch); gold #f4c542 (the card in hand, a fixed flag); paper #eef6f8; ink #06202a; muted #4e5a5e.
- Contrast (WCAG 2.1, computed): white on brand 6.94:1; brand on paper 6.33:1; ink on paper 15.37:1; muted on paper 6.50:1; ink on gold 10.35:1.
- Never color alone: lenses carry names and icons; flags carry words.
- Different from this batch (Senate rust, olive drab, brain magenta, civic blue).

## Art
- Local FLUX (`scripts/localart.py`): a street of rentals (1, 16:9), a recycling yard (1, 16:9), an empty assembly plant (1, 16:9).
- Drawn in code: the web, the three layouts, the cards.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `easy-coach` as the builder's guide and hints; `knowing-guide` as the reader of cards and attempts. `Curio.voice` with `scope: () => state.mode + ':' + state.case + ':' + state.layout + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each card.
- how `link`: "Draw a link and say because."
- how `layout`: "Switch the layout and fix the flags."
- event, whole, each attempt.
- how `challenge`: "Mark one challenge and one opportunity."
- how `explain`: "Write your explanation with a strength and a weakness."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the card web, the three layouts, gap rules, the challenge timeline, the explanation. Card data sits in a marked block `/* CAUSES-WEB DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Lenses | Use one lens for every card | The layouts stay closed until three lenses are linked. |
| Links | Link everything to everything | Each link needs a because label and is flagged if the dates don't fit. |
| Explanation | Skip the weakness | It needs a named strength and weakness. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Card (whole), waits; `link`.
2. `layout`.
3. Attempt (whole); `challenge`.
4. `explain`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D4.2.9-12 and D4.6.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Boise rent growth, 2020 to 2022 | U.S. Census Bureau, American Community Survey | Joint Center for Housing Studies of Harvard University, "America's Rental Housing" (2024) | yes |
| Mortgage rates, 2020 to 2023 | Freddie Mac, Primary Mortgage Market Survey | Federal Reserve Bank of St. Louis, FRED (MORTGAGE30US) | yes |
| About 353 million tonnes of plastic waste in 2019, about 9 percent recycled | OECD, "Global Plastics Outlook" (2022) | UN Environment Programme | yes |
| China's 2018 ban on most plastic scrap imports | Brooks, Wang and Jambeck, Science Advances (2018) | U.S. EPA, international recycling notes | yes |
| GM Janesville closed December 2008; GM bankruptcy 2009 | Goldstein, "Janesville" (Simon and Schuster, 2017) | U.S. Department of the Treasury, auto industry program reports | yes |
| Bottle deposit and bag-ban outcomes | U.S. EPA, "Advancing Sustainable Materials Management" | Container Recycling Institute | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r21, 2026-11-09): three cases with four lenses of eight cards each is 96 cards; the layouts open at six linked cards from three lenses; 9 percent of 353 million tonnes is about 32 million tonnes recycled; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 web and decks; at 680x425 sheet.
2. Cards from all four lenses are placed for local and global. (D4.6.9-12)
3. The challenge step marks a challenge and an opportunity. (D4.6.9-12)
4. Three layouts show the same web and flag gaps that the student fixes or explains. (D4.2.9-12)
5. The explanation names its layout, a strength and a weakness. (D4.2.9-12)
6. Every card names its source and year.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no layout animation; no network requests.

## Open questions
- The idea card flags a data source (default used: three real cases, Boise rents, one U.S. county's recycling program chosen at build, and GM Janesville, each checked against current data before build).
