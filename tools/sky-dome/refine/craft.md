# Craft lens: sky-dome (Curiosity No. 05), round 1

Cold lens, judged against CODEX-CURIOSITY.md, VISION "Curiosities", STANDARDS and BASELINE. Bundle as built
(532 KB), headless Chrome on port 9761, with the GPU on for frame timing. Scratch and frames:
`S:/CurioClass-codex-scratch/sky-dome/craft/` (scripts cc.py, perf.py, prof.py, kb.py, voice.py, read.py, motion.py).

## Findings

### 1. The dome squashes the sky: star patterns are drawn 2.7 times wider than tall (blocker, family:curiosity)
- Where: `src.html:819-827` `projectVector` (and `fromScreen`, `resize` 1180-1181). The normalized radius goes to
  `r*rx` horizontally and `r*ry` vertically. At 1366x768 rx = 621 and ry = 233, so this happens at **every** zoom, not
  only the whole-dome fisheye.
- What: at FOV 50 on Orion (2026-01-15 04:00 UTC, Denver), 1 degree is 24.8 px across and 9.3 px down. Orion is
  flattened into a wide smear you can't recognise (Betelgeuse to Rigel: 393 px across, 92 px down). At 680x425 (the
  site preview) the dome is about 4.6:1. Shapes also change as they turn, so "the Big Dipper on a spring evening and an
  autumn evening: the same stars, turned" (spec Things to do 13) shows a different shape, not a turned one. A
  planetarium whose star patterns are wrong breaks the "readout that lies" rule, even with the Manual's honesty
  note (`src.html:356`). The real instrument is round.
- How seen: `craft/orion-1366-fov50.png` (with object pixel coordinates from perf.py), `audit-r1/size-1366x768.png`,
  `size-1920x1080.png`, `size-680x425.png`.
- Better: use one scale (min(rx, ry)) for both axes. Fill the width with a round dome, or let a zoomed view fill the
  stage at a true aspect, the way planetarium software does. Keep the brass horizon ring round at whole-dome view.

### 2. 60 fps fails on a Chromebook-class CPU (should fix, general; Done when 7 fails as measured)
- Where: `draw()` `src.html:926-951`. Each of about 4,600 visible stars gets its own `globalAlpha`, `fillStyle`,
  `beginPath/arc/fill`. Every frame also runs `querySelectorAll` and `getComputedStyle` for label boxes (983-986).
- Measured (1366x768, Play at 1 h/s, all stars, lines and trails on, GPU Chrome):

  | CPU throttle | rAF frame median | p95 | draw() median |
  |---|---|---|---|
  | 1x (this desktop) | 7.0 ms | 13.9 ms | 7.7 ms |
  | 2x | 20.8 ms (48 fps) | 20.9 ms | 16.8 ms |
  | 4x (common Chromebook proxy) | 34.7 ms (29 fps) | 48.6 ms | 30.1 ms |

  With lines and trails off, 4x still gives 41.7 ms. Stars alone (everything else off) cost 23.8 ms per draw at 4x
  (prof.py). The star loop is the cost, not the lines.
- Better: batch the stars by colour and alpha bucket into a few paths, or draw them once to an offscreen canvas per
  sidereal step and blit it. Read the overlay rects once on resize, not every frame.

### 3. The west compass letter is hidden under the zoom buttons (should fix, general)
- Where: `.view-tools` `src.html:52` sits over the ring's W marker at the whole-dome default.
- How seen: `craft/w-marker-crop.png` (from audit `size-1366x768.png`); the same at 1920x1080 and 1280x720. W shows
  at 800x500. West is where every star the student watches goes to set.
- Better: move the view tools clear of the ring (into the deck or below the ring), or inset rx past them.

### 4. Date and time wheel engravings can't be read (should fix, general)
- Where: `wheelControl` `src.html:1257-1258`. The text is `font-size="5"` in a 100-unit viewBox, so about 5 px:
  `#e1c68d` on a gold band (#9a7945 to #ceb37b), about 1.9:1.
- What: the month marks (JAN APR JUL OCT) and hour marks (0 6 12 18) are the instrument's scale. They are blurs, and
  they fail AA (Done when 9).
- How seen: `craft/wheels-crop.png`.
- Better: dark engraving (#2a1f10, as the spec's palette says) at 8 px or more on the gold, or put the marks on the
  dark inner ring.

### 5. The spoken hint plays after the student already did it, with the on-screen hint gone (should fix, general)
- Where: `src.html:547-552` (capture listener) with `act()` at 540-541.
- What: the first pointerdown anywhere queues "Drag the time dial." and the same gesture hides the on-screen hint. So
  a student who drags the time dial first hears "Drag the time dial." after doing it. Dragging the sky or tapping a
  lever gives the same line, now with no hint on screen. The rule is that a spoken line matches the screen; here
  `valid` checks only the Manual and Place sheet. With Tab as the first key it is fine (the hint stays shown).
- How seen: voice.py V1 (hint `hidden` was already true when the line started at 1.52 s), V8, V9.
- Better: skip the line when the first gesture is on the time dial or play, and keep the visual hint until the line
  finishes. Or speak it only from a first gesture that doesn't count as the first action (Tab, Read).

### 6. Escape anywhere moves focus to the sky canvas (should fix, general)
- Where: `src.html:1397-1398`. With no Place sheet open, Escape calls `$("close-object").click()`, which runs `act()`
  and `canvas.focus()` even when no readout is open.
- What: Escape in the place search (the normal way to clear a search box) or on a lever throws focus onto the canvas
  and hides the hint.
- How seen: kb.py, focus after Escape in `#city` = `sky`, and after Escape on `#lines` = `sky`.
- Better: act only when `#object` is open, and do nothing for Escape inside inputs.

### 7. "Sydney" says the place isn't in the bundle, but it is (twice) (polish, general)
- Where: `src.html:1291-1294`. A name matching more than one place falls through to "Place not in bundled selection.
  Enter latitude and longitude."
- What: Sydney (Australia and Canada) is bundled, so the message is wrong, and the field is marked invalid.
- How seen: read.py.
- Better: "Two places match. Choose Sydney · Australia or Sydney · Canada." (the datalist already lists them).

### 8. Live-region words use internal ids (polish, general)
- Where: `src.html:1299, 1286`. Screen readers hear "milky off", "lines on", "lat 39.7 degrees".
- Better: the lever's visible name ("Milky Way off", "Latitude 39.7 degrees north").

### 9. The deep-sky card claims a magnitude range when only one value shows (nit, general)
- Where: `src.html:1136`. The hint always says "Magnitude range reflects the two source estimates." M31 shows `MAG 3.40`.
- How seen: read.py (M31 card text).
- Better: add that sentence only when the range is shown.

### 10. Readout and plate small collisions (nit, general)
- At 680x425 the brass ring runs through "AGE 26.5 d" (`craft/680-top-right-crop.png`).
- At 680x425, 800x500 and 375x812 the plate's corner dots (`.plate::before/::after`) touch "Curio" and "Dome", and
  at 375 the plate wraps to two lines ("Sky / Dome").

### 11. Two controls are not instrument-styled (polish, family:curiosity)
- The play knob with detents (spec) is a native `<select>` (`src.html:248`). The year odometer is a plain number box.
  Both work and announce their values. A detent knob and a rolling odometer would match the brass grammar of the
  wheels. The reverse switch shows only "↶"; a small engraved REV label would help.

## Checks that passed
- **Contract:** one file, 532 KB (under the spec's 600 KB). No network requests across 20+ page loads and every
  interaction (only the file itself, Network domain). No console errors or exceptions. The kit is used for voice, tone,
  Motion and Sound, with its own controls drawn. No `art:` tokens; prompts.json has none, rightly.
- **Look:** fills the screen, no header, welcome, score, goal or finish. Manual drawer and plate lower-left at
  1366x768. At 375 the plate is lower-left with Manual beside it on the right. Motion, Sound and Read are on their own
  power panel. Readouts are monospace with units.
- **Keyboard:** the Tab order runs view tools, wheels, year, transport, place, levers, Manual, power. Every one has a
  visible 3 px outline. The wheels are `role=slider` with valuetext ("20:45 local time", "2026-12-05"), announced in
  the live region. Arrow and Shift steps work, and so does Home/End. Year ArrowUp commits and announces "Year 2027".
  The rate select announces "Projector rate: 1 hour per second". Dome then Tab walks bright objects ("Moon. Enter
  selects."). Main targets: wheels 100 px, play/now/year 60 px, the rest 44 px.
- **Motion off:** Play steps 10 minutes ("Motion off. Stepped time."). Same time each night steps one day at the same
  clock. Nothing moves on its own (motion.py). Audit Motion-off row clean.
- **Words:** no em dashes in src, notes, tool.draft.json or lines. "Curio Class" is always in full. The lesson-creep
  grep only hit non-lesson uses (autocomplete, "corrected", "minute-level"). Privacy is stated ("Motion preference
  stays on this device").
- **Lines:** `voice/lines.json` holds the one line, word for word, same as `L.hint` (`allLines()`). Read's text is
  built live (date, time, place, then the object or Moon phase), as the spec says.

## Voice check (Sound on, held clicks, `__tool.vlog`)

| line | kind | expected | spoken |
|---|---|---|---|
| "Drag the time dial." (5 time-dial drags, 2 s apart) | how | 1 | 1 |
| "Drag the time dial." first tap = Read | how | 0 | 0 (Read spoke the sky) |
| "Drag the time dial." first tap = Sound | how | 0 | 0 |
| Read, 5 presses | read | 5 | 5 |
| Read with Sound off | read | 1 | 1 |
| Read 0.25 s into the hint | read cuts hint | hint cut, Read plays | hint `cut: read`, Read at +0.5 s |
| Read while Play runs | read | projector stops | stopped (`playing: false`) |

- Stale lines: the only stale case is finding 5 (the hint after its moment). Nothing plays after Reset, Now or a
  place change. No other lines exist.
- Sound off at first tap, then on: the hint never plays. That is right for a Curiosity (the hint is gone after the
  first action).
- Read text with Sirius: "November 5, 2026. 20 hours 37 minutes. Denver. Sirius, magnitude -1.46." That matches the
  card on screen.

## Note from this lens
While looking for check_tools options I ran `python scripts/check_tools.py --help`. It has no help flag and ran in
full, rebundling about 80 non-draft tools' generated `tools/<id>/<id>.html` from their current `src.html` (git-ignored
outputs; the draft tools, sky-dome included, were skipped and not touched). No src, json or tracked file was written.
The integrator should know in case a runner compares bundle timestamps.

## Audit pilot
- **Leads confirmed:** none of the 6 needed action. All 6 are "hint out of view: Drag the time dial." in states after
  an action. That is by design for a Curiosity (the hint goes after the first action), so they were **wrong leads**
  here. The audit shows "welcome not heard" on every first tap because this tool has no welcome, only the hint, which
  the "spoken" column shows correctly.
- **Clean rows cited:** sizes, Motion off, resize mid-action, five clicks and two quick taps. These agree with my own
  runs.
- **What it missed:** the anisotropic dome (1), frame time under a CPU throttle (2), the W letter under the zoom
  buttons (3; a canvas-drawn label under a DOM button), the unreadable SVG wheel engravings and their contrast (4),
  the hint spoken after the gesture it asks for while hidden (5; it logs the line but not the hint's visibility),
  Escape stealing focus (6), and the wrong ambiguous-place message (7).
