# Piggy Bank Planner

## One idea
The child wants the 12-dollar kite in the corner shop window and earns 2 dollars a week for chores, and each week chooses to spend it now (the 1-dollar candy bar and 4-dollar ball sit right there with their price tags), drop it in the piggy bank at home, or carry it to the bank down the street, which keeps it safe, lends it to the baker for a new oven, and pays a few cents extra; a surprise cost in week 5 shows another reason people save, and the goal bar shows plainly that spending every week means no kite while saving gets it.

## Not like
- corner-store (2, concept, same money family): making change at a stand. Here saving toward a goal over weeks.
- market-day (1, spec): one market day choosing goods and services. Here weeks of choices and a bank.
- interest-seesaw (5, concept): grade 5 interest. Here a bank's three jobs at grade 2, with interest shown as a few cents.
- pen-pal-parcels (2, spec, this batch): trade between countries. Here saving in one town.

## Who and how
- Grade 2, Social Studies (Economics), module "Money, Saving and Trade". Standards: D2.Eco.5.K-2 (identify prices of products in a local market), D2.Eco.9.K-2 (describe the role of banks in an economy), D2.Eco.10.K-2 (explain why people save). D2.Eco.14.K-2 moved to pen-pal-parcels (idea card).
- Driver: one child alone, or the teacher on the projector with the class voting each week; every price, choice and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Up to 8 weeks per try. tool.json `modes: ["Save for it", "Bank", "My goal"]`, `minutes: "10-20"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.5.K-2 | Read the shop's price tags, pick a goal, and compare what's in hand with each price every week | price tags with dollars as numbers and coins; "You can buy" glows on what you can afford | 2, 3 |
| D2.Eco.10.K-2 | Choose spend, piggy or bank each week and watch the goal bar; meet the week 5 surprise cost | the goal bar, the week strip, the surprise card | 4, 5 |
| D2.Eco.9.K-2 | Visit the bank and see its three jobs: keep money safe, lend it out, pay savers a little extra | the bank's three doors and the baker's oven story | 6 |

## Screens and modes
Header (kit): title "Piggy Bank Planner"; `Save for it`, `Bank`, `My goal`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** The corner shop window: a red kite with a tag "12 dollars", a ball "4 dollars", a candy bar "1 dollar". Each tag shows the number and a row of dollar pictures. The welcome is queued (`welcomeAfter: true`): "Look at the shop window! Which one do you want most? Tap it to hear its price." First hint: "Tap a thing in the window to hear its price." The first tap reads that price and cuts the welcome. A second tap sets it as the goal.

**Save for it (focus: the week's choice).** At 1366x768 the shop window is at the top (prices always in view), the week strip (8 boxes) runs across the middle, and three choice doors sit at the bottom: `Spend it` (a shop bag), `Piggy bank` (a pig), `Bank` (a bank building). The goal bar is at the right, showing piggy money, bank money and the goal line. At 680x425 the shop window shrinks to a row of three tags.
- Each week: "You did your chores. You earned 2 dollars!" Two dollar pictures drop into the child's hand. The child taps one door. (A child may split: tap a dollar, then a door, for each dollar.)
- `Spend it`: the shop opens; the child taps something they can afford. Candy: eaten, gone. The ball (after saving enough to have 4 in hand or in the piggy): bought, and the goal bar drops.
- `Piggy bank`: the dollars drop in with a clink. Piggy money can be taken out any week: on weeks 3 and 6 the candy bar is "on sale today!" and a `Take from piggy` button shows. The bank has no such button that week; bank money waits until the goal.
- `Bank`: the dollars go to the bank. The bank's counter shows the amount; every two weeks it adds the cents it pays (see Bank).
- Week 5 surprise: "Oh no! Your water bottle cracked. A new one costs 3 dollars." The child pays from piggy or bank (the child picks). If the child has less than 3 dollars saved, a grown-up pays this time and says "That's why we keep some money saved."
- When saved money reaches the goal: the kite flies in the window and the child taps `Buy it`. If 8 weeks pass first: "Not enough this time. You spent [amount] on [things]. Want to try again?" and `Try again`.
- After any ending, a week strip review shows each week's choice with its icon, and the line: "Saving means waiting now to get something bigger later."

**Bank (focus: three doors in the bank lobby).** Opens from the header or the first time the child picks `Bank`. A friendly teller, Mr. Osei, shows three doors:
1. "Safe": a vault. "Money in the bank is kept safe, even if a piggy bank breaks or gets lost." (The bank is FDIC insured; the line says only that it is kept safe.)
2. "Lend": the baker, Ms. Lane, borrows money from the bank to buy a new oven, bakes more bread, and pays the bank back a little more than she borrowed. "The bank lends saved money to people who need it."
3. "Extra": "The bank pays you a little extra for keeping your money here." The counter shows the child's extra so far in cents.
- The extra uses a sample rate of 4 percent a year, computed weekly: 2 dollars a week for 8 weeks earns about 4 cents. The tool says "a few cents" and shows the exact cents, so the bank's extra is honest: small.

**My goal (focus: setup).** For a class or a child: pick a goal from six pictures with prices (a book 6, a puzzle 8, a kite 12, a soccer ball 15, a scooter 30, a tablet game 20) and an allowance (1, 2 or 3 dollars a week). The tool shows how many weeks saving all of it takes ("12 dollars at 2 a week is 6 weeks.") and then plays Save for it with those numbers for that many weeks plus two (still with the surprise).

## Content
- Shop: kite 12, ball 4, candy 1 (dollars). Allowance 2 a week. 8 weeks. Candy sale on weeks 3 and 6. Surprise in week 5: 3 dollars.
- Outcomes: save every dollar: 16 by week 8, minus 3 for the bottle is 13, so the kite (12) is reached in week 8 (week 7 holds 14 minus 3 = 11, short by 1). Spend 1 each week on candy: 8 minus 3 leaves 5; no kite.
- Bank: three doors; the baker story in four pictures.

## Interactions in detail
- Every tap acts at once; a new line stops the old one; tapping a door during the week's line acts at once.
- `Take from piggy` shows only on sale weeks when the piggy has money. `Buy it` shows only when saved money reaches the goal. `Try again` shows after week 8.
- The goal bar uses the money family's `money()` for amounts.
- With Motion off coins appear without dropping and the kite appears without flying.

## Look
- Accent `--brand` #a3305a piggy rose (header, the doors, goal bar frame); gold #f4c542 (coins, the goal line, "You can buy" glow); paper #fcf1f5; ink #2e0b18; muted #6a5059.
- Contrast (WCAG 2.1, computed): white on brand 6.71:1; brand on paper 6.09:1; ink on paper 16.17:1; muted on paper 6.56:1; ink on gold 10.97:1.
- Never color alone: piggy and bank money on the goal bar carry the pig and bank icons and amounts.
- Different from this batch (pen pal indigo, storm teal, carousel red-brown, three towns olive).

## Art
- People art goes to Gemini with `people: true`: Mr. Osei the teller (3 poses: greeting, pointing to the vault, smiling; cutout yes); Ms. Lane the baker (4 pictures: asking for a loan, buying the oven, baking more bread, paying back; cutout yes); a grown-up helping with the bottle (1, from the side).
- Local FLUX (`scripts/localart.py`): the shop window (16:9) with kite, ball and candy as separate cutouts (3, 1:1, cutout yes); the bank lobby and vault (2); the piggy bank (1:1, cutout yes); a cracked water bottle (1); My goal pictures (6, 1:1).
- Drawn in code: price tags, dollar and coin pictures, doors, the week strip, the goal bar, the review strip.
About 23 images.

## Voice
Bank voice `big-sister` as the narrator (unique in this batch). Mr. Osei and Ms. Lane speak in the same narrator voice as quoted lines. `Curio.voice` with `scope: () => state.mode + ':' + state.week + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Look at the shop window! Which one do you want most? Tap it to hear its price."
- event `price`: "[Thing]: [n] dollars. Tap it again to make it your goal."
- event, whole, `week`: "Week [n]. You did your chores. You earned 2 dollars! Tap Spend it, Piggy bank, or Bank."
- event `clink`, `bank-in`, `spent`: short lines with sounds.
- event, whole, `sale`: "The candy bar is on sale today! You could tap Take from piggy, or keep saving."
- event, whole, `surprise`: "Oh no! Your water bottle cracked. A new one costs 3 dollars. Pay from piggy or bank?"
- event, whole, `goal`: "You have enough! Tap Buy it."
- event, whole, `short`: "Not enough this time. You spent [amount] on [things]. Want to try again?"
- event, whole, `lesson`: "Saving means waiting now to get something bigger later."
- event, whole, the three bank door lines and the baker story.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
The money family engine (described in paycheck-decoder's spec; the integrating session picks its file, for example `kit/money.js`). This grade 2 tool uses only `money(n, cents)` and `r2(n)`, plus `grow({start, deposit, months, rate, perYear})` with `perYear: 52` for the bank's few cents. It feeds it: deposits of 2 dollars on chosen weeks and rate 0.04.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Save | Tap Bank every week | Allowed; that is saving. The review strip still asks the child to see why it worked. |
| Save | Spend some, save some | Works only if spending stays at 1 dollar or less overall; the goal bar shows the gap each week. |
| Surprise | Have no savings | A grown-up pays and says why saving matters; the goal bar does not move. |
| Bank | Skip it | The extra line and the bank's three jobs play the first time the child picks Bank, and the Bank mode lists them. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap a thing: `price`; again: goal set.
2. Each week: `week` (whole), waits; a door tap: its short line; sale weeks: `sale` (whole); week 5: `surprise` (whole).
3. First Bank pick: the three bank lines (whole, in order).
4. End: `goal` or `short` (whole), then `lesson` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.5, D2.Eco.9 and D2.Eco.10 (K-2) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Banks keep deposits safe, lend saved money to borrowers who repay with interest, and pay savers interest | FDIC, Money Smart for Young People (grades Pre-K to 2), "Banks" | Federal Reserve Bank of St. Louis, Econ Lowdown "Banks and saving" (primary) | yes |
| A savings rate near 4 percent a year is within the range U.S. banks paid savers in 2025-2026 (the tool calls it a sample rate) | FDIC, National Rates and Rate Caps | Federal Reserve Bank of St. Louis, FRED savings deposit rates | yes |
| People save to buy something bigger later and to be ready for surprise costs | FDIC, Money Smart for Young People, "Saving" | Consumer Financial Protection Bureau, "Money as You Grow" (ages 3-5 and 6-12) | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r4, 2026-11-09): saving all 8 weeks gives 16 minus 3 = 13, reaching 12 in week 8 and not in week 7 (11); candy every week leaves 5; 2 dollars a week for 8 weeks at 4 percent a year, compounded weekly, earns 4 cents; My goal weeks for all 18 goal and allowance pairs; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 window, week strip, doors and goal bar fit; at 680x425 the window shrinks to tags.
2. Every price shows as a number and dollar pictures and is spoken. (D2.Eco.5.K-2)
3. "You can buy" glows only on things the child can afford. (D2.Eco.5.K-2)
4. Saving all 8 weeks reaches the kite; spending on candy every week does not. (D2.Eco.10.K-2)
5. The week 5 surprise takes 3 dollars, or a grown-up pays if savings are short. (D2.Eco.10.K-2)
6. The bank shows safe, lend (the baker) and extra (cents shown). (D2.Eco.9.K-2)
7. `Take from piggy`, `Buy it` and `Try again` are never named before they show.
8. Tap while it plays: a door tap during the week's line acts at once; no older line plays after a newer one.
9. Motion off: no falling coins or flying kite; no network requests.

## Open questions
- None for Cory.
