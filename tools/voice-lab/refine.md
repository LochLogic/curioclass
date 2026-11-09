PASS (exit check 2026-11-06)
Counts: blockers 1 (general 1, family 0), should fix 10 (general 7, family 3), polish accepted 15

# Refine: voice-lab

Curiosity No. 03. Merged from `refine/teaching.md`, `refine/play.md` and `refine/craft.md` (no sensitivity file; the
Teaching lens found nothing cultural, Native or hard-history). Lens frames: `S:/CurioClass-codex-scratch/voice-lab/teaching/out/`,
`.../play/`, `.../craft/out/`; shared audit `S:/CurioClass-codex-scratch/voice-lab/audit-r1/`. Judged by
`docs/agents/CODEX-CURIOSITY.md` and BASELINE: every fix below adds real material or makes a readout true, never a
goal, task, score or finish. Integrator spot-checks (src.html read): PEAK search and clamp at 588-591, the F1/F2 gate at
631, `clearHistory` on Live at 609, and the loop taper at 460-462 all read as the lenses say.

## Blocker
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

## Should fix
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

## Polish accepted
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

## Settled calls
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

## To the spec's open questions
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

## Not taken
- NOTE "A4 +1 ¢" beside PITCH 440 Hz (Play F14): both are honest measurements of the same tone and Done when 4 passes;
  forcing them to agree would hide real precision.
- Craft nit 11's general "grade 1 floor" text-size concern beyond polish 8: the first two minutes for a first grader
  need no reading; the readouts are the grades 8 to 12 depth.

## Exit check (2026-11-06)

Cold exit check, Claude. Fresh audit `S:/CurioClass-codex-scratch/voice-lab/exit/audit-r2/` (finished, exit 0);
own frames and drive results in `S:/CurioClass-codex-scratch/voice-lab/exit/frames/` (shots.json, shots2.json).

### Merged list
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

### Regressions
None found. Default screen at 1366x768 and 375x812 (audit) clean; CLIPS, TONE, Hold, Narrow, Vowels and Manual each
seen once; frames tied to each fix look right. Wide Ah shows fine vertical pitch-period striations at FFT 256: expected
of a 5 ms window on a 140 Hz voice, not the loop stripe.

### Gate
1. Done when: passes on what I checked (PITCH within 1 percent 80 to 1000 Hz and above, PEAK true, privacy line, no
   "correct" target, Wide near 300 Hz). Yes.
2. Codes: MS-PS4-1 now carries amplitude and energy; MS-PS4-2 written down as not covered (`notes.md:4`). Yes.
3. Solo defaults: work, including with the mic blocked. Yes.
4. Sensitivity: none flagged by the merged list (Teaching found nothing cultural or hard-history). Not applicable.
5. No blocker or should-fix open. Yes.
6. Bundle 89,241 bytes; no console errors in the audit or my 19 shots; zero resource requests (e01). Yes.
7. Voice: two fixed lines unchanged; five held clicks and two quick taps clean on every speaking control; Read speaks
   with stops. Yes.

## Audit pilot
- Leads confirmed: none as defects. The size table also confirms no console errors and no dead controls.
- Leads wrong: all 44. "#ribbon overlaps #status/#hint" is labels on the glass by design; "hint out of view" is the
  first-run hint gone after the first action; Manual "keep region" rows are the open drawer covering the page; "welcome
  not heard" after a pad, Hold, Manual or mic is the BASELINE rule 16 cut, settled in round 1.
- Missed: it has no PEAK/PITCH accuracy check, no blocked-permission (cross-origin iframe) run, and no network row in
  the report; I checked those by hand. Its 375x812 host is same-origin, so it never sees the site's no-mic state.
