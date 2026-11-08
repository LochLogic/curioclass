OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 0 (general 0, family 0), should fix 15 (general 15, family 0), polish accepted 13

# Refine: safety-sweep-house

Lens files: refine/teaching.md, refine/play.md, refine/craft.md (no sensitivity.md; rule 5 does not apply).
Frames: teaching `S:/CurioClass-codex-scratch/safety-sweep-house/teaching/frames/`, play `.../play/out/`,
craft `.../craft/out1..out3/`, shared audit `.../audit-r1/`. Integrator spot-checked items 1, 2, 4, 6 and 8 in
src.html and content.json, and frames peek-safe.png and room4.png.

## Blocker
None.

## Should fix
1. **Peeking labels the answer on the stage.** src.html:843-857 (renderFocus). The peek button sets `p.last`
   (src.html:640), and the stage outcome card for that index is drawn with the green edge, "✓ Safe result" and the
   habit line whenever `i === h.safe`. Peek each option in turn and the stage names the safe one before any pick, so
   5.5.3 and 5.5.4 need no judgment. Seen: teaching/frames/peek-safe.png (Kitchen / Cleaners, Choice 2 peeked, stage
   reads "✓ Safe result ... Never mix cleaners."); confirmed in code. Fixed: before the safe pick, every peeked or tried
   card on the stage is the same neutral "What could happen" card (no green edge, no Safe label, no habit); the Safe
   label and habit appear only after the safe pick. (general)
2. **Choose is solved by "pick the option with a grown-up in it" (12 of 12) or "pick the longest" (10 of 12).**
   content.json options (spec Content). Every safe option brings in a grown-up ("then tell a grown-up", "Get Dad
   back", "Get a grown-up to blow it out") and no unsafe one does; the safe option is also longest on 10. Seen: script
   over content.json by both Teaching and Play, then played h00 to h11 (play/out). Fixed: on most hazards one wrong
   option carries a grown-up in a wrong way ("Tell Dad later, after your game", "Wait for a grown-up to notice", "Call
   a grown-up from the hall and leave Theo by the tub"); a few safe options with no grown-up word where the spec's
   Think answer is "Act now" (pot handle style, closing the pop-up) and mixed lengths, so neither rule beats about 5 of
   12. Keep the outcome meanings, the 4/4/4 safe positions and the Think split; update the matching option text in
   the spec's Content list with the same edit. (general)
3. **The student does the grown-up's part on Gummies and Towel.** content.json `fix` for hazard 6 ("Tap Tell Dad,
   then help him drag the closed bottle up to the high cabinet") and hazard 1 ("Tap Tell Dad. When the towel is cool,
   drag it onto the hook"). The child carries the medicine, against notes.md ("Adults handle the medicine"; children
   "do not ... put medicines away alone") and the habit "Vitamins are medicine too"; on Towel the safe outcome says
   "Dad moves the towel", then the student moves it. 7.5.2 demonstrates the practice taught, so it must be the right
   one. Seen: teaching/frames/gummies-fix.png, towel-fix.png. Fixed: Gummies, after Tell Dad the student taps to
   watch Dad put the bottle up (as Lighter does) or keeps Theo away from the counter; Towel, Dad's chip moves the towel
   and the student's step is a child's step (step back, keep Theo out of the kitchen). Keep the engine's existing
   drag/tap/watch actions; update the two spec Fix lines to match. (general)
4. **The help rule contradicts the Heater answer and names the blanket on every hazard.** src.html:360-361 (`helpRule`),
   615-617, 435. The rule reads "Medicine, fire, heat or climbing: get a grown-up first. You may move a cool blanket
   away from heat without touching the heater...", shown and read on all twelve, including the chat, pop-up, tub and
   gate; the spec's general sentence ("If you can make it safe without touching those, act now, then tell.") was
   dropped, so a student who applies the rule to the heater is told they were wrong. Seen: teaching/frames/heater-think.png,
   chat-think.png; craft finding 4. Fixed: the spec's rule line word for word on every hazard, plus one short line per
   hazard (content.json) saying why this one falls on its side (Heater: "The heater stays untouched; a blanket you can
   pull away is safe to move."). (general)
5. **Heater ruler labels sit off the marks the check uses, and the ruler is clipped at 680x425.** src.html:144-150,
   886-887, 1067-1073. Labels are spread with `justify-content: space-between` plus padding while the blanket and the
   3-foot check use the ruler's outer edges: at 1366x768 the true 3 ft point is x=663 but the "3 ft" label centers
   near 651, so the blanket's edge on the label reads "2.9 feet" and "Still too close"; the tick under "2 ft" cuts its
   text; at 680x425 the ruler's lower part is cut off and "0 ft" sits on the half-foot tick. Seen: craft/out3
   ruler-2-9.png, teaching/frames/heater-2p5.png, play/out/h05-fix-680.png, play/crop-680-ruler.png, audit
   state-heater-ruler-375x812.png. Fixed: each label absolutely placed at n/4 of the ruler width, centered on its
   tick, measured from the visible blanket edge; the whole ruler inside the stage at 680x425 and 375 wide. (general)
6. **"Who is safer" Theo reason line does not match the hazard.** src.html:694-698 (`reason`). On all four Theo hazards
   it reads "Keep medicine out of little kids' reach. Grown-ups stay with them near water.", so Tub and Gate are
   explained by medicine and Pills and Gummies by water; it also differs from the spec. Seen:
   teaching/frames/pills-everyone.png, play/out/h07-reveal.png; confirmed in code. Fixed: a reason line per hazard in
   content.json, built from the spec's three lines (Theo: "Little kids can't read labels or swim, so grown-ups and big
   kids keep things out of reach." as the base) and naming this hazard. (general)
7. **Picking "Everyone" on a Theo or You hazard is never corrected.** src.html:663-673. `selected` is true for every
   chip once Everyone is in `p.who`, so the right chip shows "✓ Safer", Everyone stays pressed with no mark, and the
   reason line never says why it mostly protects one person; "always Everyone" passes all 12, though the spec's own
   check says "the reveal corrects the rest". Seen: play/out/everyone-theo.png, teaching/frames/pills-everyone.png.
   Fixed: on the reveal, an over-wide pick gets an outline and a short line ("Mostly Theo this time: ..."), never a
   red mark or a score. (general)
8. **Fix hint repeats "Tap Tell" and keeps saying it after the grown-up is here.** src.html:549-552 (hintFor) with
   content.json `fix`. Before Tell it reads "Tap Tell Dad first. Tap Tell Dad. When the towel is cool, ..." (Candle,
   Pills, Smoke alarm, Gummies, Lighter too); after Tell the hint still starts "Tap Tell Dad" while the panel shows
   "Dad is here." and no Tell button. Seen: play/out/h01-fix.png, h02-fix.png, h06-fix.png, audit
   state-alarm-hold-680x425.png; craft finding 3; confirmed in code. Fixed: before Tell, "Tap Tell Dad first." alone
   (or the fix with its leading "Tap Tell X." stripped); after Tell, only the student's remaining step. Read speaks
   the same. (general)
9. **Disabled buttons look live.** src.html:41-45 (no `button.b:disabled` style). Done before any chip and Report
   before Block look enabled; a student taps Report first and nothing happens, with no hint change. Seen:
   play/out/h04-acted.png, audit state-chat-controls-1366x768.png. Fixed: a clear disabled look (muted, no press
   motion, `cursor: default`), and a tap on disabled Report re-states "Tap Block first." in the hint. (general)
10. **Keyboard focus falls to the page after the stage House button or Escape.** src.html:483-491. The fallback tries
    `#controls` (no button in house view), `#house` (gone) and `#rooms-small` (hidden at this size), so focus lands on
    BODY. Seen: craft/out3 house-key, craft/out2 esc. Fixed: fall back to `#nav-house` or `#room-0` in house view.
    (general)
11. **The search is three oversized stickers, and the Game room's chat and pop-up float in mid-air.**
    src.html:775-841 (renderRoomObjects), art placement. The smoke alarm is as big as the bench, the gummy jar fills
    the counter, and the Game room shows its three items as white plaques across the room, not on the monitor, though
    the spec says "in plain sight but small, as in a real room" and draws the chat and pop-up on the blank screen.
    Seen: play/out/room2.png, room3.png, room4.png (integrator viewed room4), audit state-chat-controls-1366x768.png.
    Fixed: cutouts sized to the room's scale (still 44 px tap targets), chat, pop-up and the Maya line drawn on the
    monitor in room and fix views. (general)
12. **The option words vanish once a card flips.** src.html:626-633. A tried card, and all three after the safe pick,
    show only the outcome, so the side-by-side compare has no record of which action led where. Seen:
    audit state-safe-1366x768.png, play/out/h05-tried.png. Fixed: keep the option as a small line above its outcome on
    every flipped card. (general)
13. **Two tubs while it drains.** src.html:870, 879. During the 1.5 s drain the full-tub overlay and the empty-tub art
    are drawn at different sizes and positions, so two ghosted tubs overlap. Seen: play/out/h07-acted.png. Fixed: the
    two layers share one box, or the swap is a crossfade in place. (general)
14. **Composite art reads broken in three rooms.** Kitchen: the `towel-burner` cutout is a whole small stove standing
    on the floor in front of the painted range, and the pot look-alike stacks on a painted pot; Living room: the
    curtain cutout has a hard flat top beside the window; Pills fixed: a second table pasted over the painted coffee
    table. Seen: play/crop-1366-pot.png, crop-1366-candle.png, play/out/h03-back.png, audit state-room-1920x1080.png.
    Fixed: cutouts placed on the painted surfaces with no hard edges (a towel-and-burner cutout on the range, the
    curtain hanging from the window, the fixed pills art without its own table). (general)
15. **The fixed gate is a different gate.** Propped: blue posts with purple mesh (play/out/room5.png, h10-fix.png);
    latched: blue slatted gate with another latch (h10-acted.png). Fixed: before and after art of the same gate.
    (general)

## Polish accepted
1. **Room swept payoff.** The room view does not glow on its sweep though the spec promises "the room glows warm
   (lamp gold)"; the porch light sits on the lawn; the panel note doubles "✓ Room swept! Room swept!" (src.html:603);
   after all six the panel still says "One room at a time...". Fix: a warm wash in the room on its sweep, the porch
   light at the door, one "Room swept", an end-state panel line. (play/out/kitchen-swept.png, card-close-house.png)
   (general)
2. **Fix targets as places, not navy boxes.** "High medicine cabinet", "Cool towel hook", "Patio", "Pull the plug
   chain up" are dark labelled rectangles; give them a glowing outline on the painted spot; the heater blanket sits on
   the floor, not floating. (play/out/h06-fix.png, h07-fix.png, h10-fix.png) (general)
3. **Check badge on the object**, not at the top right of an empty box. (audit state-reveal-1366x768.png,
   play/out/h01-acted.png) (general)
4. **House view stickers smaller.** Swept rooms show fixed cutouts at full size (play/out/house-3.png); scale them
   with the room. (general)
5. **Grown-up moments in the scene.** Candle hold shows only a faint 〰 and no Grandma (h02-acted.png); Lighter is a
   tap with a hold bar and nothing moves (h11-fix.png). Show the grown-up's chip in the scene doing it. Word the Safety
   card "Twelve fixes, made by you and your grown-ups." (general)
6. **Poison Help on the two poison hazards.** Add the Poison Help line (1-800-222-1222, free, 24/7) under the safe
   outcome of Cleaners and Gummies, as on the Safety card. (general)
7. **Safety card icons per habit.** "Medicine lives up high" shows an empty table, Lighter a table, both online habits
   the same screen (play/out/card-1366.png). Pick art that shows each habit (the high cabinet, the shelf, chat vs
   pop-up). (general)
8. **Ruler hints for pointer users.** After a short drag: "Still too close. Drag it to 3 feet or more."; keep "Arrow
   keys move it 6 inches" and "press Enter" for keyboard focus only. (craft/out3 ruler-2-9.png) (general)
9. **Screen reader states.** `aria-pressed` on peek buttons (src.html:634), `aria-current="step"` on the step strip
   (588-589), neutral look-alike names ("Pot on the stove", "Candle", "Cabinet", "Hook") so the safe one is not named
   by its answer (src.html:819). (general)
10. **375 wide pot drift.** The pot cutout lands on the utensil crock under the room plaque (play/crop-375-pot.png);
    keep cutouts on their spots at narrow sizes. (general)
11. **"Test · hold 2 s" wraps its "s"** at 680x425 (audit state-alarm-hold-680x425.png); keep it on one line. (nit,
    general)
12. **Missed drag keeps the toggle handler** (src.html:1049-1057), so the hint updates to "Now tap <target>." and a
    second tap unselects. (nit, general)
13. **Stray indentation** at src.html:715 and 868. (nit, general)

## Settled calls
- Everyone over-pick (Teaching polish, Play should fix): should fix. The spec says no set counts as wrong, so the
  correction is an outline and a line of why, never a red mark, score or retry.
- Help rule (Teaching and Craft): the spec's general sentence is the rule; the Heater gets its own reason line. Do not
  invent a new rule.
- Option rewrite (item 2) must keep the spec's 4/4/4 safe positions, the 6/6 Think split and the Everyone 6 / Theo 4 /
  You 2 sets.
- No blocker: all three lenses found none, and the spot-checks agree.
- Safety card covering the hint at 680, 760 and 375: not a fault; the card has its own Close and Sweep again and Read
  speaks it. At 1366 and up the hint shows beside it (the audit's "every size" was wrong).
- Welcome heard after roomIn, or lost on a key/Read/Motion first tap: BASELINE rule 16 and the spec's `welcomeAfter`;
  roomIn and the panel carry its content. Do not change.
- Voice counts, stale lines, Read and order: clean in Craft and Play runs. Do not touch `voice/lines.json` beyond what
  item 8's hint words need.
- No points, timers or win states; keep it that way.

## To the spec's open questions
- Teaching 7: tapping any object first asks "Risky or looks fine?" (two buttons, never scored) before the decision or
  Looks fine card, so the student, not the tool, tells hazards from look-alikes (5.5.1). Changes the room flow.
- Play 2 (second half): a few painted ordinary objects that answer a tap with "Looks fine", so tapping everything is
  not free. The spec says empty taps do nothing and fixes three cutouts per room.
- Teaching 9: give the child a real action on Candle and Lighter (step back and keep Theo away, point Dad to it)
  instead of watch-only fixes. Changes two Fix lines.
- Play feel note: twelve identical loops of about ten taps; after items 1, 2 and 7 land, decide whether hazards need
  more varied fix shapes.
- People art review (Theo, Grandma June, Dad): already open in the spec (BASELINE rule 11); not Codex's.

## Not taken
- Rooms button and stage House button side by side at 680 and 375: both are in the spec's layout.
- "Who is safer now? ... then tap Done" while Done is disabled: a sequence that reads fine aloud; item 9 makes the
  state visible.
- Safety card covering the hint at narrow sizes: by design (see Settled calls).
- Theo reason text difference from spec (Craft 12): covered by should fix 6.
