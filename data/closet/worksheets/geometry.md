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
