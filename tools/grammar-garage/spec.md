# Grammar Garage

## One idea
Broken sentences roll into a repair shop with a clear symptom (it means the wrong thing, it won't start, it's in pieces), and the student diagnoses each one and fixes it with the right part (who or which, was running, may or must, a well-placed phrase, the right "there"), and a picture acts out the sentence before and after the repair, so they learn that grammar parts change what a sentence means; the shift ends with a mystery car that has three problems and a repair note for each.

## Not like
- story-blanks (3, spec): word jobs in an arcade story. Here grade 4 parts that change meaning.
- comma-chameleon (5, concept): commas. Here L.4.1's parts.
- sentence-remixer (6, concept): sentence variety. Here fixing broken sentences.
- dialogue-director (3, spec): dialogue punctuation in the student's own story. Here given sentences with one fault each.
- idiom-illustrator (3-5, spec): pictures of figurative meanings. Here pictures that act out literal grammar.

## Who and how
- Grade 4, ELA, module "Grammar in Use" (Language). Standard: L.4.1 (a to g).
- Driver: one student (tool.json `driver: "student"`). Every sentence is read on tap, before and after the fix.
- Seven bays, 5 cars each, then the mystery car. tool.json `modes: ["Shift", "Timed shift"]`, `minutes: "5 per bay"`, `grades_label: "Grade 4"`.
- Nothing is saved; the bay board shows ticks for the session only.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.4.1a | Bay 1: swap in who, whose, which, where or why so the sentence points at the right thing | the act-out picture changing who does what | 2 |
| L.4.1b | Bay 2: change a verb to was running, am running or will be running to fit the time clue | a timeline strip under the picture | 2 |
| L.4.1c | Bay 3: pick can, may or must to match the job card (asking, allowing, required) | the picture of the rule sign changing | 2 |
| L.4.1d | Bay 4: drag adjectives into order (a small old red wagon) | the wagon picture redrawn | 3 |
| L.4.1e | Bay 5: move a prepositional phrase so it says the right thing (the boy with the telescope) | the picture showing who has what | 3 |
| L.4.1f | Bay 6: a car that won't start (fragment) or runs on (run-on): add the missing part or split it | a sentence engine that starts or stalls | 4 |
| L.4.1g | Bay 7: pick to, too or two; there, their or they're for each blank | the picture with the right count or owner | 4 |
| L.4.1 (all) | The mystery car: find and fix three faults and write a short repair note for each | three tags and notes | 5 |

## Screens and modes
Header (kit): title "Grammar Garage"; `Bays`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A garage with seven bays, a car on the lift with a sentence painted on its side, and Rusty, a badger mechanic in coveralls with a wrench. First hint: "Tap a car to read the work order." The first tap reads the order; the welcome is queued after it (`welcomeAfter: true`).

**Work order.** The car's sentence and the customer's complaint: "The dog chased the cat who was barking." "Customer says the cat isn't the one barking." The act-out picture shows what the sentence says now (the cat barking).

**Repair.** The sentence breaks into word chips; the faulty part flashes only after the student taps `Find it` or taps the right chip. Part trays per bay offer 3 to 4 parts. The student drags a part in; `Test drive` redraws the picture to act out the new sentence and reads it. If the picture matches the complaint, the car rolls out; if not, Rusty says what the picture shows ("Now the dog is barking at nothing. Try again.").

**Bay notes.** Each bay starts with a one-screen manual page (the rule in kid words with two examples) the student can reopen.

**Mystery car.** A sentence with three faults from different bays. The student tags each fault with its bay's icon, fixes it, and picks or writes a short repair note ("Changed which to who because it's a person"). The repair notes print as a ticket.

**Timed shift (class).** Five mixed cars against a clock; the board shows cars fixed, never a speed score per student.

At 1366x768 the car, picture and trays fit; at 680x425 the picture sits above the sentence.

## Content
35 cars (5 per bay) written for Curio Class, each with a complaint, a fault, 3 to 4 tray parts and before and after act-out data (which character does what, how many, where). Examples:
- Bay 1: "This is the park which I lost my kite." (where). "The girl which dog won the prize waved." (whose).
- Bay 2: "Tomorrow at noon we ate lunch." (will be eating). "Right now I was reading." (am reading).
- Bay 3: "You may go outside for the fire drill." with the complaint "Customer says everyone has to go; it is not a choice." (must). "You must have a cookie if you want one." (may).
- Bay 4: "a red old small wagon" (a small old red wagon); order: opinion, size, age, shape, color, origin, material, purpose.
- Bay 5: "I saw a dog with a telescope." (With a telescope, I saw a dog.)
- Bay 6: "Because the bus was late." (fragment); "The bus was late we ran." (run-on: The bus was late, so we ran.)
- Bay 7: "Their are too dogs over they're." (There are two dogs over there.)

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pictures are built from parts in code (characters, props and positions from data), so every before and after is drawn from the sentence data.
- Wrong parts never lock the car; the test drive shows the meaning.
- Keyboard path: tab to a chip, pick a part, press Test drive.

## Look
- Accent `--brand` #1d4e89 garage blue (header, bays, trays); gold #f4c542 (the lit fault, rolled-out cars); paper #f2f6fb; ink #0c1a2c; muted #4a5868. Scene: a clean, sunny garage.
- Contrast (WCAG 2.1, computed): white on brand 8.39:1; brand on paper 7.73:1; ink on paper 16.13:1; muted on paper 6.70:1; ink on gold 10.76:1.
- Never color alone: faults flash and get a wrench icon; bays have numbers and icons.
- Different from this batch (card crimson, lamp amber, editor green, vase terracotta).

## Art
Local FLUX (`scripts/localart.py`), animals only.
- garage (1); Rusty (4 poses: read, wrench, think, thumbs up), "A friendly badger mechanic in blue coveralls with a wrench <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- act-out parts (about 40 sticker cutouts: dog, cat, a rabbit girl, kite, wagon in three sizes, bus, telescope, rule sign), "<object or animal>, flat sticker style, plain white background"; 1:1; cutout yes.
About 45 images. Drawn in code: cars, sentence chips, trays, timeline strip, sentence engine.

## Voice
Bank voice `gravel-ranger` as Rusty (unique in this batch). Sentences are read by Rusty too. `Curio.voice` with `scope: () => state.bay + ':' + state.car + ':' + state.step`, `welcomeAfter: true`.
- event `order`: the complaint ("Customer says the cat isn't the one barking.").
- how `welcome`: "Every sentence in this shop has one problem. Read the work order, find the broken part, and swap in the right one."
- event, whole, `sentence`: the sentence on the car.
- how `repairHow`: "Drag a part from the tray into the sentence, then tap Test drive."
- event `wrongShows`: the bay's line for what the picture shows ("Now the dog is barking at nothing. Try again.").
- event `rolls`: "Fixed! It means what the customer wanted."
- how `mysteryHow`: "Three problems in this one. Tag each one, fix it, and write a repair note."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: sentence chips, part trays, act-out picture builder, sentence engine.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Repair | Try every part | 3 to 4 parts per car; each wrong try redraws the picture and says what it means now, which is the lesson. |
| Adjective order | Drag in any order | 3 adjectives have 6 orders and only one is right (checked); the picture shows the wrong one, read aloud. |
| Mystery car | Fix without notes | The ticket needs a note per fix; notes can be picked from 3, one per fault kind. |
| Timed shift | (class only) | Shows cars fixed, not a speed score. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a car: `order`, `welcome` (queued, first time), `sentence` (whole).
2. First repair in a bay: `repairHow`.
3. Test drive: `rolls`, or `wrongShows`.
4. Mystery car: `mysteryHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.4.1 a to g wording | thecorestandards.org, Language Grade 4 | CCSS ELA 2010 PDF | yes |
| Order of adjectives: opinion, size, age, shape, color, origin, material, purpose | Cambridge Dictionary, English Grammar Today: adjectives, order | British Council, LearnEnglish: adjective order | yes |
| May for permission, can for ability, must for what is required | Merriam-Webster, can vs may usage note | Purdue OWL, modal verbs | yes |
| A fragment lacks a subject, a verb or a complete thought; a run-on joins sentences without the right punctuation or joining word | Purdue OWL, sentence fragments; run-ons | UNC Writing Center, fragments and run-ons | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b13, 2026-11-09): 3 adjectives give 6 orders, and every bay 4 phrase sorts to one order by the category list; each bay has 5 cars; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the car, picture and trays fit; at 680x425 the picture stacks.
2. Bays 1 to 3 repair meaning with relative words, progressive verbs and modals. (L.4.1a, b, c)
3. Bays 4 and 5 order adjectives and place phrases. (L.4.1d, e)
4. Bays 6 and 7 fix fragments, run-ons and confused words. (L.4.1f, g)
5. The mystery car needs three tags, fixes and notes, and prints a ticket.
6. Test drive redraws the picture from sentence data before and after.
7. The timed shift shows cars fixed only.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: cars appear in place instead of rolling; no network requests.

## Open questions
- None for Cory.
