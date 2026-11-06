# The Buyout

## One idea
Sell phone chargers against three rivals, then sell to the same shoppers after you have bought all three, and watch
what a missing rival changes (a price rise that used to send buyers to a competitor now just makes you money), then
replay the buyout as the regulator and find that "best for buyers" and "best for everyone" pick different remedies.

## Not like
- concert-ticket-market (family sibling, built): one seller facing a demand curve, shortages and price caps on a stage;
  here four sellers then one, measured by market share and HHI, and no supply and demand graph at all.
- snow-season-prices (family sibling): one shop as weather, a rival and wages move demand and costs week by week; here
  the shock is ownership itself, the same quarters played twice.
- baron-or-builder: judges real Gilded Age people with evidence cards; here a fictional market you run, with real cases
  only as remedy precedents.
- stock-market-1929: one investor riding a real price series; here a firm setting price, quality and research.
- one-more-hour, fed-chair, trade-island: marginal choice, monetary policy and trade; none has market structure.

## Who and how
Grade 12, social studies (Economics: market structures and business). Driver: students on their own laptops (solo by
default); a teacher can project Compare and Regulator for discussion. 30 to 45 minutes (Rivals 8, Buyout 8, Compare 8,
Regulator 12 or more). Standards: D2.Eco.4.9-12, D2.Eco.5.9-12, D2.Eco.6.9-12, D2.Eco.7.9-12. No personal prompts.
All brands, numbers and shoppers are a teaching model; the real cases are real.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.4.9-12 (evaluate how much competition exists among sellers and buyers) | In Compare, rate each run's sellers on the HHI ladder and rate the buyers; run the Switch test | Both HHI gauges with the 1,800 line; switch results: 49% of your buyers left (8,033 to rivals), 17% left after the buyout (all went without) | Rating Rivals "not highly concentrated" gets the 2,500 explanation; all three ratings must be made before Switch test results unlock the evidence chips |
| D2.Eco.5.9-12 (describe consequences of competition) | Play both runs, then mark the 3 rows of the Compare table that changed most for buyers | Side by side: price, shoppers served, buyer gain, quality, newest model, sellers, your profit; the profit-seeking owner's dashed line | Marking needs 4 or more quarters in each run (or Finish); the 3 marked rows become memo evidence chips with both runs' numbers |
| D2.Eco.6.9-12 (generate explanations for a government role) | In Memo, pick 1 or 2 reasons the government might step in, then write their own explanation in a sentence | Four reason chips (market power, a barrier to entry, lost trades, the owner's savings) and a sentence box | Check memo fails if no reason fits the first remedy, or the sentence has fewer than 12 words |
| D2.Eco.7.9-12 (benefits and costs of policies) | Open at least 2 remedies besides Do nothing, switch Buyers' view and Everyone's view, rank a first and second remedy | Ledger: buyer gain, owners' profit, government cost, everyone's total, side effects, each vs Do nothing | Check memo needs a view, two different ranked remedies, and one ledger evidence chip for the first remedy |

## Screens and modes
Header: title "The Buyout" with the small Ohmly box art at its left; `.seg` mode buttons **Rivals**, **Buyout**,
**Compare**, **Regulator**; icon buttons Motion (`motion`), Sound (`sound`), Read (`read`). Kit stage plus panel; at
1366x768 the stage is about 896 wide and the panel 470. Under about 900 px tall the panel goes buttons-first.

**On load:** Rivals, quarter 1 of 8, nothing played. The shelf shows four boxes at $16 each with "Preview" on the
shopper lane (the shares the coming quarter will have if nothing changes). Hint: "You run Ohmly (the violet box). Set
your price, quality and research, then press Next quarter." The welcome is queued for the first tap. First tap on
Price, Quality or Research changes the preview at once; first tap on **Next quarter** plays quarter 1 (the welcome may
be cut; the hint keeps the premise). Focus goes to the Price slider on load (`preventScroll`).

### Rivals (opens here)
- Focus: the shelf. Four boxes (Ohmly, Tidewatt, Sparrow, Kite) on the painted shelf, each with its price tag, watts
  label and quality stars in code over the blank tag strip, and a share bar under it (number on the bar). Your box has a
  violet "You" tab. Below the shelf, the shopper lane: 20 painted shoppers, each standing for 5,000 shoppers.
- Layout at 1366x768, all above the fold: shelf about 896x420; shopper lane about 896x110; quarter strip about 896x150
  (a small chart of your price and your share, Q1 to Q8, plus rival launch markers). Panel, top to bottom: hint;
  "Your choices" (Price slider $10 to $40 in $1 steps with - and + buttons and the value; Quality as 5 buttons
  Flimsy, Basic, Solid, Sturdy, Premium with stars; Research as 3 buttons None $0, Steady $30k, Fast $60k with the lab
  readout "Lab: 35 of 100 to the 30 W model"); **Next quarter** (big) and **Play to the end**; "This quarter" readouts
  (your buyers, share, profit, total profit); "Competition" gauges (sellers, largest share, HHI bar with a marked
  1,800 line, and the fixed buyers line "100,000 shoppers, each buys at most one; none can move the price").
- At 680x425: the quarter strip folds away; the Competition section becomes one line ("4 sellers, top 25%, HHI 2,500");
  shopper figures shrink but stay 20. Choices and Next quarter stay visible.
- Each quarter: rivals post their prices first (shown on the shelf before you choose), you set yours, the preview
  updates on every input, **Next quarter** commits. Shoppers walk to boxes in proportion to shares (largest remainder
  rounding to 20); the rest walk past with the old-charger icon over them ("kept an old charger").
- After quarter 8: **Next quarter** becomes **Run again** (inline confirm "Clear this run? Yes / No") and the hint says
  "Two years done. Open Buyout or Compare."

### Buyout
- Same shelf, same 8 quarters from the same start, same 100,000 shoppers a quarter. A banner over the shelf top (code,
  not modal): "Ohmly owns all four brands." Every box gets an "Owned by Ohmly" ribbon; all four tags show one price.
- Controls as in Rivals, but your choices apply to all four brands. Merger savings: your unit cost is $0.50 lower (one
  shared factory), and one lab serves all four brands. Defaults are the Rivals defaults ($16, Solid, Steady), so the
  student finds the price rise themselves. The Competition gauges show 1 seller, 100%, HHI 10,000.
- The quarter strip adds a dashed grey line "a profit-seeking owner" (the Do nothing path in Content) after the student
  plays quarter 1, so a generous student still sees what the market allows.
- Fold at 680x425 as in Rivals.

### Compare
- Focus: the split screen. Two columns (teal "Rivals", coral "Buyout"), each with a mini shelf (the painted shelf at
  about 430x190 with that run's last-played tags and share bars) over a measures table: average price paid, shoppers
  served (total), buyer gain (total), your profit (total), quality (latest), newest model, sellers, largest share, HHI.
  Under both, a chart of average price by quarter: teal, coral and the dashed grey profit-seeking owner line.
- A column with fewer than 8 quarters shows "Q5 of 8" and **Finish with these settings** (plays the rest at once with
  that run's current choices, no animation).
- Panel: "Rate the competition" (Rivals sellers, Buyout sellers: three buttons each, Under 1,800 / Over 1,800 / One
  seller, 10,000; Buyers in both runs: Many small buyers / A few big buyers); **Switch test** (enabled when all three
  ratings are in); "Mark 3 changes for buyers" (tap rows in the tables; both rows of a measure highlight together).
- At 1366x768 the two columns, the chart and the whole panel fit with no scroll. At 680x425 the chart folds away and
  the tables show the five buyer rows first (price, served, buyer gain, quality, newest model).

### Regulator
- Premise in the hint and Read: "You are the regulator. Ohmly has bought its three rivals. Each remedy replays the same
  two years with a profit-seeking owner." The student's own runs are not replayed; the remedies use the model players.
- Focus: the ledger. Top: 5 remedy buttons, each a painted vignette 4:3 (about 160x120) with its name in code under it:
  **Do nothing**, **Block it**, **Break it up**, **Price cap**, **Common charger**. Center: a chart of buyer gain by
  quarter, the chosen remedy (violet) against Do nothing (dashed grey). Below: the ledger table (rows in Content) with
  columns Do nothing, the chosen remedy, Difference. Under the ledger, a case card (real case, two lines) and the
  side-effect line.
- Panel, page 1 "Remedies": hint; View toggle **Buyers' view** / **Everyone's view** (highlights the matching total row
  and sorts a small "rank" list of the remedies opened so far); the Price cap slider ($16 to $30, $2 steps, default
  $18) shown only when Price cap is chosen; "Opened: 2 of 5". Page 2 "Memo" (panel tabs **Remedies** / **Memo**, paged,
  never a scroll panel): reason chips (pick 1 or 2), evidence chips (pick 2), First remedy and Second remedy pickers,
  view, a sentence box, **Check memo**, **Save on this device** with "Your memo stays on this device. Nothing is sent."
- At 1366x768 vignettes, chart, ledger and the panel page fit. At 680x425 the chart folds away and the case card
  becomes a "Real case" button that swaps it into the ledger's place.
- What the picture shows for every outcome (each different at a glance): Do nothing, one gold owner bar and a line that
  steps up with each price rise; Block, four colored share bars stay on the mini shelf strip and the line rises gently;
  Break it up, one bar until Q4 then two (a fence icon at Q5); Price cap, a flat line under a red cap bar and the
  quality stars on the shelf strip dropping to one star; Common charger, two new grey-boxed entrants (Nova, Brisk)
  appear on the strip at Q3.

## Content
**Model (the builder implements exactly this; reference outputs below).** 100,000 shoppers a quarter, 8 quarters.
Each shopper buys one charger or none. Logit choice: value of a box = 10 + quality value + 4 x model step - price,
spread $5 (share_j = e^(v_j/5) / (1 + sum of e^(v/5))); "none" has value 0. Quality value and unit cost by stars:
Flimsy 0 / $6, Basic 4 / $8, Solid 7 / $10, Sturdy 9.5 / $13, Premium 11.5 / $16. Models: 20 W, 30 W, 45 W, 65 W
(steps 0 to 3). Fixed cost $60,000 per brand per quarter. Research: None $0 (0 points), Steady $30,000 (35), Fast
$60,000 (55); each 100 points launches the next model from the next quarter; at 65 W research costs nothing and the
buttons disable ("65 W is the top model in this market"). Profit = (price - unit cost) x units - fixed - research.
Buyer gain for a quarter = 100,000 x 5 x ln(1 + sum of e^(v/5)) dollars (what shoppers valued minus what they paid).
HHI = sum of squared owner shares of units sold (in percent).

**Rivals AI (Rivals mode):** Solid quality; research Tidewatt Steady, Sparrow Fast, Kite None. At each quarter's
start, Tidewatt, then Sparrow, then Kite each sets the whole-dollar price ($10 to $40) that maximizes its own profit
against the prices posted last quarter (ties go to the lower price). Q1 prices are all $16.
Reference, student at $16 / Solid / Steady: shares 25, 25, 20.7, 32.4, 25.4, 25.4, 28.1, 28.1%; your total profit
$0.41M; HHI 2,500 at Q1 to 3,127 at Q8; average price $16.00 to $17.00; launches Sparrow 30 W Q3, 45 W Q5, 65 W Q7;
Tidewatt 30 W Q4, 45 W Q7; you 30 W Q4, 45 W Q7; Kite stays at 20 W.

**Remedies (Regulator; all AI).** Owners' research: each owner tries None, Steady and Fast and keeps its most
profitable 8-quarter result (it comes out Fast in every default case). Each quarter every owner, in alphabetical order,
takes 6 rounds of best-reply pricing; only the capped owner also picks quality (Flimsy to Premium).
| Remedy | What happens | Government cost | Case card |
|---|---|---|---|
| Do nothing | One owner, 4 brands, $0.50 savings | $0 | none; the savings note (Williamson) |
| Block it | 4 separate firms as in Rivals, Ohmly Steady, no savings | $0.5M court case | Staples and Office Depot, 1997 |
| Break it up | Monopoly Q1 to Q4 (the case takes a year), then two owners (Ohmly + Tidewatt, Sparrow + Kite), $0.25 savings each, Steady each | $1.5M | Standard Oil 1911; AT&T 1984 |
| Price cap | Owner's price may not exceed the cap; owner picks quality | $0.4M monitoring | British Telecom price cap, 1984 |
| Common charger | Owner pays $0.3M once to redesign; from Q3 two entrants (Nova, Brisk) sell compatible chargers, Solid, Steady, starting at 20 W | $0.3M | EU common charger rule |

Reference totals over 8 quarters (buyer gain / owners' profit / government cost / everyone's total = buyer + owners -
government; then Q1 to Q8 price, quality at Q8, newest at Q8, sellers at Q8, shoppers served):
- Do nothing: $4.82M / $6.89M / $0 / $11.71M; $22 to $30 ($22, 22, 24, 24, 27, 27, 30, 30); Solid; 65 W; 1; 555,374.
- Block it: $9.36M / $2.02M / $0.5M / $10.87M; $16.00 to $17.30; Solid; 65 W; 4 (HHI 3,183); 713,856.
- Break it up: $7.53M / $4.63M / $1.5M / $10.66M; $22 to $19 at Q5, $19.65 at Q8; Solid; 65 W; 2 (HHI 5,050); 630,218.
- Price cap $18: $6.54M / $5.00M / $0.4M / $11.14M; $18 flat; Basic Q1 to Q4 then Flimsy Q5 to Q8; 65 W; 1; 628,304.
- Common charger: $8.25M / $3.55M / $0.3M / $11.50M; $22, then $19.10 at Q3, $21.33 at Q8; Solid; 65 W; 3; 663,506.
- Cap sweep (buyer / everyone): $16 7.21 / 11.05, $18 6.54 / 11.14, $20 6.35 / 11.56, $22 5.58 / 11.26, $24 5.78 /
  11.81, $26 5.13 / 11.42, $28 5.14 / 11.56, $30 4.82 / 11.31 ($30 never binds below the owner's own path except Q8).
  Quality falls to Flimsy by Q8 at every cap of $22 or less.

Rankings the ledger shows: Buyers' view, Block 9.36 > Common charger 8.25 > Break it up 7.53 > Price cap 6.54 > Do
nothing 4.82. Everyone's view, Do nothing 11.71 > Common charger 11.50 > Price cap 11.14 > Block 10.87 > Break it up
10.66. A note under Everyone's view: "Here the owner's savings and one shared lab outweigh the lost sales over two
years. Williamson (1968) showed this can happen. Critics answer that promised savings often do not arrive (the Staples
judge found many claims poorly documented) and that the harm to buyers is real money."

Ledger rows: Buyer gain, Owners' profit, Government cost, Everyone's total, Average price (Q8), Quality (Q8), Newest
model (Q8), Sellers (Q8), Shoppers served, Side effect. Side-effect lines: Do nothing "Prices rise with every new
model; 158,482 fewer chargers sold than with rivals." Block it "The $0.50 savings never happen, and four labs pay for
the same research." Break it up "A year of monopoly first; two sellers price lower but not as low as four." Price cap
"Prices stay down, so the owner builds cheaper chargers to keep its margin." (at $28 and $30: "This cap barely binds,
so little changes.") Common charger "New makers need two quarters to arrive and start a model behind."

**Switch test (Compare):** at quarter 1 settings (Solid, 20 W). Rivals: your price $16 to $20 loses 10,225 of 20,752
buyers (49%); 8,033 go to rivals, 2,192 go without; your quarterly profit falls $64,514 to $45,277. Buyout: one price
$16 to $20 loses 14,306 of 83,009 (17%), all go without; profit rises $299,561 to $481,387.

**Ratings feedback (Compare):** Rivals sellers: correct "Over 1,800": "Four equal sellers already make 2,500. The 2023
US merger guidelines call that highly concentrated, yet the switch test shows your buyers still had somewhere to go.
Both are true." Wrong "Under 1,800": the same text opens with "Not quite." Buyout: "One seller, 10,000": "The buyout
added 7,500 points. The guidelines presume harm from a merger that adds more than 100 in a market over 1,800." Buyers:
"Many small buyers": "100,000 shoppers, each buying one charger. No buyer can bargain the price down in either run;
what changed is the sellers." Wrong choices get the same text after "Not quite." No score.

**Memo:** reasons: "One seller can set the price (market power)"; "A locked port keeps new makers out (a barrier to
entry)"; "Shoppers who would pay more than a charger costs go without (lost trades)"; "The buyout's savings are worth
more than the harm (savings)". Fits: Block and Break up, power or lost trades; Price cap, power or lost trades; Common
charger, barrier or power; Do nothing, savings. Evidence chips: the 3 marked Compare rows ("Average price: $X
with rivals, $Y after the buyout", X and Y from the student's own runs), the two switch results, and for the first
remedy its ledger rows (difference vs Do nothing). Check memo lists each part as done or "Fix:" with the reason (for a
misfit: "A price cap does not open the port. Pick a reason this remedy acts on, or another remedy."). Save stores the
memo text and picks under `curio-the-buyout-memo`, wrapped in try/catch.

**Case cards** (two lines each): Staples and Office Depot (1997): "The FTC sued to stop the two office superstores
from merging. A federal judge blocked the deal after evidence that prices were lower where both had stores." Standard
Oil (1911): "The Supreme Court ruled Standard Oil had broken the Sherman Antitrust Act of 1890 and ordered it split
into more than 30 companies." AT&T (1984): "The Justice Department sued in 1974; AT&T agreed in 1982 and in 1984 split
off seven regional phone companies, keeping long distance." British Telecom (1984): "A 1983 report by Stephen
Littlechild set a cap: prices could rise by inflation minus 3 points a year, with service quality watched by the
regulator." EU common charger: "Directive (EU) 2022/2380 made USB-C the common port for phones and other small devices
sold in the EU from 28 December 2024, and for laptops from 28 April 2026, so any USB-C charger works."

**Innovation note** (Compare, beside the newest model row): "In this model the owner keeps launching new models, and
raises the price with each one. Economists disagree here: Schumpeter argued big firms innovate more; Arrow argued a
monopoly gains less from replacing its own product. A 2021 study found drug projects bought by a company with an
overlapping drug were less likely to be developed."

## Interactions in detail
- Preview is exact: rivals have posted, so the share bars, the "Preview" lane and the readouts for the coming quarter
  change on every slider input. Nothing waits for an animation.
- **Next quarter** computes at once; readouts and the quarter strip update on the press. The shopper walk then plays
  1.4 s (Motion off: figures jump to their places). A tap during the walk acts at once; a second Next quarter cuts the
  walk to its end state and plays the next quarter.
- **Play to the end**: plays the remaining quarters 1.2 s apart (at most 9.6 s), becomes **Pause** while running;
  every control stays live and a change applies to the next quarter computed.
- Extremes: $40 with rivals sells about 215 chargers a quarter (0.3% of sales); your box gets a "Buyers are walking past"
  tag and one event line per run. Price $10 sells half the market but loses $0.72M over the run (fixed costs). Profit
  readouts show negatives with a minus sign and the word "loss". At 65 W the research buttons disable.
- Switching modes keeps each run where it was. Run again clears only that run. Compare and the memo use whatever has
  been played; Finish with these settings fills the rest.
- Regulator remedies are computed once on load (deterministic, no randomness) and the cap's 8 values on first use.
- Keyboard: slider arrows move $1, Page keys $5; every button is reachable in panel order before the shelf.

## Look
Band theme `kit/theme-912.css`. `--brand` violet `#b3a6ff` (8.09:1 on `--panel` `#141b25`, 8.78:1 on `--paper`;
button text `#16102e` on it 8.55:1). Run colors: Rivals teal `#4fd1c5` (9.28:1 on panel), Buyout coral `#ff8f7a`
(7.80:1), profit-seeking owner dashed grey `#8a96a8` (5.78:1), HHI 1,800 line gold `#f2c14e` (10.31:1). Brand boxes:
Ohmly violet, Tidewatt teal, Sparrow amber, Kite green, each also with a code mark on its tag (circle, wave, triangle,
diamond) so color is never the only signal. Shelf tags: ink `#1a1a1a` on `#f4f1ea` (15.43:1). Warm store light in
the painted shelf against the dark instrument panel; differs from concert-ticket-market's stage orange and
stock-market-1929's ticker green.

## Art
- shelf: front view of a store aisle shelf with three empty wooden-and-metal shelves, blank white price-tag strips,
  a blank header sign, warm overhead store light; 16:9; no cutout; people no; Rivals and Buyout stage, Compare minis.
- box-ohmly, box-tidewatt, box-sparrow, box-kite: a retail phone-charger box standing upright, front view, a clear
  window showing a white charger brick, a blank solid front panel in violet / teal / amber / green; 3:4; cutout yes;
  people no; on the shelf at about 150 px wide, whole box visible in every mode, names and watts in code.
- box-nova, box-brisk: the same box in plain grey with a blank white panel; 3:4; cutout yes; Regulator strip only.
- shopper-1 to shopper-6: one shopper walking in side view holding a phone, varied ages, skin tones, clothing and one
  using a cane; 9:16; cutout yes; people yes (Gemini, Cory's contact sheet); shopper lane, about 34 px wide at
  1366x768, whole figure visible; a stopped pose is the same image (no second pose needed).
- old-charger: a worn white charger cable coiled loosely, slightly frayed; 1:1; cutout yes; people no; icon over
  shoppers who buy nothing.
- remedy-nothing: an open factory gate with a delivery truck rolling out at dawn; remedy-block: the same factory road
  with a striped barrier gate lowered across it; remedy-breakup: one factory yard split by a new fence into two yards,
  each with its own gate; remedy-cap: a large blank paper price tag held down under a steel bar; remedy-standard: a
  phone, an earbuds case and a tablet side by side, each with the same oval charging port, one cable; all 4:3; no
  cutout; people no; Regulator buttons, cropped whole at about 160x120.
14 images plus 6 people images. The header icon reuses box-ohmly.

## Voice
Bank `news-reader` ("Say clearly and steadily, like a trusted radio news reader"): a business-news read for a market
story; concert-ticket-market has no voice and stock-market-1929 uses hs-narrator. `Curio.voice`, scope = mode. Readouts
and tables are read on screen; Read speaks the hint.
- welcomeRivals (how, Rivals welcome, stale once quarter 1 is played): "Four makers sell phone chargers on this shelf,
  and you run Ohmly, the violet box. Set your price, then press Next quarter to see who buys."
- welcomeBuyout (how, whole, Buyout welcome, stale once Buyout quarter 1 is played): "Ohmly has bought Tidewatt,
  Sparrow and Kite. Same shoppers, same two years, but now one price covers every box. Press Next quarter."
- welcomeCompare (how): "Both runs, side by side. Rate the competition in each run, then tap Switch test."
- welcomeRegulator (how): "You are the regulator now. Tap a remedy to replay the buyout with it, then weigh its
  benefits and costs."
- launch lines (event, when that model reaches the shelf in Rivals or Buyout, dropped if the quarter has moved on):
  "Sparrow puts a 30 watt charger on the shelf." / "...45 watt..." / "...65 watt..."; "Tidewatt puts a 30 watt
  charger on the shelf." / "...45 watt..."; "Your lab ships a 30 watt Ohmly." / "...45 watt..." / "...65 watt...";
  Buyout: "Your lab ships 30 watt chargers for all four brands." / 45 / 65. Each is a full fixed line in lines.json.
- walkingPast (event, once per run, when your Rivals share falls under 10%): "Shoppers are walking to your rivals.
  Your price or your charger is behind theirs."
- noSwitch (event, once per Buyout run, the first quarter played above $16): "Shoppers who leave now have no rival
  to go to. They keep an old charger instead."
- runDone (event, whole, at quarter 8 of either run): "Two years are done. Open Compare to set this run beside the
  other."
- switchResult (event, whole, on Switch test): "With rivals, a four dollar rise lost half your buyers, most of them to
  rivals. As the only seller, it lost about one in six, and profit went up."
- remedy lines (event, on choosing a remedy, stale when another is chosen): Do nothing "The buyout goes ahead. Prices
  climb with every new model." Block "The deal is blocked. Four sellers keep prices near sixteen dollars." Break up "A
  year in court, then two sellers. Prices fall, but not to where four sellers kept them." Price cap "The cap holds
  prices down, so the owner builds cheaper chargers to keep its margin." (cap $28 or $30: "This cap barely binds, so
  little changes.") Common charger "Any maker can now fit the port. Two new makers arrive in the third quarter."
- memoOk (event): "Your memo holds together. Save it, or try another remedy." memoFix (event): "Some parts need work.
  The list shows what to fix."
How lines play once each, then hint only. No line names a disabled control (Switch test is named only after the three
ratings; Next quarter never after quarter 8).

## Family engine
none. The market family has no kit engine (concert-ticket-market keeps its own code). The logit market model, AI
pricing and remedies live in this tool's src.html (BASELINE rule 13).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| HHI = sum of squared percent shares; 4 equal = 2,500, one seller = 10,000 | US DOJ, "Herfindahl-Hirschman Index" page | DOJ and FTC, Merger Guidelines (2023), section 2.1 | yes |
| 2023 Guidelines: over 1,800 is highly concentrated; a merger adding more than 100 there is presumed to harm competition | DOJ and FTC, Merger Guidelines (2023) | Congressional Research Service, LSB11138 (2024) | yes |
| Staples and Office Depot: FTC sued 1997, judge blocked it, prices lower where both competed; claimed savings poorly documented | FTC v. Staples, 970 F. Supp. 1066 (D.D.C. 1997) | FTC case page "Staples, Inc./Office Depot, Inc." | yes |
| Standard Oil: 1911 Supreme Court, Sherman Act 1890, split into more than 30 companies (counts of 33 and 34 both appear; the tool says "more than 30") | Standard Oil Co. of New Jersey v. United States, 221 U.S. 1 (1911) | Britannica, "Standard Oil" | yes |
| AT&T: sued 1974, agreed 1982, split off seven regional companies in 1984, kept long distance | Britannica, "AT&T" | United States v. AT&T, 552 F. Supp. 131 (D.D.C. 1982) | yes |
| BT price cap: Littlechild's 1983 report, RPI minus 3 from 1984, quality monitored | Littlechild, EPRG lecture on incentive regulation (Cambridge, 2024) | HKCER Letters vol. 12 (1992), on RPI-X | yes |
| EU common charger: Directive (EU) 2022/2380; USB-C from 28 Dec 2024, laptops 28 Apr 2026 | European Commission, "Common charger" page | Government of Ireland press release on the directive | yes |
| Innovation debate: Schumpeter (1942) vs Arrow (1962) | Arrow, "Economic Welfare and the Allocation of Resources for Invention" (1962) | Gilbert, "Looking for Mr. Schumpeter," Innovation Policy and the Economy 6 (2006) | yes (both describe the disagreement) |
| Acquired overlapping drug projects less likely developed | Cunningham, Ederer and Ma, "Killer Acquisitions," Journal of Political Economy 129(3), 2021 | Yale Insights summary of the study (2021) | yes |
| Cost savings can outweigh a merger's price harm in total welfare | Williamson, "Economies as an Antitrust Defense," AER 58(1), 1968 | OECD, "The Standard for Merger Review" roundtable (2011) | yes |
Backed twice: 10. Cut: the EU's e-waste tonnage and euro savings figures (found in one source only); "34 companies"
(sources disagree, so "more than 30"); a "most mergers are allowed" line for Do nothing (not backed twice).

Number checks (Python, `S:/CurioClass-codex-scratch/specs/the-buyout/`: sim.py, runs.py, remedies.py, checks.py,
switch.py, capres.py, contrast.py), all on the model above:
- Rivals price sweep, Solid / Steady: total profit $14 0.26M, $16 0.41M, $18 0.41M, $20 0.29M; $10 -0.72M; $40
  -0.65M (share 0.3%). Overcharging and pricing at cost both lose; the rivalry price wins.
- Rivals research: None 0.21M (share falls to 8.1% by Q7), Steady 0.41M, Fast at $17 0.79M. Skipping research is
  punished with rivals. Quality: Flimsy at $16 -0.11M, Premium at $16 -0.72M, Solid best.
- Buyout: kept at $16 the owner makes 2.49M and buyers 9.60M (a generous owner can match rivals; nothing makes it,
  hence the dashed reference). Best whole-dollar price at Solid, 20 W: $22 ($504,238 a quarter); $40 loses 0.04M.
  Do nothing owner research: None 4.03M, Steady 5.61M, Fast 6.89M, so Fast is chosen.
- Quality cut at the same price: Solid to Basic loses 39% of your buyers with rivals, 25% after the buyout; cutting
  quality loses money in both, so the tool never claims a monopoly cuts quality unless capped.
- Remedies and cap sweep: the tables in Content. Best-reply pricing converged (same results at 6, 12 and 20 rounds).
  A cap of $12 or $14 would match Block for buyers only by selling Flimsy chargers all two years, so the slider starts
  at $16 and the case card says real caps watch quality.
- Switch test numbers as in Content. Contrast ratios as in Look.

## Done when
1. On load, the shelf with four $16 boxes is the biggest thing on screen, and the first Next quarter plays quarter 1.
2. Rivals at $16 / Solid / Steady for 8 quarters ends with total profit $0.41M and HHI 3,127; $40 ends in a loss.
3. Buyout at $22 sells 59,539 a quarter (12 shoppers buy, 8 walk past on the lane); the dashed owner line appears.
4. Dragging Price during the shopper walk or during Play to the end changes the preview at once, and the next quarter
   uses the new price.
5. At 1366x768 every mode's focus and controls fit with no page scroll; at 680x425 the folds listed above happen.
6. Compare: ratings give the stated feedback; Switch test shows 49% / 8,033 to rivals and 17% / profit up.
7. Regulator: each remedy's totals match Content; Price cap at $18 shows Basic then Flimsy stars and the cap line.
8. Buyers' view and Everyone's view rank the remedies as listed, with the Williamson note under Everyone's view.
9. Check memo fails a misfit reason, a missing second remedy or an 11-word sentence, and passes a complete memo; Save
   shows the privacy line.
10. Each how line is heard once in five actions in a row; launch lines play when the model reaches the shelf.

## Open questions
- Settled (Cory, 2026-11-05): keep the clash as the lesson. Everyone's view ranks Do nothing first and Buyers' view
  ranks it last, with the short Williamson 1968 note and its critics. Do not lengthen the horizon to remove it.
