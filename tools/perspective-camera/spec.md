# Perspective Camera

## One idea
One scene sits on a little stage (a lost-and-found counter, three people and a missing backpack), and the student turns a camera dial between narrators (first person inside Kai's head, third person limited over Ms. Diaz's shoulder, third person all-knowing high above, and second person) while the passage rewrites itself and a "can know" panel lights the thoughts, secrets and events that narrator can reach; then they tap the words that tilt the scene (my careless little brother, patient Ms. Diaz), catch a first-person narrator who isn't telling everything, and rewrite a paragraph from a narrator of their choice, so they learn how an author builds a narrator's point of view through what is told, hidden and judged.

## Not like
- swap-the-teller (3-5, concept): three tellers of one mix-up. Here narrator types and their reach, grade 6.
- blizzard-scenes (6-8, spec): writing new versions from seats. Here turning one scene through narrator types and spotting judgment words.
- tone-dial (10, concept): tone words. Here point of view.
- eyewitness-vs-reporter (4, spec): firsthand and secondhand accounts. Here narrators in fiction.
- inference-interrogation (5, spec): proving inferences. Here what a narrator can know.

## Who and how
- Grade 6, ELA, module "Point of View" (Reading Literature). Standard: RL.6.6.
- Driver: one student (tool.json `driver: "student"`). Every sentence is read on tap; the student's rewrite is read back by the browser's speech voice.
- Levels: Dial (four narrators), Spot the narrator (judgment words), The twist (an unreliable first-person narrator), Your turn (rewrite), then a public-domain scene. tool.json `modes: []`, `minutes: "25-35"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the student's rewrite and the can-know panel.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.6.6 (narrator) | Turn the dial; the passage rewrites and the can-know panel lights what this narrator reaches | the passage and the panel | 2 |
| RL.6.6 (how the author develops it) | Tap judgment words and see how each tilts the reader | tapped words with a tilt arrow | 3 |
| RL.6.6 | The twist: find the lines where the first-person narrator hides something | the found lines | 4 |
| RL.6.6 | Identify the narrator of a new passage and explain in a line how the author built it | the answer and the line | 5 |
| RL.6.6 | Rewrite one paragraph from a narrator of your choice | the student's paragraph and its panel | 6 |

## Screens and modes
Header (kit): title "Perspective Camera"; `Stage`, `Twist`, `Your turn`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A miniature stage with a school lost-and-found counter, a pile of hoodies, Ms. Diaz behind the counter, Kai (a sixth grader) looking for a blue backpack, and Mr. Tran (the custodian) carrying a box in from the gym. A camera on a dial sits in front of the stage. First hint: "Turn the dial to pick a narrator." The first turn reads the narrator's name; the welcome is queued after it (`welcomeAfter: true`).

**Dial.** Four positions; the passage (about 220 words) rewrites for each, written for Curio Class:
- First person (Kai): Kai's worry about the science notes inside; Kai can't know that Mr. Tran saw a blue backpack in the gym.
- Third person limited (Ms. Diaz): she remembers Kai lost a lunchbox last month; she doesn't know about the notes.
- Third person all-knowing: everyone's thoughts, and the backpack under the bleachers.
- Second person ("You walk up to the counter..."): the reader is put in Kai's place.
The can-know panel lists 8 facts (thoughts, secrets, events); each lights for the narrators who can reach it (set in data).

**Spot the narrator.** A version with a narrator who has a stake (Kai's older brother, irritated) uses words that judge without insult: "my careless little brother", "patient Ms. Diaz", "Mr. Tran, who never notices anything". The student taps words that show the narrator's attitude; each shows a tilt arrow (toward or against a character) and a plain rewrite ("my brother").

**The twist.** Kai's first-person version, extended: Kai says the backpack was stolen, but the reader can find three lines that show Kai left it in the gym after practice ("I didn't even go to the gym. Well, just for a minute."). The student finds the lines.

**Identify.** Two new short passages (one third limited, one first person with a stake); the student picks the narrator type and writes one line on how the author built it (what's told, hidden or judged).

**Your turn.** The student picks a narrator (any of the four, or Mr. Tran in first person) and rewrites the opening paragraph. The can-know panel checks their facts: a fact their narrator can't reach lights red with "Could {Mr. Tran} know {Kai's worry}?"

**Public-domain scene.** A short scene from "The Adventures of Tom Sawyer" (1876), chapter 2, the fence-painting (third person all-knowing that dips into Tom's thoughts and judges him gently), with the same panel.

At 1366x768 the stage and passage fit side by side; at 680x425 the stage folds above the passage.

## Content
- Written for Curio Class: the four narrations, the brother's version, Kai's twist version, two identify passages.
- Mark Twain, "The Adventures of Tom Sawyer", chapter 2, from Project Gutenberg eBook #74, about 350 words, unchanged except cut sentences marked.
- Can-know panel: 8 facts with reach per narrator; judgment-word key with tilt.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- With Motion off the camera jumps between positions.
- The rewrite panel only checks facts from the panel list; anything else is the student's own.

## Look
- Accent `--brand` #6b3fa0 camera purple (header, dial, stage curtain); gold #f4c542 (the lit panel facts, the spotlight); paper #f7f3fb; ink #1d0f2e; muted #5b5266. Scene: a toy theater with a school set.
- Contrast (WCAG 2.1, computed): white on brand 7.38:1; brand on paper 6.74:1; ink on paper 16.52:1; muted on paper 6.74:1; ink on gold 11.13:1.
- Never color alone: panel facts say "can know" or "can't know"; tilt arrows carry words.
- Different from this batch (studio slate, raspberry, mixer cyan, press olive).

## Art
- People art goes to Gemini: Kai (a Vietnamese American kid about 11 in a team hoodie), Ms. Diaz (a Mexican American woman in her forties with a cardigan), Mr. Tran (an older Vietnamese American man, custodian's uniform, kind face), Kai's brother (about 15); 3 poses each; "illustrated toy theater figure <description> <pose>, warm gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): the stage set (1), a blue backpack under bleachers (1); no people.
About 14 images. Drawn in code: dial, camera, panel.

## Voice
Bank voice `smooth-narrator` reads the third-person and second-person narrations and hints (unique in this batch); first-person Kai is `casual-peer` (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.narrator`, `welcomeAfter: true`.
- event `narrator`: "{First person}. Inside {Kai}'s head."
- how `welcome`: "Same scene, different camera. Watch what each narrator can know."
- event, whole, `sentence`: the tapped sentence.
- event `tilt`: "{Careless} tilts you against {Kai}."
- event `found`: "Caught it. Kai left that out."
- event `reach`: "Could {Mr. Tran} know {Kai's worry}?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: narrator dial with four passages, can-know panel, judgment-word key, twist lines, rewrite fact check.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Spot | Tap every adjective | Only keyed words tilt; other taps say "This one describes but doesn't judge." |
| Twist | Tap every line | Each wrong tap reads the line back with "Does this hide anything?"; three keyed lines finish it. |
| Identify | Guess the type | The line on how it's built is required and read back. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Turn the dial: `narrator`, `welcome` (queued, first time).
2. Sentences: `sentence` (whole). Spot: `tilt`. Twist: `found`.
3. Your turn: `reach` as it fires.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.6.6 wording | thecorestandards.org, Reading Literature Grade 6 | CCSS ELA 2010 PDF | yes |
| First person, second person, third person limited and third person omniscient: what each narrator can know | Purdue OWL, point of view | ReadWriteThink, point of view lessons | yes |
| "The Adventures of Tom Sawyer" chapter 2, fence-painting scene, public domain | Project Gutenberg eBook #74 (checked 2026-11-09) | Library of Congress, catalog record for the 1876 first edition | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): the 8 can-know facts.

Checks run (Python, scratchpad b18, 2026-11-09): in the sample panel only the all-knowing narrator reaches all 8 facts, Kai and Ms. Diaz each reach at least one fact the other can't, and the twist has three keyed lines; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 stage and passage fit; at 680x425 the stage folds above.
2. The dial rewrites the passage and lights the panel. (RL.6.6)
3. Judgment words tilt with arrows. (RL.6.6)
4. The twist's three lines are found. (RL.6.6)
5. Identify takes a type and a line. (RL.6.6)
6. Your turn checks reach against the panel.
7. The Tom Sawyer scene works with the panel.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the camera jumps; no network requests.

## Open questions
- None for Cory.
