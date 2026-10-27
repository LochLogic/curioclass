# Socratic Seminar Board

## One idea
While the class talks, the projector draws who answers whom: every turn is a line from one seat to another, so the room can see its own conversation take shape (a star around one voice, a ping-pong match between two, or a web where everyone builds on everyone), and the debrief asks whether the talk was a web and whether every claim pointed back to the text.

## Not like
- discussion-dashboard (ela 6, showdown, not specced): talk moves, who has spoken and question stems for a grade 6 discussion. Here the core is the response map and its shape, evidence pins by paragraph, a fishbowl and an evaluation of the author's reasoning (SL.9-10.3); no per-student tallies on screen.
- talk-moves-trainer (eld 3-5) and argument-frames-pro (eld 9-12, roleplay): practice academic phrases with animated classmates. Here the classmates are real and the tool only listens through the mapper's taps.
- usage-panel (ela 11, roleplay, spec): a panel of usage experts disagreeing about grammar. Here the class itself is the panel.
- fallacy-field-guide (ela 10, cards, spec): collects named fallacies. Here the speaker check weighs one author's claims as supported or asserted, without fallacy cards.
- debate-prep-desk (ela 6) and empire-debate (social studies 11): sides and rebuttals. A seminar has no sides and no winner.

## Who and how
- Grade 10 ELA. Module: Debate and Discussion (Speaking and Listening).
- Topic line: "running a Socratic seminar".
- Driver: either. A student alone opens **Practice** (the default): a recorded seminar of six made-up classmates to map and join, 20 to 30 minutes. A class uses Prepare, Seminar, Fishbowl and Debrief with the teacher (or a student mapper) on the projector, the class in a circle or a fishbowl: one 40 to 55 minute period (10 to prepare, 25 to 30 of talk, 10 to debrief).
- Standards: SL.9-10.1 (prepared, collaborative discussion): 1a the text with paragraph numbers and evidence pins; 1b class goals and roles set in Prepare; 1c the map of who answers whom and the move chips (questions, builds on, clarifies, challenges); 1d Summarizes chips and the before-and-after vote, where students say whether their view changed. In Practice, a solo student maps a whole seminar (1c, who answers whom and with which move) and takes three turns of their own that must answer someone, point to a paragraph and add something (1a, 1c, 1d). SL.9-10.3 (evaluate a speaker's point of view, reasoning, evidence and rhetoric, including exaggerated or distorted evidence): the speaker check, where the speaker is the essay's author, never a classmate: three claims rated, plus a point-of-view card and a rhetoric card.
- tool.json: driver "either", minutes "20-55", modes ["Practice", "Prepare", "Seminar", "Fishbowl", "Debrief"], grades_label "Grade 10". Kit starter and `Curio.voice`.

## Screens and modes
Header: title "Socratic Seminar Board", small line "Who answers whom."; mode buttons **Practice** (opens first), **Prepare**, **Seminar**, **Fishbowl**, **Debrief**; Motion, Sound, Read; **Full screen**. Panel: `#hint`, seat count, the text in use, **New seminar** (asks Yes / No; clears the map, goals and votes).

### Practice (opens first; one student, no teacher needed)
- The board in its seminar look: six seats and **T** (a made-up facilitator), the Text and Open floor nodes, the paragraph strip, the Self-Reliance excerpt in a side drawer. A line on screen: "These classmates are made up. Map who answers whom, then join in."
- The recorded seminar (16 turns, Content) plays one turn at a time as a speech bubble from the speaker's seat. For each turn the student taps **whom they answered** (a seat, T, Text or Open floor) and one move chip. Then **One reading** shows the transcript's target and move ("Seat 3 answered seat 2: 'Building on seat 2'. Builds on.") with "Your call can differ." The line on the map always follows the transcript, so the shape is the same for everyone. **Next turn** moves on.
- The shape reading works as in Seminar: at turn 8 it reads Star (talk runs through T), by turn 12 it reads Web. A note at turn 12 asks: "What changed when the classmates started answering each other?"
- **Your turn** comes after turns 7, 12 and 15. The student chooses whom to answer, a move (Question, Builds on, Challenges, Clarifies) and a paragraph, then writes what they would say. The turn joins the map from a seat marked **You**. A self-check card has three ticks: "I named whom I'm answering", "I pointed to a paragraph", "I added something new (a question, an example, a disagreement)". Nothing is graded and nothing leaves the page.
- **Opening vote** and **Closing vote** become the student's own pick (Agree, Partly, Disagree) before turn 1 and after turn 16, with "What moved you, if anything?" at the end.
- **Speaker check** follows the seminar, as in Debrief, but the student makes their own call on each card first and One reading shows after (BASELINE rule 4).
- Practice keeps the student's turns, calls and votes in memory for the session; **Start over** clears them.

### Prepare
- **Text**: **Self-Reliance (excerpt)** built in (Content), or **Your own text**: a title box and a paragraph count (1 to 60), so pins can point at paragraph numbers in whatever the class read. The built-in text shows with paragraph numbers ¶1 to ¶6 and a context card.
- **Seats**: 6 to 24 seats in a ring, numbered 1 to N, plus **T** (teacher) and two nodes in the middle, **Text** and **Open floor**. No names, ever; the panel says "Seats are numbers. Nothing about students is saved."
- **Question bank**: the built-in opening, core and closing questions (Content), each with a check box to use it; **Add a question** for the teacher's own (saved on this device).
- **Class goals** (1b): choose up to three from the list (Content) or write one; they show as meters on the board.
- **Roles** (1b, optional): Mapper (taps the board), Evidence keeper (calls out paragraph numbers), Timekeeper, Opener. Shown on the board as a reminder, assigned out loud, never stored by name.
- **Opening vote**: the class's claim (Content, or the teacher's own) with three counts entered by hand: **Agree / Partly / Disagree**.

### Seminar (projector board)
- Center: the seat ring. Each turn is logged in two taps: tap the **speaker's seat**, then tap **whom they answered** (another seat, Text when they go straight to the text, Open floor for a new thread). A line draws from speaker to target with an arrowhead; repeated pairs thicken the line.
- After the second tap a chip row appears for that turn (optional, one tap, then it fades): **Question ?**, **Builds on +**, **Challenges !**, **Clarifies =**, **Cites text ¶**, **Summarizes Σ**. Cites text then asks for the paragraph number (¶1 to ¶6, or 1 to N for your own text) and drops an **evidence pin** on the paragraph strip along the bottom.
- **Wait time**: when a turn is tagged Question, a ring fills softly around the speaker's seat for the chosen wait (3 or 5 seconds, set in the panel, labeled "the teacher's choice"); no sound.
- **Undo last turn** (one level per tap, back to the start); the board keeps a turn list in the side panel (seat to seat, chip, ¶).
- Top strip: the class goals as meters, the current question from the bank (**Next question** steps through the checked ones), elapsed time.
- **Shape reading** sits in a corner, updated every turn after the eighth: **Still forming**, **Star**, **Ping-pong** or **Web** (rules in Interactions), with one plain line: "Star: most talk goes through seat 4" or "Web: 14 of 18 seats have spoken and talk is spread out." Seat numbers in this line only name the hub, never a count of who spoke least.
- **Seat counts** are hidden by default; a panel toggle shows a small dot per turn on each seat for the teacher's eyes when the board is not projected.

### Fishbowl
- Seats split into **Inner** and **Outer** (the teacher taps seats to move them). Only the inner circle is on the map; each outer seat is paired with an inner seat ("Seat 12 watches seat 3").
- **Observer prompts** on screen for the outer circle (Content), one at a time, chosen by the teacher. Observers keep their notes on paper; the board stores nothing about any one student.
- **Swap** moves outer to inner; the map for each round is kept as Round 1 and Round 2 for Debrief.

### Debrief
- **The map, replayed**: a slider replays the turns in order; the shape reading at the end; for a fishbowl, Round 1 and Round 2 side by side.
- **Moves**: class totals for each chip (bars with glyph and number), with the line "More builds and questions than challenges? More challenges? Neither is wrong; ask why."
- **Evidence pins**: the paragraph strip with a pin count per paragraph, and the question "Which paragraphs did nobody use?"
- **Goals check**: each goal's meter at the end, and a box for the class's one-line note on it (saved on this device with the goals).
- **Closing vote**: the same claim, counts again, shown beside the opening vote, with the prompt "If you moved, which paragraph or which classmate's point moved you?" (1d).
- **Speaker check** (SL.9-10.3): three of Emerson's claims (Content). For each, the class votes by hand count **Supported in the essay / Partly / Asserted only** and the teacher enters the counts; then **One reading** shows a note, labeled "One reader's call." Then two more cards: **Point of view** ("From where does Emerson speak, and who is his advice easiest for?") and **Rhetoric** ("Which figure carries the most weight: the iron string, the joint-stock company, the whip, or the hobgoblin? What does it make you feel before it proves anything?"), each with a box for the class's answer and One reading after.
- **Copy summary**: plain text of the shape, chip totals, pins per paragraph, goals and votes, with seat numbers only, to paste into the teacher's notes.

## Content
### Practice seminar (original transcript, written for Curio Class; seats 1 to 6 are made up)
Each turn: speaker to target; move; paragraph; words.
1. T to Open floor; Question. "Read one sentence you would underline and one you would argue with. Give the paragraph."
2. Seat 1 to T; Cites text, ¶1. "I'd underline 'Trust thyself' in paragraph 1. I'd argue with 'every heart vibrates to that iron string,' because not everyone feels sure of themselves."
3. Seat 2 to T; Cites text, ¶4. "Paragraph 4: 'the world whips you with its displeasure.' That's what being new at a school feels like."
4. T to seat 2; Question. "Is that displeasure the same for everyone?"
5. Seat 2 to T; Clarifies. "No. I meant it's worse if you're new or different."
6. Seat 3 to seat 2; Builds on, ¶4. "Building on seat 2: Emerson says the sour faces 'have no deep cause' and change 'as the wind blows.' So he thinks you shouldn't take them seriously."
7. Seat 4 to seat 3; Challenges. "I partly disagree with seat 3. It's easy to say they have no deep cause. Sometimes people disapprove for a good reason."
(Your turn 1)
8. Seat 5 to seat 4; Question. "Seat 4, is there a place in the essay where the other people are right?"
9. Seat 4 to seat 5; Cites text, ¶3. "Not really. Paragraph 3 says 'you will always find those who think they know what is your duty better than you know it.' He says they think they know. He never lets them be right."
10. Seat 6 to seat 4; Builds on, ¶2. "Adding to seat 4: that's the joint-stock company in paragraph 2. Society wants you to give up your 'liberty and culture' for 'bread'."
11. Seat 1 to seat 6; Clarifies. "So the trade is: you get security, and you give up thinking for yourself?"
12. Seat 6 to seat 1; Clarifies. "Yes, that's how I read it."
(Your turn 2)
13. Seat 3 to Text; Cites text, ¶6. "Paragraph 6 might answer seat 4. It says 'A foolish consistency.' He isn't against every kind of consistency, only the foolish kind."
14. Seat 2 to seat 3; Challenges, ¶6. "But he also says to speak what you think now 'though it contradict every thing you said to-day.' That sounds like he's against consistency, period."
15. Seat 5 to Open floor; Summarizes. "So far: Emerson says other people's disapproval doesn't matter much, and seats 2 and 4 think he goes too far."
(Your turn 3)
16. T to Open floor; Question. "Emerson writes about 'every man'. In 1841, who could follow this advice most freely? Who could not?"
- Shape check (recomputed from these turns with the rules in Interactions, Your turns skipped): after turn 8, Star (T touches 5 of 8); after turn 12 and at the end, Web (all six seats have spoken, T touches 5 of 12 and 6 of 16, the top pair, seat 2 and T, has 3).

### Built-in text: Ralph Waldo Emerson, "Self-Reliance" (excerpt)
- Edition: Essays: First Series, Project Gutenberg eBook #2944 (Sources). Six paragraphs printed whole, in order, with "[text skipped]" between them; the essay's own spelling kept ("to-morrow", "by-standers"); the edition's em dashes in ¶6 are shown as "--". Excerpt length 648 words.
  - ¶1 begins "Trust thyself: every heart vibrates to that iron string." (112 words)
  - ¶2 begins "Society everywhere is in conspiracy against the manhood of every one of its members." (85)
  - ¶3 begins "What I must do is all that concerns me, not what the people think." (100)
  - ¶4 begins "For nonconformity the world whips you with its displeasure." (196)
  - ¶5 "The other terror that scares us from self-trust is our consistency; ..." (43, the whole paragraph)
  - ¶6 begins "A foolish consistency is the hobgoblin of little minds, adored by little statesmen and philosophers and divines." (112)
- Context card: "Emerson (1803-1882) was an essayist and public lecturer from Concord, Massachusetts. 'Self-Reliance' was printed in his Essays: First Series in 1841. Like most writers of his time he writes 'man' and 'manhood' to mean all people. Ask whether his advice works the same for everyone."
- Opening vote claim: "You should trust your own judgment over what the people around you think."
- Question bank:
  - Opening (a round, everyone speaks once): "Read one sentence you would underline and one you would argue with. Give the paragraph number."
  - Core: "Is 'Trust thyself' the same as 'do whatever you want'? Use ¶1 and ¶3." / "In ¶2 society is 'a joint-stock company'. What does Emerson say members trade away, and what do they get?" / "¶3 says some people 'think they know what is your duty better than you know it.' When are they right?" / "In ¶4, who pays the most for nonconformity? Does everyone pay the same?" / "Emerson says 'A foolish consistency' (¶6). What makes consistency foolish, and when is it a virtue?" / "Emerson writes about 'every man'. In 1841, who could follow this advice most freely? Who could not?"
  - Closing: "Has your answer to the opening claim changed? Point to the paragraph or the classmate that moved you."
- Class goals list: "Everyone speaks at least once." (meter: seats that spoke out of all) / "Every claim points to a paragraph." (meter: Cites text chips out of all turns) / "Build on before we challenge." (meter: Builds on before the first Challenges in each thread) / "Answer a classmate, not just the teacher." (meter: turns aimed at a seat other than T) / "More questions from students." (meter: Question chips from student seats).
- Observer prompts: "When did your partner build on someone? Write the words they used." / "When did your partner point to the text? Which paragraph?" / "Did your partner ask a question that changed the direction of the talk?" / "Write one thing your partner said that you want to hear more about."
- Speaker check claims, with one reading:
  1. ¶2: "Society everywhere is in conspiracy against the manhood of every one of its members." One reading: "Asserted only. 'Everywhere' and 'every one' are sweeping; the paragraph gives a comparison (the joint-stock company), not examples."
  2. ¶4: "For nonconformity the world whips you with its displeasure." One reading: "Partly. The paragraph describes the sour faces of by-standers, an experience readers recognize, but 'the world' is an overstatement and 'whips' is a figure."
  3. ¶6: "A foolish consistency is the hobgoblin of little minds." One reading: "Partly, and watch the word 'foolish': the paragraph argues against clinging to what you said before, not against all consistency. The line is often quoted without it."
- Point of view, one reading: "Emerson speaks as a free, educated man with a public platform, to readers he calls 'man'. His advice costs least for people like him; the essay never asks what nonconformity costs someone who could lose a job, a home or their freedom for it."
- Rhetoric, one reading: "The figures do much of the arguing. 'Whips' makes disapproval feel like violence; 'hobgoblin' makes consistency feel childish and silly before any reason is given. Strong images, light evidence: that is part of what makes the essay quotable."

## Interactions in detail
- Practice: a transcript turn records the student's call beside the transcript's `{from, to, chip, para}`; One reading compares them ("Same call" or both shown). Your turns are records with `from: "You"` and count as a seat in the shape reading.
- Turn record `{from, to, chip?, para?, t}`; `from` is a seat or T, `to` is a seat, T, Text or Open floor. Tapping the same seat twice cancels the first tap.
- Shape reading, from the turns so far (each turn touches its speaker and its target seat; Text and Open floor don't count as seats):
  - **Still forming**: fewer than 8 turns.
  - **Star**: one seat (T included) touches 50 percent or more of the turns.
  - **Ping-pong**: no star, and the turns between one pair of seats, in either direction, are 40 percent or more of all turns.
  - **Web**: neither, and at least half the seats have spoken.
  - Otherwise **Spreading**: "Talk is spread out but fewer than half the seats have spoken."
- The thresholds are design choices, shown in an **About shapes** note, and fixed.
- Storage: the seminar (turns, chips, pins, votes) lives in memory only and is gone on reload or New seminar; the page warns before closing while a seminar is running. The question bank additions, chosen goals and goal notes are saved in localStorage `socratic-seminar-board:v1` (try/catch). Nothing typed about a student is ever stored; there is no field for a name.
- Projector: seats are at least 56 px, numbers at least 24 px; at 1280x720 the ring, the paragraph strip and the shape reading are all visible with no scroll. At 760 and below (teacher on a tablet) the turn list moves under the ring. At 375 the ring shrinks to 12 seats per view with a seat picker. No horizontal scroll.
- Keyboard: number keys plus Enter pick a seat, then a target; T, X (text), O (open floor); Q, B, C, L, E, S for the chips; Z undoes.

## Look
- Accent `--brand #0f6e78` (deep teal: header rule, active mode, seat outline on the first tap, arrowheads). Own light `:root` for a bright projector: `--paper #faf7f0`, `--panel #fffef8`, `--ink #1c2226`, `--muted #4f5a61`, `--line #dfe3e2`, `--btn #0f6e78`, `--head-ink #ffffff`, `--focus #8a5a00`.
- Chips (glyph, name and color): Question ? `#0f6e78`, Builds on + `#2f6b2f`, Challenges ! `#a33a2a`, Clarifies = `#5a4fa0`, Cites text ¶ `#8a5a00`, Summarizes Σ `#4f5a61`. Lines between seats are ink at 60 percent; the chip color shows only as a small badge on each line, never as the only signal.
- Contrast (WCAG 2.1): brand on paper 5.57:1, on panel 5.90:1; white on brand 5.96:1; ink on paper 15.03:1; chips on panel 5.87 to 7.00 (Cites text 5.87, Question 5.90, Builds on 6.37, Challenges 6.50, Clarifies 6.79, Summarizes 7.00).
- Different from this group (editors-in-the-margin red, key-term-tracker amber, personal-essay-studio rose, all light) and grade 10 neighbors.

## Art
None: drawn in code (seat ring, lines, paragraph strip). No people.

## Voice
Bank voice `soft-breath`, style "Say softly and calmly, like a seminar leader who lets the room think." The only 9-12 ELA tool with this voice. The kit voice queue (`Curio.voice`), `scope: () => state.mode`. **Seminar and Fishbowl are silent**: no line plays while the class is talking. The text is never voiced.
- w-practice (how, welcome Practice): "Each bubble is one turn. Tap the seat it answers, then tap a move."
- yourturn (how, first Your turn): "Your turn. Pick whom you answer and a paragraph, then write what you would say."
- shape-now (event, the Practice shape reading changes; stale on the next turn): "The map just changed shape. Look at the corner."
- w-prep (how, welcome Prepare): "Choose your text, set the seats, and pick up to three goals for the class."
- vote (how, first time Opening vote is shown): "Count hands for agree, partly and disagree, and type the numbers."
- w-seminar (how, on entering Seminar the first time, before talk starts, shown as text with Read for those who want it spoken): "Tap the speaker, then tap who they answered. The board stays quiet from here."
- w-debrief (how, welcome Debrief): "Replay the map. Then look at which paragraphs nobody used."
- check (how, first speaker check): "Vote on the author, not each other. Supported, partly, or asserted only."
- shape (event, on entering Debrief; stale when the turns change): "Your conversation was a [shape]. Look at the map and ask how it got that way."

## Family engine
None. Standalone tool on the kit starter.

## Sources
- Standards: CCSS ELA SL.9-10.1 (1a to 1d) and SL.9-10.3, https://www.thecorestandards.org/ELA-Literacy/SL/9-10/.
- "Self-Reliance": Ralph Waldo Emerson, Essays: First Series (1841), Project Gutenberg eBook #2944, https://www.gutenberg.org/ebooks/2944. Paragraphs and word counts taken from that file.
- Emerson's dates and Concord: the Ralph Waldo Emerson Society, https://emersonsociety.org/ (confirm at build; if not plainly stated, keep only "American essayist and lecturer").
- Wait time: Mary Budd Rowe's research on teacher wait time (Rowe, 1986, Journal of Teacher Education). Not shown on screen; the 3 and 5 second settings are labeled the teacher's choice.
- Seminar format (inner and outer circle, opening, core and closing questions): common classroom practice; no source shown on screen.

## Done when
- Practice opens first with no setup; each of the 16 turns takes a target and a chip and shows One reading; the shape reads Star after turn 8 and Web after turns 12 and 16 (with Your turns skipped); Your turn adds a line from the You seat; the speaker check shows One reading only after the student's own call.
- Two taps log a turn and draw a line from speaker to target; repeated pairs thicken; Undo removes the last turn.
- With 8 seats: turns T-1, T-2, T-3, T-4, 5-T, 6-T, T-7, 8-T read **Star** (T touches 8 of 8); turns 2-3, 3-2, 2-3, 3-2, 4-5, 6-7, 8-1, 5-4, 7-6, 1-8 read **Ping-pong** (pair 2-3 is 4 of 10, no seat above 40 percent); turns 1-2, 2-3, 3-4, 4-5, 5-6, 6-1, 1-4, 2-5 read **Web** (8 different pairs, 6 of 8 seats spoke, no seat above 3 of 8).
- Cites text asks for a paragraph and drops a pin; Debrief counts pins per paragraph and names the unused ones.
- Goals meters move as turns are logged and match their rules.
- Fishbowl keeps Round 1 and Round 2 maps separately; outer seats never appear on the map.
- Opening and closing votes show side by side; the speaker check shows One reading only after counts are entered; the Point of view and Rhetoric cards show One reading after the box has text.
- No voice line plays in Seminar or Fishbowl; nothing about a student is stored; a reload clears the seminar but keeps goals and added questions.
- At 1280x720 the full board fits with no scroll; at 375 and 760 there is no horizontal scroll.

## Open questions
None. Settled:
- Shape thresholds stay fixed and explained in About shapes; a teacher setting would be an extra (BASELINE rule 4).
- The class seminar stays in memory only, with a warning before closing and Copy summary; nothing tied to a seat is stored (wave 1 rule: nothing stored about a student; rule 7).
- One built-in text: Your own text covers any reading, and the essay's "man" is taught head-on (context card, a core question, the Point of view card) rather than avoided (rule 5).
- The tool now stands alone (rule 4): Practice, a recorded seminar of made-up classmates, is the default for a student with no class.
