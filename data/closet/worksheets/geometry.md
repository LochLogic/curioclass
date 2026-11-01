# 1. Transformations as Functions
minutes: 35
materials: pencil, graph paper (optional)
ican: I can apply a transformation as a rule that maps points to points and decide whether it preserves distance and angle.
directions: A transformation is a function: it takes a point (x, y) as input and gives a new point as output. Apply each rule to A(1, 1) and B(4, 5), find the length of A'B', and decide whether the rule keeps distances and angles the same. The original length AB is 5.
mistakes: Students mix up (x, y) → (-y, x) and (x, y) → (y, -x): substitute carefully, writing the input values first. Many students say the dilation keeps angles and distances; it keeps angles but doubles distances. For the stretch and the shear, one example is enough to show distance changes, but students should check a triangle to see the angles change too.
notes: Length check: AB = √(3² + 4²) = 5. Rules 1 to 5 are rigid motions (translation, reflection in the y-axis, reflection in y = x, rotation 90° counterclockwise, rotation 180°). Rule 6 is a dilation with scale factor 2: angles stay, distances double. Rule 7 stretches vertically: with C(1, 5), the right angle at C stays, but angle A changes from about 37° to about 14°. Rule 8 is a shear: angle C of triangle ABC changes from 90° to 135°.

## Warm up
fill:
  - (x, y) → (x - 4, y + 1) maps (6, 2) to {(2, 3)}
  - (x, y) → (x, -y) maps (-3, 5) to {(-3, -5)}
  - (x, y) → (2x, y) maps (3, -1) to {(6, -1)}

## Main: Apply each rule
table: Rule | A' | B' | Length A'B' | Keeps distance? (Y or N) | Keeps angles? (Y or N)
  - (x, y) → (x + 3, y - 2) | {(4, -1)} | {(7, 3)} | {5} | {Y} | {Y}
  - (x, y) → (-x, y) | {(-1, 1)} | {(-4, 5)} | {5} | {Y} | {Y}
  - (x, y) → (y, x) | {(1, 1)} | {(5, 4)} | {5} | {Y} | {Y}
  - (x, y) → (-y, x) | {(-1, 1)} | {(-5, 4)} | {5} | {Y} | {Y}
  - (x, y) → (-x, -y) | {(-1, -1)} | {(-4, -5)} | {5} | {Y} | {Y}
  - (x, y) → (2x, 2y) | {(2, 2)} | {(8, 10)} | {10} | {N} | {Y}
  - (x, y) → (x, 3y) | {(1, 3)} | {(4, 15)} | {√153} | {N} | {N}
  - (x, y) → (x + y, y) | {(2, 1)} | {(9, 5)} | {√65} | {N} | {N}
fill: Name rules 1 to 5: translation, reflection in the y-axis, reflection in the line {y = x}, rotation of {90}° counterclockwise about the origin, rotation of {180}° about the origin.
fill: The rules that keep both distance and angle are called {rigid motions}.

## Stretch
write: Write a rule for a rotation of 90° clockwise about the origin. Test it on A and B and show that A'B' = 5.
  lines: 3
  key: (x, y) → (y, -x). A(1, 1) → (1, -1) and B(4, 5) → (5, -4). A'B' = √((5 - 1)² + (-4 + 1)²) = √(16 + 9) = 5.
write: Use triangle ABC with C(1, 5) (a right angle at C) to show that the rule (x, y) → (x + y, y) does not keep angles.
  lines: 3
  key: A' = (2, 1), B' = (9, 5), C' = (6, 5). From C', the vectors to A' and B' are (-4, -4) and (3, 0); they are not perpendicular (their dot product is -12, not 0), so the 90° angle became 135°.

# 5. Congruence Criteria Card Sort
minutes: 35
materials: pencil, scissors, glue
ican: I can decide which congruence criterion, if any, proves two triangles congruent.
directions: Each card describes the marks on a pair of triangles, △ABC and △DEF unless the card names others. Sketch the pair if it helps. Cut out the cards and sort them into six piles on your desk, one for each criterion that proves the triangles congruent, plus "Not enough". Then record the letters in the table. You may glue each pile into your notebook.
mistakes: The most common error is sorting by what is listed instead of where it sits: an angle must be between the two sides for SAS, and a side must be between the two angles for ASA. Two sides and an angle that is not between them (SSA) is not enough, and neither are three angles (AAA). Students also miss marks that come free from the figure: a shared side, vertical angles and right angles.
notes: SSS: G (three pairs of sides) and D (the kite, with shared side AC). SAS: B and H (in H, AM ≅ DM and BM ≅ CM, and the vertical angles at M are the included angle). ASA: E and J (shared side AB with both angles at its ends). AAS: L and F (in F, BC is not between the right angle at C and ∠A). HL: A and K (isosceles triangle with altitude AD). Not enough: C (AAA) and I (SSA). In the main part, accept any correct order of the matching letters, such as △ABC ≅ △DEF.

## Cut out the cards
cards: Cut out the 12 cards on the dashed lines.
  plain: yes
  - **A.** Right angles at C and F, hypotenuse AB ≅ DE, leg AC ≅ DF
  - **B.** AB ≅ DE, ∠B ≅ ∠E, BC ≅ EF
  - **C.** ∠A ≅ ∠D, ∠B ≅ ∠E, ∠C ≅ ∠F
  - **D.** Kite ABCD: AB ≅ AD and CB ≅ CD (△ABC and △ADC share AC)
  - **E.** ∠A ≅ ∠D, AB ≅ DE, ∠B ≅ ∠E
  - **F.** Right angles at C and F, ∠A ≅ ∠D, BC ≅ EF
  - **G.** AB ≅ DE, BC ≅ EF, AC ≅ DF
  - **H.** Segments AD and BC cross at M, the midpoint of both (△AMB and △DMC)
  - **I.** AB ≅ DE, BC ≅ EF, ∠A ≅ ∠D
  - **J.** △ABC and △ABD share AB, with ∠CAB ≅ ∠DAB and ∠CBA ≅ ∠DBA
  - **K.** In △ABC, AB ≅ AC and AD ⊥ BC (△ABD and △ACD)
  - **L.** ∠A ≅ ∠D, ∠B ≅ ∠E, BC ≅ EF

## Main: Sort the cards
table: Criterion | Card letters | One thing to check for this criterion
  - SSS | {D, G} | {three pairs of sides, including any shared side}
  - SAS | {B, H} | {the angle is between the two sides}
  - ASA | {E, J} | {the side is between the two angles}
  - AAS | {F, L} | {the side is not between the two angles}
  - HL | {A, K} | {right triangles with the hypotenuses and one leg congruent}
  - Not enough | {C, I} | {only angles (AAA), or an angle not between the sides (SSA)}
  height: 0.5

## Main: Explain three cards
fill: In card D, the third pair of sides is AC ≅ AC because the triangles {share side AC}.
fill: In card H, the pair of angles comes from {vertical angles} at M.
fill: In card K, the hypotenuses are AB and {AC}, and the shared leg is {AD}.

## Stretch
write: Draw two different triangles that have AB ≅ DE, BC ≅ EF and ∠A ≅ ∠D. What does this show about SSA?
  lines: 3
  key: With angle A and side AB fixed, a side of length BC can swing to meet the third side in two places, making one acute and one obtuse triangle. The two triangles match in SSA but are not congruent, so SSA is not a congruence criterion.
write: Why is AAA not enough? Give an example.
  lines: 2
  key: Equal angles fix the shape but not the size. A triangle with sides 3, 4, 5 and one with sides 6, 8, 10 have the same angles but are not congruent (they are similar).

# 16. Ratios Stay the Same
minutes: 35
materials: pencil, calculator
ican: I can show that side ratios in similar right triangles depend only on the angle, which defines sine, cosine and tangent.
directions: The grid shows four right triangles that share the angle A at (1, 1). Each has its right angle on the bottom line and its top vertex on the slanted line. Count grid units to measure the legs, find the hypotenuse with the Pythagorean theorem, and compute the three ratios for angle A.
mistakes: Students mix up opposite and adjacent: for angle A, the opposite leg is the vertical side across from A, and the adjacent leg is the horizontal side next to A. Some count grid lines instead of spaces (the smallest triangle's base is 2, not 3). Rounding early hides the pattern, so keep exact decimals.
notes: Triangle 1: legs 1.5 and 2, hypotenuse 2.5. Triangle 2: 3, 4, 5. Triangle 3: 4.5, 6, 7.5. Triangle 4: 6, 8, 10. Every triangle gives opposite/hypotenuse = 0.6, adjacent/hypotenuse = 0.8 and opposite/adjacent = 0.75. Angle A is about 36.87°; a calculator gives sin 37° ≈ 0.602, cos 37° ≈ 0.799 and tan 37° ≈ 0.754, close to the measured ratios. The stretch shows the ratios change when the angle changes (tan 45° = 1).

## Warm up
fill:
  - Triangles with the same angles are {similar}, so their sides are proportional.
  - In a right triangle, the side across from the right angle is the {hypotenuse}.

## Main: Measure
graph: x | 0 17 1 | y | 0 9 1
  minor: off
  line: 3,1 3,2.5 1,1 9,1 9,7 7,5.5 7,1 7,5.5 5,4 5,1 5,4 3,2.5
table: Triangle (right angle at) | Opposite leg (vertical) | Adjacent leg (horizontal) | Hypotenuse | Opposite ÷ hypotenuse | Adjacent ÷ hypotenuse | Opposite ÷ adjacent
  - 1 (3, 1) | {1.5} | {2} | {2.5} | {0.6} | {0.8} | {0.75}
  - 2 (5, 1) | {3} | {4} | {5} | {0.6} | {0.8} | {0.75}
  - 3 (7, 1) | {4.5} | {6} | {7.5} | {0.6} | {0.8} | {0.75}
  - 4 (9, 1) | {6} | {8} | {10} | {0.6} | {0.8} | {0.75}

## Main: What do you notice?
fill:
  - Each ratio is {the same} in all four triangles, even though the triangles have different sizes.
  - Opposite ÷ hypotenuse is called the {sine} of angle A.
  - Adjacent ÷ hypotenuse is called the {cosine} of angle A.
  - Opposite ÷ adjacent is called the {tangent} of angle A.
  - With a calculator, sin 37° ≈ {0.60}, cos 37° ≈ {0.80} and tan 37° ≈ {0.75}. So angle A is about 37°.

## Stretch
write: Find the three ratios for the other acute angle of triangle 2, the angle at its top vertex (5, 4). How do they compare with angle A's ratios?
  lines: 3
  key: For the top angle, the opposite leg is 4 and the adjacent leg is 3: sine 4/5 = 0.8, cosine 3/5 = 0.6, tangent 4/3 ≈ 1.33. Its sine is angle A's cosine and its cosine is angle A's sine, because the two angles add to 90°.
write: A right triangle has legs of 4 and 4. Is its opposite ÷ adjacent ratio 0.75? What does this tell you?
  lines: 2
  key: No, 4 ÷ 4 = 1. Its acute angles are 45°, not 37°. The ratios depend on the angle: a different angle gives different ratios.

# 22. Chords, Secants and Tangents
minutes: 35
materials: pencil, compass (optional)
ican: I can find unknown segment lengths in a circle using the relationships among chords, secants and tangents.
directions: Read each description, sketch and label the circle in the box, then write an equation and solve. A secant from an outside point P meets the circle at a near point and a far point.
mistakes: In secant problems students multiply the outside part by the inside part instead of by the whole secant: PA · PB uses the outside piece and the whole length. When a problem gives the inside piece (items 10 and 12), add it to the outside piece first. For a tangent, the tangent length is squared because it is "outside part times whole" with both equal.
notes: The diagrams are given as descriptions so students practice sketching; a quick sketch with labels is part of the work. The formulas: intersecting chords AE · EB = CE · ED; two secants PA · PB = PC · PD; tangent and secant PT² = PA · PB; two tangents from one point are equal; a radius to the point of tangency is perpendicular to the tangent; the perpendicular bisector of a chord passes through the center. The fix-it is item 10 solved without distributing.

## Warm up: Which rule?
match: Match each diagram to its rule.
  - Two chords AB and CD cross at E inside the circle = AE · EB = CE · ED
  - Two secants from P meet the circle at A, B and at C, D = PA · PB = PC · PD
  - A tangent PT and a secant from P through A and B = PT² = PA · PB
  - Two tangents from P touch the circle at T and S = PT = PS
  - A radius OT drawn to the point where tangent PT touches = OT ⊥ PT
  - The perpendicular bisector of any chord = passes through the center O

## Main: Find the length
fill: Chords AB and CD cross at E. AE = 6, EB = 4, CE = 3, ED = x. x = {8}
draw: Sketch | 1.3
fill: Chords AB and CD cross at E. AE = x, EB = 10, CE = 5, ED = 8. x = {4}
draw: Sketch | 1.3
fill: Two secants from P. Secant 1: PA = 4 outside, PB = 12 whole. Secant 2: PC = 6 outside, PD = x whole. x = {8}
draw: Sketch | 1.3
fill: Two secants from P. Secant 1: PA = 5 outside and AB = 7 inside. Secant 2: PC = 4 outside and CD = x inside. x = {11}
draw: Sketch | 1.3
fill: Tangent PT = x. Secant from P: PA = 4 outside, PB = 16 whole. x = {8}
draw: Sketch | 1.3
fill: Tangent PT = 12. Secant from P: PA = 8 outside, AB = x inside. x = {10}
draw: Sketch | 1.3

## Stretch
fixit: 5(12) = 4(4 + x)
  * 60 = 16 + x
  - x = 44
  answer: x = 11
  why: The 4 must multiply both 4 and x: 60 = 16 + 4x, so 4x = 44 and x = 11.
write: Two tangents from P touch a circle at T and S. PT = 3x + 2 and PS = 5x - 6. Find x and the length of each tangent.
  lines: 2
  key: Tangents from one point are equal: 3x + 2 = 5x - 6, so 2x = 8 and x = 4. PT = PS = 14.

# 27. Parabola From Focus and Directrix
minutes: 40
materials: pencil, ruler
ican: I can derive the equation of a parabola from its focus and directrix and graph it.
directions: Every point (x, y) on a parabola is the same distance from the focus (the dot) as from the directrix (the heavy line). Set the two distances equal, square both sides and simplify. Then plot at least five points and sketch each parabola.
mistakes: Students often forget to square the whole difference ((y - 2)² = y² - 4y + 4, not y² + 4). The distance to a horizontal directrix y = k is |y - k|, not a distance formula with x. Watch the direction: the parabola opens toward the focus and away from the directrix. For parabola 3 the directrix is vertical, so the distance is |x + 2| and the parabola opens right.
notes: 1) √(x² + (y - 2)²) = |y + 2| gives x² = 8y, or y = x²/8; vertex (0, 0). 2) √((x - 1)² + (y - 1)²) = |y - 5| gives (x - 1)² = -8(y - 3), or y = -(1/8)(x - 1)² + 3; vertex (1, 3), opens down. 3) √((x - 2)² + y²) = |x + 2| gives y² = 8x, or x = y²/8; vertex (0, 0), opens right. In each case the vertex is halfway between the focus and the directrix, and p = 2 (the focus-to-vertex distance), so 4p = 8.

## Parabola 1: Focus (0, 2), directrix y = -2
graph: x | -8 8 2 | y | -2 8 2
  show: 0,2
  line2: -8,-2 8,-2
  key: -8,8 -6,4.5 -4,2 -2,0.5 0,0 2,0.5 4,2 6,4.5 8,8
fill: Equation: {x² = 8y, or y = x²/8}

## Parabola 2: Focus (1, 1), directrix y = 5
graph: x | -8 10 2 | y | -6 6 2
  show: 1,1
  line2: -8,5 10,5
  key: -7,-5 -5,-1.5 -3,1 -1,2.5 1,3 3,2.5 5,1 7,-1.5 9,-5
fill: Equation: {(x - 1)² = -8(y - 3), or y = -(1/8)(x - 1)² + 3}

## Parabola 3: Focus (2, 0), directrix x = -2
graph: x | -4 10 2 | y | -8 8 2
  show: 2,0
  line2: -2,-8 -2,8
  key: 8,-8 4.5,-6 2,-4 0.5,-2 0,0 0.5,2 2,4 4.5,6 8,8
fill: Equation: {y² = 8x, or x = y²/8}
draw: Show your derivations | 2.1

## Stretch
write: Without deriving, write the equation of the parabola with focus (0, 5) and directrix y = -5. Explain the pattern you used.
  lines: 2
  key: x² = 20y. The vertex is halfway, at (0, 0), and p = 5, so x² = 4py = 20y.

# 38. Pocket Park Design
minutes: 50
materials: pencil, ruler, compass, calculator
ican: I can use area, length and circle formulas to design a space that meets several constraints.
directions: The town has an empty lot 30 m long and 16 m wide for a pocket park. First work out the numbers the rules depend on. Then draw your park on the grid (each small square is 1 m by 1 m), and show that your design meets every rule.
mistakes: Students often count a tree's shade as its diameter squared or use the diameter in A = πr². Four trees give only about 113 square meters of shade, short of the 120 needed. Path length is measured along the middle of the path, and its area is length × 2 m. Crowns that overlap or hang past the lot edge do not count fully.
notes: Fixed numbers: lot 480 m²; shade needed 25% of 480 = 120 m²; one crown 9π ≈ 28.3 m²; 4 trees ≈ 113.1 m² (not enough), 5 trees ≈ 141.4 m², about 29% of the lot. Paving budget $3,600 ÷ $45 = 80 m² of path, so the 2 m path can be at most 40 m long. Designs will differ: grade by the rubric (every rule checked with a calculation, a neat labeled plan, and a reason for each choice). A model design: a straight path from (0, 8) to (30, 8), 30 m long, 60 m², $2,700; a 6 m by 8 m playground at x = 2 to 10, y = 10 to 16; trees centered at (4, 4), (11, 4), (18, 4), (25, 4) and (22, 13); the rest is lawn, well over 120 m².

## The rules
text: 1) A path 2 m wide runs from the gate in the middle of the left side, at (0, 8), to the right side. 2) The path's paving costs $45 per square meter, and the budget for paving is $3,600. 3) A rectangular playground has an area of at least 48 m². 4) Trees each have a round crown with a radius of 3 m. Crowns stay inside the lot and do not overlap. Tree shade must cover at least 25% of the lot. 5) Lawn covers at least 120 m².

## Part A: The numbers
fill:
  - Area of the lot: {480} m²
  - Shade needed (25% of the lot): {120} m²
  - Shade from one tree crown, to the nearest tenth: {28.3} m²
  - The fewest trees that meet the shade rule: {5}
  - The most path the budget can pave: {80} m², so the longest the path can be is {40} m

## Part B: Draw your park
graph: Meters | 0 30 2 | Meters | 0 16 2
text: Draw the path, the playground, each tree crown (use a compass) and the lawn. Label each part.

## Part C: Check every rule
table: Rule | My numbers (show the calculation) | Met? (Y or N)
  - Path length and area | {model: 30 m long, 30 × 2 = 60 m²} | {Y}
  - Paving cost | {model: 60 × $45 = $2,700 ≤ $3,600} | {Y}
  - Playground area | {model: 6 × 8 = 48 m²} | {Y}
  - Tree shade | {model: 5 × 28.3 = 141.4 m², 29% of 480} | {Y}
  - Lawn area | {model: 480 - 60 - 48 = 372 m², with the trees standing in the lawn} | {Y}
  height: 0.5

## Stretch
write: The town adds a rule: no spot on the path may be more than 10 m from a bench. Where would you put benches, and how many do you need? Explain.
  lines: 3
  key: Possible answer: along a straight 30 m path, benches at 10 m and 20 m cover every spot within 10 m (0 to 20 m and 10 to 30 m), so 2 benches are enough. A curved or longer path may need more.
