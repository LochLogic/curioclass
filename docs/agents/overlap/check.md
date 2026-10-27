# Curio Class overlap pass: cold check

**Verdict: ready with fixes.** The clusters are real, well argued and no fix touches a live tool. My check found 9 wrong tags, 22 missed clashes, 8 false or weak clashes, 17 bad or weak fixes, 8 gap corrections and 7 presentation fixes. About a dozen of these change what Cory is asked to decide. The most important ones: five fixes create new clashes (C03 with C12, C05 with C32, C09, C14 option B, C15). Three missed clashes involve live tools (computer-builder, poll-workshop, community-project-planner). Three wave 1 tools have neighbors that need a decision before their specs are written.

How I checked: I re-tagged 127 tools from their concept lines (all 65 tools named in C01 to C20, plus a stratified sample of 62 with at least one per subject and band). I read plan.md for the live tools involved. I reran the action and setting legs of the clash rule from tags.csv. I read every band block of data/tools-concepts.csv by hand. I checked each proposed concept against its module in data/modules.csv, and checked the CSTA and NGSS gap claims against data/standards and the full NGSS PE list. Scratch scripts are in the session scratchpad (overlap-check).

## 1. Wrong tags

127 tools re-tagged (381 tag fields). I disagree on 9 tools (7 percent of tools, 2.4 percent of fields). Five of them change a rule hit in a cluster.

| Tool | Field | tags.csv | Should be | Effect on clusters |
|---|---|---|---|---|
| pizza-party | action | build | manipulate (cutting shares is not assembling parts) | C08 is no longer 2 of 3; it becomes a food-setting load case. Keep the fix but move C08 down the order. |
| pattern-finder | action | sort | experiment (the AI sorts; the class trains it, as in teach-the-robot) | C12: pattern-finder and teach-the-robot now match on all three tags. The secret-keeper hit (sort + robot) disappears, so drop the secret-keeper reshape (see false clashes). |
| two-sides-theater | setting group | stage | folktale (the detail is "Three Little Pigs from the wolf's view"; no stage in the concept) | C07: the stage match with story-dress-up disappears. The same-story repeat with three-pigs-lab still justifies the fix. |
| flowchart-factory | setting group | factory | generic (the factory is only in the title) | C33 is a title clash, not 2 of 3. Retitle instead of reshaping. |
| debate-prep-desk | setting group | council-debate | generic (a prep desk) | C13: debate-prep-desk against town-hall-debate is skill only. The fix still stands, because W.6.1 has no counterclaims. |
| story-problem-theater | setting group | stage | generic (animated stories; "theater" is the title) | C10's secondary hits disappear. No change to the fix. |
| art-passport | setting group | museum | travel-map (14 stops on a world map with passport stamps) | None; C01 already argues this. Fix the tag so the file agrees with the cluster. |
| elevator-hundred | action | simulate-tune | solve | None. |
| asl-story-theater | setting group | stage | generic | None. |

Outside the sample, also noted: clock-shop is tagged shop-food, but its concept has no shop (it is a clock you drag). Retag it generic, which takes K-2 shops from 6 to 5.

Skill tags I could not check as the rule uses them: tags.csv has only the plain-language skill line, never the skill key that method.md says the rule matched on (all 586 skill strings are unique). See presentation, P1.

## 2. Missed clashes

Rerunning action plus setting from tags.csv gives 140 pairs, and 8 of them appear nowhere in clusters.md although C44 says it lists every kept rule hit (P2). The 22 pairs below come from my own read. The first ten I would act on; the rest are smaller.

**Act on these (strong):**

- **M1. computer-builder (live, g1) and input-output-machine (CS, g2).** Skill (what each hardware part does, input to output) and setting (a computer). The live tool already has the keyboard typing onto the screen and the speakers playing. Fix: reshape input-output-machine away from the desktop computer: "Takes In, Gives Out: A tablet, a game controller, a smart speaker and a microwave; the class sorts each part into 'takes in' or 'gives out', then predicts what the gadget does when one input is covered." (action sort; keeps E2-SYS-HW-11)
- **M2. poll-workshop (live, math g11) and design-the-study (math g12).** Both modules carry S-IC.B. Both tags.csv settings are newsroom (a headline, a journal editor), so it is 2 of 3 by the pass's own tags. The live tool already does sampling methods, question wording and bias. Fix: design-the-study leads with experiments only (random assignment, a control group, blinding, placebo) and has no survey or sampling-method controls. Add one line to the concept: "No polls: poll-workshop owns surveys."
- **M3. globe-theatre-stage (ELA g12) and director-s-chair (arts 9-12).** Skill (switching interpretations of a classic scene changes its meaning) and setting (stage). Fix: director-s-chair leads with its other standard, TH:Cn11 theater traditions: "Stage the same short scene as a Greek chorus, Noh, commedia, Elizabethan and modern realist production; compare what each tradition's staging rules make the audience notice."
- **M4. founding-words-explorer (ELA g9) and premise-inspector (ELA g11).** Same texts and the same move, founding documents read alongside later speeches. Fix: premise-inspector: "Lay out the Declaration's argument as premises and a conclusion, then test later responses (Seneca Falls, Douglass's Fifth of July speech, the Gettysburg Address) by which premise each accepts, stretches or rejects." Also cut "how phrases echo in later speeches" from founding-words-explorer, since RI.11-12.9 belongs to premise-inspector.
- **M5. fossil-dig (science g3) and canyon-reader (science g4).** Skill (rock layers and fossils show a past environment) and setting (digging or reading layers). Fix: canyon-reader keeps the layers (4-ESS1-1); fossil-dig drops them: "Fossil Clues: Match each fossil (a fish, a fern, a coral) to the place it lived, then piece together what this desert used to be and which animals could survive the change." (action match; 3-LS4-1, 3-LS4-3 and 3-LS4-4 stay)
- **M6. biased-bot (CS g4) and fruit-sorter-ai (CS g5).** Skill (train a classifier from examples and test it) and action (experiment). It is C12 one band up. Fix: biased-bot keeps skewed data; fruit-sorter-ai leads with features: "Choose which features (color, size, shape, weight) the classifier may use; see which ones separate the fruit and which only add noise, then test on fruit it has never seen."
- **M7. evidence-locker (ELA g4) and inference-interrogation (ELA g5).** Skill (quote the text as proof) and setting (detective). C18 keeps inference-interrogation as the 3-5 detective, so evidence-locker moves: drop the evidence-room picture and lead with W.4.9 writing: "Quote Picker: For each reason in an opinion paragraph, choose the quote that backs it and write the sentence that introduces it; a quote that only repeats the reason fades out."
- **M8. algebra-tile-studio and polynomial-garden (both math g9).** The same rectangle area model in the same grade (factoring and multiplying). C39's fix, "Polynomial Floor Plan", is still an area model. See bad fixes, B8.
- **M9. blend-bakery (ELA g1) and bundle-bakery (math g1).** Near-identical titles in the same grade, both with ovens. C41 missed it, and C09's fix keeps the bakery. See B2.
- **M10. local-changemaker-planner (social studies g12) and community-project-planner (live, SEL 9-12).** Setting (town) and near-identical titles ("... Planner"). Both plan a community project. Fix: local-changemaker-planner leads with civics only (who decides, public comment, testimony, a petition) and no team or resource management. Retitle it "Who Decides?".

**Smaller (moderate; fix in the concept or note for the spec check):**

- **M11. claim-court (ELA g5) and shape-courtroom (math g5):** two mock trials in one grade, which is C14's problem in 3-5. shape-courtroom also repeats shape-family-tree's "is a square a rectangle?" argument (g3). Fix: shape-courtroom: "Property Sieve: Shapes drop through a stack of sieves (four sides, parallel pairs, right angles, equal sides) and stop at the most specific name they earn; the class predicts where a square lands." (5.G.B)
- **M12. ten-frame-factory (math K) and make-ten-machine (math g1, wave 1):** a factory and a conveyor, both sliding counters into tens. ten-frame-factory's concept has no factory in it. Fix: retitle only, to "Ten and Some More".
- **M13. snack-scale and who-wins (both math K):** both are predict-then-reveal on a tipping scale. Fix: snack-scale: "Line up two rows of snacks one to one; the leftovers show which group has more." (K.CC.C, no scale)
- **M14. particle-zoom (science g5) and powers-of-ten-zoom (math g5):** both are zoom-to-the-atom explorers with "Zoom" in the title, in the same grade. Fix: retitle particle-zoom "Too Small to See".
- **M15. stage-blocker and choreography-board (both arts 6-8):** both place performers on a top-down stage. Fix: stage-blocker keeps the floor plan. choreography-board leads with a timeline of movement phrases (counts, levels, dynamics), with formations as a side view.
- **M16. summary-squeeze (ELA g6) and summary-scaffold (ELD 6-8):** the same skill, and titles that differ by one word. Fix: retitle summary-scaffold, for example "Say It Short".
- **M17. sentence-remixer (ELA g6) and sentence-diagram-builder (ELA g7):** both build combined sentences (skill and action). Fix at spec: remixer leads with style and pronouns (L.6.3, L.6.1), and the diagram builder with clause function (L.7.1).
- **M18. skate-park-energy (science g8) and ski-slope-designer (math g8):** both design a slope for a rider in the same grade. Fix: skate-park-energy becomes "Swing Energy" (a pendulum or playground swing, KE and PE in a live bar chart). This also clears the PhET echo in C45.
- **M19. slice-it (math g10), cone-slicer (math g12) and solid-spinner (math g12):** three slice-or-spin-a-solid explorers. Fix: cone-slicer leads with the locus definitions (drag a focus and directrix, keep the sum of distances fixed) instead of slicing.
- **M20. town-planner-disaster-ready (science g4, wave 1) and settle-the-valley (social studies g4):** both build a settlement and watch the land respond, with dams and floods in both. Fix at spec: settle-the-valley leaves hazards and dams out; town-planner owns them.
- **M21. meal-and-move-planner and fitness-program-designer (both health 9-12):** both plan workouts. Fix: meal-and-move leads with nutrition and energy balance; FITT programming stays with fitness-program-designer.
- **M22. song-form-builder and dance-pattern-puzzle (both arts 3-5):** both arrange A and B sections into forms. Note it for the spec check; the two art forms keep them apart.

**Add to C44 (rule hits not mentioned anywhere):** pie-sort and melt-or-not (live; pies are only the reward); the four 9-12 mysteries satire-decoder (spec), health-claim-checker, detective-del-pasado and ph-detective, which match each other on investigate plus detective; misleading-charts and detective-del-pasado; mundo-hispano and scramble-for-africa. Also worth a C44 line: motion-graph-match (live) and speedometer (the speedometer spec must lead with the derivative, not graph matching); model-mechanic and algorithm-audit (both on bias); and silk-road-traders, salt-and-gold-caravan and mongol-messenger (three trade routes spreading ideas in 6-8, which is fine because the region is the content).

## 3. False or weak clashes

- **F1. C41 plot-rollercoaster is grade 6, not grade 5** (data/tools-concepts.csv line 52). There is no coaster in 6-8, so it does not share a band with roller-coaster-rounding (g3). Drop it from C41, or mark the rename optional.
- **F2. C41 theory-gym (9-12) and logic-gym (6-8) are in different bands.** The heading "near-identical titles in the same band" does not apply. Drop them.
- **F3. C33** is a title clash only (see wrong tags). Keep flowchart-factory's concept and retitle it ("Chore Flowcharts" works as a title alone).
- **F4. C12 secret-keeper:** with pattern-finder's action corrected, secret-keeper matches only on the robot setting. Its new owl mail carrier also collides with C03's mail mouse (B3). Drop the reshape.
- **F5. C35 voice-switcher:** the rule hit was explainer-studio against colonial-newsroom, and both are kept. voice-switcher's "who gets the blame in news headlines" is the strongest passive-voice hook in the catalog. Mark the reshape optional.
- **F6. C14 option B ("Fair or Fixed?") is wrong**, not just optional. See B4.
- **F7. C18 is driven by the format.** Every mystery-format tool is tagged detective, so four mysteries in 3-5 became a clash, while the same pattern in 9-12 (four mysteries) went unflagged. Keep the C18 reshapes as title and setting load relief, and record the 9-12 set in C44 so the two bands are treated alike.
- **F8. C08** rests on the wrong action tag. The fix is still reasonable, because there are three food builders in K-2 and two are live, but it is load relief and should drop out of the top of the order.

## 4. Bad or weak fixes

No fix moves a live tool. I checked all 69 tools named for change against tools/: none has a tool.json or a spec folder.

**Fixes that create a new clash:**

- **B1. C15 "Hundred Chart Climb"** (a gecko climbs a hundred chart by rows of ten) is the live hundred-hop: an animal moving on a 1 to 100 chart by tens, with a "Where will it land?" mode. It also keeps "Hundred" in the title. Fix: "Bead Slider: Slide beads on a 100-bead string, ten at a time and one at a time, to solve 34 + 20 or 47 + 6; the class predicts where the count stops before sliding." (1.NBT.C, no animal, no chart)
- **B2. C09 bundle-bakery:** "cookies roll off the oven belt" puts a conveyor next to make-ten-machine (wave 1) and ten-frame-factory, the same tens-packing picture in K-2 math. It also keeps "Bakery" in grade 1 next to blend-bakery (M9). Keeping the tycoon (the open option) leaves a second shop beside the live corner-store. Fix: "Crayon Boxes: Pack the class's loose crayons into boxes of ten for every table; say how many boxes and loose crayons, then compare two classrooms' supplies with >, = and <." (action manipulate, an art supply shelf). Close the open call with this.
- **B3. C03 and C12 together:** "Mouse Mail Route" (g1 CS) and secret-keeper's "owl mail carrier" (K CS) put two animal mail carriers in K-2 CS. Fix: drop the secret-keeper reshape (F4).
- **B4. C14 option B "Fair or Fixed?"** (is the coin or spinner fair? simulate the null) is fair-dice-investigation (g12: is the casino's die loaded?) in the same grade, and sits next to sample-machine (g12). Fix: keep courtroom-statistics as written and close the open call.
- **B5. C05 "Rainy Day Fund" and C32 "Covered"** both "live a year of surprises" (a flat tire and a vet bill; a stolen bike and a fender bender) in CTE 9-12, next to the-credit-card-diaries, which lives four years of choices. Fix: keep Rainy Day Fund, since surprise costs are what an emergency fund is for. Change Covered: "Compare three insurance quotes side by side; a slider trades the monthly premium against the deductible, and a claim calculator shows who pays what for a stolen bike or a fender bender. A last round sorts real insurer messages from fake 'claim refund' texts." (action compare)
- **B6. C25 "Snow Globe Factory"** puts a second "Factory" title into grade 8 math beside function-machine-factory, the exact problem C33 raises. Fix: title "Snow Globe Maker".
- **B7. C26 "Robot Vacuum Routes":** a robot vacuum is round, so flips and turns do not show, and dilating it makes no sense. Fix: keep the routing game with an asymmetric mover, for example an L-shaped delivery cart or an arrow-shaped drone.
- **B8. C39 "Polynomial Floor Plan"** is still a rectangle area model, the same picture as algebra-tile-studio in the same grade (M8). Fix: "Polynomials as Numbers: Set x = 10 and watch every polynomial become an ordinary number; multiplying polynomials turns into long multiplication without carrying, and like terms line up like place-value columns." (A-APR.1, polynomials as a system like the integers)

**Fixes that drift from the module's standards:**

- **B9. C34 blueprint-builder:** the module is RI.4.5, a reading standard (describe a text's overall structure), but the fix ("Pattern Paragraphs") is still a writing task. Its pattern cards also repeat structure-spotter (g3, RI.3.8: sort paragraphs by sequence, cause and effect, comparison). Fix: "Same Facts, New Shape: One set of facts about a hurricane appears as a timeline, a cause-and-effect chain and a problem-and-solution article; students name each structure and say which question each version answers best." This also removes the second new "Pattern P..." title in 3-5 (B12).
- **B10. C36 source-sorter:** W.6.8 itself says "assess the credibility of each source", so the fix drops part of the module. fake-or-fact-lab carries only AASL codes, so no ELA tool would cover it. Fix: keep one quick credibility check per source before the quote-and-paraphrase steps.
- **B11. C38 "Carbon Relay"** puts photosynthesis and respiration hops next to energy-accountant (wave 1, g9: a carbon and energy ledger for photosynthesis and respiration). Fix: either take the C38 alternative now (add HS-LS2-5 to energy-accountant's module before its wave 1 spec), or point Carbon Relay at the spheres (ocean, rock, fossil fuels) and leave the cell-level bookkeeping to energy-accountant. Either way, the move needs a new module row, and science-12-population-and-resources is left with no tool. Say so in C38.

**Title problems in the fixes:**

- **B12.** "Pattern Painter" (C18, g3) and "Pattern Paragraphs" (C34, g4) are two new "Pattern P..." titles in 3-5, next to dance-pattern-puzzle. B9 resolves this.
- **B13.** "Costume Corner" (C41) sits in K-2 beside the live Calm Corner and Corner Store. Fix: "Act It Out".
- **B14.** "Round Up" (C24, a circles tool) reads as rounding in a math catalog. Fix: "Big Wheel, Small Wheel".
- **B15.** Three new "... Desk" titles (Remix Review Desk, Connection Help Desk, Lost and Found Desk) join fact-check-desk and the data-desk family. Optional: "Remix Review" and "Help Desk Heroes" are enough. No trademark issues found in any new title. One low caution not in C45: counterclaim-ping-pong ("Ping-Pong" is a registered mark for table tennis gear; "Counterclaim Rally" avoids it).

**Weaker, note for the spec check:**

- **B16.** C11 "Me vs the Counter" counts colored blocks by color, in the same grade as toy-box-sort (K: sort toys by color and count the piles). Count something else, such as claps, bounces or bells in a song.
- **B17.** C13 "Reason Builder" (keep or bounce facts by relevance) leans toward logic-gym's skill (g7, relevant and sufficient evidence) and argument-x-ray's (g6). Keep the weight on writing the paragraph. Also, C13 says grade 8 "adds formal style", but W.6.1d and W.7.1d already require it. What grade 8 adds is distinguishing the opposing claim.

Checked and fine: the other reshapes keep their module's standards (I checked each module_id in data/modules.csv), and none of the remaining new concept lines clashes with a live or planned tool in its band. The retell trio (story-stage, Bedtime Retell, Story Quilt) is module-required; keep it on the spec check list.

## 5. Gap corrections

Confirmed: 111 of 196 CSTA identifiers have no module (exact match against data/standards/csta-2026-ids.txt). The NGSS list is exact: the only PEs with no module are K-2-ETS1, 3-5-ETS1, MS-PS2-4, MS-LS1-8, MS-LS4-5, HS-PS3-4, HS-LS2-3, HS-LS2-5 and HS-ESS2-7. The SEL, library, health, CTE, world language, arts, SS module and SL counts are all right.

- **G3, SOC:** "Computing and Society in grades K-4" is off at both ends. E1-SOC-HU-15 and E4-SOC-HU-18 are covered, and grade 5 SOC-CE, SOC-HI and SOC-ET are not. "Parts of MS-SOC and HS-SOC" understates it: MS has 1 of 8 covered and HS has 0 of 9. Correct the line, and name data-policy-council's module (9-12 ethics, law and data policy, which carries no SOC code) as the natural home for HS-SOC-ET.
- **G3, candidate:** pattern-finder's module already carries E1-SOC-HU-15. The real K-2 hole is EK and E2 SOC, all uncovered. Candidates: secret-keeper (K) or teach-the-robot (g2).
- **G3, largest holes:** DAT-DC (9 uncovered: E1, E2, E3, E5, part of MS and HS) and PRO-PD (9) are as large as the listed holes and are missing from the list. PRO-RD's hole is mostly K-3 and grade 5; MS and HS each have one of two covered.
- **G4, fluency:** CCSS has RF.x.4 from K to grade 5. RF.K.4, RF.2.4, RF.3.4, RF.4.4 and RF.5.4 are all missing, not only grades 2 and 3.
- **G5, geography:** "No 9-12 geography" is overstated. D2.Geo.5, .7 and .11 appear in five modules for grades 9 to 11 (industrial revolution, imperialism, decolonization, globalization, Gilded Age). Correct it to "no 9-12 geography course".
- **G7, counts:** K-2 showdown is 22 (not 20); 9-12 explorer is 27 (not 25); 6-8 build (17) and builder (15) are as heavy as simulate-tune and go unmentioned. The band totals include K-12 and 6-12 tools, but the rare counts do not; say which.
- **G7, after the fixes:** C27 (curling), C34 (relay) and C35 (play-by-play) each add a sports setting, to bands that already have 5 or 6.
- **G2:** the HS-LS2-5 move needs a new module row and orphans science-12-population-and-resources (see B11). Optional: MS-LS4-5 (artificial selection) sits more naturally with the natural selection module than with gene-pool's heredity module.

## 6. Presentation

clusters.md is scannable. It has fixed fields per cluster, an order by severity, a clear first-look list, and plainly worded open calls. These fixes would make it ready:

- **P1. Make the pass rerunnable.** Add skill_key and setting_group columns to tags.csv, and a pairs.csv of the 150 rule hits with the tags each pair matched. Move the helper scripts from the session scratchpad into the repo. The RUNBOOK spec check for each wave needs to rerun this.
- **P2. C44 is incomplete.** Add the 8 unlisted rule hits (section 2).
- **P3. Add a one-row-per-tool decision table** at the top: tool, cluster, change (reshape, rename, move), new title, wave, and whether Cory's call is needed. Cory decides tools, and that list is currently spread across 42 sections.
- **P4. Update the first-look list.** Add the wave 1 neighbors (make-ten-machine with M12 and B2, town-planner-disaster-ready with M20, energy-accountant with B11), and the three live-tool clashes (M1, M2, M10). C08 can drop out of the top (F8).
- **P5. Close or recommend every open call.** courtroom-statistics: keep (B4). bundle-bakery: the crayon-box reshape (B2). secret-keeper: drop the reshape (F4). retell-puppets, population-dashboard, ph-detective and boundaries-builder are put plainly as they are.
- **P6. Fix the totals.** 49 reshapes, 1 move and 14 renames make 64 changed tools, not 63.
- **P7. Apply the "4 or more settings in a band" flag evenly, or drop it.** These loads have no entry: 3-5 sports 6, animals 6, robot 5, nature 5; 6-8 sports 5, town 5, water 5, stage 4, vehicle 4; 9-12 sports 5, town 5, vehicle 4, nature 4, mysteries 4. Most are fine; one C44 line saying so is enough.
