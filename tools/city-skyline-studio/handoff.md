# City Skyline Studio build handoff

## Current fix round, 2026-11-04

The current list is refine.md, OPEN round 1 after the rework. The sections below this one are historical.
Only this tool and its scratch folder were edited. Shared kit files and refine.md were left alone.

- Ink uses one local inkTargets adapter with horizontal:false and a screen upright only when Tilt is level.
  Infinite side VPs preserve the level direction at Turn 0 and 90. Check counts receding side-VP lines, excludes
  screen uprights from that count, and uses an aiming question when no line needed revision. Erasing without
  replacement still leaves a missing-line requirement. checkFix is voiced on the first red line; inkMore is
  suppressed during checking.
- Find exposes only off settings and an overall meter in 25-point steps, capped at 75 until every setting matches.
  Street-level targets keep their specified cameras and allow 0.6 m eye error. No labeled eye stop passes.
  Each missed check queues its own short result event; the reading how-to stays once. findLens names the lens
  control and Check camera. The large panel button advances after a match, including Start over on target 6.
- The tank underside fact tests tank-bottom samples against nearer painted faces. Setback tier bottoms do not
  trigger it. The current fact sits on the Build stage. Teacher notes name the tank and explain the upright
  drafting view versus Tilt. These use the existing pinhole/construction sources and the tool's drawn geometry.
- Buildings now precedes Readouts. The shorter reserved laptop hint leaves both Overlays and the five palette
  choices visible at 1366x768. Stacked hints use their text height. Ink retains its controls ahead of Readouts.
  Build hints follow completed actions even when Turn or Guides comes first. Empty cities queue addFirst;
  welcomeBuild requires a city and a still-pending eye step.
- offPage is Build-only. Narrow Find labels are shortened into a bottom edge rail and framing reserves that rail.
  Canvas type grows with the large stage, reaching 14.4 px for a 12 px base and 15.6 px for a 13 px base at 1920.
- voice/lines.json equals allLines(): 45 strings. Existing matching recordings remain; changed strings use the
  kit's browser-speech fallback. No audio was recorded and no images were replaced.

Evidence and bounded runners are in _scratch/city-skyline-studio/fix-before, fix-after, fix-support, fix-voice and
fix-final. Before/after numerical records use matching names at the scratch root. polish.md is the fix report.
The composition-brief open question remains with the spec owner. No engine changes are needed for these fixes.

The one fix audit was interrupted by the session restart after the Ink control walk. Its saved 99-lead report is
in fix-audit/audit.md; unfinished repeat, rapid-tap and resize/stress stages are not passes. Do not confuse its
placeholder clean/none rows with completed checks. The direct phone host frames cover all six targets separately.
After restart, a targeted overlay correction moved the fact chip right and reserved its box for canvas labels,
restoring the Plan legend. Five fix-overlay frames were viewed; Plan overlap is zero at 1366x768 and 1920x1080.
The full audit was not repeated. The final report answers the saved leads and preserves the remaining limits.

## Cold review changes, 2026-11-03

- Reset `view.find` explicitly while easing and on mode entry. Object.assign previously retained Find's scaling flag
  after returning to Build, so the scene and Build readouts disagreed. A Find-to-Build state now guards that path.
- Refresh camera controls and readouts whenever the target changes. Visible stage Check/Extend controls are the
  narration prerequisites. A matched stage Check moves focus to Next; Next returns focus to the visible stage Check.
- Reserve five hint lines in landscape panels, keeping camera controls still as longer hints appear. Shortened the
  visible Horizon label while retaining its full accessible name. Portrait hint height follows content.
- Portrait Ink now reserves space through Snap and Undo/Redo, rather than only the pen row, so those frequent actions
  remain on screen at 760x900 and in the 375x812 host.
- Guide instructions distinguish receding edges from uprights; tilted Ink instructions name VP 3. Updated the voice
  manifest. Five corrected/new strings use browser fallback; no recordings were made during review.
- Retry unheard eye/guide how-to lines using V.heard rather than consuming their trigger while Sound is off.
- Wrong ink lines use red dashes as well as thickness, so checking works in grayscale. Completed snapped strokes
  retain their on-stage direction label until the next drawing action. Undo/Redo clears stale labels.
- The audit's empty-clear lead prompted a check with real ink. Undo restored its strokes but lost the camera metadata,
  so a later camera change skipped the required warning. Undo/Redo snapshots now include strokes, camera and Keep state.
- Audit frames exposed ineffective inherited fixtures: audit drag bodies need an explicit return, and key steps do
  not support times. Fixed the bodies and expanded the 15 Tilt key steps. The one audit had already loaded those
  fixtures; targeted real drags/keys verify them, without running a second full audit.
- Added projected tank bands, seams, rivets, a rim and cross-bracing to the water tower. Kept the sky painting and all
  exact construction geometry. No image assets were replaced and no people are called for in this architectural view.
- Review evidence is in `_scratch/city-skyline-studio/review-*`. `codex-review.md` is the review's final record;
  the older build/audit sections below remain historical, not claims about the reviewed bundle.
- The single cold-review audit completed within 40 minutes, exit 0, with 113 leads. Motion, console, repeat/rapid input,
  focus and resize checks passed. Secondary fold limits conflict with the explicit preview/phone specification and
  remain documented. Intentional canvas overlays account for geometric overlap leads. Afterward, corrected fixture
  bodies, the eye-height wording and Undo metadata were verified only with targeted frames, not a second full audit.

Build only, 2026-11-01. No commits and no polish round.

## Structure

The existing starter-based implementation was retained and completed against the current spec, including both
Refine changes sections. src.html contains the kit/theme links, responsive layouts, content and voice tables,
saved state, geometry adapters, canvas rendering, Build, Ink, Find, and keyboard/pointer handlers.
It uses kit/perspective.js unchanged. window.__tool exposes state (also S), camera helpers, actions, and voice logs.

## This build

- Generated art/dusk-sky.webp with the built-in image tool. Full prompt and house style are in art/prompts.json.
  Raw PNG is in art/raw. No people. The image is painted at large stage size and clips at the true horizon.
- Added architectural material falloff, edge highlights and inset roof detail, retaining exact projected geometry.
- Added quiet sky drift with Motion on, stopped with Motion off, plus brief kit tones for camera and ink feedback.
- Restored the specified 10 m movement grid. New buildings also use that grid and collision checks.
- Mode entry returns the panel to its top; a new camera target clears the previous outline extensions.
- Canvas labels avoid other labels and VP dots; marker positions remain exact.
- Match events have unique attempt keys so rapid repeated successful checks each speak their result.
- Added required teacher-note opening sections and corrected the false claim that VPs lie on the page at 45 degrees.
- Updated sources, generated-art credit, existing Qwen narration credit, audit states, and readable statement breaks.

## Geometry and storage

The camera uses a 36 mm sensor. The eye stands back 120 + 0.6 (eye - 1.6) m. Auto horizon uses lens shift,
not a changed projection. Tilt uses the engine's pitched camera and third VP. Windows divide real faces projectively.
Find uniformly shrinks both pictures per target, then centers them; the readout states that effective focal scaling.
The six revised targets are 40/30/24/0, 3/45/35/0, 100/20/24/0, 20/55/35/0, 300/40/35/0, 2.5/15/24/15.
The meter changes only after Check camera. Every included setting must reach 95%, rather than just the mean.
Ink is screen-space relative to the image center in page-width units. Its camera and reflection note are saved with
the city in localStorage city-skyline-studio. A later camera change offers Keep it or Clear it. All modes state
device-only storage. Save picture renders a separate stage-size PNG and never draws guides or VP labels.

## Decisions and open questions

The spec has no explicit open-question list. Its final Refine changes replace the earlier target list and live
silhouette meter. The existing 24 mm default lens is retained. Art: none was expanded with one sky painting under
the build brief's express permission to add art where it lifts the scene. All construction remains in code.
Example city retains its supplied central-lot coordinates, including 45 m centers; moving or adding snaps to 10 m.
No new modes, topics, exports, or cross-device features were added.

## Evidence

All evidence is under _scratch/city-skyline-studio/. numbers.json recomputes the spec. verification.json records
projection checks, real jittered Plan drag, five palette additions, snapped ink, hatch/fill, Undo/Redo, freehand
revision/reflection, saved note reload, Keep it, Clear drawing, all six 100% matches, and 20-building performance.
full/ contains the one complete size pass. functional/ includes the exported PNG and student workflow frames.
affected/ holds only targeted follow-up frames. bar-comparison.png compares the tool with Beat Lab.
voice-held-stops.json and voice-matched-repeat.json contain held-click logs. Existing 39 voice recordings were
retained; no audio was recorded or regenerated. The final mechanical audit is under audit/.

## Known limits

The 375 px Find stage is only 200 px high to keep Camera in view. Every target fits, but outlines are small.
Long panel sections scroll; only Camera is shown initially in the 680x425 Build preview, as specified.
Deliberate extreme lens-shift settings can put the entire city off the page; the hint explains the next control.
Plan drag is exact. View drag near eye height uses an alternate horizontal plane to avoid a singular intersection.
Some inherited template expressions and HTML attribute lines remain longer than 160 characters.
Old refine.md and refine/ records predate this build; codex-report.md is the current check record.

## Engine changes wanted

None. Shared kit, engine, family documentation and scripts were not modified.

## Final audit record

The single audit completed within its 40-minute limit, exit 0, with 135 leads. Full record: `_scratch/city-skyline-studio/audit/audit.md`.
Every repeated size/state lead is covered by the following cause groups. The full audit was not rerun after targeted fixes.

- FIXED: compact Lens buttons overlapped by 6 px. Their label column is now 44 px; all four buttons measure 49.75 px
  with 4 px gaps at 680, 800 and 1000 widths. All three affected frames viewed, zero errors.
- FIXED: the reading hint could name Extend outline edges below the fold. A stage-chip Extend copy now exposes the
  same control at 680, 1366 and 375 widths; held clicks worked and target bounds still fit. Seven targeted frames viewed.
- Intentional overlay leads: cv/hint, cv/checkCam2, cv/fchipT and cv/fchipM overlap by design. The stage chip reserves
  framing room. HintDock uses pointer-events:none, so sample-point hit tests see cv beneath readable hint text.
  These explain the corresponding cv and hint keep-region leads; the labels are visibly readable in the frames.
- Open layout limit: all below-fold leads for Overlays, Buildings, Ink secondary controls and Find panel controls at
  760/375 use the specified stacked scrolling layout. Camera and primary pens remain visible; stage Check and Extend
  remain accessible. The strict wave rule that every short choice set be visible simultaneously is not fully met.
- Check-camera short-choice leads: the stage copy was already visible; Extend short-choice leads are addressed by
  the new stage copy. Other secondary choices still require scrolling, as above.
- Welcome-not-heard leads for eye stops, 50/85 mm and Guides follow STANDARDS: that first tap has its own line, so
  the welcome is skipped unmarked. Read and Sound also deliberately stop or skip it. No late welcome was reported.
- No-op leads: Ink canvas requires a drag; Find canvas is a view; Clear drawing on empty ink has nothing to clear.
  Real drag, fill, hatch, erase/revision, clear-on-work and reload were tested separately.
- Other-controls-moved leads: mode changes and Sun opening a dial are expected. Vertical panel shifts on high eye
  stops remain a layout lead for review; focus stayed intact and controls were not rebuilt under the pointer.
- PASS: Motion off, all mid-action resizes, settled Enter-twice paths, five held clicks and two quick taps were clean.
  No console warnings, errors or exceptions were listed. Repeated successful match speech was tested separately.
- Additional source check fixed Hatch spacing's stale aria-valuetext; 24 px now reads 24 pixels. This does not affect geometry.
