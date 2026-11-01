# 1. Limits From Tables and Graphs
minutes: 40
materials: pencil, calculator (radian mode)
ican: I can estimate limits, including one-sided limits, from tables and graphs.
directions: Use each table to estimate the limit; write DNE if the limit does not exist, or ∞ if the values grow without bound. Then sketch g from its description and read its limits, and read the limits of h.
mistakes: Students often read the function value instead of the limit: g(2) = 1, but the limit of g at 2 is 3. In the k table, the values on the two sides disagree, so the two-sided limit does not exist even though each one-sided limit does. For 1/(x - 1)², "∞" describes how the limit fails to exist; it is not a number.
notes: Table values were computed and rounded: sin(x)/x is 0.9983342 at x = ±0.1, 0.9999833 at ±0.01 and 0.9999998 at ±0.001. The (1 + x)^(1/x) table approaches e ≈ 2.718; the exact value is not needed, only a good estimate. The answer key grid shows the two pieces of g; students should also draw an open circle at (2, 3) and a closed dot at (2, 1).

## Warm up: Read a table
text: f(x) = (x² - 4)/(x - 2)
table: x | 1.9 | 1.99 | 1.999 | 2 | 2.001 | 2.01 | 2.1
  - f(x) | 3.9 | 3.99 | 3.999 | undefined | 4.001 | 4.01 | 4.1
fill: The limit of f(x) as x → 2 is {4}, even though f(2) is undefined.

## Main: Limits from tables
text: s(x) = sin(x)/x, x in radians
table: x | -0.1 | -0.01 | -0.001 | 0.001 | 0.01 | 0.1
  - s(x) | 0.99833 | 0.99998 | 1.00000 | 1.00000 | 0.99998 | 0.99833
fill: lim as x → 0 of sin(x)/x ≈ {1}
text: k(x) = (x - 3)/√((x - 3)²), which is -1 or 1
table: x | 2.9 | 2.99 | 2.999 | 3.001 | 3.01 | 3.1
  - k(x) | -1 | -1 | -1 | 1 | 1 | 1
fill: lim as x → 3 from the left of k(x) = {-1}
fill: lim as x → 3 from the right of k(x) = {1}
fill: lim as x → 3 of k(x) = {DNE}
text: r(x) = (1 + x)^(1/x)
table: x | -0.1 | -0.01 | -0.001 | 0.001 | 0.01 | 0.1
  - r(x) | 2.8680 | 2.7320 | 2.7196 | 2.7169 | 2.7048 | 2.5937
fill: lim as x → 0 of (1 + x)^(1/x) ≈ {2.718}
text: q(x) = 1/(x - 1)²
table: x | 0.9 | 0.99 | 0.999 | 1.001 | 1.01 | 1.1
  - q(x) | 100 | 10,000 | 1,000,000 | 1,000,000 | 10,000 | 100
fill: lim as x → 1 of 1/(x - 1)² = {∞ (DNE)}

## Main: Limits from graphs
text: Sketch g: a line from (-2, -1) rising to an open circle at (2, 3); a closed dot at (2, 1); then a line falling from the open circle at (2, 3) to (5, 0). Then read the limits.
graph: x | -2 6 1 | y | -2 5 1
  key: -2,-1 2,3 5,0
fill: lim as x → 2 from the left of g(x) = {3}; from the right = {3}
fill: lim as x → 2 of g(x) = {3}, and g(2) = {1}
text: The graph of h is the parabola y = x² for x < 1, with an open circle at (1, 1), and the line y = x + 2 for x ≥ 1, starting with a closed dot at (1, 3).
fill: lim as x → 1 from the left of h(x) = {1}
fill: lim as x → 1 from the right of h(x) = {3}
fill: lim as x → 1 of h(x) = {DNE}

## Stretch
write: Is g continuous at x = 2? Is h continuous at x = 1? For each, name the kind of discontinuity and say how (if possible) to remove it.
  lines: 4
  key: Neither is continuous. g has a removable discontinuity at 2: the limit is 3 but g(2) = 1; redefining g(2) = 3 makes it continuous. h has a jump discontinuity at 1: the one-sided limits (1 and 3) differ, so no single value of h(1) can fix it.

# 22. Cooling Cup Rates
minutes: 40
materials: pencil, calculator
ican: I can estimate a derivative from a table and explain what it means in context, with units.
directions: A cup of hot cocoa cools on a table in a room at 20 °C. Use the table of temperatures T(t), where t is minutes after pouring. Estimate rates of change with difference quotients, give units, and explain what each number means.
mistakes: Students drop the negative sign or the units: T′(10) ≈ -2.14 °C per minute means the cocoa is losing about 2.1 degrees each minute at that moment. Some use a one-sided difference when a symmetric one (the times on each side) is available; both are estimates, but the symmetric one is usually closer. Watch for answers that divide by the number of rows instead of the minutes between them.
notes: Tangent line estimate: T(22) ≈ 45.8 + (-1.30)(2) = 43.2. The data come from a Newton's law of cooling model, T = 20 + 70e^(-0.05t), rounded to tenths, so they behave like careful measurements. The model's exact values: T′(10) ≈ -2.12, T′(20) ≈ -1.29 and T(22) ≈ 43.3, so the estimates are close. A real cup cools at a rate that depends on the cup, the lid and the air.

## Warm up: The data
table: t (minutes) | 0 | 5 | 10 | 15 | 20 | 25 | 30
  - T(t) (°C) | 90.0 | 74.5 | 62.5 | 53.1 | 45.8 | 40.1 | 35.6
fill: Units of T′(t): {degrees Celsius per minute}
fill: Average rate of change from t = 0 to t = 5: (74.5 - 90.0)/5 = {-3.1} °C per minute

## Main: Estimate and interpret
example: To estimate T′(5), use the times on each side: (62.5 - 90.0)/(10 - 0) = -2.75 °C per minute.
fill: T′(10) ≈ (T(15) - T(5))/10 = {-2.14} °C per minute
fill: T′(20) ≈ {-1.30} °C per minute
fill: T′(25) ≈ {-1.02} °C per minute
write: Explain what T′(10) ≈ -2.14 means for the cocoa, in a sentence with units.
  lines: 2
  key: At 10 minutes after pouring, the cocoa's temperature is falling at about 2.14 degrees Celsius per minute.
choice: As time goes on, the estimates of T′(t) are
  - negative and getting more negative, so the cooling speeds up
  * negative and getting closer to 0, so the cooling slows down
  - positive and getting smaller
  - the same each time, so the cooling is steady
fill: Use T(20) and your estimate of T′(20) to make a tangent line estimate of T(22). T(22) ≈ {43.2} °C
text: Plot the data and sketch a smooth curve through it.
graph: t (minutes) | 0 30 5 | T (°C) | 0 100 10
  key: 0,90 5,74.5 10,62.5 15,53.1 20,45.8 25,40.1 30,35.6
choice: The graph of T is
  - concave down, because T is decreasing
  * concave up, because T′ is increasing (less negative)
  - a straight line, because the cocoa cools steadily
  - concave up, because T is increasing

## Stretch
write: What value does T(t) approach as t grows large? What happens to T′(t)? Explain why this makes sense for a cup in a 20 °C room.
  lines: 4
  key: T(t) approaches 20 °C, the room temperature, and T′(t) approaches 0. The cocoa cools faster when it is much hotter than the room; as the difference shrinks, it cools more and more slowly and levels off at room temperature.
