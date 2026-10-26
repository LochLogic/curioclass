# Reading Room: public domain story library (plan, DRAFT for Cory)

Status: draft 2026-10-25, nothing downloaded yet. The path and structure get agreed first; downloads and text
cleanup then run in bulk.

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
| 6-8 | about 180 | Myths and legends, adventure (Stevenson, London), Sherlock Holmes stories, poetry, first-person history (Douglass excerpts). |
| 9-12 | about 200 | Poe, Twain, O. Henry, Chekhov, Chopin, Hughes and Dunbar poems, Shakespeare scenes, founding speeches and documents. |
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
- **No silent edits.** If we abridge or adapt a story (likely for some K-2 read-alouds), the page says
  "Adapted by Curio Class from ..." and links the original.
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
- **Read-aloud** (later, once the voice bank exists): sentence highlighting while the narration plays. With about
  680 stories, this is the biggest cost, so it goes in waves, K-2 first.
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

`kind` = fable, fairy tale, folk tale, myth, short story, chapter (from a longer book), poem, play scene, speech or
document. Longer books (Oz, Wind in the Willows) come in as **chapter sets**, one entry with chapters inside.

## Site pages

| URL | Page |
|---|---|
| `/library/` | Reading Room home: by band, by kind, featured shelves |
| `/library/grade/<k..12>/` | Stories that fit a grade |
| `/library/kind/<kind>/` | Fables, myths, poems, ... |
| `/library/shelf/<theme>/` | Themed shelves: tricksters, animals who talk, journeys, voices of freedom |
| `/library/<id>/` | Story page (summary, teacher note, read, download) |

Links both ways with the rest of the site: grade pages get a small "From the Reading Room" strip, and ELA
reading-literature modules link to matching stories by standard code. Later, a few **"works with any story"
tools** (story map, character feelings tracker, compare two versions) can open any story in the library.

## The pipeline

1. **Candidate list** (agent, no downloads): title, author, year, edition, source, grades, kind, origin. About 900
   candidates for the 680 spots.
2. **License and curation pass** (agent, then Cory skims the list of "out" and "with a note" stories).
3. **Bulk download** (after this plan is agreed): text and illustration scans, into an untrusted downloads folder.
4. **Clean and level** (script plus agent): strip branding, fix OCR, mark chapters, compute the level.
5. **Enrich** (agent): glosses, questions, teacher note.
6. **Verify** (fresh agent, cold): text matches the source, glosses and codes are right, notes are fair.
7. **Bundle and go live** in waves of about 50, onto the Review Desk like the tools.
8. **Voice** later, by wave.

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

## Decisions for Cory

1. Name: "Reading Room" OK?
2. Allow clearly labeled **adaptations** for K-2 read-alouds, or originals only?
3. Include **excerpts** from long works (a Shakespeare scene, a Douglass chapter), or whole works only?
4. Is the "out" list a quick skim for you, or do you want to see every borderline story?
5. Read-aloud for all stories eventually, or only K-2 plus selected ones?
6. Pilot band: 3-5 as above, or start with K-2?
