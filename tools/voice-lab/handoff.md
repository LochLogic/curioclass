# Voice Lab / Build handoff

The source contains the instrument CSS, native keyboard controls, Manual, and original signal processing in one readable HTML file.
The shared kit supplies voice, Motion and Sound. All working plots are canvas, never painted data. Build followed by one cold review; no commits.

The audio graph keeps analyser and playback separate: MIC reaches only the analysis gain; CLIPS and TONE also reach the muted-by-Sound monitor.
Pitch uses YIN, formants use autocorrelation LPC with a 10 Hz envelope search. Spectral history retains per-frame bin spacing through band changes.
Hold stops acquisition, and returning to live clears time history to avoid inventing audio during the held gap. A/B store spectra in RAM.
Formant readouts are gated to microphone input and synthesized vowels. Generator, whistle, noise and instrument pads do not claim vocal-tract formants.
The YIN search includes shorter periods before rejecting pitches outside its 50 to 1,000 Hz reporting range, avoiding false low readings for high tones.

## Spec resolutions

Two eight-pad banks expose all specified sounds plus silence. The chord uses accurate equal temperament; a major chord has unequal thirds on a log ruler.
FFT sizes follow the explicit 512/4096 requirement; the Manual gives bin spacing rather than claiming the approximate bandwidths are exact.
The privacy sentence is retained verbatim, with the temporary spectral-buffer exception made explicit in the Manual.
The first paragraph's pitch-axis shorthand is implemented as frequency: harmonics, noise and formants are all frequencies, not independent pitches.
Numerical formants follow the live smoothed estimate; the chart now follows the live measured estimate, satisfying both the readout rule and the concept's walking dot.
No save/load is specified, and no audio capture or export has been added.
The analysis deck now uses button-based detent sliders and gain/frequency faders. Each detent exposes its value and spoken label.
Left/Right and Up/Down step, Home/End reach the limits, and click/Enter/Space advances with wraparound.

## Engine changes wanted

Shared site tool-page iframe: add allow="microphone" for this Curiosity, as the spec proposes. This file is outside the allowed write scope.
kit/curio.js showMotion and init: support a tool-supplied label formatter so rocker controls need not locally restore their plain labels after emoji insertion.
scripts/audit_tool.py drive_keys: support alphanumeric shortcuts such as 3; the initial audit stopped on this key.
The remaining audit stages were recovered in Scratch, without repeating the complete size sweep or editing the shared runner.
No shared files were changed.

## Left open

See codex-report.md for measured checks and limitations. A physical school Chromebook and an actual human voice need hardware verification.
Browser-installed speech substitutes for the named bank recording because this build may not record audio.
LPC now rejects peaks with less than 2 dB prominence, removing the shallow 2,060 Hz bump previously mistaken for a child's ee second formant.
It still estimates sparse high-pitch voices imperfectly; reference values never replace measurements.
The microphone path rejects a near-pure sine with a second-order residual check; a silent frame clears pitch and formants immediately.

## Cold review changes

Read follows the held cursor's actual frame, including an explicit empty-history response. The live chart uses measured formants;
its axes now match its coordinates, with a compact layout in short previews. Numerical formants now follow live estimates and freeze with Hold.
Sine recurrence speeds original buffer synthesis. Tone gain nodes disconnect on Stop, and the same pad becomes Start so a stopped tone can resume.
Space preserves native button activation. The source/permission notes distinguish facts and original synthesis from copyrighted publications.
The final audit exposed a stale first hint on Manual entry. Its validity now excludes the drawer and Hold, and input/Manual/Hold changes hush old speech.

## Sensitivity

The historical American English groups are descriptive source categories, never targets or a way to infer gender, age, accent or ability.
The chart labels and synthetic child/adult approximations should be checked by a sensitivity reviewer in that light.

## Refine round 1 repair details

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
