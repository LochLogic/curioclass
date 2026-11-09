# Polish: up-the-watershed (Codex fix, round 1)

The user's Curiosity instruction overrides the lesson-shaped spec and Refine. This fix preserves the creek model and illustrations while replacing the lesson frame with an open field station. No welcome screen, claim grading, score, goal, solved stamp, kit limit, locked simulator or finish screen remains. `refine.md` was not edited. Only this tool and its Scratch folder were written; no git commits were made.

Evidence root: `../../_scratch/up-the-watershed/`. Each path below is relative to that root. Original source is `before-src.html`. All named frames were opened and inspected. Numbers are retained as JSON beside the shot lists. Tests used Chrome 9910 and the narrow iframe host 8715; the final audit used Chrome 9911 and host 8715. Bundle commands were capped at 120 seconds, drive batches at 300 seconds and the audit at 2,400 seconds.

## Blocker

1. **FIXED, by removing the lesson check.** Before: `before/empty-submit.png`, `before/blanket-submit.png` and their JSON show a blank claim naming all three culprits and enabling revelation; blanket accusation returns exact spot recipes. After: `focus-v2/focus-default.png` and `verify-numbers.json` show zero claim, submit, reveal or kit controls. The baseline ledger is explicitly open model output, never a reward for a submission. It cannot create sampled evidence. This follows the user's Curiosity override instead of adding a new prerequisite or answer check.
2. **FIXED.** Before: `before/gauges.png`, `before-gauges.json`: every missed criterion gets 35%, with the lake and creek targets replaced. After: `retouch/final-fix-680.png`, `retouch/final-fix-375.png` and `numeric-verification.json`: physical storm-concentration bars on fixed scales, with permanent reference ticks and both weather values. Beach baseline 738.738 CFU/100 mL fills 92.342%; C+A 518.544 fills 64.818% of the 800 scale. No progress or success bars remain. P and sediment scales are 0.400 and 600 mg/L; the Manual names the scales. The cost track names its $0–$4.1m scale and $3m tick.

## Should fix

1. **FIXED.** Before: `before/flood-evidence.png` and JSON show the drain ending at (612,470), below S7. After: `final-map/final-map-1366.png`, `retouch/final-map-680.png` and `retouch/final-map-375.png`: endpoint (515,458), before S7. Pipe remains at the upper end; the drain miniature sits on the line.
2. **FIXED.** Before: `before/result-1366.png` has no flow and the old Claim hint states an uncheckable 20% rule. After: `verification/verify-live-flow.png`, `verify-live-flow.json`, `verification/verify-compare-1366.png`: S7 dry flow 0.750 m³/s, concentration jump 1,333 CFU/100 mL and added load 10,000,000 CFU/s. Every Logbook row has flow. The Refine example's 13.3 billion is not reproduced by the model, so it was not copied. The quiz-specific 20% rule and Claim narration are removed under the Curiosity override.
3. **FIXED, by removing evidence grading.** Before: `before-flood-evidence.json` records `validEvidence` accepting all eight entries for A, D1 and D2. After: `remaining/check-three-selections.png`, `check-three-selections.json`: tapping three log rows leaves exactly two selected for numerical comparison. There is no validator or correctness result that an oversized set can pass.
4. **FIXED.** Before: `before/feedback-680.png`, `before-feedback-680.json`: feedback bottom 522 in a 425-high viewport; the 1366 blanket frame also clips feedback. After: `verification/verify-compare-680.png`, `verify-compare-680.json`: the result appears above the entries, y=202.8–335.0. At 1366 it is y=349.4–481.6, and at 375 y=299.7–473.5. Claim feedback itself is removed.
5. **FIXED.** Before: `before/result-1366.png`, `before/result-680.png`, `before/result-375.png` cover sampling stops. After: `final-map/final-map-1366.png`, `retouch/final-map-680.png`, `retouch/final-map-375.png`: a reserved strip outside the map, zero intersection at all three sizes. Selecting another stop fades prior values and explicitly labels them Previous until the next collection. Opacity 0.35 and the Previous caption are recorded in `last-fade-1366.json`, `last-fade-680.json` and `last-fade-375.json`. The held-pointer transform bug discovered during this fix was corrected; real desktop and iframe clicks were re-tested.
6. **FIXED.** Before: `before/reveal-leaks.png`, `before-reveal-leaks.json`: 22 Logbook rows despite only two collected entries. After: `remaining/check-no-ledger-leak.png`, `check-no-ledger-leak.json`: collect once, open the ledger, switch views and open Logbook; one collected entry, one row and one flag. The ledger never mutates the sample list.
7. **FIXED.** Before: `before/restart.png`, `before-restart.json`: one tap clears the sampled case with no dialog. After: `remaining/check-clear-confirm.png`, `check-clear-confirm.json`: one entry remains while the count-specific confirmation is open. Close keeps one; confirming removes it and its flag (`check-clear-cancel.json`, `check-clear-applied.json`). Restart and solved status are absent; the simulator stays open.
8. **FIXED, by removing the lock.** Before: `before/default-lock.png`, `before-default-lock.json`: disabled Fix-it, empty title, live-looking styling. After: `remaining/check-keyboard.png`, `check-keyboard.json`: Tab, Tab, Enter enters Interventions before any samples. The open simulator has a working selected-state light. No case-solving prerequisite remains.
9. **FIXED under the Curiosity voice rule.** Before: `before-extra/submitted-five.png`, `before-extra/test-five.png` and logs show repeated instructional events; two automatic repetitions started at the requested 2-second pace. After: `verify-voice.json`: one first hint and one Read; five Test plan presses cause zero automatic how-to or failure events. The requested goal-based noPlan wording is intentionally omitted. After the first hint, speech requires Read.
10. **FIXED.** Before: `before-result-1366.json`: no live region. After: `verify-live-flow.json`: dedicated `aria-live="polite"`, atomic status, “S7, dry day: E. coli 1,441 CFU/100 mL, above the 410 reference.” `verify-dry-pipe.json` announces absent flow without treating it as a zero concentration.
11. **FIXED.** Before: `before-gauges.json`: “Remove Fence & troughs” omits cost. After: `verify-all-costs.json`: all nine names contain Add/Remove, name and dollar cost, including “Remove Fence and troughs, $60,000”.
12. **FIXED.** The two builder-log paragraphs and obsolete Claim/reveal instructions were removed from notes.md. Its modes now describe the station, collected-only Logbook and open simulator, and retain the plain upstream-only shares sentence. See notes.md, `notes-cleanup.json` (zero occurrences of all three leaked phrases) and `check-no-ledger-leak.json`; the old notes were read before the rewrite.

## Polish accepted

1. **FIXED.** `remaining/check-field-art.png` and `check-field-art.json`: 481 mg/L is in the over-400 historical band, described as poor fisheries at best. Manual lists all four bands with their historical and normally-prevailing-condition caveats. Numerical facts were checked against EIFAC, EPA and BC; no FAO document content or dataset is bundled.
2. **FIXED.** `focus-v2/focus-default.png` and JSON: no selected stop and Take sample disabled. The readout says “Tap a spot on the map first.”
3. **NOT FIXED as requested, intentionally superseded.** A Solved stamp would restore a graded finish. The explicit user instruction forbids that. The source and `verify-numbers.json` show no solved state, claim check or victory stamp. Interventions is available immediately.
4. **FIXED.** `retouch/final-fix-375.png`: no Change/0% collision. Sediment cut is a separate readout below the dry/storm table. The phone label column and headers were also adjusted to keep Storm separate from its values.
5. **FIXED.** `retouch/final-fix-375.png`, `final-map/final-map-1366.png`, `remaining/check-plans.png`: E. coli and sediment use whole numbers throughout; phosphorus uses three decimals. Calculations retain unrounded values.
6. **FIXED.** `verification/verify-compare-1366.png`, `remaining/check-plans.png` and intervention frames use sediment for the measured quantity. Bare soil remains the correct land-surface description and texture identifier.
7. **FIXED.** `retouch/final-map-680.png`, `retouch/final-map-375.png` and `final-map/final-map-1366.png`: the Plant label is off the creek and clear of sampling-stop labels. Final compact positions, including both dry and storm flags, are proved by `flags-stops/flags-stops-680.png`, `flags-stops/flags-stops-800.png`, `flags-stops/flags-stops-1000.png` and `final-phone/final-phone-flags.png`.
8. **FIXED.** `retouch/final-map-680.png`: Construction stays on one line. There is no narrow accusation grid forcing a mid-word break.
9. **FIXED.** `verification/verify-empty-compare.png`, `verify-empty-compare.json`: one entry shows “Take two samples to compare.” and leaves Compare selected disabled.

## Settled calls

- Preserved the title, synthetic flows, loads, costs, reduction factors, advisory and illustration credits. The advisory changes access and removes no pollutant. The model agrees with its independent Python implementation across all 512 intervention sets, with 88,576 comparisons and zero concentration error (`numeric-verification.json`).
- Kept HS-ESS3-4 and HS-ETS1-3 in notes: users change technologies and compare measurements, priorities, cost and who pays. No required goal or explanation gate is introduced.
- The user's Curiosity instruction supersedes all settled calls about solving, earned disclosure, goal bars and locked Fix-it. Original spec and refine.md remain untouched. Their three former open questions remain settled: title retained, advisory retained honestly, synthetic inputs labeled.
- Manual and maker's plate occupy the lower-left station corner. Power controls sit on the station, without kit CSS or a header. Neither the spec nor docs/CURIOSITIES.md assigns this tool a number, so `plate: null` and an unnumbered plate avoid inventing one.

## Cheats tried

- Empty submit, all seven accusations, and blanket evidence are removed action paths: there is no submit or grading API. Reading the ledger intentionally explains an open model; it does not pass anything or mark a source proven.
- Select every collected sample: only the last two remain selected; no pass/fail is emitted. Mixed weather, different forks, dry Pipe and beach-only tests are identified in comparisons.
- Turn every intervention on: $4,100,000, measurements remain usable. Advisory changes no concentrations. Cost is a comparison reference, not a score.
- Rapid input: 120 collections and 180 toggles in 68.8 ms of handler execution; all outputs finite, no exception, no frozen state (`check-extremes.json`). No outside HTTP resources were requested.
- Keyboard-only Map-to-Interventions, Motion off and grayscale retain operation and D/S flag letters. Read with Sound off still logs a Read (`check-keyboard.json`, `check-gray.json`, `check-read-silent.json`).

## Voice walk

At a 2-second pace with 120 ms held clicks: stop, collect, next stop, collect, Interventions, five Test plan presses, Read. Log order: initial hint once; no extra automatic instruction; current intervention instruction on Read. Sound-off Read also works. All six final entries in voice/lines.json equal `allLines()` (`post-voice.json`). The shortened first hint is "Tap a spot on the map."; its log contains only that hint and the requested Read, despite five Test plan presses. Browser fallback only; no recorded-bank timbre or actual audible quality is claimed from the muted browser log.

## The real material

Re-checked 6 November 2026 local time; raw fetch timestamps are 7 November UTC. Gathering used bounded downloads and stayed below the brief's 45-minute gathering allowance. `data/manifest.json` records URLs, byte counts, hashes and sampling; `gather_references.py` reproduces the archives. NEPIS PURLs returned HTML redirect stubs, explicitly identified in that manifest; browser source extraction supplied the text check. No executable or third-party monitoring dataset was downloaded. Reference numbers are packed inline in src.html.

| Material | Source and independent check | Licence and use |
|---|---|---|
| Network, all sample values, flows, loads, areas, prices, efficiencies, advisory duration and who-pays assignments | Original Curio Class spec.md; independently recomputed by watershed_numbers.py and check_numbers.py | Original content CC BY 4.0; code MIT. Entire synthetic dataset, no sampling and no claim of real observations. |
| E. coli 126 GM / 410 STV | EPA 2012 RWQC, recommendation 1: https://www.epa.gov/sites/default/files/2015-10/documents/rwqc2012.pdf ; WHO (2018), table B1: https://www.who.int/docs/default-source/wash-documents/who-recommendations-on-ec-bwd-august-2018.pdf | U.S. government numerical facts, public domain. WHO used only to verify; no WHO material imported. No universal single-sample closure or safety claim. |
| Nitrate-N 10 mg/L | EPA National Primary Drinking Water Regulations: https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations ; USGS Circular 1350 FAQ: https://water.usgs.gov/nawqa/nutrients/pubs/circ1350/faq.html | U.S. public-domain reference facts; drinking water only. |
| Phosphorus 0.050 mg/L | EPA Gold Book (1986): https://www.epa.gov/sites/default/files/2018-10/documents/quality-criteria-water-1986.pdf ; USGS Circular 1136: https://pubs.usgs.gov/circ/circ1136/circ1136.html | U.S. public-domain numerical fact. Clearly historical guidance, not a universal current standard. |
| Sediment bands 25, 80, 400 mg/L and their meaning | EIFAC Technical Paper 1 (1964; 1965 journal version): https://www.fao.org/4/al950e/al950e00.pdf ; EPA-600/3-77-042: https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9101Y9JU.TXT ; BC WQG-18 (2023): https://www2.gov.bc.ca/assets/gov/environment/air-land-water/water/waterquality/water-quality-guidelines/approved-wqgs/bc_env_turbidity_waterqualityguideline_technical.pdf | Public-domain numerical facts, paraphrased in original wording. No FAO/BC prose, figure or dataset imported. No permissive licence was established for the FAO document, so none of that document is bundled. Tentative historical interpretation, with species and duration limitations stated. |
| Intervention types | EPA agricultural guidance (2003), urban guidance (2005), construction permit, nutrient-removal reference (2008), BEACH Act; NRCS standards 382/390/605. Verified agriculture: https://www.epa.gov/sites/default/files/2015-10/documents/chap4e.pdf and https://www.epa.gov/nutrientpollution/sources-and-solutions-agriculture | U.S. government reference material, public domain. These support types of measures only; all numerical performance and cost assumptions remain synthetic. |
| 22 retained illustrations | Existing prompts.json provenance: FLUX.1-schnell and OpenAI gpt-image | Original Curio Class asset content, CC BY 4.0; FLUX model Apache 2.0. Both original credits retained; no new painted art or external photograph. |

## Short test

Paced exploratory runs and their observed duration: 616.286 seconds total (10 minutes 16 seconds), 287 held actions: `play-student-sampling.json`, `play-adult-interventions.json` and `play-independent-route.json`. All three walks had zero browser errors. These are automated held-input walks assessed from the grade-12 and adult perspectives, not a classroom user study.

- Would a kid open it unassigned? Yes for someone curious about the map: collection pays off without first opening a case or reading instructions. The strongest moment is the dry/storm change in the same reach.
- Would an adult play for fun? Yes: compare load against dilution, then try cost and intervention alternatives. The instrument has less sensory immediacy than Beat Lab; its interest is investigative.
- Is the real material the interface? Yes for the mass-balance rules and unit-bearing measurements; the place and inputs are explicitly synthetic, not field data.
- Does it work without a score or finish? Yes. Sampling, ledger and interventions stay open; no correctness, solved status, winning plan or finish screen exists.

Frame comparison: `final-map/final-map-1366.png` beside `before-extra/model-beat-lab.png`; also inspected and used Elements Inspector, Span and Spire and Pocket Universe before designing the station. Both expose their subject directly through working controls. The new map and lower station replace the old right-hand lesson panel.

## Lesson creep check

The requested search terms (score, points, level, goal, sticker, badge, correct, wrong, try again, complete, well done) produce no hits in src.html or voice/lines.json. Implementation names from the old claim/goal controller were removed. Soil is retained only for land-surface descriptions and the SVG texture id. No em dash was added. `final-files.json` records the file hashes and contrast checks: primary ink 13.63:1, readout units 9.78:1, sample values 9.39:1, primary button 6.98:1 and plate 4.79:1.

## Engine changes wanted

None.

## Audit

The one full audit completed within its 2,400-second limit: `fix-audit-r1/audit.md`, 79 leads, zero console or resize errors and a clean Motion-off check. Its 24 frames were inspected through four native contact sheets and critical full-size frames. `audit-input-files.json` records the audited snapshot. The audit correctly found compact target/label crowding, an all-interventions gauge-row expansion, small Manual links and a first hint naming a disabled control. Those were fixed and checked with scoped drives; no second full audit was run.

All 79 leads are individually answered in `fix-audit-dispositions.csv` and JSON: 38 FIXED, 34 INTENDED, 6 CURIOSITY OVERRIDE, 1 ACCEPTED BASELINE 16, zero unclassified. The 34 intentional cases are background controls covered and inert under native dialogs, secondary scrollable Manual references and the suppressed generic compact power-panel hint (local readouts, Read and Manual remain available). The six welcome leads presume a lesson premise; the Curiosity intentionally has only one optional first hint. A quick repeated Map tap cutting that hint remains the accepted Baseline 16 behavior.

Final scoped proofs: all 11 stops register in order in both weathers at 680x425, 800x500, 1000x625 and 375x812, with zero target intersections or label/flag collisions (`flags-stops-680.json`, `flags-stops-800.json`, `flags-stops-1000.json`, `final-phone-flags.json`). The last phone proof also checks source labels against each other and the legend, after direct frame inspection found and corrected Geese touching the legend. Earlier `post-stops-680.json` retains the intermediate Plant collision honestly; the final flags proof supersedes it. Other shapes have all-stop checks at 760x900 and 1366x768. Pulse placement now follows actual target rectangles.

Both all-nine-intervention layouts have zero control intersections, 44 px minimum control heights and an enabled Test plan at $4.1m (`post-all-fixes-680.json`, `post-all-fixes-375.json`). All five Manual links have 44 px heights at both widths (`post-links-*.json`). Sound toggling moves no power control (`post-power.json`). Final voice equality and first-hint/Read-only behavior are in `post-voice.json`; the full assertions are in `post-audit-validation.json`. These final frames were opened and inspected. `final-files.json` records final hashes and the 722,556-byte bundle. `final-port-check.json` confirms the test browser ports and host are closed. No app external HTTP resource was requested; the iframe host is local.

## Left open

- Accepted polish 3 is intentionally not applied: no Solved stamp, as the user explicitly requires a Curiosity.
- No plate number exists in the supplied owner documents; the plate is unnumbered pending owner allocation.
- The source FAO document has no verified permissive licence. Only independently checked numerical facts and original paraphrases are used; no FAO asset is included.
- This Windows Chrome check does not establish Chromebook frame rate or classroom engagement. Speech used browser fallback, not recorded bank timbre.
