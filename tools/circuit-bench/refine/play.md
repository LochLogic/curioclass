# Refine, Play lens: circuit-bench (Curiosity No. 07)

Cold lens, round 1, 2026-11-05. Judged against CODEX-CURIOSITY.md and VISION.md "Curiosities: the second shape".
Played at 1366x768 with real held clicks and jittered drags in one muted headless tab per session (my driver:
`S:/CurioClass-codex-scratch/circuit-bench/play/play.py`, sessions s1 to s6, frames in `play/f1` to `play/f6`), once
as a grade 8 student alone at home, once as a teacher projecting at 1920x1080. Shared audit:
`S:/CurioClass-codex-scratch/circuit-bench/audit-r1`.

## Short test

- **Would a kid open it unassigned?** Yes. Two drags light a bulb with nothing read (f1/04-lit.png), parts drop
  where you let go, an LED really burns out, a motor spins to 11,500 rpm. The pull is there; the payoffs are quieter
  than they should be (findings 4, 5, 8, 9).
- **Would an adult play for fun?** Yes. The solver is honest: 0.296 A and 2.91 V on one bulb, 20.5 mA through the
  LED and 330 ohm, 1.28 A stalled motor, a staircase light that works from either switch (s6 log). The meter behaves
  like a real one, fuse included.
- **Is the real thing the interface?** Yes for circuits. Mostly no for magnetism, the anchor standard (MS-PS2-3): in
  both magnet starters the needle barely moves or does not move at all, so only a number changes (findings 1, 2).
- **Does it work with no finish line?** Yes. No score, goal, level, sticker or finish screen; the lesson-creep words
  do not appear in src.html.

First two minutes, nothing read: pass. Depth a month would still find: the board, meter and twelve parts give it,
provided the magnet side shows what it computes.

## Findings

1. **Coil + compass starter: the needle never responds to turns or the core.** Where: notebook "Coil + compass"
   (src.html loadSetup n===6), compass model src.html compassFields. What: with the default 200 turns the field is
   3.90 mT against Earth's 20 uT, so the needle sits pinned at 90 degrees. 50 turns, 400 turns, iron core: still
   90. Dragged to the far corner of the board it reads 82 with 50 turns air and 90 with the core. Things to do #10
   ("watch the field readout and the needle grow") shows only the readout. How: f3/30-coil.png, f3/31-coil-iron.png
   (780.53 mT, needle unchanged), f4/42-coil-far-50.png, f4/43-coil-far-50-iron.png, s3 and s4 logs. Better: a
   starter where the needle sits around 20 to 40 degrees (compass farther off the axis, fewer turns or a resistor in
   the loop), so each turns step and the core visibly swing it, and reversing the battery swings it across north.
   **should fix**, family:curiosity.
2. **Oersted starter: the needle moves 4 degrees.** Where: notebook "Oersted wire" (loadSetup n===5). What: the
   compass sits between the outgoing wire and the return wire, whose fields mostly cancel; closing the switch gives
   4 degrees, reversing gives minus 4. The spec's checked case (0.3 A, 1 cm, about 17 degrees; I get 16.5 from
   mu0 I / 2 pi r against 20 uT) is never staged. Oersted's swing is the moment a student remembers, and here it is a
   twitch. How: f4/sheet.png (40-oersted-on, 41-oersted-reversed), s4 log. Better: one straight jumper running over
   the compass, return path routed far away on the other half of the board. **should fix**, family:curiosity.
3. **Motor + push button starter: a mouse cannot stall the motor.** Where: loadSetup n===7; holds in
   canvas.onpointerdown (src.html, 'hold' drags). What: the motor only turns while the push button is held, and the
   shaft only stalls while the motor is held. One mouse or one finger cannot do both; I needed Space on the button
   plus a mouse hold on the motor. Things to do #8 fails for a solo student with this starter. How: f3/26-motor-running.png,
   f3/27-motor-stalled.png (stall reached only with keyboard plus mouse), s3 log. Better: a slide switch in this
   starter (keep the push button elsewhere), or let a tap on the button latch. **should fix**, general.
4. **A short circuit and a burnout are silent.** Where: src.html:296 defines L.short, which is never used anywhere;
   burn() at src.html:568 sends L.burn to status() (the status line and live region), never to the voice; neither
   event plays a tone. What: the spec's two event lines ("That is a short circuit.", "That part burned out. Tap it to
   replace it.") are never spoken, and the most dramatic moments on the bench pass without a sound. How: grep for
   V.say and L.short (no hits), voice log after a burn and a short shows only my Read. Better: V.say both as event
   lines every time, plus a short pop for a burn and a crackle or hiss while a short lasts (Sound on).
   **should fix**, general.
5. **The short chip hides the glowing wire.** Where: src.html:1768 to 1770 (chip drawn 47 px below the battery).
   What: a student who shorts the pack with one wire next to it (the obvious place) gets "Short: 9.7 A" drawn right
   over that wire, so Things to do #11 ("see the wire glow red") is covered by the label. How: f3/z25.png.
   Better: place the chip above the pack or away from any wire, and let the red wire show. **should fix**, general.
6. **9 V battery label reads "9AAV".** Where: src.html battery case (the cell loop draws "AA" even when p.nine, then
   "9 V" is drawn on top). How: f3/z20.png, every LED starter frame. **should fix**, general.
7. **The mA range blows on every bulb circuit, and the screen does not say why.** Where: simulate() fuse check;
   status "Meter fuse open." What: one bulb draws 0.30 A, two in a row 0.23 A, plus the cold-filament rush, all over
   the 200 mA fuse, so Things to do #3 on mA with any bulb starter ends in FUSE every time. That is honest, but a solo
   student only sees "FUSE" and "Meter fuse open." How: f2/11-mA-in-line.png, s2 log. Better: name the rule where it
   happens, for example the status "Fuse open: over 200 mA. Use A for bulbs." **should fix**, general.
8. **The lit bulb is a faint yellow haze.** Where: bulb case in drawPart (halo alpha at most 0.5 of #ffd348 on the
   cream board). What: the first payoff of the tool is a small filament and a pale cloud; the glass itself never
   warms. Series vs parallel still reads (orange vs yellow), but only just. How: f1/zoom-04-lit.png against
   f1/zoom-01-open.png; play/series-parallel.png. Better: warm the glass fill with the glow, a stronger bloom at full
   power, a real dull-red stage at low power. **polish**, general.
9. **Burnout has no moment.** Where: burn(). What: the LED and bulb go straight from lit to the × (spec: "watch it
   flash and go dark"). How: f3/22-led-burning-50ms.png, f6/62-bulb-4AA-250ms.png, f6/63-bulb-burned.png. Better: a
   bright flash for a few frames, a wisp of smoke with Motion on, then the dark ×. **polish**, general.
10. **The opening jumpers look already plugged in, and the hint names the wrong move.** Where: reset() jumpers end at
    e12 and f16; L.hint. What: both loose tips sit in board holes exactly like connected wire ends, and both wires
    already start at the battery, while the hint says "Drag a wire from the battery to the bulb." It worked for me,
    but a student may think they are connected. How: f1/zoom-01-open.png. Better: tips lying off the hole grid at an
    angle (or a small open-end mark), and a hint like "Drag each loose wire end to a bulb leg." **polish**, general.
11. **Nothing follows the pointer when dragging a part from a drawer.** Where: drawer onpointerdown/up. What: the
    part appears only on release; mid-drag the board is unchanged. How: f6/64-drawer-mid-drag.png,
    f6/65-drawer-dropped.png. Better: draw the part under the pointer while dragging. **polish**, general.
12. **Probe leads end in mid-air.** Where: drawProbes. What: the coiled leads stop at the board's right edge on the
    mat and never reach the meter. How: f2/10-volts-across-bulb.png, f2/12-A-across-battery.png. Better: run them to
    the meter's jacks. **polish**, family:curiosity.
13. **Canvas labels look doubled.** Where: drawPart sets shadowOffsetY 4 and shadowBlur 4 (src.html:1620 to 1622)
    before the label text, so "3 V · 0.3 A", "2 × 1.5 V" and the readouts under parts carry a ghost copy. How:
    f1/zoom-04-lit.png. Better: clear the shadow before text. **polish**, general.
14. **Projected at 1920x1080, the numbers are small.** Where: resize() caps the board at 1.25; the paper tag is
    about 12 px monospace; the meter body has a large empty middle. How: audit state-parallel-1920x1080.png. Better:
    let the board grow with the screen and give the tag values the LCD's size, so a class can read "293 mA".
    **polish**, general.
15. **Read says "Meter on OFF. OFF." and reads symbol strings.** Where: readText(). What: logged Read text "Coil.
    2.78 V · 694 mA · 1.93 W Meter on OFF. OFF." How: s4 voice log; audit row 2. Better: "Meter off." and units in
    words for the browser voice. **polish**, general.
16. **680x425 preview: the Notebook and zoom buttons cover the top rail and column numbers.** How: audit
    size-680x425.png. Better: a slimmer button row or the board shifted below it at that size. **polish**, general.
17. **Leakage shows up as readings.** An open 4 x AA pack reads "6.00 V · 0.00 A · 0.0360 μW"; an idle resistor
    "0.0600 μV" (the 1 nS leak). How: s3 and s6 logs. Better: show 0 below a floor. **nit**, general.
18. **The battery tag shows "-296 mA" beside the bulb's "296 mA".** Signed current is explained only in the Manual.
    How: f1/04-lit.png. **nit**, general.
19. **A turned LED draws its colour label upside down** ("RED" reads "038"). How: f3/21-led-reversed.png. **nit**,
    general.
20. **"CIRCUIT BENCH · DC · 2.54 mm · NO. 07" top left repeats the plate.** It reads like a title header on a tool
    that already carries the maker's plate. How: f1/01-open.png. **nit**, family:curiosity.
21. **Both AA cells are drawn the same way up** (two + ends at the top). How: f1/zoom-01-open.png. **nit**, general.

Nothing cultural, Native or hard-history: no sensitivity review needed.

Frames looked at: f1/01 to 05 and zooms, f2/10 to 13, f3/20 to 31 and sheets, f4/40 to 43, f5/50 to 53 (Motion off:
dots become still arrows, glow stays; save, clear and reopen work), f6/60 to 65; audit size-680x425, size-1366x768,
size-375x812, state-series and state-parallel at 1366x768, state-parallel-1920x1080, state-manual-375x812.

Counts: 0 blocker, 7 should fix, 9 polish, 5 nit.

## Audit pilot

- **Confirmed:** 680x425 button row over the board's top rail (finding 16). The 375 drawer strip scrolls sideways,
  as the spec asks; a cut drawer shows at the edge as a cue, so not a finding.
- **Wrong:** "hint out of view" on every notebook state: the hint is correctly gone after the student's first
  action. Manual, notebook and part-tag "text hidden" rows: those are modal drawers over the bench, as designed.
  "Close overlaps title" at 375: no collision on state-manual-375x812.png. "Welcome not heard" after Notebook or
  Manual: opening a drawer hushes it, the hint stays on the mat and Read speaks it (BASELINE rule 16), not a finding.
- **Missed:** everything that needs the physics to run: both magnet starters showing almost nothing on the needle,
  the motor stall needing two holds, the silent short and burnout (a line defined and never used), the chip over the
  shorted wire, the "9AAV" label, the fuse that blows on every bulb, the weak glow and the doubled canvas labels.
