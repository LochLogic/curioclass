# AI Evaluator

## One idea
A vendor says its pothole-spotting AI is 98 percent accurate; you are the city's evaluator, you choose which photos to test it on, and the city map lights up where that number holds and where it falls apart (old Eastfield roads, rainy days), so you learn that a score is only as good as the test set behind it, then decide which of three model types the city should ship, if any.

## Not like
- model-mechanic (same family, 6-8): there you open the model and fix it. Here you can't touch the model; you design the test, read the training data sheet, ask the vendor for better data and make the release call.
- biased-bot (same family, grade 4): shows one missing group by running everyone. Here nobody hands you the groups: the vendor's own test looks perfect, and you find the weak slices by choosing what to test.
- algorithm-audit (6-8 roleplay): audits a rule-based school algorithm and debates tradeoffs. Here the system learned from data, and the evidence is measured: slices, precision, recall, a threshold.
- data-policy-council (9-12 roleplay): drafts privacy policy. This is a technical evaluation with a written verdict, no council roleplay.
- simulation-studio, sorting-showdown (9-12): simulations and algorithm speed. Here the object of study is a trained model's errors.

## Who and how
- Grades 9 to 12, computer science. Module: Building and Evaluating AI (Algorithms and Programming). Topic line: "testing AI models for accuracy and bias".
- Driver: students on laptops, alone or in pairs. 30 to 45 minutes (one class period).
- Standards: HS-ALG-ML-06, HS-ALG-ML-07, HS-ALG-ML-08, HS-ALG-PS-05, HS-SOC-HU-43, HS-ALG-IM-11 (module codes). CSTA 2017 crosswalk: 3B-AP-08 (describe how AI drives software systems), 3A-IC-25 (test and refine computational artifacts to reduce bias and equity deficits), 3B-DA-07 (evaluate the ability of models to support claims), 3A-IC-24 (evaluate how computing impacts social and economic practices). References: Mitchell et al., "Model Cards for Model Reporting" (disaggregated evaluation); Google Machine Learning Crash Course (precision, recall, thresholds).
- tool.json: driver "students", minutes "30-45", modes [] (one guided workspace with steps; no score), grades_label "Grades 9-12".

## Screens and modes
Kit frame with the 9-12 theme (`kit:theme-912`). Header: title "AI Evaluator" with small line "Riverton Street Report", Motion, Sound, Read. Under the header, a step bar of five tabs (always clickable, not a forced order): "1 Brief", "2 Training data", "3 Test plan", "4 Results", "5 Decision". Each tab shows a small dot when it has something new.

Stage (all steps): the Riverton map on the left, drawn in code (it is a data map): a river curving through four districts (Hilltop north-west, Riverside along the river, Old Town center, Eastfield east), street lines, each district labeled and filled by the current step's number (see Look). Panel on the right holds the step's controls (`.sec` sections). On narrow screens the map sits above the panel at 40 percent height.

1. Brief. Focus: the vendor's sheet, under a painted banner of a city repair truck at a pothole (art `ae-brief`). The vendor's sheet: "Street Report pothole detector. Three model types, each trained on 240 photos from the Street Report app. Accuracy on our test set: Neighbors 98 percent, Tree 97 percent, Line 98 percent." The city's needs, as three cards: "Find potholes before they hurt someone (missed potholes are the worst error)." "Don't send crews to fake potholes (each wasted trip costs a crew an hour)." "Council members must be able to see why a photo was flagged." A "How each model decides" section with three tabs: Neighbors ("finds the 5 training photos most like this one; the score is how many of the 5 are potholes"), Tree (its trained rules as nested if-then lines with thresholds), Line (a weighted sum of the four clues through a 0 to 1 squash, shown as four weight bars and a bias). Map: grey, labels only. Tapping a district on any step opens its card with a painted street view (art `ae-district`) and its note.
2. Training data. Focus: the map's shading and the table beside it. The vendor's data sheet, built from the training set: a table of photos by district and weather (dry, wet), and a bar row by kind (pothole, plain road, shadow, puddle, patch). Map: each district shaded by its share of the training photos, with the count ("Hilltop 141"). A photo browser: filter by district, weather and kind; each photo is the painted road photo for its kind and weather (art `ae-road`) with its four clue bars under it and its label.
3. Test plan. Focus: the stepper grid, with the map beside it counting photos per district. A grid of steppers, one per slice (4 districts by dry and wet), 0 to 30 in steps of 5, reading from the city's own hand-labeled pool (30 per slice). Presets: "Like the app" (the app's mix, 50 photos: Hilltop 26 dry and 4 wet, Riverside 9 and 2, Old Town 6 and 1, Eastfield 2 and 0), "Every slice" (30 each, 240), "Clear". A total line and "Run the test" (`.big-btn`). Map: each district shows how many test photos it has; a district with none is hatched "not tested".
4. Results. Focus: the map filled by the chosen metric, beside the results table. For the three models side by side (`table.inst`): Accuracy, Recall ("potholes found"), Precision ("crew trips that found a pothole"), Missed, Wasted trips, on the current test plan. Model picker (Neighbors, Tree, Line) chooses which one the rest of the step shows: a 2 by 2 confusion matrix (engine `confusion`, Pothole and Not pothole), a slice table (each slice's n, accuracy, recall, precision; slices with fewer than 10 photos marked "thin"), and a Threshold slider 0.1 to 0.9 step 0.1 (default 0.5) with "Flag as pothole when the score is at least 0.5". Map: each district filled by the chosen metric (picker: Accuracy, Recall, Precision) for the chosen model, number printed in it. Tap a district or a matrix cell: its photos appear in a drawer with the model's score and, for Neighbors, the 5 matched training photos; for Tree, the rule path; for Line, the clue contributions.
5. Decision. Focus: the Evaluation report as it fills in. Pick a model (three cards), the threshold (the Results slider value is carried over and can be changed), and a verdict: "Ship it citywide", "Ship it only where it was tested well", "Not yet: ask for more data". "Ask the vendor for more data" lists four data requests as checkboxes (Eastfield dry, Eastfield wet, Riverside wet, Old Town wet) and a "Send request" button: the vendor retrains all three models on its 240 photos plus the requested city photos ("Round 2"), and a Round 1 / Round 2 switch appears on the Results step. The Evaluation report fills in live below: model, round, threshold, verdict, the test plan per slice, overall numbers, the worst tested slice, the gap between the vendor's claim and the measured accuracy, and automatic flags ("Eastfield wet was not tested", "Old Town wet has only 1 photo", "This threshold misses 8 potholes in this test"). "Copy report" puts the report text on the clipboard. No text box; nothing is saved.

## Content
Clues (0 to 1, from the photo): Dark (dark patch area), Rim (a sharp broken edge around it), Shine (wet glare), Seams (straight cut lines, as around a repair patch).
Ranges by kind and weather (dry / wet):
| Kind | Dark | Rim | Shine | Seams |
|---|---|---|---|---|
| Pothole dry | .50 to .90 | .50 to .90 | 0 to .30 | .10 to .50 |
| Pothole wet (water in it) | .45 to .80 | .20 to .55 | .55 to .90 | .10 to .50 |
| Patch dry | .45 to .80 | .45 to .75 | 0 to .25 | .40 to .80 |
| Patch wet | .45 to .80 | .40 to .70 | .45 to .80 | .40 to .80 |
| Puddle dry | .40 to .70 | 0 to .30 | .50 to .90 | 0 to .30 |
| Puddle wet | .40 to .75 | .05 to .40 | .60 to 1 | 0 to .30 |
| Shadow dry | .55 to .90 | 0 to .30 | 0 to .15 | 0 to .20 |
| Shadow wet | .50 to .80 | 0 to .30 | .30 to .60 | 0 to .20 |
| Plain road dry | 0 to .30 | 0 to .25 | 0 to .30 | 0 to .30 |
| Plain road wet | .10 to .40 | 0 to .25 | .50 to .90 | 0 to .30 |
Districts (pothole share; then the mix of other kinds: patch, puddle, shadow, plain): Hilltop .25; 0, .10, .30, .60. Riverside .30; .03, .30, .10, .57. Old Town .35; .05, .10, .40, .45. Eastfield .50; .55, .15, .05, .25. On-screen district notes: Hilltop "newer streets, many app users"; Riverside "low streets, puddles after rain"; Old Town "tall buildings, long shadows"; Eastfield "oldest streets, many repair patches, few app users".
Generation (engine `rng`): one photo = R() < pothole share gives a pothole, else a second R() picks the kind by the cumulative mix (patch, puddle, shadow, plain); then Dark, Rim, Shine, Seams in that order, each uni(R, range), rounded to 2 decimals.
- Vendor set: seed 701, 300 photos; per photo first R() picks the district by the app's mix (Hilltop .60, Riverside .20, Old Town .15, Eastfield .05, cumulative in that order), then R() < .15 makes it wet, then the photo. Photos 1 to 240 are the vendor's training set, 241 to 300 its test set.
- City pool: seed 702; districts in the order Hilltop, Riverside, Old Town, Eastfield; dry then wet; 30 photos each. A stepper value N uses the first N of that slice.
- Round 2 city photos: seed 703, generated always in this order and size: Eastfield dry 20, Eastfield wet 20, Riverside wet 10, Old Town wet 10; only the requested groups are added.
Resulting vendor training set: 240 photos; Hilltop 141 (120 dry, 21 wet), Riverside 52 (46, 6), Old Town 37 (29, 8), Eastfield 10 (10, 0); 69 potholes, 98 plain, 48 shadow, 21 puddle, 4 patch.
Models (binary, positive = pothole, features all four):
- Neighbors: engine `knn`, k = 5; score = potholes among the 5.
- Tree: greedy, depth 3, Gini impurity; candidate thresholds are midpoints between sorted distinct values of each clue, clues tried in the order Dark, Rim, Shine, Seams, first best kept on ties; a split needs at least 5 photos on each side and must lower impurity; score = pothole share in the leaf. Rule text: "If Rim is at most 0.31 ..." with thresholds to 2 decimals.
- Line: logistic regression; weights and bias start at 0; 2000 rounds of full-batch gradient descent, learning rate 1, gradients averaged over the training set; score = 1 / (1 + e^-(bias + sum of weight times clue)).
Checked results, threshold 0.5 (Accuracy percent; Recall and Precision percent for the whole set):
| Test | Neighbors | Tree | Line |
|---|---|---|---|
| Vendor test (60) | 98 | 97 | 98 |
| Like the app (50) | 98 | 96 | 96 |
| Every slice (240), round 1 | 89 (R 90, P 80) | 87 (R 92, P 74) | 86 (R 87, P 74) |
| Eastfield dry, round 1 | 77 (7 wasted trips) | 70 (9) | 70 (9) |
| Eastfield wet, round 1 | 57 (10 wasted, 3 missed) | 60 (10, 2) | 57 (10, 3) |
| Old Town wet, round 1 | 90 (3 missed) | 83 | 77 (4 missed) |
| Every slice, round 2 (all four requests) | 93 (R 91, P 88) | 93 (R 92, P 86) | 85 (R 77, P 76) |
| Eastfield dry, round 2 | 87 | 97 | 87 |
| Eastfield wet, round 2 | 77 | 77 | 43 |
Every slice, round 1 counts (TP, FP, FN, TN): Neighbors 71, 18, 8, 143; Tree 73, 25, 6, 136; Line 69, 24, 10, 137. Round 2: Neighbors 72, 10, 7, 151; Tree 73, 12, 6, 149; Line 61, 19, 18, 142.
Threshold on Every slice, round 1: Neighbors 0.2 gives R 99, P 68; 0.7 gives R 82, P 81. Tree 0.6 gives R 81, P 88. Line 0.2 gives R 100, P 72; 0.8 gives R 67, P 74.
Talk points the numbers support: the vendor's test came from the same skewed stream, so it could not see Eastfield or rain. Eastfield's repair patches look like potholes to models that saw 4 patches. More data fixes Neighbors and Tree but not Line: a single weighted sum can't separate "dark with sharp edges" from "dark with sharp edges and seams", so the model type matters.
On screen (Brief, small): "Based on a real problem: a city's pothole app found more potholes where more residents had smartphones."

## Interactions in detail
- Nothing plays on its own; the only wait is the 300 ms retrain bar, during which every control stays live (a tap on another step or model shows at once and the retrain still lands).
- Run the test is needed after a test plan change; Results grey out with "Plan changed: run the test". Model, threshold, round and metric changes update at once (no run needed).
- With 0 photos in the plan, Run is disabled. Metrics with a zero denominator show "-" with a tooltip ("no potholes in this slice").
- The threshold slider moves in 0.1 steps; Neighbors' scores are fifths, so 0.3 and 0.4 give the same result; a small note says so when that happens.
- Send request (Decision) retrains in under 300 ms with a short "Vendor retraining" bar; Round 2 is then the default on Results; Round 1 stays available. Changing the requests and sending again replaces Round 2.
- Report flags are computed from the current plan, model, round and threshold; the tool never says a verdict is right or wrong.
- Drawers list up to 30 photos with a "Show more" button. Each photo shows the painted road photo for its kind and weather (10 images, `ae-road`) with four labeled clue bars under it (Dark, Rim, Shine, Seams, each 0 to 1 with its value), so two photos of the same kind differ by their bars. The bars, not the painting, are what the models read; a small note in the Brief says so ("The models read four clue numbers from each photo").
- Keyboard: step tabs, then panel, then map districts (arrow keys between districts, Enter opens the drawer). Visible focus (theme ring).
- Sizes: the step bar, the current step's main button and the Results table visible without scrolling at 1280x720 and 1366x768; at 680x425 the map shrinks to a strip of four district chips with their numbers. Table numbers in the readout font, at least 12 px.

## Look
- Accent `--brand #f472b6` (signal pink) with `--brand-ink #2a0a1a`, on the 9-12 theme (`kit/theme-912.css`).
- Map: land #1b2430, river #1f4a6e, streets #2b3646; district fill on a sequential scale from #3a1f2e (low) to #f9a8d4 (high) with the value printed in each district (never color alone); not tested = diagonal hatch #62789a.
- Pothole and Not pothole in the matrix: P with a hole glyph, N with a road glyph, plus the theme's `--ok` and `--warn` only for right and wrong.
- Neighbors: 9-12 tools use the theme's amber by default; model-mechanic is lime, the other ml-lab tools are light themes. Pink keeps it apart.
- Contrast: brand on panel #141b25 6.54:1; brand on section #18202b 6.19:1; brand-ink on brand 6.85:1; theme ink on panel 14.7:1; printed district numbers use #0d1219 on fills lighter than #b0577f and #e8edf3 on darker ones (both at least 4.5:1; the build checks each fill).

## Art
Local FLUX (`scripts/localart.py`), no people. One style: plain documentary photo look, top-down for road photos, eye level for streets. The map, clue bars, matrix, tables and report stay code (data maps, charts and text).
- ae-brief: "A white city road repair truck with orange stripes parked beside a pothole on a quiet street, traffic cones, a puddle, morning light, realistic painted illustration"; 16:9; cutout no; people no; banner over the vendor's sheet on Brief, dimmed in the 680x425 preview.
- ae-road (kit of 10, one image each, one prompt line): "Top-down photo of a square patch of grey asphalt road showing {a deep jagged pothole with broken edges | a deep jagged pothole full of rainwater | a neat rectangular repair patch with straight cut seams | a neat repair patch with straight seams, wet and shiny | a shallow puddle on smooth dry asphalt with sky glare | a shallow puddle in rain with ripples and glare | the dark shadow of a lamppost across smooth asphalt | a dark shadow across wet shiny asphalt | plain smooth dry asphalt | plain smooth wet shiny asphalt}, even daylight, realistic"; 1:1; cutout no; people no; pothole, patch, puddle, shadow, plain road, each dry and wet, in that order; shown 72 px in the photo browser and drawers, 160 px in the Brief clue key.
- ae-district (kit of 4, one prompt line): "Eye-level street view in a small American city of {a newer neighborhood with smooth roads, young trees and tidy sidewalks | a low street along a river with wide puddles after rain and a levee | narrow old downtown streets between tall brick buildings casting long shadows | old cracked streets covered in many square repair patches beside small houses and a closed factory}, overcast light, realistic painted illustration"; 4:3; cutout no; people no; Hilltop, Riverside, Old Town, Eastfield; the district card opened by tapping a district.
The preview.svg is code (the Riverton map with Eastfield hatched pink-low and the other districts high).

## Voice
Bank voice `wise-mentor` (Gacrux), style "Say thoughtfully and warmly, like a wise high school mentor": a senior colleague coaching a new evaluator. Not used by a group sibling or a CS neighbor (network-architect uses calm-professor, model-mechanic science-narrator). Narration is light (students read). `Curio.voice`, `scope: () => state.step`. Read speaks the hint. Numbers are never spoken.
1. welcome (how; first page load on Brief; stale when any step tab is tapped): "You are the city's evaluator. The vendor says its model is 98 percent accurate. Read the sheet, then tap Test plan to find out where that's true."
2. plan (how; first visit to Test plan; stale when Run the test is pressed): "Set how many photos to test from each part of the city with the steppers, then press Run the test."
3. weakSlice (event; after a run where a slice with 10 or more photos is under 75 percent accuracy for the chosen model; stale when the plan changes or a district is tapped): "One part of the city does much worse than the rest. Tap it on the map."
4. oneDistrict (event; after a run where every tested slice is in one district; stale when the plan changes): "You only tested one district. The score can't tell you about the others. Add photos from another district and press Run the test."
5. decide (how; first visit to Decision; stale when a verdict is picked): "Tap a model card, set the threshold, then pick a verdict. The report lists what your test can and can't show."
6. retrained (event; after Send request; stale when Run the test is pressed or the step changes): "The vendor retrained all three models. Open Results and switch to round two."
Line 3 waits for 10 photos so a two-photo slice (Like the app gives Eastfield dry 2 photos, 1 right) never sends a student chasing noise.

## Family engine
ml-lab (`kit/ml-lab.js`, full description in tools/teach-the-robot/spec.md). This tool is the only user of `MLLab.train('tree', ...)` and `MLLab.train('linear', ...)`, which follow the Models rules above exactly, with `predict(item)` returning `{label, score, path}` (tree: the list of rules taken) or `{label, score, parts}` (line: weight times clue per clue). Also uses `rng` and `uni` for the vendor set, city pool and round 2 photos, `knn` (k = 5), `evaluate` with `positive: 'pothole'`, `threshold` and `groupBy` slice, and the `confusion` view. The map, road tiles and report stay in this tool.

## Sources
- Disaggregated evaluation and model reporting: Mitchell et al., "Model Cards for Model Reporting", FAT* 2019: https://arxiv.org/abs/1810.03993
- Precision, recall, thresholds: Google Machine Learning Crash Course, "Classification": https://developers.google.com/machine-learning/crash-course/classification
- Decision trees (Gini, depth) and logistic regression: scikit-learn user guide, "Decision Trees" https://scikit-learn.org/stable/modules/tree.html and "Logistic regression" https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
- The real pothole app: Kate Crawford, "The Hidden Biases in Big Data", Harvard Business Review, April 1, 2013 (Boston's Street Bump app): https://hbr.org/2013/04/the-hidden-biases-in-big-data
- Testing and managing AI risk: NIST AI Risk Management Framework 1.0 (2023): https://www.nist.gov/itl/ai-risk-management-framework
- CSTA K-12 Computer Science Standards (2017): https://csteachers.org/k12standards/
- Riverton, the vendor, the photos and every number are made up; the results table was computed with the rules above.
- Checks run (Python port of `kit/ml-lab.js`: mulberry32 `rng`, `knn`, the tree and the logistic line exactly as written, 2026-10-29): the training set is 240 photos, Hilltop 141 (120 dry, 21 wet), Riverside 52 (46, 6), Old Town 37 (29, 8), Eastfield 10 (10, 0); 69 potholes, 98 plain, 48 shadow, 21 puddle, 4 patch. The tree's first rule is Rim at most 0.305, shown "0.31". Every row of the results table reproduced, including the round 1 and round 2 counts and every threshold point. One rounding note: Tree, Every slice, round 2 is 222 of 240 = 92.5 percent and shows 93 only with half-up rounding (JavaScript `Math.round`); the build must round half up. Neighbors gives the same result at 0.1 and 0.2, at 0.3 and 0.4, at 0.5 and 0.6, at 0.7 and 0.8 (scores are fifths). Every wasted trip in Eastfield is a repair patch for all three models (Neighbors 7 dry and 10 wet). Like the app: every slice scores 96 to 100 except Eastfield dry, 1 of 2 right, so line 3 now needs 10 photos in a slice. Line 3 fires after Every slice for all three models (Eastfield wet 57, 60, 57).

## Done when
1. Brief shows vendor accuracies 98, 97, 98, and the Tree tab shows rules starting with Rim at most 0.31.
2. Training data shows 240 photos, Eastfield 10 (all dry), 4 patches; the map shading matches.
3. "Like the app" then Run gives 98, 96, 96, with Eastfield wet hatched "not tested", and the report flags it.
4. "Every slice" then Run gives 89, 87, 86; the map shows Eastfield lowest for every model; line 3 plays.
5. Neighbors, threshold 0.2: recall 99, precision 68; threshold 0.7: recall 82, precision 81.
6. Sending all four requests gives round 2 Every slice 93, 93, 85, and Eastfield wet 43 for Line.
7. Tapping Eastfield (Results, Neighbors) lists its photos with 5 matched training photos each; wasted trips there are mostly patches.
8. Every row of the Content results table matches; the report text copies to the clipboard and contains no text the student typed.
9. The step bar, Run the test and the Results table fit without scrolling at 1366x768; district values readable in grayscale.
10. Focus: on Results the map with its printed numbers is the largest thing on the stage at 1366x768 and stays beside the table, not under it.
11. Taps during the retrain bar (Send request) switch steps and models at once; round 2 still lands.
12. Art: the ten road photos match their kind and weather, each with its four clue bars; the four district cards and the Brief banner load; no people in any image.

## Open questions
- The concept says "AI-generated outputs". This spec reads that as a model's predictions (pothole flags). If Cory meant generative AI (chatbot answers or image captions to fact-check), that is a different tool built on canned outputs; say which.
