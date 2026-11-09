OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 1 (general 0, family 1), should fix 9 (general 5, family 4), polish accepted 16

# Refine: compass-and-straightedge

Curiosity No. 09. Merged from `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (no sensitivity file; all three
lenses found no cultural, Native or hard-history content). All three lenses pass the short test and the lesson creep
check; the engine's numbers recompute right. Frames: `S:/CurioClass-codex-scratch/compass-and-straightedge/` under
`teaching/frames/`, `play/`, `craft/out/` and the shared `audit-r1/`. Integrator spot-checked src.html:290, 363-366,
406-420, 477, 485, 493, 720-724, 866, 961-964 and 1102-1106: every cited claim below holds.

## Blocker
1. **Tangent circles and tangent lines make phantom duplicate points.** `src.html:290` (`EPS = 1e-9`), `:406-411`
   (line-circle), `:413-420` (circle-circle), `:372-374` (`addPoint` merge). When two circles just touch, rounding
   leaves `h2` around 2e-16, so `h = sqrt(h2)` is about 1.5e-8, above the 1e-9 cut, and one touching point becomes two
   (the same for `dt` on a tangent line). On the spec's own hexagon walk (Things to do 5, Done when 3) on the Given
   circle sheet, opposite rim circles (centres E and C) touch at the centre A and the sheet grows M and N 1.49e-8 from
   A: three stacked labels "N A M" with leader lines, and the log foot reads "15 points" where 13 exist
   (`play/p04`, `craft/out/h1-hexagon.png`, `craft/out/h2-hexagon-phantoms`: `{"n":"M","d":1.49e-8,"parents":["E","C"]}`).
   The phantoms can be chosen with arrows and anchor new circles, which spawn more near-duplicates, while the Manual
   says tangencies are handled. Fixed: treat `h` and `dt` below a relative tolerance (about 1e-7 times the radius) as
   one touching point, and merge new crossings with a tolerance scaled to the figure; the hexagon walk then shows one
   centre and "13 points". Re-word the Manual honesty note ("Points within 10⁻⁹ sheet units are merged", "Tangencies
   use a small relative numerical tolerance") to state the tolerance actually used. (family:curiosity)

## Should fix
2. **Book ghost steps are not drawn on the student's A and B.** `src.html:961-964` (Book frame A=(-0.5,0), B=(0.5,0)),
   `:1102-1106` (ghost pushed unchanged under a comment that says it is placed apart, which it is not). On the default
   sheet, Show next step twice on I.1 lays one dashed circle centred half a unit left of the student's A and one
   centred on the midpoint of AB, while the step text says "Set the compass at A through B"; a student who draws
   circle A through B sees it miss the ghost (`teaching/frames/t6-book-ghost-i1.png`, `play/p07`,
   `craft/out/g1-ghosts-on-paper.png`; state dump: ghosts at x=-0.5 and 0.5, r=1, student A=(0,0), B=(1,0)). The same
   holds on every page whose words name A and B, and on the IV pages against the Given circle. Fixed: map each page's
   given points onto the sheet's given points when they exist (A and B for I.1, I.10, I.46 and the like; the given
   circle's centre and radius for the IV pages); when the sheet has no matching givens (blank sheet, given angle),
   draw the ghost well clear of the drawing with its own letters (item 4) so nobody reads it as theirs. Fix or remove
   the misleading comment. (family:curiosity)
3. **The record and announcements use internal ids.** `src.html:477` "Erased p5; dependent objects removed.", `:485`
   "Inked circle o3.", `:866` the `[` and `]` keys announce "circle o3. radius 1.0000 AB", `:493` the tool switch
   announces raw tool keys ("line. Arrows choose...", "erase. ..."). Seen in the teaching t8 log dump, `play/p05`,
   `craft/out/c3-erase-ink-log.png` (rows 5 and 6), `craft/k2-words`, `craft/k3-brackets`. The log is meant to read
   in Euclid's style, prints with the sheet, and Read speaks its last row aloud, so "o7" is spoken. Fixed: describe
   strokes the way the log already does: "Inked the circle with centre A through B.", "Erased point C and the 2 lines
   drawn from it.", brackets announce "Circle with centre A through B. Radius 1.0000 AB.", tool switch says
   "Straightedge.", "Eraser." (general)
4. **Book figures and ghosts carry no letters, but every step names points.** `src.html:1086-1094` (drawBook draws
   only lines and circles; 0 text nodes in `#figure`), step strings at `:966-967` and `:1032-1065`. I.1 says "Call the
   upper crossing C" with no C to find (`play/p06`); I.2 says "Circle B through C. It cuts the extended DB at G."
   (`teaching/frames/t7-book-i2-figure.png`, step 7, no labels); IV.11 uses E, F, H, V and D. I.2 and IV.11 teach the
   hardest ideas and can't be followed. Fixed: pencilled letters on the Book figure for every point a step names, and
   on the ghost points laid on the paper (matching the student's own letters where item 2 maps them onto the sheet).
   (family:curiosity)
5. **Undo also rewinds the instrument settings and the view.** `src.html:363-366`: `checkpoint()` clones the whole
   `state`, so Undo restores `tool`, `euclid`, `extend`, `hold`, `view` and the Book ghosts with the drawing
   (`craft/u1-undo-scope`: draw a circle, pick Edge, switch on Euclid's rule and Extend, pan; Ctrl+Z gives back
   `tool:"compass", euclid:false, extend:false` and the view jumps 0.7 units). A student working under Euclid's rule
   (Done when 5) silently loses it on the first Undo. Fixed: history holds only points, objects, log, serial and
   nextName (and unitLabel if a sheet change is undoable); settings, view and ghosts stay as they are. (general)
6. **The readout live region re-announces on every pointer move.** `src.html:168` (`#readout` is `aria-live=polite`),
   `:736` rewrites it on every `render()`, including each `pointermove` while panning (`:819`). With the I.1 triangle
   readout showing, a 30-step pan made 32 live-region mutations (`craft/p1-pan-triangle-live`), so a screen reader
   repeats "AB 1.0000 AC 1.0000..." through the drag. Fixed: write `#readout` only when its text changes (or drop
   `aria-live` there and keep the one `#status` announcement per move). (general)
7. **Frame time falls under 60 fps at moderate density.** `render()` (`:641`) rebuilds the whole SVG and re-places
   every label on each `pointermove` (`:819`), not once per frame. Measured on a fast desktop: 60 objects and 757
   crossings, during a 60-step pan 61 of 181 frames over 20 ms, p95 31.9 ms, max 40 ms (`craft/out/p2-dense.png`); a
   school Chromebook is several times slower, and a Book pentagon is 30 to 40 objects. Fixed: route pointer-driven
   renders through the existing `requestRender()` so there is at most one per animation frame, and skip label
   placement for points off screen (see polish 13 for density). The 13-object hexagon (0.5 ms) must stay as smooth.
   (family:curiosity)
8. **The resting straightedge covers the drawing and never slides.** `src.html:720-724` draws it on top of the
   construction at a fixed spot (about 575 to 620 px down at 1366x768): across the right I.1 circle beside D
   (`play/p03`, `craft/out/c2-triangle.png`), across the hexagon (`play/p04`) and the lower area at 1920
   (`play/r07`). A straightedge drag shows a grey band instead of the straightedge sliding over, as the spec's first
   two minutes promise. Fixed: draw it under the strokes and rest it on the table edge outside the working area (or
   move it aside when ink lies under it), and let it be the thing that slides into place along a straightedge drag
   (instantly with Motion off). (family:curiosity)
9. **The blank sheet's waiting moment says nothing.** Paper, Blank sheet gives an empty page with Compass still
   selected and the hint hidden (`play/q07`, output `true`); dragging pans and tapping does nothing. Read knows the
   line, the screen does not. Fixed: show `L.blank` as the one quiet pencilled line on the paper until the first
   point, and select the Point tool on a blank sheet. Not spoken on its own (Read reaches it). (general)
10. **The readout tag covers point labels.** `src.html:750-755` keeps the tag inside the edges but not off labels: at
    680x425 "CD 1.7321 AB" hides B's label (`play/p10`); at 375x812 "radius 1.0000 AB" sits on B's label
    (`audit-r1/state-circles-375x812.png`). Fixed: the tag avoids point labels the way labels already avoid each
    other. (general)

## Polish accepted
11. **Say where crossings come from in the log.** `src.html:432-440`. The record jumps from "Circle with centre B
    through A." to "Line from C to A." with no word that C is where the circles cut (`teaching/frames/t2-i1-triangle.png`).
    After a move that makes crossings, add a sub-line naming them: "They cut at C and D." (family:curiosity)
12. **Point names that clash with segment names.** `src.html:367-371` (pointName), `:607`, `:615` (readouts join
    names with no space). A pentagon makes points A to AN, so one point is named "AB" on a sheet whose unit is AB, and a
    segment from A to it reads "AAB 1.0000 AB" (teaching t5 dump). Skip any generated name equal to the unit label or
    to two existing single letters run together (or switch to primes or subscripts after Z), and separate names in
    multi-letter segment readouts (a space or a bar). (general)
13. **Label clutter at density.** `src.html:695-702`: every crossing gets a label, and a dense sheet becomes a block
    of overlapping two- and three-letter names (`craft/out/p2-dense.png`). Always label given, free, chosen and
    stroke-end points; drop a crossing label that would collide, or below a zoom where it can't be read, and show it on
    hover, choice or the arrow cursor. Names in the log stay the same. (family:curiosity)
14. **The margin note for more Book figures.** `src.html:630-640`. Only I.1 earns "Euclid, Book I, Proposition 1";
    the hexagon walk (`play/p04`), the square in a circle and the 1.6180 pentagon (`play/q12`) find nothing. Add the
    same quiet pencilled note where detection is cheap and sure, at least IV.15 (six equal chords close in the given
    circle) and IV.6 (square in the given circle), and others of the 14 only when equally reliable. Never spoken,
    counted or listed as found. (family:curiosity)
15. **"Things people have found" as separate entries.** `src.html:230-237`: the eight finds run together in three
    paragraphs (`play/q05`). One short entry each, led by its figure or name, so a student who just made the hexagon
    finds theirs at a glance. (family:curiosity)
16. **Triangle readout beside the triangle.** The I.1 readout is pinned top-left, far from the figure, while every
    other tag sits by its object (`play/p03`, `play/q10`). Place it beside the triangle like the other tags.
    (general)
17. **A selected stroke is hard to see.** `src.html:653` adds 0.7 px (1.2 to 1.9 px); in `craft/out/c4-select-weight.png`
    the selected CA is barely different from DB. Give the selection a soft red halo or the crossing red at about
    2.5 px. (general)
18. **Undo and redo glyphs are tiny.** `src.html:191-192`: the arrows render about 8 px in a 48 px button
    (`audit-r1/size-1366x768.png`, `size-680x425.png`). Draw them as about 22 px SVG icons like the toolbelt. (general)
19. **The Manual opens as a centred modal, not the lower-left drawer.** `src.html:65-66, 202`: the handle opens a
    740 px centred dialog (`audit-r1/state-manual-1366x768.png`); the family mark (Span and Spire,
    `span-and-spire/src.html:151`) is a drawer anchored at the lower-left handle. Anchor it there. Keep it a modal
    dialog for focus. (family:curiosity)
20. **Strokes have an 18 px tap band.** `src.html:778` `min=9`. Selecting, inking, erasing or measuring a 1.2 px line
    by touch needs a tap within 9 px; points get 44 px. Use about 22 px either side on coarse pointers. (general)
21. **The keyboard cursor ring shows for mouse users.** `src.html:703-707`, `:796`: any click focuses the sheet, so a
    dashed red ring sits on A after a drag or "Back to paper" and looks like a choice (`craft/out/c2-triangle.png`).
    Show it only after a key press. (general)
22. **Accessible names don't start with the visible word.** `src.html:174, 176`: visible "Edge" and "Erase", names
    "Straightedge, S" and "Eraser, E"; voice control users saying "click Edge" can miss. Start each name with the
    visible word ("Edge, straightedge, S"). (general)
23. **The idle compass sits on the zoom tag at 375 wide.** `src.html:718` (compass at 44,65) over "AB = 1 unit · 62%"
    (`audit-r1/size-375x812 (iframe host).png`, `play/q10`). Move one of them. (family:curiosity)
24. **The first-run hint stays after a non-drawing tool is chosen.** Choosing Measure, Erase or Point before any drag
    leaves "Drag from A to B." on screen, which those tools can't do (`play` finding 10). Show the chosen tool's line
    or hide the hint on that switch; no new speech (the welcome rule stays as BASELINE 16 has it). (general)
25. **Confirm the archive.org volume labels.** `src.html:249-251` labels thirteenbookseu02heibgoog as Books I and II,
    00 as III to IX, 03 as X to XIII; Teaching could not confirm the mapping from the item pages. Check inside each
    scan; if a volume can't be confirmed, give the link without the Book range. (general)
26. **Name proof-tower in notes.md.** notes.md "What it teaches": say plainly that G-CO.C proofs are taught in
    proof-tower and this tool is the second card for G-CO.D, as the spec's Map already says. Do not change the module
    map (see open questions). (family:curiosity)

## Settled calls
- **Book ghosts tag:** Play tagged general, Teaching and Craft family:curiosity. Settled family:curiosity: the Book's
  own coordinate frame is this tool's format, not a general habit.
- **Book letters are their own item (4), not folded into the ghost item (2):** Play joined them; they are separate
  fixes (placement vs lettering) and Codex should check both.
- **Resting straightedge:** Play said should fix, Craft said nit. Settled should fix: it covers working strokes and
  the spec promises it slides over on a straightedge drag.
- **Readout tag over labels:** Play said should fix (680x425), Craft polish (375). Merged as one should fix at both
  sizes.
- **Tangency tolerance is an engine fix, not a spec change.** The spec's Sources line "points merged within 1e-9" is
  an engine detail; Codex changes the tolerance and updates the Manual honesty note to state what the engine does.
- **Not to change:** the full-bleed `#sheet` overlapping every control and controls covered by open modal dialogs are
  by design (all three lenses; the 368 audit leads are almost all these). The first-run hint is not spoken after a
  first tap on a non-compass control (BASELINE 16); item 24 changes only the visible line. Read joining hint, last log
  row and readout through browser speech is the spec's stated fallback. The measure tool stays (spec lean). The Book
  stays browsed: no numbering of progress, ticks or "done" on pages; the margin note stays quiet, unspoken and
  uncounted. Nothing adds a goal, score, level or finish.
- **Done when 3 and 4:** Teaching passed them on the readouts; the hexagon pass holds only once blocker 1 removes the
  phantom points and the count reads true.

## To the spec's open questions
- **Reach modules overclaim.** math-10-rigid-motions-and-congruence: only G-CO.A.1 (precise definitions of circle,
  perpendicular, parallel) is exercised; nothing for transformations. math-7-scale-drawings-and-constructions (7.G.A.2,
  triangles from three measures): no sheet with three given lengths and no I.22 page, so a grade 7 student has nothing
  to build from. Choose: narrow the reaches (keep G-CO.A.1 only, drop the math-7 reach), or add a "Given three
  lengths" sheet and an I.22 Book page. (Teaching 6)

## Not taken
- History memory cap or diff history (Craft 17): fine at today's sizes, and item 5 already shrinks each snapshot;
  revisit if item 7 is reworked.
- Audit tweak (skip overlap rows against a stage-sized element and controls under an open modal dialog, Craft audit
  pilot): a change to `scripts/audit_tool.py`, not to this tool; for the integrator's audit backlog.
