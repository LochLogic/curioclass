# Batch note: spec wave 1, outside the core subjects (2026-10-27)

Cory asked for the first spec wave from the scale plan (`docs/agents/SCALE-PLAN.md` step 3): 75 tools, starting
outside the core subjects. This wave is every remaining computer science, arts, health and PE, and library tool, plus
the two grade 6-8 career tools. It ends at the spec check; builds, art and voice come later, wave by wave.

The overlap pass is done and Cory decided every cluster (`docs/agents/overlap/choices.json`). Accepted fixes are
already in `data/concepts/*.txt`, so `scripts/neighbors.py` shows the new titles and concepts. Fixes Cory left for the
spec are in the per-tool notes below: settle them in your spec.

Left for wave 2 (outside the core): CTE 9-12 (9), world languages (18: ASL needs Deaf signers on video, Spanish needs
a Spanish voice, and two ids carry accents), ELD (15).

## How this wave runs

Spec agents each take one group below (one subject area, families kept together) and write every spec in it, so the
group's tools differ from each other by design. Then the integrating session runs the spec check over the whole wave
(`python scripts/spec_sheet.py` puts every spec's one idea, accent, voice and art on one page).

## Rules for this wave (on top of SPEC.md and STANDARDS.md)

- **One spec per tool,** at `tools/<id>/spec.md`, with exactly the sections in SPEC.md. Write nothing else.
- **Topic line.** A tool with a topic line in its notes shows it under the title on the tool page. Put it in "Who and
  how" as `Topic line: ...`. Any tool whose title doesn't name its topic gets one too.
- **Title changes.** If you rename a tool (an overlap note, a trademark, a clearer name), keep writing to
  `tools/<old-id>/spec.md`, put the new title in the `#` heading and add `Renamed from: <old title>` under it. The
  integrating session moves the folder and the concept line. Keep the topic word in the title. Check every title
  against trademarks (Jenga, Mad Libs, Brain Gym and Bee-Bot were all caught): no product or brand names.
- **Families.** Only data-desk has a family doc (`docs/families/data-desk.md`). For any other family in your group,
  design one shared engine and describe it in "Family engine" the same way in every sibling's spec (the lowest grade
  sibling holds the full description, the others say what they feed it). Built siblings (robot-dance, loop-garden in
  robot) are the reference: read their src.html before writing.
- **Voice.** Narration uses `Curio.voice` (docs/KIT.md "Voice"). In "Voice", mark each line `how` (spoken once, then
  hint only) or `event` (spoken every time it happens), and say when an event line goes stale. Pick a different bank
  voice for each tool in your group, and different from the nearest built neighbors (`voices/bank.json`, status
  "kept" only). hs-narrator already speaks for ten tools: use it only when nothing else fits.
- **Look.** Each tool its own accent, different from its group siblings and neighbors, AA ratios stated.
- **Art.** Short lists; diagrams, charts, cards and simple objects drawn in code. People and characters: Codex
  (`scripts/gptart.py`), marked `people: true`, Cory reviews. Scenes and props: Cloudflare FLUX.2 (`scripts/cfart.py`).
  Real artworks: public-domain images from open-access collections (The Met, Art Institute of Chicago, National
  Gallery of Art, Rijksmuseum), each with its collection URL in "Sources". No two tools in your group ask for the same
  image.
- **No network, no accounts, nothing stored about a student.** Everything runs in the page. Save means localStorage
  with a Clear button. Never collect names, questions, health data or recordings beyond the page session. Microphone
  or camera only if the tool can't work without it, kept in memory, never saved, with a no-mic path.
- **K-2 reads nothing:** teacher led on a projector, icons on every control, every fixed line voiced, 60 px targets.
- **9-12 works like the real thing,** minimal celebration.
- **Facts.** Every number, rule and claim on screen has a source in "Sources". Health and first aid: CDC, NIH,
  American Heart Association, American Red Cross, SHAPE America or the National Health Education Standards. Computer
  science: CSTA 2017 standards plus a named reference. Arts: the National Core Arts Standards plus the source for each
  fact about a work, artist or style.
- **Health topics** (vaping, alcohol, dating, puberty, stress): factual, calm, inclusive, no scare tactics, no
  graphic content. Point to a trusted adult or the school counselor; crisis lines only if sourced (988 Suicide and
  Crisis Lifeline). Anything a parent might want to see first goes in "Open questions" for Cory.
- **Security tools** teach defense with made-up systems inside the page only. No real-world attack steps, no real
  sites or brands in phishing examples.
- **Music** is synthesized in the page (Web Audio) from public-domain melodies or original ones; no recordings unless
  public domain with a source.
- **Open questions** go at the end of the spec under `## Open questions` (only things Cory must decide).
- Plain words, no em dashes, "Curio Class" never "Curio" alone.

## Groups and per-tool notes

### Computer science: the ml-lab family (one shared engine) (`cs-ml`, 5)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| teach-the-robot | Teach the Robot | 2 | lab | ml-lab |
| biased-bot | Biased Bot | 4 | lab | ml-lab |
| leaf-sorter-ai | Leaf Sorter AI | 5 | lab | ml-lab |
| model-mechanic | Model Mechanic | 6-8 | lab | ml-lab |
| ai-evaluator | AI Evaluator | 9-12 | lab | ml-lab |

- **leaf-sorter-ai:** Topic line under the title on the tool page: "train and test a classifier". Reshaped by the overlap pass (Cory accepted, the concept above is the new one). The clash it fixed: Trains and tests a classifier like biased-bot one grade down; fruit also put it beside kitchen-lab. Family: stays in ml-lab.

### Computer science: the network and security families (`cs-net`, 7)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| internet-journey | Internet Journey | 3 | story | network |
| network-help-desk | Network Help Desk | 4 | mystery | network |
| packet-race | Packet Race | 6-8 | race | network |
| network-architect | Network Architect | 9-12 | builder | network |
| data-defenders | Data Defenders | 5 | escape | security |
| phishing-spotter | Phishing Spotter | 6-8 | arcade | security |
| capture-the-flag | Capture the Flag | 9-12 | escape | security |

- **network-help-desk:** Topic line under the title on the tool page: "wired and wireless networks, logging in". Reshaped by the overlap pass (Cory accepted, the concept above is the new one). The clash it fixed: One of four detective mysteries in 3-5. Family: stays in network.

### Computer science: K-3 (`cs-k3`, 6)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| me-vs-the-counter | Me vs the Counter | k | data | - |
| secret-keeper | Secret Keeper | k | sort | - |
| robot-mouse-mail | Robot Mouse Mail | 1 | puzzle | robot |
| spot-the-ai | Spot the AI | 1 | showdown | - |
| input-or-output | Input or Output? | 2 | sandbox | - |
| traffic-light-coder | Traffic Light Coder | 3 | builder | robot |

- **me-vs-the-counter:** Topic line under the title on the tool page: "how computers collect and count data". Reshaped by the overlap pass (Cory accepted, the concept above is the new one). The clash it fixed: Runs the same class vote as class-poll (g1 math); its CS codes are unique, so the slot stays and the angle moves to the computer. Family: Leaves class-poll on purpose: the class vote is the clash itself, and K-2 has one teacher for both tools.

- **robot-mouse-mail:** Topic line under the title on the tool page: "coding a path with arrow commands". Reshaped by the overlap pass (Cory accepted, the concept above is the new one). The clash it fixed: Programs a creature through a garden like the live loop-garden and robot-dance; 'Bee-Bot' is a TTS product name. Family: stays in robot.

- **spot-the-ai:** Topic line under the title on the tool page: "what AI is and how it learns patterns". Reshaped by the overlap pass (Cory accepted, the concept above is the new one). The clash it fixed: With its action corrected it matches teach-the-robot on skill, action and setting.

- **input-or-output:** Topic line under the title on the tool page: "computer inputs and outputs". Reshaped by the overlap pass (Cory accepted, the concept above is the new one). The clash it fixed: Same skill and setting (a desktop computer's parts) as the live computer-builder.

### Computer science: data and people, 4-12 (`cs-data`, 5)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| data-table-builder | Data Table Builder | 4 | data | data-desk |
| simulation-studio | Simulation Studio | 9-12 | data | data-desk |
| misleading-charts | Misleading Charts | 6-8 | mystery | - |
| design-for-a-friend | Design for a Friend | 5 | roleplay | - |
| algorithm-audit | Algorithm Audit | 6-8 | roleplay | - |

### Computer science: algorithms and code, 6-12 (`cs-code`, 5)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| chore-flowcharts | Flowchart Factory | 6-8 | builder | - |
| code-kitchen | Code Kitchen | 6-8 | puzzle | - |
| sorting-showdown | Sorting Showdown | 9-12 | simulator | - |
| api-playground | API Playground | 9-12 | sandbox | - |
| data-policy-council | Data Policy Council | 9-12 | roleplay | - |

- **flowchart-factory:** Topic line under the title on the tool page: "flowcharts and pseudocode". Overlap note (left for you to settle in the spec): A second 'Factory' title in 6-8 beside function-machine-factory; the factory is only in the title, so the concept stands. Suggested fix (rename): "Chore Flowcharts". Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title.

### Arts: visual art (`art-visual`, 7)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| near-and-far | Depth Detective | 3-5 | puzzle | - |
| art-style-match | Art Style Match | 3-5 | cards | art-museum |
| design-fixer | Design Fixer | 6-8 | puzzle | - |
| art-through-time | Art Through Time | 6-8 | timeline | art-museum |
| gallery-critique | Gallery Critique | 9-12 | roleplay | art-museum |
| city-skyline-studio | City Skyline Studio | 9-12 | studio | perspective |
| virtual-gallery | Virtual Gallery | 9-12 | builder | - |

- **depth-detective:** Topic line under the title on the tool page: "perspective and space in art". Overlap note (left for you to settle in the spec): One of twelve 'Detective' titles. Suggested fix (rename): "Near and Far". Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title.

### Arts: music (`art-music`, 5)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| song-form-builder | Song Form Builder | 3-5 | builder | music-studio |
| world-music-map | World Music Map | 6-8 | map | instruments |
| band-practice | Band Practice | 6-8 | race | rhythm |
| theory-gym | Theory Gym | 9-12 | puzzle | - |
| music-history-radio | Music History Radio | 9-12 | timeline | - |

- **song-form-builder:** Spec note from the overlap pass: Spec check: AB and ABA forms also appear in dance-pattern-puzzle (3-5); keep the music on form and the dance on movement.

### Arts: theater (`art-theater`, 4)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| act-it-out | Story Dress-Up | k-2 | showdown | - |
| character-voice-booth | Character Voice Booth | 3-5 | lab | - |
| stage-blocker | Stage Blocker | 6-8 | builder | stage |
| director-s-chair | Director's Chair | 9-12 | story | stage |

- **story-dress-up:** Topic line under the title on the tool page: "pretend play and acting out a story". Overlap note (left for you to settle in the spec): 'Story' beside story-stage and my-story-strip in K-2. Suggested fix (rename): "Act It Out". Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title.

- **director-s-chair:** Overlap note (left for you to settle in the spec): Switching interpretations of a classic scene repeats globe-theatre-stage in 9-12. Suggested fix (reshape): "Director's Chair": Stage the same short scene as a Greek chorus, Noh, commedia, Elizabethan and modern realist production; compare what each tradition's staging rules make the audience notice.. Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title. Family: stays in stage.

### Arts: dance (`art-dance`, 4)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| levels-and-pathways | Levels and Pathways | k-2 | showdown | dance |
| dance-pattern-puzzle | Dance Pattern Puzzle | 3-5 | puzzle | dance |
| choreography-board | Choreography Board | 6-8 | studio | dance |
| dance-styles-explorer | Dance Styles Explorer | 9-12 | explorer | dance |

- **levels-and-pathways:** Topic line under the title on the tool page: "locomotor and nonlocomotor movement". Reshaped by the overlap pass (Cory accepted, the concept above is the new one). The clash it fixed: Copying moves from the board, like the live animal-moves and beat-buddies. Family: stays in dance.

- **choreography-board:** Overlap note (left for you to settle in the spec): Places performers on a top-down stage like stage-blocker in 6-8. Suggested fix (reshape): "Choreography Board": Build a dance on a timeline of movement phrases (counts, levels, dynamics), then revise it; formations show in a side view as the phrases play to music.. Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title. Family: stays in dance.

### Arts: media arts, and CTE 6-8 (`art-media`, 5)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| flipbook-studio | Flipbook Studio | 6-8 | studio | - |
| storyboard-studio | Storyboard Studio | 9-12 | studio | - |
| brand-builder | Brand Builder | 9-12 | builder | - |
| career-cluster-explorer | Career Cluster Explorer | 6-8 | explorer | careers |
| workplace-scenarios | Workplace Scenarios | 6-8 | story | - |

### Health: body, growth and safety (`health-a`, 5)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| body-systems-tour | Body Systems Tour | 3-5 | explorer | - |
| growing-up-q-a | Growing Up Q&A | 3-5 | explorer | - |
| first-aid-responder | First Aid Responder | 9-12 | race | - |
| game-day-fuel | Meal and Move Planner | 9-12 | builder | food |
| health-claim-checker | Health Claim Checker | 9-12 | mystery | - |

- **meal-and-move-planner:** Topic line under the title on the tool page: "nutrition and fitness planning". Overlap note (left for you to settle in the spec): Plans workouts like fitness-program-designer in 9-12 health; FITT programming stays with that tool. Suggested fix (reshape): "Game Day Fuel": Plan a week of meals around your training days; the tool tracks energy in and out, flags gaps and extremes, and shows how the plan holds up on a game day.. Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title. Family: stays in food.

### Health: choices, stress and relationships (`health-b`, 4)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| pressure-point | Pressure Point | 6-8 | story | - |
| stress-toolkit | Stress Toolkit | 6-8 | sandbox | feelings |
| relationship-spectrum | Relationship Spectrum | 6-8 | roleplay | - |
| screen-week | Screen Time Detective | 6-8 | data | - |

- **relationship-spectrum:** Topic line under the title on the tool page: "healthy relationships and boundaries". Reshaped by the overlap pass (Cory accepted, the concept above is the new one). The clash it fixed: Practices peer communication in scenarios like the live conflict-coach.

- **screen-time-detective:** Topic line under the title on the tool page: "digital wellness and screen time". Overlap note (left for you to settle in the spec): One of twelve 'Detective' titles. Suggested fix (rename): "My Screen Week". Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title.

### Physical education (`pe`, 7)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| target-toss | Target Toss | k-2 | lab | - |
| playbook | Playbook | 3-5 | builder | - |
| fitness-circuit | Fitness Circuit | 3-5 | race | movement |
| rules-referee | Rules Referee | 6-8 | escape | - |
| goal-tracker | Goal Tracker | 6-8 | creature | habit-hero |
| fitness-program-designer | Fitness Program Designer | 9-12 | builder | - |
| captain-s-choices | Captain's Choices | 9-12 | story | - |

### Library and research (`library`, 6)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| keyword-fishing | Keyword Fishing | 3-5 | puzzle | - |
| credit-card-builder | Credit Card Builder | 3-5 | builder | - |
| fake-or-fact-lab | Fake or Fact Lab | 6-8 | lab | fact-check |
| research-quest | Research Quest | 6-8 | story | - |
| boolean-builder | Boolean Builder | 9-12 | sandbox | - |
| fair-use-review | Fair Use Court | 9-12 | roleplay | - |

- **keyword-fishing:** Topic line under the title on the tool page: "choosing search keywords". Reshaped by the overlap pass (Cory accepted, the concept above is the new one). The clash it fixed: A kitchen experiment beside kitchen-lab and fraction-kitchen in 3-5.

- **fair-use-court:** Topic line under the title on the tool page: "copyright, fair use and Creative Commons". Overlap note (left for you to settle in the spec): One of four mock trials in 9-12. Suggested fix (reshape): "Fair Use Review": Work as a reviewer for a student video site; weigh each upload (a meme, a remix, a class project) against the four fair use factors, then cite each source and choose a Creative Commons license for your own work.. Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title.
