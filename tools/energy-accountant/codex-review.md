# Codex review: energy-accountant

## Played

Cold Grade 9 solo run of all five scenes, wood prediction, ten passport stops, both cells and NOAA raw/swing/table; then a projector-sized walk. Played before reading builder notes or source. Strong illustrations and oxygen contrast; passport was the flattest stretch.

## Findings fixed

- **Blocker, general, Oxygen compact meter:** hidden assumptions and clipped fuel icons could make 16 look like eight. Kept units beside counts, drew all sixteen small icons, and wrote the undrawn remainder. Equal-ATP wording replaces a misleading cumulative comparison.
- **Should fix, general, Ledger nitrogen:** N/H particles started outside the scene because their source was hidden. Visible Soil N / Dietary N accounts now supply them; notes explain the atom-summary model.
- **Should fix, general, carbon bars:** Air saturated at its initial 600 C and could not grow at night. Bars now show each account's share of actual scene carbon; the night bar grows 98.0392% to 99.0196% after one respiration.
- **Should fix, general, night narration:** “only respires” excluded the available synthesis action. Reworded to “still respires”; lines.json matches allLines exactly.
- **Should fix, general, wood hint:** changing a revealed prediction left Read's hint stating the previous answer. Sliders now restore the prediction instruction; reopening an existing result preserves the result hint.
- **Should fix, general, stale voice:** the changed night instruction continued after entering the passport, and woodReveal continued during a new prediction. Entering either subview stops old speech; resuming prediction invalidates and stops the old reveal. Final passport return restores its end-specific hint. Focused before logs proved both stale clips; focused rechecks now stop both stale clips and retain the matching hint.
- **Should fix, general, voice inventory:** fixed Read-only hints and cell/refusal variants were absent from the narration inventory. Registered the existing sentences without changing their playback; 36 unique prepared lines now cover all fixed speech and Read hints.
- **Polish, general, Oxygen art:** capped waste dots covered the compact cell. Smaller foreground particles preserve the cell illustration.
- **Polish, general, passport:** joined the stamps into a trail, added a current-stop C marker, quiet carbon light and restrained arrival motion. Replaced the weakest art, a flat sugar glyph, with a shaded fuel token, explicitly not a molecular diagram.
- **Polish, general, notes/metadata:** corrected the current OpenStax attribution and removed duplicated refusal wording.

## Findings left

No blocker or should-fix finding remains after the scoped rechecks.

- Nit: the fixed passport is still mostly Next stamp. That follows the prescribed route; no new quiz or branching feature added.

## Break it

- No score, best score, graded quiz, mastery claim or reflection gate exists. Balance checks report chemistry, not learning credit.
- Wood: wrong 10/65/25 and 0/0/100 guesses, five repeated Checks, actual jittered end-to-end drag and 303 integer settings. Every reveal remains 93.3/6.7/0 with no reward; sums stay 100. New prediction hides the old reveal.
- Ledger: rapid photo/respire rhythm, all unaffordable entries, night depletion and no-light attempts. Exactly eight valid rhythm rows and two night rows; refused taps add nothing. Independent 750-attempt run: 87 accepted, 663 refused, no negative accounts or conservation errors.
- Energy checks: all eight equations independently parsed in C/H/O/N/Ca; every numerical posting satisfies input = retained + ATP + model heat. Synthesis stays not quantified.
- Oxygen meters: all 32 cell/oxygen/work combinations, quarter-glucose input, unequal totals, mixed waste, repeated Run and real Work drag. Work 64 / no oxygen / ten muscle ticks: 320 glucose, 640 ATP, 640 lactic acid, 855,680 kJ retained. No cap on numerical totals.
- Live Run: after one aerobic row, switching Oxygen off produced lactate on the next row; switching Cell then produced ethanol on the next row. Ten rows total. Remainder text makes drawn caps explicit.
- Planet: toggle every station off, switch raw/swing repeatedly, and reveal the conclusion without an answer. Empty chart says no stations; fixed axes and source values remain honest. This is an unscored evidence reveal.
- Passport: rapid Next / restart supplies no mastery badge; ten stamps still visit atmosphere, biosphere, hydrosphere and geosphere.

## Voice walk

Held 0.12 s clicks, 2 s pace, default Muscle/Work 32. Day -> Photo twice -> Respire -> Photo -> Respire -> Oxygen -> Tick -> oxygen off -> Tick -> Run -> Tick twice -> Planet -> station -> Swing -> conclusion.
Actual spoken order: welcomeLedger, welcomeOxygen, oxygenOff, welcomePlanet, planetResult. All five completed without a cut; every mode introduction heard once.
Side walk: night, passport, passportDone. The final transition guard deliberately stops night at passport entry. Read interrupts current speech, works with Sound off, and mode changes release Read promptly.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Each mode introduction | how/welcome | 1 | 1 |
| woodAsk | how | 1 | 1 |
| woodReveal | event, five Checks | 5 | 5 |
| night / passport | how | 1 each | 1 each |
Final logs: main-voice-final.json, night-to-passport-fixed.json, wood-repredict-fixed.json, wood-five-final.json, passport-repeat-final.json. Earlier short log captured only four queued reveals; waited for queue completion and verified all five. Chrome was muted; these verify scheduling, not subjective voice timbre. Read inventory checked against actual default/refusal playback.

## Facts checked

- Photosynthesis net equation, light into sugar, O2 from water, respiration in plants day/night: [OpenStax Biology 2e 8.1/8.2](https://openstax.org/books/biology-2e/pages/8-2-the-light-dependent-reactions-of-photosynthesis). Gross water exchange and net cancellation distinguished.
- Muscle glycolysis/fermentation makes two ATP and lactate; yeast makes ethanol plus CO2: [OpenStax 7.5](https://openstax.org/books/biology-2e/pages/7-5-metabolism-without-oxygen). Lactic-acid formula is the spec's neutral counting convention, not a claim about dominant cellular protonation.
- Variable aerobic ATP yield and approximately 34% standard energy capture: [OpenStax 7.4](https://openstax.org/books/biology-2e/pages/7-4-oxidative-phosphorylation); 32 is the stated model, not universal cell yield.
- ATP standard free energy 30.5 kJ/mol: [OpenStax Organic Chemistry 29.1](https://openstax.org/books/organic-chemistry/pages/29-1-an-overview-of-metabolism-and-biochemical-energy). 32 x 30.5 = 976; 2 x 30.5 = 61, recomputed.
- Glucose oxidation 2,870 kJ/mol: Campbell 12e ch.9 in spec, independently corroborated by [Georgia State University HyperPhysics](https://hyperphysics.phy-astr.gsu.edu/hbase/Organic/sugar.html). Residual model heat 1,894 kJ; this is not a cellular calorimetry measurement.
- Fermentation standard releases 196/235 kJ/mol: Lehninger 8e ch.14 in spec, corroborated by [IGNOU Unit 6, Respiration, section 6.3.3](https://egyankosh.ac.in/bitstream/123456789/7529/1/Unit-6.pdf). Recomputed heat 135/174, retained 2,674/2,635 and lactate capture 31.1%. Original book passages not re-accessed.
- Rounded masses C12/H1/O16/N14: [NIST](https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses). C72 + H12 + O96 = 180 g/mol; 168/180 = 93.3%; 12/180 = 6.7%; both equation sides 372 g. Glucose model, not total wood composition.
- All 36 monthly observations match current [NOAA MLO](https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt), [BRW](https://gml.noaa.gov/aftp/data/trace_gases/co2/in-situ/surface/txt/co2_brw_surface-insitu_1_ccgg_MonthlyData.txt) and [SPO](https://gml.noaa.gov/aftp/data/trace_gases/co2/in-situ/surface/txt/co2_spo_surface-insitu_1_ccgg_MonthlyData.txt) files, retrieved 2026-11-08. Early MLO observations at Maunakea are already disclosed.
- Independent annual-baseline calculation: BRW minimum -12.72625 August, range 19.06083; MLO range 6.51167/minimum September; SPO range 1.0675/minimum March. Display rounding 19.1/6.5/1.1 verified; snapshot date visible.
- All nine annual reference means also match means recomputed from the current NOAA 2022/2023/2024 monthly records after rounding; review-annual.json preserves the comparison.
- Northern summer photosynthesis drawdown and smaller southern swing: [NOAA GML](https://gml.noaa.gov/ccgg/ggrn.php). Descending months and lowest concentration are distinct; prompts ask both.
- Carbon reservoirs, ocean bicarbonate, shell carbonate, limestone residence and volcanic return: [OpenStax 46.3](https://openstax.org/books/biology-2e/pages/46-3-biogeochemical-cycles) and [NASA carbon cycle](https://science.nasa.gov/earth/earth-observatory/the-carbon-cycle/). Both carbonate equations balance atoms and charges. No blanket claim that weathering emits CO2.
- Sucrose condensation and alanine atom summary independently balanced; no invented synthesis energy. Nitrogen origin is labeled as simplified counting, not a single actual pathway.

## Sensitivity

Muscle-cell/body content: a biological reviewer should confirm the cutaway and the distinction between this standard free-energy model and health advice. No diets, body judgments or people images. Utqiagvik names a station location, with no claim about its Indigenous community; all assets are people:false. No religion or hard history.

## Flattest moment left

The Planet prompts rely on the student's explanation, without automated feedback. This fits the spec's unscored evidence mode. The fixed passport is clearer and richer but remains a prescribed journey.

## Graphics

All fifteen finished assets inspected at use size: five landscapes, two cell illustrations, five 160 px stamps and three station thumbnails; one consistent naturalistic style, no missing tokens or people. Preserved all paintings. Redrew code sugar art and improved passport/waste staging. Art 609.3 KiB; final bundle 1235.8 KiB.
Beat Lab and Snowy Mail Route opened from scoped mirrors for the finish comparison; no changes to their folders. Grade 9 ledger art remains rich and its payoff stays explanatory.

## Audit

One complete audit, within its 40-minute limit; 129 frames, 111 mechanical leads. All frames inspected on state sheets; suspect 680/1366/760 ledger and 375 table frames also opened natively. Disposition record: _scratch/energy-accountant/review-audit-dispositions.md.
Confirmed expected: covered background hint in the native wood dialog, old rows masked by opaque sticky headings, phone chart masked by its opaque table view, allowed first-tap welcome skips, and an empty scroll region. The modal keep expectation is now scoped correctly. No tool errors, lost settled focus, repeated how-to or resize failures remain.
The audited bundle preceded the narrow voice-transition guards and completion of the fixed Read-line inventory. Rebuilt and rechecked the two stale paths, passport return/repeats, five wood events and the full main voice path. No second audit or polish pass.
Keyboard-only three valid postings and stable focus; grayscale retains letters/shapes/dashes; Motion off has zero animations and preserves posting time. All controls meet 44 px; hints and main actions in view.
Computed AA contrast: brand/panel 8.39:1; dark text/brand 8.81:1; hint/panel 13.32:1.
Done when 1-6: PASS, balanced postings and 6 C transfer; invariant wood reveal; correct oxygen fuel/waste; NOAA swing minima/ranges/date; ten four-sphere stamps; truthful unavailable-entry reasons.
Done when 7-11: PASS, primary controls and internal tables at required sizes; how/event voice counts; dominant scene/counters/chart; exact-once rapid posting and next-tick live changes; all fifteen images and an offline, em-dash-free bundle.
Wave checks: current hints/Read; retained focus; short choice sets visible; no answer/score giveaways; honest units/assumptions; all five standards practiced; Motion off; resize during running actions; no late welcome; unknown energy labeled; distinct line/atom encodings; truthful balances; hints restore; no word-copy quiz.

## Left open

Spec choices retained unattended: seasonal NOAA overlap with climate-dashboard and the labeled alanine summary; no new feature or kit change. STANDARDS timing overrides the spec's instant Motion-off wording. Voice remains browser fallback; no recordings requested or made.
No commits, deployments or changes outside the two authorized folders. All owned Chrome/server endpoints are closed; host.html is absent. Report held in Scratch until completion to honor the explicit stop boundary.
