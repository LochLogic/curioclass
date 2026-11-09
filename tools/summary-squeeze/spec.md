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
- Driver: one student (tool.json `driver: "student"`). Every sentence is read on tap; summaries are read back by the browser's speech voice.
- Passages: "Beavers Remake a Valley" and "The Lighthouse Keeper's Log" (informational, written for Curio Class from sourced facts); fables "The Fox and the Crow" and "The North Wind and the Sun" (Aesop, V. S. Vernon Jones translation, 1912, public domain). tool.json `modes: ["Articles", "Fables", "Beat my squeeze"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the three squeezes side by side.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.6.2 (central idea, details) | Write a 50-word summary; the gauge lights the key details it carries | the gauge with lit details | 2 |
| RI.6.2 (objective summary) | Opinion and judgment words light as leaks and must come out | leak marks | 3 |
| RI.6.2 | Squeeze to 25 and 10; the 10-word summary must carry the central idea | three summaries side by side | 4 |
| RL.6.2 | Fable: the 10-word plot summary fails the gauge; rewrite as the theme and pick the details that convey it | the theme line with linked details | 5 |

## Screens and modes
Header (kit): title "Summary Squeeze"; `Articles`, `Fables`, `Side by side`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A big iron press in a print shop, a passage on the press bed and a gauge reading "Budget: 50 words", and Gus, an old printer with ink on his apron. First hint: "Tap the passage to hear it." The first tap reads the title; the welcome is queued after it (`welcomeAfter: true`).

**Read.** The passage (about 450 words) in numbered sentences; tap to hear.

**Write.** The press box: the student types a summary; a word counter fills like a pressure gauge and turns the box frame dashed when over budget (the Squeeze button stays active and says "Over by {6} words").

**Squeeze.** The detail gauge lists the passage's 6 key details (in data, with word families). A detail lights when the summary has one of its word families; when the match is only partial, the tool asks the student ("You wrote 'dams'. Does that cover 'build barriers of sticks and mud across streams'? Yes or No") and records the answer. The central idea has its own light. Opinion leaks: a list of 60 judgment words and phrases; each found one is marked with "That's your opinion. Does the passage say it?"

**Budgets.** 50, then 25, then 10. Each level shows which details the previous summary kept. At 10, the central idea light must be on; details may go out.

**Fables.** At 10 words, a plot summary ("The fox tricks the crow and gets the cheese") lights "plot" but not "theme"; the gauge asks "What do these events add up to?" The student writes a theme line (frames offered: "When you ___, ___."); the theme light uses key word families ("flattery", "praise", "trust", "pride"), and the student links two details that convey it.

**Side by side.** Three squeezes in columns, details kept per word shown as a number. Beat my squeeze replays a passage to raise that number.

At 1366x768 the passage and press fit side by side; at 680x425 the passage folds above the press.

## Content
Written for Curio Class from sourced facts:
- Beavers Remake a Valley: beavers build dams of sticks and mud that slow streams and make ponds; ponds and wetlands hold water, raise the water table and give homes to fish, frogs, birds and insects; beavers are called ecosystem engineers; some ranchers and land managers now use beaver dams or human-made copies to restore streams. Central idea: by building dams, beavers change a whole valley's water and life.
- The Lighthouse Keeper's Log: a keeper's day (trimming the wick, winding the clockwork that turned the lens, logging weather), from National Park Service and Coast Guard history facts. Central idea: keeping the light was steady, careful daily work.
- Fables: "The Fox and the Crow" and "The North Wind and the Sun" from Aesop's Fables, translated by V. S. Vernon Jones (1912), Project Gutenberg eBook #11339; the printed morals are hidden until the student writes their theme.

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
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: word counter, detail word families with confirm, leak list, budget levels, theme check.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Details | List keywords | Under 50 words, keywords light details, but the 10-word level needs the central idea's word families in a sentence with a verb. |
| Partial matches | Always answer Yes | The answers print with the summary, so a teacher sees them; they don't change the central idea light. |
| Leaks | Hide opinions in new words | The list has 60 words and phrases; others pass, which is acceptable for a practice tool. |
| Fables | Write the plot again | The theme light needs theme word families and two linked details. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the passage: title, `welcome` (queued, first time).
2. Sentences: `sentence` (whole). Squeeze: `over` or `partial` and `leak` as they fire, then `squeezed`.
3. Fables at 10: `plotOnly` if no theme.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.6.2 and RL.6.2 wording | thecorestandards.org, Grade 6 | CCSS ELA 2010 PDF | yes |
| Beaver dams slow water, create ponds and wetlands, raise the water table and support many species; beavers are ecosystem engineers | US Fish and Wildlife Service, beavers | National Park Service, beavers as ecosystem engineers | yes |
| Beaver dam analogs are used to restore streams | USDA Natural Resources Conservation Service, beaver dam analogs | US Forest Service, beaver-related restoration | yes |
| Keepers trimmed wicks, wound clockwork that turned the lens, and kept logs | National Park Service, lighthouse keepers' duties | US Coast Guard History Office, lighthouse keepers | yes |
| "The Fox and the Crow" and "The North Wind and the Sun", V. S. Vernon Jones translation (1912), public domain | Project Gutenberg eBook #11339 (checked 2026-11-09) | Library of Congress, catalog record for the 1912 edition | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad b18, 2026-11-09): the Gutenberg file is the Vernon Jones translation and includes both fables; a sample 10-word theme sentence passes the theme check and a 10-word plot sentence fails it; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 passage and press fit; at 680x425 the passage folds above.
2. The detail gauge lights details with partial-match confirms. (RI.6.2)
3. Leaks are marked. (RI.6.2)
4. Budgets 50, 25 and 10 work; 10 needs the central idea. (RI.6.2)
5. Fables need a theme line and two linked details. (RL.6.2)
6. Side by side shows details kept per word; Beat my squeeze replays.
7. Print shows the three squeezes.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the press is still; no network requests.

## Open questions
- None for Cory.
