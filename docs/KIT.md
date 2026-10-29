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

Family engines today (read the family doc before using one):

| Engine | Doc | First tool |
|---|---|---|
| `kit/graphing.js` | docs/families/graphing.md | live graphing tools |
| `kit/network.js` | docs/families/network.md | internet-journey |
| `kit/security.js` | docs/families/security.md | data-defenders (capture-the-flag extends it, BR2) |
| `kit/ml-lab.js` | docs/families/ml-lab.md | teach-the-robot |
| `kit/dance.js` | docs/families/dance.md | levels-and-pathways |
| `kit/perspective.js` | docs/families/perspective.md | city-skyline-studio |
| `kit/robot.js` | docs/families/robot.md | snowy-mail-route |
| `kit/data-desk.js` | docs/families/data-desk.md | simulation-studio |
| `kit/music-studio.js` | docs/families/music-studio.md | song-form-builder (BR2) |
| `kit/stage.js` | docs/families/stage.md | stage-blocker (BR2; director-s-chair will reuse it) |
| `kit/fact-check.js` | docs/families/fact-check.md | fake-or-fact-lab (BR2) |
| `kit/careers.js` | docs/families/careers.md | career-cluster-explorer (career-match-quiz keeps its own copy for now) |

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
Curio.tone(freq, dur, vol, type); Curio.yes()   // chimes (silent when Sound is off, and before the first tap or key)
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
const V = Curio.voice({lines, scope, welcome, speaks, welcomeAfter, hint, read, est})   // once, before Curio.init
V.say(line, {kind, key, valid, needs, maxAge, hold, hint, wait, now})   // queue a line: true if queued (a promise with wait)
V.say([line, line, [line, partOpts]], opts)   // a sequence: plays whole, in order (see "Sequences")
V.how(line, opts)               // V.say with kind 'how'
V.welcome()                     // queue the mode's welcome if it was never said; true if queued
V.dropQueued(f)                 // drop lines not started yet (all, or those f(line) picks); the line playing goes on
V.hush()                        // stop everything: queue, the clip in progress, Read (mode change, reset)
V.read()                        // what the Read button does (wired for you)
V.allLines()                    // every string in opts.lines, once each (for __tool.allLines and voice/lines.json)
V.heard(keyOrText)              // has this line started playing (spoken aloud) yet?
V.log, V.queue, V.said, V.playing, V.tapped   // for tests and VERIFY
```

A `line` is a text, or a key of `opts.lines` (`V.how('rideDrag')` speaks `lines.rideDrag`, and its key is `'rideDrag'`).

Options for `Curio.voice`:
- `lines: L`: the tool's line table. Lines and welcomes can then be named by key, and `V.allLines()` walks it (nested
  objects and lists too).
- `scope: () => state.mode`: a line belongs to the scope it was queued in. When it comes to play in a different
  scope it is dropped (`stale`), with the rest of its sequence. This replaces a `valid: () => state.mode === m` on
  every line.
- `welcome: () => entry`: the current mode's welcome, a list of entries, or null when none fits now (Remix with
  nothing to change). An entry is a key of `lines`, `[key, text]`, or `[key, text, {valid, needs, hint}]` (the text may
  be left out when the key is in `lines`: `[key, {valid}]`). Each key is said once. A queued welcome plays only while
  this still lists it and its own `valid` and `needs` pass; a welcome that fails is dropped unmarked and comes again at
  the next `V.welcome()` (for example `valid: () => !state.playing`, so it never talks over a ride already running).
- `speaks: '.tile, #try'`: buttons whose line comes later (after an animation); a first tap on one skips the welcome.
- `welcomeAfter: true`: a first tap that has its own line (or is a `speaks` button) puts the welcome off instead of
  skipping it: it is queued once the tap's line has finished. For tools with one mode, where a skipped welcome would
  never come back. Read and Sound as the first tap still skip it.
- `hint`: the hint element's id (default `hint`), a function `text => {}` for a tool that draws its own hint, or `false`
  when the tool owns the hint and lines never write it. With a function or `false`, pass `read` too: Read otherwise
  falls back to `#hint` and the helper says so once in the console.
- `read: () => text` (or a list of lines): what Read speaks (default: the hint's text).
- `est: text => ms`: Sound-off pacing (default 600 + 62 per character).

Options for `say`:
- `kind`: `'event'` (the default: praise, results, failures, "that code doesn't work") is spoken every time.
  `'how'` (how-to and teaching lines) is spoken the first time it plays, then only shown in the hint, silently.
- `key`: what "the same line" means (default: the lines key, else the text). A newer copy of a queued line replaces it,
  and a newer how-to replaces any older queued how-to (a queued sequence goes as one unit).
- `valid: () => bool`, `needs: '#share'`, `maxAge: ms` (a game beat that waited too long): checked when the line's turn
  comes, never when it is queued. A line that fails is dropped and stays unmarked, so its trigger can queue it again.
- `hold: ms`: the longest this line may hold the queue, for a recorded clip close to the default cap (2.5 s plus 80 ms
  a character, kept for a clip that never ends). It only lengthens the cap. A sequence part takes it in its own options.
- `needs` is a selector or a list. Each control must be there, enabled (not `disabled`, not `aria-disabled`), not
  `visibility: hidden`, and visible to the student: inside the viewport, or inside a scroll panel (the nearest
  `overflow: auto` or `scroll` ancestor that actually scrolls) whose box is inside the viewport. So a button below the
  fold of the page does not count, and a button scrolled out of sight in an on-screen side panel does (the student
  can scroll the panel they are looking at).
- `hint`: `true` (the default: the line's text goes in the hint), a text (this goes in the hint instead), or `false`
  (speak it without touching the hint). Ignored when the voice has `hint: false`.
- `wait: true`: return a promise that resolves `'spoken'`, `'silent'` or `'dropped'` once the line (for a sequence, its
  last line) has had its turn (with Sound off, after the estimated time). `wait: 'detail'` resolves `{as, why}`
  instead, with `why` as in the log (`heard`, `off`, `early`, `stale`, `newer`, `chain`, `hush`). For timing-bound
  tools: music, Pause and Step.
- `now: true`: drop the queue and cut the line in progress, then speak this one (Read still wins).

Sequences: `V.how(['full', 'rideChange'], {needs: '#restart'})` queues both lines as one unit. They play in order, and
the second never evicts the first (in v1, `V.how(a); V.how(b)` dropped `a`). A newer how-to queued later replaces
whatever of the sequence has not started yet, as one unit. When one line of a sequence is dropped (stale, newer, hush), the lines after it are dropped
too (`chain`), unmarked. The options apply to every line; a part written `[line, {valid, needs, kind, key, hint}]`
adds its own (its `valid` and `needs` are added to the shared ones, its `kind` replaces).

Built in: nothing speaks before the first tap or key (lines before it only set the hint), and `Curio.tone` and
`Curio.yes` are silent until then too. The first tap queues the welcome only after the tap's own handler has run, and
only if that handler neither queued nor started a line; Read, Sound and `speaks` taps skip it, unmarked (unless
`welcomeAfter`). Sound off hushes and still updates the hint; Sound on queues the welcome if it was never said. Read
stops the queue, speaks `read()` or the hint even with Sound off, and lines queued during it wait for it; a hush
releases a stopped Read, so nothing waits on it. A line is marked said when it starts playing.

`V.log` holds one entry per line: `{t, key, kind, text, as, why}`, where `as` is `spoken`, `silent` (why: `heard`,
`off`, `early`), `dropped` (why: `stale`, `newer`, `chain`, `hush`) or `read`. Repeats of the same silent or dropped
line in a row fold into one entry with a count `n` (and `t2`, the time of the last one), so a slider that re-queues its
how-to on every input leaves one entry, not hundreds. A spoken line cut off while it was playing gets `cut` on its
entry (`hush`, `read`, `sound` or `now`), so tests can find a welcome or line that was cut and never came back
(`scripts/audit_tool.py` does). `V.queue` lists the lines waiting.

A tool on the helper (about 20 lines in place of the 60 to 100 line copies):

```js
const L = {wA: 'Welcome to the shelf.', shelf: 'Drag a part onto the bench.', build: 'Now press Build.',
  fixed: 'It works.', name: {gear: 'A gear.', axle: 'An axle.'}, step: ['First...', 'Then...']};
const V = Curio.voice({
  lines: L, scope: () => state.mode,
  welcome: () => state.mode === 'a' ? ['wA', {valid: () => !state.running}] : null,
  speaks: '.tile, #try',
});
const howKey = () => !state.placed.size ? 'shelf' : 'build';   // the how-to for this moment
function setMode(m) {
  V.hush();
  state.mode = m; $('hint').textContent = L.shelf;
  V.welcome() || V.how(howKey());          // the welcome once; after that, the how-to (spoken once)
}
function placePart(id) {
  V.dropQueued();                           // a newer action: older lines that have not started give way
  V.say(L.name[id], {valid: () => state.placed.has(id)});
  V.how('build', {valid: () => howKey() === 'build', needs: '#build'});
}
function fixed() { Curio.yes(); V.say('fixed'); }                        // an event: heard every time
async function step(i) { await V.say(L.step[i], {wait: true}); runLine(i); }   // Step: go on once it is said
window.__tool = {state, allLines: V.allLines, vlog: V.log, get vq() { return V.queue; }};    // tests read the log
```

Tests: `python scripts/test_voice.py` runs `kit/voice-test.html` (not a tool, never bundled or shipped) in muted
headless Chrome with held clicks and prints PASS or FAIL per rule (`--only R28` runs one).

## curio.css

Reset, `header` with `.seg` mode buttons and `.icon-btn`, the `main` stage-plus-panel grid, `.stage` and `.scene`,
`.panel`, `.hint`, `.tip`, `.big-btn` (`.gold`). Each tool sets its colors on `:root`: `--paper --ink --muted --line
--focus --brand --btn --btn-line --head-ink --panel`. Everything else about the look is the tool's own.

## Changing the kit

A kit change touches every kit tool. Keep calls backward compatible, rebundle all tools
(`python scripts/bundle_tool.py`), and spot-check a few with `scripts/shoot.py` before deploying.
