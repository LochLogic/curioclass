# Read-Along Shelf

## One idea
A shelf of six short books (two stories, two poems, two fact books, from kindergarten to grade 2) where the reading help fades as you turn the pages: the narrator reads the first page to you, stops before the last word of each line on the next page for the class to say it, and then hands the pages over, with every word still there to tap; each finished book plants a flag on a reading map, so the class sees what kinds of texts it has read and how much help it needed.

## Not like
- big-book-pointer (k, spec): Dot reads one word at a time where the class sends her, to teach print rules. Here whole books are read for meaning, and the skill is reading more of it yourself.
- question-cube (k-2, spec): a read-aloud followed by a question game. Here the reading itself is the activity; one purpose question frames each book.
- poem-drum (k-2, concept): poems read to a drum beat. Here poems are one kind on a shelf with stories and fact books.
- alike-and-different-books (k-2, spec): compares two books. Here each book is read on its own and the map shows the range.
- character-web, research-notebook, founding-words-explorer (9-12, same format): explorers for older readers. Here a K-2 shelf and map.

## Who and how
- Grades K-2, ELA, module "Reading Range and Text Complexity" (Reading Literature). Standards: RL.K.10, RL.1.10, RL.2.10, RI.K.10, RI.1.10, RI.2.10.
- Driver: either. On a projector the teacher leads a group read (the class says the stopped words aloud); a child at a device can read alone (every word can be tapped to hear it, BASELINE rule 4).
- tool.json `modes: []` (one shelf), `minutes: "5-15"` per book, `grades_label: "Grades K-2"`, `driver: "either"`.
- Privacy: the map's flags are saved only on this device (localStorage, try/catch), and the map says "Your reading map is saved only on this device." (BASELINE rule 7). Not a personal prompt.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.K.10, RI.K.10 | Group read-aloud with a purpose: hear the "Listen for" question first, join in on the refrain or rhyme words, then answer the question by picture | the purpose card on the page edge all through the book; the stopped word's blank; three answer pictures | 2, 3 |
| RL.1.10, RI.1.10 | Read a grade 1 poem and fact book with prompting and support that fades page by page (Read to me, Read with me, I read), tapping any word for help | the help meter (three bars to one); the glowing line; tapped words read aloud | 4, 5 |
| RL.2.10, RI.2.10 | Read a grade 2 fable and fact book with the same fading support, ending each on I read, with help only on tapped words | as above; the help meter reaches one bar | 4, 5 |
| All six | See the range of what the class has read: stories, poems and fact books, at each grade step | the reading map: three regions, a flag per finished book, leaves for how little help was needed | 6 |

## Screens and modes
Header (kit): title "Read-Along Shelf"; `Shelf` (books icon), `Map` (map icon); `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** The shelf: six painted book covers on a wooden shelf, each with a kind badge (story: a tree; poem: a hill with a music note; fact book: a lighthouse; code-drawn) and a grade step (K, 1, 2 on a small step icon). First hint: "Pick a book. Tap a cover." The first tap on a cover opens it to its purpose card and plays `open` (its own line); the welcome is queued after it (`welcomeAfter: true`). Tapping a cover also reads its title.

**The book** (all six).
- Focus: the open page (1000 x 560 at 1366x768: picture left 520 x 520, words right in 30 px type, lines spaced 1.6). The current line glows (pale gold band); the stopped word shows as a dotted blank the width of the word.
- The purpose card (left edge, 180 x 120, picture plus words, read on tap): "Listen for: ___" (K) or "Read to find out: ___" (grades 1 and 2).
- Panel (right, 300 px): hint; the help meter (three bars, labeled with its level's name); `More help` (bar up) and `Less help` (bar down); `Read this page` (speaker); `Next page` (arrow, gold) and `Back` (arrow); `Shelf`.
- Help levels (per page):
  - Read to me (three bars): the narrator reads each line and it glows as it is read.
  - Read with me (two bars): the narrator reads each line up to its last word and stops; the blank pulses; the class says the word; tap the blank (or wait 4 s on a projector, set in Interactions) and the word appears and is read.
  - I read (one bar): no narration. Tap any word to hear it (it glows). Tap the line's start dot to hear the whole line. `Read this page` reads the page (it does not change the level).
- Default fade: K books (Little Red Hen, Rain): page 1 Read to me, then Read with me for the rest (the class joins in on the refrain or rhyme). Grades 1 and 2 books: page 1 Read to me, page 2 Read with me, page 3 onward I read. A one-page or two-page book: Rain is Read to me then `Again` offers Read with me; Who Has Seen the Wind is page 1 Read to me, page 2 Read with me, then `Again` offers I read for both. `More help` and `Less help` change only the current page; the next page returns to the fade.
- After the last page: the purpose question with three answer pictures (190 x 150, read on tap). Right: `purposeYes` and the flag plants on the map (a short animation of a flag on the book's spot; Motion off: it appears). Wrong: `purposeNo` names what was tapped and offers `Look back` (to the page that answers it); the question stays.
- At 680x425: the page is 640 x 360, picture above words (picture 640 x 150), words 18 px; the panel folds under the page with the meter and Next.

**Map.** Focus: the reading map (painted, 1046 x 640): Story Woods (left), Poem Hills (center), Fact Harbor (right), each with a path of three stops, K, 1, 2, rising uphill (higher grade, higher stop). Each finished book's flag stands on its stop; under it, leaves for the least help used on that book's last page (three leaves: read on my own; two: read with me; one: read to me). Tap a flag: the book's title and kind are read, and `Open` reopens it. A region with no flag shows a dotted path and "Not visited yet." `Clear map` (with a confirm card) empties it.

## Content
Lines are shown as below; in Read with me the narrator stops before the last word of each line (the word in brackets is the stopped word).

**The Little Red Hen** (story, K; a traditional folk tale, retold). Listen for: "Who helps the Little Red Hen?" Answer: no one (the hen working alone) | the duck | the cat.
1. Once there was a little red hen. / She found some seeds of [wheat].
2. "Who will help me plant the wheat?" asked the Little Red Hen. / "Not I," said the [duck]. / "Not I," said the [cat]. / "Not I," said the [dog]. / "Then I will do it myself," said the Little Red Hen. / And she [did].
3. The same, with "cut the wheat".
4. The same, with "bake the bread".
5. "Who will help me eat the bread?" asked the Little Red Hen. / "I will!" said the [duck]. / "I will!" said the [cat]. / "I will!" said the [dog].
6. "No," said the Little Red Hen. / "I will eat it [myself]." / And she [did].
(In Read with me, the class also says "Not I" with the narrator: the refrain glows a beat early.)

**Rain** (poem, K; Robert Louis Stevenson, A Child's Garden of Verses, 1885). Listen for: "Where does the rain fall?" Answer: on the ships at sea | inside a house | on the moon.
1. The rain is raining all around, / It falls on field and [tree], / It rains on the umbrellas here, / And on the ships at [sea].

**Who Has Seen the Wind?** (poem, grade 1; Christina Rossetti, Sing-Song, 1872; modern spelling "through" for the first printing's "thro'"). Read to find out: "How can we tell the wind is there?" Answer: the leaves and trees move | we can see its color | it is cold.
1. Who has seen the wind? / Neither I nor [you]: / But when the leaves hang trembling, / The wind is passing [through].
2. Who has seen the wind? / Neither you nor [I]: / But when the trees bow down their heads, / The wind is passing [by].

**Seeds on the Move** (fact book, grade 1; our own). Read to find out: "How can a seed get to a new place?" Answer: the wind carries it | it walks on legs | it rides a bike.
1. Plants can't walk. / So how do their seeds get to new [places]?
2. Some seeds ride the wind. / A dandelion seed has soft fluff / that floats like a tiny [parachute].
3. Some seeds hitch a ride on animals. / Burrs have tiny hooks that stick to [fur].
4. Some seeds are inside fruit. / An animal eats the fruit / and drops the seeds far [away].
5. A coconut can float on the sea to a new beach. / Then it can grow into a new palm [tree].

**The Lion and the Mouse** (story, fable, grade 2; Aesop, retold). Read to find out: "How does the little mouse help the lion?" Answer: she chews the net | she roars | she brings him food.
1. A lion was sleeping in the sun. / A little mouse ran across his nose, / and the lion woke up with a [roar].
2. He caught the mouse in his big paw. / "Please let me go," said the mouse. / "Someday I may help [you]."
3. The lion laughed. / "How could a tiny mouse help me?" / But he let the mouse [go].
4. A few days later, the lion was caught in a hunter's net. / He roared and pulled, / but he could not get [out].
5. The mouse heard him. / She chewed the ropes until the net broke, / and the lion was [free]. / "You were right," said the lion. / "Little friends can be great [friends]."

**Bats See with Sound** (fact book, grade 2; our own). Read to find out: "How do many bats find food in the dark?" Answer: they listen to echoes | they use flashlights | they follow the moon.
1. Most bats are awake at night. / They sleep in the day, / hanging upside [down].
2. Many bats find their food in the dark / with [sound].
3. A bat makes high squeaks. / The squeaks bounce off a moth / and come back as [echoes].
4. The bat listens to the echoes / to find out where the moth [is]. / This is called [echolocation].
5. Bats are not blind. / They can see with their eyes, [too]!

Sizes (computed): 177, 24, 42, 80, 109 and 68 words; read times at the narrator's pace about 77, 10, 18, 35, 47 and 30 s; 191 distinct words across the shelf, each with a recorded word clip.

## Interactions in detail
- Every tap acts at once; tapping a word, blank, line dot, Next, Back or a help button stops the narrator at once and does that thing. Next is never locked (a teacher may skip); a page counts as read for the map when it has been narrated to the end or shown for at least 0.5 s per word.
- Read with me: the stop waits for a tap on the blank. On a projector, `Auto reveal` (a toggle under the help meter, off by default) reveals each blank 4 s after the stop. After the last blank on a page, the hint names Next page.
- I read: any word tap plays its word clip; the line dot plays the line clip. Nothing is timed or scored.
- A book reopened from the map or shelf starts at its page 1 with the default fade; the flag stays.
- The flag's leaves record the least help used on the book's last page this time (Read to me 1, Read with me 2, I read 3); a better reading later replaces it, a worse one does not.
- Purpose: a wrong pick never ends the book; `Look back` opens the answering page (Little Red Hen 5, Rain 1, Wind 2, Seeds 2, Lion 5, Bats 4), then `Answer` returns to the question.
- Storage blocked: the map works for this page load and says "This device can't save the map right now."
- Motion off: no glow sweep or flag animation; lines glow and flags appear at once.

## Look
- Accent `--brand` #56631a deep olive (header, help meter, Next); gold #f0c043 (the line glow edge, flags); paper #fbf8ef; ink #24260f; muted #5b5d45. Scene: a sunny library nook; the map in soft storybook colors.
- Contrast (WCAG 2.1, computed): white on brand 6.57:1; brand on paper 6.19:1; ink on paper 14.55:1; muted on paper 6.39:1; ink on gold 9.07:1. Page text is ink on paper (14.55:1); the line glow is a pale band behind ink text, never colored text.
- Never color alone: help levels show bars and their name; blanks are dotted outlines; flags have leaves.
- Different from this batch (teal, magenta, red, violet) and batch 1.

## Art
Local FLUX (`scripts/localart.py`); no people (the hunter in the fable is only his net). Each book has its own painted style so the shelf feels like many authors.
- shelf: "A sunny library nook with a long wooden shelf and a reading pillow, soft gouache, the shelf front empty"; 16:9; cutout no.
- covers (6): "A picture book cover for <a little red hen with a sheaf of wheat / rain over fields and ships at sea / leaves and trees blowing in the wind / seeds traveling: a dandelion puff, a burr, a coconut on a wave / a lion and a tiny mouse / a bat flying at night with sound waves>, <style per book: folk woodcut / soft watercolor / ink and wash / bright cut paper / classic engraving tint / night gouache>, a blank band at the top"; 3:4; cutout no.
- Pages: one painting per page, in its book's style: hen 6 (finding seeds; asking the duck, cat and dog under a tree; cutting wheat; baking bread in an oven; the animals eager at the table; the hen eating alone), rain 1, wind 2 (leaves trembling on a branch; trees bowing in the wind), seeds 5 (a plant in a pot; dandelion seeds floating; burrs on a dog's fur; a bird eating berries; a coconut floating to a beach), lion 5 (lion asleep, mouse on his nose; mouse in the lion's paw; lion laughing as the mouse runs; lion tangled in a rope net in the grass; mouse chewing the net, lion free), bats 5 (bats hanging upside down in a cave; a bat flying over a dark field; a bat squeaking at a moth with sound rings; a bat turning toward the moth; a bat's face with open eyes); 1:1; cutout no. 24 pages.
- answer pictures (18): one small painting per purpose answer (the hen working alone, a duck, a cat, ships at sea, a house, the moon, trees blowing, a colored swirl, a shivering scarf, a dandelion puff in the wind, a seed with legs, a seed on a bike, a mouse chewing a net, a mouse roaring, a mouse with food, a bat with echo rings, a bat with a flashlight, a bat and the moon); 4:3; cutout no.
- map: "A storybook map with a woods on the left, rolling hills in the middle and a harbor with a lighthouse on the right, each with a winding path climbing uphill, soft gouache, no labels"; 16:10; cutout no.
- flag: "A small cloth flag on a stick, plain cream, soft gouache, plain white background"; 1:2; cutout yes (the book's kind badge is drawn on it in code). leaf: "A single green leaf, soft gouache, plain white background"; 1:1; cutout yes.
About 52 images, no people. Drawn in code: the page text, line glow, blanks, kind badges, grade steps, help meter, every control.

## Voice
Bank voice `smooth-narrator` (style "Say smoothly and warmly, like an audiobook narrator"): it reads every book, line and word. Not used by K-2 ELA neighbors or batch 1. `Curio.voice` with `scope: () => state.book + ':' + state.page`, `welcomeAfter: true`.
- event `open`: the book's title and author ("The Little Red Hen, a folk tale."; "Rain, by Robert Louis Stevenson.").
- how `welcome`: "Welcome to the Read-Along Shelf. I'll read with you, and bit by bit, you'll read more on your own."
- event, whole, `purpose`: the purpose card ("Listen for: who helps the Little Red Hen?").
- event, whole, `line` (Read to me): each line clip. event, whole, `linePart` (Read with me): each line up to its stopped word. event `word`: the word clip (blank reveals and I read taps).
- how `withMeHow` (first Read with me page): "Now you help! When I stop, you say the next word. Then tap the dotted line."
- how `iReadHow` (first I read page): "Your turn to read this page. Tap any word if you need help."
- event `level`: "Read to me." / "Read with me." / "I read." (on More help, Less help)
- event, whole, `purposeAsk`: the question again, then "Tap a picture."
- event `purposeYes`: "Yes! {answer} Your flag is on the map." event `purposeNo`: "That's {tapped}. Tap Look back to find it in the book."
- how `mapHow`: "Here is your reading map: stories, poems and fact books. Tap a flag to open its book."
Read speaks the hint, which names the current action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Purpose question | Guess; the biggest picture; the picture that looks like the cover | 1 in 3, one size, shuffled; answer pictures are their own paintings, not cover or page crops; a wrong pick stays open with Look back, so the question is answered from the book, not skipped. |
| Map flag | Tap Next through every page | A page counts only when narrated to the end or shown 0.5 s per word, so a skimmed book takes as long as a read one; the flag still needs the purpose answer. |
| Leaves (help used) | Choose I read on the last page and tap every word | The leaves record help level, not skill, and the map says so ("leaves show how much help you chose"); it is a record for the class, not a score, so nothing is won. |
| Read with me | Tap the blank before saying the word | Allowed: the blank is help, not a test; the narrator's stop and pulse ask the class to say it first. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a cover: `open`, then `welcome` (queued, first book only), then `purpose` (whole). Hint names Next page or Read this page.
2. Read to me page: `line` clips in order (whole each). Read with me: `withMeHow` (first time), then per line `linePart` (whole), stop, the tap plays `word`, then the next `linePart`. I read: `iReadHow` (first time), then only tapped `word` or `line`.
3. After the last page: `purposeAsk` (whole), then `purposeYes` or `purposeNo`; the flag animation waits for `purposeYes`.
4. Map: `mapHow` (first), then flag taps read titles.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL/RI.K.10, 1.10, 2.10 wording (actively engage in group reading activities with purpose and understanding; with prompting and support, read prose and poetry or informational texts of appropriate complexity for grade 1; by year's end read and comprehend in the grades 2-3 band, with scaffolding as needed) | thecorestandards.org, RL and RI pages, K to 2 | CCSS ELA 2010 PDF, Reading Standards K-5 | yes |
| "Rain" text, Robert Louis Stevenson, A Child's Garden of Verses (1885), public domain | Project Gutenberg, A Child's Garden of Verses | Poetry Foundation, "Rain" | yes |
| "Who Has Seen the Wind?" text, Christina Rossetti, Sing-Song (1872), public domain | Project Gutenberg, Sing-Song | Poetry Foundation, "Who Has Seen the Wind?" | yes |
| The Little Red Hen is a traditional folk tale (hen asks duck, cat and dog for help at each step; none help; she eats the bread herself) | Library of Congress, read.gov classic books, "The Little Red Hen" | Project Gutenberg, The Little Red Hen (early 1900s reader) | yes |
| The Lion and the Mouse is an Aesop fable (the spared mouse frees the lion by gnawing the net; little friends may prove great friends) | Library of Congress, The Aesop for Children (1919), read.gov | Project Gutenberg, Aesop's Fables (Jacobs, 1894) | yes |
| Dandelion seeds float on the wind on a fluffy parachute; burrs hook onto fur; animals eat fruit and drop seeds elsewhere; coconuts float on the sea to new shores | USDA Forest Service, "Seed dispersal" (Celebrating Wildflowers) | Encyclopaedia Britannica, "Seed and fruit: dispersal" | yes |
| Most bats are active at night and roost hanging upside down; many bats echolocate (high calls, listen to echoes to find insects); bats are not blind | National Park Service, "Bats" | Bat Conservation International, "About bats" / U.S. Fish and Wildlife Service, "Bats" | yes |
Backed twice: 7. Cut: 0. Seeds on the Move and Bats See with Sound are our own texts; both fable and folk tale are retold in our own words.

Checks run (Python, scratchpad b2/shelf.py, 2026-11-08): word counts, read times and distinct words as in Content; Look back pages checked against each answer's line; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the whole page (picture and words) and the panel controls show with no scroll; at 680x425 the page and Next show with 18 px or larger text.
2. Purpose card: shown and read before page 1 of every book, and stays on the page edge. (RL.K.10, RI.K.10)
3. Every book's purpose question takes only its answer; a wrong pick offers Look back to the right page. (RL.K.10, RI.K.10)
4. The fade runs by default on every book (K: Read to me then Read with me; grades 1 and 2: Read to me, Read with me, I read), and More help and Less help change only the current page. (RL/RI.1.10, 2.10)
5. I read: every word on every page plays its own clip on tap; Read with me stops before every bracketed word. (RL/RI.1.10, 2.10)
6. The map plants a flag on the right region and grade stop for each finished book, with leaves for the least help used; reload keeps it; the privacy line shows. (all six)
7. Tap while it plays: a word, blank, Next or help tap during narration stops it and acts at once; no older line plays after a newer one.
8. Pre-reader: every title, purpose question and answer is spoken; answers are pictures.
9. Motion off: no glow sweep or flag animation, same pacing; no network requests.

## Open questions
- None for Cory.
