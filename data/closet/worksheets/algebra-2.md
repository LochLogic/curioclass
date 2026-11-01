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

# 5. Long and Synthetic Division
minutes: 40
materials: pencil
ican: I can divide a polynomial by a linear factor with long division and with synthetic division and write the quotient and remainder.
directions: Divide the first four with long division and the four charts (A to D) with synthetic division. Write a 0 for every missing power before you start. Write each answer as a quotient and a remainder.
mistakes: The biggest error is leaving out missing terms: x³ - 8 must be written x³ + 0x² + 0x - 8, and x⁴ - 3x³ + 2x - 1 needs a 0 for x². In long division, students forget to subtract the whole product (subtracting 2x³ + 4x² from 2x³ + 3x² gives -x², not 7x²). In synthetic division, dividing by x + 4 uses -4, not 4.
notes: Long division, in order: x + 3, R 0; 2x² - x + 1, R 3; x² + 2x + 4, R 0; 3x² + 3x - 1, R 6. Charts: A) x² + x - 2, R 0. B) x³ + 2, R 5 (rows: 3, 0, 0, 6 and 1, 0, 0, 2, 5). C) 2x² - 3x - 2, R 1. D) x² - 3, R 2. Check: by the remainder theorem each remainder equals p(c); for (3x³ - 4x + 7) ÷ (x - 1), p(1) = 3 - 4 + 7 = 6. Stretch: (2x³ + x² - 5x + 2) ÷ (2x - 1) = x² + x - 2, R 0, so 2x³ + x² - 5x + 2 = (2x - 1)(x + 2)(x - 1).

## Warm up
fill:
  - Write x³ - 8 with every power: x³ + {0}x² + {0}x - 8
  - To divide by x + 4 with synthetic division, use the number {-4}.
  - By the remainder theorem, the remainder of p(x) ÷ (x - 2) is p({2}).

## Main: Long division
example: (x² + 7x + 10) ÷ (x + 2). x² ÷ x = x; x(x + 2) = x² + 2x; subtract: 5x + 10. 5x ÷ x = 5; 5(x + 2) = 5x + 10; subtract: 0. Quotient x + 5, remainder 0.
fill: (x² + 5x + 6) ÷ (x + 2). Quotient: {x + 3}, remainder: {0}
fill: (2x³ + 3x² - x + 5) ÷ (x + 2). Quotient: {2x² - x + 1}, remainder: {3}
fill: (x³ - 8) ÷ (x - 2). Quotient: {x² + 2x + 4}, remainder: {0}
fill: (3x³ - 4x + 7) ÷ (x - 1). Quotient: {3x² + 3x - 1}, remainder: {6}
draw: Long division work | 3.2

## Main: Synthetic division
text: Fill in each chart: bring down the first coefficient, multiply by the number on the left, add down the column, and repeat. The last number is the remainder.
text: **Chart A.** (x³ - 2x² - 5x + 6) ÷ (x - 3)
table: 3 | 1 | -2 | -5 | 6
  -  |  | {3} | {3} | {-6}
  -  | {1} | {1} | {-2} | {0}
fill: Quotient: {x² + x - 2}, remainder: {0}
text: **Chart B.** (x⁴ - 3x³ + 2x - 1) ÷ (x - 3)
table: 3 | 1 | -3 | 0 | 2 | -1
  -  |  | {3} | {0} | {0} | {6}
  -  | {1} | {0} | {0} | {2} | {5}
fill: Quotient: {x³ + 2}, remainder: {5}
text: **Chart C.** (2x³ - 7x² + 4x + 5) ÷ (x - 2)
table: 2 | 2 | -7 | 4 | 5
  -  |  | {4} | {-6} | {-4}
  -  | {2} | {-3} | {-2} | {1}
fill: Quotient: {2x² - 3x - 2}, remainder: {1}
text: **Chart D.** (x³ + 4x² - 3x - 10) ÷ (x + 4)
table: -4 | 1 | 4 | -3 | -10
  -  |  | {-4} | {0} | {12}
  -  | {1} | {0} | {-3} | {2}
fill: Quotient: {x² - 3}, remainder: {2}

## Stretch
write: Divide 2x³ + x² - 5x + 2 by 2x - 1. Then factor 2x³ + x² - 5x + 2 completely.
  lines: 3
  key: The quotient is x² + x - 2 with remainder 0, so 2x³ + x² - 5x + 2 = (2x - 1)(x² + x - 2) = (2x - 1)(x + 2)(x - 1).

# 15. Holes and Asymptotes
minutes: 40
materials: pencil, ruler
ican: I can find the holes and asymptotes of a rational function and use them to sketch its graph.
directions: Factor each function and cancel any common factor: a cancelled factor makes a hole. Fill in the table, then sketch the graphs (f and h share one grid). Draw asymptotes as dashed lines, draw a hole as an open circle, and plot a few points on each side of every vertical asymptote.
mistakes: Students often call every zero of the denominator a vertical asymptote; when the factor cancels, it is a hole instead (x = 2 in f and h). To find the hole's y-value, use the simplified function. For the horizontal asymptote, compare degrees: same degree gives the ratio of leading coefficients (g: y = 2), and a bigger denominator degree gives y = 0. Some students think a graph can never cross a horizontal asymptote; k crosses y = 0 at the origin.
notes: f(x) = (x - 2)/((x - 2)(x + 1)) = 1/(x + 1): hole (2, 1/3), vertical x = -1, horizontal y = 0, no x-intercept. g(x) = (2x + 1)/(x - 3): no hole, vertical x = 3, horizontal y = 2, x-intercept -1/2, y-intercept -1/3. h(x) = (x² - 4)/(x² - x - 2) = (x + 2)/(x + 1): hole (2, 4/3), vertical x = -1, horizontal y = 1, x-intercept -2. k(x) = 3x/(x² - 9): no hole, vertical x = -3 and x = 3, horizontal y = 0, through (0, 0). The key plots points of each curve as dots (on the shared grid, h is the curve that sits 1 unit above f everywhere); the asymptotes and holes are in the table. Because h = f + 1, the shared grid shows a vertical shift.

## Main: Find the features
table: Function | Simplified | Hole (x, y) | Vertical asymptote(s) | Horizontal asymptote
  - f(x) = (x - 2)/((x - 2)(x + 1)) | {1/(x + 1)} | {(2, 1/3)} | {x = -1} | {y = 0}
  - g(x) = (2x + 1)/(x - 3) | {does not simplify} | {none} | {x = 3} | {y = 2}
  - h(x) = (x² - 4)/(x² - x - 2) | {(x + 2)/(x + 1)} | {(2, 4/3)} | {x = -1} | {y = 1}
  - k(x) = 3x/(x² - 9) | {does not simplify} | {none} | {x = -3 and x = 3} | {y = 0}

## Sketch f and h on one grid
fill: Divide to see that h(x) = (x + 2)/(x + 1) = 1 + 1/(x + 1) = f(x) + {1}. So the graph of h is the graph of f shifted {up 1}.
graph: x | -6 6 1 | y | -6 6 1
  minor: off
  dots: yes
  key: -6,-0.2 -5.75,-0.21 -5.5,-0.22 -5.25,-0.24 -5,-0.25 -4.75,-0.27 -4.5,-0.29 -4.25,-0.31 -4,-0.33 -3.75,-0.36 -3.5,-0.4 -3.25,-0.44 -3,-0.5 -2.75,-0.57 -2.5,-0.67 -2.25,-0.8 -2,-1 -1.75,-1.33 -1.5,-2 -1.25,-4 -0.75,4 -0.5,2 -0.25,1.33 0,1 0.25,0.8 0.5,0.67 0.75,0.57 1,0.5 1.25,0.44 1.5,0.4 1.75,0.36 2.25,0.31 2.5,0.29 2.75,0.27 3,0.25 3.25,0.24 3.5,0.22 3.75,0.21 4,0.2 4.25,0.19 4.5,0.18 4.75,0.17 5,0.17 5.25,0.16 5.5,0.15 5.75,0.15 6,0.14
  key2: -6,0.8 -5.75,0.79 -5.5,0.78 -5.25,0.76 -5,0.75 -4.75,0.73 -4.5,0.71 -4.25,0.69 -4,0.67 -3.75,0.64 -3.5,0.6 -3.25,0.56 -3,0.5 -2.75,0.43 -2.5,0.33 -2.25,0.2 -2,0 -1.75,-0.33 -1.5,-1 -1.25,-3 -0.75,5 -0.5,3 -0.25,2.33 0,2 0.25,1.8 0.5,1.67 0.75,1.57 1,1.5 1.25,1.44 1.5,1.4 1.75,1.36 2.25,1.31 2.5,1.29 2.75,1.27 3,1.25 3.25,1.24 3.5,1.22 3.75,1.21 4,1.2 4.25,1.19 4.5,1.18 4.75,1.17 5,1.17 5.25,1.16 5.5,1.15 5.75,1.15 6,1.14

## Sketch g
graph: x | -6 6 1 | y | -6 6 1
  minor: off
  dots: yes
  key: -6,1.22 -5.75,1.2 -5.5,1.18 -5.25,1.15 -5,1.12 -4.75,1.1 -4.5,1.07 -4.25,1.03 -4,1 -3.75,0.96 -3.5,0.92 -3.25,0.88 -3,0.83 -2.75,0.78 -2.5,0.73 -2.25,0.67 -2,0.6 -1.75,0.53 -1.5,0.44 -1.25,0.35 -1,0.25 -0.75,0.13 -0.5,0 -0.25,-0.15 0,-0.33 0.25,-0.55 0.5,-0.8 0.75,-1.11 1,-1.5 1.25,-2 1.5,-2.67 1.75,-3.6 2,-5 4.75,6 5,5.5 5.25,5.11 5.5,4.8 5.75,4.55 6,4.33

## Sketch k
graph: x | -6 6 1 | y | -6 6 1
  minor: off
  dots: yes
  key: -6,-0.67 -5.75,-0.72 -5.5,-0.78 -5.25,-0.85 -5,-0.94 -4.75,-1.05 -4.5,-1.2 -4.25,-1.41 -4,-1.71 -3.75,-2.22 -3.5,-3.23 -2.75,5.74 -2.5,2.73 -2.25,1.71 -2,1.2 -1.75,0.88 -1.5,0.67 -1.25,0.5 -1,0.38 -0.75,0.27 -0.5,0.17 -0.25,0.08 0,0 0.25,-0.08 0.5,-0.17 0.75,-0.27 1,-0.38 1.25,-0.5 1.5,-0.67 1.75,-0.88 2,-1.2 2.25,-1.71 2.5,-2.73 2.75,-5.74 3.5,3.23 3.75,2.22 4,1.71 4.25,1.41 4.5,1.2 4.75,1.05 5,0.94 5.25,0.85 5.5,0.78 5.75,0.72 6,0.67

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

# 26. Pythagorean Identity
minutes: 35
materials: pencil
ican: I can use sin²θ + cos²θ = 1 and the quadrant of θ to find the other trigonometric values of an angle.
directions: Use sin²θ + cos²θ = 1 to find the missing sine or cosine. The quadrant decides the sign. Then find tan θ = sin θ / cos θ. Give exact answers and rationalize denominators.
mistakes: The most common error is the sign: the identity gives ±, and only the quadrant picks one. In quadrant II only sine is positive, in III only tangent, in IV only cosine. Students also take the square root too early (√(1 - 1/9) is not 1 - 1/3) or forget to rationalize: 1/(2√2) = √2/4.
notes: Work for sin θ = 1/3: cos²θ = 1 - 1/9 = 8/9, so cos θ = 2√2/3 (quadrant I), and tan θ = (1/3)/(2√2/3) = 1/(2√2) = √2/4. For sin θ = -2/3: cos²θ = 1 - 4/9 = 5/9, cos θ = √5/3 (quadrant IV), tan θ = -2/√5 = -2√5/5. Stretch: dividing the identity by cos²θ gives tan²θ + 1 = sec²θ; with tan θ = -2, sec²θ = 5, cos θ = -1/√5 = -√5/5 in quadrant II, and sin θ = tan θ cos θ = 2√5/5.

## Warm up: Signs by quadrant
table: Quadrant | I | II | III | IV
  - Sign of sin θ | + | {+} | {-} | {-}
  - Sign of cos θ | + | {-} | {-} | {+}
  - Sign of tan θ | + | {-} | {+} | {-}

## Main
example: sin θ = 3/5 in quadrant II. cos²θ = 1 - 9/25 = 16/25, so cos θ = ±4/5. In quadrant II cosine is negative: cos θ = -4/5. Then tan θ = (3/5)/(-4/5) = -3/4.
table: Given | Quadrant | sin θ | cos θ | tan θ
  - cos θ = 5/13 | IV | {-12/13} | 5/13 | {-12/5}
  - sin θ = -8/17 | III | -8/17 | {-15/17} | {8/15}
  - cos θ = -7/25 | II | {24/25} | -7/25 | {-24/7}
  - sin θ = 1/3 | I | 1/3 | {2√2/3} | {√2/4}
  - cos θ = -1/2 | III | {-√3/2} | -1/2 | {√3}
  - sin θ = -2/3 | IV | -2/3 | {√5/3} | {-2√5/5}
  - sin θ = 7/25 | II | 7/25 | {-24/25} | {-7/24}
  - cos θ = 0.6 | IV | {-0.8} | 0.6 | {-4/3}
  height: 0.45
draw: Work space | 3

## Stretch
write: Divide every term of sin²θ + cos²θ = 1 by cos²θ. What new identity do you get? Use it to find cos θ and sin θ when tan θ = -2 and θ is in quadrant II.
  lines: 4
  key: tan²θ + 1 = sec²θ. Then sec²θ = 4 + 1 = 5, so cos²θ = 1/5 and cos θ = -1/√5 = -√5/5 in quadrant II. sin θ = tan θ · cos θ = (-2)(-√5/5) = 2√5/5.

# 36. Normal Curve and Percentiles
minutes: 35
materials: pencil, calculator
ican: I can use the empirical rule and z-scores to find percents and percentiles in a normal distribution.
directions: Use the 68-95-99.7 rule for items that land on whole standard deviations, and the z-table for the others. A z-score tells how many standard deviations a value is from the mean: z = (value - mean) ÷ standard deviation.
mistakes: Students often use 68% for "above the mean plus one SD" instead of splitting the tails: 100% - 68% = 32%, and half of that, 16%, is in each tail. For a percentile, find the percent below the value, not above. When comparing two tests, students compare raw scores instead of z-scores.
notes: The heights are model numbers, roughly like adult women's heights in the United States; use the numbers given. Answers: 68%; 95%; 2.5% (half of 5%); 16%; z = (70 - 64)/2.5 = 2.4; 84th percentile; z = 1.5, about the 93rd percentile (93.3% below); test A z = 1.5 and test B z = 1.1, so test A is relatively better. Stretch: 64 to 69 is half of the middle 95%, so 47.5%; the top 2.5% starts at 500 + 2(100) = 700.

## Warm up
fill:
  - In a normal distribution, about {68}% of the data are within 1 standard deviation of the mean, {95}% within 2, and {99.7}% within 3.
  - A value 2 standard deviations below the mean has z = {-2}.

## Main: Heights
text: Model: the heights of adult women in a large group are approximately normal with mean 64 inches and standard deviation 2.5 inches. The curve shows the model.
graph: Height (inches) | 56.5 71.5 2.5 | Percent per inch | 0 16 4
  minor: off
  line: 56.5,0.18 57,0.32 57.5,0.54 58,0.90 58.5,1.42 59,2.16 59.5,3.16 60,4.44 60.5,5.99 61,7.77 61.5,9.68 62,11.59 62.5,13.33 63,14.73 63.5,15.64 64,15.96 64.5,15.64 65,14.73 65.5,13.33 66,11.59 66.5,9.68 67,7.77 67.5,5.99 68,4.44 68.5,3.16 69,2.16 69.5,1.42 70,0.90 70.5,0.54 71,0.32 71.5,0.18
fill:
  - What percent of the women are between 61.5 and 66.5 inches? {68%}
  - What percent are between 59 and 69 inches? {95%}
  - What percent are taller than 69 inches? {2.5%}
  - What percent are shorter than 61.5 inches? {16%}
  - What is the z-score of a woman who is 70 inches tall? {2.4}
  - A woman is 66.5 inches tall. About what percentile is she in? {84th}

## Main: Test scores
table: z | -2 | -1.5 | -1 | -0.5 | 0 | 0.5 | 1 | 1.5 | 2
  - Percent below | 2.3 | 6.7 | 15.9 | 30.9 | 50 | 69.1 | 84.1 | 93.3 | 97.7
fill:
  - Scores on a large test are normal with mean 500 and standard deviation 100. A student scores 650. z = {1.5}, about the {93rd} percentile.
  - Ana scores 82 on test A (mean 70, standard deviation 8) and 610 on test B (mean 500, standard deviation 100). Her z-scores are {1.5} on test A and {1.1} on test B, so she did relatively better on test {A}.

## Stretch
write: What percent of the women are between 64 and 69 inches? What test score marks the start of the top 2.5%? Explain both.
  lines: 3
  key: 64 to 69 is from the mean to 2 SD above, half of the middle 95%: 47.5%. The top 2.5% starts 2 SD above the mean: 500 + 2(100) = 700.
