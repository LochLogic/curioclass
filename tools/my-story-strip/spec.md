# My Story Strip

## One idea
Every panel in a three-panel comic strip has a job, and the kind of strip sets the jobs (What I like: say what you like, say why, say it again; All about: name it, tell a fact, tell another; What happened: first, next, last and how you felt), so the class first fixes Pepper the penguin's mixed-up strips by finding the panel that does the missing job, then each child draws, tells and labels a strip of their own, panel by panel, and plays it back like a little cartoon.

## Not like
- little-book-press (k-2, spec, same format): an open picture book of up to eight pages that prints and folds into a mini book. Here a fixed three-panel strip where each panel has a writing job named by the strip type (opinion, informative, narrative).
- owl-wants-more (k-2, spec): adding details to a thin story the owl brings. Here the child's own piece, built from the job of each part.
- show-and-tell-spotlight (k-2, spec): telling about an object aloud for listeners. Here drawing, telling and labeling a written piece in three parts.
- first-next-last (1, concept): picture-card writing that Robo acts out. Here the child draws every panel and the check is a model strip the class repairs.
- dialogue-director (3, concept, same family): four-panel comics turned into prose with quoted dialogue. Here kindergarten panels with one spoken line and a label each.

## Who and how
- Kindergarten, ELA, module "Draw, Tell and Write" (Writing). Standards: W.K.1, W.K.2, W.K.3.
- Two parts. `Fix Pepper's strips`: teacher-led on a projector, the class says the answer and a helper taps. `Make my strip`: one child (or a pair) at a device or the teacher's screen, with an adult nearby to help with typing if a child wants it. tool.json `driver: "either"`, `modes: ["Fix Pepper's strips", "Make my strip"]`, `minutes: "10-20"`, `grades_label: "Kindergarten"`.
- Every word, card and job is spoken; labels can be built from picture word cards, so a child who cannot yet write can finish a strip (BASELINE rule 4).
- Recording and saving: strips (drawings, labels, recordings) are kept only in this browser on this device, never sent anywhere. Each strip has `Delete`, and the shelf has `Clear all`. A note on the shelf says so in words and is read once. (BASELINE rule 7.)

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.K.1 | What I like strip: draw and tell the thing you like (panel 1), a reason (panel 2), and say it again with "that's why" (panel 3); in Fix, pick the panel that gives the reason | three panels with job banners (heart, "because" arrow, heart again) | 2, 5 |
| W.K.2 | All about strip: name the topic (panel 1) and tell a fact in each of panels 2 and 3; in Fix, pick the panel that tells a fact | job banners (magnifier, fact star, fact star) | 3, 5 |
| W.K.3 | What happened strip: first, next, last, and how I felt in panel 3; in Fix, put the panels in order and pick the face that shows the feeling | job banners (1, 2, 3 path stones and a feeling face) | 4, 5 |

## Screens and modes
Header (kit): title "My Story Strip"; mode tabs `Fix Pepper's strips` and `Make my strip`; `Shelf` (on Make); `Read`, `Motion`, `Sound`. Controls are 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** `Fix Pepper's strips` opens: Pepper the penguin at a drawing desk beside three strip doors (heart: What I like; magnifier: All about; path: What happened). First hint: "Pepper made three strips, but each one got mixed up. Tap a door to see one." The first tap opens that strip with its line; the welcome is queued after it (`welcomeAfter: true`).

**Fix: What I like and All about.** Focus: the strip, three panels across (each 400 x 300 at 1366x768), one panel blank with a dashed edge and its job banner; below, three picture cards (260 x 195) that could go there. `Play` reads the strip with the blank panel as a "hmm". The class picks a card: right, it drops into the panel and the whole strip plays; wrong, the card shows its own job ("That one tells what happened. This panel needs a reason.") and dims.

**Fix: What happened.** Focus: the three panels shuffled in the strip, each with its words. Drag (or tap one, then a place) to order them; `Play` plays them in the current order so a wrong order is heard. When in order, the strip plays and the class picks the face for the last panel from three (happy, sad, scared).

**Make my strip.** Step 1, pick a kind: three big doors with the same pictures. Step 2, the strip: three panels across; the panel being worked on is 600 x 450 (the other two shrink to 240 x 180 beside it) with its job banner on top ("Panel 2: Say why"). Under it, the panel's tools in one row:
- `Draw`: pen in three sizes, ten colors (each with a name read on tap), `Eraser`, `Undo`, `Clear panel`.
- `Tell it`: a big record button (tap to start, tap to stop, 30 s at most, a ring fills as time passes), `Play mine`, `Again`.
- `Label`: picture word cards (12 for the kind, plus its frame cards) that add their word to the label, or `Type` for the keyboard; `Bubble` or `Caption` places the label as a speech bubble or a strip across the panel; drag to move.
`Next panel` and `Back` move along the strip. Step 3, `Play my strip`: each panel grows in turn while its recording plays (or its label is read if there is no recording). Then `Did my strip do its jobs?`: the job of each panel is read with its banner and the maker taps `Yes` or `Not yet`; `Not yet` opens that panel. Then `Save on this device` and `Print`.

**Shelf.** Up to six saved strips as thumbnails with `Open`, `Play`, `Delete`; `Clear all` (asks first). The privacy note sits at the top.

At 1366x768 the strip and the panel tools fit above the fold. At 680x425 one panel shows at a time (380 x 285) with a three-dot strip map; word cards scroll in a row.

## Content
**Fix strips** (Pepper's panels; blank panel; three cards, right first):
1. What I like, "Rainy days": (1) Pepper in rain boots: "I like rainy days." (2) blank, job "Say why". (3) Pepper under an umbrella, grinning: "That's why I love rainy days!" Cards: Pepper jumping in a puddle, "because I can jump in puddles!" | Pepper eating soup, "Then I ate soup." | Pepper looking at snow, "I like snow too."
2. All about, "Penguins": (1) a penguin on ice: "This is all about penguins." (2) a penguin swimming fast underwater: "Penguins can't fly, but they swim fast." (3) blank, job "Tell a fact". Cards: an emperor penguin with an egg on its feet, "Some penguins keep an egg warm on their feet." | Pepper hugging a toy penguin, "I love penguins!" | a penguin at a shop counter, "Then the penguin went to the store."
3. What happened, "The lost mitten" (start order 3, 1, 2): (1) "First, I lost my mitten in the snow." (2) "Next, my puppy dug and found it." (3) "Last, I put it on. I felt ___!" Faces: happy (right) | sad | scared.

**Job banners** (icon; spoken job):
- What I like: heart, "Say what you like."; arrow, "Say why. Use because."; heart, "Say it again: that's why."
- All about: magnifier, "Name your topic."; star, "Tell a fact."; star, "Tell another fact."
- What happened: stone 1, "What happened first?"; stone 2, "What happened next?"; stone 3 and a face, "What happened last? How did you feel?"

**Word cards** (frame cards first, then pictures):
- What I like: I like, because, that's why, best, fun; pictures: park, dog, cat, ice cream, books, swing, rain.
- All about: This is all about, It can, It has; pictures: frog, dog, bug, fish, bird, tree, big, fast, legs.
- What happened: First, Next, Last, I felt; pictures: happy, sad, scared, surprised, park, home, school, friend.
Every card is read when tapped; a picture card adds its word.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Fix: a wrong card dims for this strip; the three strips can be done in any order; each finished strip gets a gold star on its door.
- Make: `Next panel` is always on (no step is locked). `Play my strip` works with any panel empty, saying "This panel is empty. Draw it or tell it." for that panel and moving on. A panel counts as done when it has a drawing (at least 10 strokes or 2 seconds of pen time) and either a recording or a label; done panels get a check on the strip map.
- Recording: needs microphone permission; if it is refused or there is no microphone, `Tell it` says "No microphone. You can use Label instead." and the strip still works.
- Save: drawings as small images, labels as text, recordings as audio, all in this browser's storage on this device. Saving a seventh strip asks which one to delete.
- Print: one landscape page with the three panels, their labels and the kind's name; no audio. The browser's print dialog opens.

## Look
- Accent `--brand` #3d4a5c slate (header, panel frames, job banners); sunny yellow #ffd447 (record ring, stars); coral #c2452b (record dot, job icons, with words); paper #f7f8fa; ink #1b2028; muted #59626e. Scene: a bright cartoonist's desk with pencils in a cup.
- Contrast (WCAG 2.1, computed): white on brand 9.00:1; brand on paper 8.47:1; ink on paper 15.39:1; muted on paper 5.82:1; ink on yellow 11.50:1; coral on paper 4.73:1; white on coral 5.02:1.
- Never color alone: the record button shows a dot and the word; jobs have icons and words; done panels have a check.
- Different from the K ELA neighbors and this batch (barn red, cobalt, emerald, brown); comic frames are thick ink lines, unlike little-book-press's paper pages.

## Art
Local FLUX (`scripts/localart.py`); no people.
- pepper (desk, wave, point, cheer: 4): "A friendly cartoon penguin cartoonist <sitting at a drawing desk / waving / pointing / cheering>, soft bold cartoon style, plain white background"; 1:1; cutout yes.
- fix panels (7 panels plus 6 cards = 13): "A cartoon penguin <in rain boots in the rain / grinning under an umbrella / jumping in a puddle / eating soup / looking at falling snow / hugging a toy penguin / at a shop counter / losing a mitten in the snow / with a puppy digging up a mitten / putting on a mitten>, soft bold cartoon style, simple background"; also "A real penguin <standing on ice / swimming fast underwater>" and "An emperor penguin holding an egg on its feet"; 4:3; cutout no.
- word pictures (18 unique: park, dog, cat, ice cream, books, swing, rain, frog, bug, fish, bird, tree, big, fast, legs, home, school, friend as two cartoon animal friends): "<subject>, simple bold cartoon, plain white background"; 1:1; cutout yes. Feeling faces are drawn in code.
- desk scene (1): "A bright cartoonist's desk with pencils in a cup and paper, soft gouache, no text"; 16:9.
About 36 images. Drawn in code: panel frames, job banners and icons, faces, bubbles, the record ring, the strip map, every control.

## Voice
Bank voice `clear-teacher` as the narrator (Pepper speaks through it). Not used by the K ELA neighbors, batches 1 and 2, or the rest of this batch. `Curio.voice` with `scope: () => state.mode + ':' + state.strip + ':' + state.panel`, `welcomeAfter: true`.
- event `door`: "{What I like}!"
- how `welcome`: "Hi, I'm Pepper. I draw comic strips, and every panel in a strip has a job."
- how `fixHow`: "One panel is missing. What job does it need? Pick the panel that does it." / for What happened: "These panels are mixed up. Put them in order: first, next, last."
- event, whole, `panel`: the panel's words. event `blank`: "Hmm."
- event `fixYes`: "Yes! That panel {says why}." then the whole strip plays. event `fixNo`: "That one {tells what happened}. This panel needs {a reason}."
- event `orderYes`: "First, next, last. Now it makes sense!" event, whole, `feelAsk`: "How did Pepper feel?"
- how `makeHow`: "Pick a kind of strip. Then draw, tell and label each panel."
- event, whole, `job`: the job banner line. event `color`: the color's name. event `card`: the card's word.
- event `recStart` / `recStop`: "Go ahead!" / "Got it."; event `noMic`: "No microphone. You can use Label instead."
- event `empty`: "This panel is empty. Draw it or tell it."
- event, whole, `jobsAsk`: "Panel {2}: did you {say why}?"
- event `saved`: "Saved on this device."
- how `shelf` (once): "Your strips stay on this device. Nobody else gets them. Tap Delete to take one away."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
`kit/comic-maker.js` (the comic-maker family). No family doc exists and no sibling is specced, so this spec describes the engine, written so dialogue-director (grade 3) can reuse it. Pure parts in one marked block, exposed as `__tool.cm`.
- **Strip**: `{id, kind, layout, panels:[{id, job, strokes, labels, audio}]}`. Layouts: `3-across`, `4-grid` (for dialogue-director), `2x3`.
- **Drawing**: strokes as `{color, size, points}` drawn to a canvas per panel; `cm.undo`, `cm.clear`; `cm.inkTime(panel)` and stroke count for "has a drawing".
- **Labels**: `{type: 'bubble'|'thought'|'caption', text, speaker, x, y, tail}`; bubbles size to their text; `cm.script(strip)` returns every label in panel order with its speaker (dialogue-director turns this into prose).
- **Audio**: per-panel recording with the browser's media recorder, a cap in seconds, `cm.record(panelId, cap)`, `cm.play(panelId)`; missing microphone returns `none` and the tool falls back.
- **Play strip**: `cm.playStrip(strip, onPanel)` steps through panels, playing each recording or reading each label, and calls back for the zoom.
- **Jobs**: a kind defines `jobs:[{icon, text}]` per panel; `cm.done(panel)` uses the rules the tool passes (here: drawing plus recording or label).
- **Store**: `cm.save`, `cm.list`, `cm.remove`, `cm.clearAll` in this browser's storage (IndexedDB), with a strip limit the tool sets; nothing leaves the device.
- **Print**: `cm.printSheet(strip)` makes a print-only page of the panels and labels.
This tool uses: Strip (3-across), Drawing, Labels (bubble and caption), Audio, Play strip, Jobs, Store, Print. Not `script` or thought bubbles.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Fix: the missing panel | Guess; pick the panel that looks most like Pepper | 1 in 3; all three cards star Pepper or penguins and are true to the topic, and each wrong card does a different job (an event, a second opinion, a feeling), so only the job decides. |
| Fix: order | Leave it as dealt; swap at random | It never deals in order; three panels have 6 orders, 5 of them wrong, and `Play` reads the current order aloud so a wrong order is heard. |
| Fix: feeling | Guess | 1 in 3, and the right face matches the event (the mitten is found). |
| Make: a strip's jobs | Draw three pictures and say nothing | Play my strip names each empty panel; a panel needs a recording or a label to be done; the jobs check reads each job aloud for the maker to answer. A studio cannot judge what a child says; the adult and the class hear it on Play. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Fix: tap a door: `door`, `welcome` (queued, first time), `fixHow`, the strip's panels (`panel`, whole, with `blank`). A pick: `fixYes` then the strip, or `fixNo`. What happened: `orderYes` after the last drag, then the strip, then `feelAsk`.
2. Make: `makeHow`; per panel `job` (whole) when it opens; color and card taps read at once; `recStart` / `recStop`.
3. `Play my strip`: each panel's recording or label, or `empty`; then `jobsAsk` per panel (whole, each waits).
4. `saved` after Save; `shelf` the first time the shelf opens.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.K.1 to W.K.3 wording (drawing, dictating and writing to compose opinion pieces that tell the topic and state an opinion; informative pieces that name what they are about and supply some information; narratives of a single event or loosely linked events in order, with a reaction) | thecorestandards.org, Writing K | CCSS ELA 2010 PDF, Writing Standards K-5 | yes |
| Penguins can't fly but swim fast underwater | Smithsonian's National Zoo, "Penguins" | Britannica, "Penguin" | yes |
| Some penguins (emperor) keep the egg warm on their feet | Australian Antarctic Division, "Emperor penguins" | National Geographic Kids, "Emperor penguin" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b3, 2026-11-08): orders of three panels 6, five wrong; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the strip and the active panel's tools show with no scroll; at 680x425 one panel at a time with the strip map.
2. Fix What I like: only the puddle card fills the "Say why" panel; then the strip plays all three. (W.K.1)
3. Fix All about: only the egg card fills the fact panel. (W.K.2)
4. Fix What happened: the strip is never dealt in order; Play reads the current order; only first, next, last finishes it; only the happy face fits. (W.K.3)
5. Make: each kind shows its three job banners, read aloud on open; a strip with a drawing and a recording or label in each panel plays from start to end and every panel shows a check.
6. No microphone: Tell it says so and a strip can be finished with labels only.
7. Save and privacy: a saved strip reopens after a reload with drawings, labels and recordings; Delete and Clear all remove them; no network requests at any time; the privacy note is shown and read once.
8. Print: one landscape page with three panels and labels, no controls.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Pre-reader: every job, card and color is spoken; labels can be made from picture cards alone. Motion off: panels switch without zoom.

## Open questions
- None for Cory.
