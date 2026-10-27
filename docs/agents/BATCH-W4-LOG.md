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

### ela-argument (11, done)

- No renames.
- Tools: argument-map (clear-teacher, dark #19ffff), rhetoric-spotter (firm-captain, light #1947ff),
  rhetorical-situation-simulator (knowing-guide, dark #ffd18c), theme-ledger (smooth-narrator, light #592439),
  argument-builder-pro (big-sister, #095909), fallacy-field-guide (gravel-ranger, khaki #5c5c08), premise-inspector
  (science-narrator, dark #cccc14), founding-words-explorer (news-reader, parchment #8c5138), thesis-workshop
  (wise-mentor, light #5b63a6), audience-shift-briefing (casual-peer, light #a61188), ad-agency (lively-host, dark
  #a3ff19).
- Family engines, each in full in one spec: kit/rhetoric.js (argument-map), kit/evidence.js (theme-ledger),
  kit/fallacies.js (fallacy-field-guide), kit/founding-docs.js (premise-inspector; no docs/families/founding-docs.md
  yet). ad-agency feeds kit/fact-check.js as fake-or-fact-lab describes it.
- For the joint review: voices repeat ela-research and ela-lit picks (firm-captain, knowing-guide, big-sister,
  gravel-ranger, news-reader, wise-mentor, casual-peer); check accents and voices across the whole wave.
- Confirm at build (only Wikipedia checked): Jefferson as an enslaver, Apess's Pequot identity, New Jersey women voting
  until 1807, the Atlantic Monthly date for Frost; founding-words-explorer context-card dates (Committee of Style,
  Farewell Address printing).

Open questions:
- [group] Show dashes from source texts as "--"?
- [argument-map] Name Madison as Federalist 51's author, or keep Avalon's "Hamilton or Madison"? 12-paragraph Thoreau
  excerpt enough, or the full essay in the drawer?
- [rhetoric-spotter] Keep Anthony's "oligarchy of race" line (A9)? Card on Henry's slaveholding fine for grade 9?
  Narrator voice for historical speakers?
- [rhetorical-situation-simulator] Keep Executive Order 9066 on the FDR card? Nez Perce reviewer for the Joseph card
  and spelling?
- [theme-ledger] "The Story of an Hour" fine at grade 9?
- [premise-inspector] Stephens' full "corner-stone" sentence or the summary? Stephens sheet right for grade 11, or
  teacher unlock? Native reviewer (ideally Pequot or Mashpee) for the Apess and X4 cards?
- [founding-words-explorer] Own glosses for today's senses, or Wiktionary? "Echoes in later speeches" moved to
  premise-inspector: OK? Add Johnson's 1755 dictionary as a second "then"?
- [thesis-workshop] Mild ghost-story fright in "The Open Window" OK at grade 10? Show the popular Frost reading as a
  chip that visibly fails?
- [audience-shift-briefing] Lock the finding in every room, or let students soften it for the class? Keep the EPA Salt
  Lake City heat-deaths card?
- [ad-agency] Letters certain at Risk 8, or add chance? Name the FTC in the letter, or keep the made-up Watchdog Desk
  citing the real rules?

### ela-craft (9, done; finished by a second agent after the pause)

- Tools: parallel-parking (9, clear-teacher, dark, lane-line yellow #f7e463), punctuation-power-ups (10, hero-coach,
  dark, magenta #ff4fd8), personal-essay-studio (11, calm-professor, light, rose #9c2a55), editors-in-the-margin (9-12,
  friendly-dad, light, red pencil #b3261e), pacing-strip (9-12, playful-friend, dark, mint #3fe0c5), word-family-tree
  (12, gravel-ranger, dark, new-leaf green #a6d84a), key-term-tracker (9-12, curious-librarian, light, amber #7a4b00),
  socratic-seminar-board (10, soft-breath, light, teal #0f6e78), speech-coach (12, easy-coach, dark, cue-light green
  #5ee07a).
- Family engine: word-lab (kit/wordlab.js) in full in word-family-tree; key-term-tracker feeds it.
- The second agent fixed voice clashes the first had missed, content errors (wrong starting answers, miscounts, a
  lumped root tree, Quarto-only Lear lines), and added activities so every module code is taught well (BASELINE
  rule 2). speech-coach has no speech-to-text, so audio never leaves the device.
- Public domain for speech-coach: Met 437878 (Vermeer, A Maid Asleep), Met 435809 (Bruegel, The Harvesters), AIC 57819
  (Wall Clock).
- Open questions for Cory: none (all settled by BASELINE.md).
