ROUND 2 (exit check 2026-11-06): blocker 1 open (door view names a First seen work it does not paint: deep Left-wall works and an all-door-wall show); polish 1 and 13 partly
Counts: blockers 1 (general 1, family 0), should fix 12 (general 10, family 2), polish accepted 15

# Refine: virtual-gallery

Merged from `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (no sensitivity lens; all three lenses found
nothing cultural, Native or hard-history, and the integrator agrees). Frames are under
`S:/CurioClass-codex-scratch/virtual-gallery/` (`play/`, `craft/`, `teaching/`, `audit-r1/`). Integrator
spot-checks: the door view (blocker 1, read `src.html:1371` and `:1467`, opened `play/f5/u1-sidewalls-door.png`),
the Hang camera (should fix 1, opened `play/f1/02-front-walls.png`) and the art sizes (should fix 3, read every
`art/*.webp` with PIL). All three hold.

## Blocker
1. **Walk door view names a "First seen" work the picture does not show.** `src.html:1467` (`doorCamera` looks
   straight down the room) with `src.html:1371` (Walk focal 0.82 x width, about 31 degrees each side). The far
   corners of the side walls sit about 33 degrees off axis from the door, so no side-wall work is ever in frame,
   while `firstSeen()` (`src.html:734`) ranks side-wall works. With the back wall empty (Done when 3, second layout)
   the stage is bare plaster, the cone sits on empty wall and the readout says "First seen: Laundromat"
   (`play/f5/u1-sidewalls-door.png`). Fixed looks like: the door view is wide enough that every work `firstSeen()`
   can name is in frame (widen the door focal, keep the camera pointing straight ahead so "straight ahead" still
   means what the Anchor Why says), and the named frame is marked in the scene (see polish 1). Re-shoot the three
   Done when 3 layouts. (general)

## Should fix
1. **Hang room hides the door wall and its works.** `src.html:1466` `overviewCamera` sits above the door looking in,
   so works on "Door, left" and "Door, right" are behind the camera: the status says "6/6 hung" while four frames show,
   the door is never drawn, and Hang on wall for a door wall looks like nothing happened (`play/f1/02-front-walls.png`).
   The same camera leaves the floor at about 45% of the stage with 40 px frames at 1366x768 and 20 px at 760x900
   (`play/f1/01-home-hung.png`, `play/f3/s7-760-hang.png`). Fixed: pull back or raise the camera (or draw the door wall
   cut away with its frames and the door gap) so all four walls and the door read, with the walls, not the floor,
   filling the stage. (family:virtual-gallery)
2. **Checklist hides most of the nine checks in a scroll panel.** Checklist, `src.html:221-236`: each row is about
   108 px because `Why` takes its own line, so 3.5 of 9 rows show at 1366x768 and one at 680x425; the Show me buttons
   below the fold are off screen. BUILD.md lesson: a short set of choices never hides in a scroll panel. Seen by all
   three lenses (`craft/out/f5-checklist-1366.png`, `craft/out/f6-checklist-680.png`, `play/f1/17-checklist-scroll.png`,
   `audit-r1/state-mode-04checklist-1366x768.png`). Fixed: `Why` beside `Show me` in the row (both 44 px targets), row
   about 56 px, so all nine fit at 1366x768 and most fit in the preview; two columns at wide sizes if needed. (general)
3. **Seven portrait works are drawn landscape, so each frame shows a strip of picture in a tall empty mat.**
   `art/window, teapot, creek, crows, laundromat, rainglass, nightpool` are 800x622 (prompts ask 4:3) against spec Art
   ("Each 3:4 portrait") and the portrait sizes in `src.html:578-591`; `object-fit:contain` leaves blank mat above and
   below (`audit-r1/state-walk-stop-1366x768.png`, `craft/out/v4-walk-play.png`, detail panel in
   `audit-r1/size-1920x1080.png`). Kitchen Window also has a stray cropped orange object at its right edge. Fixed:
   redraw those seven at 3:4 portrait (no people, no lettering, at most 50 KB each), with the Kitchen Window crop
   cleaned in the redraw. (general)
4. **Portfolio cards show no theme tags and no size.** Select, `src.html:869-874`: cards show title, medium and year
   only; spec Select says cards carry "image, title, medium, size, year and theme tags". Choosing six home works means
   opening all 14 cards one by one (`audit-r1/size-1366x768.png`, `play/f1/14-custom-night.png`). Fixed: size and tags
   on each card, the brief's tag highlighted as it is in the detail panel. (general)
5. **The large label card in Walk covers the wall label it repeats.** `.visitor-label` (`src.html:203`) sits
   bottom-right over the sharp wall label; a long title or note is cut mid-word ("coff", "woke u"), which is exactly
   the "labels run long" case the walk is meant to show (`play/f1/05-walk-longnote.png`, `teaching/f/walk-stop3.png`).
   Fixed: place the card so it never overlaps the current work or its wall label (for example the opposite side of the
   stage from the label, or under the stage). (family:virtual-gallery)
6. **A squeezed label becomes a vertical strip of letters in Walk.** `wallArt` (`src.html:1053-1059`) hides a label
   with under 12 px of room, but `drawWalkArt` and `travelTo` (`src.html:1412`, `:1624`) reset every label's
   visibility to '' while moving and between stops, so a 0-width label with `overflow-wrap:anywhere` shows as a tall
   column of single letters between abutting frames (`play/f2/r9-stop-midtravel.png`, `play/f2/r9-zoom.png`). Fixed:
   keep the squeezed-label rule through every Walk redraw. (general)
7. **No wall label at 1100 px wide and under in Walk.** `src.html:259` hides `.walk-room .sharp-label` at max-width
   1100 while `drawWalkArt` still hides the original (`src.html:1464`), so at 1000x625 and 680x425 the work at the stop
   has bare wall beside it (`play/f1/12-walk-1000.png`). Fixed: at those sizes keep one readable label at the stop
   (the sharp one scaled down, or leave the original visible). (general)
8. **Hang with nothing chosen speaks a Walk line and shows a work that is not in the show.** `welcomeKey()`
   (`src.html:708`) returns `noWalk` in Hang ("...hang it on a wall before walking"), the same line follows Show me on
   an empty show (`src.html:1758`), and the workbench title is Creek After Rain from `fresh()` (`src.html:633`) with
   every control disabled (`craft/b.log` v11-ft-mode, `audit-r1/state-mode-02hang-1366x768.png`). Fixed: a Hang line of
   its own ("The tray is empty. Tap Select and add works to the show."), added to `L` and `voice/lines.json`, and an
   empty workbench with no work title. (general)
9. **The jump line is cut off at every jump during Walk the show.** `travelTo` calls `V.hush()` when the visitor
   leaves a stop (`src.html:1617`), and "Here the story jumps. Nothing ties these two together." runs longer than the
   2 s stop (`src.html:1697`): 6 of 6 jump lines cut about 3 s in (`craft/a.log`, `craft/c.log` v4-walk-play); with
   Step they play whole. Spec Done when 11 wants jump every time. Fixed: at a jump stop, start the move only after the
   jump line ends (other stops keep 2 s); Stop, Step, Back and strip taps still act at once. (general)
10. **Every feedback message is announced twice, and a drag floods the screen reader.** `#hint` (`src.html:530`) and
    `#announce` (`src.html:565`) are both `aria-live="polite"` and `feedback()` (`src.html:721-723`) writes the same
    text to both; a drag rewrites `#hint` on every pointer move (`src.html:1878`). Fixed: one live region, and the drag
    hint updates only when the wall or the rounded drop position changes. (general)
11. **Nine of nine tick with no label note written.** Labels check (`src.html:782`, `:806-809`): titles are prefilled
    and blank notes pass, so the label-writing half of the show is never asked for while the walk shows "0 words" on
    every card (Play cheap pass `play/f1/07-checklist-ticked.png`, Teaching `teaching/t1.js` `untouchedLabels: true`).
    Fixed inside the spec's check 7: the Labels line adds a warning, the way the path crossing does, "n labels have no
    note yet" (not a fail; see Settled calls and the open questions for making it a requirement). (general)
12. **The 145 cm default center line is unexplained, and the cited guide says something different.** `fresh()`
    `src.html:632` (`lines` default 145), the wall readout "145 cm · 57.1 in", the Line check and its Why
    (`src.html:796`). The spec sources only the 120 to 170 slider; the Smithsonian guide (section II.A) centers small
    items no higher than 1015 mm (40 in) for seated viewers. Fixed: the Line Why says 145 cm is a starting height for
    standing visitors that this tool uses, not a rule from the guide, and that the guide hangs small items lower so
    seated visitors can see them. No new number on screen without a source. (general)

## Polish accepted
1. **The first-seen cone is decoration and sits over the work it names.** `.cone-note` (`src.html:219-220`) is a fixed
   triangle at screen center above the frames (z-index 4), aimed at nothing and tinting the named work green; the
   first-seen work is named only in a small mono line (`play/f1/03-walk-door.png`, `craft/out/f4-walk-door.png`).
   Better: aim the cone from the door toward the first-seen frame, draw it at floor level under the frames, and outline
   or spotlight that frame. Do this with blocker 1. (general)
2. **Walk at 680x425: overlays cover the room.** The show card covers the left third and the label card the right third
   of a 190 px stage (`play/f1/11-walk-680.png`). Better: shrink or tuck both overlays at preview sizes so the work at
   the stop stays clear. (general)
3. **Neighbouring wall labels in Walk are blurred smears.** 3 px `.wall-label` text magnified by the camera
   (`src.html:131-134`); only the current stop gets the sharp overlay (`craft/out/v4-walk-play.png`, `play/f1/13-walk-1920.png`).
   Better: blank the text of neighbouring labels while the camera is close (cheapest), or draw them sharp too. (general)
4. **Clockwise / Counterclockwise only changes the camera route.** `src.html:1551`, `:1665`: stops stay in tray order,
   so a student expecting the visit to reverse sees the same sequence. Better: name the button for what it does
   ("Route: clockwise") and say in the hint that the visit order is the tray order. (general)
5. **The walk ends flat.** "Your walk complete · 6 works · 0 story jumps" (`src.html:1704`). Better: add one clause
   comparing First seen with the starred work ("First seen was your starred work" or "First seen was X; you starred
   Y"). (general)
6. **Show me on Anchor is vague.** "Move the selected work or adjust its wall." (`src.html:1754`). Better: say what
   makes a work first seen: the frame closest to straight ahead from the door. (general)
7. **A student whose first tap is Add to show never hears the star.** `selectMore` replaces the welcome
   (`src.html:1006`, audit row 21) and does not mention Star. Better: selectMore ends with "Star the one you most want
   seen." (update `voice/lines.json`). (general)
8. **Order strip numbers and the anchor star are clipped.** `.order-item small` (`src.html:193-201`) sits in a second
   grid row cut by the item border; "3 ★" shows its top half (`craft/zoom-order.png`). Better: put the number before
   the title in the first row. (general)
9. **Seated band wording.** Hang panel line "seated eye level, 109 to 130 cm": the guide's figure is for a wheelchair
   user. Better: "wheelchair user's eye level, 109 to 130 cm". (general)
10. **Double full stop after "a.m."/"p.m." titles.** "Starred: Kitchen Window, 7 a.m.. First seen" (`src.html:793`).
    Skip the added period when the title already ends in one. (general)
11. **"Laundroma t" breaks mid-word in the order strip at 680x425** (`.order-title` overflow-wrap,
    `play/f1/11-walk-680.png`). Break between words only. (general)
12. **Flow line wording.** "0 of 1 allowed jumps in tray order." (`src.html:815`) reads oddly. Better: "0 jumps in tray
    order (1 allowed)." (general)
13. **Truncated control text.** Wall select "Right wall · 6(" with the plan open at 1366x768 (`craft/out/f8-hang-plan.png`);
    tray captions "4 ★ · hun" at 680x425 (`audit-r1/state-compact-full-workbench-680x425.png`). Shorten or let them
    wrap. (general)
14. **Center line slider has no `aria-valuetext`** (`src.html:1139`); announce "145 cm, 57.1 in". Also
    `printShow()` reuses the pattern id `plan-floor-main` (`src.html:1324`); give the print copy its own id. (general)
15. **blockmap (127 KB) and fireescape (98 KB) are over the spec's 50 KB per image.** Re-encode to 50 KB or less if
    they hold up at card and wall size; if not, leave them and note why (the bundle is 1.17 MB, under the 2 MB goal).
    (general)

## Settled calls
- **Tags on cards (Play 3) vs hide the tags (Teaching 2).** The spec says cards carry theme tags, so Play wins: show
  them (should fix 4). Teaching's "hide tags until chosen, then justify each off-theme work" changes what Select
  teaches, so it goes to the open questions.
- **Cheap all-ticks path (Teaching 3, Play 9).** Within the spec only a Labels warning is taken (should fix 11).
  Requiring a written note, a minimum statement length, or locking the star before the walk would change checks 3, 7
  and 8, so they go to the open questions. The checklist and allTicked line are already honest that meaning is not
  checked, which is why this is not a blocker.
- **Voice lines differ from the spec (Craft nit 11).** Keep the code: allTicked "Every measured check is ticked. Review
  the meaning of your show before opening." is the more honest line, given the checks cannot read meaning; welcomeWalk
  "Tap Walk the show." is fine. Do not change these; the spec's Voice text is the thing to update (open questions).
- **Autoplay stop length (Play 15).** Keep 2 s per stop and the 24 s walk (spec, Done when 6); Stop and Step let a
  student read. Only jump stops wait for their line (should fix 9).
- **Blocker 1 fix direction.** Widen the door view rather than turn the camera, so "straight ahead from the door"
  keeps meaning what the Anchor Why and `firstSeen()` say.
- **Show me on ticked rows (Play nit 22).** Leave it: the spec gives each line a Show me, and it is harmless.
- Do not change: the 1 s move / 2 s stop timing with Motion on and off, the keyboard hang path, the Motion-off walk,
  the themeShort lines (growing and night only), the privacy lines, the audit's "#hint covered" rows under modals
  (expected backdrop) and its "focus lost" rows on lower cards (clicks off the fold, not dead controls).

## To the spec's open questions
- **VA:Pr6 at the high school level (Teaching 1).** This is the only tool on module `arts-9-12-portfolio-and-curation`;
  the HS Pr6 standards are about an exhibition's effect on viewers, and nothing here asks what a visitor should leave
  understanding. Option: one "A visitor should leave understanding ..." line written before Walk, shown at the walk's
  end beside the order strip with which stops carried it, and printed on the sheet. Otherwise move Pr6 off this module
  and say so.
- **Justify selection (Teaching 2).** A one-line "why it belongs" for each chosen work without the theme tag, needed
  before Theme ticks and printed on the sheet (and/or let the student tag works before seeing Jordan's tags).
- **Make the checks ask for writing (Teaching 3, Play 9).** Labels needs a written note per work; Statement needs a
  minimum (for example 2 sentences or 20 words); the star locks once Walk is entered, or the Anchor line records
  "starred before the walk" so First seen is a prediction.
- **Source the 145 cm default (Teaching 4)** with a named source in Sources, or pick a sourced default; and decide
  whether a wall line above the seated band should get a note.
- **Spec Voice text** for welcomeWalk and allTicked to match the code (see Settled calls).
- **Art record.** `src.html:14` and `art/prompts.json` credit OpenAI gpt-image for seeds, bowl, fireescape, blockmap,
  tomatoes, vg-wall and vg-floor while the spec says local FLUX only; BASELINE rule 11 allows it, so update the spec's
  Art line.
- **Your theme naming (Play nit 23).** The brief says "Name your own show" but there is no name field in Select; the
  title stays "Your theme" until the Statement dialog.

## Not taken
- Play 10 (hang view mostly floor): folded into should fix 1, same camera.
- Craft 9 (Kitchen Window crop): folded into should fix 3, same redraw.
- Play 15 (longer autoplay stops): against spec timing; see Settled calls.
- Play nit 22 (Show me only on unticked rows): spec gives every line a Show me.
- Play nit 23 (Your theme title): needs a spec decision; sent to open questions.
- Craft nit 11 (voice text vs spec): code kept; spec to move.
- Craft nit 12 (art provenance): record item only, sent to open questions.

## Exit check (2026-11-06)

Cold check by Claude. Frames in `S:/CurioClass-codex-scratch/virtual-gallery/exit/f/` (contact sheets `sheet1-3.png`,
`zoom-left.png`), shots in `exit/shots.json`, audit in `exit/audit-r2/`. Layouts built with `__tool.place()` after
opening Hang, so every position is a legal clamp. No console errors in any shot (an early run that called `place()`
from Select threw in `renderHangTools`; that path is test-only, a student cannot reach it).

### Blocker
1. **Open.** Back-wall layout (`door-back`) and near-door side layout (`door-sides`) now show and outline the named
   frame. But two legal layouts still name a First seen work the picture does not show:
   - Left wall, far end. `door-sides-far` (Blue Teapot at Left wall x=520) and `door-left-corner` (Kitchen Window,
     `place()` clamped to x=577) both read "First seen: ..." over a bare left wall with no outline (`zoom-left.png`),
     while the DOM box for the frame sits inside the window ([96,301,47,76] and [123,299,42,78]). Right wall at the
     same depth paints (`door-sides`, Codex `last-door-edge-right`), so this is a Left-wall paint or clip fault, not
     field of view. Codex's "left-edge probe, unconfirmed" is confirmed on a legal layout.
   - All works on the door wall (`door-only`): bare room, "First seen: Map of My Block", Anchor passes for a work no
     visitor at the door can see. Codex flagged this as a spec decision. The exit check's reading: the Settled call
     was about which way the camera points, not about ranking walls behind the visitor, so excluding the two door
     walls from `firstSeen()` (and failing Anchor with a line such as "No work is in view from the door") is inside
     the blocker's "every work firstSeen() can name is in frame". If the integrator disagrees, it goes to Cory.

### Should fix
1. Fixed. Door wall unfolds below the room with the door gap; 6/6 frames show at 1366x768 and 760x900 (`hang-1366`,
   `hang-760`). Frames are still small (about 25 to 40 px) but walls now fill most of the stage.
2. Fixed. Checklist in two columns at 1366x768, all nine rows with Why and Show me visible; 680x425 shows 8 of 9,
   Flow under the fold (`checklist-1366`, `checklist-680`). Audit's "scroll panel" lead at 680 and 375 is this one row.
3. Fixed. Seven works now 600x800, under 50 KB each (Codex `after-art.json`); portrait frames fill their mats in Walk
   and Select (`walk-stop-1366`, `select-1366`).
4. Fixed. Cards show size and theme tags, brief tag highlighted (`select-1366`).
5. Fixed. Long note reads whole on the wall label, duplicate is a disclosure under the room, no overlap
   (`walk-stop-1366`).
6. Fixed. `data-squeezed` kept through redraw (`src.html:527`, `:1542`); Codex `proof/squeezed-moving.png` shows no
   letter strip.
7. Fixed. Readable current wall label at 1000x625 and 680x425 (`walk-stop-1000`, `walk-stop-680`).
8. Fixed. Empty Hang: "The tray is empty" workbench, emptyHang line spoken (`empty-hang`, audit row 1).
9. Fixed. Three of three jump lines spoken whole, about 5 s apart (Codex `proof/jump-autoplay.json` vlog); code awaits
   the line.
10. Fixed. Live regions are `#hint` and `#own-message` only (shot JSON); drag hint writes on change.
11. Fixed. Labels row shows "Warning: 6 labels have no note yet." (`checklist-1366`).
12. Fixed. Line Why says 145 cm is the tool's standing start, not the guide's, and that the guide hangs small items
   lower (Codex `jump-autoplay.json` checks text).

### Polish (bulk spot-check)
Fixed: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15 (seen on the frames above or in the check texts).
Partly: 1 (cone and outline work where the frame paints; missing in both blocker cases). 13 (tray captions "1★ hung"
fit at 680x425, `hang-680-tray`; the wall select still reads "Back wal" there).

### Regressions
None found in the default screen, each mode once, or the frames tied to the fixes. Hang at 680x425 opened in Plan
(restored state), which is fine.

### Gate
1. Done when: open. Done when 3 (first seen from the door) fails for the two blocker layouts.
2. Codes: unchanged this round; VA:Pr6 depth stays on the spec's open questions.
3. Solo defaults: work (default screen, empty Hang guidance, Select with tags).
4. Sensitivity: rule 5 does not apply (no lens or merge flag).
5. No blocker or should-fix open: no, blocker 1.
6. Bundle clean: 1.12 MB (under 2 MB), no console errors, no em dashes in src.html; network not re-measured (audit cut short), Codex offline-contract probe shows zero requests.
7. Voice: 37 lines in `voice/lines.json`, matches Codex's allLines count; held-click table clean, emptyHang and
   selectMore heard where expected.

## Audit pilot
- The audit ran into the 1500 s limit (exit 124) after the click and voice tables; stress checks and the network
  section were not saved. Sizes, mode states and held clicks came through.
- Leads confirmed: checklist row cut by the scroll panel at 680x425 and 375x812 (one row, Flow, accepted as "most
  fit"); Add to show as a first tap does not hear the welcome (accepted by polish 7, selectMore now carries the star).
- Leads wrong or expected: 3 px `wall-label` and 4 px intro text in the cutaway and compact states (scaled 3D text,
  the readable sharp label is drawn separately); "focus lost" on lower cards (off the fold); clipped `order-title`
  at 1366 for "1 ★ Kitchen Window, 7 a.m." (ellipsis by design).
- Missed: the blocker. Every door-view frame has an in-window DOM box, so a box-based check cannot see that a
  Left-wall frame never paints; only the picture shows it.
