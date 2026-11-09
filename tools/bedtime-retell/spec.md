# Bedtime Retell

## One idea
A sleepy puppet named Moss hears a short picture story read aloud, then asks the student to tell it back; the student puts picture cards in the beginning, middle and end slots and says each part with a frame ("First, the cat lost her hat." "Then..." "At the end..."), a card out of order makes Moss sit up puzzled ("Wait, she found it before she lost it?"), and Moss only drifts off to sleep when the retell has all three parts in order, so they learn to retell a story's beginning, middle and end with sequence words and past-tense frames.

## Not like
- story-stage (K, spec): a teacher-led folktale staging. Here one child retelling to a puppet, ELD, grades K to 2.
- then-what-happened (6-12, spec): narrating a comic strip with help levels, older newcomers. Here a bedtime retell with picture cards for young children.
- i-choose-because (K-2, spec, this batch): giving reasons. Here sequence.
- cause-and-effect-rewind (3-5, spec, this batch): linking causes. Here first, then, at the end.
- classroom-phrases-game (live): classroom requests. Here story language.

## Who and how
- Grades K to 2, English Language Development, module "Retelling Stories". Standards: WIDA ELD-LA (Standard 2, the language of language arts), Narrate key language use (WIDA 2020).
- Driver: one student; class mode is "Story night", a projected story with the class saying the frames together (tool.json `driver: "student"`). Every card, frame and word is read on tap.
- Five stories, one per night. Help setting: Lots (full frames with picture choices for the rest of the sentence), Some (frames with word tiles), Little (frames fade to "First" and a blank). Teacher notes map them to WIDA 1-2, 3-4 and 5-6. tool.json `modes: ["Tonight's story", "Story night"]`, `minutes: "8-12"`, `grades_label: "Grades K-2"`.
- Optional: record your retell and play it to Moss; the privacy line shows: "Your recording stays on this device. Nothing is uploaded." No speech recognition. Nothing else is saved; `Print` prints the three cards with the student's sentences as a tiny book.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| WIDA Narrate (orient: who and where) | Tell who the story is about at the start | the first card and frame | 2 |
| WIDA Narrate (sequence with time words) | Put cards in beginning, middle and end and use First, Then, At the end | the three slots filled in order | 2 |
| WIDA Narrate (past-tense frames) | Pick the past form in each frame (lost, looked, found) | the verb tile in the frame | 3 |
| WIDA ELD-LA (story words, characters, events) | Use story words from the read-aloud in the retell | the word tiles | 3 |
| WIDA Narrate (whole retell) | Hear the whole retell read back and put Moss to sleep | Moss asleep with the retell's words | 4 |

## Screens and modes
Header (kit): title "Bedtime Retell"; `Tonight's story`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more for small hands, icon plus word.

**On load and first tap.** A cozy bedroom at night with a lamp, a window with stars and a small bed where Moss, a soft green puppet, yawns under a quilt; a picture book sits on the nightstand. First hint: "Tap the book to read Moss the story." The first tap starts the story; the welcome is queued after it (`welcomeAfter: true`).

**The story.** Six pages with big pictures, read aloud page by page, each page two short sentences. Stories written for Curio Class:
1. "Nell's Red Hat": the cat Nell loses her hat in the wind, looks in the garden and the shed, and finds it on the scarecrow.
2. "The Lost Boot": a boy's boot gets stuck in mud; his sister pulls it out.
3. "Rain Day": a girl and her grandpa can't go to the park, so they build a blanket fort.
4. "Duck's Big Swim": a duckling is scared of the pond, watches the others, then swims.
5. "Too Many Apples": a bear picks too many apples and shares them with friends.

**Retell.** Moss asks "What happened first?" The student drags one of six picture cards into the first slot, then builds the sentence in the frame "First, [who] [did what]." with tiles (who: Nell, the cat; verb tiles: lost, loses, losed; rest tiles). Moss asks "Then what?" and "How did it end?" A card in the wrong slot makes Moss sit up: "Wait, she found it before she lost it?" A present-tense verb gets "Did it happen already? Try the yesterday word." Then `Read it back` reads the three sentences; Moss smiles, yawns and falls asleep, and the lamp dims.

**Story night.** The projector reads a story and the class says each frame together.

At 1366x768 the bed, cards and slots fit; at 680x425 the cards are below.

## Content
Written for Curio Class: five stories of six pages, each with six picture cards (three keyed beginning, middle and end, three extra moments), frame tiles with keyed past forms and one made-up regular form (losed, finded) to catch, and Moss's puzzled lines per wrong order.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can be moved any time; there is no score.
- With Motion off Moss doesn't sit up or yawn; his face changes in place and the lamp dims at once.

## Look
- Accent `--brand` #3a3577 night indigo (header, quilt, slots); gold #f4c542 (the lamp, the stars, the filled slot); paper #f4f3fa; ink #141230; muted #555370. Scene: a cozy bedroom at night.
- Contrast (WCAG 2.1, computed): white on brand 10.74:1; brand on paper 9.74:1; ink on paper 16.43:1; muted on paper 6.67:1; ink on gold 11.14:1.
- Never color alone: slots are labeled First, Then, At the end with icons (sunrise, arrow, star).
- Different from this batch (terracotta, hallway blue, town green, rewind amber).

## Art
- Moss is a puppet, not a person: Local FLUX (`scripts/localart.py`), "a soft green felt puppet in bed <pose>, soft gouache, plain white background", 5 poses (awake, puzzled, smiling, yawning, asleep); 1:1; cutout yes.
- People art goes to Gemini for the stories with people (the boy and his sister, a Black family; the girl and her grandpa, a Vietnamese American family), about 12 pictures.
- Local FLUX: the bedroom (1); animal story pictures (Nell, duck, bear), about 18.
About 36 images. Drawn in code: slots, frames, tiles.

## Voice
Bank voice `gentle-storyteller` reads the stories and the hint (unique in this batch); Moss is read by `soft-breath`, slow and sleepy (unique in this batch). `Curio.voice` with `scope: () => state.story + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Moss loves a story. Read it to him, then tell it back, first, then, at the end."
- event, whole, `page`: the story page.
- event `ask`: "What happened first?", "Then what?", "How did it end?"
- event `puzzled`: Moss's puzzled line for that wrong order.
- event `tense`: "Did it happen already? Try the yesterday word."
- event, whole, `retell`: the student's retell.
- event `sleep`: a yawn and "Goodnight."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: picture-book pages, card slots with keyed order, frame tiles with keyed past forms, Moss's states, help levels.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Order | Drop cards in any order | Each slot is keyed; Moss stays awake and asks about the order. |
| Extra moments | Use extra cards | The three extra cards are not the keyed beginning, middle or end; Moss asks "Is that the most important part?" |
| Past tense | Pick the first verb tile | Present and made-up forms are caught with the "yesterday word" hint. |
Low stakes by design: there is no score, and Moss always falls asleep in the end once the retell is right.

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the book: `page` (whole) per page, `welcome` (queued, first time).
2. Retell: `ask` per slot; `puzzled` or `tense` as they fire.
3. Read it back: `retell` (whole), then `sleep` (waits).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| WIDA 2020: Standard 2 is the language of language arts; Narrate features include orienting the audience, sequencing events and resolution | WIDA ELD Standards Framework, 2020 Edition | WIDA, Key Language Uses: A Closer Look (2020) | yes |
| Retelling beginning, middle and end with picture supports builds young learners' story language | Reading Rockets, story retelling | Colorín Colorado, retelling with English learners | yes |
Backed twice: 2. Cut: 0.

Checks run (Python, scratchpad b25, 2026-11-09): each story has exactly one keyed order of three cards among six, every keyed verb has one past form and two catches, and no two stories share a keyed verb set; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bed, cards and slots fit; at 680x425 cards are below; controls are 56 px or more.
2. Cards go in keyed order with Moss's puzzled lines. (WIDA Narrate)
3. Frames take past-tense verb tiles and catch the rest. (WIDA Narrate, ELD-LA)
4. Read it back plays the whole retell and Moss falls asleep. (WIDA Narrate)
5. Help levels fade frames as in Who and how; recording shows the privacy line.
6. Story night and the tiny-book Print work.
7. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
8. Motion off: Moss changes face in place; no network requests.
9. Every card, frame and tile is read on tap so a child who can't read yet can play.

## Open questions
- Home-language support: this follows Cory's open question on home-language glossaries for the ELD tools (default used: English only, with pictures and read-aloud).
