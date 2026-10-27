# Song Form Builder

## One idea
A letter in a song's form is a promise that the same music comes back: build a song from section blocks, and when you change one note in A, every A in the song changes with it, so AB, ABA and rondo become shapes you can see and hear rather than labels to memorize.

## Not like
- melody-maker (3-5, built, same family): composes one 16-beat tune on a solfege grid. Here a section is a short 8-beat phrase and the subject is how sections repeat and contrast; the note grid is only the small editor inside each block.
- dance-pattern-puzzle (3-5, dance): AB and ABA patterns made of movement cards performed at tempos. Here music only and form only: no movement, no tempo challenge (the overlap note: music keeps form, dance keeps movement).
- beat-lab (9-12, same family): its Song view arranges patterns A to H for a produced track. Here at most four short sections, linked copies, form names, and real songs to label by ear.
- note-ninja (3-5): reading notes on a staff. No staff reading here.
- chord-explorer (6-8, same family): harmony and cadences. No chords here, only melody sections.
- band-practice, world-music-map, theory-gym, music-history-radio (this group): timing, world scales and cycles, key analysis, eras. None builds or labels form.
- paint-mixer, art-style-match, depth-detective (3-5 arts): visual art.

## Who and how
- Grade 3-5, music, module "Form and Composition (Music)".
- Topic line: musical form: AB, ABA and rondo
- Driver: students or teacher (pairs on laptops; or a projector, with the class calling "same" or "new" in Listen). 15 to 30 minutes.
- Standards: NCAS MU:Cr2 (organize and develop musical ideas), MU:Cr3 (refine and complete); Listen also serves MU:Re7 (how structure shapes a response).
- Header: title, topic line, modes (`.seg`) **Build** (default) and **Listen**, then kit `motion`, `sound`, `read`. Start from `kit/starter/src.html`.

## Screens and modes

### Build (explore, the default)
- **Song strip** (top of the stage): 8 slots in a row (2 rows of 4 under 760 px wide). A placed block shows its big letter, its shape (A circle, B square, C triangle, D diamond), its color, and a tiny sketch of its 8 notes. Empty slots are dashed outlines with a number.
- **Section shelf** (under the strip): blocks A and B at start, then **+ New section** (adds C, then D; hidden after D). Each shelf block has **Edit** (pencil icon) and **Hear** (play icon, plays that section alone).
- **Editor** (opens in place of the shelf after Edit): the section's 8 beats by 6 rows (do re mi sol la do', the engine's pentatonic rows, so every note sounds good). Tap a cell to set that beat's note, tap it again for a rest. Under the grid: **Instrument** select (marimba, flute, piano, music box), **Done**. Each copy of this section in the strip ripples as notes change.
- Panel (kit `aside`): `hint`, **Play song** (becomes **Stop**), the **Form card**, **Speed** (Slow 84, Medium 100, Quick 120 beats a minute), **Starter songs** select (Sunny Day, Rondo for Recess, Blank), **Clear song**. Saved on this device; **Clear song** also clears the save.
- Strip block buttons (on focus or tap): **Hear**, **Make it A′** (only on A, B or C blocks: turns this copy into a twin, see below), **Remove**.

### Listen (optional challenge)
- Song picker: Hot Cross Buns, Mary Had a Little Lamb, Twinkle Twinkle, Ode to Joy, Row Row Row Your Boat, Frere Jacques.
- Stage: an empty strip with one slot per phrase. **Listen** plays phrase 1, which is placed as an A block automatically. For each next phrase the panel shows **Same as A** (one button per letter used so far), **Almost the same** (one per letter, makes a ′ twin), and **New**. **Hear again** replays the current phrase; **Hear A** replays the first phrase of that letter.
- When every phrase is labeled, the strip shows the form, the Form card names it, and **Play whole song** plays it with the playhead walking the blocks.

## Content

### Starter songs (8 beats per section; numbers are pentatonic rows: 0 do, 1 re, 2 mi, 3 sol, 4 la, 5 high do; `-` is a rest)
- Sunny Day, strip A B A. A (marimba): 0 1 2 2 3 2 1 0. B (flute): 4 4 3 3 2 2 1 -.
- Rondo for Recess, strip A B A C A. A (marimba): 0 2 3 5 3 2 0 -. B (flute): 1 1 2 1 1 1 2 3. C (music box): 5 4 3 4 5 - 5 -.
- Blank: A and B on the shelf, both all rests, strip empty.
- A new C or D starts as 3 3 3 3 3 3 3 3 (all sol) so it is never silent.
- Section colors and shapes: A #c2410c circle, B #3b5bdb square, C #f2b10a triangle (dark letter), D #237032 diamond. A twin (A′) uses its parent's color with diagonal stripes and a ′ after the letter.

### Twins (A′)
- A twin's first 6 beats are linked to its parent (shown with a small chain icon and locked in its editor); beats 7 and 8 are its own. Changing the parent's first 6 beats changes the twin too. A twin starts as an exact copy, so the Form card says "A′ is still the same as A. Change its last two beats." until one differs.

### Form card rules (letters are renamed by first appearance before matching, so B A B reads as ABA; the card then adds "Your B plays the A part.")
Checked in this order; the first match wins:
1. One section only, repeated, no twins (AAA...): "Strophic: the same music every time, like verses of a song."
1b. One letter with its twins only (A A′, A A′ A A′): "A and its twin: the same start with a new ending."
2. Every section different, 3 or more (ABC, ABCD): "Through-composed: nothing comes back."
3. AB: "Binary form: two parts."
4. AABB: "Binary form with each part repeated."
5. ABA: "Ternary form: away and back home."
6. AABA (or AA′BA′): "AABA: a shape used in many popular songs."
7. A returns at least twice with a different section between each return (ABACA, ABACABA, ABABA): "Rondo: A keeps coming back between other parts."
8. Anything else: "This form has no special name, and that's fine." plus the letters.
- Twins count as their parent letter for rules 3 to 7 and are shown with the ′ (AA′BA′ matches rule 6).
- Same-notes check: if two different letters have identical notes, the card adds "A and B have the same notes, so they sound like A A."
- Ending note line (shown, not spoken): for the last block, "Ends on do: sounds finished." or "Ends away from do: sounds like it wants more."

### Listen songs (public domain; note letters in C, quarter-note beats unless marked; h half, dh dotted half, e eighth; phrase boundaries as listed)
- Hot Cross Buns, 4 phrases of 1 bar, form A A B A. A: E D C(h). B: C C C C D D D D (all e).
- Mary Had a Little Lamb, 2 phrases of 4 bars, form A A′. A: E D C D | E E E(h) | D D D(h) | E G G(h). A′: E D C D | E E E E | D D E D | C(whole).
- Twinkle Twinkle, 3 phrases of 4 bars, form A B A. A: C C G G | A A G(h) | F F E E | D D C(h). B: G G F F | E E D(h) | G G F F | E E D(h).
- Ode to Joy (Beethoven, 1824), 4 phrases of 4 bars, form A A′ B A′. A: E E F G | G F E D | C C D E | E(dotted q) D(e) D(h). A′: E E F G | G F E D | C C D E | D(dotted q) C(e) C(h). B: D D E C | D E(e) F(e) E C | D E(e) F(e) E D | C D G3(h).
- Row Row Row Your Boat (6/8, eighth = 1), 4 phrases of 2 bars, form A B C D. A: C(3) C(3) | C(2) D(1) E(3). B: E(2) D(1) E(2) F(1) | G(6). C: C5 C5 C5 G G G | E E E C C C (all 1). D: G(2) F(1) E(2) D(1) | C(6).
- Frere Jacques, 8 phrases of 1 bar, form A A B B C C D D. A: C D E C. B: E F G(h). C: G(e) A(e) G(e) F(e) E C. D: C G3 C(h).
- Song end lines (shown and spoken): "Hot Cross Buns is A A B A." "Mary Had a Little Lamb is A A prime: the second half is a twin." "Twinkle Twinkle is A B A." "Ode to Joy is A A prime B A prime." "Row Row Row Your Boat is A B C D. Nothing comes back." "Frere Jacques is A A B B C C D D. Every part says itself twice."

## Interactions in detail
- Placing: tap a shelf block, then a strip slot (or drag a block onto a slot). Tapping a filled slot with a shelf block selected replaces it. Placing into a slot to the right of an empty one fills the first empty slot instead (no gaps).
- Linked copies: an edit in the editor redraws every copy of that letter in the strip with a 300 ms ripple (a still outline flash with Motion off) and a count "3 copies changed" on the Form card.
- Play song: scheduled on the audio clock (Family engine). A 1-beat lead-in tick, then each block in order with the playhead (a bar over the block and a moving dot over its note sketch). Each section uses its own instrument. After the last block the Form card speaks its line. Stop at any time; editing during play stops play.
- Edge cases: an empty strip makes Play song say "Put a block in the song strip first." (and point at the shelf). A block with all rests plays silence for its 8 beats and its sketch shows "rest". Remove on the last copy of a letter keeps it on the shelf. Clear song asks "Clear the song strip? Yes / No".
- Listen: a wrong label shows "Listen again. Is it exactly the same, a little different, or new?" and replays the phrase next to the letter it was compared with (two short plays). Two misses on one phrase reveal the answer with a one-line reason ("Same start, different ending: a twin."). Listen keeps no score; the strip just fills.
- Keyboard: Tab order is panel buttons, shelf, strip, editor. In the editor, arrows move, Enter or Space sets a note, Delete makes a rest. In the strip, Left and Right move between slots, Enter places the selected shelf block.
- Sizes: strip blocks at least 64 px tall at 1366x768 with 28 px letters; the editor's cells at least 44 px. In the 680x425 preview the strip and Form card show (shelf hidden behind a **Shelf** button), letters at least 14 px. At 375 wide: strip in 2 rows of 4, shelf, editor full width.

## Look
- Accent (`--brand`) #0e7490 deep teal. Paper #f4f7f2, ink #1c2430, muted #556070, cards white with a 2 px #d7e2df line. Section colors as in Content.
- Contrast: white on brand 5.36:1; brand on paper 4.96:1; ink on paper 14.45:1; muted on paper 5.90:1; white on A 5.18:1, on B 5.67:1, on D 6.11:1; ink on C 8.23:1. Section color is never the only signal: every block has its letter and shape.
- Notes in the editor are drawn in the section's color with the syllable written on each, on purpose not the solfege bell colors melody-maker uses, so a block always reads as one section.
- Different from melody-maker (burnt orange #b4532a on cream), paint-mixer (purple), note-ninja (indigo), and every tool in this group.

## Art
none: drawn in code (blocks, shapes, strip, playhead).

## Voice
Bank voice: `playful-friend` (a fun music teacher; no tool in this group or among this tool's neighbors uses it). Style from the bank.
- welcomeBuild (how): "Tap a block on the shelf, then tap a space in the song strip. Then press Play song."
- playHow (how, after the first block is placed): "Press Play song to hear your form."
- editHow (how, first Edit): "Tap the grid to change the notes. Every copy of this section changes too."
- linkedA, linkedB, linkedC, linkedD (event, the first edit after each Edit opens that changes 2 or more copies; stale on the next edit or on Play): "You changed A, so every A changed. Same letter, same music." (B, C and D versions say their letter.)
- twinHow (how, first Make it A′): "A prime starts as a copy. Change its last two beats to make a twin."
- formStrophic, formTwin, formThrough, formBinary, formBinaryRepeat, formTernary, formAABA, formRondo, formOther (event, after Play song finishes; stale when the strip changes or Play starts again): "The same music every time. That's how verses work." / "A and its twin. Same start, new ending." / "Nothing came back. Every part was new." / "A B. Two parts." / "A A B B. Each part says itself twice." / "A B A. You went away and came back home." / "A A B A. Lots of songs use this shape." / "A rondo! A keeps coming back between new parts." / "That shape has no special name, and that's okay."
- sameNotes (event, with the form line): "Two of your sections have the same notes. Change one so it sounds new."
- emptyStrip (event): "Put a block in the song strip first."
- welcomeListen (how): "Press Listen. Then tap Same, Almost the same, or New for each part."
- listenWrong (event, stale on the next answer): "Listen again. Is it exactly the same, a little different, or new?"
- The six song end lines in Content (event).
- Never over music: lines wait until a play ends (`wait: true` on Play); Read stops play first.

## Family engine
music-studio (no family doc yet; this spec holds the full description). Lift the sound parts of melody-maker's src.html into `kit/music-studio.js`, unchanged in sound: `ctx()` (context, master gain, the short room delay), `INSTR` (marimba, flute, piano, music box built from `pluck` and `blow`), `freq(key, semi)`, `KEYS`, `SCALES` (major, penta, minor rows with solfege) and `COL` (solfege colors), plus one new part: `MS.play(events, {bpm, lead, onStep})`, a lookahead scheduler on the audio clock (25 ms timer, 150 ms horizon, the pattern of beat-buddies' `startClock`) that takes `[{beat, semi, dur, instr}]` and returns `{stop()}`, calling `onStep(beatIndex)` in step with the sound for the playhead. melody-maker, chord-explorer and beat-lab keep their own copies until they are next reworked (KIT.md). This tool feeds it: sections as 8 pentatonic row numbers in key C, the strip order, tempo, per-section instrument, and the Listen songs as note names turned into semitones above middle C.

## Sources
- National Core Arts Standards, Music (MU:Cr2, MU:Cr3, MU:Re7): https://www.nationalartsstandards.org/
- Form names (strophic, through-composed, binary, ternary, rondo): Britannica, "Musical form", https://www.britannica.com/art/musical-form ; Britannica, "Rondo", https://www.britannica.com/art/rondo
- AABA as a common popular song form (32-bar form): Open Music Theory, "AABA (32-bar song form)", https://viva.pressbooks.pub/openmusictheory/
- Ode to Joy: Beethoven, Symphony No. 9, finale (1824), public domain score at IMSLP, https://imslp.org/wiki/Symphony_No.9,_Op.125_(Beethoven,_Ludwig_van)
- Twinkle Twinkle (melody "Ah! vous dirai-je, maman", France, 1761), Mary Had a Little Lamb (poem by Sarah Josepha Hale, 1830), Row Row Row Your Boat (published 1881), Hot Cross Buns and Frere Jacques (traditional): public domain; melodies as sung in US music classrooms, checked against the Library of Congress National Jukebox and Songs of America pages, https://www.loc.gov/collections/songs-of-america/
- Starter songs: written for Curio Class.

## Done when
1. Placing A, B, A and pressing Play song plays three sections in order with the playhead, and the Form card says ternary.
2. Changing one note of A in the editor changes every A in the strip (visible and audible), and the linked line plays once for that edit.
3. Every Form card rule in Content gives its line, including B A B read as ABA, AA′BA′ as AABA, and ABACA as rondo.
4. A twin's first 6 beats follow its parent; its last two do not.
5. Listen: each of the six songs can be labeled to the form in Content; a wrong label replays the two phrases side by side.
6. How lines are spoken once in five actions in a row; form lines every Play, dropped when the strip changes.
7. No line plays over the music; Read stops play.
8. Strip, Play song and the Form card are visible without scrolling at 1366x768, 1280x720 and in the 680x425 preview.
