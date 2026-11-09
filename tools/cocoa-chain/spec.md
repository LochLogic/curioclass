# Cocoa Chain

## One idea
Pull the red thread on a chocolate bar in a store here back to a cocoa farm in Ghana, then bring the real 2023 rains
and watch one storm reach every stop on the chain, from the farm family's bags to the price on our shelf, in dated
numbers.

Note for the builder: the idea card said "drought". The real 2023-24 harvest failure came from very heavy rain that
spread black pod disease (after a hot, dry 2022), with an old tree virus and illegal mining making it worse (Sources).
The tool shows the real event and calls it "the 2023 rains". It is still a natural disaster in one place that changes
lives far away (D2.Geo.12.3-5).

## Not like
- where-s-my-phone-from (grade 10 data desk): many parts, flow maps and tables. Here one product, one thread, six
  painted stops and one event, at grade 5.
- colonial-trade-routes (grade 5 map): 1700s cargoes on a period map. Here a modern chain and a before/after switch.
- barter-bay (grade 4 simulator): money and shocks inside one made-up town. Here real countries and dated numbers.
- border-trade-post (grade 6): two made-up countries and a tariff. Here no policy lever: nature moves the chain.
- the-shrinking-lake (grade 6 timeline): sixty years of slow change in one place. Here one event, far-off effects.
- state-economy-map (grade 4 map): layers of one state's economy. Here a single thread across three countries.

## Who and how
- Grade 5 social studies (Geography module social-studies-5-cocoa-chain). Driver: students (solo by default); a
  teacher can project it. 25 to 35 minutes.
- Standards: D2.Eco.14.3-5, D2.Eco.15.3-5, D2.Geo.12.3-5, D4.2.3-5.
- tool.json: driver "students or teacher", minutes "25-35", modes ["Follow the bar", "Explain it"], grades_label
  "Grades 4-6".
- Content note (tool page and notes.md, BASELINE rule 8): the farm stop names child labor in cocoa plainly. No prompt
  asks students about their own family or feelings, so no disclosure step is needed.

## Standards map
| Code | Student action | What they see | Done when |
|---|---|---|---|
| D2.Eco.14.3-5 (trade and interdependence among nations) | At each stop, answer the "This stop needs" question by tapping the stop on the map that supplies it (the farm's question is "Where does our money come from in the end?": the Store) | A brown goods arrow and a gold money arrow draw between the two stops; the countries' names light | After six answers the map shows the whole two-way chain, Ghana to the Netherlands to the US and money back, and the panel says "6 of 6 links" |
| D2.Eco.15.3-5 (effects on different groups within nations) | With the rains on, mark each worker Helped, Hurt or Both | The worker's pose changes, then "What the numbers show" with the sourced numbers and one reason | A person in each of the three countries is marked, and the farm family's reveal shows both fewer bags and a higher price per bag |
| D2.Geo.12.3-5 (disaster in one place affects people far away) | Tap "Bring the 2023 rains" (any stop) | Rain over Ghana on the map; every stop's picture, numbers and worker pose change at once, including the store | With the rains on, every stop shows its After state, and turning them off restores every Before state |
| D4.2.3-5 (explanations with reasoning, sequence, examples, data) | In Explain it, order six cause-and-effect sentences and back four of them with number chips | Check names the first broken link; a passing chain reads as one paragraph | Only the one causal order with the right chips passes; each distractor tile and the farm-price chip fail with their own message |

## Screens and modes
Header: title, mode buttons `Follow the bar` and `Explain it`, then the kit's Motion, Sound, Read.

**On load (Follow the bar, Before).** The Store scene fills the stage: a candy shelf, our bar front and centre with its
price tag ($1.00, in code), and a red thread running from the wrapper off the scene's left edge up into the map strip,
where it ends at a pulsing thread end over the Atlantic. Hint: "Tap the red thread to follow the bar back to the farm."
Nothing moves except the pulse (Motion off: a still red ring).
- First tap on the thread (on the scene or the map): the thread reels back along the route (1.5 s; Motion off: at
  once) and the Farm opens. The welcome may be cut by this tap (BASELINE rule 16); its point lives in the hint.
- First tap on `Next stop` or a map pin: opens that stop at once (same as the thread for the Farm).
- First tap on `Bring the 2023 rains`: the rains turn on at the Store; the rains line plays.
- First tap on `Explain it`: Explain mode opens with its welcome.

### Follow the bar
Focus: the stop scene, with its worker beside it. It is the biggest thing on screen.

Layout at 1366x768 (all above the fold, no page scroll):
- Stage (left, about 900 px wide): map strip on top (about 150 px: West Africa, the Atlantic, Europe and North
  America, six pins on the red thread, country names); the stop scene below (16:9, about 764x430) with the worker
  cutout standing fully inside its right third, feet on the scene's floor line; the number tags sit on blank painted
  surfaces (chalkboard, ship hull, gauge panel, price tag). Under the scene, the "Your dollar" strip (about 52 px).
- Panel (right, about 430 px): hint; the season switch (two big buttons: `2022: before the rains` and `Bring the 2023
  rains`); the stop name and country; the worker's card (name, job, two sentences, a "made-up person, real numbers"
  tag); the "This stop needs" question; with the rains on, `Helped`, `Hurt`, `Both`; at the bottom `Back` and
  `Next stop`. The Farm adds a `Hard facts` button that opens a card over the panel (Close returns).
- At 680x425 (tool-page preview): stage and panel stay side by side. The map strip shrinks to a 40 px route of six
  numbered dots with the thread; the dollar strip folds behind a `Your dollar` button in the panel; the worker card
  shows its first sentence and a `More` toggle. Scene text stays 10 px or more.
- At 760 wide and 375 wide: the stage stacks above the panel; the season switch and Back / Next sit directly under
  the scene so they are visible without scrolling.

What the student does and what responds:
- `Next stop` / `Back` walk Farm, Buying station, Port, Grinding factory, Candy maker, Store. A map pin opens its stop.
  The thread lights up to the open stop. At the Store, Next is disabled and the hint points to the rains (see Voice).
- "This stop needs" question (one per stop, below the card): tap the right pin. Right: the goods and money arrows draw
  between the two pins and the question is replaced by a one-line answer. Wrong pin: "Not that one. Follow the thread
  one step back." (for the Farm: "Follow the money all the way to the end."). Never required to move on.
- `Bring the 2023 rains` / `2022: before the rains`: switches every stop at once. The open scene crossfades to its
  After art (0.6 s; Motion off: instant); number tags update with a small "was" value under the new one; a blue rain
  band and the label "2023 rains" sit over Ghana on the map.
- `Helped` / `Hurt` / `Both` (rains on only): the choice is shown; the worker swaps to their "thinking" pose and "What
  the numbers show" opens under the card (Content). Any choice opens it; it never says the student was wrong. A small
  row under the buttons shows who has been marked: Ghana, Netherlands, US.
- "Your dollar" strip: two stacked bars, "One study (2015)" and "Another study (2020)", split by who gets each part of
  the bar's price. The open stop's part glows. A `$1` to `$4` stepper (in $1 steps) relabels each part in cents.
  Tapping a part opens that stop. It does not change with the rains (both studies are older).

What each stop shows, Before and After (all different at a glance):
| Stop | Before (2022) | After (2023 rains and after) |
|---|---|---|
| Farm | Healthy painted farm, yellow-orange pods; 14 bag cutouts on the drying mat; couple in working pose | Wet farm art with blackened pods; 11 bags; couple in thinking pose; rain in code over the scene |
| Buying station | Tall stack of bags by the scale; chalkboard "GH¢800 a bag" | Short stack; chalkboard "GH¢1,308 (Oct 2023)" then "GH¢2,070 (Apr 2024)" on two lines |
| Port | Ship with 10 container cutouts on deck; crane loading | Ship with 8 containers; crane idle; Kojo in thinking pose |
| Grinding factory | Gauge panel needle high, label "busy"; tag "$2,400 a tonne of beans (2022)" | Needle low, label "least in 4 years (late 2024)"; tag "over $10,000 a tonne (Dec 2024)" |
| Candy maker | Full mould line; tag "cocoa: about $2,400 a tonne" | Same line, tag "cocoa: over $10,000 a tonne"; sign "prices up about 10% or more (2025)" |
| Store | Full-size bar, tag "$1.00" | Smaller bar cutout beside a full bar tagged "about $1.10 or more"; label "example prices" |

### Explain it
Focus: the six-step ladder in the middle of the stage.

Layout at 1366x768: stage holds the question on top ("How did rain in Ghana change a chocolate bar here?"), the
ladder (six numbered slots, about 640x60 each, a chip socket at each slot's right end) in the centre, and the tile tray
(eight sentence tiles) in a column to its right; the six number chips sit in a row under the ladder. Panel: hint,
`Check`, `Read my explanation` (disabled until a Check passes), `Clear`. At 680x425 the tray becomes a two-column
grid under the ladder with tiles in 12 px type, and the chip row wraps to two lines; everything stays above the fold.

What the student does: drag a tile onto a slot, or tap a tile then tap a slot (keyboard: Enter on a tile, then Enter
on a slot). A tile on a filled slot swaps with it. Chips go into sockets the same way (only the four numbered tiles
have a socket). `Check` reads top to bottom and reports the first problem (Interactions). A pass draws a thin arrow
between each step and its map stop's icon, and enables `Read my explanation`, which reads the paragraph and shows it
as one block of text. `Clear` empties the ladder.

## Content
**Places and route.** Farm: a cocoa farm in southern Ghana's forest. Buying station: a village cocoa shed where a
licensed buying company's clerk weighs and buys bags. Port: Takoradi, Ghana (Tema also ships cocoa). Grinding factory:
near Amsterdam, the Netherlands. Candy maker: a chocolate factory in the US. Store: a store near you.

**Workers** (made-up people; the tag says "made-up person, real numbers"). Card texts:
- Farm, Ghana: Akosua and Kwame Boateng grow cocoa on about 2 hectares, like many of Ghana's roughly 800,000 cocoa
  families. They cut ripe pods by hand, ferment the beans under plantain leaves for about a week, and dry them in the
  sun. Their two children go to school.
  Needs: "Where does our money come from in the end? Tap that stop." Answer: Store. "Shoppers far away pay for every
  bar. That money flows back along the thread."
  What the numbers show (After): "Ghana harvested about 531,000 tonnes, down from about 656,000: about 1 bag in 5
  lost. Ghana raised its farm price from GH¢800 a bag to GH¢1,308, then GH¢2,070. Fewer bags, more for each bag. The
  world price rose even faster, more than 4 times." Reason: "Both: less cocoa to sell, a better price for each bag."
- Buying station, Ghana: Yaw is a purchasing clerk. He weighs each bag and pays the price Ghana's cocoa board sets
  (16 bags make a tonne). He sells the bags on to the board's marketing company for export.
  Needs: Farm. "The farms fill Yaw's shed." After: "Fewer bags came in, so Yaw had less to weigh and buy."
- Port, Ghana: Kojo loads cocoa onto ships at Takoradi. Most of Ghana's cocoa leaves as beans for factories abroad.
  Needs: Buying station. After: "Ghana shipped less cocoa and earned less from cocoa sold abroad. Fewer bags means
  less loading work."
- Grinding factory, the Netherlands: Sanne runs a grinder. The Netherlands brings in more cocoa beans than any other
  country; factories roast and grind them into cocoa butter, cocoa powder and cocoa paste for chocolate makers.
  Needs: Port. After: "Beans cost over 4 times as much. Late in 2024, factories in Europe ground less cocoa than in
  any three months in 4 years. Less grinding can mean fewer shifts."
- Candy maker, US: Luis works the line where chocolate fills bar moulds. Needs: Grinding factory. After: "Cocoa cost
  far more. In 2025 a big US chocolate maker raised prices about 10% or more and made some packs smaller."
- Store, US: Dana runs the register. Needs: Candy maker. After: "Shoppers here pay more for a bar, or get a smaller
  one. Rain in Ghana reached this shelf."

**Farm, Hard facts card** (opened by its button; plain, no art of children):
"Cocoa farming is hard, and many families earn very little. In 2018-19 a study counted about 1.56 million children
doing child labor in cocoa-growing areas of Ghana and Côte d'Ivoire. Most of it was dangerous work, like using sharp
machetes or carrying heavy loads. Ghana's rules forbid dangerous work for children under 18." Second paragraph, "Whose
idea was cocoa?": "Cacao trees first grew in South America, where people in what is now Ecuador used cacao more than
5,000 years ago. In Ghana, people honor Tetteh Quarshie, a blacksmith who brought cocoa pods home from the island of
Fernando Po and started a farm at Mampong in 1879. Ghanaian farmers built it into one of the world's biggest cocoa
crops; missionaries had planted some trees earlier."

**Map labels.** Ghana, Côte d'Ivoire, the Netherlands, United States, Atlantic Ocean. A note under the map: "Ghana
and Côte d'Ivoire are the world's two biggest cocoa growers."

**The rains line, on screen as the scene caption:** "2023: very heavy rain fell on cocoa farms in West Africa. Black
pod disease rotted many pods. A tree virus and illegal gold mining on farmland made it worse. The world's cocoa
harvest fell about 14%."

**Your dollar.** One study (2015): Farm family 6.6¢; Buying, shipping and grinding (with Ghana's government) 14¢;
Candy maker 35.2¢; Store and taxes 44.2¢. Another study (2020, dark chocolate in France): Farm family 11¢; Buying,
shipping and grinding 19¢; Candy maker and store 70¢. Caption: "Studies differ, but in both the farm family gets the
smallest part." Stepper values: $1, $2, $3, $4 (cents multiply; farm 7 to 11¢ at $1, 26 to 44¢ at $4).

**Explain it tiles** (correct order, with chips):
1. "In 2023, very heavy rain fell on cocoa farms in West Africa, and black pod disease rotted the pods." (no chip)
2. "Ghana's farms harvested much less cocoa." Chip: "656,000 → 531,000 tonnes"
3. "With less cocoa in the world, buyers paid much more for every tonne." Chip: "$2,400 → over $10,000 a tonne"
4. "Grinding factories in Europe paid more for beans and ground less cocoa." Chip: "least in 4 years"
5. "Chocolate makers paid more for cocoa, so they raised prices or made bars smaller." Chip: "about 10% or more"
6. "So rain in Ghana reached our store: shoppers here pay more or get less chocolate." (no chip)
Distractor tiles: D1 "Shoppers here wanted more chocolate, so stores raised the price." D2 "The rain only changed
things for people in Ghana." Distractor chips: X1 "GH¢800 → GH¢2,070 a bag" (true, but the farm price), X2 "16 bags
in a tonne". Tray order is shuffled on each load and Clear.

Paragraph read by `Read my explanation`: the six sentences in order with their chips in brackets read as "(from
656,000 to 531,000 tonnes)" and so on.

## Interactions in detail
- Season is one shared state across stops and modes. The rains toggle never moves the student to another stop.
- Tapping anything while the thread reels or a scene crossfades acts at once: the reel jumps to its end, the crossfade
  completes, the new action runs. No control is ever disabled during an animation.
- Needs question: each stop's question is answered once; answers persist until Reset. The arrows stay on the map. Six
  answers show "6 of 6 links" and a one-line caption "Goods go one way, money comes back. Each country needs the
  others." The Store's needs pin is the Candy maker; the Farm's is the Store.
- Helped / Hurt / Both buttons are hidden (not disabled) while the rains are off. A choice can be changed; the reveal
  stays. Turning the rains off keeps the choices and hides them; turning on restores them.
- Explain check order: (a) an empty slot from the top: "Put a sentence in step N." (b) a distractor: D1 "Step N blames
  shoppers. What made cocoa cost more in the first place?" D2 "Step N says only Ghana changed. Look at the store." (c)
  a correct tile in the wrong place: "Step N doesn't follow from step N-1. What had to happen first?" (d) a missing
  chip: "Step N needs a number. Pick one from the row." (e) X1 anywhere: "That is the price Ghana pays its farmers for
  a bag, not the world price for a tonne." (f) any other wrong chip: "That number doesn't back step N. Check its
  units." (g) all right: pass. One message at a time; no score, no count of tries, no timer.
- Reset: none in the header. `Clear` resets Explain; Follow keeps its state for the visit (no localStorage needed).
- Extremes: $4 on the stepper shows the largest cents (318¢ to the maker and store in the 2015 study, still under
  $4.00). Rains toggled ten times fast: the scene shows the last state; only the latest line is queued.

## Look
Warm cocoa paper, burnt cacao orange accent, a single red thread. Different from barter-bay's harbor blues and the
phone tool's data-desk greys.
- `--paper #fbf6ee`, `--panel #f3e7d6`, `--ink #2b1d14` (15.15:1 on paper, 13.36:1 on panel), `--muted #6b5646`
  (6.41:1 / 5.65:1), `--brand #9a3f12` (6.31:1 as text on paper; white on brand 6.79:1), thread `#c0392b` (5.05:1,
  never the only signal: the thread is also thick and dashed where unvisited), rain blue `#1f5f8b` (6.36:1; white on it
  6.84:1), goods arrow `#7a4a2a` (6.87:1), money arrow gold `#f2c14e` with a 2 px ink edge (ink on gold 9.71:1),
  Helped green `#1d6b45` (6.02:1). Helped / Hurt / Both also carry an icon and a word.
- Number tags: bold sans on the painted blank surfaces, with a paper-coloured backing plate when the surface is busy.

## Art
Painted, warm gouache style, one artist feel across the set. People are illustrated, with a varied, respectful cast;
Ghanaians shown as skilled working adults in everyday clothes, never in poverty clichés.
- store-shelf: a bright store candy aisle, one shelf at eye level with plain blank-wrapped chocolate bars and a blank
  price-tag rail; 16:9; no cutout; no people; Store background.
- farm-dry: a shaded cocoa farm under tall forest trees, ripe yellow and orange pods on the trunks, a raised drying
  mat of brown beans in sun; 16:9; no; no; Farm Before.
- farm-wet: the same farm under a grey sky, puddles, dark rotted pods on the trunks, the drying mat covered; 16:9;
  no; no; Farm After (same framing as farm-dry so the crossfade lines up).
- cocoa-bag: one jute cocoa sack, plain, standing; 1:1; cutout; no; repeated in code for bag counts (Farm, Buying).
- buying-shed: an open-sided village cocoa shed with a hanging scale and a blank chalkboard; 16:9; no; no.
- port-quay: a West African port quay with a cargo ship side-on, an empty open deck, a crane; 16:9; no; no.
- container: one shipping container, plain side; 4:3; cutout; no; stacked in code on the deck (10 or 8).
- grind-hall: a clean factory hall with roasting drums, grinders and steel hoppers, a blank round gauge panel; 16:9;
  no; no. The needle is drawn in code.
- mould-line: a chocolate factory line, melted chocolate flowing into bar moulds, a blank wall sign; 16:9; no; no.
- bar-full and bar-small: one chocolate bar in a plain blank wrapper, full size, and the same bar visibly shorter;
  4:3; cutouts; no; Store.
- People (Gemini, `people: true`, 3:4, cutouts, full body head to feet, two poses each: working, thinking):
  akosua-kwame (a Ghanaian couple in their 30s, she holds a cocoa pod, he a harvesting hook), yaw (Ghanaian clerk in a
  short-sleeve shirt by a scale), kojo (Ghanaian dockworker in a hi-vis vest and hard hat), sanne (Dutch factory
  operator in a white coat and hairnet), luis (Latino line worker in a white coat), dana (Black American cashier in a
  store apron). 12 images. Each stands fully inside the scene's right third in every mode and size; no part is cut by
  the frame or hidden behind the panel. Working and thinking poses differ clearly at 120 px tall.
- Map, rain, arrows, gauges, tags and the dollar strip: drawn in code (data and labels). Map outlines from Natural
  Earth 1:110m (public domain), equirectangular, lon -100 to 20, lat -5 to 60.

## Voice
Bank voice `friendly-dad` (relaxed, warm, like a parent tracing where something came from at the kitchen table).
Neighbors with voice files use none of it nearby; barter-bay and the phone tool have no voice yet. Narration only for
welcomes, hints, the rains and results; card texts are read on screen (Read speaks them).
| Key | Kind | When | Stale when | Text |
|---|---|---|---|---|
| wFollow | how | Follow welcome | thread pulled | "This chocolate bar came a long way. Tap the red thread to follow it back to the farm." |
| readStop | how | first stop opened | Next or a pin tapped | "Read about the people here. Then tap Next stop." |
| needs | how | first needs question shown | that question answered | "Where does this stop get its cocoa? Tap that stop on the map." |
| needsFarm | how | Farm question first shown | answered | "Where does the farm's money come from in the end? Tap that stop on the map." |
| needRight | event | right pin | another stop opened | "Yes. Cocoa comes this way, and money goes back." |
| needWrong | event, once per stop | wrong pin | answered | "Not that one. Follow the thread one step back." |
| atStore | how | Store reached with rains off | rains on | "You followed the whole chain. Now tap Bring the 2023 rains." |
| rainsOn | event, whole | rains turned on | rains turned off | "In 2023, very heavy rain fell on cocoa farms in West Africa, and a disease rotted the pods. Watch every stop change." |
| rainsOff | event | rains turned off | rains on | "Back to 2022, before the rains." |
| askHurt | how | first stop shown with rains on | a choice made there | "Was this person helped, hurt, or both? Tap one." |
| reveal | event | a choice | another stop opened | "Here is what the numbers show." |
| allLinks | event, once | sixth link drawn | another action | "Goods go one way and money comes back. Each country needs the others." |
| wExplain | how | Explain welcome | a tile placed | "Build the explanation. Drag a sentence into step 1, or tap it, then tap the step." |
| check* | event | Check | ladder changed | each Check message in Interactions, word for word (8 lines with N filled 1 to 6) |
| pass | event, whole | Check passes | ladder changed | "Every step follows the one before, with its number. Tap Read my explanation." |
| paragraph | event, whole | Read my explanation | Clear or a tile moved | the assembled paragraph |
- `needs` lines use `needs` on the map pins; `atStore` never plays when the rains are already on; `askHurt` names
  buttons only while they are visible. rainsOn is whole: lines after it wait; a rains toggle during it replaces it.
- Read: speaks the hint, then the open stop's card text (and the Hard facts card when open).

## Family engine
None. Uses `Curio.voice` and the kit header.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| 2022 hot and dry; 2023 very heavy rain spread black pod disease | BLS Monthly Labor Review, "Why is candy so expensive these days?" (2026) | Bloomberg, "Cocoa surges to 13-year high as disease ravages West Africa crop" (2023, via BNN) | yes |
| Swollen shoot virus and illegal mining also cut Ghana's crop | Graphic Online, "Cocoa paradox" | Reuters via ESM, Ghana 2023-24 output 40% below target | yes |
| World harvest fell about 14% (4.9 to 4.2 Mt; 5.04 to 4.37 Mt) | World Bank Data Blog, 7 Jan 2025 | BLS MLR 2026 (ICCO data) | yes (14.3% and 13.5%) |
| Ghana harvest about 656,000 t (2022-23), about 531,000 t (2023-24) | Graphic Online (655,808; 530,873) | ConfectioneryNews 2024 (656,140); Africa Sustainability Matters (531,000) | yes |
| Farm price GH¢800 a bag 2022-23 | COCOBOD press release, Oct 2022 | Graphic Online, Oct 2023 | yes |
| GH¢1,308 a bag from Oct 2023; GH¢2,070 (GH¢33,120 a tonne) from Apr 2024 | Graphic Online (both) | Reuters via MarketScreener (58% rise to 33,120); MyJoyOnline (63.5% to 1,308) | yes |
| 16 bags of 64 kg gross make a tonne (GH¢12,800 = 16 x 800) | COCOBOD Oct 2022 | Graphic Online (20,928 = 16 x 1,308) | yes |
| World cocoa price about $2,400 a tonne in 2022 | IMF via FRED PCOCOUSDA ($2,369) | ICCO annual report 2022 ($2,368) | yes |
| Over $10,000 a tonne in December 2024 | World Bank Data Blog (Dec average over $10/kg) | BLS MLR 2026 (record $12,565 futures, Dec 2024) | yes |
| Ghana and Côte d'Ivoire are the world's two biggest cocoa growers | World Bank Data Blog, 7 Jan 2025 (together nearly 60%) | Africa Sustainability Matters (Ghana the no. 2 producer) | yes |
| Many cocoa farmers earn very little | Cocoa Barometer 2015 via ConfectioneryNews (extreme poverty) | King's College London, "Whose cocoa life" | yes |
| Netherlands imports more cocoa beans than any country | CBS Statistics Netherlands | CBI market information | yes |
| Grinding makes cocoa butter, powder and paste | ICCO, processing pages | CBI cocoa products market page | yes |
| Europe's Q4 2024 grind lowest in 4 years | Bloomberg, 16 Jan 2025 ("lowest since 2020") | ADMIS / Mintec Q4 2024 grind notes (ECA, down 5.3%) | yes |
| Ghana earned less from cocoa exports | MyJoyOnline (export revenue down over $500 million) | BusinessLive/Bloomberg (falling cocoa hits Ghana trade surplus, Mar 2024) | yes |
| Licensed buying companies buy from farmers at COCOBOD's price and sell to its marketing company | Barry Callebaut 2015 annual report (Nyonkopa) | Academic study, Ghana domestic cocoa chain (Cogent Business, 2018) | yes |
| Takoradi (and Tema) ship Ghana's cocoa | Citi Newsroom (beans to Takoradi) | ModernGhana / CMC (55% Takoradi, 45% Tema) | yes |
| About 800,000 cocoa families; farms about 2 ha | SNV Cocoa Eco project | Kongor et al., Agroforestry Systems 2018 | yes |
| Pods cut by hand; beans fermented under leaves about 5 to 7 days; sun dried | ICCO, harvesting and post-harvest | Tropentag 2013 (Nuamah) | yes |
| 2025: a big US maker raised prices "low double digits" and shrank some packs | NBC News, 23 Jul 2025 | CNN via KSL, 23 Jul 2025 | yes |
| Farm share of a bar: 6.6% (2015) and 11% (2020); maker and store 79.4% and 70% | Cocoa Barometer 2015 via ConfectioneryNews and King's College London | FAO/BASIC 2020 via Confectionery Production | they differ; the tool shows both and says so |
| 1.56 million children in child labor in cocoa areas of Ghana and Côte d'Ivoire, 2018-19; most hazardous | NORC 2020 final report | ConfectioneryNews, 19 Oct 2020 | yes |
| Hazardous work includes machetes and heavy loads; Ghana forbids it under 18 | US DOL ILAB / NORC cocoa slides | Ghana Hazardous Child Labour Activity Framework (2008) review | yes |
| Tetteh Quarshie brought pods from Fernando Po; Mampong farm, 1879; missionaries planted earlier | COCOBOD "Cocoa" page | Time Out Accra; Visit Ghana | yes (dates of his trip vary; the tool says only 1879 for the farm) |
| People in today's Ecuador used cacao over 5,000 years ago | Zarrillo et al., Nature Ecology and Evolution 2018 | Science News, Oct 2018 | yes |

Cut (could not back twice): "most rain in 20 years" (BLS only); "more than half" of world cocoa; an exact store price for a bar (NielsenIQ $2.43 to $3.45, one source); candy CPI 9.8%;
Ghana's 160,000 t smuggling estimate; Ghana's forward sales at $2,661; Harmattan winds; the 770,000 / 710,000 country
splits; any family income figure.

Checks run (Python, `S:/CurioClass-codex-scratch/specs/cocoa-chain/check.py`): Ghana harvest -19.1% (about 1 bag in
5); family example 2 ha x 452 kg/ha = 905 kg = 14 bags at 62.5 kg net, after 11.3, shown as 11; containers 10 to 8.1,
shown as 8; farm price x1.64 then x2.59; world price x4.2 (2022 to Dec 2024); world harvest -14.3% and -13.5%; dollar
strips sum to 100 (middle 14.0 and 19.0); stepper farm cents 7 to 11 at $1, 26 to 44 at $4; store example $1.10 to
$1.13. Explain check: 20,160 tile orders give exactly 1 pass; 360 chip assignments (six chips into four sockets) give exactly 1 pass;
doing nothing gives "Put a sentence in step 1"; X1 in step 3 gives the farm-price message; D1 in step 6 fails; swapping steps
4 and 5 fails at step 4. Contrast ratios as in Look.

## Done when
1. Focus: in Follow the bar at 1366x768 the stop scene is the largest element, the worker is fully visible beside it,
   and the season switch, Back and Next stop are all above the fold; at 680x425 scene, switch and Next still show.
2. A tap while anything plays (the thread reel, a crossfade, the rains line) acts at once and the screen matches it.
3. The first tap on the thread opens the Farm; the first hint names the thread; Next walks all six stops in order.
4. D2.Eco.14: six right needs answers draw six goods and money arrow pairs and "6 of 6 links"; a wrong pin gets its
   hint once per stop.
5. D2.Geo.12: the rains switch changes every stop's art, numbers and pose as in the table, and back again; the Store
   shows the smaller bar and "about $1.10 or more" with the rains on.
6. D2.Eco.15: Helped / Hurt / Both appear only with the rains on; each reveal shows its sourced numbers; the farm
   reveal shows 531,000 vs 656,000 tonnes and GH¢800 to GH¢2,070.
7. D4.2: only the one order with the four right chips passes; D1, D2 and X1 each give their own message; nothing
   counts tries; Read my explanation reads the full paragraph.
8. Every number on screen matches this spec's Sources; the dollar strip says the studies differ.
9. Voice: each how line speaks once in a run of five repeats; rainsOn speaks every toggle on and is not cut by the
   next line; no line names a hidden button.
10. The Hard facts card, the Quarshie credit and the cacao origin read as written; no picture shows a child working.

## Open questions
- Sensitivity review (rule 5, fresh agent): Ghana's people and places in art and text, the child labor card, the
  Tetteh Quarshie credit and the missionary note, the made-up names, and the 12 people images (Cory's contact sheet).
- None for Cory.
