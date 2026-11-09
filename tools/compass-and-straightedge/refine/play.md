# Play lens: compass-and-straightedge (Curiosity No. 09), round 1

Cold lens, judged against CODEX-CURIOSITY.md and VISION "Curiosities: the second shape". Frames are mine in
`S:/CurioClass-codex-scratch/compass-and-straightedge/play/` (p*, q*, r*), driven with real drags, clicks and keys where
the input mattered, plus the shared audit `audit-r1/`.

## Short test

- Would a kid open it unassigned? Yes, mostly. The first drag from A to B lifts the brass compass, swings a pencil
  circle with a graphite scratch and leaves a line that stays (p02). Two drags and two lines make a triangle that reads
  1.0000, 1.0000, 1.0000 and 60.00 degrees with a pencilled "Euclid, Book I, Proposition 1" (p03). That lands.
- Would an adult play for fun? Yes. Walking the radius round a circle makes the six-petal flower (p04), Keep opening
  works as a modern compass (r02, log "Circle with centre C, retained radius 1.0000 AB"), and measuring a pentagon's
  diagonal against its side gives 1.6180 (q12).
- Is the real thing the interface? Yes: circles, crossings and lines are the whole screen; no lesson frame.
- Does it work with no finish line? Yes. No score, goal, level or finish anywhere I looked; the Book is browsed by a
  select menu, nothing ticks.

Passes all four. The findings below are about the instrument telling the truth and the second-session depth.

## Findings

1. **blocker** · family:curiosity · geometry engine, `src.html:290` (`EPS = 1e-9`) with `addPoint` merge.
   The hexagon walk, the tool's signature "thing people have found", makes duplicate crossings at the centre. After
   walking six circles round the given circle, points M and N sit 1.49e-8 from A (q01 output: "M crossing 1.490e-8",
   "N crossing 1.490e-8"). The paper shows three stacked labels "N A M" with leader lines at the centre (p04), and the
   log foot reads "15 points" where 13 exist. A readout that lies, on the figure a kid is most likely to make. Better:
   merge with a tolerance scaled to the figure (or merge by shared parent objects), so the flower has one centre and
   the counts are true. Also re-word the Manual's "Points within 10⁻⁹ sheet units are merged" to match.

2. **should fix** · general · The Book's ghost steps, `src.html:964` and `:1106`.
   Book figures use their own coordinates (A at -0.5, B at 0.5) while the student's A and B are at 0 and 1. On I.1,
   "Set the compass at A through B" lays a ghost circle centred half a unit left of the student's A, and the second
   ghost is centred on the middle of AB (p07, Book closed after three steps). A student following the Book on their own
   paper sees a reference that contradicts the step text and their own points. Inside the Book the small figure has no
   point labels, so "Call the upper crossing C" (p06) has no C to find. Better: map each page's figure onto the sheet's
   given points where the page starts from A and B (I.1, I.10, I.46, IV pages on the given circle), or draw ghosts in a
   clearly separate place, and letter the Book figure's points.

3. **should fix** · general · Construction record words, `src.html:477`, `:485`, `:866`.
   The log shows internal ids: "Inked circle o3." and "Erased o4; dependent objects removed." (p05 output); the [ and ]
   keys announce "circle o5". Every other log line speaks in point names ("Circle with centre B through A."). Better:
   "Inked circle with centre A through B." and "Erased the circle with centre B through A, and 2 crossings that
   depended on it."

4. **should fix** · family:curiosity · The decorative straightedge, `src.html:720`.
   It is drawn on top of the working paper at a fixed spot (about 575 to 620 px down at 1366x768). With nothing more
   than the I.1 circles it sits across the bottom of the right circle beside crossing D (p03), and across the hexagon
   (p04) and the default 1920 frame's lower area (r07). Meanwhile drawing a line never moves it: the drag shows a grey
   band, not the straightedge sliding over as the spec promises. Better: rest it on the table edge outside the drawing,
   or hide it when ink lies under it, and let it be the thing that slides in on a straightedge drag.

5. **should fix** · general · Blank sheet waiting moment (q07).
   Paper, Blank sheet gives an empty page with Compass still selected and no visible word (hint hidden, q07 output
   `true`). Dragging pans, tapping does nothing. Read knows the line ("Blank paper. Choose Point to place free points"),
   but the screen says nothing. Better: show that one quiet line on the paper until the first point, and select Point.

6. **should fix** · general · 680x425 measure tag (p10).
   Selecting the line CD at 680x425 puts the tag "CD 1.7321 AB" over the label B, which is hidden under it. Better: the
   tag avoids point labels the way labels already avoid each other.

7. **polish** · family:curiosity · The pencilled margin note, `src.html:637`.
   Only I.1 earns it. The hexagon walk (p04), the square in a circle and the 1.6180 pentagon (q12) find nothing. The
   spec's own lean was the 14 Book figures. These are the moments a month of use would find; a quiet "Euclid, Book IV,
   Proposition 15" when six equal chords close would land the way I.1 does.

8. **polish** · family:curiosity · "Things people have found" in the Manual, `src.html:230-237`.
   The eight finds are run together in three paragraphs (q05). A field guide reads better as short separate entries,
   each with its figure name, so a student who just made the hexagon can find their entry at a glance.

9. **polish** · general · Triangle readout position (p03, q10).
   The I.1 readout is pinned at the top-left corner, far from the triangle, while every other tag sits beside its
   object. Better: put it beside the triangle like the other tags.

10. **nit** · general · First-run hint after a non-drawing tool. Choosing Measure, Erase or Point before any drag leaves
    "Drag from A to B." on screen, which those tools cannot do; the audit also shows the hint unspoken when the first tap
    is Edge, Point, Erase, Measure, Paper, The Book or Manual. The visible line covers it for Edge; for the others the
    words no longer match the state.

11. **nit** · general · 375x812 (audit size-375x812, q10): the zoom tag "AB = 1 unit · 62%" sits under the resting
    compass's legs at the top-left.

## Checked and clean

- Real first drag A to B: circle drawn, hint gone, log line added (p01, p02). Motion off: audit calm row clean.
- Keyboard: Tab, Enter, Right, Enter draws "Circle with centre A through B." with focus on the sheet (p12).
- Euclid's rule on: radius resets to 0 and Keep opening is disabled after a circle (q03).
- Read speaks the tool line, the last move and the readout (q04).
- Extreme zoom out to 0.02 percent: no freeze, labels still placed (q11).
- No score, goal, level, sticker, badge or finish screen in any frame.

## Audit pilot

- Leads confirmed: none of the 368 as written. The "hint out of view" rows on circles, blank-paper and
  infinite-line-min-zoom are the hint correctly gone after the first action; the welcome "not heard" rows are real but
  minor (finding 10).
- Leads wrong: every "overlap: #sheet" row (the sheet is the full-screen paper under all controls, by design), every
  "text hidden under" row in the book, manual and paper states (a modal drawer over the instrument is expected), and
  "choices cut short by a scroll panel" in the Manual (source links lower in a long reading drawer).
- Missed: duplicate crossings at the hexagon centre and the false point count (1), Book ghosts offset from the
  student's A and B (2), raw ids in the log (3), the prop straightedge over the drawing (4), the silent blank sheet (5),
  the measure tag over a label at 680x425 (6). The audit draws circles by script but cannot see a stacked label or a
  ghost that disagrees with its words.
