# Two Authors, One Event

## One idea
Two made-up newspapers report the same night a flood closed Main Street, with the same facts, and the student lays the front pages side by side, strings each shared fact to its partner, and finds where the papers part ways: a fact with no partner glows as left out, an emphasis layer shows which facts each paper put first and which it buried, and a word layer swaps loaded words for neutral ones ("the city's failure" against "a rare storm"); then they write a neutral headline and lede from only the facts both share, so they learn that authors shape the same information to lead readers to different conclusions.

## Not like
- history-or-fiction (7, spec, this batch): fiction checked against primary sources. Here two nonfiction reports of the same facts.
- word-thermometer (6, spec): connotation of single words on a scale. Here loaded words inside news reports.
- fact-check-desk (8, concept): texts that disagree on facts. Here texts that share facts and differ in shaping.
- eyewitness-vs-reporter (spec): firsthand and secondhand accounts. Here two secondhand reports with different aims.
- memoir-and-biography (6-8, spec): how a person is presented. Here how an event is presented.

## Who and how
- Grade 7, ELA, module "Comparing Authors" (Reading Informational Text). Standards: RI.7.9, RI.7.4, RI.7.6.
- Driver: one student; class mode is a "which paper wrote this?" quiz (tool.json `driver: "student"`). Every paragraph is read on tap.
- Level 1: the Riverside Gazette and the Valley Business Weekly on the Main Street flood (written for Curio Class, labeled made up). Level 2: two September 1909 newspaper reports of Robert Peary's claim to have reached the North Pole, from Chronicling America (public domain). tool.json `modes: ["The flood", "1909 papers", "Which paper?"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.
- Nothing is saved; `Print` prints the strung pages and the neutral version.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.7.9 (emphasis, omission) | String shared facts; unpartnered facts glow as left out; the emphasis layer shows where each fact sits | strings, glowing facts, position marks (headline, first paragraph, last paragraph) | 2 |
| RI.7.4 | Tap loaded words and choose their neutral swap; say how the tone changes | the word layer with swaps | 3 |
| RI.7.6 | Name what each author wants readers to think or do and how each sets its view apart from others ("Critics say...") | the point-of-view panel | 4 |
| RI.7.9 | Write a neutral headline and lede using only shared facts | the neutral version beside both originals | 5 |

## Screens and modes
Header (kit): title "Two Authors, One Event"; `Pages`, `Layers`, `Point of view`, `Neutral`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A newsroom wall with two front pages pinned side by side and a spool of red string; Ms. Delacroix, the town's retired newspaper editor, at a desk. First hint: "Tap a headline to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Pages.** The Riverside Gazette (about 300 words): "City Failed to Fix Drains Before Main Street Flood". The Valley Business Weekly (about 300 words): "Rare Storm Closes Main Street; Shops Reopen Friday". Shared facts: 3.2 inches of rain in two hours; Main Street closed from 9 p.m. to 6 a.m.; 14 shops had water inside; no one was hurt; the city had delayed a drain project in 2023; the mayor's quote. Each paper leaves some out.

**Strings.** The student drags a string from a fact in one paper to its partner in the other. Facts with no partner glow as "left out by the other paper".

**Layers.** Emphasis: each fact shows a position mark (headline, first paragraph, middle, last paragraph); a bar compares where each paper put the delayed drain project. Words: loaded words are tappable after the student finds them (keyed: "failed", "neglected", "rare", "freak", "bounced back", "residents fumed"); each offers a neutral swap, and the paragraph rereads with it.

**Point of view.** Two questions per paper with choices and a line: "What does this author want readers to think?" and "Where does the author set their view apart from others?" (the Weekly's "Some residents blame the city, but..."; the Gazette's "City officials say the storm was unusual; records show...").

**Neutral.** The student writes a headline and a two-sentence lede using only strung facts. Any word on the loaded list or any unstrung fact is flagged.

**1909 papers.** Two front-page reports from early September 1909 of Peary's message that he had reached the North Pole, after Frederick Cook had claimed it days before; same steps, with keyed loaded words and position marks.

**Which paper?** Sentences from both papers; the class taps which paper wrote each.

At 1366x768 both pages fit side by side; at 680x425 one page shows at a time with a toggle.

## Content
- The two flood papers written for Curio Class, labeled "made-up newspapers" on screen, with keyed facts, positions, loaded words and swaps.
- The 1909 pair from Chronicling America (Library of Congress), public domain, transcribed from the page scans with keyed facts.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Strings can be removed by tapping them.
- With Motion off strings appear without stretching.

## Look
- Accent `--brand` #3f4a54 newsprint slate (header, page frames, mastheads); gold #f4c542 (strings, glowing left-out facts); paper #f4f5f6; ink #14181c; muted #575e66. Scene: a small-town newsroom wall.
- Contrast (WCAG 2.1, computed): white on brand 9.06:1; brand on paper 8.30:1; ink on paper 16.34:1; muted on paper 6.02:1; ink on gold 10.97:1.
- Never color alone: left-out facts carry a label; loaded words are underlined with a dotted line and a label after they are found.
- Different from this batch (magazine plum, ember brown, leaf green, frost blue).

## Art
- People art goes to Gemini: Ms. Delacroix (a Louisiana Creole woman in her seventies with reading glasses and a cardigan), 3 poses; "illustrated retired newspaper editor <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): newsroom wall (1); the same flooded Main Street photographed two ways (2: one dramatic at night with dark water, one calm next morning with a shopkeeper's broom and no faces).
- 1909 page scans from Chronicling America (public domain).
About 6 images. Drawn in code: newspaper layouts, strings, layers.

## Voice
Bank voice `curious-librarian` as Ms. Delacroix (unique in this batch); the Gazette is read by `firm-captain` and the Weekly by `warm-teacher` (each unique in this batch). `Curio.voice` with `scope: () => state.level + ':' + state.view + ':' + state.fact`, `welcomeAfter: true`.
- how `welcome`: "Same night, same facts, two papers. String what they share, then find where they part ways."
- event, whole, `para`: the tapped paragraph, in that paper's voice.
- event `leftOut`: "{The Weekly} left this out."
- event `swap`: the paragraph reread with the neutral word.
- event `flagged`: "{Failed} is a loaded word. Is it in both papers' facts?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: fact strings between two pages, position marks, keyed loaded words with swaps, the point-of-view panel, the neutral checker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Strings | String everything to everything | Strings between non-matching facts show "These aren't the same fact." |
| Loaded words | Tap every word | Only keyed loaded words open swaps; other taps just read the word. |
| Neutral | Copy one paper's headline | Loaded words and unstrung facts are flagged. |
| Point of view | Pick any choice | Each choice needs a line quoting the paper. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a headline: headline, `welcome` (queued, first time).
2. Paragraphs: `para` (whole).
3. Strings: `leftOut` as it fires.
4. Words: `swap`.
5. Neutral: `flagged` as it fires.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.7.4, RI.7.6, RI.7.9 wording | thecorestandards.org, Reading Informational Text Grade 7 | CCSS ELA 2010 PDF | yes |
| In early September 1909 Frederick Cook and then Robert Peary each claimed to have reached the North Pole, and newspapers took sides | Library of Congress, Chronicling America search for "peary cook north pole", September 1-10, 1909 (checked 2026-11-09; front pages from the Daily Kennebec Journal and the Daily Missoulian, September 7 to 9) | National Archives or Smithsonian, the Peary and Cook controversy | yes |
| Loaded language, emphasis and omission shape how readers understand news | News Literacy Project, bias and loaded language | Purdue OWL, analyzing rhetoric and diction | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): the flood papers are made up and labeled so on screen.

Checks run (Python, scratchpad b21, 2026-11-09): the Chronicling America search returns 1909 front pages from at least two different papers in the date range; every shared fact in the flood key appears in both papers and every left-out fact in exactly one; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 both pages fit; at 680x425 one page at a time with a toggle.
2. Strings join shared facts; left-out facts glow; position marks show emphasis. (RI.7.9)
3. Loaded words swap and reread. (RI.7.4)
4. The point-of-view panel takes choices with quoting lines. (RI.7.6)
5. The neutral version flags loaded words and unstrung facts. (RI.7.9)
6. The 1909 level works with its keyed pair.
7. Which paper? quiz and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: strings appear without stretching; no network requests.

## Open questions
- Which two 1909 front pages to transcribe for level 2 (default used: the Daily Kennebec Journal and the Daily Missoulian, September 7, 1909; their text could not be read from here, so Build reads the scans first).
