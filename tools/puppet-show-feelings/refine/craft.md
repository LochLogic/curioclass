# Craft lens: puppet-show-feelings (round 1)

Cold Craft lens, 2026-11-05. Bundle `tools/puppet-show-feelings/puppet-show-feelings.html` as built (not re-bundled).
My frames and logs: `S:/CurioClass-codex-scratch/puppet-show-feelings/craft/f1/` and `f2/` (shots1.json, shots2.json
beside them). Shared audit: `S:/CurioClass-codex-scratch/puppet-show-feelings/audit-r1/audit.md`.

## Findings

### should fix

1. **Backstage, Line 5 is a dead line: Pom never babbles, and the narrator names a control that is not there.**
   Where: src.html:401 (scene 5 `n:0`), src.html:822-835 (`#line` cycles all six, index 4 included), src.html:689 and 819
   (babble uses `scenes[state.line].n`). What: `Line` reaches "Line 5", the narrator says "What happens next? Tap an
   ending." and the hint reads "What happens next? Tap an ending. Tap Say it." in Backstage, where there are no ending
   buttons. On that line every change and `Say it` babble 0 syllables, so the Voice row (Slow, Middle, Fast) has no
   effect you can see or hear, `Say it` does nothing, and Done when 3 fails there. How: `f1/c-line5` log (line spoken,
   hint as quoted, babbleLog empty) and `f1/c-line5-change` (babbleLog `[..,0,150],[..,0,150],[..,0,95]` for Head,
   Say it, Voice; frame shows Pom silent). Better: skip scene 5 in the Line cycle (five lines: four scenes and the
   chosen ending), or give it real babble and a line that does not name the endings. Tag: general.

2. **Following the first hint skips the welcome and all of scene 1; a first tap on Show me gives the answer first.**
   Where: src.html:451-454 (`speaks` includes `#next, #back, #again`), src.html:881-883 (only a tap on the theater
   starts scene 1), src.html:886 (first hint "Welcome to the puppet show! Watch Pom. Then tap Next."). What: nothing
   plays on load; Pom bobs silently. A child doing what the hint says (tap Next, or press the right arrow) jumps to
   scene 2: the welcome is never heard and scene 1's line and question are never spoken. A first tap on `Show me`
   speaks only "Pom feels happy." with no welcome and no scene. Only a tap on the painted stage plays the intended
   opening (welcome, then scene 1 about 4.4 s later, babble, question). How: audit table rows 6-9 ("not heard" for
   Show me, Back, Next, Again), confirmed on my own runs: `f2/c-first-key` (ArrowRight: only "Whoosh!"),
   `f2/c-first-reveal` (only "Pom feels happy."), `f2/c-first-stage2` (stage tap: welcome, scene line, question).
   Better: on the first tap of Next/arrow/Show me, play scene 1 (welcome, line, babble, question) instead of
   advancing, or have the welcome and scene 1 start on the first tap anywhere. Tag: general.

3. **Backstage's key teaching line arrives about 4 s after the tap and is cut by the action the hint asks for.**
   Where: src.html:690 (`flip` queued only after the babble finishes), src.html:694-696 (the first change waits for the
   "Say a clue" line before it babbles). What: on the first change the sequence is "Say a clue. Tap Audience says."
   (about 2.9 s), then the babble, then "Only one thing changed, and the feeling changed!". A teacher who taps
   Audience says, as told, at a 4 s pace cuts the flip line after about 0.3 s; it is logged as spoken and is silent
   for the rest of the page load. The first change's babble also waits about 3 s behind the how line (Done when 4,
   "acts at once", only half holds: the pose moves at once, the voice does not). How: `f1/c-back-aud5` log: flip
   spoken at 9320, "The audience sees worried." at 9651, then flip `silent` at 14762, 23101, 31371; `f1/c-back-head5`
   babbleLog first entry at 9415 for a tap at about 6.4 s; `f2/c-keys-back` shows the same cut (flip spoken 8270,
   next flip dropped). Better: say the flip line right after the change (before or instead of the babble), or let it
   come back when it was cut early. Tag: general.

### polish

4. **Bounce icons Small and Big read as the same mark.** Where: src.html:778 (`'⌒'`, `'◠'`). What: at 1366x768 both
   are a thin arc of almost the same size; the spec asks for a small arc and a big arc. The Head icons (a pair-of-socks
   emoji rotated 28, 0 and -18 degrees) also barely show a tilt. How: `craft/zoom-controls.png` (crop of
   `f1/c-line5-change`). Better: drawn SVG icons (a low and a tall arc; one sock drooping, straight, lifted), like
   the drawn feeling faces. Tag: general.

5. **"What changed" row is 14 px (12 px in the short layouts), plain text arrows.** Where: src.html:120, 178, 258,
   682. What: the spec calls for icon arrows; on a projector for K-2 the row is unreadable from the back of a room.
   How: `audit-r1/state-backstage-audience-1366x768.png` (bottom of the console). Better: 18 px or more with the
   row's icons ("sock Down to sock Up"). Tag: general.

6. **Dot is mostly hidden in the Dot helps ending.** Where: src.html:55 (`.dot { left:0 }`) inside the clipped puppet
   window. What: Dot sits at the window's left edge behind the tied curtain; only an eye patch and part of the body
   show, and the stick floats across Pom's face. How: `audit-r1/state-ending-0-1366x768.png`. Better: move Dot in
   from the curtain (about left 12 to 18 percent) so both puppets read. Tag: general.

### nit

7. Try it and Ending vote, when on, show a thick border and tint but no check mark (spec: chosen controls show a check
   icon). src.html:357, 378; `audit-r1/state-backstage-match-680x425.png`, `state-like-vote-1366x768.png`. general.
8. At 680x425 the chosen mode button wraps to two lines ("✓ ☷" over "Backstage"). src.html:36 and 150;
   `audit-r1/state-backstage-match-680x425.png`. general.
9. At 375 wide the audience card sits flush on the stage's right edge (`right:0`, src.html:260).
   `audit-r1/state-backstage-audience-375x812.png`. general.
10. `#dots` has an `aria-label` on a plain div (no role), and the mode buttons' emoji are read aloud by screen readers
    ("performing arts Show"). src.html:286-288, 318. general.
11. Spec drift in words, settled in notes for one of them: the after-change line is "Say a clue. Tap Audience says."
    (spec: "What do you see now? Say it. Then tap Audience says."), the Like me prompt is "Tell Pom, or pass." (spec:
    "Tell a friend."; notes.md explains it, fine). Art was drawn with gpt-image (prompts.json `source`, src.html:11),
    not the local FLUX route the spec names. Worth a line in the spec or notes so later agents do not "fix" them back.
    general.

## Checks that passed

- **Contract:** one file, 1,188,058 bytes (under the 2 MB goal); no `http` URL anywhere in the bundle; no resource
  requests after load (`performance.getEntriesByType('resource')` empty, `f1/c-contract`); kit used (`Curio.voice`,
  `Curio.init`, kit css); no console errors or exceptions in any of my 24 shots or in the audit.
- **Frame times:** 240 frames at 1366x768, median 16.7 ms, p95 16.8 ms in Show and 16.7 ms in Backstage on Big bounce
  and Fast voice (`f2/c-fps-show`, `f2/c-fps-back`). Headless Chrome with GPU off; 60 fps held.
- **Ease:** Head Up to Down eases -18 to 28 degrees in about 250 ms (`f2/c-ease`), matching the spec.
- **Motion off:** body gets `calm`, kit sets transitions and animations to 0.01 ms; kite moves 0 px over 500 ms between
  scenes, breeze has no animation (`f2/c-calm-kite`); the new-kite unfold resolves at once (`f2/c-calm-ending1`).
  Audit "Motion off" row clean.
- **Access:** focus ring 4 px solid #9638a9 on Tab (`f1/c-tab`); every tool control 60 px tall (audit, every size;
  `f2/c-like-sizes`); H, V, B step the rows and A shows the audience card (`f2/c-keys-back`); arrows move scenes in
  Show; chosen Head/Voice/Bounce and feeling cards show a check and thick border; feelings always pair face and word.
  Contrast recomputed: white on brand 5.30, muted on panel 6.25, changed row #4d5f55 on #f7edda 5.86, gold text 9.53.
- **Lines:** `allLines()` (115) and `voice/lines.json` (115) match word for word, no line on either side only.
- **Art:** all 10 `art:` tokens have prompts.json entries, all `people: false`; no people in any picture.
- **Words:** no em dash in src.html, notes.md, lines.json, prompts.json; "Curio Class" never shortened; nothing stored
  but the kit's Motion preference, which the Motion button's title and notes.md both state.

## Standard voice check

Held clicks (0.12 s), Sound and Motion on, 1366x768.

| line | kind | expected | spoken | run |
|---|---|---|---|---|
| Welcome (Show) | how | once, on first plain tap | once (stage tap); never on first Next/Back/Again/Show me/arrow | f2/c-first-stage2, f2/c-first-key, audit |
| scene lines | event | every scene | 5 of 5 | f1/c-show-next5 |
| How does Pom feel? | event | every scene | 5 of 5 | f1/c-show-next5 |
| Welcome (Backstage) | how | once | once | f1/c-back-head5 |
| Say a clue. Tap Audience says. | how | once in 5 changes | 1, then hint only | f1/c-back-head5 |
| Only one thing changed... | how | once | 1 (cut after 0.3 s when Audience tapped), then silent | f1/c-back-aud5 |
| The audience sees X | event | 5 of 5 | 5 of 5 | f1/c-back-aud5 |
| Make Pom look X | event | each new target | 7 of 7 | f1/c-try6 |
| Yes! That's X! | event | every target met | 6 of 6, all six targets cycled | f1/c-try6 |
| Welcome (Like me) | how | once | once | f1/c-like5 |
| When did you feel X? | event | 5 of 5 | 5 of 5 | f1/c-like5 |
| Tap the ending you like. | how | once | once | f1/c-like5 |
| ending vote lines | event | 5 of 5 | 5 of 5 | f1/c-like5 |

- Stale lines: three Next taps 0.2 s apart, then Backstage, then Show: each line cut by the next, nothing played after
  its moment (`f1/c-stale`). Line 5 in Backstage names absent ending buttons (finding 1).
- Read during a line stops it and speaks scene line plus hint (`f1/c-read-during`); Read with Sound off speaks
  (`f1/c-read-soundoff`). Sound off then on brings the skipped welcome once (`f1/c-first-sound`). Sound alone says
  nothing (audit row 2).
- Order: lines followed the actions in every run.

## Audit pilot

- **Leads confirmed:** the four "welcome not heard" rows (Show me, Back, Next, Again): confirmed and widened to the
  arrow key and to scene 1 being skipped (finding 2).
- **Leads wrong or harmless:** "#next: event line cut (hush) and never heard whole: Whoosh!" is the intended
  behaviour (a new Next tap cuts the old scene, spec "a tap during a line stops it and goes"; the newer scene's line
  plays). The audit's note "this one has 0 modes" is wrong: the tool has three mode buttons.
- **Missed:** the audit walked only the ten Show and header controls, none of Backstage's (Head, Voice, Bounce, Say
  it, Line, Audience says, Try it) or Like me's, so it could not see the dead Line 5 (finding 1) or the cut flip line
  (finding 3). Also icon legibility (finding 4), the hidden Dot (finding 6) and missing check marks on toggles (7).
