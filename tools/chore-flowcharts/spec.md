# Chore Flowcharts
Renamed from: Flowchart Factory

## One idea
Build a flowchart for a household chore and watch it turn into pseudocode line by line as you build, then run it against a stack of test days (a dirty bowl, a stained load of darks, a plant row with one wet pot) while a token walks your arrows, so every failed day stops on the exact box that did the wrong thing.

## Not like
- function-machine-factory (math 8): the overlap pass flagged a second "Factory" title in 6-8. Renamed to Chore Flowcharts (Cory's suggested fix), topic word kept; there are no machines or factory here, only chores.
- code-kitchen (6-8, same group): writes procedures with typed values and reuses them. Here there are no variables to type and no reuse: the skill is control flow (order, if/else, repeat until) drawn as shapes and tested against cases.
- code-tracer (grade 4): predicts values while a fixed program runs. Here you build the algorithm, and the test days, not predictions, judge it.
- traffic-light-coder (grade 3): if-then rules for one intersection. Here decisions nest inside loops, and the same chart must survive four different days.
- decision-tree (SEL 6-8): branches over time for a life choice, no right answer. Here a chart passes or fails a test day by the house rules.
- loop-garden (grade 2): fewest blocks wins. Here nothing counts blocks; a chart passes when every test day passes, and extra work is only noted.

## Who and how
- Grades 6 to 8, computer science. Module: Flowcharts and Pseudocode (Algorithms and Programming), "Model algorithms with control structures and procedures". Topic line: "flowcharts and pseudocode".
- Driver: students on laptops, alone or in pairs (one builds, one reads the pseudocode aloud). A teacher can run Feed the cat on a projector first.
- 20 to 30 minutes: Feed the cat and Laundry (10 min), Water the plants (8 min), Sort the recycling (10 min).
- Standards (CSTA 2026, as listed): MS-ALG-PS-01, MS-ALG-PS-02, MS-ALG-PS-03. CSTA 2017 crosswalk (matched by topic): 2-AP-10 (use flowcharts and/or pseudocode to address complex problems as algorithms), 2-AP-12 (design programs that combine control structures, including nested loops and compound conditionals), 2-AP-17 (systematically test and refine programs using a range of test cases).
- tool.json: driver "students", minutes "20-30", modes [] (one workspace, four chores), grades_label "Grades 6-8". Kit starter.

## Screens and modes
Header (kit): "Chore Flowcharts", small line "Flowcharts and pseudocode". No mode buttons. Motion, Sound, Read.

Focus: the flowchart, the biggest thing, on the left of the stage; while a test day runs, the token walking it. The pseudocode card and the scene strip are smaller, on the right.

Stage, three parts laid out at real pixel size per window:
1. **Chart** (left, about 55 percent): the flowchart, drawn top to bottom in SVG, auto laid out (no free dragging, so arrows never tangle). Shapes: START and END ovals, steps as rectangles, questions as diamonds. Every arrow has a round **+** insert point (44 px target) at its middle. The chart scrolls inside its box when long.
2. **Pseudocode card** (right top): the same algorithm as indented pseudocode, rebuilt after every edit. Hovering or focusing a block highlights its line, and tapping a line selects its block.
3. **Scene strip** (right bottom, about 140 px tall): the chore's painted backdrop (art: scene-*) with painted cutouts placed on it that change as the token walks: the bowl swaps between dirty, clean and with food and moves onto the mat, the water dish fills, the cat waits by the mat (Feed the cat); the washer with its dial readout drawn in code on its blank display, the load basket and the soap jug, which moves to the washer when soap is added (Laundry); the six plants in their pots with a code soil tag (dry or moist) under each and the watering can moving along the row with a three-drop gauge in code (Water the plants); the item in hand moving from the kitchen bin into one of the three bins, with a code "rinsed" tag after Rinse (Sort the recycling).

Panel (kit `aside`):
- `#hint`.
- **Chore** picker: four buttons, Feed the cat, Laundry, Water the plants, Sort the recycling (each with a small painted icon from its kit: cat, washer, watering can, blue bin).
- **House rules** card for the chore (Content), always visible, short.
- **Test days**: one card per day showing its inputs as icons plus words, a ▶ button and a result line (blank, "Passed", "Passed, 1 extra step", or "Failed: reason"). Under them **+ New test day**.
- Buttons: **Run all** (big, `.gold`), **Step**, **Stop**, **Undo**, **Reset chart** (back to the chore's starter chart).
- Insert menu (opens from a +): **Step**, **If**, **Repeat until**, and **Paste** when something is cut; then the chore's list of steps or questions to pick from.
- Block toolbar (opens when a block is selected): **Change**, **Cut**, **Delete**, and for an If block **Swap Yes and No**.

## Content

Pseudocode style (this tool's own, close to the AP CSP reference sheet): `START`, one step per line, `IF condition THEN` / `ELSE` / `END IF`, `REPEAT UNTIL condition` / `END REPEAT`, `END`. Body lines indent two spaces per level. The ELSE line appears only when the No branch has blocks. REPEAT UNTIL checks its condition before each pass (so a loop may run zero times). Diamonds show the question ("Bowl dirty?"); pseudocode shows the condition ("the bowl is dirty").

Shapes: If diamond with **Yes** going down-left and **No** going down-right, rejoining at a dot below. Repeat until diamond on top: **No** goes down into the body, the body's last arrow loops back up the left side to the diamond, **Yes** leaves to the right and down. Arrow labels are words, never color alone.

**Chore 1: Feed the cat.** House rules: "Food goes in a clean bowl. The bowl goes on the mat. The water dish is full."
- State: bowl clean or dirty; food in bowl; bowl on the mat; water dish empty or full.
- Steps: Rinse the bowl (bowl clean; any food is washed away). Scoop food into the bowl (food in; if the bowl is dirty, note "food in a dirty bowl"). Put the bowl on the mat. Fill the water dish.
- Questions: "Bowl dirty?" (the bowl is dirty), "Water dish empty?" (the water dish is empty).
- Pass: food in the bowl, bowl on the mat, water full, no food went into a dirty bowl. Extra step: rinsing a clean bowl, filling a full dish.
- Test days: Monday (bowl dirty, water empty), Tuesday (bowl clean, water full), Wednesday (bowl dirty, water full), Thursday (bowl clean, water empty).
- Starter: START, Scoop food into the bowl, Put the bowl on the mat, END. Passes Tuesday only.
- Reference: IF the bowl is dirty THEN Rinse END IF; Scoop; Put on mat; IF the water dish is empty THEN Fill END IF. Passes all four, no extra steps.

**Chore 2: Laundry.** House rules (this family's, made up for this tool): "Whites wash in hot water, darks in cold. Delicates use the gentle cycle, everything else normal. Pre-treat a stain before washing. Soap goes in before you start."
- State: water temperature (unset, hot, cold), cycle (unset, gentle, normal), soap in, stain treated, washer running.
- Steps: Pre-treat the stain. Set water to hot. Set water to cold. Choose the gentle cycle. Choose the normal cycle. Add soap. Start the washer.
- Questions: "Whites?" (the load is whites), "Stain?" (there is a stain), "Delicate?" (the load is delicate).
- Checked at Start the washer: temperature set and right, cycle set and right, soap in, stain treated if there is one. Any step after the washer starts fails ("The washer is already running"). Never starting fails ("The washer never started"). Extra step: pre-treating with no stain, setting the same setting twice.
- Test days: Load 1 (whites, no stain, sturdy), Load 2 (darks, stain, sturdy), Load 3 (darks, no stain, delicate), Load 4 (whites, stain, delicate).
- Starter: START, Add soap, Start the washer, END. Fails all four ("The water temperature was never set").
- Reference: IF whites THEN hot ELSE cold END IF; IF delicate THEN gentle ELSE normal END IF; IF stain THEN pre-treat END IF; Add soap; Start. Passes all four.

**Chore 3: Water the plants.** House rules: "Water a plant only when its soil is dry. The can holds 3 waterings."
- State: a row of plants (each dry or moist), the plant you are at (starts at the first), water in the can (0 to 3).
- Steps: Water this plant (uses 1; the plant becomes moist). Refill the can (to 3). Go to the next plant.
- Questions: "Every plant checked?" (every plant is checked: you are past the last plant), "Soil dry?" (the soil is dry), "Can empty?" (the can is empty).
- Fails: watering a moist plant ("Too much water for the ivy"), watering with an empty can ("The can was empty"), asking about soil, watering or going to the next plant past the last plant ("There's no plant here"), 200 steps without reaching END ("Stopped after 200 steps. This chart may never end."). Pass: every dry plant watered once, END reached. Extra step: refilling a full can.
- Test days: Monday (fern dry, ivy moist, cactus dry, palm dry; can full), Wednesday (fern, ivy, cactus, palm dry, violet moist, aloe dry; can full), Friday (fern, ivy, cactus all moist; can full), Sunday (aloe dry; can empty).
- Starter: START, REPEAT UNTIL every plant is checked [Water this plant, Go to the next plant] END REPEAT, END. Monday fails at the ivy, Wednesday at the palm (can empty), Friday at the fern, Sunday at the aloe (can empty).
- Reference: REPEAT UNTIL every plant is checked [IF the soil is dry THEN (IF the can is empty THEN Refill END IF; Water) END IF; Go to the next plant] END REPEAT. Passes all four.

**Chore 4: Sort the recycling.** House rules (Maple Street's, made up for this tool): "Blue bin: cans, glass jars, paper and clean plastic tubs; rinse food off first. Green bin: food scraps. Gray bin: everything else."
- Items (kind, has food on it): soup can (recycle, yes), newspaper (recycle, no), banana peel (food), chip bag (other), glass jar (recycle, yes), apple core (food), yogurt tub (recycle, no).
- State: items left in the kitchen bin (in order), the item in your hand, the three bins.
- Steps: Pick up the next item. Rinse it. Put it in the blue bin. Put it in the green bin. Put it in the gray bin.
- Questions: "Kitchen bin empty?" (the kitchen bin is empty), "Recyclable?" (it can be recycled), "Food?" (it is food), "Food on it?" (it has food on it).
- Fails: a put with empty hands ("Your hands are empty. Pick up an item first."), picking up while holding ("You're already holding the soup can."), picking up from an empty kitchen bin ("The kitchen bin is empty."), a question about an item while holding nothing ("You aren't holding anything."), a wrong bin ("The chip bag doesn't go in the blue bin."), a recyclable with food on it in blue ("Rinse the soup can first."), the 200-step stop. Extra step: rinsing anything that has no food on it.
- Test days: Monday (soup can, newspaper, banana peel, chip bag), Tuesday (glass jar, apple core, yogurt tub), Wednesday (kitchen bin already empty), Thursday (chip bag, chip bag, newspaper).
- Starter: START, REPEAT UNTIL the kitchen bin is empty [Pick up the next item, Put it in the gray bin] END REPEAT, END. Passes only Wednesday.
- Reference: REPEAT UNTIL the kitchen bin is empty [Pick up; IF it can be recycled THEN (IF it has food on it THEN Rinse END IF; Blue) ELSE (IF it is food THEN Green ELSE Gray END IF) END IF] END REPEAT. Passes all four.

**New test day:** a card with the chore's inputs as toggles (Feed the cat: bowl, water; Laundry: whites or darks, stain, delicate; Water the plants: 1 to 6 plants each dry or moist, can full or empty; Recycling: up to 5 items picked from the seven). It is judged by the same house rules. Up to 4 extra days per chore; each has a **Remove** button.

## Interactions in detail
- Opens on Feed the cat with the starter chart and nothing run yet. A + tap opens the insert menu beside it; choosing If makes a diamond with two empty branches (each just an arrow with its own +); choosing Repeat until makes the loop with an empty body (one + inside).
- Cut removes a block with everything inside it and holds it on a chip at the top of the panel until pasted or replaced. Delete asks nothing; Undo (up to 30 edits) brings it back. Reset chart asks "Go back to the starter chart?" Yes / No.
- Swap Yes and No moves the Yes branch's blocks to No and back; the condition stays the same.
- Run all runs each test day in order at 250 ms per block (the token moves, the scene strip updates), writing each result. A card's ▶ runs that day at 450 ms per block. Step runs the selected day (the last one run or tapped) one block per press. Stop halts a run and clears the token. Any edit stops a run and greys every result ("Edited: run again").
- Short runs: each day's result is computed first. The token walks at most 40 blocks of a day; past that it jumps, with a "fast forward" tag, to the block where the day ends (so the 200-step stop takes about 10 s, not 50). The four reference charts take 4 to 19 s for Run all (Water the plants is the longest, 74 blocks).
- Controls stay live during a run: a tap on another day's ▶ stops the current run and starts that day at once; Step pauses the run on the current block; a chore button stops the run and switches at once; selecting a block or an edit stops it at once.
- A failure stops the token on the block that broke a rule: that block gets a red outline, a ✗ and the reason in a callout beside it; its pseudocode line gets the same mark. END reached with a rule unmet (the washer never started, a dry plant skipped) marks END.
- "Passed, N extra steps" outlines each extra block in amber with a small "extra" tag. It is a pass.
- When all of a chore's test days pass, its chore button gets a ✓ (kept for the page load only). Charts are kept per chore while the page is open; nothing is saved.
- Limits: 40 blocks per chart (the + points hide at 40, hint says so); nesting up to 3 deep.
- Motion off: the token jumps block to block at the same timing; cutouts in the scene strip swap in place without sliding; no callout slide.
- Sizes: at 1366x768 the chart, pseudocode and Run all are visible without scrolling; under about 900 px tall the panel puts Run all and the test days first and the house rules collapse to one line with a **Rules** toggle. At 760 wide the panel goes below the stage with Run all first. At 375 wide the pseudocode card folds under the chart behind a **Pseudocode** toggle and the scene strip shrinks to 100 px; + points stay 44 px.
- Keyboard: Tab reaches panel controls first, then the chart's blocks and + points in reading order; Enter opens a + menu or selects a block; Delete removes the selected block; Ctrl+Z undoes.
- `window.__tool = {state, setChore(id), chart(), setChart(json), run(dayId), runAll(), pseudocode()}` for tests.

## Look
- Accent `--brand #0e7490` (deep cyan, the START and END ovals and the header rule). Band 6-8, own light `:root`: a clean whiteboard with sticky-note diamonds.
- `--paper #f4f7f6`, `--panel #ffffff`, `--ink #14232a`, `--muted #4f6169`, `--line #d5dfe0`, `--btn #14232a`, `--head-ink #ffffff`, `--focus #c2410c`.
- Chart: steps white with a 2 px ink border; diamonds sticky-note yellow `#fff4d6` with ink border; arrows ink 2 px; the token an orange `#c2410c` dot with a white ring; pass `#15803d` with ✓, fail `#b91c1c` with ✗, extra amber `#b45309` outline with the word "extra". Pseudocode in a monospace stack, keywords bold.
- Scene strip: bright daylight home colors in soft gouache (sage, sky blue, warm wood), framed by a 1 px `--line` border so it reads as a window onto the house, not part of the chart. Code tags on it (soil, rinsed, delicate, the dial readout) are ink on white chips.
- Contrast (computed): white on brand 5.36:1; brand on paper 4.97:1; ink on paper 14.94:1; muted on paper 6.00:1; ink on diamond yellow 14.70:1; token and focus orange on paper 4.80:1; pass green on white 5.02:1; fail red on white 6.47:1; ink on white chips 16.11:1. All pass AA.
- Neighbors: code-kitchen copper on cream (a painterly diner), code-tracer slate and graph paper, packet-race signal red, model-mechanic dark lime. Minimal celebration: a ✓ on the chore button.

## Art
Local FLUX (`scripts/localart.py`), none with people. One style for all: soft gouache home illustration, bright daylight, simple clean shapes. Four small kits, one per chore; each piece is a cutout on a plain white background (prompt ends "soft gouache illustration, plain white background"), placed on its chore's backdrop by one sizing rule: pieces stand on the backdrop's floor line, each scaled to its listed share of the strip height.
- scene-kitchen, scene-laundry, scene-plants, scene-recycling: "A quiet kitchen corner with a small rug mat on a wooden floor and a pale wall" / "A small laundry nook with a tiled floor and a shelf" / "A sunny windowsill shelf running the full width, empty, with a wooden floor below" / "A kitchen corner with a tiled floor and empty space along the wall", each "soft gouache illustration, bright daylight"; 4:1; cutout no; people no; the scene strip backdrop for each chore.
- Feed the cat kit (6 pieces): bowl-dirty "a ceramic pet bowl with dried food smears" (25%); bowl-clean "a clean shiny ceramic pet bowl" (25%); bowl-food "a ceramic pet bowl filled with dry cat food" (25%); dish-empty "an empty steel water dish" (20%); dish-full "a steel water dish full of clear water" (20%); cat "a tabby cat sitting and waiting, looking up hopefully" (70%); 1:1; cutout yes; people no.
- Laundry kit (4 pieces): washer "a front-loading washing machine with a round door and a blank dark display panel" (95%, the dial readout and settings drawn in code on the blank panel); basket-whites "a laundry basket of white towels and shirts" (45%); basket-darks "a laundry basket of dark jeans and navy shirts" (45%); soap "a plain blue laundry soap jug with a blank label" (35%); 1:1; cutout yes; people no. The stain and "delicate" are code tags on the basket.
- Water the plants kit (7 pieces): fern, ivy, cactus, palm, violet, aloe, each "a [plant] in a plain terracotta pot" (55 to 75%); watering-can "a green metal watering can" (40%); 1:1; cutout yes; people no. Dry and moist are code soil tags under each pot, so one picture per plant.
- Sort the recycling kit (11 pieces): kitchen-bin "a small white kitchen trash bin with a step pedal" (60%); bin-blue, bin-green, bin-gray "a tall [blue / green / gray] wheelie bin with a blank lid" (90%); soup-can "an open soup can with a blank paper label and soup smeared inside"; newspaper "a folded newspaper with blank gray columns"; banana-peel "a banana peel"; chip-bag "a crinkled chip bag in plain orange foil with a blank front"; glass-jar "an empty glass jar with sauce smeared inside"; apple-core "an apple core"; yogurt-tub "a clean empty plain white yogurt tub" (items 20 to 30%); 1:1; cutout yes; people no. The four chore picker icons reuse cat, washer, watering-can and bin-blue.
Thirty-two images in all (4 backdrops, 28 pieces). The chart, arrows, token, + points, tags, gauges, the dial readout and preview.svg (a Feed the cat flowchart with its pseudocode beside it) are drawn in code: they are the diagram and its labels.

## Voice
Bank voice `friendly-dad` (Achird), "Say in a relaxed, friendly way, like a kind dad helping with homework", here a parent handing over the chore list. Not used by any group sibling or 6-8 CS neighbor (algorithm-audit calm-professor, code-kitchen easy-coach, misleading-charts news-reader, model-mechanic science-narrator, packet-race firm-captain); flowchart-factory, this tool's old name, was the only listed user. Item names, rules and pseudocode are on screen only. `Curio.voice`, one scope (the chore), `welcomeAfter: true`.
- welcome (how, first time each chore opens; stale once a run starts or an edit is made): "Here's a chore and its flowchart. Press Run all to test it on every day."
- plus (how, after the first run ends; stale on the first edit): "Tap a plus on any arrow to add a step, an if, or a repeat."
- branch (how, first If added; stale when a block goes into a branch): "Yes goes left, no goes right. Tap the plus inside a branch to fill it."
- loop (how, first Repeat until added; stale on the next edit): "The loop checks its question first, then runs the boxes inside until the answer is yes. Tap the plus inside it to add a box."
- failed (event, a run ends with any failure; stale on the next edit or run): "Some days failed. Tap the box with the red X to see why, then change the chart."
- never (event, the 200-step stop; stale on the next edit or run): "That loop never ended. Something inside has to move you forward."
- extra (how, first extra-step pass; stale on the next edit): "It works, but a box did work it didn't need to. Add an if so it can skip that box."
- allpass (event, all days pass; stale on the next edit or chore change): "Every day passed. Press New test day, or pick the next chore."
- newday (how, first New test day; stale when its ▶ is pressed): "Set the toggles for a tricky day, then press its play button."

## Family engine
none

## Sources
- CSTA 2026 ids MS-ALG-PS-01, MS-ALG-PS-02, MS-ALG-PS-03 (`data/standards/csta-2026-ids.txt`); CSTA K-12 CS Standards (2017) 2-AP-10, 2-AP-12, 2-AP-17: https://csteachers.org/k12standards/
- Flowchart shapes (oval terminal, rectangle process, diamond decision): ISO 5807:1985, "Documentation symbols and conventions for data, program and system flowcharts"; summary in "Flowchart", Encyclopaedia Britannica, https://www.britannica.com/technology/flowchart
- Pseudocode keywords and REPEAT UNTIL checked before each pass: College Board, AP Computer Science Principles Exam Reference Sheet, https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf
- Testing with a range of cases, including edge cases (an empty bin, one plant): CSTA 2-AP-17 (above).
- Chores, house rules, items and test days are original to Curio Class and labeled as made up; no real-world laundry or recycling claim is made.
- Checks run (a Python interpreter of the four chores' rules, 2026-10-29): every starter result in Content (Feed the cat passes Tuesday only, Monday and Wednesday fail on the dirty bowl, Thursday at END; Laundry fails all four at Start the washer on temperature; Water the plants fails Monday at the ivy, Wednesday at the palm with the can empty, Friday at the fern, Sunday at the aloe with the can empty; Recycling passes Wednesday only). Every reference chart passes all four days with no extra steps. Without "Go to the next plant" every day but Sunday fails on overwatering the fern; with only a non-moving If, Monday to Friday hit the 200-step stop. Block counts for Run all at 250 ms: Feed the cat 28 (7 s), Laundry 38 (9.5 s), Water the plants 74 (18.5 s), Recycling 64 (16 s); a 200-step day would have taken 50 s, so the walk now stops at 40 blocks and jumps. Two fail rules the reference never meets but a student chart can were missing and are added (going to the next plant past the last one, picking up from an empty kitchen bin).

## Done when
1. Each chore's starter chart gives the results in Content (Feed the cat passes Tuesday only; Laundry fails all four on temperature; Water the plants fails each day where listed; Recycling passes Wednesday only).
2. Each reference chart, built by hand, passes all four days with no extra steps; the pseudocode matches Content line for line with two-space indents.
3. Adding an If shows a diamond with Yes and No branches; Swap Yes and No moves the branch blocks; ELSE appears in the pseudocode only when No has blocks.
4. Repeat until with no "Go to the next plant" in Water the plants fails with the overwater reason (Monday, the fern); with only a non-moving step, the 200-step stop marks the loop after at most 40 walked blocks and a fast forward.
5. A failure marks the block and its pseudocode line with ✗ and the reason; an extra step marks amber and still passes.
6. New test day: a Laundry day (darks, stain, delicate) is judged by the rules; four extra days max; Remove works.
7. Cut and Paste move a whole If with its branches; Undo restores 30 edits; Reset chart asks first.
8. Every size in STANDARDS.md: Run all, the chart and the test days reachable without page scrolling; 375 wide folds the pseudocode; + points 44 px.
9. Voice: welcome once, each how line once then hint only, failed and allpass each time while fresh; no line names a hidden or disabled control; Read speaks the hint; console clean; no network requests; the name only as "Curio Class".
10. Focus: at 1366x768 and 1000x625 the flowchart is the largest thing on the stage, and during a run the token is on screen in it (the chart box scrolls to follow it).
11. Tap while it plays: during Run all, a tap on another day's ▶ starts that day at once, Step pauses on the current block, and a chore button switches at once; the scene strip always matches the token's block.
12. The scene strip shows each chore's painted pieces changing with the state (the bowl swaps, the soap jug moves, the can moves along the plants, the item drops into its bin).

## Open questions
- [chore-flowcharts] The Print button (chart plus pseudocode) was removed under the no print cards rule. OK, or does Cory want a print for the classroom wall?
- [chore-flowcharts] Thirty-two new images (four backdrops and four small kits of 6, 4, 7 and 11 cutouts), none with people; the old spec drew everything in code. Too many for a scene strip that sits beside the chart?
