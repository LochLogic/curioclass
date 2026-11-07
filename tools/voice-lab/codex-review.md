# Codex review: voice-lab
## Played
Cold-played before reading the builder's report, notes, handoff or source. Grade-8 exploration and adult measurement perspectives; actual muted Chrome audio graphs, held clicks and inspected frames, not a recruited usability study.
Covered microphone refusal, both eight-pad banks, wide/narrow analysis, chart, generator, Hold, A/B and Manual. The original loaded build ran for 601.547 seconds with 192 actions and no runtime exceptions.
Short test, reviewer judgement: kid would reopen it YES; adult play YES; real sound is the interface YES; works without a score or finish YES. The chart's initially absent live response weakened the third answer; the measured live cross now makes it central.
| Voice Lab | Beat Lab comparison |
|---|---|
| ![Live measured vowel](../../_scratch/voice-lab/review/last-focus/chart-1366-fixed.png) | ![Beat Lab](../../_scratch/voice-lab/review/finish-play/beat-lab-model.png) |
The ribbon, rulers, LED meter and lower deck have the confidence and density of a real analyser. Kept them.
## Findings fixed
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
## Findings left
No confirmed implementation blocker or should-fix left. Hardware, listening and shared-site limitations are under Left open.
## Break it
No score, quiz, success meter or gated path exists. LEVEL is RMS signal amplitude in dBFS, not progression. Silence gives -60 dBFS and no pitch; gain cannot earn anything.
Lesson-creep search of source and voice lines found only four legitimate audio LEVEL/level occurrences; no rewards, goals, quizzes, finish screen, kit header or vowel targets.
Exercised gain -20/+20, amplitude -40/0, generator 20/8,000 Hz, all four ranges, four sweeps, four waveforms, both scales, both bandwidths, three maps, every pad, and repeated rapid toggles. Resized while sound was running.
Post-fix assertions: held/empty Read, native Space, Start after Stop, silence and generated tones 80/100/220/440/880/1,000 Hz all pass. All 94 independently generated sine arrays at 44.1/48 kHz stay within 1%; worst error 0.374%.
LPC on six synthetic vowels and multiple sample positions remains an estimate; child ee F1 can under-read. Invalid/non-vowel inputs do not acquire invented formant reference values.
Evidence: `../../_scratch/voice-lab/review/verified/results.json`, `virtual-mic-final.json`, `diagnostic/results.json` and inspected before/after frames. No runtime exceptions in the focused verification. The generated mic stream measured 220 Hz, requested all three speech filters off, and its track ended on mic off. This tests graph/lifecycle, not a physical microphone.
## Voice walk
Sound on, 120 ms held clicks, two-second pace: MIC -> refusal -> Read -> Ah -> Ee -> Oo -> Read -> Sound off -> Read -> Sound on. Then TONE, a held older slice and Read.
Initial log order: fallback hint once; "Built-in sounds"; "Built-in sounds. Pitch 140 hertz. C sharp 3."; the same explicit Read with Sound off; "Tone generator. Pitch 220 hertz. A 3. Held. Cursor 1.40 seconds back, 1600 hertz."
After the audit voice fix, repeated MIC -> refusal -> Ah -> Ee -> Read -> Sound off -> Read -> Sound on at the same pace. Fallback once, cut on starting input; both requested Reads reported the displayed 140 Hz C sharp 3. No late hint followed the sound.
| Line kind | Expected | Observed |
|---|---|---|
| Mic-free how-to | Once, then quiet | Once |
| Automatic teaching or mode narration | None for this Curiosity | None |
| Explicit Reads | Each requested, current state | All logged in order |
Manual-first now logs no speech; Hold-first plus Read reports empty history. Rapid band -> Manual cuts the hint with `manual`; band -> Ah cuts it with `input`. No unsolicited line follows. Evidence: `../../_scratch/voice-lab/review/voice-audit-fix/` and the five matching JSON logs one directory above. Browser speech fallback was logged; muted testing cannot certify audible delivery or the specified recorded voice.
## Facts checked
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
## Sensitivity
Human voices/bodies and historical American English categories: a sensitivity reviewer should check the source's men/women/children labels and synthetic examples. They are descriptive historical groups, never pronunciation targets or ways to infer gender, age, accent or ability. No people images or diagnosis claims.
## Flattest moment left
Synthetic sounds have less character than recorded instruments. Kept the honest synthetic launch specified by the brief. The former flat live chart now responds directly to the sound, and first pad generation is faster.
## Graphics
No painted images or missing art tokens. Inspected 65 frames, including all 20 audit frames, the real spectrum, rulers, chart, meter, Manual and deck at all eight sizes, grayscale and Motion off. No kit header or lesson layer was added. Frame list: `../../_scratch/voice-lab/review/final-manifest.json`.
Computed text contrast: readouts 15.37:1; controls 9.92:1; deck labels 7.99:1; active pads 8.64:1; plate 7.13:1. Audit found no small targets, clipped text, horizontal scroll or focus failure.
Final bundle: 77,665 bytes (75.8 KiB), below the 400 KB spec budget. SHA-256: `e7e40e312edff168c8e2d368b5018c1a72e8ac66acde44286bdf1dd707fba793`. Evidence stays in the two authorized folders; no commits.
## Audit
Ran the unmodified audit functions once, last, through `../../_scratch/voice-lab/review/audit_bounded.py`, with an outer 2,400-second cap; completed. Chrome 9941, host 8745. Full evidence: `../../_scratch/voice-lab/review-audit/audit.md`.
74 mechanical leads: 65 frame leads are intentional canvas/status/privacy/chart or modal overlays, the deliberately dismissed hint, and scrollable Manual references; nine missing-welcome flags are intentional first-sound/fallback behaviour for a Curiosity. Every line has a disposition in `../../_scratch/voice-lab/review/audit-dispositions.json`.
All 24 walked controls had no runtime/focus failure; five-click repeats and rapid taps were clean. All listed-state and walked-control resize stress finished without exceptions or stuck controls. The Manual row also revealed the real stale-hint flaw, fixed afterward as required, with only the affected voice paths rechecked. Raw audit predates that final voice-only fix; no second full audit or polish pass.
All assigned Chrome ports 9940-9947 and host 8745 were verified closed after the last focused check. No tool-folder host.html remains.
## Left open
- Physical microphone onset under 100 ms, audible playback/speech quality and 60 fps on an actual school Chromebook require hardware checks. Desktop evidence is not a substitute.
- Embedding requires `allow="microphone"`; the shared iframe permission was not verified or changed in this scoped review. Standalone access and mic-free pads are the specified fallback.
- The named news-reader recording is absent; installed browser voices remain the build's explicit fallback. No recording or external service was invoked.
- Unattended choices followed the brief: live chart plus held numeric values; original synthetic sounds; no lesson rewards or goals. Left the spec's file untouched.
