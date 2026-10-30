# Secret Keeper

## One idea
In a pretend online game park, whatever the class pins on the share board is read by every animal player who strolls
past, while the secret box opens only with the class's own picture password, so the class sees exactly who finds out
each thing they share, and what happens when a password lands where everyone can read it.

## Not like
- robot-dance (K): commands and debugging; no information or sharing.
- me-vs-the-counter (K, this group): measuring data with a sensor. Here the data is about you, and the question is who
  gets to see it.
- computer-builder (1): hardware; it leaves the account-safety standard to this tool.
- internet-journey (3, spec): a message's path across the internet, with sharing choices at each stop. Here nothing
  travels: it is one park, one board and one box, at kindergarten level, and the only idea is "who can see this?".
- spot-the-ai, snowy-mail-route (this group): AI and arrow paths. The guide here is not a robot on purpose (the group
  already has Bolt, Kip and Bitsy nearby): the class's own bunny player and a park of animal players.

## Who and how
- Grade K, computer science. Module: Public or Private? (Systems and Security).
- Topic line: keeping private information private
- Driver: teacher on a projector. The class votes with a thumbs up (share it) or a finger on the lips (keep it
  secret); the teacher taps the class's choice.
- 10 to 15 minutes. tool.json: driver "teacher", minutes "10-15", modes ["Share or Secret", "Who's Asking?"],
  grades_label "Kindergarten".
- Standards (CSTA 2026 ids from the module): EK-SYS-SE-12, EK-SYS-IM-13; library AASL.Engage (safe sharing of
  information). 2017 crosswalk: 1A-NI-04 (what passwords are and why we use them), 1A-IC-18 (keep login information
  private).
- Reads nothing: icons on every control and card, every fixed line voiced, 60 px targets (the card and the two
  targets are much larger).

## Screens and modes
Header (kit): title "Secret Keeper", small line "Share it, or keep it secret?"; mode buttons "Share or Secret" (eye
and lock icon) and "Who's Asking?" (speech bubble icon); Motion, Sound, Read.

Stage (painted pieces placed over the painted park, re-laid per size; see Art):
- Pet Park, a pretend online game (art: pet-park): a grassy park with a path along the front.
- Left: the Share board (art: share-board), a cork board on two posts; an open eye is drawn in code on its blank top
  sign. Anything pinned here can be seen by every player in the park. Pinned cards are the card cutouts at small size.
- Right: the Secret box (art: chest-closed, swapped for chest-open when it opens). Three picture slots are drawn in code
  on the padlock's blank plate and show the password (blank until one is made in Who's Asking?). Inside the open
  chest sit the cards kept secret.
- Center front: the class's player, Bunny (art: bunny-hold), holding the current card up, large.
- Walkers: four animal players (art: fern-fox, ollie-owl, gus-goose, rascal-raccoon) stroll along the path one at a
  time, stop at the board, look, and walk on (mirrored in code for the walk back). When they look, a thought bubble
  (code) shows the board's newest card.

Panel:
- `#hint`.
- The card's name for the teacher (small copy of the card and its words) and a "card 3 of 10" row of dots.
- Two huge buttons: "Share" (open eye, `#share`) and "Keep secret" (padlock, `#secret`). Drag also works: drag the
  card from Bunny's paws to the board or the box.
- "Start over" (circular arrow), and after all cards: "Look again" (magnifier: every card on the board does its
  passerby check once more).

### Mode 1: Share or Secret (sort, opens first)
Focus: the card in Bunny's paws at the stage center, the largest thing on the stage, with the board on its left and
the box on its right at the same height, so the eye follows the card to where it goes. The panel only names the card.
Ten cards, one at a time, in a fixed order that mixes the two kinds. The class votes, the teacher taps.
- An OK-to-share card goes on the board: the next walker stops, a thought bubble shows it, the walker smiles (a small
  hop in code), line for that card.
- A private card goes on the board: the four walkers come one after another (about 1.5 s each) and each thought bubble
  shows it (a house, a phone, a cake). Gentle line naming what they now know. The card wiggles with a padlock badge;
  the hint says how to move it: tap the card on the board, then tap Keep secret. It moves into the box. (A private card
  on the board is never scolded and never scored; it is the teaching moment.)
- Any card into the box: the chest opens, the card slides in, the chest shuts. Keeping a share-OK card secret is fine
  (line says so).
- After ten cards: the board and the open box side by side, Bunny cheering (art: bunny-cheer); the summary line names
  the rule.

### Mode 2: Who's Asking? (showdown)
Focus: first the password grid, large at the stage center; then the asker and its speech bubble facing Bunny at the
stage center, the largest pair on the stage, with the box and its lock still visible at the right.
First, the class makes the secret box's password: a 3 by 3 grid of picture tiles (art: tile kit: cat, sun, apple,
star, boat, fish, tree, car, moon); tap three in order; they fill the lock's slots ("Done" button with a check,
enabled once three are picked). The password lives only in the page.
Then six players ask Bunny something, one at a time (the asker walks up, a speech bubble in code with a picture of what
they want). Three huge answer buttons: "Tell" (speech bubble), "Keep it secret" (padlock), "Get a grown-up" (Bear's
face icon). After the class's answer the asker reacts (a hop for a good choice, a shrug tilt otherwise, in code) and
the line explains. "Next" (arrow) then brings the next asker. A small row of six round badges fills as each is done
(no points, no wrong buzzer). After the sixth: Bunny cheers and the closing line plays.

## Content
Cards for Share or Secret (order shown; picture from the card kit in Art; kind; spoken name):
1. Favorite color (paint splotches), share, "your favorite color"
2. Home address (a house with the number 12 drawn in code on its blank door plate), secret, "where you live"
3. Favorite animal (a paw print), share, "your favorite animal"
4. Password (a key with three stars on its handle), secret, "your password"
5. A drawing you made (a crayon rainbow), share, "a drawing you made"
6. Phone number (a phone with number buttons), secret, "your phone number"
7. Game nickname (a name tag; "Star Frog" drawn in code on it), share, "your game nickname, a made-up name"
8. Full name (the same name tag with two short lines drawn in code, first and last), secret, "your first and last
   name"
9. Favorite food (a slice of pizza), share, "your favorite food"
10. Birthday (a cake with candles beside a small calendar page), secret, "your birthday"
Rule shown at the end: private things tell who you are, where to find you, or open your things.

Askers for Who's Asking? (asker; what they ask, as a picture; best answers; reaction):
1. Rascal the raccoon, a player you don't know: your password. Keep it secret or Get a grown-up. If Tell: Rascal opens
   the secret box and juggles the cards (comic; the card cutouts circle over his head in code); the lock's password
   tiles flip to blanks and the line says to make a new password with a grown-up; the grid reopens and the class makes
   a new one before going on.
2. Fern the fox, your best friend in the game: your password. Keep it secret (even best friends). If Tell: Fern
   giggles; line: now it isn't a secret, a grown-up can help make a new one.
3. Ollie the owl, a player you don't know: where you live. Keep it secret or Get a grown-up.
4. Gus the goose: your favorite color. Tell (that's OK to share). Keep it secret is fine too.
5. A prize pop-up (art: prize-gift inside a flashing window frame drawn in code, no animal): "You won! Tell us your full
   name and phone number." Get a grown-up (best) or Keep it secret.
6. Bear, your grown-up at home (art: bear-grownup), helping you log in: your password. Tell is OK: a grown-up at home
   can know it. Get a grown-up also fits (Bear is one).

## Interactions in detail
- Controls stay live while anything moves. A card move takes about 0.6 s; a tap on Share or Keep secret during it
  finishes the move at once (the card lands, the next card shows) and is never applied to a card the class has not
  seen. Moving a private card into the box while the walkers are coming stops them at once: the bubbles clear and the
  walker on the path walks on.
- Moving a card on the board to the box: tap it (it lifts), then Keep secret, or drag it. Moving a card from the box to
  the board is also allowed (tap the open box's card, then Share): it then gets the same walker check.
- The next card comes up only when the board has no private card on it, so every private card ends in the box. The
  hint says "Tap the card with the padlock. Then tap Keep secret." until then.
- Walkers between cards: one ambient walker about every 6 s, never more than one on the path; Motion off, they appear
  at the board, the bubble shows, they disappear (same timing).
- Who's Asking?: the answer buttons are live while the asker walks up (about 1.5 s); a tap then places the asker at
  once and answers. Next is live while the reaction line plays; it stops the line and brings the next asker. Rascal's
  Tell branch requires a new password before asker 2 (the password grid reopens, Next hidden until Done).
- Start over in each mode resets that mode. Nothing is stored: no names, no answers, no password; refresh clears all.
- Keyboard: Tab order mode buttons, header, Share, Keep secret, Start over, then cards on the board (to select one);
  in Who's Asking? the three answer buttons and Next; password tiles are a grid (arrows move, Enter picks).
- Sizes: Bunny with the card and both targets visible without scrolling at every size; at 680x425 the walkers shrink
  and the board and box sit at the stage edges; under 760 wide stack stage over panel with the buttons first.

## Look
- Band K-2, own `:root`: `--paper #f5faf6`, `--ink #14261d`, `--muted #4f6358`, `--line #d5e6da`, `--brand #17633f`
  (evergreen, the accent; header and the Keep secret button), `--focus #c2410c` with a white inner ring, Share button
  sky `#1f5fbf` with white.
- Scene (asked of the painter): green grass, sandy path, cork board in warm tan, chest in dark brown wood with brass;
  code pieces near them use cork `#d9b382`, chest wood `#7a4a22`, brass `#c9a227`. Thought and speech bubbles white
  with an ink outline.
- Neighbors: robot-dance magenta, computer-builder cobalt; siblings me-vs-the-counter gym orange, snowy-mail-route post
  red, spot-the-ai steel navy, input-or-output teal blue. Evergreen is new among them (network-help-desk's green is
  grade 4 and not a neighbor).
- Contrast (computed): white on header 7.26:1; ink on paper 15.01:1; muted on paper 6.1:1; brand on paper 6.87:1; ink
  on cork 8.09:1; white on chest 7.42:1; white on Share sky 6.09:1; focus on paper 4.9:1. Share and Keep secret differ
  by icon and word as well as color.

## Art
Local FLUX (`scripts/localart.py`) for all; no people (the players are animals). One flat, bright picture-book style
for everything, asked for in one session.
- pet-park: "A friendly cartoon park for a children's game, green grass, a curving sandy path along the front, round
  trees and flower beds, a blue sky with soft clouds, wide open lawn at left and right, flat bright picture-book
  illustration"; 16:9; cutout no; people no; stage backdrop.
- share-board: "A big cork notice board on two wooden posts with a blank pale wooden sign across the top, plain cork
  surface, flat bright picture-book illustration, plain white background"; 4:3; cutout yes; people no; left of the
  stage; eye sign and pinned cards placed in code.
- chest-closed: "A sturdy dark brown wooden treasure chest with brass corners, lid shut, a big brass padlock on the
  front with a smooth blank brass plate, flat bright picture-book illustration, plain white background"; 4:3; cutout
  yes; people no; right of the stage; password slots drawn in code on the plate.
- chest-open: the same chest with the lid swung open, a dark empty inside, the padlock hanging open; 4:3; cutout yes;
  people no; swapped in while a card goes in and while the box is open.
- bunny-hold: "A cheerful cartoon bunny game character standing, front view, both paws raised in front of its chest
  as if holding up a card, flat bright picture-book illustration, full body, plain white background"; 3:4; cutout yes;
  people no; center front; the card sits in its paws.
- bunny-cheer: the same bunny with both paws thrown up high and a big smile; 3:4; cutout yes; people no; end of each
  mode and good choices in Who's Asking?.
- Players, one prompt pattern: "A friendly cartoon [animal] game character walking, side view, flat bright picture-book
  illustration, full body, plain white background"; 3:4; cutout yes; people no; walkers and askers, mirrored in code:
  fern-fox (an orange fox), ollie-owl (a round brown owl), gus-goose (a white goose with an orange beak),
  rascal-raccoon ("with a cheeky grin and a dark mask stripe, playful"), bear-grownup ("a kind grown-up brown bear in a
  green cardigan, standing, front view").
- prize-gift: "A shiny wrapped gift box with a big red bow and gold sparkles around it, flat bright picture-book
  illustration, plain white background"; 1:1; cutout yes; people no; inside the pop-up window (frame and words in code).
- Card kit (9 pieces, one prompt: "A single [object], centered, flat bright picture-book illustration, plain white
  background"); 1:1; cutout yes; people no; the card in Bunny's paws, pinned cards, box cards, thought bubbles and the
  panel copy; each sits centered on a white rounded card drawn in code at 80 percent of the card's width: paint-splotches
  (three paint splotches, red, blue and yellow), little-house (a small house with a smooth blank plate beside the door),
  paw-print, star-key (a golden key with three stars on its handle), crayon-rainbow (a child's crayon rainbow on
  paper), button-phone (a phone with a grid of round blank buttons), name-tag (a blank white name tag sticker with a red
  band), pizza-slice, birthday-cake (a cake with lit candles beside a small blank calendar page). name-tag serves cards
  7 and 8.
- Tile kit (9 pieces, one prompt: "A simple cute [object] icon, centered, flat bright picture-book illustration, plain
  white background"); 1:1; cutout yes; people no; the password grid and the three lock slots: tile-cat, tile-sun,
  tile-apple, tile-star, tile-boat, tile-fish, tile-tree, tile-car, tile-moon. Tile frames drawn in code.
Board sign, lock slots, bubbles, badges, the pop-up frame, words and preview.svg are drawn in code. 30 images, 0 with
people.

## Voice
Bank voice `warm-teacher` (Sulafat), "Say warmly and clearly, like a kind kindergarten teacher talking to the whole
class": a calm, safe voice for a privacy topic, no scare. Not used by a CS neighbor (robot-dance lively-host,
computer-builder bright-teacher, teach-the-robot playful-friend) or a sibling. `Curio.voice`, `scope: () =>
state.mode`. Read speaks `#hint`. Every line below is fixed text in `voice/lines.json`.
How (spoken the first time its moment comes, then hint only):
1. w-share (Share or Secret entered; stale on the first Share or Keep secret tap): "Welcome to Pet Park! Some things
   are OK to share. Some things we keep secret."
2. vote (first card shown, queued after 1; stale when that card moves): "Is it OK to share, or keep it secret? Show me
   with your thumbs. Then tap Share or Keep secret."
3. board (first card that lands on the board, before its line; stale on the next card): "Everything on the board,
   every player in the park can see."
4. move (first private card on the board, after its line; stale when it is in the box): "Tap the card with the
   padlock. Then tap Keep secret."
5. look (first time the summary shows, after line 30; stale on Look again or Start over): "Tap Look again to watch the
   players read the board one more time."
6. w-ask (Who's Asking? entered; stale when Done is tapped): "Players are going to ask Bunny some questions. First,
   let's make a password for the secret box."
7. pick (queued after 6; stale when Done is tapped): "Tap three pictures. That's your password. Then tap Done."
8. answer (first asker arrives; stale when an answer is tapped): "Should Bunny tell? Tap Tell, Keep it secret, or Get a
   grown-up."
9. next (first reaction line ends; stale on Next): "Tap Next to meet the next player."
Card names (event, when the card comes up; stale when it moves):
10. "Here's your favorite color." 11. "Here's where you live." 12. "Here's your favorite animal." 13. "Here's your
password." 14. "Here's a drawing you made." 15. "Here's your phone number." 16. "Here's your game nickname, a made-up
name." 17. "Here's your first and last name." 18. "Here's your favorite food." 19. "Here's your birthday."
Share card on the board (event; stale on the next card):
20. "Now everyone in the park knows your favorite color. That's OK to share!" 21. "Now everyone in the park knows your
favorite animal. That's OK to share!" 22. "Now everyone in the park can see the drawing you made. That's OK to share!"
23. "Now everyone in the park knows your game nickname. That's OK to share!" 24. "Now everyone in the park knows your
favorite food. That's OK to share!"
Private card on the board (event; stale when it is in the box):
25. "Now every player knows where you live. Let's keep that in the secret box." 26. "Now every player knows your
password. They could open your box! Let's keep that secret." 27. "Now every player knows your phone number. Let's keep
that secret." 28. "Now every player knows your first and last name. Let's keep that secret." 29. "Now every player
knows your birthday. Let's keep that secret."
Box and end (event):
30. (all ten sorted; stale on Start over) "All sorted! We keep secret what tells who we are, where to find us, or opens
our things." 31. (private card into the box; stale on the next card) "Into the secret box! Only you, and your
grown-up, can open it." 32. (share card into the box; stale on the next card) "You can keep that secret too. That's
always OK."
Who's Asking? asker intros (event, when the asker arrives; stale when answered):
33. "Rascal wants your password. Rascal is a player you don't know." 34. "Fern is your best friend. Fern wants your
password." 35. "Ollie wants to know where you live. Ollie is a player you don't know." 36. "Gus wants to know your
favorite color." 37. "A prize! It wants your name and phone number." 38. "Bear is your grown-up at home. Bear is
helping you log in."
Reactions (event; stale on Next or Start over), by asker and answer:
39. Rascal, Keep: "Good choice! Your password stays secret." 40. Rascal, Tell: "Oh no, Rascal opened your box! Let's
make a new password with a grown-up. Tap three new pictures. Then tap Done." 41. Fern, Keep: "Good choice! Passwords
stay secret, even from best friends." 42. Fern, Tell: "Now it's not a secret anymore. A grown-up can help you make a
new one." 43. Ollie, Keep: "Good choice! Players you don't know don't need to know where you live." 44. Ollie, Tell:
"Oops! Now Ollie knows where you live. Next time, keep that secret." 45. Gus, Tell: "Sure! Your favorite color is OK
to share." 46. Gus or Bear, Keep: "That's OK to keep secret too." 47. Prize, Grown-up: "Good thinking! A grown-up can
help with prizes that ask for secrets." 48. Prize, Keep: "Good choice! A prize doesn't need your name and phone
number." 49. Prize, Tell: "Uh oh! Prizes that ask for secrets can be tricks. Next time, get a grown-up." 50. Bear,
Tell: "Yes! Your grown-up at home can know your password." 51. Rascal, Fern, Ollie, Gus or Bear, Grown-up: "Getting a
grown-up is always a good idea."
52. (after the sixth reaction; stale on Start over) "That's everyone! You're a great secret keeper. Tap Start over to
play again."
Which line when: a card comes up, its name line (10 to 19); on the board, 3 the first time, then 20 to 29; into the
box, 31 or 32. An asker arrives, its intro (33 to 38), then 8 the first time; after the answer, its reaction (39 to
51), then 9 the first time.

## Family engine
none.

## Sources
- CSTA K-12 CS Standards (2017) 1A-NI-04, 1A-IC-18: https://csteachers.org/k12standards/ ; 2026 ids from
  data/standards/csta-2026-ids.txt.
- Common Sense Education, Digital Citizenship lesson "Private and Personal Information" (full name, home address,
  birthday and passwords as information to keep private):
  https://www.commonsense.org/education/digital-citizenship/lesson/private-and-personal-information
- Austin ISD Grade 2 adaptation of Common Sense "That's Private!" (full name, birth date, address, telephone number,
  passwords kept private): https://austinisd.org/sites/default/files/dept/pe-health/docs/HSR/HSR_Grade2_AlternativeLessons.pdf
- FTC consumer advice for parents (keep street addresses and phone numbers private; COPPA consent for under 13):
  https://consumer.ftc.gov (Protecting Kids Online)
- Code.org CS Fundamentals Course E, Lesson 8 "Private and Personal Information": https://curriculum.code.org/csf-20/coursee/8/
- Cards, characters and askers are original to Curio Class.
- Checks run (Python, 2026-10-29): the ten cards alternate five share and five secret (every share and private card
  has one board line, 20 to 24 and 25 to 29); each of the six askers has a line for each of the three answers
  (18 pairs, all mapped to lines 39 to 51); every contrast ratio in Look recomputed with the WCAG 2.1 formula and
  matches.

## Done when
1. All ten cards come up in order in Bunny's paws; each target gives the reaction in Content, and walkers' thought
   bubbles show the right card.
2. A private card on the board blocks the next card until it is moved into the box; the moving controls work by tap
   and by drag.
3. Keeping a share card secret plays line 32 and never counts as wrong.
4. Who's Asking?: the password grid makes a 3-picture password; all six askers react to all three answers with the
   lines mapped in Voice; Rascal's Tell forces a new password before Next shows.
5. Focus: at 1366x768 and 680x425 Bunny with the card is the largest thing at the stage center in Share or Secret, and
   the asker with its bubble in Who's Asking?; the board and box stay visible.
6. Tap while it plays: Share or Keep secret mid-move lands the card at once; Keep secret during the walker parade stops
   it at once; an answer during the asker's walk-up answers at once; Next during a reaction line stops the line; no
   stale line plays afterwards.
7. Nothing is written to localStorage except the kit settings (check after a full run).
8. Every size in STANDARDS.md: Bunny's card and both targets visible without scrolling; 60 px targets.
9. Voice: every line in `voice/lines.json` is fixed text; how lines 2, 3, 4, 8 and 9 spoken at most once in five
   actions; card, board, box and reaction lines every time, dropped when stale; no line names a disabled control (7
   plays before Done is enabled but names it as the step after); Read and Sound rules pass with held clicks.
10. Keyboard only completes both modes with visible focus; Motion off keeps timing; console clean.

## Open questions
- Who's Asking? says a grown-up at home may know the child's password (asker 6). Common, but some schools say "only
  share with a parent or teacher". Keep "your grown-up at home", or add "or your teacher"?
- Birthday is on the keep-secret side (Common Sense and the Austin ISD lesson list it). Some K teachers celebrate
  birthdays openly in class; fine to keep as is?
- The first draft had no reaction for Tell on Ollie or the prize, and none for Keep on Bear; lines 44, 49 and 46 were
  added so every answer speaks. Fern's Tell line no longer says "let's make a new password" (nothing on screen made
  one); it now says a grown-up can help. Fine?
