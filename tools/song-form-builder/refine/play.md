# Play lens: song-form-builder (round 1)

Played cold as a grade 3-5 student alone at home and as a teacher projecting to a class. Bundle: `CURIO_DRAFT=1`,
100 KB, no console errors or exceptions in any run (the only log line was the host page's own favicon 404 at 375 wide).
Placeholder art and the browser voice are not reported.

Counts: blockers 0, should fix 4, polish 8, nits 4.

## Frames looked at

All in the lens scratch folder (`lens-sfb-play2/out/`):
- f1: default, Rondo for Recess, a full 8-block strip with a twin, the editor open, Listen idle, Listen done
  (Frere Jacques), at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x1000.
- f2 and f11: 375 wide in the iframe host (`drive.py --host`): default, a real tap-to-place, editor open and scrolled,
  Listen mid-song (Frere Jacques, part 4 of 8), Listen done (Ode to Joy).
- f3 and f4: a solo ABA build at a 2 s held-click pace, playing to the end, mid-play playhead, an edit session of five
  taps, the twin flow (Make it A′, Edit, beat 7, Done, Play).
- f5: keyboard: full Tab order, place with Enter, arrows along the strip (both ends), the bar under the strip,
  the note grid (arrows, Space, Enter, Delete), Escape.
- f6 and f7: Listen at a 2 s pace (Hot Cross Buns with two wrong answers, Mary with one wrong answer, Sound on and
  Sound off, Row Row Row done at 680x425).
- f8: drags with whole-pixel jittered pointer paths (onto slot 6 of a 1-block strip, onto a filled slot, released
  mid-strip, released off the strip), Play with an empty strip, Read during play, Clear and starter confirms,
  ripple with Motion off and on, a strip block picked.
- f10: first-tap timing on fresh pages (stage, Read, Sound, Sound off then on, Hear, a mode button, New section, Tab).
- f12: five placements in a row and two full plays (Quick).

What works well: the first screen says what to do and the hint follows every step; placing by tap, drag and keyboard
all work (no gaps, replace, off-strip drop does nothing); arrows walk the strip and stop at both ends; linked copies
ripple (outline with Motion off) and the Form card counts "3 copies changed"; Read stops the music; the empty-strip
Play speaks "Put a block in the song strip first." and flashes the shelf; how lines spoke once in five actions
(playHow 1 of 5 placements) and the form line spoke on every finished play (2 of 2), about 1 s after the music ends,
never over it. Strip, Play song and the Form card are on screen without scrolling at every size, including 680x425
and 375 wide.

## Should fix

1. **Listen, a wrong answer: the answer buttons stay live for about 4.5 s before the comparison plays, so the
   side-by-side replay is easy to skip.** (mode Listen; `answer()` awaits `listenWrong` with `wait: true` before
   `phraseDone(ck)`, while `phase` stays `'answer'`.) Seen in f6/f7 timelines: Mary, wrong tap at 22.4 s, replay of
   part 1 starts at 27.1 s; with Sound off the student sits 4.5 s in silence under "Listen again" with nothing playing.
   In Hot Cross Buns at a 2 s pace the student's second guess landed at 11.7 s, cut the line, and counted as the
   second miss, so the reveal came without the two phrases ever being heard side by side (spec Done when 5). Better:
   start the comparison at once (or the line and the comparison together, line shown and spoken after), and hold the
   answer buttons disabled until both phrases have played. **general** (any quiz with a feedback line before a
   replay).
2. **Listen: the biggest button on screen while answering is "↺ Start over", and it wipes the labels with no
   question.** (mode Listen, `#listen` once `phase !== 'idle'`; frames 375-listen, l2b-mary-wrong-680,
   1366x768-listendone.) A grade 3 student looking for "play it again" taps the big teal button and loses Frere
   Jacques at part 4 of 8. Build's Clear song asks Yes / No; Listen should match, or make the big button "↻ Hear
   again" while answering and move Start over to a small button by the Song picker. At the end of a song the hint
   says "Press Play whole song" but the big button is still Start over and Play whole song is the small one under the
   card. **family:music-studio** (Listen-style labeling).
3. **First screen: the line under the empty strip contradicts the hint.** (Build, `#barlab` default text.) With an
   empty strip it says "Tap a block in the song strip to hear it, twin it or remove it." while the hint says "Tap a
   block on the shelf". There are no blocks in the strip, and tapping an empty space does nothing. Seen in every
   default frame (f1 *-default, f11 680-clean-default, f2 375-default). Show nothing there (or "Your song strip:
   8 spaces") until the strip has a block. **general** (words match the state).
4. **Twin editor: the how line speaks the plain-section version.** (Build, `openEditor` speaks `editHow` "Tap the
   grid to change the notes. Every copy of this section changes too." for a twin as well.) Run v2-twin: after Make it
   A′ and Edit on A′, the spoken line tells the student to tap the grid, but beats 1 to 6 are locked; the hint and
   tip say beats 7 and 8. If the first Edit a student ever opens is a twin, that is the only time editHow plays. Speak
   the twin hint ("Tap the grid in beats 7 and 8 ...") for a twin, its own how key. **family:music-studio**.

## Polish

1. **A right answer in Listen is flat.** Only a chime and the block appearing; the question line just changes to
   "Part 3 of 4" (f6 timeline 20.3 s). Better: a short shown line "Yes: new music, B." for a beat before the next
   part plays, so a student alone knows the guess was right and why. **family:music-studio**.
2. **The end of a play is flat.** After ABA plays, the form line is spoken but nothing on screen changes; the Form
   card already showed "Ternary" before Play (b2-aba-play). Better: when the song finishes, briefly mark the matching
   letters in the strip (the two A blocks lift or get a bracket "home ... home"), so the shape is seen as well as
   heard. **family:music-studio**.
3. **The playhead is hard to see on a projector.** A 6 px bar above the block and a 35% opacity column on the note
   sketch (v1b-midplay). Better: the playing block lifts or gets a thick outline, so a class can follow from the back.
   **family:music-studio**.
4. **A first tap on Hear (or anything that starts sound) loses the welcome for good.** (ft-hear: welcomeBuild
   dropped stale at the first tap and never comes back; the hint still shows it.) Hear is a natural first tap. Better:
   bring the skipped welcome once when that first sound ends. **general**.
5. **The Form card reserves a tall empty box.** About 120 px of white under "Put blocks in the song strip to see its
   form." at 1366x768 and 375 wide (f1 1366x768-default, f2 375-default). At 375 it pushes the shelf to the fold, so
   the shelf's Edit and Hear buttons start below the screen. Better: reserve less at narrow widths, or put the shelf
   above the long card text in the stack layout. **general**.
6. **Teacher on a projector: the Form card text is 14.5 px at 1920x1080 and the strip stops at 150 px blocks with a
   290 px gap on the right** (1920x1080-full8). The form name is the teaching moment; scale the card's name and
   letters up on big screens and centre the strip as Listen's is. **general**.
7. **"Press Stop to wait." in the Listen reveal hint is confusing for grade 3** (`H.lReveal`). Better: "Here is the
   answer. The next part plays next. Press Stop to pause." **family:music-studio**.
8. **A solo student runs out of reasons to keep building after one or two songs.** After ABA and one edit the hint
   loops "Press Play song again"; nothing invites trying AABA or a rondo. Better: one optional "Can you build a rondo?"
   line after the second play, or a small challenge list. This adds to the spec, so it goes to the spec's open
   questions, not the builder. **general**.

## Nits

1. Keyboard: Tab from the note grid jumps out to the header, because Instrument and Done come before the grid. Done is
   one long Tab loop away; put Done after the grid in the tab order (f5 k2, k5). **general**.
2. "＋ New section C" wraps the letter onto its own line at 1366x768 and 800x500 (f1 defaults). **general**.
3. At 680x425 the empty strip is 2 rows of 4 (46 px blocks would fit in one row); the shelf then scrolls inside
   (scrollHeight 252, clientHeight 149, f11). It works; one row would give the shelf room. **family:music-studio**.
4. Listen done: the eight disabled Same / Almost buttons stay on screen under "All 8 parts labeled." (f1
   1366x768-listendone, f7 l4-row-done-680). Hide them at the end so Play whole song stands out. **family:music-studio**.

## Voice at a 2 s tap pace (from the logs)

| line | kind | expected | spoken |
|---|---|---|---|
| welcomeBuild (first tap on the shelf, stage, New section, Tab) | welcome | 1 | 1 |
| welcomeBuild (first tap Read / Sound) | welcome | 0 | 0 (Read spoke the hint only; Sound off then on brought it once) |
| welcomeBuild (first tap Hear) | welcome | 1 later | 0 (polish 4) |
| playHow (5 placements) | how | 1 | 1 |
| editHow (5 grid taps) | how | 1 | 1 |
| linked A (5 grid taps, one session) | event | 1 | 1 (one queued copy dropped as newer) |
| twinHow | how | 1 | 1 |
| form line (2 and 3 plays) | event | each play | each play, about 1 s after the music |
| emptyStrip | event | 1 | 1 |
| listenWrong | event | 1 per miss | 1 (but see should fix 1) |
| reveal and song end lines | event | 1 | 1 |

No line played over the music. No stale line played after a mode change in these runs.

Note: `tools/song-form-builder/host.html` was already in the tool folder when this lens started (another lens's
`--host`); this lens's `--host` rewrote it with the same content and left it there, since another agent may still be
using it.
