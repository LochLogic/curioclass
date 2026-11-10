# Then and Now Flip

## One idea
Grandma Ruth turns over picture cards of the same everyday thing from long ago and today (a phone, a music player, a classroom board), the class decides which is Then and which is Now from what they can see, then puts three versions of one thing on a three-step track (when Grandma was little, when a grown-up was in school, now), and finally lays Grandma's school day from 1965 beside their own, so kindergartners see that life changed in steps and that some things stayed the same.

## Not like
- capsule-from-1965 (1, concept): reading real sources for who made them and when. Here objects and eras, sorted and put in order.
- my-life-timeline (1, concept): the child's own life in order. Here things and a long-ago kid's day.
- backpack-pack (K, concept, this batch): sorting by need and want after a trip. Here sorting by time, with three-step order.
- symbol-spotter (K, concept, this batch): finding pictures and hearing what they stand for. Here comparing pictures and putting them in order.
- me-on-the-map (K, built): zooming through places. Here stepping through time.

## Who and how
- Kindergarten, Social Studies (History), module "Then and Now". Standards: D2.His.1.K-2 (create a chronological sequence of multiple events), D2.His.2.K-2 (compare life in the past to life today).
- Driver: teacher on the projector with the class calling "Then!" or "Now!", or one child alone; every card, clue and choice is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Three parts: Flip (three pairs), Three steps (three tracks), My day (four moments). tool.json `modes: ["Flip", "Three steps", "My day"]`, `minutes: "10-15"`, `grades_label: "Grade K"`.
- Nothing is saved; `Print` prints the My day strip with a blank row for a grown-up at home to draw their own school day. Teacher note: asking a grown-up at home is optional, and "a grown-up" can be anyone who cares for the child.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.2.K-2 (compare past and today) | Flip a pair and drag each card to Then or Now; hear the clue that shows which, and one thing that stayed the same | the Then and Now mats and the clue zoom | 2, 3 |
| D2.His.1.K-2 (sequence) | Put three versions of one thing in order on the three-step track | the track with three labeled steps | 4 |
| D2.His.2.K-2 (life then and now) | Lay Grandma's 1965 school day beside your own, moment by moment | the two-row day strip | 5 |

## Screens and modes
Header (kit): title "Then and Now Flip"; `Flip`, `Three steps`, `My day`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A cozy living room. Grandma Ruth sits in an armchair with a box of cards; two cards lie face down on a rug, and below them are two mats: Then (an old clock picture) and Now (a phone clock picture). The welcome is queued (`welcomeAfter: true`): "Hello, I'm Grandma Ruth. These cards show the same thing, long ago and today. Tap a card to flip it." First hint: "Tap a card to flip it." The first tap flips that card and says its name, and cuts the welcome.

**Flip (focus: the two cards).** At 1366x768 the cards are big in the center with the Then and Now mats below and Grandma at the left. At 680x425 Grandma folds to a small face in the corner.
- Tap each card to flip it; its name plays ("A phone.").
- With both flipped, the child drags each to Then or Now (or taps a card, then a mat).
- Right: the card settles and Grandma zooms in on the clue: "See the curly cord and the round dial? That's how phones looked when I was little." Then the stayed-the-same line: "We still use phones to talk to people we love."
- Wrong: the card wobbles back and Grandma says the clue as a question: "Look at the dial. Do phones today have a dial?"
- Three pairs, in order: phone, music player, classroom board.
Both cards in a pair are painted in the same bright style with the same light; the long-ago card is never faded, brown or blurry, so the clue is in the thing itself.

**Three steps (focus: the track).** A path with three big stepping stones labeled with pictures and words: "When Grandma was little" (Grandma as a girl), "When a grown-up was in school" (a teen with a backpack), "Now" (a child like the student). Three cards of one thing lie shuffled above. The child drags each to a stone. Right: it clicks in. Wrong: it wobbles back and Grandma gives the clue for that card ("This one flips open and has buttons. It came after the dial phone, before the phone with a big screen.").
- Phone: rotary dial phone; flip phone; smartphone.
- Music: record player; CD player; music on a phone with earbuds.
- Board: chalkboard; whiteboard with markers; smart board.
When all three are placed, the path lights from left to right and each step's line plays in order.

**My day (focus: two rows of four pictures).** Top row: Grandma's school day in 1965; bottom row: empty frames for "Your day". The child taps each Grandma picture to hear it, then picks the matching picture for their own day from two choices (or "Draw it" on Print). Four moments:
- Getting to school: Grandma walked with her brother (now: the child picks walk, bus or car; "Kids still walk and ride buses. That stayed the same.").
- Lunch: a metal lunch box with a thermos (now: a lunch bag or the school lunch tray).
- Playing: jump rope and hopscotch (now: jump rope or the playground; "Kids still jump rope!").
- Calling Grandpa: a phone on the kitchen wall with a cord (now: a video call on a tablet or phone).
Then Grandma: "Some things changed, and some stayed the same. What's one thing that stayed the same?" with three picture choices (walking to school, the curly-cord phone, a smart board); only walking to school fits, and the line explains why.

**Class mode.** Teacher notes: flip, then have the class call "Then!" or "Now!" before dragging.

## Content
- Pairs and tracks as above; clue and stayed-the-same lines:
  - Phone: clue "the curly cord and the round dial"; same "We still use phones to talk to people we love."
  - Music: clue "the big black record that spins"; same "We still listen to songs and dance."
  - Board: clue "white chalk on a dark board"; same "Teachers still write on a board for the class."
- Eras: Grandma was little in the 1960s, when most home phones had a dial; push-button phones came from 1963 on; flip phones were the most popular phones in the early 2000s; the first iPhone came out in 2007; CDs came out in 1982; whiteboards and smart boards replaced most chalkboards from the 2000s on.
- Teacher note: families differ; some grandparents are young, some children live with grandparents; the eras are Grandma Ruth's, not every grandma's.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The mats and track accept only after the cards are flipped; the hint before then says "Tap a card to flip it." and never names a mat.
- Wrong drops never count against the child; there is no score.
- With Motion off cards flip without turning (the picture swaps) and the path lights all at once.

## Look
- Accent `--brand` #7a4b1e warm sepia brown (header, Grandma's armchair, the track stones' rims); gold #f4c542 (the clue zoom ring, lit path); paper #fbf5ec; ink #2b1a08; muted #6a5a48. Scene: a cozy living room with a rug.
- Contrast (WCAG 2.1, computed): white on brand 7.36:1; brand on paper 6.79:1; ink on paper 15.45:1; muted on paper 6.11:1; ink on gold 10.30:1.
- Never color alone: mats and stones have pictures and words; the card art is the same full color for then and now.
- Different from this batch (forest green, playground blue, brick red, festival purple).

## Art
- Local FLUX (`scripts/localart.py`): the living room (1, 16:9); 9 object cards, all in one bright sticker style with the same light (rotary phone, flip phone, smartphone; record player, CD player, phone with earbuds; chalkboard, whiteboard, smart board) (9, 3:4); card back (1); 1965 lunch box, wall phone with cord, jump rope and hopscotch, and today's choices (8, 4:3).
- People art goes to Gemini (`people: true`): Grandma Ruth (a Black woman in her late sixties with glasses and a cardigan), 5 poses (sitting, pointing, laughing, holding a card, waving); Ruth as a girl in 1965 walking to school with her brother, at lunch, playing hopscotch (3, 4:3); a teen with a backpack (1); "illustrated <subject>, soft gouache, warm light, plain white background"; 3:4; cutout yes.
About 28 images. Drawn in code: mats, stepping stones, the day strip frames.

## Voice
Bank voice `gentle-storyteller` as Grandma Ruth and the narrator (unique in this batch), style: warm grandmother, unhurried. `Curio.voice` with `scope: () => state.mode + ':' + state.item`, `welcomeAfter: true`.
- how `welcome`: "Hello, I'm Grandma Ruth. These cards show the same thing, long ago and today. Tap a card to flip it."
- event `name`: the card's name on flip.
- how `sort` (first pair only): "Now drag each card to Then or Now."
- event, whole, `clue`: the clue line for a right Then card.
- event `same`: the stayed-the-same line.
- event `wrong`: the clue as a question.
- event, whole, `pairs-done`: "You sorted them all! Tap Three steps to put things in order."
- how `track`: "Drag each card to its step: when Grandma was little, when a grown-up was in school, or now."
- event `step-wrong`: the card's ordering clue.
- event, whole, `track-done`: the three step lines in order ("When I was little, phones had a dial. When your grown-up was in school, phones flipped open. Now, phones have a big screen.").
- how `day`: "Tap my picture to hear about my school day. Then tap the picture that matches your day."
- event `day-line`: each Grandma moment.
- event `day-same`: "That stayed the same!"
- event, whole, `ask`: "Some things changed, and some stayed the same. What's one thing that stayed the same? Tap a picture."
- event `ask-result`: the result line for the picked picture.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: flip pairs with two mats, the three-step track, the two-row day strip.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Flip sort | Pick the faded or brown card | Both cards share one full-color style and light. |
| Flip sort | The left card is always Then | Card positions are shuffled per pair. |
| Flip sort | Guess, then swap | Allowed; the wrong drop speaks the clue as a question first, so the child hears why. |
| Three steps | Biggest card first | Sizes are matched; the smartphone isn't the smallest. |
| Three steps | Order on screen | Cards are shuffled each time. |
| Stayed the same | Tap at random | Only walking to school fits; the other two each get a line saying what changed. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap a card: `name`.
2. Both flipped: `sort` (first pair). Drop: `clue` (whole) then `same`, or `wrong`; the next pair waits for `same`.
3. Third pair: `pairs-done` (whole).
4. Track: `track` (first time); wrong drop: `step-wrong`; all placed: `track-done` (whole).
5. Day: `day` (first time); tap a Grandma picture: `day-line`; pick: `day-same` where it fits; then `ask` (whole) and `ask-result`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| D2.His.1.K-2 and D2.His.2.K-2 wording | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Rotary dial phones were the home phone for most families in the 1960s and were gradually replaced by push-button phones, which AT&T introduced as Touch-Tone in 1963 | Wikipedia, Rotary dial and DTMF signaling (checked 2026-11-09) | Smithsonian National Museum of American History, telephone collection | yes |
| Flip phones peaked in the early 2000s; the Motorola Razr was the best-selling phone in the U.S. in 2005, 2006 and 2007 | Wikipedia, Flip phone (checked 2026-11-09) | TIME, coverage of the Razr (cited there) | yes |
| The first iPhone was released June 29, 2007 | Wikipedia, iPhone (1st generation) (checked 2026-11-09) | Apple Newsroom, iPhone launch release (2007) | yes |
| The compact disc was first released in October 1982 | Wikipedia, Compact disc (checked 2026-11-09) | Britannica, compact disc | yes |
| Since the 2000s whiteboards and smart boards have largely replaced chalkboards in classrooms | Wikipedia, Blackboard (checked 2026-11-09) | Britannica, interactive whiteboard | yes |
Backed twice: 6. Cut: 0 (a bike pair was dropped because its era could not be backed twice).

Checks run (Python, scratchpad r1, 2026-11-09): the saved pages contain "From the 1960s onward, the rotary dial was gradually supplanted", "starting in 1963", "2005, 2006 and 2007", "2007|6|29", "October 1982" and "Since the 2000s"; each track has one keyed order of three; the stayed-the-same question has one keyed answer; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 cards and mats fit with Grandma; at 680x425 Grandma folds to a corner.
2. Every card, clue and choice is spoken.
3. Each pair sorts to Then and Now with its clue and stayed-the-same line. (D2.His.2.K-2)
4. Each track takes three cards in order, then lights with its three lines. (D2.His.1.K-2)
5. My day lays Grandma's day beside the child's choices and asks what stayed the same. (D2.His.2.K-2)
6. Then and now cards share one art style.
7. Mats and track are never named before the cards are flipped.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: cards swap without turning; no network requests.

## Open questions
- None for Cory.
