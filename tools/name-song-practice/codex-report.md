# Codex report: name-song-practice

## Built
Built Make, Practice and Perform as a self-contained offline K-2 teacher-led tool. Name rhythm, three contours, eight favorites, two takes, optional microphone, five fixes, comparison and four feeling accompaniments are implemented. No commits, branch operations, deployment or separate polish round.

Source: tools/name-song-practice/src.html. Final bundle: tools/name-song-practice/name-song-practice.html. Teacher notes, draft metadata, voice manifest, audit states, handoff and all 17 painted assets are present. No host.html remains.

## Numbers check
PASS. Scratch setup.py recomputed G4 = 391.99544 Hz and E4 = 329.62756 Hz. All four syllable patterns total two beats; all 96 combinations have four four-beat bars, including two final rest beats. Browser checks of the actual note generator found zero bad combinations.

Song / song with count-in: 76 bpm 12.6316 / 15.7895 s; 96 bpm 10 / 12.5 s; 108 bpm 8.8889 / 11.1111 s; 120 bpm 8 / 10 s. Only Practice records, capped at 15 s. No discrepancy with the spec's rounded figures.

Contrast: white/brand 6.3193:1; brand/paper 6.0287:1; ink/paper 14.8887:1; muted/paper 6.2670:1; ink/sol 7.2356:1; ink/mi 9.2061:1. All match the listed rounded ratios.

## Feel check
Played the complete student path through Make, both practice takes, comparison and repeated performances with real held input. Best moment: the plush audience swaps from listening to cheering and offers its cycling comment after the class's chosen take.

Flattest moment 1: the early Make screen felt like an isolated worksheet. Added the painted classroom context, textured favorite pictures, layered paper and immediate clap feedback.

Flattest moment 2: cramped compact lyrics and a shallow audience weakened the payoff. Moved lyrics to a shared baseline, gave long words more space, used a right-side Practice panel and moved compact feeling controls into the top row. Final compact audience is 128 px tall versus a 108 px song strip, with all controls at least 60 px.

Compared one frame beside Snowy Mail Route in _scratch/name-song-practice/feel-comparison.png. Also bundled and opened Beat Lab from Scratch. The plush stage has comparable visual care; a real class's singing and physical classroom acoustics were not assessed by muted automation.

## Done when
1. PASS: song strip is the broadest Make/Practice scene region at 1366x768 and 680x425; final narrow lyrics and audience inspected in targeted frames. Perform puts the toys above the smaller strip.
2. PASS: actual generator checked across all 96 combinations, zero rhythm or contour errors; audio-clock note events drive the ball.
3. PASS: full mic-off and allowed-mic flows; denied and missing microphone cases checked. Actual MediaRecorder produced two memory blobs and played both.
4. PASS: all five fixes inspected. Louder/Softer use 70/30 percent internal guide lines only with the mic; steady clicks and dot, raised/glowing sol and louder guide sol, and 18-to-27 px word enlargement implemented. RMS samples use the latest 50 ms.
5. PASS: Reset, confirmed song change and reload erase takes. No external network requests observed. No song or audio enters storage; the kit's shared Motion preference is the standing-rules exception.
6. PASS: Stop and mode switching act immediately; recording switching is immediate; a feeling change applied within the next beat in the play-through.
7. PASS: two consecutive performances cheered and produced different cycling comments; event narration repeats.
8. PASS within the exercised paths: how-to counts stayed at one across five fix actions; no narration queued during a sung take. Mechanical voice findings are answered below.
9. PASS: required sizes, 375 iframe, keyboard path and compact control geometry checked. The final compact Perform check found zero visible controls under 60 px or outside the viewport.
10. PASS: Motion off preserves the clock and jumps the ball without bounces. Calm animations checked, including the final idle glow.

## Wave lessons
- PASS, Hint and voice: hints update immediately, name the next control and feed Read; Curio.voice owns heard/how/event behavior. Incomplete-mode guards direct the class back to Make.
- PASS, Focus and layout: stable control elements; no focus on load; intentional focus uses preventScroll; fix selection and comparison keep keyboard focus usable.
- PASS, Sizes: all standing sizes covered, phone through a host; primary controls remain visible and meet 60 px targets.
- PASS, No giveaways: this is a creative rehearsal, with no hidden-answer quiz or score to reveal.
- PASS, Honest numbers: loudness says it is a picture, not a measurement. Audience notes are documented as scripted encouragement.
- PASS, Standards: making/refining, two takes and one fix, expressive performance, and personal name/favorite choices exercise all four listed standards.
- PASS, Motion off: no looping animation remains active in calm mode; time and audio are unchanged.
- PASS, Short choice sets: all eight favorites, five fixes, four feelings and three comparison choices stay visible.
- PASS, Resize mid-animation: real resize stress and a playing-clock check produced no exception or stuck playback.
- PASS, Welcome timing: no welcomeAfter; the kit decides after the first handler and validates current state.
- PASS, Unknown as unknown: unfilled name/favorite regions are dashed slots; no recording playback control claims a missing take exists.
- PASS, One look/one meaning: sol/mi have labels, distinct vertical positions, dots and color; selected chips have a pressed state.
- PASS, Badge truth: the displayed practice fix is the selected one, and the chosen take's cue carries into Perform.
- PASS, Hint reversibility: mode, step, stop, reset and readiness changes all call the current-state hint renderer.
- PASS, No copying-word answer: choices express a student's song and reflection; no correctness target is encoded in wording.

## Audit leads
Audit completed once with 15 welcome leads. All size/state checks were clean, Motion off had no infinite animation, resize stress had no exceptions or stuck controls, and five-click/quick-tap voice checks were clean.

1. #m-practice: accepted. On an incomplete song, its sing welcome would name a disabled control. The current line correctly sends the class to Make.
2. #m-perform: accepted. On an incomplete song, its performance welcome would name a disabled control. The current line correctly sends the class to Make.
3. #clap: accepted. The first clap makes the Make welcome stale; Now tap a favorite thing is the current how-to.
4. #clear: accepted. The tap supplies the current Clap instruction. STANDARDS requires the first-tap welcome to skip after the tap's own line.
5. #shape-0: accepted. The tap supplies the current missing-name instruction; the first-tap welcome skips as specified.
6. #shape-1: accepted. The tap supplies the current missing-name instruction; the first-tap welcome skips as specified.
7. #shape-2: accepted. The tap supplies the current missing-name instruction; the first-tap welcome skips as specified.
8. #thing-0: accepted. I like pizza and the missing-clap instruction belong to this tap; a delayed welcome is forbidden in this multi-mode tool.
9. #thing-1: accepted. I like puppies and the missing-clap instruction belong to this tap; a delayed welcome is forbidden.
10. #thing-2: accepted. I like rainbows and the missing-clap instruction belong to this tap; a delayed welcome is forbidden.
11. #thing-3: accepted. I like trains and the missing-clap instruction belong to this tap; a delayed welcome is forbidden.
12. #thing-4: accepted. I like dinosaurs and the missing-clap instruction belong to this tap; a delayed welcome is forbidden.
13. #thing-5: accepted. I like strawberries and the missing-clap instruction belong to this tap; a delayed welcome is forbidden.
14. #thing-6: accepted. I like soccer and the missing-clap instruction belong to this tap; a delayed welcome is forbidden.
15. #thing-7: accepted. I like butterflies and the missing-clap instruction belong to this tap; a delayed welcome is forbidden.

Coverage limit: the original toolbar was outside a semantic header, so the audit discovered zero mode groups. Its explicit six states still covered Practice and Perform at every size, but its per-control walk was the initial Make screen. The final source makes the toolbar a header; a targeted browser check detects all three modes. Independent full flows cover Practice/Perform, microphone cases, comparison, feelings and keyboard input. The full audit was not repeated after the documented build repairs.

Visual repairs beyond the mechanical leads: moved lyrics below both lines, gave longer words space, exposed the compact fix badge, enlarged the compact audience through control-row layout, and hardened microphone release and incomplete-mode narration guards. Targeted final frames cover the affected states. No separate polish round was started.

## Frames looked at
All 57 original audit PNGs, directly or in the labelled four-frame boards in Scratch. Also all initial, fit, full-size, extreme, repair and QA frames: every mode, all required sizes, one/four claps, four feelings, take comparison, confirmation, grayscale, keyboard and Motion off. Reference frames from Snowy Mail Route and Beat Lab were opened. Final changed-state frames are in final-frames and qa-frames.

## Art made
17 illustrations: one classroom theater backdrop, eight plush listening/cheering poses and eight favorite cards. Final art 522.1 KB; final bundle 976.7 KB, below 2 MB. Built-in OpenAI image generation; saved originals in tools/name-song-practice/art/raw/ and finished WebP files in art/. Full prompts and provenance: art/prompts.json. One failed request batch was retried successfully; no required image is missing. Rekeyed with despill and resized the backdrop. No selected image needed a content redraw.

## Art still to paint
None. No people generated. Narration recordings were not created, as instructed; voice/lines.json contains the 48 fixed lines for big-sister/Leda and the tool uses browser speech fallback.

## Engine changes wanted
None required. No kit or other tool files changed. The tool uses Curio.voice, Curio.audio and the kit settings; the spec names no family engine.

## Left open
The full audit was not repeated after the documented build repairs. The original audit walked Make controls and covered Practice/Perform through six explicit states; its header-only mode discovery missed the old toolbar. The final semantic header is detected as three modes, and independent held-input flows exercise the other modes. Four-clap Clear words lyrics are still tightly spaced in the 680-pixel preview, though no note block covers them. Use full screen for classroom reading.

Physical microphone calibration and a live class listening session remain for classroom review. Fake microphone input exercised actual browser recording and playback. Browser fallback narration does not establish Leda's recorded delivery. Note spacing favors readable lyrics; precise rhythm lives in the audio/event model and note-duration titles.
