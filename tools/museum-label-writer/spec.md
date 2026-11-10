# Museum Label Writer

## One idea
The child is a junior curator writing the label for a real clay tablet from about 3100 BCE, one of the earliest kinds of writing, a record of barley pressed into clay in Mesopotamia; from a drawer of fact cards they put the steps of how writing began in order (clay counting tokens, tokens sealed in clay envelopes, marks pressed into tablets, picture signs for words, then signs for sounds), write a label with a reason, the steps in order, an example and a detail, and one honest "what we don't know" line; then they repair two sample labels whose steps jump around or skip a link, and reshape their own label three ways (a 40-word trail card for kids, an audio-guide script read aloud, a web page with images), so a sixth grader learns to build a clear explanation, critique an explanation's structure, and adapt it for real audiences.

## Not like
- river-kingdom (6, spec): life and law in Mesopotamia. Here writing an explanation of how writing began.
- colonial-newsroom (8, concept): writing with a point of view. Here a plain explanation for a museum.
- history-article-review (5, spec): reviewing someone else's history article. Here writing and repairing labels.
- headline-writer (ELA, concept): main ideas of news stories. Here an explanation for three audiences.

## Who and how
- Grade 6, Social Studies (Taking Informed Action), module "Museum Label Writer". Standards: D4.2.6-8 (construct explanations using reasoning, correct sequence, examples, and details with relevant information and data, while acknowledging the strengths and weaknesses of the explanations), D4.5.6-8 (critique the structure of explanations), D4.3.6-8 (present adaptations of arguments and explanations on topics of interest to others to reach audiences and venues outside the classroom using print and oral technologies and digital technologies).
- Format: studio. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Four parts: Gather and order, Write the label, Repair two labels, Three audiences. Extra: Gallery wall (finished labels printed as a class wall, one per page). tool.json `modes: ["Studio", "Gallery wall"]`, `minutes: "30-40"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D4.2.6-8 | Order five step cards, then fill the label's four parts (reason, sequence, example, detail) and one "what we don't know" line | the label card with its parts marked; the step strip | 2, 3 |
| D4.5.6-8 | Repair two sample labels: one with steps out of order, one with a missing link | the sample labels with movable sentences; the curator's check | 4 |
| D4.3.6-8 | Reshape the label into a 40-word trail card, an audio script, and a web page | three output frames with word counts and a read-aloud timer | 5 |

## Screens and modes
Header (kit): title "Museum Label Writer"; `Studio`, `Gallery wall`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A museum gallery: a glass case holds a small clay tablet with pressed marks, and beside it an empty white label card. A curator's wooden drawer sits below. The welcome is queued (`welcomeAfter: true`): "This clay tablet is about five thousand years old. It's one of the first kinds of writing. Visitors need a label that explains how writing began. Open the curator's drawer." First hint: "Tap the drawer."

**Gather and order (focus: the drawer and the step strip).** At 1366x768 the drawer opens left with fact cards, the step strip runs across the bottom and the case sits right; at 680x425 the drawer is a sheet.
- Fact cards (each with a picture and a source line): small clay tokens in shapes (cones, spheres, disks) used to count goods for thousands of years before writing; tokens sealed inside hollow clay balls ("envelopes") with their shapes pressed on the outside, around 3500 BCE; flat tablets with marks pressed in, recording numbers of things, around 3300 to 3100 BCE at Uruk; picture signs for words (a sign for barley, a sign for sheep); signs used for their sounds, so names and whole sentences could be written, over the following centuries, in wedge-shaped cuneiform.
- The child drags five step cards onto the strip in order. A wrong order plays "Which came first? Look at the dates on the cards."
- Distractor facts (true but off the point: "Clay was everywhere in Mesopotamia"; "Scribes trained for years") can be used as details, not steps.

**Write the label (focus: the label card).** Four parts built from tiles plus one free line each: Reason (why people needed writing: to keep track of grain, animals and who owed what), Sequence (the steps, from the strip), Example (this tablet: a record of barley), Detail (one fact card). Then a "What we don't know" line from three honest choices: scholars debate whether tokens led straight to writing; we can read the numbers on the earliest tablets better than some of the signs; writing may also have begun separately in Egypt around the same time. A word counter keeps the label under 120 words.

**Repair two labels (D4.5.6-8).** Two sample labels written by "other junior curators" (made for this game):
1. Steps out of order: it says signs for sounds came first, then pictures, then tokens. The child drags its sentences into order; the curator's check lights each fixed link.
2. A missing link: it jumps from tokens straight to full sentences. The child picks the missing step card and drops it in the gap.
Curator (made for this game): "A good explanation goes step by step, and each step leads to the next."

**Three audiences (the aha).** The same explanation reshaped:
- Trail card for kids: 40 words or fewer, one picture, one question for the reader. The counter turns gold at 40.
- Audio guide: a script to read aloud in about 45 seconds; `Read` speaks the child's script so they can hear the timing. If the child chooses to record their own voice, the screen says "Your recording stays on this device. It is never sent anywhere." (local MediaRecorder; no speech recognition; the recording is deleted when the page closes unless printed as text).
- Web page: a heading, the label, two images with captions, and a "Learn more" line naming the museum.
Narrator: "Same truth, three shapes. Each audience needs it a different way."

**The end.** The finished label in the case, the repaired samples and the three versions. `Print` prints the label card, the trail card, the audio script and the web page.

**Gallery wall (extra).** Prints each label as its own page for a classroom wall.

## Content
- Ten fact cards (five steps, five details), the step strip, label tiles, three "what we don't know" lines, two flawed sample labels with answers, the three output frames.
- The curator and the sample labels are made up and labeled; the tablet and every fact are real.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Recording is optional, off by default, needs a tap on `Record my voice` and the browser's own permission; nothing is uploaded.
- The trail card won't print over 40 words; the counter names how many to cut.
- Keyboard: Tab to cards, tiles and sentences; Enter to pick up; arrows to move; Enter to drop.
- With Motion off the drawer opens without sliding.

## Look
- Accent `--brand` #8f3b1b clay terracotta (header, the drawer, step numbers); gold #f4c542 (the picked card, a fixed link); paper #fbf3ee; ink #2c1006; muted #625149.
- Contrast (WCAG 2.1, computed): white on brand 7.48:1; brand on paper 6.82:1; ink on paper 16.18:1; muted on paper 6.86:1; ink on gold 10.91:1.
- Never color alone: label parts carry their names (Reason, Sequence, Example, Detail); fixed links carry a check.
- Different from this batch (field trip teal, river green, smoke slate, lake blue).

## Art
- Public domain (Met Open Access, id checked at build for the open-access flag): a proto-cuneiform tablet recording barley, Jemdet Nasr period, about 3100 to 2900 BCE (the Met's proto-cuneiform administrative tablets are the first choice); a later cuneiform tablet for comparison. Each with credit.
- Local FLUX (`scripts/localart.py`): the gallery with the case (1, 16:9); clay tokens (1, 1:1); a clay envelope (1, 1:1).
- People art goes to Gemini with `people: true`: the curator (2 poses; cutout yes).
- Drawn in code: the drawer, cards, the step strip, the label card, the three output frames.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the curator; `clear-teacher` as the narrator and the voice that reads the child's audio script. `Curio.voice` with `scope: () => state.mode + ':' + state.part + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `drawer`: "Drag the five step cards onto the strip in order."
- event, whole, each fact card.
- how `write`: "Fill each part of the label."
- how `unknown`: "Pick one honest thing we don't know."
- how `repair`: "Drag the sentences into order."
- how `gap`: "Find the missing step and drop it in the gap."
- how `shape`: "Pick a version: trail card, audio guide or web page."
- event, whole, the child's audio script when they tap Play script.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the drawer and step strip, the four-part label builder with a word counter, the sentence-repair puzzles, three output frames, optional local recording.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Step order | Leave cards in the drawer's order | The drawer shuffles; the strip checks dates. |
| Label | Fill only the example | Print waits for all four parts and the "what we don't know" line. |
| Repair | Swap sentences at random | Each link checks; the curator names the gap. |
| Trail card | Paste the whole label | Over 40 words can't print; the counter says how many to cut. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `drawer`; fact cards (whole), each waits.
2. `write`; `unknown`.
3. `repair`; `gap`.
4. `shape`; script (whole); `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D4.2.6-8, D4.5.6-8 and D4.3.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Clay tokens counted goods long before writing; tokens sealed in clay envelopes around 3500 BCE | Schmandt-Besserat, "How Writing Came About" (University of Texas Press, 1996) | Met Heilbrunn Timeline, "The Origins of Writing" | yes |
| The first tablets at Uruk, about 3300 to 3100 BCE, recorded numbers of goods | Met Heilbrunn Timeline, "The Origins of Writing" | British Museum, "Writing in Mesopotamia" | yes |
| Signs came to be used for sounds, making names and sentences possible; cuneiform | British Museum, "Cuneiform" | Encyclopaedia Britannica, "Cuneiform" | yes |
| Scholars debate whether tokens led directly to writing | Encyclopaedia Britannica, "Writing: origins" | Met Heilbrunn Timeline, "The Origins of Writing" | yes, the debate is named in both |
| Egyptian writing began around the same time | Encyclopaedia Britannica, "Hieroglyph" | British Museum, "Egyptian hieroglyphs" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r11, 2026-11-09): the five steps sort by date (tokens before 3500 BCE, envelopes about 3500, tablets about 3300 to 3100, word signs, sound signs later); a sample 40-word trail card counts as 40; a 110-word label read at about 150 words a minute takes about 44 seconds; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 drawer, strip and case fit; at 680x425 the drawer is a sheet.
2. The step strip checks the order by date. (D4.2.6-8)
3. The label needs reason, sequence, example, detail and a "what we don't know" line. (D4.2.6-8)
4. Both sample labels are repaired with checked links. (D4.5.6-8)
5. Three versions are made and print; the trail card holds to 40 words. (D4.3.6-8)
6. Recording is optional, local only, and says so on screen.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
None.
