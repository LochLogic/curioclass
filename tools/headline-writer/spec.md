# Headline Writer

## One idea
The student is the headline writer at the Maple Falls Kid Gazette: they read a short news story, type a headline that tells what the whole story is about, drag the three details that prove it into the top of the story (a detail that doesn't support the headline bounces back), and recount it in two sentences for the radio, so they learn that a main idea is what the key details add up to; at press time their headline prints beside one that is too narrow and one that is too broad, and they say why theirs fits.

## Not like
- main-idea-umbrella (2, spec): the main topic of each paragraph under an umbrella. Here a whole story's main idea in the student's own words, plus key details and a recount.
- main-idea-pinboard (3-5, concept): quoting evidence, without RI.3.2. Here headline, proof and recount at grade 3.
- fact-fusion (5, concept): pulling from several sources. Here one story.
- deadline-desk (3-5, spec): writing pieces for a class paper. Here reading a story to find its main idea.
- class-pet-pitch (3, spec): writing from fact cards. Here reading.

## Who and how
- Grade 3, ELA, module "Main Idea and Key Details" (Reading Informational). Standard: RI.3.2.
- Driver: one student or a pair (tool.json `driver: "student"`). Every story sentence is read on tap; typed headlines and recounts are read back by the browser's speech voice.
- Eight stories in order of difficulty, one story per press run. tool.json `modes: []`, `minutes: "10-20"`, `grades_label: "Grade 3"`.
- Nothing is saved; the gallery of printed front pages lasts until the page closes. `Print` prints the student's front pages.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.3.2 (main idea) | Type a headline of 3 to 10 words; Ms. Delgado's checklist asks if it covers the whole story | the headline on the desk with the checklist | 2, 3 |
| RI.3.2 (key details) | Drag three details into the "proves it" box; details that don't back the headline bounce back with a reason | the box filling, bounces with reasons | 4 |
| RI.3.2 (recount) | Pick two sentences from tiles, or type them, for the radio recount | the radio script | 5 |
| RI.3.2 (explain how) | At press time, compare three headlines and finish "Mine fits because..." | the front page with three headlines | 6 |

## Screens and modes
Header (kit): title "Headline Writer"; `Stories`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** The Gazette newsroom: a desk, a press in the back, and editor Ms. Delgado holding a story with a blank headline. A clock on the wall reads "Press in 5 minutes" (decoration only; nothing is timed). First hint: "Tap the story to start reading." The first tap plays the story's first sentence; the welcome is queued after it (`welcomeAfter: true`).

**Read.** Focus: the story (a news column 520 wide, 6 to 9 sentences, each a tap target) with a photo. Tap any sentence to hear it. `Next` goes to Headline.

**Headline.** A headline strip (up to 10 words). Under it, Ms. Delgado's checklist, as three questions with picture icons: "Does it tell about the whole story, not one part?", "Would a reader know what happened?", "Is it short?" The tool checks two things it can check: length (3 to 10 words) and key words (each story has a set of key-word groups in data; the headline must hit at least two groups, with word forms allowed: "garden", "gardens", "gardening"). A headline that hits only one group gets a narrow note: "This tells about one part. What is the whole story about?" The student can always move on after a second try; the proof step teaches the rest.

**Proves it.** Eight detail cards from the story (some key, some interesting but off to the side, one about something else). Drag three into the "proves it" box at the top of the story. Each story marks 3 to 4 key details in data; a non-key card bounces back with its reason ("Interesting, but it doesn't show that the garden fed the town").

**Radio.** Recount the story in two sentences: six sentence tiles (two good, two too detailed, two off) or type your own. Tiles have reasons; typed recounts are read back without judging.

**Press.** The front page prints with three headlines side by side: the student's, a too-narrow one, a too-broad one (from data). The student taps which is which and completes "Mine fits because it..." from three endings (covers the whole story; matches the proof details; isn't too big) or types it. Then the page goes into the gallery.

At 1366x768 the story and the step panel fit side by side; at 680x425 the panel stacks under the story.

## Content
Stories are invented local news set in Maple Falls (a made-up town); any real-world fact inside a story is sourced. Each story: 6 to 9 sentences, a photo, key-word groups, 3 to 4 key details, 4 to 5 non-key details, a narrow and a broad headline, recount tiles.
1. "Library Garden Feeds the Town" (kids grow vegetables for a food pantry).
2. "Bridge Closed for Repairs" (detours, a ferry for walkers).
3. "Monarchs Stop in Maple Falls" (a butterfly stopover on the way to Mexico; monarchs from the east fly to central Mexico for winter).
4. "Snow Day Makes Way for Snow Science" (kids measure snowfall with rulers).
5. "Class Builds a Little Free Library".
6. "Old Mill Becomes a Museum".
7. "Town Counts Its Trees" (volunteers count street trees; trees give shade and clean air).
8. "Kids Help Clean Up Maple Creek" (pick-up day; litter in water can harm fish and birds).
Narrow and broad examples (story 1): narrow "Kids Plant Tomatoes"; broad "Good Things Happen in Town".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Typed headline: plain text, 10 word limit shown as it's typed; read back on `Read mine`.
- Bounces give a reason and return the card; the student can try any card, and the box takes exactly three.
- The key-word check is generous (word forms, plural, -ing) and never blocks after the second try.
- The gallery keeps every front page this session; `Print` prints them.

## Look
- Accent `--brand` #a3262a newsprint red (masthead, header, stamps); gold #f4c542 (proof highlights, the press light); paper #faf8f3; ink #1e1a16; muted #5f5850. Scene: a cozy small-town newsroom with an old press.
- Contrast (WCAG 2.1, computed): white on brand 7.32:1; brand on paper 6.90:1; ink on paper 16.29:1; muted on paper 6.60:1; ink on gold 10.63:1.
- Never color alone: bounced cards shake and show their reason; the three headlines are labeled after the student picks.
- Different from this batch (office green, ink navy, car-wash blue, sticker magenta).

## Art
- Ms. Delgado is a person: people art goes to Gemini (5 poses: hold story, read, nod, point, cheer), "a friendly Latina newspaper editor in her forties with glasses and a pencil behind her ear <pose>, warm illustrated style, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): newsroom (1), "A cozy small-town newsroom with desks and an old printing press, soft gouache, no text"; 16:9; cutout no. Story photos (8), "<kids carrying vegetables to a pantry / a closed river bridge with a small ferry / monarch butterflies on milkweed / ...>, illustrated news photo, soft gouache, no faces in close-up"; 4:3; cutout no.
About 14 images. Drawn in code: column, cards, box, radio, front page.

## Voice
Bank voice `news-reader` as Ms. Delgado (unique in this batch). Typed text is read by the browser speech voice. `Curio.voice` with `scope: () => state.story + ':' + state.step`, `welcomeAfter: true`.
- event, whole, `sentence`: the tapped sentence.
- how `welcome`: "This story goes to print in five minutes and it has no headline. Read it, then write one that tells what the whole story is about."
- how `headlineHow`: "Type your headline in the strip. Then tap Check."
- event `narrow`: "This tells about one part. What is the whole story about?"
- event `goodHead`: "That covers it. Now prove it."
- how `proofHow`: "Drag three details that prove your headline into the box."
- event `bounce`: the card's reason.
- how `radioHow`: "Tell it for the radio in two sentences. Pick tiles or type."
- event `press`: "Stop the presses! Which headline is too narrow, and which is too broad?"
- event `fits`: "Yours fits because {it covers the whole story}."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Headline | Type all the key words | A list of words over 10 words is cut off; a short word list passes the check, but the proof step and the press comparison still teach. The check is a nudge, not a gate. |
| Proves it | Drag every card | The box takes three; non-key cards bounce with a reason (3 to 4 key of 8, so random picks of three all key happen at most 4 in 56 times, computed). |
| Radio | Pick any two tiles | Tiles show reasons; only two of six are good. |
| Press | Guess which is narrow | It's a two-way pick with reasons shown after; it is reflection, not a score. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the story: `sentence` (whole), `welcome` (queued, first time).
2. Headline: `headlineHow`; Check: `narrow` or `goodHead`.
3. Proves it: `proofHow`; bounces: `bounce`.
4. Radio: `radioHow`.
5. Press: `press`, then `fits` (waits).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.3.2 wording | thecorestandards.org, Reading Informational Grade 3 | CCSS ELA 2010 PDF | yes |
| Eastern monarchs migrate to central Mexico for winter and lay eggs on milkweed | US Fish and Wildlife Service, monarch butterfly | National Park Service, monarch migration | yes |
| Street trees give shade and help clean the air | USDA Forest Service, urban forests | Arbor Day Foundation, benefits of trees | yes |
| Litter in water can hurt fish and birds | NOAA Marine Debris Program | US EPA, trash-free waters | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b8, 2026-11-08): random three-card pick all key at most C(4,3)/C(8,3) = 4/56; 8 stories with 3 to 4 key details each; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the story and step panel fit side by side; at 680x425 they stack.
2. The headline strip limits to 10 words and the check matches key-word groups with word forms. (RI.3.2)
3. A narrow headline gets the narrow note; the student can move on after a second try.
4. Proves it takes exactly three cards; non-key cards bounce with reasons. (RI.3.2)
5. Radio accepts two tiles or typed sentences and reads them back. (RI.3.2)
6. Press shows three headlines, asks which is narrow and broad, and completes "Mine fits because". (RI.3.2)
7. The gallery keeps every front page this session and prints.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: bounces become a fade; no network requests.

## Open questions
- None for Cory.
