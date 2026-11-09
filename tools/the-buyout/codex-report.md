# Codex report: the-buyout

## Built

Four working modes, separate eight-quarter records, a deterministic logit model, exact previews, live input during play, Compare ratings and evidence, five regulator remedies, the full cap sweep, a structural memo check, and local saving. All 19 named images made individually with the built-in OpenAI image tool. Kit starter, theme, voice queue, Motion, Sound and Read used. Build only; no commits or polish round.

## Numbers check

Recomputed before implementing from the spec's parameterized scripts, copied into Scratch. Evidence: numbers.py, numbers.json, numbers.log and verification.json. 45 model and structural break checks pass. Rivals default profit $409,926.11; final HHI 3,126.979. At $10, loss $720,000; at $40, loss $649,734.97. Buyout at $22 and initial model serves 59,539.032; largest-remainder lane is 12 buyers and 8 nonbuyers. All remedy money totals and all eight cap outputs match the reference equations.

Totals use unrounded units: Do nothing 555,372, Block 713,855, Breakup 630,219, Cap $18 628,305, Common charger 663,506. The spec's summed rounded references are respectively 555,374, 713,856, 630,218, 628,304 and 663,506. No calibration was added to force rounded counts. Switch test computes 8,032.493 moving to rivals, displayed 8,032; spec says 8,033. The percentages remain 49% and 17%.

Rival prices, launch quarters and six/twelve/twenty-round best replies were recomputed. Best-reply convergence checks pass. The breakup initially copied a lab's progress to all brands; corrected it to the reference's owner-lab progress, retaining the divested brands' existing models. All five final remedy totals then match.

Contrast recomputed: violet/panel 8.09, violet/paper 8.78, dark button text/violet 8.55; teal/panel 9.28; coral/panel 7.80; reference grey/panel 5.78; gold/panel 10.31; shelf ink/ivory 15.43. All listed pairs pass AA.

## Facts checked

- Market size, eight quarters, quality values and costs, research points and costs, launch thresholds, merger savings, entry delay, government costs, buyer gain, profits, served counts, prices, shares, concentration and rankings: fictional model in spec Content, recomputed in numbers.py and independently implemented in JavaScript; verification.json.
- HHI squared percent owner shares, four equal firms 2,500, one owner 10,000, increase 7,500: [DOJ HHI](https://www.justice.gov/atr/herfindahl-hirschman-index) and computation. Over 1,800 and increase over 100: [2023 DOJ/FTC Guidelines section 2.1](https://www.justice.gov/atr/merger-guidelines/applying-merger-guidelines/guideline-1), explicitly dated in the UI.
- Staples/Office Depot, FTC suit and blocked 1997 merger, lower prices where both competed, poorly documented savings: [FTC case page](https://www.ftc.gov/legal-library/browse/cases-proceedings/9710008-staples-inc-office-depot-inc), FTC v. Staples, 970 F. Supp. 1066 (1997), and the FTC public brief. Precedent does not determine the fictional outcomes.
- Standard Oil, 1911 decision under the Sherman Act of 1890 and more than 30 companies: [court opinion](https://www.law.cornell.edu/supremecourt/text/221/1), with the spec's conservative count rather than a disputed exact number.
- AT&T, 1974 suit, 1982 agreement, seven regional companies in 1984, long distance retained: [Federal Judicial Center](https://www.fjc.gov/history/spotlight-judicial-history/breakup-ma-bell).
- BT, Littlechild's 1983 proposal and 1984 inflation-minus-three cap: [Littlechild 2024](https://www.jbs.cam.ac.uk/wp-content/uploads/2024/10/2024-eprg-littlechild-incentive-regulation.pdf). The quality-monitoring statement is also in the spec's paired historical sources. The simulated dollar cap is explicitly a different illustrative mechanism.
- EU common charger, Directive 2022/2380, 28 December 2024 and 28 April 2026 dates: [European Commission](https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red/one-common-charging-solution-all_en). Narrowed universal charger wording to port access; real power requirements still matter.
- Innovation disagreement: Schumpeter (1942), [Arrow (1962)](https://www.nber.org/books-and-chapters/rate-and-direction-inventive-activity-economic-and-social-factors/economic-welfare-and-allocation-resources-invention), and Gilbert (2006), all named in the spec. [Cunningham, Ederer and Ma (2021)](https://www.journals.uchicago.edu/doi/10.1086/712506) confirms less development of acquired overlapping drug projects. No claim that charger mergers follow that study.
- Possible savings versus lost-trade tradeoff: Williamson, Economies as an Antitrust Defense, AER 58(1), 1968, and OECD, The Standard for Merger Review, 2011, as cited in the spec. The ranking is a two-year model result, not a universal policy recommendation.

## Break it

- Profit, buyers, shares and HHI: tried $10, $40, generous Buyout pricing, and changed inputs during walking and autoplay. No score or best record can be set by tapping or sweeping. Readouts are calculated outcomes with visible assumptions, not skill ratings. $10 loses fixed and lab costs despite sales; $40 loses buyers and money.
- Compare rating gate: all three groups must be answered. Wrong answers show the specified explanation and no score. Trying every rating does not award correctness or a saved result. Switch results unlock only after the ratings and the performed Switch test.
- Mark gate: fewer than four quarters per run cannot mark. Exactly three distinct buyer measures are required for Compare evidence; a fourth mark is refused until one is removed. Resetting a run clears marks.
- Remedy/view gate: merely opening Do nothing is insufficient. At least two other remedies and both views are needed. Ranking the same remedy twice, an unopened remedy, or a missing second remedy fails.
- Reason gate: barrier for Price cap fails, including when paired with a fitting market-power reason. All selected reasons must fit. Do nothing accepts savings; Common charger accepts entry barrier or market power.
- Evidence gate: duplicate, stale cap, wrong-remedy and unavailable evidence fail. Exactly two current chips are required and one must be a ledger difference for the first remedy. Editing invalidates Check and Save rechecks; forcing a disabled Save button did not store an invalid memo.
- Sentence gate: eleven words and repeated-word padding fail. Added eight distinct words to the twelve-word minimum. A fluent but weak argument can still pass; the UI explicitly calls this a structure check and asks for discussion, with no mastery score.
- Save/privacy: successful memo stored text, remedies, reasons, view, cap and snapshots of evidence. Privacy message verified. Reload restores a draft without granting completed evidence or a valid check.

## Voice walk

Main and side walks use held 120ms clicks at a two-second pace. No recordings made; news-reader is specified, browser speech is the kit fallback. Read always uses the live hint. Welcomes have valid state checks; four mode welcomes and Compare's enabled-only Switch instruction were observed starting. Repeated how-to triggers use V.heard through the kit, not action counters.

Initial walk found event lines waiting behind welcomes and a redundant post-Switch how line waiting after its action was already complete. Fixed launch and remedy events to take priority and removed that redundant queued instruction while retaining its live hint and Read. Once-per-run notices now use a run-specific heard key, so a dropped queued notice is not consumed.

Default main path, in order, from default-voice.json: welcomeRivals, launchSparrow30, launchOhmly30, launchSparrow45, launchOhmly45, runDone, welcomeBuyout, launchAll30, launchAll45, runDone, welcomeCompare, compareSwitch, switchResult, welcomeRegulator, remedyBlock, remedyCap, memoReasons. The separate saved-memo walk heard memoEvidence and memoWrite. Side path, voice-side.json: welcomeCompare, Read, welcomeRegulator, memoReasons, memoNeedFirst, memoWrite. Its old remedyStandard drop preceded the event-priority fix; the completed audit subsequently records every remedy event starting.

Simultaneous launches still have more speech than fits between two-second actions. Visual watts update instantly; stale remaining event lines drop when quarters change. This is reported as a pacing limitation, not a claimed all-lines pass. Slower play gives each quarter's sequence time to finish. Read, mode switching, empty Evidence guidance, memo steps and structural success/failure were also exercised.

## Feel check

Best moment: raising the Buyout price and seeing old-charger icons replace rival sales, then discovering that the buyer and everyone rankings disagree. The student's own numbers survive into Compare and the memo, giving the session a concrete result.

Flattest moment 1: early cartons filled their grid tracks and pushed all tags out of the main shelf. Fixed minimum-size behavior, brought names, watts, prices and shares together, and separated the twenty figures so outcomes are readable.

Flattest moment 2: the remedy ledger initially looked like another static table. Added ownership bars whose height traces average prices across quarters, breakup at Q5, entrant boxes at Q3, and a coral cap line with falling stars. The buyer-gain chart remains on its own scale. Later quarters change models and competitor behavior; they are not repetitions of Q1.

Frames compared: frame-comparison.png places the painted shelf beside Beat Lab. The tool has comparable depth and a richer material scene; no confetti or mascots. Its appeal is testing the market and defending a specific tradeoff. It has not been through a polish round.

## Done when

1. PASS: initial four $16 boxes dominate the scene; first Next commits Q1. first and final default frames.
2. PASS: default eight-quarter profit $0.41M, HHI 3,127; $40 loss. verification.json and loss frame.
3. PASS: Buyout $22 gives 59,539, twelve painted buyers and eight old chargers; dashed owner reference appears after Q1.
4. PASS: real drag during walking changed next price to $31. During autoplay, Q1 used $16, immediate preview used $40, Q2 used $40, and Q8 completed. live-input.json and autoplay-live.json.
5. PASS: all four modes and memo controls fit at 1366x768; the named folds work at 680x425. The full audit covers seven desktop/preview sizes; separate hosted 375px checks show primary controls without sideways scroll. Phone ledger details scroll vertically. Automatic phone audit coverage remains a gap, described below.
6. PASS with numerical correction: HHI feedback and Switch results 49% and 17%, profit down with rivals and up after buyout. 8,032 to rivals by direct computation.
7. PASS: all five remedy money totals match; $18 cap is Basic in Q1-Q4 then Flimsy in Q5-Q8, with cap line and quarter stars.
8. PASS: default rankings match both lists; Williamson and critics visible. The cap slider can legitimately change rankings, as the spec's cap sweep requires.
9. PASS: misfit reason, absent second and eleven words fail; complete memo saved with privacy line. Structural check has no mastery claim.
10. FAIL (speech pacing): mode how lines start once; single launch sequences start on their quarter after priority fix. Simultaneous announcements can become stale at the required two-second pace, documented above.

## Wave lessons

- Hint and voice: FAIL for simultaneous speech pacing; other checks pass: live hint updates independently of speech, names the next enabled control, Read exercised; stale speech uses validity checks. See pacing limit above.
- Focus and layout: PASS: persistent controls, reserved hint space, preventScroll on intentional focus. Finished buttons move focus to the next useful control. Explicit spec exception: Price receives load focus.
- Sizes: PASS with the automatic iframe coverage gap below. Primary controls are 44px; short scenes fold charts, page rating groups and memo leaves, and show the full Check result in place of the editor.
- No giveaways: PASS: no correctness score, hidden solution, progress badge or best record. Simulated profit is explicitly a consequence, not proof of understanding. Structural checks do not claim semantic evaluation.
- Honest numbers: PASS: assumptions visible in the main desk and teacher notes. Units sold remain distinct from shoppers and shares of sales. Equations and all money outputs verified.
- Standards: PASS: competition ratings plus Switch; own-run buyer comparison; government-role reasons and explanation; remedy ledger, views and rankings. All four standards have a solo student action.
- Motion off: PASS: zero running animations in the calm browser frame, same autoplay timing, no blocking animation state.
- Short choices: PASS: current rating group, all five quality options, all three research options, all remedies, and each memo leaf stay in view. No scrolling choice panel.
- Resize during animation: PASS in the completed audit stress pass, with no exceptions or stuck controls. The crowd stores no removed node references; its animation serial invalidates old callbacks.
- Welcome timing: PASS: multi-mode kit welcome, no welcomeAfter; first-tap premise remains in hint and Read.
- Unknown as unknown: PASS: unplayed Compare measures say Not played, not zero or success. Preview is explicitly labeled.
- One look, one meaning: PASS: symbol plus color identifies brands; teal Rivals, coral Buyout, dashed grey reference, gold ownership/threshold.
- Badge truth: PASS: no earned badge; Opened counts visits only. Saved and checked are separate.
- Hint changes back: PASS: each mode and panel switch recomputes it; empty Evidence names Reasons instead of absent chips.
- No copying-answer shortcut: PASS: reasons require policy fit and numeric evidence; free explanation stays ungraded beyond structure.

## Audit leads

The single audit completed within the 40-minute limit, exit 0, with 32 leads. Its pre-fix snapshot is retained in audit/audit.md. No full audit was repeated. All held-click cases across all four modes and the ten five-click repetition cases had no runtime errors. Resize stress completed with no exceptions or controls left disabled.

- Read width, 3 size leads: fixed with a 44px minimum and reserved header widths. Native post-read-680 measures 44px and zero header shift on Sound.
- Load focus, 7 size leads: intentional spec exception. Price uses preventScroll exactly as requested; BUILD's general no-load-focus lesson conflicts with this explicit spec instruction.
- Phone iframe, 2 leads: the automatic probe could not find its iframe context, producing the secondary missing-hint lead. Hosted drive frames independently show the real hint and all primary controls at 375px. Ten task-specific native host children were later found behind the LibreOffice Python launcher and closed; earlier port contention is a plausible cause. The automatic phone-state filter was also corrected to 375x812 for the next review. This full automatic phone pass was not repeated.
- Buyout ribbon overlap, 2 grouped leads: fixed by wrapping within each product width, giving ribbons explicit width and padding, and painting them above the carton. Final 680 and 760 frames show no inter-ribbon overlap.
- Compare table/chart overlap, 4 leads at 1280x720: reduced the mini shelf/chart heights in this height band. Table bottom 577.5, chart top 618 in the focused check.
- Regulator table/case overlap, 2 leads at 1280x720: compacted the fixed rows and reduced noninteractive ledger cell padding. Final ledger bottom 615, case top 626.14.
- Narrow regulator labels, 4 grouped leads at 760x900: short symbol/price labels and star-only details at narrow widths. Six-brand Common charger frame shows no label overlap.
- Finish focus, 1 lead: capture focus before hiding the completed Finish row, then move it to the visible rating group with preventScroll. The native focus log preserves a control after each Finish.
- Textarea name, 1 lead: native label already existed; added explicit aria-label Your policy explanation for unambiguous audit and assistive use.
- First Play/Next welcome absent, 2 leads: accepted under BASELINE rule 16 and the spec's explicit first-tap exception. Both actions work at once, while the premise remains in the hint and Read.
- Rapid same-mode welcome cuts, 4 leads: fixed centrally by retaining the current mode and speech when its active tab is tapped. The focused native double Buyout tap leaves its welcome uncut.

Extra visual checks kept the compact memo Fix list and privacy line in view, updated result hints to Edit or Save, and made the figure unit visible on the lane. Memo result speech is invalidated by later edits; cap narration validates the cap it describes. Early driver quoting and host favicon failures were resolved in smaller focused retries. Last focused batches report zero console errors, warnings or exceptions. The current bank metadata is news-reader / Rasalgethi, 37 fixed lines, no recordings.

## Frames looked at

All 44 full-audit PNGs were inspected through eleven four-frame sheets, with problem frames opened separately. All 17 focused post-audit/final PNGs were inspected on post-sheet.png; final ownership, 1280 ledger and saved-memo frames were also opened individually.

Bar: Beat Lab and Snowy Mail Route, bundled in Scratch and opened. Initial default, 680, Compare and cap frames. Full default batch: 680, 800, 1000, 1280, 1366, 1920, 760, hosted 375, keyboard, calm and grayscale. Both large and compact Buyout, Compare and Regulator; all remedy scenes and $40 loss. Main/student and side paths, saved memo, evidence leaf, real case, live drag and hosted phone recheck. Contact sheets A, B, C and focused D/final frames, with compact problem frames opened individually.

## Art made

19 individual images, including six people assets. Total finished art 240.8 KiB; offline bundle 548.0 KiB; recorded voice 0 KiB. Budget was 850 KiB art and zero recorded voice against 2 MiB. All assets inspected on a dark contact sheet and in the tool. No image redraws were needed. Full prompts and people flags are in art/prompts.json; raw originals in art/raw.

## Art still to paint

None. People art still needs the independent review in the next cold-review stage before shipping.

## Engine changes wanted

None. No shared kit, script or family-engine source was edited.

## Left open

The full audit is complete, but its automatic 375px iframe probe failed. Manual hosted phone evidence is retained; the next cold review should revisit automatic iframe coverage.

- Exact news-reader timbre is not available without recordings, which this build explicitly forbids. Browser fallback is used.
- Simultaneous spoken launch events can outlast the two-second input pace. Visual events remain exact and current.
- A structural sentence checker cannot judge an argument's economic quality. The UI says so and gives no mastery badge.
- All spec/brief contradictions and the settled open question are documented in handoff.md.
- Scope incident: an early quality-bar command regenerated the ignored tools/snowy-mail-route/snowy-mail-route.html bundle before bar builds were moved to Scratch. Its source was not edited. All authored tool files and subsequent bar copies are confined to the requested tool and Scratch folders.

Final cleanup: all used Chrome debug ports (9980, 9981) and host port 8785 are closed. host.html is removed. Native host child cleanup is recorded in host-cleanup.json. final-manifest.json records artifact hashes, exact byte sizes, 45 passing checks and the completed audit. The report stayed as a Scratch draft until this final placement to honor the user's stop-on-report instruction.
