# Dramatic Irony Theater

## One idea
The student directs a short play and places one card that decides when the audience learns the secret (before the scene, halfway, or never), runs the same lines three ways while an audience meter shows suspense and laughter rise or fall, and tags what each line does (moves the action, shows who someone is, forces a decision), so they learn that the gap between what the characters know and what the audience knows is what makes the same words tense, funny or just a surprise.

## Not like
- perspective-camera (6, spec): a narrator's point of view in prose. Here what a theater audience knows against what the characters know, grade 8.
- tension-meter (9, concept): graphing suspense from a story's structure. Here suspense made by one reveal card, with the same lines.
- flashback-editor (8, spec, this batch): reordering scenes in time with bridges. Here the order stays fixed and only the audience's knowledge moves.
- script-read-through (3-5, spec): rehearsing a part. Here directing what the audience is told.
- globe-theatre-stage (12, concept): staging Shakespeare. Here two short original scenes.

## Who and how
- Grade 8, ELA, module "Dialogue and Dramatic Irony" (Reading Literature). Standards: RL.8.3, RL.8.6.
- Driver: one student; class mode is "Hold the secret", where two students read the parts aloud and the class has seen the secret (tool.json `driver: "student"`). Every line is read on tap.
- Two one-act scenes written for Curio Class: "The Storm Line" (suspense) and "Surprise, Surprise" (comedy). tool.json `modes: ["The Storm Line", "Surprise, Surprise", "Side by side", "Hold the secret"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.
- Nothing is saved; `Print` prints the tagged script and the side-by-side notes.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.8.6 | Place the reveal card (before, halfway, never) and run the scene | the audience meter's suspense and laughter lines | 2 |
| RL.8.6 | Compare the three runs and pick lines that turned tense or funny only because the audience knew more; explain the gap | the side-by-side meters with the student's picks | 4 |
| RL.8.3 | Pause on a line and tag it: moves the action, shows character, forces a decision | the tagged script | 3 |
| RL.8.3 | Predict how the tension resolves before the last page, naming the line that set it up | the prediction card beside the ending | 5 |

## Screens and modes
Header (kit): title "Dramatic Irony Theater"; `Stage`, `Script`, `Side by side`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A small theater with red curtains, a director's chair, a clapboard and three slots in front of the stage marked Before, Halfway and Never; the stage manager, Rosa Quintero, holds the reveal card. First hint: "Tap the reveal card to hear the secret." The first tap reads the secret; the welcome is queued after it (`welcomeAfter: true`).

**The two scenes.**
- "The Storm Line": Maya, sixteen, is babysitting at the Okafors' house. The phone keeps ringing and going dead; the porch light flickers; a branch scrapes the window. The secret: a storm has knocked down the phone line two streets away, and the caller is Mr. Okafor trying to say they will be late. About 24 lines.
- "Surprise, Surprise": friends Jun and Talia are each secretly planning a surprise party for the other on the same Saturday, and each keeps making excuses to the other. The secret: both parties are at the same park pavilion. About 24 lines.

**Stage.** The student drags the reveal card to a slot and taps `Curtain`. The scene plays with illustrated actors, speech bubbles and stage sound; the meter under the stage draws two lines as it plays, Suspense and Laughter, each step keyed per line and per reveal setting. With the reveal Before, Maya's "Hello? Who is this?" pushes suspense up; with Never, it is flat until the last line ("It was Dad. The storm knocked the line out.") gives a jump of surprise and no build. In the comedy, Before makes every excuse a laugh line ("I'm busy Saturday. Dentist."); Never makes the same lines plain until the ending.

**Script.** The student pauses on any line and tags it with one or more of: Moves the action, Shows character, Forces a decision. Each line has keyed tags with accepted alternates; a tag outside the key asks "What changes because of this line?" Before the last page the curtain holds and the student writes a prediction and taps the line that set it up.

**Side by side.** The three runs' meters stacked with the script beside them. The student marks two lines that changed most between runs and writes, for each, what the audience knew that the character didn't. A check needs the line's keyed secret word (storm, line, party, pavilion) or a character's name and "didn't know".

**Hold the secret.** The projector shows the secret to the class; two students read the parts from their own screens without it.

At 1366x768 stage, meter and script fit; at 680x425 the script is a tab.

## Content
Written for Curio Class: both scenes, with per-line keyed tags, the meter steps for each reveal setting, the secret words and the prediction keys. The storm scene has no intruder, no weapon and no harm; the scare is only noise, dark and a broken phone line.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The reveal card can move between runs at any time; each run's meter is kept until the page closes.
- With Motion off the curtain doesn't sweep and the actors don't move; the meter draws its finished lines at once.

## Look
- Accent `--brand` #8a1c2b curtain red (header, curtain, slots); gold #f4c542 (the reveal card, spotlight, meter peaks); paper #fcf2f3; ink #2b080d; muted #6b5054. Scene: a small school theater.
- Contrast (WCAG 2.1, computed): white on brand 9.20:1; brand on paper 8.39:1; ink on paper 16.74:1; muted on paper 6.60:1; ink on gold 11.29:1.
- Each scene has its own stage lighting: storm blue-gray and party yellow, both behind the brand frame.
- Never color alone: the meter lines are labeled Suspense and Laughter and drawn solid and dashed; slots have words.
- Different from this batch (editing-bay slate blue, bronze, surgical green, council violet).

## Art
- People art goes to Gemini: Rosa Quintero (a Mexican American woman in her forties with a headset and clipboard), 3 poses; Maya (a Nigerian American teen), 4 poses; Jun (a Korean American teen boy) and Talia (a white teen girl with a wheelchair), 4 poses each; "illustrated stage actor <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): theater with curtains (1); a living room set at night in a storm (1); a park pavilion set with streamers (1).
About 18 images. Drawn in code: meter, reveal slots, speech bubbles, script tags.

## Voice
Bank voice `upbeat-guide` as Rosa and the hint voice (unique in this batch); Maya and Talia are read by `big-sister`, Mr. Okafor and Jun by `friendly-dad` (both unique in this batch). `Curio.voice` with `scope: () => state.scene + ':' + state.view + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: "You're the director. Decide when the audience learns the secret, then watch the same lines change."
- event `secret`: the scene's secret.
- event, whole, `line`: the line as acted.
- event `tagAsk`: "What changes because of this line?"
- event `predict`: "Curtain's holding. How does it end?"
- event `compare`: "Which line changed the most?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: scene scripts with per-line tags, meter steps per reveal setting, the reveal slots, the three-run comparison, the secret-word check.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tag every line Moves the action | Each line is keyed; at least half the tags must match for the scene to count, and the print shows misses. |
| Side by side | Pick two lines at random | The two picks must be among the keyed lines that changed by a set amount between runs. |
| Gap note | Write "it was funny" | The note needs the keyed secret word or a character's name and what they didn't know. |
| Prediction | Write it after the ending | The curtain holds; the ending plays only after the prediction is in. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the reveal card: `secret`, `welcome` (queued, first time).
2. Curtain: `line` (whole) per line in order; `predict` when the curtain holds.
3. Script: `tagAsk` as it fires.
4. Side by side: `compare` on open.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.8.3 and RL.8.6 wording (dramatic irony; dialogue that propels action, reveals character, provokes a decision) | thecorestandards.org, Reading Literature Grade 8 | CCSS ELA 2010 PDF | yes |
| Dramatic irony: the audience understands something the character does not | Merriam-Webster, dramatic irony | Britannica, dramatic irony | yes |
Backed twice: 2. Cut: 0.

Design choices (not claims): both scenes and the meter steps are written for Curio Class; the meter shows a designed reading, labeled "How an audience might feel".

Checks run (Python, scratchpad b23, 2026-11-09): each scene has at least two lines keyed to each tag; in each scene at least four lines change suspense or laughter by two steps or more between Before and Never; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 stage, meter and script fit; at 680x425 the script is a tab.
2. The reveal card sets each run, and the meter draws keyed suspense and laughter lines. (RL.8.6)
3. Lines take keyed tags with alternates. (RL.8.3)
4. Side by side takes two keyed lines with gap notes. (RL.8.6)
5. The curtain holds for a prediction tied to a line. (RL.8.3)
6. Hold the secret shows the secret only on the projector.
7. Print shows the tagged script and notes.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: curtain and actors are still and the meter draws at once; no network requests.

## Open questions
- None for Cory.
