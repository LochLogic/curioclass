# Craft lens: circuit-bench (Curiosity No. 07), round 1

Bundle looked at: `tools/circuit-bench/circuit-bench.html` as built (not re-bundled). Shared audit:
`S:/CurioClass-codex-scratch/circuit-bench/audit-r1/audit.md`. My frames and check script are in
`S:/CurioClass-codex-scratch/circuit-bench/craft/` (`craft_checks.py`, `perf2.py`, `results.json`, `*.png`).

## Contract and look rules (passed)

- One file, 100 KB on disk (103,901 characters rendered), no fonts, no bitmaps. Well under the 2 MB goal.
- No network requests. CDP Network log on five fresh pages shows only the file itself; `performance.getEntriesByType('resource')` is empty. The Manual's source links are plain anchors and load nothing.
- No console errors or exceptions on any of my pages, and none in the audit's click table.
- Kit used for voice, tones, Motion and Sound (`Curio.voice`, `Curio.init`); no kit header, no lesson frame.
- No em dashes in src, bundle, notes, spec, lines or tool.draft.json. "Curio Class" is never shortened in any text a person reads (`Curio.` hits are kit API names).
- Lesson creep: grep for score, points, level, goal, sticker, badge, correct, wrong, try again, complete, well done finds only code variable names and Manual prose ("put the probes across two points"). No welcome screen, goal, finish or quiz.
- The object fills the screen; Manual and the engraved plate sit lower left; Motion, Sound and Read are on their own panel top right; readouts are monospace with units (LCD, part tag, battery runtime, rpm, mT, degrees).
- Privacy is stated where circuits are stored: "Circuits stay on this device. Nothing leaves it." (Notebook).
- Lines: `voice/lines.json` has the same three strings as `L` and `allLines()`, word for word.
- Art: `art/prompts.json` has no assets and the source has no `art:` tokens. Everything is drawn in code, which fits a Curiosity. No people.
- Motion off: the dots become still arrows and the bulbs keep their glow (`calm-parallel-1366.png`, `zoom-calm-arrows.png`). Done when 8 holds.
- Keyboard: a whole circuit can be built from the keyboard. Tab reaches the board after Motion, Sound and Read. W, Enter, 10 x Right, Enter, then W, 4 x Right, Enter, 10 x Left, Enter lights the bulb at 0.296 A, and "Wire connected." is announced (`kb-bulb-lit-1366.png`). Dial key 1 gives "Meter dial: volts". The red probe takes Enter and arrows ("Probe e 10"). The resistor range announces "3.90 kΩ resistor".

## Findings

1. **Event lines are never spoken.** src.html:296 and 565. `L.short` and `L.burn` are in lines.json, but no `V.say` is called anywhere in the file (grep `V.say`: no hits). A burned LED only writes the status bar. A short makes no line, no status and no announcement at all: the status stays "Meter on amps." and the only sign is the canvas chip. The spec's Voice section says both events are spoken every time. Seen in `results.json` voice run: the vlog after a burn, a 9.68 A short and an mA fuse blow holds only the hint and one Read. Level **should fix**, tag general.

2. **A part that burns while selected keeps a stale tag, and the line names the wrong action.** src.html:565. `burn()` never calls `showControls()`, so the selected LED's tag reads "Red LED · × OPEN" but still shows Red, Turn LED, Move, Turn, Remove, with no Replace (`voice-burned-led-1366.png`; `#replace-part` absent in the DOM). "That part burned out. Tap it to replace it." is also wrong: tapping the part only selects it, and the student still has to press Replace. Better: rebuild the tag on burn and say "Tap Replace on its tag." Level **should fix**, tag family:curiosity.

3. **Motion and Sound show on or off by shade alone.** src.html:15 and 158. Both buttons read "Motion" and "Sound" in both states. The only visible cue is the pressed fill, #182c24 against #292e2b to #454944 (1.07 to 1.61:1). See `zoom-power-on.png` and `zoom-power-off.png`. aria-pressed and aria-label are right, so screen readers are fine; sighted users get colour only. The look rule asks for toggle switches. Better: a drawn toggle with an ON and OFF legend, or a lit pilot lamp plus the word. Level **should fix**, tag family:curiosity.

4. **Focus on the breadboard has no visible outline.** src.html:16 and 28. `canvas:focus-visible` draws a 3 px outline at a 2 px offset, but `.board-wrap { overflow:hidden }` and the canvas fills that box, so the outline is clipped away. After four Tabs the board has focus, and the only sign is the small hole-cursor ring (`focus-4tabs-1366.png`). Level **should fix**, tag general.

5. **The focus ring all but vanishes on paper surfaces.** src.html:16. #ffda73 measures 1.2:1 on the part-tag paper (#d2cbb0), 1.03:1 on the Manual and Notebook paper (#e8e0c9) and 1.1:1 on the board (#ece8dc). Every control in the tag strip, the Adjust drawer, the Notebook and the confirm dialog sits on these. `zoom-focus-hold.png` shows "Hold shaft · H" focused with a faint light edge; `state-part-tag-680x425.png` shows "Move" focused the same way. notes.md only measured the ring on the mat. Better: a dark ring (for example #1a1f17 plus a light inner ring) inside paper areas. Level **should fix**, tag general.

6. **Read speaks symbols and reads awkwardly.** src.html:328 to 331. Logged Read texts: "Drag a wire from the battery to the bulb. Meter on OFF. OFF.", "Bulb. 2.81 V · 293 mA · 823 mW Meter on volts. 2.81 V." and "BREADBOARD · 30 columns. 2.54 mm pitch Meter on milliamps. FUSE." These have no full stop before "Meter", and unit symbols (V, mA, mW, Ω), middle dots and "- -" go straight to the speech engine. STANDARDS says nothing a voice would misread, and the spec's own example is "Meter on volts. 2.94 volts." Better: a spoken formatter (volts, milliamps, milliwatts, ohms, "no reading"), and "Meter off." for OFF. Level **should fix**, tag general.

7. **A parts drawer stays pressed after its tool is used up.** src.html:383 and 1166. `pickTool` sets `aria-pressed` on the drawer, but neither `placeAt` nor `select` clears it. After both keyboard wires were placed (tool null, cursor label shows no tool), the Wire drawer is still drawn pressed (`kb-probe-focus-1366.png`). The look and the announced state then say a tool is held when none is. Level **should fix**, tag general.

8. **The 9 V pack is overprinted "9AA V".** src.html:1634. The cell loop draws a "+" and an "AA" label for the single 9 V cell, then "9 V" is drawn on top (`zoom-9v.png`, from the LED and 9 V setup and every 9 V pack). Level **should fix**, tag family:curiosity.

9. **Every label printed on a part is doubled by a stray shadow.** src.html:1622. `shadowOffsetY=4` stays set while the part text is drawn: the bulb's `shadowBlur=0` and the reset to `#27352b60` keep a hard 4 px offset copy. So "3 V · 0.3 A", "2 × 1.5 V", "RED", the rpm and mT labels all show a ghost line under them (`zoom-labels.png`, `zoom-calm-arrows.png`). The rpm and mT labels are live readouts. Level **should fix**, tag family:curiosity.

10. **60 fps with 30 parts is not shown on a modest machine, and the loop never rests.** src.html:1814 to 1840. Unthrottled at 1366x768: 16.7 ms frames, 1.7 to 2.4 ms of script per frame with 30 to 32 parts. With CDP CPU throttle 4x in headless software rendering, the opening bench ran at about 30 fps (26 ms average). Thirty parts with five lit ran at about 13 fps (77 ms average, 8.6 ms of script). At 6x, the script alone took 18.6 ms per frame. Headless software raster overstates the time, but the step from 2 parts to 30 is real: per-part `shadowBlur`, radial glows, and the whole board (420 holes, three primitives each, plus numbers) are redrawn every frame. Also, `circuitDirty` is set everywhere but never read, so the solver runs three times and the full redraw runs every frame on an idle bench. Better: cache the board in an offscreen canvas, drop per-part shadows, and skip the solve and draw when nothing changed and Motion has nothing to animate. Then measure on a real Chromebook-class machine. Level **should fix**, tag general.

11. **The compact Adjust drawer hides what it adjusts.** src.html:888 and the `adjust-part` handler. Below 1050 px, the part controls move into a modal `<dialog>` (`showModal`). It covers the board and the tag readout, so a student who turns the resistor or pot cannot watch the LED or the numbers change (`state-part-tag-680x425.png`). Spec thing to do 6 is exactly that. Better: a non-modal tray that leaves the board and tag values in view. Level **should fix**, tag family:curiosity.

12. **The probe leads end in mid-air, and the dial has no legends.** src.html:1778. Both probe leads run to a fixed point at x 965 in the empty mat right of the board, not to the meter (`voice-short-chip-1366.png`, `calm-parallel-1366.png`). The probe-tip labels "V" and "COM" land on the Short chip and on board holes. The rotary dial has tick marks but no OFF, V, mA, A, Ω or beep legends, so it cannot be read on its own. Better: leads that leave the board edge toward the meter, and printed dial legends like a real meter. Level **polish**, tag family:curiosity.

13. **The preview sizes crop the instrument.** At 680x425 the Notebook, zoom and centre buttons sit over the top rail and column numbers 1 to 8, and the lower half of the board is out of view (`size-680x425.png`). At 800x500 the motor setup's push button, the part the student presses, is cut off behind the meter edge (`state-motor-800x500.png`). Better: centre the view on a setup's parts when it loads, and keep the board tools off the board at short heights. Level **polish**, tag family:curiosity.

14. **The LCD live region can chatter.** src.html:172. `#meter-reading` is `aria-live="polite"` and is rewritten up to five times a second whenever the value changes, for example while a motor spins up or a bulb warms. A screen reader then queues every number. Better: announce on a settle or on Read only. Level **polish**, tag general.

15. **The top-left bench label repeats the plate.** src.html:156. "CIRCUIT BENCH / DC · 2.54 mm · NO. 07" repeats the plate's name and number. It is not a header bar, but it is a second title. Level **nit**, tag family:curiosity.

16. **Ω goes to screen readers as a symbol.** The resistor range's `aria-valuetext` is "3.90 kΩ resistor", and some screen readers say "omega". Better: "3.9 kilohm resistor". Level **nit**, tag general.

## Standard voice check

Driven with held clicks (0.12 s), Sound on, Motion on, at 1366x768 (`craft_checks.py` voice and read runs; audit click table for first taps).

| line | kind | expected | spoken |
|---|---|---|---|
| Drag a wire from the battery to the bulb. | welcome / how | once in five board taps | 1 (then silent) |
| That part burned out. Tap it to replace it. | event | each burn (1 burn caused) | 0 |
| That is a short circuit. | event | each short (1 short caused) | 0 |
| Read | read | each press | 2 of 2, plus the audit's 5 of 5 |

- Repeats: the how line passes. Both event lines fail, because they are never queued (finding 1). The five-in-a-row run on Replace could not be done: Replace is missing on a burned selected part (finding 2).
- Stale lines and order: only one line is ever spoken, so nothing can go stale. The audit's five-click and two-tap rows are clean for every control that spoke.
- First tap: the audit table shows nothing before the tap. A plain tap gets the hint. Sound says nothing. Read speaks the hint plus the meter text. Notebook and Manual skip the hint because a dialog is open; the hint stays on screen and Read says it, so that is allowed under BASELINE rule 16.
- Read: the kit handles Read cutting a line and the empty queue. The Read text itself has problems (finding 6).

## Audit pilot

- **Leads confirmed:** at 680x425 and 800x500, the board tools overlap the board and cover the top rail (finding 13). At 375x812 the parts drawers scroll sideways, but that is by design (the spec asks for a strip), and a partly shown next drawer hints at the scroll.
- **Leads that were wrong:**
  - "Hint out of view" in every setup state: the hint is hidden after the first action, as the Curiosity brief asks.
  - Every "text hidden under" and "keep region covered" row for manual, notebook and part-tag: those are modal drawers over the bench by design.
  - The Manual's five source links counted as "choices cut short": the drawer scrolls.
  - The 375 Close and title "overlap": `state-manual-375x812.png` shows them side by side, clear.
  - The "welcome not heard" rows for Notebook and Manual: these are allowed, see the voice check.
- **What it missed:**
  - The event lines are never spoken. The audit only counts lines on taps, and no tap causes a burn or a short.
  - The stale tag after a burn.
  - The colour-only power toggles.
  - The clipped canvas focus ring, and the focus ring's contrast on paper.
  - The drawer left pressed.
  - "9AA V" and the doubled part labels.
  - The Read text wording.
  - The modal Adjust drawer hiding the readouts.
  - The idle loop and the frame cost under CPU throttle.

Nothing cultural, Native or hard-history here; no sensitivity review needed.
