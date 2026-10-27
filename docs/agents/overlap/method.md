# Curio Class overlap pass: method

## Tagging

- **Rows:** all 586 rows of data/tools-concepts.csv, read one by one. A tool counts as live when tools/<id>/tool.json exists (76). For live tools, and for the five with a spec but no tool yet (circuit-builder, satire-decoder, sound-studio, stock-market-1929, usage-panel), I tagged from the spec and tool.json rather than the one-line concept.
- **Band:** grades k, 1, 2 and k-2 are K-2; 3, 4, 5 and 3-5 are 3-5; 6, 7, 8 and 6-8 are 6-8; 9 to 12 and 9-12 are 9-12. A K-12 tool counts against all four bands and a 6-12 tool against 6-8 and 9-12.
- **Format and family:** copied from the CSV.
- **Skill:** a short key for the specific skill (for example `counterclaims`, `fractions-number-line`) plus a plain-language line. Two tools share a skill when a teacher would say they teach the same thing at that grade, not just the same topic. Six sets of keys were coarsened after a first pass, because the first-pass keys hid real overlaps:
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

Two or more matches in the same band is a clash. That produced 150 pairs, which I grouped into clusters by shared tool and shared picture.

Across bands, the same skill is a spiral and is fine. I also checked for cross-band pairs where all three tags match (same skill, action and setting one band apart): there were none, though polynomial-garden and expression-garden come close (C39).

On top of the rule I flagged:

- the same setting used 4 or more times in a band, or the same specific picture twice (an elevator, a safari, a passport) even when only one tag matched,
- near-identical titles in a band and title words used 5 or more times,
- titles using a trademark or a well-known product name,
- skill-only matches where a planned tool covers a live tool's whole skill.

Each cluster was then judged by hand. 150 rule hits became 45 clusters; C44 lists the rule hits I kept and why.

## Fixes

- **Live tools never move.** In a clash between a live and a planned tool, the planned tool changes.
- **Reshape** is the default: a new concept line inside the same module and standards, written in the existing style.
- **Merge** is offered only as an alternative. Each module maps to exactly one tool today, so merging needs a tool that serves two modules.
- **Move-to-gap** needs a planned tool whose module standards are all covered by other tools in the same band, so the move opens nothing new. I checked this from data/modules.csv for each candidate. It is rare: CS, ELA and most science modules carry standards no other module does. The CSTA 2026 grade-level codes (for example E1-ALG-PS-01 on bee-bot-garden) are a reason several planned tools could not move.

## What I was unsure about

- **Coarse setting groups** are a judgment call. Merging town with playground and nature with dig catches real repeats, but also raises a few false hits that I kept in C44.
- **Skill keys** for broad modules: one module can cover three skills, and I keyed the one the concept leads with. A different reader might key source-sorter on citation rather than credibility.
- **CSTA sub-codes:** the 111 uncovered identifiers in G3 come from the code prefixes in data/modules.csv. I did not check every sub-code's wording in CSTA 2026, so some may be covered in substance by a sibling code.
- **Trademark risk** is a plain reading of well-known marks (Mad Libs, Jenga, Battleship, Rube Goldberg, Monopoly, Bee-Bot, Power Grid), not legal advice. The low-risk list in C45 is a caution only.
- **Open calls** are listed at the top of clusters.md: courtroom-statistics, retell-puppets, bundle-bakery, population-dashboard, ph-detective, boundaries-builder and the wave 1 timing for festival-passport.
- **Helper scripts** (loader, clash finder, stats, standards checks) are in the session scratchpad, not in the repo.
