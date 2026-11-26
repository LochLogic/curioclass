# Trade Island: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: trade-island

#### Built

Built Islands, Policy and Case as one offline HTML file, using the kit starter, theme-912, Curio.voice and kit sound/motion controls. All 22 listed images were newly generated, processed through art.py --rekey and placed. Nine are people:true. The independent sensitivity review passed; its fictional-islands reminder is implemented beside historical cards.

The worker model remains live during the 1.2-second boat crossing. Seasons retain their own workers, offers and cost answers. Policy analytically clears both markets and settles the factory choice. Evidence freezes its values and active policy at pin time. Save checks again and stores only on this device. No commits, shared-file edits, recording, deployment or polish round.

#### Numbers check

- Before implementation, independent Python enumerated 181,800 nonzero split/deal combinations per season: S2 597 both-better, Storm 0, Motor boats 1,931. No Send cloth successes; no success at each season's best-alone split. S2 minimum 66 fishers. Accepted successful prices: 1.0714 to 1.9167 in S2; 1.0714 to 2.9 with motors.
- Best-alone maxima: Pell 120 at 60 fishers, Storm 75 at 75, motors 150 at 50; Wren 50 at 75. Reference 90/150/100 gives Pell 390 fish, 130 cloth, 130 baskets; Wren 18 fishers, 186 fish, 64 cloth, 62 baskets. Same deal at 60 leaves Pell 70.
- 294 JavaScript checks PASS, including exhaustive banners, 72 allowed lever settings, all nine factory-move rows and independent Python parity for nine reference policies. Cloth imports stay above seven; neither supply curve's zero floor binds in the allowed domain.
- Half tariff: Pell +5.8656, Wren -6.4048, combined -0.5392. Full tariff combined -10.7843. Moved Basic/Loose factory: Wren reef 81.8501, shown 82. All reference rows, jobs, reefs and currency outputs match the spec's rounding.
- Contrast recomputed: brand/panel 9.23, brand/paper 10.02, brand-ink/brand 9.37, sand/panel 9.67, cloth/panel 8.44, Alone/panel 5.78, sign ink/paper 14.58. See source-arithmetic.json, numbers.json and model-test-results.json in Scratch.
- Spec discrepancies: 21 images is a count error; 22 are enumerated. Its default 300 fish/100 baskets applies only to Seasons 1 and 2, not changed production rates. The 50-fisher default produces 100 baskets below the 120 best-alone outline, contradicting the sentence that doing nothing leaves both bars on outlines. Used the explicit rates, split and best-alone rules; spec untouched.

#### Facts checked

- All per-worker outputs, 100-worker totals, three-fish/one-cloth baskets, prices, jobs, wages, rights, reef indices and money changes: fictional teaching assumptions in spec.md Content; recomputed independently. The screen and notes identify the model. Policy is a separate economy from Islands, not an unexplained reuse of its workers.
- Absolute versus comparative advantage, gains with differing opportunity costs and no strict mutual gain when costs match: [OpenStax Economics 3e 33.1](https://openstax.org/books/principles-economics-3e/pages/33-1-absolute-and-comparative-advantage) and 33.2; Ricardo, Principles, chapter 7. Portugal 90/80 versus England 100/120 yields cloth opportunity costs 1.125 versus 0.8333 wine. The on-screen Ricardo account uses the specified cloth/wine directions and 1817 publication date.
- Tariffs transfer from buyers toward protected producers and the treasury; a large buyer can gain at its partner's expense while combined welfare falls: OpenStax [34.1](https://openstax.org/books/principles-economics-3e/pages/34-1-protectionism-an-indirect-subsidy-from-consumers-to-producers), Krugman/Obstfeld/Melitz chapter 9, plus the explicit model calculation. The spec's OpenStax 19/20 numbering belongs to Microeconomics 3e, not Economics 3e; links and metadata corrected to 33/34.
- Washer card: 2018, nearly 12%, similar dryer increases, approximately 1,800 jobs, annual consumer cost above $800,000 per job. Verified [AEA research highlight](https://www.aeaweb.org/research/washing-machines-2018-tariffs-effect), 31 July 2020, and Flaaen/Hortacsu/Tintelnot AER 110(7), 2020. The cited $815,000 exceeds the displayed lower bound. Not a claim about all tariffs.
- Cambodia card: 1999 agreement, normal annual quota growth 6%, initial possible bonus up to 14%; [USTR, 7 January 2002](https://ustr.gov/archive/Document_Library/Press_Releases/2002/January/US-Cambodian_Textile_Agreement_Links_Increasing_Trade_with_Improving_Workers%27_Rights.html) distinguishes that initial cap from the renewal's 18%. [ILO, 26 October 2005](https://www.ilo.org/resource/article/new-trade-regime-textiles-and-clothing-how-cambodian-factories-improved) confirms the 1999 foundation, inspections and public findings. No disputed monitoring start year or actual annual bonus is stated.
- Swiss card: cap 1.20 francs per euro from 2011, removed 15 January 2015, franc appreciation and exporter share losses: CRS IN10230, 11 February 2015. CRS text was available via its [EveryCRSReport reproduction](https://www.everycrsreport.com/reports/IN10230.html); the congress.gov route could not be fetched by the research tool. The source link remains CRS. Stronger-currency model distribution follows the supplied market equations and OpenStax exchange-rate treatment.
- Murky water as an environmental cost of loose textile-wastewater controls: UNEP, [Sustainability and Circularity in the Textile Value Chain, 2020](https://wedocs.unep.org/handle/20.500.11822/34184). Exact reef scores and the fictional labor regimes are model assumptions, not measured country facts.

#### Break it

- Both-better banner: tried zero/zero, one-way gifts, all fish with 300 for 200, sending more than production, holding the alone split, Send cloth, sweeping every nonzero deal and every worker split. No false banner. Trial exploration is allowed; no score or saved mastery is awarded. Storm has no successful combination.
- Accepted deal: changed workers during crossing, then made the deal unaffordable. The control acted at once and consumption reverted to no trade with the cover warning. Changing an amount invalidates immediately, including while typing. Repeated Offers replace pending replies and keep controls live.
- Cost card: wrong numbers reveal the calculation; choosing Pell gives the absolute/comparative distinction. Cycling is intentionally unscored instruction. Wren is fixed at one from Storm onward. No successful price interval or opportunity-cost answer appears before Check.
- Predict and best-alone marker: guessing and sweeping are allowed exploration; neither records a score. The first real banner reveals the prediction and Ricardo account. A rendering-order defect that delayed that footer until another action was fixed.
- Policy totals/factory choice: all lever combinations recomputed; no direct Move button can force an unprofitable move. Currency moves suppress both Growth totals. The table and pins use unrounded changes; displayed rounding does not decide movement.
- Case: empty pins, one island, no gain, no loss, money-only pins, pins taken with policy off, wrong-policy pins, six pins, empty writing and exactly 14 words all fail. A complete case passes for either stance. Alphabet and repeated-word padding fail. This is explicitly a structure check, not a judgment of economic reasoning.
- Save: editing invalidates Check. Save rechecks the current sentence and evidence, refusing a shortened sentence after a previous pass. Stored evidence and text stay local; storage failures are caught. 27 integrated UI assertions passed at each of 1366x768 and 680x425, in addition to the pure model checks.

#### Voice walk

Default sound settings, real held presses of 120 ms at a two-second pace; setup fields were prepared through input/change events. Native keyboard Tab reached the slider, Arrow Right and Page Up changed 50 to 61. Main started in order: wIslands, openStrait, Wren's reply, bothBetter, predictNo, costCard, wPolicy, wCase, casePass. Each mode how-to started once.

Five Cost card openings produced one spoken costCard and subsequent silent heard entries. Wren's reply preceded bothBetter, which preceded the prediction reveal. A newer Offer invalidates older queued replies. Side path: Storm losing deal, Wren reply, stormNone, Read, Motion off. Read used the current Offer hint. No runtime errors. Logs: voice-walk.json; side frame: voice-side.png.

Some long speech was cut when its screen was left: the initial welcome, prediction reveal, first Cost card how-to and Policy welcome. Their starts are recorded honestly; no claim that a two-second tap lets every long sentence finish. The first-tap rule permits welcome cuts, hints remain available, and Read speaks the current task. No clips recorded, as required; exact wise-mentor timbre awaits later production.

#### Feel check

Played all four seasons, losing and winning deals, the Cost card, tariff/currency/factory combinations, evidence pinning, both stances, failed checks and a saved case. Best moment: Pell produces less cloth, a cargo boat crosses, and both basket bars exceed the best-alone outlines while the production chart still shows Pell's absolute advantage.

Two flattest moments addressed during Build: tariff and currency initially felt like table-number changes, so the strip now shows shrinking or growing cargo markers and coins accumulating in the treasury; the checked Cost card felt detached from the islands, so its computed costs now remain in the island footer. The writing pause remains deliberate, with this student's frozen evidence as the payoff.

The sunny, detailed harbor, boats and working adults hold up beside Snowy Mail Route's clear cause/effect scene and Beat Lab's substantial working surface. The tool is not plainer than the bar scene. Compact frames trade detail for controls, and still show both islands and the consequence bars.

![Trade Island beside the Snowy Mail Route finish bar](../../_scratch/trade-island/feel-comparison.png)

#### Done when

1. PASS: load is Islands/Alone; scene and bars dominate; worker movements and bars respond immediately; 60 fishers produces 120. See best-alone-1366 and keyboard log.
2. PASS: 90 fishers, Send fish 150, Get cloth 100 accepts with Wren 18; Pell 130/Wren 62; banner visible. Independent model and integrated UI agree.
3. PASS: same deal at 60 gives Pell 70/no banner; exhaustive Storm search has zero banners.
4. PASS: S2 2/1/Wren; Storm 1/1/Neither; Pell choice explains absolute versus comparative advantage. Integrated checks and Cost card frames.
5. PASS: slider changes and repeated Offers act during the crossing. No JS animation lock; resize uses persistent DOM.
6. PASS: all policy reference outputs match, including currency treatment and suppressed totals. Python parity, 294 checks and integrated UI.
7. PASS: Basic/Loose moves with reef82; Strong/Strict stays with the line; tariff1 keeps the factory home. Tests and moved/stayed states.
8. PASS: case gates reject each listed omission and 14 words; full case passes. Save rechecks. Pure and integrated evidence above.
9. PASS: all eight required sizes and all modes inspected, including the 375x812 iframe on host8795. Audit findings received focused repairs and follow-up frames. Compact historical cards use a separate page; all evidence choices remain available.
10. PASS: each how-to starts once over five repeated actions; Wren reply precedes bothBetter. Held-click logs above.

#### Wave lessons

- Hint and voice: PASS. Hint changes immediately by mode/page, Read uses it, no disabled control is named; helper owns the heard set and queue.
- Focus and layout: PASS. No load focus, persistent sliders/buttons/pins, intentional focus uses preventScroll; mode switches from panel controls move focus to the mode tab.
- Sizes/targets: PASS after focused audit repairs. Targets are 44px minimum, with compact Cost inputs side by side and whole evidence chips as removal buttons.
- No giveaways: PASS. No best-price range or answer badge; exhaustive banner checks; cost/predict exploration unscored; case check states its limits.
- Honest numbers: PASS. Best-alone outlines, exact versus rounded tokens, whole baskets, own-money group changes, separate Policy model and non-additive currency totals are explicit.
- Standards: PASS. Comparative advantage is enacted through costs/splits/deals; distribution is enacted through all five policy measures, group evidence and the written case.
- Motion off: PASS. getAnimations returned an empty list; timing-free controls and model behavior remain live.
- Short choices: PASS. No choice list scrolls off a short panel; compact Cost is paged, Policy pages by island, and its card selector preserves all five measures.
- Resize mid-animation: PASS in the full audit. CSS boat state never destroys a node or disables a control.
- Deferred welcome: PASS. No welcomeAfter; first action is immediate and stale welcomes drop without being marked heard.
- Unknown as unknown: PASS. Unoffered and declined deals stay visibly unoffered/No deal; consumption never includes an unaccepted trade.
- One look/one meaning: PASS. Outline bars are best alone, filled bars are Now; both include numbers and more/fewer/same words, readable in grayscale.
- True badge: PASS. Banner requires strict improvement for both and an affordable accepted deal; no Storm banner exists.
- Hints change back: PASS. Season1 never names Offer; returning from Cost restores the current season task; empty Case directs to Policy.
- No copying answers: PASS. The cost task requires division and comparison; wrong checks teach the work rather than awarding a hidden answer score.

#### Audit leads

Completed once within the 2400-second limit on Chrome9991 and host8795. All 43 audit frames inspected. No runtime errors or warnings, lost settled focus, or stuck controls. All 44 single-control tests, ten five-click tests, ten quick-tap tests and resize stress completed. The audit reports 27 leads; dispositions follow.

- Fixed six production/season-label overlaps: Alone at 680, 800, 760 and accepted, Cost, extreme states at 680. Moved the compact production band up and reduced its padding. Follow-up bounds show zero intersection at all three compact widths.
- Fixed three Treasury/footer collisions at 680: Policy, moved factory and Policy historical page share the repaired layout. Moved the teaching-model footnote to the right panel, removed extra hint padding, and preserved full 44px Pin targets.
- Fixed six phone Policy pin-fold leads by arranging the five levers in a compact two-column desk before the ledger and paging the historical card. Follow-up phone-policy shows all six Pell pins.
- Fixed the unnamed textarea lead with an explicit aria-label, supplementing its existing native label. Verified the exact accessible-name text in the five-pin Case.
- Fixed two phone Case return-control leads by placing Pin evidence and Real case before the sheet. Five pins, valid writing and check feedback remain available below them.
- False plural lead: the audit matched the substring "1 shells" inside "26.1 shells". The full decimal quantity correctly uses plural; retained.
- Six first-action welcome leads: seasons2/3/4, worker minus/plus and Cost card. Those actions immediately change the lesson state or speak their own how-to. BASELINE16 permits cutting an outdated welcome; no delayed welcome is queued. The persistent hint names the current task.
- Two AEA source-link nothing-changed leads: each target=_blank opens the cited source in a separate tab. The tool's own page correctly stays unchanged; no automatic network request.

Beyond the audit's how-to tests, five held Offers, five Cost checks and five Case checks were verified at two-second intervals. Every result event spoke; Wren replies preceded bothBetter and the prediction. Sound-off recovery passed: reopening sound on Cost speaks costCard rather than the hidden worker task; a Storm offer made in silence does not consume stormNone. A newly exposed Alone Cost fold issue was fixed by hiding its prediction card while Cost is open and putting both phone inputs on one row. The original accepted-state drag fixture incorrectly returned a nested IIFE; corrected its body and verified a real 25-point drag from 50 to 90 fishers with an accepted winning deal. Only affected states were re-shot after fixes; no second full audit.

#### Frames looked at

Inspected the 22-asset contact sheet at final sizes, both bar-tool frames, four smoke frames, five focused frames, the voice side path, all 12 final Islands frames, all 12 final Policy/extreme frames and the four original hosted phone frames. Also inspected all ten post/ repairs, four extra/ frames, all 43 audit frames and all eleven audit-fixes/ frames. Inspected the diagnostic footer frame, three final footer/sound frames, two final Alone Cost frames and all affected phone frames, including Alone and Storm Cost. Final bounds and sound results are documented in final-verification.json. The comparison frame was opened and inspected.

#### Art made

22 new images, including nine people. Final WebP art 527.5 KiB; recorded voice 0 KiB; final bundle 1,232.0 KiB, below 2 MiB. No image was dropped for size. No redraw was necessary after cutout review. Raw images, prompts and OpenAI provenance retained; contact sheet on magenta checks key edges.

#### Art still to paint

None. Minor green fringes remain on a few cutout edges at enlarged inspection size; unobtrusive at token and portrait sizes. Fresh sensitivity review passed all nine adults.

#### Engine changes wanted

None. The audit/driver's narrow-host and key support limitations, if encountered, are documented rather than changing shared scripts.

#### Left open

- Exact wise-mentor timbre is unavailable without recordings; the brief prohibits recording. Browser fallback works through Curio.voice.
- Automatic checks establish structure and arithmetic, not the quality of a student's argument. The screen says so; both stances are permitted.
- Build follows STANDARDS' no-load-focus rule despite the spec's load-focus request. All spec questions/conflicts and responsive choices are recorded in handoff.md.
- Initial brief/standards/memory reads used the execution wait budget rather than a process watchdog. All subsequent commands used explicit termination limits. One broad read timed out and was replaced by scoped reads; no repeated long command was left running.
- Bar bundles were opened read-only. Rebundling the two other tool folders would violate the user's write boundary, so their existing bundles supplied the visual bar.
- The mechanical audit describes its pre-fix build. Focused evidence records each repair; the full audit was not repeated, as instructed.
- A five-pin phone Case has a short vertical scroll for its final privacy/structure notes; Check, Save and both return controls fit. Opening Real case puts the comparison first; closing it restores the sheet. Desktop modes do not require page scrolling.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: trade-island

#### Played

Cold play as a Grade 12 student before reading builder notes/source: Alone, trade, Storm, Cost, Policy, evidence and Case. Best moment: changing work and trade to lift both islands above their best-alone baskets. The harbor is strong. The two flat spots were the generic win banner, now made specific to this deal, and the deliberate writing pause, retained for Grade 12 reasoning. I would return to test the Storm and factory-policy tradeoffs, rather than repeat the same winning deal.

#### Findings fixed

- Blocker, general, Case: arbitrary fifteen-word lists passed and could be saved. Require named references to pinned evidence from Pell and Wren; retain a structure-only check and either stance.
- Should fix, general, narration: invalidating deals/cost answers/case text left old result speech playing. Hush results at those state changes and drop stale factory events.
- Should fix, general, voice inventory: variable Wren replies and Cost results were absent. Enumerate reachable result lines through allLines and synchronize voice/lines.json.
- Should fix, general, compact Case: save success/failure appeared only in a heading hidden at compact sizes. Put status in the visible Save button.
- Should fix, general, art: worker rows overlapped and the background stretched at tall sizes. Space complete figures in perspective and preserve the backdrop aspect.
- Polish, general: show the earned basket increase for each island in the winning banner, with a restrained motion cue; increase desktop bar-number size.
- Should fix, general, storm: conspicuous green key fringe. Redrew storm with built-in imagegen, used magenta key and art.py --rekey.
- Should fix, general, sources: Ricardo chapter link opened chapter 6. Corrected Econlib's preface-offset URL and linked USTR/Reuters beside their historical facts in notes.
- Should fix, general, Policy: 0.486 shells appeared as +0 gain. Preserve decimal precision for small nonzero changes; added a real-input audit state for tariff 0.5 plus shell +10%.
- Should fix, general, historical fact qualifier: washer consumer cost per job was missing its annual period. The card now says annual, matching AEA.
- Should fix, general, compact Islands: the five-workers-per-token key vanished with the footer. Keep it beside the compact legend, including phone.
- Should fix, general, empty Case: feedback extended below 680x425. Defer reference prompts until meaningful writing/pins exist; all seven initial fixes now fit.
- Should fix, general, Policy accessibility: steady Growth incorrectly warned of a currency swing. Describe the steady-money total; retain the warning only during a swing.
- Should fix, general, cargo motion: an uncovered accepted deal could finish its crossing. Stop it immediately when worker edits remove coverage.

#### Findings left

No blocker or should-fix finding left. Case checks evidence structure, not semantic truth; naming relevant evidence does not establish a sound economic argument. This limit is explicit on screen and remains the spec's design.

#### Break it

Independent Python and actual bundled JavaScript enumerate all 181,800 nonzero split/deal combinations in each trade season: 597, 0, 1,931 mutual gains. No win at the alone split or by sending cloth.
Zero offers, one-way gifts, maximum amounts, unavailable supply, uncovered accepted deals and unchanged alone splits fail to earn the banner. Exploration of prediction, cost feedback and best-alone marker intentionally has no score or saved mastery.
Case: one island, no gain/loss, money-only evidence, inactive-policy pins, empty/14-word/repeated/alphabet input fail. An unrelated fifteen-word list passed before the fix and now fails. All 27 final browser assertions pass, including frozen baseline-pin rejection, five-pin ceiling and stopped uncovered cargo. A complete evidence-based case still passes.
Save rechecks after edits; it cannot retain a prior passing result for shortened writing.
BUILD wave lessons checked independently: next-action hints/Read and mode changes; held-click how/result rules; stable focus and no load focus; 44px targets/visible choices; all eight sizes; no scored giveaway; explicit token/model/money assumptions; student manipulation of the stated concepts; no family engine; Motion off; resize mid-animation; unknown/not-offered/unchanged states; distinct legend meanings; truthful badges and reversible hints. Cost and prediction feedback are exploration, not mastery scores; copying either cannot earn mutual gains or pass Case.

#### Voice walk

Continuous native-input main walk, held 120 ms clicks at 2 s pace, default Sound setting: harbor, prediction No, slider to best-alone 60, Season 2, slider to 90, typed 150/100, Offer, Cost 2/1/Wren, Policy tariff, four evidence pins, Case, typed argument, Check and Save.
Heard in order: wIslands, openStrait, wrenReply, bothBetter, predictNo, costCard, costResult, wPolicy, wCase, caseResult (pass), caseResult (pass on Save). Each how-to began once. Long welcomes/Cost were cut when their state was left or answers changed; no stale result stayed queued. Zero console errors. Full evidence: review-voice-main.json.
Repeated after the final voice guard: same order, zero console errors, all spoken lines in the 792-line inventory. Side checks: five Offers = five Wren events; five Cost checks = five results; five Case checks = five results; five Cost openings = one how-to. Read works with Sound off. Editing while Read plays leaves result speech queued behind Read. Native Tab/Arrow Right/Page Up reaches the slider and changes 50 to 61.

#### Facts checked

- Fictional 100-worker production, basket recipe, opportunity costs, best-alone maxima, trade outcomes, policy prices/jobs/reef and move rule: spec Content, independent recompute.py/recomputed.json. All 72 policy scenarios agree to 1e-8 across prices/profit/rows/jobs/reef/location; review-policy-parity.json.
- Ricardo example and 1817 publication: Ricardo, Principles, chapter 7 at https://www.econlib.org/library/Ricardo/ricP.html?chapter_num=8 . Illustrative, not measured national data.
- Absolute/comparative advantage and mutual gains: [OpenStax Microeconomics 3e 19.1](https://openstax.org/books/principles-microeconomics-3e/pages/19-1-absolute-and-comparative-advantage) and [19.2](https://openstax.org/books/principles-microeconomics-3e/pages/19-2-what-happens-when-a-country-has-an-absolute-advantage-in-all-goods). Equal-cost Storm independently has zero winning deals.
- Tariff buyers/producers/treasury effects: [OpenStax 20.1](https://openstax.org/books/principles-microeconomics-3e/pages/20-1-protectionism-an-indirect-subsidy-from-consumers-to-producers); market-power basis: [Broda/Limao/Weinstein, AER 98(5), 2008](https://www.aeaweb.org/articles?id=10.1257/aer.98.5.2032). Here tariff 0.5 yields Pell +5.8656, Wren -6.4048, combined -0.5392, independently recomputed; no universal benefit claim.
- Washers 2018, nearly 12%, dryers, approximately 1,800 jobs and annual cost above $800,000/job: [AEA, The spillover effects of trade wars, 31 July 2020](https://www.aeaweb.org/research/washing-machines-2018-tariffs-effect), Flaaen/Hortacsu/Tintelnot.
- Cambodia 1999, annual 6% quota growth and initial potential 14% bonus: [USTR, 7 January 2002](https://ustr.gov/archive/Document_Library/Press_Releases/2002/January/US-Cambodian_Textile_Agreement_Links_Increasing_Trade_with_Improving_Workers%27_Rights.html); renewal raised that ceiling to 18%. [ILO, 26 October 2005](https://www.ilo.org/resource/article/new-trade-regime-textiles-and-clothing-how-cambodian-factories-improved) confirms 1999 foundation, monitoring and public reports.
- Swiss cap 1.20/euro, 2011 to 15 January 2015, appreciation: [SNB release](https://www.snb.ch/en/publications/communication/press-releases/2015/pre_20150115) and [CRS IN10230](https://www.everycrsreport.com/reports/IN10230.html). Exporter shares fell: [Reuters, Atul Prakash, 15 January 2015](https://uk.investing.com/news/stock-market-news/currency-market-furore-wipes-%24100-billion-off-swiss-stocks-29387), names Swatch, Richemont and ABB losses.
- Textile wastewater: [UNEP Global Stocktaking (2020)](https://wedocs.unep.org/handle/20.500.11822/34184); exact reef index and labor regimes are fictional assumptions, never country measurements.

#### Sensitivity

Nine people:true adults inspected with practical tools and varied skin tones, ages, genders and builds. Cultural reviewer should consider the stone/timber town contrast and fictional weak labor rules beside the Cambodia example. No equation identifies Wren as Cambodia; preserve the fictional-comparison reminder. People have equal agency; no religious/Indigenous identity is asserted.

#### Flattest moment left

The deliberate writing pause, with this student's frozen evidence visible. No timer, confetti or new topic added.

#### Graphics

Inspected all 22 assets, portraits at 48x64 and objects in the tool; no missing art tokens. One storm redraw. Prompt/provenance in art/prompts.json; raw in art/raw/storm.png; old raw retained in Scratch. Built-in imagegen, then the mandated art.py rekey using existing scientific packages.
Inspected all seven landscape/tall sizes after art/payoff fixes, 375x812 through host 8755, grayscale, Cost feedback and five-pin saved Case. Rechecked compact banner/sign separation at 680 and 760. Rich harbor remains at least as substantial as the existing Snowy Mail Route and Beat Lab frames opened read-only. Opened the side-by-side review-finish-comparison.png: the reviewed winning scene beside Beat Lab. Art 525.6 KiB; final bundle 1,234.4 KiB; no missing tokens. Brand/panel 9.23:1, sand/panel 9.67:1, outline/panel 5.78:1, sign ink/paper 14.58:1.

#### Audit

Single run completed in 36.9 minutes within the 2,400-second cap, Chrome 9951 and host 8755. All 49 audit PNGs opened individually. Eight sizes, all modes/states, Motion off, 44 single-control tests, ten five-click, ten quick-tap and full mid-action resize stress completed. No runtime errors, lost settled focus or stuck controls.
All ten leads dispositioned: empty-Case clipping fixed; false substring plural in 26.1 shells retained; six skipped first welcomes permitted by BASELINE16, with hints/Read preserving the task and no late welcome; two source links correctly open another tab. audit.md remains the original evidence.
Post-audit scope was limited to confirmed clipping and the compact token key, Growth description and uncovered cargo issues already found. All nine repair PNGs opened; empty feedback bottom is 396.7px within 425px, phone legend visible, steady/swing descriptions correct and uncovered boat stopped. All 27 final adversarial checks pass. No second audit or review round.

#### Left open

No questions asked in this unattended session. Followed explicit model equations, STANDARDS no-load-focus, 22 enumerated art assets, and browser speech fallback as the briefs lean. Exact wise-mentor timbre needs production recordings, outside this no-recording review.
Initial short document reads lacked a process watchdog; subsequent commands use explicit watchdog/subprocess timeouts. A custom native-input walk's first connection timed out; its bounded retry and final rerun completed successfully.
No git operations, commits or shared-file edits. The temporary host file is removed; netstat confirms no entries on owned ports 9950, 9951 or 8755. Process inventory was denied, so no unrelated processes were touched. Working report stayed in Scratch until the final write, honoring the user's stop condition.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Trade Island build handoff

#### Structure

src.html derives from the kit starter. It has responsive scene and notebook styles, the pure island and policy models, then persistent UI controls and Curio.voice integration. There is no family engine for these models. The offline artifact is trade-island.html; tool.draft.json stays stage built for cold review. Assembly fragments, number checks, frame scripts and evidence live in _scratch/trade-island. Future edits can be made directly in readable src.html.

#### Model details

Wren maximizes exact baskets before comparing whole baskets with 50; ties choose fewer fishers. Pell's consumption only includes an accepted trade it can still cover. Worker changes never block on the boat. Season state is separate. Both-better speech is queued after Wren's reply, then the first prediction reveal.

Policy uses analytic market-clearing solutions for the allowed lever domain. Do not round before surplus, earnings, reef or factory-choice calculations. Factory owners remain Pell residents. A currency swing suppresses both Growth totals. Pins capture their value and active policies at pin time; Save rechecks structure. Passing a structure check does not establish the truth of the argument.

#### Open questions and build decisions

- The sole spec open question requests sensitivity review of the nine people and invented cultures. Keep the islands fictional; make the varied people art, mark every people asset, and leave the independent review with evidence for the cold reviewer.
- The spec says 21 images but enumerates 22. Made all 22, including nine people. The explicit user and CODEX-BUILD art instruction overrides BUILD's older Do not draw art sentence and older Gemini-only wording. Credit OpenAI gpt-image.
- STANDARDS outranks the spec. Retained no focus on load; a prediction moves focus to the worker slider using preventScroll. The spec requests load focus while BUILD's wave lesson prohibits it.
- The spec says doing nothing leaves bars on their outlines, but specifies 50 Pell fishers and best-alone outlines at 60. Used the exact specified default: 100 baskets now against a 120-basket outline. Wren starts on its outline.
- The default's parenthesized 300 fish and 100 baskets only applies to Seasons 1 and 2. Storm and Motor boats use their actual production rates at the specified 50-fisher default.
- Scene tokens round to the nearest five workers, explicitly labeled; all numeric results use the exact slider count. This resolves single-worker increments with five-worker figures.
- The specified desktop table height cannot contain ten separate 44px pin rows plus 64px portraits. Used two island columns, six Pell rows and four Wren rows. Compact sizes page by island and combine each island's five card metrics in a selector and Pin button, keeping the 44px targets.
- Compact Policy has a Real case page with Back to levers, preserving the historical card when the entire desk cannot fit beside it. At 1000px the strip, all cards and both group columns remain visible. Compact Case places the structure-check explanation in the right panel so five evidence pins and the privacy statement fit beside Save.
- The user says stop when codex-report.md is written, so the working report lives in Scratch until the final write. This overrides the early-report-file instruction without sacrificing ongoing records.
- Voice metadata is wise-mentor. The no-recording instruction means browser fallback; the exact bank timbre is not guaranteed.
- The spec cites chapters 19 and 20 of OpenStax Principles of Economics 3e. Those chapter numbers belong to Microeconomics 3e. Verified and linked the same topics in Economics 3e chapters 33 and 34; the spec remains untouched.
- On a 375px phone, Policy puts levers before the evidence ledger to keep the main controls visible. The compact two-column lever desk keeps all six Pell group pins in view at 375x812; its Real case button opens the historical comparison. Phone Case puts its two return controls before the sheet. Cost inputs share a row on compact and phone layouts; the prediction card folds away while Cost is open and returns with its state intact. Longer student writing can scroll vertically. Landscape compact mode retains the desk and ledger side by side.

#### Sensitivity

Nine people images show varied adults with practical clothing and tools. Neither skin tone nor gender determines economic success. No real cultural costume, religion or Indigenous identity is asserted. The left stone town and right timber town are model settings, not cultural rankings. Basic and Strong labor rules are fictional; the Cambodia card describes a historical agreement without mapping Wren to Cambodia. Inspect people for anatomy, stereotypes and equal agency; the contact sheet is _scratch/trade-island/art-sheet.png. A fresh review passed all nine people. Its suggestion is implemented beside historical cards: Historical comparison. Pell and Wren are fictional. Details are in _scratch/trade-island/sensitivity-review.md.

#### Engine changes wanted

None. No shared files changed.

#### Build verification

The single full audit completed, with 27 leads dispositioned in codex-report.md. Arithmetic has 294 pure checks plus 54 integrated UI assertions. Focused audit repairs cover label/footer bounds, phone controls, accessible writing, held-click result speech and real dragging. The full audit was not repeated. Evidence and frame lists stay in Scratch. Sound recovery uses the current Cost page and only marks the Storm explanation heard after an actual spoken event.

#### Next

Read codex-report.md for the completed build checks and remaining limits. No polish round, git commit or deployment belongs to this run.

#### Cold review changes, 2026-11-07

Cold play preceded reading this handoff, the build report, notes and source. Review evidence uses `review-*`, `cold-*`,
`find-frames/` and `post-frames/` in Scratch, leaving build evidence intact. No shared file or git history was changed.

Case now requires explicit Pell and Wren references and a pinned group/measure topic from each. This closes the unrelated
fifteen-word-list pass while preserving the stated structure-only check, both stances and the original pin gates. It does
not judge causation or the truth of the argument. The Save button itself shows success/storage failure at compact sizes.

`clearResults()` stops invalid result speech on deal, Cost and writing edits, while preserving Read. Factory changes drop
queued stale events. `allLines()` enumerates the variable Wren/Cost outcomes for the 792-line production inventory;
it is evaluated for recording/checking, not during normal play. Browser fallback remains; no clips were recorded.

The winning banner now shows each island's basket increase above best alone. Desktop bar numbers are larger. Worker
figures are spaced in perspective and the harbor retains its aspect ratio. The compact banner/sign geometry is checked
separately. All original art is retained except the redrawn storm overlay. Its full prompt is in `art/prompts.json`,
raw in `art/raw/storm.png`, generated with built-in imagegen, then processed by `scripts/art.py --rekey storm`. The
previous raw is preserved in `_scratch/trade-island/storm-before.png`. All nine people assets remain people:true.

The Ricardo source link now opens chapter 7 using Econlib's preface-offset query. Notes link the USTR quota facts and
Reuters exporter-share reporting. The washer card now explicitly labels the consumer cost per job as annual.

Independent review recomputation reproduces 597/0/1,931 winning trade combinations and all 72 policy settings to 1e-8.
See `codex-review.md` for the final single-audit disposition and remaining limits. No new modes or topics were added.

The review audit completed once in 36.9 minutes. Its real empty-Case feedback clipping is repaired by showing the
evidence-reference prompts only after meaningful writing and pins exist. Focused frames confirm the full seven-item
empty-case list at 680x425. Compact Islands now keeps the five-workers-per-token key in view. An uncovered deal stops
an in-flight cargo crossing immediately. Growth's accessible description warns about exchange rates only when they
actually differ from the baseline. All 27 final adversarial assertions pass; all 72 policy scenarios remain in parity.
The nine final repair frames live in `audit-fix-frames/`; the single audit is `review-audit/audit.md`. No second audit ran.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
