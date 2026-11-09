# Recess: the third shape

Roadmap Track 9. Research: docs/agents/research/GAMES-RESEARCH.md (25 concepts, scores, sources). Name, tone and
rules decided with Cory, 2026-11-07.

## What Recess is

A treat. When kids are fully done, they go to Recess and play. The games are mentally stimulating with educational
undertones, but kids never feel they are still in class. Recess is also for home: kids can come on their own, so
there are no gates or passes; watching them is the parent's or teacher's call.

| Shape | What it is | Score or finish? |
|---|---|---|
| Tool | A lesson shaped around a standard | Often a goal |
| Curiosity | An instrument shaped around a real thing; the standard is a side effect | No score, no finish (light touch, rule 19) |
| Recess game | A real game where the thinking is the fun | Yes: levels, stars, best scores |

Original games only. A genre's mechanic (match-3, untangle, Sokoban, tower defense, programming puzzles) is fine; a
specific game's name, characters, art or levels never are.

## Design rules

**The fun comes first**
- The thinking is the fun. A Recess game makes kids plan, spot patterns, reason about space or look ahead. Any game
  that does that ties to a standard somehow, even loosely; whether a game earns its place is a judgment call per
  game, made at spec time (Cory: no bad idea seen yet).
- No class on the screen: no standard codes, no lesson words, no "show the math" cards. What is going on underneath
  goes in a teacher and parent note (`notes.md` and the tool page's teacher side), never in the game.
- Its own look: playful and bright, not the classroom tools' look.
- Timed modes are welcome. Action games are a judgment call per spec: they stay as long as the action asks for
  thinking, not reflexes alone.
- Some luck is fine (shuffled boards, a daily puzzle); nothing that works like gambling.

**Everyone is welcome**
- Every game is open to everyone. Grade bands are shown, not enforced: a color band or border on each game's card
  (K-2, 3-5, 6-8, 9-12). A kindergartner can try a 12th grade game; a 12th grader can enjoy a kinder game, no
  judgment.

**Rewards without accounts**
- Everything saves on the device only (local storage); nothing leaves it.
- Stars per level and a personal best per game.
- A shared machine is normal (a family PC, a classroom laptop cart), so each game keeps a small local best-scores
  board, arcade style, with 3-letter initials (never a name).
- No coins, shops, loot, lives, streak guilt or slot-machine hooks.

**Kind to kids**
- No ads, no accounts, no data collection.
- Undo and instant restart; a fail shows what was off, kindly.
- Short sessions (30 to 90 second levels, 15 to 30 hand-made levels, then endless or daily).
- Sound one tap away; honor reduced motion; Chromebook and phone friendly.

## What the research says (short)

- When the thinking is the core move, children learn more and choose to play far longer than when a quiz sits between
  moves (Habgood and Ainsworth 2011).
- Side rewards off the main path made more players quit (Refraction), which is why rewards stay on the play itself
  (stars, best scores), never a separate economy.
- Short levels, instant feedback and progress saved without accounts suit both classrooms and home.

## First games (from the research pass; to revisit under the Recess tone)

1. **Fraction Splitter** (grades 3-6): split a water flow into halves and thirds so each garden gets an exact share.
2. **Factor Crusher** (grades 4-7): numbers drop in; break each into a factor pair; primes shatter.
3. **Number Line Launcher** (grades 2-8): land a probe exactly on a fraction, decimal, percent or negative.
4. **Robot Route** (grades K-8): queue commands, loops and functions for a robot to run.
5. **Graph Shaper** (grades 8-11): set slope and intercept, later parabola values, to route a marble through rings.
6. **Bond Builder** (grades 7-10): join atoms until every bonding slot is filled.

Back in under the new rules: **Untangle** (spatial reasoning, graph theory underneath) and sliding-block puzzles
(planning ahead). Runners-up: Dial Lock, Balance Box, Logic Gates. Still out: deck building (draws feel like
gambling).

For the future (Cory, 2026-11-07): **Go**, **Chess** and **Checkers**. Classic public domain board games, so the
rules are free to use; the art, boards and puzzles stay our own. Look-ahead planning is the thinking; likely shapes
are play against the computer at a few levels, pass-and-play on one device, and short puzzles (capture in two, mate
in one). Not yet specced.

## The first collection (Cory, 2026-11-08)

Five games launch together so the shelf looks full on day one: Go, Chess, Checkers, Sliding blocks (Cargo Hold) and
Untangle. Each is its own physical world; only the shell is shared. Classic rules, our own art, boards and levels.

| Game | World | The grab |
|---|---|---|
| Go | Ink and stone: slate and shell stones on a warm wood board | Stones click down; captured groups wash off like ink in water. 9x9 first, then 13x13 and 19x19 |
| Chess | Paper theatre: cut-paper pieces on a stage, lit from the side | Classic, readable piece shapes; a captured piece folds flat and slides offstage |
| Checkers | Night arcade: neon pucks on a glowing grid | Jumps squash and stretch the puck; a king's crown pops on |
| Cargo Hold (sliding blocks) | A ship's hold: wooden crates slid to free one hatch | Crates thunk, the hatch swings open. No cars or parking lot (too close to a brand-name puzzle) |
| Untangle | Constellations: drag the stars until no lines cross | A solved level lights up into a picture (a whale, a fox, a ship) |

**Look and feel.** Recess feels like a toy you can pick up, not a printed page: deep saturated backgrounds with light
on them, chunky shapes, things that bounce, clack and squish (reduced motion always honored), sound one tap away. The games must be visually amazing (Cory, 2026-11-08): painted first, with code drawing only
geometry that must sit on exact coordinates; the builder paints a three-frame look board before writing game logic
and a box cover for the shelf (docs/agents/CODEX-RECESS.md, "Visually amazing").

**Puzzle material, free to use:** the Lichess puzzle database (CC0) for chess puzzles from real games; centuries-old
public domain Go problem collections; public domain checkers problems. Each spec checks the licence at source.

**Computer opponents** cover a real range (Cory, 2026-11-08): every board game (Go, Chess, Checkers and later ones like them) plays full games against the computer at several levels, from gentle beginners up to a genuinely strong top level, all offline in one file. Easy levels stay kind; the top ones give strong kids a real game. Go gets a
sensitivity check on its roots (China, Japan, Korea) like any cultural tool.

## The shell and the shelf

- **The Recess shell** is `kit/recess.js` and `kit/recess.css` (bundled with `kit:recess`). Every game shares it and
  nothing else: the corner controls (Undo, Restart, Sound, Motion, Scores), stars per level, a personal best, the
  3-letter initials board (local top 10 per level), the win card, sounds, a confetti burst, a seeded daily puzzle and
  device-only storage. `kit/recess-demo.html` is a test bench that uses every call; the API is in the file's header.
- **The shelf** is `/recess/` (`site/templates/recess.html`, rows in `data/recess.json`, box art in
  `site/templates/recess/`). Each game is a box with its grade band as a colored edge; the SVG boxes are placeholders.
- **Going live.** `build_site.py` works out each game from `tools/<id>/`: a game is live when `<id>.html` and
  `tool.json` exist (rename `tool.draft.json` at Sign-off). A live game gets a page at `/recess/<id>/` (cover, blurb,
  Play button, the grown-ups' note from `notes.md`) and plays full screen at `/recess/<id>/play/`. `art/cover.webp`
  replaces the placeholder box as soon as it exists. Once one game is live, the shelf joins the nav, the footer, search
  and the sitemap; until then it stays noindex and out of the nav. `build_site.py --recess` also counts
  `tool.draft.json`, for a local preview before Sign-off. Recess games sit on the build board under their own heading.

## Open questions

1. Does a game also appear on a standard's page, or only on the Recess shelf?
2. Which games go first once Recess has its look?
