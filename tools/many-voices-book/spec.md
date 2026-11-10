# Many Voices Book

## One idea
A big class book lies open on a rug, "Our Many Voices Book", with pages made by twelve classmates, all made up and labeled "illustration", and an empty page with the child's name tag; Ms. Rivera, the school librarian (made up), says "Read the book, then make your page," and each page is spoken by its maker, a greeting from home in the family's own language with its sound, a favorite food and a game: "Salaam! My family eats mansaf on Fridays. I play hopscotch."; then the child makes their own page, drawing or stamping a favorite food and game and picking or recording a greeting, while a spoken line says the drawing and any recording stay on this device and never leave it; next the child drags a "same" string from their page to every page that shares something with theirs ("We both play tag!") and a "different" star to a page they want to learn about; then three book characters each want a different page order, by greeting, by food, or by birthday, and the child finds an order every character agrees with, and every page gets a turn on the cover; at the end every page has a "same" with someone and a "different" worth asking about, and the book is better with all of them in it, so a child in kindergarten to grade 2 learns to make one class book together where everyone is in.

## Not like
- wonder-wall (Grades K-2, live): sorting questions. Here making a book together.
- library-adventure (Grades K-2, live): finding books. Here making one.
- windows-and-mirrors-shelf (Grades 3-5, concept): choosing books. Here pages from classmates.
- parachute-teamwork (Grades K-2, spec): moving together. Here a book together.

## Who and how
- Grades K-2, Library, module "Many Voices Book". Standards: AASL Include (Shared Foundation II), AASL Collaborate (Shared Foundation III), AASL National School Library Standards (2018).
- Format: studio. Driver: one child alone (tool.json `driver: "student"`). Every word is spoken. Controls 60 px or more.
- Twelve pages, a page maker with stamps and drawing, greeting choices or a recording, same strings and different stars, the three-character order puzzle, cover turns. Extra: Class book (on one shared device, each child adds a page and the class picks the order; first names only, no face photos). tool.json `modes: ["My page", "Class book"]`, `minutes: "15-25"`, `grades_label: "Grades K-2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| AASL Include | Hear each page; link a same and a different | strings and stars across the book | 2 |
| AASL Collaborate | Find an order all three characters agree with | the book in order; cover turns | 3 |

## Screens and modes
Header (kit): title "Many Voices Book"; `My page`, `Class book`; `Read`, `Motion`, `Sound`, `Print`. Controls 60 px or more.

**On load and first tap.** The rug, the open book, the empty page with a name tag, and Ms. Rivera on a low chair. The welcome is queued (`welcomeAfter: true`): "Read the book, then make your page. Tap the book to turn the page." First hint: "Tap the book."

**Read (focus: the book).** At 1366x768 the book spreads across the view with the page maker's face in a corner; at 680x425 one page shows at a time. Each page plays its greeting and lines; tapping any picture speaks it.

**Make.** Stamps for foods and games, a crayon tool, and greeting cards to pick or `Record my greeting` (asks for the microphone only on that tap). A spoken line: "Your page stays on this device and never leaves it."

**Link.** Drag a `Same` string from your page to each page that shares something; drag a `Different` star to one page you want to learn about. Each link speaks what is shared.

**Order.** Three characters each show their rule; the child arranges pages until all three nod (for example, greetings grouped, foods side by side, with birthdays breaking ties); a cover rotation shows every page.

**Everyone's in (the aha).** Ms. Rivera: "Every page has a same and a different. Our book needs all of them."

**The end.** The finished book. `Print` prints the child's page and the strings.

**Class book (extra).** Real class pages.

## Content
- Twelve made-up children from many backgrounds and family shapes; greetings in their family languages with spelling shown, recorded by native speakers.
- Drawings and recordings are saved in this browser's storage on this device only; `Clear my page` removes them, and nothing is sent anywhere.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pages can be reread any time; the child's page can be changed until `Done`.
- Keyboard: Tab to pages, stamps, the crayon, greeting cards, record, strings and stars, and page slots (arrows move pages); Enter picks.
- With Motion off pages change without turning.

## Look
- Accent `--brand` #9a2a6e crayon magenta (header, the book's spine, buttons); gold #f4c542 (the page in focus, same strings); paper #fbeff6; ink #2a0a1d; muted #5c4b55.
- Contrast (WCAG 2.1, computed): white on brand 7.17:1; brand on paper 6.41:1; ink on paper 16.19:1; muted on paper 7.24:1; ink on gold 11.13:1.
- Never color alone: same strings carry an equals mark; different stars are star shapes.
- Different from this batch (late-night indigo, clipboard teal, ski-lift red, pitch-fair green).

## Art
- People (illustrated): twelve page makers and Ms. Rivera, labeled "illustration", drawn as if by many hands in a crayon-and-collage style (Gemini, `people: true`, 13; cutout yes).
- Local FLUX (`scripts/localart.py`): the rug and book (1, 16:9), twelve food and game pictures (24, 1:1).
- Drawn in code: the page maker, stamps, strings and stars.
About 38 images.

## Voice
Two bank voices, each unique in this batch: `warm-teacher` as Ms. Rivera; `bright-teacher` as page lines and hints, with greetings recorded by native speakers. `Curio.voice` with `scope: () => state.mode + ':' + state.page + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `turn`: "Tap the book to turn the page."
- how `make`: "Tap a stamp, then tap your page."
- how `greet`: "Tap a greeting or Record my greeting."
- how `link`: "Drag a Same string to a page."
- how `order`: "Drag pages until all three friends nod."
- event, whole, everyone's in.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the book reader, the page maker with local storage, links, the three-rule order checker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Read | Skip pages | Links open after every page is heard. |
| Link | One string only | Each page with a match needs its string. |
| Order | Any order | All three characters must nod. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `turn`.
2. `make`; `greet`.
3. `link`; `order`.
4. Everyone's in (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| AASL Include and Collaborate wording | data/standards/aasl-2018.txt | data/modules.csv module line | yes |
| Books that reflect many cultures help children see themselves and others | Bishop (1990), "Mirrors, Windows, and Sliding Glass Doors", Perspectives | American Library Association, "Diverse Collections" interpretation of the Library Bill of Rights | yes |
| "Salaam" is an Arabic greeting; mansaf is a Jordanian national dish | Oxford Reference, Arabic greetings | Jordan Tourism Board, national dishes | yes |
Backed twice: 3. Cut: 0.

Sensitivity: greetings, foods and families from many cultures; a fresh-agent sensitivity review checks each page before Live.

Checks run (Python, scratchpad s27, 2026-11-10): twelve pages plus the child's make thirteen, and a cover rotation of thirteen gives every page a turn; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the open book; at 680x425 one page at a time.
2. Every page is heard and linked with a same or a different. (AASL Include)
3. An order is found that all three characters agree with. (AASL Collaborate)
4. Drawings and recordings stay on the device; `Clear my page` removes them; the microphone is asked for only on Record.
5. Every word is spoken; greetings are native-speaker recordings.
6. `Read` reads every page; every control is 60 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: pages change without turning; no network requests.

## Open questions
- Greeting recordings in each family language (default used: native speakers recorded with consent at the Art and voice step; the bank voice reads the rest).
