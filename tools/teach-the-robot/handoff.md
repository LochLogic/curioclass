# Handoff: teach-the-robot

Built 2026-10-27 (build stage, grade 2, ml-lab family, first tool of the family). Status: `tool.draft.json` (no
painted art is planned, but voice clips are not recorded yet, so it bundles only with `CURIO_DRAFT=1`).

## What was built

- `src.html`: the tool. Teach mode (Next pet, Cat, Dog, Mystery pet, Forget, Start over, the memory wall) and Pet
  Parade (10 pets at 3.5 s each, 10 score slots, Kip's Chart). Everything is drawn in code: lobby, door, shelves,
  Kip, one parametric pet drawing for all 26 pets, icons.
- `kit/ml-lab.js`: the family engine, built to the full family description so the four siblings can use it.
  Reference: `docs/families/ml-lab.md`.
- `voice/lines.json` (41 lines since refine round 1, bank playful-friend), `art/prompts.json` (no assets), `notes.md`, `preview.svg`
  (800 x 500: Maple in the spotlight, the look-alike line to Marmalade, Kip showing "cat"), `tool.draft.json`.
- No existing kit file was changed.

## How src.html is laid out

In file order: CSS (three page layouts: wide, compact, stack; the panel comes before the stage in the DOM so Tab
reaches panel buttons before wall cards, and the grid puts the stage first on screen), then the script.
- Data: `F` (the six features), `DECK` (16) and `PARADE` (10), each `{id, name, label, coat, pat, v}`; `L` (the
  line table) and `NUM`.
- `state`: mode, wall `[{key, pet, idx, label, arriving}]`, deck (indexes still to show), `mi` (next Mystery pet),
  busy, sel, arrivals (a counter that makes stale lines drop), `teach.spot` / `parade.spot` (the pet in the
  spotlight and its phase: walk, wait, fly, think, guess, truth), running, slots, runs `[{right, mem}]`, `tk`
  (a cancel token), `speed` (tests only).
- Drawing: `petGeom`, `drawHead` (ears blend floppy to pointy, muzzle by snout, whiskers by whiskers, scalloped
  ruff by fluffy), `drawPet`, `drawPortrait` (a wall card), `drawKip` (screen face idle, think, cat or dog; badge
  ok or bad), `ICON` (100 x 100 icons in currentColor, details in `var(--ib)`).
- `layoutFor(W, H)` computes everything in real pixels per stage size: card size (height-aware, 40 to 88 px),
  16 or 8 cards per row, names under cards only at 52 px or more, Kip scale `ks`, pet scale `ps`, door size.
  `build()` draws the static scene; `drawShelves()`, `paintKip()` and `paintDyn()` redraw the moving parts.
- Teach: `nextPet`, `teachLabel`, `finishFly`, `mystery`, `selectCard`, `forget`, `startOver`. Parade:
  `startParade`, `stopParade`. Modes: `settle`, `setMode`, `relayout`.
- `window.__tool` for tests: `teachNow(n, labels)` puts the first n deck cards on the wall at once, `guessFor`,
  `previewSVG(W, H)` (returns `{svg, match}`), `layout()`, `vlog` (the voice log), plus the actions.

## Tricky parts

- The welcome is deferred while something is moving: its `valid` needs the stage idle and no pet waiting for a
  label, and `teachLabel` calls `V.welcome()` after each card lands.
- `settle()` on a mode change finishes a flying card (it lands), drops a walking or thinking pet and stops a
  parade (a part run adds no bar). Every async step checks `aliveFor(mode)` (the token `tk`) after each await.
- `anim(ms, step, alive)`: with Motion off it jumps to the end but still waits the full time, so the parade keeps
  its 3.5 s rhythm and the same scores. Calm mode places pets at once.
- The look-alike line runs from the pet's head top to the deciding card's lower corner that faces the pet
  (6 px in from the corner, end dot r 5), so it leaves between two names instead of across one. The truth badge goes above the pet when there is room, else to
  its left, else over the body, never over the face.
- Mystery (refine round 1): walk, then the prediction beat (at least 1.8 s), then on the first Mystery pet only
  the "looks the most alike" how line while Kip thinks, then the guess and the line together, held at least 2 s and
  until "Kip thinks" ends (each wait capped, so a missing voice never stalls it), then the truth.
- The hint is the kit's: event lines pass `hint: event + next how line` (helper `both`), and Read reads the hint, so
  both always name the next control. `teachHow()` and `paradeHow()` give the hint on a mode switch; `NEEDS` maps
  each how line to the control it names.
- `rowsFor(cols)`: at 8 cards per row a shelf gets its second row only when it needs one (fuller shelf, plus a free
  slot while cards are left). `drawShelves()` relayouts when that changes. It also keeps a focused card focused
  across redraws (`refocus`).
- Busy buttons use `aria-disabled` (still focusable, the kit's `needs` treats them as off); `steer(from, to)` moves
  focus to the next control when the one in use goes away.
- The bundler inlines `kit/ml-lab.js` between script tags: a literal closing script tag in that file (even in a
  comment) breaks the bundle. It happened once in this build.
- Bundle with `CURIO_DRAFT=1 python scripts/bundle_tool.py teach-the-robot` while the tool has `tool.draft.json`;
  without it the bundler silently skips the tool and the old bundle stays.

## Engine API (short; full reference in docs/families/ml-lab.md)

`MLLab.rng, uni, r2, item, dist, knn(train, item, {features, k}), train('knn' | 'tree' | 'linear', items, opts),
evaluate(model, items, {classes, groupBy, positive, threshold}), glyph, view.confusion, view.scatter,
view.groupBars, version`. This tool uses `knn` with k = 1 over all six features, through `guessFor`. Distance ties
go to the card taught first.

## Checked at build (2026-10-27, before refine; the parade numbers here are the old parade's, see Refine round 1)

- Done when 1: first tap plays the welcome; Next pet brings Marmalade; Cat files it with line 3.
- Done when 2: 2 cards give 4 of 10, missing Rusty, Luna, Noodle, Pippin, Waffles and Bramble.
- Done when 3: 16 cards give 10 of 10; the chart shows bars with their memory counts.
- Done when 4: 11 cards give 9 (Pippin missed); adding Ziggy gives 10 and line 29 plays.
- Done when 5: Marmalade as dog gives 6 instead of 4; Forget puts the card back at the front of the deck, and
  relabeling it cat gives 4 again.
- Done when 6: 50 Mystery pets (wall sizes 1, 2, 5, 11, 16): each shows one line ending on the card an independent
  `knn` call picks, and the truth matches the table.
- Done when 7: lines 2, 5 and 17 spoken once in a run; result lines every time.
- Done when 8: Next pet, Cat, Dog, Mystery pet and Start parade on screen without scrolling at 680x425, 1280x720,
  1366x768, 760x900 and 375x812 (inside the host iframe; no horizontal scroll). Panel buttons are 60 px tall.
- Done when 9: parade slots about 2.63 s apart with Motion on and off; same score.
- Frames looked at: 1920, 1366x768 (default, Mystery truth, parade mid-run), 1280x720, 1000x625, 800x500,
  760x900, 680x425 (Mystery, parade end with 4 bars), 375x812 (Teach, parade end). No console errors.
- Keyboard: Tab order is mode buttons, Motion, Sound, Read, Next pet, Mystery pet, Start over, then the wall
  cards; Enter selects a card, Delete forgets it and focus goes to Next pet.
- Engine: the teach-the-robot score table and the whole ai-evaluator results table reproduced in Node
  (scratch scripts t1.js and t2.js, not in the repo; the family doc lists the numbers). The three views rendered
  in Chrome with made-up data.

## Known gaps

- At 680x425 the stage is about 390 x 353, so wall cards are 43 px and their whole-cell hit area 47 px; 60 px
  hit areas are reached from about 1000 px wide.
- At 760x900 the header wraps to two rows (Read on the second); everything still fits.
- Scout ("white with dark spots #3a3a3a") is drawn as a white coat with #3a3a3a spots.
- Next pet and Mystery pet are disabled while a pet waits for its Cat or Dog label (the spec only says buttons are
  disabled while a pet walks or Kip thinks). This keeps one pet in the spotlight at a time.
- During the truth phase the look-alike line passes behind the big truth badge at some sizes. It still ends on
  the right card. When the badge has to sit over the pet (small stages), the pet's small name is hidden under it.
- The first Mystery pet takes about 8 s with voice (prediction, how Kip guesses, the guess); later ones about 5 s.
- Headless Chrome has no speech voice, so spoken timing was checked with the kit's caps, not real audio. Line 33
  ("The more examples Kip saw...") was confirmed queued, but the test switched modes too soon to hear it.
- Voice clips are not recorded yet (`scripts/voice.py teach-the-robot`); the browser voice speaks until then.

## Refine round 1 (2026-10-28)

What changed, by refine.md item:
- B1: the pet drawing. Dogs: a snout reaching out by the snout value with a big nose pad, tongue and whisker dots,
  round brown eyes, a collar with a tag, ears in a contrasting shade (lighter on dark coats, with a light outline),
  floppy and half ears hang in front of the head, a thick low wagging tail. Cats: whisker pads, pink nose, w mouth,
  slit pupils, long whiskers, a curled S tail. All 26 pets checked in a contact sheet.
- B2: the parade is 5 cats and 5 dogs (Nutmeg, a cat, replaces Rusty; Noodle is retuned to a fluffy white dog).
  Engine unchanged. New table (also in spec.md under "Refine changes" and in notes.md):

  | Cards taught (N) | 1 | 2 | 3 | 4 | 5 to 9 | 10 and 11 | 12 to 16 |
  |---|---|---|---|---|---|---|---|
  | Right labels | 5 | 6 | 7 | 7 | 8 | 9 | 10 |
  | Marmalade labeled dog | 5 | 5 | 6 | 6 | 8 | 8 | 8 |

  Node check: for every N from 1 to 16, every single wrong label of any taught card lowers or holds the score.
  2-card misses: Luna, Bramble (like Bear), Pippin, Waffles (like Marmalade). Ziggy fixes Pippin (card 12), Pudding
  fixes Waffles first (card 10). Snowball as dog with 5 cards: 8 to 6.
- 3 and 20: once the deck is used up, Pet Parade replaces Next pet, empty slots go away, the hints name Mystery pet,
  Pet Parade, Teach or Start over.
- 4: Pet Parade with an empty wall says "Tap Teach first!", no welcome, and the Teach button pulse is drawn inside
  the button (the switcher clips outside shadows).
- 5: every event line carries its next step in the hint (after a Mystery result, Forget, Start over, a new card),
  and a matching how line is spoken once.
- 6 and 18: the prediction beat, then line 6 as a how line on the first Mystery pet; the guess line plays as the
  guess shows.
- 7 and 8: focus stays on the card after Enter; aria-disabled plus `steer` keep focus on a live control.
- 9: header buttons 60 px in this tool's CSS. 10: shelf counts say "3 pets". 11: guess holds 2 s (Mystery and
  parade; parade is 3.5 s per pet). 12: Kip smiles at 8 or more, looks puzzled at 4 or less. 13: only needed rows.
  14: glow stays on the shelf, the line ends on the card's corner. 15: chart axis 14 px, values and memory counts
  16 px, memory counter 34 px with 24 px paws. 16: a hit rect over the whole cell. 17: line 13 reworded.
  19: "Oops! Kip remembered that pet wrong." when the deciding card had a wrong label; line 33 says "different".
- Nits: hint changes at once when Cat or Dog is tapped; paws hidden at the compact layout; stage `role="group"`;
  Next pet and Mystery pet hush a playing line; confusion cells without onCell lose tabindex (engine);
  `MLLab.version` in the family doc; CSTA wording and a chart talk prompt in notes.md; "Pudding fixes it first".

Checked after refine (headless Chrome on ports 9410 and 9412, and Node):
- Scores in the page: 1 card 5, 2 cards 6 (misses Luna, Pippin, Waffles, Bramble), 5 cards 8, 11 cards 9 (Pippin),
  12 cards 10, 16 cards 10; Marmalade as dog: 5 (2 cards), 8 (12 cards); Snowball as dog at 5 cards: 6.
- 50 Mystery pets (wall sizes 1, 2, 5, 11, 16): one line, one end dot, the card an independent `knn` picks.
- Motion off: parade slots 3.52 to 3.56 s apart, 3 cards score 7 as in the table.
- Voice, real clicks: catOrDog, tryMystery, predict, looks, afterMystery, forgetHow, forgotHow, nextHow spoken once
  then silent (heard); events every time; empty-wall Pet Parade speaks only its own line.
- Keyboard: Next pet to Cat, Cat to Next pet (or Pet Parade when the deck is done), Mystery keeps focus, Enter on
  a card keeps it, arrows move, Escape lets go, Delete forgets and focus goes to Next pet, Start parade to Stop and
  back. Real keys: Enter, ArrowRight, Enter selects the second card with focus on it.
- Frames at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 (host iframe), looked
  at. No console errors. host.html deleted, no listeners left on 9410 to 9419.
- Engine: t1 (new parade) and t2 (ai-evaluator) re-run in Node, numbers as in the family doc.

## Refine round 2 (2026-10-28)

- Exit check item: at 680x425 the Pet Parade panel squeezed the hint to 41 px, so three-line hints ran under Start
  parade or Stop. Now the hint never shrinks (`flex: none`) and, at the compact layout, keeps room for three lines
  at 14 px (`min-height: 4.05em`, 57 px) in both modes. Kip's Chart takes what is left of the parade panel (at
  least 72 px; renderChart's floor is 72, and a chart under 56 px of plot keeps only the 0 and 10 labels). The
  compact layout hides the small "7 of 10" under the slots, since the stage shows the same tally large.
- Measured (hint height = its content, panel scrollHeight = clientHeight, so nothing hidden or scrolled):
  680x425 and 800x500 parade mid run, parade end (3 cards), parade end with the deck used up (the longest hint),
  and Teach with the deck used up: hint 57 px, Start parade or Stop at 144 to 204 px. Kip's Chart 104 to 108 px at
  680x425, 179 to 183 px at 800x500. 760x900 and 375x812 (stack) unchanged: the hint grows to its lines and Start
  parade stays on screen.
- Frames looked at: 680x425 parade mid run, parade end with the deck used up, Teach with the deck used up;
  800x500 parade end; 375x812 parade end.
- Wall card hit area at 680x425 not lifted: the stage there is about 390 px wide, so 8 cards per row leave 47 px
  cells, and a bigger hit rect would overlap the next card. It reaches 60 px from about 1000 px wide.

## Engine changes made after first writing it

- `view.confusion`: the row labels column now fits the longest name, the two titles drop to two lines when
  narrow, and column headers center the glyph and name together.
- `view.scatter`: points at 0 and 1 sit inside the frame.
- Refine round 1: `view.confusion` cells without `onCell` drop their tabindex (view code only; tables unchanged).

## Next steps

- Record voice clips (41 lines, 10 new or changed in refine round 1), then rename `tool.draft.json` to `tool.json`.
- Siblings: read `docs/families/ml-lab.md` first and check their spec tables in Node before building.

## For Cory

Nothing needs a decision.
