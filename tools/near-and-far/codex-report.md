# Codex report: near-and-far

## Built

Three offline modes: Valley composition, eight live-goal postcards, and eight Hogarth perspective finds.
Painted valley, cutouts, a camera-derived Side View, ghosts, overlap warnings, fading, keyboard controls,
saved Valley and solved indices, before/after wipe, zoom, and kit narration. No commits or polish round.
Bundle: 792696 bytes (774.1 KiB). All writes stayed within the requested tool and scratch folders.
Report evidence was collected in Scratch during the build; this final report is written last to honor the stop instruction.

## Numbers check

Independent Python: _scratch/near-and-far/check_numbers.py and numbers.json. Camera examples match exactly:
cow at 30 m: 45 px, bottom 307.5; barn at 120 m: 60 px, bottom 273.75.
Balloons at 100, 200, 600 m: heights 162, 81, 27 px; basket bottoms -84, 89.25, 204.75 px.
First complete balloon: 193.7142857 m. The spec's 194 m sentence attaches the 200 m pixel values to it.
Post/cow tops agree with the horizon at 10, 25, 60, 200 m. A 12 m pine reaches the size limit at 19.2 m.
Contrast: white/brand 6.970, brand/paper 6.381, ink/paper 13.673, muted/paper 5.992,
ink/sky 10.780, ink/white 14.934. Scene heights are stated as settings, not general real-world facts.

## Feel check

Best: the fence posts shrinking into a line with every top at eye level, followed by the gold postcard and wipe.
Flattest 1: the tiny cow's resize handle covered its grab area. Moved the handle to a separate 44 px target.
Flattest 2: the opening words crowded the horizon in the compact preview. Moved and shortened that caption layout.
Played all eight postcards with real held clicks, drags and corner resizing: student-results.json, 8 of 8 pass.
Also solved puzzle 1 using only Tab, Enter, arrows, equals and minus. All eight print zooms were inspected.
Compared bar-comparison.png with Snowy Mail Route and opened Beat Lab's bundled screen. This scene is not plainer:
layered painted grass, lake and sky, detailed cutouts, paper framing, notebook controls and immediate visible cue changes.

## Done when

1. PASS: cow at eye-level agreement is Solid; resizing alone produces two ghosts and both distances in words.
   functional-results.json and the real drag frame verify independent place/size changes.
2. FAIL as a universal statement: the specified 1.25 Solid ratio can allow more than 2 px of post-top error.
   Exact five-post solution PASS: maximum error below 0.000000001 px at the actual 1366x768 postcard.
   Retained the specified tolerance; explained the conflict in handoff.md rather than changing the rule.
3. PASS: wrong barn-on-top arrangement fails and has a written overlap warning; Front on the haystack passes.
4. PASS: balloons move lower toward the horizon as distance increases; all worked numbers match the formula.
5. PASS: visually checked all eight zoom spots; Show me one reaches all eight; real Escape restores the whole print.
6. PASS: five real drags at a two-second pace spoke dragHow and sideHow once each. Solved spoke 5 of 5 times;
   finds spoke on all 10 tested events, including repeats. Read and mode interruption were checked.
7. PASS for main controls: 44 px grab/resize areas, Front, Back, Fade and Next visible at every required size.
   The secondary notebook readout can require panel scrolling at compact sizes; live Side View text stays visible.
8. PASS: keyboard-puzzle1 frame and keyboard-results.json show both goals true using real key events.
9. PASS: both Clear buttons remove their tool storage keys; no other tool data is stored. Shared kit stores Motion.
10. PASS: measured 16:10 postcards at 1366x768, 680x425 and 375 wide; painting shifted 2.35% to the 42% horizon.
11. PASS: real interruption tests with Motion explicitly on: Side View and wipe animations were running,
    a new drag/Next acted immediately, rapid zoom moved to find 2, and no exceptions or stale-scope speech occurred.

## Wave lessons

- Hint and voice: PASS. Current action/control named immediately; Read uses that hint. How selection uses V.heard.
- Focus and layout: PASS. Stable object/control nodes during edits, no focus on load, preventScroll on explicit focus.
- Sizes: PASS for main targets, unclipped hint and core controls in the full size/mode matrix and phone host.
- No giveaways: PASS. Creation goals are explicit; success requires jointly matching independent size/place cues.
- Honest numbers: PASS. Camera and heights are scene settings, and source arithmetic was recomputed independently.
- Standards: PASS. Solo composition/revision practices VA:Cr2; the print hunt practices VA:Re7.
- Motion off: PASS. No running animations after the toggle; the sky loop uses animation:none in calm mode.
- Short choice sets: PASS. All eleven shelf choices are visible together, including the 375 px four-column shelf.
- Resize mid-animation: PASS. Window changes preserve state; controls stay enabled; no stale scene-node exception.
- Deferred welcome: PASS. No welcomeAfter; action lines win the first tap and welcomes have current-state checks.
- Unknown as unknown: PASS. Conflicting cues show ghosts and written disagreement, not a false Solid badge.
- One look, one meaning: PASS. Check plus Solid, paired ghosts, and crossed overlap lines have distinct meanings.
- Badge truth: PASS. Goal ticks are derived from current geometry; wrong overlap fails the relevant goal.
- Hints change back: PASS. Mode entry/reset selects a current hint immediately; no hint waits for narration.
- No answer by copying: PASS. Students arrange the artwork; there is no answer-card wording to match.

## Audit leads

One full audit finished in the 40-minute cap, with 43 leads. A metadata UTF-8 startup error was fixed before it began.
- 8 checkbox-target leads: fixed with a native 44 by 44 px checkbox.
- 6 caption/horizon hidden-text leads: fixed compact caption crowding and the noninteractive-layer hit-test issue.
- 5 horizon/object or handle overlaps: fixed by placing the label in a free part of the postcard.
- 1 phone setting/name overlap: fixed by keeping the scene setting on its own line.
- 1 phone Side View check/summary overlap: fixed by lowering the compact check.
- 8 quick-tap speech cuts: fixed; active mode taps preserve their welcome, and another shelf tap preserves dragHow.
- 12 skipped welcomes: expected under STANDARDS. The first action speaks its own how-to; an empty-Valley welcome
  becomes stale once the object lands. Clear valley's event itself names the next shelf action.
- 2 readout keep leads: left open as secondary-panel scrolling at 680 and 375; live cue text stays in the Side View.
All six focused geometry checks are now clean at 680/375, and final quick speech checks pass. No console errors.
The full audit was not repeated; targeted checks used its same geometry routine. The solved-wipe audit recipe
was added afterward, supported by the separately inspected real-input solution and wipe.

## Frames looked at

Reference frames: Snowy Mail Route and Beat Lab. Quick frames: 1366 Valley, compact Valley/Puzzles and first print zoom.
Full matrix once: all three modes at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900.
375x812 host: all three modes. Detail frames: empty start, calm grayscale, largest/smallest objects and finds 1 to 8.
Earned postcards 1 to 8, a mid-wipe frame, compact readout checks, and the real-input student postcard frames 1 to 8.
Audit: all 57 size/state/calm PNGs opened in fifteen labeled sheets; relevant leads also checked at full resolution.
Final focused frames: compact caption, Side View labels, six focused lead frames, full logic, and the phone Barnyard..

## Art made

One new image: valley, generated with the built-in image tool, saved to art/raw/valley.png and rekeyed with art.py.
Preserved eleven supplied FLUX cutouts and the supplied Met CC0 print. Twelve painted images plus one real print.
Total art: 517.1 KiB; bundle 774.1 KiB. No redraw was needed; the painting's vertical placement was adjusted.
Final WebP and all cutouts were visually inspected. Prompts, provenance and credit are in the tool folder.

## Art still to paint

None. No people were generated. People in the supplied historical print are part of the public-domain artwork.

## Engine changes wanted

None. The spec's open family question was resolved toward its stated None: a standalone camera implementation.

## Left open

- The universal 2 px post condition conflicts with the required Solid tolerance, as documented above.
- Gravel-ranger is selected in voice/lines.json; narration uses the kit's browser fallback. No audio was recorded.
- The supplied windmill has a masonry tower, while the asset description mentions wood. Supplied art was preserved.
- At extreme saved distances, resizing down can draw an object below 2 px; its normalized composition
  and 44 px grab target are preserved. A new pixel floor would change the size cue and therefore its depth.
- Secondary notebook readouts can need scrolling at 680 and 375; the primary Side View and controls are visible.
