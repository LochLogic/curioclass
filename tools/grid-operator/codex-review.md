# Codex review: grid-operator

## Played

Cold as Grade 12: edited the fleet, ran complete Spring, Heat wave and Winter weeks, explored empty Compare, saved rival fleets and opened challenges before reading the builder's report, handoff, notes or source. The trip and replacement-fleet comparison are strong; the original scorecard finish was flat.
Also checked it as a projected instrument. Kept the amber desk, paintings, detailed stack, three separate scores and engineering choices. Compared actual frames with Beat Lab and Snowy Mail Route; `review-feel-compare.png` preserves the side-by-side check.

## Findings fixed

- **Should fix, general, dialogs/Reset:** Escape left hints naming hidden scorecard actions; edited-Plan Reset retained the changed-plan hint and missed its welcome. Close and Reset now synchronize hints, welcome and the challenge drawer.
- **Should fix, general, Plan:** bound taps claimed the plan changed and reset work. They now explain zero/1,000 MW limits without changing the plan or run.
- **Should fix, general, Plan:** storage privacy was explicit only in Compare. Save now visibly says plans stay on this device, at every size.
- **Should fix, family:grid-operator, assumptions:** compact Plan hid historical price dates and the SMR/large-reactor upkeep simplification. Both are now in the always-visible Plan footer; Compare states its retained-coal commitment above the evidence.
- **Should fix, general, 680x425 Compare:** its short four-card drawer hid cards 3 and 4. Short-landscape actions now share a row and all four cards fit. Added compact and phone audit states.
- **Should fix, general, grayscale Run:** adjacent solid bands had faint boundaries. Added thin dark contours, preserving colors, patterns and labels; checked laptop, preview and phone frames.
- **Should fix, general, narration:** queued trip/squeeze/shortage events could remain valid after completion. Their validity now ends with the run.
- **Polish, family:grid-operator, scorecard:** added the actual peak-covered or largest-shortage hour, with a skyline plate and supplied/demand strip. It explains this fleet's result without adding a score or gate.
- **Polish, general, art:** redrew the wind painting with richer depth, clouds, access tracks and accurate three-bladed rotors, matching the existing set.
- **Should fix, general, sources:** corrected Elliott's final-report date to November 7, 2023 in metadata and replaced the inaccessible notes link with FERC's final-report page.
- **Should fix, general, audit leads:** challenge notes inherited 8.3/9.2 px small type; set them explicitly to 10 px. Scorecard was below the smallest preview fold after Escape; it now takes the inactive Step hour slot at completion, returning Step on a new run.
- **Should fix, general, Run wording:** the static title asserted supply met demand even during shortage runs. It now neutrally names supply and demand.

## Findings left

- **Should fix, spec-bound, Compare:** the spec explicitly calls the lowest value in every measure "best", including renewable share. Retained that rule and moved its explanation above the table. A better ranking/wording needs a spec decision, which the review brief forbids inventing.
- **Should fix, spec-bound, cheapest card:** saving the untouched base fleet immediately earns the best-saved-cost check. Confirmed the cheap success. It is a truthful best-saved record under the explicit spec, but demonstrates no design-evaluation skill. A mastery requirement would change the spec.
- **Nit, general:** zero-service monetary rates read `$n/a`; the undefined rate is correctly excluded from best-cost challenges.

## Break it

- **Cost/reliability/CO2:** tried saving before Run, early pause and Skip. Compare recomputes all 504 hours, rather than accepting a partial or displayed score.
- **Coal-free card:** retiring both units with no replacement fails: Heat has 12,673.6 MWh / 79 shortage hours; Winter 3,142.6 MWh / 46. A cheap Spring cannot pass the three-week gate.
- **Low-CO2 card:** retired every generating plant. Zero fuel CO2 gives 504 shortage hours, undefined rates and no award. The coal-free +400 CC fleet legitimately passes cards 1 and 2.
- **Renewable card:** swept builds and charging; the criterion remains the specified Spring-only accepted-generation ratio, not a reliability certificate. The prescribed +600 wind/+300 solar/+300 battery/+400 CC coal-free fleet reaches 50.1% and passes the card in real held-click input.
- **Cheapest record:** zero-service and unreliable fleets cannot set it; stored fake negative costs/zero shortages are ignored. An untouched base save does earn the record, as noted above. Overbuilding pays capital and upkeep; the renewable example costs $61.10/MWh across the three weeks.
- **Battery meter:** 8,064 hourly checks across 48 extreme fleet/week/charging cases pass power balance, storage balance, zero-to-four-hour capacity, power bounds and overnight gas-charge restrictions. The independent battery +200 case retains winter CO2 and cuts Spring curtailment to 1,530 MWh.
- **Input/storage:** real plus/minus sweeps clamp at 0/1,000 MW. Forged saved names/scores are replaced by normalized plans and fresh calculations; injected markup never becomes DOM.
- No quiz, prediction answer, reflection gate or rhythm/timing score exists. Numeric readouts are engineering evidence, not hidden-answer clues.

## Voice walk

Held 120 ms clicks, default 6 hours/second, Sound on, two-second action spacing: status, Save, Run week, Play Spring, Try next week/Play Heat, Try next week/Play Winter, Revise fleet, retire coal/add CC, Save, Compare, Challenge cards.
Actual starts: `wPlan, wRun, done, trip, done, squeeze, done, wCompare, challenge`. Each main-mode how-to starts once; the three completion events repeat. Side path: coal-free Heat, replay, Read during speech, then empty Compare; `dark` and `tripGas` repeat and `wCompareEmpty` fits the screen.
Ten additional real held-Step runs check event repetition; rapid stepping is a separate stress path from the default-paced main walk.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| wPlan / wRun / wCompare | Main how-to | 1 each | 1 each |
| wCompareEmpty | Side how-to | 1 | 1 |
| wRun | Repeated-run how-to | 1 | 1 |
| tripGas | Repeated Heat event | 5 | 5 |
| squeeze | Repeated Winter event | 5 | 5 |
| dark | Repeated first-shortage event | 10 | 10 |
| done | Repeated completion event | 10 | 10 |

The manifest matches all ten fixed runtime lines. Main, side, controls, keyboard and repeat logs have no console exceptions. Evidence: `focused-results.json`; recordings are absent and browser speech was used.

## Facts checked

- **Build/upkeep:** all seven build costs and fixed-upkeep rows, CC/peaker heat rates 6.370/9.905, variable upkeep 2.10/5.06, and nuclear upkeep 2.67/136.91: [EIA AEO2023 Table 1](https://www.eia.gov/outlooks/aeo/assumptions/pdf/elec_cost_perf.pdf). The nuclear operating row is large-reactor data; SMR capital is $8,349/kW, while source-exact SMR upkeep would be 3.38/106.92. The mandated hybrid is disclosed, not silently recalculated.
- **Fuel:** coal heat rate 10.777 from [EIA Annual 8.1](https://www.eia.gov/electricity/annual/html/epa_08_01.html); $2.47/MMBtu coal from [Annual 7.1](https://www.eia.gov/electricity/annual/html/epa_07_01.html), $2.77 gas from [Annual 7.20](https://www.eia.gov/electricity/annual/html/epa_07_20.html); nuclear $6.64/MWh is 2025 [Annual 8.4](https://www.eia.gov/electricity/annual/html/epa_08_04.html). Recomputed run rates: 9.31, 31.67919, 19.7449, 32.49685 dollars/MWh.
- **Emissions:** coal 2.31 lb/kWh from [EIA's 2023-generation FAQ](https://www.eia.gov/tools/faqs/faq.php?id=74&t=11); gas 116.65 lb/MMBtu from [EIA coefficients](https://www.eia.gov/environment/emissions/co2_vol_mass.php). Recomputed 1.047798375 / 0.337046573 / 0.524088902 t/MWh. Zero nuclear/wind/solar/battery-discharge fuel CO2 is the stated combustion-only boundary, not a lifecycle claim.
- **2024 capacity factors:** coal 42.6%, CC 60.5%, peakers 13.9% from [EIA Monthly 6.07.A](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_6_07_a); nuclear 90.8%, wind 34.3%, solar 23.2% from [6.07.B](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b). Preserved the builder's correct 13.9%; the spec's 19.9% is the adjacent steam-turbine value.
- **Cold gas supply:** [FERC/NERC final Elliott report release](https://www.ferc.gov/news-events/news/ferc-nerc-release-final-report-lessons-winter-storm-elliott), November 7, 2023, supports the cold-weather gas constraint context. The exact 70% restriction and Ridgeport outage are fictional scenario inputs.
- **Model assumptions:** Ridgeport/population, 770/1,000/900 MW peaks, weather/demand shapes, 40% coal minimum, 85% charging efficiency, four-hour/half-full storage and financing periods come from `spec.md`, not measured real-city data. Cost divides by served MWh; accepted W+S includes charging input. These boundaries are stated on screen/in notes.
- **Recomputed numbers:** `reference.py/reference.json` independently reproduce all 21 cases for Done when 1-6; the browser comparison passes cost, emissions, shortage hours/MWh, curtailment and share to 0.0001. Base weeks: $2,948,769 / $3,407,466 / $3,487,211; three-week $9,843,446, $28.59/MWh, 116,140 t. Base fixed upkeep $1,369,269.23/week. Rounded annuity factors explain the table's few-dollar capital-label discrepancies.
- **Teaching:** HS-ESS3-2 is practiced by designing competing fleets, testing stressful weeks and comparing cost-benefit evidence. Notes retain the required opening sections and practical home support.

## Sensitivity

None of the specified cultural, Indigenous, religious, hard-history or body topics applies. Ridgeport is fictional; all nine used pictures show equipment/places without people. Broader environmental and social factors remain named model omissions, not claims of a complete real-grid assessment.

## Flattest moment left

Compact Plan still reads like a dense instrument plate, with 10 px source data and less space to enjoy paintings. Kept its complete fleet and full-sized controls; laptop art remains large. Compare's long evidence and bars scroll rather than losing metrics.

## Graphics

All nine used paintings inspected in the tool and at plant-asset size; one consistent editorial style, no garbled lettering, people or missing art tokens. Wind was redrawn once in this review using built-in imagegen; final prompt in `art/prompts.json`, raw `art/raw/go-wind.png`, final `art/go-wind.webp`; processed with permitted `art.py --rekey`.
Bundle: 878.3 KB, offline, no external src/href requests. Brand/panel 10.63:1, brand-ink/brand 11.15:1, muted/secondary 9.07:1; tested source-value text ratios 5.15:1 or better. Motion off has zero running infinite animations; keyboard-only Step/Skip/Escape/Motion completes with visible focus.

## Audit

One full audit completed within the 40-minute cap: `review-audit/audit.md`, 23 leads. Its desktop size, focus, resize, Motion-off, repeated-click and quick-tap checks are clean apart from the confirmed findings below.

- Fixed six UI leads with two repairs: four grouped tiny-note leads and two hidden-Scorecard leads. The audit snapshot predates these narrow repairs; targeted re-shots cover all affected standard sizes and phone, including stepped-end keyboard focus. No second audit was run.
- Two whole-Compare-stage keep leads are intentional scrolling evidence, not missing content; main actions and hints remain outside its scroller.
- Thirteen first-edit welcome leads follow explicit spec staleness and BASELINE rule 16. Hints/Read preserve the next action; the real main path hears all three mode how-to lines.
- Two phone-harness leads reflect missing iframe execution context, not a verified tool failure. Separate 375px same-origin iframe frames/checks cover Plan, Run, Compare, scorecard and the repaired controls. This mechanical phone-audit coverage gap remains recorded; port-ownership/host-root follow-up is in handoff.

All 59 audit PNGs were opened via contact sheets, with the confirmed problem frames opened individually. All manually captured frames were also inspected. Evidence lives only in Scratch.

## Left open

- Followed the tool-specific design on the undefined carbon-price slider, paused-hour behavior and renewable-only charging; contradictions with broad baseline/spec wording remain documented in handoff. Added no new policy feature or mastery gate.
- Kept the specified nuclear cost hybrid and accepted-generation share accounting; source-exact replacements would alter the worked examples. These need a spec decision before claims of real-world planning accuracy.
- firm-captain recordings are missing. The build/review rules prohibit recording audio; browser fallback was tested.
- Initial fast read commands lacked hard process deadlines, and the scratch timeout helper preceded full spec reading. All later commands/checks were bounded; no source edits preceded cold play. One test fixture initially inherited saved plans and one keyboard helper omitted Enter text; isolated/repaired checks replaced those invalid results.
- Cleanup found four host children surviving their Python launcher. Their exact command lines and workspace cwd were verified before termination; multiple hosts are a plausible cause of the audit iframe gap. No second audit was run. Cleanup identities are preserved in `owned-host-cleanup.json`.
- Writes stayed in `tools/grid-operator/` and `_scratch/grid-operator/`; no commits. Assigned ports only. Owned Chrome/server processes were closed and temporary host removed.
