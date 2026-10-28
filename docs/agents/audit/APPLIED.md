# Curio Class overlap and gap audit: apply record

Applied 2026-10-27 from gaps.md, clashes-k8.md and clashes-9-12.md, with the repo's scripts (add_codes.py, build_db.py,
rename_tools.py, check_concepts.py --write). Module ids are unchanged everywhere: a module id is grade plus title, and
Word Wall cards key on it.

## Clash fixes

- 14 reshapes in data/concepts: 11 from clashes-k8.md and 3 from clashes-9-12.md (build-a-government; lake-commons and
  startup-booth synced to their specs, format tycoon kept).
- 6 renames through rename_tools.py: story-problem-theater -> story-replay, pattern-block-pond -> pattern-block-windows,
  elevator-hundred -> bead-slider, shape-courtroom -> shape-sieve, dance-floor-moves -> transformation-dock,
  fact-check-desk -> bike-lane-briefing (folders moved, renamed.json and tags.csv updated).
- tags.csv: 14 tag corrections (2 from K-8, 12 from 9-12), after-tags for the 11 K-8 reshapes, and the decisions_src.py
  after-tags for 10 more specced tools whose rows were stale (input-or-output, levels-and-pathways, me-vs-the-counter,
  spot-the-ai, director-s-chair, premise-inspector, founding-words-explorer, network-help-desk, keyword-fishing,
  conic-focus-finder). Where a clash file corrected a specced tool, its correction won over decisions_src.py
  (compound-interest-head-start, curling-stones, rigid-motion-twins, lake-commons). Title, format and family synced from
  the catalog. 35 new rows for the new tools.
- The 12 reshaped idea cards carry the applied title and concept line.

## Gaps

- Code moves: 46 module edits through add_codes.py (23 moves to existing tools, 3 dropped codes, the whole-code moves to
  new tools, WRS.Connections on world-languages-9-12-current-events-and-debate, D2.Geo.11.3-5 on
  social-studies-4-state-economy-and-resources). Part moves add the code to the target and leave it on the source.
- New tools: 35 module lines and 35 concept lines (27 from moves, 8 for W.6, W.10, RL.10 and RI.10, reversing the gap
  fill's exclusion under BASELINE rule 2). Front Line has no family until a shared engine with the weather tools is
  confirmed. Each has a short tools/<id>/idea.md in the IDEA-PASS.md template.
- Catalog fixes: 15 one-tool families dropped; 10 module descriptions updated after the moves.
- Idea cards: syllable-surgeon (root-family ward), script-read-through (register round now core and solo),
  letter-lanterns (tracing now core), bill-to-law-board-game (federal-vs-state card), settle-the-valley,
  pen-pal-parcels and playground-rules (incoming codes now standing lines).

## Not applied (and why)

- Module title changes (Bike Fund Chances, Behind the Documentary, Voices on the Vote, and the 9 trims in gaps.md
  catalog fix 4) and grade changes (ela-1-text-features to 1-2, ela-3-literal-and-figurative-language to 3-4): each
  would change the module id, and all of these modules have Word Wall cards. They need a way to pin an id in
  build_db.py first. The codes and descriptions were applied.
- coordinate-proof-lab trapezoid default: not a one-line edit. The spec sets "exclusive" in five places (name board,
  P3 and P5 checks, the API default at lines 154-155, the definition at line 98, open question at 193-194).
- shape-family-tree teacher note on the site's trapezoid definition: not in scope of this pass; for its spec.

## Checks

- coverage.py: every "all" column full; CCSS-ELA 455/455, CSTA 196/196, NGSS 208/208, CCSS-Math 147/147, C3 283/283.
- rule.py: 114 hits (K-2 18, 3-5 19, 6-8 24, 9-12 52, cross-band 1). 102 are kept with a reason in the clash files.
  12 are not judged there: 11 involve a new tool and 1 comes from two fixes meeting (listed below).
- check_codes.py: 0 invalid codes. check_words.py: 0 problems. check_concepts.py: 797 concepts, 797/797 modules,
  no errors or streaks. check_site.py not run (it needs a site build).

### Rule hits not judged by the clash files

| band | pair | match | first read |
|---|---|---|---|
| 3-5 | fraction-kitchen and camp-cook-share-out | solve, kitchen-food | real risk: two grade 5 fraction kitchens; reshape Camp Cook before spec |
| 3-5 | class-pet-pitch, headline-writer and deadline-desk | compose, newsroom | third newsroom look in 3-5; skills differ (opinion, headlines, keyboarding) |
| 3-5 | erosion-table, leaf-sorter-ai and star-lanterns | experiment, nature | broad setting, different skills |
| 3-5 | research-rover and stretch-shelf | explore, library | different skills |
| 6-8 | expression-garden and flower-lure | build, garden-farm | different subjects |
| 6-8 | levers-of-power and town-footprint | simulate-tune, town | different skills |
| K-2 | computer-builder (live) and picky-robot-shapes | build, robot-machine | different subjects |
| K-2 | library-adventure (live) and read-along-shelf | explore, library | library layout against reading range |
| K-2 | me-vs-the-counter and puppet-show-feelings | experiment, toys | from the spec after-tag meeting the K05 reshape; different subjects |
| cross-band | read-along-shelf and stretch-shelf | all three | the range tools are one per band by design (a spiral); a shared family tag would say so |

Also worth a judge's look though below the bar: little-book-press is a third K-2 book maker (with many-voices-book and
sound-and-picture-book; tagged with a press setting).
