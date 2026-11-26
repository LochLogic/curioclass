# Director's Chair: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: director-s-chair

#### Built

- Build only in S:\CurioClass-codex. No commits, branch operations, shared-engine edits or polish round.
- One offline tool: five painted house cards, rules and mask casts, eight script beats, 30 directing options,
  three seats per house, live plan, Adjust, realist room lights, program notes, Compare and local saving.
- All required source, metadata, teacher notes, voice lines, audit states and handoff files are present.
- Browser speech is the fallback. science-narrator / Charon is declared in voice/lines.json; no clips were recorded.

#### Numbers check

- `_scratch/director-s-chair/numbers.py` recomputes the spec's geometric distances and contrast ratios.
- Orange on panel 8.493:1; on section 8.048:1; brand ink on orange 9.061:1. Ink on panel 14.704:1;
  muted on section 7.706:1. The spec's rounded contrast values agree.
- 133 numerical checks passed, using exported snapshots for every house's eight choice combinations.
  They include all specified option endpoints, Greek entrance carry-forward and mask body-position points.
- Mask positions at 0, 45, 90, 135 and 180 degrees score 2, 1.5, 0, 0 and 0.
- Address terms are 0, 0, 2, 2, 0 for Greek, Noh, commedia, Globe, realist. Only realist lights affect focus.
- Difference: the direct Noh exit is 14.534 or 14.970 m, depending on the previous choice, not 14.0 m.
  Following the bridge junction makes the route longer. The measured whole-bridge entrance and exit run was
  95.05 seconds. Coordinates and the 0.4 m/s timing rule were retained. See handoff.md for the full calculation.
- Difference: the eye-pillar spot is 0.922 m from the pillar center; 0.6 m describes its horizontal separation.

#### Feel check

- Played all five complete productions. Each reached beats 1 through 8 in order and stopped at beat 8.
- Best moment: changing to the Greek side wedge reveals how the chorus shapes attention and how a Guard can
  become partly hidden. The same words read as a different relationship from that seat.
- Flattest moment 1: the first house views were generic engine solids. Added projected masonry, pine painting,
  beams, painted town cloth, oak framing, wallpaper, window, door, lamp and shaded code figures.
- Flattest moment 2: the small plan initially drowned the action in labels. Made it a quiet seat inset by default;
  Adjust enlarges it and restores editing. Enlarged the Globe's useful camera framing around the performance.
- Compared our Tour with Beat Lab and inspected Snowy Mail Route. The side-by-side frame is
  `_scratch/director-s-chair/feel-comparison.png`. The painted invitation carries its own visual identity;
  production views remain movable geometry rather than pretending the paintings can test sightlines.
- A 95-second Noh pass deliberately asks for patience. Seat, Next beat and Stop keep it responsive.

#### Done when

1. PASS: all five full playback records contain beats 0 through 7 in order, final playing=false, last=7.
   Five matching end frames were inspected in `verified-playback/`.
2. PASS: 133 numerical assertions passed over every choice combination; entrance positions carry forward.
3. PASS: exact supplied notices and current-seat focus. At Noh (-2.4, 5.4), the Guard was clear from the
   front and hidden by pillar2 from the side, with four of five rays blocked. A wider final search and the
   corresponding side-seat frame confirmed the example.
4. PASS: mask body-position points, address-house gating and realist-only light terms were computed directly
   from the running bundle in `mechanics.json` and `edge.json`.
5. PASS: three choices populate a program note; two completed houses enable Compare; all five staged views
   and beats 1, 4, 6, 8 are supported. Audit states stage two houses through real inputs.
6. PASS: a real jittered drag outside the Greek orchestra kept the move and displayed the house-rule note.
   Noh standing-chorus and realist full-front warnings were also checked.
7. PASS: House view width 887.9 px at 1366 px, or 65 percent. Choice beside it; five Tour paintings fill the
   stage; all five mask objects are visible beside their roles in Arrival and in the scene legend.
8. PASS: held-input Noh Play, Seat, Next immediately changed seat and reached beat 2 with the entry completed.
   Play scene again stops; generation-token cancellation protects every subsequent action.
9. PASS: saved choices and note equaled the reloaded values; Clear removed the storage key, current choices
   and note; a second reload stayed empty. Evidence: saved.json, reloaded.json, cleared.json, reloaded-clear.json.
10. PASS: scene view, Next and both choice buttons were inspected at every STANDARDS size, including the
    375x812 iframe on host 8795. No sideways overflow. Preview script text is 11 px; small script boxes scroll.
11. PASS: 120 ms held taps at a two-second pace produced no repeated spoken how-to key. Full Noh, Globe and
    realist records show no speech during Play. Read during calm playback returned empty speech. No em dashes
    in generated HTML, notes or metadata. Calm playback kept all beats and took 17.91 s for the Greek default.

#### Wave lessons

- PASS, hint and voice: hints update in the action handler; Curio.voice owns heard-state behavior and Read.
  The held-tap log shows a stale seat hint dropped when Seat was already used, then spoken on a later notice.
- PASS, focus and layout: no focus taken on load; page transitions move focus deliberately; scene controls
  stay mounted and endpoint navigation moves focus off a newly disabled button.
- PASS, sizes: 44 px main controls; preview and laptop layouts stay side by side, phone controls stack.
- PASS, no giveaways: interpretive choices have no correct-answer badge, score or win state.
- PASS, honest numbers: the eye is labeled a rough guide; geometric dimensions and weights are described as
  the tool's own simplification. No invented claim of an 80-second Noh run appears on screen.
- PASS, standards: students use historical conventions to direct, observe, compare and justify a note.
- PASS, Motion off: no infinite animation remained in the grayscale calm frame; movement stops, pacing stays.
- PASS, short choices: the two directing options remain together and outside the script scroller.
- Resize during animation: covered by the single mechanical audit's state and resize checks.
- PASS, first-tap welcome: separate valid welcomes for Tour, each Arrival and Compare; no welcomeAfter delay.
- PASS, unknown state: Tour labels a house not staged until all three choices are actually made.
- PASS, one look / one meaning: fixed actor colors also have initials; selected seats have rings and names;
  hidden actors are dashed code outlines.
- PASS, truthful badges: staged status follows the three choices and clears on Restart house.
- PASS, reversible hints: seat, page, beat, choice and Adjust handlers set the new hint immediately.
- PASS, no copying an answer: no scored diagnosis or correct option; the student's final claim needs staging
  evidence, and different choices support different readings.

#### Audit leads

- Audit ran once and finished: 79 leads; no resize exceptions, disabled locks or infinite calm animations.
- All 79 rows are individually answered in _scratch/director-s-chair/audit-dispositions.json.
- Fixed: Tour width (4 leads), Arrival focus (17), miniature-plan label clutter (45), hidden program
  controls (1), explicit note name (1), interrupted Tour welcome (1).
- Accepted: scrolling Tour cards required by the narrow-layout spec (2), disabled Compare probe (1),
  specified inset / legend coverage of the canvas (6), long program text scrolling in the preview (1).
- Scoped rechecks measured Tour at 44 px; Begin received focus; Seat retained focus after a tween; both
  program buttons stayed visible at 680x425; note name and 600-character cap matched; a 0.7-second Tour
  double tap spoke one uncut welcome. A real drag also proved Adjust edits survive Play and Next.
- The full audit was not rerun after these targeted repairs. Final scoped batches had zero console errors.
- Every started Chrome and server was closed. Ports 8795, 9990 and 9991 are closed; host.html was removed.

#### Frames looked at

- Bar tools: Snowy Mail Route and Beat Lab, 1366x768, bundled into Scratch and opened before implementation.
- Initial Tour, Noh Arrival, Greek and Noh scenes, compact commedia; subsequent architectural fixes.
- All eight size conditions across Scene and Compare: 680x425, 800x500, 1000x625, 1280x720, 1366x768,
  1920x1080, 760x900 and 375x812 inside the iframe host.
- Every house, all five complete endings, choices, notices, program notes, mask casts, seats, Adjust drag,
  keyboard focus, saved work, cleared work, grayscale and Motion off.
- Primary size frames were opened individually. Repeated and audit frames were inspected in QA contact sheets;
  confirmed leads were opened at their native size. See Scratch for the frame folders and contact sheets.

#### Art made

- Eight images generated during this build: five object masks and three architectural redraws, using the
  built-in image tool. Ten images used, 615.35 KiB. Thirteen retained WebPs total, 921.82 KiB.
- Replaced the Greek raised orchestra, Noh missing bridgeway and Globe covered yard with newly painted
  sibling assets. Original files remain unused. Every final WebP was inspected after the free rekey step.
- Bundle: 1036919 bytes (1012.62 KiB). All images and code inline; no automatic network requests.

#### Art still to paint

None. The owner explicitly authorized the five masks as objects. All actors stay code figures.

#### Engine changes wanted

Four precise requests in handoff.md: blocker depth order, directional masks, waypoint / linear-speed playback,
and a camera-aware scene-decoration callback. No shared engine file was changed.

#### Left open

- Some supplied notices contain one sentence despite the generic two-sentence instruction. Their exact text
  was preserved rather than adding interpretation.
- The supplied commedia mock position can hide the zanni from the front seat while its fixed notice says he
  steals focus. Coordinates and notice were preserved; the focus line honestly reports the obstruction.
- Complete non-Noh runs measured roughly 18 to 21 seconds, near the low end of the spec's approximate 20 to
  30-second range. The Noh bend produces 95 seconds rather than the spec's approximate 80.
- No recorded narration was generated, as instructed. Compact Compare uses a scrollable grid; small scene
  scripts scroll independently. No cold review or polish was performed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: director-s-chair

#### Played

Cold as a grade 10 student, with projector layouts checked. Played all five houses before reading
the builder's report, handoff, notes or source. The venue tour invites exploration; changing seats is strongest.
All eight beats completed in each full playback, including the 95.22-second Noh entrance/bridge-exit production.

#### Findings fixed

- Blocker, general, Adjust: selected actor survived a house switch and could name a missing chorus member.
  Reset selection on arrival; keyboard and turn-button checks now keep a valid actor.
- Blocker, general, compact Adjust: controls covered the ground plan. Reflowed controls above the plan; gave the phone workbench more height.
  Kept the front-seat marker visible and linked crowded initials/pose labels to their exact tokens.
- Should fix, general, Program note: intrinsic panel width could push navigation sideways. Constrained panel
  and decision widths; opened program measured zero horizontal overflow at 680x425.
- Should fix, family:stage, Compare: costume gestures read the last Tour beat. Pass the displayed beat explicitly.
- Should fix, general, voice: queued Seat guidance could outlive its beat or seat. Bind it to house/beat/seat.
- Should fix, teaching, Arrival: historical adaptations were not identified on the student screen. Added context.
- Polish, general: start keyboard focus at the offered choice; label carried notices with their original beat;
  explain hidden/dashed blocking and name Seat as the next action. Program toggle now answers with sound and hint.
- Polish, family:stage: gave code figures shoulders, sleeves, robe folds, belts, trousers and zanni costume detail.
  Hidden copying gestures remain explanatory dashed marks. Turning during playback now stops the tween first.

#### Findings left

- Should fix, spec conflict: the Noh rules overgeneralize masking and bridgeway entrances. Shite roles are
  usually masked; chorus/attendants also use kiridoguchi. Exact spec text retained, as CODEX-REVIEW requires.
- Should fix, spec conflict: the commedia mock positions hide the zanni from the front seat, although the
  supplied notice describes him stealing focus. Coordinates and intended notice retained; visibility feedback
  and Seat guidance expose the difference. See the source/spec decisions in handoff.md.
- Polish, family:stage: lower-body/furniture depth remains schematic in the realist room. Shared depth-sort
  and decoration-hook requests remain in handoff.md; no kit files changed.

#### Flattest moment left

The long Noh bridge cross asks for patience. Its slow movement teaches the convention; Seat, Next and Stop
remain live. The weakest object art and the counter-like figures were lifted without simplifying the venues.

#### Graphics

All ten used images checked in their final exports and in Arrival/Scene. Five venue paintings retained.
Painted five new mask objects with built-in imagegen, processed only with free art.py --rekey, and inspected:
art/mask-{greek,noh,zanni,capitano,dottore}-review.webp. All are people:false; actors stay figures in code.
Full prompts/provenance: art/prompts.json. Fresh cultural image recheck found no offensive representation.
Final bundle: 1,071,875 bytes (1046.8 KiB); ten used images total 634.6 KiB.

#### Audit

Audit finished once within 40 minutes: 38 leads, 29 fixed and 9 explained. Chrome 9961, host 8765.
The nine retained leads are specified narrow Tour scrolling (2), a disabled Compare probe (1), and
specified canvas insets (6). Every row is answered in _scratch/director-s-chair/review-audit-dispositions.json.
Scoped repair checks used the audit geometry checks at six affected widths; Greek/Noh label checks and
a real compact-plan drag were clean. Only repair frames were re-shot; the full audit was not rerun.
Independent checks: 426 assertions over 40 choice combinations; mask points 2/1.5/0/0/0; matching voice manifest.
Scene and five-house Compare inspected at every STANDARDS size, including the 375x812 iframe; grayscale,
Motion off, keyboard-only choice, plan arrow keys, jittered real drag and the full eight-beat playbacks checked.
Motion-on Greek playback 18.08 s; Motion-off 18.08 s. No narration during any full playback.
600-character note and choices saved/reloaded; Clear removed the saved item and current work.

| Voice line | Kind | Expected in five choice changes | Spoken |
|---|---|---:|---:|
| choiceHow | how | 1 | 1 |
| programNote | event | 5 | 5 |

Held 120 ms inputs at a two-second pace checked stale speech and Read. App checks had no console exceptions.
The temporary iframe host alone returned a favicon 404; file-based tool checks were clean.

#### Left open

- Noh direct exit is 14.534 or 14.970 m, depending on the prior choice, rather than the spec's 14.0 m estimate.
  Engine easing and the bridge bend make the full long version about 95 seconds. Coordinates retained.
- Some supplied notices have one sentence despite the generic two-sentence requirement. Exact text retained.
- Recorded narration is absent because recording was excluded. Browser speech remains the fallback.
- Fresh cultural evidence and exact source links: _scratch/director-s-chair/review-sensitivity.md.
- Only allowed tool/Scratch folders changed; no commits. Every owned Chrome/server closed; host.html removed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Director's Chair build handoff

#### Cold review, 2026-11-03

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

#### What was built

One offline HTML tool with Tour, Arrival, Scene and Compare; five historical house configurations; the eight
Antigone beats; 30 directing options with the supplied notices; three seats per house; live ground plans;
soft-rule Adjust; realist room lights; program notes; and a saved 600-character director's note.

The reusable source is `src.html`. `director-s-chair.html` is its generated bundle. `tool.draft.json` stays at
stage built for the cold review. Voice lines are listed for science-narrator / Charon, with browser speech as
the build's fallback. No audio was recorded, as instructed.

#### Source map

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

#### Art made during this build

Built-in OpenAI image generation produced five object masks and three replacement venue illustrations. All
are in `art/raw/`, processed only with the free `scripts/art.py director-s-chair --rekey <name>` form, and used
as art tokens. `art/prompts.json` contains the prompt set, style, dimensions, provenance and review status.

New mask outputs: `art/mask-greek.webp`, `art/mask-noh.webp`, `art/mask-zanni.webp`,
`art/mask-capitano.webp`, `art/mask-dottore.webp`.

New venue outputs: `art/greek-theatre-v2.webp`, `art/noh-stage-v2.webp`, `art/globe-playhouse-v2.webp`.
The original three assets remain on disk, as required. Commedia and realist venue paintings were retained.
The Greek redraw removed an invented raised orchestra; Noh now shows a distinct bridgeway and roofed stage;
the Globe redraw leaves the yard open to the sky. Every final WebP was inspected. No generated people.

#### Open question decisions

- Masks: the owner explicitly settled the spec's only open question. Paint the five masks as objects. They were
  generated as empty theater props, while all actors and moving masks remain figures in code. No people painting
  or outside review is pending for these assets.

#### Numbers and interpretation

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

#### Engine changes wanted

- `kit/stage.js`, `houseView`: depth-sort house blockers with actors and pieces. Currently blockers draw after
  every actor when curtainY is null, including a backcloth behind an actor. The tool repaints code figures from
  the engine's projected boxes, respecting Stage.sight, to avoid a wall washing out a visible actor.
- `kit/stage.js`, `figure`: orient mask shapes to the actor's facing and hide them on a full-back head. The tool's
  code figure finish does this without changing the engine.
- `kit/stage.js`, `play`: accept optional within-beat waypoints and a linear-speed mode for the Noh slide. The
  tool uses sequential Stage.play segments with distance-based timing; the engine eases each segment.
- `kit/stage.js`, `houseView`: offer a scene decoration callback using the engine camera after architecture and
  before figures. The tool currently draws architectural detail with Stage.view.camera after each engine draw.

#### Review focus and remaining limits

- Small Compare grids scroll so venue images and notices retain a readable size. Beat controls, note and Save
  stay visible. Small scene script boxes scroll independently; eight beats remain in the script.
- Detailed masks are best enjoyed in Arrival; compact scene legends shrink to keep the moving view usable.
- The engine's geometrical figures and projected scenery intentionally remain diagrammatic enough to expose
  blocking and sightlines. The venue paintings establish the sense of place.
- No recorded narration, no new family-engine changes, no publication, and no commits.
- Build evidence, screenshots, generation QA, the numerical checks and the single audit live under
  `_scratch/director-s-chair/`. The final codex-report.md records verified results and audit dispositions.

#### Final build checks and targeted repairs

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

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
