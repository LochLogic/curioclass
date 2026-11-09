# Codex build brief, a Recess game (Curio Class)

You are building ONE **Recess game** for Curio Class (curioclass.org). This brief replaces `docs/agents/CODEX-BUILD.md`
for this game. A Recess game is not a lesson tool, and the most likely way to fail is to build one anyway: the kit
header, a welcome voice, numbered steps, a "what you learned" card, standard codes, the classroom look. None of that
belongs here.

Read first, in this order:

1. `docs/GAMES.md`, all of it. It holds the owner's decisions (Cory, 2026-11-07 and 2026-11-08): what Recess is, the
   design rules, "The first collection" world table and "The shell and the shelf". Where anything else disagrees,
   GAMES.md wins.
2. `tools/<id>/spec.md`, every line. It is the source of truth for the rules, modes, levels, puzzles, art and motion.
3. `kit/recess.js` (the header is the API), `kit/recess.css` and `kit/recess-demo.html`, a working example of every
   call. Build on the shell; do not re-implement it.
4. `data/recess.json`: this game's shelf row (title, blurb, band). Do not edit it; the shelf goes live by hand later.
5. `docs/agents/STANDARDS.md` and `docs/agents/decisions/BASELINE.md`, for sizes, contrast, keyboard, reduced motion
   and one offline file. They still bind. Their lesson flow (welcome, voice, steps, finish) does not.

## What a Recess game is

A real game where the thinking is the fun. Kids come when they are done with class, or at home on their own. The
owner's direction for the first five: they must look nice, grab attention and look different from the classroom
tools. Each game owns its whole world (board, art, motion, sound design layered on `Recess.play`); only the shell is
shared.

## What to build, and what not to

- Start from `<script src="kit:recess"></script>` and `<link rel="stylesheet" href="kit:recess">`. Use
  `Recess.start`, `Recess.level`, `Recess.canUndo`, `Recess.win({score, stars})`, the shell's initials board,
  `Recess.daily()`, `Recess.calm` and `Recess.onMotion` exactly as the demo does.
- Never use `kit:curio`, its header, cards, buttons or `Curio.voice`. No voice lines. No custom score, star, initials
  or high-score UI: the shell owns those.
- No class on screen: no standard codes, no lesson words, no "show the math" card. The teacher and parent note is
  `notes.md`, written from the spec's "notes.md" section.
- No coins, shops, loot, lives, streaks or punishing timers. Undo and instant restart everywhere the spec says; a fail
  says kindly what was off.
- Classic rules, our own art, boards and levels. Never copy a specific product's name, art, levels or look.
- Every puzzle set, level list and computer opponent ships inside the one file. The game makes no network requests.
- Computer opponents cover a real range (Cory, 2026-11-08): full games at several levels, from gentle beginners up to a
  genuinely strong top level, exactly as the spec's ladder says. Easy levels stay kind and quick; strong levels may
  think a few seconds a move. Every search runs in a Web Worker on a time budget (not only a depth), so the page never
  freezes, and the level picker says plainly how strong each one is.

## Machinery (from the regular brief)

From `docs/agents/CODEX-BUILD.md`, read and follow only these sections: **Ground rules**, **Images**, **Do not hang**
and **Check your work**. They are about files, ports, art and time limits. Skip "Make it look good and play well",
"Super tools", "Read, in this order", "Files to make" and its report template: this brief replaces them.

Files to make in `tools/<id>/`: `src.html`, `tool.draft.json` (`"stage": "built"`, `"recess": true`, and a `sources`
list naming every puzzle source with its licence as stated at the source), `notes.md`, `handoff.md`, `art/prompts.json`
and `art/<name>.webp` for painted images, plus `codex-report.md`. If `bundle_tool.py` or `audit_tool.py` refuses to run
without `voice/lines.json` or `audit-states.json`, write the smallest valid one and say so in the report. The bundle
`<id>.html` is generated and git-ignored.

Images: boards, pieces and anything that must stay exact are drawn in code (SVG or canvas). Paint only what the spec's
art list names (backdrops, textures, picture reveals). Never paint text.

Puzzle material: use only what the spec lists, with the licence the spec recorded. If you go online to fetch a
puzzle set the spec names, read the licence at the source first, keep raw files in `_scratch/<id>/data/`, and put
only the curated set into the file. Give gathering at most 30 minutes.

## Check your work

As the regular brief's "Check your work", with these changes:

- **Play it for real.** Play every mode end to end as a kid of the band's youngest grade and as an adult. Win a level,
  lose a level, play the daily, play a full game against each computer level and a pass-and-play game.
- **Rules check.** Run every edge case the spec's Rules section lists (for example ko, castling, en passant, forced
  capture, multi-jumps) in a scripted test in Scratch, and list each one PASS or FAIL in the report.
- **Puzzles and levels check.** Re-solve every shipped puzzle or level with a script in Scratch and confirm the stated
  solution, minimum moves and star cutoffs.
- **Break it.** For every star, score, win and best: random moves, undo abuse, restart abuse, replaying the daily,
  initials spam, resize mid-move, keyboard only. A best score a cheat can set is a fault.
- **Grab check.** Put one frame of yours beside a frame of `kit/recess-demo.html` and of one classroom tool. The game
  must look like its own world, not like either. Say what the most satisfying moment is and show its frame.
- **Class creep check:** search `src.html` for lesson words (standard, objective, learn, skill, lesson, correct answer,
  well done) and standard codes. Each hit is removed or explained.
- Sizes: 1366x768, 390x844 portrait and the STANDARDS sizes; Motion calm; sound off; a grayscale frame.

## Report: `tools/<id>/codex-report.md`

```
# Codex report: <id> (Recess)
## Built
## Rules check          (each edge case: PASS or FAIL)
## Puzzles and levels   (each re-solved: stated vs computed)
## Computer opponent    (each level: how it plays, think time measured, level-against-level results)
## Break it
## Grab check           (best moment, flattest moment, what you changed, frames compared)
## Class creep check
## Sources              (each puzzle source, licence as stated at the source)
## Done when            (each spec item: PASS or FAIL, with evidence)
## Frames looked at
## Art made
## Shell changes wanted (anything kit/recess.js should do that it does not; do not edit the kit)
## Left open
```

## For the self-checker

A Self-check of a Recess game follows `docs/agents/CODEX-REVIEW.md` for its process, fixes and report file, but judges
the game against this brief and GAMES.md, not the lesson norms. Never add a kit header, voice, lesson card or standard
code; remove any that slipped in. Play before you read the builder's report. The game failing to grab attention, or
looking like a classroom tool, is a should fix; a rule played wrong, a puzzle with a wrong or second solution the game
rejects, a computer opponent that freezes the page, or a star a cheat can earn is a blocker.
