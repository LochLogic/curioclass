# Book Group Table

## One idea
The student joins a four-person book group as the fourth member: they prepare from a short public-domain story ("The Gift of the Magi") with two questions and a line of evidence, then at each turn pick a talk move (ask, answer with evidence, build on, paraphrase, invite the quiet member) and write or pick the words, and the group's talk deepens or stalls by the move: a paraphrase that gets Maya wrong earns a correction, and asking Omar, who hasn't spoken, brings out an idea no one had, so they learn what makes a discussion go somewhere.

## Not like
- socratic-seminar-board (10, concept): mapping who answers whom in a real seminar. Here a solo seat at a small group with chosen moves.
- podcast-listening-club (6-8, concept): judging a speaker's claims. Here taking part in a discussion.
- counterclaim-rally (concept): arguing a side. Here discussing to understand.
- character-face-off (5, spec): comparing two characters. Here talking about one story with others.
- dialogue-director (3, spec): writing dialogue. Here doing discussion.

## Who and how
- Grade 6, ELA, module "Collaborative Discussions" (Speaking and Listening). Standard: SL.6.1 (a, b, c, d).
- Driver: one student (tool.json `driver: "student"`). Role: lesson. Every bubble and sentence is read on tap. Class mode: a projector tracker for a real discussion, with a pairs card for two real students.
- Change note (spec fix, 2026-11-10): the table, the three classmates and the move chips stay. Added: a short model talk the student listens to first; three more discussions, so there are five, one a sitting; a set-up step in each talk with a goal, a turn limit and a role that changes each time; a sixth move, Probe; the evidence pin is now keyed to the question; rule slips for "back it up" and "everyone talks"; answers and build-ons are typed as full sentences against a guide; a paraphrase is typed from memory before the three versions show, and a wrong pick stays on the closing card; in the closing the student types the key ideas before any list shows and writes how two classmates saw it. The story is now the full text, not abridged.
- Two texts, five discussions. On the story: "What did each gift really cost?", "Were they wise or foolish?" and "Who gave up more?". On the issue page: "Should the group choose its own books?" and "Is it fair to grade a discussion?". tool.json `modes: ["My seat", "Class tracker"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the prep card and the closing round. The class tracker keeps counts only while the page is open.
- Change note (2026-11-11): the student now sets the deadline. The 12 turns stay, and in Set up the student picks the turn by which the goal must be met; at that turn the talk stops for a deadline check. Added the three hooks: the fifth discussion is done on your own with the end screen by code, English learner supports, access.
- English learners: every bubble is on screen as it is spoken, in the speaker's own short sentences. The words paraphrase, evidence, goal, deadline and role each show with an example from the model talk the first time they are used. Every typed turn offers a frame the student may take or leave ("You are saying that __."; "I agree with __ because line __ says __."). Instructions use no idioms; idioms in the classmates' speech are glossed on tap.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| SL.6.1a | come to discussions prepared, having read the material; draw on that preparation by referring to evidence to probe and reflect on ideas | the student | Prep: read, write two questions, pin a line that bears on the question; in the talk use the pin and Probe a classmate's claim by picking the line that backs it or does not | 5 discussions; 2 probes in each | the prep card, its items lighting when used; the probed line | 2 |
| SL.6.1b | follow rules for collegial discussions, set specific goals and deadlines, and define individual roles as needed | the student | Set up: write the group's goal, set the deadline (the turn by which the goal must be met) and check it when it comes, take a role and do its job; keep the three rules | 5 set-ups, 4 roles | the table tent, the turn clock, the role card | 3 |
| SL.6.1c | pose and respond to specific questions with elaboration and detail by making comments that contribute to the topic, text or issue | the student | Pick a move each turn and type the words: a question, or an answer or build-on of a full sentence with a detail | 5 turns in each of 5 discussions | the bubbles and the move chip | 4 |
| SL.6.1d | review the key ideas expressed and demonstrate understanding of multiple perspectives through reflection and paraphrasing | the student | Paraphrase a classmate from memory in your own words; in the closing type the key ideas, then say how two classmates saw it and whether you moved | 5 closings; 2 paraphrases in each | the closing card | 5 |

## Screens and modes
Header (kit): title "Book Group Table"; `Prep`, `Talk`, `Closing`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A library table with four chairs, a table tent of rules and three classmates already seated: Maya (quick, confident, talks first), Priya (careful, asks for proof) and Omar (quiet, sketches in the margin). First hint: "Tap Prep to read the story." The first tap reads "Prep"; the welcome is queued after it (`welcomeAfter: true`).

**Listen in first (the model).** Before the first Prep the student hears a six-turn talk about a fable ("The North Wind and the Sun", text on a card) with Priya in the fourth seat. Each of her turns shows its move chip as she speaks: she asks, answers with a line, probes Maya, paraphrases Omar, invites, and closes with two key ideas. It cannot be skipped the first time and `Listen in` reopens it.

**Prep.** O. Henry's "The Gift of the Magi" (1905), full text of about 2,100 words, in numbered sentences (tap to hear, or `Listen` for the whole story). A glossary strip (pier-glass, fob, Magi, mendicancy, meretricious). The issue page is one screen of about 300 words giving two views on each issue question. The prep card: two question boxes and one evidence pin (tap a sentence to pin it). A two-box guide sits by the questions: it cannot be answered yes or no; it points at a part of the text. The pin is keyed: each discussion's data lists the sentences that bear on its question. A pin from outside that list is turned back once with "How does that line help with today's question?"; a second miss lets it stand, tagged "off the question", and Priya challenges it in the talk.

**Set up.** Each talk opens with the table tent turned over. The student writes the group's goal in a frame ("By the end we will ..."), sees the limit (12 turns on a turn clock that counts down), sets the deadline (picks turn 6, 8 or 10 as the turn by which the goal must be met; it is flagged on the clock, and the goal frame becomes "By turn 8 we will ...") and takes a role card: Facilitator (must Invite twice), Evidence checker (must Probe twice), Note-taker (types one note after each classmate's idea; these feed the closing) or Timekeeper (must call "Halfway" at turn 6 and "Last two turns" at turn 10). The role changes every discussion, so over five the student holds each role and repeats one. A missed job shows on the closing card.

**Talk.** A discussion of 10 to 12 turns plays as speech bubbles from a branching script. At each of the student's turns, six move chips: Ask, Answer with evidence, Build on, Probe, Paraphrase, Invite. Each opens a frame ("So you're saying ___?", "Building on what Priya said, ___", "Omar, what do you think about ___?") with picked or typed words. The script branches by move, not by the words:
- Paraphrase hides the classmate's bubble. The student types what was said in their own words ("So you're saying ..."). Then three versions show and the student picks the one closest to what they typed: one is fair, one adds something the speaker did not say, one turns it around. A wrong pick brings a correction ("That's not what I meant. I said she was brave, not silly."), the bubble comes back, and "corrected" is kept on the closing card through any Replay. Each discussion calls for two paraphrases of different speakers.
- Probe ("What in the text makes you say that?") follows a classmate's claim. The classmate points to nothing; the student taps the sentence that backs the claim, or `Nothing backs it`. Keyed: of the two probes in a discussion, one claim has a backing line and one has none. A wrong tap can be tried once more; then Priya shows it and the probe is tagged "Priya found it".
- Answer with evidence and Build on take a typed sentence of eight words or more. A three-box guide: names the line or the idea it builds on; says what it shows; ties it to today's question. The tool cannot mark the words, so the model talk and the guide do that job, and the sentences print.
- Invite to Omar opens his idea: the watch and the hair were both the thing each person was proudest of, so each gave away a piece of who they were.
- Answer with evidence pulls the prep pin into the bubble; without a pin the student picks a line.
- Ask uses one of the prep questions if the student has one.
Two meters: On the question (drops when the talk wanders, for example if the student follows Maya's tangent about a movie) and Every voice in (rises when Omar speaks). Rule slips: if the student picks a move during Priya's unfinished bubble, the "one voice at a time" rule glows. If the student makes a claim with Ask or Build on and no line twice running, "back it up" glows and Priya asks for the line. If Omar has not spoken by turn 8, "everyone talks" glows. Slips are counted on the closing card.

**Closing.** The student first types the three key ideas of the talk from memory (the Note-taker's notes show; in other roles nothing shows). Then six idea cards appear, two of them off the question, and the student matches each typed idea to a card or to `not here`. Matching an idea to an off-question card says so and is kept on the card. Next the student writes two lines in frames, one each for two classmates: "{Priya} thought ___ because ___." Last, "Did your own view move? From ___ to ___, because ___" (or "It stayed, because ___"), whether the goal from Set up was met, and the move that opened the best moment. A guide for the written lines: says their idea fairly; gives their reason; no put-downs. `Replay` runs the same discussion with a different first move and a different role.

**Class tracker.** A projector view for a real class discussion: names typed by the teacher (kept only while the page is open), a tap tally for who has spoken, move stems on the side, a goal line and a talk timer. `Pairs card` prints or shows a half sheet for two real students: one of the five questions, the six move stems, and a tally where each ticks the moves the partner made and writes one paraphrase of the partner's best point.

At 1366x768 the table and bubbles fit; at 680x425 the prep card is a tab.
**Deadline check.** At the turn the student chose, the talk stops and the goal card comes up: "Deadline. Have we met the goal?" The student taps `Yes` or `Not yet` and types one line saying what shows it. On `Not yet` the student picks what the group does with the turns left (stay on the goal, or go to one named question). The goal, the deadline and the answer print on the closing card. Turns are counted; nothing is timed.

**On your own.** The fifth discussion, "Is it fair to grade a discussion?", runs with no help: `Listen in`, the guides and the move hint are closed, the frames are hidden, each probe and each paraphrase takes one answer, and nothing is marked until the closing is in.

**The end.** A results strip for the teacher on the fifth discussion, part by part: SL.6.1a, the pin on or off the question and both probes; SL.6.1b, goal written, deadline set and checked, role job done, rule slips; SL.6.1c, moves used and typed turns; SL.6.1d, paraphrases matched and the closing. Then the counts for the four talks before.

## Content
- Story: O. Henry, "The Gift of the Magi", in "The Four Million" (1906; first printed 1905), Project Gutenberg eBook #7256, full text.
- Issue page, written for Curio Class and labeled so: two short views on who should choose a group's books and two on grading discussions, with no real people or schools named.
- Model talk: six turns on "The North Wind and the Sun" (Aesop, V. S. Vernon Jones translation, 1912, public domain).
- Five branching discussions written for Curio Class, each with 5 student turns and 3 to 4 branches per turn; every branch rejoins within two turns. Each has in data: the sentences that bear on its question (for the pin), two probe claims (one backed, with its line; one not), two paraphrase points with three versions each, six closing idea cards (two off the question).
- Members' voices and personalities set in data; each has one idea that only comes out with the right move.
- What a wrong answer in the fifth discussion means: a pin off the question means the prep was about the text in general and not today's question; tapping a backing line for the probe that has none means the student takes a firm voice for evidence; a paraphrase that adds the student's own view means listening and answering are not yet apart; a deadline check of `Yes` with no line to show it means the goal was not being watched.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The script waits for the student's turn; classmates' bubbles play in order and wait for each other.
- No move is wrong; moves change what happens, and the meters show it.
- With Motion off bubbles appear without sliding.
- The deadline is a turn number, never a time. The student can take as long as they like on any turn.
- Access: every action works by tap and by keyboard. The pin is a tap or Enter on a sentence. Each move chip has a picture and a word, rule slips are named in words beside the glow, and speakers are named on every bubble, never color alone. Motion can be paused. Everything spoken is also on screen.
- On your own: one answer for each probe and paraphrase, no feedback until the closing is in.

## Look
- Accent `--brand` #a34a12 pumpkin (header, table edge, move chips); gold #f4c542 (meters, the pinned line); paper #fcf5f0; ink #2a1206; muted #66544a. Scene: a warm school library corner in autumn.
- Contrast (WCAG 2.1, computed): white on brand 5.92:1; brand on paper 5.49:1; ink on paper 16.38:1; muted on paper 6.64:1; ink on gold 10.87:1.
- Never color alone: meters show words and numbers; chips have icons and words.
- Different from this batch (sky blue, storm violet, granite green, museum burgundy).

## Art
- People art goes to Gemini: Maya (a white girl about 12, curly red hair, talking with her hands), Priya (an Indian American girl about 12 with glasses and a notebook), Omar (a Somali American boy about 12, sketchbook, quiet smile), 4 poses each (talk, listen, think, laugh); "illustrated middle school classmate <description> <pose>, warm gouache, plain white background"; 1:1; cutout yes. Story scenes: Della at the window, the comb and the watch chain (2); 4:3.
- Local FLUX (`scripts/localart.py`): library table (1).
About 15 images. Drawn in code: bubbles, chips, meters, table tent.

## Voice
Classmates: Maya `playful-friend`, Priya `big-sister`, Omar `casual-peer`; the story is read by `warm-teacher`. Each is unique in this batch. No host; hints are read by the story voice. `Curio.voice` with `scope: () => state.view + ':' + state.turn`, `welcomeAfter: true`.
- how `welcome`: "You're the fourth seat. Read the story and jot two questions; then we'll talk."
- event, whole, `bubble`: each classmate's bubble in their voice.
- how `moveHow`: "Your turn. Pick a move: ask, answer with evidence, build on, paraphrase, or invite someone."
- event `correct`: Maya: "That's not what I meant. I said {she was brave, not silly}."
- event `omar`: Omar's idea, in his voice.
- event `ruleSlip`: "One voice at a time. Let Priya finish."
- how `closingHow`: "Type the three biggest ideas from the talk. Then match them to the cards."
- how `setupHow`: "Write the group's goal. Then take your role card."
- how `probeHow`: "Tap the line that backs it up, or tap Nothing backs it."
- how `sayBack`: "Type what {Maya} just said, in your own words."
- event `backItUp`: Priya: "Which line says that?"
- event, whole, the model talk, each voice in turn.
Read speaks the hint, which names the next action and control and never a disabled one.
- how `deadline`: "Pick the turn when the goal must be met."
- how `own`: "This talk is on your own. No hints this time."
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
None. Tool-only code: branching discussion script, move chips and frames, two meters, closing card, class tracker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Prep pin | Pin the first sentence | The pin is keyed to the question; a second miss is tagged and challenged in the talk. |
| Moves | Always pick Ask | The meters stall, "back it up" glows, the role's job goes undone and Omar's idea never appears; all of it shows on the closing card. |
| Probe | Tap lines until one sticks | One of the two claims has no backing line at all; one retry, then it is tagged "Priya found it". |
| Paraphrase | Pick any version | The bubble is hidden and the student types first; two of three versions are wrong, and "corrected" stays on the card through Replay. |
| Typed turns | Type filler | Eight words are the only test the tool can make; the guide and the printout carry the rest, and a teacher sees the words. |
| Closing | Pick any three ideas | Ideas are typed before the cards show; matching to an off-question card is recorded. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. First visit: the model talk (whole). Tap Prep: "Prep", `welcome` (queued, first time).
2. Talk: `setupHow`; `bubble`s in order (each waits); at the student's turn, `moveHow` (first time); `probeHow` and `sayBack` with their moves.
3. Branches: `correct`, `omar`, `ruleSlip`, `backItUp` as they fire.
4. Closing: `closingHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SL.6.1 (a to d) wording | thecorestandards.org, Speaking and Listening Grade 6 | CCSS ELA 2010 PDF | yes |
| "The Gift of the Magi" by O. Henry, 1905, public domain | Project Gutenberg eBook #7256 (checked 2026-11-09) | Library of Congress, O. Henry and "The Four Million" catalog record | yes |
| Accountable talk moves (asking for evidence, building on, paraphrasing, inviting others) support productive discussion | TERC and Michaels, O'Connor and Resnick, "Accountable Talk" sourcebook (University of Pittsburgh) | Reading Rockets, discussion strategies | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): the two meters; the branching script.

Checks run (Python, scratchpad b16, 2026-11-09): every branch of the sample script rejoins within two turns, and Omar's idea is reachable only through Invite; contrast as in Look.

Spec fix checks (2026-11-10): counted, not run: five discussions with two probes and two paraphrases each give ten of each; four roles over five talks means each is held at least once; the Timekeeper's calls at turns 6 and 10 fall inside the 12-turn limit. The branching check above covered the first two scripts only; the three new scripts must pass the same check at Build. The full story's word count (about 2,100) and the Vernon Jones fable were not reopened in this pass.

## Done when
1. Focus and fold: at 1366x768 the table and bubbles fit; at 680x425 prep is a tab.
2. Prep takes two questions and a pin keyed to the question; they light when used; each talk has two probes, one with a backing line and one without. (SL.6.1a)
3. Each talk opens with a written goal, a 12-turn clock, a deadline the student sets and checks, and a role whose job is checked; three kinds of rule slip glow and are counted. (SL.6.1b)
4. Six moves branch the talk; answers and build-ons are typed sentences; Invite brings Omar in. (SL.6.1c)
5. Paraphrases are typed with the bubble hidden before the versions show; the closing takes typed key ideas, two classmates' views and the student's own. (SL.6.1d)
6. Five discussions on two texts are present; the model talk plays first and can be reopened.
7. The class tracker tallies speakers and keeps nothing after the page closes; the pairs card prints.
8. Print shows the prep and closing cards with typed turns and any tags.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: bubbles don't slide; no network requests.
11. The fifth discussion runs with no model, guide, hint or frame and one answer for each probe and paraphrase; the end screen shows the result for each of SL.6.1a, b, c and d. (SL.6.1)
12. Every spoken line is also on screen; each key word shows with an example at first use; the sentence frames can be left.
13. Every action works by keyboard as well as tap, nothing is shown by color alone, nothing is timed, and motion can be paused.

## Open questions
- None for Cory.
