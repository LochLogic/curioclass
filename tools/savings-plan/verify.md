FIX (no blockers): the money and all 10 "Done when" checks pass. Three things should be fixed: voice lines that get dropped for good, a nearly invisible doubling-penny line on Log scale at 365 days, and the 16:10 preview hiding the main inputs below the fold.

# Verify: savings-plan (2026-10-25)

How I checked: I recomputed all the money in Python with exact fractions and rounded each deposit half up to the cent: every preset, the ledger rows, both sum formulas, all 8 customers plus their near-miss values, the best plans for Gus and Ivy, the fees and the season total. I bundled with `CURIO_DRAFT=1` and drove the tool through CDP, using my own copy of cdp.py that collects console errors and exceptions. I took about 70 frames at 1400x900, 1920x1080, 1280x720, 1000x625, 800x500, 680x425, 760x900 (stack), 375 mobile emulation and 375 in an iframe host. I tested calm and motion runs, keyboard, Tab order and voice playback, and traced which clip actually plays. Art (3 images) and voice (14 clips) landed while I worked; the later frames use them.

## What passes

- **Money (all match the spec and notes exactly):**
  - Penny vs ten: B takes the lead on day 11 ($20.47 to $20.00). Day 20 deposit $5,242.88. Day 30: B deposit $5,368,709.12, B balance $10,737,418.23, A balance $50.00.
  - Climb vs steady: tied on day 267 at $780.00, then B leads from day 274 ($820 to $800).
  - Raise vs steady: B takes the lead on day 176 ($545.91 to $520.00).
  - Halving vs steady: A takes the lead on day 43 ($140.00 to $127.00).
  - Doubling penny over 365 days: $7.52 x 10^107.
  - The tool rounds the explicit term a x r^(k-1) to the cent. Rounding each deposit from the previous rounded one would give different numbers ($546.69 on day 176, Cam $400.04, Fay $6.721 working). The spec numbers come from the explicit rule, and so does the tool. Under that rule a halving plan's ledger reaches exactly $128.00 and never goes past it (the 365-day frame shows $128.00). The tool's wording "can never pass $128" and the notes are correct; the spec's "never reaches $128" is not.
- **Customers (all match):**
  - Ana $300.00, Ben $500.24, Cam $400.10, Dee $400.40, Eli $102.30, Fay $300.02 and Gus $956.60 are all tight in the tool.
  - Failures match: Ben at $6.73 is short $0.02, Dee at $2.66 is short $0.80, and Eli at $0.12 gives "Day 10 asks for $61.44, over the $60 cap".
  - Eli at $0.11 works but is not tight ($112.53). Cam at $18.70 and Fay at $67.21 both fail as "short".
  - Gus at a $6.00 first deposit fails the first-deposit limit.
  - Gus: the best multiply plan within his limits is $716.58 (first $4.63, times 1.06), found by brute force in both Python and the page. It is nowhere near $950. The notes say "about $717", which is right; the spec's "about $735" is the continuous estimate.
  - Ivy: the best add plan in whole cents is $1,699.60 (first $20, add $6.84) and the best multiply plan is $1,284.06. "Can't be done" earns $15; running a plan anyway shows the short line, then "No plan can reach $2,000 here. The best is $1,700."
  - Turning away any of the other 7 shows a working model plan and earns $0.
  - A perfect season ends at $225 (7 of 7 worked, 7 tight, 1 of 1 right call).
- **Shortcut drawer:** the multiply plan (penny, 30 days) gives $10,737,418.23 and the ledger agrees. The add plan (add a dollar, 280 days) gives $820.00 and agrees. The 10 percent raise gives $743.15 and agrees. With times 1.00 the drawer shows only the one-line special case ("Step 1 of 1"). The step 3 strike-through renders correctly.
- **Views at 365 days:** What goes in, Fit both, Fit the smaller (with the off-the-chart arrow and value) and Log scale all redraw with no hang. Scientific notation appears above $1 trillion, and $0 is not drawn on the log scale (halving, What goes in). Going from Log back to Fit both lands exactly on [0, 11,811,160].
- **Desk:**
  - Fixed parts are locked and labeled "fixed" with a lock: Ben's add, Dee's first deposit and type, the period for everyone.
  - Checks read "yes" or "no" plus a number.
  - All builder controls are disabled during a run, and there is one run per customer.
  - The formula never solves for the unknown (Ben shows "a1 = ?", Dee "15 x ?", Cam "a1 = ?").
  - Run timing is the same with Motion on or off (2.8 s and 2.9 s for 20 rows).
- **Keyboard:**
  - The chart cursor steps by deposit, and its aria-valuetext matches the spec format word for word.
  - The first-deposit slider moves one cent per arrow press.
  - Typing 5000 clamps to 1000.00 with the "Kept between" message; "abc" reverts.
  - Escape closes the ledger and returns focus to the Ledger button.
  - A type change keeps the first deposit and brings back the last step used for that type.
- **Lead readout:** identical plans give "Tied the whole way."; a tie counts as a lead change.
- **Contract:**
  - One file, no fetch, XHR or http references, no console errors in any frame.
  - No em dashes; "Curio Class" is never shortened.
  - lines.json has bank hs-narrator, voice Kore, the batch style, and 14 lines identical to `L` and `allLines()`; all 14 have clips.
  - prompts.json has the 3 assets, all `people: false`.
- **Phone widths:** at 375 there is no horizontal page scroll and chart ticks are about 10.5 px. At 1280x720 they are about 10.5 to 12 px.
- **kit/graphing.js g.view fix:**
  - It is backward compatible. On the last frame (t >= 1) it now assigns the target range exactly, where before it computed x0 + (x1 - x0) x 1. The result is the same for normal ranges and only differs where floating point lost precision.
  - Instant views (ms 0 or calm) go through the same apply(1) path.
  - It is documented in docs/families/graphing.md. It is not yet in BATCH-G11-LOG.md (that is the builder's or integrator's line to add).
  - rollercoaster-polynomials, imaginary-island, outbreak-model, ferris-wheel, undo-machine and savings-plan all bundle with CURIO_DRAFT=1. Each loads at 1400x900 and 680x425, cycling through every mode, with no console errors or exceptions.

## Findings

1. **Voice lines can be dropped for good** (src.html:1258, `narrate`). How serious: should fix.
   - What is wrong: a key goes into `said` when it is queued, not when it is spoken, and `hush()` empties the queue. Any line still waiting when the student clicks a preset, a shortcut, Run, Next or a mode button never plays.
   - How I saw it (clip trace):
     - A first tap queues race-welcome then race-penny. Clicking a preset during the roughly 6 s welcome drops race-penny. Clicking **Penny vs ten** afterwards (its own trigger) cannot bring it back.
     - The same happens to the customer line: entering Plan Desk and leaving or pressing Run during the desk welcome drops cust-ana for the whole season.
   - This is the same voice pattern the batch log flags for ferris-wheel.
2. **The doubling-penny line is nearly invisible on Log scale at 365 days** (src.html:642 and 659: the dot radius drops to 2.6 above 150 deposits, with a 1.2 px `--paper` outline). How serious: should fix.
   - What is wrong: with 365 dark-outlined diamonds packed together, B reads as a dark hairline on the dark plot. That straight line is the point of the log view (frame 14-365-log, zoomed). Fit both at 365 has the same thin-dot look but is less critical.
   - Suggestion: a thinner or no outline, or skip dots above some count and keep the stroked step path.
3. **The 16:10 preview hides the main inputs below the fold.** How serious: should fix (judgment call against the batch rule "controls visible without scrolling").
   - Race at 680x425 and 800x500: presets, view and scale are visible, but both plan cards, the Days slider (800x500) and the shortcut buttons are below the panel fold. Even at 1000x625 the cards start at 668 px.
   - Desk at 680x425 and 800x500: **Run the plan** (bottom at 562 px) and **Can't be done** are below the fold, and the customer card (quote and facts) is last in the panel (bottom at about 1000 px). The goal and cap are still readable on the chart.
   - The preview looks inviting and readable (chart text about 10 px).
4. **Season summary shows a stale line** (src.html:1128 and 1230). How serious: nit.
   - The deskbar's sum line still reads Ivy's "$2,000 in 20 weeks, at most $150 a week..." under "Season over" (frame 20-season, wide layout).
   - In the wide layout the right panel is empty during the summary apart from the hint.
5. **Multiply factors are shortened in result text** (src.html:455 `rnum`). How serious: nit.
   - Checks, results and the summary say "times 1.1" and "times 0.8", while the customer rule and slider say "1.10" and "0.80" (the spec writes "times 1.10").
6. **"$0.1" log tick** (src.html:481 `logTick`). How serious: nit.
   - A log axis whose lowest decade is a tenth prints "$0.1"; as money it should read "$0.10" (frame 15).
7. **Ivy's "$1,700" is an upper bound, not a reachable plan.** How serious: nit, the logic is right.
   - In whole cents the best is $1,699.60, because $130 / 19 weeks is not a whole cent.
   - "The best possible is $1,700" is fine as a bound; "at most $1,700" would be exact.
8. **Ledger at 375 px scrolls sideways inside the drawer.** How serious: nit.
   - The drawer is 510 px of content in a 373 px box, so the Lead column starts off screen. There is no page scroll.
9. **"Fixed rule: None: an open plan"** (customer card). How serious: nit.
   - It reads awkwardly; "None (open plan)" would be smoother.
10. **Recursive rule wraps** in the 540 px wide Race card at 1280 and 1400 px ("a_n = 2 x" / "a_(n-1)"). How serious: nit.

## Unsure

- Item 3 depends on how strictly "controls visible without scrolling" applies to a two-mode tool with two full plan cards. The compact panel does put presets and view controls first, so the preview is usable to explore but not to edit a plan.
- I traced voice by watching which audio clips start. I did not listen to the clips or check the art for quality (both arrived mid-check; prompts.json still says `review: pending`).
- Sound off was not traced separately; tones and voice go through the kit, which gates them on `sound`.

## Re-verify (2026-10-25)

FIX (no blockers): the three should-fix items and most nits are fixed and the money is unchanged, but a new voice gap is left: when the first tap lands on a preset or a shortcut button, the welcome it unlocks is cut after about 0.1 s and marked said, so that mode's welcome is never heard.

How I checked: fresh `CURIO_DRAFT=1` bundle (706 KB), my own CDP driver that wraps `Audio` to log every clip start, cut and end by line key, and real `Input.dispatchMouseEvent` clicks (instant, and with a 120 ms press-to-release hold like a real mouse). 15 voice scenarios. Frames at 680x425, 800x500, 1000x625, 1400x900, 760x900, 375 mobile and 375 in an iframe host; no console errors or exceptions in any frame. Money recomputed in Python with exact fractions (explicit term rounded half up to the cent) and compared with the page's `leadLines()` and `evaluate()`.

### Earlier findings

1. **Voice lines dropped for good:** fixed. `narrate` now marks a line said only when it starts (src.html:1305) and a hush drops only lines that never started.
   - Climb at 2 s into race-welcome: race-penny dropped; clicking Penny vs ten later plays race-penny in full.
   - Plan Desk, Race at 2 s, Plan Desk at 6 s: cust-ana plays on return (desk-welcome, which had started, is not repeated).
   - Shortcut B mid-welcome: shortcut-multiply plays; race-penny comes back from its preset.
   - Run during desk-welcome or cust-ana does not cut either; Next cuts the current customer line and starts the next one (Ana, Ben, Cam in a row; all 8 customers and desk-end through a full season).
   - Read mid-line (Race at 2 s, Desk at 1 s, during cust-ana, on the season summary) stops the clip and speaks the hint and its detail; nothing queued starts after it. Play the season again queues cust-ana once.
   - Sound off: no clips start; Read still speaks (forced).
2. **Penny line on Log scale at 365 days:** fixed. B is a clear dashed purple line from $1 to 10^107 at 1400x900, 800x500 and 375 (log365 frames); Fit both at 365 is also clean.
3. **16:10 preview:** fixed (judgment). Race at 680x425 and 800x500 opens on the A/B plan tabs with one full card above the fold; Days starts at 428 px, presets and shortcuts are below. At 1000x625 card, Days and presets all show. Desk at 680x425 and 800x500 shows the customer card, Run the plan and Can't be done above the fold; the Plan builder starts at 426 px, just below.
4. **Stale season line:** mostly fixed. The deskbar now reads "Desk cash $0 of a possible $225." under "Season over". Left: the right panel is still empty during the summary, and its hint still says "Plan Desk. Build a plan... press Run the plan", which Read speaks first on the summary. Nit.
5. **Shortened factors:** fixed. Checks read "times 1.10 (fixed)"; the summary says "times 1.10", "times 0.80", "times 2.00".
6. **"$0.1" log tick:** fixed. Ticks read "$0.01 | $0.10 | $1 | $10".
7. **Ivy "$1,700":** unchanged ("The best is $1,700", "The best possible is $1,700"). Nit, logic right.
8. **Ledger at 375:** fixed. Drawer scrollWidth 373 = clientWidth, all 7 columns show, no page scroll.
9. **"None: an open plan":** fixed ("None (open plan)").
10. **Recursive rule wrap at 1400:** fixed ("a1 = 0.01, an = 2 x an-1" on one line).

### New finding

11. **The unlocking tap can kill the welcome it starts** (src.html:1285-1293 `firstTap`, with the preset handler at 900 and `openShortcut` at 986). How serious: should fix.
   - What is wrong: `firstTap` runs on pointerdown and queues the welcome on a 0 ms timer, so it starts before the click. If that tap is a preset, a shortcut button or another control whose click calls `hush()`, the click cuts the welcome about 0.1 s in. It has started, so it is marked said and no trigger brings it back; Race's welcome is then never heard in the session.
   - How I saw it (120 ms hold): first tap Climb vs steady: race-welcome start at 3 ms, cut at 138 ms (0.1 s played), nothing after. First tap Show the shortcut for B: race-welcome cut at 0.1 s, shortcut-multiply plays. With an instant CDP click (press and release in the same tick) the click wins the race and the welcome plays in full, which is why a fast-click test passes.
   - Presets and shortcuts are the likeliest first taps in Race. Possible fixes: queue the welcome on click or pointerup instead of pointerdown, or skip it (unmarked) when the unlocking tap is a control that speaks or hushes.
   - Related, nit: if the first tap is Read, Race's welcome is skipped (by design) and no later tap queues it.

### Art

- Penny cutout: clean round edge on the Penny vs ten preset and Eli's card, no halo.
- Vault door: a sharp banner at the top of the season summary.
- Desk surface: a heavily dimmed wood texture behind the Plan Desk chart, read as faint warm grain; charts and labels stay clear.

### Money (unchanged)

- Penny vs ten B leads day 11 ($20.47 to $20.00), day 20 deposit $5,242.88, day 30 $10,737,418.23 vs $50.00. Climb tied day 267 at $780.00, B from day 274 ($820 to $800). Raise B day 176 ($545.91 to $520.00). Halving A day 43 ($140.00 to $127.00). Penny 365 days $7.52 x 10^107 (page ledger agrees to the cent).
- Customers, page = Python: Ana $300.00, Ben $500.24 ($6.73: $499.98), Cam $400.10, Dee $400.40 ($2.66: $399.20), Eli $102.30 ($0.12 goes over the cap on day 10 at $61.44), Fay $300.02, Gus $956.60.
