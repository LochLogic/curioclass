# Craft lens: poets-workbench (Curiosity No. 10), round 1

Cold Craft lens, 2026-11-05. Judged against REFINE.md (Craft), STANDARDS.md, BASELINE.md and CODEX-CURIOSITY.md
(the look rules). Bundle `tools/poets-workbench/poets-workbench.html` as built (1,603,263 bytes). Own frames in
`S:/CurioClass-codex-scratch/poets-workbench/craft/frames/`; throttle script and shot lists beside them.

Counts: blocker 1, should fix 5, polish 4, nit 3.

## Findings

### 1. Rhyme drawer offers slurs as rhymes for everyday words (blocker, general)
- Where: `src.html:287-290` (`BLOCKED`), `rhymeList` at `src.html:581-596`; rhyme drawer, every kind.
- What: the block list covers only the worst words. The CMU dictionary keeps many slurs and explicit words, and
  the drawer shows them as rhymes for words a grade 7 (or a K-2 class on a projector) will tap first:
  "moon" lists coon, coons, spook(s), redskin, douche; "like" and "bike" list dyke, dykes, gook, polack;
  "map" lists jap, japs, crap, rape, wop; "top" lists wop, darkie, nazi; "hit" and "pick" list tit, tits,
  prick, redskin, niggard. "coon" sits 14th in the default Perfect list for "moon", in the common-words tier
  (SCOWL puts it in size 50 and above), so it is on screen without scrolling.
- How seen: `frames/moon-drawer.png` (coon visible in the first rows), `frames/like-drawer.png`; the `words` and
  `rhyme-moon` checks in `s2.json` (72 of 100 test words are in the dictionary; 13 common words each surface
  at least one).
- Better: filter the rhyme index with a real classroom list (slurs, ethnic and sexual terms, explicit words), not
  a hand list of about 70; check "moon", "like", "map", "top", "hit", "late" and "pick" after. Rule 6.
  "redskin", "squaw" style entries are Native slurs: route the final list past the sensitivity agent.

### 2. Long poems drop well below 60 fps while typing (should fix, family:curiosity)
- Where: `render()` at `src.html:450-522` re-scans every line (four feet, every offset, every variant) and
  rebuilds the whole mirror `innerHTML` 60 ms after each keystroke.
- What: one render of The Raven (126 lines) costs about 20 ms on this desktop and 131 ms at 4x CPU throttle (a
  modest Chromebook); Paul Revere's Ride 92 ms. Typing into a loaded Raven at 4x: 61 of 208 frames over 33 ms,
  p95 122 ms, max 154 ms. Unthrottled it is already 24 of 394 frames over 33 ms (p95 34.5 ms). Frost's one line
  is fine (p95 20 ms). The dictionary load also takes 3.9 s at 4x (319 ms unthrottled); its 9 ms chunks keep
  frames smooth, so that part is fine.
- How seen: `scripts/throttle.py` + `scripts/t.js` (CDP `Emulation.setCPUThrottlingRate` 4) and the `typing`
  shot in `s2.json`.
- Better: cache `scanLine` per line text and lens (the overrides key is per line already) and patch only the
  changed `.verse` node; the shelf exists to load long poems, so this is the path students take.

### 3. Tapping a stress mark does not flip it; it opens the rhyme drawer (should fix, general)
- Where: `.proof` buttons in `#mirror` (`src.html:84-88`, handler `src.html:928-936`) sit under `#editor`
  (`src.html:75`, later in the DOM, same stacking level; the mirror's `transform` makes its own stacking
  context, so `.proof{z-index:3}` never lifts the marks above the textarea).
- What: `document.elementFromPoint` on the first mark returns `editor`. A real click on the "/" over "woods" put
  the caret in the word and opened the drawer for "woods"; the mark stayed "/". The spec's control ("Tap a stress
  mark"), Things to do 5 and the Manual ("Tap a mark ...") all promise it. The Stress key and Alt F do work.
- How seen: `frames/proofclick-after.png`; `proofclick` shot in `s2.json` (`topEl: editor`, before x, after x,
  drawer true).
- Better: give `#mirror` a z-index above the editor with `pointer-events:none` kept on everything but `.proof`,
  or drop the promise from the Manual and spec.

### 4. Alliteration underline uses the same green as rhyme family B (should fix, general)
- Where: `.word.allit{border-bottom:2px solid #2d6a3e}` (`src.html:82`) and `COLORS[1]='#2d6a3e'`
  (`src.html:275`) used for `.word.ending` underlines (`src.html:81`).
- What: with Sounds on, the end word of every B line carries a green underline that looks the same as an
  alliteration mark. In The Raven, "lore" (rhyme B) and "quaint", "curious", "forgotten" (alliteration) all
  show a green underline at once. Assonance is shown by colour alone (plum shading), and in long lines it
  shades nearly every word, so the overlay stops meaning anything.
- How seen: `frames/raven-sounds.png`.
- Better: draw alliteration as a distinct mark (a small bracket or dotted overline under the first letter, not an
  underline), keep green out of the rhyme inks, and give assonance a shape as well as a colour.

### 5. Read is a dead control on screen, and the Manual says otherwise (should fix, family:curiosity)
- Where: `$('read').onclick` at `src.html:1042-1050`; Manual text at `src.html:824-825`.
- What: with no clip (expected until the Forge voice pass, BASELINE rule 18), Read only sets the provenance line
  to the value it already has, changes the button's tooltip and sends "Type a line. The recorded hint is not
  supplied in this build." to the live region. After the first action the hint stays hidden. Nothing visible
  happens. The Manual says "Read shows and announces the hint as text", which is not true, and both the Manual
  and the screen reader text carry a build note a student should never meet.
- How seen: `read-after-typing` shot in `s3.json` (hint hidden before and after Read; `vlog` empty).
- Better: until the clip exists, Read re-shows the hint on the page for a few seconds and announces only
  "Type a line."; drop the "not supplied in this build" wording from Manual, tooltip and live region.

### 6. Alt R and Alt F do not work on a Mac (should fix, general)
- Where: `src.html:1028-1029` tests `event.key.toLowerCase()==='r'` / `'f'`.
- What: on macOS, Option+R gives `event.key` "®" and Option+F "ƒ", so neither shortcut fires (and the symbol is
  typed into the poem). The footer and the Manual advertise both. Found by reading the code; this PC cannot run
  a Mac keyboard, so not seen on a frame.
- Better: test `event.code==='KeyR'` / `'KeyF'`.

### 7. Motion has almost nothing to turn off (polish, family:curiosity)
- Where: only `@keyframes drawer-in` exists (`src.html:128`).
- What: the spec's typebar drop ("its marks drop in above it with a soft typebar clack") and Done when 7 ("Motion
  off removes the typebar and drawer animations") assume a mark animation that was not built. Typing gives a
  clack (Sound) but marks just appear. Not wrong, but the first-two-minutes moment is flatter than the spec.
- Better: a short drop of the new word's marks on word end, removed by `.calm`.

### 8. Click to edit a word reflows the whole desk twice (polish, general)
- Where: `editor` click handler `src.html:919-927` opens the drawer on any click inside a word; `edited()`
  (`src.html:535`) closes it on the next keystroke.
- What: at 1366x768 a click into "woods" moves the page 95 px left and narrows the editor by 50 px (text
  rewraps); typing a letter moves it all back. Fixing a typo costs two layout jumps. The audit's held click on
  the rhyme handle shows the same move (19 of 32 controls shifted).
- How seen: `clickword` shot in `s2.json` (`p0 293, p1 198, w0 848, w1 798`).
- Better: open the drawer over the desk edge without resizing the page grid, or open it on a second tap / the
  mark, not on every caret placement.

### 9. Slurs sit in plain text in the public bundle (polish, general)
- Where: `src.html:287-290`.
- What: the block list puts the slurs themselves in view-source of a K-12 page and in a public repo. Not on
  screen, so not a rule 6 failure, but easy to avoid.
- Better: ship the filtered dictionary (drop the words at pack time) or store hashes.

### 10. Sounds gives no readout when it finds nothing (polish, general)
- Where: Sounds key, `render()` `src.html:474-485`.
- What: on the opening Frost line, Sounds lights and nothing on the page changes (no repeats there). A student
  cannot tell an empty result from a dead key.
- How seen: audit `state-sound-repeats-1366x768.png`.
- Better: a readout in the top strip such as "repeats: 0 consonant, 0 vowel".

### 11. "stays on this device only when saved" reads as if unsaved text leaves it (nit, general)
- Where: `src.html:536`, the provenance line after the first edit.
- Better: "YOUR PAGE / not saved" (the Drafts dialog already says drafts stay on this device).

### 12. Doubled tempo control for assistive tech (nit, general)
- Where: `src.html:221-223`: the knob (`role=slider`, `tabindex=0`) and the range input are two tab stops and two
  sliders for one value, both inside one `<label>`.
- Better: keep the range input as the one control and mark the knob `aria-hidden`, or the reverse.

### 13. Drawer kind buttons mix tab and toggle roles (nit, general)
- Where: `src.html:253-255`: `role="tab"` with `aria-selected` and `aria-pressed` together.
- Better: drop `aria-pressed` on the tabs.

## Checks that passed

- Contract: one file, 1.60 MB (under the 2 MB goal); `performance.getEntriesByType('resource')` empty (no network
  requests); no console errors or exceptions in any of my shots; `check_tools.py` lists it as draft with no
  failure. Manual links open only on a person's click.
- Look rules: fills the screen at every size (audit size frames), no kit header, no welcome, score, goal or
  finish; readouts in Courier with units (lines, words, syllables, BPM, "8 of 8"); maker's plate "Curio Class
  Curiosities · No. 10 · Poet's Workbench" and Manual lower-left; Motion, Sound and Read on their own power panel.
- Access: 44 px desk controls; visible focus ring; dialog returns focus; shelf and rhyme lists use roving
  tabindex with arrows; Escape closes the drawer. Proof marks are 27 px tall but have the 44 px Stress key and
  Alt F as the equivalent (see 3 and 6 for where that equivalence breaks).
- Words: no em dashes in src, notes, lines or the bundle; "Curio Class" never "Curio" alone; privacy stated in
  Drafts ("Your drafts stay on this device.").
- Art: no `art:` tokens and an empty prompts list; the desk is drawn in CSS, as the brief asks.

## Standard voice check

One line exists, the first-run hint, and its clip is not recorded (deferred to the collective Forge pass, BASELINE
rule 18). `voice/lines.json` and `__tool.allLines()` match word for word: ["Type a line."]. `__tool.vlog` stayed empty
in every run, and the audit's held-click table shows nothing spoken on any control.

| line | kind | expected | spoken |
|---|---|---|---|
| Type a line. | how-to (first-run hint) | once on load, then on Read | 0 (no clip; Read announces text to the live region only) |

Repeats, stale lines, order: nothing to count. First tap: nothing speaks before or after any tap. Read: see 5.
Re-run this check when the Forge clip lands.

## Frames looked at

Own: `frames/moon-drawer.png`, `like-drawer.png`, `proofclick-after.png`, `raven-sounds.png`,
`raven-lens-iamb.png`, `clickword.png`, `read-after-typing.png`. Audit: `size-1366x768.png`, `size-680x425.png`,
`state-sound-repeats-1366x768.png`, `state-rhymes-375x812.png`.

## Audit pilot

- Leads confirmed: none as defects. "nothing changed" on Print is `window.print()` in headless Chrome; on the
  tempo knob it is a click that does not turn it (drag and arrows do); on The Owl and the Pussy-cat it was not
  re-checked (other books load fine).
- Leads wrong: `#editor` / `#hint` overlap at every size is by design (the hint is a pointer-events-none note on
  the page). "focus taken on load" is deliberate for a typing instrument and uses `preventScroll`. "hint out of
  view" in stress-key, playing-fast and rhymes is the hint correctly gone after the first action. Manual and
  drafts "text hidden under" rows are a modal dialog over the page. Sympathy "covered" and four books "off screen"
  are the shelf's scroll list.
- Missed: the slurs in the rhyme drawer (1), frame times on long poems (2), the stress marks being unclickable
  under the textarea (3: the audit clicks only listed controls, and the marks are `tabindex=-1` inside an
  `aria-hidden` mirror), the green clash (4), Read doing nothing visible (5; the audit row says "ok"), and the Mac
  shortcuts (6).
- Sensitivity: the slur filter (1) touches Native, ethnic and LGBTQ terms; the shelf content notes in notes.md
  (death, war, Hughes) are for the sensitivity agent, not judged here.
