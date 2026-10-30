# Research Quest

## One idea
Every shortcut you take while researching comes back as a question you can't answer: you pick a research question, choose four places to look, take notes your way and build an outline for your school's garden council, and on Friday each council member's question traces a line on the quest map straight back to the choice that answers it, or the shortcut that left you stuck.

## Not like
- fake-or-fact-lab (6-8, this group): judges one page at a time by leaving it. Here no source is a hoax; the sources differ in how useful they are for your question, and the payoff comes at the end of a whole project.
- keyword-fishing and boolean-builder (this group): how to search. Here the places to look are given; the skill is choosing among them and keeping what you find.
- credit-card-builder (3-5, this group): building full credits. Here the only source question is whether you wrote one down at all, and quote or own words.
- Research Rover (ela 4), Source Sorter (ela 6), Research Notebook (ela 9), Question Sharpener (ela 12), research family, not built: a rover through articles, credibility sorting, a free notebook, and narrowing a question. Here it is one branching story where the process stages are chapters and the ending is decided by your earlier choices.
- design-for-a-friend (5 CS, wave 1): interview questions shape a design, tested by a test drive. Here the questions come from the audience at the end, and the test is whether your notes can answer them.

## Who and how
- Grades 6 to 8, library. Module: The Research Process (Research), "Plan, gather, organize and present research".
- Driver: students on laptops, alone or in pairs; a teacher can project it and take class votes at each choice. 20 to 30 minutes for one run; a second run (with different choices) takes about 10.
- Standards: AASL.Inquire (I.A.1 formulating questions; I.B.2 devising and implementing a plan to fill knowledge gaps), AASL.Collaborate (presenting findings to a group and answering its questions); C3 D1.5.6-8 (choosing the kinds of sources that will help answer the question), D3.1.6-8 (gathering from several sources, guided by each one's origin and authority). Link: AASL.Engage VI.B.1 (ethically using others' work: quoting and paraphrasing). CCSS ELA: W.6.7, W.7.7, W.8.7 (short research projects to answer a question, drawing on several sources).
- tool.json: driver "students or teacher", minutes "20-30", modes [], grades_label "Grades 6-8".

## Screens and modes
Kit frame, own `:root` (a parchment trail map). Header: title "Research Quest", small line "Five stops to Friday's council"; Motion, Sound, Read. One mode.

Focus: the current chapter card, centered over the map and the biggest thing on screen (at least 60 percent of the stage); the map shows around it so the student always sees where they are. At the end, the Trail back map is the focus.
Stage: the quest map (art rq-trail-map) with a trail through five stops: **1 Ask**, **2 Plan**, **3 Gather**, **4 Organize**, **5 Present**. Your marker (a painted canvas backpack pin, art rq-marker) sits on the current stop and walks the trail when a stop is done. Each finished stop shows a small badge of what you chose (the question card, four place icons, note count, outline). The current chapter opens as a large card over the map (the map dims behind it).
Panel: `#hint`; the **Research pack** (everything collected so far: question card, places visited, note cards, outline), each item openable; **Rewind** (go back to an earlier stop; later stops reset, with a Yes / No check); **Start over**.

### The story
Bramble Hill Middle School's garden club has an empty raised bed (art rq-garden-bed). Principal Okoro says the club can plant it for monarch butterflies if someone brings a researched plan to the Garden Council on Friday. You are that someone. The librarian, Mr. Adeyemi, hands you a pack and points at the map. Mr. Adeyemi is never pictured: his lines appear in a speech card beside his painted library desk (art rq-library-desk).

### Stop 1, Ask
Card: "What will you research?" Four question cards to choose one:
- A "Monarch butterflies." (a topic, not a question)
- B "What do monarch butterflies need from a school garden in our area?" (the researchable one)
- C "Are monarchs the prettiest butterflies?" (opinion)
- D "How many monarchs spend the winter in Mexico?" (researchable, but no help to the garden)
Choosing shows no right or wrong; Mr. Adeyemi says one line per choice (Content) and the card goes in the pack.

### Stop 2, Plan
Card: "You have time for four visits before Friday." Six places as tiles, each with its painted picture (art rq-place-kit); pick four, then **Go**: Library shelf (book), County garden office page, Nature center naturalist (an interview), Garden club notebook (last year's notes), "Top 10 Butterfly Facts" video, Sunny Acres seed ad.

### Stop 3, Gather
For each place visited, a source card shows its passage (Content) with title, author and page or date. Five ways to note it, as buttons: **Copy it, with quote marks**, **Copy it, no quote marks**, and three **In my own words** versions (shown as three choices: one good, one too close to the original, one that changes the meaning; their order is shuffled each run). Then two save buttons: **Save note** and **Save note with its source** (they turn on once a way is chosen). The note card shows exactly what you chose (quote marks or not, the words, and the source line or "no source"). Each source card shows its place's picture (the library card shows art rq-caterpillar instead). **On to Stop 4** turns on when all four places have a saved note; until then the hint says how many are left ("Two places still need a note. Tap a place in your pack.").

### Stop 4, Organize
Your note cards on the left; an outline with three headings on the right: **What monarchs need**, **What our garden has now**, **Our plan**, plus a **Not needed** tray. Drag (or tap a card, then tap a heading) to place every card. Then pick up to three **Plan steps** for "Our plan": Plant native milkweed; Plant flowers that bloom in late summer and fall; Don't spray pesticides; Sprinkle Butterfly Blend seed mix; Count monarchs again next fall. **Done** when every card is placed and at least one plan step is picked.

### Stop 5, Present
The council table (art rq-council-room, an empty table seen from your seat) with three code nameplates on its blank name stands (Principal Okoro; Lily Tran, garden club president, grade 8; Mr. Hale, groundskeeper). The council members are never pictured: a nameplate lights when its person speaks. Your outline shows as three slides. Focus: the speech card with the question and your answer, center stage. Each council question appears in turn in a speech card; your answer is filled in automatically from your pack, or "I'm not sure..." when nothing in the pack answers it. **Next question** steps through. Then the ending card and the **Trail back**: the map returns with a line drawn from each council question to the stop whose choice decided it (green line with ✓ when answered, red dashed with ✗ when not).

## Content
Mr. Adeyemi's line per question choice: A "That's a topic. A topic is a place to start. What do you want to know about it?" B "That's a question you can answer, and it's about our garden." C "People can disagree on that one. Can research settle it?" D "You could find that out. Will it help the garden?"

Passages (places made up; the facts in them are real and sourced):
- Library shelf: "Monarchs and Milkweed", Dana Whitfield, 2022, page 12: "Monarch caterpillars eat only milkweed. Without milkweed plants, monarchs cannot complete their life cycle." Own words: good "Monarch caterpillars need milkweed. It's the only plant they eat, so no milkweed means no new monarchs." / too close "Monarch caterpillars eat just milkweed. Without milkweed plants, monarchs can't complete their life cycle." / changed "Monarch butterflies like milkweed best, but they can use other plants too."
- County garden office: "Planting for Pollinators", Bramble County Garden Office, updated April 2025: "Choose milkweed that is native to our region, such as common milkweed or butterfly weed. Avoid spraying pesticides, which can kill caterpillars." Good "The county garden office says to plant milkweed that grows naturally here, like common milkweed or butterfly weed, and not to spray pesticides." / too close "Choose milkweed native to our region, like common milkweed or butterfly weed. Avoid spraying pesticides that can kill caterpillars." / changed "Any milkweed from any store works, and a little pesticide is fine."
- Nature center: interview with Rosa Delgado, naturalist, Bramble Creek Nature Center, this week: "Adult monarchs drink nectar from lots of different flowers. In late summer and fall they need blooming flowers to fuel their long trip south." Good "Grown monarchs feed on nectar from many flowers, and flowers that bloom late in the year give them energy for migrating." / too close "Adult monarchs drink nectar from many flowers. In late summer and fall they need blooming flowers to fuel their trip south." / changed "Monarchs only visit flowers in the spring."
- Garden club notebook: club notes, last October: "We counted 2 monarchs all fall. There is no milkweed anywhere in our garden." Good "Last fall the club saw only two monarchs, and the garden has no milkweed." / too close "We counted two monarchs all fall. There is no milkweed in our garden." / changed "The club saw lots of monarchs last fall."
- Video: "Top 10 Butterfly Facts", FactBlast channel: "Monarchs can fly up to 3,000 miles to their winter home!" Good "Some monarchs travel as far as 3,000 miles to spend the winter somewhere warm." / too close "Monarchs can fly up to 3,000 miles to their winter home." / changed "Every butterfly flies 3,000 miles each year."
- Seed ad: "Butterfly Blend", Sunny Acres Seeds: "Butterfly Blend brings butterflies to ANY garden, guaranteed! Just sprinkle and wait." Good "A seed company says its mix brings butterflies to any garden." / too close "Butterfly Blend brings butterflies to any garden, guaranteed." / changed "Scientists say Butterfly Blend works in every garden."

Council questions (in this order; each lists what answers it, checked from the pack and outline):
1. Principal Okoro: "What are you asking us to do, and why?" Answered if question B was chosen and the garden club note is under "What our garden has now". Answer shown: your question, then the note.
2. Lily Tran: "Why milkweed? Why not just pretty flowers?" Answered if the library note is under "What monarchs need".
3. Mr. Hale: "Will the plants you want grow here?" Answered if the county garden office note is in the outline and "Plant native milkweed" is a plan step.
4. Principal Okoro: "Where did that fact come from?" (about the first note under "What monarchs need"; if that heading is empty, about the first note anywhere in the outline; if the outline has no notes at all, the answer is "There's nothing in the outline to point to." and it counts as not answered). Answered if that note was saved with its source. If it was copied without quote marks, the answer adds the principal's reply: "Those are the book's exact words. Put them in quote marks and name the book." and it counts as not answered.
5. Lily Tran: "When should our flowers bloom?" Answered if the naturalist note is in the outline and "Plant flowers that bloom in late summer and fall" is a plan step.
6. (Only if any note in the outline used a meaning-changing version) Mr. Hale: "Hold on. Is that really what your source said?" Never answered; the speech card shows the source's real words beside your note.
7. (Only if "Sprinkle Butterfly Blend seed mix" is a plan step) Mr. Hale: "What plants are in Butterfly Blend?" Never answered: "The ad didn't say."
Any too-close note in the outline adds one aside from the principal after the questions (not counted): "Some of your notes sound almost word for word. Try saying it your own way."

Endings (by questions not answered, of those asked):
- 0: "Plan approved! Next week the club plants native milkweed and fall flowers." Art rq-garden-bloom.
- 1 or 2: "Approved, with homework: come back with [the missing pieces, named]." Art rq-garden-bed. The missing piece for each unanswered question: 1 "a clear question and what our garden has now"; 2 "why monarchs need milkweed"; 3 "proof the plants will grow here"; 4 "where your facts came from"; 5 "when the flowers should bloom"; 6 "what your source really said"; 7 "what is in the seed mix". Two pieces are joined with "and".
- 3 or more: "Not yet. The council asks you to dig deeper and come back next month." Art rq-garden-bed.
Each ending is followed by the Trail back and two buttons: **Rewind to a stop** and **Start over**.

## Interactions in detail
- Choices never show right or wrong when made; only the council and the Trail back judge, and only in story terms. No score.
- Stop 2: a fifth tile can't be picked (it shakes; hint "Four visits. Unpick one first."). Go is enabled at exactly four.
- Stop 3: a source can be noted once; **Redo note** replaces it before Stop 4.
- Stop 4: a card can be moved between headings any number of times; three plan steps maximum (a fourth tile is disabled with the reason shown).
- Council: questions play one at a time and each one's text is on screen at once. **Next question** is live the whole time: a tap cuts the current line and shows the next question at once (it never waits for the line to finish). With Motion off, cards appear without sliding.
- The marker's walk between stops takes about 1 s (instant with Motion off) and never blocks a tap.
- Trail back lines are drawn in code over the map art; each line is a button that reopens the stop's choice in a read-only card.
- Rewind: choosing a stop asks "Go back to [stop]? Your choices after it will be cleared." Yes / No. Start over asks the same for the whole quest.
- The run in progress saves in localStorage (`rq-run`, try/catch) so a class period can end mid-quest; Start over clears it. Nothing typed, nothing about the student is kept.
- Keyboard: every choice is a button; drag in Stop 4 has the tap-then-tap alternative; visible focus.
- Sizes: the chapter card's choices and its main button visible without scrolling at 1280x720 and 1366x768; at 680x425 the map shrinks to a five-dot strip above the chapter card and the pack collapses to a count chip; at 375 wide the chapter card fills the width.

## Look
- Accent `--brand #0f766e` (trail teal: header, marker, current stop ring, main buttons). `--head-ink #ffffff`.
- Own `:root` (parchment map): `--paper #f7f1e1`, `--panel #fffaf0`, `--ink #2b2418`, `--muted #6b5d45`, `--line #e3d6b8`, `--btn #0f766e`, `--focus #9d174d`. Note cards white with a teal clip; source line in italic muted; "no source" in muted with a ✗ icon. Trail back: answered #15803d solid with ✓, not answered #b91c1c dashed with ✗ (shape and icon, never color alone). Nameplates brass #8a6a1f with white text.
- Neighbors: conflict-coach green-teal #2f7a62 and career-cluster-explorer light teal #2dd4bf (6-8, other subjects); group siblings olive, crimson, violet, orchid, brass. Map paper and teal set it apart from fake-or-fact-lab's white lab bench.
- Contrast: white on brand 5.47:1; brand on paper 4.85:1; brand on panel 5.26:1; ink on paper 13.61:1; muted on paper 5.68:1; muted on panel 6.16:1; focus on panel 7.58:1 and on paper 6.99:1; white on nameplate brass 5.05:1; answered green on panel 4.82:1; red on panel 6.22:1. All pass AA.

## Art
All local FLUX (`scripts/localart.py`); no people (the four characters speak through nameplates and speech cards). One style: hand-drawn storybook illustration in warm parchment light.
- rq-trail-map: an illustrated parchment map of a small town and school grounds, a winding dotted trail with five empty round clearings along it, a library, a nature center in woods, a garden and a school building, hand-drawn storybook style, blank banners; 16:9; cutout no; people no; the stage map under the code-drawn stop labels, marker path and Trail back lines.
- rq-marker: a small canvas backpack with a teal flap standing on a round map pin, storybook illustration, plain white background; 1:1; cutout yes; people no; your marker on the map, walking stop to stop.
- rq-garden-bed: an empty wooden raised garden bed of bare soil beside a brick school wall, late summer light, storybook illustration; 4:3; cutout no; people no; the story opening and the not-yet and homework endings.
- rq-garden-bloom: the same kind of wooden raised bed beside a brick school wall, full of pink milkweed flowers and purple asters, an orange monarch butterfly on a flower, storybook illustration; 4:3; cutout no; people no; the approved ending.
- rq-caterpillar: a striped yellow, black and white monarch caterpillar eating a broad milkweed leaf, close-up nature illustration; 4:3; cutout no; people no; the library source card.
- rq-library-desk: a school library desk with a tidy stack of books, a green reading lamp, a canvas pack waiting on top and shelves behind, storybook illustration; 4:3; cutout no; people no; beside Mr. Adeyemi's speech card in the opening and at Stop 1.
- rq-place-kit: one shared prompt, "storybook illustration of [a short stack of library books with a ribbon bookmark on a reading table / a desktop computer monitor with a blank bright screen on an office desk, a county map pinned on the wall behind / a small wooden nature center cabin among trees / a worn spiral notebook with a pressed leaf on a garden bench / a tablet on a stand with a blank dark screen / a paper seed packet with a blank front lying on soil]"; pieces: library, county page, nature center, garden notebook, video, seed ad (6); 1:1; cutout no; people no; the six place tiles at Stop 2 and the picture on each source card at Stop 3. Screens and the seed packet front stay blank; the page name, play button and ad words are code over them.
- rq-council-room: a long wooden meeting table in a school library seen from one end, three empty chairs on the far side, three blank wooden name stands, a water pitcher and glasses, afternoon light, storybook illustration; 16:9; cutout no; people no; the Stop 5 background, nameplates in code on the stands.
That is 13 images (6 of them the place kit), none with people. Cards, tiles, outline, speech cards, nameplates, Trail back lines and preview.svg are drawn in code.

## Voice
Bank voice `smooth-narrator` (Algieba), "Say smoothly and warmly, like an audiobook narrator": it tells the story and voices the chapter openings and council questions. No neighbor from `neighbors.py` (fake-or-fact-lab wise-mentor) and no other spec in this batch uses it; its only 6-8 wave user is pressure-point (health). `Curio.voice`, one scope. Passages and note texts are on screen only (Read speaks the open card). How lines are spoken the first time, then only update the hint; event lines play every time and are dropped when stale.
- open (how; the first time the quest opens; stale once a question card is tapped): "The garden club has an empty bed, and Friday the council decides what grows there. Your quest: bring them a plan. Tap a question card to begin."
- ask (how; Stop 1 opens; stale once a card is chosen): "Stop one. Tap the question you will research."
- plan (how; Stop 2 opens; stale once four places are picked): "Stop two. You have time for four visits. Tap four places."
- go (how; the first time exactly four are picked and Go turns on; stale once Go is pressed): "Four places. Press Go."
- gather (how; Stop 3 opens; stale once a way is tapped): "Stop three. Tap one of the five ways to write this note."
- save (how; the first time a way is chosen and the save buttons turn on; stale once a note is saved): "Now press Save note, or Save note with its source."
- organize (how; Stop 4 opens; stale once every card is placed): "Stop four. Tap a note, then tap a heading. Then tap up to three plan steps."
- done (how; the first time Done turns on; stale once it is pressed): "Your outline is ready. Press Done."
- present (how; Stop 5 opens; stale once Next question is pressed): "Friday. The council is waiting. Press Next question to hear them."
- Council questions 1 to 7 (event, spoken each time they come up; stale when Next question is pressed): the seven question lines in Content, each preceded by the speaker's name.
- Mr. Adeyemi's four question replies (event, on each Stop 1 choice; stale when another card is chosen or Stop 2 opens): the four lines in Content.
- Endings (event; stale on Rewind or Start over): the three ending lines in Content, without the bracketed list (the screen shows it).
- trail (how; the first Trail back; stale once a line is tapped): "Each line leads back to the choice that decided an answer. Tap a line to see that choice."

## Family engine
none

## Sources
- AASL, National School Library Standards (2018), Standards Framework for Learners: Inquire I.A.1 and I.B.2, Collaborate, Engage VI.B.1. https://standards.aasl.org/framework/
- U.S. Fish and Wildlife Service, "Monarch" (milkweed is the only food the caterpillars can eat; the eastern population travels up to 3,000 miles in migration; adults feed on the nectar of many flowers during breeding and migration). https://www.fws.gov/species/monarch-danaus-plexippus
- Xerces Society, "Monarch Butterfly Conservation" and "Milkweeds: A Conservation Practitioner's Guide" (plant milkweed native to your region; provide fall-blooming nectar plants; avoid pesticides). https://xerces.org/monarchs
- Common milkweed (Asclepias syriaca) and butterfly weed (Asclepias tuberosa) as native milkweeds: USDA PLANTS Database. https://plants.usda.gov/
- The school, town, people, book, video, ad and garden notes are made up for Curio Class. Which choices answer which council questions, and the ending bands, are the tool's own design.
- Checks run 2026-10-29 (Python model of the council rules): the ideal run (question B, the four useful places, good notes with sources, the right headings, milkweed and fall flower steps) answers all five and is approved; a run with the library quote in quote marks also answers question 4; 200,000 random runs reached all three endings (approved, homework, not yet), 5 to 7 questions asked, at most 7 unanswered. Fixed: question 4 had no answer when the outline held no notes; the homework ending named "missing pieces" with no list (the list is now in Content); Stop 3 had no button to move on (On to Stop 4 added); Next question waited for the voice line.

## Done when
1. A run with question B, the four useful places, good own-words notes saved with sources, a correct outline and the native milkweed and fall flower steps gets all five questions answered and the approved ending.
2. Each council rule in Content can be made to fail on its own (verify each of questions 1 to 5 by changing one earlier choice) and its Trail back line goes to that stop.
3. Questions 6 and 7 appear only under their conditions; the too-close aside appears only when a too-close note is in the outline; question 4 with no notes in the outline shows "There's nothing in the outline to point to."
4. Endings follow the count of unanswered questions exactly (0, 1 to 2, 3 or more); the homework ending names the missing pieces from Content.
5. Stop 2 enforces four visits; On to Stop 4 turns on only when four notes are saved; Stop 4 enforces three plan steps and every card placed; tap-then-tap works without dragging.
6. Rewind clears later stops only; the run survives a reload; Start over (after Yes) clears it.
7. Focus: the chapter card is the largest, central block at 1280x720, 1366x768 and 1920x1080; at Stop 5 the speech card is center stage.
8. Tap while it plays: a tap on Next question while a council line plays cuts it and shows the next question at once; taps during the marker's walk are taken at once.
9. No person is pictured anywhere; all 13 images load; place tiles show their painted pictures with code labels.
10. Chapter choices and their main button visible without scrolling at every size in STANDARDS.md; 375 wide works in `drive.py --host`.
11. Voice: each stop's how line once; council questions spoken as they come and dropped on Next question; endings spoken once per ending; no line names a disabled control; Read speaks the open card; console clean; no network requests; only "Curio Class".
