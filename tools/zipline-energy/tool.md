# Zipline Energy: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: zipline-energy

#### Built

Build only, 2026-11-02, in S:/CurioClass-codex. No commits, branch changes, deployment or polish round.
Built Design, Ledger and Notebook with the ellipse cable, RK4 energy accounting, real-time rides, four-speed
three-rider tests, live edits, brake sounds, replay scrubber, stored ride table, mass plot and three earned briefs.
The draft bundle is 586,526 bytes, about 573 KiB. All required build files exist; host.html was removed.
All test Chrome instances and host servers were closed. Only the assigned Chrome ports and host 8775 were used.

#### Numbers check

Evidence is in S:/CurioClass-codex/_scratch/zipline-energy/: physics_check.py, numbers.json, more-numbers.json
and browser-numbers.json. Geometry, reference rides, boundary settings and challenge ranges were recomputed.
Anchor distance 301.4963 m; cable length 302.1589 m; start height 42.13999 m; lowest height 11.97224 m.
Default 70 kg pad 800: zone 11.31547 m/s, stop 281.35244 m, peak 1.23909 g, time 24.38764 s.
Default generator 70: battery 3,292.72655 J, or 0.91465 Wh. All three riders pass.
No brake, 70 kg: edge 9.05113 m/s; rolling 3,030.35 J; drag 14,065.26 J; motion about 2,867 J.
The 19,963 J in that example is height energy lost, not the starting column total, which is about 20,716 J.
The ledger retains the remaining height energy. It does not silently change its total or zero reference.
Friction-off zone speed is 24.32806 m/s for every mass. Tree 30 m stalls 35 kg at 266.33174 m.
The swept passing ranges reproduce Z1, Z2 and Z3, including Z3 generator 50's marginal stop.
Minor reference differences: pad work for 70 kg is 4,282.28 J rather than the illustrative 4,285 J.
The calculated ledger closes well within 0.2%; numbers were not fitted to the examples. The spec was unchanged.
The Art section says 14 images but lists 13 names: seven objects/backgrounds and six riders.

#### Feel check

Played the whole default ride, failing pad batch, successful generator batch, ledger and notebook, then all three
briefs using held clicks, native select keys, slider keys and a real scrubber drag. The earned record held 16 rides.
Best moment: the heavy rider stops just inside the edge while the light rider also stays under 1.5 g, earning Z1.
First flat moment: the right-hand lab felt empty while a ride ran. Added large painted brake hardware with its
force rule, alongside the live speed readout and trace, so the selected mechanism has a visible presence.
Second flat moment: a failed batch ended with the last rider's pass banner. Replaced that with a whole-design
verdict and the specific failed rider's measurement. The successful batch now says all three riders are safe.
Compared the rich valley, layered cable and hardware with Beat Lab's instrument finish. The scene is not plain;
the remaining silhouette riders are a visible draft limitation. The comparison predates the final narrow-layout repairs.

![Zipline Energy beside Beat Lab](S:/CurioClass-codex/_scratch/zipline-energy/bar-comparison.png)

#### Done when

1. PASS: default 70 kg pad 800 gives 11.32 m/s, 281.4 m and 1.24 g; all rules tick. final-frames and browser numbers.
2. PASS: pad 800 fails 35 kg at 2.39 g; generator 70 passes all three. The pass event started four times in play-results.json.
3. PASS: no-brake edge arrival is 9.05 m/s with the edge narration and the computed ledger values above.
4. PASS: all three friction-off zone speeds are 24.32806 m/s, also confirmed through actual phone scrolling and input.
5. PASS: the 35 kg, 30 m anchor ride stalls at 266.3 m and starts the stall event. final-stall-log.json.
6. PASS: the completed 70 kg generator ledger displays 3,293 J and 0.91 Wh, with a conserved total. final-ledger70.png.
7. PASS: default friction points rise 6.79, 11.32, 14.76; friction-off points form one flat line. Mode/size frames.
8. PASS: Design's valley dominates at 1366 and 680; Ledger's energy column occupies the full available height.
9. PASS: a real sag drag cancels a running ride, clears ghosts and redraws; posture changes the silhouette immediately.
10. PASS: how-to speech is once per load, events repeat, Read has priority, and the Design welcome stays stale after Ride.
11. FAIL: seven named non-person images are painted and used; six owner-reviewed rider paintings are pending.
    The source retains their art tokens and uses silhouettes. The spec's fourteenth image is not named.
12. PASS for its stated layout/content checks: all modes at all STANDARDS sizes were viewed, including a real 375-wide
    iframe. Layouts stack at 760/375; preview text is at least 10 px; the tool has no network requests or em dashes.
    This does not mean every narrow-screen setting is simultaneously visible; see Wave lessons and Left open.

#### Wave lessons

- Hint and voice: PASS. Immediate state hints, Curio.voice, V.heard, stale guards and held 2-second tap checks.
- Focus and layout: PASS after repair. Persistent controls retain focus; the narrow hint now has reserved space.
- Sizes: FAIL against the strict target/visibility rule. Buttons are 44 px or more, but compact sliders are 27 px tall
  with wide hit areas, and narrow settings require scrolling. The scene was not reduced to fit every setting at once.
- No giveaways: PASS. Safety results appear after testing, not while sweeping a parameter. Iteration is the lesson.
- Honest numbers: PASS. Lab assumptions and omitted effects are on screen; near-edge stops retain extra precision.
- Standards: PASS. Students compute/account for energy, compare forms and design against conversion-device constraints.
- Motion off: PASS. Explicit glint stop; zero running animations. Physical duration and numerical results are preserved.
- Short choices in view: FAIL in the narrow stacked layouts. All choices remain reachable in the content viewport.
- Resize during action: PASS. Audit clean; after the viewport repair a ride survived 760, 1366 and 680 resizes, then canceled on a real drag.
- Late welcome: PASS. No welcomeAfter; hasRidden and visibility guards prevent a delayed Design welcome.
- Unknown shown as unknown: PASS. Untested lab measurements show placeholders rather than invented ticks.
- One look, one meaning: PASS. Distinct energy labels, trace dash patterns, and explicit ticks/crosses accompany color.
- Badge truth: PASS. Batch verdict uses all three results; friction-off rides receive no lab verdict.
- Hint changes back: PASS. Mode switches, edits, reset and completed what-if batches restore fitting next actions.
- No word-copy answer: PASS. Students must run a physical design; Compare is an explanation aid after evidence collection.

#### Audit leads

Ran audit_tool.py once, last among the broad checks, with a 40-minute limit. It completed in about 25 minutes:
S:/CurioClass-codex/_scratch/zipline-energy/audit/audit.md, 85 leads, 52 saved frames. No second full audit was run.
Every lead is covered by the following groups; many repeat the same narrow-layout issue across states.

- Brake-label/200 m overlaps at 680, 375 and slider extremes: fixed by moving the annotation above the cable.
  Rechecked in repair-layout-frames and phone-path frames.
- Hint overlaps with settings, ledger paragraphs, conclusion or its label: fixed by a reserved footer outside the
  scrolling mode content. Rechecked at 680, 1366, 760 and 375. Nothing scrolls behind the hint now.
- Conclusion has no name, both notebook states at every size: added an explicit aria-label, retaining the visible label.
- All below-fold settings and Compare/conclusion leads at 760/375: reachable by scrolling, but the strict simultaneous
  visibility requirement remains open. The hint explicitly says when to scroll up or down.
- Phone generator/friction clicks lost focus or exercised the pad: fixture clicks had targeted off-screen coordinates.
  Added viewport navigation to audit-states.json. Actual wheel input and held clicks subsequently verified generator
  70 passing all three and friction-off giving three equal zone speeds. See phone-path-first-results.json and
  phone-path-results.json. An initial off fixture missed Test; the narrower retry asserts three completed results.
- Cards overlay covers scene text, settings and the background hint: intentional native modal behavior. The select
  and Back to design stay visible; closing returns focus without scrolling. Its first tap now suppresses Design speech.
- Ride/Test first-tap welcomes not heard: intentional per the spec's welcome-stale-on-Ride rule and first-action priority.
  The scene and rules supply the premise; no late welcome interrupts a ride. stale-welcome.json verifies this.
- Quick repeated Reset cuts welcome: accepted because Reset explicitly hushes narration. The current hint and Read remain available.
- Sound moves four header controls when its label changes: kit label behavior; scene/settings stay put and focus is retained.
- Motion-off and resize sections were clean. Added a stronger explicit animation stop and rechecked zero running animations.
- The audit server logged a client connection reset while a tab closed. The audit completed; this was harness stderr,
  not a tool JavaScript exception. The actual student-path log has no runtime errors or resource requests.

The audit predates the footer, annotation, accessible-name, modal/phone hint and final what-if-hint repairs.
Only affected layouts and interactions were rechecked afterward. This is not a second full audit or a cold review.

#### Frames looked at

All retained PNGs were viewed directly or in labeled contact sheets. Audit: all 52 frames in audit-sheets/; repaired
and flagged layouts were also opened directly. Other groups: bar-frames, early-frames, fitted-frames,
functional-frames, sweep-design, sweep-ledger, sweep-notebook, focus-frames, phone-frames, play-frames,
final-frames, last-frames, repair-layout-frames, motion-fix-frames, phone-path and off-hint-frames.
Also viewed every finished WebP, art-sheet.png, bar-comparison.png and resize-after-repair.png.

#### Art made

Seven used images, eight image-generation calls including one pine redraw. Art totals 334,352 bytes, about 327 KiB.
Final bundle: 586,526 bytes, about 573 KiB. Built-in imagegen made the valley, cliff, pine, platform, trolley, pad
and generator. art/prompts.json contains the prompts/provenance; raw PNGs are in art/raw/. Only art.py --rekey packed them.
Cutout holes/despill processing removed the dominant key-color residue. No generated image contains a person.

#### Art still to paint

Six rider cutouts, three masses in two postures, await the owner and approved painter. Wire the retained RIDER_ART
tokens into rider() and silhouetteIcon() after review. No unspecified fourteenth asset was invented.

#### Engine changes wanted

None. Shared kit, engines and documentation were not edited.

#### Left open

- Six rider paintings and owner review; the tool deliberately remains a draft.
- Narrow scrolling and compact slider target height against the strongest STANDARDS reading.
- Recorded narration was prohibited. The 16-line inventory uses big-sister/Leda, but playback currently uses browser speech.
- Human listening, a real school-laptop performance check and real-student 30-to-45-minute use remain unverified.
- Scope mistake: the required bar check regenerated the ignored snowy-mail-route and beat-lab HTML bundles outside
  the user's two write folders. Their source files were untouched. This is also recorded in handoff.md.
- The report was written at completion, following the user's instruction to stop as soon as it is written.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: zipline-energy

#### Played

Cold Grade 11 solo run and projected-classroom view: Ride, failing Pad batch, Generator batch, Ledger scrub,
Notebook comparison and all three briefs. Played before opening builder notes or source. Strong place, credible consequences.
One review pass in S:/CurioClass-codex; no commits. Evidence paths below are relative to _scratch/zipline-energy/.

#### Findings fixed

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

#### Findings left

- Should fix, general, spec scope: HS-PS3-1 asks students to create a computational model; HS-PS3-3 includes building a physical device.
  This supplied simulation supports parts of both. Notes now say so; catalog/spec remapping is outside these write folders.
- Polish, general, spec constraint: Generator 70 works unchanged for Z1, Z2 and Z3. The actual shortcut was run and succeeds.
  Those are explicitly valid spec answers. The cards verify a physical design, and cannot establish conceptual mastery.
- Cory's personal review of the six people images is pending. They remain draft art, with people:true and owner_review:pending.

#### Break it

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

#### Voice walk

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

#### Facts checked

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

#### Sensitivity

People/body-size representation needs review: varied skin tones, ages and gender, both postures fully clothed and harnessed.
The mass labels are test inputs, not a rule for guessing weight from appearance. No cultural, Indigenous, religious or hard-history content.
The contact sheet is review-art-sheet.png; Cory's personal art approval is not asserted.

#### Flattest moment left

The approximately 24-second default solo ride has a quiet middle. Real-time playback is prescribed; the live speed,
trace, painted rider and visible brake preserve its purpose. Notebook's former flat explanation is now personal evidence.

#### Graphics

All 13 named images checked as finished WebPs, on a contact sheet and in use; six new people cutouts, no discarded strong art.
Prompts/provenance: art/prompts.json; generated with built-in imagegen, packed only with art.py --rekey.
Final assets: tools/zipline-energy/art/zl-rider-*.webp, originals in art/raw/. Art 388.45 KiB; bundle 675,332 bytes (659.50 KiB).
Compared with retained Beat Lab and Snowy Mail Route reference frames. The spec says 14 images but names 13.
Recomputed contrast: brand/panel 9.60:1, brand/secondary 9.10:1, button text/brand 10.07:1; segment labels at least 7.40:1.

#### Audit

Completed once within 40 minutes: 23 leads, 55 frames, all viewed; review-audit/audit.md and review-audit-sheets/.
Ten layout leads fixed and re-shot. Five modal-coverage leads are intentional; three first-tap skips and five rapid cuts follow BASELINE 16.
Resize had no exceptions or stuck controls. Post-a/post-b frames, final voice walk and cheat reruns verify repairs; no second audit.

#### Left open

No spec, shared kit, scripts or catalog edits; no commits. Lab settings and people were retained as the current brief directs.
The full parameter sweep exceeded the driver limit; one smaller boundary retry completed. No second audit will run.
Initial small document/memory reads used the tool yield limit rather than a hard kill; later commands enforce hard timeouts.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Zipline Energy: build handoff

#### Cold review update, 2026-11-08

This section supersedes the historical build limitations below. One cold review pass preserved the painted valley,
physics, real-time single rides and four-speed batches. Evidence is under _scratch/zipline-energy/review-*.
All design sliders now have 44 px targets. The stacked Design deck keeps the stage, Ride/Test, lab rows and every
short choice in view at 760x900 and in a real 375x812 iframe. Compact sliders use inline labels to preserve the scene.
The small-stage slogan is omitted where it collided with the scale annotation; the scale itself stays labeled.
The audit confirmed crowded phone height ticks, a compact result-text clip and narrow Notebook choices below the fold.
The phone uses fewer height ticks. Short-screen lab spacing reserves both lines of result text. Notebook now keeps
its conclusion/Compare area in a fixed lower deck and Copy/Clear outside the plot/table scroller. Comparison evidence
appears in the main notebook body and scrolls into view while all four controls remain reachable on screen.
Energy tower segments have direct labels for grayscale use. Near-edge stops cannot round up to a ticked 296.000 m.

Six rider cutouts were generated with built-in imagegen, packed only with art.py --rekey, and wired into rider()
and the mass buttons. The trolley still rotates independently; upright and tucked people hang from its attachment.
All people assets carry people:true. The final contact sheet is _scratch/zipline-energy/review-art-sheet.png.
These are review candidates, not a claim of Cory's personal approval. No live publication or recording was performed.

Compare no longer supplies a canned conclusion to an empty box. It requires completed three-mass results for both
brakes with matching cable, trolley and posture and one internally consistent setting per brake. It then shows the
student's actual stop and peak-g measurements for self-review. It never grades prose. The reflection is neutral
about which brake performed better at the student's chosen strengths. Design edits clear stale comparison evidence.
Edits, new runs and opening Cards hush old speech. Cards cancels an active ride before taking focus.
The ellipse citation was corrected from the spec's obsolete 8.1 URL to current OpenStax Precalculus 2e 10.1.
The lab-rule label is visible in Design; the values remain stated assumptions rather than industry safety standards.
All 29 fixed spoken strings include Read-only hints and the three brief instructions in voice/lines.json and allLines().
Clearing Notebook removes comparison evidence and fallback copy text as well as saved rows, retaining earned briefs.
Free design restores its own modal description rather than retaining the previous brief's wording.

The final mechanical audit completed once, within its 40-minute cap, with 23 leads and 55 frames. Ten layout leads
were repaired and re-shot; five native-modal coverage leads are intentional, and three first-tap welcome skips plus
five rapid welcome cuts are permitted by BASELINE 16. Resize stress had no exceptions or stranded disabled controls.
Final evidence: review-post-a/ (eight Notebook sizes, phone scale, both compact result messages), review-post-b/
(filled comparisons at phone/680, marginal stopping label, stall-label clearance, voice inventory and Free design),
and review-walk/ (actual main voice path, five repeated successes, Read with Sound off, Clear and cheat reruns).
All four Notebook controls passed visibility and center hit tests at all eight sizes and after showing comparisons.
No second full review or audit was run. The remaining spec/standards scope limits are named in codex-review.md.

The standards note now distinguishes using a supplied computational model from creating one (HS-PS3-1), and a
simulated device from the physical construction required by HS-PS3-3. Changing catalog standards is outside the
reviewer's write scope and would alter the spec. Review those mappings before claiming complete assessment.

#### Sensitivity

Review the new rider set for respectful representation across body builds, skin tones, age and gender. The fixed
mass labels are experimental inputs, not a way to infer a person's mass from appearance. All six figures are fully
clothed, helmeted and harnessed; there is no injury depiction. Cory's personal people-art contact-sheet review is
still pending. There is no cultural, religious, Indigenous or hard-history content.

Build only, 2026-11-02. No commits, branch changes, deployment, recordings or polish round.

#### Source and structure

src.html starts from the kit starter and remains the editable source. The generated zipline-energy.html is the offline
draft bundle. CSS defines wide, short-screen instrument-deck and narrow stacked layouts. The SVG scene uses its real
pixel dimensions. Curio Class kit owns Motion, Sound, Read and the narration queue. kit/graphing.js Plane draws the
speed trace and mass comparison plot. The local script owns ellipse geometry, energy integration, ride playback,
braking sounds, lab results, ledger, persistence, challenge cards and input handlers.

#### Physics and tricky parts

The lower rotated ellipse has the anchors as foci. Its semi-major axis is sqrt(b² + c²). RK4 integrates u = v²
in x, multiplying work by ds/dx. Each path step is at most 0.008 m, and a step ends exactly at the brake boundary.
The final zero-speed crossing is interpolated. Work is integrated alongside u rather than inferred from a residual.
The ledger measures height from the exact lowest point and splits generator work 80/20 into battery/heat.
Physical time comes from 2 ds / (v_before + v_after). Display samples are retained roughly every 0.24 m.
The speed plot and scrubber interpolate those samples, not a fitted trajectory. Numerical results are never fitted
to the spec's reference rows. Tiny differences in rounded brake work are expected; see Scratch numbers files.

Changing a control cancels every active rider, clears ghosts and redraws in the input handler. Test all three
launches at two-second intervals at 4x. A single ride uses physical time. Motion off retains duration and uses still
launch, brake-entry and finish poses. The trolley rotates to the rendered cable slope; the silhouette hangs vertically.
Riders are five times physical scale; extreme cable settings expand the vertical axis to keep them in the picture.
The platform's deck follows y(296), rather than the tree anchor focus. An edge arrival retains its approach speed
for the failure measurement while its drawn trolley rests against the padded bumper.

The simulation cache is keyed by the whole design and mass. Notebook entries are plain snapshots, not live references.
localStorage curio-zipline-energy contains completed rides and passed briefs, guarded with try/catch. The conclusion
is unsaved. A quota failure leaves new rides in session memory and shows that persistence is unavailable.
Copy table uses the clipboard when available and reveals selectable text otherwise. Clear notebook preserves earned
briefs. Numbers very near the platform use three decimals so a 5 mm margin does not display as a false edge arrival.

#### Open questions settled for this build

- Keep 1.5 g, 1 m/s, drag areas, rolling friction and battery share as explicit lab settings. Do not claim an ASTM
  standard or suitability for constructing or operating a real zipline. The screen and notes label the assumptions.
- Keep the six rider paintings and the Upright/Tuck distinction. Do not substitute weighted test bags. The user
  forbids generated people: prompts retain people:true and art tokens, while tasteful code silhouettes are used.
  The owner can commission and review the six paintings later.
- The spec says 14 images but names seven non-person assets and six riders, a total of 13. All seven non-person
  assets were generated here. No unspecified fourteenth image was invented; Done when 11 remains incomplete.

#### Art and voice

Seven images in art/ were generated with the built-in imagegen tool during this build. art/prompts.json records the
house style, prompts, drawn_by:codex and provenance. Raw originals are in art/raw/. Only art.py --rekey processed them.
The pine was redrawn once, and holes/despill options removed green/magenta residue from cutouts. All seven were
viewed at output size and in the scene. No generated image contains a person. Six rider paintings remain pending.
Wire approved RIDER_ART cutouts into rider() and silhouetteIcon() after review; they currently retain tokens while drawing silhouettes.

voice/lines.json selects big-sister / Leda and contains every allLines string. No audio was recorded. Fixed speech
falls back to the browser voice, so the selected recording-bank voice cannot yet be heard. Pad hiss, speed-linked
zip and generator whine are synthesized, follow Sound and start only with a gesture. Chrome tests were muted;
human listening and a real school-laptop performance check remain useful next review work.

#### Verification evidence

Everything made for checks is in _scratch/zipline-energy/. physics_check.py and numbers.json recompute geometry,
the reference rows and Z1/Z2/Z3 passing ranges. more-numbers.json covers worn/tuck and limiting brake settings.
browser-numbers.json independently matches the browser outputs to those calculations. The .008 m step improves
energy closure relative to the rounded reference: 70 kg pad work is 4,282.28 J, not the illustrative 4,285 J.

The student-path check used held clicks, real native select keys, real slider keys and a real scrubber drag.
It completed Z1 with generator 70, Z2 with pad 350, and Z3 with generator 70, saving 16 rides. play-results.json
contains the measured results, voice log and zero runtime errors or network requests. How line three started once;
the pass event started four times. Later build repairs corrected the late Design welcome, the batch result banner,
cutout spill and notebook width. These receive targeted checks, not a second full review.

The full size sweep was shot once for Design, Ledger and Notebook at all seven desktop/portrait sizes. A real
375-wide iframe was tested on host 8775. Only affected layouts were re-shot after repairs. Screenshots, profiles,
console/voice logs and the bar comparison are under Scratch. The phone's primary Ride/Test controls and lab card
stay visible; the stacked settings scroll inside the mode content viewport, above a separately reserved hint footer.
The footer cannot cover settings or notebook text. Long notebook tables scroll horizontally.
This is an explicit limit against the strongest every-control-in-view reading of STANDARDS.

The one mechanical audit completed in about 25 minutes with 85 leads. Most repeat narrow scrolling and the former
sticky-footer overlap. The footer now has reserved space, the brake annotation is above the cable, and the conclusion
has an explicit accessible name. Fixture scroll navigation was corrected. Phone generator and friction-off paths
were then exercised with real wheel input and held clicks. Generator passed all three; friction-off speeds were
24.328 m/s for all three. A first phone fixture accidentally missed Test; the corrected narrower rerun asserts
three completed results. Both records remain in Scratch, so use phone-path-results.json for the final friction check.

Motion off was checked after an explicit glint stop: zero running animations, same 24.3876-second default ride and
281.352 m stop. After the viewport repair, a live ride survived 760x900, 1366x768 and 680x425 resizes, then a real
sag drag canceled it with no exceptions. There was no second full audit. All audit frames were viewed in labeled
contact sheets; repaired layouts and the final interaction frames were also viewed directly.
The completed friction-off batch now offers Ledger or another Ride rather than leaving a running-state hint.
off-hint-confirm.json verifies that idle hint, all three 24.328 m/s zone speeds and all 16 voice inventory lines.

#### Engine changes wanted

None. No kit, family engine or shared documentation was edited.

#### Build limits and scope note

- Six people paintings and their owner review are pending. The source remains tool.draft.json.
- Recorded narration was prohibited. Browser voice and synthesized audio need a human listening check.
- This build is followed by a cold review, not a polish round here. See codex-report.md for final audit leads.
- CODEX-BUILD asked for bar bundles before building. I ran the two named bar bundlers, regenerating their ignored
  HTML bundles outside the user's two write folders. This was a scope mistake; their source files were not edited.
- The report is written at completion because the user's final instruction says to stop as soon as it is written.
  In-progress evidence stayed in Scratch rather than an early tool report.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
