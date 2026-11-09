# Tough Text Club

## One idea
The student climbs a ladder of four hard public-domain texts (a chapter of Frankenstein, Emily Dickinson's "Because I could not stop for Death", the Declaration of Independence and Edwin Hubble's 1929 paper on the speed of distant galaxies), plans how to read each one, then takes the supports away one at a time (read-aloud, word help, chunk summaries, guiding questions) until they read and answer on their own, while a range map records what kinds of texts they have read, so they learn to read complex literature and nonfiction independently and to choose a plan that fits the text.

## Not like
- climbing-reads (6-8, spec): graded reading with supports for middle school. Here grade 9 to 12 texts and a plan per text.
- living-explainer (9-12, spec, this batch): writing and updating. Here reading.
- old-patterns-new-stories (8, spec): reading modern stories against old ones. Here the old texts themselves, read whole.
- poetry-soundboard (7, spec): what sound does in a poem. Here reading a poem with a plan and without help.
- research-notebook (spec): gathering sources. Here reading one source deeply.

## Who and how
- Grades 9 to 12, ELA, module "Reading Range and Text Complexity" (Reading Literature, Reading Informational Text). Standards: RL.9-10.10, RL.11-12.10, RI.9-10.10, RI.11-12.10.
- Driver: one student; there is no class mode. Every passage, word card and question is read on tap while that support is on.
- Four rungs, each with a 9-10 path and an 11-12 path (the 11-12 path is longer and starts with fewer supports), and a stretch text per rung. tool.json `modes: ["Ladder", "Range map"]`, `minutes: "30-45 per rung"`, `grades_label: "Grades 9-12"`.
- The range map and plans are saved on this device only (localStorage), and the screen says so: "Your reading record stays on this device. Nothing is uploaded." `Clear my record` erases it. `Print` prints the range map and plans.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.9-10.10, RL.11-12.10 (literature: novel chapter, poem) | Read the Frankenstein chapter and the Dickinson poem, with supports dropped one at a time, and answer keyed questions | the supports panel and the question cards | 3 |
| RI.9-10.10, RI.11-12.10 (literary nonfiction: founding document, science) | Read the Declaration and Hubble's paper the same way | the supports panel and the question cards | 3 |
| all four (independently and proficiently) | Answer the final questions on each rung with every support off | the "on my own" badge per rung | 4 |
| all four (range) | Track the range read: kinds, centuries, length | the range map | 5 |
| all four (plan) | Make a reading plan before each text and check it afterward | the plan card and its after-note | 2 |

## Screens and modes
Header (kit): title "Tough Text Club"; `Ladder`, `Range map`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A quiet reading room in an old library with a tall rolling ladder against four shelves, each holding one text; the club's host, Professor Elena Marsh, sits by a lamp. First hint: "Tap the first shelf to hear what's on it." The first tap reads the shelf card; the welcome is queued after it (`welcomeAfter: true`).

**The rungs.**
1. Frankenstein, chapter 5 (Mary Shelley, 1818 text as on Project Gutenberg): "It was on a dreary night of November..." The creature wakes.
2. "Because I could not stop for Death" (Emily Dickinson, published 1890 as "The Chariot").
3. The Declaration of Independence (1776): the preamble and the first grievances for 9-10; the whole text for 11-12.
4. "A relation between distance and radial velocity among extra-galactic nebulae" (Edwin Hubble, Proceedings of the National Academy of Sciences, 1929): the introduction, the data table described in words, and the conclusion.
Stretch texts (optional, one per rung): Frankenstein chapter 10; Dickinson's "I heard a Fly buzz"; Lincoln's Second Inaugural Address; Michael Faraday's "The Chemical History of a Candle", lecture 1.

**Plan.** Before each text the student fills a plan card: what kind of text it is, what makes it hard (old words, long sentences, compressed lines, technical terms), and two moves from a list (read twice, read aloud, chunk and summarize, mark claims, list the people, look up only words that block meaning) or their own. After the text they mark which moves helped.

**Read with supports.** Four supports start on: Read-aloud (tap a sentence to hear it), Word help (tap a marked word for a plain meaning in context), Chunk summaries (a one-line summary after each chunk), Guiding questions (one per chunk). After each chunk's questions are answered, `Drop a support` turns one off, and the student picks which. Each chunk has two keyed questions (one about what the text says, one about how or why) with four choices and a "show me where" step: the student taps the sentence that proves it.

**On my own.** The last chunk of every rung runs with all supports off. A rung earns "on my own" when its last-chunk questions are right and each proof sentence is in the keyed span. A miss offers one support back and a second try.

**Range map.** A grid of kinds (novel, poem, founding document, scientific paper, speech, lecture) against centuries (18th, 19th, 20th), filled as texts are finished, with time spent and supports used shown as a small strip per text.

At 1366x768 text and supports fit side by side; at 680x425 supports are a drawer.

## Content
- Texts from the Sources table. Word help, chunk summaries, guiding questions and keyed questions written for Curio Class.
- The Declaration's words about "merciless Indian Savages" in the grievances are kept as written in the 11-12 path, with a short note before that chunk: the phrase is a slur the authors used, and it shows how the founders wrote about Native nations. The 9-10 path stops before that grievance.
- Frankenstein chapter 5 has no graphic content beyond the creature's description.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A dropped support stays off for that text unless the student takes it back after a miss.
- With Motion off the ladder doesn't roll; the rung highlights.

## Look
- Accent `--brand` #5a2a6e club purple (header, shelf labels, badges); gold #f4c542 (the current sentence, earned badges); paper #f8f3fa; ink #1e0c26; muted #5f5266. Scene: an old library reading room by lamplight.
- Contrast (WCAG 2.1, computed): white on brand 10.55:1; brand on paper 9.64:1; ink on paper 16.90:1; muted on paper 6.65:1; ink on gold 11.37:1.
- Never color alone: supports show On or Off in words; badges are labeled.
- Different from this batch (newsroom navy, lane green, rust, calendar teal).

## Art
- People art goes to Gemini: Professor Elena Marsh (a Puerto Rican woman in her sixties with silver hair and a cardigan), 3 poses; "illustrated friendly literature professor <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): library reading room with a rolling ladder (1); a candle in a dark room (1); a horse-drawn carriage on a country road at dusk (1); an observatory dome under stars (1).
About 7 images. Drawn in code: shelves, supports panel, range map.

## Voice
Bank voice `calm-professor` as Professor Marsh and the hint voice (unique in this batch); the texts are read by `smooth-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.rung + ':' + state.chunk`, `welcomeAfter: true`.
- how `welcome`: "Four hard texts. Plan how you'll read each one, then take the help away one piece at a time, until you're reading on your own."
- event `shelf`: the shelf card.
- event, whole, `sentence`: the tapped sentence (Read-aloud on only).
- event `word`: the word help card.
- event `drop`: "Which support will you drop next?"
- event `proof`: "Show me where it says that."
- event `own`: "On your own. Nice reading."
- event `privacy`: "Your reading record stays on this device. Nothing is uploaded."
Read speaks the hint, which names the next action and control and never a disabled one. With Read-aloud dropped, Read still speaks hints but never the text.

## Family engine
None. Tool-only code: chunked texts with supports, keyed questions with proof spans, the plan card, the range map, localStorage save wrapped in try and catch.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Questions | Guess choices | Each answer needs a proof sentence inside the keyed span. |
| Drop supports | Never drop any | "On my own" needs the last chunk with every support off. |
| Plan | Pick the same moves every time | The after-note asks which moves helped; the print shows plans side by side. |
| Read-aloud | Use it on the last chunk | Read-aloud is off on the last chunk; Read speaks only hints there. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the first shelf: `shelf`, `welcome` (queued, first time).
2. First save: `privacy`.
3. Reading: `sentence` and `word` on tap while on; `proof` after a choice; `drop` after each chunk.
4. Last chunk: `own` on a pass.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.9-10.10, RL.11-12.10, RI.9-10.10 and RI.11-12.10 wording | thecorestandards.org, Reading 9-10 and 11-12 | CCSS ELA 2010 PDF | yes |
| Frankenstein (1818) chapter 5 text, public domain | Project Gutenberg eBook #84 (checked 2026-11-09) | Britannica, Frankenstein | yes |
| "Because I could not stop for Death" text, public domain, first published 1890 | Project Gutenberg eBook #12242 (checked 2026-11-09) | Poetry Foundation, the poem's page | yes |
| Declaration of Independence text, including the grievance naming "merciless Indian Savages" | Project Gutenberg eBook #1 (checked 2026-11-09) | National Archives, Declaration transcription | yes |
| Hubble's 1929 PNAS paper, published in 1929 and in the U.S. public domain since 2025 | Proceedings of the National Academy of Sciences, 15(3), 1929 | Cornell University Library, copyright term chart (works published 1929 entered the public domain in 2025) | yes |
Backed twice: 5. Cut: 0.

Sensitivity note: the Declaration's slur against Native nations is kept in the 11-12 path with a note, and the 9-10 path stops before it; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b24, 2026-11-09): the Gutenberg files contain "dreary night of November", "could not stop for Death", "When in the Course of human events" and "merciless Indian Savages"; every chunk has two keyed questions with a proof span; 1929 plus 95 years is 2024, so the paper entered the public domain on January 1, 2025; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 text and supports fit; at 680x425 supports are a drawer.
2. Plan cards come before each text and take an after-note.
3. Supports drop one at a time; questions need proof sentences. (RL.9-10.10, RL.11-12.10, RI.9-10.10, RI.11-12.10)
4. The last chunk runs with every support off and earns "on my own". (all four)
5. The range map fills and persists on this device; the privacy line shows; Clear my record erases. (all four)
6. The 9-10 and 11-12 paths differ as in Content.
7. Print shows the range map and plans.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the ladder is still; no network requests.
10. Storage blocked: the tool still works and says the record won't be kept.

## Open questions
- None for Cory.
