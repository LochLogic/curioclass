# Codex report: city-skyline-studio

## Built

Build only, 2026-11-01. Completed the existing starter-based tool against the full spec and its two revision sections.
Build, Ink, and Find the Camera use the shared perspective engine unchanged. Added generated dusk art, architectural
surface detail, motion-aware sky drift, kit tones, 10 m movement, label avoidance, reliable repeat-match narration,
mode scroll reset, target-extension reset, teacher notes, source credits, audit states, and handoff. No commits.

## Numbers check

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

## Feel check

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

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

Both bar-tool frames; `early/` all four frames; `functional/` all workflow frames and the actual export; `full/` all 30
frames in contacts plus phone/extreme frames individually; `voice-keys/` all three; `affected/` targeted frames individually;
`final-frames/` all seven post-audit targeted frames individually.
Full pass: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, and 375x812 iframe, all three modes.
Also checked tilt +/-25, turn 0/90, 85 mm, horizon -600%, empty city, 80 floors/80 m dimensions, calm, grayscale,
keyboard drawing and 2 s held-click voice. Mechanical audit frames viewed through numbered contact sheets.

## Art made

One generated image, `art/dusk-sky.webp`: 1600x900, 75.39 KiB, no people. Built-in image tool, full prompt in prompts.json.
Converted with `art.py city-skyline-studio --rekey dusk-sky`; inspected the finished WebP and in-scene frames. No redraw needed.
Final bundle: 1,099,908 bytes (1074.13 KiB), under 2 MB. Existing 39 narration recordings retained; no audio was recorded or regenerated.

## Art still to paint

None.

## Engine changes wanted

None. No shared engine, kit, docs, scripts, branches or other tool folders were modified.

## Left open

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
