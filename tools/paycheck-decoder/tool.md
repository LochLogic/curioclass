# Paycheck Decoder: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: paycheck-decoder

#### Built

Three fictional pay stubs, current/YTD line cards, dependency highlighting, Plain words, live timecard and benefit controls, and an interruptible prediction reveal. Five painted assets. Source is readable, uses the kit starter/frame, Curio.voice and Curio.tone, and bundles offline.

Scope: authored files stay in this tool and its Scratch folder; no commit, shared engine edit, audio recording or polish round. The direct owner's stop instruction takes precedence over the brief's early-report instruction, so this final report is created after checks.

Initial short file inspections preceded the timeout wrapper. Subsequent build/check commands used explicit caps: bundle 2 minutes, drive batches 5 minutes, audit 40 minutes. No check hit its cap.

#### Numbers check

Independent Decimal calculations are in `_scratch/paycheck-decoder/recompute.py` and `calculations.json`. Source formulas also matched 6,000 seeded independent Decimal fixtures with zero differences, using every state model, schedule, benefit setting and cap region, including fractional hours and cent-valued rates. The 79-check initial browser run passed; later UI/guard changes have separate targeted evidence.

| Case | Recomputed result |
|---|---|
| Jordan | Gross $252.00; federal $0.00; SS $15.62; Medicare $3.65; net $232.73 |
| Sam | $1,560.00 + $117.00 = $1,677.00; net $1,286.35 |
| Avery | Gross $2,416.67; net $1,803.48 |
| Jordan, 40 h | Federal $25.28; SS $34.72; Medicare $8.12; net $491.88 |
| Sam, 40 + 40 h | Gross $1,560.00; federal $91.09; net $1,201.46 |
| Restore Sam overtime | Federal +$13.62; net +$84.89 |
| Avery $200,000, check 23 | Prior wages $182,013.26; taxable SS wages $2,486.74; SS $154.18 |
| Avery, check 24 | SS $0.00; no second Denver charge that month |

The stated example amounts agree. KFF's wording needed correction: $9,325 is total premium, not employer-only premium. Computed contrast ratios also differ slightly from the spec's rounded assertions, while all tested text pairs exceed 4.5:1.

#### Facts checked

- Fictional names, addresses, ages, pay, match rates, premiums and check numbers: spec Content, recomputed independently. Dates are an explicitly fictional consistent 2026 calendar.
- Single-filer brackets 10/12/22/24/32/35/37%, cutoffs $12,400/$50,400/$105,700/$201,775/$256,225/$640,600; standard deduction $16,100: [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf).
- SS 6.2% to $184,500 and Medicare 1.45% without a cap: [SSA 2026 changes](https://www.ssa.gov/news/en/cola/factsheets/2026.html).
- Additional Medicare 0.9% over $200,000 for employer withholding, no employer match: [IRS Q&A](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax).
- Retirement income-tax deferral versus FICA wages, and qualified pre-tax health: [IRS Publication 15](https://www.irs.gov/publications/p15), [Publication 15-B](https://www.irs.gov/publications/p15b).
- Annualized estimate differs from actual withholding tables; single/no-credit assumption stated: [IRS Publication 15-T](https://www.irs.gov/publications/p15t). Annual retirement contribution limits are explicitly omitted.
- Overtime applies over 40 hours separately each week at at least 1.5 times; federal floor $7.25: [DOL overtime](https://www.dol.gov/agencies/whd/overtime), [DOL minimum wage FAQ](https://www.dol.gov/agencies/whd/minimum-wage/faq).
- Retirement/disability/survivor eligibility and work credits: [SSA credits](https://www.ssa.gov/benefits/retirement/planner/credits.html). Medicare primarily serves people 65 and older: [SSA Medicare](https://www.ssa.gov/medicare).
- $9,325 average total single coverage and about 16% worker share in 2025: [KFF survey](https://www.kff.org/health-costs/2025-employer-health-benefits-survey/). Employer 84% is arithmetic/modeling; employee $1,440 is the spec's chosen example.
- TX/WA none; OH 2.75% above $26,050 and Columbus 2.5% after health; CO 4.4% of federal taxable income; AZ 2.5% above $16,100; MA 5% above $4,400 after health; IN/Allen 4.54% above $1,000: spec and sibling `tools/first-apartment-budget/notes.md`, labeled learning approximations, not verified real withholding tables.
- Denver $5.75/month: [official tax FAQ](https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Department-of-Finance/Our-Divisions/Treasury/Business-Tax-Information/Business-Tax-FAQ). The model explicitly omits the real earnings threshold.
- 52/26/24/12 checks, half-up line rounding, net subtraction, unchanged prior pay, capped low-pay health deductions and accumulated capped YTD are stated model assumptions.

#### Break it

- Prediction slider swept through every whole dollar: no best was set before Check.
- Repeating a revealed answer: cannot improve the first-check tally. A changed or zero-pay stub cannot set it.
- Reading Stub before guessing: now marks that profile exposed and makes its guesses practice. Jordan begins exposed. Only an original unseen worker's first prediction enters the visit tally.
- Repeated Check while already checked: locked guess cannot be replaced. Next or Try again cancels the pending reveal timer and speech.
- Minimum-rate bypass: below $7.25 rejected and original input restored. Empty/non-finite values are rejected; check number is clamped to its schedule.
- Financial meter: the take-home share is derived from the exact net, and hidden before a guess reveal. No badge, score, assessment gate or persistent best exists.
- Payroll arithmetic: 6,000 fixtures, all sums exact in cents; additional Medicare is excluded from employer matching; no averaging away a separate overtime week.
- Dependency display: changed cards clear previous glows, and visible rate/hour/check-number inputs join the line highlights.

#### Voice walk

Held presses of 120 ms at a 2 s pace. Main path logged welcomeStub, plainHow, welcomeChange, welcomeGuess, guessResult, guessResult. Read on the side path spoke the YTD card. Stale welcomes/results were cut when their action no longer fit.

Five line openings produced one plainHow; the final carry check showed it remained uncut across subsequent line selections. A click plus five keyboard hour changes produced six deltaBig starts. Motion and Sound off left no running infinite animation. Calm reveals all amounts immediately but preserves the result beat; targeted timing assertions passed. The salary-specific welcome is verified separately.

Browser speech is used; the declared bank choice is calm-professor/Schedar, but no Schedar recordings were made. This is an explicit media limitation.

#### Feel check

Best moment: Sam's overtime comes back, the affected deductions light up with signed amounts, and the increase in net stays visibly smaller than the increase in gross.

Flattest moment 1: the first card buried its math behind repeated introductory copy. Hid that repeated intro while a card is open, brought Show me above the steps and kept the hint visible during panel scroll.

Flattest moment 2: the reveal finished but still described covered amounts. Changed its state wording, exposed a personal dollars/percent comparison and kept retry/next actions accessible in the compact result.

Opened fresh Scratch bundles of Snowy Mail Route and Beat Lab. `feel-comparison.png` puts this tool beside Beat Lab. The painted wood, paper texture, workplace scenes and physical marker support the professional document rather than turning it into a generic form. Full student path covered all workers and all three modes. Final compact result frames show the net, personal dollar error and percentage together; the phone explanation is visible.

#### Done when

1. PASS: all Content amounts, exact sums; independent and browser evidence.
2. PASS: Jordan 40 h fixture and browser assertion.
3. PASS: Sam 40 + 40 removes OT; restoration deltas match.
4. PASS: line cards generated for every displayed line; numbered computations and source highlighting checked. Prior glows clear on a new card.
5. PASS: Avery cap crossing, check 23 $154.18; check 24 $0.00.
6. PASS: minimum-rate refusal and all-zero no-hours stub.
7. PASS: only changed current lines flash; signed tags replaced and expire after 3 s; reset restores original data.
8. PASS: reveal, dollar and percentage comparison, no persisted guesses; tally has the stricter unseen-first-check guard.
9. PASS: paper dominates the stage at 1366 and 680 in all modes. Measured paper/stage widths 992/1040 and 417/435 before the target-width correction.
10. PASS: rapid marker retarget and Next/Try-again reveal interruptions; audit stress disposition below.
11. PARTIAL/FAIL: 44 px row targets and five paintings pass; a whole stub cannot fit in 680x425 while preserving real-size 44 px rows. Internal paper scrolling is retained and documented.
12. PASS with media limitation: how-to starts once, events repeat and stale lines are cancelled. Browser fallback rather than recorded Schedar.

#### Wave lessons

- PASS, hint/voice: next control named, immediate hint updates, Curio.voice handles heard state; stable Plain words guidance survives successive lines. Salary gets a valid welcome.
- PASS, focus/layout: no load focus, inputs stay mounted, Escape returns to the current line after relabeling; sticky hint and preserved hint height.
- PARTIAL, sizes: all STANDARDS desktop sizes photographed; 375 direct host checked. Entire forms and documents require scrolling in compact boxes, retained as an explicit constraint.
- PASS, no giveaways: unseen-first-check guard prevents lookup/retry/zero-input tally setting. All deduction amounts and share bars are covered before reveal.
- PASS, honest numbers: learning assumptions and approximation line are visible; exact rounded-line sum and cap math checked. Contrast 10.02, 10.13, 15.46, 5.95, 6.30, 7.22 to 1 for the six tested pairs.
- PASS, standards: solo students decode gross/net, taxes and benefits, change a timecard and compare a prediction; NSPFE.Earning Income is practiced directly.
- PASS, Motion off: all infinite CSS animations stop. Amounts appear immediately; the result and narration keep the normal deadline.
- FAIL for compact full-form visibility; short choices: prediction actions stay visible; the timecard is a scrolling form at compact sizes, an unresolved strict all-controls-in-view requirement.
- PASS after repair, resize mid-animation: both flagged interruption paths pass the same audit resize methods with no errors or stuck controls.
- PASS, no late welcome: no welcomeAfter; action-specific speech takes priority.
- PASS, unknown is unknown: covered deduction values have neither readable amounts nor accessible answer labels.
- PASS, one look/meaning: apricot is selection/change; signed +/- values carry direction independently of color.
- PASS, badge truth: no earned badge or claimed skill score.
- PASS, hint restores: mode/worker/reset paths update state and instructions immediately.
- PASS, no word copying: no multiple-choice puzzle; prior answer exposure disables tally eligibility.

#### Audit leads

The single full audit completed in about 32 minutes: **90 pre-fix leads**, 37 saved frames. Its bundled snapshot remains in `audit/host/tool.html`. The full audit was not repeated after repairs; only affected states were rechecked.

| Leads | Disposition |
|---:|---|
| 6 compact header targets | FIXED: 44 px minimum width. Final 680 frame measures every header button at least 44 by 44. |
| 2 phone audit/context leads | Audit coverage gap: an owned stale host served the wrong directory. Stopped its recorded runtime; final direct 375 frames and the targeted phone Change it check pass. The original full-audit phone states remain unverified by that run. |
| 7 scrolling-form leads | 1280 fixed and checked against clipping ancestors. Secondary controls still scroll at 680/800/1000. Retained as an explicit strict all-controls-in-view failure, not dismissed as a clean audit. |
| 1 covered card hint | FIXED: sticky hint; final 680 hint is in front and fully visible after Show me. |
| 1 plural lead | False positive: `Week 1 hours` identifies the first week; it does not say a quantity of one hours. No change. |
| 4 compact result/action leads | FIXED: retry actions precede result details, `Checked` replaces the disabled `Revealed` label, and comparison/net are brought into view. Final 680 and 375 assertions pass. |
| 33 first-action welcome skips | Allowed by BASELINE rule 16. An action opens its card immediately and its how-to plays; the premise stays in the visible hint and Read. No delayed welcome is queued. |
| 25 inert edit-mode amount buttons | FIXED: every current/YTD and employer amount opens its card in Stub with edited values preserved. Held-click check confirms federal $91.09 and 40 hours survive. |
| 2 inert gross buttons in Guess first | FIXED: inspection is explicitly disabled while deductions are covered or revealing. The visible gross remains readable. |
| 2 resize interruption leads | FIXED: actions stay at the top and mode/worker panels reset their scroll. Targeted runs using the audit's own resize methods report no errors or stuck controls for Next and Try again. |
| 7 quick welcome cuts | Allowed action interruption per BASELINE rule 16; the current hint and Read remain available. Repeating a how-to after it has started would violate the once-per-load rule. |

All ten five-click audit rows were clean. No audit row reported a JavaScript exception. The initial direct phone host produced a favicon-only 404; final custom host runs have zero console/resource errors. All used ports are now closed.

#### Frames looked at

All frames in first-frames, interaction-frames, size-frames, phone-frames, targeted-frames and voice-carry-frames; all five finished paintings and feel-comparison.png. Also inspected all 37 audit frames through seven contact sheets, 12 post-fix frames, three targeted-resize/phone frames, three final compact frames and the final phone result. Critical flagged frames were opened at full size. All 90 photographed states and source hashes are listed in `validation-summary.json`.

#### Art made

5 images, all generated with the built-in image tool and processed with the free `art.py --rekey` form. Original PNGs and exact prompts are kept. No people, fake lettering or missing art. Total WebP 146,214 bytes (142.8 KiB), against a 300 KB art allowance. Recorded voice 0 KB. Final bundle 286,803 bytes (280.1 KiB), below the 2 MB goal. No redraw needed after inspection. Exact prompts and project copies are under `art/prompts.json` and `art/raw/`; the built-in image tool was used.

#### Art still to paint

None.

#### Engine changes wanted

Missing `kit/money.js` and `docs/families/money.md`: proposed pure API and rationale are in handoff.md. Shared promotion must wait for three actual finished users. This build makes no engine change.

#### Left open

- Whole-stub 680x425 requirement conflicts with 44 px rows; compact controls and paper scroll.
- No recorded bank voice, as required by Build only.
- The full audit could not verify its original 375 iframe states because of the stale host. Separate final 375 checks pass. The stale host was stopped; all used ports were verified closed; host.html was removed.
- Extremely low-pay benefit setups can be underfunded. The form labels this; actual payroll carry-forward rules are outside the model.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: paycheck-decoder

#### Played

Played cold as a grade 10 student before reading builder notes/source, then as a projector user. The paper and overtime reveal are strong; compact forms needed scrolling care. One review/fix pass, no commits.

#### Findings fixed

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

#### Findings left

- Should fix, spec conflict, family:money: Massachusetts model taxes retirement contributions even though eligible pre-tax 401(k) deferrals are generally excluded. The brief forbids changing a disputed spec formula. Preserved its calculation, corrected the on-screen wording to contrast real guidance, and named the required formula revision for the spec owner.
- Spec conflict: the complete 680x425 stub and all form controls cannot coexist with 44-pixel rows and the required document focus. Retained internal scrolling and prioritized hours/pay rate; no whole-stub PASS claimed.
- Media limitation: browser speech works; the declared calm-professor/Schedar voice has no recordings. No audio was recorded, as CODEX-BUILD requires.

#### Break it

- Closest guess: swept inputs, checked, copied Sam's revealed answer and retried. The cold first error stayed $448.35 while practice improved to $0.35. The exhaustive final sweep's $390.65 record also could not be improved by copying. No best is set before Check.
- Repeated Check cannot change its locked guess or increment an already checked attempt. Stub lookup, changed pay and zero hours cannot earn a first-unseen tally. No guesses or tally survive reload.
- Covered amounts, YTD, employer contributions and take-home share remain unavailable before Check. A visible gross is the intended input, not a net giveaway.
- Rapidly opening every line records visits only; it does not claim mastery or award a score. No quiz/reflection gate exists.
- Arithmetic check and take-home bar: independently recomputed the three originals, two hour changes and cap crossing using Decimal; zero pay, maximum weekly gross, minimum-rate refusal and exact-cent sums pass browser assertions.
- Motion-off race: old bundle accepted employerFica while revealing; repaired bundle keeps selection null and its button disabled. Next/Try again interruptions are included in the final audit.
- Zero and underfunded setups: zero uses an undefined-percentage explanation and earns no tally; an underfunded setup admits no guess. Biggest-mover comparison and stale validation were exercised directly. Retry resets focus correctly.

#### Voice walk

Held 120 ms clicks at a 2-second pace: title, gross, health, federal, SS, net, close, Change it, hours, Guess first, slider, Check, then four retries/checks. Read/Sound/mode-switch side path checked separately.
Main log order: welcomeStub, plainHow, welcomeChange, deltaBig, welcomeGuess, guessResult five times. Screen values matched the result text. First welcomes may be cut by acting, per BASELINE 16.

| Line | Kind | Expected | Heard |
|---|---|---|---|
| plainHow | how | once across five openings | 1 |
| guessResult | event | five checks | 5 |
| deltaBig | event | five key edits plus slider click | 6 |

Final healthy main-path rerun after the card repair retained that order. The underfunded instruction spoke at 1366 and 680; its guard admitted no attempt at those sizes or 375. Zero's prompt and result were checked. Read interrupts speech and can read with Sound off; mode changes drop stale speech. Salary-specific welcome was heard in the cold Avery walk. Eight fixed strings match the manifest; no recorded Schedar claim.

#### Facts checked

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

#### Sensitivity

None requiring cultural review: fictional workers, no culture/religion/hard history or bodily depiction, no people art. Financial shortfalls are treated as model constraints, not personal failure; no household income is requested.

#### Flattest moment left

After many line cards, exploring the same document remains quiet. Kept the professional older-grade tone; the named tax/benefit gap makes its most important comparison more concrete without adding a game.

#### Graphics

Viewed all five finished images and scene placements, grayscale, all seven desktop sizes and a true 375-pixel iframe. Same warm editorial style; no fake lettering or people, all assets marked people:false. Marker redrawn with built-in imagegen, prompt/raw in art, free art.py --rekey processing; original preserved in Scratch. Bundle 286 KiB (292,539 bytes); art 143 KiB.
Recomputed contrast: accent/panel 10.02:1, ink/accent 10.13:1, paper ink 15.46:1, muted 5.95:1, positive 6.30:1, negative 7.22:1. Signs and text preserve meaning in grayscale.

#### Audit

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

#### Left open

Massachusetts formula correction, missing shared money engine/doc, full 15-T tables, authentic bank recordings and complete compact-stub visibility require spec/kit/media work. No new topic or shared-file change made. Unattended decisions followed the spec/baseline; no question was required. Initial brief/runtime inspections completed before the full timeout wrapper was in place; all bundle, art, drive and audit commands had explicit limits. Test browsers/host closed; no host.html left.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Paycheck Decoder handoff

Build only, November 7, 2026. No commit and no polish round.

#### Cold review repairs, November 8, 2026

Preserved the desk, workplace paintings, apricot paper hierarchy, prediction guards and payroll formulas. Redrew the highlighter with the built-in image tool, keyed its magenta backdrop using `art.py --rekey`, and inspected the final 240-pixel asset and its 100-pixel scene placement. Prompt and raw image are in `art/`; the old asset is preserved in Scratch.

Employer-paid amounts now flash and show signed deltas, matching employee lines. Salary/worker and mode changes recompute the validation note so a rejected hourly rate cannot leave an hourly warning on Avery's salary form. Motion-off reveal keeps employer-card buttons disabled until the result beat, and `showCard` also guards the reveal, preventing a result from arriving over a newly opened card. The take-home bar names the tax/benefit gap and explicitly describes underfunded setups. Ohio's card names its omitted $332 base tax. Compact Change it hides a redundant heading and an empty validation note to keep hours and pay rate nearer the top.

No curriculum, formula, score, shared engine, voice recording or bank voice change. The annualized federal estimate, simplified location taxes, missing money engine and incompatible whole-stub/44-pixel preview requirements remain the spec decisions below. Review evidence is under `_scratch/paycheck-decoder/`, with `review-` or `-review` names; the builder's evidence is retained.

Compact Change it now scrolls the paper to the gross line on entry, so an hours edit has visible earnings beside it rather than just an employer header. Hour readouts keep their unit together and the two week sliders align. The phone timecard gets enough height for the hours and pay-rate controls together; secondary settings still scroll.

An underfunded setup also pauses Guess first before any attempt: Check/slider are disabled and the hint/Read/once-per-load how-to name Change it. This prevents the nonnegative slider from asking for an impossible negative deposit. Its fixed `underfundedGuess` line is included in the voice manifest and `allLines()`; healthy and zero-pay practice paths retain their original behavior.

The single review audit completed with 84 leads in about 32 minutes. Its old snapshot and all 51 frames are preserved in `review-audit/`. The confirmed card fix keeps Plain words, Close card, Show me and the hint outside a separate keyboard-focusable explanation scroller. Phone cards expose a named nonmodal dialog and focus Close without scrolling. The unopened list is retained. `drawLinks()` restores outlines after Plain words redraws the stub. Inner-paper scrolling brings a list-selected or returned focus line into view while preventScroll keeps the page still. The desk scene, signed feedback and full math steps are retained.

Try again is disabled until there is something to reset; after a retry the guess slider gets focus with preventScroll. The biggest-mover calculation now includes net, so Sam's OH-to-TX net gain of $56.20 is correctly larger than either individual removed tax. Zero-gross readouts avoid a false 0% of zero, with a zero-pay how-to and result event. There are seven fixed how-to lines and one fixed zero-result line in the manifest, plus the two dynamic event keys. No recording was made.

Spec correction wanted: the Massachusetts formula includes pre-tax retirement contributions even though eligible 401(k) deferrals are generally excluded under current MA DOR guidance. Do not silently rewrite the mandated formula. The card and notes now distinguish that model from the actual rule; return the formula to the spec owner. This is separate from the intentionally simplified Ohio base tax and Denver earnings-threshold omissions.

#### Structure

`src.html` starts from the kit starter's metadata, header, main/panel structure and kit initialization. It includes the 9-12 theme, then tool CSS, a document renderer, pure payroll functions, line cards and mode handlers. `window.__tool` exposes state, config, current amounts and pure calculations for testing. The bundle is generated, not hand edited.

The panel precedes the paper in DOM tab order. Workplace tabs stay selected across modes. Paper and panel have independent scrolling; the phone paper uses one column and a line card becomes a bottom sheet. Stable inputs are never replaced during slider changes. Paper rows are redrawn to show signed current-check deltas in reserved space. Tapping an amount while editing returns to Stub with that card open and preserves the edited values. Speech is routed through Curio.voice, and effects through Curio.tone.

#### Open question resolved

Keep the spec's annualized bracket estimate rather than implementing the full Publication 15-T tables. The federal card explains the distinction and assumes a single filer with no credits or extra withholding.

#### Spec conflicts and decisions

- The prompt requires the image tool; older spec text names local FLUX. Used built-in OpenAI image generation for all five paintings, each `drawn_by: codex` and `people: false`.
- All rows cannot remain 44 px while a complete four-box stub, employer strip, header and tabs fit in 680x425. Preserve target size and real pixels, with an internal paper scrollbar. The whole-stub preview requirement is left open, not claimed passed.
- YTD multiplication conflicts with capped Social Security, additional Medicare and once-monthly Denver charges. Sum the actual model checks for affected lines. Cards show the simple multiplication and then the corrected accumulated total.
- KFF's $9,325 is the total premium. Use it as total and explicitly model 84% as the employer portion. The $1,440 employee example remains the spec's chosen amount.
- The spec has no low-pay benefit shortfall rule. Limit the health deduction to gross minus retirement and label the rule in its card; show a form note if remaining taxes still exceed available pay. All-zero hourly stubs suppress benefits and taxes.
- Preserve both weeks when converting Sam's pay schedule. A later edit to the average hours deliberately replaces the alternating pattern, stated beside the slider.
- Denver's once-monthly tax uses the displayed dates, not an independent fractional-month counter. Weekly and biweekly checks begin January 2; semimonthly checks are the 15th and last day. This fixes a possible tax/date mismatch when schedules change.
- The nearest-guess tally could be set by copying an already revealed result, reading Stub first, or using zero-hour pay. Only the first check on an original unchanged positive-gross stub whose pay has not already been available in Stub or Change it enters the tally. Jordan starts as practice because the opening screen exposes it. Switching to an unseen worker in Guess first enables a first prediction. Retries are practice. Remembering a value from a previous visit is ordinary learning; no visit's tally persists.
- CODEX-BUILD asks for an early report, but the owner's direct prompt says stop when that file is written. The final report is created after checks; interim evidence stays in Scratch.
- The spec's instant Motion-off reveal is visual: amounts appear at once, while the result/voice beat keeps the same deadline as the animated reveal. This also honors STANDARDS' instruction to preserve timing. A mid-reveal Motion toggle preserves the remaining deadline.

#### Voice

Declared bank voice: calm-professor, Schedar. Seven fixed how-to lines, one fixed zero-result line, and two dynamic event keys, deltaBig and guessResult. No recording was made. Browser speech is the runtime fallback and cannot guarantee Schedar. Read speaks the current card's text when open. Mode changes, card changes and new edits hush stale speech. A still-valid Plain words how-to continues across successive line selections, then stays heard.

#### Engine changes wanted

`docs/families/money.md` and `kit/money.js` do not exist in this checkout. Proposed future shared API: `r2`, `money`, `fedTax`, `fica`, `stateTax`, `paycheck`. The tool-local `paycheck` returns integer cents, preserves week-specific overtime, applies partial Social Security cap crossing, and excludes additional Medicare from the employer match. Promote only after three finished tools actually share the implementation, per BASELINE rule 13. No shared file was edited.

#### Sensitivity

Financial learning model only. No culture, religion, hard history, bodily depiction or people artwork. Review that the fictional young workers are treated respectfully and that low earnings are never framed as personal failure. No household income is requested.

#### Evidence

`_scratch/paycheck-decoder/` holds independent Decimal calculations, 6,000 fixture results, browser shots, voice logs, adversarial checks, audit output and comparison frames. Five original PNGs are in `art/raw`; five resized WebPs are used in the offline bundle. No host.html is required for normal use.

The single full audit completed with 90 leads against its preserved pre-fix bundle. Compact targets, card hints, edit-mode line actions, prediction actions and resize interruptions have targeted repair evidence. The audit's 375 host checks were blocked by a stale owned test server, which was stopped. Separate final 375 checks pass. All used browser ports and the host port were verified closed before the report. Compact forms and the 680 whole-stub requirement remain the documented layout constraint.

Windows test note: this machine's LibreOffice `python.exe` launches a separate runtime. Stopping its launcher did not stop the first HTTP server. The final host helper records the runtime PID, has a time limit and exits through a stop flag; its supervisor waits for shutdown. No test service remains on the assigned ports.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
