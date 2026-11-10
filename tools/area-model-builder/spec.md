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
- Format: sandbox. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Eight multiplication rectangles (four 2 by 2 digit, four 4 by 1 digit), two compare rounds, six division rectangles (three with remainders), the equation strip. Extra: Match the slicing (write the equation for a slicing someone else made). tool.json `modes: ["Workbench", "Match the slicing"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.NBT.5 | Slice at place-value breaks; add the partial products | pieces labeled; the equation strip | 2 |
| 4.NBT.5 (properties) | Slice the same rectangle two ways | two strips with one total | 3 |
| 4.NBT.6 | Build the missing side in chunks; read the remainder | the area used up; a leftover sliver | 4 |

## Screens and modes
Header (kit): title "Area Model Builder"; `Workbench`, `Match the slicing`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A wooden workbench with a big blank rectangle labeled 23 by 14 and a pencil. The welcome is queued (`welcomeAfter: true`): "That's too big to count. Slice it where the numbers break apart. Drag a cut line onto the rectangle." First hint: "Drag a cut line onto the rectangle."

**Slicing (focus: the rectangle).** At 1366x768 the rectangle fills the left with the equation strip right; at 680x425 the strip is below. Cut lines snap only at place-value breaks (20 | 3 and 10 | 4). Each piece shows its sides and asks for its product; the strip fills: (20 + 3) x (10 + 4) = 200 + 80 + 30 + 12 = 322. Four-digit by one-digit: 3,215 x 6 slices into 3,000, 200, 10 and 5 strips: 18,000 + 1,200 + 60 + 30 = 19,290.

**Two slicings.** The same 23 by 14 sliced as 23 x 7 + 23 x 7 or 23 x (10 + 4): the totals match. "Two cuts, one rectangle."

**Division.** A shaded area of 852 with one side 4. The child drags chunks onto the missing side: 200 (uses 800), then 10 (uses 40), then 3 (uses 12). The side reads 213. Then 857 by 4: after 214, a sliver of 1 is left; the strip writes 857 = 4 x 214 + 1.

**Same rectangle (the aha).** A multiplication and its division sit side by side. Narrator: "Multiply, and you find the area. Divide, and you find the side. It's the same rectangle, seen from two sides."

**The end.** The child's slicings and equations. `Print` prints them.

**Match the slicing (extra).** A slicing appears; the child writes its equation.

## Content
- Eight products, six quotients (three with remainders), all within the standard's limits, readable with `Read`.

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
| Pieces | Type the total | Each piece needs its own product before the strip adds them. |
| Division | Type a quotient | The chunks must use up the area; the leftover is checked. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `cut`; `piece`.
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

## Done when
1. Focus and fold: at 1366x768 rectangle and strip; at 680x425 strip below.
2. Eight products are sliced at place-value breaks with partial products added. (4.NBT.5)
3. Two slicings of one rectangle give one total. (4.NBT.5)
4. Six quotients are built as missing sides, three with remainders. (4.NBT.6)
5. `Read` reads every card; every control is 48 px or more.
6. Stretched rectangles carry a "not to scale" tag.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: pieces appear at once; no network requests.

## Open questions
- The idea card moves 4.NBT.4 (the standard algorithm for adding and subtracting) out of this tool (default used: 4.NBT.4 is taught in road-trip-logbook; this tool keeps 4.NBT.5 and 4.NBT.6).
