# Craft lens: half-life-dice (round 1)

Cold read of spec.md, src.html, notes.md, voice/lines.json, tool.draft.json, codex-report.md and handoff.md (the last
two read as claims). No art/prompts.json: the spec has no art, so step 5 does not apply. Bundle used as built
(tools/half-life-dice/half-life-dice.html, 107,155 bytes, newer than src.html and the kit). Shared audit:
S:/CurioClass-codex-scratch/half-life-dice/audit-r1/audit.md. My frames and logs:
S:/CurioClass-codex-scratch/half-life-dice/lens-craft/ (voice/*.json and .png, frames/*.png and .json).

Counts: blockers 1, should fix 8, polish 4, nit 3.

## Blocker

**B1. Sound starts off for the whole tool, not just the Geiger clicks.** src.html:145 `Curio.init(...);$('sound').click();`
flips the kit's Sound (default on, not saved) to off on every load. The spec puts only the counter clicks off by
default ("A Geiger counter clicks (sound off by default)"). Because of this, a student gets no narration at all
unless they find Sound: no welcome, no trackTip, no tooOld. notes.md ("Sound starts off") documents the wrong
behavior. Seen in: voice/def-first-roll.json (first tap Roll once, Sound `false`, log empty), every audit frame
(header shows the muted Sound icon), and the audit's "welcome not heard" rows for 19 first taps. Better: remove the
`.click()`, keep header Sound on as the kit does, and give the counter its own clicks toggle (off by default, as the
spec says), or gate the tone on Counting noise. Then update notes.md. Without this the voice check cannot pass under
the defaults (gate item 7). *general*

## Should fix

**S1. The dice tray can't be read at any size.** drawTray (src.html:113) fits the fixed 40 x 25 grid to the box, so
cells are much wider than tall (about 26 x 7 px at 1366x768) and each die is a square sized to the short side. The
tray shows as 40 thin striped columns with 5 to 6 px dice. Faces are not readable, the tracked ring is hard to find,
and at 375 wide the whole tray is a 50 px band. Seen in: frames/zoom-tray-1366.png, tray-1920.png (still stripes at
1920x1080), d20-ten.png (two-digit faces become specks), h375-tray.png. The spec wants "each a small square with its
face". Better: keep cells square, either by fixing the tray box to the 40:25 aspect and centering it, or by giving the
tray row enough height (as is, the graph takes most of the height). Faces are still readable at about 9 px. *general*

**S2. Roll once and Roll to 10 are listed in `speaks` but never speak.** src.html:93 `speaks:'#track,#calculate,#roll-once,#roll-ten'`.
A first tap on Roll once (the control the hint names) skips the welcome, so nothing is heard. wRoll stays unheard
until the student changes mode, which means the premise "Every 1 is a decay." is lost for the most likely first
action. Seen in: voice/ft-rollonce.json (Sound turned on before the tap, log empty after 8 s); compare ft-die.json
(d20 first, wRoll after 134 ms). Better: drop `#roll-once,#roll-ten` from `speaks`. The welcome's own
`valid: !state.busy` then drops it during the roll and leaves it unmarked, so it should go through V.welcome() again
once the roll ends, or the welcome should not be gated on busy. *general*

**S3. The Dating welcome tells students to skip a step.** Spoken wDating: "Pick a sample. Drag on the ruler to estimate,
then press Calculate." The hint shown at the same moment reads "Pick a sample. Drag the ruler pin, press Estimate, then
press Calculate." A student who does what they heard gets "Press Estimate to record your ruler pin before Calculate."
To keep the spoken line naming an enabled control, the builder left Calculate enabled, styled primary, ahead of the
step it needs (handoff.md says so). Seen in: voice/rep-modes.json and read-cut.json (wDating spoken while the hint shows
hint12); frames from the audit, state-mode-dating-lab-*.png (Estimate and Calculate look the same). Better: wDating
becomes the hint12 wording (a small spec line change for the integrator to settle), and Calculate shows as secondary or
says "Estimate first" until Estimate is pressed. *general*

**S4. Protons and neutrons differ only by color, and the legend words are wrong.** Protons `#ff8f6b` and neutrons
`#9fb3c8` have a luminance contrast of 1.04:1 (computed), so in grayscale and for many color-blind students they look
alike. The 0.5 px neutron stroke does not show (frames/zoom-nuclei-1366.png). The legend is split across the two
halves as "Before: protons p+ (solid)" and "Products: neutrons n (outlined)" (src.html:131), which reads as though the
left side holds only protons and the right side only neutrons. Seen in: audit state-right-1366x768.png,
nucleus-f1-1366.png, h375-ladder.png. Better: a clear difference in shape or lightness (a hollow ring for neutrons, or a
much darker neutron fill), and one legend line, "● proton p+  ○ neutron n", over both sides. *general*

**S5. Energy ladder bars cross their labels at 375 wide.** drawLadder places each label 5 px above its bar, but the row
pitch at that height is about 13 px, so every bar strikes through the next label ("D-T fusion: 17.6 MeV" is crossed
out). Seen in: frames/h375-ladder.png, zoom-ladder-375.png, and audit state-right-375x812.png. The audit marked this
state clean. Better: set a minimum row height (label above bar, about 22 px per rung), or put labels to the right of
short bars. *general*

**S6. Disabled roll buttons look live.** After 10 rolls, and during a roll, Roll once and Roll to 10 get
`aria-disabled="true"` (src.html:105), but nothing in the kit, the theme or the tool styles that state. They stay bright
green primary buttons that do nothing and say nothing. The same goes for Average 20 runs while it runs. Seen in: audit
state-d6-ten-1366x768.png, d20-ten.png. Better: a dimmed style for `[aria-disabled="true"]` (and a short "10 rolls done.
Press Reset for a fresh tray." in the card). *general*

**S7. The half-life line can't be put on 500, and it is "Accepted" before any roll.** The handle's `snap` puts y on
expected(n) for whole and half rolls (src.html:115), so for a d6 the line jumps from 528.3 to 482.3 and never sits at
500. Yet the hint says "Drag the graph handle to 500 nuclei" and the card says "Move the line to half the starting
crowd." On a fresh tray (0 rolls) the card reads "Accepted. Expected crossing: 4.0 rolls" because it falls back to the
expected curve. Seen in: frames/mark-reach.json (every reachable y, each step labeled; 3.5 and 4 both accepted at 0
rolls), audit state-marked-680x425.png. The spec asks for the reading to snap to half rolls, not the line. Better: let
the line move in steps of 10 to 25 nuclei (so 500 is reachable), snap the reading to half rolls, and ask for a roll
before accepting a mark. Teaching may weigh the giveaway side too. *general*

**S8. The Geiger counter clicks the same for every sample.** countSample (src.html:129) plays one tone per 100 ms
frame, 10 per count, whatever the activity. Measured with Sound on: deep core wood (2 counts) gave 9 tones, fresh leaf
(1,360 counts) gave 10 (frames/geiger.json). A counter's sound is a meter, and here it says a dead sample and a living
leaf are equally active. Better: click once per counted decay, thinned (for example, about count / 20 clicks spread at
Poisson-random times over the second), so the leaf crackles and the core ticks twice. This goes with B1's separate
clicks toggle. *general*

## Polish

**P1. The half-life card still says "Press Mark a half-life" after Mark is pressed.** With Mark on and the handle not yet
moved, #half-card reads "Press Mark a half-life. Move the line to half the starting crowd." (frames/h375-tray.png,
tray-1920.png and d20-ten.png with Mark pressed). Better: "Drag the line to 500, then read the roll number." *general*

**P2. Small nuclei don't look packed.** Nucleons are drawn on a sunflower spiral with a fixed radius and dot size worked
out from the circle, so C-14 is 14 scattered 3 px dots with gaps (zoom-nuclei-1366.png), and H-2 and H-3 are two or
three dots far apart, with the symbol drawn over them at 375 (h375-ladder.png). The spec says "packed protons and
neutrons". Better: size the dots so neighbors touch (dot radius about rad / sqrt(A) x 0.9) and shrink the nucleus to
fit A. Large nuclei (U, Ba, Kr) already look right. *general*

**P3. One Clear wipes both modes, with no confirmation.** Clear in Nucleus also clears the dated samples
(frames/clear-cross.json: "3/7 samples dated" became 0 after Clear in Nucleus). Better: each Clear resets its own mode,
or the button says "Clear all progress" and asks once. *general*

**P4. At 375 wide the graph's plot area is about 45 px tall** (h375-tray.png, audit state-tracked-375x812.png): 1000, 500
and 0 crowd together and the observed points are hard to tell from the curve. With S1 fixed, give the graph a minimum
of about 140 px of plot at phone width. *general*

## Nits

- **N1.** The graph's equation label uses an ASCII hyphen and a caret, "N = 1000 × (1 - 1/6)^n" (src.html:115). A true
  minus and a superscript n would match Plane.fmt's style. *family:graphing*
- **N2.** Track one always picks the lowest-numbered live die, so the first tracked die is always die 1 in the top
  left corner (frames/tray-1920.png). A seeded random live die would feel less staged. *general*
- **N3.** The style block is six layers of @media overrides restating the same selectors (src.html:4 to 64), which
  will make the polish round's layout fixes (S1, S5, P4) easy to get wrong. Fold them into one block per breakpoint
  while fixing. *general*

## Checked and clean

- **Contract:** one file, 107 KB; no `src=`, external `href`, `@import` or `url(http`; the only `new Audio` is the kit's
  clip player. No console errors or exceptions in my 41 driven shots (the only error was the host page's favicon 404).
  Kit used for Motion, Sound, Read, tones, voice and Plane, with nothing re-implemented. Title, description, lang,
  charset and viewport are present.
- **Access:** the Tab order runs header, die picker, roll controls, toggles (frames/tab-order.json). Nothing takes focus
  on load (focus-load: BODY). The focus ring is clearly visible (focus-die.png). Targets are 44 px (audit clean at every
  size). Live and decayed dice differ by more than color (6.76:1 plus an x). Motion off: no animations, and roll timing
  is kept (calm-roll.json: still busy at 150 ms, 0 animations).
- **Lines:** all 17 strings from `__tool.allLines()` match voice/lines.json word for word, in order (frames/lines.json).
  `tooOld` is in EVENT_IDS. The 12 hint lines are Read-only and correct for their states.
- **Words:** no em dashes in src.html, notes.md, lines.json, tool.draft.json or handoff.md. "Curio Class" is never
  shortened. Classroom-safe throughout. Privacy: "Saved on this device only" sits under the cards and samples in both
  modes.

## Standard voice check

Driven with held clicks (0.12 s), Sound on (switched on before the first tap with a scripted click, because of B1),
Motion on, 1366x768. Gaps were 5 s for repeats and 0.2 to 1.2 s for the stale runs. Logs: lens-craft/voice/*.json.

| line | kind | action | expected | spoken |
|---|---|---|---|---|
| trackTip | how | Track one x5 | 1 | 1 (then not queued) |
| wRoll | welcome | first tap on a die | 1 | 1 |
| wRoll | welcome | first tap on Roll once | 1 | **0** (S2) |
| wRoll | welcome | first tap with Sound at its default | 1 | **0** (B1) |
| wNucleus | welcome | Nucleus x2 in a mode cycle | 1 | 1 |
| wDating | welcome | Dating lab entry | 1 | 1 (wording S3) |
| tooOld | event | Calculate x5 on deep core | 5 | 5 |
| read | read | Read x5 | 5 | 5 |
| (none) | - | Roll once x5, Check x5, die x5 | 0 | 0 |

1. **Repeats:** right for every line the tool speaks (table). The first two tooOld lines were cut by the next one
   (`now`), because the headless browser voice ran past the 5 s gap. That is expected for an event line with `now`.
2. **Stale:** Dating, core, Estimate, Calculate, Roll, Reset at 1.2 s: tooOld was cut by the mode change (`hush`),
   then wRoll started and was cut by Reset. Nothing played after its moment. Track then Reset at 0.2 s: trackTip
   was cut (`hush`) and not replayed. Mode buttons at 0.2 s: each welcome was cut by the next mode, and only the
   current one was left (voice/stale-*.json).
3. **First tap:** stage (tray) gives wRoll at 129 ms; key (Tab) gives wRoll at 2 ms; Nucleus gives wNucleus at
   144 ms; Track one gives trackTip only; Read gives the hint only; d20 gives wRoll. Roll once gives nothing (S2).
   With the default Sound: any first tap gives nothing (B1), and Sound as the first tap turns Sound on and gives
   wRoll, which is right for a Sound-on tap. Sound on, off, on (1.1 s apart) brings wRoll once, cut by the off, and
   it does not come back. That is kit behavior (a line is marked said when it starts), not this tool's.
4. **Read:** Read 0.75 s into wNucleus cut it and spoke the hint. Dating 0.75 s after Read started wDating at once.
   Read with Sound off spoke the hint (voice/read-cut.json, read-soundoff.json).
5. **Order:** Track then Dating lab 0.4 s later: trackTip was cut, wDating followed. No older line played after a
   newer one (voice/order.json).

## Audit pilot

**Leads confirmed:**
- "Welcome not heard" after 19 first taps: true, and the main cause is B1 (Sound starts off), which the audit row for
  `#sound` hints at (welcome heard only there). With Sound on, the same rows clear except Roll once and Roll to 10,
  which stay silent for a separate reason (S2).
- The header Sound starts off: confirmed at src.html:145. The spec scopes "off by default" to the Geiger clicks only.

**Leads that were wrong:**
- "Age estimate overlaps 13.6" and "6.8 under rect" at 680x425 (four states): this is only the handle's transparent
  hit rectangle. The visible diamond sits below the bar, clear of every label (frames/zoom-ruler-680.png).
- "Expected curve drawn across Half-life line" (marked, five sizes): the dashed curve meets the handle where the line
  crosses it, which is the reading itself, not a clash.
- "Clear: nothing changed" in both modes: the audit ran on empty progress. Clear works (clear-cross.json), but see P3.

**Found that it missed:**
- S1: the tray is unreadable at every size. The audit checks boxes, not canvas content.
- S5: ladder bars cross their labels at 375. The audit's "line drawn across" check did not catch SVG `line` elements
  over `text` in this state.
- S3: the spoken welcome and the hint give different steps.
- S4: nucleon colors at 1.04:1, with a misleading legend.
- S6: aria-disabled buttons styled as live.
- S7: the half-life line can't reach 500, and a mark is accepted with no data.
- S8: the Geiger clicks don't follow the count.
- P1 and P3: card wording that is wrong for the state, and Clear's reach across modes.
