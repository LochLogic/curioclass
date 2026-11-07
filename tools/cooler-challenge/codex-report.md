# Codex report: cooler-challenge

## Built

Build only in S:/CurioClass-codex. No commits, deployment or separate polish round.
Built both Grade 6 modes from the starter: layered lunchbox design, three live heat paths, animated tests,
ghost comparisons, a paged test log, the engineer's check and local note, plus three fair investigations.
The readable source is src.html; cooler-challenge.html is the single offline bundle; tool.draft.json has stage built.
Required teacher notes, voice manifest, audit states, all painted art and handoff are present.
The report was assembled early in Scratch, then written here last to honor the user's explicit stop condition.

## Numbers check

Independent Python: _scratch/cooler-challenge/verified-numbers.json, verify_numbers.py and fair-pairs.json.
All 3,450 unique boxes: 31 pass within $8, 46 at any price, 5 budgeted passes without a seal, 4 with black cloth.
No steel/fridge mixture passes. There are 82 near misses from 200 to 239 minutes. Two-second steps flip no verdict.
All 24 Bench settings and all 48 eligible fair pairs support their stated claims. Range: -14.3 to 130.7 °C.
The 100 g freezer-water High run reaches its plateau at 18.45 min. JS/Python anchor lunch temperatures agree to 9e-16 °C.

| Anchor | Computed cold until | Spec |
|---|---|---|
| Bare | 8:00, ends 55.54 °C | agrees |
| One frozen bottle, bare | 8:04 | agrees |
| Four bottles, bare | 8:18 | agrees |
| Four bottles, foil, seal | 8:58 | says 8:57 |
| Two foam, seal, no packs | 8:02 | agrees |
| Three foam, foil, seal, no packs | 8:03, ends 45.90 °C | agrees |
| Two foam, seal, two frozen bottles | 11:26 | agrees |
| Same plus foil | 11:49 | says 11:48 |
| Two foam, two frozen bottles, no seal | 10:45 | agrees |
| Two foam, seal, three frozen bottles | noon, $8 | agrees |
| Two foam, foil, seal, three steel packs | 8:14 | agrees |
| Same with three fridge bottles | 8:05 | agrees |
| Cotton, cardboard, seal, three frozen bottles | noon, $6 | agrees |

Use exactly 80 °F outside, not literal 27 °C: this matches the specified 49.4 °C peak and all enumeration counts.
The two foil minutes remain discrepancies; constants were not fitted. The noon $8 box is about 81 percent melted,
so it correctly uses mostly-melted art rather than the incompatible half-melted picture in Done when 1.
Contrast: ink/paper 14.80, muted/white 6.22, white/brand 6.49, pack blue/cold zone 4.76, brand/cold zone 5.41.

## Facts checked

Each data readout comes from the stated model, independently recalculated above. Costs and limits are game assumptions.

| Student-facing fact | Named source checked |
|---|---|
| Keep perishables cold; use at least two cold sources | USDA FSIS, How do you keep a bag lunch safe?, updated March 7, 2025 |
| Fridge at 40 °F or below; freezer about -18 °C | FDA, Are You Storing Food Safely? |
| Job uses 4 °C, approximately 40 °F | FDA guidance; notes explain the conservative Celsius rounding |
| A sunny parked car warms rapidly, even on mild days | McLaren, Null and Quinn, Pediatrics 2005, PubMed PMID 15995010 |
| About 40 °F rise in an hour, most in the first half-hour | Same study; the exact interpolated curve is the spec's scenario model |
| Never leave a person or pet inside a parked car, in notes | National Weather Service, Heat Safety, weather.gov/ohx/heat |
| Conduction, convection and radiation; insulation slows transfer | DOE Building Science Education, Heat Flow; NGSS MS-PS3-3 |
| Heat goes from warmer to cooler, including arrows reversing | NGSS MS-PS3-3, PS3.B; explicit model flow signs independently checked |
| Ice melts at zero while accepting heat; water's melting heat | OpenStax College Physics 2e 14.3, Phase Change and Latent Heat |
| Matter, mass and heating affect temperature change | OpenStax 14.2, Temperature Change and Heat Capacity; 48 computed fair pairs |
| Shiny reflectors absorb less radiation than dark surfaces | OpenStax 14.7, Radiation; particular absorptances are labeled model settings |
| Temperature measures average particle kinetic motion | NGSS MS-PS3-3/4 disciplinary ideas; OpenStax chapter 13 |
| Wall bars compare resistance per 10 mm in this model | Spec Content; DOE's resistance principle, not a universal ranking of products |
| MS-PS3-3 and MS-PS3-4 are taught through student actions | Official NGSS performance expectations; no energy calculation task |

Direct primary links are in notes.md. The older DOE Energy Saver page returned 404, so the current DOE Heat Flow page was checked.
The FSIS handout returned 403; its current official Q&A and USDA's August 2025 lunch-safety release confirm the guidance.
Specific heats 4.18, 2.05 and 0.47 are the spec's approximations, not exact copies of OpenStax's table.

## Break it

- Build: independently tried every legal box. Walls only, packs only, steel and fridge substitutions fail as stated.
  The over-budget $9 design stays cold but never earns Job done. Skip evaluates the whole model and cannot run before Run.
- Limits: fourth wall/fifth pack refused. Four packs block a second layer; three layers allow only two packs.
  Real held clicks confirmed no partial insertion, negative costs or hidden extra pack.
- Engineer: selected a wrong answer, then swept every option. The first result stayed wrong. Choices shuffle and have comparable lengths.
- Bench: identical, wrong-variable and multi-variable plans refused. A fair plan locks settings; edits cannot change a running plan.
  First-attempt fairness is recorded separately from the claim. Prediction and the note are unscored.
- Claim: selected the common wrong mass claim, swept all four options and revisited it. No upgrade to the first answer.
  Correct and corrected marks remain distinct. All three claims require tying a variable to the plotted changes.
- Skip permits fast physical trial and error despite the spec's estimate using full-length runs. Job done measures
  a model design; the separate engineer check assesses an explanation. Guessing has one-in-four odds per question. It cannot be eliminated by tapping all options for free.
- A held pack removal during a run is checked after preserving pointer identity across SVG redraws.
  Keyboard focus is restored during redraws and moves purposefully when the next step replaces a control.

## Voice walk

Main path: play/checks.json and voice-walk.json, real 120 ms holds at a two-second tap pace, default Sound.
Heard: wBuild, run1, flat, short, pass, check, wrong, right, note, restart, passOver, wBench,
unfair three times for distinct plan attempts, fair, predict, runB, claim, wrong, fair, right,
fair, runEnergy, right, benchDone. Repeated how lines were silent; events repeated; no main-path cuts.
Both welcomes, all main mode instructions and the unequal-heating instruction were heard in the relevant state.
Side path: Sound off, Read, Sound on, Bench, Energy. Read protected its hint; mode change dropped the obsolete queued welcome.
Current Read also includes the job constraints before the first Build run. Final fixed-line count: 33.
Achird / friendly-dad recording direction is preserved. No audio was recorded in Build; browser speech is used.

## Feel check

Played a full scripted student-style session through near miss, revision, engineer questions/note and all three investigations.
Best moment: the third bottle holds lunch to noon while the previous 11:26 curve rises as a ghost and the ice stays at zero.
Flattest moment 1: a worksheet-like Bench and cups sitting beside the painted plates. Fixed plate alignment, glass transparency,
live heat bars and the locked-plan summary, with different physical questions for the later investigations.
Flattest moment 2: compact results squeezed the graph and phone results sat below the viewport. Fixed action placement,
compact result headings and a phone test layout that prioritizes the graph alongside the controls.
Bar tools were bundled into Scratch and opened before building. Both reference frames were inspected.
bar-comparison.png puts the earned result beside Beat Lab at matching proportions. The painted place and layered box
have comparable finish; this tool deliberately has fewer controls. This is an agent play check, not a human usability study.

## Done when

1. FAIL at the literal half-melted picture; PASS for 11:26, noon at $8, flat zero line and physically correct remaining ice.
2. PASS: foil reduces solar flow, seal reduces the air path, all foam layers reduce conduction; the bare-box arrow reverses.
3. FAIL for two exact foil minutes, reported above. PASS for the other anchors, steel/fridge failures and budget enforcement.
4. PASS: qualifying run opens the two one-attempt questions; shuffled choices, first scores and device-only note checked.
5. PASS: all invalid plans rejected, valid plan locked, equal bars for Mass/Matter; Energy honestly differs.
6. PASS: all three supported claims verified, first wrong answer retained and corrected, final investigation line heard.
7. PASS: a design edit stops/restarts at 8:00 with a ghost; Bench Change plan or another question acts immediately.
8. PASS: school-laptop Build controls and plot fit; 680x425 stays side by side and uses Log; phone test/results are rechecked.
9. PASS within browser-fallback testing: how lines once, events whole, current hints and protected Read; recordings remain unmade.
10. PASS: no people or animals in any of 19 paintings, no runtime HTTP requests and no console errors in the play and frame runs.

## Wave lessons

- Hint/voice: PASS, live hints update independently of speech; main/side logs include Read and both mode welcomes.
- Focus/layout: PASS after focused fixes for Run, Skip, Check plan, claims, pack redraws and the changing plan.
- Sizes/44 px targets: PASS in the required size pass and focused fixes, including the real 375 px iframe.
- No giveaways: PASS, shuffled balanced claims, distinct first-answer records, no free correction score or prediction score.
- Honest numbers: PASS, game prices/model assumptions stated; independent 3,450-box and 48-pair checks retained.
- Standards: PASS, both codes are taught by solo design/investigation actions; no family engine applies.
- Motion off: PASS, full 24-second run, no active animations, still state changes and no placeholder art.
- Short choice sets: PASS after locked/answered layouts fold; current choices remain in view.
- Resize mid-animation: PASS in the specific Bench resize and final audit stress evidence, subject to audit result below.
- Delayed welcome: PASS, no welcomeAfter. Run can skip the welcome under BASELINE 16; premise stays in hint, job and Read.
- Unknown stays unknown: PASS, no future result or correctness appears before the test/claim.
- One look/one meaning: PASS, labeled solid/dashed/dotted lines and separate A/B endpoints, including close endpoints.
- Badges say what is true: PASS, edited/over-budget designs show no stale Job done; corrected first answers remain marked.
- Hints change back: PASS, returning to a locked Bench plan names prediction/Run, not disabled settings.
- No copying answer words from a clue: PASS, pre-answer hints name actions and graphs; explanatory answers appear after a locked attempt.

## Audit leads

Completed once, with 31 pre-fix leads. Every lead is accounted for in these groups:

- 2 scene-label overlaps: fixed by hiding the decorative label in a compact cutaway; phone and 760 px checks are clean.
- 8 focus leads: Run/Skip retain focus through guarded aria-disabled states; Check plan focuses prediction;
  Bench Run moves to the claim after testing. Includes repeated bare-result, engineer and single-click leads.
  Keyboard-only Tab/Enter twice, held removal and the new Bench path pass in post-checks.json.
- 4 compact y-label overlaps: fixed by reclaiming graph height. fixed-result-680 shows distinct labels.
- 1 phone verdict outside the viewport: fixed by folding the car during testing/results. phone-build-result is clean.
- 1 full-wall caption overlap: moved caption for short layouts. fixed-caption-1000 is clean.
- 4 pack target overlaps: smaller pictures and separated 44 px hit targets. fixed-four-packs-680 is clean;
  phone-four-packs also verifies four non-overlapping 44 px targets. Held removal preserves live pointer identity.
- 9 covered-background leads: 8 scene/graph elements and the hint are intentionally behind the modal engineer dialog.
  The dialog is fully readable; engineer-answer-680 confirms focus on Next and the selected answer/correction fit.
- 2 welcome leads: Run replaces the welcome with its how-to; a second Reset intentionally hushes the first welcome.
  BASELINE 16 permits this. No delayed welcome; premise and constraints remain in the hint, job card and explicit Read.

Motion-off, five-tap repeats and resize stress were clean in the full audit. The original audit is retained unchanged.
Focused post-fix measurements have no small targets, text overlaps, clipping, console errors or HTTP resources;
only the intentional modal hint coverage remains. This is not a second full-audit certification.

## Frames looked at

All two bar frames, four early frames, 16 mode/size frames, nine play frames, 12 focused frames and eight last-check frames.
All 67 audit frames were inspected on audit-sheet-01.png through audit-sheet-12.png, with state/size names in audit-frame-map.json.
Focused post-audit frames and their measurements are in post-frames and post-checks.json. All 14 were inspected, including keyboard, held removal, modal, phone results, four packs and Read.
The full size run was made once. Subsequent captures cover only changes, extremes and unresolved leads.

## Art made

19 paintings, 21 generation calls including two redraws, built-in imagegen. Final art: 310.17 KB; bundle: 663.86 KB.
Voice files: 0 KB, intentionally unrecorded. This is comfortably below the 2 MB goal.
Redrew the mostly-melted bottle's sliver and the dry six-cube stack. Inspected all processed images on a contrasting key color.
Prompts/provenance: art/prompts.json. Selected source PNGs: art/raw. Finished images: art/*.webp.

## Art still to paint

None. No people were drawn because this spec calls for an empty car and bench.

## Engine changes wanted

None. No shared kit or engine was changed.

## Left open

Two exact foil anchor minutes and the incompatible noon half-melted picture need a spec correction.
Recorded friendly-dad audio remains future work, as required for Build. Muted automation did not assess human audio quality.
No actual Chromebook benchmark or human classroom test was performed. The single full audit completed; final fixes received focused checks, not a full rerun.
The host file is removed, and owned Chrome/server processes are closed. No commits or polish round.
