# Pressure Point

## One idea
In every pressure moment you can tap any kid in the scene to hear what they are really thinking, and most of them don't want to either: the pressure comes from one voice, and once you answer with a refusal move, the room's thoughts change and someone else says no too.

## Not like
- decision-tree (6-8 SEL, builder): grows one decision's branches over time against goals. Here there is no tree and no time slider: it is the moment itself, a room of other kids, and the words you use to say no.
- conflict-coach (6-8 SEL, roleplay): rewinds an argument to swap a blaming line for an I-statement. Here nobody is arguing: someone offers a vape or a drink, you pick a refusal move, and the hidden thoughts of the bystanders are the reveal.
- captain-s-choices (9-12 PE, story): season-long choices move team culture dials. Pressure Point is four short scenes, each finished in about three minutes, with no dials or scores.
- stress-toolkit (6-8 health, group sibling): coping tools you try on yourself. relationship-spectrum (group sibling): placing behaviors on a healthy-to-abusive line. screen-time-detective (group sibling): a data desk. None of them is a branching story.
- safety-street (K-2 health, story): a walk with safety choices for young children. Pressure Point is middle school social pressure with a reveal mechanic, not right and wrong choices.
- mind-map (9-12 feelings): mentions vaping only as a stress habit. Here vaping and alcohol are the subject.

## Who and how
- Grade 6-8, Health, module Substance Use Prevention (effects of tobacco, vaping, alcohol and drugs; refusal skills).
- Driver: students on laptops, alone or in pairs (pairs read the character lines out loud). A teacher can project one scene for a class vote on the card.
- Minutes: 15-30 (one scene is about 3 minutes).
- Standards: NHES.S1 (health concepts: effects of nicotine and alcohol), NHES.S4 (interpersonal communication: refusal skills), NHES.S5 (decision making); also CASEL.Relationship Skills (resisting negative social pressure), CASEL.Social Awareness (What's normal? and bystander thoughts read real social norms).
- Topic line: "peer pressure and refusal skills: vaping and alcohol".
- Modes (tool.json): ["Scenes", "What's normal?", "Your moves"].

## Screens and modes
Header: title "Pressure Point" with the topic line under it, mode buttons **Scenes**, **What's normal?**, **Your moves**, then **Teacher**, **Motion**, **Sound**, **Read**. Stage left, panel right (stacks under 1000 px wide; in short landscape boxes the panel stays beside the stage, compact). A calm footer line in every mode: "Worried about vaping or drinking, yours or a friend's? Talk to an adult you trust, like a parent, the school nurse or the school counselor."

### Scenes (opens first)
- Focus: in the picker, the four covers; inside a scene, the offer panel with the kids in it (the biggest panel on the stage while the student decides), then the after panel.
- Scene picker on the stage: four comic cover panels in a 2 by 2 grid, each a crop of its scene's painting (The group chat uses `pp-phone-desk`) with its title, a one-line teaser and a small icon (vape outline or can outline, drawn in code): **After the game**, **The sleepover**, **The group chat**, **The favor**. A finished scene shows "Played" and stays playable.
- Inside a scene the stage is a comic strip of up to four panels that fill in left to right (on narrow stages, one panel at a time with **Back** and **Next** under it):
  1. Setup panel: the scene painting with the painted cast cutouts standing in it, and a caption box (narrated).
  2. Offer panel: the pressure line in a speech bubble from the person offering, who holds the painted vape or cans (a separate cutout laid at the hand in code).
  3. Your answer panel: your move in a speech bubble (you are never drawn: your bubble comes from the panel edge, labeled "You").
  4. After panel: the reply, the room's new thoughts, and who joins you.
- Panel during the offer: hint; **Look around** (lights a small thought-bubble button over every other kid, and over the person offering); the hand of move cards; **Say nothing**.
- Tapping a kid's thought button opens their thought bubble (a cloud with dotted tail, cream fill) in the offer panel. Every kid can be opened, in any order; opening is optional.
- Round 1 cards: **No thanks**, **Give a reason**, **Suggest something else**, **Make a joke**, **Leave**. Round 2 (after the push) cards: **Say it again**, **Give a reason**, **Suggest something else**, **Leave**. A card shows its label and, under it, the exact line you will say in this scene.
- After the ending: the debrief card in the panel: **What worked here**, the scene's fact card (with its source line), and **If it happens for real**. Buttons: **Replay this scene**, **Pick another scene**.

### What's normal?
- Focus: the 100-figure grid, filling the stage.
- Stage: a grid of 100 small kid figures (10 by 10, drawn in code: this is an icon chart) and a question above it.
- Panel: the question, a slider "Your guess: 0 to 100" (steps of 1, arrow keys move it), **Show the real number**, then **Next question** (4 questions, Content).
- Moving the slider outlines that many figures in a dashed ring. Show the real number fills the real count in the accent color with a solid dot inside each (the last figure filled in proportion to the decimal, from the bottom up: half a figure for 3.5 and 89.5, six tenths for 9.6, nine tenths for 12.9), keeps the dashed ring on your guess, and prints the number, the group, the year and the source. Nothing is scored.

### Your moves
- Focus: the hand of cards; the typed line's bubble when it is shown.
- Stage: the six move cards laid out as a hand (Content), each one flips on tap to show what it is, an example and when it fits.
- Panel: hint, then **Write your own line**: pick a scene from a short list, type your own refusal line (up to 120 characters), tap **Put it in the bubble** to see it drawn in a speech bubble in that scene's offer panel. A note under it: "Not saved. It clears when you leave this mode." **Clear**.

### Teacher
A small dialog: checkboxes for the four scenes (all on by default) with "Unticked scenes are hidden from the picker on this device." and **Done**. Remembered in localStorage `curio-pressure-point-scenes` (a classroom setting, not student data), wrapped in try/catch. At least one scene must stay ticked (the last checkbox disables).

## Content

### The six moves (Your moves cards; NHES.S4 refusal skills)
| Move | What it is | Example | When it fits |
|---|---|---|---|
| No thanks | A short, clear no. You don't owe a reason. | "No thanks, not my thing." | Always. Short is strong. |
| Give a reason | A true reason that is yours. | "No, I've got tryouts Monday." | When a reason makes it easier for you. |
| Suggest something else | Offer a plan that gives everyone something to say yes to. | "Let's get nachos instead." | In a group that is bored or wants to hang out. |
| Make a joke | Keep it light and still say no. | "Pass. I like my brain the way it is." | When the mood is friendly. |
| Say it again | Repeat your no, same words, calm. You don't need a new reason. | "No. I'm good." | When they push. |
| Leave | Walk away, wait somewhere else, or text family a code word that means "come get me." | "I'm going to wait by the doors." | Any time you feel stuck. Leaving is always allowed. |
Under the hand, always: "A family code word is a plan you make ahead of time: you text one word, and your family calls to get you out, no questions in front of friends." (SAMHSA, Talk. They Hear You.)

### Cast (painted waist-up cutouts, two expressions each, Art; the chat members are code avatars)
Dre (8th grade, offers), Maya, Leo, Kai; Priya (host, offers), Jules, Ana; Zoe (offers), Marcus, Ellie, Ben (chat avatars: initials in colored circles); Tomas (best friend, asks the favor). Each painted kid has a "before" picture (shown through the offer) and an "after" picture (shown in the after panel): Dre grin / neutral shrug; Maya unsure / relieved; Leo neutral / relieved; Kai unsure / relieved; Priya grin / relieved; Jules unsure / relieved; Ana unsure / relieved; Tomas worried / relieved. Skin tones and hair styles vary across the cast; no one is shown using a product.

### Scene 1: After the game (vape). Art `pp-bleachers`.
- Setup (narrated): "Friday night. The game is over, and you're on the bleachers waiting for rides." / "Dre pulls something out of his hoodie pocket."
- Offer, Dre: "It's mango. Everybody's tried it. Here."
- Thoughts before: Maya: "I don't want to. But I don't want to look like a baby." Leo: "My mom's here in ten minutes. She'd smell it." Kai: "I tried it once and felt sick. Please don't pass it to me." Dre: "If everyone says no, this gets kind of awkward for me."
- Your lines: No thanks: "No thanks, not my thing." Give a reason: "No, I've got tryouts Monday. I need my lungs." Something else: "Nah. Anyone want nachos before the stand closes?" Joke: "Pass. I like my brain the way it is." Leave: "I'm going to wait for my ride by the doors." Say it again: "No. I'm good."
- Round 1 reply by move: No thanks: "Seriously? It's not a big deal." Reason: "One hit won't do anything." Something else: "After. Try it first." Joke: Dre laughs. "Okay, okay. You sure?" Say nothing: "Come on. Just once."
- Push (round 2 opens): Dre: "Everybody else is going to." (Maya's and Kai's thoughts flash: "No, I'm not.")
- Ending: Dre shrugs and puts it away: "Whatever." Maya: "Yeah, I'm good too." Leo: "Nachos?" Leave ending: Leo: "Wait up, I'll come." Maya follows.
- Thoughts after: Maya: "That was easier once someone said it first." Kai: "Phew." Dre: "Guess nobody wanted it."
- What worked here: "Saying no first, plainly, gave Maya and Kai room to say no too. A reason or a plan helps, but you never owe one."
- Fact card: "Most e-cigarettes contain nicotine, which is highly addictive. Nicotine can harm the parts of a teen's brain that control attention, learning, mood and impulse control. The brain keeps developing until about age 25." Source: CDC.

### Scene 2: The sleepover (alcohol). Art `pp-basement`.
- Setup: "Saturday night at Priya's. Her parents are asleep upstairs." / "Priya comes back from the garage with two cans of hard seltzer."
- Offer, Priya: "My parents won't notice two missing. Let's try it."
- Thoughts before: Jules: "If my parents found out, I'd lose my phone for a month." Ana: "I'm kind of curious. But not like this." Priya: "I just don't want tonight to be boring."
- Your lines: No thanks: "No thanks, I'm not drinking." Reason: "No. My parents trust me to stay over here." Something else: "Let's do face masks and the scary movie instead." Joke: "I'll pass. I'm already this much fun." Leave: you text your family code word; "My mom's coming to get me." Say it again: "No. I'm not drinking."
- Round 1 reply: No thanks: "Come on, it's barely anything." Reason: "They'll never know." Something else: "We can do both..." Joke: Priya laughs. "Fine. But you're missing out." Say nothing: "Okay, I'll open one and we can share."
- Push: Priya: "You guys are making this weird. It's just one."
- Ending: Priya: "Okay, fine. I'll put them back." Jules: "Movie?" Leave ending: your mom calls; Priya puts the cans back: "Wait, don't go. We'll just do the movie." You can stay.
- Thoughts after: Ana: "Honestly? I'm glad." Priya: "That's a relief. I was nervous about my dad."
- What worked here: "Plan B gave everyone something to say yes to. A family code word is a way out that doesn't need an argument."
- Fact card: "Teens who drink are more likely to miss school, get lower grades and get hurt, and drinking can slow brain development, which may cause problems with memory." Source: CDC.

### Scene 3: The group chat (vape). Cover art `pp-phone-desk`; inside, a phone drawn in code fills the panel (a screen of messages).
- Setup: "Tuesday, after dinner. Your group chat lights up."
- Messages: Zoe: "park after school tmrw? my cousin left his vape at my house lol" Marcus: "im in" Zoe: "@you you coming? don't be lame"
- Thoughts before: instead of bubbles, each member shows "typed, then deleted": Ellie: "i don't really want to" Ben: "is that even safe" Marcus: "i only said yes bc zoe did".
- Your lines (sent as messages): No thanks: "nah im good". Reason: "cant, not my thing and i have practice". Something else: "park yes, vape no. someone bring a ball?" Joke: "pass, my lungs have a big future". Leave: you tap Mute chat; the chat goes quiet for the scene and the ending runs. Say it again: "still no. im good".
- Round 1 reply: Zoe: "boring" (No thanks), "ok but just come" (Reason), "we can do both" (Something else), "lol ok" (Joke), "hello??" (Say nothing).
- Push: Marcus: "everyone's gonna be there".
- Ending: Ellie: "same, ill come for basketball tho" Ben: "same" Zoe: "fine. ball it is". Leave ending: when you unmute, Ellie had posted "im not doing the vape thing either" and Ben "same".
- Thoughts after (typed, then deleted): Ellie: "glad someone said it".
- What worked here: "Online pressure can feel louder because everyone can see it. Short, clear messages work, and you can mute or leave a chat."
- Fact card: "In 2024, about 3.5 out of every 100 middle school students had used an e-cigarette in the past 30 days. 'Everyone's doing it' isn't true." Source: CDC, National Youth Tobacco Survey 2024.

### Scene 4: The favor (vape). Art `pp-hallway`.
- Setup: "Monday morning, by the lockers." / "Tomas, your best friend since third grade, looks around and lowers his voice."
- Offer, Tomas: "My mom checks my bag now. Can you keep this in your backpack till Friday? Please. You're my best friend."
- Thoughts before (Tomas only): "I hate that I need it. I tried to stop last week."
- Your lines: No thanks: "No. I can't hold it." Reason: "If a teacher finds it in my bag, I'm the one in trouble." Something else: "I won't hold it. But I'll go with you to talk to the nurse about quitting." Joke: "My backpack has rules. No vapes, no old bananas." Leave: "I've got to get to class. Talk at lunch?" Say it again: "I'm not holding it. I'm still your friend."
- Round 1 reply: No thanks: "Wow. I thought you had my back." Reason: "Nobody's going to check your bag." Something else: "...You think they'd help? I'd get in trouble." Joke: Tomas half smiles. "I'm serious though." Say nothing: "Please. Just this once."
- Push: Tomas: "You're the only one I trust."
- Ending: Tomas sighs. "Okay. Maybe I'll talk to the nurse. Will you come?" You: "Yeah. I'll come." Leave ending: at lunch Tomas sits with you: "Sorry about this morning. Maybe I'll talk to the nurse. Will you come?"
- What worked here: "You can say no to the favor and yes to the friend. Going with them to a trusted adult is having their back."
- Fact card: "In 2020, about 64 out of 100 students who used e-cigarettes wanted to quit. Nicotine is highly addictive, so quitting can be hard, and help makes it easier." Source: CDC.

### If it happens for real (every debrief, same text)
"Any move is fine. Leaving is always allowed. If you or a friend is using and wants to stop, a parent, the school nurse or the school counselor can help."

### What's normal? questions (on screen with group, year and source)
1. "Out of 100 middle school students, how many used an e-cigarette in the past 30 days?" Real: 3.5 (2024; CDC National Youth Tobacco Survey).
2. "Out of 100 eighth graders, how many vaped nicotine in the past year?" Real: 9.6 (2024; NIDA Monitoring the Future).
3. "Out of 100 eighth graders, how many drank alcohol in the past year?" Real: 12.9 (2024; NIDA Monitoring the Future).
4. "Out of 100 eighth graders, how many used no alcohol, nicotine or marijuana in the past 30 days?" Real: 89.5 (2024; NIDA Monitoring the Future).
After each reveal: "Compare your guess with the real number. When 'everyone does it' feels true, the pressure feels bigger than it is."

## Interactions in detail
- Round flow: offer, round 1 card (or Say nothing), the reply for that move, the push, round 2 card, ending. Leave in either round skips straight to the Leave ending. Say nothing in round 1 gives its reply, then the push. Say nothing is not offered in round 2: round 2 always ends with a refusal (every path ends with you not using; there is no path where your character vapes or drinks).
- Thoughts: before your round 1 card, kids show their "before" thoughts; after the ending, the same buttons show "after" thoughts, and a small sparkle (static with Motion off) marks the ones that changed. A kid who joins you gets a speech bubble in the ending panel.
- Look around is optional; if the student picks a card without opening any thoughts, the ending panel shows **What were they thinking?**, which opens all the before and after thoughts side by side.
- Replay resets the scene to the setup panel. Switching modes keeps the scene picker's Played marks for the page session only (not saved).
- Keyboard: Tab reaches thought buttons, then cards, in reading order; Enter picks. Number keys 1 to 5 pick round 1 cards.
- Teacher scene settings hide scenes from the picker only; the What's normal? questions always show.
- Narrow and short boxes: comic panels shrink to one at a time with Back and Next; the hand of cards scrolls inside the panel; cards are 44 px or taller.

## Look
- Accent `--brand` #a3263f (deep berry: comic ink red, used for headers, cards and the real-number fill), on a warm light `:root`: paper #fbf6f1, ink #2a1a1f, muted #6b5459, line #ead8d0, focus #2f5bd3, panel #ffffff. Comic panels: thick ink borders #1d1820 with white gutters; thought clouds cream #fff6d6 with a dotted tail; caption boxes #ffd166 with ink text.
- Contrast: accent on white 7.23:1, on paper 6.73:1; white text on accent 7.23:1; ink on paper 15.45:1; muted on paper 6.44:1; ink on thought cream 15.33:1; ink on caption yellow 11.5:1; accent on caption yellow 5.01:1.
- Different from group siblings (stress-toolkit moss #4f6b2c, relationship-spectrum teal #0f6e8c, screen-time-detective blue #1f5fbf) and 6-8 neighbors (rules-referee gold, goal-tracker indigo, conflict-coach burnt orange, decision-tree ochre). Never color alone: thoughts that changed carry a sparkle and the word "Now:".

## Art
22 images, 16 with people. One style for all: "flat painted comic style with bold shapes"; cutouts add "plain white background".

Scene paintings (local FLUX, `scripts/localart.py`; no people; 16:9; cutout no). The lower half of each is kept open for the cast cutouts.
- pp-bleachers: "An empty school gym after a basketball game at night, wooden bleachers in the foreground, a dark blank scoreboard, warm overhead lights, a few water bottles on the bench, flat painted comic style with bold shapes"; people no; Scene 1 panels and cover.
- pp-basement: "A cozy family basement at night, a big couch with blankets and pillows, string lights, a snack bowl, a blank dark TV, flat painted comic style with bold shapes"; people no; Scene 2 panels and cover.
- pp-hallway: "A middle school hallway in morning light, rows of plain mustard-yellow lockers with blank doors, a bulletin board with blank colored paper, flat painted comic style with bold shapes"; people no; Scene 4 panels and cover.
- pp-phone-desk: "A smartphone lying face up on a bedroom desk at night, its blank screen glowing, a desk lamp and a stack of schoolbooks, flat painted comic style with bold shapes"; people no; The group chat cover only (inside the scene the phone screen is code).

Props (local FLUX; cutouts; no people):
- pp-vape: "A small plain gray rounded rectangular vape device with a blank surface, flat painted comic style with bold shapes, plain white background"; 1:1; cutout yes; people no; in Dre's hand in Scene 1, and Tomas's in Scene 4 (laid at the hand in code, hidden when it is put away).
- pp-cans: "Two plain blank silver drink cans side by side, flat painted comic style with bold shapes, plain white background"; 1:1; cutout yes; people no; in Priya's hands in Scene 2, gone in the ending.

The cast (kit of parts: 8 kids, 2 pictures each, 16 cutouts; people: true, so Gemini via `scripts/art.py`, which is set aside for now: all 16 wait on Cory and need his review). Shared prompt: "A middle school kid, waist-up, three-quarter view, {look}, {expression}, flat painted comic style with bold shapes, plain white background"; 3:4; cutout yes; people yes. Names `pp-<name>-before` and `pp-<name>-after`. Sizing rule: every kid is scaled to the same head size and stands on the panel's lower edge; the offering kid stands in front, nearest the center.
- Dre: tall, dark brown skin, short twists, a gray hoodie; before: a confident grin; after: a neutral shrug.
- Maya: light brown skin, a long black ponytail, a team jacket; before: unsure, glancing sideways; after: a relieved smile.
- Leo: light skin, messy red hair, a green t-shirt; before: neutral; after: a relieved grin.
- Kai: East Asian, short black hair, a blue windbreaker; before: unsure, arms crossed; after: relieved.
- Priya: South Asian, long dark hair, a pajama shirt with stars; before: an excited grin; after: a relieved smile.
- Jules: light skin, short curly brown hair, an oversized sweatshirt; before: unsure; after: relieved.
- Ana: Latina, wavy dark hair with a headband, a pajama top; before: unsure, curious; after: a relieved smile.
- Tomas: light brown skin, short dark hair, a plaid shirt and a backpack strap on one shoulder; before: worried; after: relieved, a small hopeful smile.
No kid is painted holding a product: the vape and cans are separate cutouts the builder lays at the hand and removes in the ending.

Drawn in code: the comic frames, bubbles, thought clouds, caption boxes, the group chat phone screen and its avatars, the 100-figure grid (an icon chart), the move cards, cover icons and preview.svg.

## Voice
`smooth-narrator` (Algieba): "Say smoothly and warmly, like an audiobook narrator." A story voice that reads captions, not a lecturer. Different from conflict-coach (big-sister), decision-tree (casual-peer), goal-tracker (easy-coach), relationship-spectrum (wise-mentor), rules-referee (firm-captain), captain-s-choices (wise-mentor) and the group siblings. Character dialogue is on screen only (pairs read it aloud). `Curio.voice`, scope mode plus scene plus panel.
| Key | Kind | When it plays | Line | Stale when |
|---|---|---|---|---|
| wScenes | how | entering Scenes, first time | Tap a scene to start. Then read what happens, and tap a card to answer. | a scene tapped; mode left |
| wNormal | how | entering What's normal?, first time | Drag the slider to make your guess. Then tap Show the real number. | Show the real number tapped; mode left |
| wMoves | how | entering Your moves, first time | Tap a card to flip it. Or write your own line in the panel. | a card flipped or the line box used; mode left |
| look | how | the first offer panel of the load, after its setup lines | Tap Look around, then tap any kid to see what they're thinking. Or tap a card to answer. | offer panel left |
| push | how | the first push of the load | They pushed again. Tap a card to answer. You can say the same thing twice. | round 2 left |
| setup.* | event | each time its setup panel opens | each scene's setup captions (7 lines, Content) | another panel or scene showing |
| worked.* | event | each debrief | each scene's What worked here (4 lines) | debrief closed |
| real | event | each Show the real number | The real number: {n} out of 100. | another question showing |
After their first time, look and push only update the hint. Fact cards, thoughts and dialogue are read on screen; Read speaks the hint or the open debrief card.

## Family engine
none

## Sources
- CDC, About E-cigarettes and youth: "Most e-cigarettes contain nicotine, which is highly addictive"; nicotine can harm the parts of the brain that control attention, learning, mood and impulse control; 63.9% of students who currently used e-cigarettes wanted to quit (2020); 5.9% of middle and high school students used in 2024. https://www.cdc.gov/tobacco/e-cigarettes/youth.html
- CDC, Health effects of vaping: brain development "continues until about age 25". https://www.cdc.gov/tobacco/e-cigarettes/health-effects.html
- CDC MMWR, Tobacco Product Use Among Middle and High School Students, National Youth Tobacco Survey 2024: middle school current e-cigarette use 3.5%. https://www.cdc.gov/mmwr/volumes/73/wr/mm7341a2.htm
- NIDA, Reported use of most drugs among adolescents remained low in 2024 (Monitoring the Future, Dec 2024): 8th grade past-year alcohol 12.9%, past-year nicotine vaping 9.6%, past-30-day abstinence from marijuana, alcohol and nicotine 89.5%. https://nida.nih.gov/news-events/news-releases/2024/12/reported-use-of-most-drugs-among-adolescents-remained-low-in-2024
- CDC, About Underage Drinking: more school absences, lower grades, injuries, slower brain development that may cause problems with memory. https://www.cdc.gov/alcohol/underage-drinking/index.html
- SAMHSA, Talk. They Hear You. campaign: exit plans and a family code word teens can text to leave a situation. https://www.samhsa.gov/talk-they-hear-you (builder: check the wording on the campaign's parent tips page and quote it in the credit comment)
- National Health Education Standards (SHAPE America), Standards 1, 4 and 5: refusal skills under Standard 4.
- Art: scene paintings and props are original, made for this tool with local FLUX; the cast is original Gemini art reviewed by Cory (Art).
- Checks run (Python, 2026-10-29): contrast recomputed with the WCAG 2.1 formula; ink on thought cream is 15.33:1 (the spec said 16.12) and ink on caption yellow 11.5:1 (said 12.1), both fixed in Look and both far above 4.5; every other ratio matches to rounding. What's normal? fills: 3.5 is 3 whole figures and half of the 4th, 9.6 is 9 and six tenths, 12.9 is 12 and nine tenths, 89.5 is 89 and a half; the old rule only covered .5, so the fill rule now covers any tenth. 63.9 percent rounds to "about 64 out of 100" (Scene 4 fact card). Setup captions counted: 2 + 2 + 1 + 2 = 7.

## Done when
1. All four scenes play start to finish by every card path, including Say nothing then Leave; no path shows your character using, and every path ends on the debrief.
2. In Scene 1, opening Maya and Kai before answering shows the "before" thoughts; after the ending both show changed "after" thoughts with the sparkle and "Now:".
3. Round 2 never offers Say nothing; Leave in round 1 skips the push.
4. What's normal? reveals 3.5, 9.6, 12.9 and 89.5 with the last figure filled to the tenth (half for each .5), the guess ring stays visible, and each shows its year and source.
5. Your moves: all six cards flip; a typed line appears in the chosen scene's bubble, and it is gone after leaving the mode and coming back; nothing is in localStorage except the teacher scene setting.
6. Teacher: unticking two scenes hides them from the picker after reload; the last ticked scene can't be unticked.
7. Voice: the look how-to is spoken once and then only updates the hint across four scenes; each setup caption is spoken when its panel opens and dropped if the student taps Next first.
8. At 1366x768 and 680x425 the offer panel, thought buttons and all cards are visible without scrolling the page; at 375 wide the panels go one at a time with Back and Next.
9. No em dashes, no brand names on cans or devices, and every number on screen matches Sources.
10. Focus: at 1366x768 and 680x425 the offer panel with its painted kids is the biggest panel while the student decides, and every kid has a thought button over it; the vape and cans sit at the offering kid's hand and are gone in the ending.
11. Tap while it plays: tapping Next, a card, a thought button or another scene while a setup caption is being read stops the caption at once and acts; no caption plays after its panel is gone.
12. The painted cast shows each kid's before picture through the offer and the after picture in the after panel.

## Open questions
- Should there be a "go along" branch? This spec has none: every path ends in a refusal, and Say nothing only leads to the push. A go-along path is more realistic but means drawing a student character vaping or drinking.
- Is the alcohol scene (The sleepover) fine for grade 6 by default, or should it start unticked in Teacher settings? A parent might want to see it first.
- A fifth scene, "a ride home with someone who has been drinking" (calling a parent), is a common refusal-skills lesson; leave it out for 6-8 or add it?
- The cast is now painted (Art rule): 8 kids with two expressions each, 16 people images that wait on Gemini and your review. OK at 16, or one picture per kid (8) with the after mood shown only in words?
