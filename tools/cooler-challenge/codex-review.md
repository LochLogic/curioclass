# Codex review: cooler-challenge

## Played

Cold Grade 6 solo play preceded the builder report, handoff, notes and source: near miss, noon design, engineer note and all three Bench investigations. Then checked projector use. The melt plateau and third-bottle payoff are strong; the Bench needed visible samples and a more honest finish.

## Findings fixed

- **Blocker, general, Bench claims:** three wrong first picks plus an option sweep earned three "fixed" marks and completion praise. First scores now remain wrong, marks say "tested; review", and the recap/narration distinguish supported claims from corrections shown. Evidence: review-cheats versus review-fixed-cheats.
- **Should fix, general, voice:** a fresh Bench path dropped Predict at a two-second held-click pace. Shortened Fair/Predict; state-changing actions clear obsolete speech while preserving Read. Unique event keys preserve all five repeated invalid-plan responses. Sound-on no longer welcomes a student to add a wall when none fits; before/after full-wall and full-pack cases are in review-welcome-limits.
- **Should fix, general, art:** cup fronts obscured water/steel, and liquid cutouts had magenta artifacts. Redrew the water insert and fridge bottle, cropped the insert through art.py, corrected compositing and bottom-anchored mass scaling. Kept the painted settings and material textures.
- **Should fix, general, phone Bench:** tall readouts crowded the caption before a plan was locked. Compact instruments now apply there too; cups and readouts have separate stacking contexts.
- **Should fix, general, Build voice:** "Lunch is safe" overstated a classroom model. It now describes coldness in this model; notes retain USDA/FDA food-safety guidance and explain the unmodeled food-freezing phase change.
- **Should fix, general, note:** an immediate first-pass success assumed comparison evidence. Its label and placeholder now fit a single test; editing clears the obsolete saved status and hint. Added explicit accessible naming and separated the keyboard focus ring from its label.
- **Polish, general:** moved the cold-zone label away from the temperature curves, named game cost and the idle 9:00 arrow preview, and added the student's actual A/B changes and supported-first-claim count to the ending.

## Findings left

- **Should fix, spec conflict, numerical examples:** the stated model gives foil anchors 8:58 and 11:49, not 8:57 and 11:48. Kept the computed results, without fitting constants.
- **Should fix, spec conflict, scenario:** 80 degrees Fahrenheit is 26.67 degrees Celsius; the specified 49.4-degree peak and enumeration require that value. The noon $8 design is mostly melted, rather than the spec's half-frozen picture.
- **Polish:** friendly-dad recordings remain unmade; browser fallback was tested. No audio was recorded in this review.

## Break it

- **Design job:** walls alone, four bare frozen bottles, three steel packs and three fridge bottles fail at 8:03, 8:18, 8:14 and 8:05. Real Run/Skip input confirmed each. The $9 cold-to-noon design never earns Job done or opens the engineer check.
- **Meters and limits:** fifth pack, fourth layer and layers that displace existing packs are refused; costs do not acquire hidden items. Edits stop a run at 8:00 and preserve a partial ghost. Skip scores the whole test, rather than elapsed animation time.
- **Engineer questions 1 and 2:** first-position guesses followed by sweeping every other option leave the first answers unchanged. An all-wrong run remains 0 of 2, with review needed. Options shuffle and their lengths do not identify correctness.
- **Note:** an empty/arbitrary note earns no score and cannot repair either answer. Kept it unscored, as required by the spec; its local-only privacy text remains visible.
- **Bench plan:** identical samples, wrong-row and multi-row changes are rejected. Mashing can find a fair setup, but it cannot earn a supported claim. A locked plan rejects setting changes; first-attempt fairness stays separate.
- **Prediction:** Same and arbitrary A/B choices can run a fair test but earn no correctness score or mark.
- **Claims:** choosing a common wrong claim, sweeping all options and changing questions cannot upgrade the recorded first pick. Three wrong claims now finish with 0 of 3 supported and three review marks, without mastery praise.
- **Limits of the task:** trial and error can find a working design, and a one-attempt four-option question permits chance success. No new gate was added beyond the spec's independent explanations and claims.

## Voice walk

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

## Facts checked

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

## Sensitivity

None: no cultural, Indigenous, religious, historical or human-body content. All 19 assets depict materials or deliberately empty test settings, with people:false. No person or animal was added to the hot-car scene.

## Flattest moment left

The initial Bench setup remains more worksheet-like than Build. Kept its required controlled-variable rows; visible sample volumes, live heat bars and the student's numerical evidence now give its results more weight. The strongest Build plateau and ghost comparison remain intact.

## Graphics

Inspected all 19 processed assets and their in-tool scenes, plus every captured review frame. Redrew two assets with built-in imagegen, preserving the house style; prompts and raw outputs are in art/. The larger cup now lets its sample read correctly. Bundle: 578.1 KB; processed art: 283.3 KB. Compared matching desktop frames with Beat Lab and Snowy Mail Route; review-bar-comparison.png is retained in Scratch.

## Audit

Completed once within 40 minutes: review-audit/audit.md, 67 frames inspected on review-audit-look-01 through 17. Resize stress: no exceptions or controls left disabled. All eight STANDARDS sizes were checked in both modes. Keyboard Tab/Enter adds Foam and Cotton and retains focus. Grayscale retains labels/dashes. Motion off keeps 24-second Build and 10-second Bench timing with zero active animations. No tool network requests or runtime errors; the temporary host favicon 404 was fixed in the scratch harness.

All 13 audit leads accounted for: one explicit note-name fix; two initial host-routing symptoms resolved with a compatible temporary host and six focused phone replacements; four intentional modal-background coverage leads; six welcome skips/cuts allowed by BASELINE 16. No audit restart. The note fixes were re-shot at 680, 1366 and 375 pixels, with real Tab/Shift+Tab focus. Its 10 px label gap clears the 7 px ring; saved-state hints clear on edit. Focused checks have no small targets, overlaps, clipping or missing names; background text behind the modal is intentional.

Verified contrast ratios: ink/paper 14.80, muted/white 6.22, white/brand 6.49, blue/cold zone 4.76, brand/cold zone 5.41, focus/white 5.81, button edge/white 3.75. Done when 2 and 4-10 pass; 1 and 3 retain only the named spec conflicts. The initial document read completed immediately without an explicit timeout wrapper; subsequent reads/bundles used 120 seconds, drive batches 300, and this audit 2,400.

Wave lessons checked: current hints and Read, focus, 44-pixel controls, no hidden answer badges, honest assumptions, real standards practice, calm timing, visible short choice sets, resize during action, no delayed welcome, unknown results hidden, distinct line styles, truthful marks, reversible hints and no pre-answer word-copy clue.

## Left open

No tool blocker or should-fix remains. The two foil-minute examples, 27 C/80 F rounding and half-frozen noon wording need a spec correction; model constants were preserved. Recording and human listening quality, an actual Chromebook benchmark and classroom trials remain outside this review. No new feature, shared-source edit or git commit was made. Temporary host files were removed; harnesses close only their own Chrome and server children. This scratch draft is copied into the tool as the final action, per the unattended stop instruction.
