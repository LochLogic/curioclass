# Voice Lab (Curiosity No. 03)

## The real thing
A live sound spectrogram: time runs left to right, pitch runs bottom to top, and loudness glows as colour. Phoneticians
use it to read vowels and consonants, birders to tell two songs apart, audio engineers to find a hum or a hiss, and
speech therapists to show a child the sound they are making. Voice Lab is that analyser, fed by the student's own
microphone, a set of built-in sounds, or a tone generator, with a vowel chart beside it like the one a phonetics lab
plots from the same numbers.

## Map
- Anchor: science-8-waves (MS-PS4-1, MS-PS4-2).
- Also reaches: science-1-sound-and-vibration, science-4-waves-and-information, science-11-waves-and-sound,
  ela-k-rhymes-and-sounds, arts-k-2-instrument-families.
- Grade band: grades 1 to 12; the depth is pitched at grades 8 to 12, the first two minutes work for a first grader.
- Teacher plan: would teach MS-PS4-1 (frequency, amplitude and wave patterns, seen and measured) in full, but not
  MS-PS4-2 (reflection, absorption, transmission). So it is a second card beside the module's lesson tool.

## The first two minutes
- Open: a black glass screen, a frequency ruler down the left edge (0 to 4 kHz), a level meter on the right, and
  a faint grey hiss already scrolling (the room's own noise, once the mic is on). One quiet line sits on the glass:
  "Press the mic switch, then say ahhh." Under it, small: "Nothing is recorded or kept. The sound never leaves this
  device." If the mic is blocked or refused, the line changes to "No mic here. Press a sound pad below." and the
  input switch moves to CLIPS.
- First action with nothing read: flip the mic switch and make any sound. A glowing ribbon scrolls in from the right
  at once, bright where the voice is loud.
- First reaction: "ahhh" is a stack of bright stripes; a whistle is one thin line that moves when the whistle moves;
  "eee" then "ooo" makes the bright bands jump. The PITCH readout follows the voice note by note.

## Things to do
1. Say "ahhh" and slide your voice up and down: every stripe in the stack climbs and falls together.
2. Whistle a tune and watch it draw itself as one clean line, the closest a voice gets to a pure tone.
3. Say "eee, ahh, ooo" with the vowel chart open and watch your dot walk the corners of the vowel triangle.
4. Whisper the same vowels: the stripes vanish but the vowel bands stay, so the vowel is still there to read.
5. Say "sss" then "shh" and see where each one puts its hiss, high on the ruler or lower.
6. Switch from Wide-band to Narrow-band and watch the same "ahhh" change from broad vowel bands to fine harmonic lines.
7. Turn on harmonic markers and check that the stripes sit at 2, 3, 4 times the pitch.
8. Press Hold, move the crosshair, and read the exact time and frequency of any spot in a word.
9. Play the flute, violin and clarinet pads on the same note and compare their harmonic ladders in slots A and B.
10. Set the tone generator to 440 Hz, then sing until your PITCH readout matches and the two lines merge.
11. Sweep the generator from 20 Hz upward and find where your ears and your speakers stop hearing it.
12. Switch the ruler to the musical (log) scale and play a C major chord pad: three evenly spaced lines.
13. Speak a rhyming pair ("cat, hat") and find the part of the ribbon that is the same in both.
14. Have two people say the same word and compare: same vowel bands in the same order, different pitches.

## Controls
All controls sit on a control deck along the bottom edge of the glass, drawn like an analyser's front panel.
- Input selector: rotary, three detents MIC / CLIPS / TONE. Focused: Left and Right step; keys 1, 2, 3 jump.
- Mic switch: toggle (on, off). Key M. Turning it on asks the browser for the mic; turning it off releases it.
- Gain knob: -20 to +20 dB, 1 dB steps. Up and Down, Shift for 5 dB.
- Range knob: top of the ruler at 2, 4, 8 or 16 kHz (detents). Left and Right.
- Scale switch: Linear / Musical (log). Key L.
- Band switch: Wide-band (about 300 Hz analysis bandwidth, shows vowel bands) / Narrow-band (about 45 Hz, shows
  harmonics). Key B.
- Sweep fader: time across the screen, 2, 5, 10 or 20 s (detents). Left and Right.
- Hold pad: lit pad, freezes the ribbon. Space. While held, a crosshair moves with the arrow keys (Shift for big steps).
- Memory pads A and B: lit pads that store the spectrum slice under the crosshair for comparison, overlaid as two
  outlines. Keys A and S; Shift with the key clears it. Kept in memory only and gone when the tab closes.
- Harmonic markers: toggle. Key H. Draws faint ticks at 1x to 10x the current pitch.
- Vowel chart: toggle. Key V. Opens the F1/F2 plot beside the ribbon.
- Colour map: three-way switch Ember / Ice / Grey. Key C.
- Sound pads (CLIPS): eight lit pads, keys Q W E R T Y U I.
- Tone generator (TONE): waveform switch sine / triangle / square / sawtooth (key G cycles); frequency knob 20 to
  8,000 Hz on a log taper, coarse by arrows, fine (1 Hz) with Shift; level fader -40 to 0 dB.
- Power panel (Motion, Sound, Read): lower-left beside the plate, styled as small rocker switches.

## Readouts
Monospace, green-white on black, in a strip across the top of the glass.
- PITCH: fundamental frequency, Hz, whole numbers (one decimal below 100 Hz); dashes when no pitch is found.
- NOTE: nearest note and octave (A4) and cents off, signed whole number, -50 to +50.
- PEAK: strongest frequency in the current frame, Hz, whole numbers.
- LEVEL: dBFS, one decimal, -60.0 to 0.0, beside the vertical level meter on the right edge.
- F1 / F2: first two formant estimates, Hz, whole numbers, shown only while a voiced sound is held.
- CURSOR (when held): time in s (two decimals, counted back from now) and frequency in Hz.
- RATE: the device's sample rate (44100 or 48000 Hz), small, top right.

## The Manual
Contents: how to read a spectrogram (time, frequency, brightness); what each readout means; wide-band versus
narrow-band; what formants are and why vowels differ; what the mic does and does not do (nothing recorded, nothing
kept, no network); the built-in sounds and how they were made; honesty notes; sources.

Things people have found:
- Saying "eee" then "ooo" drops the second vowel band from about 2,300 Hz to under 900 Hz in adult men's averages
  (Peterson and Barney 1952, JASA 24:175).
- Children's vowel bands sit higher than adults' for the same vowel, about 3,200 Hz for the second band of "eee",
  because a shorter vocal tract resonates higher (Peterson and Barney 1952).
- A sung or spoken note is a ladder of harmonics at whole-number multiples of its pitch (Fletcher and Rossing,
  The Physics of Musical Instruments, 1998).
- In its low register a clarinet's odd harmonics are strong and its even ones weak, because the tube behaves like a
  pipe closed at one end (Fletcher and Rossing 1998; UNSW Music Acoustics, "Clarinet acoustics").
- A whisper has no harmonics at all, yet the vowel bands remain, which is why whispered words are still understood
  (Ladefoged and Johnson, A Course in Phonetics).
- Doubling a frequency raises a note by one octave; 440 Hz is the A above middle C by international standard
  (Fletcher and Rossing 1998; ISO 16:1975).
- An "s" puts its hiss higher on the ruler than a "sh" (Jongman, Wayland and Wong 2000, JASA 108:1252).
- Two people saying the same word share the vowel bands' order and shape, not their pitch (Peterson and Barney 1952).

## Look
- Grammar: an audio analyser. Black glass with a faint reflection, a scrolling heat-map ribbon filling the glass, a
  ruled frequency scale down the left in small engraved numerals, a segmented LED level meter on the right, a readout
  strip across the top, a brushed dark control deck along the bottom with knobs, rocker switches and lit pads.
- Palette from the real material: black glass #07090b, deck graphite #1b1e22, ember map (black, deep red, orange,
  yellow, white), readout phosphor green-white #d8f5e0, LED green, amber and red. Text on deck at AA or better.
- 1366x768: ribbon about 90 percent of the width and 70 percent of the height; vowel chart opens as a 320 px square
  panel over the right of the ribbon; deck 150 px tall.
- 375x812: readout strip on top (two rows), ribbon below (about 45 percent of the height, ruler kept), vowel chart
  replaces the ribbon's right half when open, deck below in two rows with the sound pads as a 4x2 grid.
- Maker's plate and Manual drawer lower-left, in the same corner as Span and Spire and Pocket Universe; the plate
  reads "Curio Class Curiosities · No. 03 · Voice Lab", engraved into the deck's metal.

## Real material and sources
- Live input: Web Audio getUserMedia with echoCancellation, noiseSuppression and autoGainControl all off (the
  browser's speech filters would otherwise erase the very things being measured), an AnalyserNode (FFT 512 for
  wide-band, 4096 for narrow-band at 48 kHz), YIN or autocorrelation pitch (50 to 1,000 Hz), and LPC formant
  estimates (order about 12 after downsampling to 10 kHz). No data file. 0 KB.
- Built-in sounds: synthesized in code at load, not recordings, so there is nothing to licence. Vowels (ah, ee, oo)
  for an adult and a child built by formant synthesis from Peterson and Barney's published averages; whistle (a
  sine with vibrato and glide); flute, violin and clarinet on one note from harmonic recipes in Fletcher and Rossing;
  "sss" and "shh" as filtered noise; a siren sweep; a C major chord. About 15 KB of code.
- Vowel chart reference points: Peterson and Barney 1952 averages for men, women and children (a published table of
  numbers, facts, cited). About 1 KB.
- Total bundle goal under 400 KB. No network requests.

## Honesty notes
Said in the Manual:
- Formants are estimates from a standard method (LPC); they wobble on high voices and fail on whispers and hisses.
- The built-in sounds are made by the computer from published numbers, not recorded instruments.
- A laptop mic and speaker roll off the lowest and highest sounds, so the edges of the ruler under-report.
- Pitch tracking can jump an octave on a breathy or creaky voice.
- The vowel chart's corners are averages for American English speakers in 1952; other accents and languages sit
  elsewhere, and that is not wrong.

## Voice
Bank `news-reader`, restyled: "Say clearly and steadily, like a radio studio engineer talking through the glass."
First-run hint (spoken once, gone after the first sound): "Press the mic switch, then say ahhh." Mic-free variant:
"No mic here. Press a sound pad." Read speaks what is on the glass now: the input, then PITCH and NOTE if a sound is
playing, in plain words ("Pitch two hundred twenty hertz, A three"). Nothing else is spoken.

## Done when
1. The tool opens to the glass with no welcome screen; the first sound draws a ribbon within 100 ms of the mic on.
2. The mic line "Nothing is recorded or kept. The sound never leaves this device." shows before and while the mic is
   on, and no audio is stored, saved or sent anywhere (checked in the code and in the network log: zero requests).
3. With the mic refused, CLIPS mode is selected and every sound pad works.
4. PITCH reads within 1 percent on generator tones from 80 to 1,000 Hz; NOTE names A4 at 440 Hz.
5. Wide-band and narrow-band visibly differ on the same "ahh" clip (bands versus harmonic lines).
6. Every control works by keyboard and announces its value; Hold plus arrows reads any point.
7. Runs at 60 frames a second at 1366x768 on a school Chromebook profile; no freeze at 16 kHz range and 20 s sweep.
8. Layout checked at 1366x768 and 375x812; plate and Manual drawer lower-left at both.
9. Motion off stops the scroll animation smoothing (the ribbon still updates in steps); contrast passes AA.
10. Short test passed and written in the report, with a frame beside Beat Lab.
11. No score, goal, level, sticker or finish screen anywhere, and no "correct" vowel target.

## Open questions
- The site's tool page embeds tools in an iframe; the mic needs `allow="microphone"` on that iframe. Lean: add it to
  the tool page template for curiosities only; until then the mic works from "Play full screen".
- Speaker feedback when the mic is on and a tone plays aloud. Lean: TONE analyses the generator directly (no mic), and
  the mic switch turns off while TONE is selected.
- A short recorded clip of a real instrument would beat a synthesized one. Lean: stay synthetic for launch; add
  public-domain recordings later only with a per-file licence check.
