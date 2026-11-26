# The Buyout: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: the-buyout

#### Built

Four working modes, separate eight-quarter records, a deterministic logit model, exact previews, live input during play, Compare ratings and evidence, five regulator remedies, the full cap sweep, a structural memo check, and local saving. All 19 named images made individually with the built-in OpenAI image tool. Kit starter, theme, voice queue, Motion, Sound and Read used. Build only; no commits or polish round.

#### Numbers check

Recomputed before implementing from the spec's parameterized scripts, copied into Scratch. Evidence: numbers.py, numbers.json, numbers.log and verification.json. 45 model and structural break checks pass. Rivals default profit $409,926.11; final HHI 3,126.979. At $10, loss $720,000; at $40, loss $649,734.97. Buyout at $22 and initial model serves 59,539.032; largest-remainder lane is 12 buyers and 8 nonbuyers. All remedy money totals and all eight cap outputs match the reference equations.

Totals use unrounded units: Do nothing 555,372, Block 713,855, Breakup 630,219, Cap $18 628,305, Common charger 663,506. The spec's summed rounded references are respectively 555,374, 713,856, 630,218, 628,304 and 663,506. No calibration was added to force rounded counts. Switch test computes 8,032.493 moving to rivals, displayed 8,032; spec says 8,033. The percentages remain 49% and 17%.

Rival prices, launch quarters and six/twelve/twenty-round best replies were recomputed. Best-reply convergence checks pass. The breakup initially copied a lab's progress to all brands; corrected it to the reference's owner-lab progress, retaining the divested brands' existing models. All five final remedy totals then match.

Contrast recomputed: violet/panel 8.09, violet/paper 8.78, dark button text/violet 8.55; teal/panel 9.28; coral/panel 7.80; reference grey/panel 5.78; gold/panel 10.31; shelf ink/ivory 15.43. All listed pairs pass AA.

#### Facts checked

- Market size, eight quarters, quality values and costs, research points and costs, launch thresholds, merger savings, entry delay, government costs, buyer gain, profits, served counts, prices, shares, concentration and rankings: fictional model in spec Content, recomputed in numbers.py and independently implemented in JavaScript; verification.json.
- HHI squared percent owner shares, four equal firms 2,500, one owner 10,000, increase 7,500: [DOJ HHI](https://www.justice.gov/atr/herfindahl-hirschman-index) and computation. Over 1,800 and increase over 100: [2023 DOJ/FTC Guidelines section 2.1](https://www.justice.gov/atr/merger-guidelines/applying-merger-guidelines/guideline-1), explicitly dated in the UI.
- Staples/Office Depot, FTC suit and blocked 1997 merger, lower prices where both competed, poorly documented savings: [FTC case page](https://www.ftc.gov/legal-library/browse/cases-proceedings/9710008-staples-inc-office-depot-inc), FTC v. Staples, 970 F. Supp. 1066 (1997), and the FTC public brief. Precedent does not determine the fictional outcomes.
- Standard Oil, 1911 decision under the Sherman Act of 1890 and more than 30 companies: [court opinion](https://www.law.cornell.edu/supremecourt/text/221/1), with the spec's conservative count rather than a disputed exact number.
- AT&T, 1974 suit, 1982 agreement, seven regional companies in 1984, long distance retained: [Federal Judicial Center](https://www.fjc.gov/history/spotlight-judicial-history/breakup-ma-bell).
- BT, Littlechild's 1983 proposal and 1984 inflation-minus-three cap: [Littlechild 2024](https://www.jbs.cam.ac.uk/wp-content/uploads/2024/10/2024-eprg-littlechild-incentive-regulation.pdf). The quality-monitoring statement is also in the spec's paired historical sources. The simulated dollar cap is explicitly a different illustrative mechanism.
- EU common charger, Directive 2022/2380, 28 December 2024 and 28 April 2026 dates: [European Commission](https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red/one-common-charging-solution-all_en). Narrowed universal charger wording to port access; real power requirements still matter.
- Innovation disagreement: Schumpeter (1942), [Arrow (1962)](https://www.nber.org/books-and-chapters/rate-and-direction-inventive-activity-economic-and-social-factors/economic-welfare-and-allocation-resources-invention), and Gilbert (2006), all named in the spec. [Cunningham, Ederer and Ma (2021)](https://www.journals.uchicago.edu/doi/10.1086/712506) confirms less development of acquired overlapping drug projects. No claim that charger mergers follow that study.
- Possible savings versus lost-trade tradeoff: Williamson, Economies as an Antitrust Defense, AER 58(1), 1968, and OECD, The Standard for Merger Review, 2011, as cited in the spec. The ranking is a two-year model result, not a universal policy recommendation.

#### Break it

- Profit, buyers, shares and HHI: tried $10, $40, generous Buyout pricing, and changed inputs during walking and autoplay. No score or best record can be set by tapping or sweeping. Readouts are calculated outcomes with visible assumptions, not skill ratings. $10 loses fixed and lab costs despite sales; $40 loses buyers and money.
- Compare rating gate: all three groups must be answered. Wrong answers show the specified explanation and no score. Trying every rating does not award correctness or a saved result. Switch results unlock only after the ratings and the performed Switch test.
- Mark gate: fewer than four quarters per run cannot mark. Exactly three distinct buyer measures are required for Compare evidence; a fourth mark is refused until one is removed. Resetting a run clears marks.
- Remedy/view gate: merely opening Do nothing is insufficient. At least two other remedies and both views are needed. Ranking the same remedy twice, an unopened remedy, or a missing second remedy fails.
- Reason gate: barrier for Price cap fails, including when paired with a fitting market-power reason. All selected reasons must fit. Do nothing accepts savings; Common charger accepts entry barrier or market power.
- Evidence gate: duplicate, stale cap, wrong-remedy and unavailable evidence fail. Exactly two current chips are required and one must be a ledger difference for the first remedy. Editing invalidates Check and Save rechecks; forcing a disabled Save button did not store an invalid memo.
- Sentence gate: eleven words and repeated-word padding fail. Added eight distinct words to the twelve-word minimum. A fluent but weak argument can still pass; the UI explicitly calls this a structure check and asks for discussion, with no mastery score.
- Save/privacy: successful memo stored text, remedies, reasons, view, cap and snapshots of evidence. Privacy message verified. Reload restores a draft without granting completed evidence or a valid check.

#### Voice walk

Main and side walks use held 120ms clicks at a two-second pace. No recordings made; news-reader is specified, browser speech is the kit fallback. Read always uses the live hint. Welcomes have valid state checks; four mode welcomes and Compare's enabled-only Switch instruction were observed starting. Repeated how-to triggers use V.heard through the kit, not action counters.

Initial walk found event lines waiting behind welcomes and a redundant post-Switch how line waiting after its action was already complete. Fixed launch and remedy events to take priority and removed that redundant queued instruction while retaining its live hint and Read. Once-per-run notices now use a run-specific heard key, so a dropped queued notice is not consumed.

Default main path, in order, from default-voice.json: welcomeRivals, launchSparrow30, launchOhmly30, launchSparrow45, launchOhmly45, runDone, welcomeBuyout, launchAll30, launchAll45, runDone, welcomeCompare, compareSwitch, switchResult, welcomeRegulator, remedyBlock, remedyCap, memoReasons. The separate saved-memo walk heard memoEvidence and memoWrite. Side path, voice-side.json: welcomeCompare, Read, welcomeRegulator, memoReasons, memoNeedFirst, memoWrite. Its old remedyStandard drop preceded the event-priority fix; the completed audit subsequently records every remedy event starting.

Simultaneous launches still have more speech than fits between two-second actions. Visual watts update instantly; stale remaining event lines drop when quarters change. This is reported as a pacing limitation, not a claimed all-lines pass. Slower play gives each quarter's sequence time to finish. Read, mode switching, empty Evidence guidance, memo steps and structural success/failure were also exercised.

#### Feel check

Best moment: raising the Buyout price and seeing old-charger icons replace rival sales, then discovering that the buyer and everyone rankings disagree. The student's own numbers survive into Compare and the memo, giving the session a concrete result.

Flattest moment 1: early cartons filled their grid tracks and pushed all tags out of the main shelf. Fixed minimum-size behavior, brought names, watts, prices and shares together, and separated the twenty figures so outcomes are readable.

Flattest moment 2: the remedy ledger initially looked like another static table. Added ownership bars whose height traces average prices across quarters, breakup at Q5, entrant boxes at Q3, and a coral cap line with falling stars. The buyer-gain chart remains on its own scale. Later quarters change models and competitor behavior; they are not repetitions of Q1.

Frames compared: frame-comparison.png places the painted shelf beside Beat Lab. The tool has comparable depth and a richer material scene; no confetti or mascots. Its appeal is testing the market and defending a specific tradeoff. It has not been through a polish round.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

All 44 full-audit PNGs were inspected through eleven four-frame sheets, with problem frames opened separately. All 17 focused post-audit/final PNGs were inspected on post-sheet.png; final ownership, 1280 ledger and saved-memo frames were also opened individually.

Bar: Beat Lab and Snowy Mail Route, bundled in Scratch and opened. Initial default, 680, Compare and cap frames. Full default batch: 680, 800, 1000, 1280, 1366, 1920, 760, hosted 375, keyboard, calm and grayscale. Both large and compact Buyout, Compare and Regulator; all remedy scenes and $40 loss. Main/student and side paths, saved memo, evidence leaf, real case, live drag and hosted phone recheck. Contact sheets A, B, C and focused D/final frames, with compact problem frames opened individually.

#### Art made

19 individual images, including six people assets. Total finished art 240.8 KiB; offline bundle 548.0 KiB; recorded voice 0 KiB. Budget was 850 KiB art and zero recorded voice against 2 MiB. All assets inspected on a dark contact sheet and in the tool. No image redraws were needed. Full prompts and people flags are in art/prompts.json; raw originals in art/raw.

#### Art still to paint

None. People art still needs the independent review in the next cold-review stage before shipping.

#### Engine changes wanted

None. No shared kit, script or family-engine source was edited.

#### Left open

The full audit is complete, but its automatic 375px iframe probe failed. Manual hosted phone evidence is retained; the next cold review should revisit automatic iframe coverage.

- Exact news-reader timbre is not available without recordings, which this build explicitly forbids. Browser fallback is used.
- Simultaneous spoken launch events can outlast the two-second input pace. Visual events remain exact and current.
- A structural sentence checker cannot judge an argument's economic quality. The UI says so and gives no mastery badge.
- All spec/brief contradictions and the settled open question are documented in handoff.md.
- Scope incident: an early quality-bar command regenerated the ignored tools/snowy-mail-route/snowy-mail-route.html bundle before bar builds were moved to Scratch. Its source was not edited. All authored tool files and subsequent bar copies are confined to the requested tool and Scratch folders.

Final cleanup: all used Chrome debug ports (9980, 9981) and host port 8785 are closed. host.html is removed. Native host child cleanup is recorded in host-cleanup.json. final-manifest.json records artifact hashes, exact byte sizes, 45 passing checks and the completed audit. The report stayed as a Scratch draft until this final placement to honor the user's stop-on-report instruction.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: the-buyout

#### Played
Cold Grade 12 solo play: both eight-quarter runs, Compare, every remedy, both views and Memo before builder notes/source; then a projection check. The shop and buyer substitution are strong; the policy clash earns discussion.

#### Findings fixed
- blocker, general, Memo: twelve isolated letters passed Check and enabled Save. Only words count, with a/I allowed; padding now fails and a complete memo still saves.
- should fix, general, 680px Memo: the maximum eight evidence chips clipped the last two choices. Consolidated compact navigation and removed instructions duplicated in the hint, retaining 44px choices.
- should fix, general, 375px Compare: the fifth buyer row fell below the fold after Switch. Shortened mini shelves and compact result typography; all five rows now fit.
- should fix, family:market, voice: simultaneous launches dropped later makers. Each shared launch now has one fixed combined event; completion and Switch results start at their trigger.
- should fix, family:market, feedback: 7,500 looked like the difference between students' final runs. Named the four-equal-owner starting point and the rebuttable nature of the guideline presumption.
- should fix, family:market, BT case: wrongly attributed the chosen three-point cap to Littlechild's report. Distinguished his RPI-X proposal from the later government cap.
- should fix, general, hints/focus: Buyout's end named its current mode; partial Compare could name a disabled Finish control; Read's fixed hints were absent from the inventory; a top-model research button could retain disabled focus. Corrected all four.
- should fix, general, compact case toggle: changing remedies could leave Back to ledger on an already-visible ledger. Label and aria-expanded now follow the actual state.
- polish, family:market, flat Switch/Compare handoff: added proportional buyer-flow tracks and a next-step hint after three marks. Retained the shop, palette, ownership graphics and deliberate welfare clash.
- polish, art: replaced the common-charger vignette with a matching-style painting whose three shared USB-C ports and cable connector are clearly visible.

- should fix, general, final craft: active memo navigation cut its own instruction, chart series depended on color, and Evidence could request an unavailable first-remedy ledger. Preserved active-page speech, added matching dotted/solid legends and corrected prerequisite hints.
- should fix, general, phone Buyout: the ownership banner overlapped its ribbons. Increased shelf room and separated the banner; zero overlap, Next at y=683.

#### Findings left
None known at blocker/should fix level.
- polish: rapid navigation cuts longer event speech. All four mode how-tos start once on the required path; no promise that every long event finishes before a student's next action.
- nit: a small magenta edge remains under one shopper shoe at enlarged inspection size; unobtrusive in the 34px lane.

#### Break it
- Profit/buyers/share/HHI: real end-to-end Price drag, $40 autoplay, rapid Next taps and the default Solid/Steady price sweep. No score/best record exists; $40 loses $649,734.97, and at-cost $10 loses $720,000. Repeated taps book exactly eight quarters.
- Lab meter: inspected no-research and Fast/top-model behavior; at 65 W research disables and focus moves to Next. This is model progress, not a mastery meter.
- Ratings: wrong choices and trying options unlock the unscored demonstration, with corrective explanations. No correctness or saved skill result is awarded, as the spec intends.
- Compare marks: early marking is refused; four/five taps retain at most three distinct rows. Exactly three current marks supply evidence, not a correctness grade.
- Remedy/view/ranking: one view, duplicate remedy and missing/unopened choices fail. Changing cap changes the actual welfare ranking; sweeping cannot set a best score.
- Reasons/evidence: misfit and mixed fitting/misfit reasons fail; one/duplicate chip, wrong-remedy and stale-cap evidence fail. Eight available chips remain accessible.
- Explanation/Save: alphabet padding, repeated-word padding and eleven words fail; complete structure passes and saves locally with privacy text. Editing invalidates Check. The check explicitly does not judge persuasive economic prose.
- Evidence: cold-*.json, cheap-*-after.json, final-memo-gates.json, live-preview.json, top-research-focus.json and independent-numbers.json in Scratch.

#### Voice walk
Default settings, held 120ms presses at two-second gaps: shelf, Rivals Q1-Q8, Buyout Q1-Q8, Compare ratings, Switch, three rows, Regulator, Block/Cap/Common, both views, Memo.
Started in order: welcomeRivals; Sparrow30; combined Ohmly/Tidewatt30; Sparrow45; combined Ohmly/Tidewatt45 + Sparrow65; runDone; welcomeBuyout; all30; all45; runDone; welcomeCompare; compareSwitch; switchResult; welcomeRegulator; Block; Cap; Common; memoReasons.
Mark/next-step lines are discarded when the student has already acted or left Compare; hints update immediately. Side checks covered Evidence, Write, Read interrupt, Sound off and mode changes.
| Line | Kind | Expected starts | Observed |
|---|---|---:|---:|
| Each mode welcome | how-to | 1 | 1 each |
| memoWrite, five taps | how | 1 | 1, preserved through repeat taps |
| remedyBlock, five taps | event | 5 | 5 |
All fixed Read hints and combined lines are in voice/lines.json and allLines. Browser fallback is used; no recordings were made.

#### Facts checked
- Remaining reference extremes independently recomputed in reference_extremes.py: None/Fast research, Flimsy/Premium quality, generous and $40 Buyout runs, owner research profits and six/twelve/twenty-round price convergence all match.
- Fictional shopper count, costs, quality values, research, savings, launches, logit shares, buyer gain, profit, HHI, remedy totals and all eight caps: spec Content, independently recomputed in independent_model.py; 59 numerical parity checks agree within 0.000001 in their respective units. Default profit $409,926.11; HHI 3,126.979.
- Unrounded counts explain small spec differences: 555,372 / 713,855 / 630,219 / 628,305 / 663,506 served. Switch computes 8,032.493 to rivals, displayed 8,032; 49% and 17%, and both profit directions, agree.
- HHI squared owner shares, 2,500/10,000, >1,800 and increase >100, rebuttable presumption: [DOJ/FTC 2023 Guideline 1](https://www.justice.gov/atr/merger-guidelines/applying-merger-guidelines/guideline-1), checked live.
- Staples/Office Depot 1997 block and lower prices with rivalry: [FTC case](https://www.ftc.gov/legal-library/browse/cases-proceedings/9710008-staples-inc-office-depot-inc) and [FTC pricing analysis](https://www.ftc.gov/news-events/news/speeches/econometric-analysis-ftc-v-staples); savings caveat also checked against the FTC's merger-specific-efficiencies account.
- Standard Oil 1911, Sherman Act 1890 and breakup into more than thirty: [Supreme Court opinion, 221 US 1](https://www.law.cornell.edu/supremecourt/text/221/1).
- AT&T suit 1974, agreement 1982, seven regional companies in 1984, retained long distance: [DOJ history](https://www.justice.gov/archives/atr/technological-innovation-and-monopolization) and [Congressional account](https://www.govinfo.gov/content/pkg/CRPT-106hrpt1048/html/CRPT-106hrpt1048.htm).
- BT: Littlechild's 1983 proposal and government's X=3 choice: [Littlechild 2024](https://www.jbs.cam.ac.uk/wp-content/uploads/2024/10/2024-eprg-littlechild-incentive-regulation.pdf); 1984 cap and service monitoring: [Oftel 1986 report](https://assets.publishing.service.gov.uk/media/5a7cac6fe5274a2f304ef634/0007.pdf).
- EU Directive 2022/2380, 28 Dec 2024 small-device and 28 Apr 2026 laptop dates: [European Commission](https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red/one-common-charging-solution-all_en). Port access is distinguished from required power.
- Schumpeter/Arrow innovation debate: Schumpeter 1942 and [Arrow 1962](https://www.nber.org/books-and-chapters/rate-and-direction-inventive-activity-economic-and-social-factors/economic-welfare-and-allocation-resources-invention); overlapping acquired drug projects less developed: [Cunningham, Ederer and Ma, JPE 2021](https://www.journals.uchicago.edu/doi/10.1086/712506). No charger-market inference claimed.
- Savings can outweigh lost trades in total welfare: Williamson 1968, confirmed by [OECD welfare framework](https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/10/economic-analysis-in-merger-investigations_697b181f/f9cc5dc4-en.pdf). Default buyer/total rankings are model results, not general policy advice.

#### Sensitivity
Six people assets checked, all people:true: varied ages, skin tones, bodies and clothing, including a shopper using a cane. Whole figures and ordinary agency are preserved. A fresh sensitivity lens should inspect representation and any perceived association between shopper identity and outcome; these figures represent aggregates, not demographic estimates. The regulation cases are historical precedents, not reenactments of personal harm.

#### Flattest moment left
The memo remains a deliberate writing pause. Its value is defending this student's tradeoff; automatic structure checking cannot judge the argument. Switch now shows the substitution and three marked measures lead clearly to Regulator.

#### Graphics
All 19 named assets inspected, including all six people; none missing (the spec prose totals twenty but enumerates nineteen). One redraw, via built-in imagegen, full prompt/provenance in art/prompts.json, raw in art/raw/remedy-standard.png, processed by art.py --rekey. Art about 241 KiB; bundle 553.4 KiB. Warm shop, dimensional cartons and ownership graphics retained.

#### Audit
The single audit finished inside forty minutes, exit 0, with 11 leads and 59 frames, all inspected. Eight Price load-focus notices follow the explicit spec; two first-tap welcome notices follow BASELINE rule 16. The one confirmed overlap, at 375px in Buyout, is repaired and re-shot at 375px.
All 50 held-click cases across four mode openings report no runtime errors; ten five-tap and ten rapid-tap cases are clean. The completed resize stress reports no exceptions or controls left disabled. No second full audit. Post-audit focused frames/logs cover repaired phone, memo navigation, prerequisite hints, filled grayscale charts and the main voice path.
Numerical and structural validation: 78 checks pass; sampled AA contrasts range from 5.78:1 to 15.43:1. Catalog module standards match the four spec codes and their student activities.

#### Left open
- Reference assumption: the spec's 39%/25% quality-cut comparison uses Rivals at $16 and the profit-seeking Buyout price of $22. Prices are not specified beside that example; no fixed quality-cut percentage is shown in the tool. The spec is unchanged.
- Retained explicit spec Price focus on load despite BUILD's general no-load-focus lesson; preventScroll is used. No questions were required.
- Exact news-reader timbre needs recordings; the brief prohibits recording audio. Browser fallback remains.
- Opening reads and a few short log-tail reads lacked termination timers. Bundle, drive and audit processes used bounded wrappers; bundle 120s, drive batches 300s, audit 2400s. No commits.
- An early manual host favicon 404 was corrected in the harness; final hosted phone shots have no console errors. The offline tool makes no network requests. Owned hosts and Chrome close before completion.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### The Buyout build handoff

#### Structure

src.html derives from the kit starter. It contains responsive scene CSS, persistent controls, a pure market model, then the application. It uses kit:curio, kit:theme-912, Curio.voice, Curio.tone and the kit Motion, Sound and Read controls. No family engine exists for this market. The generated offline file is the-buyout.html. tool.draft.json remains stage built for the next cold review.

The editable source is readable and uncompressed. Scratch includes assembly fragments, image-path provenance, raw number checks, browser test scripts, audit evidence and a contact sheet. Rebuilding from scratch fragments is a build convenience; future edits can go directly into src.html.

#### Tricky parts

- market uses unrounded logit probabilities, distinguishes all shoppers from shares of sales, and aggregates concentration by owner. One lab costs once per owner; fixed costs apply to each brand. Research advances after a committed quarter, for sale in the next one.
- Rivals post their sequential best responses once per quarter. Preview never repeatedly reprices competitors while the student slides Price. Buyout choices apply to all brands.
- A lab's research points belong to its lead firm. On breakup, the divested owner keeps the existing model but builds its own research progress. This matches the spec's calculation scripts and preserves the intended unequal Q8 models after the split.
- Market results update immediately. The crowd is a largest-remainder illustration of 20 figures, each about 5,000 shoppers. Crowd motion never blocks controls. Play to the end remains live; mode switches pause it. Each run is retained separately.
- Remedy firms are deterministic. All defaults and the cap sweep use the same best-reply solver. Real case cards provide historical precedents, not causal estimates for the model. Changing a cap can change the view rankings.
- Compare marks require four played quarters per run and exactly three buyer measures. Ratings teach with feedback and have no correctness score. Switch evidence requires all ratings and a performed test.
- Memo uses three visible leaves to avoid a scrolling panel. The check verifies reason fit, different opened remedies, both inspected views, two current evidence chips including a ledger chip for the first remedy, and an explanation of at least 12 words with eight distinct words. It explicitly does not grade the argument's quality. Editing invalidates a successful check and Save rechecks everything.
- Saved writing is restored as a draft. Evidence is re-earned on a fresh run; stored values never confer completed status. localStorage failures are caught. The privacy statement appears beside Save.
- Voice metadata requests news-reader. No recordings were made because this is Build only with an explicit no-recording instruction. The kit falls back to browser speech, so the bank's exact timbre is not guaranteed.

#### Open questions and build decisions

- The sole listed open question is settled in the spec. Retained the default clash: Buyers' view puts Block it first, Everyone's view puts Do nothing first. Kept the Williamson note and critics, with no extended horizon.
- The art paragraph says 14 plus 6 people images but names 19 assets. Made all 19 individually: shelf, six cartons, six shoppers, old charger and five remedies. Every shopper has people: true. The owner explicitly requests the image tool, so these use OpenAI gpt-image rather than the older Gemini wording.
- CODEX-BUILD and the user require painted art, overriding BUILD's old Do not draw art sentence. All drawings are newly generated and credited. No placeholders remain.
- The spec explicitly requests load focus on Price, while BUILD's wave lesson says nothing takes focus on load. Followed the more specific spec with preventScroll; cold review should retain this documented exception or settle it.
- The stated 896px stage plus 470px panel exceeds 1366px once gaps are included. The desktop split is approximately 66/34 with the panel inset inside its width.
- At small sizes the non-buyer Compare measures fold away while the five buyer rows remain. Memo uses three leaves within its required Memo page. This preserves 44px controls without a scrolling choice panel.
- At 680x425 the three Compare rating groups also page through Rivals, Buyout and Buyers, advancing to an unrated group after a choice. Group tabs preserve access to previous ratings. Small mini shelves abbreviate names to a symbol and initial and show watts; complete names are in tooltips and image alternatives. The main shelf keeps complete labels.
- At short heights a memo check replaces the editor with its complete six-part result list. Edit explanation restores the editor. This avoids clipping a failed requirement below the fold.
- The Compare welcome originally names Switch test before it is enabled. Reworded it to name the three rating groups; a separate how line names Switch test only after all ratings exist.
- The cap outcome retains the buyer-gain chart. Its ownership strip adds a coral cap line, quarter prices and falling stars, keeping price and dollar buyer gain on separate scales.
- The literal USB-C case phrase any charger works overstates universal power compatibility. Kept the specified dates and port standard while using the narrower phrase the standard opens the charging port. Teacher notes clarify power requirements.
- Exact total shopper counts differ by one or two from sums of rounded quarterly references. Display sums of unrounded units. The Switch test sends 8,032, not 8,033, to rivals. Numbers and differences are documented in the report.
- At a two-second tap pace, simultaneous launch announcements cannot all finish before the quarter changes. Launch sequences now interrupt older welcomes and start immediately, then drop remaining stale lines when the quarter moves on, as the event validity rule requires. Visual watts update immediately. The report records the actual logs rather than claiming all launch speech finishes.

#### Sensitivity

The six individually painted shoppers include varied ages, skin tones, clothing, body types and an older woman using a cane. They are ordinary shoppers with equal agency; nobody is tied to a particular purchasing outcome or moral category. The contact sheet is _scratch/the-buyout/art-sheet.png. A fresh reviewer should inspect people art for anatomy, representation and respectful portrayal before shipping. No cultural identity is asserted. The historical cases concern economic regulation, not a reenactment of personal harm.

#### Engine changes wanted

None. All work uses the current kit without edits.

#### Build QA disposition

The single full audit completed within its forty-minute budget. Its original snapshot is retained in Scratch. Focused fixes address Read's width, stable header widths on Sound toggles, ownership ribbon wrapping and paint order, 1280x720 table/chart spacing, narrow regulator labels, Finish focus, and an explicit textarea accessible name. Active mode taps now preserve speech. Short memo results retain the privacy line. The hosted phone checks use drive.py because the audit's iframe context probe failed; this remains a documented audit coverage gap, not a claim that the automatic phone pass was clean.

The system python command is a LibreOffice launcher. It left native background host children after parent shutdown. Cleanup queried normal command-line metadata, matched only drive.py the-buyout --host 8785, and closed those ten children. Other processes were excluded. host-cleanup.json and final-manifest.json record this. Earlier host contention is a plausible cause of the audit's automatic iframe failure. All three used ports were verified closed at completion. Future host helpers should launch the native Python executable directly and keep its process handle.

The user required stopping immediately after the final codex-report.md write. A working report draft was kept in Scratch during checks, then placed in the tool folder only at completion. This takes precedence over the build brief's early-report-file timing.

#### Next handoff

Cold review evidence and remaining limits are in codex-review.md. No commits were made. The tool remains stage built for the separate blind Refine lenses.

#### Cold review repairs

The cold reviewer played both runs, Compare, all remedies and the memo before reading this handoff or the source. Review evidence uses the review-prefixed files, cold-frames, size-before, cheat-before, cheat-after and post-frames in Scratch. The final review report supersedes the build's outstanding findings.

- Memo length now excludes isolated alphabet letters except a and I, closing a twelve-letter padding bypass. The check still explicitly evaluates structure, not prose quality.
- Combined model launches have one fixed announcement per quarter, including both firms when they share a launch. All combinations live in L and voice/lines.json. This retains every factual event at a two-second tap pace without holding up play.
- Switch results interrupt obsolete how-to speech and then offer the marking how-to while it is relevant. The result tracks visualize retained buyers, rival switching and going without. Motion off removes the reveal and retains the figures.
- HHI feedback identifies the equal-share starting point for the 7,500-point example. The BT card distinguishes Littlechild's proposed RPI-X from the government's later choice of three percentage points.
- End-of-Buyout hints name Rivals or Compare. If research reaches its maximum under keyboard focus, focus moves to Next quarter with preventScroll.
- Read's fixed hints now belong to L and the voice inventory. Compare names only enabled Finish buttons and directs students to Regulator after three marks. Its 375px layout keeps all five buyer rows in view after the Switch result.
- At short landscape heights, Memo uses one navigation row with a Remedies return button. Duplicate Evidence instructions are omitted because the hint already says them. This keeps the maximum eight chips and privacy line visible; focus moves off a hidden panel tab to the current memo leaf.
- Redrew remedy-standard with the built-in image tool. Its three matching USB-C ports and one cable connector now face the viewer at card size. Prompt/provenance are in art/prompts.json; the prior raw image is preserved only in Scratch.
- Final audit completed inside forty minutes, with eleven leads. Eight load-focus notices follow the explicit spec; two missing welcomes follow BASELINE rule 16. The confirmed 375px ownership overlap is repaired by giving Buyout's shelf thirty-two more pixels and separating the products from its banner. No full audit was repeated.
- Final focused craft repairs preserve speech on repeated active memo tabs/leaves, use solid/dotted/dashed chart patterns, and keep evidence/marking how-to lines consistent with completed prerequisites. Evidence with Compare chips but no first remedy now directs the student to Reasons.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
