# Codex review: circuit-bench

## Played
Cold grade-8 and adult-perspective play: loose leads, all eight setups, independent probes, drawers and running resize before reading the builder's report, handoff, notes or source. Best moment: closing a loop makes the actual solved circuit give light. This feels like a bench worth taking apart.

Short test, as reviewer judgments rather than a child/adult study:

| Question | Judgment |
|---|---|
| Would a kid open it unassigned? | Yes: physical leads and a waiting bulb invite action. |
| Would an adult play for fun? | Yes: meter loading, motor back voltage and rewiring have real depth. |
| Is the real thing the interface? | Yes: topology, current, light and magnetic response drive the display. |
| Does it work without a score or finish? | Yes: nothing grades, unlocks or ends exploration. |

![Circuit Bench beside Elements Inspector](../../_scratch/circuit-bench/review-short-test-comparison.png)

## Findings fixed
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

## Findings left
No known implementation blocker or should-fix remains.
- **Validation limitation:** no physical school Chromebook was available; spec Done when 10's hardware 60 fps claim remains unverified. Desktop/model evidence is not a hardware certification.
- **Polish:** narration uses the kit's browser fallback; the named Schedar recordings are absent. No recording was generated in this review.

## Break it
[Independent arithmetic](../../_scratch/circuit-bench/review-numbers.json), [47 current-source checks](../../_scratch/circuit-bench/review-vm-results.json), browser rechecks and held input cover:
- One bulb 0.29636 A and 2.91 V; series 0.22643 A; parallel source 0.58524 A. The small independent parallel difference is explicit wire topology.
- Protected LED 20.496 mA; all four colours; reverse dark; direct LED opens and can be replaced. Resistance 10 ohms/100 kilohms; wiper 0/50/100 percent; one/four cells, 9 V and reversal.
- Motor 0.150 A running, 1.282 A stalled in the push-button setup, then 0.150 A after release. The extra contact/wire resistance explains the difference from the bare-loop 1.293 A example.
- Coil 50/400 turns, core factor 100 and magnetic reversal. The 200-turn air-core formula independently gives 5.61985 mT/A.
- Meter OFF/V/mA/A/ohms/continuity; negative and floating probes; A-across-source 9.68 A; mA fuse opens; powered ohms LIVE; cold bulb 1.00 ohm; disconnected resistance OL.
- Rapid wiring, 150-wire save boundary, empty circuit and zoom endpoints stay finite. Keyboard alone placed a battery and bulb and wired a 0.29636 A loop. The phone saved and reopened all four slots with switch states [true, false]; Cancel preserved the four-part circuit and Clear retained all slots.
- Powered resize 1366 to 680 and back stayed responsive. Motion off produced identical canvas pixels 700 ms apart while current stayed 0.22643 A. Grayscale preserves shapes, polarity and readouts.
- No score, quiz or success meter exists to cheat. Lesson-creep search finds only physical measurement "points", "endpoints" and a coordinate array called points.

## Voice walk
Sound on; real held input and about two-second action spacing. Final first-wire log contains the initial hint once. Read then speaks selected battery values, series-bulb values, "Red probe. Choose a board hole", "COM probe. Choose a board hole", and motor input/current context. Read still speaks with Sound off.

| Line kind | Expected | Observed |
|---|---|---|
| Initial wiring hint | Once on first eligible action | Once after first real drag |
| Context/value Read | Each explicit request | Five requests in the main walk |
| Automatic short/burn speech | Zero under the Curiosity brief | Zero; events remain visible/live-region status |

Evidence: [main voice walk](../../_scratch/circuit-bench/review-voice-walk.json), [fixed first drag](../../_scratch/circuit-bench/review-welcome.json), [focus-change/key-release check](../../_scratch/circuit-bench/review-hold-release.json). Chrome was muted; logs verify dispatch and state agreement, not recording quality.

## Facts checked
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

## Sensitivity
None: a physical electronics bench with no people imagery, bodies, cultural representation, religious content or hard-history narrative. Oersted is a setup name; no new historical claim was added.

## Flattest moment left
An unpowered or open circuit is quiet. That remains honest instrument behavior; live measurements, warm filaments and freely editable setups supply the response when the circuit changes.

## Graphics
Original canvas/SVG parts, breadboard, glass, copper, resistor bands, motor, compass and probes inspected at final sizes. No painted assets added or removed. All 94 audit PNGs were inspected through eight contact sheets; phone drawers and opening, small preview and changed states also at full size. Final bundle 100,264 bytes. Comparison above shows the material-driven density beside Elements Inspector.

## Audit
The single [full audit](../../_scratch/circuit-bench/review-audit/audit.md) finished within its 40-minute limit with **133 leads**. No runtime exceptions, stuck resize controls, repeated-speech or keyboard-focus failures were reported. [Every lead has a disposition](../../_scratch/circuit-bench/review-audit-dispositions.json): intentional canvas overlays, modal coverage, vanished first-run hints, a scrollable Manual source index and padded title boxes account for the visual flags. Manual/Notebook intentionally hush the initial wiring welcome. The hidden phone Contact click was corrected in the test state.

The audit was not rerun. Its small-preview frame exposed the clipped loose tips; the final opening and corrected phone save route were rechecked with native input afterward. All four slots and clear/cancel passed. The source-to-final [diff](../../_scratch/circuit-bench/review-changes.diff) and final [validation manifest](../../_scratch/circuit-bench/review-validation.json) are preserved. The phone wrapper logged two favicon 404 responses; these came from the test host, not instrument code or outside-data requests.
The unchanged checker definitions pass on a scratch metadata mirror, without its entry point. [Contract result](../../_scratch/circuit-bench/review-contract.json). Final targeted batches have no instrument console exceptions. Initial browser timeouts were retried in smaller batches; test-harness encoding/focus-event mistakes were corrected and distinguished from instrument faults.

## Left open
- Physical Chromebook performance and actual child/adult usability testing remain unmeasured; the short-test answers are review judgments.
- The declared DC/thermal/magnetic approximations remain; no schematic view or generator was added. E12 range, quiet 2.4 kHz buzzer and Read-only later speech follow the brief/spec lean without asking an unattended user.
- **Scope breach:** importing the repository checker unexpectedly ran its top-level global bundler and regenerated other tools' generated HTML. I stopped it. No other tool source was intentionally edited, and I did not attempt a shared-workspace rollback. Subsequent validation extracted definitions without the entry point. The first read/memory lookup also lacked an explicit kill limit; later commands were bounded.
- No git commits or deployment. Review consists of one cold pass, fixes and scoped rechecks. All owned review Chrome/server sessions were closed; ports 9930 to 9937 and 8735 were verified closed.
