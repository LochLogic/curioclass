# Codex review: interest-rate-dial

## Played

Cold as a grade 7 student, then as a projecting teacher: Street, all six Predict cases, wrong calls, replay, compact screens and voice. The signed car versus changing card debt is the strongest moment. Played before reading builder material.

## Findings fixed

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

## Findings left

- No confirmed blocker or should-fix knowingly left open. Recorded wise-mentor audio remains a later phase; browser speech is the authorized fallback.

## Break it

- Four-pick gate: empty and three-pick Turn attempts leave picks/score unchanged. Post-reveal changes, repeated Turn and Street/Predict switching cannot alter or duplicate a score.
- Entire six-round actual input runs: first position everywhere 10/24; last position after mashing all options 6/24; rates-up-bad-for-everyone 11/24. None earns a perfect recap.
- Priya cheats with the other three correctly reasoned: always Yes 3/6; always No 3/6; Yes when falling 2/6; Street's memorized boundary 3/6; forgetting $2,000 3/6; large profit 4/6; new rate below 10% 2/6; $1,000 cushion 3/6. Full tallies are 20-22/24, with specific wrong calls visible.
- Future totals, poses, cafe sign and worked remainder stay concealed before Turn, including More. Future rates are supplied inputs as specified, not answers.
- Fast final recap retains the final result before endLine, even when cafeHow is still speaking. The suspected result-drop issue was falsified by the real held-click log; no change was made there.
- Play again clears all six prior tallies and picks, starts at round 1 with a permutation of the six cases, and scores only the new round. Prior 24/24 cannot carry over.
- Street bar, pin, moods and cafe verdict are computed explorations, not mastery meters. Whole-pixel jittered sweeping reaches both useful extremes without scoring; pin stores both card plans, so toggling plans at a pinned rate remains Same.
- Signed at base 6 then moved to 9: $356.42 stays fixed; card becomes 23%, 113 months, $1,784.53. Minimum/$100 at base 6 remains 107/18 months and $1,483.44/$240.64.
- Cafe narration cap, real keyboard boundaries, final recap arithmetic and targeted regressions: see retained review-event-cap, review-key-boundaries, review-validation and review-regression-final JSON evidence.

## Voice walk

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

## Facts checked

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

## Sensitivity

Fictional Japanese American saver, Black car buyer/nurse, Latino delivery worker/card holder and South Asian cafe owner. A cultural reviewer should check the association of each group with one financial role, the cast together and the worried expressions. My cold visual check found respectful full-body adults and consistent identities, with no mocking poses. All 12 people assets are flagged people:true. Luis's repair origin is accessible in Read, tooltip, context and notes; debt is not framed as carelessness. No cultural traditions are taught.

## Flattest moment left

The recap is still mostly six counts and a discussion prompt. The preceding outcome comparison now does more teaching and the final answers remain readable. Adding new scenarios or another goal would exceed this review's scope.

## Graphics

Inspected all 16 named images, all 12 poses at about 150-170 px, compact/full-screen placements and open/closed/car outcomes. The spec says 17 but names 16; nothing named is missing. Both cafes redrawn once with the built-in image tool, saved to art/raw/shop-open.png and art/raw/shop-closed.png, then scripts/art.py --rekey only. Final prompts are in art/prompts.json. About 593 KB art; bundle 1022 KB. Beat Lab and Snowy Mail Route frames inspected; retained the street's richer illustration and its own palette.

- Independently recomputed AA contrast on paper/white: ink 14.26/15.80, muted 5.63/6.24, brass 5.71/6.33; neighbor colors at least 5.81/6.44. Focus 5.24/5.81; gold on dial 5.83. Icons and words retain meaning in grayscale.

## Audit

- Completed the single audit on Chrome 9941, host 8745, within the 40-minute deadline. Final audit.md has 31 leads; its 82 PNGs were opened in indexed contact sheets, with relevant full-size frames also inspected. Seven non-phone sizes, all listed states, Motion off, single/repeated/quick held controls and resize stress completed. No exceptions, infinite calm animations or resize-stuck controls.
- Two phone-harness leads: audit's host returned 404 and no iframe context, so its missing hint is not a tool finding. No automated phone PASS is claimed. Filled that gap through drive.py --host 8745 with eight 375x812 states: default, Predict, wrong reveal, signed high, pinned high, More, final answers and recap. Real held clicks; all frames opened; minimum target 44 px, width 375, no console errors. host.html removed and server stopped.
- Eighteen keep-region leads: context, More and recap intentionally cover six background regions with native modal backdrops. Dialog controls remain visible and own focus. Confirmed on their frames; no pupil choice in the open dialog is covered by the street.
- Three queued-how leads: Pin was already used in pinned-low, and Turn was already used in both reveal states. Their validity guards correctly drop obsolete instructions. Independent main-path and Read logs provide the instruction coverage; no unstarted line is marked heard.
- Six missing first-tap welcomes: dial, minus, plus, Sign, Pin and context act immediately and can skip welcome under BASELINE 16. The premise and controls remain in hint/Read; the context dialog has its own Close instruction. No deferred welcomeAfter pattern.
- Two quick-cut leads: a second Sign tap is Shop again and must stop the now-false signed statement; Reset intentionally hushes its old welcome. Five actual signing events spoke five times in the independent held test. Five-click audit checks were otherwise clean; mode/Reset layout changes are expected.
- The audit used the corrected layout/art bundle. Its only subsequent source change was the narrow cafe-event reversal guard found by the manual voice edge path. Rechecked that guard with a 0.2-second reversal, both voice side paths and the complete main path; no second audit or polish pass. All other earlier fixed frames were covered by this audit or their targeted re-shoots.

## Left open

- No kit/shared-script changes, commits, publishing or new topics. Scratch holds evidence, scripts and contact sheets. host.html removed.
- Spec ambiguities resolved toward its explicit requirements: 16 named images; monthly classroom formulas; shuffled fixed cases; browser voice until an authorized recording phase.
- Initial read-only doc/memory probes returned immediately before hard subprocess deadlines were installed. All bundling, browser batches and the audit used explicit deadlines. A malformed test-harness expression was discarded and replaced with the successful scoped check.
