# Cartoon Soundtrack Mixer: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: cartoon-soundtrack-mixer

#### Built

Built Theater, Score it and Mood Swap around the original 24-second Whiskers and the Storm cartoon. Four music cues have five live shapers, six presets, ten synthesized effects, quarter-second placement, dragging, scrubbing, scene playback, secret class guesses and device-only writing and saving.

The self-contained bundle is `cartoon-soundtrack-mixer.html`. Source is 1,391 readable lines, maximum 159 characters. The draft manifest is stage built. Teacher notes, ten-line voice manifest, audit states, prompts and handoff are present. No git commits, publishing or polish round. Shared kit files were not changed.

#### Numbers check

- Python evidence: `_scratch/cartoon-soundtrack-mixer/numbers.txt` and `source_checks.py`.
- Four scenes times six seconds equals 24 seconds. Quarter-second snapping gives 96 divisions. Narrow timeline: 720 pixels divided by 24 seconds equals 30 pixels per second.
- Two bars at 66, 104 and 152 beats per minute last 7.272727, 4.615385 and 3.157895 seconds. Six seconds is 82.5 percent of the slow loop.
- The source's approximate 680 px estimate of 27 px/s disagrees with its 62 percent formula, which gives 17.5667. The 1366 and 1920 estimates round correctly from 35.2883 and 49.6. A full 375 px divided by 24 gives 15.625 before margins. Actual layout is responsive; the narrow scrolling scale is exact.
- Recomputed supplied contrast pairs: 10.1886, 15.0072, 7.7623, 12.6210, 8.5686, 12.6467, 8.9632, 8.6970 and 11.3947 to one. They meet AA for text.
- The art list names 16 assets, although its total says 15. All 16 are made and used.
- Content explicitly puts Funny's Boing at 7.2 s, matching the puff, while Done when 4 generalizes about the 7.0 s flash. The explicit score timing was retained. Scary and Sad have Thunder at 7.0 s; all three have Tiny mew at 16.0 s.

#### Feel check

Walked the student flow through the silent film, shaping cues, effects placement, full playback, live swaps and saved writing. All Chrome checks were muted as required, so this is visual and scheduling evidence, not a human headphone listening verdict.

Best moment: the storm keeps moving through a score swap, followed by the tiny kitten reveal and the warm curled-up ending. The gray kitten was redrawn smaller to match the carried and sleeping kitten.

Two flattest moments and changes:
- The short preview squeezed the film and hid presets. Packed its header, moved transport over the frame, used a compact Preset menu and kept the shapers visible.
- The completed three-way demo pointed back to the same demo. It now points to Start scoring; closing the writing card also restores a useful next action.

Bundled and opened scratch copies of Snowy Mail Route and Beat Lab without writing to their folders. Compared the tool with Beat Lab in `_scratch/cartoon-soundtrack-mixer/feel-compare.png`. The theater and cartoon have substantial painted detail. The film remains small in a short preview with both effects lanes occupied.

#### Done when

1. PASS: movie frame, transport and timeline stay in the viewport at 1366x768, 680x425 and the 375 px host. All STANDARDS sizes were checked. Dense two-lane compact use has the limitation below.
2. PASS for scheduled behavior: switches preserve the picture clock. Recorded switch handling advanced it by zero to eight milliseconds, with incoming notes scheduled at the current position. Perceptual listening remains open.
3. PASS for scheduled behavior: live tempo, instrument and loudness edits replace the active cue immediately. Beat anchors preserve musical phase across tempo changes. `repair-frames/tempo-phase.png` and `tempo-phase.json` show the live edit.
4. FAIL against the literal all-score flash wording: Funny's explicit Boing is 7.2 s, rather than 7.0 s. Placement and synchronization checks passed: real drag placed Boing at 7.25 s, a second drag moved it to 10.0 s, dragging off removed it, and the prescribed Thunder and Tiny mew schedules are exact. See the source conflict above.
5. PASS: full 24-second runs at all three tempos ended at picture time 24 with the audio clock offset accounted for. The final 124-note strings run had maximum calculated note/picture scheduling error of 3.56e-15 seconds. This measures the common clock, not speaker output latency.
6. PASS: Play hushes narration. Swap-name speech began after completion. No logged speech began during the cartoon. Read stops playback first.
7. PASS: Motion off uses a 300 ms gray tint, preserves timed poses and freezes ambient grain and rain motion. The audit found no infinite animations.
8. PASS: score and both writing responses survived reload. Clear score emptied cues, effects and both responses in state and localStorage. Saving is disclosed on screen and guarded against storage failure.
9. PASS: the two-second edit run spoke effectsHow once. The full audit's five-held-click runs were clean. The repaired same-mode double tap retained one uncut welcome.

#### Wave lessons

- PASS, Hint and voice: immediate owned hints, Curio.voice, valid checks and V.heard; Read returned the restored writing-close hint. First actions proceed immediately.
- PASS, Focus and layout: controls update in place; deliberate focus uses preventScroll. No focus on load. Native field focus rings sit inside the field and labels remain readable.
- PASS, Sizes: all required sizes, the iframe phone host, 44 px controls and the unclipped main hint checked. Repaired Read measures 44 by 44 at 680 and 800.
- PASS, No giveaways: Class guess hides names, choices and pressed-state clues; all hidden switches are equally disabled until Show.
- PASS, Honest numbers: time is measured from the playback clock. There is no estimated success meter. Source estimate discrepancies are reported above.
- PASS, Standards: composing, comparing, intended mood, writing and silent-film accompaniment cover the listed standards through student actions; notes map them explicitly.
- PASS, Motion off: full story timing is retained; ambient motion freezes and the flash becomes gray.
- PASS, Short choice sets: music shapers and the ten-effect shelf fit their panels. The phone timeline intentionally scrolls at the spec's 30 px/s; scene keys and playhead following support navigation.
- PASS, Resize mid-action: the full audit found no exceptions or controls left disabled.
- PASS, No late welcome: Play and Hear it three ways skip a first-tap welcome while the cartoon runs. Re-entering the current mode no longer hushes its welcome.
- PASS, Unknown as unknown: blank cues say Silent rather than implying a score exists. Secret scores stay unnamed until Show.
- PASS, One look, one meaning: Feel uses both words and patterns; effects use labeled green chips.
- PASS, Badge truth: the swap strip describes the active score and current scene. Secret mode removes that strip's information.
- PASS, Hints change back: mode changes, stopping, writing close and demo completion restore relevant actions; targeted Read logs confirm the writing-close hint.
- PASS, No answer by copying: secret-score guessing requires listening; no visible answer text or selected-state clue remains.

#### Audit leads

The full audit completed successfully with 64 leads: `_scratch/cartoon-soundtrack-mixer/audit/audit.md`. It was run once and was not rerun after repairs. Every lead category is disposed of here.

- Fixed: small Read targets at 680 and 800. Targeted geometry now measures 44 by 44.
- Fixed: all repeated ruler/block overlap leads. Removed the compact negative margin; targeted measured overlap is zero at both affected widths.
- Fixed test setup: score-shaped tried a hidden wide-screen preset at compact sizes, causing focus to fall to the page. Audit states now use the visible Feel menu and real arrow/Enter keys. The compact control was exercised successfully.
- Intentional: phone timeline controls outside the horizontal viewport. The spec requires a 720 px scrolling timeline. Stopped seeks now follow the playhead too; the 18 s phone check positioned it at x=188.
- Fixed explicit naming: both writing fields now have aria-labelledby, in addition to their native labels.
- Intentional: the modal writing card covers the movie, Play and background hint. Its own prompts and Save and return are visible.
- Fixed: same-mode quick taps cut welcome speech. A shared guard preserves the current mode and narration; the targeted blank-score double tap logged one spoken welcome with no cut.
- Expected first-tap behavior: Play silent and Hear it three ways suppress welcome speech while the movie plays. This follows STANDARDS and the spec's no-voice-over-cartoon rule.
- Clean audit rows: exceptions, one-click controls, five-click narration, Motion off and resizing. The Sound button intentionally hushes speech; mode transitions intentionally move controls.

Additional targeted repairs: stopped phone seeks, Space on focused buttons, live tempo phase continuity, Sound off/on clock transfer, current demo and writing-close hints, and an inset native-field focus ring. Final smoke: zero console errors, warnings or exceptions. No automatic remote resource references; the recorded tool resource list was empty.

#### Frames looked at

Reviewed 64 manual PNG frames across bar-frames, early-frames, size-frames, student-frames, target-frames, final-frames, last-frames, preaudit-frames, compact-frames, repair-frames, close-frames and smoke-frames. This covers every required size, modes, gray rendering, Motion off, keyboard input, real drags, writing, secret guesses and dense effects.

Reviewed all 55 audit PNGs on seven contact sheets, plus the affected layouts at full size in targeted frames. Also inspected generated images, keyed artwork, the art contact sheet and the side-by-side bar comparison. All evidence is in `_scratch/cartoon-soundtrack-mixer/`.

#### Art made

Sixteen finished images, 688.2 KiB total. One kitten image was redrawn, for 17 generation calls. Final bundle: 1,044,977 bytes, 1020.5 KiB, below 2 MB. Backgrounds are 1600 px wide; cutouts are sized for their display roles. The kitten key was despilled and inspected.

Built-in OpenAI image generation was used. Full project prompt set: `art/prompts.json`; originals: `art/raw/`; finished assets: `art/*.webp`. Only the free `art.py --rekey <name>` form was used. No people, downloads or recorded audio.

#### Art still to paint

None. All named assets are generated, keyed, inspected and placed.

#### Engine changes wanted

As detailed in handoff.md: move local tuba and strings into `kit/music-studio.js` INSTR; add public absolute start, phase, gain and live-update options to play, including an 80 ms stop fade; document these in `docs/families/music-studio.md`. Local extensions and event offsets currently supply the behavior without modifying shared files.

#### Left open

- Human headphone review of synthesized timbres, transitions and effects. Chrome was muted for every run.
- Upbeat-guide/Zephyr recordings are prepared in the manifest but not recorded, per the build instructions. Browser speech is the fallback.
- Three or more concurrent effects can overlap visually in the two-lane track. Short previews also give the film limited height with two occupied lanes.
- Literal Done when 4 timing conflict for Funny, as documented above.
- The full audit reflects the pre-repair bundle; targeted checks cover the final repairs. A cold review remains appropriate.

Final cleanup verified: host.html absent, no listening test ports, and no Chrome processes belonging to this tool. Build only work is complete.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: cartoon-soundtrack-mixer

#### Played
Cold Grade 4 solo run before reading builder notes: full silent film, three-way demo, four shaped cues, effects, complete score, live swaps, Class guess/Show and writing; also checked the projected-class flow. The theater and expressive cat are strong. Stopped music edits were the flattest action.
Checked all five catalog standards against composing, personal mood, comparison, written reasons and the silent-film accompaniment activity. Notes retain the required three opening sections and practical home activities.

#### Findings fixed
- **Should fix, general, Score it/effects:** dense chips covered one another. Two-lane labels now stay separate with 44 px grab areas; exact onset pins and duration strokes retain the time scale. Labels show start and length. Checked every required size and 16 real drags at 680, 1366 and 375.
- **Should fix, general, effect boundaries:** moving near 24 s permanently shortened sounds, and last-slot collisions could share an onset. Preserve intended length, clip only playback/display, and search for a free quarter-second slot. Rain restores its three-second length after moving back; all 16 boundary onsets are distinct.
- **Should fix, general, effect editing:** drag-release hints retained the old time and Remove could be hidden. Placement, movement and chip dragging open Effects; release names the current time; canceled drags restore the start. Stopped phone selections scroll into view. Final real drag and phone frames confirm this.
- **Should fix, general, Box scene:** the painted background box competed with a different animated box. Repainted the porch without its baked-in box and redrew kitten-peek against the empty box reference. One box now persists through the reveal and pickup.
- **Should fix, general, Home scene:** a flat rectangle covered a cat walking below the cat door. The approach now changes perspective toward the painted opening and clips at its jamb.
- **Should fix, general, voice and hints:** Read during playback named Stop after stopping; later swaps could leave old score-name speech queued or speaking. Read now names a stopped action, new swaps drop stale results, and queued results validate the announced score. Read remains protected. Stop hints name controls in the current mode.
- **Should fix, general, phone privacy:** the saving notice was hidden. It now has a visible footer line; final 375 px checks show it inside the viewport with zero page scrolling.
- **Should fix, general, writing:** the focus ring touched the prompt at 680x425. Textarea focus is now inset; the repaired frame is clear.
- **Polish, general, cue shaping:** replaced the identical beep with a two-note audition using the selected melody, tempo, loudness, instrument and style. Play, Read, mode changes and Sound changes stop the audition.
- **Polish, general, payoff:** completed scores name the student's mood, shaped scenes and effects, with correct singular/plural words. The three-way demo ends on the storm rather than the next scene.

#### Findings left
- **Polish, general, dense compact preview:** two 44 px effect lanes leave limited film height at 680x425 and on a phone. Transport and editing remain reachable without page scrolling. Larger classroom views present the cartoon much better.
- No other confirmed blocker or should-fix remains. Perceptual audio review and the spec conflicts below remain unverified or unresolved, rather than being called passes.

#### Flattest moment left
The short preview with both effect lanes occupied. Live mood changes and the kitten ending remain the strongest moments; the painted theater, full art set and musical choices were preserved.

#### Graphics
Inspected all 16 assets and rendered scenes, plus Beat Lab and Snowy Mail Route frames. Repainted `art/bg-porch.webp` and `art/kitten-peek.webp` using built-in image generation, retained selected originals in `art/raw/`, and processed with `art.py --rekey`. Prompts and provenance are in `art/prompts.json`. No people are present; the spec explicitly calls for an empty piano bench and an animal story. Art: 693.0 KiB. Final offline bundle: 1032.8 KiB.

#### Audit
Ran `audit_tool.py` once, last, with a 2400-second limit, Chrome 9931 and host 8735. It finished with 10 leads. Read `_scratch/cartoon-soundtrack-mixer/review-audit/audit.md`; all 61 audit PNGs were inspected, with relevant writing and secret-guess frames also opened at full size.
- Four phone timeline leads are the spec's required 720 px scrolling timeline, rather than sideways page overflow. Final selected-effect checks also keep the selected chip visible.
- Three writing keep-region leads are deliberate modal coverage. Keep regions are now scoped to each state's visible work rather than requiring the stage behind the dialog.
- Two skipped welcomes are Play silent and Hear it three ways, as required by the no-narration-over-cartoon rule.
- The quick Start scoring tap cuts its welcome because the second tap hits Chase and shapes the first cue. A targeted real double tap confirmed that state change, which makes the introductory guidance stale.
- Held controls, repeat clicks, Motion off and resize checks reported no errors, lost focus, repeated how-to lines or controls left disabled.
- The initial dense-effects fixture failed to return its drag points, so its audit pictures were empty. Corrected the manifest and verified the density case separately with 16 real drags at each of 680, 1366 and 375. Do not count that initial audit state as dense coverage.
- Final hint, focus, privacy, duration-label and count repairs were checked only in affected frames after the audit; the full audit was not rerun. Final targeted runs report zero tool errors. Earlier helper-host favicon 404s were outside the bundled tool.

| Voice check | Kind | Expected | Spoken |
|---|---|---:|---:|
| Effects guidance, five requests | how | 1 | 1 |
| Show result, five random rounds | event | 5 | 5 |

Three complete 24-second clock runs at 66, 104 and 152 beats/minute finished at 24. Incoming live-edit/swap notes were scheduled immediately, and the picture clock did not restart. A real effect drag landed at 8.25 s. Sound off/on preserved monotonic time. Writing and clearing survived fresh loads; keyboard, grayscale, reduced motion, blank scores, full effect capacity and all required sizes were checked. Fixed narration matches all ten manifest lines; resource inspection found no external tool requests.

#### Left open
- Every Chrome was muted. Synthesized timbre quality, perceptual transitions and physical speaker/display latency were not listened to or measured. No audio was recorded, as required; browser narration remains the fallback for the prepared upbeat-guide/Zephyr manifest.
- Spec conflict: Funny explicitly uses Boing at 7.2 s while Done when 4 generalizes about 7.0 s. Preserved Content: Scary/Sad Thunder is at 7.0 s and all Tiny mews are at 16.0 s.
- Recomputed 24 s, 96 quarter-second slots, 30 px/s phone scale, loop lengths and all nine AA contrast pairs. The spec's 680 px estimate of 27 px/s disagrees with its 62 percent formula, which gives 17.57; the named art list totals 16 rather than 15. Spec was not edited.
- Shared-engine additions remain requested in handoff.md. Tuba, strings and timing workarounds stay tool-local; no kit file changed.
- No git commits. All review writes stayed in the tool and its scratch folder; temporary host.html is absent and no assigned test port remains listening.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Cartoon Soundtrack Mixer handoff

#### Built structure
`src.html` extends the kit starter. CSS lays out a theater, canvas picture, timeline and tabbed control desk. All images use art tokens and all sound is synthesized locally. Three modes share one fixed cartoon. The Music, Effects and Story panels update persistent controls in place. A narrow timeline is 720 px wide and follows the playhead.

The script contains original cue presets and ready-made scores, local instrument extensions, shared-clock playback, the cartoon renderer, persistent cue controls, effect placement and dragging, Mood Swap, and device-only saving. `window.__tool` exposes state and telemetry for cold review.

#### Timing details
The picture reads the audio context clock when music plays, or the page clock for silent playback. `MS.play` starts each scene's events with `exclusive:false`. It has an 80 ms start offset. Live edits restart only the edited scene at the current phase, with the previous layer fading out. Mood Swap keeps the picture clock and restarts incoming cues at its current phase. Music gates and per-cue loudness wrap the shared voices. Effects schedule against the same context clock.

An event offset compensates for the engine's start delay on live swaps. Runtime beat anchors preserve the melody's beat when Tempo changes. Sound off transfers the picture to the page clock and Sound on transfers back without jumping. Music routes through the engine's dry and room buses. Effects use the same audio context.

#### Engine changes wanted
- `kit/music-studio.js`, `INSTR`: move the tool's `tuba` and `strings` definitions into the shared table, with the current signatures. Tuba is sawtooth an octave down through a 700 Hz lowpass; strings are two detuned sawtooths through an 1800 Hz lowpass with 120 ms attack.
- `kit/music-studio.js`, `play`: expose a scheduled absolute start time, initial phase/offset, per-player gain and an 80 ms stop fade. Expose a live event/instrument update that cancels the already scheduled horizon. The current engine requires a local restart to meet the spec's immediate edit and swap behavior.
- `docs/families/music-studio.md`: document those additions together with the engine implementation. No shared files were changed in this build.

#### Spec decisions and reconciliation
- Open questions: the spec lists none.
- The art list counts 16 named assets, although its total says 15. All 16 were generated and used.
- The ready-made Funny score uses Boing at 7.2 s, matching the puffed-fur pose. Scary and Sad use Thunder at the 7.0 s flash. All three use Tiny mew at 16.0 s. Content timing was followed; Done when 4's general flash wording conflicts with Funny's explicit score.
- Compact views show the six presets in a native Preset menu so all five musical shapers remain available. Full-size views show all six preset chips.
- On a short landscape preview, the transport sits over the bottom of the movie frame to give the picture more height.
- The required source calculations are in `_scratch/cartoon-soundtrack-mixer/numbers.txt`. Contrast and two-bar timing match the spec. A 375 px full width divided by 24 seconds is 15.625 px/s before margins; the supplied approximate 14 px/s is a layout estimate. The implemented narrow timeline uses the required 30 px/s.
- The stated 680 px estimate of 27 px/s is also inconsistent with a 62 percent width: that formula gives 17.5667 px/s. The 1366 and 1920 estimates agree with the formula after rounding. Actual timeline width follows the responsive layout.
- Fixed narration is prepared in `voice/lines.json` for upbeat-guide/Zephyr. No audio was recorded, per build instructions; browser speech is the current fallback.

#### Cold-review focus
Listen to the four timbres on headphones, including live changes and mood swaps. Perceptual listening remains open because Chrome checks are muted. Cold-review repairs below address the box layering, doorway, dense chips and stale hints. The movie remains small in the short preview when both effect lanes are full. No git commit was made.

#### Cold review changes, 2026-11-04
The first student play preceded reading the builder's report. The porch plate was repainted without its baked-in box, and kitten-peek was redrawn against the empty box reference. One animated box now persists into the carry scene, and the cat approaches the real small doorway in perspective with clipping at its jamb rather than a flat covering rectangle. Full prompts and the built-in image generation provenance are in art/prompts.json; selected raw assets and finished WebP assets stay in art/.

Crowded effects now spread their reachable labels into two lanes. Exact onset pins and duration strokes remain on the timeline, and crowded labels print their onset. Sparse effects retain proportional chips. The packing calculation uses the actual timeline width on resize. Effect duration is retained when moving near the ending; playback and the displayed duration clip at 24 seconds. Same-time collisions at the right boundary search left for a free quarter-second slot. Selecting a chip updates the hint with its time and length.

Stopped cue edits audition two notes through MS.play with the chosen timbre, loudness, tempo and style, replacing the generic beep. Read, mode changes, Play and Sound changes stop that audition. Read during playback changes the hint to a valid stopped action before reading. The completed score's film label names the student's intended mood, shaped scenes and effect count. The three-way demo now ends on the storm's final frame. Dense short previews still have limited film height because the timeline retains two 44 px effect lanes.

Targeted checks after the single audit repair drag-release hints and canceled drags, open the effect panel when a chip drag starts, and keep stopped phone selections visible. Phone saving disclosure stays visible in its own footer line. Textarea focus is inset so it does not cover the writing prompt. A newer swap drops a queued score-name result and stops a score-name line in progress; Read remains protected. The dense-effects audit fixture now explicitly returns its drag points and resets the narrow scroll viewport before each drag. Its initial audit screenshots were empty; use the separate real-input dense checks for that case.

#### Verification and audit
The full audit completed with 64 leads. Repeated 680/800 ruler overlaps and the 42 px Read target were fixed, as were same-mode double taps cutting a welcome. Writing fields now have explicit aria-labelledby. The compact score-shaped audit state now uses the visible Feel menu rather than a hidden wide-screen preset chip. Modal coverage of the movie is intentional. The 375 px scrolling timeline is required by the spec and its playhead now follows stopped seeks as well as playback.

The full audit was not rerun after those repairs. Targeted held-click, keyboard, geometry, voice, sound-clock and frame checks passed. Evidence is under `_scratch/cartoon-soundtrack-mixer/`, especially `audit/audit.md`, `repair-frames/`, `close-frames/`, `timing-*.json`, `final-clock.json` and `feel-compare.png`. All Chrome runs were muted, so perceptual headphone review remains open. The final report gives the dispositions.

#### Cold review verification complete
The one full review audit finished with 10 leads and no resize exceptions or controls left disabled. Dispositions and limitations are in codex-review.md. The dense fixture was repaired after its initial empty audit frames; separate real-input runs placed all 16 effects at distinct quarter-second times at 680, 1366 and 375 with no overlapping or undersized chips. Crowded labels now show onset and length. Final affected-frame checks cover stale speech, protected Read, drag time hints, phone disclosure/selection, inset writing focus, demo ending and singular/plural payoff counts. No second full audit was run. Test browsers and hosts were closed and host.html removed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
