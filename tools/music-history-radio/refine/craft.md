# Craft lens: music-history-radio (round 1)

Counts: blockers 0, should fix 3, polish 4, nit 5

Read: spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, the shared audit (audit-r1).
Frames and logs (scratch, `refine/music-history-radio/craft/`): `f1/` (lines, targets, Tab walk), `f2/` + `v-*.json`
(standard voice check), `f3/` + `v-x*.json` (follow-ups), `art-sheet.png`, `focus-strip.png`. Every Chrome was
`drive.py` on port 9801 with its own profile; 0 console errors or exceptions in all 54 shots.

## Contract: passes

- One file: the bundle is 905,024 bytes (goal 2 MB). No network: `performance.getEntriesByType('resource')` is empty,
  no `http` src/href, no fetch or XHR in the bundle. No storage of any kind; "Results are not saved." is on screen.
- Kit: `Curio.voice`, `MS.ctx`, `MS.pluck`, `MS.blow`, `MS.freq`. The local conductor (variable phrase lengths and
  bar-line swaps) is explained in handoff.md "Engine changes wanted"; `MS.play` has no phrase-boundary hook, so this is fair.

## Access: mostly passes

- Targets (1366x768 and 680x425, every mode): all 44 px or more (smallest: Sound, Read, knob, volume, Reset at 44).
- Focus: every Tab stop shows the gold ring (Tab walk `f1/c03-tab01..18`); the hidden tuner and volume inputs show
  it on the dial window and volume knob. Live result is `role=status`; sliders carry `aria-valuetext`.
- Color is never the only signal: the eye changes shape, "SIGNAL LOCKED" text, "changed" tags, giveaway rows have a bar.
- Motion off (audit calm frame, clean), Sound and Read work (below).

## Lines: pass

`__tool.allLines()` (319) and `voice/lines.json` (319) match word for word, both ways. Every Read part (hint, ident,
`Name. feature`, desk rows) is one of those lines (checked on the Read logs).

## Findings

### should fix

1. **How lines for Mixing desk, Mystery, Compare and Flip are almost never heard** (src.html 1141-1147, 1444,
   1465-1469, 1544-1545). They play only while the radio is off or paused. The normal path is Power first, then
   explore, and on that path the only spoken lines are idents and results:
   - Mixing desk after Power: only "1720. Baroque." (`v-t3-desk-playing`); deskHow is spoken only from a paused
     radio (`v-x2b-paused-desk`).
   - Mystery after Power: nothing at all (`v-t3-mystery-playing`); mysteryHow only from paused (`v-x2-paused-mystery`).
   - Compare and Flip while playing: nothing (`v-x1-playing-compare-flip`).
   - Power as the first tap: only "900. Chant." The tuning how-to ("drag the tuning knob or tap Station") is never
     spoken; dialReady is hint-only (audit lead, confirmed in `v-r1-power-x5`).
   STANDARDS ("one welcome per mode, queued when the mode is entered"; "Say how to act") win over the spec's "how
   lines play over the static or before Power", because with this tool the music never stops between stations.
   Better: speak each how line once over the ducked music, as the idents already do, keeping its `valid`.
   Tag: general.
2. **powerHow is wrong for Mystery** (src.html 1092, 1143). On Mystery entry before Power the voice says "Press
   Power to hear the station. Then use the controls below the radio." The year pin is above the radio, and the
   hint at that moment says "Press Power to hear the hidden station. Then move the year pin and press Tune in."
   powerHow is said once per page, so whichever mode is entered first uses it up (`v-r1-mystery-events`,
   `v-s2-fast-prepower`). Better: give each mode its own Power line (the hint texts deskPower and mysteryPower
   already exist in lines.json). Tag: general.
3. **Gamelan's spoken lines and result heading drop the "encounter" framing** (src.html 1110-1111, 1328). The
   screen says "1889 encounter" (strip) and "Paris encounter, 1889" (meta), but the voice says "1889. Javanese
   gamelan." (`v-x3-gamelan-dial`) and "It was 1889. Javanese gamelan." (`v-x4-gamelan-mystery`). The result
   heading reads "Javanese gamelan · 1889" (`f3/x4-gamelan-mystery.png`). The words don't match the state, and the
   wording is the kind the notes work hard to avoid. **Flag for the sensitivity agent** (rule 5), including whether
   Mystery should ask for "the year you hear" of a living tradition. Not judged here. Tag: general.

### polish

4. **The needle covers the locked station's year, and the end years clip when the dial scrolls** (src.html 65-73,
   1362-1365). Locked on 1200, 1889 or 1987, the red needle runs through that year's digits (`f3/x6-1987-1366.png`,
   `f3/x4-gamelan-mystery.png`, audit `state-locked-second-680x425.png`). At 1366x768 in Mystery and Mixing desk,
   "1987" reads "198" and "900" is clipped (audit `state-mystery-reveal-1366x768.png`, `state-desk-extreme-1366x768.png`).
   Better: let the needle stop above the numerals (or lift the locked year above it) and pad the scale so end
   labels fit. Tag: general.
5. **Hip hop notation is cut off at 1366x768** (src.html 115-116, 1234-1244). On Hip hop in Dial the SNARE row of
   the pad grid is half below the panel's fold (`f3/x6-1987-1366.png`), which works against Done when 9 (panel
   visible without scrolling). Better: a shorter listen-for line or a tighter grid on that station. Tag: general.
6. **One-key shortcuts with no modifier and no off switch** (src.html 1661-1674): C, F, M and Space act anywhere
   outside an input (WCAG 2.1.4). M also leaves a Mystery round mid-listen. Better: act only when focus is on the
   stage, or add Shift. Tag: general.
7. **Fast tuning uses up idents** (src.html 1405-1409, 1431). Tapping Station at a 0.2 to 0.4 s pace starts each
   ident and cuts it after a syllable. It is then marked heard and never returns (`v-s2-fast-dial-then-desk-reset`,
   `v-x3-gamelan-dial`: 6 idents spoken and cut). This follows the kit rule (marked when it starts). Better: queue an
   ident only once the lock has held for about 400 ms. Tag: general.

### nit

8. The dial window is its own Tab stop before the tuner, so Tab lands twice on the same dial with the same ring
   (`f1/c03-tab07`, `c03-tab08`). `tabindex="-1"` on `#dial-window`. Tag: general.
9. Idents differ from the spec's wording ("You're tuned to 900. Plainchant.", "1720. The Baroque.") versus built
   "900. Chant.", "1720. Baroque." lines.json matches the tool; the spec is out of date. Tag: general.
10. Dead code: `$('maker')?.classList` (src.html 1678; no element has id `maker`). Also several 7 to 9 px
    declarations (lines 58, 80, 83, 113, 145, 174, 185-191) are all overridden by the "Final build repairs" block,
    which is hard to maintain. Tag: general.
11. flipHow says "at the next bar" when it plays while paused (the only time it plays), where Flip switches at once.
    Tag: general.
12. The volume knob is hidden during a covered Mystery round (src.html 1352). Tag: general.

## Art: passes

All 15 `art:` tokens (radio, knob, room, 12 postcards) have prompts.json entries. Only mhr-pc-hiphop shows people,
and it is `people: true`. Every asset is `drawn_by: codex`, not a local model (BASELINE rule 11). The contact sheet
(`art-sheet.png`) shows no other people and no fake lettering. The people image's stereotype and representation check
belongs to the sensitivity agent.

## Words: pass

No em dashes in src.html, notes.md, lines.json, prompts.json, tool.draft.json or handoff.md. "Curio Class" everywhere,
never "Curio" alone (the radio plate reads CURIO CLASS). Language is classroom-safe. Nothing is stored, and the screen
says so.

## Standard voice check

Held clicks (`hold` 0.12), Sound on, Motion on, gaps longer than the lines (3 to 4.5 s) for repeats.

| line | kind | expected | spoken |
|---|---|---|---|
| welcome (Dial) | how | once | 1 (stage, key, Station, Sound off then on); 0 when Power is the first tap (finding 1) |
| powerHow | how | once | 1 of 5 pre-Power Compare taps; also 1 on the first Desk or Mystery entry (finding 2) |
| ident, 12 stations | how | once each | 5 of 5 on Next x5 and ArrowRight x5; 0 of 5 on Prev x5 back; 0 of 4 on Power resume |
| compareHow | how | once | 0 (playing, `v-x1`); pre-Power Compare says powerHow instead |
| flipHow | how | once | 1 pre-Power (`v-r1-flip-paused`); 0 while playing (`v-x1`); dropped when Flip is pressed (`v-s2-compare-next-flip-fast`) |
| deskHow | how | once | 0 after Power (`v-t3-desk-playing`); 1 only from paused (`v-x2b`) |
| mysteryHow | how | once | 0 after Power (`v-t3-mystery-playing`); 1 only from paused (`v-x2`) |
| result (It was ...) | event | every Tune in | 7 of 7 (`v-r1-mystery-events`) |
| setDone | event | every set end | 1 of 1 (cut by New set 1.1 s later, at my pace) |
| Random mix x5, Flip x5 | none defined | 0 | 0 |

- **Stale lines:** fast runs (0.22 s gaps) through Station, mode, Reset, Tune in and Next station: every running line
  was hushed by the next action. No line played after its moment, and none named a hidden or disabled control
  (`v-s2-*`). flipHow was dropped when Flip was pressed.
- **First tap:** stage tap: welcome in 124 ms. ArrowRight: welcome in 6 ms. Mode button: powerHow in 130 ms. Read:
  hint only (audit). Sound: nothing; Sound back on: welcome once (`v-t3-sound-off-on`). Sound off, then Power,
  then Sound on: the ident is logged `silent/off`, then spoken on Sound on (`v-t3-sound-off-power-on`).
- **Read:** Read during an ident cuts it and reads (`v-r4-read-during-ident`). With Sound off it still reads. A mode
  change right after Read starts the next line in 129 ms. Tuning to a new station cuts a running Read (`v-r4-read-playing-then-next`).
  That is a user action that makes the Read text stale, so it is accepted.
- **Order:** spoken lines follow the actions in every log.

## Audit pilot

- **Confirmed:** "#power: welcome not heard". Power as the first tap gives only the ident; the tuning how-to is never
  spoken (part of finding 1).
- **Wrong or acceptable:**
  - "#compare: welcome not heard": powerHow plays instead and carries the premise.
  - "#reset: nothing changed": Reset at the Baroque default is rightly a no-op.
  - "Power two quick taps: ident cut": the second tap is Pause, a deliberate stop; marked-on-start is the kit rule
    (related to finding 7).
- **Missed by the audit:**
  - Finding 1. Its one-click-per-fresh-page walk never enters a mode after Power, so it can't see the how lines
    going silent.
  - Finding 2: wrong words in powerHow.
  - Finding 3: gamelan wording.
  - Finding 4: the needle through the year digits and clipped end years. Its "lines across labels" check passed them.
  - Finding 5: the hip hop pad grid inside a scroll panel.
  - Finding 6: shortcuts.
  - Finding 8: the double Tab stop.
- Its clean rows (sizes, states, Motion off, resize, five clicks at 2 s) agreed with my frames wherever I looked.
