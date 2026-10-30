# Question Sharpener

## One idea
Every research question has a price: the tool breaks your draft question into the sub-questions it would take to answer, prices each in hours and sources against a 27-hour research season, and tells you when the question is too broad, too narrow or already answered; once a question fits, you run the season week by week and find out whether you left enough slack.

## Not like
- Research Notebook (ela 9, this group): takes notes and cites sources for a question that is given. Here no source is read at all; the question itself is the product, and its cost is the lesson.
- research-quest (6-8 library, wave 1): a story about the research process. Here the student drafts and re-drafts one question and sees its price change with every word.
- Source Portfolio (library 9-12, this group): chooses sources for a question. Here sources are only counted, as a model of how much has been written.
- Enduring Questions (library 9-12, this group): finds the lasting issue under a question you wonder about and reads expert positions. Here the question is a project question and the test is whether it can be finished in a season.
- ad-agency (ela 12) and startup-tycoon: business tycoons. The overlap pass moved this tool off business: the currency is time, not money, and nothing is bought or sold.
- Big Question Chart (K-2) and Research Rover (4), research family, not specced: the class picks a question, or a rover explores a mini library. Here the grade 12 step is choosing scope (place, time, kind of question) and planning the work it costs.

## Who and how
- Grade 12 ELA, module Extended Research Project: "Self-directed research, narrowing and broadening the inquiry".
- Topic line: "writing a research question".
- Standards: W.11-12.7, AASL.Inquire.
- Driver: students alone or in pairs. 20 to 35 minutes (pricing 10 to 15, one season 10 to 15).
- tool.json: driver "students", minutes "20-35", modes [] (two views, not modes), grades_label "Grade 12". Kit starter, own light `:root`.

## Screens and modes
Kit frame. Header: "Question Sharpener", Motion, Sound, Read. Two views as a segmented control: **Price it** and **Run the season** (the second is disabled with the reason "Price a question that fits first" until one does).

**Price it.** Focus: the assembled question and its Price tag (the hours bar against the 27-hour line and the verdict stamp); together they take the center and the widest column, the builder a narrower column at the left. It opens with nothing chosen: the Price tag shows an empty tree and the line "Choose chips to price a question." (A saved last question loads instead, if there is one.)

At the left, the **Question builder**, top to bottom:
1. **Interest**: three big chips, Music, Sports, Food.
2. **Focus**: three chips for the chosen interest (Content), each with its small painted picture (Art) and a "written about: plenty / some / little" tag. The chosen focus's picture also sits beside the assembled question, smaller than the question text.
3. **Kind of question**: four chips, What, How has ... changed, Why, Should.
4. **Where**: around the world, in the United States, in our state, in our town.
5. **When**: throughout history, since 1950, since 2000, this year.
6. **Add our own survey** toggle (shown only for state and town; Content).
The assembled question sits above the builder in large type, rebuilt live ("Why do small music venues close in our town since 2000?"). An **Edit wording** button lets the student retype the sentence freely; the price still comes from the chips, and the line "Priced from your choices, not your wording" appears under it.

Right of the stage, the **Price tag**: the sub-question tree (the question at the root, its sub-questions as branches), each branch with a clock badge (hours) and a book badge (sources), the total hours on a long bar against the 27-hour season line (marks at 23 and 27), and the **verdict** stamp (Content). Under the tag: **What you would need to find out**, one line per sub-question naming the kind of evidence (Content).

Below both, the **Ledger**: every question the student priced this session, one row each (question, hours, sources, verdict), newest on top, up to 20. Tap a row to load it back into the builder.

**Run the season** (for the question loaded when the view opened). Focus: the sub-question bars filling, in the center at full width. A six-week calendar across the top: weeks 1, 2, 4, 5, 6 have 5 hours; week 3 is marked "Exams: 2 hours". Below it, the sub-questions as horizontal bars in the student's order, each filling as hours go in; with a survey, one more bar, **Our survey** (6 hours), joins the list and can be ordered like the rest. Controls: **Up** and **Down** on each bar (or drag) to set the order, **Drop** on each bar (asks Yes / No; a dropped sub-question becomes a named limit in the report), and the big button **Run week n**. Hours pour into bars in order: the first unfinished bar takes hours until full, then the next. At the start of week 4 a card appears: "A source you counted on is checked out. The sub-question you are working on needs 2 more hours." (Content). After week 6, the **Season report** replaces the controls (Content); **Back to pricing** and **Run again** sit under it.

Panel (right): `#hint`, the season's hours (27), a **Why this verdict** box that states the rule that fired in one line, and **Clear ledger** (asks Yes / No).

## Content
The prices are a model, not a measurement: the panel says so once ("These prices are a model of how research scales, not real counts"). No real-world facts are stated or implied; the tool never answers any of its questions.

Interests and focuses. Base sources: plenty 12, some 6, little 3. Each focus has two own sub-questions (S1 is about numbers, S2 about people's views) and four stems; `{where}` and `{when}` are filled from the chips.

| Interest | Focus (base) | What | How has ... changed | Why | Should |
|---|---|---|---|---|---|
| Music | Streaming (12) | What is the most-streamed song {where} {when}? | How has the way people listen to music changed {where} {when}? | Why do listeners pay for streaming {where} {when}? | Should streaming services pay musicians more per play {where} {when}? |
| Music | School music programs (6) | What share of schools have a band {where} {when}? | How have school music programs changed {where} {when}? | Why do some schools cut music programs {where} {when}? | Should every school offer a music program {where} {when}? |
| Music | Small music venues (3) | What is the oldest music venue {where} {when}? | How have places to hear live music changed {where} {when}? | Why do small music venues close {where} {when}? | Should towns help keep small music venues open {where} {when}? |
| Sports | Youth sports (12) | What is the most-played youth sport {where} {when}? | How has youth sports turnout changed {where} {when}? | Why do teenagers stop playing on teams {where} {when}? | Should youth leagues limit travel teams {where} {when}? |
| Sports | Women's leagues (6) | What was the first women's pro league {where} {when}? | How has attendance at women's games changed {where} {when}? | Why has interest in women's leagues grown {where} {when}? | Should women's and men's games get equal air time {where} {when}? |
| Sports | Pickup games in parks (3) | What is the most popular park sport {where} {when}? | How has pickup play in parks changed {where} {when}? | Why do people choose pickup games over leagues {where} {when}? | Should parks save courts for pickup play {where} {when}? |
| Food | School lunch (12) | What is the most-served school lunch {where} {when}? | How have school lunches changed {where} {when}? | Why do students buy lunch or bring their own {where} {when}? | Should students help plan school lunch menus {where} {when}? |
| Food | Food trucks (6) | What was the first food truck {where} {when}? | How have food trucks changed {where} {when}? | Why do cooks start food trucks instead of restaurants {where} {when}? | Should food trucks be allowed to park near restaurants {where} {when}? |
| Food | Community gardens (3) | What is the largest community garden {where} {when}? | How have community gardens changed {where} {when}? | Why do people join community gardens {where} {when}? | Should empty town lots become community gardens {where} {when}? |

Own sub-questions (S1, S2): Streaming "Who listens, and on what?", "What do listeners say they pay for?"; School music programs "Which schools have programs?", "What do teachers and students say?"; Small music venues "Which venues opened and closed, and when?", "What do owners and musicians say?"; Youth sports "Who plays, and who stops?", "What do players and coaches say?"; Women's leagues "What do attendance and viewing numbers show?", "What did leagues and broadcasters decide?"; Pickup games "Who plays, where and when?", "What do players and park staff say?"; School lunch "What is served, and what gets eaten?", "What do students and cafeteria staff say?"; Food trucks "How many trucks are there, and who runs them?", "What do the rules and permits say?"; Community gardens "Where are the gardens, and who tends them?", "What do gardeners and neighbors say?".

Sub-questions by kind (n): What 1 (the question itself); How 3 (S1, S2, "What was it like at the start of the period?"); Why 3 (S1, S2, "Which causes matter most, and how do we know?"); Should 4 (S1, S2, "What would change, and for whom?", "What do people who disagree value?").

Price rules:
- Hours per sub-question h = 3 x P x T. P (where): world 3, United States 2, state 1.5, town 1. T (when): throughout history 3, since 1950 2, since 2000 1.5, this year 1. Total H = n x h, plus 6 with a survey.
- Sources per sub-question S = floor(base x pa x ta), plus 2 with a survey. pa: world 1, United States 1, state 0.5, town 0.2. ta: throughout history 1, since 1950 1, since 2000 0.8, this year 0.3.
- Survey: allowed only for state and town ("A class survey can reach your town or state, not the world").

Verdicts, checked in this order (stamp text, then the Why line):
1. What, base 12 or 6, world or United States: "Already answered". Why: "One reference book or one search answers this. Ask how, why or should."
2. What, otherwise: "Too narrow: one fact". Why: "A single fact isn't a research question. Ask how, why or should."
3. How, this year: "Too narrow: no time to change". Why: "Change needs a span of time. Try since 2000."
4. H over 27: "Too broad". Why: "This needs H hours; the season has 27. Narrow the place or the time."
5. S under 2: "Too narrow: thin shelf". Why, for state and town: "Only S source(s) per sub-question. Widen the place or time, or add a survey."; for world and United States, where no survey is offered: "Only S source(s) per sub-question. Choose a longer time." (6 of the 96 world and United States settings, counted by source base, land here, all with this year; checked, Sources.)
6. H 23 or less: "Researchable: room to spare". H over 23 to 27: "Researchable: no slack". Why: "Fits in the season with 27 minus H hours to spare."

What you would need to find out (one line per sub-question): S1 "Numbers: counts, dates or records"; S2 "Voices: what people involved say"; start-of-period "Background: a source from the start of the span"; causes "Comparison: weigh the causes against each other"; what would change "Effects: who gains and who loses"; who disagrees "Values: the strongest case for the other side".

Season: weeks 5, 5, 2, 5, 5, 5 hours (27). Week 4 surprise: +2 hours on the first unfinished bar in the order. If every bar is already finished (possible only after drops, since the smallest researchable plan is 15 hours and weeks 1 to 3 give 12), the card says instead: "A source you counted on is checked out, but you had already finished that part. No hours lost." Season report (one of): "Answered, with X hours to spare" (all finished, X of 2 or more); "Answered, just" (all finished, under 2 to spare); "Answered in part" (any unfinished or dropped), listing each unfinished sub-question with "Y of Z hours" and a suggested limits sentence: "This paper does not fully answer: {sub-question}." Under it, one line comparing the plan: "You planned H hours. The season needed H plus 2." (or "The season needed H." when the surprise cost nothing).

## Interactions in detail
- Every chip change re-prices at once; with Motion on the bar slides and the stamp drops in (300 ms); with Motion off they change in place.
- The Ledger adds a row only when the price changes and the student pauses 1.5 seconds, or presses **Keep in ledger**, so scrolling through chips does not fill it. Same question twice: the old row moves to the top.
- Edit wording: the free sentence is kept with the ledger row; the price still follows the chips. Ten words or fewer gets a gentle note "Short questions often hide their scope. Check where and when."
- Run the season: Run week is the only way time passes. Each week's hours pour in over 600 ms (instant with Motion off); a tap on Run week, Back to pricing or anything else during a pour finishes that pour at once and acts. Reorder and Drop are allowed before any week. The surprise card needs **OK** before week 4 runs. Fractional hours are kept exactly in quarters (6.75 shows as 6 3/4).
- Survey: turning on the survey and then choosing world or United States turns the survey off and hides the toggle.
- Ending a season with spare hours: the report says where they could go ("Spare hours could go to a second draft or a stronger counterargument.").
- Store: the ledger and the last question save to localStorage `qs-ledger` (try/catch); Clear ledger empties it.
- Keyboard: builder chips are radio groups (arrow keys), then the price tag, then the ledger. In the season, the bars are a list; Alt+Up and Alt+Down move the focused bar.
- Sizes: at 1366x768 and 1280x720 builder and price tag sit side by side, ledger below with its own scroll. At 680x425 the builder collapses to five dropdowns in one row and the ledger becomes a **Ledger (n)** button. At 760 and 375 wide everything stacks: question, builder, verdict, tree, ledger. The season calendar becomes a vertical list at 375.

## Look
- Accent `--brand #6237c8` (violet). Own light `:root`, a planning desk: `--paper #f4f2fa`, `--panel #ffffff`, `--ink #1f1a2e`, `--muted #5a5470`, `--line #d8d2e8`, accent `--brand #6237c8` (violet: chips selected, bar fill, Run week), `--btn #6237c8` with `--head-ink #ffffff`, `--focus #0b6e8a`. Verdict stamps: fits `#1d6b3e`, over or under `#a3261b`, both with a word, never color alone. Selected chips sit on lilac `#ece6fb`.
- The 27-hour line is a dashed ink line; the 23 mark a short tick labeled "slack".
- Neighbors: ad-agency and the other wave 4 tools are still being specced; satire-decoder oxblood, usage-panel ink red, boolean-builder orchid on dark. Group siblings: Research Notebook fountain-pen blue, Portrait in Four Media coral, Source Mixer cyan, Source Portfolio green, Enduring Questions lantern gold. Violet on light lavender paper is new among 9-12 ELA tools.
- Contrast (WCAG 2.1): white on brand 7.24:1; brand on paper 6.53:1, on panel 7.24:1; ink on paper 15.20:1; muted on paper 6.45:1, on panel 7.15:1; focus on panel 5.81:1, on paper 5.24:1; fits on panel 6.51:1; over on panel 7.37:1; ink on lilac 13.87:1. All pass AA.

## Art
Local FLUX (`scripts/localart.py`), no people. 10 images. The price tag, tree, badges, bars, calendar and stamps stay in code (they are the chart); the paintings make each focus a real thing to picture.
- Focus pictures (kit of parts, one image each). Shared prompt: "a warm painted picture of [subject], soft daylight, simple uncluttered composition"; 4:3; cutout no; people no; the focus chip thumbnail (cropped square) and the picture beside the assembled question. Pieces: qs-streaming (a pair of headphones resting on a phone with a dark blank screen, on a bedside table); qs-school-music (a trumpet and a folding music stand in an empty school band room with chairs in rows); qs-small-venue (a tiny empty music club stage with a microphone stand, an amp and string lights); qs-youth-sports (a soccer ball on bright grass in front of a small goal net); qs-womens-leagues (a basketball resting on a polished arena court under bright lights, empty stands); qs-pickup-park (an outdoor park basketball court with a chain net at golden hour, a ball by the line); qs-school-lunch (a cafeteria tray with a sandwich, an apple, carrots and a milk carton with a plain blank label); qs-food-truck (a colorful food truck parked on a city street, its menu board painted plain and blank, side view); qs-community-garden (raised wooden garden beds full of tomatoes and greens, a watering can on the path).
- qs-checked-out: an old library book lying on a wooden desk with a plain blank due-date card sticking out of its pocket; 4:3; cutout no; people no; the week 4 surprise card (the card's words in code).
- Drawn in code: chips, sub-question tree, clock and book badges, the hours bar, season calendar and bars, verdict stamps; preview.svg shows the tree with the 27-hour bar and the qs-small-venue picture.

## Voice
Bank voice `big-sister` (Leda, "Say in a friendly, youthful way, like a helpful older student"): a senior who just finished her own project. No neighbor or batch tool uses it (research siblings: research-notebook calm-professor, portrait-in-four-media knowing-guide, source-mixer news-reader, source-portfolio firm-captain). `Curio.voice`, scope the view, `welcomeAfter: true`. Results are read on screen in the Why this verdict box; each how line speaks only the first time its verdict appears.
- w-price (how; Price it welcome; stale once any price shows): "Tap an interest, a focus and a kind of question. Then tap where and when, and watch the price."
- answered (how; first Already answered; stale when the verdict changes): "A search already answers that one. Tap How, Why or Should instead."
- broad (how; first Too broad; stale when the verdict changes): "That costs more hours than the season has. Tap a smaller place or a shorter time."
- thin (how; first thin shelf at state or town; stale when the verdict changes): "Not enough sources for that. Tap a longer time, or turn on Add our own survey."
- thin-far (how; first thin shelf at world or United States; stale when the verdict changes): "Not enough sources for that. Tap a longer time."
- fits (event; each time the verdict changes into Researchable; stale if the chips change before it plays): "That one fits the season."
- w-season (how; Run the season welcome; stale once week 1 runs): "Use Up and Down to put the sub-questions in order. Then press Run week."
- surprise (event; each week 4 card that costs hours; stale once OK is pressed): "A source is checked out. That costs two more hours. Press OK to go on."
- done (event; each season report; stale on Run again or Back to pricing): "Season's over. Here's what got answered."

## Family engine
research (`kit/research.js`). No family doc exists yet; this is the full description, written so the lower grades can reuse it. Members: Big Question Chart (K-2), Note Card Shuffle (3), Research Rover (4), Fact Fusion (5), Source Sorter (6), Summary Scaffold (ELD 6-8), Research Notebook (9), Portrait in Four Media (10), Source Mixer (11), this tool (12) and Source Portfolio (library 9-12). Each part works alone; a tool loads the ones it needs.

- **Source**: `R.source({id, kind, title, author, date, medium, origin, authority, context, cites: [ids], quotable, citation: {...}, segments: [{id, text, loc}]})`. kind is a short label ("eyewitness", "reference", "chart", "broadcast transcript", "photograph"); medium is text, chart, transcript or image; origin names who first produced the information (two sources with the same origin are not independent); quotable false for summaries of modern works. Lower grades use only title, kind and segments.
- **Shelf and Reader**: `R.shelf(el, sources, {onOpen})` draws source cards; `R.reader(el, source, {onPick, ranges})` lists segments with locators and lets a student pick a segment or a word range inside one (keyboard: arrows to move, Enter to pick).
- **Note**: `R.note({kind: 'quote'|'paraphrase'|'idea', text, from: segId, range})`. `R.closeness(text, sourceText)` returns `{run, reuse}`: the longest run of identical words (lowercased, punctuation stripped) and the share of the source's words of 4 or more letters that reappear. Tools set their own thresholds (grade 9 flags a run of 5 or reuse of 60 percent; grade 6 may flag 4).
- **Board**: `R.board(el, columns, notes, {onMove, empty, crowded})`: columns by sub-question or category, drag or number keys, with readouts for empty and crowded columns.
- **Trace**: `R.trace(sentences, notes, sources)` returns each sentence's status (own idea, no source, one source, synthesis, too close, sides differ) and draws threads from sentence to note to segment in SVG, with a text list as the accessible equivalent.
- **Conflicts and corroboration**: `R.conflicts(pairs)` holds known disagreements between segments; `R.web(sources)` groups sources by origin and returns, for each claim, the number of independent origins that support it (one origin repeated by four pages counts once). Used by Source Portfolio and Source Mixer.
- **Weight**: `R.weights(sources, values)` returns each source's share of an answer and flags any share over a tool's cap (Source Mixer's overreliance warning).
- **Matrix**: `R.matrix(claims, sources, cell)` draws a claims by sources grid with three states (states, differs, silent) for cross-checking (Portrait in Four Media).
- **Cite**: `R.cite(source, style, {loc})` returns the in-text citation and `R.works(sources, style)` the list, for 'mla9' and 'apa7'; it handles authors, editors, chapters in edited books, reprints (APA "Original work published"), web articles, government documents, broadcasts and museum objects. Styles are named in the tool with their editions. Lower grades use `R.cite(source, 'simple')` (title and author).
- **Question**: `R.question(slots, rules)` assembles a question from slots and prices it: sub-questions, hours, sources, verdict and the rule that fired (this tool). `R.season(plan, weeks, events)` runs the week-by-week season.
- **Store**: `R.store(key)` namespaced localStorage with try/catch, `save`, `load` and `clear`.

## Sources
- Researchable questions, narrowing and broadening: CCSS ELA W.11-12.7, https://www.thecorestandards.org/ELA-Literacy/W/11-12/
- AASL National School Library Standards (2018), shared foundation Inquire ("Build new knowledge by inquiring, thinking critically, identifying problems, and developing strategies for solving problems"), https://standards.aasl.org/framework/
- The price model, interests, focuses and stems are written for Curio Class and state no facts about music, sports or food; the source counts are a model, said so on screen.
- Checks run 2026-10-29 (Python, scratch qs.py): every Done when price recomputed and matches (13.5 h, 0 sources, thin; 19.5 h, 2, room; 81 h, broad; 27 h, 4, no slack; 18 h, 3, room). All 288 settings per source base enumerated (3 bases, which the 9 focuses share; 4 kinds, 4 places, 4 times, survey where offered): broad 99, one fact 56, thin 42, no slack 35, room 22, no change 18, already answered 16; every focus has at least 3 researchable settings for each of How, Why and Should. Thin shelf without a survey offered: 6 settings per base set, all at world or United States with this year, so the Why line and the voice no longer offer a survey there (fixed). Smallest researchable plan 15 hours (Why, town, this year, with survey), so the week 4 surprise always finds an unfinished bar unless the student drops some; the no-target card was added. The survey's 6 hours had no bar in the season; Our survey was added. Season run for every researchable setting with no drops: every "room to spare" ends "Answered, with X hours to spare" (22 of 22); "no slack" ends "Answered, just" (14) or "Answered in part" (21). The 27-hour season ends with bar 4 at 19/4 of 27/4 hours and the 18-hour season with 7 to spare, as in Done when. Hours per sub-question are always whole, halves or quarters. Contrast ratios recomputed; all match Look.

## Done when
1. "Why do small music venues close in our town since 2000?" prices at 3 sub-questions x 4.5 hours = 13.5 hours, 0 sources each, stamp "Too narrow: thin shelf"; adding the survey gives 19.5 hours, 2 sources, "Researchable: room to spare".
2. "How has the way people listen to music changed around the world throughout history?" gives 81 hours, "Too broad"; "What is the most-streamed song in the United States this year?" gives "Already answered"; "What is the oldest music venue in our town this year?" gives "Too narrow: one fact"; any How with this year gives "Too narrow: no time to change".
3. "Should youth leagues limit travel teams in our state since 2000?" gives 4 x 6.75 = 27 hours, 4 sources, "Researchable: no slack"; "Why do teenagers stop playing on teams in the United States this year?" gives 18 hours, 3 sources, "room to spare".
4. The survey toggle is absent for world and United States; Why this verdict always names the rule that fired.
5. Season with the 27-hour question in 1: after week 6, sub-questions 1 to 3 are full and sub-question 4 shows 4 3/4 of 6 3/4 hours; report "Answered in part" with the limits sentence. With the 18-hour question: "Answered, with 7 hours to spare".
6. Dropping a sub-question before week 1 lists it in the report as a limit; the season cannot start without at least one sub-question.
7. Ledger keeps up to 20 rows, reloads a row into the builder, survives reload, and Clear ledger (after Yes) empties it; no network requests; console clean.
8. At every size in STANDARDS.md the assembled question, the verdict stamp and Run week are visible without scrolling the page; 375 wide works in `drive.py --host`.
9. Voice: welcome once per view, each how line once, "That one fits the season" every time a question becomes researchable; no thin-shelf line or Why line offers a survey at world or United States; only "Curio Class" appears.
10. Focus: in Price it at 1366x768 the assembled question and the Price tag (bar and stamp) are the widest, central block; in Run the season the bars are.
11. Tapping Run week twice fast, or Back to pricing during a pour, acts at once: the first pour completes instantly and nothing waits on the animation.
12. A season with a survey shows an Our survey bar; dropping bars until all are done by week 3 shows the no-hours-lost surprise card and the plan line without "plus 2".

## Open questions
- [question-sharpener] The overlap pass kept the tycoon format; here the tycoon currency is hours in a research season, not money. Does that meet the reshape, or should the format label change to simulator?
- [question-sharpener] AASL.Inquire is mapped to a grade 12 ELA module. Keep it, or is W.11-12.7 alone the better standards line?
- [question-sharpener] Students choose from 9 focuses only (plus free rewording that does not change the price). Add a "my own topic" path with a self-rated "written about" setting, or keep it closed so every price is predictable?
