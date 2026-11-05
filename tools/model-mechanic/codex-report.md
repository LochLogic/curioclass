# Codex report: model-mechanic

## Built

- Garage and all three Work Orders use the shared ml-lab engine, seeded data, real nearest-neighbor votes and grouped evaluation.
- Built the matrix, time filters, 40-photo strip, evidence drawers, four-feature photo inspector, label edits, training steppers, k choices and clue switches.
- Completed orders show their repair note and enable Next. Their edits survive Garage visits. Garage resets when left. Nothing is saved.
- Added teacher notes, draft metadata, 53 voice lines, audit states, nine art assets and preview.svg. No commits or polish round.
- The single full mechanical audit timed out at 40 minutes without audit.md. This report does not claim a clean full audit.
- Process deviation: the brief's bar-tool prerequisite regenerated the ignored snowy-mail-route and beat-lab HTML bundles outside the two allowed folders. Other tools' source files were not edited.

## Numbers check

PASS: all 17 reference table rows reproduce in Node and in the browser. The additional 11 k-value cases in Sources also match, for 28 numeric cases total.

Evidence: _scratch/model-mechanic/numbers.cjs, source-extras.cjs, all-reference-results.json and eight-labels.json. The pool has 320 items; tests have 15 day and 25 night items. No discrepancy with the specification remained.

Measured scoring was about 1 to 2 milliseconds in the checked runs, including the 320-photo maximum. Scoring uses selected numeric clues, not image pixels.

Recomputed contrast: brand ink/lime 11.26:1; ink/paper 15.62:1; ink/panel 14.19:1; muted/panel 7.77:1; lime/panel 11.01:1; focus/panel 11.51:1. Glyph letters use dark ink on the class colors.

## Feel check

Best moment: opening a mislabeled night deer with an Empty tag, changing it to Deer, and seeing two test errors disappear on the next run. The complete eight-label path finishes at 37/40 with Deer 10/10.

Two flattest moments and repairs:
1. The initial engine rendering left a tiny matrix in a large empty corner. Centered and sized its host in real pixels, with bigger cells and compact letter keys where needed.
2. Completing an order initially left the repair note below the fold. The earned note now replaces the evidence preview and the diagonal grows into the available space. Tapping a cell still reopens inspection.

Played the full three-order sequence with held clicks. Scarcity, missing night examples and bad labels need different repairs; they produce different matrix patterns. Garage supports further experiments without a win condition.

Looked at both bar tools. Side-by-side evidence is _scratch/model-mechanic/bar-comparison.png. The finish uses a dark instrument bench, documentary camera images, large inspectors, count motion, tag flips, immediate tones and restrained repair feedback.

## Done when

1. PASS: Garage 39/40, Day 15, Night 24; k=1 gives 37; Mask only gives 11. Browser reference checks and mask-only frame.
2. PASS: WO1 starts 32 with Fox-to-Raccoon 8. Both fox +5 steps produce 40/40 and both live goals. Held-click fox-repair and complete-journey checks.
3. PASS: WO2 starts Night 17. Night 10 each gives Night 22 and 37 overall; Mask off gives Night 22 and 36 overall. Both browser configurations checked; Mask-off path also played.
4. PASS: WO3 starts 33 with Deer-to-Empty 4. The drawer shows deer labeled Empty. k=5 gives 39. All eight UI label edits, then restoring all clues and k=1, gives 37 and Deer 10/10.
5. PASS: every reference row matches the shared engine. Independent pre-build calculation plus browser checks.
6. PASS: goals tick and untick after runs. A bad k change drops WO1 to 30, unticks Fox and disables Next. Any pending edit also disables Next.
7. PASS: changed is spoken once across five held-click changes; all five repeated score events start at a two-second tap pace. Read delays the queued score until it finishes. Next is named only after the goals enable it.
8. PASS: Run, matrix and all training steppers fit at 1280x720 and 1366x768. Through the 375 px host, numbers measure 15.36 px and matrix targets 44 px. Grayscale retains letters and X marks.
9. PASS: the matrix is the dominant stage element at 1366x768 and 1000x625 in both modes. Inspected full-size and mode frames.
10. PASS: a real cell press during the tween snaps and opens its drawer. A second Run starts immediately. Programmatic Reset during a tween restores 39/40 without an exception.
11. PASS: all nine painted assets are used; animal height follows Size, day/night backdrops differ, infrared subjects are grayscale-tinted, Empty uses grass and odd numbered photos flip. Horizontal placement is clamped to prevent body cropping.

## Wave lessons

- Hint and voice: PASS. Hints update synchronously, Read speaks the current hint, the helper owns heard-state deduplication, and score events have distinct run keys. Checked five changes, five runs, Read and initial order speech.
- Focus and layout: PARTIAL. Native dialogs restore focus, controls stay in place, sticky hints reserve height, and keyboard arrows/Enter open cells. Phone resize during a tween preserves Run focus. Pure engine resize focus remains a follow-up below.
- Sizes: PARTIAL. Checked every required size, 44 px controls, compact inspectors and phone number size. Full toolbox access still requires scrolling in short previews and on phones.
- No giveaways: PASS. Counts, photos and neighbors are actual model evidence. There is no hidden correct-answer badge or fake result meter.
- Honest numbers: PASS. Fixed test denominators, synthetic-data disclosure, feature bars and all reference results were checked. With zero examples the model explicitly has no answer.
- Standards: PASS. Students collect a different training mix, refine a model from its errors, correct labels and examine unequal day/night outcomes. The shared family model was reused.
- Motion off: PASS. No infinite animations remain running, no scan is created, and results update immediately. All art is present.
- Short choices visible: PASS in the checked layouts. The compact inspector shows all four 44 px relabel buttons; the five k buttons fit at 1000 px. Long photo evidence lists intentionally scroll.
- Resize mid-animation: PASS in targeted phone tests and ordinary playback. The result remains 37/40 and Run retains focus across 375-to-760-to-375 resizing.
- Deferred welcome: PASS. The two-mode helper uses no welcomeAfter. First actions speak their own line; the initial Work Orders entry speaks its welcome and order title in order.
- Unknown as unknown: PASS. Zero training produces No answer, rather than an invented animal prediction.
- One look, one meaning: PASS. Colored letters identify classes, diagonal outlines mark correct cells and red X notches mark errors. Night tint affects images, not answer tags or notches.
- Truthful badge: PASS. Stale results gray immediately; live goals and Next reflect the last completed run and pending edits disable advancement.
- Hint changes back: PASS. Returning to a completed order restores the Goal met hint. Closing its inspection restores the repair note.
- No answer by word copying: PASS. Repair controls are real model levers. The debrief names the fault after a successful repair.

## Audit leads

Audit not finished. Ran audit_tool.py once on port 9971 with host port 8775, under a 2400-second limit. It generated 54 frames and continued walking controls, then the limit terminated it. It did not produce audit.md or a complete leads list.

Inspected every generated audit frame. Visible issues repaired with targeted checks: hint loss while the toolbox scrolls, phone Run access, short-screen inspector choices, zero-model cell sizes, answer-tag consistency when opening test photos and night notch colors. Additional targeted checks cover all eight label edits, completed-order inspection, Read ordering and Reset during a tween.

The full audit was not rerun after repairs, as directed. Completed targeted drive batches reported no tool console errors, warnings or exceptions. One earlier host-only favicon 404 was removed by giving the temporary host a data favicon; later phone batches had no errors.

## Frames looked at

Inspected 87 manual PNG frames and 54 audit PNG frames, individually or on contact sheets, plus the final-size art and bar comparison. Evidence stays under _scratch/model-mechanic/.

Manual coverage includes every STANDARDS size in both modes, the complete order sequence, goal reversal, all reference scores, day/night filtering through the UI, drawers, large photos, label repair, zero/max training, Mask-only, grayscale, Motion off, keyboard navigation, resize and mid-tween input. Final art frames were inspected after rekeying.

## Art made

9 finished images: 7 new OpenAI gpt-image cutouts and two preserved FLUX clearing backgrounds. No people. Full prompts and provenance are in art/prompts.json; raw new images are in art/raw/.

Art totals 481,704 bytes, about 470 KiB. The final offline bundle is 745,046 bytes, about 728 KiB on disk, under 2 MB. The bundler reports 725 KB before on-disk line-ending overhead.

No generation redraws were needed. Rekey processing was repeated to remove magenta and blue fringes. Final options use holes=true and despill=false. Inspected the final scene, deer inspector, preview and all seven cutouts at final asset size.

## Art still to paint

None missing. Fine key-colored edge specks remain visible on some isolated cutouts at full resolution; their final forest composites were inspected. This is a possible future matte refinement, not a placeholder.

## Engine changes wanted

See handoff.md for exact files and functions: preserve cell focus in ml-lab resize redraws; allow separate truth rows and prediction columns for abstention; fix the art pipeline's sequential magenta despill mask. No shared engine or script was edited.

## Left open

- A completed mechanical audit remains open. The 40-minute run timed out, and scoped rechecks do not replace it.
- Short previews and phones scroll for training controls, complaints, longer repair notes and evidence. Run is sticky and the phone matrix/hint fit initially; all primary controls fit together on the specified laptops.
- Browser narration is unrecorded, as required for this build. The science-narrator selection and 53 lines are prepared; actual voice identity and offline speech depend on installed browser voices.
- Pure ResizeObserver redraws inside the shared matrix engine can still require focus work. The tested phone Run focus path passes; a full matrix-cell resize focus audit was not completed.
- Zero training uses a fifth No answer column plus an unused zero row because the engine is square. A relabeled example can also make a zero-count animal label predictable; the spec's blanket statement has that label-edit exception.
- Kept the spec's painted-cutout direction: only Size changes the painting; all four numeric clues appear as bars. This open-question decision and the clamped horizontal placement are recorded in handoff.md.
