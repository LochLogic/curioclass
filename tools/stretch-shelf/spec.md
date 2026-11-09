# Stretch Shelf

## One idea
A reading trail climbs from a shelf of stories, poems, plays and fact texts at the student's grade to a stretch text at the top of the grade band, and the student reads the stretch text with three supports on (word taps, chunk recaps and audio), switching them off one at a time as they feel ready, answering a quick check at each chunk, and filling a range map across genres and subjects, so they learn that hard texts get easier with the right supports and that a strong reader reads widely, until they finish a top-of-band text with all supports off.

## Not like
- read-along-shelf (K-2, concept): the same skill one band down, with read-alongs. Here grades 3-5, supports a student switches off, and a range map.
- research-rover (4, concept): finding and using sources. Here reading range and stamina.
- side-by-side-reader (3-5, spec): comparing two texts. Here reading one at a time, widely.
- mood-in-the-pictures (3-5, spec): what pictures and sound add. Here audio is a support to switch off.
- deadline-desk (3-5, spec): writing stamina. Here reading stamina.

## Who and how
- Grades 3-5, ELA, module "Reading Range and Text Complexity" (Reading). Standards: RL.3.10, RL.4.10, RL.5.10, RI.3.10, RI.4.10, RI.5.10.
- Driver: one student (tool.json `driver: "student"`).
- Grade picker (3, 4, 5) sets the shelf; each grade has 8 texts (2 stories, 2 poems, 1 play, 3 fact texts across science, history and the arts) plus 2 stretch texts. tool.json `modes: []`, `minutes: "15-30 per text"`, `grades_label: "Grades 3-5"`.
- Saving: the range map and which supports were off are kept in this browser (localStorage, try/catch); the footer says "Your reading map stays on this device." `Clear my map` removes it. Without storage, the map lasts until the page closes.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.3.10, RL.4.10, RL.5.10 | Read stories, poems and a play at grade level, chunk by chunk, with checks | the literature row of the range map filling | 2, 3 |
| RI.3.10, RI.4.10, RI.5.10 | Read fact texts in science, history and the arts | the informational row filling | 2, 3 |
| RL.x.10, RI.x.10 (independently, top of band) | Read a stretch text and switch supports off one at a time | three support switches and a "supports off" badge | 4, 5 |
| RL.x.10, RI.x.10 (range) | See genres and subjects covered on the map and pick a missing one | empty squares that glow as suggestions | 6 |

## Screens and modes
Header (kit): title "Stretch Shelf"; `Shelf`, `My map`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A forest trail climbing to a lookout, with a shelf at the trailhead and Coach Fern, a mountain goat in a trail cap. First hint: "Tap a book on the shelf to start." The first tap names the text; the welcome is queued after it (`welcomeAfter: true`).

**Reading view.** Focus: the text in chunks (each 70 to 180 words, one chunk shown at a time, 18 px or larger, line length up to 70 characters). Three support switches at the top, all on to start:
- Word taps: bold words can be tapped for a kid definition and a picture.
- Chunk recaps: after each chunk, a two-sentence recap appears before the check.
- Audio: the chunk is read aloud with each sentence lit; it can be replayed.
Switching one off is the student's choice; the hint suggests it after two chunks in a row with checks right on the first try ("Ready to try it with Audio off?"). Turning a support back on is always allowed, with no penalty.

**Chunk check.** Two quick questions per chunk (pick one of three), one about what happened or what was said, one about a word or a why. A wrong pick shows the sentence that answers it; the student picks again.

**Finish.** A trail marker: the text's genre and subject square on the range map fills, with a badge for the supports that were off at the end ("Read with no supports").

**Range map.** A grid: rows Story, Poem, Play, Science, History, Arts; columns Grade text and Stretch. Empty squares glow and suggest a text.

At 1366x768 the reading view fits without scrolling inside a chunk; at 680x425 the switches fold into a `Supports` menu.

## Content
Texts are public domain or written for Curio Class; grade-level placement uses the standards' three-part view of complexity (counts like sentence and word length, a qualitative read of structure and meaning, and the reader and task), and the tool shows no number on texts.
- Grade 3 shelf: "The Lion and the Mouse" and "The Fox and the Crow" (Aesop, 1919 Library of Congress tellings); "Who Has Seen the Wind?" (Christina Rossetti, 1872) and "Rain" (Robert Louis Stevenson, 1885); a play "The Lost Lunchbox" (original); fact texts "How Bats See in the Dark" (science), "The First Public Libraries" (history), "How a Drum Makes Sound" (arts). Stretch: "The Ugly Duckling" (Hans Christian Andersen, a public-domain English translation, abridged in chunks) and "Why Leaves Change Color" (original, top-of-band).
- Grade 4 shelf: "The Owl and the Pussy-cat" (Edward Lear, 1871); a chapter from "The Velveteen Rabbit" (Margery Williams, 1922); originals in science, history and the arts. Stretch: an original article on the Erie Canal and a longer Velveteen Rabbit chapter.
- Grade 5 shelf: similar mix with originals on the water cycle, the Underground Railroad's network (told with care, with sources), and how murals are made. Stretch: "The Real Princess" (Andersen) and an original article on volcano monitoring.
Every fact in original texts is sourced at build in the text's data file (two sources each).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Support switches are 44 px toggles with words (On, Off); the state shows in the chunk's corner.
- Checks are never scored as a test; the map records finished texts, not marks.
- The student can leave a text and come back; the chunk position is kept with the map.

## Look
- Accent `--brand` #2d6a4f trail green (header, switches, trail markers); gold #f4c542 (filled map squares, the lookout flag); paper #f4f9f6; ink #10241b; muted #4c5e55. Scene: a forest trail climbing to a lookout.
- Contrast (WCAG 2.1, computed): white on brand 6.39:1; brand on paper 6.00:1; ink on paper 15.29:1; muted on paper 6.49:1; ink on gold 10.01:1.
- Never color alone: map squares show a check mark and the text's title; switches say On or Off.
- Different from this batch (game-show violet, block brick, fair red, clinic blue).

## Art
Local FLUX (`scripts/localart.py`).
- trail (1): "A forest trail climbing to a lookout with a bookshelf at the trailhead, soft gouache, no text"; 16:9; cutout no.
- Coach Fern (4, wave, point, cheer, sit and read): "A friendly mountain goat in a trail cap <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- text covers (30): one per text; 3:4; cutout no. For public-domain texts, a public-domain illustration may be used instead if its rights page says public domain (id logged at build).
- word-tap pictures (about 120): small spot pictures; 1:1; cutout yes.
About 155 images. Drawn in code: switches, chunks, map.

## Voice
Bank voice `easy-coach` as Coach Fern and the read-along voice (unique in this batch). `Curio.voice` with `scope: () => state.text + ':' + state.chunk`, `welcomeAfter: true`.
- event `pick`: "{The Ugly Duckling}. A stretch text!"
- how `welcome`: "Welcome to the trail. Every text has three supports. Read with them on, and switch one off when you feel ready."
- event, whole, `chunk`: the chunk read aloud (Audio on).
- event, whole, `word`: the tapped word's definition.
- how `checkHow`: "Quick check. Tap the best answer."
- event `lookBack`: "Here's the sentence that tells you. Try again."
- event `ready`: "Two right in a row. Ready to try it with {Audio} off?"
- event `marker`: "Trail marker! {Poem} done."
- event `summit`: "Top of the trail, with no supports. That's a stretch!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Chunk checks | Guess | One in three; a wrong pick shows the answering sentence. It's practice, not a score. |
| Supports off badge | Switch off, then back on | The badge records the supports off at the end of the text; turning one back on is fine and shown honestly. |
| Range map | Read only stories | The map shows empty rows and suggests texts; it is a nudge, not a gate. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a text: `pick`, `welcome` (queued, first time).
2. Each chunk: `chunk` (whole, Audio on); word taps: `word` (whole).
3. Check: `checkHow` (first time); wrong: `lookBack`; streak: `ready`.
4. Finish: `marker`; stretch with no supports: `summit` (waits).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.3.10 to RL.5.10 and RI.3.10 to RI.5.10 wording | thecorestandards.org, Reading Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
| Text complexity has three parts: quantitative, qualitative, and reader and task | CCSS ELA Appendix A | Achieve the Core, text complexity guidance | yes |
| The listed texts are public domain (Aesop 1919, Rossetti 1872, Stevenson 1885, Lear 1871, Williams 1922, Andersen translations) | Project Gutenberg, each text's page | Library of Congress or HathiTrust records for each edition | yes |
Backed twice: 3. Cut: 0.

Sensitivity note: the grade 5 Underground Railroad text goes to the fresh-agent review.

Checks run (Python, scratchpad b10, 2026-11-08): a sample opening chunk of The Ugly Duckling runs 78 words, inside the 70 to 180 chunk range; 10 texts per grade; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 a chunk reads without inner scrolling; at 680x425 switches fold into a menu.
2. Every shelf has stories, poems, a play and fact texts in three subjects. (RL.x.10, RI.x.10)
3. Chunk checks show the answering sentence on a wrong pick.
4. Each support switches off and back on, and the badge reflects the end state.
5. The stretch text can be finished with all supports off. (RL.x.10, RI.x.10)
6. The range map fills, suggests missing squares, and survives a reload where storage works; `Clear my map` removes it.
7. Text is 18 px or larger with line length up to 70 characters.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the trail doesn't scroll; no network requests.

## Open questions
- None for Cory.
