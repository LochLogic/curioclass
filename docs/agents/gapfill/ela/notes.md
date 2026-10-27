# ELA gap fill: notes

Domain: CCSS ELA (all strands, K-12) and the empty WIDA language-use cells. Checked with
`python scripts/overlap/stage_check.py docs/agents/gapfill/ela --missing`: 0 errors, 0 warnings.

## Result

| Measure | Before (all planned) | After this folder |
|---|---|---|
| CCSS ELA grade-level standards | 169 of 455 | 414 of 455 (the other 41 are by-design exclusions) |
| K-2 / 3-5 / 6-8 / 9-12 | 56 / 40 / 34 / 39 | 113 / 116 / 111 / 74 (each band's remainder is exclusions only) |
| WIDA language uses x band | 11 of 16 | 16 of 16 |

30 code lines on existing modules and 43 new modules, one new tool each: K-2 11 (10 ELA, 1 ELD), 3-5 12, 6-8 12,
9-12 7, plus 1 ELD tool for 6-12.

## Code adds to existing modules (codes.txt)

Each add is a code whose wording the tool already practices; most are a sibling of a code the module has.
- Evidence and theme: theme-tracker RL.4.1, quote-picker RI.4.1, character-face-off RL.5.2, thesis-workshop RL.9-10.1,
  character-web RL.9-10.2, satire-decoder RL.11-12.1 (spec).
- Word meaning: idiom-illustrator RL.3.4, word-thermometer RL.6.4 and RI.6.4, two-authors-one-event RI.7.4 and RI.7.6,
  founding-words-explorer RI.9-10.4, tone-dial L.9-10.5.
- Structure and summary: plot-rollercoaster RL.6.5, summary-squeeze RL.6.2, ambiguity-lab RL.11-12.3.
- Writing: dialogue-director L.3.2 (quotation marks in dialogue), fact-fusion W.5.7 and W.5.8, rhetorical-situation-simulator
  W.11-12.4 and SL.11-12.6, personal-essay-studio W.11-12.5, source-mixer W.11-12.8.
- Reading across sources: research-rover RI.4.9, fact-check-desk RI.8.8.
- Discussion: usage-panel SL.11-12.1 (its spec already said it supports it).
- Span tools in other subjects that do the work (cheap because they already span a band):
  - talk-moves-trainer (ELD 3-5): SL.3.1, SL.4.1, SL.5.1, which fills the start of the empty 3-5 speaking and listening row.
  - summary-scaffold (ELD 6-8): RI.6.2, RI.7.2, RI.8.2.
  - research-quest (library 6-8, spec): W.6.7, W.7.7, W.8.7.
  - fake-or-fact-lab (library 6-8, spec): W.6.8, W.7.8, W.8.8.
  - boolean-builder (library 9-12, spec): W.9-10.8, W.11-12.8 ("using advanced searches effectively").
- WIDA: time-machine-talk (3-5) gets WIDA.Inform (learners describe each past scene), inbox-simulator (9-12) gets
  WIDA.Inform (replies give requested information; ELD-SI covers all four language uses).

The five specced tools (satire-decoder, usage-panel, research-quest, fake-or-fact-lab, boolean-builder) had their
Standards line extended to match.

I did not put another grade's code on a single-grade module, even where the tool is grade-free (for example RF.1.1 on
sentence-train, grade K, or RL.5.5 on story-building-blocks, grade 3). Those codes went to band-span modules instead.

## New modules (modules.txt, concepts.txt, tags.csv)

Most are band spans with a grade switch and one skill, about three codes per grade.

- **K-2:**
  - Windblown Pages: pictures, captions and text features against the words; who made each part.
  - Alike and Different Books: two texts or two versions of a tale; a story book against a fact book.
  - Question Cube: who, what, where, when, why and how; key details and connections.
  - Because Bridge: an author's reasons, with because (L.1.6).
  - Poem Drum: poems against stories, rhythm and feeling words, reading a poem aloud and recording it.
  - Vocabulary Jar: new words from read-alouds.
  - Big Question Chart: shared research (W.7, W.8).
  - Puppet Wants More: revising by adding details, plus RF.1.1 sentence features.
  - Show and Tell Spotlight: SL.4 to SL.6 and L.2.3 formal against informal.
  - Class Phone Call: SL.1 to SL.3.
  - I Choose Because (ELD): Argue.
- **3-5:**
  - Draft Car Wash: W.4, W.5 and L.2/L.3 (revising and editing).
  - Radio Hour Notes: SL.2 and SL.3.
  - Planetarium Guide: SL.4 to SL.6.
  - Script Read-Through: RF.3 and RF.4 in grades 3 to 5.
  - Main Idea Pinboard: main idea or central message with text evidence (RL/RI.1, RL/RI.2, RI.4.8, W.5.9).
  - Glossary Makers: academic and subject words (RI.4, L.4 to L.6).
  - Mood in the Pictures: RL.7.
  - How It Works Diagrams: RI.7 and RI.3.
  - Swap the Teller: RL.6 and RI.3.6.
  - Side by Side Reader: RL/RI.9 and the grade 5 structure codes.
  - Show, Don't Tell: grade 4, RL.4.3 with W.4.3.
  - Note Card Shuffle: grade 3, W.3.7 and W.3.8.
- **6-8:**
  - Draft Versus Draft: W.4, W.5, L.7.3.
  - Theme Evidence Ladder: RL.1, RL.2, RL.6.9.
  - Claim, Quote, Comment: RI.1 with W.9.
  - Page, Audio, Screen: RL.7 and RI.7.
  - Podcast Listening Club: SL.1 to SL.3.
  - Docent Tour Talk: SL.4 to SL.6.
  - Context, Roots, Dictionary: L.4 and L.6.
  - Double Meanings: grade 8, RL.8.4, RI.8.4, L.8.5.
  - Pause and Break: L.2.
  - Explainer Sections: W.2 with RI.5.
  - Blizzard Scenes: W.3 with RL.7.6 and RL.8.5.
  - Memoir and Biography: RI.3, RI.6, RI.6.9.
  - Then What Happened? (ELD, 6-12): Narrate.
- **9-12:**
  - Editors in the Margin: W.4, W.5, L.11-12.2, L.11-12.3.
  - Theme Ledger: RL.1, RL.2, W.9.
  - Idea Threads: RI.1 to RI.3 and RI.9-10.5.
  - Portrait in Four Media: grade 10, RI.9-10.7 and SL.9-10.2.
  - Audience Shift Briefing: grade 9, SL.9-10.4 to SL.9-10.6.
  - Key Term Tracker: L.4, L.6, RL/RI.11-12.4.
  - Pacing Strip: W.3.

Some span modules repeat a code another tool already has (RI.K.1, SL.K.3, SL.K.4, RF.1.4, RI.3.3, RL.4.9, RI.4.9,
RL.6.2, W.7.2, W.8.3, W.11-12.5). That keeps a code for every grade the module spans, as the brief asks.

## Left out by design (41 codes)

- **RL.x.10 and RI.x.10, all grades (22):** "read and comprehend a range of texts at grade level". This is the whole reading
  diet across a year, not a skill one short tool can practice or show.
- **W.x.10, grades 3 to 12 (8):** "write routinely over extended and shorter time frames". This is a habit of the
  writing program, not a tool skill. K-2 has no W.10 on the official list.
- **W.x.6, all grades (11):** "use technology, including the Internet, to produce and publish writing". Every writing
  tool on the site is digital, so tagging one would be an empty claim and tagging all would be noise. The real skills
  inside it (keyboarding, collaborating online, linking sources) belong to CS and library tools.

## Judgment calls and warnings

- The checker shows no warnings now. Four clashes on the first run were fixed by reshaping my own tools:
  - The picture-flap tool became Windblown Pages (match, weather), apart from meet-the-book-makers.
  - Show and Tell moved off the stage setting (act-it-out).
  - The narrative scene became a blizzard trip, not a home (blueprint-studio).
  - Quote Sandwich became Claim, Quote, Comment (cooler-challenge, kitchen-food).
  - I also renamed Editor's Margin, because a possessive counts as the overused title word "s".
  - Run with every gapfill folder, Page, Audio, Screen clashed with another folder's panel-of-experts (6-8, compare and
    film-media), and 6-8 film-media reached 6 tools. It now has a book-club world (library). Swap the Teller was
    renamed from Who Tells the Tale, because "who" reached 5 title uses.
- Close skills in the same band that the rule does not flag, kept on purpose:
  - Main Idea Pinboard sits beside headline-writer (main idea) and quote-picker and inference-interrogation (quoting).
    It is the only 3-5 tool for grade 3 evidence and for informational evidence in grade 5.
  - Audience Shift Briefing (grade 9, presenting findings with media) is near rhetorical-situation-simulator (grade 11,
    rhetorical choices in a speech). If they feel too alike at spec time, give the briefing a fixed audience and make
    the media choice the main variable.
  - Show, Don't Tell (grade 4) and Note Card Shuffle (grade 3) are single-grade modules. Their sibling grades are
    already covered by character-choice-story and slow-mo-writer, and by research-rover and fact-fusion.
- **Checker limit:** coverage.py's grade_bands() raises on grade `9-10` or `11-12`, even though the brief allows those
  spans. So the two 9-10 modules use grades 10 and 9, the same way existing modules carry 9-10 codes. If 9-10 spans
  should work, coverage.py needs `'9-10'` and `'11-12'` in GRADE_BAND.
- **CCSS on ELD and library modules:** five code lines put ELA codes on ELD or library modules (talk-moves-trainer,
  summary-scaffold, research-quest, fake-or-fact-lab, boolean-builder). These tools already do the work and span a band.
  When the merge rebuilds frameworks, the merger should check that those modules list CCSS-ELA.

## fact-check-desk (ELA 8, planned): reshape idea

It clashes with misleading-charts (6-8 CS) because both are a newspaper fact-check desk. I added no newspaper or
fact-check world in 6-8, and I did not change its concept. RI.8.8 now sits on its module beside RI.8.9.

Reshape idea for when it is specced: **almanac editors**. The class edits a town almanac or record book, and two
sources disagree about one entry (the year the bridge opened, who set the school's mile record). Students trace each
claim to its evidence and rule which version prints, with a footnote naming the weaker source. The skill stays the
same (conflicting sources), the fact-check family engine still fits, and the world moves from newsroom to a reference
book. 6-8 has one library or book tool, so it is not crowded. The title would change from Fact Check Desk to something
like Almanac Dispute.

## Questions for Cory

1. Are you OK leaving RL.10, RI.10, W.10 and W.6 out by design (41 codes)?
2. Are you OK with ELA codes on five ELD and library tools (listed above)? The alternative is new ELA tools, which
   would cost about three more.
3. Several planned single-grade ELA modules teach a skill that is the same across their band, for example echo-reader
   (1), text-feature-makeover (1), sentence-train (K), story-building-blocks (3) and socratic-seminar-board (10).
   Widening them to band spans would be tidier, but it is not needed for coverage now. Do you want that done later?
