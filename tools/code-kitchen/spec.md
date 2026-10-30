# Code Kitchen

## One idea
Orders hang on the ticket rail and you cook them by writing code on a recipe card, where "3" with quotes is text and stops the griddle, and then the manager changes the menu ("the Classic gets 4 pancakes now") and the tool counts how many edits your code needs, so a procedure with a parameter (one change) beats copy and paste (five changes) in a way you feel.

## Not like
- chore-flowcharts (flowchart-factory, 6-8, same group): draws control flow as shapes and tests it on days. Here there are no flowcharts, ifs or loops: the skill is values with types, variables, and procedures with parameters, measured by edits after a change.
- code-tracer (grade 4): predicts values in a fixed program. Here you write and change the program; the jars show values only as a readout.
- loop-garden (grade 2): fewer blocks earn more stars. Here length never scores; the par is how few edits a menu change needs.
- score-keeper (grade 3): variables change while a game runs. Here variables hold typed values you choose, and the wrong type is the puzzle.
- kitchen-lab, recipe-scaler, smoothie-lab (math): measuring and scaling food. Here food is only output; no fractions, ratios or measuring.

## Who and how
- Grades 6 to 8, computer science. Module: Variables, Data Types and Procedures (Algorithms and Programming), "Store data and structure reusable code". Topic line: "variables, data types and procedures".
- Driver: students on laptops, alone or in pairs.
- 20 to 35 minutes: Sets A and B (12 min), C and D (15 min), Open kitchen any time.
- Standards (CSTA 2026, as listed): MS-PRO-VD-16, MS-PRO-PD-12, MS-PRO-RD-17. CSTA 2017 crosswalk (matched by topic): 2-AP-11 (create clearly named variables that represent different data types and perform operations on their values), 2-AP-14 (create procedures with parameters to organize code and make it easier to reuse), 2-AP-13 (decompose problems and subproblems into parts).
- tool.json: driver "students", minutes "20-35", modes ["Tickets", "Open kitchen"], grades_label "Grades 6-8". Kit starter.

## Screens and modes
Header (kit): "Code Kitchen", small line "Cook with code". Mode buttons: **Tickets** (opens first, level 1), **Open kitchen**. Motion, Sound, Read.

Focus (Tickets and Open kitchen): the recipe card, the biggest thing, center-left; while Cook runs, the highlighted line on it and the station beside it, which shows what that line just did.

Stage, laid out at real pixel size per window:
1. **Ticket rail** (top strip): paper tickets (code: text on a cream card) on a steel rail, one per order: table number, items as small icons (the food cutouts, shrunk) with numbers, a "TO GO" stamp and the label text when to go. A served ticket gets a ✓ stamp; a wrong plate gets a ✗ and the reason.
2. **Recipe card** (left, about 50 percent): the code on a lined index card, monospace, line numbers, at least 17 px at 1366x768. Lines are made of tiles; each value slot shows its type by shape: number in a round chip, text in a tag chip with quotes, True/False in a pill. A `def` line holds an indented body with a thin guide.
3. **Station** (right): the painted griddle, toaster and plate at the pass (art: kitchen kit) over the faded diner-pass backdrop; cooked food appears as painted cutouts (eggs on the griddle, pancakes stacking one cutout per pancake, toppings on top, toast popping, the plate or a to-go box sliding to the pass). Below it the **Jars** shelf: one painted glass canister cutout per variable, its current value drawn in code as a chip in its type shape on the jar. While a procedure runs, its parameters appear as jars inside a small card frame that disappears when it returns.

Panel (kit `aside`):
- `#hint`.
- **Cook** (big, `.gold`), **Step**, **Stop**, **Undo**, **Restart level**.
- **Add a line** drawer: `name = value`, `def name(blanks):`, and every built-in and every procedure on the card as a call. New lines go under the selected line.
- **Pantry** tray (fills the selected slot): number keypad 0 to 12, text tiles (the four toppings, " eggs", " pancakes", "Classic"), **True**, **False**, the variables and parameters in scope, `str( )`, and `+`. A slot can also be typed into: digits make a number, quotes make text, `True`/`False`, or a name.
- Line tools for the selected line: **Move up**, **Move down**, **Indent** / **Outdent** (into or out of a `def`), **Delete**.
- Edits counter (after a menu change): "Edits since the change: 2 (par 1)".
- Level strip: 12 dots in four labeled sets (A "Jars", B "Recipe cards", C "Blanks", D "Menu changes"); a dot fills when served, gets a ring when par was met. All levels open.

Open kitchen panel: the same, plus **New ticket** (table 1 to 12, eggs 0 to 6, pancakes 0 to 8, toppings, toast 0 to 4, To go, a label up to 24 characters), **Clear card**, **Clear saved**.

## Content

The card's language (this tool's own, written like Python):
- Values: whole numbers, text in quotes, `True` and `False`. `name = value` stores a value. `a + b`: two numbers add; two texts join ("3" + "2" is "32"); a number and a text stop with "Can't add a number and text." `str(x)` turns a number into text.
- `def name(blank, blank):` defines a procedure; its indented lines run when it is called, with each blank holding the value passed in. Blanks exist only inside the call.
- Built-ins (the kitchen): `crack_eggs(count)` number 1 to 6; `pour_pancakes(count)` number 1 to 8; `add_topping(name)` text, one of "syrup", "butter", "berries", "banana"; `toast(slices)` number 1 to 4; `label(words)` text, up to 24 characters; `serve(table, to_go)` number 1 to 12 and True/False, sends the plate and clears the station.
- Errors stop the cook on that line, in plain words: "pour_pancakes needs a number. stack holds the text "32"." / "serve needs True or False. It got the text "no"." / "We don't have "bluberries"." / "No jar named stak." / "Can't add a number and text."
- A plate matches its ticket when eggs, pancakes, toast, the set of toppings and to go all match, and for to go the label matches exactly. A dine-in plate's label is ignored. A plate for a table with no ticket: "Table 9 didn't order that."
- An edit is one slot changed, one line added, deleted or moved.

Levels (starter code uses `;` here for line breaks; on the card each is its own line):
- **A1 Numbers.** Ticket: T3, 4 pancakes, syrup. Starter: `stack = "4"; pour_pancakes(stack); add_topping("syrup"); serve(3, False)`. Stops on line 2. Fix: `stack = 4`.
- **A2 Joining.** Ticket: T7 to go, 5 pancakes, label "5 pancakes". Starter: `small = "3"; extra = "2"; stack = small + extra; pour_pancakes(stack); label(stack + " pancakes"); serve(7, True)`. First stop: stack holds "32". After numbers: "Can't add a number and text." on the label line. Fix: `label(str(stack) + " pancakes")` (or the text "5 pancakes").
- **A3 True or False.** Tickets: T5, 1 toast; T6 to go, 1 toast, label "toast". Starter: `to_go = "no"; toast(1); serve(5, to_go); to_go = "yes"; toast(1); label("toast"); serve(6, to_go)`. Fix: False and True.
- **B4 Same plate twice.** Tickets: T1 and T2, each the Classic (2 eggs, 3 pancakes, butter). Starter: the Classic written out with `serve(1, False)`. Change: "The Classic now has 4 pancakes." Par 1 (a `def classic():` called twice).
- **B5 Three tables.** Tickets: T4, T5, T6, the Classic. Starter: `def classic():` with its body, then `classic(); serve(4, False)`. Change: "The Classic gets berries instead of butter." Par 1.
- **B6 A card inside a card.** Tickets: T3 Eggs and toast (2 eggs, 2 toast); T4 Big breakfast (2 eggs, 2 toast, 4 pancakes, syrup). Starter: both written out flat. Change: "Toast is 1 slice on every plate." Par 1 (`big_breakfast()` calls `eggs_and_toast()`).
- **C7 One blank.** Tickets: T1 2 pancakes, T2 5 pancakes, T3 3 pancakes, all syrup. Starter: `def stack(size):` with `pour_pancakes(size); add_topping("syrup")`, then `stack(2); serve(1, False)`. Change: "Stacks get butter, not syrup." Par 1.
- **C8 Two blanks.** Tickets: T5 3 pancakes berries; T6 4 pancakes banana; T7 2 pancakes syrup. Starter: C7's `stack(size)` with syrup fixed. Change: "Every stack gets 1 extra pancake." Par 1 (`pour_pancakes(size + 1)`).
- **C9 A yes-or-no blank.** Tickets: T8 Classic; T9 to go Classic, label "Classic"; T10 to go Classic, label "Classic". Starter: `def classic():` and three plain calls with serves. Change: "To-go labels now read "Classic, thanks!"" Par 1 (`def order(table, to_go):` that cooks, labels and serves).
- **D10 Copy and paste.** Tickets: T1 to T5, each a Short stack (3 pancakes, syrup). Starter: all five written out flat (15 lines: pour, topping and serve for each table), already correct. Change 1: "Short stacks are 2 pancakes now." Change 2 (after serving change 1): "Short stacks get berries instead of syrup." Par 1 for change 2 only (refactor after change 1 pays off).
- **D11 Order slips.** Tickets: T1 3 pancakes berries; T2 to go, 2 eggs and 1 toast, label "eggs"; T3 to go, 4 pancakes banana, label "4 pancakes"; T4 2 eggs and 1 toast; T5 to go, 3 pancakes berries, label "3 pancakes". Starter: an empty card. Change: "Egg plates get 2 toast." Par 1.
- **D12 Two changes.** Tickets: T1 to T3 Short stack (3 pancakes, syrup); T4 to T6 Egg plate (2 eggs, 1 toast). Starter: correct, with stacks as a procedure and egg plates copied three times. Change 1: "Egg plates get 3 eggs." Change 2: "Short stacks get banana on top of the syrup." Par 1 each.

Open kitchen: an empty card and no tickets until New ticket; up to 8 tickets. The card and tickets are saved on this device (localStorage `curio-code-kitchen-open`); level dots too (`curio-code-kitchen`), all in try/catch. Clear saved asks first.

## Interactions in detail
- Cook runs line by line at 350 ms per kitchen action (eggs crack onto the griddle, pancakes drop onto the stack, toppings land, toast pops, the plate slides to the pass); assignments update a jar with a short drop. Step runs one line. Stop halts and clears the station. Any edit stops a run.
- Controls stay live while Cook runs: tapping a slot or line stops the run at once and selects it; Step pauses on the next line; Stop clears at once; a level dot or mode button stops and switches at once. The longest level run (D10, 15 kitchen lines) takes about 5 s; a 40-line Open kitchen card at most 14 s.
- After Cook, every plate is checked against the rail. All matched: the level dot fills; from B4 on the Manager's note slides over the rail with the change, tickets update, the edits counter starts at 0. Cook again; when all match, the counter freezes and shows par. Missing par shows "Restart level to try a reuse plan" (no penalty).
- Typing "3" with quotes into a number slot is allowed on purpose: the slot shows a tag chip, and the error comes at Cook.
- Undo keeps 40 steps and also undoes the edits counter. Restart level puts back the starter and the first menu.
- Extremes: 40 lines per card; a procedure that calls itself stops after 20 nested calls ("This recipe calls itself forever."); a value over a built-in's range stops with its range ("pour_pancakes takes 1 to 8."). A stack of 8 pancakes still fits the station: each pancake cutout overlaps the one below by 70 percent.
- Motion off: no slides or drops; the station jumps to each state at the same timing.
- Sizes: at 1366x768 the rail, card, station and Cook are on screen; under about 900 px tall the jars shelf shrinks to one row and the Pantry becomes a pop-over from the selected slot. At 760 wide the panel goes below with Cook first. At 375 wide the station folds into a strip of plate icons above the card; slots stay 44 px.
- Keyboard: Tab order is mode buttons, header, Cook, Step, panel tools, then the card's lines and slots; Enter edits a slot; Alt+Up and Alt+Down move a line; Ctrl+Z undoes.
- `window.__tool = {state, setLevel(n), card(), setCard(json), cook(), edits()}` for tests.

## Look
- Accent `--brand #9a4a12` (copper, like the pans; header and Cook). Band 6-8, own light `:root`: a diner kitchen in cream tile and copper, the code on a lined recipe card.
- `--paper #fbf3e4`, `--panel #fffaf1`, `--ink #2b1d14`, `--muted #6b5545`, `--line #e7d6bd`, `--btn #2b1d14`, `--head-ink #ffffff`, `--focus #1d4ed8`. Card `#fffdf7` with a red top rule and blue lines.
- Painted station in the diner-pass style (warm painterly, cream tile and copper, soft morning light); the backdrop stays faded to about 25 percent so the cutouts and the card read first.
- Type chips: number round, `#dbeafe` with `#1e3a8a`; text tag with quotes, `#fde68a` with `#78350f`; True/False pill, `#dcfce7` with `#14532d`. Shape carries the type, color only helps. Errors `#b91c1c` with a ✗ and words.
- Contrast (computed): white on brand 6.25:1; brand on paper 5.66:1; ink on paper 14.78:1; muted on paper 6.33:1; ink on card 16.02:1; number chip 8.49:1; text chip 7.28:1; boolean chip 8.30:1; error red on card 6.36:1; focus blue on paper 6.08:1. All pass AA.
- Neighbors: chore-flowcharts deep cyan whiteboard (gouache home scenes), code-tracer dark slate editor, model-mechanic dark lime, packet-race signal red. A filled dot and a par ring; no confetti.

## Art
Local FLUX (`scripts/localart.py`), none with people. One style: warm painterly diner illustration, cream tile and copper, soft morning light (the house style in `art/prompts.json`).
- diner-pass (made, pending review): "A warm diner kitchen pass-through window with a steel ticket rail holding blank plain paper tickets, a cream tile wall, copper pans hanging, soft morning light, an empty clean counter"; 16:9; cutout no; people no; faded (about 25 percent) behind the station and rail.
- Kitchen kit (13 pieces, each "..., warm painterly diner illustration, plain white background"; 1:1; cutout yes; people no). Sizing rule: every piece is scaled against the griddle's width (the share in brackets). griddle "a flat steel diner griddle with copper trim, seen from slightly above" (100%); toaster "a chrome two-slot diner toaster" (35%); plate "an empty round white diner plate" (45%); to-go-box "an open plain brown paper takeout box" (45%); fried-egg "a single fried egg, sunny side up" (14%); pancake "a single golden pancake seen from the side at a slight angle" (30%); toast "a single slice of golden toast" (16%); syrup "a glossy pool of maple syrup dripping over the edge" (30%); butter "a square pat of butter, slightly melting" (8%); berries "a small heap of blueberries and raspberries" (14%); banana "a small fan of banana slices" (14%); jar "a tall empty glass canister with a copper lid" (18%); ticket-rail "a short steel ticket rail with small clips" (full rail width, stretched in x only).
- The ticket text, the recipe card, chips, the jars' values, the Manager's note and preview.svg (a recipe card beside a plate with a pancake stack) are drawn in code: they are code, text and labels.

## Voice
Bank voice `easy-coach` (Umbriel), "Say in an easy-going, encouraging way, like a relaxed sports coach", here the head cook during a calm rush. Not used by any group sibling or CS neighbor (algorithm-audit calm-professor, chore-flowcharts friendly-dad, misleading-charts news-reader, model-mechanic science-narrator, packet-race firm-captain). Code, errors and tickets are on screen only. `Curio.voice`, `scope: () => state.mode`.
- w-tickets (how, Tickets welcome; stale when a slot is selected or Cook pressed): "Orders are on the rail. Tap a slot on the recipe card to fix it, then press Cook."
- slot (how, first slot selected; stale when the slot is filled): "Pick a value from the pantry, or type one. Quotes make it text."
- stopped (event, Cook stops on an error; stale on the next edit): "The cook stopped. Read the red note on that line, fix it, then press Cook."
- served (event, all plates match; stale on the next edit or level change): "Every order's out."
- change (event, a menu change arrives; stale on the next Cook): "The menu just changed. Update your card, then press Cook again."
- par (event, par met; stale on the next level): "One change did it. That's what a procedure buys you."
- over (how, first time par is missed; stale on Restart level or the next level): "That took a lot of edits. Press Restart level and try a procedure, so the change is in one place."
- blank (how, first level in set C opens; stale on the first Cook): "A blank holds whatever you pass in, only while that recipe runs."
- w-open (how, Open kitchen welcome; stale on New ticket): "Press New ticket to write an order, then write the card and press Cook."

## Family engine
none

## Sources
- CSTA 2026 ids MS-PRO-VD-16, MS-PRO-PD-12, MS-PRO-RD-17 (`data/standards/csta-2026-ids.txt`); CSTA K-12 CS Standards (2017) 2-AP-11, 2-AP-13, 2-AP-14: https://csteachers.org/k12standards/
- Python value types, joining text with + ("3" + "2" gives "32"), `str()`: The Python Tutorial, "An Informal Introduction to Python", https://docs.python.org/3/tutorial/introduction.html ; Built-in Functions, `str`, https://docs.python.org/3/library/functions.html
- Adding a number and text raises TypeError in Python: Built-in Exceptions, TypeError, https://docs.python.org/3/library/exceptions.html#TypeError
- `def`, parameters and local names inside a function: The Python Tutorial, "Defining Functions", https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Procedures reduce the places a change must be made: Harold Abelson and Gerald Jay Sussman, Structure and Interpretation of Computer Programs, 2nd ed., section 1.1.8 (procedures as black-box abstractions), https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book-Z-H-10.html
- Menu items, tickets, levels, pars and the language's kitchen built-ins are original to Curio Class.
- Checks run (Python, 2026-10-29): "3" + "2" gives "32" and 3 + "2" raises TypeError, as the tool's errors say; str(5) + " pancakes" is "5 pancakes" (10 characters); every to-go label fits 24 characters ("Classic, thanks!" is 16). Edit counts walked by hand for every change: B4 1 with a procedure, 2 copied; D10 change 2: 1 after a refactor, 5 left copied; D12 change 1: 1 with an egg procedure, 3 copied. D10's starter is 15 lines (three per table), not the 20 the old spec said; fixed. Every ticket stays inside the built-in ranges after its change (the largest stack after the C8 change is 4 + 1 = 5 of 8).

## Done when
1. A1 stops on line 2 with the number message; after `stack = 4` T3 is served.
2. A2 shows "32" in the stack jar and stops; with numbers it stops on the label line; with `str(stack)` the label reads "5 pancakes" and T7 matches.
3. A3 stops on serve with the True or False message; with False and True both tickets match.
4. B4: with `def classic()` called twice, the change needs 1 edit and the dot gets its ring; with the plate copied, 2 edits and no ring.
5. C8: `pour_pancakes(size + 1)` passes the change in 1 edit; parameters show as jars inside the call frame and vanish after.
6. D10: change 2 counts 1 edit when the stacks were refactored after change 1, 5 when left copied.
7. Errors: a misspelled topping, an unknown name, a range overflow and a self-calling recipe each stop with their message.
8. Open kitchen: a new ticket and the card survive a reload; Clear saved empties both after a Yes.
9. Every size in STANDARDS.md: Cook, the rail and the selected line visible without page scrolling; slots 44 px.
10. Voice: welcome once per mode, how lines once then hint only, stopped and change each time while fresh; Read speaks the hint; console clean; no network requests; the name only as "Curio Class".
11. Focus: at 1366x768 and 1000x625 the recipe card is the largest thing on the stage, and during Cook the running line is highlighted while the station shows its painted result.
12. Tap while it plays: during Cook, tapping a slot stops the run and selects the slot at once, and Stop clears the station at once; the plates on the station always match the lines run so far.

## Open questions
- [code-kitchen] Thirteen new painted cutouts (the station and food kit) beside the existing diner-pass backdrop, none with people. OK?
