# Nonsense Words

## One idea
A calm, plain reading drill: one made-up word at a time, so a child has to sound it out letter by letter instead of
guessing from memory. Three modes go from relaxed to timed: Explore, Practice test, Challenge.

Asked for by a grade 2 teacher (docs/Return/two-tools.txt, 2026-11-03). Not flashy on purpose: no distractions while a
child is reading. One small fun flourish in the top bar is fine; nothing moves near the word.

## Not like
- vowel-team-tag (grade 2, same module): a race game with vowel teams in real words. Here there is no game, only
  reading made-up words aloud to a grown-up or partner.
- blend-bakery (grade 1) and letter-lanterns (K): taught sounds with play. Here the sounds are already taught; this is
  fluency practice.
- sight-words (grade 2, built at the same time): real words read by sight. This tool is the opposite skill: words you
  can only decode. The two share a look and layout on purpose; build them as siblings.

## Who and how
- Grade 2 (fits grades 1 to 3), ELA foundational skills. Module: ela-2-long-vowels-and-two-syllable-words.
- Standard: CCSS RF.2.3a (short and long vowels in regularly spelled one-syllable words; CVC is short, CVCe is long).
- Driver: a child reading aloud with a teacher, aide, parent or partner beside them, who also marks right or wrong if
  the child can't yet judge. 5 to 10 minutes. Also used by a teacher on a projector for a whole-class warm-up.
- tool.json: driver "students", minutes "5-10", modes ["Explore", "Practice test",
  "Challenge"], grades_label "Grades 1-3".
- Also listed later on the Supply Closet's Learning Supports shelf. Teacher notes may say decodable nonsense words are a
  common structured-literacy practice, including for children with dyslexia; never call it a diagnosis, treatment or
  clinically proven.

## Look
- Page background: warm parchment (a soft paper texture made in code or a light image; keep it quiet). A deep blue
  border around the whole outer edge of the page.
- The word: plain, very readable sans serif (system font stack is fine; a single-story "a" helps early readers if
  the font has it), dark ink on the parchment, medium size: about 64 to 96 px on a laptop, never filling the screen.
  Lowercase. Centered. Nothing else moves while a word is up.
- Top bar: title, mode buttons, Sound and Motion. The one flourish lives here (for example a small inked quill or a
  letter that wiggles once when a session ends). Keep it still during a word.
- Large, plain buttons, readable for a 7 year old: icons plus one word.

## Content
The bank is tools/nonsense-words/words.txt: 200 words (114 CVC short vowel, 50 CVCe long vowel with silent e, 36 with
the letter pairs sh, ch, th). Embed it as is. The owner reads and approves this list before the tool ships; it was
filtered against real words, sound-alikes of real words and a rude-word list. Do not add words. If you think a word in
it reads as rude or real, leave it in, and list it in handoff.md for the owner.

A teacher can choose which kinds are in play (CVC, CVCe, letter pairs, or all), default all, shown as three toggles.

## Screens and modes

### Explore (opens first)
- The full 200-word bank, in a stable order (grouped by kind, then as listed). A small "12 of 200" counter.
- Back and Next buttons and the arrow keys move freely both ways. A Shuffle button reorders the bank.
- Flag button (and F key) marks a word to come back to; a flag shows on the word. A "Flagged (3)" button shows only
  flagged words; tap a word there to jump to it. Flags persist in localStorage for the session's kinds.
- No timer, no scoring.

### Practice test (Challenge with less stress)
- A run through the words in play, shuffled. Forward only: there is no Back.
- An hourglass timer beside the word (not over it): green sand for 2 seconds, then yellow for 2 seconds, then red. It
  never skips the word on its own and never makes a sound; red only means "take your time and try".
- The child (or grown-up) marks each word with a big green check (Right) or a red mark (Not yet). Marking moves to the
  next word right away. Keyboard: Right arrow or R for right, Left arrow or N for not yet.
- Skip moves forward with no mark. Flag works as in Explore.
- Session length: 20 words by default (10, 20, 30 choice). End screen: number right, a list of Not yet and skipped
  words, and "Practice these" which opens Explore with just those words.

### Challenge
- 30 words per session, shuffled from the words in play. A 1 minute cap.
- Self-scoring with automatic progression: Right or Not yet moves on at once. A Skip button counts as Not yet.
- A subtle timer in a corner (a thin ring or small 0:42), never large or red-flashing.
- When time runs out, the session ends and shows the score (for example 23 of 30 right). The child's best score is kept
  in localStorage and shown on the end screen.
- 30 right inside one minute: a big celebration banner across the screen, with a cheer sound if Sound is on, and
  confetti if Motion is on. Lesser results get a calm, warm line ("23 right in one minute. Beat it next time?").

## Interactions in detail
- One word visible at a time, always.
- Every control works by keyboard and by touch; buttons at least 56 px tall.
- No reading voice for the words themselves: the child must read them. Voice is for short instructions only, and
  only when a mode starts ("Read each word out loud. Tap the green check if you read it right."), spoken once.
- Remember the last mode and kinds in localStorage.

## Art
Parchment texture and the top-bar flourish only. No people, no characters. Small icons can be drawn in code.

## Voice
Instructions only, about 6 lines (mode intros, Challenge start, the 30 of 30 cheer line). The browser voice is fine
until the voice night.

## Family engine
None. Build it to share a layout with sight-words, which uses the same three modes.

## Done when
- All three modes work as written, with the timings above.
- The bank is exactly words.txt; kinds toggles filter it.
- No word ever moves on by itself in Practice test.
- The size goal (2 MB) is easy here; it should be far under it.
