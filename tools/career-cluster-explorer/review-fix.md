# career-cluster-explorer: review fix (Trails jobs on the map)

2026-10-29. Cory's note: "The trail section of the tool should have the jobs and descriptions over the map so they can be more of the focal point."

## What changed (src.html, notes.md)

- `drawTrailCards()` draws each stop's job on the map, in `#pan` coordinates so it moves with the town:
  - the current stop: a card at its numbered dot (Stop N of M, the job's emoji, title, a lantern in the cluster's color with the cluster name, and the stop's line), joined to the dot by a short yellow pointer;
  - every earlier stop: a compact label at its dot (stop number and job title; one label per dot, one row per stop, so "1-4" at the gate lists four jobs) with a thin pointer;
  - the last stop: the end line ("This bag of kettle corn took 4 clusters", from each trail's own `end`) with the cluster chips, pinned at the top of the town.
- Placement tries spots around the dot (above, below, beside, corners, at three distances, then top or bottom of the town) and scores the whole layout (card plus every label): nothing may overlap a dot, another card or label, or the end line, or leave the town. If no clean layout fits it shrinks the card (lg 340, md 290, sm 240, xs 200, then `flat`, a wide short card that drops the Stop line, which the panel still shows). A last-resort pass may cover an earlier or later dot, never this stop's or the next stop's; in the final runs it was never needed.
- `panToTrail()` pans so the card and its dot are in view and clear of the ◀ ▶ buttons, then takes in the most recent earlier stops while they fit. Motion off: instant pan, no card fade (Motion on: a 0.3 s fade-up of the card only).
- The panel keeps a short card (Stop N of M, emoji, title; cluster and line are screen-reader text). The panel's end row is no longer shown (the map has it). Back, Next, Open career and the trail picker are unchanged. Stack layouts now only scroll the town back into view if it scrolled off.
- At phone widths (under 560 px) the ◀ ▶ buttons hide in Trails only: at 375 they covered the cards. Next and Back pan the town; drag, wheel, arrow keys and the minimap still work. Noted in notes.md.
- Found on the way: the kit's `.calm *{transition-duration:.01ms}` makes every property transition, so a size read straight after a class change was stale in Motion off (wrong card size and overlaps). The trail layers set `transition-property:none`. The kit rule may bite other tools that measure after a class change.
- No line text changed: `allLines()` equals voice/lines.json (9 lines), so every clip still matches. No art touched.

## Checks

- Bundled: `python scripts/bundle_tool.py career-cluster-explorer`, 343 KB. `check_tools.py`: ok.
- Driven with scripts/drive.py (ports 9301 and 9302, host 8821): every stop of all 5 trails (27 stops) at 1366x768, 1280x720, 1920x1080, 1000x625, 800x500, 680x425, 760x900 and 375x812 (host), Motion on (final-on/) and off (final-off2/): 432 frames. Each frame's script measured the card, the labels, the end line and the dots: 0 overlaps, the card fully inside the town, and not under a ◀ ▶ button, in all 432. No console errors (only the host server's favicon 404).
- Real held clicks: Trails, Kettle corn, Next x4 at 1366 (Motion on and off): trailEnd4 spoken after the welcome, focus lands on Open career. Ankle trail by the select plus Next at 680. A drag in Trails moves the cards with the town.
- Frames in S:/CurioClass-codex-scratch/review/career-trails/ (contact sheets sheet-on-*.png). Best: final-on/1366x768-t0-s5.png, final-on/1920x1080-t1-s6.png, final-on/h375x812-t3-s5.png.

## Left

- The full chain does not fit on screen at once on any size (the town is 2400 units wide at stage height), so the end view shows the last card, the end line and the stops that fit; the rest are labeled where they are when the student drags. A zoom-out view at the end would be the next step if Cory wants every stop in one look.
- At 680x425 and 375 the card can sit a long way above or below its dot (the flat card) on the twisted-ankle ending, where four stops crowd one corner.
- At 760x900 cards use the small size (the stage is short for its width); readable but smaller than at 1366.

## Town art

2026-10-29. Cory's note: "the background graphics are not good and need upgraded."

### What changed (src.html, tool.json, notes.md, preview.svg)

- `drawScene()` keeps the code sky gradient, stars, moon, string lights and poles, fence, power lines (poles moved down 20 to stand on the painted hills), Main Street road with crosswalk and lane lines, the weather board and the big screen. Every old flat place drawing is gone (far hills, ridge, ground, foreground grass, airport hill and all 33 places).
- New: `town-land.webp` across the bottom (y 309 to 900; the barn sprite covers its little lit house), then the 33 sprites as SVG `<image href="art:town-...">` through one helper, `put(href, w, h, left x, ground y, scale)`, drawn back to front (turbine, soccer, Ferris, radio, stage, art row, barn, bridge, gate, kettle, first aid, food trucks, theater, braids, then the front row, then Main Street). Scales 0.6 to 1.3 so a car or truck stays smaller than a stall, a stall smaller than a building, and the hotel and clinic tallest on Main Street.
- The river: the bridge sprite brings its own water; below it the old river is now a soft teal-to-navy gradient with faint ripples, so the river marker still sits on water.
- The road is narrower and lower (y 818 to 890) so the shops stand on the sidewalk above it; the police car, crosswalk and delivery truck are on it.
- Signs stay code text over the art: FAIR on the gate arch, 72° CLEAR on the board, 2 : 1 on the screen, LIBRARY on the library pediment, SALE on a small red board over the house's painted sign, $ above the bank pediment, HARDWARE on the orange awning, HIRING on a card in the shop window, HOTEL on the hotel roof line.
- The plane sprite faces left, so its dashed trail now runs off to the right (it flies left).
- The Ferris wheel sprite first kept a lot of its green key between the spokes. A display-time filter covered it for one pass; the coordinator then re-keyed `town-ferris.webp` (magenta key) and removed the filter, so src.html has no filter now (see Round 2).
- `police` is now "A police car at the crosswalk" (the sprite replaced the drawn officer; careers unchanged; not a voiced line).
- Minimap silhouette redrawn for the new skyline (bigger Ferris, shorter clinic, wider hotel).
- Unused `poly` and `win` helpers removed. Header comment, tool.json sources and notes.md now say the town is painted; tool.json has the FLUX credit line.

### Moved HOT ids

- `bank` (1960, 520) to (1960, 600): the old spot was sky above the painted bank.
- `upstairs` (1800, 400) to (1790, 500): the old spot was above the painted clinic's roof; it now sits on its upper windows.
- Nothing else moved. `field` stays between the soccer light poles at their height.

### Checks

- Bundle 772 KB (art about 335 KB as WebP, about 450 KB once inlined). `check_tools.py`: ok.
- Trails layout check (the scoring script from career-trails, every stop of all 5 trails): 1366x768 Motion on 27/27, 1366x768 and 375x812 Motion off 54/54, 375x812 Motion on 27/27: 0 overlaps with dots, card always in the town and never under a ◀ ▶ button. No console errors (only the host server's favicon 404).
- Frames in S:/CurioClass-codex-scratch/review/career-town/: `full/scene.png` and `full/scene-hot.png` (the whole 2400x900 town at 1:1, with and without every marker drawn on), `fest/fest-1366-p0..p4.png` (Festival panned left to right at 1366x768), `fest/fest-1366-calm-p2.png` (Motion off), `fest/fest-1920.png`, `fest/sheet-h375.png` (phone, panned), `sheet-trails-last.png` and `sheet-trails-h375.png` (each trail's last stop), all Trails frames in `trails-on/`, `trails-off/`, `trails-h/`, and `preview.png` (the new card).

### Open concerns

- (Closed in Round 2: the Ferris wheel was re-keyed and the filter removed.)
- The gate sprite has the word "Ticket" painted on its booth; it reads fine but is the one bit of painted text.
- The Ferris wheel is the biggest thing in town (346 wide) and its legs reach behind the gate and kettle stand; it reads as the centerpiece but crowds that corner.
- The soccer pitch sits on the crest of the hills; at full size it looks like a field up the hill rather than on the fairground.
- The town art is FLUX art with `"review": "pending"` in prompts.json; nobody has signed off each sprite yet.

## Round 2

2026-10-29, from final-art.md (Final look: FIX, 2 must, 4 should, 7 polish). New art from the coordinator: art row (one grounded group, no people, 195x140), soccer field (flat, 247x75), bank (no lettering, 169x194), gate (re-keyed), Ferris (re-keyed, filter removed). No art redrawn or re-keyed here.

### What changed (src.html)

- **Art row (must 1, 2):** the new sprite at 0.7 stands on the fairground left of the field (x 1222, ground 692), clear of the pitch.
- **Soccer field (should 3, 5):** the flat field at 0.8 lies on the fairground just behind the fence (x 1368 to 1566, y 639 to 699), below the hill crest, so it reads as a field at the fair, not a slab on the ridge. Two code light towers with a glow (the old idea) stand at its back corners. First aid moved off it, to the right (x 1560, 0.55). Food trucks moved to the front row (0.62) and the braids booth forward (ground 790) to make room.
- **Signs (should 4):** the library marker moved to the doorway, the hardware marker to the shop's left wall; LIBRARY and HARDWARE read whole. $ moved into the new bank's pediment.
- **put() sizes:** artrow 195x140, soccer 247x75, bank 169x194 (0.9), so nothing is stretched.
- **Polish:** Ferris wheel 0.62 (hub still at 1000, 420; base 678), so the gate, kettle stand and stage have air. Fire truck 20 right, off the river. Road gets a soft left end (gradient over its first 64 units, rounded corners). Minimap skyline lighter (#8d82c4 on #0d0a22). The old `#unkey` comment is gone and the Town art note is corrected.
- **375 Trails labels (polish 12):** `clipLabs()` hides an earlier-stop label, and its pointer, while any part of it is outside the stage; it runs after each layout and on every pan, so a label shows again once it is fully in view. No half words at the edge.
- **375 ankle ending (polish 13):** with `field` and `firstaid` moved, the layout now puts the Physical Therapist card beside stop 5 (sm card, not the flat fallback).

### Moved HOT ids (this round)

`artrow` (1290, 530) to (1290, 640); `field` (1420, 420) to (1467, 670); `firstaid` (1450, 600) to (1603, 655); `food` (1330, 680) to (1316, 745); `braids` (1560, 720) to (1543, 745); `library` (1700, 600) to (1700, 662); `hardware` (2000, 700) to (1958, 728). Earlier round: `bank`, `upstairs`.

### Checks

- Bundle 835 KB.
- Trails layout check, every stop of all 5 trails: 1366x768 Motion on 27/27, 1366x768 and 375x812 Motion off 54/54, 375x812 Motion on 27/27; 0 overlaps with dots, cards always in the town and never under a ◀ ▶ button. No console errors (only the host's favicon 404).
- Frames in S:/CurioClass-codex-scratch/review/career-town/round2/: `fest/fest-1366-p0..p4.png`, `fest/fest-1366-calm-p2.png`, `fest/fest-1920.png`, `fest/fest-h375-p*.png`, `sheet-trails-last.png`, `sheet-trails-h375.png`, `trails-on/`, `trails-off/`, `trails-h/`, zooms `z-hardware.png`, `z-ferris.png`, `z-roadend.png`. Whole town at 1:1: `../full/scene-hot.png`. preview.svg regenerated.

### Open

- Ferris spokes: a thin pink edge is visible at 1:1 (z-ferris.png), mostly on the outer rim. At 1366 it is barely there and reads as trim; a tighter re-key would remove it.
- Bank sprite: fine, no lettering. Gate: no green specks seen in the frames.
