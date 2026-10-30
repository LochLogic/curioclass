# Workplace Scenarios

## One idea
At work, small choices travel: live one day as a junior camp counselor, and every choice you make sends a thread down the day's timeline, so a text you didn't send at 8:15 shows up as a missing sign-in at 3:30, and the end-of-day ripple map draws exactly who caught each choice.

## Not like
- career-cluster-explorer (6-8, same group): meets 83 jobs for a minute each, with no choices. Here one job, one day, and every choice has a consequence later.
- career-match-quiz (6-8, built): about your interests. Here about how you act once you have a job.
- conflict-coach (6-8 SEL, built): rewinds one argument line by line to see a face react. Here the choices are about responsibility and teamwork, and the effects land hours later on other people, not in the next line.
- walk-in-their-shoes (3-5 SEL, built): replays one moment from each character's view. Here you stay yourself; the map shows where your choices landed.
- captain-s-choices (9-12 PE): a season with fixed scores and team culture dials. Here there are no dials or meters, only threads between moments.

## Who and how
- Grade 6-8, career and technical education, module "Workplace Skills (Career Exploration)".
- Topic line: teamwork, communication and responsibility on the job
- Driver: students (laptops or tablets, alone or in pairs), or the teacher on a projector with the class voting on each choice. 15 to 25 minutes for one day; replays add 5 to 10.
- Standards: CTE.Career Ready Practices (Advance CTE): CRP1 responsible employee, CRP4 communicate clearly, CRP6 creativity, CRP8 solve problems and persevere, CRP9 integrity, CRP12 work productively in teams.

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound`. Modes (`.seg`): `Day` (default), `Ripple map` (always available; before the day ends it shows the map so far, with unplayed stops grayed).

**Day.** Focus: the story card over the painted place, the biggest thing on the stage (at least 60% of the stage width at 1366x768). Top: the day timeline, 8 stops with times (Content), the current stop marked; earlier stops show the choice made as its letter. Stage: the stop's painted backdrop (Art) with the story card over its lower part: the time and place, the opening (which changes with earlier choices; any changed sentence carries a small thread icon so the student sees a ripple arrive), and then three choice buttons (`A`, `B`, `C`, each with its full text). After a choice: the result card (one or two sentences), its Career Ready Practice tag (for example "CRP4: communicate clearly"), and `Next`. After stop 8, `Next` reads `See the ripple map`.
People appear as name chips, each with a painted object badge (Art) instead of a face: Ms. Ortega (camp director, a clipboard), Kai (senior counselor, 17, a two-way radio), Dev (junior counselor, 13, your partner, a phone), Mia (Bluebird, age 7, her paper owl), Leo (Bluebird, age 7, a small sneaker), Mr. Price (Leo's dad, car keys). A `Job card` button (always available) shows Content "Job card".

**Ripple map.** Focus: the threads, drawn across the whole stage. The timeline drawn large: each stop a column with the choice made (its letter, its short text and the badges of anyone it involved); threads (curved lines) run from a choice to every later moment it changed (Content "Ripples"): a later opening, a result, or an end-of-day note. Thread style by kind: helped (green, solid, plus icon), cost someone (rust, dashed, minus icon), mixed (gray, dotted, dot icon); a legend says so in words. Tap a thread to see both ends' text side by side. Under the map: three end-of-day notes (from Kai, Dev and Ms. Ortega, each with its badge), built from the day's choices. Buttons: `Rewind to here` on any played stop (replays from that choice; later stops reset and threads redraw), `New day` (full restart).

No points, score, stars or win state. Every ending is a normal day with notes.

## Content
**Job card:** "Junior counselor, Lakeside Rec Center summer camp (made up). A volunteer role for ages 12 to 15. You help a senior counselor run a group of eight 7-year-olds, the Bluebirds. Rules: counselors only use the glue guns; count campers at every move; radio Kai before leaving the group; tell Ms. Ortega about any problem with space or safety." Note under it: "Under United States law, most paid jobs outside farms are closed to people under 14, and 14- and 15-year-olds can work only certain jobs for limited hours. So many people start with volunteer roles like this one."

**Stops** (time, place, opening; choices with flag and kind; result):
1. 8:15, in the car. "Your ride is running 15 minutes late. You were supposed to set out the craft bins by 8:30." A. Text Kai: "Ride's late, here by 8:45. Can someone set out the craft bins?" (heads_up, helped): "Kai texts back: 'Thanks for telling me. I've got the bins.'" B. Say nothing and hurry in when you get there. (silent, cost): "You arrive at 8:45. Dev is doing sign-in alone and setting out bins at the same time." C. Text Kai: "Running late." (vague, mixed): "Kai texts back: 'How late? Anything I need to cover?' Your ride pulls in before you answer." Tag CRP4.
2. 9:15, craft table. Opening by flag: heads_up "The bins are out and the glue guns are warm." / silent "Craft starts ten minutes late, and two campers never got signed in." / vague "Kai set out half the bins. The glitter is missing." Then: "Mia wants to use the hot glue gun herself." A. Explain the rule, then let Mia point where every dot of glue goes while you hold the gun. (safe_way, helped): "Mia directs every dot. Her owl ends up with three eyes, on purpose." B. Let her try it just this once while you watch. (bent_rule, cost): "Mia is careful. Two other Bluebirds were watching." C. Say no and move on to the next camper. (flat_no, mixed): "Mia folds her arms and stops working on her owl." Tag CRP1.
3. 10:30, the path to the pool. "You count the Bluebirds. Seven. There should be eight." A. Stop the line, count again, and radio Kai. (stopped_count, helped): "Leo was tying his shoe by the fountain. Kai walks him up. You reach the pool three minutes late, and the lifeguard counts eight." B. Keep walking. You probably miscounted. (kept_walking, cost): "At the pool the lifeguard counts seven. Kai runs back and finds Leo by the fountain, scared." C. Ask Dev to walk the group on while you run back to look. (split_up, mixed): "You find Leo at the fountain. But Dev walked seven kids to the pool alone, and the lifeguard noticed." Tag CRP8.
4. 12:00, lunch pavilion. "A juice box bursts across a whole table. Dev is on his phone." A. Ask Dev straight out: "Can you grab paper towels? I'll move the kids." (asked_dev, helped): "Dev jumps up. 'Sorry, my mom texted.' The table is dry in two minutes." B. Clean it all yourself and complain to Kai later. (complained, mixed): "It takes you ten minutes. Kai says she'll talk to Dev." C. Post "Dev is useless lol" in the junior counselor group chat. (posted, cost): "Three people react with laughing faces. Dev sees it." Tag CRP12.
5. 1:15, the field. Opening by flag: asked_dev "Dev nudges you: 'Say the shadow tag one.'" / complained "Dev won't look at you." / posted "Dev sits at the far end of the bench." Plus, if flat_no: "Mia is still sulking from craft time." Then: "It's too hot for running games. Ms. Ortega asks the junior counselors for an idea." A. Suggest a shade game you know and offer to explain it. (led_idea, helped): "Ms. Ortega says, 'Great. Go.' Eight kids learn a new game in the shade." B. Say you don't have any ideas. (no_idea, mixed): "Ms. Ortega picks a game herself. It's fine." C. Suggest letting the campers vote between two shade games. (vote, helped): "The vote takes one minute, and everyone plays the winner." (with flat_no: "Mia votes, and joins in.") Tag CRP6.
6. 2:30, the gym. Opening, if bent_rule: "On the way in, a Bluebird grabs a glue gun from the craft cart. 'Mia got to!' Kai takes it away." Then: "Thunder. Everyone heads inside, but the Otters group is already in the gym." A. Find Ms. Ortega and tell her both groups are at the gym. (told_director, helped): "Ms. Ortega opens the art room. 'Thanks for coming to me instead of fighting it out.'" B. Tell the Otters' counselor the gym is yours today. (argued, cost): "The two of you argue in front of sixteen kids until Kai steps in." C. Take the Bluebirds to the hallway for a quiet game without telling anyone. (vanished, cost): "Kai checks the gym, then the art room, then finds you. 'I didn't know where my group was.'" Tag CRP8.
7. 3:30, pickup. Opening by the first flag found in this order: kept_walking "Leo told his dad he got left behind at the fountain. Mr. Price is upset." / split_up "Leo told his dad you ran back to find him. Mr. Price wants to know what happened." / silent "Mr. Price asks why Leo's sign-in sheet has no time on it." / none of these "Mr. Price asks how Leo's day went." Problem choices (when kept_walking, split_up or silent is set): A. Listen first, then tell him plainly what happened and offer to get Ms. Ortega. (honest, helped): "Mr. Price nods. 'Thanks for being straight with me.' Ms. Ortega talks with him." B. Say none of it was your fault. (blamed, cost): "Mr. Price asks for Ms. Ortega, and he is not happy." C. Say everything went great. (smoothed, cost): "Mr. Price frowns. That night he hears the whole story from Leo." No-problem choices: A. Tell him one thing Leo did today, like finding the shady spot for the game. (specific, helped): "Mr. Price grins. 'He never tells me anything. Thanks.'" B. Say "He was fine." (fine, mixed): "Mr. Price nods and heads off." C. Send him to Ms. Ortega. (passed_on, mixed): "Ms. Ortega answers him, and wonders why you didn't." Tag CRP9.
8. 4:00, staff room. "Ms. Ortega asks each junior counselor: what will you do differently tomorrow?" A. Name one thing you'd change and one you'd keep. (reflect, helped): "She writes it down. 'That's how you get better at this.'" B. Say it went fine. (shrug, mixed): "She waits a moment, then moves on to Dev." C. Ask her advice about your hardest moment today. (ask_advice, helped): "She tells you about her first summer, when she lost a whole group for five minutes." Tag CRP1.

**Ripples** (flag: where it lands; each is a thread; a thread is drawn only when its landing text really changed because of that flag):
- heads_up, silent, vague: stop 2 opening and Kai's note. silent also lands on the stop 7 opening when it is the flag that opens stop 7 (no kept_walking or split_up).
- bent_rule: stop 6 opening and Kai's note. flat_no: stop 5 opening, and the stop 5 result only when vote is chosen there. safe_way: Ms. Ortega's note.
- kept_walking, split_up: stop 7 opening and Ms. Ortega's note. stopped_count: Ms. Ortega's note only (the stop 7 opening it leads to is the ordinary one).
- asked_dev, complained, posted: stop 5 opening and Dev's note.
- led_idea, no_idea, vote: Ms. Ortega's note. told_director, argued, vanished: Kai's note.
- Stop 7 choices and stop 8 choices: Ms. Ortega's note.

**End-of-day notes** (each person's note joins their lines in this order):
- Kai: heads_up "You told me early, so I could cover. That's most of this job." / silent "I didn't know you'd be late. Dev did two jobs this morning." / vague "Next time, tell me what needs covering, not just that you're late." Then bent_rule "One of ours grabbed a glue gun because Mia got to use one." Then told_director "The art room save was smart." / argued "Arguing over the gym in front of the kids didn't help anyone." / vanished "When I can't find my group, my stomach drops. Radio me first."
- Dev: asked_dev "Thanks for just asking me. I'm putting my phone away tomorrow." / complained "I wish you'd told me yourself instead of Kai." / posted "I saw the group chat."
- Ms. Ortega: safe_way "Mia showed me her three-eyed owl." Then stopped_count "You stopped the line to count. That's exactly right." / kept_walking "Counting is the job. We were lucky today." / split_up "You found Leo. Next time radio first, so no one is alone with a group." Then led_idea "Your shade game was a hit." / vote "Letting them vote was clever." / no_idea "Bring one game idea tomorrow." Then stop 7: honest or specific "Parents trust us when we're straight with them." / blamed "Owning it would have helped with Mr. Price." / smoothed "Mr. Price called me tonight. Tell parents what really happened." / fine or passed_on "Parents love one real detail about their kid." Then stop 8: reflect or ask_advice "See you tomorrow, 8:30." / shrug "Think about one thing for tomorrow. See you at 8:30."

## Interactions in detail
- Choices are buttons with the full text; keys 1, 2, 3 choose too. A choice locks once made; `Next` moves on. `Rewind to here` is the only way to change it.
- Openings and notes are computed from the flags at each moment, so a rewind recomputes every later stop.
- The thread icon in an opening opens the Ripple map with that thread highlighted.
- Threads draw in over about 1 second when the map opens (instant with Motion off). A tap during the draw finishes it at once and acts on the tap (opens that thread's two ends, or rewinds); nothing waits on the animation.
- Teacher mode on a projector: the same screens; choice buttons are at least 60 px tall at 1920x1080 so a class can vote by letter.
- Save: the current day (choices so far) saves on this device (localStorage `workplace-scenarios-day`, try/catch); `New day` clears it. No names are asked for; the student is "you".
- Sizes: story card and the three choices visible without scrolling at every STANDARDS.md size; at 1366x768 the backdrop is the stage and the card sits over its lower part; at 375 wide the backdrop is a short banner above the card; in the 680x425 preview the card text is at least 14 px. Badges are 32 px in chips and 48 px on the map.

## Look
- Accent (`--brand`) #1e6fd9 lake blue; paper #f4f8fb, panel #ffffff, ink #1b2733, muted #556372; threads: helped #187a42, cost #b4461a, mixed #6b7280; timeline track #d7e3ee.
- Contrast: accent on panel 4.85:1 (on paper 4.54:1); white on accent 4.85:1; ink on paper 14.2:1; muted on panel 6.15:1; helped 5.38:1, cost 5.48:1, mixed 4.83:1 on panel. Thread kinds also differ by line pattern and icon.
- The story card is panel white at 94% opacity with a soft shadow, so its text keeps the panel contrast over any backdrop.
- Bright summer-camp daylight in the paintings. Differs from career-cluster-explorer's festival night and career-match-quiz's cream, navy and coral, and from this batch's hospital night, office, journal and trail-map paper.

## Art
Local FLUX (`scripts/localart.py`), one session, no people. Shared style line for every image: "soft painterly flat illustration, warm summer daylight, gentle colors". Blank surfaces wherever text would go. Webp, long side 1400 px for backdrops, 256 px for badges.
- Backdrops (16:9; cutout no; people no; the stage behind the story card, which covers the lower third, so the place reads in the top two thirds):
  - wp-car: "the back seat of a family car stopped in morning traffic, a phone lying face down on the seat, a sunlit windshield and red brake lights ahead, (style)".
  - wp-craft: "a long craft table in a bright rec center room, plastic bins of colored paper and glue sticks, a rolling craft cart with two glue guns on a stand, (style)".
  - wp-path: "an empty paved path through tall trees leading to a fenced outdoor pool, a stone drinking fountain beside the path, (style)".
  - wp-lunch: "empty picnic tables under a wooden pavilion, lunch boxes and juice boxes on the tables, a paper towel roll on a post, (style)".
  - wp-field: "a wide empty grass field in hot midday sun, a row of big shade trees with cool shadows, orange cones on the grass, (style)".
  - wp-gym: "an empty school gym with rain streaking the high windows, gray stormy light, folded bleachers and a ball cart, (style)".
  - wp-pickup: "the empty front curb of a rec center in late afternoon light, parked cars, a wooden bench with a plain clipboard on it, (style)".
  - wp-staff: "a small staff room with a blank white whiteboard, a round table with mugs and clipboards, afternoon light, (style)".
- Person badges (a kit of six; 1:1; cutout yes; people no): one shared prompt "a single (object) centered on a plain white background, (style)", for these objects: a clipboard with a pen; a black two-way radio; a smartphone with a dark screen; a folded paper owl craft with three googly eyes; a small blue sneaker with a loose lace; a ring of car keys. Sizing rule: each object fills 80% of its square, centered, so the six read at the same size. Used in name chips, the map's choice columns and the end-of-day notes.
- 14 images, none with people. Drawn in code: the timeline, threads, legend, story card, chips and every label.

## Voice
Bank voice: `casual-peer` (a teen who has worked at camp before, telling you how the day goes; not one of the characters; different from every tool `neighbors.py` lists and from this batch). Style: casual, warm, like a teen who has done this two summers. `Curio.voice`, `scope: () => state.mode`.
- welcome (how; on entering Day before any choice; stale when a choice is made): "It's day three of camp. Read what's happening, then tap A, B or C."
- rippleArrives (event; when an opening contains a ripple, just before the opening; stale when the stop changes): "Something from earlier just showed up."
- opening (event; each stop as it opens, the computed opening text; stale when the stop changes).
- result (event; after each choice, the chosen result text; stale when the stop changes).
- choiceHow (how; after the first result; stale when Next is tapped): "Tap Next to keep the day moving."
- dayDone (event; after stop 8's result; stale when the mode changes or New day is tapped): "That's the day. Tap See the ripple map to find where your choices landed."
- welcomeMap (how; on entering Ripple map; stale when a thread or Rewind is tapped): "Each line runs from a choice to where it landed. Tap a line to read both ends."
- rewindHow (how; first rewind; stale on the next choice): "You went back. Tap a new choice, and watch the threads redraw."
- note (event; an end-of-day note, read when its card is tapped; stale on the next tap).
All opening, result and note texts in Content are voiced (they are the story); choice button texts are not (Read speaks them).

## Family engine
none

## Sources
- Career Ready Practices CRP1, CRP4, CRP6, CRP8, CRP9, CRP12 (the 12 practices of the Common Career Technical Core, 2012): Advance CTE, https://careertech.org/resource/career-ready-practices (the builder checks the numbering and wording against Advance CTE's current list before build; see Open questions).
- Under 14, most non-agricultural jobs are not allowed; 14 and 15 only in certain jobs with hour limits; 16 is the basic minimum age: U.S. Department of Labor, Wage and Hour Division, Fact Sheet #43, Child Labor Provisions for Nonagricultural Occupations under the FLSA, https://www.dol.gov/agencies/whd/fact-sheets/43-child-labor-non-agriculture
- Camp, people, story and notes: written for this tool.
- Checks run (Python, 2026-10-29): all 6,561 possible days (3 choices at 8 stops). Every day gets one note from each of Kai, Dev and Ms. Ortega and an opening at every stop; 5,103 days (78%) reach the problem pickup at stop 7 and 1,458 the ordinary one. Each day draws 10 to 12 threads (all-A 10, all-C 12) under the rule above. Fixed from the old spec: stopped_count drew a thread to a stop 7 opening it never changes, and flat_no drew one to the stop 5 result when vote was not chosen; both now draw only where text changes. Removed `Print my day` (a print card; Save on this device is enough).

## Done when
1. Every stop's opening is right for each relevant earlier flag (walk all 3 stop-1 choices to stop 2; all 3 stop-3 choices plus silent to stop 7).
2. Stop 7 uses the problem choices when kept_walking, split_up or silent is set, and the no-problem choices otherwise.
3. The Ripple map draws exactly the threads in Content for two full playthroughs (all-A: 10 threads, all-C: 12), each with words, pattern and icon.
4. End-of-day notes join in the stated order and change after a rewind.
5. Rewind to here resets only later stops; New day clears storage; the day survives a reload.
6. There is no score, meter or win message anywhere.
7. Focus: at 1366x768 and 680x425 the story card with its three choices is the largest thing on the Day stage, and the threads span the Ripple map stage.
8. Tap while it plays: a tap on a thread or Rewind while the threads draw acts at once; a choice tapped while an opening is spoken stops it and the result plays.
9. Story card and choices are visible without scrolling at every STANDARDS.md size; projector choice buttons are 60 px or taller at 1920x1080.
10. All 8 backdrops and 6 badges load; no painted image shows a person or fake lettering.
11. How lines are spoken once in five stops in a row; opening and result are spoken every stop and dropped when stale.

## Open questions
- Career Ready Practices numbering: the tags use the 2012 list of 12 (CRP1 to CRP12). Advance CTE released a modernized framework in October 2024 and now hosts a 2024 Career Ready Practices document; if the practices were renumbered or reworded, should the tags follow the new list, or drop numbers and show only the plain names?
- The C choice at stop 4 has a student post an unkind group-chat message (no slur, no names beyond Dev). Fine for grades 6-8, or soften it to "Vent about Dev in the group chat"?
- People are shown as object badges (a clipboard for Ms. Ortega, a radio for Kai), not faces, so no image waits on Gemini. Fine, or should the six characters get painted portraits later (6 images for Cory's review)?
