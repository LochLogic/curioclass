# Phone Plan Showdown

## One idea
The child plays a skeptical customer at a phone store counter where a salesperson, Marcus (made up, labeled "illustration"), makes bold claims about two prepaid plans from made-up carriers, Plan A at $20 a month plus $3 per GB and Plan B at $35 a month with 5 GB included and $1 per GB after; for each claim ("Plan B is always cheaper") the child builds the inequality behind it from tiles (20 + 3g < 35), solves it, graphs the solution set on a number line, and answers Marcus in words ("Plan A is cheaper only if I use less than 5 GB; at 5 GB they tie at $35; above that Plan B wins"); two-kinds rounds solve px + q = r and p(x + q) = r, such as a family of 4 each paying (x + 5) dollars toward a $72 bill, once with arithmetic (72 / 4 = 18, then 18 - 5 = 13) and once with algebra, and the child compares the steps; fine-print rounds bring 6.5% tax ($35 becomes $37.28), a 1/4-off first month ($26.25) and a $0.10 per minute call fee, with an estimate first (is the bill near $40 or $60?); in the final showdown the child picks a plan for a sample family's use and defends it with the inequality; at the end the child sees that an inequality turns "it depends" into an exact answer you can check, so a seventh grader learns to solve multi-step problems with rational numbers in any form and to write and solve equations and inequalities of the forms px + q = r, p(x + q) = r and px + q > r or < r.

## Not like
- balance-puzzle (6, spec): one-step equations and inequalities. Here two steps.
- two-trains (8, live): systems with two unknowns. Here one unknown at a time.
- model-my-world (9, spec): equations fit to data. Here equations from stated prices.
- summer-stand (6, spec): two variables in a table and graph. Here solving for the crossing point.

## Who and how
- Grade 7, Math, module "Multi-Step Equations and Inequalities". Standards: 7.EE.3 (solve multi-step real-life and mathematical problems posed with positive and negative rational numbers in any form (whole numbers, fractions, and decimals), using tools strategically; apply properties of operations to calculate with numbers in any form; convert between forms as appropriate; and assess the reasonableness of answers using mental computation and estimation strategies), 7.EE.4 (use variables to represent quantities in a real-world or mathematical problem, and construct simple equations and inequalities to solve problems by reasoning about the quantities: a. solve word problems leading to equations of the form px + q = r and p(x + q) = r, where p, q, and r are specific rational numbers; solve equations of these forms fluently; compare an algebraic solution to an arithmetic solution, identifying the sequence of the operations used in each approach; b. solve word problems leading to inequalities of the form px + q > r or px + q < r, where p, q, and r are specific rational numbers; graph the solution set of the inequality and interpret it in the context of the problem).
- Format: roleplay. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Eight claims from Marcus, six two-kinds rounds, six fine-print rounds, the final showdown. Extra: Swap roles (a partner plays the customer and the student writes the claims). tool.json `modes: ["At the counter", "Swap roles"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.EE.4b | Build each claim as an inequality; solve; graph; answer in words | 20 + 3g < 35 and its ray | 2 |
| 7.EE.4a | Solve px + q = r and p(x + q) = r two ways | arithmetic and algebra steps side by side | 3 |
| 7.EE.3 | Estimate, then work tax, discounts and fees | the bill with fine print | 4 |

## Screens and modes
Header (kit): title "Phone Plan Showdown"; `At the counter`, `Swap roles`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A bright phone store counter, two plan cards from made-up carriers, and Marcus with a big smile. A label reads "Sample prices." The welcome is queued (`welcomeAfter: true`): "Plan B is always cheaper. Trust me! Build his claim from the tiles." First hint: "Drag tiles to build the claim."

**A claim (focus: the tile tray).** At 1366x768 the counter is on top, the tile tray and number line below, and Marcus right; at 680x425 the number line is a tab. The child builds the inequality, then solves it step by step (subtract 20 from both sides, divide by 3). The number line takes an open or closed circle and a direction. The child answers in words from sentence starters. Marcus reacts: he concedes, or doubles down with a new claim.

**Two kinds.** A family bill card: 4 people each pay (x + 5) toward $72. The child solves with arithmetic first (undo in reverse), then with algebra, and the two step lists sit side by side with matching steps linked.

**Fine print.** Tax at 6.5%, 1/4 off the first month, a $0.10 per minute call fee. Each starts with an estimate slider (near $40 or near $60?), then the exact work in any form (0.065 or 6.5/100).

**Showdown.** A sample family's use (7 GB a month, 120 call minutes). The child picks a plan and defends it with the solved inequality.

**Check the claim (the aha).** Marcus: "Okay, okay. It depends." Narrator: "And now you know exactly what it depends on."

**The end.** The claim log with each inequality and graph. `Print` prints it.

**Swap roles (extra).** A partner plays the customer.

## Content
- Two plans from made-up carriers with sample prices labeled "sample prices", near the range of current U.S. prepaid plans and dated; all readable with `Read`.
- Numbers include negatives (a credit of -$5), fractions and decimals.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Tiles and steps can be undone until `Check`.
- Keyboard: Tab to tiles, the inequality sign, step boxes, the number line (arrows move by 1), sentence starters and the estimate slider; Enter places or checks.
- With Motion off Marcus's reactions show as text cards.

## Look
- Accent `--brand` #a3480c signal orange (header, plan cards, buttons); gold #f4c542 (the tile in hand, the solution ray); paper #fbf2eb; ink #2b1203; muted #5e5249.
- Contrast (WCAG 2.1, computed): white on brand 6.02:1; brand on paper 5.45:1; ink on paper 15.96:1; muted on paper 6.84:1; ink on gold 10.85:1.
- Never color alone: open and closed circles are labeled "not included" and "included".
- Different from this batch (balloon sky blue, midway red, diner teal, licorice purple).

## Art
- People (illustrated): Marcus and a sample family, labeled "illustration" (Gemini, `people: true`, 2; cutout yes).
- Local FLUX (`scripts/localart.py`): the phone store (1, 16:9).
- Drawn in code: plan cards with made-up logos, tiles, the number line, receipts.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as Marcus; `wise-mentor` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.claim + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `build`: "Drag tiles to build the claim."
- how `solve`: "Type the next step."
- how `graph`: "Tap the number line, then pick a direction."
- how `answer`: "Pick a sentence starter and finish it."
- how `estimate`: "Slide to your estimate first."
- event, whole, check the claim.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: claim tiles, step checks with exact rationals (`Frac` as described in equation-golf's spec), the solution number line, receipts in cents. Prices sit in a marked block `/* PLANS DATA: begin */ ... /* end */` with the date and source.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Claims | Agree with Marcus | Each answer is checked against the solved inequality. |
| Graph | Shade the whole line | The circle and direction are checked. |
| Two kinds | Solve one way only | Both step lists must be filled. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `build`; `solve`; `graph`; `answer`.
2. Two kinds use `solve`.
3. `estimate`.
4. Check the claim (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.EE.3, 7.EE.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Sample plan prices sit in the range of current U.S. prepaid plans | FCC, "Communications Marketplace Report" (2024), mobile wireless pricing section | U.S. Bureau of Labor Statistics, CPI "Wireless telephone services" | yes |
| Comparing arithmetic and algebraic solutions builds equation sense | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Expressions and Equations" | Kieran (2007), "Learning and teaching algebra at the middle school through college levels", Second Handbook of Research on Mathematics Teaching and Learning | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s19, 2026-11-10): 20 + 3g < 35 exactly when g < 5, a tie of $35 at 5 GB, and Plan B cheaper for every g above 5 (to 20 GB); 4(x + 5) = 72 gives 13 both ways; 6.5% of $35 is $2.28 (half up); 3/4 of $35 is $26.25; 120 minutes at $0.10 is $12; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 counter, tiles and line; at 680x425 line as a tab.
2. Eight claims are built, solved, graphed and answered in words. (7.EE.4b)
3. Six px + q = r and p(x + q) = r problems are solved two ways and compared. (7.EE.4a)
4. Six fine-print problems are estimated, then worked in any form. (7.EE.3)
5. Carriers are made up and prices are labeled sample prices with a date.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: reactions show as text; no network requests.

## Open questions
- The idea card flags a data source (default used: sample prices from made-up carriers set near the FCC and BLS picture of current U.S. prepaid plans, labeled sample prices with the date, checked again before build).
