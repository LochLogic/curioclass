# Codex report: paycheck-decoder

## Built

Three fictional pay stubs, current/YTD line cards, dependency highlighting, Plain words, live timecard and benefit controls, and an interruptible prediction reveal. Five painted assets. Source is readable, uses the kit starter/frame, Curio.voice and Curio.tone, and bundles offline.

Scope: authored files stay in this tool and its Scratch folder; no commit, shared engine edit, audio recording or polish round. The direct owner's stop instruction takes precedence over the brief's early-report instruction, so this final report is created after checks.

Initial short file inspections preceded the timeout wrapper. Subsequent build/check commands used explicit caps: bundle 2 minutes, drive batches 5 minutes, audit 40 minutes. No check hit its cap.

## Numbers check

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

## Facts checked

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

## Break it

- Prediction slider swept through every whole dollar: no best was set before Check.
- Repeating a revealed answer: cannot improve the first-check tally. A changed or zero-pay stub cannot set it.
- Reading Stub before guessing: now marks that profile exposed and makes its guesses practice. Jordan begins exposed. Only an original unseen worker's first prediction enters the visit tally.
- Repeated Check while already checked: locked guess cannot be replaced. Next or Try again cancels the pending reveal timer and speech.
- Minimum-rate bypass: below $7.25 rejected and original input restored. Empty/non-finite values are rejected; check number is clamped to its schedule.
- Financial meter: the take-home share is derived from the exact net, and hidden before a guess reveal. No badge, score, assessment gate or persistent best exists.
- Payroll arithmetic: 6,000 fixtures, all sums exact in cents; additional Medicare is excluded from employer matching; no averaging away a separate overtime week.
- Dependency display: changed cards clear previous glows, and visible rate/hour/check-number inputs join the line highlights.

## Voice walk

Held presses of 120 ms at a 2 s pace. Main path logged welcomeStub, plainHow, welcomeChange, welcomeGuess, guessResult, guessResult. Read on the side path spoke the YTD card. Stale welcomes/results were cut when their action no longer fit.

Five line openings produced one plainHow; the final carry check showed it remained uncut across subsequent line selections. A click plus five keyboard hour changes produced six deltaBig starts. Motion and Sound off left no running infinite animation. Calm reveals all amounts immediately but preserves the result beat; targeted timing assertions passed. The salary-specific welcome is verified separately.

Browser speech is used; the declared bank choice is calm-professor/Schedar, but no Schedar recordings were made. This is an explicit media limitation.

## Feel check

Best moment: Sam's overtime comes back, the affected deductions light up with signed amounts, and the increase in net stays visibly smaller than the increase in gross.

Flattest moment 1: the first card buried its math behind repeated introductory copy. Hid that repeated intro while a card is open, brought Show me above the steps and kept the hint visible during panel scroll.

Flattest moment 2: the reveal finished but still described covered amounts. Changed its state wording, exposed a personal dollars/percent comparison and kept retry/next actions accessible in the compact result.

Opened fresh Scratch bundles of Snowy Mail Route and Beat Lab. `feel-comparison.png` puts this tool beside Beat Lab. The painted wood, paper texture, workplace scenes and physical marker support the professional document rather than turning it into a generic form. Full student path covered all workers and all three modes. Final compact result frames show the net, personal dollar error and percentage together; the phone explanation is visible.

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

All frames in first-frames, interaction-frames, size-frames, phone-frames, targeted-frames and voice-carry-frames; all five finished paintings and feel-comparison.png. Also inspected all 37 audit frames through seven contact sheets, 12 post-fix frames, three targeted-resize/phone frames, three final compact frames and the final phone result. Critical flagged frames were opened at full size. All 90 photographed states and source hashes are listed in `validation-summary.json`.

## Art made

5 images, all generated with the built-in image tool and processed with the free `art.py --rekey` form. Original PNGs and exact prompts are kept. No people, fake lettering or missing art. Total WebP 146,214 bytes (142.8 KiB), against a 300 KB art allowance. Recorded voice 0 KB. Final bundle 286,803 bytes (280.1 KiB), below the 2 MB goal. No redraw needed after inspection. Exact prompts and project copies are under `art/prompts.json` and `art/raw/`; the built-in image tool was used.

## Art still to paint

None.

## Engine changes wanted

Missing `kit/money.js` and `docs/families/money.md`: proposed pure API and rationale are in handoff.md. Shared promotion must wait for three actual finished users. This build makes no engine change.

## Left open

- Whole-stub 680x425 requirement conflicts with 44 px rows; compact controls and paper scroll.
- No recorded bank voice, as required by Build only.
- The full audit could not verify its original 375 iframe states because of the stale host. Separate final 375 checks pass. The stale host was stopped; all used ports were verified closed; host.html was removed.
- Extremely low-pay benefit setups can be underfunded. The form labels this; actual payroll carry-forward rules are outside the model.
