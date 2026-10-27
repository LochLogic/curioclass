# Teach the Robot

## One idea
The class shows Kip the robot one pet at a time and says out loud "cat" or "dog"; Kip keeps every example on its memory wall, and when a new pet walks in Kip draws a line to the remembered pet that looks most like it and guesses from that one, so the class watches its guesses get better as they teach it more, and different, examples.

## Not like
- spot-the-ai (grade 1, showdown): the class decides which everyday scenes use AI. Here nobody judges scenes; the class is the teacher and builds the robot's memory card by card.
- robot-dance (K, sequence cards): Bolt does exactly what the cards say and never guesses. Kip is never told the rule; it only has examples and guesses from them.
- computer-builder (grade 1): parts give a computer powers. Nothing is assembled here; the only thing that grows is the memory wall.
- loop-garden (grade 2): repeat blocks and fewest-blocks stars. No program, no stars here; the measure is how many pets of ten Kip gets right.
- input-or-output (grade 2): sorting gadget parts into in and out. Here the class sorts pets to teach a learner, and the learner then sorts on its own.
- biased-bot, leaf-sorter-ai (same family, 4 and 5): those choose where the data comes from and which clues count. Here the only lever is how many examples Kip has seen, which is the first idea of the family.

## Who and how
- Grade 2, computer science. Module: Teach the Machine (Algorithms and Programming). Topic line: "how a computer learns from examples".
- Driver: teacher, on a projector or smartboard. The class names each pet out loud, predicts Kip's guesses, and counts the parade score together. 15 to 25 minutes.
- Standards: E2-ALG-ML-02 (module code). CSTA 2017 crosswalk: 1A-DA-07 (identify and describe patterns in data to make predictions). Reference: AI4K12 Big Idea 3, "Computers can learn from data".
- tool.json: driver "teacher", minutes "15-25", modes ["Teach", "Pet Parade"], grades_label "Grade 2".
- No reading needed: every control has an icon, every fixed line is spoken.

## Screens and modes
Kit frame: header, stage (left), panel (right). Header: title "Teach the Robot" with small line "Show Kip examples", mode buttons (`.seg`) "Teach" (open book icon) and "Pet Parade" (flag icon), then Motion, Sound, Read (`motion`, `sound`, `read`).

Stage, drawn in code and laid out per size: the lobby of a pet hotel. Cream wall, wood floor, a door on the left where pets walk in. Kip stands center-right: a round-cornered box robot with a face screen (its screen shows a thinking swirl, then a cat or dog icon as its guess). Behind Kip is the memory wall: two shelves with headers, Cat shelf (cat face icon) on top, Dog shelf (dog face icon) below, each holding up to 16 small portrait cards in rows.

### Mode 1: Teach (opens first)
- Panel: `#hint`; big buttons "Next pet" (paw icon), "Cat" (cat face, teal) and "Dog" (dog face, orange), "Mystery pet" (question mark), "Forget" (trash can, shown only while a wall card is selected), "Start over" (circular arrow); a counter "Kip remembers: N" with N small paw icons.
- Next pet: the next example card in the deck walks in from the door and sits in the spotlight. Cat and Dog light up. The teacher taps what the class says; the pet shrinks into a portrait card and flies onto that shelf.
- Mystery pet: the next pet of the parade list walks in. Kip thinks (1.2 s), a dotted look-alike line draws from the pet to the one remembered card that is most alike (that card glows), and Kip's screen shows its guess. Then the pet turns to the class and the truth shows: a big cat or dog icon over it, plus a check (right) or an X (wrong) on Kip's screen.
- Tapping a wall card selects it (thick outline); Forget removes it. The teacher can fix a mislabel this way.

### Mode 2: Pet Parade (the measurement)
- Panel: `#hint`; "Start parade" (play icon); "Stop" (square, in its place while running); a scoreboard of 10 round slots; Kip's Chart: a bar chart, one bar per parade run, bar height = pets right (0 to 10), under each bar a paw icon and the number of pets Kip remembered at that run.
- Start parade: the 10 parade pets walk past one by one; Kip guesses each (look-alike line as in Teach); each slot fills with a check (green, check glyph) or an X (red, X glyph). At the end the tally shows large ("7 of 10") and a new bar grows on the chart.
- Chart keeps the last 8 runs for the page load. Runs with the same memory size stack side by side, never replace.

## Content
Features (0 to 1), used by the engine and by the drawing, so what Kip compares is what the class sees:
ears (0 floppy, 1 pointy), snout (0 short, 1 long), whiskers (0 small, 1 long), size (0 small, 1 big), dark (0 white coat, 1 black coat), fluffy (0 smooth, 1 very fluffy).

Example deck, in this fixed order (name is for the teacher, shown small under the card):
| # | Name | Is a | Coat | ears | snout | whiskers | size | dark | fluffy |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Marmalade | cat | orange tabby #e8913a | .75 | .30 | .70 | .20 | .30 | .20 |
| 2 | Bear | dog | dark brown, shaggy #4a2f1f | .50 | .55 | .50 | .90 | .85 | .85 |
| 3 | Inky | cat | black #1f1f24 | .85 | .25 | .75 | .30 | .95 | .20 |
| 4 | Pebble | dog | white #f4f1ea | .30 | .50 | .40 | .20 | .05 | .90 |
| 5 | Snowball | cat | white #f7f5f0 | .80 | .20 | .85 | .35 | .05 | .85 |
| 6 | Rocket | dog | gray and white #8c8f96 | .85 | .65 | .45 | .70 | .50 | .70 |
| 7 | Tiger | cat | gray stripes #7d7f86 | .90 | .30 | .80 | .60 | .60 | .30 |
| 8 | Biscuit | dog | golden #d9a441 | .20 | .65 | .35 | .60 | .30 | .40 |
| 9 | Coco | cat | brown #6e4a2e | .80 | .25 | .70 | .30 | .70 | .20 |
| 10 | Pudding | dog | tan #c49a6c | .35 | .15 | .50 | .30 | .45 | .10 |
| 11 | Smoky | cat | gray #8a8d94 | .85 | .20 | .80 | .50 | .55 | .95 |
| 12 | Ziggy | dog | red and white #c8642c | .85 | .55 | .40 | .35 | .35 | .30 |
| 13 | Duchess | cat | cream #efe1c2 | .75 | .30 | .85 | .65 | .15 | .70 |
| 14 | Moose | dog | black #222226 | .25 | .75 | .35 | .95 | .90 | .30 |
| 15 | Pepper | cat | black and white #26262b | .90 | .20 | .75 | .20 | .75 | .15 |
| 16 | Scout | dog | white with dark spots #3a3a3a | .55 | .60 | .40 | .45 | .60 | .20 |

Parade (and Mystery pet, cycling in this order):
| # | Name | Is a | Coat | ears | snout | whiskers | size | dark | fluffy |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Maple | cat | orange #e39a4c | .85 | .25 | .80 | .30 | .35 | .35 |
| 2 | Rusty | dog | golden #c98a3a | .20 | .70 | .40 | .55 | .35 | .30 |
| 3 | Luna | cat | black #232327 | .85 | .20 | .80 | .40 | .90 | .80 |
| 4 | Noodle | dog | white #f2efe8 | .25 | .55 | .40 | .25 | .10 | .30 |
| 5 | Ghost | cat | white #f5f3ee | .80 | .25 | .85 | .30 | .10 | .50 |
| 6 | Shadow | dog | black #1e1e22 | .20 | .75 | .35 | .85 | .90 | .30 |
| 7 | Pippin | dog | red #c0612e | .85 | .55 | .45 | .30 | .40 | .30 |
| 8 | Waffles | dog | tan #b8905f | .30 | .20 | .50 | .25 | .50 | .15 |
| 9 | Bramble | cat | gray #85888f | .85 | .25 | .90 | .60 | .55 | .75 |
| 10 | Juniper | dog | gray #7a7d84 | .80 | .65 | .40 | .60 | .60 | .60 |

Parade score after teaching the first N deck cards with the right labels (checked with the engine, k = 1):
N = 1: 4, 2: 4, 3: 5, 4: 7, 5 to 9: 8, 10 and 11: 9, 12 to 16: 10. With 2 cards Kip misses Rusty, Noodle, Pippin and Waffles (all look most like Marmalade) and Luna and Bramble (most like Bear). Pippin, a pointy-eared dog, is fixed only by Ziggy (card 12); Waffles, a short-nosed dog, only by Pudding (card 10). That is the talk point: Kip needed an example like the new pet.

Drawing: one parametric pet, side view facing the class. Body ellipse width 140 to 260 px by size; head circle; ears drawn from floppy (rounded drooping flap) to pointy (upright triangle) by ears; muzzle length by snout; whisker strokes length by whiskers; fill = coat color; fluffy adds a scalloped fur outline; tabby, stripes and spots are simple overlay strokes. Cats and dogs share the drawing, so the class sees the same clues Kip uses.

## Interactions in detail
- Next pet with the deck used up: nothing walks in; "every card" line. Start over restores the deck, empties the wall, clears the chart.
- Labels are never checked. A wrong label teaches Kip wrong, and its later guesses show it. The wall card keeps the label the teacher chose.
- Mystery pet or Start parade with an empty wall: nothing walks; the "doesn't remember" line plays and Next pet pulses once.
- Guessing: engine `knn` with k = 1 over all six features. Distance ties go to the card taught first. The look-alike line always ends on the card that decided.
- While a pet is walking or Kip is thinking, every button but Stop and the header is disabled (dimmed, not hidden). A tap on a disabled button does nothing.
- Parade timing: 2.6 s per pet (walk in 0.8 s, think 1.0 s, truth 0.8 s). Motion off: pets appear in place and the line draws at once; timing stays the same.
- Stop ends the parade; a part run adds no bar. Mode switch stops and hushes. Each mode keeps its state for the page load. Nothing is saved.
- Keyboard: Tab order is mode buttons, header buttons, panel buttons, then wall cards. Enter or Space activates; on a selected wall card, Delete forgets it. Visible focus.
- Sizes: Next pet, Cat, Dog, Mystery pet and Start parade are visible without scrolling at every size in STANDARDS.md. Targets 60 px. At 680x425 the wall shrinks to 8 cards per row (cards at least 40 px) and the chart to its last 4 bars. Stage text at least 10 px in the preview.

## Look
- Accent `--brand #16679a` (cerulean, like a hotel awning; header). Band K-2, own `:root`: `--paper #fbf7ef`, `--ink #2b2238`, `--muted #66597a`, `--line #e6dccb`, `--brand #16679a`, `--focus #c2410c` with a 3 px white inner ring.
- Stage: wall #f6e3c8, floor #c98f5a with darker plank lines, door #8a5a3c. Kip: silver-blue #8fb3d9 body, #2b2238 outline, face screen #1f2a3a with a cerulean #16679a antenna light.
- Buttons: Cat #0f7c7a (teal) and Dog #b5531a (burnt orange), white text and icon; check #1f7a3f, X #b42318, each with its glyph.
- Neighbors: robot-dance magenta night stage, computer-builder blue #2049b8, loop-garden lawn green, score-keeper raspberry; internet-journey (grade 3, specced in this wave) is purple #6a3d9a. Cerulean on a warm lobby sits between computer-builder's royal blue and game-remix's teal and is unlike the rest.
- Contrast: white on #16679a 6.10:1; ink on paper 14.15:1; muted on paper 6.00:1; brand on paper 5.71:1; brand on wall 4.87:1; ink on wall 12.06:1; white on Cat teal 5.02:1; white on Dog orange 4.98:1; focus on paper 4.85:1. All pass AA.

## Art
none: drawn in code. Kip, the 26 pets (one parametric drawing), the lobby, shelves, chart and preview.svg (Kip with a look-alike line from Maple to Marmalade on the wall) are SVG in the tool.

## Voice
Bank voice `playful-friend`, style "Say playfully and cheerfully, like a fun music teacher". Not used by any neighbor (robot-dance lively-host, computer-builder bright-teacher, loop-garden hero-coach, score-keeper friendly-dad). Every fixed line below is recorded; `Curio.voice` with `scope: () => state.mode`. Kind: how = once, then hint only; event = every time, dropped when stale.

Teach:
1. how, welcome: "This is Kip. Kip is a robot that learns from examples. Tap Next pet to show Kip a pet."
2. how: "Is it a cat or a dog? Say it out loud. Then tap Cat or Dog."
3. event: "Kip remembers: that one is a cat!" (stale once another pet is in the spotlight)
4. event: "Kip remembers: that one is a dog!" (same)
5. how (after 2 cards on the wall): "Now tap Mystery pet. Kip will guess!"
6. event: "Kip looks for the pet it remembers that looks the most alike." (stale when the guess shows)
7. event: "Kip thinks it's a cat!" 8. event: "Kip thinks it's a dog!" (stale when the truth shows)
9. event: "Yes! Kip got it right!"
10. event: "Oops! Kip guessed wrong. Kip needs more examples."
11. event: "Kip doesn't remember any pets yet. Tap Next pet first!"
12. event: "That's every example card! Tap Pet Parade to see how Kip does."
13. how: "Tap a card on the wall, then the trash can, to make Kip forget it."
14. event: "Kip forgot that one."
15. event: "Starting over! Kip's memory is empty."

Pet Parade:
16. how, welcome: "Welcome to the Pet Parade! Ten new pets will walk by. Count how many Kip gets right."
17. how: "Tap Start parade."
18 to 28. event, at the end: "Kip got zero out of ten right." "Kip got one out of ten right." and so on through "Kip got ten out of ten right!" (eleven fixed lines, one per score)
29. event: "That's more than last time!" 30. event: "That's the same as last time." 31. event: "That's fewer than last time. Did Kip learn something wrong?"
32. how (after the first full parade): "Tap Teach and show Kip more pets. Then run the parade again."
33. event, the first time a run scores 10 after an earlier run scored less: "The more examples Kip saw, the better Kip guessed!"

Read speaks the hint. During a parade, guesses are shown, not spoken (lines 7 and 8 are Teach only), so the class can call them out.

## Family engine
`kit/ml-lab.js` (family ml-lab, five tools: teach-the-robot, biased-bot, leaf-sorter-ai, model-mechanic, ai-evaluator). This spec holds the full description; the siblings say what they feed it. Loaded with `<script src="kit:ml-lab"></script>` after the kit; exposes `MLLab`. No DOM style of its own beyond what views draw; colors come from CSS variables the tool sets.
- `MLLab.rng(seed)`: mulberry32, exactly `a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296`. Every generated dataset in the family uses it, so numbers in the specs are reproducible.
- `MLLab.uni(R, lo, hi)`: `lo + (hi - lo) * R()`. Generated feature values are rounded to 2 decimals at creation.
- Items: `{id, label, v: {feature: 0..1}, tags: {...}}`. Tags hold groups (room, day or night, district).
- `MLLab.knn(train, item, {features, k})` returns `{label, votes, neighbors: [{item, d}], score(label)}`. Euclidean distance over the listed features. Neighbors sorted by distance, then by position in `train`. Vote by count; a tie goes to the tied label whose nearest member comes first. `score(label)` = share of the k neighbors with that label.
- `MLLab.train(type, train, opts)` returns a model `{type, predict(item) -> {label, score, neighbors?}}`. Types: `'knn'` (opts `features`, `k`), `'tree'` and `'linear'` (binary, opts `features`, `positive`; described in ai-evaluator's spec, the only user).
- `MLLab.evaluate(model, items, {classes, groupBy, positive, threshold})` returns `{n, ok, acc, cm, byGroup, mistakes, tp, fp, fn, tn, recall, precision}`. `cm[true][predicted]` counts. `groupBy(item)` gives a group key; `byGroup[key] = {n, ok, acc, cm}`. With `positive` and `threshold`, the positive label is predicted when its score is at least the threshold.
- Views (SVG, re-laid out on resize, keyboard focusable, every class shown by a glyph or letter as well as a color): `MLLab.view.confusion(el, ev, {classes, names, glyphs, onCell})` (rows true, columns predicted, diagonal cells outlined, counts in every cell, tap a cell to get its items); `MLLab.view.scatter(el, items, {fx, fy, glyphs, query, onPick})` (two features as axes 0 to 1, a query item with lines to its neighbors); `MLLab.view.groupBars(el, byGroup, {names, glyphs})` (one bar per group with "n of m right").
- This tool uses `knn` (k = 1, all six features) and `evaluate` (accuracy only). It draws its own wall and chart, no engine views.

## Sources
- AI4K12, Five Big Ideas in AI, Big Idea 3 "Learning" and the K-2 grade band guidelines: https://ai4k12.org (Touretzky, Gardner-McCune, Martin, Seehorn, AAAI 2019).
- CSTA K-12 Computer Science Standards (2017), 1A-DA-07: https://csteachers.org/k12standards/
- Nearest-neighbor classification (how Kip guesses): scikit-learn user guide, "Nearest Neighbors": https://scikit-learn.org/stable/modules/neighbors.html
- The pets and their feature values are made up for this tool; the parade scores above were computed from them with the engine.

## Done when
1. Teach opens with the welcome on the first tap; Next pet brings Marmalade, and Cat files it on the Cat shelf with line 3.
2. Teaching cards 1 and 2 correctly, then a parade, scores 4 of 10, with misses on Rusty, Luna, Noodle, Pippin, Waffles and Bramble.
3. After all 16 cards taught correctly, the parade scores 10 of 10, and the chart shows both bars with their memory counts.
4. Teaching cards 1 to 11 scores 9 (Pippin missed); adding Ziggy makes the next parade 10, and line 29 plays.
5. Labeling Marmalade as a dog and running the parade gives a different score than the right label; Forget on that card restores it.
6. Every Mystery pet shows one look-alike line ending on the card that decided, and the truth always matches the table.
7. Lines 2, 5 and 17 are each spoken once in a run of five actions; result lines (9, 10, 18 to 31) every time.
8. Next pet, Cat, Dog and Start parade are visible without scrolling at 680x425, 1366x768 and 375 wide; targets are 60 px.
9. Motion off: no walking, same timing, same scores.
