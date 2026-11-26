# Name Song Practice: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: name-song-practice

#### Built
Built Make, Practice and Perform as a self-contained offline K-2 teacher-led tool. Name rhythm, three contours, eight favorites, two takes, optional microphone, five fixes, comparison and four feeling accompaniments are implemented. No commits, branch operations, deployment or separate polish round.

Source: tools/name-song-practice/src.html. Final bundle: tools/name-song-practice/name-song-practice.html. Teacher notes, draft metadata, voice manifest, audit states, handoff and all 17 painted assets are present. No host.html remains.

#### Numbers check
PASS. Scratch setup.py recomputed G4 = 391.99544 Hz and E4 = 329.62756 Hz. All four syllable patterns total two beats; all 96 combinations have four four-beat bars, including two final rest beats. Browser checks of the actual note generator found zero bad combinations.

Song / song with count-in: 76 bpm 12.6316 / 15.7895 s; 96 bpm 10 / 12.5 s; 108 bpm 8.8889 / 11.1111 s; 120 bpm 8 / 10 s. Only Practice records, capped at 15 s. No discrepancy with the spec's rounded figures.

Contrast: white/brand 6.3193:1; brand/paper 6.0287:1; ink/paper 14.8887:1; muted/paper 6.2670:1; ink/sol 7.2356:1; ink/mi 9.2061:1. All match the listed rounded ratios.

#### Feel check
Played the complete student path through Make, both practice takes, comparison and repeated performances with real held input. Best moment: the plush audience swaps from listening to cheering and offers its cycling comment after the class's chosen take.

Flattest moment 1: the early Make screen felt like an isolated worksheet. Added the painted classroom context, textured favorite pictures, layered paper and immediate clap feedback.

Flattest moment 2: cramped compact lyrics and a shallow audience weakened the payoff. Moved lyrics to a shared baseline, gave long words more space, used a right-side Practice panel and moved compact feeling controls into the top row. Final compact audience is 128 px tall versus a 108 px song strip, with all controls at least 60 px.

Compared one frame beside Snowy Mail Route in _scratch/name-song-practice/feel-comparison.png. Also bundled and opened Beat Lab from Scratch. The plush stage has comparable visual care; a real class's singing and physical classroom acoustics were not assessed by muted automation.

#### Done when
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

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
All 57 original audit PNGs, directly or in the labelled four-frame boards in Scratch. Also all initial, fit, full-size, extreme, repair and QA frames: every mode, all required sizes, one/four claps, four feelings, take comparison, confirmation, grayscale, keyboard and Motion off. Reference frames from Snowy Mail Route and Beat Lab were opened. Final changed-state frames are in final-frames and qa-frames.

#### Art made
17 illustrations: one classroom theater backdrop, eight plush listening/cheering poses and eight favorite cards. Final art 522.1 KB; final bundle 976.7 KB, below 2 MB. Built-in OpenAI image generation; saved originals in tools/name-song-practice/art/raw/ and finished WebP files in art/. Full prompts and provenance: art/prompts.json. One failed request batch was retried successfully; no required image is missing. Rekeyed with despill and resized the backdrop. No selected image needed a content redraw.

#### Art still to paint
None. No people generated. Narration recordings were not created, as instructed; voice/lines.json contains the 48 fixed lines for big-sister/Leda and the tool uses browser speech fallback.

#### Engine changes wanted
None required. No kit or other tool files changed. The tool uses Curio.voice, Curio.audio and the kit settings; the spec names no family engine.

#### Left open
The full audit was not repeated after the documented build repairs. The original audit walked Make controls and covered Practice/Perform through six explicit states; its header-only mode discovery missed the old toolbar. The final semantic header is detected as three modes, and independent held-input flows exercise the other modes. Four-clap Clear words lyrics are still tightly spaced in the 680-pixel preview, though no note block covers them. Use full screen for classroom reading.

Physical microphone calibration and a live class listening session remain for classroom review. Fake microphone input exercised actual browser recording and playback. Browser fallback narration does not establish Leda's recorded delivery. Note spacing favors readable lyrics; precise rhythm lives in the audio/event model and note-duration titles.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: name-song-practice

#### Played
Cold Grade 1 play preceded the builder report, handoff, notes and source: Make, Hear it, both takes, thumbs, one fix, comparison and Silly performance. Also exercised the projecting-teacher path and a keyboard-only solo path. The cheering plush audience is the strongest moment.

Independently checked all 96 combinations, G4/E4, rhythm totals, tempos and contrast ratios against the spec. The actual note generator agrees. Notes retain the required first three sections and practical home activities. All four standards have student actions.

#### Findings fixed
- **Should fix, general, compact Practice:** four-clap Clear words lyrics collided. Kept the strip full width, moved mic/reset beside the lower controls, weighted spacing toward words and widened the last phrase. Compact/phone words grow from 11 to 16.5 px; full-screen enlargement remains 18 to 27 px.
- **Should fix, general, Perform:** changing feeling left a held syllable and its ball on the old tempo. Retimed its remaining sound and event at the next beat. The Happy-to-Sleepy test now ends at the computed 5.84947 s instead of 5.61556 s.
- **Should fix, general, song-change dialog:** confirmation narration could outlive Keep my song, Yes, change it or Escape. Hush on dialog entry/exit, preserving focus without scrolling. Final Escape check cuts the old line and restores the current hint.
- **Should fix, general, audit layout leads:** moved the compact fix badge above the last bar heading and tightened phone lyric line boxes so enlarged words cannot reach the next row headings. Removed excess span width behind two large-screen word-box warnings without moving their text. The responsive badge keeps the fix concise; the chosen comparison card stays selected.
- **Polish, general, flattest moment, Compare:** bare take buttons did not connect reflection to the chosen fix. Added First try and the actual take-2 cue, retained the chosen take on the full-size badge, and made the comparison hint ask students to listen/think about their fix. Updated the matching voice manifest.
- **Polish, general, Make art:** redrew the soccer card with clearer sewn panels, warm paper texture and a rounded silhouette. Preserved the other 16 paintings and the toy-stage payoff.

#### Findings left
- **Polish, narration:** browser fallback remains. CODEX-BUILD.md prohibits recording audio; the matching 48-line big-sister manifest is ready for recordings.
- **Nit, graphics:** faint violet fringing remains on parts of the lamb cutout at the largest view. It is subtle at laptop size; left without another art pass.
- No blocker or should-fix remains from this review's findings.

#### Flattest moment left
With the microphone off, comparison depends on remembering the class's live singing. The cue now focuses that reflection; optional in-page recording supplies actual playback.

#### Graphics
All 17 finished images checked in the scenes and on the Scratch contact sheet. Soccer redrawn with built-in OpenAI image generation, then art.py --rekey soccer. Full prompt, house style and provenance remain in art/prompts.json; raw selection is art/raw/soccer.png. No people or missing art tokens. Cozy stage, eight plush poses and all eight favorites retained. Art: 521.2 KB. Final bundle: 978.2 KB (1,001,708 bytes). Opened both bar tools for comparison; the scene retains its richness.

#### Audit
Completed once within the 40-minute cap, exit 0. Evidence: _scratch/name-song-practice/review-audit/audit.md. Opened all 81 audit PNGs directly or on labelled boards.

31 leads answered:
- 14 duplicated reports describe the compact badge and phone lyric/header overlaps in Clear words and Compare. Fixed and re-shot.
- Two large-screen warnings concerned overlapping transparent word boxes; the visible words were separated. Tightened the boxes and re-shot.
- 15 welcome warnings accepted under STANDARDS: the two incomplete mode entries send the class back to Make; Clap, Clear claps, all three shape controls and all eight favorites supply their own current line, so the welcome skips. No late welcome was added.

Opening screens were clean at all eight sizes. Resize stress completed without exceptions or stuck controls. Control/focus checks, Motion off, repeated held clicks and quick taps were clean apart from the explained welcome leads.

After the scoped fixes, eight targeted frames in _scratch/name-song-practice/final-targeted/ show no collisions, controls under 60 px, controls below the fold, or console errors. Phone clear/compare/perform, compact clear/compare, large-screen words, wide comparison and dialog Escape were inspected. The full audit was not repeated, as instructed.

Voice check at a two-second held-tap pace, allowing the final queue to settle:

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| Louder! Big voices. | event | 5 | 5 |
| Tap Sing take 2, and try your fix. | how | 1 | 1 |

Read works with Sound off and releases promptly on a mode change. The 48 manifest lines match allLines(). Keyboard-only input reaches Listen with focus intact; grayscale and Motion off retain readable cues and timing. No external asset URLs or song/audio storage were introduced. Wave checks covered immediate hints, stable controls, visible short choice sets, truthful cues, incomplete states, resize, motion and voice; this creative rehearsal has no hidden-answer quiz to give away.

#### Left open
No classroom acoustic calibration or live class trial is claimed. Microphone success used a synthetic MediaStream with the real MediaRecorder; denial and missing-device paths were simulated. Two takes replayed. Reset and confirmed song edits erased them; leaving Practice released the stream while retaining the takes for comparison. No song/audio is saved between visits.

The spec's microphone policy question is unchanged. No new modes/topics, commits or shared-kit changes. Repository edits stayed in tools/name-song-practice/ and _scratch/name-song-practice/. Test Chrome/server processes are closed and host.html is removed. One review pass, with the required final audit and only scoped repairs afterward.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Name Song Practice handoff

Built and cold-reviewed in one review pass. No git commit or deployment.

#### Implementation
src.html starts from the kit starter. Local responsive CSS and semantic controls precede the tool logic. The logic contains the song generator, stable-control renderer, practice state machine, local synthesizer, audio-clock scheduler, memory-only recorder and microphone lifecycle.

Curio.voice owns narration and Read; Curio.audio provides the shared audio context. Music uses a 25 ms lookahead with a 75 ms horizon. The ball and count-in read AudioContext.currentTime. Feeling changes invalidate a future scheduled beat and rebuild it. Resize changes only CSS geometry, so notes are measured again without resetting playback.

The four bars stay across on landscape previews and use a two-by-two arrangement on phones. Notes use readable visual spacing, with extra room for longer favorite words; exact durations are in the event model and note titles. Lyrics share a baseline below both staff lines. Multiple name syllables use neutral dots because names are never typed or stored. The second take's chosen fix is reused in Perform when Take 2 or Both good is selected.

Compact Practice keeps a full-width song strip, with microphone/reset controls beside the lower action row and privacy text below it. Compact Perform places the four feelings in the top control row to preserve audience height. The song-control toolbar is a semantic header so the audit's mode discovery can find it. Microphone input releases when leaving Practice, with existing take blobs retained for comparison.

All 17 painted assets are in art/ with generated originals in art/raw/. Prompts and provenance are in art/prompts.json. Generated using the built-in OpenAI image tool, then processed only with art.py --rekey. No people were generated.

#### Open question decisions
- Microphone: retained, off by default, following the option developed throughout the spec. Permission is requested on the explicit toggle. At most two audio blobs stay only in page memory. Thumbs remains the full alternative.

#### Engine changes wanted
None required. No kit files were changed. A future shared music scheduler could extract the local lookahead and source-cancellation routines, but this spec has no family engine.

#### Remaining classroom check
Listen to the four accompaniments and browser narration on an actual classroom device. The loudness display is illustrative and is labelled as such. Plush comments cycle as scripted encouragement and do not analyze the class. The manifest names big-sister/Leda, but this build did not record narration, as instructed.

Evidence, bounded command runner, reference bundles, frames and mechanical audit output are in _scratch/name-song-practice/. The final report records tested results and remaining limits.

#### Cold review repairs
Cold play preceded this handoff and the source. Compact Clear words lyrics had collisions; the strip now uses the full width, with space weighted toward actual words and a wider last phrase. Compact and phone words enlarge from 11 to 16.5 px. Take comparison shows the actual take-2 fix, and the selected take remains on the cue badge.

Feeling changes now retime a held syllable and its oscillator at the next beat, so the ball follows the changed tempo. Song-change confirmation speech is hushed on close or cancellation. The soccer card was redrawn with built-in OpenAI image generation and processed only with art.py --rekey soccer.

Review evidence and the single final audit are in _scratch/name-song-practice/. Browser voice fallback remains because narration recording is prohibited by the build brief. No classroom acoustic calibration is claimed.

The review audit completed once within the 40-minute cap: 81 frames, 31 leads. Fourteen duplicate layout leads were repaired by moving the compact badge and tightening phone lyric line boxes. Two large-screen span-box overlaps were removed without moving the words. Fifteen welcome warnings follow the required first-tap and incomplete-song guards. The eight final targeted frames report no collisions or invalid control geometry and no console errors. The full audit was not repeated after those scoped repairs.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
