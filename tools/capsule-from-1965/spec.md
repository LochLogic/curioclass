# Capsule From 1965

## One idea
A dented metal time capsule comes out of the ground at Maple Hill School, buried by a first-grade class in 1965, and the child picks up four things inside (a class photo, a letter, a lunch ticket, a toy catalog page) and uses a magnifier to find who made each one, when and where from clues printed on the thing itself, asks their own questions from a question jar (some answered by another object), and ends by laying the 1965 kids' wishes and favorite toys beside their own, so a first grader learns that old objects are sources that can tell us about people we can never meet.

## Not like
- then-and-now-flip (K, spec): sorting pictures of the same thing as then or now, and Grandma's day told aloud. Here four objects are read as sources for maker, date and place, and the child asks the questions.
- the-last-carousel-ride (1, concept, next batch): comparing two people's accounts of one event. Here one class's objects from one year.
- symbol-spotter (K, spec): national symbols on everyday things. Here a school's own past.
- community-helpers-village, market-day, compass-rose-quest, teddy-bear-makers (1, this batch): helpers, trading, maps and making. Here reading old sources.

## Who and how
- Grade 1, Social Studies (History), module "Old Objects as Sources". Standards: D2.His.4.K-2 (compare perspectives of people in the past to those of people in the present), D2.His.10.K-2 (compare different accounts or sources), D2.His.11.K-2 (identify the maker, date and place of origin for a historical source from information within the source itself), D2.His.12.K-2 (generate questions about a particular historical source as it relates to a particular historical event or development).
- Driver: teacher on the projector with the class calling out what they spot, or one child alone; every clue, question and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Three parts: Open the capsule (four objects), Question jar, Then and me. tool.json `modes: ["Capsule", "Question jar", "Then and me"]`, `minutes: "15-25"`, `grades_label: "Grade 1"`.
- The Then and me page is kept only while the page is open; `Print` prints it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.11.K-2 | Move the magnifier over each object and tap the clue that shows who made it, when and where | the object's Maker, Date and Place tags filling in | 2, 3 |
| D2.His.12.K-2 | Pick or build questions from the question jar about the objects | the child's question on a card, with "Find out" | 4 |
| D2.His.10.K-2 | Answer a question from one object by opening another (the catalog page tells what the photo's toy was) | the two objects side by side with the answer | 5 |
| D2.His.4.K-2 | Lay the 1965 kids' wishes and favorite toys beside the child's own picks | the Then and me page with "same" and "different" marks | 6 |

## Screens and modes
Header (kit): title "Capsule From 1965"; `Capsule`, `Question jar`, `Then and me`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** The new playground at Maple Hill School. A digger has just lifted a dented metal box out of the dirt. Principal Gomez stands beside it. The welcome is queued (`welcomeAfter: true`): "Look what the diggers found! A time capsule. A first-grade class buried it here in 1965. Tap the lid to open it." First hint: "Tap the lid to open it." The first tap opens the lid and cuts the welcome.

**Capsule (focus: the open box).** Four objects lie in the box. Tapping one lifts it to the table. At 1366x768 the object fills the center, the magnifier sits at its corner, and three empty tags (Maker, Date, Place, each with an icon: a pencil, a calendar, a house) are at the right. At 680x425 the tags sit under the object.
- The child drags the magnifier over the object. Under the lens, three spots on each object can be tapped. A right spot fills its tag with a ding: "The date! It's stamped right here." A spot that holds no clue says what it is ("That's just a smudge.").
- The four objects (all made for this tool, fictional):
  1. Class photo: maker = "Bright Photo Studio" printed on the cardboard frame; date = "May 1965" written in pen on the back (the child taps `Flip` to see the back); place = "Maple Hill School, Room 4" on the chalkboard behind the class.
  2. Letter: maker = signed "Your friend, Patty Ruiz, age 6"; date = "June 1, 1965" at the top; place = "Maple Hill School" on the letterhead.
  3. Lunch ticket: maker = "Maple Hill School Lunchroom" printed on it; date = "Week of March 8, 1965"; place = same school; price "25 cents" printed in the corner.
  4. Toy catalog page: maker = "Hartwell's Department Store"; date = "Christmas 1964" across the top; place = "Main Street, Maple Hill".
- When an object's three tags are full, it gets a gold check and goes on the shelf. After all four, Principal Gomez says: "You found who, when and where for every one. That makes them sources." The `Question jar` opens.

**Question jar (focus: the jar).** A glass jar with question slips. The child taps `Pick a question` to draw one, or `Make a question` to build one from three picture tiles: a question word (Who, What, Why, Where), an object, and a part of it (the toy, the price, the wish). Five slips are in the jar:
- "Why was lunch so cheap?"
- "What toy is the boy holding in the photo?"
- "What did Patty wish for?"
- "Who took the class photo?"
- "Where was the store?"
Each slip shows `Find out`. Some answers come from the same object; two need a second object:
- "What toy is the boy holding?" opens the photo and the catalog page side by side: the same rocking horse is on the page, "Rocking horse, 4 dollars 98 cents".
- "Why was lunch so cheap?" opens the ticket and a price card: "In 1965, 25 cents bought much more than it does now. Prices go up over time. 25 cents then is like about 2 dollars and 50 cents today. Also, since 1946 a law has helped pay for school lunches."
A built question with no answer in the capsule gets: "Good question! The capsule doesn't say. Who could we ask?" and a picture of a grandparent, a library and the school office.

**Then and me (focus: two columns).** Left: Patty's letter wishes and the class's three favorite toys from the catalog. Right: empty slots. Patty's wishes (read aloud): "I hope people go to the Moon. I hope I get a horse. I hope my school gets a swimming pool." Toys: a rocking horse, a yo-yo, a jump rope.
- The child fills the right side by picking pictures: three wishes (from twelve picture choices, such as "visit space", "a pet", "a new playground", "be a doctor") and three favorite toys (from twelve, including a yo-yo, a jump rope, a tablet game, building bricks).
- `Compare` marks each pair "Same" (an equal sign and the word) or "Different". Principal Gomez notes one surprise: "Patty hoped people would go to the Moon. Four years later, in 1969, they did!"
- Extra: `Write back` lets the class record or type a short reply letter for a new capsule, then `Print`.

## Content
- Four objects with three clue spots each and one decoy spot each, all listed above.
- Question jar: five slips; tile builder with 4 question words, 4 objects, 3 parts each.
- Then and me: Patty's three wishes; three catalog toys; twelve wish pictures and twelve toy pictures for the child.
- Price card numbers: 25 cents times about 10 (the 1965 to now price ratio) is about 2 dollars 50 cents; kept round for first graders.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The magnifier also works by keyboard: arrow keys move it, Enter taps the spot under it.
- `Flip` shows only on the photo. `Find out` shows only on a drawn or built question. `Compare` shows only when all six right-side slots are full; the hint names the next empty slot instead.
- With Motion off the lid opens without swinging and objects appear on the table without lifting.

## Look
- Accent `--brand` #55606e old-tin slate (header, the capsule, tag frames); gold #f4c542 (filled tags, the object check, the lit question); paper #f3f4f6; ink #15191f; muted #575d66. Objects keep their own aged paper colors inside a slate frame.
- Contrast (WCAG 2.1, computed): white on brand 6.39:1; brand on paper 5.81:1; ink on paper 16.03:1; muted on paper 6.03:1; ink on gold 10.84:1.
- Never color alone: tags carry icons and words; Same and Different carry symbols.
- Different from this batch (brick orange, market teal, map navy, workshop raspberry).

## Art
- People art goes to Gemini with `people: true`: Principal Gomez (5 poses: by the box, pointing, smiling, reading, surprised; 1:1; cutout yes); the 1965 class photo (one image, 4:3, about 18 first graders and a teacher, black and white, made for this tool); a grandparent (1, 1:1).
- Local FLUX (`scripts/localart.py`): the playground dig scene (16:9); the capsule closed and open (2); the letter, lunch ticket and catalog page as aged paper replicas with their printed clues added in code (3, 3:4); catalog toys (3); wish and toy picture choices (24, 1:1); the library and the school office (2).
- Drawn in code: the magnifier and lens, tags, the jar and slips, tiles, the compare columns, every printed clue word (so text stays sharp and exact).
About 41 images.

## Voice
Two bank voices, both unique in this batch: `clear-teacher` as Principal Gomez and narrator; `bright-teacher` as Patty's letter read aloud. `Curio.voice` with `scope: () => state.mode + ':' + state.object + ':' + state.slip`, `welcomeAfter: true`.
- how `welcome`: "Look what the diggers found! A time capsule. A first-grade class buried it here in 1965. Tap the lid to open it."
- how `pick` (once): "Tap something to pick it up."
- how `lens` (once): "Drag the magnifier. Find who made it, when, and where."
- event `clue`: "The maker!" / "The date! It's stamped right here." / "The place!"
- event `no-clue`: the decoy's line.
- event, whole, `object-done`: "That's who, when and where. On the shelf it goes."
- event, whole, `sources`: "You found who, when and where for every one. That makes them sources. Tap Question jar."
- how `jar`: "Tap Pick a question, or Make a question."
- event, whole, each answer line (photo toy, price card, Patty's wish, the studio, the store).
- event, whole, `no-answer`: "Good question! The capsule doesn't say. Who could we ask?"
- event, whole, `patty` (bright-teacher): the three wishes.
- how `then-me`: "Pick three wishes and three toys of your own."
- event, whole, `moon`: "Patty hoped people would go to the Moon. Four years later, in 1969, they did!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the magnifier with hit spots, the tag filler, the question jar and tile builder, the two-object answer view, and the compare columns.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tap everywhere | Each object has one decoy spot that says what it is; tags fill only from their real clue, and the child hears which kind of clue they found. |
| Tags | Skip the photo's back | The date is only on the back; `Flip` is named in the hint after the other two tags fill. |
| Questions | Draw slips without listening | Answers play whole and open the object they come from. |
| Then and me | Copy Patty's picks | Allowed; `Compare` then shows all Same, and Principal Gomez asks "Is anything different for you?" |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap lid: `pick`.
2. First object: `lens`; each clue: `clue` or `no-clue`; three tags: `object-done` (whole).
3. Four objects: `sources` (whole).
4. Question jar: `jar`; each `Find out`: its answer (whole) or `no-answer` (whole).
5. Then and me: `patty` (whole), waits; then `then-me`; `Compare`: Same/Different words, then `moon` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.4, 10, 11 and 12 (K-2) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| A time capsule is a store of objects and messages put away to be found by people in the future | Wikipedia, Time capsule (checked 2026-11-09) | International Time Capsule Society (Oglethorpe University) | yes |
| Prices have risen about tenfold since 1965 (CPI-U annual average 31.5 in 1965; about 322 in 2025) | U.S. Bureau of Labor Statistics, CPI-U series CUUR0000SA0 | Federal Reserve Bank of Minneapolis, CPI 1913- table | yes |
| The National School Lunch Act became law in 1946 and helps pay for school lunches | Wikipedia, National School Lunch Act (checked 2026-11-09) | USDA Food and Nutrition Service, NSLP history | yes |
| People first landed on the Moon in July 1969 (Apollo 11) | NASA, Apollo 11 mission overview | Wikipedia, Apollo 11 (checked 2026-11-09) | yes |
| Rocking horses, yo-yos and jump ropes were common toys in the 1960s | Wikipedia, Yo-yo (1960s Duncan revival) | The Strong National Museum of Play, toy collections | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r2, 2026-11-09): 322 / 31.5 = 10.2, so 25 cents then is about 2 dollars 55 cents now (rounded to "about 2 dollars and 50 cents"); 1969 minus 1965 is 4 years ("four years later"); every object has exactly one Maker, one Date and one Place spot plus one decoy; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 object, magnifier and tags fit; at 680x425 the tags sit under the object.
2. Each of the four objects fills Maker, Date and Place only from its real clue spots. (D2.His.11.K-2)
3. The photo's date is only on its back, reached with `Flip`. (D2.His.11.K-2)
4. The question jar draws five slips and builds questions from tiles; unanswerable questions get the "who could we ask" line. (D2.His.12.K-2)
5. The photo toy and lunch price questions open a second object to answer. (D2.His.10.K-2)
6. Then and me compares six picks with the 1965 picks and marks Same and Different. (D2.His.4.K-2)
7. `Flip`, `Find out` and `Compare` are never named before they show.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no lid swing or lift; no network requests.

## Open questions
- None for Cory.
