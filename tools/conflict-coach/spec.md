# Conflict Coach

## One idea
Say the same hard thing two ways and watch the other kid react: rewind any line of a fictional argument, swap a blaming "you" line for an I-statement or a real reflective listen, and see their face, their reply and the conversation meter change in front of you.

## Not like
- decision-tree (6-8, builder): there you map choices and their consequences as a tree you build. Here nothing is mapped and no tree or outcome chart is ever drawn. The choice is never what to do, only how to say it, and you replay one moment in place.
- walk-in-their-shoes (3-5, story): there you read one story through different characters' eyes. Here you are always yourself, talking live with one peer, and the skill is your own wording.
- feelings-faces, feelings-weather-report (K-2): those name feelings. Here feelings words are a tool you use inside a sentence, and nobody's own feelings are named or scored.

## Who and how
- Grade 6-8, Social and Emotional Learning, module "Conflict Resolution (SEL)".
- Driver: students or teacher. Students pair up on one laptop, or a teacher runs Scenes on a projector during advisory and the class votes on each move out loud. 15 to 25 minutes.
- Standards: CASEL Relationship Skills (communicating effectively, listening actively, resolving conflicts constructively). Also matches Illinois SEL Standard 2D (prevent, manage and resolve interpersonal conflicts in constructive ways).
- Sensitive by default: every scene is fictional and ordinary. The tool never asks a student to type, pick or say anything about their own life, family or classmates. There is no text box anywhere in the tool.

## Screens and modes
Header: title "Conflict Coach", mode tabs `Scenes`, `Line Builder`, `Partner Cards` (`.seg`), icon buttons `Motion`, `Sound`, `Read`. Opens in Scenes on the scene picker. Stage on the left, panel on the right (`.panel`, hint paragraph id `hint`).

**Scene picker (top of the panel in Scenes and Line Builder).** Five cards, each with the other kid's name, a one-line setup and a small drawn face: `The Slides` (Jordan), `The Jacket` (Priya), `The Lunch Seat` (Mateo), `The Lab Controls` (Aiyana), `The Weekend Plan` (Sam). A small check appears on a card after a Clean run (see Scenes).

**Scenes (the main mode, explore first).**
- Stage: a bench-and-wall backdrop for the scene's place (art below), the other kid drawn in code on the right, sitting at the far end of the bench, half facing you. You are never drawn: the view is from your seat. Their speech bubble is above them; your line appears as a bubble rising from the bottom left.
- Conversation meter: a horizontal bar across the top of the stage with five labeled stops: `Heated`, `Tense`, `Calm`, `Listening`, `Working it out`. A marker slides between them. Each stop has its own word and icon (flame, zigzag, flat line, ear, two hands), so color is never the only signal.
- Turn strip under the meter: three steps, `1 Say it`, `2 Hear them`, `3 Fix it`, the current one highlighted.
- Panel: the turn's prompt, then four move cards (your possible lines, full sentences), shuffled each time the turn is shown. Below them the Coach box, empty until you pick.
- After you pick: your bubble appears, the meter marker moves, the other kid's face and posture change, their reply bubble appears, and the Coach box names the move and says in one sentence what it did. Buttons appear: `Rewind` (undo this line and pick again) and `Next` (go to the next turn).
- After Rewind, the line you just took back stays on the stage as a faded "Last time" bubble beside the new one, with the meter's old position as a faded ghost marker, until you pick the next line or press Next. This side-by-side is the point of the tool.
- After turn 3: an ending card on the stage (the scene's ending for the final meter stop), and the Coach clipboard in the panel listing your three moves with their names. Buttons: `Replay scene`, `Next scene`, `Pick a scene`.
- Clean run (optional challenge): if all three final moves were strong moves (see Content), the clipboard shows "Clean run" and the scene card gets its check. Saved in localStorage `curio-conflict-coach-clean` (list of scene ids only, try/catch). A `Clear checks` button sits under the scene picker. No points, no timer.

**Line Builder.** Build one I-statement from tiles and have the coach check each part.
- Stage: a sentence frame in big type with four slots: `I feel [ 1 ] when [ 2 ] because [ 3 ]. Could we [ 4 ]?` The other kid from the chosen scene sits beside it with a neutral face.
- Panel: four tile rows, one per slot, four tiles each (tap a tile to drop it in its slot, tap a filled slot to empty it). Buttons: `Check my line`, `Say it to them`, `Clear`.
- `Check my line` marks each slot with a word and icon: `Feeling word`, `Just the facts`, `About you`, `Doable ask`, or, for a trap tile, the trap's name (`That's a thought, not a feeling`, `That's a judgment`, `That's about them`, `That's a demand`) plus one sentence why. Never a total score.
- `Say it to them` (enabled when all four slots are filled) plays the full line as your bubble and shows the other kid's reaction: open if no traps, guarded if one trap, defensive if two or more, with a reply line (Content).

**Partner Cards.** For two students reading aloud. No scoring, nothing to pick except the scene.
- Stage: two big cards side by side, `Speaker` and `Listener`, for the current scene.
- Speaker card: the situation from the speaker's side and the frame "I feel ___ when ___ because ___. Could we ___?" with two feeling-word suggestions.
- Listener card: the other side's hidden reason (from Content) and the frame "So you feel ___ because ___. Did I get that right?" then "From my side, ___."
- Buttons: `Swap roles` (cards flip with a short turn, instant when Motion is off), `Next scene`, `Show both sides` (reveals both reasons for the after-talk), `Print cards`.

## Content
Strong moves are marked (S). Meter changes: I-statement +2, half I-statement +1, brush-off 0, blame -1; reflective listen +2, fix-it-fast 0, defend -1, dismiss -1; both-sides plan +2 (S), ask what works +2 (S), give in 0, demand -1. The meter starts at `Tense` (stop 2 of 5) and clamps at both ends. Ending by final stop: Heated or Tense = still stuck, Calm = okay for now, Listening or Working it out = worked it out.

Coach lines (one per move, shown after every pick, with the scene's name filled in):
- I-statement (S): "I-statement. You said how you feel, what happened and what you need, without blaming. That is easier to hear."
- Half I-statement: "Half an I-statement. You named a feeling, but not what you need. Add an ask."
- Blame: "You-statement. It starts with what they did wrong, so people usually defend themselves."
- Brush-off: "Brush-off. It avoids the fight now, but the problem is still there."
- Reflective listen (S): "Reflective listen. You said back their feeling and their reason. They can tell you heard them."
- Fix-it-fast: "Fix it too fast. You jumped to a solution before showing you heard them."
- Defend: "Yeah-but. You went back to your side before they finished theirs."
- Dismiss: "Dismiss. Telling someone their reason doesn't count makes them dig in."
- Both-sides plan (S): "Both-sides plan. It meets your need and theirs."
- Ask what works (S): "Ask what works. Inviting their idea makes it a plan you made together."
- Give in: "Give in. It ends the argument, but your need disappears. Try one that works for both."
- Demand: "Demand. An order, not a plan. It usually starts the fight again."

**1. The Slides (Jordan).** Setup: "Your group project is due Friday. Jordan said they'd make four slides. It's Wednesday and their slides are blank."
- Say it: I-statement "I feel stressed when our slides are still blank on Wednesday, because I want us to get a good grade. Can we figure out a plan today?" Half "I'm really stressed about the slides." Blame "You never do your part. You're so lazy." Brush-off "Whatever, I'll just do them myself."
- Their side (their reply to any Say it line): "I'm sorry. My grandma's been staying with us and I've had no quiet place to work this week."
- Hear them: Reflective "So it's been hard to focus at home with your grandma there, and you're stuck." Fix-it-fast "Just do them at lunch then." Defend "Yeah, but I have stuff going on too." Dismiss "That's not really an excuse."
- Fix it: Both-sides "What if we work on them together in the library after school tomorrow?" Ask "What would help you get them done by Thursday?" Give in "Never mind, I'll do all of it." Demand "Just have them done by tonight or I'm telling the teacher."
- Endings: stuck "Jordan goes quiet and walks off. The slides are still blank." Okay "Jordan says they'll try. You're both still a little worried." Worked "You meet in the library Thursday. Jordan finishes three slides and you help with the fourth."
- Hidden reason (Partner Cards): "Your house is crowded and loud this week and you're embarrassed to say so."

**2. The Jacket (Priya).** Setup: "You lent Priya your favorite jacket. She gave it back with a juice stain on the sleeve."
- Say it: I-statement "I feel upset when my jacket comes back stained, because it's my favorite. Could we figure out how to clean it?" Half "I'm upset about my jacket." Blame "You ruined my jacket. You're so careless." Brush-off "It's fine. Forget it."
- Their side: "I didn't even see it. I'm really sorry. I was hoping you wouldn't be mad."
- Hear them: Reflective "So you didn't notice it, and you were worried I'd be mad." Fix-it-fast "Just pay for a new one." Defend "Well, I'd have noticed." Dismiss "Not noticing doesn't make it okay."
- Fix it: Both-sides "Could you help me try to wash it out this weekend?" Ask "What do you think we should do about it?" Give in "Don't worry about it, it's just a jacket." Demand "You have to buy me a new one."
- Endings: stuck "Priya says sorry again but won't look at you." Okay "Priya offers to try a stain remover. It's a start." Worked "You wash it together Saturday. Most of the stain comes out."
- Hidden reason: "You didn't see the stain, and you feel awful that you might lose a friend over it."

**3. The Lunch Seat (Mateo).** Setup: "You asked Mateo to save you a seat at lunch. When you got there, he'd given it to someone else."
- Say it: I-statement "I felt left out when my seat was gone, because I was looking forward to sitting with you. Can we work out saving seats?" Half "I felt left out at lunch." Blame "You gave away my seat. You're a terrible friend." Brush-off "I don't care where I sit."
- Their side: "The new kid, Theo, didn't know anyone. I thought you'd be there way sooner."
- Hear them: Reflective "So you were trying to help Theo, and you didn't know I'd be late." Fix-it-fast "Okay, so just tell him to move tomorrow." Defend "I was only five minutes late." Dismiss "That doesn't matter, you promised."
- Fix it: Both-sides "Could we pull up another chair so all three of us fit?" Ask "How could we do it tomorrow so it works for both of us?" Give in "Fine, I'll sit somewhere else." Demand "Tomorrow you save my seat, no matter what."
- Endings: stuck "Mateo shrugs and turns back to Theo." Okay "Mateo says he'll try to save a seat next time." Worked "The next day there are three chairs. Theo laughs at your joke."
- Hidden reason: "A new kid had nowhere to sit, and you wanted to be kind."

**4. The Lab Controls (Aiyana).** Setup: "In science lab, Aiyana always runs the experiment. You end up just writing things down."
- Say it: I-statement "I feel bored when I only take notes, because I want to learn the lab too. Could we switch jobs halfway?" Half "I'm kind of bored in lab." Blame "You always hog everything. You're so bossy." Brush-off "It's fine, I'll write."
- Their side: "I just get nervous we'll mess up the steps and lose points."
- Hear them: Reflective "So you're nervous about our grade, so you want to make sure the steps are right." Fix-it-fast "Just let me do it next time." Defend "I wouldn't mess it up." Dismiss "That's silly. It's just a lab."
- Fix it: Both-sides "What if I run it next time and you check the steps with me?" Ask "What would make you okay with switching?" Give in "Never mind, you can keep doing it." Demand "Starting now, I do it every time."
- Endings: stuck "Aiyana grabs the beaker again. You pick up the pencil." Okay "Aiyana lets you pour one step. It's a start." Worked "Next lab you run it while Aiyana reads the steps. You both finish early."
- Hidden reason: "You worry about grades, and doing it yourself feels safer."

**5. The Weekend Plan (Sam).** Setup: "Sam planned a movie trip with friends this weekend. You heard about it after, and you weren't asked."
- Say it: I-statement "I felt hurt when I heard about the movie after, because I like hanging out with all of you. Could you include me next time?" Half "I felt hurt about the movie." Blame "You left me out on purpose." Brush-off "I didn't want to go anyway."
- Their side: "My mom only had room for three in the car. I felt bad about it."
- Hear them: Reflective "So there wasn't room in the car, and you felt bad about it too." Fix-it-fast "Then just take the bus next time." Defend "You could have asked to come." Dismiss "That sounds made up."
- Fix it: Both-sides "Next time could we pick a place we can all get to, like the park?" Ask "How could we plan it next time so I'm in?" Give in "It's okay, you don't have to invite me." Demand "Next time you have to ask me first."
- Endings: stuck "Sam says 'okay' and changes the subject." Okay "Sam says they'll text you next time." Worked "Sam starts a group chat for Saturday at the park, and you're the first one added."
- Hidden reason: "There wasn't room, and you felt bad but didn't know how to say it."

Their replies, same in every scene: after Say it they always answer with the scene's "Their side" line; if the meter landed on Heated, it starts "Wow. Okay. Well, " and they fold their arms; after a brush-off it starts "Um, okay. Well, ". After Hear them: reflective "Yeah. Exactly." Fix-it-fast "It's not that easy." Defend "See, this is why I didn't say anything." Dismiss "Forget it then." After Fix it: both-sides or ask what works "Yeah, that could work." Give in "Oh. Okay, if you're sure." Demand "You can't just tell me what to do." Then the ending card.

**Line Builder tiles** (per scene; one trap per row, marked T, all others good):
- The Slides: feeling `stressed`, `worried`, `frustrated`, T `like you don't care`. When `our slides are blank on Wednesday`, `the plan isn't done yet`, `we're two days from the due date`, T `you're being lazy`. Because `I want a good grade`, `I can't finish it alone`, `I want us to be ready`, T `you always do this`. Ask `make a plan today`, `split the slides`, `work on it after school`, T `do it right now`.
- The Jacket: `upset`, `sad`, `disappointed`, T `like you're careless`. When `my jacket came back stained`, `there's juice on the sleeve`, `I saw the stain`, T `you wrecked it`. Because `it's my favorite`, `I wear it a lot`, `I saved up for it`, T `you never take care of things`. Ask `try to clean it together`, `look up how to get stains out`, `talk about what to do`, T `buy me a new one`.
- The Lunch Seat: `left out`, `disappointed`, `sad`, T `that you're a bad friend`. When `my seat was gone`, `I couldn't find a spot`, `I ate at another table`, T `you ditched me`. Because `I wanted to sit with you`, `lunch is my favorite part of the day`, `I was looking forward to it`, T `you only care about the new kid`. Ask `pull up another chair`, `plan seats together`, `all sit together tomorrow`, T `never do that again`.
- The Lab Controls: `bored`, `left out`, `frustrated`, T `like you think I'm dumb`. When `I only take notes`, `I don't get to pour`, `you run every step`, T `you're bossy`. Because `I want to learn it too`, `I learn by doing`, `I want to be ready for the test`, T `you're a control freak`. Ask `switch jobs halfway`, `take turns each lab`, `run it together`, T `let me do everything`.
- The Weekend Plan: `hurt`, `left out`, `sad`, T `that you don't like me`. When `I heard about the movie after`, `I wasn't asked`, `I saw the photos`, T `you left me out on purpose`. Because `I like hanging out with you`, `I'd have wanted to come`, `you're my friends`, T `you always do this`. Ask `include me next time`, `plan something we can all do`, `text me about plans`, T `always ask me first`.

Trap explanations: feeling row "Feel like you... is a thought about them, not a feeling. Try one word: hurt, worried, upset." When row "That's a judgment about them. Say only what happened, what a camera would see." Because row "That's about them. Say why it matters to you." Ask row "That's a demand. Ask for something you could both agree to."

Line Builder replies: no traps "Okay. I didn't know it bugged you that much. Yeah, let's try that." One trap "I mean, okay, but that part felt kind of harsh." Two or more "Why are you attacking me?"

## Interactions in detail
- Scenes: the four cards are buttons (44 px tall minimum, full sentence, keyboard focusable). Picking is one tap. Cards dim but stay readable after a pick; the picked one gets a border and the move's name.
- Faces, drawn in code (SVG), like tools/feelings-faces: a head with hair, brows, eyes, mouth, plus a body with arms and a slight body turn. Five postures matching the meter: Heated (brows down, mouth tight, arms crossed, turned away), Tense (arms crossed, half turned), Calm (neutral mouth, hands on knees), Listening (facing you, head tilt, brows up), Working it out (small smile, facing you, one hand open). Changes ease over 400 ms, instant when Motion is off.
- Characters: Jordan (skin #7a4a2e, short black hair), Priya (#a8714b, long dark braid), Mateo (#c68a5e, dark curls), Aiyana (#8d5a3b, long straight black hair), Sam (#f1c8a0, brown bob). Simple clothes in scene colors. Names and looks are a mix on purpose; no scene ties a trait to a group.
- Rewind can be pressed any number of times on the same turn; only the most recent taken-back line shows as the faded "Last time" bubble. Rewind on turn 2 or 3 restores the meter to its value before that turn. A Clean run counts only the final three lines kept, so rewinding is never punished.
- Replay scene starts the meter at Tense again. Switching scenes or modes calls `Curio.stop()` and resets the scene.
- Line Builder: one tile per slot; dropping a new tile replaces the old. `Check my line` with empty slots marks them "Pick one". `Clear` empties all four. Changing the scene clears the frame.
- Partner Cards: `Print cards` prints both cards for the current scene (print stylesheet, black on white, no header). `Show both sides` toggles.
- Projector use: in Scenes, the four cards also show letters A to D, and keys 1 to 4 or A to D pick, R is Rewind, N is Next, so a teacher can run a class vote.
- Nothing is stored except the Clean run list and the kit's Motion setting.

## Look
6-8 band sets its own `:root` (no band theme file). Warm courtyard look, different from the SEL neighbors (calm-corner green #2f7a62, feelings-weather-report teal #26627a, feelings-faces magenta #b0407a).
- `--paper #fff8f1`, `--ink #26211f`, `--muted #6b5d55`, `--line #ecd9c6`, `--brand #b3471d` (burnt orange), `--panel #ffffff`, `--focus #1f5f8b`.
- Meter stops: Heated #a1302a, Tense #8a5a00, Calm #6b5d55, Listening #1f5f8b, Working it out #2f6b3a, each with a word and icon.
- Speech bubbles: theirs white with ink text, yours #f6ead8 with ink text. "Last time" bubble at 55% opacity with a dashed border plus the label "Last time".
- Contrast (computed): white on brand 5.47:1; brand on paper 5.2:1; ink on paper 15.12:1; muted on paper 6.01:1; ink on your bubble 13.4:1; white on Heated 7.07:1, on Listening 6.84:1, on Working it out 6.39:1; Tense color on paper 5.63:1. All pass AA for normal text.
- No confetti. A Clean run gets a single soft chime (`Curio.yes()`) and the check mark.

## Art
Backdrops only, no people or figures anywhere (local FLUX). Characters are drawn in code. Each is a full-frame 16:9 backdrop behind the bench, softened with a light overlay so the bubbles read.
- bg-classroom: "an empty middle school classroom in warm afternoon light, tables with laptops closed, a blank whiteboard, soft painted illustration"; 16:9; cutout no; people no; The Slides.
- bg-hallway: "an empty school hallway with a row of blue lockers and a wooden bench, warm light, soft painted illustration"; 16:9; cutout no; people no; The Jacket.
- bg-cafeteria: "an empty school cafeteria with long tables and orange chairs, sunny windows, soft painted illustration"; 16:9; cutout no; people no; The Lunch Seat.
- bg-lab: "an empty school science lab with beakers and a sink on a long counter, blank wall posters, soft painted illustration"; 16:9; cutout no; people no; The Lab Controls.
- bg-courtyard: "an empty school courtyard with a brick wall, a wooden bench and a small tree, late afternoon, soft painted illustration"; 16:9; cutout no; people no; The Weekend Plan and the Line Builder and Partner Cards stage.
The bench in front is drawn in code so the characters sit on it. If an image fails, the stage falls back to a flat paper scene with the bench.

## Voice
Bank voice `big-sister` (Leda, "3-8 peer voice"): "Say in a friendly, youthful way, like a helpful older student." The coach is a friendly older student. The dialogue itself is on screen only (one voice for five different kids would sound wrong). Narration is the welcomes, the Coach lines and the hints, so Read can use recordings. Fixed lines:
- Welcome, Scenes: "Pick a scene. You'll choose what to say, and you can rewind any line to try it another way."
- Welcome, Line Builder: "Build an I-statement. Pick one tile for each part, then check your line."
- Welcome, Partner Cards: "Grab a partner. One of you is the Speaker, one is the Listener. Then swap."
- Hint, Say it: "Say how you feel, what happened and what you need."
- Hint, Hear them: "Say back their feeling and their reason before you answer."
- Hint, Fix it: "Look for a plan that works for both of you."
- Hint, after Rewind: "See the faded line? That was last time. Compare how they react."
- Hint, Line Builder: "A feeling is one word, like hurt or worried. 'I feel like you' is a thought, not a feeling."
- Hint, Partner Cards: "Listener, say back what you heard before you share your side."
- The twelve Coach lines in Content, recorded with "{name}" left out (they do not use names).
- Ending lines: "You worked it out." "Okay for now." "Still stuck. Try rewinding a line."
- Clean run: "Clean run. Every move was a strong one."
Voice behavior follows STANDARDS.md (collision-lab pattern).

## Family engine
none

## Sources
- CASEL, "What Is the CASEL Framework?" (Relationship Skills: communicating effectively, listening actively, resolving conflicts constructively): https://casel.org/fundamentals-of-sel/what-is-the-casel-framework/
- Illinois State Board of Education, Social/Emotional Learning Standards, Goal 2, Standard 2D: https://www.isbe.net/Pages/Social-Emotional-Learning-Standards.aspx (builder: check the 2D wording before quoting it in notes)
- I-statements ("I-messages") as a way to state a problem without blame: Thomas Gordon, Parent Effectiveness Training (1970); Gordon Training International, "I-Messages": https://www.gordontraining.com/
- Active (reflective) listening, saying back the speaker's feeling and meaning: Carl R. Rogers and Richard E. Farson, "Active Listening" (1957), University of Chicago Industrial Relations Center.
- The coach lines say "usually" and "easier to hear", not "always" or "proven". Keep that wording.

## Done when
1. In each of the five scenes, all three turns show four full-sentence cards, and picking each moves the meter by the amount in Content (start Tense, clamp at Heated and Working it out).
2. Rewind on any turn restores the meter and the face, keeps the taken-back line as a faded "Last time" bubble, and allows a new pick; the final ending matches the final meter stop.
3. Picking the three strong moves in a scene gives "Clean run" and a check on the scene card that survives a reload; `Clear checks` removes it; a Clean run still counts after rewinds.
4. Line Builder: every trap tile is caught with its own explanation, a line with no traps gets the open reply, two traps get the defensive reply, and `Say it to them` is disabled until all four slots are filled.
5. Partner Cards: `Swap roles` flips the cards, `Show both sides` reveals both reasons, and `Print cards` prints both cards cleanly.
6. There is no text input anywhere, and localStorage holds only `curio-conflict-coach-clean` and the kit Motion key.
7. The other kid's five postures are visibly different and every meter stop shows a word and icon, not just a color.
8. Keys 1 to 4, A to D, R and N work in Scenes; all buttons are reachable by Tab with visible focus.
9. The move cards and the Rewind and Next buttons are visible without scrolling at 1366x768, 1280x720 and 800x500, and the tool works at 760 and 375 wide.
10. Welcomes play once per mode, Read speaks the current hint, and mode switches stop speech (STANDARDS.md voice checks).
