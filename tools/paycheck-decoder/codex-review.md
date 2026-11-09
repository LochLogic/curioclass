# Codex review: paycheck-decoder

## Played

Played cold as a grade 10 student before reading builder notes/source, then as a projector user. The paper and overtime reveal are strong; compact forms needed scrolling care. One review/fix pass, no commits.

## Findings fixed

- Should fix, general, `src.html` Change it: hourly minimum-wage rejection stayed on Avery's salary form. Worker/mode changes now recompute the current validation note. Targeted assertion passes.
- Should fix, family:money, employer strip: changing a plan altered employer contributions without signed delta tags or flashing. All three employer lines now use the same feedback as employee lines; health removal shows -$301.27.
- Blocker, general, Motion-off Guess first: an employer card could open during the timed reveal and the result arrived over it. Reproduced on the preserved old bundle, then blocked card entry and disabled employer buttons until the reveal ends.
- Should fix, family:money, underfunded Stub: a negative take-home percentage claimed money reached the account. It now names the shortfall and says no deposit in this model; the net card explains the assumption. Guess first blocks an impossible negative-deposit prediction, records no attempt, and names Change it in the hint and a new once-per-load how-to.
- Should fix, general, compact Change it: decorative/form space pushed pay rate out of view. Removed redundant space, enlarged the phone timecard, kept hour units together, aligned week sliders and scrolled the compact paper to earnings on entry.
- Should fix, general, line cards: scrolling to Show me covered Close at 680; the phone sheet hid its hint. Hint and controls now remain visible while the keyboard-focusable explanation scrolls. Phone sheets have dialog semantics; Escape returns to a visible stub line. All eight sizes re-shot.
- Should fix, general, Show me: Plain words erased four dependency outlines while keeping its pressed state true. Confirmed on the old bundle; the new renderer restores the outlines and input highlights.
- Should fix, family:money, comparisons: zero gross showed a false 0% of zero, and biggest change excluded net. Zero now explains the undefined percentage; Sam OH-to-TX correctly names take-home +$56.20 as largest.
- Should fix, general, Guess first: Try again was active with nothing to reset. It now enables after a change/check and returns focus to the guess slider on reset.
- Polish, family:money, Ohio card: made the omitted $332 base tax explicit while preserving the spec's simplified formula and all original amounts.
- Polish, general, flattest moment: the take-home bar did not explain its gap. It now names the actual tax total and employee-benefit total, including after a guess reveal.
- Polish, general, art: replaced the green-fringed highlighter with a detailed painted chisel-tip pen; preserved the desk and all three workplaces.

## Findings left

- Should fix, spec conflict, family:money: Massachusetts model taxes retirement contributions even though eligible pre-tax 401(k) deferrals are generally excluded. The brief forbids changing a disputed spec formula. Preserved its calculation, corrected the on-screen wording to contrast real guidance, and named the required formula revision for the spec owner.
- Spec conflict: the complete 680x425 stub and all form controls cannot coexist with 44-pixel rows and the required document focus. Retained internal scrolling and prioritized hours/pay rate; no whole-stub PASS claimed.
- Media limitation: browser speech works; the declared calm-professor/Schedar voice has no recordings. No audio was recorded, as CODEX-BUILD requires.

## Break it

- Closest guess: swept inputs, checked, copied Sam's revealed answer and retried. The cold first error stayed $448.35 while practice improved to $0.35. The exhaustive final sweep's $390.65 record also could not be improved by copying. No best is set before Check.
- Repeated Check cannot change its locked guess or increment an already checked attempt. Stub lookup, changed pay and zero hours cannot earn a first-unseen tally. No guesses or tally survive reload.
- Covered amounts, YTD, employer contributions and take-home share remain unavailable before Check. A visible gross is the intended input, not a net giveaway.
- Rapidly opening every line records visits only; it does not claim mastery or award a score. No quiz/reflection gate exists.
- Arithmetic check and take-home bar: independently recomputed the three originals, two hour changes and cap crossing using Decimal; zero pay, maximum weekly gross, minimum-rate refusal and exact-cent sums pass browser assertions.
- Motion-off race: old bundle accepted employerFica while revealing; repaired bundle keeps selection null and its button disabled. Next/Try again interruptions are included in the final audit.
- Zero and underfunded setups: zero uses an undefined-percentage explanation and earns no tally; an underfunded setup admits no guess. Biggest-mover comparison and stale validation were exercised directly. Retry resets focus correctly.

## Voice walk

Held 120 ms clicks at a 2-second pace: title, gross, health, federal, SS, net, close, Change it, hours, Guess first, slider, Check, then four retries/checks. Read/Sound/mode-switch side path checked separately.
Main log order: welcomeStub, plainHow, welcomeChange, deltaBig, welcomeGuess, guessResult five times. Screen values matched the result text. First welcomes may be cut by acting, per BASELINE 16.

| Line | Kind | Expected | Heard |
|---|---|---|---|
| plainHow | how | once across five openings | 1 |
| guessResult | event | five checks | 5 |
| deltaBig | event | five key edits plus slider click | 6 |

Final healthy main-path rerun after the card repair retained that order. The underfunded instruction spoke at 1366 and 680; its guard admitted no attempt at those sizes or 375. Zero's prompt and result were checked. Read interrupts speech and can read with Sound off; mode changes drop stale speech. Salary-specific welcome was heard in the cold Avery walk. Eight fixed strings match the manifest; no recorded Schedar claim.

## Facts checked

- Fictional workers, employers, addresses, pay, ages, premiums and match rates: spec Content, not claims about actual employers. 52/26/24/12 checks, equal prior pay and half-up rounding are stated model assumptions.
- 2026 single-filer $16,100 deduction; 10/12/22/24/32/35/37% bracket rates and all cutoffs: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf), checked live. Decimal results are in `review-calculations.json`.
- SS 6.2%, $184,500 cap, Medicare 1.45% without a cap: [SSA 2026 Changes](https://www.ssa.gov/news/en/cola/factsheets/2026.html). Avery check 23 is $154.18 SS; check 24 is zero.
- Additional Medicare 0.9% employer withholding above $200,000, no employer match: [IRS Additional Medicare Q&A](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax).
- Qualified pre-tax health reduces income-tax and FICA wages; pre-tax 401(k) reduces income-tax wages and remains subject to FICA: [IRS Publication 15](https://www.irs.gov/publications/p15), [15-B](https://www.irs.gov/publications/p15b). Annual retirement limits are explicitly omitted.
- Withholding is an estimate, not this tool's exact tax return: [IRS 15-T](https://www.irs.gov/publications/p15t). Kept the spec's annualized method, not new payroll tables.
- Federal $7.25 floor and 1.5-times overtime after 40 hours in each workweek: [US DOL FLSA](https://www.dol.gov/agencies/whd/flsa). The model does not implement higher state wage floors.
- Work credits and retirement/disability/survivor benefits: [SSA credits](https://www.ssa.gov/benefits/retirement/planner/credits.html). Medicare mainly age 65+: [SSA Medicare](https://www.ssa.gov/medicare).
- KFF 2025 $9,325 is total single premium, workers average 16%; employer 84% is a model: [KFF survey](https://www.kff.org/health-costs/2025-employer-health-benefits-survey/). Existing correction confirmed, not claimed as a new fix.
- Location numbers: spec Sources and First Apartment Budget notes define the approximations. Compared with [Ohio law](https://codes.ohio.gov/ohio-revised-code/chapter-5747), [Columbus](https://www.columbus.gov/Government/City-Auditor/Income-Tax-Division/General-Income-Tax-Information), [Colorado DOR](https://tax.colorado.gov/individual-income-tax-guide), [Arizona 2026 140ES](https://azdor.gov/sites/default/files/document/FORMS_INDIVIDUAL_2026_140ES_f.pdf), [Massachusetts rates](https://www.mass.gov/info-details/tax-rates), [Indiana DOR](https://www.in.gov/dor/resources/tax-rates-and-reports/rates-fees-and-penalties/), [Allen County](https://www.allencounty.in.gov/251/Local-Income-Taxes). These are not certified real withholding estimates.
- Texas no personal income tax: [Texas Governor economic development](https://gov.texas.gov/business/page/business-climate). Washington's 2026 wage-income model: [Washington Fiscal Information](https://fiscal.wa.gov/Revenue/RevenueOverview). Massachusetts 5% and single $4,400 exemption: [2026 Circular M](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download), official search extract; direct access was blocked.
- Massachusetts generally excludes eligible pre-tax 401(k) deferrals: [MA DOR pension guidance](https://www.mass.gov/info-details/tax-treatment-of-non-government-pensions) and [TIR 02-18](https://www.mass.gov/technical-information-release/tir-02-18-tax-changes-contained-in-an-act-enhancing-state-revenues-and-related-acts), official search extracts. The specified formula disagrees; its card now explains the contrast and the formula revision remains open.
- Denver $5.75/month and actual $500 monthly threshold: [Denver tax FAQ](https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Department-of-Finance/Our-Divisions/Treasury/Business-Tax-Information/Business-Tax-FAQ). Its threshold omission remains labeled, as the spec model requires.
- Original nets $232.73/$1,286.35/$1,803.48; Jordan 40 h $491.88; Sam no OT $1,201.46; restoring OT adds $13.62 federal and $84.89 net: independent arithmetic from the named rules above.

## Sensitivity

None requiring cultural review: fictional workers, no culture/religion/hard history or bodily depiction, no people art. Financial shortfalls are treated as model constraints, not personal failure; no household income is requested.

## Flattest moment left

After many line cards, exploring the same document remains quiet. Kept the professional older-grade tone; the named tax/benefit gap makes its most important comparison more concrete without adding a game.

## Graphics

Viewed all five finished images and scene placements, grayscale, all seven desktop sizes and a true 375-pixel iframe. Same warm editorial style; no fake lettering or people, all assets marked people:false. Marker redrawn with built-in imagegen, prompt/raw in art, free art.py --rekey processing; original preserved in Scratch. Bundle 286 KiB (292,539 bytes); art 143 KiB.
Recomputed contrast: accent/panel 10.02:1, ink/accent 10.13:1, paper ink 15.46:1, muted 5.95:1, positive 6.30:1, negative 7.22:1. Signs and text preserve meaning in grayscale.

## Audit

Exactly one full audit completed in about 32 minutes, with the 40-minute cap, Chrome 9941 and host 8745. It found 84 leads against its preserved pre-repair snapshot. All default sizes, Motion off and resize stress were clean; no JavaScript exceptions. All ten five-click rows were clean.

| Leads | Disposition |
|---:|---|
| 10 secondary settings scroll | Confirmed compact-form/spec constraint; hours and rate prioritized. |
| 2 grammar flags | False positives: Week 1 hours identifies a workweek. |
| 26 phone overlap/covered-paper flags | Intended bottom sheet; now a named nonmodal dialog. |
| 5 card control/hint leads | Fixed; controls stay visible during inner scrolling at every size. |
| 33 skipped first-tap welcomes | Allowed by BASELINE 16; hints and Read retain the instructions. |
| 7 quick welcome cuts | Allowed action interruptions under BASELINE 16. |
| 1 pristine Retry action | Fixed: disabled until meaningful, keyboard focus restored on reset. |

Re-shot all affected card sizes, re-walked the main voice path and re-ran the score cheats. Final held-key test scrolled the explanation 160 px, then Escape returned to a visible federal line. Targeted runs logged zero console errors. All 51 audit frames were viewed on six sheets; lead frames and every targeted PNG were also inspected. Evidence/index: `_scratch/paycheck-decoder/review-validation.json`.

## Left open

Massachusetts formula correction, missing shared money engine/doc, full 15-T tables, authentic bank recordings and complete compact-stub visibility require spec/kit/media work. No new topic or shared-file change made. Unattended decisions followed the spec/baseline; no question was required. Initial brief/runtime inspections completed before the full timeout wrapper was in place; all bundle, art, drive and audit commands had explicit limits. Test browsers/host closed; no host.html left.
