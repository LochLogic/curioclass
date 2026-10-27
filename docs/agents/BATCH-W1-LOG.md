# Wave 1 spec log

Rules: `docs/agents/BATCH-W1.md`. 75 specs in 14 groups, all outside the core subjects (computer science, arts, media
and careers, health, PE, library), written 2026-10-27 by one agent per group, at most four at once. Nothing is built
yet. Next for these tools: art and voice nights, then build batches (SCALE-PLAN.md steps 4 and on).

## Spec check (2026-10-27)

- **Spec sheet:** `python scripts/spec_sheet.py docs/agents/BATCH-W1.md` shows 0 flags (no missing spec, none over 300
  lines, no em dash, no voice or accent repeated inside a group, no art name asked for twice).
- **Renames applied** with `scripts/rename_tools.py` (concept title, tool folder, tags.csv, this wave's note,
  `docs/agents/overlap/renamed.json`). All are plain phrases with no product or brand name:
  - depth-detective to Near and Far (`near-and-far`)
  - flowchart-factory to Chore Flowcharts (`chore-flowcharts`)
  - story-dress-up to Act It Out (`act-it-out`)
  - meal-and-move-planner to Game Day Fuel (`game-day-fuel`)
  - screen-time-detective to Screen Week (`screen-week`); the overlap note's "My Screen Week" was not taken because the
    weeks are pretend, not the student's
  - fair-use-court to Fair Use Review (`fair-use-review`)
- **Renamed after Cory's pick (2026-10-27):** `robot-mouse-mail` to Snowy Mail Route (`snowy-mail-route`, Pip the
  penguin). Code & Go Robot Mouse is a well-known coding toy doing this exact activity, and computer-builder already has
  a mouse.
- **Voices recast** where near neighbors (same band and subject) shared one: capture-the-flag wise-mentor to
  hs-narrator (ai-evaluator keeps wise-mentor); choreography-board easy-coach to casual-peer (band-practice keeps
  easy-coach); brand-builder knowing-guide to hs-narrator (dance-styles-explorer keeps knowing-guide). All 23 kept
  voices are now in use across the wave; repeats across subjects or bands are expected with 23 voices for 75 tools.
- **Standards:** 13 specs named a secondary code their module did not carry (for example near-and-far adds VA:Re7 for
  its Hogarth mode). `python scripts/overlap/wave_standards.py docs/agents/BATCH-W1.md --apply` added them to
  `data/modules.csv`; every spec now claims exactly its module's codes. No spec dropped a module code.
- **Tags and clashes:** all 75 re-tagged from their specs into `docs/agents/overlap/tags.csv` (24 changed). The rule
  now finds 15 same-band pairs with a wave 1 tool, all on action and setting with different skills; one is a real
  picture clash (misleading-charts and fact-check-desk, both a newspaper fact-check desk in 6-8). See
  `docs/agents/overlap/wave1-gaps.md`.

## Shared engines the specs declare

Build each with its first tool; the siblings use it. None has a family doc yet (only data-desk, graphing and
number-line do), so the first build of each should write `docs/families/<name>.md`.

| Engine | Tools in this wave |
|---|---|
| kit/ml-lab.js | teach-the-robot, biased-bot, leaf-sorter-ai, model-mechanic, ai-evaluator |
| kit/network.js | internet-journey, network-help-desk, packet-race, network-architect |
| kit/security.js | data-defenders, phishing-spotter, capture-the-flag |
| kit/robot.js | snowy-mail-route, traffic-light-coder (and live robot-dance) |
| kit/dance.js | levels-and-pathways, dance-pattern-puzzle, choreography-board, dance-styles-explorer |
| kit/movement.js | fitness-circuit, levels-and-pathways |
| kit/stage.js | stage-blocker, director-s-chair |
| kit/music-studio.js, kit/rhythm.js, kit/instruments.js | song-form-builder, band-practice, music-history-radio, world-music-map |
| kit/data-desk.js | data-table-builder, simulation-studio (screen-week uses pretend data, so not the engine) |
| kit/fact-check.js | fake-or-fact-lab (siblings fact-check-desk and ad-agency build on it) |
| kit/careers.js | career-cluster-explorer (moved out of the live career-match-quiz) |
| kit/perspective.js, kit/art-museum.js, kit/habit-hero.js, kit/feelings.js | city-skyline-studio, art-style-match, goal-tracker, stress-toolkit (feelings only if a later sibling needs it) |

Other notes from the spec agents:
- career-cluster-explorer adds three Occupational Outlook Handbook fields to the shared `careers.json` (see questions).
- brand-builder bundles six more free-license Google Fonts families inside its file.
- game-day-fuel reuses label-detective's food records and lunch-tray-builder's food group keys.
- Several health source URLs and the 2025 AHA choking wording were written from memory; each spec tells its build
  agent to recheck them. Nutrition sources (Dietary Guidelines, USDA FoodData Central, ACSM 2016) are outside the
  approved health source list; NIH ODS backs them where it can.

## Open questions for Cory

Collected from each spec's Open questions section (54).
### Computer science: the ml-lab family (one shared engine) (`cs-ml`, 5)

- **Biased Bot** (`biased-bot`)
  - The teacher notes would name the real-world parallel (face recognition that worked worse for darker-skinned women, Gender Shades 2018). Keep it in the notes only, or leave it out for grade 4?
- **AI Evaluator** (`ai-evaluator`)
  - The concept says "AI-generated outputs". This spec reads that as a model's predictions (pothole flags). If Cory meant generative AI (chatbot answers or image captions to fact-check), that is a different tool built on canned outputs; say which.

### Computer science: the network and security families (`cs-net`, 7)

- **Packet Race** (`packet-race`)
  - The format is a race, but the explore-first rule puts Watch first (packets flowing, tap a router to break it) with Race one tap away. Open on Watch as written, or straight on Race?
- **Data Defenders** (`data-defenders`)
  - The escape room format calls for timed team play; this spec makes the Team timer optional and Off by default, so no team is rushed on the CIA ideas. Keep it off by default, or start at 20 minutes?

### Computer science: K-3 (`cs-k3`, 6)

- **Secret Keeper** (`secret-keeper`)
  - Who's Asking? says a grown-up at home may know the child's password (asker 6). Common, but some schools say "only share with a parent or teacher". Keep "your grown-up at home", or add "or your teacher"?
  - Birthday is on the keep-secret side (Common Sense and the Austin ISD lesson list it). Some K teachers celebrate birthdays openly in class; fine to keep as is?
- **Snowy Mail Route** (`snowy-mail-route`)
  - Title: the overlap pass gave "Robot Mouse Mail", but "Code & Go Robot Mouse" is a well known coding toy that does this exact activity, and computer-builder already has a mouse. This spec renames it "Snowy Mail Route" with a penguin. Cory kept the rename (2026-10-27).

### Computer science: data and people, 4-12 (`cs-data`, 5)

- **Data Table Builder** (`data-table-builder`)
  - The family rule asks for real data with a source. Here the real data is the class's own, and the practice table (Room 4) is made up and labeled so. Keep the made-up sample, or replace it with a small real public table?
- **Simulation Studio** (`simulation-studio`)
  - The data-desk rule asks for public data such as government statistics. This log is a published research data set (Azzalini and Bowman 1990, measured at Yellowstone and distributed in the R package MASS). Its real flaws (the night codes and the corrected column meaning) are the point of the tool. Is that source acceptable?
  - The log has 299 rows, over the family's "under about 200 rows on screen"; the table pages 15 rows at a time. Fine, or trim to the first 10 days (about 200 eruptions; the numbers above would be recomputed)?
  - Old Faithful is a classic for data-desk-distributions (grade 12) too. This spec claims it for simulation-studio; say if you would rather keep it for distributions.
- **Algorithm Audit** (`algorithm-audit`)
  - The unfairness is framed by neighborhood (across the river, less home internet), never by race or family income by name, to keep a 6-8 class discussion calm. Keep it that gentle, or name income directly in the background card?
  - Four board and parent portraits (people: true) for Cory to review. Drop them for name plates only, if fewer people images are preferred.

### Computer science: algorithms and code, 6-12 (`cs-code`, 5)

- **Data Policy Council** (`data-policy-council`)
  - The tool names real laws (FERPA, COPPA, California's SOPIPA) and places the made-up district in California so SOPIPA applies. Keep the real laws, or make the state law generic ("a state student privacy law")?
  - Six portraits (five adults, one teen; Codex, for your review). Keep portraits, or use nameplates with icons only?

### Arts: visual art (`art-visual`, 7)

- **Near and Far** (`near-and-far`)
  - Should Near and Far join the perspective family with vanishing-point-studio and city-skyline-studio (it uses the same camera formula), or stay on its own?
- **Gallery Critique** (`gallery-critique`)
  - Panelist avatars: approve three generated portraits, or use initials only?
  - The Gulf Stream invites readings about race (a Black sailor alone in danger, painted in 1899). The claims above stay with what is visible; should the tool add a curator claim that names this reading, with a museum source?

### Arts: music (`art-music`, 5)

- **Music History Radio** (`music-history-radio`)
  - The stations follow European concert music to 1850, then American popular styles. World-music-map covers other places, so this tool keeps that line. Is that the arc you want, or should a station from outside it (for example West African drumming as a root of the American stations) be added?

### Arts: theater (`art-theater`, 4)

- **Act It Out** (`act-it-out`)
  - The Gingerbread Boy's classic ending has the fox eat him (told gently, beat 12). Keep it, or end with him jumping safely to the far bank?
- **Character Voice Booth** (`character-voice-booth`)
  - Recording inside the tool page's embedded preview needs the iframe to allow the microphone (`allow="microphone"`). Allow it on the tool page, or show "Open full screen to record" in the preview?

### Arts: dance (`art-dance`, 4)

- **Levels and Pathways** (`levels-and-pathways`)
  - The pose figure is shared with the PE movement family (fitness-circuit). This spec puts it in `kit/movement.js` and has `kit/dance.js` build on it, so the site has one dancer model. OK, or should dance keep its own figure?
- **Dance Pattern Puzzle** (`dance-pattern-puzzle`)
  - Folk dances: Mayim Mayim, Seven Jumps and Tinikling are common in US elementary PE and music. Keep these three, or swap one for a dance closer to your students?
- **Dance Styles Explorer** (`dance-styles-explorer`)
  - Eight styles here: ballet, modern, jazz, tap, breaking, Irish step, flamenco, Bharatanatyam. Keep this set, or swap one (for example West African dance or a Native American social dance) for your students?
  - The code dancer stands in for living traditions (breaking, flamenco, Bharatanatyam). OK to ship with the on-screen disclaimer, or should a dancer from each tradition review the demo phrases first?

### Arts: media arts, and CTE 6-8 (`art-media`, 5)

- **Flipbook Studio** (`flipbook-studio`)
  - Keep only Save on this device and Print pages, or also add `Download GIF` (an in-page GIF encoder, about 10 KB of code) so students can keep the animation as a file? It is a download of their own work, not a share code.
- **Career Cluster Explorer** (`career-cluster-explorer`)
  - The three Handbook fields (`edu`, `outlook`, `ooh`) go into the shared `careers.json` that the live career-match-quiz bundles. Rebuilding that file changes a live tool's data (its pay and job numbers stay the same; the new fields are unused there). OK to extend it in place, or should this tool keep its own copy until career-match-quiz is next touched?
- **Workplace Scenarios** (`workplace-scenarios`)
  - Career Ready Practices numbering: the tags use the 2012 list of 12 (CRP1 to CRP12). Advance CTE released a modernized framework in October 2024 and now hosts a 2024 Career Ready Practices document; if the practices were renumbered or reworded, should the tags follow the new list, or drop numbers and show only the plain names?
  - The C choice at stop 4 has a student post an unkind group-chat message (no slur, no names beyond Dev). Fine for grades 6-8, or soften it to "Vent about Dev in the group chat"?

### Health: body, growth and safety (`health-a`, 5)

- **Growing Up Q&A** (`growing-up-q-a`)
  - Question box (concept change): the concept had an anonymous question box stored only locally. Per the wave rule, there is no text box at all. In its place: 21 pre-written real-kid questions, a card pointing to the teacher's paper box, and a teacher button that prints blank slips. OK, or drop the print button too?
  - Default wording: "Girls and boys" (common in district curricula) or "Body parts" (inclusive of every body)? The tool offers both; Cory picks the default.
  - Default topics: Periods and Erections and wet dreams are on by default. Some districts teach these only in grade 5 or in separate groups. Keep them on, or default them off for teachers to turn on?
  - Parent preview: should the tool page carry a line for parents ("Preview every card at this address; nothing your child does is stored")?
- **First Aid Responder** (`first-aid-responder`)
  - An opioid overdose scene (recognize it, call 911, give naloxone if available, CPR if needed; CDC and AHA 2025 cover it) is common in high school health now. Add it as a seventh scene, or leave it out so parents and districts aren't surprised?
  - Race framing for emergencies: the clock is optional (Timer Off) and accuracy is required to finish. Is a timed race the right tone, or should Timer Off be the default?
- **Game Day Fuel** (`game-day-fuel`)
  - Rename to "Game Day Fuel" (the overlap pass's suggestion) as written? The topic line keeps "nutrition and fitness planning".
  - The 2025-2030 Dietary Guidelines came out in January 2026 and changed some advice. This spec uses the 2020-2025 calorie and food group tables; should the build switch to the new edition's numbers where they differ (the build agent would recheck every target)?
  - Athletes are all fictional; there is no "my own week" with the student's age and sex, to keep nothing about the student entered. OK?
- **Health Claim Checker** (`health-claim-checker`)
  - The vaping case uses CDC facts and a made-up shop. Vaping is a topic parents may want to preview; keep it as case 1, or move it later in the shelf?

### Health: choices, stress and relationships (`health-b`, 4)

- **Pressure Point** (`pressure-point`)
  - Should there be a "go along" branch? This spec has none: every path ends in a refusal, and Say nothing only leads to the push. A go-along path is more realistic but means drawing a student character vaping or drinking.
  - Is the alcohol scene (The sleepover) fine for grade 6 by default, or should it start unticked in Teacher settings? A parent might want to see it first.
  - A fifth scene, "a ride home with someone who has been drinking" (calling a parent), is a common refusal-skills lesson; leave it out for 6-8 or add it?
  - Cast drawn in code (this spec) keeps people out of the art queue; Codex portraits would look richer but add about 11 people images for review.
- **Stress Toolkit** (`stress-toolkit`)
  - Keep the 988 line in a 6-8 tool's footer (as in resilience-map), or show only "a trusted adult or your school counselor" and keep 988 inside More help?
  - Should students be able to save their starred toolkit (tool names only, no ratings) on the device with a Clear button? This spec saves nothing and offers Print instead.
  - The worry dump asks students to type a real worry, kept in memory and erased. Fine as is, or should it start with an example worry already typed so no one has to write their own?
- **Relationship Spectrum** (`relationship-spectrum`)
  - Default for Teacher: Friendships and dating (this spec) or Friendships only, so dating is something a teacher turns on? A parent might want to see the dating cards first.
  - The Abusive zone includes threats, isolating and controlling behavior but no physical or sexual harm (physical harm is named only in the Flags glossary; loveisrespect's "pressuring you to have sex" sign is left out entirely for 6-8). Is that the right line?
  - Show the loveisrespect text and phone numbers in the footer, or only "a trusted adult or the school counselor" with loveisrespect inside More help?

### Physical education (`pe`, 7)

- **Target Toss** (`target-toss`)
  - Throwing at the screen: the tool assumes a projector on a wall or a pull-down screen and says never to throw at a TV or touch panel. Is that the right line for classrooms with interactive flat panels, or should the setup card suggest a hoop taped to the wall beside the screen instead?
- **Goal Tracker** (`goal-tracker`)
  - Saving a real log: the wave rules forbid keeping health data beyond the page session, so My goal is a one-sitting "last 7 days" log. A month-long personal tracker would need Save on this device (localStorage with Clear). Keep it session-only, or allow device saving for this tool?

### Library and research (`library`, 6)

- **Fake or Fact Lab** (`fake-or-fact-lab`)
  - S2 shows a realistic edited photo (a shark in a flooded street) as the hoax. It is labelled as an art collage once found. Fine to generate and show, or swap for a less realistic fake?
- **Fair Use Review** (`fair-use-review`)
  - The four real case cards name real people and works (Roy Orbison's "Oh, Pretty Woman", Gerald Ford's memoir, a photo of Prince, Google). They are court-case citations from the Copyright Office's index, not made-up content. Keep them, or describe each case without names?
  - Theo's leans and calls are authored judgments on made-up cases, labelled as one reviewer's view with a not-legal-advice line. Is that framing enough, or should a teacher toggle hide Theo's call and show only his factor reasons?
