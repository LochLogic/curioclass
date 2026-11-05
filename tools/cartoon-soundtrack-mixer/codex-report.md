# Codex report: cartoon-soundtrack-mixer

## Built

Built Theater, Score it and Mood Swap around the original 24-second Whiskers and the Storm cartoon. Four music cues have five live shapers, six presets, ten synthesized effects, quarter-second placement, dragging, scrubbing, scene playback, secret class guesses and device-only writing and saving.

The self-contained bundle is `cartoon-soundtrack-mixer.html`. Source is 1,391 readable lines, maximum 159 characters. The draft manifest is stage built. Teacher notes, ten-line voice manifest, audit states, prompts and handoff are present. No git commits, publishing or polish round. Shared kit files were not changed.

## Numbers check

- Python evidence: `_scratch/cartoon-soundtrack-mixer/numbers.txt` and `source_checks.py`.
- Four scenes times six seconds equals 24 seconds. Quarter-second snapping gives 96 divisions. Narrow timeline: 720 pixels divided by 24 seconds equals 30 pixels per second.
- Two bars at 66, 104 and 152 beats per minute last 7.272727, 4.615385 and 3.157895 seconds. Six seconds is 82.5 percent of the slow loop.
- The source's approximate 680 px estimate of 27 px/s disagrees with its 62 percent formula, which gives 17.5667. The 1366 and 1920 estimates round correctly from 35.2883 and 49.6. A full 375 px divided by 24 gives 15.625 before margins. Actual layout is responsive; the narrow scrolling scale is exact.
- Recomputed supplied contrast pairs: 10.1886, 15.0072, 7.7623, 12.6210, 8.5686, 12.6467, 8.9632, 8.6970 and 11.3947 to one. They meet AA for text.
- The art list names 16 assets, although its total says 15. All 16 are made and used.
- Content explicitly puts Funny's Boing at 7.2 s, matching the puff, while Done when 4 generalizes about the 7.0 s flash. The explicit score timing was retained. Scary and Sad have Thunder at 7.0 s; all three have Tiny mew at 16.0 s.

## Feel check

Walked the student flow through the silent film, shaping cues, effects placement, full playback, live swaps and saved writing. All Chrome checks were muted as required, so this is visual and scheduling evidence, not a human headphone listening verdict.

Best moment: the storm keeps moving through a score swap, followed by the tiny kitten reveal and the warm curled-up ending. The gray kitten was redrawn smaller to match the carried and sleeping kitten.

Two flattest moments and changes:
- The short preview squeezed the film and hid presets. Packed its header, moved transport over the frame, used a compact Preset menu and kept the shapers visible.
- The completed three-way demo pointed back to the same demo. It now points to Start scoring; closing the writing card also restores a useful next action.

Bundled and opened scratch copies of Snowy Mail Route and Beat Lab without writing to their folders. Compared the tool with Beat Lab in `_scratch/cartoon-soundtrack-mixer/feel-compare.png`. The theater and cartoon have substantial painted detail. The film remains small in a short preview with both effects lanes occupied.

## Done when

1. PASS: movie frame, transport and timeline stay in the viewport at 1366x768, 680x425 and the 375 px host. All STANDARDS sizes were checked. Dense two-lane compact use has the limitation below.
2. PASS for scheduled behavior: switches preserve the picture clock. Recorded switch handling advanced it by zero to eight milliseconds, with incoming notes scheduled at the current position. Perceptual listening remains open.
3. PASS for scheduled behavior: live tempo, instrument and loudness edits replace the active cue immediately. Beat anchors preserve musical phase across tempo changes. `repair-frames/tempo-phase.png` and `tempo-phase.json` show the live edit.
4. FAIL against the literal all-score flash wording: Funny's explicit Boing is 7.2 s, rather than 7.0 s. Placement and synchronization checks passed: real drag placed Boing at 7.25 s, a second drag moved it to 10.0 s, dragging off removed it, and the prescribed Thunder and Tiny mew schedules are exact. See the source conflict above.
5. PASS: full 24-second runs at all three tempos ended at picture time 24 with the audio clock offset accounted for. The final 124-note strings run had maximum calculated note/picture scheduling error of 3.56e-15 seconds. This measures the common clock, not speaker output latency.
6. PASS: Play hushes narration. Swap-name speech began after completion. No logged speech began during the cartoon. Read stops playback first.
7. PASS: Motion off uses a 300 ms gray tint, preserves timed poses and freezes ambient grain and rain motion. The audit found no infinite animations.
8. PASS: score and both writing responses survived reload. Clear score emptied cues, effects and both responses in state and localStorage. Saving is disclosed on screen and guarded against storage failure.
9. PASS: the two-second edit run spoke effectsHow once. The full audit's five-held-click runs were clean. The repaired same-mode double tap retained one uncut welcome.

## Wave lessons

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

## Audit leads

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

## Frames looked at

Reviewed 64 manual PNG frames across bar-frames, early-frames, size-frames, student-frames, target-frames, final-frames, last-frames, preaudit-frames, compact-frames, repair-frames, close-frames and smoke-frames. This covers every required size, modes, gray rendering, Motion off, keyboard input, real drags, writing, secret guesses and dense effects.

Reviewed all 55 audit PNGs on seven contact sheets, plus the affected layouts at full size in targeted frames. Also inspected generated images, keyed artwork, the art contact sheet and the side-by-side bar comparison. All evidence is in `_scratch/cartoon-soundtrack-mixer/`.

## Art made

Sixteen finished images, 688.2 KiB total. One kitten image was redrawn, for 17 generation calls. Final bundle: 1,044,977 bytes, 1020.5 KiB, below 2 MB. Backgrounds are 1600 px wide; cutouts are sized for their display roles. The kitten key was despilled and inspected.

Built-in OpenAI image generation was used. Full project prompt set: `art/prompts.json`; originals: `art/raw/`; finished assets: `art/*.webp`. Only the free `art.py --rekey <name>` form was used. No people, downloads or recorded audio.

## Art still to paint

None. All named assets are generated, keyed, inspected and placed.

## Engine changes wanted

As detailed in handoff.md: move local tuba and strings into `kit/music-studio.js` INSTR; add public absolute start, phase, gain and live-update options to play, including an 80 ms stop fade; document these in `docs/families/music-studio.md`. Local extensions and event offsets currently supply the behavior without modifying shared files.

## Left open

- Human headphone review of synthesized timbres, transitions and effects. Chrome was muted for every run.
- Upbeat-guide/Zephyr recordings are prepared in the manifest but not recorded, per the build instructions. Browser speech is the fallback.
- Three or more concurrent effects can overlap visually in the two-lane track. Short previews also give the film limited height with two occupied lanes.
- Literal Done when 4 timing conflict for Funny, as documented above.
- The full audit reflects the pre-repair bundle; targeted checks cover the final repairs. A cold review remains appropriate.

Final cleanup verified: host.html absent, no listening test ports, and no Chrome processes belonging to this tool. Build only work is complete.
