# Because Bridge

## One idea
An author's point stands on the far bank of a river and Fern the fox wants to cross to it: the class pulls sentences out of the author's short text and lays them as bridge planks, but only a sentence that tells why the point is true will hold her weight, so a plank that is true but off the point (recess often comes after lunch) wobbles and Fern steps back, and when every plank holds she walks across reading the point aloud with "because" for each one.

## Not like
- question-cube (k-2, spec): answering who, what, where questions and lighting the proof sentence. Here only the reasons for one point, and sentences that are true but do not support it.
- alike-and-different-books (k-2, spec): comparing two books. Here one text and how its parts hold up its point.
- big-question-chart (k-2, concept): pinning facts under parts of an answer to a question. Here building support for an author's point and joining it with because.
- windblown-pages (k-2, concept): putting pictures and captions back and telling what pictures add. Here sentences as reasons.
- main-idea-pinboard (3-5, concept, same family): pinning sentences that prove a main idea, with a coverage meter. Here the same engine as a bridge for K-2, with three planks and no writing.

## Who and how
- Grades K to 2, ELA, module "Reasons an Author Gives" (Reading Informational Text). Standards: RI.K.8, RI.1.8, L.1.6, RI.2.8.
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class says which sentence is a reason and a helper drags or taps. Every sentence, plank and button is spoken and every plank has a picture, so a child alone can play (BASELINE rule 4).
- Three texts, each with a grade tag; any class can open any of them. Each text: Read, Build, Walk, then one more step (K: Point to it; grade 1: Because or and?; grade 2: How does it help?). tool.json `modes: []`, `minutes: "10-15"` per text, `grades_label: "Grades K-2"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.K.8 | Recess text: with the narrator's prompts, pick the three sentences that give reasons and lay them as planks; Point to it: tap the picture that shows each reason | the text with pictures; five plank cards; the bridge | 2 |
| RI.1.8 | Helmet text: pick the three reasons from five, with no prompts; wobbling planks must be swapped | the same, no prompt line | 3 |
| L.1.6 | Because or and?: for four sentence pairs pick the joining word (because, and, but); hear why because tells a reason | two sentence halves and three word cards | 4 |
| RI.2.8 | Trees text: two points, two bridges (Trees help people; Trees help animals); sort six reasons and two off-point facts onto the right bridge, then for each plank pick how it helps the point (a "so" ending) | two bridges; eight planks; three "so" cards per plank | 5, 6 |

## Screens and modes
Header (kit): title "Because Bridge"; `Texts` (book icon); `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A river scene: Fern the fox on the near bank, the far bank empty, and three book signs along the path (Recess, tag K; Helmets, tag 1; Trees, tag 2). First hint: "Pick a text. Tap a sign to read it." The first tap opens the text with its line; the welcome is queued after it (`welcomeAfter: true`).

**Read.** Focus: the text as a picture page (1000 x 520): one picture per sentence with the sentence under it, read aloud in order with each sentence lighting as it is read. Tap a sentence to hear it again. The point (the first sentence) is on a banner on the far bank. `Build the bridge` comes after the reading ends (and is always on after the first reading).

**Build.** Focus: the bridge (three empty plank slots over the river, 1200 x 300) and the five plank cards below it (each a sentence from the text with its picture, 220 x 160, spoken on tap; tapping one also lights its sentence in a small strip of the text). Drag a plank to a slot (or tap the plank, then the slot); drag it back to take it off. In the Recess text the narrator gives a prompt for each pick ("Find a reason that tells why recess is good. Look for something about your body."). `Walk across` turns on when three slots are full.

**Walk.** Fern steps onto the bridge. A plank that does not support the point wobbles and tips (Motion off: it tilts still and gets a crack mark), Fern steps back, and the line says why ("That's true, but does it tell why recess is good for kids?"). The class swaps it; Walk again. When all three hold, Fern crosses, and at each plank the point is read with because: "Recess is good for kids because playing makes their bodies strong." A bridge crossed on the first walk gets a gold flag; any other crossing a plain flag.

**Trees (grade 2).** Two points, two bridges stacked (Trees help people; Trees help animals), each with three slots, and eight plank cards. Walk checks both; a plank on the wrong bridge wobbles with "That's a reason, but for which point?"

**Point to it (K), Because or and? (grade 1), How does it help? (grade 2).** After crossing. Point to it: "Which picture shows how recess helps you make friends?" with three pictures. Because or and?: two sentence halves with a gap and three word cards; the whole sentence is read with the picked word, and only the right one stays. How does it help?: one plank at a time, "Trees give shade, so ___" with three endings.

At 1366x768 the bridge and the plank cards fit above the fold. At 680x425 the bridge is 640 x 180, cards 120 x 90 in one row (five) or two rows (eight).

## Content
**Recess Is Good for Kids** (K; point first; R = reason, F = true but off the point; in the order read):
1. (point) Recess is good for kids.
2. R At recess, kids run, jump and play, and that makes their bodies strong.
3. R After recess, it is easier to sit still and listen in class.
4. R At recess, kids learn to share, take turns and make friends.
5. F Recess often comes after lunch.
6. F Some playgrounds have a tall slide.
Plank texts are short forms of the sentences (a tap lights the full sentence in the text): "Playing makes bodies strong." "After recess, it is easier to listen." "Kids learn to share and make friends." "Recess often comes after lunch." "Some playgrounds have a tall slide."
Point to it: strong body (a child-free picture: a fox cub hanging from monkey bars | a fox cub asleep | a lunch tray); listen (fox cubs at desks listening | cubs on a slide | a bell); friends (two cubs sharing a ball | one cub alone reading | a cub eating).

**Wear a Helmet When You Ride a Bike** (grade 1):
1. (point) You should wear a helmet when you ride a bike.
2. R A helmet covers your head if you fall.
3. R A hard bump on the head can hurt your brain, and a helmet helps stop that.
4. R In many states, the law says kids must wear a helmet on a bike.
5. F Helmets come in lots of colors.
6. F Most bikes have two wheels.
Because or and?: "I wear a helmet ___ it covers my head." (because | and, but); "I have a helmet ___ I have a bike." (and | because, but); "I wanted to ride ___ it was raining." (but | because, and); "I ride slowly on the path ___ people are walking there." (because | and, but).

**Trees Help a City** (grade 2; two points):
1. (point A) Trees help the people in a city.
2. A Trees give shade that keeps streets and houses cooler on hot days.
3. A Tree roots soak up rainwater, so streets flood less.
4. A Tree leaves catch dust and help clean the air.
5. (point B) Trees help the animals in a city, too.
6. B Birds build nests in tree branches.
7. B Squirrels eat the nuts and seeds that trees make.
8. B Bees drink nectar from tree flowers.
9. F Some trees lose their leaves in the fall.
10. F The tallest trees in the world are redwoods.
How does it help? (plank: right "so" ending | two others): shade: "so people stay cool." | so birds have homes. | so streets flood less. Roots: "so streets don't fill with water." | so the air is cleaner. | so people stay cool. Leaves: "so the air is cleaner to breathe." | so squirrels have food. | so streets flood less. Nests: "so birds have a safe home." | so the air is cleaner. | so bees have food. Nuts: "so squirrels have food." | so birds have homes. | so people stay cool. Nectar: "so bees have food." | so squirrels have food. | so the air is cleaner.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Build: plank cards are shuffled each time; any slot takes any plank; a plank can be moved between slots.
- Walk: all wobbling planks wobble together (not one at a time), so a walk shows how many are off the point but the class still says which and why. Nothing is scored; the flag only marks a first-walk crossing.
- Grade 2: a reason on the wrong bridge wobbles with its own line; an off-point fact wobbles on either bridge.
- The extra step's wrong picks dim; the right pick reads its whole sentence.
- `Texts` returns to the river; texts keep their state until `Start over`.

## Look
- Accent `--brand` #6b4e2e walnut brown (header, bridge rails, signs); gold #f4c542 (flags, stars); river blue drawn in the art only; paper #fbf7f0; ink #231a10; muted #665a4c. Scene: a calm river in a spring meadow in soft watercolor.
- Contrast (WCAG 2.1, computed): white on brand 7.62:1; brand on paper 7.14:1; ink on paper 16.03:1; muted on paper 6.28:1; ink on gold 10.53:1.
- Never color alone: wobbling planks tilt and get a crack mark; flags carry a star or a plain stripe; tags carry the grade in words.
- Different from the K-2 ELA neighbors (question-cube magenta, alike-and-different-books, read-along-shelf olive) and this batch (barn red, cobalt, emerald, slate).

## Art
Local FLUX (`scripts/localart.py`); no people (the recess and helmet pictures use fox cubs).
- river (1): "A calm river between two grassy banks in a spring meadow, seen from the side, soft watercolor, no bridge, no text"; 21:9; cutout no.
- fern (stand, step, step back, cross, cheer: 5): "A small red fox with a green scarf <standing / stepping forward / stepping back carefully / walking across / cheering>, soft watercolor, plain white background"; 1:1; cutout yes.
- sentence pictures (Recess 6, Helmets 6, Trees 10 = 22): "<the sentence's scene with fox cubs or animals>, soft watercolor, simple background"; 4:3; cutout no. Examples: "fox cubs running and jumping on a playground", "a fox cub on a bike wearing a helmet", "a bird building a nest in a city tree".
- point-to-it pictures (9, some shared with sentence pictures, 6 new): "<subject>, soft watercolor, plain white background"; 1:1; cutout yes.
About 34 images. Each sentence picture also appears on its plank. Drawn in code: the bridge, planks' frames, cracks, flags, signs, word cards, every control.

## Voice
Bank voice `science-narrator` as the narrator. Not used by the K-2 ELA neighbors, batches 1 and 2, or the rest of this batch. `Curio.voice` with `scope: () => state.text + ':' + state.step`, `welcomeAfter: true`.
- event `sign`: "{Recess Is Good for Kids}!"
- how `welcome`: "Welcome to Because Bridge. Fern wants to reach the author's point on the far bank. Only reasons hold her up."
- event, whole, `sentence`: each sentence as it is read and on tap.
- how `buildHow`: "Find three sentences that tell why {recess is good for kids}. Drag each one onto the bridge."
- event (Recess only) `prompt`: "Find a reason that tells why recess is good. Look for something about {your body}."
- event `plank`: the plank's sentence. event `walkHow` (once): "All set? Tap Walk across."
- event `wobble`: "Wobbly! That's true, but does it tell why {recess is good for kids}? Swap it out." event `wrongBridge`: "That's a reason, but for which point?"
- event, whole, `because`: "{Recess is good for kids} because {playing makes their bodies strong}." per plank. event `flag`: "Fern made it across!"
- event, whole, `pointAsk` / `pointYes` / `pointNo`: "Which picture shows {how recess helps you make friends}?" / "Yes, that shows it!" / "Look again."
- how `joinHow`: "Because tells why. And adds on. But shows a change. Which word fits?" event, whole, `joinRead`: the whole sentence with the picked word. event `joinNo`: "Hmm, does that sound right? Try another."
- event, whole, `howAsk`: "{Trees give shade}, so..." event `howYes` / `howNo`: "Yes! That's how it helps." / "That's how a different reason helps."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
`kit/evidence.js` (the evidence family), described in full in tools/theme-ledger/spec.md, exposed as `__tool.ev`.
This tool uses:
- **Source pack**: each text is a pack with one paragraph per sentence and a key; the point sentences are claims (`{id, text}`), and the key gives each reason 3 for its point and 0 for every other point; off-point facts are 0 for all.
- **Evidence links**: a plank on a bridge is a link `{span (the whole sentence), claim, weight 3}`; no tag or comment.
- **checks**: only `offKey` is used, shown as the wobble (strict here, since the K-2 key is exact); the other checks are off.
- **Strength**: `ev.coverage` gives how many of the point's key reasons are on its bridge; three of three crosses.
- **Board view**: drawn as the bridge (the claim card is the far-bank banner, pinned cards are planks, the coverage meter is the planks that hold).
Not Spans with skips, Ledger view, Series, Draft or Sides.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Build (K, 1) | Guess three of five; pick sentences that sound most like the point | 1 in 10 (computed); the off-point facts are true, from the same text and about the same topic (recess, bikes), so "it's about recess" does not pick. |
| Walk | Swap at random after a wobble | Trial and error can finish a bridge, so the gold flag is only for a first-walk crossing, the wobble line names why it fails, and the because read makes the class hear every reason. The extra step checks the reasons again in a new form. |
| Trees (2) | Guess; put animal sentences anywhere | 1 in 560 (computed) for both bridges; a reason on the wrong bridge wobbles. |
| Because or and? | Always pick because | Because is right in 2 of 4; and and but are right once each (computed). |
| How does it help? | Pick the ending that repeats a word from the plank | Wrong endings come from the other reasons in the same text and are true "so" endings, so only the match decides; each ending is right once and wrong at least once (computed). |
| Point to it (K) | Guess | 1 in 3, and the wrong pictures show the same fox cubs at recess. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a sign: `sign`, `welcome` (queued, first time), then each `sentence` in order (whole, each waits).
2. Build: `buildHow`; Recess only, `prompt` per slot; plank taps read at once; `walkHow` once all three slots are full.
3. Walk: `wobble` or `wrongBridge` for wobbling planks, or `because` per plank (whole, each waits), then `flag`.
4. The extra step: `pointAsk`, `joinHow` then `joinRead`, or `howAsk` (whole), and the yes or no lines.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.K.8, RI.1.8, RI.2.8, L.1.6 wording (with prompting and support, identify the reasons an author gives to support points; identify the reasons; describe how reasons support specific points; use frequently occurring conjunctions such as because to signal simple relationships) | thecorestandards.org, RI and L K-2 | CCSS ELA 2010 PDF | yes |
| Recess builds physical activity, helps attention in class afterward, and builds social skills (sharing, taking turns, friends) | CDC, "Strategies for Recess in Schools" (2017) | American Academy of Pediatrics, "The Crucial Role of Recess in School" (2013) | yes |
| A helmet protects the head in a fall and lowers the risk of head and brain injury | NHTSA, "Bicycle Safety" | CDC, "Bicycle Safety" | yes |
| Many US states have laws that require children to wear bike helmets | IIHS, "Bicycle helmet use laws" | Bicycle Helmet Safety Institute, "Helmet laws for bicycle riders" | yes |
| Tree shade keeps streets and buildings cooler | EPA, "Using Trees and Vegetation to Reduce Heat Islands" | USDA Forest Service, "Urban forests" | yes |
| Trees take up rainwater and reduce stormwater runoff | EPA, "Stormwater Trees" | USDA Forest Service, Urban and Community Forestry | yes |
| Tree leaves catch dust and remove air pollution | USDA Forest Service (Nowak and others), "Air pollution removal by urban trees" | EPA, "Using Trees and Vegetation to Reduce Heat Islands" (air quality section) | yes |
| City trees give birds nests, squirrels nuts and seeds, and bees nectar from their flowers | National Wildlife Federation, "Trees for wildlife" | USDA Forest Service, urban wildlife pages | yes |
| Some trees lose their leaves in fall; the tallest trees are coast redwoods | USDA Forest Service, "Why leaves change color"; National Park Service, Redwood National and State Parks | Britannica, "Deciduous tree" and "Redwood" | yes |
Backed twice: 9. Cut: 0.

Checks run (Python, scratchpad b3, 2026-11-08): choose 3 of 5 is 10 ways, one right; two bridges from eight planks is 560 ways, one right; Because or and? answers 2, 1, 1; How does it help? each ending right once; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the bridge and all plank cards show with no scroll; at 680x425 the same with smaller cards.
2. Recess: only the three reasons cross; each off-point fact wobbles; with prompts per slot; Point to it takes only its pictures. (RI.K.8)
3. Helmets: no prompts; only the three reasons cross. (RI.1.8)
4. Because or and?: each of the four sentences keeps only its word and is read whole. (L.1.6)
5. Trees: only the right three reasons cross each bridge; off-point facts and reasons on the wrong bridge wobble. (RI.2.8)
6. How does it help?: each of the six planks takes only its ending. (RI.2.8)
7. Because read: a crossing reads the point with because once per plank, in plank order.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Pre-reader: every sentence, plank and card is spoken and has a picture.
10. Motion off: wobbles become still tilts with a crack mark; Fern moves without walking frames; no network requests; nothing saved.

## Open questions
- Helmets: the law reason says "In many states". Fine for every class, or swap it for a third safety reason so no class feels it does not apply where they live? (Default used: keep it; also in sara-questions.md.)
