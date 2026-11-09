# Windblown Pages

## One idea
A gust blows the pictures, captions and a diagram off two books, and the teams put each one back on the page whose words it shows, but the real game comes next: for every page the class decides whether an answer lives in the words, in the picture, or in both, and finds the spot that proves it, so they discover that the picture of Hattie the hen saying "She looked high and low" is the only place that shows her hat sitting on the cow's horn right behind her.

## Not like
- meet-the-book-makers (k, spec): sorting every book part to the author or the illustrator. Here the makers are named once on the covers; the game is what a picture shows that the words do not.
- read-along-shelf (k-2, spec): reading books with help that fades. Here pages are rebuilt and their words and pictures compared.
- question-cube (k-2, spec): answering question words and lighting the proof sentence. Here every answer is first placed as words, picture or both, and pictures count as proof.
- alike-and-different-books (k-2, spec): comparing two books. Here comparing the words and pictures of one page.
- text-feature-makeover (1, concept, same family): adding headings, a glossary and icons to a plain page. Here pictures, captions and a labeled diagram.

## Who and how
- Grades K to 2, ELA, module "Pictures and Words Together" (Reading Literature). Standards: RL.K.6, RL.K.7, RL.1.7, RI.1.6, RI.1.7, RL.2.7, RI.2.7.
- Driver: teacher on a projector (tool.json `driver: "teacher"`); two teams, Team Breeze and Team Gust, take turns; the team says its answer and a helper taps. Every page, caption, card and question is spoken, so a pre-reader can play (BASELINE rule 4).
- Two books: a storybook, "Hattie's Hat", and a fact book, "Wind at Work". Rounds: Meet the makers, Gust!, Words or picture?, Picture tells more, The diagram (fact book). tool.json `modes: []`, `minutes: "15-25"`, `grades_label: "Grades K-2"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.K.6 | Meet the makers: tap the author's and the illustrator's names on each cover and hear what each does; then once, "Who made this picture?" | the two covers; two name cards | 2 |
| RL.K.7 | Gust!: put each storybook picture back on the page whose words it shows | blank pages with their words; scattered pictures | 3 |
| RL.1.7, RL.2.7 | Words or picture? (storybook): decide where an answer about a character, setting or event lives, then tap the spot that shows it; Picture tells more: pick what the picture adds | Words, Picture, Both buttons; the page | 4, 5 |
| RI.1.6 | Words or picture? (fact book): decide if the answer is in the words (including the caption) or the picture | the same buttons on the fact pages | 4 |
| RI.1.7 | Gust! (fact book) and Picture tells more: put photos and captions back and say what the picture adds to the key idea | fact pages with captions | 3, 5 |
| RI.2.7 | The diagram: put the labels back on the sailboat diagram, answer questions only it can answer, and say how it helps the words | the diagram with five empty label spots; the parts box | 6 |

## Screens and modes
Header (kit): title "Windblown Pages"; `Books` (book icon); team scoreboard (two weathervanes with tokens); `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A cozy library corner with an open window, the two books on a table, and Gail the gull in a little reporter's hat at a microphone. First hint: "Tap Hattie's Hat to meet the makers." The first tap opens that book's cover with its line; the welcome is queued after it (`welcomeAfter: true`).

**Meet the makers.** Focus: the cover (700 x 520) with "Words by" and "Pictures by" name cards. Tap each card to hear the name and what that maker does. Then the window bangs open: Gust!

**Gust!** Focus: the open book as a row of page thumbnails (each 220 x 160 with its words, the picture spot blank) and the blown pieces scattered over the table (pictures 200 x 150, captions as strips). Tap a piece to hear what it is ("A picture: a red hat flying over a fence."); drag it (or tap it, then a page) to a page. The team whose turn it is places one piece. Right: it snaps in, the page is read, a token goes on that team's weathervane. Wrong: the wind blows it back, the turn passes. After the first storybook picture is placed: "Who made this picture?" (Author | Illustrator), once.

**Words or picture?** Focus: one page large (1000 x 520), words below the picture, and three buttons: `Words` (a page-lines icon), `Picture` (a frame icon), `Both`. The question is read; the team picks; then "Show me!": the team taps the words or the spot in the picture that proves it (hot spots are about 140 x 140 px, invisible until the answer). Right place and right proof: two tokens; right place, wrong spot: one, and the spot glows.

**Picture tells more.** Focus: the page with the picture covered by a curtain. The words are read. "What will the picture tell us that the words don't?" Three cards are read; the team picks; the curtain opens and the picture proves or disproves it.

**The diagram.** Focus: the sailboat diagram (900 x 520) with five empty label spots and a parts box beside it (five label cards, each with a short meaning read on tap). Drag each label to its spot. Then two questions only the diagram can answer, and a last one: "How does the diagram help the words?" with three cards.

At 1366x768 each round's page and controls fit above the fold. At 680x425 the page is 640 x 330 and Gust! shows the table as a scrolling row.

## Content
Both books are written for Curio Class. Makers are made-up names, said as names only.

**"Hattie's Hat"** (words by Lena Brook, pictures by Omar Reyes). Pages (words; what the picture shows):
1. "Hattie the hen had a brand-new hat." Hattie in a red hat with a yellow flower, in a barnyard.
2. "Whoosh! The wind blew it away." The hat sailing over a fence, leaves swirling, Hattie flapping.
3. "Hattie ran and ran." Hattie running past a pond while two ducks watch.
4. "She looked high and low." Hattie peering under a bucket; the hat is hooked on the cow's horn right behind her.
5. "At last, she found it." The hat on top of the hay wagon with a bird sitting in it on three eggs; Hattie smiling, wearing a flowerpot instead.

**"Wind at Work"** (words by Sam Ortiz, pictures by Ana Li). Pages (words; picture; caption):
1. "Wind is moving air." A flag flapping and trees bending. Caption: "You can't see wind, but you can see what it moves."
2. "Wind turns windmills." A farm windmill beside a pond where cows drink. Caption: "This windmill pumps water for the cows."
3. "Wind carries seeds." A dandelion puff with seeds floating away. Caption: "Each seed has a fluffy top, like a tiny umbrella."
4. "Wind pushes sailboats." The labeled diagram. Caption: "The wind pushes on the sail."

**Gust! pieces**: five storybook pictures; three fact-book photos and three captions (the diagram stays for its own round). Storybook pages take only their picture; fact pages take only their photo and their caption.

**Words or picture?** (question; right answer; proof):
- p1 "What color is Hattie's hat?" Picture; the hat.
- p2 "What sound did the wind make?" Words; "Whoosh!".
- p1 "What kind of animal is Hattie?" Both; "hen" and Hattie.
- p4 "Where is the hat now?" Picture; the cow's horn.
- p3 "Who is watching Hattie run?" Picture; the ducks.
- fact p1 "What is wind?" Words; "moving air".
- fact p2 "What does this windmill do?" Words (the caption); "pumps water for the cows".
- fact p3 "What is on top of each seed?" Both; "fluffy top" and the seed's top.
Picture 3, Words 3, Both 2. Captions count as words; labels on the diagram count as the picture (said on the first fact page).

**Picture tells more** (words read; three cards, right first):
- p4 "She looked high and low.": "Her hat is on the cow's horn, right behind her." | "Hattie is looking for her hat." (the words already say that) | "The hat fell in the pond."
- p5 "At last, she found it.": "A bird is sitting on eggs in the hat, so Hattie let it keep the hat." | "Hattie found her hat." (the words already say that) | "Hattie's hat blew into a tree."
- fact p2 "Wind turns windmills.": "The windmill stands by a pond where cows drink." | "Wind turns windmills." (the words already say that) | "The windmill is on a boat."

**The diagram** (labels and meanings): sail ("the cloth the wind pushes"), mast ("the tall pole that holds up the sail"), hull ("the body of the boat that floats"), rudder ("the flat part under the back that steers"), wind arrow ("which way the air is moving"). Questions: "Which part steers the boat?" (tap: rudder) | "Which way will the boat go?" (three arrows: with the wind arrow, against it, straight up) | "How does the diagram help the words?" ("It shows the parts and where they are." | "It tells a story about a boat." | "It shows what the sea sounds like.").

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Turns: Gust! alternates by piece; Words or picture? and Picture tells more alternate by question; The diagram alternates by label, then by question. `Pass` gives the turn to the other team.
- Tokens: one per right placement, label or pick; Words or picture? gives two for right place and proof. The scoreboard shows both totals; teams can be turned off (`Teams: off`) for one-class play.
- Proof taps: one tap answers; a tap outside every hot spot says "Tap right on it."
- A book's rounds unlock in order, but `Books` lets a teacher jump to any round after Gust! for that book.
- Nothing is saved.

## Look
- Accent `--brand` #00607a wind cyan (header, scoreboard, page frames); gold #f6c445 (tokens, stars); paper #f4f9fa; ink #10262d; muted #4b5f66. Scene: a library corner on a breezy day, leaves in at the window.
- Contrast (WCAG 2.1, computed): white on brand 7.11:1; brand on paper 6.69:1; ink on paper 14.79:1; muted on paper 6.32:1; ink on gold 9.65:1.
- Never color alone: Words, Picture and Both have icons; teams have weathervane shapes (a leaf for Breeze, a swirl for Gust) as well as color; proof spots glow with an outline.
- Different from this batch (indigo, moss, engine black, curtain wine) and the K-2 ELA neighbors (owl-wants-more is a greener teal).

## Art
Local FLUX (`scripts/localart.py`); no people.
- library (1): "A cozy library corner on a breezy day, an open window with leaves blowing in, two books on a table, soft gouache, no text"; 16:9; cutout no.
- gail (stand, report, point, cheer: 4): "A friendly seagull in a small reporter's hat with a microphone, <standing / talking / pointing / cheering>, soft gouache, plain white background"; 1:1; cutout yes.
- story pictures (5): "<each Hattie page's picture as in Content>, soft gouache picture book style"; 4:3; cutout no. The hat on the cow's horn must be clear but not the first thing the eye lands on.
- fact photos (3): "<a flag flapping and trees bending in wind / a farm windmill beside a pond with cows drinking / a dandelion puff with seeds floating>, realistic soft watercolor"; 4:3; cutout no.
- covers (2): "<Hattie the hen in a red hat / a sailboat, a windmill and a dandelion>, soft gouache book cover art, no text"; 3:4; cutout no.
- diagram: drawn in code (sailboat outline, label lines, wind arrow) so labels and spots are exact; a painted sea backdrop (1) behind it.
About 16 images. Drawn in code: page frames, captions, curtains, tokens, weathervanes, the diagram, every control.

## Voice
Bank voice `news-reader` (style "like a trusted radio news reader") as Gail the gull. Not used by the K-2 ELA neighbors or the rest of this batch. `Curio.voice` with `scope: () => state.book + ':' + state.round + ':' + state.item`, `welcomeAfter: true`.
- event `book`: "{Hattie's Hat}!"
- how `welcome`: "This is Gail with the windy news. A big gust is coming to the library. Hold on to your pages!"
- event `maker`: "{Lena Brook} wrote the words." / "{Omar Reyes} made the pictures."
- event `gust`: "Here it comes! Whoosh! The pictures blew off the pages!"
- how `gustHow`: "Put each picture back on the page whose words it shows."
- event `piece`: what the piece is. event, whole, `page`: the page's words. event `placeYes`: "Back where it belongs!" event `placeNo`: "The wind blew it back. {Team Gust}, your turn."
- event, whole, `makerAsk`: "Who made this picture?" event `makerYes`: "Yes! The illustrator made the pictures."
- how `wopHow`: "Where is the answer: in the words, in the picture, or both?"
- event, whole, `question`. event `wopYes`: "Yes! Now show me." event `wopNo`: "Look again. Is it in the {words}?" event `proofYes` / `proofNo`: "There it is!" / "Tap right on it."
- event, whole, `ptmAsk`: "What will the picture tell us that the words don't?" event `ptmSays`: "The words already say that. What does the picture add?" event `ptmYes`: "The picture shows it!"
- how `diagramHow`: "The labels blew off the sailboat diagram. Put each one back."
- event `label`: the label and its meaning.
- event `token`: a soft wind chime (sound) for each token.
- event `wrap`: "That's the windy news. Pictures tell us things words don't!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
`kit/text-features.js` (the text-features family). No family doc exists and no sibling is specced (text-feature-makeover, structure-spotter and how-it-works-diagrams are concepts), so this spec describes the engine. Pure parts in one marked block, exposed as `__tool.tf`.
- **Page**: `{id, words, picture:{src, hotspots:[{id, box, name}]}, caption, labels:[{id, text, meaning, spot}]}`.
- **Feature pieces**: picture, caption, label, heading, sidebar, glossary, menu (the later siblings use the last four); `tf.fits(piece, page)` checks a piece belongs on a page.
- **Answer source**: questions `{ask, where: 'words'|'picture'|'both', proof:[ids]}`; `tf.where(answer, pick)` and `tf.proof(tap, ids)` check the place and the tap.
- **Reveal**: covering and uncovering a feature for "what does it add" comparisons; text-feature-makeover uses it to time a search with and without a feature.
- **Diagram**: label spots with lines; `tf.labelCheck(label, spot)`; an optional step animation (how-it-works-diagrams runs steps only when every label and sentence is placed).
This tool uses: Page, Feature pieces (picture, caption, label), Answer source, Reveal, Diagram (no step animation).

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Gust! | Place pieces at random | First storybook piece 1 in 5; fact captions are only right with their photo's page; a wrong piece blows back and the turn passes. |
| Words or picture? | Always pick Both | Both is right twice in eight (computed); always Both scores 2 of 8 and no proof tokens elsewhere. |
| Proof | Tap anywhere | Hot spots are small and named; a wrong tap gets "Tap right on it" and no proof token. |
| Picture tells more | Pick the sentence that sounds most like the page | The "words already say that" card is the closest match to the words every time, and it is always wrong, which is the lesson. |
| The diagram | Guess labels | 5 labels on 5 spots in one way of 120 (computed); each label's meaning is read on tap. |
| Makers | Guess | 1 in 2, asked once; the names were heard on the cover first. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a book: `book`, `welcome` (queued, first time); name taps play `maker`; then `gust`.
2. Gust!: `gustHow`; piece taps play `piece`; a placement plays `placeYes` then `page` (whole), or `placeNo`; `makerAsk` (whole) once.
3. Words or picture?: `wopHow` (first), `question` (whole), `wopYes` or `wopNo`, then the proof tap and `proofYes` or `proofNo`.
4. Picture tells more: the page words (whole), `ptmAsk` (whole), then `ptmSays` or `ptmYes`.
5. The diagram: `diagramHow`; label taps play `label`; questions as above.
6. `wrap` after the last round of the second book.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.K.6, RL.K.7, RL.1.7, RI.1.6, RI.1.7, RL.2.7, RI.2.7 wording (name the author and illustrator and define the role of each; relationship between illustrations and the story; use illustrations and details to describe characters, setting or events; distinguish information from pictures and words; images such as a diagram showing how a machine works clarify a text) | thecorestandards.org, RL and RI K-2 | CCSS ELA 2010 PDF | yes |
| Wind is moving air; farm windmills pump water; dandelion seeds have a fluffy parachute (pappus) carried by wind | NOAA SciJinks, "What is wind?" and USDA Forest Service, "Dandelion" | National Geographic Education, "Wind" and Britannica, "Windmill" and "Dandelion" | yes |
| Sailboat parts: sail, mast, hull, rudder (the rudder steers) | Britannica, "Sailing" and "Rudder" | US Sailing, "Parts of a sailboat" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b4, 2026-11-08): Words or picture? answers Picture 3, Words 3, Both 2; label orders 5! = 120; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 each round's page and controls show with no scroll; at 680x425 the same with a scrolling table.
2. Makers: both covers' name cards read the name and role; "Who made this picture?" takes only Illustrator. (RL.K.6)
3. Gust!: every picture, photo and caption fits only its page; the page is read when it does. (RL.K.7, RI.1.7)
4. Words or picture?: each of the eight takes only its place and only its proof spot; tokens as described. (RL.1.7, RL.2.7, RI.1.6)
5. Picture tells more: each of the three takes only the picture card; the "words already say that" card plays its own line. (RL.2.7, RI.1.7)
6. The diagram: five labels fit only their spots; the two diagram questions and the "How does it help" question take only their answers. (RI.2.7)
7. Teams: turns alternate as described; Teams: off plays the same rounds with one score.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Pre-reader: every page, piece, caption and card is spoken.
10. Motion off: the gust becomes a fade, pieces move without blowing; no network requests; nothing saved.

## Open questions
- None for Cory.
