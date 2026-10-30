# Folk Song Arranger

## One idea
One old tune, three real jobs: arrange "Skip to My Lou" for a lullaby night, a harvest square dance or an eighth-grade walk, and the arranger's checks (range, balance, length, fit) tell you what a real small band would run into, so every revision you make carries a reason you can say out loud at the concert.

## Not like
- song-form-builder (3-5, music-studio family): builds form from A and B letter blocks. Here the form is a tool for a job; the student also picks players, roles, octaves and dynamics and is checked against a real occasion.
- music-history-radio (9-12): one tune re-arranged by each era's rules, listened to. Here the student makes the arrangement, for an occasion, not an era.
- beat-lab (9-12): produces an original track on a grid. Here nothing is composed note by note; an existing melody is given parts and a plan.
- chord-explorer (6-8): harmony on a keyboard. Here chords are one role a player can take.
- band-practice (6-8): the student performs one part in time. Here the student arranges and listens.
- storyboard-studio (9-12): shot planning, film. cover-version-review (this band): judges two finished versions; this tool makes one.

## Who and how
- Grade 6-8, music, module "Arranging a Song (Music)". Topic line: arranging a folk tune for an occasion.
- Driver: students (headphones suggested). 25 to 40 minutes.
- Standards: NCAS MU:Cr2 (organize and develop ideas), MU:Cr3 (refine and complete; revise from feedback), MU:Pr4 (select, analyze and interpret for a performance).
- Header: title, topic line, modes **Arrange** (default), **Concert card**, then kit `motion`, `sound`, `read`.

## Screens and modes

### Arrange
- Focus: the arrangement grid in the middle of the stage: one row per player (up to 5), one column per section in order, each cell showing that player's role in that section (Melody, Chords, Bass, Beat or Rest) as a colored block with its word and a dynamic letter (p, mf, f). The grid is at least 55% of the stage height at 1366x768.
- Above the grid: the occasion banner (painted venue strip with the occasion's name and its needs in code: tempo window, length window, one special need) and the timeline ruler in seconds.
- Left of the grid: the players' painted instrument cutouts (on stands, no people), each with its name.
- Below the grid: the four check lights: **Range**, **Balance**, **Length**, **Fit**, each green (a check mark) or amber (an exclamation mark) with a one-line reason; tap a light to highlight the cells it is about.
- Panel: `hint`, **Play** (becomes **Stop**), **Occasion** (three buttons: Lullaby night, Square dance, Eighth-grade walk), **Tempo** slider (40 to 140 beats a minute), **Add player** (opens the seven instruments; at most 5 players), **Add section** (opens the section palette), **Reason** box (Interactions), **Reset**.
- Tap a cell: a small picker opens on it: role (five buttons), dynamic (p, mf, f), and for Melody or Bass, **Octave** down, normal, up. Tap a column head: **Move left**, **Move right**, **Remove**. Tap a player's cutout: **Remove player**, and **Solo** (hear only this player while playing, toggle).
- Responds: every change redraws the grid cell and reruns the four checks at once.

### Concert card
- Focus: a printed-program style card (code over a painted paper texture) with the occasion, the tune's credit, the players, the section plan as a strip, and the revision log as "Why we changed it" bullets.
- **Play** plays the final arrangement with the strip highlighting the current section. **Back to Arrange**.
- If any check light is amber, the card shows it under "Still to solve" in plain words.

## Content

### The tune
- "Skip to My Lou", an American play-party song from the 1840s (public domain). The A strain is the familiar chorus, 8 bars of 4/4 (written as 16 bars of 2/4 in many books, the same music), in F major.
- The builder transcribes the melody from a public-domain printing (Content source in Sources) into note names for `MS.parse`, and records the edition in Sources and in the tool's credit comment. The melody's lowest and highest notes, as transcribed, feed the Range check; no other number in this spec depends on the transcription.
- Chords for the A strain (one per bar): F, F, C, C, F, F, C, F (the tune's standard I and V harmony; the builder checks it against the same printing).

### Sections (palette)
- **Intro** options (4 bars each): "Chords only" (the last 4 bars' chords, no melody), "Bass walk-up" (bass alone F2 G2 A2 C3 rising, one note a beat, then 2 bars of chords), "Drum call" (2 bars of hand drum alone, then 2 bars of chords).
- **A** (8 bars): the tune.
- **New section** options (8 bars each, written for Curio Class from the tune's own notes): "Minor turn" (the A melody in D minor, chords Dm, Dm, A, A, Dm, Dm, A, Dm), "Call and answer" (each 2-bar phrase of A sung, then answered by 2 bars of a different player playing it an octave up), "Counter-line" (a new slower line in half notes, F A C A, C E G E, F A C A, C E F rest, written above the A chords so it can sit over the tune).
- **Outro** options: "Last line twice" (the final 2 bars of A played twice, slowing over the last bar), "Hold" (the final F chord held 4 beats, 1 bar). "Last line twice" is 4 bars.
- The default arrangement when the tool opens: occasion Lullaby night, Tempo 72, players Fiddle and Guitar, sections Intro (Chords only), A, A, Outro (Hold); Fiddle Melody mf, Guitar Chords p. That is 21 bars (Hold is 1 bar), 70 s at 72, so its checks open with Length amber ("1:10. Needs 1:30 to 2:30.") as the first thing to solve.

### Instruments (sounding ranges; "school range" is the comfortable range used by the Range check, the tool's own choice for players this age, said on screen)
| Instrument | Full range | School range | Loudness (tool's scale) | Roles allowed |
|---|---|---|---|---|
| Fiddle (violin) | G3 to E7 | G3 to E6 | 3 | Melody, Chords (double stops shown as Chords), Rest |
| Flute | C4 to C7 | C4 to G6 | 2 | Melody, Rest |
| Guitar | E2 to about B5 | E2 to E5 | 2 | Melody, Chords, Bass, Rest |
| Banjo (5-string, open G tuning) | D3 to about D6 | D3 to D5 | 4 | Melody, Chords, Rest |
| Upright bass (sounds an octave below written) | E1 to about G4 | E1 to G3 | 3 | Bass, Rest |
| Accordion | F3 to A6 (treble keys) | F3 to C6 | 4 | Melody, Chords, Bass, Rest |
| Hand drum | unpitched | n/a | 4 | Beat, Rest |
- Sound: synthesized with the music-studio engine (Family engine): fiddle and flute on `MS.blow` with different brightness, guitar and banjo on `MS.pluck` (banjo brighter with a fast decay), bass on `MS.pluck` an octave low, accordion a new reedy voice (two detuned sawtooths through a lowpass), hand drum a new short noise-and-tone hit.
- Roles: Melody plays the section's melody at the chosen octave; Chords plays the bar's chord as a strum on beats 1 and 3 (fiddle: two-note double stops on beat 1); Bass plays the chord root on beat 1 and fifth on beat 3; Beat plays the hand drum on every beat, accented on 1. Dynamics multiply volume: p 0.5, mf 1, f 1.5.

### Occasions
| Occasion | Tempo window | Length window | Special need (part of Fit) |
|---|---|---|---|
| Lullaby night at the library | 60 to 76 | 1:30 to 2:30 | No Beat role and no f dynamic anywhere |
| Harvest square dance in the barn | 112 to 128 | 2:00 to 3:00 | Every A section has a Bass or Beat role (dancers need the pulse) |
| Eighth-grade walk in the courtyard | 84 to 100 | 3:00 to 3:30 | 120 students cross the stage about 1.5 s apart: the music must last at least 180 s, and the Outro must be "Hold" or "Last line twice" so it ends cleanly |

### The four checks (rules)
- **Range**: every Melody and Bass note, at its octave, inside that player's school range. Amber names the player, section and the lowest or highest note that is out ("Flute, A: the low C3 is below the flute's C4. Try Octave up.").
- **Balance**: in each section with a Melody, melody loudness = sum over melody players of loudness times dynamic; the rest = the same for all non-resting non-melody players. Amber when the rest is more than twice the melody ("A, bar 1: melody 3 against 12. The melody is buried."). A section with no Melody (Intro, Outro) is skipped. A section with Melody in no row is amber unless it is an Intro or Outro ("Who has the tune in A?").
- **Length**: seconds = total bars times 4 times 60 / Tempo; amber outside the occasion window, with the number ("2:21. Needs 2:00 to 3:00.").
- **Fit**: Tempo inside the window, the occasion's special need met, and at least one Intro and one New section in the arrangement (the module asks for both). Amber lists the first unmet item.

## Interactions in detail
- Play: plays from the start of the arrangement (or from the tapped column when a column head is tapped with **Play from here**), with a playhead across the grid and the current column outlined. Every control stays live: a role, dynamic, octave, Solo or Tempo change takes effect from the next scheduled note (inside the engine's 150 ms horizon) and the grid redraws at once. Removing the playing section jumps the playhead to the next one. Stop fades in 50 ms.
- Reason box: after the first time all four checks have been looked at (any light tapped or the first Play finished), every later change opens a one-line strip in the panel: "Why?" with six chips (So the melody is heard, To fit the occasion, To keep it in range, For variety, To give a player a rest, So the ending feels finished) and a short text field (60 characters). The reason is optional; a change with no reason is logged as "(no reason given)". The log shows the last 8 entries with **Undo** on the newest.
- Limits: 5 players, 14 sections. A full grid's **Add** buttons are disabled with a tooltip "Five players is the most."
- Switching occasion keeps the arrangement and reruns the checks (that is the point: the same plan fails a different job).
- Saved on this device: the arrangement per occasion and the log (localStorage, try/catch). **Reset** asks "Clear this occasion's arrangement?" with **Clear** and **Keep**.
- Motion off: the playhead jumps per beat instead of gliding; the column outline still moves.
- Sizes: at 1366x768 the grid, check lights, Play and Occasion are visible without scrolling; 14 columns fit by shrinking column width to a 44 px minimum, then the grid scrolls sideways inside its box (never the page). Preview 680x425: grid and check lights readable. At 375 wide: the grid turns so sections are rows and players columns.

## Look
- Accent (`--brand`) #456f22 moss green (a fiddle-case lining). Paper #f6f0e2 (parchment), panel #fffaf0, ink #2b2418, muted #6a5d48. Role colors (always with the role word): Melody #b04a1f, Chords #2d5f8a, Bass #5b3d82, Beat #8a6a12, Rest #d8d0bf with gray text. Check lights: green #2f7a3a with a check, amber #a8600a with an exclamation mark.
- Contrast: ink on paper 13.51:1, on panel 14.75:1; muted 5.65:1 and 6.17:1; brand on paper 5.21:1, on panel 5.69:1; white text on brand 5.92:1. Role blocks carry white text (each 5:1 or more; the builder confirms) or ink on Rest.
- Different from song-form-builder, storyboard-studio (tally red), beat-lab (orange), band-practice (cyan), and from the other 6-8 arts specs in this batch.

## Art
Local FLUX, no people. Style: "warm painted illustration, wood and lamplight".
- Instruments (7 cutouts, one shared prompt "<item>, standing alone on a simple wooden stand, front view, warm painted illustration, plain white background"; 3:4; cutout yes; people no; the player column, and smaller in Add player):
  - fiddle: a violin with its bow resting across it
  - flute: a silver flute on a slim stand
  - guitar: an acoustic guitar with a worn spruce top
  - banjo: a five-string banjo with a round head
  - upright-bass: an upright double bass with its bow
  - accordion: a red piano accordion with mother-of-pearl keys
  - hand-drum: a round frame drum with a goatskin head and wooden rim
- Venues (3, 5:1 strips behind the occasion banner, no cutout, people no):
  - venue-library: "a cozy library reading corner at night with floor lamps, beanbags, shelves of books and a small rug, warm painted illustration"
  - venue-barn: "the inside of a big wooden barn set for a dance with hay bales, string lights and an open dance floor, warm painted illustration"
  - venue-courtyard: "a school courtyard set for a ceremony with rows of empty folding chairs on the grass, a center aisle and a small wooden stage with steps under a balloon arch, warm painted illustration"
- paper-card: "plain cream concert program paper with soft fiber texture, full frame"; 3:4; the Concert card background.
- 11 images, none with people. Drawn in code: the grid, role blocks, ruler, playhead, check lights and every label.

## Voice
Bank voice: `gravel-ranger` (an old fiddler who has played every barn and gym in the county; no neighbor or other spec in this band uses it). Style from the bank. `Curio.voice` with `scope: () => state.mode`. No line plays while the arrangement plays (V.hush on Play); result lines wait for Stop or the end.
- welcomeArrange (how; entering Arrange; stale when any cell or Play is tapped): "Here's an old tune and a job to do. Press Play to hear it, then tap a block to change who plays what."
- checksHow (how; first time a check light turns amber; stale when that light turns green): "Amber means a real band would trip there. Tap the light to see where."
- reasonHow (how; first time the Reason strip opens): "Every change gets a reason. Tap one, or type your own."
- allGreen (event; all four lights turn green; stale on the next change): "That'll work. Every check is green."
- occasionChange (event; occasion switched with any light amber; stale on the next change): "Same plan, new job. See what the checks say now."
- welcomeCard (how; entering Concert card): "Here's your program. Press Play to hear the final version."
- Numbers and amber reasons are on screen only, so every spoken line is fixed.

## Family engine
none (not a family member). Borrows `kit/music-studio.js` as a sound engine, as music-history-radio does: `MS.parse` (tune and sections), `MS.play` with `exclusive: false` per player bus so Solo and per-player gain work, live `p.bpm`, `MS.blow`, `MS.pluck`, `MS.tick`. Adds to the engine (and docs/families/music-studio.md, in the same change): an accordion voice, a hand-drum hit, and chord strums as events (the doc says chords and drums are not in the engine yet; the first tool that needs them adds them).

## Sources
- National Core Arts Standards, Music MU:Cr2, Cr3, Pr4: https://www.nationalartsstandards.org/
- "Skip to My Lou", 1840s play-party song, public domain: Library of Congress, "Skip to My Lou" in the American Folklife Center collections, https://www.loc.gov/ (search "Skip to My Lou"); Wikipedia, "Skip to My Lou" (1840s, Roud 3433). Melody and chords to be transcribed from a public-domain printing found through IMSLP or the Internet Archive; the builder names the edition here.
- Instrument ranges: Samuel Adler, The Study of Orchestration (Norton); Vienna Symphonic Library Academy instrument pages, https://www.vsl.co.at/en/Academy ; banjo open G tuning (gDGBD): Britannica, "Banjo", https://www.britannica.com/art/banjo
- Square dance music keeps a steady, quick walking pulse: CALLERLAB (the callers' association) publishes recommended music speeds, https://www.callerlab.org/ ; the builder checks the 112 to 128 window against it before shipping (the windows are the tool's own, said on screen).
- Occasion windows, school ranges, loudness scale, the balance rule and the New section strains: written for Curio Class (tool's own choices).
- Checks run (Python, 2026-10-29): seconds = bars x 4 x 60 / tempo. Default plan (Intro 4 + A 8 + A 8 + Outro "Hold" 1 = 21 bars) at 72: 70 s, under 1:30, so Length is amber on open as intended. A 40-bar lullaby plan at 68 = 141 s (2:21, inside); at 60 = 160 s, at 76 = 126 s. Square dance: Intro 4 + A x7 + New section 8 + Outro 2 = 70 bars: 150 s at 112, 140 s at 120, 131 s at 128, all inside 2:00 to 3:00. Walk: Intro 4 + A x6 + New x2 + Outro 4 = 72 bars: 180 s at 96, 188 s at 92, 173 s at 100 (too short at 100, so the walk needs 74 bars or a slower tempo), 206 s at 84. 120 walkers x 1.5 s = 180 s. Balance example: Flute mf melody (2) against Banjo, Accordion and Hand drum at mf (12) = 6 times, buried; Fiddle f melody (4.5) against Guitar and Bass at mf (5) passes. Contrast ratios recomputed with the WCAG 2.1 formula.

## Done when
1. Focus: at 1366x768 and 680x425 the arrangement grid is the largest, central thing, with check lights under it.
2. The default plan opens with Length amber; adding A sections until 1:30 turns it green, with the seconds shown matching bars x 240 / tempo.
3. Putting Flute on Melody an octave down shows Range amber naming the lowest note; Octave up fixes it.
4. Balance turns amber for the buried example and green for the passing one; Intro and Outro columns are never flagged for balance.
5. Switching occasion keeps the plan and reruns the checks; Square dance with an A section lacking Bass and Beat shows Fit amber.
6. Tap while it plays: changing a role, dynamic, Solo or Tempo during Play is heard within 150 ms and redrawn at once; removing the playing column moves the playhead on without stopping.
7. The Reason strip appears only after the checks were first looked at, logs chips and text, and Undo reverts the newest change.
8. No voice line plays during Play; how lines speak once in five changes; allGreen speaks each time all four go green.
9. Concert card lists the plan, credit and reasons, and "Still to solve" when any light is amber.
