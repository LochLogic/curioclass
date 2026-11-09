# Text Feature Makeover

## One idea
Octavia the octopus has a page about ocean animals that is one long plain wall of words, and every question she asks takes ages to find, so the class gives the page a makeover one text feature at a time (headings, a table of contents, a glossary, icons, a menu) and finds the answer to her next question with the new feature; a sand timer fills while they look, and the two bars side by side (plain page, made-over page) show what each feature is for: it helps you find things fast.

## Not like
- windblown-pages (k-2, spec, same family): putting pictures, captions and a diagram back and deciding if an answer is in the words or the picture. Here adding the features that help you find facts, and timing the finding.
- meet-the-book-makers (k, spec): who made the parts of a book, and the cover and title page. Here features inside an informational text.
- big-question-chart (k-2, spec): gathering answers to a class question. Here finding answers fast in one text.
- structure-spotter (3, concept, same family): text structures. Here text features.
- context-clue-hunt (1, spec): working out a word from clues around it. Here a glossary gives the meaning.

## Who and how
- Grades 1 and 2, ELA, module "Text Features" (Reading Informational Text). Standards: RI.1.5 (Level 1), RI.2.5 (Level 2).
- Driver: a pair at one device or the teacher on a projector (tool.json `driver: "either"`). Every sentence is read on tap and every question aloud (BASELINE rule 4).
- Two levels: `Level 1: Ocean Makeover` (headings, table of contents, glossary, icons, menu) and `Level 2: Moon Makeover` (captions, bold words, subheadings, an index, a menu, on a longer text). tool.json `modes: []`, `minutes: "15-20"`, `grades_label: "Grades 1-2"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.1.5 | Place a heading on each section, then find a fact using the headings | heading signs; the timer bars | 2, 7 |
| RI.1.5 | Build the table of contents from the headings, then use it to jump to a page | a contents page with page numbers | 3 |
| RI.1.5 | Match glossary cards to bold words, then use the glossary to answer "What does school mean here?" | a glossary page | 4 |
| RI.1.5 | Place icons (a fish plate for what it eats, a house for where it lives) on the sentences they mark, then find a fact by icon | small icons in the margin | 5 |
| RI.1.5 | Turn on the menu (tabs on screen) and use it to jump | a tab bar | 6 |
| RI.2.5 | Level 2: add captions to photos, bold key words, subheadings and an index, then use each to find a fact | the moon pages with each feature | 8 |

## Screens and modes
Header (kit): title "Text Feature Makeover"; `Level 1`, `Level 2`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A seaside reading nook with Octavia holding a long, droopy scroll. First hint: "Tap Octavia's page to start." The first tap opens the plain page with her line; the welcome is queued after it (`welcomeAfter: true`).

**The page.** Focus: the text page (780 x 560), and on the right the toolbox (five feature tools, each a picture and a word, 120 x 100) and the timer bars (a pair of bars per feature: plain and made-over). Every sentence is a tap target (read aloud on tap; a second tap answers). The plain page is all four sections run together with no headings, pictures off, no bold.

**A round.** For each feature, in order:
1. Octavia asks a question on the page as it is (before). The sand timer starts when her question ends. The class taps the sentence that answers it; a wrong sentence ripples and is read, and the timer keeps going. Right: the timer stops and the plain bar fills to the time taken.
2. Octavia says "This takes forever! Let's add {headings}." The tool lights in the toolbox; tap it and do its job (below).
3. Octavia asks a new matched question; the class uses the feature to find it. The made-over bar fills next to the plain one.
4. Octavia says what the feature is for, in one sentence.

**Feature jobs (Level 1).**
- Headings: four heading signs (Sharks, Octopuses, Sea Turtles, Clownfish) to drag onto the start of each section; the section's picture appears as hint once placed right.
- Table of contents: the page splits into a little book (contents page plus four pages); the class drags each heading to its line on the contents page and the page numbers fill in. Using it: tap a contents line to jump.
- Glossary: four words go bold (school, ink, shell, anemone); drag each meaning card to its word on the glossary page. Using it: tap a bold word to open its glossary line.
- Icons: a key at the top (fish plate: what it eats; little house: where it lives); drag the icons to the eight sentences that tell those things (two per animal). Using it: Octavia asks what an animal eats and the class looks for the plate.
- Menu: flip the switch; a tab bar appears (Home, Sharks, Octopuses, Sea Turtles, Clownfish, Glossary). Using it: "Show me the clownfish page."

**Level 2 (Moon Makeover).** A six-page moon text with photos; same round shape with captions (match a caption to each photo), bold words (tap the word the glossary needs), subheadings (place two subheadings within a page), an index (drag words to their page numbers, alphabetical order shown), and the menu.

**Before and after.** After the last feature: the plain page and the made-over page side by side with every feature tagged by the question it answered, and the two sets of bars.

At 1366x768 the page, toolbox and bars fit above the fold. At 680x425 the toolbox becomes a row above the page.

## Content
All text written for Curio Class.

**Ocean Animals (Level 1), four sections:**
- Sharks: Sharks are fish. Many sharks eat fish and squid. A shark can lose a tooth and grow a new one. Sharks live in oceans all over the world.
- Octopuses: An octopus has eight arms. It can squirt ink to hide from danger. It eats crabs and clams. An octopus lives in a den between rocks.
- Sea Turtles: A sea turtle has a hard shell. Some sea turtles eat sea grass, and some eat jellyfish. Sea turtles swim in warm oceans. They lay their eggs on sandy beaches.
- Clownfish: Clownfish are small orange and white fish. They live in an anemone, a sea animal with stinging arms that do not hurt them. Clownfish eat tiny animals and plants that float by. Many small fish swim in a school.
- Icon sentences (eats; lives): sharks: "Many sharks eat fish and squid." ; "Sharks live in oceans all over the world." Octopuses: "It eats crabs and clams." ; "An octopus lives in a den between rocks." Sea turtles: "Some sea turtles eat sea grass, and some eat jellyfish." ; "Sea turtles swim in warm oceans." Clownfish: "Clownfish eat tiny animals and plants that float by." ; "They live in an anemone..."
- Glossary: school: a big group of fish swimming together. ink: a dark liquid an octopus squirts. shell: the hard cover on a turtle's back. anemone: a sea animal with soft stinging arms.

**Questions (before | after, the feature):**
- Headings: Where does it tell about sea turtles? | Where does it tell about clownfish?
- Table of contents: What page is about octopuses? (the before question asks to find the octopus part) | What page is about sharks?
- Glossary: What does "shell" mean? | What does "school" mean here?
- Icons: Where does an octopus live? | What does a sea turtle eat?
- Menu: Find the shark part. | Show me the clownfish page.

**The Moon (Level 2), six pages:** Our Moon; The Moon's Light (subheadings: Reflected Light, Phases); Craters; People on the Moon (Apollo 11, 1969); Moon and Tides; Index and Glossary. Bold words: crater, phase, orbit, tide. Captions for four photos (a full moon, a crater close-up, an astronaut footprint, a beach at high tide). Index words: Apollo 11, crater, footprint, light, orbit, phase, tide.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The timer counts from the end of Octavia's question to the right tap; Read taps (first tap on a sentence) do not stop it. The bars show seconds as length with the number under them; no score, no ranking, nothing kept.
- A feature job must be finished before the after question; a misplaced piece slides back with a hint ("This heading goes where the words tell about turtles").
- If the before question is not found in 60 s, Octavia says "Phew, it's hiding! Here it is," lights the sentence, and fills the bar to 60.
- `Next feature` appears after Octavia's what-it-is-for line; the order is fixed.

## Look
- Accent `--brand` #b0304a coral (header, headings once added, frames); gold #f4c542 (the timer sand, stars); paper #fdf6f5; ink #2a1416; muted #6b5254. Scene: a seaside reading nook with a porthole.
- Contrast (WCAG 2.1, computed): white on brand 6.24:1; brand on paper 5.84:1; ink on paper 16.26:1; muted on paper 6.65:1; ink on gold 10.67:1.
- Never color alone: plain and made-over bars are labeled with a plain page icon and a sparkle page icon; icons have shapes and a key.
- Different from this batch (dusk violet, workshop teal, brick map, olive post office) and from windblown-pages' sea teal.

## Art
Local FLUX (`scripts/localart.py`); no people except one astronaut in a suit with the visor down (Level 2), drawn locally as an object.
- nook (1): "A cozy seaside reading nook with a porthole window, soft gouache, no text"; 16:9; cutout no.
- Octavia (4, ask, droop, cheer, point): "A friendly coral-pink octopus wearing round glasses, <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- ocean animals (4): "A realistic <shark / octopus / green sea turtle / clownfish in an anemone>, natural history illustration style, plain white background"; 4:3; cutout no.
- moon pictures (4): "<a full moon / a close-up of moon craters / an astronaut boot print in moon dust / a beach at high tide>, realistic illustration"; 4:3; cutout no.
About 13 images. Drawn in code: the page, headings, contents, glossary, icons, tab bar, timer, bars, controls.

## Voice
Bank voice `curious-librarian` as Octavia (unique in this batch). `Curio.voice` with `scope: () => state.level + ':' + state.feature + ':' + state.step`, `welcomeAfter: true`.
- event `open`: "Here's my page about ocean animals."
- how `welcome`: "Hi, I'm Octavia! My page is hard to use. I'll ask a question, and you tap the sentence that answers it. Then we'll give my page a makeover."
- event, whole, `ask`: the question.
- event, whole, `sentence`: the tapped sentence.
- event `found` / `notHere`: "You found it!" / "Not here. Keep looking."
- event `slow`: "This takes forever! Let's add {headings}."
- how `job`: "{Drag each heading to the start of its part.}"
- event `hintPiece`: "{This heading goes where the words tell about turtles.}"
- event `forWhat`: "{Headings tell you what each part is about, so you can skip right to it.}" (one line per feature)
- event `hiding`: "Phew, it's hiding! Here it is."
- event `after`: "Look at my page now! Every feature helped us find something faster."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
`kit/text-features.js`, described in tools/windblown-pages/spec.md, exposed as `__tool.tf`. This tool uses Page (sections as pages, with sentence ids), Feature pieces (heading, glossary, menu, plus icons, contents, caption, bold, subheading and index added to the piece list here), Answer source (questions with `where: 'words'` and a proof sentence id), and Reveal (with the timer: `tf.time(start, stop)` added for the before and after bars). Not Diagram.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Find a fact | Tap every sentence | Each wrong tap is read and the timer runs, so tapping all fills the bar; nothing is scored, and the bars show the feature only when it is used. |
| Headings | Drop headings anywhere | 4 headings on 4 sections: 24 orders, one right (computed); misplaced ones slide back. |
| Icons | Drop icons anywhere | 8 icon spots from 16 sentences; only the eats and lives sentences take them. |
| Glossary | Match in any order | 4 meanings to 4 words: 24 orders, one right. |
| Index (Level 2) | Any page | Each index word has one page in the data. |
The tool teaches by contrast, so its honest check is the after question found with the feature (Done when 7).

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the page: `open`, `welcome` (queued, first time).
2. Each round: `ask` (whole); per tap `sentence` (whole) then `found` or `notHere`; or `hiding` at 60 s.
3. `slow`, then `job`, `hintPiece` on a miss; then `ask` (whole) for the after question; `found`; `forWhat`.
4. End: `after`.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.1.5 and RI.2.5 wording (headings, tables of contents, glossaries, electronic menus, icons; captions, bold print, subheadings, glossaries, indexes, electronic menus, icons) | thecorestandards.org, RI Grades 1 and 2 | CCSS ELA 2010 PDF | yes |
| Octopuses have eight arms and can release ink to escape predators | NOAA Ocean Service (oceanservice.noaa.gov), octopus | Smithsonian Ocean (ocean.si.edu), octopus | yes |
| Sharks shed and replace teeth throughout their lives | Florida Museum of Natural History, shark biology pages | Smithsonian Ocean (ocean.si.edu), sharks | yes |
| Green sea turtles eat seagrass and algae as adults; leatherbacks eat jellyfish | NOAA Fisheries, green turtle and leatherback species pages | Sea Turtle Conservancy, sea turtle information | yes |
| Clownfish live among sea anemones whose stings do not harm them | National Geographic, clownfish animal page | Smithsonian Ocean (ocean.si.edu), clownfish and anemones | yes |
| Sea turtles lay eggs on sandy beaches | NOAA Fisheries, sea turtles | Sea Turtle Conservancy | yes |
| Apollo 11 landed on the Moon in 1969 | NASA, Apollo 11 mission overview | Smithsonian National Air and Space Museum, Apollo 11 | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad b6, 2026-11-08): two icon sentences per animal (8 of 16 sentences); heading and glossary orders 4! = 24; every after question's answer sentence carries its feature (heading, contents line, bold word, icon, tab); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the page, toolbox and bars show with no scroll; at 680x425 the toolbox sits above the page.
2. Headings: each sits only on its section. (RI.1.5)
3. Contents: page numbers fill when headings are placed; a contents tap jumps to the page. (RI.1.5)
4. Glossary: each meaning sits only on its word; a bold word tap opens its line. (RI.1.5)
5. Icons: only the eight eats and lives sentences take icons, each the right kind. (RI.1.5)
6. Menu: the tab bar jumps to each part. (RI.1.5)
7. Bars: the before and after times fill for each feature, measured from the question's end to the right tap.
8. Level 2: captions, bold words, subheadings, index and menu each work and answer their question. (RI.2.5)
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Pre-reader: every sentence and question is read; tools have pictures.
11. Motion off: the sand drops as a fill, no wobbling scroll; no network requests; nothing saved.

## Open questions
- None for Cory.
