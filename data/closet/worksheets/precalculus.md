# 1. Function Families Gallery
minutes: 40
materials: pencil, graphing calculator or graph paper (optional)
ican: I can recognize the graphs of the parent functions and describe each one's domain, range and end behavior.
directions: Each gallery card describes a graph in words. Match each card to its parent function. Then fill in the table of domain, range and end behavior, and sketch one graph on the grid.
mistakes: Students mix up the cubic and the cube root (both pass through the origin and rise left to right): the cubic is flat at the origin and steep far out, the cube root is steep (vertical) at the origin and flattens far out. For domain and range, watch for [0, ∞) versus (0, ∞): the square root includes 0, the exponential never reaches 0. Sine and cosine have no end behavior limit; they keep oscillating.
notes: The gallery is given as word descriptions of the graphs, so students must picture each shape. To make it visual, project or draw the twelve parent graphs without labels and let students match those as well. End behavior is written as "x → -∞, y → ?; x → ∞, y → ?". For the square root and log, only the right end exists; for the log, y → -∞ as x → 0 from the right.

## Warm up: Match the gallery
match: Match each graph card to its parent function.
  - A straight line through the origin, rising at a 45° angle = f(x) = x
  - A U shape with its lowest point at the origin = f(x) = x²
  - Flat at the origin, then rising steeply to the upper right and falling steeply to the lower left = f(x) = x³
  - A V shape with its corner at the origin = f(x) = |x|
  - Starts at the origin and curves up to the right, getting flatter; nothing to the left of the y-axis = f(x) = √x
  - Vertical at the origin, then flattening out as it goes right and left = f(x) = ∛x
  - Two separate branches, in quadrants I and III, each hugging both axes = f(x) = 1/x
  - Hugs the x-axis on the left, crosses the y-axis at 1, then climbs steeply = f(x) = eˣ
  - Hugs the y-axis far below, crosses the x-axis at 1, then climbs slowly = f(x) = ln x
  - A wave between -1 and 1 that passes through the origin going up = f(x) = sin x
  - A wave between -1 and 1 with a peak at (0, 1) = f(x) = cos x
  - Flat steps one unit wide, each with a closed dot on the left and an open dot on the right = f(x) = ⌊x⌋

## Main: Domain, range, end behavior
table: Function | Domain | Range | End behavior (left; right)
  - x | {all reals} | {all reals} | {y → -∞; y → ∞}
  - x² | {all reals} | {[0, ∞)} | {y → ∞; y → ∞}
  - x³ | {all reals} | {all reals} | {y → -∞; y → ∞}
  - absolute value of x | {all reals} | {[0, ∞)} | {y → ∞; y → ∞}
  - √x | {[0, ∞)} | {[0, ∞)} | {none; y → ∞}
  - ∛x | {all reals} | {all reals} | {y → -∞; y → ∞}
  - 1/x | {x ≠ 0} | {y ≠ 0} | {y → 0; y → 0}
  - eˣ | {all reals} | {(0, ∞)} | {y → 0; y → ∞}
  - ln x | {(0, ∞)} | {all reals} | {none; y → ∞}
  - sin x | {all reals} | {[-1, 1]} | {oscillates; oscillates}
  - cos x | {all reals} | {[-1, 1]} | {oscillates; oscillates}
  - ⌊x⌋ | {all reals} | {all integers} | {y → -∞; y → ∞}

## Stretch: Sketch one
text: Sketch f(x) = ∛x on the grid. Plot at least five exact points first (try x = -8, -1, 0, 1 and 8).
graph: x | -8 8 2 | y | -3 3 1
  key: -8,-2 -6,-1.817 -4,-1.587 -2,-1.26 -1,-1 -0.5,-0.794 -0.125,-0.5 0,0 0.125,0.5 0.5,0.794 1,1 2,1.26 4,1.587 6,1.817 8,2
write: Which two families in the table have the same domain, range and end behavior as f(x) = x? How can you still tell their graphs apart?
  lines: 3
  key: f(x) = x³ and f(x) = ∛x (and ⌊x⌋ has the same domain and end behavior but its range is only integers). The cubic is flat at the origin and steep far out; the cube root is vertical at the origin and flat far out. The line has the same steepness everywhere.

# 5. Concavity From Rate Tables
minutes: 35
materials: pencil, calculator (optional)
ican: I can use average rates of change from a table to decide where a function is concave up or concave down.
directions: For each table, find the average rate of change on each interval: (change in y) ÷ (change in x). Then look at how the rates change. Rates that increase mean concave up; rates that decrease mean concave down.
mistakes: Students judge concavity from whether the y-values go up or down. That tells increasing or decreasing, not concavity: k decreases but is concave up, because its rates (-32, -16, -8, -4, -2) increase. In table g the x-values go up by 2, so each rate is the change in g divided by 2, not the change in g alone. Watch for "the rates are getting smaller" for k: the numbers get closer to 0, but -2 is greater than -32.
notes: Rates: f 3, 5, 7, 9, 11 (f(x) = x² + 2x + 2, concave up); g 18, 14, 10, 6, 2 (g(x) = 20x - x², concave down); h 5, 10, 20, 15, 5 (concave up, then down); k -32, -16, -8, -4, -2 (k(x) = 64(1/2)ˣ, concave up). An average rate on an interval is close to the slope near the interval's middle, so h's rates describe slopes near x = 0.5, 1.5, 2.5, 3.5 and 4.5. The slope grows to about x = 2.5 and is smaller by 3.5, so the inflection point is somewhere between them: accept any answer near x = 3. A table can only suggest concavity between its points; it cannot prove it.

## Warm up: What rates tell you
example: The rates 1, 4, 9 increase, so each piece of the graph is steeper than the last: the graph bends up (concave up, like a cup). Rates 9, 4, 1 decrease: the graph bends down (concave down, like a cap).
choice: The average rates of change of a function on three intervals in a row are -6, -4 and -1. On these intervals the function is
  - decreasing and concave down
  * decreasing and concave up
  - increasing and concave up
  - increasing and concave down
choice: A function has average rates of change 5, 5, 5 and 5 on four intervals in a row. Its graph is most likely
  - concave up
  - concave down
  * a straight line, with no concavity
  - curved, but we cannot tell which way

## Main: Four tables
text: **Table f.** Write each rate under the x where its interval starts.
table: x | 0 | 1 | 2 | 3 | 4 | 5
  - f(x) | 2 | 5 | 10 | 17 | 26 | 37
  - rate to the next x | {3} | {5} | {7} | {9} | {11} | none
fill: The rates are {increasing}, so f is concave {up} on 0 ≤ x ≤ 5.
text: **Table g.** Careful: the x-values go up by 2.
table: x | 0 | 2 | 4 | 6 | 8 | 10
  - g(x) | 0 | 36 | 64 | 84 | 96 | 100
  - rate to the next x | {18} | {14} | {10} | {6} | {2} | none
fill: The rates are {decreasing}, so g is concave {down} on 0 ≤ x ≤ 10.
text: **Table h.**
table: x | 0 | 1 | 2 | 3 | 4 | 5
  - h(x) | 10 | 15 | 25 | 45 | 60 | 65
  - rate to the next x | {5} | {10} | {20} | {15} | {5} | none
fill: h is concave {up} from x = 0 to about x = {3}, then concave {down} to x = 5.
text: **Table k.**
table: x | 0 | 1 | 2 | 3 | 4 | 5
  - k(x) | 64 | 32 | 16 | 8 | 4 | 2
  - rate to the next x | {-32} | {-16} | {-8} | {-4} | {-2} | none
fill: The rates are {increasing} (closer to 0), so k is concave {up}, even though k is {decreasing}.

## Main: Graph h
text: Plot the points of table h and sketch a smooth curve through them. Mark the point where the graph changes from concave up to concave down.
graph: x | 0 5 1 | h(x) | 0 70 10
  key: 0,10 1,15 2,25 3,45 4,60 5,65
  minor: off
fill: The inflection point is near x = {3}, where the graph is {steepest}.

## Stretch
write: Table h could show the number of members (in hundreds) of a new club over its first 5 months. Describe in words how the club grows, using the rates and the concavity.
  lines: 3
  key: The club grows slowly at first, then faster and faster (concave up) until about month 3, when it is growing fastest, about 2,000 members a month. After that it keeps growing but more and more slowly (concave down), as if it is filling up.

# 15. Ferris Wheel Timing
minutes: 40
materials: pencil, calculator (radian mode)
ican: I can model a Ferris wheel ride with a sinusoidal function and solve a trigonometric inequality to find when a rider is above a height.
pairs: ferris-wheel
directions: A Ferris wheel has a diameter of 36 meters, and its center is 21 meters above the ground. It turns at a steady speed and makes one full turn every 12 minutes. A rider boards at the lowest point at t = 0 minutes. Answer in exact form when you can, then as decimals.
mistakes: Students use sine because "trig graphs are sine," but a rider who starts at the bottom has height 21 - 18 cos(πt/6): a negative cosine starts at its minimum. Some find only t = 4 from the calculator and miss t = 8; the wheel passes 30 m twice each turn, once going up and once coming down. Watch for degree mode: πt/6 is in radians.
notes: The model is h(t) = 21 - 18 cos(πt/6): amplitude 18 (the radius), midline 21 (the center), period 12, so B = 2π/12 = π/6. h(t) > 30 means cos(πt/6) < -1/2, so 2π/3 < πt/6 < 4π/3, which gives 4 < t < 8 in each turn (and 16 < t < 20 in the second). In the stretch, cos(πt/6) < -7/9 gives πt/6 between arccos(-7/9) ≈ 2.4619 and 2π - 2.4619 ≈ 3.8213, so 4.70 < t < 7.30, about 2.60 minutes per turn. For the second rider, 21 + 18 sin(πt/6) > 30 means sin(πt/6) > 1/2, so 1 < t < 5. The Ferris Wheel tool lets students drag the car and watch the same graph grow.

## Warm up: Read the wheel
fill:
  - Lowest height: {3} m
  - Highest height: {39} m
  - Amplitude: {18} m
  - Midline: h = {21}
  - Period: {12} minutes
  - B in cos(Bt): {π/6}

## Main: Model the ride
fill: Because the rider starts at the bottom, h(t) = {21 - 18 cos(πt/6)}
table: t (minutes) | 0 | 1 | 2 | 3 | 4 | 5 | 6
  - h(t) (meters) | {3} | {5.41} | {12} | {21} | {30} | {36.59} | {39}
text: Graph h for two full turns. Then draw the line h = 30 and shade the times when the rider is above it.
graph: t (minutes) | 0 24 2 | h (meters) | 0 40 5
  key: 0,3 1,5.41 2,12 3,21 4,30 5,36.59 6,39 7,36.59 8,30 9,21 10,12 11,5.41 12,3 13,5.41 14,12 15,21 16,30 17,36.59 18,39 19,36.59 20,30 21,21 22,12 23,5.41 24,3
  key2: 0,30 24,30
  minor: off
fill: Solve h(t) = 30: cos(πt/6) = {-1/2}
fill: So πt/6 = {2π/3} or {4π/3}, and t = {4} or {8} minutes.
fill: In the first turn, the rider is above 30 m when {4 < t < 8}. In the second turn: {16 < t < 20}.
fill: Each turn, the rider is above 30 m for {4} minutes, which is {1/3} of the ride.
choice: Why is the time above 30 m centered on t = 6?
  - Because 30 m is the midline of the wheel
  * Because the rider is at the top at t = 6, and the wheel is symmetric
  - Because the period is 6 minutes
  - Because cosine is always largest at t = 6

## Stretch
write: The best view of the lake is above 35 m. During which times in the first turn is the rider above 35 m? How long is that each turn?
  lines: 3
  key: 21 - 18 cos(πt/6) > 35 means cos(πt/6) < -7/9. arccos(-7/9) ≈ 2.4619, so 2.4619 < πt/6 < 3.8213, which gives 4.70 < t < 7.30. That is about 2.60 minutes each turn.
write: A second rider boards at the 3 o'clock position (at the midline, moving up) at t = 0. Write her height function and find when she is above 30 m in her first turn.
  lines: 3
  key: h(t) = 21 + 18 sin(πt/6). h(t) > 30 means sin(πt/6) > 1/2, so π/6 < πt/6 < 5π/6, which gives 1 < t < 5 minutes. Still 4 minutes, just at a different time.

# 21. Trigonometry Review
minutes: 45
materials: pencil, scientific calculator, unit circle (optional)
ican: I can use identities, solve trigonometric equations, evaluate inverse trig functions and solve any triangle.
directions: Give exact answers unless a decimal is asked for. Solve equations on 0 ≤ x < 2π. Round side lengths to the nearest hundredth and angles to the nearest tenth of a degree. Set your calculator to degrees for Part D and radians where the problem uses π.
mistakes: Students lose solutions to equations by finding only the calculator's answer (2 sin x = 1 has two solutions in [0, 2π)). For inverse trig, the output must be in the principal range: arcsin(sin(5π/6)) is π/6, not 5π/6, and arctan(-√3) is -π/3. In the law of cosines, students forget that the -2ab cos C term changes sign for obtuse angles.
notes: The quadratic in cos x factors as (2 cos x + 1)(cos x - 1) = 0. For the 5-7-10 triangle, cos C = (25 + 49 - 100)/70 = -13/35. The ambiguous case: h = 10 sin 30° = 5 and 5 < 6 < 10, so two triangles exist (B ≈ 56.4° or 123.6°).

## Part A: Identities
fill: Simplify (1 - cos²θ)/sin θ = {sin θ}
fill: Simplify tan θ · cos θ = {sin θ}
fill: Find the exact value of cos 75° using cos(45° + 30°): {(√6 - √2)/4}
fill: If sin θ = 3/5 and θ is in quadrant I, then cos θ = {4/5} and sin 2θ = {24/25}
write: Verify the identity sec²θ - tan²θ = 1.
  lines: 3
  key: sec²θ - tan²θ = 1/cos²θ - sin²θ/cos²θ = (1 - sin²θ)/cos²θ = cos²θ/cos²θ = 1.

## Part B: Equations on 0 ≤ x < 2π
fill: 2 sin x - 1 = 0: x = {π/6, 5π/6}
fill: 2cos²x - cos x - 1 = 0: x = {0, 2π/3, 4π/3}
fill: tan x = -1: x = {3π/4, 7π/4}

## Part C: Inverse trig
fill: arcsin(1/2) = {π/6}
fill: arccos(-√2/2) = {3π/4}
fill: arctan(-√3) = {-π/3}
fill: sin(arccos(3/5)) = {4/5}
fill: arcsin(sin(5π/6)) = {π/6}

## Part D: Any triangle
fill: In triangle ABC, A = 40°, B = 65° and a = 10. Find b. b ≈ {14.10}
fill: a = 7, b = 9 and C = 60°. Find c. c = {√67 ≈ 8.19}
fill: A triangle has sides 5, 7 and 10. Find its largest angle. ≈ {111.8°}
fill: a = 8, b = 11 and C = 30°. Find the area. Area = {22} square units
choice: A = 30°, a = 6 and b = 10. How many triangles fit these measurements?
  - None
  - One
  * Two
  - Infinitely many

## Stretch
write: A surveyor at point P sights two trees on opposite sides of a pond. One tree is 120 m from P, the other is 150 m from P, and the angle between the sight lines is 48°. How far apart are the trees?
  lines: 3
  key: Law of cosines: d² = 120² + 150² - 2(120)(150) cos 48° = 14,400 + 22,500 - 36,000(0.66913) ≈ 36,900 - 24,088.7 = 12,811.3, so d ≈ 113.19 m.

# 26. Fix the Matrix Mistakes
minutes: 35
materials: pencil
ican: I can add, subtract, multiply by a scalar and multiply matrices, and tell when a sum or product is undefined.
directions: Matrices are written row by row: [1 2; 3 4] has first row 1 2 and second row 3 4, and [1; 2; 3] is one column. Each problem shows a student's work with a mistake. Say what went wrong, then write the correct answer, or write "undefined" if the sum or product cannot be done.
mistakes: The most common product error is multiplying entry by entry, as in the 2 × 2 product. Students also flag a product as undefined whenever the two matrices have different sizes; what matters is the inside dimensions: a 3 × 1 times a 1 × 2 is defined (3 × 2), while a 2 × 2 times a 1 × 3 is not. In the stretch, many expect BA = AB; matrix multiplication is not commutative.
notes: Products, row by column: the 2 × 2 product gives 1(5) + 2(7) = 19, 1(6) + 2(8) = 22, 3(5) + 4(7) = 43, 3(6) + 4(8) = 50. The 2 × 3 times 3 × 2 product: row 1 is 2(1) + 0(0) + (-1)(2) = 0 and 2(4) + 0(-1) + (-1)(3) = 5; row 2 is 1(1) + 3(0) + 2(2) = 5 and 1(4) + 3(-1) + 2(3) = 7. Stretch: AB = [3 3; 1 3] and BA = [2 2; 1 4]. Students can write the dimensions under each matrix first (2 × 3 and 3 × 2) and circle the inside pair.

## Warm up: Sizes first
fill:
  - A sum A + B is defined only when A and B {have the same dimensions}.
  - (2 × 3)(3 × 4) gives a {2 × 4} matrix.
  - (3 × 2)(3 × 2) is {undefined}.
  - (1 × 3)(3 × 1) gives a {1 × 1} matrix.
  - (3 × 1)(1 × 3) gives a {3 × 3} matrix.

## Main: Find and fix
write: [2 -1; 4 0] + [3 5; -2 6] = [5 4; 6 6]
  lines: 2
  key: Row 2, column 1 is wrong: 4 + (-2) = 2, not 6. Correct: [5 4; 2 6].
write: [7 3; 1 -2] - [4 -5; 6 1] = [3 -2; -5 -3]
  lines: 2
  key: Row 1, column 2: 3 - (-5) = 8; the student subtracted 5 instead. Correct: [3 8; -5 -3].
write: -3[2 -4; 0 5] = [-6 -12; 0 -15]
  lines: 2
  key: (-3)(-4) = 12, not -12: a sign error. Correct: [-6 12; 0 -15].
write: [1 2 3] + [1; 2; 3] = [2 4 6]
  lines: 2
  key: A 1 × 3 matrix and a 3 × 1 matrix have different dimensions, so the sum is undefined.
write: [1 2; 3 4][5 6; 7 8] = [5 12; 21 32]
  lines: 2
  key: The student multiplied entry by entry. Use rows times columns. Correct: [19 22; 43 50].
write: [2 0 -1; 1 3 2][1 4; 0 -1; 2 3] = [4 5; 5 7]
  lines: 2
  key: Row 1, column 1: 2(1) + 0(0) + (-1)(2) = 0; the student used +2 for (-1)(2). Correct: [0 5; 5 7].
write: [1 2; 3 4][1 2 3] = [1 2 3; 3 6 9]
  lines: 2
  key: A 2 × 2 times a 1 × 3: the inside dimensions (2 and 1) do not match, so the product is undefined.
write: [1; 2; 3][4 5] is undefined, because the matrices are not the same size.
  lines: 2
  key: Wrong: a 3 × 1 times a 1 × 2 has matching inside dimensions (1 and 1), so it is defined and is 3 × 2. Correct: [4 5; 8 10; 12 15].

## Stretch
text: A = [1 1; 0 1] and B = [2 0; 1 3]. A student found AB = [3 3; 1 3] and wrote "so BA = [3 3; 1 3] too."
fill: BA = {[2 2; 1 4]}
write: What does this show about matrix multiplication?
  lines: 2
  key: AB and BA can be different: matrix multiplication is not commutative, so the order of the factors matters.

# 36. Slice the Cone
minutes: 30
materials: pencil
ican: I can name the conic section made when a plane slices a double cone, and sketch it.
directions: Each picture shows a double cone from the side. The thick line is a flat plane seen edge-on, cutting through the cone. Name the curve the plane makes, then sketch that curve as you would see it looking straight at the plane.
mistakes: Students call slice 4 a hyperbola because the plane is steep. A plane parallel to one side of the cone cuts only one nappe and makes one open branch: a parabola. A hyperbola needs the plane to cut both nappes, which makes two branches. Some draw the ellipse as a circle; only a plane perpendicular to the axis makes a circle.
notes: Slice 1 is tilted but less steep than the side of the cone: ellipse. Slice 2 is vertical, parallel to the axis, and cuts both nappes: hyperbola (two branches). Slice 3 is perpendicular to the axis: circle. Slice 4 is parallel to the right-hand side of the cone: parabola. If you have a cone of clay or foam, cut it with dental floss to show each slice. The degenerate conics in the stretch come from planes through the vertex.

## Warm up: Parts of a double cone
fill:
  - The point where the two cones meet is the {vertex}.
  - Each of the two cones is called a {nappe}.
  - The line through the vertex, down the middle of both cones, is the {axis}.

## Main: Name each slice
picword:
  - cone-slice-ellipse | 1. {ellipse}
  - cone-slice-hyperbola | 2. {hyperbola}
  - cone-slice-circle | 3. {circle}
  - cone-slice-parabola | 4. {parabola}
table: Slice | How the plane meets the cone | How many nappes it cuts
  - 1 | {tilted, less steep than the side} | {1}
  - 2 | {parallel to the axis} | {2}
  - 3 | {perpendicular to the axis} | {1}
  - 4 | {parallel to one side} | {1}
chart: Slice 1 | Slice 2 | Slice 3 | Slice 4
  rows: 1
  height: 1.3
  key: 1: a closed oval. 2: two separate open branches that open away from each other. 3: a round closed curve. 4: one open U-shaped branch.
match: Match each conic to its equation.
  - circle = x² + y² = 16
  - ellipse = x²/25 + y²/9 = 1
  - parabola = y = x² - 3
  - hyperbola = x²/9 - y²/16 = 1

## Stretch: Through the vertex
write: Now the plane passes through the vertex. What does it make if the plane is (a) perpendicular to the axis, (b) along one side of the cone, (c) parallel to the axis?
  lines: 3
  key: (a) a single point, (b) a single line, (c) two lines that cross at the vertex. These are the degenerate conics.
