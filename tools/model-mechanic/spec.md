# Model Mechanic

## One idea
A nature preserve's trail-camera AI is misnaming animals, and every mistake lands in one square of a confusion matrix: tap the square to see the actual photos and the training photos they were matched to, work out which part is broken (too few foxes, no night photos, mislabeled examples), fix that part, and watch the mistakes leave the square.

## Not like
- leaf-sorter-ai (same family, grade 5): the main view there is the clue map and the only lever is which clues count. Here the main view is the confusion matrix, and the levers are the training mix, the number of neighbors k, the labels and the clues, found by diagnosis.
- biased-bot (same family, grade 4): one cause (whose examples) and a per-room bar chart. Here three different faults each leave a different pattern in the matrix, and finding which one is the job.
- ai-evaluator (same family, 9-12): the evaluator can't touch the model and decides whether to ship it. Here you are inside the model with tools in hand.
- algorithm-audit (6-8 roleplay): audits a school's rule-based decision and debates tradeoffs. Here the model learns from photos, and the work is measuring and repairing it, not debating.
- misleading-charts (6-8 mystery): charts that lie by design. The matrix here is honest; the model is what is wrong.

## Who and how
- Grades 6 to 8, computer science. Module: Machine Learning Models (Algorithms and Programming). Topic line: "confusion matrices and fixing a model".
- Driver: students, alone or in pairs on laptops. 20 to 35 minutes; each work order takes about 5 to 10.
- Standards: MS-ALG-ML-06, MS-ALG-ML-07, MS-ALG-ML-08, MS-DAT-IM-29 (module codes). CSTA 2017 crosswalk: 2-DA-08 (collect data and transform it to make it more useful and reliable), 2-DA-09 (refine computational models based on the data they generate), 2-IC-21 (discuss issues of bias in the design of existing technologies). Reference: Google Machine Learning Crash Course, "Classification" (confusion matrix, class imbalance).
- tool.json: driver "students", minutes "20-35", modes ["Garage", "Work Orders"], grades_label "Grades 6-8".

## Screens and modes
Kit frame. Header: title "Model Mechanic" with small line "Cedar Hollow trail camera", mode buttons "Garage" (wrench icon) and "Work Orders" (clipboard icon), Motion, Sound, Read.

Shared layout (both modes): stage on the left with two parts, panel on the right.
- Test photos strip (top of stage): the 40 test photos as small camera frames (day frames in color, night frames in green-gray infrared), each with the model's answer tag (letter plus color: D Deer, F Fox, R Raccoon, E Empty) and a red corner notch when wrong. Above it: "Right: 39 of 40", "Day 15 of 15", "Night 24 of 25".
- Confusion matrix (engine `confusion`, big, center of the stage): rows "What it really was", columns "What the model said", 4 by 4, counts in every cell, diagonal cells outlined in lime, off-diagonal cells shaded by count. Tabs above it: "All", "Day", "Night".
- Cell drawer (opens under the matrix when a cell is tapped): every test photo in that cell, each with "Matched to:" its k nearest training photos (thumbnails with their labels). Tapping a training photo opens it large with its label and two buttons: "Relabel as..." (Deer, Fox, Raccoon, Empty) and "Close".
Panel (the toolbox), in sections (`.sec` style):
- `#hint`.
- Training photos: a 4 by 2 grid of steppers, rows Deer, Fox, Raccoon, Empty, columns Day and Night, each "N" with "Fewer" and "More" in steps of 5 (0 to 40). A total line "Training photos: 160".
- Neighbors: "k = 5" with buttons 1, 3, 5, 7, 9 (pressed state shows the value).
- Clues: switches Size, Legs, Tail, Mask (all on at start).
- "Run the test" (play icon, `.big-btn`): retrains and re-scores. Any change above greys the results with "Changed: run the test" until pressed.
- "Reset" (circular arrow): back to this mode's starting setup.

### Mode 1: Garage (opens first)
Free play with a working model: Deer, Fox, Raccoon and Empty each 20 day and 20 night, k = 5, all clues on. Right: 39 of 40. Nothing to win; students try breaking it and fixing it.

### Mode 2: Work Orders
A work order card at the top of the panel: number, title, the ranger's complaint, the goal as checkboxes that tick live after each run, and "Next work order" (enabled when every goal box is ticked). Three orders:
1. "Where are the foxes?" Complaint: "The camera keeps calling our foxes raccoons." Setup: Deer 20/20, Fox 2/1, Raccoon 25/25, Empty 20/20 (day/night), k = 5, all clues. Start: 32 of 40; the Fox row shows 2 right and 8 in the Raccoon column. Goal: Fox at least 9 of 10; every other animal at least 9 of 10.
2. "Night shift" Complaint: "It works all day and gets confused at night." Setup: every animal 30 day, 0 night, k = 5, all clues. Start: 32 of 40; Day 15 of 15, Night 17 of 25; the Raccoon row shows 8 in the Fox column, all at night. Goal: Night at least 22 of 25; Right at least 36 of 40.
3. "Ghost deer" Complaint: "Deer keep coming up as empty frames." Setup: every animal 15 day and 15 night, k = 1, all clues; 8 of the 30 deer training photos are labeled Empty (a volunteer's slip). Start: 33 of 40; the Deer row shows 4 in the Empty column. Goal: Deer 10 of 10; Right at least 37 of 40.
After each order is met, a debrief card names the fault and the fixes that work (below), then the next order.

## Content
Features measured by the camera's detector, 0 to 1: Size (how much of the frame the animal fills), Legs (leg length for its body), Tail (tail length and bushiness), Mask (dark face mask and ringed-tail contrast).
| Animal | Size | Legs | Tail | Mask |
|---|---|---|---|---|
| Deer | 0.65 to 0.95 | 0.65 to 0.90 | 0.05 to 0.25 | 0.05 to 0.25 |
| Fox | 0.30 to 0.55 | 0.35 to 0.60 | 0.55 to 0.85 | 0.15 to 0.40 |
| Raccoon | 0.30 to 0.50 | 0.20 to 0.45 | 0.40 to 0.65 | 0.65 to 0.90 |
| Empty (wind, grass) | 0 to 0.15 | 0 to 0.20 | 0 to 0.20 | 0 to 0.20 |
Night (infrared) photos: the mask is washed out (Mask times 0.35) and every feature gets a little noise. Generation per photo, for each feature in the order Size, Legs, Tail, Mask: x = uni(R, range); at night, if Mask then x = x * 0.35, then x = x + (2R() - 1) * 0.05; clamp to 0 to 1; round to 2 decimals.
Photo library (training pool): seed 601; for each animal in the order Deer, Fox, Raccoon, Empty, 40 times: one day photo, then one night photo. A stepper value N uses the first N of that animal and time.
Test set (40, fixed): seed 602; per animal, day photos then night photos: Deer 5 + 5, Fox 3 + 7, Raccoon 2 + 8, Empty 5 + 5 (foxes and raccoons are mostly out at night).
Work order 3 labels: counting the 30 deer training photos in order (15 day, then 15 night), photos 2, 6, 10, 14, 18, 22, 26, 30 are labeled Empty (4 day, 4 night).
Checked results (Right of 40; Day of 15; Night of 25), engine `knn`:
| Setup | Right | Day | Night | Where the mistakes are |
|---|---|---|---|---|
| Garage, k = 5 | 39 | 15 | 24 | 1 raccoon called fox |
| Garage, k = 1 or 3 or 7 | 37 | 15 | 22 | 3 raccoons called fox |
| Garage, Mask only | 11 | 7 | 4 | everywhere |
| Garage, no Legs (Size, Tail, Mask) | 40 | 15 | 25 | none |
| WO1 start | 32 | 13 | 19 | 8 foxes called raccoon |
| WO1, Fox to 7/6 | 40 | 15 | 25 | none |
| WO1, k = 1 | 39 | 14 | 25 | 1 fox called raccoon |
| WO1, Raccoon to 5/5 | 39 | 14 | 25 | 1 fox called raccoon |
| WO2 start | 32 | 15 | 17 | 8 raccoons called fox |
| WO2, night 10 each | 37 | 15 | 22 | 3 raccoons called fox |
| WO2, Mask off | 36 | 14 | 22 | 4 raccoons called fox |
| WO3 start | 33 | 13 | 20 | 4 deer called empty, 3 raccoons called fox |
| WO3, k = 5 | 39 | 15 | 24 | 1 raccoon called fox |
| WO3, all 8 relabeled Deer | 37 | 15 | 22 | 3 raccoons called fox |
Debriefs (shown after each order):
1. "Class imbalance: with 50 raccoon photos and 3 fox photos, a fox's 5 nearest neighbors are mostly raccoons. Fixes: add fox photos, use fewer raccoons, or a smaller k."
2. "Missing data: the model never saw a night photo, and at night a raccoon's mask disappears. Fixes: add night photos, or stop trusting the Mask clue. The animals hurt most were the ones that live at night, which is how biased data works."
3. "Label noise: 8 deer were labeled Empty, and with k = 1 one wrong neighbor decides. Fixes: find and relabel them, or raise k so one wrong photo gets outvoted."
On-screen fact line (Garage, small): "Motion cameras take many photos with no animal at all: wind, moving grass, rain."

## Interactions in detail
- Run the test recomputes in under 100 ms; the matrix counts tween over 400 ms (instant with Motion off); the test strip tags flip.
- Matrix tabs filter the same results (no retraining). The goal boxes always use All, Day or Night as written.
- Cell drawer: lists up to 10 photos; matched training photos shown for the current k. In WO3, the mislabeled training photos show a deer with the tag "Empty"; relabeling one marks the results changed. Relabels persist until Reset or mode change; Garage labels can be changed too.
- Steppers clamp at 0 and 40; a class with 0 training photos in both columns shows a warning "The model has never seen a fox" and the run still works (that class is never predicted).
- Fewer than k training photos total disables that k.
- Work Orders keep the current order and its edits when switching to Garage and back; Reset restores the order's setup. Completing all three shows "All work orders done" with a "Start again" button.
- Keyboard: panel before stage; matrix cells are a grid of buttons (arrow keys move, Enter opens the drawer). Visible focus.
- Sizes: Run the test, the matrix and the training steppers visible without scrolling at 1280x720 and 1366x768 (steppers compact: 36 px rows, 44 px buttons); at 680x425 and narrower the test strip collapses to the three scores and a "Photos" button. Matrix numbers at least 12 px at every size.
- Nothing is saved.

## Look
- Accent `--brand #a3e635` (lime). Band 6-8, own dark workshop `:root`: `--paper #121612`, `--panel #1a201a`, `--ink #e9efe6`, `--muted #a9b5a4`, `--line #2e382d`, `--brand #a3e635` (lime; header rule, pressed buttons, diagonal outlines) with `--brand-ink #142000`, `--focus #ffd166`.
- Class tags (letter plus color): Deer D #f2b866, Fox F #ff8a5b, Raccoon R #9ec5ff, Empty E #c9c9c9. Wrong notch #ff6b6b with an X.
- Night frames: tinted #0d140d to #cfe8c8; day frames use the day art.
- Neighbors: the 6-8 CS concepts have no built tools yet; game-remix teal, score-keeper raspberry, code-tracer rust are light themes. Lime on a dark bench is unlike them and unlike ai-evaluator's pink.
- Contrast: brand-ink on lime 11.26:1; ink on paper 15.62:1; ink on panel 14.19:1; muted on panel 7.77:1; lime on panel 11.01:1; focus on panel 11.51:1; tag colors on panel 9.34, 7.14, 9.39, 10.02:1. All pass AA.

## Art
- `clearing-day`: "a forest clearing with ferns, a fallen mossy log and a dirt path, seen from a trail camera strapped to a tree at knee height, daylight, photo style, wide angle"; 16:10; cutout no; people no; Cloudflare FLUX.2. Background of day frames.
- `clearing-night`: "the same forest clearing with ferns, a fallen log and a dirt path at night, black and white infrared trail camera photo, soft glow in the center"; 16:10; cutout no; people no; Cloudflare FLUX.2. Background of night frames (tinted green-gray in CSS).
- Ask both for a clean frame with plain edges, so no fake timestamp lettering appears.
Animals are drawn in code as silhouettes built from their four values (body size, leg length, tail, mask and ringed tail), with eye shine at night, so the picture matches the numbers. preview.svg: the matrix with one bright off-diagonal cell and two frames above it.

## Voice
Bank voice `science-narrator`, style "Say in a clear, informative way, like a nature documentary narrator". Fits a wildlife camera; not used by any group sibling or the CS neighbors here.
1. how, welcome Garage: "This camera AI names every animal it sees. Each square shows what an animal really was and what the model said."
2. how, first tap of the matrix: "Tap a square off the diagonal to see the photos the model got wrong."
3. how, first time the drawer opens: "Each wrong photo shows the training photos it was matched to. Look for the reason."
4. how, first panel change: "You changed the model. Press Run the test."
5. event, after a run: "The model got N of 40 right." (forty-one fixed lines, zero to forty)
6. how, welcome Work Orders: "The rangers sent work orders. Read the complaint, find the broken part, and fix it."
7. event, each order opens: "Work order one. Where are the foxes?" "Work order two. Night shift." "Work order three. Ghost deer."
8. event: "Goal met. Read what was wrong, then go to the next work order." (stale on any change)
9. event: "That fixed one thing and broke another. Check the other rows." (when a run meets one goal box and unticks another)
10. event, after a relabel: "Label changed. Run the test to see what it does."
Debriefs are read on screen, not spoken. Read speaks the hint.

## Family engine
ml-lab (`kit/ml-lab.js`, full description in tools/teach-the-robot/spec.md). Uses `rng` and `uni` for the photo library and test set, `knn` (k from the panel, features = switched-on clues, neighbors for the cell drawer), `evaluate` with `classes` Deer, Fox, Raccoon, Empty and `groupBy: p => p.tags.time` for the Day and Night tabs, and the `confusion` view with `onCell` for the drawer. The silhouettes, steppers and work orders stay in this tool.

## Sources
- Confusion matrix, accuracy, class imbalance: Google Machine Learning Crash Course, "Classification": https://developers.google.com/machine-learning/crash-course/classification
- Nearest neighbors and the effect of k: scikit-learn "Nearest Neighbors": https://scikit-learn.org/stable/modules/neighbors.html
- Camera traps produce many empty frames and are classified with machine learning: Norouzzadeh et al., "Automatically identifying, counting, and describing wild animals in camera-trap images with deep learning", PNAS 115(25), 2018: https://www.pnas.org/doi/10.1073/pnas.1719367115
- Night photos are black-and-white infrared: Rovero et al., "Which camera trap type and how many do I need?", Hystrix 24(2), 2013.
- When the animals are active (raccoons mostly at night; red foxes at dusk, night and dawn; deer at dawn and dusk): National Wildlife Federation wildlife guide pages for Raccoon, Red Fox and White-tailed Deer: https://www.nwf.org/Educational-Resources/Wildlife-Guide/Mammals
- CSTA K-12 Computer Science Standards (2017): https://csteachers.org/k12standards/
- Cedar Hollow, its photos and all feature values are made up; the results table was computed with the engine.

## Done when
1. Garage opens at 39 of 40, Day 15, Night 24; k = 1 gives 37; Mask only gives 11.
2. Work order 1 starts at 32 with 8 in the Fox row, Raccoon column; Fox day and night each +5 meets the goal at 40 of 40.
3. Work order 2 starts at Night 17 of 25; adding 10 night photos per animal meets it at Night 22; switching Mask off instead also meets it.
4. Work order 3 starts at 33 with 4 in the Deer row, Empty column; the drawer for that cell shows mislabeled deer photos; k = 5 meets it at 39; relabeling all 8 instead meets it at 37.
5. Every row of the results table matches when set up as described.
6. Goal boxes tick and untick live after each run; Next is enabled only when all are ticked.
7. Line 4 is spoken once in a session of five changes; line 5 after every run.
8. Run the test, the matrix and the steppers are visible without scrolling at 1366x768; matrix numbers are at least 12 px at 375 wide; tags readable in grayscale by letter.
