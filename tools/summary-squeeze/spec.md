# Summary Squeeze

## One idea
The student squeezes a passage through a press that allows 50, then 25, then 10 words, and a detail gauge shows which of the passage's key details still survive each squeeze and which opinion words leaked in ("amazing", "I think", "should"), so they decide at every size which details are support and which are only interesting; at 10 words an informational passage ends on its central idea, and a fable's 10-word plot summary fails the gauge until the student names what the details add up to, the theme, so they learn that a summary keeps the central idea and its main support, and that a story's last squeeze is its theme, not its plot.

## Not like
- main-idea-pinboard (3-5, spec): pinning sentences that prove a main idea. Here writing summaries at shrinking sizes, grade 6.
- summary-scaffold (6-8, concept): an organizer with citation frames. Here compression by word budget.
- theme-evidence-ladder (concept): ranking evidence for a theme. Here compressing to the theme.
- theme-tracker (4, spec): details feeding themes with lamps. Here summaries that end on the theme.
- research-rover (4, spec): notes from sources. Here summaries of one passage.

## Who and how
- Grade 6, ELA, module "Central Idea and Summary" (Reading Informational Text and Literature). Standards: RI.6.2, RL.6.2.
- Driver: one student (tool.json `driver: "student"`). Role: lesson. Every sentence is read on tap; summaries are read back by the browser's speech voice.
- Change note (spec fix, 2026-11-10): the press, Gus and the three budgets stay. Added: Gus squeezes a short sample first as the model; before writing, the student marks the sentences that carry the key details and writes the central idea as one sentence, and the gauge's list stays hidden until then; a "Yes" on a partial match is limited to two a summary and is tagged; a Leak hunt of five of Gus's summaries teaches opinion words the 60-word list cannot catch, and the student checks their own summary for them; three more articles, two more fables and one longer story, so each standard has five texts, one a sitting; fable plot summaries are checked for opinion too.
- Passages: five articles written for Curio Class from sourced facts ("Beavers Remake a Valley", "The Lighthouse Keeper's Log", "The Dance in the Hive", "A Ditch Across New York", "Why Leaves Turn"); four fables ("The Fox and the Crow", "The North Wind and the Sun", "The Lion and the Mouse", "The Crow and the Pitcher"; Aesop, V. S. Vernon Jones translation, 1912, public domain) and one longer story ("The Gift of the Magi", O. Henry, 1905, public domain). tool.json `modes: ["Articles", "Fables", "Beat my squeeze"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the three squeezes side by side.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| RI.6.2 (central idea) | determine a central idea of a text | the student | Write the central idea as one sentence before the gauge opens; the 10-word squeeze must carry it | 5 articles | the student's sentence beside the central idea light | 2, 5 |
| RI.6.2 (details) | determine how it is conveyed through particular details | the student | Mark the six sentences that carry the key details, then write a 50-word summary that keeps them | 5 articles, 6 details each | the student's marks; the gauge with lit details | 3 |
| RI.6.2 (objective summary) | provide a summary distinct from personal opinions or judgments | the student | Tap the opinion in five of Gus's summaries; take leaks out of your own; tick the self-check | 5 hunt items; 3 squeezes per text | leak marks and the self-check box | 4 |
| RL.6.2 (theme, details) | determine a theme of a text and how it is conveyed through particular details | the student | Write the theme as a sentence that is not the plot and link the two details that convey it | 4 fables and 1 story | the theme line with linked details | 6 |
| RL.6.2 (summary) | provide a summary distinct from personal opinions or judgments | the student | Write a plot summary (25 words for a fable; 50, 25 and 10 for the story) with no leaks | 5 | the plot summary above the theme line | 6 |

## Screens and modes
Header (kit): title "Summary Squeeze"; `Articles`, `Fables`, `Side by side`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A big iron press in a print shop, a passage on the press bed and a gauge reading "Budget: 50 words", and Gus, an old printer with ink on his apron. First hint: "Tap the passage to hear it." The first tap reads the title; the welcome is queued after it (`welcomeAfter: true`).

**Gus goes first (the model).** Gus squeezes a 120-word sample, "How a Press Prints a Page" (made up and labeled): he marks three sentences, says the central idea in a sentence, writes 30 words, catches one opinion of his own ("the best machine ever made") and takes it out, then squeezes to 10. It cannot be skipped the first time and `Gus's squeeze` reopens it.

**Leak hunt.** Five of Gus's two-sentence summaries of the sample, each holding one opinion or judgment in plain words that a word list would miss ("everyone should learn this", "it is a shame presses are gone", "which is more fun than typing", "the smartest invention", "sadly"). The student taps the opinion in each. A wrong tap can be tried once more; after a second miss Gus underlines it and that item comes back at the end with a new summary. Done once, before the first passage.

**Read.** The passage (about 450 words; fables about 150; the story about 2,000 with a `Listen` button) in numbered sentences; tap to hear.

**Mark and name.** Before the press box opens, the student taps the sentences that carry what matters most (six for an article or the story, three for a fable) and writes the central idea as one sentence ("This article shows that ..."). Marks are checked as a set: the tool says how many of the marks are key details, not which. Two tests, then Gus shows the ones still missing with a "shown" tag. The central idea sentence is kept beside the press and is not marked right or wrong here; the 10-word squeeze tests it.

**Write.** The press box: the student types a summary; a word counter fills like a pressure gauge and turns the box frame dashed when over budget (the Squeeze button stays active and says "Over by {6} words").

**Squeeze.** The detail gauge lists the passage's 6 key details (in data, with word families). A detail lights when the summary has one of its word families; when the match is only partial, the tool asks the student ("You wrote 'dams'. Does that cover 'build barriers of sticks and mud across streams'? Yes or No") and records the answer. Only two Yes answers count in one summary; after that a partial match stays dark until the summary is rewritten. A detail lit by a Yes carries the tag "you said so" and does not count in the details-kept number. The central idea has its own light. Opinion leaks: a list of 60 judgment words and phrases; each found one is marked with "That's your opinion. Does the passage say it?" The list cannot catch every opinion, so before each squeeze counts the student rereads and ticks a self-check, "Every sentence here is something the passage says, not what I think of it", with Gus's clean summary beside it. The tick opens only after the summary has been read back.

**Budgets.** 50, then 25, then 10. Each level shows which details the previous summary kept. At 10, the central idea light must be on; details may go out. The student's central idea sentence from Mark and name is shown beside the 10-word squeeze with "Do these say the same thing?" and a Yes or Not yet tick; Not yet reopens the sentence.

**Fables and the story.** A fable takes a 25-word plot summary first; the story takes 50, 25 and 10. The leak check and the self-check run on these too, so "the crow was foolish" comes out of the plot summary. At 10 words, a plot summary ("The fox tricks the crow and gets the cheese") lights "plot" but not "theme"; the gauge asks "What do these events add up to?" The student writes a theme line (frames offered: "When you ___, ___."); the theme light uses key word families ("flattery", "praise", "trust", "pride"), and the student links two details that convey it. Links are keyed: a detail that does not carry the theme is turned away once with "Does that part show it?"; after a second miss Gus shows one link with a "shown" tag. The story's theme uses the families "give", "sacrifice", "love", "worth".

**Side by side.** Three squeezes in columns, details kept per word shown as a number. Beat my squeeze replays a passage to raise that number.

At 1366x768 the passage and press fit side by side; at 680x425 the passage folds above the press.

## Content
Written for Curio Class from sourced facts:
- Beavers Remake a Valley: beavers build dams of sticks and mud that slow streams and make ponds; ponds and wetlands hold water, raise the water table and give homes to fish, frogs, birds and insects; beavers are called ecosystem engineers; some ranchers and land managers now use beaver dams or human-made copies to restore streams. Central idea: by building dams, beavers change a whole valley's water and life.
- The Lighthouse Keeper's Log: a keeper's day (trimming the wick, winding the clockwork that turned the lens, logging weather), from National Park Service and Coast Guard history facts. Central idea: keeping the light was steady, careful daily work.
- The Dance in the Hive: a honeybee that finds food dances on the comb; the angle of the waggle run shows the direction of the food measured from the sun, and the length of the run shows how far; other bees follow the dance and fly out; Karl von Frisch worked this out and shared a Nobel Prize in 1973. Central idea: honeybees tell each other where food is by dancing.
- A Ditch Across New York: the Erie Canal opened in 1825 and ran about 363 miles from Albany to Buffalo; mules and horses pulled boats along a towpath and locks lifted them; shipping goods became far cheaper and faster; towns along it grew and New York City became the country's busiest port. Central idea: one canal changed how goods and people moved and made New York grow.
- Why Leaves Turn: leaves are green from chlorophyll, which uses sunlight to make food; as days shorten the tree stops making it and the green fades; yellow and orange pigments that were there all along show through; red and purple pigments are made in fall from sugars held in the leaf; the tree then seals off the leaf and it drops. Central idea: fall color comes from what is left, and what is made, when a leaf's green breaks down.
- Fables: "The Fox and the Crow", "The North Wind and the Sun", "The Lion and the Mouse" and "The Crow and the Pitcher" from Aesop's Fables, translated by V. S. Vernon Jones (1912), Project Gutenberg eBook #11339; the printed morals are hidden until the student writes their theme. Theme families: Lion and Mouse, "small", "help", "kindness", "repay"; Crow and Pitcher, "think", "clever", "need", "little by little".
- Story: "The Gift of the Magi" by O. Henry, from The Four Million (1906), Project Gutenberg eBook #7256 (the number checked for book-group-table), full text in numbered sentences.
- Each text carries in data: its key detail sentences (six, or three for a fable), detail word families, central idea or theme families, and for literature the two or more details keyed as conveying the theme.
- Model and Leak hunt: the 120-word sample, Gus's three squeezes of it, and seven two-sentence summaries with one keyed opinion each (five shown, two spare).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Summaries can be edited and re-squeezed any time.
- The student's yes or no on partial matches is kept for that summary only.
- With Motion off the press doesn't come down.

## Look
- Accent `--brand` #4d6b1f press olive (header, press frame, gauge rim); gold #f4c542 (lit details, the central idea light); paper #f5f8ef; ink #18220a; muted #555c49. Scene: an old print shop with type cases.
- Contrast (WCAG 2.1, computed): white on brand 6.11:1; brand on paper 5.69:1; ink on paper 15.37:1; muted on paper 6.49:1; ink on gold 10.15:1.
- Never color alone: lights carry words (kept, missing); leaks are underlined with a label.
- Different from this batch (studio slate, camera purple, raspberry, mixer cyan).

## Art
- People art goes to Gemini: Gus (an older white man with a gray beard and an inky apron), 4 poses; the lighthouse keeper (a woman keeper in the 1880s trimming a wick, 1 picture); "illustrated print shop character <pose>, warm gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): print shop with press (1); beaver pond in a green valley (1); a lighthouse lens room (1); fox and crow (1); wind and sun with a traveler seen far off as a small figure (1).
About 10 images. Drawn in code: press box, gauge, columns.

## Voice
Bank voice `wise-mentor` as Gus (unique in this batch); articles are read by `science-narrator` and fables by `gentle-storyteller` (each unique in this batch). `Curio.voice` with `scope: () => state.passage + ':' + state.budget`, `welcomeAfter: true`.
- how `welcome`: "Fifty words. Then twenty-five. Then ten. Keep what matters most."
- event, whole, `sentence`: the tapped sentence.
- event `over`: "Over by {6} words."
- event `partial`: "You wrote {dams}. Does that cover {build barriers of sticks and mud}?"
- event `leak`: "That's your opinion. Does the passage say it?"
- event `plotOnly`: "That's what happened. What do these events add up to?"
- event `squeezed`: "Squeezed! {4} details kept in {25} words."
- how `mark`: "Tap the six sentences that matter most. Then tap Test."
- how `name`: "Write what the whole passage is about in one sentence."
- how `hunt`: "Tap the part that is Gus's opinion."
- how `selfcheck`: "Read it back. Then tick the box if every sentence comes from the passage."
- event, whole, Gus's squeeze.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: word counter, detail word families with confirm, leak list, budget levels, theme check.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Marks | Tap every sentence; tap until the count is right | Marks are checked as a set of six (or three) and the tool gives only a count; two tests, then missing ones are tagged "shown" on the printout. |
| Details | List keywords | Under 50 words, keywords light details, but the 10-word level needs the central idea's word families in a sentence with a verb. |
| Partial matches | Always answer Yes | Two Yes answers a summary; details lit that way are tagged and left out of the details-kept number. |
| Leak hunt | Tap words at random | Each summary has about twenty words and one keyed phrase; a second miss brings a new summary. |
| Leaks in own summary | Hide opinions in new words; tick the box unread | The 60-word list is backed by the self-check, which opens only after the read-back. The tool cannot judge those words, so the hunt and Gus's clean summary carry the teaching. |
| Central idea | Write anything in the sentence box | The 10-word squeeze must light the central idea, and the two are put side by side for the student to compare. |
| Fables and story | Write the plot again; link any two details | The theme light needs theme word families; links are keyed, with one free miss before a "shown" tag. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. First visit: Gus's squeeze (whole), then `hunt`. Tap the passage: title, `welcome` (queued, first time). `mark`; `name`.
2. Sentences: `sentence` (whole). Squeeze: `over` or `partial` and `leak` as they fire, `selfcheck`, then `squeezed`.
3. Fables at 10: `plotOnly` if no theme.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.6.2 and RL.6.2 wording | thecorestandards.org, Grade 6 | CCSS ELA 2010 PDF | yes |
| Beaver dams slow water, create ponds and wetlands, raise the water table and support many species; beavers are ecosystem engineers | US Fish and Wildlife Service, beavers | National Park Service, beavers as ecosystem engineers | yes |
| Beaver dam analogs are used to restore streams | USDA Natural Resources Conservation Service, beaver dam analogs | US Forest Service, beaver-related restoration | yes |
| Keepers trimmed wicks, wound clockwork that turned the lens, and kept logs | National Park Service, lighthouse keepers' duties | US Coast Guard History Office, lighthouse keepers | yes |
| "The Fox and the Crow" and "The North Wind and the Sun", V. S. Vernon Jones translation (1912), public domain | Project Gutenberg eBook #11339 (checked 2026-11-09) | Library of Congress, catalog record for the 1912 edition | yes |
| Waggle dance: the run's angle shows direction from the sun and its length shows distance; von Frisch shared the 1973 Nobel Prize | NobelPrize.org, Physiology or Medicine 1973 | Encyclopaedia Britannica, Karl von Frisch | to confirm at Build |
| Erie Canal opened 1825, about 363 miles, Albany to Buffalo; cut shipping cost and time | New York State Canal Corporation, canal history | National Park Service, Erie Canalway | to confirm at Build |
| Chlorophyll fades in fall; carotenoids show through; anthocyanins are made in fall | US Forest Service, science of fall colors | SUNY ESF, why leaves change color | to confirm at Build |
| "The Lion and the Mouse" and "The Crow and the Pitcher" are in the Vernon Jones translation; "The Gift of the Magi" is in The Four Million (1906), public domain | Project Gutenberg eBooks #11339 and #7256 | Library of Congress catalog records | to confirm at Build |
Backed twice: 5. Added by the spec fix and not opened in this pass: 4 rows, marked "to confirm at Build". Cut: 0.

Checks run (Python, scratchpad b18, 2026-11-09): the Gutenberg file is the Vernon Jones translation and includes both fables; a sample 10-word theme sentence passes the theme check and a 10-word plot sentence fails it; contrast as in Look.

Spec fix checks (2026-11-10): counted, not run: 5 articles, 4 fables and 1 story give five texts for each code; 7 hunt summaries cover 5 shown plus 2 returns. The four added source rows, the two added fable titles were written from memory and none was opened; Build must open each before the text ships.

## Done when
1. Focus and fold: at 1366x768 passage and press fit; at 680x425 the passage folds above.
2. Before the press opens the student writes the central idea as a sentence; it is shown again beside the 10-word squeeze. (RI.6.2)
3. Six key sentences are marked as a set (three in a fable) before the gauge's list shows; the gauge lights details, with at most two tagged Yes answers a summary. (RI.6.2)
4. The Leak hunt's five summaries are done once; leaks are marked in the student's summaries and the self-check is ticked after the read-back. (RI.6.2, RL.6.2)
5. Budgets 50, 25 and 10 work; 10 needs the central idea. (RI.6.2)
6. Fables and the story need a leak-free plot summary, a theme line and two keyed linked details. (RL.6.2)
7. Five articles, four fables and one story are present, each with its key in data.
8. Gus's squeeze plays before the first passage and can be reopened.
9. Side by side shows details kept per word; Beat my squeeze replays.
10. Print shows the three squeezes, the central idea sentence and any "shown" or "you said so" tags.
11. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
12. Motion off: the press is still; no network requests.

## Open questions
- None for Cory.
