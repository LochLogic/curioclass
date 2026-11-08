# Codex report: zipline-energy

## Built

Build only, 2026-11-02, in S:/CurioClass-codex. No commits, branch changes, deployment or polish round.
Built Design, Ledger and Notebook with the ellipse cable, RK4 energy accounting, real-time rides, four-speed
three-rider tests, live edits, brake sounds, replay scrubber, stored ride table, mass plot and three earned briefs.
The draft bundle is 586,526 bytes, about 573 KiB. All required build files exist; host.html was removed.
All test Chrome instances and host servers were closed. Only the assigned Chrome ports and host 8775 were used.

## Numbers check

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

## Feel check

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

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

All retained PNGs were viewed directly or in labeled contact sheets. Audit: all 52 frames in audit-sheets/; repaired
and flagged layouts were also opened directly. Other groups: bar-frames, early-frames, fitted-frames,
functional-frames, sweep-design, sweep-ledger, sweep-notebook, focus-frames, phone-frames, play-frames,
final-frames, last-frames, repair-layout-frames, motion-fix-frames, phone-path and off-hint-frames.
Also viewed every finished WebP, art-sheet.png, bar-comparison.png and resize-after-repair.png.

## Art made

Seven used images, eight image-generation calls including one pine redraw. Art totals 334,352 bytes, about 327 KiB.
Final bundle: 586,526 bytes, about 573 KiB. Built-in imagegen made the valley, cliff, pine, platform, trolley, pad
and generator. art/prompts.json contains the prompts/provenance; raw PNGs are in art/raw/. Only art.py --rekey packed them.
Cutout holes/despill processing removed the dominant key-color residue. No generated image contains a person.

## Art still to paint

Six rider cutouts, three masses in two postures, await the owner and approved painter. Wire the retained RIDER_ART
tokens into rider() and silhouetteIcon() after review. No unspecified fourteenth asset was invented.

## Engine changes wanted

None. Shared kit, engines and documentation were not edited.

## Left open

- Six rider paintings and owner review; the tool deliberately remains a draft.
- Narrow scrolling and compact slider target height against the strongest STANDARDS reading.
- Recorded narration was prohibited. The 16-line inventory uses big-sister/Leda, but playback currently uses browser speech.
- Human listening, a real school-laptop performance check and real-student 30-to-45-minute use remain unverified.
- Scope mistake: the required bar check regenerated the ignored snowy-mail-route and beat-lab HTML bundles outside
  the user's two write folders. Their source files were untouched. This is also recorded in handoff.md.
- The report was written at completion, following the user's instruction to stop as soon as it is written.
