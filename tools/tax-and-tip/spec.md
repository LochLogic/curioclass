# Tax and Tip

## One idea
For a week of shifts the child runs the register at a family diner owned by Mr. Haddad (made up, labeled "illustration"), where tax is 8% and every receipt is a percent problem: a $25 breakfast rings up at $27.00, a $16 senior order takes 25% off to $12, and a $40 table's tip is $6 at 15% or $8 at 20%; each receipt drops a point on a graph of bill against total, and the tax points line up through the origin, so the child names the constant (total = 1.08 x bill) and what the point (1, 1.08) means; then a catering order with a flat $5 delivery fee makes a line that misses the origin, and the child tests tables and graphs to say which relationships are proportional; unit-rate rounds come from the kitchen and the delivery bike (1/2 mile every 1/4 hour is 2 miles per hour; 3/4 cup of batter per 1/2 batch is 1 1/2 cups per batch); back-office rounds raise menu prices 6% ($9.50 becomes $10.07), compare a server's quick $6 tip with the exact $5.70 (about 5.3% error), price a $2,000 grill loan at 5% simple interest for 3 years ($300 interest), and mark up a $4 supply by 50%; at the end the child sees that a proportional relationship has one constant running through every receipt and that a fixed fee breaks it, so a seventh grader learns to compute unit rates with fractions, recognize and represent proportional relationships, and solve multistep percent problems.

## Not like
- smoothie-lab (Grades 6-7, live): equivalent ratios in recipes, same ratio family. Here the constant of proportionality and percents.
- grocery-run (5, spec): decimals and a budget. Here percents and proportional graphs.
- summer-stand (6, spec): dependent and independent variables. Here proportional or not.
- phone-plan-showdown (7, spec): equations and inequalities. Here percents on receipts.

## Who and how
- Grade 7, Math, module "Proportional Relationships". Standards: 7.RP.1 (compute unit rates associated with ratios of fractions, including ratios of lengths, areas and other quantities measured in like or different units), 7.RP.2 (recognize and represent proportional relationships between quantities: a. decide whether two quantities are in a proportional relationship, e.g., by testing for equivalent ratios in a table or graphing on a coordinate plane and observing whether the graph is a straight line through the origin; b. identify the constant of proportionality (unit rate) in tables, graphs, equations, diagrams, and verbal descriptions; c. represent proportional relationships by equations; d. explain what a point (x, y) on the graph of a proportional relationship means in terms of the situation, with special attention to the points (0, 0) and (1, r) where r is the unit rate), 7.RP.3 (use proportional relationships to solve multistep ratio and percent problems: simple interest, tax, markups and markdowns, gratuities and commissions, fees, percent increase and decrease, percent error).
- Format: tycoon. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Five shifts of orders, the receipt graph, four proportional-or-not tests, six unit rates, six back-office problems. Extra: Rush hour (a fast round on the projector). tool.json `modes: ["Shifts", "Rush hour"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.RP.2 | Ring up receipts; read the graph; test the delivery fee | points through the origin; a line that misses it | 2 |
| 7.RP.1 | Find unit rates from fractions | 2 miles per hour; 1 1/2 cups per batch | 3 |
| 7.RP.3 | Work tax, discounts, tips, increases, error, interest, markup | receipts and the back-office ledger | 4 |

## Screens and modes
Header (kit): title "Tax and Tip"; `Shifts`, `Rush hour`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A diner counter at breakfast, a chrome register, plates on the pass, and Mr. Haddad in an apron. The welcome is queued (`welcomeAfter: true`): "Tax here is 8 percent. Ring up table 3. Tap the register." First hint: "Tap the register."

**A shift (focus: the register).** At 1366x768 the counter fills the left with the receipt and the graph right; at 680x425 the graph is a tab. Orders arrive as tickets; the child types the tax, discount or tip, then the total. Each receipt adds a point (bill, total). After four points the child taps `Find the constant`, types 1.08 and the equation, and taps the point (1, 1.08) to say what it means ("each dollar of food costs $1.08").

**Proportional or not.** Four tables and graphs: tax, tip at 20%, a $5 delivery fee, a buy-one-get-one deal. The child tests each by equal ratios or by the graph and sorts them.

**Unit rates.** The delivery cyclist's log and the cook's batter card give rates with fractions; the child divides and names the unit.

**Back office.** Six problems in a ledger: menu prices up 6%, percent error on a mental tip, the grill loan, a 50% markup, a 20% markdown on day-old pie, and a server's commission on catering.

**One constant (the aha).** Mr. Haddad: "One number runs through every receipt. Add a flat fee and the line jumps off zero."

**The end.** The week's receipts and graph. `Print` prints them.

**Rush hour (extra).** Fast orders on the projector.

## Content
- Thirty orders across five shifts, made-up menu prices labeled "sample prices", all readable with `Read`.
- Tipping is presented as a U.S. custom; a teacher note says customs vary by country.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Receipt lines can be retyped until `Print receipt`.
- Keyboard: Tab to tickets, the register keys, the graph (arrows move between points), tables and ledger boxes; Enter rings up or checks.
- With Motion off receipts print at once.

## Look
- Accent `--brand` #0f6b6b diner teal (header, the register, buttons); gold #f4c542 (the ticket in hand, the point (1, r)); paper #ebf6f6; ink #042222; muted #4a5858.
- Contrast (WCAG 2.1, computed): white on brand 6.30:1; brand on paper 5.71:1; ink on paper 15.15:1; muted on paper 6.73:1; ink on gold 10.27:1.
- Never color alone: proportional lines are labeled "through (0, 0)"; others say "misses (0, 0)".
- Different from this batch (signal orange, balloon sky blue, midway red, licorice purple).

## Art
- People (illustrated): Mr. Haddad, two servers, a cook, a delivery cyclist and varied customers, labeled "illustration" (Gemini, `people: true`, 6; cutout yes).
- Local FLUX (`scripts/localart.py`): the diner (1, 16:9), plates (4, 1:1).
- Drawn in code: the register, receipts, tables and the graph.
About 11 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as Mr. Haddad; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.shift + ':' + state.order + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `ring`: "Type the tax, then the total."
- how `constant`: "Tap Find the constant."
- how `point`: "Tap the point at 1 and say what it means."
- how `sort`: "Drag the table to Proportional or Not."
- how `rate`: "Type the unit rate."
- how `ledger`: "Fill in the next ledger line."
- event, whole, one constant.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
ratio (family "ratio"; no engine file yet). This tool builds the ratio family's shared pieces first, in a marked block `/* RATIO ENGINE: begin */ ... /* end */`: a ratio table with equal-ratio checks, a unit-rate finder for fraction pairs, a proportional test (equal ratios and a line through (0, 0)) and a percent helper (part, whole, rate; increase, decrease, error), all exact with `Frac` as described in equation-golf's spec; smoothie-lab moves onto it when next touched. Cents use `money` and `r2` as described in paycheck-decoder's spec. Tool-only code: shifts, the register, receipts, the ledger.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Totals | Type the bill | Each receipt checks tax or tip and total. |
| Proportional | Pick every straight line | The delivery fee line is straight but misses (0, 0). |
| Percent error | Subtract only | The check needs the error divided by the exact tip. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `ring`; `constant`; `point`.
2. `sort`.
3. `rate`; `ledger`.
4. One constant (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.RP.1 to 7.RP.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The point (1, r) and the origin in proportional graphs | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-7 Ratios and Proportional Relationships" | Lobato and Ellis (2010), "Developing Essential Understanding of Ratios, Proportions, and Proportional Reasoning, Grades 6-8", NCTM | yes |
| Simple interest is principal x rate x time | Consumer Financial Protection Bureau, "What is the difference between a loan's interest rate and its APR?" | Council for Economic Education and Jump$tart Coalition, "National Standards for Personal Financial Education" (2021), Managing Credit | yes |
Backed twice: 3. Cut: 0.

Sensitivity: tipping customs vary by country; the teacher note says so, and no customer is shown as a poor tipper.

Checks run (Python, scratchpad s19, 2026-11-10): $25 x 1.08 = $27.00; 25% off $16 is $12; 15% and 20% of $40 are $6 and $8; 1/2 / 1/4 = 2 and 3/4 / 1/2 = 1 1/2; $9.50 x 1.06 = $10.07; 15% of $38 is $5.70 and ($6 - $5.70) / $5.70 is about 5.3%; $2,000 x 5% x 3 = $300; $4 marked up 50% is $6; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 counter, receipt and graph; at 680x425 graph as a tab.
2. Receipts are graphed, the constant is named with an equation, and (1, r) is explained; proportional and not are sorted. (7.RP.2)
3. Six unit rates are found from ratios of fractions. (7.RP.1)
4. Back-office percent problems are solved, including interest, markup and percent error. (7.RP.3)
5. The RATIO ENGINE block is built for the family; prices are sample prices.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: receipts print at once; no network requests.

## Open questions
None.
