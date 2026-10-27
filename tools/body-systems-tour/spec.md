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

The body (all modes): a front-view figure drawn in code on a dark "inside" stage: a soft rounded outline with no face, no hair and no body details (a plain oval head, arms slightly out), sized to fill the stage height. Six system layers sit inside it, each a simple textbook-style SVG diagram (Content, "Systems and parts"). Layers not in use are faint (25 percent opacity); layers in use are full color.

### Ride along (opens first)
- Panel, top: three traveler buttons, each with icon and name: **🌬 Breath of air**, **🍎 Bite of apple**, **⚡ Brain message**. Under them: **▶ Ride** (auto, one stop every 4 s, becomes **⏸ Pause**), **Next stop ▶**, **◀ Back**, **↺ Start over**.
- Stage: the traveler is a glowing token (a small cloud, an apple piece, a lightning spark) on a dotted path through the layers. The path for the chosen traveler is drawn faintly from start to end so you can see where it will go.
- Stop card (panel, middle): stop number "Stop 3 of 9", the part name, its system tag (icon and color and name), and one or two sentences (Content).
- Handoff ribbon: when the next stop is in a different system, a ribbon slides across the stage between the two parts: "Lungs hand oxygen to the blood." The new layer brightens and the old one stays on, so by the end every system the traveler used is lit.
- End of ride: a "Team" card lists the systems the traveler used, in order, as icon chips ("Lungs → Heart and blood → Muscles"), with **Ride another** (shows the three traveler buttons again).

### Body at work
- Panel, top: four activity buttons with icons: **🪑 Resting**, **🏃 Running**, **🥪 Eating lunch**, **😴 Sleeping**.
- Stage: all six layers on. Each system animates at the activity's pace: the heart pulses at the example beat, the lungs swell at the example breath rate, food dots move through the gut while eating, small sparks run down the nerves, leg muscles tighten and relax while running, sweat drops appear on the outline while running.
- Panel, middle: six gauge rows, one per system, each with icon, name and a three-step word gauge (**Slow**, **Medium**, **Fast** or **Resting**, **Busy**, **Very busy**), plus a number where the Content gives one (heart, breathing). Under the heart row: "At this example beat a heart beats about 122,400 times a day" (computed: beats per minute times 1,440).
- Panel, bottom: the activity's **Team play** card (three sentences, Content).
- **Team check** (optional, a small button): "Tap every system that works harder when you run." The student taps layers on the body or gauge rows; **Check** marks each ✓ or ✗ with a one-line reason. No score, nothing kept.

### Systems
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
- Body at work: switching activity eases the animation rates over 1 s. With Motion off nothing pulses; the gauges and numbers still change and each system shows a static "working" glow in its own color.
- Tapping a system's layer in Body at work highlights its gauge row, and the reverse.
- Systems: hiding a layer also hides its labels; tab order is the panel toggles first, then the parts of visible layers, top to bottom.
- Sizes: at 1366x768 the whole figure, the traveler buttons, the stop card and Next stop are visible together. In the 680x425 preview the figure fits the stage height and labels are at least 10 px; the stop card shows the part name and first sentence. Under 900 px tall the panel puts Next stop and Ride above the stop card.
- Nothing is saved; no localStorage except the kit's Motion setting.

## Look
- Accent `--brand` #c2410c (burnt orange: the tour car and the traveler's glow), on its own light `:root`: paper #fff8f2, ink #2a1d16, muted #6b5a50, line #f1dccd, focus #2f5bd3, panel #ffffff. The stage is a deep "inside" night #1a1530 with the accent light #ff9a5c for the traveler and path.
- Contrast: accent on white 5.18:1, on paper 4.92:1; white text on accent 5.18:1; ink on paper 15.52:1; muted on paper 6.23:1; #ff9a5c on stage 8.4:1; label text #f4ecff on stage 15.32:1. System colors are all above 3:1 on the stage (shapes), and every system also has its icon and name.
- Group siblings: growing-up-q-a mauve, first-aid-responder mint, meal-and-move-planner sky blue, health-claim-checker yellow. 3-5 health neighbors: label-detective and germ-spread-sim teal, fitness-circuit raspberry, playbook green; none uses orange.

## Art
none: drawn in code (the figure outline, six system layers as simple diagrams, travelers, ribbons, gauges). No faces or body details.

## Voice
`upbeat-guide` (Zephyr): "Say brightly and clearly, like an upbeat tour guide." Different from fitness-circuit (big-sister) and playbook (lively-host).
| Key | Kind | Line | Stale when |
|---|---|---|---|
| wRide | how | Welcome aboard! Pick a traveler, then tap Ride or Next stop. | mode left |
| wWork | how | Tap an activity, like Running, and watch every system change. | mode left |
| wSys | how | Tap a part of the body to learn what it does. Use the switches to show or hide a system. | mode left |
| stop.* | event | each ride stop text in Content (23 lines) | another stop or traveler showing |
| ribbon.* | event | each handoff ribbon text (10 lines) | its stop has passed |
| team | event | That ride used {n} systems working as a team. | ride restarted |
| play.* | event | each Team play card (4 lines) | another activity picked |
| check | how | Tap every system that works harder when you run. Then tap Check. | Team check closed |
Part fact cards are read on screen; Read speaks the open card or the hint.

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

## Done when
1. Each of the three rides plays start to end with Ride and with Next stop; stop counts are 9, 7 and 7; every system change shows its ribbon; the Team card lists the systems in order.
2. Back and Next are disabled at the ends; switching traveler mid-ride restarts cleanly with no leftover speech.
3. Body at work: each activity sets the gauges and numbers in the table; the beats-per-day line equals the example beat times 1,440 (85 gives 122,400).
4. With Motion off nothing moves, yet every gauge, number and card still updates.
5. Team check marks Digestion ✗ and the other five ✓ with their reasons.
6. Systems: every labeled part opens its card by mouse and by keyboard; hiding a layer hides its parts from the tab order.
7. At 1366x768 the figure, traveler buttons, stop card and Next stop are visible without scrolling; at 680x425 scene text is 10 px or more; at 375 wide (host) the stage is first and Next stop is reachable.
8. Welcome and how-to lines speak once per load; stop and ribbon lines speak each time their stop comes up and are dropped when the student has moved on.
