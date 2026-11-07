# Teaching lens: compass-and-straightedge (Curiosity No. 09)

Cold lens, round 1, 2026-11-06. Judged as a Curiosity (CODEX-CURIOSITY.md, VISION "Curiosities: the second shape").
Frames and scripts: `S:/CurioClass-codex-scratch/compass-and-straightedge/teaching/` (shots.json, shots2.json, frames/).
The engine is sound: every number I recomputed matches. The weak spot is the Book. Its step-by-step help can't be
followed against the student's own paper.

Counts: blockers 0, should fix 3, polish 3, nits 2.

## Findings

### 1. Book ghost strokes are not drawn on the student's A and B (should fix, family:curiosity)
- Where: src.html:961-970 (Book geometry uses its own frame, A=(-0.5,0), B=(0.5,0)), src.html:1105-1106 (ghost
  pushed unchanged, with the comment "Place the reference slightly apart from the starting A/B pair").
- What: on the default sheet, pressing Show next step on I.1 twice lays two dashed circles. One is centred left of
  the student's A and the other on the midpoint of AB. Neither is centred on the A or B labelled on the paper.
  The step text says "Set the compass at A through B", so a student who draws circle A through B sees their circle
  miss the ghost. The reference then contradicts the paper it's drawn on. The same happens on every page whose
  words name A and B.
- How seen: `frames/t6-book-ghost-i1.png`. The state dump shows ghosts at x=-0.5 and x=0.5 with r=1, and the
  student's A=(0,0) and B=(1,0).
- Better: fit the page's own given points onto the student's given points when they exist. Or draw the ghost
  well clear of the drawing, with its own letters (see 2), so nobody reads it as being on their A and B.

### 2. Book figures and ghosts have no letters, but the steps name points (should fix, family:curiosity)
- Where: src.html:1086-1094 (drawBook draws only lines and circles), Book step strings at src.html:1032-1036 and
  1046-1065.
- What: the steps say "Circle D through G. It cuts extended DA at L." (I.2) and use E, F, H, V and D for IV.11.
  Neither the figure nor the ghosts carry a single letter (0 text nodes in `#figure`). The only labels on the
  sheet are the student's own A and B, and those are different points from the Book's A and B. I.2 and IV.11 are
  the two pages that teach the hardest ideas (the collapsing-compass transfer and the golden division), and they
  can't be followed.
- How seen: `frames/t7-book-i2-figure.png` (I.2 at step 7, steptext "Circle B through C. It cuts the extended DB
  at G.", no labels).
- Better: put pencilled letters on the figure and the ghost points the steps name.

### 3. Log and announcements use internal ids (should fix, general)
- Where: src.html:477 (`Erased ${id}; dependent objects removed.`), src.html:485 (`Inked circle o3.`),
  src.html:866 (the [ and ] keys announce `circle o3`).
- What: the construction record is meant to be read back "in Euclid's style" (spec Things to do 12) and printed
  with the sheet. Instead it shows "Inked circle o3." and "Erased p5; dependent objects removed." Students never
  see o3 or p5 anywhere else, and a screen reader user hears "circle o3" when picking strokes.
- How seen: t8 log dump: `["Given points A and B. AB = 1 unit.","Circle with centre A through B.","Circle with
  centre B through A.","Inked circle o3.","Erased p5; dependent objects removed."]`.
- Better: name things as the log already does: "Inked the circle with centre A through B." and "Erased point C
  and the 2 lines drawn from it."

### 4. The log never says where crossings come from (polish, family:curiosity)
- Where: src.html:432-440.
- What: the record reads "Circle with centre B through A." and then "Line from C to A." with nothing between. C
  first appears as a crossing on the paper, but the log never says so. Euclid's own wording is "the circles cut
  one another at C". Without that line the record can't be read on its own, and a printed log that runs into a
  second column loses the link to the figure.
- How seen: `frames/t2-i1-triangle.png` (log entries 3 and 4).
- Better: after a move, add a sub-line naming the new crossings, for example "They cut at C and D."

### 5. Point names run into double letters fast, including "AB" (polish, general)
- Where: src.html:367-371 (pointName), 607 and 615 (readouts join names with no space), 633 (the triangle check
  looks up points by name).
- What: every crossing of every pair gets a letter. A pentagon of 11 strokes already makes 40 points, A to AN
  (t5). One of those points is named "AB" on a sheet where "AB = 1 unit" is the unit and "AB" is also a segment.
  A segment from A to point AB would read "AAB  1.0000 AB". That confuses the very idea, segment naming, that
  G-CO.D.12 relies on.
- How seen: t5 dump `names: A B C ... Z AA AB AC ... AN`.
- Better: skip names that clash with the unit (or use primes or subscripts, A1, A2), and put a space or a bar in
  multi-letter segment readouts.

### 6. Map claims beyond what the instrument exercises (polish, family:curiosity)
- Where: spec.md "Map"; notes.md "What it teaches".
- What: G-CO.D.12 is fully exercised: copying a segment (I.2 tested by hand with Euclid's rule on, AL = 1.0000),
  bisecting a segment, bisecting an angle (t11: 25.45 and 25.45 degrees, halves of 50.91), perpendiculars and
  parallels. G-CO.D.13 is fully exercised too: the triangle (t2), the hexagon (t3) and the square. G-CO.C is
  honestly marked partial, and proof-tower carries it, so as a second card this is fine. But notes.md should name
  proof-tower as the place G-CO.C is taught. Of the "reaches":
  - math-10-rigid-motions-and-congruence: only G-CO.A.1 (precise definitions of circle, perpendicular and
    parallel) is exercised. There is nothing for transformations.
  - math-7-scale-drawings-and-constructions (7.G.A.2, triangles from three measures): there is no starting sheet
    with three given lengths and no I.22 page, so a grade 7 student has nothing to build from.
- Better: keep the reach to G-CO.A.1, or add a "Given three lengths" sheet and an I.22 Book page.

### 7. The margin note only names I.1 (nit, family:curiosity)
- Where: src.html:630-640.
- What: the spec's lean was to name all 14 Book figures quietly. Only I.1 gets "Euclid, Book I, Proposition 1".
  A hexagon (IV.15) or a bisector (I.10) gets nothing. That's fine as it stands; a few more notes would add
  depth without becoming a target.

### 8. archive.org volume labels not confirmed (nit, general)
- Where: src.html:249-251.
- What: the Manual labels thirteenbookseu02heibgoog as Books I and II, 00 as III to IX, and 03 as X to XIII. Both
  item pages I opened (00: 456 pp, 02: 449 pp) have the same three-volume description and no volume number, so I
  couldn't confirm the mapping. Worth a look inside each scan before ship.

## Done when (Teaching checks)
| # | Result | Evidence |
|---|---|---|
| 1 | PASS | t1: a real drag from A to B makes "Circle with centre A through B."; audit size frames clean |
| 2 | PASS | t2: `AB 1.0000 AC 1.0000 BC 1.0000`, angles `60.00° 60.00° 60.00°`, note "Euclid, Book I, Proposition 1" |
| 3 | PASS | t3: circles walked from rim crossings at radius 1 land at -60, -120, -180, 120, 60, then back on B (same point, merged) |
| 4 | PASS (readout) | t5: side/diagonal readout `longer / shorter 1.6180`, line angle 36.00°, diagonal 1.9021 (2 sin 72° = 1.90211). I built a shorter valid pentagon, not the full Book method; I recomputed the Book IV.11 page geometry (II.11 radius 0.618, golden triangle with 36°/72°) and it is right |
| 5 | PASS | t4: Euclid's rule on, Keep opening disabled, I.2 by hand gives AL = 1.0000 = BC |
| 6 | PASS, see 3 | only made points are used (hitPoint); log in order; t8: undoing everything leaves 1 entry, redo restores 5 |
| 7 | PASS | ghosts appear only on Show next step; nothing ticked. But see 1 and 2 |
| 8 | PASS (teaching part) | t9: C, Enter, Arrow, Enter draws a circle; Motion off is clean in the audit. Craft owns the rest |
| 12 | PASS | lesson creep grep: no score, goal, level, sticker, correct or wrong; no em dashes |

## Facts spot-checked (12)
Gauss and the 17-gon, 1796, aged 18 (born April 1777). Wantzel 1837. Lindemann 1882. Mohr 1672 and Mascheroni 1797
(confirmed on MacTutor's Mascheroni page). Heath died 1940. Golden ratio 1.618034, shown as 1.6180. The pentagon's
diagonal and angle (t5). IV.16 arithmetic: 120 - 72 = 48, half is 24 degrees, 360/24 = 15. The II.11 page geometry:
EB = sqrt(5)/2, AH = 0.618, AH squared = AB x HB = 0.382. The 14 enunciations and 3 postulates in the Book and
Manual match spec.md word for word. The honesty notes match the code (EPS 1e-9, 600-object cap). No errors.
No cultural, Native or hard-history content, so no sensitivity review is needed.

## Audit pilot
- Leads confirmed: none that bear on teaching. "hint out of view" on circles, blank-paper and infinite-line is
  right: the hint is meant to go after the first action.
- Leads wrong: the 368 leads are almost all `#sheet` overlaps (the sheet fills the screen by design) and controls
  "hidden" under modal drawers that are meant to cover them. The manual's "choices cut short" lead is just source
  links further down a scrolling drawer.
- What it missed: the Book ghosts landing off the student's A and B (1), the figures having no letters (2), internal
  ids in the log (3), and point names clashing with the unit (5). None are mechanical layout faults.
