# Sound Studio

## One idea
Every sound is a sum of sine waves: you build one harmonic by harmonic and hear it, while a scope shows its pressure trace, a spectrum shows its frequencies as bars, and a tube of air shows compressions one wavelength apart, all changing together with v = f x wavelength worked live underneath.

## Not like
- sound-elevator (K-2, live): high and low pitch for little kids on eight floors. This is the physics: frequency in hertz, period, wavelength, wave speed in different media, harmonics and beats, with real units.
- beat-lab (9-12 arts, live): a music production studio for making tracks. Sound Studio makes one sound at a time and measures it; no sequencer, no songs, no mixer.
- chord-explorer (6-8 music, live): stacks notes into chords for harmony. Here the unit is not a note but a sine wave and its frequency.
- spectrum-explorer (grade 11, concept): electromagnetic waves across the spectrum. Sound Studio is mechanical pressure waves only, which need a medium, and shows wave speed changing with the medium.
- elements-inspector (grade 10, built): emission spectra of light from atoms. Our spectrum is of sound harmonics, built by hand.
- field-lines, collision-lab, circuit-builder, motion-graph-match (grade 11 batch): none use waves or audio.

## Who and how
- Grade 11, physical science (Waves and Sound module). Format: Studio. Family: none.
- Driver: students, on their own laptops, headphones recommended. A teacher can also project it.
- Minutes: 20 to 40.
- Standards: HS-PS4-1 (use mathematical representations to support a claim about the relationships among the frequency, wavelength and speed of waves traveling in various media).
- Look: 9-12 pro instrument. Link `kit:curio` then `kit:theme-912`. Tool accent `--brand` a phosphor green (about #39d98a) for traces, plus amber (about #ffb547) for ghost and second traces. Readouts in the theme's readout font. No confetti, no mascot.

## Screens and modes
Header (kit): title "Sound Studio" with subtitle "Frequency, wavelength and harmonics", mode buttons in a `.seg` group (Tone, Harmonics, Beats, Match), then the kit buttons `motion`, `sound`, `read`.

Layout in every mode: the stage on the left holds three stacked instruments; the panel on the right holds controls and readouts.
1. Scope (top, widest): pressure versus time. Y axis "air pressure change (relative)", X axis in milliseconds. A Time per screen selector under it: 2, 5, 10, 20, 50 ms (default 10 ms).
2. Spectrum (middle): one bar at each frequency present. X axis in Hz, linear, 0 to 8.5 times the fundamental, labeled at each harmonic. Bar height is amplitude.
3. Tube (bottom): a speaker cone at the left end of a long tube of dots (about 24 columns by 6 rows). Dots crowd at compressions and spread at rarefactions. A ruler in meters runs under the tube. Labeled "slow motion, not real speed".

The panel always holds a `hint` paragraph (one or two sentences for the current mode), a Play / Stop button (`.big-btn`, label switches between "Play" and "Stop") and a Reset button. Nothing sounds until Play is pressed.

### Mode 1: Tone (one sine wave)
Panel controls:
- Frequency slider, logarithmic, 20 Hz to 10,000 Hz, default 440 Hz, with a number box beside it (Enter applies; clamped to range).
- Note buttons: "A2 110", "A3 220", "Middle C 262", "A4 440", "A5 880", "C8 4186". Each sets the exact frequency: 110.00, 220.00, 261.63, 440.00, 880.00, 4186.01 Hz.
- Medium selector: Air, Helium, Water, Steel (default Air).
- Air temperature slider, -20 C to 40 C, default 20 C, shown only when Medium is Air.
- Volume slider, 0 to 100 percent, default 40 percent.
- Lock ruler toggle (default off).
Readouts (large, monospace, with units): Frequency f (Hz); Period T = 1/f (ms, 3 significant figures); Wave speed v (m/s, whole number); Wavelength = v / f (m, 3 significant figures; shown in cm below 0.1 m); and a worked line such as "wavelength = v / f = 343 m/s / 440 Hz = 0.78 m".
Responds: the scope draws the sine with two vertical cursors one period apart labeled with T (for example "T = 2.27 ms"). The spectrum shows one bar. Tube compressions sit one wavelength apart against the ruler. Changing Medium changes v and the wavelength but not f or the scope, and a note appears: "Same frequency, new speed, so a new wavelength."

### Mode 2: Harmonics (build a sound)
Panel controls:
- Fundamental slider, logarithmic, 55 Hz to 1,000 Hz, default 220 Hz, with number box.
- Eight harmonic sliders labeled "1 (f)", "2 (2f)" through "8 (8f)", each 0 to 100 percent, each showing its own frequency under it (for example "660 Hz" for harmonic 3 at 220 Hz). Beside each, a Flip button (aria-pressed) that shifts that harmonic by half a cycle.
- Preset buttons: Sine, Square, Sawtooth, Triangle, Clear.
- Show parts toggle: when on, the scope also draws each nonzero harmonic as a thin faint line under the bold sum.
- Volume slider (shared value with the other modes).
Responds: scope draws the sum; spectrum bars match the sliders exactly; the tube shows the sum as uneven crowding, with the ruler marking one wavelength of the fundamental in air at 20 C. Readouts: fundamental f, period T, fundamental wavelength in air, and "Pitch you hear: about f Hz".

### Mode 3: Beats (two tones)
Panel controls:
- Tone A slider, 200 Hz to 600 Hz, default 440 Hz.
- Difference slider, -12 Hz to +12 Hz in 0.5 Hz steps, default +3 Hz. Tone B = A + difference, shown as a readout.
- Buttons: A only, B only, Both (the Play / Stop button plays Both).
- Volume slider (shared).
Responds: the scope here uses a fixed 1,000 ms window (labeled; the Time per screen selector is hidden) and shows the sum with its envelope in amber; the spectrum shows two close bars; the tube shows the two waves adding. Readouts: f A, f B, beat frequency = |fA - fB| in beats per second, time between beats in seconds. At difference 0: "No beats. The two tones are identical."

### Mode 4: Match (optional challenge)
A hidden target sound. The target's trace is drawn in amber on the scope as a ghost; its spectrum is hidden.
Panel controls: Play target, Play mine, the same eight harmonic sliders and Flip buttons as Harmonics (fundamental locked to the target's and shown as a readout), Show answer, Previous target, Next target, and a counter "Target 3 of 6".
Readout: Match percent, live. At 95 percent or more: the line "Matched." in the accent color and one soft Curio.yes() chime. No score, no timer, no stars.

Keys: 1 to 4 switch modes; Space toggles Play / Stop when focus is not in a text box; sliders take arrow keys natively.

## Content
Speeds of sound (Medium selector):
- Air: v = 331.3 + 0.606 x T, with T in degrees C. -20 C gives 319 m/s, 0 C gives 331 m/s, 20 C gives 343 m/s, 40 C gives 356 m/s.
- Helium at 20 C: 1,007 m/s (ideal gas: square root of gamma R T / M, gamma 5/3, M 4.0026 g/mol, T 293.15 K).
- Fresh water at 20 C: 1,481 m/s.
- Steel (mild carbon steel, bulk longitudinal waves): 5,890 m/s.

Human hearing: about 20 Hz to 20,000 Hz for young healthy ears; the top end drops with age. A4 = 440 Hz is standard tuning; the note buttons use equal temperament values listed above.

Presets (amplitude per harmonic 1 to 8, as fractions of slider maximum; F means Flip on):
- Sine: 1, 0, 0, 0, 0, 0, 0, 0.
- Square: 1, 0, 1/3, 0, 1/5, 0, 1/7, 0.
- Sawtooth: 1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8.
- Triangle: 1, 0, 1/9 F, 0, 1/25, 0, 1/49 F, 0.
- Clear: all 0.
Each harmonic n is amplitude x sin(2 pi n f t + phase), with phase 0, or pi when Flip is on.

Match targets (fundamental; amplitudes for harmonics 1 to 8; reveal line shown by Show answer). All have Flip off.
1. 220 Hz; 1, 0, 0, 0, 0, 0, 0, 0. "A pure sine wave: one frequency only."
2. 220 Hz; 1, 0.5, 0, 0, 0, 0, 0, 0. "The fundamental plus half as much of the second harmonic, one octave up."
3. 220 Hz; 1, 0, 0.33, 0, 0, 0, 0, 0. "The fundamental plus the third harmonic: the first step toward a square wave."
4. 330 Hz; 1, 0.5, 0.33, 0.25, 0, 0, 0, 0. "The first four steps of a sawtooth."
5. 220 Hz; 0, 1, 0, 0, 0, 0, 0, 0. "Only the second harmonic: a pure sine at 440 Hz, one octave above the fundamental."
6. 165 Hz; 0.6, 1, 0.4, 0, 0.2, 0, 0, 0. "The second harmonic is the strongest part, yet the pitch you hear is still about 165 Hz."

Hint texts (one per mode; also the Read fallback):
- Tone: "Slide the frequency and watch the period and wavelength. Then change the medium: the frequency stays, the wavelength changes."
- Harmonics: "Flip changes the picture, not the sound. Your ear hears which frequencies are there and how strong, not where each wave starts."
- Beats: "Count the wobbles for five seconds and divide by five. Check your count against the beat frequency."
- Match: "Listen to the target, then build it with the sliders. The amber trace is the target's shape."
Speaker note, shown in Tone whenever the frequency is below 100 Hz: "Hearing little or nothing? Many laptop speakers cannot play very low notes. Try headphones."

## Interactions in detail
- Audio: Web Audio. Tone uses one OscillatorNode; Harmonics and Match use a PeriodicWave built from the eight amplitudes and phases, rebuilt on slider change (debounced about 30 ms); Beats uses two oscillators. Every start, stop and change ramps gain over about 30 ms so there are no clicks.
- Safety: master gain never exceeds 0.25 (about -12 dB full scale) at Volume 100 percent. Harmonic sums are normalized so the waveform peak stays at or below 1 before the master gain; a small "auto-level" label says the sum is scaled to stay safe. Volume is 40 percent on every load.
- Kit Sound off: audio is silent and a panel note says "Sound is off. Turn on Sound to hear it." Visuals keep running.
- The scope is computed from the same math as the audio (not an analyser node), so it is exact and steady. If less than one period fits on screen (for example 20 Hz at 2 ms), it still draws and notes "Less than one period on screen. Try a longer time." If more than about 200 periods fit, it draws the envelope as a filled band and notes "Too many cycles to draw one by one."
- Tube: spacing uses the real wavelength in the ruler's meters; motion is slowed, mapping 20 to 10,000 Hz logarithmically onto 0.3 to 3 cycles per second on screen. The ruler span auto-picks from 0.5, 1, 2, 5, 10, 20, 50, 100 m so that about 1 to 5 wavelengths show, and briefly shows "scale now 0 to 5 m" (with the new span) when it changes. With Lock ruler on, the span stays fixed so wavelengths visibly shrink or grow. If one wavelength is longer than the tube: "One wavelength is longer than this tube."
- Motion off (kit `body.calm`): the tube freezes into a still, correct snapshot of compressions; the scope is static anyway; no slider glide on Show answer.
- Extremes: the number box clamps and shows the clamped value. All harmonics at 0: silence, flat scope, "No waves, no sound." Steel at 20 Hz: wavelength about 295 m, ruler at 100 m with the longer-than-tube note.
- Match percent: 100 x (1 - (sum of |a_i - t_i|) / (sum of a_i + sum of t_i)) over the eight amplitudes, floored at 0, rounded to a whole number. Flip is ignored, matching the "picture, not sound" lesson. Show answer glides the sliders to the target over about 0.5 s (instant with Motion off) and shows the reveal line.
- Switching modes stops all sound (audio and Curio.stop()) and keeps each mode's settings for the session. Reset returns the current mode to its defaults.
- No localStorage beyond the kit's motion setting.
- Must stay usable in a 16:10 iframe and full screen: Curio.fit for the stage; the panel scrolls if needed.

## Art
- panel-backdrop: dark acoustic foam studio wall, soft pyramid foam texture, dim and low contrast, charcoal and deep teal; 16:9; cutout no; people no.
Everything else (scope, spectrum, tube, speaker cone, ruler, sliders) is drawn in code. No people, faces or hands.

## Voice
Bank "hs-narrator", voice "Kore", style "Read clearly and naturally, at a moderate pace". 9 lines. Each plays once per session at its trigger; Read replays the current hint.
- welcome (first tap in the tool): "Welcome to Sound Studio. Every sound here is built from sine waves. Press Play to hear one."
- tone (first entry to Tone): "Tone mode. Slide the frequency and watch the period and the wavelength change on the readouts."
- tone-medium (first medium change): "Now the medium has changed. The frequency stays the same, but the speed changes, so the wavelength changes too."
- harmonics (first entry to Harmonics): "Harmonics mode. Add waves at two, three and four times the fundamental, and listen to the tone color change while the pitch stays put."
- harmonics-flip (first Flip press): "You flipped a harmonic. The picture on the scope changed, but your ear hears almost no difference."
- beats (first entry to Beats): "Beats mode. Two tones close in frequency add up and wobble. The wobble rate is the difference between them."
- match (first entry to Match): "Match mode. Listen to the target sound and build it yourself with the harmonic sliders."
- matched (first match of any target): "Matched. Those are the frequencies in the target."
- speaker (first time Tone goes below 100 hertz): "If you hear little or nothing, your speaker may not play notes this low. Try headphones."

## Family engine
none. Keep the wave math (harmonic sum, speed of sound by medium, wavelength, match percent) in one clearly marked block "WAVE ENGINE" so a future waves family can lift it.

## Sources
- Air, v = 331.3 + 0.606 T: Wikipedia, "Speed of sound" (practical formula for dry air), https://en.wikipedia.org/wiki/Speed_of_sound ; HyperPhysics, http://hyperphysics.phy-astr.gsu.edu/hbase/Sound/souspe.html
- Helium 1,007 m/s at 20 C: computed with the ideal gas speed of sound formula, HyperPhysics, http://hyperphysics.phy-astr.gsu.edu/hbase/Sound/souspe3.html ; helium molar mass 4.0026 g/mol, NIST, https://www.nist.gov/pml/periodic-table-elements
- Water 1,481 m/s at 20 C: Wikipedia, "Speed of sound" (water section); Evident (Olympus) "Material Sound Velocities", https://www.olympus-ims.com/en/ndt-tutorials/thickness-gauge/appendices-velocities/
- Steel 5,890 m/s (mild steel 1020, longitudinal): Evident (Olympus) "Material Sound Velocities", same URL.
- v = f x wavelength, T = 1/f: HyperPhysics, http://hyperphysics.phy-astr.gsu.edu/hbase/Waves/wavrel.html ; OpenStax College Physics 2e, chapters 16 and 17, https://openstax.org/books/college-physics-2e
- Square, sawtooth and triangle Fourier series: HyperPhysics, "Fourier Analysis and Synthesis", http://hyperphysics.phy-astr.gsu.edu/hbase/Audio/fourier.html ; Wolfram MathWorld, "Fourier Series, Square Wave / Sawtooth Wave / Triangle Wave", https://mathworld.wolfram.com/
- Beat frequency = |f1 - f2|: HyperPhysics, "Beats", http://hyperphysics.phy-astr.gsu.edu/hbase/Sound/beat.html
- Ear largely insensitive to phase for steady tones: Wikipedia, "Ohm's acoustic law", https://en.wikipedia.org/wiki/Ohm%27s_acoustic_law
- Hearing range about 20 Hz to 20 kHz: OpenStax College Physics 2e, section 17.6 "Hearing".
- A4 = 440 Hz: ISO 16:1975; note frequencies from f = 440 x 2^((n - 49)/12) for piano key n.

## Done when
1. Tone at 440 Hz in air at 20 C reads period 2.27 ms, speed 343 m/s, wavelength about 0.78 m, and the scope's period cursors are one period apart.
2. Switching Medium keeps 440 Hz and the scope unchanged and gives wavelengths of about 2.29 m (helium), 3.37 m (water) and 13.4 m (steel); air at 0 C gives about 0.753 m.
3. The Square preset puts bars at 1, 3, 5 and 7 times f with heights 1, 1/3, 1/5, 1/7, and the scope shows a squarish wave; Show parts draws the four component lines.
4. Pressing Flip on any harmonic changes the scope shape but leaves the spectrum bars and Match percent unchanged.
5. Beats at 440 Hz and +3 Hz reads 3 beats per second and the envelope shows 3 wobbles per second; difference 0 shows "No beats".
6. Match target 1 reaches "Matched." with only harmonic 1 at 100 percent; Show answer on target 6 sets sliders to 0.6, 1, 0.4, 0, 0.2, 0, 0, 0; there is no score or timer anywhere.
7. Nothing sounds before Play; switching modes stops sound; no click on start or stop; Sawtooth at Volume 100 percent stays within the safe master gain.
8. Kit Sound off silences audio and shows the note; Motion off freezes the tube with readouts intact; keys 1 to 4 and Space work.
9. Each voice line plays once at its trigger and not again that session; Read speaks the current hint.
10. Works in a 16:10 iframe and full screen, one file, no network requests, no em dashes in visible text.
