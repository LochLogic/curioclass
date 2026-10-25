FIX (5 should fix, 9 nits, no blockers)

# Verify: imaginary-island (2026-10-25)

Checked cold against spec.md, POLISH.md, VERIFY.md and BATCH-G11.md. Draft bundle (`CURIO_DRAFT=1`, 487 KB with the 12 recorded clips). Frames and console/network logs came from my own headless Chrome driver over CDP (scripts/shoot.py does not report console errors). Narrow and embedded sizes were checked in an iframe host page served on 127.0.0.1. Everything is in my scratchpad.

## What passed

- **Math, recomputed in Python (cmath), not taken from the tool.** 3 + 2i times i, four times: Fox Den, Salt Flats, Waterfall, back to Orchard, all at 3.6056. 4 + i the same way: Hermit Hut, Shipwreck, Tide Pools, all at 4.1231. The heading of 3 + 2i is 33.69 degrees. w = 1 - i turns by -45 degrees and stretches by 1.4142. All 12 clues end where the spec says: i Bell Tower, -1 Old Pier, -2 + 3i Fox Den, -3 - 2i Salt Flats, 1 - 4i Tide Pools, 4 + i Cave, 2i Twin Rocks, -4 Sea Arch, 5 - 3i Black Sand Beach, -3 + 2i Hidden Cove, 13 Far Buoy, -1 + 4i Hermit Hut. The tool's `clueEnd` and walked results match. Springs presets: discriminants 16, 0, -4, -16, -4, -16. Roots ±2, 1 twice, ±i, ±2i, 1 ± i and -3 ± 2i (Hidden Cove and Salt Flats). With b = 0 and c from -4 to 13: real ±2, meeting at 0 when c = 0, then ±0.71i up to ±3.61i. Repeated squaring from 3 + 3i gives 18i, then -324, then 104976 (refused, as it should be).
- **Coastline (the tool tuned the constants, which the spec allows):** Sea Arch is 0.13 from the shore and Black Sand Beach 0.05. Every other landmark is at least 0.51 inland (the nearest is Orchard at 0.51), and Far Buoy is 6.4 out at sea. All within the spec.
- **Done when 1 to 7 hold.** Dragging the lantern to 3 + 2i gives "You are at the Orchard". Four presses of × i return exactly to [3, 2], with each worked line showing the i² step and the dial lighting 1, 2, 3, 4, and six presses show "i⁶ = i² = −1". The × w worked line matches the spec exactly, including "Turned by −45° and stretched by 1.41". With Motion off (`curio-motion=calm`), all seven operations jump and leave dashed trails (frame 10-calm-trails). Square it at 0 gives the harbor note. Squaring from 3 + 3i zooms to 25, then 50 and pins "z = −324, off the chart" to the edge, then refuses with "Too far out to chart" (frames 07-square-0..3). Every clue reports its result, "Landed it." at 0.2, and the tally counts each clue once even when walked again. Springs behave as written in frames 20 to 26.
- **Worked lines:** checked against the spec's examples for × i, × (−1), × (−i), Reflect, Square it, + w and × w, plus extra cases (negative factors in parentheses, (2i)² = 4i² = −4, (−3)² = 9, w = 0 gives "w is 0, so the product is 0."). Number display: "2i", "3", "−i", "3 − 2i", -0 shown as 0. The quadratic formula line for b = −2, c = 2 matches the spec.
- **Contract:** one file, no network requests (the only URLs are the SVG namespace), no console errors or exceptions in any run. Kit used for fit, say, yes, Motion, Sound and Read. Buttons are 44 px tall at every width I tried (375, 768, 800, 1024, 1280, 1400). The lantern, w and guess pin are 44x44 hit areas. Focus rings show on map markers, landmarks and buttons (frames 30 to 32). Color is never the only signal: the marker shapes differ (lantern, diamond, X, drop), every marker has a text label, layer buttons show a check mark, and trail segments are labeled.
- **Contrast (WCAG):** brand teal on the section background 7.99, brand-ink on brand 8.33. Lantern, w, pin and spring label text on the halo color range from 8.7 to 13.4, and tick text is 11.1.
- **Lines:** all 12 are word for word the same in spec.md, voice/lines.json, `L` and `allLines()`. The bundled clip map has exactly these 12 keys. Bank, voice and style follow the batch rules. Nothing played before the first input. Lines are cut on mode change.
- **Art:** one optional prompt, `people: false`, no people asked for. In the draft build the tool draws the island fully in code, and the stand-in is not drawn (it only uses a webp).
- **Words:** no em dashes in any tool file. "Curio Class" is never shortened to "Curio" on screen. In Clue Trail, nothing gives away the end before Walk it or Show the arithmetic.

## Findings

1. **Clue Trail: the parked lantern still drags the Explore traveler** (src.html:898-899, 733-734). How seen: I dragged from the lantern at 1 in Clue Trail. `state.ex.z` became [−2, −2], an Explore undo step was pushed and the "roads" line was queued, while the Clue lantern stayed put. Clicking on the lantern also drops no guess pin, because pointerdown is stopped there. This matters for clue 12, whose answer is its own start. Only Enter or dragging the pin over gets a guess there. Should fix: ignore pointer input on the traveler outside Explore.
2. **Clue Trail stays zoomed out after a far clue** (src.html:947-953; `travel` zooms at 850). How seen: frames 13-clue-arith and 56. After walking clue 11 (ends at 13), the view stays at -15 to 15 for every later clue. At that zoom landmark names are hidden (k < 40), so "Start at the Cave" points at an unlabeled dot. Should fix: `setClue` should return the view to Fit.
3. **Spring labels cover landmark labels** (src.html:1063-1068). How seen: frame 20-springs-default, where the r1 = 2 drop and box sit on "Lighthouse" ("Ligh...se") and "r2 = −2" touches "Sea Arch". Frame 21-preset_6_13 also shows it: "r2 = −3 − 2i, the Salt Flats" covers the "Salt Flats" label, and the r1 box runs into Twin Rocks. Spring labels are not in the label collision boxes. Should fix.
4. **"Harbor" label reads as Fern Well's** (src.html:532, `harbor: [-10, 38, 'end']`). How seen: frames 01-default and z01. The label sits 38 px below the origin, directly above "Fern Well" and closer to the Fern Well icon at -i than to the anchor. Should fix: move it up-left of the origin, or beside the anchor.
5. **16:10 embed: operations are off screen** (src.html:23-24). How seen: iframe host at 680x425 (the tool page stage width) and 800x500 (frames 47 and 42). Under 900 px the panel stacks below the map, and the header wraps to two rows. The first screen is the header and part of the map. Every operation, readout and slider needs scrolling inside the iframe, so the map and its buttons are never seen together. Done when 9 asks for "usable in a 16:10 iframe". It works at 1024x640 and in full screen. Should fix, for example two columns down to about 640 px wide with a compact panel, or a single-row header.
6. **Mode switch mid-walk parks the Clue lantern mid-arc** (src.html:1156, 971). How seen: I walked clue 3, switched to Explore partway, then came back (frame 33). `cl.z` stayed at 0.79 + 3.52i with a half-drawn trail, and the clue was not reset. Nit.
7. **Half-cent rounding is lopsided in worked lines** (src.html:310, `Math.round`). How seen: with z = 0.5 − 1.25i and w = 2.5 + 0.5i (Snap off), the line reads "... − 0.62i² = 1.25 − 2.87i + 0.63". The same 0.625 shows as 0.62 and then 0.63. Very small values also lose their middle steps: "(0.09 + 0.02i)² = 0.01" sits next to "You are at the Harbor". Nit.
8. **Tab order runs through all 19 landmark notes** before the layer buttons and operations (src.html:555, gLandFocus). How seen: a Tab walk goes header, map, lantern, w, then 19 landmarks, then Grid. Keyboard users need 21 Tabs to reach × i. The letter keys help, but only once the map has focus. Nit.
9. **Spoke and ring labels collide with tick labels** (src.html:515-516, 522-523). How seen: in frame 51, "180°" sits on the "−6" tick, "90°" by "6i" and the road name, and "270°" on "−6i". In frame 03 ring label 4 hides under "Waterfall". In frames 07-square-0/1 the ring labels 4 to 10 pile up at wide zooms. Nit.
10. **Worked lines wrap inside a number** (src.html:61, `word-break: break-word`). How seen: frames 02, 06 and 55 show "= −3 / − 2i" and "= −4 − / i" split across lines. A non-breaking space inside each complex number would keep them together. Nit.
11. **Map labels touch icons:** "−4i" touches the Tide Pools icon, "−4" sits under the Sea Arch icon, and the "i" and "−i" ticks hug Bell Tower and Fern Well. In frame 50 the Fox Den label is clipped at the left edge at zoom 3. At 375 px wide the map text is about 9 to 10 px on screen (frame z40). Nit.
12. **Voice order on a quick first move** (src.html:289-292, 899). How seen: the clips played as "East and west..." and then "Welcome...", because the drag ended inside the 250 ms delay. A first arrow-key move always does this. `setClue` also calls `stopVoice` (948), so pressing Next clue right away cuts the Clue Trail intro, and it never replays. Nit.
13. **Explore hint is below the fold at 1400x900** (frame 01): the panel scrolls, so the one instruction line is cut off on a common laptop window. Nit.
14. **w starts on the Summit and hides its icon** (frame 01). This is per the spec (w = 1 + i), and the label still shows. Nit, only noting it.

## What I could not check

- I did not listen to the audio. I only confirmed which clip played, and in what order.
- Real pinch zoom and real mouse hover. I used synthetic CDP pointer and wheel events. A hover tooltip stayed up after re-renders in my runs, which may be an artifact of synthetic events.
- Screen reader output.
- The island-terrain art is not painted yet (draft), so the clipped texture over the island is untested. tool.draft.json correctly keeps the tool on the bench.

## Re-verify

FIX (2 should fix, 4 nits; 11 of the 14 earlier findings fixed, 2 partly, 1 unchanged per spec)

Checked cold on 2026-10-25 against a fresh `CURIO_DRAFT=1` bundle (539 KB). Frames, console, network and voice order came from my own headless Chrome driver over CDP. Every size except 1400x900 ran in an iframe host page served on 127.0.0.1: 680x425, 800x500, 760x475, 760x1000, 1000x625 (also direct), 375x812 and 375x667. No console errors or exceptions in any run. No network requests except the page itself.

### Earlier findings

1. **Lantern drags Explore in Clue Trail: fixed.** Dragging from the parked lantern now pans the map. `ex.z` stays [1, 0] and no undo step is pushed. A click on the lantern in clue 12 drops the guess pin at −1 + 4i.
2. **Clue Trail stays zoomed out: fixed.** After walking clue 11 the view is ±15. Next clue, Previous clue and `setClue` all return it to ±7 with names showing.
3. **Spring labels cover landmark labels: fixed at 1400x900.** Labels find a clear spot, and a landmark name under a spring is dimmed. See new finding A for the inset at smaller sizes.
4. **"Harbor" reads as Fern Well's: fixed.** The label now sits up and left of the anchor, clear of Fern Well.
5. **16:10 embed hides the operations: fixed.** At 680x425, 760x475 and 800x500 the map and panel sit side by side under a one-row header. The traveler readout and all seven operations are visible next to the map. The worked line starts at the bottom edge and needs a panel scroll (nit C).
6. **Mode switch mid-walk: fixed.** Leaving partway through clue 3 and coming back puts the lantern back at 3 + 2i with no trail and no result. The guess is kept and Walk it is enabled.
7. **Rounding in worked lines: partly fixed (nit).** Halves now round the same way every time: "− 0.63i² = 1.25 − 2.88i + 0.63 = 1.88 − 2.88i". Very small values still lose their middle steps: "(0.09 + 0.02i)² = 0.01", next to "You are at the Harbor". With Snap off, a step can still look wrong: "(0.25 + 0.13i)² = ... = 0.06 + 0.06i − 0.02 = 0.05 + 0.06i".
8. **Tab order: fixed.** After the header, Tab goes to the 7 operations, then the map, the lantern, w, a single landmark stop (arrow keys step Harbor, Lighthouse, Bell Tower...), the layer buttons and zoom. The I/R/S/A/M/U keys, arrow and Shift-arrow, and Enter in Clue Trail all work.
9. **Spoke and ring labels on ticks: fixed.** Frames at ±7, ±25 and ±50 show no degree label on a tick, and ring labels are left out where they would crowd.
10. **Worked lines wrap inside a number: fixed, with a regression (new finding B).**
11. **Labels touching icons: partly fixed (nit).** At 1400x900 the "−4i" tick moved left, clear of Tide Pools. At 1000x625 and smaller, where map text is scaled up, ticks still collide: "−2 −1" run into "Fern Well", and "Shipwreck" sits on "−5" and "−4". At every size "−4" touches the bottom of the Sea Arch icon. At 375 px wide the map text is still about 9 px.
12. **Voice order: fixed.** A quick first drag and a first arrow-key move both play Welcome first, then the roads line. Clue Trail, then Next clue right away, no longer cuts the Clue Trail intro. Pressing × i twice plays Welcome, the × i line, then the i² line.
13. **Explore hint below the fold at 1400x900: fixed.** The hint is fully visible (y 770 to 816).
14. **w starts on the Summit: unchanged, per spec.**

### New findings

A. **The Springs inset covers the r1 label and Fox Den** (src.html:1109-1112, 1133-1142; the inset is not in the label collision boxes and draws above the springs). How seen: frames sp-1000-0, sp-680-0 and sp-375-0, preset x² + 6x + 13. At 1000x625 (the tool page size) and smaller, r1 reads "1 = −3 + 2i, the Hidden Cove" because the "r" is under the inset. "Fox Den" shows as "ox Den" in every Springs frame at 1000 px wide and below. At 680x425 the r2 box also covers part of "Real Road (real part)". At 1400x900 the label is placed below the spring and is fine. Should fix.

B. **"Turned by ... and stretched by ..." is clipped in the compact embed** (src.html:965, workedHTML; a line with no " = " becomes one nowrap span). How seen: frames z-f680-mul-turned and z-f680-clue11-arith. At 680x425 it reads "Turned by 149° and stretched by 2." for 2.92. In Clue 11, Show the arithmetic loses the 3.61 completely. The line runs 18 to 44 px past the panel at 680x425, 760x475 and 800x500. The "(walk 2.5 west, 1.5 north)" tail of + w also touches the edge. Wider layouts wrap fine. Should fix.

C. **Compact embed: the worked line is below the fold** (frame f680-after-xi). At 680x425 the worked line's top is at y 410 of 425. After pressing an operation, the arithmetic needs a panel scroll. Nit.

D. **Landmark hover tip goes stale** (src.html:604, 621-631). How seen: frame tip-stale. I hovered over Cave and then zoomed out. The tip "Cave: 4 + i" stays where Cave used to be, and stays after the mouse moves away. The landmark is redrawn under the pointer, so pointerleave never fires. This used real CDP mouse input. Only hovering and leaving another landmark, a layer toggle or a mode change clears it. Nit.

E. **Small text mismatches about the art** (art/prompts.json, tool.draft.json). The local_note says the texture is drawn at "70 percent opacity", but the code uses 0.62. The draft's sources line still says "Island ... drawn in code" now that a painted texture is inlined. The prompt's review is still "pending". Nit.

### Regressions checked (all pass)

- **Explore:** Orchard at 3.61 and 33.7°. Four × i presses visit Fox Den, Salt Flats, Waterfall and Orchard, with the dial lighting 1 to 4. The sixth press gives "i⁶ = i² = −1". × (−1), × (−i), Reflect, + w, × w and Square it give the right values and worked lines. "Turned by 45° and stretched by 1.41" appears. Squaring from 3 + 3i gives 18i at ±25, then −324 pinned to the edge at ±50, then "Too far out to chart". Square at 0 gives the harbor note. With Motion off, all 7 operations leave dashed trails.
- **Clue Trail:** all 12 clues end at the spec's landmarks, from Bell Tower to Hermit Hut. Each shows "Landed it.", the after-lines appear on clues 11 and 12, and the tally reads "Landed 12 of 12 tried".
- **Springs:** the presets give discriminants 16, 0, −4, −16, −4, −16, and roots ±2, 1 twice, ±i, ±2i, 1 ± i and −3 ± 2i (Hidden Cove and Salt Flats). With b = 0 and c from −4 to 13: ±2, ±1, 0 twice, ±0.71i, ±2i and ±3.61i. The formula lines are right.
- **Sizes:** every button is at least 44 px tall at every size, and no size scrolls sideways.
- **Art:** art/island-terrain.webp (1024x1024) is inlined as a data:image/webp. It is clipped inside the coast as a soft green texture with no seams, and the labels stay readable over it.
- **Voice:** the 12 recorded clips are inlined, and their keys match lines.json, `L` and `allLines()` word for word. All 12 decode in Chrome, at 6.5 to 11.4 s, which fits their length. I did not listen to them.
