# Opinion Builder

## One idea
The student writes a letter to the school library committee about which of three new books the class should buy, building an opinion, two reasons with because, a result with so and a closing from frames and word banks, then watches a committee member test each reason against the book (a reason about the book holds; "because I want it" or a reason that fits any book gets "Would that be true for every book?"), so they learn to state an opinion and back it with reasons that really support it.

## Not like
- i-choose-because (K-2, spec): one spoken reason for a choice. Here a written letter with two reasons, a result and a closing.
- talk-moves-trainer (3-5, spec later): discussion moves in a group. Here a written letter to readers.
- cause-and-effect-rewind (3-5, spec): because for a cause in science. Here because for a reason in an opinion.
- math-explainer (3-5, spec, this batch): steps of a solution. Here reasons for an opinion.
- time-machine-talk (3-5, spec, this batch): past tense narration. Here present tense opinions.

## Who and how
- Grades 3 to 5, English Language Development, module "Opinions with Reasons". Standards: WIDA ELD-LA (Standard 2, the language of language arts), Argue key language use (WIDA 2020).
- Driver: one student; class mode is "Committee vote", where the projector shows three letters (built-in samples) and the class votes on which reasons hold (tool.json `driver: "student"`). Every blurb, tile and letter is read on tap.
- Three topic sets: books for the library (main), a class pet, a field trip. Help setting: Lots (full frames with picture tiles), Some (sentence starters with word banks), Little (slot names only, then typing). Teacher notes map them to WIDA 1-2, 3-4 and 5-6. tool.json `modes: ["Write my letter", "Committee vote"]`, `minutes: "15-25"`, `grades_label: "Grades 3-5"`.
- Nothing is saved; `Print` prints the letter.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| WIDA Argue (state an opinion) | Build "I think we should buy ___." | the opinion slot | 2 |
| WIDA Argue (reasons with because) | Build two reasons from the blurb's word bank | the committee member's test on each reason | 3 |
| WIDA Argue (reasons that support) | Fix a reason that fits every book or is only a feeling | "Would that be true for every book?" | 3 |
| WIDA Argue (result with so; closing) | Build "so ___" and "That is why ___." | arrows: because points back, so points forward | 4 |
| WIDA ELD-LA (talking about books) | Use book words (character, adventure, funny, facts, mystery, ending) | the word bank by book | 3 |

## Screens and modes
Header (kit): title "Opinion Builder"; `Books`, `Letter`, `Committee`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A school library's front desk with a new-books cart holding three covers and a note pinned above: "We can buy one new book for your class. Which one? Tell us why. The Library Committee." Ms. Hollis, the librarian, sits at the desk. First hint: "Tap a book to hear about it." The first tap reads that blurb; the welcome is queued after it (`welcomeAfter: true`).

**Books.** Three made-up books with covers and blurbs: "The Night the Bridge Sang" (a mystery in a river town, a girl and her grandfather solve it), "Ten Tiny Engineers" (true facts about animals that build, like beavers and weaver birds, with diagrams), "Captain Pickle and the Lost Lunch" (a funny comic about a cafeteria hero). Each blurb's key words go into that book's word bank.

**Letter.** Five slots: Opinion (I think we should buy...), Reason 1 (because...), Reason 2 (Also,...), Result (so...), Closing (That is why...). Each slot can be read back. The finished letter shows two arrows: because pointing back from the reason to the opinion, so pointing forward from the reasons to the result.

**Committee.** Three members (Ms. Hollis, a fourth grade student named Jada, and Mr. Okoye, a parent) test each reason, one at a time: a reason about this book ("because it has a mystery to solve") gets a nod and the matching blurb line glows; a reason that fits every book ("because it is a book", "because it is good") gets "Would that be true for every book?"; a feeling only ("because I want it") gets "Why would other kids like it too?" The student revises; then the committee reads the letter aloud and votes, and the book goes on the cart with the student's letter tucked inside.

**Committee vote.** On the projector, three sample letters for the class to test reason by reason.

At 1366x768 the books and letter fit; at 680x425 the books are a tab.

## Content
- Three books per topic set, made-up titles and covers, blurbs and word banks written for Curio Class. Each reason tile is tagged "about this book", "fits every book" or "feeling only".
- Pet and field trip sets follow the same frames with their own blurbs.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Slots can be rebuilt any time; the committee retests only the changed slot.
- With Motion off the arrows appear without drawing and the book doesn't slide to the cart.

## Look
- Accent `--brand` #6d4a1d library oak brown (header, desk, slot frames); gold #f4c542 (a reason that holds, the because and so arrows); paper #faf5ee; ink #231707; muted #615446. Scene: a warm school library front desk.
- Contrast (WCAG 2.1, computed): white on brand 7.93:1; brand on paper 7.31:1; ink on paper 16.17:1; muted on paper 6.76:1; ink on gold 10.79:1.
- Never color alone: reasons that hold show a check with words; arrows are labeled because and so.
- Different from this batch (party magenta, clock blue, chalkboard green, museum violet).

## Art
- People art goes to Gemini: Ms. Hollis (a white woman in her fifties with reading glasses on a chain), Jada (a Black girl about ten), Mr. Okoye (a Nigerian American man in his forties), 3 poses each (listening, nodding, asking); "illustrated school library committee member <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): the library desk with a book cart (1); nine made-up book covers, no real titles (9).
About 19 images. Drawn in code: slots, arrows, tiles.

## Voice
Bank voice `curious-librarian` as Ms. Hollis and the hint voice (unique in this batch); the student's letter and the blurbs are read by `smooth-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.topic + ':' + state.slot`, `welcomeAfter: true`.
- how `welcome`: "Pick the book you think the class should have. Then write us a letter that tells us why."
- event `blurb`: the book's blurb.
- event, whole, `slot`: the slot read back.
- event `every`: "Would that be true for every book?"
- event `feeling`: "Why would other kids like it too?"
- event `holds`: "That's a reason about this book."
- event, whole, `letter`: the finished letter, then the vote.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: blurbs and word banks, five-slot letter builder, tagged reason tiles with the committee test, because and so arrows, help levels.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Reasons | Use "because it is good" twice | Tagged "fits every book"; the committee asks each time. |
| Reasons | Copy one reason into both slots | Reason 2 must differ from Reason 1. |
| Typed reasons (Little help) | Type anything | A typed reason holds only if it uses a word from the chosen book's bank; otherwise the committee asks "Where does the book show that?" |
| Result | Leave out so | The vote waits for a result slot with so. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a book: `blurb`, `welcome` (queued, first time).
2. Letter: `slot` (whole) on read back.
3. Committee: `holds`, `every` or `feeling` per reason; `letter` (whole) at the end.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| WIDA 2020: Standard 2 is the language of language arts; Argue covers stating an opinion and supporting it with reasons | WIDA ELD Standards Framework, 2020 Edition | WIDA, Key Language Uses: A Closer Look (2020) | yes |
| Grade 3 to 5 opinion writing: state an opinion, give reasons that support it, use linking words (because, therefore, since), and give a conclusion | CCSS W.3.1, W.4.1, W.5.1 (thecorestandards.org) | CCSS ELA 2010 PDF | yes |
Backed twice: 2. Cut: 0.

Checks run (Python, scratchpad b26, 2026-11-09): every "about this book" reason tile for each book uses a word from that book's blurb; no "about this book" tile is shared by two books; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 books and letter fit; at 680x425 books are a tab.
2. The opinion slot names one book. (WIDA Argue)
3. The committee tests each reason and asks about reasons that fit every book or are only feelings. (WIDA Argue, ELD-LA)
4. Because and so arrows show in the letter, and the closing completes it. (WIDA Argue)
5. The committee reads the letter and votes.
6. Help levels behave as in Who and how.
7. Committee vote, the pet and field trip sets, and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: arrows appear without drawing; no network requests.

## Open questions
- Home-language support: this follows Cory's open question on home-language glossaries for the ELD tools (default used: English only, with pictures and read-aloud).
