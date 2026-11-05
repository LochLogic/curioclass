# Director's Chair build handoff

## Cold review, 2026-11-03

- Played all five houses before reading this handoff or the builder report. Review evidence is in
  `_scratch/director-s-chair/review-*`. No shared engine edits or commits.
- Fixed a stale Adjust selection on entering a new house, a panel minimum-width overflow when the program
  opens, stale queued Seat guidance, and Compare gestures that used the last Tour beat instead of the
  displayed Compare beat. Scene focus now starts at the first offered choice.
- Notice headings identify the originating beat when blocking carries forward. Hidden-Guard feedback
  explains dashed figures and directs the student to Seat. The specified commedia coordinates remain intact.
- Added student-facing context that each staging is a directing adaptation, not a historical reconstruction.
- Refined code figures with shoulders, sleeves, robe folds, belts, trousers and zanni costume detail.
  Five new mask object images use `mask-*-review` tokens. The originals remain available. All moving actors
  stay figures in code, as the owner requested. Prompts, provenance and final image checks are recorded.
- Fresh cultural check: `_scratch/director-s-chair/review-sensitivity.md`. No offensive imagery found.
  Left open because the spec is exact: Noh shite masking is not universal, and the bridgeway rule omits the
  chorus/attendant entrance. The supplied commedia mock positions also conflict with the intended front-seat
  focus. These need spec decisions, not a silent implementation change.
- Independent numeric check: 426 assertions over 40 branching combinations passed. The direct Noh exit
  is 14.534 m from the chorus-sings position (36.336 s at 0.4 m/s), not the spec's 14.0 m estimate.
- Recorded narration remains absent under the build/review instruction not to record audio.
- The single review audit finished: 38 leads. Fixed the 29 compact Adjust overlap rows; explained the nine
  intended scrolling/inset/disabled-probe rows in `_scratch/director-s-chair/review-audit-dispositions.json`.
  Compact Adjust now stacks controls above the plan and gives the phone workbench more room. Dense actor
  initials and pose tags become linked callouts; the seat label stays clear. `clarifyPlanLabels` is a local
  display-only finish, called after the engine plan update. True actor/seat coordinates remain authoritative.
- Repair checks at 680, 800, 1000, 760, 1366 and 375 widths were clean, with further Greek/Noh label and real
  compact drag checks. The full audit was not rerun after these scoped repairs. No second full review.

Build only, 2026-11-01. No commits, no shared files changed, no polish round.

## What was built

One offline HTML tool with Tour, Arrival, Scene and Compare; five historical house configurations; the eight
Antigone beats; 30 directing options with the supplied notices; three seats per house; live ground plans;
soft-rule Adjust; realist room lights; program notes; and a saved 600-character director's note.

The reusable source is `src.html`. `director-s-chair.html` is its generated bundle. `tool.draft.json` stays at
stage built for the cold review. Voice lines are listed for science-narrator / Charon, with browser speech as
the build's fallback. No audio was recorded, as instructed.

## Source map

- DATA holds the exact script, house rules, dates, options and notices extracted from the spec.
- HOUSES supplies geometry, levels, blockers, seats and camera framing to Stage.house.
- initialSnap, applyChoice and makeBeats build deterministic branching snapshots. Choices carry forward;
  the script's Noh center arrival, Globe balcony preparation and Creon's exit are separate presets.
- WEIGHTS replaces body-position points with a mask-aware term and adds chorusGaze and audience address.
- renderTour, arrive, renderScene and renderCompare own the four page layouts. Scene controls stay mounted
  between beat changes. The script itself scrolls; short directing choices remain outside its scroll region.
- animate uses Stage.play for each straight segment. The commedia lazzo has repeated segments. Noh turns at
  the bridge junction so an entrance or exit follows the bridgeway. Play scene holds each beat for two seconds
  after its crossing. Stop and navigation cancel through a generation token.
- Stage.view.house and Stage.view.plan provide the live camera, sightlines and coordinates. decorate adds
  projected architectural finishes. paintFigures uses engine-projected boxes and real sight status to restore
  code figures after background blockers, draw directional masks and show the mocking gesture.
- Curio.voice owns narration. How-to lines use heard-state behavior, every switch updates the hint immediately,
  Play scene hushes narration, and Read returns no line while the scene is playing.
- Save persists only choices and the director's note, under curio-directors-chair. Exploratory Adjust edits and
  light levels last for the current visit. Clear removes the storage item and current choices.

## Art made during this build

Built-in OpenAI image generation produced five object masks and three replacement venue illustrations. All
are in `art/raw/`, processed only with the free `scripts/art.py director-s-chair --rekey <name>` form, and used
as art tokens. `art/prompts.json` contains the prompt set, style, dimensions, provenance and review status.

New mask outputs: `art/mask-greek.webp`, `art/mask-noh.webp`, `art/mask-zanni.webp`,
`art/mask-capitano.webp`, `art/mask-dottore.webp`.

New venue outputs: `art/greek-theatre-v2.webp`, `art/noh-stage-v2.webp`, `art/globe-playhouse-v2.webp`.
The original three assets remain on disk, as required. Commedia and realist venue paintings were retained.
The Greek redraw removed an invented raised orchestra; Noh now shows a distinct bridgeway and roofed stage;
the Globe redraw leaves the yard open to the sky. Every final WebP was inspected. No generated people.

## Open question decisions

- Masks: the owner explicitly settled the spec's only open question. Paint the five masks as objects. They were
  generated as empty theater props, while all actors and moving masks remain figures in code. No people painting
  or outside review is pending for these assets.

## Numbers and interpretation

Contrast recomputed in `_scratch/director-s-chair/numbers.py`: orange on panel 8.493:1, on section 8.048:1,
brand ink on orange 9.061:1, ink on panel 14.704:1, muted on section 7.706:1.

The given direct Noh entry endpoints are 12.226 m apart, or 30.566 s at 0.4 m/s. The given exit endpoints are
14.534 m apart after the chorus-sings option and 14.970 m from the default center, rather than the spec's
14.0 m estimate. The actual animation follows a bend at (-2.7, 6), so it takes longer again. Other center
crosses also take time. Use the full-play timing evidence in Scratch for the measured complete performance;
the screen does not promise an 80-second duration. Coordinates were preserved rather than shortening the
bridge. The eye-pillar position is 0.922 m from the pillar center; 0.6 m is its horizontal clearance.

The engine eye is a rough guide, not a verdict about art. The fixed commedia notice describes a mocking zanni
stealing focus, but the specified collinear positions can hide him behind the Capitano from the front seat.
The focus line reports this honestly; another seat reveals the copying. This tension is in the supplied
blocking and notice, not a changed coordinate.

## Engine changes wanted

- `kit/stage.js`, `houseView`: depth-sort house blockers with actors and pieces. Currently blockers draw after
  every actor when curtainY is null, including a backcloth behind an actor. The tool repaints code figures from
  the engine's projected boxes, respecting Stage.sight, to avoid a wall washing out a visible actor.
- `kit/stage.js`, `figure`: orient mask shapes to the actor's facing and hide them on a full-back head. The tool's
  code figure finish does this without changing the engine.
- `kit/stage.js`, `play`: accept optional within-beat waypoints and a linear-speed mode for the Noh slide. The
  tool uses sequential Stage.play segments with distance-based timing; the engine eases each segment.
- `kit/stage.js`, `houseView`: offer a scene decoration callback using the engine camera after architecture and
  before figures. The tool currently draws architectural detail with Stage.view.camera after each engine draw.

## Review focus and remaining limits

- Small Compare grids scroll so venue images and notices retain a readable size. Beat controls, note and Save
  stay visible. Small scene script boxes scroll independently; eight beats remain in the script.
- Detailed masks are best enjoyed in Arrival; compact scene legends shrink to keep the moving view usable.
- The engine's geometrical figures and projected scenery intentionally remain diagrammatic enough to expose
  blocking and sightlines. The venue paintings establish the sense of place.
- No recorded narration, no new family-engine changes, no publication, and no commits.
- Build evidence, screenshots, generation QA, the numerical checks and the single audit live under
  `_scratch/director-s-chair/`. The final codex-report.md records verified results and audit dispositions.

## Final build checks and targeted repairs

All five complete performances reached all eight beats in order. The full Noh entrance and bridge exit took
95.05 seconds, with no narration during playback. Motion off retained the Greek default's 17.91-second pacing.
The mask body-position, house-specific address and realist-only light terms passed direct engine checks.

The single mechanical audit produced 79 leads. Each is classified in
`_scratch/director-s-chair/audit-dispositions.json`: 69 addressed by shared fixes in this tool and 10 accepted
because they describe the required scrolling gallery, intentionally disabled Compare button, inset overlays
or long program text. No exceptions, resize locks or infinite calm animations were reported.

Targeted repairs after that audit: explicit 44 px Tour width, focus on Begin after Arrival, no late focus steal
after a choice tween, quiet text-free miniature plan, a sticky program action row, explicit note-field name,
and an idempotent Tour button that leaves its welcome uninterrupted. Playback also keeps current Adjust edits
instead of rebuilding them from presets. Real held input and a jittered drag checked these changes. The full
mechanical audit was not rerun after the targeted repairs.

A final Noh geometry check found (-2.4, 5.4) clear from the front and hidden from the side by pillar2, with
four of five face rays blocked. A dragged Greek Guard at about (4.05, 11.89) kept that position through Play
and Next, proving Adjust carry-forward. All started Chrome instances and host servers were closed; host.html
was removed. The final source and bundle hashes are in Scratch's final-validation.json.
