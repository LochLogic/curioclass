# Water Shapes Earth: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: water-shapes-earth

#### Built

Three grade 9 investigation benches, four investigation steps, two to four test groups, three seeded trials per group, pairwise fairness checks, live cancellation, Plane graphs, plan-specific comparisons and a local lab book.
One offline HTML artifact. Build only: no commits, branch changes, deployment or polish round.
User's exact folder was confirmed as S:\CurioClass-codex. Repository writes stayed in this tool and its Scratch folder.

#### Numbers check

PASS: independent Python recomputation before implementation, saved in Scratch/numbers.json.
Ice ratio 1.090651, critical fill 0.916883, model threshold 0.917. Sandstone 95% adds 0.795181 mm in 40 cycles, displayed 0.80.
Granite/sandstone/shale at 100% split at cycles 50/20/13. At 95%, cycles 126/51/32 before run limits.
All 18 dissolve combinations at eight weeks match, including 15.20 g for cold CO2-rich limestone and 19.984 g for granite.
All 12 Manning speeds match. Medium/4% = 0.904806; flood/1% = 0.941036; flood/4% = 1.882072 m/s.
Water/air density ratio = 833.33. Maximum permitted modeled loss = 7.20 g.
480 complete discrete plans match browser calculations. 9,600 noisy result values pass their no-noise ±10% bounds; 10,000 factors stay in [0.9,1.1].
Accent contrasts recomputed: 6.52:1 on panel, 6.18:1 on secondary background, 6.84:1 with brand ink.
Final math check clarified one spec footnote: a trial can be 13.79% above its three-trial mean, rather than "up to 13 percent". Done when 7 correctly compares with the no-noise baseline; that bound passes. Invented lab rates remain explicitly labeled.

#### Feel check

Completed a full three-bench student path: default freeze, water comparison, slope comparison, graph, claim and Compare.
Best moment: C visibly splits while the half-filled control stays unchanged and B approaches, but does not reach, the threshold.
Flattest moment 1: the original empty crack blended into the freezer background. Added a dark cavity, partial liquid and a persistent split state.
Flattest moment 2: the initial delta was too quiet to read. Added carried painted stones, a growing deposit, sorted grain positions and result-dependent labels.
The warm painted jar bench gives Dissolve a distinct place and makes its smaller mass change legible without pretending granite visibly shrinks.
Bar tools were bundled into Scratch mirrors and opened before implementation. The side-by-side comparison is in Scratch/feel-compare.jpg.
The painted scenes have at least the visual richness of the bar frames. The sustained activity is controlled experimentation, not a score chase.

#### Done when

1. PASS: no-noise default values 0.00 / 0.795181 / 1.00 mm; C splits at cycle 20. Browser fixture and full Run evidence.
2. PASS: 480-plan exhaustive model check covers all rocks, fills, liquids, cycle counts and the zero/oil controls.
3. PASS: changing rock plus fill is unfair; fair event starts on all five held Run presses at a two-second pace.
4. PASS: direct browser run gives 15.20 g and 19.984 g, rendered to 15.20 and 19.98 g.
5. PASS: stream fixtures give 0.9048 m/s with sand/gravel, 1.8821 with pebbles, 0.1228 with no moving grains.
6. PASS: flood/mixed frame shows pebble, gravel and sand deposition in order, then silt in the lake.
7. PASS: 9,600 result values checked against their no-noise baseline, plus 10,000 clipped normal factors.
8. PASS: Run uses the full main width at 1366x768 and 680x425; Graph replaces that scene with the plot.
9. PASS: cell edits cancel immediately; a group tab previews that group's final result; Skip and modes act at once. Durations: at most 15/12/20 seconds.
10. PASS: two-second held-click logs show Conclude/Graph how-to once, fair five times and break twice. Read starts the current hint.
11. PASS WITH LIMITS: standard sizes and hosted 375 px checked, 13 image decodes pass, no people, no external requests in the artifact, no em dashes. Narrow secondary content scrolls as described below.

#### Wave lessons

- Hint and voice: PASS. Hint changes synchronously; Read uses it. Validity guards prevent old welcomes after plan edits. V.heard governs how-to repetition.
- Focus and layout: PASS. Stable controls, no load focus, visible focus rings, preventScroll on deliberate moves, focus restored after Skip and dialog close.
- Sizes: PASS WITH LIMITS. 44 px controls. Compact Plan fits four groups; narrow table scroll stays inside its own box. Phone Compare and hint are above the graph.
- No giveaways: PASS / not a hidden-answer activity. The ready plan is an experiment, not a puzzle with a concealed correct option.
- Honest numbers: PASS. Invented rates, simplified frost mechanism, Manning assumptions, grain thresholds and storage scope are stated.
- Standards: PASS. Students plan, run repeated trials, compare data and explain expansion, solvent behavior and moving-water effects for HS-ESS2-5.
- Motion off: PASS. No infinite CSS animation remains active; sound and run pacing are retained under STANDARDS.
- Short sets of choices: PASS WITH EXCEPTION. Bench and step buttons stay visible. The specified narrow plan-table scroller is retained.
- Resize mid-animation: PASS in targeted checks. All three held-input/resize paths reported no exceptions; full runs and immediate Skip were independently verified.
- Welcome timing: PASS. Mode-scoped welcome has no welcomeAfter; Run first suppresses stale setup narration.
- Unknown is unknown: PASS. Untested results say Not run yet; changed plans invalidate the old view.
- One look, one meaning: PASS. Group labels A-D accompany colors; dots are trials, thick marks are means; only transported grains appear in the delta.
- Badge truth: PASS. Only current-run groups show results; split threshold and moved-grain labels match computed state.
- Hints change back: PASS. Plan, Run, Graph, Conclude and dialog close all update the same hint immediately.
- No copying an answer: PASS / not a diagnosis puzzle. Compare follows the student's own experiment and uses its measurements.

#### Audit leads

The single full audit stopped after 64 frames with KeyError: End in its keyboard driver. No audit.md was produced; its complete walk and full resize sweep did not run.
Fixed the two submitted test states to use supported ArrowDown keys. No second full audit was run.
Targeted continuation used the audit's size and resize functions: four-group plans at 680/1000/1366, maximum cycles at 1366 and the book at 680/1366.
All six states had zero mechanical leads, visible unclipped hints and no runtime errors. All three held-input resize paths reported no runtime errors.
Visual leads from the partial audit: compact jars/tray too small, scale readings above the painted displays, slope card under group buttons. Fixed and re-shot affected views.
Earlier Stream Table first-frame exception was fixed by clamping negative elapsed time; affected runs have no console errors.
The host wrapper's favicon 404 was removed. Final hosted and affected artifact shots have no console errors or warnings.

#### Frames looked at

Before build: bar-frames/snowy-mail-route.png and beat-lab.png.
During build: all six early frames, model/interaction checks, diagnostic Stream Table, all twelve full frames, secondary frames, four voice/session frames and four extra frames.
All 64 partial-audit frames were inspected on labeled contact sheets, with full-size inspection of the compact Dissolve failure.
All six targeted frames, eight final frames and three final art/slope frames were inspected. Final phone Plan/Conclude/four-group frames were also rechecked.
PNG folders and labeled contact sheets remain in _scratch/water-shapes-earth/.

#### Art made

13 selected images from 14 generations, all 13 decoded successfully in the artifact. Finished art 429.24 KiB. Bundle 683.60 KiB (700,005 bytes).
The jar was redrawn once to replace a source with mixed transparency/key spill. The final source uses keyed processing and a cropped margin.
Other cutouts were composited onto the required key and processed with art.py --rekey and despill. No paid art.py generation form was run.
All selected finished images were inspected at output size and in their scenes. No image contains a person.

#### Art still to paint

None of the 13 specified images. Recorded gravel-ranger narration was not produced because Build prohibits recording; browser speech is the fallback.

#### Engine changes wanted

None. Shared kit, docs and scripts were not changed.

#### Left open

- Browser speech cannot guarantee the specified gravel-ranger timbre until recordings are supplied.
- Human headphone listening was not performed. Synthesized ice and stream sounds require cold-review listening.
- The lab is a simplified educational model; invented freeze/dissolve rates are not measurements of field times.
- Phone Plan requires vertical page scrolling to reach its full table; the page does not scroll sideways. Compact secondary explanations scroll inside the panel.
- STANDARDS overrides the spec's instant Motion-off wording: timing remains unchanged, with Skip to end live.
- Full mechanical audit remains incomplete because its End key crashed the driver; the submitted states are corrected. No second full audit, cold review or polish round was started.
- Art-driven compact layout fixes and the final jar replacement received targeted checks, not another full size sweep.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: water-shapes-earth
#### Played
Confirmed S:\CurioClass-codex. Played as a solo Grade 9 student before reading builder notes/source, then checked the projection view.
All three benches: Plan, Run, Skip, Graph, Conclude, Compare and lab book, with held clicks and Sound on. The split is the best payoff.
#### Findings fixed
- Blocker, general, Stream Table: no-transport sand still built a delta and a silt cloud. Deposits now require transported grains; only mixed includes suspended fines.
- Should fix, general, narration: Graph speech delayed or suppressed Conclude on the main path. Step switches hush old-screen speech; completed runs queue the next-action line.
- Should fix, general, lab book: a first tap could speak the freezer welcome over the book. It now speaks the book instruction, hushes stale speech, and makes the background inert until Close.
- Should fix, general, calm stream: grain positions still interpolated with Motion off. They now stay still until completion or a requested group preview; run timing is unchanged.
- Should fix, general, stacked Plan: the bench put every dropdown below the phone fold. The editable table now precedes the still bench; Run retains the large scene.
- Should fix, general, Compare: explanations repeated general facts instead of the actual manipulated variable. It now names a controlled pair, changed settings, means and mechanism.
- Should fix, general, storage: Run saved automatically before any storage notice. The lab-book button now says On this device.
- Should fix, general, completion: finishRun now rejects stopped/invalidated runs, preventing stale completion from entering the book.
- Polish, general, graphics: replaced the green-fringed jar, neutralized residual tint in its SVG presentation, and anchored it on the scale.
- Polish, general, graphics: shaded and textured the flat delta; put its low-contrast labels on a dark field plate.
- Should fix, general, compact stream: audit frames confirmed crowding captions and a slope card under group buttons. Captions now have a 15 px minimum line step; the compact slope card sits at lower left.
- Polish, general, claim input: added explicit aria-labelledby alongside the existing native label association.
- Should fix, general, scientific scope: notes now distinguish ideal pore saturation, invented rates, CO2-only temperature effects and simplified grain cutoffs from field measurements.
#### Findings left
Should fix, spec source conflict: 32 mm pebbles at 1.50 m/s is not a verified rounding of Hjulström's table. Constants stay because the brief prohibits spec changes; teacher notes disclose the difference.
Browser narration remains the existing fallback; no recordings were commissioned.
#### Break it
- Fairness: identical groups in every bench remain repeats, never Fair; two changed variables remain confounded. Real Run/Compare clicks confirm no causal endorsement.
- Crack gauge: all fills, rocks, liquids and cycle limits tested. Zero/oil stay zero, width stops at 1.00 mm, break cycles match the model.
- Mass readout: all water/rock/temperature combinations at minimum, eight and maximum weeks match the invented-rate calculation.
- Stream meter: all slope/flow/sediment combinations checked; low/0.25% moves nothing, medium/4% moves sand/gravel, flood/4% moves pebbles.
- Low-flow sand now has neither a delta nor silt. Mixed flood still produces sorted deposits. Grain movement uses trial 1, as its visible readout does.
- Noise: 318 numerical cases and 6,360 seeded noisy trials pass their baseline bounds; reseeding cannot set a score because no score or best record exists.
- Empty claim + Compare intentionally opens a worked example; it never marks the claim correct. Identical tests explicitly reject changed-cause inference.
- Repeated Run resets the experiment. Editing mid-run cancels and invalidates it; Skip after cancellation cannot save it. Group preview and mode change act immediately.
#### Voice walk
Main path at default settings, held 120 ms clicks, 2 s spacing: Run, Skip, Graph, Conclude, Compare; repeat in Dissolve and Stream Table.
Spoken order after fixes: break, Graph how-to, Conclude how-to, Dissolve how-to, finished how-to, Stream how-to.
First Run suppresses the Freeze welcome as BASELINE 16 permits; its instructions remain in the hint/Read. The side path hears that welcome too.
Later Graph/Conclude visits stay silent. Old-screen speech stops on a step change. Read speaks the current hint and a mode switch releases it immediately.
| Line | Kind | Expected | Observed |
|---|---|---|---|
| fair | event | 5 repeated Runs | 5 starts |
| graph | how | once | 1 |
| conclude | how | once | 1 |
| dissolve, stream | mode how | once each | 1 each |
| finished | how | once | 1 |
| break | event | 2 completed runs | 2 starts |
| book | how | once over 5 opens | 1 |
| Read with Sound off | forced read | current hint | 1 |
The log verifies starts, cuts and ordering, not a human listening judgment or the gravel-ranger timbre. No fixed-line wording changed.
Final modal tests hear the book instruction first, block covered Run/mode controls and restore focus on Close. A natural Freeze-Thaw run reaches Run complete without Skip.
#### Facts checked
- Ice expands about 9%: [USGS Water Density](https://www.usgs.gov/water-science-school/science/water-density). Spec density inputs independently give 1.090651 volume ratio and 0.916883 critical fill.
- Ideal 91.7% pore-fill argument: [FHWA-HRT-06-117, chapter 2](https://www.fhwa.dot.gov/publications/research/infrastructure/pavements/pccp/06117/02.cfm); not a universal rock threshold. Fagerlund's work concerns critical saturation of concrete.
- Crack rates/break cycle checks are explicitly invented spec constants: granite/sandstone/shale split at 50/20/13 cycles at full fill; sandstone 95% gives 0.795181 mm at 40 cycles.
- Normal rain about pH 5.6 due to CO2: [USGS pH and Water](https://www.usgs.gov/water-science-school/science/ph-and-water).
- CO2-bearing water dissolves carbonate into dissolved calcium/bicarbonate: [USGS WRIR 02-4045, table 3](https://pubs.usgs.gov/wri/wri024045/htms/table3.htm).
- Dissolution helps form caves/sinkholes: [USGS Natural Holes](https://eros.usgs.gov/earthshots/natural-holes); the tool does not say every sinkhole has this cause.
- Calcite limestone/marble and marble's recrystallized texture: [USGS recognition guide](https://pubs.usgs.gov/gip/acidrain/4.html). Granite's tiny rate and marble's 0.8 factor are lab assumptions.
- Gas solubility generally decreases as temperature rises: [OpenStax Chemistry 2e, 11.3](https://openstax.org/books/chemistry-2e/pages/11-3-solubility). The 1.2/1.5 loss multipliers are invented, not measured temperature laws.
- Dissolve arithmetic: 8-week cold CO2 limestone 15.20 g, granite 19.984 g; maximum modeled loss 7.20 g. Independent Python and browser checks agree.
- Manning relationship: [USGS WSP 2175](https://pubs.usgs.gov/wsp/wsp2175/wsp2175_vol2.pdf). Depth approximates hydraulic radius for a wide channel; n = 0.03 is the chosen model constant.
- All 12 speeds recomputed: medium/4% 0.904806, flood/1% 0.941036, flood/4% 1.882072 m/s.
- Grain thresholds/order: [Hjulström (1935), table 7 and figures 17-18](https://paleoarchive.com/literature/Hjulstrom1935-MorphologicalActivityRiversRiverFyris.pdf), printed pp. 295-298, downloaded and visually inspected. 8 mm: 0.81 m/s; 30 mm: 2.18-2.21 m/s. Exact tool cutoffs are model choices, not verified measurements for all three specified sizes.
- Already-suspended fines versus erosion from the bed are distinguished. Mixed material's cloud does not claim cohesive clay erodes at every speed.
- Water about 1,000 kg/m3 versus air about 1.2: [NASA Glenn atmosphere model](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/earth-atmosphere-equation-metric/); ratio 833.33, stated about 830 near sea level.
- Numerical rates/noise are simulation definitions. HS-ESS2-5 is practiced through manipulating one variable, repeated trials and evidence-based explanations, rather than a score.
#### Sensitivity
None: material-property investigations, no cultural identities, hard history, religion or bodies. All 13 images contain no people; an unoccupied scientific bench fits this spec.
#### Flattest moment left
Granite barely changes in Dissolve. That quiet control is scientifically useful; the readable scale and trial dots carry the difference. Compare was the flatter avoidable moment and is now plan-specific.
#### Graphics
Inspected all 13 finished assets at output size and their scenes; replaced ws-jar via the built-in imagegen skill and art.py --rekey.
Kept the painted freezer, mineral textures, warm lab, glass, balance, tray and stone cutouts. Delta gains shading, deposition ridges and grain texture.
Compared with the existing Snowy Mail Route and Beat Lab bar frames. No simplification or new topic was introduced.
Art 419.18 KiB; bundle 674.61 KiB. The SVG neutralizes key tint on colorless glass; text/readouts remain in code.
#### Audit
One full audit completed, exit 0, within its 40 minute cap, Chrome 9941 and host 8745. All 97 generated frames inspected, with full-size confirmation of the compact stream leads.
17 leads disposed: five caption/slope overlap rows fixed; one native-label false lead hardened with explicit ARIA; four region/scroller rows intentional; seven welcome omissions/cuts allowed by BASELINE 16.
The scene-region samples hit intentional group controls over an empty corner. Four-group phone scrolling is the spec's internal table scroller, with no page-wide overflow.
No runtime errors, lost focus, resize exceptions, stuck controls or infinite CSS animations. All repeated-click checks clean.
Wave lessons checked independently: current hint/Read, stable controls, 44 px targets, empty data shown unknown, group letters alongside colors, honest model labels, no scored giveaways, and controlled-investigation standards coverage.
The audit did not detect the book's wrong-screen speech or continuous SVG grain travel with Motion off; this review fixed both.
Final affected frames re-shot at every implicated size, all inspected, zero console errors. Claim association verified at all eight sizes; stream spacing/card at 680, 800, 1000 and 1366.
Main-path and modal voice checks re-run; Copy table and Clear both succeed. Motion-off stream stays static while its 15-second run remains active. No second full audit.
#### Left open
- Browser fallback cannot guarantee the specified gravel-ranger timbre; recordings remain a later pipeline step.
- Spec conflict: replacing the 1.50 m/s pebble cutoff with the original table's approximately 2.2 m/s for 30 mm would prevent the specified 1.88 m/s flood from moving those pebbles. Resolve size/cutoff/outcome together in the spec; no unauthorized substitute made.
- No unattended questions: kept invented rates as the spec leans toward, and preserved Motion-off timing under STANDARDS rather than the spec's instant-run wording.
- Phone Plan prioritizes editable controls before the still bench. The full illustrated Run remains unchanged in focus.
- No commits; changes confined to the named tool and Scratch.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Water Shapes Earth handoff

Build only. No commits, deployment or polish round.

#### Source map

src.html starts from the kit starter frame. CSS provides real-pixel wide, short landscape and stacked layouts.
CONFIG defines each bench's variables and default plan. calculate is the pure numerical model.
Each run snapshots its plan, fairness, seeded trial factors and results before animation begins.
The SVG renderer paints code-driven cracks, liquid, chip area, stream channels, grains and delta over generated art.
Plots use kit/graphing.js Plane. Shared motion, tones and narration use kit/curio.js.
Stable plan controls and step/mode buttons retain focus. Editing a cell cancels playback and invalidates the old view.
The lab book stores completed runs under curio-water-shapes-earth with try/catch. Claims are session-only.
The __tool hook exposes state, models, seed generator, voice log and rendering for review.

#### Open questions resolved

- Keep the invented freeze and dissolve rates as the spec leans toward. Label them as lab-model rates on screen and in notes. Do not add measured field rates or new content.

#### Conflicting instructions and interpretations

- STANDARDS and POLISH say Motion off removes movement but never timing. That overrides the spec's instant-run wording. Run duration is preserved, with Skip to end live throughout.
- User requires stopping when codex-report.md is written. The report is therefore written once, after verification, rather than as an early rolling document.
- Bar tools were bundled into Scratch mirrors to obey the user's write-only scope. Original bar-tool folders were not changed.
- Dissolve trial noise acts on loss rate, not directly on remaining mass; freeze width stops at 1.00 mm when broken.
- The claim column copies session claims for their own run. Claims do not enter localStorage.
- All 13 specified illustrations were generated using the built-in image tool instead of the spec's older local-FLUX workflow, as requested by the user and current build instructions.
- A Stream Table group tab previews that group's computed final state immediately. It does not rewind the overall clock, so a four-group playback still ends within 20 seconds.

#### Art and voice

Prompts, provenance and raw originals are in art/. Assets use art tokens in one image bank.
No people were requested. Textures clip to code-drawn rock halves. All changing measurements stay in code.
voice/lines.json specifies gravel-ranger, Algenib. No recordings were made during Build; browser narration is the fallback.
The jar was redrawn once after full-size inspection found colored spill from the original mixed alpha/key source.
Its final opaque green source uses the supported keyed treatment, with a cropped outer margin, to keep glass neutral.
Other cutouts use the existing despill option. Every selected finished image was inspected at its output size.

#### Engine changes wanted

None. Kit, docs and scripts were not edited.

#### Review next

Cold review should inspect the simplified frost model, dissolution chip shrinkage, delta sorting and the real-time performance of SVG redraws.
Read codex-report.md for checked states and remaining limitations. Evidence stays in _scratch/water-shapes-earth/.

#### Verification outcome

480 discrete plans matched independent Python fixtures. Another 9,600 noisy result values stayed within their no-noise bounds.
All 13 selected images decoded. Hosted phone frames have no page-wide horizontal scroll; Plan still needs vertical scrolling.
Held-click voice logs show one Conclude and Graph how-to, five unfair-plan events and two split events.
Completed runs persist; session claims are not stored; Copy table worked through a real held click.
The complete default student path finished its 10 / 8 / 15 second runs without errors.

The single full audit stopped after 64 frames with KeyError: End in its own key map. No audit.md was produced.
The submitted audit-states.json now uses supported ArrowDown inputs. A second full audit was not run.
Targeted checks reused the audit's size/resize functions: six remaining/extreme states had no mechanical leads,
and held-input resize paths for all three benches reported no runtime errors. The complete walk remains unverified.
Frame inspection prompted compact bench-space, scale-display and slope-card fixes; affected paths were re-shot only.
Chrome sessions and host servers used ports 9990, 9991 and 8795 and were closed. Temporary host.html was removed.

#### Numeric footnote

The supplied Sources footnote says a trial can be up to 13 percent from its group's mean.
The exact maximum above a three-trial mean for factors 1.1 / 0.9 / 0.9 is 13.79 percent.
Done when 7 correctly uses the no-noise baseline, and every tested trial meets that bound.

#### Cold review changes

Review evidence lives under Scratch/review-*. Cold student play preceded reading this handoff and source.
Step changes hush speech from the old screen so Graph cannot delay Conclude; completed runs queue the finished how-to.
finishRun ignores inactive or invalidated runs, preventing stale completion from entering the book.
Compare selects a real one-variable pair and names its changed values, measured means and relevant water property.
Identical plans are described as repeats; fully confounded plans do not receive causal model answers.
Stream deltas require transported grains. Silt appears only for mixed sediment, which includes pre-suspended fines.
The jar was redrawn and processed with art.py --rekey; its SVG applies saturate(0) to neutralize residual key tint.
The Lab book control states On this device before any automatic save. Notes distinguish model constants from field measurements.
The no-transport state is included in audit-states.json. Review uses Chrome 9940-9947 and host 8745.
On stacked screens Plan now places the editable table before the still bench, keeping the dropdowns above the fold.
Run continues to give the illustrated bench the full stage. The earlier phone Plan scrolling limitation is resolved for primary controls.

#### Spec source conflict found in cold review

Hjulström 1935 table 7, printed page 295, gives 8 mm at 0.81 m/s and 30 mm at 2.18-2.21 m/s.
Page 296 explicitly calls the curve a preliminary zone with depth/grain-size qualifications.
The spec's 32 mm pebble cutoff of 1.50 m/s cannot be represented as a faithful rounding of that table.
The tool now identifies cutoffs as model choices in notes and avoids attributing exact cutoffs to Hjulström on screen.
Changing the constants would contradict the spec's flood/4% pebble outcome, so that spec decision remains open.
The source PDF, text extraction and full-page renders are preserved in Scratch. No new measured threshold was substituted.

#### Final audit and confirmed corrections

The cold-review audit completed once, exit 0, within 40 minutes. Its 97 frames and report remain in Scratch/review-audit.
Confirmed compact caption spacing and slope-card overlaps are fixed. The claim's existing label now also has explicit ARIA linkage.
Region warnings for the intentional group controls and the specified phone table scroller are documented in the review report.
The lab book now owns its narration and makes background controls inert; closing it restores focus and the current step's hint.
Motion off keeps stream grains static during the timed run, then shows the final outcome. An explicit group preview still acts immediately.
No shared engine, scripts or docs were edited. Main-path/modal voice and affected-size checks follow these narrow corrections; no second audit is run.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
