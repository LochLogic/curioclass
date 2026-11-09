# Slow-Mo Writer

## One idea
The student lays a short true-to-life story out as a film strip, one frame per sentence, finds the big moment and stretches it into five frames using five lenses (what I saw, heard, felt in my body, thought, and said), and squeezes the dull parts into a single fast-forward frame with time words (later that day, after lunch); a pace graph under the strip shows where the story races and where it slows, so they learn that writers control time by giving the moment that matters the most words.

## Not like
- show-don-t-tell (3, spec): one feeling shown in one scene. Here the pacing of a whole story.
- blizzard-scenes (5, concept): settings and mood. Here time and pace.
- story-spine (K-2, concept): beginning, middle, end. Here grade 5 pacing across a whole narrative.
- dialogue-director (3, spec): dialogue staging. Here dialogue is one of five lenses on one moment.
- comma-chameleon (4, spec): punctuation. Here narrative pacing.

## Who and how
- Grade 5, ELA, module "Narrative Pacing" (Writing). Standards: W.5.3 (a, b, c, d, e), W.5.5.
- Driver: one student (tool.json `driver: "student"`). Every frame is read on tap; the student's own sentences are read back by the browser's speech voice.
- Three starter stories (The Bike Fall, The First Dive, Lost in the Store), then the student's own story. tool.json `modes: ["Starter stories", "My story"]`, `minutes: "25-40"`, `grades_label: "Grade 5"`.
- Saving: the student's own strip is kept in this browser; footer: "Your story stays on this device." `Clear my story` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.5.3a | Set the opening frame: who, where and the problem | the first frame with three tags | 2 |
| W.5.3b (pacing) | Find the big moment and stretch it with the five lenses | five new frames at the moment and a tall bar on the pace graph | 3 |
| W.5.3b (description, dialogue) | One stretched frame must be a "said" frame (dialogue) and one a "felt" frame | lens icons on frames | 3 |
| W.5.3c | Squeeze dull frames into one fast-forward frame with a time word | the fast-forward frame and a flat bar | 4 |
| W.5.3d | Swap three plain words in the big moment for exact ones from a word tray | the swapped words underlined | 5 |
| W.5.3e | Pick an ending frame that follows from the moment | the last frame | 6 |
| W.5.5 | Compare the first strip and the revised strip on the pace graph | two graphs, before and after | 6 |

## Screens and modes
Header (kit): title "Slow-Mo Writer"; `Stories`, `My story`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** An editing desk with a light table, a film strip lying across it and Reel, a little film camera with legs and a director's cap. First hint: "Tap a story to load its film strip." The first tap reads the story's title; the welcome is queued after it (`welcomeAfter: true`).

**Strip.** Each sentence is a frame, left to right; tap a frame to hear it. Under the strip, the pace graph: one bar per stretch of story time, its height the number of words spent on it. The starter strip is evenly paced and flat (every event gets one sentence, including "We ate breakfast" and "The big moment").

**Find the moment.** The student taps the frame they think is the big moment (the key accepts one or two frames per story). A wrong pick gets "Is this where everything changes?" and the student may keep going.

**Stretch.** The moment frame opens into five lens slots: See, Hear, Feel (in my body), Think, Say. Each slot has three sentence chips written for that story plus a type box. The student fills at least four, including Say and Feel. Each filled slot becomes a frame; the pace graph's bar for the moment grows.

**Squeeze.** Dull frames glow when tapped together (two or more in a row); `Fast-forward` merges them into one frame that needs a time word from a tray (later that day, after an hour, by the time, the next morning, meanwhile). The bar for that stretch flattens.

**Exact words.** Three plain words in the moment glow (went, big, said); a tray offers exact words (skidded, towering, gasped). The student picks one that fits the sentence; the data marks which fit.

**Ending.** Three ending frames to pick from; the one that follows from the moment is marked in data; the others get a gentle "Does this end come from what happened?"

**Before and after.** Two pace graphs side by side; `Play` reads the revised strip from start to end.

**My story.** A blank strip of up to 15 frames; the same tools; nothing is scored; the tool only checks the stretched moment has at least four lens frames and the strip has one fast-forward frame.

At 1366x768 the strip, lens slots and graph fit; at 680x425 the strip scrolls sideways inside its own box (the page doesn't scroll sideways).

## Content
Written for Curio Class:
- The Bike Fall (a girl's first ride down a steep hill, the fall, her brother's help).
- The First Dive (a boy on the diving board at the city pool, the jump, coming up laughing).
- Lost in the Store (a child loses a parent in a big store, panic, a clerk helps, the reunion).
- Each starter: 10 to 12 even frames, the moment key, 15 lens chips (3 per lens), 3 plain words with exact swaps, 3 endings.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Frames can be dragged to reorder; lens frames stay together.
- Typed sentences are read back; they aren't judged.
- With Motion off the graph bars change height without growing.

## Look
- Accent `--brand` #7a4b14 film sepia (header, strip edges, sprocket holes); gold #f4c542 (the moment frame, the light table glow); paper #fbf6ef; ink #271706; muted #62564a. Scene: a warm editing room.
- Contrast (WCAG 2.1, computed): white on brand 7.38:1; brand on paper 6.87:1; ink on paper 16.12:1; muted on paper 6.62:1; ink on gold 10.66:1.
- Never color alone: lens frames carry icons and words; the graph shows word counts as numbers.
- Different from this batch (detective navy, stage pink, track teal, courtroom mahogany).

## Art
- People art goes to Gemini: one picture per starter's big moment and one per opening (6), "children's book illustration <scene>, warm watercolor, no text"; 4:3.
- Local FLUX (`scripts/localart.py`): editing desk (1); Reel (4 poses: point, cut, think, cheer), "A friendly little vintage film camera character with legs and a director's cap <pose>, soft gouache, plain white background"; 1:1; cutout yes.
About 11 images. Drawn in code: strip, frames, lens slots, graph.

## Voice
Bank voice `easy-coach` as Reel (unique in this batch); starter strips are read by `casual-peer` (unique in this batch), since they're told by a kid. `Curio.voice` with `scope: () => state.story + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Writers control time. Slow down the moment that matters, and speed through the rest."
- event, whole, `frame`: the tapped frame.
- event `notMoment`: "Is this where everything changes?"
- how `stretchHow`: "Stretch it. Fill the lenses: what you saw, heard, felt, thought and said."
- how `squeezeHow`: "Tap the slow frames in a row, then Fast-forward with a time word."
- event `graph`: "Look at your graph. The moment is the tallest part now."
- event `play`: the revised strip, read whole.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: frame strip, lens slots, merge, word swap, pace graph.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Moment | Pick any frame | The key accepts one or two frames; others get a question, and the graph shows a stretched dull part. |
| Stretch | Fill one lens | At least four lenses, including Say and Feel. |
| Squeeze | Skip it | Done needs one fast-forward frame with a time word. |
| Exact words | Pick any | Each swap is marked fit or not for its sentence. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a story: title, `welcome` (queued, first time).
2. Frames: `frame` (whole). Moment: `notMoment` if wrong; `stretchHow` (first time).
3. After the stretch: `squeezeHow` (first time), then `graph`.
4. `Play`: `play`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.5.3 and W.5.5 wording | thecorestandards.org, Writing Grade 5 | CCSS ELA 2010 PDF | yes |
| Pacing in narrative: slowing down the important moment with detail and speeding through less important time with transitions | ReadWriteThink, narrative writing and pacing lessons | Reading Rockets, writing personal narratives | yes |
Backed twice: 2. Cut: 0.

Design choices (not claims): the five lenses; the four-lens rule; the pace graph's measure (words per stretch of story time).

Checks run (Python, scratchpad b15, 2026-11-09): for a sample starter strip, the moment bar is the tallest after a four-lens stretch and a two-frame squeeze; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the strip, slots and graph fit; at 680x425 the strip scrolls in its own box.
2. The opening frame takes who, where and the problem. (W.5.3a)
3. The moment stretches with at least four lenses including Say and Feel. (W.5.3b)
4. Fast-forward merges frames with a time word. (W.5.3c)
5. Exact word swaps are marked fit. (W.5.3d)
6. Endings and before-and-after graphs work. (W.5.3e, W.5.5)
7. My story survives a reload where storage works; `Clear my story` removes it.
8. Print shows the strip and graph.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: bars don't grow; no network requests.

## Open questions
- None for Cory.
