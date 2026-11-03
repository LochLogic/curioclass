# Sight Words

## One idea
Plain, calm practice of the Dolch and Fry sight words: pick a list and a set, then read one word at a time in three
modes, from relaxed to timed: Explore, Practice test, Challenge.

Asked for by a grade 2 teacher (docs/Return/two-tools.txt, 2026-11-03). Same look and layout as nonsense-words; build
them as siblings. Not flashy on purpose.

## Not like
- nonsense-words (built at the same time): decoding made-up words. Here the words are real and read by sight.
- letter-lanterns (K): letter sounds with play. Here there is no game.

## Who and how
- Grade 2 (fits K to 3; Fry sets reach older readers), ELA foundational skills. Module:
  ela-2-long-vowels-and-two-syllable-words.
- Standard: CCSS RF.2.3f (recognize and read grade-appropriate irregularly spelled words). Also suits RF.1.3g and
  RF.K.3c; list those in teacher notes only.
- Driver: a child reading aloud with a grown-up or partner, or a teacher on a projector. 5 to 10 minutes.
- tool.json: driver "students", minutes "5-10", modes ["Explore", "Practice test",
  "Challenge"], grades_label "Grades K-3".

## Look
Exactly as nonsense-words: parchment page, deep blue outer border, plain readable medium-size word (about 64 to 96
px), one small flourish in the top bar, nothing moving near the word.

## Content
Use only tools/sight-words/words.json (built from the teacher's three lists in docs/Return/Lists). Embed it as is.
- Dolch sets, in level order: Pre-primer (40), Primer (52), Grade 1 (41), Grade 2 (46), Grade 3 (41), Nouns (95).
- Fry sets: the 1,000 words in ten alphabetical sets of 100, named by letter range. The supplied Fry list has no
  frequency ranks, so the sets are alphabetical for now. Keep the set loader generic, so a ranked list ("First 100",
  "Second 100", ...) can replace it later by editing data only.
- on_both: words found on a Dolch list and on Fry. In a Dolch set such a word shows a small quiet "also Fry" tag under
  it; in a Fry set, "also Dolch". The tag is small and grey, never competing with the word.

## Screens and modes

### Picker (first screen)
Two tabs, Dolch and Fry. Each set is a large button with its name and word count. A teacher can pick one or several
sets. A "Mix" switch shuffles across the picked sets. Remember the picks in localStorage.

### Explore
As nonsense-words: free Back and Next, arrow keys, Shuffle, Flag (F key), a Flagged list, a "12 of 46" counter.

### Practice test
As nonsense-words, with more time: the hourglass is green for 4 seconds, then yellow for 4 seconds, then red. Never
skips on its own, never makes a sound. Forward only. Child-led Right or Not yet, then the next word at once. Skip and
Flag. Session length 20 by default (10, 20, 30, or "the whole set"). End screen with Not yet words and "Practice
these".

### Challenge
As nonsense-words: 30 words from the picked sets, 1 minute cap, Right or Not yet moves on, Skip counts as Not yet,
subtle corner timer, best score kept per set, and the big celebration banner for 30 right in one minute.

## Interactions in detail
Same as nonsense-words. One word at a time. Keyboard and touch. No voice reading the words; instructions only, once.

## Art
Shared with nonsense-words: parchment and the flourish. No people.

## Voice
Instructions only, about 6 lines. Browser voice until the voice night.

## Family engine
None. Share the layout and mode code pattern with nonsense-words (each tool still a single file).

## Done when
- Every Dolch and Fry set loads; counts match words.json.
- Tags show for every on_both word in the right list.
- Practice timings are 4 s green, 4 s yellow; Challenge matches nonsense-words.
