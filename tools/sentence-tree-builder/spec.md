# Sentence Tree Builder

## One idea
The student grows sentences as trees, snapping clauses to the trunk and phrases onto the branch of the word they describe, and the tree shows what each piece does: two trunks side by side for a compound sentence, a grafted branch for a dependent clause, and a phrase hung on the wrong branch makes the sentence say something silly that a small picture shows ("Running across the ice, the farmer's hat blew off" draws a hat with legs), so they learn what phrases and clauses do and how the type of sentence signals how the ideas relate.

## Not like
- sentence-remixer (6, spec): combining for variety and fixing pronouns. Here sentence types and modifiers, grade 7.
- parallel-parking (9, concept): parallel structure. Here phrases and clauses.
- comma-chameleon (4, spec): commas. Here structure.
- grammar-garage (4, spec): grade 4 grammar. Here grade 7 clauses.
- pause-and-break (6-8, spec): punctuation as pauses. Here what each piece modifies.

## Who and how
- Grade 7, ELA, module "Phrases, Clauses and Sentence Types" (Language). Standard: L.7.1 (a, b, c).
- Driver: one student; class mode is a "tallest sensible tree" challenge (tool.json `driver: "student"`). Every piece is read on tap.
- Three groves: The Frozen Pond (a fox, a farmer and a winter morning), The Bakery Fire Drill, The Science Fair. tool.json `modes: ["Grow", "Four ways", "Tallest tree"]`, `minutes: "20-30"`, `grades_label: "Grade 7"`.
- Nothing is saved; `Print` prints the trees and the four-ways answer.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.7.1a | Snap each phrase or clause where it belongs; the piece names its kind and what it modifies | the piece's label on its branch | 2 |
| L.7.1b | Build a target type (simple, compound, complex, compound-complex) and pick the joiner that signals the relationship | the tree shape and the joiner's meaning tag | 3 |
| L.7.1c | Fix misplaced and dangling modifiers by moving the branch or rebuilding the sentence | the silly picture and the fix | 4 |
| L.7.1b | Four ways: build one set of ideas four ways and choose the type that best shows how they connect | four trees and the student's choice with a reason | 5 |

## Screens and modes
Header (kit): title "Sentence Tree Builder"; `Grow`, `Four ways`, `Tallest tree`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A greenhouse with a bare trunk labeled "The fox ran", a basket of pieces and Hazel, an orchard keeper with pruning shears. First hint: "Tap the trunk to hear the sentence." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Grow.** The basket holds phrases ("across the frozen pond", "with a red tail", "at dawn") and clauses ("because the farmer's dog barked", "and the dog gave up", "although the ice was thin", "who lived by the barn"). The student drags a piece onto a word. On snap, the piece names itself ("Prepositional phrase. Tells where the fox ran.", "Dependent clause. Tells why."). A clause dropped on the trunk's side becomes a second trunk (compound) if it is independent; a dependent clause grafts on as a branch.

**Targets.** Puzzles ask for a type: make it compound, then complex, then compound-complex, with the same ideas. Joiners carry meaning tags: because (cause), although (contrast), when (time), and, but, so. A joiner that doesn't fit the relationship is kept but the sentence is read back with "Does {although} fit? The second idea isn't a contrast."

**Modifier levels.** Sentences with misplaced or dangling modifiers: "Running across the ice, the farmer's hat blew off" (a hat running), "She fed the fox with a red tail" read as she has the tail, "The baker found a fire alarm in her apron pocket that was ringing". A picture of the silly meaning shows; the student moves the branch to the right word or rebuilds the sentence by adding the missing doer.

**Four ways.** Four ideas (The ice was thin. The fox crossed the pond. The dog stopped at the shore. The farmer called the dog home.) built as simple sentences, a compound, a complex and a compound-complex; the student picks the one that best shows how the ideas connect and writes why.

**Tallest tree.** The longest sentence that still makes sense; every piece must attach to a word it can modify.

At 1366x768 the tree and basket fit side by side; at 680x425 the basket is below.

## Content
Written for Curio Class: three groves with pieces keyed by kind, target word, and allowed joiners; modifier sentences with their silly pictures and fixes; four-ways idea sets.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pieces can be pulled off and moved; the sentence rereads.
- With Motion off branches appear without growing.

## Look
- Accent `--brand` #2f6b2a leaf green (header, trunks, branches); gold #f4c542 (labels on snap, joiner tags); paper #f3f8f1; ink #0e220c; muted #4e5c4b. Scene: a bright greenhouse.
- Contrast (WCAG 2.1, computed): white on brand 6.45:1; brand on paper 5.99:1; ink on paper 15.57:1; muted on paper 6.60:1; ink on gold 10.31:1.
- Never color alone: pieces carry kind labels; trunks are counted in words ("two trunks: compound").
- Different from this batch (magazine plum, ember brown, frost blue, newsprint slate).

## Art
- People art goes to Gemini: Hazel (a white woman in her sixties with gardening gloves and shears), 3 poses; "illustrated friendly orchard keeper <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): greenhouse (1); silly modifier pictures (6: a hat running on ice, a girl with a fox tail feeding a fox, a ringing apron pocket, and three more from the other groves), "funny children's book illustration of <scene>, soft gouache, no text"; 4:3.
About 10 images. Drawn in code: trunks, branches, pieces, labels.

## Voice
Bank voice `easy-coach` as Hazel and the sentence reader (unique in this batch). `Curio.voice` with `scope: () => state.grove + ':' + state.sentence + ':' + state.piece`, `welcomeAfter: true`.
- how `welcome`: "Every sentence is a tree. Snap each piece onto the word it describes, and the tree shows what it does."
- event `snap`: "{Prepositional phrase}. Tells {where the fox ran}."
- event `joiner`: "Does {although} fit? The second idea isn't a contrast."
- event `silly`: "Wait. Who was running?"
- event, whole, `sentence`: the built sentence.
- how `fourHow`: "Same four ideas, four ways. Which way shows how they connect?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: tree with keyed attach points, piece kinds, joiner meaning tags, modifier pictures.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Snapping | Drop pieces anywhere | Each piece attaches only to keyed words; elsewhere it shows the silly picture or "That doesn't describe {pond}." |
| Targets | Use "and" for everything | Compound-complex targets need a dependent clause; joiner tags question wrong relationships. |
| Modifiers | Delete the phrase | The fix needs the phrase kept, moved or rebuilt with a doer. |
| Four ways | Pick the longest | The choice needs a reason naming a relationship (cause, contrast, time). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the trunk: sentence, `welcome` (queued, first time).
2. Snapping: `snap` per piece; `joiner` as it fires.
3. Modifier levels: `silly` then the fix read as `sentence`.
4. Four ways: `fourHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.7.1 (a, b, c) wording | thecorestandards.org, Language Grade 7 | CCSS ELA 2010 PDF | yes |
| Phrases and clauses; simple, compound, complex and compound-complex sentences | Purdue OWL, sentence types and clauses | Merriam-Webster, compound sentence and complex sentence | yes |
| Misplaced and dangling modifiers | Purdue OWL, dangling modifiers | Merriam-Webster, dangling modifier | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b21, 2026-11-09): the four-ways sample builds to one, two, one-plus-graft and two-plus-graft clause shapes; every sample piece has a keyed attach word; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 tree and basket fit; at 680x425 the basket is below.
2. Pieces snap to keyed words and name their kind and job. (L.7.1a)
3. Target types build with joiner tags. (L.7.1b)
4. Modifier levels show the silly picture and fix by moving or rebuilding. (L.7.1c)
5. Four ways builds four trees and takes a choice with a reason. (L.7.1b)
6. Tallest tree checks every attach point.
7. Print shows the trees.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: branches appear without growing; no network requests.

## Open questions
- None for Cory.
