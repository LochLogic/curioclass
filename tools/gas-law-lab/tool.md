# Gas Law Lab: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: gas-law-lab

#### Built

- Grade 10 gas bench, Piston / Can / Balloon, three gases, four altitudes, notebook with all specified graph axes,
  ordinary least squares fitting, device-only saving, and a two-set Absolute zero investigation.
- Started from the kit starter. Kit frame, theme, audio and Curio.voice are used. All 11 images are generated and placed.
- Build only. No git operation, commit, deployment, voice recording or polish round. Authorized workspace confirmed first.
- Commands use bounded subprocesses: 120 s bundle, 300 s drive batches, 2400 s final audit. Only ports 9980, 9981 and 8785.

#### Numbers check

- Independent script: `_scratch/gas-law-lab/recompute.py`; results: `numbers.json`.
- Recomputed all piston volumes/pressures, rms speeds, per-molecule energy, slopes, can limits, altitude pressures,
  balloon volumes, piston stop temperature and the worked energy example. All displayed precision matches the spec.
- Exact weight increment: 24.516625 kPa. At 25 °C: 97.861614786 mL unloaded; one weight gives 125.841625 kPa / 78.796090866 mL.
- Can 0.017 mol: 199.665168 kPa at 80 °C; 200.230552 at 81 °C. Pump from 0.016 to 0.017 mol at 100 °C is refused.
- Energy example: rise 7.267793 mm, weights gain 0.356363514 J, work 1.829182 J, motion change 2.743773 J, bath 4.572954 J.
- Enumerated 256 extreme-error sign patterns for 12 temperature layouts: worst zero-crossing error 7.553798 °C.
  Thirty actual seeded guided runs had worst error 4.377950 °C. This is evidence, not an exhaustive proof over every seed/layout.
- The spec calls R exact; its chosen decimal is a truncated representation of the exact N_A k product. That decimal is used consistently.

#### Facts checked

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

#### Break it

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

#### Voice walk

- Browser fallback only; eight lines listed for bank bright-teacher, voice Autonoe, with the spec's lab-instructor style.
- Held clicks, 120 ms, two-second pace. Bench: wBench, weightTip, fitTip, zero. The student's action can cut the welcome.
- Absolute zero, default settings: wZero, fitTip, zero, second, zero. Both fits completed with Real lab on.
  Crossings in this walk: −273.3317 and −274.6121 °C. The two how-to lines started once; the zero event started twice.
- Can side path: canStop on each audible refusal; Read interrupted correctly; Sound off did not consume the event;
  Sound on allowed the next canStop. A stale Bench welcome was dropped, not replayed late.
- An input cut fitTip when Fit was pressed; it had already started. No action waited for narration. Current hints update synchronously.
- Clear and Delete now hush stale speech/Read. Final held Read → Clear → actual can refusal started canStop promptly; see `read-clear-proof.json`.
- Evidence: `voice-bench.json`, `voice-zero.json`, `voice-side.json`, `fix-weight-voice.json`. Logs establish clip starts; no recorded voice was produced or auditioned.

#### Feel check

- Best moment: the second dashed line comes back to the first line's zero crossing, then the card presents this student's two results.
- Flattest moment 1: weight changes initially jumped a number. Added visible piston travel, weighted compression, wall-hit flashes,
  input tones and signed energy/rise readouts. The water tint follows the bath while the thermometer follows the gas.
- Flattest moment 2: the first fitted line vanished as the next step opened. Kept it visible until the student changes the second setup.
- Art correction: the first keyed glass had colored spill. Regenerated the bath and cylinder with alpha; inspected their final placement.
- Compared the 1366×768 bench with both bar tools; `bar-comparison.png` places this bench beside Beat Lab.
  The painted place, instrument detail, immediate motion and compact control desk meet the visual bar. The investigation stays within the gas-law spec.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

- Both bar frames; original art sheet; first 1366 / 680 / guided views; all seven functional and four recheck frames.
- Every frame of the 12-shot size run, including grayscale, Motion off, both guided views and the initial keyboard check.
- Phone Bench, guided graph and result card at 375×812. All three voice-walk frames.
- Five extra frames: warming cheat/still energy, successful full keyboard fit, sea level, 1600 m, 3000 m; 5000 m was in functional frames.
- All 29 audit frames, in eight contact sheets; all 11 focused fix frames, plus the 16 archived failed-injector frames in seven sheets.
- Final phone controls, Notebook and compact result; real whole-pixel slider drag at the can limit; gas-only comparison; final Read/Clear/refusal frame.
- Final numeric/semantic validation: `FINAL_VALIDATION.json`. Layout evidence: `fix-*.json`, `phone-*-final.json`; all in Scratch.

#### Art made

- 11 images; two glass assets redrawn once. All no-people. No missing art.
- 610.34 KB total finished WebP; 0 KB recorded voice; final bundle 917.99 KB against the 2048 KB goal.
- Final files: `art/gl-*.webp`; raw originals: `art/raw/*.png`; full house style and individual prompts: `art/prompts.json`.
- Built-in OpenAI image generation was used. Six apparatus sprites and four landscape panels were generated as sheets,
  split mechanically, then sized/keyed with the permitted free `art.py --rekey` form. No downloaded art or paid art.py call.

#### Art still to paint

None. No people images are planned or present.

#### Engine changes wanted

- `kit/particles.js`, new Box API: implement and document the absent family engine, then replace the local picture after reuse is justified.
- `docs/families/particles.md`: describe its actual API and sibling contracts. Neither file was written outside the authorized roots.

#### Left open

- Required particles family engine/doc absent; full family API and sibling features were not invented in kit.
- PubChem live page verification was blocked; the specified masses and recomputed outputs were retained.
- Voice recording is intentionally deferred. The browser fallback does not establish the selected bank voice's final sound.
- Deliberate compact Notebook tradeoff: its table scrolls to recorded rows; Clear is pinned and Delete is sticky. Main experiment controls stay in view.
- Audit iframe-context detection remains unverified by that runner; independent 375 px host checks pass.
- Spec decisions: keep HS-PS3-2; gas-only slope is unchanged; use the user's image tool; no docs writes.
- Report was drafted in Scratch and installed only at the end because the user requires stopping when codex-report.md is written.
- Host-only favicon 404 is recorded separately from the offline tool. `host.html` was removed and hosts/browsers were closed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: gas-law-lab

#### Played

Cold grade 10 play covered the bench, all apparatus and the complete default noisy two-set experiment before builder notes or source. Strong apparatus feedback; the result initially hid its best evidence. Evidence: review-cold/.

#### Findings fixed

- Blocker, general, apparatus switching: native Can to Piston selection carried 0.0200 mol past the 0.0100 limit. Destination limits now clamp it; native recheck returned 0.0100.
- Should fix, family:graphing, graph crossing: a Kelvin-axis fit printed 0.0 degrees Celsius; small molar crossings rounded to zero; compact fit text scrolled away. Correct units/precision and the current hint now carry the computed crossing.
- Should fix, general, keyboard: notebook row deletes preceded experiment controls. Controls now come first in DOM order while explicit grid positions preserve the scene.
- Should fix, general, notebook: deleting unrelated bench data destroyed completed guided work. Unrelated rows preserve fits; deleting B preserves valid A.
- Should fix, general, voice: the 60-degree instruction was ambiguous and named disabled Fit line at 1920. Welcome now names the total span and available controls; fitTip supplies the fitting instruction when enabled.
- Should fix, general, voice: compression/stop speech continued after reversal. Those lines now hush; queued fit results also validate the current fit, axes and visible graph. Five-cycle and Read/axis-race rechecks pass.
- Should fix, general, Motion: the drawn piston volume could remain stale through calm heating and jump on resuming. Calm rendering now synchronizes it; a real Motion click preserved exactly the same piston position.
- Should fix, family:particles, Balloon: a pixel-width cap flattened volume growth in the 760-wide portrait view. The base size now reserves room for maximum volume before cube-root scaling, retaining the same largest artwork and correct proportional growth.
- Polish, general, payoff: comparison card covered the convergence. Laptop result card now leaves the common crossing visible; compact card still fits.
- Polish, general, graphics: redrew the fringe-marked can in the existing style with clean alpha, preserved the other ten assets. Removed the empty decorative magnifier when the real particle canvas is hidden in graph focus.
- Should fix, general, scientific framing: result now labels extrapolation and real-gas condensation; the can scene calls 200 kPa a model cutoff. Its compact caption was shortened after the audit confirmed thermometer overlap at 680.

#### Findings left

- Should fix, family:particles, upstream engine: required kit engine and family doc are absent and outside the authorized write roots; see Left open and handoff.
- Polish, general, compact notebook: saved-row management still scrolls. These rows are observations, not a hidden set of answer choices.

No unresolved tool-local blocker or should-fix was found in the tested paths.

#### Break it

- No points, best score, quiz, or reflection gate. Gate is two qualified data sets and valid Celsius/volume fits.
- Repeated Record 20 times: one temperature, no progress. Four settings across 3 degrees: no progress; hint names the remaining 57-degree gap.
- Kelvin fit: cannot advance the guided step. Vertical/flat data: no false line. All 15 graph-axis combinations returned a finite fit or a truthful no-line result.
- Unchanged B and two-factor B: cannot finish. Exact valid B at double amount: slope doubles, both crossings -273.15 C.
- A deleted required row invalidates the result. Unrelated bench deletion preserves it; B deletion returns to B with A intact.
- Warm-up Record rhythm across almost 99 degrees with only two bath settings: blocked. A whole-pixel jittered real slider sweep stops the can bath at 80 C, never exceeding 200 kPa.
- Can Pump at 0.016 mol/100 C refused, remains 198.56 kPa. Can 0.017 mol bath clamps to 80 C below 200 kPa. Valve stops at 0.001 mol; piston at 300 mL raises pressure.
- Energy example rechecked in browser: lift 7.267793 mm, weights 0.356363514 J. Picture hits remain labeled picture-only; bars have fixed apparatus scales and signed lift values.
- Balloon width at sea level versus 5,000 m: the 760-wide cap gave a false 1.0160 ratio; fixed ratio is 1.233259, matching the cube root of the volume ratio. The 680 and 1366 checks match too.
- 100 seeded UI fits: none outside 8 C. Independent 291,840 extreme-error cases over 1,140 layouts: largest error 7.553798 C. This is finite evidence, not proof for all possible layouts.

#### Voice walk

Held 120 ms clicks, 2 s gaps, Sound and Motion on, default Real lab. Main path: Absolute zero, Ice/Record, Room/Record, Hot/Record, Boiling/Record, Notebook/Fit, Pump, repeat four settings, Notebook/Fit. Heard wZero, fitTip, zero, second, zero, in that order.
Latest checked noisy crossings: -273.8949 and -273.0913 C. The final audit-fix recheck preserved all five spoken lines. Bench/side paths also covered welcome, weight, can refusal and piston stop.

| Line | Kind | Expected starts | Observed |
| --- | --- | --- | --- |
| wZero / fitTip / second | welcome/how | 1 each per main walk | 1 each |
| zero | event | 2 main; 5 repeated fits | 2; 5 |
| weightTip | how | 1 across five actions | 1; hushed on reversal |
| canStop / stop | event | 5 each | 5 each |

First taps on stage, weight, mode, Read, Sound and keyboard behaved correctly. Read interrupted speech and worked with Sound off; rapid mode/reset dropped stale lines. No recorded clips exist; these are browser-fallback start/timing checks.

#### Facts checked

- PV=nRT, Kelvin offset, fixed-pressure volume, fixed-volume pressure, extrapolation and condensation: [OpenStax Chemistry 2e 9.2](https://openstax.org/books/chemistry-2e/pages/9-2-relating-pressure-volume-amount-and-temperature-the-ideal-gas-law).
- Collisions and pressure, rms speed sqrt(3RT/M), equal mean translational energy (3/2)kT: [OpenStax Chemistry 2e 9.5](https://openstax.org/books/chemistry-2e/pages/9-5-the-kinetic-molecular-theory).
- Translational (3/2)nRT, nitrogen rotational nRT, expansion work P delta V: [OpenStax University Physics 2, 3.5](https://openstax.org/books/university-physics-volume-2/pages/3-5-heat-capacities-of-an-ideal-gas). Worked example independently gives 1.82918 J work, 2.74377 J motion gain, 4.57295 J heat.
- R, Avogadro and Boltzmann constants: [NIST CODATA](https://physics.nist.gov/cuu/pdf/wallet_2018.pdf), cross-checked with current SI constants. R's specified decimal is truncated, not the entire exact product.
- Representative He 4.0026, N2 28.014 and Ar 39.95 g/mol: [IUPAC CIAAW](https://www.ciaaw.org/abridged-atomic-weights.htm); [PubChem helium](https://pubchem.ncbi.nlm.nih.gov/compound/Helium) and [argon](https://pubchem.ncbi.nlm.nih.gov/element/18). Nitrogen PubChem page challenged the request; CIAAW independently verifies 2 times 14.007.
- Standard atmosphere 101.325 kPa and conventional g = 9.80665 m/s2: [NIST SI Appendix B.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8).
- Altitude pressures and balloon expansion: [NOAA/NASA/USAF U.S. Standard Atmosphere 1976](https://ntrs.nasa.gov/citations/19770009539). Formula gives 101.325/83.5235/70.1085/54.0199 kPa and 2.4465/2.9680/3.5359/4.5890 L at 25 C.
- Piston/can reference values, slopes, rms speeds, kinetic energies and weighted lift recomputed in review-numbers.py/json. Piston area, weights, capacity, can cutoff and error ranges are specified model settings, not equipment ratings.
- [NGSS HS-PS3-2](https://www.nextgenscience.org/pe/hs-ps3-2-energy): students change a heated weighted piston and relate particle-motion energy to raised-weight position energy; the standard is practiced, not only named.

#### Sensitivity

None: ideal-gas apparatus and unpeopled landscapes, with no cultural, historical, religious or bodily content. All 11 images inspected; none contains a person, and each is marked people:false. No person is needed for this apparatus-only scene.

#### Flattest moment left

Repeating four temperature measurements in set B is still the slowest stretch, but it is the specified controlled replication. The former flat payoff is lifted: the result now sits beside the visible convergence, rather than covering it.

#### Graphics

All 11 assets inspected in their scene and/or final-sized files; ten strong assets retained, can redrawn once using the built-in image tool. Replacement prompt: art/prompts.json, raw: art/raw/gl-can.png, finished: art/gl-can.webp. Free art.py --rekey preserved alpha.
Finished art 611.36 KiB; final bundle 921.67 KiB. Compared the lab with the existing Beat Lab reference frame. No placeholder or missing art. Steel-sky brand/panel 9.87:1; brand ink 10.53:1; muted/panel 8.13:1.

#### Audit

One complete audit, Chrome 9961 / host 8765, within its 2400-second cap: `_scratch/gas-law-lab/review-audit/audit.md`. All 30 audit PNGs inspected in four sheets; no runtime errors, infinite motion or resize-stuck controls.

- 19 leads resolved: 1 disabled Fit instruction and 1 compact caption overlap fixed; 3 saved-row scroll notices retained; 2 iframe-reader/hint notices independently checked; 12 skipped/cut welcomes allowed by BASELINE rule 16, with instructions retained in hint/Read.
- Focused post-fix checks use the audit's measurement function, not a second audit. Can 680, welcome 1920 and hosted phone: no overlap, clipping, small targets, missing hints or disabled-control instruction. The 1920 saved-data scroll notice remains intentional.
- Every STANDARDS size checked: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, hosted 375x812. Grayscale, Motion off/on, keyboard-only 0/80 C recording and fit, live Record during warming, and all apparatus extremes checked. Current hint and main controls stay visible.
- Console clean in direct-file runs. Hosted runs additionally logged the test server's automatic favicon 404; no tool runtime exception or external resource request. Final proof: `REVIEW_FINAL_VALIDATION.json`; final hashes/line/art checks: `review-static.json`, both in Scratch.
- Closed the three exact gas-law-lab 8765 child hosts left by the LibreOffice launcher after verifying command, workspace and process identity. Ports 9960, 9961 and 8765 now refuse connections; host.html removed. No unrelated process touched.

#### Left open

- Spec names kit/particles.js and docs/families/particles.md, neither exists. Writes there are forbidden; the local independent particle picture remains documented in handoff.
- Spec says a gas-only change produces a different slope. Ideal-gas theory and tested data give the same slope; the truthful implementation remains, and the spec is unchanged.
- Browser-fallback timing is verified; final bank-voice recording quality remains untested because recording is outside this pass.
- Compact Notebook data rows scroll intentionally. Main experiment controls, readouts, current hints and fitted crossing remain available; recorded rows are not answer choices.
- Nitrogen PubChem access challenged; independent CIAAW values were used without asking the unattended user. No new feature, external outreach or git commit.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Gas Law Lab build handoff

#### Structure

`src.html` starts from the kit starter and uses `kit:curio` and `kit:theme-912`. Constants and the SI model come first,
then measurement/progress logic, the tool-local particle picture, responsive SVG apparatus/graph renderers and input
wiring. `__tool` exposes the specified API plus pure model/regression helpers and voice logs. Art tokens resolve to
all 11 generated WebP assets. Prompts and raw art are in `art/`; generated images are credited in tool.draft.json.

#### Tricky parts

- Physical units are SI internally, with volume displayed in mL or L and pressure in kPa. Use the exact weight increment.
- Guided sets require four distinct bath settings and use true temperatures to reject repeated-temperature and insufficient-span shortcuts; noisy readings are
  fitted without rounding. A set must keep one fixed recipe, and B changes exactly one factor. Stop rows do not qualify.
- Deleting current-set data invalidates its comparison; unrelated bench rows leave guided fits intact, and deleting B retains valid A.
  Clear resets the comparison. Every Record still saves a row, including a non-qualifying bench row.
- A gas-only change leaves the slope unchanged. The result card reports that case accurately.
- Can input is limited at the current gas temperature, then its bath is limited to the last safe whole degree.
- Graph axes must stay at T (°C) and V (mL) for guided completion. Bench supports all specified axis combinations.
- The short layout moves Real lab and Start again into the tab rail. Long notebook tables may scroll; primary controls stay put.
- The browser voice is the kit fallback. `voice/lines.json` specifies bank bright-teacher and voice Autonoe; no audio was recorded in Build.

#### Spec decisions and contradictions

- Open question: retain HS-PS3-2. Do not add an unrequested state standard; the gas laws lead into the particle/weight energy representation.
- The spec requests a new `docs/families/particles.md`, but the authorized write roots exclude docs. It was not written.
- `kit/particles.js` and its family doc are absent. The particle picture is implemented locally, not in kit. See Engine changes wanted.
- The spec says every second line has a different slope even if only the gas changes. Ideal gas theory says otherwise;
  recommend changing amount or weights and show a same-slope gas comparison honestly.
- The spec names local FLUX; the user's image-tool requirement wins. OpenAI gpt-image made all assets, with no people.
- Transparent glass had key-color artifacts on its first pass. It was regenerated with alpha, preserved through art.py --rekey.
- The build brief asks for an early codex-report.md while the user explicitly says to stop when it is written. The report
  was assembled in Scratch and copied to the tool only after the checks, so the user's stop boundary is respected.
- The spec's “R exact” is a rounded decimal representation of the exact N_A k product. The specified decimal is used consistently.

#### Sensitivity

No cultural, historical, bodily or people content. Model equipment is not a real apparatus safety certification.

#### Engine changes wanted

- `kit/particles.js`, new `Box` API: implement the family API listed in spec.md, including walls, heat-bath collisions,
  species, counts, still frames and picture-only hit counting. It does not exist in this checkout, so a faithful reuse
  is impossible. Promote only after the family has the required finished uses, per BASELINE rule 13.
  Required methods: `addSpecies`, `add`, `remove`, `setT`, `setWall`, `hits`, `meanKE`, `speedHist`, `count`, `frame`,
  `still`, `dissolve`; options include shape, dimensions, seed, bathCoupling, attract and zones. Sibling-only attraction
  and dissolving behavior was not added to this gas-law tool.
- `docs/families/particles.md`: document the actual promoted API and sibling contracts. This build has no authority to write docs.

#### Next work

Read codex-report.md for the original build and codex-review.md for the cold review. No git operation was performed.
Voice recording is still deferred; the review tested browser speech fallback timing, not the final Autonoe recordings.

#### Cold review repairs

- Clamp amount to the destination apparatus limit when switching from Can to Piston (0.0200 to 0.0100 mol).
- Graph crossings now use the selected x-axis unit, including kelvin. Celsius is no longer printed on every crossing.
- Experiment controls precede notebook row deletes in DOM order; explicit grid positions preserve the visual layout.
- Deleting an unrelated bench row preserves guided fits; deleting a B row preserves the valid A fit.
- The guided welcome specifies a total 60-degree span. Both the screen hint and Read remain available.
- Reversing compression or leaving the piston stop hushes the corresponding active line when its claim stops fitting.
- A queued zero-crossing event also checks the actual fit, selected axes and visible notebook, so Read cannot delay it into a different graph.
- Motion off synchronizes the rendered piston volume, preventing a stale position when Motion resumes after a temperature change.
- Balloon width reserves room for the largest allowed volume before applying cube-root scaling. This preserves area proportional
  to volume to the two-thirds power at narrow portrait widths, rather than flattening growth against a pixel cap.
- At laptop widths the result card leaves the lines' common crossing visible. It labels the real-gas extrapolation limit.
- gl-can was redrawn with the built-in OpenAI image tool and processed by art.py --rekey with its alpha preserved.
  Raw replacement: art/raw/gl-can.png. The full replacement prompt is in art/prompts.json; the old asset is in Scratch.
- Final audit: `_scratch/gas-law-lab/review-audit/audit.md`, one complete run, 19 leads. The early Fit instruction and
  compact can-caption overlap are fixed; focused checks are in `review-audit-fixes/`. Other leads are permitted first-tap
  welcome skips, recorded-data row scrolling, and the runner's iframe-context lookup gap. Hosted phone checks remain independent.

#### Validation and test environment

The original build audit is in `_scratch/gas-law-lab/audit/audit.md`; its 94 original leads are mapped to fixes or deliberate
tradeoffs in codex-report.md. Focused post-fix checks and `FINAL_VALIDATION.json` are in Scratch. The compact Notebook
table intentionally scrolls to data rows; Clear is always in its toolbar and Delete stays at the table edge.

The LibreOffice Python launcher left host child processes after the parent exited. Final cleanup matched only the
exact `scripts/drive.py gas-law-lab --host 8785` command, checked it again before stopping it, and verified that ports
9980, 9981 and 8785 were closed. No unrelated Python or Chrome process was targeted. `host.html` is removed.

The cold review's final validation is `_scratch/gas-law-lab/REVIEW_FINAL_VALIDATION.json`; final file hashes are in
`review-static.json`. Exact-command and workspace checks closed the three review host children on 8765; connection
refusal confirmed closure of 9960, 9961 and 8765. The final balloon frame check confirms the expected 1.233259 width
ratio from sea level to 5,000 m at 760 wide, as well as at 680 and 1366.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
