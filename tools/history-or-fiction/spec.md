# History or Fiction?

## One idea
The student investigates a short historical fiction story, written for Curio Class, about a messenger boy running through the Great Chicago Fire of October 1871, pinning each detail to a case board and checking it against primary sources in an evidence drawer (newspaper reports, a city map, photographs of the ruins), stamping it Documented, Altered or Invented and then working out why the author changed it; the twist is the famous cow that kicked over a lantern, which the drawer shows was a newspaper story a reporter later said was made up, so they learn how fiction writers use and bend history, and why.

## Not like
- memoir-and-biography (6-8, spec): two nonfiction tellings of one event. Here fiction checked against history.
- two-authors-one-event (7, spec, this batch): two articles shaping the same facts. Here a story against primary sources.
- eyewitness-vs-reporter (spec): firsthand and secondhand accounts. Here fiction's changes to history.
- satire-decoder (11, concept): what is said versus meant. Here what happened versus what was invented.
- fact-fusion (5, spec): merging sources into one table. Here sources as clues against a story.

## Who and how
- Grade 7, ELA, module "Fiction and History" (Reading Literature). Standard: RL.7.9.
- Driver: one student (tool.json `driver: "student"`). Every story page and source is read on tap.
- Case: "The Runner on Clark Street" (about 1,500 words in five short pages, written for Curio Class). tool.json `modes: ["The case", "Author's note"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.
- Content note on the first screen: "About 300 people died in the fire. The story tells this plainly." Nothing is saved; `Print` prints the case board and the author's note.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.7.9 (compare portrayal with historical accounts) | Pin a story detail and find sources in the drawer that confirm or contradict it | the detail pinned with source strings | 2 |
| RL.7.9 (how the author used history) | Stamp each detail Documented, Altered or Invented | the stamp on each pin | 3 |
| RL.7.9 (why the author altered history) | For each Altered or Invented detail, pick or write the reason | the reason card on each pin | 4 |
| RL.7.9 | The cow twist: decide whether the novelist should keep the legend, and write an author's note telling readers what is real | the author's note | 5 |

## Screens and modes
Header (kit): title "History or Fiction?"; `Story`, `Case board`, `Drawer`, `Author's note`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A detective's office with a cork case board, a desk with a five-page story and a wooden evidence drawer; Detective June Albright, in a 1940s hat, leans on the desk. First hint: "Tap the story to hear page one." The first tap reads the page title; the welcome is queued after it (`welcomeAfter: true`).

**Story.** Five pages. Tom Quinn, 12, runs messages for a telegraph office. Keyed details include: the fire starts in the O'Leary barn on DeKoven Street on the night of October 8 (documented); a hot, dry wind blows from the southwest (documented); Tom sees Mrs. O'Leary's cow kick over a lantern (legend, see the twist); Tom meets Mayor Mason on a bridge and carries his telegram (invented meeting; the mayor's telegrams for help are documented); the courthouse bell falls (documented); the fire's two days pass in what the story tells as one long night (altered: time compressed); Tom's family loses their home (invented characters, but about 100,000 people lost homes, documented).

**Drawer.** Primary and expert sources, each with a short excerpt or picture and its source line:
- Photographs of the ruins (Library of Congress 2004682763, "Ruins after the great fire of Oct. 1871, Chicago"; 2022886701, ruins of the court house).
- A city map of the burned district.
- A newspaper report of the fire's spread and the wind.
- A note on the mayor's telegrams asking other cities for help.
- The cow card: the cow-and-lantern story first appeared in newspapers; the reporter Michael Ahern later said it was made up, and another reporter claimed he wrote it; in 1997 the Chicago City Council passed a resolution clearing Mrs. O'Leary and her cow.
- A history museum card on how the O'Leary family, Irish immigrants, were blamed, and how anti-Irish prejudice made the story spread.
The student drags a string from a pin to each source that bears on it.

**Stamps and reasons.** Documented, Altered (a real fact changed: time, place, who was there) or Invented (a character or conversation that never happened but could have). Reasons for Altered or Invented: to give readers someone to follow, to compress time, to show what many people felt, to make a scene more dramatic, or the student's own. A stamp that contradicts the keyed sources asks "What does the drawer say?"

**The twist.** When the cow pin is stamped, Detective Albright asks: "The story uses the legend. Should the author keep it?" The student picks Keep (and tell readers it's a legend), Change (Tom hears the rumor instead of seeing it) or Cut, with a reason, and then writes a short author's note (frames: "Real:", "Changed:", "Invented:").

At 1366x768 the story and board fit side by side; at 680x425 the drawer is a tab.

## Content
- "The Runner on Clark Street", written for Curio Class, with keyed details and their stamps.
- Source excerpts and summaries from the Sources table; two Library of Congress photographs (public domain, no known restrictions as listed).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Strings and stamps can change any time.
- With Motion off strings appear without stretching.

## Look
- Accent `--brand` #7a3b12 ember brown (header, board frame, stamps); gold #f4c542 (strings, the twist pin); paper #fbf5ef; ink #2a1206; muted #66574b. Scene: a lamplit detective's office.
- Contrast (WCAG 2.1, computed): white on brand 8.53:1; brand on paper 7.88:1; ink on paper 16.34:1; muted on paper 6.41:1; ink on gold 10.87:1.
- Never color alone: stamps carry words; strings are labeled with the source name.
- Different from this batch (magazine plum, leaf green, frost blue, newsprint slate).

## Art
- Public domain: Library of Congress photographs 2004682763 and 2022886701 (fire ruins).
- People art goes to Gemini: Detective June Albright (a Black woman in her forties in a 1940s hat and coat), 3 poses; Tom Quinn (an Irish American boy about 12 in 1871 clothes, running, no fire behind him), 2 poses; "illustrated <description> <pose>, warm gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): detective's office with a case board (1); an 1871 Chicago street at dusk with an orange glow far off, no people (1).
About 9 images. Drawn in code: board, strings, stamps, map.

## Voice
Bank voice `knowing-guide` as Detective Albright (unique in this batch); the story is read by `gentle-storyteller` and sources by `news-reader` (each unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.pin`, `welcomeAfter: true`.
- how `welcome`: "Every line of this story is a suspect. Pin a detail, check the drawer, then stamp it."
- event, whole, `page`: the story page.
- event, whole, `source`: the source excerpt.
- event `contradicts`: "What does the drawer say?"
- event `twist`: "The story uses the legend. Should the author keep it?"
- how `noteHow`: "Tell readers what's real, what's changed, and what's invented."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: pinned details, source strings, keyed stamps and reasons, the author's note frames.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Stamps | Stamp everything Documented | Keyed contradictions ask what the drawer says, and the note needs at least one Changed and one Invented line. |
| Strings | String every source to every pin | Strings to unrelated sources show "Doesn't bear on this." |
| Reasons | Pick the same reason for all | Each reason is checked against the keyed kind of change (time compressed needs "to compress time" or the student's own words). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the story: page title, `welcome` (queued, first time).
2. Pages and sources: `page`, `source` (whole) on tap.
3. Stamps: `contradicts` as it fires.
4. The cow pin: `twist`; then `noteHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.7.9 wording | thecorestandards.org, Reading Literature Grade 7 | CCSS ELA 2010 PDF | yes |
| The fire began in the O'Leary barn on DeKoven Street on October 8, 1871; about 300 died; more than 17,000 buildings burned; about 100,000 lost homes; strong southwest winds and drought spread it | Chicago History Museum and Northwestern University, "The Great Chicago Fire and the Web of Memory" | Wikipedia, Great Chicago Fire, with its cited histories (checked 2026-11-09) | yes |
| The cow story was a newspaper invention; Michael Ahern later said it was made up, and another reporter claimed authorship | "The Great Chicago Fire and the Web of Memory", the O'Leary legend (checked 2026-11-09) | Wikipedia, Great Chicago Fire, with its cited histories (checked 2026-11-09) | yes |
| The Chicago City Council cleared Mrs. O'Leary and her cow in 1997 | "The Great Chicago Fire and the Web of Memory" (checked 2026-11-09) | Wikipedia, Great Chicago Fire, citing historian Richard Bales's research (checked 2026-11-09) | yes |
| Library of Congress photographs 2004682763 and 2022886701 show the ruins, 1871 | loc.gov item pages (checked 2026-11-09) | Library of Congress search results for "chicago fire 1871 ruins" | yes |
Backed twice: 5. Cut: 1 (the year of Ahern's admission: one source says 1893, another says the fortieth anniversary in 1911; the tool says "later").

Sensitivity note: deaths are told plainly with a content note; the O'Leary family's blame is shown as prejudice against Irish immigrants, told with care; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b21, 2026-11-09): every keyed Documented detail has at least one source string in the key; the story has at least two Altered and two Invented details; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 story and board fit; at 680x425 the drawer is a tab.
2. Details pin and string to sources. (RL.7.9)
3. Stamps check against keyed sources. (RL.7.9)
4. Altered and Invented stamps take reasons. (RL.7.9)
5. The cow twist takes a choice and the author's note needs Real, Changed and Invented lines. (RL.7.9)
6. The content note shows on the first screen.
7. Print shows the board and author's note.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: strings appear without stretching; no network requests.

## Open questions
- None for Cory.
