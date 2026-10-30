# Paycheck Decoder

## One idea
Every line on a real-looking pay stub opens up to show the exact math behind it, so you can tap "Federal income tax $104.71" and watch it built from the 2026 brackets step by step, then change one thing on the timecard and see which lines move, which stay put, and why your first check is smaller than your pay rate promised.

## Not like
- first-apartment-budget (9-12, money, built): shows one monthly take-home number and spends it. Here there is no budget; the stub itself is the thing you explore, line by line, down to the cent.
- compound-interest-head-start (9-12, money, this group): grows savings over decades. Here one pay period, no interest.
- the-credit-card-diaries (9-12, money, this group): a four-year story of choices. Here no story and no choices with consequences, only cause and effect on one stub.
- covered-insurance-claims (9-12, money, this group): insurance and fake messages. Here the only document is your own pay stub.
- interview-simulator (9-12, this group): getting the job. Here the job already pays you.
- corner-store (2, money, built): coins and change. Here payroll taxes and benefits.

## Who and how
- Grade 9-12, career and technical education (personal finance), module "Earning Income and Paychecks".
- Topic line: gross pay, net pay, taxes and benefits on a real pay stub
- Driver: students on laptops (alone or in pairs); the teacher can project one stub for a "where did my money go?" opener. 15 to 35 minutes.
- Standards: NSPFE.Earning Income (National Standards for Personal Financial Education 2021: gross and net pay, payroll taxes, benefits).
- Data as of line on screen: "2026 federal tax rules (IRS), Social Security and Medicare (SSA). State and city taxes simplified."

## Screens and modes
Header: title, topic line, mode buttons (`.seg`): `Stub` (default), `Change it`, `Guess first`; then `Read`, `Motion`, `Sound`.

Above the stage in every mode, a row of three stub tabs, each with a small painted picture of the workplace (Art): `Jordan, cashier`, `Sam, warehouse`, `Avery, web developer` (Content). The chosen stub stays chosen across modes.

**Stub.** Focus: the pay stub, centered on the painted desk and the largest thing on the stage (at least 60% of the stage width at 1366x768); the line card opens in the panel beside it. Stage: a pay stub drawn in code at real pixel size on a painted walnut desk (Art), laid out like the real thing: employer block (made-up name and address), employee block (first name, pay period, pay date, check number), then four boxes: Earnings (rate, hours, this period, year to date), Pre-tax deductions, Taxes, After-tax and net pay; a strip at the bottom "Paid by your employer, not taken from you" (employer Social Security and Medicare match, employer 401(k) match, employer share of the health plan). Every line is a button (44 px tall). Tap a line:
- The painted highlighter (Art) slides to it and leaves an apricot band, and the panel opens its card: the line's plain name ("FICA SS" = "Social Security tax"), one sentence on what it is, where the money goes, and the math as numbered steps with the real numbers ("1. Pay this period $1,677.00. 2. Minus health premium $55.38 (health premiums are taken out before this tax) = $1,621.62. 3. Times 6.2% = $100.54.").
- `Show me on the stub` lights every number the steps used (the health line and the gross line glow too).
- Year to date: tapping a YTD number explains it as this check times the check number (pay date is the 6th check of the year for the biweekly stub, and so on), and says Social Security stops when year-to-date pay passes $184,500 (it never does here).
Panel also holds: `Plain words` toggle (relabels every stub line from payroll shorthand to plain words, so students can flip between what a real stub says and what it means) and a short list "Lines not opened yet" with buttons to each.

**Change it.** Focus: the stub, still the largest thing, on the left; the panel becomes the timecard and benefits form:
- `Hours` slider per week (0 to 60; biweekly stubs show Week 1 and Week 2), `Pay rate` number box ($7.25 to $60.00 an hour, or salary $20,000 to $200,000 for Avery), `Pay schedule` select (weekly, every two weeks, twice a month, monthly), `401(k)` slider (0 to 15 percent, step 1), `Health plan` select (none, employer plan, plus the stub's own premium), `Where you work` select (the seven places in Content), `Check number` stepper (1 to the schedule's checks per year; sets the year to date, so the Social Security cap can be reached).
- Every change recomputes the stub instantly. Lines that changed flash and show a small delta tag ("+$12.40", "-$3.10") for 3 seconds; lines that did not change stay still. A one-line "What moved" note under the stub names the biggest mover ("Overtime raised gross pay by $117.00; federal tax rose $13.62 and take-home rose $84.89"). A new change during the 3 seconds replaces the tags at once with the new deltas.
- `Back to the real stub` resets the chosen stub to its Content values.

**Guess first.** Focus: the stub with its gray bars and the guess slider right under it. An optional challenge, one stub at a time. The stub shows only gross pay; every other line is a gray bar. Prompt: "Drag the slider to guess the take-home pay, then tap Check." A `Take-home guess` slider (0 to gross, step $1) with a live percent of gross. `Check` reveals the lines one by one (each slides in with its amount over about 2 seconds in all; instant with Motion off), then shows the guess against the real net in dollars and percent of gross. A tap on `Next stub` or `Try again` during the reveal finishes it at once and acts. No score; a tally "Closest guess this visit: within $x" per stub. `Next stub` moves on; `Try again` hides the lines.

## Content
**The three stubs** (all names, employers and addresses made up):
1. Jordan, 16, cashier at Riverbend Grocery, Houston, Texas (no state income tax). $14.00 an hour, 18 hours, paid weekly, check 12 of the year. No 401(k), no health plan.
   Gross $252.00; federal income tax $0.00; Social Security $15.62; Medicare $3.65; net $232.73.
2. Sam, 19, warehouse associate at Northgate Supply, Columbus, Ohio. $19.50 an hour, Week 1 44 hours and Week 2 40 hours (4 overtime hours at 1.5 times, $29.25), paid every two weeks, check 6. 401(k) 3 percent with a 3 percent employer match; employer health plan $55.38 a check ($1,440 a year over 26 checks).
   Regular $1,560.00 + overtime $117.00 = gross $1,677.00; 401(k) $50.31; health $55.38; federal $104.71; Social Security $100.54; Medicare $23.51; Ohio $15.66; Columbus city tax $40.54; net $1,286.35.
3. Avery, 22, junior web developer at Bluepeak Studio, Denver, Colorado. Salary $58,000, paid twice a month (24 checks), check 1 (first check of the month). 401(k) 5 percent with a 4 percent match; health $60.00 a check ($1,440 a year over 24).
   Gross $2,416.67; 401(k) $120.83; health $60.00; federal $177.47; Social Security $146.11; Medicare $34.17; Colorado $68.86; Denver occupational privilege tax $5.75; net $1,803.48.

**Line cards** (plain name, what it is, where it goes):
- Gross pay: everything you earned this period before anything comes out.
- Regular and overtime: overtime is 1.5 times your rate for hours over 40 in a workweek, for most hourly jobs (federal Fair Labor Standards Act). Salaried Avery has no overtime line.
- 401(k): money you save for retirement from your own pay, taken out before federal income tax (but not before Social Security and Medicare). Goes to your own retirement account. The employer match is extra money from the employer into the same account.
- Health premium: your share of the employer's health plan, taken out before all these taxes. The employer pays the rest: on average about $9,325 a year for single coverage in 2025, and workers paid about 16 percent of it (KFF). This stub uses $1,440 a year, the figure first-apartment-budget uses.
- Federal income tax: paid to the U.S. Treasury. The stub estimates the year: this check's taxable pay times checks per year, minus the $16,100 standard deduction, through the 2026 brackets (10 percent on the first $12,400, 12 percent up to $50,400, 22 percent up to $105,700, and higher above), then divides by checks per year. Card note: "Real payroll uses the IRS withholding tables, which land close to this. Withholding is an estimate; the tax return in spring settles it."
- Social Security: 6.2 percent of pay after the health premium, on pay up to $184,500 a year (2026). Pays benefits to retired workers, people with disabilities and survivors today; your work earns you credits toward your own.
- Medicare: 1.45 percent with no cap (plus 0.9 percent more on wages over $200,000). Pays for hospital insurance for people 65 and older.
- State and city taxes (simplified, the same table first-apartment-budget uses): Texas and Washington none; Ohio 2.75 percent of yearly pay above $26,050 (after 401(k) and health) plus Columbus city tax 2.5 percent of pay after health; Colorado 4.4 percent of federal taxable income plus Denver's $5.75 a month occupational privilege tax (on the first check of the month); Arizona 2.5 percent above $16,100; Massachusetts 5 percent above $4,400 (after health only); Indiana with Allen County 4.54 percent above $1,000. Card note: "Simplified for learning; real state forms have more steps."
- Net pay: what lands in your account.
- Employer strip: employer Social Security and Medicare match (the same 7.65 percent again, paid by the employer), employer 401(k) match, employer health share. Line: "Your job costs your employer more than your gross pay."

**Places** (`Where you work`): Houston TX, Seattle WA, Columbus OH, Denver CO, Phoenix AZ, Boston MA, Fort Wayne IN.

## Interactions in detail
- All money in cents, rounded half up per line (the engine's `r2`); net is gross minus the rounded lines, so the stub always adds up to the cent. A footer check line "Gross minus every line = net" shows the sum.
- Federal tax per check = r2(fedTax(max(0, (gross - 401(k) - health) x checks - 16,100)) / checks). Social Security = r2(0.062 x (gross - health)), stopping when year-to-date pay after health reaches $184,500 (reachable in Change it with a high salary: the check that crosses it taxes only the part under the cap, and later checks show $0.00 with a card note). Medicare = r2(0.0145 x (gross - health)), plus 0.9 percent on year-to-date wages above $200,000.
- Overtime: hours over 40 in each week separately (biweekly: Week 1 and Week 2 sliders), never averaged across weeks; the card says so. Salaried pay has no hours slider.
- Pay rate below $7.25 is blocked with a note (federal minimum wage); hours 0 gives a stub of all $0.00 lines and the note "No hours, no pay, no taxes."
- Federal tax $0.00 is explained, not hidden: Jordan's card shows the yearly estimate ($252 x 52 = $13,104) under the $16,100 standard deduction.
- Changing the schedule keeps the yearly pay and hours per week the same and redraws the check (weekly 52, biweekly 26, twice a month 24, monthly 12; hourly pay for twice a month and monthly uses hours x rate x 52 / checks).
- Year-to-date = this check's amounts x the check number (no mid-year raises).
- The highlighter slides to a tapped line in 0.25 s (instant with Motion off); tapping another line mid-slide sends it straight to the new line and opens that card.
- Esc closes a line card; focus returns to the line. Tab order: stub tabs, panel controls, then stub lines top to bottom.
- Sizes: the stub is laid out at real pixels per size over the desk texture; at 680x425 the boxes stack in two columns and the employer strip collapses to one line; at 375 wide the stub scrolls inside its own frame and line cards open as a bottom sheet.

## Look
- Accent `--brand #ffb48c` (apricot highlighter: the band on a tapped line, the active mode, the Check button), `--brand-ink #2a1404`. Moved off #ffe14d in the joint review of waves 2 and 3 (intersection-quest has the same yellow). Base `kit/theme-912.css`.
- Scene: the painted dark walnut desk, about `#1a1410`, under the stub; the stub paper `#fbfaf6` with ink `#1d2128`, muted `#5a6170`, box rules `#c9ccd3`, header band `#e8ebf0`. Delta tags: up `#0f6b3d` with "+", down `#a32020` with "-" (on the paper; sign always shown, never color alone).
- Contrast: accent on panel `#141b25` 10.02:1, on `--sec-bg` 9.5:1; brand-ink on accent 10.13:1; stub ink on paper 15.6:1; muted on paper 6.1:1; up tag 6.9:1 and down tag 7.2:1 on paper. No text sits on the desk texture itself.
- Differs from first-apartment-budget (cream, navy, terra), market-time-machine (paper, brass, deep navy) and the rest of this batch (lake blue, spring green, jade, periwinkle, brick coral, trail green, safety orange, violet, raspberry).

## Art
Local FLUX (`scripts/localart.py`), one session, no people. Webp.
- pd-desk: "a full-frame top-down texture of a dark walnut wooden desk with fine grain, a fountain pen and a coffee ring near one corner, warm low lamp light"; 16:10; cutout no; people no; the stage under the stub (the pen and ring stay at the edge the stub leaves free; the builder crops so they never sit under the stub).
- pd-marker: "a single chunky apricot orange highlighter pen with its cap off, lying diagonally, top-down view, plain white background, realistic"; 4:1; cutout yes; people no; slides to each tapped line (about 120 px long) and rests at the line's right end.
- Workplace thumbnails (4:3; cutout no; people no; 96 px on the stub tabs; signs blank): one shared style "small realistic painting, bright even light":
  - pd-grocery: "an empty grocery store checkout lane with a conveyor belt and a card reader, (style)".
  - pd-warehouse: "an empty warehouse aisle with tall shelves of cardboard boxes and a pallet jack, (style)".
  - pd-studio: "an empty small design studio desk with two monitors showing plain colored panels, a sketchbook and a plant, (style)".
- 5 images, none with people. Drawn in code: the stub, its lines and boxes, the highlighter band, delta tags and every number (a document that must change to the cent).

## Voice
Bank voice `calm-professor` (Schedar), "Say evenly and clearly, like a calm, friendly college professor": a patient explainer of a dry document. Not used by another tool `neighbors.py` lists or by this batch. `Curio.voice`, `scope: () => state.mode`. Line cards and math steps are on screen only (Read speaks them).
- welcomeStub (how; on entering Stub before any line is tapped; stale when a line is tapped): "This is a real kind of pay stub. Tap any line to see the math behind it."
- plainHow (how; after the first line card opens; stale when Plain words is tapped): "Tap Plain words to see what each short label means."
- welcomeChange (how; on entering Change it; stale when a control changes): "Change the hours, the pay or the benefits. Lines that move will flash."
- deltaBig (event; after a change; stale if another change comes first): "The biggest change was (line)."
- welcomeGuess (how; on entering Guess first; stale when the slider moves): "Drag the slider to guess the take-home pay. Then tap Check."
- guessResult (event; each Check; stale on Next stub or Try again): "Take-home was (net), (percent) of gross. You were off by (difference)."

## Family engine
The money family engine (described here in full; first-apartment-budget and market-time-machine are the built siblings it comes from; compound-interest-head-start, the-credit-card-diaries, covered-insurance-claims and startup-booth use it too; the integrating session decides its file, for example `kit/money.js`, and moves the live tools onto it when they are next touched):
- Formatting: `money(n, cents)` and `r2(n)` (half-up cents) from first-apartment-budget; `pct(x, d)` from market-time-machine.
- Payroll, tax year 2026: `BR` brackets and `fedTax(ti)` as in first-apartment-budget; `STD = 16100`; `fica(gross, health, ytd)` with Social Security 6.2 percent to the $184,500 wage base and Medicare 1.45 percent plus 0.9 percent over $200,000; `PLACES`, first-apartment-budget's `CITY[].tax` table moved into the engine (rates, bases, minus amounts and names unchanged), and `stateTax(place, gross, k401, health)`; `paycheck({gross, checks, k401pct, health, place, ytd})` returns every line in cents.
- Loans and cards: `loanPay(balance, rate, months)` (first-apartment-budget's formula with rate and term as inputs), `CARD_APR = .24`, `LATE_FEE = 32`, and `statement(card)`, first-apartment-budget's monthly statement step (interest on a carried balance, minimum payment max($35, 1 percent plus interest), late fee) as a pure function.
- Saving: `grow({start, deposit, months, rate, perYear})` with the effective monthly rate (1 + r/n)^(n/12) - 1 and a yearly split into deposits, simple interest and interest on interest (specified in compound-interest-head-start).
- Seeded randomness: `rng(seed)` and `newSeed()` from first-apartment-budget (startup-booth seeds its event weeks with them).
- Data line: each tool shows its "data as of" line from its own sources.
The grade 2 and grade 5 siblings (corner-store, piggy-bank-planner, grocery-run) use only the formatting and rng parts.
This tool feeds it: the three stubs above and the Change it inputs; it uses `paycheck`, `fedTax`, `fica`, `stateTax`, `money`, `r2`.

## Sources
- 2026 federal income tax brackets (single) and $16,100 standard deduction: IRS Rev. Proc. 2025-32, as in first-apartment-budget (https://www.irs.gov/pub/irs-drop/rp-25-32.pdf).
- 2026 Social Security wage base $184,500, 6.2 percent and Medicare 1.45 percent: SSA, 2026 Social Security Changes fact sheet (https://www.ssa.gov/news/en/cola/factsheets/2026.html).
- Additional Medicare Tax 0.9 percent over $200,000: IRS, Questions and Answers for the Additional Medicare Tax (https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax).
- Withholding method being simplified: IRS Publication 15-T, Federal Income Tax Withholding Methods (2026) (https://www.irs.gov/publications/p15t).
- Overtime at 1.5 times over 40 hours a workweek, $7.25 federal minimum wage: U.S. Department of Labor, Fair Labor Standards Act overview (https://www.dol.gov/agencies/whd/flsa).
- Health premiums before tax (cafeteria plans) and 401(k) before income tax but not FICA: IRS Publication 15-B and Publication 15 (2026) (https://www.irs.gov/publications/p15b, https://www.irs.gov/publications/p15).
- Employer single-coverage premium $9,325 and worker share in 2025: KFF, 2025 Employer Health Benefits Survey (https://www.kff.org/health-costs/2025-employer-health-benefits-survey/); the $1,440 worker figure as used in first-apartment-budget's notes.
- State and city tax approximations: first-apartment-budget notes ("Simplified on purpose"), tools/first-apartment-budget/notes.md; Denver occupational privilege tax $5.75 a month: City and County of Denver, Occupational Privilege Tax (https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Department-of-Finance/Our-Divisions/Treasury/Business-Tax-Information/Occupational-Privilege-Tax).
- Stubs, names, employers: made up for this tool.
- Checks run (Python, 2026-10-29, half-up cents and the formulas above): all three stubs reproduce every line and net to the cent (Jordan $232.73, Sam $1,286.35, Avery $1,803.48). Jordan at 40 hours: federal $25.28, Social Security $34.72, Medicare $8.12, net $491.88. Sam with Week 1 at 40: gross $1,560.00, federal $91.09, net $1,201.46; turning overtime back on raises federal by $13.62 and take-home by $84.89, as the What moved example says. Avery at $200,000 (gross $8,333.33, $8,273.33 after health): check 23 crosses the wage base, with $182,013.26 before it, so it taxes only $2,486.74 ($154.18 Social Security instead of $512.95) and check 24 shows $0.00. The old spec could not reach this case: its salary range stopped at $150,000 (which never crosses the cap) and the check number was fixed, so the salary range now reaches $200,000 and Change it gains a `Check number` stepper. Largest hourly stub: 60 hours a week at $60.00, weekly gross $4,200.00, fits the stub layout.

## Done when
1. The three stubs show exactly the Content amounts; each adds up to the cent (Jordan net $232.73, Sam $1,286.35, Avery $1,803.48).
2. Jordan at 40 hours a week (Change it): federal $25.28, Social Security $34.72, Medicare $8.12, net $491.88.
3. Sam with Week 1 at 40 hours: no overtime line, gross $1,560.00, federal $91.09, net $1,201.46 (the What moved note: federal tax rose $13.62 and take-home rose $84.89 with overtime back on); the overtime card says weeks are not averaged.
4. Every line opens a card whose numbered steps reproduce its amount; `Show me on the stub` lights every number the steps use.
5. Avery at a $200,000 salary, `Check number` 23: Social Security taxes $2,486.74 for Social Security ($154.18) and check 24 shows $0.00.
6. A pay rate under $7.25 is refused with the minimum wage note; 0 hours gives an all-zero stub with its note.
7. Change it flashes only the lines that changed, with signed delta tags, and `Back to the real stub` restores Content values.
8. Guess first reveals every line and reports the difference in dollars and percent; nothing is saved between visits.
9. Focus: at 1366x768 and 680x425 the stub is the largest thing on the stage in all three modes.
10. Tap while it plays: a tap on another line mid-slide moves the highlighter there at once; Next stub during the Guess first reveal finishes it and moves on with no stale line.
11. Stub lines stay 44 px and readable at every STANDARDS.md size; the 680x425 preview shows a whole stub; the 5 paintings load with no person or fake lettering.
12. How lines play once each across five actions in a row; deltaBig and guessResult play every time and drop when stale.

## Open questions
- Withholding is the annualized bracket estimate (first-apartment-budget's method), not the exact IRS Publication 15-T percentage tables, so a real 2026 stub could differ by a few dollars. The card says so. Keep it, or build the full 15-T tables into the money engine?
