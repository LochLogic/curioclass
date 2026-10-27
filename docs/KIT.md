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
Curio.voice(opts)               // the narration queue for a tool's lines: see "Voice" below
```

Behavior built in: nothing speaks before the first tap or key; a waiting browser line is dropped on stop (no echo);
Motion is remembered across tools (`curio-motion`) and adds `body.calm`, which stops CSS animation (timing is kept).

## Voice: Curio.voice (the narration queue)

New tools narrate through `Curio.voice` instead of copying a queue (STANDARDS.md "Voice behavior"). It holds the rules
every CS-batch fix round relearned: one line at a time, each line checked when its turn comes, how-to lines spoken
once, results spoken every time, the first-tap welcome, Read, Sound and one log for tests.

```js
const V = Curio.voice({welcome, speaks, hint, read, est})   // once, before Curio.init; returns the same V on later calls
V.say(text, {kind, key, valid, needs, maxAge, hint, wait, now})   // queue a line: true if queued (a promise with wait)
V.how(text, opts)               // V.say with kind 'how'
V.welcome()                     // queue the mode's welcome if it was never said; true if queued
V.dropQueued(f)                 // drop lines not started yet (all, or those f(line) picks); the line playing goes on
V.hush()                        // stop everything: queue, the clip in progress, Read (mode change, reset)
V.read()                        // what the Read button does (wired for you)
V.log, V.queue, V.said, V.playing, V.tapped   // for tests and VERIFY
```

Options for `Curio.voice`:
- `welcome: () => [key, text]`: the current mode's welcome, a list of `[key, text]` pairs, or null when it does not fit
  now (Remix with nothing to change). Each key is said once. A queued welcome plays only while this still lists it.
- `speaks: '.tile, #try'`: buttons whose line comes later (after an animation); a first tap on one skips the welcome.
- `hint`: the hint element's id (default `hint`) or a function `text => {}` for a tool that draws its own hint.
- `read: () => text`: what Read speaks (default: the hint's text). `est: text => ms`: Sound-off pacing (default 600 + 62 per character).

Options for `say`:
- `kind`: `'event'` (the default: praise, results, failures, "that code doesn't work") is spoken every time.
  `'how'` (how-to and teaching lines) is spoken the first time it plays, then only shown in the hint, silently.
- `key`: what "the same line" means (default: the text). A newer copy of a queued line replaces it, and a newer how-to
  replaces any older queued how-to.
- `valid: () => bool`, `needs: '#share'` (a selector or a list: each control must be there, shown and enabled),
  `maxAge: ms` (a game beat that waited too long): checked when the line's turn comes, never when it is queued. A line
  that fails is dropped and stays unmarked, so its trigger can queue it again.
- `hint: false`: speak it without putting it in the hint.
- `wait: true`: return a promise that resolves `'spoken'`, `'silent'` or `'dropped'` once the line has had its turn (with
  Sound off, after the estimated time). For timing-bound tools: music, Pause and Step.
- `now: true`: drop the queue and cut the line in progress, then speak this one (Read still wins).

Built in: nothing speaks before the first tap or key (lines before it only set the hint). The first tap queues the
welcome only after the tap's own handler has run, and only if that handler neither queued nor started a line; Read,
Sound and `speaks` taps skip it, unmarked. Sound off hushes and still updates the hint; Sound on queues the welcome if
it was never said. Read stops the queue, speaks the hint even with Sound off, and lines queued during it wait for it;
a hush releases a stopped Read, so nothing waits on it. A line is marked said when it starts playing.

`V.log` holds one entry per line: `{t, key, kind, text, as, why}`, where `as` is `spoken`, `silent` (why: `heard`,
`off`, `early`), `dropped` (why: `stale`, `newer`, `hush`) or `read`. `V.queue` lists the lines waiting.

A tool on the helper (about 20 lines in place of the 60 to 100 line copies):

```js
const V = Curio.voice({
  welcome: () => ['w-' + state.mode, L.w[state.mode]],
  speaks: '.tile, #try',
});
const howText = () => !state.placed.size ? L.how.shelf : L.how.build;   // the how-to for this moment
function setMode(m) {
  V.hush();
  state.mode = m; $('hint').textContent = L.w[m];
  V.welcome() || V.how(howText());       // the welcome once; after that, the how-to (spoken once)
}
function placePart(id) {
  V.dropQueued();                         // a newer action: older lines that have not started give way
  V.say(L.name[id], {valid: () => state.placed.has(id)});
  V.how(howText(), {valid: () => howText() === L.how.build});
}
function fixed() { Curio.yes(); V.say(L.fixed); }                       // an event: heard every time
async function step(i) { await V.say(L.step[i], {wait: true}); runLine(i); }   // Step: go on once it is said
window.__tool = {state, vlog: V.log, get vq() { return V.queue; }};    // tests read the log
```

Tests: `python scripts/test_voice.py` runs `kit/voice-test.html` (not a tool, never bundled or shipped) in muted
headless Chrome with held clicks and prints PASS or FAIL per rule.

## curio.css

Reset, `header` with `.seg` mode buttons and `.icon-btn`, the `main` stage-plus-panel grid, `.stage` and `.scene`,
`.panel`, `.hint`, `.tip`, `.big-btn` (`.gold`). Each tool sets its colors on `:root`: `--paper --ink --muted --line
--focus --brand --btn --btn-line --head-ink --panel`. Everything else about the look is the tool's own.

## Changing the kit

A kit change touches every kit tool. Keep calls backward compatible, rebundle all tools
(`python scripts/bundle_tool.py`), and spot-check a few with `scripts/shoot.py` before deploying.
