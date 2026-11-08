# Codex report: grid-operator

## Built
Plan, Run and Compare are complete in the offline bundle. Eight painted plant cards, three 168-hour weeks, real-time dispatch, outage banners, battery storage, four saved plans, comparison metrics and all four challenge cards are implemented.
Required source, draft metadata (stage built), notes, voice manifest, audit states, handoff and artwork are present. preview.svg is included. No commits, shared-file edits, audio recording, deployment or polish round.
Writes stayed in tools/grid-operator and _scratch/grid-operator. The working folder was verified as S:\CurioClass-codex before work.
Build/check commands used explicit timeouts after the initial fast read commands. Those initial reads completed immediately but were not wrapped in process timeouts. Bundles used 120 seconds, browser batches 300 seconds and the audit 2400 seconds.

## Numbers check
Independent Python reference and browser/JavaScript calculations agree for 21 reference week cases. The JavaScript model also passed 1,209,856 assertions, including 201,600 randomized hourly power/storage balances. Evidence: numeric-reference.json, model-validation.json and source-extras.json in Scratch.

| Case | Recomputed evidence |
|---|---|
| Base Spring | $2,948,769; $28.43/MWh; 32,582 t; zero shortfall; 2,000 MWh curtailed |
| Base Heat wave | $3,407,466; $27.82/MWh; 39,115 t; zero shortfall |
| Base Winter | $3,487,211; $29.52/MWh; 44,444 t; zero shortfall |
| Base three weeks | $9,843,446; $28.59/MWh; 116,140 t, using unrounded values |
| Retire both coal | Spring $21.69/MWh; Heat 12,673.6 MWh / 79 h; Winter 3,142.6 MWh / 46 h |
| Keep only coal 1 | Heat 2,216.1 MWh / 30 h |
| No coal, +400 CC | Zero shortage; CO2 12,706 / 21,725 / 21,744 t; $29.56 / $29.37 / $30.46 per MWh |
| No coal, +300 solar, +200 battery | Spring 27.0% W+S; Heat 5,944.7 MWh / 43 h; Winter 2,889.5 MWh / 40 h |
| Base +200 battery | Winter CO2 unchanged; Spring curtailment 1,530 MWh |
| Renewable challenge fleet | No coal, +600 wind, +300 solar, +300 battery, +400 CC: Spring 50.1% W+S |

Additional source claims reproduced: +100 / +200 / +300 CC without coal leave 6,248.4 / 2,216.1 / 227.9 MWh short in Heat wave; +300 has 11 short hours. Coal on with +600 wind gives 25.7% Spring W+S.
Run rates recompute to 9.31, 31.67919, 19.7449 and 32.49685 dollars/MWh. Coal/gas CO2 recomputes to 1.047798375, 0.337046573 and 0.524088902 t/MWh. Base fixed upkeep is $1,369,269.23/week.
Actual annuity factors are 0.0805864035 (30 years) and 0.1097946247 (15 years). The specified rounded factors are used. Some capital labels differ from the spec's rounded table cells by $1 to $7; the full worked scores match. Play durations are approximately 28 and 7 seconds.

## Facts checked
- Fictional Ridgeport, demand peaks 770/1,000/900 MW, demand shapes, weather, events, coal minimum, battery four-hour capacity, 85% efficiency and half-full starts: explicit teaching assumptions in spec.md, not measured city data.
- Build costs per 100 MW: nuclear SMR $834.9m, CC $117.6m, peakers $86.7m, wind $209.8m, solar $144.8m, battery $127.0m. Fixed upkeep 136.91 / 45.68 / 13.73 / 7.88 / 29.64 / 17.16 / 45.76 dollars/kW-year: [EIA AEO2023 Table 1](https://www.eia.gov/outlooks/aeo/assumptions/pdf/elec_cost_perf.pdf), with the nuclear exception below.
- CC/peaker heat rates 6.370 / 9.905 MMBtu/MWh and variable upkeep 2.10 / 5.06; coal upkeep 5.06: the same AEO2023 table. Coal heat rate 10.777: [EIA Annual Table 8.1](https://www.eia.gov/electricity/annual/html/epa_08_01.html).
- Coal/gas fuel prices $2.47 / $2.77 per MMBtu are historical 2024 inputs: [EIA Monthly Table 4.1](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_4_01) for coal and [EIA Annual Table 7.20](https://www.eia.gov/electricity/annual/html/epa_07_20.html) for gas. Nuclear fuel $6.64/MWh is 2025: [EIA Annual Table 8.4](https://www.eia.gov/electricity/annual/html/epa_08_04.html). The on-screen cost-date note corrects the spec's blanket 2024 statement.
- Nuclear variable/fixed upkeep 2.67 / 136.91 is the AEO2023 large light-water-reactor row. SMR instead lists 3.38 / 106.92. The spec's common operating assumptions were retained, while new nuclear uses SMR capital cost. This is a model simplification, not a source-exact SMR estimate.
- Coal 2.31 pounds CO2/kWh: [EIA emissions FAQ](https://www.eia.gov/tools/faqs/faq.php?id=74&t=11). Gas 116.65 pounds CO2/MMBtu: [EIA emissions coefficients](https://www.eia.gov/environment/emissions/co2_vol_mass.php). Conversion uses 0.45359237 kg/lb.
- US 2024 capacity factors coal 42.6%, CC 60.5%, peakers 13.9%: [EIA Monthly 6.07.A](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_a). Corrected the spec's peaker 19.9%, which is the adjacent steam-turbine value. Nuclear 90.8%, wind 34.3%, solar 23.2%: [Table 6.07.B](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b).
- Cold-weather gas constraints are grounded in the [FERC/NERC Elliott findings](https://www.ferc.gov/news-events/news/ferc-nerc-release-final-report-lessons-winter-storm-elliott). Ridgeport's exact 70% restriction is invented. Zero fuel CO2 for nuclear, wind, solar and battery discharge is the combustion-only model boundary; lifecycle emissions are excluded explicitly.
- Cost per MWh divides full cost by served energy. W+S share is accepted renewable output / served energy, including charging input. Unserved energy has no dollar price. These are explicit model definitions, not external factual estimates.

## Break it
Twelve additional cheat/reachability checks pass in cheat-checks.json.
- Retire everything: 504 shortage hours, zero served, per-MWh values n/a, no challenge awarded. Zero cost/CO2 cannot win reliability or cheapest-plan cards.
- Save before running, pause early or Skip: comparison always computes all 504 hours; no partial result can set a saved best.
- Forge stored scores or labels: scores are recalculated from the fleet; names are regenerated as Plan A-D. Injected HTML names and negative stored scores are ignored.
- Inject excessive/negative builds or forbidden coal construction: saved-plan normalization clamps buildable types to 0-1,000 MW and coal additions to zero.
- Spam steppers past both bounds: 1,000 maximum and zero minimum hold. Existing capacity remains separate from new builds.
- Add maximum capacity: reliable/low-carbon cards can be met legitimately, but capital/upkeep remains charged. The tested overbuilt renewable fleet cannot beat base cost. Cheapest means best saved so far, stated on the card.
- Retire coal and cherry-pick Spring: Heat and Winter shortages still appear in comparison. The +400 CC fleet meets cards 1 and 2; the specified renewable fleet meets card 3.
- Sweep battery charging and capacity: storage never exceeds four hours or its power limit. Loss is charged at 85%, gas charging is confined to 00:00-05:00, and its fuel/CO2 are counted. CC readout/chart includes charging generation.
- Edit while playing: playback stops and hour resets to -1, with the required plan-changed hint. Week and coal changes also reset immediately.
- Remove all fossil capacity: the heat-wave banner correctly says no output is removed; it does not invent a gas-unit trip. no-fossil-result.json records zero shortfall and no false trip narration.

## Voice walk
Curio.voice and firm-captain manifest are used with browser speech fallback. No recordings were made. The manifest matches all ten fixed runtime lines.
Main held-click path at 2-second spacing logged, in order: wPlan, wRun, trip, done, wCompare. It saved base, ran Heat wave, then saved and compared a coal-free +400 CC alternative. See voice-main-retry.json.
Side path logged wCompareEmpty with one plan, then squeeze/done in two winter runs. events-result.json independently recorded tripGas twice, squeeze twice and dark four times across fresh runs. All event lines repeat; how/welcome lines remain once per page.
The original drive voice batch exceeded a single CDP evaluation's time limit. A smaller bounded walk using the existing drive helpers succeeded, with zero exceptions. This is recorded rather than counted as an initial pass.
The audit's five held clicks at 2-second pace were clean. Five focused 0.7-second double-tap checks also passed after active-mode and already-reset actions were made harmless to valid narration. Each welcome started once, with no cut. Read's audit checks were clean. The final challenge walk also logged its challenge event after the one-plan welcome.

## Feel check
Played a three-week student path and the coal-retirement/replacement alternatives. Best moment: the trip cuts a visible notch from supply, then a revised fleet covers the same high-demand week; its higher cost and lower fuel CO2 make the result specific to the design.
Flattest moment 1: the compact fleet initially clipped its controls. Reworked the small cards as illustrated instrument plates, retaining 44px controls and readable source data.
Flattest moment 2: Compare was a tall list with wasted width. Grouped each cell's metrics, added the specified three bars, and kept comparison controls outside the phone's scrolling table. Whole-week evidence is much easier to contrast.
Compared the final fleet frame beside Beat Lab in feel-compare.png, and inspected Snowy Mail Route's motion/feedback frame. Grid Operator's large plant paintings, dimensional control-room setting and sharp supply/shortfall chart meet the visual bar for a Grade 12 instrument. It has less branching content than Beat Lab, but the fleet/weather/storage tradeoffs support repeated design attempts without decorative rewards.

## Done when
1. PASS: base weekly and three-week cost/CO2/curtailment values match after rounding; numeric-reference.json.
2. PASS: both-coal retirement case and shortage counts match.
3. PASS: one-coal Heat wave trip gives 2,216.1 MWh / 30 hours.
4. PASS: +400 CC gives zero shortages, the specified CO2/rates, and cards 1/2.
5. PASS: +300 solar / +200 battery gives 27.0% Spring and specified shortage totals/hours.
6. PASS: battery-only comparison and the 50.1% renewable challenge case match.
7. PASS: Plan's 4x2 fleet, Run's dominant chart and Compare's dominant table checked at 1366x768 and 680x425. Canvas legend text is 10px minimum. Long evidence tables scroll.
8. PASS: controls-result.json verifies same-frame pause, one-hour Step, immediate week reset and instant completion. Speed is read from state on the next frame.
9. PASS: laptop Run controls/chart fit; 375px iframe Run has readable labels and Play without scrolling. Nine unique embedded WebP assets load, with no people.
10. PASS: main/side/repeated-event walks and the audit's five-click checks verify the requested narration behavior. One-plan Compare uses wCompareEmpty.

## Wave lessons
- Hint/voice: PASS. Hints update immediately, name live controls, and Read uses the current hint. The kit tracks heard lines; no custom narration counters.
- Focus/layout: PASS after repair. Static fleet buttons survive updates; Run week moves focus to Play, loading a plan moves it to Run week, and no focus is taken on load.
- Sizes/targets: PASS for the preview/laptop controls and focused phone checks. All tested targets are at least 44px; all hints stay in view. Phone fleet editing uses a long scroll editor rather than shrinking its artwork and controls.
- No giveaways: PASS. This is an open engineering model, not a hidden-answer quiz. No badge awards a partial or empty reliable result.
- Honest numbers: PASS with explicit assumptions and documented nuclear-source simplification. No unserved dollar penalty or lifecycle CO2 claim is invented.
- Standards: PASS. Students create competing energy designs, test them and compare cost-benefit evidence for HS-ESS3-2.
- Motion off: PASS. No infinite animation remains; timers retain their pace. calm-result.json records zero running infinite animations.
- Short choices: PASS after repair. Phone/compact comparison actions stay above the evidence table. The optional challenge drawer uses its own panel space; plant editing is a longer control collection.
- Resize mid-animation: PASS for exception/unlock behavior. The chart redraws from model records, not transient DOM nodes. The audit's scorecard visibility difference is explained below.
- Late welcome: PASS. Explicit first-edit staleness matches the spec; no welcomeAfter is used.
- Unknown/known: PASS. Scenarios are invented, with a faint demand forecast and explicit ready/running/completed states, not hidden diagnostic facts.
- One look/one meaning: PASS. Coal hatch, peaker dots, battery lines, shortfall cross-hatch, hollow curtailment and text labels remain distinct, including grayscale.
- Badges true: PASS. Checks use full tests; best means the stated lowest value, not an overall recommendation.
- Hint changes back: PASS. Week, mode, plan and Reset transitions set the current next action synchronously.
- No answer by copying: PASS/not applicable to a hidden-answer quiz. Students must evaluate tradeoffs; copying one criterion does not optimize the other scores.

## Audit leads
One full audit completed with 44 leads in audit/audit.md. It began before the final repairs, so it is not a clean final snapshot. No second full audit was run. Focused repairs were checked in seven lead JSON/frame cases, five quick-voice cases and the final challenge check.
- 8 small Plan/Run mode-target leads across four widths: fixed with a 44px minimum.
- 4 initial battery label overlap leads: fixed with compact title sizing and unambiguous capacity type.
- 2 iframe-host/no-hint leads: test-host conflict, repaired for focused 375px checks. Actual phone Run, scorecard, Compare and Plan were subsequently opened and inspected.
- Run-week focus lead across seven sizes: fixed with deliberate Play focus and preventScroll.
- Behind-modal Scorecard and clipped short scorecard actions: fixed by hiding the duplicate button while its dialog is open and compacting the short-height dialog.
- 2 zero-font saved-summary leads: fixed by hiding an explicit summary span, keeping visible text at least 10px.
- 2 whole-Compare-stage keep leads: intentional. The full table and bars are larger than the viewport and scroll; no metric is omitted, and controls/hint remain outside that scroll area.
- Challenge-drawer keep lead: fixed by giving the four cards the panel space used by saved-plan shortcuts. All four fit at 1366x768 in challenge-final.png.
- Charging notice, maximum nuclear label and maximum battery label overlaps: fixed; lead-max.json is clear.
- Scorecard "left disabled" during resize: a comparison artifact while its duplicate button was changed to hidden during an open dialog. It is restored on close; the final end-of-week frame shows the button available. It is not a stuck run control.
- 13 first-edit welcome leads (keep0/plus0, keep1, keep2, keep3/plus3, keep4/plus4, keep5/plus5, keep6/plus6, plus7): intentional staleness. The spec says wPlan stops fitting after a fleet edit. The next-control hint updates at once; wRun is still heard on entry.
- 5 quick-tap welcome-cut leads (Plan, Run, Compare, Reset, Start over): fixed. Re-selecting the current mode and resetting an already-base plan do not cut valid narration. quick-*.json logs one uncut welcome each.

## Frames looked at
Opened both bar frames; every initial/fit, functional, seven-size-per-mode, phone, extras, quick, lead, targeted, voice and final frame; and all 49 full-audit PNGs via labeled contact sheets with problem frames inspected separately. Evidence directories and contact sheets are all in Scratch.
Key frames: last-frames/feel-final.png; lead-frames/lead-max.png; lead-frames/lead-score.png; lead-frames/lead-phone-run.png; lead-frames/lead-phone-compare.png; last-frames/phone-plan-final.png; challenge-frames/challenge-final.png; extras-frames/grayscale.png; feel-compare.png.

## Art made
Nine new gpt-image assets, 480,922 bytes (469.7 KB) of WebP. Wind was redrawn once to remove an unrelated industrial plant. No people. Original two unused paintings and their provenance remain preserved.
Final bundle: 729,885 bytes (712.8 KB); voice: 0 KB recorded. Nine unique image data URIs; no external src/href requests. Under the 2 MB goal.
Images, prompts, raw files, provenance and final-size visual inspection are complete. See art/prompts.json and Scratch art-paths.json / wind-redraw-path.json.

## Art still to paint
None.

## Engine changes wanted
None.

## Left open
- Nuclear combines SMR build cost with large-reactor upkeep, as the spec requires. This explicit simplification needs owner review before release; the tool remains beta.
- No second full audit after repairs, per the one-audit build instruction. The cold reviewer should use the final bundle and the focused evidence, not treat the 44-lead report as the final visual state.
- Phone fleet cards and long comparison evidence scroll. The main controls and hint stay visible; full plant artwork/data was preserved.
- firm-captain recordings are not present because this build forbids recording audio. Browser fallback narration was tested.
- Initial fast read commands lacked process timeout wrappers; every later build/check command was explicitly bounded. No command was left running.

All owned Chrome processes and the local host are closed, and temporary host.html is removed. Ports 9980-9987 and 8785 were checked at completion. No git commit or polish round.
