# Codex report: circuit-bench (Curiosity No. 07)

## Built

A working DC electronics bench: a 30-column breadboard, physical components, curved jumpers, multimeter, local notebook and lower-left Manual and maker's plate. Motion, Sound and Read sit on the bench's own power panel. No kit CSS, starter, lesson frame, modes, tasks, rewards or ending.

The opening battery and bulb are disconnected. Two real pointer drags close their circuit. The filament warms and current flows from the numerical solution. All twelve drawers work, including dragging a part onto the board. Component bodies and legs can move separately; keyboard wiring uses a hole cursor. Compact benches unfold the selected part's controls with Adjust.

Included: 1 to 4 AA cells or 9 V, bulbs, four LED colours, E12 resistors, three-terminal potentiometers, SPDT switches, momentary buttons, motor and shaft hold, buzzer, coil and core, compass, six meter positions, probes, fuse replacement, conventional/electron current, eight editable setups, four local save slots and confirmed clearing. Saves never leave the device.

Source: [src.html](src.html). Offline instrument: [circuit-bench.html](circuit-bench.html). Notes, handoff, draft metadata, voice bank, audit states and empty painted-art manifest are present. The final file is **98,433 bytes (96.1 KiB)**, below both the 600 KB spec budget and 2 MB goal. No commits, deployment or polish round.

Unattended decisions: keep the requested E12 resistance range, which has 49 positions rather than the inconsistent 61; defer the schematic and generator as the spec leans; implement a quiet 2.4 kHz buzzer; use code drawing throughout. The Curiosity brief wins over the spec's automatic event narration. The report is deliberately the final artifact written, respecting the requested stop condition.

## The real material

No outside dataset or image is bundled. Actual circuits enter a conductance matrix with Norton battery sources, 1 nS reference leakage and at most 20 diode-state passes. Solver, component models and compass are separately marked in the source. Bulb heat, LED damage, motor back voltage, meter loading and the fuse affect the same network.

| Material or fact | Source and licence |
|---|---|
| Ohm's law, series/parallel circuits, Kirchhoff rules and meter connections | [OpenStax College Physics 2e, chapters 20-21](https://openstax.org/books/college-physics-2e/pages/21-introduction-to-circuits-and-dc-instruments), CC BY-NC-SA 4.0; facts cited, no text or assets copied |
| Filament resistance increasing with heat | OpenStax College Physics 2e, 20.3; same licence, facts only |
| Magnetic fields, solenoids and ferromagnets | OpenStax College Physics 2e, chapter 22; same licence, facts only |
| Motor back voltage | [OpenStax College Physics 2e, 23.6](https://openstax.org/books/college-physics-2e/pages/23-6-back-emf), same licence, facts only |
| Diode directionality | [Georgia State University HyperPhysics, Diode](http://hyperphysics.phy-astr.gsu.edu/hbase/Solids/diode.html), copyrighted page; facts only, nothing copied |
| Earth's magnetic-field context | [NOAA / BGS World Magnetic Model](https://www.ncei.noaa.gov/products/world-magnetic-model), public government information; no model coefficients or dataset used |
| All component constants, capacities, thermal timing, buzzer load, core multiplier and fixed 20 μT northward field | Explicit design assumptions supplied by the spec and declared in the Manual; not measured product specifications |
| Instrument code, drawn parts and original Manual text | Curio Class original work; MIT code, CC BY 4.0 text and graphics |

Wires use 0.01 Ω. Their magnetic field is integrated along their drawn path using Biot-Savart, with the compass 1 cm below the wire plane. Coil centre field uses the finite-solenoid equation; its external compass coupling uses a declared distance falloff approximation. There are no inductive transients, battery depletion, steel interference or core saturation. Dots are visual current indicators, not electron drift speeds. These limits are in the Manual.

## Break the instrument

[Independent computations](../../_scratch/circuit-bench/independent-numbers.json) and [actual JavaScript solver checks](../../_scratch/circuit-bench/solver-results.txt) cover:

| Case | Result |
|---|---|
| One bulb, two AA cells, two wires | 0.29636 A; 2.90516 V across bulb; 9.80274 Ω hot |
| Two bulbs in series | 0.22643 A; 0.33119 W each; branch currents agree |
| Two bulbs in parallel | 0.58524 A from the source; branch currents sum to source current |
| Red LED, 330 Ω and 9 V | 20.496 mA; no damage |
| Direct red LED, two AA cells | About 96.9 mA before damage; opens, then conducts again after replacement |
| Reversed LED | Zero modeled forward current |
| Motor, two AA cells | About 11,511 rpm at 0.150 A; held shaft about 1.293 A; release returns to running current |
| A probes across two AA cells | About 9.68 A, source short indication; mA opens its fuse |
| Cold 330 Ω resistor | 330 Ω; disconnected pair OL; powered resistance measurement LIVE |
| Coil centre field | 5.61985 mT/A for 200 air-core turns; core multiplier checked |
| Straight-wire equation limit | 0.3 A at 1 cm gives 6.0 μT; with 20 μT north, 16.70° |

Small differences from rounded spec examples come from explicit wire resistance and topology. The simplified independent parallel calculation and exact wired network differ slightly for that reason.

The [random-network stress test](../../_scratch/circuit-bench/stress-solver-results.txt) checks 300 diode networks. Maximum Kirchhoff residual was 2.631 nanoamps; none reached the iteration limit. Empty networks and wide resistance ranges stay finite.

Real, whole-pixel pointer drags verified first and second jumpers, drawer placement and moving a body to the edge without changing its four-column leg span. Quarter turns return to their initial geometry; a turn beyond the board is rejected. Empty mat, floating probes, clear/cancel, local save/reload, powered ohms, fuse failure, zero wiper setting and running resize were exercised. The final small camera keeps both opening terminal pairs in view.

Motion off produced identical canvas pixels 700 ms apart while the solved bulb current remained 0.296 A. Current becomes stationary arrows. Grayscale frames retain polarity signs, labels and readings.

With 30 parts, 30 wires and 59 electrical nodes, desktop Chrome measured a 16.6 ms median frame interval, 18.1 ms at the 95th percentile, and 1.9 ms of instrument work at the 95th percentile. This is desktop evidence, not a physical Chromebook measurement.

## Voice walk

Bank: calm-professor / Schedar. No recordings were made, as instructed; Curio.voice uses the browser fallback. Dynamic values are available through Read and the meter's polite live region.

The [615.4-second interaction walk](../../_scratch/circuit-bench/walk-results.json) logged the initial hint once and two explicit Read requests, with no runtime exceptions. Its network log contains only the local HTML file. All test Chrome instances were muted.

Automatic short and burnout speech from the spec was omitted because the Curiosity brief permits only the initial hint and subsequent Read. Those events remain visible and announced through the live status region. The initial hint disappears after a material action. A final targeted Manual/Close/Read walk verified that opening a drawer does not queue a stale wiring instruction behind it.

The audit's held-click, five-click and quick-tap checks completed without voice repetition or focus failures. Keyboard adjustment changed the battery to three cells, kept focus on Cells and announced “3 cells, 4.5 volts”; the unfolded tag title updated with it.

## Short test

These are design judgments informed by a ten-minute automated interaction walk, not findings from child or adult participants.

- **Would a kid open it unassigned? Yes:** the waiting battery, bulb and loose jumper ends invite a direct physical action; closing the loop makes light without a page of instructions.
- **Would an adult play for fun? Yes:** measuring a circuit changes it, a spinning motor makes back voltage, and polarity and coil changes give further things to investigate. The notebook preserves experiments.
- **Is the real thing the interface? Yes:** terminal topology, component bodies, light, current, meter loading and magnetic response are the instrument. Readings are calculated, not preset outcomes.
- **Does it work without a score or finish? Yes:** any setup can be rewired or discarded; nothing grades it, unlocks it or ends it.

Compared with Elements Inspector, the bench is quieter when disconnected; that is an honest unpowered instrument. Its density comes from the board, physical parts and independent probes. I would keep using it to compare measurements and magnetic effects, with the declared DC-model limits in mind.

![Circuit Bench beside Elements Inspector](../../_scratch/circuit-bench/short-test-comparison.png)

## Lesson creep check

[Search results](../../_scratch/circuit-bench/finish-results.json): no prohibited lesson language in voice lines. Four source hits are all “points”: one means physical measurement points; three refer to the coordinate array used to constrain body dragging. None means rewards. No score, goal, level, sticker, badge, quiz, finish screen, mode pills or kit header was built.

## Done when

| Spec item | Verdict and evidence |
|---|---|
| 1. Disconnected opening; two wires light a bulb | PASS: real pointer input, final-drag.json; first wire leaves it dark, second settles at 0.296 A |
| 2. One bulb about 0.30 A / 2.9 V; series about 0.23 A | PASS: independent and JavaScript solver checks; actual meter loading is included |
| 3. Protected LED 20-21 mA; direct LED burns and is replaceable | PASS: 20.496 mA, damage and replacement assertions |
| 4. Reversed LED dark; reversed battery reverses compass | PASS: zero-current and compass polarity assertions |
| 5. Held motor about 1.3 A, running about 0.15 A | PASS: stall, release and speed assertions; held-control browser checks |
| 6. A short indication; mA replaceable fuse | PASS: source short and fuse assertions, visible FUSE state |
| 7. Keyboard placement, wiring, measurement and announced controls | PASS: hole cursor, native adjustments, keyboard wire input, probe arrows; audit Enter walks and final focused range test |
| 8. Motion off leaves light and static current arrows | PASS: identical canvas pixel comparison with bulb powered |
| 9. Required desktop, preview and phone sizes | PASS: all eight required viewport/iframe cases inspected; targeted compact fixes verified with zero horizontal page overflow |
| 10. Offline file, checker, punctuation and Chromebook speed | FAIL strictly on hardware validation: offline/checker/punctuation and desktop speed pass; physical school Chromebook speed was not measured |
| 11. Honest short-test answers with frame comparison | PASS: this report and comparison PNG |
| 12. No scoring or ending structure | PASS: source and voice search with coordinate-word exceptions explained |

The repository's unmodified check() and notes_sections() functions pass for this instrument, using a scratch metadata mirror. The global check_tools.py command was not allowed to rebundle other tools outside the write scope. The method and zero problems are recorded in contract-results.json.

## Audit leads

The single full audit completed: **147 leads**, with no runtime, focus, repeated-speech or stuck-resize failures. Its snapshot predates the final corrections. It was not rerun. Every lead has a disposition in [audit-dispositions.json](../../_scratch/circuit-bench/audit-dispositions.json); the [snapshot-to-final diff](../../_scratch/circuit-bench/after-audit.diff) is preserved.

- Fixed confirmed meter overlap at 1000x625 by using the compact dial selector at short heights.
- Fixed cramped tray labels; all twelve drawers fit at 680, 760 and 1000. The phone retains the explicitly requested horizontal parts strip, reachable by touch and Tab.
- Fixed hidden adjustment controls with a wrapped Adjust drawer; the phone frame and bounds show every control in view.
- Fixed phone engraving below 10 px, Manual/Notebook close-heading overlap and source-link hit areas. All three source links measure 44 px high.
- Canvas corner controls intentionally overlay the mat. Native drawers intentionally cover and inert the underlying bench. The initial hint intentionally vanishes after action; sources intentionally live at the end of a scrollable Manual.

The final targeted browser batches reported zero browser errors. Two host socket resets occurred as Chrome closed connections during test-server shutdown; they were not instrument exceptions. All Chrome ports 9980-9987 and host 8785 were subsequently verified closed.

## Frames looked at

Inspected the four reference frames, four early frames, all functional and full-size frames, all 89 audit frames through twelve labelled contact sheets, four ten-minute walk frames, final compact/phone adjustments, source links, keyboard focus, current arrows, geometry extremes, drawer/body drags and the side-by-side comparison. Confirmed issues were also inspected at full size.

Evidence directories: references/, early/, functional/, final/, audit/, post/, last/ and drag-parts/ under _scratch/circuit-bench/. Validation scripts, input batches, numeric results, per-lead dispositions and artifact hashes are preserved there. The [validation manifest](../../_scratch/circuit-bench/validation-manifest.json) records the final executable artifacts and closed ports before this final report write.

## Art made

Zero painted images and zero recorded audio. Breadboard holes, rails, labels, screws, filament, glass, polarity, resistor bands, motor flywheel, coil windings, compass, probe cables and tray miniatures are original canvas/SVG drawing. No image was needed or left as a placeholder. Original drawn materials and instrument colours follow the circuit spec, not the reference tools' palettes.

## Engine changes wanted

None. Shared Motion, Sound, Read and tones were used without changing kit files.

## Left open

- Physical Chromebook speed and an actual child/adult usability study remain unmeasured. The desktop benchmark and short-test judgments are explicitly limited above.
- Coil external-field falloff, fixed Earth field, motor mechanical response, diode thresholds and damage timing are stated approximations. This is a DC instrument, not a transient or product-calibration model.
- Browser voice fallback is used; no Schedar recording was generated. Schematic view and generator remain deferred as specified.
- Procedural deviations: startup troubleshooting printed extra regular-brief sections, and two initial read attempts lacked an explicit command kill limit. They did not write artifacts; subsequent checks used explicit time limits. The Curiosity brief governed the actual implementation.
- No deployment or commits were made. No polish round was started.
