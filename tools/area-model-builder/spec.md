# Area Model Builder

## One idea
On a workbench lies a big blank rectangle labeled 23 by 14, and the child drags cut lines at place-value breaks to slice it into pieces they can compute (20 x 10, 20 x 4, 3 x 10, 3 x 4), types each piece's partial product, and writes on an empty strip 23 x 14 = (20 + 3) x (10 + 4) = 200 + 80 + 30 + 12 = 322; one-digit multipliers slice a long rectangle into strips (3,215 x 6 is four strips that add to 19,290); compare rounds show two different slicings of the same rectangle giving the same total; and at the end the child multiplies with no cut lines offered at all, so a fourth grader learns to multiply up to four digits by one digit and two two-digit numbers using place value, the properties of operations, area models and equations, and to explain the calculation. Division, the same rectangle run backward to find a missing side, is the next tool's job.

## Not like
- tile-the-floor (3, spec): area itself, same area engine. Here area as a model for big products.
- algebra-tile-studio (9, spec): factoring polynomials with tiles. Here whole-number products.
- equal-groups-zoo (3, spec): what multiplication means. Here multi-digit multiplication.
- road-trip-logbook (4, spec): adding and subtracting in columns. Here multiplying and dividing.

## Who and how
- Grade 4, Math, module "Multi-Digit Multiplication and Division". Standards: 4.NBT.5 (multiply a whole number of up to four digits by a one-digit whole number, and multiply two two-digit numbers, using strategies based on place value and the properties of operations; illustrate and explain the calculation by using equations, rectangular arrays, and/or area models). Not here: 4.NBT.6, division with remainders, which has its own lesson tool in this module (approved 2026-11-10).
- Format: sandbox. Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Change note (spec fix, 2026-11-10): the workbench and the slicing stay. Before, the equation strip filled itself and nothing asked the child to explain. Now the child types the whole equation into an empty strip (for division too), and after every second rectangle writes how the calculation worked, beside a model line and a three-box guide. The guide works 12 x 13 and 852 divided by 4 first as the models, so the six quotients are all the child's. The Content list now names every product and quotient.
- Twelve multiplication rectangles (six 2 by 2 digit; one 2 by 1, one 3 by 1 and four 4 by 1 digit), three compare rounds, the equation strip, then four products on your own. Extra: Match the slicing (write the equation for a slicing someone else made). tool.json `modes: ["Workbench", "Match the slicing"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.
- Change note (split, 2026-11-11): 4.NBT.6 left for the new division tool, so the six division rectangles, the guide's 852 by 4 and the "same rectangle" ending are gone. The room went to four more products (so a one-digit multiplier is met with two, three and four digits), a third compare round and six "Tell how" lines. Added the three hooks: four products on your own with the end screen, English learner supports, access.
- English learners: every spoken line is also on screen in short sentences. The words product, partial product, equation and area model each show on a labeled rectangle the first time they are used. "Tell how" comes with a frame the child may take or leave: "I broke __ into __ and __. I multiplied __. Then I added __."

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.NBT.5 | multiply up to four digits by one digit, and two two-digit numbers, by place value and properties; illustrate and explain with equations and area models | the student | Slice at place-value breaks, type each partial product, type the whole equation, and on six rectangles write how it worked | 12 (six 2 by 2 digit; 2, 3 and 4 digits by 1 digit) and 4 on your own | the child's pieces and the child's own equation | 2, 4, 5 |
| 4.NBT.5 (properties) | use the properties of operations | the student | Slice the same rectangle two ways and write both equations | 3 | two strips with one total | 3 |

## Screens and modes
Header (kit): title "Area Model Builder"; `Workbench`, `Match the slicing`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A wooden workbench with a big blank rectangle labeled 23 by 14 and a pencil. The welcome is queued (`welcomeAfter: true`): "That's too big to count. Slice it where the numbers break apart. Drag a cut line onto the rectangle." First hint: "Drag a cut line onto the rectangle."

**The guide goes first (the model).** The workbench guide slices 12 by 13, types the four pieces, writes (10 + 2) x (10 + 3) = 100 + 30 + 20 + 6 = 156 on the strip and says how: "I broke 12 into 10 and 2 and 13 into 10 and 3, multiplied each pair, and added the four pieces." It cannot be skipped and `Guide's example` reopens it.

**Slicing (focus: the rectangle).** At 1366x768 the rectangle fills the left with the equation strip right; at 680x425 the strip is below. Cut lines snap only at place-value breaks (20 | 3 and 10 | 4). Each piece shows its sides and asks for its product. Then the strip, which is empty boxes, is the child's to write: (20 + 3) x (10 + 4) = 200 + 80 + 30 + 12 = 322. The strip is checked as a whole; a miss marks the box that is wrong, once, and a second miss sends the rectangle to the back of the stack with new numbers.

**Tell how.** After every second rectangle (six times) a box opens: "Tell how you got it." The guide's model line stays in view with a three-box guide: says how each number was broken apart; names the pieces or chunks; says how they were put together. The child types or says a line and ticks the boxes. The tool cannot mark the words, so the model and the guide do that job; the line prints with the slicing. Four-digit by one-digit: 3,215 x 6 slices into 3,000, 200, 10 and 5 strips: 18,000 + 1,200 + 60 + 30 = 19,290.

**Two slicings.** The same 23 by 14 sliced as 23 x 7 + 23 x 7 or 23 x (10 + 4): the totals match. "Two cuts, one rectangle."

**One rectangle (the aha).** The child's three compare rounds sit side by side. Narrator: "You cut each one two ways and the total never moved. Break the numbers any way you like. The rectangle is the same size."

**On your own.** Four products with the guide gone: `Guide's example` and the hints are hidden, cut lines no longer snap or suggest a break, pieces do not ask for their products, and the strip is one blank line. The child may slice or not, types the product and the equation, and each takes one answer. Nothing is marked until all four are in.

**The end.** The child's slicings and equations, and a results strip for the teacher: "4.NBT.5: 3 of 4 on your own", with the item missed and the answer the child gave. `Print` prints them.

**Match the slicing (extra).** A slicing appears; the child writes its equation.

## Content
- All readable with `Read`. Stretched rectangles carry a "not to scale" tag.
- The guide's model: 12 x 13 = 156.
- Products, two-digit by two-digit: 23 x 14 = 322; 36 x 25 = 900; 47 x 18 = 846; 52 x 34 = 1,768; 68 x 39 = 2,652; 84 x 56 = 4,704. One-digit multiplier: 86 x 7 = 602; 409 x 6 = 2,454; 3,215 x 6 = 19,290; 1,408 x 7 = 9,856; 2,356 x 4 = 9,424; 5,079 x 3 = 15,237.
- Two slicings: 23 x 14 as 23 x (10 + 4) and as 23 x 7 + 23 x 7; 36 x 25 as (30 + 6) x 25 and as 36 x (20 + 5); 84 x 56 as (80 + 4) x 56 and as 84 x (50 + 6).
- On your own: 29 x 31 = 899; 75 x 48 = 3,600; 2,460 x 7 = 17,220; 4,706 x 8 = 37,648. What a wrong answer means: 609 for 29 x 31 (or 2,840 for 75 x 48) means the child multiplied tens by tens and ones by ones and left out the two cross pieces. 14,322 for 2,460 x 7 means the pieces were worked as 2 x 7, 4 x 7 and 6 x 7 without their place values lined up. 3,248 or 32,608 for 4,706 x 8 means the zero in the tens place was dropped or a piece was put in the wrong place. A right product with a wrong equation means the child can compute but cannot yet show the break.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cut lines and chunks can be moved until `Check`.
- Keyboard: Tab to cut lines, pieces, the strip boxes and chunk buttons; arrows move a cut line to the next break; Enter places.
- With Motion off pieces appear at once.
- Access: every action works by tap and by keyboard. A cut line can be dragged, or picked with a tap and placed with a tap on a break, or moved with arrow keys. Motion can be paused. A wrong strip box is marked with a cross and the word "check", not by color alone.
- On your own: one answer each, no feedback until the fourth is in, then each shows right or not with the keyed product.

## Look
- Accent `--brand` #556b1f workbench olive (header, the rectangle frame, buttons); gold #f4c542 (the piece in hand, a finished strip); paper #f3f6ec; ink #1a2108; muted #555a4c.
- Contrast (WCAG 2.1, computed): white on brand 5.98:1; brand on paper 5.47:1; ink on paper 15.18:1; muted on paper 6.50:1; ink on gold 10.21:1.
- Never color alone: every piece shows its sides and product in numbers.
- Different from this batch (craft-fair plum, brick orange, quilt navy, track teal).

## Art
- Local FLUX (`scripts/localart.py`): the workbench frame (1, 16:9).
- Drawn in code: rectangles to scale where they fit and stretched with a "not to scale" tag where they don't, cut lines, pieces, chunks and the strip.
About 1 image.

## Voice
Two bank voices, each unique in this batch: `easy-coach` as the workbench guide; `big-sister` as the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.piece + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `cut`: "Drag a cut line onto the rectangle."
- how `piece`: "Type the product for this piece."
- how `strip`: "Type the whole equation on the strip."
- how `tell`: "Tell how you got it, then check the guide."
- event, whole, the guide's example.
- how `own`: "Four more on your own. No hints this time."
- event, whole, one rectangle.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
area (family "area"). Uses the shared pieces from the marked block `/* AREA ENGINE: begin */ ... /* end */` as described in tile-the-floor's spec: split lines that report each rectangle's area. Tool-only code: place-value snapping, the equation strip, division chunks and remainders, the "not to scale" tag.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Slicing | Cut anywhere | Cuts snap only at place-value breaks. |
| Pieces | Type the total | Each piece needs its own product. |
| Equation | Wait for the strip to fill | The strip is empty boxes; it is checked whole and a second miss brings a new rectangle. |
| Tell how | Tick the boxes on an empty line | The ticks open only when the line has words; the line prints for the teacher. |
| On your own | Retry until right; lean on the snapping | One answer each, no snapping, no piece prompts, and nothing is marked until all four are in. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). The guide's example (whole). `cut`; `piece`; `strip`; `tell`.
2. One rectangle (whole), waits.
3. `own`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.NBT.5, 4.NBT.6 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Area models link partial products to the distributive property | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | Van de Walle, Karp and Bay-Williams (2019), "Elementary and Middle School Mathematics: Teaching Developmentally", 10th edition | yes |
| Division as finding a missing side of a rectangle | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | National Research Council (2001), "Adding It Up: Helping Children Learn Mathematics" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s13, 2026-11-10): 23 x 14 = 200 + 80 + 30 + 12 = 322; 3,215 x 6 = 18,000 + 1,200 + 60 + 30 = 19,290; 852 = 4 x 213 with chunks using 800, 40 and 12; 857 = 4 x 214 + 1; contrast as in Look.
Checks run again for the spec fix (Python, scratchpad s/fx, 2026-11-10): 12 x 13 = 156; the eight products and their place-value pieces (36 x 25 = 600 + 150 + 120 + 30; 47 x 18 = 400 + 320 + 70 + 56; 52 x 34 = 1,500 + 200 + 60 + 8; 1,408 x 7 = 7,000 + 2,800 + 56; 2,356 x 4 = 8,000 + 1,200 + 200 + 24; 5,079 x 3 = 15,000 + 210 + 27); 23 x 7 + 23 x 7 = 322; 36 x 20 + 36 x 5 = 900; the six quotients and remainders with every remainder less than its divisor.
Checks run for the split (Python, scratchpad s/fx, 2026-11-11): 68 x 39 = 2,652; 84 x 56 = 4,704; 86 x 7 = 602; 409 x 6 = 2,454; 80 x 56 + 4 x 56 = 84 x 50 + 84 x 6 = 4,704; on your own 899, 3,600, 17,220, 37,648; wrong answers 20 x 30 + 9 x 1 = 609, 70 x 40 + 5 x 8 = 2,840, 14,000 + 280 + 42 = 14,322. The division checks above no longer apply.

## Done when
1. Focus and fold: at 1366x768 rectangle and strip; at 680x425 strip below.
2. Twelve products are sliced at place-value breaks and the child types every partial product and the whole equation. (4.NBT.5)
3. Three rectangles are each sliced two ways with both equations written and one total. (4.NBT.5)
4. Six "Tell how" lines are written and checked against the guide. (4.NBT.5)
5. Four products on your own run with no model, hint, snapping or piece prompts, one answer each; the end screen shows how many were right and what was missed. (4.NBT.5)
6. The guide's 12 x 13 plays first and can be reopened.
7. `Read` reads every card; every control is 48 px or more; every spoken instruction is also on screen, and each key word shows on a labeled rectangle at first use.
8. Every action works by keyboard as well as tap, cut lines have a tap and a key way, and nothing is shown by color alone.
9. Stretched rectangles carry a "not to scale" tag.
10. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
11. Motion off: pieces appear at once; motion can be paused; no network requests.

## Open questions
- The idea card moves 4.NBT.4 (the standard algorithm for adding and subtracting) out of this tool (default used: 4.NBT.4 is taught in road-trip-logbook; this tool keeps 4.NBT.5 and 4.NBT.6).
- The family engine line still names "division chunks and remainders" as tool-only code; after the split that code belongs to the new division tool (default used: left for Build to drop).
