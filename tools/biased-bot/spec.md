# Biased Bot

## One idea
Bitsy, the cafeteria robot, reads the lunch number each student writes on a card, and it was trained only on Room 12's handwriting: run the lunch line and every Room 9 student who writes a 1 with a long flag gets tacos instead of pasta, then discover that piling on more Room 12 cards changes nothing and that a few cards from Room 9 fix it.

## Not like
- teach-the-robot (same family, grade 2): there more examples make Kip better. Here more examples of the same kind do nothing; what matters is whose examples they are, and the harm lands on one group.
- leaf-sorter-ai (same family, grade 5): chooses which clues a classifier may use. Here the clues are fixed (an 8 by 8 grid of ink); the lever is where the training data comes from.
- data-defenders (grade 5): protecting a school's data from attack. Nothing is attacked here; the unfairness comes from ordinary, missing data.
- data-table-builder (grade 4): collect and chart class data. Here the data is handwriting, and the chart is who got the right lunch.
- code-tracer, score-keeper: programs and variables. Bitsy has no program to read; it only has examples.

## Who and how
- Grade 4, computer science. Module: Training Data Matters (Algorithms and Programming). Topic line: "how training data can make AI unfair".
- Driver: students or teacher. Pairs on laptops, or a teacher on a projector asking the class to predict each room's score before a run. 15 to 25 minutes.
- Standards: E4-ALG-ML-02, E4-SOC-HU-18, E4-DAT-IM-11, E3-ALG-ML-02 (module codes). CSTA 2017 crosswalk: 1B-DA-07 (use data to propose cause and effect and predict outcomes), 1B-IC-19 (improve technology for the diverse needs of users), 1B-IC-20 (seek diverse perspectives to improve computational artifacts). Reference: AI4K12 Big Idea 3 (learning) and Big Idea 5 (societal impact).
- tool.json: driver "students or teacher", minutes "15-25", modes ["Lunch Line", "Try Your Writing"], grades_label "Grade 4".

## Screens and modes
Kit frame. Header: title "Biased Bot" with small line "Who did the robot learn from?", mode buttons "Lunch Line" (tray icon) and "Try Your Writing" (pencil icon), Motion, Sound, Read.

### Mode 1: Lunch Line (opens first)
Stage: a cafeteria serving counter (art, below) with Bitsy behind it: a squat robot with a card slot and a screen that shows the number it read. The menu board on the wall is drawn in code: "1 Pasta", "4 Tacos", "7 Salad", each with a food icon. The 30 lunch cards (10 per room) wait in a line on the left as index cards, each with the handwritten number drawn as pencil strokes and a room badge in the corner.
Panel:
- `#hint`.
- Training jars: three jars, one per room, each with its badge, its name and "N cards". Under each: "Fewer" (minus) and "More" (plus), 3 cards per step (one each of 1, 4, 7), from 0 to 30. Tapping a jar opens the card viewer (below).
- "Train Bitsy" (gear icon): retrains on what is in the jars. Enabled only when the jars changed since the last training.
- "Run the lunch line" (play icon, `.big-btn.gold`); "Stop" in its place while running.
- Results: one bar per room (engine `groupBars`): "Room 12: 10 of 10 right lunches". A small "Mix-ups" list under it: "Room 9: 4 cards wrote 1 (pasta), got tacos." A visible score strip on the stage puts Room 9 first after a run, including in compact windows.
- "Start over" (circular arrow): jars back to the start, results cleared.
Card viewer (overlay on the stage, closes with Close or Escape): each room's ten lunch cards are always shown for handwriting comparison, even if the training jar is empty. The actual jar cards appear in a separate section when present. Both sections are grouped 1, 4, 7.

### Mode 2: Try Your Writing
Stage: a big drawing pad (an index card, 300 to 420 px square on large screens, smaller in short or narrow boxes so the drawing and ink grid remain side by side) on the left; on the right "What Bitsy sees": the 8 by 8 grid of the drawing, each cell shaded by its ink; under it "Bitsy reads: 4" and the three training cards it found most alike, each with its room badge and number.
Panel: `#hint`; "Clear pad" (eraser); "Bitsy, read it!" (eye icon); "Teach Bitsy my way" with three buttons "It's a 1", "It's a 4", "It's a 7": adds the drawing to a fourth jar "My cards" (pencil badge) and retrains. "My cards" exists for this page load only, is never saved, and shows its count in both modes.

## Content
The story (shown on first load as a card on the stage, also spoken): "Room 12 built Bitsy to read lunch cards, and they trained it with their own handwriting. Now the whole school uses it."
Rooms and how they write (fictional rooms; badge shape plus color):
| Room | Badge | How they write | Template set | Slant | Wobble |
|---|---|---|---|---|---|
| Room 12 | blue circle #2f6db5 | 1 as a straight stick, 7 plain, 4 closed at the top | plain | 0.08 | 3 |
| Room 3 | green square #26774d | first graders: same shapes, big and wobbly | plain | 0.28 | 7 |
| Room 9 | berry triangle #b23a6e | 1 with a long flag, 7 with a line through it, 4 open at the top | flag | 0.08 | 3 |

On screen, in the card viewer for Room 9: "Lots of people learn to write 1 with a long flag and 7 with a line through it."
Templates (strokes in a 100 by 100 box, y down; each stroke a list of points):
- plain 1: (50,10)-(50,90). plain 4: (62,10)-(20,64)-(82,64) and (62,10)-(62,90). plain 7: (20,12)-(80,12)-(42,90).
- flag 1: (22,46)-(62,10)-(62,90). flag 4: (28,10)-(24,60)-(82,60) and (66,28)-(66,90). flag 7: (20,12)-(80,12)-(42,90) and (30,52)-(74,52).
Card generation (engine `rng`): per card, `s = (2R()-1) * slant`; then for each stroke, each point: `x' = x + (2R()-1) * wobble + s * (50 - y)`, then `y' = y + (2R()-1) * wobble`.
- Jar cards: seeds Room 12 1201, Room 9 901, Room 3 301. Ten rounds of (1, 4, 7) in that order. A jar holding N cards uses the first N/3 cards of each digit.
- Lunch line cards: seeds 1202, 902, 302. Four rounds of (1, 4, 7); keep the first 4 ones, 3 fours and 3 sevens, in that order: 10 per room, line order Room 12, Room 3, Room 9 interleaved card by card.
Grid (the features): shift and scale the strokes so the longest side of their bounding box is 80, centered on (50,50); sample a 32 by 32 grid of points at ((i+0.5)*100/32, (j+0.5)*100/32); a point is ink when it is within 6 units of any stroke segment; each of the 8 by 8 cells is the share of ink points in its 4 by 4 block (0 to 1). The pad uses the same pipeline on the student's pointer strokes.
Classifier: engine `knn`, k = 3, over the 64 grid cells.
Checked results (lunch line, per room, right lunches of 10):
| Jars (Room 12 / Room 9 / Room 3) | Room 12 | Room 3 | Room 9 |
|---|---|---|---|
| 15 / 0 / 0 (start) | 10 | 10 | 6 (all four 1s read as 4) |
| 30 / 0 / 0 | 10 | 10 | 6 |
| 15 / 0 / 30 | 10 | 10 | 6 |
| 15 / 3 / 0 | 10 | 10 | 6 |
| 15 / 6 / 0 | 10 | 10 | 10 |
| 15 / 15 / 15 | 10 | 10 | 10 |
| 0 / 15 / 0 | 6 (1s read as 7) | 6 (1s read as 7) | 10 |
| 3 / 0 / 0 | 10 | 10 | 5 |
Talk points the table supports: messy writing (Room 3) was never the problem; a style Bitsy never saw was. With Room 12 at 15 and Room 3 empty, one Room 9 card of each number is not enough for the three-neighbor vote; two are. This is conditional on these jar settings. Training only on Room 9 flips the harm onto everyone else.

## Interactions in detail
- Run: each card slides into Bitsy's slot (0.9 s per card, 30 cards, about 27 s), Bitsy's screen shows the number it read, and a tray slides out with that food icon. A mix-up shows the tray plus a sticker "Wanted pasta" with the food the card asked for. The room bars fill as cards finish. Stop halts; the bars show the cards done so far, marked "stopped".
- "Skip to results" (fast-forward icon) appears during a run and finishes it at once.
- Changing a jar marks the results "old" (greyed, with "Train Bitsy, then run again"); Run is disabled until Train Bitsy is pressed. Train Bitsy shows a 0.6 s gear spin.
- A jar at 0 disables Fewer; at 30, More. All jars at 0: Train Bitsy is disabled and the hint says to add cards.
- Pad: pointer draws a 9 px pencil line; up to 6 strokes; a 7th stroke clears the pad first. An empty pad disables "Bitsy, read it!". Reading shows the grid, the guess and the three look-alikes. Nothing is kept after the page closes.
- "Teach Bitsy my way" adds the current drawing to My cards with the chosen label and retrains; the lunch line results go "old". My cards counts in training like any jar. Teaching keeps the last trained room jars, leaving pending jar changes untrained. Show which jar received the card, update the three look-alikes immediately, and explain a one-of-three vote when it cannot change the guess.
- A different mode hushes and keeps each mode's state. Re-tapping the current mode does nothing. Start over also empties My cards.
- Keyboard: Tab order is mode buttons, header, panel controls (jars in order), then stage cards. The pad also accepts arrow keys to draw (a keyboard pen: arrows move, Space lifts and lowers the pen) so the mode works without a mouse.
- Sizes: Run, Train Bitsy and the jar buttons visible without scrolling at every STANDARDS.md size; in short windows the lunch line shows 10 cards at a time and scrolls itself. Scene text at least 10 px in the preview.

## Look
- Accent `--brand #8a5a00` (mustard; header). Own `:root`: `--paper #fffaf0`, `--ink #2a2418`, `--muted #6b5f48`, `--line #eadfc8`, `--brand #8a5a00` (mustard; header), `--focus #1d5fd1`.
- Stage: cafeteria art with a #e9f1ee tile wall tint; cards white with pencil strokes #3b3b3b; foods pasta #e7b53c, tacos #d9662b, salad #4f9a3a, each with an icon.
- Room badges: Room 12 blue circle #2f6db5, Room 9 berry triangle #b23a6e, Room 3 green square #26774d; My cards pencil #6b5f48. Shape plus name, never color alone.
- Neighbors: code-tracer rust #a8461a, score-keeper raspberry #a82755, game-remix teal #0b6b6f. Mustard on cream reads as a lunchroom and differs from them.
- Contrast: white on #8a5a00 5.93:1; ink on paper 14.80:1; muted on paper 6.02:1; brand on paper 5.70:1; brand on tile 5.16:1; focus on paper 5.59:1; white on room badges 5.28, 5.64, 5.49:1; ink on pasta 8.12:1. All pass AA.

## Art
- `cafeteria-counter`: "a bright school cafeteria serving counter with steel trays, a sneeze guard and a blank green menu board on a tiled wall, flat vector illustration, soft daylight, front view"; 16:9; cutout no; people no; Cloudflare FLUX.2 (`scripts/cfart.py`). Used full-bleed behind the lunch line; the menu text is drawn in code over the blank board. Ask for a blank board so no fake lettering appears.
Everything else (Bitsy, cards, trays, foods, jars, grid, preview.svg) is drawn in code.

## Voice
Bank voice `news-reader`, style "Say clearly and steadily, like a trusted radio news reader", framed as the school's morning announcements reporting on the lunch line. Not used by a neighbor (code-tracer clear-teacher, score-keeper friendly-dad, game-remix big-sister) or by a group sibling.
1. how, welcome Lunch Line: the story first, then "Press Run the lunch line to see how Bitsy does." A first tap on Run still speaks the story, then "Watch the lunch cards, or press Stop or Skip to results."
2. event, after a run (one per room result, numbers filled from fixed clips): "Room 12 got 10 right lunches out of 10." The tool records the eleven totals per room as fixed lines ("Room 9 got 6 right lunches out of 10.") and plays the three in room order. Use "1 right lunch" for a total of one. A relevant same/flip/all teaching event may lead the totals.
3. event, when any room is under 8: "Some students got the wrong lunch. Tap a room's jar to see how its students write."
4. how, first jar change: "Pick the cards, then press Train Bitsy."
5. event, when Room 9 stays at 6 after only Room 12 or Room 3 cards were added: "More cards from the same rooms did not help Room 9."
6. event, the first time all three rooms reach 10: "Every room got the right lunch this time." Only when every room has training cards, add "Every room has cards in the training jars. Bitsy learned from all three rooms."
7. event, when a room drops below 10 that was at 10 before: "Now a different room is getting the wrong lunch."
8. how, welcome Try Your Writing: "Write a 1, a 4 or a 7 on the card, the way you always do. Use arrows and Space for the keyboard pen." After ink exists, prompt the enabled Bitsy, read it! control.
9. event: "Bitsy read a 1." "Bitsy read a 4." "Bitsy read a 7." (three lines; stale once the pad changes)
10. how, after the first read: "If Bitsy got it wrong, teach it your way with the buttons below."
11. event: "Your card went into My cards." (stale on the next pad change)
Read speaks the hint. Event feedback cuts an instructional line already playing, while preserving other event feedback and Read's priority. The instruction remains available in the current hint. Narration never names a real place or group of people.

After a run, when Room 9 has training cards but still scores below 10, the hint says "Room 9 still got wrong lunches. Press More under Room 9 again, then Train Bitsy." When only Room 9 is trained (0 / 15 / 0), the other-room experiment says "Try examples from the other rooms. Use More under Room 12 or Room 3, then Train Bitsy."

## Family engine
ml-lab (`kit/ml-lab.js`, full description in tools/teach-the-robot/spec.md). Uses `rng` and `uni` for the cards, `knn` (k = 3, features = the 64 grid cells, items tagged `room`), `evaluate` with `groupBy: item => item.tags.room`, and the `groupBars` view for the room results. The grid rasterizer and stroke templates stay in this tool.

## Sources
- Numeral styles (a 1 with a long upstroke and a 7 with a crossbar are common in much of Europe and Latin America): "Regional handwriting variation", Wikipedia, section "Arabic numerals": https://en.wikipedia.org/wiki/Regional_handwriting_variation
- Training-data representation and societal impact: AI4K12 Big Idea 5 "Societal Impact", https://ai4k12.org ; Buolamwini and Gebru, "Gender Shades", Proceedings of Machine Learning Research 81 (2018), https://proceedings.mlr.press/v81/buolamwini18a.html, for the teacher notes only: measured accuracy gaps by skin type and gender in commercial classifiers, without access to the companies' training data.
- CSTA K-12 Computer Science Standards (2017): https://csteachers.org/k12standards/
- Rooms, cards and all results are made up for this tool; the results table was computed with the engine and the rules above.

## Done when
1. From the start (Room 12 jar 15), a run gives Room 12 10, Room 3 10, Room 9 6, and the mix-ups list counts four Room 9 cards that wrote 1 (pasta) and got tacos.
2. Raising Room 12 to 30 and retraining still gives Room 9 6, and line 5 plays.
3. Room 9 at 3 still gives 6; at 6 gives 10 for every room, and line 6 plays.
4. Room 12 and Room 3 at 0, Room 9 at 15: Room 12 and Room 3 drop to 6 with 1s read as 7, and line 7 plays.
5. Run is disabled after a jar change until Train Bitsy is pressed; results show as old.
6. A drawn stick 1 reads as 1; the grid view matches the drawing; the three look-alikes show room badges. Teaching a drawing adds to My cards and changes later reads.
7. Every room is told apart by badge shape and name with color off (grayscale screenshot).
8. Run, Train Bitsy and the jars are on screen without scrolling at 680x425, 1366x768, 760 wide and 375 wide.

## Open questions
- The teacher notes would name the real-world parallel (face recognition that worked worse for darker-skinned women, Gender Shades 2018). Keep it in the notes only, or leave it out for grade 4?
