# Social gap fill: notes (2026-10-27)

Domain: C3 (all four dimensions), NSPFE personal finance, AASL (library). Checker:
`python scripts/overlap/stage_check.py docs/agents/gapfill/social --missing` gives 0 ERROR and 0 warn lines (Question Kite and Question Ladder were renamed Wonder Kite and Inquiry Ladder once the ela and cs folders pushed "question" to 5 title uses).

Every code was matched against the official wording. The C3 wording was read from the official NCSS PDF named in
`data/standards/c3-indicators.txt` (text pulled out locally, not stored in the repo). NSPFE and AASL are coded at the
level modules.csv already uses (`NSPFE.<Topic>`, `AASL.<Foundation>`), which is what coverage measures.

## Coverage after this folder (all planned)

| Framework | Before | After |
|---|---|---|
| C3 indicators | 116 of 283 | 283 of 283 (K-2 63/63, 3-5 72/72, 6-8 73/73, 9-12 75/75) |
| NSPFE topic x band | 6 of 18 | 18 of 18 |
| AASL foundation x band | 13 of 24 | 24 of 24 |

Live + specced C3 moves from 12 to 17 because three specced library tools (research-quest, fake-or-fact-lab) and two
live tools (wonder-wall, concert-ticket-market) now carry codes they already teach.

## 1. Codes added to existing modules (codes.txt, 33 lines)

Each line names the tool and what it already does. Highlights:

- **Inquiry arc on tools that already do it:** wonder-wall (D1.5.K-2, sorting questions by source type),
  research-quest (D1.5.6-8, D3.1.6-8), fake-or-fact-lab (D3.2.6-8), debate-prep-desk (D3.4.6-8, D4.1.6-8),
  who-decides (D4.3.9-12, D4.7.9-12), empire-debate (D2.His.16.9-12, D4.1.9-12), supreme-court-simulator (D3.4.9-12).
- **Civics:** playground-rules, town-council, class-election, bill-to-law-board-game, rights-match,
  paper-plane-assembly-line, agora-assembly, two-parties, constitutional-convention, reconstruction-amendments,
  movement-strategy-room, muckraker-studio.
- **Economics and geography:** community-helpers-village (government services), concert-ticket-market (its $75 price
  cap scenario), the-buyout (regulators), settle-the-valley, colonial-trade-routes, region-compare, climate-postcards.
- **History:** revolution-road (three viewpoints), then-and-now-overlay, colonial-newsroom (Patriot vs Loyalist spin).
- **NSPFE (as the brief asked):** grocery-run gets NSPFE.Spending (3-5), lemonade-stand gets NSPFE.Earning Income (6-8).
- **AASL:** secret-keeper gets AASL.Engage (K-2, safe sharing), question-sharpener gets AASL.Inquire (9-12).
- **Specs updated** (`- Standards` line, as the brief allows): secret-keeper, research-quest, fake-or-fact-lab.

Judgment calls a reviewer may want to check:
- D2.Geo.10.3-5 on climate-postcards: the indicator says "explain why environmental characteristics vary among world
  regions"; the tool compares real climates city by city, so the "why" (latitude, oceans, height) has to be in its spec.
  It is the only 3-5 tool that compares world climates, so this was better than a new tool for one code.
- D4.1.K-2 on playground-rules: the class votes on rules "and why", an argument with reasons at K-2 level.
- AASL.Engage on secret-keeper rather than meet-the-book-makers: safe sharing fits Engage more clearly than knowing
  who wrote and who drew a book.

## 2. New modules (51 tools)

| Band | Count | Tools |
|---|---|---|
| K-2 | 8 | Wonder Kite, How Do You Know?, Teddy Bear Makers, Storm Helpers, Pen Pal Parcels, Capsule From 1965, The Last Carousel Ride, Many Voices Book (library) |
| 3-5 | 15 | Inquiry Ladder, Source Scout, Made for Whom?, Why the Pony Express Ended, History Article Review, School Fix-It Meeting, Tools for Change, Pool Repair Vote, Ripple Street, Barter Bay, Learn and Earn, Interest Seesaw, Bike Fund Chances, Cocoa Chain, Windows and Mirrors Shelf (library) |
| 6-8 | 18 | Panel of Experts, Rabbit Hole Notebook (library), Historians Disagree, Evidence Corkboard, Unlabeled Archive, Voices on the Vote, Museum Label Writer, Levers of Power, Motion on the Floor, Shaping Our Week, Smoke and Honey, Border Trade Post, Snow Season Prices, Economy Checkup, Interest Rate Dial, Startup Shares, E-Bike Buyer, The Shrinking Lake |
| 9-12 | 10 | Enduring Questions (library), Source Portfolio (library), Missing Voices Archive, Behind the Documentary, Claim Repair Shop, Causes Web, Jury Room, Layers and Scales, Suburb Boom, Climate on the Move |

How they were grouped:
- **One inquiry skill per tool, spiralling by band.** Questions (Wonder Kite, Inquiry Ladder, Panel of Experts,
  Enduring Questions), sources (How Do You Know?, Source Scout, Source Portfolio), historical sources (Capsule From 1965, Made
  for Whom?, Unlabeled Archive, Missing Voices Archive), claims and critique (Why the Pony Express Ended, History Article
  Review, Evidence Corkboard, Historians Disagree, Behind the Documentary, Claim Repair Shop), explanations (Teddy Bear
  Makers, Cocoa Chain, Museum Label Writer, Causes Web) and action (Storm Helpers, Tools for Change, Levers of Power).
  Each sits in a history, civics, economics or geography world, so the D1, D3 and D4 codes ride on real content.
- **Economics and finance combined where one tool honestly does both:** Learn and Earn (human capital + Earning
  Income), Interest Seesaw and Interest Rate Dial (interest rates + Saving + Managing Credit), Startup Shares (innovation
  + Investing). Bike Fund Chances (3-5) and E-Bike Buyer (6-8) pair a finance topic with Managing Risk.
- **Courses:** K-5 in ss-k5. Middle school has no economics or civics course, so the 6-8 finance and market tools
  (Snow Season Prices, Economy Checkup, Interest Rate Dial, Startup Shares, E-Bike Buyer) are cte-explore 6-8 modules,
  the 6-8 civics tools are us-hist-8 Civics modules, and the trade and externality tools are world-geo-6. High school
  geography tools sit in world-hist-hs and us-hist-hs (there is no 9-12 geography course; existing D2.Geo codes already
  sit on history modules). New strand names: Inquiry (social-studies), Community and Reading (library), Economics and
  Personal Finance (cte-explore).
- **Crowded settings avoided:** no new tool in 9-12 council and debate or business and money, none in the 6-8 travel
  map, none in K-2 town, robot or machine, none in 3-5 nature. Titles avoid every word used 5 or more times.

Modules with four codes (the brief says "about three"): Wonder Kite, Teddy Bear Makers, Storm Helpers, Capsule From 1965,
Inquiry Ladder, Why the Pony Express Ended, School Fix-It Meeting, Tools for Change, Interest Seesaw, Cocoa Chain,
Enduring Questions, Source Portfolio. In each, the four are one connected skill at one band (C3 indicators are written
per band, not per grade), or the fourth is a library or finance code naming the same activity. Each could drop its
fourth code to a sibling if Cory prefers a strict three.

## 3. Warnings

The first run raised four clashes, two crowded settings and five title words. All were fixed, none kept:
- Shaping Our Week (was explore + home, like mi-casa) now predict-reveal; Evidence Corkboard (investigate + detective,
  like detective-del-pasado) now a generic real-source setting; the pool tool (choose-path + water, like ship-s-log) now
  debate; Rabbit Hole Notebook (explore + library, like house-of-wisdom) now trace.
- Ripple Street moved from town (3-5, 6 tools) to home; Suburb Boom from town (9-12) to a real aerial-photo setting.
- Titles with "or" (7 uses) and "who" (5 uses) renamed: How Do You Know?, Bike Fund Chances, Made for Whom?, Pool Repair
  Vote, Shaping Our Week.

## 4. Left out by design

Nothing on the three official lists is left uncovered. Outside the lists, not coded on purpose:
- NSPFE learning outcomes (379, `NSPFE.<Topic>.<grade>-<n><letter>`): modules use topic codes, as the existing finance
  modules do; finer coding is a later pass if Cory wants it.
- AASL competencies (68, `AASL.I.A.1`): same reason; specs name competencies in prose.
- C3 companion appendices (psychology, sociology, religious studies) are not in the official list.

## 5. Questions for Cory

1. **Size.** 51 new tools close every C3, NSPFE and AASL cell. If that is too many, the cheapest cuts are the
   single-topic ones (Barter Bay, Unlabeled Archive, The Shrinking Lake, Economy Checkup); each would leave two codes
   uncovered unless folded into a neighbor.
2. **A middle school economics and civics home.** Five finance and market tools are in cte-explore (Career
   Exploration) and three civics tools are us-hist-8 modules with present-day content. Is that fine, or add a 6-8
   civics and economics course?
3. **Cross-subject codes.** C3, NSPFE and AASL codes now sit on six modules in other subjects (debate-prep-desk,
   question-sharpener, grocery-run, lemonade-stand, climate-postcards, secret-keeper). Keep, or keep these frameworks on
   social, library and finance modules only?
4. **Sensitive content, for the spec writer:** Made for Whom? (a railroad poster selling land taken from Native
   nations; include their view), Voices on the Vote (exclusion of women and Black men), Missing Voices Archive (whose
   records were kept in 1918), Cocoa Chain (child labor on cocoa farms is real: mention it, or keep the drought story
   only?).
5. **Finance at K-2.** NSPFE has no K-2 band, so piggy-bank-planner stays C3-only. Fine?
