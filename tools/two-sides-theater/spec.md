# Two Sides Theater

## One idea
In a little theater the class is the director: first they put the scene cards of Goldilocks and the Three Bears in order, and the show plays exactly what they chose, so an opening that skips "who and where" leaves the audience asking "Whose house is this?" and a middle scene put last leaves the curtain stuck halfway; then comes the two-sides scene, where the same broken chair is told by Baby Bear and by Goldilocks, and the class sorts each line to the character whose side it shows, picks a feeling for each voice, and records both, so they hear one event sound completely different from each side.

## Not like
- who-said-that (1, spec): which speaker said each line, and a narrator who is a character. Here how each character sees the same event, and reading each in their own voice.
- story-stage (k, spec): acting a folktale's events with puppets. Here ordering scenes for a beginning and an ending, and voicing two points of view.
- moral-of-the-story (2, spec): lessons across fables. Here structure and point of view in one tale.
- echo-reader (1, spec): echoing a model reading and comparing waves. Here reading dialogue in two characters' voices.
- story-building-blocks (3, concept): chapters, scenes and stanzas. Here grade 2 beginning and ending.

## Who and how
- Grade 2, ELA, module "Story Structure and Point of View" (Reading Literature). Standards: RL.2.5, RL.2.6.
- Driver: a pair at one device with a microphone, or the teacher on a projector with two volunteers (tool.json `driver: "either"`). Every card and line is read on tap (BASELINE rule 4).
- Two shows: `Goldilocks and the Three Bears` and `Jack and the Beanstalk` (both English folk tales, retold for Curio Class). Each: `Order the Show`, `Two Sides`, `Curtain Call`. tool.json `modes: []`, `minutes: "15-20"`, `grades_label: "Grade 2"`.
- Privacy (BASELINE rule 7), shown before the first recording: "Your recordings stay on this device and are gone when you close the page. Nothing is sent anywhere."

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.2.5 | Order six scene cards; pick which card opens the show and which ends it, and say what each does (opening: who and where; ending: how the problem is wrapped up) | the cue sheet; the show playing their order | 2, 3 |
| RL.2.6 | Sort lines about the same event to the character whose side each shows | two speech stands, one per character | 4 |
| RL.2.6 | Pick a feeling for each character, hear the model, and record each side in a different voice | feeling chips; two recordings | 5, 6 |

## Screens and modes
Header (kit): title "Two Sides Theater"; `Shows`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A small red-curtained theater with Director Dot the squirrel in a beret and a megaphone. First hint: "Tap a show poster to start." The first tap opens the show with its line; the welcome is queued after it (`welcomeAfter: true`).

**Order the Show.** Focus: the cue sheet (six numbered slots, a star on slot 1 marked Opening and a bow on slot 6 marked Ending, 1300 x 180) and the scene cards (picture plus one sentence, 200 x 160), plus one extra card from the middle of the story labeled "Bonus scene?" that fits nowhere (decoy). Drag cards to slots (or tap, then a slot). `Play the show`: the stage plays the scenes in the class's order with puppets and narration. Problems the show reveals:
- Opening without who and where: the audience (drawn heads) whispers "Whose house is this? Who are they?"
- A scene before what causes it (porridge eaten before Goldilocks arrives): the narrator stops, "Wait, who ate it? She isn't here yet!"
- An ending that doesn't wrap up: the curtain sticks halfway and the audience says "Is that it?"
After a clean run, two questions: "What did the opening tell us?" (picks: who and where | the ending | a joke) and "How did the ending wrap it up?" (picks: Goldilocks ran home and the bears had their house back | the porridge was hot | the bears went for a walk).

**Two Sides.** The broken-chair scene (or the giant's kitchen). Two speech stands (Baby Bear and Goldilocks), and eight line cards about the same event. Drag each line to the character whose side it shows. Right: the line clips onto the stand. Wrong: the character shakes their head and Dot reads the line in that character's voice ("Goldilocks saying 'Someone broke MY chair!'? Is that her side?").
Then for each character: feeling chips (sad, cross, scared, sorry, surprised; each a face plus word). Pick one; `Hear it` plays the model actor reading that character's four lines in that feeling. `Record`: a 3, 2, 1 count, then the child reads the four lines (prompter shows them, one lit at a time; each line ends on tap or after 6 s).

**Curtain Call.** Both recordings play back to back, Baby Bear's side then Goldilocks's, with the puppets on stage. Then Dot asks "Which line shows that Goldilocks was sorry?" and "Which line shows that Baby Bear was upset?" (tap a line card on either stand).

At 1366x768 the cue sheet and cards, or the two stands, fit above the fold. At 680x425 slots are 110 x 90 and stands stack.

## Content
Retold for Curio Class from public-domain tellings.

**Goldilocks.** Scenes in order: 1 (Opening) Three bears lived in a little house in the woods. Their porridge was too hot, so they went for a walk. | 2 A girl named Goldilocks found the house and went inside. She tasted the porridge and ate Baby Bear's all up. | 3 She sat in the chairs, and Baby Bear's little chair broke. | 4 She lay down in Baby Bear's bed and fell asleep. | 5 The bears came home. "Someone's been sitting in my chair, and it's broken!" cried Baby Bear. | 6 (Ending) Goldilocks woke up, jumped out the window and ran all the way home, and the bears had their house back. Decoy: "The bears wondered if the porridge was cool yet." (a middle beat with no slot).
Two Sides lines (Baby Bear | Goldilocks):
- Baby Bear: "Someone sat in MY chair!" | "It was my favorite chair, and now it's in pieces." | "Who comes into a house without asking?" | "Now where will I sit?"
- Goldilocks: "I was so tired from walking." | "The little chair looked just my size." | "I didn't mean to break it!" | "I should have knocked first. I'm sorry."
Feelings that fit: Baby Bear sad or cross; Goldilocks scared or sorry. (Any feeling can be recorded; Dot asks "Does that feeling fit Baby Bear's side?" for the others, once.)

**Jack and the Beanstalk.** Scenes: 1 (Opening) Jack and his mother were very poor. They sold their cow for a handful of magic beans. | 2 In the night, the beans grew into a beanstalk up to the clouds. | 3 Jack climbed it and found a giant's castle and crept into the kitchen. | 4 The giant came home. "Fee-fi-fo-fum!" Jack hid, then took the giant's hen that laid golden eggs. | 5 The giant chased Jack down the beanstalk. | 6 (Ending) Jack chopped the beanstalk down, the giant stayed up in the sky, and Jack and his mother were never hungry again. Decoy: "Jack looked at the clouds."
Two Sides, the kitchen (Jack | the Giant):
- Jack: "My mother and I are so hungry." | "This kitchen is as big as a field!" | "I have to hide, fast!" | "That hen could feed us for years."
- Giant: "I smell someone in MY kitchen!" | "I worked hard for that hen." | "Who sneaks into a castle?" | "Come back with my hen!"
Feelings that fit: Jack scared or surprised; the Giant cross or surprised.
Changes for the sensitivity review: in the old telling the giant falls and dies; here the beanstalk comes down and the giant stays in the sky. Jack taking the hen is kept as told, because hearing the giant's side of it is the point of the scene.

## Interactions in detail
- Every tap acts at once; a new line or playback stops the old one. Recording stops any playback.
- `Play the show` can be pressed any time; it plays the filled slots in order and stops at the first problem.
- Recording: the browser's media recorder, kept in memory only; one take per character, replaced on retake; `Start over` and closing the page drop them. No speech recognition.
- If the microphone is blocked or missing: "No microphone? You can read the lines aloud to your partner. I'll play the actors." The Curtain Call plays the model actors in the chosen feelings.
- Stars: Order the Show on the first clean run; Two Sides with all eight lines on the first try; Curtain Call answers.

## Look
- Accent `--brand` #9b1c31 velvet red (header, curtains, cue sheet); gold #f4c542 (footlights, stars, the bow); paper #fdf7f3; ink #2a1216; muted #6a5052. Scene: a small theater with footlights.
- Contrast (WCAG 2.1, computed): white on brand 8.06:1; brand on paper 7.59:1; ink on paper 16.53:1; muted on paper 6.86:1; ink on gold 10.79:1.
- Never color alone: Opening and Ending slots have a star and a bow plus words; the two speech stands show each character's picture; feeling chips are faces with words.
- Different from this batch (rain blue, wine table, playground orange, lab purple).

## Art
Local FLUX (`scripts/localart.py`) for the theater, Dot, the bears, the giant and objects; Goldilocks and Jack are people, so their puppets and scene pictures go to Gemini.
- theater (1): "A small cozy theater stage with red curtains and footlights, soft gouache, no text"; 16:9; cutout no.
- Director Dot (3, direct, clap, puzzled): "A squirrel in a beret holding a small megaphone <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- puppets (8): the three bears (local), the giant (local, friendly-looking, big beard), Goldilocks (Gemini), Jack and his mother (Gemini), the hen (local): "a <character> as a flat stick puppet, storybook gouache, plain white background"; 3:4; cutout yes.
- scene cards (14): "<three bears leaving a cottage in the woods / a girl tasting porridge / ...>, storybook gouache"; 4:3; cutout no.
- audience heads (1 strip): "a row of cartoon audience heads from behind, simple"; 8:1; cutout yes.
About 27 images. Drawn in code: cue sheet, slots, stands, chips, the stuck curtain, controls.

## Voice
Director Dot: bank voice `lively-host`; model actors: Baby Bear `playful-friend`, Goldilocks `big-sister`, Jack `casual-peer`, the Giant `gravel-ranger`; each actor recorded in every fitting feeling and in a neutral read. None is used elsewhere in this batch. `Curio.voice` with `scope: () => state.show + ':' + state.step`, `welcomeAfter: true`.
- event `poster`: "{Goldilocks and the Three Bears}! Places, everyone."
- how `welcome`: "Welcome to my theater! You're the director. Put the scenes in order, then tap Play the show."
- event, whole, `scene`: the scene sentence.
- event `whose`: "Whose house is this? Who are they?"
- event `notYet`: "Wait, {who ate it? She isn't here yet!}"
- event `isThatIt`: "Is that it? The curtain is stuck."
- event `bravo`: "Bravo! What a show."
- event, whole, `ask`: the opening or ending question. event `askYes` / `askNo`: "That's what it did!" / "Think about what the {opening} told the audience."
- how `sidesHow`: "Same chair, two sides. Put each line on the stand of the one who would say it."
- event `wrongSide`: "{Goldilocks} saying {'Someone sat in MY chair'}? Is that her side?"
- how `feelHow`: "Pick a feeling for {Baby Bear}. Then tap Hear it, and tap Record."
- event `fit`: "Does that feeling fit {Baby Bear}'s side?"
- how `privacy`: "Your recordings stay right here and go away when you close the page."
- event `curtain`: "Curtain call! Here are both sides."
- event `noMic`: "No microphone? You can read the lines aloud to your partner. I'll play the actors."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Order the Show | Random order | 7 cards for 6 slots: 5040 fills (computed), one right; the show stops at the first problem. |
| Opening and ending questions | Tap the first pick | Right picks are first in one of four questions (data positions 2, 1, 3, 2; computed). |
| Two Sides | Sort by "I" or "my" | Both sides use I and my (Baby Bear 3 of 4 lines, Goldilocks 4 of 4; computed); it has to be what the line shows about the event. |
| Two Sides | Random | 8 lines, two stands: 70 ways to split them four and four, one right (computed). |
| Record | Stay silent | Nothing is scored; the curtain call simply plays a silent side, and Dot says "I didn't hear {Baby Bear}! Want to record again?" |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a poster: `poster`, `welcome` (queued, first time).
2. Tap a card: `scene` (whole). Play the show: `scene` per slot, then `whose`, `notYet`, `isThatIt` or `bravo`; then `ask` (whole), `askYes` or `askNo`.
3. Two Sides: `sidesHow`, `wrongSide` per miss; `feelHow`, `fit` once if needed; `privacy` before the first recording.
4. Curtain Call: `curtain`, both recordings, then `ask` (whole).
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.2.5 and RL.2.6 wording (beginning introduces the story and ending concludes the action; differences in characters' points of view, including speaking in a different voice for each character when reading dialogue aloud) | thecorestandards.org, RL Grade 2 | CCSS ELA 2010 PDF | yes |
| The Three Bears is an English tale first printed by Robert Southey (1837); the intruder became a girl called Goldilocks in later tellings | Ashliman, Folklinks, "The Three Bears" (University of Pittsburgh) | Encyclopaedia Britannica, "Goldilocks and the Three Bears" | yes |
| Jack and the Beanstalk: magic beans for a cow, a giant's castle, "Fee-fi-fo-fum", a hen that lays golden eggs, the beanstalk chopped down | Joseph Jacobs, English Fairy Tales (1890), Project Gutenberg | Ashliman, Folklinks, Jack and the Beanstalk (Type 328) | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b7, 2026-11-08): 7P6 = 5040; C(8,4) = 70; I/my/me counts per side; question right positions; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the cue sheet and cards fit with no scroll; at 680x425 the same, smaller.
2. The show plays the class's order and stops at the first problem with its line; the right order runs clean. (RL.2.5)
3. The opening and ending questions take only their right picks. (RL.2.5)
4. Two Sides: each line clips only to its character. (RL.2.6)
5. Hear it plays the chosen character's lines in the chosen feeling. (RL.2.6)
6. Record keeps one take per character in memory and plays both at the curtain call; reload leaves none. (RL.2.6)
7. Privacy: the card shows before the first recording; no network requests at any time.
8. No microphone: the tool runs with the model actors only.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: puppets appear in place, the curtain cuts instead of sliding; nothing saved.

## Open questions
- None for Cory.
