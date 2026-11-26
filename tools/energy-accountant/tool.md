# Energy Accountant: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: energy-accountant

#### Built
Grade 9 biology bookkeeping in three modes: Ledger, Oxygen switch and Planet's books. Five painted living scenes,
lettered moving atoms, stocked accounts, a real scrolling reaction ledger, an unscored wood-mass prediction, ten carbon
passport stamps, live oxygen/work experiments and a NOAA seasonal graph. Starter-derived, kit narration and DataTable/Chart.
Build only. No commits or polish round. Writes confined to the tool and its Scratch folder. Chrome 9980-9987; host 8785.

#### Numbers check
Independent Python parsing checked all eight equations in C/H/O/N/Ca before implementation; numbers.json preserves results.
- Photosynthesis and respiration: C6 H12 O18 each side; sucrose C12 H24 O12; alanine summary C6 H18 O6 N2.
- 32 x 30.5 = 976 kJ ATP; 2870 - 976 = 1894 heat; efficiency 34.00697 percent.
- Fermentation ATP = 61; muscle heat 196 - 61 = 135, retained 2870 - 196 = 2674.
  Yeast heat 235 - 61 = 174, retained 2870 - 235 = 2635. 61/196 = 31.12245 percent.
- Glucose: 72 C + 12 H + 96 O = 180 g/mol. Air 168/180 = 93.3333 percent; water 12/180 = 6.6667.
  Reactants 264 + 108 = products 180 + 192 = 372 g with rounded teaching masses.
- Exact annual differences: MLO 3.035 and SPO 2.825 ppm/year before rounding. BRW swing minimum -12.72625 in August,
  range 19.060833; MLO range 6.511667, minimum September; SPO range 1.0675, minimum March. All displayed values match.
- Sucrose and alanine energy remain explicitly not quantified. No invented energy used to make totals pass.

#### Facts checked
- Photosynthesis uses light and carbon dioxide; released oxygen originates in water. OpenStax Biology 2e 8.2,
  https://openstax.org/books/biology-2e/pages/8-2-the-light-dependent-reactions-of-photosynthesis . Net equation is on
  screen; gross water exchange in the animation preserves the oxygen-origin lesson.
- Respiration continues in plants at night; muscle fermentation retains carbon in lactate, yeast produces ethanol and
  CO2; fermentation yields two ATP and leaves energy in products. OpenStax 7.5,
  https://openstax.org/books/biology-2e/pages/7-5-metabolism-without-oxygen . Fermentation is not framed as a bad choice.
- Numerical free energies and approximately 30-32 ATP: supplied Campbell Biology 12e ch. 9 and Lehninger 8e ch. 14
  citations in the spec. Arithmetic independently verified; the original book passages were not re-accessed.
  The interface labels this standard free-energy bookkeeping, not a measurement of cellular heating.
- Air, living things, ocean, shell carbonate and limestone as carbon reservoirs; dissolution and carbonate atom/charge
  balance; volcanic return to air. OpenStax 46.3,
  https://openstax.org/books/biology-2e/pages/46-3-biogeochemical-cycles . Final return uses volcanism, not a blanket
  claim that weathering releases CO2. The passport is explicitly one possible journey.
- Seasonal northern summer drawdown, year-round respiration and smaller opposite southern season: NOAA GML,
  https://gml.noaa.gov/ccgg/ggrn.php and https://www.gml.noaa.gov/infodata/isotopes/c13tellsus.html .
- Monthly NOAA means, annual baselines and snapshot provenance: spec's frozen 2026-10-27 BRW/MLO/SPO dataset. MLO source
  https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt checked, including early-2023 Maunakea collection during
  the Mauna Loa closure. BRW/SPO endpoints could not be accessed by the verifier; do not call those a fresh download.
- C12/H1/O16/N14 are rounded teaching masses, with NIST attribution as supplied in the spec,
  https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses . Glucose percentages were
  recomputed, not copied as wood composition. Soil minerals remain necessary; plant nitrogen is an explicitly simplified NH3 count.

#### Break it
- No score, mastery badge, best result or reflection gate. Wood Check always reveals the source-based answer,
  including a deliberately wrong 100 percent air prediction. Sweeping it cannot earn credit. 303 slider settings
  remained integer, bounded and summed to 100; a real jittered drag reached [0,0,100] and revealed the same explanation.
- Atom/energy balance indicator: tried free respiration, synthesis without sugar, repeated rapid entries and depleted
  opening stocks. Independent destination expectations plus 500 attempts: 131 valid, 369 refused, no negative stocks,
  no atom difference. A fixture initially omitted alanine Body N+2; fixed the independent fixture, then zero failures.
- Oxygen counter: tested all 32 cell/oxygen/work combinations, quarter-glucose work, mixed cell waste, high work and
  repeated Run. Counts record actual ticks, not imaginary equal runs. Work32 on/off uses 1/16 glucose for equal32 ATP.
  High-work yeast ten ticks gives 320 glucose, 640 ATP, 640 ethanol, 640 CO2 and 843200 kJ retained. Drawing caps do not cap totals.
- Switching off and changing cell/work during real Run changed the next tick; final 10-row trace saved. Second entry
  during animation committed the first exactly once. Motion off still waits 1.5 seconds; Clear cancels its pending timer.
- Planet station sweeps cannot rescale axes. All curves can be hidden without inventing data. No answer is graded;
  the explicit scientist conclusion is a teaching reveal, not earned approval.

#### Voice walk
Held clicks0.12s, normal2s tap pace, default Work32/Muscle. Initial short main walk started Ledger welcome, Oxygen
welcome, Oxygen-off event, Planet welcome and scientist result in that order. It left modes before two clips finished;
the Oxygen event also unnecessarily cut its introduction. Removed that pre-emption and verified welcome then event
complete with no cut. Deliberate mode switches continue to discard stale narration as STANDARDS requires.
Complete main path: Day -> Photo -> Photo -> Respire -> Photo -> Respire -> Oxygen -> Tick -> oxygen off -> Tick
-> Run -> Tick -> Tick -> Planet -> station -> Swing -> conclusion. Same2s pace, seventeen held taps. All five lines
in the order above completed with no cut, including every mode introduction. voice-main-complete.json preserves the log.
Side path: Night -> Respire -> Ledger -> Follow carbon -> nine Next stamps. Log order: night, passport, passportDone,
all complete. Five wood Checks2s apart produced woodReveal-1 through woodReveal-5, all complete after the queue drained;
the obsolete slider instruction stops at Check. Four0.7s repeated selections each produced one uncut introduction.
Sound-off/Read path speaks the current hint, queues no consumed silent welcome, and Read intentionally interrupts speech.
Logs are browser playback records with Chrome muted; they verify scheduling, not subjective recorded-voice quality.

#### Feel check
Best moment: keep Work32 and switch oxygen off. The same ATP buys a sixteen-hexagon fuel pile and a growing waste pile,
while the retained-energy figure makes the biological cost concrete. Then yeast changes both the painting and products.
Flat moment one was a number-only energy result: replaced it with a persistent, proportionate stored/ATP/heat strip.
Flat moment two was a crowded passport over the account ring: gave it the stage, larger paintings, short stamp captions
and stable surrounding controls. The strip follows the current stamp; Back to ledger remains in view.
Played the scene, respiration/fermentation, wood, passport and seasonal comparison paths. Later scenes change available
reactions and stocks; later Oxygen ticks accumulate the consequences of the student's actual choices. No fabricated win.
bar-comparison.png places deer fermentation beside Beat Lab. Both bar tools were opened from Scratch mirrors.
The five naturalistic scenes and textured cell paintings hold their own against that finish; this is a scientific ledger,
so its reward is an explanatory record rather than confetti. All fifteen images teach or locate something.

#### Done when
1. PASS: all entries balance, independent 500-attempt property run; photo Air C decreases6 and Sugar C increases6.
2. PASS: 303 slider cases plus real drag; invariant 93.3/6.7 reveal, no score.
3. PASS: 32 oxygen combinations and quarter/high-work frames; Work32 1/16 glucose, muscle32 lactate; 2674/2635 per glucose.
4. PASS: independent NOAA calculations and Swing frames; -12.7 August, ranges19.1/6.5/1.1, SPO March; data date visible.
5. PASS: real nine Next-stamp clicks, ten visited stamps and all four named spheres. Final compact frame inspected.
6. PASS: Night gives No light, exhausted Respire gives No sugar to burn; guarded transactions refuse either input.
7. PASS: every desktop size in every mode; focused final680/760 fixes; hosted375 all three modes, zero global horizontal
   overflow, controls/hints in view, table scrolls internally. The full audit's iframe lookup failed; separate host checks passed.
8. PASS: five-repeat audit how-to checks clean; five distinct wood reveals fully spoken; Night guards check available sugar
   at start and hush it if the final sugar is spent. Repeated current-selection cuts repaired; Read interrupts intentionally.
9. PASS: actual frames1366 and680 show scene/accounts, counters and chart as the dominant area in their respective modes.
10. PASS: real held second entry, exact-once transaction and live Run trace; oxygen/cell change immediate, next tick uses new values.
11. PASS: fifteen decoded images, no missing art tokens or external asset tags, property requests empty, no em dashes.

#### Wave lessons
- Hint and voice: PASS. Synchronous hint changes, current Read, V.heard selection; no input waits for speech. Five wood
  events retained, current-selection clips complete, Oxygen event waits behind its valid how-to. Stale mode narration drops.
- Focus and layout: PASS. Stable entry nodes, selected-mode guards, no load focus; audit settled Enter twice clean.
  Wood reveal button bounds unchanged; passport selector/panel stay fixed. Energy labels separated after audit.
- Sizes: PASS. Seven desktop sizes once per mode, audit state sweep, focused680/760 fixes, actual375 host checks.
- No giveaways: PASS. No score or gated approval. Tried wrong wood percentages and slider sweeps; invariant unscored reveal.
- Honest numbers: PASS. Opening stocks, per-posting kJ, actual ticks, continuous fuel and drawing caps labeled.
  Unquantified synthesis energy disclosed; totals are reaction flows, not account stocks.
- Standards: PASS. Solo photosynthesis supports HS-LS1-5; sucrose/alanine atom synthesis HS-LS1-6; oxygen experiment
  HS-LS1-7 and HS-LS2-3; four-sphere passport and seasonal evidence HS-LS2-5. No unearned standard or family claim.
- Motion off: PASS. Audit no infinite loops; final check zero animations, pending until1.5 seconds and no post-Clear callback.
- Short choices visible: PASS. Scene buttons, reaction set and mode controls in view. Tables are scroll regions, not hidden choices.
- Resize mid-animation: PASS. Audit exercised every state/walk transition, no exceptions or controls left locked.
- First-tap welcome: PASS. Fixed Photo's pending-state exclusion; own-line first taps intentionally skip welcome.
- Unknown as unknown: PASS. Energy unavailable says not quantified; station toggles show selected/hidden state.
- One look, one meaning: PASS. C/H/O/N letters, energy labels, line shapes/dashes and text distinguish values without color.
- Badge says what is true: PASS. Atom balances checked independently; energy partial status is explicit. No mastery badge.
- Hint changes back: PASS. Mode/scene/oxygen handlers synchronously replace it; Read uses current hint.
- No answer by word copying: PASS. No scored text-matching choice. Scientist conclusion and wood reveal are explicitly instructional.

#### Audit leads
One audit, exit0, about33 minutes, 99 frames, 132 leads. No runtime exceptions or disabled leftovers after resize.
audit-dispositions.md/.json in Scratch answer every non-clean bullet A001-A127, plus every walk-table finding.
- A001-A003: fixed Read minimum44px. A004-A005: iframe lookup failure answered with independent successful375 host run.
- Singular count leads: fixed 1 entry. Energy/atom overlap leads: separate block lines. Soil title leads: hide duplicate title
  and center Soil account. Passport background overlap/panel shift: hide inactive account layer, keep selector/panel fixed.
- Wood covered #hint: native modal intentionally makes background inert; current instruction/result are inside the dialog.
- Sticky table overlap leads: opaque headings/totals mask older scroll rows. Native760/1366 Oxygen frames confirm no overprint.
- Quick same-selection narration cuts: early return on current scene/mode, empty clears preserve speech. Focused logs check guards.
- Walk Photo welcome: fixed pending exclusion. Night/Wood/Passport first taps intentionally use their own how-to, per STANDARDS.
  Read speaks its hint and Sound off stops narration. Scene-specific entry availability can change while scene buttons stay fixed.
- Ledger scroll region click is focus/scroll, not a dead action. Sound's state glyph changes header text width; focus stays stable.
No second full audit was run; only affected states and narration paths were rechecked.

#### Frames looked at
Every captured drive PNG was opened directly or on contact sheets. Sets: early8, check5, extras12, full-ledger7,
full-planet7, oxygen-a4, oxygen-b3, original phone3, failed phone-try1, drags-a3, run-check3,
final-visual9, final-phone3, final-voice-a2, final-voice-b8, final-edge4, edge-retry2. All99 audit PNGs reviewed on15 state sheets;
flagged Oxygen ledger760/1366 also opened native. Final compact posted/Soil, tall Night, synthesis, passport, wood,
calm timing and tall Planet opened native. Original overflow phone frame is retained as failed evidence, replaced by passing frames.
All15 finished WebPs inspected at their final sizes, including stamps after keying and three redraws.

#### Art made
15 selected assets from18 image generations: five1000px scenes, two800px cells, five160px keyed circular stamps,
three440px stations. Naturalistic science gouache throughout; all people:false. Art609.3KB, recorded voice0KB,
1230.1 KB self-contained bundle against the2MB goal. No placeholders. Full prompts/provenance in art/prompts.json.
Redrew Air stamp to remove landscape; Arctic and South Pole stations to remove false mountain horizons.
Only art.py --rekey used. Atom motion, precise bars, graph, accounts and countable piles are code-native.

#### Art still to paint
None. No people called for or depicted. No image generation limit or fallback placeholder remains.

#### Engine changes wanted
kit/data-desk.js Chart.drawXY: support line-series groupBy/groups/groupLabels with separate paths, symbols and dashes.
Current line renderer ignores grouping. Tool uses supported12-row pivot for chart, retains original36-row DataTable.
No kit, docs, script, other tool or engine edits were made.

#### Left open
- A very short tour that leaves a mode after a few taps can cut that mode's unfinished narration. Controls stay live and
  stale narration stops on mode change. Complete per-mode and repeated-action paths are recorded separately; no pacing lock added.
- BRW/SPO direct-download verification and original textbook free-energy passages remain unverified independently of the
  supplied spec snapshot/citations. Arithmetic and atom balance are verified. Cold science review should confirm these passages.
- No audio recorded, as required. Fifteen calm-professor lines are prepared; installed browser fallback timbre can vary.
- Audit375 lookup failed even though separate hosted375 checks passed. Some earlier Chrome/CDP batches failed transport
  startup; bounded smaller retries and final successful batches are preserved. No hidden claim those failed runs passed.
- Two final-edge iframe test snippets incorrectly looked for lexical Curio on contentWindow; their layout results were
  captured but the test waits errored. Replaced only those waits with window timers and rechecked the two affected states.
- Windows taskkill had left seven owned preview hosts alive. Exact process arguments and repository cwd were verified
  before psutil terminated them. Final inventory: no owned Chrome, no host.html, all assigned ports closed.
- Spec/open-question choices and conflicts are in handoff.md: retain seasonal NOAA overlap and labeled alanine summary;
  STANDARDS timing wins over instant Motion-off wording; user stop boundary wins over writing the report early;
  current image-tool instruction wins over the spec's older local method. Voice-only sound follows the specific spec.
- Cold review is next. No polish round, commit, upload or deployment started. Owned Chrome processes and servers closed; host.html removed and assigned ports verified closed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: energy-accountant

#### Played

Cold Grade 9 solo run of all five scenes, wood prediction, ten passport stops, both cells and NOAA raw/swing/table; then a projector-sized walk. Played before reading builder notes or source. Strong illustrations and oxygen contrast; passport was the flattest stretch.

#### Findings fixed

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

#### Findings left

No blocker or should-fix finding remains after the scoped rechecks.

- Nit: the fixed passport is still mostly Next stamp. That follows the prescribed route; no new quiz or branching feature added.

#### Break it

- No score, best score, graded quiz, mastery claim or reflection gate exists. Balance checks report chemistry, not learning credit.
- Wood: wrong 10/65/25 and 0/0/100 guesses, five repeated Checks, actual jittered end-to-end drag and 303 integer settings. Every reveal remains 93.3/6.7/0 with no reward; sums stay 100. New prediction hides the old reveal.
- Ledger: rapid photo/respire rhythm, all unaffordable entries, night depletion and no-light attempts. Exactly eight valid rhythm rows and two night rows; refused taps add nothing. Independent 750-attempt run: 87 accepted, 663 refused, no negative accounts or conservation errors.
- Energy checks: all eight equations independently parsed in C/H/O/N/Ca; every numerical posting satisfies input = retained + ATP + model heat. Synthesis stays not quantified.
- Oxygen meters: all 32 cell/oxygen/work combinations, quarter-glucose input, unequal totals, mixed waste, repeated Run and real Work drag. Work 64 / no oxygen / ten muscle ticks: 320 glucose, 640 ATP, 640 lactic acid, 855,680 kJ retained. No cap on numerical totals.
- Live Run: after one aerobic row, switching Oxygen off produced lactate on the next row; switching Cell then produced ethanol on the next row. Ten rows total. Remainder text makes drawn caps explicit.
- Planet: toggle every station off, switch raw/swing repeatedly, and reveal the conclusion without an answer. Empty chart says no stations; fixed axes and source values remain honest. This is an unscored evidence reveal.
- Passport: rapid Next / restart supplies no mastery badge; ten stamps still visit atmosphere, biosphere, hydrosphere and geosphere.

#### Voice walk

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

#### Facts checked

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

#### Sensitivity

Muscle-cell/body content: a biological reviewer should confirm the cutaway and the distinction between this standard free-energy model and health advice. No diets, body judgments or people images. Utqiagvik names a station location, with no claim about its Indigenous community; all assets are people:false. No religion or hard history.

#### Flattest moment left

The Planet prompts rely on the student's explanation, without automated feedback. This fits the spec's unscored evidence mode. The fixed passport is clearer and richer but remains a prescribed journey.

#### Graphics

All fifteen finished assets inspected at use size: five landscapes, two cell illustrations, five 160 px stamps and three station thumbnails; one consistent naturalistic style, no missing tokens or people. Preserved all paintings. Redrew code sugar art and improved passport/waste staging. Art 609.3 KiB; final bundle 1235.8 KiB.
Beat Lab and Snowy Mail Route opened from scoped mirrors for the finish comparison; no changes to their folders. Grade 9 ledger art remains rich and its payoff stays explanatory.

#### Audit

One complete audit, within its 40-minute limit; 129 frames, 111 mechanical leads. All frames inspected on state sheets; suspect 680/1366/760 ledger and 375 table frames also opened natively. Disposition record: _scratch/energy-accountant/review-audit-dispositions.md.
Confirmed expected: covered background hint in the native wood dialog, old rows masked by opaque sticky headings, phone chart masked by its opaque table view, allowed first-tap welcome skips, and an empty scroll region. The modal keep expectation is now scoped correctly. No tool errors, lost settled focus, repeated how-to or resize failures remain.
The audited bundle preceded the narrow voice-transition guards and completion of the fixed Read-line inventory. Rebuilt and rechecked the two stale paths, passport return/repeats, five wood events and the full main voice path. No second audit or polish pass.
Keyboard-only three valid postings and stable focus; grayscale retains letters/shapes/dashes; Motion off has zero animations and preserves posting time. All controls meet 44 px; hints and main actions in view.
Computed AA contrast: brand/panel 8.39:1; dark text/brand 8.81:1; hint/panel 13.32:1.
Done when 1-6: PASS, balanced postings and 6 C transfer; invariant wood reveal; correct oxygen fuel/waste; NOAA swing minima/ranges/date; ten four-sphere stamps; truthful unavailable-entry reasons.
Done when 7-11: PASS, primary controls and internal tables at required sizes; how/event voice counts; dominant scene/counters/chart; exact-once rapid posting and next-tick live changes; all fifteen images and an offline, em-dash-free bundle.
Wave checks: current hints/Read; retained focus; short choice sets visible; no answer/score giveaways; honest units/assumptions; all five standards practiced; Motion off; resize during running actions; no late welcome; unknown energy labeled; distinct line/atom encodings; truthful balances; hints restore; no word-copy quiz.

#### Left open

Spec choices retained unattended: seasonal NOAA overlap with climate-dashboard and the labeled alanine summary; no new feature or kit change. STANDARDS timing overrides the spec's instant Motion-off wording. Voice remains browser fallback; no recordings requested or made.
No commits, deployments or changes outside the two authorized folders. All owned Chrome/server endpoints are closed; host.html is absent. Report held in Scratch until completion to honor the explicit stop boundary.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Energy Accountant handoff

Build only. No commits, deployment, or polish round. All scratch material is in _scratch/energy-accountant/.

#### Source map

src.html follows the kit starter frame with kit:curio and kit:theme-912. Tool CSS lays out real-pixel scenes, account cards,
two oxygen counters and the chart. No fixed scene is shrunk to fit the preview.
reactions holds balanced equations, independent atom totals and the numerical free-energy allocations.
makeTransfer moves atoms between stocked accounts; applyEntry updates molecule stocks, work and heat.
Each scene has a separate book; all five scenes post into the Ledger mode's shared table. Oxygen mode has its own table.
finishEntry posts a pending animation exactly once before another entry or scene starts. Atom positions are measured
from live account nodes each frame, so resizing does not invalidate a mover.
Stable entry nodes use aria-disabled and a refusal reason so keyboard focus survives a stock changing.
The carbon passport is a ten-step view inside the scene stage. Scene selector and side controls keep their positions;
inactive accounts, painting, ledger table and posting status hide until it closes. It records a possible journey,
not evidence that a student mastered carbon cycling. Its strip can scroll horizontally; the next-step button stays visible.
The wood card is a native dialog. Sliders redistribute whole percentages with a largest-remainder split; Check is unscored.
tick snapshots Oxygen, Cell and Work synchronously, and increments the actual condition's cumulative counters.
Run schedules ten ticks at 400 ms; changing settings affects the next tick. Run again restarts that schedule.
The 36-row NOAA DataTable retains all source means and computed swings. Chart uses a twelve-row pivot with three numeric
series because the engine's line renderer does not implement groupBy. renderTable is read-only.
Curio.voice owns narration and Read. __tool exposes state, model functions, allLines and vlog for review.

#### Open questions resolved

- Retain NOAA CO2 in both this tool and climate-dashboard. This tool uses only the 2023 seasonal swing at three stations;
  the separate dashboard's long-term question is different. No source or station was changed.
- Retain the single alanine atom summary as the spec leans toward. On screen it says it is not one real reaction and
  explains soil nitrate nitrogen is represented as ammonia solely for atom counting. No unrequested two-step path added.

#### Conflicting instructions and model choices

- The user requires stopping when codex-report.md is written. It is therefore written once after verification,
  instead of creating the early rolling report requested by the general build brief. Evidence accumulates in Scratch.
- The user and current build brief require the built-in image tool. It supersedes the spec's older local FLUX method.
  All fifteen assets were generated during this Build, with full prompts and provenance in art/prompts.json.
- STANDARDS and POLISH say Motion off removes movement, never timing. This takes precedence over the spec's instant
  posting wording: a quiet ledger entry still posts after 1.5 seconds, and a second entry finishes it immediately.
  Oxygen Run keeps ten 400 ms ticks. Toggling Motion during a posting retains its original completion time.
- Sucrose has no numerical energy value and alanine is atom-only. Their energy cells say not quantified. Totals
  distinguish balanced atoms from partially quantified energy. No invented reaction energy was added.
- Clear ledger removes reaction postings and restores the explicitly labeled opening stocks, rather than leaving all
  matter at zero and making every entry impossible. Night restores two glucose on re-entry when below two, as specified.
- Nitrogen stock uses the internal soil key as an NH3 atom-count supply. Cold review made this source visible in
  Leaf by day and Deer, labeled Soil N and Dietary N respectively. It is not a claim that a deer takes nitrogen
  directly from soil or that NH3 assimilation is the actual multi-step synthesis pathway. Energy and work accounts have zero atoms.
- Fermentation products remain in Body. Oxygen counters identify lactic acid and ethanol separately. Products can
  accumulate from both cell types in one oxygen-condition column; the exact mixture stays visible.
- The photosynthesis animation includes gross water exchange to show that released O2 is from water. The displayed
  equation is the requested net equation. Opening accounts hold enough water for those exchanges.
- The passport uses volcanic CO2 release for the final return to Air. This avoids treating all weathering as a CO2 source.
- Exact annual-mean differences are used before rounding: MLO growth 3.035 and SPO 2.825 ppm/year. Rounded displayed
  swings and ranges match the spec. Station toggles keep fixed axes, so toggling never silently rescales a comparison.
- The NOAA source page confirms early 2023 MLO observations were collected at Maunakea during the Mauna Loa closure;
  a data-method note preserves that detail. BRW and SPO source URLs were not accessible in the web verifier; their
  supplied snapshot values are retained. Cold review accessed all three current files directly on 2026-11-08;
  all 36 monthly observations match. Review copies are review-noaa-BRW/MLO/SPO.txt in Scratch.
- Browser narration is the fallback. calm-professor and all fixed lines are prepared in voice/lines.json; no recordings
  were made, as the Build instructions require. The kit chooses the installed browser voice, so its timbre is not
  guaranteed to match the named bank voice until recordings are supplied.
- Bar tools were bundled into scoped mirrors under Scratch. Original bar-tool folders were not written.

#### Sensitivity

The tool shows a muscle fiber and metabolism, so a reviewer should check biological clarity and the distinction
between a chemical model and health advice. There are no people images, diet claims, body judgements, cultural narratives,
religion or hard history. Utqiagvik is named as NOAA's Arctic station location; no cultural claim is made about its community.

#### Art

Fifteen generated assets: five scenes, two cells, five round passport vignettes and three station landscapes.
Air stamp was redrawn to remove landscape. Arctic and South Pole station paintings were redrawn to remove mountains
and establish correct flat polar horizons. Station buildings are generic illustrations, not documentary site photographs.
Cutout stamps use the supported despill treatment. Every asset has people:false. Original selected PNGs are in art/raw/.
Atoms, glucose fractions, waste piles, accounts, bars, ledger and chart remain in code because they count or move.

#### Engine changes wanted

kit/data-desk.js, Chart.drawXY: implement groupBy, groups and groupLabels for line charts, splitting the numeric y
column into independent station paths with series shapes and dash patterns. It currently connects rows across groups
unless the consumer pivots them into separate columns. This tool uses the supported pivot workaround; no engine was edited.

#### Verification evidence

Independent formula parsing and numerical work are in numbers.json and prepare.py in Scratch. property.js exercises
stock conservation, input refusal, destinations, percentages and all oxygen work combinations. Driver JSON files,
per-size layout readings, voice logs, frames and audit output stay in Scratch. Read codex-report.md for final results
and limitations. Cold review is the next phase; no polish round was started in this session.

The full audit ran once, exited successfully after about 33 minutes, and produced 99 frames and 132 mechanical leads.
audit-dispositions.md and .json answer each lead individually. All 99 frames were reviewed in state contact sheets;
flagged Oxygen ledger frames were also inspected at native size. The table overlap leads are older rows passing under
opaque sticky headings and totals, not visible overprinting. No audit runtime exception occurred.
The audit's 375 px iframe lookup failed. Separate hosted drive checks exercise that actual 375 px iframe directly.
Post-audit changes are limited to its findings: label separation, singular grammar, minimum Read width, Soil heading,
stable passport controls, and same-selection narration guards. Only the affected states are rechecked, not a second audit.

Focused held-click checks confirmed four repeated mode/scene selections preserve their complete introduction, the
Night-to-passport side path completes, and five wood Checks each queue and speak their own reveal. An Oxygen-off
event now queues behind its still-valid introduction instead of cutting it; the experiment itself updates immediately.
Read remains interrupting by design. A deliberate mode switch still discards narration from the previous mode.
voice-main-complete.json records the full seventeen-tap main path at the required two-second pace: all three mode
introductions, Oxygen-off event and scientist conclusion complete with no cut. The three-mode 375 px host checks
have zero global horizontal overflow and decoded images. Tables keep their own horizontal scroll at that width.
The final owned-process inventory found seven preview hosts that Windows taskkill had silently left running.
They were identified by exact drive.py energy-accountant --host 8785 arguments and the verified repository cwd,
then terminated with psutil. No owned Chrome remained; all assigned ports are now closed and host.html is removed.

#### Cold review, 2026-11-08

Review repaired visible nitrogen provenance, scene-carbon bar scaling, night narration, wood prediction hints and stale subview speech. The passport now has connected stamps, a current C marker and a shaded code fuel token. Compact oxygen icons show the full drawn count, label the numerical remainder and keep waste clear of cell art. All fifteen paintings remain. Review evidence and audit dispositions live in Scratch; codex-review.md is the review record.

Current NOAA monthly files and all nine annual references were independently verified. The one audit completed within 40 minutes. Its saved overlay/scroll/welcome leads were confirmed against frames and the baseline. Voice-transition guards were subsequently rebuilt and checked with held clicks, repeated events and the complete main path. The 36-line voice inventory also includes the fixed Read hints, verified against default and refusal playback. No new feature, kit edit, second audit or commit.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
