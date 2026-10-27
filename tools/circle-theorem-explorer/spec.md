# Circle Theorem Explorer

## One idea
Every circle theorem is something that refuses to change: drag any point and every number on the figure moves
except one locked relationship (an inscribed angle stays half its arc, a tangent stays square to its radius), and a
`Break it` button shows the one move that makes the rule stop holding, so you learn what each theorem actually
depends on.

## Not like
- proof-blocks, now Proof Tower (gr 10, this group): writes proofs with statements and reasons. Here nothing is written; you watch what stays fixed and what breaks it.
- coordinate-proof-lab (gr 10, this group): proves properties by computing slopes and lengths on a grid. Here no coordinates; angles and arcs only.
- cone-slicer, now Conic Focus Finder (gr 12 explorer): curves traced by distance rules. Here the circle is given and the theorems live on it.
- polar-rose-studio (gr 12 studio): angle as input to a curve. Here radians are an arc length divided by a radius.
- ferris-wheel (gr 11 simulator): a point going round as a sine wave over time. Here no time; the figure is still until you drag.

## Who and how
- Grade 10, Geometry, module Circles. Students drive, own laptops or pairs; also works on a projector. 10 to 35 minutes.
- Topic line: "circle theorems, arcs and radians".
- Standards (module): G-C.A (all circles are similar; inscribed angles, radii, chords, tangents; inscribed and
  circumscribed circles; cyclic quadrilaterals), G-C.B (arc length is proportional to the radius; radian measure;
  sector area).
- CCSS clusters: cards 1 to 7 serve G-C.A.2, card 8 serves G-C.A.3, card 9 serves G-C.A.1, cards 10 and 11 serve
  G-C.B.5. Card 6 (equal tangents) also touches G-C.A.4 (+).
- tool.json: driver "students or teacher", minutes "10-35", modes [] (one explorer with optional Predict),
  grades_label "Grade 10".

## Screens and modes
Header (kit, 9-12 theme): title "Circle Theorem Explorer", subtitle "Drag anything. One thing won't move." Kit
buttons `Motion`, `Sound`, `Read`.
Layout: stage left (one large circle and its figure, drawn at real pixel size), panel right (card list, layers,
readouts). Under 1000 px wide the panel goes under the stage with the card list as a horizontal strip. Under 900 px
tall the card list becomes a dropdown so the figure and the locked line stay in view.

- Card list (panel), grouped: Angles (1 to 3, 5), Lines (4, 6, 7), Triangles (8), Size (9 to 11). Choosing a card
  loads its figure.
- Figure: draggable points are solid dots with 44 px targets; fixed points are small rings. Measures are drawn on
  the figure (angle arcs with their values, segment lengths, arc measures in small labels outside the circle).
- The locked line (top of the panel, large): the card's relationship with today's numbers, for example "∠ACB = 60°,
  half of arc AB = 120°". It has a lock glyph while the rule holds.
- Layers (toggles under the readouts, any mix): `Measures`, `Arcs`, `Why` (draws the helper lines a proof uses, such
  as the radius to C that splits the figure into two isosceles triangles, with one sentence of reason), `Ghosts`
  (leaves faint copies of the last five drags so you can see many positions at once).
- `Break it`: animates the one move that breaks the rule (Content), the lock opens, the locked line turns warn with
  words ("Not half any more: the vertex left the circle"). `Fix it` puts the point back where the rule holds.
- `Predict` (optional, per card): hides the locked value; type your prediction, then `Check` reveals it. Correct
  within the snap step leaves a small check on the card for this session.
- `Snap to 1°` (on by default): points on the circle move in 1° steps around it, so every arc is a whole number of
  degrees and every inscribed angle is a whole or half degree, and readouts are exact. Off: readouts to 0.1° and the
  locked line says "equal to within 0.1°".

## Content
Positions are given as degrees around the circle (0° at the right, counterclockwise), radius 4 units unless said.
1. Inscribed angle and central angle. A at 200°, B at 320°, C draggable on the major arc (start 80°). Locked:
   ∠ACB = half the central angle AOB. Start: central 120°, inscribed 60°. Break it: C slides off the circle inward
   to 60% of the radius (angle grows past half). Euclid III.20.
2. Same arc, same angle. A, B as card 1; C at 80° and D at 140°, both draggable. Locked: ∠ACB = ∠ADB (60° and 60°).
   Break it: D crosses to the minor arc (its angle becomes 180° − 60° = 120°). Euclid III.21.
3. Angle in a semicircle. A at 180°, B at 0° (a diameter), C draggable. Locked: ∠ACB = 90°. Break it: B moves to
   340°, so AB is no longer a diameter (∠ACB becomes half of 160° = 80°, or 100° on the other side). Euclid III.31.
4. Tangent and radius. Point T draggable on the circle; the tangent line at T. Locked: the radius OT meets the
   tangent at 90°. Break it: the line tilts 15° about T and now cuts the circle at a second point (a secant), angle
   75°. Euclid III.18.
5. Cyclic quadrilateral. Vertices at 30°, 110°, 200°, 290° (all draggable). Locked: opposite angles add to 180°.
   Start: 90° + 90° = 180° and 95° + 85° = 180°. Break it: one vertex moves outside the circle. Euclid III.22.
6. Two tangents from a point. External point P draggable (5 units from O at start, radius 3). Locked: PT₁ = PT₂.
   Start: both 4.00 (a 3-4-5 right triangle with the radius). Break it: one line rotates off tangency (now a secant).
   Follows from Euclid III.36.
7. Crossing chords. A at 20°, B at 170°, C at 100°, D at 250°; chords AB and CD cross at E. Locked: AE × EB =
   CE × ED. Start: both 14.17. Break it: E is moved off chord CD (D slides off the circle), products differ. Euclid
   III.35.
8. Circles of a triangle. △ABC draggable. Layer choice `Around` (perpendicular bisectors meet at the circumcenter;
   one circle through all three vertices) and `Inside` (angle bisectors meet at the incenter; one circle touching all
   three sides). Locked: the three lines meet at one point. Break it: one bisector is swapped for a median (three
   points of crossing appear). Euclid IV.4 and IV.5.
9. All circles are similar. Two circles, radii 2 and 5, draggable centers and radius handles. `Match`: slide the
   small circle's center onto the big one's (a translation), then dilate by 5 ÷ 2 = 2.5 about that center; it lands
   exactly. Locked: "a slide then a dilation by k = r₂ ÷ r₁ carries one onto the other". Break it: replace the second
   circle with an ellipse (no dilation matches; the readout says so).
10. Radians. Radius slider 1 to 5 (step 0.5), angle θ draggable. `Unroll` lays the arc straight along the radius
   as a string. Locked: arc length ÷ radius = θ in radians. Start r = 3, θ = 60°: arc 3.14, 3.14 ÷ 3 = 1.047 = π/3.
   At r = 5, 60°: arc 5.24, ratio still 1.047. A full turn is 2π = 6.283 radii of string. Break it: "measure" the arc
   with a straight chord instead (chord ÷ radius changes as θ grows, no longer proportional).
11. Sector area. Same controls. Locked: sector area = (θ ÷ 360°) × πr² = ½r²θ. Start r = 3, θ = 60°: 4.71
   (= 3π/2). Break it: the slice is cut along the chord (a segment, not a sector; area smaller).
Every Why layer sentence (one each): card 1 "OC splits it into two isosceles triangles; each outside angle is twice
its base angle." 2 "Both are half the same central angle." 3 "Half of a 180° arc." 4 "Any other point of the line
is farther from O than T." 5 "The two angles stand on arcs that make the whole circle." 6 "Two right triangles share
OP and a radius." 7 "Triangles AEC and DEB are similar." 8 "Every point on a perpendicular bisector is the same
distance from both ends." 9 "A dilation scales every radius by the same factor." 10 "Similar circles: arcs scale with
the radius." 11 "The sector is θ ÷ 360° of the whole disk."

## Interactions in detail
- Angles are computed from point positions with atan2 and shown to 0.1°; with Snap on they are exact halves.
  Lengths to two decimals; products in card 7 are computed from unrounded lengths, so both products always print the
  same digits while the rule holds.
- A point on the circle can't be dragged onto another point (it stops 2° short). Card 3's C can't sit on A or B
  (no triangle): it stops 1° short. Card 6's P can't enter the circle (it stops at 1.05 × radius, where tangents
  still exist); the readout explains "Inside the circle there are no tangents".
- `Break it` and `Fix it` animate over 600 ms (instant with Motion off) and can be repeated; dragging after a break
  keeps the broken state until `Fix it` or a card change.
- Predict checks within 0.5° (Snap on) or 0.1 (lengths). Wrong: "Not quite. Drag a point and watch the locked line."
- Keyboard: Tab through draggable points (panel controls first), arrow keys move a point 1° along the circle (or
  0.1 unit off it), aria-valuetext "C at 80 degrees; angle ACB 60 degrees".
- Reset: `Reset card`; card states last for the page session; nothing is saved.
- `window.__tool = {state, card(n), move(point, deg), breakIt(), fixIt(), locked()}`.

## Look
Accent `--brand #b8b0d8` (dusk lavender), `--brand-ink #10161f`. Stage: a night observatory dome `#0e1220`, the
circle `#e8edf3` 2 px, measures `#a6b3c4`, the locked angle or segment filled with the accent at 35% and outlined
in the accent, broken state `#ffb8a8` dashed plus words.
Contrast (computed): brand on --panel 8.44:1, on --sec-bg 8.00:1, on the dome 9.09:1; brand-ink on brand 8.85:1;
measures on the dome 8.76:1. Greyer than algebra-tile-studio's #6cc4ff and exponent-rule-builder's #a5a8ff; no
9-12 math tool uses a muted lavender.

## Art
none: drawn in code (circles, figures, layers, preview.svg).

## Voice
Bank voice `soft-breath`, style "soft and unhurried, like a quiet guide in a planetarium". No 9-12 math tool uses
it. `Curio.voice`; one scope (the card), `welcomeAfter: true` (one mode).
- welcome (how): "Pick a card and drag any point. Watch the line at the top. It stays true."
- breakHow (how, first card change after the welcome): "When you are ready, tap Break it to see what the rule needs."
- predictHow (how, first Predict opened): "Type your guess, then tap Check."
- broke (event, Break it finishes; stale on Fix it or card change): "Now it breaks. Look at what moved."
- fixed (event, Fix it finishes; stale on card change): "Back on the circle. The rule holds again."
- unrolled (event, Unroll finishes on card 10; stale when the radius or angle changes): "The arc, laid straight. Count how many radii it takes."

## Family engine
none.

## Sources
- G-C text: Common Core State Standards for Mathematics, High School Geometry, Circles, https://www.thecorestandards.org/Math/Content/HSG/C/
- Theorems (III.18 tangent, III.20 central and inscribed, III.21 same segment, III.22 cyclic quadrilateral, III.31 semicircle, III.35 crossing chords, III.36 tangent and secant, IV.4 inscribed circle, IV.5 circumscribed circle): Euclid's Elements, D. E. Joyce edition, Clark University, https://mathcs.clarku.edu/~djoyce/java/elements/bookIII/bookIII.html
- Radians and sector area: OpenStax, Algebra and Trigonometry 2e, 7.1 "Angles", https://openstax.org/books/algebra-and-trigonometry-2e/pages/7-1-angles
- Every start value above was recomputed in Python (2026-10-27).

## Done when
1. Card 1 at the start shows 120° and 60°; dragging C anywhere on the major arc keeps 60° with the lock; Break it opens the lock with a larger angle.
2. Card 2: D on the minor arc shows 120°, and the locked line says the rule needs both on the same arc.
3. Card 3: ∠ACB reads 90.0° for every C; after Break it (B at 340°) it reads 80.0° or 100.0°.
4. Card 5 start: 90 + 90 and 95 + 85, both 180.
5. Card 6 start: both tangents 4.00; P can't be dragged inside the circle.
6. Card 7 start: both products 14.17.
7. Card 10: r = 3 and r = 5 at 60° give arcs 3.14 and 5.24, ratio 1.047 each; card 11 gives 4.71 at r = 3.
8. Keyboard alone can drag every point; with Snap off the locked line says "within 0.1°"; every size in STANDARDS.md keeps the figure and the locked line visible without page scrolling.
9. Console clean, no network, no em dashes, "Curio Class" only in full.

## Open questions
- none.
