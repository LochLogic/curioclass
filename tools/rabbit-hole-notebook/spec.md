# Rabbit Hole Notebook

## One idea
A notebook lies open to a blank page beside a shelf of six big question cards (Why do cities have so many pigeons? Who decides what goes on a stamp? Why is the ocean salty? and three more), and June, a high school librarian's aide (made up, labeled "illustration"), says "Pick the question you most want answered," and the student picks one and starts reading short sources written for the tool from checked facts, a museum note, a city report, an interview and a chart, each answering a little and raising two or three new, smaller questions at the bottom; the student picks one to follow and the notebook draws a new branch, so "Why so many pigeons?" leads to a museum note that pigeons are rock doves people brought to North America in the 1600s, which raises "Why did people bring them?" and "What do pigeons eat in a city?"; every few sources the notebook asks "Does your big question still fit?" and the student can reword it ("Why did people bring pigeons to cities?"), with the old wording kept, crossed out; the student decides when they have enough, writes a three-line answer, and lists the supporting questions that got them there, while a spoken line says the notebook stays on this device; at the end the map shows that small questions shaped the big one and the big one picked the small ones, so a student in grades 6 to 8 learns to follow curiosity across sources and see how questions grow during research.

## Not like
- enduring-questions (Grades 9-12, spec): enduring issues and expert positions. Here one curiosity path.
- wonder-wall (Grades K-2, live): sorting questions. Here following them across sources.
- windows-and-mirrors-shelf (Grades 3-5, spec): reading lives. Here research questions.
- eras-of-computing (Grades 6-8, spec): a fixed timeline. Here a path the student chooses.

## Who and how
- Grades 6-8, Library, module "Rabbit Hole Notebook". Standards: AASL Explore (Shared Foundation V), AASL National School Library Standards (2018); D1.4.6-8 (points of agreement and disagreement experts have about a compelling question, worked here as how supporting and compelling questions reshape each other), C3 Framework.
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every source and note. Controls 48 px or more.
- Six big questions, about 40 short sources (six or seven per question), branches, rewrite checks, the stop rule, a three-line answer. Extra: Swap notebooks (a partner reads the map and guesses the final question). tool.json `modes: ["Notebook", "Swap notebooks"]`, `minutes: "25-40"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| AASL Explore | Follow sources and branches; reflect at each rewrite | the branching map | 2 |
| D1.4.6-8 | Reword the big question; tie supporting questions to the answer | crossed-out wording; the answer's links | 3 |

## Screens and modes
Header (kit): title "Rabbit Hole Notebook"; `Notebook`, `Swap notebooks`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The open notebook, the shelf of six cards, and June with a pencil behind her ear. The welcome is queued (`welcomeAfter: true`): "Pick the question you most want answered. Tap a card." First hint: "Tap a question card."

**Read (focus: the source).** At 1366x768 the source is left with the notebook map right; at 680x425 the map is a tab. Each source names its type and where its facts come from, with two or three new questions at the bottom.

**Branch.** Tapping a new question adds it to the map and opens its source. The student can jump back to any branch.

**Rewrite.** After every third source: "Does your big question still fit?" `Keep it` or `Reword`; reworded questions keep the old line crossed out.

**Stop.** `I have enough` opens a three-line answer with chips linking to the supporting questions used.

**They shaped each other (the aha).** June: "Your small questions changed your big one, and your big one chose the small ones."

**The end.** The map and the answer. `Print` prints them.

**Swap notebooks (extra).** Partner guess.

## Content
- Each short source is written for the tool from two checked sources, credited at its foot; public domain images where checked.
- The notebook is saved in this browser's storage on this device only; `Clear notebook` removes it, and nothing is sent anywhere.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Any branch can be revisited; the big question can be reworded any time after the first rewrite check.
- Keyboard: Tab to question cards, source links, branch nodes (arrows move along the map), rewrite buttons and answer chips; Enter opens or picks.
- With Motion off branches appear without drawing.

## Look
- Accent `--brand` #4c5f1f notebook moss (header, branches, buttons); gold #f4c542 (the branch in focus, the big question); paper #f4f6ec; ink #161d06; muted #535849.
- Contrast (WCAG 2.1, computed): white on brand 7.09:1; brand on paper 6.49:1; ink on paper 15.87:1; muted on paper 6.73:1; ink on gold 10.65:1.
- Never color alone: the big question has a box and a star; visited branches carry a check.
- Different from this batch (e-bike blue, bookshelf walnut).

## Art
- People (illustrated): June, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Public domain images where checked (Library of Congress, Smithsonian open access), credited on each source (about 10).
- Local FLUX (`scripts/localart.py`): the notebook in a sketchbook style (1, 16:9), six question card pictures (6, 1:1).
- Drawn in code: hand-lettered branches and the map.
About 18 images.

## Voice
Two bank voices, each unique in this batch: `big-sister` as June; `smooth-narrator` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.question + ':' + state.source + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `pick`: "Tap a question card."
- how `follow`: "Tap a new question to follow it."
- how `fit`: "Tap Keep it or Reword."
- how `stop`: "Tap I have enough when you can answer."
- how `answer`: "Write three lines and link the questions you used."
- event, whole, they shaped each other.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: a source graph per big question, the notebook map in local storage, rewrite checks, the answer builder.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Follow | Stop after one source | The stop button opens after three sources. |
| Rewrite | Always keep | The end asks how the small questions changed the big one, even if kept. |
| Answer | Write without links | Each line links to a supporting question. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `pick`; `follow`.
2. `fit`.
3. `stop`; `answer`.
4. They shaped each other (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| AASL Explore and C3 D1.4.6-8 wording | data/standards/aasl-2018.txt | data/standards/c3-indicators.txt and data/modules.csv | yes |
| City pigeons are rock doves brought to North America by Europeans in the 1600s | Cornell Lab of Ornithology, All About Birds, "Rock Pigeon" | Smithsonian Magazine, history of the city pigeon | yes |
| Stamp subjects are recommended by the Citizens' Stamp Advisory Committee | U.S. Postal Service, "Stamp Selection Criteria" and the Citizens' Stamp Advisory Committee | Smithsonian National Postal Museum, stamp design process | yes |
| Questions develop and change during inquiry | C3 Framework (2013), Dimension 1, "Developing Questions and Planning Inquiries" | Kuhlthau (2004), "Seeking Meaning", Information Search Process | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s28, 2026-11-10): six questions with six or seven sources each is about 40 sources; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 source and map; at 680x425 map as a tab.
2. At least three sources are followed and the map grows branches. (AASL Explore)
3. The big question is checked at each rewrite, and a three-line answer links its supporting questions. (D1.4.6-8)
4. Every short source credits two checked sources.
5. The notebook stays on the device; `Clear notebook` removes it.
6. `Read` reads every source and note; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: branches appear at once; no network requests.

## Open questions
- Sourced facts behind each short page (default used: each page written from two checked sources credited at its foot; the full source list is built at Build).
