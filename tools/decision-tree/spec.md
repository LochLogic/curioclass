# Decision Tree

## One idea
Grow a fictional kid's decision as a tree, then drag time from Right away to Next month and watch branches bloom or wilt against the goals you say matter: the branch that looks best right away is often not the one standing best a month later, and you can graft two branches into a better option.

## Not like
- conflict-coach (6-8, roleplay): there you replay one conversation line by line and the choice is how to say it. Here nobody talks, nothing is rewound, and the choice is what to do: you compare several whole options side by side as branches over time.
- walk-in-their-shoes (3-5, story): there you replay one moment through each character's eyes and pick one ending. Here you never switch viewpoint; you lay out every option at once, pick the goals, and scrub time across all of them.
- comeback-club (3-5, creature): a training loop with one creature and puzzles. No creature, no puzzles here; the only thing that grows is the tree you plant.
- calm-corner, feelings-weather-report (K-2): those name and calm feelings. Here no one's feelings are scored; branches are marked only against a fictional kid's goals.

## Who and how
- Grade 6-8, Social and Emotional Learning, module "Responsible Decisions (SEL)".
- Driver: students or teacher. Students on a laptop, alone or in pairs; or a teacher runs it on a projector in advisory and the class calls out which goals to turn on and which branch they think will win. 15 to 25 minutes.
- Standards: CASEL Responsible Decision-Making (identifying solutions for personal and social problems; anticipating and evaluating the consequences of one's actions).
- Sensitive by default: four fictional, ordinary dilemmas (a double booking, a quiz photo, a saved-money choice, a new game). There is no text box anywhere. The tool never asks about the student's own life, family or classmates.

## Screens and modes
Header: title "Decision Tree", mode tabs `Grow`, `Side by side` (`.seg`), icon buttons `Motion`, `Sound`, `Read`. Opens in Grow with The Double Booking loaded and nothing planted, its story card open on the stage. Stage on the left, panel on the right (`.panel`).

**Guide (top of the panel, both modes).** A step strip of buttons, `1 Goals`, `2 Plant`, `3 Slide time`, `4 Choose` in Grow and `Goals A`, `Goals B`, `Slide time` in Side by side. A step turns into a tick when done (Grow: a goal on; two branches planted; the slider has reached Next month; a branch chosen. Side by side: a Goals A chip on; a Goals B chip on; time moved) and the first step not done is marked current (`aria-current="step"`). Pressing a step moves focus to its control (the first goal chip, the first unplanted option, the slider, or Choose). Under it the hint paragraph (id `hint`), which starts with "Step N of M:" in the compact layout, where the strip itself is hidden to save height. While Graft, Make a call or Choose is active the strip is replaced by a mode bar ("Grafting", "Making a call", "Choosing") with a `Cancel` button.

**Grow (the main mode, explore first).**
- Stage: a hillside backdrop with a painted trunk and mound at the bottom center (art below); branches and leaves are drawn in code. A painted wooden sign on the trunk holds the decision (Content "Setup", short form) and is a button: it opens and closes the story card. Above the trunk, three soft horizontal bands with labels at the left edge: `Right away` (lowest), `Next week`, `Next month` (top). The band at the slider's stop is highlighted and its label is a filled tab; pressing a band label moves the slider there (the labels are pointer shortcuts, out of the Tab order, since the slider has the keys).
- Story card: over the stage, the kid's portrait, "{title} ({name})", the Setup text and two numbered first steps, with a close button. It opens with each dilemma in Grow, closes when the first branch is planted, on its close button or Escape, and the sign brings it back. In the compact layout the dilemma picker sits inside this card. Planted branches fan out from the trunk top and grow up through the bands. Each branch carries one leaf per band it has reached; the leaf holds the consequence text (at least 14 px at 1366x768) and a row of goal marks.
- Branch tip badge: the branch's standing so far, as an icon plus a word plus a tally: `Blooming` (open flower) when ups outnumber downs, `Even` (plain leaf) when they match, `Wilting` (curled brown leaf) when downs outnumber ups, then "3 up, 1 down". Never color alone.
- Panel, top to bottom:
  1. Dilemma picker: four cards, each with the kid's portrait (a small round head crop), the name and the title: `The Double Booking` (Dev), `The Quiz Photo` (Kai), `The Tablet Fund` (Nia), `The New Game` (Theo). The full setup text shows under the picker in the tall wide layout (in the short and compact layouts the story card carries it).
  2. "What matters to {name}?": four goal chips (toggle buttons with icons, `aria-pressed`). Any number may be on. With none on, leaves show no marks and badges read "Pick a goal".
  3. Options: four option cards (full sentences, letters A to D). Tap to plant that branch; tap again (shown as `Planted`, with a small `Pull up` link) to remove it.
  4. Time: a three-stop slider `Right away`, `Next week`, `Next month`, and a `Play` button that steps through the stops (1.2 s each; instant growth when Motion is off, same pacing).
  5. `Choose a branch`: a wide primary button that appears under the slider when the slider reaches Next month (in the short and compact layouts it joins the time row as `Choose`).
  6. Tool row, labelled "Try": `Graft`, `Make a call`, `Who it touches`, then the smaller `Print tree` and `Clear tree`. Under it a closed "Keys" disclosure with the keyboard shortcuts.
- Not-ready buttons stay pressable (`aria-disabled`, faded) and say why in the hint and by voice: Make a call before it is ready says "Plant two branches and turn on a goal, then make your call before next month.", at Next month "Calls are made before next month. Slide back to make one."; Choose before Next month says "Slide time to next month first, then choose a branch."
- `Play` reads `Replay` once the slider is at Next month (it starts again from Right away).
- `Graft`: press it, then tap two planted branches on the stage (or their option cards). If they are the dilemma's graft pair, a new branch grows from between them, marked with a small graft knot and the label "Graft", and its option text appears as a fifth card (letter G) under the options. Any other pair: "Those two don't fit together. Try a different pair." After two misses the hint adds: "Look for two options that could both happen."
- `Make a call` (optional challenge): available when at least two branches are planted and the slider is not yet at Next month. Tap the branch you think will be standing best at Next month; it gets a small flag. When the slider reaches Next month the panel shows "You called it." if your branch is among the best (ties count), or "Surprise: {option letter} is standing best by next month." With no goal on there is no best branch, so the button is off until a goal is on, and if every goal is turned off after the flag the result line reads "Turn on a goal to see which branch stands best." No points, nothing stored.
- `Who it touches`: toggles small name tags on every leaf (Content "who"), so students can see who each consequence lands on.
- `Choose a branch`: at Next month. Tap a branch; the stage dims the others and shows a card with the kid's portrait: "{name} chose: {option}.", a path line ("Your path: goals on: ... Planted: ... Your call: ..."), its three leaves listed in order, and one look-back question on screen (Content "Look back"). Buttons on the card: `Back to the tree`, `Next dilemma`, `Compare goals side by side` (opens Side by side with this tree's goals as Goals A and Goals B empty, focus on the first Goals B chip). Choosing is never graded.
- `Print tree`: prints the current dilemma, goals on, the call and the chosen branch if made, every planted branch with its leaves and marks, black on white.
- `Clear tree`: pulls up every branch, resets the slider to Right away, keeps the goal chips.

**Side by side.** Same choices, different goals.
- Stage: two smaller trees of the current dilemma, left and right, each with all four option branches planted, plus the graft if it was found in Grow this session (otherwise a faint bud labeled "Graft not found yet"). Above each tree a label: `Goals A (left)` and `Goals B (right)`, or `(top)` and `(bottom)` when the stage is tall and the trees stack; the panel headings say the same ("Goals A, left tree").
- Panel: the dilemma picker, two rows of goal chips (`Goals A`, `Goals B`), the shared time slider and `Play`, and a `Swap` button that swaps the two chip sets.
- Side by side opens with both chip sets off. Until each set has at least one goal on, the line reads "Pick at least one goal for Goals A and for Goals B." and nothing about agreeing is said.
- Below the slider a line updates live: "Standing best at {time}: A: {letters}. B: {letters}." When they differ: "Same choices, different goals, different best branch." When they match: "Both goal sets agree here."
- Nothing to win here. It shows that people who care about different things can sensibly choose differently.

## Content
Mark code per leaf: one character per goal, in the dilemma's goal order: `+` helps, `-` hurts, `0` no change. Standing at a time = ups minus downs over the goals that are on, counted across every leaf from Right away up to that time. Bands: R = Right away, W = Next week, M = Next month. Each leaf also has a `short` title (two to five words) that the leaf shows instead of its full text when the leaf is too narrow to fit it; tapping the leaf shows the full text.

### The Double Booking (Dev)
Setup: "Robotics practice and Ana's bowling party are both this Saturday at 2. The robot competition is next month." Sign: "Practice or the party?"
Goals: 1 `Keep my word to the team` (handshake), 2 `Be a good friend to Ana` (heart), 3 `Have fun` (star), 4 `Be ready for the meet` (gear).
- A "Skip practice and go bowling. Don't tell anyone."
  R "Bowling is a blast. At practice, the team waits for you." who: team | `-++0` | short: "Team waits for you"
  W "Coach asks where you were. A teammate had to cover your job." who: Coach, team | `-00-` | short: "Coach asks why"
  M "The arm you never tested jams at the meet." who: team, Dev | `-0--` | short: "Arm jams at meet"
- B "Go to practice. Don't say anything to Ana."
  R "Practice goes well. At the party, Ana keeps looking at the door." who: Dev, Ana | `+--+` | short: "Ana waits at the door"
  W "Ana hears you were just at practice and goes quiet." who: Ana | `0-00` | short: "Ana goes quiet"
  M "The arm works at the meet. Things with Ana still feel a bit off." who: team, Ana | `+-++` | short: "Ana feels off"
- C "Ask Coach if you can leave practice early."
  R "Coach says yes, once the arm is tested. You rush and arrive as the cake comes out." who: Coach, Ana | `+++0` | short: "Here for the cake"
  W "Coach asks you to make up the hour on Tuesday, your free afternoon." who: Coach, Dev | `00-+` | short: "Make-up Tuesday"
  M "The arm mostly works. A test you rushed shows up as a small glitch." who: team | `000-` | short: "A small glitch"
- D "Tell Ana you can't come, and ask to bowl with her Sunday."
  R "Ana is disappointed, but she says Sunday works." who: Ana | `+0-+` | short: "Ana says Sunday"
  W "Sunday bowling, just the two of you. It's a good time." who: Ana, Dev | `0++0` | short: "Fun Sunday"
  M "The arm works at the meet, and Ana comes to cheer." who: team, Ana | `++++` | short: "Ana cheers"
- Graft C + D: G "Text Ana you'll be late, leave practice early, and bowl with her Sunday too."
  R "You test the arm, leave early and catch the end of the party. Ana saved you a slice." who: Coach, Ana | `+++0` | short: "Party's end"
  W "Sunday bowling too, but Tuesday's make-up practice eats your free afternoon." who: Ana, Dev | `0+-+` | short: "Lose free Tuesday"
  M "The arm works, apart from one small glitch. Ana comes to cheer." who: team, Ana | `++0-` | short: "One glitch"
- Look back: "Which consequence did you not see coming when you planted the branches?"

### The Quiz Photo (Kai)
Setup: "At 9 at night, someone posts a photo of tomorrow's math quiz in the class group chat." Sign: "Look or not?"
Goals: 1 `Be honest` (shield), 2 `Do well on the quiz` (paper with a check), 3 `Stay in with the group` (three dots), 4 `Really learn the math` (light bulb).
- A "Open the photo and memorize the answers."
  R "Ten minutes and you know every answer. Easy night." who: Kai | `-0+-` | short: "An easy night"
  W "Ms. Ortiz spots the same wrong answer on twelve quizzes. Everyone retakes a new quiz, you aren't ready, and the group argues about who posted it." who: Ms. Ortiz, class, group | `----` | short: "Everyone retakes it"
  M "The unit test covers the same math, and you never really learned it. The group chat has gone quiet since the retake." who: Kai, group | `0---` | short: "Never learned it"
- B "Don't open it. Study like normal."
  R "You study for an hour while the chat keeps buzzing." who: Kai | `+0-+` | short: "Chat keeps buzzing"
  W "Ms. Ortiz gives a new quiz. You're ready for it." who: Kai, class | `++0+` | short: "Ready for new quiz"
  M "The unit test goes fine." who: Kai | `0+0+` | short: "Unit test fine"
- C "Mute the chat and go to bed early."
  R "No photo, no studying. Lights out at 9:30." who: Kai | `+00-` | short: "Lights out early"
  W "The new quiz catches you unready." who: Kai | `0-0-` | short: "Caught unready"
  M "You're a step behind for the unit test." who: Kai | `0-0-` | short: "Behind for the test"
- D "Tell Ms. Ortiz about the photo."
  R "You send her a short message. A few kids guess it was you." who: Ms. Ortiz, group | `+0-0` | short: "Kids guess it's you"
  W "She swaps in a new quiz. Some friends act cold for a few days." who: group | `+0-0` | short: "Friends act cold"
  M "Things settle down with the group." who: group | `+0+0` | short: "Things settle down"
- Graft B + D: G "Study like normal, and tell Ms. Ortiz without naming anyone."
  R "You study, then message her that a photo of the quiz is going around." who: Kai, Ms. Ortiz | `+00+` | short: "Study, then tell"
  W "The new quiz is harder than the first. You pass, but only just." who: Kai, class | `+-0+` | short: "Pass, only just"
  M "Someone works out who told, and there are a few days of cold shoulders. The unit test goes fine." who: group, Kai | `0+-+` | short: "Cold shoulders, test fine"
- Look back: "Which goal did you turn on first, and did it change which branch looked best?"

### The Tablet Fund (Nia)
Setup: "Nia has saved $80 toward a $150 drawing tablet. This Saturday her friends are going to the county fair, and a day there costs about $35." Sign: "Spend or save?"
Goals: 1 `Get the tablet soon` (tablet), 2 `Have fun with friends` (two circles), 3 `Stick to my saving plan` (calendar), 4 `Have free time` (clock).
- A "Go to the fair and spend the $35."
  R "Rides, fried dough and a photo strip with everyone. Your fund drops to $45." who: Nia, friends | `-+-0` | short: "Fair day, $45 left"
  W "You check the tablet price again. It feels a long way off now." who: Nia | `-0-0` | short: "Tablet feels far"
  M "Still saving. Your friends are already planning the next outing." who: Nia, friends | `-+00` | short: "Friends plan more"
- B "Skip the fair and keep saving."
  R "You stay home. Your friends post fair photos all afternoon." who: Nia, friends | `+-+0` | short: "Fair photos all day"
  W "Your allowance brings the fund to $90." who: Nia | `+0+0` | short: "Fund reaches $90"
  M "The fund reaches $110. The tablet is in sight." who: Nia | `+0+0` | short: "Fund reaches $110"
- C "Go to the fair, but bring only $10."
  R "You skip most rides and share snacks. Fun, even watching from the rail." who: Nia, friends | `0++0` | short: "Cheap fun at fair"
  W "Your allowance brings the fund to $80 again." who: Nia | `00+0` | short: "Back to $80"
  M "The tablet is still a while off." who: Nia | `-000` | short: "Tablet still far off"
- D "Ask a neighbor if you can walk their dog for money."
  R "Mr. Lee says yes, $5 a walk after school. The first walk is Saturday, so you miss the fair." who: Mr. Lee, Nia | `+-0-` | short: "Walks, no fair"
  W "Five walks, $25 more. Your afternoons are short." who: Mr. Lee, Nia | `+00-` | short: "Five walks, $25"
  M "The fund hits $150 and you buy the tablet, but the walks still take every afternoon." who: Nia, Mr. Lee | `+0+-` | short: "Tablet, busy days"
- Graft C + D: G "Go to the fair with $10, and start walking Mr. Lee's dog on Monday."
  R "A fun, cheap day at the fair. Walks start Monday." who: friends, Mr. Lee | `0++0` | short: "A cheap fair day"
  W "The walks earn back more than the fair cost. Your afternoons are short." who: Mr. Lee, Nia | `+00-` | short: "Walks pay it back"
  M "You buy the tablet a little later than you would have with walks alone." who: Nia | `++0-` | short: "Tablet, a bit later"
- Look back: "What did the branch you chose cost Nia, and was it worth it?"

### The New Game (Theo)
Setup: "It's Monday. Theo's science project is due Friday and he hasn't started. The game all his friends are playing came out today." Sign: "Game or project?"
Goals: 1 `Turn in good work` (ribbon), 2 `Play with friends online` (game controller), 3 `Get enough sleep` (moon), 4 `Keep the week calm` (wave).
- A "Play tonight. Start the project Thursday."
  R "A great night of gaming with friends." who: friends | `0+0+` | short: "Gaming night"
  W "Thursday you're up past midnight gluing the poster." who: Theo, family | `-0--` | short: "Up past midnight"
  M "The grade is a C, and your friends are on to a new game." who: Theo | `-000` | short: "A C grade"
- B "Do the whole project tonight. No game."
  R "You stay up late and get most of it done." who: Theo | `+--0` | short: "Up late working"
  W "Done early. You play all weekend." who: Theo, friends | `0+0+` | short: "Done, play all weekend"
  M "A good grade. You're a level behind your friends, but you catch up." who: Theo, friends | `+000` | short: "Good grade, behind"
- C "Plan it: one part each night, then play."
  R "Thirty minutes on the project, then an hour of the game." who: Theo, friends | `++00` | short: "Project, then game"
  W "Wednesday the glue runs out. You skip the game to get more." who: Theo | `0-00` | short: "Glue runs out"
  M "A good grade, and you kept up with the game." who: Theo, friends | `++0+` | short: "Good grade, kept up"
- D "Ask a classmate to be your project partner."
  R "Jun says yes, if you do the poster." who: Jun | `+000` | short: "Jun says yes"
  W "Jun does his part on time. You do yours late." who: Jun, Theo | `00-0` | short: "Yours is late"
  M "A decent grade, and a new friend to play with." who: Jun, Theo | `++00` | short: "A new friend"
- Graft C + D: G "Partner with Jun and split the nights: project first, then play together."
  R "You and Jun plan it on a call, then play together." who: Jun, friends | `++0+` | short: "Plan, then play"
  W "Jun is sick two nights. You cover his part and stay up late." who: Jun, Theo | `+---` | short: "Jun is sick"
  M "A good grade, and gaming with Jun becomes a thing." who: Jun, Theo | `++00` | short: "Gaming with Jun"
- Look back: "Which branch looked best right away? Was it still best by next month?"

Worked check (all four goals on, standing at R / W / M; computed in Python from the codes above):
- Double Booking: A 1/-1/-4, B 0/-1/1, C 3/3/2, D 1/3/7, G 3/4/5. Best right away C and G; best at next month D.
- Quiz Photo: A -1/-5/-8, B 1/4/6, C 0/-2/-4, D 0/0/2, G 2/3/4. Best right away G; best at next month B.
- Tablet Fund: A -1/-3/-3, B 1/3/5, C 2/3/2, D -1/-1/0, G 2/2/3. Best right away C and G; best at next month B.
- New Game: A 2/-1/-2, B -1/1/2, C 2/1/4, D 1/0/2, G 3/1/3. Best right away G; best at next month C.
So in every dilemma the right-away leader is not the next-month leader with all goals on, and the graft wins only sometimes. Do not "fix" the codes so a graft always wins.
- Checked over all 15 non-empty goal sets in every dilemma: in The Quiz Photo, option A (memorize the answers) is never best or tied for best at Next month under any goal set (its best case, "Stay in with the group" alone, ends at -1 while C ends at 0). Keep it that way if any code changes.

## Interactions in detail
- Planting: a branch grows from the trunk in 500 ms (instant with Motion off) and shows leaves for every band up to the slider's current stop. Moving the slider back hides the higher leaves (they shrink to buds) and recomputes badges.
- Up to five branches (four options plus the graft). Layout spreads planted branches evenly in a fan; branch order is A, B, C, D left to right, and the graft grows between its two parents (between C and D for C + D grafts; between B and C for the Quiz Photo's B + D graft, with its knot linked to both). The stage is laid out at real pixel size per box (STANDARDS.md "Sizes"); at narrow sizes leaf text collapses to its short title (Content `short`) and tapping a leaf shows its full text (in the panel in the tall wide layout; as a card over the stage in the short, compact and stacked layouts, so it stays next to the tree).
- Goal marks: on each leaf, one small icon per goal that is on, with an up arrow (helps), down arrow (hurts) or flat dash (no change), plus the word in the accessible name ("Have fun: helps"). Toggling a chip updates every mark and badge at once with a 300 ms fade (instant with Motion off).
- Tapping a leaf puts its full text, who it touches and its marks for all four goals in the panel.
- Pulling up a parent branch also pulls up its graft. Changing dilemma clears the tree, resets the slider and turns all goal chips off, and calls `Curio.stop()`. A found graft is remembered for the session (for Side by side) but not stored.
- Graft mode: while active, the Graft button reads `Cancel graft` (`Cancel` in compact), the mode bar shows "Grafting" with `Cancel`, planted branches get a dashed outline, and Escape cancels. Grafting needs both parents planted; if fewer than two are planted the hint says "Plant at least two branches first."
- Make a call: one flag at a time; tapping another branch moves it. Moving the slider back below Next month clears the result line but keeps the flag.
- Ties: badges and the "standing best" lines list every tied letter.
- Keyboard: 1 to 4 plant or pull up A to D, 5 plants or pulls up G once found, G toggles Graft, left and right arrows move the slider, P is Play, W toggles Who it touches. Escape closes, in order: the choose card (focus back to Choose), an active mode (focus to its button when it was in the mode bar), the story card (focus to the sign), the leaf details. All controls reachable by Tab with visible focus; Tab order is header, step strip, picker, chips, options, time, tools, Keys, then the stage (sign, story card). Option cards and chips at least 44 px tall.
- Projector use: the letters A to D and G are large on the branch tips so a class can call them out.
- Nothing is stored except the kit's Motion setting.

## Look
6-8 band sets its own `:root` (no band theme file). An outdoor orchard look, different from the batch siblings (mustard #8a5a10, violet #5a2fb8, burnt orange #b3471d) and the K-2 SEL neighbors (green #2f7a62, teal #26627a, magenta #b0407a).
- `--paper #f6f8ee` (pale sage), `--ink #1f2a1a`, `--muted #5a6352`, `--line #dfe5cf`, `--brand #4a6417` (moss olive), `--panel #ffffff`, `--focus #a3306e` (outline only, 3 px).
- Scene: sky band `#dfeef2`, bark `#74503a` (letter circles, sampled from the painted trunk's shadow side), wood `#93664a` (branch strokes, the trunk's mid tone, with a 0.8 px darker edge), leaf fill `#cfe6b8`, bloom fill `#f7d3e2`, wilt fill `#ecd9bf`; badge chips: Blooming `#b8336a`, Even `#2f6e34`, Wilting `#8a5a2b`, each with white text and its own icon.
- Contrast (computed): white on brand 6.72:1; brand on paper 6.26:1; ink on paper 13.94:1; muted on paper 5.86:1; focus ring on paper 6.11:1; ink on sky 12.57:1; ink on leaf fill 11.15:1, on bloom fill 10.94:1, on wilt fill 10.85:1; white on Blooming 5.65:1, on Even 6.17:1, on Wilting 5.87:1, on bark 7.12:1; sign words `#2e1c0e` on the plank under its 45% light wash at least 7:1. All pass AA for normal text.
- No confetti. "You called it" gets one soft chime (`Curio.yes()`).

## Art
- bg-hillside: "a gentle grassy hill under a wide pale blue sky, rolling green fields fading into soft hills, a few small white clouds, late morning light, soft painted illustration"; 16:9; cutout no; people no; full-frame backdrop behind the tree in both modes, under a 28% paper overlay so leaves read. Local FLUX. If it fails, a flat sky band and a drawn green hill.
- Portraits kid-dev, kid-kai, kid-nia, kid-theo: head-and-shoulders, about twelve, facing forward, friendly, plain clothes with no text; OpenAI gpt-image, edited for Curio Class (prompts in `art/prompts.json`). Dev and Kai have no pronouns in the content and are drawn with a relaxed, gender-neutral look; Nia is "her", Theo is "he". Shown in the picker (round head crop), the story card and the choose card, always beside the name (`alt=""`). Not on the stage in Side by side, not in print.
- tree-base (trunk and mound, under the branches), sign-plank (the sign button, stretched by its ends), tip-bloom, tip-even, tip-wilt (a small sprig on the shoulder of each branch letter, matching its badge; Even and "Pick a goal" use tip-even) and graft-knot (at the graft's join): FLUX.2 [klein] on Cloudflare Workers AI, cut out and edited for Curio Class. The badge chips keep the word and icon, so the state is never shown by a painting alone.
- Everything else (branches, leaves, bands, buds, goal icons, preview.svg) is drawn in code. Each painting is named once in an `ART` map in src.html (the bundler inlines a copy per name).

## Voice
Bank voice `casual-peer` (Zubenelgenubi): "Say casually and naturally, like a friendly teenager explaining something." Not used by any sibling (walk-in-their-shoes gentle-storyteller, comeback-club upbeat-guide, conflict-coach big-sister). Leaf texts and option cards are on screen only. Fixed lines:
- Welcome, Grow: "Plant a few options, pick what matters, then slide time forward and watch what grows."
- Welcome, Side by side: "Same choices, two sets of goals. Watch where they agree and where they don't."
- Setup, one per dilemma: the four Setup texts in Content.
- Hint, no goals on (shown first, matching step 1): "Turn on at least one goal so the leaves can show what helps and what hurts."
- Hint, goals on, nothing planted: "Tap an option to plant it as a branch."
- Hint, ready to slide: "Now slide time forward. The best branch right away isn't always the best one later."
- Hint, graft: "Tap two branches that could both happen at once."
- Hint, graft miss: "Those two don't fit together. Try a different pair."
- Hint, graft found: "Nice graft. Two options together made a new one."
- Hint, after two graft misses: "Look for two options that could both happen."
- Hint, make a call: "Pick the branch you think will be standing best by next month."
- Called it: "You called it."
- Surprise: "Surprise. A different branch is standing best by next month." For a tie between other branches: "Surprise. Other branches are standing best by next month."
- Make a call with no goal on: "Turn on a goal to see which branch stands best."
- Hint, at Next month: "That's next month. Choose the branch you'd go with."
- Make a call, not ready yet: "Plant two branches and turn on a goal, then make your call before next month."
- Make a call, at Next month: "Calls are made before next month. Slide back to make one."
- Choose, before Next month: "Slide time to next month first, then choose a branch."
- Hint, choose: "Pick the branch you'd choose. There's no wrong pick here."
- The four Look back questions in Content.
- Side by side, a set with no goals: "Pick at least one goal for Goals A and for Goals B."
- Side by side agree: "Both goal sets agree here." Differ: "Same choices, different goals, different best branch."
Voice behavior follows STANDARDS.md (collision-lab pattern).

## Family engine
none

## Sources
- CASEL, "What Is the CASEL Framework?", Responsible Decision-Making competence and its listed examples (identifying solutions for personal and social problems; anticipating and evaluating the consequences of one's actions; reflecting on one's role): https://casel.org/fundamentals-of-sel/what-is-the-casel-framework/ (builder: check the wording before quoting it in notes.md)
- The tree itself is a teaching picture, not a claim: the tool states no research finding or number about decision-making, so nothing else on screen needs a source. If notes.md mentions decision trees as a planning tool, the builder cites a named source there.
- All dilemmas, characters, consequences and goal codes are original fictional content written for Curio Class; the worked standings in Content were computed from those codes.
- Wording rule: the tool says "often" and "isn't always", never that a choice is right or wrong.

## Done when
1. In each of the four dilemmas, planting A to D grows four branches with one leaf per band up to the slider stop, and every leaf's text, who tags and marks match Content.
2. With all four goals on and every branch planted (graft found), the standings at Right away, Next week and Next month match the worked check in Content, including ties. Turning on any single goal or any mix of goals in The Quiz Photo never puts A (memorize the answers) best or tied for best at Next month.
3. Toggling any goal chip updates every mark and badge immediately; with no goals on, badges read "Pick a goal".
4. Graft works only for the dilemma's pair (Double Booking C+D, Quiz Photo B+D, Tablet Fund C+D, New Game C+D); any other pair shows the miss line, and pulling up a parent removes the graft.
5. Make a call reports "You called it." or the Surprise line correctly at Next month, counting ties as called.
6. Side by side shows two trees, the graft only if found in Grow this session, and the "Standing best" line changes with each chip set; `Swap` swaps them.
7. Choose a branch shows the chosen option, the path line, its three leaves and the dilemma's Look back question, with no grade; `Compare goals side by side` carries the goals into Goals A.
11. The step strip ticks each step as it is done and its buttons move focus to the right control; the mode bar's `Cancel` and Escape leave Graft, Make a call and Choose; pressing a not-ready Make a call or Choose says why.
8. There is no text input anywhere; localStorage holds only the kit Motion key. Print tree prints cleanly in black and white.
9. Option cards, goal chips and the time slider are visible without scrolling at 1366x768, 1280x720 and 800x500; leaf text is readable in the 680x425 preview; the tool works at 760 and 375 wide.
10. Keys 1 to 5, G, arrows, P and W work; welcomes play once per mode, Read speaks the current hint, and mode or dilemma changes stop speech.
