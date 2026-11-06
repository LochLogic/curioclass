# Worry Size Sorter

## One idea
Every worry is real, and its size is how much help it needs: drag everyday worries into Small, Medium and Big baskets, practice a real coping tool on the small and medium ones and watch your own worry meter, and find out that a Big worry goes to a trusted adult every time, even when someone said not to tell.

## Not like
- calm-corner (K-2, teacher-led, built): five calm-down tools for a class on a projector. Here a grade 3-5 student works alone; tools are tied to a sized worry, rated with a before-and-after meter and turned into a week goal. Different tools too: box breathing, talk back, squeeze and let go and a worry box (no balloon, star, counting or stretches).
- feelings-weather-report (K-2, built): naming feelings as weather. Here the feeling is given (worry); the move is sizing it and choosing help.
- mind-map (9-12, built): mental health conditions, myths and crisis lines for teens. Here nothing is a condition or diagnosis; help is a trusted adult, with one hotline for kids who cannot tell anyone they know.
- recess-upstander (3-5 health, concept): bullying seen from a bystander across a week. Here being hurt is one Big card among thirteen, and the student is the one with the worry.
- safety-sweep-house (3-5 health, concept): hazards in a house. Here the online-photo card is sized and sent to an adult; there is no house to search.
- growing-up-q-a (3-5 health, spec): a read-and-browse shelf. Here the student drags, practices and keeps a chart.

## Who and how
- Grade 3-5, Health, module Worries and Coping. Driver: students (solo by default, rule 4); a teacher can project Sort and let the class call out baskets. Minutes: 15-30, plus one minute a day for a week.
- Standards: NHES.S1, NHES.S6, NHES.S7 (NHES 2024). tool.json modes: ["Sort", "Body clues", "Tools", "My week"]. No score.
- The student never types a worry of their own; every worry is a written card. Nothing typed anywhere.
- Disclosure: the Big cards (a secret that feels wrong, being hurt, an online stranger, a very sick family member, weeks of worry) may bring a real disclosure. notes.md names this (rule 8) and says: if a student tells you something about abuse, being hurt or not being safe, stay calm, thank them, do not promise to keep it secret, and follow your school's reporting procedure (in the US, school staff are mandated reporters). Class talk stays on the cards; no one is asked to share their own worries aloud. On screen, the Big panel and Read say "You never have to tell the class. Tell one grown-up you trust."

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| NHES.S1 (1.5.2 health-promoting behaviors; 1.5.7 when and why to seek help) | Taps the five body clues; sorts the five Big cards; reads the "too big to carry" signs | Each clue's fact; every Big card lands in Big with its reason and the trusted-adult panel | Every body clue opens its fact; a Big card dropped in Small or Medium moves to Big with its reason |
| NHES.S6 (6.5.1, 6.5.3, 6.5.4, 6.5.5, 6.5.6) | Picks a tool, a time of day and a helper; picks the "because" from their own meter result; checks off each day; reflects at the end | A goal sentence built from their choices; a 7-day chart; a week-end reflection with what helped and what got in the way | A goal can be set, today checked, future days refused, and day 8 opens the reflection with the right N-of-7 line |
| NHES.S7 (7.5.1, 7.5.2) | Does each tool (breathes the square, picks a talk-back, squeezes and lets go, boxes the worry) and rates the worry meter before and after | The meter's before and after, the change in words, and "This one helps me" adding the tool to My helpers | Each tool runs start to end, the meter result matches the before/after for all 25 pairs, and My helpers feeds My week |

## Screens and modes
Header: title "Worry Size Sorter", small line "Size it. Try a tool. Get help.", mode buttons **🧺 Sort**, **💓 Body clues**, **🛠 Tools**, **📅 My week** (keys 1 to 4), then **Motion**, **Sound**, **Read**.

On load: Sort is shown with the first card on top of the stack and its three baskets. Hint: "Drag the card into Small, Medium or Big. Or tap the card, then tap a basket." Nothing speaks before the first tap. The first tap on the card picks it up (its own sound only); the first tap on a basket with no card held does nothing but show the basket's meaning (no line); the first tap on a mode button opens that mode and queues its welcome. The welcome may be cut by a tap (BASELINE 16); everything it says is also in the hint and Read.

### Sort (opens first)
- Focus: the worry card and the baskets. At 1366x768: stage about 940 px wide on the left, panel 380 px on the right. The card (about 380x290: painted vignette on top, the worry text under it, 22 px) sits centered at the top of the stage; under it the three baskets in a row, Small (smallest), Medium, Big (largest), each with its name and meaning in code on a label strip. A thin line above the baskets: "Every worry is real. Its size is about how much help it needs." All of it above the fold.
- Basket meanings: Small "I can handle it with a tool." Medium "A tool, and talk it over with someone." Big "Tell a trusted adult. Now."
- Panel: the hint, then the result of the last drop, then its buttons, then a progress line "4 of 13 sorted".
- Drop a Small or Medium card in Small or Medium: it settles in the basket (a thumbnail joins the basket's row). Panel: "You put it in Medium." then the card's "Many kids say" line and its "It gets bigger if" line, then buttons **Try a tool on it** (opens Tools with this worry) and **Next worry ▶**.
- Drop a Small or Medium card in Big: accepted. Panel: "Telling a trusted adult is never wrong. Many kids could also work on this one with a tool." Buttons **Try a tool on it**, **Next worry ▶**.
- Drop a Big card in Small or Medium: the card lifts and slides into Big (0.6 s; jumps with Motion off). Panel: "This one is Big." and the card's reason, then the trusted-adult panel. Same panel when it is dropped in Big at once, opened by "Yes, this one is Big."
- Trusted-adult panel (replaces the drop result in the panel, scrolls nothing at 1366x768): "Big worries go to a trusted adult, every time." The six adults as small chips in code (Parent or caregiver, Grandparent, Teacher, School counselor, Coach, Doctor); "Ways to start" (three lines, Content); "If that grown-up doesn't help, keep telling until someone does." "Danger right now? Call 911." "Can't tell anyone you know? Call or text Childhelp: 1-800-422-4453." "You never have to tell the class. Tell one grown-up you trust." Button **Next worry ▶**.
- After card 13: the stage shows the three baskets with their thumbnails and counts. Panel end card: "You sorted 13 worries. Big: N. Every Big one goes to a trusted adult." A second line by case: if any Small or Medium card went to Big, "You put K in Big that a tool could also help. Telling is never wrong; a tool can help while you wait."; if no tool was tried, "Pick one worry and try a tool on it."; else "Tools you tried: T." Buttons **Make my week goal ▶** (My week), **Sort again** (new shuffle, empty baskets; My helpers and the goal are kept).
- Card order: shuffled once per load, with the rule that the first two cards are one Small and one Medium, and no two Big cards come in a row.
- At 680x425: the line above the baskets folds away, basket meanings shrink to the name only (meaning on tap and in Read), the card art is 40 percent smaller, the panel stays at the right at 240 px with the drop result and one button visible.

### Body clues
- Focus: the painted kid (cutout `ws-kid-stand`, whole body visible, centered, about 560 px tall at 1366x768) with five numbered hotspot rings in code. Panel: the open clue, then "When is a worry too big to carry?" card.
- Hotspots: Head (thoughts and sleep), Chest (fast heart), Lungs (fast breathing), Tummy (butterflies, stomachache), Hands and shoulders (sweaty, shaky, tight). Tap one: its ring fills in the accent, the panel shows the clue (Content), and a small line under each clue names the tool that answers it ("Try: Box breathing").
- First line of the panel before any tap: "Worry is your body getting ready for a challenge. Tap a ring to see where it shows up."
- "Too big to carry" card (always visible under the clue): "Tell a trusted adult if a worry: lasts for weeks, gets in the way of school, home or play, keeps you from sleeping, or is about someone being hurt or not safe."
- At 680x425 the kid shrinks to fit the stage height and the "Too big" card folds to its title (tap to open).

### Tools
- Focus: the tool's own picture in the stage center (the breathing square, the worry cloud, the squeezing kid, the worry box). Panel: the worry meter and the steps.
- Top of stage: four tool tiles, **Box breathing**, **Talk back**, **Squeeze and let go**, **Worry box**, each with a code icon and its name. When opened from Sort, a line above the tiles shows the worry: "Your worry: A spelling test tomorrow." Opened from the header with no card, Talk back and Worry box use a worry the student picks from a list of the eight Small and Medium cards (default the first Small card).
- Every tool runs in three steps, shown as steps 1-2-3 in the panel:
  1. **Before**: the worry meter, a vertical 5-step thermometer in code: 1 Calm, 2 A little, 3 Some, 4 A lot, 5 Very. "How worried does your body feel right now? Tap a step." For a card, a note: "Picture it's really happening." Tapping a step starts step 2 (the tool's Start button appears and is enabled).
  2. **The tool** (below).
  3. **After**: the meter again, then the result line (Content, "Meter results") and buttons **This one helps me** (adds to My helpers, toggles to "In My helpers ✓"), **Try another tool**, **Back to sorting** (only when opened from Sort).
- Box breathing: a square drawn in code (420 px at 1366x768), a dot travels one side per phase: up the left side "Breathe in", across the top "Hold", down the right "Breathe out", along the bottom "Hold". The side being traced thickens and a count 1 to 4 shows in the middle, one per second. Buttons **Start**, **Stop**, and a **Count of 4 / Count of 3** toggle (3 is shorter, for when 4 feels long). Two rounds play (32 s at 4, 24 s at 3: the source's practice needs more than a few breaths), then "Another round?" **One more round** (up to 4 rounds) or **Done** (to step 3). Stop at any moment goes straight to step 3. Changing the count during a round applies from the next phase at once.
- Talk back: the worry cloud creature (painted) floats over the card's vignette with a speech bubble in code saying the worry's thought (Content). Three talk-back buttons (Content), all helpful, each a different style (Facts, Plan, Brave). Tap one: the student's bubble shows it, the cloud swaps from `ws-cloud-big` to `ws-cloud-mid`; tap a second one: `ws-cloud-small`. A line: "Say it out loud, or in your head. Worry talks less when you talk back." **Done** goes to step 3 (enabled after one talk-back).
- Squeeze and let go: the painted kid in poses. Three parts, one at a time: Hands ("Make two tight fists"), Shoulders ("Pull your shoulders up to your ears"), Feet ("Curl your toes tight"). Each part: squeeze 5 s with a code bar filling, then "Let go" 10 s, the kid in `ws-kid-loose`. Pose per part while squeezing: `ws-kid-fists`, `ws-kid-shoulders`, `ws-kid-toes`. The student taps **Next part ▶** after each (each run is 15 s); **Stop** goes to step 3. A line: "Notice how loose feels after tight."
- Worry box: the card's worry printed on a paper slip in code, in the tool's plain font. Tap **Fold it**: the slip folds twice (code animation, 0.8 s; instant with Motion off). Tap **Put it in the box**: it drops into the painted box `ws-worry-box`. Panel: "Your worry is in the box. Pick a worry time with a grown-up, 10 minutes, not at bedtime, to open it and talk. At home, write it on real paper." **Done** to step 3.
- At 680x425: the tiles become a single row of icons, the meter becomes a horizontal 5-step row, and the tool picture fills the stage.

### My week
- Focus: the 7-day chart. Before a goal exists, the stage shows the goal builder; after, the chart takes the stage and the goal sentence sits above it.
- Goal builder (three rows of choices, all visible at 1366x768): **Tool**: the four tools, with My helpers marked "Helps me" and listed first; **When**: Morning (`ws-icon-morning`), After school (`ws-icon-afterschool`), Bedtime (`ws-icon-bedtime`); **Who helps me remember**: A grown-up at home, My teacher, A friend, Me (a note or alarm). Then **Because**: if the chosen tool has a meter result this load, the line is built from it ("Because my meter went from 4 to 2 when I tried it"); else the student picks the body clue it helps (fast heart, fast breathing, tight muscles, busy thoughts). **Set my goal** is enabled when Tool, When and Who are picked.
- Goal sentence: "I will do Box breathing at Bedtime every day this week. A grown-up at home helps me remember. Because my meter went from 4 to 2 when I tried it."
- Chart: seven columns labeled with weekday names from the start day (code), today ringed. Tap today (or a past day you forgot) to check it off; tap again to uncheck. Future days are locked and show a small lock; tapping one shows "Come back on Thursday to check this one." Counter "Done: 3 of 7".
- Privacy line, always on screen under the chart and the builder: "Your goal and check marks stay on this device. They never leave it."
- Buttons: **Practice now** (opens the goal's tool in Tools), **Finish my week** (opens the reflection early), **New goal** (asks "Start over? Your check marks will be cleared." **Yes, start over** / **Keep my goal**).
- Reflection (day 8 or Finish my week): "You did it N of 7 days." with the N line (Content), then **What helped?** and **What got in the way?** chips (multi-pick, Content), then **Next week I will**: Keep this goal / Change the time / Try a different tool. Choosing one starts a new week with that change pre-filled in the builder.
- At 680x425: the builder shows one row at a time with **Next ▶**; the chart keeps all seven columns at 44 px.

## Content

### Worry cards (id, size, text, art)
Small (both Small and Medium accepted; "Many kids say Small"):
- s1 "A spelling test tomorrow." Gets bigger if: "you can't sleep, or it happens before every test." Art ws-card-test.
- s2 "I can't find my library book." Gets bigger if: "it's been missing for weeks and you're scared to say so." Art ws-card-book.
- s3 "I have to read out loud in class." Gets bigger if: "you start feeling sick every time it's your turn." Art ws-card-podium.
- s4 "My first swim lesson is tomorrow." Gets bigger if: "you're scared of the water and no one knows." Art ws-card-pool.
Medium ("Many kids say Medium"):
- m1 "My friend seems mad at me." Gets bigger if: "it turns into being left out or teased every day." Art ws-card-bench.
- m2 "We're moving, and I'll go to a new school." Gets bigger if: "you feel sad or scared most days for weeks." Art ws-card-boxes.
- m3 "My grown-ups were arguing, and I keep thinking about it." Gets bigger if: "anyone gets hurt, or you feel unsafe at home. Then it's Big." Art ws-card-kitchen.
- m4 "I got a bad grade, and I'm scared to show my family." Gets bigger if: "you're afraid someone will hurt you. Then it's Big." Art ws-card-folder.
Big (only Big; reason shown):
- b1 "A grown-up asked me to keep a secret, and it feels wrong." Reason: "A secret that feels wrong, or that you're told to keep from your family, is always one to tell." Art ws-card-door.
- b2 "Someone at home is very sick." Reason: "This is too heavy to carry alone. A trusted adult can help you understand it and help you feel better." Art ws-card-bedside.
- b3 "Someone online asked me for a photo and said to keep it secret." Reason: "Tell a trusted adult right away, even if you already sent something. You won't be in trouble for telling." Art ws-card-tablet.
- b4 "An older kid hurts me on the bus and says not to tell." Reason: "Being hurt is never okay. Someone saying 'don't tell' is a sign to tell." Art ws-card-bus.
- b5 "I've felt worried almost every day for weeks, and it's hard to sleep." Reason: "Worry that lasts for weeks, or gets in the way of sleep, school or play, is a sign to get help." Art ws-card-calendar.

### Ways to start (trusted-adult panel)
- "I need to tell you something important."
- "Something is worrying me and I need help."
- "Someone told me to keep a secret, and it doesn't feel right."

### Talk back (worry thought; Facts / Plan / Brave)
- s1 "You'll forget every word." / "I practiced. I know most of them." / "I'll go over the hard ones once more tonight." / "One test is one test. I can do hard things."
- s2 "You'll be in big trouble." / "Lots of kids lose a book. Libraries help find them." / "I'll check my backpack, then ask the librarian." / "I can tell the truth and fix it."
- s3 "Everyone will laugh." / "Most kids are busy thinking about their own turn." / "I'll take a breath and read slowly." / "My voice might shake, and I can still do it."
- s4 "You'll sink." / "The teacher is right there, and lessons start in shallow water." / "I'll tell the teacher I'm nervous." / "Brave means scared and trying anyway."
- m1 "They hate you now." / "I don't know that yet. Maybe they're having a bad day." / "I'll ask, 'Are we okay?'" / "I can be kind first."
- m2 "You'll never make a friend." / "I made friends before. I can do it again." / "I'll say hi to one kid the first day." / "New is hard, and I can handle hard."
- m3 "It's your fault." / "Grown-ups argue sometimes. It isn't my job or my fault." / "I'll tell a grown-up I trust how it made me feel." / "I can take care of me right now."
- m4 "Everyone will be mad forever." / "One grade doesn't decide everything." / "I'll show it and ask what to work on." / "Telling the truth takes guts, and I have guts."

### Body clues (spot, clue, try)
- Head: "Worry thoughts can loop: what if, what if. They can make it hard to fall asleep." Try: Worry box, Talk back.
- Chest: "Your heart beats faster. Your body is getting ready to act, like before a race." Try: Box breathing.
- Lungs: "Breathing gets fast and shallow. Fast breathing can make worry feel bigger." Try: Box breathing.
- Tummy: "Butterflies, or a stomachache. Lots of kids feel worry in their tummy." Try: Box breathing, Talk back.
- Hands and shoulders: "Hands can get sweaty or shaky. Muscles get tight, and tight muscles tell your body it's stressed." Try: Squeeze and let go.
Intro (panel): "Worry is your body getting ready for a challenge, even when there's no real danger. The feelings are real, and they pass."

### Meter results (before b, after a)
- a < b: "Your meter went from b to a. This tool helped your body calm down."
- a = b, b > 1: "Same as before. That's okay. Not every tool works every time. Try another one."
- a > b: "Your meter went up. That happens. Try a different tool, or talk to someone."
- b = 1 and a = 1: "You started calm. Practicing when you're calm makes a tool ready for a hard day."

### Week reflection
- N = 7: "Every day! That's a habit starting." 4 to 6: "Most days. Nice work." 1 to 3: "A start. What got in the way?" 0: "The week got away. That happens. Try an easier time of day."
- What helped: "My helper reminded me", "I did it at the same time", "It made me feel better", "It was quick".
- What got in the way: "I forgot", "I was busy", "I didn't feel worried", "It felt silly", "Someone interrupted".

## Interactions in detail
- Drag: pointer drag with a ghost of the card; a basket highlights when the card is over it; dropping elsewhere returns the card to the top (0.3 s). Tap-to-place: tap the card (it lifts, "Picked up") then tap a basket. Keyboard: Enter or Space picks the card up, 1/2/3 or arrow keys and Enter place it, Esc puts it back.
- Taps while anything plays: a basket tap during the Big slide finishes the slide at once and opens the panel; **Next worry** during the slide does the same and then advances. In Box breathing, Stop, the count toggle and every mode button act at once; Stop never waits for the phase to end. A mode switch stops any tool run and hushes speech; coming back to Tools shows step 1 again for that tool.
- Sort again keeps My helpers and the goal. Reloading the page keeps only My week (goal, start date, checks, helpers) in localStorage `wss-week` (try/catch; if storage is blocked the chart works for this visit and the privacy line adds "This browser won't save it.").
- Week day index: the start date is the local calendar date the goal was set (YYYY-MM-DD). Index = calendar days from start to today, counted on dates, not hours, so daylight saving never shifts it. Index 0 to 6: that column is today. Index 7 or more: the reflection opens. A negative index (the clock was set back) shows day 1.
- Extremes: all 13 cards in one basket (no Big card ever lands outside Big); every card in Big (accepted, end note counts them); no drops at all (no progress, no end screen, nothing scored); meter 1 to 1, 5 to 5, 1 to 5, 5 to 1 (each has its line); a week with 0 or 7 checks (each has its line).
- Done-state words match the state: the panel never says "Try a tool" for a Big card, and the end line counts the real cards.

## Look
- Accent `--brand` #9a4a1c (warm clay), on a light `:root`: paper #fdf7ee, ink #2a211a, muted #6b5b4c, line #ecdcc8, focus #2f5bd3, panel #ffffff.
- Basket colors (each also named in words on its label): Small #2f6e4a green, Medium #8a5a00 amber, Big #2c4f8f deep blue (calm, not alarm red).
- Contrast (computed): brand on white 6.23:1, on paper 5.85:1; white on brand 6.23:1; ink on paper 14.81:1; muted on paper 6.11:1; white on Small 6.09:1, Medium 5.93:1, Big 8.01:1; Small, Medium, Big on paper 5.71, 5.56, 7.52:1.
- Neighbors: calm-corner #2f7a62, feelings-weather-report #26627a, mind-map #1f5c63, label-detective #1d5c63, germ-spread-sim #1f7a6a, growing-up-q-a #8e4a7a, body-systems-tour #c2410c, fitness-circuit #6f2dbd. Clay is darker and browner than body-systems-tour's orange.
- Rounded cards with a soft shadow, generous spacing, no confetti; the Big panel is calm, with the blue edge, not red.

## Art
26 images. One style for all: "soft gouache picture-book illustration, warm light, gentle textures". Cutouts add "plain white background". Text on papers, screens and signs stays blank (code writes it).
People (people: true; drawn per BASELINE 11, on Cory's contact sheet, fresh-agent representation check; never a local model). One kid, the same in every pose: "A 9-year-old kid with short curly dark hair, warm brown skin, a mustard yellow hoodie, blue jeans and red sneakers, full body, front view". 3:4, cutouts, whole body inside the frame with margin:
- ws-kid-stand: standing relaxed, arms at sides, calm face. Body clues; whole figure visible, hotspots placed over it.
- ws-kid-fists: standing, both hands in tight fists at chest height, eyes squeezed. Squeeze, Hands part.
- ws-kid-shoulders: standing, shoulders pulled up to the ears. Squeeze, Shoulders part.
- ws-kid-toes: sitting on a low stool, feet flat, toes curled, sneakers off, socks on. Squeeze, Feet part.
- ws-kid-loose: standing with arms hanging loose, shoulders low, soft smile, eyes half closed. Every Let go.
No people (local FLUX):
- ws-basket: "A sturdy woven wicker basket with two handles, front view"; 1:1; cutout; drawn three times at 70, 85 and 100 percent for Small, Medium, Big with code label strips.
- ws-cloud-big: "A puffy gray storm cloud creature with a worried frown and small stick arms crossed"; 1:1; cutout; Talk back start.
- ws-cloud-mid: "A smaller light gray cloud creature with a doubtful sideways look"; 1:1; cutout; after one talk-back.
- ws-cloud-small: "A tiny pale cloud creature with a sleepy small smile"; 1:1; cutout; after two talk-backs. The three differ by size, color and face at 64 px.
- ws-worry-box: "A shoebox covered in blue paper with painted stars and a slot cut in the lid"; 1:1; cutout; Worry box.
- ws-icon-morning: "A sunrise over a windowsill with a cereal bowl"; 1:1; My week When.
- ws-icon-afterschool: "A backpack leaning on a front door with a snack apple"; 1:1; My week When.
- ws-icon-bedtime: "A bedside lamp glowing beside a pillow and a crescent moon in the window"; 1:1; My week When.
- ws-bg: "A soft sunny classroom corner with a reading rug, cubbies and a plant, blurred and calm"; 16:10; Sort stage background at 30 percent strength under the baskets.
Card vignettes, 4:3, used on the card and as basket thumbnails:
- ws-card-test: "A school desk with a blank paper test and a sharpened pencil".
- ws-card-book: "A library shelf with one empty gap between colorful books with blank spines".
- ws-card-podium: "A classroom reading chair with an open picture book on a small stand".
- ws-card-pool: "Swim goggles and a towel at the edge of a bright indoor pool, shallow steps".
- ws-card-bench: "An empty playground bench under a tree with a dropped jump rope".
- ws-card-boxes: "Moving boxes stacked by a front door with a backpack on top".
- ws-card-kitchen: "A quiet evening kitchen with two coffee mugs left on the table".
- ws-card-folder: "A school folder on a bed with a blank paper sticking out".
- ws-card-door: "A closed wooden bedroom door with a soft hallway light underneath".
- ws-card-bedside: "A bedside table with a glass of water, pill bottles with blank labels and a handmade blank card".
- ws-card-tablet: "A tablet on a bed showing a blank chat screen".
- ws-card-bus: "An empty yellow school bus seat seen from the aisle, a backpack on the floor".
- ws-card-calendar: "A wall calendar with blank squares beside a window with rain".
Drawn in code: the breathing square and its dot, the worry meter, hotspot rings, speech bubbles, paper slip and its fold, basket label strips, chips, the week chart, tool tile icons and preview.svg.

## Voice
`friendly-dad` (Achird): "Say in a relaxed, friendly way, like a kind dad helping with homework." Different from calm-corner (warm-teacher), feelings-weather-report (hero-coach), growing-up-q-a (clear-teacher), body-systems-tour (upbeat-guide), fitness-circuit (big-sister), playbook (lively-host). `Curio.voice`, scope = mode plus tool. Card texts, clues and panel copy are read on screen; Read speaks the hint, then the open card or panel.
| Key | Kind | When | Stale when | Line |
|---|---|---|---|---|
| wSort | how | entering Sort first time | a card is picked up; mode left | Every worry is real. Its size is how much help it needs. Drag the card into Small, Medium or Big. |
| wClues | how | entering Body clues first time | a ring tapped; mode left | Worry shows up in your body. Tap a ring on the kid to see where. |
| wTools | how | entering Tools first time | a tile or meter step tapped; mode left | Pick a tool. First, tap the meter to show how worried your body feels. |
| wWeek | how | entering My week first time, no goal | a choice tapped; mode left | Pick a tool, a time and a helper. Then tap Set my goal. |
| howAfter | how | first step 3 | a meter step tapped | Tap the meter again. How does your body feel now? |
| big | event, whole | each time a Big card lands in Big | never (plays every time; Next worry waits for it with a "Listening" dim, max 4 s) | This one is Big. Tell a trusted adult. Keep telling until someone helps. |
| bIn, bHold, bOut | event | each breathing phase starts | the phase ended or Stop | Breathe in. / Hold. / Breathe out. (the second Hold reuses bHold) |
| sqz, letgo | event | each squeeze part / let-go starts | the part ended or Stop | Squeeze tight. / Now let go. |
| meterDown | event | step 3 result, a < b | step left | Your meter went down. That tool helped. |
| meterOther | event | step 3 result, a >= b | step left | That's okay. Try another tool, or talk to someone. |
| goalSet | event | Set my goal | mode left | Your goal is set. Check off each day you do it. |
| checked | event | a day checked off, at most once per day | another tap | Checked. Nice work. |
| weekEnd | event, whole | reflection opens | mode left | Your week is done. Let's look at what helped. |
The Big line plays whole; the drop result panel shows at once and only **Next worry** waits. Breathing and squeeze cues are spoken every phase because the student's eyes may be closed; with Sound off the on-screen count carries it. No line names a disabled control (wTools names the meter, which is always enabled).

## Family engine
none

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Worry/anxiety comes from the fight-or-flight response; hormones get the body ready for a challenge even without real danger | KidsHealth (Nemours), "Anxiety" https://kidshealth.org/en/teens/anxiety.html | Cleveland Clinic, "Box Breathing" (stress activates fight or flight) https://health.clevelandclinic.org/box-breathing-benefits | yes |
| Faster heartbeat and breathing | KidsHealth "Anxiety" | CDC, "Anxiety and Depression in Children" (heart pounding) https://www.cdc.gov/children-mental-health/about/about-anxiety-and-depression-in-children.html | yes |
| Fast, shallow breathing can increase anxiety | Cleveland Clinic "Box Breathing" | WebMD, "What Is Box Breathing?" (helps hyperventilation) https://www.webmd.com/balance/what-is-box-breathing | yes |
| Butterflies or stomachaches | KidsHealth "Anxiety" | CDC page; NIMH, "Children and Mental Health" https://www.nimh.nih.gov/health/publications/children-and-mental-health | yes |
| Sweaty or shaky hands | KidsHealth "Anxiety" | CDC page (shaky, sweaty) | yes |
| Worry can make it hard to sleep | CDC page (trouble sleeping) | NIMH (sleep problems) | yes |
| Stress tightens muscles; tight muscles keep the stress cycle going | Michigan Medicine (Healthwise), "Progressive Muscle Relaxation" https://www.uofmhealth.org/health-library/ta4146 | HealthLinkBC (Healthwise), "Progressive Muscle Relaxation" https://www.healthlinkbc.ca/healthwise/progressive-muscle-relaxation | yes |
| Squeeze a muscle group, then let go completely (tense 4 to 10 s, rest 10 to 20 s); the tool uses 5 s and 10 s | Michigan Medicine | HealthLinkBC | yes |
| Box breathing: in 4, hold 4, out 4, hold 4; 3 to 4 rounds | Cleveland Clinic | WebMD | yes |
| Start with 2 or 3 counts if 4 feels long; don't strain | WebMD | Cleveland Clinic ("stay at your comfort level") | yes |
| Talking back to worry with helpful, realistic self-talk helps kids cope | HereToHelp BC (Anxiety Canada material), "Healthy Thinking for Younger Children" https://www.heretohelp.bc.ca/sites/default/files/healthy-thinking-for-younger-children.pdf | KidsMatter (Australia), "Fears and helpful self-talk" | yes |
| Worry box: write a worry, put it in a box, talk about it at a set worry time (about 10 to 15 minutes, not right before bed) | YoungMinds, "How to make a worry box" https://youngminds.org.uk/blog/how-to-make-a-worry-box-a-guide-for-parents/ | Just One Norfolk (NHS), "Worry box" https://www.justonenorfolk.nhs.uk/media/us1bjpvw/worry-box.pdf | yes |
| Get help when worry lasts weeks or gets in the way of school, home or play | NIMH (weeks or longer; school, home, friends) | CDC (school, home or play) | yes |
| A secret you're asked to keep from your family, or that feels wrong, is one to tell | Childhelp, "Safe vs. Unsafe Secrets" https://childhelp.org/safe-vs-unsafe-secrets-how-to-talk-to-kids-about-the-difference/ | eSafety Commissioner (Australia), "Secrets and surprises" https://www.esafety.gov.au/sites/default/files/2026-09/secrets-and-surprises-sept-2026.pdf | yes |
| Keep telling trusted adults until someone helps | Childhelp "Safe vs. Unsafe Secrets" | Advocates for Youth, 3Rs "Seeking Help" lesson https://www.advocatesforyouth.org/wp-content/uploads/2023/07/2.5_Seeking-Help_3Rs2023.pdf | yes |
| Trusted adults include parents, grandparents, teachers, school counselors, coaches, doctors | Childhelp (parents, grandparents, teachers, counselors, coaches, family friends) | KidsHealth "Anxiety" (parent, school counselor, doctor) | yes (each adult named by at least one; family and school adults by both) |
| An online stranger asking for a photo or secrecy: tell a trusted adult | NetSmartz (NCMEC) https://www.missingkids.org/netsmartz | US Attorney's Office tip sheet (tell a trusted adult if pressured for photos) https://www.justice.gov/usao-ri/file/765166/dl | yes |
| Childhelp hotline: call or text 1-800-422-4453; emergencies call 911 | Childhelp Hotline https://www.childhelphotline.org/ | Child Welfare Information Gateway contact page https://www.childwelfare.gov/ (call or text 1-800-4-A-CHILD) | yes |
| NHES 2024 standards 1, 6, 7 and 3-5 indicators 1.5.2, 1.5.7, 6.5.1 to 6.5.6, 7.5.1, 7.5.2 | SHAPE America, NHES 2024 https://shapeamerica.org/standards/health/new-he-standards/ | repo `data/standards/nhes-2024.txt` (codes) | yes |
Cut: "your face feels warm and your mouth dry" (KidsHealth only, no second source), so there is no Face ring.
Claims: 18 backed twice, 1 cut (warm face and dry mouth).
Number checks (S:/CurioClass-codex-scratch/specs/worry-size-sorter/checks.py, Python): contrast ratios above; box breathing 16 s a round at 4 (32 s for two, 64 s for four), 12 s at 3; squeeze part 15 s, three parts 45 s in three tapped runs; meter results for all 25 before/after pairs (down 10, up 10, same 4, calm start 1); week index across DST start, DST end with month end, a leap day, year end, day 8 (reflection) and a clock set back (day 1); week lines for N = 0 to 7; the sort rule through mash-all-Small, all-Medium, all-Big, random and right: no Big card ever ends outside Big (5 moved when mashed), all-Big is accepted with the end note.

## Done when
1. Focus: at 1366x768 Sort shows the card, all three baskets with meanings and the panel with its buttons above the fold; Body clues shows the whole kid; Tools shows the tool picture and the meter together; My week shows the full builder or all seven chart columns and the privacy line.
2. At 680x425 each mode keeps its focus and main controls visible, with the folds listed above.
3. Every Big card dropped in Small or Medium moves to Big with its reason and the trusted-adult panel (Standards map S1); a Small or Medium card dropped in Big is accepted with the "never wrong" note.
4. Each body clue ring opens its fact and its "Try" tool; the "Too big to carry" card is visible in Body clues.
5. Each of the four tools runs before, tool, after; the result line is right for 1 to 1, 5 to 5, 1 to 5 and 5 to 1; This one helps me lists the tool first in My week (Standards map S7).
6. A tap while anything plays acts at once: Stop mid-phase in Box breathing goes to step 3 at once; a mode switch mid-squeeze hushes speech and stops the run; Next worry during the Big slide finishes it and advances after the Big line.
7. My week: a goal sets only with Tool, When and Who; the "because" comes from the student's own meter result or their own clue pick; today and past days check, future days refuse; with the date moved to day 8 the reflection opens with the right N-of-7 line (Standards map S6).
8. The privacy line shows in My week; nothing is typed anywhere; only `wss-week` (and the kit's Motion) is in localStorage.
9. Voice: in five Big drops the Big line plays five times; wSort plays once, then hint only; no line plays after its phase or mode has passed.
10. Keyboard only: a card can be picked, placed, and every tool and the chart can be used, with visible focus.

## Open questions
- Sensitivity review (rule 5 spirit; content touches abuse, online exploitation and family illness): a fresh agent checks the five Big cards, their reasons, the talk-back lines for m3 and m4, and the trusted-adult panel wording, including whether the Childhelp line and number belong on screen for grades 3-5 (default: yes, under the trusted-adult line).
- People art: the five kid poses are one character; Cory sees them on the contact sheet (BASELINE 11).
