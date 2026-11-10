# Skateboard Fund Chances

## One idea
A $60 skateboard sits in a shop window and the child gets $8 a month for a year; each month they split the $8 between a jar (safe, never grows) and shares in the Sunny Squeeze class juice company (can grow or shrink), and a chance card shows how the juice business did that month (a hot summer, a lemon shortage, a new flavor); once the board is bought, risk cards come (rain, a cracked wheel, a theft at the park), and before each one the child chooses to avoid it, lower it with a lock, share it with a small insurance fee, or keep the risk and pay if it happens; the year-end card compares the all-jar, all-shares and the child's own path and the protected and unprotected board, so a fourth grader learns that investing can grow money for longer goals but can also shrink, that saving is safer for near goals, and that protecting what you own has a cost too.

## Not like
- piggy-bank-planner (2, spec): saving toward one goal with a jar and a bank. Here saving versus investing, and risk after buying.
- interest-seesaw (5, concept): how interest works. Here growth and loss by chance.
- covered-insurance-claims (9-12, concept): real insurance policies and claims. Here the plain idea of avoiding, lowering, sharing or keeping a risk.
- barter-bay (4, spec, this batch): what money is. Here what to do with it.

## Who and how
- Grade 4, Social Studies (Personal Finance), module "Bike Fund Chances" (see Open questions). Standards (National Standards for Personal Financial Education, 2021, grade 4):
  - NSPFE.Investing.4-1a: explain why people invest their money.
  - NSPFE.Investing.4-2a: identify the similarities and differences between saving and investing.
  - NSPFE.Investing.4-2b: provide examples of financial goals that are suited for saving versus investing.
  - NSPFE.Managing Risk.4-1a: give examples of risks that people and households face.
  - NSPFE.Managing Risk.4-1d: describe how valuable personal items might be lost or damaged.
  - NSPFE.Managing Risk.4-2a: recommend ways to reduce or avoid a given risk.
  - NSPFE.Managing Risk.4-4a: provide examples of large financial risks that people buy insurance for.
- Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Two parts: The fund (12 months), Protect it (3 risk cards); then the year-end card. Extra: Replay with a different deck. tool.json `modes: ["Play", "Replay deck"]`, `minutes: "15-25"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| NSPFE.Investing.4-2a | Split $8 each month between the jar and juice shares with a slider (0, 2, 4, 6 or 8 dollars to shares) | the jar and the shares growing or shrinking on a small two-line chart | 2 |
| NSPFE.Investing.4-1a | Read each month's chance card and see why the shares moved | the chance card and the share price arrow | 2 |
| NSPFE.Investing.4-2b | Sort four goals into Save or Invest (a skateboard this year, college in ten years, a birthday gift next month, a first car when you're 16) | the goal cards in two bins | 3 |
| NSPFE.Managing Risk.4-1a, 4-1d, 4-2a, 4-4a | Before each risk card, pick Avoid, Lower, Share or Keep, then see the result | the risk card, the four choices with their cost, the result | 4 |
| NSPFE.Investing.4-2a (with Risk) | Read the year-end card | three paths side by side, and the protected and unprotected board | 5 |

## Screens and modes
Header (kit): title "Skateboard Fund Chances"; `Play`, `Replay deck`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A shop window with a skateboard tagged $60. On a table: a glass jar and a Sunny Squeeze stock certificate (one share costs $4 to start). A month dial reads January. The welcome is queued (`welcomeAfter: true`): "That skateboard costs $60. Every month you get $8. Where does it go: the jar, the juice company, or some of each? Slide to choose." First hint: "Slide to split your $8, then tap Next month."

**The fund (focus: the slider, the chance card and the chart).** At 1366x768 jar, certificate and chart sit across the top and the chance card below; at 680x425 the chart folds behind a `Chart` tab.
- Each month: the child sets the slider (dollars to shares), taps `Next month`, and a chance card flips. Money put into shares buys parts of shares at that month's price.
- The main deck (12 months, in order): January, a normal month (no change); February, a rainy month, fewer drinks sold (down 10 percent); March, a new strawberry flavor (up 10 percent); April, normal; May, the school fair (up 20 percent); June, a hot summer starts (up 25 percent); July, still hot (up 25 percent); August, a lemon shortage, lemons cost more (down 20 percent); September, normal; October, a big order from the soccer league (up 10 percent); November, a spill means a batch is thrown out (down 25 percent); December, normal.
- With this deck: all jar reaches $60 in month 8 and ends the year at $96; all shares reaches $60 in month 6 and ends at about $98; half and half reaches $60 in month 7 and ends at about $97. A `Buy the board` button lights when jar plus shares reach $60; buying takes $60 from the jar first, then sells shares.
- The goals sort comes after month 6: "Some goals are near, some are far. Which fit saving and which fit investing?" Answers: skateboard this year (Save), birthday gift next month (Save), college in ten years (Invest), first car at 16 (Invest).

**Protect it (focus: the risk card).** After the board is bought, three risk cards come one at a time. Before each, four choices with a cost:
- Rain on the way: Avoid (keep the board inside on rainy days, $0, but no riding); Lower (wipe it dry after, $0, a little rust may come); Share (insurance doesn't cover rust, so this choice is grayed with the reason "Insurance doesn't pay for this"); Keep (ride anyway; result: rusty bearings, $8 to fix).
- A cracked wheel: Avoid (not possible: "Wheels wear out. You can't stop that."); Lower (check the wheels each month, $0, catches it early: a $3 wheel instead of $6); Share (board insurance, $2 a month, pays for the wheel); Keep (pay $6 for a new wheel when it cracks).
- A theft at the park: Avoid (never take it to the park, $0, but no park rides); Lower (a lock, $5 once); Share (board insurance, $2 a month, pays $60 if stolen); Keep (nothing; if it's stolen, it's gone).
- In the main deck the wheel cracks and the board is not stolen. The result card shows what each choice cost this time: "The insurance cost $2 a month even though nothing was stolen. That's the price of sharing the risk."
- A risk words card names the four ways plainly: avoid it, lower it, share it, keep it.

**Year-end card.** Three paths (all jar, all shares, yours): the month you could buy the board and the money left at the end; and two boards (protected, unprotected) with what was spent on protection and on repairs. Narrator: "Shares can grow faster, but they can shrink too. A jar is slower but safe. Protection costs a little to save a lot, if the bad thing happens." `Print` prints it.

**Replay deck (extra).** A second deck where the juice company has a hard year: all shares reaches $60 only in month 9, later than the jar (month 8), and ends at about $85; half and half ends at about $90. In this deck the board is stolen at the park. The year-end card shows both decks side by side if both were played.

## Content
- Two 12-month decks (main and replay) with share price changes; four goal cards; three risk cards with four choices each and set results per deck.
- Sunny Squeeze is a made-up class company; its share price starts at $4.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Buy the board` shows only when the fund reaches $60. Risk choices show only after the board is bought. A choice that can't help is shown grayed with its reason, never hidden, and the hint never names it.
- Keyboard: arrow keys move the slider; Enter for `Next month`; Tab through the four choices.
- With Motion off cards change without flipping and the chart draws at once.

## Look
- Accent `--brand` #a3245e skate berry (header, the chart's shares line, the certificate seal); gold #f4c542 (the jar line, `Buy the board`, the chosen protection); paper #fbf1f5; ink #2e0a1b; muted #64505a.
- Contrast (WCAG 2.1, computed): white on brand 7.07:1; brand on paper 6.40:1; ink on paper 16.17:1; muted on paper 6.70:1; ink on gold 10.98:1.
- Never color alone: chart lines are labeled "Jar" and "Shares" and use solid and dashed lines; price changes carry arrows and percents.
- Different from this batch (ripple blue, fix-it plum, barter ochre, valley olive).

## Art
- Local FLUX (`scripts/localart.py`): the shop window with the board (1, 16:9); the skate park (1, 16:9); twelve chance card pictures (12, 1:1: rain, strawberries, school fair, sun, lemons, soccer, a spill, plus five calm months reusing two pictures); three risk card pictures (3, 1:1: rain, a cracked wheel, an empty bike rack at the park).
- Drawn in code: the jar, the certificate, the slider, the chart, choice cards, the year-end card.
About 19 images. No people art.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the narrator; `news-reader` reads the chance cards like a news flash. `Curio.voice` with `scope: () => state.mode + ':' + state.month + ':' + state.risk`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each chance card (news-reader).
- how `buy` (once): "You have $60! Tap Buy the board."
- how `goals`: "Drag each goal to Save or Invest."
- how `risk`: "Pick a way to handle this risk."
- event, whole, each result line.
- event, whole, `year`: as in the year-end card.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the monthly split with fractional shares, the deck runner, the chart, the risk choices with set results, the year-end compare.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| The fund | Put everything in shares | It wins in the main deck, so the year-end card always shows the replay deck's result too: "This year the juice company did well. Will it always?" |
| Goals sort | Put all in Save | Two goals belong in Invest; wrong drops say how far away the goal is. |
| Risk choices | Always pick Share | Rain can't be shared, and the cost of insurance shows on the year-end card. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Each month: chance card (whole).
2. At $60: `buy` (once). After month 6: `goals`.
3. Each risk: `risk`; result (whole).
4. End: `year` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NSPFE grade 4 wording for Investing 4-1a, 4-2a, 4-2b and Managing Risk 4-1a, 4-1d, 4-2a, 4-4a | National Standards for Personal Financial Education (CEE and Jump$tart, 2021), consumerfinance.gov copy, read 2026-11-09 | data/standards/nspfe-2021.txt (codes) | yes |
| Saving is safe and suited to near goals; investing can grow more over long times but can lose value | Investor.gov (U.S. SEC), "Saving and investing" | FINRA, "Investing basics: risk" | yes |
| A share is a small part of a company; its price goes up and down with how the company does | Investor.gov, "Stocks" | Federal Reserve Bank of St. Louis, Econ Lowdown, "Stocks" | yes |
| Ways to handle risk: avoid, reduce, share (insurance), keep | Insurance Information Institute, "What is risk management?" | NSPFE 2021, Managing Risk introduction | yes |
| Insurance costs money even when nothing goes wrong; it pays for covered losses | Insurance Information Institute, "How insurance works" | Consumer Financial Protection Bureau, money lessons for kids, "Insurance" | yes |
| Rust on skateboard bearings comes from water; wheels wear and crack with use | Wikipedia, Skateboard (bearings and wheels) (checked 2026-11-09) | a skate shop maintenance guide (Tactics, "How to clean skateboard bearings") | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r6, 2026-11-09): main deck, all jar reaches $60 in month 8 and ends at $96; all shares month 6, ending $97.62; half month 7, ending $96.81; replay deck, all shares month 9, ending $84.59; half month 9, ending $90.29; risk costs add up per choice; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 jar, certificate, chart and card fit; at 680x425 the chart is a tab.
2. Each month's split and chance card update the jar, shares and chart to the checked values. (NSPFE.Investing.4-1a, 4-2a)
3. The four goals sort into Save and Invest. (NSPFE.Investing.4-2b)
4. Each risk card's four choices give their set cost and result, and grayed choices say why. (NSPFE.Managing Risk.4-1a, 4-1d, 4-2a, 4-4a)
5. The year-end card compares three paths and two boards. (NSPFE.Investing.4-2a)
6. `Buy the board` and the risk choices are never named before they show.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no flips; no network requests.

## Open questions
- The module is titled "Bike Fund Chances" while the tool is a skateboard fund (default used: the tool stays "Skateboard Fund Chances"; the module title is Cory's to align).
