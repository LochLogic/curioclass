# Codex review: trade-island

## Played

Cold play as a Grade 12 student before reading builder notes/source: Alone, trade, Storm, Cost, Policy, evidence and Case. Best moment: changing work and trade to lift both islands above their best-alone baskets. The harbor is strong. The two flat spots were the generic win banner, now made specific to this deal, and the deliberate writing pause, retained for Grade 12 reasoning. I would return to test the Storm and factory-policy tradeoffs, rather than repeat the same winning deal.

## Findings fixed

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

## Findings left

No blocker or should-fix finding left. Case checks evidence structure, not semantic truth; naming relevant evidence does not establish a sound economic argument. This limit is explicit on screen and remains the spec's design.

## Break it

Independent Python and actual bundled JavaScript enumerate all 181,800 nonzero split/deal combinations in each trade season: 597, 0, 1,931 mutual gains. No win at the alone split or by sending cloth.
Zero offers, one-way gifts, maximum amounts, unavailable supply, uncovered accepted deals and unchanged alone splits fail to earn the banner. Exploration of prediction, cost feedback and best-alone marker intentionally has no score or saved mastery.
Case: one island, no gain/loss, money-only evidence, inactive-policy pins, empty/14-word/repeated/alphabet input fail. An unrelated fifteen-word list passed before the fix and now fails. All 27 final browser assertions pass, including frozen baseline-pin rejection, five-pin ceiling and stopped uncovered cargo. A complete evidence-based case still passes.
Save rechecks after edits; it cannot retain a prior passing result for shortened writing.
BUILD wave lessons checked independently: next-action hints/Read and mode changes; held-click how/result rules; stable focus and no load focus; 44px targets/visible choices; all eight sizes; no scored giveaway; explicit token/model/money assumptions; student manipulation of the stated concepts; no family engine; Motion off; resize mid-animation; unknown/not-offered/unchanged states; distinct legend meanings; truthful badges and reversible hints. Cost and prediction feedback are exploration, not mastery scores; copying either cannot earn mutual gains or pass Case.

## Voice walk

Continuous native-input main walk, held 120 ms clicks at 2 s pace, default Sound setting: harbor, prediction No, slider to best-alone 60, Season 2, slider to 90, typed 150/100, Offer, Cost 2/1/Wren, Policy tariff, four evidence pins, Case, typed argument, Check and Save.
Heard in order: wIslands, openStrait, wrenReply, bothBetter, predictNo, costCard, costResult, wPolicy, wCase, caseResult (pass), caseResult (pass on Save). Each how-to began once. Long welcomes/Cost were cut when their state was left or answers changed; no stale result stayed queued. Zero console errors. Full evidence: review-voice-main.json.
Repeated after the final voice guard: same order, zero console errors, all spoken lines in the 792-line inventory. Side checks: five Offers = five Wren events; five Cost checks = five results; five Case checks = five results; five Cost openings = one how-to. Read works with Sound off. Editing while Read plays leaves result speech queued behind Read. Native Tab/Arrow Right/Page Up reaches the slider and changes 50 to 61.

## Facts checked

- Fictional 100-worker production, basket recipe, opportunity costs, best-alone maxima, trade outcomes, policy prices/jobs/reef and move rule: spec Content, independent recompute.py/recomputed.json. All 72 policy scenarios agree to 1e-8 across prices/profit/rows/jobs/reef/location; review-policy-parity.json.
- Ricardo example and 1817 publication: Ricardo, Principles, chapter 7 at https://www.econlib.org/library/Ricardo/ricP.html?chapter_num=8 . Illustrative, not measured national data.
- Absolute/comparative advantage and mutual gains: [OpenStax Microeconomics 3e 19.1](https://openstax.org/books/principles-microeconomics-3e/pages/19-1-absolute-and-comparative-advantage) and [19.2](https://openstax.org/books/principles-microeconomics-3e/pages/19-2-what-happens-when-a-country-has-an-absolute-advantage-in-all-goods). Equal-cost Storm independently has zero winning deals.
- Tariff buyers/producers/treasury effects: [OpenStax 20.1](https://openstax.org/books/principles-microeconomics-3e/pages/20-1-protectionism-an-indirect-subsidy-from-consumers-to-producers); market-power basis: [Broda/Limao/Weinstein, AER 98(5), 2008](https://www.aeaweb.org/articles?id=10.1257/aer.98.5.2032). Here tariff 0.5 yields Pell +5.8656, Wren -6.4048, combined -0.5392, independently recomputed; no universal benefit claim.
- Washers 2018, nearly 12%, dryers, approximately 1,800 jobs and annual cost above $800,000/job: [AEA, The spillover effects of trade wars, 31 July 2020](https://www.aeaweb.org/research/washing-machines-2018-tariffs-effect), Flaaen/Hortacsu/Tintelnot.
- Cambodia 1999, annual 6% quota growth and initial potential 14% bonus: [USTR, 7 January 2002](https://ustr.gov/archive/Document_Library/Press_Releases/2002/January/US-Cambodian_Textile_Agreement_Links_Increasing_Trade_with_Improving_Workers%27_Rights.html); renewal raised that ceiling to 18%. [ILO, 26 October 2005](https://www.ilo.org/resource/article/new-trade-regime-textiles-and-clothing-how-cambodian-factories-improved) confirms 1999 foundation, monitoring and public reports.
- Swiss cap 1.20/euro, 2011 to 15 January 2015, appreciation: [SNB release](https://www.snb.ch/en/publications/communication/press-releases/2015/pre_20150115) and [CRS IN10230](https://www.everycrsreport.com/reports/IN10230.html). Exporter shares fell: [Reuters, Atul Prakash, 15 January 2015](https://uk.investing.com/news/stock-market-news/currency-market-furore-wipes-%24100-billion-off-swiss-stocks-29387), names Swatch, Richemont and ABB losses.
- Textile wastewater: [UNEP Global Stocktaking (2020)](https://wedocs.unep.org/handle/20.500.11822/34184); exact reef index and labor regimes are fictional assumptions, never country measurements.

## Sensitivity

Nine people:true adults inspected with practical tools and varied skin tones, ages, genders and builds. Cultural reviewer should consider the stone/timber town contrast and fictional weak labor rules beside the Cambodia example. No equation identifies Wren as Cambodia; preserve the fictional-comparison reminder. People have equal agency; no religious/Indigenous identity is asserted.

## Flattest moment left

The deliberate writing pause, with this student's frozen evidence visible. No timer, confetti or new topic added.

## Graphics

Inspected all 22 assets, portraits at 48x64 and objects in the tool; no missing art tokens. One storm redraw. Prompt/provenance in art/prompts.json; raw in art/raw/storm.png; old raw retained in Scratch. Built-in imagegen, then the mandated art.py rekey using existing scientific packages.
Inspected all seven landscape/tall sizes after art/payoff fixes, 375x812 through host 8755, grayscale, Cost feedback and five-pin saved Case. Rechecked compact banner/sign separation at 680 and 760. Rich harbor remains at least as substantial as the existing Snowy Mail Route and Beat Lab frames opened read-only. Opened the side-by-side review-finish-comparison.png: the reviewed winning scene beside Beat Lab. Art 525.6 KiB; final bundle 1,234.4 KiB; no missing tokens. Brand/panel 9.23:1, sand/panel 9.67:1, outline/panel 5.78:1, sign ink/paper 14.58:1.

## Audit

Single run completed in 36.9 minutes within the 2,400-second cap, Chrome 9951 and host 8755. All 49 audit PNGs opened individually. Eight sizes, all modes/states, Motion off, 44 single-control tests, ten five-click, ten quick-tap and full mid-action resize stress completed. No runtime errors, lost settled focus or stuck controls.
All ten leads dispositioned: empty-Case clipping fixed; false substring plural in 26.1 shells retained; six skipped first welcomes permitted by BASELINE16, with hints/Read preserving the task and no late welcome; two source links correctly open another tab. audit.md remains the original evidence.
Post-audit scope was limited to confirmed clipping and the compact token key, Growth description and uncovered cargo issues already found. All nine repair PNGs opened; empty feedback bottom is 396.7px within 425px, phone legend visible, steady/swing descriptions correct and uncovered boat stopped. All 27 final adversarial checks pass. No second audit or review round.

## Left open

No questions asked in this unattended session. Followed explicit model equations, STANDARDS no-load-focus, 22 enumerated art assets, and browser speech fallback as the briefs lean. Exact wise-mentor timbre needs production recordings, outside this no-recording review.
Initial short document reads lacked a process watchdog; subsequent commands use explicit watchdog/subprocess timeouts. A custom native-input walk's first connection timed out; its bounded retry and final rerun completed successfully.
No git operations, commits or shared-file edits. The temporary host file is removed; netstat confirms no entries on owned ports 9950, 9951 or 8755. Process inventory was denied, so no unrelated processes were touched. Working report stayed in Scratch until the final write, honoring the user's stop condition.
