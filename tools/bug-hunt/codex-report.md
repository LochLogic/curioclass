# Codex report: bug-hunt

## Built

Built Hunt, Run, Explain and Real story in one offline HTML file, using the shared kit and twelve original paintings.
Hunt has seeded inheritance, two habitat changes, keyboard pecking, a miss lockout, pause blur and an honest ending.
Run has live controls, 200 moths, History, prediction locking and a 120-generation limit.
Explain uses the player's actual records and device-only writing. Real story has eight stops and disconnected historical points.
This was Build only. No commits or polish round. Draft metadata remains stage built.

## Numbers check

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

## Facts checked

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

## Break it

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

## Voice walk

Main held-click path: miss, breed, sootCard, nextGen, cleanCard, huntEnd, welcomeExplain, cardWrongA, chips,
welcomeRun, history, welcomeStory, stop2, stop7. Other stop events went stale when the student moved to a different stop.
The first welcome was skipped by acting, which BASELINE 16 allows; its instructions remained in the hint and Read.
Each heard how line started once. Five repeated misses at a two-second tap pace started miss only once.
Wrong-card feedback updated immediately even when its queued speech became stale. All four modes' instructions were available on the path.
The side path covered keyboard pecking, Read, live History takeover, writing and reload; the gate path tested Read interruption separately.
Soot and clean card narration finished before Continue acted in the full hunt. No chip instruction played with absent evidence.
No recordings were made. The 28 fixed lines use Curio.voice with browser speech fallback; bank/style metadata is casual-peer.
Evidence: play/session.json, voice-breaks/results.json and card-read-result.json.

## Feel check

Best moment: soot reverses which painted moths disappear into the tree, followed by the student's own birth counts.
History's steep decline on clean bark is an earned visual comparison with a small-population Hunt that may have a low peak.
Flattest moment 1: the old breeding swap felt abrupt. Added survivor pulsing, a newborn fade and moving bar heights.
Flattest moment 2: compact hints covered the timeline and writing actions. Moved those hints into the notebook panel and reserved graph space.
Played the complete fourteen-round Hunt through Explain, History and all eight story stops using native held input.
Compared Hunt with Snowy Mail Route and History with Beat Lab in Scratch/bar-comparison.png. The paintings hold up beside both bars.
No separate polish round was started.

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

Looked at all 95 audit PNGs on twelve labeled sheets, plus the full seven-size, four-mode set (28 frames).
Also reviewed native play (13), voice side path (3), phone modes (4), extremes (6), targeted layout checks (10),
the corrected Read gate, eight post-audit desktop frames, two phone modal frames and the final root-bundle frame.
Early art/previews and the bar comparison were viewed. Scratch retains the individual frames and labeled sheets.
Final smoke: candidate and root bundle bytes match; the smaller held-input retry logged zero errors, warnings or exceptions.

## Art made

Twelve images generated with the built-in OpenAI image tool; prompts and original PNGs are in art/prompts.json and art/raw/.
Finished cutouts were inspected, keyed with the required free art.py --rekey form, and despilled.
Three barks were measured and tinted; moths retain wing detail while tinting to their own darkness at runtime.
No generation redraw was needed. Processing revisions corrected key fringes and calibrated darkness.
Art: 1414.256 KiB. Voice recordings: 0 KiB. Final HTML: 2004.019 KiB (2,052,115 bytes).
This is about 2.05 MB against the 2 MB goal. Background quality is 72; no teaching image was removed to meet a hard cap.

## Art still to paint

None. No people appear; every asset explicitly has people false.

## Engine changes wanted

scripts/bundle_tool.py, bundle(): accept an optional slash in kit stylesheet links. A formatter's valid self-closing link was not inlined.
The exact starter tag is restored here, and the final bundle has no unresolved asset URLs. No shared source was changed.

## Left open

- Source statistical disagreements above, the specified sorter answer-length giveaway, and the native calm/mashing batch that stopped twice at its limits.
- The extra final two-shot smoke lost its Chrome connection; a smaller one-shot retry passed with zero browser errors.
- Browser narration quality was not judged by listening, because all automated Chrome sessions were muted as required.
- Windows desktop/headless verification is not a physical Chromebook or screen-reader user trial.
- One early bar-tool bundling command regenerated their existing ignored HTML outside the two authorized folders. Their sources were untouched.
  This scope mistake is recorded in handoff.md. Subsequent authored files and evidence stayed inside the two authorized folders.
- Initial short read/preparation commands lacked an explicit process timeout and completed promptly; subsequent scripts used explicit timeout wrappers.
- The report was drafted in Scratch and finalized last to honor the user's instruction to stop immediately when it is written.
All started Chrome instances and HTTP servers are closed; ports 9990 to 9997 and 8795 were checked closed. host.html is absent.
