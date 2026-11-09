# Explainer Studio

## One idea
The student writes a one-page magazine explainer about two things readers mix up (weather and climate, or alligators and crocodiles), and the studio makes them develop each part with the right kind of content: a definition sharp enough to rule out look-alikes, a classification, a comparison chart checked against fact cards, and a quoted expert; then the page is previewed in print while a skimmer, who reads only headings, chart and captions, and a close reader, who flags any claim with no fact behind it, each test it, so they learn to develop a topic with facts and precise words, not just arrange it.

## Not like
- explainer-sections (6-8, spec): the order and job of sections, read and built. Here what goes inside each section.
- fact-fusion (5, spec): combining three sources into one table. Here writing an explainer from fact cards.
- pitch-deck-studio (8, concept): persuasive slides. Here informative writing.
- glossary-makers (3-5, spec): defining terms in a glossary. Here a definition inside an explainer, tested against look-alikes.
- linked-feature (spec): a linked web feature. Here a printed magazine page.

## Who and how
- Grade 7, ELA, module "Informative Writing" (Writing). Standard: W.7.2 (a, b, c, d, e, f). Section order and headings as structure belong to explainer-sections; this tool carries the development and content parts.
- Driver: one student; class mode makes an issue (tool.json `driver: "student"`). Every fact card is read on tap.
- Topics: "Weather or Climate?" and "Alligator or Crocodile?" tool.json `modes: ["Weather and climate", "Alligators and crocodiles", "Class issue"]`, `minutes: "30-40"`, `grades_label: "Grade 7"`.
- Nothing is saved; `Print` prints the magazine page.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.7.2a (introduce, preview) | Write a headline and a lede that names the two things and what the page will show | the headline and lede slots | 2 |
| W.7.2a (definition, classification, comparison) | Write a definition that passes the look-alike test; sort facts into a classification; fill the comparison chart | the definition box, the classification and the chart | 3 |
| W.7.2b (develop with facts, quotes, examples) | Fill each section with facts from cards and one quoted expert line | sections with fact tags | 4 |
| W.7.2c, W.7.2d (transitions, precise words) | Join sections with transitions; replace vague words ("stuff", "a lot") with domain words | the vague-word flags | 5 |
| W.7.2e (formal style) | Keep a formal style; casual phrases are flagged | the style flags | 5 |
| W.7.2f (conclusion) | Write a conclusion that says why the difference matters | the conclusion slot and the skimmer's summary | 6 |

## Screens and modes
Header (kit): title "Explainer Studio"; `Fact cards`, `Layout`, `Preview`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A bright magazine studio with a layout table, an empty page with slots (headline, lede, definition box, chart, two sections, pull quote, conclusion) and a shelf of fact cards. Editor Priya Raman stands at the table with a red pencil. First hint: "Tap a fact card to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Definition box.** The student writes a definition. The look-alike test reads it against keyed look-alikes: "Weather is what the sky is doing" also fits "a cloud"; "a crocodile is a reptile with big teeth" fits an alligator too. The box shows which look-alikes still fit until the definition rules them out (a time span for weather and climate; snout shape and where they live for the reptiles).

**Classification.** Fact cards drag into groups (for weather and climate: time span, what is measured, how it is predicted; for the reptiles: body, habitat, behavior). Wrong groups are allowed but the close reader asks about them later.

**Comparison chart.** Rows from the classification; the student fills each cell from a card. Cells are checked against the cards ("Climate: averages over 30 years or more" matches; "Climate: what you wear today" doesn't).

**Sections.** Two sections, each needing at least three facts tagged to cards and an example. One pull quote from an expert card (a NOAA or NPS page quoted with attribution).

**Transitions, words and style.** Transition chips (similarly, in contrast, for example, as a result); a vague-word list ("stuff", "things", "a lot", "really") and a casual list ("kinda", "super", "you guys") flag as the student writes.

**Preview.** The page renders as a printed magazine page. Two testers:
- The Skimmer reads only headline, headings, chart and captions and says in one sentence what they learned. The student compares it to what they meant to teach and edits until they match.
- The Close Reader flags any sentence with no fact tag ("Says who?").

**Class issue.** Pages from many students in one printable issue.

At 1366x768 the cards and page fit side by side; at 680x425 the cards are a drawer.

## Content
Written for Curio Class from the facts in Sources:
- Weather and climate: weather is the state of the air at a place and time (hours to days); climate is the average weather of a place over a long period, usually 30 years or more; examples: a rainy Tuesday versus a rainy season.
- Alligators and crocodiles: American alligators have a broad, U-shaped snout and mostly live in fresh water; American crocodiles have a narrower, V-shaped snout and can live in salt or brackish water; South Florida is one of the few places where both live; a crocodile's lower teeth show when its mouth is closed.
- Fact cards, keyed look-alikes for the definition test, and a key for the chart.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Every slot can be edited any time; the testers rerun on Preview.
- With Motion off the page appears without a print-roll effect.

## Look
- Accent `--brand` #8c2f6d magazine plum (header, slot frames, chart headers); gold #f4c542 (fact tags, the definition's passing mark); paper #fbf2f8; ink #2b0b20; muted #6a5063. Scene: a sunny magazine studio.
- Contrast (WCAG 2.1, computed): white on brand 7.66:1; brand on paper 6.99:1; ink on paper 16.35:1; muted on paper 6.52:1; ink on gold 11.02:1.
- Never color alone: flags have labels; slots say "empty" or "filled".
- Different from this batch (ember brown, leaf green, frost blue, newsprint slate).

## Art
- People art goes to Gemini: Editor Priya Raman (an Indian American woman in her thirties with a red pencil behind her ear), 3 poses; the Skimmer (a teen boy flipping pages fast) and the Close Reader (an older man with a magnifier), 2 poses each; "illustrated <description> <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): magazine studio (1); storm clouds over a town (1); a long-term weather station in a field (1); an alligator in a freshwater swamp (1); a crocodile on a mangrove shore (1).
About 12 images. Drawn in code: page layout, chart, flags.

## Voice
Bank voice `bright-teacher` as Editor Raman (unique in this batch); the Skimmer is `playful-friend` and the Close Reader is `clear-teacher` (each unique in this batch). `Curio.voice` with `scope: () => state.topic + ':' + state.view + ':' + state.slot`, `welcomeAfter: true`.
- how `welcome`: "Readers mix these two up. Your page will fix that. Start with a definition only one of them fits."
- event, whole, `card`: the tapped fact card.
- event `lookalike`: "That also fits {a cloud}. Sharpen it."
- event `vague`: "{Stuff} is vague. What exactly?"
- event `skim`: the Skimmer's one-sentence summary.
- event `saysWho`: "Says who?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: look-alike definition test, classification groups, chart key, fact tags, word and style lists, the two testers.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Definition | Copy a fact card | The look-alike test still runs; a copied card that doesn't rule out the look-alikes stays open. |
| Chart | Fill cells with anything | Cells are checked against cards. |
| Sections | Write without facts | The Close Reader flags each untagged sentence. |
| Skimmer | Ignore it | The page isn't marked done until the student confirms the Skimmer's summary matches their goal or edits headings. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a card: `card`, `welcome` (queued, first time).
2. Definition: `lookalike` as it fires.
3. Writing: `vague` as it fires.
4. Preview: `skim` (waits), then `saysWho` per flagged sentence.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.7.2 (a to f) wording | thecorestandards.org, Writing Grade 7 | CCSS ELA 2010 PDF | yes |
| Weather is short-term conditions; climate is the average over a long period, usually 30 years | NOAA National Ocean Service, weather and climate | NASA, "What's the difference between weather and climate?" | yes |
| Alligators have a broad U-shaped snout, crocodiles a narrower V-shaped one; crocodiles tolerate salt water; South Florida has both | National Park Service, Everglades, alligators and crocodiles | Florida Fish and Wildlife Conservation Commission, American crocodile | yes |
| A crocodile's lower teeth show when its mouth is closed; an alligator's mostly don't | National Park Service, Everglades | Smithsonian's National Zoo, crocodilian facts | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b21, 2026-11-09): a sample vague definition still matches at least one keyed look-alike and a sharpened one matches none; every chart cell in the key has a fact card; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 cards and page fit; at 680x425 the cards are a drawer.
2. Headline and lede slots work. (W.7.2a)
3. The definition passes only when no look-alike fits; classification and chart are checked. (W.7.2a)
4. Sections need three tagged facts and an example; one expert quote with attribution. (W.7.2b)
5. Vague and casual words flag; transition chips work. (W.7.2c, d, e)
6. The conclusion slot and the Skimmer's summary work. (W.7.2f)
7. The Close Reader flags untagged sentences.
8. Class issue and Print work.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: no print-roll effect; no network requests.

## Open questions
- None for Cory.
