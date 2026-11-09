# Quote Picker

## One idea
The student writes two short pieces from the same article, an opinion paragraph and an explainer, and for each point picks the quote or fact that backs it from three choices (one strong, one that only repeats the point, one off topic) and writes the sentence that introduces it, and when an editor reads the paragraph aloud a repeat quote fades with "You already said that" and an unintroduced quote lands with a thud, so they learn that evidence has to add something and that opinion and explaining use it differently.

## Not like
- main-idea-pinboard (3-5, spec): pinning proof for an author's main idea. Here the student's own writing.
- claim-court (5, concept): judging an author's evidence. Here choosing and introducing evidence.
- persuasion-poster (3, concept): a poster. Here a paragraph and an explainer.
- note-card-shuffle (3, spec): notes in own words. Here exact quotes with introductions.
- because-bridge (K-2, spec): reasons on a bridge. Same evidence engine, older writers.

## Who and how
- Grade 4, ELA, module "Writing with Evidence" (Writing). Standards: W.4.1, W.4.2, W.4.9, RI.4.1.
- Driver: one student (tool.json `driver: "student"`). The article is read on tap; drafts are read back by the editor.
- Two articles: "Should Maple Street Build a Skate Park?" (opinion) and "How Do Sea Otters Keep Warm?" (explain); each article is used for both pieces. tool.json `modes: []`, `minutes: "25-40"`, `grades_label: "Grade 4"`.
- Saving: drafts are kept in this browser; footer: "Your drafts stay on this device." `Clear my drafts` removes them.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.4.1 | Opinion draft: state an opinion, order two or three reasons, back each with a chosen quote or fact, link with words like for instance and in addition, and end with a conclusion | the opinion draft with reason slots | 2, 3 |
| W.4.2 | Explain draft: group facts under two headings, add a definition and a quote to each group, link with another, for example, also, because, and conclude | the explain draft with headings | 4 |
| W.4.9 | Every point comes from the article; quotes and facts are dragged from it | article lines with link lines to the draft | 2, 4 |
| RI.4.1 | Each quote is checked against the article's exact words; the intro says what the text says | the exact-words check | 5 |
| W.4.1, W.4.2 | The editor reads each draft; repeat quotes fade, unintroduced quotes thud | the read-back with marks | 6 |

## Screens and modes
Header (kit): title "Quote Picker"; `Articles`, `My drafts`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A newspaper office desk with an article clipped to a board, two blank drafts labeled Opinion and Explain, and Editor Finch, a finch in a green eyeshade with a blue pencil. First hint: "Tap an article to read it." The first tap reads the headline; the welcome is queued after it (`welcomeAfter: true`).

**Opinion draft.** The student picks or types an opinion. Three reason slots; for each reason, the quote tray offers three article lines (data: strong, repeat, off topic). The student picks one and types an introducing phrase (or picks a starter: "According to the article,", "The park manager said,", "One fact is that"). Linking chips go between reasons. A conclusion box ends it.

**Explain draft.** Two heading slots (the student picks from four headings; two fit). Under each, drag two facts, a definition (from a glossary line in the article) and one quote. Link chips: another, for example, also, because. A conclusion box.

**Editor read.** `Hand it in` reads the draft aloud. The evidence engine checks each quote: a quote that `repeats` the reason (word overlap above the engine's threshold) fades with "You already said that. What does this quote add?"; a quote with no introducing phrase thuds and gets "Who said this? Introduce it."; an `offKey` quote (key rating 0 for the reason) gets "Does this back that reason?" Each note points to the draft line.

**Exact words.** `Check quotes` compares each quote in quotation marks to the article; any changed word lights with the article's version beside it.

At 1366x768 the article and draft fit side by side; at 680x425 the article is a drawer.

## Content
Articles written for Curio Class:
- "Should Maple Street Build a Skate Park?" (about 350 words, a made-up town): what neighbors and the park manager said; costs and maintenance in plain words; facts about physical activity and youth programs sourced; both sides given. Opinion pieces may take either side; each side has strong quotes.
- "How Do Sea Otters Keep Warm?" (about 300 words): sea otters have the densest fur of any animal, up to about a million hairs per square inch; they have no blubber; air trapped in the fur keeps their skin dry; they groom for hours a day; they eat about a quarter of their body weight each day to make enough body heat. Glossary lines: insulate, groom, blubber.
- Each article has a key (evidence engine Source pack) rating lines 0 to 3 for each reason and heading, and the three-choice trays.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Drafts are free text with chips; nothing is refused.
- Editor marks are advice; the student may revise and hand in again.

## Look
- Accent `--brand` #2e6b30 editor green (header, eyeshade, slots); gold #f4c542 (chosen quotes, the desk lamp); paper #f3f9f3; ink #0e220f; muted #4c5d4d. Scene: a cozy newspaper office.
- Contrast (WCAG 2.1, computed): white on brand 6.44:1; brand on paper 6.03:1; ink on paper 15.67:1; muted on paper 6.60:1; ink on gold 10.29:1.
- Never color alone: faded quotes also get a dashed outline and a note; thuds show a mark and words.
- Different from this batch (garage blue, card crimson, lamp amber, vase terracotta).

## Art
Local FLUX (`scripts/localart.py`), no people.
- office (1); Editor Finch (4 poses: read, mark, think, nod), "A friendly finch newspaper editor in a green eyeshade holding a blue pencil <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- article pictures (4): "<an empty lot on a small-town street / a skate park ramp / a sea otter floating and grooming / a sea otter wrapped in kelp>, realistic illustration, no text"; 4:3.
About 9 images. Drawn in code: drafts, trays, chips, marks.

## Voice
Bank voice `clear-teacher` as Editor Finch and the article reader (unique in this batch). `Curio.voice` with `scope: () => state.article + ':' + state.draft + ':' + state.step`, `welcomeAfter: true`.
- event `headline`: "{How Do Sea Otters Keep Warm?}"
- how `welcome`: "Two drafts, one article. For each point, pick the quote that backs it, and tell the reader who said it."
- event, whole, `line`: the tapped article line.
- how `pickHow`: "Pick the quote that adds something to your reason."
- event `repeats`: "You already said that. What does this quote add?"
- event `thud`: "Who said this? Introduce it."
- event `offKey`: "Does this back that reason?"
- event `clean`: "Every quote pulls its weight. Nice work."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
evidence (`kit/evidence.js`), described in full in tools/theme-ledger/spec.md, exposed as `__tool.ev`. This tool uses: Source pack (each article with a key rating lines per reason or heading), Spans (whole sentences, or word ranges for quotes), Claims (reasons and headings), Evidence links (quote to reason), checks (`repeats`, `offKey`, and `unexplained` for a quote with no introducing phrase), Draft (the two drafts with read-back marks). Not Ledger, Series, Board view or Sides.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Quote pick | Try each choice | Each try is read back with its mark, which is the lesson; three choices per slot. |
| Repeats | Pick the line that sounds most like the reason | That is the repeat choice by design; it fades. |
| Introductions | Type "Quote:" before every quote | Accepted as an introduction only if it names a source or uses a starter frame (data). |
| Exact words | Edit the quote to fit | The check lights every changed word. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap an article: `headline`, `welcome` (queued, first time).
2. Article: `line` (whole). First tray: `pickHow`.
3. Hand it in: the draft, then `repeats`, `thud`, `offKey` as they fire, or `clean`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.4.1, W.4.2, W.4.9, RI.4.1 wording | thecorestandards.org, Writing and Reading Informational Grade 4 | CCSS ELA 2010 PDF | yes |
| Sea otters have the densest fur of any animal, up to about a million hairs per square inch, and no blubber; air trapped in the fur insulates them; they groom often | Monterey Bay Aquarium, sea otter | NOAA Fisheries, southern sea otter | yes |
| Sea otters eat about 20 to 25 percent of their body weight a day | Monterey Bay Aquarium, sea otter | US Fish and Wildlife Service, southern sea otter | yes |
| Children and teens should get 60 minutes of physical activity a day | CDC, physical activity for children | US Department of Health and Human Services, Physical Activity Guidelines for Americans | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b13, 2026-11-09): each three-choice tray in the sample has one repeat line whose word overlap with its reason is highest; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the article and draft fit; at 680x425 the article is a drawer.
2. The opinion draft takes an opinion, reasons, quotes, intros, links and a conclusion. (W.4.1, W.4.9)
3. Linking chips and the conclusion box are prompted. (W.4.1)
4. The explain draft takes headings, facts, a definition, a quote, links and a conclusion. (W.4.2)
5. Check quotes lights changed words. (RI.4.1)
6. The editor read marks repeats, missing intros and off-key quotes.
7. Drafts survive a reload where storage works and print.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: faded quotes don't animate; no network requests.

## Open questions
- None for Cory.
