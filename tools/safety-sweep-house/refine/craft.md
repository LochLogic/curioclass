# Craft lens: safety-sweep-house (round 1)

Cold Craft lens, 2026-11-06. Bundle `tools/safety-sweep-house/safety-sweep-house.html` as built (not re-bundled).
My frames and logs: `S:/CurioClass-codex-scratch/safety-sweep-house/craft/out1` (voice runs), `out2` (drags, ruler,
keyboard hold, fps, Escape), `out3` (drag-miss, House by key, ruler at the 3 ft label). Shared audit:
`S:/CurioClass-codex-scratch/safety-sweep-house/audit-r1`.

## Contract

- One file, 2,282,683 bytes: 46 inline webp images (2.19 MB of it), no audio. Over the 2 MB goal, under 6 MB, so no
  `Size:` line is required. No `http(s)://` anywhere in the bundle; no network requests seen in any drive run.
- No console errors or exceptions in 14 driven shots (drive.py "errors in 0 shots") or in the audit.
- Kit used: `Curio.voice`, `Curio.tone`, `Curio.yes`, kit header buttons, `Curio.onMotion`. Nothing re-implemented.
- Frame times (out2 `fps`): room open, hazard zoom, House, another room over 3.2 s: median 16.7 ms, p95 16.7,
  max 16.8 (headless, GPU off). Clean.

## Voice check

Driven with held clicks (0.12 s), Sound on, Motion on, at 2 s, 3 s, 0.6 s and 0.2 s paces (out1 `v-*.json`,
out2 `stale.json`). Headless speech never ends, so lines run to the kit's cap; that makes queues longer than real.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| roomIn (room entered 4 times) | how | 1 | 1, then silent 3 (v-repeat-look) |
| lookalike (look-alike tapped 5 times) | how | 1 | 1, then silent 4 (v-repeat-look) |
| stop, think, choose, fix, who (two hazards in a row) | how | 1 each | 1 each; second hazard all silent "heard" (v-full-kitchen) |
| tried (two hazards, two unsafe picks on the first) | event, once per hazard | 2 | 2 (v-full-kitchen) |
| safe (two hazards) | event | 2 | 2 (v-full-kitchen) |
| roomDone | event | 1 | 1 (v-full-kitchen) |
| welcome | welcome | after the first room tap's line, or skipped | played after roomIn when the student lingered (v-repeat-look, 9.9 s); skipped when a hazard opened first (v-full-kitchen); never comes when the first tap is a key, Read, Sound or Motion |

- Stale lines: at 0.2 s taps through look-alike, hazard, Think, Choose, peek, unsafe pick, House, another room and a
  hazard (v-fast), nothing played after its moment; "tried" was cut by House; later how lines went silent. Clean.
- Read: cuts the playing line and speaks hint plus card, with Sound off too (v-read 5.7 s); a room change after Read
  goes straight on. Clean.
- Order: always followed the actions. Clean.
- First tap: Read speaks the hint only, Sound and Motion say nothing, a room tap gets roomIn (audit table, confirmed in
  v-read and v-key-first). The welcome lost on a key, Read or Motion first tap is fine under BASELINE rule 16: its
  content is in the roomIn hint and the panel ("Find two hazards").
- `allLines()` returns the 14 lines of `voice/lines.json` word for word, same order (out2 `esc.json`).

## Findings

1. **Ruler labels sit off the marks the check uses** (src.html:144-150, 886-887, 1072). Mode: Hallway / Heater fix.
   The blanket's left edge moves on 275 to 792 px at 1366x768 (1 ft every 129 px), but the "0 ft".."4 ft" labels are
   spread with `justify-content:space-between` plus 12 px padding, so their centers land at 298, 416, 534, 651, 769.
   Drag the blanket's edge onto the "3 ft" label and the readout says "2.9 feet" and "Still too close"
   (out3 `ruler-2-9.png`); at 4 ft the edge is 23 px past the "4 ft" label. The tick under "2 ft" also cuts through
   its text. At 375 wide the labels crowd the ticks (audit `state-heater-ruler-375x812.png`). A measuring tool that
   disagrees with its own check misleads. Better: place each label absolutely at `d/4` of the ruler width, centered on
   its tick, and measure from the visible blanket edge, not the button's padded box. **should fix**, general.

2. **Keyboard focus is dropped to the page after House or Escape** (src.html:483-491). Enter on the stage's
   "⌂ House" button (out3 `house-key`) or Escape during a hazard (out2 `esc`) ends with focus on BODY: the fallback
   tries `#controls` (no button in house view), `#house` (gone) and `#rooms-small` (display:none at this size). A
   keyboard user must Tab from the top again. Better: fall back to `#nav-house` or `#room-0` in house view.
   **should fix**, general.

3. **Hint repeats "Tap Tell ..." on every grown-up-first fix** (src.html:549 with content.json `fix`). `hintFor()`
   builds "Tap Tell Dad first. " + `h.fix`, and five of the six adult fixes start "Tap Tell Dad." or "Tap Tell Grandma
   June," so the hint and Read say: "Tap Tell Dad first. Tap Tell Dad. When the towel is cool, drag it onto the hook
   across the kitchen." Same on Candle, Pills, Smoke alarm, Gummies and Lighter. Better: drop the prefix, or strip
   the leading "Tap Tell X." from `h.fix` there. **should fix**, general.

4. **The help rule names the heater blanket on every hazard** (src.html:360-361, 617, 435). After the Think answer the
   card and Read say "You may move a cool blanket away from heat without touching the heater." on the chat, the
   pop-up, the tub and the gate. The spec's rule line is general ("If you can make it safe without touching those,
   act now, then tell."). Words do not match the state. Better: the spec's general line, with the blanket sentence only
   on the Heater card. (Teaching may weigh what the rule should say.) **should fix**, general.

5. **Ruler hints speak to keyboard users only** (src.html:905, 1078). After a mouse or touch drag that stops short,
   the hint says "Move the blanket to 3 feet or farther, then press Enter" (out3 `ruler-2-9.png`), and the fix hint
   says "Arrow keys move it 6 inches" at 375 wide on a phone (audit `state-heater-ruler-375x812.png`). A drag already
   checks on release. Better: "Still too close. Drag it to 3 feet or more." and keep the keys note for keyboard focus.
   **polish**, general.

6. **A missed drag leaves a select that never updates the hint** (src.html:1049-1057). After a drop outside the target
   the click handler is swapped for one that only sets `selected`: the hint stays "Move the object into the marked
   target, or select it and tap the target." and a second tap no longer unselects. It does work (out3 `miss-real`:
   real click on the object, then the target, finishes). Better: keep the original toggle handler, which also sets
   "Now tap <target>." **nit**, general.

7. **The Safety card covers the hint at narrow and short sizes** (audit lead, src.html:240, 270). Confirmed at 680x425
   and 375x812 (audit `state-safety-card-680x425.png`, `-375x812.png`): the fixed card sits over the panel. The card
   carries its own Close and Sweep again, and Read still speaks the card, so nothing is lost. At 1366x768 the hint is
   visible (the panel is only inert); the audit's "every size" is wrong there. **nit**, general.

8. **Screen reader states are thin.** Peek buttons have no pressed or expanded state (src.html:634); the step strip
   has no `aria-current` on the current step (src.html:588-589); look-alike hotspots are named from file names
   ("medicine cabinet high", "pot back burner", src.html:819). Better: `aria-pressed` on peek, `aria-current="step"`,
   and plain names ("Medicine cabinet", "Pot on the stove"). **polish**, general.

9. **Line naming a disabled control.** "Who is safer now? Tap everyone it helps, then tap Done." plays while Done is
   disabled (enabled after the first chip, src.html:677). It is a sequence, so it reads fine aloud; STANDARDS says no
   line names a disabled control. **nit**, general.

10. **Safety card icons do not match their habits** (src.html:1168, uses each hazard's `after` art). "Medicine lives
    up high" shows an empty table with blocks (`pillbox-gone`), "Matches and lighters" shows a table (`lighter-shelf`
    at 36 px), and both online habits show the same screen icon (audit `state-safety-card-1366x768.png`). Better: an
    icon per habit that shows the habit. **polish**, general.

11. **Kitchen towel cutout reads as a second stove.** The `towel-burner` cutout is a whole small stove standing on the
    floor in front of the backdrop's own range (audit `state-room-1920x1080.png`). Better: a towel-and-burner cutout
    placed on the painted range, or a backdrop without a stove there. **polish**, general.

12. **Small words.** "Who is safer" Theo reason in code (src.html:696) differs from the spec's text; stray indentation
    at src.html:715 and 868. **nit**, general.

Checked with nothing found: no em dashes in src, content, notes or lines; "Curio Class" only, never "Curio" alone in
copy; classroom-safe words; nothing stored (notes say so; only the kit's Motion setting); all 46 `art:` tokens have
prompts.json entries and no extra ones; the five people images (theo-blocks, theo-walk, chip-dad, chip-grandma,
chip-theo) carry `people: true` and come from gpt-image, not a local model (they still need Cory's contact sheet and
the representation check, BASELINE rule 11; prompts.json says only "builder inspected"); colour is never the only
signal (Tried, Safe, swept lamps all have words or glyphs); keyboard drag alternative, ruler arrows and keyboard hold
on the candle all work (out2 `ruler-keys`, `hold`); visible focus ring on the ruler blanket (outline solid);
Motion off has no running animation (audit). No cultural, Native or hard-history content; nothing for sensitivity.

Counts: blocker 0, should fix 4, polish 4, nit 4.

## Audit pilot

- Confirmed: the safety-card "hint out of view" lead at 680x425 and 375x812 (finding 7), but low weight because the
  card has its own buttons and Read covers it.
- Wrong: the same lead "at every size": at 1366x768 and up the hint is on screen beside the card. The "welcome late,
  after Search the room" rows are the spec's own design (welcomeAfter), not a fault.
- Missed: the ruler that disagrees with its check (1), focus lost after House or Escape (2: the audit's held-click
  table says "rebuilt, focus kept" for #nav-house, true, but it never presses the stage House button or Escape), the
  doubled "Tap Tell" hint and the heater sentence on every rule card (3, 4: words), keyboard-only ruler hints (5), the
  drag-miss handler (6), and the art and icon fit (10, 11).
