# Codex report: gas-law-lab

## Built

- Grade 10 gas bench, Piston / Can / Balloon, three gases, four altitudes, notebook with all specified graph axes,
  ordinary least squares fitting, device-only saving, and a two-set Absolute zero investigation.
- Started from the kit starter. Kit frame, theme, audio and Curio.voice are used. All 11 images are generated and placed.
- Build only. No git operation, commit, deployment, voice recording or polish round. Authorized workspace confirmed first.
- Commands use bounded subprocesses: 120 s bundle, 300 s drive batches, 2400 s final audit. Only ports 9980, 9981 and 8785.

## Numbers check

- Independent script: `_scratch/gas-law-lab/recompute.py`; results: `numbers.json`.
- Recomputed all piston volumes/pressures, rms speeds, per-molecule energy, slopes, can limits, altitude pressures,
  balloon volumes, piston stop temperature and the worked energy example. All displayed precision matches the spec.
- Exact weight increment: 24.516625 kPa. At 25 °C: 97.861614786 mL unloaded; one weight gives 125.841625 kPa / 78.796090866 mL.
- Can 0.017 mol: 199.665168 kPa at 80 °C; 200.230552 at 81 °C. Pump from 0.016 to 0.017 mol at 100 °C is refused.
- Energy example: rise 7.267793 mm, weights gain 0.356363514 J, work 1.829182 J, motion change 2.743773 J, bath 4.572954 J.
- Enumerated 256 extreme-error sign patterns for 12 temperature layouts: worst zero-crossing error 7.553798 °C.
  Thirty actual seeded guided runs had worst error 4.377950 °C. This is evidence, not an exhaustive proof over every seed/layout.
- The spec calls R exact; its chosen decimal is a truncated representation of the exact N_A k product. That decimal is used consistently.

## Facts checked

- PV = nRT, proportional gas laws, Celsius-to-kelvin offset and straight-line absolute-zero extrapolation:
  [OpenStax Chemistry 2e 9.2](https://openstax.org/books/chemistry-2e/pages/9-2-relating-pressure-volume-amount-and-temperature-the-ideal-gas-law).
- Wall collisions make gas pressure; no attraction in this model; rms speed sqrt(3RT/M); mean translational energy
  (3/2)kT; all species have equal mean translational energy at equal temperature:
  [OpenStax Chemistry 2e 9.5](https://openstax.org/books/chemistry-2e/pages/9-5-the-kinetic-molecular-theory).
- Translational energy (3/2)nRT; nitrogen's extra rotational nRT; work PΔV; weights' potential energy m g Δh:
  [OpenStax University Physics 2, 3.5](https://openstax.org/books/university-physics-volume-2/pages/3-5-heat-capacities-of-an-ideal-gas),
  plus the computed weight displacement.
- R, N_A, k and conventional gravity: [NIST constants](https://physics.nist.gov/cuu/Constants/Table/allascii.txt).
  The live 2022 listing retains the specified SI constants; the build uses the spec's requested R decimal.
- He 4.0026, nitrogen 28.014 and argon 39.95 g/mol: retained from the spec's PubChem entries. Live PubChem pages
  returned a browser challenge, so a fresh independent verification of those three source pages remains open.
- Altitude pressures and balloon volumes: [U.S. Standard Atmosphere 1976](https://ntrs.nasa.gov/citations/19770009539)
  and independent evaluation of the spec's troposphere equation.
- 20.0 cm² piston, 5.00 kg blocks, 300 mL stop, 250 mL can, 200 kPa cutoff, amount limits and noise ranges are
  specified model settings, not equipment ratings. The UI labels the ideal-gas and scaled-picture assumptions.
- [HS-PS3-2](https://www.nextgenscience.org/pe/hs-ps3-2-energy): solo students heat a weighted gas and compare
  particle-motion energy with the energy in the raised weights. No state-standard code was added.
- Changing only gas cannot change the ideal-gas V/T slope. The spec contradicts itself here; the result is shown honestly.

## Break it

- One row: Fit disabled. Two identical/flat rows: no sloped-line result. Wrong axes cannot advance the guided investigation.
- Twenty repeated records at one temperature: blocked. Four rows spanning only 30 °C: blocked with a named remaining gap.
- Mixed first setups: rows are saved as bench data, excluded from progress. Unchanged or two-factor second setups: blocked.
- A single warm-up with repeated Record taps originally could collect a wide span without four bath settings.
  Fixed by requiring four distinct bath settings and four distinct gas readings. Retest: 97.36 °C span, only two bath settings, blocked.
- Piston-stop rows are excluded from guided sets. Deleting a required row invalidates the comparison and hides the result.
- Exact second set at 0.008 mol: slope 2×, same crossing. Noisy seeds stay within the tested bounds. Gas-only comparison has the same slope.
- Can: tried both excess Pump and excess bath, including a combined test-hook amount/temperature update.
  Fixed transactional validation order; all reference checks then passed. Limits remain live during temperature changes.
- Record during warming saves the displayed sample at once: tested at 59.09 °C / 109.05 mL, then immediately restarted cooling.
- Device saving verified. No best score, points or hidden-answer badge. Wall hits and energy bars are observations, not completion gates.
- A real jittered whole-pixel drag tried to take the can bath to 100 °C: it stopped at 80 °C, below 200 kPa. A native gas selection gave a 1.000 slope ratio for nitrogen vs helium.
- Motion-off positions compared across 1.3 seconds: unchanged. Still frames have speed arrows and sampled picture hit counts.
- Evidence: `model-checks.json`, `cheat-checks.json`, `live-record.json`, `extra-checks.json`, `keyboard-run.json` in Scratch.

## Voice walk

- Browser fallback only; eight lines listed for bank bright-teacher, voice Autonoe, with the spec's lab-instructor style.
- Held clicks, 120 ms, two-second pace. Bench: wBench, weightTip, fitTip, zero. The student's action can cut the welcome.
- Absolute zero, default settings: wZero, fitTip, zero, second, zero. Both fits completed with Real lab on.
  Crossings in this walk: −273.3317 and −274.6121 °C. The two how-to lines started once; the zero event started twice.
- Can side path: canStop on each audible refusal; Read interrupted correctly; Sound off did not consume the event;
  Sound on allowed the next canStop. A stale Bench welcome was dropped, not replayed late.
- An input cut fitTip when Fit was pressed; it had already started. No action waited for narration. Current hints update synchronously.
- Clear and Delete now hush stale speech/Read. Final held Read → Clear → actual can refusal started canStop promptly; see `read-clear-proof.json`.
- Evidence: `voice-bench.json`, `voice-zero.json`, `voice-side.json`, `fix-weight-voice.json`. Logs establish clip starts; no recorded voice was produced or auditioned.

## Feel check

- Best moment: the second dashed line comes back to the first line's zero crossing, then the card presents this student's two results.
- Flattest moment 1: weight changes initially jumped a number. Added visible piston travel, weighted compression, wall-hit flashes,
  input tones and signed energy/rise readouts. The water tint follows the bath while the thermometer follows the gas.
- Flattest moment 2: the first fitted line vanished as the next step opened. Kept it visible until the student changes the second setup.
- Art correction: the first keyed glass had colored spill. Regenerated the bath and cylinder with alpha; inspected their final placement.
- Compared the 1366×768 bench with both bar tools; `bar-comparison.png` places this bench beside Beat Lab.
  The painted place, instrument detail, immediate motion and compact control desk meet the visual bar. The investigation stays within the gas-law spec.

## Done when

1. PASS: 97.86 / 122.48 mL and R = 8.314, checked against independent values and browser model assertions.
2. PASS: one weight gives 125.84 kPa / 78.80 mL; He 1363 and nitrogen 515 m/s without changing P or V.
3. PASS: can 90.84 / 124.10 kPa; 0.017 mol bath clamps at 80 °C; excess Pump refused with canStop.
4. PASS: balloon 2.45 L at sea level and 4.59 L at 5000 m; all four painted altitude scenes inspected.
5. PASS: exact four-temperature fits cross at −273.15, displayed −273.2; 0.008 mol doubles the slope.
6. PASS for tested cases: all extreme sign patterns in the 12 layouts and 30 seeded UI runs within 8 °C; one-row Fit disabled.
7. PASS: 0.356363514 J and 7.267793 mm in the browser model, with bars and live scene.
8. PASS: apparatus/particle view dominates Bench at 1366 and 680; graph dominates the guided fitting steps.
9. PASS: held-click mid-approach Record and immediate bath restart, with no warming lockout.
10. PASS in main/side voice walks: how-to once, event repeats, no Fit instruction while disabled.
11. PASS for the required main controls/readouts, keyboard, Motion off, images and offline behavior. Every STANDARDS size was looked at; compact Notebook record management scrolls intentionally.

## Wave lessons

- Hint/voice: PASS in main and side walks. Hint updates in the input handler; Read reads it; how lines use V.heard.
- Focus/layout: PASS in targeted keyboard work; no focus on load. Boundary controls transfer focus to their enabled partner.
  Row deletion preserves focus on the next row or Clear. Result focuses its close button without scrolling.
- Sizes/44 px: PASS after the focused corrections. Main controls, hints and readouts remain visible, with no target below 44 px.
- No giveaways: PASS. No quiz/score; guided completion demands the measurements and valid fits, including the warm-up shortcut test.
- Honest numbers: PASS. SI readouts never use the particle picture; model assumptions and device-only storage are visible.
  Energy bars have labeled scales fixed per apparatus, so doubling amount doubles the motion bar. Weight-bar saturation is labeled; the signed value is always shown.
- Palette: computed brand/panel 9.87:1, brand/section 9.35:1, brand ink/brand 10.53:1, muted/panel 8.13:1, brass/chip 10.09:1.
- Standards/family: HS-PS3-2 is taught. FAIL for required family reuse: the specified engine/doc do not exist; local picture used.
- Motion off: PASS targeted position comparison, no CSS animation loops; exact values update instantly.
- Short choices: apparatus/gas/altitude choices are native selects; all four bath presets remain in view.
- Resize mid-animation: PASS in the completed audit stress run, 1366×768 to 760×900 and back after inputs. No exceptions or controls left disabled.
- Welcome after first tap: PASS. Stale welcomes do not return late; first actions proceed immediately.
- Unknowns: no hidden diagnosis state. Every displayed physical value is a model result or a labeled noisy reading.
- One look/one meaning: species differ by color and size; set A uses circles/solid blue, B diamonds/brass.
- Badge truth: no badge. Set counts exclude duplicated settings and unqualified bench rows.
- Hint returns: changing apparatus replaces the hint at once; can warnings clear on the next action.
- No answer by copied words: no multiple-choice diagnosis or answer-card matching mechanic.

## Audit leads

- Completed one full audit within its 40-minute limit: `_scratch/gas-law-lab/audit/audit.md`. Its 94 leads describe the pre-fix bundle.
- Bath-label/value overlaps: fixed by removing negative spacing and reserving a full 44 px slider row.
- Small Real lab checkbox: fixed with a 44×44 input and a smaller painted check inside it. The independent phone check also found Read at 42 px; fixed to 44.
- Apparatus text behind Notebook: covered art was not a visible overlap, but is now hidden or marked decorative in Notebook, matching its actual role.
- Record flash over graph/table: suppressed in Notebook; the new row, plot dot, count and tone provide immediate feedback there.
- Clear below the compact fold: moved to the graph toolbar. Delete column sticks to the table edge.
  Remaining scroll leads concern recorded-data rows at 680 and 375, not answer choices or main experiment controls. This deliberate table-scroll tradeoff remains.
- Focus lost after the first fit: fixed by moving to Pump. The result focuses its close button, without scrolling.
- Readouts under the result card: fixed by sizing the card to the space above the readout deck. Both 680 and 375 pass the keep-region checks.
- Rapid weights cut weightTip: fixed by checking V.heard before queuing it. Two 0.7-second taps now produce one uncut how-to.
- First-action and rapid-mode welcome cuts: intentional under BASELINE rule 16 and the spec's stale welcomes. The premise remains in the current hint and Read.
- Mode-opening layout movement is expected. Sound's icon/text changes shift header controls; the main experiment controls stay put and focus remains usable.
- Audit could not locate the 375 iframe context and therefore reported no hint there. Separate drive.py --host runs evaluated the iframe directly:
  controls, Notebook and result all reached correctly; current hint and keep regions were in view. This is an audit-reader gap, not a claimed audit PASS.
- Host favicon 404 is from the test host's automatic browser request. The bundled tool has no external resources or network code.
- Final cleanup found child host processes left by the LibreOffice Python launcher. Only exact gas-law-lab --host 8785 processes were stopped;
  final validation confirms 9980, 9981 and 8785 are closed. Residual hosts may have affected the audit's iframe-context lookup.
- The completed audit found no runtime errors, infinite CSS motion, or resize-stuck controls. Five-click voice checks were clean.
- Focused post-fix measurements use the audit's page-measurement function, not a second full audit: five flagged widths, both Notebook widths, result and three phone states.
  All size/overlap/clipping/hint/keep checks pass; only the deliberate compact data-row scrolling remains.
- The first focused injector had an unfilled template token, then an automatic-semicolon return issue. Those results were rejected and archived;
  the corrected injector is required to return a measurement object. A driver “0 errors” message alone was never accepted as a pass.

## Frames looked at

- Both bar frames; original art sheet; first 1366 / 680 / guided views; all seven functional and four recheck frames.
- Every frame of the 12-shot size run, including grayscale, Motion off, both guided views and the initial keyboard check.
- Phone Bench, guided graph and result card at 375×812. All three voice-walk frames.
- Five extra frames: warming cheat/still energy, successful full keyboard fit, sea level, 1600 m, 3000 m; 5000 m was in functional frames.
- All 29 audit frames, in eight contact sheets; all 11 focused fix frames, plus the 16 archived failed-injector frames in seven sheets.
- Final phone controls, Notebook and compact result; real whole-pixel slider drag at the can limit; gas-only comparison; final Read/Clear/refusal frame.
- Final numeric/semantic validation: `FINAL_VALIDATION.json`. Layout evidence: `fix-*.json`, `phone-*-final.json`; all in Scratch.

## Art made

- 11 images; two glass assets redrawn once. All no-people. No missing art.
- 610.34 KB total finished WebP; 0 KB recorded voice; final bundle 917.99 KB against the 2048 KB goal.
- Final files: `art/gl-*.webp`; raw originals: `art/raw/*.png`; full house style and individual prompts: `art/prompts.json`.
- Built-in OpenAI image generation was used. Six apparatus sprites and four landscape panels were generated as sheets,
  split mechanically, then sized/keyed with the permitted free `art.py --rekey` form. No downloaded art or paid art.py call.

## Art still to paint

None. No people images are planned or present.

## Engine changes wanted

- `kit/particles.js`, new Box API: implement and document the absent family engine, then replace the local picture after reuse is justified.
- `docs/families/particles.md`: describe its actual API and sibling contracts. Neither file was written outside the authorized roots.

## Left open

- Required particles family engine/doc absent; full family API and sibling features were not invented in kit.
- PubChem live page verification was blocked; the specified masses and recomputed outputs were retained.
- Voice recording is intentionally deferred. The browser fallback does not establish the selected bank voice's final sound.
- Deliberate compact Notebook tradeoff: its table scrolls to recorded rows; Clear is pinned and Delete is sticky. Main experiment controls stay in view.
- Audit iframe-context detection remains unverified by that runner; independent 375 px host checks pass.
- Spec decisions: keep HS-PS3-2; gas-only slope is unchanged; use the user's image tool; no docs writes.
- Report was drafted in Scratch and installed only at the end because the user requires stopping when codex-report.md is written.
- Host-only favicon 404 is recorded separately from the offline tool. `host.html` was removed and hosts/browsers were closed.
