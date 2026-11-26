# Cooler Challenge: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: cooler-challenge

#### Built

Build only in S:/CurioClass-codex. No commits, deployment or separate polish round.
Built both Grade 6 modes from the starter: layered lunchbox design, three live heat paths, animated tests,
ghost comparisons, a paged test log, the engineer's check and local note, plus three fair investigations.
The readable source is src.html; cooler-challenge.html is the single offline bundle; tool.draft.json has stage built.
Required teacher notes, voice manifest, audit states, all painted art and handoff are present.
The report was assembled early in Scratch, then written here last to honor the user's explicit stop condition.

#### Numbers check

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

#### Facts checked

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

#### Break it

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

#### Voice walk

Main path: play/checks.json and voice-walk.json, real 120 ms holds at a two-second tap pace, default Sound.
Heard: wBuild, run1, flat, short, pass, check, wrong, right, note, restart, passOver, wBench,
unfair three times for distinct plan attempts, fair, predict, runB, claim, wrong, fair, right,
fair, runEnergy, right, benchDone. Repeated how lines were silent; events repeated; no main-path cuts.
Both welcomes, all main mode instructions and the unequal-heating instruction were heard in the relevant state.
Side path: Sound off, Read, Sound on, Bench, Energy. Read protected its hint; mode change dropped the obsolete queued welcome.
Current Read also includes the job constraints before the first Build run. Final fixed-line count: 33.
Achird / friendly-dad recording direction is preserved. No audio was recorded in Build; browser speech is used.

#### Feel check

Played a full scripted student-style session through near miss, revision, engineer questions/note and all three investigations.
Best moment: the third bottle holds lunch to noon while the previous 11:26 curve rises as a ghost and the ice stays at zero.
Flattest moment 1: a worksheet-like Bench and cups sitting beside the painted plates. Fixed plate alignment, glass transparency,
live heat bars and the locked-plan summary, with different physical questions for the later investigations.
Flattest moment 2: compact results squeezed the graph and phone results sat below the viewport. Fixed action placement,
compact result headings and a phone test layout that prioritizes the graph alongside the controls.
Bar tools were bundled into Scratch and opened before building. Both reference frames were inspected.
bar-comparison.png puts the earned result beside Beat Lab at matching proportions. The painted place and layered box
have comparable finish; this tool deliberately has fewer controls. This is an agent play check, not a human usability study.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

All two bar frames, four early frames, 16 mode/size frames, nine play frames, 12 focused frames and eight last-check frames.
All 67 audit frames were inspected on audit-sheet-01.png through audit-sheet-12.png, with state/size names in audit-frame-map.json.
Focused post-audit frames and their measurements are in post-frames and post-checks.json. All 14 were inspected, including keyboard, held removal, modal, phone results, four packs and Read.
The full size run was made once. Subsequent captures cover only changes, extremes and unresolved leads.

#### Art made

19 paintings, 21 generation calls including two redraws, built-in imagegen. Final art: 310.17 KB; bundle: 663.86 KB.
Voice files: 0 KB, intentionally unrecorded. This is comfortably below the 2 MB goal.
Redrew the mostly-melted bottle's sliver and the dry six-cube stack. Inspected all processed images on a contrasting key color.
Prompts/provenance: art/prompts.json. Selected source PNGs: art/raw. Finished images: art/*.webp.

#### Art still to paint

None. No people were drawn because this spec calls for an empty car and bench.

#### Engine changes wanted

None. No shared kit or engine was changed.

#### Left open

Two exact foil anchor minutes and the incompatible noon half-melted picture need a spec correction.
Recorded friendly-dad audio remains future work, as required for Build. Muted automation did not assess human audio quality.
No actual Chromebook benchmark or human classroom test was performed. The single full audit completed; final fixes received focused checks, not a full rerun.
The host file is removed, and owned Chrome/server processes are closed. No commits or polish round.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: cooler-challenge

#### Played

Cold Grade 6 solo play preceded the builder report, handoff, notes and source: near miss, noon design, engineer note and all three Bench investigations. Then checked projector use. The melt plateau and third-bottle payoff are strong; the Bench needed visible samples and a more honest finish.

#### Findings fixed

- **Blocker, general, Bench claims:** three wrong first picks plus an option sweep earned three "fixed" marks and completion praise. First scores now remain wrong, marks say "tested; review", and the recap/narration distinguish supported claims from corrections shown. Evidence: review-cheats versus review-fixed-cheats.
- **Should fix, general, voice:** a fresh Bench path dropped Predict at a two-second held-click pace. Shortened Fair/Predict; state-changing actions clear obsolete speech while preserving Read. Unique event keys preserve all five repeated invalid-plan responses. Sound-on no longer welcomes a student to add a wall when none fits; before/after full-wall and full-pack cases are in review-welcome-limits.
- **Should fix, general, art:** cup fronts obscured water/steel, and liquid cutouts had magenta artifacts. Redrew the water insert and fridge bottle, cropped the insert through art.py, corrected compositing and bottom-anchored mass scaling. Kept the painted settings and material textures.
- **Should fix, general, phone Bench:** tall readouts crowded the caption before a plan was locked. Compact instruments now apply there too; cups and readouts have separate stacking contexts.
- **Should fix, general, Build voice:** "Lunch is safe" overstated a classroom model. It now describes coldness in this model; notes retain USDA/FDA food-safety guidance and explain the unmodeled food-freezing phase change.
- **Should fix, general, note:** an immediate first-pass success assumed comparison evidence. Its label and placeholder now fit a single test; editing clears the obsolete saved status and hint. Added explicit accessible naming and separated the keyboard focus ring from its label.
- **Polish, general:** moved the cold-zone label away from the temperature curves, named game cost and the idle 9:00 arrow preview, and added the student's actual A/B changes and supported-first-claim count to the ending.

#### Findings left

- **Should fix, spec conflict, numerical examples:** the stated model gives foil anchors 8:58 and 11:49, not 8:57 and 11:48. Kept the computed results, without fitting constants.
- **Should fix, spec conflict, scenario:** 80 degrees Fahrenheit is 26.67 degrees Celsius; the specified 49.4-degree peak and enumeration require that value. The noon $8 design is mostly melted, rather than the spec's half-frozen picture.
- **Polish:** friendly-dad recordings remain unmade; browser fallback was tested. No audio was recorded in this review.

#### Break it

- **Design job:** walls alone, four bare frozen bottles, three steel packs and three fridge bottles fail at 8:03, 8:18, 8:14 and 8:05. Real Run/Skip input confirmed each. The $9 cold-to-noon design never earns Job done or opens the engineer check.
- **Meters and limits:** fifth pack, fourth layer and layers that displace existing packs are refused; costs do not acquire hidden items. Edits stop a run at 8:00 and preserve a partial ghost. Skip scores the whole test, rather than elapsed animation time.
- **Engineer questions 1 and 2:** first-position guesses followed by sweeping every other option leave the first answers unchanged. An all-wrong run remains 0 of 2, with review needed. Options shuffle and their lengths do not identify correctness.
- **Note:** an empty/arbitrary note earns no score and cannot repair either answer. Kept it unscored, as required by the spec; its local-only privacy text remains visible.
- **Bench plan:** identical samples, wrong-row and multi-row changes are rejected. Mashing can find a fair setup, but it cannot earn a supported claim. A locked plan rejects setting changes; first-attempt fairness stays separate.
- **Prediction:** Same and arbitrary A/B choices can run a fair test but earn no correctness score or mark.
- **Claims:** choosing a common wrong claim, sweeping all options and changing questions cannot upgrade the recorded first pick. Three wrong claims now finish with 0 of 3 supported and three review marks, without mastery praise.
- **Limits of the task:** trial and error can find a working design, and a one-attempt four-option question permits chance success. No new gate was added beyond the spec's independent explanations and claims.

#### Voice walk

120 ms held clicks, two-second gaps, default Sound on: add walls and bottles, Run, plateau, pass, engineer answers/note, Bench Mass/Matter/Energy, fair plan, prediction, Run and claim. Main-path evidence: review-release-walk; side evidence: voice-side.json, read-then-run.json and review-welcome-limits.

Heard in order: wBuild, run1, flat, pass, check, right, right, noteFirst, wBench, fair, predict, runB, claim, right, fair, right, fair, runEnergy, right, benchDone. No dropped lines or cut event results on this final walk.

| Line | Kind | Expected | Heard |
|---|---|---:|---:|
| run1, flat, check, noteFirst, predict, runB, claim, runEnergy | how | 1 each | 1 each |
| fair | event | 3 | 3 |
| right | event | 5 | 5 |
| benchDone | event | 1 | 1 |
| unfair, five identical checks | event | 5 | 5 whole |

Read works with Sound off; mode change releases it immediately. Stale speech is stopped when its screen is left. Welcome cuts follow BASELINE 16; action advances can stop obsolete how-to speech. The 35 fixed lines match allLines and the voice manifest.

#### Facts checked

| Fact or number | Named source and result |
|---|---|
| Cold perishables below 40 F; at least two cold sources | [USDA FSIS Q&A](https://ask.fsis.usda.gov/article/How-do-you-keep-a-bag-lunch-safe) and [USDA August 2025 guidance](https://content.govdelivery.com/accounts/USDAOC/bulletins/3ebbb1b): agree. The handout itself returned 403. |
| Fridge 40 F or colder; freezer 0 F, about -18 C | [FDA, Are You Storing Food Safely?](https://www.fda.gov/consumers/consumer-updates/are-you-storing-food-safely): agree. Notes explain conservative 4 C rounding. |
| Sunny cars heat rapidly, including mild days; never leave people or pets inside | [NWS, Children, Pets and Vehicles](https://www.weather.gov/safety/heat-children-pets): agrees with the safety framing; the car is an empty model chamber. |
| About 41 F rise in an hour; most in first half-hour | [McLaren, Null and Quinn, Pediatrics 2005](https://pubmed.ncbi.nlm.nih.gov/15995010/): 80 percent in 30 minutes. Exact interpolation is a scenario assumption. |
| A possible 20 F rise in ten minutes | [NY DMV heatstroke guidance](https://dmv.ny.gov/news/new-york-state-offers-guidance-prevent-heatstroke-ahead-weekend-warm): agrees. |
| Warmer-to-cooler transfer, conduction/convection/radiation and insulation | [DOE/PNNL Heat Flow](https://basc.pnnl.gov/information/building-science-introduction-heat-flow): agree; outward arrows match the model's signs. |
| Wall resistance and sealed-air-gap comparisons | [ASHRAE Fundamentals, chapter 26](https://handbook.ashrae.org/Handbooks/F21/SI/f21_ch26/f21_ch26_si.aspx): construction matters. Exact tile rankings/resistances are identified as model choices. |
| Ice's zero-degree melting plateau; melting heat 334 J/g | [OpenStax 14.3](https://openstax.org/books/college-physics-2e/pages/14-3-phase-change-and-latent-heat): agree for pure water at ordinary pressure. |
| Matter/mass/heating affect temperature change | [OpenStax 14.2](https://openstax.org/books/college-physics-2e/pages/14-2-temperature-change-and-heat-capacity): agree. Specific heats 4.18, 2.05 and 0.47 are model approximations, not exact table quotations. |
| Shiny reflectors versus dark absorbers | [OpenStax 14.7](https://openstax.org/books/college-physics-2e/pages/14-7-radiation): agrees; numerical absorptances remain model settings. |
| Temperature and average particle kinetic motion; two claimed standards | Official [NGSS MS-PS3-3](https://www.nextgenscience.org/pe/ms-ps3-3-energy) and [MS-PS3-4](https://www.nextgenscience.org/pe/ms-ps3-4-energy): authentic student design/investigation actions, no energy-total calculation task. |
| Prices, capacities, limits, run times and graph values | Spec Content plus independent review_numbers.py: all 3,450 designs, 31 budgeted/46 total passes, no steel/fridge pass; 24 Bench states and 48 fair pairs support the claims. Two foil-minute conflicts are reported above. |

#### Sensitivity

None: no cultural, Indigenous, religious, historical or human-body content. All 19 assets depict materials or deliberately empty test settings, with people:false. No person or animal was added to the hot-car scene.

#### Flattest moment left

The initial Bench setup remains more worksheet-like than Build. Kept its required controlled-variable rows; visible sample volumes, live heat bars and the student's numerical evidence now give its results more weight. The strongest Build plateau and ghost comparison remain intact.

#### Graphics

Inspected all 19 processed assets and their in-tool scenes, plus every captured review frame. Redrew two assets with built-in imagegen, preserving the house style; prompts and raw outputs are in art/. The larger cup now lets its sample read correctly. Bundle: 578.1 KB; processed art: 283.3 KB. Compared matching desktop frames with Beat Lab and Snowy Mail Route; review-bar-comparison.png is retained in Scratch.

#### Audit

Completed once within 40 minutes: review-audit/audit.md, 67 frames inspected on review-audit-look-01 through 17. Resize stress: no exceptions or controls left disabled. All eight STANDARDS sizes were checked in both modes. Keyboard Tab/Enter adds Foam and Cotton and retains focus. Grayscale retains labels/dashes. Motion off keeps 24-second Build and 10-second Bench timing with zero active animations. No tool network requests or runtime errors; the temporary host favicon 404 was fixed in the scratch harness.

All 13 audit leads accounted for: one explicit note-name fix; two initial host-routing symptoms resolved with a compatible temporary host and six focused phone replacements; four intentional modal-background coverage leads; six welcome skips/cuts allowed by BASELINE 16. No audit restart. The note fixes were re-shot at 680, 1366 and 375 pixels, with real Tab/Shift+Tab focus. Its 10 px label gap clears the 7 px ring; saved-state hints clear on edit. Focused checks have no small targets, overlaps, clipping or missing names; background text behind the modal is intentional.

Verified contrast ratios: ink/paper 14.80, muted/white 6.22, white/brand 6.49, blue/cold zone 4.76, brand/cold zone 5.41, focus/white 5.81, button edge/white 3.75. Done when 2 and 4-10 pass; 1 and 3 retain only the named spec conflicts. The initial document read completed immediately without an explicit timeout wrapper; subsequent reads/bundles used 120 seconds, drive batches 300, and this audit 2,400.

Wave lessons checked: current hints and Read, focus, 44-pixel controls, no hidden answer badges, honest assumptions, real standards practice, calm timing, visible short choice sets, resize during action, no delayed welcome, unknown results hidden, distinct line styles, truthful marks, reversible hints and no pre-answer word-copy clue.

#### Left open

No tool blocker or should-fix remains. The two foil-minute examples, 27 C/80 F rounding and half-frozen noon wording need a spec correction; model constants were preserved. Recording and human listening quality, an actual Chromebook benchmark and classroom trials remain outside this review. No new feature, shared-source edit or git commit was made. Temporary host files were removed; harnesses close only their own Chrome and server children. This scratch draft is copied into the tool as the final action, per the unattended stop instruction.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Cooler Challenge build handoff

Build only. No commits and no separate polish round. The final report is codex-report.md.

#### Structure

src.html starts from the kit starter and remains readable. Its order is responsive layout, fixed controls and dialogs,
material/art/voice tables, thermal model, Build actions and rendering, log, engineer's check, Bench, then bindings.
The offline bundle is generated by scripts/bundle_tool.py. No data file or outside library is loaded.
The kit owns Motion, Sound, Read, the voice queue and tones. Both graphs and the changing cutaway are local SVG.
The car and bench are large paintings; swatches are also used as the actual wall textures.

Build precomputes 1,441 points from the explicit ten-second model, then reveals them over 24 seconds.
Bench evaluates sample enthalpy at each graph point and runs for ten seconds. Motion off preserves both durations.
Edits invalidate a Build run with a revision number; Bench uses a generation number. Mode changes stop active tests.
The comparison ghost belongs to the actual previous full or partial run. Completed runs are immutable log snapshots.
Pack removal has keyboard access. Layer-label buttons provide keyboard access to the thin layer bands.
The cups are positioned from the painted plate centers after cover sizing, rather than floating beside the plates.

#### Graphics and voice

All 19 specified images were made individually with the built-in imagegen tool during this build.
Full prompts and people:false tags are in art/prompts.json. Raw files are in art/raw; processed WebP files are in art.
Only art.py --rekey was used. No paid art-script generation, downloads of artwork or audio recordings were made.
The mostly-melted bottle and dry steel stack were redrawn for a clear ice sliver and a consistent six-cube stack.
Glass assets use the pipeline's holes and despill options so the samples can be seen inside their cups.
The warm painted realism style stays consistent. Sources credit OpenAI gpt-image.

voice/lines.json contains the runtime lines with the specified friendly-dad / Achird direction.
It includes a truthful unequal-heating line for Energy. Browser speech is the current fallback; recordings remain future work.
The main voice walk used held clicks at a two-second pace. Its log is in Scratch/voice-walk.json.
The final manifest contains 33 lines, including the job constraints on Read before the first Build test.

#### Settled choices and contradictions

There are no listed Open questions in the spec. These internal conflicts were resolved without changing spec.md:

- The user explicitly requires this image tool; that supersedes the spec's older Local FLUX production route.
  The spec's exclusion of people and animals remains because an empty car is part of what this scene teaches.
- Car outside temperature is both 27 °C and 80 °F. Use exactly 80 °F, or 26.6667 °C, in the curve.
  This reproduces its 49.4 °C peak, 31 budgeted passes, 46 total passes, 82 near misses and the 11:26 main anchor.
  Literal 27 °C does not reproduce those figures. The readout shows 26.7 °C and 80 °F consistently.
- Two foil anchors still differ under the stated model: bare + four bottles + foil + seal gives 8:58, not 8:57;
  two foam + two bottles + foil + seal gives 11:49, not 11:48. No constants or times were fitted to examples.
  Done when 3 therefore does not pass its demand for every exact minute. The independent Python and JS agree.
- The noon three-bottle pass has about 81 percent of its ice melted. It shows the mostly-melted painting, not half-frozen ice.
  This follows the model's state rule rather than Done when 1's incompatible half-melted picture description.
- Mass and Matter hold heat equal; Energy changes only the heat setting. Its bars and narration correctly differ.
  Repeating the spec's equal-heat line in Energy would contradict the investigation.
- The kJ axes are retained as the spec requests. NGSS excludes calculating total thermal energy, not displaying the supplied heat.
  Students make graphical comparisons and do no energy calculation. Notes state the distinction.
- One-try claims retain the first answer. Cold review replaced the automatic "fixed" mark with "tested; review".
  A displayed correction is not student mastery. The completion recap counts supported first claims and chooses truthful narration.
  Engineering questions retain their first score too. Neither a note nor a prediction is scored.
- Compact segmented controls use 44 px height rather than the contradictory 36 px row height. At short landscape sizes,
  a locked plan folds to its summary before Run, and answered claims fold away to keep corrections and Next in view.
  Before an unanswered claim, question-navigation buttons fold away while the hint names the question.
- The log folds to a Log dialog at all heights up to 650 px, including 1000x625, to keep action and plot useful.
  At 1366x768, the log stays beneath the scene and the full Build shelf stays above the fold.
- Skip is explicitly required, so physical trial and error can happen faster than the spec's estimate of 77 full runs.
  Job done measures the design, not demonstrated understanding. The one-attempt engineer questions remain separate evidence.
- The user requires stopping when the tool report is written. The report was started early in Scratch/report-draft.md,
  filled during checks and written into the tool as the final build action.

#### Checks and evidence

Scratch means S:/CurioClass-codex/_scratch/cooler-challenge.
verified-numbers.json and fair-pairs.json independently enumerate all boxes and all 48 eligible fair Bench pairs.
play/checks.json covers the actual full two-second held-click main path, the wrong-answer sweeps, local note and three investigations.
size-frames contains the single full Build and Bench size pass, including the real iframe at host port 8795.
focused-frames and last-frames contain only fixes, extremes and checks missing from that pass.
Static checks include source readability, matching voice lines, contrast, network attributes and size.
The final audit and its leads are in Scratch/audit; their dispositions are in codex-report.md.
The single audit completed with 31 pre-fix leads. Compact labels, plot spacing, pack targets, phone results and focus
were addressed with focused checks in post-checks.json, not a second complete audit. Modal coverage of the background
is intentional. Run can replace the welcome under BASELINE 16; the premise remains in the hint, job and Read.
All 14 post-fix frames were inspected. They have no small targets, text overlaps, clipping, console errors or HTTP
resources. The only keep-region lead is the intentional hint coverage behind the engineer dialog.
Final size: 663.86 KB bundle, including 310.17 KB WebP art, and 0 KB recorded voice. The temporary host file is absent.
All browser profiles and previews remain in Scratch. Chrome ports are within 9990 through 9997.
Host and Chrome processes started by these checks are closed by their harnesses.

#### Sensitivity

No cultural, religious, historical or human-body material. No people or animals in any art.
Food safety and hot-car safety are grounded in USDA/FDA/National Weather Service guidance in notes.md.
The car is an idealized test chamber; the tool never recommends leaving real food, people or pets there.
The teacher notes distinguish a classroom model from a food-safety guarantee.

#### Engine changes wanted

None. No shared kit, engine, documentation or other tool was intentionally edited.

#### Cold review changes

The cold review played the student path before reading this file. Its evidence uses review-prefixed files in Scratch.
Two-second held-click testing caught a dropped prediction instruction. Fair/predict lines are now shorter, and state-changing
actions hush obsolete narration. Current speech is still browser fallback, with 35 matching lines in voice/lines.json.
Repeated result events have unique queue keys, so five identical invalid-plan checks receive five whole responses.
Wrong first claims remain wrong; no correction-shown state earns a "fixed" badge. The final recap and per-test feedback
use the student's actual evidence. A first-pass design gets a note prompt that does not assume an earlier comparison run.
Editing a saved note clears its old saved-status message. Narration distinguishes model coldness from a real food-safety guarantee.
The water insert and fridge bottle were redrawn with built-in imagegen and rekeyed to remove magenta artifacts.
Samples now render above the translucent cup front, with bottom-anchored mass scaling. The cold-zone label moved off the curves.
Phone readouts use the compact instrument layout even before a plan is locked, keeping the caption and readouts separate.
Review-only Chrome ports are 9960 and 9961; the iframe host uses 8765. No git commit or shared-file change is authorized.

The single cold-review audit completed inside its 40-minute cap. review-audit/audit.md retains all 13 original leads:
one explicit note-name fix, two host-routing symptoms, four intentional modal-background coverage leads, and six
welcome skips/cuts permitted by BASELINE 16. Resize stress found no exceptions or controls left disabled.
The temporary host compatibility repair let that same audit continue; it was not restarted.
review-post-audit contains six replacement phone states and the note at 680, 1366 and 375 pixels.
review-note-focus adds real Tab/Shift+Tab focus checks: the label gap is 10 px against a 7 px focus-ring reach.
The note now has an explicit accessible label, contextual placeholder and clear saved/unsaved hint behavior.
All focused checks are clean except intended background text behind the modal. All frames were inspected.
review-release-walk records each main how-to once, five right-result events, and no dropped lines or cut events.
Five identical invalid plans get five whole events; Read remains protected when Run is pressed.
Sound-on welcomes are guarded against full-wall and full-pack states, so they cannot ask for a wall that will not fit.
review-welcome-limits retains both before/after cases; the current room-limit hint stays visible.
Final bundle is about 578 KB; processed art is 283 KB. No recorded audio was added.

#### Left open

Resolve the two exact foil anchor times and the noon ice-picture wording in a future spec correction.
Recorded Achird narration has not been made, as required for Build only. Human audio quality has not been assessed.
The Windows headless tests do not certify performance on an actual school Chromebook.
The 375 px iframe keeps all main controls visible. While designing, the painted scene continues below them.
During a test it folds to prioritize the graph in the same viewport. A locked Bench plan folds to its summary too.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
