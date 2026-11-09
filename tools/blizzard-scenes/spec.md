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
- Driver: one student, or students trading scenes (tool.json `driver: "student"`). Every sentence is read on tap; the student's scenes are read back by the browser's speech voice.
- Grade picker: 6 (write and retell), 7 (adds the two-narrator reading), 8 (adds two model structures and the reorder). tool.json `modes: ["Grade 6", "Grade 7", "Grade 8"]`, `minutes: "35-50"`, `grades_label: "Grades 6-8"`.
- Saving: the student's scenes are kept in this browser; footer: "Your scenes stay on this device." `Clear my scenes` removes them.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.7.6 | Read the driver's and the new kid's versions; mark lines as knows, notices or hides for each narrator | two columns with marks and lit "only this narrator" lines | 2 |
| W.6.3 | Pick a seat and write a scene with a narrator, dialogue, description and a slow moment, using the prompt strip | the student's scene with prompt ticks | 3 |
| W.7.3 | Rewrite from another seat; facts only one narrator could know light up across the two columns | two columns of the student's versions | 4 |
| RL.8.5 | Compare two model structures (in order, and starting at the end) and answer what each does to suspense | the two models with structure strips | 5 |
| W.8.3 | Reorder: start at the headlights, go back, with time-shift transitions and a reflective ending | the third version and its transitions | 6 |

## Screens and modes
Header (kit): title "Blizzard Scenes"; `Models`, `My scenes`, `Side by side`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A school bus at night, half buried in snow beside a dark gas station with one flickering light, and the seating chart: the driver (Mr. Hale), a nervous chaperone (Ms. Duarte), the quiet new kid (Ren), the class clown (Dez) and an empty seat marked "You". First hint: "Tap the driver's seat to hear his version." The first tap reads the scene's title; the welcome is queued after it (`welcomeAfter: true`).

**Models.** Two versions of the same 20 minutes (about 350 words each), written for Curio Class: the driver's (he knows the radio said the plow is coming in an hour; he hides his worry from the kids) and Ren's (Ren notices the gas station's back door is open and a light moving inside; Ren doesn't know about the plow). The student marks sentences knows, notices or hides for each narrator. Lines only one narrator could know light up when both are marked.

**My scene.** The student picks a seat (any of the five) and writes in a text box with a prompt strip: a line of dialogue, one detail for each of two senses, a slow moment, what your narrator doesn't know. Prompts tick when the student taps them as done; nothing is scored.

**Rewrite from another seat.** The student picks a second seat and rewrites. The two versions sit in columns; the student taps facts that only one narrator could know (a list builds under each column).

**Grade 8: models and reorder.** Two short model texts with different structures (the driver's version in order, and a version that starts at the end, when the plow's lights appear, and goes back). Structure strips show each as blocks in story time. Then the student reorders their own scene: a strip of their paragraphs to drag, a transition tray for time shifts (Two hours earlier, Back then, Now, By the time) and a reflective ending box.

**Side by side.** Up to three versions in columns and four questions: what does the reader know first in each; which has the most suspense; whose feelings are hidden; which ending lands. The student answers in a line each.

At 1366x768 two columns fit; at 680x425 versions are tabs.

## Content
Written for Curio Class:
- The setting: a class trip bus heading home from a science museum, a sudden blizzard, a closed gas station on a two-lane road, the radio, the plow coming. No one is hurt; the moving light is the station owner checking her pipes, who brings blankets and cocoa.
- Models: the driver's and Ren's versions (grade 7); the in-order and end-first versions (grade 8).
- Mark key: each model sentence marked by narrator for knows, notices, hides.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Scenes autosave as the student types.
- Class trade: `Trade` makes a printable copy for a classmate to rewrite from a third seat.
- With Motion off the snow is still.

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

## Family engine
None. Tool-only code: narrator marks and the only-one comparison, text boxes with prompt strips, paragraph reorder with a transition tray, side-by-side columns.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Marks | Mark everything "knows" | Marks are compared with the key and differences shown; "only" lines light only when marks are right. |
| My scene | Write one line | Nothing is scored; prompt ticks are the student's own, and the side-by-side questions need two versions. |
| Reorder | Keep the same order | The reorder needs the headlights paragraph first and a transition at each jump. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the driver's seat: title, `welcome` (queued, first time).
2. Models: `sentence` (whole); `markHow` (first time); `only` as it fires.
3. My scenes: `seatHow`; grade 8 reorder: `reorderHow`.
4. Side by side: `side`.

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
2. Model marks work and "only" lines light. (RL.7.6)
3. My scene takes a seat and text with prompts. (W.6.3)
4. The rewrite shows two columns and only-one facts. (W.7.3)
5. Grade 8 models show structure strips with questions. (RL.8.5)
6. The reorder needs the headlights first and transitions. (W.8.3)
7. Scenes survive a reload where storage works; `Clear my scenes` removes them.
8. Print and Trade show the versions.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: the snow is still; no network requests.

## Open questions
- None for Cory.
