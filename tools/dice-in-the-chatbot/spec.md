# Dice in the Chatbot

## One idea
Send the same message to two chatbots side by side: Rulebot gives the same answer every time because it follows written rules, while Nextword, a tiny next-word predictor trained on 20 sentences about a school astronomy club, rolls weighted dice for every word, so its answer changes with each send; turn its randomness dial to 0 and it freezes into one answer ("bring" becomes "a good first ."), fix its dice seed and even the "random" answers repeat, and what you measure becomes your evidence in a debate on whether either one understands, feels or can be blamed.

## Not like
- ai-evaluator (9-12, ml-lab): tests a classifier's accuracy on photos. Here nothing is classified or scored; the object is how a text generator picks words, and whether that is understanding.
- spot-the-ai (grade 1): is this made by AI or a person? Here you open both machines and measure them.
- teach-the-robot, biased-bot, leaf-sorter-ai, model-mechanic (ml-lab): training data shapes a classifier. Here the model's training text is fixed and fully visible; the lesson is randomness and meaning.
- sorting-showdown (9-12 CS): deterministic algorithms raced on speed. Here a deterministic and a probabilistic algorithm answer the same input, and the measure is how often the output changes.
- simulation-studio (9-12, data desk): seeded simulation of a geyser. Here the seed is the reveal: the chatbot's "randomness" is a deterministic generator underneath.
- coin-cell-greenhouse, pull-request-review (this group): code limits and AI-written code. This tool is about AI-written text and what it does and doesn't know.

## Who and how
- Grades 9 to 12, computer science. Module: Minds and Machines (Computing and Society), "Deterministic and probabilistic algorithms, and human versus machine intelligence". Topic line: "random and rule-based chatbots, and what machines understand".
- Driver: students on laptops, alone or in pairs. 25 to 40 minutes.
- Standards (module codes, CSTA 2026): HS-ALG-PS-04 (compare deterministic and probabilistic algorithms: Chat, Measure, Inside), HS-SOC-HU-44 (human versus machine intelligence: Debate). CSTA 2017 crosswalk: 3B-AP-08 (describe how artificial intelligence drives many software systems), 3B-AP-11 (evaluate algorithms in terms of efficiency, correctness and clarity), 3A-IC-24 (evaluate how computing impacts social practices).
- tool.json: driver "students", minutes "25-40", modes ["Chat", "Measure", "Inside", "Debate"], grades_label "Grades 9-12". Kit starter, `kit:theme-912`.

## Screens and modes
Header (kit): "Dice in the Chatbot", small line "Two bots, one question". Modes: **Chat** (first), **Measure**, **Inside**, **Debate**. Motion, Sound, Read.

Panel in Chat, Measure and Inside: **Randomness** slider 0 to 1.5, step 0.1, default 1.0, with the number shown and the words "0: always the likeliest word" under it; **Dice seed**: **New each send** (default) or **Fixed: 7** (a two-button switch); **Training text** button (opens a drawer with all 20 sentences and the word count table for any word tapped).

### Chat
Focus: the two reply columns, side by side and filling the stage, so the same message's two answers sit level with each other. The painted night field (Art) sits dimmed behind them; each window's header carries its bot's painted avatar.
Stage: two chat windows side by side (stacked under 760 px), each with its name and a one-line "How I work": **Rulebot** ("I check my 6 rules from the top. The first rule that matches picks my reply.") and **Nextword** ("I continue your message one word at a time. Each word is a weighted dice roll."). One message box under both, **Send**, and prompt chips: "when does the club meet", "what should I bring", "is the moon bright", "tell me about saturn", "do you like the stars", "are you sure". Typing is allowed (letters, numbers and spaces, up to 60 characters); messages live only in the page.
Each Rulebot reply shows a small tag "Rule 2" (tap: the rule highlights in a rules drawer). Each Nextword reply shows the start word in muted ink, then the generated words; tap the reply to open it in Inside.
**Send 5 times** button: sends the current message five times to both bots, so the difference shows at once. The five replies land 250 ms apart (about 1.3 s); any tap while they land (Send, a chip, the slider, a mode) places the rest at once and then acts. Nextword's avatar shows its rolling pose while a reply is being placed, then returns to idle; Rulebot shows its card pose when a rule fires and idle on "No rule".

### Measure
Focus: the result table's bars for the current message, the largest thing on the stage; the Sweep chart takes its place once run (a tab switches back).
Stage: a lab sheet. Top: message picker (the six chips or the last typed message) and **Run 20**, **Run 100**. Result table, one row per distinct reply: reply text, count, share, a bar; separately for Rulebot and Nextword. Readouts: "Distinct replies: Rulebot 1, Nextword 9", "Most common reply share". Below: **Sweep** button: runs 100 sends at each Randomness 0, 0.5, 1.0, 1.5 and draws a chart of distinct replies (y) against Randomness (x), Rulebot as a flat line at 1, Nextword as points. **Save to evidence** stores the current table as an evidence card for Debate (up to 6 cards, in the page only).

### Inside
Focus: the dice for the selected step (its bars and the 0 to 1 strip), centered and largest; the reply's words run above it as a row of steps.
Stage: the last Nextword reply laid out word by word. Under each step, the dice for that step: a bar for every word that ever followed the current word in the training text, with its count and its chance at the current Randomness; the picked word's bar outlined, and the dice number u (0 to 1) that picked it marked on a 0 to 1 strip of the stacked bars. **Step** walks one word at a time; **Roll again from here** rerolls from the selected step. Moving the Randomness slider redraws the chances live (the reply is not regenerated until Roll again). Rulebot's side panel shows its six rules and which one fired.

### Debate
Focus: the three columns of the claims board, with the tray of unplaced claims along the bottom.
Stage: a claims board with three columns, **Our data supports it**, **Our data argues against it**, **This lab can't tell**. Eight claim cards (Content) start in a tray. Drag (or select, then tap a column) each claim into a column, then attach evidence: tap **Add evidence** on a placed claim and pick from the evidence cards (saved Measure tables, plus four built-in cards: "Rulebot's rules", "Nextword's training text", "The Fixed: 7 run", "Inside: the dice at 'bring'"). The board never marks a column right or wrong; each claim has a **What others noticed** button that shows one or two lines of reasoning (Content) after the student has placed it. **Copy board** puts the claims, columns and evidence as text on the clipboard.

## Content
Rulebot rules (checked in order on the lowercased message split into words; first match wins):
1. a word is "hello" or "hi" → "Hi! I answer questions about the Night Sky Club."
2. "when" and ("meet" or "meets") → "The club meets Friday nights at the field, or in Room 12 when it rains."
3. "where" → "We meet at the field. If it rains, Room 12."
4. "bring" → "Bring a red light and a warm coat."
5. "saturn" → "Saturn is up after ten in the fall."
6. "join" → "New members can join on any Friday."
No match → "I don't have a rule for that. Try asking when, where or what to bring." (shown as "No rule").

Nextword training text (lowercase, words split on spaces, "." is a word):
the club meets on friday nights at the field . / the club meets on clear nights at the field . / the club meets in room 12 when it rains . / the moon is bright on clear nights . / the moon is full on friday . / the moon is a good first target . / the telescope is in room 12 . / the telescope is heavy so two people carry it . / we look at the moon first . / we look at saturn when it is up . / we look at the stars after the moon sets . / saturn has rings you can see in the telescope . / saturn is up after ten in the fall . / bring a red light and a warm coat . / bring a snack for the break . / new members can join on friday . / new members can borrow a telescope . / it rains a lot in the spring . / clouds can cancel the night . / the stars are faint when the moon is bright .
(20 sentences, 169 words, 64 different words.)

Model: count every pair of neighbors (word, next word) inside each sentence. Start word = the last word of the message that is in the training text and is not "."; if none, "the". Then repeat: the candidates are every word that followed the current word, in alphabetical order ("." sorts first); weight = count^(1/R) for Randomness R > 0; chance = weight / sum; draw u from the generator, walk the cumulative chances in candidate order, take the first word whose cumulative chance exceeds u. At R = 0 take the highest count; on a tie take the first in alphabetical order. Stop after "." or after 12 words (then show "..." ). Generator: mulberry32 (the same code as simulation-studio); New each send seeds it from the send counter plus 1000 (send 1 uses seed 1001); Fixed: 7 seeds 7 before every send.

Checked counts and chances (from the text above):
- after "meets": on 2, in 1. Chances at R 1.0: on 2/3, in 1/3; at R 0.5: on 0.80, in 0.20; at R 1.5: on 0.614, in 0.386.
- after "on": friday 3, clear 2 (R 1.0: 0.6 and 0.4). After "friday": "." 2, nights 1. After "the": moon 6, club 3, telescope 3, field 2, stars 2, break 1, fall 1, night 1, spring 1. After "a": good, lot, red, snack, telescope, warm, 1 each. After "bright": "." 1, on 1.
- R = 0 replies: "when does the club meet" (start "club") → "meets on friday ."; "what should I bring" → "a good first ."; "do you like the stars" → "after ten in the moon is bright ."; "is the moon bright" → "." only (shown as "(nothing more)"); "tell me about saturn" → "has rings you can borrow a good first ."; "are you sure" (start "you") → "can borrow a good first .".
- R = 1.0, start "club": the reply "meets on friday ." has chance 2/3 x 3/5 x 2/3 = 4/15, about 26.7 percent; "meets on clear nights ." 8.9 percent; "meets in room 12 ." 6.7 percent. About 15 percent of replies reach the 12-word cap. More than 2,000 different replies are possible (2,233).
- Seeded runs (mulberry32, seeds 1001 to 1100, "when does the club meet"): at R 1.0, "meets on friday ." comes 30 times of 100 and there are 48 distinct replies. Sweep, distinct replies at R 0, 0.5, 1.0, 1.5: 1, 39, 48, 46 ("what should I bring": 1, 56, 56, 54). The count does not always rise with R, because at high R more replies run to the 12-word cap and some long ones repeat; the chart's text alternative says so. Fixed: 7 at R 1.5 gives "meets in the spring ." every time.
- R = 1.0, start "bring": "a warm coat ." 16.7 percent; "a good first ." 8.3 percent.
- Nextword can say things nobody wrote: "meets in the field ." (2.0 percent at R 1.0) appears nowhere in the training text.

Claims (Debate), each with its "What others noticed":
1. "Nextword understood my question." Noticed: "It never reads the question. It starts from one word and continues the text it was trained on."
2. "Rulebot understood my question." Noticed: "It matched a word to a rule a person wrote. Change the wording and it misses."
3. "Nextword chooses its words on purpose." Noticed: "Inside shows a dice roll for every word. At Fixed: 7 the same rolls give the same words."
4. "Nextword is truly random." Noticed: "Its dice come from a formula. Same seed, same answer."
5. "Nextword copies its training text." Noticed: "Each pair of words comes from the text, but it can join them into sentences nobody wrote."
6. "Rulebot is more trustworthy." Noticed: "It never makes things up, but it only knows six things."
7. "If Nextword gives a wrong meeting time, Nextword is responsible." Noticed: "The people who trained it and the people who put it in front of students chose to use it."
8. "Bigger chatbots work the same way, just bigger." Noticed: "Large language models also pick the next piece of text by chance from learned weights, but they learn far richer patterns than word pairs. This lab can't measure that."

## Interactions in detail
- Rulebot is deterministic; Nextword at R = 0 is deterministic; at R > 0 with New each send it varies; with Fixed: 7 every send repeats exactly. Measure shows this directly: Rulebot 1 distinct reply always; Nextword 1 at R 0; with Fixed: 7, 1 at any R.
- Sweep always uses New each send seeds 1001 to 1100 for each R so it reproduces; the chart's numbers are listed in its text alternative.
- Typed messages with no known word: Rulebot "No rule", Nextword starts at "the". Empty message: Send is disabled.
- Changing Randomness during Measure clears the table ("Settings changed: run again").
- Inside with no reply yet shows "Send a message in Chat first" and a **Go to Chat** button.
- Debate: a claim can move between columns freely; evidence can be removed (x). Copy board works with any number placed. Nothing is saved after the page closes.
- Keyboard: modes, panel, message box, chips, then replies; Debate cards movable with Enter and arrows. Visible focus.
- Sizes: both chat windows, the message box and Send fit without scrolling at 1366x768 and 1280x720; at 680x425 the two windows sit side by side at half width with the last three replies each. Text in chat bubbles at least 14 px.

## Look
- Accent `--brand #36d6e7` (signal cyan: Send, the Randomness thumb, the picked-word outline, the header rule) with `--brand-ink #062126`, on `kit:theme-912`.
- Rulebot bubbles `#232d3b` with a square-cornered "rule" tag; Nextword bubbles `#1d2a33` with a die glyph; dice bars `#8a9bb3`, picked bar outlined in brand with a ▲.
- Contrast (computed): brand on `--panel` 9.83:1, on `--sec-bg` 9.32:1; brand-ink on brand 9.52:1; bubble text `#e8edf3` on `#232d3b` about 12:1. All pass AA. The picked word is outlined and marked, never color alone.
- Neighbors: ai-evaluator and capture-the-flag pink, sorting-showdown violet, api-playground lemon, network-architect sky blue (#7cc4ff; cyan here is greener and brighter), simulation-studio orange.

## Art
Local FLUX (`scripts/localart.py`), no people. One style: soft painted illustration, deep night blues with cyan light.
- night-field: "A school sports field at night under a starry sky, a telescope on a tripod beside a folding table with a red flashlight and a thermos, deep blue tones, painted illustration"; 16:9; cutout no; people no; dimmed behind the Chat windows and on preview.svg.
- rulebot-idle: "A friendly boxy robot built from a grey metal filing cabinet with a closed drawer, two round lamp eyes and short arms, painted illustration, plain white background"; 1:1; cutout yes; people no; Rulebot's avatar, idle and on "No rule".
- rulebot-card: same robot "with its top drawer open, holding up one blank index card"; 1:1; cutout yes; people no; Rulebot's avatar when a rule fires, and beside its rules in Inside.
- nextword-idle: "A small round friendly robot with a clear glass dome full of colorful dice, soft cyan lights and stubby arms, painted illustration, plain white background"; 1:1; cutout yes; people no; Nextword's avatar.
- nextword-roll: same robot "tossing two dice into the air with both arms raised"; 1:1; cutout yes; people no; Nextword's avatar while a reply is placed.
Chat bubbles, dice bars, the 0 to 1 strip, tables, the Sweep chart, the claims board and its cards are drawn in code (text, charts and controls).
## Voice
Bank voice `big-sister` (Leda), style "Say in a friendly, youthful way, like a helpful older student": an older student running the lab with you. Not used by a 9-12 CS tool or a group sibling. Light narration, `Curio.voice`, `scope: () => state.mode`. Read speaks the hint. Bot replies are never spoken.
- w-chat (how, Chat welcome; stale on the first Send): "Tap a message chip, then press Send. Press Send again and see which bot changes."
- five (event, a Send 5 times where Nextword gives at least 2 different replies; stale after the next send): "Rulebot said the same thing five times. Nextword didn't."
- zero (how, first time Randomness is set to 0; stale when it moves off 0): "At zero, Nextword always takes the likeliest word. Press Send again."
- seed (event, Fixed: 7 is on and the same reply comes twice; stale after the next send): "Same seed, same dice, same answer. The randomness came from a formula."
- w-measure (how, Measure welcome; stale on the first run): "Pick a message, then press Run 100 and count the different replies."
- w-inside (how, Inside welcome with a reply; stale on the first Step): "Press Step to walk the reply one word at a time and see each dice roll."
- w-inside-empty (how, Inside welcome with no reply yet; stale once a reply exists): "There's no reply to open yet. Press Go to Chat and send a message."
- w-debate (how, Debate welcome; stale when the first claim is placed): "Drag each claim into a column, then press Add evidence on it."
## Family engine
none (the bigram model is small and lives in this tool; ml-lab is a classifier engine and is not used).

## Sources
- CSTA 2026 PK-12 Computer Science Standards: https://csteachers.org/2026-csta-pk-12-computer-science-standards/ ; CSTA 2017: https://csteachers.org/k12standards/
- Bigram (n-gram) language models and sampling: Jurafsky and Martin, "Speech and Language Processing", 3rd ed. draft, chapter 3 "N-gram Language Models": https://web.stanford.edu/~jurafsky/slp3/
- Temperature in sampling (weights raised to 1/T): same book, chapter on large language models (decoding and sampling).
- Rule-based chatbots: Weizenbaum, "ELIZA: A Computer Program for the Study of Natural Language Communication between Man and Machine", Communications of the ACM 9(1), 1966.
- Pseudo-random generators are deterministic from their seed: NIST SP 800-90A Rev. 1 (definitions): https://csrc.nist.gov/pubs/sp/800/90/a/r1/final
- The Night Sky Club, both bots and the training text are made up; all chances were computed from the text above.
- Checks run (Python, 2026-10-29, with a port of mulberry32 that gives 0.62707394 for seed 1, the JavaScript value): 20 sentences, 169 words, 64 different words; every neighbor count and chance in Content; all six R 0 replies; exact reply chances by enumeration (2,233 replies from "club" at R 1.0, 15.2 percent at the cap, "meets in the field ." 2.0 percent, "a warm coat ." 16.7 percent); the seeded Run 100 and Sweep numbers above. Done when 3's band 18 to 36 is about two binomial spreads (4.4) around 26.7; the seeded run gives 30. The draft's Done when said Nextword shows "more" at every R; the seeded counts are 39, 48, 46, so it now gives the exact numbers.

## Done when
1. "when does the club meet": Rulebot answers with Rule 2 every time; Nextword at R 0 says "meets on friday ." every time.
2. "what should I bring" at R 0: Nextword says "a good first ."; Inside shows six equal bars after "a".
3. Measure, start "club", R 1.0, Run 100 (seeds 1001 to 1100): Rulebot 1 distinct; "meets on friday ." 30 of 100 (any port of the rules lands between 18 and 36), 48 distinct.
4. Fixed: 7, Run 20 at R 1.5: Nextword 1 distinct reply.
5. Inside after "meets" at R 0.5 shows on 0.80 and in 0.20; at R 1.5, 0.614 and 0.386.
6. Sweep for "when does the club meet" draws Rulebot flat at 1 and Nextword at 1, 39, 48, 46, with the numbers in the text alternative.
7. Debate: every claim placeable; What others noticed appears only after placing; Copy board text lists evidence.
8. Chat windows, message box and Send fit without scrolling at 1366x768; the five line plays once per qualifying Send 5 times and not after other sends; no line names a disabled control (Send is disabled on an empty message).
9. Focus: at 1366x768 and 1000x625 the two reply columns (Chat), the result bars (Measure), the selected step's dice (Inside) and the three columns (Debate) are each the largest thing on the stage.
10. Tap while it plays: during Send 5 times, a chip, Send or the Randomness slider acts at once (the remaining replies land first, in order); during the Sweep draw-on, a mode switch or Run acts at once.

## Open questions
- [dice-in-the-chatbot] Claim 8 says large language models also sample the next piece of text from learned weights. Is that level of claim about real chatbots fine for this tool, or should Debate stay strictly inside what the lab measures?
- [dice-in-the-chatbot] Typed messages are allowed (60 characters, never saved). Keep, or chips only?
