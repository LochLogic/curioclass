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
- Driver: one student (tool.json `driver: "student"`). Role: lesson. Every sentence is read on tap; the student's rewrite is read back by the browser's speech voice.
- Change note (spec fix, 2026-11-10): the stage, the dial and the can-know panel stay. Added: the narrator voice works the first dial position as the model; the student predicts what each next narrator can know before the dial turns; judgment words and the twist's lines are now marked as a set with a limited number of taps, and the student calls each tilt before the arrow shows; Identify goes from two passages to five, one a poem with a speaker, with one pick each, two evidence lines and an explain line beside a guide; the Tom Sawyer scene is longer, in three parts, so the student follows the narrator across a text and writes how Twain builds him. The sensitivity read is left for the fresh reader at final review; no wording was changed for it.
- Levels: Dial (four narrators), Spot the narrator (judgment words), The twist (an unreliable first-person narrator), Your turn (rewrite), then a public-domain scene. tool.json `modes: []`, `minutes: "25-35"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the student's rewrite and the can-know panel.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| RL.6.6 (what a narrator can know) | explain how an author develops the point of view of the narrator | the student | Before each turn of the dial, tap the facts this narrator can reach; then turn and compare | 3 predictions of 8 facts | the passage and the panel | 2 |
| RL.6.6 (word choice) | explain how an author develops the point of view | the student | Mark the judgment words as a set; for each, say who it tilts the reader toward or against | 6 words | tapped words with a tilt arrow | 3 |
| RL.6.6 (what is hidden) | explain how an author develops the point of view | the student | Mark the three lines where Kai gives himself away, then write what he hides and how the author lets us see it | 3 lines, 1 written answer | the found lines | 4 |
| RL.6.6 (narrator or speaker) | explain how an author develops the point of view of the narrator or speaker in a text | the student | Name the narrator or speaker of a new text, tap two lines that show it, and write how the author built it | 5 (4 passages, 1 poem) | the answer, the lines and the explain line | 5 |
| RL.6.6 (across a text) | explain how an author develops the point of view | the student | In three parts of a longer scene, say what the narrator is doing and tap the line; then write three sentences on how it builds | 3 parts, 1 paragraph | the scene with the student's marks | 7 |
| RL.6.6 (apply) | explain how an author develops the point of view | the student | Rewrite one paragraph from a narrator of your choice | 1 | the student's paragraph and its panel | 6 |

## Screens and modes
Header (kit): title "Perspective Camera"; `Stage`, `Twist`, `Your turn`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A miniature stage with a school lost-and-found counter, a pile of hoodies, Ms. Diaz behind the counter, Kai (a sixth grader) looking for a blue backpack, and Mr. Tran (the custodian) carrying a box in from the gym. A camera on a dial sits in front of the stage. First hint: "Turn the dial to pick a narrator." The first turn reads the narrator's name; the welcome is queued after it (`welcomeAfter: true`).

**The first take (the model).** The narrator voice works the first position, Kai in first person: it lights the facts Kai can reach, stops on one he cannot ("Kai never sees the gym, so this narrator can't tell us"), and writes the model explain line: "The author keeps us inside Kai's head. We get his worry about the notes, and we never hear what Mr. Tran saw." It cannot be skipped the first time and `First take` reopens it.

**Dial.** Four positions; the passage (about 220 words) rewrites for each, written for Curio Class. Before each of the other three positions, the dial locks and the panel's 8 facts show unlit: the student taps the ones this narrator will be able to tell, then turns. The passage rewrites, the panel lights, and any fact the student got wrong is ringed with the sentence that settles it.
- First person (Kai): Kai's worry about the science notes inside; Kai can't know that Mr. Tran saw a blue backpack in the gym.
- Third person limited (Ms. Diaz): she remembers Kai lost a lunchbox last month; she doesn't know about the notes.
- Third person all-knowing: everyone's thoughts, and the backpack under the bleachers.
- Second person ("You walk up to the counter..."): the reader is put in Kai's place.
The can-know panel lists 8 facts (thoughts, secrets, events); each lights for the narrators who can reach it (set in data).

**Spot the narrator.** A version with a narrator who has a stake (Kai's older brother, irritated) uses words that judge without insult: "my careless little brother", "patient Ms. Diaz", "Mr. Tran, who never notices anything". The passage holds six keyed judgment words or phrases among many plain describing words. The student gets six taps, then `Check`. The check says how many of the six are right, not which; the student may move taps and check once more, and after that the missed ones are shown with a "shown" tag. For each found word the student then taps who it tilts the reader toward or against (two arrows, three characters) before the arrow and the plain rewrite ("my brother") show; a wrong call is counted.

**The twist.** Kai's first-person version, extended: Kai says the backpack was stolen, but the reader can find three lines that show Kai left it in the gym after practice ("I didn't even go to the gym. Well, just for a minute."). The student gets three marks and `Check`, with the same rule: a count only, one more check, then "shown". Then two written lines: "Kai hides that ___" and "The author lets us catch it by ___". A guide: says what really happened; points to Kai's own words.

**Identify.** Five new short texts: third person limited, first person with a stake, second person, third person all-knowing, and a poem, Robert Louis Stevenson's "My Shadow", whose speaker is a small child who does not know how shadows work. For each the student picks the narrator type from four (for the poem: who is speaking and what they do not understand, from four), with one pick. A wrong pick is answered with the line that settles it, tagged, and a spare text of that type is added at the end. Then the student taps two lines that show it (keyed: a thought only this narrator could give, a hidden fact, a judging word) and writes one or two sentences on how the author built it. The model line from the first take stays in view with a three-box guide: what this narrator tells; what stays hidden; which words judge. The tool cannot mark the sentences, so the model and the guide do that job, and they print.

**Your turn.** The student picks a narrator (any of the four, or Mr. Tran in first person) and rewrites the opening paragraph. The can-know panel checks their facts: a fact their narrator can't reach lights red with "Could {Mr. Tran} know {Kai's worry}?"

**Public-domain scene.** The fence-painting scene from "The Adventures of Tom Sawyer" (1876), chapter 2, about 900 words in three parts (Tom faces the fence; Ben Rogers arrives; the narrator's closing remarks on work and play), a third person all-knowing narrator that dips into Tom's thoughts and judges him gently, with the same panel. After each part the student picks what the narrator is mostly doing there (inside Tom's head; reporting what anyone could see; stepping back to comment) and taps one line that shows it; keyed, one retry, then "shown". At the end the student writes three sentences on how Twain builds this narrator from the start of the scene to the end, beside the same guide.

At 1366x768 the stage and passage fit side by side; at 680x425 the stage folds above the passage.

## Content
- Written for Curio Class: the four narrations, the brother's version, Kai's twist version, four identify passages (third limited, first person with a stake, second person, all-knowing) of about 120 words each and four spares, one of each type.
- Robert Louis Stevenson, "My Shadow", from A Child's Garden of Verses (1885), public domain, all four stanzas.
- Mark Twain, "The Adventures of Tom Sawyer", chapter 2, from Project Gutenberg eBook #74, about 900 words in three parts, unchanged except cut sentences marked.
- Can-know panel: 8 facts with reach per narrator; six judgment words with tilt; three twist lines; for each identify text its type and its keyed evidence lines; for each Tom Sawyer part its keyed stance and lines.

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
- how `predict`: "Tap what this narrator can know. Then turn the dial."
- how `mark`: "You have {six} taps. Mark the words that judge. Then tap Check."
- how `explain`: "Tap two lines that show it. Then write how the author built it."
- event, whole, the first take.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: narrator dial with four passages, can-know panel, judgment-word key, twist lines, rewrite fact check.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Dial | Turn and watch | The dial locks until the facts are predicted; misses are ringed. |
| Spot | Tap every adjective | Six taps only, checked as a set with a count; a second miss is tagged "shown". The tilt is called before the arrow shows. |
| Twist | Tap every line | Three marks only, checked as a set; then the student writes what is hidden. |
| Identify | Guess the type; write nothing real | One pick; a miss is tagged and adds a spare text. Two keyed evidence lines are needed. The written line is not marked by the tool; the model and guide carry it and it prints. |
| Tom Sawyer | Guess one of three | One retry, then "shown", and a line must be tapped as well. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. First visit: the first take (whole). Turn the dial: `predict`, then `narrator`, `welcome` (queued, first time).
2. Sentences: `sentence` (whole). Spot: `mark`, then `tilt`. Twist: `mark`, then `found`. Identify: `explain`.
3. Your turn: `reach` as it fires.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.6.6 wording | thecorestandards.org, Reading Literature Grade 6 | CCSS ELA 2010 PDF | yes |
| First person, second person, third person limited and third person omniscient: what each narrator can know | Purdue OWL, point of view | ReadWriteThink, point of view lessons | yes |
| "The Adventures of Tom Sawyer" chapter 2, fence-painting scene, public domain | Project Gutenberg eBook #74 (checked 2026-11-09) | Library of Congress, catalog record for the 1876 first edition | yes |
| "My Shadow" by Robert Louis Stevenson, in A Child's Garden of Verses (1885), public domain | Project Gutenberg, A Child's Garden of Verses | Poetry Foundation, "My Shadow" | to confirm at Build |
Backed twice: 3. Added by the spec fix and not opened in this pass: 1 row. Cut: 0.

Design choices (not claims): the 8 can-know facts.

Checks run (Python, scratchpad b18, 2026-11-09): in the sample panel only the all-knowing narrator reaches all 8 facts, Kai and Ms. Diaz each reach at least one fact the other can't, and the twist has three keyed lines; contrast as in Look.

Spec fix checks (2026-11-10): counted, not run: 3 dial predictions, 6 judgment words, 3 twist lines, 5 identify texts with 4 spares and 3 Tom Sawyer parts. The poem and the longer Tom Sawyer cut were named from memory and not opened in this pass; Build must open both and set the three part breaks and the word count from the Gutenberg text.

## Done when
1. Focus and fold: at 1366x768 stage and passage fit; at 680x425 the stage folds above.
2. The dial rewrites the passage and lights the panel only after the student has predicted the reachable facts, three times. (RL.6.6)
3. Six judgment words are marked as a set with six taps, and each tilt is called before its arrow shows. (RL.6.6)
4. The twist's three lines are marked as a set and the student writes what Kai hides. (RL.6.6)
5. Identify takes five texts, one a poem: a single pick, two evidence lines and a written line each. (RL.6.6)
6. Your turn checks reach against the panel.
7. The Tom Sawyer scene runs in three parts with a stance and a line for each and a closing three sentences. (RL.6.6)
8. The first take plays before the dial and can be reopened.
9. Print shows the rewrite, the written lines and any "shown" tags.
10. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
11. Motion off: the camera jumps; no network requests.

## Open questions
- None for Cory.
