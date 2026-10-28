# Curio Class audit, phase 2: clashes in K-2, 3-5 and 6-8

Scope: the 61 fresh rule hits in docs/agents/overlap/pairs.csv for K-2 (21), 3-5 (16) and 6-8 (24), plus the overlap
risks the idea pass named for these bands (IDEA-PASS-LOG.md "Overlap" lines and the cards' own flags). Every tool was
judged from its idea.md, spec.md or tool.json. Live tools never move. Each reshape below was re-checked against its band
neighbors in tags.csv with the clash rule (skill key, action, coarse setting group) using the after-tags given in its
row, and against its module codes.

Result: 15 clusters (K01 to K15) plus a records section (K16). 11 reshapes, 16 keeps with a note, every other hit kept
with a reason. No live tool changes.

## Decision table

| id | fix | new concept line or note |
|---|---|---|
| story-problem-theater | reshape, title **Story Replay** | Short cartoon stories (birds on a wire, apples in a basket) stop at the question; act them out with counters, pick a number sentence, and the cartoon replays the way your sentence says. All story types within 20. |
| symbol-spotter | reshape (title stays) | Find national symbols on everyday things (a coin, a stamp, a flag, a postcard), hear the idea each stands for (freedom, fairness, welcome), then open holidays that honor people who changed the country and ask your own questions. |
| shade-builder | reshape (title stays) | Feel which backyard spots the sun warmed, then shade the sandbox with umbrellas, a tree, a tent or a sail; a heat camera shows which spots stay cool, and two designs are compared to pick the better one. |
| pattern-block-pond | reshape, title **Pattern Block Windows** (re-applies C17) | Fill stained-glass window outlines with pattern blocks (two triangles make a rhombus), build new window shapes from sticks and clay-ball corners, and count sides and corners to compare shapes. |
| elevator-hundred | reshape, title **Bead Slider** (re-applies C16) | Slide beads on a 100-bead string by tens and ones to solve 34 + 20 or 47 + 6, make a new ten when the ones run over, slide back for 10 less or 60 - 30, and write each slide as an equation. |
| puppet-show-feelings | reshape (title stays) | Watch a sock-puppet show, then go backstage and change one thing at a time (head tilt, voice speed, bounce) to see the audience read a new feeling; pick the ending you like and say how a puppet is like you. |
| pattern-painter | reshape (title stays; restores the accepted C31 fix) | Color the town's multiplication-table mural to make patterns pop (even products, multiples of 5, square numbers); predict the next square and say why the rule always works, then estimate first to check whether a two-step answer can be right. |
| shape-courtroom | reshape, title **Shape Sieve** (re-applies C31) | Quadrilaterals and triangles drop through sieves (four sides, parallel pairs, right angles, equal sides) and stop at the most specific name they earn; predict where a square lands, then build a hierarchy where every shape keeps its parents' properties. |
| dance-floor-moves | reshape, title **Transformation Dock** (re-applies C38 as reviewed) | An L-shaped cargo tile must land on its outline; slide, flip, turn and resize it, replay the route as coordinate rules, decide which docks are congruent or only similar, then tile triangles to see why angles sum to 180. |
| fact-check-desk | reshape, title **Bike Lane Briefing** | Two articles disagree about whether new bike lanes made a town safer; as the mayor's aide with the crash data open, sort each disagreement into fact or interpretation, trace claims to evidence, and flag the irrelevant ones for the council. |
| net-folder | reshape (title stays) | Design a board game's box and pyramid pieces: draw nets from coordinates, find each face's area and the total cardboard, fold them, and fill the box with half-inch cubes to see why l x w x h still works with fractions. |
| market-day | keep, note | C13's reshape stands. Spec: the student is the shopper with tokens; no coins, no making change and no snack stand (corner-store, live, owns those). Lead with service stalls and handmade goods. |
| festival-parade | keep, note | C01's reshape stands. Spec: the parade and the clue guessing lead; the closing map is a single dotted route, never stamps, a passport or a zoom through nested places (art-passport and me-on-the-map, both live). |
| question-jar | keep, note | Spec: bins are data methods only (count, measure, ask people, just an opinion), never look it up, ask an expert or try it (wonder-wall, live). Keep the jar sort short; the plan rounds are the main play for grades 1 and 2. |
| many-voices-book | keep, note | Spec: the order step is about inclusion (no page left at the back), not story sequence; sound-and-picture-book owns sequencing pages to change a story. |
| blend-bakery | keep, note | Spec: the vowel-team station uses the grade 1 teams (ee, ai, oa) inside one-syllable blending; vowel-team-tag (grade 2) owns the wider team set, prefixes and suffixes at speed. Too-big flag still stands. |
| day-in-the-life | keep, note | Spec: it leads with one first-person school day (story format) and its map step is population distribution (D2.Geo.6.3-5); no North America and no regions-and-ways-of-life map (nations-of-north-america, live). |
| fossil-clues | keep, note | C27's split stands: no rock layers here (canyon-reader owns them). Re-key its skill as fossil-environments (see tag corrections). |
| stadium-count | keep, note | Shares the times-ten zoom with zoom-by-tens (grade 5) on purpose: grade 4 zooms out over whole numbers, grade 5 zooms in past the decimal point. Spec both with different looks (crowd, meter stick). |
| inside-the-keypress | keep, note | E4-SYS-HW-12 also sits on network-help-desk. Spec: troubleshooting here stays inside one device (keys, apps, drivers); network-help-desk owns connection, sign-in and permission problems. |
| source-sorter | keep, note | Same skill key as fake-or-fact-lab. Spec: judge from clues inside the source, plus quoting, paraphrase and citation (W.6.8); fake-or-fact-lab owns leaving the page (lateral reading). |
| summary-scaffold | keep, note | Same skill as summary-squeeze (grade 6). Spec: the ELD frame-and-cite organizer for newcomers; no word-count squeeze (summary-squeeze owns it). |
| explainer-sections | keep, note | W.7.2 on two tools. Spec: section structure and order here; explainer-studio owns content inside sections. |
| blizzard-scenes | keep, note | W.8.3 on two tools. Spec: point of view and rewriting a scene here; flashback-editor owns flashback structure and time-shift transitions. |
| evidence-corkboard | keep, note | Its card already says it: a canal office board, not a detective's den (detective-del-pasado, misleading-charts and others use the mystery look). |
| silk-road-traders | keep, note | Spec: lead with the ideas map, oasis towns and monsoon ships; the camel caravan crossing a desert belongs to salt-and-gold-caravan. |
| reaction-kitchen | keep, note | Its hand warmer bench repeats hand-warmer-lab's product (grade 10). Spec: grade 7 tests kitchen materials and temperature only, no bond energies; teacher note names the grade 10 follow-up. |

After-tags used for the rule re-check (skill, action, setting group): story-problem-theater (word-problems-20,
manipulate, plain); symbol-spotter (national-symbols, explore, real); shade-builder (sunlight-warming, build, home);
pattern-block-pond (compose-shapes, build, studio); elevator-hundred (add-within-100, manipulate, plain);
puppet-show-feelings (responding-to-characters, experiment, toys); pattern-painter (arithmetic-patterns, explore,
studio); shape-courtroom (classify-shapes, predict-reveal, plain); dance-floor-moves (transformations, solve, shipping);
fact-check-desk (conflicting-sources, investigate, council-debate); net-folder (surface-area, build, game). None makes a
new 2-of-3 match in its band. Single-tag matches left: shade-builder and five home tools (setting only), shape-courtroom
and shape-family-tree (skill only, grades 3 and 5, a spiral), pattern-painter and paint-mixer (live, setting only),
fact-check-desk and five 6-8 assemblies (setting only).

Module check: every reshape keeps its module's codes taught in full. Bead Slider covers 1.NBT.4 to 1.NBT.6 (the idea
card's 34 + 25 was a grade 2 sum and is dropped); Pattern Block Windows keeps K.G.5 (sticks and clay balls) and K.G.6;
Shape Sieve keeps 5.G.3 and 5.G.4 with triangles; Transformation Dock keeps the 8.G.A angle-sum step from the idea
card; Bike Lane Briefing keeps RI.8.9 and RI.8.8; net-folder keeps 6.G.2 to 6.G.4 (the rest of 6.G.1 still moves to the
grade 6 sign shop).

## Tag corrections

The orchestrator's note: tags.csv carries pre-fix tags for tools that had a spec or were live. In these bands I found
no stale spec or live tag that made a false hit. choreography-board and leaf-sorter-ai carry their decisions_src.py
after-tags already; secret-keeper, misleading-charts, world-music-map and flipbook-studio match their specs; the live
tools' tags match their tool.json. Two idea-pass tags read the card's minor step instead of what the student mostly
does:

| id | field | value |
|---|---|---|
| fossil-clues | skill_key | fossil-environments |
| festival-parade | action | predict-reveal |

## Clusters

### K01. Puppet stages in K-2

- **Tools:** story-stage (ELA, K); story-problem-theater (math, g1); bedtime-retell (ELD, K-2); puppet-show-feelings
  (arts, K-2); tap-to-start-puppets (CS, K-2); act-it-out (arts, K-2). All planned.
- **Hit:** story-stage and story-problem-theater, action (manipulate) and setting (stage): both act a story out on a
  puppet stage. Six puppet or stage tools sit in K-2.
- **Fix:** story-stage owns the puppet stage (its family). Reshape story-problem-theater to Story Replay: the replay
  of the student's own number sentence is the idea, and it needs no stage. The arts and CS puppets stay, since puppetry
  is the subject (arts) or the sprite (CS). bedtime-retell is kept (C20, accepted); its sleepy friend could be drawn as
  a plush at spec time.

### K02. Two parades and a town hunt in K-2

- **Tools:** symbol-spotter (social studies, K); festival-parade (social studies, g1, wave 1); shape-spy (math, K)
- **Hit:** shape-spy and symbol-spotter, action (hunt) and setting (town), both in kindergarten. symbol-spotter's
  parade-day town also repeats festival-parade's parade one grade apart.
- **Fix:** reshape symbol-spotter to everyday objects that carry the symbols. shape-spy keeps its hunt: its card now
  leads with the parts of K.G.A the live tools skip (solids, tilted shapes, position words), which was C18's aim.

### K03. The playground twice in kindergarten

- **Tools:** shade-builder (science, K); playground-rules (social studies, K)
- **Hit:** action (build) and setting (town: the same school playground), same grade.
- **Fix:** playground-rules keeps the playground (its rules are about one). shade-builder moves to a backyard sandbox;
  the warming and design work (K-PS3-1, K-PS3-2, K-2-ETS1) is unchanged.

### K04. Ponds and elevators beside live tools (first-pass fixes the idea cards undid)

- **Tools:** pattern-block-pond (math, K) beside hundred-hop (live, K, frog on lily pads); elevator-hundred (math, g1)
  beside sound-elevator (live, K-2, mouse in an elevator)
- **Hit:** pattern-block-pond and nature-inventor, action (build) and setting (nature). Below the bar, both repeat a
  live tool's picture. C16 and C17 fixed this in the first pass; both were tier C "later", and the idea cards went back
  to the lily pads and the elevator.
- **Fix:** re-apply C17 (Pattern Block Windows) and C16 (Bead Slider) with the idea cards' teaching detail kept. This
  also clears the nature-inventor hit.

### K05. Feelings with a puppet, and questions in a jar

- **Tools:** puppet-show-feelings (arts, K-2) beside feelings-faces (live); question-jar (CS, K-2) beside wonder-wall
  (live)
- **Hit:** idea-pass risks, below the bar. puppet-show-feelings opened on "say how each puppet feels and how you can
  tell", which is feelings-faces, and C56 fences off more K-2 feelings-naming tools. question-jar sorts questions by how
  to find out, as wonder-wall does.
- **Fix:** reshape puppet-show-feelings to the performer's side (TH:Re7, TH:Re8, TH:Cn10). question-jar keeps its line
  with a note: its bins are data methods, and the plan rounds (who a plan misses) are where it differs.

### K06. Market Day beside the live Corner Store

- **Tools:** market-day (social studies, g1); corner-store (math, g2, live)
- **Hit:** action (manage) and setting (shop-food).
- **Fix:** keep with a note. C13 already reshaped market-day (accepted): the student is a shopper choosing between
  goods and services, not a seller making change. The note keeps coins and snacks out.

### K07. Festival Parade on the world map

- **Tools:** festival-parade (social studies, g1, wave 1); art-passport (live); me-on-the-map (live)
- **Hit:** action (explore) and setting (travel-map) with each live tool.
- **Fix:** keep with a note. C01's reshape (accepted) took the passport out; the tag comes from the closing map step.
  The student mostly guesses from clues (tag correction above).

### K08. Making books in K-2

- **Tools:** many-voices-book (library); sound-and-picture-book (arts); field-trip-slideshow (arts). All K-2.
- **Hit:** many-voices-book and sound-and-picture-book, action (compose) and setting (book). field-trip-slideshow is
  an idea-pass risk.
- **Fix:** keep. The students do different things: add a page about yourself and place it so everyone is in
  (AASL.Include); author a three-page story whose order changes its meaning (MA:Cr); do crew jobs and present
  (MA:Pr). Note on many-voices-book.

### K09. Phonics bakery and playground tag

- **Tools:** blend-bakery (ELA, g1); vowel-team-tag (ELA, g2)
- **Hit:** idea-pass risk (one tag: drill). Both cards cover vowel teams, two-syllable words, endings and tricky words,
  because RF.1.3 and RF.2.3 both do.
- **Fix:** keep with a note; this is the grade 1 to grade 2 spiral, and each tool leads with its grade's core.

### K10. Mysteries and courtrooms in 3-5 (C31 again)

- **Tools:** pattern-painter (math, g3); shape-courtroom (math, g5); label-detective (live); inference-interrogation
  (ELA, g5); claim-court (ELA, g5); shape-family-tree (math, g3)
- **Hit:** pattern-painter with label-detective (live) and inference-interrogation, action (investigate) and setting
  (detective). C31 renamed it Pattern Painter (accepted) to end the case file, but the idea card made it a mystery again
  ("who painted this", witnesses). shape-courtroom's C31 reshape was left for the spec and the idea card went back to a
  trial, so grade 5 has two courtrooms (with claim-court) and the idea pass flagged the shape-family-tree overlap.
- **Fix:** reshape both. inference-interrogation and claim-court stay (C31). Trapezoid: inclusive definition in Shape
  Sieve with a teacher note, matching shape-family-tree (left to the gap agent's catalog fixes).

### K11. Maps in 3-5 and a day abroad

- **Tools:** day-in-the-life (social studies, g3); nations-of-north-america (live, g5); fraction-trail, state-quest
  (live), state-economy-map
- **Hit:** day-in-the-life and nations-of-north-america, action (explore) and setting (travel-map). Both teach how land
  and weather shape ways of life. The fraction-trail and state map hits are C57's kept map hits.
- **Fix:** keep day-in-the-life with a note: a first-person story day in four present-day countries, with population
  distribution as its map, against a grade 5 regions map of Native nations.

### K12. Fact-check desks in grade 8

- **Tools:** fact-check-desk (ELA, g8); misleading-charts (CS, 6-8, spec)
- **Hit:** action (investigate) and setting (newsroom). Both open on "the fact-check desk at a town paper".
- **Fix:** misleading-charts has a spec, so fact-check-desk changes: the mayor's aide briefing the council. The skill
  (two texts in conflict, irrelevant evidence) and its fact-check family stay.

### K13. Dance floors and craft fairs in 6-8 math

- **Tools:** dance-floor-moves (math, g8) and choreography-board (arts, 6-8, spec); net-folder (math, g6) and
  snow-globe-maker (math, g8)
- **Hit:** dance-floor-moves and choreography-board, action (compose) and setting (stage). C38's reshape was reviewed as
  Transformation Dock but left for the spec, and the idea card went back to dancers. net-folder and snow-globe-maker
  are an idea-pass risk: both are craft-fair stalls in 6-8 math.
- **Fix:** re-apply Transformation Dock; snow-globe-maker keeps the craft fair (C37, accepted) and net-folder moves to a
  board game's box and pieces.

### K14. Same code or same skill twice in 6-8 ELA and library

- **Tools:** explainer-sections and explainer-studio (W.7.2); blizzard-scenes and flashback-editor (W.8.3);
  source-sorter and fake-or-fact-lab (source-credibility); summary-squeeze and summary-scaffold (summary);
  claim-quote-comment and cer-builder; draft-versus-draft (6-8) and draft-car-wash (3-5)
- **Hit:** idea-pass risks; source-sorter and the summary pair share a skill key, the rest share a code.
- **Fix:** keep all, with notes on the first tool of each of the four same-band pairs. Each pair splits the code by what
  the student does (structure against content, point of view against flashback, inside clues against lateral reading,
  compression against frames). claim-quote-comment (nonfiction quoting) and cer-builder (an ELD lab conclusion) differ
  by text and purpose; the drafts pair is a cross-band spiral.

### K15. Trade routes, assemblies and other 6-8 setting pairs

- **Tools and hits (all action and setting):** silk-road-traders and salt-and-gold-caravan (manage, travel-map);
  detective-del-pasado and evidence-corkboard (investigate, detective); five-themes-field-trip and tenochtitlan-builder
  (build, town); gene-pool and hunter-to-farmer (simulate-tune, garden-farm); house-of-wisdom and rabbit-hole-notebook
  (trace, library); raindrop-s-journey and invasive-species-alert (choose-path, water); dramatic-irony-theater and
  dancers-on-tour (simulate-tune, stage); moon-phase-model (live) and planet-builder (simulate-tune, space);
  summer-stand and tax-and-tip (manage, shop-food); mongol-messenger and historians-disagree (idea-pass risk, same
  empire).
- **Fix:** keep. In each pair the content is the subject and the student does something different: ideas spreading by
  card trade against running a caravan business; a Spanish tense case against an Erie Canal evidence board; mapping a
  living river city against building an ancient one; strawberry genetics against the first farms; one book's
  translation journey against a self-chosen inquiry trail; a water molecule's path against managing a lake invasion;
  revealing a secret to an audience against adapting a dance to venues; gravity and orbits against lighting and phases
  (planet-builder's card already says so); a drink stand's variables against a diner's percents (C37 kept both).
  mongol-messenger is a relay race, historians-disagree compares accounts. Notes on silk-road-traders and
  evidence-corkboard keep their looks apart.

## K16. Records: every other hit, and cross-band risks

**Kept for C57's reason (still true after the idea pass):**

- Both live (C56): art-passport and me-on-the-map; beat-buddies and animal-moves; feelings-faces and
  feelings-weather-report; hamburger-paragraph and lunch-tray-builder; i-spy-science and habitat-hunt.
- The creature format always means care-for: habit-hero (live), terrarium-pal and letter-lanterns (three pairs).
- 'Machine' is broad (W1): sound-elevator (live) and make-ten-machine.
- Maps are native to geography, history and languages: fraction-trail with state-quest (live) and state-economy-map;
  state-quest and state-economy-map; expansion-map, civil-war-map-room, mundo-hispano and world-music-map (six pairs).
- Mystery format: inference-interrogation and label-detective (live).
- Historical assemblies, the event is the content: agora-assembly and constitutional-convention (D2.Civ.8.6-8 now moves
  to the convention; agora keeps D2.His.3 and D2.Civ.9).
- A lab bench is the default for science: cer-builder and molecule-builder; sign-parameters-lab (ASL, lab format) and
  electromagnet-lab.
- Kitchen chemistry and ratios: smoothie-lab (live) and reaction-kitchen.
- Drawing and animation: vanishing-point-studio (live) and flipbook-studio.
- Different newsroom work: explainer-studio and colonial-newsroom.
- Vehicles carry different math: hot-air-and-sandbags and two-trains (live).
- Different writing: headline-writer and class-pet-pitch (the poster tool is now a care guide plus a poster).

**Kept, new hits, different skills on a broad setting:**

- K-2: bedtime-retell and my-life-timeline (order, home: a story retell against a keepsake timeline); push-the-pumpkin
  and plant-experiment-shelf (experiment, garden-farm: forces on a farm path against a bean fair test); secret-keeper
  (spec, pet park) and three-towns (sort, town); text-feature-makeover and orchestra-zoo (live) (explore, animals: the
  page is about ocean animals, not a zoo).
- 3-5: cartoon-soundtrack-mixer and stop-motion-clay-shoot (compose, film-media: scoring against animating, different
  MA codes); slow-mo-writer with each (the film strip is only a view of the student's sentences); food-web-wobble and
  settle-the-valley, leaf-sorter-ai and erosion-table (nature: food webs, people and land, a classifier, erosion);
  fossil-clues and canyon-reader (C27 split, note above); radio-hour-notes and toy-ad-reality-check (annotate,
  film-media: listening notes against ad tricks); blueprint-builder and inquiry-ladder (build, construction: text
  structures against supporting questions; blueprint-builder's C45 retitle was left for the spec and its card now
  reads facts, which met C45's aim).
- 3-5 idea-pass risks, kept: shape-family-tree and shape-courtroom (see K10); main-idea-pinboard, claim-court and
  quote-picker (pinning an author's support, judging it, using it in one's own paragraph); note-card-shuffle and
  research-rover (grade 3 notes, grade 4 sources and outline); make-ten-machine and fact-rally (building strategies
  against speed, W1).

**Cross-band risks named by the idea pass (spirals, kept; each card already states its boundary):** fact-rally and
multiplication-dungeon; hallway-art-museum and traveling-art-show; cereal-ad-questions and toy-ad-reality-check;
audience-talkback and scene-staging-comparison; neighborhood-issue-play and three-viewpoints-scene; tools-for-change and
levers-of-power; barter-bay and border-trade-post (round 1 brief); fair-survey-kit, lunch-survey-cleanup and
catalog-column-rules; crash-test-lab and collision-lab (live; no momentum math at grade 8); reaction-kitchen and
hand-warmer-lab (note above); half-pipe-energy and zipline-energy; planet-builder and orbit-lab; leaf-factory and
energy-accountant; dancers-on-tour and museum-courtyard-performance; morning-show-crew and mini-documentary-crew;
scene-staging-comparison and director-s-chair; viral-video-breakdown and fair-use-review; choreography-board and
choreography-for-a-cause; economy-checkup and economy-dashboard. None matches on all three tags.
