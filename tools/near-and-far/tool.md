# Near and Far: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: near-and-far

#### Built

Three offline modes: Valley composition, eight live-goal postcards, and eight Hogarth perspective finds.
Painted valley, cutouts, a camera-derived Side View, ghosts, overlap warnings, fading, keyboard controls,
saved Valley and solved indices, before/after wipe, zoom, and kit narration. No commits or polish round.
Bundle: 792696 bytes (774.1 KiB). All writes stayed within the requested tool and scratch folders.
Report evidence was collected in Scratch during the build; this final report is written last to honor the stop instruction.

#### Numbers check

Independent Python: _scratch/near-and-far/check_numbers.py and numbers.json. Camera examples match exactly:
cow at 30 m: 45 px, bottom 307.5; barn at 120 m: 60 px, bottom 273.75.
Balloons at 100, 200, 600 m: heights 162, 81, 27 px; basket bottoms -84, 89.25, 204.75 px.
First complete balloon: 193.7142857 m. The spec's 194 m sentence attaches the 200 m pixel values to it.
Post/cow tops agree with the horizon at 10, 25, 60, 200 m. A 12 m pine reaches the size limit at 19.2 m.
Contrast: white/brand 6.970, brand/paper 6.381, ink/paper 13.673, muted/paper 5.992,
ink/sky 10.780, ink/white 14.934. Scene heights are stated as settings, not general real-world facts.

#### Feel check

Best: the fence posts shrinking into a line with every top at eye level, followed by the gold postcard and wipe.
Flattest 1: the tiny cow's resize handle covered its grab area. Moved the handle to a separate 44 px target.
Flattest 2: the opening words crowded the horizon in the compact preview. Moved and shortened that caption layout.
Played all eight postcards with real held clicks, drags and corner resizing: student-results.json, 8 of 8 pass.
Also solved puzzle 1 using only Tab, Enter, arrows, equals and minus. All eight print zooms were inspected.
Compared bar-comparison.png with Snowy Mail Route and opened Beat Lab's bundled screen. This scene is not plainer:
layered painted grass, lake and sky, detailed cutouts, paper framing, notebook controls and immediate visible cue changes.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

Reference frames: Snowy Mail Route and Beat Lab. Quick frames: 1366 Valley, compact Valley/Puzzles and first print zoom.
Full matrix once: all three modes at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900.
375x812 host: all three modes. Detail frames: empty start, calm grayscale, largest/smallest objects and finds 1 to 8.
Earned postcards 1 to 8, a mid-wipe frame, compact readout checks, and the real-input student postcard frames 1 to 8.
Audit: all 57 size/state/calm PNGs opened in fifteen labeled sheets; relevant leads also checked at full resolution.
Final focused frames: compact caption, Side View labels, six focused lead frames, full logic, and the phone Barnyard..

#### Art made

One new image: valley, generated with the built-in image tool, saved to art/raw/valley.png and rekeyed with art.py.
Preserved eleven supplied FLUX cutouts and the supplied Met CC0 print. Twelve painted images plus one real print.
Total art: 517.1 KiB; bundle 774.1 KiB. No redraw was needed; the painting's vertical placement was adjusted.
Final WebP and all cutouts were visually inspected. Prompts, provenance and credit are in the tool folder.

#### Art still to paint

None. No people were generated. People in the supplied historical print are part of the public-domain artwork.

#### Engine changes wanted

None. The spec's open family question was resolved toward its stated None: a standalone camera implementation.

#### Left open

- The universal 2 px post condition conflicts with the required Solid tolerance, as documented above.
- Gravel-ranger is selected in voice/lines.json; narration uses the kit's browser fallback. No audio was recorded.
- The supplied windmill has a masonry tower, while the asset description mentions wood. Supplied art was preserved.
- At extreme saved distances, resizing down can draw an object below 2 px; its normalized composition
  and 44 px grab target are preserved. A new pixel floor would change the size cue and therefore its depth.
- Secondary notebook readouts can need scrolling at 680 and 375; the primary Side View and controls are visible.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: near-and-far
#### Played
Played before builder files as a Grade 4 solo student: Valley, all eight postcard starts, the print hunt and Escape.
Then solved all eight postcards with held clicks, jittered real drags and corner resizing; solved puzzle 1 by keyboard.
Checked the compact/projected view too. The painted valley and earned before/after postcard are strong.
VA:Cr2 is practiced through composition and revision; VA:Re7 through identifying and explaining the print's mistakes.
Evidence is in _scratch/near-and-far/: cold/play/hands frames, review-play/results.json and review-keyboard.json.

#### Findings fixed
- Blocker, general, src.html drawSide: the eye was fixed five pixels above ground, unrelated to the 1.5 m camera.
  It now follows the objects' shared vertical scale. Exact cow and post solutions meet eye level.
- Should fix, general, Puzzle 3: its cover goal ticked before the pictures overlapped. Actual overlap is now required.
- Should fix, general, pointer selection: preventDefault discarded focus, so arrows after clicking did nothing.
  Stable object nodes now receive focus with preventScroll. A real click plus arrow moves exactly one percent.
- Should fix, general, Mixed-Up Picture: fitting moved the print but left its spotlight at old coordinates.
  Fit now recomputes the ring; compact and phone zoom frames were checked.
- Should fix, general, fade readout: only misty-near disagreements were explained. Every wrong fade band now gets
  concise advice in Valley and Misty Hills; other postcards retain their specified goal focus.
- Should fix, general, horizon chip: repeated fitting could squeeze its caption into several lines. Prevented wrapping.
- Should fix, general, narration: fixed Read hints were absent from allLines and voice/lines.json. Both now agree.
- Should fix, general, windmill art: masonry contradicted the wooden-tower brief. Repainted a detailed timber tower.
- Should fix, general, selected-cow readout: cropped at 680x425, 1280x720 and 375x812.
  Tightened short-screen shelf spacing, omitted the redundant compact notebook title and shortened fade advice.
  The full readouts, all shelf choices and 44 px controls now fit; the postcard keeps its size.
- Should fix, general, audit-states.json: solved-wipe drag expressions returned no points, so the state was unsolved.
  Added explicit returns. The corrected recipe reaches the earned wipe at 680, 1366 and 375.
- Polish, general: the completed hunt still asked for more finds and repeated completion on revisits.
  Added current next-action wording and a revisit label; completion narration triggers on the newly found eighth error.
- Polish, general: a stationary press cut applicable instructions. Actual movement now invalidates that speech.
- Polish, general: the first cow barely registered in Side View. A shared scale for small subjects gives it 40 px
  at 1366x768 while preserving relative heights. Redrew the flat hills with layered painted texture and natural ends.

#### Findings left
- Should fix, spec: Done when 2 promises universal two-pixel post alignment, but the required Solid tolerance allows
  larger errors. Changing that tolerance would change the spec; exact solutions do meet the horizon.
- Should fix, spec goals: other postcards can satisfy their listed goals while displaying an overlap warning.
  Enforcing overlap in all of them would add goals. The written warning remains; Puzzle 3's explicit goals work.

#### Flattest moment left
Fine tuning a tiny far object still takes patience. The 44 px grab area, keys and existing target outline support it.
Automatic snapping or another distance control would change the specified interaction and was not added.

#### Graphics
Checked all 12 painted assets in the shelf/postcards and the public-domain print at all eight zoom spots.
Redrew hills and windmill with built-in imagegen. Full prompts: art/prompts.json; raw outputs: art/raw/hills.png
and art/raw/mill.png; final assets: art/hills.webp and art/mill.webp. No people were generated.
Kept the valley, nine other cutouts, notebook framing and gold/wipe payoff. Compared with the existing bar frame.
Total final WebP art: 559.7 KiB. Final bundle: 851595 bytes, 833.2 KiB, below 2 MB.

#### Audit
One full audit finished inside the 2400-second limit: _scratch/near-and-far/review-audit/audit.md, 32 leads.
- Fixed five confirmed leads: three cropped readouts and two consequences of the invalid wipe recipe.
- Fourteen hill/object overlaps are intentional in that flat starting picture; exposed areas and keyboard selection work.
- Twelve welcome skips follow STANDARDS: a first action's own line wins, with no late empty-Valley welcome.
- One caption keep lead is a hit-test false positive from pointer-events:none; its text is visibly clear.
All 68 audit PNGs were inspected in labeled sheets. Every initial size/mode, Motion off and resize-mid-action was clean.
Scoped rechecks only: review-audit-fixes/results.json and results-last.json. Wipe succeeds at three sizes;
complete cow readouts pass at 680, 1280 and 375. The final two checks have zero leads and zero console errors.
Two scoped wipe warnings classify the temporary BEFORE overlay against an underlying object; these are intentional.
No full audit was rerun after the fixes.

| Line | Kind | Expected starts | Observed |
|---|---|---:|---:|
| dragHow, five shelf taps | how | 1 | 1 |
| dragHow / sideHow, five real drags | how | 1 each | 1 each |
| ghost, five edits | event | 5 | 5 |
| solved, five completions | event | 5 | 5 |
| find events, including revisits | event | 5 | 5 |

First-tap stage/control/mode/Read/Sound/key cases, fast stale-line changes, Read interruption and Sound-off Read passed.
Independent review-numbers.json matches the camera examples and contrast ratios; exact fence-top errors are zero.
Notes open with the three required sections. Tool storage clears correctly. No external assets or fetch calls.
Chrome ports 9950/9951 and host 8755 are closed; host.html is removed. No commits were made.

#### Left open
- A 10 m place / 12 m size post is Solid under the specified ratio yet misses eye level by 22.5 px at 1000x625.
- The first complete balloon is at 193.714 m. The spec's 81 px height and 89.25 px bottom belong to 200 m, not 194 m.
- A saved composition can draw an extreme object below two painted pixels after shrinking the window; its normalized
  cues and 44 px grab target remain intact. Enforcing a new floor would change that composition's depth.
- Narration remains browser fallback. No gravel-ranger clips were recorded, as instructed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Near and Far build handoff

#### Structure

src.html starts from the kit starter. It contains local styling, the postcard stage and notebook panel,
then the content tables and camera, interaction, puzzle, narration and print functions.
Curio.voice owns the queue; the tool owns the visible hint. No family engine is imported.
The single-file offline bundle is near-and-far.html. Build with CURIO_DRAFT=1.

#### Important implementation choices

- Coordinates are fractions of a true 16:10 postcard. The normalized focal length is 1.44 postcard heights.
- The Side View has a logarithmic 4 to 1000 m horizontal scale. Object heights share a linear vertical scale
  sized to the current objects; hills are a scenic-band exception. Diagram ghosts show both conflicting distances.
- Every picture has a minimum 44 px grab area independent of its painted size. The resize handle has a separate
  44 px target. The DOM nodes for objects remain stable during manipulation.
- The generated valley is shifted down 2.35 percent inside the clipped postcard so the painted shore meets
  the 42 percent horizon. The shoreline polygon and interpolated snapping edge are beside lakeLeft().
- The valley, nine supplied cutouts and the Met print were retained. Cold review redrew hills and the windmill.
- Hills use the top band as their placement cue, with size ignored. This reconciles the specified wide scenic band
  and its horizon condition; treating the bottom as an ordinary 300 m object makes those instructions conflict.
- Soft and misty use SVG color matrices toward #d9e6ee, plus reduced edge detail, rather than transparency.
- New taps stop or replace old animations and invalidate narration immediately. No interaction awaits an animation.
- Valley data and solved indices alone use the two tool storage keys; the shared kit additionally stores Motion.

#### Open question decided

The spec asks whether to join the perspective family. It names Family engine: None and leans toward remaining
independent, so this build stays on its own. The ground-plane formula is shared in principle, without importing
the perspective engine or changing kit files.

#### Spec discrepancies

- A balloon first fits fully at 193.7142857 m. The stated 81 px height and 89.25 px basket bottom are at 200 m,
  not at 194 m. The Sources section gives the correct 200 m example. Camera arithmetic follows the formula.
- Solid has a 25 percent ratio tolerance, so Done when 2 cannot universally imply post tops within 2 px.
  Exact solutions do meet the horizon within floating-point error. The tolerance was retained, as specified.
- Cold review replaced the supplied masonry windmill with the specified wooden tower and redrew the flat hills.
- Extreme saved objects can fall below 2 painted pixels when a large viewport is shrunk. Keeping normalized
  size and placement unchanged preserves the composition and its depth; enforcing a new pixel floor would change
  that depth. The 2 px constraint applies when editing, and the grab area remains at least 44 px after resizing.

#### Art and voice

art/prompts.json records nine retained FLUX cutouts, the generated valley and two cold-review redraws with provenance.
art/public-domain.json is the supplied Met credit record. The house style is soft painted storybook gouache.
voice/lines.json lists all fixed lines, with gravel-ranger selected. No speech was recorded; browser fallback is active.

#### Cold review changes, 2026-11-01

- Puzzle 3's cover goal now requires actual overlap before ticking.
- Pointer selection focuses the stable object node with preventScroll, so arrows work immediately after a click.
- A no-movement press preserves applicable speech; actual dragging invalidates it on the first movement.
- The Side View uses the true 1.5 m eye on its shared vertical scale and makes a lone small subject visible.
- Valley and Misty Hills readouts explain every incorrect fade band, rather than only misty near objects.
- Zoom spotlights are recomputed on resize, including the phone layout's first fit.
- The completed print hunt offers revisiting and gives a current next action.
- Every fixed Read hint is included in allLines() and voice/lines.json.
- Built-in imagegen redrew hills and the wooden windmill; full prompts and provenance are in art/prompts.json.

#### Engine changes wanted

None. No kit or shared file was changed.

#### Evidence

All scripts, screenshots, comparison frames and checks are in _scratch/near-and-far/.
numbers.json contains the independent camera and contrast calculations. functional-results.json records the
camera examples, eight puzzle solutions, incorrect overlap, storage clearing and print-hunt checks.
keyboard-results.json records a solution of puzzle 1 using only Tab, Enter, arrows, equals and minus.
The final codex-report.md gives the inspection results and any remaining limits. No polish round was started.

#### Build audit disposition, before cold review

The full audit completed with 43 leads. Twenty-nine were addressed by caption/horizon layout, native checkbox size,
side-view check placement, block setting text on phones, and preserving applicable speech across quick repeats.
Twelve welcome-skip leads follow the explicit first-action rule: placing an object speaks its current drag how-to,
and the empty-Valley welcome becomes stale. Two readout keep leads remain: the secondary notebook readout needs
scrolling at 680x425 and 375 wide, while the live Side View and main controls remain in view.

Focused checks using the same audit geometry routine are clean for empty, selected cow and balloons at 680 and 375.
voice-quick-results.json records three welcomes and dragHow each starting once and remaining uncut across repeats.
The full audit was not repeated. A solved-wipe recipe was added to audit-states.json after that full run;
the same solution and wipe were separately played through the real controls and inspected.

#### Cold review audit, 2026-11-01

The single full cold-review audit finished inside its 40-minute limit with 32 leads, in
_scratch/near-and-far/review-audit/. Five confirmed leads were fixed: three cropped selected-cow readouts and
two consequences of a solved-wipe recipe whose drag expressions did not return their points.
Targeted rechecks in review-audit-fixes/ show the complete readouts at 680, 1280 and 375, and an actual solved
wipe at 680, 1366 and 375. The final two readout checks have no mechanical leads or console errors.
The other 27 full-audit leads were 14 intentional hill/object overlaps, 12 expected first-action welcome skips,
and one transparent-caption hit-test false positive. All 68 audit PNGs were inspected in labeled sheets.
Motion off and resize-mid-action checks were clean. No full audit was rerun after the scoped fixes.
The compact Valley layout hides its redundant notebook title and tightens shelf spacing; the postcard stays large.
See codex-review.md for the final review, spec conflicts and voice counts.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
