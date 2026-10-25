# The kit

What every Curio Class tool does the same way lives in `kit/`, so a fix reaches every tool on its next bundle.
New tools start from `kit/starter/src.html`. The 54 tools built before the kit (2026-10-25) carry their own copies;
move one onto the kit when it is next reworked.

## Three layers (what goes where)

| Layer | Where | What | Example |
|---|---|---|---|
| Kit | `kit/curio.js`, `kit/curio.css` | the same in every tool | Motion, Sound, Read, speech, chimes, the header and panel frame |
| Family engine | `kit/<family>.js`, spec in `docs/families/<family>.md` | a mechanic shared by a collection | the number line, data table and charts, coordinate plane |
| Tool | `tools/<id>/src.html` | the one idea, its world and content | the coaster car, the diver, the ski hill |

Rule of thumb: if two tools in different families need it, it belongs in the kit. If only siblings need it, it is
the family engine. Everything that makes a tool feel like itself stays in the tool.

## Using it

```html
<link rel="stylesheet" href="kit:curio">          <!-- before the tool's own <style> -->
<script src="kit:curio"></script>                  <!-- before the tool's own script -->
<script src="kit:number-line"></script>            <!-- a family engine, after the kit -->
```

`scripts/bundle_tool.py` inlines them. The header buttons need the ids `motion`, `sound` and `read`; the panel's
hint paragraph is `hint` (Read falls back to it).

## curio.js

```js
Curio.init({clips: "voice:*", rate: .9, readFallback: () => text})   // once, at the end of the tool's script
Curio.say(lineOrLines, force)   // recorded clip if there is one, else the best browser voice; resolves when done
Curio.stop()                    // stop talking (mode changes, resets)
Curio.wait(ms)
Curio.tone(freq, dur, vol, type); Curio.yes()   // chimes (silent when Sound is off)
Curio.fit('stage', 'scene', 1000, 620)          // scale a fixed-size design to its box (sets --s)
Curio.reduce, Curio.sound, Curio.last           // current state
Curio.onMotion(fn), Curio.onSound(fn)           // react to the buttons
```

Behavior built in: nothing speaks before the first tap or key; a waiting browser line is dropped on stop (no echo);
Motion is remembered across tools (`curio-motion`) and adds `body.calm`, which stops CSS animation (timing is kept).

## curio.css

Reset, `header` with `.seg` mode buttons and `.icon-btn`, the `main` stage-plus-panel grid, `.stage` and `.scene`,
`.panel`, `.hint`, `.tip`, `.big-btn` (`.gold`). Each tool sets its colors on `:root`: `--paper --ink --muted --line
--focus --brand --btn --btn-line --head-ink --panel`. Everything else about the look is the tool's own.

## Changing the kit

A kit change touches every kit tool. Keep calls backward compatible, rebundle all tools
(`python scripts/bundle_tool.py`), and spot-check a few with `scripts/shoot.py` before deploying.
