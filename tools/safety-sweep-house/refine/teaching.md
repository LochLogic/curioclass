# Teaching lens: safety-sweep-house (round 1)

Lens: Teaching. Bundle as built (not re-bundled). My frames: `S:/CurioClass-codex-scratch/safety-sweep-house/teaching/frames/`
(peek-safe, peek-unsafe, chat-think, heater-think, heater-2p5, gummies-fix, pills-everyone, towel-fix; 1366x768).
Shared audit frames used: state-room, state-safe, state-heater-ruler, state-safety-card (1366x768 and 680x425).
Counts: blocker 0, should fix 6, polish 4, nit 1.

## Findings

1. **Choose (renderFocus, src.html:846-857): peeking at the safe option labels it "Safe result" on the stage before
   the student picks.** `p.last` is set by the peek button, and the stage card for that index is drawn with the green
   edge, "✓ Safe result" and the habit line whenever `i === h.safe`. Peek each option in turn and the stage names the
   answer, so the 5.5.3 comparison and the 5.5.4 choice need no judgment. Better: a peek shows only the neutral
   "What could happen" card for every option; the Safe label and habit appear only after the pick.
   Seen: frames/peek-safe.png (Kitchen / Cleaners, Choice 2 peeked, stage reads "✓ Safe result ... Never mix
   cleaners."). Level: **should fix**. Tag: general.

2. **Choose (content.json options): the cheap pass "pick the option that brings in a grown-up" is right 12 of 12, and
   "pick the longest option" 10 of 12.** Every safe option names a grown-up, Dad or Grandma June ("then tell a
   grown-up", "Get Dad back..."), and no unsafe option does. The spec's own check balanced position (4/4/4) but not
   wording. A student can pass 5.5.4 without reading an outcome. Better: give at least one distractor per hazard a
   grown-up in a wrong way (tell later, wait for a grown-up to notice, ask a grown-up while leaving Theo by the tub),
   and trim the safe options so they are not the longest. Seen: python over content.json options (keyword
   grown-up/tell/Dad/Grandma: safe-only on 11, safe plus "Tell them your school" on Chat; longest = safe on 10).
   Level: **should fix**. Tag: general.

3. **Think (src.html:360-361, 615-617): the help rule contradicts the Heater answer and is shown unchanged on every
   hazard.** The rule says "Medicine, fire, heat or climbing: get a grown-up first", yet the Heater's answer is "Act
   now, then tell"; the code patches this with a heater-only sentence ("You may move a cool blanket away from heat
   without touching the heater") that then appears on all twelve hazards, including the Game room chat. A student
   applying the stated rule to the heater is marked "Here, the safer help choice is: Act now", and the rule they were
   just taught is the reason they were wrong. The spec's general sentence ("If you can make it safe without touching
   those, act now, then tell") was dropped. Better: the spec's general rule, plus one line specific to the current
   hazard explaining why it falls on its side. Seen: frames/heater-think.png, frames/chat-think.png. Level:
   **should fix**. Tag: general.

4. **Check / fix (Gummies hazard 6 and Towel hazard 1, content.json fix lines): after "get a grown-up first", the
   student still does the grown-up's part.** Gummies: "Tap Tell Dad, then help him drag the closed bottle up to the
   high cabinet": the student carries the medicine (the art is an amber pill bottle). notes.md says "Adults handle the
   medicine" (Support at home) and children "do not ... put medicines away alone" (Good to know), and the habit is
   "Vitamins are medicine too". Towel: the safe outcome says "Dad moves the towel", then the fix asks the student to
   drag the towel to the hook. 7.5.2 is "demonstrate practices", so the practice demonstrated must be the one taught.
   Better: Gummies, the student taps to watch Dad put it up (as the lighter does) or keeps Theo away; Towel, Dad's
   chip moves it and the student's step is something a child does (step back, keep Theo out of the kitchen). Seen:
   frames/gummies-fix.png, frames/towel-fix.png. Level: **should fix**. Tag: general.

5. **Who is safer reveal (reason(), src.html:694-698): the Theo reason line does not match the hazard.** It reads
   "Keep medicine out of little kids' reach. Grown-ups stay with them near water." on all four Theo hazards, so Pills
   and Gummies are explained by water and Tub and Gate by medicine. It also differs from the spec's line. The reason
   is the 5.5.5 reflection, so it should be about this fix. Better: a reason line per hazard in content.json. Seen:
   frames/pills-everyone.png (Pills reveal ends "near water"). Level: **should fix**. Tag: general.

6. **Heater ruler (src.html:886-887, 1067-1073): the foot labels drift up to about a quarter foot from the true
   marks.** The labels are spaced by `justify-content: space-between` with padding, while the blanket position and
   the 3-foot check use the ruler's outer edges. Measured at 1366x768: the true 3 ft point is x=663, the "3 ft" label
   spans 642-661; true 0 ft is 275, label at 289; true 4 ft is 792, label ends at 778. A student who lines the blanket
   up with the "3 ft" label is at about 2.85 ft and hears "Still too close", on the one measured fact in the tool.
   The bubble readout is right, so this is a mismatch rather than a lie. Better: place each label centered on its
   tick (absolute left = n/4 of the ruler). Seen: frames/heater-2p5.png plus measured rects. Level: **should fix**.
   Tag: general.

7. **Room view (renderRoomObjects): 5.5.1 is thin.** Each room has exactly three tappable cutouts with a hover ring;
   two are hazards and the third tells the student it is fine. Nothing asks the student to decide "risky or fine"
   before the tool says so, so telling hazards from look-alikes is done by the tool, not the student. Better: tapping
   any object first asks "Risky or looks fine?" (two buttons, never scored, like Think), then opens the decision or
   the Looks fine card. This changes the spec's flow, so it belongs in the spec's open questions if not taken.
   Seen: audit state-room-1366x768.png, code. Level: **polish**. Tag: general.

8. **Who is safer, over-picking (src.html:663-673): picking "Everyone" on a Theo or You hazard gets no feedback.**
   The Everyone chip stays pressed with no mark, the right chip shows "✓ Safer", and the reason line never says why
   the fix mostly protects one person. Better: a short "Mostly Theo: ..." line or an outline on the over-picked chip
   with a word of why. Seen: frames/pills-everyone.png. Level: **polish**. Tag: general.

9. **Candle and Lighter fixes are watch-only (hold the candle "to watch her blow it out", tap "to watch Dad put it
   away").** That is right for safety, but the student demonstrates nothing; the Safety card then says "Twelve fixes,
   made by you." Better: give the child's real part an action (step back and keep Theo away, point Dad to it) and
   word the card as "made safer by you and your grown-ups". Seen: content.json, audit state-safety-card-1366x768.png.
   Level: **polish**. Tag: general.

10. **Poison Help and the 911 line appear only after all six rooms.** A class that sweeps two rooms never sees the
    number, though the Cleaners and Gummies hazards are exactly when it applies. Better: show the Poison Help line on
    the safe outcome of those two hazards as well. Seen: code (renderSafety only), spec Safety card. Level: **polish**.
    Tag: general.

11. **Look-alike accessible names read like the answer** ("pot back burner", "battery candle", "medicine cabinet
    high", "life jacket hook"), while hazards are named by title ("Cleaners", "Towel"). A screen-reader user hears
    which object is the safe one. Better: neutral names for all three (for example "pot on stove", "candle",
    "cabinet"). Seen: src.html:819. Level: **nit**. Tag: general.

## Done when

1. Focus: pass (state-safe, peek frames: hazard large left, outcome cards beside it).
2. 1366x768 and 680x425 fit: pass (audit clean rows).
3. Taps take effect at once: not mine to judge; audit resize and held-click rows clean.
4. Look-alikes open "Looks fine", never a decision card: pass (code path at src.html:828-838).
5. Think before options, split 6 and 6: pass (pick() guards on `p.think`; adult true on 6, false on 6, recomputed).
   But see finding 3.
6. All three outcomes side by side after the safe pick; no path to Check without it: pass (state-safe frame;
   goStep('fix') guard). But see findings 1 and 2.
7. Who is safer matches Content: sets pass (Everyone 6, Theo 4, You 2, recomputed); reason lines fail (finding 5).
8. Twelve fixes with fixed art and check; habits on card and Safety card: pass mechanically (safety-card frame shows
   all twelve habits), with findings 4 and 9 on what the fixes teach.
9. Rooms light; Safety card with 1-800-222-1222 and the 911 line: pass (state-safety-card frames).
10. Voice counts: left to the Craft lens.

## Facts

Spot-checked against the spec Sources and my own knowledge of those sources: Poison Help 1-800-222-1222, free, 24/7, US
(HRSA); bleach plus ammonia makes a harmful gas, also outdoors; candles 12 inches from anything that burns; space
heaters 3 feet; smoke alarms tested monthly; escape plan two ways out and an outside meeting place; get out, stay out,
call 911 from outside; a young child can drown in a few inches of water, quickly and silently; pool gates self-close
and self-latch; pot handles turned to the back; child-resistant caps are not childproof. All correct. 3 feet = 36 in,
6-inch arrow steps = 0.5 ft (code uses 0.5): correct.

## Grade, notes, guardrails

Language is plain and right for grades 3-5. Teacher notes name the sensitive topics (poisoning, fire, drowning, online
strangers) and the disclosure procedure (rule 8): good. No points, timers or win states. notes.md "Good to know" and
"Support at home" are true of the tool except where finding 4 contradicts them (the tool has the child put medicine
away). Home ideas are doable tonight.

Sensitivity: no cultural, Native or hard-history content. The people set (Dad, Grandma June, Theo) goes to the rule 11
people review as the spec already says; not judged here.

## Audit pilot

- Leads confirmed: none to confirm for teaching. The one lead ("hint out of view" on the Safety card) is a layout
  matter; on the 1366x768 frame the hint sits in the panel behind the card's overlay, which is by design while the
  card is open.
- Leads wrong: none found.
- What it missed (as expected, all outside a mechanical audit): the peek giveaway (finding 1), the grown-up keyword
  cheap pass (2), the rule that contradicts its own answer (3), the child doing the adult's step (4), the mismatched
  reason line (5), and the ruler label drift (6, measurable, but only by comparing labels to the check's geometry).
