# Trade Island

## One idea
Run Pell, the island that is better at both fishing and weaving, and find that it still fills more baskets by
fishing more and trading fish for Wren's cloth (and that a storm which evens out the costs kills every good deal),
then pull three real policy levers (a tariff, a currency swing, a factory moving across the strait) and read who
wins and who loses on each island.

## Not like
- the-buyout (same format and grade, spec): one market's structure, four sellers then one; here two whole economies,
  opportunity cost and trade policy, and no market share or HHI.
- where-s-my-phone-from (grade 10 data desk): real supply-chain data for one product; here a model of two islands
  the student runs, with real cases only as case cards.
- one-more-hour: one person's marginal hours; here a whole island's split of workers between two goods.
- two-villages: property rights and contracts inside one country; here trade between two.
- fed-chair, economy-dashboard: interest rates and indicators for one economy; no trade between nations.
- lake-commons (science 9) and grid-operator (science 12): the 2026 audit (docs/agents/audit/clashes-9-12.md, K06)
  kept the islands here because the two-island model is how comparative advantage is taught, and moved lake-commons
  to a lake town and grid-operator's island to a backdrop. Different picture too: two islands across a strait with
  boats and looms, never a lake, a control room or a single island map.
- imaginary-island (math 11, live): a night chart of the complex plane; nothing shared but the word island.

## Who and how
Grade 12, social studies (Economics: Global Trade). Driver: students on their own laptops, solo by default (Wren is
played by the computer); a teacher can project Islands Season 2 and the Policy table for discussion. 35 to 45
minutes (Islands 15, Policy 15, Case 10). Standards: D2.Eco.14.9-12, D2.Eco.15.9-12. No personal prompts. The idea
card's two-student bargaining mode is left out (it needs two devices to be fair); a pair can share one laptop and
argue each deal aloud. Pell, Wren, shells and beads are a teaching model; the case cards are real.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.14.9-12 (analyze the role of comparative advantage in international trade) | In Islands, fill the Cost card (fish given up for one cloth on each island), then move Pell's workers and offer deals until both islands fill more baskets; repeat in Storm and Motor boats | Per-worker chart; Alone vs Now bars for fish, cloth and full baskets on both islands; Wren's reply; the cost row once checked | Season 2 shows the "Both islands fill more baskets" banner only with Pell's fishers above 60 (lowest found: 66); the Cost card's Storm answer is "Neither: same cost"; no deal in Storm lights the banner |
| D2.Eco.15.9-12 (explain how globalization trends and policies affect growth, labor markets, rights, the environment and income distribution in different nations) | In Policy, set each lever and read both islands' Growth, Jobs, Wages, Rights and Reef cards and the winners and losers table; pin evidence; in Case, argue for or against one policy | Ten group rows with portraits and +/- amounts; five cards per island; the factory's choice to move or stay | Check case fails without a pinned chip from each island, without one gain and one loss, or without a chip from Jobs, Wages, Rights or Reef |

## Screens and modes
Header: title "Trade Island"; `.seg` mode buttons **Islands**, **Policy**, **Case**; icon buttons Motion (`motion`),
Sound (`sound`), Read (`read`). Kit stage plus panel; at 1366x768 the stage is about 896 wide, the panel 470. Under
about 900 px tall the panel goes buttons-first.

**On load:** Islands, Season 1 "Alone" (strait closed). The painted strait fills the stage top, Pell on the left,
Wren on the right, worker tokens standing at each island's fish dock and loom shed (each token is 5 workers, 20 per
island; Pell 10 and 10 at the default, Wren 15 and 5 at its best alone). Below it the bars. Panel top: the Predict
card: "Pell is better than Wren at fishing AND at weaving. Should Pell trade with Wren?" **Yes** / **No**. The workers
slider starts at 50 fishers (300 fish, 150 cloth, 100 baskets). Hint: "Slide Pell's
workers between fish and cloth to fill the most baskets." Focus goes to the slider (`preventScroll`). First tap on
the slider moves tokens and bars at once; first tap on Yes or No records the guess and collapses the card to "You
said No. Keep going." (the welcome may be cut; the hint keeps the task). Nothing is scored.

### Islands (opens here)
- Focus: the strait scene with the Alone and Now bars under it. Scene about 896x330; bars about 896x230: for each
  island three pairs (fish, cloth, full baskets), the Alone value as a hollow grey outline bar with its number, Now
  as a filled bar (Pell sea blue, Wren sand) with its number and a small up or down arrow glyph and word ("more",
  "fewer", "same").
- Season tabs at the top of the panel: **1 Alone**, **2 Open strait**, **3 Storm**, **4 Motor boats**, each keeping its
  own split and deal. Below: the per-worker chart (a small table: "One Pell worker: 6 fish or 3 cloth"; "One Wren
  worker: 2 fish or 2 cloth"; changed numbers marked "storm" or "motor boats"); the workers slider (Pell fishers
  0 to 100 in 1s, with - and + buttons; "Weavers: 100 minus that"); Wren's split shown read-only ("Wren chooses its
  own split").
- Seasons 2 to 4 add the Deal box: **Send fish** / **Send cloth** toggle; Send amount and Get amount steppers (0 to 300
  in 10s, - and + buttons, the value typed or stepped); the price line "That is 1.5 fish for each cloth"; **Offer
  deal**. Wren's reply appears under it. A deal accepted is drawn as a boat crossing with crate and bolt icons and stays
  in force until the amounts change (then "Not offered yet").
- **Cost card** button opens the card in the panel (paged, not a scroll panel): "One cloth costs Pell __ fish" and
  "One cloth costs Wren __ fish" (steppers 0 to 4 in 0.5s), "Who should make more of the cloth?" **Pell** / **Wren** /
  **Neither: same cost** (fixed order), **Check**. From Season 3 on, Wren's row is filled and marked "unchanged since
  Season 2".
- Season 1: no Deal box (the strait is closed, the hint never names Offer). Reaching 120 baskets shows "Pell's best
  alone: 120 baskets" on the bar.
- At 680x425: the per-worker chart becomes one line; the bars keep only the baskets pair per island; the scene shrinks
  but keeps both islands whole. Slider, Deal box and Offer stay visible.
- What the picture shows for every outcome: both better, a gold banner over the strait and both baskets bars filled
  past their outlines; only Wren better, Wren's bar past its outline and Pell's short of it with the word "fewer";
  declined, the boat stays at Wren's dock and a "No deal" tag; Storm, rain over Pell and broken masts; Motor boats,
  motor boats at Pell's dock.

### Policy
- Premise in the hint and Read: "The islands now trade with money: Pell's shell and Wren's bead. Pell sells fish and
  buys cloth. Pull a lever and see who wins and who loses on each island."
- Focus: the winners and losers table, center, about 896x330: ten rows (Pell shoppers, fishers, home weavers,
  factory owners, factory workers, treasury; Wren shoppers, fishers, home weavers, factory workers), each with its portrait (48x64),
  group name, island, and the change per season in that island's money with a gain or loss word and +/- sign (never
  color alone), plus a pin button. Above it a strait strip (the strait art cropped as a 896x140 band) showing the
  factory cutout on the island where it now sits and two crate counters ("Cloth to Pell: 46 bolts", "Fish to Wren:
  27 crates"). Between them the island cards, 2 rows of 5 (about 896x170): Growth, Jobs, Wages, Rights, Reef, each with
  a pin.
- Panel: hint; **Tariff on Wren cloth**: 0 / 0.5 / 1 shell a bolt (labeled "none", "about 10%", "about 20%");
  **Pell's shell**: Steady / Rises 10% / Rises 20%; **Cloth factory**: Stays in Pell / May move to Wren; **Wren's
  rules**: Labor Basic / Strong, Dye Loose / Strict; **Reset levers**; the case card for the lever moved last.
- At 1366x768 the strip, cards, table and the whole panel fit. At 680x425 the strip folds away, the cards become one
  line per island, and the table pages by island (**Pell** / **Wren** tabs).
- Outcomes at a glance: tariff, the cloth counter drops and Pell's treasury chest fills; shell rises, the fish counter
  drops; factory moves, the factory cutout slides across the strait and Wren's reef image swaps to the murky state
  under Loose dye rules; factory stays, it shakes once and the line "Moving would not pay" shows on it.

### Case
- Focus: the case sheet, center: **For** / **Against** and policy picker **The tariff** / **Letting the factory move**;
  pinned chips (the group or card, island and value as pinned); a sentence box; **Check case**; **Save on this
  device** with "Your case stays on this device. Nothing is sent." The matching real case card sits beside the sheet.
- At 680x425 the case card becomes a **Real case** button. With no pins yet the hint reads "Pin rows and cards in
  Policy, then come back."

## Content
**Islands model.** Each island has 100 workers. A family's full basket is 3 fish and 1 cloth; full baskets =
floor(min(fish / 3, cloth)). Per worker per season: Season 1 and 2, Pell 6 fish or 3 cloth, Wren 2 fish or 2 cloth;
Season 3 Storm, Pell 3 fish or 3 cloth; Season 4 Motor boats, Pell 9 fish or 3 cloth (Wren unchanged throughout).
Best alone: Pell 120 baskets at 60 fishers (360 fish, 120 cloth) in Seasons 1 and 2, 75 at 75 (Storm), 150 at 50
(Motor boats); Wren 50 at 75 fishers (150 fish, 50 cloth). Alone outlines always show these best-alone values.
Slider default 50 fishers (300 fish, 150 cloth, 100 baskets) in every season.
**Wren's AI:** for an offered deal, Wren tries every split 0 to 100 and keeps the one with the most exact baskets
(ties: fewer fishers); it accepts only if its full baskets beat 50. It declines with the reason.
**Cost card answers:** Seasons 1 and 2, Pell 2, Wren 1, Wren; Storm, Pell 1, Wren 1, Neither; Motor boats, Pell 3,
Wren 1, Wren. Feedback: right, "Right. One Pell worker gives up 2 fish for each cloth; one Wren worker gives up 1.
Wren makes cloth more cheaply, so Pell should fish." Pell chosen: "Pell makes more cloth per worker (3 against 2),
but each Pell cloth costs 2 fish and each Wren cloth costs 1. Cost is what you give up." A wrong number shows the
working: "Pell: 6 fish or 3 cloth a worker, so 1 cloth = 6 / 3 = 2 fish." (Storm and Motor boats use their numbers.)
**Reference deals** (Send fish 150, Get cloth 100, 1.5 fish a cloth): Season 2 at 90 fishers, Pell 390 fish, 130
cloth, 130 baskets (alone 120); Wren picks 18 fishers, 186 fish, 64 cloth, 62 baskets (alone 50): more of both
goods on both islands. Storm: Wren accepts (62) but Pell's best is 50 baskets at 100 fishers (alone 75). Motor boats
at 75 fishers: Pell 525 fish, 175 cloth, 175 baskets (alone 150); Wren 62.
**Island lines:** both better: "Both islands fill more baskets than either could alone, and Pell is still better at
both jobs." Predict reveal on the first banner: "You said No. Pell gained by doing less of what it is good at."
(or "You said Yes. Here is why it works.") Storm, after a declined or losing deal: "When each cloth costs both
islands the same fish, no price helps both." Ricardo card (after the first banner): "David Ricardo, 1817: Portugal
needed fewer workers than England for both wine and cloth, yet both gained when England made cloth and Portugal
made wine."

**Policy model** (cloth in bolts, fish in crates, per season; Pell prices p, r in shells; Wren prices q, s in beads;
E = beads per shell: 1, 1.1, 1.2). Cloth: Pell buyers 240 - 20p; Pell home weavers 20p - 40; Wren buyers 120 - 10q;
Wren home weavers 100q - 373 (all floored at 0). Fish: Pell buyers 300 - 30r; Pell fishers 40r - 40; Wren buyers
200 - 25s; Wren fishers 10s - 10. The cloth factory sells 20 x (price - cost) bolts: in Pell at p, cost 3 shells
(1 materials + wage 6 / 3 bolts a worker); in Wren at q, cost in beads 1 + wage / 3 + dye (Basic wage 3, Strong 4.5;
dye Loose 0, Strict 0.5). Prices: q = E(p - t) for cloth (tariff t on cloth into Pell), s = E r for fish; each market
clears in total. Groups (change from the open-trade start, own money): shoppers lose the area under their demand
between old and new price (cloth plus fish); fishers and home weavers gain the area under supply; factory owners
(Pell people wherever the factory is) profit 10 x (price - cost)^2, in shells (divide by E in Wren); factory workers
gain jobs x (wage - other work), other work 4 shells in Pell and 2 beads in Wren; treasury t x cloth imports. Jobs:
Pell catch / 6, Pell home cloth / 3, factory output / 3; Wren catch / 2, Wren home cloth / 2. Reef (of 100): Pell
100 - 0.1 x catch - 0.05 x factory output if in Pell; Wren 100 - 0.1 x catch - (0.25 Loose, 0.05 Strict) x factory
output if in Wren. Rights card text: Pell "48-hour weeks, inspectors check wages and hours, workers may form a union";
Wren Basic "60-hour weeks, few wage and hour checks, unions not recognized"; Strong as Pell. Wages card: factory wage and other work on that island.
Growth card: the island's total of its rows. When the shell has moved, both Growth cards read "Not added up: a
currency swing changes what each money is worth, so this model shows each group, not a total."
**Factory choice:** with "May move", the owners compare profits after each market settles and move only if Wren
earns more than 1 shell a season more. Move table (Basic-Loose, Basic-Strict, Strong-Loose, Strong-Strict): steady
shell, no tariff M M M S; tariff 0.5, M S S S; tariff 1, S S S S; shell +10%: no tariff M M M M, tariff 0.5 M M M S,
tariff 1 M S S S; shell +20%: no tariff M M M M, tariff 0.5 M M M M, tariff 1 M M M S.
**Reference outputs** (rounded; Pell shells / Wren beads):
- Start: cloth 4.90, fish 5.24 on both islands; cloth to Pell 46, fish to Wren 27; factory in Pell, 38 bolts, 13
  jobs; jobs Pell 28 fishing, 19 weaving; Wren 21, 59; reef Pell 81, Wren 96.
- Tariff 0.5: Pell cloth 5.22, Wren 4.72; Pell shoppers -45, home weavers +20, owners +13, factory workers +4,
  treasury +13 (total +6); Wren shoppers +13, home weavers -19 (total -6); both together -0.5. Tariff 1: shoppers
  -88, weavers +42, owners +29, workers +9, treasury +7 (Pell -1); Wren shoppers +26, weavers -35 (Wren -9).
- Shell +10%: Pell shoppers +68, fishers -28, home weavers -16, owners -10, workers -4; Wren shoppers -33, fishers
  +15, home weavers +20; fish to Wren 15. Shell +20%: +131, -53, -29, -18, -7; Wren -61, +30, +41; fish to Wren 4.
- Factory moves (Basic, Loose): Pell shoppers +17, home weavers -7, owners +41, factory workers -25 (13 jobs gone),
  total +26; Wren shoppers +8, home weavers -13, factory workers +19 (19 jobs), total +14; Wren reef 82. Basic,
  Strict or Strong, Loose: 47 bolts, 16 jobs, owners +19, Pell total -2; Wren +13 (Strict, reef 93) or +37 (Strong,
  reef 84). Strong and Strict: stays.
**Case cards** (two lines each, with a link): Tariff, washers 2018: "The US put tariffs on imported washing machines
in 2018. Washer prices rose nearly 12%, dryers rose about as much, and about 1,800 jobs were added, at a cost to
buyers of more than $800,000 a job." (aeaweb.org research highlight). Factory move, Cambodia textile deal 1999: "In
1999 the US raised Cambodia's clothing quota 6% a year, and promised up to 14% more on top if its garment factories
followed labor law. The ILO sent monitors into the factories and made what they found public." (ILO page).
Currency, Swiss franc 2015: "On 15 January 2015 Switzerland's central bank dropped the cap of 1.20 francs per euro
it had held since 2011. The franc jumped, and shares of Swiss exporters fell." (CRS report IN10230).
**Case check:** For or Against, a policy, 2 to 5 pins including: one from each island, one gain and one loss, one
from Jobs, Wages, Rights or Reef; pins taken while that policy was on (tariff above 0, or the factory moved); a
sentence of 15 words or more. Each failed part reads "Fix: ..." ("Fix: pin a row from Wren too."). Pass: "Your case
holds together. Save it, or argue the other side." Save stores picks and text under `curio-trade-island-case`.

## Interactions in detail
- Slider and steppers recompute bars at once; the boat crossing plays 1.2 s (Motion off: the boat jumps). A tap during
  it acts at once; a new Offer cuts the crossing to its end.
- Offer with more than Pell makes: "Pell only makes 360 fish at this split. Move workers or send less." (event).
  More than Wren can make: "Wren can make at most 200 cloth." Wren's reply names its numbers: "No deal: Wren would fill
  48 baskets, fewer than the 50 it fills alone." An accepted deal holds while the slider moves (Wren's side is fixed);
  if Pell no longer has the goods, the deal shows "Pell can't cover this" and the Now bars use no trade.
- Extremes: 0 fishers fills 0 baskets; 100 fishers fills 0 baskets alone. Send 0 or Get 0 keeps Offer enabled and
  Wren replies "A deal needs something both ways."
- Policy levers apply at once (closed-form solve, no animation wait); Reset levers returns to the start. Pins persist
  across modes in memory; a pin's value is frozen as pinned.
- Keyboard: slider arrows 1, Page keys 10; every control reachable in panel order before the table pins.

## Look
Band theme `kit/theme-912.css`. `--brand` harbor blue `#7cc4ff` (9.23:1 on `--panel`, 10.02:1 on `--paper`;
`--brand-ink` `#0b1a2a` on it 9.37:1). Pell series = brand blue; Wren series sand `#f0b860` (9.67:1 on panel); fish
`#b8d4e8` (11.23:1), cloth madder `#ff9a8a` (8.44:1), Alone outlines grey `#8a96a8` (5.78:1), gains `--ok`, losses
`--warn`, each with a +/- sign and word. Code text on painted signs: `#1a1a1a` on `#f4ead6` (14.58:1). Sunlit sea
blues and sands; differs from the-buyout violet, grid-operator amber, lake-commons reed green, imaginary-island
teal, stock-market-1929 ticker green.

## Art
- strait: two islands across a sunny strait seen from a hill, left island a whitewashed stone harbor town with
  sailing fishing boats at a dock and a stone loom shed, right island timber houses on stilts, terraced green slopes
  and open-sided loom sheds with colored cloth drying; blank wooden sign boards on each dock; 16:9; no cutout; people
  no; Islands stage and Policy strip.
- boat-sail, boat-motor, boat-broken (mast snapped, sail torn), trade-boat (a small cargo boat with crates and cloth
  bolts on deck): 4:3; cutouts; people no; docks and the strait crossing.
- storm: dark rain clouds with slanting rain, transparent edges; 4:1; cutout; over Pell in Storm.
- pell-fisher, pell-weaver, pell-factory-worker, pell-owner, pell-shopper, wren-fisher, wren-weaver,
  wren-factory-worker, wren-shopper: one standing adult in work clothes holding the tool of the job (a net, a
  shuttle, a bolt, a ledger, a market basket), Pell in sea-blue linen, Wren in sand and rust cotton, a varied cast of
  ages, genders and body types; 3:4; cutouts; people yes (Gemini, Cory's contact sheet, fresh-agent check); worker
  tokens (about 30x40) and table portraits (48x64), whole figure visible.
- basket (a woven basket holding three fish and a folded cloth), crate (a wooden fish crate), bolt (a rolled bolt
  of cloth), chest (a small wooden coin chest): 1:1; cutouts; people no; bar labels, counters, treasury row.
- factory: a two-story brick cloth mill with tall windows and a chimney, blank sign board; 4:3; cutout; Policy strip.
- reef-healthy (bright coral and fish in clear water), reef-murky (pale coral in cloudy brown water): 4:3; no cutout;
  Reef cards. 21 images, 9 with people. Header icon reuses trade-boat.

## Voice
Bank `wise-mentor`, style "Say thoughtfully and warmly, like a harbor master who has watched many trading seasons"
(no neighbor uses it: the-buyout news-reader, grid-operator firm-captain, lake-commons easy-coach, imaginary-island
and stock-market-1929 hs-narrator). `Curio.voice`, scope = mode. Bars, tables and cards are read on screen; Read
speaks the hint.
- wIslands (how, Islands welcome, stale once the slider moves): "Pell is better than Wren at fishing and at weaving.
  Slide Pell's workers between fish and cloth, and fill as many baskets as you can."
- openStrait (how, on entering Season 2): "The strait is open. Set what Pell sends and what it gets, then tap Offer
  deal."
- costCard (how, on first opening the card): "Work out what one cloth costs each island in fish, then tap Check."
- bothBetter (event, each time a deal newly lights the banner): the both-better line in Content.
- noDeal (event, each decline): Wren's reply text. stormNone (event, once per Storm visit): the Storm line.
- wPolicy (how): "Pull a lever on the right, then read who wins and who loses on each island."
- factoryMoves (event, when it moves): "The factory crosses to Wren. Watch the jobs, the wages and the reef."
  factoryStays (event): "Moving would not pay under these rules, so the factory stays in Pell."
- wCase (how): "Pick a side and a policy, then use your pins to make the case."
- casePass / caseFix (event): the pass text in Content, or "Some parts need work. The list shows what to fix."
How lines play once, then hint only. No line names Offer deal in Season 1 or Check case before a pin exists.

## Family engine
none. The money family has no engine for trade models; the islands and policy models live in src.html (BASELINE 13).

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails (or the design change made here) |
|---|---|---|
| Both-better banner (S2, S4) | guessing deals; mashing big amounts; keeping Pell's alone split; the common wrong answer (Pell keeps making both, or sends cloth); the answer on screen (a price range or best deal shown); doing nothing | Random deals light it 0.33% (S2) and 1.06% (S4) of split and deal combos (computed); at Pell's alone split no deal of 181,800 does it; Send cloth never does in S2 or S4; all fish with 300 for 200 fills 100 and Wren declines; no price range, best deal or opportunity cost is shown before the Cost card is checked; doing nothing leaves the bars on their outlines. Finding one by trial still shows the price between 1 and 2 fish, which the Ricardo card then names. |
| Storm (no banner) | mashing until one lights | none exists (0 of 181,800); Wren accepts deals that leave Pell worse, so the student sees why |
| Cost card numbers | guessing (9 values each); elimination across seasons (Wren repeats) | not scored; a wrong number shows the working at once, so cycling only teaches; Wren's row is filled and labeled unchanged from Season 3, so nothing hinges on it |
| Cost card pick | guessing (1 of 3); position; the common wrong answer "Pell, it makes more cloth" | fixed order unrelated to the answer; the answer changes (Wren, Neither, Wren); Pell gets its own reply on absolute vs comparative advantage; not scored |
| Predict | guessing | commit-then-see, no score; the reveal explains both answers |
| Best alone marker | sweeping the slider | allowed: it is exploring, not the code's skill; it just marks 120 |
| Check case | random pins; one-sided pins; pins from the start state; a short or empty sentence; pinning only money rows | needs a pin from each island, a gain and a loss, a Jobs, Wages, Rights or Reef pin, pins taken with the chosen policy on, and 15 words; pins show on the sheet verbatim for the teacher. It checks structure, not the argument; the screen says so ("This checks that your case uses evidence from both islands and both sides, not whether it is right"). Both stances pass. |
| Factory choice | none (computed); a student cannot force a move | the table above; ties stay |

## Heard in order
Grade 12: none required by grade. Rules that must hold: Wren's reply plays before the both-better line when one Offer
causes both; the predict reveal plays after the both-better line, never instead of it; a newer Offer drops older
replies not yet started.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Ricardo, 1817: Portugal needed fewer workers for both cloth (90 vs 100) and wine (80 vs 120), yet both gained | Ricardo, Principles of Political Economy and Taxation, ch. 7 (Econlib) | Britannica, "Comparative advantage" | yes |
| Gains need different opportunity costs; the trade price falls between them; equal costs, no gain | OpenStax, Principles of Economics 3e, ch. 19 | Krugman, Obstfeld and Melitz, International Economics, ch. 3 | yes |
| A tariff raises the home price: buyers lose, home producers and the treasury gain, net loss; exporters abroad lose | OpenStax, Principles of Economics 3e, ch. 20 | Krugman, Obstfeld and Melitz, ch. 9 | yes |
| A big buyer's small tariff can gain at its partner's cost; both together lose | Krugman, Obstfeld and Melitz, ch. 9 (large-country tariff) | Broda, Limao and Weinstein, "Optimal Tariffs and Market Power," AER 98(5), 2008 | yes |
| A stronger currency hurts exporters and import-competing producers, helps buyers of imports | OpenStax, Principles of Macroeconomics 3e, ch. 29 | CRS Insight IN10230 (2015), on the franc | yes |
| Swiss franc: cap 1.20 per euro from Sept 2011 dropped 15 Jan 2015; franc jumped; exporter shares fell | CRS Insight IN10230 | ANSA, "Switzerland scraps franc's cap against euro," 15 Jan 2015 | yes |
| Washers 2018: prices up nearly 12%, dryers too, about 1,800 jobs, more than $800,000 a job | Flaaen, Hortacsu and Tintelnot, AER 110(7), 2020 (AEA research highlight) | UChicago News, "What washing machines can teach us about the cost of tariffs" (2019) | yes ($815k and $820k both appear, so "more than $800,000") |
| Cambodia, 1999: US textile deal gave 6% more clothing quota a year plus a bonus of up to 14% a year if factories met labor law | USTR press release, "U.S.-Cambodian Textile Agreement Links Increasing Trade with Improving Workers' Rights," January 2002 (6% normal increase; bonus raised "from 14 to 18 percent" in the renewal; Cambodian labor law and core labor standards) | Cambodia Daily, "US Delay on Garment Quota Irks Minister" (agreement signed January 1999; "automatic 6 percent increase"; "bonus quota of up to 14 percent per year if labor conditions are satisfactory") | yes |
| The ILO monitored the garment factories under the deal and made its findings public; the program, Better Factories Cambodia, went on after the quotas ended | ILO feature, "New trade regime in textiles and clothing: How Cambodian factories improved their image" (deal laid the foundation in 1999; surprise inspections, results made public; all export factories must register with Better Factories Cambodia) | Maquila Solidarity Network archive, ILO garment sector project (born from the US-Cambodia Textile Agreement; ILO-trained monitors inspect registered factories) | yes (start year differs, 2000 or 2001, so the card names no start year) |
| Textile dyeing wastewater pollutes rivers and coasts where rules are loose | UNEP, Sustainability and Circularity in the Textile Value Chain (2020) | Kant, "Textile dyeing industry an environmental hazard," Natural Science 4(1), 2012 | yes |
| Workers displaced by import competition earn less for years after | Autor, Dorn and Hanson, AER 103(6), 2013 | Autor, Dorn, Hanson and Song, QJE 129(4), 2014 | yes |
Backed twice: 11. Cut: the washers' consumer cost ($1.5 billion and $1.2 billion both appear); a "20% of industrial
water pollution" textile figure (disputed); the 2022 WTO ruling on the washer tariffs (one source found); the year
ILO monitoring began in Cambodia (2000 and 2001 both appear); the bonus Cambodia was actually granted each year
(5%, 9% and 14% appear for different years); the claim that it was the first trade deal to tie labor to market
access (one source found).
Number checks (Python: isl_final.py, policy.py, tune.py, final.py in the spec agent's session scratchpad folder `ti`,
not in the repo): every Islands value
above, including best-alone splits, the reference deals, 181,800 split-and-deal combos per season (both-better
597 in S2, 0 in Storm, 1,931 in Motor boats; 0 at the alone split; accepted price range 1.07 to 1.92 fish a cloth in
S2 and 1.07 to 2.9 in S4), random mashing 0.3%; the policy model solved for every lever combination (cloth imports stay
7 or more, so the tariff never flips trade), groups, jobs, reef and the move table; tariff 0.5 both islands -0.5 and
tariff 1 -10.8 together; contrast ratios as in Look.

## Done when
1. On load the strait and bars are the biggest thing; the slider moves tokens and bars at once; 60 fishers shows 120.
2. Season 2 at 90 fishers, Send fish 150, Get cloth 100: Wren accepts with 18 fishers; Pell 130, Wren 62; banner on.
3. The same deal at 60 fishers leaves Pell at 70 with no banner; Storm has no deal that lights it.
4. Cost card: Season 2 answers 2, 1, Wren; Storm 1, 1, Neither; the Pell reply names absolute vs comparative.
5. Moving the slider or tapping Offer during the boat crossing acts at once.
6. Policy: each lever's reference outputs match Content; a currency move hides both Growth totals with the note.
7. Factory May move: Basic/Loose moves (Wren reef 82); Strong/Strict stays with the stays line; tariff 1 keeps it home.
8. Check case fails one-island pins, no loss pin, money-only pins and a 14-word sentence; passes a complete case.
9. At 1366x768 every mode's focus and controls fit with no page scroll; at 680x425 the listed folds happen.
10. Each how line is heard once in five actions in a row; Wren's reply plays before the both-better line.

## Open questions
- Sensitivity review (rule 5 and rule 11): the nine people images and the two invented island cultures (no real
  culture's dress or buildings).
