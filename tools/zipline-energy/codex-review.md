# Codex review: zipline-energy

## Played

Cold Grade 11 solo run and projected-classroom view: Ride, failing Pad batch, Generator batch, Ledger scrub,
Notebook comparison and all three briefs. Played before opening builder notes or source. Strong place, credible consequences.
One review pass in S:/CurioClass-codex; no commits. Evidence paths below are relative to _scratch/zipline-energy/.

## Findings fixed

- Should fix, general, Design: 27/34 px sliders and hidden narrow choices. All slider targets are 44 px;
  the 375x812 and 760x900 deck now keeps all design choices, Ride/Test and lab rows visible together.
- Should fix, general, 1920 Design: taller targets pushed the hint below the screen. Removed empty hardware spacing;
  the 180 px brake illustration retains its actual display size. Footer now ends exactly at 1080 px.
- Should fix, general, Notebook: empty Compare revealed a canned answer; its question assumed a better generator result.
  Now needs complete, matching three-mass evidence for both brakes and a written attempt, then shows measured evidence.
  It gives no automatic writing score. The question now asks what the student's chosen brakes actually did.
- Should fix, general, stalled rides: generic advice said to change a brake the rider never reached.
  Hint and event now name Tree anchor and Cable sag; confirmed at 266.3 m on the 30 m tree case.
- Should fix, general, voice: edits/new runs could leave old speech running, Cards could cover a live result,
  and friction-off single rides could queue the lab how-to. Hush/cancel and what-if guards fit; Read hints are registered.
- Should fix, general, art: six rider paintings were missing. Generated, keyed, inspected and wired both postures for
  three people; retained the rich valley, all seven original paintings, cable slope and independent hanging bodies.
- Should fix, general, Ledger: segment identity depended on color. Large segments now carry short text labels;
  every value remains labeled beside the tower. Checked in grayscale and all eight sizes.
- Should fix, general, sources: corrected the obsolete ellipse citation from 8.1 to current OpenStax 10.1.
- Polish, general: replaced the flat canned Notebook response with this student's two-brake measurements.
- Polish, general: suppressed the small-stage slogan where it collided with the scale annotation.
- Should fix, general, audit: crowded phone height ticks, clipped compact result text and hidden Notebook controls.
  Fewer phone ticks, tighter short-screen lab spacing, fixed Notebook action areas and a separate evidence scroller.
- Should fix, general, boundaries: marginal stops could round to a ticked 296.000 m. Near-edge precision now preserves
  the strict inequality; Clear also removes stale comparison evidence and clipboard-fallback text.

## Findings left

- Should fix, general, spec scope: HS-PS3-1 asks students to create a computational model; HS-PS3-3 includes building a physical device.
  This supplied simulation supports parts of both. Notes now say so; catalog/spec remapping is outside these write folders.
- Polish, general, spec constraint: Generator 70 works unchanged for Z1, Z2 and Z3. The actual shortcut was run and succeeds.
  Those are explicitly valid spec answers. The cards verify a physical design, and cannot establish conceptual mastery.
- Cory's personal review of the six people images is pending. They remain draft art, with people:true and owner_review:pending.

## Break it

- Lab verdict and card awards: cycled every challenge and every brake without riding; no results or award.
- Swept brake strength repeatedly end to end: results cleared, no award. No pre-test success meter reveals a target.
- Ran the easy 35 kg rider three times: only the 35 kg result exists; no three-rider card or comparison evidence.
- Restarted Test five times at 2 s intervals, then edited: no completed three-rider verdict or award.
- Friction-off Test: equal 24.33 m/s zone speeds, explicitly a what-if, hidden lab verdict and no card.
- Legitimate completed Generator 70 tests earned Z1, then Z2, then Z3. Shared-answer limitation is named above.
- Compare with no rides, one brake, repeated light riders or empty prose: asks for the missing work, supplies no conclusion.
  Arbitrary nonempty prose can expose measured evidence after valid tests; it never receives a correctness claim.
- Swept the Ledger scrubber: no score/award; fixed start total and labeled energy values remain conserved.
- Opening Cards during a run cancels it and clears queued speech. No unfinished run is recorded as a completed success.
- Evidence: review-walk/breaks.json, review-precheck/, review-targeted/, review-browser-numbers.json.

## Voice walk

Held 120 ms presses, 2 s action pace, waiting for physical rides to finish; Sound on, Motion on, default design.
Stage tap, Ride, Test all three, Generator, Test all three, Ledger, real scrubber drag, Notebook, empty Compare,
typed explanation, Compare. Started lines: design, three, hard, pass, ledger, notebook, compareWrite, compare.
Every mode's how-to started in order. Action-driven cuts are logged; no late welcome or older-state queue survived.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| design, three, ledger, notebook | how/welcome | once each | once each |
| compareWrite, compare | how | once each | once each |
| pass, five further completed batches | event | five further | five further |
| Read, including Sound off | read | twice | twice |

Fast mode changes and Reset left no queued speech. Separate stall and friction-first paths heard matching guidance.
Evidence: review-walk/main.json, side.json, review-stall-voice.json and review-off-voice.json.
All 29 fixed strings, including Read-only hints, match voice/lines.json. Browser speech is the fallback; no audio recorded.
Chrome stayed muted: the logs verify speech starts, with no claim of a human listening check.

## Facts checked

- Work transfers energy; kinetic energy is half mass times speed squared; friction transfers energy to thermal stores:
  [OpenStax College Physics 2e 7.2](https://openstax.org/books/college-physics-2e/pages/7-2-kinetic-energy-and-the-work-energy-theorem).
- Height energy is mgh relative to a chosen zero; friction-free speed follows sqrt(2 g delta h):
  [OpenStax 7.3](https://openstax.org/books/college-physics-2e/pages/7-3-gravitational-potential-energy).
- Quadratic air drag and reduced frontal area reducing drag:
  [OpenStax 5.2](https://openstax.org/books/college-physics-2e/pages/5-2-drag-forces).
- Density varies with altitude and temperature; 1.20 kg/m³ is an explicit near-sea-level laboratory approximation:
  [NASA Glenn Earth Atmosphere Model](https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html).
- Constant two-focus distance sum and a squared = b squared + c squared:
  [OpenStax Precalculus 2e 10.1](https://openstax.org/books/precalculus-2e/pages/10-1-the-ellipse).
- Motion can drive electrical generation:
  [OpenStax 23.5](https://openstax.org/books/college-physics-2e/pages/23-5-electric-generators).
- 1.5 g, 1 m/s, coefficients, drag areas, force settings, F = k v and the 80/20 split are the spec's lab assumptions,
  not industry safety guidance. Hoerner's book was not independently inspected; exact drag areas are not claimed as measurements.
- Independently solved the two-focus geometry and integrated 27 rides: default Pad 70 kg gives 11.31547 m/s,
  281.35244 m, 1.23909 g; Generator 70 gives 3,292.73 J battery, 0.91465 Wh; no-brake edge is 9.05113 m/s.
  Friction-off speeds coincide at 24.32806; tree 30 stalls 35 kg at 266.33174; sag 20 stalls at 274.68861 m.
  Browser comparison: max stop difference 0.001285 m, speed difference 1.85e-13 m/s, zero pass mismatches,
  max closure 0.000000529 percent. Boundary probes match Z1/Z2/Z3; marginal worn Generator 50 stops at 295.99969 m.
  The spec's 19,963 J is height lost, not start total; remaining height stays in the 20,716 J ledger. No solver retuning.
- Standard wording checked against [NGSS HS-PS3](https://www.nextgenscience.org/dci-arrangement/hs-ps3-energy).
  Evidence: review_physics.py, review-numbers.json, review-browser-numbers.json, review-boundary-Z*.json.

## Sensitivity

People/body-size representation needs review: varied skin tones, ages and gender, both postures fully clothed and harnessed.
The mass labels are test inputs, not a rule for guessing weight from appearance. No cultural, Indigenous, religious or hard-history content.
The contact sheet is review-art-sheet.png; Cory's personal art approval is not asserted.

## Flattest moment left

The approximately 24-second default solo ride has a quiet middle. Real-time playback is prescribed; the live speed,
trace, painted rider and visible brake preserve its purpose. Notebook's former flat explanation is now personal evidence.

## Graphics

All 13 named images checked as finished WebPs, on a contact sheet and in use; six new people cutouts, no discarded strong art.
Prompts/provenance: art/prompts.json; generated with built-in imagegen, packed only with art.py --rekey.
Final assets: tools/zipline-energy/art/zl-rider-*.webp, originals in art/raw/. Art 388.45 KiB; bundle 675,332 bytes (659.50 KiB).
Compared with retained Beat Lab and Snowy Mail Route reference frames. The spec says 14 images but names 13.
Recomputed contrast: brand/panel 9.60:1, brand/secondary 9.10:1, button text/brand 10.07:1; segment labels at least 7.40:1.

## Audit

Completed once within 40 minutes: 23 leads, 55 frames, all viewed; review-audit/audit.md and review-audit-sheets/.
Ten layout leads fixed and re-shot. Five modal-coverage leads are intentional; three first-tap skips and five rapid cuts follow BASELINE 16.
Resize had no exceptions or stuck controls. Post-a/post-b frames, final voice walk and cheat reruns verify repairs; no second audit.

## Left open

No spec, shared kit, scripts or catalog edits; no commits. Lab settings and people were retained as the current brief directs.
The full parameter sweep exceeded the driver limit; one smaller boundary retry completed. No second audit will run.
Initial small document/memory reads used the tool yield limit rather than a hard kill; later commands enforce hard timeouts.
