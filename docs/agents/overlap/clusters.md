# Curio Class overlap pass: clusters

Scope: all 586 tools in data/tools-concepts.csv (76 live, 510 planned), tagged in tags.csv. The rule and tagging method are in method.md, gaps in gaps.md, and every rule hit in pairs.csv (before the fixes) and pairs-after.csv (after them). This is the revised pass; the "Revision" section of method.md lists what changed since the first draft.

Live tools are fixed points. Every fix moves a planned tool; no live tool is asked to change.

## Summary

**58 clusters plus 3 wave 1 decisions.** C01 to C52 each change at least one planned tool, ordered most serious first: clashes with live tools, then planned clashes, then trademarks, setting repeats and titles. C53 to C58 are spec notes and records, so nobody re-flags them.

| Kind | Clusters |
|---|---|
| Clash with a live tool (2 of 3 tags in one band) | 14 |
| Same story, setting or picture as a live tool (below the bar) | 5 |
| Clash between planned tools | 21 |
| Same skill or picture between planned tools (below the bar) | 7 |
| Title (near-identical or overused words) | 4 |
| Trademark | 2 (plus C02 and C06, filed as live clashes) |
| Spec notes | 1 |
| Setting or format load | 2 |
| Records (live-live overlaps, every kept rule hit) | 2 |

Per tool, the decision table below asks for:

| Fix | Tools |
|---|---|
| Reshape (new concept line, usually a new title) | 62 |
| Rename (title only, concept stands) | 17 |
| Add a standard to the module (energy-accountant) | 1 |
| Keep, with a line for the spec check | 7 |
| Keep, listed because an alternative is on the table | 4 |
| Move-to-gap | 0 recommended (offered as the option for boundaries-builder, ph-detective and population-dashboard) |
| Merge | 0 recommended (offered as the option for retell-puppets) |

That is 79 planned tools changed (62 + 17), about 15 percent of the 510 planned. The rule found 152 pairs before the fixes and 92 after; every one of the 92 is listed with its reason in C57. None of the new concept lines creates a new rule hit (checked with `python scripts/overlap/rule.py --after`).

### Look at these first

1. **Wave 1 decisions (W1 to W3 and C01).** festival-passport needs its new concept before its spec. make-ten-machine, town-planner-disaster-ready and energy-accountant each have a neighbor or a standard to settle first.
2. **Clashes with live tools found in the recheck:** C03 input-output-machine against computer-builder, C04 design-the-study against poll-workshop, C05 and C06 against community-project-planner.
3. **C02 bee-bot-garden** clashes with two live K-2 coding tools at once, and "Bee-Bot" is a product name.
4. **C23 counterclaims** run in grades 6, 7 and 8 ELA, though grade 6 has none in its standard.
5. **C33 trademarks:** Mad Libs, Jenga, Battleship, Rube Goldberg, Monopoly.
6. **C20 retell-puppets** matches story-stage on all three tags (reshape or merge).
7. **C30 and C32:** four courtrooms and four mysteries in 9-12.

### Open calls for Cory

Each has a recommendation; the options are in the decision table and decisions.json.

- **energy-accountant (W3):** add HS-LS2-5 to its module before the wave 1 spec (recommended), or leave the carbon cycle for a later tool.
- **retell-puppets (C20):** reshape to Bedtime Retell (recommended), or merge into story-stage.
- **boundaries-builder (C07):** reshape to Relationship Spectrum (recommended), or move to the 6-8 nutrition gap.
- **ph-detective (C32):** rename to Mystery Liquids (recommended), or move to the HS-PS3-4 gap.
- **population-dashboard (C54):** keep (recommended once W3 lands), or move to the HS-ESS2-7 gap.
- **voice-switcher (C55):** keep (recommended), or reshape to Play-by-Play Voice.
- **counterclaim-ping-pong (C52):** keep the title, or rename to Counterclaim Rally.

Closed since the first draft: courtroom-statistics is kept (C30), bundle-bakery becomes Crayon Boxes (C13), and the secret-keeper reshape is dropped.

## Decision table

One row per tool that changes or needs a call. Generated from scripts/overlap/decisions_src.py by `python scripts/overlap/build_decisions.py`; the same rows are in decisions.json.

<!-- decision-table:start -->
| tool_id | title | band | status | cluster | suggested fix | new title | new concept line | options |
|---|---|---|---|---|---|---|---|---|
| make-ten-machine | Make Ten Machine | K-2 | planned | W1 | keep, spec note |  | (unchanged) Wave 1. Owns the conveyor and tens-packing picture in K-2 math; ten-frame-factory is retitled and bundle-bakery leaves the conveyor (Crayon Boxes). |  |
| ten-frame-factory | Ten Frame Factory | K-2 | planned | W1 | rename (title only) | Ten and Some More | (unchanged) |  |
| town-planner-disaster-ready | Town Planner: Disaster Ready | 3-5 | planned | W2 | keep, spec note |  | (unchanged) Wave 1. Owns hazards, floods and dams in grade 4; settle-the-valley is trimmed to leave them out. |  |
| settle-the-valley | Settle the Valley | 3-5 | planned | W2 | reshape |  | Settle a valley: choose where farms, homes and roads go and see how the land and the people change each other, from cleared forests and worn-out soil to new trails and trade. |  |
| energy-accountant | Energy Accountant | 9-12 | planned | W3 | add a standard to its module |  | (unchanged) Wave 1. Its carbon and energy ledger already models photosynthesis and respiration; HS-LS2-5 is the carbon cycle across the spheres and has no module. | Add HS-LS2-5 (and optionally HS-LS2-3) to its module before the wave 1 spec (recommended) OR Leave it and give HS-LS2-5 its own tool later (a new module row; an earlier draft re-pointed population-dashboard there as 'Carbon Relay') |
| festival-passport | Festival Passport | K-2 | planned | C01 | reshape | Festival Parade | Floats from festivals around the world roll past on the projector; the class guesses what is being celebrated from the food, music and clothes, then hears the story behind it, sees where it happens on the map, and joins in one song or move. |  |
| bee-bot-garden | Bee Bot Garden | K-2 | planned | C02 | reshape | Mouse Mail Route | The class lays arrow cards to send a mail mouse across a snowy town grid; before it runs, kids trace the route with a finger and predict where it will stop, then run it and fix the card that sent it the wrong way. |  |
| input-output-machine | Input-Output Machine | K-2 | planned | C03 | reshape | Takes In, Gives Out | A tablet, a game controller, a smart speaker and a microwave; the class sorts each part into 'takes in' or 'gives out', then predicts what the gadget does when one input is covered. |  |
| design-the-study | Design the Study | 9-12 | planned | C04 | reshape |  | Test whether energy drinks really speed up reaction times: choose random assignment, a control group, blinding and a placebo, and a skeptical journal editor shows how each missing piece lets a hidden variable fake the result. Surveys and sampling stay with poll-workshop. |  |
| local-changemaker-planner | Local Changemaker Planner | 9-12 | planned | C05 | reshape | Who Decides? | Pick a local problem (a dangerous crosswalk, a closed library branch) and trace who actually decides it: which office, which meeting, when public comment opens; then draft the testimony or petition that reaches them. |  |
| power-grid-tycoon | Power Grid Tycoon | 9-12 | planned | C06 | reshape | Grid Operator | Keep a city's lights on from the grid control room, mixing coal, gas, solar, wind and nuclear; balance cost, reliability and emissions through a heat wave and a still, cloudy week. |  |
| boundaries-builder | Boundaries Builder | 6-8 | planned | C07 | reshape | Relationship Spectrum | Place short friendship and dating scenarios on a line from healthy to unhealthy; red-flag cards explain each placement, and a 'what you could say' card practices setting the boundary. | Reshape to Relationship Spectrum (recommended) OR Move to the 6-8 nutrition gap: 'Day of Meals: Plan a day of meals and snacks around a busy schedule (practice, a test, a late night), then see how energy, focus and mood hold up and adjust the plan.' |
| compound-interest-garden | Compound Interest Garden | 9-12 | planned | C08 | reshape | Rainy Day Fund | Live a year of surprise costs (a flat tire, a cracked phone, a vet bill) with and without an emergency fund, then see what the fund grows to if it sits untouched for ten years. |  |
| roller-coaster-physics | Roller Coaster Physics | 9-12 | planned | C09 | reshape | Zipline | Design a zipline from a cliff platform to a far tree; with friction on, energy conservation decides whether the rider reaches the far platform and how hard the brake has to work. |  |
| move-like-me | Move Like Me | K-2 | planned | C10 | reshape | Levels and Pathways | An animated dancer stretches, twists and bends at high, middle and low levels, then travels straight, curved and zigzag pathways; the class copies each one, then invents a pathway for the dancer to follow. |  |
| text-feature-safari | Text Feature Safari | K-2 | planned | C11 | reshape | Page Makeover | A plain page about ocean animals is hard to use; the class adds a heading, captions, labels and a glossary one at a time and sees which question each one helps answer faster. |  |
| book-detectives | Book Detectives | K-2 | planned | C12 | reshape | Meet the Book Makers | An author and an illustrator take turns showing their part of a picture book; the class decides which job made each part of the page (words or pictures) and names the book's main topic and two details that tell about it. |  |
| market-day | Market Day | K-2 | planned | C13 | reshape |  | With five tokens, the class shops a weekend market as consumers; each stall sells a good or offers a service, every choice means giving something else up, and the stall owners explain what they made or did. |  |
| bundle-bakery | Bundle Bakery | K-2 | planned | C13 | reshape | Crayon Boxes | Pack the class's loose crayons into boxes of ten for every table; say how many boxes and loose crayons, then compare two classrooms' supplies with >, = and <. |  |
| pizza-physics | Pizza Physics | 6-8 | planned | C14 | reshape | Big Wheel, Small Wheel | Settle classic round-object arguments (one big trampoline or two small ones? a 26-inch bike wheel or a 20-inch?) by measuring circumference and area. |  |
| two-sides-theater | Two Sides Theater | K-2 | planned | C15 | reshape | Bear's Side of the Story | Goldilocks and Baby Bear tell the same morning (beginning, middle and end) two ways; tap a character to hear the scene in their voice and see their thought bubble, then the class voices the next scene as the other character. |  |
| elevator-hundred | Elevator Hundred | K-2 | planned | C16 | reshape | Bead Slider | Slide beads on a 100-bead string, ten at a time and one at a time, to solve 34 + 20 or 47 + 6, then write the slides as an equation. |  |
| pattern-block-pond | Pattern Block Pond | K-2 | planned | C17 | reshape | Pattern Block Windows | Snap pattern blocks together to fill a stained-glass window outline; the window glows when two triangles make a rhombus. |  |
| shape-spy | Shape Spy | K-2 | planned | C18 | reshape | Hide and Seek Solids | A teddy bear hides beside, above, behind or under 3D solids in a toy room; the class names the solid, says whether it is flat or solid, and calls the position word before the teacher lifts the cover. |  |
| pizza-party | Pizza Party | K-2 | planned | C19 | reshape | Fair Folds | Fold and cut paper shapes (squares, circles, rectangles) into halves and fourths for a class art project; uneven cuts leave a friend with a smaller piece, and the class spots which cuts are fair. |  |
| retell-puppets | Retell Puppets | K-2 | planned | C20 | reshape | Bedtime Retell | A sleepy puppet friend asks to hear a short story again; learners retell the beginning, middle and end with sentence frames and picture prompts, answering 'what happened first? then what?', and the friend drifts off after a complete retell. | Reshape to Bedtime Retell (recommended) OR Merge into story-stage as an ELD sentence-frame mode (needs one tool serving two modules) |
| class-snack-vote | Class Snack Vote | K-2 | planned | C21 | reshape | Me vs the Counter | A ball bounces for ten seconds; half the class tallies the bounces by hand while the computer counts them too; compare the totals and the mistakes, then use the computer's counts to pick the bounciest ball. |  |
| pattern-finder | Pattern Finder | K-2 | planned | C22 | reshape | Spot the AI | Everyday scenes play out (a phone unlocking with a face, a map choosing a route, a toy that answers back); the class guesses which ones use AI, and the teacher reveals the pattern each one learned from. |  |
| debate-prep-desk | Debate Prep Desk | 6-8 | planned | C23 | reshape | Reason Builder | Pick a kid-relevant issue (a later school start?), write a claim, then choose which of eight facts actually support it; off-topic and weak facts bounce out, and the paragraph builds from the ones that hold. |  |
| town-hall-debate | Town Hall Debate | 6-8 | planned | C23 | reshape | Claim vs Claim | A group-chat argument about a school rule gets rewritten for the school board: sort each message into your claim, an opposing claim or neither, then write a formal paragraph that names the strongest opposing claim fairly and shows exactly where the two part ways. |  |
| fruit-sorter-ai | Fruit Sorter AI | 3-5 | planned | C24 | reshape | Leaf Sorter AI | Choose which features (color, edge, shape, size) a classifier may use to sort leaves by tree; see which features separate them and which only add noise, then test it on leaves it has never seen. |  |
| director-s-chair | Director's Chair | 9-12 | planned | C25 | reshape |  | Stage the same short scene as a Greek chorus, Noh, commedia, Elizabethan and modern realist production; compare what each tradition's staging rules make the audience notice. |  |
| premise-inspector | Premise Inspector | 9-12 | planned | C26 | reshape |  | Lay out the Declaration's argument as premises and a conclusion, then test later responses (Seneca Falls, Douglass's Fifth of July speech, the Gettysburg Address) by which premise each accepts, stretches or rejects. |  |
| founding-words-explorer | Founding Words Explorer | 9-12 | planned | C26 | reshape |  | Read founding documents with plain-English layers and historical context; trace how each document's central ideas develop across its sections. |  |
| fossil-dig | Fossil Dig | 3-5 | planned | C27 | reshape | Fossil Clues | Match each fossil (a fish, a fern, a coral) to the place it lived, then piece together what this desert used to be and which animals could survive the change. |  |
| evidence-locker | Evidence Locker | 3-5 | planned | C28 | reshape | Quote Picker | For each reason in an opinion paragraph, choose the quote that backs it and write the sentence that introduces it; a quote that only repeats the reason fades out. |  |
| polynomial-garden | Polynomial Garden | 9-12 | planned | C29 | reshape | Polynomials as Numbers | Set x = 10 and watch every polynomial become an ordinary number; multiplying polynomials turns into long multiplication without carrying, and like terms line up like place-value columns. |  |
| courtroom-statistics | Courtroom Statistics | 9-12 | planned | C30 | keep |  | (unchanged) |  |
| fair-use-court | Fair Use Court | 9-12 | planned | C30 | reshape | Fair Use Review | Work as a reviewer for a student video site; weigh each upload (a meme, a remix, a class project) against the four fair use factors, then cite each source and choose a Creative Commons license for your own work. |  |
| robber-baron-or-captain | Robber Baron or Captain? | 9-12 | planned | C30 | reshape | Baron or Builder? | Place industrialists on a line from robber baron to captain of industry using evidence cards (wages, prices, philanthropy, monopolies); the class compares placements and argues the hardest cases. |  |
| pattern-detective | Pattern Detective | 3-5 | planned | C31 | reshape | Pattern Painter | Color the multiplication table to make patterns pop (every even product, every multiple of 5, the square numbers), predict the next colored square and explain the rule in one sentence, then use a pattern to crack a two-step word problem. |  |
| network-detective | Network Detective | 3-5 | planned | C31 | reshape | Help Desk Heroes | Families call the help desk because a device won't connect; ask the right questions (wired or wireless? signed in, or just not allowed?) and fix each one. |  |
| shape-courtroom | Shape Courtroom | 3-5 | planned | C31 | reshape | Property Sieve | Shapes drop through a stack of sieves (four sides, parallel pairs, right angles, equal sides) and stop at the most specific name they earn; the class predicts where a square lands. |  |
| ph-detective | pH Detective | 9-12 | planned | C32 | rename (title only) | Mystery Liquids | (unchanged) | Rename to Mystery Liquids, concept unchanged (recommended) OR Move to the HS-PS3-4 gap: 'Even Out: Drop hot metal into cold water, mix hot and cold water, and predict the final temperature; watch energy flow until both sides match.' Needs a new module row. |
| mad-libs-machine | Mad Libs Machine | 3-5 | planned | C33 | rename (title only) | Story Blanks | (unchanged) |  |
| food-web-jenga | Food Web Jenga | 3-5 | planned | C33 | rename (title only) | Food Web Wobble | (unchanged) |  |
| battleship-grid | Battleship Grid | 3-5 | planned | C33 | reshape | Sea Search Grid | Hide boats on the first quadrant and call coordinates to find a partner's; each miss tells you how far off you were. |  |
| rube-goldberg-workshop | Rube Goldberg Workshop | 3-5 | planned | C33 | rename (title only) | Contraption Workshop | (unchanged) |  |
| lemonade-monopoly | Lemonade Monopoly | 9-12 | planned | C33 | reshape | The Buyout | The same phone-charger market runs twice, once with four competing makers and once after one buys out the rest; compare prices, choice and quality side by side, then see what regulators can do. |  |
| chain-reaction | Chain Reaction | 3-5 | planned | C34 | reshape | Rewind It | A picture story (a dropped ice cream, a missed bus) runs backward one step at a time; learners link each step with because, so or as a result to rewind it to the start. |  |
| treasure-map-steps | Treasure Map Steps | K-2 | planned | C35 | reshape | Lost and Found | Two-step clues about what came in and went out of the lost and found each day ('14 mittens, 6 picked up, 5 more found') point to the box that holds the missing toy. |  |
| story-map-treasure | Story Map Treasure | K-2 | planned | C35 | reshape | Story Quilt | Sew a story quilt one square at a time (beginning, problem, how the character feels, solution, lesson), choosing the picture that belongs in each square and retelling it aloud. |  |
| recipe-scaler | Recipe Scaler | 3-5 | planned | C36 | reshape | Costume Crew | Each costume for the school play takes 3/8 yard of fabric and 2/3 of a spool of ribbon; scale up for the whole cast and work out how many bolts and spools to buy, then add up the scraps left over. |  |
| pizza-shop-assembly-line | Pizza Shop Assembly Line | 3-5 | planned | C36 | reshape | Paper Plane Factory | Make paper airplanes alone, then on an assembly line with specialized jobs; productivity jumps, and the class sees how each worker depends on the others. |  |
| keyword-kitchen | Keyword Kitchen | 3-5 | planned | C36 | reshape | Keyword Fishing | Cast a search with the keywords you choose and see what you catch; too broad pulls in junk and too narrow catches nothing. |  |
| ice-cream-shop | Ice Cream Shop | 6-8 | planned | C37 | reshape | Snow Globe Maker | Design snow globes, cone-shaped tree ornaments and cylinder bases; volume decides how much water and glitter each needs and what each costs to make. |  |
| dance-floor-moves | Dance Floor Moves | 6-8 | planned | C38 | reshape | Dock It | An L-shaped cargo tile must land exactly on its outline; slide, flip, turn and resize it in the fewest moves, then replay the route as a sequence of rules and decide which docks were congruent and which only similar. |  |
| transformation-golf | Transformation Golf | 9-12 | planned | C38 | reshape | Shape Twins | Each level shows a shape and its twin; map one onto the other with the fewest rigid motions, then write the sequence as the proof that they are congruent. |  |
| choreography-board | Choreography Board | 6-8 | planned | C38 | reshape |  | Build a dance on a timeline of movement phrases (counts, levels, dynamics), then revise it; formations show in a side view as the phrases play to music. |  |
| space-cargo | Space Cargo | 9-12 | planned | C39 | reshape | Curling Stones | Slide stones of different masses with different pushes along the ice; F = ma predicts where each one stops, and sweeping changes the friction. |  |
| inquiry-planner | Inquiry Planner | 9-12 | planned | C40 | reshape | Question Sharpener | Start from a broad interest and narrow it into a researchable question; the tool tests each draft (too broad, too narrow, already answered) and maps what you would need to find out. |  |
| island-economy | Island Economy | 9-12 | planned | C41 | reshape | Lake Commons | Manage a lake town's fish, forest and water over generations, through good years and flood years; sustainable use keeps the town going and overuse brings collapse. |  |
| build-a-government | Build a Government | 9-12 | planned | C41 | reshape | Write the Charter | Design a government for a newly formed country; pick a system, write its powers, and test it against crises (a disputed election, a famine, a leader who won't leave). |  |
| argument-frames-pro | Argument Frames Pro | 9-12 | planned | C42 | rename (title only) | Counterpoint Frames | (unchanged) |  |
| scam-shield | Scam Shield | 9-12 | planned | C43 | reshape | Covered | Compare three insurance quotes side by side; a slider trades the monthly premium against the deductible, and a claim calculator shows who pays what for a stolen bike or a fender bender. A last round sorts real insurer messages from fake 'claim refund' texts. |  |
| flowchart-factory | Flowchart Factory | 6-8 | planned | C44 | rename (title only) | Chore Flowcharts | (unchanged) |  |
| essay-architect | Essay Architect | 3-5 | planned | C45 | reshape | Essay Train | Paragraphs are train cars; each coupling is a transition, and a weak one lets the cars drift apart until the order and the links make sense. |  |
| blueprint-builder | Blueprint Builder | 3-5 | planned | C45 | reshape | Same Facts, New Shape | One set of facts about a hurricane appears as a timeline, a cause-and-effect chain and a problem-and-solution article; students name each structure and say which question each version answers best. |  |
| source-sorter | Source Sorter | 6-8 | planned | C46 | reshape |  | Give each source a quick credibility check, then practice quoting it and paraphrasing it; the tool flags paraphrases that copy too closely and builds the citation for each version. |  |
| snack-scale | Snack Scale | K-2 | planned | C47 | reshape | Snack Lineup | Line up two rows of snacks one to one; the leftovers show which group has more, and the class says the numbers before the teacher matches them up. |  |
| skate-park-energy | Skate Park Energy | 6-8 | planned | C48 | reshape | Swing Energy | Pull a playground swing back and let go; kinetic and potential energy trade places in a live bar chart, and a longer pull or a heavier rider changes the totals. |  |
| cone-slicer | Cone Slicer | 9-12 | planned | C49 | reshape | Focus Finder | Drag a point so its distances to two foci (or to a focus and a line) follow one rule, and watch an ellipse, a hyperbola or a parabola appear; then find each one's equation. |  |
| meal-and-move-planner | Meal and Move Planner | 9-12 | planned | C50 | reshape | Game Day Fuel | Plan a week of meals around your training days; the tool tracks energy in and out, flags gaps and extremes, and shows how the plan holds up on a game day. |  |
| depth-detective | Depth Detective | 3-5 | planned | C51 | rename (title only) | Near and Far | (unchanged) |  |
| root-detective-cards | Root Detective Cards | 3-5 | planned | C51 | rename (title only) | Root Cards | (unchanged) |  |
| screen-time-detective | Screen Time Detective | 6-8 | planned | C51 | rename (title only) | My Screen Week | (unchanged) |  |
| data-detective | Data Detective | 6-8 | planned | C51 | rename (title only) | Trend Line | (unchanged) |  |
| unit-detective | Unit Detective | 9-12 | planned | C51 | rename (title only) | Unit Sense | (unchanged) |  |
| watershed-detective | Watershed Detective | 9-12 | planned | C51 | rename (title only) | Upstream | (unchanged) |  |
| word-zoo | Word Zoo | K-2 | planned | C52 | rename (title only) | Word Habitats | (unchanged) |  |
| story-dress-up | Story Dress-Up | K-2 | planned | C52 | rename (title only) | Act It Out | (unchanged) |  |
| particle-zoom | Particle Zoom | 3-5 | planned | C52 | rename (title only) | Too Small to See | (unchanged) |  |
| summary-scaffold | Summary Scaffold | 6-8 | planned | C52 | rename (title only) | Say It Short | (unchanged) |  |
| counterclaim-ping-pong | Counterclaim Ping-Pong | 6-8 | planned | C52 | keep |  | (unchanged) | Keep the title OR Rename to Counterclaim Rally ('Ping-Pong' is a registered mark for table tennis gear) |
| sentence-remixer | Sentence Remixer | 6-8 | planned | C53 | keep, spec note |  | (unchanged) Spec check: lead with style and pronouns (L.6.3, L.6.1); clause function belongs to sentence-diagram-builder (L.7.1). |  |
| song-form-builder | Song Form Builder | 3-5 | planned | C53 | keep, spec note |  | (unchanged) Spec check: AB and ABA forms also appear in dance-pattern-puzzle (3-5); keep the music on form and the dance on movement. |  |
| speedometer | Speedometer | 9-12 | planned | C53 | keep, spec note |  | (unchanged) Spec check: lead with the derivative as rate; graph matching belongs to the live motion-graph-match. |  |
| inbox-simulator | Inbox Simulator | 9-12 | planned | C53 | keep, spec note |  | (unchanged) Spec check: stay on email and register; job interviews belong to interview-simulator. |  |
| prototype-lab | Prototype Lab | 9-12 | planned | C53 | keep, spec note |  | (unchanged) Spec check: iterate one product; breaking down a global problem belongs to design-challenge-studio. |  |
| population-dashboard | Population Dashboard | 9-12 | planned | C54 | keep |  | (unchanged) | Keep as written (recommended once energy-accountant takes HS-LS2-5, W3) OR Move to the HS-ESS2-7 gap: 'Living Planet: Scrub through four billion years and watch life and Earth change each other: microbes fill the air with oxygen, plants build soil, reefs build coastlines.' Needs a new module row and leaves science-12-population-and-resources without a tool. |
| voice-switcher | Voice Switcher | 6-8 | planned | C55 | keep |  | (unchanged) | Keep (recommended): news headlines that hide who is to blame are the strongest passive-voice hook in the catalog OR Reshape to Play-by-Play Voice: sports commentary switching between active and passive voice |
<!-- decision-table:end -->

## Decide before specs: wave 1 neighbors

Four wave 1 tools have a planned neighbor or a standard that should be settled before their spec is written. festival-passport is C01. The other three:

### W1. make-ten-machine (math, g1, wave 1)

- **Neighbors:** ten-frame-factory (K) is a factory of ten frames beside make-ten-machine's conveyor of counters. bundle-bakery (g1) had cookies rolling off a belt into boxes of ten; C13 turns it into Crayon Boxes with no conveyor. sound-elevator (live) shares only the broad "machine" setting.
- **Decide:** make-ten-machine owns the conveyor and tens-packing picture in K-2 math. Retitle ten-frame-factory; its concept has no factory in it.

<!-- fixes:W1:start -->
- **make-ten-machine** (keep, spec note) Wave 1. Owns the conveyor and tens-packing picture in K-2 math; ten-frame-factory is retitled and bundle-bakery leaves the conveyor (Crayon Boxes).
- **ten-frame-factory** (rename): **Ten and Some More**. Factory title beside make-ten-machine's conveyor (wave 1); the concept has no factory in it.
<!-- fixes:W1:end -->

### W2. town-planner-disaster-ready (science, g4, wave 1)

- **Neighbor:** settle-the-valley (social studies, g4) builds farms, dams and roads and watches the land respond, so both grade 4 tools would place dams against floods.
- **Decide:** town-planner owns hazards, floods and dams in grade 4. settle-the-valley keeps people changing the land and leaves hazards out; its module (D2.Geo.4, D2.Geo.5) does not need them.

<!-- fixes:W2:start -->
- **town-planner-disaster-ready** (keep, spec note) Wave 1. Owns hazards, floods and dams in grade 4; settle-the-valley is trimmed to leave them out.
- **settle-the-valley** (reshape): Settle a valley: choose where farms, homes and roads go and see how the land and the people change each other, from cleared forests and worn-out soil to new trails and trade.
<!-- fixes:W2:end -->

### W3. energy-accountant (science, g9, wave 1) and HS-LS2-5

- **The choice:** HS-LS2-5 (the carbon cycle across biosphere, atmosphere, hydrosphere and geosphere) has no module. energy-accountant's ledger already tracks carbon through photosynthesis and respiration. The first draft re-pointed population-dashboard there as "Carbon Relay", which would have put the same photosynthesis and respiration hops beside energy-accountant, needed a new module row, and left science-12-population-and-resources with no tool.
- **Recommended:** add HS-LS2-5 (and, if wanted, HS-LS2-3) to energy-accountant's module before its spec is written, and let the spec extend the ledger one step past the cell into air, ocean and rock. That is a data edit, outside this pass. population-dashboard then stays as written (C54).

<!-- fixes:W3:start -->
- **energy-accountant** (add a standard) Wave 1. Its carbon and energy ledger already models photosynthesis and respiration; HS-LS2-5 is the carbon cycle across the spheres and has no module.
  - Option: Add HS-LS2-5 (and optionally HS-LS2-3) to its module before the wave 1 spec (recommended)
  - Option: Leave it and give HS-LS2-5 its own tool later (a new module row; an earlier draft re-pointed population-dashboard there as 'Carbon Relay')
<!-- fixes:W3:end -->

## Clusters

Tool notation: id (subject, grade, live / planned / spec). Tags are the ones in tags.csv: skill_key, action, setting_group. "Below the bar" means fewer than 2 of the 3 tags match, but the picture a class sees repeats.

### A. Clashes with live tools

### C01. Passport stamps twice in K-2

- **Tools:** festival-passport (social studies, g1, planned, wave 1); art-passport (arts, K-2, live); me-on-the-map (social studies, K, live)
- **Kind:** clash with a live tool
- **Tags matched:** with art-passport: action (explore) and setting (travel-map: a world map with passport stamps). With me-on-the-map: action and setting.
- **Fix:**
<!-- fixes:C01:start -->
- **festival-passport** (reshape): **Festival Parade**. Floats from festivals around the world roll past on the projector; the class guesses what is being celebrated from the food, music and clothes, then hears the story behind it, sees where it happens on the map, and joins in one song or move.
<!-- fixes:C01:end -->

### C02. Coding a creature through a garden, K-2

- **Tools:** bee-bot-garden (CS, g1, planned); loop-garden (CS, g2, live); robot-dance (CS, K, live)
- **Kind:** clash with a live tool, plus a trademark
- **Tags matched:** with loop-garden: action (program) and setting (garden-farm). With robot-dance: skill (sequence-debug) and action (program).
- **Why it matters:** its codes (E1-ALG-PS-01, E1-PRO-PD-04, E1-PRO-TR-07) are the grade 1 versions of the K and g2 indicators, so the skill stays and only the angle, setting and name move.
- **Fix:**
<!-- fixes:C02:start -->
- **bee-bot-garden** (reshape): **Mouse Mail Route**. The class lays arrow cards to send a mail mouse across a snowy town grid; before it runs, kids trace the route with a finger and predict where it will stop, then run it and fix the card that sent it the wrong way.
<!-- fixes:C02:end -->

### C03. Computer parts twice in K-2

- **Tools:** input-output-machine (CS, g2, planned); computer-builder (CS, g1, live)
- **Kind:** clash with a live tool
- **Tags matched:** skill (hardware-parts: what each part does, input to output) and setting (a computer). The live tool already has the keyboard typing onto the screen and the speakers playing.
- **Fix:** move away from the desktop computer; E2-SYS-HW-11 stays.
<!-- fixes:C03:start -->
- **input-output-machine** (reshape): **Takes In, Gives Out**. A tablet, a game controller, a smart speaker and a microwave; the class sorts each part into 'takes in' or 'gives out', then predicts what the gadget does when one input is covered.
<!-- fixes:C03:end -->

### C04. Study design beside poll-workshop

- **Tools:** design-the-study (math, g12, planned); poll-workshop (math, g11, live)
- **Kind:** clash with a live tool
- **Tags matched:** skill (study-design: both modules carry S-IC.B) and setting (newsroom: a poll headline, a journal editor).
- **Why it matters:** the live tool already covers sampling methods, question wording and bias. design-the-study keeps experiments, which its module names (random assignment).
- **Fix:**
<!-- fixes:C04:start -->
- **design-the-study** (reshape): Test whether energy drinks really speed up reaction times: choose random assignment, a control group, blinding and a placebo, and a skeptical journal editor shows how each missing piece lets a hidden variable fake the result. Surveys and sampling stay with poll-workshop.
<!-- fixes:C04:end -->

### C05. Community project planners, 9-12

- **Tools:** local-changemaker-planner (social studies, g12, planned); community-project-planner (SEL, 9-12, live)
- **Kind:** clash with a live tool
- **Tags matched:** skill (community-project) and setting (town). The titles are near-identical.
- **Fix:** civics only (who decides, public comment, testimony, petitions); team and resource management stay with the live tool.
<!-- fixes:C05:start -->
- **local-changemaker-planner** (reshape): **Who Decides?**. Pick a local problem (a dangerous crosswalk, a closed library branch) and trace who actually decides it: which office, which meeting, when public comment opens; then draft the testimony or petition that reaches them.
<!-- fixes:C05:end -->

### C06. A city to run beside a live city tycoon

- **Tools:** power-grid-tycoon (science, g12, planned); community-project-planner (SEL, 9-12, live)
- **Kind:** clash with a live tool, plus a trademark
- **Tags matched:** action (manage) and setting (town). The title is also the name of the Power Grid board game.
- **Fix:** keep the energy tradeoffs (HS-ESS3-2) and move the player into a grid control room.
<!-- fixes:C06:start -->
- **power-grid-tycoon** (reshape): **Grid Operator**. Keep a city's lights on from the grid control room, mixing coal, gas, solar, wind and nuclear; balance cost, reliability and emissions through a heat wave and a still, cloudy week.
<!-- fixes:C06:end -->

### C07. Communication and boundaries, 6-8

- **Tools:** boundaries-builder (health-PE, 6-8, planned); conflict-coach (SEL, 6-8, live)
- **Kind:** clash with a live tool
- **Tags matched:** skill (conflict-resolution) and action (converse through peer scenarios).
- **Why it matters:** NHES.S4 is also on feelings-faces and pressure-point, so the framing is free to change. Relationships are a required 6-8 health topic, so the reshape keeps them rather than moving the tool.
- **Fix:**
<!-- fixes:C07:start -->
- **boundaries-builder** (reshape): **Relationship Spectrum**. Place short friendship and dating scenarios on a line from healthy to unhealthy; red-flag cards explain each placement, and a 'what you could say' card practices setting the boundary.
  - Option: Reshape to Relationship Spectrum (recommended)
  - Option: Move to the 6-8 nutrition gap: 'Day of Meals: Plan a day of meals and snacks around a busy schedule (practice, a test, a late night), then see how energy, focus and mood hold up and adjust the plan.'
<!-- fixes:C07:end -->

### C08. Savings that grow, 9-12

- **Tools:** compound-interest-garden (CTE, 9-12, planned); savings-plan (math, g11, live); market-time-machine (CTE, 9-12, live)
- **Kind:** clash with a live tool
- **Tags matched:** with savings-plan: skill (savings-growth) and action (simulate-tune). market-time-machine also grows money over decades.
- **Fix:** the emergency fund leads (its module names it first); compounding becomes the payoff.
<!-- fixes:C08:start -->
- **compound-interest-garden** (reshape): **Rainy Day Fund**. Live a year of surprise costs (a flat tire, a cracked phone, a vet bill) with and without an emergency fund, then see what the fund grows to if it sits untouched for ten years.
<!-- fixes:C08:end -->

### C09. Two roller coasters in grade 11

- **Tools:** roller-coaster-physics (science, g11, planned); rollercoaster-polynomials (math, g11, live); ferris-wheel (math, g11, live)
- **Kind:** clash with a live tool
- **Tags matched:** action (build a track) and setting (amusement park), and near-identical titles. ferris-wheel is a third ride in grade 11.
- **Fix:**
<!-- fixes:C09:start -->
- **roller-coaster-physics** (reshape): **Zipline**. Design a zipline from a cliff platform to a far tree; with friction on, energy conservation decides whether the rider reaches the far platform and how hard the brake has to work.
<!-- fixes:C09:end -->

### C10. Copying moves on the board, K-2

- **Tools:** move-like-me (arts dance, K-2, planned); animal-moves (health-PE, K-2, live); beat-buddies (arts music, K-2, live)
- **Kind:** clash with a live tool
- **Tags matched:** with animal-moves: skill (locomotor-skills) and action (move-along). beat-buddies also has the class moving like animals.
- **Fix:** levels and pathways (its module names levels), no animals, no freeze game.
<!-- fixes:C10:start -->
- **move-like-me** (reshape): **Levels and Pathways**. An animated dancer stretches, twists and bends at high, middle and low levels, then travels straight, curved and zigzag pathways; the class copies each one, then invents a pathway for the dancer to follow.
<!-- fixes:C10:end -->

### C11. Safari twice in K-2

- **Tools:** text-feature-safari (ELA, g1, planned); orchestra-zoo (arts, K-2, live); line-safari (arts, K-2, live)
- **Kind:** clash with a live tool
- **Tags matched:** with orchestra-zoo: action (explore) and setting (animals). With line-safari: the safari setting and the title word.
- **Fix:** a page makeover. A hide-and-reveal page was considered and dropped: it would match big-book-pointer (K) on action and setting.
<!-- fixes:C11:start -->
- **text-feature-safari** (reshape): **Page Makeover**. A plain page about ocean animals is hard to use; the class adds a heading, captions, labels and a glossary one at a time and sees which question each one helps answer faster.
<!-- fixes:C11:end -->

### C12. A detective case in K-2

- **Tools:** book-detectives (ELA, K, planned); resource-detective (social studies, g2, live)
- **Kind:** clash with a live tool
- **Tags matched:** action (investigate) and setting (detective).
- **Fix:** keeps all of its module (main topic, key details, author and illustrator).
<!-- fixes:C12:start -->
- **book-detectives** (reshape): **Meet the Book Makers**. An author and an illustrator take turns showing their part of a picture book; the class decides which job made each part of the page (words or pictures) and names the book's main topic and two details that tell about it.
<!-- fixes:C12:end -->

### C13. Shops and bakeries in K-2

- **Tools:** market-day (social studies, g1, planned); bundle-bakery (math, g1, planned); corner-store (math, g2, live); blend-bakery (ELA, g1, planned); piggy-bank-planner (social studies, g2, planned)
- **Kind:** clash with a live tool
- **Tags matched:** market-day and bundle-bakery each match corner-store and each other on action (manage) and setting (shop-food). bundle-bakery and blend-bakery are both grade 1 bakeries with near-identical titles.
- **Why it matters:** a sort is not an option for market-day, because K-2 social studies already has three sorts. A cookie conveyor for bundle-bakery would repeat make-ten-machine (W1), and keeping the tycoon would leave a second shop beside corner-store.
- **Fix:** keep piggy-bank-planner (money at home, not a stall) and blend-bakery (its title stays once bundle-bakery leaves the bakery). Reshape the other two; the bundle-bakery call is closed.
<!-- fixes:C13:start -->
- **market-day** (reshape): With five tokens, the class shops a weekend market as consumers; each stall sells a good or offers a service, every choice means giving something else up, and the stall owners explain what they made or did.
- **bundle-bakery** (reshape): **Crayon Boxes**. Pack the class's loose crayons into boxes of ten for every table; say how many boxes and loose crayons, then compare two classrooms' supplies with >, = and <.
<!-- fixes:C13:end -->

### C14. Kitchens in 6-8

- **Tools:** pizza-physics (math, g7, planned); reaction-kitchen (science, g7, planned); smoothie-lab (math, g6, live)
- **Kind:** clash with a live tool
- **Tags matched:** pizza-physics against smoothie-lab and reaction-kitchen: action (experiment) and setting (kitchen-food).
- **Fix:** keep reaction-kitchen (kitchen chemistry is the standard hook; it still hits smoothie-lab, kept in C57). Reshape pizza-physics. The first draft's title, "Round Up", read as rounding in a math catalog.
<!-- fixes:C14:start -->
- **pizza-physics** (reshape): **Big Wheel, Small Wheel**. Settle classic round-object arguments (one big trampoline or two small ones? a 26-inch bike wheel or a 20-inch?) by measuring circumference and area.
<!-- fixes:C14:end -->


### Same story, setting or picture as a live tool (below the bar)

### C15. The Three Little Pigs twice in grade 2

- **Tools:** two-sides-theater (ELA, g2, planned); three-pigs-lab (science, g2, live)
- **Kind:** same story as a live tool
- **Tags matched:** setting (folktale); the story itself repeats in the same grade. (two-sides-theater's setting was retagged from stage to folktale, so the first draft's stage match with story-dress-up is gone.)
- **Fix:**
<!-- fixes:C15:start -->
- **two-sides-theater** (reshape): **Bear's Side of the Story**. Goldilocks and Baby Bear tell the same morning (beginning, middle and end) two ways; tap a character to hear the scene in their voice and see their thought bubble, then the class voices the next scene as the other character.
<!-- fixes:C15:end -->

### C16. An elevator twice in K-2

- **Tools:** elevator-hundred (math, g1, planned); sound-elevator (arts, K-2, live); hundred-hop (math, K, live)
- **Kind:** same setting as a live tool
- **Tags matched:** setting only (an elevator going up and down), plus the title word.
- **Why it matters:** the first draft's fix (a gecko climbing a hundred chart) was the live hundred-hop: an animal moving on a 1 to 100 chart by tens. The new fix drops both the animal and the chart.
- **Fix:**
<!-- fixes:C16:start -->
- **elevator-hundred** (reshape): **Bead Slider**. Slide beads on a 100-bead string, ten at a time and one at a time, to solve 34 + 20 or 47 + 6, then write the slides as an equation.
<!-- fixes:C16:end -->

### C17. A pond twice in kindergarten math

- **Tools:** pattern-block-pond (math, K, planned); hundred-hop (math, K, live)
- **Kind:** same setting as a live tool
- **Tags matched:** setting (nature: both are pond scenes in kindergarten math).
- **Fix:**
<!-- fixes:C17:start -->
- **pattern-block-pond** (reshape): **Pattern Block Windows**. Snap pattern blocks together to fill a stained-glass window outline; the window glows when two triangles make a rhombus.
<!-- fixes:C17:end -->

### C18. Shape hunting in kindergarten

- **Tools:** shape-spy (math, K, planned); line-safari (arts, K-2, live, has a shape-hunt mode); shape-talk (ELD, K-2, live)
- **Kind:** same skill as a live tool
- **Tags matched:** skill (naming 2D shapes) with line-safari's hunt mode and shape-talk.
- **Fix:** lead with the parts of K.G.A the live tools skip: 3D solids, flat versus solid, and position words.
<!-- fixes:C18:start -->
- **shape-spy** (reshape): **Hide and Seek Solids**. A teddy bear hides beside, above, behind or under 3D solids in a toy room; the class names the solid, says whether it is flat or solid, and calls the position word before the teacher lifts the cover.
<!-- fixes:C18:end -->

### C19. Food builders in K-2

- **Tools:** pizza-party (math, g1, planned); hamburger-paragraph (ELA, g2, live); lunch-tray-builder (health-PE, K-2, live)
- **Kind:** same setting as live tools (load relief)
- **Tags matched:** setting (kitchen-food). pizza-party's action was retagged from build to manipulate, so this is no longer 2 of 3; it stays because two of the three K-2 food builders are live and pizza also appears in 3-5 and 6-8.
- **Fix:**
<!-- fixes:C19:start -->
- **pizza-party** (reshape): **Fair Folds**. Fold and cut paper shapes (squares, circles, rectangles) into halves and fourths for a class art project; uneven cuts leave a friend with a smaller piece, and the class spots which cuts are fair.
<!-- fixes:C19:end -->


### B. Clashes between planned tools

### C20. Retelling on a puppet stage, K-2

- **Tools:** retell-puppets (ELD, K-2, planned); story-stage (ELA, K, planned)
- **Kind:** clash
- **Tags matched:** all three in the first draft's reading (retelling, puppets acted out, a stage), and the same family. story-problem-theater's stage tag was a title word, so it drops out.
- **Fix:** reshape recommended; merge is the alternative. Today each module maps to exactly one tool, so a merge needs a tool that serves two modules.
<!-- fixes:C20:start -->
- **retell-puppets** (reshape): **Bedtime Retell**. A sleepy puppet friend asks to hear a short story again; learners retell the beginning, middle and end with sentence frames and picture prompts, answering 'what happened first? then what?', and the friend drifts off after a complete retell.
  - Option: Reshape to Bedtime Retell (recommended)
  - Option: Merge into story-stage as an ELD sentence-frame mode (needs one tool serving two modules)
<!-- fixes:C20:end -->

### C21. Class votes, K-2

- **Tools:** class-snack-vote (CS, K, planned); class-poll (math, g1, planned); lunch-line-data (math, g2, planned); toy-box-sort (math, K, planned)
- **Kind:** clash
- **Tags matched:** class-snack-vote and class-poll: skill (class-data) and action (analyze-data); class-poll's concept already says "pets or snacks". class-snack-vote and lunch-line-data: action and setting (food data).
- **Why it matters:** the CS module standards (EK-DAT-DC-08, EK-DAT-DI-09) are on no other module, so the slot stays and the angle moves to the computer. The first draft counted colored blocks, which repeated toy-box-sort (K: sort toys by color and count the piles); the new line counts bounces.
- **Fix:**
<!-- fixes:C21:start -->
- **class-snack-vote** (reshape): **Me vs the Counter**. A ball bounces for ten seconds; half the class tallies the bounces by hand while the computer counts them too; compare the totals and the mistakes, then use the computer's counts to pick the bounciest ball.
<!-- fixes:C21:end -->

### C22. Teaching an AI from pictures, K-2

- **Tools:** pattern-finder (CS, g1, planned); teach-the-robot (CS, g2, planned)
- **Kind:** clash
- **Tags matched:** all three once pattern-finder's action is corrected from sort to experiment: skill (ai-patterns), action (the class trains it) and setting (robot).
- **Fix:** keep teach-the-robot (training by examples is its standard). Reshape pattern-finder; its module also carries E1-SOC-HU-15, which an everyday-uses angle fits. The first draft's secret-keeper reshape is dropped: with the action fixed, secret-keeper matches only on the robot setting, and its owl mail carrier would have sat beside C02's mail mouse.
<!-- fixes:C22:start -->
- **pattern-finder** (reshape): **Spot the AI**. Everyday scenes play out (a phone unlocking with a face, a map choosing a route, a toy that answers back); the class guesses which ones use AI, and the teacher reveals the pattern each one learned from.
<!-- fixes:C22:end -->

### C23. Counterclaims three times in 6-8 ELA

- **Tools:** debate-prep-desk (ELA, g6, planned); counterclaim-ping-pong (ELA, g7, planned); town-hall-debate (ELA, g8, planned); agora-assembly (social studies, g6, planned); constitutional-convention (social studies, g8, planned)
- **Kind:** clash
- **Tags matched:** ping-pong and town-hall: skill (counterclaims) and action (debate). town-hall against both assemblies: action and setting (council-debate). debate-prep-desk against the other two: skill only (its setting was retagged to generic), but its concept ends in counterargument practice.
- **Why it matters:** W.6.1 has no counterclaims. W.6.1d and W.7.1d already require formal style; what grade 8 adds is acknowledging and distinguishing the opposing claim.
- **Fix:** keep counterclaim-ping-pong (grade 7 owns counterclaims). Reshape the other two. For Reason Builder, the spec should keep the weight on writing the paragraph; sorting facts by relevance alone leans toward logic-gym (g7) and argument-x-ray (g6).
<!-- fixes:C23:start -->
- **debate-prep-desk** (reshape): **Reason Builder**. Pick a kid-relevant issue (a later school start?), write a claim, then choose which of eight facts actually support it; off-topic and weak facts bounce out, and the paragraph builds from the ones that hold.
- **town-hall-debate** (reshape): **Claim vs Claim**. A group-chat argument about a school rule gets rewritten for the school board: sort each message into your claim, an opposing claim or neither, then write a formal paragraph that names the strongest opposing claim fairly and shows exactly where the two part ways.
<!-- fixes:C23:end -->

### C24. Training a classifier, 3-5

- **Tools:** fruit-sorter-ai (CS, g5, planned); biased-bot (CS, g4, planned); kitchen-lab (math, g3, planned)
- **Kind:** clash
- **Tags matched:** fruit-sorter-ai and biased-bot: skill (train-classifier) and action (experiment); it is C22 one band up. fruit-sorter-ai and kitchen-lab: action and setting (food).
- **Fix:** biased-bot keeps skewed data; fruit-sorter-ai leads with features and moves from fruit to leaves.
<!-- fixes:C24:start -->
- **fruit-sorter-ai** (reshape): **Leaf Sorter AI**. Choose which features (color, edge, shape, size) a classifier may use to sort leaves by tree; see which features separate them and which only add noise, then test it on leaves it has never seen.
<!-- fixes:C24:end -->

### C25. Switching interpretations of a scene, 9-12

- **Tools:** director-s-chair (arts, 9-12, planned); globe-theatre-stage (ELA, g12, planned)
- **Kind:** clash
- **Tags matched:** skill (staging-interpretation) and setting (stage).
- **Fix:** director-s-chair leads with its other standard, TH:Cn11 (theater traditions).
<!-- fixes:C25:start -->
- **director-s-chair** (reshape): Stage the same short scene as a Greek chorus, Noh, commedia, Elizabethan and modern realist production; compare what each tradition's staging rules make the audience notice.
<!-- fixes:C25:end -->

### C26. Founding documents and later speeches, 9-12

- **Tools:** premise-inspector (ELA, g11, planned); founding-words-explorer (ELA, g9, planned)
- **Kind:** same skill, planned (below the bar: both settings are real documents, which is generic)
- **Tags matched:** skill (founding-documents). Same texts and the same move: founding documents read alongside later speeches.
- **Fix:** premise-inspector takes the later responses (RI.11-12.9); founding-words-explorer drops "echoes in later speeches" and keeps RI.9-10.9's central ideas.
<!-- fixes:C26:start -->
- **premise-inspector** (reshape): Lay out the Declaration's argument as premises and a conclusion, then test later responses (Seneca Falls, Douglass's Fifth of July speech, the Gettysburg Address) by which premise each accepts, stretches or rejects.
- **founding-words-explorer** (reshape): Read founding documents with plain-English layers and historical context; trace how each document's central ideas develop across its sections.
<!-- fixes:C26:end -->

### C27. Fossils and rock layers, 3-5

- **Tools:** fossil-dig (science, g3, planned); canyon-reader (science, g4, planned)
- **Kind:** clash
- **Tags matched:** skill (fossils-rock-layers) and setting (digging or reading layers).
- **Fix:** canyon-reader keeps the layers (4-ESS1-1); fossil-dig drops them and keeps 3-LS4-1, 3-LS4-3 and 3-LS4-4.
<!-- fixes:C27:start -->
- **fossil-dig** (reshape): **Fossil Clues**. Match each fossil (a fish, a fern, a coral) to the place it lived, then piece together what this desert used to be and which animals could survive the change.
<!-- fixes:C27:end -->

### C28. Quoting as proof, 3-5

- **Tools:** evidence-locker (ELA, g4, planned); inference-interrogation (ELA, g5, planned)
- **Kind:** clash
- **Tags matched:** skill (quote-evidence) and setting (detective: an evidence locker, an interrogation).
- **Fix:** C31 keeps inference-interrogation as the 3-5 detective, so evidence-locker drops the evidence room and leads with W.4.9 writing.
<!-- fixes:C28:start -->
- **evidence-locker** (reshape): **Quote Picker**. For each reason in an opinion paragraph, choose the quote that backs it and write the sentence that introduces it; a quote that only repeats the reason fades out.
<!-- fixes:C28:end -->

### C29. Polynomial area models in grade 9

- **Tools:** polynomial-garden (math, g9, planned); algebra-tile-studio (math, g9, planned); expression-garden (math, g6, planned)
- **Kind:** same picture, planned (skill key shared, below the bar)
- **Tags matched:** skill (polynomial-area-model): the same rectangle area model in the same grade, for multiplying and for factoring. expression-garden is the same algebra-tile garden one band down. "Garden" is in eight titles.
- **Why it matters:** the first draft's fix, "Polynomial Floor Plan", was still a rectangle area model.
- **Fix:** polynomials as a number system (A-APR.1 says they behave like the integers).
<!-- fixes:C29:start -->
- **polynomial-garden** (reshape): **Polynomials as Numbers**. Set x = 10 and watch every polynomial become an ordinary number; multiplying polynomials turns into long multiplication without carrying, and like terms line up like place-value columns.
<!-- fixes:C29:end -->

### C30. Courtrooms in 9-12

- **Tools:** fair-use-court (library, 9-12, planned); robber-baron-or-captain (social studies, g11, planned); courtroom-statistics (math, g12, planned); supreme-court-simulator (social studies, g12, planned)
- **Kind:** clash
- **Tags matched:** all six pairs share action (debate) and setting (courtroom).
- **Fix:** keep supreme-court-simulator (the court is the subject) and courtroom-statistics ("the null is innocent until proven guilty" is the standard teaching frame; the first draft's alternative, a fair-coin simulation, would repeat fair-dice-investigation in the same grade). The call is closed. Reshape the other two.
<!-- fixes:C30:start -->
- **courtroom-statistics** (keep) Kept: 'the null is innocent until proven guilty' is the standard teaching frame; the alternative would repeat fair-dice-investigation. Call closed.
- **fair-use-court** (reshape): **Fair Use Review**. Work as a reviewer for a student video site; weigh each upload (a meme, a remix, a class project) against the four fair use factors, then cite each source and choose a Creative Commons license for your own work.
- **robber-baron-or-captain** (reshape): **Baron or Builder?**. Place industrialists on a line from robber baron to captain of industry using evidence cards (wages, prices, philanthropy, monopolies); the class compares placements and argues the hardest cases.
<!-- fixes:C30:end -->

### C31. Mysteries and mock trials in 3-5

- **Tools:** label-detective (health-PE, 3-5, live); inference-interrogation (ELA, g5, planned); pattern-detective (math, g3, planned); network-detective (CS, g4, planned); claim-court (ELA, g5, planned); shape-courtroom (math, g5, planned)
- **Kind:** clash
- **Tags matched:** the four mysteries share action (investigate) and setting (detective). claim-court and shape-courtroom are two mock trials in grade 5 (setting courtroom); shape-courtroom also repeats shape-family-tree's "is a square a rectangle?" argument (g3).
- **Why it matters:** every mystery-format tool is tagged detective, so this is partly the format. C32 treats the four 9-12 mysteries the same way. The reshapes here are setting relief: four cases and two trials in one band is a lot.
- **Fix:** keep inference-interrogation (proving an inference with a quote is real detective work) and claim-court. Reshape three.
<!-- fixes:C31:start -->
- **pattern-detective** (reshape): **Pattern Painter**. Color the multiplication table to make patterns pop (every even product, every multiple of 5, the square numbers), predict the next colored square and explain the rule in one sentence, then use a pattern to crack a two-step word problem.
- **network-detective** (reshape): **Help Desk Heroes**. Families call the help desk because a device won't connect; ask the right questions (wired or wireless? signed in, or just not allowed?) and fix each one.
- **shape-courtroom** (reshape): **Property Sieve**. Shapes drop through a stack of sieves (four sides, parallel pairs, right angles, equal sides) and stop at the most specific name they earn; the class predicts where a square lands.
<!-- fixes:C31:end -->

### C32. Mysteries in 9-12

- **Tools:** satire-decoder (ELA, 9-12, spec); health-claim-checker (health-PE, 9-12, planned); detective-del-pasado (world languages, 6-12, planned); ph-detective (science, g10, planned); misleading-charts (math, 6-8, planned)
- **Kind:** clash
- **Tags matched:** all six pairs of the four 9-12 tools share action (investigate) and setting (detective). detective-del-pasado also hits misleading-charts in 6-8.
- **Fix:** keep satire-decoder (spec written), health-claim-checker (investigating a viral claim is the skill) and detective-del-pasado (a mystery story is how it practices past tenses). Rename ph-detective, which is also one of the twelve "Detective" titles; identifying unknowns by pH is real lab work, so the case frame stays.
<!-- fixes:C32:start -->
- **ph-detective** (rename): **Mystery Liquids**. One of four 9-12 mysteries and one of twelve 'Detective' titles; identifying unknowns by pH is real lab work, so the case frame stays.
  - Option: Rename to Mystery Liquids, concept unchanged (recommended)
  - Option: Move to the HS-PS3-4 gap: 'Even Out: Drop hot metal into cold water, mix hot and cold water, and predict the final temperature; watch energy flow until both sides match.' Needs a new module row.
<!-- fixes:C32:end -->

### C. Trademarks

### C33. Trademark titles

- **Tools:** mad-libs-machine (ELA, g3); food-web-jenga (science, g5); battleship-grid (math, g5); rube-goldberg-workshop (science, g4); lemonade-monopoly (social studies, g12). All planned. bee-bot-garden (C02) and power-grid-tycoon (C06) are filed with their live clashes.
- **Kind:** trademark
- **Tags matched:** none needed; the risk is the name. Mad Libs is a Penguin Random House mark; Jenga, Battleship and Monopoly are Hasbro marks; the Rube Goldberg name is licensed by Rube Goldberg Inc. lemonade-monopoly also echoes lemonade-stand (g6) and shares a family and D2.Eco.4.9-12 with the live concert-ticket-market.
- **Fix:** rename three; reshape battleship-grid (distance feedback makes it more than the board game) and lemonade-monopoly.
<!-- fixes:C33:start -->
- **mad-libs-machine** (rename): **Story Blanks**. Mad Libs is a Penguin Random House mark.
- **food-web-jenga** (rename): **Food Web Wobble**. Jenga is a Hasbro mark.
- **battleship-grid** (reshape): **Sea Search Grid**. Hide boats on the first quadrant and call coordinates to find a partner's; each miss tells you how far off you were.
- **rube-goldberg-workshop** (rename): **Contraption Workshop**. The Rube Goldberg name is licensed by Rube Goldberg Inc.
- **lemonade-monopoly** (reshape): **The Buyout**. The same phone-charger market runs twice, once with four competing makers and once after one buys out the rest; compare prices, choice and quality side by side, then see what regulators can do.
<!-- fixes:C33:end -->

### D. Setting repeats and smaller pairs

### C34. Chain-reaction machines in 3-5

- **Tools:** chain-reaction (ELD, 3-5, planned); rube-goldberg-workshop (science, g4, planned)
- **Kind:** clash
- **Tags matched:** action (build) and setting (robot-machine: a chain-reaction machine).
- **Fix:** keep the science contraption (4-PS3-4 asks students to design a device that converts energy), retitled in C33.
<!-- fixes:C34:start -->
- **chain-reaction** (reshape): **Rewind It**. A picture story (a dropped ice cream, a missed bus) runs backward one step at a time; learners link each step with because, so or as a result to rewind it to the start.
<!-- fixes:C34:end -->

### C35. Treasure hunts in K-2

- **Tools:** treasure-map-steps (math, g2); place-value-vault (math, g2); story-map-treasure (ELA, g1); compass-rose-quest (social studies, g1). All planned.
- **Kind:** clash
- **Tags matched:** treasure-map-steps and place-value-vault: action (solve) and setting (treasure). Four treasure hunts in one band.
- **Fix:** keep compass-rose-quest (maps belong to its skill) and place-value-vault (vault codes fit place value). Reshape two.
<!-- fixes:C35:start -->
- **treasure-map-steps** (reshape): **Lost and Found**. Two-step clues about what came in and went out of the lost and found each day ('14 mittens, 6 picked up, 5 more found') point to the box that holds the missing toy.
- **story-map-treasure** (reshape): **Story Quilt**. Sew a story quilt one square at a time (beginning, problem, how the character feels, solution, lesson), choosing the picture that belongs in each square and retelling it aloud.
<!-- fixes:C35:end -->

### C36. Shops and kitchens in 3-5

- **Tools:** recipe-scaler (math, g4); grocery-run (math, g5); pizza-shop-assembly-line (social studies, g3); keyword-kitchen (library, 3-5); kitchen-lab (math, g3); fraction-kitchen (math, g5). All planned.
- **Kind:** clash
- **Tags matched:** recipe-scaler, grocery-run and pizza-shop-assembly-line: action (manage) and setting (shop-food). keyword-kitchen and kitchen-lab: action (experiment) and setting (kitchen-food). Three are measuring cups in 3-5 math.
- **Fix:** keep grocery-run, kitchen-lab and fraction-kitchen (measuring cups are the natural model for unlike denominators). Reshape three.
<!-- fixes:C36:start -->
- **recipe-scaler** (reshape): **Costume Crew**. Each costume for the school play takes 3/8 yard of fabric and 2/3 of a spool of ribbon; scale up for the whole cast and work out how many bolts and spools to buy, then add up the scraps left over.
- **pizza-shop-assembly-line** (reshape): **Paper Plane Factory**. Make paper airplanes alone, then on an assembly line with specialized jobs; productivity jumps, and the class sees how each worker depends on the others.
- **keyword-kitchen** (reshape): **Keyword Fishing**. Cast a search with the keywords you choose and see what you catch; too broad pulls in junk and too narrow catches nothing.
<!-- fixes:C36:end -->

### C37. Food shops in 6-8 math

- **Tools:** ice-cream-shop (math, g8); tax-and-tip (math, g7); lemonade-stand (math, g6). All planned.
- **Kind:** clash
- **Tags matched:** ice-cream-shop and tax-and-tip: action (manage) and setting (shop-food). lemonade-stand adds a third food stand.
- **Fix:** keep tax-and-tip and lemonade-stand. Reshape ice-cream-shop. The first draft's "Snow Globe Factory" put a second "Factory" title in grade 8 beside function-machine-factory.
<!-- fixes:C37:start -->
- **ice-cream-shop** (reshape): **Snow Globe Maker**. Design snow globes, cone-shaped tree ornaments and cylinder bases; volume decides how much water and glitter each needs and what each costs to make.
<!-- fixes:C37:end -->

### C38. Transformations and choreography

- **Tools:** dance-floor-moves (math, g8); choreography-board (arts, 6-8); stage-blocker (arts, 6-8); transformation-golf (math, g10); equation-golf (math, g9). All planned.
- **Kind:** clash
- **Tags matched:** dance-floor-moves and choreography-board: action (compose) and setting (stage). transformation-golf and equation-golf: action (solve) and setting (sports: golf); "Transformation Golf" is also a widely used Desmos activity. choreography-board and stage-blocker both place performers on a top-down stage (setting only).
- **Fix:** keep equation-golf and stage-blocker (the floor plan is its skill). Reshape three. The first draft's robot vacuum is round, so flips and turns would not show; an L-shaped tile shows every move, and resizing it separates congruent from similar (8.G.A.2, 8.G.A.4).
<!-- fixes:C38:start -->
- **dance-floor-moves** (reshape): **Dock It**. An L-shaped cargo tile must land exactly on its outline; slide, flip, turn and resize it in the fewest moves, then replay the route as a sequence of rules and decide which docks were congruent and which only similar.
- **transformation-golf** (reshape): **Shape Twins**. Each level shows a shape and its twin; map one onto the other with the fewest rigid motions, then write the sequence as the proof that they are congruent.
- **choreography-board** (reshape): Build a dance on a timeline of movement phrases (counts, levels, dynamics), then revise it; formations show in a side view as the phrases play to music.
<!-- fixes:C38:end -->

### C39. Space simulators in 9-12

- **Tools:** launch-pad (math, g9, wave 1); orbit-lab (science, g9); space-cargo (science, g11). All planned.
- **Kind:** clash
- **Tags matched:** all three pairs share action (simulate-tune) and setting (space).
- **Fix:** keep launch-pad (wave 1) and orbit-lab (orbits are the content). Reshape space-cargo. Curling adds a fifth sports setting in 9-12 (see C55).
<!-- fixes:C39:start -->
- **space-cargo** (reshape): **Curling Stones**. Slide stones of different masses with different pushes along the ice; F = ma predicts where each one stops, and sweeping changes the friction.
<!-- fixes:C39:end -->

### C40. Business tycoons and research planners, 9-12

- **Tools:** inquiry-planner (ELA, g12); ad-agency (ELA, g12); startup-tycoon (CTE, 9-12); research-notebook (ELA, g9). All planned.
- **Kind:** clash
- **Tags matched:** inquiry-planner, ad-agency and startup-tycoon: action (manage) and setting (business-money). inquiry-planner and research-notebook share the research family.
- **Fix:** keep ad-agency and startup-tycoon (their pair is kept in C57). Reshape inquiry-planner; research-notebook keeps notes, synthesis and citation.
<!-- fixes:C40:start -->
- **inquiry-planner** (reshape): **Question Sharpener**. Start from a broad interest and narrow it into a researchable question; the tool tests each draft (too broad, too narrow, already answered) and maps what you would need to find out.
<!-- fixes:C40:end -->

### C41. Islands in 9-12

- **Tools:** island-economy (science, g9); trade-island (social studies, g12); build-a-government (social studies, g12); imaginary-island (math, g11, live)
- **Kind:** clash
- **Tags matched:** island-economy and trade-island: action (manage) and setting (island). build-a-government's new nation is also an island: four in the band.
- **Fix:** keep trade-island (the two-island model is how comparative advantage is taught). Reshape two.
<!-- fixes:C41:start -->
- **island-economy** (reshape): **Lake Commons**. Manage a lake town's fish, forest and water over generations, through good years and flood years; sustainable use keeps the town going and overuse brings collapse.
- **build-a-government** (reshape): **Write the Charter**. Design a government for a newly formed country; pick a system, write its powers, and test it against crises (a disputed election, a famine, a leader who won't leave).
<!-- fixes:C41:end -->

### C42. Debates in 9-12 and the two "Pro" titles

- **Tools:** usage-panel (ELA, g11, spec, wave 1); argument-frames-pro (ELD, 9-12); data-policy-council (CS, 9-12); debate-en-español (world languages, 9-12); empire-debate (social studies, g11); argument-builder-pro (ELA, g9). All planned.
- **Kind:** title
- **Tags matched:** the five roleplays share action (debate) and setting (council-debate). argument-builder-pro and argument-frames-pro differ by one title word.
- **Fix:** keep usage-panel (spec written), empire-debate (primary-source debate), debate-en-español (debating is the language target) and data-policy-council (its product is a written policy); their pairs are kept in C57. Rename argument-frames-pro.
<!-- fixes:C42:start -->
- **argument-frames-pro** (rename): **Counterpoint Frames**. Title differs by one word from argument-builder-pro (9-12); the ELD scaffolds already make the tool different.
<!-- fixes:C42:end -->

### C43. Scams, insurance and a year of surprises, 9-12

- **Tools:** scam-shield (CTE, 9-12); capture-the-flag (CS, 9-12); compound-interest-garden, now Rainy Day Fund (CTE, 9-12); the-credit-card-diaries (CTE, 9-12). All planned.
- **Kind:** clash
- **Tags matched:** scam-shield and capture-the-flag: action (solve an escape) and setting (cyber).
- **Why it matters:** the first draft's fix ("live a year of surprises") repeated Rainy Day Fund (C08) and sat beside the-credit-card-diaries, which lives four years of choices. Insurance leads, as the module title does.
- **Fix:**
<!-- fixes:C43:start -->
- **scam-shield** (reshape): **Covered**. Compare three insurance quotes side by side; a slider trades the monthly premium against the deductible, and a claim calculator shows who pays what for a stolen bike or a fender bender. A last round sorts real insurer messages from fake 'claim refund' texts.
<!-- fixes:C43:end -->

### C44. Factories in 6-8

- **Tools:** flowchart-factory (CS, 6-8); function-machine-factory (math, g8). Both planned.
- **Kind:** title
- **Tags matched:** none beyond the title word. flowchart-factory's setting was retagged to generic (the factory is only in its title), so the first draft's 2-of-3 hit is gone.
- **Fix:** retitle; the concept stands.
<!-- fixes:C44:start -->
- **flowchart-factory** (rename): **Chore Flowcharts**. A second 'Factory' title in 6-8 beside function-machine-factory; the factory is only in the title, so the concept stands.
<!-- fixes:C44:end -->

### C45. Building metaphors in 3-5 ELA

- **Tools:** story-building-blocks (ELA, g3); essay-architect (ELA, g5); blueprint-builder (ELA, g4); blueprint-studio (math, g7); structure-spotter (ELA, g3). All planned.
- **Kind:** clash
- **Tags matched:** story-building-blocks and essay-architect: action (order) and setting (construction). blueprint-builder is a third construction image, and "Blueprint Builder" and "Blueprint Studio" are near-identical titles.
- **Why it matters:** blueprint-builder's module is RI.4.5, a reading standard, but the first draft's fix was still a writing task, and its pattern cards repeated structure-spotter (g3).
- **Fix:** keep story-building-blocks. Reshape two.
<!-- fixes:C45:start -->
- **essay-architect** (reshape): **Essay Train**. Paragraphs are train cars; each coupling is a transition, and a weak one lets the cars drift apart until the order and the links make sense.
- **blueprint-builder** (reshape): **Same Facts, New Shape**. One set of facts about a hurricane appears as a timeline, a cause-and-effect chain and a problem-and-solution article; students name each structure and say which question each version answers best.
<!-- fixes:C45:end -->

### C46. Credibility tools in 6-8

- **Tools:** source-sorter (ELA, g6); fake-or-fact-lab (library, 6-8); fact-check-desk (ELA, g8). All planned.
- **Kind:** same skill, planned (below the bar)
- **Tags matched:** source-sorter and fake-or-fact-lab: skill (source-credibility).
- **Why it matters:** credibility is the whole of the library tool, but W.6.8 itself asks students to assess each source, and fake-or-fact-lab carries only AASL codes. So source-sorter keeps one quick check and leads with quoting, paraphrasing and citing.
- **Fix:**
<!-- fixes:C46:start -->
- **source-sorter** (reshape): Give each source a quick credibility check, then practice quoting it and paraphrasing it; the tool flags paraphrases that copy too closely and builds the citation for each version.
<!-- fixes:C46:end -->

### C47. Tipping scales in kindergarten math

- **Tools:** snack-scale (math, K); who-wins (math, K). Both planned.
- **Kind:** same picture, planned (below the bar)
- **Tags matched:** action (predict-reveal) and format (showdown and sandbox): both are predict, then a scale tips.
- **Fix:** one-to-one matching, which is how K.CC.C compares groups.
<!-- fixes:C47:start -->
- **snack-scale** (reshape): **Snack Lineup**. Line up two rows of snacks one to one; the leftovers show which group has more, and the class says the numbers before the teacher matches them up.
<!-- fixes:C47:end -->

### C48. Slopes for a rider in grade 8

- **Tools:** skate-park-energy (science, g8); ski-slope-designer (math, g8). Both planned.
- **Kind:** same picture, planned (below the bar)
- **Tags matched:** setting (sports): both design a slope for a rider in the same grade. "Energy Skate Park" is also the name of a well-known PhET simulation.
- **Fix:**
<!-- fixes:C48:start -->
- **skate-park-energy** (reshape): **Swing Energy**. Pull a playground swing back and let go; kinetic and potential energy trade places in a live bar chart, and a longer pull or a heavier rider changes the totals.
<!-- fixes:C48:end -->

### C49. Slicing and spinning solids, 9-12

- **Tools:** cone-slicer (math, g12); slice-it (math, g10); solid-spinner (math, g12). All planned.
- **Kind:** same picture, planned (below the bar)
- **Tags matched:** action (explore) on three slice-or-spin-a-solid explorers.
- **Fix:** cone-slicer leads with the focus and directrix definitions (G-GPE.A.3) instead of slicing.
<!-- fixes:C49:start -->
- **cone-slicer** (reshape): **Focus Finder**. Drag a point so its distances to two foci (or to a focus and a line) follow one rule, and watch an ellipse, a hyperbola or a parabola appear; then find each one's equation.
<!-- fixes:C49:end -->

### C50. Workout planners in 9-12 health

- **Tools:** meal-and-move-planner (health-PE, 9-12); fitness-program-designer (health-PE, 9-12). Both planned.
- **Kind:** same skill, planned (below the bar)
- **Tags matched:** action (plan); both plan workouts.
- **Fix:** meal-and-move-planner leads with nutrition and energy balance; FITT programming stays with fitness-program-designer.
<!-- fixes:C50:start -->
- **meal-and-move-planner** (reshape): **Game Day Fuel**. Plan a week of meals around your training days; the tool tracks energy in and out, flags gaps and extremes, and shows how the plan holds up on a game day.
<!-- fixes:C50:end -->

### E. Titles

### C51. "Detective" in twelve titles

- **Tools:** label-detective (live), resource-detective (live), detective-del-pasado, book-detectives (C12), pattern-detective and network-detective (C31), ph-detective (C32), depth-detective, root-detective-cards, screen-time-detective, data-detective, unit-detective, watershed-detective
- **Kind:** title
- **Tags matched:** title word; most are mystery format. data-detective (math, g8) also echoes the CS 6-8 module "Data Detectives".
- **Fix:** keep the two live tools and detective-del-pasado. The others are handled in their clusters or retitled here; concepts stand. New titles were checked against every title in their band.
<!-- fixes:C51:start -->
- **depth-detective** (rename): **Near and Far**. One of twelve 'Detective' titles.
- **root-detective-cards** (rename): **Root Cards**. One of twelve 'Detective' titles.
- **screen-time-detective** (rename): **My Screen Week**. One of twelve 'Detective' titles.
- **data-detective** (rename): **Trend Line**. One of twelve 'Detective' titles; echoes the CS 6-8 module 'Data Detectives'.
- **unit-detective** (rename): **Unit Sense**. One of twelve 'Detective' titles.
- **watershed-detective** (rename): **Upstream**. One of twelve 'Detective' titles.
<!-- fixes:C51:end -->

### C52. Near-identical titles in a band

- **Tools:** word-zoo (ELA, g1) and orchestra-zoo (arts, K-2, live); story-dress-up (arts, K-2), story-stage (ELA, K) and my-story-strip (ELA, K); particle-zoom (science, g5) and powers-of-ten-zoom (math, g5); summary-scaffold (ELD, 6-8) and summary-squeeze (ELA, g6); counterclaim-ping-pong (ELA, g7)
- **Kind:** title
- **Tags matched:** title words. particle-zoom and powers-of-ten-zoom are also both zoom-to-the-atom explorers in grade 5; the summary pair shares a skill.
- **Dropped from the first draft:** plot-rollercoaster is grade 6, so it does not share a band with roller-coaster-rounding (g3). theory-gym (9-12) and logic-gym (6-8) are in different bands. The first draft's "Costume Corner" would have sat beside the live Calm Corner and Corner Store.
- **Fix:**
<!-- fixes:C52:start -->
- **word-zoo** (rename): **Word Habitats**. 'Zoo' beside the live orchestra-zoo in K-2; the concept already sorts words into habitats.
- **story-dress-up** (rename): **Act It Out**. 'Story' beside story-stage and my-story-strip in K-2.
- **particle-zoom** (rename): **Too Small to See**. A zoom explorer with 'Zoom' in the title beside powers-of-ten-zoom in grade 5.
- **summary-scaffold** (rename): **Say It Short**. Same skill and a one-word title difference from summary-squeeze in 6-8.
- **counterclaim-ping-pong** (keep) Low title caution only; the tool stays the grade 7 counterclaim tool.
  - Option: Keep the title
  - Option: Rename to Counterclaim Rally ('Ping-Pong' is a registered mark for table tennis gear)
<!-- fixes:C52:end -->

### F. Spec notes and loads

### C53. Pairs for the spec check

- **Kind:** spec notes. Each pair overlaps enough that the spec writer should keep them apart, but the concepts already differ.
- **Tools:** sentence-remixer (ELA, g6) and sentence-diagram-builder (ELA, g7): skill (combining-sentences) and action (build). song-form-builder and dance-pattern-puzzle (arts, 3-5): both arrange A and B sections. speedometer (math, g12) and motion-graph-match (science, g11, live). inbox-simulator (ELD, 9-12) and interview-simulator (CTE, 9-12). prototype-lab (CTE, 9-12) and design-challenge-studio (science, g12): skill (engineering design) and setting (lab).
<!-- fixes:C53:start -->
- **sentence-remixer** (keep, spec note) Spec check: lead with style and pronouns (L.6.3, L.6.1); clause function belongs to sentence-diagram-builder (L.7.1).
- **song-form-builder** (keep, spec note) Spec check: AB and ABA forms also appear in dance-pattern-puzzle (3-5); keep the music on form and the dance on movement.
- **speedometer** (keep, spec note) Spec check: lead with the derivative as rate; graph matching belongs to the live motion-graph-match.
- **inbox-simulator** (keep, spec note) Spec check: stay on email and register; job interviews belong to interview-simulator.
- **prototype-lab** (keep, spec note) Spec check: iterate one product; breaking down a global problem belongs to design-challenge-studio.
<!-- fixes:C53:end -->

### C54. Data desks in 9-12

- **Tools:** population-dashboard (science, g12); which-model-wins and data-desk-distributions (math); economy-dashboard and where-s-my-phone-from (social studies); climate-dashboard and energy-accountant (science, wave 1); simulation-studio (CS); chart-narrator (ELD). All planned.
- **Kind:** format load
- **Tags matched:** no single pair; 9-12 has 12 data-format tools and 9 whose action is analyze-data, most of them real-data screens.
- **Fix:** keep population-dashboard once energy-accountant takes HS-LS2-5 (W3). If Cory wants one data desk fewer, its alternative is the HS-ESS2-7 gap; that needs a new module row and leaves science-12-population-and-resources with no tool.
<!-- fixes:C54:start -->
- **population-dashboard** (keep) One of 12 data-format tools in 9-12; its standards are also on island-economy and carrying-capacity.
  - Option: Keep as written (recommended once energy-accountant takes HS-LS2-5, W3)
  - Option: Move to the HS-ESS2-7 gap: 'Living Planet: Scrub through four billion years and watch life and Earth change each other: microbes fill the air with oxygen, plants build soil, reefs build coastlines.' Needs a new module row and leaves science-12-population-and-resources without a tool.
<!-- fixes:C54:end -->

### C55. Setting loads by band

- **Kind:** setting load. The "4 or more in a band" flag, applied to every band after the fixes (`python scripts/overlap/stats.py --after`):
  - K-2: animals 7, robot or machine 7, town 7, kitchen or food 6, nature 5, garden or farm 5, shops 4 (before the fixes: robot or machine 10, animals 8, kitchen or food 8, shops 5, and stage, treasure and travel map 4 each).
  - 3-5: travel map 8, sports 6, animals 6, nature 6, robot or machine 4.
  - 6-8: travel map 9, lab 6, town 6, newsroom 5, water 5, sports 4, kitchen or food 4, shops 4, vehicle 4.
  - 9-12: lab 12, business or money 10, council or debate 8, body or medical 6, sports 5, travel map 5, and 4 each for vehicle, film, nature, detective, family tree, town, newsroom and space.
- **Fix:** keep. Maps, labs, councils and money settings are native to their subjects, and the pairs inside them that meet the rule are each kept with a reason in C57. Two notes: the 6-8 newsrooms (explainer-studio, colonial-newsroom, voice-switcher, fact-check-desk, printing-press) each do different newsroom work, so voice-switcher stays; and future specs in 3-5, 6-8 and 9-12 should avoid adding another sports setting.
<!-- fixes:C55:start -->
- **voice-switcher** (keep) One of five newsroom settings in 6-8; the rule hit was between two other newsroom tools.
  - Option: Keep (recommended): news headlines that hide who is to blame are the strongest passive-voice hook in the catalog
  - Option: Reshape to Play-by-Play Voice: sports commentary switching between active and passive voice
<!-- fixes:C55:end -->

### G. Records

### C56. Live tools that overlap each other

- **Tools:** feelings-faces and feelings-weather-report (K-2, naming feelings); i-spy-science and habitat-hunt (K-2, hunting in nature photos); beat-buddies and animal-moves (K-2, moving like animals); hamburger-paragraph and lunch-tray-builder (K-2, food builders); art-passport and me-on-the-map (K-2, world maps); mind-map and resilience-map (9-12, mental health explorers); savings-plan and market-time-machine (9-12, money growing over time). All live.
- **Kind:** live-live
- **Fix:** keep (both ends are fixed points). This list is a fence for future specs: no more planned K-2 tools on naming feelings, moving like animals, building food or world maps, and no more 9-12 mental health explorers or savings-growth simulators.

### C57. Every rule hit kept

- **Kind:** record. Generated by `python scripts/overlap/build_decisions.py` from the rule run on the catalog after every fix in this file.

<!-- kept-hits:start -->
After the fixes, the rule finds 92 pairs. Every one is kept, grouped here by reason:

- **Two grade 5 space experiments on different things: gravity and shadows.** drop-zone and shadow-clock (3-5, action+setting).
- **Different skills and subjects: erosion, plant growth, people changing the land.** erosion-table and settle-the-valley (3-5, action+setting); growth-spurt and erosion-table (3-5, action+setting); growth-spurt and settle-the-valley (3-5, action+setting).
- **Maps are native to geography, history and world languages; each tool covers a different place, era or subject (fraction-trail is a number line drawn as a trail, internet-journey follows data packets).** fraction-trail and colonial-trade-routes (3-5, action+setting); fraction-trail and state-economy-map (3-5, action+setting); fraction-trail and state-quest (live) (3-5, action+setting); internet-journey and day-in-the-life (3-5, action+setting); state-economy-map and colonial-trade-routes (3-5, action+setting); state-quest (live) and colonial-trade-routes (3-5, action+setting); state-quest (live) and state-economy-map (3-5, action+setting); expansion-map and civil-war-map-room (6-8, action+setting); mundo-hispano and civil-war-map-room (6-8, action+setting); mundo-hispano and expansion-map (6-8, action+setting); world-music-map and civil-war-map-room (6-8, action+setting); world-music-map and expansion-map (6-8, action+setting); world-music-map and mundo-hispano (6-8, action+setting); ideas-that-spread and where-s-my-phone-from (9-12, action+setting); mundo-hispano and scramble-for-africa (9-12, action+setting).
- **Different writing in different subjects: headlines and a persuasive poster.** headline-writer and persuasion-poster (3-5, action+setting).
- **Mystery format: every mystery tool is tagged detective, and the content differs (C31, C32).** inference-interrogation and label-detective (live) (3-5, action+setting); misleading-charts and detective-del-pasado (6-8, action+setting); detective-del-pasado and ph-detective (9-12, action+setting); health-claim-checker and detective-del-pasado (9-12, action+setting); health-claim-checker and ph-detective (9-12, action+setting); satire-decoder and detective-del-pasado (9-12, action+setting); satire-decoder and health-claim-checker (9-12, action+setting); satire-decoder and ph-detective (9-12, action+setting).
- **Inherited traits and animal senses; how-animals-see is live.** puppy-traits and how-animals-see (live) (3-5, action+setting).
- **Historical assemblies; the event is the content.** agora-assembly and constitutional-convention (6-8, action+setting).
- **A lab bench is the default setting for science; each tool runs a different experiment.** cer-builder and molecule-builder (6-8, action+setting); collision-lab (live) and illusion-lab (9-12, action+setting); gas-law-lab and collision-lab (live) (9-12, action+setting); gas-law-lab and illusion-lab (9-12, action+setting); hand-warmer-lab and collision-lab (live) (9-12, action+setting); hand-warmer-lab and gas-law-lab (9-12, action+setting); hand-warmer-lab and illusion-lab (9-12, action+setting); prototype-lab and collision-lab (live) (9-12, action+setting); prototype-lab and gas-law-lab (9-12, action+setting); prototype-lab and hand-warmer-lab (9-12, action+setting); prototype-lab and illusion-lab (9-12, action+setting).
- **Different newsroom work: explaining a topic and partisan spin (C55).** explainer-studio and colonial-newsroom (6-8, action+setting).
- **Vehicles carry different math: equations and systems; two-trains is live.** hot-air-and-sandbags and two-trains (live) (6-8, action+setting).
- **Spec note (C53).** sentence-remixer and sentence-diagram-builder (6-8, skill+action); inbox-simulator and interview-simulator (9-12, action+setting); prototype-lab and design-challenge-studio (9-12, skill+setting).
- **sign-parameters-lab is an ASL tool for K-12 whose format is lab, not a science bench.** sign-parameters-lab and electromagnet-lab (6-8, action+setting); sign-parameters-lab and collision-lab (live) (9-12, action+setting); sign-parameters-lab and gas-law-lab (9-12, action+setting); sign-parameters-lab and hand-warmer-lab (9-12, action+setting); sign-parameters-lab and illusion-lab (9-12, action+setting); sign-parameters-lab and prototype-lab (9-12, action+setting).
- **Kitchen chemistry is the standard hook for reactions; smoothie-lab is live and about ratios (C14).** smoothie-lab (live) and reaction-kitchen (6-8, action+setting).
- **Drawing and animation; vanishing-point-studio is live.** vanishing-point-studio (live) and flipbook-studio (6-8, action+setting).
- **Passive voice in headlines and the spread of print (C55).** voice-switcher and printing-press (6-8, action+setting).
- **Persuasion campaigns and launching a business (C40).** ad-agency and startup-tycoon (9-12, action+setting).
- **Debate is the target skill in each, on different content: usage, ELD argument frames, data policy, Spanish, imperialism (C42).** argument-frames-pro and data-policy-council (9-12, action+setting); argument-frames-pro and debate-en-español (9-12, action+setting); argument-frames-pro and empire-debate (9-12, action+setting); data-policy-council and debate-en-español (9-12, action+setting); data-policy-council and empire-debate (9-12, action+setting); debate-en-español and empire-debate (9-12, action+setting); usage-panel and argument-frames-pro (9-12, action+setting); usage-panel and data-policy-council (9-12, action+setting); usage-panel and debate-en-español (9-12, action+setting); usage-panel and empire-debate (9-12, action+setting).
- **Music production (live) and wave physics (spec).** beat-lab (live) and sound-studio (9-12, action+setting).
- **The courtroom is the teaching frame in one and the subject in the other (C30).** courtroom-statistics and supreme-court-simulator (9-12, action+setting).
- **Factories are the history in both, 150 years apart.** factory-floor and home-front-mobilizer (9-12, action+setting).
- **Vectors and derivatives; speedometer has a spec note (C53).** flight-planner and speedometer (9-12, action+setting).
- **The family-tree metaphor is native to each subject: word roots, parent functions, common ancestry.** function-family-reunion and tree-of-life (9-12, action+setting); word-family-tree and function-family-reunion (9-12, action+setting); word-family-tree and tree-of-life (9-12, action+setting).
- **Quadratic projectiles (wave 1) and Kepler's laws (C39).** launch-pad and orbit-lab (9-12, action+setting).
- **Different skills; a disease test is the standard example for conditional probability (medical-test-paradox is wave 1).** medical-test-paradox and body-thermostat (9-12, action+setting); medical-test-paradox and outbreak-model (live) (9-12, action+setting); outbreak-model (live) and body-thermostat (9-12, action+setting).
- **Different skills and eras: sequences (live), monetary policy, the 1929 crash (spec).** savings-plan (live) and fed-chair (9-12, action+setting); savings-plan (live) and stock-market-1929 (9-12, action+setting); stock-market-1929 and fed-chair (9-12, action+setting).
- **Both live (C56).** art-passport (live) and me-on-the-map (live) (K-2, action+setting); beat-buddies (live) and animal-moves (live) (K-2, action+setting); feelings-faces (live) and feelings-weather-report (live) (K-2, skill+action); hamburger-paragraph (live) and lunch-tray-builder (live) (K-2, action+setting); i-spy-science (live) and habitat-hunt (live) (K-2, action+setting).
- **Weather is the science topic in one and a metaphor for feelings in the other (live).** feelings-weather-report (live) and weather-wardrobe (K-2, action+setting).
- **The creature format always means care-for; the skills differ (habits, living needs, letters).** habit-hero (live) and terrarium-pal (K-2, action+setting); letter-lanterns and habit-hero (live) (K-2, action+setting); letter-lanterns and terrarium-pal (K-2, action+setting).
- **Pies are only the reward in pie-sort; melt-or-not is live.** pie-sort and melt-or-not (live) (K-2, action+setting).
- **'Machine' is broad: pitch and making ten (W1).** sound-elevator (live) and make-ten-machine (K-2, action+setting).
- **'Sports' is broad; the skills differ.** target-toss and fact-rally (K-2, action+setting).
<!-- kept-hits:end -->

### C58. Low title cautions

- **Tools:** the data-desk family name; mind-map (live); settle-the-valley (social studies, g4); game-show-strategist (math, g12)
- **Kind:** trademark (low)
- **Fix:** keep.
  - data-desk: an internal family name, never shown to students.
  - mind-map (live): "Mind Map" is registered in some countries but is in common generic use.
  - settle-the-valley: a faint echo of Catan's "settle".
  - game-show-strategist names the Monty Hall problem, a standard name for a math problem.
  - theory-gym and logic-gym: "Gym" alone is fine; the registered mark is "Brain Gym".
  - counterclaim-ping-pong is listed as an option in C52.
