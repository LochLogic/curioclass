# Model Mechanic: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: model-mechanic

#### Built

- Garage and all three Work Orders use the shared ml-lab engine, seeded data, real nearest-neighbor votes and grouped evaluation.
- Built the matrix, time filters, 40-photo strip, evidence drawers, four-feature photo inspector, label edits, training steppers, k choices and clue switches.
- Completed orders show their repair note and enable Next. Their edits survive Garage visits. Garage resets when left. Nothing is saved.
- Added teacher notes, draft metadata, 53 voice lines, audit states, nine art assets and preview.svg. No commits or polish round.
- The single full mechanical audit timed out at 40 minutes without audit.md. This report does not claim a clean full audit.
- Process deviation: the brief's bar-tool prerequisite regenerated the ignored snowy-mail-route and beat-lab HTML bundles outside the two allowed folders. Other tools' source files were not edited.

#### Numbers check

PASS: all 17 reference table rows reproduce in Node and in the browser. The additional 11 k-value cases in Sources also match, for 28 numeric cases total.

Evidence: _scratch/model-mechanic/numbers.cjs, source-extras.cjs, all-reference-results.json and eight-labels.json. The pool has 320 items; tests have 15 day and 25 night items. No discrepancy with the specification remained.

Measured scoring was about 1 to 2 milliseconds in the checked runs, including the 320-photo maximum. Scoring uses selected numeric clues, not image pixels.

Recomputed contrast: brand ink/lime 11.26:1; ink/paper 15.62:1; ink/panel 14.19:1; muted/panel 7.77:1; lime/panel 11.01:1; focus/panel 11.51:1. Glyph letters use dark ink on the class colors.

#### Feel check

Best moment: opening a mislabeled night deer with an Empty tag, changing it to Deer, and seeing two test errors disappear on the next run. The complete eight-label path finishes at 37/40 with Deer 10/10.

Two flattest moments and repairs:
1. The initial engine rendering left a tiny matrix in a large empty corner. Centered and sized its host in real pixels, with bigger cells and compact letter keys where needed.
2. Completing an order initially left the repair note below the fold. The earned note now replaces the evidence preview and the diagonal grows into the available space. Tapping a cell still reopens inspection.

Played the full three-order sequence with held clicks. Scarcity, missing night examples and bad labels need different repairs; they produce different matrix patterns. Garage supports further experiments without a win condition.

Looked at both bar tools. Side-by-side evidence is _scratch/model-mechanic/bar-comparison.png. The finish uses a dark instrument bench, documentary camera images, large inspectors, count motion, tag flips, immediate tones and restrained repair feedback.

#### Done when

1. PASS: Garage 39/40, Day 15, Night 24; k=1 gives 37; Mask only gives 11. Browser reference checks and mask-only frame.
2. PASS: WO1 starts 32 with Fox-to-Raccoon 8. Both fox +5 steps produce 40/40 and both live goals. Held-click fox-repair and complete-journey checks.
3. PASS: WO2 starts Night 17. Night 10 each gives Night 22 and 37 overall; Mask off gives Night 22 and 36 overall. Both browser configurations checked; Mask-off path also played.
4. PASS: WO3 starts 33 with Deer-to-Empty 4. The drawer shows deer labeled Empty. k=5 gives 39. All eight UI label edits, then restoring all clues and k=1, gives 37 and Deer 10/10.
5. PASS: every reference row matches the shared engine. Independent pre-build calculation plus browser checks.
6. PASS: goals tick and untick after runs. A bad k change drops WO1 to 30, unticks Fox and disables Next. Any pending edit also disables Next.
7. PASS: changed is spoken once across five held-click changes; all five repeated score events start at a two-second tap pace. Read delays the queued score until it finishes. Next is named only after the goals enable it.
8. PASS: Run, matrix and all training steppers fit at 1280x720 and 1366x768. Through the 375 px host, numbers measure 15.36 px and matrix targets 44 px. Grayscale retains letters and X marks.
9. PASS: the matrix is the dominant stage element at 1366x768 and 1000x625 in both modes. Inspected full-size and mode frames.
10. PASS: a real cell press during the tween snaps and opens its drawer. A second Run starts immediately. Programmatic Reset during a tween restores 39/40 without an exception.
11. PASS: all nine painted assets are used; animal height follows Size, day/night backdrops differ, infrared subjects are grayscale-tinted, Empty uses grass and odd numbered photos flip. Horizontal placement is clamped to prevent body cropping.

#### Wave lessons

- Hint and voice: PASS. Hints update synchronously, Read speaks the current hint, the helper owns heard-state deduplication, and score events have distinct run keys. Checked five changes, five runs, Read and initial order speech.
- Focus and layout: PARTIAL. Native dialogs restore focus, controls stay in place, sticky hints reserve height, and keyboard arrows/Enter open cells. Phone resize during a tween preserves Run focus. Pure engine resize focus remains a follow-up below.
- Sizes: PARTIAL. Checked every required size, 44 px controls, compact inspectors and phone number size. Full toolbox access still requires scrolling in short previews and on phones.
- No giveaways: PASS. Counts, photos and neighbors are actual model evidence. There is no hidden correct-answer badge or fake result meter.
- Honest numbers: PASS. Fixed test denominators, synthetic-data disclosure, feature bars and all reference results were checked. With zero examples the model explicitly has no answer.
- Standards: PASS. Students collect a different training mix, refine a model from its errors, correct labels and examine unequal day/night outcomes. The shared family model was reused.
- Motion off: PASS. No infinite animations remain running, no scan is created, and results update immediately. All art is present.
- Short choices visible: PASS in the checked layouts. The compact inspector shows all four 44 px relabel buttons; the five k buttons fit at 1000 px. Long photo evidence lists intentionally scroll.
- Resize mid-animation: PASS in targeted phone tests and ordinary playback. The result remains 37/40 and Run retains focus across 375-to-760-to-375 resizing.
- Deferred welcome: PASS. The two-mode helper uses no welcomeAfter. First actions speak their own line; the initial Work Orders entry speaks its welcome and order title in order.
- Unknown as unknown: PASS. Zero training produces No answer, rather than an invented animal prediction.
- One look, one meaning: PASS. Colored letters identify classes, diagonal outlines mark correct cells and red X notches mark errors. Night tint affects images, not answer tags or notches.
- Truthful badge: PASS. Stale results gray immediately; live goals and Next reflect the last completed run and pending edits disable advancement.
- Hint changes back: PASS. Returning to a completed order restores the Goal met hint. Closing its inspection restores the repair note.
- No answer by word copying: PASS. Repair controls are real model levers. The debrief names the fault after a successful repair.

#### Audit leads

Audit not finished. Ran audit_tool.py once on port 9971 with host port 8775, under a 2400-second limit. It generated 54 frames and continued walking controls, then the limit terminated it. It did not produce audit.md or a complete leads list.

Inspected every generated audit frame. Visible issues repaired with targeted checks: hint loss while the toolbox scrolls, phone Run access, short-screen inspector choices, zero-model cell sizes, answer-tag consistency when opening test photos and night notch colors. Additional targeted checks cover all eight label edits, completed-order inspection, Read ordering and Reset during a tween.

The full audit was not rerun after repairs, as directed. Completed targeted drive batches reported no tool console errors, warnings or exceptions. One earlier host-only favicon 404 was removed by giving the temporary host a data favicon; later phone batches had no errors.

#### Frames looked at

Inspected 87 manual PNG frames and 54 audit PNG frames, individually or on contact sheets, plus the final-size art and bar comparison. Evidence stays under _scratch/model-mechanic/.

Manual coverage includes every STANDARDS size in both modes, the complete order sequence, goal reversal, all reference scores, day/night filtering through the UI, drawers, large photos, label repair, zero/max training, Mask-only, grayscale, Motion off, keyboard navigation, resize and mid-tween input. Final art frames were inspected after rekeying.

#### Art made

9 finished images: 7 new OpenAI gpt-image cutouts and two preserved FLUX clearing backgrounds. No people. Full prompts and provenance are in art/prompts.json; raw new images are in art/raw/.

Art totals 481,704 bytes, about 470 KiB. The final offline bundle is 745,046 bytes, about 728 KiB on disk, under 2 MB. The bundler reports 725 KB before on-disk line-ending overhead.

No generation redraws were needed. Rekey processing was repeated to remove magenta and blue fringes. Final options use holes=true and despill=false. Inspected the final scene, deer inspector, preview and all seven cutouts at final asset size.

#### Art still to paint

None missing. Fine key-colored edge specks remain visible on some isolated cutouts at full resolution; their final forest composites were inspected. This is a possible future matte refinement, not a placeholder.

#### Engine changes wanted

See handoff.md for exact files and functions: preserve cell focus in ml-lab resize redraws; allow separate truth rows and prediction columns for abstention; fix the art pipeline's sequential magenta despill mask. No shared engine or script was edited.

#### Left open

- A completed mechanical audit remains open. The 40-minute run timed out, and scoped rechecks do not replace it.
- Short previews and phones scroll for training controls, complaints, longer repair notes and evidence. Run is sticky and the phone matrix/hint fit initially; all primary controls fit together on the specified laptops.
- Browser narration is unrecorded, as required for this build. The science-narrator selection and 53 lines are prepared; actual voice identity and offline speech depend on installed browser voices.
- Pure ResizeObserver redraws inside the shared matrix engine can still require focus work. The tested phone Run focus path passes; a full matrix-cell resize focus audit was not completed.
- Zero training uses a fifth No answer column plus an unused zero row because the engine is square. A relabeled example can also make a zero-count animal label predictable; the spec's blanket statement has that label-edit exception.
- Kept the spec's painted-cutout direction: only Size changes the painting; all four numeric clues appear as bars. This open-question decision and the clamped horizontal placement are recorded in handoff.md.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: model-mechanic
#### Played
Cold as a grade 7 student: Garage, error drawer, nearest-match inspector, all three work orders and the final repair note, before reading builder notes or source. Strong documentary evidence and a real, satisfying label repair; short previews remain cramped.

#### Findings fixed
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

#### Findings left
- Blocker, family:ml-lab, diagnostic mastery: cycling k and clues can meet all work-order goals without reading a matrix or opening evidence. Reproduced before and after repairs. The spec explicitly accepts these repairs; a diagnosis gate would be a new feature. This remains a specification conflict, not a clean pass.
- Should fix, general, short layouts: at 680x425 and 800x500 some toolbox controls require panel scrolling; at 375 wide the training panel is below the stage. The laptop layouts fit Run, matrix and steppers. Meeting the stricter every-control/every-size rule needs an approved compact-layout change, not smaller targets or stripped art.
- Polish, family:ml-lab, zero training: the shared square matrix includes an unused No answer truth row. The accurate abstention column and explanatory notes remain; a rectangular engine API is still wanted.

#### Break it
- Overall, Day, Night and every class count: independently regenerated seeds 601/602 and all 17 reference table rows, plus 11 extra k cases; 17 browser results agree. Counts are actual held-out classifications, not button-count rewards.
- WO1: swept all five k buttons with Run; k=1 genuinely meets the specified goals. k=9 lowers accuracy to 30/40 and unticks Fox. No score bypass was hidden or called fixed.
- WO2: the cheap Mask-off experiment genuinely reaches Night 22/25 and total 36/40. Trying k alone never repairs the missing night examples.
- WO3: cheap k=5 genuinely reaches 39/40. Also repaired all eight bad labels with real held CDP clicks through the UI; restoring all clues and k=1 gives 37/40 and Deer 10/10.
- Next/Start again: repeated Run, disabled Next, Reset, mode spam, Day filtering and a post-success edit cannot advance a failing or dirty order. Numerical k/clue trial-and-error completion remains open above.
- Extremes: all-zero training gives 0/40 and No answer; no clues gives 10/40; maximum 320 examples gives 37/40. More data is not rewarded automatically. No saved best score or reflection gate exists.
- Relabeling: one correct label repair improves the real result to 35/40 without clearing the Deer goal. Labels are training data only; test truth stays fixed. Stale evidence is explicitly marked after edits.

#### Voice walk
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

#### Facts checked
- Truth/prediction matrix counts, accuracy and why total accuracy can hide group failures: [Google ML Crash Course, Classification](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall).
- Nearest k voting, Euclidean clues and larger k suppressing noise: [scikit-learn, Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html). Stable tie order is this shared engine's documented rule, not a universal ML claim.
- Eight bad labels and all numeric fixes: `spec.md` generation rules, independent `recompute-spec.py`, `review-numbers.json`, browser-numbers-result.json and all-eight-ui-result.json. Synthetic feature ranges, seeds and Mask x0.35 are teaching assumptions, now labeled as such.
- Empty camera frames and ML classification: [Norouzzadeh et al., PNAS 2018](https://www.pnas.org/doi/10.1073/pnas.1719367115). Moving vegetation false triggers: [Smithsonian eMammal camera-trap guidance](https://emammal.si.edu/training/camera-trap-training); weather-driven vegetation: WABSI, Camera Trapping Guide 2018.
- Monochrome infrared: Rovero, Zimmermann, Berzi and Meek, Hystrix 24(2), 2013, doi:10.4404/hystrix-24.2-6316. It does not establish this toy's universal mask-loss claim; that claim was corrected.
- Mostly nocturnal raccoons: NWF Raccoon guide and Connecticut DEEP Raccoon fact sheet; fox twilight/night activity: Minnesota DNR Red Fox; deer dawn/dusk: Florida FWC Living with White-Tailed Deer. The 15-day/25-night sample split is synthetic, not population prevalence.
- CSTA crosswalk wording: [CSTA revised 2017 standards](https://csteachers.org/wp-content/uploads/2025/03/csta-k-12-computer-science-standards-revised.pdf). Model refinement and data cleaning are student actions; 2-IC-21 accessibility discussion is explicitly partial. Module IDs match data/modules.csv.
- Recomputed contrast: ink/panel 14.19:1, muted/panel 7.77:1, brand ink/lime 11.26:1, focus/panel 11.51:1.

#### Sensitivity
None requiring a cultural reviewer: a fictional wildlife preserve, animal classes and empty frames, without human culture, religion, hard history or bodies. No people assets; no people were needed in camera photographs. Bias is described as unequal training-data coverage, not as a claim about a human community.

#### Flattest moment left
Night-shift data entry takes repeated +5 taps. They are real experiments, but the numerical goal can still substitute for diagnosis. Fixing that needs the spec decision named above.

#### Graphics
All nine assets inspected individually and in composites: both forest clearings, day/night deer, fox and raccoon, wind grass. No missing art tokens. New night raccoon matches the set and preserves infrared anatomy/contrast. Isolated keyed edges retain tiny specks; the final night composite is grayscale and clean at its actual display size.
Inspected every manual frame, individually or on labeled contact sheets, including all STANDARDS sizes, 375 iframe, inspector sizes, extremes, final payoff, grayscale, Motion off and the two bar tools. Kept the rich art. Finished art 475.8 KiB; final bundle 743.9 KiB (761770 bytes).

#### Audit
Audit not finished: the single run reached its 2400 s limit; the last saved phase is "clicks done, stress checks next". Automatic checks after that checkpoint are unverified; manual repeat and voice checks above are separate evidence.
`_scratch/model-mechanic/review-audit/audit.md` records 320 mechanical leads and 59 frames, all inspected. The frozen audited file is review-audit/host/tool.html; the final scoped fixes were not given a second full audit.
Confirmed and fixed: scroll-heading occlusion, Next focus loss, phone Next below the fold, and undersized/clipped empty-model cells. Targeted final frames cover every size affected by the toolbox wrapper, both Next focus cases, 375 px advancement/inspector/resize, and the exact main-path voice walk.
Checker-only leads: intentionally hidden original legend text replaced by visible 10 px pseudo text; the matrix behind a native modal; modal content covering inert background controls; first-tap welcomes skipped for an action's own speech, permitted by BASELINE 16. The modal keep-region declaration was corrected. Expected control movement on mode changes is not a panel jump.
The saved repeat entries for ten controls are clean. Quick-tap welcome cuts on mode/Reset controls are intentional cancellations; the premise remains in the hint and Read. The timeout process-tree cleanup was denied by Windows; the owned Chrome was then closed through CDP and the owned audit process was stopped.
The short-layout limits and specification-level diagnosis shortcut stay open above. All post-fix drive batches have no tool console warnings, errors or exceptions. No owned Chrome debugging or host port remains open, and host.html is removed.

#### Left open
No diagnosis gate or extra topic was added; the specification-level shortcut and short-layout conflict remain explicit. The painted-cutout choice follows the spec: only Size changes the painting; other clues stay in bars. No kit or spec edits and no git commits.
The first two read-only documentation/location commands did not have a subprocess timeout; they returned in under a second. All subsequent shell commands were bounded. Harness-only favicon 404s occurred on the temporary phone host; they are not requests made by the offline tool. Two offscreen inspector fixtures were corrected and re-shot successfully.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Model Mechanic handoff

Build only, 2026-11-02. No commits. Start with src.html, the spec and codex-report.md for checks and limitations.

#### Structure

src.html starts from the kit starter. Its CSS lays out an instrument bench, with the toolbox before the stage in DOM keyboard order. Data generation uses MLLab.rng, uni and r2. Training uses the family knn model; evaluation and confusion rendering use the family engine. No kit files were edited.

Work Orders keep their current index, labels and edits across Garage switches. Garage resets when left, so its edited labels last until Reset or a mode change. evaluate computes results; run updates goals and starts a 400 ms count tween. snapTween finalizes that tween before student input. Photo inspectors are native modal dialogs with focus restoration. Fixed training order is animal, day, night. WO3 wrong label indices differ by day and night because the specification counts all thirty deer together.

revision changes when the configuration changes. Each score event has a unique run key, so repeated identical scores are not collapsed at a two-second tap pace. Do not replace those keys with one shared score key. Completed orders can still be inspected, and closing the drawer restores their repair note. Test photos keep the model's answer tag when enlarged and show the true animal in a separate caption.

Responsive controls move the hint above the phone stage and put Run, Reset and the existing order-advance button in the phone header. Desktop hints and Run sit outside the clipped toolbox-body scroller, whose training headings stay visible. The short landscape photo inspector uses two columns so all four label choices stay visible. The smallest landscape matrices place time tabs on the right to preserve 44 px cells. Narrow matrices use letter labels with an explicit species key.

#### Open question decision

Took the spec's painted-cutout direction: seven animal/grass assets sized by Size, four measured values shown as bars when enlarged. The scene explicitly says the paintings do not encode every feature. Exact classification uses all selected numeric clues. No code silhouettes substituted.

#### Art

Preserved both existing FLUX clearings. Seven new assets made with the built-in imagegen tool and copied to art/raw, then processed only with art.py --rekey. Full subject prompts and house style are in art/prompts.json. No people.

Final cutout options are holes=true and despill=false. The shared magenta despill pass left blue edge pixels; the hole-aware rekey removes that blue fringe. Fine key-colored specks can still be found at full asset resolution, but the final in-scene frames were inspected after processing.

#### Engine changes wanted

- `kit/ml-lab.js`, `view.confusion` / its `host` redraw: capture the focused cell's row and column before clearing the SVG, then focus the replacement with preventScroll after resize. The cold review adds a local focus observer around this tool; a shared fix would still help other tools.
- `kit/ml-lab.js`, `view.confusion`: allow distinct rowClasses and colClasses. The zero-training workaround currently uses a fifth No answer column plus an unused zero truth row. Four truth rows and a separate abstention column would express this edge case more cleanly. No kit file was edited.
- `scripts/art.py`, `cut_out`, magenta despill branch: compute the spill mask before changing either red or blue, then apply it to both channels. Recomputing the condition after red changes can leave blue edges. This build uses the existing holes option instead; the shared script was not edited.

#### Follow-up

The single mechanical audit reached its 40-minute cap without writing audit.md. All 54 generated audit frames were inspected. Targeted checks passed after repairs, but this is not a completed full audit. Evidence and profiles are in _scratch/model-mechanic. No Chrome or server should remain running, and host.html is removed.

Narration is browser fallback, with science-narrator and every fixed line prepared in voice/lines.json. Do not record automatically. Browser voice identity and offline speech depend on the browser's installed voices.

#### Specification edge cases

- Kept Size height exact and clamped the seeded horizontal position to keep animals inside their frames. The unclamped 10-to-60-percent left positions can crop wide fox and raccoon cutouts.
- A zero-count animal can still be predicted if the student gives its label to another animal. This is correct nearest-neighbor behavior and an exception to the spec's blanket zero-count prediction statement.
- All eight wrong labels are reachable using Size only and k=9. Restore all clues and k=1 for the reference 37/40 result.

#### Cold review changes

Reviewed cold on 2026-11-07. Evidence is in _scratch/model-mechanic/review-* and the final codex-review.md. The matrix still uses the shared engine. Local wrappers label axes explicitly, preserve focus across engine redraws, and animate actual prediction changes along curved paths during the existing 400 ms tween. Completed notes summarize the current run. The training table now reserves space for full 44 px buttons.

Modal instructions have separate once-only trainingPhoto and testPhoto voice lines, included in lines.json. Read uses the visible modal instruction while an inspector is open. The Mask reduction is explicitly simulated.

Left open by the spec: numerical completion can be found by sweeping k or clues. No additional quiz or diagnosis gate was added. A result is an accurate measurement, but it is not proof that the student diagnosed the fault.

The CSTA 2017 crosswalk 2-IC-21 is partial: students explore biased data, but do not discuss accessibility in technology design. Notes now qualify that claim. Adding that topic would exceed this spec.

Audit-confirmed repairs: Next moves focus to Run before becoming disabled; the toolbox clips scrolling content below fixed instructions/actions; the empty-model 680 px layout reserves full 44 px matrix targets and puts the No answer key in the score strip. The modal audit state keeps the inspector, rather than the intentionally covered matrix. The full audit used the frozen pre-repair bundle; only affected layouts and interactions were re-shot afterward.

#### Sensitivity

None requiring a cultural lens: a fictional wildlife preserve, three animal classes and empty frames, without people, culture, religion, hard history or human bodies. The unequal-data analogy is limited to this simulated classifier.

#### Cold review audit outcome

Audit not finished: the single run reached its 2400 s limit; the last saved phase is "clicks done, stress checks next". Automatic checks after that checkpoint are unverified; manual repeat and voice checks above are separate evidence.

Final targeted checks and report are in codex-review.md; detailed evidence and the validation manifest are in _scratch/model-mechanic. The fixed-line registry contains 63 lines, including registered Read parts, empty-evidence guidance and inspector instructions. No git commit was made. All owned Chrome and host ports are closed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
