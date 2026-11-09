# Craft lens: voice-lab (Curiosity No. 03), round 1

Cold Craft lens, 2026-11-05. Judged against CODEX-CURIOSITY.md and the VISION "Curiosities" section, plus REFINE
Craft and the standard voice check. Bundle `tools/voice-lab/voice-lab.html` as built (not re-bundled). My frames and
run logs are in `S:/CurioClass-codex-scratch/voice-lab/craft/out/` (shots: perf.json, voice.json, keys.json,
keys2.json in the folder above it).

## Contract (clean)

- One file, 77.7 KB (spec goal under 400 KB). The kit is inlined; no images, fonts or audio files.
- No network requests: `performance.getEntriesByType('resource')` is 0 after a 20 s run, and the bundle has no fetch,
  XHR, WebSocket or beacon. The only URLs are source links in the Manual.
- No console errors or exceptions in any of my 18 shots (the one 404 was the host page's own favicon).
- Kit used, not re-implemented: `Curio.voice`, `Curio.audio`, `Curio.init` wires Motion, Sound and Read.
- No em dashes; "Curio Class" everywhere; lesson-creep search (score, points, goal, sticker, badge, correct, wrong,
  try again, complete, well done) has no hits. No welcome screen, goal, score, finish or kit header.
- Privacy line is on the glass at every size and state, before and while the mic is on.

## 60 fps (clean)

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

## Findings

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

## Access (clean except 1)

- Tab order: ribbon, input, mic, gain, range, sweep, the four switches, bank, Stop, pads (`k-tab-pad`: the 13th Tab
  lands on "Ah adult, key Q" with a visible ring).
- Gain: Shift+Right +5, Up +1, Shift+Left twice to -4 dB, aria-valuetext "-4 decibels". Tone frequency: Shift+Up
  +1 Hz twice then Up one semitone to 468 Hz, valuetext "468 hertz". Input rotary: Left and Right reach TONE.
- Hold by Space: focus moves to the ribbon, arrows move the crosshair, the label reads "CURSOR -0.58 s · 960 Hz.
  Arrows move the crosshair. Space returns to live." and the live region reads the same with pitch and note.
- Targets are 44 px or more everywhere (CSS minimum on button, input, select). Colour is never the only signal:
  A solid and B dashed with text labels, vowel groups by shape, the level meter by position.
- Contrast: lowest text pairs are #a9b9b1 and #b9c8c0 on #07090b to #292d30, all well above 4.5:1.

## Lines and voice

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

## Audit pilot

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
