# Area Model Builder

## One idea
On a workbench lies a big blank rectangle labeled 23 by 14, and the child drags cut lines at place-value breaks to slice it into pieces they can compute (20 x 10, 20 x 4, 3 x 10, 3 x 4), each piece shows its partial product, and an equation strip writes 23 x 14 = (20 + 3) x (10 + 4) = 200 + 80 + 30 + 12 = 322; four-digit by one-digit products (3,215 x 6) slice into four strips that add to 19,290; a compare round shows two different slicings of the same rectangle giving the same total; then division runs the rectangle backward: the area is 852 and one side is 4, and the child builds the other side in chunks (200, then 10, then 3) while the shaded area is used up, and when 857 is divided by 4 a sliver of 1 is left over and becomes the remainder; at the end the child sees that every multiplication and division here is the same rectangle seen from two sides, so a fourth grader learns to multiply up to four digits by one digit and two two-digit numbers, and to divide up to four digits by one digit with remainders, using place value, the properties of operations, area models and equations.

## Not like
- tile-the-floor (3, spec): area itself, same area engine. Here area as a model for big products.
- algebra-tile-studio (9, spec): factoring polynomials with tiles. Here whole-number products.
- equal-groups-zoo (3, spec): what multiplication means. Here multi-digit multiplication.
- road-trip-logbook (4, spec): adding and subtracting in columns. Here multiplying and dividing.

## Who and how
- Grade 4, Math, module "Multi-Digit Multiplication and Division". Standards: 4.NBT.5 (multiply a whole number of up to four digits by a one-digit whole number, and multiply two two-digit numbers, using strategies based on place value and the properties of operations; illustrate and explain the calculation by using equations, rectangular arrays, and/or area models), 4.NBT.6 (find whole-number quotients and remainders with up to four-digit dividends and one-digit divisors, using strategies based on place value, the properties of operations, and/or the relationship between multiplication and division; illustrate and explain the calculation by using equations, rectangular arrays, and/or area models).
- Format: sandbox. Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Change note (spec fix, 2026-11-10): the workbench and the slicing stay. Before, the equation strip filled itself and nothing asked the child to explain. Now the child types the whole equation into an empty strip (for division too), and after every second rectangle writes how the calculation worked, beside a model line and a three-box guide. The guide works 12 x 13 and 852 divided by 4 first as the models, so the six quotients are all the child's. The Content list now names every product and quotient.
- Eight multiplication rectangles (four 2 by 2 digit, four 4 by 1 digit), two compare rounds, six division rectangles (three with remainders), the equation strip. Extra: Match the slicing (write the equation for a slicing someone else made). tool.json `modes: ["Workbench", "Match the slicing"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.NBT.5 | multiply up to four digits by one digit, and two two-digit numbers, by place value and properties; illustrate and explain with equations and area models | the student | Slice at place-value breaks, type each partial product, type the whole equation, and on four rectangles write how it worked | 8 (four 2 by 2 digit, four 4 by 1 digit) | the child's pieces and the child's own equation | 2, 4 |
| 4.NBT.5 (properties) | use the properties of operations | the student | Slice the same rectangle two ways and write both equations | 2 | two strips with one total | 3 |
| 4.NBT.6 | find quotients and remainders, up to four digits by one digit, by place value and the link to multiplication; illustrate and explain with equations and area models | the student | Build the missing side in chunks, typing each chunk and the area it uses, type 857 = 4 x __ + __, and on three rectangles write how it worked | 6 (three with remainders; three- and four-digit) | the area used up; a leftover sliver | 5, 4 |

## Screens and modes
Header (kit): title "Area Model Builder"; `Workbench`, `Match the slicing`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A wooden workbench with a big blank rectangle labeled 23 by 14 and a pencil. The welcome is queued (`welcomeAfter: true`): "That's too big to count. Slice it where the numbers break apart. Drag a cut line onto the rectangle." First hint: "Drag a cut line onto the rectangle."

**The guide goes first (the model).** The workbench guide slices 12 by 13, types the four pieces, writes (10 + 2) x (10 + 3) = 100 + 30 + 20 + 6 = 156 on the strip and says how: "I broke 12 into 10 and 2 and 13 into 10 and 3, multiplied each pair, and added the four pieces." It cannot be skipped and `Guide's example` reopens it. The guide also works the first division, 852 by 4, before the child's six.

**Slicing (focus: the rectangle).** At 1366x768 the rectangle fills the left with the equation strip right; at 680x425 the strip is below. Cut lines snap only at place-value breaks (20 | 3 and 10 | 4). Each piece shows its sides and asks for its product. Then the strip, which is empty boxes, is the child's to write: (20 + 3) x (10 + 4) = 200 + 80 + 30 + 12 = 322. The strip is checked as a whole; a miss marks the box that is wrong, once, and a second miss sends the rectangle to the back of the stack with new numbers.

**Tell how.** After every second rectangle (four times in multiplication, three in division) a box opens: "Tell how you got it." The guide's model line stays in view with a three-box guide: says how each number was broken apart; names the pieces or chunks; says how they were put together. The child types or says a line and ticks the boxes. The tool cannot mark the words, so the model and the guide do that job; the line prints with the slicing. Four-digit by one-digit: 3,215 x 6 slices into 3,000, 200, 10 and 5 strips: 18,000 + 1,200 + 60 + 30 = 19,290.

**Two slicings.** The same 23 by 14 sliced as 23 x 7 + 23 x 7 or 23 x (10 + 4): the totals match. "Two cuts, one rectangle."

**Division.** A shaded area of 852 with one side 4, worked by the guide: chunks of 200 (uses 800), 10 (uses 40) and 3 (uses 12), so the side reads 213 and the strip says 852 = 4 x 213. Then the child's six. For each chunk the child types its size and the area it uses up, and the shaded area shrinks only when both are right. Chunks can be any size that fits, so 100 + 100 + 10 + 4 is as good as 200 + 10 + 4. When less than one more row is left the child types the leftover and then the whole equation in empty boxes: 857 = 4 x 214 + 1.

**Same rectangle (the aha).** A multiplication and its division sit side by side. Narrator: "Multiply, and you find the area. Divide, and you find the side. It's the same rectangle, seen from two sides."

**The end.** The child's slicings and equations. `Print` prints them.

**Match the slicing (extra).** A slicing appears; the child writes its equation.

## Content
- All readable with `Read`. Stretched rectangles carry a "not to scale" tag.
- The guide's models: 12 x 13 = 156; 852 = 4 x 213.
- Products, two-digit by two-digit: 23 x 14 = 322; 36 x 25 = 900; 47 x 18 = 846; 52 x 34 = 1,768. Four-digit by one-digit: 3,215 x 6 = 19,290; 1,408 x 7 = 9,856; 2,356 x 4 = 9,424; 5,079 x 3 = 15,237.
- Two slicings: 23 x 14 as 23 x (10 + 4) and as 23 x 7 + 23 x 7; 36 x 25 as (30 + 6) x 25 and as 36 x (20 + 5).
- Quotients: 936 = 3 x 312; 1,848 = 6 x 308; 7,245 = 5 x 1,449; 857 = 4 x 214 + 1; 2,507 = 8 x 313 + 3; 4,125 = 7 x 589 + 2.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cut lines and chunks can be moved until `Check`.
- Keyboard: Tab to cut lines, pieces, the strip boxes and chunk buttons; arrows move a cut line to the next break; Enter places.
- With Motion off pieces appear at once.

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
- event, whole, the guide's two examples.
- how `chunk`: "Drag a chunk onto the missing side."
- how `left`: "Type what's left over."
- event, whole, same rectangle.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
area (family "area"). Uses the shared pieces from the marked block `/* AREA ENGINE: begin */ ... /* end */` as described in tile-the-floor's spec: split lines that report each rectangle's area. Tool-only code: place-value snapping, the equation strip, division chunks and remainders, the "not to scale" tag.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Slicing | Cut anywhere | Cuts snap only at place-value breaks. |
| Pieces | Type the total | Each piece needs its own product. |
| Equation | Wait for the strip to fill | The strip is empty boxes; it is checked whole and a second miss brings a new rectangle. |
| Tell how | Tick the boxes on an empty line | The ticks open only when the line has words; the line prints for the teacher. |
| Division | Type a quotient; try chunk sizes until one sticks | Each chunk needs its size and the area it uses, and a chunk that is too big is refused without saying by how much. The leftover and the full equation are typed. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). The guide's example (whole). `cut`; `piece`; `strip`; `tell`.
2. `chunk`; `left`.
3. Same rectangle (whole), waits.
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

## Done when
1. Focus and fold: at 1366x768 rectangle and strip; at 680x425 strip below.
2. Eight products are sliced at place-value breaks and the child types every partial product and the whole equation. (4.NBT.5)
3. Two rectangles are each sliced two ways with both equations written and one total. (4.NBT.5)
4. Seven "Tell how" lines are written and checked against the guide, four for products and three for quotients. (4.NBT.5, 4.NBT.6)
5. Six quotients are built as missing sides, three with remainders, with the child typing each chunk, the leftover and the equation. (4.NBT.6)
6. The guide's 12 x 13 and 852 by 4 play first and can be reopened.
7. `Read` reads every card; every control is 48 px or more.
8. Stretched rectangles carry a "not to scale" tag.
9. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
10. Motion off: pieces appear at once; no network requests.

## Open questions
- The idea card moves 4.NBT.4 (the standard algorithm for adding and subtracting) out of this tool (default used: 4.NBT.4 is taught in road-trip-logbook; this tool keeps 4.NBT.5 and 4.NBT.6).
