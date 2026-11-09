# Dancers on Tour: review handoff

## Structure
`src.html` contains styles, the original piece and venue data, model functions, the audienceRenderer adapter, the plan, warm-up controls and events. `window.__tool` exposes the model and voice log. All review scripts and evidence are in `_scratch/dancers-on-tour/`.

## Painted dancers
The owner asked for painted dancers. Three generated `people: true` cast atlases now supply five poses in front, back and right profile; right mirrors for left. Six dancers retain their identity, skin, hair, build and clothing across the set. The middle step doubles as the raised Circle, and arms-wide doubles as jump preparation. Turning uses four readable facing keyframes. No kit code figure is displayed.

`PAINTED_POSES`, `painted-dancers.json` and `audienceRenderer.setup/resize/draw` form the swap boundary. The JSON holds tight [x,y,width,height] cells by view, pose row and dancer index. Keep raw atlas dimensions 1086x1448 or update the adapter. Height is normalized against each dancer's standing row so a low crouch stays low. Projection, independent dancer position and depth ordering still use Dance.floor. The owner contact sheet is `_scratch/dancers-on-tour/painted-contact.jpg`.

## Review repairs
- Low point totals no longer turn Safety green when the warm-up is too short, out of order or includes long holds. Points remain the spec's exact sum. The complete checklist feeds Safety and ready, as the warm-up mode requires.
- Note praise fires only when an edit actually changes a note from unmet to met. Default notes do not earn praise after unrelated warm-up taps.
- A completed run recaps the number of phrases that kept fit, spacing and sightlines throughout the run. Failed runs use a neutral completion sound rather than the success chime.
- Phone Adapt packs Spread/Run/Reset, Front, Tempo and Swaps into a compact control desk beneath the plan, retaining 44px targets.
- All existing venue paintings, surface textures, music, precise plan geometry and live edits remain.

## Spec conflicts left open
Do not relax the sight thresholds to manufacture completion. Independent review recomputed the formation numbers and searched possible low sample seats within the stated audience areas; no common low seat could see all four fit/spaced/note-compliant formations. With the current sample seats no whole venue can meet all-green. In particular the theater's all-nine-seat note is unreachable. `numbers-review.json` records the search assumptions. This is a blocker requiring a content decision under CODEX-REVIEW section 3.

The explicit gym risk formula leaves 2 hard-floor jump points after a complete warm-up, whereas Done when 4 says that preparation should make it green. Kept the explicit formula and the safer amber result. A warm-up does not remedy floor impact. The distances, minutes, temperatures and points are authored model thresholds, not medical prescriptions.

The park note now checks every straight travel segment as well as the four formations. Default endpoint clearance is 1.0 m, yet dancer 4 crosses the sprinkler exactly between Window and Circle. The repaired check rejects that path. A discrete search found no joint Fit/Spacing/sprinkler solution at the available controls with the current straight paths. That is another authored-constraint conflict; do not clear it by pretending endpoint clearance proves travel clearance.

## Voice
Curio.voice uses wise-mentor, with browser fallback and no recorded clips. All fixed lines are in voice/lines.json. Run hushes narration and intercepts Read, as the spec requires. The main path and side/repeat logs are in review scratch. How-to lines are once per page; tooClose remains an event on each transition into inadequate spacing.

## Sensitivity
Bodies and preparation are involved. Inspect the full painted contact sheet for anatomy, ordinary releve rather than pointe, consistent identities and natural representation. No body is scored or presented as the ideal dancer. The cast does not portray every ability; no unsupported claim of universal representation is made. The invented dance claims no cultural lineage.

## Engine changes wanted
None. No kit, scripts, docs or other tools were changed.

## Verification
See codex-review.md for the final bounded audit, confirmed leads, frame evidence and remaining conflicts. No commits were made.


## Final review checks
One full review audit completed within 40 minutes: 279 mechanical leads, 95 frames. Every frame was inspected through contact sheets and focused full-size views. All default sizes, Motion off, resize stress, console checks and held/quick click checks completed. Most leads measure overlapping transparent dancer targets or unpainted closed-disclosure text. Dense real taps select the nearest dancer; an expanded disclosure leaves 24px before privacy text.

Post-audit repairs and scoped checks: phone warm-up menu plus all twelve reorder arrows fit above 660px at 375x812; real drag reorders; resize moves the list between stage and panel without losing focus or scrolling. Theater rings are separated. Sound-on after edits recovers valid instructions in all three modes. The repeated main voice walk starts all three mode instructions once and stays silent during Run. Run captions clear on edits/reset; reset preserves other venues. Live spread, swap and tempo edits keep the clock moving.

The active art list contains nine delivered images. The 32 superseded single-figure prompt records are preserved under superseded_assets, rather than left in the active paint queue. Verification receipts and final bundle SHA-256 are in `_scratch/dancers-on-tour/review-verification.json`. No second full audit was run. Long explanatory notes and preparation checks still scroll on short screens.
