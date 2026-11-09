# Rhyme Time Rumble

## One idea
A listen-only sound show in a bouncy ring: the Red Corner and the Blue Corner take turns on five bouts (Rhyme, Beats, Glue, Sound Spot, Swap), and since no letter ever appears on screen, every answer has to come from the ears, with silly pictures that are built to fool the eyes (the picture that starts the same is never the one that rhymes).

## Not like
- letter-lanterns (k, draft): letters matched to their sounds. Here no print at all: rhyme, syllables, onset and rime, and sounds inside spoken words (phonological awareness).
- big-book-pointer (k, spec, same format): print rules and letter names. Here sounds only.
- blend-bakery (1, concept): blends letter sound jars and reads the word. Here blending is heard only, and the answer is a picture.
- sentence-train (k, concept): spells cargo by sound. Here nothing is spelled.
- story-stage, meet-the-book-makers, word-meaning-yard (k): stories, books and meanings, not sounds.
- socratic-seminar-board (10, spec, same format): a talk map. Different band and play.

## Who and how
- Kindergarten, ELA, module "Rhymes and Sounds" (Foundational Skills). Standard: RF.K.2 (a to e).
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class is two corners (Red Corner: a drum badge; Blue Corner: a bell badge); the corner whose turn it is says its answer out loud, then a helper taps. Every word is spoken and every choice is a picture, so a child alone can play (BASELINE rule 4: alone, both corners are theirs).
- Five bouts, picked from the Fight card in any order, plus `Main event` (two items from each bout, 10 items). tool.json `modes: []`, `minutes: "5-20"`, `grades_label: "Kindergarten"`.
- Not a personal prompt. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RF.K.2a | Rhyme bout: hear a word, pick the picture that rhymes (not the one that starts the same); then say another rhyme aloud | three pictures; the right one bounces into the ring beside the word's picture; `We said one!` | 2 |
| RF.K.2b | Beats bout: hear a word, clap its syllables, pick the number of drums; the drum then beats each syllable as it is said | four drum buttons (1 to 4 drums); the word's syllables pop as drum hits | 3 |
| RF.K.2c | Glue bout: hear an onset and a rime apart (/k/ ... at), say the word, pick it; then the word is split back apart | three pictures; the two sound bubbles join | 4 |
| RF.K.2d | Sound Spot bout: hear a sound and a spot (first, middle, last), pick the CVC word that has it there | three pictures; a three-box sound strip (no letters) whose box glows at that spot | 5 |
| RF.K.2e | Swap bout: hear a word, a sound to change or add, pick the new word | the word's picture morphs into the new one; three pictures | 6 |

## Screens and modes
Header (kit): title "Rhyme Time Rumble"; `Fight card` (list icon); `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** The ring (painted, bouncy, festive), the announcer Rumbles (a fluffy friendly purple monster with a toy microphone) in the middle, both corner badges with 0 points. The Fight card is open: five bout buttons (120 x 120 picture icons: Rhyme a hat on a cat, Beats a drum, Glue a glue bottle, Sound Spot a spotlight on a box, Swap two arrows) and `Main event` (belt icon, gold). First hint: "Pick a bout. Tap Rhyme to start." The first tap on a bout starts it with its own line (`boutStart`); the welcome is queued after it (`welcomeAfter: true`).

**Every bout.**
- Focus: the ring center: the prompt picture (240 x 240, the word heard) and, below it, three answer pictures (200 x 200, equal size, shuffled) or, in Beats, four drum buttons (each shows 1, 2, 3 or 4 painted drums in a row). No letters or words appear anywhere in the ring (picture names are spoken, never printed); the picture's name is read on tap.
- Top bar: Red Corner (drum badge, points) left, Blue Corner (bell badge, points) right; the corner whose turn it is glows and its badge bounces.
- Panel (right, 300 px): hint, `Hear it again` (ear), `Pass` (arrow), `Fight card`.
- A turn: the item is said (`item`, whole). The corner talks and answers out loud, the helper taps. Right on the first pick: 1 point, the picture bounces into the ring, the confirm line plays (`yes`, whole), and the payoff (the rhyme pair said together, the drum beats, the bubbles split, the sound box glows, the morph). Wrong: `no` names the picked picture and what it shares ("Cup starts like cat. Does it rhyme? Cat, cup."), it dims, and the other corner may steal from the two left (1 point). Then the payoff plays. Then the turn passes.
- Six items per bout, three per corner. After the sixth: the bout's cheer, both corners' points, and the Fight card.
- At 1366x768: header 56, corners 60, prompt 240, answers 200, spacing: all above the fold. At 680x425: prompt 120, answers 110, drums 90.

**Bouts.**
- Rhyme: "This is {cat}. Which one rhymes with {cat}?" After the payoff: "Can you say another word that rhymes with {cat}? Say it out loud!" and `We said one!` (thumbs up) plays a cheer (no points, it is the class's word).
- Beats: "Clap the beats in {butterfly}. How many claps?" Payoff: the word said in syllables, a drum hit on each, the drums light one by one.
- Glue: "Glue these sounds: {/k/} ... {at}. What's the word?" Two sound bubbles drift together as they are said. Payoff: "{/k/} ... {at}. {cat}!" and the bubbles pop apart and together again.
- Sound Spot: "Which one has {/m/} at the {start}?" (start, middle or end; the three-box strip shows the spot glowing). Payoff: the word said slowly, sound by sound, each box lighting in turn, the spot's box lighting gold.
- Swap: "This is {cat}. Change {/k/} to {/h/}. What's the new word?" (or "Add {/s/} to the start of {top}."). Payoff: the prompt picture morphs into the new one (a crossfade with sparkles; Motion off: a cut) and both words are said.

**Main event.** Two items from each bout in bout order (10 items, five per corner), then the belt: the corner with more points holds up a painted belt, and both corners get the cheer (`mainEnd`). A tie: both corners hold the belt.

## Content
Sound clips (the class hears these, never a letter name): /k/, /h/, /m/, /s/, /t/, /g/, /b/, /f/, /p/, /n/, /ă/, /ŭ/, /ĭ/, /ŏ/, the onsets /tr/ and /sn/, and the rimes "at", "op", "un", "ish", "ain", "ail". Every picture's word is a clip; Beats words also have a syllable-by-syllable clip.

**Rhyme** (prompt | rhymes | starts the same | other):
1. cat | hat | cup | fan
2. bug | rug | bed | bun
3. log | dog | leg | lock
4. pen | hen | pig | pet
5. cake | snake | coat | cave
6. bee | tree | bat | bean

**Beats** (word | syllables): sun 1 (sun); rabbit 2 (rab-bit); pumpkin 2 (pump-kin); butterfly 3 (but-ter-fly); banana 3 (ba-na-na); alligator 4 (al-li-ga-tor).

**Glue** (onset + rime | right | same rime | same onset):
1. /k/ + at | cat | hat | cap
2. /m/ + op | mop | top | map
3. /s/ + un | sun | bun | sock
4. /f/ + ish | fish | dish | fan
5. /tr/ + ain | train | rain | tray
6. /sn/ + ail | snail | nail | snake

**Sound Spot** (sound, spot | right | two others; none ends in /l/, /r/ or /ks/):
1. /m/, start | mop | top, sun
2. /s/, start | sock | bus (/s/ at the end), rock
3. /ŭ/, middle | cup | cap, kit
4. /ĭ/, middle | pig | pan, pup
5. /t/, end | hat | ham, top (/t/ at the start)
6. /g/, end | bag | bat, gum (/g/ at the start)

**Swap** (word, change | right | two one-change-elsewhere words):
1. cat, change /k/ to /h/ | hat | cap, cot
2. bag, change /ă/ to /ŭ/ | bug | bat, rag
3. cap, change /p/ to /t/ | cat | map, cup
4. sun, change /s/ to /b/ | bun | run, sub
5. map, change /ă/ to /ŏ/ | mop | cap, mat
6. top, add /s/ to the start | stop (a stop sign) | tops (two spinning tops: added at the end), mop

**Main event**: Rhyme 1 and 4, Beats 2 and 4, Glue 1 and 5, Sound Spot 2 and 5, Swap 1 and 6.

## Interactions in detail
- Every tap acts at once; a picture tap during the item line reads that picture's name and stops the line; a pick acts at once. `Hear it again` replays the item.
- The first pick of the corner whose turn it is scores; a steal is one pick by the other corner. A second wrong pick (the steal) shows the right picture with its payoff and no point.
- `Pass` gives the item to the other corner as a steal with all three pictures.
- Bouts can be replayed; items come in the same order each time, with pictures shuffled.
- Corner points carry across bouts until `New show` (on the Fight card, circle arrow).
- Motion off: no bounces, drifting bubbles or morphs; states change at once on the same timing; the drum still sounds (Sound on) and its drums light.

## Look
- Accent `--brand` #b0172f ring red (header, Red Corner); Blue Corner #1f4fbf; gold #ffcf33 (Main event, the belt, the spot's glow); paper #fff8f0; ink #24140f; muted #67524a. Scene: a soft, bouncy party ring with balloons, not a fighting ring.
- Contrast (WCAG 2.1, computed): white on brand 6.98:1; brand on paper 6.62:1; white on blue 7.17:1; blue on paper 6.81:1; ink on paper 16.87:1; muted on paper 6.92:1; ink on gold 12.03:1.
- Never color alone: corners have badges (drum, bell); right picks bounce with a check icon; dimmed picks show an x.
- Different from the K ELA neighbors (letter-lanterns night indigo, big-book-pointer brick, meet-the-book-makers amber) and this batch (teal, magenta, olive, violet).

## Art
Local FLUX (`scripts/localart.py`); no people. Pictures are bright, simple and silly (a cat wearing a hat is fine), each a single clear object.
- ring: "A soft bouncy party ring with padded ropes, balloons and confetti in a bright gym, cheerful gouache, the ring floor clear"; 16:9; cutout no.
- rumbles-idle, rumbles-ask, rumbles-cheer, rumbles-think: "A fluffy friendly purple monster with a toy microphone, <smiling / leaning in asking / cheering with arms up / tapping its chin>, cheerful gouache, plain white background"; 3:4; cutout yes; center of the ring.
- belt: "A shiny toy champion belt with a big gold buckle, blank plate, cheerful gouache, plain white background"; 3:1; cutout yes.
- drum: "A small red toy drum, cheerful gouache, plain white background"; 1:1; cutout yes (repeated 1 to 4 times on a button).
- word pictures (57): one per word in Content, each "A <word> <a short silly touch where it helps: a hat on a cat>, cheerful gouache, plain white background", 1:1, cutout yes: cat, hat, cup, fan, bug, rug, bed, bun, log, dog, leg, lock, pen, hen, pig, pet, cake, snake, coat, cave, bee, tree, bat, bean, sun, rabbit, pumpkin, butterfly, banana, alligator, cap, mop, top, map, sock, fish, dish, train, rain, tray, snail, nail, bus, rock, kit (a toy kit box), pan, pup, ham, bag, gum, cot, rag, run (a running rabbit), sub (a sub sandwich), mat, stop (a stop sign with a blank face), tops (two spinning tops). The stop sign's face stays blank (no letters on screen).
About 64 images, no people. Drawn in code: the corner badges and points, the sound bubbles, the three-box sound strip, sparkles, every control.

## Voice
Bank voice `hero-coach` (style "Say with bright, encouraging energy, like a friendly superhero coach") as Rumbles. Not used by K ELA neighbors (letter-lanterns playful-friend) or batch 1. Sound clips are recorded separately as clean isolated sounds (stops crisp with no added "uh", held sounds about 0.8 s), as in letter-lanterns. `Curio.voice` with `scope: () => state.bout + ':' + state.item`, `welcomeAfter: true`.
- event `boutStart`: "{Rhyme} bout! Ears ready!"
- how `welcome`: "Welcome to Rhyme Time Rumble! No letters here. Just listen! Red Corner and Blue Corner take turns."
- how `boutHow` (once per bout): Rhyme "I say a word. You find the picture that rhymes." Beats "Clap the beats. Then tap the drums." Glue "I say two sounds. Glue them into a word." Sound Spot "Listen for the sound and where it is." Swap "Change one sound to make a new word."
- event, whole, `item`: the item line (Bouts), then "{Red} Corner, tap a picture."
- event `name`: the picture's word.
- event, whole, `yes`: "Yes! {cat}, {hat}. They rhyme!" / "{But-ter-fly}. Three beats!" / "{/k/} ... {at}. {Cat}!" / "{Mop}. {/m/} is at the start!" / "{Cat} turns into {hat}!"
- event `no`: Rhyme "{Cup} starts like {cat}. Does it rhyme? {Cat}, {cup}." / Beats "Let's clap it again: {but-ter-fly}." / Glue "{Hat}? Listen to the first sound: {/k/}." / Spot "{Bus} has {/s/} at the end. We need it at the start." / Swap "{Cap} changed the end sound. We change the first sound." Then "{Blue} Corner, can you steal it?"
- event `steal` / `noSteal`: "Stolen! A point for {Blue} Corner!" / "Here it is!" (then the payoff).
- event `turn`: "{Blue} Corner, you're up!"
- event `produce`: "Can you say another word that rhymes with {cat}? Say it out loud!" event `saidOne`: "Rhyme time!"
- event, whole, `boutEnd`: "Bout over! Red Corner {n}, Blue Corner {m}. Great listening!"
- event, whole, `mainEnd`: "And the belt goes to ... {Red} Corner! Everybody give a cheer!" (tie: "It's a tie! You both get the belt!")
Read speaks the hint, which names the current action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Rhyme | Guess; pick the picture that starts the same; the one that looks like the prompt | 1 in 3; every item has a same-start picture (the common wrong answer) and it is always wrong; pictures are unrelated in look; six right by chance 1 in 729 (computed 0.00137). |
| Beats | Guess; always pick 2 | 1 in 4; answers 1, 2, 2, 3, 3, 4, so a fixed answer wins at most 2 of 6 (computed). The drum payoff plays every time, so wrong counts are corrected by ear. |
| Glue | Pick the rhyming picture; the one that starts the same | Each item has a same-rime and a same-onset picture; only blending both parts gives one word. |
| Sound Spot | Pick any picture that has the sound | Items 2, 5 and 6 include a picture with the sound in the wrong spot (bus, top, gum; computed); items 3 and 4 put the other choices' vowels in the middle too. |
| Swap | Pick any one-sound change; the picture that looks like the prompt | Both wrong pictures are one sound away from the prompt word, in the other positions (computed for 1 to 5; item 6 adds at the end instead of the start), so only changing the named spot works. |
| Answer on screen | Read the answer | No letters or words appear in the ring; the stop sign is blank; picture names are only spoken. |
| Doing nothing / mashing | Wait; tap all three | A turn scores only on its first pick; mashing gives the other corner a steal. Pass gives points away. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a bout: `boutStart`, then `welcome` (queued, first bout only), then `boutHow` (first time per bout), then `item` (whole).
2. Picture taps play `name`. A pick plays `yes` (whole) with the payoff, or `no` then the steal ask; a steal plays `steal`/`noSteal`, then the payoff. Rhyme adds `produce`; `We said one!` plays `saidOne`. Then `turn`, then the next `item`, which waits for the payoff.
3. After item 6: `boutEnd` (whole). Main event ends with `mainEnd` (whole).
Every sound inside a line is its recorded clip, never a letter name; no letter is ever named.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RF.K.2 a to e wording (recognize and produce rhyming words; count, pronounce, blend and segment syllables; blend and segment onsets and rimes; isolate and pronounce initial, medial vowel and final sounds in three-phoneme words, not ending in /l/, /r/ or /x/; add or substitute individual sounds in simple one-syllable words to make new words) | thecorestandards.org, Reading: Foundational Skills K (RF.K.2) | CCSS ELA 2010 PDF, Reading Standards: Foundational Skills K-5 | yes |
| Syllable counts of the Beats words (sun 1, rabbit 2, pumpkin 2, butterfly 3, banana 3, alligator 4) | Merriam-Webster dictionary entries (syllable breaks) | Cambridge Dictionary entries (pronunciation) | yes |
Backed twice: 2. Cut: 0.

Checks run (Python, scratchpad b2/rumble.py, 2026-11-08): Beats answers 1, 2, 2, 3, 3, 4 (a fixed answer wins at most 2 of 6; all six by guessing 1 in 4,096); every Sound Spot answer has its sound in the named spot and no distractor does; bus, top and gum carry the sound in another spot; no Sound Spot word ends in /l/, /r/ or /ks/; every Swap rule turns the prompt into the right word, and both distractors are exactly one sound from the prompt in another spot (items 1 to 5); six right in a bout by chance 1 in 729; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the prompt picture, three answers (or four drums) and both corners show with no scroll; at 680x425 the same with smaller pictures.
2. Rhyme: all six take only the rhyming picture; the same-start picture gets its own line; `We said one!` cheers. (RF.K.2a)
3. Beats: all six take only the right drum count; the payoff beats each syllable. (RF.K.2b)
4. Glue: all six take only the blended word; the bubbles join and split. (RF.K.2c)
5. Sound Spot: all six take only the word with the sound in the named spot; the strip's box glows at that spot. (RF.K.2d)
6. Swap: all six take only the new word; the picture morphs. (RF.K.2e)
7. No letter or written word appears anywhere in the ring, and no line names a letter.
8. Scores follow the rules (first pick 1, steal 1, Pass gives a steal); Main event plays its ten items and awards the belt (or a tie).
9. Tap while it plays: a picture tap during the item line names it and stops the line; no older line plays after a newer one.
10. Every sound clip is a clean isolated sound (no "uh" after /k/, /t/, /g/, /b/, /p/).
11. Motion off: no bounces or morphs, same pacing; no network requests; nothing saved.

## Open questions
- None for Cory.
