# Craft lens: first-aid-responder (round 1)

Counts: blockers 0, should fix 5 (general 5, family 0), polish 2, nit 2

Bundle looked at: `tools/first-aid-responder/first-aid-responder.html` (CURIO_DRAFT=1, 560,078 bytes). My frames and
voice logs: `<scratch>/refine/first-aid-responder/craft/v1` to `v5` (`*.png`, `*.log.json`, `out.txt`), held clicks
(0.12 s), Sound on, Motion on, 1366x768, a fresh Chrome profile per run (port 9751). Shared audit:
`<scratch>/refine/first-aid-responder/audit-r1`.

## Contract

- One file, 0.56 MB (under the 2 MB goal). No network requests: `performance.getEntriesByType('resource')` is empty
  (v1 `allLines.json`). No console errors or exceptions in any of my 33 shots or in the audit.
- Kit used: `Curio.voice`, `Curio.tone`, `Curio.yes`, `Curio.audio`, `Curio.onSound`, `Curio.onMotion`, kit
  `.calm` and `:focus-visible`. The metronome (Web Audio on the kit's context) and the card drag are tool code; the
  kit has neither, so nothing is re-implemented.
- Metronome: `__tool.testMetro()` gives 220 clicks in 120 s, 0.5455 s apart (Done when 5).

## Findings

### Should fix

1. **The coach nags an idle student forever: "Keep going. Don't stop." every 9 s.** (general)
   Where: `coachKey()` and `coach()`, src.html:1471-1488. In free practice (no round running) any single chest tap
   makes `coachKey` return `coachPause` once the student goes quiet for 2 s, and `coach()` re-says it every 8 s with
   no end. How I saw it: v2 `idle-nag` (3 taps, then 40 s idle): spoken at 12.2, 21.5, 30.7 and 39.9 s and still
   going. v2 `idle-dialog`: it keeps playing while the Clear best times dialog is open (21.4 s), over the dialog's
   own line. v3 `kb-cpr-held`: 5 taps, then the same line. A student who taps once and reads the rate note, or a
   teacher who taps to demo and starts talking, gets a scolding loop. During a running round the pause line is right
   (v2 `cpr-rep`, `slow-round`). Better: speak `coachPause` only while a round runs (in free practice show it, at
   most say it once), and add `!$('clear-dialog').open` to its `valid`.

2. **Space does not press the chest after the mouse picks CPR rhythm, and Space after Stop starts a new round and
   wipes the summary.** (general)
   Where: keydown handler src.html:1664-1669 (`if (active?.closest('button') && active.id!=='chest') return;`),
   Stop handler src.html:1608-1611, key "2" path src.html:1661. Focus sits on the CPR rhythm button after a click or
   the 2 key, so Space re-clicks that button. After Stop, focus moves to Start, so the next Space starts a round.
   How I saw it: v3 `kb-cpr-click-space`: click CPR rhythm, Space five times: `total 0`, focus `m-cpr`, while the
   welcome line and hint say "Press Space or tap the chest". v5 `stop-space`: Start, 3 taps, Stop, Space three
   times: `running true, summary false`, the round-over line cut. Better: in CPR rhythm, Space and Enter on the
   mode buttons, Start and Stop count as compressions (or move focus to the chest after a mode entry and after Stop),
   so the key the line names always works and a summary is never lost to the next keypress.

3. **After every mouse tap on a card the hint turns into keyboard text and Read speaks a card the student never
   chose.** (general)
   Where: `choose()` src.html:1173-1175 moves focus to the first unused card after any placed or Never card, and
   that card's `onfocus` (src.html:1098-1102) sets `state.readCard` and the hint "Enter places this card. Read gives
   its full text." The hint "Tap the next step. Read can explain your last move." is overwritten at once, and
   `read()` (src.html:967) prefers `state.readCard` over `state.lastFeedback`. How I saw it: v3 `hint-after-tap`
   (tap Make the scene safe with the mouse: hint is the Enter line, focus on `card-d1`); v4 `r-wrong` (tap the
   "Wait a minute" Don't card, Read says "When the AED arrives, turn it on and follow its voice prompts. Press Enter
   to place this card."); v4 `r-right` (a correct tap, Read says "Stop every few compressions to check them. Press
   Enter to place this card."). The why behind a mistake, the thing Read promises, is never spoken. Better: move
   focus only when the tap came from the keyboard (or with `preventScroll` and without touching the hint and
   readCard when the pointer was used), and let Read speak `lastFeedback` after a choice.

4. **Read speaks run-together and symbol text.** (general)
   Where: `read()` src.html:964-968 uses `textContent` of `#summary` (src.html:1433-1437) and `#finish`
   (src.html:1216-1222). How I saw it, v4 logs, word for word:
   - summary: "Partial round Average rate63.9/min In target band0.0%Longest pause0.9 s Compressions4 ..."
   - finish: "Response complete.0:05.2 · 0 mistakes · Your first best run is set.Why this order Make the scene
     safe: ... Check response + breathing, at most 10 s: ... Push hard + fast, 100 to 120/min: ... Run it again
     Next scene ▶"
   The voice gets "rate63.9", "slash min", "plus", "10 s" and the two button labels. STANDARDS asks for nothing a
   voice would misread. Better: build a spoken string for each ("Average rate 64 a minute. 0 percent in the target
   band. Longest pause 0.9 seconds. 4 compressions.") and for the finish use each step's `text` with its reason, not
   the short titles, and leave out the buttons.

5. **Three step cards start in lower case.** (general)
   Where: src.html:660 "send someone to call 911", src.html:712 "gently take off rings or anything tight near the
   burn", src.html:816 "start timing the seizure" (the spec's "and 3." split carried over). It shows as the small
   line on the card at 1280x720 and up (audit `state-scene-open-1366x768.png`, Send someone to call 911), in each
   card's tooltip and slot title, and in three Read lines in `voice/lines.json`. Better: capitalize the three `text`
   values (the lines file follows from `allLines()`).

### Polish

6. **"to the beat" when there is no beat.** (general) src.html:863 `wCpr`: "Press Space or tap the chest to the
   beat." The metronome is Off by default, so a first-time student hears about a beat that isn't playing. Better:
   "Press Space or tap the chest at a steady pace. Keep the needle in the shaded band." (or name Metronome).
7. **At 375 wide the "either order" pair splits across rows.** (general) Scene 3 (Deep cut) slots 3 and 4 share a
   rank; in the 3-column phone rail slot 3 sits at the end of row 1 with "either order" under it and slot 4 starts
   row 2 with only a thicker bottom border, so the pair no longer reads as joined (audit
   `state-scene-open-375x812.png`). Better: mark both slots (for example "3 or 4" on each) rather than a label
   under the first.

### Nit

8. **A line that never plays.** src.html:868 `roundEnd: 'Round over. Check your rate summary.'` is in `L` and
   `voice/lines.json` but every round end says `roundEnd<percent>`. It would be recorded for nothing.
9. **Read can't be pressed while the Clear dialog is open** (the modal makes the header inert; v3 `read-dialog`
   logs no read). The dialog's own line still plays once, so this is minor.

## Access

- Keyboard: Tab reaches the mode buttons, the six scene cards, More, every step card, the panel and the Field guide
  cards; Enter places a focused card and focus moves to the next one (v4 `kb-place.png`, focus ring clearly visible
  in the kit's 4 px outline). The audit's "settled, then Enter twice" column is clean for every control. Keys 1 to 3
  change modes. The two keyboard breaks are in finding 2.
- Targets: 44 px everywhere (audit, all sizes clean).
- Color is never the only signal: ✓ and ✗ glyphs with words, "Not yet:" text, the gauge band labeled "Target 100 to
  120", the in-band tone differs in pitch as an extra.
- Motion: `.calm` stops the standby dot, shake, land and squash; the needle snaps; the card flight is skipped when
  `Curio.reduce` (audit Motion off clean). Sound: Sound off stops the metronome (`Curio.onSound`) and lines go
  silent (v3 `read-soundoff`). Read: works with Sound off and cuts a playing line (v3 `read-midbrief`); its content
  is findings 3 and 4.

## Lines

`__tool.allLines()` (167 lines) and `voice/lines.json` (167 lines) match word for word, both ways (v1
`allLines.json`). Each spoken line I logged matched its frame and state, except the idle coach line (finding 1) and
the Read texts (findings 3, 4).

## Standard voice check

All held clicks (0.12 s), Sound on, Motion on. Logs in `v1` to `v5`.

| Line | Kind | Expected | Spoken | Run |
|---|---|---|---|---|
| brief0 (scene opened, then Restart x4, 10 s apart) | event | 5 | 5 | v1 rep-brief |
| order "Tap the step you would do first..." | how | 1 | 1, then silent (heard) x4 | v1 rep-brief |
| done "Scene complete..." (5 finishes, Run it again 0.9 s later) | event | 5 | 5 | v1 rep-finish |
| best "New best time." (first finish on a fresh profile) | event | 1 | 1 | v1 first run, v3 read-finish |
| wCpr (CPR rhythm entered 5 times) | welcome/how | 1 | 1 | v2 mode-rep |
| wGuide (Field guide entered 5 times) | welcome/how | 1 | 1 | v2 mode-rep |
| round "Tap Start 2-minute round..." (24 free taps, two visits) | how | 1 | 1 | v2 round-how |
| roundEnd percent (5 rounds, Stop, 4.5 s apart) | event | 5 | 5 | v2 cpr-rep |
| coachPause in a running round with real pauses | event | about every 8 s | every 9 s | v2 cpr-rep, slow-round |
| coachPause in free practice, idle 40 s | event | 0 (or 1) | **4, unending** | v2 idle-nag |
| coachPause with the Clear dialog open | event | 0 | **2** | v2 idle-dialog |
| clearHow (dialog) | how | 1 | 1 | v2 idle-dialog |

1. Repeats: right for every line but `coachPause` (finding 1). Wrong-move feedback is on screen only, as the spec
   says (v1 rep-wrong).
2. Stale lines: v3 `stale-fast` (0.2 s taps through a scene, CPR, Scenes, a second scene, All scenes): every line
   was cut or dropped as its moment passed; nothing played late. The `order` line is dropped (not marked heard)
   when the first card is tapped during the briefing, so it can come back later, as the rules want.
3. First tap (fresh page each): stage heading, welcome within about 0.2 s (v4 `ft-stage2`); scene card, only its
   briefing (v3 `ft-scene`, `ft-stage`); mode button, that mode's welcome (v3 `ft-mode`); Read, the hint only
   (`ft-read`); Sound, nothing (`ft-sound`); Sound off then on, the welcome once (`ft-sound-offon`); a key (Tab),
   the welcome (`ft-key`). All pass.
4. Read: stops a playing line and speaks (v3 `read-midbrief`), works with Sound off (`read-soundoff`); a mode
   change right after Read starts its welcome at once (`read-then-mode`, 0.75 s later). What it says is findings 3
   and 4.
5. Order: lines follow the actions in every log.

## Art

Every `art:` token (fa-gym, fa-cafeteria, fa-shop, fa-kitchen, fa-field, fa-hallway, fa-kit, fa-aed, fa-manikin)
has a `prompts.json` entry. The three local FLUX backdrops (gym, shop, hallway) show empty rooms, no people (checked
at full size). The other six are gpt-image; fa-manikin carries `people: true`, which is cautious but harmless.

## Words

No em dashes in src.html, notes.md or lines.json. "Curio Class" is written in full. Language is classroom safe.
Privacy: "Saved only on this device." shows on all three modes, under the only control that stores anything.
Lower-case card text is finding 5.

## Audit pilot

Leads confirmed on my own frames:
- 375x812: Timer: On and Clear best times sit below the fold on the picker and in scenes (audit size and state
  frames). Confirmed, but not a finding: neither is a main control, and the cards, rail and deck are in view.
- 375x812 clear-confirmation: the hint is out of view (it lives in the header, the page is scrolled to the Clear
  button). Confirmed; the dialog itself says what to do, so I did not report it.

Leads that were wrong:
- The 12 "overlap #chest / div.pad-label" rows (680x425, 800x500, 1000x625, four states): the label is placed under
  the torso inside the same bay by design, `pointer-events:none`; on `state-cpr-running-800x500.png` it sits below
  the torso with no clash.
- "Welcome not heard" after a first tap on the six scene cards and on Clear best times: correct behavior. The tap's
  own line plays (the briefing, or the dialog's how line), and "Tap a scene card to open it." would be stale once a
  scene or the dialog is open.

What it missed (none of these show in a single click or a 2 s, five-click pace):
- The free-practice coach loop that needs 9 s of idle time to show (finding 1).
- Space and Enter following focus to the mode button or Start instead of the chest (finding 2): the audit presses
  Enter on whatever holds focus, not the key the line names.
- What Read says after a mouse tap and how it reads a summary or finish card (findings 3 and 4).
- Lower-case card text (finding 5) and the "to the beat" wording (finding 6).
