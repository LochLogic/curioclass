# Polynomials as Numbers

## One idea
Set x = 10 and every polynomial turns into an ordinary number, so multiplying polynomials becomes long
multiplication where nothing ever carries: (2x + 3)(x + 4) keeps 11 and 12 in their columns while 23 × 14 has to
carry to 322, and turning the x dial to 2 or 100 shows why a polynomial can't carry: x is not always 10.

## Not like
- algebra-tile-studio (gr 9, same group): multiplies and factors with the area model. Cory's overlap call gives the area model to that tool; here there is no rectangle at all, only place-value columns and the long multiplication layout.
- rollercoaster-polynomials (gr 11): zeros and graphs of polynomials. Here no graph; arithmetic of polynomials as numbers.
- exponent-rule-builder (gr 9, same group): one base and its exponents. Here the powers of x are columns, like ones, tens, hundreds.
- factor-forge (gr 6): factors whole numbers. Here numbers and polynomials side by side, and the place where they part ways.
- savings-plan (gr 11): sums of sequences. Unrelated mechanic.

## Who and how
- Grade 9, Algebra 1, Polynomial Arithmetic. Students drive. 15 to 30 minutes.
- Topic line: "adding and multiplying polynomials" (from the batch note).
- Standards (module): A-APR.A (A-APR.A.1: polynomials are closed under addition, subtraction and multiplication; add, subtract and multiply them).
- CCSS cluster: A-APR.A in every mode; the closure line in Columns and the Orders checks serve A-APR.A.1 directly.
- tool.json: driver "students", minutes "15-30", modes ["Columns", "Multiply", "Orders"], grades_label "Grade 9".

## Screens and modes
Header: title, subtitle "Every polynomial is a number in disguise." Modes `Columns` (opens first), `Multiply`,
`Orders`. Kit buttons.
Layout: the column board is the stage, center and the largest thing at every size; the panel (x dial, mode buttons,
order cards in Orders) sits right, or under the board below 1000 px wide with the dial first.
The column board (every mode): five columns headed x⁴, x³, x², x, 1, and under each header its value at the
current x ("1000", "100", "10", "1" at x = 10). Each polynomial is a row of cells; a cell holds a whole-number
coefficient from −99 to 99, with `+` and `−` buttons and a number box. The row's polynomial prints at its left
("2x² + 11x + 12") and its value at the right ("= 322").
The x dial (every mode, top of the panel): buttons `x = 10` (default), `x = 100`, `x = 2`, `x = −1`, `x = 0` and a
slider from −10 to 10 (step 1) with a box. Changing x re-labels the column values and every row's value.

### Columns (add and subtract)
Focus: the result row filling column by column, with the carried number sum right beside it.
Two rows, A and B, and a result row. Operation buttons `A + B`, `A − B`. The result is written column by column,
each column animating its own sum, right to left, 150 ms a column (all at once with Motion off; no carrying arrows
ever appear). Beside it, the ordinary sum of the two
numbers at x = 10 in the usual written form, with carries shown as small digits. When any result coefficient is
above 9 or below 0, a note links them: "The polynomial keeps 11 in the x column. The number has to carry. Both
are right: at x = 10 they are the same number." A line under the board: "A polynomial plus or minus a polynomial is
always a polynomial: each column is just a whole number."

### Multiply
Focus: the long multiplication layout (partial rows and the product row) on the board, with the number version beside
it.
Two factor rows A and B (up to degree 2 each). `Multiply` lays out long multiplication exactly as on paper:
one partial row per term of B (B's ones term first), each shifted one column left per power, then the column sums.
Every partial-row cell is the product of one A cell and one B cell, shown on focus as "3 × 4 in the 1 column".
At right, the same digits as ordinary long multiplication of the two numbers at x = 10, with carries. `Test at
many x` evaluates A × B and the product row at x = −2, −1, 0, 1, 2, 3, 10 and 100 in a table, all equal (with
the equals signs checked). At x = 100, when every product coefficient is from 0 to 99, the note says "Each coefficient now has two
digits of room, so the number shows the coefficients without any carrying." (With a negative coefficient the blocks
borrow from each other and the note stays hidden.) Partial rows appear one at a time, 300 ms apart, then the column
sums (all at once with Motion off).

### Orders (builder challenges)
Focus: the result row on the board with the order's target row printed directly above it, so a match reads column by
column.
Order cards in the panel. Each gives a target; you set the rows (factor rows, or two rows for a sum) on the board and
press `Multiply` (or `A + B` for order 6, the only sum order); the order ticks when the result row equals the target
polynomial exactly. A card that is met gets a check and the word
"filled"; filled orders saved on this device (localStorage `curio-poly-numbers`, try/catch) with `Clear orders`.

## Content
Columns examples (menu `Load example`):
- 3x² + 2x + 1 alone: 321 at x = 10.
- (5x² + 3x + 7) − (2x² + 6x + 1) = 3x² − 3x + 6: at x = 10, 537 − 261 = 276 = 300 − 30 + 6.
- (4x + 8) + (7x + 5) = 11x + 13: at x = 10, 48 + 75 = 123 = 110 + 13.
Multiply examples:
- (x + 2)(x + 3) = x² + 5x + 6: 12 × 13 = 156.
- (x + 1)² = x² + 2x + 1: 11² = 121.
- (2x + 3)(x + 4) = 2x² + 11x + 12: 23 × 14 = 322 (number carries; polynomial does not).
- (x² + x + 1)(x − 1) = x³ − 1: 111 × 9 = 999 (negative coefficient: x − 1 is 9 at x = 10).
- (x + 1)³ = x³ + 3x² + 3x + 1: 1331 = 11³. (x + 1)⁴ = x⁴ + 4x³ + 6x² + 4x + 1: 14641.
- (x² + 2x + 1)(x² + 2x + 1) = x⁴ + 4x³ + 6x² + 4x + 1 (the same as (x + 1)⁴: 121 × 121 = 14641).
Orders:
1. "Make x² + 7x + 12 as a product." Works: (x + 3)(x + 4).
2. "Make x² − 1." Works: (x + 1)(x − 1). At x = 10: 11 × 9 = 99.
3. "Make 2x² + 7x + 3." Works: (2x + 1)(x + 3). At x = 10: 21 × 13 = 273.
4. "Make x³ − 8 from a first-degree and a second-degree factor." Works: (x − 2)(x² + 2x + 4). At 10: 8 × 124 = 992.
5. "Make 144 at x = 10 two different ways, with two products of first-degree factors that are different polynomials.
   Then find an x where they disagree." Works: (x + 2)(x + 2) = x² + 4x + 4 and (x − 1)(x + 6) = x² + 5x − 6;
   both 144 at x = 10; at x = 0 they are 4 and −6. The card ticks when both products are built, are different
   polynomials, agree at x = 10, and the dial is on an x where they differ.
6. "Make a sum, not a product: two polynomials that add to 5x² + 0x − 2, both with all three terms nonzero." Many work, for example (3x² + 4x − 5) + (2x² − 4x + 3).

## Interactions in detail
- Polynomials are integer coefficient arrays; every operation is exact integer arithmetic. Values at x are exact
  integers: the largest possible (degree 4 at x = 100, coefficients up to 29,403) stays far below 2^53.
- Coefficients are clamped to −99..99 in the inputs; a product coefficient may reach 3 × 99 × 99 = 29,403 and is
  shown in full (columns widen; at 375 px the board scrolls sideways inside its box with the row labels fixed).
- Degree cap: factor rows up to degree 2 (x² column) in Multiply, so products stay within x⁴; Columns rows up to x⁴.
- The ordinary long multiplication on the right is drawn only at x = 10 (it is the number view); at other x the
  right side shows the two values and their product as plain numbers.
- At x = 0 the board notes "Every column but the ones is worth 0 now"; at x = −1 the column values alternate
  1, −1, 1, −1, 1 and the note says so.
- Order checks compare coefficient arrays exactly; factor order does not matter. Order 5 also checks that the two
  products differ in at least one coefficient.
- Tap while it plays: any coefficient change, dial change, operation or mode switch during a column or partial-row
  animation finishes it at once and shows the new state; nothing waits for the animation.
- Reset: `Clear rows` per mode. Mode switches keep rows for the session.
- Keyboard: Tab through cells; up and down arrow keys change a coefficient by 1; Enter runs the operation.
- `window.__tool = {state, setMode, setX(x), rows(), multiply(), check(order)}`.

## Look
Accent `--brand #f3e3a0` (chalk cream), `--brand-ink #231c05`. The board is a dark ledger `#121a14` with column
rules `#2e3b31` and headers `#f3e3a0`; coefficients in the readout font `#e8edf3`; carries on the number side
small `#ffb8a8` digits with a caret glyph; negative coefficients carry a minus sign (never color only). Contrast
(computed): brand on panel 13.44:1, on --sec-bg 12.74:1, brand-ink on brand 13.15:1.

## Art
none: drawn in code. The whole tool is a place-value board of numbers (columns, coefficients, carries, the dial),
which is a diagram that must re-lay itself for every x; there is no scene, object or character to paint.

## Voice
Bank voice `friendly-dad` (Achird, "Say in a relaxed, friendly way, like a kind dad helping with homework"). Every
kept voice is used by one of this tool's neighbors; friendly-dad's only other user is optimization-workshop (grade 12
calculus), the most distant. Not used by group siblings or the R02 batch. `Curio.voice`, `scope: () => state.mode`.
Rows, notes and order cards are read on screen; Read speaks the hint.
- wColumns (how, Columns welcome; stale on the first operation): "Set the coefficients in rows A and B with plus and minus, then press A plus B. Watch each column add on its own."
- wMultiply (how, Multiply welcome; stale on the first Multiply): "Fill the two factor rows and press Multiply. It's long multiplication, just without carrying."
- wOrders (how, Orders welcome; stale when an order card is tapped): "Tap an order card. Set the rows on the board, then press Multiply."
- carry (how, first result coefficient above 9 at x = 10; stale when x changes or no coefficient is above 9): "That column holds more than 9. The polynomial keeps it there. The number has to carry."
- dial (how, first dial change away from 10; stale on the next dial change): "New x, new column values. The polynomial didn't change. Its value did."
- order5 (how, order 5 first has both products agreeing at x = 10; stale when it is filled or the order changes): "Both make 144. Now move the x dial to a value where they disagree."
- filled (event, an order met; stale on order change): "Order filled. Tap another order card."

## Family engine
none.

## Sources
- A-APR.A: Common Core State Standards for Mathematics, High School Algebra, Arithmetic with Polynomials and Rational Expressions, https://www.thecorestandards.org/Math/Content/HSA/APR/
- Adding, subtracting and multiplying polynomials; a polynomial at x = 10 as a base-ten number: OpenStax, Elementary Algebra 2e, 6.1 "Add and Subtract Polynomials" and 6.3 "Multiply Polynomials", https://openstax.org/books/elementary-algebra-2e/pages/6-3-multiply-polynomials
- Checks run (Python, numpy polymul, 2026-10-29): every Multiply example and order expands as listed, and the product
  equals A × B at x = −2, −1, 0, 1, 2, 3, 10 and 100; at x = 10: 12 × 13 = 156, 11² = 121, 23 × 14 = 322,
  111 × 9 = 999, 11 × 121 = 1331, 121 × 121 = 14641, 13 × 14 = 182, 11 × 9 = 99, 21 × 13 = 273, 8 × 124 = 992;
  at x = 100 (x + 1)⁴ = 104060401. Columns: 537 − 261 = 276, 48 + 75 = 123. Order 5: x² + 4x + 4 and x² + 5x − 6
  agree only at x = 10 (every other x on the dial separates them). Order 6 example sums to 5x² + 0x − 2. Largest
  product coefficient 3 × 99 × 99 = 29,403; largest value 1.5 × 10^13, below 2^53 = 9.0 × 10^15. The x = 100 note
  was true only for coefficients 0 to 99 (x³ − 1 shows 999999), so it now shows only then.

## Done when
1. Columns: (5x² + 3x + 7) − (2x² + 6x + 1) gives 3x² − 3x + 6 and 276 at x = 10, beside 537 − 261 = 276.
2. Multiply (2x + 3)(x + 4): partial rows 8x + 12 and 2x² + 3x, product 2x² + 11x + 12; the number side shows 23 × 14 with carries and 322.
3. `x = 100` on (x + 1)⁴ (loaded as (x² + 2x + 1)(x² + 2x + 1)) reads 104060401 and the two-digits-of-room note shows; on (x² + x + 1)(x − 1) it reads 999999 and the note stays hidden.
4. `Test at many x` on (x² + x + 1)(x − 1) shows equal columns at all eight x values; at x = 10, 111 × 9 = 999.
5. Order 5 ticks with (x + 2)(x + 2) and (x − 1)(x + 6) only after the dial is moved off 10 (for example x = 0: 4 and −6).
6. Order 4 accepts (x − 2)(x² + 2x + 4) in either order; order 6 ticks only on `A + B`.
7. Coefficient inputs refuse 100; a product coefficient above 99 still shows in full.
8. Focus: at 1366x768 and 1000x625 the column board is the largest thing, center, in every mode, and in Orders the target row sits directly above the result row.
9. Tap while it plays: changing a coefficient or the dial during a column or partial-row animation shows the new result at once, with no half-filled columns.
10. Filled orders survive a reload; `Clear orders` works; every size in STANDARDS.md keeps the board and dial visible; keyboard only works; no voice line names a disabled control; console clean, no network.

## Open questions
- [polynomials-as-numbers] Voice: every kept voice is already used by a neighbor; this keeps friendly-dad (shared only with optimization-workshop, grade 12). OK?
