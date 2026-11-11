# Blizzard Scenes

## One idea
A class trip bus is stranded by a blizzard at a closed gas station at night; the student reads a model scene told by the driver and again by the quiet new kid, marks what each narrator knows, notices and hides, writes their own scene from a seat they choose, then rewrites it from another seat and in a new order (starting when the headlights appear), and the versions sit side by side with facts only one narrator could know lit up, so they learn that point of view and order are choices that change what a reader knows and feels.

## Not like
- flashback-editor (8, concept): rearranging a finished story into a flashback with time-shift transitions. Here new versions written from different seats.
- perspective-camera (6, concept): first, second and third person. Here different narrators inside one scene.
- tension-meter (9, concept): graphing suspense. Here point of view and order.
- slow-mo-writer (5, spec): pacing one moment. Here who tells it and when.
- show-don-t-tell (3, spec): one feeling shown. Here what each narrator can see.

## Who and how
- Grades 6-8, ELA, module "Narrative Point of View and Structure" (Writing and Reading Literature). Standards: W.6.3, W.7.3, RL.7.6, W.8.3, RL.8.5.
- Driver: one student, or students trading scenes (tool.json `driver: "student"`). Role: lesson. Every sentence is read on tap; the student's scenes are read back by the browser's speech voice.
- One blizzard night, three places in one town. Each grade has its own place, its own model texts and fact cards, and that grade's wording on the goal card. No path needs another.
  - Grade 6, the bus. W.6.3: write a narrative that sets a context and a narrator, orders events so they unfold naturally, uses dialogue, pacing and description, uses transition words to signal shifts in time or setting, uses sensory details, and ends with a conclusion that follows from the events.
  - Grade 7, the diner. RL.7.6: analyze how an author develops and contrasts the points of view of different characters or narrators. W.7.3: as grade 6, with a point of view set at the start, transitions that signal shifts from one time or setting to another, and a conclusion that reflects on the events.
  - Grade 8, the plow and the radio room. RL.8.5: compare and contrast the structure of two or more texts and analyze how the differing structure of each contributes to its meaning and style. W.8.3: as grade 7, with events ordered so they unfold logically, transitions that show how events relate, and precise words and sensory language.
- Change note (spec fix, 2026-11-11): the storm, the seats, the two-narrator reading, the rewrite from another seat and the side by side stay. Before, the grades shared the bus, the prompt strip was ticked by the student with nothing behind it, the marks showed their own corrections, grade 8 only moved old paragraphs and any transition passed, and the structure questions had no check. Now every scene is five beats, each checked against the fact cards its narrator could know and against a guide the student taps in their own words; grade 7 marks five moments and names how the author builds each view; grade 8 compares two texts by different writers on five points and writes a new scene out of time order with transitions checked for direction. The host writes a model beat first and the last two items are on your own. Added the three hooks.
- English learners: every spoken line is also on screen in short sentences. The words narrator, point of view, dialogue, slow moment, transition, structure and reflect each show with the host's model beat as the example the first time they are used. Each beat offers a frame the student may take or leave ("From where I sat, I could see __."). Instructions use no idioms.
- tool.json `modes: ["Grade 6", "Grade 7", "Grade 8"]`, `minutes: "35-50"` a sitting (grades 7 and 8 take two), `grades_label: "Grades 6-8"`. Nothing is timed.
- Saving: the student's scenes are kept in this browser; footer: "Your scenes stay on this device." `Clear my scenes` removes them.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| W.6.3 | write a narrative: context and narrator, natural order, dialogue, pacing, description, time transitions, sensory detail, a conclusion that follows | the student | Pick a seat and write a scene in five beats (set the scene, talk, slow moment, time jump, ending), tagging the facts each beat uses and checking each beat against the guide | 5 beats | the scene, the fact cards, the guide | 3 |
| RL.7.6 | analyze how an author develops and contrasts the points of view of different narrators | the student | For five moments told by both narrators, mark what each knows, notices or hides, and name how the author shows it with the words tapped | 5 moments, 2 narrators | the two columns side by side | 2 |
| W.7.3 | write a narrative with a point of view, transitions that signal shifts, and a conclusion that reflects | the student | Write five beats from one seat, then rewrite the same five from another seat that knows different facts | 10 beats in 2 versions | the two versions in columns with their fact cards | 4 |
| RL.8.5 | compare and contrast the structure of two texts and analyze how each structure contributes to meaning and style | the student | For five points of structure, tap the place in each text and choose what the difference does to meaning or to style | 5 points, 2 texts | the two texts with structure strips | 5 |
| W.8.3 | write a narrative with logical order, transitions that show how events relate, precise words and sensory language, and a reflective conclusion | the student | Write a new five-beat scene that starts at the end and goes back, with a transition at each jump, then sharpen three words and mark two sense details | 5 beats, 3 jumps | the scene and its strip in story time | 6 |

## Screens and modes
Header (kit): title "Blizzard Scenes"; `Models`, `My scenes`, `Side by side`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. The goal card gives the grade's standards in their own words.

**On load and first tap.** A small town at night under heavy snow, seen from above: a school bus half buried beside a dark gas station, a diner with one lit window, a plow's lights far up the road. The grade's place is lit, with its seats. First hint: "Tap a seat to hear who sits there." The first tap reads the scene's title; the welcome is queued after it (`welcomeAfter: true`).

**The host writes first (the model).** The host writes one beat aloud from a seat no student can pick (a stray dog under the bus): picks two fact cards the dog could know, writes three sentences, and taps the guide lines in them. In grade 7 the host also marks one moment in the models; in grade 8, answers one structure point. It cannot be skipped the first time and `The host's beat` reopens it, except on the items on your own.

**Fact cards.** Each place has 16 fact cards (what the radio said; the open back door; who has the only flashlight). Every card is keyed to the seats that could know it. While writing a beat the student tags the cards it uses. A card the narrator could not know is turned back with "How would {Ren} know that?"

**A scene is five beats.** Set the scene (who is telling, where, when); talk (a line of dialogue that shows something about the speaker); slow moment (a few seconds told in four or more sentences, with details for two senses); time jump (a shift in time or place with a transition); ending. A beat needs three sentences or more and at least one fact card its narrator could know.

**Check it against the guide.** After each beat the guide shows that beat's lines (for the slow moment: "stays in one moment", "something seen", "something heard or felt"). The student taps the words in their own beat that do each one; a line with nothing tapped sends them back. The transition in the time jump is checked against the tray's labels (earlier, later, same time, elsewhere) and the direction the student says the jump goes.

**Grade 6, the bus.** Seats: the driver (Mr. Hale), a nervous chaperone (Ms. Duarte), the quiet new kid (Ren), the class clown (Dez) and "You". The student reads one short model (Dez's, about 250 words), then writes five beats from another seat. The ending must follow: the student taps the earlier sentence in their own scene that the ending grows from.

**Grade 7, the diner.** Models: the same 20 minutes told by the cook (she knows the generator has an hour of fuel and hides it) and by a trucker's daughter (she notices the cook counting cans; she does not know about the fuel), about 350 words each, set in columns by moment. For each of five moments the student marks each narrator `knows`, `notices`, `hides` or `does not know`, and names how the author shows it (inner thoughts given; what the narrator looks at; a word choice; something left unsaid), tapping the words. Marks and method are one answer; a miss says only "Read both again" and a second miss prints as "shown". Then the student writes five beats from one diner seat and rewrites them from another; a fact list builds under each column of what only that narrator could know, and the ending must look back ("what I understood later").

**Grade 8, the plow and the radio room.** Two texts by different writers about the same hour: "Blade Down", a plow driver's story told in order (about 400 words), and "Dispatch Log", the radio room's night told as timed log entries that begin with the last entry and step back (about 300 words). Structure strips show each as blocks in story time. Five points: where each begins; how each is divided; where the reader learns the bus is safe; how time moves; how each ends. For each the student taps the place in both texts and chooses, from four, what the difference does (to meaning: what the reader knows and when; to style: how it sounds and feels). Then one line in their own words. The student then writes a new five-beat scene from a seat in the plow or the radio room that starts at the end and goes back: three jumps, each with a transition whose label matches the jump, the strip redrawn from what they wrote. Last, they swap three flagged plain words (went, got, thing, nice, very and the like) for exact ones and mark two sense details.

**Side by side.** The student's versions in columns and four questions answered in a line each: what the reader knows first in each; which keeps the reader waiting; whose feelings are hidden; which ending lands.

**On your own.** Writing: beats 4 and 5 are written with the host's beat closed, frames shut unless opened, and no card or guide turn-backs until both are in. Reading (grades 7 and 8): the last two moments or points take one answer each and nothing is marked until both are in.

**The end.** A results strip for the teacher by code. Writing code: for beats 4 and 5, fact cards the narrator could know, transition matching its jump, and the guide lines met, with the beats printed. Reading code: the two items on your own right or not in each keyed part, with the student's line. Then the counts from the guided items and anything printed as "shown".

At 1366x768 two columns fit; at 680x425 versions are tabs.

## Content
Written for Curio Class:
- The night: a class trip bus heading home from a science museum, a sudden blizzard, a closed gas station on a two-lane road, a diner a mile on, the county plow and its radio room. No one is hurt; the moving light in the station is the owner checking her pipes, who brings blankets and cocoa.
- Models: Dez's version on the bus (grade 6); the cook's and the daughter's versions in the diner (grade 7); "Blade Down" and "Dispatch Log" (grade 8); the host's dog beat.
- Fact cards: 16 a place, each keyed to the seats that could know it.
- Keys: grade 7, for five moments, each narrator's mark and the method with its words; grade 8, for five points, the places in each text and what the difference does, with what each wrong choice stands for. Transition tray: 16 transitions labeled earlier, later, same time or elsewhere. A list of plain words to sharpen.
- What a wrong answer on your own means. A fact card the narrator could not know: the student is writing as themselves, who has read every version, and not from the seat. A time jump with "later" where the story goes back: transitions are being added for sound and not for direction. An ending that brings in something new: the conclusion is not growing from the events. RL.7.6, "knows" marked where the narrator only notices: the student is not separating what a character sees from what they understand. Method "inner thoughts" chosen everywhere: the student sees whose head we are in but not how the author does it. RL.8.5, the same effect chosen for every point: structure is being read as "one is backwards" and no more. A style difference answered with a meaning choice: the two are not yet apart.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Scenes autosave as the student types.
- Class trade: `Trade` makes a printable copy for a classmate to rewrite from a third seat.
- With Motion off the snow is still.
- Access: every action works by tap and by keyboard. Fact cards and transitions are placed by drag, or picked up and placed with taps, or with arrow keys and Enter; words are tapped or reached with arrow keys. Marks and turn-backs are words, never color alone; "only this narrator" lines carry a label. Read-back has its words on screen. Motion (the snow) can be paused. Nothing is timed.
- On your own: no turn-backs until both items are in.

## Look
- Accent `--brand` #4a3f7a storm violet (header, column rules, seat chart); gold #f4c542 (the headlights, lit lines); paper #f5f4fa; ink #17132b; muted #57536a. Scene: blue-violet night snow with one warm light.
- Contrast (WCAG 2.1, computed): white on brand 9.20:1; brand on paper 8.41:1; ink on paper 16.49:1; muted on paper 6.74:1; ink on gold 11.09:1.
- Never color alone: marks are words; lit lines also carry a "only" tag.
- Different from this batch (sky blue, pumpkin, granite green, museum burgundy).

## Art
- People art goes to Gemini: the five passengers (Mr. Hale, a white man in his sixties in a heavy coat; Ms. Duarte, a Latina woman in her thirties; Ren, a Japanese American kid about 12 with a sketchbook; Dez, a Black kid about 12 in a bright hat; the station owner, an older white woman in a parka), 2 poses each; "illustrated young adult novel character <description> <pose>, cool night palette, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): bus in snow at night (1), gas station with one light (1), plow headlights through snow (1); 16:9; no people.
About 13 images. Drawn in code: seating chart, columns, structure strips.

## Voice
Bank voice `smooth-narrator` as the host (unique in this batch); the driver's model is read by `gravel-ranger` and Ren's by `soft-breath` (each unique in this batch). `Curio.voice` with `scope: () => state.grade + ':' + state.view + ':' + state.version`, `welcomeAfter: true`.
- how `welcome`: "Same bus, same storm. Who tells it changes what you know. Listen to the driver, then to Ren."
- event, whole, `sentence`: the tapped sentence.
- how `markHow`: "Mark each line: does this narrator know it, notice it, or hide it?"
- event `only`: "Only {Ren} could know this."
- how `seatHow`: "Pick your seat and write what your narrator sees."
- how `reorderHow`: "Start at the headlights. Then go back. Pick a transition for each jump."
- event `side`: "Three versions. Which one keeps you waiting longest?"
Read speaks the hint, which names the next action and control and never a disabled one.
- event `howKnow`: "How would {Ren} know that?"
- how `beatHow`: "Write this beat. Tag the facts you use. Then check it against the guide."
- how `methodHow`: "Mark what each narrator knows. Then tap the words that show you."
- how `pointHow`: "Tap the place in each text. Then choose what the difference does."
- how `jumpHow`: "Which way does this jump go? Choose a transition that says so."
- how `own`: "The last two are on your own."
- event, whole, the host's beat.
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
None. Tool-only code: narrator marks and the only-one comparison, text boxes with prompt strips, paragraph reorder with a transition tray, side-by-side columns.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| My scene | Write one line; tick the prompts | Five beats of three sentences or more; the student must tap the words that meet each guide line; each beat needs a fact card its narrator could know. |
| Point of view | Use every fact | Cards are keyed by seat and a card the narrator could not know is turned back. |
| Marks (grade 7) | Mark everything "knows"; copy the shown differences | Four marks, judged with the method and its words as one answer; a miss shows nothing. |
| Structure (grade 8) | Pick from four | The place in each text must be tapped, and five points have five different keyed effects, split between meaning and style. |
| Reorder (grade 8) | Drop any transition at each jump | The scene is newly written; each transition's label must match the direction of its jump. |
| On your own | Lean on turn-backs | None until both items are in. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a seat: title, `welcome` (queued, first time), then the host's beat (whole), waits.
2. Models: `sentence` (whole). Grade 7: `methodHow` (first time); `only` as it fires. Grade 8: `pointHow`.
3. My scenes: `seatHow`; `beatHow`; `howKnow` as it fires; `jumpHow` at a time jump.
4. Items on your own: `own`. Side by side: `side`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.6.3, W.7.3, RL.7.6, W.8.3, RL.8.5 wording | thecorestandards.org, Grades 6-8 | CCSS ELA 2010 PDF | yes |
| A narrator's point of view limits what the reader learns; a story can open at a later moment and move back | ReadWriteThink, point of view and narrative structure lessons | Purdue OWL, narrative essays and point of view | yes |
Backed twice: 2. Cut: 0.

Design choices (not claims): knows, notices, hides; the four side-by-side questions.

Checks run (Python, scratchpad b16, 2026-11-09): in the sample mark key, each model has at least two lines only its narrator could know; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 two columns fit; at 680x425 versions are tabs.
2. Grade 7: five moments take each narrator's mark and the author's method with words tapped, as one answer. (RL.7.6)
3. A scene is five beats; each takes fact cards checked against the seat and the student's taps against the guide; grade 6's ending points back to an earlier sentence. (W.6.3)
4. Grade 7 writes five beats from one seat and five from another, with only-one facts listed and an ending that looks back. (W.7.3)
5. Grade 8: five structure points take a place in each text and an effect on meaning or style. (RL.8.5)
6. Grade 8 writes a new scene that starts at the end, with each transition matching its jump, three words sharpened and two sense details marked. (W.8.3)
7. The host's beat plays first; a second miss prints as shown. The last two items run on your own and the end screen shows results by code.
8. Scenes survive a reload where storage works; `Clear my scenes` removes them. Print and Trade show the versions and results.
9. Every spoken instruction is also on screen; each key word shows with the host's beat at first use; the frames can be left.
10. Every action works by keyboard as well as tap, nothing is shown by color alone, nothing is timed, and motion can be paused.
11. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
12. Motion off: the snow is still; no network requests.

## Open questions
- For Cory: the grades no longer share the bus. Grade 7 moves to the diner and grade 8 to the plow and radio room on the same night, so each grade has its own texts. Default used: this split. Say if all three should stay on the bus with different models.
