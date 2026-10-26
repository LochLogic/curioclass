# Reading Room: public domain and openly licensed story library (plan)

Status: plan AGREED by Cory 2026-10-25 (decisions at the bottom). The 700 stories are curated, downloaded and, since
2026-10-26, processed into readable text (see "Processing" below). Word help, questions and teacher notes come next.

## Inventory (2026-10-25)

| File | What |
|---|---|
| `data/library/sources.csv` | One row per source book: key, title, author, year, basis, license, where, Gutenberg ids |
| `data/library/stories-pd.csv` | Public domain, not-renewed and CC stories: 463 in the library, 147 on `reserve` |
| `data/library/stories-sw.csv` | 237 StoryWeaver picture books (levels 1 to 5, mostly K-3) |
| `data/library/speeches.csv` | The separate Speeches and Documents collection (15, not counted in the 700) |
| `library/_sources/` | Raw downloads, not in git: `gutenberg/<id>/` (EPUB with images + text), `storyweaver/<id>.json` + illustrations |
| `scripts/library_fetch.py` | Downloads the Gutenberg books (mirror, 2 s apart) and, with `--storyweaver`, the StoryWeaver illustrations |
| `scripts/library_sw.py` | Splits Cory's saved StoryWeaver export into one JSON per book |
| `scripts/library_check.py` | Every story's source is on disk and its title is found in the text |

**Newer and better known (Cory, 2026-10-25).** The first pass leaned on 1850 to 1920 collections. Cory asked for a
newer, more widely known selection, so 70 stories were added: Newbery winners from 1924 to 1929, the first Nancy
Drew and Hardy Boys books, Christie, Hemingway, Fitzgerald, Faulkner, Hurston, Harlem Renaissance poets, My
Father's Dragon and Stormy, Misty's Foal (never renewed), 1950s and 60s Bradbury, Vonnegut, Philip K. Dick, Asimov
and Piper stories (never renewed), and Doctorow's Little Brother (CC BY-NC-SA). The 65 least-known older picks
moved to `reserve`: kept on file, not in the library, and available as swaps.

**Round 2: lean as far into new and popular as possible (Cory, 2026-10-25).** 83 more added: every Hardy Boys book
through 1930, nine more Christie, Sayers and Wodehouse titles, Zorro, the Scarlet Pimpernel, Captain Blood, the
Oz sequels and Nesbit's magic books, and the mid-century science fiction that young readers still find: Andre
Norton, Harry Harrison (Deathworld, The Stainless Steel Rat), Weinbaum, Leiber, Pohl, Sheckley, Silverberg,
Bradley, E. E. Smith, Piper and more Philip K. Dick. 82 more older picks moved to reserve (147 in all). Classic
fairy tales and folk tales that every child knows stay in, as do the world folk tales (the plan's breadth rule);
StoryWeaver's modern picture books carry most of K-2. Speeches moved to their own collection (below).

Library total: 463 + 237 StoryWeaver = **700**.

Hard limit: famous children's books from after 1930 (Dr. Seuss, Charlotte's Web, Narnia, The Hobbit) are still
under copyright and cannot be in the library. The renewal and CC routes are where newer titles come from. For the
never-renewed titles we rely on Project Gutenberg's own copyright clearance (it checks renewals before posting a
post-1930 US work) and record that in `story.json`.

## The idea

A free library of public domain stories, poems and short nonfiction for K-12, as good to read in class as the
tools are to use. Each story is one offline HTML file, like a tool, so a teacher can keep it, project it or hand
it out. It must beat a plain Project Gutenberg page: clean text, original illustrations, words explained,
read-aloud, questions and a teacher note.

**Name:** "Reading Room" (top nav, URL `/library/`). Not just "Library", because library/AASL is already one of
our 12 subjects. Fits the cabinet-of-curiosities look (a museum reading room).

## How many, and for which grades

Stories are tagged by **grade range**, not one grade, because a fable works from grade 1 to grade 4. The goal is
**50 to 75 good fits per grade**, reached through overlap. Unique stories per band:

| Band | Unique stories | Notes |
|---|---|---|
| K-2 | about 120 | Mostly **teacher read-aloud** (fits teacher-led K-2). Public domain picture books for early readers are thin, since most are post-1930. Fables, nursery tales, Potter, poems, short folk tales. |
| 3-5 | about 180 | The deepest shelf: fairy and folk tales from many places, Just So Stories, Oz, Wind in the Willows chapters, myths. |
| 6-8 | about 180 | Myths and legends, adventure (Stevenson, London), Sherlock Holmes stories, poetry, short first-person history. |
| 9-12 | about 200 | Poe, Twain, O. Henry, Chekhov, Chopin, Hughes and Dunbar poems, whole short plays, founding speeches and documents. |
| **Total** | **about 680** | Spread over 13 grades, that gives each grade about 60 to 90 fits. |

## What counts as public domain

- **US rule:** a work published in the US in 1930 or earlier is public domain as of 2026 (1931 works join on
  2027-01-01). Foreign works published 1930 or earlier are public domain in the US too. We follow US law and say
  so on the license page. Some of these works are still under copyright in other countries (author died less than
  70 years ago).
- **Translations count separately.** A 1930-or-earlier translation is fine; a modern translation of Grimm is not.
- **Illustrations too:** we use the original public domain art from editions published in 1930 or earlier
  (Rackham, Crane, Denslow, Potter, Tenniel, Kay Nielsen).
- Also free to use: US government works and CC0 texts.
- Every story records its source edition, year, URL and translator in `story.json`. A checker refuses a story
  without them.

## Newer stories we can use (after 1930)

The 1930 line is only the simplest rule. These are also open to us, in order of how much they help:

1. **Openly licensed children's books (CC BY, CC BY-SA, CC0).** These fill the thin K-2 shelf with modern,
   leveled, illustrated picture books from many cultures:
   - Pratham Books StoryWeaver: thousands of leveled stories (levels 1 to 4), CC BY 4.0, in many languages.
   - African Storybook: thousands of picture books, CC BY.
   - Book Dash: CC BY 4.0, professionally illustrated.
   - Global Digital Library, and Bloom Library (check each book's license).

   All Creative Commons licenses are in (Cory, 2026-10-25). Each story page shows its own license. ND (no
   derivatives) stories are kept word for word: no abridging or retelling, and our glosses and questions sit
   beside the text, never in it. NC (noncommercial) fits because Curio Class is free forever. A CC BY-SA story
   keeps CC BY-SA on its own page. StoryWeaver needs a login to read; Cory made an account, and its books were
   saved through his signed-in Chrome. StoryWeaver also carries Book Dash and African Storybook titles.
2. **US works from 1931 to 1963 whose copyright was never renewed.** Before 1964 a copyright lapsed after 28
   years unless it was renewed, and most books were never renewed. The famous ones usually were. Each one is
   checked against the Copyright Office renewal records (the Stanford renewal database covers books) and the
   check is saved in `story.json`. Slower, so used for specific good finds, not bulk.
3. **US works from 1931 to 1977 published without a copyright notice.** Rare for books, more common for
   pamphlets and magazine pieces. Only with clear evidence.
4. **US federal government works, any year.** Mostly nonfiction (NASA, National Park Service, Library of
   Congress oral histories such as the WPA life histories, which need a careful read for dialect and content).
5. **Our own retellings and translations.** A folk tale or myth itself has no owner, so we can retell it from
   several old sources in our own words, or translate an old non-English text ourselves. The result is a new
   Curio Class work under CC BY, labeled as a retelling. This is the adaptation route below. Retellings of
   stories from living cultures get outside review.

`story.json` records which of these routes the story came by (`basis`: pd-1930, cc-license, not-renewed,
no-notice, us-gov, retelling).

## Sources

| Source | Use | Note |
|---|---|---|
| Standard Ebooks | First choice for text | CC0, already proofread and modernized-spelling aware |
| Project Gutenberg | Most texts | The text is public domain, but Gutenberg's trademark terms mean we **strip their header, footer and name** from anything we change |
| Wikisource | Poems, speeches, documents | Check the edition |
| Internet Archive, Library of Congress, UF Baldwin Library | Illustrations, scans of original editions | Baldwin is a children's literature collection |
| HathiTrust | Checking a first publication date | Read only |

## Curation (the real work)

A lot of famous public domain children's writing has racist caricature, colonial framing or demeaning dialect.
Each candidate gets one of three outcomes, and the reason goes in `story.json`:

1. **In.**
2. **In with a teacher note.** A note on dated attitudes or hard history, written plainly. Never gamified (same
   rule as the tools).
3. **Out.** Examples we already know to leave out: Little Black Sambo, the Uncle Remus dialect books, Kipling's
   "How the Leopard Got His Spots" (it uses a slur), and the original Doctor Dolittle.

More rules:
- **The "out" list is handled by the agents and not shown to Cory** (his call, 2026-10-25). Reasons are still
  saved in `stories.csv` so a decision can be looked up later.
- **Adaptations are welcome but always labeled.** If we abridge, modernize or retell a story, the page says
  "Adapted by Curio Class from ..." and links the original. No silent edits.
- **Folk tales from a living culture,** often first collected by outsiders, get the same outside-review flag as
  Nations and Art Passport.
- **Breadth of the world.** Track where stories come from (region, culture, original language) so the shelf isn't
  all Grimm and Andersen. Old English-language collections from many places exist: Ozaki's Japanese Fairy Book,
  Babbitt's Jataka Tales, Lang's color Fairy Books, and African and Caribbean folk tale collections, checked case by
  case.

## Reading level

Our own measure, the **Reading Room level**, worked out from sentence length, how common the words are and how much
old-fashioned vocabulary there is. A human can override it (old texts often fool formulas). We never call it Lexile,
which is a trademark. The grade range shown blends the level with the content (a scene can be easy to read but not
right for grade 2).

## What a story page has

One HTML file per story, offline, under the tool size cap:

- **Reader:** large clean text, font size control, a dyslexia-friendly font option, dark mode, page or scroll
  view, and a print view.
- **Original illustrations,** cleaned up, with credits. This needs no AI art. When an edition had no pictures, one
  plain plate (an ornament or title card) is fine.
- **Word help:** old-fashioned or hard words are underlined and a tap gives a short meaning. Written by an agent,
  checked by the verify agent.
- **Read-aloud for K-2 stories** (once the voice bank exists): sentence highlighting while the narration plays.
  Read-aloud for grades 3-12 is at the end of the roadmap; those stories put their effort into text, word help and
  questions.
- **Before / during / after:** 3 to 6 discussion questions tied to CCSS RL or RI codes, plus one "try this"
  activity.
- **Teacher note:** summary, length in minutes read aloud, themes, content notes, and the source edition.

## Data and files

```
data/library/stories.csv        one row per story: id, title, author, year, kind, origin, grades, level, status, decision
library/<id>/story.json         source edition, url, translator, credits, curation decision + reason, codes
library/<id>/text.md            the cleaned text (paragraphs, simple markup for glosses)
library/<id>/art/               cleaned public domain plates
library/<id>/voice/             later
library/<id>/<id>.html          the bundled reader (made by a script, like bundle_tool.py)
scripts/library.py              build, level, check (source fields present, no Gutenberg branding left, size cap)
```

`kind` = fable, fairy tale, folk tale, myth, short story, picture book, poem, play, speech or document. Longer books
(Oz, Wind in the Willows) come in whole, as **chapter sets**: one entry with chapters inside.

## Excerpts: a separate add-on shelf

Excerpts (a Shakespeare scene, a Douglass chapter, a passage from a novel) are **not part of the main library**.
They live on their own shelf, `/library/excerpts/`, with `excerpt: true` in `story.json`. They are built after the
main library is done and never count toward the per-grade goals. Each one names the work it comes from, says
what was cut, and links the full text.

## Speeches and Documents: a separate collection

Speeches and founding documents are **their own collection** (Cory, 2026-10-25), not part of the 700 stories:
`data/library/speeches.csv`, shown at `/library/speeches/`. Same story page format (text, word help, questions,
teacher note), tagged by grade range. Now: the Declaration, the Gettysburg Address, Lincoln's Second Inaugural,
Douglass's "What to the Slave Is the Fourth of July?", FDR's First Inaugural, Four Freedoms and Pearl Harbor
addresses, Eisenhower's Farewell, Kennedy's Inaugural and moon speech, Johnson's "We Shall Overcome", Reagan's
Challenger and Brandenburg Gate speeches, and the Apollo 11 landing transcript. US government works are free to
use; speeches by private citizens (for example "I Have a Dream") are still under copyright and stay out.

## Site pages

| URL | Page |
|---|---|
| `/library/` | Reading Room home: by band, by kind, featured shelves |
| `/library/grade/<k..12>/` | Stories that fit a grade |
| `/library/kind/<kind>/` | Fables, myths, poems, ... |
| `/library/shelf/<theme>/` | Themed shelves: tricksters, animals who talk, journeys, voices of freedom |
| `/library/<id>/` | Story page (summary, teacher note, read, download) |
| `/library/speeches/` | Speeches and Documents (its own collection) |
| `/library/excerpts/` | The excerpts add-on shelf (later) |

Links both ways with the rest of the site: grade pages get a small "From the Reading Room" strip, and ELA
reading-literature modules link to matching stories by standard code. Later, a few **"works with any story"
tools** (story map, character feelings tracker, compare two versions) can open any story in the library.

### Built (2026-10-25): pages ready to populate

`scripts/build_site.py` (section "reading room") and `site/templates/library/` build every page above except themed
shelves and excerpts. Kinds are grouped into seven shelves (`/library/kind/<shelf>/`: picture-books, short-stories,
poems, tales, chapter-books, plays, true-stories). Band pages live at `/library/grade/k-2/` and so on. Every row not
marked `reserve` gets a page now; until its text exists the page says "on the reading desk" and is kept out of the
sitemap and search engines.

**To make a story ready**, add `library/<id>/` (same id as the CSV row):

- `text.md`: the story in Markdown. `## Heading` for chapters or parts, `---` for a scene break (also a page break in
  page view), `![alt](art/p01.jpg)` for pictures. A gloss is `{word|meaning}`; readers tap the word to see the meaning.
- `story.json` (all optional): `summary`, `level` (Reading Room level, never "Lexile"), `adapted` (say how, for
  example "abridged to 1,200 words"; shown on the page and in the download), `words` (else counted),
  `questions` `{"before": [...], "during": [...], "after": [...]}` where each item is a string or
  `{"q": "...", "ccss": "RL.3.2"}`, and `teacher_note` (HTML).
- `art/`: pictures used by `text.md`. They are copied to the site and inlined into the download.

The build then makes the story page with the reader (text size, Book, Plain or Spaced font, Paper, Sepia or Night,
scroll or page view, print) and a one-file offline download at `/library/<id>/<id>.html`. Attribution comes from
`sources.csv` (or the StoryWeaver export) automatically. To check the reader locally without a real story, run
`python scripts/build_site.py --preview`, which adds a made-up fable from `site/fixtures/reader-preview/` at
`/library/reader-preview/`. Never deploy a `--preview` build.

Still to do: themed shelves, the "From the Reading Room" strip on grade pages, read-aloud for K-2, and a
self-hosted dyslexia-friendly font for the Spaced option (it uses Verdana with extra spacing for now).

**Deploy gate.** A plain `python scripts/build_site.py` leaves the whole Reading Room out (no `/library/` pages, nav
or footer link, sitemap entries or search rows). Build with `--library` to include it. Cory lifted the earlier hold on
2026-10-25: deploys now build with `--library` and the Reading Room goes live as it is, to be filled in later.

### Mythology and Sacred Texts (2026-10-25)

**Mythology** (`/library/mythology/`, one page per tradition) comes from `data/library/mythology.csv`, which has the
usual columns plus `tradition`: greek, roman, homer, beowulf, norse, celtic, egyptian, mesopotamian, native, african,
south-asian, east-asian, mesoamerican, pacific (labels and blurbs in `MYTH` in `build_site.py`). A row with a blank
title is a cross-listing: it names a story that lives in another collection by id, so the Odyssey or the Zitkala-Sa
Iktomi stories appear on both shelves with one page. Native stories are credited to their nation and told by Native
writers where possible; the tradition page notes that some stories (Lakota and Dakota Iktomi) are told only in winter.

**Sacred Texts** (`/library/sacred-texts/`) comes from `data/library/sacred-texts.csv`: one central text per
religion, each in a single public-domain English translation, presented without commentary. The framing is "for
teaching about religion, not for teaching religion". Choices: Tanakh (JPS 1917, via Sefaria), Bible (KJV), Qur'an
(Pickthall 1930), Bhagavad Gita (Arnold), Dhammapada (Muller), Japji (Macauliffe 1909), Tattvartha Sutra (Jaini 1920),
Tao Te Ching and Analects (Legge), Kojiki (Chamberlain), the Gathas (Mills, selection), Book of Mormon, the Hidden
Words, the Egyptian Book of the Dead (Budge, selections) and the Poetic Edda (Bellows). Still to verify: the Jain
archive item really is Jaini's translation, and the Hidden Words edition year and copyright basis. The long ones
(Bible, Tanakh, Qur'an) will need a multi-part reader with a table of contents before they can be made ready.

**Fetch modes** in `scripts/library_fetch.py`: Gutenberg (default), `--storyweaver`, `--other` (Wikisource),
`--archive` (Internet Archive OCR text) and `--sefaria` (a Tanakh version). The last three write to
`library/_sources/other/<key>/`.

### Processing: every row readable (2026-10-26)

`scripts/library_process.py` turns the downloads into `library/<id>/text.md`, `story.json` and `art/` for every row not
on `reserve` (586 rows; the StoryWeaver books, Wikisource, Sefaria and archive.org texts each have their own reader in
the same script). Run `python scripts/library_cuts.py && python scripts/library_process.py <ids>`; `--redo` redoes
every row and `--report` writes `library/_sources/process-report.csv` (how each row was placed, words, flags).
`--outline SOURCE [words | a-b]` prints a source's numbered blocks, which is how cuts are written. Git keeps
`text.md` and `story.json` (about 90 MB); `art/` (about 350 MB) is left out like `_sources/`, and `--redo` remakes it
from the downloads (fetch first on a fresh machine).

How a Gutenberg row is placed, in order: a hand cut in `scripts/library_cuts.py` (syntax in its docstring: `#Heading`,
`start >> end` with phrases or `@N` block numbers, `[Label]` pieces, `txt:` for a poem from the plain text), else the
heading that matches the title (or the row's `find` text), else the whole book when the book is the story. The walk
reads the epub in document order: contents tables are skipped but picture-layout tables are read cell by cell,
`<pre>` verse keeps its lines and indents, titled poem groups (Mother Goose) split by title, drop caps are rejoined,
text wrapped around pictures a word to a line is joined back into paragraphs (and a drop cap set as a letter picture
comes back from the plain text). `trim_ends` then strips front matter (copyright, printers, contents), the back
(publisher ads, series lists, transcriber notes, glossaries, pronunciation lists, "Notes to ..."), and anything after
a closing THE END.

Known gaps, by choice: `tattvartha` has no usable source yet (the row stays "on the reading desk"); the 1925 In Our
Time is not on Gutenberg, so the Hemingway stories from it stay on reserve. Swaps made while processing are recorded in
each row's `note`: "Dream Variations" replaces Hughes's "Dreams" (not in a public domain book online), and the
Caroling Dusk selection leaves out "Incident" (a slur) and "Song for a Dark Girl" (a lynching).

## The pipeline

1. **Candidate list** (agent, no downloads): title, author, year, edition, source, grades, kind, origin. About 900
   candidates for the 680 spots.
2. **License and curation pass** (agents only; a second agent checks the first one's "out" and "with a note" calls).
3. **Bulk download** (after this plan is agreed): text and illustration scans, into an untrusted downloads folder.
4. **Clean and level** (script plus agent): strip branding, fix OCR, mark chapters, compute the level.
5. **Enrich** (agent): glosses, questions, teacher note.
6. **Verify** (fresh agent, cold): text matches the source, glosses and codes are right, notes are fair.
7. **Bundle and go live** in waves of about 50, onto the Review Desk like the tools.
8. **Voice** for K-2 stories as the voice bank allows. Grades 3-12 read-aloud and the excerpts shelf come last.

## Pilot (before any bulk work)

Ten stories in the 3-5 band, built end to end to prove the format, the reader and the pipeline:

1. Five Aesop fables (as one fables set)
2. "The Elves and the Shoemaker" (Grimm)
3. "The Ugly Duckling" (Andersen)
4. "The Elephant's Child" (Kipling, Just So Stories, 1902, with its own illustrations)
5. "Momotaro" (Ozaki, Japanese Fairy Book, 1908)
6. "The Monkey and the Crocodile" (Babbitt, Jataka Tales, 1912)
7. "The Velveteen Rabbit" (Williams, 1922, Nicholson illustrations)
8. "The River Bank" (Grahame, The Wind in the Willows chapter 1, 1908)
9. An Anansi story (collection to be chosen and checked)
10. "The Owl and the Pussy-cat" (Lear, poem)

## Decisions (Cory, 2026-10-25)

1. Name: **Reading Room**.
2. **Adaptations are OK,** always labeled.
3. **Excerpts are OK, but only on their own add-on shelf,** built after the main library.
4. **Cory does not see the "out" list.** Agents decide, a second agent checks.
5. **Read-aloud for K-2 is important;** read-aloud for other grades goes to the end of the roadmap.
6. Pilot band: no preference, so the pilot stays 3-5 as above (the deepest shelf, and needs no voice).
7. Post-1930 sources are in, by the routes in "Newer stories we can use".
