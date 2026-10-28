# Family: robot

Four tools, kindergarten to grade 3 (computer science, Algorithms and Programming), share one program engine:
`kit/robot.js`, inlined with `<script src="kit:robot"></script>` after `kit:curio`. It holds a program of cards, the
card strip that edits it, and the runner that walks it, with a trace of what each card did. It was lifted from
robot-dance's card strip and step runner, and snowy-mail-route was the first tool built on it. Sound, voice, art and
the world stay in the tool.

## What the engine does (shared)

```js
// 1. Program model
const prog = Robot.program({max: 12, onEdit(info, prog) {}});
prog.list                      // [{id, op, args}]; prog.gen goes up on every edit; prog.length, prog.full, prog.max
prog.add(op, at, args)         // at = end by default; returns the card, or null when full
prog.replace(i, op, args)      // keeps the card's id
prog.move(i, d)                // swap with the neighbor d away (-1 or 1); returns the new index, or -1
prog.remove(i), prog.clear(), prog.load(list)   // load takes ops ('up') or {op, args}, cut to max, new ids
prog.on(fn)                    // fn({kind: 'add'|'replace'|'move'|'remove'|'clear'|'load', ...}, prog) on every edit
prog.ops(), prog.card(i), prog.indexOf(id)

// 2. The card strip (the UI)
const strip = Robot.strip(el, {
  prog, max, layout: 'row' | 'column', label: "Pip's arrow cards",
  renderCard(card, i, faceEl, btn) {},  // draw the card face (the tool's art)
  cardLabel(card, i) {},                // the card's accessible name, e.g. "Card 3: Left"
  onSelect(i | null, why) {},           // why: 'tap', 'key', 'edit', 'lock' or the tool's own word
  onMove(from, to) {}, onRemove(i, card) {},
  canEdit() {},                         // false: card taps, the three buttons and keys all do nothing
  buttons: el,                          // where the three card buttons go (default: right after the strip)
  bounds: () => el,                     // the box the buttons stay inside
  emptyFocus: () => el,                 // where focus goes when the last card is taken away
  names: {earlier, later, remove}, buttonsLabel,
});
strip.select(i, why), strip.deselect(why), strip.sel, strip.locked   // getters
strip.el, strip.box, strip.cells   // the strip, the box around it and the slot elements (read only)
strip.setNow(i)                // the run pointer (a chevron) and a glow on card i; null clears
strip.setBug(i, text = '?')    // a badge on the card a run stopped at
strip.pulse(i)                 // a pulsing card
strip.lock(on)                 // during a run: cards stay focusable, edits are off (aria-disabled)
strip.flash(), strip.flip(i), strip.render(), strip.place(), strip.card(i), strip.cell(i)
strip.size({cw, ch, gap, rowGap, cols, nd, pad, ptrW, ptrH, btn, btnGap, btnH, btnTop})   // px, per layout

// 3. The runner
const run = Robot.run(prog, {
  style: 'sequence' | 'rules',
  beat: 1100 | () => ms,       // read before every beat, so a speed button acts at once
  exec, onStep(i, card, info, ms, run), onPause(next, run), onEnd(result, run),
  target, same(card, want), pause,          // sequence with a target (robot-dance)
  world, when(card, world, run), tick(n, world, run), ticks, traceIdle,   // rules
  snap(world),                              // what to keep in the trace when exec gives no snap; sequence calls
                                            // snap() with no argument (the tool reads its own world), rules snap(world)
});
run.go()      // walk to the end; when paused, walk the rest
run.step()    // one card (or one tick), then pause; ignored while a beat is running
run.stop()    // at once; late callbacks of a stopped run are ignored (generation guard)
run.status    // 'ready' | 'running' | 'paused' | 'ended' | 'stopped'; run.busy, run.next, run.tick, run.result
run.gen       // goes up on every stop; a tool keeps it to spot late work from an old walk
run.alive(g)  // no argument: still ready, running or paused; with g: g is still run.gen and the run has not ended
              // or stopped (check it after an await in onStep before touching the world)
run.trace     // [{t, i, op, result, reason, snap}]; run.traceFor(i); Robot.trace and Robot.traceFor(i): the last run
Robot.last    // the last run made (getter), Robot.version  // 1
```

- **Sequence:** each card once, in order. `exec(card, i, run, targetResult)` returns `{ok: true}` or
  `{stop: reason}`, with an optional `snap`. Results: `done`, `stop` (with `reason` and `step`), `stopped`, and
  `edited` if the program changed under the run. With a `target` (a list of ops or cards) it also gives robot-dance's
  `ok`, `wrong`, `ranout` and `extra`, and `info.want` in onStep.
- **Rules:** every tick the cards are checked top to bottom with `when(card, world, run)`; the first that holds runs
  `exec(card, i, world, run)`; at most one fires per tick. Then `tick(n, world, run)` moves the world; it returns
  false to end the run (`done`). Also ends on `ticks`, a `{stop}` or Stop.
- `onStep` is called once per beat with `info = {result, reason, snap, want | tick}` and the beat length, so the tool
  can time its animation inside the beat. The runner waits the beat after `onStep`; `onEnd` and `onPause` see a
  settled runner (`busy` false).

Fixed by the engine: the strip's slots (numbered cards, dashed empty slots with their number), one selection at a
time, the three card buttons (Move earlier, Take away, Move later; Move up and Move down in a column) under the
strip or beside it, with chevron-and-bar icons that do not look like arrow commands; keys (arrows move between cards
or move the picked card, Delete and Backspace take it away, Escape puts it down); focus kept on the same card across
redraws and rescued when buttons hide; a FLIP slide when a card moves (none with Motion off); the run pointer, glow,
bug badge and pulse. Default styles are injected first in `<head>` (`#robot-css`), so a tool's own CSS wins. Colors:
`--rb-line`, `--rb-card`, `--rb-ink`, `--rb-sel`, `--rb-glow`, `--rb-pulse`, `--rb-bug`, `--rb-empty`, `--rb-r`.

- **Picking:** a tap on a card picks it and a second tap puts it down. A card the tool picked (`strip.select(i,
  'foot')`, say from a footprint) stays picked on the first tap, so the class can tap it to look without losing it;
  the next tap puts it down. `onSelect` gets the tool's `why`.
- **Motion off (`.calm`):** the kit's `.calm *` rule cuts every animation to almost nothing, which makes an infinite
  pulse strobe. The engine turns the pulse into a still ring and the bug wobble into nothing under `.calm`, and a FLIP
  slide or card flip does not run. A sibling's own looping animations need the same `animation:none` under `.calm`.

## Rules for siblings

- Cards, the strip, the runner and the trace come from the engine. A sibling adds its own world (a stage, a map, a
  crossing), its own card faces, sounds and voice, and decides what each card does in `exec`.
- Any edit resets the world and clears the old run (the strip already clears its marks). Lock the strip while a run
  is walking.
- **The bug badge does not answer the question.** When a run stops on a card and the narrator asks "which card sent
  Pip that way?", `setBug` waits: show the badge only after the class answers (a tap on a footprint, a trace mark or a
  card) or after the hint has asked twice. A tool that never asks may badge at once. (Refine round 1,
  snowy-mail-route.)
- **After a stop, point at the last good mark.** The hint names the last trace mark the run left ("the card after it
  made Pip bump"), or card one when the run stopped before any mark, not marks the bad card never made.
- K-2 siblings: card buttons 60 px at full screen (44 px in the 16:10 preview), every card has a spoken or drawn
  meaning, nothing to read.
- New engine features go into the engine and this file in the same change, keeping existing calls working.

## What each tool brings (its own)

| Tool | Grade | Engine use | Its one idea (not shared) |
|---|---|---|---|
| robot-dance | K | (own copy for now) sequence with a target | Bolt dances the cards beside Dot, who knows the dance; Bolt trips on the wrong card |
| snowy-mail-route | 1 | sequence, ops up down left right, max 12, row | Pip walks a snowy grid and leaves numbered footprints; tap a footprint to find its card; guess where Pip stops |
| loop-garden | 2 | (own copy for now) | relative turns and repeat blocks, fewest-block stars |
| traffic-light-coder | 3 | rules, column | if-then rules checked again and again at a crossing |

robot-dance and loop-garden move onto the engine only when they are next reworked.
