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
