# Theory Gym

## One idea
Hold a key up to the music like a lens: slide it and every chord is relabeled with its Roman numeral in that key while notes that don't belong light up, so finding the key, naming the cadence and catching the pivot chord of a modulation all come down to sliding the lens until the music makes sense.

## Not like
- chord-explorer (6-8, built): you choose a key, build chords in it and hear cadences by ear with the chords already labeled. Here the key is unknown and you deduce it from the score; minor keys with the raised leading tone, perfect versus imperfect cadences, and modulation by pivot chord are new.
- note-ninja (3-5): naming single notes. The interval warm-up here goes further (number and quality).
- sound-studio (grade 11 science): frequencies and harmonics as physics, not harmony.
- song-form-builder, music-history-radio, world-music-map, band-practice (this group): form, eras, world tunings, timing. Only this tool reads a score.
- gallery-critique (9-12): analysis by pinning claims on a painting; no music, no lens.
- beat-lab (9-12): production with scale lock; here nothing is composed.

## Who and how
- Grade 9-12, music, module "Music Theory (Music)".
- Topic line: keys, cadences and modulation
- Driver: students (own laptops, headphones optional). 20 to 40 minutes; each set stands alone for 10.
- Standards: NCAS MU:Re7 (analyze how structure and context shape response), MU:Re8 (interpret expressive intent through the elements of music).
- Header: title, topic line, modes **Lens** (explore, default) and **Workout** (puzzle sets), then kit `motion`, `sound`, `read`. Link `kit:curio` then `kit:theme-912`.

## Screens and modes

### Shared score view
- A grand staff (treble and bass) at real pixel size, block chords in four voices (or a single melody line), no key signature (accidentals written on the notes). Under each chord or note a numeral box.
- **The lens**: a translucent blue band right under the staff carrying the key name ("G major"), with **◀** and **▶** (move one step around the circle of fifths), drag to slide, and a **Major / Minor** switch. Major keys in order: C, G, D, A, E, B, F sharp, D flat, A flat, E flat, B flat, F. Minor keys in order: C, G, D, A, E, B, F sharp, C sharp, G sharp, E flat, B flat, F (the usual spellings: the old "same tonics" list would have asked for D flat minor and A flat minor). The ghost key signature of the lens key shows at the start of the staff.
- With the lens on a key: each chord's box shows its Roman numeral in that key, or "?" if it matches no numeral in Content "Lens rules"; each melody note's box shows its scale degree (1 to 7, with "raised 6" or "raised 7" in minor), or "?". Notes outside the key get a red ring and an x; notes that fit only as a raised 6th or 7th in minor get a small "raised 7" or "raised 6" tag. A counter: "7 of 8 chords fit G major" (or "notes" for a melody).
- **Two lenses** toggle: a second band (green outline) appears under the first; each numeral box then shows two numerals, and a chord that fits both gets a gold bracket labeled "fits both".
- **Play passage**; tapping a chord or note plays it; a small keyboard strip under the panel lights the chord's notes.

### Lens (explore)
- Focus: the staff with its numeral boxes and the lens under it, across the full stage width; the panel holds only pickers.
- Panel: `hint`, **Passage** picker (all 17 passages from Workout Sets 1 to 3, named by set and number), the lens controls, **Two lenses**, **Play passage**. Nothing is graded.

### Workout
- Focus: the same staff and lens, with the answer buttons for the current rep directly under the lens (not in a side list), so eye and hand stay on the music.
- Panel: four sets as rows of rep tiles: **Warm-up: intervals** (8), **Set 1: Find the key** (6), **Set 2: Name the cadence** (6), **Set 3: Find the pivot** (5). A tile shows a filled dot when solved with no hints, a hollow dot when solved with hints. Progress is saved on this device; **Clear progress** with a confirm.
- Each rep has **Check** (or **Lock in**), **Spot me** (a hint, up to two per rep) and **Next rep**. Check and Lock in are always enabled; pressed with a choice missing they say what is missing ("Pick a number and a quality first.").
- Warm-up: two notes on the staff (played one after the other, then together). Pick the number (2nd to octave) and the quality (perfect, major, minor, augmented, diminished), then **Check**. A keyboard strip with a half-step counter helps.
- Set 1: slide the lens to the key and press **Lock in**.
- Set 2: the lens is set for you; pick the cadence from **Perfect authentic**, **Imperfect authentic**, **Half**, **Plagal**, **Deceptive**.
- Set 3: Two lenses is on. Set lens 1 to the opening key and lens 2 to the closing key (each checked by its own **Lock in**), then tap the pivot chord.

## Content

### Voicing rule (for every passage)
Bass: the chord root, placed between E2 and D4, nearest the previous bass. Upper three voices: close position under the soprano. Soprano: given where listed; otherwise the chord tone nearest the previous soprano, starting on the third of the first chord. A seventh chord with the root in the soprano leaves out its fifth in the upper voices.

### Warm-up: intervals (lower note first; answer)
C4 G4 perfect 5th; E4 G4 minor 3rd; D4 F sharp 4 major 3rd; F4 B4 augmented 4th; B3 F4 diminished 5th; A3 F4 minor 6th; G3 F4 minor 7th; E flat 4 B flat 4 perfect 5th.
Quality table (half steps): 2nd minor 1, major 2; 3rd minor 3, major 4; 4th perfect 5, augmented 6; 5th diminished 6, perfect 7; 6th minor 8, major 9; 7th minor 10, major 11; octave perfect 12.

### Set 1: Find the key (answer; why it is tricky)
1. Melody: D F sharp A G F sharp E C sharp D. D major (G major fits all but C sharp; B minor and E minor fit every note but do not end home).
2. Melody: F A B flat C D E flat D C B flat. B flat major (the A rules out E flat major, the E flat rules out F major; G minor and C minor fit every note but do not end home).
3. Chords: Am Dm E Am. A minor (C major fits all but the G sharp in E; the raised 7 tag shows in the minor lens).
4. Chords: Em Am B7 Em. E minor (G major fails on D sharp).
5. Melody: E G A B G E D E. E minor (C, G and D major and A, B and D minor also fit every note; only E minor ends home).
6. Chords: F Bb C7 F. F major (D minor and G minor fit every note but end on F, not home).
- Lock in is right when every note fits the lens key (raised 6 and 7 count in minor) and the last note, or the last chord as the tonic triad, is the key's tonic. If every note fits but it ends elsewhere: "Every note fits, but it doesn't end on home. Which key ends here?"

### Set 2: Name the cadence (key; numerals; soprano per chord; answer)
1. C major: I IV V I; soprano E F D C. Perfect authentic.
2. G major: I vi IV V; soprano B B C D. Half.
3. F major: I V I IV I; soprano A G A B flat A. Plagal.
4. D major: I IV V vi; soprano F sharp G A B. Deceptive.
5. A minor: i iv V i; soprano E D B C. Imperfect authentic (the soprano ends on the third).
6. E minor: i VI iv V; soprano B C C B. Half.
- Definitions shown after each answer: perfect authentic, V to I with both in root position and the tonic on top; imperfect authentic, V to I without all of that; half, the phrase stops on V; plagal, IV to I; deceptive, V to vi (or VI in minor).

### Set 3: Find the pivot (chords; keys; pivot; its two numerals)
1. C F C Am D7 G. C major to G major. Am: vi in C, ii in G.
2. C G7 C Dm Bb C7 F. C major to F major. Dm: ii in C, vi in F.
3. G C G Em A7 D. G major to D major. Em: vi in G, ii in D.
4. D G A7 D Em F#7 Bm. D major to B minor. Em: ii in D, iv in B minor.
5. F Bb C F Dm G7 C. F major to C major. Dm: vi in F, ii in C.
- The pivot is the last chord both lenses fit, right before the first chord only the new key fits. Taps: any chord after the pivot gives tooLate ("Too late. The music already turned. Look one chord earlier."), even one that fits both (the last chord of 1, 2, 4 and 5 does); an earlier chord that fits both gives tooEarly ("That one fits both keys too, but the music hasn't turned yet. Look later."); an earlier chord only the old key fits gives stillOld ("That chord is still only in the first key. Look later.").

### Lens rules
- Major: I ii iii IV V vi vii° and V7. Minor: i ii° III iv v VI VII from natural minor, plus V, V7 and vii° with the raised 7th. Upper case major, lower case minor, ° diminished. Notes are compared by spelling (F sharp is not G flat).
- A chord fits a key when its spelled notes match one of these numerals exactly; a melody note fits when it is in the scale (in minor, also the raised 6th and 7th). Lock in (Set 1) judges notes; the counter and "fits both" bracket judge chords by numeral.

### Spot me hints (first, then second)
- Warm-up: "Count the letter names, counting both notes." / "Now count half steps on the keyboard."
- Set 1: "Find a note with a sharp or flat. Which keys have it?" / "Look at the last chord or note. Is it home?"
- Set 2: "Read the numerals of the last two chords." / "Is the tonic on top at the end?"
- Set 3: "Find the first chord only the second lens fits." / "The pivot is just before it."

## Interactions in detail
- Sliding the lens relabels all numerals in 150 ms (instant with Motion off) and plays nothing; Play passage is separate.
- While a passage plays, everything stays live: sliding the lens relabels at once and the passage keeps playing; tapping a chord stops the passage and plays that chord; Check, Lock in, a pivot tap, Next rep or a rep tile stops the passage at once, then its line plays.
- Lock in with a wrong key: "Some notes are still outside the lens." (if any are), or the not-home line above. Two wrong lock-ins open Spot me's first hint.
- Cadence wrong answers name the difference: choosing Perfect when it is Imperfect gives "Close. Look at the top note of the last chord."; Half when Deceptive gives "It ends on vi, not V."; others give "Read the last two numerals again."
- Warm-up: number and quality are checked separately ("Number right, quality wrong").
- Keyboard: ◀ and ▶ keys move the lens when it has focus; Tab reaches chords in order; Enter on a chord plays it (Set 3: chooses it).
- Sizes: at 1366x768 the staff (8 chords) with numeral boxes, lens and answer buttons are visible without scrolling; noteheads at least 12 px tall. In the 680x425 preview the staff and lens of Lens mode, text at least 11 px. At 760 and 375 wide the staff scrolls sideways inside its box with the lens and answer buttons pinned under it.

## Look
- Accent (`--brand`) #1f4fd1 court-line blue on a maple gym floor: paper #f6ecd9, ink #1d1b16, muted #5f5848; fits #276b35, outside #b3261e, pivot bracket #b07d12; lens 2 outline #276b35.
- Contrast (rechecked in Python): white on brand 6.78:1; brand on paper 5.79:1; ink on paper 14.68:1; muted on paper 6.02:1; fits 5.53:1; outside 5.58:1; pivot bracket 3.1:1 (a non-text mark, with its "fits both" label in ink). Outside notes carry an x and a ring, never color alone.
- 9-12 theme: `kit/theme-912.css` as the base, this tool's own colors on `:root`. Minimal celebration: a solved rep fills its dot, nothing more.
- Different from chord-explorer (night navy with colored chord tones), gallery-critique (pink on charcoal), music-history-radio (green on bakelite), storyboard-studio (red on dark), virtual-gallery (lime), city-skyline-studio (cyan), beat-lab (orange on black).

## Art
none: drawn in code. The tool is all notation and diagram (the staff, noteheads, numeral boxes, the lens band and the keyboard strip), each placed by pitch and key, and there is no scene, object or character to paint; the maple floor is a flat color.

## Voice
Bank voice: `firm-captain` (clear directions, like a trainer; not used by any of this tool's neighbors or another spec in this batch). Style from the bank. Uses `Curio.voice`, scope = mode.
- welcomeLens (how; Lens entered; stale once the lens moves): "Slide the lens with the arrow buttons. Watch which chords fit and which notes light up."
- twoHow (how; first Two lenses on; stale once lens 2 moves): "Two lenses. Slide the green one too. A gold bracket marks a chord that fits both keys."
- welcomeWorkout (how; Workout entered; stale once a rep tile is tapped): "Tap a rep tile to start a set."
- warmupHow (how; first Warm-up rep; stale on Check): "Pick the number, then the quality, then press Check."
- set1How (how; first Set 1 rep; stale on Lock in): "Slide the lens to the key, then press Lock in."
- set2How (how; first Set 2 rep; stale once a cadence is picked): "Read the last two chords, then tap the cadence name."
- set3How (how; first Set 3 rep; stale on the first Lock in): "Slide each lens to its key and press its Lock in. Then tap the pivot chord."
- right (event; every right answer; stale on Next rep): "That's it." The answer line is on screen, not spoken.
- outside, notHome, tooEarly, tooLate, stillOld, closePerfect, itEndsOnVi, readAgain, numberRight, missing (event; each wrong try; stale on the next try): the lines in "Interactions in detail" and Content, word for word.
- setDone (event; every set finished; stale on the next rep tile): "Set complete. Tap the next set's first tile."
- Lines never play over Play passage: an action that stops the passage plays its line at once; a line from anything else waits for the passage to end.

## Family engine
none. Sound: a soft piano made from `pluck` partials (the same recipe as melody-maker's piano), chords played with a 15 ms roll from the bass up.

## Sources
- National Core Arts Standards, Music MU:Re7, MU:Re8: https://www.nationalartsstandards.org/
- Intervals (number by letter names, quality by half steps): Open Music Theory, "Intervals", https://viva.pressbooks.pub/openmusictheory/
- Diatonic chords and Roman numerals in major and minor, raised leading tone: Open Music Theory, "Roman numerals and SATB chord construction" and "Minor scales"; Kostka and Payne, Tonal Harmony.
- Cadence types (perfect and imperfect authentic, half, plagal, deceptive): Open Music Theory, "Cadence types", https://viva.pressbooks.pub/openmusictheory/
- Modulation by pivot (common) chord: Open Music Theory, "Modulation", https://viva.pressbooks.pub/openmusictheory/
- Circle of fifths order and key signatures: Britannica, "Key", https://www.britannica.com/art/key-music
- All passages: written for Curio Class.
- Number checks (Python, 2026-10-29, all 24 keys with spelled scales): Set 1, keys that fit every note: 1 D major, B minor, E minor; 2 B flat major, G minor, C minor; 3 A minor only; 4 E minor only; 5 C, G, D major and A, B, D, E minor; 6 F major, D minor, G minor. In each, the answer is the only key that fits and ends home; the old "why it is tricky" notes missed E minor (1), G and C minor (2), three minor keys (5) and G minor (6) and are corrected. Set 2: every soprano note is a tone of its chord. Set 3: by the fit-by-numeral rule the pivot is Am, Dm, Em, Em, Dm as listed, with both numerals right; the last chord of passages 1, 2, 4 and 5 fits both keys, so the tap lines now go by position (any chord after the pivot is tooLate). Warm-up: all 8 intervals match the quality table (half steps 7, 3, 4, 6, 6, 8, 10, 7). Contrast ratios in Look recomputed.

## Done when
1. Sliding the lens over each Set 1 passage gives the fits listed in Sources; only the answer key fits every note and ends home (check every key in Python).
2. Every numeral shown matches the lens rules for all 17 passages in both lenses; melody boxes show scale degrees.
3. Set 2: each passage accepts only its answer; the Perfect versus Imperfect and Half versus Deceptive lines appear.
4. Set 3: each pivot is accepted, earlier and later chords give their lines (a later chord that fits both gives tooLate), and the pivot shows both numerals.
5. Warm-up: all 8 intervals check right, with number and quality judged separately.
6. Focus: the staff, numeral boxes and lens are the largest thing in both modes at 1366x768 and 680x425; answer buttons sit under the lens.
7. A tap while a passage plays: a lens slide relabels in the same frame without stopping it; a chord tap, Check or Lock in stops it at once.
8. Progress dots save and Clear progress empties them.
9. How lines once each in five reps in a row; event lines every time, dropped when stale; no line names a control that is off or hidden.
10. Staff, lens and answer buttons visible without scrolling at 1366x768 and 1280x720; preview readable at 680x425.
