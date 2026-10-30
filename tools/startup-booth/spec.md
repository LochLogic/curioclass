# Startup Booth
Renamed from: Startup Tycoon

## One idea
Run a Saturday market booth for 12 weeks, and every price you try drops a dot on a "price vs. share who bought" chart, so the demand curve you could not see at the start appears from your own experiments; draw the break-even line over it and you can see which prices keep the business alive, then pitch an investor using only numbers your booth actually earned.

## Not like
- first-apartment-budget (9-12, built tycoon): a personal budget for a year of rent and surprises, graded out of 100. Here a business: price, unit cost and fixed cost, with no score, and the hero is a demand chart you build by testing.
- paycheck-decoder, compound-interest-head-start (9-12, this group): money you earn as a worker or save. Here money a business makes and loses each week.
- interview-simulator (9-12, this group): talking about yourself. The pitch here is about numbers, picked from your own run.
- market-time-machine (9-12, built): investing in index history. Here you are the business an investor might buy into.
- prototype-lab (9-12, this group): designing a product to pass tests. Here selling one to customers at a price.

## Who and how
- Grade 9-12, career and technical education, module "Entrepreneurship".
- Topic line: starting a small business and pricing for profit
- Driver: students on laptops, alone or in pairs (one reads the week report aloud). Teacher can project Numbers for a whole-class break-even talk. 30 to 50 minutes for a 12-week run and a pitch.
- Standards: CTE.Career Clusters.

## Screens and modes
Header: title, topic line, modes (`.seg`): `Run` (default), `Numbers`, `Pitch`; then `Read`, `Motion`, `Sound`.

**Run.**
1. Setup. Focus: the three booth cards, side by side. Each card shows its painted booth (Art), startup cost, unit cost, weekly fixed cost and the one lesson it is known for ("leftovers keep", "fruit spoils", "only 8 hours a week"). You start with $800 of summer job savings. Every class gets the same weeks by default (one fixed event schedule per booth, so a whole class can compare runs with no code to share); a `New weeks` button deals a different schedule, and a `Steady weeks` checkbox turns events off. `Open the booth` pays the startup cost.
2. Week screen. Focus: the demand chart, the largest thing on the stage (at least half its height at 1366x768), with the market band above it. Stage, top band: the painted market street (Art) with your painted booth (its sign text in code on the blank sign) and a crowd of simple dot figures drawn in code that fills to the week's visitors. Stage, below: the demand chart (step 4). Panel at the right with three decisions for this week:
   - Price: a stepper in the business's step ($1 for tees, $0.25 for smoothies, $5 for tune-ups), with the margin per item shown live ("You keep $9.00 of each $15 tee").
   - Make: how many to make (tees and smoothies), stepper of 5; the cost shows live and is capped by cash. Bike tune-ups have no batch, only the 8-hour cap.
   - Marketing: `.seg` $0, $25, $50, $100 (flyers, a school paper ad, posts with a paid boost).
   - `Run the Saturday`: the crowd walks past (2 seconds, instant with Motion off), a tally counts buyers, and the week report opens. A tap on the report area or `Next week` during the walk finishes it at once.
3. Week report card (over the market band): visitors, share who bought, sold, left over (and what happens to it), revenue, costs (making, booth, marketing), cash profit, cash now, hours you worked, profit per hour. If an event hit, its card (with its painted picture) is on top. `Next week`.
4. The demand chart, growing all run: x price, y share of visitors who bought, one dot per week labeled with the week number. After 3 dots at 2 or more different prices, `Show the trend line` draws the straight fit through the dots. A second layer, `Break-even`, draws the curve of the share you would need at each price to cover this week's fixed costs plus marketing for the visitors you had; dots above it made money. `Table view` shows the same dots as rows.
5. After week 12: the season card: total profit, startup cost earned back (the week it happened), total hours, profit per hour, the full demand chart and the cash line over 12 weeks. `Take it to Pitch` and `Run again`.

**Numbers.** Focus: the profit vs. units chart, centered and the largest thing. No simulation. One business's break-even on one chart: sliders for price, unit cost, weekly fixed costs and units sold; a profit vs. units chart with the fixed-cost line, the revenue line and the total-cost line meeting at break-even. Readouts: margin per item, break-even units (rounded up), profit at the chosen units. Presets load each booth's numbers.

**Pitch.** Focus: the slide being built, centered, with its three number chips under it. Uses your last finished run (or a sample run if none). Two parts:
1. The pitch builder: five slides (Who buys it, What it costs to make, What you keep, What happened in 12 weeks, What you'd do with $1,000). Each slide offers 3 number chips from your run, one right and two that are real numbers from the run but the wrong ones (revenue offered as profit, a single week offered as the season). Pick one per slide. Ms. Okafor, of the made-up Riverside Seed Fund, asks each slide's question aloud (shown as a name card, never drawn); a wrong pick gets her follow-up ("Is that what you kept, or what came in?") and a second try.
2. Three ways to pay for a second booth ($1,000): `Your savings` (cash after the season minus $1,000; no interest, smaller cushion), `A small-business loan` ($1,000 at 9% for 12 months), `Riverside Seed Fund` ($1,000 for 20% of the business). A table compares the first year if the second booth earns what the first did, and if it earns nothing.

## Content
**Booths** (all made up, all at the same Saturday market):
| | Inkwell Tees | Fresh Pour Smoothies | Spoke Doctor Tune-ups |
|---|---|---|---|
| Startup cost | $420 (heat press, screens, ink) | $300 (blender, cooler, cart) | $340 (stand, tools) |
| Unit cost | $6.00 a shirt | $1.90 a cup | $8.00 of parts a tune-up |
| Weekly fixed | $35 booth fee | $55 cart space and permit | $10 booth share |
| Base visitors | 25 | 70 | 6 |
| Marketing reach k | 4 | 6 | 1 |
| Top price (nobody buys) | $25 | $8 | $60 |
| Leftovers | keep to next week | spoil (thrown out) | none, 8 tune-ups a week max |
| Hours | 6 at the booth + 0.1 per shirt made | 5 + 0.05 per cup made | 1 + 1 per tune-up |

Unit costs and fees are made up but in a believable range for a teen side business in 2026; the tool says so on the setup card.

**Events** (about one every 3 weeks, never in week 1; the default schedule comes from seed 1 per booth, `New weeks` draws a new seed): Rain (visitors x0.3 for tees and smoothies; Spoke Doctor unchanged), Heat wave (smoothies x1.5), School spirit week (tees x1.5), Fall fair weekend (all x1.3), Blank shirt price up to $7.00 for 3 weeks (tees), Blender repair $45 (smoothies, a one-time cost), Flat-tire week after a nail spill at the bike rack (tune-ups x1.5).

**Pitch questions** (Ms. Okafor): "Who buys from you?", "What does one cost you to make?", "What do you keep from each sale?", "How did the 12 weeks go?", "What would $1,000 change?". Slide 5's chips are plans (second booth at the Sunday market, a bigger batch, more ads); she asks the follow-up "How many more would you need to sell to pay for it?" with three number chips.

## Interactions in detail
Model (all rounding half-up, money to the cent with the family `r2`):
- Visitors V = round((base + regulars + round(k x sqrt(marketing))) x event). Regulars start at 0 and grow by 0.1 x sold each week (kept as a decimal).
- Share who bought s = max(0, 1 - price / top price). Demand = round(V x s).
- Tees and smoothies: sold = min(demand, stock), where stock = leftovers + made. Tees leftovers carry; smoothie leftovers are thrown out. Tune-ups: sold = min(demand, 8), parts cost only for tune-ups done.
- Costs this week = made x unit cost (tune-ups: sold x unit cost) + weekly fixed + marketing. Cash profit = revenue - costs. Cash = cash + cash profit.
- Hours = booth hours + per-unit hours x made (tune-ups: x sold). Profit per hour = cash profit / hours, shown to the cent with "before taxes".
- Make is capped so cash after making and fixed costs stays at or above $0 (the stepper stops there and says "That's all your cash covers"). If cash cannot cover the fixed costs and marketing, the week becomes `Out of cash`: `Borrow $200 from family` (paid back from the next weeks' profit, shown as a line) or `Close the booth` (the season card shows where it ended). No shaming words; the card says "Lots of first businesses run short of cash. Here's where it happened."
- A leftover card for tees names the stock's cost ("17 shirts on the shelf, $102 at cost: the money isn't gone, it's on the shelf").
- The trend line is a least-squares fit of share on price through the week dots (events are drawn as hollow dots and left out of the fit, with a note). Break-even share at price p = (fixed + marketing) / (V x (p - unit cost)), drawn only where p > unit cost.
- Numbers mode: break-even units = ceiling(fixed / (price - unit cost)); "Never" when price is at or below unit cost.
- Pitch loan: the family `loanPay(1000, 0.09, 12)`; equity: 20% of the second booth's first-year profit (weekly average of the last 4 weeks x 52), plus a line "and 20% of the business if you ever sell it". The table shows both the "earns what the first did" and "earns nothing" columns, so the loan's fixed payments and the investor's shared risk are both visible. No row is labeled best.
- Events: the family `rng(seed)`; the same seed, booth and decisions give the same weeks on any machine.
- Run and its chart can be saved to localStorage (`Keep this run`, one slot) so Pitch can use it next class; `Clear` deletes it. Nothing else is stored.
- Sizes: below 760 px the stage sits above the panel and the market band shrinks to a strip over the chart; at 680x425 the band is a thin strip with the booth and the visitor count, and the chart fills the rest; at 375 decisions stack with `Run the Saturday` pinned.

**Worked checks** (Steady weeks on, $800 start):
- Tees, $15, make 20, $25 marketing every week. Week 1: V = 25 + 0 + 20 = 45, s = 0.40, demand 18, sold 18, 2 left; revenue $270, costs $180 (120 + 35 + 25), cash profit $90, cash $470, 8 hours. Week 2: V 47, sold 19, profit $105. From week 7 demand passes the 20 made and the batch is the limit. Season: 240 sold, profit $1,440, cash $1,820, 96 hours, $15.00 per hour; startup earned back in week 4 (90 + 105 + 120 + 120 = 435).
- Same plan at other prices (season profit): $10 $240, $12 $720, $15 $1,440, $18 $1,044, $20 $260. Make 30 at $15: $1,215. No marketing: $405. $100 marketing: $540.
- Rain in week 3 (tees, same plan): V 15, sold 6, cash profit -$90, 17 shirts left at $102 cost; those sell by week 11, so the season still ends at $1,440 (startup earned back in week 6 instead of 4).
- Smoothies, $5, make 40, $25: week 1 V 100, s 0.375, sold 38 (2 thrown out), profit $34; season $513, cash $1,013, 84 hours, $6.11 per hour; startup earned back in week 8. At $3 every week loses $36 until cash caps the batch (30 cups in week 11, 5 in week 12): the season loses $481.50 (cash $18.50). At $4 it makes $48; make 60 at $5: $467.
- Tune-ups, $35, $25 marketing: week 1 V 11, s 0.417, sold 5, revenue $175, costs $75, profit $100; season $1,470, 70 tune-ups, 82 hours, $17.93 per hour. At $30: $1,494 but 99 hours ($15.09); at $45: $1,023 in 51 hours ($20.06).
- Break-even at $15 tees with $25 marketing: (35 + 25) / 9 = 6.67, so 7 shirts a week.
- Pitch after the tees season: last-4-week average $120, so a second booth projects $6,240 a year. Loan: $87.45 a month, $49.40 interest. Seed Fund: 20% = $1,248. If the second booth earns nothing: the loan still costs $1,049.40 in payments; the Seed Fund gets 20% of nothing (and still owns 20%).

## Look
- theme-912 dark base (panel #141b25, sec-bg #18202b) with accent `--brand #b69cff` (soft violet: Run the Saturday, the active mode, week dots), `--brand-ink #1d1236`.
- Contrast: accent on panel 7.57:1, on sec-bg 7.18:1; brand-ink on accent 7.71:1.
- Booth awnings in the paintings: tees pink (about `#ff8fb1`), smoothies mint (about `#7ee0a1`), tune-ups yellow (about `#ffd166`), each with its name in code on the blank sign. The market painting is bright Saturday morning, a warm contrast to the dark chart. Chart: dots in accent; hollow event dots; trend line `#e8e4ff` dashed; break-even curve `#ffd166` with the word "break-even" at its end; money-made zone tinted.
- Differs from first-apartment-budget and market-time-machine (light cream papers) and from this batch's other dark tools (paycheck-decoder apricot, compound-interest-head-start spring green, Covered jade, hospital-shift periwinkle, prototype-lab orange).

## Art
Local FLUX (`scripts/localart.py`), one session, no people (the crowd is dot figures drawn in code because it is a count). Shared style line: "bright cheerful painterly illustration, Saturday morning light, an outdoor town market". Blank surfaces on every sign. Webp.
- sb-market: "an empty town market street on a Saturday morning with a row of white canopy tents, string lights, brick shopfronts and a paved walkway, (style)"; 4:1; cutout no; people no; the market band behind the booth and crowd.
- Booths (a kit of three; 1:1; cutout yes; people no; stands in the middle of the band, its base on the walkway line, 70% of the band's height; also on the setup cards): one shared prompt "a small market booth with a (color) striped awning, a blank white sign board on top and a folding table, (goods), plain white background, (style)": pink awning with folded printed t-shirts in stacks and a heat press; mint green awning with a blender, a cooler and rows of smoothie cups; yellow awning with a bicycle on a repair stand and a pegboard of tools.
- Event pictures (4:3; cutout no; people no; 240 px on the event card), one each: sb-rain "heavy rain on an empty market street with puddles and closed canopy tents, (style)"; sb-heat "a blazing sun over a market street with heat shimmer and a thermometer, (style)"; sb-spirit "school pennants and streamers in team colors hanging over a market street, (style)"; sb-fair "a small Ferris wheel and fair lights at the end of a market street, (style)"; sb-shirts "a cardboard box of plain blank t-shirts with a price tag showing a blank label, (style)"; sb-blender "a broken blender with a cracked jar and a wrench beside it on a counter, (style)"; sb-nails "scattered nails on the pavement beside a bike rack with a flat bicycle tire, (style)".
- 11 images, none with people. Drawn in code: the crowd dots, sign text, the demand and profit charts, the report and season cards, pitch slides and chips.

## Voice
Bank voice `easy-coach` (Umbriel), "Say in an easy-going, encouraging way, like a relaxed sports coach": a market manager who has watched a lot of first booths. Not used by another tool `neighbors.py` lists or by this batch; its other 9-12 users are math and health tools. Ms. Okafor's questions use the same voice (one speaker; her name card shows). `Curio.voice`, `scope: () => state.mode`.
- welcomeRun (how; on the setup screen; stale when a booth is opened): "Tap a booth card, then tap Open the booth."
- weekHow (how; at the first week; stale when Run the Saturday is tapped): "Set a price, how many to make and your marketing. Then tap Run the Saturday."
- weekDone (event; each report; stale on Next week): "(sold) sold. Cash profit (profit)."
- eventCard (event; when an event hits; stale on Next week): the event's one line, such as "Rain all morning. Not many people out."
- chartHow (how; after week 3 with two prices; stale when the trend line is shown): "Your dots are a demand curve. Tap Show the trend line."
- outOfCash (event; stale on a choice): "You're out of cash for this week. Tap Borrow from family, or Close the booth."
- seasonDone (event; after week 12; stale when Pitch or Run again is tapped): "Twelve weeks done. Look at your chart before you change anything."
- welcomeNumbers (how; on entering Numbers; stale when a slider moves): "Drag the sliders and watch where the lines cross."
- welcomePitch (how; on entering Pitch; stale when a chip is tapped): "Tap the number from your run that answers each question."
- okafor1 to okafor5 and follow-ups (event; stale on the next slide).

## Family engine
money (described in full in paycheck-decoder): `money`, `r2`, `loanPay`, `rng` and `newSeed` for the event schedule. No tax lines: the season card says "before taxes" and links to paycheck-decoder for how pay is taxed.

## Sources
- Startup costs, break-even and the parts of a business plan: U.S. Small Business Administration, "Calculate your startup costs", "Write your business plan" and "Fund your business" (loans vs. investors) (https://www.sba.gov/business-guide/plan-your-business), as of October 2026.
- Break-even formula (fixed costs / (price - variable cost)): SBA Learning Center, "Break-even analysis" (https://www.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs).
- Teen work hours: U.S. Department of Labor, YouthRules, for the note that self-employment rules differ from job rules (https://www.youthrules.gov).
- All booth costs, prices, demand numbers, events, Riverside Seed Fund and Ms. Okafor are made up for teaching; the setup card and season card say so. Data as of: October 2026 (made-up numbers checked against typical 2026 costs, no named suppliers).
- Checks run (Python, 2026-10-29, a week-by-week simulation of the model above with half-up rounding): every tees, tune-up, break-even and pitch check reproduces to the cent, and the loan is $87.45 a month ($49.40 interest). Fixed: smoothies at $3 were listed as losing $432 (cash $68), which ignores the spec's own cash cap; with the cap the batch drops to 30 and then 5 cups in weeks 11 and 12 and the season loses $481.50 (cash $18.50). Added: the rain week does not change the tees season total ($1,440), only the payback week (6). Removed the class code box (a code to pass between devices by hand); the fixed default schedule gives a class the same weeks with nothing to share.

## Done when
1. Every worked check above matches the tool to the cent with Steady weeks on.
2. The demand chart adds one dot per week; the trend line appears only after 3 dots at 2 or more prices; event weeks are hollow and left out of the fit.
3. The break-even curve is not drawn at or below unit cost; dots above it are the weeks that made money.
4. Smoothie leftovers are thrown out every week; tee leftovers carry with their cost shown; tune-ups never exceed 8.
5. Make cannot exceed cash; Out of cash offers borrow or close, and a closed run still reaches the season card.
6. With the default weeks, the same booth and decisions give the same events on two machines; New weeks changes them.
7. Numbers gives 7 shirts for $15, $6 unit cost, $60 fixed, and "Never" at $6.
8. Pitch uses the kept run's numbers; wrong chips are real numbers from the run; the loan shows $87.45 a month; no option is labeled best.
9. Focus: at 1366x768 and 680x425 the demand chart is the largest thing on the week screen, the profit chart in Numbers and the slide in Pitch.
10. Tap while it plays: Next week or the report tapped while the crowd walks finishes the walk at once and acts, with no stale line after.
11. Decisions, Run the Saturday and the week report are visible without scrolling at every STANDARDS.md size; chart dots have week labels and the chart has a table view; all 11 paintings load with no person or fake lettering.
12. How lines once each in five actions in a row; event lines every time, dropped when stale; Keep this run fills one localStorage slot and Clear empties it.

## Open questions
- Title: "Startup Tycoon" is taken by several games (itch.io, app stores). "Startup Booth" found no match. OK, or another name?
- The made-up costs and demand give $15 to $20 an hour at the best prices, before taxes. Too rosy for teens, or fine since the bad prices show losses?
- The Seed Fund deal is simplified to "20% of profit and 20% of a sale". Enough for 9-12, or add a line on valuation ($1,000 for 20% means the fund values the business at $5,000)?
- The class code box is gone (a code to pass by hand); a class now shares one fixed default event schedule, with `New weeks` for a different one. OK?
