# Mood in the Pictures

## One idea
One story moment (the troll under the bridge in "The Three Billy Goats Gruff") comes three ways behind three doors, Words, Panels and Performance, and the student sets a mood dial after each and tags what every picture and sound adds, follows or changes from the words, then swaps one panel for another artist's version of the same moment and watches the mood strip swing while the words stay exactly the same, so they see that an illustrator or performer is also telling the story.

## Not like
- windblown-pages (K-2, spec): putting pictures back with their pages. Here comparing what the pictures and sound add to the same words.
- page-to-screen (10, concept): storyboarding a film. Here reading versions, not making one.
- dialogue-director (concept): making a comic. Here judging comics others made.
- side-by-side-reader (3-5, spec): two different texts compared. Here one text in three media.
- two-sides-theater (2, spec): one event told from two characters' sides. Here one telling given three treatments.

## Who and how
- Grades 3-5, ELA, module "Pictures, Panels and Performances" (Reading Literature). Standards: RL.3.7, RL.4.7, RL.5.7.
- Driver: one student or a pair (tool.json `driver: "student"`). Text is read on tap; the Performance door is audio by design (captions shown under it).
- Three moments: Troll Under the Bridge (Three Billy Goats Gruff), Wolf at the Door (Aesop, "The Wolf and the Kid"), Lantern in the Storm (an original Curio Class scene). Grade picker (3, 4, 5) sets which tasks show. tool.json `modes: []`, `minutes: "15-25"`, `grades_label: "Grades 3-5"`.
- Nothing is saved; `Print` prints the mood strip and tags.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.3.7 | Panels: tap what the pictures add (a shadow, a worried face, a clue) and tag it mood, character, setting or clue | tag pins on the panels | 2, 3 |
| RL.3.7 | Words then Panels: set the mood dial after each | the dial readings on the strip | 2 |
| RL.4.7 | Grade 4 and up: link each tag to the exact line it follows, or mark it "adds" or "changes" | a thread from tag to line | 4 |
| RL.4.7 | Performance: tap where the voice or music follows a direction in the text ("in a deep voice", "trip, trap") | marks on the audio timeline | 5 |
| RL.5.7 | Swap a panel for another artist's version; the mood strip updates and the student says what changed | two mood strips and a sentence | 6 |
| RL.5.7 | Compare the three doors on one strip and finish "The ___ version made it feel ___ because ___" | the strip and the sentence | 7 |

## Screens and modes
Header (kit): title "Mood in the Pictures"; `Moments`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A dim gallery hall with three doors (Words, Panels, Performance) and Lumen the moth, a museum guide with a tiny lantern. First hint: "Tap the Words door to start." The first tap opens Words with its line; the welcome is queued after it (`welcomeAfter: true`).

**Words.** The moment as plain text (8 to 10 sentences, read on tap, no pictures). Then the mood dial: a half-circle with five picture faces and words (calm, cheerful, tense, scary, funny); drag the pointer.

**Panels.** Four comic panels of the same text (the words appear in captions). 12 to 16 hot spots per moment (in data) the student can tap: each opens a tag tray (mood, character, setting, clue). Tags are checked against data: a shadow under the bridge is mood; a goat's raised hoof is character. At grade 4 and up, each tag also gets "follows the words" (thread to a line), "adds" (nothing in the text says it) or "changes" (it differs from the text: the troll drawn small when the text says big). Then the mood dial again.

**Performance.** The same words read as a produced performance: narrator, character voices, footsteps and a music cue (made in code: a few low notes for tense, bright notes for calm). A timeline under it with captions. The student taps the timeline where the sound follows a direction in the text (data: 4 to 6 per moment) or adds something the text doesn't say (a thunder roll). Then the dial.

**Mood strip and swap.** Three dial readings side by side. `Swap a panel`: panel 3 can be replaced with a second artist's version (a different style, same words); the student sets the dial again and the strip shows both. Grade 5 completes the compare sentence from tiles or by typing.

At 1366x768 four panels and the tag tray fit; at 680x425 panels show two at a time.

## Content
- **Troll Under the Bridge.** Retold for Curio Class from the Norwegian tale collected by Asbjørnsen and Moe (G. W. Dasent's 1859 English translation is public domain). The moment: the smallest goat crosses, the troll calls out, the goat says wait for the bigger brother. Text directions used in Performance: "trip, trap", the troll's voice, "a tiny voice", the creak of the bridge.
- **Wolf at the Door.** Retold from Aesop, "The Wolf and the Kid" (public domain in the 1894 Jacobs and 1919 Library of Congress tellings): the mother goat warns the kid; the wolf knocks and copies her voice; the kid asks to see a white paw. No one is harmed in this moment.
- **Lantern in the Storm** (original): a girl carries a lantern to the barn in a storm to check on a calf; the text says nothing about how she feels, so the art carries the mood.
- Artists: style A (bright picture-book gouache) and style B (dark woodcut) are both made locally for each moment; a public-domain illustration may replace style B for the Troll at build if a plate is found whose rights page says public domain (its id is logged then; a flag).
- Hot spots: 12 to 16 per moment, each with its tag and its follows, adds or changes mark.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A wrong tag shows a hint ("Look at where the shadow falls. What feeling does it make?") and lets the student try again; tags are not scored.
- The dial has no right answer; the strip shows the student's own readings. Only tags and timeline marks are checked.
- The Performance plays in full once, then the timeline can be scrubbed; Sound off shows captions only with a note that the door works best with sound.

## Look
- Accent `--brand` #5b3a7a gallery plum (header, door frames, the strip); gold #f4c542 (Lumen's lantern glow, tag pins); paper #f8f5fb; ink #1f1529; muted #5d5468. Scene: a dim museum hall with three tall doors.
- Contrast (WCAG 2.1, computed): white on brand 9.01:1; brand on paper 8.34:1; ink on paper 16.24:1; muted on paper 6.63:1; ink on gold 10.78:1.
- Never color alone: dial faces carry words; tag types have icons (a heart for mood, a person for character, a tree for setting, a magnifier for clue).
- Different from this batch (planetarium navy, radio orange, reading-table green, story teal).

## Art
Local FLUX (`scripts/localart.py`); the Lantern girl is a person drawn small and from behind in the storm, so local art is used for the moment; Lumen is a moth.
- hall (1): "A dim museum hall with three tall wooden doors, soft gouache, no text"; 16:9; cutout no.
- Lumen (4, wave, point, glow, think): "A small friendly moth museum guide holding a tiny lantern <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- panels (24): "<scene>, <bright picture-book gouache / dark woodcut print style>, no text"; 4:3; cutout no. Four panels times three moments times two styles.
About 29 images. Drawn in code: dial, strip, tags, threads, timeline, music cues.

## Voice
Bank voice `smooth-narrator` as Lumen and as the narrator of the Words door (unique in this batch). The Performance is produced audio: the same narrator plus character takes (troll, goat, wolf, kid, mother goat) generated with the bank's performance settings; footsteps from the kit sound set. `Curio.voice` with `scope: () => state.moment + ':' + state.door`, `welcomeAfter: true`.
- event, whole, `line`: the tapped sentence.
- how `welcome`: "Welcome to the gallery. Behind each door is the same moment, told a different way. Read the words first, then see what the pictures and sounds add."
- how `dialHow`: "How does it feel? Drag the pointer on the mood dial."
- how `panelHow`: "Tap anything the pictures add, then pick what it shows."
- event `tagHint`: the hot spot's hint.
- how `perfHow`: "Listen. Then tap the timeline where the sound follows the words."
- event `swap`: "Same words, different artist. How does it feel now?"
- event `strip`: "Look at your mood strip. The words never changed."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tap every hot spot with one tag | Each hot spot has its own tag; one tag for all fits at most a third of them (data, checked). |
| Follows, adds, changes | Mark all "adds" | Each moment has at least 4 "follows", 3 "adds" and 1 "changes" (checked). |
| Timeline marks | Tap everywhere | Marks count only within 1.5 seconds of a data cue; stray taps show "Nothing in the words says that here." |
| Mood dial | Any reading | It's the student's own; there is nothing to beat. The compare sentence asks why. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Words: `line` (whole), `welcome` (queued, first time), then `dialHow` after the last sentence.
2. Panels: `panelHow`; wrong tag: `tagHint`.
3. Performance: plays, then `perfHow`.
4. Swap: `swap`; strip complete: `strip`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.3.7, RL.4.7, RL.5.7 wording | thecorestandards.org, Reading Literature Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
| "The Three Billy Goats Gruff" was collected in Norway by Asbjørnsen and Moe and translated by G. W. Dasent (1859) | Project Gutenberg, Dasent, Popular Tales from the Norse | Britannica, Peter Christen Asbjørnsen | yes |
| "The Wolf and the Kid" is an Aesop fable in public-domain English tellings | Project Gutenberg, Jacobs, The Fables of Aesop (1894) | Library of Congress, The Aesop for Children (1919) | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b9, 2026-11-08): one tag fits at most 4 of 14 hot spots (29 percent); follows, adds and changes minimums; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 four panels and the tray fit; at 680x425 two panels show.
2. Words and Panels each end with the mood dial, and readings land on the strip. (RL.3.7)
3. Hot spot tags check against data with hints. (RL.3.7)
4. At grade 4 and up, tags thread to lines or are marked adds or changes. (RL.4.7)
5. Performance timeline marks count within 1.5 seconds of a cue. (RL.4.7)
6. Swap replaces panel 3 with the second style and adds a strip reading. (RL.5.7)
7. Grade 5 compare sentence from tiles or typed. (RL.5.7)
8. Sound off shows captions and a note.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: doors open without swinging; no network requests.

## Open questions
- None for Cory.
