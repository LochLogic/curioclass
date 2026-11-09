# Story Stage

## One idea
A real little puppet theater where the class puts on a folktale it has just heard: they choose the backdrop, bring the puppets on, and move them to make each big event happen (the littlest goat trip-traps onto the bridge), and the stage plays every choice, so if they bring on the big goat first the show goes their way and the narrator says how the story went, and they can switch back; after the show they make its playbill: who was in it, where it happened, and what happened, in order.

## Not like
- read-along-shelf (k-2, spec): reading books with fading help. Here acting a heard story out.
- meet-the-book-makers (k, spec): who made the words and pictures of a book. Here characters, setting and events, by doing them.
- question-cube (k-2, spec): question words with proof sentences. Here questions answered by pointing at the puppets on stage.
- owl-wants-more (k-2, spec): adding details to a story. Here retelling a folktale's events in order.
- bedtime-retell (k-2, concept, same family): telling a story back to a sleepy friend with frames. Here acting it with puppets on a stage, with the order heard and seen.

## Who and how
- Kindergarten, ELA, module "Story Time: Characters and Setting" (Reading Literature). Standards: RL.K.1, RL.K.2, RL.K.3.
- Driver: teacher on a projector, or a small group at one device (tool.json `driver: "either"`). Children take turns as puppeteers; the class says what happens next. Every word, card and puppet is spoken and every card is a picture, so pre-readers can play (BASELINE rule 4).
- Two folktales, each in three parts: Hear it, Put on the show, Make the playbill; plus `Free play` (any backdrop, any puppets, no story). tool.json `modes: ["Story", "Free play"]`, `minutes: "10-20"` per tale, `grades_label: "Kindergarten"`. Nothing is saved.
- It is a sandbox: nothing on stage is wrong; a choice that differs from the story is played and named, never blocked.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.K.1 | During the show, answer the narrator's question about the scene by pointing at (tapping) the puppet or place | the stage with the puppets on it | 3 |
| RL.K.2 | Put on the show: make each big event happen in order, with its key details (who, where, what they do and say) | the stage, the event strip with five frames filling as each happens | 2, 4 |
| RL.K.3 | Make the playbill: pick the characters, the setting and three big events in order | the playbill page with three sections and picture cards | 5 |

## Screens and modes
Header (kit): title "Story Stage"; mode tabs `Story` and `Free play`; `Tales` (book icon); `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A puppet theater with its wine curtain closed and two tale posters beside it (The Three Billy Goats Gruff; The Mitten). First hint: "Pick a story. Tap a poster to hear it." The first tap opens the tale with its line; the welcome is queued after it (`welcomeAfter: true`).

**Hear it.** Focus: the tale told as six picture panels (each 700 x 400, one at a time, with page arrows), read aloud; each panel lights its words as read. `Put on the show` comes after the last panel and stays on after.

**Put on the show.** Focus: the stage (1100 x 520) with the curtain open, a backdrop rack (three backdrop thumbnails) on the left, the puppet box (puppets as cutouts) below, and the event strip (five empty frames) above. The narrator asks for each step in order:
1. "Where does our story happen?" Tap a backdrop. Any backdrop goes up. The story's own is named ("Yes, a bridge over a stream!"); another is played and named ("Ooh, a beach show! In our story it was a bridge over a stream.") with `Our way` and `My way` buttons; My way keeps it and the show goes on there.
2. Each big event: "What happens first?" The puppeteer drags the puppet on and moves it to the place (zones glow faintly when a puppet is dragged: left bank, bridge, under the bridge, right bank). When the story's event is done, its frame in the strip fills with a picture and the narrator tells that bit, with the characters' lines (tap a puppet to hear its line again). A different event plays as done ("The big goat goes first! Trip, TRAP!") and the narrator says "In our story, the littlest goat went first." with `Our way` and `My way`.
3. A question after each event, answered by tapping on the stage: "Who is hiding under the bridge?" Right: that puppet does a little bow. Another: "Look again. Who did we hear say 'Who's that tripping over my bridge?'"
4. Curtain: when the five frames are full, the curtain closes and opens for a bow; `Play our show` plays the class's show back with the narrator, in the order they made it.

**Make the playbill.** Focus: a playbill page (900 x 560) with three sections: Starring (character cards), Where (setting cards), What happens (three numbered slots). Below it, picture cards: the tale's characters and two from the other tale, three settings, and seven event cards (five from this tale, two from the other). Tap to hear, drag to place, `Check`. Right sections get a gold star; a miss or extra is named. `Print playbill` prints it.

**Free play.** Every backdrop and puppet from both tales, plus a sun, a moon and rain to drop in; tap a puppet to hear its lines or make it do its move. No questions.

At 1366x768 the stage, the rack, the box and the strip fit above the fold. At 680x425 the stage is 640 x 300, the rack and box become pull-up drawers.

## Content
Retellings are written for Curio Class from the folktales.

**The Three Billy Goats Gruff** (Norway). Setting: a bridge over a stream between two hillsides; the green hill is on the far side. Characters: Little Billy Goat, Middle Billy Goat, Big Billy Goat, the Troll.
Hear it panels:
1. Three billy goats lived on a hillside. The grass was gone, and across a stream was a hill of sweet green grass.
2. Under the bridge lived a grumpy troll.
3. Little Billy Goat went first. Trip, trap, trip, trap! "Who's that tripping over my bridge?" roared the Troll. "Only me, Little Billy Goat. Wait for my bigger brother. He's much bigger!" So the Troll let him go.
4. Middle Billy Goat came next. Trip, trap! "Who's that tripping over my bridge?" "Wait for my big brother. He's the biggest of all!" So the Troll let him go too.
5. Then came Big Billy Goat. TRIP, TRAP! The Troll climbed up, and Big Billy Goat lowered his horns and butted him, splash, into the stream. The Troll swam away and never came back.
6. The three goats ate the sweet green grass until they were round and happy.
Show events (frames): Little goat crosses; Middle goat crosses; Big goat crosses; the Troll goes into the stream; the goats eat on the green hill.
Questions: "Who is hiding under the bridge?" (Troll) / "Who is crossing the bridge now?" (Middle goat) / "Who is the biggest goat?" (Big goat) / "Where did the Troll go?" (the stream) / "Where are the goats eating now?" (the green hill).
Backdrops: bridge over a stream (story); a sandy beach; a city street.

**The Mitten** (Ukraine). Setting: a snowy forest. Characters: Grandpa Badger, Mouse, Frog, Rabbit, Fox, Bear, Cricket.
Hear it panels:
1. Grandpa Badger was gathering sticks in the snowy forest, and he dropped his warm red mitten.
2. A cold little Mouse found it and crawled inside. "So cozy!"
3. Frog hopped up. "May I come in?" "Yes!" Then Rabbit squeezed in too.
4. Fox wanted in, and then Bear! "There's always room for one more," said Bear, and he squeezed in. The mitten stretched and stretched.
5. Then a tiny Cricket hopped up. "Me too?" The Cricket squeezed in, and POP! The mitten burst, and the animals tumbled out into the snow.
6. Grandpa Badger came back and found his mitten in pieces. "What a lot of visitors," he said, and he took it home to sew.
Show events: Badger drops the mitten; Mouse goes in; Frog, Rabbit, Fox and Bear squeeze in (one frame, in order); Cricket squeezes in and it pops; Badger finds the pieces.
Questions: "Who dropped the mitten?" (Badger) / "Who went in first?" (Mouse) / "Who is the biggest animal in the mitten?" (Bear) / "Who was the tiniest one?" (Cricket) / "Where is our story?" (the snowy forest).
Backdrops: a snowy forest (story); a summer pond; a farm.

**Playbill cards** (per tale): characters: every character in the tale (Goats: three goats and the Troll; Mitten: all seven) and two from the other tale; settings: the three backdrops; events: the five frames plus two from the other tale; the right three for What happens are the first, the middle and the last frame (goats: Little goat crosses, Big goat crosses, goats eat on the hill; Mitten: Mouse goes in, Bear squeezes in, it pops).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Puppets: drag on stage, drag to move, drag back to the box. Each puppet has three poses (stand, move, talk) and its move (goats trip-trap across, the Troll pops up, animals squeeze into the mitten). Two puppets can share a zone.
- The show listens for the next story event: a puppet reaching its zone in the right state. Any other move plays and, if it is a story event out of order or a new event, the narrator says how the story went with `Our way` and `My way`. My way records the class's order; the strip shows the class's frames in their order with a little pencil on frames done their way.
- Questions: tap a puppet or a zone; one tap answers; questions never block the next event.
- Playbill: Starring takes any number of cards and is checked as an exact set; Where takes one; What happens takes three in order.
- `Tales` returns to the posters; a tale keeps its show until `Start over`.

## Look
- Accent `--brand` #7d1d3f curtain wine (header, curtain, playbill frame); gold #f5c64a (stage lights, stars); paper #fdf6f4; ink #2a1218; muted #6d5157. Scene: a small wooden puppet theater with footlights.
- Contrast (WCAG 2.1, computed): white on brand 9.91:1; brand on paper 9.28:1; ink on paper 16.41:1; muted on paper 6.63:1; ink on gold 10.90:1.
- Never color alone: zones glow with an outline and a small picture; playbill stars come with a check mark; pencil marks show my-way frames.
- Different from this batch (indigo, moss, engine black, wind cyan) and the K ELA neighbors.

## Art
Local FLUX (`scripts/localart.py`); no people (Grandpa Badger is a badger).
- theater (1): "A small wooden puppet theater with a wine red curtain and footlights, soft gouache, no text"; 16:9; cutout no.
- tale panels (12): "<each Hear it panel's scene>, soft gouache, gentle storybook style, simple background"; 7:4; cutout no. The Troll is grumpy and lumpy, not scary.
- backdrops (6): "<a wooden bridge over a stream between two hills, one bare and one green / a sandy beach / a city street / a snowy forest / a summer pond / a farm>, soft gouache, empty of characters, no text"; 21:10; cutout no.
- puppets (11 characters x 3 poses = 33): "A <character> puppet, <standing / moving / talking>, soft gouache, plain white background"; 3:4; cutout yes. Characters: three billy goats in three sizes, the Troll, Grandpa Badger, Mouse, Frog, Rabbit, Fox, Bear, Cricket.
- red mitten (whole, stretched, burst: 3) and free play props (sun, moon, rain: 3): plain white background; cutout yes.
- event frames reuse panel pictures cropped.
About 58 images. Drawn in code: zones, the event strip, the playbill, stars, every control.

## Voice
Bank voice `warm-teacher` (style "like a kind kindergarten teacher talking to the whole class") as the narrator; characters' lines are read by the same voice with each character's line marked. Not used by the K ELA neighbors or the rest of this batch. `Curio.voice` with `scope: () => state.tale + ':' + state.step`, `welcomeAfter: true`.
- event `poster`: "{The Three Billy Goats Gruff}!"
- how `welcome`: "Welcome to Story Stage! First we hear a story. Then we put on the show."
- event, whole, `panel`: each panel's words.
- how `showHow`: "Let's put on our show. You're the puppeteers!"
- event, whole, `whereAsk`: "Where does our story happen?" event `whereYes`: "Yes, {a bridge over a stream}!" event `whereOther`: "Ooh, {a beach} show! In our story it was {a bridge over a stream}. Our way, or your way?"
- event, whole, `nextAsk`: "What happens {first}?" event, whole, `event`: the narrator's telling of that event, with lines. event `otherWay`: "In our story, {the littlest goat went first}. Our way, or your way?"
- event `line`: a puppet's line on tap.
- event, whole, `qAsk`: the scene question. event `qYes`: "Yes! {The Troll}!" event `qNo`: "Look again. {Who did we hear say 'Who's that tripping over my bridge?'}"
- event `bow`: "Take a bow!"
- how `playbillHow`: "Let's make the playbill. Who was in it? Where was it? What happened?"
- event `billYes` / `billMiss` / `billExtra`: "That part is just right!" / "Someone is missing from our show." / "Was {Bear} in this story?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
`kit/story-stage.js` (the story-stage family; not `kit/stage.js`, which is the stage-blocker engine). No family doc exists and the only sibling, bedtime-retell (K-2), is a concept, so this spec describes the engine. Pure parts in one marked block, exposed as `__tool.ss`.
- **Tale**: `{id, panels:[{pic, words}], setting, characters, events:[{id, actor, zone, state, telling, lines}], questions:[{after, ask, answer}], backdrops}`.
- **Stage**: backdrops, zones per backdrop (rectangles with names and pictures), puppets with poses and a move animation; `ss.place(puppet, zone)`.
- **Show**: `ss.watch(tale, onEvent, onOther)` compares each move with the next story event; `ss.log()` keeps the class's order and which events were their way; `ss.play(log)` plays a show back.
- **Retell strip**: frames per event, filled from the log.
- **Playbill**: `ss.bill(tale, picks)` checks characters as an exact set, setting as one, and events as an ordered triple (first, middle, last).
bedtime-retell can reuse Tale, Retell strip and Playbill without the stage. This tool uses all parts.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| The show | Drag puppets anywhere | Nothing is blocked (sandbox), but every out-of-order move is named with how the story went, and the strip shows the class's order with pencil marks, so the retelling in order is what the class sees and hears. |
| Questions | Tap the nearest puppet | Two to five puppets are on stage at each question; answers move between characters and places; a wrong tap gets a detail from the story as a clue. |
| Playbill: Starring | Pick every card | Two cards come from the other tale (exact set; extras named). |
| Playbill: What happens | Any three events | Ordered first, middle, last from seven event cards: 1 in 210 (computed); two events come from the other tale. |
| Playbill: Where | Guess | 1 in 3, after the class has seen the backdrop on stage. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a poster: `poster`, `welcome` (queued, first time), then each `panel` (whole, each waits).
2. Show: `showHow`, `whereAsk`; a backdrop tap plays `whereYes` or `whereOther`.
3. Per event: `nextAsk` (whole); a move plays `event` (whole) or `otherWay`; then `qAsk` (whole) and `qYes` or `qNo`.
4. After the fifth event: `bow`; Play our show plays the log.
5. Playbill: `playbillHow`; Check plays `billYes`, `billMiss` or `billExtra` per section.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.K.1 to RL.K.3 wording (with prompting and support, ask and answer questions about key details; retell familiar stories, including key details; identify characters, settings and major events) | thecorestandards.org, RL K | CCSS ELA 2010 PDF | yes |
| The Three Billy Goats Gruff is a Norwegian folktale (Asbjornsen and Moe): three goats cross a troll's bridge to reach grass, smallest first, each sending the troll to wait for a bigger brother, and the biggest knocks the troll into the stream | G. W. Dasent, Popular Tales from the Norse (1859), "The Three Billy-Goats Gruff", Project Gutenberg eBook #8933 | D. L. Ashliman, Folktexts (University of Pittsburgh), Norwegian tales | yes |
| The Mitten is a Ukrainian folktale in which forest animals crowd into a lost mitten until it bursts | Library of Congress catalog, Alvin Tresselt, The Mitten: An Old Ukrainian Folktale (1964) | Jan Brett, The Mitten (1989), author's note on janbrett.com | yes |
Backed twice: 3. Cut: 0.
Our Mitten retelling uses a badger owner, a red mitten and a cricket, and none of the people, names or pictures from Tresselt's or Brett's books; the original folktale's ending with the troll's eyes and bones is softened to a splash.

Checks run (Python, scratchpad b4, 2026-11-08): playbill ordered triples 7 x 6 x 5 = 210; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the stage, rack, box and strip show with no scroll; at 680x425 with drawers.
2. Goats show: the five events fill the strip in story order with their tellings; a big-goat-first move plays, names the story's order, and My way keeps it with a pencil mark. (RL.K.2)
3. Questions: each of the ten questions takes only its puppet or zone and bows it. (RL.K.1)
4. Mitten show: the five events fill in order; the squeeze-in frame needs Frog, Rabbit, Fox and Bear in that order. (RL.K.2)
5. Playbill: Starring takes only the tale's characters (exact set); Where only its setting; What happens only first, middle, last in order; Print playbill prints one page. (RL.K.3)
6. Free play: every backdrop, puppet and prop works with no questions.
7. Play our show: plays the class's order, their-way events included.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Pre-reader: every panel, card and line is spoken; every card is a picture.
10. Motion off: puppets move without bobbing, curtain fades; no network requests; nothing saved.

## Open questions
- None for Cory.
