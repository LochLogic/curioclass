# Polish: voice-lab (Codex fix, round 1)

Curiosity No. 03. Reproduced before editing, then checked the repaired instrument. All evidence paths below are relative to `_scratch/voice-lab/`.
Working folder: `S:\CurioClass-codex`. Writes stayed in this tool and its Scratch folder. No commits or edits to `refine.md` or `refine/`.

## Blocker

1. FIXED. PEAK now always uses the independent 4096-point tracker. Before: Wide 80 Hz sine read 46.875 Hz and 100 Hz saw read 76.64 Hz. After: 79.94 and 99.98 Hz. Both bands agree within 0.08 Hz on 80/100/140/440 Hz; 20 Hz shows dots rather than a false precise value. Evidence: `before/observations.md`, `after/b1-peak.json`, `break/band-and-unresolved.json`.

## Should fix

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

## Polish accepted

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

## Settled calls

- Applied all severity/placement calls: fine PEAK independent of band; whistle extension; history retained; chart remains right-hand.
- Preserved the two fixed voice lines, first-action cancellation, TONE releasing the mic, no grading of vowels and no lesson flow.
- Audit overlaps between the canvas and its intended status/hint labels are judged as instrument labels, not accidental occlusion. Privacy was moved off the data.
- No new sound list, oscillator view, simultaneous mic/tone mode or site template edits. Those are the spec's open questions.
- Unattended choice: followed the proposed click-step controls, 256-point Wide window and mic-blocked CLIPS fallback. Corrected the proposed exact chord-period fact rather than repeating it.

## Cheats tried

- Sweep simple tones, saw and square across the coarse Wide bins, then repeat in Narrow: PEAK remains independently measured. Unresolved 20 Hz returns dots. No score or pass condition exists.
- Feed a pure sine through a synthetic microphone stream: PITCH about 440 Hz, formants zero. Noise/whisper/silence also cannot retain a false vowel estimate.
- Rapid Hold/Live, pad switches, +/-20 dB gain, 16 kHz range, 20-second sweep and both ends of detents: state stayed finite and responsive. Sample+draw cost mean 1.08 ms, p95 3.5 ms on this machine; not a physical Chromebook claim.
- Sweep tone amplitude: displayed energy follows amplitude squared. Six dB gives 1.995x amplitude and 3.981x energy, rounded to about two and four. No assessment or skill claim is made by this readout.
- Evidence: `after/b1-peak.json`, `break/band-and-unresolved.json`, `proof/formants-honesty.json`, `break/mic-release.json`, `break/stress.json`, `proof/numbers.json`.

## Voice walk

Held clicks were 0.12 s, spaced 2 s apart, as requested. Browser narration was checked through `__tool.vlog`; Chrome playback was muted by the runner.

| Line / kind | Expected | Observed |
| --- | --- | --- |
| First hint / first-action hint | Once | 1 spoken start; Read may stop it |
| No-mic fallback / how-to, five refused mic attempts | Once, then silent | 1 spoken, 4 silent |
| Read with Sound off | Speaks current state | Logged as read |
| Held silent Read | Proper stops, empty-history message | Logged as read |

The two fixed lines still equal `allLines()` word for word. No new narration was added. Evidence: `voice/hint.json`, `voice/refused.json`, `voice/held.json`.

## The real material

No external audio, images, datasets, code or prose were downloaded or bundled in this fix. Existing numerical vowel facts and original synthesis remain.
All new explanatory wording is original. Current source pages were read on 2026-11-06; gathering was under 45 minutes.

- Amplitude/energy: [UNSW Decibels](https://www.animations.physics.unsw.edu.au/jw/dB.htm), independently checked against [Moebs, Ling and Sanny, OpenStax 17.3](https://openstax.org/books/university-physics-volume-1/pages/17-3-sound-intensity). UNSW copyright terms are at [its policy](https://www.unsw.edu.au/copyright-disclaimer). OpenStax currently states CC BY-NC-SA 4.0, not CC BY 4.0; only the physical fact was checked, no content copied. No restricted material was imported.
- C4 flute: [UNSW C-foot C4](https://phys.unsw.edu.au/music/flute/modernC/C4.html), independently corroborated by [Yamaha's C/B footjoint explanation](https://www.yamahamusiclondon.com/Woodwind/Flutes/Standard-and-Step-Up-Flutes/). Copyright UNSW and Yamaha respectively, facts checked only; no media/prose reproduced. C4=261.625565 Hz independently recomputed from A4=440.
- Chord periodicity: [UNSW Acoustics FAQ](https://phys.unsw.edu.au/jw/musFAQ.html) for equal temperament, and [de Cheveigné and Kawahara's YIN paper](https://www.ee.columbia.edu/~dpwe/e6820/papers/deChevK02-yin.pdf) for periodicity estimation. Copyright UNSW and ASA; references only, independently implemented mathematics. Ratios independently recomputed in `static-checks.json`.
- FFT/window: [W3C Web Audio](https://www.w3.org/TR/webaudio/), W3C Software and Document licence 2023. Browser API used; no source prose/code copied. Bin spacing and noise bandwidth independently computed from its Blackman definition.
- Existing chart/synthesis: Peterson and Barney 1952 factual averages; copyrighted paper, no open redistribution licence claimed. No new data copied or reference numbers changed. Existing corroboration and the rest of the signal-processing references remain in the Manual and `tool.draft.json`.
- Original code and synthetic audio: MIT. Original Manual explanations: CC BY 4.0. There is no newly sampled or packed external dataset, so no download/packing script was needed.

## Engine changes wanted

No shared-engine edit was required. The existing handoff still names the site iframe microphone allow attribute and shared runner/label improvements. The site template is outside this fix's scope.

## Audit

Audit not finished. The one final run used port 9911, host 8715 and the dedicated Scratch profile, with a hard 40-minute limit. It exited 1 before its first size snapshot: a Chrome DevTools domain-enable command timed out after the runner's internal 60-second wait (`Audit.tab`, `drive.Tab.send`). No audit.md or mechanical leads were produced, so none can be claimed clean. No second audit was run, as CODEX-FIX directs stopping after an unfinished audit. Details: `fix-audit/NOT_FINISHED.md`.

The independent drive.py batches completed with zero tool console errors, warnings or exceptions on the accepted repaired-state runs. Network evidence in `break/network.json` contains only the initial local HTML document for all eight shots: zero HTTP or other subresource requests. The bundle is 89,241 bytes. The required audit gate remains unverified despite those focused checks.

## Lesson creep check

Source search found only six physical audio LEVEL/level occurrences, all explained as signal amplitude or meter values. Zero score, points, goal, sticker, badge, correct, wrong, quiz or finish flow was added. No em dash in src.html. Fixed voice lines contain no lesson creep.

## Short test and frames looked at

The repair preserves the short-test answers: a child can press a pad and see a reaction; an adult can compare real spectra and measure them; sound is the interface; neither needs a score or finish. This was an instrument repair pass, not a new lesson or a new timed user study.

| Repaired instrument | Family model |
| --- | --- |
| ![Voice Lab](../../_scratch/voice-lab/proof/ab-instruments.png) | ![Beat Lab](../../_scratch/voice-lab/before/beat-lab.png) |

Inspected before/after frames, proof frames and all size/contact sheets. Default sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812. Also inspected Beat Lab, Elements Inspector and the two family-mark models. Focus, chart, both bands, both banks, TONE, Manual and Motion off have explicit frames.

## Left open

- Site iframe permission, simultaneous reference-tone/mic activity, additional mic-free clips and an oscilloscope remain the integrator/spec open questions. Nothing outside the allowed folders was changed.
- The final mechanical audit did not finish; its gate remains open for the exit reviewer.
- Actual human microphone characteristics, audible installed voice quality and a physical school Chromebook remain hardware checks. A synthetic mic stream verified filter options, estimates, privacy and ended tracks on release.
- The instrument intentionally declines precise PEAK values below its resolvable fine-FFT range; LPC remains an estimate and this is explained in the Manual.
- Initial stale-cache/overlapping runner captures were discarded as fix evidence. Fresh profiles and uncached host URLs were used for the accepted measurements. `before/observations.md` records the baseline and evidence-path correction.
