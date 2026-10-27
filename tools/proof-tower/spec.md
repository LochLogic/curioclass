# Proof Tower
Renamed from: Proof Blocks

## One idea
A proof is a tower you stack: each statement is a block, and a block locks in place only when you give it a reason
and every statement that reason needs is already a locked block below it, so a gap in the logic is a block you can
see wobbling, and each theorem you finish becomes a new reason card for the next tower.

## Not like
- equation-golf (gr 9 puzzle): legal moves on one equation, counted like golf strokes. Here nothing is counted; each block needs support from below.
- rigid-motion-twins (gr 10, this group): a congruence proof is a list of slides, turns and flips. Here proofs are statements and reasons, and congruent triangles come from SSS, SAS and ASA cards.
- coordinate-proof-lab (gr 10, this group): proofs by measuring slopes and lengths on a grid. Here no coordinates and no measuring; the diagram is never to be trusted, only the reasons.
- circle-theorem-explorer (gr 10, this group): watches theorems hold while you drag. Here you prove them.
- exponent-rule-builder (gr 9 puzzle): rules found by climbing a power ladder; no proof structure.
- identity-proof-race (gr 12, not specced yet): timed trig identity proofs. Here untimed, synthetic geometry.

## Who and how
- Grade 10, Geometry, module Proofs and Constructions. Students drive, own laptops or pairs. 20 to 45 minutes.
- Topic line: "geometry proofs and constructions".
- Standards (module): G-CO.C (prove theorems about lines and angles, triangles, parallelograms), G-CO.D (make
  formal constructions with compass and straightedge).
- CCSS clusters: Tower levels 1, 2, 5 serve G-CO.C.9; levels 3, 4 serve G-CO.C.10; levels 6, 7, 8 serve G-CO.C.11.
  Compass challenges 1 to 6 serve G-CO.D.12; challenges 7 and 8 serve G-CO.D.13.
- tool.json: driver "students", minutes "20-45", modes ["Tower", "Compass"], grades_label "Grade 10".

## Screens and modes
Header (kit, 9-12 theme): title "Proof Tower", subtitle "Every block needs a reason under it." Modes `Tower` (opens
first) and `Compass`. Kit buttons `Motion`, `Sound`, `Read`.
Layout: stage left (diagram and tower side by side), panel right. Under 1000 px wide the panel goes under the stage,
tray first. Under 900 px tall the diagram becomes a thumbnail at the top left of the stage with `Enlarge`, so the
tower and tray stay in view.

### Tower (levels)
- Level strip above the stage: `1` to `8`. A level opens when the one before it is finished. Teacher toggle in the
  panel's foot, `Open all levels` (also adds every theorem card).
- Diagram (left of stage): the level's figure, drawn in code with labels and tick marks. Caption under it: "Not
  drawn to prove anything. Only reasons count."
- Tower (right of stage): the Given blocks sit locked at the bottom (the foundation). A dashed ghost block at the
  top holds the Prove statement.
- Panel: tray with two tabs, `Statements` (the level's statement blocks, including look-alikes that can't be
  proved) and `Reasons` (the reason shelf). Buttons `Hint`, `Remove block`, `Start over`.
- Drag a statement block onto the tower (it lands where you drop it: on top, or between two blocks). Drag a reason
  card onto the block's reason socket, or select the block and tap a reason. The tower checks itself after every
  change (Interactions). Locked blocks stand straight with a lock glyph and an accent bar. A block that can't lock
  tilts a few degrees with a dashed warn outline and text under it naming what is missing.
- When the Prove block locks: the tower's outline turns accent, the panel shows the finished two-column proof
  (Statement | Reason, bottom to top) and "New reason card: <theorem>". The next level opens.

### Compass (constructions)
- Stage: a white-on-dark construction sheet. Tools across the top of the stage: `Point`, `Straightedge`,
  `Compass`, `Carry` (compass that keeps its opening), `Undo`, `Clear`. Panel: challenge list `C1` to `C8`, the
  steps used, and the check result.
- `Straightedge`: tap two points, a full line is drawn through them. `Compass`: tap a center, then a point the
  circle passes through. `Carry`: tap two points to set the opening, then tap a center. Every crossing of two drawn
  lines or circles is marked as a small constructed point; taps snap to points within 12 px.
- `Point` places a free point (drawn hollow). Free points may be used to draw, but a challenge only counts when the
  points it checks were all constructed (drawn solid).
- When a challenge checks, its short proof appears as a three or four block mini tower, already filled in, with
  each reason highlighted on the figure as you hover or focus it.

## Content
Reason shelf at the start: Given; Definition of midpoint; Definition of congruent segments; Definition of
congruent angles; Definition of perpendicular lines (they form right angles); All right angles are congruent;
Reflexive property; Transitive property and substitution; Subtraction property of equality; Linear pairs are
supplementary; Angles that make a straight line add to 180°; Corresponding angles postulate (parallel lines make
congruent corresponding angles); SSS; SAS; ASA; CPCTC (corresponding parts of congruent triangles are congruent);
Definition of parallelogram; Definition of rectangle (a parallelogram with four right angles); Definition of bisect.
Theorem cards earned: Vertical angles are congruent (level 1), Alternate interior angles are congruent (level 2),
Opposite sides of a parallelogram are congruent (level 6).

Each level: figure, then blocks as "statement [reason; needs]". G = given. Look-alikes have no valid reason.
1. Vertical angles. Lines AC and BD cross at E. G1 "AC and BD are lines that meet at E". Prove ∠AEB ≅ ∠CED.
   S1 m∠AEB + m∠BEC = 180° [Linear pairs; G1]. S2 m∠BEC + m∠CED = 180° [Linear pairs; G1].
   S3 m∠AEB + m∠BEC = m∠BEC + m∠CED [Transitive; S1, S2]. S4 m∠AEB = m∠CED [Subtraction; S3].
   S5 ∠AEB ≅ ∠CED [Def. congruent angles; S4]. Look-alike: ∠AEB ≅ ∠BEC.
2. Alternate interior angles. Lines ℓ above m, transversal t; angles 1 to 4 at ℓ and 5 to 8 at m, numbered top
   left, top right, bottom left, bottom right. G1 ℓ ∥ m. Prove ∠3 ≅ ∠6.
   S1 ∠2 ≅ ∠6 [Corresponding angles; G1]. S2 ∠2 ≅ ∠3 [Vertical angles; none]. S3 ∠3 ≅ ∠6 [Transitive; S1, S2].
   Look-alike: ∠3 ≅ ∠5.
3. Triangle angle sum. △ABC, line DE through B with D on A's side. G1 DE ∥ AC, with D, B, E on one line.
   Prove m∠A + m∠ABC + m∠C = 180°.
   S1 ∠DBA ≅ ∠A [Alternate interior; G1]. S2 ∠EBC ≅ ∠C [Alternate interior; G1].
   S3 m∠DBA + m∠ABC + m∠EBC = 180° [Straight line 180°; G1]. S4 m∠A + m∠ABC + m∠C = 180° [Substitution; S1, S2, S3].
   Look-alike: ∠DBA ≅ ∠C.
4. Isosceles base angles. △ABC, D on AC, segment BD. G1 AB ≅ CB. G2 D is the midpoint of AC. Prove ∠A ≅ ∠C.
   S1 AD ≅ CD [Def. midpoint; G2]. S2 BD ≅ BD [Reflexive; none]. S3 △ABD ≅ △CBD [SSS; G1, S1, S2].
   S4 ∠A ≅ ∠C [CPCTC; S3]. Look-alike: ∠ABD ≅ ∠CBD placed before S3 (true, but nothing proves it yet), so
   "△ABD ≅ △CBD by SAS" wobbles with "needs below: ∠ABD ≅ ∠CBD".
5. Perpendicular bisector. Segment AB, M its midpoint, line ℓ through M, P on ℓ. G1 ℓ ⟂ AB at M. G2 M is the
   midpoint of AB. G3 P is on ℓ. Prove PA ≅ PB.
   S1 AM ≅ BM [Def. midpoint; G2]. S2 ∠PMA and ∠PMB are right angles [Def. perpendicular; G1, G3].
   S3 ∠PMA ≅ ∠PMB [All right angles; S2]. S4 PM ≅ PM [Reflexive; none]. S5 △PMA ≅ △PMB [SAS; S1, S3, S4].
   S6 PA ≅ PB [CPCTC; S5]. Look-alike: PM ≅ AM.
6. Parallelogram sides. ABCD with diagonal AC. G1 AB ∥ DC. G2 AD ∥ BC. Prove AB ≅ CD.
   S1 ∠BAC ≅ ∠DCA [Alternate interior; G1]. S2 ∠BCA ≅ ∠DAC [Alternate interior; G2]. S3 AC ≅ AC [Reflexive].
   S4 △ABC ≅ △CDA [ASA; S1, S3, S2]. S5 AB ≅ CD [CPCTC; S4]. Look-alike: △ABC ≅ △ACD (wrong vertex order:
   "The letters don't match: A must pair with C").
7. Parallelogram diagonals. ABCD, diagonals meet at E. G1 ABCD is a parallelogram. Prove AC and BD bisect each other.
   S1 AB ∥ DC [Def. parallelogram; G1]. S2 AB ≅ CD [Opposite sides; G1]. S3 ∠BAE ≅ ∠DCE [Alternate interior; S1].
   S4 ∠ABE ≅ ∠CDE [Alternate interior; S1]. S5 △ABE ≅ △CDE [ASA; S3, S2, S4]. S6 AE ≅ CE [CPCTC; S5].
   S7 BE ≅ DE [CPCTC; S5]. S8 AC and BD bisect each other [Def. bisect; S6, S7]. Look-alike: AE ≅ BE.
8. Rectangle diagonals. Rectangle ABCD. G1 ABCD is a rectangle. Prove AC ≅ BD.
   S1 ABCD is a parallelogram [Def. rectangle; G1]. S2 AD ≅ BC [Opposite sides; S1].
   S3 ∠DAB and ∠CBA are right angles [Def. rectangle; G1]. S4 ∠DAB ≅ ∠CBA [All right angles; S3]. S5 AB ≅ AB [Reflexive].
   S6 △DAB ≅ △CBA [SAS; S2, S4, S5]. S7 BD ≅ AC [CPCTC; S6]. Look-alike: △DAB ≅ △ABC.
Compass challenges (sheet units, A and B given):
- C1 Equilateral triangle on AB, A(−2, 0), B(2, 0). Mini tower: AC ≅ AB (radii of circle A); BC ≅ BA (radii of
  circle B); AC ≅ BC ≅ AB (transitive). Euclid I.1.
- C2 Perpendicular bisector of AB. Mini tower: P and Q are each the same distance from A and B (radii of equal
  circles); so P and Q are on the perpendicular bisector (converse of level 5); line PQ is the perpendicular bisector.
- C3 Midpoint of AB (the perpendicular bisector's crossing with AB).
- C4 Bisect ∠BAC (rays from A(0, 0) at 0° and 70°).
- C5 Copy ∠BAC (40°) onto the ray from P.
- C6 Parallel to line ℓ through P (P two units off ℓ).
- C7 Regular hexagon inscribed in the circle with center O through A. Mini tower: each side equals the radius (the
  compass opening never changes); so each center triangle is equilateral; six 60° turns close the hexagon.
- C8 Square inscribed in the circle: a diameter, its perpendicular bisector, the four ends joined.

## Interactions in detail
- Check rule: a block locks when its reason is one listed for it and at least one listed premise set is fully made
  of locked blocks lower in the tower. The pass runs bottom to top and repeats until nothing changes, so moving a
  premise lower can lock several blocks at once. Premises are matched by statement id, never by text.
- Messages under a block that can't lock (one at a time, first that applies): "Needs a reason." / "This reason can't
  give this statement." / "Needs below: <statement>." (missing) / "Move <statement> below it." (present but higher)
  / for look-alikes "No reason on the shelf proves this from what you know."
- A level's own theorem card, if shown (Open all levels), is greyed: "This is what you are proving."
- `Hint`: first press names the reason of the lowest block in the listed solution that isn't locked yet; second
  press names its statement. Hints are optional and not counted.
- Extra locked blocks that the Prove block doesn't use stay; the two-column proof marks them "(not used)".
- Compass checks: lengths and angles are compared with a tolerance of 1e-6 times the length of AB (floating point
  only; the construction itself is exact). The checked points must be constructed (crossings), never free points;
  a free point gives "That point was placed by hand. Use a point where two lines or circles cross." C1 accepts
  either crossing point (above or below AB). Steps used counts each line and circle drawn; `Undo` removes the last.
- Keyboard: Tab through tray blocks, Enter picks one up, arrow keys choose its slot in the tower, Enter drops; on a
  selected block, R opens the reason list. In Compass, arrow keys move a crosshair between existing points.
- Progress (finished levels and earned cards) saves on this device (localStorage) with `Clear progress` in the panel
  foot. Nothing else is stored.
- `window.__tool = {state, setMode, level(n), place(statementId, slot), reason(slot, reasonId), check(), challenge(n)}`.

## Look
Accent `--brand #b673ff` (ultraviolet), `--brand-ink #10161f`. Stage slate `#121826`; Given blocks stone `#3a4252`;
statement blocks `#232c3b`; diagram lines `#e8edf3`; wobble outline dashed `#ffb8a8` (theme warn) plus text, never
color alone; the lock glyph marks locked blocks. Compass sheet `#0f141c` with drawn circles `#a6b3c4`, lines
`#e8edf3`, constructed points solid accent, free points hollow.
Contrast (computed): brand on --panel 5.68:1, on --sec-bg 5.38:1, on slate 5.81:1; brand-ink on brand 5.95:1; ink on
block 11.93:1, on Given block 8.57:1; warn on block 8.48:1. No 9-12 math tool uses this violet; nearest are
image-transformer's #a58cff (gr 12) and correlation-guessing-game's #e59cff (gr 9).

## Art
none: drawn in code (diagrams, blocks, construction sheet, preview.svg).

## Voice
Bank voice `clear-teacher` (Iapetus), style "clear and kind, like a patient geometry teacher at the board". No 9-12
math neighbor uses it. `Curio.voice`, `scope: () => state.mode`.
- wTower (how, Tower welcome): "Drag a statement onto the tower, then give it a reason. It locks only when what the reason needs is already below it."
- wCompass (how, Compass welcome): "Pick a challenge. Choose Compass or Straightedge, then tap points to draw."
- wobble (how, first wobbling block): "That block wobbles. Read the line under it to see what it still needs."
- circular (how, first greyed theorem card used): "That is what you are proving, so it can't be a reason yet."
- freePoint (how, first free point in a check): "That point was placed by hand. Use a point where two lines or circles cross."
- levelDone (event, Prove block locks; stale when the level changes): "The proof holds. Its theorem is now a reason card."
- built (event, challenge checks; stale when the challenge changes): "Constructed. Every point came from the compass and the straightedge."

## Family engine
none.

## Sources
- G-CO.C and G-CO.D text: Common Core State Standards for Mathematics, High School Geometry, Congruence, https://www.thecorestandards.org/Math/Content/HSG/CO/
- Proof content (vertical angles I.15, alternate angles I.29, angle sum I.32, isosceles base angles I.5, parallelogram sides I.34) and constructions (equilateral triangle I.1, carried compass I.2, bisect angle I.9, bisect segment I.10, perpendicular I.11, copy angle I.23, parallel I.31, hexagon IV.15, square IV.6): Euclid's Elements, D. E. Joyce edition, Clark University, https://mathcs.clarku.edu/~djoyce/java/elements/elements.html
- Every level's premise sets were checked by hand against these propositions (2026-10-27).

## Done when
1. Level 1: placing S5 with its reason before S4 leaves it wobbling with "Needs below: m∠AEB = m∠CED"; moving S4 under it locks both.
2. Level 4: "△ABD ≅ △CBD" with SAS wobbles naming ∠ABD ≅ ∠CBD; switching the reason to SSS locks it once S1 and S2 are below.
3. Level 6: "△ABC ≅ △ACD" never locks and says the letters don't match.
4. Finishing level 1 adds "Vertical angles are congruent" to the shelf and level 2 can be finished with it; the two-column proof lists every block bottom to top.
5. Look-alike blocks never lock with any reason.
6. C1 checks with circles about A through B and about B through A, the crossing C, and segments AC and BC; a hand-placed C near the crossing is refused.
7. C7 checks with six constructed points stepped around the circle and the six sides drawn.
8. Keyboard alone finishes level 1; every size in STANDARDS.md keeps the tower, the tray and the Prove block visible without page scrolling.
9. Console clean, no network, no em dashes, "Curio Class" only in full.

## Open questions
- Title: "Proof Blocks" is also the name of a published drag-and-drop proof tool (University of Illinois,
  PrairieLearn). This spec renames it "Proof Tower". Keep the rename?
- Levels open in order (each earns a card the next needs). Fine for a class, or open all levels by default?
