# Craft lens: levels-and-pathways (round 1)

Cold Craft lens on the CURIO_DRAFT=1 bundle (946 KB). Frames and logs are in
`<scratchpad>/refine/levels-and-pathways/craft/` (folders A, B, C, D, E; shots files shotsA to shotsD; resize_check.py).
The shared audit (audit-r1) was read, not re-run.

Counts: blockers 0, should fix 2, polish 2, nit 4.

## Findings

### Should fix

1. **Draw a path, small sizes: badge leader lines tangle across the path and each other.** (general)
   Where: Draw a path, `drawParts()` leader routing (src.html about 2383 to 2396), at 680x425 (the tool page preview)
   and 375 wide. What: with a four-part path, badges 1 to 4 are stacked up on the back wall and their thin black
   leaders run as long elbows and boxes that cross the drawn pathway and each other; it is not possible to see which
   badge belongs to which part, which is the whole point of the numbered badges. At 1366x768 the same path is clean
   (short leaders, one per side). How seen: audit frames `state-four-part-drawn-path-680x425.png` and
   `state-four-part-drawn-path-375x812.png`, zoomed in `craft/zoom-4part-375.png`; compared with the 1366x768 frame.
   Better: when a leader cannot be short and clear, put the badge on the part (or number the part itself on the line)
   rather than routing a long leader; a leader should never cross the ribbon line or another leader.

2. **Painted dancer rig: low-level shapes show cut-out seams.** (family:dance)
   Where: `paintDancer()` puppet pieces (src.html 804 onward) with the kit poses, Levels and Pathways at Low. What:
   at Low the articulated painted pieces read as separate flat strips: the low stand at the end of a Low trip has both
   forearms hanging as detached rectangles from the shoulders to below the knees, with green fringe left at the
   fingertips; kneeling Bend and Twist at Low show the thighs as two blunt boxes with cut ends and a forearm strip
   sticking up behind the shoulder. On a projector this looks broken, and Low is the level the class copies most
   carefully. Middle and High shapes read well. How seen: audit `state-ribbon-finished-1366x768.png` (zoom
   `craft/zoom-lowstand.png`), my `D/M3-low-skip-end-1366.png` (zoom `craft/zoom-m3.png`), `D/M4-updown-mid.png`
   (Up and down at Low, Bend), `D/M6-low-twist-1366.png`, and `D/M2-low-walk-mid-1920.png` (low gallop mid-stride,
   torso and leg pieces visibly out of joint). Better: fix the low-stand arm pose (hands on knees, elbows bent) and
   the kneel joints so pieces overlap at the joints, and re-despill the hand edges.

### Polish

3. **The tool queues an empty "barrier" line in the voice queue.** (general)
   Where: `newRun()` (`V.say('', {now:true, valid:() => false})`, src.html 1517) and `afterRead()` (693, plus the
   `readUntil` polling for Read with Sound off). What: every new action logs an event line with no text as
   "dropped, stale". It works (no line was lost in my runs), but it bends the kit instead of using it, and it fooled
   the audit into reporting "Stretch: event line lost, spoken 0 of 5, dropped 5: stale" when Stretch was in fact
   spoken 6 of 6 at a 2 s pace (`A/A3-rep-stretch-2s.json`). Better: use `V.hush()` / `V.dropQueued()` and a kit
   way to wait for Read (or add one to the kit), so the log holds only real lines.

4. **Part badges sit inside an SVG with `role="img"`.** (general)
   Where: `#sv role="img"` (src.html 209) holds the `.part` badges with `role="button"`. What: children of an img
   role are presentational, so a screen reader does not expose the part buttons or their good labels ("Part 1,
   zigzag, low level. Change its level"). Keyboard use works (Tab reaches them, Enter cycles the level, focus ring
   shows: `D/K3-draw-keyboard.png`, `D/K4-draw-keyboard-enter.json`). Better: put the badges in a group outside the
   img role (or drop the role from the stage and label the scene another way).

### Nit

5. **Tab order differs from the visual order in Levels at 1366x768.** (general) Up and down and Surprise show first
   (`.go-row{order:-1}` in `wide.short`), but Tab reaches High, Middle, Low first (`D/K2-tab9.json`: the 9th Tab is
   Middle). Harmless for a teacher, but the order could match.
6. **Tapping a part badge speaks "Low level. Get close to the floor." while no dancer is on stage.** (family:dance)
   `cyclePart()` uses the same level line as Levels (`A/A5-rep-part.json`, 5 of 5 spoken, correct as an event). In
   Draw a path nobody is dancing yet, so "Get close to the floor" asks the class to move before Dance it. A short
   "Part 1, low." style line would fit the moment better.
7. **Stale art entries.** `art/prompts.json` still has 31 `dancer-*` entries (people: true, deferred: false, no
   art) marked superseded by painted-dancers; no `art:` token uses them. Remove or mark them deferred so tools and
   checkers do not count them as pending people art.
8. **Spec Voice table is out of date.** spec.md lists wDraw as "Draw a pathway on the floor with your finger. Start
   at the star. Then tap Dance it." and has no rows for clean, clear, returnStar, chooseMove, pathReady; the code and
   lines.json agree with each other (see Lines below), so only the spec needs the update. The spec's "Art: none,
   people: false" also no longer matches the painted cast.

## Checks that passed

**Contract.** One file, 946 KB (under the 2 MB goal). No network requests: no fetch, XHR, import(), links,
WebSocket or http URLs in the bundle (the `voice:*` clip token is left for the voice step, expected). Kit used:
`Curio.voice`, `kit/dance.js` (clock, music, trails, readPath, floor), kit Motion, Sound, Read. No console errors or
exceptions in any of my 33 driven shots or in the audit.

**Access.** Every control 60 px or more at every STANDARDS size (audit sizes and states clean; part badges have a
64 x 64 hit area). Visible focus on tiles, mode buttons and part badges (`D/K2-tab9.png`, `D/K3-draw-keyboard.png`).
Keyboard: Tab reaches modes, Motion, Sound, Read, then the panel; Draw a path is fully usable from the keyboard
(Surprise path, then Tab to a part badge, Enter cycles its level). Nothing takes focus on load (`D/K1-tab1.json`:
first Tab lands on Levels). Color is never alone: level buttons carry cloud, table and grass glyphs and words;
ribbons differ by pattern (dotted prints, solid, wide stripes) and end badges; Mystery right answers get a star.
Motion off: no endless animation (audit), the move keeps its count-in and timing (`D/M1-calm-mid-move.png`). Sound
off then on brings the skipped welcome once; Read works with Sound off.

**Resize lead checked.** The audit's "#d-surprise ... left disabled" lead is a random-path artifact: with a seeded
Surprise path, the enabled controls before and after a 1366x768 to 760x900 and back resize are identical, and no
exception fires (`resize_check.py`, `E/`).

**Lines.** All 47 strings in `L` equal `voice/lines.json` word for word and in order; `__tool.allLines()` returns 47.
Hints are set from the same strings (composite move hints "Stretch! Middle level. Stay in the middle." are the two
lines joined). No line names a disabled or hidden control in any run (askPath, askLevel, nextHow, wMystery and
danceIt carry `needs`).

**Art.** Every `art:` token in src.html (sunlit-studio, painted-dancers, painted-gallery-bow) has a prompts.json
entry; the two people images are `people: true`, drawn by Codex with a fresh review note (rule 11). No local-model
people.

**Words.** No em or en dashes in src.html, notes.md, lines.json, prompts.json or spec.md; "Curio Class" never
"Curio" alone; classroom-safe. Privacy: nothing is saved; notes say the shared Motion setting is kept on this device.

## Standard voice check

Driven with `scripts/drive.py`, held clicks (0.12 s), Sound and Motion on, 1366x768, logs from `__tool.vlog`.

### 1. Repeats (each action five times in a row, gap longer than its lines)

| line | kind | expected | spoken | run |
|---|---|---|---|---|
| atHigh (tap High) | event | 5 | 5 | A1, gap 4 s |
| chooseMove "Tap a move, and copy the dancer!" | how | 1 | 1 (4 silent) | A1 |
| stretch | event | 5 | 5 | A2, gap 15 s |
| atMiddle (move call) | event | 5 | 5 | A2 |
| copyMe | how | 1 | 1 (4 silent) | A2 |
| freeze | event | 5 | 5 | A2 |
| wLevels (after a move ends) | how | 1 | 1 (3 silent) | A2 |
| skip (way) | event | 5 | 5 | A6, gap 4 s |
| zigzag (pathway) | event | 5 | 5 | A6 |
| pathReady "Tap Go, and follow the dancer!" | how | 1 | 1 (9 silent) | A6 |
| straight, walk (Go call) | event | 5 each | 5 each | B1, gap 22 s |
| ribbon | event | 5 | 5 | B1 |
| wPaths after a trip | how | 0 more | 0 (silent or dropped) | B1 |
| rightPath | event | 5 | 5 | B3, five rounds |
| rightLevel | event | 5 | 5 | B3 |
| askPath, askLevel, nextHow | how | 1 each | 1 each (4 silent) | B3 |
| returnStar | how | 1 | 1 (3 silent) | B3 |
| wMystery after Next | how | 0 more | 0 (4 silent) | B3 |
| wrong | event | every accepted wrong | 3 of 3 accepted | B2 (taps 2 and 4 landed during the replay, when the answers are rightly disabled) |
| surprise (path) | event | 5 | 5 | A4, gap 7 s |
| part names (firstX, thenX) | event | every path | every path (13 of 13) | A4 |
| tapPart | how | 1 | 1 (4 silent) | A4 |
| danceIt | how | 1 | 1 (silent after) | A4, A5 |
| atLow/atHigh/atMiddle (part badge) | event | 5 | 5 | A5 |
| stretch at a 2 s pace | event | 6 | 6 | A3 (audit's "0 of 5" was the empty barrier line, finding 3) |

### 2. Stale lines

Fast taps 0.35 s apart: Stretch, Twist, Low, Surprise, Pathways, Curved, Go, Clean floor (`C/S1`); and Draw a path,
Surprise path, Low, Dance it, Surprise path, Mystery path, Go, Levels (`C/S2`). Every line was either cut by the next
action or dropped as newer, hush or chain; no Levels line played after Pathways opened, no part names after Low, no
Mystery line after Levels. The last line in each run matched the screen (clean; wLevels).

### 3. First-tap timing (fresh page each)

| first tap | heard | ok |
|---|---|---|
| the stage | wLevels within 0.14 s | yes |
| Stretch (own line) | Stretch! / Middle level, then copyMe; wLevels after the move ends (17 s) | yes |
| Pathways mode button | wPaths within 0.12 s | yes |
| Read | the hint only, no welcome after | yes |
| Sound | nothing; Sound back on 3 s later brings wLevels once | yes |
| a key (Tab) | wLevels | yes |
| High (own line), then Sound off and on | atHigh, chooseMove; wLevels once on Sound on | yes |
| mode entries Draw, Mystery, Levels | wDraw, wMystery, wLevels, once each | yes |

### 4. Read

Read during "Twist!" cut it at once and spoke the hint; the move's next line waited for Read (`C/R1`). Read with
Sound off spoke (`C/R2`). Mode change right after Read started wMystery 0.13 s after the tap (`C/R3`). Read during a
trip did not stop the trip; ribbon followed at the trip's end (`C/R4`).

### 5. Order

In every log the spoken lines follow the taps in order; no older action's line followed a newer one.

**Voice check verdict: counts right.**

## Audit pilot

**Leads confirmed:** none of the 13.

**Leads that were wrong:**
- "Welcome not heard" after a first tap on High, Middle, Low, the six moves, Up and down and Surprise (11 leads):
  these controls speak their own line, which is what REFINE step 3 asks for; the premise is not lost, because the
  tool queues wLevels when the first move ends (`C/F2`, 17 s) and Sound off and on brings it (`C/F7`).
- "Stretch: event line lost, spoken 0 of 5, dropped 5: stale": Stretch was spoken every time (6 of 6 at 2 s,
  `A/A3`); the dropped entries are the tool's empty barrier line (finding 3).
- "#d-surprise left disabled after resize": the missing name was a part badge label from a different random path;
  a seeded rerun shows identical enabled controls and no exception.

**What it missed:**
- The leader-line tangle in Draw a path at 680x425 and 375 wide (finding 1): its check for lines drawn across labels
  passed, but leaders crossing the path and each other are not checked.
- The painted rig's seams at Low (finding 2): art and pose quality are outside what it can see.
- The SVG `role="img"` wrapping the part buttons (finding 4).
