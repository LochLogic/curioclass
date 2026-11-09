# Bug Hunt build handoff

## Source map

src.html starts from the kit starter and uses kit:curio CSS, sound, motion and Curio.voice.
The model-code script is pure seeded population logic. The second script owns state, canvas rendering and DOM controls.
Hunt and Run store birth snapshots; both graphs and evidence chips read those snapshots. Peck removals have separate round records.
Art tokens are declared once in an image table and bundled offline. Moth cutouts are tinted in a canvas cache per individual darkness.
The three bark WebPs were calibrated to the spec's CIE lightness scale. Measurements and all test scripts are in Scratch.

## Decisions and spec conflicts

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

## Tricky parts

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

## Sensitivity

English industrial and scientific history is presented factually. No people appear in the twelve images.
The Real story debate should be reviewed for the distinction between soot removal and lichen recovery.
Do not imply that the garden branch art is a photograph or a measured release-site reconstruction.

## Engine changes wanted

scripts/bundle_tool.py, bundle(): allow optional whitespace and a closing slash in the kit stylesheet link regex.
An HTML formatter produced a valid self-closing link that was left as an unresolved kit URL. This tool keeps the exact starter link as a workaround.
No kit source or bundler source was changed.

## Scope note

Build only. No commits, branch changes or polish round.
One early command regenerated the existing ignored HTML bundles for snowy-mail-route and beat-lab to open the required bar tools.
That command wrote outside the requested two folders. It did not edit their sources. All original build content and evidence is in the authorized folders.
Do not repeat that command; open their existing bundles or copy them into Scratch for comparison.

## Cold review repairs

Run Reset and History now draw fresh seeds; passing an explicit seed to resetRun still supports reproducible tests.
Story taps and explanation choices hush previous feedback before changing the visible state.
Retapping one refused card keeps its explanation playing; Read retains priority during feedback changes.
Run's active hint names Pause when playback is active. The 40-moth sample reserves space for its label.
The breeding label now shows the actual pale and dark parent counts, and the carbonaria cutout was repainted.
At 375 pixels, Run's Bars and Line share one plot, and both modes keep their frequent controls and graph in view.
Predict brings Line into view. Returning to Bars before placing the pin names Line as the next action.
Paused Hunt enters with the Resume instruction, and next-generation lines wait until hunting is available.
Review evidence and the bounded runner are in _scratch/bug-hunt/review-* and review_run.py.

## Cold review limits and open decisions

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

## Earlier build review guidance

Read codex-report.md for measured PASS and FAIL items, screenshots, the model limitations and audit leads.
Run only the named scripts for bug-hunt. Long checks use explicit limits in _scratch/bug-hunt/run.py. Initial short read/preparation calls lacked an explicit process timeout and completed promptly.

The exact specified right-card text is longest. Equal card heights and shuffling reduce position clues,
but do not eliminate that wording giveaway; the report records the general no-giveaways check as failed.
Final audit completed with 58 leads. The final bundle was compared byte-for-byte with the focused candidate.
