# Wave 4 spec log

Rules: `docs/agents/BATCH-W4.md`. 42 specs in five groups (9-12 ELA and library, ELD 6-12), one agent per group,
at most three at once beside the wave 3 art agent. One joint review follows.

## Agent reports

### ela-research (6, done)

- No renames written; enduring-questions raises one (below).
- Tools: research-notebook (g9, calm-professor, light, fountain-pen blue #2348a6), portrait-in-four-media (g10,
  knowing-guide, dark, coral #ff8a66; Met 286656, 291505, 291515, 286896, 291500, 285421, 283097), source-mixer (g11,
  news-reader, dark, console cyan #45d4e8; Met 260387), question-sharpener (g12 tycoon, big-sister, light, violet
  #6237c8), source-portfolio (library 9-12, firm-captain, light, archive green #17693c), enduring-questions (library
  9-12, gravel-ranger, dark, lantern gold #ffd166).
- Family engine: research (kit/research.js), described in full in question-sharpener: Source, Shelf/Reader, Note with
  closeness(), Board, Trace, Conflicts and corroboration (R.web, independent origins), Weight, Matrix, Cite (MLA 9 /
  APA 7), Question/Season, Store. Lower-grade reuse named: Big Question Chart, Note Card Shuffle, Research Rover, Fact
  Fusion, Source Sorter, Summary Scaffold. source-mixer also uses data-desk.
- spec_sheet.py: no voice, accent or art clash inside the group.

Open questions:
- [research-notebook] Pokagon's 1895 sentence uses "white men" and "red men". Keep it with a context note, or drop it?
- [research-notebook] OK to treat a reference entry written for Curio Class as a citable source?
- [portrait-in-four-media] OK to use a made-up conservator interview (labeled) and a storyboard with a deliberate wrong
  date (1841) and unhedged "firsts"?
- [portrait-in-four-media] The concept says "a scientist's life"; Atkins is a botanist and photographer. Good fit?
- [source-mixer] A 1936 radio transcript instead of the concept's "video transcript" (alternative: the narration of The
  Plow That Broke the Plains)?
- [source-mixer] Should teachers see or change the support/complication tags on each source part?
- [question-sharpener] Tycoon currency is hours, not money. Meets the overlap reshape, or make it a simulator?
- [question-sharpener] Keep AASL.Inquire on this grade 12 ELA tool?
- [question-sharpener] Add a "my own topic" path?
- [source-portfolio] Made-up tribal fisheries department beside the real Lower Elwha Klallam card: Native educator
  review?
- [source-portfolio] Keep C3 D1.5, D3.1 and D3.2 on a library tool?
- [enduring-questions] Title matches an NEH grant program. Keep, or rename (for example "The Long Argument")?
- [enduring-questions] Phones and cameras are live local debates and the experts are composites. Add a teacher note?
- [enduring-questions] The "who was left out" lines (slavery, the three-fifths clause, who could vote): parent preview?

### ela-lit (10, done)

- No renames.
- Tools: character-web (9, wise-mentor, rose #ff8fb8), tension-meter (9, news-reader, seismograph red #ff5a4f),
  world-lit-atlas (10, upbeat-guide, atlas green #8ff05a), american-lit-timeline (11, warm-teacher, parchment #e3c98a),
  shakespeare-remix (9, casual-peer, violet #9d8cff), globe-theatre-stage (12, lively-host, Globe oak #c0a080),
  page-to-screen (10, friendly-dad, non-photo blue #7cc4ff), ambiguity-lab (12, curious-librarian, dusk periwinkle
  #b9c4ff), idea-threads (9-12, bright-teacher, magenta #ff6fd0), tone-dial (10, gentle-storyteller, orchid #f29ff0).
- Family engines: shakespeare (kit/bard.js: Text, Script, Gloss, Align, Stage, Score, Store) in full in
  globe-theatre-stage, used by shakespeare-remix; lit-timeline (kit/lit-timeline.js) in full in american-lit-timeline.
- Voices and accents checked against specs on disk 2026-10-27; recheck in the joint review (ela-argument and ela-craft
  were still writing). news-reader is also source-mixer's voice.

Open questions:
- [character-web] Bertha Mason note enough at grade 9, or drop? Codex portraits or monograms only?
- [tension-meter] Parent preview (Owl Creek hanging; Dracula attacks, Renfield)? Join data-desk instead of its own chart?
- [american-lit-timeline] Parent preview for pairs 6 and 2 (slavery, boarding schools)? Keep Bradford's "wild men" and
  Edwards's sermon? Timeline stops at 1929 (public domain line)?
- [shakespeare-remix] The lovers' deaths in Set 1. Modern Afterlives titles (title only), or pre-1930 works only?
- [globe-theatre-stage] Delivery shown visually with no audio (one voice style per tool): OK? Keep Trifles here or give
  it its own tool? Parent preview (Trifles murder, the Shrew speech)?
- [world-lit-atlas] Parent preview for Equiano (kidnapping, birthplace debate)? Cut "Indian-fashion" from Azuela or keep
  with a note? No pins yet for the Middle East, South America or Oceania.
- [page-to-screen] Made-up Suspicion meter labeled "our estimate" OK? Parent preview (Vera's "newly dug grave" lie)?
- [ambiguity-lab] Parent preview (witch meeting, "devilish Indian", "new-born babe")? Stockton's "savage blood": teacher
  note enough, or on screen? Invented closed endings OK?
- [idea-threads] Parent preview (Du Bois's "Negro", "Southern outrages")? Check the Eisenhower text against GovInfo
  page images? One paragraph cut from Du Bois and Thoreau: OK?
- [tone-dial] Spooky Ominous column fine at grade 10? Keep or drop audio for the six one-tone versions?
