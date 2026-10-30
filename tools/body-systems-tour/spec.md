# Body Systems Tour

## One idea
Ride along with one traveler (a breath of air, a bite of apple or a message from the brain) as each body system hands it to the next, then switch the body from resting to running, eating or sleeping and watch every system change pace together.

## Not like
- fitness-circuit (3-5 PE, race): feels the heart from the outside with a pulse count during real exercise. Body Systems Tour shows the inside of a drawn body, nobody exercises, and there is no class data.
- germ-spread-sim (3-5 health, simulator): germs spreading through a classroom. Here nothing spreads; one traveler moves through one body.
- label-detective (3-5 health, mystery): what is on a food label. Here food is followed after the first bite, with no nutrients or numbers on labels.
- growing-up-q-a (3-5 health, explorer, same group): how a body changes over years. Body Systems Tour is how it works minute to minute; no growth, no puberty.
- habit-hero (K-2 health, creature): habit meters on a hero. No meters for good or bad choices here; every activity is normal body work.

## Who and how
- Grade 3-5 (best in 4 and 5), Health, module The Human Body Systems (how body systems keep us healthy).
- Driver: either. Students on laptops alone or in pairs, or a teacher on a projector reading stops aloud.
- Minutes: 10-25 (one ride is about 2 minutes).
- Standards: NHES.S1 (comprehends concepts related to health promotion: how body systems work).
- Topic line: "how body systems work together".
- Modes (tool.json): ["Ride along", "Body at work", "Systems"].

## Screens and modes
Header: title "Body Systems Tour" with small line "How body systems work together", mode buttons **🚃 Ride along**, **⚙ Body at work**, **🔎 Systems** (keys 1 to 3), **Motion**, **Sound**, **Read**. Stage left (the body), panel right (stacks below at 760 px wide, with the stage first and the traveler buttons pinned to the top of the panel).

The body (all modes): a front-view outline drawn in code on a dark "inside" stage: a soft glowing rounded silhouette with no face, no hair and no body details (a plain oval head, arms slightly out), sized to fill the stage height. It is the diagram frame: the nerves, spinal cord, arteries (red), veins (blue), esophagus and every traveler path are code lines drawn inside it. The organs, bones and muscles are painted cutouts (Art) laid inside the outline in six system layers (Content, "Systems and parts"). Layers not in use are faint (25 percent opacity); layers in use are full color with a soft rim glow in the system's color.

### Ride along (opens first)
- Focus: the traveler and the part it is in. The body fills the stage (the biggest thing on screen); the current stop's part is lit, and the stop card sits beside it in the panel.
- Panel, top: three traveler buttons, each with icon and name: **🌬 Breath of air**, **🍎 Bite of apple**, **⚡ Brain message**. Breath of air is picked on open, so Ride and Next stop are live at once. Under them: **▶ Ride** (auto: the next stop comes 4 s after the current stop's line ends, or 4 s after it shows with Sound off; becomes **⏸ Pause**), **Next stop ▶**, **◀ Back**, **↺ Start over**. A full ride runs about 60 to 90 s; that is longer than 30 s on purpose, because every stop is a reading moment, and Pause, Next stop, Back and the traveler buttons stay live the whole time.
- Stage: the traveler is a painted cutout (a puff of air, a bite of apple, a spark) with a soft glow, on a dotted path through the layers. The path for the chosen traveler is drawn faintly from start to end so you can see where it will go.
- Stop card (panel, middle): stop number "Stop 3 of 9", the part name, its system tag (icon and color and name), and one or two sentences (Content).
- Handoff ribbon: when the next stop is in a different system, a ribbon slides across the stage between the two parts: "Lungs hand oxygen to the blood." The new layer brightens and the old one stays on, so by the end every system the traveler used is lit.
- End of ride: a "Team" card lists the systems the traveler used, in order, as icon chips ("Lungs → Heart and blood → Muscles"), with **Ride another** (shows the three traveler buttons again).

### Body at work
- Focus: the whole body changing pace. The body stays the biggest thing on the stage; the gauges in the panel echo it.
- Panel, top: four activity buttons, each a small painted picture with its icon and word (Art): **🪑 Resting**, **🏃 Running**, **🥪 Eating lunch**, **😴 Sleeping**. Resting is picked on open.
- Stage: all six layers on. Each system animates at the activity's pace: the heart cutout pulses (scales) at the example beat, the lungs cutout swells at the example breath rate while the diaphragm cutout moves down and up, food dots move through the gut while eating, small sparks run down the nerves, the leg muscle cutouts tighten (scale) and relax while running, sweat drops (code) appear on the outline while running. A tap on another activity changes the paces at once (eased over 1 s), never at the next beat.
- Panel, middle: six gauge rows, one per system, each with icon, name and a three-step word gauge (**Slow**, **Medium**, **Fast** or **Resting**, **Busy**, **Very busy**), plus a number where the Content gives one (heart, breathing). Under the heart row: "At this example beat a heart beats about 122,400 times a day" (computed: beats per minute times 1,440).
- Panel, bottom: the activity's **Team play** card (three sentences, Content).
- **Team check** (optional, a small button): "Tap every system that works harder when you run." The student taps layers on the body or gauge rows; **Check** (live from the start; a system left untapped counts as "not picked") marks each ✓ or ✗ with a one-line reason. No score, nothing kept.

### Systems
- Focus: the part you tapped and its fact card, which opens beside it on the stage.
- Panel: six layer toggles with icon, color swatch and name (all on at start), **Show all**, **Hide all**.
- Stage: tap or click any labeled part (or Tab to it and press Enter) to open its fact card beside it: part name, system, one or two sentences. Labels show on hover and focus; **Labels on / off** toggles them all.

## Content

### Systems and parts (color, icon, parts on the figure)
| System | Color | Icon | Parts (labels) |
|---|---|---|---|
| Brain and nerves | #ffd166 | ⚡ | brain, spinal cord, nerves (arms and legs) |
| Heart and blood | #ff6b6b | ❤ | heart, arteries (red), veins (blue), blood |
| Lungs and breathing | #7cc6ff | 🌬 | nose and mouth, windpipe, bronchial tubes, lungs, air sacs (inset circle), diaphragm |
| Digestion | #8ee07a | 🍎 | mouth, esophagus, stomach, liver, small intestine, large intestine |
| Muscles | #ff9ecb | 💪 | upper arm muscles, thigh muscles, calf muscles, heart muscle (note) |
| Bones | #f4ecff | 🦴 | skull, spine, ribs, arm bones, leg bones, knee joint |

### Part fact cards (Systems mode)
- Brain: Your brain is the control center. It sends and receives messages all the time, even while you sleep.
- Spinal cord: A thick bundle of nerves inside your spine. Messages travel along it between your brain and body.
- Nerves: Nerves carry messages, like "move" or "that's hot," between your brain and every part of you.
- Heart: Your heart is a muscle about the size of your fist. It pumps blood all around your body.
- Arteries and veins: Arteries carry blood away from the heart. Veins carry blood back to it.
- Blood: Blood carries oxygen and food energy to every part of you and carries waste away.
- Nose and mouth: Air comes in here. Your nose warms the air and helps clean it.
- Windpipe and bronchial tubes: Air travels down the windpipe, which splits into tubes that go into each lung.
- Air sacs: Tiny air sacs at the ends of the tubes. Oxygen moves from them into your blood, and carbon dioxide moves out.
- Diaphragm: A dome-shaped muscle under your lungs. When it tightens and moves down, air rushes in.
- Mouth (digestion): Teeth break food into small pieces and saliva starts to break it down.
- Esophagus: A muscular tube. Its muscles squeeze food down to your stomach.
- Stomach: Your stomach mixes food with digestive juices and churns it into a thick liquid.
- Liver: Your liver makes bile, a juice that helps digest fats.
- Small intestine: Most nutrients from food pass through its walls into your blood here.
- Large intestine: It soaks up water and turns what is left into waste that leaves your body when you use the bathroom.
- Muscles: Your body has hundreds of muscles. Muscles that move you pull on bones.
- Heart muscle (note): Heart muscle is a special kind of muscle that never stops working.
- Skull: Your skull protects your brain.
- Ribs: Your ribs make a cage that protects your heart and lungs.
- Spine: Your spine holds you up and protects your spinal cord.
- Arm and leg bones, knee joint: Bones give your body its shape. Joints like the knee let bones bend and move. Adults have 206 bones.

### Rides (stop, system, text; a handoff ribbon before each system change)
**🌬 Breath of air** (9 stops): 1 Nose (Lungs): "You breathe in. Your nose warms the air and helps clean it." 2 Windpipe (Lungs): "The air rushes down your windpipe." 3 Bronchial tubes (Lungs): "The windpipe splits into tubes, one for each lung." 4 Air sacs (Lungs): "Oxygen slips out of the tiny air sacs into your blood." Ribbon: "Lungs hand oxygen to the blood." 5 Heart, left side (Heart and blood): "Blood full of oxygen comes to your heart. The left side pumps it out to the body." 6 Arteries (Heart and blood): "Arteries carry the blood down to your legs." Ribbon: "Blood hands oxygen to the muscles." 7 Thigh muscle (Muscles): "Your muscles use oxygen to turn food into energy. Carbon dioxide is left over." Ribbon: "Muscles hand carbon dioxide back to the blood." 8 Veins and heart, right side (Heart and blood): "Veins bring the blood back. The right side of your heart pumps it to your lungs." Ribbon: "Blood hands carbon dioxide to the lungs." 9 Lungs (Lungs): "You breathe out the carbon dioxide. Then the next breath comes in."
**🍎 Bite of apple** (7 stops): 1 Mouth (Digestion): "Teeth crunch the apple into small pieces. Saliva starts to break it down." 2 Esophagus (Digestion): "Muscles in your esophagus squeeze the bite down." 3 Stomach (Digestion): "Your stomach churns the bite with digestive juices." 4 Small intestine (Digestion): "Sugar and other nutrients from the apple pass into your blood." Ribbon: "Digestion hands food energy to the blood." 5 Blood (Heart and blood): "Your blood carries the sugar all over your body." Ribbon: "Blood hands energy to the brain and muscles." 6 Brain and leg muscles (two tags: Brain and nerves, Muscles; both layers light): "Your brain uses the energy to think, and your muscles use it to move." Ribbon: "Meanwhile, back in digestion..." 7 Large intestine (Digestion): "The apple's fiber is not digested. It moves on, water is soaked up, and the rest leaves as waste."
**⚡ Brain message** ("Kick the ball!", 7 stops): 1 Eyes and brain (Brain and nerves): "Your eyes see the ball. Your brain decides: kick it!" 2 Spinal cord (Brain and nerves): "The message zips down your spinal cord." 3 Leg nerve (Brain and nerves): "A nerve carries the message to your leg." Ribbon: "Nerves hand the message to the muscles." 4 Thigh muscles (Muscles): "Thigh muscles tighten and pull." Ribbon: "Muscles pull on the bones." 5 Knee joint (Bones): "The pull swings your lower leg at the knee." 6 Foot (Bones): "Your foot meets the ball. Kick!" Ribbon: "Meanwhile, your muscles ask for more oxygen." 7 Heart (Heart and blood): "Moving more means your muscles need more oxygen, so your heart starts to beat faster."

### Activities (Body at work)
Heart and breathing numbers are labeled "Example for a 10-year-old" with the range under them; the pulse and breath animation speeds are the tool's own example values inside those ranges.
| Activity | Heart (example, range) | Breathing | Brain | Digestion | Muscles | Bones | Sweat |
|---|---|---|---|---|---|---|---|
| Resting | Medium, 85 a minute (ages 7 to 9: 70 to 110; 10 and up: 60 to 100) | Medium, 20 a minute (ages 6 to 12: 18 to 30) | Busy | Resting | Resting | Resting | none |
| Running | Fast, 170 a minute (working hard at age 10: about 162 to 195) | Fast and deep (no number) | Very busy | Resting | Very busy | Busy | yes |
| Eating lunch | Medium, 85 | Medium, 20 | Busy | Very busy | Resting | Resting | none |
| Sleeping | Slow, 70 (slower than awake; example) | Slow (no number) | Busy (sorting memories) | Resting | Resting | Resting | none |
Team play cards:
- Resting: "Even sitting still, your heart beats and you breathe without thinking about it. Your brain keeps them going. Your bones hold you up."
- Running: "Your brain sends messages to your leg muscles. Working muscles need more oxygen, so you breathe faster and deeper and your heart pumps faster. Sweat on your skin helps cool you down."
- Eating lunch: "Your digestive system breaks lunch into nutrients. They pass into your blood in the small intestine, and your heart pumps them to every part of you."
- Sleeping: "Your heart and breathing slow down. Your brain sorts what you learned today, and deep sleep helps your body grow and repair. Kids 6 to 12 need 9 to 12 hours of sleep a night."
Team check answers (Running): Brain and nerves ✓, Heart and blood ✓, Lungs ✓, Muscles ✓, Bones ✓ ("Bones carry the load and joints move"), Digestion ✗ ("Digestion is not the one speeding up to help you run").

## Interactions in detail
- Picking a traveler resets the ride to stop 1 and dims all layers except the first stop's system. **Back** at stop 1 and **Next stop** at the last stop are disabled. **▶ Ride** stops at the end and shows the Team card.
- Changing traveler mid-ride asks nothing: it simply starts the new ride (hush the voice first).
- The traveler token glides between stops in 1.2 s along the path (instant with Motion off; the stop card still changes at the same moment).
- A tap while Ride plays acts at once: Next stop, Back or a stop change mid-glide snaps the token to the new stop, stops the old line and shows the new card; Pause holds the token where it is; Ride keeps going from the new stop. No stale stop or ribbon line plays after the student has moved on.
- Body at work: switching activity eases the animation rates over 1 s. With Motion off nothing pulses; the gauges and numbers still change and each system shows a static "working" glow in its own color.
- Tapping a system's layer in Body at work highlights its gauge row, and the reverse.
- Systems: hiding a layer also hides its labels; tab order is the panel toggles first, then the parts of visible layers, top to bottom.
- Sizes: at 1366x768 the whole figure, the traveler buttons, the stop card and Next stop are visible together. In the 680x425 preview the figure fits the stage height and labels are at least 10 px; the stop card shows the part name and first sentence. Under 900 px tall the panel puts Next stop and Ride above the stop card.
- Nothing is saved; no localStorage except the kit's Motion setting.

## Look
- Accent `--brand` #c2410c (burnt orange: the tour car and the traveler's glow), on its own light `:root`: paper #fff8f2, ink #2a1d16, muted #6b5a50, line #f1dccd, focus #2f5bd3, panel #ffffff. The stage is a deep "inside" night #1a1530 with the accent light #ff9a5c for the traveler and path.
- Contrast: accent on white 5.18:1, on paper 4.92:1; white text on accent 5.18:1; ink on paper 15.52:1; muted on paper 6.23:1; #ff9a5c on stage 8.4:1; label text #f4ecff on stage 15.32:1. System colors on the stage run 6.34:1 (#ff6b6b) to 15.32:1 (shapes and rim glows), and every system also has its icon and name.
- Paintings: one soft watercolor children's science book style for every image, warm and friendly, nothing gory. The organs keep their natural colors; each layer's rim glow carries its system color.
- Group siblings: growing-up-q-a mauve, first-aid-responder mint, meal-and-move-planner sky blue, health-claim-checker yellow. 3-5 health neighbors: label-detective and germ-spread-sim teal, fitness-circuit raspberry, playbook green; none uses orange.

## Art
Local FLUX (`scripts/localart.py`), one session, one style: every prompt ends "soft watercolor children's science book illustration, clean edges" and every cutout adds "plain white background". 22 images, none with people.

Body parts (cutouts, front view, laid inside the code outline). Sizing rule: each part sits at a fixed spot in the outline's own coordinates (fractions of the figure height and width, set once by the builder) and scales with the figure; arm and leg pieces are painted once and mirrored for the other side.
- bst-brain: "A human brain seen from the front, soft pink folds"; 1:1; cutout yes; people no; Brain and nerves layer, in the head.
- bst-heart: "A human heart, front view, red and dark red, with the big blood vessels at the top"; 1:1; cutout yes; people no; Heart and blood layer, pulses (scales) at the example beat.
- bst-lungs: "A pair of pink human lungs with the windpipe and branching bronchial tubes, front view"; 1:1; cutout yes; people no; Lungs layer, swells with each breath.
- bst-air-sacs: "A tiny bunch of round air sacs like a cluster of grapes, wrapped in thin red blood vessels"; 1:1; cutout yes; people no; the air sacs inset circle.
- bst-diaphragm: "A thin dome of pink muscle shaped like an upside-down bowl"; 4:1; cutout yes; people no; under the lungs, moves down on each breath in.
- bst-stomach: "A human stomach, a curved pink pouch, front view"; 1:1; cutout yes; people no; Digestion layer.
- bst-liver: "A human liver, a smooth reddish-brown wedge shape, front view"; 4:3; cutout yes; people no; Digestion layer.
- bst-small-intestine: "A coiled pink small intestine in neat loops"; 1:1; cutout yes; people no; Digestion layer.
- bst-large-intestine: "A large intestine shaped like a wide upside-down U frame, soft pinkish tan"; 1:1; cutout yes; people no; Digestion layer, framing the small intestine.
- bst-skull: "A smooth cream-colored human skull, front view, gentle and rounded"; 1:1; cutout yes; people no; Bones layer.
- bst-ribcage-spine: "A cream-colored human rib cage with the spine running down the middle, front view"; 3:4; cutout yes; people no; Bones layer.
- bst-arm-bones: "The cream-colored bones of one upper arm and forearm, ending at the wrist, vertical"; 9:16; cutout yes; people no; Bones layer, both arms.
- bst-leg-bones: "The cream-colored bones of one leg: thigh bone, kneecap, the two shin bones and the foot bones, vertical"; 9:16; cutout yes; people no; Bones layer, both legs; the knee joint and foot are hotspots on it.
- bst-arm-muscle: "One upper arm muscle, a rounded red-pink muscle with fine fibers, vertical"; 9:16; cutout yes; people no; Muscles layer, both arms.
- bst-leg-muscles: "The red-pink thigh and calf muscles of one leg with fine fibers, vertical"; 9:16; cutout yes; people no; Muscles layer, both legs; tightens (scales) while running.

Travelers (cutouts, small, with a glow added in code):
- bst-air-puff: "A small puffy light blue cloud of air with a soft glow"; 1:1; cutout yes; people no; Breath of air token.
- bst-apple-bite: "A small bite-sized piece of red apple with white flesh"; 1:1; cutout yes; people no; Bite of apple token.
- bst-spark: "A small bright yellow zigzag spark of light"; 1:1; cutout yes; people no; Brain message token.

Activities (full-frame little scenes, used on the four activity buttons and above the Team play card):
- bst-act-resting: "A comfy armchair beside a sunny window with an open book on the seat"; 4:3; cutout no; people no.
- bst-act-running: "A pair of blue running shoes on a red school running track in sunshine"; 4:3; cutout no; people no.
- bst-act-lunch: "A school lunch tray with a sandwich, carrot sticks, a pear and a carton of milk"; 4:3; cutout no; people no.
- bst-act-sleeping: "A cozy bed with a blue quilt and a pillow, a night window with stars and a crescent moon"; 4:3; cutout no; people no.

Drawn in code: the body outline (the diagram frame every path, line and label is laid on; it stays a plain glowing silhouette so it re-lays out per size and needs no person image), nerves, spinal cord, arteries and veins, esophagus, mouth and nose openings, the traveler paths, ribbons, food dots, sweat drops, sparks on the nerves, gauges, labels and preview.svg.

## Voice
`upbeat-guide` (Zephyr): "Say brightly and clearly, like an upbeat tour guide." Different from fitness-circuit (big-sister), growing-up-q-a (clear-teacher) and playbook (lively-host). `Curio.voice`, scope mode plus traveler.
| Key | Kind | When it plays | Line | Stale when |
|---|---|---|---|---|
| wRide | how | entering Ride along, first time | Welcome aboard! Tap Ride to start the tour, or tap Next stop to go one stop at a time. | Ride, Next stop or a traveler tapped; mode left |
| wWork | how | entering Body at work, first time | Tap an activity, like Running, and watch every system change. | an activity tapped; mode left |
| wSys | how | entering Systems, first time | Tap a part of the body to learn what it does. Use the switches to show or hide a system. | a part or switch tapped; mode left |
| again | how | the first Team card of the load, after team | Tap Ride another to pick a new traveler. | Ride another tapped |
| check | how | Team check opened, first time | Tap every system that works harder when you run. Then tap Check. | Check tapped; Team check closed |
| stop.* | event | each time a stop opens | each ride stop text in Content (23 lines) | another stop or traveler showing |
| ribbon.* | event | each time a handoff ribbon shows, before the next stop's line | each handoff ribbon text (10 lines) | its stop has passed |
| team | event | each time a ride ends | That ride used {n} systems working as a team. | ride restarted or traveler changed |
| play.* | event | each time an activity is picked | each Team play card (4 lines) | another activity picked |
Part fact cards are read on screen; Read speaks the open card, else the current stop, else the hint.

## Family engine
none

## Sources
- NHES 2024 (SHAPE America), Standard 1: https://www.shapeamerica.org/standards/health/
- Heart is a pump with two sides, right to lungs and left to body; arteries and veins: NHLBI, "How the Heart Works": https://www.nhlbi.nih.gov/health/heart
- Air path, air sacs, oxygen and carbon dioxide exchange, diaphragm: NHLBI, "How the Lungs Work": https://www.nhlbi.nih.gov/health/lungs
- Mouth, saliva, esophagus muscles, stomach, small intestine absorption, liver bile, large intestine and fiber: NIDDK, "Your Digestive System and How It Works": https://www.niddk.nih.gov/health-information/digestive-diseases/digestive-system-how-it-works
- Brain, spinal cord and nerves carry messages; brainstem runs breathing and heartbeat: NINDS, "Brain Basics: Know Your Brain": https://www.ninds.nih.gov/health-information/public-education/brain-basics/brain-basics-know-your-brain
- Heart about the size of a fist; adult skeleton 206 bones; skull, ribs and spine protect organs; muscles pull on bones; heart muscle: NCI SEER Training, Anatomy and Physiology: https://training.seer.cancer.gov/anatomy/
- Resting pulse ranges by age: MedlinePlus, "Pulse": https://medlineplus.gov/ency/article/003399.htm
- Breathing rates, school-age children 18 to 30 a minute: MedlinePlus, "Rapid shallow breathing": https://medlineplus.gov/ency/article/007198.htm
- Working hard heart rate (vigorous: 77 to 93 percent of 220 minus age; age 10 gives 162 to 195): CDC, "Target Heart Rate and Estimated Maximum Heart Rate": https://www.cdc.gov/physical-activity-basics/measuring/heart-rate.html
- Sweat cools the body: MedlinePlus, "Sweat": https://medlineplus.gov/sweat.html
- Sleep: heart and breathing slow, memory, deep sleep and growth hormone: NHLBI, "How Sleep Works" and "Why Is Sleep Important?": https://www.nhlbi.nih.gov/health/sleep
- 9 to 12 hours for ages 6 to 12: CDC, "About Sleep": https://www.cdc.gov/sleep/about/index.html
- Example beats and breaths (85, 170, 70, 20) and the beats-per-day line are the tool's own examples inside the sourced ranges, labeled "Example" on screen.
- Art: original paintings made for this tool with local FLUX (Art).
- Checks run (Python, 2026-10-29): 85 x 1,440 = 122,400 beats a day. CDC vigorous range at age 10: 220 - 10 = 210; 77 percent is 161.7 and 93 percent is 195.3, so "about 162 to 195" holds and 170 sits inside it; 85 is inside both resting ranges (70 to 110 and 60 to 100); 20 breaths is inside 18 to 30. Rides counted: 9 + 7 + 7 = 23 stop lines; ribbons 4 + 3 + 3 = 10. Team check answers match the Running row of the activity table (every system Busy or Very busy except Digestion, Resting). Every contrast in Look recomputed with the WCAG 2.1 formula; all match to rounding, and the six system colors on the stage run 6.34 to 15.32:1.

## Done when
1. Each of the three rides plays start to end with Ride and with Next stop; stop counts are 9, 7 and 7; every system change shows its ribbon; the Team card lists the systems in order.
2. Back and Next are disabled at the ends; switching traveler mid-ride restarts cleanly with no leftover speech.
3. Body at work: each activity sets the gauges and numbers in the table; the beats-per-day line equals the example beat times 1,440 (85 gives 122,400).
4. With Motion off nothing moves, yet every gauge, number and card still updates.
5. Team check marks Digestion ✗ and the other five ✓ with their reasons.
6. Systems: every labeled part opens its card by mouse and by keyboard; hiding a layer hides its parts from the tab order.
7. At 1366x768 the figure, traveler buttons, stop card and Next stop are visible without scrolling; at 680x425 scene text is 10 px or more; at 375 wide (host) the stage is first and Next stop is reachable.
8. Welcome and how-to lines speak once per load; stop and ribbon lines speak each time their stop comes up and are dropped when the student has moved on.
9. Focus: at 1366x768 and 680x425 the body is the biggest thing on the stage in every mode, the lit part holds the traveler, and every painted organ sits inside the outline in its place at every size (mirrored arm and leg pieces line up on both sides).
10. Tap while it plays: during Ride, Next stop, Back, Pause and a traveler tap each act at once (mid-glide and mid-line); in Body at work an activity tap changes the paces at once; no old line plays after.
11. The welcome names only live controls: Ride and Next stop work the moment the tool opens.

## Open questions
- The body outline stays a plain glowing silhouette drawn in code (the frame for every path and label), with painted organs inside. OK, or should it be a painted figure too (one more image, people: true, waiting on Cory)?
