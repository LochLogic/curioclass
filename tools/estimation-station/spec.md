# Estimation Station

## One idea
A freight train unloads real things at Mr. Hollis's station: you guess each one's length, then pick the tool that can really do the job (a stick for things that stand up, the bendy tape for curvy things, the right units), line its zero up and read it yourself, and your points push your train along the track against a ghost of your last run; on the order slips the same tape turns into a number line you add and subtract on.

## Not like
- paperclip-ruler (grade 1): counts same-size non-standard units (paperclips, shoes) with no gaps. Here the units are standard (inches, feet, centimeters, meters), the tool choice is the decision, and every measure is guessed first.
- jump-line (grade 2): an open, unmarked number line where the child draws jumps of any size for sums to 1000. Here the line is a marked tape measure, the numbers are lengths in a story, and the child lays ribbon pieces on it (end to end or side by side) instead of drawing jumps.
- lunch-line-data (grade 2): measures carrots to build a line plot. Here nothing is graphed; the measure is checked against a guess and a tool choice.
- kitchen-lab (grade 3): mass, liquid volume and elapsed time. Here length only.
- bus-stop (grade K): a counters-and-cards story ride. Here there are no cards to pick; every answer is a typed number read off a tool.

## Who and how
- Grade 2, math, module "Rulers and Units" (math-2-rulers-and-units). Standards: 2.MD.A (2.MD.1, 2.MD.2, 2.MD.3, 2.MD.4) and 2.MD.B (2.MD.5, 2.MD.6).
- Driver: teacher on a projector (tool.json `driver: "teacher"`): the class calls out guesses and readings, a child or the teacher taps. Every question and step is spoken and every choice is a picture or a numeral, so a child alone at home can play (BASELINE rule 4).
- Minutes: one Freight run (8 jobs) 12 to 18; Yard 5 or more. Race format: no clock; you race your own last run.
- No personal prompts. The last run and best run are kept in localStorage (`estimation-station-runs`), and the end screen says "Your runs are saved only on this device." (BASELINE rule 7).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 2.MD.1 select and use rulers, yardsticks, meter sticks, tapes | Picks a tool from the rack for each crate (a rigid stick fails on curvy things, the tape flops on standing things, a tool without the asked unit greys); drags it so its zero line sits at the item's end; reads the far end and types it | Five painted-look tools drawn in code to scale with real tick marks; Start and End lenses; the stamp on each crate card | 3, 4 |
| 2.MD.2 measure twice in two units, relate to unit size | On the two-unit crate measures in feet (or meters, inches, centimeters), guesses the other unit, measures again | Big jump arcs for the big unit above, small ticks for the small unit below, both numbers side by side | 5 |
| 2.MD.3 estimate in inches, feet, centimeters, meters | Types a guess before any tool appears, every crate; uses the one-unit square beside the item and the Measured shelf of things already measured | The guess and the real length on the crate card, with 0 to 3 stars | 2 |
| 2.MD.4 how much longer | On the ribbon crate lines one tool along two ribbons that share a start, reads both, types the difference | After a right answer, a jump arc on the tool from the short ribbon's end to the long one's, labeled with the difference | 6 |
| 2.MD.5 length word problems within 100, equation with a symbol for the unknown | Hears an order slip, lays the second piece on the tape where the story says, sees the number sentence their layout makes with a box for the unknown, types the box | The slip text, the pieces on the tape, the equation with a box, then the box filled | 7 |
| 2.MD.6 lengths from 0 on a number line; sums and differences on it | Lays pieces from 0 (side by side) or end to end on the 0 to 100 tape, and reads the answer as a point or a gap on it | The tape with 101 equally spaced ticks, numbers every 10, pieces as bars from 0 | 7 |

## Screens and modes
Header (kit): title "Estimation Station", mode buttons (`.seg`, icon plus word, 60 px tall): `Freight` (train icon, default), `Yard` (toolbox icon); then `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at the 680x425 preview) and carries an icon and a word.

**On load and first tap.** Freight opens with the painted platform, the train already stopped, crate 1 open and its item lying on the work table beside the one-unit square; the number pad is live. Nothing speaks before the first tap (kit). First hint: "Freight is here! Guess how long the {item} is, in {unit}. Tap the numbers, then tap Check." The first tap on a number key types that digit at once and plays nothing of its own, so the kit queues the welcome after it (the welcome then runs into the crate line). The welcome may be cut (BASELINE 16); the premise (guess first, then measure) also lives in the hint, in Read and in the crate line.

**Freight.** Focus: the work table with the item and, once picked, the tool lying along it. Layout at 1366x768 (stage about 1036 x 704, panel 330 px, all above the fold):
- Race strip (top, 84 px): two code-drawn tracks with 44 ties. Upper: "This run" with the painted engine and cars cutout. Lower: "Last run" with the same train drawn grey with a dashed outline (word label in ink, so color is not the only signal). Crate dots under the tracks show which job (1 to 8) is on.
- Work table (middle, about 440 px tall): a painted wood tabletop strip for lying and curvy items; for standing items the table swaps to a painted platform floor with a wall behind, and the item stands on the floor line. The item is drawn at a scale picked at random per crate so the item fills 55 to 80 percent of the width (or height), so its size on screen says nothing by itself; the one-unit square (code, 1 unit at that scale, labeled "1 inch" or "1 centimeter"; for feet and meter crates a code silhouette of 1 foot or 1 meter) sits at the table's left end during the guess. The crate card sits at top right of the table: item name, the asked unit, then the guess, the stamp and the measure as they come.
- Bottom row (120 px): the tool rack left (five tiles 120 x 96, each a picture of the tool and its word: `Inch ruler`, `Centimeter ruler`, `Yardstick`, `Meter stick`, `Tape`), the Measured shelf right (thumbnails of items measured this run with their lengths, up to 7, one row).
- Tool controls, shown only when a tool is on the table, under its right end: `Nudge left` and `Nudge right` (arrow icons, move the tool a quarter unit), `Flip` (tape only, turn-over icon: inches side or centimeters side), `Mark and move` (chalk icon, only while the item runs past the tool's end).
- Panel: Mr. Hollis portrait (painted cutout, 120 px, three poses) beside the hint (22 px), then the number pad (display 64 px showing the typed number and the unit word, keys `1` to `9`, `0`, `Back`, and `Check` in gold, keys 64 px), then `Next crate` (gold, train icon, shown after a job ends) and `New run` (circular arrow).
- At 680x425: header 44 px, panel 210 px wide, portrait 48 px beside the hint, number pad keys 44 px in a 4 x 3 grid with Back and Check in the bottom row; the race strip shrinks to 40 px; the Measured shelf folds to the last 3 items; tool tiles 64 x 56 with icons and short words. Scene text stays 10 px or more.

Each job runs in steps; the hint always names the step's action and control: guess (number pad, Check), tool (a rack tile), measure (drag the tool, then the number pad and Check), result (`Next crate`).

The eight jobs of a run (jobs 1 to 5 shuffled per run; 6 to 8 always last, because 7 and 8 use the tape as a number line):
1. Inch crate (lying). 2. Centimeter crate (lying). 3. Curvy crate. 4. Standing crate. 5. Two-unit crate. 6. Ribbon crate (how much longer). 7 and 8. Order slips.

What the picture shows: a right measure, the item drops into its crate, the crate card gets its numbers and stars, the crate rides onto the train and the train moves forward by the job's points (the ghost moves by its stored points for the same job); a wrong measure, the Start lens and End lens pulse; the end of the run, the loaded train pulls out past the ghost (or behind it), and the end screen shows all 8 crate cards in a row, the total beside last run and best run, and a `Tool sense` badge when every tool stamp was earned. Buttons: `New run`, `Yard`.

Order slips (jobs 7, 8): the work table becomes the tape line: the cloth tape pulled straight across the stage, 0 to 100 (inches or centimeters as the slip says), a tick every unit, a longer tick every 5, numbers every 10, about 9 px a unit at 1366 wide. Piece A (a code bar with its length written on it) is already laid from 0. Piece B waits above the tape. The slip card (paper, top left) shows the story and, after B is placed, the equation with a box.

**Yard.** Focus: the same work table, no race strip, no stars. A shelf of every item (paged, 12 tiles a page, `Next page` and `Back page` arrow buttons) and the tool rack. Tap an item to put it on the table (a fresh length from its range each time), tap any tool, measure, then `Show me` (eye icon) shows the true length on the crate card. `Flip` and `Mark and move` work as in Freight. Nothing is saved. At 680x425 the item shelf shows 6 tiles a page.

## Content
**Tools** (code drawn, true proportion; ticks and numbers rendered crisp at every zoom):
- Inch ruler: 12 in, rigid; zero line inset a quarter inch from its left edge; numbers 1 to 12. Reads inches; feet by moves (it is 1 foot).
- Centimeter ruler: 30 cm, rigid; zero inset half a centimeter; numbers every centimeter.
- Yardstick: 36 in, rigid; zero at its end; numbers every inch; bold foot marks at 12, 24, 36 with "1 ft", "2 ft", "3 ft". Reads inches and feet.
- Meter stick: 100 cm, rigid; zero at its end; numbers every 10, a long tick every 5. Reads centimeters; meters by moves (it is 1 meter).
- Tape (the station's cloth tape): 60 in on one side with foot marks, 150 cm on the other; bends; flops when stood up; zero at the metal tip. Reads inches, feet, centimeters.

**Tool rule** (the stamp): a tool works if it reads the asked unit, bends for a curvy item, and stands for a standing item. Moves = length divided by the tool's length in that unit, rounded up. The stamp goes to the first tool picked if it is among the working tools with the fewest moves (ties all count). Computed stamps (check.py): inch crates: Inch ruler, Yardstick, Tape; centimeter crates: Centimeter ruler, Meter stick, Tape; curvy: Tape only; standing in inches: Yardstick only; standing in centimeters: Meter stick only (mailbox post too, at 2 moves).

**Crate pool** (length per run drawn as a whole number in the range; the drawn item is within 0.15 unit of that whole number, never past the tape's end, so the nearest whole is never in doubt; no item repeats within a run or from the last run when another is left):
- Inch, lying: paperclip 1 to 2, toy car 2 to 4, crayon 3 to 4, pencil 4 to 7, spoon 5 to 7, comb 5 to 8, paintbrush 7 to 9, picture book 9 to 11, keyboard 11 to 12.
- Centimeter, lying: bead 1 to 2, eraser 4 to 7, leaf 6 to 12, chalk 7 to 9, glue stick 9 to 12, scissors 13 to 18, feather 15 to 25, banana 16 to 22, notebook 25 to 29.
- Curvy (code path, tape only): toy snake in 20 to 34, shoelace in 27 to 45, jump rope in 40 to 58, bead necklace cm 40 to 70, ribbon cm 60 to 140, garden hose cm 110 to 150.
- Standing: suitcase in 18 to 30, small table in 24 to 30, chair in 30 to 34, broom in 48 to 58, crate stack cm 40 to 95, lamp cm 45 to 80, sunflower in a pot cm 60 to 99, mailbox post cm 100 to 130.
- Two-unit (whole units so both readings are exact): rug, lying, feet then inches, 4 to 8 ft (48 to 96 in); bench, lying, inches then feet, 36 to 96 in (3 to 8 ft); door, standing, meters then centimeters, 2 m (200 cm); ladder, standing, centimeters then meters, 100, 200 or 300 cm.
- Ribbon pairs (red striped ribbon longer, blue dotted ribbon shorter, sharing a start line): inches 29 and 17, 33 and 24, 35 and 19; centimeters 86 and 58, 72 and 45, 94 and 67.
- Order slips (A is laid, B is placed; answer):
  - Join: "Mia's ribbon is 25 inches. Leo's is 38 inches. They tie them end to end. How long is the new ribbon?" 63. "A green rope is 47 centimeters and a red rope is 36 centimeters. They tie them together. How long is the rope now?" 83. "A train track piece is 19 inches. Ben adds a 44 inch piece. How long is the track?" 63. "A paper chain is 58 centimeters. Ana adds 29 centimeters more. How long is it now?" 87. "Two scarves are 36 inches each. Sewn end to end, how long are they?" 72. "A fence board is 27 centimeters. Another is 45 centimeters. Laid end to end, how long?" 72.
  - Take from: "A rope is 80 centimeters. Gus cuts off 25 centimeters. How long is the rope now?" 55. "A garden hose is 64 inches. Mr. Hollis cuts off 18 inches. How long is it now?" 46. "A ribbon is 91 centimeters. Sam uses 46 centimeters for a bow. How much is left?" 45.
  - Compare: "The rope is 52 inches. The toy snake is 34 inches. How much longer is the rope?" 18. "A scarf is 75 centimeters. A belt is 48 centimeters. How much longer is the scarf?" 27. "A bench is 61 inches. A suitcase is 27 inches. How much longer is the bench?" 34.
  - Missing part: "Ana has 45 centimeters of ribbon. She needs 70 centimeters for a bow. How much more does she need?" 25. "Leo's tower is 38 inches tall. He wants it 60 inches tall. How many more inches?" 22. "A chain is 29 centimeters. It must reach 83 centimeters. How much more chain is needed?" 54.
  Each slip of a run is drawn independently from all 15 (no repeat within a run), so join and subtract kinds mix by chance.
- Placements on the tape line: B snaps to whole ticks. End to end means B starts at A's end; side by side means B starts at 0 under A; for take-from, the cut piece may also be laid over A's last part ending at A's end. The equation shown follows the placement: end to end "A + B = box"; side by side with B longer "A + box = B"; side by side with B shorter "A - B = box"; cut piece over A's end "A - B = box". A placement starting anywhere else springs back.

**Points** (44 a run): guess 3, 2, 1 or 0 stars (3 if off by at most 1 or 10 percent, 2 if at most 1 or 20 percent, 1 if at most 2 or 30 percent, whichever is larger); stamp 1; measure 2 on the first try, 1 on the second, 0 after. Crates 1 to 4: 6 each. Two-unit: guess 3, stamp 1, measure 2, second guess 3, second measure 2 (11). Ribbon: stamp 1, each ribbon read 1, difference 2 or 1 (5). Slips: answer 2 or 1 (2 each). First run ever: the ghost is the "Starter ghost", 4 points a job (32), labeled so.

## Interactions in detail
- Guess: the pad types up to 3 digits; Check with nothing typed does nothing and the hint stays. Check locks the guess on the crate card; the one-unit square stays, the rack lights. No tool appears before Check.
- Tool pick: tap a tile (or drag it to the table). A tool that does not work plays its reason and goes back (it is not greyed, so the rack never shrinks); a wrong first pick loses the stamp, never the job. A working tool lands on the table lying parallel to the item, a little below it, its zero end 2 units left of the item's start (never lined up for the child). Standing items: the stick stands on the floor beside the item (it rests on the floor, so its zero is already at the bottom; the skill there is the choice and the reading). Curvy items: the tape tip appears at one end; the child drags the tape along the path (it follows the curve while the pointer stays within 30 px of it), and at the other end it lifts and lies straight under the item.
- Lining up: drag the tool left or right (it stays parallel), or Nudge, or arrow keys. The Start lens (a 150 px circle, 4x, at the item's start) shows the item's end and the tool's zero line together from the moment the tool lands. Once the tool stops, the End lens appears at the item's far end, 4x, showing ticks and the nearest numbers. No length is written anywhere: the child reads it.
- Mark and move: when the item runs past the tool's end, the button lights. Tapping it draws a chalk mark at the tool's end, labeled with the tool's length ("36"), and slides the tool so its zero sits on the mark. The child adds the pieces and types the total.
- Measure Check: the typed number is compared to the true whole length. Right: chime, the item drops into its crate, points move the train (1.2 s, Motion off: the train jumps on the same beat). First wrong: both lenses pulse, the line names zero and the far end; the pad clears. Second wrong: the tool slides to zero at the start, the End lens rings the number, the line says the length, 0 points.
- Two-unit: after the first measure the second guess opens with the tool still placed; Check locks it; the tool switches face (yardstick feet to inches by its numbers, tape Flip, meter stick meters to centimeters) and any chalk marks relabel. After the second measure, big arcs (one per foot or meter) draw above the item and small ticks below it, with both numbers.
- Ribbon crate: tool pick as usual (stamp), one placement along both ribbons, then "Red ribbon" Check, "Blue ribbon" Check, then "How much longer?" Check. The jump arc draws only after the difference is checked, or after the second wrong try.
- Slips: the slip line plays; B is live at once. After B lands in a meaning spot, the equation with a box appears and the pad lights. B stays draggable until the slip is solved, and the equation follows each new layout. Check compares the typed number with the story's answer, not the layout's. Right: the box fills, the gap or end on the tape glows, chime. First wrong: the line asks whether the story puts the pieces end to end or side by side. Second wrong: B moves to the right layout, the box fills and the jump draws.
- Next crate: the next job slides in (the train pulls a car forward). `New run`: asks nothing; starts job 1 of a new run (the run in progress is dropped and not saved). A run is saved as "last run" at its end, and as "best run" if higher.
- A tap always acts at once: the train's ride, the drop and the arcs never block the pad, the rack or Next crate; a tap during the right line does not cut the line unless it starts a new line.
- Mode switch hushes speech; Freight keeps its run; Yard keeps its item.
- Resizing mid-drag keeps the tool's position in item units.

## Look
- Accent `--brand` #9c3520 freight-car red (header, mode buttons, track ties); gold #e8a917 for Check and Next crate; paper #f7f2e7; ink #231f1a; muted #5e574d; tape yellow #f2c230; wood sticks #e2c48a; table #c9b48e; jump arcs #1f6f8b; ghost train #7c8a99 (non-text only). Different from bus-stop navy #2b4c7e and roller-coaster-rounding teal #0d6f7a.
- Contrast (WCAG 2.1, computed): white on brand 7.13:1; brand on paper 6.39:1; ink on paper 14.67:1; muted on paper 6.38:1; ink on gold 7.89:1; ink on tape 9.77:1; ink on wood 9.74:1; ink on table 8.11:1; white on jump blue 5.67:1; jump blue on paper 5.08:1; ghost grey on paper 3.16:1 (non-text, over 3:1; its label is ink).
- Ribbons: red with white stripes and blue with white dots, so they differ without color.

## Art
One style: warm painted children's picture book, small-town station in late-afternoon light. People go to Gemini with `people: true`; everything else may use local FLUX. Each item is trimmed so the object touches the left and right edges of its image (its ends are the image ends), shown at its crate's length. Text on signs stays in code over blank surfaces.
- station-platform: "A small-town railway platform with a wooden canopy, a blank station sign, brick wall, late-afternoon light"; 16:9; cutout no; people no; Freight and Yard backdrop.
- engine and freight-car: "A small red steam-style freight engine, side view facing right" and "an open red freight car holding wooden crates, side view"; 4:1 each; cutout yes; people no; race strip (the ghost train is the same art greyed in code) and the arrival.
- tabletop: "Warm wooden workbench top seen from above, full frame"; 5:1; cutout no; people no; lying crates.
- platform-floor: "Wooden platform floor and a plain cream station wall, front view"; 16:9; cutout no; people no; standing crates.
- 18 lying items (cutout yes, people no, seen from above on a plain background): paperclip, toy car, crayon, pencil, spoon, comb, paintbrush, picture book with a blank cover, computer keyboard, glass bead, pink eraser, green leaf, white chalk stick, glue stick, scissors, feather, banana, spiral notebook with a blank cover. Aspects by shape: 5:1 for pencil, paintbrush, crayon, chalk, glue stick, comb, feather; 4:1 for spoon, scissors, banana, keyboard, paperclip; 16:9 toy car; 4:3 picture book, notebook, eraser; 1:1 bead, leaf.
- 8 standing items (cutout yes, people no, front view, base on the bottom edge): suitcase 3:4, small table 4:3, chair 3:4, broom 9:16, crate stack 9:16, lamp 9:16, sunflower in a pot 9:16, mailbox on a post 9:16.
- Two-unit items: woven rug seen from above 4:1; wooden bench side view 5:1; wooden door in a frame 9:16; wooden ladder standing 9:16; all cutout yes, people no.
- Curvy item parts (cutout yes, 1:1): snake toy head, jump rope handle, garden hose nozzle; textures (cutout no, 4:1, full frame): braided rope, green hose, shoelace weave. The curves are code paths stroked with these textures.
- mr-hollis, three poses (talking, pointing at the table, cheering with his cap raised), 1:1, cutout yes, people yes: "a friendly older Black station master with a gray beard, navy conductor cap and vest, head and shoulders". Panel portrait; the pose follows his lines.
41 images plus Mr. Hollis's 3 poses; 3 with people (contact sheet and the fresh representation check, BASELINE 11). Drawn in code: all tools and ticks, lenses, the one-unit square, curves, ribbons, tape line, pieces, arcs, the race strip, crate cards, pad, shelf.

## Voice
Bank voice `gravel-ranger` (Algenib): he is Mr. Hollis. Style line: "Say warmly with a gravelly voice, like an old station master telling a child how a job is done." Different from marching-band (firm-captain, Alnilam), corner-store (Achird) and bus-stop (bright-teacher). `Curio.voice` with `scope: () => state.mode + ':' + state.job + ':' + state.step`. Numbers are spoken as words; templates in braces are expanded by the builder over Content, every expansion in lines.json, with "1 inch", "1 foot", "1 meter", "1 centimeter" singulars.

Freight:
- how `welcome` (stale when a job's guess is checked): "Hello there, I'm Mr. Hollis, the station master. Freight's in! We guess first, then we measure."
- event, whole, `crate` (job opens): "Crate {n}! A {item}. How long is it, in {unit}?"
- how `guessHow` (first guess only; stale on Check): "Guess first. The little square is one {unit}. Tap the numbers, then tap Check."
- event `guessed` (each Check of a guess): "You guessed {e} {unit}. Now tap a tool on the rack."
- event `noUnit`: "The {tool} shows {toolUnits}. This crate needs {unit}. Tap another tool."
- event `noBend`: "A stick can't bend around the {item}. Tap a tool that bends."
- event `flop`: "The tape flops over. Tap a tool that stands up."
- event `toolOk` (lying): "The {tool}. Drag it so the zero line sits at the end of the {item}." (standing): "The {tool}. Read the number at the top." (curvy): "The tape. Drag it along the {item}, end to end."
- how `readHow` (first time a tool is still for 1 s; stale when a number is typed): "Look in the end circle. Type the number you read, then tap Check."
- how `markHow` (first time Mark and move lights): "The {item} is longer than the {tool}. Tap Mark and move, then add up the pieces."
- event, whole, `right`: "Yes, {L} {unit}. You guessed {e}. {s} stars!" (s = zero: "Yes, {L} {unit}. You guessed {e}. Keep guessing, you'll get closer.")
- event `wrong1`: "Not quite. Look at the zero, and look where the {item} ends. Try again."
- event, whole, `wrong2`: "It's {L} {unit}. The {item} ends at {L}."
- how `nextHow` (first result only; stale when Next crate is tapped): "Tap Next crate."
- Two-unit: event, whole, `second`: "{L1} {unit1}. Now guess: how many {unit2} long is it? Tap the numbers, then Check." event `secondMeasure`: "Now read it in {unit2}." event, whole, `relate`: "{L1} {unit1} is {L2} {unit2}. {Big} are bigger, so it takes fewer of them."
- Ribbon: event, whole, `ribbonCrate`: "Two ribbons! How much longer is the red one? Tap a tool first." event `readRed`: "Read the red striped ribbon, then tap Check." event `readBlue`: "Now the blue dotted ribbon." event `askDiff`: "How much longer is the red ribbon? Tap the numbers, then Check." event, whole, `diffRight`: "Yes! {a} take away {b} is {d}. The red ribbon is {d} {unit} longer." event `diffWrong1`: "Not quite. Count the spaces from the end of the blue ribbon to the end of the red one. Then tap Check." event, whole, `diffWrong2`: "It's {d}. {a} take away {b} is {d}."
- Slips: event, whole, `slip`: "Order slip! " + the slip text. how `placeHow` (first slip; stale when B lands): "Drag the {B} onto the tape where the story puts it." event `badSpot`: "Put it at zero, or at the end of the {A}." event `equation`: "Your number sentence: {eq}, with a box for the number we need. Type it, then tap Check." event, whole, `slipRight`: "Yes! {eqFilled}." event `slipWrong1`: "Not quite. Does the story put the pieces end to end, or side by side? Drag the {B} if you need to, then tap Check." event, whole, `slipWrong2`: "It's {ans}. {eqFilled}."
- event, whole, `end`: "The train is loaded! {P} points. Your last run had {G}." plus "You beat it!" or "Race it again next time!" then event `endHow`: "Tap New run to race your score."

Yard: how `yardWelcome` (stale when an item is tapped): "This is the yard. Tap anything on the shelf, tap any tool, and measure it. Tap Show me to check." event `showMe`: "The {item} is {L} {unit}."

Read speaks the hint, which always names the action and control of the step (never Next crate or Mark and move while hidden). Repeats: `noUnit`, `noBend`, `flop`, `badSpot` once per tool or spot per job; results every time.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Guess stars (2.MD.3) | Guessing; the same number every time; a number from the last run; reading the length off the screen; doing nothing; mashing; the common wrong answer (a centimeter number on an inch crate) | Random 1 to 100 averages 0.7 stars and the best fixed number for a whole kind averages 1.1 to 1.35 (check.py) against about 2.6 for a guess within 20 percent; lengths are drawn per run and items never repeat from the last run; no tool is on screen before Check, the drawn scale is random per crate (item fills 55 to 80 percent), so size on screen means nothing without the one-unit square (using the square is the skill); no Check means no progress; 3 digits max; unit swaps score 0. |
| Tool stamp (2.MD.1) | Always the same tool; elimination; the answer's position on the rack; trying tools until one works | The rack never shrinks and its order is fixed while the crate order is shuffled; only the first pick counts; no single tool earns the stamp on every kind (tape fails standing, sticks fail curvy, each ruler fails the other unit), and the `Tool sense` badge needs all six stamps of a run, which include a curvy and a standing crate. A tape on a short straight item does earn it: that is a right tool there, not a shortcut. |
| Measure (2.MD.1) | Reading from the tool's edge; starting at 1; counting tick marks instead of spaces; typing the guess; mashing; a readout | Edge and start-at-1 and tick counting give one more than the length and fail; the guess is right only if it was already right; no length is shown before Check; two wrong tries score 0; nothing in the scene writes the length (Measured shelf shows only past items). |
| Second unit (2.MD.2) | Typing the first number again; always a bigger number; guessing | The same number fails both guess bands and the measure; the run's two-unit crate goes big-to-small or small-to-big at random, so "always bigger" is wrong half the time and earns no guess stars then; the measure points need the reading. |
| Ribbon difference (2.MD.4) | Typing a ribbon's length; adding them; the jump arc | Both fail; the arc draws only after Check; counting ticks between the ends on the tool is the skill (2.MD.6). |
| Slip answer (2.MD.5, 2.MD.6) | Always side by side; always end to end; elimination between slips; reading the equation; reading the tape; solving the equation of a wrong layout | Kinds are drawn independently, so neither layout always works (end to end fails 9 of 15, side by side fails 6 of 15); the equation has a box, not the answer; Check judges the story's answer, so a self-consistent answer to a wrong layout fails; reading a point or gap on the tape after a right layout is the number line strategy the code asks for. |
| Race against the ghost | Doing nothing; mashing; New run until the ghost is weak | No Check, no points; mashing earns at most stars by luck; an abandoned run is never saved, so the ghost stays the last finished run. |

## Heard in order
For each step: lines in order; "waits" means the next line waits for it to finish; taps always act at once.
1. Load, first tap on a key: (digit typed) then `welcome`, then `crate` (waits for welcome), then `guessHow` (first job only). Next action spoken: "Tap the numbers, then tap Check."
2. Each later job opening: `crate` (whole), then the guess hint silently (how already heard). Next action is in `crate`'s question plus the hint.
3. Guess Check: `guessed` ("Now tap a tool on the rack"). A digit typed while `crate` plays does not cut it.
4. Tool pick: a failing tool plays `noUnit`, `noBend` or `flop` (each names the next tap); a working tool plays `toolOk`; then `readHow` (first time) after the tool is still 1 s; `markHow` first time Mark and move lights.
5. Measure Check: `right` (whole) then `nextHow` (first time); or `wrong1`; or `wrong2` (whole) then `nextHow`. Feedback always plays before Next crate's next `crate` line, which waits for it.
6. Two-unit: `right` for the first measure (whole), then `second` (waits for it); the second guess's Check plays `secondMeasure` in place of `guessed`; the second measure's Check plays `relate` (whole) or `wrong1` / `wrong2`, then `nextHow`.
7. Ribbon: `ribbonCrate` (whole), tool lines as in 4, `readRed`, Check, `readBlue`, Check, `askDiff`, Check, `diffRight` (whole) or `diffWrong1` or `diffWrong2` (whole), then `nextHow`. A wrong ribbon reading plays `wrong1` / `wrong2` with the ribbon's name.
8. Slip: `slip` (whole), `placeHow` (first slip), B lands: `equation` (again only when the layout's equation changes), Check: `slipRight` (whole) or `slipWrong1` or `slipWrong2` (whole). The next slip's `slip` waits.
9. End: `end` (whole), then `endHow`.
10. Yard: `yardWelcome`; each Show me: `showMe`.
No line contains a bare letter sound; units are spoken as words.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| 1 foot = 12 inches; 1 yard = 3 feet = 36 inches (yardstick length, foot marks at 12, 24, 36) | NIST Handbook 44, Appendix C, Units of length | NIST Special Publication 811, Appendix B | yes |
| 1 meter = 100 centimeters (meter stick length) | BIPM, The International System of Units (SI Brochure), prefixes | NIST Special Publication 330 (SI) | yes |
| 2.MD.1 to 2.MD.6 wording (tools named: rulers, yardsticks, meter sticks, measuring tapes; two units related to unit size; estimate in inches, feet, centimeters, meters; how much longer; word problems within 100 with a symbol for the unknown; number line with equally spaced points from 0) | CCSS Mathematics, Grade 2, Measurement and Data, corestandards.org/Math/Content/2/MD | Common Core Standards Writing Team (2012), Progressions: Geometric Measurement K-5, grade 2 section | yes |
| A bigger unit gives a smaller count for the same length (the inverse relation 2.MD.2 asks for) | CCSS 2.MD.2 | Progressions, Geometric Measurement K-5, grade 2 | yes |
| A ruler is a number line, and second graders use it to show sums and differences (2.MD.6) | CCSS 2.MD.6 | Progressions, Geometric Measurement K-5, grade 2 | yes |
Backed twice: 5. Cut: 2 (body benchmarks such as "a fingernail is about 1 centimeter" and a coin as "about 1 inch": replaced by the drawn one-unit square and the Measured shelf). Item lengths, the tape's 60 inches and 150 centimeters, and the slips are story values, not claims.

Checks run (Python, scratchpad check.py, est.py, more.py, 2026-11-06):
- Stamp sets for every length of every crate (listed under Tool rule); always-one-tool strategies: inch ruler and yardstick earn 0 on curvy and centimeter crates, meter stick and centimeter ruler 0 on inch and curvy, tape 0 on standing; no single tool earns all.
- Two-unit: rug and bench stamps are tape (or tape and yardstick at 36 and 72 inches); door and ladder meter stick only; second readings 36 to 96 inches, 100 to 300 centimeters.
- Guess bands chosen after trying four: random 1 to 100 earns 0.73 stars on average, always 50 earns 0.91, the best fixed number per kind 1.06 to 1.35, a guess within 20 percent 2.5 to 2.9, within 30 percent 2.0 to 2.7. (The first band set let "always 6" on inch crates average 1.85; tightened.)
- Measure wrong answers: start at 1 or counting ticks gives length + 1, which fails for every length from 1 to 150; the quarter-inch zero inset alone would not change the nearest inch, so the feedback names zero, not the edge.
- Slips: all 15 answers within 100 (18 to 87), every one regroups; join 6, take 3, compare 3, missing 3. Ribbons: differences 9 to 28.
- Run maximum 44; a careful run about 40; the no-skill strategies above about 20, below the Starter ghost's 32.
- Contrast ratios as in Look.

## Done when
1. Focus: at 1366x768 the work table with the item and tool is the biggest thing on the stage; the rack, Nudge buttons, number pad, Check and Next crate are all above the fold; at 680x425 the item, tool, pad and Check show with no scroll and text is 10 px or more.
2. Every crate asks for a guess before any tool appears, the one-unit square shows, and the crate card shows guess, length and the stars by the bands in Content (try off by 0, 1, 20 percent, 30 percent, 50 percent). (2.MD.3)
3. Tool rule: on a curvy crate every stick plays `noBend` and goes back to the rack, on a standing crate the tape flops and goes back, a tool without the unit plays `noUnit` and goes back; the rack never shrinks; the stamp follows the first pick only; Tool sense needs all six. (2.MD.1)
4. Measuring: the tool never lands lined up; the Start and End lenses show; no length is written before Check; reading from the edge or from 1 fails; Mark and move adds a chalk mark labeled with the tool's length. (2.MD.1)
5. Two-unit: both orders (big to small, small to big) play, the tool switches face, and the big arcs and small ticks draw with both numbers after the second Check. (2.MD.2)
6. Ribbon crate: one placement, two readings, the difference; the arc never shows before the difference is checked. (2.MD.4)
7. Slips: all 15 play; end to end and side by side each give their own equation with a box; a wrong layout springs back or reads a wrong number; the answer fills the box. (2.MD.5, 2.MD.6)
8. Tap while it plays: typing a digit during `crate` or tapping a tool during the train ride acts at once, and no older line plays after a newer one.
9. Pre-reader: every step's question and next action is spoken; tools, Next crate and the pieces are pictures with words; a child with Sound on finishes a run without reading.
10. Race: the ghost moves by the last finished run's job points (Starter ghost on the first run), the end screen compares, and the run is saved only at its end, with the on-device line shown.
11. Voice: five wrong Checks in a row play `wrong1` or `wrong2` each time; `guessHow`, `readHow`, `markHow`, `placeHow` play once each; no line names a hidden control.
12. Motion off: train, drops and arcs appear at their end states on the same beats; no network requests.

## Open questions
- None for Cory. Mr. Hollis (3 people images) goes to the contact sheet and the fresh representation check. The idea card's printable measuring card is left out (STANDARDS: no print-and-carry features); the Yard covers free measuring.
