# Play lens: safety-sweep-house (round 1)

Played twice: as a grade 4 student alone at home (every room, every hazard, wrong picks, look-alikes, the end card,
Sweep again) and as a teacher projecting at 1366x768. Frames in `S:/CurioClass-codex-scratch/safety-sweep-house/play/out/`
(room0-5, look0-5, hNN-stop/tried/fix/acted/reveal/back for all 12 hazards, kitchen-swept, house-3, card-*, confirm,
ruler-2ft, the 680x425 fix and safe frames, everyone-theo), plus the shared audit frames. Voice runs with held clicks
(voice-slow, 3 s gap; voice-fast, 0.3 s gap) in `play/run2.txt`. No console errors in any shot.

## Should fix

1. **Choose is solved by one rule: pick the option that mentions a grown-up.** (content.json options; Choose step)
   In 12 of 12 hazards the safe card is the only one that brings in a grown-up ("then tell a grown-up", "Get Dad back",
   "Get a grown-up to blow it out"; the chat's "Tell them your school" is not a grown-up). It is also the longest
   option in 10 of 12. By the second room a student taps the grown-up card without reading, and the outcome peeks
   (5.5.3) stop mattering. Seen by: script over content.json, then played h00 to h11. Better: give at least one wrong
   option per hazard a plausible grown-up flavour that is still wrong ("Tell Dad later, after your game"), and one or
   two safe options without one (the pot handle, closing the pop-up), with lengths mixed. general
2. **The search is three obvious stickers.** (src.html:775-841, renderRoomObjects; Stop step, 5.5.1) Only the three
   cutouts are tappable and they are the largest, most saturated things in each room: the smoke alarm is as big as
   the bench (room2.png), the gummy jar fills the counter (room3.png), and the Game room shows its three items as white
   text plaques floating mid-air (room4.png), so there is nothing to search. The spec asks for hazards "in plain sight
   but small, as in a real room". Better: size cutouts to the room's scale, sit the chat and pop-up on the monitor,
   and let a few painted ordinary objects answer a tap with "Looks fine" so tapping everything is not free. general
3. **Fix hint still says "Tap Tell Dad" after Dad is here.** (src.html:549-552, hintFor) On all six grown-up hazards,
   after Tell the hint stays "Tap Tell Grandma June, then hold the candle..." / "Tap Tell Dad. When the towel is
   cool..." while the panel shows "Dad is here." and no Tell button (h01-fix.png, h02-fix.png, h06-fix.png,
   audit state-alarm-hold-680x425.png). Words do not match the state; a solo student looks for a button that is gone.
   general
4. **"Everyone" always earns a green check.** (src.html:667-672) On a Theo or You hazard, picking Everyone marks the
   right chip "✓ Safer" and leaves Everyone highlighted with no correction (everyone-theo.png). The spec's own check
   says "always Everyone ... the reveal corrects the rest"; it does not, so the cheap answer for 5.5.5 passes all 12.
   Better: mark an over-wide pick ("Not everyone this time: Theo is the one at risk") with an outline, never a score.
   general
5. **The option words vanish once a card flips.** (src.html:629-633) A tried card and, after the safe pick, all three
   cards show only the outcome; the stage cards show only outcomes too (state-safe-1366x768.png, h05-tried.png). The
   "compare side by side" moment shows three results with no record of which action led to which. Better: keep the
   option as a small line above its outcome on every flipped card. general
6. **Disabled buttons look live.** (src.html:41-45, no `button.b:disabled` style; kit styles only `.big-btn`) Done before
   any chip is picked and Report before Block look exactly like enabled buttons (h04-acted.png, audit
   state-chat-controls-1366x768.png). A student taps Report first and nothing happens, with no hint change. general
7. **Heater ruler at 680x425: clipped and misread.** (src.html:144-150, 886-887) The ruler's lower part is cut off by
   the stage edge and the evenly spaced labels drift off the ticks: "0 ft" sits on the half-foot tick and "4 ft" near
   3.5 (h05-fix-680.png, play/crop-680-ruler.png). This is the one measuring task in the tool (3-foot rule). At 1366
   the labels are a few px off but readable (ruler-2ft.png). Better: place each label at its tick, and keep the ruler
   inside the stage at the preview size. general
8. **Two tubs while it drains.** (src.html:870, 879) During the 1.5 s drain the full tub overlay and the empty tub
   art are drawn at different sizes and positions, so two ghosted tubs overlap (h07-acted.png). general
9. **Composite art reads broken in three rooms.** Kitchen: the towel hazard is a small tabletop stove standing on the
   floor in front of the painted range, and the pot look-alike is stacked on a painted pot (play/crop-1366-pot.png).
   Living room: the curtain cutout has a hard flat top and hangs beside the window, not from it
   (play/crop-1366-candle.png). Pills fixed: a second, lighter table is pasted over the painted coffee table, edges
   visible (h03-back.png). POLISH: never a hard edge, keep the action area clear. general
10. **The fixed gate is a different gate.** Propped: blue posts with purple mesh panels (room5.png, h10-fix.png);
    latched: blue slatted gate with a different latch (h10-acted.png). Anything shown twice must match. general

## Polish

- **The payoff is flat.** Room swept changes nothing in the room view (no warm glow, kitchen-swept.png) though the
  spec promises one; the house view lights rooms, but the porch glow sits on the lawn, not the porch (card-close-house.png),
  and the panel still says "One room at a time. Look closely..." after all six. Better: a warm wash and lamp in the
  room on its sweep, the porch light at the door, an end-state panel line. general
- **Fix targets are labelled navy boxes, not places.** "High medicine cabinet", "Cool towel hook", "Patio, clear of the
  gate", "Pull the plug chain up" are dark rectangles over tiles or air (h06-fix.png, h07-fix.png, h10-fix.png); the
  gummy fix drags a pill bottle, not the gummy jar; the heater blanket floats in front of the stairs. Better: a
  glowing outline on the painted hook, cabinet or patio spot. general
- **Floating check badge.** On Safe, Who and Reveal the green ✓ hangs at the top right of an empty box, far from the
  object (state-reveal-1366x768.png, h01-acted.png). Put it on the object. general
- **"✓ Room swept! Room swept! Tap House..."** doubled in the panel note (src.html:603, kitchen-swept.png). general
- **Theo reason line talks about medicine on the tub and the gate** ("Keep medicine out of little kids' reach...",
  src.html:696, h07-reveal.png); the spec's line ("can't read labels or swim") fits all four. general
- **House view stickers too big.** Swept rooms show the fixed cutouts at full size: the smoke alarm and heater fill the
  hallway, the bottles tower over the kitchen (house-3.png). Smaller, or a lamp only. general
- **Grown-up moments are off stage.** Holding the candle shows a faint 〰 glyph and no Grandma (h02-acted.png); the
  lighter is a tap on a box with a hold-style progress bar (h11-fix.png) and nothing moves. A chip of the grown-up
  doing it, in the scene, would land the "tell" lesson. general
- **Feel after room 3.** Twelve identical loops of about 10 taps, each ending in the same five chips; with item 1 the
  middle steps go automatic. Fixing 1, 2 and 4 is most of the cure; varying the Who reason line per hazard helps.
  general
- **375 wide:** cover-cropped backdrop with percent-placed cutouts drifts the pot onto the utensil crock, under the
  "Kitchen, Found 0 of 2" plaque (play/crop-375-pot.png). general
- **Safety card icons:** "Medicine lives up high" shows an empty table, and the chat and pop-up habits share the same
  desk picture (card-1366.png). general
- **Chat and pop-up are not on the monitor** in the fix step (audit state-chat-controls-1366x768.png). general

## Nit

- 680x425: "Test · hold 2 s" wraps its "s" to a new line (audit state-alarm-hold-680x425.png). general
- 680 and 375: the header Rooms button and the stage House button do the same thing side by side. general

## Checked and fine

First screen names the action (size-1366x768.png); every waiting step names its control (Think, Choose, Tried, Look
fine, Keep searching, Who, Back to room). Look-alikes never open a decision card (look0-5.png). Unsafe picks never reach
Check. Safety card shows all 12 habits plus Poison Help and 911, pages at 680x425 (card-680.png, card-680-p2.png);
Sweep again confirms (confirm.png). Voice: how lines once then silent, "tried" once per hazard, safe and roomDone each
time; no stale line in the fast run. Calm mode, resize and console: audit clean rows, cited.

## Audit pilot

- Lead confirmed in part: "Safety card hint out of view" is true at 680x425, 760 and 375 (the card covers the panel)
  but not at 1366 or 1920, where the hint shows beside it. Low impact: the card carries its own Close and Sweep again.
- Lead not reported: welcome heard late after roomIn (BASELINE rule 16; roomIn already names the action).
- Missed by the audit: disabled-looking-live buttons (6), the ruler clipped and mislabelled at 680 (7), the double tub
  mid-animation (8), stale "Tap Tell" hints (3), the Everyone reveal (4), and all art and giveaway items. None are
  mechanical-check shaped except 6 and 7.
