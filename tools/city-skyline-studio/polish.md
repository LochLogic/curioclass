# Polish: city-skyline-studio (Codex fix, round 1)

Evidence root: `_scratch/city-skyline-studio/`. Before and after shots used the same
1366x768 states unless a different size is stated. The initial driver failure was
retried once, smaller, successfully. No commits. refine.md and refine/ were not edited.

## Blocker

1. FIXED. Snap and Check share inkTargets with horizontal:false; screen upright only at Tilt 0. Three flat lines changed from 0 misses plus reflection to 3 dashed red misses and no reflection. Near-flat Snap changed from horizontal to free. Tilt 15 also rejects all three; Turn 0/90 still snap to infinite side VPs. Evidence: fix-before/before-flat.png, fix-before/before-snap.png; fix-after/after-flat.png, fix-after/after-snap.png; final-ink-patterns.json.

## Should fix

2. FIXED. Only receding side-VP lines count; upright-only drawings cannot finish. Zero-red completion asks how the student aimed, rather than what they changed. Evidence: before-upright.json versus after-upright.json; proof-ink-patterns.json; fix-voice/aiming-reflection.png and .json show three real drags, checkAim once, and the neutral question.
3. FIXED. Exact per-setting percentages are removed from visible feedback; only off settings appear. The overall meter uses 25-point steps and reaches 100 only on a match. The original numeric-inversion attack can no longer read an eye or turn percentage. Evidence: before-score.json, after-score.json, proof-find-cheats.json and corresponding frames.
4. FIXED. Kept the specified 3 m and 2.5 m cameras, allowing 0.6 m eye error below 10 m. The former 2.4 versus 3 m miss, despite a 4.809 px horizon gap, now matches. Both low targets accept +/-0.6 m, reject +/-0.9 m; no eye stop passes. The reading hint uses horizon crossings near the bases, without claiming visible roofs. Evidence: before-street.json, after-street.json, proof-find-tolerances.json.
5. FIXED. The fact names only the tank's uncovered underside and checks samples against nearer painted faces. No tank and covered tank both suppress it; the visible tank enables it. The notes question names the tank, not setback tiers. Evidence: before-bottoms-no-tank.json and fix-before/before-bottoms-no-tank.png; proof-bottoms-no-tank.json, proof-bottoms-visible.json, proof-bottoms-occluded.json and their fix-support frames.
6. FIXED. Buildings precedes Readouts; the laptop hint reserve is smaller while retaining four readable lines. At 1366x768 Buildings moved from y=935.86 to 668.06 and all five palette buttons are at y=701.45..755.64. Overlays also stays visible. Ink controls stay before Readouts. Evidence: before-fold.json, after-fold.json, fix-final/final-build-1366x768.png and final-ink-1366x768.png.
7. FIXED. Build selects its next rung from completed actions and a current Tilt cue. Turn-first gives Guides in both hint and Read; Guides-first gives buildNext. Evidence: before-turn-first.json, after-turn-first.json, proof-guides-first.json; fix-voice/guide-bridge.json speaks guidesHow then buildNext.
8. FIXED. inkMore is suppressed during checking. First red line queues checkFix as a once-only how-to. Evidence: before-check-voice.json versus after-check-voice.json; fix-voice/main-check.json has checkHow and checkFix once, inkMore zero across two bad lines. The revision side path then speaks checkReflect once.
9. FIXED. Each missed check has a unique short result event; its reading how-to remains once. Evidence: before-repeat-miss.json versus after-repeat-miss.json; fix-voice/find-five-misses.json contains five miss events and one findEye after five real held checks at a 2 s pace.
10. FIXED. findLens ends with Pick a lens, then press Check camera. Evidence: before-lens-how.json, after-lens-how.json; fix-voice/lens-action.json shows the new line actually spoken after the miss.
11. FIXED. welcomeBuild requires a city and its pending eye step; emptying the city queues addFirst once. Evidence: before-clear.json versus after-clear.json; fix-voice/empty-city.json and .png. The earlier welcome was cut as the city emptied; returning to Build did not repeat addFirst.

## Polish accepted

12. FIXED. The current fact is visible on the Build stage at 1366x768, y=722.45..756, rather than below the panel at y=1376.17. Stacked layouts put it under the hint so it does not cover the drawing. Evidence: after-fold.json, fix-final/final-build-1366x768.png; the affected 760x900 and 375x812 Build frames were re-shot and viewed. The final right-side placement also leaves zero Plan overlap at 1366x768 and 1920x1080: overlay-plan.json, overlay-wide-plan.json and fix-overlay frames.
13. FIXED. Stacked hints have min-height 0 and take their text height: 23.19 px at 760x900 and 46.38 px at 375x812 in Build. Evidence: final-build-760x900.json, final-build-375x812.json and their frames; the affected 760x900 and 375x812 Build frames were re-shot and viewed.
14. FIXED. The hint says Most of your city and leads with Press Auto, with the wider-lens option conditioned on Auto. Auto restores the city from a -600% manual horizon. Evidence: proof-off-city.json, proof-off-city-auto.json and fix-support frames.
15. FIXED. The big panel button reads Next target after matches 1 to 5 and Start over on target 6. All six labels were checked in proof-find-tolerances.json, and the target-2 frame shows the large Next target button. Real held panel-button clicks advance to target 2 and, on the last target, return to target 1 with Tilt 0: final-panel-next.json and final-panel-start-over.json.
16. FIXED. offPage is Build-only. Find entry with no camera action speaks only welcomeFind, with no offPage delaying Check. Evidence: fix-voice/find-entry.json and .png; the subsequent five checks all speak their result. The held Build stop path still speaks offPage once: overlay-build-offpage-voice.json.
17. FIXED. Stage text grows with the large stage: 12 px becomes 14.4 px and 13 px becomes 15.6 px at 1920x1080, with actual stage width 1560 px. Evidence: proof-wide-type.json and fix-support/proof-wide-type.png; final-build-1920x1080.png.
18. FIXED. Narrow Find VP chips use short names at the stage edges, with extra bottom framing room. Viewed all six 375x812 targets; the chips stay beside the amber outline. Evidence: fix-final/final-find-375x812.png and phone-target-2.png through phone-target-6.png.
19. FIXED. Readouts and notes say the picture stays upright like a drafting view and Tilt shows the real lean. Evidence: proof-drafting-note.json and fix-support/proof-drafting-note.png with the 48 degree down readout.

## Settled calls

- Applied: Rule 5 does not apply; contract kept. No sensitivity file was present.
- Left the composition-brief open question to the spec owner. No new feature or topic was added.
- Used the suggested visual allowance for the low targets, keeping the listed target cameras. No questions were asked in this unattended session.

## Cheats tried

- Three flat strokes at Turn 30: 3 misses, reflection closed. Same at Tilt 15: 3 misses, closed.
- Three uprights: 0 receding lines, closed. Uprights placed on a VP's screen column: closed.
- Three Tilt-15 upright strokes aimed at VP 3: 0 receding lines, closed. Erasing the only red stroke leaves a missing-line message; replacing it with an upright still cannot complete. Evidence: final-tilted-uprights.json and final-erasure-and-uprights.json.
- Original per-setting-percent inversion: neither numeric eye nor turn feedback is available; the initial camera remains unmatched.
- All five eye-stop buttons, with every other setting correct, for every target: 0 matches in 30 attempts.
- Sweep all four lenses with the untouched default eye and turn: 0 matches in 4 attempts.
- Low-target tolerance: +/-0.6 m passes; +/-0.9 m fails on both. Sidewalk stop still fails on target 6.
- Positive controls: all six exact hidden cameras match; three actual receding edges open the neutral aiming reflection; a red edge undone and redrawn correctly opens the revision reflection.
- Check tests line direction, not placement on a face. That optional nit remains as listed in refine.md.

## Voice walk

Held clicks were 120 ms, with a 2 s action pace, using scripts/drive.py and its CDP helpers.
Main path heard: welcomeBuild, turnHow, guidesNext, guidesHow, composeGoal, welcomeInk, checkHow, checkFix.
The add action completes the bridge step before buildNext starts; a separate held Guides-first path heard guidesHow then buildNext.
Fresh correct-edge path: checkHow, checkAim. Revision path: checkHow, checkFix, checkReflect.
Find: welcomeFind; five missed checks each speak a miss event, then findEye once. Lens path speaks findCheck and findLens once.
Empty city: welcomeBuild while the city exists, cut on clear, then addFirst once. No welcome over the empty city.
voice/lines.json equals allLines(), 45 strings. Matching recordings remain; revised strings use browser speech fallback. No audio was recorded.

## Checks and frames

- Final bundle: 904016 bytes. No tool network requests in the measured resource lists. JSON manifests validate; allLines and voice manifest are equal at 45 strings. git diff --check is clean. refine.md and refine/ have no diff; the temporary host file was removed.
- Viewed all 88 fix frames, including five final overlay frames. The first 83 comprise 13 before, 12 direct after, 12 supporting probes, 8 voice paths and 38 final-size/target/regression frames. All three modes were shot at all eight STANDARDS sizes. Only affected stacked Build frames were repeated after the fact was moved below the hint.
- The first phone host fixture requested a missing favicon. The temporary host now supplies a data favicon; subsequent phone runs are clean. This was a host-page request, not a request by the bundled tool.
- Motion off plus grayscale was viewed at 1366x768. At 1920x1080, 20 buildings with Guides and Windows averaged 3.44 ms per draw over 60 draws, below the 16.67 ms frame budget. This measures draw cost, not display refresh rate.

## Feel check

The best moment remains lifting the eye and seeing the city turn into a rooftop plan while the guides remain exact. The two flat moments were hunting below the fold for Buildings and nudging an unreadably precise street-eye answer; both are addressed above. The sky painting, shaded architecture, tank details and play remain. Compared the final 1366x768 frame with the existing Beat Lab bar frame, without writing to that other tool.

| City Skyline Studio | Beat Lab bar |
|---|---|
| ![Current city](../../_scratch/city-skyline-studio/fix-overlay/overlay-default.png) | ![Existing bar frame](../../_scratch/city-skyline-studio/bar-frames/beat-lab.png) |

## Engine changes wanted

None. All changes are tool-local, using the engine's existing target options.

## Audit

Audit not finished. The one required run used port 9921, host 8725 and a 40 minute hard limit. The session was cut after the Ink control walk. Its saved report has 99 leads at fix-audit/audit.md. The full audit was not repeated after restart.

- Intentional overlays: canvas/hint, Check/Extend, target labels and fact chips share the stage. The compact hint has pointer-events:none, so hit-test samples see the canvas beneath it. The readable compact frames confirm these leads do not mean hidden text.
- Corrected after the partial audit: the lower-left fact chip covered the Plan legend. It now sits on the right, is constrained away from the Plan, and canvas labels reserve its rectangle. Targeted fix-overlay/overlay-plan.png, overlay-wide-plan.png and overlay-third-vp.png were viewed; their matching JSON records all measure 0 square pixels of Plan overlap. The saved audit predates this small overlay correction.
- Known scrolling limits: secondary Building editors, Overlays and secondary Ink/Find controls scroll in stacked and compact layouts. The stage copies of Check camera and Extend remain available. The 1366x768 palette is visible. The strict rule that every secondary short choice set stays visible simultaneously remains unmet.
- Empty-city hint-out-of-view: Clear city retains the panel scroll position. The palette remains visible and addFirst was heard once in the held-click path; the hint is above that panel position. This scrolling limitation remains.
- Helicopter keep-region 93%: the audit had scrolled the portrait page to reach Overlays. Viewed its 760x900 frame; the top of the stage is above the scrolled viewport. The initial unscrolled size frames are recorded separately.
- Audit phone failure: iframe context not found caused the automatic 375 check and its no-hint lead. Direct drive.py host runs read the real 375-wide iframe, saw its hint, checked every mode and all six targets, and produced clean frames. The automatic audit phone check remains unverified.
- Welcome leads: eye stops, longer lenses, Guides and palette additions have their own first-tap line, so STANDARDS requires skipping the welcome unmarked. Read and Sound also intentionally interrupt or skip it. The explicit main voice path heard all required lines.
- No-op leads: Ink canvas needs a drag; Clear drawing was tested on empty ink. Real drags and revisions were checked separately. Clear drawing remaining enabled when empty is an accepted optional nit.
- Other-controls-moved leads are mode changes and the Sun dial opening. Completed Build/Ink control rows have no runtime errors or failed settled Enter paths.
- Completed portions: sizes/states (with the phone-context limitation), Motion off, and Build/Ink one-control walks. Find control walk, five-click/rapid-tap audit stages, and mid-action resize/stress stages did not finish. Their placeholder clean/none lines are not claimed as passes. The separate targeted five-miss voice walk passed.

## Left open

- The spec owner's composition-brief question and the optional nits remain outside this pass.
- Source facts use the existing Joseph D'Amelio construction and Szeliski pinhole sources in spec.md; underside visibility is verified against the actual painted tank faces. No replacement unsourced fact was added.
- Full audit completion remains open because of the session interruption, including the unfinished stages listed above.
