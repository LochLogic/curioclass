# Dance Pattern Puzzle

## One idea
A dance pattern can hide in more than the moves: the dancer may repeat one step but change the side, the level or the facing, so each puzzle asks "what repeats here?", you build the missing cards to keep the pattern going, and the last puzzles are real folk dances (a grapevine, an adding-on dance, the poles of tinikling) cracked the same way.

## Not like
- robot-dance (K computer science, built): copy a target dance card for card and find the one wrong card (a bug). Here there is no target dance to copy: you find a rule (which attribute repeats) and continue it, and every card has four attributes, not just a move.
- song-form-builder (3-5 music, this wave): letters for music sections that change together. Here the letters are found in movement (overlap note: music keeps form, dance keeps movement); the music is a plain count track with no sections.
- loop-garden (robot family): repeat blocks and fewest-block stars. No repeat block or shortest answer here.
- fitness-circuit (3-5 PE, movement family): exercise stations and heart rate. No patterns, no folk dances.
- art-style-match, depth-detective (3-5 art puzzles): visual art. No shared mechanic.
- Dance siblings: levels-and-pathways (levels and pathways shown as a floor ribbon), choreography-board (phrases on a timeline, revised with devices), dance-styles-explorer (styles, traces, critique). Only this tool has move cards with side, level and facing, and folk dances.

## Who and how
- Grade 3-5, arts (dance), module "Patterns in Dance (Dance)".
- Topic line: patterns, tempo and folk dances
- Driver: students in pairs on laptops, or the teacher on a projector with the class dancing each solved pattern. Minutes: 15-30.
- tool.json modes: ["Puzzles", "My dance"]; driver "students or teacher".
- Standards (NCAS dance): DA:Cr2.1.3a to DA:Cr2.1.5a (structure a dance with a beginning, middle and end; patterns), DA:Pr5.1.3b (tempo, moving in time), DA:Cn11.1.3a to DA:Cn11.1.5a (dances from different cultures); also DA:Re7.1.3a (find a movement pattern that creates a phrase). Moved here from levels-and-pathways (integrator, BR1, 2026-10-28): DA:Re7.1.1a and DA:Re7.1.2a (find and describe a repeated movement pattern) and DA:Cr3.1.1b (show movements by picture or symbol). The tool is grades 3 to 5, so the next Spec pass either adds a K-2 entry that teaches them or moves them again (rule 2).

## Screens and modes
Header: title "Dance Pattern Puzzle", small line "Patterns, tempo and folk dances", modes (`.seg`) **🧩 Puzzles** (default) and **💃 My dance**, then kit `motion`, `sound`, `read`. Stage left (dancer on top, card strip under it), panel right; under 1000 px wide the panel goes below with the card maker first.

Focus (both modes): the card strip, where the pattern lives; during Dance it, the dancer and the lit card. The strip is the widest thing on the stage (cards at least 64 px wide and 88 px tall at 1366x768) and sits in the middle band, with the dancer above it at about 45% of the stage height.

Stage (both modes): the `'square'` view from the dance engine: a wooden dance platform in front of the backdrop image (Art), the dancer on it. Under the platform, the **card strip**: up to 10 cards in a row (two rows of 5 under 760 px). A card shows a mini dancer in that card's pose, and three small marks so color is never the signal: a side arrow with a letter (◀ L or R ▶; no arrow for moves with no side), a level bar (three stacked ticks, one filled: top High, middle Middle, bottom Low) and a facing arrow on a small circle (front, right, back, left). A blank card shows a big "?". Under each card a letter space (empty until solved). A count strip above the cards: 2 counts per card.

### Puzzles (opens on the chapter map the first time, then on the last open puzzle)
- **Chapter map**: six chapter tiles in a row (Moves, Sides, Levels, Facing, Adding on, Folk dances), each with three puzzle dots (filled when solved) and a mini pose. Every puzzle is open from the start; the map suggests the next one with a glow.
- **Puzzle screen**: the puzzle name and chapter at the top of the stage, the strip with some "?" cards.
- Panel: `hint`; the **card maker** (enabled when a "?" card is selected): **Move** row (8 icon buttons, plus the chapter's folk moves in Chapter 6), **Side** (◀ L, R ▶), **Level** (High, Middle, Low), **Facing** (Front, Right, Back, Left arrows). Then **▶ Dance it** (big gold), **Tempo** (🐢 Slow 72, 🚶 Medium 96, 🐇 Fast 120 beats a minute; Medium at start), **🔍 Pattern lens**, **↺ Reset puzzle**, **🗺 Chapters**, **⏭ Next puzzle**.
- Opening a puzzle (on the first visit, or from the map) shows its cards at once; nothing auto-plays.
- Select a "?" card: it lifts, and the card maker shows the previous card's values. Each tap in the card maker updates the card at once and the dancer previews it (2 counts, no music).
- Dance it: count-in ("Five, six, seven, eight!"), then the dancer dances the whole strip, each card lighting in turn, to the music at the tempo. If every filled card matches the answer, the letters appear under the cards (Content), a chime, the puzzle dot fills and the dancer repeats the dance once with the letters lighting. If not, the dancer stops on the first wrong card, the card wobbles, and one line names the first attribute that breaks the pattern, in the order move, side, level, facing ("Look at the level."). The card keeps the student's choice.
- Pattern lens: dims the attribute marks that never change in this puzzle and outlines the one that does, with the chapter's word ("Watch the side."). It never shows the answer.

### My dance (free build)
- The strip has 8 empty slots (16 counts). Tap a slot, then the card maker; **➕ Copy card** copies the selected card to the next empty slot, **🪞 Mirror card** copies it with the other side, **🗑 Remove**.
- Letters are worked out live under the cards: the same card gets the same letter; the same card on the other side gets the letter with a prime (A′); the first new card gets the next letter. When the letters form a named pattern, its name shows (AB, AAB, ABB, ABC, AABB, ABBA, ABAC; "No repeat yet" otherwise).
- **Challenge cards** (optional, a small deck in the panel, tap for the next): "Make an AB pattern with one move and two levels." "Make an AABB pattern where only the side changes." "Make an ABC pattern that ends facing front." "Make an ABBA pattern." "Make an adding-on dance: A, AB, ABC." "Use all three levels in one pattern." Each shows a check when the strip fits it.
- **▶ Dance it** and **Tempo** as in Puzzles, plus **🔁 Loop** (repeat until Stop). Dance it is disabled while the strip is empty. Saved on this device; **🧽 Clear** empties the strip and the save.
- Named patterns: the filled cards' letters, with a primed letter counted as its own letter (so A A A′ A′ reads as AABB), must be one named unit repeated whole one or more times (A B A B is AB). The adding-on challenge checks the letters A, A B, A B C in order (6 cards).

## Content
Moves (each card is 2 counts; side applies to all but Clap and Jump; for Turn the side is the turn direction, a quarter turn, and its facing is the facing after the turn): **Step** (step out and together), **Clap**, **Stamp**, **Point** (toe taps out and back), **Kick** (low kick front), **Reach** (one arm reaches out and back), **Jump** (two feet), **Turn** (quarter turn). Levels change the shape through the engine (High on toes with arms up, Low with knees deep).

Puzzles (cards in order; "?" marks a blank; the answers; the letters shown after solving). Cards face front at Middle unless marked.
| # | Name | Cards | Answers | Letters |
|---|---|---|---|---|
| 1-1 | Clap and jump | Clap, Jump, Clap, Jump, Clap, ?, Clap, ? | Jump, Jump | A B A B A B A B |
| 1-2 | Two claps | Clap, Clap, Stamp R, Clap, Clap, Stamp R, ?, ? | Clap, Clap | A A B A A B A A |
| 1-3 | Three in a row | Reach R, Clap, Jump, Reach R, ?, Jump, Reach R, ? | Clap, Clap | A B C A B C A B |
| 2-1 | Right, left | Step R, Step L, Step R, ?, Step R, ?, Step R, Step L | Step L, Step L | A A′ A A′ A A′ A A′ |
| 2-2 | Two and two | Point R, Point R, Point L, Point L, Point R, ?, Point L, ? | Point R, Point L | A A A′ A′ A A A′ A′ |
| 2-3 | Kick and clap | Kick R, Clap, Kick L, Clap, Kick R, Clap, ?, ? | Kick L, Clap | A B A′ B A B A′ B |
| 3-1 | Sky and floor | Reach R High, Reach R Low, Reach R High, Reach R Low, ?, Reach R Low, ?, Reach R Low | Reach R High, Reach R High | A B A B A B A B |
| 3-2 | Elevator | Clap High, Clap Middle, Clap Low, Clap Middle, Clap High, ?, ?, Clap Middle | Clap Middle, Clap Low | A B C B A B C B |
| 3-3 | Two things change | Step R High, Step L High, Step R Low, Step L Low, Step R High, Step L High, ?, ? | Step R Low, Step L Low | A A′ B B′ A A′ B B′ |
| 4-1 | Around the square | Turn R (faces Right), Clap (Right), Turn R (Back), Clap (Back), Turn R (Left), Clap (Left), ?, ? | Turn R (Front), Clap (Front) | no letters (every card differs); the lens word: a quarter turn every 2 cards |
| 4-2 | Stamp and turn | Stamp R (Front), Stamp L (Front), Turn L (Left), Stamp R (Left), Stamp L (Left), Turn L (Back), ?, ? | Stamp R (Back), Stamp L (Back) | A A′ B, A A′ B, A A′ with the facing changed each time |
| 4-3 | Back to front | Jump, Turn R (Right), Jump (Right), Turn R (Back), ?, ?, Jump (Left), Turn R (Front) | Jump (Back), Turn R (Left) | Jump, turn, jump, turn: A B A B with a quarter turn each B |
| 5-1 | Adding on | Clap, Clap, Stamp R, Clap, ?, Jump | Stamp R | A, A B, A B C |
| 5-2 | Going down | Reach R High, Reach R High, Reach R Middle, Reach R High, ?, Reach R Low | Reach R Middle | A, A B, A B C |
| 5-3 | Four rounds | Step R, Step R, Step L, Step R, Step L, Point R, ?, ?, ?, Point L | Step R, Step L, Point R | A, A A′, A A′ B, A A′ B B′ |
| 6-1 | Mayim Mayim grapevine | Cross R front, Side L, ?, Side L, Cross R front, Side L, ?, Side L | Cross R behind, Cross R behind | A B C B A B C B |
| 6-2 | Seven Jumps | Round 3 row: Knee up R, Knee up L, Kneel R. Round 4 row: ?, ?, ?, Kneel L | Knee up R, Knee up L, Kneel R | A A′ B, then A A′ B B′ |
| 6-3 | Tinikling | Poles row (given, 3 counts a bar): tap, tap, close, three times. Dancer row: In, In, Out, In, ?, Out, ?, In, ? | In, In, Out | In In Out, three times |
Notes for the table: Tinikling cards are 1 count each (3 to a bar); all others are 2. In 4-1 the lens word replaces letters because every card differs; the solved screen says "The pattern is in the facing: a quarter turn every two cards." In 4-2 and 4-3 the letters ignore facing on purpose and the solved screen says so ("Same moves, new facing each time"). Cards in 4-x show their facing arrow large.

Folk moves (Chapter 6 only): Cross front (the right foot crosses in front of the left), Side (step to the side), Cross behind (the right foot crosses behind the left); Knee up R and L (stand on one foot, other knee up), Kneel R and L (one knee on the floor); In (hop between the poles), Out (hop outside the poles). The Seven Jumps holds after a round are a still pose on a long note; Tinikling plays in 3 counts a bar.

Culture cards (shown above the strip in Chapter 6, read on screen; Read speaks them):
- Mayim Mayim: "A circle dance from Israel. Mayim means water in Hebrew; the dance was made to celebrate finding water. Its grapevine step crosses in front, steps to the side, crosses behind, steps to the side."
- Seven Jumps: "A folk dance from Denmark. Dancers circle, then hold still poses on long notes. Each round adds one more pose, going lower each time: knees up, then kneeling, then elbows, then the head down."
- Tinikling: "A dance from the Philippines, named for the tikling bird. Two people tap bamboo poles on the ground twice, then close them. The dancer hops in, in, and out, and the poles get faster." Under it, small: "In class, use tape lines or ropes on the floor instead of poles."

Music: original tunes synthesized in the page, one per chapter look: Chapters 1 to 5 a bright folk-band loop in 4 (accordion-like square lead, guitar strum pluck, bass, light drum), Mayim Mayim an original minor-key tune in 4 with hand drum, Seven Jumps an original tune in 2 with long held notes for the holds, Tinikling an original tune in 3 with two wood-block taps and a clap for the poles. No real recordings, no traditional melodies (the steps are traditional; the tunes are ours).

## Interactions in detail
- One run at a time: Dance it while dancing restarts; leaving a puzzle stops the run at once (run token).
- Everything stays live during a run: selecting a card, a card maker tap, Reset puzzle, Chapters or Next puzzle stops the run at once (the dancer holds the current pose, then shows the change); the Pattern lens and Read work without stopping it.
- Tempo changes take effect at once: the clock re-times from the current moment, so the rest of the current card plays at the new speed. Tinikling: **Faster and faster** toggle (on by default in 6-3); when 6-3 is solved, the replay plays the 3 bars four times, each pass 8 beats a minute faster than the last, capped at 120.
- Run lengths: an 8-card strip with count-in and the solved replay is 36 counts (30.0 s at Slow, 22.5 s at Medium); the 10-card puzzle 5-3 is 44 counts (36.7 s at Slow). Over 30 s only at Slow, the student's own choice, and any tap stops it.
- Answers check all four attributes, except where a move has no side (Clap, Jump) and in the cards Content marks. Puzzle 4-1 checks the facing too.
- Reset puzzle puts the "?" cards back. Solved puzzles stay solved for the page session and are saved on this device with the My dance strip (localStorage `dance-pattern-puzzle`); **🧽 Clear** in My dance also clears puzzle progress after a confirm.
- Keyboard: arrow keys move between cards; Enter selects; 1 to 8 pick a move; Q W pick side; A S D pick level; Z X C V pick facing; Space is Dance it.
- Motion off: the dancer shows each card's end pose for its 2 counts; the lit card and the count strip keep the timing.
- Sound off: no music or voice; the count-in shows as big numbers 5 6 7 8.
- My dance letters: compared on move, side, level and facing; a prime means "same but the other side". With 3 or more distinct letters, C, D and so on.

## Look
- Accent `--brand` #1f63c7 (cobalt). Paper #fff8ec, ink #1b2233, muted #535d73, line #ead9bd, panel #ffffff, focus #b45309.
- Contrast: white on accent 5.73:1; accent on paper 5.42:1; ink on paper 15.03:1; muted on paper 6.25:1.
- Card marks are ink on white; a solved card gets a cobalt bottom band with its letter in white (5.73:1). A wrong card shows a red-orange #c0392b outline (5.44:1 on white) and a wobble, plus the hint words.
- The dancer: simple shapes from the engine (no face), cobalt top, cream skirt-shorts, 2 px outline, in front of the painted festival square.
- Different from song-form-builder (teal #0e7490), fitness-circuit (raspberry #c2185b), art-style-match (#9b2457), paint-mixer (purple), melody-maker (burnt orange), robot-dance (magenta), and the dance siblings (teal, mint, lilac).

## Art
Local FLUX (`scripts/localart.py`), one session, no people. One style: "flat painterly style with soft shapes, warm light".
- festival-square: "an open-air town square at golden hour, a low wooden dance platform in the center foreground, strings of round paper lanterns and plain cloth bunting overhead, whitewashed walls with blank shutters, potted plants, warm light, flat painterly style with soft shapes, an empty square"; 16:9; cutout no; people no; the backdrop behind the platform in the engine's `'square'` view, dimmed 20 percent behind the dancer.
- bamboo-pole: "one long straight green and tan bamboo pole lying flat, side view, flat painterly style with soft shapes, plain white background"; 5:1; cutout yes; people no; drawn twice on the floor in puzzle 6-3; the engine slides the two poles apart and together (tap, tap, close) and stretches each to the floor width.
- Culture pictures (one per Chapter 6 culture card, shown above its text; 16:10; cutout no; people no):
  - culture-mayim: "a round stone water well in a sunny green field with young olive trees and a clear blue sky, flat painterly style with soft shapes"; Mayim Mayim.
  - culture-syvspring: "a white Danish farmhouse with a red tile roof beside a green village meadow in summer light, flat painterly style with soft shapes"; Seven Jumps.
  - culture-tikling: "a barred rail bird with a brown back and a black and white striped chest stepping through short grass near two bamboo poles lying on the ground, flat painterly style with soft shapes"; Tinikling (the dance is named for this bird).
- 5 images, none with people. Drawn in code: the dancer and every card's mini dancer (the dance engine's jointed figure: it must bend into 8 moves and 7 folk moves at three levels and four facings, which painted poses cannot cover), the card marks, the count strip, the chapter map and every label.

## Voice
`clear-teacher` (Iapetus): "Say clearly and kindly, like a patient elementary school teacher." Different from song-form-builder (playful-friend), fitness-circuit (big-sister), art-style-match (lively-host), near-and-far (gravel-ranger), robot-dance (lively-host) and the dance siblings (warm-teacher, casual-peer, knowing-guide). Spoken lines are short; card text and culture cards are read on screen. `Curio.voice` with `scope: () => state.mode + ':' + state.puzzle`.
| Key | Kind | When it plays | Line | Stale when |
|---|---|---|---|---|
| wMap | how | chapter map shown on the first visit | Tap a chapter to open its first puzzle. | a chapter tile is tapped |
| wPuzzles | how | first puzzle opened | Find what repeats. Tap a question card, then pick its move, side, level and facing. Then tap Dance it. | a "?" card is tapped, or the puzzle is left |
| wMine | how | entering My dance | Build your own dance. Tap a slot, then pick a move, and watch the letters show your pattern. | a slot is tapped, or mode left |
| countIn | event | every Dance it | Five, six, seven, eight! | run stopped |
| lookMove, lookSide, lookLevel, lookFacing | event | a run stops on a wrong card | Look at the move. / Look at the side. / Look at the level. / Look at the facing. | card changed or new run |
| fixHow | how | the first wrong card of the page load, after its look line | Tap the wobbly card and change it. Then tap Dance it again. | the wobbly card is tapped |
| solved | event | every solve | The pattern holds! Watch it again with the letters. | new run or puzzle left |
| nextHow | how | after the first solved replay | Tap Next puzzle for a new one, or Chapters for the map. | Next puzzle or Chapters is tapped |
| ch1 to ch6 | how | first puzzle opened in each chapter | Moves: the pattern is in which move comes next. / Sides: same move, but watch which side. / Levels: same move, but watch how high or low. / Facing: watch which way the dancer faces. / Adding on: each round adds one more card. / Folk dances: real dances use patterns too. | puzzle left |
| lens | how | first Pattern lens tap | The pattern lens shows what changes. The answer is still yours to find. | puzzle left |
| allChapter | event | a chapter's third puzzle solved | You solved a whole chapter! Tap Chapters to pick another one. | puzzle left |
| challengeMet | event | the strip first fits the current challenge card | That fits the challenge card! | strip changed |
| emptyStrip | event | Space pressed with an empty strip | Tap a slot and pick a move first. | strip changed |
- countIn plays with `wait: true` (as the clock's count-in) so the dancer starts on "one".
- No line names a disabled control: the card maker is named only after a "?" card is the next step, and Dance it is disabled (never named) while the strip is empty.

## Family engine
**dance** (`kit/dance.js`; full description in levels-and-pathways/spec.md). Uses the shared figure, `Dance.poses`, `Dance.level`, `Dance.phrase` (one step per card, 2 counts, `side` for mirroring, `facing`), `Dance.clock` (meter 4, 2 and 3; count-in), `Dance.floor('square')`, `Dance.music`, `Dance.counts`. No trails. Feeds it: 8 moves and 9 folk moves as poses at 3 levels, the 18 puzzles, 4 music tracks, and the Tinikling poles drawn as two moving bars on the floor.

## Sources
- National Core Arts Standards, Dance (2014), grades 3 to 5, DA:Cr2.1, DA:Pr5.1, DA:Cn11.1: https://www.nationalartsstandards.org/
- Patterns, repetition, mirroring and accumulation as ways to structure dance for children: Anne Green Gilbert, Creative Dance for All Ages, 2nd ed. (Human Kinetics, 2015), dance concepts (relationships, form).
- Mayim Mayim: Israeli circle dance celebrating water, grapevine step: Gurit Kadman, Am Roked (Schocken, 1969); "mayim" = water: any Hebrew dictionary (Milon Morfix, https://www.morfix.co.il/).
- Seven Jumps (Danish "Syvspring"), the added still poses in order: Elizabeth Burchenal, Folk-Dances of Denmark (G. Schirmer, 1915).
- Tinikling: Philippine dance with bamboo poles, named after the tikling bird, tap-tap-close pattern in 3: Francisca Reyes Aquino, Philippine Folk Dances, Vol. 1 (1953); National Commission for Culture and the Arts, Philippines: https://ncca.gov.ph/
- Using tape or ropes in place of poles in class: teaching practice, the tool's own suggestion.
- Checks run (Python, 2026-10-29): every puzzle's cards with the listed answers were lettered by the rule in Interactions (same move, side, level and facing: same letter; same but the other side: prime; Clap and Jump have no side), and all thirteen lettered puzzles in the table (1-1 to 3-3, 5-1 to 5-3, 6-1) match; 4-x and 6-2, 6-3 are described in words, and the facing chains in 4-1, 4-2 and 4-3 come back to front as stated. Named patterns: Step R, Step R, Step L, Step L reads AABB (the challenge card); Clap High, Clap Low reads AB; Clap, Stamp, Stamp, Clap reads ABBA; Clap, Clap, Stamp, Clap, Stamp, Jump reads A A B A B C (adding on). This needed the new rule that a primed letter counts as its own letter for naming; without it the AABB challenge could not be met. Run lengths: 36 counts is 30.0 s at 72, 22.5 s at 96, 18.0 s at 120; 44 counts is 36.7 s at 72. Tinikling replay: the old "faster each time, up to 120" from Slow took 7 passes and 40.5 s; four passes of 9 counts are now 26.0 s from 72 and 20.1 s from 96. Contrast ratios in Look recomputed with the WCAG 2.1 formula (values as stated).

## Done when
1. Every puzzle in the table loads with its cards and blanks, and the listed answers solve it; letters appear as in the table.
2. A wrong card stops the dancer on that card and names the first broken attribute in the order move, side, level, facing.
3. The pattern lens outlines the attribute that changes and never fills a card.
4. Tempo changes the dance speed at once, mid-card; the 6-3 replay plays four passes, each 8 faster, never over 120; the painted poles close on count 3.
5. My dance letters are right for A B A′ B, A A B B, A B B A and a 3-letter pattern; each challenge card checks only when the strip fits it; Clear empties the strip and the save.
6. The card maker, Dance it and the strip are visible together at 1366x768 and 1000x625; at 375 wide the strip wraps to two rows and nothing scrolls sideways.
7. Keyboard alone can solve puzzle 2-1.
8. How-to lines are spoken once per load; countIn, look lines and solved speak every time.
9. Every culture card fact has its source in Sources, and each culture card shows its painted picture.
10. Focus: at 1366x768 and 1000x625 the card strip is the widest thing on the stage and the dancer stands above it, in front of the painted square.
11. Tap while it plays: during Dance it, a card tap, a card maker tap, Reset puzzle or Next puzzle stops the run at once; a Tempo tap changes speed mid-card; no stale look or countIn line plays after.

## Open questions
- Folk dances: Mayim Mayim, Seven Jumps and Tinikling are common in US elementary PE and music. Keep these three, or swap one for a dance closer to your students?
- The dancer stays the dance engine's code figure (faceless shapes) because it bends into every move, level and facing. A painted dancer would be a person (Gemini, your review) and need many pose cutouts per move; keep the code figure for the whole dance family?
