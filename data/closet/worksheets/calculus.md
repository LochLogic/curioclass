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

# 5. Limits at Infinity
minutes: 35
materials: pencil, calculator
ican: I can find limits at infinity and use them to find horizontal asymptotes.
directions: Find each limit. Write ∞ or -∞ if the values grow without bound. Then give the horizontal asymptote that the limit shows, or write "none." Show your work: for rational functions, divide every term by the highest power of x in the denominator.
mistakes: For √(9x² + 1), students write √(9x²) = 3x for every x; it is 3|x|, which is -3x when x is negative, so the limit at -∞ is -3/2, not 3/2. Students say "the degree of the top is bigger, so the limit is 0"; that rule is backward. A limit of ∞ means there is no horizontal asymptote on that side, not that the asymptote is y = ∞.
notes: Rules for rational functions: if the degree of the numerator is less than the degree of the denominator, the limit is 0; if the degrees are equal, it is the ratio of the leading coefficients; if the numerator's degree is greater, there is no horizontal asymptote. Warm-up values: f(10) = 21/7 = 3, f(100) = 201/97 ≈ 2.0722, f(1,000) = 2,001/997 ≈ 2.0070, f(10,000) = 20,001/9,997 ≈ 2.0007. The sin x / x limit uses the squeeze theorem: -1/x ≤ sin x / x ≤ 1/x for x > 0.

## Warm up: Watch it settle
text: f(x) = (2x + 1)/(x - 3). Round to four decimal places.
table: x | 10 | 100 | 1,000 | 10,000
  - f(x) | {3} | {2.0722} | {2.0070} | {2.0007}
fill: As x → ∞, f(x) → {2}, so the line y = {2} is a horizontal asymptote.

## Main: Eight limits
example: lim as x → ∞ of (6x² + x)/(2x² - 5) = lim (6 + 1/x)/(2 - 5/x²) = 6/2 = 3. Horizontal asymptote: y = 3.
fill: lim as x → ∞ of (3x² - 5x + 1)/(6x² + 2) = {1/2}. Asymptote: {y = 1/2}
fill: lim as x → ∞ of (4x + 7)/(x² - 3) = {0}. Asymptote: {y = 0}
fill: lim as x → ∞ of (x³ + 1)/(2x² - x) = {∞}. Asymptote: {none}
fill: lim as x → -∞ of (5 - 2x)/(3x + 4) = {-2/3}. Asymptote: {y = -2/3}
fill: lim as x → ∞ of √(9x² + 1)/(2x - 5) = {3/2}. Asymptote: {y = 3/2}
fill: lim as x → -∞ of √(9x² + 1)/(2x - 5) = {-3/2}. Asymptote: {y = -3/2}
fill: lim as x → -∞ of (eˣ + 3) = {3}. Asymptote: {y = 3}
fill: lim as x → ∞ of (sin x)/x = {0}. Asymptote: {y = 0}

## Stretch
choice: Which function has two different horizontal asymptotes?
  - (3x² - 5x + 1)/(6x² + 2)
  - (x³ + 1)/(2x² - x)
  * √(9x² + 1)/(2x - 5)
  - (4x + 7)/(x² - 3)
write: Can the graph of a function cross its horizontal asymptote? Use (sin x)/x to explain.
  lines: 3
  key: Yes. (sin x)/x approaches its asymptote y = 0 as x → ∞, but it equals 0 every time sin x = 0 (x = π, 2π, 3π, ...), so it crosses the asymptote over and over. A horizontal asymptote describes the end behavior only.

# 16. Motion on a Line
minutes: 45
materials: pencil
ican: I can use velocity and acceleration to describe a particle's motion, including when it speeds up or slows down.
pairs: motion-graph-match
directions: Each particle moves along a horizontal line; t is in seconds and position s is in meters, with t ≥ 0. Velocity is v = s′(t) and acceleration is a = v′(t). Positive velocity means moving right. A particle speeds up when v and a have the same sign, and slows down when they have opposite signs.
mistakes: Students say "acceleration is negative, so it slows down." That is only true when the velocity is positive: in particle A on 1 < t < 2, v and a are both negative, so it speeds up while moving left. For total distance, students subtract s(4) - s(0) and get 4; the particle turns around twice, so add the distance of each leg: 4 + 4 + 4 = 12. On a velocity graph, speed is the distance from the t-axis, so speeding up means the graph moves away from the axis.
notes: Particle A: v = 3(t - 1)(t - 3), a = 6(t - 2); s(0) = 0, s(1) = 4, s(3) = 0, s(4) = 4. Particle B: s(2) = -3 is its leftmost point. Particle C: v(2) = 0 and a(t) = -2t < 0 for t > 0. Particle D's graph has v = 0 at t = 1 (on the line from (0, -3) to (2, 3)) and at t = 5.5 (on the line from (4, 3) to (6, -1)); its acceleration is the slope of each segment: 3, 0, -2 and 0. The Motion Graph Match tool shows position, velocity and acceleration graphs drawing together.

## Warm up: Signs
fill:
  - v > 0 and a > 0: speeding up or slowing down? {speeding up}
  - v > 0 and a < 0: {slowing down}
  - v < 0 and a < 0: {speeding up}

## Main: Particle A
text: s(t) = t³ - 6t² + 9t
fill: v(t) = {3t² - 12t + 9}, and a(t) = {6t - 12}
fill: The particle is at rest when t = {1 and 3}, and a(t) = 0 when t = {2}.
table: Interval | Sign of v | Sign of a | Speeding up or slowing down?
  - 0 < t < 1 | {+} | {-} | {slowing down}
  - 1 < t < 2 | {-} | {-} | {speeding up}
  - 2 < t < 3 | {-} | {+} | {slowing down}
  - t > 3 | {+} | {+} | {speeding up}
fill: Total distance traveled from t = 0 to t = 4: {12} m. Displacement: {4} m.

## Main: Particles B and C
text: **Particle B:** s(t) = 2t² - 8t + 5
fill: v(t) = {4t - 8}, a(t) = {4}. B moves left when {0 ≤ t < 2}, slows down when {0 < t < 2}, and speeds up when {t > 2}.
text: **Particle C:** v(t) = 4 - t² for 0 ≤ t ≤ 4
fill: a(t) = {-2t}. C changes direction at t = {2}, slows down when {0 < t < 2}, and speeds up when {2 < t ≤ 4}.

## Main: Particle D
text: The graph shows the velocity of particle D.
graph: t (seconds) | 0 8 1 | v (m/s) | -4 4 1
  line: 0,-3 2,3 4,3 6,-1 8,-1
  minor: off
fill: D is at rest at t = {1} and t = {5.5}.
fill: a(3) = {0} m/s², and a(5) = {-2} m/s².
fill: D speeds up when {1 < t < 2} and {5.5 < t < 6}, and slows down when {0 < t < 1} and {4 < t < 5.5}.

## Stretch
write: At t = 1.5, particle A has negative acceleration, but it is speeding up. Explain how that can be.
  lines: 3
  key: At t = 1.5, v = 3(0.5)(-1.5) = -2.25 and a = 6(1.5) - 12 = -3. Both are negative, so the acceleration points the same way the particle is moving (left). The velocity is getting more negative, so the speed |v| is increasing.

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

# 26. Definite Integral Properties
minutes: 35
materials: pencil
ican: I can evaluate definite integrals using their properties and the areas of geometric shapes.
directions: Use the given values and the properties of definite integrals for Part A. In Part B, sketch the graph of each integrand and use area formulas (triangles, rectangles, trapezoids, circles); area below the x-axis counts as negative.
mistakes: Students forget that reversing the limits changes the sign. In 2f - 3g they multiply only one of the integrals by its constant. For ∫ from 1 to 6 of (3 - x) dx, many add the two triangle areas (2 + 4.5) instead of counting the part below the axis as negative. For √(9 - x²), students need to recognize the top half of a circle of radius 3.
notes: Properties used: ∫ from a to a = 0; ∫ from b to a = -∫ from a to b; ∫ from a to b + ∫ from b to c = ∫ from a to c; ∫ (kf ± g) = k∫f ± ∫g; ∫ from a to b of a constant c = c(b - a). Item 10 is 0 because x³ is odd and the interval is symmetric about 0. Stretch graph: from 0 to 2, area 4; from 2 to 4 the line crosses at x = 3, so +1 and -1 cancel; from 4 to 6, -4; from 6 to 8, a triangle of -2.

## Part A: Use the properties
text: Given: ∫ from 0 to 3 of f(x) dx = 5, ∫ from 3 to 7 of f(x) dx = -2, and ∫ from 0 to 7 of g(x) dx = 4.
example: ∫ from 3 to 0 of 2f(x) dx = -2 · ∫ from 0 to 3 of f(x) dx = -2(5) = -10.
fill: ∫ from 0 to 7 of f(x) dx = {3}
fill: ∫ from 3 to 0 of f(x) dx = {-5}
fill: ∫ from 0 to 7 of [2f(x) - 3g(x)] dx = {-6}
fill: ∫ from 7 to 7 of f(x) dx = {0}
fill: ∫ from 0 to 3 of [f(x) + 4] dx = {17}

## Part B: Use geometry
fill: ∫ from -3 to 3 of √(9 - x²) dx = {9π/2}
fill: ∫ from 0 to 4 of (2x + 1) dx = {20}
fill: ∫ from -2 to 3 of |x| dx = {13/2}
fill: ∫ from 1 to 6 of (3 - x) dx = {-5/2}
fill: ∫ from -2 to 2 of x³ dx = {0}

## Stretch: Read the graph
text: The graph of f is made of line segments.
graph: x | 0 8 1 | y | -3 3 1
  line: 0,2 2,2 4,-2 6,-2 8,0
  minor: off
fill: ∫ from 0 to 8 of f(x) dx = {-2}
fill: ∫ from 8 to 0 of f(x) dx = {2}
fill: ∫ from 0 to 8 of |f(x)| dx = {12}

# 37. Average Value
minutes: 40
materials: pencil, calculator
ican: I can find the average value of a function on an interval and explain what it means in context.
directions: The average value of f on [a, b] is 1/(b - a) times the integral of f from a to b. Give exact answers and decimals rounded to three places. In Part B, explain each answer in a sentence with units.
mistakes: Students compute (f(a) + f(b))/2, the average of the endpoint values; that works only for linear functions like 2x + 1, not for x² or sin x. Some forget to divide by b - a, giving the integral instead of the average. In context, the average rate is not the total: 30 liters per minute is an average rate, while 300 liters is the total amount.
notes: Part A work: x² gives (1/3)(27/3) = 3; 2x + 1 gives (1/4)(30 - 2) = 7; sin x gives (1/π)(2) = 2/π; 1/x gives (1/(e - 1))(ln e - ln 1) = 1/(e - 1); √x gives (1/4)(2/3)(8) = 4/3; eˣ gives (1/ln 3)(3 - 1) = 2/ln 3. Temperature: the integral of sin(πt/12) from 0 to 12 is 24/π, so the average is 60 + (10)(24/π)/12 = 60 + 20/π ≈ 66.37 °F. The stretch is the Mean Value Theorem for integrals: a continuous function equals its average value somewhere on the interval.

## Warm up: Two ways to average
fill: The average of f(x) = 2x + 1 at x = 1 and x = 5 is {7}.
fill: The average of f(x) = x² at x = 0 and x = 3 is {4.5}.
text: Keep these numbers. You will compare them with the first two average values in Part A.

## Part A: Six average values
example: Average value of f(x) = 3x² on [0, 2]: (1/2) ∫ from 0 to 2 of 3x² dx = (1/2)(8) = 4.
fill:
  - f(x) = x² on [0, 3]: {3}
  - f(x) = 2x + 1 on [1, 5]: {7}
  - f(x) = sin x on [0, π]: {2/π ≈ 0.637}
  - f(x) = 1/x on [1, e]: {1/(e - 1) ≈ 0.582}
  - f(x) = √x on [0, 4]: {4/3 ≈ 1.333}
  - f(x) = eˣ on [0, ln 3]: {2/ln 3 ≈ 1.820}
choice: For which function did the average of the endpoint values in the warm up equal the true average value?
  - f(x) = x², because it is a polynomial
  * f(x) = 2x + 1, because it is linear
  - Both of them
  - Neither of them

## Part B: In context
fill: The temperature t hours after 8 a.m. is T(t) = 60 + 10 sin(πt/12) °F. Its average value from 8 a.m. to 8 p.m. (0 ≤ t ≤ 12) is {60 + 20/π ≈ 66.37} °F.
write: Explain what your answer means.
  lines: 2
  key: Over the 12 hours from 8 a.m. to 8 p.m., the temperature averaged about 66.4 °F. A steady temperature of 66.4 °F for those 12 hours would have the same integral as the real temperature.
fill: Water flows into a tank at r(t) = 40 - 2t liters per minute for 0 ≤ t ≤ 10. The average rate is {30} liters per minute, and the total that flows in is {300} liters.
write: Explain what the average rate means.
  lines: 2
  key: If water had flowed in at a steady 30 liters per minute for the 10 minutes, the same 300 liters would have entered the tank.

## Stretch
fill: f(x) = x² equals its average value on [0, 3] at x = c. c = {√3 ≈ 1.732}
write: Why must a continuous function equal its average value at least once on the interval?
  lines: 3
  key: A continuous function on [a, b] has a smallest value m and a largest value M, and its average value is between them. By the Intermediate Value Theorem it takes on every value between m and M, so it takes on its average value somewhere. This is the Mean Value Theorem for integrals.
