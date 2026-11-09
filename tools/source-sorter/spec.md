# Source Sorter

## One idea
The student answers "Why are there fewer monarch butterflies?" by sorting a cart of ten source cards into Use, Check and Skip, tapping the clue on each card that decided it (no author, selling something, written in 1998), then turns the keepers into notes as exact quotes or paraphrases while a copy meter lights any run of the source's own words, and halfway through the sources show the question is too big and the student narrows it, so they learn to judge a source from its own clues, take notes without copying, and credit every source.

## Not like
- fact-fusion (5, spec): combining three trusted sources into one table. Here judging which sources to trust at all.
- fake-or-fact-lab (6-8, concept): checking made-up pages by reading other sites. Here clues inside the source itself.
- research-rover (4, spec): notes from given sources, grade 4. Here credibility, paraphrase and a refocused question.
- research-notebook (9, concept): threads from sentences back to source words. Here a sorting cart and copy meter, grade 6.
- linked-feature (spec): building a linked article. Here the research before writing.

## Who and how
- Grade 6, ELA, module "Research and Citing Sources" (Writing). Standards: W.6.7, W.6.8.
- Driver: one student (tool.json `driver: "student"`). Every card is read on tap.
- Shelves: "Monarch Butterflies" and a second shelf, "Why Do Some Places Get More Lightning?" tool.json `modes: ["Monarchs", "Lightning"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the answer paragraph and the source list.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.6.8 (credibility) | Sort each source into Use, Check or Skip and tap the clue that decided it | the three bins and the clue chip on each card | 2 |
| W.6.8 (quote or paraphrase) | Take notes as exact quotes in quotation marks or as paraphrases the copy meter passes | notes with the meter | 3 |
| W.6.8 (bibliographic information) | Each note carries a citation line built from the card's author, title, publisher and date | the citation line | 4 |
| W.6.7 (refocus) | When the sources point to one cause, narrow the question | the old and new question cards | 5 |
| W.6.7 (short research project) | Write a short answer where every sentence carries a note tag | the paragraph with tags and the sorted source list | 6 |

## Screens and modes
Header (kit): title "Source Sorter"; `Cart`, `Notes`, `Answer`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A school library with a book cart of ten cards, three bins labeled Use, Check and Skip, and a question card pinned above: "Why are there fewer monarch butterflies?" A librarian's cat, Dewey, naps on the cart. First hint: "Tap a card to hear it." The first tap reads the card; the welcome is queued after it (`welcomeAfter: true`).

**Cart.** Ten cards, each showing author, title, publisher or site, date, purpose and a short excerpt. Sources (made-up cards based on real kinds of sources, labeled "practice cards" on screen, with facts from the Sources table):
- A government wildlife agency page (US Fish and Wildlife Service style).
- A conservation science group's report.
- An interview with a university butterfly scientist.
- An encyclopedia entry.
- A school garden club blog.
- An ad for a garden spray that "keeps your garden bug-free".
- A 1998 newspaper article.
- A forum post by "ButterflyFan22" with no sources.
- A 2024 news article about the proposed listing.
- A video description from a channel selling butterfly kits.
The student drags each to a bin and taps the clue that decided it (author named or not, date, purpose: inform or sell, evidence given). The key accepts more than one bin for some cards when the clue fits ("Check" for the 1998 article because it is old, "Use" for the garden club blog only if it cites the agency).

**Notes.** From Use cards. Two note types:
- Quote: the student highlights words in the excerpt; the note keeps them exact, in quotation marks.
- Paraphrase: the student types; the copy meter lights any run of four or more words in a row that match the source and reads "Too close" until they are reworded. A note that is a paraphrase cannot contain quotation marks around the source's words; a note that has them becomes a quote.
Each note gets a citation line built from the card.

**Refocus.** After six notes, a pattern card shows the notes grouped by cause; most point to milkweed and habitat loss. Dewey wakes up: "Your notes keep landing on one thing." The student narrows the question from three choices or writes their own ("How has losing milkweed hurt monarchs?").

**Answer.** A short paragraph (5 to 8 sentences); each sentence must carry a note tag. The source list sorts alphabetically by author or title.

**Lightning shelf.** Ten cards on why some places get more lightning (warm, moist air rising; Florida's sea breezes; Lake Maracaibo's storms), same steps.

At 1366x768 the cart and bins fit side by side; at 680x425 the bins are below.

## Content
- Card text written for Curio Class from the facts in Sources, labeled "practice cards" so no real page is misquoted.
- Monarch facts: monarch caterpillars eat only milkweed; habitat loss (including milkweed), insecticides and climate change are the main threats; in December 2024 the US Fish and Wildlife Service proposed listing the monarch as a threatened species.
- Lightning facts: thunderstorms form when warm, moist air rises; Florida has more lightning than most US states; Lake Maracaibo in Venezuela has some of the most frequent lightning on Earth.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can move between bins any time; notes from a card moved to Skip get a "source skipped" mark.
- The copy meter checks only when the student taps `Check note`.
- With Motion off cards move without sliding.

## Look
- Accent `--brand` #8a5200 cart amber (header, cart, bins); gold #f4c542 (copy meter runs, note tags); paper #fbf6ee; ink #2a1800; muted #66584a. Scene: a warm school library.
- Contrast (WCAG 2.1, computed): white on brand 6.39:1; brand on paper 5.94:1; ink on paper 15.88:1; muted on paper 6.38:1; ink on gold 10.51:1.
- Never color alone: bins have words; the meter reads "Too close" or "Your words".
- Different from this batch (ivy green, coaster magenta, roots blue, rally orange).

## Art
- Local FLUX (`scripts/localart.py`): library with a book cart and bins (1); Dewey the cat (4 poses: nap, stretch, point, peek), "A friendly gray tabby library cat <pose>, soft gouache, plain white background"; 1:1; cutout yes; a milkweed field with monarchs (1); monarch caterpillar on milkweed (1); thunderstorm over a lake at night (1).
About 8 images. Drawn in code: cards, bins, meter, citation lines.

## Voice
Bank voice `curious-librarian` as Dewey and the card reader (unique in this batch). `Curio.voice` with `scope: () => state.shelf + ':' + state.view + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: "Every source leaves clues. Who wrote it? When? Why? Sort each card, and tap the clue that decided it."
- event, whole, `card`: the tapped card.
- event `clue`: "{No author}. Good clue."
- event `tooClose`: "Too close to the source's words. Say it your way."
- event `refocus`: "Your notes keep landing on one thing."
- event `untagged`: "This sentence needs a note tag."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
research (`R`), described in full in tools/question-sharpener/spec.md. This tool uses: Source, Shelf/Reader (the cart), Note with `R.closeness` (the copy meter), Cite (citation lines), Question (refocus) and Weight (Use, Check, Skip). Not Board, Trace, Conflicts or Matrix. The clue chips are tool-only keyed data.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Put everything in Use | The ad, forum post and kit seller are keyed Skip; their clue chips show why. |
| Clues | Tap any clue | The clue must be one keyed for that card and bin. |
| Paraphrase | Change one word | `R.closeness` still finds four-word runs. |
| Answer | Write without tags | Each sentence needs a note tag. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a card: `card`, `welcome` (queued, first time).
2. Sort: `clue` per keyed clue.
3. Notes: `tooClose` as it fires.
4. After six notes: `refocus`.
5. Answer: `untagged` as it fires.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.6.7 and W.6.8 wording | thecorestandards.org, Writing Grade 6 | CCSS ELA 2010 PDF | yes |
| In December 2024 the US Fish and Wildlife Service proposed listing the monarch butterfly as threatened | Federal Register, proposed rule, 2024-12-12 (checked 2026-11-09) | US Fish and Wildlife Service press release, December 2024 | yes |
| Monarch caterpillars eat only milkweed; loss of milkweed and nectar habitat, insecticides and climate change threaten monarchs | US Fish and Wildlife Service, monarch species page | USDA Forest Service, monarch butterfly biology and threats | yes |
| Thunderstorms form when warm, moist air rises; Florida has the most lightning of the US states by density | NOAA National Weather Service, lightning science | NOAA National Severe Storms Laboratory, lightning basics | yes |
| Lake Maracaibo has some of the most frequent lightning on Earth | NASA Earth Observatory, Lake Maracaibo lightning | Guinness World Records, highest concentration of lightning | yes |
| Credibility clues (author, date, purpose, evidence) and paraphrasing in your own words with credit | Purdue OWL, evaluating sources and paraphrasing | Common Sense Education, evaluating sources | yes |
Backed twice: 6. Cut: 1 (a percent drop in eastern monarch numbers; the figures found differed by source and year).

Design choices (not claims): the cards are practice cards written for Curio Class, labeled on screen.

Checks run (Python, scratchpad b20, 2026-11-09): the Federal Register search returns the 2024-12-12 proposed rule to list the monarch as threatened; a sample paraphrase that changes one word still trips the four-word run check; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 cart and bins fit; at 680x425 the bins are below.
2. Cards sort with keyed clue chips. (W.6.8)
3. Quotes stay exact; paraphrases pass the copy meter. (W.6.8)
4. Each note has a citation line. (W.6.8)
5. The refocus card appears after six notes and the question narrows. (W.6.7)
6. The answer needs a note tag per sentence; the source list sorts. (W.6.7)
7. The Lightning shelf works the same way.
8. Print shows the answer and source list.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: cards move without sliding; no network requests.

## Open questions
- None for Cory.
