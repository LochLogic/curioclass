# Interest Rate Dial

## One idea
Turn one big dial on the bank door of Maple Street and watch four neighbors react at once: Abe's savings grow faster, Keisha's car payment climbs until she signs a fixed rate and the dial can no longer touch it, Luis's variable card balance keeps swelling, and Priya decides at what rate a loan for a second cafe stops being worth it.

## Not like
- economy-checkup (CTE 6-8, concept): four neighbors read real past years of inflation and jobs on a chart. Here there is no history and no inflation; one rate lever, live math on every card, and a fixed-versus-variable lock.
- compound-interest-head-start (CTE 9-12, spec): two savers race over fifty years; time is the lever. Here saving is one of four views, five years only, and the lever is the rate.
- the-credit-card-diaries (CTE 9-12, spec): one person's credit report over four years of choices. Here no credit score; one card balance and how the rate and the minimum payment set its cost.
- fed-chair (social studies 12, concept): set the Fed's rate and watch inflation and jobs. Here no economy-wide outcomes; households and one small business.
- startup-shares (CTE 6-8, concept): spreading money across risky companies. Here no investing in shares; Priya's choice is whether borrowing pays.
- snow-season-prices, e-bike-buyer, career tools (CTE 6-8): prices, purchases and careers; no rate lever.

## Who and how
- Grades 6-8, career and technical education (personal finance), module "Interest Rate Dial" (cte-6-8-interest-rate-dial).
- Standards: D2.Eco.10.6-8 (influence of interest rate changes on borrowing and investing), NSPFE.Saving, NSPFE.Managing Credit.
- Driver: students on laptops, solo by default; a teacher can project Street and turn the dial as the class calls out who is happy. 20 to 35 minutes (Street 10 to 15, Predict 10 to 15, talk 5).
- tool.json: driver "students or teacher", minutes "20-35", modes ["Street", "Predict"], grades_label "Grades 6-8".
- No personal prompts. The street, people and loans are made up; a footer line says "Made-up neighbors and numbers for learning. Not financial advice." Nothing is saved except the kit's Motion setting.

## Standards map
| Code | Student action | What they see | Done when check |
|---|---|---|---|
| D2.Eco.10.6-8 | Turn the dial past Priya's line in Street; in Predict, multiply each round's loan by its new rate and call Yes or No | Priya's card works the math ($50,000 x 10% = $5,000; $7,200 - $5,000 = $2,200 left) and her sign flips from "Opening soon" to "Not at this rate" between 7.0 and 7.5; Keisha's payment rises with the dial | Street: 7.0 shows Yes with $2,200 left, 7.5 shows No with $1,950 left. Predict round 5 (rate up to 10, yet Yes) and round 2 (rate down to 5, yet No) both reveal the worked math |
| NSPFE.Saving | Pin a rate, turn the dial, compare Abe's balance | Abe's $2,000 after 5 years at the new rate, with the pinned value under it | Pin at 3.0 (Abe $2,000.00, "no interest at 0 percent"), turn to 8.0: Abe $2,566.72, interest $566.72, pinned line $2,000.00 |
| NSPFE.Managing Credit | Tap Sign on Keisha's card, turn the dial; switch Luis's plan between Minimum and $100 a month | Keisha's payment frozen under a "Signed: 7% fixed" stamp while Luis's rate, interest and payoff time keep moving; the minimum plan's months and interest beside the $100 plan's | Sign at 6.0 ($356.42), turn to 9.0: Keisha still $356.42, Luis 23%, 113 months, $1,784.53. At 6.0, Minimum 107 months (8 years 11 months), $1,483.44; $100 a month 18 months, $240.64 |

## Screens and modes
Header: title, topic line "How one interest rate changes saving, borrowing and a business choice", modes (`.seg`) `Street` (default) and `Predict`, then `Read`, `Motion`, `Sound`.

On load: Street at base rate 6.0 percent, pinned at 6.0, Keisha unsigned, Luis on Minimum. Nothing plays until the first tap (kit rule). First hint: "Drag the dial on the bank door, or tap + and -. Watch all four neighbors." The first tap on the dial, + or - changes the rate at once and every card updates; it may cut the welcome (BASELINE 16). First tap on Sign signs at once; on Pin pins; on Predict enters round 1.

**Street.** Focus: the dial and the four cards around it. Stage (painted street backdrop, Art) takes the left of the window; the bank's door is in the middle with the dial (220 px across at 1366x768) on it, a `-` and `+` button (56 px) either side, and the big readout "Base rate 6.0%" under it. Four neighbor cells, two left of the bank and two right: each has the neighbor's painted cutout (about 150 px tall, whole body showing, feet on the street line) and a card under it (about 300 x 170 px).
- Abe (saver, top left, green): "Saves $2,000 for 5 years at 3.0%" / big number "$2,323.23 after 5 years" / "Interest earned $323.23" / a thin bar from $2,000 to $2,835.25 (the 7 percent top). Pinned line under it.
- Keisha (car buyer, bottom left, blue): "Borrows $18,000 for a car, 5 years, 7.0% fixed" / big "$356.42 a month" / "Interest in all $3,385.20" / button `Sign at 7.0%`. Signed: a stamp "Signed: 7.0% fixed", the button becomes `Shop again`, numbers freeze, and a muted line "Today's car rate: 8.5% (her loan won't change)". Her car cutout appears in the driveway when signed (a dashed outline before).
- Luis (card holder, top right, red): "Owes $1,500 on a card at 20.0% (variable)" / big "107 months to pay off (8 years 11 months)" / "Interest in all $1,483.44" / "This month: $25.00 interest, pays $40.00" / plan toggle `Minimum` `$100 a month`.
- Priya (cafe owner, bottom right, plum): her shop next door (open or closed art, Art) / "Second shop loan: $50,000 at 9.0%" / worked lines "Interest a year: $50,000 x 9.0% = $4,500" / "Shop earns $7,200 a year before interest" / "Left for Priya: $2,700 (she needs $2,000)" / verdict sign over the blank painted sign: "Opening soon" or "Not at this rate".
- Poses: each cutout shows pleased, neutral or worried (Interactions). The pose also has a word under the card ("Happier than at 6.0%", "Same", "Worse off than at 6.0%"), so the pose is never the only signal.
- Panel (right, about 400 px): hint, the rate ladder (four rows: Savings = base - 3, Car loan = base + 1, Card = base + 14, Cafe loan = base + 3, each with its current value; caption "Made-up add-ons for this street; real banks set each rate their own way"), `Pin this rate` (pins current numbers), `Who turns the dial?` (opens an info card, Content), `Start over`.
- 1366x768: everything above is above the fold; the stage is about 940 x 700. 680x425: panel stays at the side, compact (hint, Pin, Start over); the ladder and `Who turns the dial?` fold into a `More` button; the dial shrinks to 130 px, cutouts to 70 px, and each card shows only its line 1 and big number (Keisha's Sign and Luis's toggle stay). At 375 wide the four cells stack two by two under the dial.

**Predict.** Focus: the four covered cards and the dial with its ghost needle. Six rounds (Content). Same street layout. The dial sits at the round's start rate with a dashed ghost needle at the end rate and a label "Moving to 8.0%". Cards show the start numbers, poses neutral; each card has its pick buttons along the bottom (56 px tall, icon plus word): Abe, Keisha, Luis get `Better` (up arrow), `Worse` (down arrow), `Same` (equals bar), in that fixed order; Priya's card shows the round's loan, profit and "New loan rate: 11.0%" with `Yes` and `No`, her interest and left lines blank. Keisha's card shows "Signed: 5.0% fixed" in signed rounds, "Not signed yet" otherwise. The ladder shows "now" and "after" for each rate.
- Panel: "Round 1 of 6", the hint, `Turn the dial` (disabled until all four picks are made; a pick can be changed before it), then `Next round` after the reveal. Six small marks show rounds done.
- Reveal: the needle sweeps to the end rate (1.2 s; instant with Motion off), numbers move to their new values, poses update, Priya's lines fill in, and each card shows "Right" (check icon) or "Not quite" (cross icon) with a one-line reason (Content). Panel: "You called 3 of 4." `Next round` is live during the sweep: tapping it finishes the reveal at once and moves on.
- After round 6: an end card over the stage: "You called 19 of 24." and the talk prompt "Who on Maple Street hopes rates go up? Who hopes they go down? Does Keisha care now that she signed?" with `Back to Street` and `Play again` (rounds shuffled).
- 1366x768: all above the fold. 680x425: the ghost label and the ladder fold under `More`; pick buttons shrink to 44 px; cards show line 1 and the big number.

## Content
- Dial: base rate 3.0 to 10.0 percent in 0.5 steps (15 detents), default 6.0. Add-ons: savings base - 3, car base + 1, card base + 14, cafe base + 3.
- Abe Nakamura: $2,000 in savings, interest added monthly, 5 years (60 months), no new deposits.
- Keisha Brooks: $18,000 car loan, 60 monthly payments, fixed rate. Interest in all = payment x 60 - $18,000.
- Luis Ortega: $1,500 on a card (from a car repair, said on his card's line 1 hover and in Read), variable rate. Minimum plan: each month interest = balance x rate / 12, rounded to the cent; payment = the larger of $25 or (1% of the balance + that month's interest), never more than what is owed. Card note: "A common minimum rule. Cards differ: the dollar floor is often $25 to $40." $100 plan: $100 a month until paid.
- Priya Shah, Sunrise Cafe: borrows $50,000 for a second shop; pays interest each year ($50,000 x rate) and repays the loan from the shop later; the shop earns $7,200 a year before interest; she opens only if $2,000 or more a year is left for her extra work and risk.
- Table (base: savings % and Abe after 5 yrs | car % and payment, interest | card %, minimum months, interest | $100 months, interest | cafe %, interest, left, verdict):
  - 3.0: 0.0% $2,000.00 | 4.0% $331.50, $1,890.00 | 17.0% 100, $1,193.25 | 17, $198.21 | 6.0% $3,000 $4,200 Yes
  - 4.0: 1.0% $2,102.50 | 5.0% $339.68, $2,380.80 | 18.0% 102, $1,288.51 | 18, $212.09 | 7.0% $3,500 $3,700 Yes
  - 5.0: 2.0% $2,210.16 | 6.0% $347.99, $2,879.40 | 19.0% 105, $1,385.39 | 18, $226.21 | 8.0% $4,000 $3,200 Yes
  - 6.0: 3.0% $2,323.23 | 7.0% $356.42, $3,385.20 | 20.0% 107, $1,483.44 | 18, $240.64 | 9.0% $4,500 $2,700 Yes
  - 7.0: 4.0% $2,441.99 | 8.0% $364.98, $3,898.80 | 21.0% 109, $1,582.66 | 18, $255.35 | 10.0% $5,000 $2,200 Yes
  - 7.5: 4.5% $2,503.59 | 8.5% $369.30, $4,158.00 | 21.5% 110, $1,632.79 | 18, $262.80 | 10.5% $5,250 $1,950 No
  - 8.0: 5.0% $2,566.72 | 9.0% $373.65, $4,419.00 | 22.0% 111, $1,683.14 | 18, $270.33 | 11.0% $5,500 $1,700 No
  - 9.0: 6.0% $2,697.70 | 10.0% $382.45, $4,947.00 | 23.0% 113, $1,784.53 | 18, $285.54 | 12.0% $6,000 $1,200 No
  - 10.0: 7.0% $2,835.25 | 11.0% $391.36, $5,481.60 | 24.0% 114, $1,886.92 | 19, $301.14 | 13.0% $6,500 $700 No
  (Half steps not listed are computed the same way; the builder computes, never hard-codes.)
- Predict rounds (start -> end, Keisha, Priya's profit and loan; answers Abe / Keisha / Luis / Priya):
  1. 4.0 -> 8.0, not signed, $7,200 and $50,000: Better / Worse / Worse / No (11%: $5,500, $1,700 left)
  2. 8.0 -> 5.0, signed at 9.0%, $5,500 and $50,000: Worse / Same / Better / No (8%: $4,000, $1,500 left)
  3. 6.0 -> 6.5, not signed, $9,000 and $50,000: Better / Worse / Worse / Yes (9.5%: $4,750, $4,250 left)
  4. 9.0 -> 4.0, signed at 10.0%, $4,000 and $40,000: Worse / Same / Better / No (7%: $2,800, $1,200 left)
  5. 3.0 -> 10.0, signed at 4.0%, $10,000 and $30,000: Better / Same / Worse / Yes (13%: $3,900, $6,100 left)
  6. 10.0 -> 7.0, not signed, $6,500 and $40,000: Worse / Better / Better / Yes (10%: $4,000, $2,500 left)
- Reveal reasons (filled with the round's numbers): Abe up "Higher rate, more interest on his savings: $2,566.72." / down "Lower rate, less interest for Abe." Keisha signed "Signed at 9.0% fixed: the dial can't change her $373.65." / up "She hasn't signed, so she pays the new rate: $373.65 a month." / down "Not signed yet: the lower rate cuts her payment." Luis up "His card is variable: more interest, $1,683.14 in all." / down "Variable rate: it fell with the dial." Priya: "$50,000 x 11% = $5,500. $7,200 - $5,500 = $1,700 left. Under $2,000, so she waits." (or "...$2,000 or more, so she opens.").
- `Who turns the dial?` card: "On a real street there is no single dial. Each bank sets a base rate called the prime rate, and most set it about 3 points above the Federal Reserve's target rate. When the Fed raises or lowers its rate, prime usually follows, and so do rates tied to it, like most credit card rates (prime plus an add-on). A fixed-rate loan keeps the rate it was signed at."

## Interactions in detail
- Dial: drag around a 270 degree sweep; it snaps to the nearest detent and updates every card on each detent (no wait for release). Keyboard: role slider, arrows +/- 0.5, Home 3.0, End 10.0. `-` and `+` step 0.5 and disable at the ends.
- Numbers tween over 0.4 s to new values (instant with Motion off); a new change mid-tween jumps to the new target at once. All money to the cent, computed in full precision; Luis's interest is rounded per month as banks do.
- Sign: locks Keisha's rate and payment at the current values. Later dial moves change only her "Today's car rate" line. `Shop again` unsigns and re-reads the current rate.
- Pin: stores all four cards' main numbers and the rate; each card shows "Pinned at 6.0%: ...". On load the pin is 6.0. Poses: Abe pleased when his balance is above the pinned one, worried below, neutral equal; Luis by total interest on his current plan (lower is pleased); Keisha unsigned by payment vs pinned, signed by today's car rate vs her signed rate (today higher: pleased, lower: worried); Priya pleased on Yes, worried on No, whatever the pin.
- Luis's plan toggle recomputes at once; the pin stores both plans so a plan switch compares fairly.
- Extremes: 3.0 makes Abe's rate 0.0% (line "No interest at 0 percent: just the $2,000 he saved."); 10.0 is the top and every number fits its card at every size (largest: $2,835.25, 114 months, $1,886.92, $6,500).
- Predict: picks are toggles within a card (one per card); `Turn the dial` enables when all four have a pick. Taps on picks after the reveal do nothing. Mode switch mid-round keeps the round's picks; Street is left at whatever the student set. `Play again` shuffles the six rounds.
- `Start over`: rate 6.0, pin 6.0, unsigned, Minimum, Predict back to round 1, voice hushed.
- Tab order: modes, dial, -, +, card controls (Sign, plan toggle or picks) left to right, panel.

## Look
Own light `:root` (6-8 has no band theme): paper `#f6f3ec`, panel `#ffffff`, ink `#1f2328`, muted `#5b616b`, button line `#7b8088`, focus `#1f5fd1`. Accent `--brand #8a5300` (bank brass: mode buttons, Pin, Turn the dial), white text on it. Dial face is the door's dark wood `#2e2a24` with a gold ring and ticks `#d99a1e` and numerals `#f6f3ec`. Neighbor colors (card edge, name, bar): Abe `#1d6b3a`, Keisha `#1f5fa8`, Luis `#a3261b`, Priya `#74388a`. Predict covers `#e4ddcf`.
Contrast (computed, on paper / on panel): ink 14.26 / 15.80; muted 5.63 / 6.24; brand 5.71 / 6.33, white on brand 6.33; Abe 5.89 / 6.53; Keisha 5.81 / 6.44; Luis 6.65 / 7.37; Priya 7.08 / 7.85; focus 5.24 / 5.81; button line 3.59 / 3.97 (non-text); gold ring on door 5.83, numerals on door 12.87; ink on cover 11.69. Right and wrong use icon and word, never color alone. Neighbors' accents: career-cluster-explorer teal `#2dd4bf`, workplace-scenarios blue `#1e6fd9`, compound-interest-head-start spring green, the-credit-card-diaries raspberry, savings-plan ledger green; brass differs from each.

## Art
Shared style line: "warm painted storybook illustration, soft morning light, gentle textures". Signs, windows and papers are blank; words go in code. Webp.
- street-bg: "a sunny small-town main street in morning light, a brick bank with columns and a tall wooden door in the center, a small house with a garden at left, a house with a driveway and garage at lower left, apartment steps at right, a corner cafe with an empty storefront beside it at lower right, all signs blank"; 16:9; cutout no; people no; the Street and Predict backdrop, local FLUX. The dial is drawn in code over the door.
- abe-neutral, abe-pleased, abe-worried: "an older Japanese American man in a brown cardigan holding a small savings passbook, full body standing" with pose "calm face" / "warm smile, small thumbs up" / "slight frown, hand on chin"; 3:4; cutout yes; people true (Gemini, Cory review); above his card.
- keisha-neutral, keisha-pleased, keisha-worried: "a young Black woman in teal nurse scrubs holding car keys, full body standing" with the same three poses; 3:4; cutout yes; people true.
- luis-neutral, luis-pleased, luis-worried: "a young Latino man in a delivery jacket holding a phone, full body standing" with the same poses; 3:4; cutout yes; people true.
- priya-neutral, priya-pleased, priya-worried: "a South Asian woman in her forties in a cafe apron holding a coffee cup, full body standing" with the same poses; 3:4; cutout yes; people true.
- shop-open: "a cozy small cafe storefront with warm lights on, chairs and potted plants outside, a blank awning and a blank sign board"; 4:3; cutout yes; people no; Priya's Yes state.
- shop-closed: "the same small storefront dark and empty, brown paper over the windows, a blank sign board"; 4:3; cutout yes; people no; Priya's No state. The two states must differ at a glance (light vs dark).
- car: "a small blue hatchback car, side view, shiny, plain white background"; 16:9; cutout yes; people no; in Keisha's driveway once she signs.
- 17 images, 12 with people (Gemini only, contact sheet for Cory and a fresh stereotype check: no group shown as careless with money; Luis's balance comes from a car repair). Cutouts sit fully inside their cells at every size, feet on the street line, never behind a card.

## Voice
Bank voice `wise-mentor`, "Say thoughtfully and warmly, like a wise high school mentor": a neighbor who explains the street. Not used by any tool `neighbors.py` lists (upbeat-guide, casual-peer, smooth-narrator, big-sister, hs-narrator). `Curio.voice`, `scope: () => state.mode`. Lines read numbers only where named.
- welcomeStreet (how; on entering Street; stale after the dial moves): "One dial sets the rates on Maple Street. Drag the dial on the bank door, or tap plus and minus, and watch all four neighbors."
- signHow (how; after the second dial move while Keisha is unsigned; stale once she signs): "Keisha is buying a car. Tap Sign on her card to lock today's rate, then turn the dial again."
- signed (event; on Sign; stale on Shop again): "Keisha signed at (rate) percent fixed. Her payment is set now, but Luis's card rate still moves with the dial."
- pinHow (how; after four dial moves with no Pin tap; stale on Pin): "Tap Pin this rate to keep these numbers, then turn the dial and compare."
- cafeNo (event; when Priya's verdict turns to No; stale if it turns back first; spoken at most twice per load, then hint only): "At this rate the loan costs Priya too much. She says no to the second shop."
- cafeYes (event; when it turns back to Yes; same limits): "Borrowing got cheaper. Priya says yes again."
- welcomePredict (how; on entering Predict; stale after the first pick): "The dial is about to move. For each neighbor, tap Better, Worse or Same. For Priya, tap Yes or No."
- cafeHow (how; first round, once three picks are made and Priya's is not; stale on her pick): "For Priya, multiply the loan by the new rate. If two thousand dollars or more is left, tap Yes."
- turnHow (how; when the fourth pick enables Turn the dial; stale on Turn the dial): "Now tap Turn the dial."
- result (event; whole; after the sweep): "You called (n) of four." 
- nextHow (how; after result; stale on Next round): "Read each card's reason, then tap Next round."
- endLine (event; whole; after round 6's result): "That's all six rounds. Who on the street hopes rates go up, and who hopes they go down? Tap Back to Street to test it."

## Family engine
none (no money engine is built yet; this tool computes its own four formulas as given in Content).

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails (or the design change made here) |
|---|---|---|
| Predict picks for Abe, Keisha, Luis | guessing; position (Better is always first); mashing; doing nothing; the common wrong answer "rates up is bad for everyone"; "the car is always Same"; the answer on screen (poses, numbers, ladder) | Guessing all three right is 1 in 27 per round. Button order is fixed and unrelated to answers, which vary (Abe Better 3 times, Worse 3). Mashing: only the last pick counts, scored once at the reveal. Doing nothing: Turn the dial stays disabled, nothing advances. "Bad for everyone" gets Abe wrong in all 6 rounds (computed). "Car always Same" is wrong in the 3 unsigned rounds. Poses stay neutral and numbers show the start values until the reveal; the ladder shows the after rates, which only restates the dial's direction; turning a rate into better or worse for each role is the skill checked. |
| Predict pick for Priya | always Yes or always No; Yes when the rate falls; memorized Street line (Yes at 7.0 or below); profit bigger than interest (forgetting her $2,000); "big profit means Yes"; answer on screen | Each heuristic was run over the 6 rounds: always Yes 3/6, always No 3/6, Yes when falling 2/6, Street line 3/6, no cushion 3/6, rate under 10% 2/6, profit at least $7,200 4/6, $1,000 cushion 3/6. Profit and loan change each round so the line moves (round 5 Yes at 13%, round 4 No at 7%). Her interest, left and sign stay blank until the reveal. |
| Round tally and end total | replaying the same rounds from memory | `Play again` shuffles round order; the start and end rates are on screen, so memory of a round equals knowing it, and the tally is not a grade (no stars, no unlocks). |
| Street: Priya's verdict and poses | not a check (computed from the dial); sweeping finds the line | Sweeping is the exploring the mode asks for; the worked math stays on her card so the line is explained, not just found. |
| Street: cafeNo and cafeYes lines | sweeping the dial back and forth to hear them | Event lines, spoken at most twice each per load, then hint only; dropped when the verdict changed again before they play. |

## Heard in order
Grades 6-8: none required by grade. Rules that must hold: in Predict, result plays after the sweep ends and before nextHow, and the end card's endLine waits for round 6's result; tapping Next round drops result and nextHow if not yet started (the student chose to move on), never mid-word of a line already playing. signed plays before signHow could ever replay (signHow is stale once signed). A Read during a sweep waits for nothing and stops queued lines.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Higher rates make borrowing cost more and hold businesses back from expanding; lower rates encourage loans for cars and homes | Federal Reserve Board, "Fed FAQ: Why Do Interest Rates Matter?" transcript, 2016 (federalreserve.gov/mediacenter/files/why-do-interest-rates-matter-transcript-092016.pdf) | BizMonthly, "As interest rates rise, soft landing is goal" (2023), businesses put off equipment purchases as rates rise | yes |
| Savings earn more interest at a higher rate; interest is added on interest (compounding) | Investor.gov (SEC), Compound Interest Calculator and glossary | FDIC Money Smart for Young Adults, saving module | yes |
| Most credit cards have a variable rate: the prime rate plus a margin, moving when prime moves | Capital One, "Fixed vs. variable interest rates" (capitalone.com/learn-grow) | Chase, "Difference between fixed and variable APR credit cards" (chase.com) | yes |
| A fixed-rate loan keeps its signed rate for the life of the loan | Capital One (above) | OneUnited Bank, "Fixed vs. Variable Rates" | yes |
| The prime rate is usually about 3 points above the Fed's target rate; banks set their own | Citi, "What is the prime rate?" | Wikipedia, "U.S. prime rate" (2020: federal funds 0.25%, prime 3.25%) | yes |
| Card rates run about 14 points over prime (the +14 add-on) | CFPB analysis of 2023 card data as reported by PaymentsJournal: average APR margin 14.3 points | ABA Banking Journal, "Missing the point on credit card APR margins" (2024): disputes the cause, not the size | yes on size |
| A common minimum payment: the larger of a dollar floor or 1% of the balance plus interest; floors differ | CBS News MoneyWatch, "How are credit card minimum payments calculated?" (floor $25 to $35; 1% to 3% plus interest) | Chase cardmember agreement and education page (larger of $40 or 1% plus interest) | yes; the tool uses $25 and says floors differ |
| Paying only the minimum takes years and costs much more interest | computed here (107 months, $1,483.44 vs 18 months, $240.64) | CBS News (above), same point | yes |
Backed twice: 8. Cut: a "typical card rate today" figure and current savings averages (would date; not needed). Made up and labeled: the street, people, add-ons (-3, +1, +3), Priya's profit and $2,000 rule.
Checks run (Python, 2026-11-06): every Content table row from the formulas above (amortized car payment rounded to the cent, monthly-rounded card simulation, monthly compounding); every Standards map and Done when number; Predict answers for all 6 rounds and eight wrong heuristics for Priya (scores above), "bad for everyone" (Abe 0/6), "car always Same" (3/6); no Priya tie at $2,000 in any round or detent (7.0 leaves $2,200, 7.5 leaves $1,950); 3.0 gives Abe 0% and $2,000.00 with no divide by zero; largest values fit (Interactions).

## Done when
1. Defaults at 6.0: Abe $2,323.23, Keisha $356.42 and $3,385.20, Luis 107 months and $1,483.44 ($25.00 interest, $40.00 payment this month), Priya Yes with $2,700 left.
2. Priya shows Yes with $2,200 left at 7.0 and No with $1,950 left at 7.5, with the worked lines and open or closed shop art; cafeNo plays at most twice per load.
3. Pin at 3.0, turn to 8.0: Abe $2,566.72 with "Pinned at 3.0%: $2,000.00", pleased pose and its word.
4. Sign at 6.0, turn to 9.0: Keisha stays $356.42 under "Signed: 7.0% fixed" with "Today's car rate: 10.0%" and a pleased pose; Luis shows 23.0%, 113 months, $1,784.53.
5. Luis at 6.0, $100 a month: 18 months, $240.64.
6. Predict: Turn the dial stays disabled until four picks; each round's reveal matches the Content answers and reasons; the end card totals the right calls out of 24.
7. Predict before the reveal shows no new numbers, neutral poses and a blank Priya interest, left and sign.
8. Focus: at 1366x768 and 680x425 the dial and the four cards are the largest things in both modes.
9. Tap while it plays: turning the dial mid-tween jumps every card to the new values at once; Next round during a sweep finishes the reveal and moves on.
10. 1366x768 fold: dial, + and -, all four cards with Sign, plan toggle and picks, and the panel's Pin or Turn the dial are visible without scrolling; at 680x425 the ladder folds under More.
11. Keyboard: the dial moves by arrows, Home and End; every pick and button is reachable with visible focus; right and wrong show icon and word.
12. How lines spoken once each in five actions in a row; result plays after every sweep and before nextHow.

## Open questions
- Twelve people images (four neighbors in three poses) go to Gemini and Cory's contact sheet; the fresh agent should check the four together for stereotypes about who saves and who owes.
