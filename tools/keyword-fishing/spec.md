# Keyword Fishing

## One idea
Every word you tie on your line is a filter you can watch work: fish (made-up kid web pages) that don't carry that word swim away from your bobber before you cast, so you see a lone word pull in a crowd, a little word like "what" change nothing, and one word too many empty the lake.

## Not like
- credit-card-builder (3-5, this group): what to do with a source once you have it. Here you are finding it; no credits, no sources opened.
- boolean-builder (9-12, this group): operators, parentheses and a Venn diagram over a research database. Here there are no operators at all: every word must be on the page, and the skill is which words to choose, drop or swap.
- research-quest (6-8, this group) and resource-detective (2, built): a story and a clue trail. Here it is a short puzzle per level with a live count, no story.
- library-adventure (K-2, built): finding a book on a shelf by its spine label. Here the shelf is replaced by a search box.
- wonder-wall (K-2, built): sorting questions by how to answer them. Here the question is given and you turn it into search words.
- Research Rover (ela grade 4, research family, not built): notes and outlines from a mini library. Here nothing is read or noted; the catch itself is the lesson.

## Who and how
- Grades 3 to 5, library. Module: Search Like a Pro (Research), "Keywords, catalogs and kid-safe search".
- Topic line: "choosing search keywords".
- Driver: students in pairs on laptops, or a teacher on a projector with the class calling out words. 15 to 25 minutes.
- Standards: AASL.Curate (IV.A.2 identifying possible sources of information), AASL.Inquire (I.A.1 formulating questions).
- tool.json: driver "students or teacher", minutes "15-25", modes ["Levels", "Free fishing"], grades_label "Grades 3-5".

## Screens and modes
Kit frame (`kit:curio`), own `:root`. Header: title "Keyword Fishing", small line "Pick the words, watch what bites"; mode buttons **Levels** (fish icon, opens first) and **Free fishing** (wave icon); Motion, Sound, Read.

Focus (both modes): the lake, with the fish gathering at or leaving the bobber and the Nibble count on it. The stage is the biggest block (left, about 60 percent of the width; top under 1000 px wide), the bobber at its center.
Stage: the painted lake seen from the dock (art kf-lake-dock). The 30 pond fish (Content) are painted cutouts in four topic kinds (art kf-fish-kit), each with a white code tag on its side showing its page title in 12 px or larger type; they swim slowly in the water (flipped to face the way they swim, a small code wiggle for the tail). The painted bobber (art kf-bobber) floats in the middle on a fishing line drawn in code. A **Nibble count** badge sits on the bobber: "30 fish nibbling", updated live.

Panel (right): `#hint`; the question card (Levels only); **Your line**: a row of up to 8 word slots on a drawn fishing line (Level 3 starts with all 8 full); under it the **Word box** (Levels: the level's tiles; Free fishing: the tackle box and a text field); buttons **Cast** (big, gold), **Take it off** and **Swap a word** (both act on the selected line word), **Clear line**; then the **Bucket** (a painted pail icon, art kf-bucket, over its list), which lists what was reeled in after a cast.

### Levels (opens first)
Six levels in a strip above the question card ("1" to "6", each with a fish sticker once solved; any level can be opened any time). Each level shows a kid's question, the tiles made from it, and the goal line: "Catch 3 fish or fewer, and one of them must answer the question." Tap a tile to tie it on the line (or drag it). Tap a word on the line to select it (it lifts); then press **Take it off** or **Swap a word** (or drag it off the line). Fish react at once: fish that have every word on the line swim toward the bobber and circle it; the others drift away. Cast reels in the circling fish. The bucket then lists each one (title, site, one-line snippet). If an answer fish is caught it gets a gold fin and "This one answers it!" and, if the bucket holds 3 or fewer, the level gets its sticker.

### Free fishing
The same lake and line with no question and no goal. The Word box becomes the **Tackle box**: every content word in the pond, grouped in four drawers (Ocean and pets, Night animals and sports, Earth and fire, Space and weather) plus a fifth drawer "Little words". A text field "Type a word" with an **Add** button lets a student try any word; a word no fish has shows "No fish here know that word." under the field and is still tied on, so the lake empties (that is the lesson).

## Content
Pond (30 fish; all titles and sites made up; snippets say what the page covers, never a fact). Words listed are the page's content words; every fish also has all the little words.

| Id | Title | Site | Snippet | Words |
|---|---|---|---|---|
| T1 | Sea Turtle Snack Guide | Ocean Kids Notebook | What sea turtles eat, with pictures of their food. | sea turtle eat food jellyfish seagrass ocean animal |
| T2 | What's on a Sea Turtle's Menu? | Reef Ranger Club | A sea turtle's diet, food by food. | sea turtle eat food diet ocean animal |
| T3 | Sea Turtle Nests | Shoreline Science Kids | Where sea turtles dig nests and leave their eggs. | sea turtle egg nest beach sand night animal |
| T4 | Hatchling Race to the Waves | Ocean Kids Notebook | Baby sea turtles leaving the nest at night. | sea turtle egg hatchling beach night ocean animal |
| T5 | Turtle Pond Pets | Pet Pals Corner | Caring for a pet turtle in a tank. | turtle pet pond tank food eat animal |
| T6 | Giant Tortoises of the Islands | World Animal Atlas for Kids | Where giant tortoises live. | tortoise turtle giant size island land animal |
| T7 | Tortoise Size Chart | Reptile Ruler | How the size of tortoises compares, kind by kind. | tortoise turtle size weight land animal chart |
| T8 | Turtle Racing Board Game | Toy Shelf Reviews | A review of a turtle race game. | turtle game toy race |
| T9 | Sea Turtle Stuffed Toy | Toy Shelf Reviews | A review of a plush sea turtle. | sea turtle toy plush |
| T10 | Tortoise Pet Care | Pet Pals Corner | Food and homes for pet tortoises. | tortoise turtle pet food eat animal |
| T11 | The Tortoise and the Hare | Story Time Shelf | The old fable, retold. | tortoise hare story race |
| B1 | How Bats Hunt at Night | Night Sky Nature | How bats use sound to find food in the dark. | bat animal echolocation sound dark night insect food hunt |
| B2 | Fruit Bats and Their Food | World Animal Atlas for Kids | Bats that eat fruit. | bat animal fruit food eat tree |
| B3 | Bat Caves | Night Sky Nature | Where bats sleep in the day. | bat animal cave dark sleep |
| B4 | Picking a Baseball Bat | Ballpark Basics | Choosing a bat for your size. | bat baseball wood size sport |
| B5 | Cricket Bats Explained | Ballpark Basics | The flat bat used in the sport of cricket. | bat cricket sport wood |
| B6 | Paper Bat Craft | Craft Time Corner | Fold and cut a paper bat. | bat paper craft |
| B7 | Spooky Bat Stories | Story Time Shelf | Short stories with bats in them. | bat story night spooky |
| V1 | Why Volcanoes Erupt | Rock Hound Kids | What happens inside a volcano before it erupts. | volcano erupt magma lava pressure earth |
| V2 | Volcano in a Bottle | Science Fair Station | A baking soda volcano project. | volcano project baking soda erupt experiment |
| V3 | Island Volcano Walks | Island Trails for Kids | Trails near island volcanoes. | volcano lava island erupt trail |
| V4 | Volcano Park Trip Planner | Family Trip Board | Planning a visit to a volcano park. | volcano park trip map |
| V5 | Lava Lamp How-To | Craft Time Corner | Make a lamp with oil and water. | lava lamp craft oil water |
| M1 | Mars, the Cold Red Planet | Space Scouts Notebook | What the weather and temperature are like on Mars. | mars planet temperature cold weather space |
| M2 | Rovers on Mars | Space Scouts Notebook | Robots that drive on Mars. | mars planet rover robot space |
| M3 | Mars, Roman God of War | Myth Map for Kids | The myth behind the planet's name. | mars myth rome god war |
| M4 | Mars Street Bakery Menu | Mars Street Bakery | A made-up bakery's cakes. | mars bakery food menu cake |
| M5 | Weather on Other Planets | Space Scouts Notebook | Weather on the planets, compared. | planet weather temperature space |
| M6 | Coldest Places on Earth | Polar Pals | The coldest places on our planet. | cold temperature ice earth |
| M7 | Planet Mars Coloring Page | Space Scouts Notebook | A page to print and color. | mars planet coloring art |

Little words (on every fish): a, an, the, what, do, does, how, is, are, why, where, when, of, to, in, on, at, it, their, they, get, can.
Matching (the tool's own simple model, said in the teacher notes): a fish bites only if it has every word on the line. A word and its plural count as the same word (turtle, turtles; egg, eggs; volcano, volcanoes, volcanos). Real search engines rank pages instead of requiring every word; this pond works like a simple library catalog so the effect of each word is visible.

Levels (tiles in the order shown; answer fish; the goal is the tool's own choice: 3 fish or fewer including an answer fish):
1. "Little words": question: "What do sea turtles eat?" Tiles: what, do, sea, turtles, eat. Answer: T1 or T2. Checked catches: what do = 30; sea turtles = 5; turtles eat = 4 (T1, T2, T5, T10); sea turtles eat = 2 (solved).
2. "Too many": question: "How do bats find food in the dark?" Tiles: how, do, bats, find, food, in, the, dark. Answer: B1. bats = 7; bats food = 2 (B1, B2, solved); bats food dark = 1; find = 0 ("find" is on no page).
3. "Too few": question: "Where do sea turtles lay their eggs?" The line starts full: sea, turtles, lay, eggs, beach, night, Florida, sand. Catch: 0. Tiles to add back if removed: the same eight. Answer: T3. sea turtles eggs = 2 (T3, T4, solved); sea turtles nest needs the swap (below) = 1.
4. "Same idea, other word": question: "How big do tortoises grow?" Tiles: how, big, do, tortoises, grow. Swap list: big → size, large, huge; grow → get. Answer: T7. tortoises = 4 (T6, T7, T10, T11); tortoises big = 0; tortoises size = 2 (solved); tortoises large = 0.
5. "Two meanings": question: "How cold does it get on Mars?" Tiles: how, cold, does, it, get, on, Mars. Swap list: cold → temperature, freezing. Answer: M1. Mars = 5 (M1, M2, M3, M4, M7); cold = 2 (M1, M6, solved); Mars cold = 1; Mars temperature = 1.
6. "Put it together": question: "Why does lava come out of a volcano?" Tiles: why, does, lava, come, out, of, a, volcano. Swap list: come → erupt, burst (out stays a dead word until removed). Answer: V1. volcano = 4; lava = 3 (V1, V3, V5, solved); lava volcano = 2; volcano erupt = 3 (solved); come = 0; out = 0.
Swap lists for other words (shown when that tile is selected and Swap is pressed): eat → food, diet; lay → nest; eggs → nest, hatchling; dark → night; find → hunt.

Feedback lines (the hint, after Cast):
- More than 3 fish: "That's [n] fish. Too many to read! Tap a word tile that says what you want to know."
- 0 fish: "Nothing bit. Tap a word on your line, then press Take it off or Swap a word."
- Only little words on the line: "Little words are on every page, so they catch everything. Use the words that name your topic."
- A little word added to a line with other words (count unchanged): "Same fish as before. Little words don't change the catch."
- 1 to 3 fish with no answer fish: "Small catch, but none of these answers the question. Tap a word on your line and swap it, or tie on a different tile."
- Solved: "Good catch! [title] answers the question."

## Interactions in detail
- The live preview is the point, and the lake never blocks a tap: tiles, line words and Cast stay live while fish swim and while a cast reels in; a new tap re-aims the fish at once from wherever they are. Every change to the line re-sorts the fish within 600 ms (fish swim, ease in and out; with Motion off they fade to the bobber or to the edges instantly). The Nibble count updates at once.
- Cast: the line drops, the circling fish rise into the bucket over 800 ms (instant with Motion off), then the feedback line. Casting with an empty line says "Tap a word tile to tie it on your line first."
- More than 12 fish circling: they bunch in a tangle drawn round the bobber, and the bucket shows the first 12 with "+ [n] more".
- Duplicate tile: a word already on the line can't be added twice (the tile is dimmed). Eight slots full: tiles dim, hint "Your line is full. Tap a word on your line, then press Take it off."
- Take it off and Swap a word are disabled until a line word is selected. Swap a word: a small pop-up lists the swap words as tiles; tapping one replaces the selected word. Swap stays disabled for a selected word with no swap list, and the hint says "No swaps for that word. Press Take it off, or pick another word."
- Feedback after Cast is chosen in this order, first that fits: empty line; only little words; 0 fish; 1 to 3 fish with an answer fish (solved); 1 to 3 fish with no answer fish; more than 3 fish. The "Same fish as before" line is shown when a little word is tied on and the count does not change, not on Cast. In Free fishing only the count lines apply (no answer fish, no solved line).
- Fish are buttons: tapping a fish (or Enter on it) shows its title, site and snippet in a tag card, in any mode, so the lake is worth poking.
- Level stickers save in localStorage (`kf-levels`, try/catch); **Clear stickers** (panel footer, asks "Clear all six stickers?" with Yes and No) empties it. Free fishing saves nothing.
- Keyboard: tiles and line words are buttons in reading order; panel before stage; fish after; Enter casts when focus is on Cast. Visible focus.
- Sizes (STANDARDS.md): question, line, tiles and Cast visible without scrolling at 1280x720 and 1366x768; at 680x425 the bucket collapses to its count and the fish tags hide their titles (tags show on focus). At 375 wide the stage sits above the panel and is 220 px tall.

## Look
- Accent `--brand #4d7c0f` (lily-pad olive: header, Cast outline, solved stickers). `--head-ink #ffffff`.
- Own `:root` (a misty morning lake): `--paper #eef6f3`, `--panel #ffffff`, `--ink #1d2a24`, `--muted #4f5f57`, `--line #cfe0d8`, `--btn #4d7c0f`, `--focus #c2410c`. The lake is painted (kf-lake-dock); the painted fish come in four topic colors close to ocean #f4a259, night #8e7dbe, earth #e07a5f, space #5fa8d3, each with its code tag `#fff7d6` and ink text; the bobber is painted red and white; gold fin #f2b632 plus the word "Answers it" (never color alone).
- Neighbors: credit-card-builder crimson, research-quest teal, fake-or-fact-lab violet; 3-5 greens nearby are forest (depth-detective #2e6440) and field green (playbook #1e7a3c); olive is a yellow-green apart from both.
- Contrast: white on brand 4.99:1; brand on paper 4.54:1; brand on panel 4.99:1; ink on paper 13.57:1; muted on paper 6.15:1; muted on panel 6.76:1; focus on panel 5.18:1 and on paper 4.71:1; ink on fish tag 13.86:1; white on deep lake 9.02:1. All pass AA.

## Art
All local FLUX (`scripts/localart.py`); no people. One style: soft storybook painting of a misty morning lake.
- kf-lake-dock: a calm lake on a misty morning seen from the end of a wooden dock, reeds and lily pads at the edges, soft green hills far away, clear open water across the middle two thirds, storybook painting; 16:9; cutout no; people no; the stage background the fish swim over.
- kf-fish-kit: one shared prompt, "a single friendly cartoon fish seen from the side facing right, [round orange body with pale stripes / slim violet body with long dark fins / chunky coral red body with spots / sleek sky blue body with a silver belly], a smooth plain flank, storybook painting, plain white background"; pieces: ocean (orange, the turtle pages T1 to T11), night (violet, the bat pages B1 to B7), earth (coral, the volcano pages V1 to V5), space (blue, the Mars pages M1 to M7) (4); 16:10; cutout yes; people no; every pond fish, flipped to face its swim direction, with its title tag in code across the flank. Sizing rule: all fish the same length (about 110 px at 1366x768, 70 px at 680x425), tags centered on the flank; the gold "Answers it" fin and the level stickers are code overlays on copies of the cutout.
- kf-bobber: a red and white fishing bobber floating upright with a small ring of ripples, storybook painting, plain white background; 1:1; cutout yes; people no; the bobber at the center of the lake, under the code Nibble count badge; it dips on Cast.
- kf-bucket: a small dented tin fishing pail with a wire handle, seen from the front, storybook painting, plain white background; 1:1; cutout yes; people no; the Bucket header in the panel, and the pail the fish rise into on Cast.
That is 7 images, none with people. The line, word slots, tiles, tackle box drawers, tags, badges, tangle and preview.svg are drawn in code (controls and labels; the line bends as words are tied on).

## Voice
Bank voice `friendly-dad` (Achird), "Say in a relaxed, friendly way, like a kind dad helping with homework": a patient grown-up on the dock. No neighbor from `neighbors.py` (credit-card-builder bright-teacher) and no other spec in this batch uses it (its wave users are 6-8: flowchart-factory, flipbook-studio). `Curio.voice`, `scope: () => state.mode`. Questions and fish tags are on screen only (Read speaks them). How lines are spoken the first time, then only update the hint; event lines play every cast and are dropped when stale.
- w-levels (how; Levels welcome; stale once a word is on the line): "Tap word tiles to tie them on your line. Watch which fish swim to your bobber. Then press Cast."
- w-free (how; Free fishing welcome; stale once a word is on the line): "Free fishing. Tap any word in the tackle box, or type your own and press Add, and watch the lake."
- swap (how; the first time a level with a swap list opens; stale once Swap a word is used): "Stuck? Tap a word on your line, then press Swap a word."
- tooMany (event; after a cast with more than 3 fish; stale once the line changes): "Too many to read! Tap a word tile that says what you want to know."
- none (event; after a cast with 0 fish; stale once the line changes): "Nothing bit. Tap a word on your line, then press Take it off or Swap a word."
- little (event; after a cast with only little words; stale once the line changes): "Little words are on every page. Tap the tiles that name your topic."
- noAnswer (event; after a cast of 1 to 3 fish with no answer fish; stale once the line changes): "Small catch, but none of these answers the question. Try swapping a word."
- solved (event; each solved cast; stale on level change): "Good catch! That one answers the question."
- unknown (event, Free fishing; when a typed word no fish has is added; stale once the word is removed): "No fish here know that word. Tap it on your line and press Take it off."

## Family engine
none

## Sources
- AASL, National School Library Standards for Learners, School Librarians, and School Libraries (2018), Standards Framework for Learners: Inquire I.A.1, Curate IV.A.2. https://standards.aasl.org/framework/
- All pages, sites and questions are made up for Curio Class; snippets describe topics and state no facts. The every-word match, plural rule, little-word list and the 3-fish goal are the tool's own choices (teacher notes say so and say that real web search ranks results instead).
- Checks run 2026-10-29 (Python, the 30-fish pond with the every-word rule and the plural rule "same word, or one is the other plus s or es"): all 25 checked catches in the Levels list match (for example sea turtles eat = 2, bats = 7, tortoises size = 2, Mars = 5, volcano erupt = 3); every level has solving lines of 1 to 3 words from its tiles and swaps (Level 1: 4, Level 4: 11, the others 27 or more); a line of only little words catches 30. Fixed: Level 3 starts with 8 words but the line held only 6, so the line now holds 8; tapping a line word both removed it and selected it for Swap, so tapping now selects and Take it off removes.

## Done when
1. Each level's checked catches in Content match the live Nibble count and the bucket exactly (verify with `__tool.catch(words)` against the table).
2. Adding or removing any word re-sorts fish within 600 ms; with Motion off fish move instantly; the count never lags the line.
3. Every level can be solved with the solution in Content, gets its sticker, and the sticker survives a reload; Clear stickers (after Yes) removes them.
4. A line of only little words catches all 30; adding a little word to any line leaves the count unchanged and shows the "Same fish" line.
5. Level 3 opens with all eight words on the line; selecting a line word enables Take it off and Swap a word; Swap a word replaces it with each listed swap and stays disabled for words with no swap list.
6. Free fishing: a typed unknown word empties the lake and shows "No fish here know that word."; typed plurals match singular words.
7. Every painted fish opens its tag card by tap and by Enter; tags stay readable (12 px or more) on every fish kind.
8. Focus: the lake with the bobber is the largest block at 1280x720, 1366x768 and 1920x1080, with the bobber at its center.
9. Tap while it plays: during a cast's reel-in and while fish are moving, a tile or line-word tap is taken at once and the fish re-aim from where they are.
10. Question, line, tiles and Cast are visible without scrolling at every size in STANDARDS.md; 375 wide works in `drive.py --host`.
11. Voice: welcome once per mode, how lines once, result lines every cast and dropped when the line changes; no line names a disabled control; Read speaks the hint; console clean; no network requests; the name appears only as "Curio Class".
