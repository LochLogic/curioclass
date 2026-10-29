PASS (exit round 1 failed two narrow items; integrator fixed both and verified by driving, 2026-10-29)
Counts: blockers 2 (general 2, family 0), should fix 14 (general 14, family 0), polish accepted 9

# Refine: half-life-dice

Builder: Codex (third single-tool test, 2026-10-29). Lenses: refine/teaching.md (1 / 6 / 4 / 3), refine/play.md
(0 / 8 / 8 / 4), refine/craft.md (1 / 8 / 4 / 3); refine/sensitivity.md PASS (rule 5 referral from Teaching, low
risk: two should fix, one nit, merged below). Merged by the integrator. Sources: T = Teaching, P = Play, C = Craft,
S = Sensitivity. Every finding is tagged general unless marked.

## Blockers

1. **Sound starts off for the whole tool** (C B1, P S4, T cross-lens note) general. `src.html` ends with
   `Curio.init(...);$('sound').click();`, so the kit's header Sound (on by default) is off on every load and a solo
   student hears no welcome, no trackTip, no tooOld (BASELINE rule 4). The spec puts only the Geiger counter's clicks
   off by default. Remove the click; header Sound stays as the kit sets it. Give the counter its own toggle,
   `Counter clicks`, off by default, next to Counting noise (Settled 1). Fix notes.md ("Sound starts off").
2. **Mark a half-life refuses a correct line and accepts one with no data** (T B1, T S2, P S2, C S7, T nit 13)
   general. The handle snaps to the expected curve's height at each half roll, so it never sits on 500 (d6: 528 or
   482), and acceptance compares the student's own noisy tray with the exact half-life: on the default seed a d12 line
   at 498 gets "Move to half the crowd" and only 544 is accepted; with 0 rolls the card says "Accepted. Expected
   crossing: 4.0 rolls". Settled 2 gives the new rule: the line moves in 25-nucleus steps (pointer and arrow keys), it
   is "on half the crowd" at 500; the card then reads the tray's own crossing (to the half roll) against the exact
   value, and when they differ by more than 0.5 rolls it says why ("One tray scatters. Press Average 20 runs to see
   the crowd hug the exact value."). Before any roll, Mark says "Roll first, then mark the half-life." and accepts
   nothing.

## Should fix

1. **The dice tray is not readable as dice** (P S1, C S1, T S4) general. The 40 x 25 grid is stretched into a wide
   short box: dice are 3 to 6 px squares in stripes with wide gaps, faces about 5 px at 1366x768, 2 px at 680x425, a
   50 px band at 375; the tracked ring is clipped at the top edge. Keep cells square (fit a centred 40:25 block, or
   choose columns from the box aspect, still 1,000 dice), faces about 9 px or more at 1366x768 and readable on a
   projector at 1920x1080, ring never clipped. Also: a die that rolls 1 is never seen showing 1 (it greys in the same
   frame). Show the roll's faces for a beat with this roll's 1s outlined in the accent (shape, not colour only), then
   grey them, with timing the same with Motion off.
2. **The d20 tray never reaches its half-life** (T S3, P polish 4) general. Rolls stop at 10 while a d20's half-life is
   13.5 and the graph runs to 16. Roll once continues to the graph's last roll for every die (Roll to 10 keeps its
   name and stops at 10); the card says so when a die needs more than 10 rolls (Settled 3).
3. **Roll buttons look live when they do nothing** (P S3, C S6, P polish 3) general. `aria-disabled` has no style, so
   at the last roll, during a roll and during Average 20 runs the buttons stay bright primary and silent. Give
   `[aria-disabled="true"]` a dimmed look, and at the last roll a card line and hint "Every roll is done. Press Reset
   for a fresh tray." Track one after the last roll says "Press Reset to track a die from the start."
4. **Roll once and Roll to 10 swallow the welcome** (C S2) general. They are in `speaks` but never speak, so a first
   tap on Roll once (the control the hint names) skips wRoll and nothing is heard. Remove them from `speaks`, and make
   sure wRoll is not lost while a roll is busy (queue it after the roll, or do not gate the welcome on busy).
5. **The Dating welcome skips Estimate** (P S5, C S3, T polish 10) general. Spoken "Drag on the ruler to estimate,
   then press Calculate" while the hint says to press Estimate first. wDating becomes the hint's words (Settled 4).
   Then Calculate shows as secondary (and its hint says "Press Estimate first") until Estimate is pressed for this
   sample.
6. **Estimate is free, and the ruler can't be read between ticks** (P S6, T S7) general. Estimate takes the untouched
   pin (1,000 years) and Calculate prints the exact age; "Close" can be found by drag-Estimate-repeat. The ruler marks
   only whole halvings, so the two real samples (10.8 and 9.07) sit between ticks with nothing to read (straight
   reads are 24 and 14 percent off). Add minor marks at their log positions (12, 11, 10, 9, 8, 7 dpm/g, and the same
   between later halvings), labelled where they fit; the pin starts unplaced for each sample and Estimate needs a
   moved pin; one Estimate per sample, then Calculate shows both side by side ("You read 3,000 years. Exact: 3,349.
   Off by 10 percent.") with no "Close" verdict before Calculate.
7. **Counting noise never varies** (P S7) general. Every recount of cave charcoal is 337 because the count is seeded on
   the sample index. Add `Count again` (with noise on) that draws the next count from the same seeded stream, so the
   same seed still gives the same sequence (Done when 7), and list the counts so far so the spread shows (Settled 5).
   The ± range stays the square root of the current count.
8. **The Geiger counter clicks the same for every sample** (C S8) general. Ten tones per count whatever the activity
   (deep core 9 tones, fresh leaf 10). Click once per counted decay, thinned (about count / 20, at seeded random times
   over the second), so a living leaf crackles and the deep core ticks twice. Plays only when Counter clicks is on.
9. **The nucleus drawing gives wrong pictures** (T S5, P S8, C S4, P polish 1, C P2) general. The legend is split as
   "Before: protons p+ (solid)" over the left and "Products: neutrons n (outlined)" over the right, read as titles;
   protons and neutrons differ by colour only (1.04:1 luminance; the 0.5 px stroke does not show); protons fill the
   centre with a neutron shell (the spiral colours the first Z dots); light nuclei are loose clouds. Titles "Before"
   and "After (your product)" over the sides, one legend line "● proton p+  ○ neutron n" with a real shape or
   lightness difference (a hollow ring or much darker neutron), protons and neutrons mixed through the cluster
   (seeded), dots sized so neighbours touch, and symbols and the arrow clear of the dots at every size (375 wide).
10. **The energy ladder has no scale and its bars cross their labels** (T S6, C S5, P polish 7) general. Bars start at
    methane on a log scale with no ticks, so methane looks like zero and carbon-14 decay like half of fission (it is
    about 1/1,300); at 680x425 and 375 each bar strikes through the next label. Draw a faint axis with ticks at
    1 eV, 1 keV, 1 MeV and 100 MeV (labelled), bars from 1 eV, at least about 22 px per rung or labels beside short
    bars, never touching a bar. (A student action on the ladder is an open question for Cory, below; do not add one.)
11. **"Dead Sea Scrolls paper" is wrong for the artifact** (S 1) general. The scrolls are mostly parchment with some
    papyrus. Name the sample "Dead Sea Scrolls fragment" everywhere (src.html, notes.md; the spec now says so), keep
    10.8 dpm/g.
12. **Teacher notes: real artifacts, textbook values; cancer care** (S 2, T nit 14) general. notes.md Good to know: one
    line that both are real artifacts but the activity values are simplified textbook examples (published radiocarbon
    studies give a range of dates across many scrolls, and real dates are calibrated; the Tutankhamun value fits the
    tomb's date of about 1323 BCE), and one line that the N3 to N5 cards touch on cancer care and thyroid treatment,
    which a student may know from their own family (rule 8). The optional context line (the scrolls are ancient Jewish
    texts found near Qumran; the seeds come from an Egyptian king's burial) may go in too.
13. **Two cards keep naming a step that is done** (P polish 8, C P1) general. After Mark is pressed the half card still
    says "Press Mark a half-life..."; after a wrong Check the change box still says "Check both sums to test it".
    "Drag the line to 500, then read the roll number." and "Fix the sum that is off, then press Check again." (and
    the hints to match).
14. **The fusion and fission energies are credited to a page that does not state them** (T polish 11) general.
    OpenStax Chemistry 2e 21.4 gives neither 17.6 nor about 200 MeV. Settled 6: the values stay, credited to OpenStax
    College Physics 2e 32.5 (D-T, 17.59 MeV) and 32.6 (average U-235 fission, 200 MeV), checked by the integrator on
    2026-10-29. Update the credits comment in src.html, tool.draft.json sources and notes.md.

## Polish accepted

1. Each roll lands: "98 of 591 live dice decayed this roll (17 percent)" in the summary, so the same fraction at every
   age shows in the student's own data, beside the tracked die's fixed chance (T polish 8, P polish 5).
2. N4 shows the gamma ray in the equation once balanced (⁰₀γ), since gamma is one of the three decays HS-PS1-8 names
   (T polish 9).
3. Steppers: add -10 and +10 steps (or press-and-hold repeat) and "or type a number" by the boxes; the start values
   stay away from every answer (P polish 2). F1 now needs 131 presses.
4. Track one rings a seeded random live die away from the edges, never clipped (P polish 3, C N2).
5. One look, one meaning: toggles that are on (Show expected, Mark a half-life, Counting noise, Counter clicks) get one
   style, distinct from the primary action buttons; Clear and New seed set apart from the seven choices; each Clear
   resets its own mode's progress, or says "Clear all progress" and asks once (P polish 6, C P3).
6. 375 wide: the graph keeps at least about 140 px of plot height (C P4).
7. Positron written ⁰₊₁e as in the spec (T nit 12, P nit 1).
8. Graph label with a true minus and a superscript n (P nit 2, C N1, family:graphing for the label style).
9. Small words: "Counting noise" not wrapping at 1366 and 800; card buttons keep a short name at 375 (P nit 3); the
   deep core with noise reads "near the end of the clock's range" when the range reaches below 50,000 years (P nit 4);
   N3 "Thyroid treatment and imaging" (S nit).

Declined: folding the six @media layers into one per breakpoint (C N3); a refactor, not a student-facing change. Do
it only if it makes the layout fixes safer.

## Settled by the integrator

1. **Sound.** Header Sound stays as the kit sets it (on). The spec's "sound off by default" is the Geiger counter's
   clicks only: a `Counter clicks` toggle, off by default. Spec line updated.
2. **Mark a half-life rule.** The spec's "accepts a reading within 0.5 rolls of the exact value" fails for one noisy
   tray (Teaching's d12 case). Replaced in the spec: the line is accepted at 500 (25-nucleus steps), the card reports
   the tray's own crossing and the exact value, and explains the scatter when they differ by more than 0.5 rolls;
   nothing is accepted before a roll. Done when 2 updated to match.
3. **Roll cap.** The spec never set one; Roll once continues to the graph's end for each die. Spec line added.
4. **wDating line.** "Pick a sample. Drag the ruler pin, press Estimate, then press Calculate." (the hint's wording, so
   one recording serves both). Spec Voice updated.
5. **Count again.** A button, not a mode; within the spec's Counting noise. Spec line added.
6. **Sources.** 17.6 MeV and about 200 MeV credited to OpenStax College Physics 2e 32.5 and 32.6 (fetched 2026-10-29:
   "17.59 MeV" for D-T; "the average fission reaction of 235U produces 200 MeV"). Spec Sources updated.
7. **Sample name.** "Dead Sea Scrolls fragment" (Sensitivity). Spec Content updated.
8. Not findings: the audit's "Age estimate over 13.6 and 6.8" (transparent hit area only), "expected curve across the
   half-life line" (the reading itself), "Clear changed nothing" (empty progress). Check giving both sums is the
   balancing skill, not a giveaway (Play, Teaching).

## Spec open questions

- **For Cory: give the student an action on the energy ladder?** (T S6, rule 2). HS-PS1-8 asks for "the energy
  released in fission, fusion and decay"; today the ladder is only shown after Check. Teaching proposes one small
  action, for example: after a card balances, the student taps the rung band where they think its energy lands
  (chemistry, keV, MeV, hundreds of MeV) before it is revealed. It would teach the scale by prediction; it adds a step
  to every card. Not sent to polish; the ticks (Should fix 10) go in either way.
- (Existing, the spec's own) 5,730 or 5,700 years: unchanged, for Cory.

## Exit check, round 1

Fresh cold agent, 2026-10-29. Frames in S:/CurioClass-codex-scratch/half-life-dice/exit/ (defaults/, b2/, b4/, b5/, b6/). Bundle 118 KB, no console errors or exceptions in any shot (only the host page's favicon 404), zero resource requests (b5/net).

- Blocker 1: held. Sound on at every size (defaults/*), Counter clicks off; held Roll once starts wRoll (b2/voice-first-roll); 0 clicks by default, leaf 68, core 2, 0 with Sound off (b2/clicks-*).
- Blocker 2: held. Before a roll Mark says "Roll first" and refuses 500 (b2/mark-before-roll-500); 525 refused, 500 accepted by keys and by a real drag (b2/mark-525, mark-500-keys, mark-500-drag); d12 8.5 vs 7.966 gives the scatter line (b2/mark-d12-cap).
- Should fix 1: held at the named targets. Square cells, faces 10.8 px at 1366, 16 px at 1920, ring clear, landed 1s outlined, same 400 ms in calm (defaults/roll-3-1366x768, b2/normal-landing-1920, b2/calm-landing). Note: at 680x425 and 375 cells are still 4 px with 3 px faces, a texture rather than dice (defaults/roll-3-680x425, roll-3-375x812); not named in the fix, integrator's call.
- Should fix 2: held. d20 rolls to 16, 465 left, crossing 14.5; Roll to 10 stops at 10 and the card says Roll once continues (b2/d20-16, d20-roll10-card).
- Should fix 3: held. Roll buttons dim during a roll, Average and at the cap; cap card and hint name Reset; Track one at the cap says "Press Reset to track a die from the start." (defaults/roll-3-1366x768, b2/cap-d6, cap-d6-track, average-mid).
- Should fix 4: held. First held Roll once speaks wRoll (b2/voice-first-roll); five rolls 2 s apart, wRoll once, nothing lost (b6/voice-5-rolls).
- Should fix 5: held. wDating equals the hint and is spoken on entry (b2/voice-dating); Calculate stays secondary with "Press Estimate first" until Estimate (b5/date-calc-first, date-drag-est-calc).
- Should fix 6: not held (regression). Unplaced pin, moved pin needed, one locked Estimate, no verdict before Calculate, "You read 1,800 years. Exact: 1,906. Off by 6 percent." all hold (b5/date-drag-est-calc). But the new minor labels repeat rounded values at different ages: "0.04 0.04" and "0.02 0.02" at 1366, "0.03 0.03" and "0.02 0.02 0.02" at 1920, around the deep core's own 0.02 (b5/ruler-1366x768, ruler-1920x1080; defaults/dating-1366x768). Fix: more digits there, or skip a label whose text matches a neighbour.
- Should fix 7: held. Cave counts 337, 324, 366, 333, same on a second load and at 375; history listed; ± 18 for 333 (b5/count-again, count-again-repeat, count-again-375).
- Should fix 8: held. Clicks follow the count (leaf 68, core 2), off by default, gated by header Sound (b2/clicks-on-leaf-core).
- Should fix 9: not held at 375 and 760x900. Titles, one legend, mixed touching nucleons and the grayscale difference hold (b4/gray-N2-1366, gray-F2-680). The arrow overlaps the Ba nucleus on F1 when balanced at 375 and 760x900 (defaults/ladder-F1-375x812, ladder-F1-760x900; b4/nuc-sweep-375x812, nuc-sweep-760x900). All other cards and sizes clear (b4/nuc-sweep-*).
- Should fix 10: held. Axis with 1 eV, 1 keV, 1 MeV, 100 MeV, bars from 1 eV, no text/bar overlaps at 375, 680x425, 800x500 (defaults/ladder-F1-*).
- Should fix 11: held. "Dead Sea Scrolls fragment" in tool and notes, 10.8 kept (defaults/dating-1366x768).
- Should fix 12: held. notes.md Good to know has the artifacts line and the N3 to N5 family line.
- Should fix 13: held. Active Mark card says "Drag the line to 500, then read the roll number."; wrong Check change box and hint say "Fix the sum that is off, then press Check again." (b2/mark-525, b4/wrong-check-1366).
- Should fix 14: held. Credits comment, tool.draft.json and notes cite College Physics 2e 32.5 and 32.6.
- Polish 1: held ("124 of 715 live dice decayed this roll (17 percent).", defaults/roll-3-*).
- Polish 2: held (N4 balanced shows gamma, b4/N4-gamma). Polish 3: held (+10/-10 on desktop, type hint, hold repeat 10 to 21, b4/stepper-hold).
- Polish 4: held (ring inside the tray, crop-1366-tray). Polish 5: held (toggles inset outlined, actions solid, dashed New seed and Clear; each Clear only its own mode, b5/persist-b-reload).
- Polish 6: held (phone plot 138 px, b6/phone-plot). Polish 7: held (0 +1 e, b4/N5-positron). Polish 8: held (true minus, superscript n).
- Polish 9: partly held. Counting noise on one line at 1366 and 800; core noise reads "Near the end of the clock's range" (b6/core-noise); N3 "Thyroid treatment and imaging". Not held: at 375 the card buttons still show only N1 to F2 (defaults/nucleus-375x812). Polish, not blocking.
- Settled 1 to 8: held as written (sound, 500-only rule, roll cap, wDating line, Count again button, sources, sample name; the Settled 8 non-findings still are).
- Done when 1: held (expected 161.51 at 10, 20-run mean within 5.6 at every roll, b2/done-1-2). Done when 2: held (all seven exact values match Content; 500 accepted with tray and exact value).
- Done when 3: held (chance 1 in 6 at every age, b2/done-3-track). Done when 4: held (all seven accept only the right product, mass and charge failures named, b4/nucleus-checks).
- Done when 5: held (four rungs and the 22 million line). Done when 6: held (1,906; 3,349; 22,920; core too old with tooOld spoken; ± is the root of the count, b5/date-ages, date-core-voice).
- Done when 7: held (same seed same tray, new seed differs, progress survives reload, Clear resets, calm shows faces, b5/seed-same, persist-*, b2/calm-landing).
- Done when 8: held except the items above. Tray, graph and buttons in view at all six sizes (defaults/*; nucleus at 680x425 has 5 px of panel cut, controls visible); Tab reaches every control in order, the pin and line handles take arrows with a visible ring (b5/kb-*, b6/pin-focus).
- Gate: codes taught (energy-ladder action stays Cory's open question), solo defaults good, sensitivity PASS, voice counts right (22 lines in lines.json match the tool exactly), contract clean. Open: Should fix 6 and 9 as above.

## Audit pilot (exit)

audit-exit/audit.md was not written when this check finished (frames only, still running); no leads to mark.

## Integrator fixes after exit round 1 (2026-10-29)

- Should fix 9, fission arrow over Ba at 375 and 760x900: the arrow moved from mid-stage into the title row (y 33,
  16 px), between "Before" and "After (your product)". Checked F1 balanced at 680x425, 800x500, 760x900, 1366x768,
  1920x1080 and 375 (host): arrow box touches 0 nucleons and 0 text. Frames: exit/fix/fix-ladder-F1-*.png.
- Should fix 6 regression, repeated ruler minor labels: a minor label is skipped when its text is already on the ruler.
  Checked at all five ruler sizes: 0 repeated labels (14 to 44 labels). Frames: exit/fix/fix-ruler-*.png.
- Not blocking, left for Cory: Polish 9 partly held (at 375 the card buttons show only N1 to F2, no short names); the
  dice tray at 680x425 and 375 still reads as a texture (4 px cells, 3 px faces), fine at the sizes the review named.
- No fresh exit round was run on these two changes (one SVG text position, one label filter); the drive checks above
  are the evidence.
