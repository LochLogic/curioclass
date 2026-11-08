# Codex review: model-mechanic
## Played
Cold as a grade 7 student: Garage, error drawer, nearest-match inspector, all three work orders and the final repair note, before reading builder notes or source. Strong documentary evidence and a real, satisfying label repair; short previews remain cramped.

## Findings fixed
- Should fix, general, `src.html`: training buttons clipped horizontally at 1280x720. Fixed table column sizing while keeping every button 44 px; rechecked all sizes.
- Should fix, family:ml-lab, matrix: row and column titles looked like two column headings. Labels now explicitly say Rows: real animal and Columns: model answer.
- Should fix, general, narration: the long welcome could hold the drawer instruction until its screen had gone. State transitions stop stale ordinary speech while retaining Read priority. Both mode how-to lines start on the main path.
- Should fix, general, photo inspector: no voiced next action and the header Read was inert behind a modal. Added once-only instructions, modal Read and consistent Close/Escape handling using the kit queue, with visible current instructions.
- Should fix, general, empty evidence: an empty square and a run with no training data incorrectly used the ordinary matched-photo instruction. Each now has an accurate, voiced next action.
- Should fix, general, Read recordings: dynamic result hints and filter/return instructions were outside the fixed-line registry. Read now uses registered score and action parts; every fixed hint is prepared for recording.
- Should fix, family:ml-lab, pending edits: the previous successful explanation remained beside a changed model. Hide that debrief until a new test; mark old evidence and the bench state explicitly.
- Should fix, general, science wording: the night debrief implied real infrared always removes raccoon masks. It now names the Mask reduction as a simulation assumption and limits the unequal-impact claim to this test set.
- Should fix, general, standards claim: notes now qualify 2-IC-21 as partial coverage, since its accessibility-design discussion is outside this tool.
- Polish, general, flattest result: real prediction changes now travel between matrix cells during the specified 400 ms tween. The repair note reports errors corrected, new errors and errors remaining for this student's last run.
- Polish, general, focus: a local observer restores the focused matrix cell after the engine replaces its SVG. Verified direct host resize and arrow-key/Enter inspection.
- Polish, general, weakest art: redrew night raccoon, then revised its face mask to retain the pale infrared teaching cue. Preserved the rest of the documentary set and dark lime bench.
- Should fix, general, audit leads: scrolling headings could sit under sticky Run. Fixed instructions/actions now sit outside a clipped toolbox scroller, with sticky training column headings.
- Should fix, general, audit leads: Next disabled itself under keyboard focus. It now transfers focus to Run; on phones the existing Next/Start again button moves beside Run.
- Should fix, family:ml-lab, audit leads: the zero-training preview had 41 px cells, 9 px glyphs and a clipped last row. Widened it to 43.8 px targets (44 px rounded), with 10 px glyphs and a fully visible matrix; No answer now has a key in the score strip.

## Findings left
- Blocker, family:ml-lab, diagnostic mastery: cycling k and clues can meet all work-order goals without reading a matrix or opening evidence. Reproduced before and after repairs. The spec explicitly accepts these repairs; a diagnosis gate would be a new feature. This remains a specification conflict, not a clean pass.
- Should fix, general, short layouts: at 680x425 and 800x500 some toolbox controls require panel scrolling; at 375 wide the training panel is below the stage. The laptop layouts fit Run, matrix and steppers. Meeting the stricter every-control/every-size rule needs an approved compact-layout change, not smaller targets or stripped art.
- Polish, family:ml-lab, zero training: the shared square matrix includes an unused No answer truth row. The accurate abstention column and explanatory notes remain; a rectangular engine API is still wanted.

## Break it
- Overall, Day, Night and every class count: independently regenerated seeds 601/602 and all 17 reference table rows, plus 11 extra k cases; 17 browser results agree. Counts are actual held-out classifications, not button-count rewards.
- WO1: swept all five k buttons with Run; k=1 genuinely meets the specified goals. k=9 lowers accuracy to 30/40 and unticks Fox. No score bypass was hidden or called fixed.
- WO2: the cheap Mask-off experiment genuinely reaches Night 22/25 and total 36/40. Trying k alone never repairs the missing night examples.
- WO3: cheap k=5 genuinely reaches 39/40. Also repaired all eight bad labels with real held CDP clicks through the UI; restoring all clues and k=1 gives 37/40 and Deer 10/10.
- Next/Start again: repeated Run, disabled Next, Reset, mode spam, Day filtering and a post-success edit cannot advance a failing or dirty order. Numerical k/clue trial-and-error completion remains open above.
- Extremes: all-zero training gives 0/40 and No answer; no clues gives 10/40; maximum 320 examples gives 37/40. More data is not rewarded automatically. No saved best score or reflection gate exists.
- Relabeling: one correct label repair improves the real result to 35/40 without clearing the Deer goal. Labels are training data only; test truth stays fixed. Stale evidence is explicitly marked after edits.

## Voice walk
Held clicks, 2 s gaps, default Sound and Motion: title tap, Raccoon/Fox error square, training photo, Close, k=1, Run; Work Orders, Fox/Raccoon error square and its training photo, Close, Fox day/night +5, Run, Next; Raccoon/Fox error and training photo, Close, Mask off, Run, Next; Deer/Empty error and training photo, Close, k=5, Run.
Started in order: wGarage, drawer, trainingPhoto, changed, score37, wOrders, score40, order2, score36, order3, score39, allDone. Both mode welcomes/how-to lines start once. Actions may cut the first welcome, as BASELINE 16 allows.
Order1 and the two intermediate goalMet events become stale when the student changes or advances at this pace; they are dropped rather than spoken over a later order. Final allDone is heard after score39.

| Line | Kind | Expected starts | Observed |
|---|---|---:|---:|
| changed across five real changes | how | 1 | 1 |
| identical score across five Runs | event | 5 | 5 |
| diagonal across five cell taps | how | 1 | 1 |
| wGarage / wOrders on main path | welcome | 1 each | 1 each |

First Read reads only the hint; first Sound speaks nothing; first mode enters that mode. Read in a photo uses its visible instruction. Read followed by a change waits before the result; a mode switch releases it immediately. The 63 allLines strings match lines.json. Browser speech fallback remains unrecorded.

## Facts checked
- Truth/prediction matrix counts, accuracy and why total accuracy can hide group failures: [Google ML Crash Course, Classification](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall).
- Nearest k voting, Euclidean clues and larger k suppressing noise: [scikit-learn, Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html). Stable tie order is this shared engine's documented rule, not a universal ML claim.
- Eight bad labels and all numeric fixes: `spec.md` generation rules, independent `recompute-spec.py`, `review-numbers.json`, browser-numbers-result.json and all-eight-ui-result.json. Synthetic feature ranges, seeds and Mask x0.35 are teaching assumptions, now labeled as such.
- Empty camera frames and ML classification: [Norouzzadeh et al., PNAS 2018](https://www.pnas.org/doi/10.1073/pnas.1719367115). Moving vegetation false triggers: [Smithsonian eMammal camera-trap guidance](https://emammal.si.edu/training/camera-trap-training); weather-driven vegetation: WABSI, Camera Trapping Guide 2018.
- Monochrome infrared: Rovero, Zimmermann, Berzi and Meek, Hystrix 24(2), 2013, doi:10.4404/hystrix-24.2-6316. It does not establish this toy's universal mask-loss claim; that claim was corrected.
- Mostly nocturnal raccoons: NWF Raccoon guide and Connecticut DEEP Raccoon fact sheet; fox twilight/night activity: Minnesota DNR Red Fox; deer dawn/dusk: Florida FWC Living with White-Tailed Deer. The 15-day/25-night sample split is synthetic, not population prevalence.
- CSTA crosswalk wording: [CSTA revised 2017 standards](https://csteachers.org/wp-content/uploads/2025/03/csta-k-12-computer-science-standards-revised.pdf). Model refinement and data cleaning are student actions; 2-IC-21 accessibility discussion is explicitly partial. Module IDs match data/modules.csv.
- Recomputed contrast: ink/panel 14.19:1, muted/panel 7.77:1, brand ink/lime 11.26:1, focus/panel 11.51:1.

## Sensitivity
None requiring a cultural reviewer: a fictional wildlife preserve, animal classes and empty frames, without human culture, religion, hard history or bodies. No people assets; no people were needed in camera photographs. Bias is described as unequal training-data coverage, not as a claim about a human community.

## Flattest moment left
Night-shift data entry takes repeated +5 taps. They are real experiments, but the numerical goal can still substitute for diagnosis. Fixing that needs the spec decision named above.

## Graphics
All nine assets inspected individually and in composites: both forest clearings, day/night deer, fox and raccoon, wind grass. No missing art tokens. New night raccoon matches the set and preserves infrared anatomy/contrast. Isolated keyed edges retain tiny specks; the final night composite is grayscale and clean at its actual display size.
Inspected every manual frame, individually or on labeled contact sheets, including all STANDARDS sizes, 375 iframe, inspector sizes, extremes, final payoff, grayscale, Motion off and the two bar tools. Kept the rich art. Finished art 475.8 KiB; final bundle 743.9 KiB (761770 bytes).

## Audit
Audit not finished: the single run reached its 2400 s limit; the last saved phase is "clicks done, stress checks next". Automatic checks after that checkpoint are unverified; manual repeat and voice checks above are separate evidence.
`_scratch/model-mechanic/review-audit/audit.md` records 320 mechanical leads and 59 frames, all inspected. The frozen audited file is review-audit/host/tool.html; the final scoped fixes were not given a second full audit.
Confirmed and fixed: scroll-heading occlusion, Next focus loss, phone Next below the fold, and undersized/clipped empty-model cells. Targeted final frames cover every size affected by the toolbox wrapper, both Next focus cases, 375 px advancement/inspector/resize, and the exact main-path voice walk.
Checker-only leads: intentionally hidden original legend text replaced by visible 10 px pseudo text; the matrix behind a native modal; modal content covering inert background controls; first-tap welcomes skipped for an action's own speech, permitted by BASELINE 16. The modal keep-region declaration was corrected. Expected control movement on mode changes is not a panel jump.
The saved repeat entries for ten controls are clean. Quick-tap welcome cuts on mode/Reset controls are intentional cancellations; the premise remains in the hint and Read. The timeout process-tree cleanup was denied by Windows; the owned Chrome was then closed through CDP and the owned audit process was stopped.
The short-layout limits and specification-level diagnosis shortcut stay open above. All post-fix drive batches have no tool console warnings, errors or exceptions. No owned Chrome debugging or host port remains open, and host.html is removed.

## Left open
No diagnosis gate or extra topic was added; the specification-level shortcut and short-layout conflict remain explicit. The painted-cutout choice follows the spec: only Size changes the painting; other clues stay in bars. No kit or spec edits and no git commits.
The first two read-only documentation/location commands did not have a subprocess timeout; they returned in under a second. All subsequent shell commands were bounded. Harness-only favicon 404s occurred on the temporary phone host; they are not requests made by the offline tool. Two offscreen inspector fixtures were corrected and re-shot successfully.
