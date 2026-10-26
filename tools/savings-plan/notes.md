## A 5-minute start

1. Open **Race**. It starts on **Penny vs ten**: Plan A puts in $10 every week, Plan B starts with one cent and doubles it every day. Ask the class who wins a 30-day race before anyone touches anything.
2. Hover over the chart (or Tab to it and use the Left and Right arrows) and walk the days. A leads until day 11, when the penny passes it, $20.47 to $20.00. Day 30 asks for one deposit of $5,368,709.12.
3. Press **Show the shortcut for B** and step through it. The five steps derive the geometric series formula with the plan's own numbers, and step 5 lands on the same $10,737,418.23 as the **Ledger**.

## The two modes

- **Race** (explore, no score): two plans, A (blue, solid, circles) and B (purple, dashed, diamonds). Each plan is an add plan (the same amount more each time) or a multiply plan (the same factor each time), with a first deposit, a step and a period (every day or every week). Each card shows its rule both ways, explicit and recursive, and the deposits so far, this deposit and the balance. **What you have** draws the balance (the partial sum S_n) as dots with flat steps; **What goes in** draws each deposit (the term a_n) as dots. **Fit both**, **Fit the smaller** and **Log scale** change the view. **Who leads** lists every change of leader (a tie counts). **Ledger** lists every deposit day. **Show the shortcut** derives the sum formula for that plan in five steps.
- **Plan Desk** (optional challenge): a season of 8 customers, each with a goal, a deadline, a cap on any one deposit, and sometimes a fixed rule or a limit on the first deposit (locked parts show a lock and the word "fixed"). Build a plan, watch the checks, then **Run the plan** (one run per customer) or say **Can't be done**. A plan that works earns $20, a tight one (no more than 5 percent over the goal) $10 more, and the one right turn-away $15. A perfect season is $225.

## Talk about it

- Which list is the sequence and which is the series? Point to each one on the chart and in the ledger.
- Why does the doubling penny lose for ten days and then win by millions? What does day 30 alone ask for, compared with everything Plan A puts in?
- In the add shortcut, why does every column add to the same thing? In the multiply shortcut, why does almost everything cancel?
- The halving plan adds less and less forever. Why can it never pass $128? (64 / (1 - 0.5) = 128.)
- Gus can start with at most $5 and never put in more than $45. Why does a steady climb reach $950 when no doubling-style plan can?
- Ivy's goal is $2,000. How can you prove no plan works, without trying them all?

## Good to know

- Every deposit is rounded to the cent (half up) and the balance is the sum of the rounded deposits, so the ledger is exact. The shortcut and the formula use exact values; the drawer shows both, and they can differ by a few cents for multiply plans (they match exactly for add plans).
- Above $1 trillion, money shows as scientific notation with three significant figures, such as $7.52 × 10^107 for the doubling penny over 365 days.
- Checked numbers: Penny vs ten, B takes the lead on day 11 ($20.47 to $20.00), day 20 deposit $5,242.88, day 30 deposit $5,368,709.12 and balance $10,737,418.23. Climb vs steady, tied on day 267 at $780.00, B leads from day 274 ($820 to $800). Raise vs steady, B takes the lead on day 176 ($545.91 to $520.00). Halving vs steady, A takes the lead on day 43 ($140.00 to $127.00).
- Plan Desk model plans (all tight): Ana first $15, add $0 ($300.00). Ben first $6.74 ($500.24; $6.73 is 2 cents short). Cam first $18.71 ($400.10). Dee add $2.67 ($400.40; $2.66 is 80 cents short). Eli first $0.10 ($102.30; $0.12 asks for $61.44 on day 10). Fay first $67.22 ($300.02). Gus first $5, add $0.97 ($956.60). Ivy cannot be done: the best add plan starts at $20 and climbs to $150, 20 x (20 + 150) / 2 = $1,700.
- With multiply steps of 0.01, the best Gus multiply plan within his limits reaches about $717, far short of $950.
- Over a long horizon the halving plan's rounded ledger can land exactly on $128.00 (the small deposits round up before they round to zero); it never goes past it.
- Keyboard: the chart cursor takes Left and Right (deposit by deposit), Home and End. The first-deposit slider moves a cent per arrow press and a dollar with Page Up and Page Down. Escape closes the ledger and the shortcut. With Motion off, views change at once and the run plays at the same pace without the bars growing.
- Sources: OpenStax, Algebra and Trigonometry 2e, sections 13.2 to 13.4 (CC BY 4.0); Common Core F-IF.A.3 and A-SSE.B.4. Customers and goals are invented.
