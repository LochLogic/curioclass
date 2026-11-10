# Summer Stand

## One idea
On a hot street the child runs a summer drink stand next to a neighbor, Mrs. Chen (made up, labeled "illustration"), who lends the table: each morning the child sets a price per cup and the hours open, customers come, and a ledger records cups and money; after each day the tool asks which quantity depends on which (money earned depends on cups sold), then shows the rule three ways side by side, as a table, a graph and an equation (e = 1.5c at $1.50 a cup, so 40 cups bring $60), and changing the price changes the steepness of the line; variable rounds name the independent and dependent variable in new pairs (hours open and cups sold, cups sold and lemons used, temperature and customers) and write an equation when the pattern is steady; earning rounds show that income is not profit, since supplies cost $0.35 a cup, so a 40-cup day earns $60 and keeps $46; then an offer arrives to babysit for $12 an hour (a made-up offer), and two lines on one graph show that 3 hours at the stand (36 cups, $41.40 after supplies on a sunny day) beat 3 hours of babysitting ($36), but a rainy 10-cup day keeps only $11.50, which is the risk a wage does not have; at the end the child sees that a table, a graph and an equation are three views of the same rule, so a sixth grader learns to use variables for two quantities that change together, to tell the dependent from the independent variable, and to compare income from selling goods with income from a wage.

## Not like
- tax-and-tip (7, concept): percents and proportional costs. Here a rule between two variables.
- corner-store (2, live): coins and change. Here earnings, costs and profit.
- two-trains (8, live): two lines that meet as a system. Here two lines compared by reading values.
- grocery-run (5, spec): spending to a plan. Here earning and its risks.

## Who and how
- Grade 6, Math and personal finance, module "Dependent and Independent Variables". Standards: 6.EE.9 (use variables to represent two quantities in a real-world problem that change in relationship to one another; write an equation to express one quantity, thought of as the dependent variable, in terms of the other quantity, thought of as the independent variable; analyze the relationship between the dependent and independent variables using graphs and tables, and relate these to the equation); NSPFE.Earning Income, grade 8 benchmarks (income from selling goods and from wages; costs and profit; the trade-offs of being self-employed).
- Format: tycoon. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Seven stand days with weather, the ledger, the three-view panel, eight variable pairs, the babysitting offer. Extra: Class prices (each student's price makes one line on a shared graph on the projector). tool.json `modes: ["Stand", "Class prices"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 6.EE.9 | Set a price; name what depends on what | table, graph and e = 1.5c side by side | 2 |
| 6.EE.9 | Name variables in new pairs; write equations | the pair cards; equations like l = c / 4 | 3 |
| NSPFE.Earning Income | Find profit; compare the stand with a wage | two lines on one graph; the rainy day | 4 |

## Screens and modes
Header (kit): title "Summer Stand"; `Stand`, `Class prices`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A summer sidewalk, a folding table with a pitcher, a price board, a coin jar, and Mrs. Chen on her porch. The welcome is queued (`welcomeAfter: true`): "Pick a price per cup on the board, then tap Open." First hint: "Tap a price on the board."

**A stand day (focus: the street).** At 1366x768 the street fills the top with the ledger left and the three-view panel right; at 680x425 the panel is a tab. Customers walk up in a steady stream (about 12 cups an hour on a sunny day, labeled "made up"). The ledger fills: cups, money. At closing the child answers "Which depends on which?" by dragging the words onto the arrow.

**Three views.** The panel shows the table, the graph (cups across, dollars up) and the equation e = 1.5c. Tapping a table row lights the matching point and the matching substitution. A new price ($1.25, $2.00) redraws a steeper or flatter line.

**Variable rounds.** Eight pair cards; the child drags "independent" and "dependent" onto each, and writes an equation where the pattern is steady (one lemon makes 4 cups, so l = c / 4; cups = 12h on a sunny day). One card (temperature and customers) has no steady rule, and the child says so.

**Profit.** Supplies show as a second column at $0.35 a cup. The child finds the day's profit: $60 - $14 = $46.

**The offer.** A note: "Babysit Saturday, $12 an hour?" The graph shows two lines for 0 to 4 hours: stand profit (sunny), stand profit (rainy, 10 cups) and the wage. The child compares at 3 hours and picks what each choice gives: being your own boss and the chance of more, or a sure amount.

**Three views (the aha).** Mrs. Chen: "Table, graph, equation. Same rule, three ways to see it."

**The end.** The ledger and the graphs. `Print` prints them.

**Class prices (extra).** Each student's price adds a line on the projector.

## Content
- Seven days with weather, the customer rate and supply cost labeled "made up", the babysitting offer labeled "made-up offer", all readable with `Read`.
- No real brand names; the stand sells a plain lemon drink.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Price and hours can be changed before `Open`; answers can be changed until `Check`.
- Keyboard: Tab to the price board, hours, Open, ledger rows, the panel and pair cards; Enter sets or checks.
- With Motion off customers do not walk; the ledger fills at once.

## Look
- Accent `--brand` #a1460f awning orange (header, the ledger, buttons); gold #f4c542 (the row in hand, the matching point); paper #fbf2ea; ink #2a1204; muted #5e5249.
- Contrast (WCAG 2.1, computed): white on brand 6.18:1; brand on paper 5.59:1; ink on paper 16.00:1; muted on paper 6.83:1; ink on gold 10.88:1.
- Never color alone: the three lines carry labels at their ends ("stand, sunny", "stand, rainy", "babysitting").
- Different from this batch (measuring-cup teal, trellis green, deep-sea navy, market plum).

## Art
- People (illustrated): Mrs. Chen and six varied customers, labeled "illustration" (Gemini, `people: true`, 7; cutout yes).
- Local FLUX (`scripts/localart.py`): the summer street (1, 16:9), the stand (1, 1:1), a rainy street (1, 16:9).
- Drawn in code: the ledger, table, graph and price board.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as Mrs. Chen; `upbeat-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.day + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `open`: "Tap Open to start the day."
- how `depends`: "Drag each word onto the arrow."
- how `pair`: "Drag the labels onto the next pair."
- how `profit`: "Type the day's profit."
- how `offer`: "Compare the lines at 3 hours."
- event, whole, three views.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Cents use `money` and `r2` as described in paycheck-decoder's spec. Tool-only code: the stand day, the ledger, the three-view panel (table rows linked to graph points and substitutions), pair cards, the offer.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Depends | Swap the words at random | Each pair is checked, and the reason card asks which one you choose. |
| Equation | Type any rule | It is checked against every ledger row. |
| Offer | Pick the bigger number | The rainy line is part of the answer, and the reason card is needed. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `open`; `depends`.
2. `pair`.
3. `profit`; `offer`.
4. Three views (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 6.EE.9 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| NSPFE Earning Income benchmarks | Council for Economic Education and Jump$tart Coalition, "National Standards for Personal Financial Education" (2021) | data/standards/nspfe-2021.txt | yes |
| Tables, graphs and equations as linked views of one relationship | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Expressions and Equations" | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", grades 6-8 algebra | yes |
Backed twice: 3. Cut: 0.

Sensitivity: money and jobs are shown neutrally; neither choice is called right, and no wage claims a real market rate.

Checks run (Python, scratchpad s17, 2026-11-10): 1.5 x 40 = $60 and 40 x $0.35 = $14, profit $46; 3 hours x 12 = 36 cups, $54 - $12.60 = $41.40 against 3 x $12 = $36; rainy 10 cups $15 - $3.50 = $11.50; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 street, ledger and panel; at 680x425 panel as a tab.
2. Each stand day names the dependent and independent variable and shows table, graph and equation. (6.EE.9)
3. Eight pair cards are labeled, with equations where the pattern is steady. (6.EE.9)
4. Profit is found, and the stand is compared with a wage on one graph, rainy day included. (NSPFE.Earning Income)
5. Made-up rates and the offer are labeled; no brand names.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the ledger fills at once; no network requests.

## Open questions
None.
