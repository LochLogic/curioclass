# circuit-bench: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: circuit-bench (Curiosity No. 07)

#### Built

A working DC electronics bench: a 30-column breadboard, physical components, curved jumpers, multimeter, local notebook and lower-left Manual and maker's plate. Motion, Sound and Read sit on the bench's own power panel. No kit CSS, starter, lesson frame, modes, tasks, rewards or ending.

The opening battery and bulb are disconnected. Two real pointer drags close their circuit. The filament warms and current flows from the numerical solution. All twelve drawers work, including dragging a part onto the board. Component bodies and legs can move separately; keyboard wiring uses a hole cursor. Compact benches unfold the selected part's controls with Adjust.

Included: 1 to 4 AA cells or 9 V, bulbs, four LED colours, E12 resistors, three-terminal potentiometers, SPDT switches, momentary buttons, motor and shaft hold, buzzer, coil and core, compass, six meter positions, probes, fuse replacement, conventional/electron current, eight editable setups, four local save slots and confirmed clearing. Saves never leave the device.

Source: [src.html](src.html). Offline instrument: [circuit-bench.html](circuit-bench.html). Notes, handoff, draft metadata, voice bank, audit states and empty painted-art manifest are present. The final file is **98,433 bytes (96.1 KiB)**, below both the 600 KB spec budget and 2 MB goal. No commits, deployment or polish round.

Unattended decisions: keep the requested E12 resistance range, which has 49 positions rather than the inconsistent 61; defer the schematic and generator as the spec leans; implement a quiet 2.4 kHz buzzer; use code drawing throughout. The Curiosity brief wins over the spec's automatic event narration. The report is deliberately the final artifact written, respecting the requested stop condition.

#### The real material

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

#### Break the instrument

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

#### Voice walk

Bank: calm-professor / Schedar. No recordings were made, as instructed; Curio.voice uses the browser fallback. Dynamic values are available through Read and the meter's polite live region.

The [615.4-second interaction walk](../../_scratch/circuit-bench/walk-results.json) logged the initial hint once and two explicit Read requests, with no runtime exceptions. Its network log contains only the local HTML file. All test Chrome instances were muted.

Automatic short and burnout speech from the spec was omitted because the Curiosity brief permits only the initial hint and subsequent Read. Those events remain visible and announced through the live status region. The initial hint disappears after a material action. A final targeted Manual/Close/Read walk verified that opening a drawer does not queue a stale wiring instruction behind it.

The audit's held-click, five-click and quick-tap checks completed without voice repetition or focus failures. Keyboard adjustment changed the battery to three cells, kept focus on Cells and announced “3 cells, 4.5 volts”; the unfolded tag title updated with it.

#### Short test

These are design judgments informed by a ten-minute automated interaction walk, not findings from child or adult participants.

- **Would a kid open it unassigned? Yes:** the waiting battery, bulb and loose jumper ends invite a direct physical action; closing the loop makes light without a page of instructions.
- **Would an adult play for fun? Yes:** measuring a circuit changes it, a spinning motor makes back voltage, and polarity and coil changes give further things to investigate. The notebook preserves experiments.
- **Is the real thing the interface? Yes:** terminal topology, component bodies, light, current, meter loading and magnetic response are the instrument. Readings are calculated, not preset outcomes.
- **Does it work without a score or finish? Yes:** any setup can be rewired or discarded; nothing grades it, unlocks it or ends it.

Compared with Elements Inspector, the bench is quieter when disconnected; that is an honest unpowered instrument. Its density comes from the board, physical parts and independent probes. I would keep using it to compare measurements and magnetic effects, with the declared DC-model limits in mind.

![Circuit Bench beside Elements Inspector](../../_scratch/circuit-bench/short-test-comparison.png)

#### Lesson creep check

[Search results](../../_scratch/circuit-bench/finish-results.json): no prohibited lesson language in voice lines. Four source hits are all “points”: one means physical measurement points; three refer to the coordinate array used to constrain body dragging. None means rewards. No score, goal, level, sticker, badge, quiz, finish screen, mode pills or kit header was built.

#### Done when

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

#### Audit leads

The single full audit completed: **147 leads**, with no runtime, focus, repeated-speech or stuck-resize failures. Its snapshot predates the final corrections. It was not rerun. Every lead has a disposition in [audit-dispositions.json](../../_scratch/circuit-bench/audit-dispositions.json); the [snapshot-to-final diff](../../_scratch/circuit-bench/after-audit.diff) is preserved.

- Fixed confirmed meter overlap at 1000x625 by using the compact dial selector at short heights.
- Fixed cramped tray labels; all twelve drawers fit at 680, 760 and 1000. The phone retains the explicitly requested horizontal parts strip, reachable by touch and Tab.
- Fixed hidden adjustment controls with a wrapped Adjust drawer; the phone frame and bounds show every control in view.
- Fixed phone engraving below 10 px, Manual/Notebook close-heading overlap and source-link hit areas. All three source links measure 44 px high.
- Canvas corner controls intentionally overlay the mat. Native drawers intentionally cover and inert the underlying bench. The initial hint intentionally vanishes after action; sources intentionally live at the end of a scrollable Manual.

The final targeted browser batches reported zero browser errors. Two host socket resets occurred as Chrome closed connections during test-server shutdown; they were not instrument exceptions. All Chrome ports 9980-9987 and host 8785 were subsequently verified closed.

#### Frames looked at

Inspected the four reference frames, four early frames, all functional and full-size frames, all 89 audit frames through twelve labelled contact sheets, four ten-minute walk frames, final compact/phone adjustments, source links, keyboard focus, current arrows, geometry extremes, drawer/body drags and the side-by-side comparison. Confirmed issues were also inspected at full size.

Evidence directories: references/, early/, functional/, final/, audit/, post/, last/ and drag-parts/ under _scratch/circuit-bench/. Validation scripts, input batches, numeric results, per-lead dispositions and artifact hashes are preserved there. The [validation manifest](../../_scratch/circuit-bench/validation-manifest.json) records the final executable artifacts and closed ports before this final report write.

#### Art made

Zero painted images and zero recorded audio. Breadboard holes, rails, labels, screws, filament, glass, polarity, resistor bands, motor flywheel, coil windings, compass, probe cables and tray miniatures are original canvas/SVG drawing. No image was needed or left as a placeholder. Original drawn materials and instrument colours follow the circuit spec, not the reference tools' palettes.

#### Engine changes wanted

None. Shared Motion, Sound, Read and tones were used without changing kit files.

#### Left open

- Physical Chromebook speed and an actual child/adult usability study remain unmeasured. The desktop benchmark and short-test judgments are explicitly limited above.
- Coil external-field falloff, fixed Earth field, motor mechanical response, diode thresholds and damage timing are stated approximations. This is a DC instrument, not a transient or product-calibration model.
- Browser voice fallback is used; no Schedar recording was generated. Schematic view and generator remain deferred as specified.
- Procedural deviations: startup troubleshooting printed extra regular-brief sections, and two initial read attempts lacked an explicit command kill limit. They did not write artifacts; subsequent checks used explicit time limits. The Curiosity brief governed the actual implementation.
- No deployment or commits were made. No polish round was started.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: circuit-bench

#### Played
Cold grade-8 and adult-perspective play: loose leads, all eight setups, independent probes, drawers and running resize before reading the builder's report, handoff, notes or source. Best moment: closing a loop makes the actual solved circuit give light. This feels like a bench worth taking apart.

Short test, as reviewer judgments rather than a child/adult study:

| Question | Judgment |
|---|---|
| Would a kid open it unassigned? | Yes: physical leads and a waiting bulb invite action. |
| Would an adult play for fun? | Yes: meter loading, motor back voltage and rewiring have real depth. |
| Is the real thing the interface? | Yes: topology, current, light and magnetic response drive the display. |
| Does it work without a score or finish? | Yes: nothing grades, unlocks or ends exploration. |

![Circuit Bench beside Elements Inspector](../../_scratch/circuit-bench/review-short-test-comparison.png)

#### Findings fixed
- **Blocker, family:circuit, part tag:** potentiometer showed only one section's voltage and dissipation. It now reports outer A-B voltage, current at A and both sections' power. Endpoint and mid-wiper checks pass. Motor watts are explicitly input power.
- **Blocker, general, keyboard holds:** H or Space released after focus moved could leave a shaft/contact latched. Global key release clears the relevant holds; canvas/window blur also releases them. Reproduced before; both release checks pass afterward.
- **Should fix, general, notebook:** restore changed every saved SPDT switch to contact B. It now releases momentary push buttons while preserving switch positions.
- **Should fix, family:circuit, fuse cover:** loading a fresh setup reset the fuse electrically but left OPEN printed. Reset now synchronizes the cover with the circuit.
- **Should fix, general, Read:** selected probes were spoken as "undefined". Red probe and COM probe now have names. The first real wire drag also used to suppress the only welcome; it now speaks once while the second loose lead still needs connecting.
- **Should fix, general, save limits:** unlimited added wires could create a circuit that its own restore rejected above 150 wires. Addition now enforces the existing save limit with a plain status message; a maximum-size snapshot reopens.
- **Should fix, general, Manual/sources:** clarified vertical five-hole connectivity, Shift-drag versus new jumper, panning and power-tag meanings. Added named finite-solenoid and E12 references with current licences in the Manual and draft metadata.
- **Polish, family:circuit, flattest response:** series bulbs had the same pale filament colour as one bright bulb. Solved power now drives a distinct orange/yellow filament and 80 ms light response. Existing glass, metal, wiring and bench texture remain.
- **Should fix, general, 680x425 opening:** loose jumper tips were below the work window. Both tips are now visible in the opening window. Wiring removes the matching loose lead, so either connection order works. Real black-first drags at 1366 and red-first drags at 680 each lit a 0.29636 A loop; the phone tips are both in view and its first drag works.
- **Audit state correction:** the phone save-switch route now opens Adjust before Contact. Its former hidden-control click was an invalid test, not an instrument fault.

#### Findings left
No known implementation blocker or should-fix remains.
- **Validation limitation:** no physical school Chromebook was available; spec Done when 10's hardware 60 fps claim remains unverified. Desktop/model evidence is not a hardware certification.
- **Polish:** narration uses the kit's browser fallback; the named Schedar recordings are absent. No recording was generated in this review.

#### Break it
[Independent arithmetic](../../_scratch/circuit-bench/review-numbers.json), [47 current-source checks](../../_scratch/circuit-bench/review-vm-results.json), browser rechecks and held input cover:
- One bulb 0.29636 A and 2.91 V; series 0.22643 A; parallel source 0.58524 A. The small independent parallel difference is explicit wire topology.
- Protected LED 20.496 mA; all four colours; reverse dark; direct LED opens and can be replaced. Resistance 10 ohms/100 kilohms; wiper 0/50/100 percent; one/four cells, 9 V and reversal.
- Motor 0.150 A running, 1.282 A stalled in the push-button setup, then 0.150 A after release. The extra contact/wire resistance explains the difference from the bare-loop 1.293 A example.
- Coil 50/400 turns, core factor 100 and magnetic reversal. The 200-turn air-core formula independently gives 5.61985 mT/A.
- Meter OFF/V/mA/A/ohms/continuity; negative and floating probes; A-across-source 9.68 A; mA fuse opens; powered ohms LIVE; cold bulb 1.00 ohm; disconnected resistance OL.
- Rapid wiring, 150-wire save boundary, empty circuit and zoom endpoints stay finite. Keyboard alone placed a battery and bulb and wired a 0.29636 A loop. The phone saved and reopened all four slots with switch states [true, false]; Cancel preserved the four-part circuit and Clear retained all slots.
- Powered resize 1366 to 680 and back stayed responsive. Motion off produced identical canvas pixels 700 ms apart while current stayed 0.22643 A. Grayscale preserves shapes, polarity and readouts.
- No score, quiz or success meter exists to cheat. Lesson-creep search finds only physical measurement "points", "endpoints" and a coordinate array called points.

#### Voice walk
Sound on; real held input and about two-second action spacing. Final first-wire log contains the initial hint once. Read then speaks selected battery values, series-bulb values, "Red probe. Choose a board hole", "COM probe. Choose a board hole", and motor input/current context. Read still speaks with Sound off.

| Line kind | Expected | Observed |
|---|---|---|
| Initial wiring hint | Once on first eligible action | Once after first real drag |
| Context/value Read | Each explicit request | Five requests in the main walk |
| Automatic short/burn speech | Zero under the Curiosity brief | Zero; events remain visible/live-region status |

Evidence: [main voice walk](../../_scratch/circuit-bench/review-voice-walk.json), [fixed first drag](../../_scratch/circuit-bench/review-welcome.json), [focus-change/key-release check](../../_scratch/circuit-bench/review-hold-release.json). Chrome was muted; logs verify dispatch and state agreement, not recording quality.

#### Facts checked
No external dataset, photograph, audio or source text was imported. References checked 2026-11-05; no sampling. [Source ledger](../../_scratch/circuit-bench/review-facts.json) records the exact routes and use.

| Fact/material | Named source and licence/use |
|---|---|
| Ohm, Kirchhoff, series/parallel, power and meter connections | OpenStax College Physics 2e 20.2-20.4 and 21.1-21.4, current CC BY-NC-SA 4.0, facts only; independently held to [MIT DC circuits](https://ocw.mit.edu/courses/8-02t-electricity-and-magnetism-spring-2005/01decae81aae80df6e65d8831582764a_chap7dc_circuits.pdf). |
| Hot filament resistance | [OpenStax 20.3](https://openstax.org/books/college-physics-2e/pages/20-3-resistance-and-resistivity), same licence; Rose-Hulman filament laboratory corroborates the temperature relationship. |
| Volts across, amps in line, fuse and unpowered resistance | [OpenStax 21.4](https://openstax.org/books/college-physics-2e/pages/21-4-dc-voltmeters-and-ammeters); [SparkFun Education](https://www.sparkfuneducation.com/how-to/multimeter.html) and [Fluke](https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-measure-resistance) corroborate. Manufacturer/tutorial content was not copied. |
| LED polarity and limiting resistor | Existing GSU HyperPhysics Diode citation is copyrighted and was inaccessible live; [CMU's LED experiment](https://courses.ideate.cmu.edu/99-355/s2016a4/text/ex/electronics/led-current-limiter/led-current-limiter.html) and [UCSB's LED demonstration](https://web.physics.ucsb.edu/~lecturedemonstrations/Composer/Pages/64.56.html) independently confirm directionality and reverse-dark behavior. Facts only, no source assets reused. |
| Wire field, coil, iron and finite centre field | OpenStax College Physics 22.2/22.9 and [University Physics 2, 12.6](https://openstax.org/books/university-physics-volume-2/pages/12-6-solenoids-and-toroids), current CC BY-NC-SA 4.0, facts only; MIT lecture 13 corroborates the finite formula; NASA corroborates current/compass response. |
| Motor back voltage and stall current | [OpenStax 23.6](https://openstax.org/books/college-physics-2e/pages/23-6-back-emf), same licence; Texas Instruments SSZTBP2 corroborates proportional back EMF and zero at stall. No manufacturer material bundled. |
| E12 values and 49 settings | [Vishay document 31001](https://www.vishay.com/docs/31001/dectable.pdf), copyright Vishay, facts only. Four decades of twelve intervals plus the endpoint is 49; the spec's 61 is inconsistent with its stated range. |
| Earth-field context | [NOAA/BGS WMM](https://www.ncei.noaa.gov/products/world-magnetic-model), public US government information; no coefficients or WMM implementation. Fixed northward 20 microtesla is a declared design value. |
| Every battery, bulb, LED, resistor, motor, coil, buzzer and meter constant | [Curio Class's Circuit Bench spec](spec.md) and declared model assumptions, recomputed rather than represented as measured product data. Includes capacities/runtime, thermal/damage timing, core factor and local external-field approximation. Original code MIT; original text/graphics CC BY 4.0. |

#### Sensitivity
None: a physical electronics bench with no people imagery, bodies, cultural representation, religious content or hard-history narrative. Oersted is a setup name; no new historical claim was added.

#### Flattest moment left
An unpowered or open circuit is quiet. That remains honest instrument behavior; live measurements, warm filaments and freely editable setups supply the response when the circuit changes.

#### Graphics
Original canvas/SVG parts, breadboard, glass, copper, resistor bands, motor, compass and probes inspected at final sizes. No painted assets added or removed. All 94 audit PNGs were inspected through eight contact sheets; phone drawers and opening, small preview and changed states also at full size. Final bundle 100,264 bytes. Comparison above shows the material-driven density beside Elements Inspector.

#### Audit
The single [full audit](../../_scratch/circuit-bench/review-audit/audit.md) finished within its 40-minute limit with **133 leads**. No runtime exceptions, stuck resize controls, repeated-speech or keyboard-focus failures were reported. [Every lead has a disposition](../../_scratch/circuit-bench/review-audit-dispositions.json): intentional canvas overlays, modal coverage, vanished first-run hints, a scrollable Manual source index and padded title boxes account for the visual flags. Manual/Notebook intentionally hush the initial wiring welcome. The hidden phone Contact click was corrected in the test state.

The audit was not rerun. Its small-preview frame exposed the clipped loose tips; the final opening and corrected phone save route were rechecked with native input afterward. All four slots and clear/cancel passed. The source-to-final [diff](../../_scratch/circuit-bench/review-changes.diff) and final [validation manifest](../../_scratch/circuit-bench/review-validation.json) are preserved. The phone wrapper logged two favicon 404 responses; these came from the test host, not instrument code or outside-data requests.
The unchanged checker definitions pass on a scratch metadata mirror, without its entry point. [Contract result](../../_scratch/circuit-bench/review-contract.json). Final targeted batches have no instrument console exceptions. Initial browser timeouts were retried in smaller batches; test-harness encoding/focus-event mistakes were corrected and distinguished from instrument faults.

#### Left open
- Physical Chromebook performance and actual child/adult usability testing remain unmeasured; the short-test answers are review judgments.
- The declared DC/thermal/magnetic approximations remain; no schematic view or generator was added. E12 range, quiet 2.4 kHz buzzer and Read-only later speech follow the brief/spec lean without asking an unattended user.
- **Scope breach:** importing the repository checker unexpectedly ran its top-level global bundler and regenerated other tools' generated HTML. I stopped it. No other tool source was intentionally edited, and I did not attempt a shared-workspace rollback. Subsequent validation extracted definitions without the entry point. The first read/memory lookup also lacked an explicit kill limit; later commands were bounded.
- No git commits or deployment. Review consists of one cold pass, fixes and scoped rechecks. All owned review Chrome/server sessions were closed; ports 9930 to 9937 and 8735 were verified closed.

<!-- end part -->

## Refine

<!-- part: refine.md -->

PASS (exit check 2026-11-06)
Counts: blockers 2 (general 1, family 1), should fix 17 (general 11, family 6), polish accepted 17

### Refine: circuit-bench

Lens files: `refine/teaching.md`, `refine/play.md`, `refine/craft.md`. No sensitivity review needed (all three lenses
agree: nothing cultural, Native or hard-history). Frames below are under `S:/CurioClass-codex-scratch/circuit-bench/`
(`teaching/f/`, `play/f1` to `f6`, `craft/`, `audit-r1/`). The circuit side is strong: every checked number matches the
spec (0.296 A one bulb, 0.226 A series, 20.5 mA LED, 1.28 A stall, 9.68 A short). The magnet side is where the work is.

#### Blocker
1. **Coil + compass: the needle is pinned at 90 degrees, and beside the coil it points the wrong way.** src.html:561
   (coil centre field) and 582-585 (compassFields, coil branch); starter loadSetup n===6 (src.html:1052-1058). The
   coil's external field is the centre field divided by 1 + (d / 2 cm)^3, about 2.7 to 3.9 mT at the compass against
   Earth's 20 uT, so the needle reads 88 to 90 degrees at 50, 100, 200 and 400 turns and 90.0 with the core; at the
   board's far corner it is still 82 to 90 (teaching t16, t24; play f3/30-coil.png, f3/31-coil-iron.png,
   f4/42-coil-far-50.png, f4/43-coil-far-50-iron.png). The field also always points along the coil axis, so a compass
   beside the coil swings the same way as one on the axis, which is backwards for a real coil (teaching t24). Only the
   mT label moves; the needle, the one thing that shows a force, does not. Why a blocker: MS-PS2-3 is the anchor code
   and spec Things to do 10 ("watch the field readout and the needle grow") is its only activity; BASELINE rule 2 says
   the anchor must be really taught, CODEX-CURIOSITY's short test asks that the real thing be the interface, and REFINE
   makes a readout that misleads a blocker. Fixed looks like: a dipole far field (moment N I pi r^2, times 100 with the
   core; radial and axial parts, so the field beside the coil runs back the other way), and a starter whose compass sits
   where 50 turns gives roughly 20 to 40 degrees, so each turns step, the core and the cell count visibly swing the
   needle and reversing the battery swings it across north. Add a slide switch to the starter so closing it swings the
   needle. Update the Manual's honesty note on the coil field to say what the model now does. (family:curiosity)
2. **Oersted wire: the needle swings 4 degrees, and the wrong way for what the student sees.** src.html:586-596
   (Biot-Savart with rz = -0.01, compass 1 cm BELOW the wire) against draw order src.html:1801-1802 (wires drawn
   first, the compass disc drawn on top, so the picture says the compass sits ABOVE the wire); starter loadSetup
   n===5 (src.html:1043-1051). In the starter the compass sits between the outgoing and return leads, which run on
   the diagonal and mostly cancel: +4.3 degrees closed, -3.8 reversed, 4.4 at the best hole (teaching t15, t15b, t21;
   play f4/40-oersted-on, f4/41-oersted-reversed). The spec's checked case (0.3 A at 1 cm, about 17 degrees) is never
   staged; a north-south wire gives 11 (teaching t23). A student checking with the right-hand rule or a real compass on
   a real wire gets the opposite swing. Done when 4 passes only on the letter. Fixed looks like: the geometry and the
   picture agree (compute for the compass above the wire, or draw jumpers arching over the compass and say "under" in
   the Manual; pick one and make the Manual match); the starter runs one straight jumper north-south across the compass
   with the return path routed far away, so closing the switch gives a clear swing near the spec's 17 degrees and
   reversing the battery swings it as far the other way. Add a "Things people have found" entry: a wire lined up with
   the needle swings it most; one across it barely moves it. (general)

#### Should fix
1. **The short and burnout event lines are never spoken, and the events make no sound.** src.html:296-297 (L.short,
   L.burn), 565-570 (burn() sends L.burn only to status()); grep for `V.say` finds no hits. A short sets no status at
   all. Seen by Play (voice log after a burn and a short) and Craft (`results.json` voice run: 0 of 1 for each). The
   spec's Voice section says both are spoken every time. Fixed: queue both as event lines each time (not once-only),
   plus a short pop on a burn and a crackle while a short lasts, Sound on only. (general)
2. **A part that burns while selected keeps a stale tag with no Replace, and the line names the wrong move.**
   src.html:565 (burn() never calls showControls()). The tag reads "Red LED · × OPEN" but still offers Red, Turn LED,
   Move, Turn, Remove, and `#replace-part` is absent (craft `voice-burned-led-1366.png`). Fixed: rebuild the tag on
   burn so Replace shows; and keep the spec's line "Tap it to replace it." true by making a tap on a burned part
   replace it (see Settled calls). (family:curiosity)
3. **Motor + push button starter: one pointer cannot stall the motor.** loadSetup n===7 (src.html:1059-1065); the
   tag's hold control (src.html:773-775) and the canvas shaft hold (1230, 1275) only stall while held. The motor turns
   only while the button is held, so a mouse or one finger cannot also hold the shaft; Play needed Space plus a mouse
   hold (play f3/26-motor-running.png, f3/27-motor-stalled.png). Things to do 8 fails for a solo student (rule 4).
   Fixed: make the tag's "Hold shaft · H" a latch (press to grab, press again to let go, aria-pressed and a visible
   state), keeping press-and-hold on the shaft itself. Keep the push-button starter. (general)
4. **The ammeter shows "- -" in a complete loop that carries no current.** src.html:617 (`connected()` false for a
   blocked or open loop). With mA in the gap of the reversed-LED loop the LCD shows "- -" while the tag says 0.00 A
   (teaching t20); the same with any open switch in series. The Manual defines "- -" as a floating probe. Done when 4
   wants 0 mA. Fixed: in A and mA, show 0.00 when both probes sit on nodes of the board; keep "- -" for a probe in an
   empty hole or off the board. (general)
5. **The short chip covers the glowing wire.** src.html:1768-1770 (chip 47 px below the battery). A short wire laid
   next to the pack, the obvious place, sits under "Short: 9.7 A" (play f3/z25.png); the probe labels also land on it
   (craft `voice-short-chip-1366.png`). Things to do 11 is "see the wire glow red". Fixed: place the chip clear of
   every wire and probe (above the pack or to the free side). (general)
6. **The 9 V battery reads "9AAV".** src.html:1634: the cell loop draws "+" and "AA" for the single 9 V cell, then
   "9 V" on top (play f3/z20.png; craft `zoom-9v.png`). Fixed: skip the AA cell drawing for the 9 V pack and draw a
   9 V battery body with its snap terminals. (family:curiosity)
7. **Every label printed on a part has a ghost copy.** src.html:1620-1622: shadowOffsetY 4 stays set while part text
   is drawn, so "3 V · 0.3 A", "2 × 1.5 V", "RED" and the live rpm and mT readouts are doubled (play
   f1/zoom-04-lit.png; craft `zoom-labels.png`, `zoom-calm-arrows.png`). Fixed: reset shadow (colour transparent,
   offset 0, blur 0) before any text. (family:curiosity)
8. **The mA range blows on every bulb circuit and the screen does not say why.** Fuse check in simulate(); status
   "Meter fuse open." A bulb draws 0.23 to 0.30 A plus cold inrush, over the 200 mA fuse, so Things to do 3 on mA with
   any bulb starter always ends in FUSE (play f2/11-mA-in-line.png). Honest, but a solo student is stuck. Fixed: the
   status says the rule where it happens, for example "Fuse open: over 200 mA. Use A for bulbs." and the Manual's
   meter section says the same. (general)
9. **The coil is 4 ohm at every turn count, with no word about it.** src.html:512; Manual line 235. Going 50 to 400
   turns multiplies the field at the same 0.694 A (teaching t16), so a student may conclude "more turns, stronger" at
   the same battery, which a real coil wound from the same wire does not give. Fixed: one honesty line in the Manual
   ("every coil here is 4 ohm, as if wound with thicker wire as turns rise; a real coil from the same wire gains
   resistance with its turns"). Scaling R with turns is a spec change: see open questions. (family:curiosity)
10. **No real-world safety line about shorts.** Manual lines 217-222; notes.md. The tool invites a student to short a
    battery and shows nothing bad happening; a grade 3 to 8 student alone at home can try it with real cells and a
    paper clip. Fixed: one plain line in the Manual's meter section and in teacher notes: "On a real bench a short
    heats the wire fast and can burn you; never short a real battery, and never use mains power." Teacher notes add
    that the bench is for battery-level DC only. (general)
11. **Motion and Sound show on or off by shade alone.** src.html:15, 158. Both buttons keep the same words; the pressed
    fill differs by 1.07 to 1.61:1 (craft `zoom-power-on.png`, `zoom-power-off.png`). Color is the only signal, and
    the look rule asks for toggle switches. Fixed: drawn toggles with an ON/OFF legend or a lit pilot lamp plus the
    word. (family:curiosity)
12. **Focus on the breadboard has no visible outline.** src.html:16, 28: `.board-wrap { overflow:hidden }` clips the
    canvas's focus-visible outline (craft `focus-4tabs-1366.png`). Fixed: draw the focus ring inside the canvas or on
    the wrapper. (general)
13. **The focus ring vanishes on paper surfaces.** src.html:16: #ffda73 is 1.03 to 1.2:1 on the tag, Manual, Notebook
    and board papers (craft `zoom-focus-hold.png`, audit `state-part-tag-680x425.png`). Fixed: a dark ring (for example
    #1a1f17 with a light inner ring) inside paper areas; measure and record it in notes.md. (general)
14. **Read speaks symbols and run-on text.** src.html:328-331. Logged: "Meter on OFF. OFF.", "Bulb. 2.81 V · 293 mA ·
    823 mW Meter on volts. 2.81 V.", "... Meter on milliamps. FUSE." (craft read run; play s4 voice log). Fixed: a
    spoken formatter (volts, milliamps, milliwatts, ohms, kilohms, "no reading" for "- -", "fuse open"), a full stop
    before "Meter", and "Meter off." The spec's own example is "Meter on volts. 2.94 volts." (general)
15. **A parts drawer stays pressed after its tool is used up.** src.html:383, 1166: pickTool sets aria-pressed but
    placeAt and select never clear it (craft `kb-probe-focus-1366.png`). Fixed: clear the pressed state whenever the
    tool is cleared. (general)
16. **The draw loop never rests, and 30 parts drop well below 60 fps on a slow machine.** src.html:1814-1840;
    `circuitDirty` is set in ten places but never read. At 4x CPU throttle: opening bench about 30 fps, 30 parts with
    five lit about 13 fps (craft `perf2.py`, `results.json`). Done when 10 asks for 60 fps with 30 parts. Fixed: cache
    the board (holes, rails, numbers) in an offscreen canvas, drop per-part shadowBlur, solve only when circuitDirty or
    a part is time-varying, skip the redraw when nothing moves; re-measure and record the numbers in notes.md.
    (general)
17. **The compact Adjust drawer hides what it adjusts.** src.html:888 and the `adjust-part` handler: below 1050 px the
    part controls open in a modal dialog over the board and tag (audit `state-part-tag-680x425.png`), so turning the
    resistor or pot hides the LED and the numbers. Things to do 6 is exactly that. Fixed: a non-modal tray that leaves
    the part and its tag values in view. (family:curiosity)

#### Polish accepted
1. **Lit bulb glow is a faint haze.** drawPart bulb case (halo alpha at most 0.5). Warm the glass fill with the glow,
   a stronger bloom at full power, a real dull-red stage at low power (play f1/zoom-04-lit.png). (general)
2. **Burnout has no moment.** burn(). A bright flash for a few frames, a wisp of smoke with Motion on, then the dark ×
   (the spec says "watch it flash and go dark"; play f3/22-led-burning-50ms.png, f6/63-bulb-burned.png). (general)
3. **Battery tag shows "-296 mA".** src.html:655. Show "supplies 296 mA" as the spec's battery tag reads; keep the sign
   for the meter (teaching t03; play f1/04-lit.png). (general)
4. **Restore the Manual's attributions.** Manual lines 249-256: the spec's short sources per "Things people have
   found" entry, including "as Hans Christian Oersted found in 1820", so the "Oersted wire" starter has its name
   explained. (family:curiosity)
5. **The opening jumpers look already plugged in.** reset() ends at e12 and f16. Lay the loose tips off the hole grid
   at an angle, or give them a visible open-end mark (play f1/zoom-01-open.png). Keep the hint text. (general)
6. **Nothing follows the pointer when dragging from a drawer.** Draw the part under the pointer while dragging (play
   f6/64-drawer-mid-drag.png). (general)
7. **Probe leads end in mid-air, and the dial has no legends.** src.html:1778 (drawProbes ends at x 965). Run the leads
   off the board edge to the meter's jacks; print OFF, V, mA, A, ohm and beep legends round the dial (play
   f2/10-volts-across-bulb.png; craft `calm-parallel-1366.png`). (family:curiosity)
8. **Numbers too small when projected at 1920x1080.** resize() caps the board at 1.25; tag values are about 12 px. Let
   the board grow with the screen and size tag values near the LCD's (audit `state-parallel-1920x1080.png`). (general)
9. **Short preview sizes crop the instrument.** At 680x425 the Notebook, zoom and centre buttons cover the top rail and
   columns 1 to 8; at 800x500 the motor starter's push button sits behind the meter. Keep board tools off the board at
   short heights and centre the view on a starter's parts when it loads (audit `size-680x425.png`,
   `state-motor-800x500.png`). (family:curiosity)
10. **The LCD live region chatters.** src.html:172: `#meter-reading` aria-live polite rewrites up to five times a
    second. Announce on settle (value steady about 1 s) or on Read. (general)
11. **Compass tag shows "0.00 V · 0.00 A · 0.00 W".** src.html:655. Show only the angle (teaching t15b). (general)
12. **Leakage shows up as readings.** "0.0360 μW" on an open pack, "0.0600 μV" on an idle resistor (the 1 nS leak).
    Show 0 below a floor on tags (play s3, s6 logs). (general)
13. **A turned LED draws "RED" upside down** ("038"). Keep part text upright at any rotation (play
    f3/21-led-reversed.png). (general)
14. **Both AA cells are drawn the same way up.** Alternate them as a real holder does (play f1/zoom-01-open.png).
    (general)
15. **Two honesty clauses.** Battery runtime: "real cells give less at high draw" (2000 mAh at 0.3 A gives 6 h 40
    min, generous for alkaline). Ohms on a diode: the 1 mA test source forces an LED on (2.01 kohm, teaching t19);
    say so in the honesty notes. (general)
16. **Ω reaches screen readers as a symbol.** The resistor's aria-valuetext "3.90 kΩ resistor": write "3.9 kilohm
    resistor". Share the formatter from should fix 14. (general)
17. **The top-left "CIRCUIT BENCH / DC · 2.54 mm · NO. 07" repeats the plate.** src.html:156. Drop the name and
    number, keep "DC · 2.54 mm" if wanted (play and craft both noted it). (family:curiosity)

#### Settled calls
- **Magnetism as a blocker (Play and Teaching both raised it).** Teaching rated the coil and Oersted items should fix;
  Play said "mostly no" to "is the real thing the interface" for the magnet side. Settled as blockers under
  CODEX-CURIOSITY.md and REFINE: MS-PS2-3 is the anchor code, the needle is the instrument's only showing of a force,
  and today it is pinned (coil), points the wrong way beside a coil, and swings opposite to the drawn geometry
  (Oersted). Those are readouts that mislead, and the anchor standard is not really exercised. The fix is the real
  physics shown plainly, never a goal, target angle or challenge.
- **Welcome cut short by the first tap, or skipped when a drawer opens:** fine (BASELINE rule 16). The hint stays on
  the mat and Read speaks it. Do not change.
- **"Hint out of view" on every starter:** correct; loadSetup hides the hint after the first action, as the Curiosity
  brief asks. Do not change.
- **Manual, Notebook and part-tag drawers covering the bench, and the 375 drawer strip scrolling sideways:** by
  design (spec). Not findings. The compact Adjust drawer is different (should fix 17) because the student must watch
  the board while adjusting.
- **The burn line keeps the spec's wording** ("That part burned out. Tap it to replace it."). Craft suggested "Tap
  Replace on its tag."; settled by making a tap on a burned part replace it, so the spoken line is true and the voice
  bank stays as specced.
- **Motor stall:** fixed by a latching tag control, not by changing the starter's push button to a slide switch (the
  spec lists "motor and push button" as the starter).
- **Do not add** a target angle, a "make the needle reach X" prompt, or any score or finish while fixing the magnet
  side. The circuit solver and its numbers are verified; do not retune AA, bulb, LED or motor values.

#### To the spec's open questions
- **MS-PS2-5 is half exercised.** Only the magnetic field side (a compass moving with nothing touching it) is here; no
  electric field or charge. The spec says "in part". Integrator or Cory: confirm the module's lesson tool carries the
  electric half, or the code's claim on this module rests on the lesson tool alone (BASELINE rule 2).
- **Also-reaches overclaim.** science-3-magnets-and-static-electricity (3-PS2-3, 3-PS2-4) has no static electricity
  and no magnet-to-magnet force; science-11 HS-PS2-5 has only the current-makes-a-field half (no generator, by the
  spec's own open question). Suggest listing both as "touches", not reaches. Grade 4 (4-PS3-2) is genuinely exercised
  by the bulb, buzzer, motor and hot wire.
- **Scale coil resistance with turns?** It would show the real trade-off (more turns, less current on the same
  battery) as MS-PS2-3 data, but changes the spec's model values. Lean: yes, after the blocker fix lands.

#### Not taken
- Changing the first-run hint to "Drag each loose wire end to a bulb leg." (Play): the hint is a spec voice line;
  polish 5 fixes the look that caused the doubt.
- Replacing the motor starter's push button with a slide switch (Play): settled by the latching hold instead.

#### Exit check (2026-11-06)

Claude, cold exit check on the bundle `circuit-bench.html` (version circuit-bench-fix-1, 118,824 bytes). Frames and JSON
under `S:/CurioClass-codex-scratch/circuit-bench/exit/` (`f/` for drive.py shots s1 to s15, `audit-r2/` for the audit,
`perf.py` and `perf_noshort.py` for the craft lens's 30-part build re-run). Chrome 9701, host 8911. Note: my first
timing checks shared Chrome 9701 with the running audit and gave throttled background-tab results; every timing number
below was re-run with the audit finished.

##### Blockers
1. **Coil + compass: FIXED.** Coil starter (50 turns, switch closed) re-solved at each step: 50/100/200/400 turns give
   28.4/46.9/64.6/76.3 degrees; core 88.1; 1 to 4 cells 15.7/28.4/37.9/45.0; battery reversed -29.0; switch open 0.00;
   closed again 28.4 (f/coil.png, s2 result). Moving the compass beside the coil (above its middle) gives -83.9 against
   +28.4 on the axis, so the side field runs back the other way. compassFields (src.html:717-728) is the dipole formula
   B = mu0/(4 pi r^3)[3(m.r)r - m], checked by hand. Manual line 312 names the dipole model; line 302 the 4 ohm note.
2. **Oersted wire: FIXED.** Starter: closed -13.71, reversed +13.79, open 0, closed again -13.71 (s2). Hand check of
   src.html:730-739: dl x r with the compass 1 cm above the wire; current runs rail 0 to rail 13 (south on screen,
   0.296 A), so the field above points west and the needle swings west (negative). Picture and maths agree: the
   compass is drawn over the jumper (f/oersted.png) and the Manual says above. "Things people have found" has the
   alignment entry (src.html:323).

##### Should fix
1. **Short and burn spoken: FIXED.** After a real first tap: burn logged "burn:spoken", a separate short logged
   "short:spoken", status "That is a short circuit." (s5, s7). Event lines are not once-only (V.say kind event).
2. **Burned tag and tap-to-replace: FIXED.** Selected LED burns, tag rebuilds to "Red LED · × OPEN" with Replace first
   (s5). A real tap on the burned LED body (with its supply removed) replaced it: burned false (s7 burn-tap2).
3. **Motor latch: FIXED.** Real click on #hold-part: aria-pressed true, text "Release shaft · H", 1.282 A with the
   button closed; second click releases to 0.150 A (s3 motor-latch).
4. **Ammeter zero in a blocked loop: FIXED.** Reversed LED loop broken and bridged by the probes: 0.00 on mA and A
   (real clicks on the range buttons); probe moved to an empty hole: "- -" (s9). Nit, not counted: the mA range shows
   "0.00 A" and A shows "-296 mA" (auto-ranged units), fine for a 1999-count meter.
5. **Short chip clear of wires: FIXED, with a regression.** The chip sits above the pack, clear of the wires
   (f/short-chip.png). But drawShortChips (src.html:2068-2085) rebuilds every obstacle and re-runs clearance() inside the
   sort comparator for 208 candidates, every frame, while a short lasts. See Regressions.
6. **9 V body: FIXED.** f/nine-volt-led.png: one "9 V" body with snaps, no AA drawing.
7. **Ghost labels: FIXED.** Labels sharp in f/adjust-680.png and f/nine-volt-led.png ("330 Ω", "RED", "9 V").
8. **Fuse explains itself: FIXED.** One bulb, probes across a real gap, real mA click: LCD "FUSE", status "Fuse open:
   over 200 mA. Use A for bulbs.", fuse cover "FUSE OPEN · tap to replace"; A then reads 296 mA (s9). Manual line 284.
9. **4 ohm coil honesty: FIXED.** Manual line 302.
10. **Safety line: FIXED.** Manual line 287; notes.md lines 49-50 (battery-level DC only).
11. **Motion and Sound toggles: FIXED.** Real clicks: "Motion OFF" / "Sound OFF" words, aria-label, and the drawn
    switch flips (f/z-toggles-focus.png).
12. **Board focus: FIXED.** Four Tabs land on #board; the inset ring shows (f/z-toggles-focus.png).
13. **Paper focus ring: FIXED.** Focused "Reverse · F" on the tag: outline rgb(26,31,23) 3 px plus a 5 px light rim,
    clearly visible (f/z-paper-focus.png); ratios recorded in notes.md line 60.
14. **Read formatter: FIXED.** Held Read: "Bulb. 2.91 volts , 296 milliamps , 861 milliwatts. Meter on volts. 2.91
    volts."; with the meter off: "... Meter off." (s3). Nit, not counted: the logged text has a space before each comma.
15. **Drawer pressed state: FIXED.** Real click on the Resistor drawer, real tap on the board: part placed, no drawer
    left pressed (s10).
16. **60 fps with 30 parts: PARTLY FIXED.** The craft lens's own 30-part build (5 lit) with its two accidental shorts
    removed (its 9 V packs sat on one rail): 16.67 ms frames at 1x (0.3 ms work) and 17.0 ms at 4x CPU throttle
    (1.3 ms work), so the ordinary bench now meets the bar, better than polish.md claimed. With a short on the bench it
    does not: one short on that 30-part, 17-wire board gives 25.4 ms per draw and 29.5 ms frames (about 34 fps) on this
    desktop; the original build with two shorts gives 46 to 51 ms draws (about 18 to 20 fps) at 1x and 263 ms at 4x
    (perf.py output). Cost grows with wires times candidates, so a busier mat is worse. Things to do 11 is "make a
    short", so this is on the main path.
17. **Compact Adjust: FIXED.** 680x425, resistor Adjust: the tray is non-modal (`:modal` false), sits under the tag,
    and the resistor, LED glow and the 20.5 mA values stay in view (f/adjust-680.png).

**Of 19 blocker and should-fix items: 17 fixed, should fix 16 partly, and should fix 5 fixed but carrying the
regression below.**

##### Polish (spot-checked in bulk, never blocking)
Seen fixed: battery tag "supplies" (3), AA cells alternate (14), top-left reads only "DC · 2.54 mm" (17), opening
jumper tips sit off the grid with open-end rings (5), dial legends and probe jacks (7), warmer bulb glow (1), compass on
the starters shows its angle (11). Taken from polish.md, not re-checked: smoke and flash timing (2), drag ghost (6),
1920 tag size (8), live-region settle (10), kilohm aria-valuetext (16).

##### Regressions
- **Short chip search per frame (from should fix 5).** drawShortChips recomputes all obstacles and calls clearance()
  twice per sort comparison, about 1.5 million distance checks per short per frame on a 17-wire mat. Narrow fix:
  compute the chip spot once when a short starts (and again only when wires or probes change), score each candidate
  once before sorting, and keep the result in p.chip. Then re-measure s15 (one short, 30 parts) and the perf.py build.
- Default screen, every starter, Manual, Notebook and calm frames at 1366x768 (audit-r2 state-*.png,
  f/z-states.png): no other regressions. Coil starter shows the needle at 28 degrees; Oersted at -14.
- No console errors in any shot or in the audit; resized mid-action clean; Motion off: nothing runs forever.

##### Gate
1. Done when: 1 to 9 pass in my checks or the audit (4 now real: 0 mA on the reversed LED, the needle crosses north on
   reversal; 5 at 1.28 A / 0.15 A; 6 chip and fuse). 10 partly: one file, no network requests (only the file itself
   loaded), no em dashes, but not 60 fps while a short is on a busy mat. 11 and 12 hold (no score, goal or finish).
2. Codes: MS-PS2-3 is now really exercised (needle swings with turns, core, cells and direction). Open for the
   integrator, carried from the merged list: the written call on MS-PS2-5 (only the magnetic half here) and listing
   3-PS2-3, 3-PS2-4 and HS-PS2-5 as "touches". Not a tool fix, but rule 2 wants it written before PASS.
3. Solo defaults: hold for one pointer now (motor latch, fuse message, tap-to-replace).
4. Sensitivity: not needed (all three lenses agree).
5. Blockers and should-fix: one open (should fix 16 under a short, caused by the should fix 5 change).
6. Bundle: 118,824 bytes, far under 2 MB; no console errors; no network requests.
7. Voice: hint once on the first tap (audit), Read speaks the hint plus the formatted meter, burn and short spoken each
   time as events, Sound off silent per polish.md; voice/lines.json holds the same three lines as L.

#### Audit pilot
- Leads confirmed: none that are findings. The overlap rows (board tools, cursor label and hint over the board) are by
  design; the Manual and Notebook "keep region" and hidden-text rows are the modal drawers, settled as by design;
  "hint out of view" on starters is settled; the 375 drawer strip scrolling sideways is settled.
- Leads wrong: "welcome not heard" after a first tap on Notebook or Manual: a Curiosity has no welcome, only the hint,
  which is shown on the mat and spoken on Read (settled call).
- What it missed: the short-chip frame cost (it never builds a short on a busy board and measures no frame times), and
  every physics readout (the needle numbers needed drive.py and src.html).

#### Integrator call (2026-11-06, BASELINE rule 2)
Settled in spec.md Map: MS-PS2-5 stays on the anchor as "in part" (magnetic half only; the electric half rests on the
module's lesson tool). 3-PS2-3, 3-PS2-4 and HS-PS2-5 move to "touches", not claimed. Codex: make tool.draft.json and
any notes match spec.md Map (claimed codes MS-PS2-3, MS-PS2-5 in part, 4-PS3-2, 4-PS3-4). The only tool fix left is
should fix 16: work out each short chip's spot once per short (or when wires change), not every frame.

#### Exit check (2026-11-06)

Round 2 re-check (Claude, cold). Bundle circuit-bench.html, version circuit-bench-fix-2, 119,919 bytes. Scope: the two
items the first exit check left open (should fix 16 and its should fix 5 regression; the integrator's standards call),
plus a no-regression look at the frames they touch. Frames and JSON under
`S:/CurioClass-codex-scratch/circuit-bench/exit2/` (`audit-r2/` audit, `perf*.py` and `*.out.json` timing on the same
30-part fixtures as the first exit check, `inval-1366.png`, `contact-1366.png`). Chrome 9310, host 8310, both closed.

##### Blockers
1. Coil + compass: FIXED (first exit check). Coil starter frame re-seen: needle off north, 0.97 mT, 50 turns. Polish.md
   re-measured 28.37 to 76.26 degrees across turns, matching the first exit check; no magnetic code changed.
2. Oersted wire: FIXED (first exit check). Starter frame re-seen, compass over the jumper.

##### Should fix
1 to 4, 6 to 15, 17: FIXED (first exit check), unchanged code; spot-seen in the audit frames (9 V body, burn wording in
lines.json, toggles, Read logs "Drag a wire from the battery to the bulb. Meter off.").
5. Short chip clear of wires: FIXED, regression gone. drawShortChips (src.html:2071-2129) now samples obstacles once
   per wire/probe key and keeps each chip in a WeakMap keyed on that key and the source centre. Live: one short gave
   one layout, 60 explicit redraws plus 4 s of animation kept it at 1; adding a wire made exactly one new layout; the
   chip sits clear on the top strip (x300 y52, 47 px clearance; perf-1short-30parts-1366.png, perf2-30parts-lit-1366.png);
   removing the shorted pack with the real Remove button cleared the chip and the short (inval-1366.png).
16. 60 fps with 30 parts: FIXED. Same fixtures as the first exit check, 1366x768, 16 wires, 5 lit:
    | case | 1x frame / work | 4x frame avg, p50 / work |
    |---|---|---|
    | no short | 16.67 / 0.32 ms | 17.4, 16.7 / 1.47 ms |
    | one short | 16.67 / 0.41 ms | 17.7, 16.7 / 1.97 ms |
    | two shorts | 16.67 / 0.41 ms | 18.2, 16.7 / 1.98 ms |
    (Before: one short 29.5 ms frames at 1x, two shorts 263 ms draws at 4x.) A short now costs about 0.5 ms of work
    at 4x, and every case matches the no-short control the first exit check accepted. The occasional 33 ms frames at
    4x come with the software rasteriser (--disable-gpu); script work stays near 2 ms of a 16.7 ms budget.
    Polish.md's 38.75 fps no-short 4x control did not reproduce here (likely a contended or background tab); its
    "not fixed" was over-cautious.

**Of 19 blocker and should-fix items: 19 fixed.**

##### Integrator call (standards)
Applied: tool.draft.json standards MS-PS2-3, MS-PS2-5 (standards_scope: in part, magnetic half), 4-PS3-2, 4-PS3-4;
3-PS2-3, 3-PS2-4, HS-PS2-5 listed as touches_not_claimed; notes.md line 30 says the same as spec.md Map.

##### Polish (spot-checked in bulk, never blocking)
Unchanged since the first exit check; seen again in the audit frames: AA polarity, open-end rings, top-left label,
maker plate, warm bulbs. Known, not done (polish.md Left open): at 680x425 the AA battery Adjust tray puts Turn and
Remove in horizontal overflow (cell count and Reverse stay visible).

##### Regressions
None. Default, all eight starters and the Manual at 1366x768 (contact-1366.png) match the first exit check. Motion
off: nothing runs forever. Resized mid-action: clean. 36 held clicks, five-click and quick-tap rows: no errors,
focus kept. No console errors and only the file itself loaded in every timing and invalidation run.

##### Gate
1. Done when: 1 to 12 pass; 10 now holds under a short too (one file, no network, no em dashes, 60 fps bar met as
   the no-short bench was).
2. Codes: MS-PS2-3 exercised; MS-PS2-5 in part and the touches written in spec.md Map, tool.draft.json and notes.md.
3. Solo defaults: hold (first exit check; nothing touched).
4. Sensitivity: not needed (all three lenses agree).
5. Blockers and should-fix: none open.
6. Bundle: 119,919 bytes, far under 2 MB; no console errors; no network requests.
7. Voice: hint heard once on the first tap (audit rows 0, 3, 5 to 34), Read speaks hint plus meter, Sound off silent;
   voice/lines.json holds the same three lines as L (polish.md allLines check). Event narration code unchanged.

#### Audit pilot
- Leads confirmed: none that are findings. All 112 leads are the settled categories (board overlays, modal Manual
  and Notebook coverage, hint hidden on starters, phone strip scroll).
- Leads wrong: "welcome not heard" after a first tap on Notebook or Manual; a Curiosity has no welcome (settled).
- What it missed: frame cost with a short on a busy mat, and the chip layout count; both needed the perf fixtures.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: circuit-bench (Curiosity No. 07), round 1

Bundle looked at: `tools/circuit-bench/circuit-bench.html` as built (not re-bundled). Shared audit:
`S:/CurioClass-codex-scratch/circuit-bench/audit-r1/audit.md`. My frames and check script are in
`S:/CurioClass-codex-scratch/circuit-bench/craft/` (`craft_checks.py`, `perf2.py`, `results.json`, `*.png`).

#### Contract and look rules (passed)

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

#### Findings

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

#### Standard voice check

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

#### Audit pilot

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

<!-- end part -->

<!-- part: refine/play.md -->

### Refine, Play lens: circuit-bench (Curiosity No. 07)

Cold lens, round 1, 2026-11-05. Judged against CODEX-CURIOSITY.md and VISION.md "Curiosities: the second shape".
Played at 1366x768 with real held clicks and jittered drags in one muted headless tab per session (my driver:
`S:/CurioClass-codex-scratch/circuit-bench/play/play.py`, sessions s1 to s6, frames in `play/f1` to `play/f6`), once
as a grade 8 student alone at home, once as a teacher projecting at 1920x1080. Shared audit:
`S:/CurioClass-codex-scratch/circuit-bench/audit-r1`.

#### Short test

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

#### Findings

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

#### Audit pilot

- **Confirmed:** 680x425 button row over the board's top rail (finding 16). The 375 drawer strip scrolls sideways,
  as the spec asks; a cut drawer shows at the edge as a cue, so not a finding.
- **Wrong:** "hint out of view" on every notebook state: the hint is correctly gone after the student's first
  action. Manual, notebook and part-tag "text hidden" rows: those are modal drawers over the bench, as designed.
  "Close overlaps title" at 375: no collision on state-manual-375x812.png. "Welcome not heard" after Notebook or
  Manual: opening a drawer hushes it, the hint stays on the mat and Read speaks it (BASELINE rule 16), not a finding.
- **Missed:** everything that needs the physics to run: both magnet starters showing almost nothing on the needle,
  the motor stall needing two holds, the silent short and burnout (a line defined and never used), the chip over the
  shorted wire, the "9AAV" label, the fuse that blows on every bulb, the weak glow and the doubled canvas labels.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: circuit-bench (Curiosity No. 07), round 1

Judged as a Curiosity (CODEX-CURIOSITY.md, VISION "Curiosities: the second shape"). I did not read codex-report,
codex-review or handoff. Frames: `S:/CurioClass-codex-scratch/circuit-bench/teaching/f/` (t01 to t31). Every number
below came from the running bundle (drive.py, port 9771). I recomputed each one in Python as well.

#### What holds (checked, no finding)

- The circuit physics matches the spec's checked values and my own recompute:
  - one bulb: 296 mA in line, 2.91 V across it (t10);
  - two bulbs in series: 226 mA in all three gaps, 1.46 V + 1.46 V = 2.93 V (t11);
  - two bulbs in parallel: 0.585 A from the battery (t12);
  - red LED + 330 ohm on 9 V: 20.5 mA (t13);
  - red LED straight on 2 x AA: 97 mA, burns, then a Replace button appears (t14);
  - motor: 11,500 rpm and 0.150 A running, 1.28 A when held, back to 0.150 A when let go (t17);
  - A range across 2 x AA: 9.68 A with "Short: 9.7 A". On mA the fuse opens and can be replaced (t18);
  - bulb resistance: 1.00 ohm cold, 2.91 V / 0.296 A = 9.8 ohm hot, ohms mode says LIVE on a powered bulb (t19);
  - coil: 5.62 mT per amp at 200 turns. The solver, meter ranges and E12 colour bands are right.
- Done when 1 (two jumpers light the bulb, t02/t03), 2, 3, 5, 6, 7 (keyboard place, wire and probe, t31),
  8 (Motion off shows still arrows and the glow, t30) and 12 (no score, goal, level or finish anywhere; the
  lesson-creep grep is clean) pass. Done when 9: cite the audit's size rows and frames; the board, drawers and
  meter are present at every size. Done when 10: Craft's job. Done when 11: not checked, by brief rule.
- No predict, quiz or hidden-information mode, so nothing can give an answer away.
- notes.md "What it teaches", "Key skills" and "A five-minute start" are true of this tool. The home ideas can be
  done tonight.
- Nothing cultural, Native or hard-history. No sensitivity review needed.

#### Fact spot-checks (second source, 2026-11-05)

1. OpenStax College Physics 2e licence is CC BY-NC-SA 4.0 (book page footer): matches. Section 21.3 is Kirchhoff's
   Rules, 21.4 is DC Voltmeters and Ammeters: matches the Manual's section list.
2. Finite-solenoid centre field: OpenStax UP2 eq. 12.27 at the midpoint gives mu0 N I / sqrt(L^2 + 4R^2), the same
   as the Manual's formula and the code.
3. Oersted, 1820, a compass needle near a wire; reversing the current reverses the swing (National MagLab, Linda
   Hall Library): matches the spec. (The Manual drops the name and date; see finding 10.)
4. Earth's horizontal field of about 20 uT for mid-latitude North America: a fair round value. I could not pin an
   exact US range from a second source; it is labelled a design value, so that is fine.
5. AA internal resistance: Energizer E91 sheet gives 150 to 300 milliohm fresh. The model's 0.15 ohm is at the low
   end. That is fine.
6. AA capacity: Energizer rates 2850 mAh at 25 mA, and less at high drain. The model's 2000 mAh gives "6 h 40 min" at
   0.3 A, which is generous for an alkaline cell at that drain. It is labelled an estimate (finding 13).
7. LED forward voltages: red 1.8 to 2.2 V and blue 3.0 to 3.4 V in common tables. The model's 2.0 and 3.0 V fit.
8. Tungsten hot/cold ratio about 10 to 15: the model's 9.8 / 1.0 fits.
9. E12 decade values (Vishay 31001): 10 12 15 18 22 27 33 39 47 56 68 82. The code's array matches; 49 settings is
   correct for four decades plus the endpoint.
10. Straight-wire field mu0 I / (2 pi r): 0.3 A at 1 cm is 6.0 uT, so a needle 16.7 degrees off north under a wire
    running north-south. The code's Biot-Savart reproduces this: 11 degrees for the drawn arc, t23.
11. Continuity beep: meters set it somewhere between about 0 and 100 ohm (forum reports, no maker figure found).
    30 ohm is a fair design value.

#### Findings

1. **Coil + compass starter: the needle is pinned at 90 degrees, so "more turns, more current, iron core" never
   shows on it** (src.html:1052-1058 loadSetup(6); compassFields 582-585). Level: should fix. Tag: family:curiosity.
   - What: with 200 turns on 2 x AA, the coil's external field at the compass is about 2.7 mT against Earth's 20 uT.
     The needle reads 88.4 / 89.2 / 89.6 / 89.8 degrees at 50 / 100 / 200 / 400 turns, and 90.0 degrees with the
     core.
   - Even at the board's far corner, 50 turns gives 82 degrees and 400 turns gives 89 degrees. 1 cell vs 4 cells
     gives 75 vs 86 degrees.
   - Why it matters: MS-PS2-3 (factors that affect the strength of magnetic forces) and the spec's Things to do 10
     ("watch the field readout and the needle grow") depend on seeing the force change. Only the mT readout moves;
     the one thing that shows a force does not.
   - Better: a starter where the compass sits far enough away (or the external-field falloff is realistic: a dipole
     of N I pi r^2 gives about 20 uT at 7.6 cm, not the model's 70 uT). Then 50 turns sits near 20 to 40 degrees
     and turns, cells and core visibly swing it.
   - The starter also has no switch, so the needle never swings on closing.
   - Seen: t16-coil.png, t24 values.

2. **Oersted wire starter swings the needle only 4 degrees** (src.html:1043-1051). Level: should fix. Tag: general.
   - What: the compass sits between the outgoing and the return jumper, which run diagonally and partly cancel. The
     reading is +4.3 degrees closed and -3.8 degrees reversed (t15, t15b).
   - Scanning every hole in that setup, the best is 4.4 degrees (t21). The spec's checked value is about 17 degrees.
   - Done when 4 technically passes (the swing does reverse), but 4 degrees on a 60 px dial is barely visible.
   - The physics is right: wires on this board mostly run east-west, which barely moves a needle. A north-south
     wire gives 11 degrees (t23). The tool never says this.
   - Better: lay the starter's jumper north-south straight over the compass, away from the return lead. Add a
     "Things people have found" line: a wire lined up with the needle swings it most, and one across it barely
     moves it. That is the real Oersted condition.
   - Seen: t15b-oersted-on.png, t22, t23.

3. **The compass is drawn on top of the wire but its field is computed as if it sat 1 cm below the wire, so the
   needle swings the wrong way for what the student sees** (src.html:586-596, draw order 1801-1802). Level: should
   fix. Tag: general.
   - What: in t23 the compass disc covers the jumper, so the picture says the compass is above the wire. The code
     puts it 1 cm below (rz = -0.01), and the Manual says so.
   - For a wire under a compass, the deflection is opposite. A student or teacher checking with the right-hand
     rule, or with a real compass on a real wire, gets the reverse answer.
   - Better: draw jumpers over the compass (they arch above the board), or compute for the compass above.
   - Seen: t23-ns-wire.png.

4. **The coil's field points the same way all round it** (src.html:582-585). Level: should fix. Tag:
   family:curiosity.
   - What: the field to the compass is always along the coil's axis, scaled by distance. With the compass beside
     the coil (t24: 18,11 and 18,13) the needle points the same way as on the axis (87 to 88 degrees east). A real
     coil's field beside it runs the other way, back round to close the loop.
   - Mapping a field with a compass is the natural investigation for MS-PS2-5 (evidence that a field exists around
     the object). Here that map is wrong off the axis.
   - The Manual's honesty note says only "falls away with distance".
   - Better: a dipole field (radial and axial parts). If that is out of scope, an honesty line saying the compass
     model only holds near the coil's axis.

5. **The coil keeps 4 ohm at every turn count** (src.html:512; Manual line 235). Level: should fix. Tag:
   family:curiosity.
   - What: going from 50 to 400 turns doubles and redoubles the field at the same 0.694 A (t16). A real coil wound
     from the same wire gains resistance with its length, so on the same battery its current falls as turns rise.
   - The result "more turns, stronger" is the standard's claim at equal current, and that is how the textbooks say
     it. The tool lets students conclude it holds at equal battery too, without saying why.
   - Better: one honesty line ("every coil here is 4 ohm, as if made of thicker wire as turns rise; a real coil
     gains resistance with turns"), or scale R with turns so the current readout shows the trade-off. The second
     is richer MS-PS2-3 data.

6. **The ammeter reads "- -" in a loop that is open or blocked, not 0** (src.html:617, connected() 473-483).
   Level: should fix. Tag: general.
   - What: with the meter on mA in the gap of the reversed-LED loop, the LCD shows "- -" (t20). The tag says
     0.00 A.
   - The Manual defines "- -" as "a probe or its circuit is floating", but both probes are firmly in a complete
     loop. The same happens with any open switch in series.
   - Done when 4 says the reversed LED reads 0 mA. A real meter reads 0.00 mA here, and "the current is zero" is
     exactly the observation the student should make.
   - Better: in A and mA, show 0.00 when both probes are on nodes of the solved network. Keep "- -" for a probe in
     an empty hole.
   - Seen: t20 values.

7. **The anchor module's second code is only half exercised, and two also-reaches overclaim** (spec Map; module
   science-8-electric-and-magnetic-forces = MS-PS2-3; MS-PS2-5). Level: should fix. Tag: family:curiosity.
   - MS-PS2-3: really exercised, through the coil turns, cells and core with the mT readout. Findings 1 and 5 weaken
     it.
   - MS-PS2-5: covers fields between objects not in contact, electric as well as magnetic. Only the magnetic half
     can be done here (the compass moves with nothing touching it). Electric fields and charges are absent.
   - The spec says "in part", and the tool is a second card beside the module's lesson tool. That is acceptable only
     if the lesson tool carries the electric half and the module card says so. Under BASELINE rule 2 the integrator
     should confirm it does, or the code's claim should rest on the lesson tool alone.
   - Also-reaches: science-3-magnets-and-static-electricity (3-PS2-3, 3-PS2-4) has no static electricity and no
     magnet-to-magnet interaction (only Earth on a compass). science-11 HS-PS2-5 has its current-makes-a-field half
     but not its changing-field-makes-a-current half (no generator, by the spec's own open question).
   - Better: list science-3 and science-11 as "touches" in the module data, not as reaches the tool fills. Grade 4
     (4-PS3-2: electric current turned into light, heat, sound and motion) is genuinely exercised by the bulb,
     buzzer, motor and hot short wire.

8. **No real-world safety line about shorts** (Manual lines 217-222; notes.md; spec Things to do 11 "nothing
   explodes"). Level: should fix. Tag: general.
   - What: the tool invites a student to short a battery, watch the wire glow red, and sees nothing bad happen.
   - A grade 3 to 8 student alone at home (rule 4) can try that with real AA or 9 V batteries and a paper clip. Real
     shorts get hot enough to burn fingers, and a 9 V on steel wool or foil can start a fire. Lithium cells are worse.
   - Better: one plain line in the Manual's meter section and in teacher notes ("On a real bench a short heats the
     wire fast and can burn you; never short a real battery, and never use mains power"). Add a teacher-notes line
     that the bench is for battery-level DC only.

9. **Battery tag shows negative current ("-296 mA")** (src.html:655; t03). Level: polish. Tag: general.
   - A grade 8 student reads "-296 mA" next to a bulb's "+296 mA" and may think the battery takes current in.
   - The Manual explains signed current, but only in the dense "What the instrument assumes" paragraph.
   - Better: show the battery as "supplies 296 mA" (as the spec's battery tag reads), and keep the sign for the
     meter.

10. **"Things people have found" lost the Oersted name and the sources the spec gave each entry** (Manual lines
    249-256). Level: polish. Tag: family:curiosity.
    - The notebook calls a starter "Oersted wire" but nothing on screen says who Oersted was or that this is the
      1820 discovery.
    - Better: restore the spec's short attributions, e.g. "as Hans Christian Oersted found in 1820".

11. **Compass tag shows "0.00 V · 0.00 A · 0.00 W"** (src.html:655 for type compass; t15b). Level: nit. Tag:
    general. An electrical reading on a part with no legs reads as broken. Show only the angle.

12. **Ohms across a forward LED reads 2.01 kohm** (meterRead 607-615; t19). Level: nit. Tag: general.
    - The 1 mA test source has unlimited compliance, so it forces the LED on.
    - A real meter's low test voltage usually reads OL in ohms; makers add a diode mode for this.
    - Better: cap the test source near 2 V, or add a line to the honesty notes.

13. **Battery runtime is generous at bulb-level draw** (src.html:658). Level: nit. Tag: general.
    - 2000 mAh at 0.3 A gives 6 h 40 min. Alkaline cells deliver well under their rated capacity at that drain.
    - It is labelled an estimate. One honesty clause ("real cells give less at high draw") would make it true.

#### Audit pilot

- **Leads confirmed:**
  - The manual, notebook and part-tag dialogs cover the board while they are open. That is expected for modal
    drawers, not a teaching issue.
  - The phone drawer strip scrolls sideways (7 of 12 out of view at 375). That is real, but Play and Craft own it.
- **Leads wrong:**
  - "hint out of view" on every starter state: loadSetup() hides the hint on purpose (reset(false) sets
    state.hint = false), and Read then speaks the selected part's tag. Not a fault.
  - The board/notebook/zoom "overlap" rows: those buttons sit on the mat above the canvas by design.
- **What it missed:** everything above. Findings 1 to 6 are physics and readout behaviour that only show when the
  setups are driven and the numbers read: the pinned coil needle, the 4 degree Oersted swing, the drawn-vs-computed
  compass geometry, the one-direction coil field, the fixed coil resistance and the ammeter's "- -" in a complete
  open loop. The audit also cannot see the module-code coverage or the missing safety line.

Counts: blocker 0, should fix 8, polish 2, nit 3.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: circuit-bench (Codex fix, round 2)

Scope: the 2026-11-06 exit check retains the round 1 repairs and leaves should fix 16 open, caused by should fix 5's per-frame placement search. The integrator's concluding call also requires standards metadata and notes to match spec.md Map. No questions were asked in this unattended session. Evidence root is `_scratch/circuit-bench/`.

The first line and final Integrator call in refine.md make this a narrow round 2: short-chip placement/performance and the written standards scope. The old blockers and other should-fix items were already repaired in the checked-out source. Their original faults did not recur in the regression checks described below; they were not reintroduced to manufacture before frames. RETAINED means accepted by the supplied round 1 exit check, unchanged here, and not claimed as a newly verified fix. Scientific code, controls, narration and artwork before drawShortChips are byte-identical to the saved round 2 baseline.

#### Blocker

1. FIXED, round 1 repair verified again: coil at 50/100/200/400 turns gives 28.37/46.93/64.60/76.26 degrees; core 89.07; cells 1 to 4 give 15.71/28.37/37.91/44.99; reversal -46.29; open switch essentially zero. Axial +29.17 versus beside -73.20. `r2-proof-coil.json`, `r2-proof-coil-equator.json`, viewed proof and starter-6 frames at 1366x768. Original pinned-needle fault not reproduced; no new magnetic change.
2. RETAINED: Oersted starter still reads -13.71 degrees (`r2-starter-5.json` and viewed 1366x768 frame), compass above the straight jumper. The reversal/open-switch sequence was not rerun this round; its round 1 exit acceptance remains the evidence for those steps. No new fix claimed.

#### Should fix

1. RETAINED: event narration, pop and crackle code unchanged; not freshly walked through burn and short repeats. The supplied exit check accepted the round 1 repair. See Voice walk for this round's limits.
2. RETAINED: burn tag rebuild and tap-to-replace code unchanged; not freshly burned/tapped this round.
3. RETAINED: motor latch and push-button starter unchanged. Motor starter frame viewed at 1366x768 and 800x500; latch/stall sequence not rerun.
4. FIXED, round 1 repair verified again: blocked LED gives 0.00 A on both current ranges; empty and missing probes give - -. `r2-proof-ammeter-cheats.json` and viewed 1366x768 frame. Original fault not reproduced.
5. FIXED: existing clear placement retained while removing its per-frame search. Same busy-board positions before/after: (720,52), clearance 9 px for one short; (300,52), 47 px and (720,52), 9 px for two shorts. The simple short with probes retains 9.866 px clearance at 1366x768, 680x425, 800x500 and 1920x1080. All frames viewed. `r2-before-clean-*.json`, `r2-after-*.json`, `r2-proof-short-clearance.json`, `r2-short-*.json`. New WeakMap entries reject stale saved chips and refresh on relevant geometry changes. See cache attempts below.
6. FIXED, round 1 repair visually verified again: 9 V body and snaps, single label; viewed starter-3 and turn-label frames at 1366x768. Original overprinted AA label not reproduced.
7. FIXED, round 1 repair visually verified again: sharp part text in viewed starter, 680 Adjust and 1920 projector frames. The old fillText interception returns an empty list because rasterized part text is already cached; that empty diagnostic is not proof. Source shadow-reset logic is unchanged.
8. RETAINED: fuse explanation and Use A for bulbs remain in the captured Manual and unchanged event handler. Fuse was not freshly blown this round.
9. FIXED, round 1 repair verified again: captured Manual explicitly says every coil is 4 ohms with thicker wire as turns rise. `r2-proof-manual.json`; no resistance-model change.
10. FIXED, round 1 repair verified again: required real-bench heat/burn/mains sentence remains in the captured Manual and teacher notes; battery-level DC only remains in notes. `r2-proof-manual.json`.
11. FIXED, round 1 repair verified again: visible Motion OFF and Sound OFF in `r2-proof-toggle-off.json` and its viewed 1366x768 frame; labels and switch marks remain.
12. FIXED, round 1 repair verified again: four real Tabs focus board; 3 px dark outline at -6 px inset. `r2-proof-focus-board.json` and viewed 1366x768 frame.
13. FIXED, round 1 repair verified again: real Tab focus shows dark 3 px outline on the 680x425 paper tray, with the light rim retained. `r2-proof-adjust-680.json` and viewed frame. Previously documented contrast ratios are retained, not newly measured.
14. FIXED, round 1 formatter verified again: volts, milliamps, milliwatts, kilohms, no reading, fuse open and Meter off. `r2-proof-read-format.json`. These are formatter outputs, not a new audible walk.
15. RETAINED: centralized drawer pressed-state synchronization unchanged; no fresh placement sequence this round.
16. NOT FIXED to a strict 60 fps at 4x CPU throttle. The specific round 2 regression is fixed: placement is cached, obstacles sampled once per geometry, candidates scored once without sorting. Before/after measurements at 1366x768 are below. Desktop one/two-short runs now reach 59.81/60.05 fps, but 4x runs reach 42.68/43.54 fps. The no-short control is also below the bar (38.75 fps). No blanket performance PASS is claimed.
17. FIXED, round 1 repair verified again at 680x425: Adjust is non-modal, tag y204 and tray y239; resistor, LED and 20.5 mA remain visible. `r2-proof-adjust-680.json` and viewed frame. Original modal obstruction not reproduced.

#### Polish accepted

1. RETAINED and viewed: warm one-bulb and parallel glow, dimmer series glow, 1366x768 starters 0 to 2.
2. RETAINED: burnout flash/smoke code unchanged; transient was not freshly captured this round.
3. FIXED, round 1 repair verified again: battery tag says supplies 9.68 A in `r2-proof-short-clearance.json` and viewed 1366x768 frame.
4. FIXED, round 1 repair verified again: discovery attributions including Oersted in 1820 remain in captured Manual (`r2-proof-manual.json`).
5. FIXED, round 1 repair visually verified again: default loose tips have open-end rings, viewed `r2-starters/r2-default.png`, 1366x768.
6. RETAINED: drawer drag ghost code unchanged; no fresh mid-drag capture.
7. FIXED, round 1 repair visually verified again: probes reach meter jacks and dial has range legends; viewed short/probe frames at 1366x768, 680x425 and 800x500.
8. FIXED, round 1 repair verified again at 1920x1080: tag font 22 px, board scale 1.437. `r2-proof-projector.json` and viewed frame.
9. FIXED, round 1 repair visually verified again: tools above board at 680x425, push button visible at 800x500. Viewed Adjust and motor frames; `r2-proof-motor-800.json` records part coordinates.
10. RETAINED: LCD settle/read announcement code unchanged; no fresh one-second live-region timing measurement.
11. RETAINED: angle-only compass tag code unchanged; no fresh selection capture of that tag.
12. FIXED, round 1 repair visually verified again: opening and idle motor tags show zeros, not leakage micro-readings; viewed default and starter-7 frames at 1366x768.
13. FIXED, round 1 repair visually verified again: reversed LED text upright in viewed `r2-proof-turn-labels.png`, 1366x768.
14. FIXED, round 1 repair visually verified again: AA polarity alternates in viewed default and starter frames, 1366x768.
15. FIXED, round 1 repair verified again: high-draw runtime and diode ohmmeter caveats remain in captured Manual (`r2-proof-manual.json`).
16. RETAINED: resistor aria-valuetext still uses spoken formatter; kilohms formatter is verified, but no fresh slider event/aria measurement.
17. FIXED, round 1 repair visually verified again: top-left keeps only DC and pitch; maker plate retained, viewed default at 1366x768.

#### Settled calls
Curiosity brief wins. No goal, score, level, quiz, finish or kit header added. Physics constants and circuit solver unchanged. No coil-resistance spec change. The integrator's written standards decision is applied to tool.draft.json and notes.md; catalog files are outside this session's write scope.

- Magnetism stays an instrument readout with real field direction; no target angle or challenge added.
- First-tap hint suppression and Read behavior are retained, including opening a drawer first.
- Starter loads still dismiss the first-action hint.
- Manual and Notebook remain modal; compact Adjust remains non-modal. Existing scrolling and coverage are reported under Audit.
- Burn wording remains exactly: That part burned out. Tap it to replace it. Tap-to-replace code is retained.
- Motor starter keeps its push button; the separate shaft latch is retained.
- AA, bulb, LED and motor constants are unchanged. No score, finish or magnetic target was introduced.

#### Cheats tried
No score, check to pass or finish exists. The meaningful attempts target misleading/stale instrument output.

- 240 unchanged redraws: zero new layout searches. Current changed while staying above 3 A: zero new searches.
- Add a wire, replug its endpoint, remove it: exactly one layout per change; result agrees with an independent evaluation of the original clearance rule.
- Attach, move and remove a probe: exactly one layout per change and same independent placement result.
- Move and rotate the battery: exactly one new layout for each source centre change.
- End a short: chip removed. Restart it: one fresh layout. Restore a forged save with chip (-999,-999): ignored and correctly recomputed.
- Thirty extra solves/draws: layout count unchanged. Real Red probe click and arrow/Enter input: geometry refreshes (layout count 1 to 3) and clear label retained.
- Floating-probe shortcut: empty and missing probes stay - -; a genuinely blocked but attached current branch reads zero.

Evidence: `r2-cache-invalidation.json`, `r2-probe-real-move.json`, `r2-proof-ammeter-cheats.json`. All corresponding frames viewed.

#### Voice walk
No narration code, event triggers, hint or bank text changed. Current browser allLines() exactly equals voice/lines.json's three lines; recorded in `r2-proof-read-format.json` and checked by script. Read formatter outputs were rechecked as numbers/text. A new full audible burn/short repeat walk was not performed; no fresh heard-count claim is made for those retained round 1 repairs. The final audit's own voice evidence is reported below. Existing missing recordings still use browser speech fallback; none were generated.

#### Engine changes wanted
None.

#### Audit
FINISHED, once, last, within its 2400 second deadline. Command: `python scripts/audit_tool.py circuit-bench _scratch/circuit-bench/r2-fix-audit --port 9911 --profile S:/CurioClass-codex/_scratch/circuit-bench/chrome-r2-audit --host-port 8715`. Muted Chrome; no rerun. Report: `r2-fix-audit/audit.md`; 94 frames reviewed on contact sheets 0 to 10, with full-size phone Manual and compact/phone part-tag frames also viewed.

All 112 mechanical leads are accounted for here:

| Rows | Disposition |
|---|---|
| 38 overlaps | Board controls, cursor and hint intentionally overlay the canvas. The two phone drawer title/Close bounding boxes overlap, but the visible words do not touch; full-size phone Manual viewed. Retained settled design. |
| 3 scroll-panel leads | Phone parts strip and Manual source links are intentionally scrollable. The 680x425 AA battery Adjust tray puts Turn/Remove in horizontal overflow; cell count and Reverse stay visible with the part and its tag. This existing secondary-control limitation is recorded below, not called newly fixed. |
| 10 hidden hints | Starters and restored circuits dismiss the first-action hint. Correct under the Curiosity brief and explicit settled call. |
| 50 text-under-box leads | Manual and Notebook intentionally cover the bench beneath them. No text within the active drawer was shown hidden under an accidental box in the reviewed frames. |
| 9 keep-region leads | Eight are the intentional Manual/Notebook modal coverage; one is two phone board samples behind board tools while Adjust is open. Part, tag and adjustments remain visible. Settled instrument/drawer behavior retained. |
| 2 missing welcomes | First tap on Notebook or Manual suppresses the one-time hint. The hint remains on the mat and Read speaks it. Explicitly accepted by the supplied exit check; no lesson welcome added. |

Motion off: clean, nothing runs forever. Full final resize stress: no exceptions and no controls left disabled. All 36 held-click rows have empty error cells and focus retained; ten five-click and ten quick-tap rows are clean. Read logs the hint followed by Meter off on the opening bench. These checks do not exercise a fresh burnout/short event sequence. The audit does not measure frame rate or prove magnetic equations; the targeted numbers above do that work.

No new cache-related regression was found. A blanket gate PASS is not claimed because should fix 16's strict throttled 60 fps bar remains unproved. The owned Chrome/host listeners are checked closed before publishing this report (`r2-cleanup.json`); port 9910 was handled by the driver's owner-aware cleanup. No unrelated browser was closed.

#### Left open
Strict 60 fps at 4x throttle remains unproved; physical Chromebook performance was not measured. The round 2 placement regression is removed. The standards call is applied in the permitted metadata and notes; no catalog or module files were edited. The coil-resistance scaling, schematic and generator open questions remain untouched. No ten-minute student/adult play session was repeated in this narrow rendering repair. The existing AA battery Adjust tray at 680x425 requires horizontal scrolling for Turn/Remove; the main cell-count and reversal controls remain visible. Event speech and transient burn repairs marked RETAINED were not freshly walked in this round.

#### The real material
Only rendering/cache code and standards scope were changed. No scientific fact, model constant, dataset, source text, artwork or recording was added or retuned. Existing named sources and licence statements in the Manual and tool.draft.json remain. The standards-scope authority is the integrator's 2026-11-06 call in spec.md Map. Original code is MIT; original instrument text/graphics CC BY 4.0. No downloads or data sampling were needed.

The existing factual sources remain OpenStax College Physics 2e and University Physics Volume 2 (current cited licence CC BY-NC-SA 4.0, facts only), Georgia State University HyperPhysics (copyright, diode facts only), Vishay document 31001 (copyright, E12 facts only), NOAA/BGS World Magnetic Model (government context, no coefficients), Britannica (copyright, attribution only) and CPSC (public US government battery-hazard information). No material from these sources was newly copied or fetched. All constants remain declared Curio Class design assumptions. The source URLs and licensing details remain in the bundled Manual and tool.draft.json.

#### Performance evidence
Same exit-check fixture, 1366x768, 30 parts and five lit bulbs. The initial broad before batch used allowed port 9910. The clean before rerun and all after/targeted batches use muted Chrome 9914. Before files are the clean rerun against the saved unmodified bundle except the one-short/4x row, which comes from the initial batch; after files use the generated fix-2 bundle. One-short fixture has 17 wires, two-short fixture 16. Units are ms unless fps is named.

| Case | Before draw | After draw | Before fps | After fps | After mean frame work |
|---|---:|---:|---:|---:|---:|
| One short, 1x | 29.01 | 0.187 | 31.38 | 59.81 | 0.521 |
| Two shorts, 1x | 52.49 | 0.172 | 18.08 | 60.05 | 0.511 |
| One short, 4x | 161.07 | 1.482 | 5.42 | 42.68 | 2.226 |
| Two shorts, 4x | 304.81 | 1.277 | 3.04 | 43.54 | 2.024 |

One-short 4x before value comes from `r2-before-1short-4x.json`; the others from `r2-before-clean-*.json`. Every after result shows shortLayouts unchanged over 180 animated frames plus 60 explicit redraws. Matching no-short control: 59.73 fps at 1x and 38.75 fps at 4x (`r2-no-short-*.json`). This control supports removal of the short-specific cost; it does not certify 60 fps under throttling.

The initial long two-short/4x browser evaluation hit the driver's 60-second per-call deadline. It was retried once with 60 frames and 10 explicit draws and completed cleanly. All shell/process commands had bounded lifetimes; bundles 120 seconds, drive batches at most 300 seconds, final audit 2400 seconds.

#### Regression and bundle
Default and every one of the eight starters re-shot at 1366x768; all viewed. Existing coil, meter zero/floating, focus, 680 Adjust, 800 motor, 1920 projector, Manual and toggle repairs received targeted checks. All successful final drive batches report zero console errors. Default and performance runs report an empty automatic resource list. Physics examples remain one bulb 0.29636 A, series 0.22643 A, parallel 0.58524 A total, red LED/330 ohm/9 V 20.496 mA. No constants were changed.

Bundle: 119,919 bytes. The repository's unmodified check() and notes_sections() passed against a scratch mirror of this tool, avoiding the global rebundler's writes to other tools. `contract-results.json`. Source and voice contain no em dash. No git commands or commits were made, and refine.md and refine/ were not edited.

Viewed frame groups: `r2-before/`, `r2-before-clean/`, `r2-after/`, `r2-control/`, `r2-checks/`, `r2-proof/`, `r2-starters/`, via their r2 contact sheets and selected full-size frames. Final audit frames are listed in its audit.md. The maker plate, Manual and instrument surface remain; no lesson structure was introduced.

#### Lesson creep check
The new internal score and bestScore variables rank geometric label positions; they are not displayed or saved as student scores. Existing references to electrical points and cached raster/geometry values describe the instrument. Voice lines are unchanged and contain none of the lesson terms. No goal ladder, score display, level, quiz, finish screen, welcome gate or kit header was added.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Circuit Bench build handoff

#### Structure
Edit src.html. CSS and instrument markup come first, followed by state, three marked solver/model/compass blocks, physical controls, input handling and canvas drawing. The shared kit JavaScript is bundled, with no kit CSS. circuit-bench.html is generated by scripts/bundle_tool.py with CURIO_DRAFT=1. The draft is intentionally unpublished.

#### Physics
solveNetwork stamps a conductance matrix with Norton sources and 1 nS leakage per node. LED active states have at most 20 passes. simulate advances filament resistance, damage timers and motor speed. Meter conductance participates in the same network. Resistance measurements solve a separate cold, source-disconnected network with a 1 mA test source. A and mA are current-carrying branches, with a replaceable 200 mA fuse. Source and sink currents are signed.

Wire magnetic fields integrate Biot-Savart along their actual drawn jumper curve, sampling the compass 1 cm above the board plane. Coil labels report the finite-solenoid centre field; external compass coupling uses the vector dipole approximation with moment NIπr² and core multiplier 100, softened inside one radius. This is not a 3D field solver, an inductive-transient solver, or a WMM implementation.

#### Input and storage
The canvas has a hole cursor and part shortcuts; Tab reaches all controls. W plus Enter at each end wires by keyboard. Shift-drag replugs a component leg; plain terminal drag fits a new jumper. Parts drawers also drag onto the board. Push buttons and direct shaft holds release on pointer cancellation and lost capture. The motor tag and H latch the shaft until toggled; window blur and loading release that latch. Four versioned local storage slots save the circuit, probes, meter and fuse. Saves never leave the device.

On a compact bench, Adjust unfolds the selected part's paper tag with every control wrapped into view. This moves the original controls into a non-modal grid tray beneath the paper values, then returns them when closed. The board stays interactive. The 1000x625 preview uses the compact meter selector. Small tray labels are shortened while their accessible names retain the full part and key.

#### Validation evidence
All scripts, numbers, browser frames and audit output are in _scratch/circuit-bench/. verify.py independently recomputes examples in Python, then exercises the actual JavaScript solver using Node. check_contract.py calls the repository checker functions on a scratch metadata mirror, because the global script would rebundle other tools outside this session's write scope. Browser checks use Chrome 9980 to 9987 and host 8785 only, with audio muted.

#### Brief decisions
The Curiosity brief replaces the lesson frame. The initial hint is spoken once; Read speaks context and the live meter. Short and burnout events speak every time, update the live region and have Sound-gated electrical effects. No schematic or generator was added, as the spec defers them. Buzzer uses quiet, voltage-scaled 2.4 kHz tones only with Sound on. E12 10 Ω to 100 kΩ has 49 detents, not 61; the stated range wins. No painted asset adds material here.

#### Engine changes wanted
None required. This instrument draws its own controls and uses the shared kit for Motion, Sound, Read and tones.

#### Cold review changes
Saved SPDT positions now survive restore; only push buttons release. Canvas focus loss and global key release clear momentary holds. Reset synchronizes the fuse cover. Read names both probe tools. The 150-wire save limit is enforced when wiring. Potentiometer tags use outer voltage and both sections' power; motor watts are input. Bulb light has its own 80 ms response and a distinct orange series filament. The solver and original bench artwork remain intact.

Review evidence uses Chrome 9930 to 9937 and host 8735, separate from the builder's evidence. The initial hint remains eligible after the first wire drag, while the second loose lead still needs connecting. Sources in the Manual and draft metadata now name the finite-solenoid reference and its current online licence. No external data, new lesson structure, recordings or painted assets were added.

The audit's small-preview frame exposed clipped loose wire tips. Their opening positions are now rows e and f, in reach at all sizes. Wiring removes the matching loose lead instead of always removing the red one, so black-first and red-first connection orders both work. The phone save-switch audit state explicitly opens Adjust before Contact. The full audit was run once; these final opening/state corrections have targeted rechecks.

#### Left open
The external coil-field falloff, motor mechanical response, LED threshold, damage timers and fixed Earth field are declared models. Physical Chromebook performance is not a hardware measurement from the headless desktop test. No deployment, commits or polish round belongs to this build.


#### Refine round 1
Fix evidence is in _scratch/circuit-bench/fix-before*, fix-after*, fix-proof*, and fix-audit/.
Chrome ports are 9910 to 9917, with the iframe host on 8715; every browser is muted and closed by its runner.
The cached board is invalidated by zoom and device pixel ratio. circuitDirty triggers a solve; modelMoving keeps thermal and motor states evolving until settled.
At rest, RAF checks interaction state without redrawing. Current dots, moving motors and short burn effects keep drawing as needed; Motion off freezes travel without changing physics timing.
No AA, bulb, LED or motor constants were retuned. The coil stays 4 ohms at every turn count, explicitly stated in the Manual.
The Oersted starter uses a straight north-south jumper and distant return leads; finite jumper length gives a smaller swing than an infinite-wire example.
All source facts remain attributed in the Manual and draft metadata. No third-party text, artwork or datasets were bundled.


#### Refine performance measurement, 2026-11-06
Muted desktop Chrome at 1366x768, 4x CPU throttle, 30 parts with five lit bulbs: original 20.62 fps, first board-cache pass 46.69 fps, final board/part-cache pass 45.39 fps. Final mean measured frame work was 1.16 ms versus 5.86 ms originally; scheduling/compositing still kept observed throughput below 60 fps. This requirement remains open. The two-lit 30-part run varied from 54.02 to 39.42 fps, so a steady 60 fps is not claimed. On an idle bench, counters stayed at one solve and two draws during a two-second observation. This is a headless desktop measurement, not a school Chromebook test.
The mandatory final audit disconnected with Windows error 64 at its first browser size; it produced no report or leads. No second audit was run.

#### Refine round 2
The exit check's remaining rendering regression was in drawShortChips. A WeakMap now caches each active source's chosen chip against wire endpoints, attached probe positions and the source centre. Current changes, thermal solves, pan and zoom keep that world-coordinate layout. A short ending drops its entry; loading a saved chip never bypasses the cache. Obstacles are sampled once per geometry change and each candidate is scored once, with the original clearance and nearest-position rule preserved.

The debug metric shortLayouts verifies that steady animation does no placement searches. R2 cache checks cover 240 unchanged redraws, wire addition/removal/replugging, probe attachment/movement/removal, battery movement/rotation, a short ending/restarting and a forged stale chip in a save. New evidence uses muted Chrome 9914, the final audit uses 9911, and its iframe host is 8715. Only browsers started by these runners are closed.

The integrator's 2026-11-06 standards call is recorded in tool.draft.json and notes.md: MS-PS2-3; MS-PS2-5 in part, magnetic half only; 4-PS3-2; 4-PS3-4. Codes 3-PS2-3, 3-PS2-4 and HS-PS2-5 are touches without claims. The electric half of MS-PS2-5 rests on the module's lesson tool, as spec.md Map states. Catalog edits are outside this session's permitted scope.

At 1366x768 with the exit fixture, one/two shorts now measure 59.81/60.05 fps and 0.19/0.17 ms per draw. At 4x throttle they measure 42.68/43.54 fps, compared with 38.75 fps without shorts; mean work is about 2 ms. The search regression is fixed, but the strict 4x/60 fps claim remains unproved. See notes.md and r2-after-*.json for exact figures; prior round 1 measurements above are historical.


#### Refine round 2 final audit
The final round 2 audit completed once within the 40-minute limit, using Chrome 9911 and iframe host 8715. All 94 frames were reviewed. Its 112 mechanical leads are classified in polish.md: intentional canvas/modal/scroll and hidden-hint behavior, accepted drawer-first hint suppression, and the existing 680x425 battery tray's horizontally scrolled Turn/Remove controls. No console errors, endless calm motion, focus loss, resize exceptions or stuck controls were reported. The ten repeated-input and ten quick-tap rows are clean. This audit does not establish frame rate or independently repeat the burn/short event walk. Strict 60 fps at 4x throttle remains unproved; the short-label placement regression is removed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
- 2026-11-25: earlier round polish-1.md moved to S:/CurioClass-archive/tool-rounds-2026-11-25/circuit-bench
