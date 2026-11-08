# Codex report: energy-accountant

## Built
Grade 9 biology bookkeeping in three modes: Ledger, Oxygen switch and Planet's books. Five painted living scenes,
lettered moving atoms, stocked accounts, a real scrolling reaction ledger, an unscored wood-mass prediction, ten carbon
passport stamps, live oxygen/work experiments and a NOAA seasonal graph. Starter-derived, kit narration and DataTable/Chart.
Build only. No commits or polish round. Writes confined to the tool and its Scratch folder. Chrome 9980-9987; host 8785.

## Numbers check
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

## Facts checked
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

## Break it
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

## Voice walk
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

## Feel check
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

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
Every captured drive PNG was opened directly or on contact sheets. Sets: early8, check5, extras12, full-ledger7,
full-planet7, oxygen-a4, oxygen-b3, original phone3, failed phone-try1, drags-a3, run-check3,
final-visual9, final-phone3, final-voice-a2, final-voice-b8, final-edge4, edge-retry2. All99 audit PNGs reviewed on15 state sheets;
flagged Oxygen ledger760/1366 also opened native. Final compact posted/Soil, tall Night, synthesis, passport, wood,
calm timing and tall Planet opened native. Original overflow phone frame is retained as failed evidence, replaced by passing frames.
All15 finished WebPs inspected at their final sizes, including stamps after keying and three redraws.

## Art made
15 selected assets from18 image generations: five1000px scenes, two800px cells, five160px keyed circular stamps,
three440px stations. Naturalistic science gouache throughout; all people:false. Art609.3KB, recorded voice0KB,
1230.1 KB self-contained bundle against the2MB goal. No placeholders. Full prompts/provenance in art/prompts.json.
Redrew Air stamp to remove landscape; Arctic and South Pole stations to remove false mountain horizons.
Only art.py --rekey used. Atom motion, precise bars, graph, accounts and countable piles are code-native.

## Art still to paint
None. No people called for or depicted. No image generation limit or fallback placeholder remains.

## Engine changes wanted
kit/data-desk.js Chart.drawXY: support line-series groupBy/groups/groupLabels with separate paths, symbols and dashes.
Current line renderer ignores grouping. Tool uses supported12-row pivot for chart, retains original36-row DataTable.
No kit, docs, script, other tool or engine edits were made.

## Left open
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
