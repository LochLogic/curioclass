# City Skyline Studio: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: city-skyline-studio

#### Built

Build only, 2026-11-01. Completed the existing starter-based tool against the full spec and its two revision sections.
Build, Ink, and Find the Camera use the shared perspective engine unchanged. Added generated dusk art, architectural
surface detail, motion-aware sky drift, kit tones, 10 m movement, label avoidance, reliable repeat-match narration,
mode scroll reset, target-extension reset, teacher notes, source credits, audit states, and handoff. No commits.

#### Numbers check

Python: `_scratch/city-skyline-studio/verify_numbers.py` and `numbers.json`. No discrepancy with current spec formulas.
At W=1200, 35 mm: f=1166.6667 px. Turn 45: VP L=-566.6667, VP R=1766.6667.
Turn 30: VP L=-73.5753, VP R=2620.7259. At 85 mm, turn 45: separation=5666.6667 px.
FOV: 73.7398, 54.4322, 39.5978, 23.9132 degrees for 24/35/50/85 mm.
At eye=60 m, the 60 m points on the 34-floor (119 m) and 52-floor (182 m) buildings project exactly to the horizon.
Tilt 15 at 35 mm: VP 3 distance=4354.0593 px, horizon shift=312.6074 px.
Drone/Helicopter stand-back=209.04/359.04 m, angle down=35.66/48.09 degrees.
Each revised target matches exactly; no labeled eye-height stop reaches 95% for any target's eye setting.
Corrected inherited metadata's obsolete 6 m stand-back claim to 0.6 m and notes' false on-page VP claim at 45 degrees.

Computed contrast: cyan on panel 10.27:1, cyan on section 9.73:1, button ink on cyan 9.43:1. The spec's 11.0:1 ink-on-cyan claim is higher than the actual ratio; all meet AA.

#### Feel check

Played Build through moving buildings, Ink through snapped edges, hatch/fill, a red-line revision, reflection and
export, then all six camera targets. Best moment: an edge locks onto VP L outside the page, then a raised eye
reveals the roofs of the same block. The result follows the student's construction rather than awarding points.
Flattest moment 1: the original plain sky made viewpoint exploration feel schematic. Added a large painted dusk
sky, directional facade light, inset roof edges and quiet motion; the street view now reads as a place.
Flattest moment 2: adding a building before Guides gave no composition direction. The first move/add now gives
the composition goal immediately; kit tones and snap feedback give the drawing actions a physical response.
Also cleared carried-over outline extensions so each new camera target is readable.
Compared `_scratch/city-skyline-studio/bar-comparison.png` with Beat Lab; opened Snowy Mail Route as well.
The city has a richer main scene, while the control panel keeps the serious instrument character of the grade band.

#### Done when

1. PASS. Python and browser projection checks put points at 60 m exactly on the horizon for both test buildings.
2. PASS. Engine values match the Python worked checks above; results in `verification.json`.
3. PASS. Projected edge-to-VP error <=1.05e-13 px at pitch 0, 15 and -25; guides use those exact endpoints.
4. PASS. Tilt 15 gives the specified f/tan(15) distance; tilted snap targets omit screen vertical and include VP 3.
5. PASS. Real drag produced `to VP L`; hatch/fill and Undo/Redo worked. Stage-size PNG is in `functional/export.png`.
   Export bytes are identical with guides shown or hidden. Four ink marks and reflection survived reload; clear emptied ink.
   Wrong-camera Keep/Clear prompt appeared. A wrong freehand line turned red, Undo reported it missing, and its replacement
   opened the reflection. Done kept the note and restored Snap.
6. PASS. All six revised targets returned 100% and every per-setting score=1. Start over returned to target 1, Tilt=0.
   Outlines were measured for all six targets at all eight required sizes; every outline fit whole.
7. PASS for Camera and stage. All camera sliders are visible at every required size, including 375x812 in an iframe.
   Phone Tilt bottom=793.53 of 812; 680x425 Tilt bottom=396.27. No horizontal overflow. At 1920x1080 with 20 buildings,
   Windows and Guides, average render time=3.40 ms per frame across 60 redraws, within a 16.7 ms frame budget.
8. PASS. Five held eye-stop clicks at 2 s gaps spoke turnHow once and offPage once. After the event-key fix, three
   successful Check camera clicks at 2 s gaps each spoke Matched and its settings, with an empty final voice queue.

#### Wave lessons

- Hint and voice: PASS in focused tests. Read uses the current hint via Curio.voice. How lines once, match events repeat.
- Focus and layout: PASS in focused tests. Keyboard-only Tab/Enter/arrows drew a snapped line with focus on cv.
  Mode changes reset panel scroll. Controls are created once; hints reserve height and nothing takes focus on load.
- Sizes: PASS for primary camera/pen controls. Full size pass, phone iframe, targeted extreme frames and audit frames viewed.
- No giveaways: PASS. Hidden camera settings are not exposed before a successful check. Meter is Check-only, then stale after changes.
- Honest numbers: PASS. Readouts state sensor/focal relation, target-fit scale, stand-back, tilt shift and per-setting checks.
- Standards: PASS. VA:Cr2 composition and construction; VA:Cr3 freehand checking, replacement and saved reflection are solo actions.
- Motion off: PASS in focused frames. Sky interval clears and camera changes jump. No CSS animation loops.
- Short choice sets: FAIL under the strict all-choices-visible rule in portrait layouts. Camera/lenses and primary pens
  remain visible, but secondary color, export, overlay and building sections can require the specified panel scrolling.
- Resize mid-animation: PASS. Every resize reprojects the model; audit found no exceptions or disabled controls left stuck.
- Late welcome: PASS. No welcomeAfter; each mode uses Curio.voice and stale scope checks.
- Unknown as unknown: PASS. Hidden camera is an unlabeled outline; settings are revealed only on a match.
- One look, one meaning: PASS. Cyan dashed guides, red VPs, amber dashed target and solid gold selection remain distinct.
- Truthful badge and reversible hint: PASS. Match becomes Last check after a change; targets clear previous extensions.
- No answer by copying: PASS. Students read edges, roofs and upright lean; no answer-choice wording is supplied.

#### Audit leads

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

#### Frames looked at

Both bar-tool frames; `early/` all four frames; `functional/` all workflow frames and the actual export; `full/` all 30
frames in contacts plus phone/extreme frames individually; `voice-keys/` all three; `affected/` targeted frames individually;
`final-frames/` all seven post-audit targeted frames individually.
Full pass: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, and 375x812 iframe, all three modes.
Also checked tilt +/-25, turn 0/90, 85 mm, horizon -600%, empty city, 80 floors/80 m dimensions, calm, grayscale,
keyboard drawing and 2 s held-click voice. Mechanical audit frames viewed through numbered contact sheets.

#### Art made

One generated image, `art/dusk-sky.webp`: 1600x900, 75.39 KiB, no people. Built-in image tool, full prompt in prompts.json.
Converted with `art.py city-skyline-studio --rekey dusk-sky`; inspected the finished WebP and in-scene frames. No redraw needed.
Final bundle: 1,099,908 bytes (1074.13 KiB), under 2 MB. Existing 39 narration recordings retained; no audio was recorded or regenerated.

#### Art still to paint

None.

#### Engine changes wanted

None. No shared engine, kit, docs, scripts, branches or other tool folders were modified.

#### Left open

- At 375 wide, Find's stage is 200 px high so Camera remains visible. All outlines fit but are small.
- Secondary controls scroll in compact/phone layouts, as specified. Extreme manual lens shift can move the city off-page.
- View dragging near eye height uses an alternate horizontal plane; Plan dragging is exact.
- Some inherited template expressions and HTML attributes exceed about 160 characters; statement lines were expanded.
- The first broad voice shot had an invalid numeric CSS selector in the test file, retried with quoted values and passed.
  Early phone-host shots had a host-page favicon 404; the final hosted targeted batch returned zero errors.
- The full audit is not mechanically clean: stacked secondary controls and high-eye panel shifts remain as documented above.
  Intentional canvas overlays still trigger geometric overlap/keep leads. Audit snapshot precedes the compact Lens,
  stage Extend and hatch accessible-value fixes; only the seven affected frames were rechecked afterward.

All Chrome processes and host servers started for checks were closed. Temporary tool host.html was removed.
No polish round was started. No git commit was made.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: city-skyline-studio


#### Played

- Cold Grade 9-12 student pass in Build, Ink and Find before reading the builder files; then projection, drawing,
  keyboard and target checks. The low-eye skyline and roof reveal are strong; keep their scale and dusk atmosphere.
- Inspected all eight STANDARDS sizes in all three modes, grayscale, Motion off, empty city and extreme camera/building settings.

#### Findings fixed

- **Blocker, family:perspective, Build after Find:** `view.find` survived Object.assign and kept Find's focal scaling.
  Explicitly reset it on mode entry and easing. Verified Build's rendered focal length equals its readout again.
- **Should fix, family:perspective, target navigation:** focal scaling and horizon readouts stayed on the previous target.
  Refresh controls/readouts whenever the target changes.
- **Should fix, general, Find keyboard:** a matched stage Check hid the focused button; Next focused a panel copy below the fold.
  Move focus to visible Next, then the visible stage Check, with preventScroll. Two Enter presses reach target 2.
- **Should fix, general, portrait Ink:** Undo/Redo were below the fold. Reserve stage space through that button row;
  Undo bottom is 895/900 px at 760 wide and 807/812 px in the 375 host.
- **Should fix, general, layout:** long hints shifted controls. Reserve five landscape hint lines and keep Horizon's value row stable.
- **Should fix, family:perspective, teaching:** "every edge" incorrectly included uprights; tilted Ink promised screen verticals.
  Distinguish receding edges/uprights, name VP 3 when tilted, and qualify the horizon-crossing fact for short buildings.
- **Should fix, general, voice:** historical eye/guide counters could consume unheard instructions; phone Find depended on
  offscreen panel copies. Retry unheard how-to lines with V.heard and use visible Check/Extend as prerequisites.
- **Should fix, general, grayscale checking:** red alone identified bad ink. Added a dash pattern, retaining red and thickness.
- **Should fix, family:perspective, Clear/Undo:** restoring cleared ink lost its saved camera and skipped the old-camera warning.
  Undo/Redo now restore the strokes, camera and Keep state together; checked Clear, Undo, Redo and a subsequent camera change.
- **Polish, general, flattest action:** the snapped-line tag vanished on release. Keep its direction beside the completed line;
  clear it on the next drawing action or Undo/Redo.
- **Polish, family:perspective, weakest art:** the water tower was a bare tank on four posts. Added projected bands, seams,
  rivets, a top rim and steel cross-bracing; retained its construction frame, exact projection and the strong sky painting.

#### Findings left

- **Should fix, general/spec conflict:** secondary Overlays, Buildings and export controls still require scrolling in
  portrait/short layouts. The spec explicitly requires Camera-only preview and a scrolling phone panel; a full simultaneous
  choice layout needs a spec decision. Primary Camera, pens, values and Undo/Redo fit. This is not an all-controls-visible pass.
- **Polish, general:** five corrected/new voice strings fall back to browser speech. Recording is forbidden in this review.

#### Flattest moment left

- Later camera targets repeat setting adjustments after the construction idea is understood. Preserved the six specified targets.

#### Graphics

- Checked the sole bitmap, dusk-sky.webp, at its 1600x900 output and in-scene. Kept it; no missing art tokens or people assets.
- Improved the weakest code-drawn structure, the water tower, and inspected street/roof views. No asset was removed.
- Compared the retained scene finish with the existing Beat Lab comparison frame. Bundle: 1,007,012 bytes, about 983 KiB.

#### Audit

- The single final audit completed, exit 0, within 40 minutes: 113 leads, all read and grouped below. No full rerun.
- Fixed ineffective drag/key fixtures exposed by the saved frames, then rechecked actual 15-degree Tilt and both ink drags.
- The empty-clear lead led to the camera-metadata fix above. Rechecked Clear/Undo/Redo and the required camera warning.
- Canvas/hint/target-chip overlaps and covered hint sample points are intentional overlays; the frames are readable.
  Check/Extend have visible stage copies, so leads naming their scrolled panel copies do not block either action.
- Fold/short-choice leads remain the explicit spec conflict above. High-eye readouts shift secondary building controls;
  mode switches and opening Sun also move controls as expected. Camera controls and focus remain intact.
- Skipped welcomes after a first tap's own line follow STANDARDS; Read/Sound intentionally skip or stop speech.
  Canvas taps and clearing empty ink are expected no-ops. Real-work paths were checked separately.
- Motion off, repeat/rapid input, settled Enter paths, resizes, and console checks passed. All 39 audit frames inspected.
- The audit snapshot predates the corrected fixture bodies, shorter eye-height hint and Undo metadata fix.
  Only their affected frames were re-shot afterward; five revised narration lines use browser fallback.
- Python recomputed the worked VPs/FOV, 60 m crossings and tilt. Browser edge error <=2.22e-12 px; all six targets scored 100%.
- Real snapped line, hatch/fill, Undo/Redo, saved ink reload, keyboard revision/reflection, note and guide-free PNG passed.
- At 1920x1080, 20-building redraws averaged 4.365 ms, within a 16.7 ms frame budget; this is not a classroom hardware test.
- Contrast: cyan/panel 10.27:1, cyan/section 9.73:1, ink/cyan 9.43:1, label/chip 16.72:1.

| Voice line | Kind | Expected | Spoken |
|---|---|---:|---:|
| turnHow across five held stop changes | how | 1 | 1 |
| Matched across five held checks, 2 s apart | event | 5 | 5 |
| Hidden settings for those checks | event | 5 | 5 |
| Next target after repeated checks settle | how | 1 | 1 |
| Read with Sound off | read | 1 | 1 |

- Voice manifest matches allLines exactly; repeated-match queue drained. All narration was tested muted via held clicks.

#### Left open

- Spec conflict and five browser-fallback lines above. No kit changes, other-tool writes, recordings or git commits.
- Evidence: `_scratch/city-skyline-studio/review-*`, `final-targeted/`, `review-audit/`.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1 merged 2026-11-04, polish not started)
Counts: blockers 1 (general 0, family 1), should fix 10 (general 9, family 1), polish accepted 8

### Refine: city-skyline-studio (round 2026-11-04, after the Codex rework)

The 2026-10-28 Refine is kept in refine-2026-10-28.md and refine-2026-10-28/ (it ran before Codex reworked the tool).
Lenses: refine/teaching.md, refine/play.md, refine/craft.md. Shared audit: 114 leads. Measure-first run: the lenses
did not read codex-report.md or codex-review.md.

#### Blocker

1. **Check my drawing passes flat lines, and Snap teaches them.** `misses()` and `lineEnd()` use `Persp.targets()`
   with its default `horizontal` target, so at Turn 30 three flat lines across the towers get "All 3 lines hit their
   vanishing points" and Snap labels a flat roof edge "horizontal". This is the classic two-point mistake passing the
   tool's one revise step (VA:Cr3). Drop the level target here (snap and check): at Turn 0 or 90 the far VP already
   comes back as a level direction. Keep the upright only at Tilt 0. (Teaching 1) family:perspective

#### Should fix

2. **Check my drawing passes on any three upright lines anywhere, then asks "What did you change?"** when no line was
   ever red. Count only receding lines toward the three (or require at least one), and when `checkHadRed` is false ask
   "How did you aim each line at its vanishing point?" instead. (Play 2, Teaching 5) family:perspective
3. **Find the Camera can be solved from the per-setting percents** without reading the outline (target 1 in five
   checks). After a miss show only which settings are off (no percent) and the reading hint for the first one; the
   overall meter may move in coarse steps. (Teaching 2, Play 3) general
4. **The street-level targets (3 m and 2.5 m) ask for precision the picture can't show** at the 12% tolerance, and
   their hint names visible roofs that are not visible. Tie the eye tolerance to what shows (outline horizon within a
   few pixels), or raise them to heights that read clearly (for example 6 m and 4 m), and fix the hint. (Teaching 3)
   general
5. **"Tiers above your eye show their undersides" is false**: the stepped tiers' undersides are hidden; only the water
   tank shows one. Show the fact only when an uncovered bottom is drawn, name the tank, and fix the notes.md question.
   (Teaching 4) general
6. **At 1366x768 the Buildings section is below the fold** while addFirst, buildNext and composeGoal send the student
   there. Put Readouts after Buildings (or fold Readouts to a summary). (Play 1) general
7. **The Build hint is a fixed ladder**: done out of order, the voice moves on but the hint and Read stay on "Drag the
   eye height slider". Pick the rung by what is still undone. (Craft 1) general
8. **Check my drawing voice**: the first line drawn during a check speaks inkMore ("...press Check my drawing") while
   the button reads Stop checking, and checkFix is never spoken. No inkMore while checking; checkFix once, the first
   time a line turns red. (Craft 2) general
9. **A second missed Check camera is silent**. Add a short event line per miss ("Not yet. Two settings are off."),
   reading how-to kept to once. (Craft 3) general
10. **findLens names no action or control**: end it with "Pick a lens, then press Check camera." (Craft 4) general
11. **After Clear city the welcome plays over an empty stage** and addFirst is never spoken. The welcome needs a
    city; addFirst is spoken once when the city empties. (Craft 5) general

#### Polish accepted

12. The facts tip sits at the bottom of the panel, out of view at 1366x768: show the current fact under the hint or
    as a stage chip. (Play polish 1) general
13. 760x900 and 375: the stacked hint keeps a four-line reserve, pushing Overlays below the fold; size it to its text
    when stacked. (Play polish 2) general
14. "Your city is off the page" overstates it with a building filling the stage, and offCity's "pick a wider lens"
    misleads when the Horizon is moved: say "Most of your city is off the page", and lead with "Press Auto" (or a
    wider lens while Auto is on). (Play polish 3, Craft 7) family:perspective
15. Find: after a match the big panel button becomes Next target (Start over on target 6). (Play polish 4) general
16. offPage is Build-only; in Find it fires with no student action and delays findCheck. (Play polish 5, Craft 6)
    family:perspective
17. Stage labels scale up with the stage above about 1400 px (13 to 15 px at 1920). (Play polish 6) general
18. Find at 375: VP chips sit on the amber outline; keep them at the stage edge or shorten them. (Craft 8)
    family:perspective
19. "Looking 48 degrees down" with parallel uprights: a readout note that the picture stays upright like a drafting
    view and Tilt shows the real lean, plus the same line in notes.md. (Teaching 7) family:perspective

#### To the spec's open questions (not for the builder)

- Composition is one recipe line (`composeGoal`) in a module named "...and Composition": two or three short briefs
  to pick from, saved with the drawing? (Teaching 6)

#### Nits (optional)

- Check tests direction, not place: a line in empty sky aimed at VP R passes (Teaching 8, family:perspective)
- Water tower sized in "Floors"; its 8 m width and depth sit below the sliders' 10 m minimum (Play nit 1)
- Empty city readout "Horizon crosses 0 of 0 buildings" (Play nit 2)
- The selection outline shows through nearer buildings (Play nit 3)
- Undo is off after a reload though the strokes are back (Play nit 4)
- Fill on empty sky does nothing, silently (Play nit 5)
- buildNext is cut after 0.2 s when a building is added as it starts (Play nit 6)
- The stage chip reads "Extend" while lines say "Extend outline edges" (Craft 9)
- Clear drawing stays enabled on an empty drawing (Craft 10)
- Scrambled indentation through most functions in src.html (Craft 11)

#### Settled calls

- Rule 5 does not apply. Contract clean.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: city-skyline-studio (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json and the CURIO_DRAFT=1 bundle. Driven with
`scripts/drive.py` (held clicks 0.12 s, Sound on, Motion on, real keys) in three runs of 37 fresh pages at 1366x768.
Frames and logs: the craft scratch folder (`refine/city-skyline-studio/craft/out-rep`, `out-run2`, `out-run3`, with
rep.log, run2.log, run3.log). Shared audit: `audit-r1/audit.md` and its frames.

Counts: blockers 0, should fix 5, polish 3, nit 3.

#### Contract and access (clean)

- One file, 1,009,411 bytes (under the 2 MB goal). No network requests (Resource Timing empty after all three modes;
  no http(s) reference in the page). No console errors, warnings or exceptions in any of the 37 pages.
- Kit used: `Curio.voice`, `Curio.init`, theme-912, `kit:perspective`; nothing re-implemented that I could see.
- Keyboard: Tab reaches the mode buttons, header, the stage (visible cyan focus ring, out-run3/focus-tab2.png) and the
  panel; arrows step sliders, Page Up/Down jump eye stops, arrows move a building, Enter draws in Ink. Targets: the
  audit's 44 px check is clean at every size and my frames agree. Color is never the only signal (red misses are also
  dashed and counted; VPs are labeled; pressed buttons fill). Motion off is clean (audit). Sound off, Read still
  speaks (run2 read-soundoff).
- `voice/lines.json` matches `__tool.allLines()` word for word: 40 and 40, none missing either way.
- Art: one asset, `art:dusk-sky`, has its prompts.json entry, no people (none needed). Words: no em or en dashes on
  screen in any mode, in src.html, notes.md or lines.json; "Curio Class" only, never "Curio" alone; classroom-safe;
  privacy stated in every mode ("saved in this browser on this device only", the reflection note included).

#### Findings

1. **should fix, general.** src.html `hintNow()` (Build branch, about line 1500) against the spoken lines. The Build
   hint is a fixed ladder (eye, then turn, then guides), so when a student does the steps in another order the voice
   moves on but the hint and Read stay on the first rung. Seen: run1 rep-turn (first action Turn: spoken "Turn on
   Guides under Overlays...", hint and Read still "Drag the eye height slider..."); run2 read-during (Guides first:
   guidesHow then buildNext spoken, Read then says "Drag the eye height slider..."); run3 tilt-how (tiltHow spoken, hint
   unchanged). STANDARDS: the hint changes when the state changes, and the spoken line matches it. Better: pick the
   hint rung by what is still undone and let it follow the line a step just queued.
2. **should fix, general.** Ink with Check my drawing on (`commit()` line 2046 and the check branch of `hintNow`). The
   first line drawn during a check speaks inkMore, "Keep drawing, or try Hatch and Fill. Then press Check my
   drawing...", while the button already reads "Stop checking" and the hint shows checkHow or checkFix. And checkFix
   ("Fix the dashed red lines...") is never queued anywhere, so a student with red lines hears nothing about fixing
   them. Seen: run1 rep-check (five missing lines: inkMore 1, checkFix 0), run3 reflect. Better: no inkMore while
   `S.check`; checkFix as a how-to the first time a line turns red.
3. **should fix, general.** Find, `checkCamera()` miss branch. A missed Check camera is a result, but only its reading
   hint is voiced, as a how-to: the first miss speaks findEye and every later miss on the same setting is silent (no
   line, no tone), though the panel shows a fresh "Not yet: N settings are off" each time. Seen: run1 rep-findmiss (5
   presses: findEye spoken 1, then `silent heard` 4). A student pressing Check camera again hears nothing happen.
   Better: a short event line per miss ("Not yet. Two settings are off.") with the reading how-to kept to once.
4. **should fix, general.** `L.findLens` "Read the lens: the farther apart the outline's vanishing points, the longer
   the lens. Close together means a wide lens." is the only Find reading line that names no action or control (the
   others say Press Extend outline edges, turn until, Tilt until). Cory's rule: every waiting moment names the next
   action and the control. Better: end with "Pick a lens, then press Check camera."
5. **should fix, general.** Build after Clear city (run3 clearcity). With Clear city as the first tap, the welcome then
   played "Drag the eye height slider and watch the horizon stay with your eyes." over an empty stage while the hint
   showed addFirst ("Your city is empty. Tap Tower..."); addFirst itself is never spoken. The welcome's `valid` only
   checks `!S.eyeMoved`. Better: the welcome needs a city, and addFirst is spoken once when the city empties.
6. **polish, general.** offPage on entering Find (run2 ft-find): "One vanishing point just went off the page" plays
   five seconds after the Find welcome with no student action; the target's camera simply starts that way. Better: in
   Find, arm offPage only after the first camera change.
7. **polish, general.** offCity line and hint, "Move Horizon on page, or pick a wider lens." (out-run3/offcity.png,
   Horizon at 600% above). A wider lens does not bring that horizon back, and the one-tap fix, Auto, is not named.
   Better: "Your city is off the page. Press Auto, or move Horizon on page."
8. **polish, family:perspective.** Find at 375 wide (audit state-mode-find-the-camera-375x812.png): the "VP (off the
   page)", "VP R: infinitely far" and horizon chips sit on top of the small amber outline, the thing the student has to
   read. Better: on narrow stages keep VP chips at the stage edge or shorten them so the outline stays clear.
9. **nit, general.** The stage chip button reads "Extend" while the hint and lines say "Press Extend outline edges"
   (audit state-find-missed-check-1366x768.png); only its aria-label has the full name. "Extend edges" would match.
10. **nit, general.** Clear drawing stays enabled on an empty drawing and does nothing (audit "nothing changed"),
    while Undo and Redo show disabled. Could match them.
11. **nit, general.** src.html has scrambled indentation through most functions (statements after `;` pushed to new
    deeply indented lines, for example `checkCamera()` and `syncCam()`), which makes the source hard to review.

#### Standard voice check

Repeats (run1, five actions, gaps longer than the lines):

| line | kind | expected | spoken |
|---|---|---|---|
| turnHow (5 eye stops) | how | 1 | 1 |
| offPage (same run, at 150 m) | event, once per session by spec | 1 | 1 |
| guidesNext (5 Turn key steps) | how | 1 | 1 |
| guidesHow (Guides on and off x5) | how | 1 | 1 (buildNext follows once, as a sequence) |
| welcomeBuild (5 lens taps, no own line) | welcome | 1 | 1 |
| inkMore (5 lines, Snap on) | how | 1 | 1 |
| checkFix (5 missing lines, check on) | how | 1 | **0** (inkMore spoken instead; finding 2) |
| findEye (5 missed Check camera) | how | 1 | 1 |
| miss result (same 5) | event | 5 | **0** (finding 3) |
| matched + settings (5 matched checks) | event | 5 + 5 | 5 + 5 |
| findNext (same) | how | 1 | 1 (then `silent heard` 4) |

Stale lines (run2 stale-build, stale-find, stale-ink: taps 0.35 s apart, then a mode switch): no line played after its
moment. Superseded lines were dropped (`newer`, `hush`, `stale`); welcomeBuild was dropped `stale` once the eye had
moved; nothing named a hidden control.

First-tap timing (fresh page each): stage tap, welcome at 150 ms; a stop, only turnHow (the welcome is later dropped as
stale because the eye moved, which fits the state); 85 mm, only offPage, then Sound off and on brought welcomeBuild
once; Guides, only guidesHow, then Ink brought welcomeInk; Ink and Find buttons, their welcome within 150 ms; Read
first, the hint only; Sound first, nothing, then Sound on brought the welcome once; a key (eye slider ArrowRight),
turnHow only. Nothing spoke before a tap. Clear city first: finding 5.

Read: Read during guidesHow cut it and spoke the hint (the queued buildNext dropped `hush`, unmarked); Read with Sound
off spoke; a mode change 0.7 s after Read started welcomeInk 140 ms later; an event during Read (offPage) waited for Read
to end. What Read says is wrong when the hint is stale (finding 1).

Order (run2 order-build, 1.5 s apart): turnHow, guidesHow, buildNext in action order; no older line after a newer one.

#### Audit pilot

Confirmed on my frames or runs:
- Held-click table: a first tap on a stop, 50/85 mm or Guides skips the welcome. Confirmed, but right for those taps
  (each has its own line); the welcome comes back on Sound off and on or the next mode entry while it still fits. Not a
  finding by itself.
- "#clearInk nothing changed" on an empty drawing: confirmed, nit 10.
- 760x900 and 375: Overlays, Buildings, Show render, Save, Check my drawing below the fold. Confirmed, but the camera
  sliders, pens, values and Undo/Redo (the every-few-seconds controls) are on screen, as STANDARDS asks. Not reported
  by Craft.

Wrong leads:
- "#cv / #hint overlap" and "#hint keep region covered" at 680x425 and 800x500: in compact layout the hint band sits
  over the top of the stage on purpose and is fully readable (size-680x425.png).
- "#cv / #fchipT, #fchipM, #checkCam2, #extendQuick overlap": the Find chip is a deliberate stage overlay on the sky,
  clear of the outline at 1366x768 and 680x425.
- "#cv nothing changed" in Ink and Find: a plain tap draws nothing in Line mode, and Find's stage is not a control.
- "choices cut short by a scroll panel" naming Check camera at 680x425 and 800x500: Check camera is also on the stage
  chip, on screen.

Missed by the audit:
- Hint and Read stuck on the first Build rung when steps are done out of order (finding 1).
- Check-mode voice: inkMore in the wrong state, checkFix never spoken (finding 2).
- A repeated missed Check camera is silent (finding 3); the five-click rows did not include Check camera.
- The welcome playing over an emptied city (finding 5), and the wording items (4, 6, 7, 9).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: city-skyline-studio (round 1)

Fresh and cold. Played twice: as a grade 9-12 student alone at home on a 1366x768 laptop, and as a teacher projecting
at 1920x1080. Bundle: `city-skyline-studio.html` (CURIO_DRAFT=1, as handed over). Frames are in
`C:\Users\Cory\AppData\Local\Temp\claude\912539a76ace91d0\c55c8920-4b50-4aa7-8632-31d061e89e76\scratchpad\refine\city-skyline-studio\play\`
(f1 Build extremes, f2 Ink, f3 Check my drawing, f4 Find the Camera, f5 voice walks as JSON, f6 empty states), plus the
shared audit frames in `audit-r1\`. Voice was walked with a real first tap and the kit's `V.log` (f5/w1-walk.json,
f5/w2-find.json).

**Counts: blockers 0, should fix 3, polish 6, nit 6.**

#### Should fix

1. **Build, 1366x768: the Buildings section the hints name is below the fold, with no cue.** (general)
   The panel order is Camera, Overlays, Readouts, Buildings (src.html:253-257). At 1366x768 the panel ends at the
   Readouts heading; Tower, Block, Slab, Stepped, Water tower, Example city and Clear city all need a panel scroll.
   Three lines send the student there: `addFirst` ("Your city is empty. Tap Tower, Block... under Buildings"),
   `buildNext` ("...or add one from Buildings") and `composeGoal`. Seen: f6/e1-empty.png (empty city, hint names
   Buildings, nothing of Buildings on screen), f1/01..16 at 1366, audit "off screen at load" rows 21-27. A solo student
   who clears the city is told to tap something they cannot see. Better: put Readouts after Buildings (or fold Readouts
   to a one-line summary with a toggle), so the palette sits under Overlays at 1366x768; the fact tip (src.html:275)
   would then also come closer to view (see polish 1).

2. **Ink, Check my drawing passes on any three upright lines anywhere, then asks "What did you change?" when nothing
   was ever red.** (family:perspective)
   I turned the check on and drew three short vertical strokes in the empty street (keyboard cursor, Enter, ArrowDown
   x10, Enter). Result: "All 3 lines hit their vanishing points." and the reflection opened: "What did you change to make
   your lines hit their vanishing points?" Seen: f3/c4-three-hits-no-miss.png. The check only measures direction
   (src.html:2131: ready when no misses and either a red line was seen or three lines were drawn), so the cheap way
   through the revise step is three verticals or three level lines, none on a building edge. And when no line was ever
   red, the question assumes a fix that never happened: words do not match the state. Better: count only lines that
   are not upright or level (receding edges) toward the three, or require at least one receding line; and when nothing
   was red, ask a different question ("Which vanishing point did your slanted lines aim at?") or open nothing.

3. **Find the Camera: the per-setting scores let a student solve any target without reading the outline.** (general)
   After each Check camera the panel lists Eye height, Turn, Lens (and Tilt) as percents with check marks. Each score
   is a plain distance: turn 1 - |difference| / 40, eye 1 - |ln ratio| / ln 10. Target 1, eye only: 10 m gave 39%, 20 m
   69%, 80 m 69%; turn 20 and 40 both 75%, so the answer is 30. Two or three checks per setting pin each one, and the
   check marks say which are already right (f4/f2-miss "Eye height 39%, Turn ✓ 100%, Lens ✓ 100%", f3b, f3c). The
   reading hints are good, but the numbers make them optional. Better: after a missed check, show only which settings
   are off (no percent) and the reading hint for the first one; keep the meter for the overall match, or show coarse
   words ("close", "far") without direction-free exact distances.

#### Polish

1. **The facts tip sits at the very bottom of the panel, out of view at 1366x768.** (general) `#tip` (src.html:275)
   changes with the state ("Where the horizon crosses a building, it marks your real eye height.", "Above the horizon
   you see bottoms", "Nearly one-point perspective") but is only seen after scrolling the whole panel (f1/15, f6/e2).
   These are the spec's "Facts shown on screen". Better: show the current fact under the hint, or as a small chip on
   the stage near the horizon label.

2. **760x900 and 375: a blank band under the hint pushes Overlays below the fold.** (general) The hint keeps a reserved
   height (src.html:106-107, `min-height: calc(4 * 1.45em)` when stacked) but holds one line, leaving about 90 px of
   empty panel (audit size-760x900.png, f4/f14-760.png). `guidesNext` says "Turn on Guides under Overlays", and at
   760x900 Overlays starts at 928 px. Better: let the stacked hint size to its text (keep the reserve only for the
   side-by-side layout), which brings Overlays above the fold at 760x900.

3. **Drone or Helicopter with an 85 mm lens: "Your city is off the page" while a building fills the stage.**
   (family:perspective) With Auto on, Drone + 85 mm shows one or two buildings filling the left of the stage, yet the
   hint and the stage chip say "Your city is off the page" and "your city is above the page" (f1/10-drone-85.png,
   f1/13-add-all.png, where a slab roof fills the stage). The test is "fewer than a third of the buildings show"
   (src.html:1199-1209), so the words overstate it, and the advice "Move Horizon on page" switches Auto off.
   Better: "Most of your city is off the page" and, while Auto is on, lead with "pick a wider lens".

4. **Find, after a match the big panel button is still Check camera.** (general) The stage chip swaps to Next target,
   but in the panel the wide primary button stays "Check camera" and Next target is the small button beside the target
   number (f4/f4-match.png, f7-last-match.png). The hint says "Press Next target". Better: after a match, the big
   button becomes Next target (Start over on target 6), like the chip.

5. **Find: the Build-only `offPage` line plays in Find before `findCheck`.** (family:perspective) In the Find walk
   (f5/w2-find.json) the first eye change in Find spoke "One vanishing point just went off the page. The lines still
   aim at it." at 10.4 s and pushed "When you think your camera matches, press Check camera..." to 14.8 s. Find starts
   at Turn 0, so a VP is "infinitely far" from the first frame; the line adds nothing to the Find task and delays the
   how-to the student needs. Better: keep `offPage` to Build.

6. **Projected at 1920x1080, the stage labels are small.** (general) The horizon label, VP L / VP R chips and "the
   outline's horizon" are about 11-12 px bold (audit size-1920x1080.png, f4/f15-1920.png). Fine on a laptop, hard to
   read from the back of a room. Better: scale stage label type with the stage width above about 1400 px (13-15 px at
   1920).

#### Nit

1. **Water tower:** it is sized in "Floors" ("1. Water tower, 6 floors"), and its Width and Depth read "8 m" while the
   sliders' minimum is 10, so the thumbs sit at 10 (f6/e2-water.png; src.html:1781-1786). Say "Height" for the water
   tower, or let the sliders reach 8.
2. **Empty city readout:** "Horizon crosses 0 of 0 buildings" (f6/e1-empty). Hide the row or say "No buildings yet".
3. **Selection outline shows through nearer buildings.** The amber outline of the selected building is drawn on top
   of everything, so at the sidewalk it reads as a box floating on the front slab (f1/16-example-drag.png,
   f2/i11). A thinner or dashed line where it is hidden would read as "behind".
4. **Undo is off after a reload** although the strokes are back (f2/i5-fill.png: 3 strokes, Undo greyed). Either keep
   the undo list with the drawing or let Undo remove saved strokes.
5. **Fill on empty sky does nothing, silently** (f2/i5: tap at 800,300 in the sky, no fill, no message). A short
   "Tap a face of a building" status would help.
6. **`buildNext` is cut after 0.2 s** when a building is added just as it starts (f5/w1-walk.json: buildNext spoken
   40.8 s, composeGoal 41.0 s). Drop `buildNext` from the queue as soon as a building is added or moved, before it can
   start.

#### What worked (checked, no finding)

- First screen at every size says what to do and names the control; the welcome is spoken once, then each next step
  (turnHow, guidesNext, guidesHow, buildNext, composeGoal, tiltHow) is spoken once and only updates the hint after
  (f5/w1-walk.json: five more eye moves, no repeat). Read speaks the current hint.
- Extremes hold up: Turn 0 and 90 ("VP R: infinitely far", the one-point fact), Tilt +25 and -25 (VP 3 above or
  below, labels clear), Horizon 600% above ("your city is above the page"), 80 floors at 80 m, 20 buildings, empty city
  (f1, f6).
- Ink: snapping labels the line ("horizontal", "vertical"), Hatch aims at the face's VP, the drawing survives a reload,
  Save picture gives a PNG without guides (f2/i10), and changing the camera in Build asks Keep it or Clear it (f2/i11).
  Clear city and Clear drawing take two presses ("Really clear?").
- Find: every target's outline sits whole under the chip at 1366, 1920, 1000, 760 and 680 (f4/f9 to f15); Extend
  outline edges draws the outline's own horizon and VPs, which makes the eye height easy to read (f4/f3-extend.png);
  matching lines the render up with the outline, which is a satisfying moment; Start over resets Tilt and says so.
- Motion off: the audit's calm run is clean.

#### Audit pilot

**Confirmed on my own frames:**
- Build controls below the fold at 1366x768 (rows 21-27, "off screen at load"): confirmed, and it matters because the
  empty-city and buildNext hints name Buildings (should fix 1).
- 760x900 and 375: Overlays and Buildings below the fold: confirmed; the reserved hint height is the cause of most of it
  (polish 2).
- Find, "others moved 4-5 of 25" after Check camera: confirmed, the scores list opens and pushes Overlays down; all
  below the fold, harmless.

**Leads that were wrong, or right but not a problem:**
- Every `#cv` overlap with `#hint` (680x425, 800x500), `#fchipT`, `#fchipM`, `#checkCam2`, `#extendQuick`: by design.
  The hint docks over the stage top in the compact layout and the Find chip sits on the stage; no outline or label is
  covered (Find shrinks the outline under the chip).
- "choices cut short by a scroll panel" in Find (680x425, 800x500, 1366x768): the hint names Check camera and Extend
  outline edges, and both are on the stage chip, visible. The only gap is the chip's label "Extend" against the hint's
  "Extend outline edges" (the chip's aria-label and title say the full name); fine.
- "Welcome not heard" after a first tap on an eye stop, 50 mm, 85 mm or Guides: the tap queued its own line, so the
  welcome is skipped by rule, and the hint still shows the welcome until the eye moves, so Read gives it. Not a problem.
- "nothing changed" for `#cv` in Ink and Find and `#clearInk`: a tap without a drag draws nothing, Find's canvas has no
  tap action, and Clear drawing on an empty drawing has nothing to clear. Expected.

**What it missed:**
- The cheap pass in Check my drawing and its reflection question that assumes a fix (should fix 2).
- The per-setting scores that let Find be solved by trial (should fix 3).
- The "city off the page" wording at Drone + 85 mm (polish 3), the fact tip out of view (polish 1), the panel's primary
  button after a match (polish 4), `offPage` in Find (polish 5), projector label size (polish 6).
- A real first tap matters for its voice rows: my first walk without one logged every line as silent "early".

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: city-skyline-studio (round 1, 2026-11-04)

Fresh cold read of spec.md (with its Refine changes), src.html, notes.md, tool.draft.json, voice/lines.json and
kit/perspective.js, against REFINE.md, STANDARDS.md, BASELINE.md and the BUILD.md wave lessons. Shared audit:
`audit-r1/audit.md` and its frames. My own frames and scripts are in the scratch folder `teaching/` (f1/, f2/,
shots1.json, shots2.json, dw.js).

Counts: blockers 1, should fix 3, polish 3, nit 1.

#### Standards (module arts-9-12-two-point-perspective-and-composition: VA:Cr2, VA:Cr3)

- **VA:Cr2 (organize and develop artistic ideas and work): taught.** The student sets up a construction (eye height,
  turn, lens, tilt), places and sizes buildings on a lot grid and reads the result through Guides and Plan. That is
  real skill building through experiment. The "composition" half of the module title is thin (polish 2).
- **VA:Cr3 (refine and complete): taught in design, undermined in practice.** Ink, Check my drawing, the reflection
  note and Save picture make a real revise-and-finish loop, but the check accepts the most common two-point error
  (blocker 1), so a student can pass the revise step without revising anything.

#### Done when

| # | Check | Result | How |
|---|---|---|---|
| 1 | Horizon at eye level; crosses buildings at the eye's real height (60 m) | pass | dw.js: points at y = 60 m, z = 150 and 400 project exactly to the horizon row; "Horizon crosses N of 9" counts buildings taller than the eye |
| 2 | Worked check at W = 1200 | pass | 35 mm: f 1166.7; t 30: VP L -73.6, VP R 2620.7; t 45: -566.7, 1766.7; 85 mm at 45: 5666.7 px apart. FOV 73.7, 54.4, 39.6, 23.9 |
| 3 | Guides meet at the VPs within 1 px | pass | worst edge-line distance to its VP 5e-13 px; f1/t1 frame shows guides converging on VP L |
| 4 | Tilt 15: VP 3 at f / tan 15; verticals meet there | pass | 4354.06 px both ways; a projected upright passes through VP 3 (u 600.000); horizon shift = f tan 15 |
| 5 | Ink snaps and says which; PNG without guides; survives reload; Clear empties | pass | f2/saved.png has render and ink, no guides, horizon or VPs; 2 strokes after a new tab; Clear drawing then 0 with "Undo brings it back" |
| 6 | Each target matched with its listed settings; no stop matches a target | pass | every target scores 1.000 and says "Matched."; best stop score per target 0.82, 0.73, 0.82, 0.70, 0.88, 0.81 (all under 0.95) |
| 7 | Camera and stage above the fold at every size; 60 fps with 20 buildings at 1920x1080 | pass | audit size rows (only Overlays and Buildings fall below the fold at 760 and 375); 2.1 ms per draw with 20 buildings, Guides and Windows on |
| 8 | How lines once in five slider moves; matched every time | pass (cited) | audit "Five held clicks" clean on the stops; Matched plus the settings line played on each of six matches (t8). The counts table is Craft's |

#### Findings

##### Blocker

1. **Check my drawing passes flat lines, and Snap teaches them.** Where: Ink, `misses()` (src.html:1102) and
   `lineEnd()` (src.html:2212), both using `Persp.targets()` with its default `horizontal` target
   (kit/perspective.js `targets`). What: at Turn 30 no building edge is level on the page (edges on the horizon aim at
   the VPs anyway), yet any screen-level line counts as a hit. I drew three flat lines across the towers with Check on:
   "All 3 lines hit their vanishing points." and the reflection opened, asking what I changed (f1/t1-check-level-lines.png).
   Drawing a roof edge flat is the classic two-point mistake, and this is the tool's one revise step (VA:Cr3). With
   Snap on, a roof edge 300 px above the horizon drawn 3 degrees off level snapped to "horizontal" and the status
   read "Last line: horizontal." (f1/t2), so the pen itself rewards the error. With Tilt 15 the same flat lines still
   pass (f2/t11). The check's message is a meter that misleads when its assumption fails, so this is a blocker
   (REFINE, Rounds). Better: drop the level target in this tool (snap and check). It is never needed: when Turn is 0
   or 90 the far VP comes back from `vps()` as an infinite direction whose angle is already level, so one-point views
   still snap and pass. Keep the upright only when Tilt is 0, as now. Tag: **family:perspective** (the engine's
   default target list).

##### Should fix

2. **Find the Camera can be solved from the scores, not the picture.** Where: Find, `showScores()` (src.html:1356)
   and the miss message (src.html:1422). What: after each Check the panel shows an exact percent per setting, and each
   score is a straight line toward the answer (turn 1 - |diff| / 40, eye 1 - |ln ratio| / ln 10). From Turn 0 the
   turn reads 25%, so the answer is 30; one check per lens button finds the lens. I matched target 1 in five checks
   without looking at the outline (f1/t3: turn 0, lens 24, eye 10, turn 30, eye 40). Checks cost nothing, so this is
   "trying every option for free" (BUILD.md wave lessons, No giveaways), and the round 2 change that took the live
   meter away only slowed the sweep down. Better: after a check show per setting only "matches" or "not yet" (no
   percent), keep the "read the X next" hint, and let the overall meter move in coarse steps; or count tries per
   target and offer Extend outline edges as the help instead of numbers. Tag: **general**.

3. **The two street-level targets ask for a precision the picture can't show.** Where: Find targets 2 (3 m) and 6
   (2.5 m), eye tolerance 95% = within 12%. What: at target 2 with eye 2.4 m (Turn and Lens right) the student's
   render and the amber outline are almost the same picture, the outline's horizon a few pixels off (f2/t8t9.png, top
   2.4 m, bottom 3.0 m), yet the eye scores 90% and the target is "Not yet". The outline has no floor lines, so 3 m
   cannot be told from 2.5 m or 3.4 m by reading; the student can only nudge the slider and press Check until the
   percent passes, which is finding 2 again. The hint for both says "Roofs below eye level are visible", but at 3 m
   no roof is. Better: give the eye score a tolerance tied to what shows on the page (for example the outline's
   horizon within a few pixels of the student's, or within 0.6 m below 10 m), or raise these two targets to heights
   that read clearly (for example 6 m and 4 m, still off every stop), and give low targets a hint about where the
   horizon cuts the nearest building's base. Tag: **general**.

4. **A fact on screen says tiers show undersides; they don't.** Where: Build fact line, `FACTS.bottoms`
   (src.html:346) and `bottomsShown()` (src.html:1691); notes.md "Things to talk about". What: the fact "Tiers above
   your eye show their undersides: above the horizon you see bottoms." came up at the sidewalk (f1/t4 tips), because
   `bottomsShown()` counts any bottom face projected on the page. The stepped tower's tiers sit on the wider tier
   below, so their undersides are hidden: the zoomed frame shows only walls at both setbacks (f1/t4-crop.png). The
   only real underside on screen is the water tank between its legs. notes.md asks "Which tiers show their
   undersides", which sends a class looking for something that is not there. Better: say "Things above your eye
   show their undersides, like the water tank on its legs: above the horizon you see bottoms.", show it only when a
   bottom face is actually drawn uncovered (the tank), and fix the notes question to the tank. Tag: **general**
   (a fact keyed to geometry, not to what the student sees).

##### Polish

5. **The reflection asks "What did you change" when nothing changed.** Where: Ink, Check my drawing, `#reflect`
   (src.html:246). After three lines that all hit with no red line ever (f1/t1), the question reads as a trick. Better:
   when `checkHadRed` is false ask "How did you aim each line at its vanishing point?" and keep the current question for
   a real fix. Tag: **general**.

6. **Composition is one recipe line.** Where: Build, `composeGoal` (src.html:365). The module is "Two-Point
   Perspective and Composition", but the only composition moment is one hint that gives the answer with the goal ("a
   low eye, a wide lens, the horizon low"). Better: two or three short briefs to pick from (make the tower feel huge,
   a calm wide street, a map-like view from above), each saved with the drawing, and let the student find the settings.
   This touches what the tool teaches, so it may belong in the spec's open questions. Tag: **general**.

7. **"Looking 48 degrees down" with parallel uprights needs one sentence.** Where: Readouts, Eye height
   (src.html:1675), audit frame state-helicopter-guides-plan-1366x768.png. From the Helicopter stop the readout says the
   block is 48 degrees down, but the camera stays level (the page is shifted), so uprights stay parallel. A student who
   knows real aerial photos lean will wonder why. Better: a readout note "The picture stays upright, like a drafting
   view; Tilt shows the real lean (three-point)." and the same line in notes.md "Good to know". Tag:
   **family:perspective**.

##### Nit

8. **Check my drawing tests direction, not place.** A line in empty sky aimed at VP R passes. Fine for a first
   check; a later version could ask that each line start on a building corner. Tag: **family:perspective**.

#### Other checks (nothing found)

- Facts recomputed: stand-back 155 m, 209 m, 359 m and 21, 36, 48 degrees down; "1 focal length = lens / 36 x page
  width"; VPs 2 / sin 2t focal lengths apart (the same number for every lens, as notes.md says); VP 3 and tilt-shift
  directions (looking up: VP 3 above center, center above the horizon). All match the spec's Sources.
- Hidden information: no target value is in the DOM before a match; the eye stops do not settle in Find; target 6
  says only "looks up". The giveaway is the scores (finding 2), not leaked text.
- Language is plain and right for 9-12. What it teaches, Key skills and Support at home describe this tool; the home
  ideas (a box from a low seat, receding room edges, a ruled box sketch) are doable tonight. No sensitive topics.
- Guardrails: no timers, no points beyond "Found N of 6". Nothing cultural, Native or hard-history: no sensitivity
  review needed.

#### Audit pilot

- **Confirmed:** the size rows I leaned on for Done when 7 (camera section and stage above the fold everywhere;
  Overlays and Buildings below it at 760 and 375); the five-held-clicks rows for Done when 8.
- **Wrong or by design:** "#clearInk nothing changed" (a fresh page has no ink; with two strokes it clears and says
  Undo brings it back, f2/t6); "#cv nothing changed" in Find (the stage takes no clicks in Find by design); the
  #cv / #checkCam2 overlap "at every size" is the stage chip, and the outline is fitted under it (f2/t8t9).
- **Missed (it can't see these):** the level-line pass in Check my drawing and the "horizontal" snap (blocker 1); Find
  solved from the per-setting percents (2); street-level targets that can't be read at the tolerance (3); the false
  underside fact (4); the reflection wording (5).

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: city-skyline-studio (Codex fix, round 1)

Evidence root: `_scratch/city-skyline-studio/`. Before and after shots used the same
1366x768 states unless a different size is stated. The initial driver failure was
retried once, smaller, successfully. No commits. refine.md and refine/ were not edited.

#### Blocker

1. FIXED. Snap and Check share inkTargets with horizontal:false; screen upright only at Tilt 0. Three flat lines changed from 0 misses plus reflection to 3 dashed red misses and no reflection. Near-flat Snap changed from horizontal to free. Tilt 15 also rejects all three; Turn 0/90 still snap to infinite side VPs. Evidence: fix-before/before-flat.png, fix-before/before-snap.png; fix-after/after-flat.png, fix-after/after-snap.png; final-ink-patterns.json.

#### Should fix

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

#### Polish accepted

12. FIXED. The current fact is visible on the Build stage at 1366x768, y=722.45..756, rather than below the panel at y=1376.17. Stacked layouts put it under the hint so it does not cover the drawing. Evidence: after-fold.json, fix-final/final-build-1366x768.png; the affected 760x900 and 375x812 Build frames were re-shot and viewed. The final right-side placement also leaves zero Plan overlap at 1366x768 and 1920x1080: overlay-plan.json, overlay-wide-plan.json and fix-overlay frames.
13. FIXED. Stacked hints have min-height 0 and take their text height: 23.19 px at 760x900 and 46.38 px at 375x812 in Build. Evidence: final-build-760x900.json, final-build-375x812.json and their frames; the affected 760x900 and 375x812 Build frames were re-shot and viewed.
14. FIXED. The hint says Most of your city and leads with Press Auto, with the wider-lens option conditioned on Auto. Auto restores the city from a -600% manual horizon. Evidence: proof-off-city.json, proof-off-city-auto.json and fix-support frames.
15. FIXED. The big panel button reads Next target after matches 1 to 5 and Start over on target 6. All six labels were checked in proof-find-tolerances.json, and the target-2 frame shows the large Next target button. Real held panel-button clicks advance to target 2 and, on the last target, return to target 1 with Tilt 0: final-panel-next.json and final-panel-start-over.json.
16. FIXED. offPage is Build-only. Find entry with no camera action speaks only welcomeFind, with no offPage delaying Check. Evidence: fix-voice/find-entry.json and .png; the subsequent five checks all speak their result. The held Build stop path still speaks offPage once: overlay-build-offpage-voice.json.
17. FIXED. Stage text grows with the large stage: 12 px becomes 14.4 px and 13 px becomes 15.6 px at 1920x1080, with actual stage width 1560 px. Evidence: proof-wide-type.json and fix-support/proof-wide-type.png; final-build-1920x1080.png.
18. FIXED. Narrow Find VP chips use short names at the stage edges, with extra bottom framing room. Viewed all six 375x812 targets; the chips stay beside the amber outline. Evidence: fix-final/final-find-375x812.png and phone-target-2.png through phone-target-6.png.
19. FIXED. Readouts and notes say the picture stays upright like a drafting view and Tilt shows the real lean. Evidence: proof-drafting-note.json and fix-support/proof-drafting-note.png with the 48 degree down readout.

#### Settled calls

- Applied: Rule 5 does not apply; contract kept. No sensitivity file was present.
- Left the composition-brief open question to the spec owner. No new feature or topic was added.
- Used the suggested visual allowance for the low targets, keeping the listed target cameras. No questions were asked in this unattended session.

#### Cheats tried

- Three flat strokes at Turn 30: 3 misses, reflection closed. Same at Tilt 15: 3 misses, closed.
- Three uprights: 0 receding lines, closed. Uprights placed on a VP's screen column: closed.
- Three Tilt-15 upright strokes aimed at VP 3: 0 receding lines, closed. Erasing the only red stroke leaves a missing-line message; replacing it with an upright still cannot complete. Evidence: final-tilted-uprights.json and final-erasure-and-uprights.json.
- Original per-setting-percent inversion: neither numeric eye nor turn feedback is available; the initial camera remains unmatched.
- All five eye-stop buttons, with every other setting correct, for every target: 0 matches in 30 attempts.
- Sweep all four lenses with the untouched default eye and turn: 0 matches in 4 attempts.
- Low-target tolerance: +/-0.6 m passes; +/-0.9 m fails on both. Sidewalk stop still fails on target 6.
- Positive controls: all six exact hidden cameras match; three actual receding edges open the neutral aiming reflection; a red edge undone and redrawn correctly opens the revision reflection.
- Check tests line direction, not placement on a face. That optional nit remains as listed in refine.md.

#### Voice walk

Held clicks were 120 ms, with a 2 s action pace, using scripts/drive.py and its CDP helpers.
Main path heard: welcomeBuild, turnHow, guidesNext, guidesHow, composeGoal, welcomeInk, checkHow, checkFix.
The add action completes the bridge step before buildNext starts; a separate held Guides-first path heard guidesHow then buildNext.
Fresh correct-edge path: checkHow, checkAim. Revision path: checkHow, checkFix, checkReflect.
Find: welcomeFind; five missed checks each speak a miss event, then findEye once. Lens path speaks findCheck and findLens once.
Empty city: welcomeBuild while the city exists, cut on clear, then addFirst once. No welcome over the empty city.
voice/lines.json equals allLines(), 45 strings. Matching recordings remain; revised strings use browser speech fallback. No audio was recorded.

#### Checks and frames

- Final bundle: 904016 bytes. No tool network requests in the measured resource lists. JSON manifests validate; allLines and voice manifest are equal at 45 strings. git diff --check is clean. refine.md and refine/ have no diff; the temporary host file was removed.
- Viewed all 88 fix frames, including five final overlay frames. The first 83 comprise 13 before, 12 direct after, 12 supporting probes, 8 voice paths and 38 final-size/target/regression frames. All three modes were shot at all eight STANDARDS sizes. Only affected stacked Build frames were repeated after the fact was moved below the hint.
- The first phone host fixture requested a missing favicon. The temporary host now supplies a data favicon; subsequent phone runs are clean. This was a host-page request, not a request by the bundled tool.
- Motion off plus grayscale was viewed at 1366x768. At 1920x1080, 20 buildings with Guides and Windows averaged 3.44 ms per draw over 60 draws, below the 16.67 ms frame budget. This measures draw cost, not display refresh rate.

#### Feel check

The best moment remains lifting the eye and seeing the city turn into a rooftop plan while the guides remain exact. The two flat moments were hunting below the fold for Buildings and nudging an unreadably precise street-eye answer; both are addressed above. The sky painting, shaded architecture, tank details and play remain. Compared the final 1366x768 frame with the existing Beat Lab bar frame, without writing to that other tool.

| City Skyline Studio | Beat Lab bar |
|---|---|
| ![Current city](../../_scratch/city-skyline-studio/fix-overlay/overlay-default.png) | ![Existing bar frame](../../_scratch/city-skyline-studio/bar-frames/beat-lab.png) |

#### Engine changes wanted

None. All changes are tool-local, using the engine's existing target options.

#### Audit

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

#### Left open

- The spec owner's composition-brief question and the optional nits remain outside this pass.
- Source facts use the existing Joseph D'Amelio construction and Szeliski pinhole sources in spec.md; underside visibility is verified against the actual painted tank faces. No replacement unsourced fact was added.
- Full audit completion remains open because of the session interruption, including the unfinished stages listed above.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### City Skyline Studio build handoff

#### Current fix round, 2026-11-04

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

#### Cold review changes, 2026-11-03

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

#### Structure

The existing starter-based implementation was retained and completed against the current spec, including both
Refine changes sections. src.html contains the kit/theme links, responsive layouts, content and voice tables,
saved state, geometry adapters, canvas rendering, Build, Ink, Find, and keyboard/pointer handlers.
It uses kit/perspective.js unchanged. window.__tool exposes state (also S), camera helpers, actions, and voice logs.

#### This build

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

#### Geometry and storage

The camera uses a 36 mm sensor. The eye stands back 120 + 0.6 (eye - 1.6) m. Auto horizon uses lens shift,
not a changed projection. Tilt uses the engine's pitched camera and third VP. Windows divide real faces projectively.
Find uniformly shrinks both pictures per target, then centers them; the readout states that effective focal scaling.
The six revised targets are 40/30/24/0, 3/45/35/0, 100/20/24/0, 20/55/35/0, 300/40/35/0, 2.5/15/24/15.
The meter changes only after Check camera. Every included setting must reach 95%, rather than just the mean.
Ink is screen-space relative to the image center in page-width units. Its camera and reflection note are saved with
the city in localStorage city-skyline-studio. A later camera change offers Keep it or Clear it. All modes state
device-only storage. Save picture renders a separate stage-size PNG and never draws guides or VP labels.

#### Decisions and open questions

The spec has no explicit open-question list. Its final Refine changes replace the earlier target list and live
silhouette meter. The existing 24 mm default lens is retained. Art: none was expanded with one sky painting under
the build brief's express permission to add art where it lifts the scene. All construction remains in code.
Example city retains its supplied central-lot coordinates, including 45 m centers; moving or adding snaps to 10 m.
No new modes, topics, exports, or cross-device features were added.

#### Evidence

All evidence is under _scratch/city-skyline-studio/. numbers.json recomputes the spec. verification.json records
projection checks, real jittered Plan drag, five palette additions, snapped ink, hatch/fill, Undo/Redo, freehand
revision/reflection, saved note reload, Keep it, Clear drawing, all six 100% matches, and 20-building performance.
full/ contains the one complete size pass. functional/ includes the exported PNG and student workflow frames.
affected/ holds only targeted follow-up frames. bar-comparison.png compares the tool with Beat Lab.
voice-held-stops.json and voice-matched-repeat.json contain held-click logs. Existing 39 voice recordings were
retained; no audio was recorded or regenerated. The final mechanical audit is under audit/.

#### Known limits

The 375 px Find stage is only 200 px high to keep Camera in view. Every target fits, but outlines are small.
Long panel sections scroll; only Camera is shown initially in the 680x425 Build preview, as specified.
Deliberate extreme lens-shift settings can put the entire city off the page; the hint explains the next control.
Plan drag is exact. View drag near eye height uses an alternate horizontal plane to avoid a singular intersection.
Some inherited template expressions and HTML attribute lines remain longer than 160 characters.
Old refine.md and refine/ records predate this build; codex-report.md is the current check record.

#### Engine changes wanted

None. Shared kit, engine, family documentation and scripts were not modified.

#### Final audit record

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

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: refine.md folded in (last changed 2026-11-04)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-04)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-04)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-04)
- 2026-11-25: polish.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
- 2026-11-25: earlier round refine-2026-10-28 moved to S:/CurioClass-archive/tool-rounds-2026-11-25/city-skyline-studio
- 2026-11-25: earlier round refine-2026-10-28.md moved to S:/CurioClass-archive/tool-rounds-2026-11-25/city-skyline-studio
