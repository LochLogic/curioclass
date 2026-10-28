# Counterpoint Frames
Renamed from: Argument Frames Pro

## One idea
In this debate you can't just repeat your side: every turn your classmate makes a point, and your reply only counts when it answers that point with a counter move (concede and counter, question the evidence, turn it around), so you tap the words you are answering, the frame wraps around them, and the frames fade round by round until the last turn is yours alone.

## Not like
- argument-builder-pro (ela 9, evidence family): builds a written outline for both sides from an evidence pack. Here a live spoken debate, turn by turn, with WIDA language frames by level; the titles differed by one word, so this tool is renamed (overlap note, taken).
- talk-moves-trainer (eld 3-5, eld-talk, not built): agree, disagree and add on with animated classmates, choosing the polite phrase. Here the moves are argument moves (concede and counter, question evidence, turn it around), the student writes the reply, and it must answer a specific point.
- i-choose-because (eld K-2, eld-talk, not built): pick one of two pictures and say why. Here a whole debate with a claim, three counters and a close.
- classroom-phrases-game (eld K-2, eld-talk, built): everyday classroom phrases. Same engine pieces (word-by-word light-up, "your turn" echo), academic content.
- socratic-seminar-board (ela 10): maps a whole class discussion. Here one student against one classmate, with frames.
- opinion-builder (eld 3-5, not built): an opinion with because and so. Here opinions meet a counterargument every turn.

## Who and how
- ELD grades 9 to 12. Module: Academic Argument (Language for Language Arts).
- Driver: a student alone against a made-up classmate; **Two players** lets two students at one laptop debate each other with the same frames. 20 to 30 minutes (one debate about 10).
- Standards: WIDA.ELD-2 (Language for Language Arts) through debate on four issues, in writing and aloud; WIDA.Argue taught in full: state a claim with a reason, answer a counterclaim with concession and rebuttal, question evidence, add reasons, and close by weighing both sides ("Although ___, ___ because ___").
- Help setting: **Lots of help**, **Some help**, **Little help** (WIDA levels 1-2, 3-4, 5-6 in teacher notes), and a switch **Fade as I go** (on by default): frames step down one level each round from the chosen start.
- Speaking without a microphone: after each turn, **Say it** lights the student's reply word by word and counts "Your turn: 3, 2, 1", and the student says it aloud, to a partner or alone. Nothing is recorded.
- Topic line: "academic argument language".
- tool.json: driver "students", minutes "20-30", modes ["Debate", "Move cards"], grades_label "Grades 9-12". Kit starter plus `kit:eld-talk`.

## Screens and modes
Header: title "Counterpoint Frames"; mode buttons **Debate** (opens first), **Move cards**; Motion, Sound, Read. Panel: Help setting, Fade as I go, Two players, hint, tip.

### Debate (opens first)
- Topic picker: four cards (see Content). Then **Pick your side**: two buttons with the side's claim.
- Stage: a small debate stage. Left podium **You** (or Player 1); right podium **Jordan** (a classmate; Player 2 in Two players); center back, the moderator **Ms. Lin**. Under the stage, the transcript: every turn as a card, newest at the bottom.
- Rounds (the round strip shows 1 to 5, each with a word): **1 Opening**, **2 Counter**, **3 Counter**, **4 Counter**, **5 Closing**.
  - 1 Opening: the student states the claim and one reason. Reason chips (three per side) or typed.
  - 2 to 4 Counter: Jordan makes a point (card appears, read aloud). The student taps the words they are answering in Jordan's card (they light and drop into the frame as a quote chip), picks a move card (**Concede and counter**, **Question the evidence**, **Turn it around**, **Add a reason**), and completes the frame. **Check** shows three ticks, each a word plus ✓ or ○: **Answers Jordan's point**, **Uses a counter move**, **Gives a reason**. **Submit** is allowed with any ticks; ○ items get one line of help first, then Submit goes through on the second press.
  - 5 Closing: "Although [their best point], I still believe [claim] because [reason]." Jordan's best point is any of the three, tapped.
- Frames by level (see Content): **Full frame** (sentence with blanks and a word bank of chips), **Starter** (first words only, word bank behind **Words**), **Open** (a text box and a **Help** button that shows the starter for this move, never counted against the student).
- After each Submit: **Say it** (light-up and echo), then Ms. Lin's one-line note on the move used ("You conceded a fair point and still answered it.") and the next round.
- End: the transcript with the moves used per round, **Read the debate** (both sides, alternating), **Copy transcript**, **New debate**. No winner is declared; Ms. Lin names the strongest turn by the checks ("Your round 3 answered Jordan's exact words and gave a reason.").

### Move cards
- Eight cards, each a move with its frames at three levels, a plain meaning, when to use it, and an example from the topics: Concede and counter; Question the evidence; Turn it around; Add a reason; State a claim; Give an example; Ask to clarify ("What do you mean by ___?"); Close by weighing.
- **What do you say?**: ten short debate moments; pick the move that fits from three. A wrong pick says when that move is used ("Question the evidence is for when a fact has no source."). Then **Say it** for the right frame.

## Content
Frames (Full / Starter / Open help line):
- Concede and counter: "It is true that ___, but ___ because ___." / "It is true that..." / "Agree with one part. Then say but."
- Question the evidence: "How do we know that ___? ___ because ___." / "How do we know that..." / "Ask where their fact comes from. Then say why it matters."
- Turn it around: "That point actually supports my side, because ___." / "That point actually..." / "Show how their point helps you."
- Add a reason: "Another reason ___ is that ___. For example, ___." / "Another reason..." / "Give a new reason and an example."
- Opening: "I believe that ___ because ___." / "I believe..." Closing: "Although ___, I still believe ___ because ___." / "Although..."
Word bank (chips at Full): it is true that, I agree that, you are right that, but, however, still, how do we know, what evidence shows, actually, another reason, in addition, for example, because, this means, which shows, although.

Topics (Jordan always argues the side the student did not pick; each point has keywords for the check):
1. "Should students have homework on weekends?"
   - Yes reasons: practice helps you remember; long projects need more than one evening; planning your own weekend work is a skill for college and work.
   - No reasons: students need rest to learn well on Monday; many students have jobs, sports or activities on weekends; weekend homework is easy to rush.
   - Jordan's points against Yes: "Weekends are for rest. Rested students come back ready to learn." (rest, rested, ready, tired); "Lots of students have jobs, sports or activities on weekends." (jobs, sports, activities, busy); "Homework nobody checks until Monday is easy to rush." (rush, check, Monday).
   - Jordan's points against No: "Practice over the weekend helps you remember Friday's lesson." (practice, remember); "Big projects need more than one evening." (project, time, evening); "Planning your own work is a skill you'll need later." (plan, skill, later).
2. "Should the school library lend video games?"
   - Yes reasons: some games teach problem solving and history; games bring new students into the library; not every student can buy games.
   - No reasons: library money should go to books; games are easy to lose or break; students already have a lot of screen time.
   - Jordan against Yes: "Library money is limited, and books should come first." (money, books, budget); "Game discs and cases get lost or broken." (lost, broken, damage); "Students already spend a lot of time on screens." (screen, time).
   - Jordan against No: "Some games teach history and problem solving." (teach, history, problem); "Games could bring new students into the library." (new, bring, students); "Not every student can afford to buy games." (afford, buy, cost).
3. "Should every student learn to code before graduating?"
   - Yes reasons: many jobs use computers; coding teaches step-by-step problem solving; it helps you understand the apps you use.
   - No reasons: the schedule is already full; not every career needs it; schools would need more trained teachers.
   - Jordan against Yes: "The school day is already full of required classes." (schedule, full, classes); "Not every career needs coding." (career, need, job); "Schools don't have enough trained teachers for it." (teachers, trained).
   - Jordan against No: "Many jobs use computers every day." (jobs, computers, work); "Coding teaches you to solve problems step by step." (problem, step); "Coding helps you understand the apps you use." (apps, understand).
4. "Should zoos exist?"
   - Yes reasons: zoos run breeding programs for endangered animals; zoos teach visitors about animals; zoo scientists study animal health.
   - No reasons: zoo animals have much less space than in the wild; some zoo animals show signs of stress, such as pacing; the money could protect wild habitats instead.
   - Jordan against Yes: "Zoo animals have much less space than they would in the wild." (space, wild, room); "Some zoo animals pace back and forth, a sign of stress." (pace, stress); "That money could protect wild habitats instead." (money, habitat, protect).
   - Jordan against No: "Zoos run breeding programs for endangered animals." (breeding, endangered, programs); "Zoos teach visitors about animals they would never see." (teach, visitors, learn); "Zoo scientists study animal health." (scientists, health, study).
Jordan's order: if the student's opening reason matches a reason tag, Jordan's first point is the one that answers it (for example the student's "practice helps you remember" draws "Weekends are for rest" first, since rest and practice compete for the same time); otherwise the listed order.

What do you say? moments (right move in brackets): "Jordan says 'Everyone knows zoos are cruel.'" [Question the evidence]; "Jordan says weekends are busy for many students, and that's true." [Concede and counter]; "Jordan says games cost a lot, which is why the library should lend them." [Turn it around]; "You want to make a new point." [Add a reason]; "You don't understand Jordan's word 'habitat'." [Ask to clarify]; "The debate is ending." [Close by weighing]; "Jordan says 'Studies show coding is useless.'" [Question the evidence]; "Jordan says big projects need time. You agree, but think class time is better." [Concede and counter]; "You start the debate." [State a claim]; "You want to show your reason is real." [Give an example].

## Interactions in detail
- Check (shared engine, `Talk.check`): **Answers Jordan's point** when the reply holds a quote chip from Jordan's current card or at least one of that point's keywords (lowercase, with s, es, ed, ing endings removed). **Uses a counter move**: the chosen move's markers appear: Concede and counter needs one of (true, agree, right, fair, may, although, while) and one of (but, however, still, yet); Question the evidence needs (how do we know, what evidence, where does, is that true, who says) or a question about the point; Turn it around needs (actually, supports my, helps my, shows why); Add a reason needs (another reason, also, in addition, besides). **Gives a reason**: because, since, so, this means, for example, which shows.
- At Full frame the chips make all three ticks possible; at Open the check reads the typed text only. A reply answering only the student's own claim gets "You answered your own point. Tap Jordan's words first."
- Fade: with Fade as I go on, round 1 uses the chosen start level and each later round steps down one (Full, Starter, Open), never below Open. Off: the chosen level stays. The student can tap **More help** in any round to step up for that round.
- Two players: each player gets the same frames and checks; Jordan's points are replaced by Player 2's turn, and Player 2 taps Player 1's words the same way. Ms. Lin's notes speak to "Player 1" and "Player 2".
- Say it: the reply lights word by word at a steady 420 ms per word while it is read, then "Your turn: 3, 2, 1, say it" and the words light again at 500 ms per word. With Motion off the light-up still steps (no pulse). Skip is always allowed.
- Mode change calls `V.hush()`. Storage `counterpoint-frames:v1` (try/catch): help setting, fade switch, finished transcripts (last five). **Clear** asks first. Nothing typed leaves the page.
- Sizes: at 1366x768 the stage, the current Jordan card, the frame and Submit fit; the transcript scrolls in its own box. At 1000x625 the stage shrinks to a strip of three portraits. At 760 and 375 the stage is a header strip and the frame and Submit are pinned; tap targets 44 px. No horizontal scroll.

## Look
- Own dark `:root`, a stage under lights: `--paper #14121a`, `--panel #1d1a26`, `--ink #f1eef7`, `--muted #b4adc4`, `--line #332e42`, accent `--brand #ff6b6b` (spotlight coral: the active round, Submit, Jordan's quote chips), `--btn #ff6b6b`, `--head-ink #1a0f10`, `--focus #8fd3ff`. The student's own text in mint `#7ee0b5`. Ticks carry ✓ and ○ with words.
- Neighbors: argument-builder-pro civic green, socratic-seminar-board #0f6e78, classroom-phrases-game teal; nearest catalog accent tension-meter #ff5a4f (dE 13.4, ELA 9).
- Contrast: ink on paper 16.19:1; muted on paper 8.59:1, on panel 7.91:1; brand on paper 6.69:1, on panel 6.16:1; text on brand 6.76:1; mint on panel 10.76:1; focus on panel 10.53:1. All pass AA.

## Art
- jordan-neutral: a high school student in a plain hoodie standing at a simple podium, friendly neutral face, waist up, flat illustration, plain background. 1:1; cutout yes; people yes (Codex, Cory reviews); right podium.
- jordan-thinking: the same student, hand on chin, considering. 1:1; cutout yes; people yes; while the student writes.
- jordan-nodding: the same student nodding with a small smile. 1:1; cutout yes; people yes; after a reply that ticks Answers Jordan's point.
- lin-neutral: a teacher in a cardigan holding a clipboard, calm, waist up, same style. 1:1; cutout yes; people yes; moderator.
- lin-speaking: the same teacher mid-sentence, one hand open. 1:1; cutout yes; people yes; when she gives a note.
- Nothing in the art marks a home country, religion or immigration story. The student's podium is drawn in code with no figure.

## Voice
Bank voice `firm-captain` (Alnilam), style "Say firmly but kindly, like a debate moderator keeping the rounds moving." No other ELD tool or eld-hs tool uses it. `Curio.voice`, `scope: () => state.mode`. The voice reads Ms. Lin's lines and, on Hear it, Jordan's points (prefixed "Jordan says:").
- w-debate (how): "Pick a topic and a side. Then give your opening: your claim and one reason."
- tap-words (how, first Counter round): "Tap Jordan's words you want to answer. Then pick a move card."
- check-miss (event; stale on edit): "One part is missing. Look at the circle in the checks."
- own-point (event): "You answered your own point. Tap Jordan's words first."
- say-it (how): "Now say it out loud. Your turn in three, two, one."
- note-concede, note-question, note-turn, note-add (event, after each Submit): "You agreed with part of it and still answered it." / "You asked where the fact comes from." / "You turned their point into support for your side." / "You added a new reason with an example."
- fade (how, first round at a lower level): "Less help this round. You can tap More help any time."
- close (how): "Last round. Name their best point, then say why you still believe your claim."
- end (event): "Debate over. Read it back and find your strongest turn."
- w-cards (how): "Open a move card, or play What do you say."
- pick-right (event): "Yes. That move fits." pick-wrong (event): the chosen move's when-to-use line.
- Every Jordan point (event, on Hear it and when it appears).

## Family engine
eld-talk, `kit/eld-talk.js` (no family doc yet; this spec holds the full description; the integrating session copies it to docs/families/eld-talk.md). Built from the live classroom-phrases-game's Learn and Situations code.
- `Talk.phrase({id, text, move, use, icon})`: a phrase or frame with its talk move and a when-to-use line.
- `Talk.highlight(el, text, {per, voice})`: lights each word in turn at a steady pace while the line plays (classroom-phrases-game's 420 ms), returns a promise; Motion off keeps the stepping and drops the pulse.
- `Talk.echo(el, {count: 3, per})`: the "Your turn: 3, 2, 1, say it" step with the words lit again; never records.
- `Talk.pick(moment, options)`: one right phrase or move among three; a wrong pick returns its `use` line ("We say ___ when ___").
- `Talk.frames(move)`: {full, bank, starter, help} per move. Moves: agree, disagree, add on, ask to clarify, choose because (K-2), concede and counter, question the evidence, turn it around, add a reason, state a claim, give an example, close by weighing.
- `Talk.level(setting, round, fade)`: returns 'full', 'starter' or 'open' from the help setting ('lots', 'some', 'little'), the round and the fade switch.
- `Talk.check(text, {move, target, reason})`: returns {move, addresses, reason, notes} using marker lists per move and the target turn's keywords (lowercase, endings removed); quote chips count as addressing.
- `Talk.run(script, handlers)`: rounds of turns {speaker, text, keywords, tags}, with the next turn chosen by tags (Jordan answers the student's reason first).
- `Talk.cast(el, people)`: portraits with states (neutral, thinking, nodding, speaking) and `setState`.
- `Talk.store(key)`: localStorage wrapper with Clear.
Siblings: classroom-phrases-game (K-2, built) uses highlight, echo and pick, and moves onto the engine when next touched; talk-moves-trainer (3-5) feeds agree, disagree and add on frames, a classmate cast, `check` and `run`; i-choose-because (K-2) feeds two-picture choices to `pick`, the choose-because frame at 'full' only (picture chips, no typing) and `echo`. This tool feeds the counter moves, four debate scripts, `level` with fade, and `check` with quote chips.

## Sources
- WIDA ELD Standards Framework, 2020 Edition (Argue: claim, counterclaim, evidence and reasoning; proficiency levels 1 to 6): https://wida.wisc.edu/teach/standards/eld.
- Zoo breeding programs for endangered species: Association of Zoos and Aquariums, Species Survival Plan programs, https://www.aza.org/species-survival-plan-programs.
- Pacing as a sign of stress in some zoo animals: Clubb, R. and Mason, G., "Captivity effects on wide-ranging carnivores," Nature 425, 473-474 (2003), https://doi.org/10.1038/425473a.
- All other points are reasons and opinions written for Curio Class, not facts with numbers. Jordan and Ms. Lin are made up.

## Done when
- Weekend homework, Yes side, opening reason "practice helps you remember": Jordan's first point is "Weekends are for rest".
- Tapping "rest" and building "It is true that rest matters, but practice helps you remember because ..." ticks all three; "I believe homework is good because it helps" ticks only Gives a reason and gets the own-point line.
- Question the evidence with "How do we know that zoo animals pace? ... because ..." ticks Uses a counter move and Answers Jordan's point.
- Fade on, start Lots: rounds use Full, Starter, Open, Open, Open; More help steps one round up.
- Two players: Player 2's typed turn becomes the card Player 1 taps.
- Say it lights every word at the stated pace and records nothing (no microphone permission is ever asked).
- What do you say?: all ten moments accept their bracketed move and explain wrong picks.
- Transcripts survive reload (last five); Clear asks first.
- How lines are spoken once in five actions; Jordan's points and notes repeat when they recur.
- No horizontal scroll at any listed size; frame and Submit stay pinned at 375.

## Open questions
- None beyond the group's home-language question (see then-what-happened).
