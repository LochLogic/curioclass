# Codex report: up-the-watershed

## Built
Grade 12 watershed investigation with Cases, Sample, Claim and Fix-it. Three case files share a painted, flowing map; eight kits force a sampling plan, claims require selected evidence, and a $3 million cleanup portfolio exposes competing goals and social costs.

Built from the kit starter with the grade 9-12 theme, Curio Class voice, motion and sound controls. One offline bundle; no family engine. Local progress, three saved plans, session-only Why text, Reset and Clear my progress are implemented. All writes stayed in this tool and its Scratch folder. No commits or polish round.

Final bundle: **755,489 bytes (737.8 KiB)**. Source: 1,524 readable lines, none over 160 characters. All assigned Chrome/server ports are closed; host.html is removed.

## Numbers check
PASS. `_scratch/up-the-watershed/watershed_numbers.py` independently reconstructs flow, loads, beach attenuation, every sample, every fix and all 512 portfolios. JavaScript agrees on 4,174 numeric comparisons and every goal classification (`browser-model-results.json`). All 88 displayed sample cells match the spec, including rounding, no flow and Not modeled (`display-results.json`). No numerical spec correction was needed.

Worked portfolios: E+D2+A+C+G costs $2,955,000, meets all goals, and leaves storm beach water at 461.46 while the beach is protected by closure. The $1,595,000 alternative fails lake dry phosphorus at 0.209475. All fixes cost $4,100,000. Exactly two in-budget all-goal portfolios exist; both use the advisory. B1 and B2 nitrate reductions multiply on the remainder.

The fictional model and limitations are visible in the tool and teacher notes. The 410 value is the EPA statistical threshold used as this case's action line, not a universal legal closure rule. Reference facts were taken from the spec's Sources; no new factual topic was added.

## Feel check
Best moment: the expensive plant upgrade finally pulls dry lake phosphorus below its line, but the beach result still says Protected, not cleaned. That makes the student's budget choice worth explaining. The three cases change the inference: dry sewer evidence, storm runoff evidence, then a sediment source that is present but too small to be the culprit.

Flattest moment 1: an early map felt like floating labels. Added seven painted source miniatures, five clipped aerial textures, shaded banks, bridges, roads, lake highlights, quiet flow and a sample pulse. Large source photos let the student inspect the place. Repositioned compact icons and labels so the art remains usable.

Flattest moment 2: cleanup testing initially felt like instantaneous arithmetic. Added the 400 ms test beat followed by a real 400 ms gauge fill, immediate budget/toggle feedback and immediate invalidation during motion. Motion off preserves the beat. Whole-creek shares now occupy the panel so revealing the answer does not bury the map.

Played the real-click three-case routes and cleanup/save/compare sequence. I would continue through the competing cleanup plans after ten minutes; once all three cases are known, the fixed data has limited replay depth. This is a build assessment, not a measured student engagement result.

Compared with Beat Lab and Snowy Mail Route. The field-map art, case photography, instrument readouts and restrained feedback meet the intended finish without copying their scenes. Comparison: `_scratch/up-the-watershed/feel-comparison.png`.

## Done when
1. PASS: every site/weather table value and its displayed rounding; 88/88 cells, `display-results.json`.
2. PASS: Beach solved with A, D1 and D2 in five real samples, three kits left; `final-solve-beach.json`.
3. PASS: geese accusation marked wrong with about 9 percent dry and 5 percent storm; `functional/geese-wrong.png`.
4. PASS: Green lake solved using Outfall alone for E plus storm pairs for B and C; five samples, `final-solve-lake.json`. Dry field/construction evidence is rejected by the validator.
5. PASS: C alone solves Creek with two samples; B feedback says only 14 percent, `final-solve-creek.json` and `functional/fields-wrong.png`.
6. PASS: $2,955,000 advisory portfolio meets all three goals and explicitly distinguishes protection from cleaning; `advisory.json`.
7. PASS: $1,595,000 portfolio has dry lake P displayed as 0.209 and fails that goal; `lake-fails.json`.
8. PASS: all fixes cost $4,100,000, show the over-budget state and disable Test plan; `over-budget.json` and frame.
9. PASS: Cases, Sample, Claim and Fix-it have the specified visual focus at 1366x768 and 680x425. Map labels are at least 10 px. Full sweep and focused frames inspected.
10. PASS: three active gauge animations clear synchronously on a toggle and stay cleared; `gauge-interrupt.json`. Calm retains the test beat with zero animations, `gauge-calm.json`.
11. PASS: full map, kits and Take sample fit 1366 and the 375-wide iframe. All 22 images decode, textures follow their parcels, and finished art contains no people. Final map/result frames inspected.
12. PASS: how-to deduplication, repeated last-kit/out-of-kits events and five repeated solved events checked with held input. `solved-events-drained.json` records five callbacks, five spoken events and an empty queue. Evidence controls and full-portfolio hints do not name disabled next actions.

## Wave lessons
- PASS, Hint and voice: hints update synchronously; Read uses the visible hint. Heard-state how-to deduplication and distinct event keys verified at a 2 s tap pace. Mode changes stop stale context.
- PASS, Focus and layout: controls persist under the pointer, dialogs restore focus, and hints reserve space. Real case routes, keyboard frame and post-fix geometry checks cover this.
- PASS, Sizes: 44 px targets, visible hints, all seven STANDARDS desktop sizes and the 375x812 iframe checked. Extra 700x900 portrait check covers the breakpoint.
- PASS, No giveaways: neutral source art and equal suspect controls; no pre-sample success state. Claims require purchased samples. The post-submit reveal is the spec's deliberate teaching feature.
- PASS, Honest numbers: made-up watershed, repeatable weather samples, fixed reductions and omitted processes are explained; concentration and storm load are distinguished.
- PASS, Standards: sampling/claiming and changing cleanup designs exercise HS-ESS3-4; comparing costs, goals and Why explanations exercises HS-ETS1-3. No family is specified.
- PASS, Motion off: tool animations explicitly stop, results stay legible, and the calculation beat remains. Calm probe finds zero active animations.
- PASS, Short choices stay visible: all three case cards, seven suspects and nine fix choices fit their layouts without a hidden choice scroll panel.
- PASS, Resize mid-animation: audit resize sweep has no exception or stuck control; active-plan invalidation is version guarded. Brackets and pinned results reposition without replacing controls.
- PASS, Deferred welcome: no welcomeAfter; mode-scoped welcomes and modal-return welcome verified. Same-mode quick taps preserve the line.
- PASS, Unknown as unknown: samples appear only when collected or after explicit whole-creek reveal. Untested gauges show question marks.
- PASS, One look one meaning: D/S letters, order and color consistently mean dry/storm; source halos indicate checked claims, not automatically guilty sources. Grayscale inspected.
- PASS, Badge truth: solved requires the exact culprit set and valid evidence; Protected explicitly says water is still over 410. Goals reflect the independent model.
- PASS, Hints restore: plan changes clear tested/save hints immediately; leaving reveal restores Claim instructions. A full portfolio names Compare plans, not disabled Save.
- PASS, No word copying: source photos and names identify locations; students must use measured jumps, weather and target shares to establish responsibility.

## Audit leads
Ran the mechanical audit once, to completion, within its 40-minute limit. Original result: **549 leads**, retained in `_scratch/up-the-watershed/audit/audit.md`. Default sizes and calm were clean; the original state findings drove the following focused fixes. The complete audit was not repeated.

Every original lead has a disposition in `audit-dispositions.csv` (549 entries, with original audit line and state). Grouped responses:
- 406 overlap and 107 hidden-text rows: responsive source/spot geometry, heading placement, flags and source-share placement corrected. Modal logbook masking and the closeable passive result covering map detail are intentional. The result body passes input through; its 44 px Close target now has reserved header space. Final result probes find no header/value collisions.
- Whole-creek shares moved from the map to reserved panel space. Final 680, 1366 and 375 checks show 22 flags, eight source-share rows and zero flag collisions. Focused map checks remove the remaining title/S1 and compact source/flag collisions.
- 15 below-fold rows: retained for the three auxiliary footer controls on the phone. The page scrolls to them; map, kits, Take sample and all choice sets remain visible.
- Seven disabled-evidence narration rows: fixed by showing the evidence action only after selecting a suspect. All three final real-click claim routes pass.
- Four tiny-text rows: units now have a 10 px minimum; compact Evidence uses real text spans instead of a zero-font parent.
- One hidden Fix-it hint: fixed by moving the same actual hint element into the Fix-it wrapper. Focused Fix-it checks find the hint in view at both core sizes.
- One locked Fix-it focus row: expected from the automatic probe before a case is solved. A real solved case unlocks Fix-it and keeps all controls usable.
- Two missing-first-welcome rows: modal Close restores the unplayed Cases premise; the notes-return probe verifies it. Clear uses the same return handler.
- One empty Restart row: idempotent on a fresh case; exhausted-kit restart restores eight kits and removes the evidence.
- Five quick-tap welcome rows: Cases/Sample/Claim/Reset fixed by the same-mode guard. The old Open creek coordinates hit a different control after changing screens; stopping the obsolete welcome is intentional, and Read remains available.

## Frames looked at
The late complete sweep has 38 frames: four modes at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375-wide, plus result, logbook, reveal, keyboard, grayscale and Motion off. Opened these and the important changed states at native size.

Inspected another 139 original frames through 27 contact sheets, with native views of critical cases, fixes, results and final phone states. `frame-sheet-manifest.json` maps every sheet to its originals, including all 58 mechanical-audit frames. Earlier failing frames are preserved; the `last/`, `final-paths/`, `result-finish/` and `voice-finish/` folders show focused verification of the final corrections.

All final drive batches report zero console errors/warnings/exceptions. The bundle prints expected missing-recording notices because recording audio is outside this build. `validation-manifest.json` indexes numeric, visual, motion, persistence and voice evidence, bundle hashes and cleanup status.

## Art made
22 final WebPs used: eight retained scene paintings and 14 newly generated assets (two case scenes, seven source miniatures, five aerial textures). Final art totals **476,080 bytes (464.9 KiB)**; bundle is **737.8 KiB**. Full prompts, original-image provenance and `drawn_by: codex` are recorded. OpenAI generation credit is in tool.draft.json.

Processed through `art.py --rekey <name>` only. Magenta-keyed icons were despilled, then inspected at final size. No redraws were needed; key/despill and sizing were refined. Exact waterways, parcels, roads, labels, brackets, result bars and notice text are drawn in code. No generated text, logos or people.

## Art still to paint
None. All specified illustrations are present. No audio was recorded; browser speech fallback uses the kit, while the requested bank/style identity remains in voice/lines.json.

## Engine changes wanted
None. Shared kit, scripts, docs and other tool folders were not edited. The temporary iframe host received a data favicon from the scratch harness and was removed after each batch.

## Left open
- Cold review has not run. The complete audit predates the focused fixes; original findings and post-fix evidence are both retained rather than claiming a clean rerun.
- Compact fix cards expose full effects and who-pays text through accessible descriptions and titles; larger laptops show it inline. Touch discoverability deserves a cold-review look.
- Spec voice-bank recordings and actual classroom engagement/duration remain unmeasured. Speech timbre currently depends on the browser's fallback voice.
- The three spec questions are resolved in handoff.md: retain Up the Watershed, count advisory as protection with dirty water stated, and retain fictional scaled costs/loads.
- Process deviations: reference bar tools were opened after the first playable version; this report was written last to obey the user's explicit stop-on-report instruction. Two initial instant inspection commands lacked a hard deadline; subsequent substantive commands and all bundle/drive/audit runs used hard limits.
