# Grocery Run

## One idea
Coach Reyes (made up, labeled "illustration") puts the child in charge of food for field day: 28 students and 4 adults (2 of them need gluten-free food), a $120 budget, and a rule that everyone gets two drinks, a sandwich and fruit; in a store with plain store-brand shelves the child fills a cart, and each choice is worked on a scratch pad in columns: 32 people x 2 drinks = 64, drinks come in 12-packs and 64 / 12 is 5 remainder 4, so buy 6 and say what the remainder means; price lines like 6 x $4.79 = $28.74 are done with the standard algorithm, checked place by place; a 1,152-gram bag of grapes shared by 32 people is 36 grams each, built with an area model before the numbers; compare rounds weigh a 24-pack at $9.60 against a 6-pack at $2.70 by unit price ($0.40 against $0.45), with decimal division modeled first; at the register the receipt has one mistake (a doubled item or a wrong total) and the child finds it by adding decimals; with a tight budget the child sorts wants from needs and decides what to do with what's left; at the end the plan feeds everyone, fits the budget and passes the receipt check, so a fifth grader learns to multiply multi-digit numbers with the standard algorithm, to divide four-digit numbers by two-digit numbers with models and equations, to compute with decimals to hundredths, and to plan spending with unit prices and a budget.

## Not like
- corner-store (2, live): coins and change at a stand. Here a budget and unit prices.
- piggy-bank-planner (2, spec): saving for a goal. Here spending to a plan.
- tax-and-tip (7, concept): percents at a register. Here whole-number and decimal operations.
- summer-stand (6, concept): running a stand over time. Here one shopping plan.

## Who and how
- Grade 5, Math and personal finance, module "Operations with Whole Numbers and Decimals". Standards: 5.NBT.5 (fluently multiply multi-digit whole numbers using the standard algorithm), 5.NBT.6 (find whole-number quotients of whole numbers with up to four-digit dividends and two-digit divisors, using strategies based on place value, the properties of operations, and/or the relationship between multiplication and division; illustrate and explain the calculation by using equations, rectangular arrays, and/or area models), 5.NBT.7 (add, subtract, multiply, and divide decimals to hundredths, using concrete models or drawings and strategies based on place value, properties of operations, and/or the relationship between addition and subtraction; relate the strategy to a written method and explain the reasoning used); NSPFE.Spending, grade 4 benchmarks (compare prices and options, plan spending with a budget, tell needs from wants).
- Format: builder (changed from tycoon). Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Twelve store items with sample prices, the guest list, the scratch pad, four compare rounds, the receipt check, the wants and needs sort. Extra: Class plans (compare plans that meet the same budget in different ways). tool.json `modes: ["Field day", "Class plans"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5.NBT.5, 5.NBT.6 | Work packs, people and prices on the pad; share bulk packs | column products; the area model for 1,152 / 32 | 2 |
| 5.NBT.7 | Find unit prices; add the receipt | decimal models, then numbers | 3 |
| NSPFE.Spending | Fit the budget; sort wants and needs; find the receipt mistake | the budget card; the corrected receipt | 4 |

## Screens and modes
Header (kit): title "Grocery Run"; `Field day`, `Class plans`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A store aisle with plain store-brand shelves, a cart, a guest list on a clipboard and a budget card ($120), and Coach Reyes with a whistle. The welcome is queued (`welcomeAfter: true`): "Everyone gets two drinks, a sandwich and fruit. Start with drinks: how many do we need? Tap the scratch pad." First hint: "Tap the scratch pad."

**The pad (focus: the scratch pad).** At 1366x768 the aisle fills the left with the pad and cart total right; at 680x425 the pad is a sheet. 32 x 2 = 64 drinks; 64 / 12 = 5 r4; the child picks "buy 6 packs" and types what the 4 means (4 drinks short with 5 packs). Price lines: 6 x $4.79 in columns, checked place by place.

**Sharing.** 1,152 grams of grapes for 32 people: the child builds an area model (1,152 = 32 x 30 + 32 x 6) and writes 36 grams each. Sandwiches: 3 loaves of 20 slices for 30 sandwiches with gluten-free bread for 2.

**Compare.** A 24-pack at $9.60 against a 6-pack at $2.70. A hundredths grid splits $9.60 into 24 parts ($0.40) before the numbers.

**The register.** The receipt prints with one mistake. The child adds the column of decimals, finds the doubled line, and the clerk fixes it.

**Budget.** If the cart passes $120, the child sorts items into needs and wants and drops wants first. A plan that totals $113.65 leaves $6.35, and the child chooses what to do with it (save it for the next event, or buy sunscreen).

**Plan works (the aha).** Coach Reyes: "Same four operations, and they decide what you can afford. Checking the receipt is part of shopping."

**The end.** The shopping plan and checked receipt. `Print` prints them.

**Class plans (extra).** Plans side by side.

## Content
- Twelve items with sample prices labeled "sample prices", set near recent U.S. averages and dated; no real brand names; all readable with `Read`.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Items can be added and removed until checkout.
- Keyboard: Tab to shelf items, the pad's boxes, the cart, compare cards and receipt lines; Enter adds or checks.
- With Motion off the receipt appears printed.

## Look
- Accent `--brand` #1f4f8f cart blue (header, the pad lines, buttons); gold #f4c542 (the item in hand, the receipt line in question); paper #eef3fa; ink #081a33; muted #4e5767.
- Contrast (WCAG 2.1, computed): white on brand 8.16:1; brand on paper 7.32:1; ink on paper 15.62:1; muted on paper 6.53:1; ink on gold 10.71:1.
- Never color alone: over-budget shows the amount over in words; the mistake line is marked and named.
- Different from this batch (clockmaker brass, campfire red, lab teal, garden moss).

## Art
- People (illustrated): Coach Reyes, the clerk and the class, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Local FLUX (`scripts/localart.py`): the store aisle (1, 16:9), twelve plain store-brand items (12, 1:1), field day (1, 16:9).
- Drawn in code: the scratch pad, the hundredths grid, the area model, the receipt.
About 17 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as Coach Reyes; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.item + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `pad`: "Type the next digit on the pad."
- how `remainder`: "Pick what the remainder means."
- how `compare`: "Find each unit price."
- how `receipt`: "Tap the line that's wrong."
- how `budget`: "Drag a want out of the cart."
- event, whole, plan works.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
money (family "money"), using `money` and `r2` as described in paycheck-decoder's spec for exact cents. Tool-only code: the scratch pad, the area model, unit price compare, the receipt check, the needs and wants sort. Prices sit in a marked block `/* PRICES DATA: begin */ ... /* end */` with the date and source.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pad | Type the total | The pad goes column by column. |
| Remainder | Always round down | 5 packs leaves 4 people without a drink, and the field day check fails. |
| Receipt | Pay without checking | Checkout waits until the mistake is found. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `pad`; `remainder`.
2. `compare`.
3. `receipt`; `budget`.
4. Plan works (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 5.NBT.5, 5.NBT.6, 5.NBT.7 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| NSPFE Spending benchmarks for grade 4 | Council for Economic Education and Jump$tart Coalition, "National Standards for Personal Financial Education" (2021) | data/standards/nspfe-2021.txt | yes |
| Sample prices near recent U.S. averages | U.S. Bureau of Labor Statistics, "Average Price Data" (CPI), U.S. city average | USDA Economic Research Service, "Food Price Outlook" | yes |
| Comparing unit prices helps shoppers choose | Federal Trade Commission, consumer advice on unit pricing | NIST, Handbook 130, "Uniform Unit Pricing Regulation" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s15, 2026-11-10): 32 x 2 = 64 and 64 / 12 = 5 r4; 6 x $4.79 = $28.74; 1,152 / 32 = 36; $9.60 / 24 = $0.40 and $2.70 / 6 = $0.45; $120 - $113.65 = $6.35; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 aisle and pad; at 680x425 pad as a sheet.
2. Packs and prices are multiplied and divided on the pad, with the remainder explained. (5.NBT.5, 5.NBT.6)
3. Unit prices and the receipt are worked with decimals, models first. (5.NBT.7)
4. The plan fits the budget, wants and needs are sorted, and the receipt mistake is found. (NSPFE.Spending)
5. Prices are labeled sample prices with a date; no real brand names.
6. Coach Reyes, the clerk and the class are labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the receipt appears printed; no network requests.

## Open questions
- The idea card changes the format from tycoon to builder (default used: builder, since one shopping plan is built and checked and nothing runs over time).
- The idea card flags a data source (default used: sample prices set near the BLS Average Price Data U.S. city average, labeled sample prices with the date, checked again before build).
