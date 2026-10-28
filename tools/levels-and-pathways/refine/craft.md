# Craft lens: levels-and-pathways (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/dance.js and
docs/families/dance.md. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py levels-and-pathways` (149 KB).
Driven with `scripts/drive.py` (held clicks 0.12 s, Sound on, Motion on unless noted), own profile, ports 9600 to 9609.
Browser voice (clips not recorded yet, as expected).

Counts: blockers 0, should fix 4 (general 4, family 0), polish 3 (general 2, family 1), nit 4 (general 2, family 2).

## Contract

- One file, 149 KB, no network requests (`performance.getEntriesByType('resource')` empty in every mode; the only
  URLs in the bundle are the SVG namespace), no console errors or exceptions in any of the 40-odd driven shots.
- Kit used: `Curio.voice`, `Curio.yes/tone`, kit motion, sound and read buttons. `kit/dance.js` loads after
  `kit:curio`; no closing script tag inside it.
- Engine against the spec's Family engine section: floor views (studio, stage, square, void), 27 named poses,
  `level` with per-pose high and low, 8 gaits, 6 `dyn` qualities, `phrase` with `side: 'L'`, `clock` with count-in,
  pause, resume, seek, setBpm (next count), stop and token, `play` with offsets and loop, `trail` (ribbon, exposure,
  off), `music` (silent with Sound off and before the first tap), `counts`, Motion off as keyframes per count: all
  present. The figure lives in dance.js, not movement.js, which is right per BASELINE w1-21.
- docs/families/dance.md against the code: every documented call exists with the documented options. Small gaps
  below (nit).

## Access

- Keyboard: every control is a real button; Tab order is header, then panel; focus ring (4 px #6b4fbb plus white) is
  clearly visible (frame `k_tab`). Draw's keyboard path works: Tab to Surprise path, Enter makes a path and names its
  parts (`k_draw_surprise`).
- Icons: every button has an icon (emoji or a drawn glyph or mini dancer); none text-only.
- Color never the only signal: level tiles carry cloud, table, grass and a word; ribbons carry pattern plus end badge;
  pressed tiles add a check mark; solved Mystery dots add a tick.
- Motion off (`calm_paths`): the trip runs in steps, ribbon and badge still drawn. Sound off: no voice, no tune.
  Read works with Sound off.
- Targets: panel tiles are 72 px and big buttons 60 px at every size. Header buttons are not (finding 1).

## Lines

- `voice/lines.json` holds 40 lines; the `L` table in src.html holds the same 40, word for word, no extras, no
  duplicates. Every fixed line is in `allLines()`.
- No em dashes in src.html, notes.md, tool.draft.json, dance.js or dance.md. "Curio Class" never shortened. Notes say
  nothing is saved or sent (rule 7 not triggered: nothing is stored). Classroom-safe language throughout.

## Art

- No `art:` tokens; prompts.json lists none (everything is drawn in code). The dancer is simple shapes, people:
  false is right.

## Standard voice check

All runs with held clicks; times from `__tool.vlog`.

| Line | Kind | Action (x5) | Expected | Spoken |
|---|---|---|---|---|
| stretch | event | Stretch x5 (full moves) | 5 | 5 |
| atMiddle | event | Stretch x5 | 5 | 5 |
| copyMe | how | Stretch x5 | 1, then silent | 1 (4 silent) |
| freeze | event | Stretch x5 | 5 | 5 |
| atHigh / atLow | event | High, Low, High, Low, High (idle) | 3 / 2 | 3 / 2 |
| move names, atX, freeze | event | Surprise x5 | 5 each run | 5 runs, all called; copyMe silent after 1 |
| upDown, atHigh, atMiddle, atLow, freeze | event | Up and down x1 | in order H, M, L, M, H | upDown, H, M, L, M, H, freeze, each on its count |
| zigzag | event | Zigzag tile x5 | 5 | 5 |
| skip | event | Skip tile x5 | 5 | 5 |
| straight, walk, ribbon | event | Go x5 | 5 each | 5 each |
| askPath | how | 3 wrong path answers, then right | 1, then silent | 1 (4 silent) |
| askLevel | how | 2 wrong level answers, then right | 1, then silent | 1 (3 silent) |
| wrong | event | 5 accepted wrong answers | 5 | 5 |
| rightPath / rightLevel | event | 2 rounds solved | 2 / 2 | 2 / 2 |
| wMystery (after Next) | how | Next x2 | spoken once if never heard | 0: dropped stale both times (finding 2) |
| surprise | event | Surprise path x5 | 5 | 5 |
| firstX / thenX | event | Surprise path x5 | 5 sequences | 5 sequences, names match the drawn parts |
| danceIt | how | Surprise path x5 | 1, then silent | 1 (4 silent) |
| walk, doneDraw | event | Dance it x5 | 5 / 5 | 5 / 5 |
| wDraw | how | Clear x5 | 1, then silent | 1, then silent |

Stale lines (gap 0.2 s): Stretch, Twist, High, Pathways, Curved, Clean floor: the dropped move call goes `hush`, the
Paths welcome plays, Curved follows it in order; nothing from Levels plays after the mode change. Go, Zigzag, Go,
Gallop, Mystery: old `walk` calls dropped (`hush`), Mystery welcome plays. Surprise path, Surprise path, Clear,
Surprise path, Levels: every part-name sequence and danceIt dropped (`newer`, `chain`, `hush`), Levels welcome plays.
Right path answer then Levels 150 ms later: rightPath cut, Levels welcome next. No stale line found except finding 3.

First tap (fresh page each): stage tap, welcome at about 50 ms after the tap; Pathways mode button, its welcome; Read,
the hint only; Sound, nothing; Sound off then on, the welcome once; Zigzag tile, only "A zigzag pathway."; Go (a
`speaks` button), only its call; Stretch, only its call (welcome skipped unmarked, it plays on the next mode entry);
a first drag in Draw, only the part names and danceIt; first key (Tab), the kit's welcome, then Enter on Pathways
cuts it for the Paths welcome. All as the brief expects.

Read: Read during "Middle level..." drops the rest of the call and reads the hint; the move goes on and freeze still
plays. Read with Sound off speaks the hint. Read then a mode change: the next welcome starts at once.

Order: in every log the spoken lines follow the order of the actions.

## Findings

1. **should fix, general.** Header buttons are under the K-2 60 px target. src.html:45-46 and the kit header: mode
   buttons, Motion, Sound and Read measure 52 px tall at 1280x720, 1366x768 and 1920x1080, and 48 px tall at
   1000x625, 800x500 and 680x425 (where the mode buttons are 54x48). Only under 560 px wide do they reach 60 px.
   Spec "targets are 60 px or more"; handoff says the same. Seen with a measure script over every visible button in
   all four modes (frames `f1/m*.png`). Better: min-height 60 px for `.seg button` and `.icon-btn` at every layout
   (compact can drop the h1 or tighten padding to make room).
2. **should fix, general.** After Next in Mystery the waiting moment names the wrong control. src.html:690-696:
   `nextRound` queues `V.how('wMystery', {valid: () => M.step === 'go' && !state.busy})` right after
   `newRun('return')`, so `state.busy` is true when it comes up and it is dropped stale every time (log
   `wMystery dropped stale` at both Nexts). A stale line does not set the hint, so after the dancer walks back the
   hint still reads "Yes! That's the level. Tap Next for a new mystery." while Next is disabled and Go is the action;
   Read then speaks "Tap Next" too. Frame `outH/mys_after_next.png`. Better: queue the round's how-to after `walkTo`
   ends (as `playAgain` does), or set the hint to the Go step at once.
3. **should fix, general.** Coming back to Mystery (or Sound off and on) mid-round plays the "Tap Go" welcome when Go
   is disabled. src.html:274 and 991-992: the mystery welcome entry is `['wMystery', {valid: () => !state.busy}]`, with
   no check of the step. Run: first tap Go (welcome skipped unmarked), watch the trip, switch to Levels and back:
   "The magic floor hides the pathway. Tap Go, watch the dancer..." is spoken and becomes the hint, at step `path`,
   with Go `aria-disabled`; the askPath hint (which pathway, tap the answer) is replaced. Same after Sound off and on
   (`mys_return`, `mys_soundonoff` logs). The same gap applies to `wPaths`/`wDraw` in principle, but there the line
   stays true. Better: `valid: () => !state.busy && M.step === 'go' && !M.gallery`, `needs: '#y-go'`, so the how-to
   for the current step (askPath or askLevel) plays instead.
4. **should fix, general (the tool's own path rule).** A smooth drawn arc is split into straight and curved parts.
   src.html:762-783 (`bendParts`, the handoff's added "straight run split off a curve" rule). `__tool.analyze` on a
   half-sine arch from the star to x 90 (rise 30) gives "straight + curved + straight"; an S-curve gives
   "straight + curved"; a real drag of a rainbow arch (`f_drag`) was spoken "First, straight. Then curved. Then
   straight." A semicircle and a shallow arch come out curved, the line straight, a 3-corner zigzag zigzag, a tiny
   line tooShort. Done when 5 says "a smooth arc is curved"; a child or teacher who draws one rainbow hears three
   parts, two of them wrong. Better: only split off a straight run whose turn into the curve is a visible bend (or
   require the run to be much straighter than the curve's average curvature, not just within 0.6 units), and add the
   sine arch and S-curve to the builder's classifier tests.
5. **polish, general.** `rightLevel` ("Yes! That's the level. Tap Next for a new mystery.") is an event, so its how-to
   half is spoken all 7 times. Fine as the spec has it; a shorter event ("Yes! That's the level.") plus a how-to
   "Tap Next for a new mystery." (spoken once, hint after) would follow the don't-nag rule more closely.
6. **polish, general.** After a Pathways trip the hint rests on "Look at the floor! The ribbon shows our pathway."
   (`r_paths_go5`), which names no next action; same after Dance it ("Great dancing! Draw a new one, or dance it
   again." does name actions, so Draw is fine). Better: a silent how-to after the ribbon line that sets the hint to
   "Pick a pathway, then tap Go." Read then says what to do.
7. **polish, family:dance.** The Mystery round dots sit across the top-right corner of the mirror frame
   (`outH/mys_after_next.png`); they read, but they would sit cleaner on the wall above the mirror or in the panel.
   (The mirror strip is the engine's studio layout, so siblings using `studio` will meet the same corner.)
8. **nit, family:dance.** docs/families/dance.md does not list `Dance.flat`, `Dance.skeleton`, `Dance.shade` or
   `Dance.heard`, which the engine exports (kit/dance.js:901-903). Either document them or keep them internal.
9. **nit, family:dance.** The spec's engine section says facing can be "front, three-quarter, side, back, or any
   angle"; the engine takes degrees only (plus 'travel' and 'front' in `phrase`). The doc says degrees, so the doc is
   right; worth a line in dance.md (0 front, 90 the dancer's left, 180 back) for siblings.
10. **nit, general.** In the narrow header (under 900 px) the mode buttons show only an aria-hidden emoji, so their
    accessible name comes from `title` alone ("Levels (key 1)"). Works; an `aria-label` would be steadier.
11. **nit, general.** At 760x900 (stack) the Levels move grid and the Pathways level row are below the fold
    (bottom 999 to 1082 px); Go-row buttons come first, as designed. The Play lens may want the move grid first in
    Levels, since moves are the main control there.

Frames and logs: scratchpad lens-lp-craft (`f1/m*.png` sizes, `outA` to `outI` voice and access runs, `v?.log`).
