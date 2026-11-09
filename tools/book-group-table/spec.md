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
- Driver: one student (tool.json `driver: "student"`). Every bubble and sentence is read on tap. Class mode: a projector tracker for a real discussion.
- One story, two discussions: "What did each gift really cost?" and "Were they wise or foolish?". tool.json `modes: ["My seat", "Class tracker"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the prep card and the closing round. The class tracker keeps counts only while the page is open.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SL.6.1a | Prep: read the story, jot two questions and pin one line of evidence; then use them in the talk | the prep card, and its items lighting when used | 2 |
| SL.6.1b | Follow the three group rules (one voice at a time, back it up, everyone talks); the meter shows when a rule slips | the table tent and the meter | 3 |
| SL.6.1c | Pick a move each turn: ask, answer with evidence, build on, paraphrase, invite; the next bubbles change by the move | the bubbles and the move chip | 4 |
| SL.6.1d | Closing round: review the key ideas, say whether anyone changed their mind, and name the move that opened the best moment | the closing card | 5 |

## Screens and modes
Header (kit): title "Book Group Table"; `Prep`, `Talk`, `Closing`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A library table with four chairs, a table tent of rules and three classmates already seated: Maya (quick, confident, talks first), Priya (careful, asks for proof) and Omar (quiet, sketches in the margin). First hint: "Tap Prep to read the story." The first tap reads "Prep"; the welcome is queued after it (`welcomeAfter: true`).

**Prep.** O. Henry's "The Gift of the Magi" (1905), lightly abridged to about 1,300 words with each cut marked, in numbered sentences (tap to hear). A glossary strip (pier-glass, fob, Magi). The prep card: two question boxes and one evidence pin (tap a sentence to pin it).

**Talk.** A discussion of 10 to 12 turns plays as speech bubbles from a branching script. At each of the student's turns, five move chips: Ask, Answer with evidence, Build on, Paraphrase, Invite. Each opens a frame ("So you're saying ___?", "Building on what Priya said, ___", "Omar, what do you think about ___?") with picked or typed words. The script branches by move, not by the words:
- Paraphrase offers three versions of what Maya just said; one gets her wrong, and Maya corrects it ("That's not what I meant. I said she was brave, not silly.").
- Invite to Omar opens his idea: the watch and the hair were both the thing each person was proudest of, so each gave away a piece of who they were.
- Answer with evidence pulls the prep pin into the bubble; without a pin the student picks a line.
- Ask uses one of the prep questions if the student has one.
Two meters: On the question (drops when the talk wanders, for example if the student follows Maya's tangent about a movie) and Every voice in (rises when Omar speaks). Rule slips: if the student picks a move during Priya's unfinished bubble, the "one voice at a time" rule glows.

**Closing.** Three key ideas to pick from six (two are off the question), a "changed my mind?" line for each member and the student, and the move that opened the best moment. `Replay` runs the same discussion with a different first move.

**Class tracker.** A projector view for a real class discussion: names typed by the teacher (kept only while the page is open), a tap tally for who has spoken, move stems on the side, and a talk timer.

At 1366x768 the table and bubbles fit; at 680x425 the prep card is a tab.

## Content
- Story: O. Henry, "The Gift of the Magi", in "The Four Million" (1906; first printed 1905), Project Gutenberg eBook #7256, abridged with cuts marked.
- Two branching discussions written for Curio Class, each with 5 student turns and 3 to 4 branches per turn; every branch rejoins within two turns.
- Members' voices and personalities set in data; each has one idea that only comes out with the right move.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The script waits for the student's turn; classmates' bubbles play in order and wait for each other.
- No move is wrong; moves change what happens, and the meters show it.
- With Motion off bubbles appear without sliding.

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
- how `closingHow`: "Pick the key ideas. Did anyone change their mind?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: branching discussion script, move chips and frames, two meters, closing card, class tracker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Moves | Always pick Ask | The meters stall and Omar's idea never appears; the closing round asks which move opened the best moment. |
| Paraphrase | Pick any version | The wrong version brings a correction from Maya. |
| Closing | Pick any three ideas | Two of six are off the question and say so when picked. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Prep: "Prep", `welcome` (queued, first time).
2. Talk: `bubble`s in order (each waits); at the student's turn, `moveHow` (first time).
3. Branches: `correct`, `omar`, `ruleSlip` as they fire.
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

## Done when
1. Focus and fold: at 1366x768 the table and bubbles fit; at 680x425 prep is a tab.
2. Prep pins and questions light when used. (SL.6.1a)
3. Rule slips glow and the meters move. (SL.6.1b)
4. Moves branch the talk; the wrong paraphrase gets corrected; Invite brings Omar in. (SL.6.1c)
5. The closing card takes ideas, changed minds and the best move; Replay works. (SL.6.1d)
6. The class tracker tallies speakers and keeps nothing after the page closes.
7. Print shows the prep and closing cards.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: bubbles don't slide; no network requests.

## Open questions
- None for Cory.
