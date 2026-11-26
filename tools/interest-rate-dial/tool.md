# Interest Rate Dial: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: interest-rate-dial

#### Built
- Built only in the authorized tool and Scratch folders, from S:\CurioClass-codex.
- Street: 15-detent brass dial, live four-neighbor calculations, fixed-rate signing, both card-payment plans, pin comparisons and open/closed cafe.
- Predict: six specified cases, four editable picks before reveal, single scoring, interruptible sweep, personal six-round recap and shuffled replay.
- Complete offline HTML, readable src.html, built-stage draft metadata, notes, voice manifest, art manifest, audit states and handoff. No commits, deployment or polish round.
- Browser speech fallback is intentional in this Build: no audio was recorded. The manifest selects wise-mentor / Gacrux.

#### Numbers check
- Independently recomputed all nine published rows and all six prediction cases in `verify_math.py`; retained results in `numbers.json`.
- Runtime comparison: zero number failures. Card recurrence reproduces every specified month and cent, including $1,483.44 / 107 months and $240.64 / 18 months at base 6.
- Exact binary nearest-cent rounding with ties to even reproduces the spec's Python reference. Half-up rounding changes a few cents; neither a lookup table nor unexplained constants replace the formulas.
- Verified the 7.0 / 7.5 cafe boundary ($2,200 / $1,950), 3.0 / 8.0 pin ($2,000.00 / $2,566.72), signed-at-7 car payment ($356.42) and base-9 card ($1,784.53 / 113 months).
- Independently recomputed contrast ratios. On paper / white: ink 14.26 / 15.80, muted 5.63 / 6.24, brass 5.71 / 6.33, Abe 5.89 / 6.53, Keisha 5.81 / 6.44, Luis 6.65 / 7.37, Priya 7.08 / 7.85. Focus 5.24 / 5.81. Gold / door 5.83; numerals / door 12.87.
- Spec contradictions are recorded in handoff: 16 named images versus stated 17; older Gemini-only wording versus current Codex permission; 20-35 metadata versus 25-35 suggested segment sum; Luis's balance wording versus a principal-reducing minimum rule.

#### Facts checked
Verified on 2026-11-07. These are model explanations, not current-rate claims or personal advice.
- Higher borrowing rates increase financing costs and can deter expansion: [Federal Reserve Board transcript](https://www.federalreserve.gov/mediacenter/files/why-do-interest-rates-matter-transcript-092016.pdf).
- Compounding earns interest on accumulated interest: [SEC Investor.gov glossary](https://www.investor.gov/introduction-investing/investing-basics/glossary/compound-interest). Abe's monthly addition and 60-month outcome are computed from the specified fictional inputs.
- A fixed car rate stays set when market rates move; variable rates can follow an index, and variable cards are common: [Capital One, fixed versus variable rates](https://www.capitalone.com/learn-grow/money-management/fixed-vs-variable-apr/). No claim that fixed credit-card terms can never change.
- Banks' prime convention is about 3 points above the Fed target's upper bound: [Federal Reserve Board, Jefferson speech](https://www.federalreserve.gov/newsevents/speech/jefferson20250219a.htm). This official source corroborates the spec's bank source.
- A floor or interest-plus-percentage minimum is common; issuers differ: [Chase's current explanation](https://www.chase.com/personal/credit-cards/education/basics/how-to-calculate-your-minimum-credit-card-payment). Its examples include $25/$35 floors and its own $40 or 1%-plus-interest rule. This toy uses $25, no fees, no new charges and monthly rounding.
- Paying the minimum raises time and interest in these cases: the explicit recurrence and the same Chase explanation. No real-card payoff promise is made.
- The historical 14.3-point card margin was above prime, not directly above the Fed rate: [CFPB's 2024 analysis of 2023 data](https://www.consumerfinance.gov/archive/blog/credit-card-interest-rate-margins-at-all-time-high/). The tool labels its own add-ons as made up.
- Names, households, repair, principals, terms, profits and Priya's $2,000 requirement are authored fictional inputs from Content. The footer says so. Priya's annual interest and remainder are computed, including the later principal-repayment assumption in notes.

#### Break it
- Exhaustively ran all 54 pick combinations in each of 6 rounds: 324 scoring cases, zero failures. Empty and three-pick reveals stayed blocked.
- Repeated Turn and post-reveal pick changes could not rescore or alter picks. Only the last pre-reveal pick counts.
- First button everywhere: 10/24. Last button everywhere: 6/24. Always Worse for all three households plus Yes when rates fall: 10/24. A partly informed strategy with car always Same and cafe always Yes: 18/24, still wrong in six cases.
- The conditional "rates up is bad for everyone, down is good" rule gets 11/24 and Abe 0/6. Independently checked all eight Priya heuristics: always Yes 3/6, always No 3/6, Yes when falling 2/6, Street line 3/6, no cushion 3/6, new rate under 10% 2/6, profit at least $7,200 4/6, $1,000 cushion 3/6. All their choices are included in the exhaustive runtime score test.
- Covered cards: neutral poses, starting household figures, hidden shop/sign and blank interest/remainder. Priya's new loan rate is deliberately supplied, as the spec requires. Her $2,000 requirement remains visible in compact layouts.
- Pin stores both plans; switching plans does not manufacture a better comparison. Signing freezes the quoted rate, not the live ladder.
- Real whole-pixel, jittered circular drag reached 10.0. Rapid Next during the sweep reached round 2 with no stale sweep or extra score.
- Found and fixed the cafe narration cap consuming muted or stale events. Test: 8 muted oscillations used zero spoken lines; 4 further paced oscillations with sound on produced exactly 2 cafeNo and 2 cafeYes starts, queue empty.
- Street's bar, moods and cafe verdict are exploratory calculations, with no pass threshold or saved score. Sweeping is the intended experiment.

#### Voice walk
- Held presses: 120 ms. Main and side paths: 2 seconds between taps, Sound on by default; logs captured after settling.
- Main heard: welcomeStreet, signed, cafeNo, welcomePredict, cafeHow, result, nextHow. Result began after the sweep and nextHow after result; queue empty.
- signHow became stale when signing; pinHow became stale on pin/mode change; turnHow became stale when Turn was already tapped. These unstarted lines were dropped, not marked heard.
- Side path: Read interrupted cafeHow and then read the current instruction. Next discarded unstarted result/nextHow. Street Read included the repair origin. No queued line cut Read off.
- Full six-round student walk: 4, 2, 4, 3, 3, 3 = 19/24. Result was heard in rounds 2-6, including three repeated 3-of-4 events; endLine followed the final result. The first result was deliberately skipped by Next while cafeHow was still finishing, permitted by Heard in order.
- No how-to line spoke twice in a path. Runtime allLines and the 31-line manifest match. Browser fallback timbre is a limitation, not a recorded wise-mentor claim.
- Closing tests: three actual Sign actions in five alternating clicks each spoke; double-tapping the selected mode kept one whole welcome; modal closure restored the current hint and focus. Replay cleared totals/picks and produced a permutation of all six cases.

#### Feel check
- Played the full six rounds through real held input, including wrong calls. Best moment: Keisha's car arrives and her signed payment holds while the same turn worsens Luis's cost and closes Priya's second shop.
- Flattest moment 1: number-only rate changes. Added the planned three-pose people, physical needle, small mechanical tones, savings fill, signing stamp, arriving car and large lit/dark shop states.
- Flattest moment 2: compact reveals originally lost their explanation and Priya's cushion. Kept Right/Not quite visible, put full worked reasons and comparison detail under More, and retained "Needs $2,000 left" beside her question.
- Found compact portrait overflow, a clipped phone mode label and selected-hover contrast loss. Fixed the containing geometry, mode width and selected hover style. Added actual-size compact dial numerals.
- [Side-by-side comparison](../../_scratch/interest-rate-dial/feel-comparison.png): signed Street beside Beat Lab, both from 1366x768 frames. Also opened Snowy Mail Route. The painted street, detailed dial and illustrated people meet the visual finish bar; the interaction remains deliberately narrower than a music studio.
- Later cases change signed status, direction, profit and principal. The tool earns its six-round session; replay supplies shuffled practice, not unlimited new scenarios.

#### Done when
1. PASS: all base-6 defaults match, including this month's $25 interest and $40 minimum. Independent/runtime number records and default frames.
2. PASS: 7.0 leaves $2,200 Yes; 7.5 leaves $1,950 No. Lit/dark art, worked math and narration cap checked.
3. PASS: pin at 3 then 8 shows $2,566.72 with $2,000.00 pinned and Abe pleased. `minimum-pinned-high.png`.
4. PASS: signed at base 6, raised to 9: $356.42 fixed, today's 10.0%, card 23%, 113 months, $1,784.53. `signed-nine.png`.
5. PASS: $100 plan at 6 shows 18 months and $240.64. `hundred-hover-fixed.png`.
6. PASS: four-pick gate, all round answers/reasons and end arithmetic checked exhaustively. Actual 19/24 student recap and separate 24/24 run.
7. PASS: no outcome art, future household values or Priya interest/remainder before reveal. Neutral poses and visible input-only loan/profit/rate.
8. PASS: dial and four cards dominate at 1366x768 and 680x425, in both modes. Full-size frames and comparison opened.
9. PASS: new detents interrupt number tweens; real Next during sweep advances cleanly. Resize findings in audit disposition below.
10. PASS: primary controls above fold at laptop/preview sizes; compact ladder behind More; 375 iframe also checked. All measured targets at least 44 px.
11. PASS: real Tab, arrows, Home and End tested; focus stays visible. End then Left gives 9.5; Home gives 3; End gives 10. Icons plus words indicate outcomes.
12. PASS with the explicit skip rule: how-to lines once, repeated event results retained, result before nextHow when not skipped, final result before endLine. Logs name each allowed interruption.

#### Wave lessons
- PASS, Hint and voice: immediate hints, Read of current state, heard-based how-to selection and valid/needs guards. Two-second held walks retained.
- PASS, Focus and layout: stable interactive DOM, no load focus, preventScroll for intentional focus moves, fixed-width controls and reserved hint space.
- PASS, Sizes: all 8 standard shapes in both modes, plus extremes, grayscale and Motion off. Phone hosted on 8795; targets measured at 44 px or larger.
- PASS, No giveaways: pre-reveal concealment and all 324 score cases checked; no pass badge, unlock or stored best score.
- PASS, Honest numbers: invented add-ons and monthly-payment assumptions stated; correct fixed-versus-variable behavior and exact rounding.
- PASS, Standards: solo dial/pin, signing/plan comparison, and cafe arithmetic in six cases teach all three stated codes. No family engine is claimed.
- PASS, Motion off: finite outcome timing kept; idle signal explicitly stopped; audit calm finding addressed below.
- PASS, Short choices: every prediction choice stays visible, never in an inner scroll panel.
- PASS, Resize mid-animation: CSS reflow retains the existing nodes and running state; audit's stress outcome recorded below.
- PASS, First-tap welcome: actions run immediately and may skip welcome; no deferred welcomeAfter pattern.
- PASS, Unknown: neutral figures and concealed outcome art before calling a prediction.
- PASS, One look/one meaning: fixed stamp, dashed future needle, selected button, and Right/Not quite each retain one meaning.
- PASS, Truthful badge: cafe verdict is based on the actual remainder and $2,000 rule; no score or success cue appears early.
- PASS, Reversible hint: mode changes restore the appropriate next action immediately; Street state and Predict picks survive switches.
- PASS, No word matching: a rate direction cannot answer Priya's varied-profit cases; role-specific reasoning is required.

#### Audit leads
- Completed the single full audit on 9991, host 8795, within its 40-minute limit. It reported 60 leads, repeated across states and sizes. No console exceptions, infinite calm animations or resize-stuck controls were found. The original report and frames are retained; the audit was not rerun after the following targeted fixes.
- Fixed every "1 points" occurrence with computed singular/plural wording. Final runtime text shows "base + 1 point".
- Phone dial/readout overlaps in default, Predict, minimum, maximum, signed, pinned, four-pick and reveal states: retained the deliberate brass readout plate over the unused lower dial sector. Added pointer-events:none so it cannot block the slider. Labels remain visible; the closing phone check confirms pointer pass-through. The geometric overlap is intentional.
- Context, More and end-recap keep-region/hidden-text leads: intentional native modal backdrops covering the six background keep regions. Background controls are inert while the dialog owns focus. No choice inside a dialog is covered by the street. Full-size lead frames were inspected.
- Fixed the phone More title box overlapping Close by reserving separate heading width. Final measured heading right 263 px; Close left 274.98 px, no overlap. Close stays visible while details scroll.
- Fixed Start over falling outside the 1280x720 reveal panel with a denser short-laptop sidebar. Final reset bottom 687.67 px is inside panel bottom 697 px. The same density rule covers recap's background panel.
- Pinned-low pinHow and reveal turnHow drops: those instructions were invalidated by the already-completed Pin and Turn inputs. Their valid guards correctly discard stale queued instructions. Current hints and the independent main walk were checked; result then nextHow were heard when Next was not chosen early.
- Fixed pointer focus on the slider with focus({preventScroll:true}) at deliberate pointerdown. Final held-click focus is dial, base 6.5.
- Fixed Sound moving four header controls by reserving button widths. Closing test maximum header movement is 0.45 px. Predict and Reset-to-Street movement in the walk is the expected mode change.
- Missing first-tap welcomes after dial, minus, plus, Sign or Pin: permitted by BASELINE rule 16. Their own action happens immediately; the premise and next action remain in the scene, hint and Read. Sound/Read first taps use the kit's explicit skip rules.
- Five-click Sign finding: the control alternates Sign and Shop again. Added hush on Shop again so an obsolete signed statement stops; all three actual Sign actions in a fresh five-click sequence now start their event line, queue empty. A Shop again action has no signed announcement to repeat.
- Quick mode-tap cuts: fixed redundant mode activation so a second tap on the selected mode does not hush its welcome. Final double-Predict test heard one whole welcome, with no cut. Reset still intentionally hushes speech, as specified; its cut is accepted under the first-tap rule.
- Additional affected-state checks passed: context Escape restores hint/focus; replay shuffles and clears all picks/tallies; More during the last sweep closes before the end card; Escape followed by Enter reopens the recap. Final targeted batches had zero console errors. The outer test-host favicon warning from the earlier size batch was repaired in the harness; the final phone batch was clean.


#### Frames looked at
- All manual drive PNGs were opened: reference, first-layout, finished-art, functional, score test, all 16 standard-size mode frames, seven extremes, two repaired phone frames, voice walks, boundary tests and the student recap.
- First layout shots contained draft placeholders while the art-conversion dependency was installed. Every final named asset is generated, converted and placed; no placeholder remains.
- Audit frame inspection: All 86 audit PNGs inspected in 11 contact sheets, with the phone More and 1280x720 reveal leads opened at full size. All 10 post-audit closing frames and the three final phone frames were also opened individually. The contact-sheet index maps every audit PNG to its sheet.
- Evidence and exact input files stay in `_scratch/interest-rate-dial/`. No screenshots or scratch scripts were placed in the tool folder.

#### Art made
- 16 generated images, 12 people assets. Built-in OpenAI image tool; full prompts and people flags in art/prompts.json; originals in art/raw; finished WebP files in art/.
- 605728 bytes of WebP, approximately 592 KB. Recorded voice: 0 KB. 1043427-byte bundle, approximately 1019 KB, under the 2 MB goal. Budget announced: 850 KB art, 0 KB recorded voice.
- No redraw was needed. Pleased/worried poses used each neutral image as an identity reference. Finished images inspected at display size; keying used art.py --rekey only.
- Fresh mandated people review: PASS, all 12 poses. No stereotyped carelessness, mocking expressions, anatomy or framing issue identified. Contact sheets and reviewer record retained in Scratch. Owner contact-sheet review remains a shipping step, outside Build.

#### Art still to paint
None from the named list. The spec's arithmetic says 17; only 16 assets are named and all 16 are present.

#### Engine changes wanted
None. Shared kit, docs, scripts and other tools were not edited. The Scratch key-driver extension only adds Home/End to the existing driver's input map.

#### Left open
- No recorded narration, by explicit build instruction. Browser fallback works; the selected bank voice awaits a later authorized recording phase.
- Owner's contact-sheet review and a cold tool review are later steps. Nothing was published.
- Workflow exception: initial read-only workspace and instruction probes used the execution tool's ordinary wait rather than a hard process deadline. They returned immediately. Subsequent build, art-conversion, drive, audit and helper commands used explicit process timeouts.
- One low-level keyboard probe reached its 120-second limit. A smaller retry using the stock driver with Home/End support passed; nothing remains blocked by that probe.
- Final bundle SHA-256: 017ad0e2385c9bf4a6fd64426cd5479178389055433bf8158347a325c629796f.
- All owned Chrome and host processes were closed after their batches. host.html was removed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: interest-rate-dial

#### Played

Cold as a grade 7 student, then as a projecting teacher: Street, all six Predict cases, wrong calls, replay, compact screens and voice. The signed car versus changing card debt is the strongest moment. Played before reading builder material.

#### Findings fixed

- **Blocker, general, recap:** assumed Keisha signed although the final case is unsigned. Replaced with a question about how signing changes her situation.
- **Should fix, general, final reveal:** recap hid the worked answers after 1.2 seconds. Existing See your recap now opens it on request; result, recap instruction and end narration follow their screens.
- **Should fix, general, More:** included a hidden fixed-payment claim while Keisha was unsigned. Explicitly hidden rows stay out of the summary.
- **Should fix, general, motion:** Motion off during the 1.2-second sweep left its animation frame alive. Cancel the frame and retain the timing; verified the needle holds its exact endpoint.
- **Should fix, general, hint ownership:** a late dialog-close callback could restore Street's hint after entering Predict. Restoration checks mode, round and phase; Read is hushed when closing its dialog.
- **Should fix, general, cafe voice:** reversing the verdict left the old cafe announcement speaking over its opposite sign. Stop that obsolete event on reversal; the replacement must match the current verdict.
- **Should fix, general, facts:** prime comparison now names the upper bound of the Fed target range. Monthly card assumptions, no fees/new charges, and Priya's later principal repayment are explicit on screen.
- **Should fix, general, laptop:** reveal sidebar could clip Start over at 1366. Applied the existing denser sidebar through 850 px height.
- **Polish, general:** wrong calls retain the chosen answer beside the actual outcome; brass outlines mark revealed cards. Ladder says Start to result after revealing. Footer states Motion storage stays on this device.
- **Polish, general, art:** the two cafes changed geometry and had magenta edges. Redrew both against green with the same facade and lighting direction; closed windows are papered and furniture stacked. Preserved the painted street, all people and the detailed brass dial.

#### Findings left

- No confirmed blocker or should-fix knowingly left open. Recorded wise-mentor audio remains a later phase; browser speech is the authorized fallback.

#### Break it

- Four-pick gate: empty and three-pick Turn attempts leave picks/score unchanged. Post-reveal changes, repeated Turn and Street/Predict switching cannot alter or duplicate a score.
- Entire six-round actual input runs: first position everywhere 10/24; last position after mashing all options 6/24; rates-up-bad-for-everyone 11/24. None earns a perfect recap.
- Priya cheats with the other three correctly reasoned: always Yes 3/6; always No 3/6; Yes when falling 2/6; Street's memorized boundary 3/6; forgetting $2,000 3/6; large profit 4/6; new rate below 10% 2/6; $1,000 cushion 3/6. Full tallies are 20-22/24, with specific wrong calls visible.
- Future totals, poses, cafe sign and worked remainder stay concealed before Turn, including More. Future rates are supplied inputs as specified, not answers.
- Fast final recap retains the final result before endLine, even when cafeHow is still speaking. The suspected result-drop issue was falsified by the real held-click log; no change was made there.
- Play again clears all six prior tallies and picks, starts at round 1 with a permutation of the six cases, and scores only the new round. Prior 24/24 cannot carry over.
- Street bar, pin, moods and cafe verdict are computed explorations, not mastery meters. Whole-pixel jittered sweeping reaches both useful extremes without scoring; pin stores both card plans, so toggling plans at a pinned rate remains Same.
- Signed at base 6 then moved to 9: $356.42 stays fixed; card becomes 23%, 113 months, $1,784.53. Minimum/$100 at base 6 remains 107/18 months and $1,483.44/$240.64.
- Cafe narration cap, real keyboard boundaries, final recap arithmetic and targeted regressions: see retained review-event-cap, review-key-boundaries, review-validation and review-regression-final JSON evidence.

#### Voice walk

- Held 120 ms presses, default Sound/Motion, two-second gaps: dial, Sign, further dial changes, Pin, plan comparison, Predict, four calls per round, Turn, Next and recap. The first complete main walk heard cafeNo, signed, welcomePredict, cafeHow, turnHow, result, nextHow, five further results, recapHow, endLine. No duplicated how-to starts.
- First Street welcome can be skipped by a tap on the dial, allowed by BASELINE 16; its premise/control instructions stay in hint and Read. The separate cold Street path heard signHow.
- Read side path interrupts cafeHow, speaks the current hint, survives a mode switch/reset and works with Sound off. No queued line cuts Read. All 32 authored lines match the manifest.
- Repeated the full main path after the cafe fix, plus reversal and fast-recap side paths. Latest main: six scored rounds, five spoken results and one queued result discarded on Next; nextHow/recapHow were also discarded after advancing. These are the spec's explicit Next-before-speech exceptions, not claimed as heard. Reversal stops the obsolete event; the fast final recap still hears result before endLine.

| Line | Kind | Expected | Observed |
|---|---|---|---|
| welcomePredict, cafeHow, turnHow | how/welcome | once each | once in both main walks |
| nextHow, recapHow | how | once unless Next advances first | once each first walk; skipped latest |
| result | event | six queued, Next may discard an unstarted line | six spoken first walk; five spoken plus one discarded latest |
| signed | event | five Sign actions | five |
| endLine | event | open recap | one |

- Combined voice batch hit 300 seconds after saving its paths; retried only the side path successfully. No new audio was recorded.

#### Facts checked

Checked live on 2026-11-07, plus independent arithmetic at all 15 detents and all six specified round decisions.

- Higher rates raise borrowing cost and can restrain expansion: [Federal Reserve Board transcript](https://www.federalreserve.gov/mediacenter/files/why-do-interest-rates-matter-transcript-092016.pdf).
- Banks determine prime; it is a reference rate, not a Fed-set universal household rate: [Federal Reserve FAQ](https://www.federalreserve.gov/faqs/credit_12846.htm).
- Prime convention is the Fed target range's upper bound plus three percentage points: [Federal Reserve, Jefferson speech, 2025](https://www.federalreserve.gov/newsevents/speech/jefferson20250219a.htm).
- Higher savings rates and compounding: [SEC Investor.gov calculator](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator). Independently computed $2,000 at 0%, $2,323.23 at 3% and $2,835.25 at 7%, compounded monthly for 60 months.
- Fixed auto borrowing stays fixed when market rates move; variable card borrowing can follow prime: [Capital One fixed/variable explanation](https://www.capitalone.com/learn-grow/money-management/fixed-vs-variable-apr/).
- Minimum rules differ; floor versus percentage-plus-interest and slower payoff: [Chase education](https://www.chase.com/personal/credit-cards/education/basics/how-to-calculate-your-minimum-credit-card-payment). This fictional model's $25 floor is not Chase's $40 rule.
- Actual card interest is often daily: [CFPB guidance](https://www.consumerfinance.gov/ask-cfpb/how-does-my-credit-card-company-calculate-the-amount-of-interest-i-owe-en-51/). Tool and notes now distinguish the monthly model.
- Historical 14.3-point margin was above prime in 2023: [CFPB analysis](https://www.consumerfinance.gov/archive/blog/credit-card-interest-rate-margins-at-all-time-high/). The tool's plus-14 remains explicitly fictional, not a current-rate claim.
- Fictional people, amounts, add-ons and Priya's $2,000 rule: spec Content. Annual loan times rate and earnings minus interest recompute correctly: $2,200 at base 7, $1,950 at 7.5; round 2 rejects $1,500 left despite falling rates; round 5 accepts $6,100 despite rising rates.
- All runtime money values match an independent implementation of the specified binary ties-to-even monthly convention. Exact decimal half-up gives cent differences, including $1,483.46/$240.65 at base 6; this is a rounding-policy difference, not a change in months or decisions. Kept the specified convention and documented it.

#### Sensitivity

Fictional Japanese American saver, Black car buyer/nurse, Latino delivery worker/card holder and South Asian cafe owner. A cultural reviewer should check the association of each group with one financial role, the cast together and the worried expressions. My cold visual check found respectful full-body adults and consistent identities, with no mocking poses. All 12 people assets are flagged people:true. Luis's repair origin is accessible in Read, tooltip, context and notes; debt is not framed as carelessness. No cultural traditions are taught.

#### Flattest moment left

The recap is still mostly six counts and a discussion prompt. The preceding outcome comparison now does more teaching and the final answers remain readable. Adding new scenarios or another goal would exceed this review's scope.

#### Graphics

Inspected all 16 named images, all 12 poses at about 150-170 px, compact/full-screen placements and open/closed/car outcomes. The spec says 17 but names 16; nothing named is missing. Both cafes redrawn once with the built-in image tool, saved to art/raw/shop-open.png and art/raw/shop-closed.png, then scripts/art.py --rekey only. Final prompts are in art/prompts.json. About 593 KB art; bundle 1022 KB. Beat Lab and Snowy Mail Route frames inspected; retained the street's richer illustration and its own palette.

- Independently recomputed AA contrast on paper/white: ink 14.26/15.80, muted 5.63/6.24, brass 5.71/6.33; neighbor colors at least 5.81/6.44. Focus 5.24/5.81; gold on dial 5.83. Icons and words retain meaning in grayscale.

#### Audit

- Completed the single audit on Chrome 9941, host 8745, within the 40-minute deadline. Final audit.md has 31 leads; its 82 PNGs were opened in indexed contact sheets, with relevant full-size frames also inspected. Seven non-phone sizes, all listed states, Motion off, single/repeated/quick held controls and resize stress completed. No exceptions, infinite calm animations or resize-stuck controls.
- Two phone-harness leads: audit's host returned 404 and no iframe context, so its missing hint is not a tool finding. No automated phone PASS is claimed. Filled that gap through drive.py --host 8745 with eight 375x812 states: default, Predict, wrong reveal, signed high, pinned high, More, final answers and recap. Real held clicks; all frames opened; minimum target 44 px, width 375, no console errors. host.html removed and server stopped.
- Eighteen keep-region leads: context, More and recap intentionally cover six background regions with native modal backdrops. Dialog controls remain visible and own focus. Confirmed on their frames; no pupil choice in the open dialog is covered by the street.
- Three queued-how leads: Pin was already used in pinned-low, and Turn was already used in both reveal states. Their validity guards correctly drop obsolete instructions. Independent main-path and Read logs provide the instruction coverage; no unstarted line is marked heard.
- Six missing first-tap welcomes: dial, minus, plus, Sign, Pin and context act immediately and can skip welcome under BASELINE 16. The premise and controls remain in hint/Read; the context dialog has its own Close instruction. No deferred welcomeAfter pattern.
- Two quick-cut leads: a second Sign tap is Shop again and must stop the now-false signed statement; Reset intentionally hushes its old welcome. Five actual signing events spoke five times in the independent held test. Five-click audit checks were otherwise clean; mode/Reset layout changes are expected.
- The audit used the corrected layout/art bundle. Its only subsequent source change was the narrow cafe-event reversal guard found by the manual voice edge path. Rechecked that guard with a 0.2-second reversal, both voice side paths and the complete main path; no second audit or polish pass. All other earlier fixed frames were covered by this audit or their targeted re-shoots.

#### Left open

- No kit/shared-script changes, commits, publishing or new topics. Scratch holds evidence, scripts and contact sheets. host.html removed.
- Spec ambiguities resolved toward its explicit requirements: 16 named images; monthly classroom formulas; shuffled fixed cases; browser voice until an authorized recording phase.
- Initial read-only doc/memory probes returned immediately before hard subprocess deadlines were installed. All bundling, browser batches and the audit used explicit deadlines. A malformed test-harness expression was discarded and replaced with the successful scoped check.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: interest-rate-dial

Build and cold review. No commits or deployment.

#### Source layout
`src.html` starts from the kit starter. Tool CSS re-lays the four cards and dial at actual pixel sizes. The JS contains the models, six round records, voice table, render functions and input handlers. No family engine exists for money. `window.__tool` exposes the state and model for reproducible review.

Scratch holds the original build assembly parts and scripts. The reviewed `src.html` is authoritative; running the old assemble.py would overwrite review fixes. Images use only art tokens. No runtime files or network are needed after bundling.

#### Tricky parts
- Card interest, payment and balance round monthly with ties to even, matching the spec's Python table. `cents()` rounds the exact floating-point value using BigInt. Do not replace it with Math.round without repeating the number check.
- Keisha's signed annual rate is separate from base. Pin stores both Luis plans to keep comparisons fair.
- Predict uses separate round state; Street survives mode switches. The reveal is scored once. A new round drops queued, unstarted narration.
- Number tweens last 400 ms. A new change during one jumps to the target. The dial sweep is 1.2 seconds, with unchanged pacing when Motion is off.
- Cafe narration limits count actual starts in V.log, with validity checked at playback; muted or stale queued lines use no allowance. Shop again hushes a statement that no longer fits.
- Native modal close callbacks use restoreModal to protect the current hint and focus. The final reveal closes More before opening the recap; Escape can return to the recap button. Keep these ownership checks when changing dialog behavior.
- Contact sheets and source evidence are in `_scratch/interest-rate-dial/`.

#### Open questions and contradictions resolved
- Followed the named art list: 16 assets (1 backdrop, 12 people poses, 2 shops, 1 car). The spec says 17 but names only 16.
- The user's explicit image-tool instruction and the newer Codex people permission take precedence over the older Gemini-only language. All 12 people assets have `people: true` and use reference images to retain each neighbor's identity.
- The open question leans toward a fresh stereotype review and an owner contact sheet. Both sheets are prepared. The fresh agent passed all 12 poses under BASELINE rule 11; evidence is in Scratch's record-review.md. Owner review remains for shipping, outside this build.
- No voice was recorded, following CODEX-BUILD's explicit no-record instruction. `wise-mentor` is selected in lines.json; browser fallback cannot reproduce its recorded timbre.
- The source section's 14.3-point margin is above prime, while this fictional tool adds 14 to its own base. Kept the specified formulas and explicit made-up-add-ons caption. Do not describe the tool base as the actual Fed target.
- The segment suggestions total 25-35 minutes, while the required metadata says 20-35. Kept the explicitly required metadata; segment times are flexible suggestions.
- The opening description says Luis's balance swells, but the specified minimum repays some principal every month. Followed the formula: rate increases raise total interest and payoff time, not the initial $1,500 balance.
- Build/check commands use explicit bounded timeouts. Initial read-only probes returned immediately before that wrapper was established. Reference tools were bundled into Scratch to respect the write boundary.

#### Sensitivity
The four neighbors are fictional Japanese American, Black, Latino and South Asian adults in varied roles. Luis's debt comes from a car repair, not carelessness. Review the people together for stereotypes, respectful worry expressions, hands and full-body framing. No cultural practices or eligibility claims are taught.

#### Engine changes wanted
None. All work is tool-local.

#### Next phase
The cold review is recorded in codex-review.md. Do not infer authorization to publish or start another polish round from this handoff.

#### Cold review changes, 2026-11-07
- Final worked answers stay visible until See your recap. recapHow names that control, then endLine is queued only with the open recap.
- The recap asks how signing changes Keisha's situation, without assuming the final case was signed.
- Wrong calls retain the student's choice beside the correct outcome. Reveal cards have a brass outline.
- The context card names the Fed target range's upper bound, monthly/no-new-charge/no-fee assumptions and Priya's later principal repayment.
- Closed cafe redrawn with the built-in image tool using the open cafe as reference. Same facade, blank sign and framing; brown paper and stacked furniture show the state. Open cafe also redrawn against green to preserve its burgundy awning while cleaning magenta edging. Both raw outputs and prompts remain in art/.
- Retained the spec's ties-to-even money convention. Independent decimal half-up results differ by cents, not months or decisions; do not treat these fictional totals as bank payoff quotes.
- Audit end-recap now presses See your recap explicitly; wrong-reveal covers feedback at every size.
- Do not run Scratch assemble.py over this reviewed source: it holds the earlier build parts.

- Further cold findings: guard late modal-close restoration by mode/round/phase, hush dialog Read on close, label revealed ladders Start to result, cancel the live sweep frame when Motion is turned off, and use the existing dense sidebar through 850 px height.
- Cold checks: all 15 detents match the specified monthly convention; 11 cheap six-round strategies failed to reach 24/24; cap is two cafeYes/two cafeNo starts; five separate signing events spoke; Home/End and jittered pointer drag reach the correct limits. No shared scripts were edited.

- Final voice edge fix: a cafe verdict reversal hushes only an already-playing opposite cafe event, then queues the matching event. It uses V.playing text, preserves the two-start limits and does not cut Read. The full voice main path and reversal are rechecked after the single audit.

#### Cold audit coverage
The single final audit completed on Chrome 9941 / host 8745 within 40 minutes. Its 31 leads are classified in codex-review.md. All seven non-phone sizes, Motion off, focus, repeat inputs and resize stress completed. The audit's own phone host returned 404 and no iframe context, so the separate drive.py host route supplied eight phone states with real held clicks. All eight are 375 px wide with 44 px minimum targets and no console errors.

#### Audit harness change wanted
In scripts/audit_tool.py, Audit.size, save a frame and the host response status when iframe context is missing before returning the lead. This run's failed phone route produced no diagnostic screenshot. Investigate the host's 404 separately; its cause is unconfirmed. No shared script was changed here.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
