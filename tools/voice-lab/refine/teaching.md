# Refine lens: Teaching, voice-lab (Curiosity No. 03), round 1

Judged against docs/agents/CODEX-CURIOSITY.md and VISION.md "Curiosities: the second shape", not lesson norms.
Frames: `S:/CurioClass-codex-scratch/voice-lab/teaching/out/` (my own, 1366x768, drive.py on port 9741) plus the
shared audit at `S:/CurioClass-codex-scratch/voice-lab/audit-r1/`. Measurements saved as `tones.json`,
`vowels.json`, `peaknarrow.json` in `S:/CurioClass-codex-scratch/voice-lab/teaching/`.

## Findings

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

## Done when (teaching-relevant items tested)

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

## Facts spot-checked (second source)

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

## Audit pilot

- Leads confirmed: none that bear on teaching. The "#ribbon overlaps #status, #hint and #privacy" rows are labels
  drawn on the glass, by design. "count and word disagree: '1 dBFS'" is a false lead (a LEVEL value like −13.1).
- Leads that were wrong or not teaching: "hint out of view" in every state is correct behavior. The first-run hint
  is meant to vanish after the first action (Curiosity rule). "Welcome not heard" after a pad tap is allowed by
  BASELINE rule 16.
- What it missed: every finding above. The audit cannot check whether a readout is true (the PEAK blocker needed a
  tone sweep against PITCH), whether a standard is exercised (amplitude and energy), or what a synthetic clip
  implies (whisper loudness, the flute range).
