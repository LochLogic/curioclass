# Codex report: voice-lab (Curiosity No. 03)

## Built

Built a full-window sound analyser, not a lesson sequence. The glass shows actual Web Audio spectra from microphone input,
original synthesized sounds or a tone generator. It has frequency and time rulers, RMS meter, YIN pitch and musical note,
LPC estimates, Hold with a movable cursor, temporary A/B spectrum outlines, harmonic markers and a reference vowel chart.

The lower-left corner carries the exact Curio Class Curiosities No. 03 plate and Manual drawer, beside its Motion, Sound and Read panel.
Two banks of eight pads expose all specified sounds plus silence. Sources, limitations and discoveries live in the Manual.
No painted images, external libraries, recordings, saved audio, network APIs, commits, publishing or polish round.

Deliverables: src.html, voice-lab.html, tool.draft.json, notes.md, voice/lines.json, audit-states.json, art/prompts.json and handoff.md.
The draft has curiosity=true, plate=3 and stage=built. The source and all test evidence stay inside the two authorized folders.

Bundle: **74,197 bytes**, 3.71% of the 2 MB goal and below the spec's 400 KB goal.
SHA-256: `a094ddfca6f5a3f666e9f6a687ec952516e7838296010fe7f23976065cacae23`.
All started Chrome instances used mute-audio. Ports 9980, 9981, 9982, 9983 and host 8785 were verified closed before this report.
There is no host.html in the tool folder.

## The real material

| Material or fact | Source and permission |
|---|---|
| Live sound, FFT, Blackman window, device sample rate | W3C Web Audio specification, https://www.w3.org/TR/webaudio/; W3C document licence, API used, prose not copied |
| Nine vowel reference triples and synthesis resonances | Peterson and Barney, JASA 24:175–184 (1952), https://doi.org/10.1121/1.1906875; factual numerical values only, no paper text, figures or recordings copied |
| Fundamental-frequency estimation | de Cheveigné and Kawahara, YIN (2002), https://doi.org/10.1121/1.1458024; original implementation of the algorithm |
| Formant estimates | Standard autocorrelation LPC, order 12, pre-emphasis and approximate 10 kHz downsampling; original implementation, visibly labelled estimates |
| Harmonic and instrument principles | Fletcher and Rossing, The Physics of Musical Instruments (1998); UNSW Music Acoustics clarinet research, https://phys.unsw.edu.au/music/clarinet/index.html; principles only, original illustrative recipes |
| Whisper and vowel explanation | Ladefoged and Johnson, A Course in Phonetics; reference only, no excerpts |
| Relative sss/shh frequency content | Jongman, Wayland and Wong (2000), JASA 108:1252; principle only, no excerpts |
| A4 and octave/note arithmetic | ISO 16:1975 reference-frequency fact; independently implemented equal temperament |
| Synthetic audio and presentation | Original code and synthesis MIT; original Manual CC BY 4.0 |

No external dataset, audio asset, font or image is loaded. Each reference and its permission status also appears in tool.draft.json and the Manual.
Synthetic pads are actual generated audio analysed by the same nodes, not prepainted spectral patterns.
The historical chart is descriptive, not a pronunciation target. It distinguishes men, women and children with shapes as well as colour.

## Break the instrument

- Seven real generator frequencies from 80 through 1,000 Hz passed the 1% requirement; worst error 0.211% in the final functional retry.
- Independently generated sine arrays at 44,100 and 48,000 samples/s passed all **94** cases from 80 through 1,000 Hz in 20 Hz steps.
  Worst relative error was **0.374%**. A4 at 440 Hz maps to A4 and zero cents in the independent note calculation.
- Fixed a 1,000 Hz boundary rejection and a high-tone subharmonic error. The 8,000 Hz tone now leaves PITCH blank while PEAK remains about 8,001 Hz.
- Both eight-pad banks ran, including noise, whispered vowel, chord and silence. Silence returned −60 dBFS and no pitch.
- Checked all range/sweep settings, gain endpoints, tone amplitude endpoints, four waveforms and frequency endpoints without exceptions.
- Permission refusal selected CLIPS and showed the fallback hint. A generated MediaStream exercised the microphone graph and release path.
  echoCancellation, noiseSuppression and autoGainControl were all false; all stream tracks ended when switched off.
- Hold retained exactly 19 history frames during a 150 ms wait. A/B survived return to live; clearing works. Returning to live clears the time gap.
- Actual keyboard input reached TONE with Tab and two Right presses. Hold arrows and Shift arrows moved the cursor in the screenshot walk.
- Desktop rendering measured a 16.65 ms mean frame interval across 90 frames, approximately 60 fps. This is not a Chromebook hardware result.
- A **600.016 second** exploratory/measurement walk finished with zero runtime exceptions. Its network log contains only the local document navigation.
  This walk preceded the final synthesis and voice fixes; focused checks cover those fixes separately.
- Final voice/keyboard/numerical checks had no JavaScript errors. Final phone follow-up had zero console errors or warnings.

Evidence: ../../_scratch/voice-lab/functional-retry.json, stress-final.json, keyboard-final.json, voice-final.json and play/results.json.
LPC remains approximate: adult ee measured about 280/2,270 Hz and oo about 280/830 Hz; the synthetic child's ee can under-read F2 near 2,060 Hz.
Formant output is suppressed for known non-vowel synthetic sources. The tool never substitutes a reference point for a measured estimate.

## Voice walk

Bank metadata is news-reader / Rasalgethi, with the specified studio-engineer style. No voice recordings were made.
Curio.voice uses browser speech fallback. The exact bank voice is therefore not guaranteed on the device.

Held clicks at two-second spacing verified the first hint once, followed by two explicit Read calls, including with Sound off.
Read reports current input and detected pitch/note; on Hold it also reads the cursor. It speaks no unsolicited teaching sequence.
An audit exposed an incorrect welcome argument shape on a non-audio first action. It was fixed to the documented tuple;
voice-final.json records the corrected welcome and Read calls with no exception. Repeated and rapid click checks finished clean.

## Short test

The ten-minute walk used a casual grade-8 exploration perspective followed by a measurement/comparison perspective.
This was an automated engineering walk with frame inspection, not recruited child or adult usability testing.

- Would a kid open it without an assignment? **Yes, my judgement:** a whistle, vowel or siren immediately makes a manipulable sound picture.
- Would an adult play for fun? **Yes, my judgement:** spectrum memories, analysis bandwidth, formants and controlled tones support real comparisons.
- Is the real thing the interface? **Yes:** the ribbon and measurements come from the actual audio graph.
- Does it work without a score or finish? **Yes:** nothing must be passed, unlocked or finished.

| Voice Lab | Beat Lab reference |
|---|---|
| ![Voice Lab held vowel measurement](../../_scratch/voice-lab/retry/vowels-final.png) | ![Beat Lab reference](../../_scratch/voice-lab/models/beat-model.png) |

The comparison is density and confidence: working material fills the stage, controls belong to the instrument, and numbers answer actions.
Elements Inspector was also used, including selecting oxygen. Span and Spire and Pocket Universe supplied the plate, Manual and power-panel family marks.

## Lesson creep check

Searched src.html and voice lines for score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done.
Only **LEVEL/level** remains, in four audio-readout/meter occurrences: dBFS is an essential instrument measurement, not progression.
No score, challenge ladder, stickers, quiz, finish screen, mode pills or kit header exists. There is no vowel target to match.

## Done when

| Spec item | Result and evidence |
|---|---|
| 1. Open directly; mic response within 100 ms | **FAIL, hardware timing unverified.** Direct glass opening and generated-stream input pass; physical microphone latency was not measured. |
| 2. Privacy line; no recording/storage/transmission | **PASS.** Exact line before/during input; code inspection, stream lifecycle and local-file network log. Temporary spectral RAM is explicitly explained. |
| 3. Refused mic selects CLIPS; every pad works | **PASS.** Refusal path and both complete pad banks exercised. |
| 4. Pitch accuracy and A4 | **PASS.** Seven real generator checks plus 94 independent sample-array checks, all within 1%. |
| 5. Wide and Narrow visibly differ | **PASS.** 512/4096 FFTs and broad-band versus harmonic-line frames. |
| 6. Keyboard controls, values and held cursor | **PASS.** Native named controls, range value text, shortcuts, live announcements, actual keyboard selector and Hold-arrow runs. |
| 7. 60 fps on Chromebook; extreme range/sweep | **FAIL, hardware unverified.** Desktop approximately 60 fps and 16 kHz/20 s extremes pass; no physical school Chromebook was available. |
| 8. Layout and lower-left family marks | **PASS.** All eight STANDARDS sizes, with 375 px in an iframe, plus targeted overlap fixes and final phone frames. |
| 9. Motion off and AA contrast | **PASS.** Stepped updates, no perpetual CSS animations. Phosphor/glass 17.15:1; muted deck text 8.17:1; module labels 8.33:1; active text 9.02:1. |
| 10. Short test and reference frame | **PASS as engineering judgement.** Ten-minute walk, four answers and side-by-side frames above; not a human usability study. |
| 11. No lesson rewards or correct vowel | **PASS.** Lexical inspection and visual inspection, with the legitimate audio LEVEL exception. |

## Audit leads

Initial audit: **41 leads**, then the runner stopped on unsupported key `3`. A smaller recovery ran the unfinished states,
Motion, held-click walk, repeats, rapid taps and resize stress without repeating the full size sweep. Recovery finished with **68 leads**.
These are retained pre-fix leads, not a claim of a clean raw audit. Detailed dispositions are in ../../_scratch/voice-lab/audit-dispositions.json.

- Fixed genuine issues: input module overlap at 800–1,000 px, phone F1/F2 overlap, obscured cursor text, welcome API exception,
  Manual link target sizes, Manual title block geometry and the scratch HTTP host's favicon errors.
- Canvas/status/hint/privacy/chart overlaps are intentional instrument overlays. The first hint is intentionally hidden after sound begins.
- The modal Manual intentionally covers and makes the instrument inert. Its scrollable source links are reference prose, not hidden activity choices.
- The plural checker mistook dBFS for a plural noun. Live-glass clicks intentionally do nothing until Hold.
- A lesson-style premise is intentionally not spoken after the student has already started a sound. Sound-off speech cuts are intentional; Read still works.
- The first tone-state recipe opened a native popup rather than changing input. It now uses Tab and Right keys;
  keyboard-final.json independently confirms actual keyboard selection reaches TONE.
- Recovery captured some pages before the voice fix and other pages afterward. Final focused voice and phone checks verify the corrected paths.
- All repeat/rapid-click rows were clean, and completed resize stress reported no exceptions or stuck disabled controls.
  Server connection-reset messages were test-tab HTTP connections closing, not application exceptions.

## Frames looked at

Inspected all **56 screenshot PNGs** in models/, first/, frames/, retry/, final/, phone-clean/, play/, audit/ and audit-remaining/.
This excludes Chrome's automatically installed profile resource images. The screenshot list is in ../../_scratch/voice-lab/final-manifest.json.
The complete size run was done once; follow-ups targeted discovered defects. Final phone frames show the readable cursor beside the chart and the clear Manual header.

## Art made

None. art/prompts.json deliberately has an empty asset list. Exact canvas data, rulers, meter, chart and CSS instrument surfaces are the finished visual material.

## Engine changes wanted

Shared tool-page iframe needs allow="microphone" as the spec anticipates; it is outside the authorized write scope.
The kit could allow plain power-panel labels without locally restoring them after emoji insertion.
The audit keyboard mapper should support alphanumeric shortcuts. No shared files were changed.

## Left open

- Physical microphone response timing, school Chromebook performance and listening quality require hardware verification.
- High-pitch LPC can have large errors, especially the synthetic child's ee. Historical reference values remain exact and separate from estimates.
- No recorded news-reader bank voice is bundled; offline speech depends on installed browser voices.
- Gain/frequency use accessible native faders, and range/sweep use detented selectors, rather than reproducing every rotary-knob shape literally.
- Spec tensions were resolved without questions: two banks accommodate more sounds than eight pads; the chord has unequal log-scale thirds;
  bin spacing is distinguished from bandwidth; temporary spectral memory qualifies the privacy wording; explicit Hold-only formant readouts
  take precedence over the concept's continuously walking vowel-dot description. The tool is a second module card because MS-PS4-2 is not covered.
- No learner study or month-long usage study was performed. The depth assessment is an engineering judgement.

Build only. The report was written last to honor the instruction to stop when it exists.
