# Class Pet Pitch

## One idea
The class wants a pet, and Principal Hedge will decide, but only after reading two things made from the same stack of fact cards: a care guide that explains the pet and a poster that argues for it; writing both shows the difference between the two jobs, because a guide groups facts under headings and never says "you should", while a poster picks only the facts that work as reasons and links each one to an opinion, and the principal's reactions (a frown for a reason with no fact, a shrug for a fact with no link, a raised eyebrow for "you should" in a guide) say exactly which job slipped.

## Not like
- author-s-mailbox (2, spec): sorting other authors' texts by purpose. Here writing two texts with two purposes from one set of facts.
- first-next-last (1, spec): a robot testing a how-to, story or opinion built from cards. Here grade 3 informative and opinion pieces with headings, a defined word and linking words, typed by the student.
- hamburger-paragraph (2, built): paragraph parts. Here two whole pieces compared.
- quote-picker (4, concept): quotes behind reasons. Here facts behind reasons.
- headline-writer (3, spec): main idea of someone else's news story. Here the student's own writing.

## Who and how
- Grade 3, ELA, module "Opinion and Informative Writing" (Writing). Standards: W.3.1, W.3.2.
- Driver: one student or a pair (tool.json `driver: "student"`). Fact cards are read on tap; typed text can be read back by the browser's speech voice (BASELINE rule 4).
- Three pets (guinea pig, betta fish, leopard gecko); for each: `Care Guide`, `Poster`, `Principal's Office`. tool.json `modes: []`, `minutes: "25-40"`, `grades_label: "Grade 3"`.
- Saving: drafts are kept in this browser (localStorage, try/catch) so a class can finish over two days; the footer says "Your writing stays on this device." `Clear my work` removes it. `Print` prints both pieces as a two-page spread.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.3.2a | Care Guide: type an opening that names the pet; drag fact cards under headings (Food, Home, Daily Care, Good to Know); add the pet picture | the guide page with headings | 2 |
| W.3.2b, c | Add facts under every heading; link facts in one section with also, another, and, more, but | the linking word chips between facts | 2, 3 |
| W.3.2a | Add a "What it means" box for one word from the facts (nocturnal, habitat, social, vitamin C) | the box beside the section | 3 |
| W.3.2d | Type a closing | the guide's last line | 2 |
| W.3.1a | Poster: type one opinion sentence and pick three reason cards | the poster with three reason bands | 4 |
| W.3.1b, c | Back each reason with a fact card and snap a linking word to it (because, since, for example, therefore) | each band's fact and link | 4, 5 |
| W.3.1d | Type a closing line that returns to the opinion | the poster footer | 4 |
| W.3.1, W.3.2 | Principal's Office: hear both read aloud and see her reactions | reaction stamps by each line | 6 |

## Screens and modes
Header (kit): title "Class Pet Pitch"; `Pets`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** The school office door with Principal Hedge the hedgehog holding a sign: "Pet requests need two things: a care guide and a poster." Three pet crates. First hint: "Tap a pet to start its request." The first tap opens the pet with its line; the welcome is queued after it (`welcomeAfter: true`).

**Fact stack.** Every screen has the pet's fact stack on the left: 12 illustrated fact cards (each 220 x 120, a picture and one sentence, read on tap). The same stack feeds both pieces.

**Care Guide.** Focus: a guide page (640 x 820, scrolls inside on short screens): title, opening box, four heading sections, a picture slot, a "What it means" box, closing box. Drag facts under headings (any number; each fact once). Between two facts in a section, a link chip slot accepts also, another, and, more, but. Typed boxes take up to 300 characters. `Check my guide` runs the guide checks and shows sticky notes, one per problem, in this order: no opening; a heading with no facts; a fact under the wrong heading (each fact card has a home heading in data); a section with two facts and no link; no word explained; no closing; and any typed box containing "you should", "you must" or "best pet" (the note: "A guide explains. Save that for the poster!").

**Poster.** Focus: a poster (620 x 860): opinion box at the top, three reason bands, footer box. Each band takes a reason card (the reasons are short claims from data: "Guinea pigs are friendly", "A guinea pig is quiet", "Guinea pigs need a friend"), a fact card under it, and a link chip in front of the fact (because, since, for example, therefore). `Check my poster` notes, in order: no opinion (an opinion box without "should", "I think", "best", "would be" or "great" gets "Is this your opinion?"); fewer than three reasons; a reason with no fact; a fact that doesn't back its reason (data pairs); a missing link; no closing; a closing that doesn't name the pet.

**Principal's Office.** Principal Hedge reads the guide, then the poster, aloud (her voice for her lines; the browser's speech voice for the student's typed text, with each sentence lit). Reaction stamps appear by lines: a smile for each backed reason, a frown for a reason with no fact, a shrug for a fact on the poster with no link, a raised eyebrow for "you should" in the guide. At the end she gives a decision card. The decision depends only on the checks (all pass: "Request approved, pending the weekend plan!"), and every pet's stack includes one fact that needs a plan (who feeds the gecko over a long weekend); the student types one line for it.

At 1366x768 the fact stack and the page fit side by side. At 680x425 the stack becomes a drawer.

## Content
Fact cards (written for Curio Class; home heading in brackets). Reasons the poster offers are listed after.
**Guinea pig:** eats hay every day [Food]; needs fresh vegetables and vitamin C, because its body can't make its own [Food]; needs fresh water every day [Food]; lives in a roomy cage with soft bedding [Home]; likes a hidey house to feel safe [Home]; is social and is happier with a guinea pig friend [Good to Know]; squeaks and whistles to talk [Good to Know]; its teeth never stop growing, so it chews hay to wear them down [Daily Care]; needs its cage cleaned often [Daily Care]; can live 5 to 7 years [Good to Know]; is awake in the day [Good to Know]; needs someone to care for it on weekends and holidays [Daily Care]. Word to explain: social. Reasons: friendly; quiet; awake in the day, when we are; easy to hold gently.
**Betta fish:** eats small pellets once or twice a day [Food]; needs warm water, about 78 to 80 degrees Fahrenheit, with a heater [Home]; needs a filter and a tank of at least 5 gallons [Home]; male bettas must live alone because they fight [Good to Know]; can breathe some air from the surface [Good to Know]; needs part of its water changed every week [Daily Care]; likes plants to rest on [Home]; can live 3 to 5 years [Good to Know]; is colorful and has long fins [Good to Know]; should not be overfed [Food]; needs a light on a timer [Daily Care]; needs someone to feed it on long weekends [Daily Care]. Word: habitat. Reasons: quiet; fun to watch; small space; one fish is enough.
**Leopard gecko:** eats live insects, like crickets and mealworms [Food]; needs a calcium powder on its insects [Food]; needs a warm side and a cool side in its tank [Home]; needs a hide box [Home]; is nocturnal, mostly awake at dusk and night [Good to Know]; can drop its tail to escape, and it grows back [Good to Know]; can live 15 years or more [Good to Know]; needs its tank spot-cleaned every day [Daily Care]; should be held gently and not by the tail [Daily Care]; sheds its skin [Good to Know]; needs a shallow water dish [Food]; needs care over long weekends [Daily Care]. Word: nocturnal. Reasons: quiet; doesn't need a big tank; interesting to learn about; gentle.
Each reason has 1 or 2 backing facts in data (guinea pig "friendly" is backed by "is social"; "awake in the day" by "is awake in the day").

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Facts can be dragged between sections and back to the stack; links attach to the gap between facts.
- Checks list problems in a fixed order and show at most three notes at a time, each pointing at its spot; the student fixes and checks again. No score.
- Typed text: plain text only; the browser speech voice reads it in the Principal's Office and on `Read mine`. If no speech voice exists, the text is shown lit sentence by sentence with no audio.
- Drafts autosave per pet; `Clear my work` asks once.

## Look
- Accent `--brand` #2a6b5e school-office green (header, headings, poster frame); gold #f4c542 (smiles, stars, the approved stamp); paper #f4faf8; ink #10261f; muted #4b5f58. Scene: a sunny school office with a bulletin board.
- Contrast (WCAG 2.1, computed): white on brand 6.24:1; brand on paper 5.91:1; ink on paper 15.07:1; muted on paper 6.46:1; ink on gold 9.79:1.
- Never color alone: reaction stamps are faces with words; guide and poster have different shapes (a booklet, a tall poster).
- Different from this batch (newsroom navy, car-wash blue, newsprint red, sticker magenta).

## Art
Local FLUX (`scripts/localart.py`); the principal is a hedgehog, so no people art.
- office (1): "A sunny cartoon school office with a bulletin board and three pet crates, soft gouache, no text"; 16:9; cutout no.
- Principal Hedge (5, sign, read, smile, frown, eyebrow): "A friendly hedgehog school principal with reading glasses <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- pets (3): "A realistic <guinea pig / betta fish / leopard gecko>, natural history illustration, plain white background"; 4:3; cutout yes.
- fact card pictures (36): "<a guinea pig eating hay / a betta tank with a heater / a gecko on a warm rock / ...>, simple soft gouache"; 4:3; cutout no.
About 45 images. Drawn in code: guide, poster, chips, stamps, notes, controls.

## Voice
Bank voice `calm-professor` as Principal Hedge (unique in this batch). Student text is read by the browser speech voice. `Curio.voice` with `scope: () => state.pet + ':' + state.part`, `welcomeAfter: true`.
- event `pet`: "A {guinea pig} request!"
- how `welcome`: "Hello! I'll decide about a class pet after I read two things: a care guide that explains it and a poster that argues for it. Use the same facts for both."
- event, whole, `fact`: the fact card.
- how `guideHow`: "Drag facts under the right headings, link them, explain one word, and write an opening and a closing."
- event `guideNote` (one per note): "{This heading has no facts yet.}" / "A guide explains. Save that for the poster!"
- how `posterHow`: "Write your opinion, pick three reasons, back each with a fact, and link them."
- event `posterNote`: "{This reason needs a fact behind it.}" / "Is this your opinion?"
- event `smile` / `frown` / `shrug` / `eyebrow`: "Good reason." / "Where's the fact?" / "How does that fact help your opinion?" / "Is a guide supposed to tell me what to do?"
- event `decision`: "Request approved, pending the weekend plan! Who will care for {the guinea pig} on long weekends?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Guide headings | Put all facts under one heading | Every fact has a home heading; misplaced facts get a note. |
| Poster reasons | Use any fact as backing | Only data pairs back a reason (1 or 2 of 12 facts per reason, computed). |
| Poster opinion | Type anything | The opinion check looks for opinion words; a fact sentence gets "Is this your opinion?" (it is a gentle prompt, not a gate). |
| Guide | Copy the poster's opinion into the guide | "You should", "you must" and "best pet" are flagged in guide boxes. |
| Links | Any chip anywhere | Chips only attach between facts or before a backing fact; "therefore" before a backing fact gets "Therefore comes after the reasons, in the closing." |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a pet: `pet`, `welcome` (queued, first time).
2. Tap a fact: `fact` (whole). Guide: `guideHow` (first time); Check: `guideNote` per note.
3. Poster: `posterHow`; Check: `posterNote` per note.
4. Office: the guide and poster read aloud with `smile`, `frown`, `shrug` or `eyebrow` at stamped lines, then `decision`.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.3.1 and W.3.2 wording | thecorestandards.org, Writing Grade 3 | CCSS ELA 2010 PDF | yes |
| Guinea pigs need daily hay, fresh vegetables and vitamin C (they cannot make it), have ever-growing teeth, are social, and live about 5 to 7 years | RSPCA, guinea pig care | VCA Animal Hospitals, "Guinea pigs: care" | yes |
| Bettas need warm water (about 78 to 80 degrees F) with a heater and filter, a tank of at least 5 gallons, males kept alone, can gulp air at the surface, live about 3 to 5 years | VCA Animal Hospitals, betta fish care | PetMD, betta fish care | yes |
| Leopard geckos eat live insects dusted with calcium, need a warm and cool side and a hide, are mostly crepuscular or nocturnal, can drop and regrow tails, and can live 15 to 20 years | VCA Animal Hospitals, "Leopard geckos: care" | RSPCA, leopard gecko care | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: classroom pets are a welfare question; every stack includes the weekend and holiday care fact, and the decision card asks for that plan.

Checks run (Python, scratchpad b8, 2026-11-08): 12 facts per pet with at least 2 per heading; backing facts per reason 1 or 2; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the fact stack and the page fit side by side; at 680x425 the stack is a drawer.
2. Guide checks find each listed problem and pass a complete guide with an opening, four filled headings and a closing. (W.3.2a, b, d)
3. Link chips attach between facts; the word box takes its word and meaning. (W.3.2a, c)
4. Poster checks find each listed problem and pass a poster with an opinion, three backed reasons and a closing. (W.3.1a, b, d)
5. Link chips before backing facts read aloud in place. (W.3.1c)
6. The Principal's Office reads both pieces and places reaction stamps by the lines that earned them.
7. Drafts survive a reload where storage works; `Clear my work` removes them; the tool runs without storage.
8. Print gives a two-page spread.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: stamps appear without bouncing; no network requests.

## Open questions
- None for Cory.
