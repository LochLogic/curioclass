# School Wall Mural

## One idea
Your criteria pick the winner: weight what six neighbors told you into a rubric and watch four painted mural sketches re-rank live as you change whose wishes count, then walk the winner past the real wall (sidewalk, across the street, a passing bus, five summers of sun) to find what your rubric forgot before you defend it at the board meeting.

## Not like
- design-fixer (6-8, puzzle): fixes one broken poster until the eye lands right. Here nothing is broken; four finished sketches are judged against criteria the student builds from other people's wishes.
- brand-builder (9-12, builder): one logo tested on fixed surfaces. Here the test is distance, speed and sun on one large wall, and the criteria come from a community, not a client.
- virtual-gallery (9-12, builder): hangs a show indoors for a visitor. Here one public work faces a street and a board vote.
- frame-it, vanishing-point-studio (6-8): camera and perspective drawing. Nothing is drawn here; the student judges.
- art-through-time (6-8): history of movements. This tool looks at one neighborhood and one wall.
- morning-show-crew (this band): reach and audiences for a message. Here the audience writes the criteria.

## Who and how
- Grade 6-8, visual arts, module "Public Art and Murals (Visual Arts)". Topic line: planning a community mural.
- Driver: students (own laptops; pairs work well). 25 to 40 minutes.
- Standards: NCAS VA:Pr4 (select work for presentation), VA:Pr5 (prepare work for a space), VA:Pr6 (convey meaning through presentation), VA:Re9 (criteria to evaluate work), VA:Cn10 (art and community).
- Header: title, topic line, modes **Listen**, **Judge** (default after the first visit to Listen), **Street test**, **Board**, then kit `motion`, `sound`, `read`. Mode buttons are always live; the tool opens on Listen.

## Screens and modes

### Layout (all modes)
- Stage left (about 68% wide), panel right with `hint`, the mode's controls and **Reset**. Under 1000 px wide the panel goes under the stage, buttons first.
- A thin strip across the top of the stage shows the current winner: its sketch thumbnail and name, always visible, so every change elsewhere shows its effect.

### Listen (explore)
- Focus: the six neighbor places, a 3 by 2 grid of painted cards (no people) filling the stage.
- Each card: the painted place, the neighbor's name and role in code under it. Tap a card: it flips to the neighbor's quote (Content) and the one or two criteria the quote raises, as chips. Each chip has **Add to rubric** (a toggle; on shows a check).
- Panel: the rubric so far (chips added), and **Go to Judge**.
- Responds: a chip added appears in the rubric list at once with weight 2.

### Judge (the core)
- Focus: the four sketches as a ranked row of large thumbnails (each about 22% of the stage width, 4:1 sketches stacked as rows of a leaderboard when the stage is narrow), with a stacked score bar under each: one colored segment per criterion, length = weight times score.
- Panel: the rubric: one row per criterion in the rubric with a weight stepper (0, 1, 2, 3; 0 dims the row) and who asked for it (neighbor name). **Add criterion** opens the list of all seven criteria (ones not yet heard in Listen are shown with "not heard yet" but can still be added). **Equal weights** sets every rubric row to 2.
- Tap a sketch: it opens large (the whole stage) with its per-criterion score and the reason for each score (Content), and **Back to ranking**.
- Responds: on every weight change the bars resize and the row re-sorts over 400 ms (Motion off: at once). When the leader changes, the top strip changes and a small note says "New leader: Sunflower Street. History now counts less."
- Ties: equal totals share a rank, shown "tied", and the top strip says "Tie: pick one with Choose".
- **Choose this one** (on a sketch's large view) sets the student's chosen sketch for Street test and Board (default: the current leader). The chosen sketch carries a pin icon.

### Street test
- Focus: the chosen sketch shown on the painted wall from one viewpoint, filling the stage.
- Viewpoint buttons: **Sidewalk** (3 m), **Across the street** (18 m), **Bus window** (9 m, moving), **Five summers**.
- On each view a readout card (code, over a solid panel on the stage corner): the sketch's smallest key detail, its size on the wall, and how big it looks (in arcminutes, with a plain word: "easy to read", "you can tell something is there", "lost"). Rule in Content.
- Sidewalk and Across the street: the sketch is warped onto the wall's painted surface (CSS perspective to four measured corner points per view) and blurred in code so detail under 5 arcminutes smears out (blur radius from the angle; rule in Content).
- Bus window: tap **Ride past**: the wall slides past the painted bus window in 1.7 s (the time a 12 m wall takes at 25 km per hour), with motion blur. After it passes, three buttons ask what you caught: one per sketch feature (Content, three per sketch), toggle the ones you saw; then the readout says how many focal shapes the sketch has and that a glance holds about three (tool's own guide). **Ride again** replays.
- Five summers: a slider **Summers** 0 to 5. The sketch fades by the pigment model (Content); under it a strip of the sketch's paint swatches, each with its pigment name, its lightfastness rating (I, II or III) and its look after the chosen number of summers.
- **Swap paint** (Five summers only): for a sketch with a III or II pigment, offers the listed lightfast swap; applying it changes the sketch's "lasts outdoors" score to the revised value and the Judge ranking updates.
- **Enlarge detail** (Sidewalk and Across views, sketch A only): the revision named in Content ("Enlarge detail"): A's Readable goes from 1 to 2 and its History from 4 to 3; the ranking updates.

### Board
- Focus: the painted meeting room with three blank nameplates (names in code) and the chosen sketch on an easel in the middle.
- The board asks three questions, one at a time, chosen from the chosen sketch's two lowest-scoring criteria in its revised state plus always "Why this one over the others?" (Content). Each question shows two or three answer cards. Each card names its evidence ("Street test: across the street, 86 arcminutes"). Cards whose evidence the student has not actually seen (that view never opened, that criterion not in the rubric) are shown locked with "Run the Across the street test first" and can't be picked.
- After three answers: the board's reply (Content), which says which answers had evidence and what the board still worries about. No vote count, no score. **Back to Judge** and **Present again** (restart Board).

## Content

### Neighbors (made up for Curio Class)
1. Rosa Delgado, owns Sol Flowers across the street. Quote: "People should smile when they walk by. This corner has been gray for twenty years." Criteria: Bright and welcoming.
2. Ken Ito, rides the 14 bus every morning. Quote: "I see that wall for two seconds from the bus. Make it something I can get in two seconds." Criteria: Readable from the street.
3. Mrs. Odette Banks, Willow Street Senior Center. Quote: "This street had a streetcar and a button factory. Kids should know where they live." Criteria: Our history.
4. Tomas Reyes, volunteers at the Third Street community garden. Quote: "We have birds, bees and a lot of concrete. Bring some green." Criteria: Nature and calm.
5. Jada Price, skate park regular, 8th grade. Quote: "If students don't help paint it, it isn't ours. Leave a part for us." Criteria: Students help make it.
6. Mr. Lee Harmon, school custodian. Quote: "Sun hits that wall all afternoon. Cheap paint is gone in three summers, and every color costs a day of scaffolding." Criteria: Lasts outdoors, Cost and time.

### Criteria (7) and the sketches' scores (1 to 4)
| Criterion | A River Timeline | B Sunflower Street | C Quilt Blocks | D Open Book |
|---|---|---|---|---|
| Our history | 4 | 1 | 3 | 2 |
| Readable from the street | 1 | 4 | 3 | 3 |
| Bright and welcoming | 2 | 4 | 3 | 2 |
| Lasts outdoors | 3 | 2 | 1 | 4 |
| Students help make it | 2 | 2 | 3 | 4 |
| Nature and calm | 2 | 4 | 1 | 2 |
| Cost and time | 1 | 3 | 4 | 2 |

Reasons (shown in the large view, one line each):
- A River Timeline: muted earth tones and dozens of small scenes along a river: the streetcar, the button factory, the old bridge. History 4 (names three real local landmarks); Readable 1 (smallest key detail, the factory windows, is 6 cm); Bright 2 (earth tones); Lasts 3 (earth pigments rate I, one II blue); Students 2 (painted by a hired artist, students fill the sky); Nature 2; Cost 1 (14 colors, 12 painting days).
- B Sunflower Street: five giant sunflowers and three swallows in flat bold shapes on sky blue. History 1; Readable 4 (smallest key detail, a swallow's eye, 40 cm); Bright 4; Lasts 2 (its yellow is a II pigment, its red a II); Students 2; Nature 4; Cost 3 (5 colors, 5 days).
- C Quilt Blocks: a grid of quilt squares based on patterns from the senior center's quilting circle, in hot pink, orange and teal. History 3; Readable 3 (smallest key detail, one quilt square's inner triangle, 25 cm); Bright 3; Lasts 1 (fluorescent pink and an alizarin crimson, both III); Students 3 (each class paints one block); Nature 1; Cost 4 (6 colors, 4 days, simple stencils).
- D Open Book: an open book whose pages turn into the street, birds and the river, with a banner carrying a line students choose (letters in code). History 2; Readable 3 (smallest key detail, banner letters 45 cm tall); Bright 2 (soft blues); Lasts 4 (all I pigments plus a clear UV-blocking topcoat); Students 4 (students write the banner line and paint the pages); Nature 2; Cost 2 (9 colors, 9 days).
- Score = sum over rubric rows of weight times score. Checked: every one of the four sketches wins under some weighting (see Sources), and with equal weights on all seven B leads (20), then D (19), C (18), A (15).

### Street test rules
- Visual angle of the smallest key detail: angle = 2 atan(size / 2 / distance), in arcminutes. Sidewalk 3 m, bus 9 m, across 18 m.
- Words: 15 arcminutes or more "easy to read"; 5 to under 15 "you can tell something is there"; under 5 "lost". The 5 arcminute line is the height of a letter a person with 20/20 vision can just read (Snellen); 15 (three times that) is the tool's own guide for reading at a glance, said on screen as a rule of thumb.
- Values (checked): A 6 cm: 68.8, 22.9, 11.5 arcminutes (sidewalk, bus, across). B 40 cm: 457.7, 152.8, 76.4. C 25 cm: 286.3, 95.5, 47.7. D 45 cm: 514.7, 171.9, 85.9.
- Blur in code: blur radius in pixels = max(0, (15 minus angle) / 15) times 6 px at 1366 wide, scaled with the stage, applied only to the sketch layer.
- Bus: 12 m wall at 25 km per hour = 1.73 s in view. Focal shapes per sketch: A 9 (too many for a glance), B 3, C 1 (one grid), D 2. The three "what did you catch" features per sketch: A streetcar / button factory / bridge; B sunflowers / swallows / blue sky; C pink squares / teal triangles / a quilt grid; D an open book / birds / the banner words.
- Enlarge detail (A only): redraw the factory as one large shape with 30 cm windows: A's Readable becomes 2 (smallest key detail now 30 cm: 57.3 arcminutes across the street) and Cost and time stays 1 (the tool notes "fewer small scenes, same days"), History drops to 3 (the bridge is cut to make room).

### Pigments and fading (five summers)
- Lightfastness ratings follow the ASTM scale for artists' paints: I excellent, II very good, III not lightfast enough for lasting work.
- Sketch pigments: A: yellow ochre PY43 (I), burnt sienna PBr7 (I), ultramarine blue PB29 (I), a Prussian blue PB27 (II), carbon black PBk7 (I), titanium white PW6 (I). B: Hansa yellow PY3 (II), naphthol red PR112 (II), phthalo blue PB15 (I), phthalo green PG7 (I), titanium white (I). C: fluorescent pink (III), alizarin crimson PR83 (III), pyrrole orange PO73 (I), phthalo green-blue (I), carbon black (I). D: ultramarine (I), phthalo blue (I), titanium white (I), carbon black (I), yellow ochre (I).
- Fade model (the tool's own picture, labeled "a simple model, not a lab test"): each summer a pigment loses this share of its remaining color strength: I 1%, II 4%, III 15%. After five summers: I 4.9%, II 18.5%, III 55.6% lost. Shown by mixing that swatch toward the wall's primer gray; the sketch layer's saturation drops by the mean loss of its pigments weighted equally.
- Swaps: PR83 to quinacridone red PR209 (I); fluorescent pink to quinacridone magenta PR122 (I); PY3 to arylide yellow PY74 in a lightfast grade, shown as II remaining "better, but check the brand"; PR112 to pyrrole red PR254 (I). After C's two swaps its Lasts becomes 3 and its Bright stays 3 (the label says "a little less glow"); after B's two swaps its Lasts becomes 3.

### Board questions (the two lowest criteria of the chosen sketch, plus "why this one")
- Our history: "What does this have to do with Willow Street?" Cards: "Mrs. Banks asked for history; our score is X" (needs History in the rubric); "Students will add a timeline panel" (only D and C).
- Readable: "Can drivers and riders even tell what it is?" Cards: "Across the street the smallest detail is N arcminutes" (needs Across opened); "Ken Ito rides by; on the bus test I caught K of 3 features" (needs Bus run).
- Bright: "Isn't it a bit dull?" Cards: "Rosa asked for welcome; we weighted it W" (needs Bright in rubric).
- Lasts: "Will it look like this in five years?" Cards: "With the swap, every pigment is I or II" (needs Swap paint applied); "Five summers test: up to P% color lost" (needs Five summers opened).
- Students: "Who actually paints it?" Cards: a sketch's student plan line from its reasons.
- Nature: "Where's the green Tomas asked for?" Cards: rubric weight and score.
- Cost: "Can we afford N painting days?" Cards: "N days, C colors, against the others' days" (always available).
- Why this one: "Why this over the other three?" Cards: "It led under our rubric by X points" (needs it to be the leader); "It wasn't the leader, but it passed the street test the leader failed" (needs a street test where the chosen sketch beat the leader).
- Board reply: "You answered N of 3 with evidence from your tests." plus one line per unanswered or weak spot: "We still worry about cost." No approve or reject.

## Interactions in detail
- Every control acts at once; Judge re-sorts on each weight step. Rubric with every weight 0: bars empty, all four "tied", hint "Give at least one criterion a weight."
- Street test opened before Judge: uses the current leader (B with equal weights).
- Swap paint and Enlarge detail are revisions: listed in a "Changes" box in the panel with **Undo** each. Undo restores the scores everywhere.
- Ride past during Motion off: the wall cuts in, holds 1.7 s, cuts out (timing kept).
- Saved on this device: rubric, weights, chosen sketch, revisions (localStorage, try/catch). **Reset** clears them and returns to Listen.
- Sizes: at 1366x768 the ranked sketches and the weight steppers are both visible without scrolling. In the 680x425 preview the ranked row and top strip show with scene text at least 10 px. At 375 wide, ranking stacks as a list, rubric under it.

## Look
- Accent (`--brand`) #1f5fa8 cobalt (primer-can blue). Paper #f3f1ec (sidewalk concrete), panel #ffffff, ink #1e2328, muted #5a6068. Criterion segment colors (each with its name on the bar on hover and in the legend): history #8a5a2b, readable #1f5fa8, bright #c9861a, lasts #4a6b3a, students #8c3f8f, nature #2f8a5a, cost #5a6068.
- Contrast: ink on paper 14.03:1, on panel 15.83:1; muted 5.62:1 and 6.35:1; brand on paper 5.71:1, white text on brand 6.44:1.
- Different from design-fixer (indigo), brand-builder (studio green), virtual-gallery (lime), frame-it (amber), stage-blocker (spike orange), and from the other 6-8 arts specs in this batch.

## Art
Local FLUX, no people. One style: "soft gouache illustration, warm afternoon light, city neighborhood".
- place-flower-shop: "a small corner flower shop storefront with a striped awning, buckets of bright flowers on the sidewalk, a blank wooden sign board above the door, soft gouache illustration, warm afternoon light"; 4:3; no cutout; people no; Listen card 1.
- place-bus-stop: "a city bus stop shelter with a bench and a blank route sign on a pole, an empty street behind, soft gouache illustration"; 4:3; card 2.
- place-senior-porch: "the porch of an old brick community building with two rocking chairs, potted geraniums and blank framed pictures on the wall, soft gouache illustration"; 4:3; card 3.
- place-garden-gate: "a community garden gate in a chain fence with raised vegetable beds, sunflowers and a bee hive box, soft gouache illustration"; 4:3; card 4.
- place-skate-ramp: "a concrete skate park with a quarter pipe ramp, a skateboard resting on the ledge, chalk marks on the ground, soft gouache illustration"; 4:3; card 5.
- place-custodian-bench: "a school custodian's workbench with paint cans, rollers, brushes, a folded ladder and a dusty window, soft gouache illustration"; 4:3; card 6.
- sketch-a-river-timeline: "a long mural design in muted earth tones: a river running left to right with an old streetcar, a brick button factory with many small windows and an arched stone bridge, painted on paper"; 4:1; sketch A.
- sketch-b-sunflowers: "a long mural design: five giant sunflowers and three swallows in flat bold shapes on a sky blue ground, painted on paper"; 4:1; sketch B.
- sketch-c-quilt: "a long mural design: a grid of geometric quilt squares with triangles and stars in hot pink, orange, teal and black, painted on paper"; 4:1; sketch C.
- sketch-d-open-book: "a long mural design in soft blues: a giant open book whose pages curl into a street, birds and a river, with a long blank ribbon banner across the top, painted on paper"; 4:1; sketch D (banner words in code).
- wall-sidewalk: "a long blank pale stucco school wall seen at an angle from the sidewalk, a tree and a fire hydrant at the edge, soft gouache illustration, warm afternoon light"; 16:9; Street test Sidewalk (sketch warped onto the blank wall).
- wall-across: "a long blank pale stucco school wall seen straight on from across a two-lane street, parked bicycles and a crosswalk, soft gouache illustration"; 16:9; Across the street and Five summers.
- bus-window: "the inside of a city bus looking out a wide side window, a seat back and a grab pole in the foreground, the window empty pale sky, soft gouache illustration"; 16:9; Bus window (the wall slides behind the glass, clipped to the window shape in code).
- board-room: "a school board meeting room with a long wooden table, three blank name plates, microphones and an empty easel in the center, soft gouache illustration"; 16:9; Board.
- 14 images, none with people. Drawn in code: score bars, rubric, readouts, swatches, banner letters, top strip, nameplate names.

## Voice
Bank voice: `clear-teacher` (the art teacher running the mural project; no neighbor or other spec in this band uses it). Style from the bank. `Curio.voice` with `scope: () => state.mode`.
- welcomeListen (how; entering Listen; stale when a card is tapped): "Six neighbors live with this wall. Tap a card to hear what each one wants."
- addHow (how; first card flipped; stale when a chip is added): "Tap Add to rubric to keep what matters to you."
- welcomeJudge (how; entering Judge; stale when a weight changes): "Set a weight for each criterion with the steppers. Watch the sketches change places."
- newLeader (event; leader changes; stale when another weight changes): "New leader." (the name and reason are on screen)
- zeroHow (how; all weights 0): "Give at least one criterion a weight."
- welcomeStreet (how; entering Street test; stale when a view is tapped): "Now test your pick on the real wall. Tap a view."
- busHow (how; Bus window opened; stale when Ride past is tapped): "Tap Ride past. You get under two seconds, just like the bus."
- busAsk (event; after each ride; stale when a feature is toggled): "Tap what you caught."
- summersHow (how; Five summers opened; stale when the slider moves): "Drag Summers to see five years of sun."
- welcomeBoard (how; entering Board; stale when a card is picked): "The board has three questions. Pick the answer you can back up."
- lockedHow (how; first tap on a locked card): "That answer needs a test you haven't run. Try a Street test view first."
- boardDone (event; after three answers): "The board has its reply. Read it and decide what to change."

## Family engine
none

## Sources
- National Core Arts Standards, Visual Arts VA:Pr4, Pr5, Pr6, Re9, Cn10: https://www.nationalartsstandards.org/
- Snellen letters subtend 5 minutes of arc at the 20/20 line: American Academy of Ophthalmology, "Visual Acuity", EyeWiki, https://eyewiki.aao.org/Visual_Acuity
- ASTM lightfastness categories I to III for artists' paints: ASTM D4303 (test methods) and D5098 (acrylic emulsion artists' paints), https://www.astm.org/d5098-18.html
- Pigment ratings and swaps (PR83 alizarin poor, PR209, PR122, PR254, PB15, PB29, PY43 excellent): Bruce MacEvoy, Handprint, "Guide to watercolor pigments", https://www.handprint.com/HP/WCL/waterfs.html ; Golden Artist Colors lightfastness ratings, https://www.goldenpaints.com/ . The builder checks each rating against these before shipping.
- Neighbors, sketches, scores, fade percentages and the 15 arcminute guide: written for Curio Class (tool's own model, labeled on screen).
- Checks run (Python, 2026-10-29): all 16,383 non-zero weightings of the 7 criteria (weights 0 to 3): B wins 7,753, D 4,245, C 2,210, A 328, ties 1,847, so every sketch can win (A with History alone, B with Nature alone, C with Cost alone, D with Students alone). Equal weights: B 20, D 19, C 18, A 15. Visual angles as listed in Content. Bus 12 m at 25 km per hour = 1.728 s. Fade compounding: I 1, 2, 3, 3.9, 4.9%; II 4, 7.8, 11.5, 15.1, 18.5%; III 15, 27.8, 38.6, 47.8, 55.6%. A's enlarged 30 cm detail across the street: 57.3 arcminutes. Contrast ratios recomputed with the WCAG 2.1 formula.

## Done when
1. Focus: in Judge at 1366x768 and 680x425 the ranked sketches with their score bars are the largest, central thing, and the top strip shows the leader.
2. Setting only History to 3 (others 0) puts A first; only Nature puts B first; only Cost puts C first; only Students puts D first; all weights 0 shows all four tied.
3. Every weight step re-sorts at once (within the 400 ms slide; instantly with Motion off) and the top strip updates on the same step.
4. Street test readouts match the Content values for each sketch and view, and the words follow the 5 and 15 arcminute lines.
5. Ride past lasts 1.7 s with Motion on and off; tapping a view button or mode button mid-ride stops it and switches at once.
6. Five summers at 5 shows III swatches at about 56% loss; Swap paint updates the Lasts score and the Judge ranking; Undo restores both.
7. Board locks answer cards whose test was not run and unlocks them once it is; the reply counts answers with evidence correctly.
8. How lines speak once in five repeated actions (weight steps, rides); newLeader and boardDone speak every time they happen and are dropped when stale.
9. Reset clears saved rubric, choice and revisions; reload restores them before Reset.
