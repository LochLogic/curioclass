# Savings Plan

## One idea
Every saving plan is two lists at once, what you put in each time (a sequence) and what you have (its sum, a series),
and racing two plans side by side shows a doubling penny lose for ten days, win by millions, and ask for deposits
nobody could ever pay.

## Not like
- compound-interest-garden (CTE): money grows from interest on a balance over decades. Here there is no interest at
  all; the growth is in the deposits themselves, and the balance is a finite series you can see term by term.
- outbreak-model: continuous exponential growth and logarithms for "when". Here everything is discrete: term n,
  partial sum S_n, explicit and recursive rules, and the two sum shortcuts.
- corner-store (same format, grade 2): a bright snack stand counting coins against a clock. Here a dark ledger desk,
  customers with goals and limits, and plans that run week by week. No coins to count, no clock.
- first-apartment-budget: a monthly budget you survive. Here there is no budget, only the shape of a deposit plan.
- rollercoaster-polynomials (graphing sibling): reuses the plane, but plots discrete dots and steps, never a
  continuous curve, and the scene is a ledger, not a track.
- which-model-wins (grade 9): fits models to data. Here you build the sequence and the data comes from it.

## Who and how
Grade 11, math (Algebra 2, Sequences and Series). Driver: students, on their own laptops. 25 to 40 minutes.
Standards: F-IF.A.3 (sequences are functions on the integers, defined recursively), A-SSE.B.4 (derive and use the
finite geometric series formula). Arithmetic series also appears, as its natural partner.
Look: links `kit:curio` then `kit:theme-912`; tool accent `--brand` a ledger green (about #2fa37a, checked for AA
against the theme's panel and paper). Readouts use the theme's readout font. No confetti, no mascot.

## Screens and modes
Header: title "Savings Plan" with small line "Sequences and series, Curio Class"; mode buttons (`.seg`) **Race** and
**Plan Desk**; icon buttons **Motion**, **Sound**, **Read** (ids `motion`, `sound`, `read`). Read speaks the panel
`hint`. Opens in Race with preset 1 loaded. Mode change calls `Curio.stop()` and keeps each mode's state.

### Race (explore, no score)
- Stage (left, about 65 percent): the chart (graphing plane). x axis "day", y axis "dollars". Plan A in `--gr-1`
  solid, Plan B in `--gr-2` dashed. Each plan is drawn as dots at each deposit with flat steps between (the balance
  does not change between deposits). Lead-change days get a thin vertical marker and a label ("B leads, day 11").
- Under the chart, a toggle (`.seg`): **What you have** (balance, S_n, default) and **What goes in** (each deposit,
  a_n, drawn as dots only). A second toggle: **Fit both**, **Fit the smaller**, **Log scale**.
- Panel (right): two plan cards, A and B. Each card has:
  - a name field (default "Plan A", "Plan B"; 20 characters max),
  - type buttons **Add the same amount** / **Multiply by the same number**,
  - **First deposit** (number input plus slider, $0.01 to $1,000.00, step $0.01),
  - **Add** ($0.00 to $100.00, step $0.01) or **Times** (0.50 to 3.00, step 0.01), whichever the type uses,
  - **Every** buttons **day** / **week**,
  - the rule in text, both forms: explicit ("a_n = 0.01 x 2^(n - 1)") and recursive ("a_1 = 0.01, a_n = 2 x a_(n-1)"),
  - a live readout: deposits so far, this deposit, balance now.
- Below the cards: **Days** slider (7 to 365, default 30), the preset buttons, the lead readout, and **Show the
  shortcut** (one per card: "Show the shortcut for A", "for B").
- Presets (buttons): **Penny vs ten**, **Climb vs steady**, **Raise vs steady**, **Halving vs steady**. Editing any
  control after a preset just changes the plans (no "custom" state needed).
- **Ledger** button opens a drawer over the stage: a table with one row per day on which either plan deposits.
  Columns: Day, A deposit, A balance, B deposit, B balance. Lead-change rows are marked with a "lead" tag in a
  column of their own (not color only). **Close ledger** returns to the chart.
- Shortcut drawer (from **Show the shortcut**): a step-by-step derivation using that plan's real numbers, with
  **Back**, **Next step** and **Close**. Content below.

### Plan Desk (the tycoon, optional challenge)
You run a small savings-plan desk for one season of 8 customers. Each customer pays a fee if your plan works.
- Top strip: "Customer 3 of 8", desk cash ("Desk cash: $60"), and a row of 8 small slots that fill with a word
  ("works", "tight", "short", "turned away") as the season goes.
- Customer card (left): name, what they are saving for, their words (quote), and a facts list: Goal, Deadline
  (with "weeks" or "days"), Most in one deposit, First deposit at most (if any), Fixed rule (if any).
- Plan builder (center): the same controls as a Race card, but the period and length are set by the customer and
  any fixed part is locked with a lock icon and the word "fixed". The chart shows deposits as bars and the balance
  as a stepped line, with a horizontal goal line and a horizontal cap line on the bars, both labeled.
- Checks (under the chart), each with a word and an icon, updating live:
  "Reaches the goal by the deadline", "No deposit over the cap", "First deposit within the limit" (only when the
  customer has one), "Follows the customer's rule". Each reads "yes" or "no" plus the number ("short by $14.20").
- Buttons: **Show the formula**, **Run the plan**, **Can't be done**. After a result: **Next customer**. After
  customer 8: the season summary with **Play the season again**.

## Content

### Race presets (all checked by computing them; see Sources)
Deposits happen on day 1 of the plan and then every 1 or 7 days (deposit k lands on day 7(k - 1) + 1 for weekly).
1. Penny vs ten. A: "Ten a week", add $0, first $10, every week. B: "Doubling penny", multiply 2, first $0.01,
   every day. Days 30. Lead changes: A leads from day 1; B takes the lead on day 11 ($20.47 to $20.00). Day 30:
   B deposit $5,368,709.12, B balance $10,737,418.23, A balance $50.00. Day 20 deposit: $5,242.88.
2. Climb vs steady. A: "Steady twenty", add $0, first $20, weekly. B: "Add a dollar", add $1, first $1, weekly.
   Days 280. A leads; tied on day 267 at $780.00 (week 39); B leads from day 274 ($820 to $800).
3. Raise vs steady. A: "Steady twenty" as above. B: "Ten percent raise", multiply 1.10, first $5, weekly. Days 200.
   B takes the lead on day 176 (week 26): $545.91 to $520.00.
4. Halving vs steady. A: "Steady twenty". B: "Halving", multiply 0.50, first $64, weekly. Days 70. B leads
   from day 1; A takes the lead on day 43 (week 7): $140.00 to $127.00. B never reaches $128; a note under the lead
   readout says "Halving plans add less and less: this one can never pass $128."

### Shortcut steps (the drawer fills in the plan's own a, r or d, and n = deposits so far)
Multiply plans:
1. "Write the sum: S = a + ar + ar^2 + ... + ar^(n-1)."
2. "Multiply every term by r: rS = ar + ar^2 + ... + ar^(n-1) + ar^n."
3. "Line them up and subtract. Every middle term cancels: S - rS = a - ar^n."
4. "Factor: S(1 - r) = a(1 - r^n), so S = a(1 - r^n) / (1 - r)."
5. "With this plan: S = [a](1 - [r]^[n]) / (1 - [r]) = [value]. The ledger says [ledger total]."
Add plans:
1. "Write the sum forward: S = a_1 + a_2 + ... + a_n."
2. "Write it backward: S = a_n + a_(n-1) + ... + a_1."
3. "Add the two rows. Every column adds to the same thing, a_1 + a_n, and there are n columns: 2S = n(a_1 + a_n)."
4. "So S = n(a_1 + a_n) / 2, where a_n = a_1 + (n - 1)d."
5. "With this plan: S = [n]([a_1] + [a_n]) / 2 = [value]. The ledger says [ledger total]."
Special case r = 1: the drawer shows only "Every deposit is the same: S = n x a = [value]. (The shortcut would divide
by zero, so it is not needed.)"
Each step animates its row in (a 250 ms fade, none in calm mode); the cancelling terms in step 3 get a strike line.

### Plan Desk customers (fixed order, one season)
Period is weeks unless marked days. "Tight" means the total is at least the goal and at most goal x 1.05.
1. Ana, used bike. Goal $300, 20 weeks, cap $25. No fixed rule. Quote: "Any plan is fine, I just want the bike by
   summer." Model plan: add $0, first $15, total $300.00 (tight).
2. Ben, concert trip. Goal $500, 26 weeks, cap $40. Fixed: add $1 each week. Unknown: first deposit. Quote: "I'm
   doing the add-a-dollar challenge. What should my first deposit be?" Model: first $6.74, total $500.24, last $31.74.
   ($6.73 gives $499.98: short.)
3. Cam, laptop repair. Goal $400, 12 weeks, cap $60. Fixed: multiply 1.10. Unknown: first deposit. Quote: "My hours
   go up every week, so each deposit is 10 percent more than the last." Model: first $18.71, total $400.10, last
   $53.38.
4. Dee, keyboard. Goal $400, 16 weeks, cap $50. Fixed: add type, first deposit $5.00. Unknown: the amount added.
   Quote: "I can only start with five dollars. Then the same raise every week." Model: add $2.67, total $400.40,
   last $45.05. ($2.66 gives $399.20: short.)
5. Eli, fishing kit. Goal $100, 10 days, cap $60. Fixed: multiply 2. Unknown: first deposit. Quote: "I love the
   doubling penny. Double it every day, but I can't put in more than sixty dollars in one day." Model: first $0.10,
   total $102.30, last $51.20. ($0.11 works but is not tight: $112.53. $0.12 breaks the cap: last $61.44.)
6. Fay, class trip. Goal $300, 10 weeks, cap $70, first deposit at most $70. Fixed: multiply 0.80. Unknown: first
   deposit. Quote: "My summer job is winding down, so each deposit is 80 percent of the one before." Model: first
   $67.22, total $300.02, last $9.02.
7. Gus, drum kit. Goal $950, 40 weeks, cap $45, first deposit at most $5. No fixed rule. Quote: "Open plan. I can
   barely start, but I can climb." Model: add, first $5, add $0.97, total $956.60, last $42.83 (also first $5, add
   $1.00: $980.00). No multiply plan works: the best one (first $5, times about 1.058) reaches only about $735.
8. Ivy, car down payment. Goal $2,000, 20 weeks, cap $150, first deposit at most $20. No fixed rule. Quote: "Open
   plan. Can you get me there?" Impossible: the most any add plan can reach is start at $20 and climb to $150,
   20 x (20 + 150) / 2 = $1,700; a multiply plan with the same first and last deposits reaches less.

Fees: plan works $20; tight bonus $10; correct "Can't be done" on Ivy $15; anything else $0.
Result lines (on screen):
- Works: "Plan works: $[total] by [week/day] [N]. Fee $20." plus "Tight plan, +$10." when tight.
- Short: "Short by $[gap] at [week] [N]. [Name] goes elsewhere."
- Cap: "[Week] [k] asks for $[deposit], over the $[cap] cap. [Name] goes elsewhere."
- First limit: "The first deposit is over $[limit]. [Name] goes elsewhere."
- Wrong turn-away: "This one could be done. One plan that works: [model plan]."
- Right turn-away (Ivy): "Right call. The best possible is $1,700, short of $2,000. Fee $15."
- Ivy run anyway: shows the failing check as above, then "No plan can reach $2,000 here. The best is $1,700."
Season summary: totals (plans that worked, tight plans, right calls, desk cash out of a possible $225) and one line
per customer: what you did and the model plan. Ends: "Season over. Every plan here was a sequence; every goal was a
sum."

### Show the formula (Desk)
Shows the explicit sum formula for the chosen type with the customer's known values filled in and the unknown as a
boxed "?", for example Ben: "S_26 = 26(a_1 + a_26) / 2, with a_26 = a_1 + 25 x 1". Under it: "Your plan right now:
S_26 = $[current]". It never solves for the unknown.

## Interactions in detail
- Rounding: every deposit is rounded to the cent (half up) and the ledger balance is the sum of rounded deposits.
  Shortcut and formula values are exact and may differ by a few cents; the drawer shows both. Above $1 trillion,
  stop rounding and show amounts as "$1.07 x 10^13" style scientific notation with three significant figures.
  Desk checks always use the ledger.
- Race updates live on every input (no Run button). Lead readout lists up to 4 lead changes in order, then "and
  [k] more"; with none it says "A leads the whole way" (or B, or "Tied the whole way" for identical plans).
- Ties count as their own state: "Tied on day 267 at $780.00." A lead change is any change of leader, tie included.
- Fit both: y range 0 to 1.1 x the larger balance. Fit the smaller: 0 to 1.1 x the smaller plan's top value; the
  larger plan's steps run off the top and get a small "off the chart" arrow with its value. Log scale: plot
  log10(dollars) and label ticks "$0.01", "$1", "$100", "$10,000" and so on; values of $0 are not drawn. View
  changes use `g.view` with a 400 ms move (instant in calm mode).
- Many dots: up to 365 per plan. If the engine's point handles are heavy, draw the dots and steps in the tool's own
  SVG layer positioned with `g.px` (allowed by the family rules); dots are not draggable.
- Hover or focus on the chart (use `g.trace`-style keyboard stepping, Left and Right arrows by deposit) shows a
  readout: "Day 11. A: deposit $0, balance $20.00. B: deposit $10.24, balance $20.47."
- Type change keeps the first deposit and resets the step to $0 add or times 1.00, then to the last value used for
  that type on that card if there was one.
- Input limits: typing outside a range clamps to the nearest limit and shows "Kept between $0.01 and $1,000.00"
  under the field for 3 seconds. Blank or non-numbers revert to the last good value.
- Desk: inputs update the chart and checks live. **Run the plan** plays the ledger one row every 120 ms (the bars
  fill, the balance line climbs; in calm mode rows appear without the fill movement, same timing), then shows the
  result, adds the fee to desk cash with a short tick-up, and plays `Curio.yes()` on a working plan only. One run per
  customer; the builder locks after it. **Can't be done** asks "Turn [Name] away?" with **Yes, turn away** and
  **Keep working**.
- While running, all builder controls and the three buttons are disabled; **Next customer** appears after the result.
- Read button: in Race, reads the lead readout; in Desk, reads the customer quote and facts.
- Speech: welcome line on first entry to each mode (after the first tap), customer line when each customer appears,
  shortcut intro when a drawer opens, season line at the end. `Curio.stop()` on mode change, reset and drawer close.
- Reset: **Play the season again** clears the desk. Presets reset Race. State is not saved across visits except
  Motion (kit).
- Narrow window: panel drops under the stage; ledger drawer becomes full width. Works in a 16:10 iframe.
- Accessibility: every color pair also differs by dash or shape; checks use words; all buttons 44 px or more;
  focus visible; the table is a real table with headers.

## Art
- desk-surface: dark walnut desk top seen from above, soft lamp light from one corner, empty, no objects, subtle grain;
  16:10; cutout no; people no. (Plan Desk background, heavily darkened behind panels.)
- penny-coin: a single worn copper one-cent coin, slight angle, studio light, plain dark background; 1:1; cutout yes;
  people no. (Icon on the Penny vs ten preset button and on Eli's card.)
- vault-door: a round steel bank vault door, closed, dim light, front view; 4:3; cutout no; people no. (Season
  summary header.)
Everything else (chart, ledger, cards, icons, locks, check marks) is drawn in code. No people, faces or hands.

## Voice
Bank "hs-narrator", voice "Kore", style "Read clearly and naturally, at a moderate pace". 14 lines.
- race-welcome: "Two saving plans, one race. Change either plan and watch who pulls ahead, and when."
- race-penny: "The doubling penny starts with one cent. Watch day eleven, then look at what day thirty asks you to put in."
- shortcut-multiply: "Here is the shortcut for a multiply plan. Write the sum, multiply it by the ratio, and subtract. Almost everything cancels."
- shortcut-add: "Here is the shortcut for an add plan. Write the sum forward and backward, then add the two rows. Every column is the same."
- desk-welcome: "Welcome to the Plan Desk. Each customer brings a goal, a deadline and a limit. Build a plan that works, or say it can't be done."
- cust-ana: "Ana needs three hundred dollars for a bike in twenty weeks, never more than twenty five dollars a week. Any plan is fine."
- cust-ben: "Ben adds one dollar more every week. He needs five hundred dollars in twenty six weeks. Pick his first deposit."
- cust-cam: "Cam's deposits grow ten percent every week. He needs four hundred dollars in twelve weeks. Pick his first deposit."
- cust-dee: "Dee starts with five dollars and adds the same raise every week. She needs four hundred dollars in sixteen weeks."
- cust-eli: "Eli wants to double every day for ten days and reach one hundred dollars, never more than sixty dollars in a day."
- cust-fay: "Fay's deposits shrink to eighty percent of the last one each week. She needs three hundred dollars in ten weeks."
- cust-gus: "Gus can start with five dollars at most and never go over forty five a week. He needs nine hundred fifty dollars in forty weeks."
- cust-ivy: "Ivy needs two thousand dollars in twenty weeks. She can start with twenty dollars and never go over one hundred fifty a week."
- desk-end: "That's the season. Look back at each plan, and at the one that could never work."

## Family engine
Graphing (`kit:graphing`, built by rollercoaster-polynomials). Uses: `Plane` for both charts (x day or week from 0
to the horizon, y dollars), `g.px` to place the tool's own dots, steps, bars, goal and cap lines, `g.view` for the
fit buttons, `g.label` for lead markers and log tick labels, `g.slider` for every numeric control, the trace-style
keyboard readout, and `--gr-1` / `--gr-2` with their dash patterns for A and B. No continuous `g.fn` curves. If the
engine has no log axis, the tool plots log10 values itself as described; it does not change the engine.

## Sources
- Standards text: Common Core State Standards for Mathematics, F-IF.A.3 and A-SSE.B.4,
  https://www.thecorestandards.org/Math/Content/HSF/IF/ and https://www.thecorestandards.org/Math/Content/HSA/SSE/
- Sum formulas and both derivations: OpenStax, Algebra and Trigonometry 2e, sections 13.2 to 13.4 (arithmetic and
  geometric sequences, series), https://openstax.org/books/algebra-and-trigonometry-2e/pages/13-4-series-and-their-notations
- Every preset and customer number above was computed with the rounding rule in this spec (Python check by the spec
  agent, 2026-10-25); the verify agent should recompute them in the tool's own ledger.
- No real prices, rates or people are used; customers and goals are invented.

## Done when
1. Race opens on Penny vs ten: the lead readout says B takes the lead on day 11 ($20.47 to $20.00), and the ledger's
   day 30 row shows B deposit $5,368,709.12 and balance $10,737,418.23.
2. Climb vs steady reports a tie on day 267 at $780.00 and B leading from day 274; Halving vs steady reports A taking
   the lead on day 43 and the $128 note.
3. Show the shortcut walks all 5 steps for a multiply plan and for an add plan with the plan's own numbers, the
   formula and ledger totals agree within a few cents, and r = 1.00 shows the special-case line instead.
4. What goes in / What you have, Fit both, Fit the smaller and Log scale all redraw correctly at 365 days with the
   doubling penny (no hang, scientific notation above $1 trillion, nothing drawn at $0 on log).
5. Plan Desk: entering each model plan in the Content list gives "works" (and "tight" where marked); Ben at $6.73,
   Dee at $2.66 and Eli at $0.12 fail with the right result line.
6. Gus: no multiply plan passes the goal check within the caps; the add model plan does.
7. Ivy: Can't be done earns $15 with the $1,700 line; turning away any other customer shows a working plan and $0.
   A full perfect season ends at $225.
8. Fixed rules are locked and labeled; checks read in words, not only color; everything works by keyboard alone.
9. Motion off: no movement, same run timing; Sound off: no chimes; voice lines play once each at the right moments.
10. Usable in a 16:10 iframe and on a narrow laptop window; no network requests; no em dashes in any text.
