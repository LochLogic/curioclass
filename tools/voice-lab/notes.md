## What it teaches

Voice Lab is a Curiosity: an open sound analyser. Using it makes frequency, amplitude, harmonics and vowel resonances visible and measurable.
It supports MS-PS4-1; it does not cover the reflection, absorption and transmission required by MS-PS4-2, so it belongs beside the module's lesson tool.

## Key skills

- Compare frequency and amplitude independently.
- Inspect harmonics and relate frequency ratios to octaves.
- Freeze a signal and measure time and frequency.
- Compare spectra while recognising estimation limits.

## Support at home

- Hum one note while changing the shape of your mouth. Listen for the change in vowel quality.
- Compare humming and whispering the same word.
- Listen for the difference between a whistle and a buzz, without trying to make either loud.

## Five-minute start

Open the glass. Press a synthetic sound pad if microphone access is unavailable. Explore freely, then open the Manual when a readout raises a question.
Nothing must be passed or finished. The default microphone is off and requests permission only when explicitly switched on.

## Inputs

MIC uses live local audio, CLIPS uses original synthesized examples in two eight-pad banks, TONE provides a directly analysed oscillator.
No audio is recorded, exported, saved or transmitted. Rolling analysis and A/B spectral memories are temporary RAM, as explained in the Manual.

## Talk questions

What moves when you change a vowel but keep the note steady? What changes between Wide and Narrow? Which differences survive a quieter input?

## Good to know

Reference vowels are historical American English averages, not pronunciation targets. LPC is an estimate; high voices, whispers and noise can defeat it.
The vowel chart follows live estimates; Its numerical F1/F2 readout is live too; Hold freezes the values for the cursor's time. It never substitutes historical reference values.
Stop changes to Start for a paused tone generator. Press Start to resume that tone.
Use moderate playback volume. Microphone audio never plays through the speakers. Read uses available browser speech; the selected bank voice is not recorded.
The site iframe requires allow="microphone"; changing the shared site template is outside this build's write scope.
Size: target below 400 KB, with no image or audio assets. One bundled offline HTML file.

## Refine repairs

Tone OUTPUT now shows a linear amplitude ratio and its square, relative signal energy for the same waveform and duration.
These are generator ratios before analysis Gain, not room sound energy. About +6 dB means twice the amplitude and four times the energy.
Wide uses 256 samples, Narrow 4096; PEAK always uses the separate 4096-sample tracker.
When iframe policy blocks microphone access, the instrument starts on CLIPS and offers the sound pads immediately.
The input rotary and Range, Sweep, Bank and Wave are click-stepped controls with announced keyboard values.
The synthetic flute, violin and clarinet use C4, about 262 Hz; steady clips loop whole cycles without an edge taper.
The C-major pad uses equal temperament. A near-C2 pitch estimate is an approximate shared pattern, not an exact common period.
