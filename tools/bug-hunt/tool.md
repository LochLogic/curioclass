# Bug Hunt: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: bug-hunt

#### Built

Built Hunt, Run, Explain and Real story in one offline HTML file, using the shared kit and twelve original paintings.
Hunt has seeded inheritance, two habitat changes, keyboard pecking, a miss lockout, pause blur and an honest ending.
Run has live controls, 200 moths, History, prediction locking and a 120-generation limit.
Explain uses the player's actual records and device-only writing. Real story has eight stops and disconnected historical points.
This was Build only. No commits or polish round. Draft metadata remains stage built.

#### Numbers check

Evidence: check_numbers.py, numbers.json, check_model.cjs, model-checks.json, spec-reference/ and reference-recomputed.json in Scratch.
The initial large independent Python job hit its 120-second limit; the smaller 50-Hunt, 20-Run retry completed.
The shipped JavaScript model was checked over 2,000 hunts per behavior and 400 History runs, plus 50 seeds per Run extreme.
- Careful: 74.8 percent reach 15 dark moths in displayed soot cohorts 3 to 8; 89.8 percent end at half that peak or less.
- Idle: 1.15 percent reach that peak. Two-eaten model: 1.7 percent. Random fifteen-eaten model: 6.05 percent.
- History: 400 of 400 rise above 50 percent during soot and fall below it by generation 55.
- Birds off with mutation on: only 80 percent of 50 seeds remain below 25 percent at generation 55. The spec's universal bound fails.
- Both toggles off still allows four incomers; it is not pure drift from a closed starting population.
- The original Hunt script includes out[3:9], which means displayed cohorts 4 to 9, and an extra final offspring endpoint.
- Original source rerun: Hunt 87.35/95.9 percent on its own endpoints, versus 73.8/90.6 on the displayed endpoints.
- Original Run rerun: generation-15 median 44.5 percent and Birds-off generation-30 median 7.5 percent reproduce the source.
- The original Run script mutates g1 only. The written rule and this build mutate both inherited pale copies.
- Fourteen displayed cohorts contain 420 moths including the initial 30, with 390 newly bred young visible after it.
- Recomputed research release total: 706+101+731+82+751+53+763+58+774+34+797+14 = 4,864.
- Bark darkness measured 20.114, 50.151 and 85.230. Six rendered moth targets had maximum error below 0.01.
- Contrast: ink/paper 12.918, ink/white 14.842, muted/paper 5.635, brand/paper 5.563, white/brand 6.392, focus/paper 5.992.
- Dark-bar contrast 15.13 and pale-bar contrast 11.69 reproduce. Nearest claimed accent dE 18.9 reproduces.
- The claim that all science accents are dE 48 or more away does not reproduce: carrying-capacity is 37.8 and mitosis is 42.1.
No model parameter was changed to manufacture the spec's preferred success percentages.

#### Facts checked

- Variation, inherited color, dominance of a dark copy and differential predation: Cook and Saccheri (2013), plus Cook et al. (2012).
  https://pmc.ncbi.nlm.nih.gov/articles/PMC3668657/ and https://pubmed.ncbi.nlm.nih.gov/22319093/
- Transposable element in cortex, inferred date around 1819: van't Hof et al. (2016), checked against Liverpool's research release.
  https://pubmed.ncbi.nlm.nih.gov/27251284/ and https://news.liverpool.ac.uk/2016/06/01/jumping-gene-took-peppered-moths-dark-side/
- First documented dark Manchester record, 1848: Liverpool's release and ASU Ask A Biologist.
  https://askabiologist.asu.edu/games-sims/peppered-moths-game/natural-selection.html
- Pale speckles, bark camouflage, soot and lichen loss: Cook and Saccheri (2013), Cook et al. (2012) and ASU's historical account.
- About 98 percent dark by the late nineteenth century: the spec's Manchester record, with ASU corroborating near-city populations by 1900.
  The tool keeps the coarse 1890s label; it does not imply a measured annual series.
- Kettlewell's 1950s polluted and clean woodland comparison: his 1955 and 1956 papers, with Cook and Saccheri (2013).
  https://www.nature.com/articles/hdy195536.pdf and https://doi.org/10.1038/hdy.1956.28
- Britain's 1956 smoke-control law: original Clean Air Act, chapter 52.
  https://www.legislation.gov.uk/ukpga/Eliz2/4-5/52/enacted
- Decline since the 1960s to 1970s: Cook et al. (2012) and the spec's two-source historical synthesis.
- Michigan parallel and lichen disagreement: Grant, Owen and Clarke (1996), whose abstract explicitly reports no perceptible local lichen change.
  https://academic.oup.com/jhered/article-abstract/87/5/351/816056?login=false
- Majerus: Cambridge-area study, 4,864 released moths and stronger predation on dark moths: Cook et al. (2012), abstract and Table 2.
  https://discovery.ucl.ac.uk/id/eprint/1354483/1/609.full.pdf
  Table 2's releases are 2002 to 2007; the timeline's wider 2001 to 2007 span includes baseline observations.
- Game counts, times, darkness, probabilities and rates are stated model assumptions from the spec, checked against the code.
  The model-limits sentence separates them from natural rates and historical decades.

#### Break it

- Pecking bare bark starts the timer but awards no moth. A second immediate tap cannot evade the one-second lockout.
- Mashing, idle, random eating and reverse selection were compared over seeded model runs. No stored best or success badge exists.
- Pause and mode switching cannot expose moths for study: the paused field is blurred and covered. The clock stays still.
- Restart returns the same seed and population. It is a fresh hunt, not an accumulated score.
- Prediction: native input set a pin, History locked it, and off/on toggles plus a later graph click could not move it.
- Live slider drag during History took over the bark, updated the current band cell and preserved playback; the next generation used it.
- Wrong cards both returned the stated reasons and left writing closed. Correct-card order is shuffled, with uniform visual cards.
- The sorter is a teaching discussion, not a mastery assessment. Trial can discover its correct card; no mastery or completion is awarded.
- Evidence chips were checked against the exact Hunt snapshots and round removals. Empty evidence disables chips.
- Device writing survived reload with the exact edited sentence. Clipboard denial has a selection fallback.
- Read during a queued story originally could strand its gate. Fixed: interrupted or dropped narration requeues while that card is current.
  Native held Read, an immediate Continue attempt and a later completed narration verified blocked=true, ready=true, with zero console errors.
- History now preserves Birds, Mutation and Speed; a native off/off/2x path retained them and recorded zero predation.
- The long native calm/mashing batch hit its limit, and its smaller retry did too. Stopped and closed its own browser through CDP.
  Do not treat that unfinished batch as a completed native mashing measurement.

#### Voice walk

Main held-click path: miss, breed, sootCard, nextGen, cleanCard, huntEnd, welcomeExplain, cardWrongA, chips,
welcomeRun, history, welcomeStory, stop2, stop7. Other stop events went stale when the student moved to a different stop.
The first welcome was skipped by acting, which BASELINE 16 allows; its instructions remained in the hint and Read.
Each heard how line started once. Five repeated misses at a two-second tap pace started miss only once.
Wrong-card feedback updated immediately even when its queued speech became stale. All four modes' instructions were available on the path.
The side path covered keyboard pecking, Read, live History takeover, writing and reload; the gate path tested Read interruption separately.
Soot and clean card narration finished before Continue acted in the full hunt. No chip instruction played with absent evidence.
No recordings were made. The 28 fixed lines use Curio.voice with browser speech fallback; bank/style metadata is casual-peer.
Evidence: play/session.json, voice-breaks/results.json and card-read-result.json.

#### Feel check

Best moment: soot reverses which painted moths disappear into the tree, followed by the student's own birth counts.
History's steep decline on clean bark is an earned visual comparison with a small-population Hunt that may have a low peak.
Flattest moment 1: the old breeding swap felt abrupt. Added survivor pulsing, a newborn fade and moving bar heights.
Flattest moment 2: compact hints covered the timeline and writing actions. Moved those hints into the notebook panel and reserved graph space.
Played the complete fourteen-round Hunt through Explain, History and all eight story stops using native held input.
Compared Hunt with Snowy Mail Route and History with Beat Lab in Scratch/bar-comparison.png. The paintings hold up beside both bars.
No separate polish round was started.

#### Done when

1. PASS: Hunt owns the largest area; Run gives its main graph and sample strip the stage. Laptop controls fit, with targeted compact corrections.
2. PASS: load is still; native first peck eats and starts the clock; first bare-bark tap is a miss.
3. FAIL against the quoted success percentages: literal cohort checks give 74.8/89.8 percent, not about 85/95. Idle remains below 5 percent.
   The mashing model is weak; the full native mashing duration remains unverified after bounded retries.
4. PASS: every checked histogram sums to 30 or 200, dark bins equal line counts, markers use the current bark, and measured colors agree.
5. PASS: native breeding-beat taps finish immediately; History slider takeover is immediate and live.
6. FAIL against the strict bound: History 400/400 passes the rise/fall criterion; the strict Birds-off under-25 bound fails with the written mutation rule.
7. PASS: both misconceptions refused, writing opens for b, chip numbers match records, and saved text/privacy survived reload.
8. PASS: historical points have no joining line; stop 7 explicitly states the lichen disagreement.
9. PASS: native Tab/arrows/Shift/Space ate a moth; moths never enter the tab order.
10. PASS with documented stale-event behavior: repeated how lines start once, story gates wait, and disabled chips are not named as next actions.
11. PASS: twelve bundled paintings, no external requests, no source em dashes, and model limits in Hunt end, Run and notes.

#### Wave lessons

- Hint/voice: PASS, synchronous hints, shared queue, state-valid events, Read priority and held-input logs.
- Focus/layout: PASS after targeted fixes; right-card focus goes into writing, stable controls and reserved hint space.
- Sizes/targets: PASS for main DOM controls, seven standard desktop sizes and 375 iframe; moth pecks have a minimum 44-pixel hit region.
- No giveaways: FAIL against the general rule, constrained by the exact specified card text. Shuffled equal-height cards have no answer IDs, score or mastery badge; source text still makes b longest.
- Honest numbers: PASS, real birth records and model assumptions; an unlucky hunt does not receive a fabricated hill.
- Standards: PASS, MS-LS4-4 writing and misconception comparison; MS-LS4-6 histograms, time series and prediction.
- Motion off: PASS for no running animations, instant specified breeding and a native 1-second clock delta; the full calm-duration batch remains unfinished.
- Short choice sets: PASS after compact modal fixes; all sorter and timeline choices remain visible.
- Resize during action: PASS in the audit, with no exceptions or stuck controls.
- Deferred welcome: PASS, no welcomeAfter; first input remains immediate.
- Unknown as unknown: PASS, no interpolated historical measurements or invented success.
- One look/meaning: PASS, one darkness scale and consistent bark-band labels.
- Badge truth: PASS, no mastery or saved-success badge is claimed.
- Hints change back: PASS, mode entry and pause/reset update hints synchronously.
- No answer by copying clue words: PASS for the hunt; Explain remains the specified explicit misconception discussion, not a hidden-answer quiz.

#### Audit leads

The one audit completed within 40 minutes with 58 leads; audit/audit.md preserves every row.
- All-size canvas/field-label overlaps are intentional labels painted above the hunt field. Moth placement avoids their rectangle.
- The phone's 9-pixel bird label is now 10 pixels. Pause deliberately blurs and covers the field and its labels to prevent scouting.
- Explain focus falling to the page is fixed: the correct card focuses the first available chip or writing field.
- All three empty writing fields now have explicit accessible names. The no-data hint names usable header modes.
- Copy clipping at 1280 is fixed with shorter compact textareas and reserved action space; targeted post-fix native checks confirm its center is uncovered.
- Story/end cards deliberately obscure the inactive field and its labels. This is a modal presentation, not missing content.
- Compact modal hints and end buttons were genuinely covered. Fixed by hiding the compact inactive graph/actions and moving limits into the notebook.
  End buttons and the hint now pass center hit-testing at 680 and 375; the final root bundle's 680 screenshot was checked again.
- The fixture's skipped-breeding how line is expected when it jumps directly through that beat; native full play heard it once.
- Sound changed header width. Fixed with stable button widths; subsequent frames keep the header in place.
- Reset at an already reset state is an intentional no-op. The progressed Run-to-120/reset check verified actual reset behavior.
- First bark input, Read, Sound-off and rapid mode/restart changes may interrupt welcome speech under BASELINE 16.
  Instructions remain in the hint and Read; no delayed welcomeAfter is scheduled. Read speaks the current instructions directly.
- Repetition checks were clean. Motion-off and all resize-stress checks finished without exceptions or stuck controls.
The audit describes the pre-fix baseline. Targeted post-fix checks are separate; it was not rerun.

#### Frames looked at

Looked at all 95 audit PNGs on twelve labeled sheets, plus the full seven-size, four-mode set (28 frames).
Also reviewed native play (13), voice side path (3), phone modes (4), extremes (6), targeted layout checks (10),
the corrected Read gate, eight post-audit desktop frames, two phone modal frames and the final root-bundle frame.
Early art/previews and the bar comparison were viewed. Scratch retains the individual frames and labeled sheets.
Final smoke: candidate and root bundle bytes match; the smaller held-input retry logged zero errors, warnings or exceptions.

#### Art made

Twelve images generated with the built-in OpenAI image tool; prompts and original PNGs are in art/prompts.json and art/raw/.
Finished cutouts were inspected, keyed with the required free art.py --rekey form, and despilled.
Three barks were measured and tinted; moths retain wing detail while tinting to their own darkness at runtime.
No generation redraw was needed. Processing revisions corrected key fringes and calibrated darkness.
Art: 1414.256 KiB. Voice recordings: 0 KiB. Final HTML: 2004.019 KiB (2,052,115 bytes).
This is about 2.05 MB against the 2 MB goal. Background quality is 72; no teaching image was removed to meet a hard cap.

#### Art still to paint

None. No people appear; every asset explicitly has people false.

#### Engine changes wanted

scripts/bundle_tool.py, bundle(): accept an optional slash in kit stylesheet links. A formatter's valid self-closing link was not inlined.
The exact starter tag is restored here, and the final bundle has no unresolved asset URLs. No shared source was changed.

#### Left open

- Source statistical disagreements above, the specified sorter answer-length giveaway, and the native calm/mashing batch that stopped twice at its limits.
- The extra final two-shot smoke lost its Chrome connection; a smaller one-shot retry passed with zero browser errors.
- Browser narration quality was not judged by listening, because all automated Chrome sessions were muted as required.
- Windows desktop/headless verification is not a physical Chromebook or screen-reader user trial.
- One early bar-tool bundling command regenerated their existing ignored HTML outside the two authorized folders. Their sources were untouched.
  This scope mistake is recorded in handoff.md. Subsequent authored files and evidence stayed inside the two authorized folders.
- Initial short read/preparation commands lacked an explicit process timeout and completed promptly; subsequent scripts used explicit timeout wrappers.
- The report was drafted in Scratch and finalized last to honor the user's instruction to stop immediately when it is written.
All started Chrome instances and HTTP servers are closed; ports 9990 to 9997 and 8795 were checked closed. host.html is absent.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: bug-hunt
#### Played
Cold Grade 8 play preceded all builder files: a real hunting round, History, Explain and all eight story stops; then the full fourteen-round Hunt with held input.
The bark, bird and reversal of camouflage are strong. History makes the population lesson visible. Explain is much easier to guess than to reason through.
Root was S:\CurioClass-codex throughout. No commits. Authored files stayed in tools/bug-hunt/ and _scratch/bug-hunt/.
#### Findings fixed
Native checks and before/after frames are indexed in _scratch/bug-hunt/review-gallery-index.json; named voice and cheat logs below supply the reproductions.
- Blocker, general, Run prediction: fixed random seed exposed the next result through replay. Reset and History now start fresh trials; explicit test seeds still work.
- Blocker, general, Hunt Pause: blur still revealed a dark moth's location during a frozen clock; a native resume-and-peck caught it. Paused rendering now omits moths while retaining bark, bird and population state.
- Should fix, general, Real story / Explain: old speech continued over a different scene or answer. Feedback interrupts obsolete speech while preserving Read priority.
- Should fix, general, wrong-card feedback: repeated taps could cut the one allowed explanation short. The same refused card now keeps its narration playing.
- Should fix, general, Explain: chip instructions could be dropped before the first chip tap. Correct feedback and the next action now share one how-to line.
- Should fix, general, Run: active playback still told students to press Play. Hints now name the actual Pause control.
- Should fix, general, main-path Run voice: Play, Step and History now interrupt the obsolete welcome before its Play instruction can run over active playback; History's own line follows immediately.
- Should fix, general, Hunt voice: a first Pause or a return to paused Hunt could welcome students by telling them to peck. It now says Resume; next-generation speech is invalid while paused.
- Should fix, general, Run sample: the title obscured the first moth row. All forty moths now sit below the label.
- Should fix, general, 375-pixel layout: Run controls clipped and Bars pushed them farther down. Bars and Line share the plot; controls fit through Reset.
- Should fix, general, phone prediction regression: Predict now opens Line; returning to Bars gives a valid Line instruction, dropped when stale. Locking the pin stops obsolete how-to speech.
- Should fix, general, phone feedback: kept Explain's original stage height and tightened the cards so a refusal remains visible with all three choices.
- Should fix, general, phone Hunt: the histogram fell below the viewport. Rebalanced field, timer and graph; moved the tip below them, retaining the painted field.
- Polish, general, breeding: strengthened the flattest transition with the actual pale/dark parent counts, retaining pulsing survivors and the newborn fade.
- Polish, general, art: repainted carbonaria with clearer body shading and wing detail; preserved its calibrated darkness and the rest of the set.
- Polish, general, tint canvas: marked its readback use explicitly, removing the warning exposed by the calibration check.
#### Findings left
- Blocker, general, Explain: blind enumeration opens writing; the correct card is also conspicuously longest. Cold and post-fix native attempts confirmed this.
  The spec prescribes both the exact cards and retry-to-correct flow. Changing that gate or its wording needs a spec decision, so CODEX-REVIEW section 3 forbids improvising it here.
- Should fix, general, statistical acceptance: the written model does not meet the spec's quoted Hunt and Birds-off percentages. Exact rules retained; measurements below.
- Should fix, general, no-eaten explanation: the prescribed "every moth bred" overstates a model with 30 survivors but only 29 local young after the incomer replaces one.
  Run likewise has 200 survivors and 196 local young. Seed-1 parent tracing confirmed a missing parent in both cases; see review-parent-coverage.json.
- Polish, general, low-peak ending: the prescribed chance wording can understate a student's deliberate reverse selection. It remains the specified ending, not an earned success claim.
#### Break it
- Hunt counter: bare-bark taps, rapid repeated taps and a blind 135-point grid sweep. The lockout held; the grid caught 2, not 15. No saved best score exists.
- Pause / mode escape: clock delta 0 over 2.5 seconds while paused; moths hidden after fixing the visible blur silhouettes. Returning to Hunt preserves the pause rather than granting scouting time.
- Population meters: 30,800 review-run snapshots of the shipped model conserved 30/200 moths; histogram dark bins equaled the line's numerator, with legal inherited copies.
- Hunt behavior, 200 seeds each: careful peak 15+ on soot 75.5%, final at most half that peak 89.5%; idle peak 1.5%, two-eaten masher 2%, random fifteen-eater 9.5%.
- Run, 50 seeds: History rose above half on soot and fell below half by generation 55 in 50/50. Birds off stayed below 25% in 40/50; both toggles off in 48/50.
- Slider sweep 0 to 100 without advancing: generation and dark count stayed 0. Extremes 0/100, clearing 50 and generation 120 worked; the cap disables Play and Step honestly.
- Prediction: real drag set generation 25; Step and off/on toggles left it locked at 25. Three new History trials differed, so observing a replay no longer reveals an exact future.
- Live History takeover: real Bark drag changed the next cohorts to darkness 50 while playback continued; the current band and hint agreed.
- Explain: both misconceptions refuse with their own reasons. All-options guessing still opens the boxes, an unresolved spec-constrained blocker, not excused as "only teaching."
- Evidence chips: no-data chips disabled; saved text survived a fresh load. Writing and Copy award no mastery or completion score. Generated counts were compared with the actual Hunt records.
#### Voice walk
Held pecks at a 2-second pace, twelve per round with the full 25-second timer, through all fourteen generations and both narrated story cards; then Explain, History and Real story.
Heard in order: breed, sootCard, nextGen, cleanCard, huntEnd, welcomeExplain, cardWrongA, writeEvidence, welcomeRun, history, welcomeStory, stop2, stop7, stop8.
The first hunting tap skipped welcomeHunt, allowed by BASELINE 16; its instructions remained in the hint and Read. Both story-card narrations finished before Continue.
The browser reverted to a compact viewport between the two bounded Hunt batches. The compact writing path was rechecked using its actual Next buttons.
Main and targeted logs: _scratch/bug-hunt/review-main-phase-*.json, review-compact-writing-path.json, review-read-priority.json and review-repeat-*.json.
| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| breed / nextGen / each mode how-to | how | once | once each |
| miss, five held taps | how | 1 | 1 |
| refused card A, five taps in one visit | event, spec once per card | 1 | 1 |
| same story stop, five taps | event | 5 | 5 |
Sound-off Read worked; mode changes released Read; stale story events did not speak over a later scene. Fixed strings matched allLines and the 31-line voice catalog.
#### Facts checked
- Inherited variation, dominance and selective predation: [Cook and Saccheri, Heredity 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3668657/).
- Cortex-region DNA insertion and inferred date about 1819: [van't Hof et al., Nature 2016](https://pubmed.ncbi.nlm.nih.gov/27251284/). This is an inferred origin, not a witnessed mutation.
- First recorded dark Manchester moth in 1848; near-city dark frequency about 98% by 1900: [Arizona State University](https://askabiologist.asu.edu/games-sims/peppered-moths-game/natural-selection.html).
- Manchester's 98% by 1895: [Butterfly Conservation](https://butterfly-conservation.org/moths/why-moths-matter/amazing-moths/peppered-moth-and-natural-selection), corroborated by [Grant and Wiseman 2002](https://pubmed.ncbi.nlm.nih.gov/12140267/). No annual series was invented.
- Soot, pollution and lichen loss; Kettlewell's 1950s polluted/clean experiments: Cook and Saccheri, above, and the original 1955/1956 experiments they cite.
- Britain's 1956 smoke-control law: [Clean Air Act 1956, chapter 52](https://www.legislation.gov.uk/ukpga/Eliz2/4-5/52/enacted). Enactment is distinguished from later implementation.
- Dark-form decline since the 1960s/1970s: [Cook et al., Biology Letters 2012](https://pubmed.ncbi.nlm.nih.gov/22319093/).
- Michigan's parallel decline and absence of detectable local lichen change: [Grant, Owen and Clarke, Journal of Heredity 1996](https://academic.oup.com/jhered/article-abstract/87/5/351/816056?login=false).
- Majerus's Cambridge-area study and greater dark-moth predation: [Cook et al., original paper](https://mallet.oeb.harvard.edu/sites/g/files/omnuum6606/files/malletlab/files/609.full_.pdf).
  Independently summed its six release rows to 4,864. Releases were 2002-2007; the stop's 2001-2007 span includes baseline observations, not seven release years.
- Counts, mutation rates, incomers, timings and darkness formulas are explicitly game assumptions from the spec. They are not field estimates.
- Bark darkness remeasured 20.114 / 50.151 / 85.230; six rendered moth targets were within 0.008. Contrast: ink/paper 12.92, muted/paper 5.63, white/brand 6.39.
#### Sensitivity
English industrial/scientific history: check credit to named researchers, illustrative rather than documentary scenes, and the distinction between demonstrated bird selection and disputed lichen contribution.
No Native, religious, personal-body or hard-history content is introduced. No people appear; all twelve assets are marked people false. Woodland and town exteriors do not require a token worker figure.
#### Flattest moment left
The last clean-bark rounds repeat the same hunt after the lesson is visible. Their recorded population remains meaningful, but no extra mechanic or topic was added beyond the spec.
#### Graphics
All twelve images inspected, including keyed cutouts, 54-pixel moths, 130-pixel bird poses, bark in play and all four story scenes. One carbonaria redraw via the imagegen skill's built-in edit path.
Kept the field-notebook palette, rich oak textures, painted landscapes, bird and animated graphs. Compared existing Beat Lab and Snowy Mail Route bundles without rebuilding them.
Art prompt: tools/bug-hunt/art/prompts.json; final cutout: art/bh-moth-carbonaria.webp; original retained in Scratch. Final offline bundle: 2,056,608 bytes (2008.4 KiB), below 2 MiB.
#### Audit
One audit completed, exit 0, within the 40-minute limit: Chrome 9961, host 8765; 39 leads, 83 frames, in _scratch/bug-hunt/review-audit/.
- Confirmed and fixed: paused moth silhouettes and the Pause welcome mismatch; native paused/return paths now show no moths and say Resume.
- Intended overlaps: notebook labels over the canvas and modal covers over inactive field text. The prediction readout occupies clear graph space. Kept after viewing.
- Dropped breeding how-to: fixture skips the breeding beat immediately; the held-input main path spoke it. Quick mode/welcome cuts are allowed by BASELINE 16.
- Explain table pairs cached labels with newly shuffled positions; text-targeted native checks confirmed each feedback matches its actual card.
- Phone audit unavailable: port 8765 served an earlier tool-folder helper, so audit host URLs returned 404. Its phone "nothing new" is not a clean result.
- Separate 375-pixel tests covered every mode, both Run plots, unlocked/locked prediction, Hunt Pause/cards/end and Explain refusal/writing.
- Audit snapshot precedes final phone and voice repairs. Those received targeted re-shoots and held-input voice checks, without a second audit or review round.
Also viewed 28 mode/size frames across all seven STANDARDS sizes; checked calm, grayscale, keyboard, extremes and resized actions. Audit resize stress had no exceptions or stranded disabled controls.
Wave checks covered focus retention, load focus, targets, visible choices, hints/Read, state-matched speech and matching graph counts. Explain remains the named no-giveaways failure.
Evidence index: review-gallery-index.json; numeric checks: review-numbers.json and review-parent-coverage.json; later voice/phone logs: review-*-voice*.json and review-phone-predict-branch.json.
#### Left open
The spec-constrained Explain blocker and quantitative/parent-representation conflicts above prevent an unqualified PASS. No model tuning, extra assessment, new feature or kit change was made.
No recordings were created. Browser fallback speech was enabled; muted timing/log checks cannot judge narration timbre or pronunciation by listening.
All Chrome ports 9960-9967 verified closed. Windows denied taskkill for the earlier HTTP helper PID 55144; port 8765 may remain occupied. Temporary tool host removed; cleanup evidence: review-cleanup.json.
Initial short read commands completed before the explicit timeout wrapper was installed; subsequent bundles, drives and audit were process-bounded. No commits.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Bug Hunt build handoff

#### Source map

src.html starts from the kit starter and uses kit:curio CSS, sound, motion and Curio.voice.
The model-code script is pure seeded population logic. The second script owns state, canvas rendering and DOM controls.
Hunt and Run store birth snapshots; both graphs and evidence chips read those snapshots. Peck removals have separate round records.
Art tokens are declared once in an image table and bundled offline. Moth cutouts are tinted in a canvas cache per individual darkness.
The three bark WebPs were calibrated to the spec's CIE lightness scale. Measurements and all test scripts are in Scratch.

#### Decisions and spec conflicts

- Open questions: none in the spec. No owner response was required.
- Image tool used, as the build request requires. Older local-FLUX and do-not-draw language yields to this instruction.
- The opening seven-line brief incorrectly questioned the mutation schedule. It has six entries, all reached by generation 10.
- There are fourteen displayed birth populations, generations 1 to 14, and thirteen visible breeding transitions.
  These cohorts total 420 moths including the initial 30; 390 young are visibly bred after the opening cohort.
  The source's generation 0 to 14 array includes another offspring endpoint after round 14.
- Measured Hunt hill success differs from the source's claimed percentages with the literal generation labels. Do not tune gene rules to manufacture a hill.
- The original hunt_final.py checks max(out[3:9]); out[0] is the initial population, so it counts displayed generations 4 to 9.
  The spec's end rule checks displayed generations 3 to 8. This accounts for a material part of the success-rate mismatch.
- The original run5.py calls run3.breedN, which mutates only g1, the copy from parent A.
  The written Run rule mutates each passed pale copy. This build follows that written rule, including both copies.
- Birds off with four incomers and mutation can exceed 25 percent. Both off still permits incoming dark copies, so it is not strictly drift alone.
- With Birds off, 200 survivors cannot each supply a parent-A place among only 196 locally bred young.
  The shuffled order gives 196 survivors those places; random parent B can include all 200. The four remaining births are incomers.
- The final Hunt end sentence uses then reached when the final count did not fall, instead of claiming then down to.
- Explain uses a completed Hunt round as evidence availability. An untouched opening Hunt does not hide a real Run record.
- Run starts at generation 0, as its axis requires; the variation chip labels that generation honestly rather than calling it generation 1.
- Evidence inheritance says young inherit gene copies from their parents. A dark parent can produce pale young if it carries a pale copy.
- The source's contrast ratios for mauve differ slightly from recomputation. Use the measured ratios in the report.
- At phone size the field and controls stack. The compact preview preserves at least 60 percent for the Hunt field.

#### Tricky parts

Predictions lock as soon as Play, Step or History acts. Turning Predict off and on does not unlock the old pin.
The sorter is a teaching discussion, not an assessment badge. Trying all cards cannot earn a saved success score.
Pause hides the moths as well as stopping the clock. Mode changes and window blur pause Hunt.
The renderer omits moths while paused: blur alone revealed a dark moth's position. Population and locations remain unchanged for Resume.
Continue checks cardReady even when invoked directly. The card voice promises have visit tokens to reject stale resolutions.
Returning to a card after a mode change requeues its whole narration. Read retains priority through the kit queue.
Text saves inside try/catch. Clipboard denial gives a keyboard-copy fallback. Nothing is sent off the device.
Keep the kit stylesheet link in its exact starter form. HTML formatters add a closing slash that the current bundler does not recognize.
Compact Hunt end cards show their model-limits paragraph in the adjacent notebook panel so the three action buttons fit.
The explicit spec rule makes the breeding beat instant with Motion off; the hunt clock keeps its full 25 seconds.
This is a specific pacing exception to the general POLISH timing advice, recorded here rather than silently changing the spec.
History preserves Birds, New dark copies and Speed; only Reset restores all defaults.

#### Sensitivity

English industrial and scientific history is presented factually. No people appear in the twelve images.
The Real story debate should be reviewed for the distinction between soot removal and lichen recovery.
Do not imply that the garden branch art is a photograph or a measured release-site reconstruction.

#### Engine changes wanted

scripts/bundle_tool.py, bundle(): allow optional whitespace and a closing slash in the kit stylesheet link regex.
An HTML formatter produced a valid self-closing link that was left as an unresolved kit URL. This tool keeps the exact starter link as a workaround.
No kit source or bundler source was changed.

#### Scope note

Build only. No commits, branch changes or polish round.
One early command regenerated the existing ignored HTML bundles for snowy-mail-route and beat-lab to open the required bar tools.
That command wrote outside the requested two folders. It did not edit their sources. All original build content and evidence is in the authorized folders.
Do not repeat that command; open their existing bundles or copy them into Scratch for comparison.

#### Cold review repairs

Run Reset and History now draw fresh seeds; passing an explicit seed to resetRun still supports reproducible tests.
Story taps and explanation choices hush previous feedback before changing the visible state.
Retapping one refused card keeps its explanation playing; Read retains priority during feedback changes.
Run's active hint names Pause when playback is active. The 40-moth sample reserves space for its label.
The breeding label now shows the actual pale and dark parent counts, and the carbonaria cutout was repainted.
At 375 pixels, Run's Bars and Line share one plot, and both modes keep their frequent controls and graph in view.
Predict brings Line into view. Returning to Bars before placing the pin names Line as the next action.
Paused Hunt enters with the Resume instruction, and next-generation lines wait until hunting is available.
Review evidence and the bounded runner are in _scratch/bug-hunt/review-* and review_run.py.

#### Cold review limits and open decisions

The prescribed Explain cards still allow blind enumeration and reveal the longest answer. This is an open blocker,
not a passing assessment. Changing the gate or exact wording requires a spec decision under CODEX-REVIEW section 3.
Independent review runs also confirmed the Hunt/Birds-off percentage mismatch and the impossible every-parent promise
when incomers leave fewer local births than survivors. Do not change the written model to manufacture acceptance.
The single review audit finished with 39 leads. Its saved bundle predates the final targeted phone and voice repairs;
those repairs have separate native-input logs and frames. Automated phone audit coverage was unavailable because port
8765 served an earlier tool-folder helper, returning 404 for the audit host. Separate 375-pixel mode checks were used.
The audit's shuffled-card labels are cached across fresh pages; its label/feedback pairings are not reliable evidence.
All review Chrome ports 9960-9967 were verified closed. Windows denied stopping the earlier HTTP helper PID 55144;
port 8765 may remain occupied. No further process-control attempts were made, and the temporary tool host file is gone.
Suggested audit changes: verify the served host before collecting phone results, and re-read shuffled card labels per page.
No shared audit script was changed.

#### Earlier build review guidance

Read codex-report.md for measured PASS and FAIL items, screenshots, the model limitations and audit leads.
Run only the named scripts for bug-hunt. Long checks use explicit limits in _scratch/bug-hunt/run.py. Initial short read/preparation calls lacked an explicit process timeout and completed promptly.

The exact specified right-card text is longest. Equal card heights and shuffling reduce position clues,
but do not eliminate that wording giveaway; the report records the general no-giveaways check as failed.
Final audit completed with 58 leads. The final bundle was compared byte-for-byte with the focused candidate.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
