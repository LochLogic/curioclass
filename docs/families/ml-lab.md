# Family: ml-lab

Five tools, grade 2 to 12 (computer science, "how a computer learns from examples"), share one engine:
`kit/ml-lab.js`, inlined with `<script src="kit:ml-lab"></script>` after `kit:curio`. It exposes `MLLab` (and
`module.exports` under Node, so numbers can be checked without a browser). The full description lives in
`tools/teach-the-robot/spec.md`, "Family engine"; this file is the working reference. Built 2026-10-27 with
teach-the-robot, the first tool of the family.

Warning: the bundler inlines the file between script tags, so a literal closing script tag anywhere in
`kit/ml-lab.js` (even inside a comment) ends the script early and `MLLab` is undefined. Never write one.

## What the engine does (shared)

```js
// numbers: every generated dataset uses these, so spec tables rebuild exactly
MLLab.rng(seed)            // mulberry32, exactly as written in the spec; returns R() in [0, 1)
MLLab.uni(R, lo, hi)       // lo + (hi - lo) * R()
MLLab.r2(x)                // round to 2 decimals (half away from zero, guarded against 0.285 -> 0.28)
MLLab.item(id, label, v, tags)   // {id, label, v: {feature: 0..1}, tags: {room, time, district, ...}}
MLLab.dist(a, b, features) // Euclidean over the listed features (a missing value counts as 0)

// k nearest neighbors
MLLab.knn(train, item, {features, k})
  -> {label, votes, neighbors: [{item, d}], score(label)}
  // sorted by distance (closer than 1e-9 counts as equal), then by position in train.
  // Vote by count; a tie goes to the tied label whose nearest member comes first. score = share of the k.

// models: {type, predict(item)} plus what each type shows
MLLab.train('knn', items, {features, k, positive})
  // predict -> {label, score, scores, neighbors, votes}
MLLab.train('tree', items, {features, positive, negative, depth: 3, minLeaf: 5, names})
  // Gini, splits "at most" a midpoint between sorted distinct values, features tried in order, first best kept on
  // ties, a split must lower impurity. predict -> {label, score, scores, path: [{feature, threshold, le, text}], leaf}
  // model.rules() -> [{depth, text, leaf?, score?, n?}], text like "If Rim is at most 0.31"; model.root
MLLab.train('linear', items, {features, positive, negative, rounds: 2000, rate: 1})
  // logistic regression, weights and bias from 0, full-batch gradient descent, gradients averaged.
  // predict -> {label, score, scores, parts: [{feature, w, x, wx}], bias}; model.weights, model.bias
  // score: with positive set, the positive label's score; otherwise the predicted label's.
  // negative defaults to the first other label in the training set.

// evaluation
MLLab.evaluate(model, items, {classes, groupBy, positive, threshold})
  -> {n, ok, acc, cm, cells, classes, byGroup, results, mistakes, tp, fp, fn, tn, recall, precision}
  // cm[truth][predicted] counts, cells[truth][predicted] the items. results: [{item, pred, ok, out}].
  // With positive and threshold: predict positive when its score is at least the threshold.
  // byGroup[key] = {n, ok, acc, cm, cells (and tp..precision with positive)}. A zero denominator gives null.

// drawing
MLLab.glyph(shape, x, y, r, parent, style)   // circle, square, triangle, down, diamond, hex, star, plus, x
MLLab.view.confusion(el, ev, {classes, names, glyphs, onCell, rowTitle, colTitle})
  // rows "What it really was", columns "What the model said", counts in every cell, diagonal outlined,
  // off-diagonal shaded by count. Tap, Enter or Space on a cell: onCell({truth, pred, count, items}).
  // Arrow keys move between cells. Titles drop to two lines when the view is narrow. Without onCell the cells are
  // plain graphics (no role, no tabindex): the svg's aria-label lists every count.
MLLab.view.scatter(el, items, {fx, fy, glyphs, names, labels: {x, y}, query: {item, neighbors}, onPick, classes})
  // two features as axes 0 to 1 (fy null: a one-axis strip). The query item is a "?" ring with dashed lines to its
  // neighbors, which get a ring. Pass the same item objects as the knn neighbors (matched by reference).
  // With onPick, points are focusable buttons.
MLLab.view.groupBars(el, byGroup, {names, glyphs, order, unit: 'right'})
  // one bar per group, length = share right, "n of m right" under it
// every view: {svg, update(data, opts), redraw(), destroy()}, re-laid out by a ResizeObserver on el (give el a
// size), and an aria-label on the svg listing its numbers.

MLLab.version   // 1. Raise it when a change could alter a sibling's numbers or views; note the change here.
```

`glyphs[label]` is `{shape, color, letter}` or just a shape name. Defaults go circle, square, triangle, diamond,
star, hex by class order. Every class shows a shape (and a letter if given) as well as a color, never color alone.

## Colors (CSS variables the tool sets on :root)

| Variable | Used for | Fallback |
|---|---|---|
| `--ml-ink` | text, outlines | `--ink`, #222 |
| `--ml-muted` | titles, axis numbers | `--muted`, #555 |
| `--ml-line` | grid lines, empty cell borders | `--line`, #ccc |
| `--ml-bg` | the "?" query ring fill | `--panel`, #fff |
| `--ml-cell` | empty cells, plot background | #fff |
| `--ml-ok` | diagonal outline (right) | #1f7a3f |
| `--ml-bad` | off-diagonal shading (wrong) | #b42318 |
| `--ml-focus` | focus ring | `--focus`, #c2410c |
| `--ml-1` to `--ml-6` | class colors when glyphs give none | colorblind-safe set (#1f77b4, #d95f02, #1b9e77, #7570b3, #e7298a, #66a61e) |
| `--readout-font` | counts in the confusion matrix | ui-monospace, Consolas |

The engine has no stylesheet of its own; the views draw on the tool's panel.

## What each tool brings (its own)

| Tool | Grade | Engine parts | Its one idea (not shared) |
|---|---|---|---|
| teach-the-robot | 2 | `knn` (k = 1, six features) | the class labels examples; more and different examples make better guesses. Draws its own wall and chart, no views |
| biased-bot | 4 | `rng`, `uni`, `knn` (k = 3, 64 grid cells), `evaluate` with `groupBy` room, `groupBars` | training data from one room fails other rooms' handwriting |
| leaf-sorter-ai | 5 | `rng`, `uni`, `knn` (k = 3, switched-on clues), `evaluate`, `scatter` (strip with one clue) | which clues count |
| model-mechanic | 6-8 | `rng`, `uni`, `knn` (k from the panel), `evaluate` with classes and `groupBy` time, `confusion` with `onCell` | reading a confusion matrix, day vs night |
| ai-evaluator | 9-12 | `rng`, `uni`, `knn` (k = 5), `train('tree')`, `train('linear')`, `evaluate` with `positive`, `threshold`, `groupBy`, `confusion` | disaggregated evaluation, recall vs precision, thresholds |

## Rules for siblings

- Models, scores and the three views come from the engine. A sibling adds its own scene (a lunchroom, leaves, a
  camera trap, a city map) and its own questions.
- Every number in a spec table is computed with the engine and its seed. Check yours in Node before building the
  page: `const MLLab = require('../../kit/ml-lab.js')` works without a browser.
- New engine features go into the engine and this file in the same change, keeping existing calls working. Re-run
  the checks below after any engine change.
- The views need a sized element (they read its box). Put them in a panel or stage cell with a set height.

## Verification (2026-10-27, Node, against the specs)

- teach-the-robot (refine round 1, 2026-10-28, parade rebalanced to 5 cats and 5 dogs): parade scores after N
  correct cards, N = 1 to 16: 5, 6, 7, 7, 8, 8, 8, 8, 8, 9, 9, 10, 10, 10, 10, 10, with the spec's misses.
  Marmalade labeled dog gives 5 with 2 cards and 8 with 12 or more; no single wrong label of any taught card raises
  the score at any N. In the page, 50 Mystery pets across wall sizes 1, 2, 5, 11 and 16 matched an independent
  `knn` call and the table.
- ai-evaluator: the whole results table reproduced exactly. Vendor test 98, 97 and 98. Every slice: knn 89 (R 90,
  P 80, 71/18/8/143), tree 87 (R 92, P 74), linear 86 (R 87, P 74). Eastfield dry 77/70/70, Eastfield wet 57/60/57,
  Old Town wet 90/83/77. knn at threshold 0.2: R 99, P 68. The tree's first rule is "If Rim is at most 0.31". The
  training counts match.
- The three views were rendered in Chrome with made-up data (3 classes and a 2-class tree evaluation, a scatter with
  a query, a strip, group bars): no errors, cells focusable, onCell fires.
- 2026-10-28: confusion cells without `onCell` lost their tabindex (they were focus stops that did nothing). View
  code only; the teach-the-robot and ai-evaluator tables above were re-run in Node and are unchanged.
- biased-bot, leaf-sorter-ai and model-mechanic tables were not checked here; each builder checks its own.
