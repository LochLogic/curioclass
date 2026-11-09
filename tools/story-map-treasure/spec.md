# Story Map Treasure

## One idea
After hearing a story, the class turns it into a treasure map: each story picture is a stop on the trail (where it starts, the problem, what happens, how it is fixed), and at every stop they answer a detail question and set the character's face, so the faces become a feelings line along the trail that shows how the character changed; the chest at the X is locked with two keys, the lesson and the detail that proves it, and a true detail that does not prove the lesson will not turn the lock.

## Not like
- story-stage (k, spec): acting a folktale's events with puppets and a playbill. Here mapping a story's parts and feelings and naming its lesson.
- moral-of-the-story (2, concept): fables from many cultures, events to lesson with a proof card. Here grade 1 retelling on a map with feelings at each stop; this tool does not use the fables that one plans (Lion and the Mouse, Ant and Grasshopper, Anansi, Panchatantra, Jataka, Frog in the Well).
- who-said-that (1, spec): who is telling. Here what happens and why.
- first-next-last (1, spec): writing your own story with time words. Here retelling someone else's.
- plot-rollercoaster (6, concept, same family): tension heights on a ride. This tool sets the shared story-map engine.

## Who and how
- Grade 1, ELA, module "Story Elements and Lessons" (Reading Literature). Standards: RL.1.1, RL.1.2, RL.1.3.
- Driver: teacher on a projector or a pair at one device (tool.json `driver: "either"`). The story is read aloud page by page; every question has picture picks (BASELINE rule 4).
- Two stories: `The Elves and the Shoemaker` (a Grimm tale, retold for Curio Class) and `Rosa's Kite` (written for Curio Class). Each: `Hear it`, `Map it`, `Open the chest`, `Walk the trail` (retell). tool.json `modes: []`, `minutes: "15-20"`, `grades_label: "Grade 1"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.1.3 | Place each story picture on its trail stop: start (who and where), problem, two events, solution | the map's stops with signs (a house, a storm cloud, footprints, a bridge) | 2 |
| RL.1.1 | At each stop, answer a who, what, where or why question by tapping a picture | a question card at the stop | 3 |
| RL.1.3 | Set the main character's face at each stop; the faces draw the feelings line | five faces on a line under the trail | 4 |
| RL.1.2 | Open the chest: pick the lesson, then the detail that proves it | two keyholes | 5 |
| RL.1.2 | Walk the trail: the class retells stop by stop while the ship sails, with the stop picture as a prompt | the ship moving stop to stop | 6 |

## Screens and modes
Header (kit): title "Story Map Treasure"; `Stories`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A rolled-up map on a ship's deck with Captain Pip the parrot. First hint: "Tap a story to unroll its map." The first tap unrolls the map with its line; the welcome is queued after it (`welcomeAfter: true`).

**Hear it.** The story as a picture book: six pages (picture 720 x 405 and two short sentences), read aloud with each word lit; `Back`, `Next`, `Read again`. The last page has `Map it`.

**Map it.** Focus: the island map (1000 x 520) with a dotted trail from the ship to the X and five stops along it, each with a sign: Start (a little house), Problem (a storm cloud), Event 1 and Event 2 (footprints 1 and 2), Solution (a bridge). Below: five story pictures, shuffled (180 x 110). Drag a picture to a stop (or tap, then a stop). Right: the picture pins to the stop and the stop opens its question card. Wrong: the picture slides back and Pip says what that stop is for ("The problem is what goes wrong").

**The stop card.** A key-detail question with three picture picks, then "How does {the shoemaker} feel here?" with four faces (happy, sad, worried, surprised; each face drawn plus its word). The face is placed on the feelings line under the trail at that stop. Faces are checked against the data; a wrong face asks "Look at the picture. How does his face look?" and shows the stop picture larger.

**Open the chest.** When all five stops are done, the X glows. The chest has two keyholes: Lesson (three lesson cards) and Proof (three detail cards, all true to the story, only one showing the lesson). Right lesson: the first key turns. Right proof: the second key turns and the chest opens on a gold star and the lesson written on a scroll. A true detail that doesn't prove it: "That did happen. But does it show {the lesson}?"

**Walk the trail.** The ship sails stop to stop; at each it stops and shows the picture and face; Pip asks "What happened here?" and the class tells it aloud; `Next stop` goes on. At the end Pip retells the whole story in four sentences with the lesson. Nothing is recorded.

At 1366x768 the map and the picture row fit above the fold. At 680x425 the map is 640 x 340 and pictures 120 x 74.

## Content
**The Elves and the Shoemaker** (from the Brothers Grimm, 1812, public domain; retold for Curio Class):
- Pages: 1. A kind shoemaker and his wife were very poor. 2. He had leather for only one pair of shoes. He cut it and went to bed. 3. In the morning, the shoes were done! They were perfect. 4. This happened night after night, and the shoemaker sold the shoes. 5. One night, he and his wife hid and watched. Two tiny elves were sewing, and they had no clothes! 6. The wife sewed tiny clothes, and the shoemaker made tiny shoes. The elves put them on and danced away, happy.
- Stops: Start: the shoemaker and wife in their little shop (face: worried). Problem: only enough leather for one pair (worried). Event 1: shoes done by morning (surprised). Event 2: hiding and seeing the elves with no clothes (surprised). Solution: making the elves clothes and shoes (happy).
- Questions (right first): Where does the story start? a shoe shop | a farm | a ship. What was the problem? no money for leather | a lost shoe | a broken door. Who made the shoes at night? two elves | the wife | a cat. Why did the shoemaker hide? to see who made the shoes | to play a game | to find his hat. What did the wife make? tiny clothes | a cake | a hat for herself.
- Lesson: "When someone helps you, help them back." | "Shoes are hard to make." | "Go to bed early, and your work will get done by itself."
- Proof: "The shoemaker and his wife made tiny clothes for the elves." (right) | "He had leather for only one pair of shoes." | "He sold the shoes in the morning."

**Rosa's Kite** (written for Curio Class; Rosa and her brother Teo are young foxes):
- Pages: 1. Rosa got a new red kite. 2. "I can fly it by myself!" she told her brother Teo. 3. A big wind pulled the kite into a tall tree. 4. Rosa pulled and pulled, but it was stuck. 5. Teo got Grandpa, and Grandpa reached up with a long rake and lifted the kite down. 6. Rosa held the string and Teo held the tail. Together, they flew it high.
- Stops: Start: Rosa with her new kite in the park (happy). Problem: the kite stuck in the tree (sad). Event 1: Rosa pulling and pulling (worried). Event 2: Teo getting Grandpa with the rake (surprised). Solution: flying it together (happy).
- Questions: Where are they? a park | a school | a store. What went wrong? the kite got stuck in a tree | the kite ripped | Rosa fell. What did Rosa try first? pulling the string | climbing the tree | crying for help. Who did Teo get? Grandpa | a firefighter | a bird. How did they fly it at the end? together | Rosa alone | Teo alone.
- Lesson: "It is good to work together and take help." | "Kites are red." | "If a kite gets stuck in a tree, just wait for the wind."
- Proof: "Rosa and Teo flew the kite together, and it went high." (right) | "A big wind pulled the kite into a tree." | "Rosa got a new red kite."
Picks above list the right one first; on screen the right pick sits at these positions (Elves questions 1 to 5, then Kite): 2, 1, 3, 2, 1 and 3, 2, 1, 3, 2. Lesson and proof right positions: Elves 2 and 3, Kite 3 and 1.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pictures can be placed in any order; the question card opens on placement; stops can be visited again.
- The face pick is checked against the data's face; two faces are close (worried, sad), so the wrong-face prompt points at the picture.
- The Lesson key must turn before the Proof keyhole is active; the Proof cards stay shown so the class can talk about them.
- Walk the trail can be started any time after the chest opens; `Next stop` moves on; nothing is recorded.
- One star per story for the chest; a second star when every stop's question and face were right the first time.

## Look
- Accent `--brand` #8c2f1b brick red (header, the trail, the X); gold #f4c542 (keys, stars, the chest); paper #fbf5e6 parchment; ink #2b1a10; muted #6a5541. Scene: a hand-drawn island map on parchment.
- Contrast (WCAG 2.1, computed): white on brand 8.28:1; brand on paper 7.61:1; ink on paper 15.35:1; muted on paper 6.46:1; ink on gold 10.26:1.
- Never color alone: stops have sign icons and words (Start, Problem, 1, 2, Solution); faces are drawn and labeled; keyholes have their words.
- Different from this batch (dusk violet, workshop teal, coral sea, olive post office).

## Art
Local FLUX (`scripts/localart.py`) for the map, the foxes and objects; people art (the shoemaker, his wife) goes to Gemini per the art rule.
- island map (2, one per story, same island with different landmarks): "A hand-drawn treasure map of a small island on parchment with a dotted trail, a ship, and an X, soft ink and watercolor, no text"; 16:9; cutout no.
- Captain Pip (4, point, listen, cheer, hold key): "A green parrot in a little captain's hat <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Elves pages (6, Gemini for the shoemaker and wife; elves are small fantasy figures): "<a kind old shoemaker and his wife in a poor little shop / ...>, warm storybook gouache"; 16:9; cutout no.
- Rosa's Kite pages (6, local): "<a young fox girl with a new red kite in a park / ...>, soft gouache"; 16:9; cutout no.
- question picks (30): "<a shoe shop / a farm / a ship / ...>, simple soft gouache icon, plain white background"; 1:1; cutout yes.
About 48 images. Drawn in code: trail, stop signs, faces, feelings line, chest and keyholes, controls.

## Voice
Bank voice `knowing-guide` as Captain Pip (unique in this batch); story pages read by Pip. `Curio.voice` with `scope: () => state.story + ':' + state.step`, `welcomeAfter: true`.
- event `unroll`: "{The Elves and the Shoemaker}! Let's map it."
- how `welcome`: "Ahoy! Every story is a trail. Listen to the story, then put each picture on its stop. The treasure is the lesson."
- event, whole, `page`: the page's two sentences.
- how `mapHow`: "Drag each picture to its stop. Start, the problem, what happened, and how it was fixed."
- event `pinned`: "Pinned!" then event, whole, `question`: the stop's question.
- event `wrongStop`: "The {problem} is {what goes wrong}. Try another stop."
- event `qYes` / `qNo`: "Yes!" / "Listen again: {He had leather for only one pair of shoes.}"
- event, whole, `feel`: "How does {the shoemaker} feel here?"
- event `faceNo`: "Look at the picture. How does {his} face look?"
- event `chest`: "The X is glowing! What did the story teach us?"
- event `keyOne`: "One key turns! Now find the part of the story that proves it."
- event `proofNo`: "That did happen. But does it show {when someone helps you, help them back}?"
- event `open`: "Treasure! {When someone helps you, help them back.}"
- event, whole, `walk`: "What happened here? Tell it." and at the end the four-sentence retell.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
`kit/story-map.js` (the story-map family). No family doc exists and the only sibling, plot-rollercoaster (6), is a concept, so this spec describes the engine for both. Pure parts in one marked block, exposed as `__tool.sm`.
- **Story**: `{id, pages:[{text, pic, words}], parts:[{id, role:'start'|'problem'|'event'|'solution'|'climax'|'resolution', pic, face, tension?}], lesson:{picks, right}, proof:{picks, right}}`.
- **Trail**: `sm.place(partId, stopId)` checks a part against a stop's role; `sm.done(trail)`.
- **Stop questions**: `{ask, picks, right}` per part; `sm.answer(q, pick)`.
- **Feelings line**: `sm.faces(trail)` gives the face per stop in order for drawing; plot-rollercoaster uses `tension` the same way for track height.
- **Lock**: `sm.lock(lessonPick, proofPick)` turns key one only on the lesson, key two only on the proof.
- **Walk**: steps through placed parts in order with a prompt and the stored retell.
- **Pull-out** (plot-rollercoaster): remove a part and report what breaks; not used here.
This tool uses Story, Trail, Stop questions, Feelings line, Lock, Walk.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Trail | Try each picture at each stop | It places it, but the second star needs first tries; 5 pictures in order by chance is 1 in 120 (computed). |
| Stop questions | Always the first pick | Right positions vary across the ten questions (data order sets them); no single position is right more than 4 times. |
| Faces | Always happy | Happy is right at 3 of 10 stops. |
| Chest proof | Any true detail | All three proof cards are true to the story; only one shows the lesson. |
| Chest lesson | Pick the longest | The right lesson is not the longest pick in either story (computed). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a story: `unroll`, `welcome` (queued, first time), then `page` (whole) for page one.
2. Map it: `mapHow` (first time); each drop: `pinned` then `question` (whole), or `wrongStop`; `qYes` or `qNo`; `feel` (whole); `faceNo` if wrong.
3. Chest: `chest`, `keyOne`, `proofNo` or `open`.
4. Walk: `walk` (whole) at each stop, then the retell.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.1.1, RL.1.2, RL.1.3 wording (key details; retell with central message or lesson; characters, settings and major events using key details) | thecorestandards.org, RL Grade 1 | CCSS ELA 2010 PDF | yes |
| The Elves and the Shoemaker is a Grimm tale (KHM 39, first published 1812): elves make shoes at night for a poor shoemaker, who with his wife makes them clothes, and the elves leave | Ashliman, Folklinks, "The Elves" (University of Pittsburgh) | Project Gutenberg, Grimm's Fairy Tales (Hunt translation), "The Elves" | yes |
| Story map: a graphic organizer for the parts of a story (characters, setting, problem, events, solution) | Reading Rockets, "Story Maps" | ReadWriteThink (NCTE), "Story Map" interactive | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b6, 2026-11-08): 5 stops in order by chance 1/120; right-pick positions across the ten questions; happy faces 3 of 10; right lesson is not the longest pick in either story; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the map and the picture row show with no scroll; at 680x425 the same, smaller.
2. Each picture pins only on its stop; a wrong drop slides back with the stop's meaning. (RL.1.3)
3. Each stop's question takes only its right picture. (RL.1.1)
4. Each face sets on the feelings line; the line shows five faces in trail order. (RL.1.3)
5. The chest: key one turns only on the lesson, key two only on the proof; true non-proof details give `proofNo`. (RL.1.2)
6. Walk the trail stops at each stop in order and ends with the retell and the lesson. (RL.1.2)
7. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
8. Pre-reader: every page, question and pick is read on tap; picks are pictures.
9. Motion off: the map does not unroll, the ship jumps stop to stop; no network requests; nothing saved.

## Open questions
- None for Cory.
