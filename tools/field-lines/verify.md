FIX

Verify of field-lines, 2026-10-25. Bundled with CURIO_DRAFT=1 (944 KB, 30 local voice clips). Headless Chrome 156 with --mute-audio over CDP, held clicks (press, 120 ms, release) for voice. Physics checked in Python from the CODATA and NASA constants. No console errors or exceptions in any frame. No network requests (the only URLs in the bundle are the SVG namespace). No em dashes in src, notes, lines or bundle. Contrast: every accent passes AA on the panel, section and board colors (lowest is the red #FF6E61 at 5.98:1 on the section background).

## What passed

- Physics, Twin boards: board fields match Python for every preset (Opposite pair probe gravity 0.457, electric 0.366; Big and small 0.622 on both; Row of three 0.379 and 0.065). Single, probe at 2 then Double: 0.75 to 0.19 on both boards, "(× 0.25)", distance "(× 2)". Halve gives "(× 4.00)". Like pair at (6, 6) reads 0.00 on both, and Release leaves the probe still with the cancel hint (Done when 4 and 5).
- Physics, Real pairs: every force and ratio matches Python at x1, x2, x1/2, x8 and x1/8 for all five pairs. Hydrogen 3.63 × 10⁻⁴⁷ N and 8.24 × 10⁻⁸ N, ratio 2.27 × 10³⁹; protons 1.87 × 10⁻³⁴ N, 231 N, 1.24 × 10³⁶; balls 6.67 × 10⁻¹¹ N, 8.99 × 10⁻³ N, 1.35 × 10⁸; apple 9.82 N; Earth and Moon 1.98 × 10²⁰ N. Doubling quarters both forces and the ratio line never changes. Apple Halve is disabled at the surface with the right note (Done when 8 and 9).
- Spread: lines per tile 36, 16, 9, 5.76, 4, 2.94, 2.25, 1.78, 1.44 match the spec; r = 3 shows 9 tiles, "Lines per tile: 4", "1/9", point on the solid curve (Done when 7). Formula card constants correct.
- Field lines: 36 gravity and 24 electric lines in Opposite pair (6 per size unit, the 12 minus-to-plus lines dropped). The flat-screen note "Line spacing on a flat screen is a sketch..." is present under the View toggles whenever Field lines is on.
- Drawing stays smooth while dragging: with 6 objects of size 5 (272 lines), a real CDP drag ran at a steady 16.7 ms per frame (median and p95), tracing both boards took 7 to 10 ms (worst 14.5 ms, objects spread to the corners). With Field lines, Arrow grid and Strength shading all on, about 20 ms per frame. Slower school laptops may drop to 30 to 45 fps; I could not test one.
- Done when 1, 2, 3, 10: load shows two amber "m 3" discs with all lines in and a "+3"/"−3" dipole; dragging the probe on the electric board moved the gravity twin and updated the readout 20 times in 20 moves; Flip sign left the gravity trace identical and the gravity board pixels unchanged (0 differing pixels after the pulse); keyboard alone selects (Tab), moves (arrows, Shift 1 unit), resizes (+, -), flips (S), removes (Delete), Escape deselects; Motion off draws Release paths at once.
- Lines: all 30 spoken lines (12 narration, 18 hints) are in voice/lines.json, allLines() and local.json word for word.
- Voice basics: first tap queues one welcome per mode (plus tb-howto after tb-welcome), first tap on a mode button gives only that mode's welcome, Read cuts a welcome and speaks the hint, a line triggered during Read waits for Read to end, Sound off stops speech and Read still speaks.
- Sizes: no horizontal overflow at 680x425, 800x500, 1000x625, 760, 1280x720, 1366x768 or 375 in an http iframe host. All targets 44 px or more. Twin boards stack at 375 with gravity on top.

## Findings

1. Release in Opposite pair (Done when 6 and the symmetry line). Twin boards, Release probe. The tool is honest but not clear for students. The readout says "Gravity: still moving after 8 seconds. Electric: still moving after 8 seconds." (correct: Python agrees the gravity probe swings straight through the midpoint between y 8.5 and 3.5, and the electric probe swings around the minus without landing). But the gravity trail is one vertical stroke drawn over itself with an open ring in the middle, so with Motion off, or after the run, nothing shows it went back and forth, and the hint says "Gravity only ever pulls it in", which reads as if it should have landed. The only explanation is in notes.md, which students never see. Suggest a specific hint (and a line) when the gravity end is "time" on a symmetry line, for example "On the center line the two pulls balance sideways, so the probe falls through the middle and swings back and forth. Nudge it sideways and try again." Seen in frames 05, 06, 07 and phys.py. Should fix.

2. notes.md "Release in Opposite pair": "Nudge the probe sideways with an arrow key first and the gravity trail lands on a disc." One arrow press (0.25 units) and two presses (0.5) still do not land within 8 s; it takes 0.75 units (three presses) or Shift+arrow (1 unit). Checked in Python with the tool's integrator (Verlet, dt 0.002). Should fix (say Shift+arrow).

3. Voice: an interrupted Read blocks narration for up to 12 s. src.html narrate() awaits readP, and readP is a race of say() and wait(2500 + 80 per character). When Read is cut off (a mode switch calls hush(), which pauses the clip), the paused clip never fires ended, so readP only resolves at the timeout. Held clicks: welcome, Read at 1.2 s, Spread at 2.4 s: the Spread welcome started at 9.2 s, 6.8 s of silence after entering the mode (test 58). In a longer click-around the Real pairs welcome started 10 s late (test 57). hush() should also reset readP. Should fix.

4. Voice: stale pair line. Entering Real pairs queues rp-welcome and then rp-hydrogen. Picking Earth and Moon 1 s later does not drop it: "In a hydrogen atom, the electric pull is..." played at 6.6 s while Earth and Moon was on screen, then the Earth and Moon line at 14.7 s (test 59). Drop a queued pair line when the pair changes. Should fix.

5. Voice: state lines play late. Welcome, then Like pair at 1 s and Row of three at 2 s: tb-zero ("Here the pulls cancel, and the field is zero.") played at 19.8 s, long after the probe left the zero point (test 53). Consider dropping tb-zero if the probe no longer reads zero when it comes up. Nit.

6. Voice: if the first tap is Read (or Sound), the Twin boards welcome and how-to never play this session (test 55: said list empty after Read and a preset). Probably intended for Sound; for Read the welcome could queue after Read ends. Nit.

7. 16:10 preview, Twin boards (compact layout). At 680x425 and 800x500 all six Presets are below the panel fold. After selecting an object (any click on a disc selects it) and pressing Release, the Release readout plus the selection row push View and the Double, Halve, Release and Clear buttons below the fold too at 680x425 (frame 45). 1000x625 fits. Should fix (for example keep the selection row compact, or show the release result in the scene).

8. 16:10 preview, Spread at 680x425 (frame 80): the plot is wider than its area (pw is forced to at least 120 px), so the "6" tick is cut at the panel edge; "25 tiles at r = 5" overlaps the ruler's "distance r" label; "this tile: 1 line" sits against the formula card; the point label "r = 5: 1.44" has the curve running through it. At 800x500 the "r = 1: 36" label collides with the "solid: 36 / r²" legend (frame 40-800-sp). Should fix (small).

9. Spread at 375 in the iframe host: the rotated y-axis label "lines per tile" is clipped at the left edge (left -7 px, frame 42-375-sp). Nit.

10. Spread tile count versus average: at r = 2.5, 3.5, 4, 4.5 and 5 the highlighted tile shows 4, 4, 1, 1 and 1 lines while the panel says 5.76, 2.94, 2.25, 1.78, 1.44 "on average". At r = 4 four of the lines sit exactly on the tile's edges (offset 1.0) and are not counted. Honest with "on average", but a student comparing the two numbers may be confused. Nit.

11. Twin boards, Clear all then Release (frame 72): hint "The probe sits still: the pulls cancel here." and readout "stayed still, the pulls cancel" when there are no objects at all. Should say the boards are empty. Nit.

12. Real pairs, two protons: the start distance 1.0 × 10⁻¹⁵ m is less than one proton diameter (charge radius about 0.84 × 10⁻¹⁵ m), and Halve goes down to 1.25 × 10⁻¹⁶ m, where two point charges are not a meaningful model. The values follow the spec and are computed correctly; consider limiting Halve for this pair as the apple pair is limited, or a one-line note. Nit (spec level).

13. Number format: Two protons at 8 times the distance shows "3.6 N"; 3 significant figures would be "3.60 N" (sci() strips the trailing zero via toPrecision then unary plus). Nit.

14. Probe value labels overlap lines or discs in places: gravity "0.46" crossed by the center field line at 1000x625 and 1280x800; electric "1.84" partly under a +5 disc with six large objects (frame 24). Readable but untidy. Nit.

15. Voice count: 30 recorded lines, above the batch's "about 5 to 25"; 18 of them are hints for Read. Nit, flag only.

## Unsure

- Performance on a real low-end school laptop: headless on this PC has headroom (7 to 10 ms trace per frame), but with all three views on a 3x slower CPU it would run near 15 to 20 fps while dragging.
- Whether losing the welcome after a first Read tap (finding 6) is the intended rule for this batch.

## Re-verify

FIX

Re-verify of field-lines, 2026-10-25, cold. Bundled with CURIO_DRAFT=1 (988 KB, 31 local voice clips, all 31 lines.json lines present as clip keys, in src and in allLines()). Headless Chrome with --mute-audio over CDP, http-served (127.0.0.1), held clicks (press, 120 ms, release) for voice, clip playback logged by patching HTMLMediaElement.play. No console errors or exceptions. No em dashes in src, notes, lines or bundle.

Spot checks that still pass: Single, probe at 2: 0.75 on both boards; Double: 0.19 "(× 0.25)", distance "(× 2)"; Halve back: 0.75 "(× 4.00)", "(× 0.5)". Hydrogen 3.63 × 10⁻⁴⁷ N, 8.24 × 10⁻⁸ N, ratio 2.27 × 10³⁹; Earth and Moon 1.98 × 10²⁰ N (Python agrees). Spread at r = 3: "Area: 9 tiles", "Lines per tile: 4", "Strength: 1/9 of distance 1". Drag with six size 5 objects (real CDP drag, 60 moves): 16.7 ms per frame median, p95 and max, trace 6.9 ms, at 1280x720 and 680x425. No horizontal overflow at 680x425, 800x500, 1000x625, 1280x720, or in the iframe host at 760 and 375 (all three modes); no visible target under 44 px.

Per finding:

1. Swing (should fix): FIXED. Opposite pair, Release: hint is the new swing line, readout "Gravity: turned back 1 time, still moving after 8 seconds." The gravity trail now shows the return pass offset to the side with a dot at the turnaround and the open ring at the end, readable with Motion off (frame swing-calm-1280) and after a Motion on run. Read speaks the swing clip (recorded and inlined). Nudged 1 unit, the hint goes back to the release line and both trails land.
2. Notes nudge (should fix): FIXED. notes.md now says at least 0.75 units / Shift+arrow; the tool's own F.release agrees: 0.25 and 0.5 sideways still "time", 0.75 lands at 2.99 s, 1.0 at 2.70 s.
3. Interrupted Read blocks narration (should fix): FIXED. hush() resets readP. Welcome, Read at 1.2 s, Spread at 2.4 s: sp-welcome started at 2.54 s. Real pairs, Read at 1.2 s, Twin boards at 2.4 s: tb-welcome at 2.54 s. First tap Read, Spread at 1.0 s: sp-welcome at 1.13 s.
4. Stale pair line (should fix): FIXED. Real pairs, Earth and Moon at 1.0 s: rp-welcome, then rp-earthmoon at 6.7 s; rp-hydrogen never played.
5. Late tb-zero (nit): FIXED. Welcome, Like pair at 1 s, Row of three at 2 s: tb-zero dropped, tb-negative played after tb-howto.
6. Read as first tap loses the welcome (nit): FIXED. Read spoke the hint, then tb-welcome started 160 ms after it ended, then tb-howto. Sound as first tap still gives no welcome (intended).
7. 16:10 Twin boards fold (should fix): FIXED for its main point. Presets are a select in the top row and the Double, Halve, Release, Clear row sits above the readout, so at 680x425 and 800x500 the presets and all four probe buttons stay in view with an object selected after a Release (frame tb-680-selrel). Left over, nit: at 680x425 with a selection the release readout (bottom 492 > 425) and the View row drop below the fold, and at 800x500 the View row does; the trail and the hint still tell the result.
8. Spread at 680x425 and 800x500 (should fix): FIXED. "6" tick visible, "25 tiles at r = 5" clear of the ruler, "this tile" clear of the formula card, point label off the curve, "r = 1: 36" clear of the legend (frames sp-680-r5-one, sp-800-r1). Left over, nit: the ruler's "0" and "1" numerals touch the "distance r from the source" caption by 2 to 6 px at 680, 760 and 375.
9. Spread y label at 375 (nit): FIXED. The label is now horizontal above the axis, nothing clipped.
10. Tile count versus average (nit): not changed, acceptable with "on average".
11. Clear all then Release (nit): FIXED. "No objects on the board, so there is no field to follow." and the empty hint.
12. Protons below a proton size (nit, spec level): not changed.
13. "3.6 N" (nit): FIXED in code (sci() now returns toPrecision(3) without the unary plus).
14. Probe labels over lines (nit): not re-checked in detail; the "0.46" label still sits next to the center field line at 1280x720.
15. Voice count (nit): now 31 lines; flag only.

New:

16. Wide layout (1280x720, 1366x768, 1280x800), Twin boards. The compact fix does not apply to the wide panel. With the default screen the Presets row already ends below the fold (bottom 759 to 868 px against 720 to 800). After selecting an object and pressing Release, the release readout and the selection row push Double, Halve, Release and Clear below the fold at 1280x720 and 1366x768 (bottom 785 px; frame w1366x768-sel), so pressing Release again needs a panel scroll. 1366x768 is a common school laptop size. 1920x1080 fits. Should fix (for example the same probe-buttons-first order and preset select in wide when the height is under about 900).
