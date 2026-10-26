# Resilience Map

## One idea
Every stress has a part you can change and a part you can't: pick an ordinary situation, flip between those two halves, and watch a different set of routes light up across the same island map, so "what helps" depends on which half you are looking at.

## Not like
- mind-map (9-12 health, explorer, built): its Stress bucket fills with stressors and drains through healthy or clogging taps, one amount, one direction. Here there is no level or bucket and nothing is measured; the mechanic is splitting one situation into a changeable and an unchangeable half and seeing that each half calls for different routes. No conditions, myths or help-a-friend scripts.
- community-project-planner (9-12 SEL, tycoon): it runs a project with a budget, team and time. Here nothing is managed or scored; the only "plan" is a short personal coping plan made from chips.
- stress-toolkit (6-8 health, sandbox, not built): it tries breathing, grounding and journaling exercises and tracks which help. Here no exercise is run or timed and nothing is tracked; strategies are places to read about and match to a situation.
- calm-corner (K-2): guided calm-down activities on a projector. Here there is no guided breathing at all (one landmark mentions deep breaths as text).
- not-yet-gym (3-5): growth mindset as a training loop with stripes. No rewards, goals met or progress here.

## Who and how
- Grades 9-12, Social and Emotional Learning, module Stress and Resilience. Format: Explorer.
- Driver: students on their own laptops (a teacher can also project the map for a discussion). 15-30 minutes, fits an advisory period.
- Standards: CASEL.Self-Management ("identifying and using stress management strategies", "using planning and organizational skills", "setting personal and collective goals").
- Sensitive tool (BATCH-SEL.md, Cory's full-review tier). Nothing asks what is stressing the student. All situations are about fictional teens. The plan uses chips only, no free text.

## Screens and modes
Header (kit): title "Resilience Map", mode buttons `The map` | `Stress in the body` | `My plan`, then `Motion`, `Sound`, `Read`. Kit theme `kit:theme-912` with this tool's own `--brand`. Below everything, in every mode, the help footer (see "Help footer").

### The map (default)
- Stage: a painted island seen from above at twilight (art `map-island`, scaled evenly so it keeps its shape; pins, labels, routes, the harbor dot, the lighthouse beam and the legend are SVG on top, re-laid out per size) on a night sea. Five areas, each with a label and an icon, and 20 landmarks (round pins with a small icon and a short name):
  - Body Coast (west shore, icon: a leaf), 5 landmarks.
  - Mind Woods (north, icon: a tree), 6 landmarks.
  - People Village (center, icon: two houses), 3 landmarks.
  - Action Ridge (east hills, icon: a peak), 5 landmarks.
  - The Lighthouse (a point on the south shore, icon: a lighthouse with a soft beam), 1 landmark: Get help.
- Panel, top to bottom:
  1. Hint paragraph (`hint`).
  2. Section "Try a situation": 8 situation buttons (a name and three words, e.g. "Dev: test on Friday"), then `Clear situation`.
  3. When a situation is picked: its one-line story, then a two-button switch `The part they can change` | `The part they can't` (aria-pressed). Under it, the half's text and its route list (2 or 3 landmarks, each with a one-line "how it fits" sentence; each is a button that opens that landmark).
  4. Section "Landmark": the open landmark card (name, area, what it is, "Try it small", "Fits best when", source line) and the button `Add to my plan` (becomes `In my plan` with a check, pressed again removes it).
- What responds: clicking a pin opens its card, rings the pin and draws its label bold. Picking a situation dims every pin except that half's route, and draws a path (solid for the part they can change, long dashes for the part they can't) from the island's harbor to each route pin in order. Flipping the switch redraws the path to the other half's pins (300 ms fade; instant with Motion off). With no situation, every pin is full strength and there is no path.
- Route styles, never color alone: "can change" routes are solid lines with a wrench glyph on each pin; "can't change" routes are long-dash lines with a wave glyph. The legend in the stage corner says "Solid, wrench: work on the problem. Dashes, wave: handle how it feels."
- A small note under the switch, always the same: "Researchers who study coping describe two kinds: working on the problem, and handling how it feels. Matching the kind to the part you can change often helps." (Lazarus and Folkman.)

### Stress in the body
- Stage left: a painted standing figure (art `body-figure`: a smooth mannequin-like body in slate gray-blue, no face, no hair, no gender cues, with the brain, heart, stomach and neck and shoulder muscles softly visible inside, in muted tones) with 7 hotspot buttons drawn in code on top: Brain, Head, Heart, Muscles, Stomach, Sleep, Focus. Stage right: a small line chart "Stress over a week" (x: Mon to Sun, y: no numbers, labels "calm" at the bottom and "on alert" at the top).
- Panel: hint; switch `A short burst` | `Stress that keeps going`; the open hotspot card; the button `Add this sign to my plan`.
- What responds: a hotspot opens its card (what happens, from the sources). The switch redraws the chart: "A short burst" rises on Thursday and comes back to calm by Friday, with the caption "In short bursts, stress can help you avoid danger or meet a deadline. Then the body settles." "Stress that keeps going" rises Monday and stays high, with the caption "When stress lasts, the body stays alert even though there is no danger. Over months that is linked to health problems, which is why recovery time matters." Under the chart, always: "Resilience is coming back toward calm. The map has routes that help."

### My plan
- Stage: a single printable card titled "My resilience map", with five boxes:
  1. "Signs I might notice" (from body signs).
  2. "When I can change it, I can..." (change landmarks).
  3. "When I can't change it, I can..." (Body, Mind and People landmarks).
  4. "People I can go to" (role chips only).
  5. "Any time" (fixed, cannot be removed): "A trusted adult at school, like a counselor, teacher or coach." and "Call or text 988, or chat at 988lifeline.org (988 Suicide & Crisis Lifeline)."
- Panel: hint; chip groups for boxes 1 to 4 (each chip toggles, max 4 per box; a fifth tap shows "Four is plenty. Remove one to add another." and changes nothing); then `Save on this device`, `Clear`, `Print`.
- Note under the buttons, always: "This plan stays on this computer. Nothing is sent anywhere. You don't have to fill in anything."

### Help footer (every mode)
- One calm line across the bottom, ink on a slightly darker band, normal weight, no icon that looks like an alarm: "Need to talk? A trusted adult at school can help. In the US, call or text 988, or chat at 988lifeline.org." The text "988lifeline.org" is a plain link (`https://988lifeline.org`, target _blank, rel noopener). A button `More help` opens a small dialog (Esc and `Close` close it, focus returns to the button):
  - "988 Suicide & Crisis Lifeline: call or text 988, or chat at 988lifeline.org. Free and confidential, any time, day or night (24/7/365). The 988 Lifeline is for everyone."
  - "If someone is in immediate danger, call 911."
  - "A trusted adult at school, like a school counselor, teacher, nurse or coach, can help you find support."
  - "This tool is for learning. It can't tell you what you feel or diagnose anything."
- In boxes under 500 px tall the line shortens to "Need to talk? A trusted adult, or call or text 988." plus `More help`. The footer never covers the main controls.

## Content

### Landmarks (id, name, area, kind, what it is / try it small / fits best when, source)
Kind: change = work on the problem; ride = handle how it feels; both.
- sleep, Keep a sleep routine, Body, ride. Going to bed and getting up at about the same time. / Pick a bedtime for tonight and set a reminder 30 minutes before it. / Almost always; stress and poor sleep feed each other. [NIMH, CDC]
- move, Move more, Body, ride. Any movement counts: a walk, a game, dancing in your room. / A 10 minute walk. CDC suggests starting small and building up to 2 and a half hours a week. / The part you can't change, or a stuck moment. [CDC]
- meals, Eat regular meals, Body, ride. Regular, healthy meals keep energy steady. / Plan a real breakfast for tomorrow. / Busy weeks, when meals are the first thing skipped. [NIMH, CDC]
- caffeine, Go easy on caffeine, Body, ride. Lots of soda, coffee or energy drinks can make a stressed body feel more on edge. / Swap one caffeinated drink for water. / Late nights before a big day. [NIMH]
- breathe, Deep breaths and a stretch, Body, ride. Slow breathing and stretching help the body settle. / Three slow breaths, then roll your shoulders. / Right before the hard moment. [CDC]
- unwind, Make time to unwind, Mind, ride. Plan time for something relaxing you enjoy. / Put 20 minutes of something you like on today's list. / A week with no breaks in it. [CDC]
- unplug, Take a break from news and social media, Mind, ride. Stepping away from the feed for a while. / Phone in another room for one hour. / When scrolling keeps the worry going. [CDC]
- journal, Keep a journal, Mind, ride. Writing thoughts down to get them out of your head. / Write three lines on paper tonight (not in this tool). / Thoughts that keep circling. [NIMH, CDC]
- rethink, Question an unhelpful thought, Mind, ride. Noticing a thought like "I always mess up" and asking if it is really true. / Write the thought, then a fairer version of it. / After a setback. [NIMH]
- grateful, Notice something good, Mind, ride. Practicing gratitude: naming something that went right. / Name one good thing from today. / Long stretches of stress. [CDC]
- outside, Get outside, Mind, ride. Time outdoors, active or just relaxing. / Eat lunch outside or walk the long way. / Days spent indoors on screens. [CDC]
- trust, Talk with someone you trust, People, both. Telling a person you trust what is going on and how you feel. / Think of who that could be (the plan has role chips). / Both halves; a good listener helps you see which part you can change. [CDC]
- friends, Friends who help in a good way, People, both. Time with friends or family who help you cope in a positive way. / Make a plan with one of them this week. / When you'd rather pull away. [NIMH]
- group, A club, team or community group, People, both. Being part of something: a club, a team, a community or faith group. / Look at one club list or team sign-up. / Moves, changes, or feeling left out. [CDC]
- steps, Break it into small steps, Action, change. Turning one big task into pieces you can start. / Write the first step small enough to do in 10 minutes. / Big tasks that feel too big to start. [CASEL]
- schedule, Make a plan with times, Action, change. Putting the steps on a calendar. / Block two study times this week. / Deadlines that pile up. [CASEL]
- askearly, Ask early, Action, change. Asking the person in charge (a teacher, coach or manager) before it becomes a crisis. / Write the one-sentence question you would ask. / Due dates, schedules, rules: anything someone else sets. [CASEL]
- goal, Set one small goal, Action, change. Choosing one thing to work on and when. / "By Friday I will..." / After a disappointment, when you want to get better. [CASEL]
- talkdirect, Talk it through with them, Action, change. Speaking directly and calmly with the person the problem is about. / Plan your first sentence: what happened and what you need. / Problems with another person. [CASEL]
- help, Get help (the Lighthouse), Lighthouse, both. When stress won't go away or feels like too much, more support helps: a trusted adult at school, a counselor, a doctor. Call or text 988 any time. / Not a "try it small": the card shows the same lines as the More help dialog. / Any time. Asking for help is a strength, not a last step. [NIMH, MedlinePlus, 988lifeline.org]

### Situations (button label; story; can change: text, route; can't change: text, route)
1. "Dev: test on Friday". Dev has a chemistry test on Friday and keeps putting off studying. Can change: how and when he studies. Route: steps ("Split the unit into four topics, one per night."), schedule ("Two study blocks on the calendar, Tuesday and Wednesday."), askearly ("Ask the teacher Monday about the part he doesn't get."). Can't: the test is Friday no matter what. Route: sleep ("A full night Thursday helps more than a late cram."), breathe ("Three slow breaths before the test starts."), rethink ("'I'm bad at chemistry' becomes 'I haven't learned unit 4 yet.'").
2. "Ana: didn't make varsity". Ana tried out and made JV, not varsity. Can change: how she trains for next year. Route: askearly ("Ask the coach what to work on."), goal ("One skill goal for the season."), schedule ("Extra practice twice a week."). Can't: this season's roster. Route: friends ("Time with friends who aren't about the team."), move ("Play for fun this weekend."), rethink ("'I'm not good enough' becomes 'Not yet, this year.'").
3. "Sam: moving in March". Sam's family is moving across town, so Sam will change schools. Can change: how Sam gets ready. Route: group ("Look up clubs at the new school."), schedule ("Set a weekly call with old friends."), steps ("Visit the new school before the first day."). Can't: the move itself. Route: trust ("Tell someone how it really feels."), journal ("Write about what Sam will miss and what might be good."), unwind ("Keep one favorite routine the same.").
4. "Priya: group project". Priya's group partner isn't doing his share, and the project is due in a week. Can change: how the work is split and who knows. Route: talkdirect ("Ask him which part he will finish by Wednesday."), steps ("List every task with a name next to it."), askearly ("Tell the teacher now, not the night before."). Can't: how her partner acts. Route: breathe ("Settle before the talk, not during the anger."), rethink ("'This is all on me' becomes 'I can do my part well.'"), friends ("Vent to a friend who will also make her laugh.").
5. "Malik: everything due at once". Malik has three assignments due the same week as a big game. Can change: the order and timing. Route: schedule ("A day-by-day plan for the week."), askearly ("Ask about one extension before the week starts."), steps ("Start the biggest one first, 10 minutes at a time."). Can't: the due dates and the game. Route: sleep ("Keep the bedtime even this week."), meals ("Real meals, not just snacks."), caffeine ("Water instead of a third energy drink.").
6. "Lena: friend group shift". Lena's best friend has been spending most of her time with a new group. Can change: who Lena reaches out to. Route: talkdirect ("Tell her friend she misses her, without blame."), group ("Try one new club."), goal ("Sit with someone new once this week."). Can't: who her friend spends time with. Route: trust ("Talk with someone she trusts about it."), grateful ("Notice the friends who did show up."), unplug ("Take a break from watching their posts.").
7. "Tomás: work schedule". Tomás's first job posted his shifts for the week of his finals. Can change: whether he asks for a swap. Route: askearly ("Ask the manager today about trading one shift."), schedule ("Plan study time around the shifts that stay."), steps ("Find a coworker who might trade."). Can't: the schedule that's already posted. Route: breathe ("A slow breath before asking."), outside ("A walk between shift and studying."), sleep ("Protect sleep on the work nights.").
8. "Grace: waiting to hear". Grace auditioned for the spring play and the cast list comes out in a week. Can change: what she does while she waits. Route: goal ("Pick a backup way to be part of the play, like crew."), steps ("Get the lines she'd need ready, just in case."). Can't: the director's decision. Route: unwind ("Plan something fun for cast list day."), unplug ("Stop refreshing the group chat."), friends ("Wait with a friend, not alone.").

### Body hotspots (name; card text; source)
- Brain: Stress hormones make the brain more alert. That helps in a real emergency. [MedlinePlus]
- Heart: Stress hormones raise your pulse, so your heart beats faster. [MedlinePlus]
- Muscles: Muscles tense up. Lasting tension can show up as body pains or a stiff neck and shoulders. [MedlinePlus, CDC]
- Head: Headaches are a common physical reaction to stress. [CDC, MedlinePlus]
- Stomach: Stomach problems or an upset stomach can come with stress. [CDC, MedlinePlus]
- Sleep: Nightmares or trouble sleeping can come with stress. [CDC]
- Focus: Stress can make it hard to concentrate and make decisions, and can bring forgetfulness. [CDC, MedlinePlus]
Plan sign chips (box 1): Racing heart, Tense shoulders, Headache, Upset stomach, Trouble sleeping, Hard to focus, Feeling on edge, Snapping at people. ("Feeling on edge" and "Snapping at people" come from CDC's feelings list: worry, anger, frustration.)

### Plan role chips (box 4)
Parent or guardian, Another family adult, School counselor, A teacher, A coach, A friend, A school nurse, A faith or community leader, A boss or coworker.

## Interactions in detail
- First load: map, no situation, no landmark open; the landmark section shows "Click any pin to read about it." Tab order: mode buttons, panel controls, then the pins (west to east), then the footer.
- Picking the same situation again does nothing; `Clear situation` returns to the plain map and keeps any open landmark. Switching situations resets the switch to "The part they can change".
- Route items in the panel open their landmark and ring its pin; the path order follows the list.
- The Lighthouse pin is never dimmed, in any situation, and has a slow 4 s beam pulse (static beam with Motion off).
- `Add to my plan` from a card sends change landmarks to box 2, ride landmarks to box 3, both-kind landmarks to box 3; "help" has no add button (it is always in box 5). If the box is full, the button reads "Box full (4)" and is disabled, with that text visible. From Stress in the body, hotspots map to sign chips: Brain to Feeling on edge, Heart to Racing heart, Muscles to Tense shoulders, Head to Headache, Stomach to Upset stomach, Sleep to Trouble sleeping, Focus to Hard to focus.
- Plan memory: picks live in page memory only until `Save on this device`, which writes one localStorage key `curio-resilience-plan` (ids only, no text) in try/catch and shows "Saved on this computer." for 3 s. On load, a saved plan is restored silently. If storage fails, show "Couldn't save here. Print it instead." `Clear` asks inline ("Clear your plan? Yes, clear / Keep it"), then empties boxes 1 to 4 and removes the key. `Print` prints only the plan card plus the Any time box (print CSS: white paper, black ink).
- No scores, counts, badges or "complete" states anywhere. No chime on any pick (Sound only gives a very soft tick on pin open, `Curio.tone`, silent when Sound is off).
- Extremes: zero picks prints a card with only the Any time box filled; that is fine. Very small boxes (680x425): the map keeps all 20 pins at 44 px hit targets with labels shown only for the open pin and route pins; the panel compacts to the situation buttons as a select-like list of 2 columns.
- Reset: changing mode stops speech (`Curio.stop`), keeps the situation and plan. No global reset beyond `Clear situation` and `Clear`.

## Look
- Base: `kit:theme-912` (dark). Accent `--brand: #f2a0b8` (dawn rose, the lighthouse dawn), `--brand-ink: #2a0f19`. Different from batch siblings (mustard #8a5a10, violet #5a2fb8, burnt orange #b3471d), mind-map teal #1f5c63 and the theme default amber #f2a93b.
- Scene: sea #10263a (the stage behind the painting), painted island in the same family (meadow and forest greens, pale sand west shore, grey-blue ridge east), route path in light-on-dark gold #ffe08a, open-pin ring #8fd3ff, footer band #1a1420.
- Contrast (computed, WCAG 2.1): brand on --panel 8.65:1, on --sec-bg 8.2:1; brand-ink on brand 8.89:1; brand on sea 7.72:1; map labels have a 4 px halo #0b1a28 (paint-order stroke), so they read on any part of the painting: pin labels #e8edf3 on the halo 15.0:1, area names #f3eee4 on the halo 15.2:1; ink #e8edf3 on sea 13.11:1, on footer 15.31:1; route gold on sea 11.97:1; ring on sea 9.5:1; muted on sea 7.25:1. All pass AA.
- Labels at least 13 px at 1366x768 and 10 px or more in the 680x425 preview. Stage drawn at real pixel size per box (STANDARDS.md "Sizes").

## Art
Plan and prompts: `art-plan.md`, `art/prompts.json`.
- `map-island` (1600 x 914 WebP, about 40 KB): FLUX.2 [klein] 4B on Cloudflare Workers AI, no people. The island box (pin u, v from 0 to 1) is x 390 to 1250, y 150 to 740 in the painting (`ISL` in src.html); every pin, the harbor (dock, east shore) and the lighthouse lamp (`LAMP`, where the beam starts) are placed on their painted regions. A sea-dark scrim (0.28) dims the painting while a situation is picked.
- `body-figure` (362 x 800 WebP cutout, about 30 KB): OpenAI gpt-image-2 through Codex, reviewed. Hotspot points are measured on the painting (`PT` in src.html).
- Drawn in code: pins and their icons, labels and area names, routes and glyphs, the harbor dot, the beam, the legend, the hotspot pills, leader lines and dots, the sleep moon, the week chart and the plan card.
- `preview.svg` is a screenshot of the map (`scripts/preview.py`).

## Voice
Bank `soft-breath` (Enceladus), style "Say softly and calmly, like a mindfulness teacher". Not used by any other tool; siblings use gentle-storyteller, upbeat-guide, big-sister. Narration is only welcomes and hints (Read uses the hint recordings). Fixed lines, all recorded:
- Welcome, The map: "This is a map of ways people handle stress. Click any pin to look around, or try a situation."
- Welcome, Stress in the body: "Here's what stress does in the body. Click a spot to read about it, and compare a short burst with stress that keeps going."
- Welcome, My plan: "You can build your own map here. Pick what fits you. It stays on this computer, and you don't have to fill in anything."
- Hint, map (no situation): "Click a pin to read about it. Pick a situation to see which routes fit."
- Hint, map (situation picked): "Flip between the part they can change and the part they can't. Watch the routes move."
- Hint, body: "Click a spot on the figure. Then switch between a short burst and stress that keeps going."
- Hint, plan: "Click chips to add them. Save keeps it on this computer, Clear erases it, Print gives you a copy."
- Help dialog: "If you need to talk, a trusted adult at school can help. In the US, you can call or text nine eight eight, any time." (Recorded with "nine eight eight" spoken; on-screen text uses 988.)
- Not spoken: landmark cards, situations, chips, footer line (on screen; Read speaks the current hint).

## Family engine
none.

## Sources
- 988 Suicide & Crisis Lifeline, https://988lifeline.org (checked 2026-10-26): name "988 Suicide & Crisis Lifeline", Call / Text / Chat, "available 24/7/365", "The 988 Lifeline is for everyone."
- CDC, Managing Stress, https://www.cdc.gov/mental-health/living-with/index.html (May 12, 2026): stress is a normal part of life; coping list (breaks from news and social media, unwind, deep breaths and stretch, journal, outdoors, gratitude, talk with people you trust, community or faith groups, sleep, move more and build up to 2 and a half hours a week, eat healthy); reactions (headaches, body pains, stomach problems, sleep problems, trouble concentrating, worry, anger, frustration); "Call or text 988 or chat 988lifeline.org."
- NIMH, I'm So Stressed Out! Fact Sheet (NIH Pub. No. 20-MH-8125), https://www.nimh.nih.gov/health/publications/so-stressed-out-fact-sheet: journal, exercise and regular meals, sleep routine, avoid excess caffeine, challenge unhelpful thoughts, friends and family who help you cope; 988 wording "call or text the 988 Suicide & Crisis Lifeline at 988 or chat at 988lifeline.org."
- MedlinePlus, Stress and your health, https://medlineplus.gov/ency/article/003211.htm (reviewed 5/15/2026): hormones make the brain more alert, muscles tense, pulse up; short bursts can help avoid danger or meet a deadline; chronic stress keeps the body alert "even though there is no danger"; headaches, trouble sleeping, forgetfulness, upset stomach.
- Lazarus, R. S., and Folkman, S. (1984). Stress, Appraisal, and Coping. Springer: problem-focused and emotion-focused coping. Folkman, S., and Moskowitz, J. T. (2004). Coping: pitfalls and promise. Annual Review of Psychology 55: 745-774 (matching coping to controllability; stated modestly as "often helps").
- CASEL, What Is the CASEL Framework?, https://casel.org/fundamentals-of-sel/what-is-the-casel-framework/: Self-Management examples used for Action Ridge.
- Harvard Center on the Developing Child, resilience key concept, https://developingchild.harvard.edu/science/key-concepts/resilience/: "capabilities that underlie resilience can be strengthened at any age" (teacher notes only).
- 911 for immediate danger: https://www.911.gov.
- Note: APA's "Building your resilience" and "Stress effects on the body" pages block automated reading; nothing on screen depends on them.

## Done when
1. All three modes open, no console errors, at every STANDARDS.md size; situation buttons, the switch and the footer's `More help` are visible without scrolling at 1366x768 and 680x425.
2. Picking each of the 8 situations and flipping the switch lights exactly that half's route pins (ids as listed), redraws the path, and the line style plus glyph differ between halves (check in a grayscale frame).
3. The Lighthouse pin is never dimmed; the footer line and `More help` are present in every mode, the 988 text matches the Sources wording, and the link goes to https://988lifeline.org.
4. Every landmark and hotspot card text matches Content, and every fact on screen is in Sources.
5. Before Save, localStorage has no `curio-resilience-plan`; after Save it holds ids only; after Clear (confirmed) it is gone; reload restores a saved plan. No text field exists anywhere in the tool.
6. A fifth chip in any plan box is refused with the message; Print output shows only the plan card and Any time box.
7. No score, count, badge, confetti or "complete" state anywhere; no screen asks the student what is stressing them.
8. Voice: one welcome per mode, Read speaks the current hint, Sound off is silent (STANDARDS.md "Voice behavior", tested with held clicks).
9. Motion off: no path fade or beam pulse, same content.
10. Keyboard only: every pin, chip and button reachable with visible focus; the More help dialog traps focus and Esc closes it.
