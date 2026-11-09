# Allusion Hunter

## One idea
The student hunts through a page of everyday texts written for Curio Class (a sports headline, a phone ad, a song verse, a text message, a short story) for allusions, a "Trojan horse" app update, a "David and Goliath" match, a "Romeo" at the bus stop, taps each to open the story it comes from, and writes what the allusion borrows from that story here, so they learn that an allusion packs a whole story into a few words and that its meaning depends on where it is used.

## Not like
- myth-museum (4, spec): Greek myths behind everyday words, grade 4. Here allusions from many sources found in context, grade 7.
- double-meanings (8, spec, this batch): sorting puns, irony, analogy and allusion. Here hunting and explaining allusions, plus analogies and connotation built from them.
- word-thermometer (6, spec): connotation of near-synonyms on a scale. Here connotation among words born from stories (Herculean, huge).
- simile-slam (5, spec): similes. Here allusions.
- root-detective-cards (4, spec): word parts. Here story sources.

## Who and how
- Grade 7, ELA, module "Figurative Language and Allusions" (Language). Standard: L.7.5 (a, b, c).
- Driver: one student; class mode is an allusion-of-the-week wall that lasts while the page is open (tool.json `driver: "student"`). Every text and source story is read on tap.
- Three field pages (Sports and School, Ads and Apps, Songs and Stories), the journal stage, and the student's own headline. tool.json `modes: ["Field pages", "Journal", "My headline", "Class wall"]`, `minutes: "20-30"`, `grades_label: "Grade 7"`.
- Nothing is saved; `Print` prints the journal.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.7.5a | Tap a phrase that alludes to a story; open the source card; write what it means here | the find, the source card and the student's line | 2 |
| L.7.5a | Decoy phrases that sound special but aren't allusions are caught | the decoy card | 3 |
| L.7.5b | Complete analogies built from allusions (Achilles' heel is to weakness as Pandora's box is to...) | the analogy row | 4 |
| L.7.5c | Sort near-synonyms by connotation (Herculean, huge, tremendous, overwhelming) | the sorted row with a reason | 4 |
| L.7.5a | Write a headline with an allusion on purpose; a reader card says what someone who doesn't know the source would miss | the headline and reader card | 5 |

## Screens and modes
Header (kit): title "Allusion Hunter"; `Field pages`, `Journal`, `My headline`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A naturalist's field journal open on a mossy log, a magnifying glass and a page of mixed texts pinned like specimens; Professor Iris Wentworth, a field guide in a canvas hat. First hint: "Tap a text to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Field pages.** Each page has about eight short texts with 12 keyed allusions and 4 decoys. Examples: "Tiny Eastside upsets the champs in a David and Goliath final" (Bible story as literature), "This 'free' app update is a Trojan horse" (Greek myth, Homer and Virgil), "He's no Romeo, but he did hold the door" (Shakespeare), "The new rule opened a Pandora's box" (Greek myth), "Their goalie's one weakness is his Achilles' heel" (Greek myth), "Everything she touches turns to gold, a real Midas touch" (myth), "Sour grapes, they said, after losing" (Aesop), "We crossed the Rubicon when we bought the tickets" (history, Julius Caesar), "a Herculean cleanup" (myth). Decoys: "a golden opportunity", "as cool as a cucumber", "a whale of a time", "rock-solid". The student taps a phrase; a find opens the source card (a short retelling and its source); a decoy says "That's an everyday phrase, not a story." Then the student writes what the allusion borrows here ("The update looks like a gift but hides something harmful") and the tool checks for a keyed idea word (gift, hidden, trick).

**Journal.** Analogies: rows like "Achilles' heel : weakness :: Pandora's box : ___" with four choices, and two the student completes from scratch. Connotation: four words in a row to order from mildest to strongest or most admiring to least, with a reason card for the top word ("Herculean names a hero, so it sounds admiring").

**My headline.** The student writes a headline for a school event using one allusion on purpose. Reader cards then speak: a reader who knows the source ("I get it: the small team beat the giant") and a reader who doesn't ("Who's Goliath?"). The student adds a few words so both readers get it, or keeps it and says why.

**Class wall.** One allusion a week, with the class's lines about what it means.

At 1366x768 the field page and journal fit side by side; at 680x425 the journal is a tab.

## Content
- Field pages and decoys written for Curio Class.
- Source cards: short retellings written for Curio Class from the sources in the Sources table. Bible stories are told as literary sources beside myths, Shakespeare, Aesop and history, credited as "a story from the Hebrew Bible" with no religious claim.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Found allusions stay marked on the page.
- With Motion off the magnifying glass doesn't move.

## Look
- Accent `--brand` #4a5d23 field olive (header, journal cover, finds); gold #f4c542 (found allusions, the magnifier rim); paper #f5f7ef; ink #171d0a; muted #565c4a. Scene: a mossy log in a sunny wood.
- Contrast (WCAG 2.1, computed): white on brand 7.29:1; brand on paper 6.74:1; ink on paper 15.97:1; muted on paper 6.42:1; ink on gold 10.61:1.
- Never color alone: finds carry a "found" label; decoys a "decoy" label.
- Different from this batch (gym brick red, studio violet, chat teal, plum).

## Art
- Public domain (Art Institute of Chicago): 142544 "The Trojan Horse Being Dragged into the City of Troy", Giulio Bonasone, 1545; 48948 "David and Goliath", Rembrandt van Rijn, 1655. Each image is viewed before use.
- People art goes to Gemini: Professor Iris Wentworth (a Black British woman in her sixties in a canvas field hat), 3 poses; "illustrated friendly field naturalist <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): field journal on a mossy log (1); source scenes with no faces close up (5: a jar with mist escaping, a golden apple tree for Midas, a fox under grapes, a river crossing at dawn, a heel and an arrow in a classical painting style).
About 10 images. Drawn in code: field pages, journal rows, reader cards.

## Voice
Bank voice `knowing-guide` as Professor Wentworth (unique in this batch); source cards are read by `gentle-storyteller` (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.page + ':' + state.find`, `welcomeAfter: true`.
- how `welcome`: "Some phrases carry a whole story inside them. Find them, open the story, and say what it means here."
- event, whole, `text`: the tapped text.
- event `found`: "Found one. It comes from {the Trojan War}."
- event, whole, `source`: the source card.
- event `decoy`: "That's an everyday phrase, not a story."
- event `reader`: the reader card's line.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
myths (`kit/myths.js`, `__tool.my`), described in full in tools/myth-museum/spec.md. This tool uses: Myth records (the source cards; `culture` holds the source kind, such as Greek myth, Shakespeare or Hebrew Bible story) and Allusion records with `my.find` (listed word forms only, never guessed). Not the museum rooms or exhibit walk. The field pages, decoys, journal and reader cards are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Finds | Tap every phrase | Decoys are marked and counted in the print. |
| Meaning lines | Copy the source card | The line must name something in the field text (the app, the team) as well as an idea word. |
| Analogies | Pick at random | Two rows must be written from scratch. |
| Headline | Write without an allusion | The headline must contain a phrase from the source map or one the student links to a source card. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a text: `text`, `welcome` (queued, first time).
2. Finds: `found` (waits), then `source` (whole) if opened; `decoy` as it fires.
3. My headline: `reader` per card.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.7.5 (a, b, c) wording | thecorestandards.org, Language Grade 7 | CCSS ELA 2010 PDF | yes |
| Meanings and origins of Trojan horse, Achilles' heel, Pandora's box, Midas touch, Herculean, David and Goliath, sour grapes, crossing the Rubicon, Romeo | Merriam-Webster, each entry | Britannica, each source story | yes |
| An allusion is a brief reference to a well-known person, place, event or work | Merriam-Webster, allusion | Purdue OWL, literary terms | yes |
| AIC 142544 (Bonasone, 1545) and 48948 (Rembrandt, 1655) are public domain | Art Institute of Chicago API, is_public_domain true (checked 2026-11-09) | Art Institute of Chicago artwork pages, CC0 | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: Bible stories appear only as literary sources alongside myths, Shakespeare, fables and history, with no religious claim; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b22, 2026-11-09): each field page has 12 keyed allusions and 4 decoys from at least four source kinds; the AIC search returned both object ids as public domain; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 field page and journal fit; at 680x425 the journal is a tab.
2. Finds open source cards and take a meaning line with a keyed idea. (L.7.5a)
3. Decoys are caught. (L.7.5a)
4. Analogy rows and connotation rows work, two analogies from scratch. (L.7.5b, L.7.5c)
5. My headline gets two reader cards and a revision or reason. (L.7.5a)
6. Class wall works while the page is open.
7. Print shows the journal.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the magnifier stays still; no network requests.

## Open questions
- None for Cory.
