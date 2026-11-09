# Theme Tracker

## One idea
The student reads "The Ugly Duckling" in five short parts with three candidate themes burning as lamps on a shelf, and every detail they highlight and drag to a lamp, with a few words on why, feeds that lamp's oil, so some lamps grow bright and some fade as the story goes on; a lamp built on one flashy line goes dark when the ending contradicts it, and the brightest theme must survive a short summary built only from the student's highlights, so they learn that a theme is what the details add up to, not what one line says.

## Not like
- theme-evidence-ladder (6-8, concept): ranking quotes against rival themes. Here a grade 4 story read part by part.
- theme-ledger (9-12, spec): two themes over a whole novel with the evidence engine. Here one tale and lamps.
- moral-of-the-story (2, concept): fable morals. Here a theme the student has to build.
- main-idea-pinboard (3-5, spec): main ideas in nonfiction and fables. Here theme in a longer literary tale.
- show-don-t-tell (4, spec): feelings from details. Here themes from details.

## Who and how
- Grade 4, ELA, module "Theme and Summary" (Reading Literature). Standards: RL.4.2, RL.4.1.
- Driver: one student (tool.json `driver: "student"`). Every sentence is read on tap.
- The story: Hans Christian Andersen, "The Ugly Duckling" (1843), retold for grade 4 from H. P. Paull's 1872 English translation (public domain), about 1,400 words in five parts. tool.json `modes: ["Solo", "Class lamps"]`, `minutes: "30-40"`, `grades_label: "Grade 4"`.
- Nothing is saved; `Print` prints the lamps, the highlights and the summary.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.4.1 | Highlight a detail and label it "says it" (stated in the text) or "shows it" (inferred), with a few words on why | the highlight with a tag and a note | 2 |
| RL.4.2 (theme) | Drag each highlight to the lamp it supports; lamps brighten or fade as the parts go on | three lamps with oil levels | 3, 4 |
| RL.4.2 (own theme) | After part 3, write a fourth theme on the empty lamp | the student's own lamp | 5 |
| RL.4.2 (summary) | Write a short summary using only highlighted details; it must hold up the brightest theme | the summary card beside the lamp | 6 |

## Screens and modes
Header (kit): title "Theme Tracker"; `Story`, `Lamps`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A lighthouse keeper's study at dusk: a shelf with three oil lamps and one empty lamp, an open storybook, and Keeper Ione, a heron in a knit sweater. First hint: "Tap the storybook to start part one." The first tap reads the title and the first sentence; the welcome is queued after it (`welcomeAfter: true`).

**Story.** One part at a time, sentences numbered, tap to hear. Three lamps on the shelf, each labeled: "Being different is not being worse", "Be kind to others", "Hard times can make you stronger". (A fourth, empty lamp waits.)

**Highlight.** Long-press or `Highlight` a sentence (or a run of up to three). A small card asks: "Says it or shows it?" and "Why? (a few words)". Then drag the card to a lamp (or two lamps; a detail can feed two). The lamp's oil rises by the detail's weight for that lamp from the data key (0 to 3); a 0 adds nothing and Keeper Ione asks "How does this one feed that lamp?" (the student may keep it).

**Fading.** At the end of each part, each lamp's flame shows the oil from all highlights so far. Some key lines count against a lamp: the ending lowers any lamp the ending contradicts. "Hard times can make you stronger" can stay lit, but a lamp the student writes as "If you are different, run away" goes dark at part 5, when the swans welcome him and he stays.

**Own lamp.** After part 3, the empty lamp unlocks; the student writes a theme in a sentence (the claim check asks for a whole idea, not a topic: "Kindness" gets "That's a topic. What does the story say about kindness?").

**Summary test.** After part 5, the brightest lamp is chosen. The student builds a summary of 4 to 6 sentences: highlighted details appear as chips; the student writes in their own words around them. The summary must mention the beginning, middle and end parts (it uses at least one highlight from parts 1, 3 and 5) and at least 3 highlights that feed the chosen lamp. Keeper Ione reads it and says whether the lamp stays lit.

**Class lamps.** The class's brightest lamps are tallied on the board (anonymous counts only).

At 1366x768 the story and shelf fit side by side; at 680x425 the shelf is a strip above the story.

## Content
- The retelling: part 1 the duck's nest and the big gray egg; part 2 the farmyard teases and pecks him; part 3 he runs away, the wild ducks and the geese, the hunters (told gently: guns boom and the geese fly away), the old woman's cottage with the hen and the cat; part 4 the hard winter, the ice, the farmer who carries him home; part 5 spring, the swans, his reflection, the children who call him the most beautiful, and that he is not proud, because a good heart is never proud.
- The key: every sentence rated 0 to 3 for each of the three lamps, plus "says it" or "shows it" answer per key sentence (the tool accepts either where the key says both).
- Changes from the 1872 translation are listed in the data file (shortened; the hunting scene softened; old words updated).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Highlights can be moved between lamps or removed; oil updates.
- Nothing is refused; the oil level and Keeper Ione's questions are the feedback.

## Look
- Accent `--brand` #6b5200 lamp amber (header, lamp brass, part tabs); gold #f4c542 (flames, highlights); paper #fbf8ee; ink #241b00; muted #5f5844. Scene: a lighthouse study at dusk, warm light.
- Contrast (WCAG 2.1, computed): white on brand 7.42:1; brand on paper 6.98:1; ink on paper 16.04:1; muted on paper 6.66:1; ink on gold 10.48:1.
- Never color alone: oil levels have numbers on hover and focus (out of 10); tags carry words.
- Different from this batch (garage blue, card crimson, editor green, vase terracotta).

## Art
Public-domain illustrations: none suitable were found in Met or Art Institute of Chicago open access for this tale (searched 2026-11-09), so scenes are generated.
Local FLUX (`scripts/localart.py`), animals only.
- study (1); Keeper Ione (4 poses: read, point, think, smile), "A friendly gray heron in a knit sweater holding a lantern <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- story scenes (10, two per part): "<a duck on a nest with one big gray egg / a gray duckling alone on a frozen pond / swans on a spring lake>, 19th-century storybook watercolor style, no text"; 4:3.
About 15 images. Drawn in code: lamps, flames, oil, cards.

## Voice
Bank voice `wise-mentor` as Keeper Ione and the story reader (unique in this batch). `Curio.voice` with `scope: () => state.part + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "A theme is what a story adds up to. As you read, highlight details and feed them to the lamp they fit. Watch which lamp burns brightest."
- event, whole, `sentence`: the tapped sentence.
- how `tagHow`: "Does the story say it right out, or show it so you figure it out?"
- event `noOil`: "How does this one feed that lamp?"
- event `partEnd`: "End of part {3}. {Two} lamps are burning bright."
- event `topic`: "That's a topic. What does the story say about {kindness}?"
- event `dark`: "This lamp went dark. The ending doesn't hold it up."
- event `stays`: "Your summary holds it up. The lamp stays lit."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: lamps and oil, highlight cards, own-theme claim check, summary test. (The evidence engine is not used; the lamp key is simpler than its source pack.)

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Oil | Feed every highlight to every lamp | A 0 adds nothing; feeding all lamps equally leaves no brightest lamp, and Keeper Ione asks which one the details really hold up. |
| Summary | Use highlights from one part | It needs highlights from parts 1, 3 and 5 and 3 that feed the chosen lamp. |
| Own lamp | Type a topic word | The claim check asks for a whole idea. |
| Says or shows | Tag all "says it" | Wrong tags get "Does it say that in words? Look again." The key has at least 6 "shows it" lines (checked). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the storybook: title, first sentence, `welcome` (queued, first time).
2. Sentences: `sentence` (whole); first highlight: `tagHow`; zero oil: `noOil`.
3. End of each part: `partEnd`; own lamp: `topic` if needed; part 5: `dark` where a lamp fails.
4. Summary: `stays` or the reason it doesn't.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.4.2 and RL.4.1 wording | thecorestandards.org, Reading Literature Grade 4 | CCSS ELA 2010 PDF | yes |
| "The Ugly Duckling" by Hans Christian Andersen, 1843; H. P. Paull's 1872 translation is public domain | Project Gutenberg, Andersen's Fairy Tales (Paull translation) | The Hans Christian Andersen Centre, University of Southern Denmark, tale list and dates | yes |
| Theme is a central message a reader builds from details across the text, not a single line | ReadWriteThink, theme lessons | Reading Rockets, teaching theme | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b13, 2026-11-09): a sample key gives at least 6 "shows it" lines and each lamp at least 3 rated details across parts 1, 3 and 5; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the story and shelf fit; at 680x425 the shelf is a strip.
2. Highlights take a says-it or shows-it tag and a note. (RL.4.1)
3. Highlights feed lamps by the key's weights. (RL.4.2)
4. Lamps update per part and a contradicted lamp goes dark. (RL.4.2)
5. The own lamp unlocks after part 3 with the claim check. (RL.4.2)
6. The summary test needs parts 1, 3 and 5 and 3 matching highlights. (RL.4.2)
7. Class lamps tally anonymously.
8. Print shows lamps, highlights and summary.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: flames are still; no network requests.

## Open questions
- None for Cory.
