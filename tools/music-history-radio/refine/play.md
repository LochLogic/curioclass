# Play lens: music-history-radio

Counts: blockers 0, should fix 9, polish 5, nit 5

Played cold twice: as a grade 9-12 student alone at home with headphones (no teacher; Power first, because the
welcome says so), and as a teacher projecting it at 1366x768 and 1920x1080. Bundle as handed over (CURIO_DRAFT=1).
Frames and logs via `scripts/drive.py` (port 9771, held clicks, real drags); shared audit read, not re-run. All Chrome
runs are muted, so "what a student hears" is judged from the audio graph: an analyser tapped on the output (RMS and
peak every 50 ms), the conductor's own state (`RadioAudio.inspect`), counted `RadioAudio.start` calls, and `V.log`.
No console errors or exceptions in any shot.

Frames looked at (mine, in the play scratch `out/`): default 1366x768 and 1920x1080 powered, Motion off powered,
mid-tune between Baroque and Classical, Hip hop, Gamelan, Ragtime, Mixing desk with a Chant/Hip hop/Rock and roll mix,
Mystery reveal with a moved guess (Gamelan forced), 760x900 Mystery reveal, a 3x zoom of the 680x425 Mixing desk; plus
every audit frame at 1366x768, 680x425, 800x500 and 375x812 (default, all three modes, compare-ready, mystery covered,
reveal, complete set).

Checked and fine: the default screen says what to do (Power is central, the hint and the welcome name it); the radio
is the biggest thing in Dial and Mixing desk at 1366x768; nothing overlaps at 1366x768 or 1920x1080; Flip waits for
the bar line (pressed at 13.99 s, applied at 15.69 s, the bar count carries on); desk knobs show "next bar" at once and
apply on the line; the ident ducks the music by about 8 dB while it plays (-37.7 dB during, -29 dB after, Disco) and
it comes straight back; every loop is under 30 s (Chant 17.5, organum 24.4, Renaissance 20.4, Baroque 18.2, Classical
18.9, Romantic 21.1, Gamelan 21.3, Ragtime 17.6, Swing 13.6, Rock and roll 15.5, Disco 17.0, Hip hop 22.2, gap
included); Space toggles Power from the page; Read speaks the hint first; Motion off keeps the same timing (the needle
jumps, static 300 ms).

## Blockers

None.

## Should fix

1. **Once Power is on, no how line is ever spoken again.** Voice welcome (src.html:1141-1148) returns nothing when
   powered and playing; `compare()` (1465) and the flipHow trigger (1444) speak only while paused. The welcome tells
   the student to press Power first, so this is the main path. Held-click run, gap 3 s: Power, Station, Compare,
   Station, Flip, Mixing desk, Random mix, Mystery station, Tune in, Next station. Spoken: six idents and one result.
   compareHow, flipHow, dialReady, deskHow and mysteryHow never appear in the log, not even as `silent`. A student who
   opens Mystery station after Power hears a mystery tune start with no word on what to do; one who opens the Mixing
   desk hears only "1720. Baroque." The hint shows each line, so the screen is right, but STANDARDS "say how to act"
   wants the line spoken the first time. The idents already duck the music; the first how line of each mode (and
   compareHow) can duck the same way. Seen: `path-main` log. general.

2. **Mystery before Power speaks the wrong instruction.** Mystery station from a fresh page speaks powerHow (L.powerHow,
   src.html:1092): "Press Power to hear the station. Then use the controls below the radio." The hint at that moment
   says "Press Power to hear the hidden station. Then move the year pin and press Tune in." The year pin is above the
   radio, and after Power nothing more is spoken (mysteryHow never plays). Same for the Mixing desk first. Give each
   mode its own power line that names its next control, and let mysteryHow / deskHow follow once Power is on.
   Seen: `path-mystery-first`, `path-desk-first` logs. general.

3. **Spinning the dial uses up every station's ident.** `tune()` hushes on every station change (src.html:1431) and
   `identify()` queues the ident as a once-only how line (1408). One real drag across the needle rail (3.5 s, Power
   on) started all eleven idents for about 300 ms each and cut every one (`cut: hush`); stepping back through five of
   those stations afterwards was all `silent`. Spinning the dial is the first thing most students will do with a
   radio, so most never hear an ident whole, and Done when 8 ("spoken once per station") fails in practice. Queue the
   ident only after the needle has rested on the lock for about half a second, or mark it heard only when it finished.
   Seen: `sweep` log. general.

4. **Fine-tuning near the lock edge restarts the tune over and over.** `tune()` restarts at bar 1 whenever the same
   station is re-locked (src.html:1433), even though it was still audible (strength 0.6 to 0.7) a moment before. A
   drag that wobbles 3 px either side of the 15% edge on Organum restarted the music 20 times in under a second. A
   student settling the needle with a trackpad hears bar 1 stutter. Restart on a new station only (as the spec says,
   "a new lock"), or only after the signal was lost for a while. Seen: `wobble` (22 starts counted). family:music-studio.

5. **Stations are up to 14 dB apart in loudness, and the static is louder than most of them.** Steady RMS over 3.5 s
   per station, idents already heard (no duck): Rock and roll -26.0, Renaissance -27.5, Gamelan -28.0, Romantic -29.2,
   Disco -29.5, Ragtime -29.7, Swing -31.7, Classical -32.8, Organum -33.2, Chant -34.0, Baroque -38.9, Hip hop -39.7 dB.
   Turning from Renaissance to Baroque drops about 11 dB; Disco to Hip hop about 10 dB, so the "heavy, laid-back beat"
   is the quietest station on the dial (and RMS flatters it, since its kick is low and heavy). Static alone at the
   midpoint is -29.3 dB, louder than eight stations, so a student on headphones gets a blast between stations and then
   a faint Baroque or Hip hop. Level-match the stations (a per-station trim on the bus, src.html:833) to within about
   3 dB, and set the static a few dB under the average station. Seen: `loud-clean`, `static-positions`.
   family:music-studio.

6. **The "changed" tag is on every row of every station, so it says nothing.** `renderPanel` (src.html:1307, 1313)
   compares feature sentences, and no two stations share one, so every station after Chant shows five "changed" tags
   (counted: 0 for Chant, 5 for each of the other eleven). The previous station is also the dial neighbor, so Ragtime's
   rows are "changed" relative to Gamelan, which reads as a progression the notes say it isn't. Compare by a short
   category per row (for example Rhythm: free / steady / syncopated / swing / backbeat) and skip Gamelan as the
   neighbor of Ragtime, or drop the tag. Seen: `m-changed`, `f-hiphop`, `f-midtune`. general.

7. **A Gamelan Mystery round scores the student against a date the tool says is not the music's date.** Mystery uses
   `year: 1889` (src.html:474, reveal 1511). Forced Gamelan, guess 1300: "Javanese gamelan · 1889. You said 1300: 589
   years off", directly above "an encounter, not an origin". A student who hears a centuries-old tradition and places
   it early is marked far off. Leave Gamelan out of Mystery sets (or score it differently) and say why. Flag for the
   sensitivity and teaching lenses; I don't judge the content. Seen: `f-mystery-guess-reveal`. general.

8. **The Mixing desk knobs are almost impossible to set with a mouse.** At 1366x768 each knob is an invisible 54 px
   range over the painted knob (src.html:124), twelve eras in 54 px, about 4.5 px per era. A 40 px drag right from the
   Sound knob's center went from Baroque straight to Hip hop. The knobs are the focus of the mode. Give them the
   tuning knob's drag (32 px per step, src.html:1631) or small ◀ ▶ buttons beside each era name; arrow keys already
   work but nothing on screen says so. Seen: `knobdrag`. general.

9. **flipHow is spoken while the radio is off, against the hint.** Station, Compare, Station before Power: the voice
   says "Press Flip to switch between the two stations at the next bar." while the hint says "Press Power, then drag
   the tuning knob or tap Station to find a station." and nothing is playing (there is no next bar). Hold flipHow until
   Power is on, under the duck from item 1. Seen: `path-compare-unpowered` log. general.

## Polish

1. **The Mystery reveal hides the student's own pin.** On Tune in the guess slider is hidden (src.html:1347) and the
   strip shows only the answer, so "320 years off" is a number with nothing to see. Keep the student's pin (dimmed) and
   draw the gap between the two pins; that is the moment the true-time strip was built for.
   Seen: `state-mystery-reveal-1366x768`, `f-mystery-guess-reveal`. general.

2. **"Within 50 years" can be farmed without listening.** Cheap way (Python over the twelve years): a fixed guess of
   1930 to 1950 is within 50 years of five of twelve stations, so about 2.5 of 6 per set with no listening, while the
   900 to 1500 stations need a near-exact ear. A tolerance of half the gap to the neighboring stations on the true-time
   strip, or "closest station" scoring, would make the count mean the same thing across the dial. Flag to Teaching.
   general.

3. **Projected at 1920x1080 the dial labels are tiny on a huge radio.** Dial years are 11 px, the "SIGNAL LOCKED" and
   phrase lines 10 px, the hint 13 px, while the dial window is about 860 px wide and mostly empty cream. Scale the
   year marks with the radio (say 1.6 to 2% of the dial width) so the back row can read the station.
   Seen: `f-1920`, `m-1920`. general.

4. **Hip hop's pad grid is cut off at 1366x768.** The panel scrolls (scrollHeight 666, clientHeight 634) and the
   SNARE row sits under the footer; only a scroll shows it. Tighten the panel (the five "changed" tags from Should fix
   6 cost a few px per row) so the notation fits. Seen: `f-hiphop`, `m-hiphop-panel`. general.

5. **At 760x900 the revealed clues are below the fold.** After Tune in the hint says "Compare the two highlighted
   clues, then press Next station." but the highlighted rows are under the radio, off screen. Scroll the panel into
   view on reveal, or put the two clue names in the result line ("Clues: Texture, Instruments").
   Seen: `f-760-reveal`. general.

## Nits

1. **The needle sits on the tuned year.** At every size the red needle crosses the station's own label ("9|00",
   "17|20", "18|89"), the one year the student wants to read. A real radio does this, so it's optional: a small lift
   of the labels or a bold year above the needle would help. Seen: default and desk frames.
2. **Tune in works before Power.** In a fresh Mystery the student can reveal without hearing anything. Fine for a
   teacher demo; a disabled look until the station has played a bar would match the hint.
3. **680x425 Mixing desk: Power covers the bottom edge of the dial window** and both knobs touch it.
   Seen: `zoom-desk680`.
4. **A station change cuts the old sound to zero in one sample** (`silence()`, src.html:999, `setValueAtTime(0)`).
   By code only (all runs muted): a sustained choir or pad can click. A 20 ms ramp would hide it.
5. **Reset at the starting mix does nothing visible** (audit lead). Not a dead control; a disabled look while the mix
   is Baroque/Baroque/Baroque would say so.

## Feel

The radio itself lands: the painted set, the tuning eye closing, one tune through twelve worlds. The flat parts are
around it. Mystery has no sound at the moment it should land (the reveal speaks only "It was 1956. Rock and roll."
while the pins vanish), the Mixing desk is fun on Random mix but frustrating by hand, and the "changed" tags train the
eye to ignore them. On headphones the level jumps between stations and the static between them will be the most
noticed sound in the tool. A teacher projecting has a beautiful radio whose station names are unreadable from the
back.

Spoken on the main path (Power first, held clicks, 3 s gaps), for reference:

| line | kind | expected | spoken |
|---|---|---|---|
| ident (each station, first lock) | how | once each | once each when tuned by Station; cut after about 300 ms when swept |
| compareHow, flipHow | how | once | 0 |
| dialReady | how | once | 0 |
| deskHow | how | once | 0 |
| mysteryHow | how | once | 0 |
| result | event | every Tune in | every Tune in |

## Audit pilot

Leads confirmed:
- `#power` first tap, welcome not heard: confirmed in substance. Power speaks only "900. Chant.", so the second half of
  the welcome (how to change stations) is never spoken, and nothing after it is either (Should fix 1).
- Two quick taps on Power, ident cut by hush: the cut is correct (the second tap pauses), but it is one case of a
  real problem: the cut ident counts as heard and never comes back (Should fix 3).

Leads that were wrong:
- `#compare` first tap, welcome not heard: what plays instead is powerHow, which names the next action (Power). Fine.
- Mixing desk Reset "nothing changed": the mix is already at its starting value; not a dead control (Nit 5).

What it missed: everything that only shows with sound on or over time: idents burned by a dial sweep, restarts on
re-lock, the 14 dB loudness spread and loud static, how lines never spoken once Power is on, the wrong power line in
Mystery, flipHow while off. Also: the "changed" tags lit on every row, the mix knob's 4.5 px per era, the Gamelan round
scored against an encounter date, the vanishing guess pin, the cheap-solve guess, the tiny dial labels when projected,
the clipped Hip hop grid (inside a scrolling panel, so not a fold failure), the 760x900 reveal fold, and the needle
crossing the tuned year (its "lines across labels" check came back clean).
