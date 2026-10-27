# Curio Class overlap pass: method

## Tagging

- **Rows:** all 586 rows of data/tools-concepts.csv, read one by one. A tool counts as live when tools/<id>/tool.json exists (76). For live tools, and for the five with a spec but no tool yet (circuit-builder, satire-decoder, sound-studio, stock-market-1929, usage-panel), I tagged from the spec and tool.json rather than the one-line concept.
- **Band:** grades k, 1, 2 and k-2 are K-2; 3, 4, 5 and 3-5 are 3-5; 6, 7, 8 and 6-8 are 6-8; 9 to 12 and 9-12 are 9-12. A K-12 tool counts against all four bands and a 6-12 tool against 6-8 and 9-12.
- **Format and family:** copied from the CSV.
- **Skill:** a short key for the specific skill (for example `counterclaims`, `fractions-number-line`) plus a plain-language line. Two tools share a skill when a teacher would say they teach the same thing at that grade, not just the same topic. Sets of keys were coarsened where the first-pass keys hid real overlaps (six in the first draft, more in the revision below):
  - class-poll and class-snack-vote to `class-data`
  - debate-prep-desk to `counterclaims` (its concept ends in counterargument practice)
  - boundaries-builder to `conflict-resolution`
  - move-like-me to `locomotor-skills`
  - pattern-finder and teach-the-robot to `ai-patterns`
  - compound-interest-garden and savings-plan to `savings-growth`
- **Action:** what the student or class does most of the time, from a fixed list of 31: count-along, move-along, predict-reveal, sort, match, order, build, compose, manipulate, simulate-tune, experiment, explore, hunt, solve, fix, investigate, annotate, drill, choose-path, debate, converse, manage, care-for, analyze-data, locate, discuss, rehearse, trace, plan, program, compare. Build means assembling a structure from parts; compose means making an open-ended creative product; simulate-tune means setting parameters and watching a model run; experiment means a fair test with one variable changed.
- **Setting:** the metaphor or world, written as a detail (for example "passport stamps") plus a coarse group used for matching (in brackets in tags.csv). Raw groups were merged when a student would see the same kind of place: shop, food service and bakery are `shop-food`; kitchen and food are `kitchen-food`; garden and farm; zoo, animals and safari; council and debate; film, camera, recording and radio; newsroom and poster; ocean and river are `water`; travel map, travel and trail; vehicle, train and race; casino and game show; treasure and vault; fantasy, maze and fortress; body and hospital; town and playground; construction and repair shop; business and bank; nature and dig; security, network and code are `cyber`.
- **Generic settings** never count as a match: plain (no metaphor), real (real data, photos or sources), school, cards and game.

## The clash rule

For every pair of tools that share at least one band, count the matches among:

1. skill key equal,
2. action equal,
3. coarse setting group equal and not generic.

Two or more matches in the same band is a clash. After the revision's tag fixes that produces 152 pairs (pairs.csv), which I grouped into clusters by shared tool and shared picture.

Across bands, the same skill is a spiral and is fine. I also checked for cross-band pairs where all three tags match (same skill, action and setting one band apart): there were none, though polynomial-garden and expression-garden come close (C29).

On top of the rule I flagged:

- the same setting used 4 or more times in a band, or the same specific picture twice (an elevator, a safari, a passport) even when only one tag matched,
- near-identical titles in a band and title words used 5 or more times,
- titles using a trademark or a well-known product name,
- skill-only matches where a planned tool covers a live tool's whole skill.

Each cluster was then judged by hand. 152 rule hits became 58 clusters plus three wave 1 notes (W1 to W3). After the fixes the rule finds 92 pairs (pairs-after.csv); C57 lists every one with the reason it is kept.

## Fixes

- **Live tools never move.** In a clash between a live and a planned tool, the planned tool changes.
- **Reshape** is the default: a new concept line inside the same module and standards, written in the existing style.
- **Merge** is offered only as an alternative. Each module maps to exactly one tool today, so merging needs a tool that serves two modules.
- **Move-to-gap** needs a planned tool whose module standards are all covered by other tools in the same band, so the move opens nothing new. I checked this from data/modules.csv for each candidate. It is rare: CS, ELA and most science modules carry standards no other module does. The CSTA 2026 grade-level codes (for example E1-ALG-PS-01 on bee-bot-garden) are a reason several planned tools could not move.

## What I was unsure about

- **Coarse setting groups** are a judgment call. Merging town with playground and nature with dig catches real repeats, but also raises a few false hits that I kept in C57.
- **Skill keys** for broad modules: one module can cover three skills, and I keyed the one the concept leads with. A different reader might key source-sorter on citation rather than credibility.
- **CSTA sub-codes:** the 111 uncovered identifiers in G3 come from the code prefixes in data/modules.csv. I did not check every sub-code's wording in CSTA 2026, so some may be covered in substance by a sibling code.
- **Trademark risk** is a plain reading of well-known marks (Mad Libs, Jenga, Battleship, Rube Goldberg, Monopoly, Bee-Bot, Power Grid), not legal advice. The low-risk list in C58 is a caution only.
- **Open calls** are listed at the top of clusters.md and in the options column of the decision table.
- **Helper scripts** are in scripts/overlap/ (see Revision).

## Revision

A cold check (check.md) returned "ready with fixes". This revision answers it.

- **Tags:** 10 tags corrected (pizza-party, pattern-finder, two-sides-theater, flowchart-factory, debate-prep-desk, story-problem-theater, asl-story-theater, clock-shop, art-passport, elevator-hundred). tags.csv is now the master file and carries the matched `skill_key` column, so the rule can be re-run from it. More keys were merged where a teacher would call the skill the same: `hardware-parts` (computer-builder, input-output-machine), `study-design` (poll-workshop, design-the-study), `community-project`, `quote-evidence`, `fossils-rock-layers`, `train-classifier`, `founding-documents`, `staging-interpretation`, `polynomial-area-model` and `combining-sentences`.
- **Rule:** re-run on the corrected tags: 152 hits before the fixes, 92 after. Every after-hit has a written reason in C57; none is unexplained.
- **Fixes:** every new concept line was re-checked against its band (live and planned) with `rule.py --after`, and against its module's standards. Counts: 62 reshape, 17 rename (title only), 1 add-standard, 7 keep with a spec note, 4 keep. That is 79 changed tools, about 15 percent of the 510 planned. Merge and move-to-gap are recommended nowhere; three move-to-gap and one merge are offered as options.
- **Versus the first draft:**
  - The five fixes that made new clashes were redone: C16 Bead Slider, C13 Crayon Boxes, the secret-keeper reshape dropped (C22), courtroom-statistics kept and its open call closed (C30), and Covered became a premium versus deductible comparison (C43). The other weak fixes the checker named were reworked (C25, C26, C34, C36, C39 and others).
  - New clusters cover the missed clashes, including the three with live tools (C03, C04, C05), the other strong pairs and the four 9-12 mysteries (C32).
  - False clashes were dropped or downgraded: plot-rollercoaster, theory-gym and logic-gym, and the voice-switcher reshape (now keep, with an option).
  - The first draft's population-dashboard move ("Carbon Relay") became an option elsewhere; HS-LS2-5 now goes on energy-accountant's module (W3).
  - Wave 1 neighbors got a "decide before specs" section (W1 to W3) and joined the first-look list with the live-tool clashes.
  - clusters.md opens with a one-row-per-tool decision table; decisions.json holds the same rows for tooling.
  - gaps.md: SOC wording corrected (K-5 patchy, MS 1 of 8, HS 0 of 9); DAT-DC and PRO-PD added; fluency gaps at K and grades 2 to 5; 9-12 geography reworded to "no geography course", since D2.Geo codes sit on five history modules; counts note that band totals include K-12 and 6-12 tools.
- **Scripts** (in scripts/overlap/, each with a usage line at the top; run from the repo root):
  - `python scripts/overlap/rule.py` writes pairs.csv; `--after` applies the fixes and writes pairs-after.csv.
  - `python scripts/overlap/stats.py [--after]` prints loads by band, rare formats and title collisions.
  - `python scripts/overlap/standards.py` prints the NGSS, CSTA, fluency and geography coverage behind gaps.md.
  - `python scripts/overlap/build_decisions.py` writes decisions.json and fills the decision table, the per-cluster fix lists and the C57 kept hits in clusters.md (idempotent).
  - decisions_src.py holds every decision and its after-tags; clusters_meta.py holds cluster titles and kept-hit reasons; common.py is the shared loader and rule.
