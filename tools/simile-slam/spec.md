# Simile Slam

## One idea
On a small stage with a mic and a round clock, the student plays short rounds of figurative language: finish a simile with a fresh ending instead of a tired one, say what a metaphor means in a passage, sort simile from metaphor, match an idiom, adage or proverb to its plain meaning, and catch homographs, synonyms and antonyms, and their best comparisons go on a Fresh Wall; a last round reads a short public-domain poem and names what each comparison makes them see, so they learn that a comparison works by what it makes you see.

## Not like
- idiom-illustrator (3-5, spec): idioms drawn literally. Here similes and metaphors made and read, grade 5.
- word-thermometer (6, concept): shades of meaning. Here comparisons and word relationships.
- myth-museum (4, spec): allusions. Here figurative comparisons.
- genre-remix (4, spec): poem structure. Here figurative meaning.
- tone-dial (10, concept): tone. Here figurative language basics.

## Who and how
- Grade 5, ELA, module "Figurative Language" (Language and Reading Literature). Standards: RL.5.4, L.5.5 (a, b, c).
- Driver: one student, or the class with the wall on the projector (tool.json `driver: "student"`). Every line is read on tap.
- Five round types, then the closing poem. Rounds are timed with a gentle 60-second clock that can be turned off (`Clock: on/off`). tool.json `modes: ["Rounds", "Class wall"]`, `minutes: "15-25"`, `grades_label: "Grade 5"`.
- Saving: the Fresh Wall is kept in this browser; footer: "Your wall stays on this device." `Clear my wall` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.5.5a | Finish It: complete a simile or metaphor; tired endings score a spark, fresh fitting endings score three | the ending and a spark count | 2 |
| RL.5.4, L.5.5a | Mean It: read a line in a passage ("The classroom was a zoo") and pick what it says about the thing | the line highlighted in its passage | 3 |
| L.5.5a | Simile or Metaphor: sort 8 lines | two bins | 3 |
| L.5.5b | Say It Plain: match an idiom, adage or proverb to its meaning | matched pairs | 4 |
| L.5.5c | Double Take: homographs (wind and wind; bow and bow) heard in sentences, and synonym and antonym pairs | the word in two sentences with two pictures | 5 |
| RL.5.4 | Closing poem: name what each comparison makes you see | the poem with notes | 6 |

## Screens and modes
Header (kit): title "Simile Slam"; `Rounds`, `Fresh Wall`, `Poem`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A small coffee-house stage with a mic stand, a round clock and Emcee Lark, a meadowlark in a beret. First hint: "Tap Round 1 to start." The first tap reads the round's name; the welcome is queued after it (`welcomeAfter: true`).

**Finish It.** "As quiet as ___." Four chips (a mouse; a snowfall at midnight; a library on Sunday; a loud drum) and a type box. Chips are rated in data: tired (1 spark), fresh and fitting (3), doesn't fit (0, "Is a drum quiet?"). Typed endings: if they match the tired list (a mouse, a lamb), 1 spark and "That one's been used a lot. Try something only you would say."; anything else gets 2 sparks and goes to the wall draft for the student to keep or not. The tool never judges a typed ending as wrong; it reads it back in the full line.

**Mean It.** A short passage (60 to 100 words) with one figurative line lit; three meanings; the right one reads with the line.

**Simile or Metaphor.** 8 lines drop; sort into Simile (uses like or as) or Metaphor (says one thing is another). Tricky lines include "like" used not as a comparison ("I like pizza"), sorted into a third bin: Not a comparison.

**Say It Plain.** 6 idioms, adages and proverbs to 6 meanings (the early bird catches the worm; actions speak louder than words; break the ice; a picture is worth a thousand words; don't count your chickens before they hatch; hit the books).

**Double Take.** A homograph in two sentences ("The wind is strong." "Wind the clock."), each read aloud with its pronunciation; the student taps the picture for each. Then synonym and antonym pairs: sort pairs into Same (enormous, huge) or Opposite (ancient, modern).

**Fresh Wall.** The student's kept lines on a brick wall; tap to hear; print as a poster.

**Closing poem.** Christina Rossetti, "Who Has Seen the Wind?" (1872, public domain). For each comparison line, the student picks what it makes them see (the leaves hanging trembling; the trees bowing down their heads) and why the wind is shown only by what it does.

At 1366x768 the stage and round fit; at 680x425 the clock folds into the header.

## Content
Written for Curio Class except the closing poem:
- Finish It: 12 starters (as quiet as, as tall as, as bright as, as slow as, as cold as, her laugh was a ___, the hallway was a ___, ...), each with 4 rated chips and a tired list.
- Mean It: 8 passages, each with a figurative line and 3 meanings.
- Simile or Metaphor: 16 lines.
- Say It Plain: 12 sayings with meanings.
- Double Take: 8 homographs (wind, bow, tear, lead, live, close, read, minute) with two sentences and pictures each; 12 synonym and antonym pairs.
- Closing poem: Rossetti, "Who Has Seen the Wind?", from "Sing-Song: A Nursery Rhyme Book" (1872), public domain.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The clock is gentle: at 0 the round ends with the score so far; with the clock off, rounds end when all items are done.
- Sparks are shown per round; there's no total leaderboard.
- Class wall: the projector shows the wall of whoever is signed in on that device only.

## Look
- Accent `--brand` #b4235a stage pink (header, curtain, sparks frame); gold #f4c542 (sparks, the spotlight); paper #fdf3f6; ink #2c0a17; muted #6a4f59. Scene: a warm little stage with string lights.
- Contrast (WCAG 2.1, computed): white on brand 6.31:1; brand on paper 5.81:1; ink on paper 16.62:1; muted on paper 6.72:1; ink on gold 11.10:1.
- Never color alone: sparks are counted with a number; bins have words.
- Different from this batch (detective navy, film sepia, track teal, courtroom mahogany).

## Art
Local FLUX (`scripts/localart.py`), no people.
- stage (1); Emcee Lark (4 poses: mic, point, laugh, bow), "A friendly meadowlark emcee in a beret holding a microphone <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- homograph pictures (16): "<wind blowing trees / a hand winding a clock / a bow on a gift / a performer bowing shown as a bird bowing>, flat sticker style, plain white background"; 1:1; cutout yes.
- closing poem pictures (2): "leaves trembling on a branch in wind / trees bending in wind, soft watercolor, no people"; 4:3.
About 23 images. Drawn in code: clock, chips, bins, wall.

## Voice
Bank voice `lively-host` as Emcee Lark (unique in this batch); passages and the closing poem are read by `soft-breath` (unique in this batch). `Curio.voice` with `scope: () => state.round + ':' + state.item`, `welcomeAfter: true`.
- event `round`: "Round {1}: {Finish It}!"
- how `welcome`: "A good comparison makes you see something new. Let's warm up."
- event `line`: the finished line, read whole.
- event `tired`: "That one's been used a lot. Try something only you would say."
- event `fresh`: "Ooh, I can see that!"
- event `noFit`: "Is a {drum} {quiet}?"
- event `homograph`: "{Wind}. {Wind}. Same spelling, different words."
- how `poemHow`: "What does each line make you see?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: round engine, rated chips, bins, wall.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Finish It | Type random words | Typed endings get 2 sparks and are read back in the line; the wall is the student's choice. The round is practice, not a gate. |
| Mean It | Guess | 3 choices; the right one is read with the line. |
| Sorting | Guess bins | 16 lines; each wrong drop says what makes it a simile, a metaphor or not a comparison. |
| Double Take | Tap either picture | Each sentence is read aloud with its pronunciation, so the sound gives it away; that is the skill. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a round: `round`, `welcome` (queued, first time).
2. Finish It: `line`, then `tired`, `fresh` or `noFit`.
3. Double Take: `homograph`.
4. Closing poem: the poem (whole), `poemHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.5.4 and L.5.5 wording | thecorestandards.org, Reading Literature and Language Grade 5 | CCSS ELA 2010 PDF | yes |
| A simile compares using like or as; a metaphor says one thing is another | Poetry Foundation, glossary (simile, metaphor) | Merriam-Webster, simile and metaphor | yes |
| Meanings of the 12 sayings | Merriam-Webster, idiom entries | Cambridge Dictionary, idiom entries | yes |
| "Who Has Seen the Wind?" by Christina Rossetti, in "Sing-Song" (1872), public domain | Project Gutenberg, Sing-Song: A Nursery Rhyme Book | Poetry Foundation, Christina Rossetti, "Who Has Seen the Wind?" | yes |
| Pronunciations of the 8 homographs differ by meaning | Merriam-Webster, each entry | Cambridge Dictionary, each entry | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad b15, 2026-11-09): every Finish It starter has one tired, at least one fresh and one non-fitting chip; the 16 sort lines include at least 2 "like" lines that are not comparisons; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the stage and round fit; at 680x425 the clock folds.
2. Finish It rates chips and reads typed endings back. (L.5.5a)
3. Mean It and the sort work, with a Not a comparison bin. (RL.5.4, L.5.5a)
4. Say It Plain matches sayings to meanings. (L.5.5b)
5. Double Take plays homographs and sorts synonym and antonym pairs. (L.5.5c)
6. The closing poem notes what each comparison shows. (RL.5.4)
7. The Fresh Wall survives a reload where storage works, prints, and `Clear my wall` removes it.
8. Clock off works.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: sparks don't burst; no network requests.

## Open questions
- None for Cory.
