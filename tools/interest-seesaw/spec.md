# Interest Seesaw

## One idea
The child has $100 of birthday money and a seesaw with a saver on one end and a borrower on the other: they pick where to keep the money (a jar at home, a bank savings account, a credit union account or a savings bond) and watch interest add coins on the saver's side year by year, then a neighbor needs to borrow $200 for a bike and the seesaw tips the other way as interest adds to what the borrower pays back; the teller shows that the bank pays savers less than it charges borrowers and that the gap is how the bank pays its workers and keeps the lights on, so a fifth grader learns what interest is, why savers earn it and borrowers pay it, and what banks and credit unions do in an economy.

## Not like
- piggy-bank-planner (2, spec): saving toward a goal with a jar. Here where the money is kept and what interest does to it.
- skateboard-fund-chances (4, spec): risk and return of investing. Here safe accounts and loans, both sides of interest.
- learn-and-earn (4, spec): income from skills. Here what money earns or costs once you have it.
- compound-garden (grade 8, concept): compound growth over decades. Here simple yearly interest over five years and one loan.

## Who and how
- Grade 5, Social Studies (Economics), module "Interest Seesaw". Standards: D2.Eco.9.3-5 (describe the role of other financial institutions in an economy), D2.Eco.10.3-5 (explain what interest rates are). Personal finance: NSPFE 2021 Saving 4-4a, 4-5b; Managing Credit 4-1a, 4-1b.
- Format: explorer.
- Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Two sides: Saver (the $100) and Borrower (the $200 bike loan), then the teller's window that joins them. Extra: Shop for a loan (the same $200 at two loan lengths). tool.json `modes: ["Saver", "Borrower", "Shop for a loan"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.10.3-5 | Move the $100 between places and run five years; then borrow $200 and run twelve months | coins added on the saver's side each year; coins added on the borrower's side each month; the rate shown as "cents per dollar per year" | 2, 3 |
| D2.Eco.9.3-5 | Open the teller's window and follow one dollar from a saver to a borrower and back | the money-flow loop: saver deposits, bank lends, borrower repays with interest, bank pays the saver less and keeps the gap | 4 |
| NSPFE Saving 4-4a | Compare the jar at home with an account | the jar grows by zero; the account's sign says "insured" | 2 |
| NSPFE Saving 4-5b | Compare the bank's and the credit union's savings rates side by side | two rate cards and their five-year totals | 2 |
| NSPFE Managing Credit 4-1a, 4-1b | Borrow $200 and see why more than $200 is paid back; read why the bank lends | the payback total; the teller's line on why lenders lend | 3, 4 |

## Screens and modes
Header (kit): title "Interest Seesaw"; `Saver`, `Borrower`, `Shop for a loan`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A park seesaw. On the left a kid named Jada holds a $100 birthday card; the right end is empty. Below, four places to keep the money: a jar at home, Main Street Bank, River Credit Union, a U.S. savings bond. The welcome is queued (`welcomeAfter: true`): "Jada has a hundred dollars of birthday money. Where should she keep it? Drag the money to a place, then tap Run five years." First hint: "Drag the money to a place."

**Saver (focus: the four places and the seesaw).** At 1366x768 the seesaw sits above the places; at 680x425 the places become a row of cards under a smaller seesaw.
- Each place card shows its rate as "cents per dollar per year" and as a percent, the date the rate was read, and one fact: the jar ("No interest. Can be lost or stolen."), the bank ("Insured by the FDIC up to $250,000."), the credit union ("Owned by its members. Insured by the NCUA."), the bond ("Backed by the U.S. government. Must be held at least one year.").
- `Run five years`: a coin counter adds each year's interest to Jada's side. Simple yearly interest for clarity, then a note at the end shows the compounded total too (e.g. at 4% a year: $104, $108.16, $112.49, $116.99, $121.67; at 0.4%: $102.02 after five years).
- Rates are real and dated: filled at build from the FDIC national average savings rate, the NCUA credit union average, and TreasuryDirect's current EE and I bond rates. Each card shows "rate as of" and its source.
- After two places have been run, `Compare` shows them side by side.

**Borrower (focus: the seesaw's right side).** Mr. Okafor next door needs $200 for a bike to ride to work. He borrows it from Main Street Bank at a personal loan rate (filled at build from the Federal Reserve G.19 average; the example uses 12% a year). `Run twelve months`: each monthly payment drops a stack of coins on his side, part paying back the $200 and part paying interest (shown in two colors and two patterns). At 12% over 12 months, payments of $17.77 a month, total $213.24, so $13.24 of interest. The seesaw tips: what Jada earned in five years is far less than what Mr. Okafor pays in one.

**Teller's window.** The teller (Ms. Ruiz) shows one dollar's trip: Jada's savings sit in the bank; the bank lends that money to Mr. Okafor; he pays it back with interest; the bank pays Jada interest and keeps the difference to pay its tellers, its building and its losses on loans not paid back. The child taps each step of the loop to light it. Ms. Ruiz: "Banks pay savers so they'll keep money here. They charge borrowers more, because some loans don't get paid back and the bank has bills too." A side card names what credit unions do differently (owned by members, often slightly better rates).

**Shop for a loan (extra).** The same $200 at the same rate over 6 months or 12 months. Six months: about $34.51 a month, total about $207.06; twelve: $17.77 a month, total $213.24. Shorter loan, bigger payments, less interest. The child picks which fits Mr. Okafor's $40-a-month budget and says why.

**The end.** Both sides on one screen. Narrator: "Interest is the price of using money. Savers get paid for lending it to the bank. Borrowers pay for using someone else's money." `Print` prints the comparison card.

## Content
- Four places with real, dated rates (filled at build, each with its source and "rate as of"); one loan at the G.19 rate; the teller's loop; the shop-for-a-loan pair.
- Jada, Mr. Okafor, Ms. Ruiz, Main Street Bank and River Credit Union are made up; the FDIC, NCUA, TreasuryDirect and Federal Reserve rates are real.
- Numbers round to cents; the example figures above are for the spec's check and change with the build-time rates.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Drag or tap-then-place moves the $100 (keyboard: Tab to the money, Enter, arrow to a place, Enter).
- `Run` buttons can be tapped again to replay; `Skip to the end` jumps to the total.
- With Motion off the seesaw jumps to its tilt and coins appear without falling.

## Look
- Accent `--brand` #0b6e4f money green (header, the seesaw beam, interest coins); gold #f4c542 (the money being dragged, the lit step in the loop); paper #eef7f3; ink #04221a; muted #4b5b55.
- Contrast (WCAG 2.1, computed): white on brand 6.25:1; brand on paper 5.73:1; ink on paper 15.40:1; muted on paper 6.57:1; ink on gold 10.34:1.
- Never color alone: principal coins are plain and interest coins carry a star; the seesaw tilt is also written ("Saver +$21.67", "Borrower +$13.24").
- Different from this batch (timeline violet, trade harbor teal, ship's log wood, review red).

## Art
- People art goes to Gemini with `people: true`: Jada (2 poses: holding the card, cheering; cutout yes), Mr. Okafor with his bike (1, cutout yes), Ms. Ruiz at the window (1, cutout yes).
- Local FLUX (`scripts/localart.py`): the park with the seesaw (1, 16:9); the bank lobby (1, 16:9).
- Drawn in code: the seesaw beam and tilt, coins, place cards, the money-flow loop, the comparison card.
About 6 images.

## Voice
Three bank voices, each unique in this batch: `upbeat-guide` as the narrator, `easy-coach` as Ms. Ruiz the teller, `hero-coach` as Mr. Okafor. `Curio.voice` with `scope: () => state.mode + ':' + state.place + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `place`: "Drag the money to a place, then tap Run five years."
- event, whole, each year's coin count.
- how `compare`: "Run a second place, then tap Compare."
- how `borrow`: "Tap Run twelve months to see Mr. Okafor pay it back."
- event, whole, the loan total.
- how `loop`: "Tap each step to follow one dollar through the bank."
- event, whole, the teller's lines.
- how `shop`: "Pick six months or twelve months for Mr. Okafor."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the seesaw with tilt from two totals, the yearly interest counter, the monthly loan schedule, the loop and the compare card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Saver | Keep it in the jar | The jar's side shows $100 after five years beside a growing account. |
| Teller's loop | Tap steps at random | Steps light only in order; a wrong tap plays "Where does the money go next?" |
| Shop for a loan | Pick the smaller payment without looking | The budget line shows $34.51 fits $40 and the total interest is lower; the child picks a reason tile. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `place`.
2. Year counts (whole), each waits. `compare`.
3. `borrow`; loan total (whole), waits.
4. `loop`; teller's lines (whole). `shop`. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.9.3-5 and D2.Eco.10.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| NSPFE 2021 Saving 4-4a, 4-5b and Managing Credit 4-1a, 4-1b wording | National Standards for Personal Financial Education (CEE and Jump$tart, 2021), PDF at files.consumerfinance.gov | Council for Economic Education, standards page | yes |
| Bank deposits are insured by the FDIC up to $250,000 per depositor per bank | FDIC, "Deposit insurance" | Consumer Financial Protection Bureau, "Is my money safe in a bank?" | yes |
| Credit unions are member-owned and insured by the NCUA up to $250,000 | NCUA, "Share insurance" | MyCreditUnion.gov (NCUA), "What is a credit union?" | yes |
| Savings bonds are backed by the U.S. government and must be held at least one year | TreasuryDirect, "EE bonds" | TreasuryDirect, "I bonds" | yes |
| Banks pay less on deposits than they charge on loans, and the spread covers costs and loan losses | Federal Reserve Bank of St. Louis, "How banks make money" (Page One Economics) | Federal Reserve Education, "Banks and interest" | yes |
| National average savings rate and personal loan rate (filled at build) | FDIC national rates and rate caps (monthly) | Federal Reserve G.19 consumer credit, 24-month personal loan rate | yes, each read on the build date |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r8, 2026-11-09): $100 at 4% a year compounded is $104, $108.16, $112.49, $116.99, $121.67; at 0.4% it is $102.02 after five years; a $200 loan at 12% a year is $17.77 a month over 12 months (total $213.24) and $34.51 over 6 months (total $207.06); $34.51 fits a $40 budget and $17.77 leaves more room; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 seesaw and places fit; at 680x425 the places are a card row.
2. Saver: the jar stays at $100; an account grows by its dated rate; two places compare. (D2.Eco.10.3-5; Saving 4-4a, 4-5b)
3. Borrower: $200 at the build rate shows monthly payments and a total over $200. (D2.Eco.10.3-5; Managing Credit 4-1a)
4. Teller's loop lights in order and names why the bank lends and keeps a gap. (D2.Eco.9.3-5; Managing Credit 4-1b)
5. Every rate card shows its source and "rate as of" date.
6. Shop for a loan shows both totals and payments.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no falling coins or tilting; no network requests (rates are baked in at build).

## Open questions
- Rates: the build reads the FDIC, NCUA, TreasuryDirect and Federal Reserve rates on the build date and bakes them in with "rate as of" (default used: refresh them once a year with the site's yearly check).
