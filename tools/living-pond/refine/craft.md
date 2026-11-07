# Craft lens: living-pond (Curiosity No. 13), round 1

Cold Craft lens, 2026-11-06. Judged against docs/agents/CODEX-CURIOSITY.md, "Curiosities: the second shape" in
docs/VISION.md, "The look" in docs/CURIOSITIES.md, STANDARDS and BASELINE. Bundle `tools/living-pond/living-pond.html`
as built (not re-bundled). My frames and scripts: `S:/CurioClass-codex-scratch/living-pond/craft/` (run1 to run4,
shots1.json, shots2.json, throttle.py, throttle2.py, z-*.png crops). Shared audit: `S:/CurioClass-codex-scratch/living-pond/audit-r1/`.

Counts: blockers 0, should fix 7, polish 7, nit 4.

## Contract (clean)

- One file, 745,839 bytes (0.75 MB), well under the 2 MB goal. Art is two packed WebP atlases.
- No network requests: `performance.getEntriesByType('resource')` is empty after load and a run (run1/perf-default).
  No fetch, XHR or remote src in the bundle. Manual source links open only on a click (target _blank).
- Console clean in every shot of mine (the only exceptions were from my own synthetic keydown dispatched on `window`,
  which has no `matches`; real keys target an element, re-run on `document.body` was clean).
- Kit used for voice, tones, Motion and Sound (`Curio.voice`, `Curio.tone`); no kit header or kit.css frame.
- No score, goal, level, sticker, badge, finish screen or toast. Lesson-creep grep on src.html: only hits are
  "level" inside honesty prose about oxygen levels. No em dashes in src.html, notes.md, tool.draft.json, lines.json or
  the bundle. "Curio Class" is never shortened.
- Matter stays exact: 742.0 in, 1269.7 against an expected 1269.7 after 1,050 key adds and a crash (run3), 744.0 after
  ten winters with one minnow added (run1/tenyears-whole).
- Storage blocked: Save shows "This browser can't save here. The pond keeps running." and the pond keeps running
  (run1/storage-blocked). The Saved drawer states "Saved ponds stay on this device. Nothing leaves it." (rule 7).
- Art: both `art:` tokens (pond-shores-v2, pond-specimens) have prompts.json entries, `people: false`, and no people
  are drawn.
- Lines: `allLines()` returns exactly the one line in voice/lines.json, word for word.

## Findings

### Should fix

1. **Controls are browser dropdowns, not real instrument controls.** src.html:228, 230, 240-244. Speed, Lens, Feeder,
   Bottom, Decomposers, Canopy and Year are seven native `<select>` boxes; at 1366x768 the habitat row is five
   200 px wide form fields (audit size-1366x768.png, run1 frames). The look rule (CURIOSITIES.md "Real controls",
   CODEX-CURIOSITY "The look") asks for knobs, faders, toggle switches and dials that turn and click with a small sound;
   the spec itself calls Canopy and Year "dials" and Decomposers an On/Off switch. Better: a three-detent rotary switch
   for speed, lens, feeder, bottom, canopy and year (arrow keys step it and it announces its value), a lever toggle for
   decomposers, each with a soft click on Sound. Span and Spire and Pocket Universe use zero selects. family:curiosity.

2. **None of the spec's event lines exist.** src.html:622 (`L` holds only `hint`), voice/lines.json (one line). The
   spec's Voice section lists event lines ("Ice. No new air gets in until spring.", "Oxygen's low. The minnows are
   gasping at the top.", winterkill, heron or turtle left, "The snails are gone."). I ran 136 weeks with the feeder on
   Lots: the pond log recorded two freezes, a winterkill and "Heron flew off", and the voice log shows only the hint
   (run1/voice-events). The winters and the heron are the tool's drama and a student looking at the tank hears none of
   it. Add them as `V.say` events with the spec's 20 s spacing and a `valid` that the event is still true. family:curiosity.

3. **No first-run hint on screen below 900 px wide.** src.html:142 (`#hint{display:none}` under max-width 900). At
   680x425 (the site preview), 800x500, 760x900 and 375x812 the instrument never shows "Tap a creature to drop it in.";
   only the voice says it, and only after a touch (audit size-680x425.png, size-760x900.png, size-375x812; confirmed in
   CSS). The brief's one quiet first-run hint must be on the instrument at every size. A short version on the tank
   rim ("Tap a creature below") would fit. family:curiosity.

4. **The hint is spoken after the action it describes.** src.html:662-667. `afterTouch()` queues "Tap a creature to
   drop it in." on the first action of any kind and hides the on-screen hint at the same moment. If that first action
   was a tray tap, the student hears the instruction for what they just did, while the screen no longer shows it.
   Seen in the audit's held-click table (rows 6 to 13: every Add and Food tap speaks it) and in run1/voice-adds (hint
   spoken 1.4 s after the first minnow drop). Give the line a `valid` that no specimen has been dropped yet, or skip it
   when the first touch was itself a stocking tap. family:curiosity.

5. **"Whole run" vanishes when switched on.** src.html:42 and 85. `button[aria-pressed=true]` sets white text and
   `.chartbar button` then sets a transparent background, so the pressed button is white on the cream chart paper.
   Seen in run1/tenyears-whole.png (crop z-whole.png): the label is nearly invisible exactly when the chart shows the
   whole run. Give the pressed state its own dark fill or an inked underline. general.

6. **The oxygen meter has no marks at 3 and 2.** src.html:1597-1619. The dial ticks only 0, 5, 10, 15, 20; "3 gasp"
   and "2 kill" are loose captions in the meter's top-left corner that point at nothing, and at short heights (w under
   120) they are dropped entirely (680x425 frames). The spec asks for marks at 3 "fish gasp" and 2 "winterkill" on the
   needle meter. Draw two red-zone ticks or a shaded 0 to 3 band on the arc, labelled there. general.

7. **Matter lens by keyboard can only follow the muck.** src.html:1765. Enter on the tank in Matter always calls
   `follow(14)` (Muck), whatever the drop point is on; the tank's label promises "Enter ... follows a dot in Matter". A
   keyboard user cannot follow a dot from algae, a minnow or water and air, which is Things to do item 3. Follow the
   dot nearest the arrow-key crosshair, as Life does with `inspectCreature`. general.

### Polish

8. **Frame rate holds on a fast machine, thins under throttle.** Measured with rAF intervals at 1366x768 (run1, run3,
   run4, throttle.py and throttle2.py, CDP CPU throttling): Starter pond and add limits (80 algae clumps, 120 snails,
   120 minnows, 60 nymphs, 3 turtles, 2 herons, 240 specks) run a 16.7 ms median with no frame over 20 ms at 1x. At 4x
   CPU throttle (a fair modest-laptop stand-in) Matter and Energy hold 60 fps, Life at the limits drops 15 of 180 frames
   to 33 ms. At 6x every lens drops 40 to 55 percent of frames. The loop redraws the tank, chart and oxygen canvases on
   every frame (src.html:1781) though the chart and meter change once a model week; drawing those two only on
   `advance()` or a change, and skipping the tank redraw with Motion off, buys the headroom. A net swipe makes up to six
   ghost runs in one pointer move (src.html:1670-1677 into `act`): one 60 ms long task on this desktop, likely about
   200 ms on a Chromebook; compute the ghost once at the end of the swipe. Ghost runs themselves are 3 to 4 ms warm. general.

9. **Sounds are sine blips, not the spec's sounds.** src.html:653-661. Splash, net swish, flake ticks, heron plunk,
   turtle knock, ice crackle and crack are all `Curio.tone` sine beeps at different pitches. Short noise bursts
   (filtered white noise for splash, swish and crackle) would make the tank sound like water. family:curiosity.

10. **The strip chart is about 35 px tall at the 680x425 preview.** src.html:155-163. The short-screen layout gives the
    recorder 103 px and the legend bar keeps 44 px of it, so the plot has a 0 to 80 scale in about 35 px (audit
    size-680x425.png, crop z-680chart.png). At 680x425 the oxygen readout "13.4 mg/L" also sits on the dial's base
    line. Fold the legend into the plot's top margin at short heights so the trace gets the room. general.

11. **New, then Save, does not start a new pond.** src.html:1083-1084 and 955-968. The dialog asks "Save this pond
    before starting another?"; Save saves and opens the Saved ponds drawer, and the old pond keeps running, so the
    student has to press New again (run1/new-save: overlay "saves", week unchanged). Save then ask Starter or Empty,
    or label the button "Save only". general.

12. **The Habitat panel on short screens ignores Escape and outside taps.** src.html:943-946, 1725. At 680x425 the
    panel covers the whole tray and chart; Escape leaves it open (run2/habitat-680.png, `habitat-open` still true). Close
    it on Escape and on a tap outside, like the drawer. general.

13. **The "Living Pond / FIELD STATION / 13" label sits behind the right-hand cattails.** src.html:223 and 1231. At
    1366x768 and 1920x1080 the cattail sprite crosses "Pond" and "/ 13" (crop z-station.png). Move the label left of the
    reeds or draw the reeds lower. general.

14. **At 680x425 the Matter and Energy ledgers cover about 40 percent of the tank.** run2/matter-680.png. The tank is
    about 150 px tall there and the ledger box is about 90 px tall on its left third. A two-line compact ledger at short
    heights (IN POND and the trip) would leave the dots visible. general.

### Nit

15. **Run's pressed state reads backwards.** src.html:773-774. While running the button says "Ⅱ Hold" with
    `aria-pressed=true`, so a screen reader hears "Hold, pressed" for a running pond, and the Roman numeral glyph may be
    read as "two". Use a plain label ("Running, press to hold") or drop aria-pressed. general.

16. **The calendar's "Year 1" is in Georgia serif.** src.html:58. The spec's calendar readout is monospace
    (`YEAR 3 · WEEK 22 · SUMMER`), like every other readout. family:curiosity.

17. **Replay leaves the speed on Fast.** src.html:984. After a replay ends the chart speed stays at 8 weeks a second.

18. **The tank's focus ring is clipped.** src.html:43 and 50. The canvas outline sits outside the canvas and `.tank`
    clips it; the only focus sign is the small yellow crosshair. A ring drawn inside the canvas edge when focused would
    be clearer. Focus rings elsewhere are visible (crops z-focus-tray.png, z-focus-footer.png, z-focus-power.png).

## Access (checked)

- Every control is a real button, select or input with a 44 px target; tray buttons announce kind, count and the
  drawing multiplier ("Add Snail. 68 present. One drawing = 2."); net mode relabels them ("Net one ..."), and
  Decomposers explains it cannot be netted.
- Keys: Space, period, < >, 1 to 7, N, L, W, M and Escape all work; arrows move the drop point on the tank; Enter
  inspects in Life (see 7 for Matter). The drawer is modal, traps Tab, returns focus on close.
- Motion off (calm frame, run1/motion-off): swimming, arrivals and flight stop, counts still update.
- Colour is never the only signal on the chart: each line has its own dash and an end letter (A, S, M, N).

## Standard voice check

Held clicks (0.12 s), Sound on, Motion on; logs from `__tool.vlog`.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| "Tap a creature to drop it in." | how (first-run hint) | once, only while it still fits | once per load in 5 Add taps (run1/voice-adds), but stale after a tray tap (finding 4) |
| Read (calendar, oxygen, temperature, counts, latest log) | read | every press, Sound off too | 3 of 3, including one with Sound off; cut the hint as it should (run1/voice-read) |
| Ice, oxygen low, winterkill, heron left, turtle left, snails gone | event | each event, at most once in 20 s | 0 of 5 events over 136 weeks (finding 2) |
| First tap on Sound | none | nothing | nothing (audit row 2) |

Repeats, order and Read: clean. No line named a hidden control. Stale lines: only the hint after a stocking tap.

## Short-test notes for the merge (Craft view only)

The real thing is the interface: the tank, chart and meter are drawn from the live model, painted art only places it.
What holds it back from the look of Beat Lab or Elements Inspector is finding 1: the lower third of the screen is a
row of web form dropdowns.

## Audit pilot

- **Leads confirmed:** "hint out of view" at 680x425, 800x500, 760x900 and 375x812 (finding 3, CSS display:none);
  the held-click table's "spoken" column showing the hint after every Add and Food tap (finding 4).
- **Leads wrong (noise):** every `#pond` overlap row at every size and state (the tank is a full-screen stage with its
  calendar, power panel, transport and ledgers on top by design); "hint out of view" at 1000 px and up in the states
  (the hint hides after the first action by design); "text under 10 px" on the TIME and LENS labels at 375 (font-size 0
  hides the words on purpose, the selects carry aria-labels); "keep region" for #ledger (the ledger sits on the canvas)
  and for #run, #speed, #tray in manual and saved (a modal drawer); the tray cut short at 375 (the spec asks for a
  scrolling row); "welcome not heard" after a first tap on the tank, Run, Step and the tray (the hint is the welcome
  and it was spoken, as the same rows show).
- **What it missed:** the invisible pressed "Whole run" (5), the missing oxygen marks (6), the missing event lines (2),
  dropdowns in place of real controls (1), Matter keyboard following only muck (7), New then Save (11), Habitat
  ignoring Escape (12), the station label behind the cattails (13), the tiny chart at 680x425 (10), and frame times
  under throttle (8).
