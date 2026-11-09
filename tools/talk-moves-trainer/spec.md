# Talk Moves Trainer

## One idea
The student joins a four-person book group talking about a short story they all just heard, and at each pause chooses which move the talk needs right now (agree and add on, disagree politely, ask a question, connect two ideas, sum up) and then the phrase that does it, while the classmates react honestly (a good question gets a fuller answer, a reply that ignores the last speaker gets a puzzled look, repeating someone gets "Yes, that's what I said"), so they learn when each move helps a discussion and not just how it sounds.

## Not like
- counterpoint-frames (9-12, spec): one-on-one argument with counter moves, written replies. Here a group discussion about a story with joining moves.
- i-choose-because (K-2, spec): one spoken reason for a choice. Here a whole discussion with many turns.
- opinion-builder (3-5, spec): a written letter with reasons. Here spoken turns in a group.
- perspective-frames (6-8, spec, this batch): comparing speakers in writing. Here being one of the speakers.
- socratic-seminar-board (10, spec): maps a whole class seminar. Here one student learning the moves inside a small group.

## Who and how
- Grades 3 to 5, English Language Development with Speaking and Listening, module "Academic Conversations". Standards: WIDA ELD-SI (Standard 1, language for social and instructional purposes), SL.3.1, SL.4.1, SL.5.1.
- Driver: one student; class mode is "Fishbowl", where the projector shows the group and the class calls out the move before the student picks (tool.json `driver: "student"`). Every line, story sentence and phrase is read on tap.
- Grade setting (3, 4, 5) adds that grade's discussion goals; Help setting Lots (three phrases per move), Some (frames with a blank), Little (move only, the student types the turn). Teacher notes map help to WIDA 1-2, 3-4 and 5-6. tool.json `modes: ["Book group", "Move cards", "Fishbowl"]`, `minutes: "15-25"`, `grades_label: "Grades 3-5"`.
- Nothing is saved; `Print` prints the talk map and the student's summary.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SL.3.1a, SL.4.1a, SL.5.1a (come prepared) | Hear the story first and point to the part that backs a turn | the story strip with the tapped sentence | 2 |
| SL.3.1c, SL.4.1c, SL.5.1c (ask and answer questions, link comments) | Choose ask or connect when the talk needs it | the classmate's fuller answer; the link on the talk map | 3 |
| SL.3.1b, SL.4.1b, SL.5.1b (agreed-upon rules, respectful disagreement) | Disagree politely with a reason | the classmate's reaction | 3 |
| SL.3.1d, SL.4.1d, SL.5.1d (explain own ideas in light of the talk; draw conclusions) | Sum up the key ideas and say how your thinking changed | the closing summary | 4 |
| WIDA ELD-SI (social and instructional language) | Pick the phrase that fits the move and the moment | phrase choices with when-to-use lines | 3 |

## Screens and modes
Header (kit): title "Talk Moves Trainer"; `Book group`, `Move cards`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A round table in a reading corner with four classmates and an empty chair for the student: Ana (the group leader this week), Malik, Hye-jin and Tomás. A story card sits in the middle: "The Saturday Garden". First hint: "Tap the story card to hear the story." The story plays (about three minutes, with pictures), and the welcome is queued after it (`welcomeAfter: true`).

**The story.** "The Saturday Garden", written for Curio Class: Lena would rather play soccer than help at her grandmother's community garden. One Saturday she leaves early, and that night a storm knocks down the bean poles. The next week she comes back, fixes the poles with a neighbor, and finds out the beans feed the food pantry. The story leaves room to disagree: was Lena wrong to leave, and why did she come back?

**Book group.** Ana asks a question and the talk runs in turns. At each pause (about eight per discussion) the student first picks a move from five cards: Agree and add on, Disagree politely, Ask a question, Connect ideas, Sum up. Then they pick or build the phrase ("I agree with Malik, and I want to add that...", "I see it differently because...", "Can you say more about...?", "That connects to what Hye-jin said about...", "So far we've said..."). The classmates react to what the moment needed:
- a question when someone said something unclear gets a fuller answer;
- a reply that ignores the last speaker gets a puzzled look and "Wait, what about what I said?";
- repeating the last speaker gets "Yes, that's what I said";
- a disagreement without a reason gets "Why do you think that?";
- a summary too early gets "But we just started!"
Two discussion questions per session; the second is chosen by where the talk went.

**Closing.** The student sums up the key ideas and finishes "At first I thought ___, but now I think ___ because ___." A talk map shows the student's turns as arrows connecting the people they answered.

**Move cards.** Each move with its phrases, when to use it, and a short example from the group; tap to hear.

**Fishbowl.** On the projector, the class calls the move at each pause before the student picks.

At 1366x768 the table and choices fit; at 680x425 the story strip is a tab.

## Content
- The story, two discussion scripts with branches, phrases and classmate reactions written for Curio Class.
- Grade goals: grade 3 adds "ask to check you understood"; grade 4 adds "pose a specific question"; grade 5 adds "draw a conclusion" in the summary.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A move can be changed before the phrase is chosen; the group waits at each pause with no timer.
- With Motion off faces change without animation and the talk map draws arrows without the line moving.

## Look
- Accent `--brand` #6a3d9a book-group purple (header, move cards, the table rug); gold #f4c542 (the student's chair, a good move); paper #f6f2fa; ink #1d0f2e; muted #5c5268. Scene: a cozy reading corner with a round table.
- Contrast (WCAG 2.1, computed): white on brand 7.64:1; brand on paper 6.92:1; ink on paper 16.38:1; muted on paper 6.64:1; ink on gold 11.13:1.
- Never color alone: reactions are faces with words; moves are labeled icons.
- Different from this batch (detective teal, earth red, town slate, highlighter olive).

## Art
- People art goes to Gemini: Ana (a Mexican American girl about ten), Malik (a Black boy about ten), Hye-jin (a Korean American girl about nine), Tomás (a white boy about ten who uses a wheelchair), 5 expressions each (neutral, thinking, nodding, puzzled, smiling); "illustrated fourth grader in a book group <expression>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): the reading corner with a round table (1); six story pictures, no faces (Lena seen from behind in each) (6).
About 27 images. Drawn in code: move cards, talk map, story strip.

## Voice
Bank voice `bright-teacher` as the hint voice and the story narrator (unique in this batch); Ana and Hye-jin are read by `playful-friend`, Malik by `casual-peer` and Tomás by `lively-host` (each unique in this batch). `Curio.voice` with `scope: () => state.question + ':' + state.pause`, `welcomeAfter: true`.
- how `welcome`: "You're part of the book group. When the talk pauses, choose the move it needs, then the words."
- event, whole, `story`: the story.
- event `turn`: a classmate's line.
- event `react`: the classmate's reaction to the student's move.
- event `use`: the move card's when-to-use line, after a pick that didn't fit.
- event, whole, `summary`: the student's summary.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
eld-talk (`kit/eld-talk.js`), described in full in tools/counterpoint-frames/spec.md. This tool uses: `Talk.phrase`, `Talk.highlight`, `Talk.pick` for moves and phrases, `Talk.frames` (adding two moves to the engine's list: connect, with frames such as "That connects to what ___ said about ___", and sum up, with "So far we've said ___"), `Talk.level` for help, `Talk.check` for typed turns at Little help, `Talk.run` for the branching discussion and `Talk.cast` for the four classmates. The story, the reactions table and the talk map are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Moves | Always pick Agree | Each pause is keyed to what it needs; agreeing with an unclear point gets "Wait, do you know what I meant?" |
| Linking | Pick a phrase without naming anyone | Connect and add-on phrases need the classmate's name and their idea. |
| Disagree | Disagree without a reason | "Why do you think that?" and the turn waits. |
| Summary | Repeat the last line | The summary needs ideas from at least two classmates and the student's own change. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the story card: `story` (whole), `welcome` (queued, first time).
2. Each pause: `turn` (waits); after the pick, `react`; `use` if the move didn't fit.
3. Closing: `summary` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SL.3.1, SL.4.1 and SL.5.1 wording, parts a to d | thecorestandards.org, Speaking and Listening grades 3, 4, 5 | CCSS ELA 2010 PDF | yes |
| WIDA 2020: Standard 1 is language for social and instructional purposes | WIDA ELD Standards Framework, 2020 Edition | WIDA, Key Language Uses: A Closer Look (2020) | yes |
| Talk moves (adding on, revoicing, asking for reasoning, agreeing and disagreeing) support classroom discussion | Michaels, O'Connor and Resnick, "Deliberative Discourse Idealized and Realized" (Studies in Philosophy and Education, 2008) | Chapin, O'Connor and Anderson, Classroom Discussions (Math Solutions, 2009) | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b27, 2026-11-09): every pause in both scripts has exactly one keyed best move; each wrong move at each pause has a written reaction; every branch reaches the closing; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 table and choices fit; at 680x425 the story strip is a tab.
2. The story plays before the talk, and turns can point to a story sentence. (SL.3.1a, SL.4.1a, SL.5.1a)
3. Each pause takes a move, then a phrase, and classmates react to the fit. (SL.3.1b-c, SL.4.1b-c, SL.5.1b-c, WIDA ELD-SI)
4. The closing summary and the talk map appear. (SL.3.1d, SL.4.1d, SL.5.1d)
5. Grade settings add their goals.
6. Help levels behave as in Who and how.
7. Move cards, Fishbowl and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no face animation or moving lines; no network requests.

## Open questions
- Home-language support: home-language glossaries for ELD frames (Cory's open question in RUNBOOK.md)? (default used: English only, with pictures and read-aloud)
