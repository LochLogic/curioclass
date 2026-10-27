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
- Standards (CSTA 2026 ids from the module): EK-SYS-SE-12, EK-SYS-IM-13. 2017 crosswalk: 1A-NI-04 (what passwords are
  and why we use them), 1A-IC-18 (keep login information private).
- Reads nothing: icons on every control and card, every fixed line voiced, 60 px targets (the card and the two
  targets are much larger).

## Screens and modes
Header (kit): title "Secret Keeper", small line "Share it, or keep it secret?"; mode buttons "Share or Secret" (eye
and lock icon) and "Who's Asking?" (speech bubble icon); Motion, Sound, Read.

Stage (backdrop art: pet-park; everything else drawn in code or placed art, re-laid per size):
- Pet Park, a pretend online game: a grassy park with a path along the front.
- Left: the Share board, a big cork board on two posts with an open eye sign. Anything pinned here can be seen by every
  player in the park.
- Right: the Secret box, a wooden chest with a big padlock. Three picture slots on the lock show the password (blank
  until one is made in Who's Asking?). Inside it (shown when open) are the cards kept secret.
- Center front: the class's player, Bunny (art), holding the current card up.
- Walkers: four animal players (art: fox Fern, owl Ollie, goose Gus, raccoon Rascal) stroll along the path one at a
  time, about every 6 s, stop at the board, look, and walk on. When they look, a thought bubble shows the board's
  newest card.

Panel:
- `#hint`.
- The card in play, large (picture, with its name under it for the teacher), and a small "card 3 of 10" row of dots.
- Two huge buttons: "Share" (open eye, `#share`) and "Keep secret" (padlock, `#secret`). Drag also works: drag the
  card from Bunny's paws to the board or the box.
- "Start over" (circular arrow), and after all cards: "Look again" (magnifier: every card on the board does its
  passerby check once more).

### Mode 1: Share or Secret (sort, opens first)
Ten cards, one at a time, in a fixed order that mixes the two kinds. The class votes, the teacher taps.
- An OK-to-share card goes on the board: the next walker stops, a thought bubble shows it, the walker smiles, line for
  that card.
- A private card goes on the board: every walker in turn stops and the thought bubble shows it (a house, a phone, a
  cake). Gentle line naming what they now know. The card wiggles with a padlock badge; the hint says how to move it:
  tap the card on the board, then tap Keep secret. It moves into the box. (A private card on the board is never scolded
  and never scored; it is the teaching moment.)
- Any card in the box: the lid opens, the card slides in, the lid shuts. Keeping a share-OK card secret is fine (line
  says so).
- After ten cards: the board and the open box side by side; the summary line names the rule.

### Mode 2: Who's Asking? (showdown)
First, the class makes the secret box's password: a 3 by 3 grid of picture tiles (cat, sun, apple, star, boat, fish,
tree, car, moon); tap three in order; they fill the lock's slots ("Done" button with a check). The password lives only
in the page.
Then six players ask Bunny something, one at a time (the asker walks up, speech bubble with a picture of what they
want). Three huge answer buttons: "Tell" (speech bubble), "Keep it secret" (padlock), "Get a grown-up" (Bear icon).
After the class's answer the asker reacts and the line explains. A small row of six round badges fills as each is
done (no points, no wrong buzzer).

## Content
Cards for Share or Secret (order shown; picture drawn in code; kind; spoken name):
1. Favorite color (paint splotches), share, "your favorite color"
2. Home address (a house with a number 12 on the door and a street sign), secret, "where you live"
3. Favorite animal (a paw print), share, "your favorite animal"
4. Password (a key with three stars), secret, "your password"
5. A drawing you made (a crayon rainbow), share, "a drawing you made"
6. Phone number (a phone with number buttons), secret, "your phone number"
7. Game nickname (a name tag reading "Star Frog"), share, "your game nickname, a made-up name"
8. Full name (a name tag with two lines, first and last), secret, "your first and last name"
9. Favorite food (a slice of pizza), share, "your favorite food"
10. Birthday (a cake with candles and a calendar page), secret, "your birthday"
Rule shown at the end: private things tell who you are, where to find you, or open your things.

Askers for Who's Asking? (asker; what they ask, as a picture; best answers; reaction):
1. Rascal the raccoon, a player you don't know: your password. Keep it secret or Get a grown-up. If Tell: Rascal opens
   the secret box and juggles the cards (comic); the lock's password tiles flip to new blanks and the line says to make
   a new password with a grown-up; the class makes a new one before going on.
2. Fern the fox, your best friend in the game: your password. Keep it secret (even best friends). If Tell: Fern
   giggles; line: now it isn't a secret, make a new one with a grown-up.
3. Ollie the owl, a player you don't know: where you live. Keep it secret or Get a grown-up.
4. Gus the goose: your favorite color. Tell (that's OK to share). Keep it secret is fine too.
5. A prize pop-up (a flashing gift box, no animal): "You won! Tell us your full name and phone number." Get a grown-up
   (best) or Keep it secret.
6. Bear, your grown-up at home (art), helping you log in: your password. Tell is OK: a grown-up at home can know it.
   Get a grown-up also fits (Bear is one).

## Interactions in detail
- Tapping a target with no card in play does nothing (buttons disabled between cards while an animation runs, about
  1.5 s, dimmed not hidden).
- Moving a card on the board to the box: tap it (it lifts), then Keep secret, or drag it. Moving a card from the box to
  the board is also allowed (tap the open box's card, then Share): it then gets the same walker check.
- The next card comes up only when the board has no private card on it, so every private card ends in the box. The
  hint says "Move the card with the padlock to the secret box" until then.
- Walkers: never more than one walking at a time; Motion off, they appear at the board, bubble shows, they disappear
  (same timing).
- Who's Asking? Rascal's Tell branch requires a new password before asker 2 (the password grid reopens).
- Start over in each mode resets that mode. Nothing is stored: no names, no answers, no password; refresh clears all.
- Keyboard: Tab order mode buttons, header, Share, Keep secret, Start over, then cards on the board (to select one);
  in Who's Asking? the three answer buttons; password tiles are a grid (arrows move, Enter picks).
- Sizes: the card and both targets visible without scrolling at every size; at 680x425 the walkers shrink and the
  board and box sit at the stage edges; under 760 wide stack stage over panel with the buttons first.

## Look
- Band K-2, own `:root`: `--paper #f5faf6`, `--ink #14261d`, `--muted #4f6358`, `--line #d5e6da`, `--brand #17633f`
  (evergreen, the accent; header and the Keep secret button), `--focus #c2410c` with a white inner ring, Share button
  sky `#1f5fbf` with white.
- Scene: cork #d9b382, chest wood #7a4a22 with brass #c9a227, park grass from the backdrop.
- Neighbors: robot-dance magenta, computer-builder cobalt; siblings me-vs-the-counter gym orange, snowy-mail-route post
  red, spot-the-ai steel navy, input-or-output teal blue. Evergreen is new among them (network-help-desk's green is
  grade 4 and not a neighbor).
- Contrast: white on header 7.26:1; ink on paper 15.01:1; muted on paper 6.1:1; brand on paper 6.87:1; ink on cork
  8.09:1; white on chest 7.42:1; white on Share sky 6.09:1; focus on paper 4.9:1. Share and Keep secret differ by icon
  and word as well as color.

## Art
- pet-park: "A friendly cartoon park for a children's game, green grass, a curving sandy path along the front, round
  trees and flower beds, a blue sky with soft clouds, open space at left and right, flat bright illustration"; 16:9;
  cutout no; people no; Cloudflare FLUX (scripts/cfart.py); stage backdrop.
- bunny: "A cheerful cartoon bunny game character standing, holding its paws up in front as if holding a card, flat
  bright style, full body"; 3:4; cutout yes; people true (character, Codex scripts/gptart.py, Cory reviews); the class's
  player.
- fern-fox, ollie-owl, gus-goose, rascal-raccoon, bear-grownup: each "A friendly cartoon [animal] game character
  walking, side view, flat bright style, full body" (raccoon: "with a cheeky grin and a little mask stripe, playful not
  scary"; bear: "a kind grown-up bear in a cardigan"); 3:4; cutout yes; people true (Codex, Cory reviews); walkers
  and askers, mirrored in code for the other direction.
Cards, board, box, lock, password tiles, thought bubbles and preview.svg are drawn in code. 7 images.

## Voice
Bank voice `warm-teacher` (Sulafat), "Say warmly and clearly, like a kind kindergarten teacher talking to the whole
class": a calm, safe voice for a privacy topic, no scare. Not used by a CS neighbor (robot-dance lively-host,
computer-builder bright-teacher, teach-the-robot playful-friend) or a sibling.
How (once per page load, then hint only):
1. welcome Share or Secret: "Welcome to Pet Park! Some things are OK to share. Some things we keep secret."
2. "Is it OK to share, or keep it secret? Show me with your thumbs. Then tap Share or Keep secret."
3. "Everything on the board, every player in the park can see."
4. "Tap the card with the padlock. Then tap Keep secret."
5. welcome Who's Asking?: "Players are going to ask Bunny some questions. First, let's make a password for the secret box."
6. "Tap three pictures. That's your password. Then tap Done."
7. "Should Bunny tell? Tap Tell, Keep it secret, or Get a grown-up."
Card names (events, when the card comes up): one per card, "Here's [spoken name]." for all ten, for example
8. "Here's your favorite color." through 17. "Here's your birthday."
Share-OK on the board (event; stale on the next card): 18. "Now everyone in the park knows your favorite color. That's OK to share!" (one line per share card: favorite color, favorite animal, a drawing you made, game nickname, favorite food: lines 18 to 22, same pattern)
Private on the board (event): 23. "Now every player knows where you live. Let's keep that in the secret box." 24. "...
knows your password. Now they could open your box! Let's keep that secret." 25. "... knows your phone number. Let's
keep that secret." 26. "... knows your first and last name. Let's keep that secret." 27. "... knows your birthday.
Let's keep that secret." (each begins "Now every player")
28. "Into the secret box! Only you, and your grown-up, can open it." (private card in the box, event)
29. "You can keep that secret too. That's always OK." (share card in the box, event)
30. "All sorted! We keep secret what tells who we are, where to find us, or opens our things." (event)
Who's Asking? (events): 31. "Rascal wants your password. Rascal is a player you don't know." 32. "Fern is your best
friend. Fern wants your password." 33. "Ollie wants to know where you live." 34. "Gus wants to know your favorite
color." 35. "A prize! It wants your name and phone number." 36. "Bear is your grown-up at home. Bear is helping you log
in." 37. "Good choice! Passwords stay secret, even from best friends." 38. "Oh no, Rascal opened your box! Let's make a
new password with a grown-up." 39. "Now it's not a secret anymore. Let's make a new password." 40. "Good choice!
Players you don't know don't need to know where you live." 41. "Sure! Your favorite color is OK to share." 42. "That's
OK to keep secret too." 43. "Good thinking! A grown-up can help with prizes that ask for secrets." 44. "Yes! Your
grown-up at home can know your password." 45. "Getting a grown-up is always a good idea." 46. "That's everyone! You're
a great secret keeper."
The builder writes lines 8 to 27 out in full in `voice/lines.json` from the patterns above (fixed text, no templates
at run time).

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

## Done when
1. All ten cards come up in order; each target gives the reaction in Content, and walkers' thought bubbles show the
   right card.
2. A private card on the board blocks the next card until it is moved into the box; the moving controls work by tap
   and by drag.
3. Keeping a share card secret plays line 29 and never counts as wrong.
4. Who's Asking?: the password grid makes a 3-picture password; all six askers react to all three answers as written;
   Rascal's Tell forces a new password.
5. Nothing is written to localStorage except the kit Motion setting (check after a full run).
6. Every size in STANDARDS.md: the card and both targets visible without scrolling; 60 px targets.
7. Voice: every line in `voice/lines.json` is fixed text; how-to lines 2, 3, 4, 7 spoken at most once in five actions;
   reaction lines every time, dropped when stale; Read and Sound rules pass with held clicks.
8. Keyboard only completes both modes with visible focus; Motion off keeps timing; console clean.

## Open questions
- Who's Asking? says a grown-up at home may know the child's password (asker 6). Common, but some schools say "only
  share with a parent or teacher". Keep "your grown-up at home", or add "or your teacher"?
- Birthday is on the keep-secret side (Common Sense and the Austin ISD lesson list it). Some K teachers celebrate
  birthdays openly in class; fine to keep as is?
