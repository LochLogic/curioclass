# Flashback Editor

## One idea
The student cuts a short story told in order into scenes on a film editor's timeline and rebuilds it with a flashback, writes a bridge at every jump in time (a time phrase, a sense that pulls the narrator back, or a line of reflection), and sends the cut to a test reader who drops a "lost" flag at any jump left unbridged, so they learn that a flashback is a choice about pacing and that every shift in time has to be signaled.

## Not like
- blizzard-scenes (6-8, spec): rewriting a scene from a new point of view. Here the same scenes in a new time order, with written bridges, grade 8.
- slow-mo-writer (5, spec): slowing one moment down. Here pacing across a whole story with a flashback.
- tension-meter (9, concept): graphing suspense in a finished story. Here the student builds the structure.
- dramatic-irony-theater (8, spec, this batch): what the audience knows in a fixed play. Here the order of scenes changes.
- paragraph-surgeon (8, spec, this batch): the job of each sentence in a paragraph. Here scenes on a timeline.

## Who and how
- Grade 8, ELA, module "Narrative Techniques" (Writing). Standard: W.8.3 (a, b, c, d, e).
- Driver: one student; class mode is "Premiere", where a student's cut plays on the projector and the class raises a lost card (tool.json `driver: "student"`). Every scene and bridge is read on tap.
- The story "Starting Block" written for Curio Class in seven scenes, a second practice story "The Ferry" in five scenes, and the student's own scenes. tool.json `modes: ["Starting Block", "The Ferry", "My scenes", "Premiere"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.
- The student's own scenes stay only while the page is open. Nothing is saved; `Print` prints the cut with bridges, the pacing strip and the ending.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.8.3a, W.8.3c | Reorder scenes into a flashback structure; write a bridge at every time jump | the timeline with gap markers turning to bridges | 2 |
| W.8.3c | Choose the bridge kind: time phrase, sensory trigger, reflection | the bridge cards and the test reader's flags | 3 |
| W.8.3b, W.8.3d | Slow a key moment with description and dialogue; summarize a dull stretch | the pacing strip's scene lengths | 4 |
| W.8.3e | Write an ending that reflects on the whole experience and a note on what the flashback let the story do | the ending card and the side-by-side play | 5 |

## Screens and modes
Header (kit): title "Flashback Editor"; `Timeline`, `Pacing`, `Premiere`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A dim editing bay with two monitors and a timeline of seven scene clips in the order they happened; the editor, Wen, in a cardigan, sips tea at the desk. First hint: "Tap the first clip to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**"Starting Block".** Ines, thirteen, swims the 100 freestyle at the league final. Scenes in time order: 1 the summer she learns to dive; 2 the slip on wet tile at practice, a split chin and stitches; 3 three weeks out of the pool; 4 her coach, Ms. Dube, saying "Just get wet. That's all today"; 5 the first dive back; 6 the final, on the block; 7 the race and the wall. Each clip carries a "when" tag (two summers ago, last spring, today).

**Timeline.** The student drags clips into a new order. A starting suggestion card offers "Open on the block" without forcing it. Each cut where the "when" tag jumps shows a red gap marker. Tapping the marker opens a bridge card with three kinds: Time phrase ("Two summers ago, the tile was wet"), Sensory trigger ("The chlorine hit her, and she was back on that wet tile"), Reflection ("She hadn't known then how long three weeks could be"). The student writes the bridge in their own words; a kind check needs a time word, a sense word or a feeling-and-time pair. A bridge going back to the present is also required.

**Test reader.** `Send to reader` plays the cut; the reader, Teo, a ninth grader, reads clip by clip and drops a lost flag at any unbridged jump ("Wait, when is this?") and a "too fast" flag at a time phrase that only names a year with no link to the scene. A cut passes with no flags.

**Pacing.** A strip under the timeline shows each scene's length in words. The student picks one key moment to slow (adding description of the block, her hands, a line of dialogue from Ms. Dube) and one stretch to summarize (the three weeks out become two sentences). The strip changes as they write.

**Ending and note.** The student writes an ending that reflects on the experience, not only the result, then a note on what the flashback let the story do. Original and edit play side by side with their pacing strips.

**My scenes.** The student pastes their own scenes, tags each "when", and works the same way.

At 1366x768 the monitors and timeline fit; at 680x425 the second monitor is a tab.

## Content
Written for Curio Class: "Starting Block" (seven scenes, about 900 words) and "The Ferry" (five scenes: a boy's first ferry ride alone, and the storm crossing years earlier), each with "when" tags, bridge examples per kind and keyed summary targets. The fall in "Starting Block" is told without blood detail; the stitches are mentioned once.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Clips can move at any time; bridges stay with the cut they were written for and turn back into gap markers if the clips around them change.
- With Motion off clips don't slide and the playhead doesn't move; each clip highlights in turn.

## Look
- Accent `--brand` #24476b editing-bay slate blue (header, timeline, clip frames); gold #f4c542 (bridges, the playhead); paper #f1f5f9; ink #0b1a29; muted #4d5966. Scene: a dim editing room with two monitors.
- Contrast (WCAG 2.1, computed): white on brand 9.60:1; brand on paper 8.76:1; ink on paper 16.05:1; muted on paper 6.53:1; ink on gold 10.81:1.
- Never color alone: gap markers say "gap" and show a broken-link icon; flags have words.
- Different from this batch (curtain red, bronze, surgical green, council violet).

## Art
- People art goes to Gemini: Wen (a Chinese American man in his fifties in a cardigan), 3 poses; Teo (a Filipino American teen with headphones around his neck), 3 poses; "illustrated film editor <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`), no faces close up: an indoor pool from the stands (1), a starting block from behind (1), wet tile by a pool edge (1), a swimmer's hand on the wall (1), a ferry deck in a gray sea (1), the editing bay (1).
About 12 images. Drawn in code: timeline, gap markers, bridges, pacing strip.

## Voice
Bank voice `smooth-narrator` as Wen and the hint voice (unique in this batch); story scenes and Teo are read by `soft-breath` (unique in this batch). `Curio.voice` with `scope: () => state.story + ':' + state.view + ':' + state.clip`, `welcomeAfter: true`.
- how `welcome`: "This story is in the order it happened. Cut it so it starts where it matters, and build a bridge every time you jump in time."
- event, whole, `clip`: the tapped clip.
- event `gap`: "That's a jump in time. Build a bridge."
- event `lost`: "Wait, when is this?"
- event `pass`: "I followed every jump."
- event, whole, `cut`: the cut with bridges, as the test reader reads it.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: clips with "when" tags, gap detection, bridge kind checks, the test reader's flag rules, the pacing strip.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Flashback | Keep the original order | The cut must contain at least one backward jump and one return. |
| Bridges | Type "later" everywhere | A bridge needs a time word linked to the scene, a sense word or reflection; repeated bridges get "too fast". |
| Pacing | Leave lengths alone | The slowed moment must grow and the summarized stretch must shrink by a set share. |
| Ending | Write "She won" | The ending needs a reflection word (knew, learned, realized, felt) or links back to the flashback. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the first clip: `clip`, `welcome` (queued, first time).
2. Timeline: `gap` when a gap appears.
3. Send to reader: `cut` (whole), with `lost` at each flag; `pass` at the end with no flags.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.8.3 (a to e) wording, including transitions that signal shifts in time frame and a conclusion that reflects on the experience | thecorestandards.org, Writing Grade 8 | CCSS ELA 2010 PDF | yes |
| A flashback interrupts a story's order to show an earlier event | Merriam-Webster, flashback | Britannica, flashback | yes |
| Writers speed up time with summary and slow it down with scene (description and dialogue) | Purdue OWL, narrative writing | ReadWriteThink, pacing in narrative | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): both stories are written for Curio Class; Ines's league and coach are made up.

Checks run (Python, scratchpad b23, 2026-11-09): every pair of adjacent clips with different "when" tags in the suggested cut is flagged until bridged; each sample bridge passes the kind check for its kind and a bare "later" fails; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 monitors and timeline fit; at 680x425 the second monitor is a tab.
2. Clips reorder and gaps appear at time jumps. (W.8.3a, W.8.3c)
3. Bridges take a kind check; the test reader flags unbridged jumps. (W.8.3c)
4. The pacing strip responds to a slowed moment and a summarized stretch. (W.8.3b, W.8.3d)
5. The ending and note play beside the original. (W.8.3e)
6. My scenes works with pasted scenes.
7. Premiere and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: clips and playhead are still; no network requests.

## Open questions
- None for Cory.
