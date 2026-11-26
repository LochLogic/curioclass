# voice-lab: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: voice-lab (Curiosity No. 03)

#### Built

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

#### The real material

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

#### Break the instrument

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

#### Voice walk

Bank metadata is news-reader / Rasalgethi, with the specified studio-engineer style. No voice recordings were made.
Curio.voice uses browser speech fallback. The exact bank voice is therefore not guaranteed on the device.

Held clicks at two-second spacing verified the first hint once, followed by two explicit Read calls, including with Sound off.
Read reports current input and detected pitch/note; on Hold it also reads the cursor. It speaks no unsolicited teaching sequence.
An audit exposed an incorrect welcome argument shape on a non-audio first action. It was fixed to the documented tuple;
voice-final.json records the corrected welcome and Read calls with no exception. Repeated and rapid click checks finished clean.

#### Short test

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

#### Lesson creep check

Searched src.html and voice lines for score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done.
Only **LEVEL/level** remains, in four audio-readout/meter occurrences: dBFS is an essential instrument measurement, not progression.
No score, challenge ladder, stickers, quiz, finish screen, mode pills or kit header exists. There is no vowel target to match.

#### Done when

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

#### Audit leads

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

#### Frames looked at

Inspected all **56 screenshot PNGs** in models/, first/, frames/, retry/, final/, phone-clean/, play/, audit/ and audit-remaining/.
This excludes Chrome's automatically installed profile resource images. The screenshot list is in ../../_scratch/voice-lab/final-manifest.json.
The complete size run was done once; follow-ups targeted discovered defects. Final phone frames show the readable cursor beside the chart and the clear Manual header.

#### Art made

None. art/prompts.json deliberately has an empty asset list. Exact canvas data, rulers, meter, chart and CSS instrument surfaces are the finished visual material.

#### Engine changes wanted

Shared tool-page iframe needs allow="microphone" as the spec anticipates; it is outside the authorized write scope.
The kit could allow plain power-panel labels without locally restoring them after emoji insertion.
The audit keyboard mapper should support alphanumeric shortcuts. No shared files were changed.

#### Left open

- Physical microphone response timing, school Chromebook performance and listening quality require hardware verification.
- High-pitch LPC can have large errors, especially the synthetic child's ee. Historical reference values remain exact and separate from estimates.
- No recorded news-reader bank voice is bundled; offline speech depends on installed browser voices.
- Gain/frequency use accessible native faders, and range/sweep use detented selectors, rather than reproducing every rotary-knob shape literally.
- Spec tensions were resolved without questions: two banks accommodate more sounds than eight pads; the chord has unequal log-scale thirds;
  bin spacing is distinguished from bandwidth; temporary spectral memory qualifies the privacy wording; explicit Hold-only formant readouts
  take precedence over the concept's continuously walking vowel-dot description. The tool is a second module card because MS-PS4-2 is not covered.
- No learner study or month-long usage study was performed. The depth assessment is an engineering judgement.

Build only. The report was written last to honor the instruction to stop when it exists.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: voice-lab
#### Played
Cold-played before reading the builder's report, notes, handoff or source. Grade-8 exploration and adult measurement perspectives; actual muted Chrome audio graphs, held clicks and inspected frames, not a recruited usability study.
Covered microphone refusal, both eight-pad banks, wide/narrow analysis, chart, generator, Hold, A/B and Manual. The original loaded build ran for 601.547 seconds with 192 actions and no runtime exceptions.
Short test, reviewer judgement: kid would reopen it YES; adult play YES; real sound is the interface YES; works without a score or finish YES. The chart's initially absent live response weakened the third answer; the measured live cross now makes it central.
| Voice Lab | Beat Lab comparison |
|---|---|
| ![Live measured vowel](../../_scratch/voice-lab/review/last-focus/chart-1366-fixed.png) | ![Beat Lab](../../_scratch/voice-lab/review/finish-play/beat-lab-model.png) |
The ribbon, rulers, LED meter and lower deck have the confidence and density of a real analyser. Kept them.
#### Findings fixed
- **Blocker, family:spectrogram, held Read:** moving into a 220 Hz historical slice displayed 220 but narrated the latest 440. Read now takes pitch/note from the displayed frame, and explicitly identifies empty history.
- **Should fix, family:spectrogram, LPC:** a shallow spectral ripple made synthetic child ee report F2 near 2,060 Hz. Rejecting peaks below 2 dB prominence gives 3,130 Hz in three sampled frames against the 3,200 Hz synthesis resonance. No reference-point substitution.
- **Should fix, family:spectrogram, mic measurement:** a pure sine entering the microphone graph acquired spurious formants, and stale pitch survived a silent frame. A second-order residual gate rejects near-pure sines; silent frames clear pitch/formants. The generated mic recheck passes and all six synthetic vowels still yield estimates.
- **Should fix, family:spectrogram, chart:** the live estimate was computed but hidden. The measured cross now follows live vowels; the numerical readout remains Hold-only. Added Hz to the readout label.
- **Should fix, family:spectrogram, chart calibration/layout:** axis labels did not match plotted coordinates; the 680x425 chart crushed its points and labels. Matched coordinates to ticks, used compact chart margins, removed a colliding label and protected the privacy sentence from the chart.
- **Should fix, general, keyboard:** global Space intercepted native buttons. Space now activates the focused button; canvas/body retain the Hold shortcut.
- **Should fix, family:spectrogram, generator:** Stop left no clear restart action and retained connected gain nodes. The existing pad becomes Start, standby is explicit, and stopped gain nodes disconnect.
- **Should fix, general, first response:** adult vowel synthesis blocked about 137 ms on this desktop. Equivalent sine recurrence reduces generation to about 6-13 ms; direct-sine comparison differs by at most 1.5e-8 in the tested partial.
- **Should fix, general, provenance:** clarified copyrighted publications versus factual values and original MIT synthesis, named the actual W3C licence, added links and LPC guidance, and updated notes/handoff/voice metadata/audit states.
- **Should fix, general, audit-confirmed voice:** a first Manual tap narrated an inaccessible mic switch. The first hint now excludes Manual/Hold; entering these states or changing input hushes stale speech. Focused first-tap, rapid-tap and main-path rechecks passed with no runtime errors.
#### Findings left
No confirmed implementation blocker or should-fix left. Hardware, listening and shared-site limitations are under Left open.
#### Break it
No score, quiz, success meter or gated path exists. LEVEL is RMS signal amplitude in dBFS, not progression. Silence gives -60 dBFS and no pitch; gain cannot earn anything.
Lesson-creep search of source and voice lines found only four legitimate audio LEVEL/level occurrences; no rewards, goals, quizzes, finish screen, kit header or vowel targets.
Exercised gain -20/+20, amplitude -40/0, generator 20/8,000 Hz, all four ranges, four sweeps, four waveforms, both scales, both bandwidths, three maps, every pad, and repeated rapid toggles. Resized while sound was running.
Post-fix assertions: held/empty Read, native Space, Start after Stop, silence and generated tones 80/100/220/440/880/1,000 Hz all pass. All 94 independently generated sine arrays at 44.1/48 kHz stay within 1%; worst error 0.374%.
LPC on six synthetic vowels and multiple sample positions remains an estimate; child ee F1 can under-read. Invalid/non-vowel inputs do not acquire invented formant reference values.
Evidence: `../../_scratch/voice-lab/review/verified/results.json`, `virtual-mic-final.json`, `diagnostic/results.json` and inspected before/after frames. No runtime exceptions in the focused verification. The generated mic stream measured 220 Hz, requested all three speech filters off, and its track ended on mic off. This tests graph/lifecycle, not a physical microphone.
#### Voice walk
Sound on, 120 ms held clicks, two-second pace: MIC -> refusal -> Read -> Ah -> Ee -> Oo -> Read -> Sound off -> Read -> Sound on. Then TONE, a held older slice and Read.
Initial log order: fallback hint once; "Built-in sounds"; "Built-in sounds. Pitch 140 hertz. C sharp 3."; the same explicit Read with Sound off; "Tone generator. Pitch 220 hertz. A 3. Held. Cursor 1.40 seconds back, 1600 hertz."
After the audit voice fix, repeated MIC -> refusal -> Ah -> Ee -> Read -> Sound off -> Read -> Sound on at the same pace. Fallback once, cut on starting input; both requested Reads reported the displayed 140 Hz C sharp 3. No late hint followed the sound.
| Line kind | Expected | Observed |
|---|---|---|
| Mic-free how-to | Once, then quiet | Once |
| Automatic teaching or mode narration | None for this Curiosity | None |
| Explicit Reads | Each requested, current state | All logged in order |
Manual-first now logs no speech; Hold-first plus Read reports empty history. Rapid band -> Manual cuts the hint with `manual`; band -> Ah cuts it with `input`. No unsolicited line follows. Evidence: `../../_scratch/voice-lab/review/voice-audit-fix/` and the five matching JSON logs one directory above. Browser speech fallback was logged; muted testing cannot certify audible delivery or the specified recorded voice.
#### Facts checked
Checked online 2026-11-05. No external audio, imagery, library or downloadable dataset was added; only the existing 27 numerical formant facts remain bundled.
- All nine formant triples: [Peterson and Barney 1952, Table II](https://pure.mpg.de/rest/items/item_2375480/component/file_2375479/content), corroborated by [Iseli, Shue and Alwan 2007, Table I](https://www.ee.ucla.edu/~spapl/paper/Iseli_JASA_07.pdf). Exact agreement. ASA copyright; no open redistribution licence claimed for either paper. Numerical facts only, no copied text, table artwork or recordings.
- Pitch/YIN and its limits: [de Cheveigne and Kawahara 2002](https://www.ee.columbia.edu/~dpwe/e6820/papers/deChevK02-yin.pdf), plus independent periodic-array calculations. ASA copyright; original implementation, no copied software.
- FFT/Blackman, bin spacing and window tradeoff: [W3C Web Audio](https://www.w3.org/TR/webaudio/), under the [W3C Software and Document licence 2023](https://www.w3.org/copyright/software-license-2023/). Recomputed 48,000/512 = 93.75 Hz, 48,000/4096 = 11.71875 Hz; these are bin spacings, not analysis bandwidths. No spec prose copied.
- LPC/pre-emphasis and speaker-dependent uncertainty: [Praat formant guidance](https://praat.org/manual/Sound__To_Formant__burg____.html), corroborated by the Iseli research above. Copyrighted references; original code, no copied prose or software.
- Harmonic multiples and low-register clarinet odd-harmonic emphasis: [UNSW clarinet research](https://phys.unsw.edu.au/jw/clarinetacoustics.html) and [UNSW flute acoustics](https://phys.unsw.edu.au/jw/fluteacoustics.html); consistent with the spec's Fletcher/Rossing reference. Copyrighted research; only principles used, recipes are original illustrative MIT synthesis.
- Whisper preserves resonances without periodic voicing: [Smith 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5051627/) (CC BY 3.0) and [Li/Guo 2012](https://www.isca-archive.org/tal_2012/li12_tal.pdf) (copyrighted paper, no open licence claimed). Fact corroboration only; nothing from their audio/text bundled.
- Sss/shh relative spectral location: spec's Jongman/Wayland/Wong 2000 research, corroborated by [Jongman/Wang/Sereno 2000](https://www.isca-archive.org/icslp_2000/jongman00b_icslp.pdf). Copyrighted references; the 6,500/2,700 Hz noise filters are original approximations, not measured recordings.
- A4 = 440 Hz: [ISO 16:1975](https://www.iso.org/standard/3601.html), current as confirmed 2022, copyrighted factual reference only. Independent equal-temperament arithmetic confirms A4, octave doubling and the C-major chord's unequal 4/3-semitone thirds.
- Privacy: code inspection plus request log; only document navigations, with no audio upload, recording, export or storage calls. Temporary rolling spectra and A/B RAM are disclosed. Only Motion is saved.
Sources and permission distinctions are also in the Manual and `tool.draft.json`. Original code/synthesis MIT; original Manual CC BY 4.0. Checked publications retain their own copyrights.
#### Sensitivity
Human voices/bodies and historical American English categories: a sensitivity reviewer should check the source's men/women/children labels and synthetic examples. They are descriptive historical groups, never pronunciation targets or ways to infer gender, age, accent or ability. No people images or diagnosis claims.
#### Flattest moment left
Synthetic sounds have less character than recorded instruments. Kept the honest synthetic launch specified by the brief. The former flat live chart now responds directly to the sound, and first pad generation is faster.
#### Graphics
No painted images or missing art tokens. Inspected 65 frames, including all 20 audit frames, the real spectrum, rulers, chart, meter, Manual and deck at all eight sizes, grayscale and Motion off. No kit header or lesson layer was added. Frame list: `../../_scratch/voice-lab/review/final-manifest.json`.
Computed text contrast: readouts 15.37:1; controls 9.92:1; deck labels 7.99:1; active pads 8.64:1; plate 7.13:1. Audit found no small targets, clipped text, horizontal scroll or focus failure.
Final bundle: 77,665 bytes (75.8 KiB), below the 400 KB spec budget. SHA-256: `e7e40e312edff168c8e2d368b5018c1a72e8ac66acde44286bdf1dd707fba793`. Evidence stays in the two authorized folders; no commits.
#### Audit
Ran the unmodified audit functions once, last, through `../../_scratch/voice-lab/review/audit_bounded.py`, with an outer 2,400-second cap; completed. Chrome 9941, host 8745. Full evidence: `../../_scratch/voice-lab/review-audit/audit.md`.
74 mechanical leads: 65 frame leads are intentional canvas/status/privacy/chart or modal overlays, the deliberately dismissed hint, and scrollable Manual references; nine missing-welcome flags are intentional first-sound/fallback behaviour for a Curiosity. Every line has a disposition in `../../_scratch/voice-lab/review/audit-dispositions.json`.
All 24 walked controls had no runtime/focus failure; five-click repeats and rapid taps were clean. All listed-state and walked-control resize stress finished without exceptions or stuck controls. The Manual row also revealed the real stale-hint flaw, fixed afterward as required, with only the affected voice paths rechecked. Raw audit predates that final voice-only fix; no second full audit or polish pass.
All assigned Chrome ports 9940-9947 and host 8745 were verified closed after the last focused check. No tool-folder host.html remains.
#### Left open
- Physical microphone onset under 100 ms, audible playback/speech quality and 60 fps on an actual school Chromebook require hardware checks. Desktop evidence is not a substitute.
- Embedding requires `allow="microphone"`; the shared iframe permission was not verified or changed in this scoped review. Standalone access and mic-free pads are the specified fallback.
- The named news-reader recording is absent; installed browser voices remain the build's explicit fallback. No recording or external service was invoked.
- Unattended choices followed the brief: live chart plus held numeric values; original synthetic sounds; no lesson rewards or goals. Left the spec's file untouched.

<!-- end part -->

## Refine

<!-- part: refine.md -->

PASS (exit check 2026-11-06)
Counts: blockers 1 (general 1, family 0), should fix 10 (general 7, family 3), polish accepted 15

### Refine: voice-lab

Curiosity No. 03. Merged from `refine/teaching.md`, `refine/play.md` and `refine/craft.md` (no sensitivity file; the
Teaching lens found nothing cultural, Native or hard-history). Lens frames: `S:/CurioClass-codex-scratch/voice-lab/teaching/out/`,
`.../play/`, `.../craft/out/`; shared audit `S:/CurioClass-codex-scratch/voice-lab/audit-r1/`. Judged by
`docs/agents/CODEX-CURIOSITY.md` and BASELINE: every fix below adds real material or makes a readout true, never a
goal, task, score or finish. Integrator spot-checks (src.html read): PEAK search and clamp at 588-591, the F1/F2 gate at
631, `clearHistory` on Live at 609, and the loop taper at 460-462 all read as the lenses say.

#### Blocker
1. **PEAK lies about low frequencies in Wide band (the default).** `src.html:588-591`. The peak search runs on the
   512-point Wide FFT (93.75 Hz bins at 48 kHz) from bin 1 up, and the parabolic offset is clamped to half a bin, so
   anything under about 190 Hz snaps to bin 1 plus or minus half a bin, while the readout shows whole hertz. Seen by
   two lenses: a 100 Hz sawtooth reads PEAK 47 Hz beside PITCH 100 Hz (Teaching, `teaching/out/saw100-wide.png`,
   `tones.json`); an 80 Hz tone reads PEAK 100 Hz (Craft, `craft/out/k-tone` log); 100 Hz square reads 82 Hz; the adult
   "Ee" pad's PEAK jumps 228 to 301 Hz frame to frame when its strongest harmonic is 280 Hz. Narrow is right to 1 Hz in
   every case. A deep voice's fundamental and spec Things to do 11 (sweep from 20 Hz) live in this range. Fixed: PEAK
   always comes from the 4096-point `tracker` analyser (whatever the Band switch shows), so a low tone reads within a
   few hertz of PITCH in both bands; if any case still can't resolve, show dashes rather than a precise wrong number.
   This also keeps PEAK true if Wide moves to a 256-point window (polish 4). (general)

#### Should fix
1. **On the site, the first screen tells every student to do something that cannot work.** `src.html:122` hint,
   `toggleMic` at 368. The site's tool page iframe has no microphone permission (Play, `play/p15-iframe-first.png`), so
   the student reads "Press the mic switch, then say ahhh.", presses it, and only then hears "No mic here." Fixed: on
   load, the tool checks whether the mic is allowed at all (`document.permissionsPolicy?.allowsFeature('microphone')`,
   falling back to `document.featurePolicy`) and, when it is blocked, opens straight on the no-mic state: input on
   CLIPS, the fallback hint "No mic here. Press a sound pad." on the glass (its spoken line unchanged), ideally with a
   short note that Play full screen gives the mic. Normal mic-refused behaviour stays as it is (`play/p12-mic-refused`).
   The iframe itself is a site item, not this tool's (see open questions). (family:curiosity)
2. **F1 / F2 readout never moves in live play.** `src.html:631` (`state.held&&f?.f1`). While a vowel plays the estimate
   is good (ah 710/1100, oo 280/830, child ee 310/3130) and the chart cross moves, but the readout shows "··· / ···"
   until Hold is pressed, so one of five readouts looks broken (Play, `play/p06` log, p19). The spec's "while a voiced
   sound is held" means sustained, not the Hold pad. Fixed: show the live smoothed estimate whenever a voiced input is
   giving one, dashes when not (whisper, hiss, silence), and let Hold freeze it. (family:curiosity)
3. **PITCH goes blank on whistles, including the built-in whistle pad.** `yin()` at `src.html:486-506` (capped at
   1,000 Hz). The Whistle pad glides 680 to 1,120 Hz and PITCH and NOTE show dashes for about a third of each loop
   (Play `play/p02-whistle-pitchlog.png`, Teaching `teaching/out/whistle.png`); real whistles sit at 1 to 3 kHz, so
   Things to do 2 and the first-two-minutes promise ("PITCH follows the voice note by note") fail. Fixed: raise the
   PITCH ceiling to about 4 kHz for a clean single line (or fall back to the tracker's PEAK when the input is one
   clean line above the YIN range), keeping Done when 4 (within 1 percent from 80 to 1,000 Hz) passing. If the higher
   range can't be made reliable, at least the whistle pad stays inside the range and the Manual says a whistle may sit
   above PITCH, read PEAK. (general)
4. **The big MIC knob is not the mic switch.** INPUT module, `src.html:131-132`. The hint says "Press the mic switch";
   the eye goes to the large round knob labelled MIC, which is a styled `<select>` that opens a browser drop-down
   (MIC / CLIPS / TONE) and does nothing visible. The real switch is the small rocker also labelled MIC (Play,
   `play/p13-rotary-click.png`; Craft finding 6). Fixed: the input rotary turns one detent per click (no drop-down),
   keeping Left/Right and keys 1, 2, 3; the rocker reads "MIC ON / OFF" (or lights when on) so the two never share a
   bare label. (general)
5. **The vowel chart covers the newest sound.** `#vowels` at `src.html:34`, short-box rules 98 and 104. Time enters at
   the right, and the chart sits over the right of the ribbon: at 1366x768 it hides the live edge (Play says the last
   1.3 s at the default sweep, Craft about 5 s at a 20 s sweep), the 1x to 10x harmonic ticks drawn at the right edge
   (lines 703-708) and the Hold crosshair at its default 0.98; at 680x425 it covers almost the whole ribbon. Seen:
   audit `state-vowel-held-1366x768.png`, `state-live-vowels-680x425.png`, `craft/out/perf-stress.png`,
   `craft/out/k-vowels-375.png`, `play/p06`, `p19`. Fixed, keeping the spec's right-hand panel: when the chart is open
   the ribbon narrows so its live edge, the harmonic ticks and the Hold crosshair's default sit just left of the
   panel; at short and narrow sizes the chart takes the ribbon's right half (spec 375x812 line) and the ribbon keeps
   the left half. (general)
6. **The looped clips draw a fake event every 4 seconds.** `makeBuffer`, `src.html:460-462`. The 8 ms taper at both
   ends of each 4 s buffer makes a 16 ms dip every loop, which shows as a regular vertical broadband stripe a student
   can measure as part of the sound (Craft, `craft/out/perf-stress.png`, stripes about 4 s apart on Narrow Ee). Fixed:
   harmonic clips hold a whole number of cycles and loop with no taper; noise and glide clips use a crossfade at the
   loop point instead of a fade to zero. Check on Narrow at a 20 s sweep that no stripe remains. (general)
7. **Pressing Live after Hold wipes the ribbon.** `toggleHold`, `src.html:609` (`else clearHistory()`). Hold, measure,
   Live: the whole picture is gone (Play `play/p07-hold-then-live` log; Craft finding 8). A teacher loses what the class
   was looking at, and a student can't hold, check, then compare with the next word. Fixed: Live keeps the history and
   resumes scrolling (the gap may show); `clearHistory` stays for an input change and mic off. (general)
8. **Amplitude and energy, half the anchor code, is never shown.** MS-PS4-1 asks how a wave's amplitude relates to its
   energy. Students can change amplitude (OUTPUT, GAIN, LEVEL in dBFS), but nothing links amplitude to energy, and dBFS
   alone can't be read as "twice the amplitude" at grade 8 (Teaching finding 2, code read plus `data/modules.csv:619`).
   Fixed with more real material, not a task: a linear amplitude readout beside the tone level (for example "×0.25")
   with relative energy (amplitude squared), and a Manual "Things people have found" entry such as "6 dB up is twice
   the amplitude and four times the energy", with a source. MS-PS4-2 stays honestly declared untaught. (family:curiosity)
9. **The instrument does not fill the site's preview sizes.** At 680x425 the glass plot is about 60 px tall, the 4k
   and 3k ruler labels touch, the hint sits on grid lines and the deck takes over half the screen; at 800x500 it is
   about 170 px (Craft finding 3; audit `size-680x425.png`, `size-800x500.png`; Play saw the same cramped ribbon).
   Fixed: in short boxes the deck folds to one row (pads as a compact strip, Measure into the footer) so the glass keeps
   at least half the height, and the ruler drops to two ticks when the plot is under about 120 px. (general)
10. **The ribbon's focus ring is invisible.** `#glass{overflow:hidden}` at `src.html:27` clips the `#ribbon` focus
    outline. The ribbon is the first Tab stop and Hold moves focus to it on purpose (line 608), so a keyboard user
    measuring never sees focus (Craft, `craft/out/k-tab1.png`, `k-hold.png`). Fixed: an inset outline
    (`outline-offset:-3px`) or a ring drawn inside the glass. (general)

#### Polish accepted
1. **Vowel chart says what its dots are.** `src.html:634-664`, `teaching/out/ee-oo-chart.png`. Add a legend line
   "Peterson and Barney 1952, US English averages" on the chart itself, and name the vowels on all three groups (or
   say in the legend that names are on the men's set). Keeps Done when 11 (no "correct vowel target") true in spirit.
   (family:curiosity)
2. **Octave ticks on the Musical ruler.** `src.html:685` uses 20, 50, 100, 200, 500, 1k. Add octave ticks (55, 110,
   220, 440, 880 Hz, or C2 to C8) so the equal room per octave the Manual describes is visible
   (`teaching/out/chord-log.png`). (general)
3. **Whisper sounds and draws like a whisper.** `src.html:430-442, 458-459`. Every clip is normalized to one peak, so
   "Whisper ah" is louder and brighter than voiced "Ah" (`teaching/out/whisper-vs-ah.png`). Scale it about 15 to 20 dB
   below the voiced vowels and band-limit its noise floor so the three resonances stand out. (general)
4. **Wide band at the spec's bandwidth.** The spec asks for about 300 Hz; the 512-point Blackman gives about 160 Hz, so
   adult "Ah" still shows half-resolved harmonic stripes in Wide (`teaching/out/ah-wide.png`). Use a 256-point Wide
   window (update the RATE strip's "FFT" note and the Manual's bin numbers), and confirm Done when 5 still passes.
   Do this together with the Blocker fix so PEAK does not get coarser. (general)
5. **The flute can't play A3.** `src.html:291`. A concert flute's lowest note is C4. Put all three instruments on
   C4 (about 262 Hz; still the clarinet's low register, so the odd-harmonic finding holds), relabel the pads, update
   the Manual, and keep should fix 6's whole-cycle loop. (general)
6. **A/B outlines readable.** `src.html:710-720`. Both traces are squeezed into the left 30 percent over the ribbon with
   labels across them (`play/p03-instruments-AB.png`, `play/p18-sss-then-shh.png`). Give them a darker backing panel, a
   wider plot, and labels outside the traces. (general)
7. **Privacy line off the data.** `#privacy` at `src.html:31`. It sits over 0 to 400 Hz of older history, where the
   fundamentals and F1 are drawn (Play F10, Craft finding 9; `craft/out/k-tone.png`). Move it to the time-axis row or
   the readout strip, still visible before and while the mic is on (Done when 2). (general)
8. **Readable from the back of a room, and plainer words.** `src.html:25-26`: readouts stay 19 px and deck legends
   10 px at 1920x1080 (audit `size-1920x1080.png`). Scale readouts with the viewport (clamp to about 32 px) and lift
   the smallest deck and chart text where it fits. Change "A / B · volatile slices" (line 167) to "A / B are kept until
   you close the tab". (general)
9. **The chord's "C2" becomes a find, not an error.** C major pad reads PITCH 65.5 Hz, "C2 +4 ¢" (`play/p04-chord-log.png`,
   `teaching/out/chord-log.png`). It is the chord's real common period. Add a sourced "Things people have found" entry
   (C4, E4 and G4 repeat together once every C2 period). (family:curiosity)
10. **Range, Sweep, Bank and Wave as instrument controls.** They are drop-down `<select>`s; the spec asks for a range
    knob with detents and a sweep fader. Draw detent knobs or stepped faders in the deck's metal that step on click,
    keeping the same keyboard paths and announcements (Craft finding 6). Same treatment as should fix 4. (family:curiosity)
11. **Switches show every position.** Linear, Wide and Ember show only the current one (audit `size-1366x768.png`).
    Two- and three-position switches with every position printed and the lit one marked. (general)
12. **A pad press during Hold returns to Live.** `playPad`, `src.html:466`. Now it plays sound while the ribbon stays
    frozen ("CLIPS / HOLD", `play/p14-hold-pad-press`). Pressing a pad releases Hold (keeping history, per should fix 7). (general)
13. **Read keeps its full stops.** `readNow`, `src.html:305-309`. With no pitch it says "Built-in sounds Held. Cursor
    ...". Add the missing period. (general)
14. **Adult vowel pads say whose average they are.** "Ah adult", "Ee adult", "Oo adult" play the men's averages
    (`src.html:415`) while the chart splits men and women. Label them "man" to match the chart. (general)
15. **Above-range tick.** A tone above the Range (8 kHz on a 4 kHz ruler) leaves the glass blank while PEAK reads
    8001 Hz (`craft/out/k-tone.png`). Draw a small "above range" mark at the top edge. (general)

#### Settled calls
- **PEAK level:** Teaching called it a blocker, Craft a should fix. REFINE.md: a meter or estimate that misleads is a
  blocker. Blocker.
- **Whistle PITCH:** Teaching polish, Play should fix. It breaks a spec activity and the first-two-minutes promise on
  the tool's own pad: should fix.
- **Live wipes the ribbon:** Play should fix, Craft polish. A teacher loses the frozen picture: should fix.
- **Input controls:** Play's MIC knob confusion is a should fix (it blocks the first action); Craft's wider "web-form
  controls" point is polish 10.
- **Vowel chart tag:** Play general, Craft family:curiosity; kept general (any overlay over a live edge). Fixed by
  narrowing the ribbon, not by moving the panel, so the spec's right-hand placement stands.
- **Welcome cut short by the first tap** (audit "welcome not heard" after a pad, Hold, Manual or mic): fine under
  BASELINE rule 16; the hint and Read still carry it. Not a finding.
- **Audit false leads:** "#ribbon overlaps #status/#hint/#privacy/glass-label" is labels on the glass by design (except
  the privacy box, polish 7); "hint out of view" is the first-run hint correctly gone after the first action; "1 dBFS"
  is a misparse of "-13.1 dBFS"; the Manual drawer's scroll rows are the drawer working.
- **Do not change:** the voice lines and their behaviour (Craft's voice check is clean: counts, stale lines, order,
  Read with Sound off); the two fixed lines in `voice/lines.json`; the 60 fps path (Craft table: cost under 3.3 ms);
  TONE releasing the mic (the spec's lean against feedback); no score, goal, level, finish, task or "correct" target,
  and the amplitude fix adds a readout and a Manual entry, never an exercise.

#### To the spec's open questions
- **Site item: the tool page iframe needs `allow="microphone"`** (spec open question 1; Play saw no allow attribute on
  the host iframe, `play/p15-iframe-first.png`). This is the site's tool page template, not this tool; Codex does not
  touch it. The tool's own part (open on the no-mic hint when blocked) is should fix 1.
- **Things to do 10 can't be done** (sing until PITCH matches the 440 Hz tone): TONE releases the mic by the spec's own
  lean (`src.html:359-372`). Either drop the line from the spec or choose a path: a "with headphones" mode (mic and tone
  both live) or, in MIC mode, a silent reference line drawn on the glass to sing onto (Teaching 8, Play F13).
- **Mic-free material.** Without a mic (the site embed, many Chromebooks) only the whistle and siren move. Candidate
  added clips: a pad that glides ee to ah to oo and one that slides "ahh" up an octave (Play F9), and a spoken word pair
  for Things to do 13 and 14. Both banks are full at eight pads, so this changes the sound list. Without a word-pair
  clip, the ela-k-rhymes-and-sounds reach is unsupported wherever the mic is blocked: keep it only if the iframe gets
  the mic, or drop it (Teaching 10).
- **A small oscilloscope trace** of the current input so "wave pattern" (sine, triangle, square, sawtooth) is seen as a
  wave shape, not only as a spectrum (Teaching 2). A new view, so a spec call.

#### Not taken
- NOTE "A4 +1 ¢" beside PITCH 440 Hz (Play F14): both are honest measurements of the same tone and Done when 4 passes;
  forcing them to agree would hide real precision.
- Craft nit 11's general "grade 1 floor" text-size concern beyond polish 8: the first two minutes for a first grader
  need no reading; the readouts are the grades 8 to 12 depth.

#### Exit check (2026-11-06)

Cold exit check, Claude. Fresh audit `S:/CurioClass-codex-scratch/voice-lab/exit/audit-r2/` (finished, exit 0);
own frames and drive results in `S:/CurioClass-codex-scratch/voice-lab/exit/frames/` (shots.json, shots2.json).

##### Merged list
- **Blocker 1, PEAK in Wide: fixed.** PEAK reads the 4096-point tracker (`src.html:681-686`). TONE in Wide (FFT 256):
  80 Hz sine 79.94, 100 Hz saw 99.97, 100 Hz square 99.98, 140 Hz 139.98, 440 Hz 439.97; Narrow gives the same values;
  20 Hz shows dots, not a number (e02).
- **Should fix 1, blocked mic on the site: fixed.** A cross-origin iframe with no `allow` (my own host page) opens on
  CLIPS, "No mic here. Press a sound pad.", status "CLIPS / NO MIC HERE · PLAY FULL SCREEN FOR MIC", rocker disabled
  (e03). Same-origin load still opens on the mic hint (e01). The site iframe `allow="microphone"` stays a site item.
- **Should fix 2, live F1/F2: fixed.** Without Hold: Ah man 710 / 1103, Ee man 281 / 2268, Oo man 281 / 832, whistle
  dashes (e04); Hold freezes it.
- **Should fix 3, whistle PITCH: fixed.** Whistle pad: 0 blanks in 50 samples, 679 to 1127 Hz (e05); clean tones
  1000, 1500, 2500, 3900 Hz read within 0.1 Hz (e18).
- **Should fix 4, MIC knob: fixed.** The rotary is a button that steps one detent per click (two held clicks: MIC to
  CLIPS to TONE), no visible select anywhere, rocker reads MIC OFF / MIC ON (e06, e01).
- **Should fix 5, chart over the live edge: fixed.** 1366x768: ribbon 0 to 1030, chart 1038 to 1358, meter and "now"
  left of the panel (e07). 680x425: ribbon 0 to 344, chart 352 to 672 (e08).
- **Should fix 6, loop stripe: fixed.** Narrow Ee at a 20 s sweep, 14 s of play across three loop points: steady
  harmonic lines, no vertical stripe (e09).
- **Should fix 7, Live wipes history: fixed.** Hold then Live: history 152 frames kept and grew to 250 (e10).
- **Should fix 8, amplitude and energy: fixed.** -6 dB: AMP ×0.501, ENERGY ×0.2512; -12: ×0.251 / ×0.0631; Manual
  entry "About 6 dB up doubles amplitude and quadruples relative energy", sourced UNSW and OpenStax (e11).
- **Should fix 9, short boxes: fixed.** Glass 224 of 425 px at 680x425 (e12, frame shows one-row deck, Hold/A/B in the
  footer), 299 of 500 at 800x500 (e13).
- **Should fix 10, ribbon focus: fixed.** First Tab lands on the ribbon with a 2 px solid ring at -3 px offset,
  visible inside the glass (e14); Hold also focuses the ribbon (e15).
- **Polish, spot-checked in bulk:** 1 chart legend (e07, e08), 4 FFT 256 in Wide (e02, RATE strip), 5 C4 recipes
  (code `makeBuffer`), 7 privacy line in its own row (e01, e07), 8 A/B wording (e07), 10 Range/Sweep/Bank stepped
  faders (e07), 11 every switch position shown (e07), 12 pad releases Hold (code `playPad:567`), 13 Read stops (e15
  "Held. Cursor ..."), 14 pads say "man" (e07). Others taken on polish.md's evidence. Polish never blocks.

##### Regressions
None found. Default screen at 1366x768 and 375x812 (audit) clean; CLIPS, TONE, Hold, Narrow, Vowels and Manual each
seen once; frames tied to each fix look right. Wide Ah shows fine vertical pitch-period striations at FFT 256: expected
of a 5 ms window on a 140 Hz voice, not the loop stripe.

##### Gate
1. Done when: passes on what I checked (PITCH within 1 percent 80 to 1000 Hz and above, PEAK true, privacy line, no
   "correct" target, Wide near 300 Hz). Yes.
2. Codes: MS-PS4-1 now carries amplitude and energy; MS-PS4-2 written down as not covered (`notes.md:4`). Yes.
3. Solo defaults: work, including with the mic blocked. Yes.
4. Sensitivity: none flagged by the merged list (Teaching found nothing cultural or hard-history). Not applicable.
5. No blocker or should-fix open. Yes.
6. Bundle 89,241 bytes; no console errors in the audit or my 19 shots; zero resource requests (e01). Yes.
7. Voice: two fixed lines unchanged; five held clicks and two quick taps clean on every speaking control; Read speaks
   with stops. Yes.

#### Audit pilot
- Leads confirmed: none as defects. The size table also confirms no console errors and no dead controls.
- Leads wrong: all 44. "#ribbon overlaps #status/#hint" is labels on the glass by design; "hint out of view" is the
  first-run hint gone after the first action; Manual "keep region" rows are the open drawer covering the page; "welcome
  not heard" after a pad, Hold, Manual or mic is the BASELINE rule 16 cut, settled in round 1.
- Missed: it has no PEAK/PITCH accuracy check, no blocked-permission (cross-origin iframe) run, and no network row in
  the report; I checked those by hand. Its 375x812 host is same-origin, so it never sees the site's no-mic state.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: voice-lab (Curiosity No. 03), round 1

Cold Craft lens, 2026-11-05. Judged against CODEX-CURIOSITY.md and the VISION "Curiosities" section, plus REFINE
Craft and the standard voice check. Bundle `tools/voice-lab/voice-lab.html` as built (not re-bundled). My frames and
run logs are in `S:/CurioClass-codex-scratch/voice-lab/craft/out/` (shots: perf.json, voice.json, keys.json,
keys2.json in the folder above it).

#### Contract (clean)

- One file, 77.7 KB (spec goal under 400 KB). The kit is inlined; no images, fonts or audio files.
- No network requests: `performance.getEntriesByType('resource')` is 0 after a 20 s run, and the bundle has no fetch,
  XHR, WebSocket or beacon. The only URLs are source links in the Manual.
- No console errors or exceptions in any of my 18 shots (the one 404 was the host page's own favicon).
- Kit used, not re-implemented: `Curio.voice`, `Curio.audio`, `Curio.init` wires Motion, Sound and Read.
- No em dashes; "Curio Class" everywhere; lesson-creep search (score, points, goal, sticker, badge, correct, wrong,
  try again, complete, well done) has no hits. No welcome screen, goal, score, finish or kit header.
- Privacy line is on the glass at every size and state, before and while the mic is on.

#### 60 fps (clean)

Frame cost measured in the page (time from frame start to the end of the tool's rAF work), headless Chrome with GPU
off, 240 frames each:

| Case | interval med / max | cost med / p95 / max | frames over 25 ms |
|---|---|---|---|
| 1366x768, Ah pad, Wide, 5 s | 16.7 / 16.8 ms | 1.1 / 2.2 / 3.1 ms | 0 |
| 1366x768, Ee pad, Narrow, 16 kHz, 20 s, harmonics, chart, A stored, history full (1200) | 16.7 / 16.8 | 1.4 / 2.3 / 3.2 | 0 |
| same, then Hold | 16.7 / 16.8 | 1.2 / 2.2 / 2.4 | 0 |
| 1920x1080, Narrow, chart | 16.7 / 16.8 | 1.3 / 2.5 / 3.3 | 0 |

The only hitch: a full repaint after a ruler change (Scale click) costs one 17 ms frame (one dropped frame); a Colour
click costs 8.8 ms. Even at four times slower this is one short hitch, not a stall. Motion off draws in steps at
about 8 fps (audit calm row clean).

#### Findings

1. **should fix** (general). Ribbon focus ring is invisible. `src.html:27` `#glass{overflow:hidden}` clips the
   `:focus-visible` outline (offset 2px) of `#ribbon`, which fills the glass. The ribbon is the first Tab stop and
   Hold moves focus to it on purpose (`toggleHold`, line 608), so a keyboard user holding and measuring never sees
   where focus is. Seen: `craft/out/k-tab1.png` (activeElement = ribbon, no ring) and `k-hold.png`. Better: an inset
   outline (`outline-offset:-3px`) or a ring drawn on the glass.

2. **should fix** (family:curiosity). The vowel chart hides the live edge of the instrument. The panel sits over the
   right of the ribbon (`src.html:34`, spec-placed), which is exactly where "now" enters: at 1366x768 it covers about
   the newest 5 s at a 20 s sweep, the harmonic markers (drawn at the right edge, lines 703-708; with Harmonics on and
   the chart open, the 1x to 10x ticks are under the panel), and the Hold crosshair at its default 0.98 position. At
   680x425 it covers the whole ribbon. Seen: `craft/out/perf-stress.png`, audit `state-vowel-held-1366x768.png`,
   `state-live-vowels-680x425.png`, `craft/out/k-vowels-375.png`. Better: put the chart over the oldest (left) part of
   the ribbon, or shrink the ribbon beside it, and move the harmonic ticks to the left of the panel when it is open.

3. **should fix** (general). The instrument does not fill the preview sizes. At 680x425 the glass plot is about 60 px
   tall: the ruler labels 4k and 3k touch, the hint sits on the grid lines and the deck takes over half the screen;
   at 800x500 about 170 px. This is the size the site shows beside "Play full screen". Seen: audit
   `size-680x425.png`, `size-800x500.png`. Better: in short boxes, fold the deck to one row (pads as a compact strip,
   Measure into the footer) so the glass keeps at least half the height, and drop to two ruler ticks when the plot is
   under about 120 px.

4. **should fix** (general). PEAK misreads low tones in Wide band. With the tone generator at 80 Hz PEAK reads 100 Hz
   (25 percent high), at 100 Hz it reads 98; 220 Hz and up are within a few hertz. The search starts at bin 1
   (93.75 Hz at 48 kHz, `src.html:588`) and the interpolation is clamped, so anything below about 140 Hz snaps
   toward bin 1. PITCH is right (80.0). Seen: `craft/out/k-tone` run log
   `[80, 80, "D#2 +49", 100], [100, 100, "G2 +35", 98]`. A deep voice's fundamental lives here. Better: show dashes for
   PEAK below about 1.5 bins in Wide, or take PEAK from the 4096-point tracker analyser.

5. **should fix** (general). The looped clips draw a fake event every 4 s. `makeBuffer` tapers 8 ms at both ends of
   each 4 s buffer (`src.html:461-462`), so every loop has a 16 ms dip that the spectrogram shows as a vertical
   broadband stripe, regular as a metronome. A student measuring with Hold can read it as part of the sound. Seen:
   `craft/out/perf-stress.png` (stripes at about -18.5, -14.5, -10.5, -6.6 and -2.6 s, Narrow, Ee). The harmonic clips
   already hold a whole number of cycles in 4 s (140 Hz and 280 Hz, 220 Hz recipes), so they loop cleanly without
   the taper; keep a crossfade only for the noise and glide clips.

6. **polish** (family:curiosity). Several controls are web-form controls, not instrument controls. Range, Sweep, Bank
   and Wave are drop-down `<select>`s (the spec asks for a range knob with detents and a sweep fader), and the input
   rotary is a round `<select>` with no pointer, so a click opens a browser list instead of turning. Keyboard and
   announcements work (Range and Sweep step with Left and Right, verified: `k-range` run gives 8000 and 20 and
   "Sweep 20 seconds"). Seen: every frame. Better: detent knobs or stepped faders drawn in the deck's metal, keeping
   the same keyboard paths.

7. **polish** (general). Linear, Wide and Ember show only the current position, so nothing on the panel says what
   pressing them gives (Musical, Narrow, Ice or Grey). Seen: `size-1366x768.png`. Better: two- and three-position
   switches with every position printed and the lit one marked.

8. **polish** (general). Pressing Live after Hold wipes the whole ribbon (`toggleHold` calls `clearHistory`,
   `src.html:609`); the Manual says only that Hold "freezes the ribbon". A student who held to compare two words loses
   the first one on release. Better: keep the history and resume scrolling, or say "Live starts a fresh sweep" in the
   Manual.

9. **polish** (general). The privacy line's dark box sits over the bottom-left of the ribbon (`src.html:31`), the
   0 to 400 Hz band where voice fundamentals and the 80 to 140 Hz tones are drawn, for about 360 px of older history.
   Seen: `craft/out/k-tone.png`, `perf-stress.png`. Better: put it in the readout strip or below the time axis.

10. **nit** (general). A tone above the Range (8 kHz on a 4 kHz ruler) leaves the glass blank while PEAK reads 8001 Hz;
    a small "above range" tick at the top edge would explain it. Seen: `craft/out/k-tone.png`.

11. **nit** (general). Much of the deck and chart text is 10 px (legends, switch labels, memory note, chart labels);
    readable at 1366x768, small for the grade 1 floor the spec claims. "A / B · volatile slices" is jargon; "A / B
    are kept until you close the tab" says it plainly.

#### Access (clean except 1)

- Tab order: ribbon, input, mic, gain, range, sweep, the four switches, bank, Stop, pads (`k-tab-pad`: the 13th Tab
  lands on "Ah adult, key Q" with a visible ring).
- Gain: Shift+Right +5, Up +1, Shift+Left twice to -4 dB, aria-valuetext "-4 decibels". Tone frequency: Shift+Up
  +1 Hz twice then Up one semitone to 468 Hz, valuetext "468 hertz". Input rotary: Left and Right reach TONE.
- Hold by Space: focus moves to the ribbon, arrows move the crosshair, the label reads "CURSOR -0.58 s · 960 Hz.
  Arrows move the crosshair. Space returns to live." and the live region reads the same with pitch and note.
- Targets are 44 px or more everywhere (CSS minimum on button, input, select). Colour is never the only signal:
  A solid and B dashed with text labels, vowel groups by shape, the level meter by position.
- Contrast: lowest text pairs are #a9b9b1 and #b9c8c0 on #07090b to #292d30, all well above 4.5:1.

#### Lines and voice

`voice/lines.json` holds the two fixed lines and `allLines()` returns the same two, word for word. Read is dynamic
(input, pitch, note, held cursor), as the spec asks. No art tokens (prompts.json is empty with a reason).

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| "Press the mic switch, then say ahhh." (first tap on the glass) | how (welcome) | once | once, at 0.15 s after the tap |
| "No mic here. Press a sound pad." (mic x5, 3 s apart) | how | once, then silent | spoken 1, silent 1, then nothing queued |
| Read, first tap | read | the hint only | the hint only |
| Sound, first tap | none | nothing | nothing |
| A pad, first tap | none | nothing (pad starts sound; hint hides) | nothing |
| Read with Sound off, live then held | read | spoken | "Built-in sounds. Pitch 140 hertz. C sharp 3." then the same plus "Held. Cursor 0.10 seconds back, 1600 hertz." |

Stale lines: glass, Scale, Mic, a pad, Read, Stop at 0.2 s gaps: the hint, then the fallback, then Read's status,
in action order; nothing played after its moment (the fallback started before the pad tap and is not re-queued).
Mic then a pad 0.2 s later: the fallback is not repeated and the hint is hidden. Read during the welcome cut it and
spoke the hint. Order kept in every run. Nothing to report.

#### Audit pilot

- Leads confirmed: the ribbon covered at 680x425 with the chart open (finding 2); the narrow preview (finding 3, from
  the frames, not a row).
- Leads wrong: the "#ribbon overlaps #status/#hint/#privacy/glass-label" rows are overlays on a canvas by design
  (except the privacy box, finding 9). "count and word disagree: 1 dBFS" is a misparse of "-13.1 dBFS". "hint out of
  view" in every state is the hint correctly gone after the first action. The Manual rows (ribbon and controls
  covered, links cut by a scroll panel) are a modal drawer that scrolls, as intended. "Welcome not heard" after a
  pad, Hold, Manual or the mic is BASELINE rule 16; the hint's job is done by then (a pad makes sound, the mic gives
  its own fallback line), and Read still speaks status.
- Missed: the invisible ribbon focus ring (finding 1); the chart hiding the harmonic markers and the "now" edge at
  1366x768 (finding 2); the PEAK error below 140 Hz (finding 4); the 4 s loop stripes (finding 5); Live wiping the
  ribbon (finding 8). It also cannot measure frame cost; the table above does.

Counts: 0 blocker, 5 should fix, 4 polish, 2 nit.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: voice-lab (Curiosity No. 03)

Cold Play lens, 2026-11-05. Judged against CODEX-CURIOSITY.md and VISION.md "Curiosities: the second shape", plus
POLISH.md. Played as a grade 8 student alone at home (and a first grader poking), and as a teacher projecting.
Own frames: `S:/CurioClass-codex-scratch/voice-lab/play/` (p01 to p19). Shared audit: `S:/CurioClass-codex-scratch/voice-lab/audit-r1/`.
Headless Chrome has no microphone, so MIC was judged from the code and the refused path only.

#### Short test

- **Would a kid open it unassigned?** Yes with a microphone: seeing your own "ahhh" turn into a stack of stripes is the
  hook, and it needs nothing read. Without a mic (the site's embed, many school Chromebooks) it is a bank of steady
  four-second drones; still good, but much less pull (see F1, F9).
- **Would an adult play for fun?** Yes. Narrow-band harmonics, the clarinet's missing even harmonics (p03), the log ruler
  and the child-versus-adult vowel shift (p19) are real things an adult enjoys finding.
- **Is the real thing the interface?** Yes. The ribbon is real FFT data at 48 kHz, the readouts are live, and no
  painted art sits in the way.
- **Does it work with no finish line?** Yes. No score, goal, level, sticker, finish screen or vowel target anywhere
  (searched src.html; the only "level" hits are the dBFS meter).

Passes all four, so no blocker. The risks are in the first two minutes without a mic and in readouts that go blank.

#### Findings

**F1. Embedded view tells the student to do something that cannot work.** should fix, family:curiosity
- Where: first screen in the site iframe; `src.html:122` hint, `toggleMic` at 368.
- What: the tool page iframe has no `allow="microphone"` (checked: host iframe has no allow attribute, p15), so every
  first-time student on the site is told "Press the mic switch, then say ahhh.", presses it, and only then hears
  "No mic here." The spec's open question leaves the template alone, which is fine, but the tool can know up front
  (`document.permissionsPolicy?.allowsFeature('microphone')` / `featurePolicy`) and open on the fallback hint, ideally
  naming Play full screen for the mic.
- How: p15-iframe-first.png; p12-mic-refused (fallback only after the press).

**F2. The big MIC knob is not the mic switch.** should fix, general
- Where: INPUT module, `src.html:131` (rotary is a styled `<select>`) beside the small MIC rocker at 132.
- What: the hint says "Press the mic switch". The eye goes to the large round knob labelled MIC; clicking it opens a
  plain browser drop-down (MIC / CLIPS / TONE) and nothing happens. The actual switch is the small rocker also labelled
  MIC. Two controls both reading MIC, and the wrong one is the obvious one. Better: label the rocker "MIC ON/OFF" (or
  light it) and make the knob a real rotary that steps on click instead of a drop-down.
- How: p13-rotary-click.png.

**F3. PITCH goes blank on whistles, including the tool's own whistle pad.** should fix, general
- Where: `yin()` at `src.html:506` (50 to 1,000 Hz limit).
- What: the built-in whistle glides 680 to 1,120 Hz; PITCH and NOTE drop to dashes for about a third of every loop
  (logged: `0/1050 0/1076 0/1095 ...`). Real whistles sit around 1 to 3 kHz, so "whistle a tune" (spec Things to do 2)
  will show dashes almost the whole time. The generator does the same above 1 kHz (1500 Hz: PITCH dashes, PEAK 1500).
  Better: extend the pitch range to about 4 kHz, or fall back to PEAK for a clean single line.
- How: p02-whistle-pitchlog.png and its log; p11-tone-sweep log.

**F4. F1 / F2 readout is dead in live play.** should fix, family:curiosity
- Where: `updateReadouts()` at `src.html:631` (`state.held&&f?.f1`).
- What: while a vowel plays, the internal estimate is good (ah 710/1100, oo 280/830, child ee 310/3130) and the chart
  cross moves, but the readout strip shows "··· / ···" until Hold is pressed. A student saying "eee, ahh, ooo" sees
  one of five readouts never change and reads it as broken. The spec meant "while a voiced sound is held" as sustained,
  not the Hold pad. Better: show the live estimate (it is already smoothed at 65 ms) and let Hold freeze it.
- How: p06 log (`··· / ···` with current f1 710, f2 1100); p06 and p19 frames.

**F5. Releasing Hold wipes the ribbon.** should fix, general
- Where: `toggleHold()` at `src.html:609` (`else clearHistory()`).
- What: Hold, measure, press Live: the whole picture is gone and starts from empty (history 12 frames right after).
  A teacher who froze a word to point at it loses the context the class was looking at; a student cannot hold, check,
  then compare with the next word. A real analyser resumes scrolling. Better: keep history and let the gap show.
- How: p07-hold-then-live log.

**F6. Vowel chart sits over the newest sound.** should fix, general
- Where: `#vowels` at `src.html:34` (right edge), and the 680x425 rules at 104.
- What: time enters at the right, so the chart covers the live edge: at 1366x768 the last 1.3 s, at 680x425 almost the
  whole ribbon (the ribbon is about 70 px tall there and the chart fills it, 7 of 9 points covered). Saying a vowel
  while watching the chart means not seeing it arrive. Better: dock the chart over the left (oldest) side, or let the
  ribbon shrink beside it.
- How: state-vowel-held-1366x768, state-live-vowels-680x425 (audit, confirmed), p06, p19.

**F7. Hold plus a pad press plays sound but nothing moves.** nit, general
- Where: `playPad()` at `src.html:466`.
- What: with Hold on, pressing a pad lights it and plays it, status reads "CLIPS / HOLD", and the ribbon stays frozen.
  A kid thinks the pad is broken. Better: a pad press returns to Live.
- How: p14-hold-pad-press log ("CLIPS / HOLD | true").

**F8. A/B outlines are hard to read.** polish, general
- Where: memory drawing at `src.html:710-720`.
- What: both outlines are squeezed into the left 30 percent of the glass, on top of the ribbon, on top of each other,
  and the "A spectrum / B spectrum" labels sit across the outlines. Clarinet versus flute (p03) and sss versus shh
  (p18) are the comparisons the pads invite, and they are the hardest thing on screen to read. Better: a darker
  backing panel, wider plot, and the labels outside the traces.
- How: p03-instruments-AB.png, p18-sss-then-shh.png.

**F9. Without a mic, nothing moves but the whistle and siren.** polish, family:curiosity
- Where: `makeBuffer()`, voice bank.
- What: every vowel pad is one steady vowel on one pitch, looped. The spec's best moments ("eee then ooo makes the
  bands jump", "slide your voice and every stripe climbs together", rhyme and two-speaker compares) all need a mic.
  More real material, not a game: a pad that glides ee to ah to oo, and one that slides an "ahh" up an octave, would
  give the no-mic student the same reaction.
- How: p06 (switching pads by hand is the only way to see bands jump).

**F10. The privacy line covers the bottom-left of the data.** polish, general
- Where: `#privacy` at `src.html:31`.
- What: it must stay visible (Done when 2), but it sits over 0 to 300 Hz on the oldest part of the ribbon, where the
  first harmonic and F1 live, and under the A/B traces. Better: put it on the time axis row or in the readout strip
  once a sound is running.
- How: p03, p06, p19, audit vowel-held overlap rows.

**F11. Projected, the numbers are small.** polish, general
- Where: `.readout output{font-size:19px}` and 10 px deck labels, fixed at every size.
- What: at 1920x1080 the readouts stay 19 px and the deck legends 10 px; from the back of a room PITCH and NOTE, the
  two numbers a teacher points at, are hard to read. Better: scale readouts with the viewport (clamp to about 32 px).
- How: audit size-1920x1080.png.

**F12. The chord reads "C2", a note not being played.** polish, family:curiosity
- Where: C major pad; PITCH 65.5 Hz, NOTE C2 +4 (p04).
- What: this is real (C4, E4, G4 repeat together every C2 period), but with no word it looks like an error. Manual
  says pitch is unreliable for chords. Better: turn it into a "Things people have found" entry (the shared period of a
  major chord), which is exactly the kind of depth a month of use should find.
- How: p04-chord-log.png.

**F13. Singing against the tone is gone.** polish, family:curiosity
- Where: `selectInput()` releases the mic in TONE (spec open question, lean taken).
- What: spec Things to do 10 (sing until your PITCH matches 440 Hz) cannot be done: TONE turns the mic off. The lean
  avoids feedback, fair, but the activity is a good one. Possible later: in MIC mode a quiet reference line at a chosen
  frequency drawn on the glass (no sound out) to sing onto.
- How: code read, `src.html:359-366`, 368-371.

**F14. NOTE says +1 cent beside PITCH 440.** nit, general
- Where: tone at 440 Hz: PITCH "440 Hz", NOTE "A4 +1 ¢" (state-tone-1366x768, p11 log).
- What: two readouts of the same number disagree by rounding; a student tuning to 440 sees "+1" and keeps nudging.
  Done when 4 still passes.

#### Checked and fine

- No welcome screen, goal, score or finish; the first-run hint is one quiet line, gone on first audio, and Read speaks
  the live state (code read; audit row 0).
- Wide versus Narrow on the same vowel visibly differ (state-narrow-memory: bands, then harmonic lines with 1x to 10x
  markers on them). Clarinet odd harmonics strong, even weak (p03). Child ee band higher than adult ee (p19).
- Tone tracking 80 to 1,000 Hz correct (80.0, 110, 440, 1000); 20 and 40 Hz show dashes honestly.
- 20 s sweep at 16 kHz range: frame median 16.8 ms, p95 17.6 ms (p09, headless, no GPU). No freeze.
- Motion off keeps time (audit clean; code steps the draw at 125 ms, sampling unchanged).
- Manual drawer and plate lower-left at every size, power panel beside them (audit frames).
- Mic refused: CLIPS selected, fallback line shown and spoken, pads work (p12).

#### Audit pilot

- Leads confirmed: the vowel chart covering the ribbon at 680x425 and 375x812 (F6); the privacy line over the glass
  (F10); the cramped ribbon at 680x425.
- Leads wrong or harmless: "#ribbon overlaps #status/#hint/#privacy/glass-label" at every size is by design (labels on
  the glass). "hint out of view" in every state is the hint correctly gone after the first sound. "count and word
  disagree: 1 dBFS" is the "-13.1 dBFS" readout, not a count. Manual "choices cut short by a scroll panel" is the
  sources list in a scrolling drawer, fine. Welcome "not heard" after a pad tap is BASELINE rule 16.
- What it missed: F2 (the knob is a drop-down), F3 (pitch blank on whistles), F4 (F1/F2 dead live), F5 (Live wipes
  the ribbon), F1 (the iframe has no mic permission, so the first hint fails on the site), F8 (A/B unreadable), F12.
- Harness note: drive.py's `wait` does not advance requestAnimationFrame in a background headless tab, so ribbons in
  frames reflect time spent in `js`/`after`, not the wait. Frames that need a long ribbon should wait inside `after`.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Refine lens: Teaching, voice-lab (Curiosity No. 03), round 1

Judged against docs/agents/CODEX-CURIOSITY.md and VISION.md "Curiosities: the second shape", not lesson norms.
Frames: `S:/CurioClass-codex-scratch/voice-lab/teaching/out/` (my own, 1366x768, drive.py on port 9741) plus the
shared audit at `S:/CurioClass-codex-scratch/voice-lab/audit-r1/`. Measurements saved as `tones.json`,
`vowels.json`, `peaknarrow.json` in `S:/CurioClass-codex-scratch/voice-lab/teaching/`.

#### Findings

1. **blocker** (general). `src.html:588-591`, PEAK readout in Wide band (the default). In Wide, PEAK reports the
   wrong frequency for any low tone and states it to the whole hertz. A 100 Hz sawtooth reads PEAK 47 Hz while PITCH
   reads 100 Hz and the ribbon's brightest line sits at 100 Hz. A sine at 80 Hz reads 56 Hz, a sawtooth at 147 Hz
   reads 163 Hz, and a 100 Hz square wave reads 82 Hz. The adult "Ee" pad's PEAK jumps between 228 and 301 Hz each
   frame when the strongest harmonic is at 280 Hz. Cause: the peak search runs on the 512-point Wide FFT
   (93.75 Hz bins at 48 kHz), starts at bin 1, and the parabolic offset is clamped to half a bin, so anything under
   about 190 Hz falls onto bin 1 ± 0.5. In Narrow every case is right to 1 Hz (30, 55, 80, 100, 147 and 220 Hz, sine
   and sawtooth). The brief counts a readout that lies as a blocker, and Things to do 11 ("sweep the generator from
   20 Hz upward") sends students straight into this range. The Manual's bin-spacing note does not excuse a readout
   that shows whole-hertz precision. Better: always take PEAK from `tracker` (the 4096-point analyser that already
   exists), or show dashes or a "±47 Hz" band when the Wide bin is too coarse. How seen: `tones.json`,
   `peaknarrow.json`, frame `out/saw100-wide.png` (PITCH 100 Hz beside PEAK 47 Hz).

2. **should fix** (family:curiosity). Module code MS-PS4-1, amplitude and energy. The anchor's code asks students to
   model "how the amplitude of a wave is related to the energy in a wave". The tool exercises frequency well (PITCH,
   NOTE, harmonics, the ruler), and it lets students change amplitude (OUTPUT fader, GAIN, LEVEL in dBFS). But
   nothing on the glass, in the readouts or in the Manual ever links amplitude to energy, and the only amplitude
   units are decibels, which a grade 8 student cannot turn into "twice the amplitude". So half the code is only
   implied. The fix is more real material, not a task: for example, a linear amplitude readout next to OUTPUT
   (×0.13, ×0.25) with relative energy (amplitude squared), and a Manual "Things people have found" entry such as
   "6 dB up is twice the amplitude and four times the energy." A small oscilloscope trace of the current input would
   also make "wave pattern" visible. Right now the sine, triangle, square and sawtooth switch is seen only as a
   spectrum, never as a wave shape. MS-PS4-2 is honestly declared untaught, and this is a second card (spec Map,
   notes.md), which is right. How seen: code read of every readout and Manual paragraph, plus the
   `data/modules.csv:619` codes.

3. **polish** (family:curiosity). The vowel chart (`src.html:634-664`, frame `out/ee-oo-chart.png`). The legend
   reads "○ men □ women △ children", and only the men's points carry vowel names. Nothing visible on the chart says
   these are 1952 American English averages. The spec's honesty note ("other accents and languages sit elsewhere,
   and that is not wrong") lives only in the Manual and the aria-label. A student who sees their cross land away
   from a dot will read the dot as the target, which is the "correct vowel target" that Done when 11 forbids in
   spirit. Better: a second legend line, "Peterson and Barney 1952, US English averages", and vowel names on all
   three groups (or on the men's set only, with that said in the legend).

4. **polish** (general). `src.html:685` sets the Musical (log) ruler ticks at decimal hertz (20, 50, 100, 200, 500,
   1k). The Manual says "each octave gets equal room", but the ruler never shows an octave. Octave ticks (C2 to C8,
   or 55, 110, 220, 440, 880 Hz) would let a student see the equal spacing that the doubling rule predicts, and see
   the C major chord's 4-then-3-semitone gap that the Manual describes. How seen: frame `out/chord-log.png`.

5. **polish** (general). The whistle and PITCH. YIN is capped at 1,000 Hz (`src.html:506`). The Whistle pad glides
   from 680 to 1,120 Hz, and PITCH shows dashes for the top half of each glide (from 1,000 to 1,127 Hz,
   `out/whistle.png` run). Most real whistles sit at 1 to 3 kHz, so for Things to do 2 PITCH will mostly be blank,
   while the spec's first-two-minutes text promises "the PITCH readout follows the voice note by note". Better:
   raise the PITCH ceiling for a clean single line (a whistle is the easiest pitch there is), or add one Manual line
   saying a whistle usually sits above the PITCH range, so read PEAK.

6. **polish** (general). Whisper loudness (`src.html:430-442, 458-459`). Every clip is normalized to the same peak,
   so "Whisper ah" plays and draws louder and brighter than voiced "Ah adult" (LEVEL −16 vs −13 dBFS, and the ribbon
   fills top to bottom with noise). A real whisper is far quieter than a voiced vowel. Side by side
   (`out/whisper-vs-ah.png`), the vowel bands do survive, which is the point of Things to do 4. But the frame also
   teaches "a whisper is stronger everywhere", which is false. Better: scale the whisper about 15 to 20 dB below the
   voiced vowels, and band-limit its noise floor so the three resonances stand out.

7. **polish** (general). Wide-band bandwidth. The spec calls for about 300 Hz. A 512-point Blackman at 48 kHz is
   about 160 Hz (about 145 Hz at 44.1 kHz), so on the adult "Ah" (140 Hz pitch) Wide still shows half-resolved
   harmonic stripes inside the formant bands (`out/ah-wide.png`), rather than the classic smooth vowel bands
   phoneticians read. Done when 5 still passes, because Wide and Narrow clearly differ (`out/ah-wide.png` against
   `out/ah-narrow-harm.png`). A 256-point Wide window would match the convention the Manual teaches.

8. **polish** (family:curiosity). Spec Things to do 10 ("sing until your PITCH matches the 440 Hz tone and the two
   lines merge") cannot be done. Choosing TONE releases the mic, and turning the mic on stops the tone
   (`src.html:361-372`). This was the spec's own leaned choice against speaker feedback, and the Manual does not
   promise the activity, so it is not a lie. It is still one of the richest activities on the list. A "with
   headphones" path (mic and tone both live, monitor muted) would bring it back.

9. **polish** (general). The flute pad is labelled "A3 · 220 Hz" (`src.html:291`). A concert flute's lowest note is
   C4 (B3 with a B foot), so a flute cannot play A3. Violin and clarinet can. Using A4 for all three, or C4 or above
   for the flute, keeps "same note, different ladder" honest.

10. **polish** (family:curiosity). Activities with no mic-free path. Things to do 13 and 14 (rhyming pair, two
    people saying the same word), and the ela-k-rhymes-and-sounds reach, need the mic. notes.md says the site
    iframe still lacks `allow="microphone"`, so on the tool page's embedded preview the instrument always falls
    back to clips. Teaching impact: the ELA K reach is unsupported wherever the mic is blocked. Either add a
    word-pair clip or drop that reach until the mic is guaranteed. (The iframe change itself is the integrator's.)

11. **nit** (general). Pressing a pad labelled "Ah adult", "Ee adult" or "Oo adult" plays the men's averages
    (`src.html:415`), while the chart separates men and women. "Ah man" or a women's set would match the chart.

12. **nit** (general). A C major chord reads PITCH 65.5 Hz, "C2 +4 ¢" (`out/chord-log.png`). This is the chord's
    real common period (the missing fundamental), and the Manual says pitch is unreliable for chords. It would be a
    good "Things people have found" entry instead of something that looks like an error.

13. **nit** (general). With no pitch, `readNow` (`src.html:305-309`) drops a period: "Built-in sounds Held. Cursor
    ..." (inspect output, whisper run). This matters only for the screen-reader live region and Read.

Not flagged for sensitivity review: nothing cultural, Native or hard-history. The men, women and children groups
and the accent caveat are handled in the Manual's honest-edges paragraph.

#### Done when (teaching-relevant items tested)

- 1 No welcome screen: PASS (audit size frames, my frames). "Ribbon within 100 ms of mic on": not testable in
  headless Chrome without a mic device, not tested.
- 2 Privacy line before and while: shown on every frame. No fetch, XHR, WebSocket or beacon in `src.html` (grep).
  Network log: Craft's.
- 3 Mic refused leads to CLIPS: PASS (audit row #mic heard "No mic here. Press a sound pad."). All 16 pads in both
  banks played, with sane readouts (`vowels.json`).
- 4 PITCH within 1% from 80 to 1,000 Hz: PASS. 44 tones, sine, square, sawtooth and triangle at 55 to 1,000 Hz:
  worst error 0.57% (sawtooth at 700 Hz). NOTE names A4 at 440 Hz (+1 ¢ sine, +7 ¢ square).
- 5 Wide and Narrow differ: PASS (`out/ah-wide.png` against `out/ah-narrow-harm.png`). Harmonic markers 1× to 10×
  sit on the narrow-band lines.
- 6 Hold plus arrows reads any point: the cursor maths (`src.html:722-725, 808-811`) uses the same freqToY and sweep
  mapping as the ruler and time axis. Keyboard is Craft's.
- 11 No score, goal, level, sticker, finish or "correct" anywhere: PASS (grep of src.html). See finding 3 for the
  chart's implied target.
- 7, 8, 9, 10: Craft and Play.

#### Facts spot-checked (second source)

- All 27 Peterson and Barney values in the Manual and `refs` (F1/F2/F3 for ee, ah and oo, for men, women and
  children) match Iseli, Shue and Alwan 2007, JASA 121:2283, Table I, exactly. The CCRMA (Stanford) secondary table
  agrees on the men's rows and the ee and oo rows, but gives 590 and 680 Hz for women's and children's "ah" F1. Those
  are P&B's /ɔ/ values (an error on that page), so the tool is right.
- The synthesized vowels recover their own references through the tool's LPC: men's ah 710/1100 (ref 730/1090),
  ee 280/2270 (270/2290), oo 280/830 (300/870); children's ah 1110/1410 (1030/1370), ee 310/3130 (370/3200),
  oo 460/1125 (430/1170). The estimates are honest.
- Jongman, Wayland and Wong 2000, JASA 108(3):1252-1263, DOI 10.1121/1.1288413: confirmed. Peterson and Barney JASA
  24:175-184 and its DOI, and the YIN DOI, match the standard citations. A4 = 440 Hz under ISO 16:1975: correct.
- FFT bin spacing at 48 kHz: 48000/512 = 93.75 Hz and 48000/4096 = 11.72 Hz, as the Manual says. C4, E4 and G4 in
  the chord code are 261.626, 329.628 and 391.995 Hz (MIDI 60, 64 and 67 exactly). The thirds are 4 and 3
  semitones, as the Manual says, and the Manual correctly overrides the spec's "evenly spaced" claim. 140 Hz is
  C♯3 +18 ¢: correct.
- sss puts its peak higher than shh (about 6 to 7 kHz against 2.3 to 3.1 kHz, `out/sss-shh-8k.png`). This matches
  the Jongman et al. principle, and the Manual rightly says to use the 8 or 16 kHz range.
- The flute's range does not include A3 (finding 9).

#### Audit pilot

- Leads confirmed: none that bear on teaching. The "#ribbon overlaps #status, #hint and #privacy" rows are labels
  drawn on the glass, by design. "count and word disagree: '1 dBFS'" is a false lead (a LEVEL value like −13.1).
- Leads that were wrong or not teaching: "hint out of view" in every state is correct behavior. The first-run hint
  is meant to vanish after the first action (Curiosity rule). "Welcome not heard" after a pad tap is allowed by
  BASELINE rule 16.
- What it missed: every finding above. The audit cannot check whether a readout is true (the PEAK blocker needed a
  tone sweep against PITCH), whether a standard is exercised (amplitude and energy), or what a synthetic clip
  implies (whisper loudness, the flute range).

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: voice-lab (Codex fix, round 1)

Curiosity No. 03. Reproduced before editing, then checked the repaired instrument. All evidence paths below are relative to `_scratch/voice-lab/`.
Working folder: `S:\CurioClass-codex`. Writes stayed in this tool and its Scratch folder. No commits or edits to `refine.md` or `refine/`.

#### Blocker

1. FIXED. PEAK now always uses the independent 4096-point tracker. Before: Wide 80 Hz sine read 46.875 Hz and 100 Hz saw read 76.64 Hz. After: 79.94 and 99.98 Hz. Both bands agree within 0.08 Hz on 80/100/140/440 Hz; 20 Hz shows dots rather than a false precise value. Evidence: `before/observations.md`, `after/b1-peak.json`, `break/band-and-unresolved.json`.

#### Should fix

1. FIXED. Permissions Policy is checked before the first frame, including the featurePolicy fallback. A blocked iframe opens on CLIPS, the unchanged no-mic hint and a Play full screen note. The unavailable mic rocker is disabled; keyboard M also follows the fallback. Before/after: `before/s1-policy.png`, `after/s1-policy.png`, `after/s1-policy.json`.
2. FIXED. Live usable LPC estimates now appear with smoothing; Hold freezes them. Before: Ah measured 710/1100 but displayed dots. After: about 709/1105 live. Whisper, whistle, sine, hiss and silence clear estimates. Evidence: `before/observations.md`, `after/s2-formants.json`, `proof/formants-honesty.json`, `break/mic-release.json`.
3. FIXED. A concentrated high spectral line extends PITCH to 4 kHz without promoting noisy harmonics. Before: the whistle lost pitch above 1 kHz; after: zero blank samples out of 45, tracking through 1123 Hz. Clean tones 1500, 2000, 3000 and 3900 Hz also pass. Evidence: `before/s3-whistle.png`, `after/s3-whistle.json`, `proof/numbers.json`.
4. FIXED. The input rotary steps per click and has announced detents, arrows and 1/2/3 shortcuts; there is no browser dropdown. The separate rocker says MIC ON or MIC OFF. Evidence: `before/s4-input.png`, `after/s4-input.png`, `sizes/controls.json`, `break/keyboard-input.json`.
5. FIXED. The chart owns the right-hand width, and the ribbon, meter, harmonic ticks and cursor use the remaining width. Checked at 1366x768, 680x425 and 375x812. At 375 the ribbon ends at x187 and chart begins x191. Evidence: `before/s5-chart-{1366,680,375}.png`, matching `after/` frames, and `proof/phone-chart.png` plus its rectangles JSON.
6. FIXED. Steady harmonic buffers contain whole cycles and no taper. Noise, glides and the chord overlap the continuing tail with the head rather than fading to zero. Before: 4-second broadband stripes; after: none across a 20-second Narrow Ee sweep. Evidence: `before/s6-loop.png`, `after/s6-loop.png`, `break/loops-final.png`; numerical buffer edge/RMS checks in `proof/numbers.json`.
7. FIXED. Live resumes without clearing spectral history; input changes and mic off still clear it. Before: 87 frames to zero; after: 88 to 88 on release. Evidence: `before/observations.md`, `after/s7-history.json`, `after/s7-history.png`.
8. FIXED. Tone OUTPUT has linear AMP and relative ENERGY readouts, with an original sourced Manual explanation. At -12 dB: amplitude 0.251 and energy 0.0631; at -6 dB: 0.501 and 0.2512. This is the same waveform/duration relative to 0 dB, before analysis Gain, not calibrated room energy. Evidence: `proof/numbers.json`, `proof/tone-680.png`. MS-PS4-2 remains explicitly untaught in notes.
9. FIXED. Short landscape uses a single deck row and Measure in the footer. Glass height went from 117 to 224 px at 680x425, and 239 to 299 px at 800x500 (52.7% and 59.8% of viewport height). The frequency ruler uses two ticks below 120 plot pixels. Evidence: `before/s8-s9-size-{680,800}.png`, `after/s8-s9-size-{680,800}.png`, `sizes/default-{680,800}.png`.
10. FIXED. Ribbon focus uses an inset -3 px outline. First Tab and Hold focus remain on the visible glass. Before: +2 px clipped; after: visible inset ring. Evidence: `before/s10-focus.png`, `sizes/focus.png`, `sizes/focus.json`.

#### Polish accepted

1. FIXED. Chart caption names Peterson and Barney 1952, US English averages, and says names are on the men's set. Evidence: `proof/phone-chart.png`, `proof/large-readouts.png`.
2. FIXED. Musical ruler uses octave ticks from 27.5 through 14080 Hz, clipped to the selected range. Evidence: `proof/musical-chord.png`.
3. FIXED. Whisper has only filtered resonances and its peak is 18 dB below voiced vowels. RMS is about -34.8 dBFS versus Ah at -13.0; the three broad bands are visible without harmonic stripes. Evidence: `proof/whisper.png`, `proof/ah-wide.png`, `proof/numbers.json`.
4. FIXED. Wide FFT is 256, with RATE and Manual updated. At 48 kHz its bin spacing is 187.5 Hz and Blackman equivalent noise bandwidth about 324 Hz; Narrow is 4096. The same Ah visibly changes from bands to harmonic lines. PEAK stays on 4096. Evidence: `proof/ah-wide.png`, `proof/ah-narrow.png`, `static-checks.json`.
5. FIXED. All three instrument recipes and labels use C4, about 262 Hz, with integer-cycle buffer lengths. Evidence: `proof/ab-instruments.png` (clarinet PITCH 261.45, PEAK 262), `proof/numbers.json`.
6. FIXED. A/B outlines now have a dark backing, span 52% of the plot instead of 30%, and have labels outside their trace area. Evidence: `proof/ab-instruments.png`.
7. FIXED. The exact privacy sentence occupies its own row below the time axis, outside spectral data. Visible before input and during simulated mic input. Evidence: `sizes/default-680.png`, `proof/phone-chart.png`, `break/mic-release.json`.
8. FIXED. Readouts scale to 31.68 px at 1920x1080; deck and chart text are lifted where space allows. A/B says it is kept until the tab closes. Evidence: `proof/large-readouts.png`, its font measurement JSON, `break/layout-values.json` (readout boxes do not overlap).
9. FIXED with a factual correction to the requested wording. The Manual explains the near-C2 estimate as an approximate periodic pattern, not an exact common period. The equal-tempered ratios over C2 are 4, 5.039684 and 5.993228, not 4:5:6. Evidence: `proof/musical-chord.json`, `static-checks.json`; sources below.
10. FIXED. Range, Sweep, Bank and Wave are stepped faders in the deck, with click, keyboard and announced values. Evidence: `sizes/controls.png`, `sizes/controls.json`, `break/keyboard-sweep.json`.
11. FIXED. Linear/Musical, Wide/Narrow and Ember/Ice/Grey show every position with the active one underlined and lit. Evidence: `sizes/controls.png`, `proof/tone-680.png`.
12. FIXED. A pad releases Hold and keeps history. Held history 60 frames became 92 after playing the next pad; held=false. Evidence: `proof/hold-pad.json`, `proof/hold-pad.png`.
13. FIXED. Read keeps sentence stops with no pitch, including held empty history. Evidence: `voice/held.json`: “Microphone off. Held. Cursor ... No spectrum at this time.”
14. FIXED. The men's vowel pads say man; child pads retain their descriptive labels. Evidence: `proof/ah-wide.png`, `proof/phone-chart.png`.
15. FIXED. An out-of-range peak draws an above range marker at the top live edge. Evidence: `proof/tone-above.png`, JSON PEAK 7999.93 Hz on a 4 kHz ruler.

#### Settled calls

- Applied all severity/placement calls: fine PEAK independent of band; whistle extension; history retained; chart remains right-hand.
- Preserved the two fixed voice lines, first-action cancellation, TONE releasing the mic, no grading of vowels and no lesson flow.
- Audit overlaps between the canvas and its intended status/hint labels are judged as instrument labels, not accidental occlusion. Privacy was moved off the data.
- No new sound list, oscillator view, simultaneous mic/tone mode or site template edits. Those are the spec's open questions.
- Unattended choice: followed the proposed click-step controls, 256-point Wide window and mic-blocked CLIPS fallback. Corrected the proposed exact chord-period fact rather than repeating it.

#### Cheats tried

- Sweep simple tones, saw and square across the coarse Wide bins, then repeat in Narrow: PEAK remains independently measured. Unresolved 20 Hz returns dots. No score or pass condition exists.
- Feed a pure sine through a synthetic microphone stream: PITCH about 440 Hz, formants zero. Noise/whisper/silence also cannot retain a false vowel estimate.
- Rapid Hold/Live, pad switches, +/-20 dB gain, 16 kHz range, 20-second sweep and both ends of detents: state stayed finite and responsive. Sample+draw cost mean 1.08 ms, p95 3.5 ms on this machine; not a physical Chromebook claim.
- Sweep tone amplitude: displayed energy follows amplitude squared. Six dB gives 1.995x amplitude and 3.981x energy, rounded to about two and four. No assessment or skill claim is made by this readout.
- Evidence: `after/b1-peak.json`, `break/band-and-unresolved.json`, `proof/formants-honesty.json`, `break/mic-release.json`, `break/stress.json`, `proof/numbers.json`.

#### Voice walk

Held clicks were 0.12 s, spaced 2 s apart, as requested. Browser narration was checked through `__tool.vlog`; Chrome playback was muted by the runner.

| Line / kind | Expected | Observed |
| --- | --- | --- |
| First hint / first-action hint | Once | 1 spoken start; Read may stop it |
| No-mic fallback / how-to, five refused mic attempts | Once, then silent | 1 spoken, 4 silent |
| Read with Sound off | Speaks current state | Logged as read |
| Held silent Read | Proper stops, empty-history message | Logged as read |

The two fixed lines still equal `allLines()` word for word. No new narration was added. Evidence: `voice/hint.json`, `voice/refused.json`, `voice/held.json`.

#### The real material

No external audio, images, datasets, code or prose were downloaded or bundled in this fix. Existing numerical vowel facts and original synthesis remain.
All new explanatory wording is original. Current source pages were read on 2026-11-06; gathering was under 45 minutes.

- Amplitude/energy: [UNSW Decibels](https://www.animations.physics.unsw.edu.au/jw/dB.htm), independently checked against [Moebs, Ling and Sanny, OpenStax 17.3](https://openstax.org/books/university-physics-volume-1/pages/17-3-sound-intensity). UNSW copyright terms are at [its policy](https://www.unsw.edu.au/copyright-disclaimer). OpenStax currently states CC BY-NC-SA 4.0, not CC BY 4.0; only the physical fact was checked, no content copied. No restricted material was imported.
- C4 flute: [UNSW C-foot C4](https://phys.unsw.edu.au/music/flute/modernC/C4.html), independently corroborated by [Yamaha's C/B footjoint explanation](https://www.yamahamusiclondon.com/Woodwind/Flutes/Standard-and-Step-Up-Flutes/). Copyright UNSW and Yamaha respectively, facts checked only; no media/prose reproduced. C4=261.625565 Hz independently recomputed from A4=440.
- Chord periodicity: [UNSW Acoustics FAQ](https://phys.unsw.edu.au/jw/musFAQ.html) for equal temperament, and [de Cheveigné and Kawahara's YIN paper](https://www.ee.columbia.edu/~dpwe/e6820/papers/deChevK02-yin.pdf) for periodicity estimation. Copyright UNSW and ASA; references only, independently implemented mathematics. Ratios independently recomputed in `static-checks.json`.
- FFT/window: [W3C Web Audio](https://www.w3.org/TR/webaudio/), W3C Software and Document licence 2023. Browser API used; no source prose/code copied. Bin spacing and noise bandwidth independently computed from its Blackman definition.
- Existing chart/synthesis: Peterson and Barney 1952 factual averages; copyrighted paper, no open redistribution licence claimed. No new data copied or reference numbers changed. Existing corroboration and the rest of the signal-processing references remain in the Manual and `tool.draft.json`.
- Original code and synthetic audio: MIT. Original Manual explanations: CC BY 4.0. There is no newly sampled or packed external dataset, so no download/packing script was needed.

#### Engine changes wanted

No shared-engine edit was required. The existing handoff still names the site iframe microphone allow attribute and shared runner/label improvements. The site template is outside this fix's scope.

#### Audit

Audit not finished. The one final run used port 9911, host 8715 and the dedicated Scratch profile, with a hard 40-minute limit. It exited 1 before its first size snapshot: a Chrome DevTools domain-enable command timed out after the runner's internal 60-second wait (`Audit.tab`, `drive.Tab.send`). No audit.md or mechanical leads were produced, so none can be claimed clean. No second audit was run, as CODEX-FIX directs stopping after an unfinished audit. Details: `fix-audit/NOT_FINISHED.md`.

The independent drive.py batches completed with zero tool console errors, warnings or exceptions on the accepted repaired-state runs. Network evidence in `break/network.json` contains only the initial local HTML document for all eight shots: zero HTTP or other subresource requests. The bundle is 89,241 bytes. The required audit gate remains unverified despite those focused checks.

#### Lesson creep check

Source search found only six physical audio LEVEL/level occurrences, all explained as signal amplitude or meter values. Zero score, points, goal, sticker, badge, correct, wrong, quiz or finish flow was added. No em dash in src.html. Fixed voice lines contain no lesson creep.

#### Short test and frames looked at

The repair preserves the short-test answers: a child can press a pad and see a reaction; an adult can compare real spectra and measure them; sound is the interface; neither needs a score or finish. This was an instrument repair pass, not a new lesson or a new timed user study.

| Repaired instrument | Family model |
| --- | --- |
| ![Voice Lab](../../_scratch/voice-lab/proof/ab-instruments.png) | ![Beat Lab](../../_scratch/voice-lab/before/beat-lab.png) |

Inspected before/after frames, proof frames and all size/contact sheets. Default sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812. Also inspected Beat Lab, Elements Inspector and the two family-mark models. Focus, chart, both bands, both banks, TONE, Manual and Motion off have explicit frames.

#### Left open

- Site iframe permission, simultaneous reference-tone/mic activity, additional mic-free clips and an oscilloscope remain the integrator/spec open questions. Nothing outside the allowed folders was changed.
- The final mechanical audit did not finish; its gate remains open for the exit reviewer.
- Actual human microphone characteristics, audible installed voice quality and a physical school Chromebook remain hardware checks. A synthetic mic stream verified filter options, estimates, privacy and ended tracks on release.
- The instrument intentionally declines precise PEAK values below its resolvable fine-FFT range; LPC remains an estimate and this is explained in the Manual.
- Initial stale-cache/overlapping runner captures were discarded as fix evidence. Fresh profiles and uncached host URLs were used for the accepted measurements. `before/observations.md` records the baseline and evidence-path correction.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Voice Lab / Build handoff

The source contains the instrument CSS, native keyboard controls, Manual, and original signal processing in one readable HTML file.
The shared kit supplies voice, Motion and Sound. All working plots are canvas, never painted data. Build followed by one cold review; no commits.

The audio graph keeps analyser and playback separate: MIC reaches only the analysis gain; CLIPS and TONE also reach the muted-by-Sound monitor.
Pitch uses YIN, formants use autocorrelation LPC with a 10 Hz envelope search. Spectral history retains per-frame bin spacing through band changes.
Hold stops acquisition, and returning to live clears time history to avoid inventing audio during the held gap. A/B store spectra in RAM.
Formant readouts are gated to microphone input and synthesized vowels. Generator, whistle, noise and instrument pads do not claim vocal-tract formants.
The YIN search includes shorter periods before rejecting pitches outside its 50 to 1,000 Hz reporting range, avoiding false low readings for high tones.

#### Spec resolutions

Two eight-pad banks expose all specified sounds plus silence. The chord uses accurate equal temperament; a major chord has unequal thirds on a log ruler.
FFT sizes follow the explicit 512/4096 requirement; the Manual gives bin spacing rather than claiming the approximate bandwidths are exact.
The privacy sentence is retained verbatim, with the temporary spectral-buffer exception made explicit in the Manual.
The first paragraph's pitch-axis shorthand is implemented as frequency: harmonics, noise and formants are all frequencies, not independent pitches.
Numerical formants follow the live smoothed estimate; the chart now follows the live measured estimate, satisfying both the readout rule and the concept's walking dot.
No save/load is specified, and no audio capture or export has been added.
The analysis deck now uses button-based detent sliders and gain/frequency faders. Each detent exposes its value and spoken label.
Left/Right and Up/Down step, Home/End reach the limits, and click/Enter/Space advances with wraparound.

#### Engine changes wanted

Shared site tool-page iframe: add allow="microphone" for this Curiosity, as the spec proposes. This file is outside the allowed write scope.
kit/curio.js showMotion and init: support a tool-supplied label formatter so rocker controls need not locally restore their plain labels after emoji insertion.
scripts/audit_tool.py drive_keys: support alphanumeric shortcuts such as 3; the initial audit stopped on this key.
The remaining audit stages were recovered in Scratch, without repeating the complete size sweep or editing the shared runner.
No shared files were changed.

#### Left open

See codex-report.md for measured checks and limitations. A physical school Chromebook and an actual human voice need hardware verification.
Browser-installed speech substitutes for the named bank recording because this build may not record audio.
LPC now rejects peaks with less than 2 dB prominence, removing the shallow 2,060 Hz bump previously mistaken for a child's ee second formant.
It still estimates sparse high-pitch voices imperfectly; reference values never replace measurements.
The microphone path rejects a near-pure sine with a second-order residual check; a silent frame clears pitch and formants immediately.

#### Cold review changes

Read follows the held cursor's actual frame, including an explicit empty-history response. The live chart uses measured formants;
its axes now match its coordinates, with a compact layout in short previews. Numerical formants now follow live estimates and freeze with Hold.
Sine recurrence speeds original buffer synthesis. Tone gain nodes disconnect on Stop, and the same pad becomes Start so a stopped tone can resume.
Space preserves native button activation. The source/permission notes distinguish facts and original synthesis from copyrighted publications.
The final audit exposed a stale first hint on Manual entry. Its validity now excludes the drawer and Hold, and input/Manual/Hold changes hush old speech.

#### Sensitivity

The historical American English groups are descriptive source categories, never targets or a way to infer gender, age, accent or ability.
The chart labels and synthetic child/adult approximations should be checked by a sensitivity reviewer in that light.

#### Refine round 1 repair details

PEAK and the high clean-line pitch extension use the independent 4096-point tracker, never the display FFT.
The unresolved bottom two tracker bins deliberately show dots. The Wide display is 256 points.
Live LPC values are smoothed only between usable estimates; noise and silence clear them rather than holding old formants.
Harmonic buffers use an integer number of cycles; noise, glides and the equal-tempered chord overlap the continuing tail with the head.
The whisper peak is 18 dB below the voiced pads. C4 instrument buffers choose their sample length to preserve whole cycles.
Hold to Live keeps spectral history; a sound pad releases Hold. Input changes and microphone-off still clear history.
The chart reserves its own right-hand width. Canvas coordinates, meter, harmonic markers and cursor use the remaining width.
In short landscape previews Measure moves into the footer and the deck stays in one row. The privacy sentence has its own row below data.
Tests and before/after evidence live in _scratch/voice-lab. No shared kit, site, scripts or review files changed.
The requested exact-C2 chord explanation was corrected: the equal-tempered tones do not have a short exact common period.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
