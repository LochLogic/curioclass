# Craft lens: virtual-gallery (round 1)

Cold Craft lens, 2026-11-05. Bundle `tools/virtual-gallery/virtual-gallery.html` as built (not re-bundled).
Own frames and logs: `S:/CurioClass-codex-scratch/virtual-gallery/craft/out/` (shots in `shots.json`, logs `a.log`,
`b.log`, `c.log`). Shared audit: `S:/CurioClass-codex-scratch/virtual-gallery/audit-r1/`.

Counts: blocker 0, should fix 4, polish 5, nit 6.

## Findings

### Should fix

1. **Seven portrait works are drawn as landscape pictures, so every frame shows a small picture floating in a tall
   empty mat.** Where: `art/prompts.json` (window, teapot, creek, crows, laundromat, rainglass, nightpool all ask
   `"aspect": "4:3"`, and the files are 800x622), against spec Art ("Each 3:4 portrait, the listed size read as width
   x height") and the sizes in `src.html:578-591` (30 x 40, 28 x 36, 46 x 61, 23 x 30, 36 x 48, 40 x 50, 50 x 70, all
   taller than wide). The frame is drawn at the real portrait size and the image is `object-fit:contain`, so a 46 x 61
   cm canvas shows as a landscape strip with blank mat above and below; the card says "46 x 61 cm" while the picture is
   wider than tall. How seen: `audit-r1/state-walk-stop-1366x768.png` (Creek, grey bands top and bottom),
   `craft/out/v4-walk-play.png` (Laundromat), `audit-r1/size-1920x1080.png` (detail panel: a tall empty box with a
   landscape creek in the middle); image sizes read with PIL. Better: redraw these seven at 3:4 (or the listed ratio)
   so the picture fills its frame, as busstop, seeds and tomatoes already do. Tag: general.

2. **The jump line is cut off mid-sentence at every jump during Walk the show.** Where: `src.html:1617` (`travelTo`
   calls `V.hush()` when the visitor leaves a stop) with the 2 s stop at `src.html:1697`. "Here the story jumps.
   Nothing ties these two together." runs longer than the 2 s pause, so the move to the next stop hushes it. How seen:
   `craft/a.log`/`c.log` v4-walk-play: 6 jumps, 6 `jump` spoken, all 6 with `cut: hush` about 3 s after starting.
   With Step (v16) the 4 jump lines play whole. Better: hold the stop until a jump line has finished (or start the move
   only after it ends), or drop it with `valid` instead of a hush. Tag: general.

3. **The checklist shows only part of the nine checks.** Where: Checklist, `src.html:227-236` (each row about 108 px
   tall, because the `Why` summary takes its own 44 px line under the text). At 1366x768 the list scrolls 1041 px in a
   422 px box (3.5 rows visible), at 680x425 1041 in 132 (one row). A student cannot see their show's status at a
   glance, which is the point of the mode. How seen: `craft/out/f5-checklist-1366.png`, `f6-checklist-680.png`,
   `audit-r1/state-mode-04checklist-*.png`; audit lead "choices cut short by a scroll panel" at every size. Better:
   put `Why` beside `Show me` (both 44 px targets, side by side) so a row is about 56 px; nine rows then fit at
   1366x768, and the preview sizes show most of them. Tag: general.

4. **Every feedback message is announced twice to a screen reader.** Where: `src.html:530` (`#hint` is
   `aria-live="polite"`), `src.html:565` (`#announce` is also polite), `src.html:721-723` (`feedback()` writes the same
   text to both). Also `src.html:1878`: a drag rewrites the live `#hint` on every pointer move, so a screen reader is
   flooded while dragging. How seen: code read. Better: one live region (drop `#announce`, or take `aria-live` off
   `#hint` and keep the announcer), and update the drag hint only when the wall or the rounded drop position changes.
   Tag: general.

### Polish

5. **Order strip numbers and the anchor star are clipped.** Where: Walk, `.order-item small` (`src.html:193-201`):
   the stop number sits in a second grid row cut by the item's bottom border; "3 ★" shows only its top half.
   How seen: `craft/zoom-order.png` (from `out/f4-walk-door.png`, 1366x768). Better: put the number in the first row
   (before the title) or give the item room for it. Tag: general.

6. **Neighbouring wall labels in Walk are blurred smears.** Where: Walk stops, `.wall-label` at a 3 px font
   (`src.html:131-134`) magnified by the 3D camera; only the current work's label gets the sharp overlay
   (`drawWalkArt`). How seen: `craft/out/v4-walk-play.png`, left edge: a large white label with unreadable grey blur.
   Better: draw any label that is in view at a stop with the same sharp path, or blank its text while the camera is
   close. Tag: general.

7. **Hang with nothing chosen speaks a Walk line.** Where: `welcomeKey()` `src.html:708` gives `noWalk` in Hang:
   "Tap Select to choose a work, then tap Hang and hang it on a wall before walking." The student is already in Hang
   and has not asked to walk. The same line is the hint after `Show me` on an empty show (`src.html:1758`). How seen:
   `craft/b.log` v11-ft-mode (first tap Hang, `noWalk` spoken); audit table rows 1 and 2. Better: a Hang line of its
   own ("The tray is empty. Tap Select and add works to the show."), in `L` and voice/lines.json. Tag: general.

8. **The first-seen cone is drawn over the artwork it names.** Where: Walk at the door, `.cone-note`
   (`src.html:219-220`) sits above the frames (z-index 4), tinting the first-seen work green. How seen:
   `craft/out/f4-walk-door.png` (Bus Stop, 10 p.m. under the cone). Better: draw it lower (floor level, below the
   frames) or as an outline, so the work the student is judging stays clean. Tag: general.

9. **Kitchen Window has a stray cropped object at its right edge.** Where: `art/window.webp`, an orange strip of a
   neighbouring element cut by the picture edge. How seen: `audit-r1/size-1920x1080.png`, first card. Better: fold into
   the redraw in finding 1. Tag: general.

### Nit

10. Two images are over the spec's 50 KB per-image cap: blockmap 127 KB, fireescape 98 KB. The bundle is 1.17 MB, well
    under the 2 MB goal, so this is only a spec mismatch. Tag: general.
11. Lines differ from the spec's Voice section: welcomeWalk is "Tap Walk the show." (spec: "...to follow a visitor
    through the door."), allTicked is "Every measured check is ticked. Review the meaning of your show before opening."
    (spec: "Every check is ticked. Your show is ready to open."). voice/lines.json matches the code word for word; the
    integrator decides whether the spec or the code moves. Tag: general.
12. Art provenance: `src.html:14` and prompts.json name OpenAI gpt-image for seeds, bowl, fireescape, blockmap,
    tomatoes, vg-wall and vg-floor, while the spec says local FLUX only. No people in any of the 16 (all
    `people: false`, none seen); BASELINE rule 11 allows Codex drawing, so this is a record item. Tag: general.
13. Truncated control text: the Wall select reads "Right wall · 6(" with the plan open at 1366x768
    (`out/f8-hang-plan.png`); tray captions read "4 ★ · hun" at 680x425 (`audit-r1/state-compact-full-workbench-680x425.png`).
    Tag: general.
14. The center line slider has no `aria-valuetext` (`src.html:1139`), so it is announced as "145" with no unit. Add
    "145 cm, 57.1 in". Tag: general.
15. `printShow()` builds a second SVG with the same pattern id `plan-floor-main` as the open plan (`src.html:1324`),
    a duplicate id in the page while the print sheet exists. Tag: general.

## Contract

- One file, 1,170,809 bytes (2 MB goal met). No `http` URLs in the bundle; `performance.getEntriesByType('resource')`
  empty after a full hang (`f1-hang8`). No console errors or exceptions in 27 shots (one exception came from my own
  harness calling `__tool.place` outside Hang, not reachable from the page).
- Kit used: `Curio.voice`, `Curio.init`, `Curio.tone/yes`, `theme-912`, kit focus ring. Not re-implemented.
- Frame times (rAF deltas, 1366x768, muted headless Chrome with software rendering): Walk the show with 8 works,
  1863 frames, median 16.7 ms, p95 16.7 ms, max 33.4 ms, 1 frame over 20 ms. Motion off walk: max 16.8 ms.
- Access: every control is a real button, select or range with 44 px targets (audit clean at all sizes); kit
  focus ring visible; keyboard hang path works (`k1`: Enter on a tray work hangs it at 400 cm, ArrowRight x2,
  Shift+ArrowRight, ArrowLeft gives 430 cm; `k2`: Delete returns it, focus stays on the tray work). Pass/fail is icon
  plus words ("Meets check" / "Needs attention"), never color alone. Contrast of small text checked: medium line
  7.5:1, save note 7.8:1, tray caption 7.1:1, visitor small 6.3:1. Motion and Sound work (audit Motion off clean).
- Words: no em dashes in src, notes, lines, prompts; "Curio Class" everywhere; classroom-safe; privacy stated in the
  footer, the own-pictures line and the checklist note.
- Art tokens: all 16 `art:` tokens have prompts.json entries and files.

## Voice check (held clicks 0.12 s, Sound on, Motion on, 1366x768)

| line | kind | run | expected | spoken |
|---|---|---|---|---|
| welcomeSelect | how | card first tap, then 5 adds | 1 | 1 |
| selectMore | how | 5 adds, 3.5 s apart | 1 | 1 (then silent x4) |
| welcomeHang | how | 5 hangs | 1 | 1 |
| lightHow | how | 5 hangs; then Light x5 | 1 | 1 |
| hangMore | how | 5 hangs | 1 | 1 |
| inspect (Hang welcome, work hung) | how | Hang entered 5 times | 1 | 1 |
| welcomeWalk | how | Walk entered 5 times | 1 | 1 |
| firstSeen | event | Walk entered 5 times | 5 | 5 |
| welcomeChecklist | how | Checklist entered 5 times | 1 | 1 |
| themeShort | event | growing, night, growing, city, night | 4 | 4 (none for city) |
| jump | event | Walk the show, 6 jumps | 6 whole | 6, all cut (finding 2) |
| jump | event | Step x5, 4 jumps | 4 | 4 whole |
| walkComplete | event | end of walk | 1 | 1 |

- Stale lines (v7, taps 0.2 s apart through Walk, Step x3, Hang, Checklist, Walk, Walk the show, Stop): every line was
  cut or dropped by the next action; nothing played after its moment.
- First tap: Read speaks the hint only (v8); Sound says nothing, Sound on again brings welcomeSelect once (v9); Tab
  brings the welcome (v10); a mode button speaks that mode's welcome (v11, but see finding 7); Walk the show skips the
  welcome and speaks only its own line (v12); Step brings continueWalk (v16).
- Read during the welcome cuts it and speaks the hint (v13); Read works with Sound off (v14); a mode change right after
  Read speaks at once (v13, 0.1 s after the tap).
- Order: lines follow the actions in every run.
- Each spoken line was checked against the frame at its time; finding 7 is the one that does not fit its screen.

## Audit pilot

- Confirmed: "choices cut short by a scroll panel" on Checklist and clear-confirm (finding 3).
- Confirmed but not a finding: "#hint covered" in label-open, statement-open and clear-confirm: the modal backdrop
  dims the hint, but each dialog carries its own instructions and Done button.
- Wrong or harmless: "welcome not heard" after a first tap on Add to show follows the spec (welcomeSelect is stale once
  a work is added), though that student never hears "Star the one you most want seen" (a Play/Teaching call).
  "focus lost" on cards 15 to 18 and "nothing changed" / "covered" on the lower Why and Show me rows: the click landed
  on the footer or outside the scroll box for controls cut by the fold, not dead controls.
- Missed: landscape art in portrait frames (1), the jump line cut during the walk (2), the double live region (4),
  clipped order-strip numbers (5), blurred neighbour labels (6), the cone over the art (8).

No cultural, Native or hard-history content found; nothing flagged for a sensitivity review.
