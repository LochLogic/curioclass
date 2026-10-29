# Play lens: half-life-dice

Played cold twice: as a grade 10 student alone at home (Sound as the tool starts it, no teacher), and as a teacher
projecting at 1366x768 and 1920x1080. Bundle: tools/half-life-dice/half-life-dice.html (built 2026-10-29 00:22).
My frames: S:/CurioClass-codex-scratch/half-life-dice/lens-play/f1/ (shots1-4.json beside it). Audit frames looked
at: S:/CurioClass-codex-scratch/half-life-dice/audit-r1/ (size-1366x768, state-marked-1366, state-d6-ten-1920,
state-tracked-680 and -375, state-mode-nucleus-1366, state-right-1366 and -375, state-wrong-1366, state-fission-680
and -375, state-mode-dating-lab-1366 and -800x500, state-noise-1366 and -375, state-too-old-680,
state-average-760x900, state-mid-roll-680).

Counts: **0 blockers, 8 should fix, 8 polish, 4 nits.**

## Should fix

1. **The tray of dice is not a tray of dice at most sizes.** Roll mode, `drawTray()` (src.html line 104). The 40 x 25
   grid is stretched into a wide, short box and each die is sized by the row height, so the dice become 40 vertical
   stripes of 3 to 6 px squares with 15 to 20 px gaps. At 1366x768 the faces are about 5 px and can't be read, and at
   680x425 the tray is a band of 2 px slivers. Only 760x900 and 1920x1080 look like a tray. The ring on a tracked die
   is cut off by the canvas top (die 1 is in row 0). For a teacher projecting, this is the tool's main picture.
   Seen: size-1366x768, state-mid-roll-680x425, state-tracked-375x812, my 01, 02, 05 and the zoom z05.png. What
   better looks like: keep the cells square and centre a block that fits (or pick the column count from the box's
   aspect, still 1,000 dice), with faces at 9 px or more at 1366x768. **general**
2. **"Drag the graph handle to 500 nuclei" can't be done, and the half-life can be marked without rolling.** Roll,
   Mark a half-life (`snap` in drawGraph, line 107). The handle snaps to the expected curve's height at each half
   roll, so a careful drag to 500 lands on 482 (or 527). The reading then comes from that snapped height, so it is
   nearly always the snap step, whatever the tray did. With 0 rolls the card says "Accepted. Expected crossing:
   4.0 rolls. Exact for a d6: 3.802." The cheap path is Mark, then arrow keys until "Accepted", with no dice rolled.
   Dragged to the bottom it reads "Expected crossing: 25.5 rolls", off the graph. Seen: my 04 (drag to 500: y 482.25,
   "Accepted. Your tray: 4.0 rolls"), 04b, audit state-marked-1366x768. Better: snap the line to 25-nucleus steps so
   500 is reachable, read the crossing from the tray's own points, and ask for Roll to 10 first, with the card saying
   so before it marks anything. **general**
3. **Roll once and Roll to 10 look live after roll 10 and do nothing.** Roll (`updateRoll` sets only
   `aria-disabled`, and the kit has no style for it). At 10 rolls both buttons keep their bright primary fill, a click
   is silent, and nothing says that Reset starts a new tray. Seen: my 02 (coin, 0 left after 10 rolls, buttons
   unchanged), 03, 06. Better: a disabled look, and a hint or card line at 10 rolls that names Reset or New seed.
   **general**
4. **Sound starts off on every load, so a student on their own never hears a welcome.** The load script calls
   `$('sound').click()` after `Curio.init` (line 138), which turns the kit's default (on) off, every time. The spec
   asked only for the Geiger clicks to start off ("A Geiger counter clicks (sound off by default)"). With Sound off,
   all three mode welcomes and trackTip are silent. The audit's 19 "not heard" rows come from this. Seen: audit click
   table, my 22 (first tap on Roll once: empty log, Sound aria-pressed false). Better: leave narration on as the kit
   does and give the counter's tone its own off-by-default setting, or stay silent but say on screen that Sound turns
   on the narration. **general**
5. **The Dating lab welcome skips Estimate.** wDating, "Pick a sample. Drag on the ruler to estimate, then press
   Calculate." (spec line, lines.json). A student who follows it presses Calculate and gets "Press Estimate to record
   your ruler pin before Calculate." The hint (hint12) has the right order. Seen: my 12 (Calculate first), 20 and 21
   (the line is spoken). Better: "Pick a sample. Drag the ruler pin, press Estimate, then press Calculate." (the
   hint's words, so one recording serves both). **general**
6. **The estimate step can be skipped for free.** Dating (`estimate`, `calculate`). Estimate takes the untouched pin
   at 1,000 years and Calculate then prints the exact age. "Close." can also be found by sweeping: drag a bit, press
   Estimate, repeat. So "read the age from the ruler first" costs nothing and has no stake. Seen: audit
   state-noise-1366x768 and state-too-old-680x425 ("Estimate: 1,000 years. Compare with the halving ticks." then the
   full answer), my 13. Better: Estimate is only accepted after the pin has moved for this sample, the pin starts at
   0, and Calculate shows the estimate and the exact age side by side ("You read 3,000. Exact: 3,349. Off by 10
   percent."), with no "Close" before Calculate. **general**
7. **Counting noise never varies.** Dating (`countSample` seeds on the sample index). Cave charcoal with noise counts
   337 every time: three noise off-and-on toggles, switching to Hearth and back, all 337. New seed is only in Roll
   mode. A student who turns on "noise" sees one fixed number with a ± after it, and the idea that a recount differs
   by about the square root of the count never shows. Seen: my 10 (`[337, 337, 337, ["hearth", 621], ["cave again",
   337]]`). Better: a `Count again` button that draws the next count from the same seeded stream (so the same seed
   still gives the same sequence, Done when 7), with the counts so far listed so the student sees the spread.
   **general**
8. **The nucleus captions read as "before = protons, products = neutrons".** Nucleus, `drawNuclei` (line 117): the
   left caption is "Before: protons p+ (solid)" and the right one is "Products: neutrons n (outlined)". They are one
   legend split in two, but each sits over a side as its title. "Outlined" also means the proposed product's dashed
   box in the equation below. Seen: state-mode-nucleus-1366x768, state-right-375x812 (zoom z-375-right.png). Better:
   titles "Before" and "After (your product)" over the sides, and one legend line with a dot of each colour:
   "proton p+" and "neutron n". **general**

## Polish

1. **Light nuclei look like a loose cloud, not a nucleus.** Dot size is capped at 4 px inside a radius set by the
   box, so C-14 and F-18 are 14 to 18 dots scattered across 150 px, while U-238 and the fission fragments are packed
   balls. At 375 wide the symbol labels "C" and "N" sit on the dots and the arrow overlaps the Ba nucleus. Seen:
   state-right-1366x768, my 16 (F-18), state-fission-375x812, z-375-right.png. Better: size the dots so light nuclei
   are packed too, and keep labels and the arrow clear of the drawings.
2. **Steppers start at A 10, Z 3 on every card.** F1 needs 131 presses of + and 53 more; N2 needs 224 and 87 (the
   builder's own audit state clicks + 131 times). Typing works, but nothing says so. Better: start at the parent's
   values, or add -10 and +10 steps or a press-and-hold repeat, and say "or type a number" by the boxes.
3. **Track one is easy to miss and can lead nowhere.** It always rings die 1 in the top-left corner (the first live
   index), where the ring is clipped. After roll 10 it still rings a die and the card says "Chance it decays next
   roll", but no roll is possible. Seen: my 05, 06, z05.png. Better: pick a live die near the middle (seeded), and
   after roll 10 say "Press Reset to track a die from the start."
4. **The d20 tray never reaches its half-life.** Rolls stop at 10, the d20 half-life is 13.5 rolls, and the graph
   already runs to 16, so the card can only ever say "Expected crossing". Seen: my 03. Better: let d20 roll to 16
   (Roll to 16 when the graph goes there), so every die's tray crosses 500.
5. **Each roll is a flat moment.** Dice that decayed this roll turn the same gray as old decays, so the student can't
   see "about 1 in 6 of the live dice went this time". The hint stays "Pick a die, then press Roll once" through rolls
   1 to 9. Better: outline this roll's new decays until the next roll (shape, not only colour), with "162 decayed
   this roll" in the summary, and after roll 1 a hint that points at the graph or Track one.
6. **One look has two meanings.** The green primary fill marks both "do this" (Roll once, Roll to 10, Estimate,
   Calculate, Check) and "this toggle is on" (Show expected, Mark a half-life, Counting noise). Clear sits in the card
   row after F2 and in the sample row after Deep core, styled like an eighth choice, and wipes saved progress with no
   confirm. New seed sits in the die row like an eighth die. Seen: state-right-1366x768, state-noise-1366x768.
   Better: one style for toggles that are on; Clear and New seed set apart from the choices, and Clear asks once.
7. **The energy ladder's log scale has no scale.** The bars start at methane, so the methane rung is a 5 px stub,
   and there are no powers of ten, so "log scale" is a word, not something to read. At 680 and 375 the labels crowd
   the bar above. Seen: state-right-1366x768, state-fission-680x425, z-375-right.png. Better: a faint axis at 1 eV,
   1 keV, 1 MeV and 100 MeV, bars starting at 1 eV, and labels that never touch a bar.
8. **Two cards keep saying the step that is done.** After Mark a half-life is pressed, the half card still says
   "Press Mark a half-life. Move the line to half the starting crowd." (my 03, until the line moves). After a wrong
   Check the change box still says "Your proposed product is outlined. Check both sums to test it." (state-wrong).
   Better: "Drag the orange line to 500." and "Fix the sum that is off, then press Check again."

## Nits

1. The positron shows as ⁰₁e. The spec writes ⁰₊₁e, and a "+1" pairs with the -1 on the electron (my 16).
2. The graph title "N = 1000 × (1 - 1/6)^n" uses a caret and a hyphen; a superscript n and a real minus read better
   when projected.
3. "Counting noise" wraps onto two lines at 1366x768 and 800x500. At 375 the card buttons lose their names (N1 to F2
   only).
4. Deep core with noise dates to 48,186 years (range 44,834 to 53,916) and says "Too old to date well". Fine with the
   range, but "near the end of the clock's range" fits that number better (my 11).

## Voice (Sound turned on first; held clicks, 2.2 s gaps)

| line | kind | expected | spoken |
|---|---|---|---|
| wRoll | how | 1 | 1 (on Sound on) |
| trackTip | how | 1 in 5 Track one taps | 1 |
| wNucleus | how | 1 | 1 |
| wDating | how | 1, not again on return | 1 |
| tooOld | event | 3 of 3 core dates | 3 |

Order and staleness looked right in these runs. The problems are which words (Should fix 5) and that Sound starts
off (Should fix 4).

## Checked and fine

- The Nucleus Check gives both sums ("Mass numbers: 14 ≠ 10. Charges: 6 ≠ 2.") but never the product. Working from
  the sums is the balancing skill itself, so I don't count it as a giveaway. The element name follows Z as intended.
- Reset in the middle of Roll to 10 stops cleanly (rolls 0, not busy). Calculate during a count says to let it
  finish. Motion off keeps the 400 ms roll (my 08).
- Average 20 runs hugs the dashed curve (mean 164.45 at roll 10), and the dotted mean reads clearly at 760x900.
- Fresh leaf: an estimate of 0 years is "Close." (my 13). No console errors in any of my shots.

## Audit pilot

- **Leads confirmed:** the 19 "welcome not heard" rows are real for a student who keeps the defaults. The cause is
  Sound starting off (Should fix 4), not the voice code: with Sound on, every welcome played once (my 20, 21).
- **Leads that were wrong:** the Dating lab overlap at 680x425 (g "Age estimate" over "13.6", "6.8" under a rect) is
  the pin's transparent hit box; on state-too-old-680x425 the pin and both labels are clear and legible. The "line
  drawn across" in the marked state is the expected curve crossing the half-life line, which is the point of the
  activity. Clear's "nothing changed" is the empty-progress case.
- **What it missed:** the tray's stretched grid and unreadable faces at 1366x768 and 680x425 (Should fix 1): it
  checks text and boxes, not what a canvas draws. It also missed the dead Roll buttons after roll 10 (they are only
  aria-disabled, so the walk marks them ok), the half-life line that can't reach 500 and the marking with no rolls,
  the hollow Estimate gate, the noise count that never changes, a welcome line that names the wrong next control, the
  nucleus captions that read as titles, and SVG labels drawn on the nucleon dots and the arrow over the Ba nucleus at
  375 wide (text over shapes in the same drawing, not over boxes).
