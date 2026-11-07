# Play lens: virtual-gallery (round 1)

Played twice: as a 9-12 student alone at home (first run, no teacher, held clicks, real drags and keys) and as a
teacher projecting at 1366x768 and 1920x1080. Bundle as built (not re-bundled). Frames in
`S:/CurioClass-codex-scratch/virtual-gallery/play/f1` to `f5`; audit frames in `.../audit-r1`.

What works: the Select welcome names the action, the 6 to 8 counter and badges read clearly, drag from the tray to a
wall (jittered pointer) and to a side wall both land where dropped (f2/r2, r3, r6), keyboard Enter on a tray work
hangs it and arrows move it 5 or 25 cm (f2/r4), Plan replaces the room at 680x425 and 375 (f1/10, f3/s4), Walk
keeps 1 s moves and 2 s stops with Motion on and off (f2/r7 and r8: stop changes at 0, 3.0, 6.0, 9.0 s in both),
Stop mid-move holds between works and Step resumes (f2/r9, r10), jump marks and the jump line land on the right stop
(f1/08), allTicked plays once all nine checks pass (f4/t1), the night and growing hints are right (f1/14, f4/t2).

## Findings

### Blocker

1. **Walk, door view: "First seen" names a work the view does not show.** `src.html:1467` (doorCamera looks
   straight down the room) with `src.html:1371` (focal 0.82 x width, about 62 degrees across) never shows the side
   walls, while `firstSeen()` (`src.html:734`) ranks side-wall works. With the back wall empty (Done when 3's second
   layout) the door view is a bare wall and the readout says "First seen: Laundromat". The walk's whole promise is
   "shows what they see first"; here the picture and the readout disagree, and the cone sits on empty wall.
   Seen: f5/u1-sidewalls-door.png. Better: widen the door view (or turn the camera toward the first-seen work) so the
   named work is in frame and marked. general.

### Should fix

2. **Hang room hides the door walls.** `src.html:1466` overviewCamera sits above the door looking in, so works on
   "Door, left" and "Door, right" are behind the camera: the status says "6/6 hung" while four frames show, and the
   door itself is never drawn. A student who picks Door, left and taps Hang on wall sees nothing happen.
   Seen: f1/02-front-walls.png. Better: pull the camera back or up so the door wall is in view, or draw the door wall
   cut away with its frames. family:virtual-gallery.
3. **Portfolio cards show no theme tags (and no size).** `src.html:869-874` shows title, medium and year only; the
   spec's Select says cards carry "image, title, medium, size, year and theme tags". Choosing six "home" works means
   opening all 14 cards one by one to read tags in the side panel, which is the slowest part of the first two minutes.
   Seen: audit size-1366x768.png, f1/14-custom-night.png. general.
4. **The checklist hides most checks in a scroll panel.** `src.html:221-236`: nine 108 px rows in an inner scroller,
   about 3.5 visible at 1366x768 (fewer at 680x425). A student cannot see the state of the show at a glance, and the
   "Show me" buttons below the fold are off screen. BUILD.md lesson "a short set of choices never hides in a scroll
   panel". Seen: audit state-mode-04checklist-1366x768.png, f1/07, f1/17. Better: compact rows (Why inline or as a
   tooltip, Show me only on unticked rows), or two columns at wide sizes. general.
5. **A squeezed label turns into a vertical strip of letters in Walk.** `wallArt` (`src.html:1053-1059`) hides a
   label with under 12 px of room, but `drawWalkArt` and `travelTo` (`src.html:1412`, `1624`) reset every label's
   visibility to '' while moving and between stops, so a 0-width label with `overflow-wrap:anywhere` shows as a
   tall column of single letters between two abutting frames. Seen: f2/r9-stop-midtravel.png (zoom f2/r9-zoom.png).
   general.
6. **No wall label at 1100 px wide and under in Walk.** `.walk-room .sharp-label {display:none}` at max-width 1100
   (`src.html:259`) while `drawWalkArt` still hides the original label (`src.html:1464`), so at 1000x625 and 680x425
   the work at the stop has bare wall beside it. "Which labels run long" is invisible in the preview sizes.
   Seen: f1/12-walk-1000.png. general.
7. **The large label card covers the wall label it repeats.** `.visitor-label` (`src.html:203`) sits bottom-right
   over the sharp wall label; with a long title or note the wall label is cut mid-word ("coff", "woke u"). The two
   copies collide exactly when the label is long, the case the walk is meant to show. Seen: f1/05-walk-longnote.png.
   family:virtual-gallery.
8. **Hang with nothing chosen: wrong words and a work that is not in the show.** `welcomeKey` returns `noWalk` in
   Hang (`src.html:708`), so the student in Hang hears "Tap Select to choose a work, then tap Hang and hang it on a
   wall before walking", and the workbench title is Creek After Rain (the `fresh()` default, `src.html:633`) with
   every control disabled. Seen: audit state-mode-02hang-1366x768.png and its table row 1. Better: a Hang-specific
   line ("Tap Select and add works to the show first.") and an empty workbench. general.
9. **Nine of nine with no label written.** Cheap pass: six home works, Hang on wall six times, Auto space, Light
   each, star whatever is centred, a four-word statement ("These places are home."): every check ticks and "Every
   measured check is ticked" plays. Titles are prefilled and blank notes pass (`src.html:782`), so the label-writing
   half of the show is never asked for, while the walk shows "0 words" on every card. Seen: f1/07-checklist-ticked.png,
   f4/t1 log. Better: Labels counts a note as written (or flags "n labels have no note" as a warning the way the path
   crossing is). general.

### Polish

10. **The hang view is mostly floor.** At 1366x768 the floor fills about 45% of the stage and frames are about 40 px
    tall (f1/01); at 760x900 the room is a small box with frames about 20 px and the door-light trapezoid floats in
    empty space under the floor (f3/s7-760-hang.png). Better: a lower, closer camera so the walls fill the stage.
11. **The cone is decoration.** `.cone-note` (`src.html:219`) is a fixed triangle at screen centre, not aimed at
    anything, and the first-seen work gets no mark in the scene, only a small mono line bottom-left (f1/03, f3/s8).
    Better: outline or spotlight the first-seen frame and point the cone at it.
12. **Walk at 680x425: overlays cover the room.** The show card covers the left third and the label card the right
    third of a 190 px stage; the neighbour frame sits under the show card (f1/11-walk-680.png).
13. **Neighbour works and labels blur in Walk.** Only the current stop is redrawn sharp; neighbours are 3 px CSS
    labels scaled up and look smeared, worst at 1920x1080 (f1/13, f1/06).
14. **Clockwise / Counterclockwise only changes the camera route.** `src.html:1551`, `1665`: the stop order stays the
    tray order, so a student who toggles expecting the visit to reverse sees the same sequence. Better: a label such
    as "Route: clockwise" plus a hint line, or make it reverse the visit.
15. **Autoplay stops are too short to read a label.** 2 s per stop (spec) against POLISH's 1400 + 75 ms per character:
    a 25-word note needs about 12 s. The student can press Stop, but the autoplay walk never lets a label be read.
16. **The walk ends flat.** "Your walk complete · 6 works · 0 story jumps" (`src.html:1704`) says nothing about the
    anchor; one line comparing First seen with the star would land the lesson of the walk.
17. **Show me on Anchor is vague.** "Move the selected work or adjust its wall." (`src.html:1754`) does not say what
    makes a work first seen (closest to straight ahead from the door).
18. **A student whose first tap is Add to show never hears "Star the one you most want seen."** The tap's own
    selectMore line replaces the welcome, and selectMore does not mention the star (audit row 21, confirmed in code
    `src.html:1006`).

### Nit

19. Double full stop after titles ending in "a.m." or "p.m.": "Starred: Kitchen Window, 7 a.m.. First seen" (`src.html:793`; f3/s2 hint text).
20. "Laundroma t" breaks mid-word in the order strip at 680x425 (`.order-title` overflow-wrap; f1/11).
21. "0 of 1 allowed jumps in tray order" reads oddly (`src.html:815`); "0 jumps (1 allowed)".
22. Show me appears on ticked rows too (f1/07).
23. "Your theme" keeps that title in Select whatever tag is picked; the show can only be named in the Statement
    dialog in Hang.

Counts: blocker 1, should fix 8, polish 9, nit 5. Nothing cultural, Native or hard-history; no sensitivity review
needed (the "Where I'm From" prompt is handled in notes.md, Teaching with care).

## Audit pilot

- **Confirmed:** the checklist rows cut by a scroll panel (finding 4); Add to show as a first tap skipping the
  welcome (finding 18, polish only, since selectMore still names the next step); the Hang mode spoken line (table
  row 1) is the wrong-words lead in finding 8; clean size rows and Motion-off timing held on my frames.
- **Wrong or benign:** "keep region #hint covered" in label-open, statement-open and clear-confirm is the modal
  dialog's backdrop over the footer, expected for a modal. "Focus lost" on cards bowl to blockmap is the click
  landing below the fold on partly visible cards (my own scripted clicks there hit the footer); a real user scrolls.
- **Missed:** the door view that shows nothing while naming First seen (blocker 1), door-wall works invisible in Hang
  (2), cards without tags (3), the vertical letter strip (5), labels gone at 1100 px and under (6), the label card
  covering the wall label (7), the Creek After Rain empty workbench (8), the nine-of-nine cheap pass (9).
