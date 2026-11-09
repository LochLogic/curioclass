# Postcard Writer

## One idea
Postcards from the class trip have to be right before Pat the pigeon will carry them, and the class learns why by hearing the friend read each card exactly as it is written: a list with no commas becomes "We saw sharks crabs and seals" ("What's a sharks crab?"), a date with no comma turns into "June thirty-two thousand twenty-seven", and a lowercase month leaves "may" sounding like "may I", so every capital, comma, end mark and spelling the class fixes changes what the friend hears, and the friend's reply shows the card was understood.

## Not like
- sentence-train (k, spec): building one sentence from word cars with a capital engine and an end-mark caboose. Here grade 1 conventions on a whole card: names, months, dates, lists, end marks and spelling patterns.
- owl-wants-more (k-2, spec): adding details to a thin story, then a capitals and end-marks polish. Here the conventions are the whole game, and each one is heard through a literal reading.
- little-book-press (k-2, spec): making a book. Here short real-world messages with a date, a greeting and a sign-off.
- blend-bakery (1, spec): reading words by sound. Here spelling words by common patterns inside writing.
- word-zoo (1, concept): sorting words by part of speech. Here punctuation and capitals.

## Who and how
- Grade 1, ELA, module "Capitals, Punctuation and Spelling" (Language). Standard: L.1.2 (a to e).
- Driver: teacher on a projector or a child alone (tool.json `driver: "either"`). Every card is read on tap and the literal reading is spoken.
- Two parts: `Fix the mail` (six postcards from Room 12's trips, each with mistakes) and `Write my own` (a blank postcard). tool.json `modes: ["Fix the mail", "Write my own"]`, `minutes: "10-20"`, `grades_label: "Grade 1"`.
- Nothing is saved. A child's own card can be printed; the friend's name is typed by the child, so the print screen says "Printing makes a paper postcard. Nothing is kept here." (BASELINE rule 7.)

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.1.2a | Fix lowercase names and months (rosa to Rosa, may to May); in Write my own, the checker asks for them | the card; capital choices | 2 |
| L.1.2b | Add or fix end marks (period, question mark, exclamation point) | the mark tiles | 3 |
| L.1.2c | Add the comma in the date (June 3, 2027) and the commas in a list of single words (sharks, crabs and seals) | a comma tile; gaps glow where a comma could go | 4 |
| L.1.2d | Fix misspelled words with common patterns (fish, jump, like, rain) and frequently occurring irregular words (said, was, they, have, come, of) | three spellings to pick from | 5 |
| L.1.2e | Write my own: untaught words typed by sound are accepted and read as written, without a red mark | the card as typed | 6 |

## Screens and modes
Header (kit): title "Postcard Writer"; mode tabs; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A classroom mailbox on a post, a stack of six postcards with trip pictures, and Pat the pigeon in a mail cap on the box. First hint: "Pick a postcard. Tap the aquarium card to start." The first tap turns that card over with its line; the welcome is queued after it (`welcomeAfter: true`).

**Fix the mail.** Focus: the card's back (1000 x 600): date line top right, the greeting, the message (32 px handwriting-style type), the sign-off; the stamp and address on the right half. Under it: `Read it as written` (the friend's face with a speech bubble) and `Mail it` (a mailbox). The tile row: capital tool, comma, period, question mark, exclamation point, and `Fix spelling`.
- Read it as written: the friend reads the card exactly as printed, with the mistakes acting out (a missing end mark runs on with no breath; a missing list comma joins two words; a lowercase month is read as the everyday word; a misspelled word is read as written), and asks a question about the oddest part.
- To fix: tap a word to capitalize it (a capital tile shows the choices: the word with a capital, as it is); drag a comma or end mark into a gap (gaps glow when a tile is held); tap a word and `Fix spelling` to pick from three spellings.
- Mail it: Pat checks the card. If anything is still wrong, Pat names how many things are left, not where ("Two things still need fixing.") and the class uses Read it as written again. When right, Pat flies off, and a reply postcard comes back from the friend, answering something in the card.

**Write my own.** Focus: a blank card back with the same lines, a tile tray (Dear, names, months, numbers, starters "We saw", "I liked", "It was", picture words from the trips, "and", the comma and marks) and `Type` (keyboard). The checker runs on Mail it and names the first thing to fix with its place glowing. Untaught words typed by sound are read as written and not marked; only the pattern and tricky words in the tray's list are checked for spelling. `Print` prints the front picture and the back.

At 1366x768 the card and tiles fit above the fold. At 680x425 the card is 640 x 384 and the tile row scrolls.

## Content
Room 12's trips; every card is written for Curio Class. (card: the text as printed | the fixes)
1. Aquarium: "june 3 2027 / Dear rosa, / We saw sharks crabs and seals. The fesh swam fast / From Ben" | June; 3, 2027; Rosa; sharks, crabs and seals; fish; end mark after fast (period or exclamation point).
2. Apple orchard: "May 10, 2027 / Dear max, / i picked red green and yellow apples. it was fun! / From Lily" | Max; I; red, green and yellow; It.
3. Science museum: "march 4, 2027 / Dear Grandpa, / Did you know a whale is a mammal. We sed hi to a big robot! / Love, Sam" | March; question mark after mammal; said.
4. Farm: "October 12 2027 / Dear Aunt Jo, / I fed the cows goats and pigs. thay wer hungry! / From Nia" | 12, 2027; cows, goats and pigs; They (one spelling pick that also fixes the capital); were.
5. Fire station (a firefighter dog in the art): "may 5, 2027 / Dear Leo, / We got to sit in the red truck I liked the lit and the bell / From Ava" | May; end mark after truck; light; end mark after bell.
6. Pond: "April 22, 2027 / Dear sam, / We saw frogs ducks and a turtle. Can you cum next time / From Max" | Sam; frogs, ducks and a turtle; come; question mark after time.
Spelling picks (right | two wrong): fesh: fish | fesh, phish. sed: said | sed, sayd. thay: They | Thay, Thae. wer: were | wer, wur. lit: light | lite, lit. cum: come | cum, kum.
Literal readings and the friend's questions:
- "june 3 2027": "June thirty-two thousand twenty-seven? That's a lot of days!"
- "may 5": "May? Like may I? Is that a month?"
- "sharks crabs and seals": "Sharks crabs? What's a sharks crab?"
- "cows goats and pigs": "Cows goats? Is that a cow that's a goat?"
- missing end mark: read on with no pause into the next line, then "Whew! I ran out of breath. Where does that sentence stop?"
- "Did you know a whale is a mammal.": "That sounds like you're telling me, but you're asking. How do I know?"
- "fesh", "lit", "cum", "sed", "thay", "wer": read as written, then "Fesh? What's a fesh?"
- lowercase names: "rosa? Who's that? Names get capitals."
Replies (one per card): "Dear Ben, Sharks are my favorite too! Love, Rosa" and five like it.
Write my own word list for spelling checks: the six pattern words above plus fish, jump, like, rain, play, said, was, they, have, come, of, were, from, friend, and the trip picture words.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Read it as written reads the current card state, so after each fix the reading changes.
- Capital tool: tap any word; a capital where none belongs (We Saw) is allowed and read normally, but Mail it counts it as a thing to fix.
- Commas in lists: both "sharks, crabs and seals" and "sharks, crabs, and seals" are accepted (said in the teacher note on the card: "Both are fine.").
- End marks: where a period or an exclamation point both make sense (card 1, "fast"), both are accepted.
- Mail it: counts remaining fixes and names only the number; a second Mail it with the same count adds one glow hint on the earliest one.
- Write my own: the checker order is date, greeting name, first word capitals, I, end marks, list commas, tray-word spelling; it names the first and glows it.

## Look
- Accent `--brand` #1f4f9a airmail blue (header, card border stripes, stamp frame); gold #f5c542 (stamps, Pat's cap badge); airmail red stripes are decoration only; paper #f7f9fd; ink #141c2c; muted #525b6e. Scene: a classroom mailbox by a sunny window.
- Contrast (WCAG 2.1, computed): white on brand 7.94:1; brand on paper 7.54:1; ink on paper 16.17:1; muted on paper 6.47:1; ink on gold 10.51:1.
- Never color alone: glowing gaps also get a dashed box; fixed spots get a small check after mailing.
- Different from this batch (rose, plum, storybook green, savanna) and the grade 1 and K-2 neighbors.

## Art
Local FLUX (`scripts/localart.py`); no people (friends and writers are names only; trip scenes show animals and places).
- mailbox (1): "A classroom mailbox on a post by a sunny window, soft gouache, no text"; 16:9; cutout no.
- pat (stand, fly, read, cheer: 4): "A friendly gray pigeon in a little blue mail cap with a satchel, <standing / flying / reading a postcard / cheering>, soft gouache, plain white background"; 1:1; cutout yes.
- postcard fronts (6): "<an aquarium tank with sharks and crabs / an apple orchard with red, green and yellow apples / a science museum with a whale skeleton and a friendly robot / a farm with cows, goats and pigs / a red fire truck with a firefighter dog / a pond with frogs, ducks and a turtle>, bright postcard illustration, soft gouache, no text"; 3:2; cutout no.
- friend faces (6, animals for the friends): "A friendly <rabbit / cat / owl / bear / fox / hedgehog> face, soft gouache, plain white background"; 1:1; cutout yes.
- tray pictures (18): "<subject from the trips>, simple soft gouache icon, plain white background"; 1:1; cutout yes.
About 35 images. Drawn in code: card backs, stamps, tiles, gaps, every control.

## Voice
Bank voice `easy-coach` as Pat the pigeon and the friends' readings. Not used by the rest of this batch. `Curio.voice` with `scope: () => state.mode + ':' + state.card`, `welcomeAfter: true`.
- event `card`: "A postcard from the {aquarium}!"
- how `welcome`: "Hi, I'm Pat. I carry the mail, but only when it's right. Let's hear how your friend would read it."
- event, whole, `literal`: the card read exactly as written, then the friend's question.
- event `capital`: "{June}, with a capital." event `mark`: "{Period}." event `comma`: "Comma."
- event, whole, `spellAsk`: "Which spelling is right?" event `spellYes` / `spellNo`: "Yes, {fish}!" / "Let's read that one as written."
- event `left`: "{Two} things still need fixing."
- event `mailed`: "It's right! Off it goes!" then event, whole, `reply`: the friend's reply.
- how `ownHow`: "Write your own postcard. Pick tiles or type. If you don't know how to spell a word, write it the way it sounds."
- event `check`: the first thing to fix ("The month needs a capital." / "Put a comma between the day and the year." / "Where does this sentence stop?" / "Your list needs commas." / "Check the spelling of {said}.").
- event `print`: "Printing makes a paper postcard. Nothing is kept here."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Capitals | Capitalize every word | Extra capitals count as things to fix at Mail it. |
| Commas | Put commas in every gap | Extra commas count; the literal reading pauses at each one, so "sharks, crabs, and, seals" sounds wrong. |
| End marks | Period everywhere | Card 3 needs a question mark and card 6 too; the literal reading of a period on a question says so. |
| Spelling | Pick the longest or the most different | The right spelling is the longest in only three of six picks and ties in two (computed); wrong picks are common phonetic slips. |
| Mail it | Mail again and again | Mail names only how many are left; a repeat adds one glow, so fixing still means finding the rule. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a card: `card`, `welcome` (queued, first time).
2. `Read it as written`: `literal` (whole).
3. Fixes: `capital`, `mark`, `comma`, `spellAsk` (whole) then `spellYes` or `spellNo`.
4. Mail it: `left`, or `mailed` then `reply` (whole).
5. Write my own: `ownHow`; Mail it plays `check` or `mailed`; Print plays `print`.
No line contains a bare letter or letter sound (letters in spelling picks are never named; the picks are read as words).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.1.2 a to e wording (capitalize dates and names of people; end punctuation; commas in dates and to separate single words in a series; conventional spelling for common patterns and frequently occurring irregular words; spell untaught words phonetically) | thecorestandards.org, Language Grade 1 | CCSS ELA 2010 PDF | yes |
| Comma between the day and the year in a US date (June 3, 2027); the comma before "and" in a series is optional | Chicago Manual of Style, commas with dates and the serial comma | Purdue OWL, "Commas" | yes |
| A whale is a mammal (card 3) | Smithsonian Ocean, "Whales" | NOAA Fisheries, "Whales" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b5, 2026-11-08): each card's fixes listed and counted (card 1: 6, card 2: 4, card 3: 3, card 4: 4, card 5: 4, card 6: 4); right spelling longest in three of six, tied in two; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the card back and tile row show with no scroll; at 680x425 with a scrolling tile row.
2. Capitals: each card's names, months, I and first words fix with the capital tool; extra capitals count at Mail it. (L.1.2a)
3. End marks: each needed mark is accepted (both marks where both fit); a period on a question is read as telling. (L.1.2b)
4. Commas: date commas and list commas fix as listed; both list styles accepted. (L.1.2c)
5. Spelling: each pick takes only its right spelling. (L.1.2d)
6. Write my own: an untaught word typed by sound is read as written and not marked; the checker names the first of the listed rules. (L.1.2e)
7. Read it as written: after each fix the literal reading changes to match the card.
8. Mail it: names only the count; a right card plays the reply.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Print: one page with front and back; nothing saved; no network requests. Motion off: Pat appears instead of flying.

## Open questions
- None for Cory.
