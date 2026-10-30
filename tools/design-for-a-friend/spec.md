# Design for a Friend

## One idea
You interview a friend before you design their app, and the kind of question you ask decides what you learn: an open question uncovers a real need, a leading one ("Wouldn't points be fun?") gets a polite "Sure!" that looks just like a need on your board, and only the friend's test drive of your design shows which features they used and which they never touched.

## Not like
- network-help-desk (4): asking questions reveals parts of a home network, and every question gets a true, useful answer. Here questions differ in kind, and a leading question produces a false need that looks real until the test drive.
- game-remix (5): you change a working program and credit its author. Here nothing is coded; you decide what to build, for whom, from what they told you.
- biased-bot (4) and leaf-sorter-ai (5): data decides what a model learns. Here people decide what a design needs, and the evidence is what they say and do.
- design-fixer (6-8, art): fixes a poster for the eye. Here the fix is for a person's need, and the test is whether they can finish a task.
- algorithm-audit (6-8, this group): tests a finished system for fairness. Here you design a new feature from scratch with its users.

## Who and how
- Grade 5, computer science. Module: Human-Centered Design (Computing and Society), "Design technology for real users". Topic line: "designing an app with the people who will use it".
- Driver: students in pairs on laptops (one asks, one takes notes, then swap), or a teacher on a projector with the class voting on each question. 20 to 35 minutes (one friend about 8 minutes, One app for all about 10).
- Standards (CSTA 2026 ids from the module): E5-ALG-IM-03, E5-SOC-HU-18. 2017 crosswalk: 1B-AP-13 (use an iterative process to plan a program, including others' perspectives and user preferences), 1B-IC-19 (improve the accessibility and usability of technology for the diverse needs and wants of users), 1B-IC-20 (seek diverse perspectives to improve computational artifacts). Reference: Nielsen Norman Group, "Interviewing Users".
- tool.json: driver "students or teacher", minutes "20-35", modes ["Interview", "One App for All"], grades_label "Grade 5".

## Screens and modes
Kit frame, own `:root` (a warm design studio). Header: title "Design for a Friend", small line "Maple Street Garden app"; mode buttons "Interview" (speech bubble icon) and "One App for All" (three people icon); Motion, Sound, Read.

The setting: the made-up Maple Street Community Garden wants an app so gardeners can sign up for watering days. Its test task is the same for everyone: "Sign up to water your plot on Saturday, and remember to go." Five steps: 1 Read the home screen, 2 Find your plot, 3 Pick Saturday, 4 Tap Save, 5 Remember on Saturday.

### Mode 1: Interview (opens first)
Focus, per tab: Ask, the friend's portrait and the newest chat bubble at the stage center, the largest pair on the
stage, with the Needs board beside them; Design, the phone with its slots at the stage center; Test drive, the
friend's marker walking the five steps under the phone, with each step's light and snag bubble beside the screen it
happens on.
Start: the community garden (art: garden-backdrop) behind three friend cards (portrait, name, one line): "Lou, 72, has grown tomatoes here for forty years", "Ana, 9, shares plot 12 with her mom", "Kofi, 15, keeps his grandma's plot going". Tap one to begin. A "Friends" strip at the top of the stage lets you switch friends any time; each keeps its own progress.

Three steps on one screen, shown as tabs under the friend's name: "Ask", "Design", "Test drive". All open; nothing locked.
- Ask. Stage: the friend's portrait (art: friend-lou, friend-ana or friend-kofi) over the garden and a chat column. Panel: "Questions" with the friend's question cards (below), and "Questions left: 4" (the friend has time for four; the tool's own limit). Tapping a card spends one question; the friend's answer appears as a chat bubble and the answer's note goes on the Needs board. Follow-up cards appear only after the open question they follow; they also cost one. "Start over with Lou" refills the questions and clears the board.
- Needs board (right side of the stage under the chat, or its own tab at small sizes): yellow sticky notes for needs and wishes (they look the same) and blue cards for facts about the friend. Each note shows the friend's own words when tapped.
- Design. Stage: a phone frame showing the app's home screen with three empty feature slots (the tool's own limit for one friend). Panel: the feature shelf, eleven cards (below), each with an icon and a one-line description. Tap a card then a slot, or drag; tap a placed card to remove it. The phone preview changes as features are placed (big text makes the words bigger, the Spanish switch adds an "ES / EN" toggle, plant pictures replace plot names with the painted plants from the plant kit, and so on).
- Test drive. "Start test drive" (big button). The friend's marker (their portrait cutout in a circle) walks the five steps along a path under the phone, about 0.8 s a step (4 s a friend); each step lights green (done) or orange with a snag bubble in the friend's words when a need is not met by a placed feature. Then the result card: "Lou finished the task." or "Lou got stuck at steps 1 and 4.", and each placed feature stamped "Used at step 2" or "Never used". Any wish note on the Needs board whose feature was placed and never used gets a gray "Polite yes" stamp and a line: "You asked a leading question, so Lou agreed to be kind."
- "Back to design" keeps the design for another try.

### Mode 2: One App for All
Focus: the one phone with its four slots at the stage center; during and after the test drive, the three-row result
table under it, the largest thing once it fills.
One phone, four slots (the tool's own limit), all three friends. The Needs boards from Interview are shown side by side (or, for friends not yet interviewed, a "Not interviewed yet" card with "Interview" button). "Start test drive" runs Lou, then Ana, then Kofi; result table: three rows by five steps, green or orange. A "Helped more than one friend" line names any placed feature that met needs for two friends. A hint when a full design fails: "Four slots, six needs. Look for one feature that helps two friends."

## Content
Needs (id; who; what; features that meet it; steps where it matters):
- L1, Lou, "Small words are hard to read"; Big text or Read aloud; steps 1 and 3.
- L2, Lou, "Taps the wrong button"; Big buttons far apart; step 4.
- A1, Ana, "Mom reads Spanish best"; English and Spanish switch; steps 1 and 4.
- A2, Ana, "Can't read plant names yet"; Plant pictures or Read aloud; step 2.
- K1, Kofi, "Forgets by Saturday"; Reminder you set; step 5.
- K2, Kofi, "Signs up walking, one hand"; Big buttons far apart or Home screen shortcut; step 4.
Wishes (from leading questions; never used in any test drive): Lou "Video lessons?", Ana "Points and badges?", Kofi "Chat with gardeners?".

Feature shelf (eleven): Big text; Read aloud; Big buttons far apart; English and Spanish switch; Plant pictures; Reminder you set; Home screen shortcut; Video lessons; Points and badges; Chat with gardeners; Weather forecast. (Weather is nobody's need or wish.)

Checked designs: every need is met by Read aloud, Big buttons far apart, English and Spanish switch, Reminder you set (four features, the only four-card set that finishes the task for all three friends). With five or more slots other sets would work (for example Big text, Plant pictures, Big buttons, Spanish switch, Reminder), but One App for All has four.

Questions (kind; question; answer; what it adds). Lou:
1. open: "Tell me about the last time you used an app." "My grandson set one up. The words were so small I gave up and called him instead." Need L1.
2. open: "What's the hardest part of using a tablet?" "My finger hits the wrong button and I end up somewhere else." Need L2.
3. follow-up to 2: "Can you show me what happened?" "See this Save? It's the size of an ant, right next to Delete." Adds the quote to L2.
4. leading: "Wouldn't video lessons help you learn the app?" "Sure, I suppose." Wish "Video lessons?".
5. yes or no: "Do you like the garden?" "Yes." Nothing.
6. open: "What do you do in the garden?" "Tomatoes, forty years of them. I water every Saturday." Fact card.
Ana:
1. open: "Tell me how your family uses the garden." "Mom and I share plot 12. She signs us up on her phone. She reads Spanish best, so I help with the English words." Need A1.
2. open: "What's confusing in the app?" "The plot list just says words like zucchini and kohlrabi. I know our plants by how they look!" Need A2.
3. follow-up to 1: "What happened last time your mom signed up?" "She asked me what Save means. I told her: guardar." Adds the quote to A1.
4. leading: "Wouldn't points and badges make it more fun?" "Ooh, yes! Points!" Wish "Points and badges?".
5. yes or no: "Is the app hard?" "Kind of." Nothing.
6. open: "What's your favorite thing to grow?" "Strawberries. And sunflowers taller than my mom." Fact card.
Kofi:
1. open: "Walk me through your Saturday." "I work at the pizza place till 2. Last time I totally forgot my watering day and the beans dried out." Need K1.
2. open: "Where are you when you sign up?" "Walking to the bus. Phone in one hand, backpack in the other. Tiny buttons are the worst." Need K2.
3. follow-up to 1: "What would have helped you remember?" "Something that buzzes me at like 2:15, right when my shift ends." Adds the quote to K1.
4. leading: "Wouldn't a chat with other gardeners be cool?" "Yeah, sure, I guess." Wish "Chat with gardeners?".
5. yes or no: "Do you use apps a lot?" "Yeah." Nothing.
6. open: "Why do you garden?" "My grandma started our plot. I keep it going." Fact card.
Each yes or no answer adds a hint line: "A yes or no question got a yes or no. Try asking them to tell you about something."

Snag bubbles (friend's words at a failed step): L1 "I can't read this." L2 "Oops, I hit Delete." A1 "Mom: ¿Qué dice aquí?" (shown with "Mom asks: what does it say here?") A2 "Which one is our plot?" K1 "Wait, was that today?" K2 "Ugh, missed the button."

On-screen ideas (Test drive result cards and the One App for All line): "A leading question suggests its own answer, so people often just agree." "A feature built for one person's need often helps many people. That's called the curb-cut effect."

## Interactions in detail
- Asking a question spends it at once; the bubble types in over 600 ms (instant with Motion off). With 0 questions left the cards disable and the hint says "Lou has to go. Look at your Needs board, then tap Design."
- Needs and wishes are both yellow and carry the same note style, so the board never gives away which is which; tapping a note shows the friend's words.
- A friend's test drive checks each step in order: a step fails if any of that friend's needs listed for that step has no placed feature that meets it. All five steps are always shown (no early stop).
- A placed feature is "Used" if it meets a need of that friend at some step; otherwise "Never used". The "Polite yes" stamp appears only on a wish whose feature was placed.
- Design without asking anything is allowed; the test drive still runs and shows the snags. Placing the same feature twice is not allowed (its shelf card greys out).
- One App for All uses needs from the content above even for friends not yet interviewed (the test is about the friends, not your notes), but shows "Not interviewed yet" on their board so the class sees what they skipped.
- Every control stays live while a test drive plays and responds at once: tapping a slot or a shelf card, Back to
  design, a tab or a friend stops the drive at once (no result card, no line); Start test drive restarts it from step 1;
  Motion off shows each step's result at once on the same timing.
- Mode switch keeps both modes' state. Nothing is saved after the page closes.
- Keyboard: friend cards, question cards and shelf cards are buttons; a shelf card then a slot (Enter, Enter) places it. Visible focus.
- Sizes: question cards, the chat's last bubble and "Questions left" visible without scrolling at 1280x720, 1366x768 and 680x425 (the Needs board becomes a tab there); in Design, the phone and the shelf side by side down to 760 wide, stacked below that with the slots first.

## Look
- Accent `--brand #0369a1` (deep sky blue; header, selected tab, slot outlines, Start test drive). `--head-ink #ffffff`.
- Own `:root` (design studio): `--paper #fbf7f0`, `--panel #ffffff`, `--ink #1f1d2b`, `--muted #5c5870`, `--line #e6e0d4`, `--btn #0369a1`, `--focus #9a3412`. Sticky notes #fff1a8 with a 1 px shadow; fact cards #dbeefe; step done #15803d with a check, snag #c2410c with a "!" (glyph and word, never color alone); "Polite yes" stamp gray #5c5870.
- Neighbors: code-tracer rust, game-remix teal, biased-bot mustard, network-help-desk green, leaf-sorter-ai navy, data-defenders gold, design-fixer indigo. Deep sky on warm paper is apart from them and from its group siblings (chalk yellow, hot spring orange, fuchsia, navy).
- Contrast: white on brand 5.93:1; brand on paper 5.56:1; brand on sticky note 5.20:1; ink on paper 15.50:1; ink on note 14.50:1; muted on paper 6.37:1; muted on panel 6.81:1; focus on paper 6.84:1; white on step-done green 5.02:1; white on snag orange 5.18:1. All pass AA.

## Art
People go to Gemini (`scripts/art.py`, set aside for now, so these wait on Cory); everything else is local FLUX
(`scripts/localart.py`). One warm, flat illustration style for all, asked for in one session per tool.
- friend-lou: "portrait of a friendly older man, about 72, with reading glasses pushed up, a straw sun hat and a
  gardening apron, holding a tomato, warm natural light, flat illustration, plain cream background, chest up"; 1:1;
  cutout yes; people: true (Gemini, Cory reviews); friend card, chat avatar, test drive marker.
- friend-ana: "portrait of a cheerful girl, about 9, in a yellow raincoat holding a small watering can, flat
  illustration, plain cream background, chest up"; 1:1; cutout yes; people: true (Gemini, Cory reviews); same uses.
- friend-kofi: "portrait of a relaxed teenage boy, about 15, with a backpack strap on one shoulder and a phone in his
  hand, wearing a work cap, flat illustration, plain cream background, chest up"; 1:1; cutout yes; people: true
  (Gemini, Cory reviews); same uses.
- Ana's mom appears only as a speech bubble (no image).
- garden-backdrop: "A small neighborhood community garden on a sunny morning, raised wooden plots with tomatoes, beans
  and sunflowers, a watering can on a gravel path, a low fence and a shed with a blank wooden sign, warm flat
  illustration"; 16:9; cutout no; people no; the Interview stage behind the friend cards and the portrait (softened 40
  percent behind the chat so bubbles read).
- Plant kit (6 pieces, one prompt: "A single [plant], centered, warm flat illustration, plain white background"); 1:1;
  cutout yes; people no; the app's plot list on the phone when Plant pictures is placed: plant-tomato (a red tomato on
  its vine), plant-zucchini, plant-kohlrabi (a pale green kohlrabi bulb with leaves), plant-beans (green bean pods),
  plant-strawberry, plant-sunflower.
The phone frame and app screens (they are mock-ups of a UI), feature cards, sticky notes, the step path, stamps and
preview.svg (a phone with three feature cards beside a sticky note board with one gray "Polite yes" stamp) are drawn
in code. 10 images, 3 with people.

## Voice
Bank voice `wise-mentor` (Gacrux), "Say thoughtfully and warmly, like a wise high school mentor": the studio lead who
loves good questions. Changed from curious-librarian, which spot-the-ai (this batch, same subject) uses. Not used by
any CS neighbor (code-tracer clear-teacher, game-remix big-sister, biased-bot news-reader, network-help-desk
upbeat-guide, leaf-sorter-ai gravel-ranger, data-defenders hero-coach, data-table-builder knowing-guide,
algorithm-audit calm-professor) or a group sibling. Friends' answers are read on screen; Read speaks the hint.
`Curio.voice`, `scope: () => state.mode`.
How (spoken the first time its moment comes, then hint only):
1. w-interview (Interview entered; stale on a friend tap): "The garden wants an app. Before you design it, meet the
   people who'll use it. Tap a friend to start."
2. ask (first friend opened; stale on the first question): "You have time for four questions. Tap a question card to
   ask it."
3. open-q (first open answer; stale on the next question): "That answer went on your Needs board. Open questions get
   stories."
4. closed-q (first leading or yes or no answer; stale on the next question): "Hmm. Did that question let them tell you
   something new? Try a card that asks them to tell you about something."
5. time-up (questions run out, first time; stale on the Design tab): "Time's up for questions. Tap the Design tab and
   pick three features."
6. design (first Design visit; stale on Start test drive): "Tap a feature, then tap a slot on the phone. When you're
   ready, tap Start test drive."
10. w-all (One App for All entered; stale on Start test drive): "Now one app for all three friends, with four slots.
    Look for features that help more than one. Then tap Start test drive."
Events (every time; stale on any design change, a new drive or a mode switch):
7. Drive ends with every step done: "Lou finished the task!" / "Ana finished the task!" / "Kofi finished the task!"
8. Drive ends with snags: "Lou got stuck. Look at the orange steps, then tap Back to design." / the same with Ana /
   the same with Kofi.
9. A wish stamped (after 7 or 8): "Your friend said yes to be kind. A leading question can do that."
11. One App for All, all three finished: "Everyone finished. Some features helped more than one friend."
12. One App for All, someone stuck: "Someone got stuck. Four slots, six needs. Look for one feature that helps two
    friends."

## Family engine
none.

## Sources
- Interview practice (open questions, avoid leading and yes or no questions, ask follow-ups): Nielsen Norman Group, "Interviewing Users": https://www.nngroup.com/articles/interviewing-users/
- The curb-cut effect: Angela Glover Blackwell, "The Curb-Cut Effect", Stanford Social Innovation Review, Winter 2017: https://ssir.org/articles/entry/the_curb_cut_effect
- Bigger, well-spaced tap targets help people who mistap: W3C, Understanding WCAG 2.2 Success Criterion 2.5.8 "Target Size (Minimum)": https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Designing with users in rounds (ask, make, test, change): IDEO.org, The Field Guide to Human-Centered Design (2015): https://www.designkit.org/resources/1.html
- CSTA K-12 Computer Science Standards (2017): https://csteachers.org/k12standards/
- Maple Street Garden, its app, Lou, Ana, her mom and Kofi are made up.
- Checks run (Python, 2026-10-29, every set of the eleven features against the six needs): exactly one set of four
  finishes for all three (Read aloud, Big buttons far apart, English and Spanish switch, Reminder you set); no set of
  three does; eight sets of five do. Read aloud helps Lou and Ana, Big buttons helps Lou and Kofi. Each friend alone
  needs at least two features, so three slots in Interview always leave room. Lou with Big text and Big buttons
  finishes, with Big text alone snags at step 4; Kofi with Home screen shortcut and Reminder finishes, with Chat and
  Reminder snags at step 4. Empty designs snag Lou at 1, 3, 4; Ana at 1, 2, 4; Kofi at 4, 5. Every contrast ratio in
  Look recomputed with the WCAG 2.1 formula and matches.

## Done when
1. Asking Lou questions 1 and 2 puts two notes on his board; question 3 appears only after question 2; after four questions every card disables.
2. Asking Ana question 4 adds a wish note that looks the same as a need note.
3. A Lou design of Big text and Big buttons far apart finishes all five steps; removing Big buttons snags step 4 with "Oops, I hit Delete."
4. A Lou design of Big text, Big buttons far apart and Video lessons finishes all five steps, stamps Video lessons "Never used", and, if question 4 was asked, stamps the wish "Polite yes".
5. One App for All with Read aloud, Big buttons far apart, English and Spanish switch, Reminder you set finishes for all three and names Read aloud and Big buttons as helping more than one friend; no other set of four finishes for all three.
6. Kofi with Home screen shortcut and Reminder you set finishes; with Chat and Reminder he snags at step 4.
7. Lines 2, 3, 4 and 6 are each spoken once in a run of five actions; lines 7 and 8 after every test drive.
8. Question cards and "Questions left" visible without scrolling at 1366x768 and 680x425; step results readable in grayscale by glyph and word.
9. Focus: at 1366x768 and 680x425 the portrait with the newest bubble (Ask), the phone (Design) and the marker on the
   step path (Test drive) are each the largest thing at the stage center.
10. Tap while it plays: during a test drive, a slot tap or Back to design stops it at once with no result line, and
    Start test drive restarts from step 1.
11. Voice: no line names a disabled control; 7, 8 and 12 every drive and dropped on a design change.

## Open questions
- The three friends are people (Lou, Ana, Kofi), all waiting on Cory; the tool is about real users, so they stay.
- The voice moved from curious-librarian to wise-mentor because spot-the-ai (grade 1, same subject) uses
  curious-librarian. Fine?
