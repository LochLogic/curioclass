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
- Standards: CASEL Relationship Skills (communicating effectively, listening actively, resolving conflicts constructively).
- Sensitive by default: every scene is fictional and ordinary. The tool never asks a student to type, pick or say anything about their own life, family or classmates. There is no text box anywhere in the tool.

## Screens and modes
Header: title "Conflict Coach", mode tabs `Scenes`, `Line Builder`, `Partner Cards` (`.seg`), icon buttons `Motion`, `Sound`, `Read`. Opens in Scenes on the scene picker. Stage on the left, panel on the right (`.panel`, hint paragraph id `hint`).

**Scene picker (top of the panel in Scenes and Line Builder).** Five cards, each with the other kid's name, a one-line setup and a small drawn face: `The Slides` (Jordan), `The Markers` (Priya), `The Tryout` (Mateo), `The Lab Controls` (Aiyana), `The Weekend Plan` (Sam). A small check appears on a card after a Clean run (see Scenes).

**Scenes (the main mode, explore first).**
- Stage: a bench-and-wall backdrop for the scene's place (art below), the other kid painted (art below) on the right, sitting on a short backless bench, half facing you. You are never drawn: the view is from your seat. Their speech bubble is above them; your line appears as a bubble rising from the bottom left.
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
- Buttons: `Swap roles` (cards flip with a short turn, instant when Motion is off), `Next scene`, `Show both sides` (reveals both reasons for the after-talk, in the third person so both partners can read it: "Both sides." the Speaker's reason, the other kid's reason, then "What did each of you not know at the start?"; in the short 16:10 preview it shows in the panel under the buttons), `Print cards`.

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

**2. The Markers (Priya).** Setup: "In art class, Priya keeps taking markers from your desk without asking. Today two came back with the caps off, dried out."
- Say it: I-statement "I feel frustrated when my markers come back dried out, because I bought them for my project. Could you ask me before you borrow them?" Half "I'm frustrated about my markers." Blame "You keep stealing my stuff. You're so rude." Brush-off "Never mind, take whatever."
- Their side: "I didn't think you'd mind. Mine ran out last week and I didn't want to ask the teacher again."
- Hear them: Reflective "So yours ran out, and you felt awkward asking the teacher for more." Fix-it-fast "Just buy your own then." Defend "I'd never take someone's stuff without asking." Dismiss "That's not my problem."
- Fix it: Both-sides "What if we share a cup of markers on the table, and we both put the caps back on?" Ask "What would make it easy for you to ask me first?" Give in "Forget it, you can just use them." Demand "Don't touch my markers ever again."
- Endings: stuck "Priya slides the markers back without a word. The table is quiet." Okay "Priya says she'll ask next time. You're still a little annoyed about the dried ones." Worked "You set a shared cup between you. Priya brings two new markers for it on Monday."
- Hidden reason (Partner Cards): "Your markers ran out, and asking the teacher again felt embarrassing."

**3. The Tryout (Mateo).** Setup: "You told Mateo you're trying out for the school play and asked him to keep it quiet. Today two kids in your class asked you about it."
- Say it: I-statement "I felt embarrassed when other kids asked about the tryout, because I wasn't ready for people to know. Can we talk about keeping things between us?" Half "I felt really embarrassed today." Blame "You told everyone. You can't keep your mouth shut." Brush-off "It doesn't matter. Everyone knows now."
- Their side: "I only told Ava and Jin because I was excited for you. I didn't know it was a big secret."
- Hear them: Reflective "So you were excited for me, and you didn't know how much I wanted it kept quiet." Fix-it-fast "Okay, so just tell them you were joking." Defend "I said it was a secret, though." Dismiss "Being excited doesn't make it okay."
- Fix it: Both-sides "Next time I share something, could I say if it's private, and you check before you tell anyone?" Ask "What would help you know when something is just between us?" Give in "Whatever, you can tell people stuff." Demand "You're never telling anyone anything I say again."
- Endings: stuck "Mateo says 'fine' and walks to his next class." Okay "Mateo says he'll be more careful. It still stings a little." Worked "Mateo asks Ava and Jin to keep it quiet. After the tryout, he's the first one to ask how it went."
- Hidden reason: "You were proud of your friend, and you didn't realize it was meant to be private."

**4. The Lab Controls (Aiyana).** Setup: "In science lab, Aiyana always runs the experiment. You end up just writing things down."
- Say it: I-statement "I feel bored when I only take notes, because I want to learn the lab too. Could we switch jobs halfway?" Half "I'm kind of bored in lab." Blame "You always hog everything. You're so bossy." Brush-off "It's fine, I'll write."
- Their side: "I just get nervous we'll mess up the steps and lose points."
- Hear them: Reflective "So you're nervous about our grade, and you want to make sure the steps are right." Fix-it-fast "Just let me do it next time." Defend "I wouldn't mess it up." Dismiss "That's silly. It's just a lab."
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

Their replies, same in every scene: after Say it they always answer with the scene's "Their side" line; if the meter landed on Heated, it starts "Wow. Okay. Well, " and they fold their arms; after a brush-off it starts "Um, okay. Well, ". After Hear them: reflective "Yeah. Exactly." Fix-it-fast "It's not that easy." Defend "See, you're not even listening." Dismiss "Forget it then." After Fix it: both-sides or ask what works "Yeah, that could work." Give in "Oh. Okay, if you're sure." Demand "You can't just tell me what to do." Then the ending card.

**Line Builder tiles** (per scene; one trap per row, marked T, all others good):
- The Slides: feeling `stressed`, `worried`, `frustrated`, T `like you don't care`. When `our slides are blank on Wednesday`, `the plan isn't done yet`, `we're two days from the due date`, T `you're being lazy`. Because `I want a good grade`, `I can't finish it alone`, `I want us to be ready`, T `you always do this`. Ask `make a plan today`, `split the slides`, `work on it after school`, T `agree you finish them all tonight`.
- The Markers: `frustrated`, `annoyed`, `upset`, T `like you don't respect me`. When `my markers come back dried out`, `the caps are left off`, `my markers are gone from my desk`, T `you steal my stuff`. Because `I bought them for my project`, `I need them to finish`, `I take care of my things`, T `you're so rude`. Ask `agree to ask before borrowing`, `share a cup on the table`, `both put the caps back on`, T `agree you never touch them again`.
- The Tryout: `embarrassed`, `hurt`, `surprised`, T `like you can't be trusted`. When `kids ask about the tryout`, `people know before I tell them`, `kids bring it up in class`, T `you blab to everyone`. Because `I'm not ready for people to know`, `I'm nervous about it`, `I want to tell people myself`, T `you always tell everyone everything`. Ask `keep private things between us`, `check before sharing`, `talk about what's private`, T `agree you never tell anyone anything`.
- The Lab Controls: `bored`, `left out`, `frustrated`, T `like you think I'm dumb`. When `I only take notes`, `I don't get to pour`, `you run every step`, T `you're bossy`. Because `I want to learn it too`, `I learn by doing`, `I want to be ready for the test`, T `you're a control freak`. Ask `switch jobs halfway`, `take turns each lab`, `run it together`, T `agree I do every step from now on`.
- The Weekend Plan: `hurt`, `left out`, `sad`, T `like you don't want me around`. When `I hear about plans after`, `I'm not asked`, `I see the photos after`, T `you leave me out on purpose`. Because `I like hanging out with you`, `I'd want to come`, `our friendship matters to me`, T `you always do this`. Ask `all go together next time`, `plan something we can all do`, `start a group chat for plans`, T `agree you always ask me first`.

Trap explanations: feeling row "Feel like you... is a thought about them, not a feeling. Try one word: hurt, worried, upset." When row "That's a judgment about them. Say only what happened, what a camera would see." Because row "That's about them. Say why it matters to you." Ask row "That's a demand. Ask for something you could both agree to."

Line Builder replies: no traps "Okay. I didn't know it bugged you that much. Yeah, let's try that." One trap "I mean, okay, but that part felt kind of harsh." Two or more "Why are you attacking me?"

## Interactions in detail
- Scenes: the four cards are buttons (44 px tall minimum, full sentence, keyboard focusable). Picking is one tap. Cards dim but stay readable after a pick; the picked one gets a border and the move's name.
- Faces and body language: three paintings per kid (art below). Five postures matching the meter: Heated (upset painting: brows down, frown, arms folded, turned away; leaned back 4 degrees), Tense (guarded painting: half turned away, hands gripped in the lap), Calm (open painting, upright), Listening (open painting leaned 3 degrees toward you), Working it out (open painting leaned 5 degrees toward you). A change crossfades the paintings and eases the lean over 400 ms, instant when Motion is off. The picker face chips are the head of the open painting. If a painting fails to load, that kid falls back to the code-drawn SVG figure (head, hair, brows, eyes, mouth, arms) with the same five postures.
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
Backdrops have no people or figures (local FLUX). Each is a full-frame 16:9 backdrop behind the bench, softened with a light overlay so the bubbles read.

Characters (gpt-image-2 through Codex, `"people": true`, reviewed; prompts in `art/prompts.json`, plan in `art-plan.md`): three seated full-length paintings per kid, cut out, 480 px tall, about 16 KB each. `kid-<name>` (open: facing you, small smile, one hand open on the thigh), `kid-<name>-guarded` (half turned away, hands gripped in the lap), `kid-<name>-upset` (arms folded, turned away). The variants were drawn with the base as a reference so each kid stays consistent. Hips sit 58% of the way down the painting, on the code-drawn seat.
- bg-classroom: "an empty middle school classroom in warm afternoon light, tables with laptops closed, a blank whiteboard, soft painted illustration"; 16:9; cutout no; people no; The Slides.
- bg-artroom: "an empty middle school art room with paint-splashed tables, jars of brushes and blank paper on the walls, warm light, soft painted illustration"; 16:9; cutout no; people no; The Markers.
- bg-hallway: "an empty school hallway with a row of blue lockers and a wooden bench, warm light, blank bulletin board, soft painted illustration"; 16:9; cutout no; people no; The Tryout.
- bg-lab: "an empty school science lab with beakers and a sink on a long counter, blank wall posters, soft painted illustration"; 16:9; cutout no; people no; The Lab Controls.
- bg-courtyard: "an empty school courtyard with a brick wall, a wooden bench and a small tree, late afternoon, soft painted illustration"; 16:9; cutout no; people no; The Weekend Plan and the Line Builder and Partner Cards stage.
- bench: a short backless wooden bench seen from the front (Cloudflare FLUX.2 klein, magenta-keyed cutout, 640 x 226). Only its two ends are shown, meeting behind the kid's legs, so it is about as wide as the kid's shoulders plus a bit; the seat top sits at the kid's knees. It stands alone at the kid's spot on the scene picker and is left out in Partner Cards. If it fails to load, a plain vector bench of the same size stands in. If a backdrop fails, the stage falls back to a flat paper scene.

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
