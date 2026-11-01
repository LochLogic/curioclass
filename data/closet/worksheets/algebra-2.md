# 1. Powers of i
minutes: 30
materials: pencil
ican: I can simplify any power of i by using its repeating cycle of four.
directions: Use i² = -1 to build the cycle, then simplify each power of i to i, -1, -i or 1. Escape the maze by stepping only on true statements. Last, explain the cycle.
pairs: imaginary-island
mistakes: Students often divide the exponent by 4 and use the quotient instead of the remainder. For i^27, 27 = 4(6) + 3, and the remainder 3 gives -i. When the remainder is 0 the answer is 1, not 0 or i. For i^(-1), multiply 1/i by i/i to get -i.
notes: Remainder rule: divide the exponent by 4; remainder 0 → 1, 1 → i, 2 → -1, 3 → -i. Multiplying by i turns a point a quarter turn on the complex plane, so four quarter turns bring you back to 1, which is why the cycle has length four. In the maze, (-i)² = (-1)²i² = -1 is true.

## Warm up: Build the cycle
example: i¹ = i. i² = -1. i³ = i² · i = -i. i⁴ = i² · i² = (-1)(-1) = 1. Then the pattern starts again: i⁵ = i⁴ · i = i.
table: Power | i⁵ | i⁶ | i⁷ | i⁸
  - Value | { i} | {-1} | {-i} | { 1}

## Main: Simplify
fill:
  - i¹⁰ = {-1}
  - i¹³ = { i}
  - i¹⁹ = {-i}
  - i²⁴ = { 1}
  - i²⁷ = {-i}
  - i⁴² = {-1}
  - i¹⁰¹ = { i}
  - i⁰ = { 1}
  - i³⁵ = {-i}
  - i⁵⁸ = {-1}
  - i⁸⁹ = { i}
  - i⁻¹ = {-i}
maze: Step only on true statements.
  * i² = -1
  * i⁹ = i
  * i¹⁵ = -i
  * i²⁰ = 1
  * i³ · i⁵ = 1
  * i² + i⁴ = 0
  * (-i)² = -1
  * i⁵⁰ = -1
  - i³ = i
  - i⁴ = -1
  - i¹¹ = i
  - i⁶ = 1
  - i⁰ = 0
  - i²⁵ = -i
  - i + i³ = 2i
  - i² · i² = -1
  - i¹⁰⁰ = i
  - i⁷ = 1

## Stretch: Explain the cycle
write: Explain why the powers of i repeat every four. Then find i + i² + i³ + i⁴, and use it to find i + i² + i³ + ... + i¹⁰².
  lines: 4
  key: Each new power multiplies by i, and i⁴ = 1, so after four steps you are back to 1 and the values i, -1, -i, 1 repeat. One cycle sums to i - 1 - i + 1 = 0. The first 100 powers are 25 full cycles, which sum to 0, leaving i¹⁰¹ + i¹⁰² = i + (-1) = -1 + i.

# 21. Algebra II Midyear Review
minutes: 45
materials: pencil, scientific calculator
ican: I can solve problems with polynomials, rational expressions, exponentials and logarithms.
directions: Part A is a code: solve each problem, find the answer in the decoder, and write its letter in the numbered box. Then work Parts B to D. Show your work and give exact answers unless a decimal is asked for.
mistakes: Common slips: forgetting to check for extraneous solutions (the square root equation and the log equation each produce one); cancelling terms instead of factors in rational expressions ((x² - 9)/(x² + 5x + 6) is not -9/(5x + 6)); writing log(x²y/z) as 2 log x · log y. In compound interest, students sometimes use 0.5 instead of 0.05.
notes: The code spells ALGEBRA. Part A work: log₂ 8 = 3; p(2) = 2(8) + 2 - 4 = 14; log₅ 625 = 4; 2^(x + 1) = 64 = 2⁶ so x = 5; 80 → 40 → 20 → 10 mg after three half-lives; √(x + 7) = x + 1 gives x² + x - 6 = 0, x = 2 (x = -3 is extraneous); degree 3. In the log equation, x = -2 makes log₂ x undefined, so only x = 4 works. The interest answer uses 1.05¹⁰ ≈ 1.62889.

## Part A: Code warm up
code: Solve and decode.
  - log₂ 8 | 3 | A
  - Remainder when 2x³ + x - 4 is divided by (x - 2) | 14 | L
  - log₅ 625 | 4 | G
  - Solve 2^(x + 1) = 64 | 5 | E
  - Milligrams left of 80 mg after 18 hours if the half-life is 6 hours | 10 | B
  - Solve √(x + 7) = x + 1 | 2 | R
  - The degree of x³ - 2x² - 5x + 6 | 3 | A
  decoys: 6 7 12 8

## Part B: Polynomials
fill: Divide x³ - 2x² - 5x + 6 by (x - 1). Quotient: {x² - x - 6}, remainder: {0}
fill: Factor x³ - 2x² - 5x + 6 completely: {(x - 1)(x - 3)(x + 2)}. Zeros: {1, 3, -2}
fill: Expand (x + 2)³ = {x³ + 6x² + 12x + 8}
choice: Describe the end behavior of f(x) = -2x⁴ + x.
  - Up on the left, down on the right
  - Down on the left, up on the right
  * Down on both ends
  - Up on both ends

## Part C: Rational expressions
fill: Simplify (x² - 9)/(x² + 5x + 6) = {(x - 3)/(x + 2)}, for x ≠ -3, -2
fill: Add 2/x + 3/(x + 1) = {(5x + 2)/(x(x + 1))}
fill: f(x) = (x - 1)/(x² - 1) has a hole at x = {1} and a vertical asymptote at x = {-1}
fixit: 3/x + 1/2 = 2
  - Multiply every term by 2x: 6 + x = 4x
  * 6 = 5x
  - x = 6/5
  answer: x = 2
  why: Subtracting x from both sides gives 6 = 3x, not 5x, so x = 2. Check: 3/2 + 1/2 = 2.

## Part D: Exponentials and logarithms
fill: Solve log₂ x + log₂(x - 2) = 3. x = {4}
fill: Solve 5e^(2x) = 40. Exact: x = {(ln 8)/2}. Decimal to the nearest hundredth: x ≈ {1.04}
fill: Expand log(x²y/z) = {2 log x + log y - log z}
fill: $2,000 is invested at 5% interest compounded once a year. After 10 years the balance is {$3,257.79}

## Stretch
write: A culture of 500 bacteria doubles every 3 hours. Write a model for the number of bacteria after t hours and find when there will be 8,000.
  lines: 3
  key: N(t) = 500 · 2^(t/3). 8,000 = 500 · 2^(t/3) gives 2^(t/3) = 16 = 2⁴, so t/3 = 4 and t = 12 hours.
