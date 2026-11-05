# Play lens: first-aid-responder (round 1)

Counts: blockers 0, should fix 6, polish 5, nit 6

Played twice: as a grade 9-12 student alone at home (mouse, then Space key), and as a teacher projecting at 1920x1080.
Bundle as given (CURIO_DRAFT=1). My frames and scripts are in
`C:\Users\Cory\AppData\Local\Temp\claude\912539a76ace91d0\c55c8920-4b50-4aa7-8632-31d061e89e76\scratchpad\refine\first-aid-responder\play\`
(`f1/*.png`, shot lists `s1.json` to `s4.json`). Every drive used held clicks (0.12 s) or real Space keys and logged
`__tool.vlog`. No console errors in any shot.

## Should fix

1. **Don't cards give themselves away by their format.** (Scenes, every scene; `src.html` scene data)
   All 12 Don't cards repeat their title word for word as the small text ("Hold them down" / "Hold them down"). 32 of
   the 33 correct steps have a short title, often with a "+", and a longer, different small text ("Ease down + clear the
   area" / "Ease them to the floor and move hard or sharp things away"). A student can spot the two traps in every scene
   without reading them, which skips the part of the lesson that says what not to do. Seen in frames `02`, `12`, `18`,
   `19` and checked over all six scenes with a script. Better: give Don't cards the same short-title plus fuller-text
   shape as real steps (e.g. "Ice it" / "Put ice on the burn to cool it fast"), and drop the one real step whose text
   equals its title ("Call 911" in Heat at practice). Missed BUILD wave lesson (no giveaways by option length or form).
   **general**

2. **After a mouse tap, the hint and Read jump to a random card.** (Scenes, `choose()` focus move plus card `onfocus`)
   When a tap retires a card (a correct step or a Don't), `choose` moves focus to the first unused card even for a mouse
   tap; that card's `onfocus` then sets the hint to "Enter places this card. Read gives its full text." and
   `state.readCard` to that card. In `02` and `15` a correct tap in Choking at lunch left the hint on the keyboard line,
   and Read then spoke "Give 5 back blows ... Press Enter to place this card." (in `02` the focused card was the Don't
   "Reach blindly into their mouth"). The hint a moment earlier promised "Read can explain your last move." Better: move
   focus only when the tap came from the keyboard (`e.detail===0`), or keep the feedback line as Read's text after a tap.
   **general**

3. **The coach nags while nobody is tapping.** (CPR rhythm, `coachKey()` / `coach()`)
   In free practice, after six taps and then no input, "Keep going. Don't stop." was spoken at 9.1 s, 18.2 s and 27.4 s
   and keeps going every 9 s for as long as the student sits on the mode (`06-idle-nag`). After Start with no taps yet
   it says "Keep going. Don't stop." at about 4.8 s, before the first compression (`07-round-no-taps`). Better: the pause
   line plays only during a round and only after at least one compression, and free practice goes quiet after one pause
   line (back to "Find your rhythm"). STANDARDS: don't nag; the line matches the state. **general**

4. **"Tap the chest to the beat" with no beat.** (CPR rhythm welcome `wCpr` and hint; `state.cpr.metro=false`)
   The welcome and the hint say "Press Space or tap the chest to the beat", but the Metronome starts Off (`03`, `08`:
   metro false, no clicks). A solo student has no beat and no idea what 110 a minute feels like. The spec's arc is to
   learn the rhythm and then hold it without the metronome. Better: Metronome On by default (Sound on), with the
   "round" or summary line nudging "Try a round with the Metronome off" once they hold the band; or reword the welcome.
   **general**

5. **The chest pad's focus ring strikes through its label.** (CPR rhythm, `#chest` focus outline and `.pad-label`)
   Start moves focus to the chest, so for the whole round a light blue focus bar runs straight through "CENTER OF CHEST ·
   PRESS SPACE" (`09`, `10`, zoom `z-padlabel.png`, at 1366x768; the audit flagged the same boxes at 680 to 1000).
   Better: keep the label outside the button's outline (more bottom padding on `.pad-bay`, or an outline offset inward).
   **general**

6. **Reflex taps after 2:00 wipe the round's trace.** (CPR rhythm, `compress()` with `practiceAfterSummary`)
   A student tapping at 110 does not stop exactly at 2:00. In `09` the next few Space presses after the round switched the
   strip chart to a new free-practice trace ("RATE TRACE · 0:06 / 2:00", "7 compressions") while the panel still shows
   "Two-minute round ... 219 compressions"; the coach box shows "Keep going. Don't stop." beside the summary. The trace
   they just earned is gone (it survives only if it was a new best, as the faint ghost). Anything shown twice must match.
   Better: ignore taps for about 1.5 s after the round ends, or keep the round trace until Start or a deliberate tap
   after a pause. **general**

## Polish

7. **The rate trace is too flat to read.** (CPR rhythm, `drawTrace()`)
   60 to 160 fits into about 60 px at 1366x768 and 1920x1080, so the band is about 12 px and a steady 90 a minute sits
   just under it, looking almost on target (`10`, zoom `z-trace.png`, `21`). Better: plot 80 to 140 (clamp beyond),
   give the band more height, and color the line out of band (warn color plus the words "too slow"/"too fast" in the
   summary so color is not the only signal). **general**

8. **"Either order" is hard to see.** (Scenes, shared-rank slots)
   The shared slots carry a thin bar and a 9 px "↔ either order" under the first slot only (`timed-laptop` audit
   frame, `19`, `20`); at 375 wide the pair even splits across rows. The spec says the slots are "drawn joined". Better:
   one bracket spanning both slots with the label at readable size. **general**

9. **The ghost race barely shows.** (Scenes, `updateScenePanel()` ghost)
   The ghost is a 16 px hollow ring on a slot's corner (`12`), easy to miss, and right after a first timed finish the
   panel still says "Ghost: finish a timed scene to set one." next to "Your first best run is set." (`scene-finish`
   audit frame, `11`). Better: a visible marker that steps along the rail while racing, and "Ghost set: race it next
   time" after the first best. **general**

10. **Big screens leave the deck small.** (Scenes at 1920x1080, teacher projecting)
    In `18` the cards keep 12 to 13 px small text and about 300 px of empty field sits under the deck. Better: let the
    rail and deck grow with the stage height so a class can read the cards from the back. **general**

11. **"Your own ghost" means nothing yet.** (Picker first screen, "Six situations. Your decisions. Your own ghost.")
    A solo student meets "ghost" with no explanation on the first screen. Better: "Beat your own best time" or one line
    on what the ghost is. **general**

## Nit

12. Small texts that start lowercase: "send someone to call 911", "start timing the seizure", "gently take off rings
    ..." (`timed-laptop`, `19`), and the finish feedback "✓ stopping stops the blood flow." (`scene-finish`). **general**
13. The round-end voice rounds: screen "In target band 99.5%", voice "100 percent" (`09` log `roundEnd100`). **general**
14. Field guide "When to call 911" Practice it opens Heat at practice with no reason given (`16`). **general**
15. Pressing 1 in the middle of a scene returns to the picker and throws the run away without a word. **general**
16. At 375 wide the picker's Timer and Clear best times sit below the six cards (audit lead; confirmed, harmless: they
    move above the rail once a scene opens, `state-scene-open-375x812`). **general**
17. After a first tap on Clear best times and Keep them, the Scenes welcome never plays; the hint is restored, so this
    is minor (audit lead). **general**

## What it is like (feel)

- **Scenes** feel quick and clear: the briefing is short, the rail and deck are the biggest thing, and a wrong step
  explains itself with the earlier step's reason. Run 2 of the same scene becomes memory, and the ghost is too faint to
  make it a race (item 9). The Don't format tell (item 1) is the moment that went flat: I could finish every scene with
  no mistakes without reading the traps.
- **CPR rhythm** works well with Space at 110: needle steady, 99.5 percent in band over a real 2-minute round (219
  compressions, `09`), "Push faster" at 90 (`10`). It lands less than it could at the end: no beat to start (item 4), and
  the round's picture disappears under the next taps (item 6). The coach nag (item 3) is the moment I would close the
  tab.
- **Field guide** is plain and readable at every size I looked at (`16`, `17`, `state-guide-aed-*`).
- **POLISH.md:** calm mode keeps the clock and skips only the card flight (`22`); no timing is shortened. Words and
  state disagree in items 3, 4, 6, 9, 13.

## Frames looked at

Mine: `f1/01` to `f1/22`, `z-padlabel.png`, `z-trace.png`. Audit: `size-1366x768`, `state-scene-error-1366x768` and
`-680x425`, `state-scene-finish-1366x768` and `-680x425`, `state-timed-laptop-1366x768`, `state-cpr-running-1366x768`,
`state-cpr-summary-680x425`, `state-scene-open-375x812`, `state-clear-confirmation-375x812`.

## Audit pilot

- **Confirmed:** chest / pad-label overlap (and it is worse than the lead says: the focus ring strikes through the label
  at 1366x768 and 1920x1080 too, item 5); Timer and Clear below the fold on the 375 picker (real, harmless, item 16);
  welcome not heard after a first tap on Clear best times (minor, item 17).
- **Wrong or harmless:** "welcome not heard" after a first tap on any scene card: once a scene is open the picker's
  welcome is stale, and the briefing plus the "order" line are the right lines. "Hint out of view" with the Clear dialog
  at 375: the dialog itself names both choices.
- **Missed by the audit:** the Don't card format tell (item 1); hint and Read hijacked by the focus move after a mouse
  tap (item 2, the audit's "focus kept" row hides it); the idle coach nag (item 3: its five-click runs never wait 10 s
  with no input); "to the beat" with the Metronome off (item 4); the round trace wiped by post-round taps (item 6); the
  flat strip chart and faint ghost (items 7, 9); stale ghost text after a first best (item 9).
