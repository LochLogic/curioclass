# Polish: circuit-bench (Codex fix, round 1)

Evidence root: `_scratch/circuit-bench/`. Before and after batches use scripts/drive.py, muted Chrome 9910, 1366x768 unless a size is in the name. The phone runs in an actual 375x812 iframe on host 8715. No questions were asked in this unattended run; all settled calls were followed. No circuit constants were retuned.

## Blocker
1. FIXED: coil vector dipole field and switched 50-turn starter. Before 88.37/89.19/89.59/89.80 degrees; after 28.37/46.93/64.60/76.26 degrees. Core 89.07; cells 1 to 4 give 15.71/28.37/37.91/44.99; reversal -46.29; open switch essentially zero. Axial +29.17 versus beside -73.20 in the field-only diagnostic. Evidence: before-coil.json, proof-coil.json, proof-coil-equator.json and corresponding viewed frames. Manual names dipole moment, return field and near-field softening.
2. FIXED: compass is 1 cm above the drawn wire; vertical jumper and distant return. Before +4.34/-3.75; after -13.71/+13.79 and open essentially zero. Evidence: before-oersted-conducting.json, after-oersted.json and viewed frames. The finite drawn wire yields about 14 degrees; the independent infinite-wire 0.3 A example is 16.70 degrees. Manual includes the alignment discovery.

## Should fix
1. FIXED: real held-input walk logged hint once, burn twice and short twice. Pop and crackle were logged only with Sound on; tone count stayed 88 before and after a Sound-off short. Event queue is repeatable, and bulb inrush has an 80 ms short-event qualification. Evidence: fix-interactions/results.json.
2. FIXED: burn rebuilds the tag immediately; after-burn.json has Replace=true versus false before. Real body tap replaced it, confirmed in fix-interactions/results.json and the viewed burned-part-tap-replaced frame.
3. FIXED numerically: latching motor tag with visible Release shaft and aria-pressed. Stalled 1.282 A; released 0.150 A at 11,498 rpm. One pointer then held the separate push button at 1.282 A, confirmed in the viewed motor-one-pointer-stalled frame.
4. FIXED: blocked LED loop reads 0.00 in A and mA, empty and missing probes retain - -. before-zero-ammeter.json, after-zero-ammeter.json, proof-ammeter-cheats.json and open-switch-zero.json (0.00 A). Occupancy includes terminals on open contacts and burned parts, independent of conducting edges.
5. FIXED: short chip searches for a free position. proof-short-clearance.json measures 9.87 world px clearance from sampled wire/probe geometry; frame viewed at 1366x768.
6. FIXED: dedicated 9 V body and snap terminals; viewed after-9v-labels and proof-turn-labels frames.
7. FIXED: no text shadow or offset. proof-turn-labels.json reports transparent shadow, offset 0 on every tested label. Viewed frames show sharp labels.
8. FIXED: fuse status explains over 200 mA and Use A for bulbs; before-fuse.json versus after-fuse.json; Manual agrees.
9. FIXED: Manual explicitly states every coil is 4 ohms and explains wire gauge versus turns. before/after manual text and proof-manual frame.
10. FIXED: requested real-bench safety sentence in Manual and teacher notes; notes restrict the model to battery-level DC. before/after manual text and proof-manual frame.
11. FIXED: physical switch marks and visible ON/OFF legends. after-controls.json and proof-toggle-off.json, both frames viewed.
12. FIXED: inset board ring at -6 px. before-focus-keyboard.json versus proof-focus-board.json and viewed frame.
13. FIXED: dark ring plus light rim on paper. 13.69:1 board, 10.31:1 tag, 12.73:1 Manual. proof-adjust-680 frame and fix-contrast.json. Ratios added to notes.md.
14. FIXED formatter: spoken units, no reading, fuse open, full sentence before Meter, Meter off. before-controls.json versus proof-read-format.json; Actual held Read produced the formatted volts sentence in fix-interactions/results.json.
15. FIXED: centralized tool-state synchronization clears pressed drawers after placement, selection, Escape, reset and restore. before-controls.json had part-resistor pressed; after-controls.json has none.
16. NOT FIXED: 4x CPU, 30 parts with five lit bulbs improved from 20.62 fps to 45.39 fps, still below 60. Board and part raster caches, native Bezier wires, dirty solving and idle redraw suppression are implemented. Mean measured frame work fell from 5.86 ms to 1.16 ms. Idle stays at one solve and two draws over two seconds. Evidence: perf-five-before.json, perf-five-after-cached.json, perf-idle-after-cached.json. No physical Chromebook or 60 fps claim is made.
17. FIXED at 680x425: non-modal grid tray under the tag; board 110 px tall, tag y204, tray y239. Viewed proof-adjust-680. The final 375x812 frame shows resistor, LED, tag and controls together.

## Polish accepted
1. FIXED: warmer glass, stronger bloom, distinct low-power red filament; after-perf and proof-projector frames viewed. Viewed final-mode-1 beside final-mode-0 and final-mode-2, including their final regression frames.
2. FIXED: bright flash, Motion-gated smoke and final dark cross. Viewed fix-interactions/burn-flash.png and fix-targeted-final/burn-flash-motion-on.png plus burn-smoke-motion-on.png. The frame loop makes one final redraw when the effect expires, including Motion off.
3. FIXED: battery tag says supplies with positive current; proof-short-clearance.json and viewed frame.
4. FIXED: each discovery has its short attribution, including Oersted in 1820; proof-manual text and viewed frame.
5. FIXED visually: off-grid tips and open-end rings; final opening frames viewed. Real black-first then red connection produced 0.296 A and glow 0.957.
6. FIXED: document pointer delegation keeps the part preview under a drag that has left its drawer. fix-interactions/ghost.json reports ghost=true; mid-drag frame viewed.
7. FIXED: probe leads continue to actual meter jacks, including an SVG bridge across the canvas edge; dial legends engraved. proof-short-clearance and default frames viewed.
8. FIXED at 1920x1080: tag values 22 px; board scale 1.437 rather than capped at 1.25. proof-projector.json and frame viewed.
9. FIXED: tools moved above board at 680x425; motor push button visible at 800x500. Both viewed frames and proof-motor-800.json.
10. FIXED: LCD no longer aria-live; changed reading announced after one second of stable display or on Read. Actual Read log confirms the formatter.
11. FIXED: compass tag only angle, no electrical zeros. compass-tag.json shows only 28 degrees from north with an empty extra line.
12. FIXED: tags floor magnitudes below 1 micro-unit to zero, suppressing 1 nS leakage; opening frame has zeros.
13. FIXED: canvas text counter-rotates at any part angle. proof-turn-labels.json RED rotation 0; frame viewed.
14. FIXED: alternating AA polarity ends; final opening frames viewed.
15. FIXED: runtime high-draw caveat and LED ohms test-source caveat in Manual; proof-manual text.
16. FIXED: shared spoken formatter used for resistor aria-valuetext; range-spoken.json reports 3.90 kilohms resistor after an actual input event. The final frame shows the changed bands and faded LED; the range naming collision was corrected.
17. FIXED: top-left duplicate name and number removed; viewed opening frames retain the engraved maker plate.

## Settled calls
All applied: no lesson targets, goal, score, level, quiz, finish or kit header. Hint behavior preserved. Manual and Notebook remain modal; Adjust is non-modal. Burn line unchanged and motor starter retains its push button. AA/bulb/LED/motor values unchanged. Spec open questions remain for the integrator.

## Cheats tried
Blocked LED and open meter checks cannot turn a floating probe into a zero reading: empty and missing probe tests both keep - -. Coil-only axial/equatorial diagnostic checks direction, not just an increasing field label. No score or passing state exists. Additional attempts: A directly across the source reads +9.62 A, swapped probes -9.62 A, and mA opens its fuse; open push-button terminals read zero rather than floating. The series/parallel inrush test produces zero false short events; a lasting hard short produces one event (short-debounce.json).

## Voice walk
Real held inputs, with 2 s pauses at setup changes: hint once, burnout twice, short twice, a Sound-off short silent, then Read: Bulb. 2.91 volts, 296 milliamps, 861 milliwatts. Meter on volts. 2.91 volts. The exact log is fix-interactions/results.json. voice/lines.json remains identical to allLines(). Browser speech fallback is used; existing missing recordings are not generated in this session.

## Engine changes wanted
None.

## Audit
AUDIT NOT FINISHED. Ran scripts/audit_tool.py once with a 2400 second limit, Chrome 9911 and host 8715. Chrome disconnected at the first size before any frame or audit.md: ConnectionResetError, Windows error 64, specified network name no longer available. No audit leads were produced. Per CODEX-FIX, stopped testing and reported the failure instead of starting another audit. The required exit gate is not claimed.

## Left open
Should fix 16 remains NOT FIXED at the requested 60 fps bar; the final mechanical audit did not finish. Spec open questions about module coverage and scaling coil resistance were left unchanged. The 20 microtesla field, core multiplier, capacities and component constants are declared model assumptions. No physical Chromebook measurement is claimed.


## The real material
No datasets, photographs, fonts, third-party prose or recorded clips were downloaded or bundled. The material is original circuit code and equations; numerical constants are the spec's declared design choices, not product measurements. No data sampling or packer is needed. Online checks were factual corroboration only, within the 45 minute gathering allowance.

- OpenStax College Physics 2e, chapters 20 to 23: Ohm/Kirchhoff rules, series/parallel circuits, heating, ammeters, coils and back EMF. Current site licence CC BY-NC-SA 4.0, checked 2026-11-06; facts only, no text/images copied. https://openstax.org/books/college-physics-2e/pages/21-4-dc-voltmeters-and-ammeters and https://openstax.org/books/college-physics-2e/pages/22-9-magnetic-fields-produced-by-currents-amperes-law
- OpenStax University Physics Volume 2, 12.1, 12.2, 12.4, 12.6: Biot-Savart, straight-wire orientation, loop moment and finite solenoid. Current site licence CC BY-NC-SA 4.0, checked 2026-11-06; facts only, no assets copied. https://openstax.org/books/university-physics-volume-2/pages/12-2-magnetic-field-due-to-a-thin-straight-wire and https://openstax.org/books/university-physics-volume-2/pages/12-4-magnetic-field-of-a-current-loop
- Independent magnetic check: MIT 8.02T, Sources of Magnetic Fields, 9.5 equation 9.5.5 and 9.1, copyrighted course notes; used only to check equations and signs, no text or assets bundled. https://web.mit.edu/8.02t/www/802TEAL3D/visualizations/coursenotes/modules/guide09.pdf . Coil wire-length caveat also checked against MIT 8.022 lecture 7 and NIST Circular 470; facts only (NIST is US government material).
- Oersted's 1820 attribution: OpenStax 12.2 independently corroborated by University of Copenhagen, Niels Bohr Institute, Electromagnetism - The unique discovery (copyright university site, facts only), checked 2026-11-06. https://nbi.ku.dk/english/www/hco/oersted/opdagelsen . The spec's Britannica route was unavailable; no text from it was copied. Its existing citation is retained as the requested discovery attribution.
- Short heating/burn safety: US Consumer Product Safety Commission, Batteries (US government information), checked 2026-11-06, alongside OpenStax electrical heating. https://www.cpsc.gov/Regulations-Laws--Standards/Voluntary-Standards/Topics/Batteries . Energizer Battery Care independently corroborated short-circuit heat, copyrighted website, facts only: https://energizer.com/about-batteries/battery-care/ . No battery dataset or manufacturer text was copied.
- Existing diode facts: Georgia State University HyperPhysics, Diode, copyrighted, facts only; E12 values: Vishay document 31001, copyrighted, facts only; NOAA/BGS WMM: government field context only, no coefficients bundled. Their names and licence statements remain in the Manual and tool.draft.json. Component values, nominal capacities, core multiplier, numerical floors and fixed 20 microtesla Earth field are Curio Class design assumptions. Code MIT; original text and drawn instrument CC BY 4.0.

## Numbers and regression evidence
Independent arithmetic in fix-numbers.json retains one bulb 0.29636 A, two series 0.22650 A, parallel about 0.586 A total, LED 20.496 mA and the infinite-wire 6.0 microtesla / 16.70 degree example. The motor starter's extra contacts/wires give the measured 1.282 A stall and 0.150 A running. None of the verified source, bulb, LED or motor constants changed.

All eight starters were re-shot at 1366x768, along with the default, calm arrows, 1920x1080 projector, 800x500 motor and compact Adjust at 680x425 and 375x812. Opening screens at every STANDARDS size have no page scroll. Final targeted batch: zero console errors; prior range exception corrected and re-shot. The offline resource walk returned an empty resource list. Bundle is about 113 KB. The repository contract helper passed on a scratch metadata mirror without invoking the global rebundler; source and voice have no em dash.

Viewed frame groups: fix-before/, fix-before-more/, fix-after/, fix-proof/, fix-sizes/, fix-interactions/, fix-final-modes/, fix-targeted-final/, fix-perf/ and fix-perf-cached/. Contact sheets are in Scratch. JSON numbers live directly in Scratch unless their folder is named. Intermediate frames that caught the tray overlay, stale burn flash, range exception or false startup short are superseded by the targeted final frames and numbers, not counted as proof.

## Curiosity shape
The four short-test qualities remain visible: an unassigned student gets light with two real wire drags; an adult can probe and rewire; the filament, needle, coil and meter are the interface; it runs without a score or finish. This fix used instrument interactions and inspected frames, not a fresh ten-minute student/adult play session. No lesson gate was added. The lesson-creep search found only electrical points and geometry variable names (fix-lesson-creep.json); voice lines contain none of the lesson terms.

Manual evidence counts from the browser-captured Manual text at 1366x768: each of the fixed-resistance explanation, real-bench safety line, high-draw runtime caveat, diode ohms caveat, Oersted attribution and above-wire geometry note occurs exactly once. Exact excerpts and counts are in fix-manual-evidence.json. Browser and host listeners started here are closed.
