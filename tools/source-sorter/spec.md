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
- Driver: one student (tool.json `driver: "student"`). Role: lesson. Every card is read on tap.
- Change note (spec fix, 2026-11-10): the library, Dewey, the bins and the copy meter stay. Added: Dewey sorts one card and takes one note first as the model; a Search desk where the student picks which results belong on the cart; bin and clue are now committed together, with a second miss tagged; the student builds the source entry from the card's parts for five sources; a paraphrase must also pass a meaning check; each answer sentence must be backed by a note on the same point; the refocus choice is keyed; and three quick shelves where the student writes the starting question, so there are five short projects, one a sitting.
- Shelves: "Monarch Butterflies" and "Why Do Some Places Get More Lightning?" (ten cards each), then three quick shelves of six cards: Honeybee Dances, Fall Leaves, Salt in the Sea. tool.json `modes: ["Monarchs", "Lightning", "Honeybee Dances", "Fall Leaves", "Salt in the Sea"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the answer paragraph and the source list.
- Change note (hooks, 2026-11-11): Added the three hooks: the last quick shelf is done on your own with the end screen by code, English learner supports, access. The mode list now names all five shelves.
- English learners: every spoken line is also on screen in short sentences. The words source, credible, quote, paraphrase, plagiarism and bibliography each show with an example on Dewey's card the first time they are used. Notes and answer sentences offer frames the student may take or leave: "According to __, __."

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| W.6.8 (gather) | gather relevant information from multiple print and digital sources | the student | At the Search desk pick the results that could help answer the question and leave the rest | 16 results on a full shelf, 10 on a quick shelf | the results list and the cart | 2 |
| W.6.8 (credibility) | assess the credibility of each source | the student | Sort each source into Use, Check or Skip and tap the clue that decided it, as one answer | 10 or 6 cards a shelf, 38 in all | the three bins and the clue chip on each card | 3 |
| W.6.8 (quote or paraphrase) | quote or paraphrase the data and conclusions of others while avoiding plagiarism | the student | Take notes as exact quotes or as paraphrases that pass the copy meter and the meaning check | 6 notes a full shelf, 4 a quick shelf | notes with the meter | 4 |
| W.6.8 (bibliographic information) | provide basic bibliographic information for sources | the student | Build the entry for five sources from the card's parts; the tool builds the rest the same way | 5 (no author, no date, a site, a book, an interview) | the entry slots filling | 5 |
| W.6.7 (refocus) | refocus the inquiry when appropriate | the student | When the notes point one way, narrow the question; on one shelf decide it should stay | 5 shelves | the old and new question cards | 6 |
| W.6.7 (short research project) | conduct short research projects to answer a question, drawing on several sources | the student | Write (on quick shelves) the starting question, then a short answer where every sentence is backed by a note on the same point | 5 projects | the paragraph with tags and the sorted source list | 7 |

## Screens and modes
Header (kit): title "Source Sorter"; `Cart`, `Notes`, `Answer`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A school library with a book cart of ten cards, three bins labeled Use, Check and Skip, and a question card pinned above: "Why are there fewer monarch butterflies?" A librarian's cat, Dewey, naps on the cart. First hint: "Tap a card to hear it." The first tap reads the card; the welcome is queued after it (`welcomeAfter: true`).

**Dewey goes first (the model).** Dewey handles one sample card (a zoo's web page on a different question, why flamingos are pink): reads who wrote it, when and why, drops it in Use with the clue "author named", takes one paraphrase note, checks it says what the page says, and builds its entry. It cannot be skipped the first time and `Dewey's card` reopens it.

**Search desk.** The question card is pinned and a results list shows 16 titles, each with one line about it (10 on a quick shelf). Six are about monarchs but not about why there are fewer (how to draw one, a festival, a poem, a toy, a different butterfly, a spelling list). The student ticks the ones worth a closer look and taps `Load the cart`. The check is of the whole set and says how many picks will not help, not which; one more try, then Dewey lifts the stray ones off with a reason each. The ten that remain are the cart.

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
The student drags each to a bin and taps the clue that decided it (author named or not, date, purpose: inform or sell, evidence given). Bin and clue are judged together when the card is let go. A miss says only "Look at the card again" and does not say whether the bin or the clue was off; after a second miss Dewey sorts it, says why, and the card is tagged "Dewey sorted it" on the printout. The key accepts more than one bin for some cards when the clue fits ("Check" for the 1998 article because it is old, "Use" for the garden club blog only if it cites the agency).

**Notes.** From Use cards. Two note types:
- Quote: the student highlights words in the excerpt; the note keeps them exact, in quotation marks.
- Paraphrase: the student types; the copy meter lights any run of four or more words in a row that match the source and reads "Too close" until they are reworded. A note that is a paraphrase cannot contain quotation marks around the source's words; a note that has them becomes a quote.
After a paraphrase passes the copy meter it meets the meaning check. Three short statements show, one that says what the excerpt says, one that says more than it does, one that turns it around; the student picks the one their note says. If the pick is not the keyed one, or the note shares no key word family with the excerpt, the note is marked "check the meaning" and cannot be tagged in the answer until it is rewritten.

**Entries.** For the first five sources the student takes notes from, the student builds the entry: the card's parts (author, title, publisher or site, date) are loose tiles, and the student drags them into a four-slot line in order, or drags `none given` where the card has none (an entry with no author starts with the title; no date takes "n.d."). Order and gaps are keyed; one retry, then Dewey sets it. After five, the tool builds each note's citation line from the card the same way.

**Refocus.** After six notes, a pattern card shows the notes grouped by cause; most point to milkweed and habitat loss. Dewey wakes up: "Your notes keep landing on one thing." The student narrows the question from three choices (one fits the notes, one is wider than the first question, one is about something the notes do not cover) or writes their own ("How has losing milkweed hurt monarchs?"). A choice that does not fit is answered once with "Do your notes cover that?" A question in the student's own words must name the cause their notes point to. On the Salt in the Sea shelf the notes all answer the first question, and the right call is `Keep the question`.

**Answer.** A short paragraph (5 to 8 sentences; 3 to 4 on a quick shelf); each sentence must carry a note tag. Every note belongs to one point on the pattern card, and a sentence must share a key word family with the note it is tagged to; if it does not, the tag is refused with "Does that note back this sentence?" A three-box guide sits under the paragraph: it answers the question I ended with; every sentence comes from a note; the words are mine or in quotation marks. The source list sorts alphabetically by author or title.

**Lightning shelf.** Ten cards on why some places get more lightning (warm, moist air rising; Florida's sea breezes; Lake Maracaibo's storms), same steps.

**Quick shelves.** Three small projects of six cards and four notes. Each starts from a topic card, not a question: the student writes the starting question, beside two model questions and a guide (it asks why or how; one word cannot answer it; six cards could answer it). Then Search desk, Cart, Notes, Refocus and Answer run as before.

At 1366x768 the cart and bins fit side by side; at 680x425 the bins are below.
**On your own.** The last quick shelf, Salt in the Sea, runs with Dewey quiet: his card is closed, and the search picks, each sort with its clue, each entry and the refocus call are given once with no second try and no hints. Nothing is marked until the answer paragraph is in.

**Results strip (on the end screen).** For the teacher: W.6.8 on the last shelf (search picks right, sorts with clue right, notes that passed the copy meter and the meaning check, entries right) and W.6.7 (the starting question against its guide, the refocus call, answer sentences backed by a note), in numbers and words. It prints with the rest.

## Content
- Card text written for Curio Class from the facts in Sources, labeled "practice cards" so no real page is misquoted.
- Monarch facts: monarch caterpillars eat only milkweed; habitat loss (including milkweed), insecticides and climate change are the main threats; in December 2024 the US Fish and Wildlife Service proposed listing the monarch as a threatened species.
- Lightning facts: thunderstorms form when warm, moist air rises; Florida has more lightning than most US states; Lake Maracaibo in Venezuela has some of the most frequent lightning on Earth.
- Honeybee Dances facts: a bee that finds food dances on the comb; the angle of the waggle run gives the direction from the sun and its length the distance; Karl von Frisch described it and shared a Nobel Prize in 1973.
- Fall Leaves facts: chlorophyll makes leaves green; in fall it breaks down and yellow and orange pigments show; red pigments are made in fall.
- Salt in the Sea facts: rain wears minerals out of rock and rivers carry them to the sea; water leaves the sea by evaporating and the salts stay behind; vents in the sea floor add minerals too.
- Each shelf carries in data: its results list with the off-question titles keyed; for each card its bins, clues and entry parts; for each excerpt its key word families and three meaning statements; the pattern card's points; three refocus choices with the fitting one keyed.
- On your own, with what each common wrong answer means:
  - W.6.8: ticking every result that has the topic word means the student is matching words and not the question; sorting a seller's page into Use because it has facts means purpose is not being weighed; a paraphrase that swaps a few words means the student is copying with changes and not restating; an entry that starts with the site when an author is named means the parts are not yet known.
  - W.6.7: changing the question on this shelf, where the notes already answer it, means refocusing has become a habit and not a judgment; an answer sentence with no note behind it means the student is writing from what they already believed.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can move between bins any time; notes from a card moved to Skip get a "source skipped" mark.
- The copy meter checks only when the student taps `Check note`.
- With Motion off cards move without sliding.
- Access: every action works by tap and by keyboard. Cards and entry tiles can be dragged, or picked with a tap and placed with a tap. Bins are named in words, and the copy meter shows a number and the words "too close" or "your own words", never color alone. Motion can be paused.
- On your own: one answer each, no feedback until the last part is in.

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
- event `notBacked`: "Does that note back this sentence?"
- how `search`: "Tick the ones that could help answer the question. Then tap Load the cart."
- how `meaning`: "Which one says what your note says? Tap it."
- how `entry`: "Drag the parts into the line in order."
- how `ask`: "Write the question you want this shelf to answer."
- event, whole, Dewey's card.
Read speaks the hint, which names the next action and control and never a disabled one.
- how `own`: "This shelf is on your own. I will look when your answer is written."
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
research (`R`), described in full in tools/question-sharpener/spec.md. This tool uses: Source, Shelf/Reader (the cart), Note with `R.closeness` (the copy meter), Cite (citation lines), Question (refocus) and Weight (Use, Check, Skip). Not Board, Trace, Conflicts or Matrix. The clue chips are tool-only keyed data.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Search desk | Tick everything | Six of sixteen are off the question; the set is checked whole with a count. |
| Sort | Put everything in Use | The ad, forum post and kit seller are keyed Skip. |
| Clues | Tap clues until Good clue | Bin and clue are one answer; a miss does not say which was off, and a second miss tags the card. |
| Paraphrase | Change one word; type unrelated words | `R.closeness` still finds four-word runs; unrelated words fail the key-word test and the meaning check, and the note cannot be used. |
| Entries | Drop tiles anywhere | Order and `none given` are keyed; one retry, then Dewey sets it and says so on the print. |
| Refocus | Pick any choice | Two of three do not fit the notes, and one shelf needs Keep the question. |
| Answer | Tag any note to any sentence | The sentence must share a key word family with its note. |
| On your own | Retry until right; lean on the hints | One answer each, no hints or models, and nothing is marked until all are in. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. First visit: Dewey's card (whole). `search`. Tap a card: `card`, `welcome` (queued, first time).
2. Sort: `clue` per keyed clue.
3. Notes: `tooClose` as it fires; `meaning`; `entry` on the first entry.
4. After six notes: `refocus`.
5. Answer: `untagged` and `notBacked` as they fire. Quick shelves open with `ask`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.6.7 and W.6.8 wording | thecorestandards.org, Writing Grade 6 | CCSS ELA 2010 PDF | yes |
| In December 2024 the US Fish and Wildlife Service proposed listing the monarch butterfly as threatened | Federal Register, proposed rule, 2024-12-12 (checked 2026-11-09) | US Fish and Wildlife Service press release, December 2024 | yes |
| Monarch caterpillars eat only milkweed; loss of milkweed and nectar habitat, insecticides and climate change threaten monarchs | US Fish and Wildlife Service, monarch species page | USDA Forest Service, monarch butterfly biology and threats | yes |
| Thunderstorms form when warm, moist air rises; Florida has the most lightning of the US states by density | NOAA National Weather Service, lightning science | NOAA National Severe Storms Laboratory, lightning basics | yes |
| Lake Maracaibo has some of the most frequent lightning on Earth | NASA Earth Observatory, Lake Maracaibo lightning | Guinness World Records, highest concentration of lightning | yes |
| Credibility clues (author, date, purpose, evidence) and paraphrasing in your own words with credit | Purdue OWL, evaluating sources and paraphrasing | Common Sense Education, evaluating sources | yes |
| Waggle dance: angle gives direction from the sun, length gives distance; von Frisch shared the 1973 Nobel Prize | NobelPrize.org, Physiology or Medicine 1973 | Encyclopaedia Britannica, Karl von Frisch | to confirm at Build |
| Chlorophyll breaks down in fall; yellow and orange pigments show; red pigments are made in fall | US Forest Service, science of fall colors | SUNY ESF, why leaves change color | to confirm at Build |
| Sea salt comes from minerals worn out of rock and carried by rivers, and from sea-floor vents; evaporation leaves salts behind | NOAA National Ocean Service, why is the ocean salty | US Geological Survey, why is the ocean salty | to confirm at Build |
Backed twice: 6. Added by the spec fix and not opened in this pass: 3 rows. Cut: 1 (a percent drop in eastern monarch numbers; the figures found differed by source and year).

Design choices (not claims): the cards are practice cards written for Curio Class, labeled on screen.

Checks run (Python, scratchpad b20, 2026-11-09): the Federal Register search returns the 2024-12-12 proposed rule to list the monarch as threatened; a sample paraphrase that changes one word still trips the four-word run check; contrast as in Look.

Spec fix checks (2026-11-10): counted, not run: 10 + 10 + 6 + 6 + 6 is 38 cards; 6 + 6 + 4 + 4 + 4 is 24 notes; 16 results less 6 off the question leaves the 10 cart cards. The three quick-shelf fact rows were written from memory and not opened; Build must open each source before the cards are written.

## Done when
1. Focus and fold: at 1366x768 cart and bins fit; at 680x425 the bins are below.
2. The Search desk loads the cart only after the student's picks are checked as a set. (W.6.8)
3. Cards sort with bin and clue judged together; a second miss is tagged. (W.6.8)
4. Quotes stay exact; paraphrases pass the copy meter and the meaning check. (W.6.8)
5. The student builds five entries from the card's parts; later notes get a citation line. (W.6.8)
6. The refocus card appears after the notes; the keyed choice or a fitting question is needed, and Salt in the Sea keeps its question. (W.6.7)
7. The answer needs a note tag per sentence that backs it; the source list sorts. (W.6.7)
8. The Lightning shelf and three quick shelves work the same way; quick shelves begin with the student's own question. (W.6.7)
9. Dewey's card plays first and can be reopened.
10. Print shows the answer, the source list and any tags.
11. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
12. Motion off: cards move without sliding; no network requests.
13. The last quick shelf runs with Dewey's card closed and one try for each pick, sort, entry and call; the end screen shows the result for W.6.7 and W.6.8. (W.6.7, W.6.8)
14. Every spoken instruction is also on screen; each key word shows with a picture or example at first use; any sentence frame can be left.
15. Every action works by keyboard as well as tap, drags have a tap way, nothing is shown by color alone, and motion can be paused.

## Open questions
- None for Cory.
