# Draft Car Wash

## One idea
A muddy rough draft rolls into a car wash with a ticket naming its reader and its job (teach a six-year-old cousin to plant a seed), and at each station the student adds, cuts, moves, shines words, buffs sentences and finally polishes mistakes, each choice backed by a reason sign, then the same draft rolls through again for a different reader (the principal), and the student sees that the changes that make writing fit depend on who reads it, while fixing mistakes is only the last station.

## Not like
- owl-wants-more (K-2, concept): adding details for a curious owl. Here grades 3-5 and all kinds of revising, then editing.
- editors-in-the-margin (high school, concept): margin comments on a peer's essay. Here a guided station line with one reader at a time.
- deadline-desk (3-5, spec): routine and stamina for a newspaper. Here one draft revised for a reader.
- class-pet-pitch (3, spec): writing two pieces from facts. Here changing a given draft.
- hamburger-paragraph (2, built): paragraph parts. Here revising for fit.

## Who and how
- Grades 3-5, ELA, module "Revising and Editing" (Writing). Standards: W.3.4, W.3.5, L.3.3, W.4.4, W.4.5, L.4.2, L.4.3, W.5.4, W.5.5, L.5.3, and taken in: L.3.2 (commas in addresses, spelling patterns) and L.5.2 (spelling) at Polish.
- Driver: one student (tool.json `driver: "student"`). Text is read on tap.
- Grade picker sets the drafts and the Polish rules (grade 3, 4 or 5). tool.json `modes: []`, `minutes: "15-25"`, `grades_label: "Grades 3-5"`.
- Extra: `My own draft` lets the student paste or type their own draft; the stations become a checklist. The line under the box says "Your draft stays on this device. Nothing is sent anywhere." It is not saved after the page closes.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.3.4, W.4.4, W.5.4 | Read the ticket (reader and job) before every run; run the same draft for a second reader | the ticket and the before-after-after view | 2, 7 |
| W.3.5, W.4.5, W.5.5 | Add station: pick the missing step or detail the reader needs | the new sentence sliding in with its reason sign | 3 |
| W.3.5, W.4.5, W.5.5 | Cut station: pick the sentence that wanders off the job | the sentence rinsed away | 3 |
| W.3.5, W.4.5, W.5.5 | Move station: drag sentences into an order that works | the reordered draft | 3 |
| L.3.3a, L.4.3a | Word Shine: pick the more exact word or the phrase for effect | the shining word | 4 |
| L.3.3b | Word Shine at grade 3: a talk-or-write card spots spoken versus written phrasing | the card | 4 |
| L.4.3c | Word Shine at grade 4: formal or informal for this reader | the card | 4, 7 |
| L.5.3a | Sentence Buff: combine choppy sentences, expand a thin one, reduce a long one | the buffed sentence | 5 |
| L.4.3b | Sentence Buff at grade 4: punctuation for effect (an exclamation point, or a comma for a pause) | the card | 5 |
| L.3.2, L.4.2, L.5.2 | Polish: capitals, commas, quotation marks, spelling | each fix sparkling | 6 |

## Screens and modes
Header (kit): title "Draft Car Wash"; `Drafts`, `My own draft`; `Read`, `Motion`, `Sound`, `Print`.

**On load and first tap.** A muddy cartoon car with the draft painted on its side, a ticket on its windshield, and Suds the otter in a car-wash cap. First hint: "Tap the ticket to see who will read this draft." The first tap plays the ticket; the welcome is queued after it (`welcomeAfter: true`).

**Station line.** Focus: the car (the draft as a card 640 x 360, sentences numbered) moving left to right through six stations shown as arches: Add, Cut, Move, Word Shine, Sentence Buff, Polish. One station is open at a time.
- **Add.** Three candidate sentences; one gives the reader something it needs (a missing step), one is true but not needed, one is for a different reader. Pick and drop it in its place (the drop spot must be right: the step goes where it belongs). Reason sign: "Your cousin needs to know to water the seed."
- **Cut.** Tap the sentence that wanders. Reason sign: "This is about your dog, not about planting."
- **Move.** Drag numbered sentences; the station checks the data order rules (steps before results; first, then, last).
- **Word Shine.** Two marked words; each offers three choices, one exact for this reader. Grade 3 adds a talk-or-write card ("gonna" or "going to"); grade 4 a formal-or-informal card for the reader.
- **Sentence Buff.** Grade-set: combine two choppy sentences (pick the joined version), expand a thin one, reduce a wordy one; each choice shows its effect.
- **Polish.** Errors are underlined only after the student taps `Find mistakes` (the count shows: "4 to fix"); tap one, pick the fix. Grade 3: capitals, address commas, spelling patterns; grade 4: plus quotation marks in speech and the comma before and or but; grade 5: plus spelling.

**Roll-out.** Before and after side by side, with the ticket. Then `Same draft, new reader`: a second ticket ("Reader: the principal. Job: explain the garden project.") runs the clean draft again; the Add, Cut and Word Shine choices change (the cousin's "super fun" becomes "students learn"); Polish has nothing new. The end shows all three versions with each reader.

**My own draft.** The student pastes or types; each station becomes a question card ("Who is your reader? What do they still need?"). No scoring.

At 1366x768 the draft and the open station fit; at 680x425 the station arches become a step bar.

## Content
Drafts (written for Curio Class; 4 per grade, each 6 to 9 sentences with a first and second ticket):
- Grade 3: Plant a Seed (cousin, 6 / the principal); Thank You, Firefighters (a firefighter / the class newsletter); My Best Recess Game (a new student / the PE teacher); Make a Paper Boat (a friend at home / a library display card).
- Grade 4: Our Class Garden (a grandparent / the town paper); Why We Need a Bike Rack (the PTA / a classmate); The Day the Power Went Out (a pen pal / a writing contest judge); Feed the Birds in Winter (a younger brother / a nature center sign).
- Grade 5: Clean the Creek Day (volunteers / the city council); A Book You Should Read (a reluctant reader / the librarian's blog); How a Volcano Erupts (a fourth grader / a science fair board); Our Trip to the Museum (a parent email / the school website).
Each draft has data: the missing piece, the wandering sentence, the correct order rules, two shine words with choices, buff items and Polish errors (4 to 6, by grade rules).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A wrong pick shows the reason sign for why it doesn't fit this reader, then lets the student pick again; it is never the end.
- Every station has `Why?` which reads its reason sign.
- The car moves only when the station is done; `Motion` off makes it jump.
- Grade 4 punctuation-for-effect cards use exclamation points, question marks and commas.

## Look
- Accent `--brand` #1d5f8c car-wash blue (header, arches, tickets); gold #f4c542 (sparkles, the open station); paper #f3f8fc; ink #0f2233; muted #4a5a68. Scene: a bright car wash with spinning brushes and bubbles.
- Contrast (WCAG 2.1, computed): white on brand 6.85:1; brand on paper 6.40:1; ink on paper 15.15:1; muted on paper 6.65:1; ink on gold 9.96:1.
- Never color alone: each station arch has a name and an icon (plus, scissors, arrows, star, polish cloth, check).
- Different from this batch (office green, ink navy, newsprint red, sticker magenta).

## Art
Local FLUX (`scripts/localart.py`); readers are drawn as animals (a young rabbit cousin, a badger principal), so no people art.
- car wash (1): "A bright cartoon car wash with six arches, brushes and bubbles, soft gouache, no text"; 16:9; cutout no.
- Suds (4, wave, point, scrub, cheer): "A cheerful otter car-wash worker in a cap <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- car (3, muddy, half, shiny): "A small cartoon car <muddy / half clean / shining>, soft gouache, plain white background"; 4:3; cutout yes.
- readers (24): "<a young rabbit / a badger principal / ...> portrait, soft gouache, plain white background"; 1:1; cutout yes.
About 32 images. Drawn in code: draft card, tickets, signs, arches, step bar.

## Voice
Bank voice `casual-peer` as Suds (unique in this batch). `Curio.voice` with `scope: () => state.draft + ':' + state.reader + ':' + state.station`, `welcomeAfter: true`.
- event `ticket`: "Reader: {your cousin, age 6}. Job: {teach how to plant a seed}."
- how `welcome`: "Welcome to the Draft Car Wash! We clean drafts for their reader. Mistakes come last, at Polish."
- how `stationHow` (per station): "Add: pick what your reader still needs, then drop it in." / "Cut: tap the sentence that wanders off the job." / "Move: drag the sentences into an order that works." / "Shine: pick the best word for this reader." / "Buff: pick the sentence that reads best." / "Polish: tap Find mistakes, then fix each one."
- event, whole, `reason`: the reason sign.
- event `rollOut`: "Look how it shines! Now, same draft, new reader."
- event `compare`: "Same facts, different reader, different changes."
Read speaks the hint, which names the next action and control and never a disabled one. Spelling fixes are shown, not spoken letter by letter.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Add, Cut, Shine | Guess | Wrong picks show why and the station waits; there is no score to farm, and the reason signs carry the teaching. |
| Move | Random order | Order rules must all hold; most random orders of 6 to 9 sentences fail. |
| Reader swap | Repeat the first choices | The second reader's right answers differ in every Add, Cut and Shine item (checked in data). |
| Polish | Tap everything | Only underlined errors open, and only after Find mistakes; each needs its right fix. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the ticket: `ticket`, `welcome` (queued, first time).
2. Each station: `stationHow` (first time); each pick: `reason` (whole).
3. Roll-out: `rollOut`; second run, then `compare`.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.3.4 to W.5.5, L.3.3, L.4.2, L.4.3, L.5.3, L.3.2 and L.5.2 wording | thecorestandards.org, Writing and Language Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
| Planting a seed: plant it at the depth on the packet, water it, give it light, and keep the soil moist while it sprouts (the Plant a Seed draft) | University of Minnesota Extension, starting seeds | RHS, sowing seeds | yes |
| Volcano draft: magma rises, pressure builds and it erupts as lava, ash and gas | USGS, Volcano Hazards Program | National Geographic Kids, volcano facts | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b8, 2026-11-08): every draft's second-reader answers differ from the first in each Add, Cut and Shine item; Polish errors per draft 4 to 6; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the draft and the open station fit; at 680x425 the arches are a step bar.
2. Every run starts with the ticket, and its reader appears on the roll-out. (W.x.4)
3. Add, Cut and Move work as described, each choice with a reason sign. (W.x.5)
4. Word Shine offers grade-set cards (talk-or-write at 3, formal-or-informal at 4). (L.3.3, L.4.3)
5. Sentence Buff combines, expands and reduces. (L.5.3a, L.4.3b)
6. Polish shows its count only after Find mistakes and uses the grade's rules. (L.3.2, L.4.2, L.5.2)
7. The reader swap changes the right answers and ends with three versions side by side.
8. My own draft turns stations into questions and keeps nothing after the page closes.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: the car jumps between stations; no network requests.

## Open questions
- None for Cory.
