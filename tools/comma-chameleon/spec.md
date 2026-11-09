# Comma Chameleon

## One idea
Cammy the chameleon paints a picture of exactly what a sentence says, and the student places commas until Cammy's picture matches the target picture ("Let's eat, Grandma" with Grandma at the table instead of on a plate), so they learn that a comma is a meaning tool, not decoration; levels cover series, introductory words, yes and no, tag questions, direct address and title marks, and a trickster round has them place commas to make a silly picture on purpose, then fix it.

## Not like
- grammar-garage (4, spec): grade 4 grammar repairs with act-out pictures. Here grade 5 commas and title marks, matching a target picture.
- tense-time-line (5, concept): perfect tenses, tense shifts and correlative conjunctions (L.5.1, moved there from this tool).
- dialogue-director (3, spec): dialogue punctuation. Here L.5.2's commas and titles.
- sentence-remixer (6, concept): combining sentences. Here commas only.
- idiom-illustrator (3-5, spec): figurative pictures. Here literal pictures from punctuation.

## Who and how
- Grade 5, ELA, module "Conjunctions, Tense and Commas" (Language). Standard: L.5.2 (a to d). L.5.1 moved to tense-time-line; L.5.2e spelling moved to draft-car-wash's grade 5 Polish station, as the idea card says.
- Driver: one student (tool.json `driver: "student"`). Every sentence is read on tap, with its comma pauses.
- Six levels of 5 sentences, a hidden-error level and the trickster round. tool.json `modes: ["Play", "Make one"]`, `minutes: "5 per level"`, `grades_label: "Grade 5"`.
- Nothing is saved; `Make one` sentences can be printed for a friend.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.5.2a | Series level: place commas so the list shows the right number of things (eggs, milk, cheese and crackers vs cheese crackers) | Cammy's picture with the counted items | 2 |
| L.5.2b | Introductory level: a comma after an introductory word or phrase (After we ate, the dog...) | the picture of who did what when | 2 |
| L.5.2c | Yes and no, tag questions, direct address levels (Let's eat, Grandma) | the picture of who is spoken to | 3 |
| L.5.2d | Titles level: italics for a book or movie title, quotation marks for a song or story title | the picture of a book cover or a song sheet | 4 |
| L.5.2a to c | Hidden error level: one wrong comma among right ones | the mismatch spot glowing | 5 |
| L.5.2a to c | Trickster round: make a silly picture on purpose, then fix it | two pictures, silly and meant | 6 |

## Screens and modes
Header (kit): title "Comma Chameleon"; `Levels`, `Make one`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A sunny greenhouse with an easel and Cammy, a chameleon in a painter's smock holding a brush with her tail. First hint: "Tap the target picture to hear what it should show." The first tap reads the target; the welcome is queued after it (`welcomeAfter: true`).

**Level.** Two pictures: Target (what was meant) and Cammy's (what the sentence says now). The sentence below, with every gap between words a 44 px drop spot. A comma tray. Drag a comma into a gap (or tap a gap and press the comma key); Cammy repaints at once to show the new meaning, and the sentence is read with a pause at each comma. When Cammy's picture matches the target, the level card ticks.

**Picture builder.** Each sentence's data lists its meanings: for each comma pattern that changes meaning, the scene parts to draw (who is at the table, what is on the plate, how many items in the cart). Patterns that don't change meaning but are still wrong (a comma after "and" in a two-item list) draw the same picture and add a small note: "Same picture, but a comma doesn't go here."

**Titles level.** Sentences with titles in them; the student picks italics or quotation marks from the tray for each title (a book, a movie, a magazine; a song, a poem, a short story, a chapter). Cammy paints the thing: a book cover or a song sheet.

**Hidden error level.** Sentences already have commas, one of them wrong; tap the wrong one and drag it to the right gap.

**Trickster round.** A target picture that is silly (the cook is chopped, not the carrots); the student places commas to make Cammy paint it, laughs, then fixes it for the real target.

**Make one.** The student types a sentence and two pictures' worth of meanings by picking from scene parts; it prints as a puzzle for a friend.

At 1366x768 both pictures and the sentence fit; at 680x425 the pictures stack above the sentence.

## Content
35 sentences written for Curio Class, each with its comma patterns and pictures. Examples:
- Series: "At the store we bought eggs, milk, cheese and crackers." vs "eggs, milk, cheese, and crackers" (both 4 items, both accepted; the serial comma note says some style guides use it and some don't) vs "eggs, milk and cheese crackers" (3 items).
- Introductory: "After we ate, the dog licked the plates." vs "After we ate the dog..." (a pause problem shown as a confused reader picture with a question mark).
- Direct address: "Let's eat, Grandma." / "Let's eat Grandma."; "I'm calling, Mom." / "I'm calling Mom."
- Yes and no: "No, thanks." vs "No thanks" (both accepted where meaning is the same; the rule note shows the comma).
- Tag questions: "It's cold, isn't it?"
- Titles: "We read *Charlotte's Web* and sang "Take Me Out to the Ball Game.""
- Trickster: "Our cook likes cooking, her family and her dog." (silly without the comma after cooking: likes cooking her family).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Commas can be dragged out again; Cammy repaints each time.
- The serial (Oxford) comma is accepted both ways where the meaning is the same, with a note.
- Keyboard path: arrow to a gap, press the comma key or Delete.

## Look
- Accent `--brand` #237a57 chameleon green (header, Cammy's frame, tray); gold #f4c542 (matched pictures, the sun); paper #f2f9f5; ink #0c2419; muted #4b5e55. Scene: a bright greenhouse studio.
- Contrast (WCAG 2.1, computed): white on brand 5.26:1; brand on paper 4.92:1; ink on paper 15.32:1; muted on paper 6.48:1; ink on gold 10.07:1.
- Never color alone: a match shows a check and "Match!"; a mismatch shows the differing spot outlined and named.
- Different from this batch (rover indigo, root plum, card red, glacier teal).

## Art
Local FLUX (`scripts/localart.py`), animals only (Grandma is a grandmother goose, Mom is a rabbit).
- greenhouse (1); Cammy (5 poses: paint, point, laugh, think, cheer), "A friendly chameleon painter in a smock holding a brush with her tail <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- scene parts (about 60 sticker cutouts: a family of animals, a dinner table, a plate, groceries, a dog, a phone, a book cover, a song sheet), "<part>, flat sticker style, plain white background"; 1:1; cutout yes.
About 66 images. Drawn in code: pictures assembled from parts, the sentence and gaps.

## Voice
Bank voice `playful-friend` as Cammy (unique in this batch). Sentences are read by Cammy with real pauses at commas. `Curio.voice` with `scope: () => state.level + ':' + state.sentence + ':' + state.step`, `welcomeAfter: true`.
- event `target`: the target description ("Grandma is coming to dinner.").
- how `welcome`: "I paint exactly what a sentence says. Put commas where they belong until my picture matches the target."
- event, whole, `sentence`: the sentence with its current commas.
- how `dragHow`: "Drag a comma into a gap. Watch my picture change."
- event `oops`: the funny mismatch line ("Uh oh, Grandma is on the menu!").
- event `match`: "Match! That comma saved the day."
- event `sameNote`: "Same picture, but a comma doesn't go here."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: gap drop spots, comma patterns, picture builder, title marks.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Match | Try every gap | Each try repaints and reads, which is the lesson; sentences have 6 to 12 gaps, so blind tries are slow. |
| Match | Put commas everywhere | Extra commas change the picture or add the "doesn't go here" note; the level ticks only on an exact accepted pattern. |
| Titles | Mark all with italics | Song, poem and story titles take quotation marks; Cammy paints a book cover instead of a song sheet. |
| Hidden error | Tap every comma | The first wrong tap is free; each later tap reads the rule for the tapped comma. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the target: `target`, `welcome` (queued, first time).
2. Sentence: `sentence` (whole); first drag: `dragHow`.
3. Each comma: repaint; `oops`, `sameNote` or `match`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.5.2 a to d wording | thecorestandards.org, Language Grade 5 | CCSS ELA 2010 PDF | yes |
| Commas separate items in a series; the serial comma before "and" is optional in some styles and required in others | Purdue OWL, commas (series) | The Chicago Manual of Style Online, serial comma (Q and A) | yes |
| Commas after introductory elements, with yes and no, before tag questions, and around direct address | Purdue OWL, extended rules for commas | Merriam-Webster, comma usage guide | yes |
| Italics for titles of long works (books, movies, magazines); quotation marks for short works (songs, poems, short stories, chapters) | Purdue OWL, titles (MLA formatting of titles) | The Chicago Manual of Style Online, titles of works | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b14, 2026-11-09): every sample sentence's meant pattern differs in picture from its no-comma version; the serial and no-serial forms of the series example give the same item count; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 both pictures and the sentence fit; at 680x425 they stack.
2. Series and introductory levels repaint by comma pattern. (L.5.2a, b)
3. Yes and no, tag question and direct address levels repaint. (L.5.2c)
4. The titles level takes italics or quotation marks. (L.5.2d)
5. The hidden error level finds and moves one wrong comma.
6. The trickster round makes the silly picture, then the meant one.
7. Make one prints a two-meaning puzzle.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: Cammy repaints without brush strokes; no network requests.

## Open questions
- None for Cory.
