# My Life Timeline

## One idea
Juno, a six-year-old, pulls keepsakes out of a shoebox one at a time (a baby photo, a tiny shoe, a birthday card, a story Grandpa tells), and the child names what kind of proof each one is (a photo, a thing, a paper, a told memory) and places it on Juno's timeline by the clues it holds, so the finished line shows a life in order and shows that one moment can be proven by different kinds of sources while some moments live only in a story; then the child makes a timeline of their own from stickers and drawings, with no baby photos or birth facts needed.

## Not like
- then-and-now-flip (K, spec): the same thing across eras. Here one person's life in order, each event with its proof.
- capsule-from-1965 (1, spec): four old objects read for maker, date and place. Here many keepsakes sorted by kind of source and placed in order.
- state-story-timeline (4, concept, same family): a state's history at grade 4. Here one child's life at grade 1.
- the-last-carousel-ride (1, concept): two accounts of one day. Here one life, many kinds of proof.

## Who and how
- Grade 1, Social Studies (History), module "Timelines and Me". Standards: D2.His.1.K-2 (create a chronological sequence of multiple events), D2.His.9.K-2 (identify different kinds of historical sources).
- Driver: teacher on the projector with the class calling where each keepsake goes, or one child alone; every keepsake, kind and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Two parts: Juno's box, then My timeline. tool.json `modes: ["Juno's box", "My timeline"]`, `minutes: "15-25"`, `grades_label: "Grade 1"`.
- Privacy: My timeline uses stickers and drawings only. Nothing is uploaded, no photo can be added, and nothing is saved after the page closes. The screen says so in one line under the title of My timeline: "Your timeline stays on this screen. It is never sent anywhere."
- Teacher note (in the tool's teacher panel): family stories differ (adoption, foster care, loss, moves). My timeline starts from now and goes back only as far as the child wants; no step asks for a baby photo, a birth date, a birth place or a family member.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.9.K-2 | Tap the kind of source for each keepsake: Photo, Thing, Paper or Told memory | the keepsake's kind badge (icon plus word) | 2 |
| D2.His.1.K-2 | Drag each keepsake to its age on Juno's line using the clue it holds | the keepsake settling on the line in order | 3 |
| D2.His.9.K-2 (one event, many sources) | Stack a second keepsake on a moment already proven, and find the moment with only a story | two badges on "First day of school"; one Told memory alone on "First steps" | 4 |
| D2.His.1.K-2 (own line) | Put at least four sticker moments in order from long ago to now on the child's own line | the child's line and its order check | 5, 6 |

## Screens and modes
Header (kit): title "My Life Timeline"; `Juno's box`, `My timeline`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** Juno sits on a rug with a shoebox on her lap. A long line runs under her with seven age marks: 0 (a baby), 1, 2, 3, 4, 5, 6 (now). The welcome is queued (`welcomeAfter: true`): "Hi, I'm Juno! I'm six. This box has things from my whole life, but they're all mixed up. Tap the box to pull something out." First hint: "Tap the box to pull something out." The first tap pulls the first keepsake and cuts the welcome.

**Juno's box (focus: the keepsake on the table, then the line).** At 1366x768 Juno and the box are at the left, the keepsake fills the center, four kind buttons sit under it, and the line runs across the bottom. At 680x425 Juno shrinks to a small portrait in the corner.
- Step 1, kind: four big buttons, each an icon plus a word: Photo (a camera), Thing (a toy block), Paper (a sheet with lines), Told memory (a speech bubble). A right tap gives the badge. A wrong tap: "Is it a picture someone took, or something you can hold?" for that keepsake.
- Step 2, place: the keepsake shrinks and the child drags it to an age mark. Each keepsake has a clue, read aloud by Juno or Grandpa. A right drop settles; a wrong one floats back with the clue again.
- Eight keepsakes in the box (pulled in this mixed order):
  1. Birthday card, "Happy 5th Birthday, Juno! Love, Mom" (Paper, age 5).
  2. Tiny knit hat Grandpa made "for the day you came home" (Thing, age 0).
  3. Grandpa's story: "You took your first steps holding the dog's tail! You were one." (Told memory, age 1). Shown as a speech bubble with Grandpa's face.
  4. Juno's drawing of a dog, with "JUNO 4" written in big letters (Paper, age 4).
  5. Photo of Juno in a backpack at a school door, a sign says "Kindergarten" (Photo, age 5).
  6. A tiny shoe; Juno: "This was my first shoe. My feet were still small. I was two." (Thing, age 2).
  7. A name tag from the kindergarten door: "Juno, Room 2" (Thing, age 5; it goes on the same moment as the photo).
  8. A swimming certificate, "Juno swam the whole pool! Summer, age 6" (Paper, age 6).
  And one more, Juno's baby photo (Photo, age 0), so both age 0 and age 5 hold more than one kind of proof.
- When a second keepsake lands on age 5, Juno says: "Two kinds of proof for my first day of school! A photo and a thing." When all are placed, Juno points at age 1: "My first steps only have Grandpa's story. Sometimes a told memory is the only proof we have."
- Age 3 stays empty. Juno: "I don't have anything from when I was three. That's OK. Not every year has a keepsake." Then the `My timeline` mode lights.

**My timeline (focus: the child's own line).** The privacy line shows at the top. The line has four spots, left to right, with pictures: "A long time ago", "Last year", "This year", "Today". No ages are asked.
- Twelve moment stickers with pictures and spoken names: learned to ride a bike, lost a tooth, learned to swim, first day of school, made a new friend, a birthday, learned to read a book, a trip, a new pet, moved to a new home, won a game, helped someone. Plus `Draw one` to draw a moment with a finger or mouse on a small canvas and say its name with picture tiles.
- The child drags at least four moments onto spots (more than one per spot is fine) and picks a kind of proof for each from the same four buttons, or "I just remember it" (a speech bubble with the child's own face icon).
- `Check my order` reads the line from left to right ("A long time ago, you learned to swim. Last year, a birthday...") and asks "Is that the right order?" with `Yes` and `Move something`. The child is the only one who knows their life, so the check is the child's own.
- `Print` prints the line with stickers, drawings and kinds.

## Content
- Juno's keepsakes: nine (eight in the list plus the baby photo), each with kind, age and clue line. Age 0 holds two (photo, thing); age 5 holds three (the birthday card, plus a photo and a thing for the first day of school); age 3 holds none.
- Twelve moment stickers; the drawing canvas keeps strokes only in memory.
- Kinds: Photo, Thing, Paper, Told memory (plus "I just remember it" on My timeline).

## Interactions in detail
- Every tap acts at once; a new line stops the old one; pulling the next keepsake during a line starts its line.
- The kind buttons show first; the keepsake can be dragged only after its kind is right, and the hint says "Drag it to Juno's line."
- `Check my order` shows when four or more moments are placed; the hint names how many more first.
- Keyboard: Tab to a keepsake or sticker, Enter to pick up, arrow keys along the line, Enter to drop.
- With Motion off keepsakes appear on the table and the line without flying.

## Look
- Accent `--brand` #a0452e warm terracotta (header, the line, kind badges); gold #f4c542 (the lit age mark, the settled ring, today's spot); paper #fdf3ee; ink #2c110a; muted #68534c.
- Contrast (WCAG 2.1, computed): white on brand 6.20:1; brand on paper 5.68:1; ink on paper 16.14:1; muted on paper 6.56:1; ink on gold 10.84:1.
- Never color alone: kinds carry icons and words; age marks carry pictures and numbers.
- Different from this batch (kite sky blue, council green, changemaker purple, backpack mustard).

## Art
- People art goes to Gemini with `people: true`: Juno (6 poses: holding the box, pulling, pointing, laughing, thinking, waving; 1:1; cutout yes); Grandpa (3 poses for the told memory bubble; 1:1); Juno at 0, 1, 2, 4 and 5 in her keepsake photos and the drawing's subject (the baby photo and the kindergarten photo, 4:3, 2 images).
- Local FLUX (`scripts/localart.py`): the rug scene (16:9); the shoebox closed and open (2); keepsakes: knit hat, tiny shoe, name tag, card, certificate (5, 1:1, cutout yes); twelve moment stickers in one sticker style (12, 1:1).
- Drawn in code: the line, age marks and spots, kind buttons, the child's drawing canvas, Juno's dog drawing (a child's crayon style drawn as strokes), every written word on keepsakes.
About 32 images.

## Voice
Two bank voices, both unique in this batch: `gentle-storyteller` as Juno's lines and the narrator; `wise-mentor` as Grandpa's story. `Curio.voice` with `scope: () => state.mode + ':' + state.item + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Hi, I'm Juno! I'm six. This box has things from my whole life, but they're all mixed up. Tap the box to pull something out."
- how `kind` (first keepsake): "What kind of proof is this? Tap Photo, Thing, Paper, or Told memory."
- event `kind-no`: that keepsake's question line.
- event, whole, `clue`: each keepsake's clue (Juno or Grandpa).
- how `place` (once): "Drag it to Juno's line."
- event, whole, `two-kinds`: "Two kinds of proof for my first day of school! A photo and a thing."
- event, whole, `only-story`: "My first steps only have Grandpa's story. Sometimes a told memory is the only proof we have."
- event, whole, `no-three`: "I don't have anything from when I was three. That's OK. Not every year has a keepsake. Tap My timeline."
- how `mine`: "Drag four moments onto your line, from a long time ago to today."
- how `mine-kind` (once): "Tap what kind of proof you have, or I just remember it."
- event, whole, `read-back`: the line read left to right, then "Is that the right order?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
timeline-maker has no family doc or engine yet; this is its first tool, and state-story-timeline (grade 4) is its sibling. Tool-only code for now: a line of marks, drag-to-mark with a right answer per item (Juno's box) or free placing (My timeline), stacked items on one mark, and read-back in order. Write these as one plain object so the grade 4 sibling can lift them into a family engine.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Kind | Tap all four buttons | Wrong taps play a question about the keepsake; the badge comes only from the right tap, and the hint names what to look for. |
| Place | Try every age | A wrong drop floats back and replays the clue; the child must hear the clue to place it. |
| Place | Read the number on the item | Only three keepsakes show a number; the hat, shoe, story, name tag and photos need the clue or the stack. |
| My timeline | Put stickers anywhere | Allowed; the read-back makes the child hear the order and choose to keep or move. Only the child knows their life. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap box: keepsake 1, `kind`.
2. Right kind: badge chime, then `clue` (whole), then `place` (once). Wrong: `kind-no`.
3. Drop: settle or the clue again (whole). Second item on age 5: `two-kinds` (whole).
4. All placed: `only-story` (whole), waits; then `no-three` (whole).
5. My timeline: `mine`; first sticker: `mine-kind`; `Check my order`: `read-back` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1.K-2 and D2.His.9.K-2 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Historical sources include photographs, objects (artifacts), written papers and spoken memories (oral history) | Library of Congress, "Using Primary Sources" (teachers) | National Archives, "Document Analysis Worksheets" (photo, artifact, written document, sound recording) | yes |
| Oral history records people's spoken memories as a source | Oral History Association, "Oral History: Defined" | Wikipedia, Oral history (checked 2026-11-09) | yes |
| A timeline shows events in the order they happened | National Geographic Education, "Timeline" | Wikipedia, Timeline (checked 2026-11-09) | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: family situations vary (adoption, foster care, loss, moves). Juno's life is gentle and ordinary; My timeline asks for no baby photo, birth facts or family members, and starts from now. "Moved to a new home" is a sticker, not a prompt. A fresh-agent sensitivity read is needed before build.

Checks run (Python, scratchpad r3, 2026-11-09): nine keepsakes cover ages 0, 1, 2, 4, 5, 6 with two at 0, three at 5 and none at 3; each keepsake's clue names or implies exactly one age; kinds count 3 Thing, 3 Paper, 2 Photo, 1 Told memory, so no kind can be guessed by count; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 Juno, keepsake, kind buttons and line fit; at 680x425 Juno becomes a corner portrait.
2. Each of nine keepsakes takes only its right kind. (D2.His.9.K-2)
3. Each keepsake settles only on its age; the line ends in order. (D2.His.1.K-2)
4. Ages 0 and 5 show at least two kinds; age 1 shows only a told memory; age 3 stays empty with Juno's line. (D2.His.9.K-2)
5. My timeline takes at least four stickers or drawings and reads them back in order. (D2.His.1.K-2)
6. No step asks for a photo upload, an age, a birth date or a family member; the privacy line shows.
7. `Check my order` and the drag step are never named before they show.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no flying keepsakes; no network requests, and nothing stored after the page closes.

## Open questions
- My timeline sticker "moved to a new home" could be hard for some children (default used: kept as one choice among twelve, never asked about). Remove it?
