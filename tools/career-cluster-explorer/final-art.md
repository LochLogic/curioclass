PASS
Re-check counts: must fix 0, should fix 0, polish open 2 (known, not done). Round 1 counts: must 2, should 4, polish 7.

# career-cluster-explorer: Final look after Cory's review (painted town, Trails cards on the map)

## Re-check (round 2), 2026-10-29

Same agent, ports and scratch. Rebuilt bundle (19:35, 831,384 bytes). I rescanned the sprites, re-rendered the whole
2400x900 town with and without markers, and re-ran all 147 shots. Everything is in
S:/CurioClass-codex-scratch/review/career-final-art/r2/ (scene-m0.png, scene-m1-0/1/2.png, z-*.png, shots/, run.log,
sheet-h375-town.png, sprites-*.png). Chrome and the 8861 server are closed.

| # | Finding | Now | Frame |
|---|---|---|---|
| 1 | Art row floating on the pitch | Closed: one grounded stall with an easel and a flower cart, standing on its own dirt patch on the fairground left of the field | r2/scene-m0.png, r2/z-artrow.png |
| 2 | People in the art row picture | Closed: the easel and the stall hold sunflower paintings only, no figures | r2/z-artrow.png |
| 3 | Soccer pitch as a slab on the hill | Closed: a flat field on the fairground behind the fence, two code light towers, first aid tent beside it, not on it | r2/scene-m0.png, r2/shots/fest-1366x768.png |
| 4 | Markers over LIBRARY and HARDWARE | Closed: both words read whole at 1366 and on the 1:1 town; HIRING and $ also clear | r2/shots/pan-1366-p4.png, r2/scene-m1-2.png |
| 5 | `field` marker in the sky | Closed: on the pitch. All 37 markers sit on the place they name (artrow, field, firstaid, food, braids, library and hardware re-checked after their moves) | r2/scene-m1-1.png, r2/scene-m1-2.png |
| 6 | Green key on the gate posts | Closed: post feet are clean (19 faint green edge pixels left in the file, none visible) | r2/z-gate-scene.png |
| 7 | Ferris crowding and fringe, stale comment | Closed for crowding (0.62: gate, kettle stand and stage have air) and the comment (no `unkey` in src.html). The spoke edge is now a muted purple, not pink; about 5,470 edge pixels still meet my magenta test, but nothing reads as fringe at 1366 or 1920. Left as known polish | r2/z-ferris-file.png, r2/scene-m0.png |
| 8 | Fire truck on the river edge | Closed: on the bank | r2/z-fire-scene.png |
| 9 | Bank door lettering | Closed: the redrawn bank has none | r2/sprites-dark.png |
| 10 | Road end | Closed: soft fade with rounded corners | r2/scene-m0.png |
| 11 | Minimap contrast | Closed: the skyline is now a light lavender shape, clearly visible | r2/z-mini.png |
| 12 | 375 labels cut mid-word | Closed: no half words in any of the 27 phone frames. Side effect: a label whose dot is in view but whose label would cross the edge is hidden, e.g. "Coach / Athletic Trainer" at the 1-2 dot on the ankle ending. Known polish; the label returns once the town is dragged | r2/sheet-h375-town.png, r2/shots/h375-ankle-s5.png |
| 13 | 375 ankle card far from its dot | Closed: the card sits beside stop 5 (xs card, not the flat fallback) | r2/shots/h375-ankle-s5.png |

No regressions:
- **Trails layout:** 121 of 121 measured layouts are clean (no card or label over a dot, no overlaps, card fully in
  the town). The sizes are the same as round 1: every stop of all 5 trails at 1366 Motion on and off and at 375, plus
  stop 2 and the last stop at 1920, 1280, 760x900 and 680x425. No flat fallback cards remain. Titles are 23 px at
  1920, 19 px at 1366 and 14.5 to 15.5 px at 375.
- **Motion off:** reduce is true with 0 animations.
- **Voice:** in the held-click Trails run, welcomeTrails starts at 1.34 s and trailEnd4 at 7.09 s, matching the end
  line.
- **Bundle:** 0 `art:` tokens, all 34 sprites inlined (md5 matched), no network requests, no em dashes. There are no
  console errors other than the local favicon 404.
- **Panned shots:** the check marks on places in r2/shots/pan-*.png come from earlier card shots in the same test
  profile (saved places). This is not a finding.

Sensitivity on the redrawn art (art row, soccer field, bank, gate, Ferris): no people, faces or hands; no lettering
except the gate's "Ticket"; no symbols, brands or stereotypes. The whole set still has no people. careers.json is
unchanged, so the career cards stand as passed.

Cory's two notes now read as clearly answered. The middle of the fair, the one weak patch in round 1, now looks like
part of the same painted town.

Known, not done (Review Desk "changed" note): the Ferris spoke edge (item 7) and the hidden in-view labels at 375
(item 12).

---

Round 1 findings follow, unchanged.

Cold check on 2026-10-29 against REFINE.md (Final look), STANDARDS.md and BASELINE.md, after reading handoff.md,
final.md, refine/final-sensitivity.md and review-fix.md (both sections). This file covers the tool as it is now; final.md
is left as it was.

Bundle checked as built by the builder (career-cluster-explorer.html, 19:10, same time as src.html). Driven with
scripts/drive.py on Chrome ports 9341 and 9342 (own profiles), the 375 host served from the tool folder on 8861 (the
existing host.html, not rewritten). 147 shots, all looked at as frames or contact sheets. Everything is in
S:/CurioClass-codex-scratch/review/career-final-art/ (shots/, run.log, scene-*.png, z-*.png, sprites-*.png,
sheet-h375.png). Chrome and the server were closed after the run.

## Cory's two notes: do they read as answered?

- **"The trail section should have the jobs and descriptions over the map."** Yes, clearly. The current stop's card
  (Stop N of M, emoji, title, cluster lantern, the stop's line) sits on the map at its numbered dot with a pointer,
  earlier stops carry name labels, and the last stop pins "This bag of kettle corn took 4 clusters" with chips at the
  top of the town (shots/tr-1366-kettle-s5.png, shots/tr-1366-lights-s3.png, shots/tr-1920x1080-ankle-end.png,
  shots/trcalm-1366-bridge-s5.png). The panel now only repeats the title. The jobs are the focal point.
- **"The background graphics are not good and need upgraded."** Mostly yes. The town now reads as one painted
  storybook place at night with one palette and outline style (scene-m0.png, shots/fest-1366x768.png,
  shots/pan-1366-p2.png, shots/pan-1366-p4.png). Main Street, the farm, bridge and river, and the front row of
  tents are a big step up. The one patch that still looks unfinished is the middle hill (soccer pitch, art row, first
  aid tent), which is the must-fix below. Cory will notice it, because it sits in the center of the default view at
  every size.

## Must fix

1. **Art row is floating clutter on top of the soccer pitch** (scene-m0.png around x 1230 to 1380, y 520 to 600;
   z-soccer.png; shots/fest-1366x768.png right edge; shots/card-1366-artrow.png). `town-artrow.webp` is a scatter
   of loose objects: a window and a wall lantern hanging in the sky, an easel whose picture floats above its leg, a
   sandwich board, and the parade float. Placed at (1214, 606, 0.8) the float and sandwich board stand on the green
   pitch, and the window, lantern and picture hang in the air left of it. It reads as debris on the field, not as
   "art row: the festival poster, a photo booth and the costume parade float". Needs a redrawn sprite of one grounded
   group (a poster board, a photo booth, a float) placed on the fairground in front of the hill, not on the pitch.
2. **The art row picture shows people from the local model** (z-artrow.png: the easel painting is two figures, an
   adult in a pink dress and a child). STANDARDS (Art): never people, faces or hands from a local model. It is small
   in the scene (about 20 px), but it is a person picture nobody reviewed. The redraw in item 1 should give the
   poster a non-figure design (ask for a blank or patterned poster, worded positively).

## Should fix

3. **The soccer pitch reads as a raised slab on the hilltop** (z-soccer.png, scene-m0.png x 1060 to 1250 at the
   2000-wide view). The sprite has a thick dark edge under it, so at scale 1.3 on the crest it looks like a table top
   or a field up on the ridge, and the first aid tent sits on its front edge. With item 1 this whole middle patch
   looks stacked. Options: a flatter field sprite set lower behind the fence, or smaller and set back, with the first
   aid tent clear of it. The `field` marker (1420, 420) then needs to move onto the pitch (item 5).
4. **Markers cover their own code signs** (z-signs.png, shots/pan-1366-p4.png, shots/fest-760x900.png): the library
   marker sits on the middle of "LIBRARY" (reads "LIB(dot)ARY") and the hardware marker on "HARDWARE" (reads
   "(dot)ARDWARE"). Move either the marker (for example library to the doorway, hardware to the window, as bank and
   upstairs were moved) or the sign text so both read. The other signs (FAIR, 72° CLEAR, 2 : 1, $, SALE, HIRING,
   HOTEL) sit cleanly on the art.
5. **The `field` marker floats in the sky** between the light poles, about 100 scene units above the pitch
   (scene-m1-1.png, shots/pan-1366-p2.png, also the "1-2" dot in shots/tr-1920x1080-ankle-end.png). It names "the
   youth soccer game under the lights"; every other marker sits on its place. Put it on the pitch once item 3 settles
   where the pitch goes. Every other tap marker checks out on its place (scene-m1-0/1/2.png); `weather` sits on the
   board's pole just under the board, which is fine.
6. **Green key leftovers on the gate** (z-gate.png): the two light green bow-tie shapes at the feet of the gate
   posts are key green that survived (95 strongly green pixels in `town-gate.webp`, 21 on the edge). They show as
   bright green specks right beside the FAIR arch at every size. Re-key or crop them.

## Polish

7. **Ferris wheel crowding and fringe.** The wheel is the biggest thing in town (346 wide) and its legs run behind
   the gate, the kettle stand and the stage (z-gate.png, scene-m0.png). It reads as the centerpiece and the overlaps
   are front-to-back correct, so this is polish, not a blocker; a slightly smaller wheel (about 0.62) would give the
   gate and kettle stand air. The file on disk is now magenta-keyed (6,606 semi-transparent magenta edge pixels, 18
   green): the spokes have a thin pink outline (z-ferris-top.png, z-ferris-scene.png). On the purple sky it reads as
   neon trim, but it is key fringe. review-fix.md describes a green key and an `#unkey` filter; that filter is no
   longer in src.html, and the comment at src.html line 625 still describes it. Update the comment and the note.
8. **Fire truck parked on the river's edge** (z-fire.png): its painted ground strip overhangs the water. Move it a
   little right (about 20 units) onto the bank.
9. **Bank door lettering**: the bank sprite has tiny garbled lettering above the ATM (z-bank.png). Unreadable at
   display size; the code "$" carries the meaning. Note only; the gate's "Ticket" is the one readable painted word
   and is fine.
10. **Main Street road starts abruptly** at its left end behind the sponsor tent (scene-m0.png bottom, x about 1370
    at the 2000-wide view): a hard dark rectangle. A short fade or a curb end would finish it.
11. **Minimap silhouette barely shows** (z-mini.png): the redrawn skyline is a very low-contrast purple shape in a
    strip about 20 px tall; the yellow view box works, the skyline adds little. Raise its contrast a step.
12. **375 Trails: earlier-stop labels cut by the stage edge** (sheet-h375.png; shots/h375-lights-s4.png shows
    "ne Technician / Worker", shots/h375-kettle-s2.png shows "ancher"). They pan in with the town, so nothing is
    lost, but a half word at the edge looks broken. Hide a label whose dot is off the stage, or clamp it in.
13. **375 flat card far from its dot** on the ankle ending (shots/h375-ankle-s5.png: the Physical Therapist card is at
    the bottom, dot 5 at the top right, no visible pointer between them). Known in review-fix.md; still true.

## Frames (step 1)

- Festival at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900 (shots/fest-*.png), panned
  left to right at 1366 (shots/pan-1366-p0..p4.png), 375 host default and mid-pan (shots/h375-fest*.png). No
  placeholders, no garbled lettering beyond item 9, no text over busy art except items 4 and 12. Lantern and panel
  text unchanged and readable.
- Cards on the moved and art-heavy spots (artrow, field, weather, firstaid, ferris, police, forsale, upstairs,
  bank) at 1366 all open and sit on solid panels (shots/card-1366-*.png).
- Trails layout, measured in each frame (script in mk.py: every card, label and end line against every trail dot,
  each other and the town box): every stop of all 5 trails (27) at 1366 Motion on, 1366 Motion off and 375 (host),
  plus stop 2 and the last stop of each trail at 1920x1080, 1280x720, 760x900 and 680x425. 121 of 121 layouts have
  no card or label over a dot, no overlaps between them, and the card fully in the town. Card title size: 23 px (lg)
  at 1920, 19 px (md) at 1366, 15.5 px (sm) at 375 and the short stages, 14.5 px only on the 3 flat or xs fallbacks.
  Line text 12.5 to 18 px on solid card panels: readable at every size.
- Motion off: shots/fest-1366-calm.png reports Curio.reduce true and 0 running animations; Trails in Motion off uses
  the same md cards with no overlaps (shots/trcalm-*.png).
- Minimap: the view box tracks the pan in every panned frame; see item 11 for the silhouette.

## Art (step 2)

- 34 sprites, all present in the bundle as WebP (md5 matched per file), 0 `art:` tokens left.
- One artist feel across the set: gouache, dark outline, blue-violet shading, warm windows (sprites-dark.png,
  sprites-white.png). Scale is sensible on Main Street and in the front row; the soccer pitch and art row are the
  exceptions (items 1 and 3).
- Key check per file (strongly green or magenta pixels, and how many are semi-transparent edge pixels): real
  fringe only on the Ferris wheel (item 7) and the gate (item 6). The soccer grass, stage lights, fire truck lights and
  the land strip's green and magenta counts are painted colors, not key (checked on sprites-lime.png and in the scene).
- Grounding: everything stands on ground except the art row pieces (item 1); the fire truck is on the bank edge
  (item 8). The plane is meant to fly.

## Voice (step 3)

No line or clip changed since final.md (review-fix.md: `allLines()` equals voice/lines.json). One real held-click run
at 1366 (shots/real-trails-1366.png): Trails, Kettle corn, Next x4; welcomeTrails spoken at 1.35 s, trailEnd4 spoken
at 7.06 s after it, hint "That's the end of the trail. Pick another trail, or tap Open career...", matching the
pinned end line "took 4 clusters". Nothing overlapped.

## Full run (step 4)

Solo student: the painted town is far more inviting than before, and the Trails cards make each trail a story you
read on the map. The thing a student will poke at is the middle hill, where the art row and soccer field look
dropped in. Teacher projecting at 1920: the trail cards and end line read from the back of the room.

## Contract (step 5)

Bundle 835,040 bytes (under 2 MB), no fetch, XHR or external src/href, no em dashes. No console errors in 147 shots;
the only log is the local server's favicon 404 (host frames only).

## Sensitivity (pictures changed)

- People in the art: only the small painting on the art row easel (item 2). No other sprite shows a person, face or
  hand: vehicles are empty, the stage has instruments only, the booths and tents are empty, the petting pen has
  goats. The police place is now a police car, no figure.
- Stereotypes or anything off for a K-12 classroom: none found. No religious, political, brand or cultural symbols;
  the town hall's pediment symbol and the clinic's red crosses are generic. Painted text: "Ticket" on the gate booth
  (fine) and the garbled bank door lettering (item 9).
- Career cards: careers.json is unchanged since refine/final-sensitivity.md (its PASS covered all 93 cards, the
  gender-neutral people emoji and the object emoji). The cards checked here (shots/card-1366-*.png) still show the
  same emoji and wording. Fair across kinds of people as before.
