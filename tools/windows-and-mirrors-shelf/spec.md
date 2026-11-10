# Windows and Mirrors Shelf

## One idea
An empty bookshelf has a mirror at one end and a window at the other, and a line at the top names where the idea comes from, educator Rudine Sims Bishop, who in 1990 described books as windows, mirrors and sliding glass doors; Mr. Haddad, the school librarian (made up, labeled "illustration"), asks the child to pick a few "about me" cards (city, small town or farm; big family or small; languages at home; things you love), while a spoken line says the answers stay on this device and never leave it; then blurbs of made-up books arrive one at a time, a graphic novel about a girl in a Navajo Nation town learning to herd sheep with her grandmother, a mystery set in a busy Lagos market, a sports story about a boy who uses a wheelchair and plays basketball, and seven more, and the child drags each to the mirror end (a life like mine) or the window end (a life different from mine); next three illustrated readers sort the same ten blurbs, and their shelves come out different, so one book is a mirror for one reader and a window for another; the child looks at their own shelf to notice what it is missing, then builds a stack of five with both mirrors and windows across at least three genres and two formats, and writes one line on what they hope to find in a window book; at the end the child sees that a good reading life has both kinds of books, and that their own shelf shows which they need more of, so a student in grades 3 to 5 learns to read widely, both books like their life and books about other lives.

## Not like
- many-voices-book (Grades K-2, spec): a class book. Here choosing what to read.
- library-adventure (Grades K-2, live): finding books in a library. Here balancing a reading life.
- rabbit-hole-notebook (Grades 6-8, concept): research questions. Here reading for self and others.
- e-bike-buyer (Grades 6-8, spec): comparing sources to buy. Here comparing shelves.

## Who and how
- Grades 3-5, Library, module "Windows and Mirrors Shelf". Standards: AASL Include (Shared Foundation II), AASL Explore (Shared Foundation V), AASL National School Library Standards (2018).
- Format: sort. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every blurb and card. Controls 48 px or more.
- Six about-me cards, ten blurbs, three readers' shelves, a stack of five with a genre and format check, one line. Extra: Class shelf (the class sorts one blurb and sees the split, no names). tool.json `modes: ["My shelf", "Class shelf"]`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| AASL Include | Sort blurbs by closeness to your life; compare three readers | one book on two different ends | 2 |
| AASL Explore | Build a five-book stack across genres and formats; name a hope | the stack check | 3 |

## Screens and modes
Header (kit): title "Windows and Mirrors Shelf"; `My shelf`, `Class shelf`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The empty shelf with a mirror and a window, the Bishop line, and Mr. Haddad holding a stack. The welcome is queued (`welcomeAfter: true`): "First, tell the shelf about you. Tap an about-me card." First hint: "Tap an about-me card."

**About me.** Six cards with simple choices; a spoken line about storage.

**Sort (focus: the shelf).** At 1366x768 the shelf runs across the view with the blurb card below; at 680x425 the blurb is a sheet. Each blurb has a cover, a genre and a format; the child drags it to an end, or to the middle for "a bit of both".

**Three readers.** Three readers' shelves appear under the child's; the same book is outlined on each, sitting at different ends.

**Missing.** The shelf counts mirrors and windows and lists genres and formats not yet chosen.

**Stack.** The child picks five; the stack checks for both kinds, three genres and two formats, then asks for one line.

**Both kinds (the aha).** Mr. Haddad: "The same book was a mirror for Ava and a window for you. A good shelf has both."

**The end.** The shelf, the stack and the line. `Print` prints a reading list.

**Class shelf (extra).** Class split.

## Content
- All books are made up; blurbs are written with care, with real places and peoples named respectfully, and every cover is labeled "made-up book".
- About-me answers and the stack are saved in this browser's storage on this device only; `Clear my shelf` removes them, and nothing is sent anywhere.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Books can move until `Done sorting`; the stack can change until `Print`.
- Keyboard: Tab to cards, blurbs, the two ends and the middle, readers' shelves and stack slots; Enter places.
- With Motion off books jump to the shelf.

## Look
- Accent `--brand` #6b4426 bookshelf walnut (header, shelf, buttons); gold #f4c542 (the blurb in hand, the window frame); paper #f8f2ec; ink #24140a; muted #594e46.
- Contrast (WCAG 2.1, computed): white on brand 8.47:1; brand on paper 7.62:1; ink on paper 16.03:1; muted on paper 7.26:1; ink on gold 10.95:1.
- Never color alone: ends carry a mirror or window icon and words; genres carry labels.
- Different from this batch (e-bike blue, notebook moss).

## Art
- People (illustrated): Mr. Haddad and three readers, labeled "illustration" (Gemini, `people: true`, 4; cutout yes).
- Local FLUX (`scripts/localart.py`): ten covers for made-up books, each in its own style (10, 2:3), the shelf (1, 16:9).
- Drawn in code: about-me cards, the counts and the stack check.
About 15 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as Mr. Haddad; `warm-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.book + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `about`: "Tap an about-me card."
- how `sort`: "Drag the book to the mirror or the window."
- how `readers`: "Tap a reader's shelf to compare."
- how `stack`: "Pick five books for your stack."
- how `hope`: "Write one line about a window book."
- event, whole, both kinds.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: about-me cards in local storage, the shelf sorter, three fixed reader shelves, the stack check.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Put everything on one end | The shelf asks about each book with the about-me cards in view. |
| Readers | Skip them | The stack opens after the three readers. |
| Stack | Five of one genre | The check needs three genres, two formats and both kinds. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `about`; `sort`.
2. `readers`.
3. `stack`; `hope`.
4. Both kinds (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| AASL Include and Explore wording | data/standards/aasl-2018.txt | data/modules.csv module line | yes |
| Books as windows, mirrors and sliding glass doors (Bishop, 1990) | Bishop (1990), "Mirrors, Windows, and Sliding Glass Doors", Perspectives: Choosing and Using Books for the Classroom 6(3) | Reading Is Fundamental, "Mirrors, Windows, and Sliding Glass Doors" (with the original essay) | yes |
| Navajo Nation families herd sheep, often with grandparents | Navajo Nation Museum and Diné cultural resources on sheep herding | Smithsonian National Museum of the American Indian, "Navajo-Churro sheep" | yes |
Backed twice: 3. Cut: 0.

Sensitivity: cultural portrayals in the blurbs; a fresh-agent sensitivity review checks each blurb before Live.

Checks run (Python, scratchpad s28, 2026-11-10): ten blurbs across five genres and three formats allow a stack of five meeting three genres and two formats; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 shelf and card; at 680x425 card as a sheet.
2. Ten blurbs are sorted and the three readers compared. (AASL Include)
3. A balanced stack of five and a line are made. (AASL Explore)
4. About-me answers stay on the device; `Clear my shelf` removes them.
5. Every book is labeled made up; the Bishop source is named on screen.
6. `Read` reads every blurb and card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: books jump; no network requests.

## Open questions
None.
