# Safety Sweep House

## One idea
Sweep a lived-in house room by room for hidden hazards, and for each one use the same four decision steps (Stop,
Think, Choose, Check), peeking at "what could happen" for every option before you pick, so the student learns that
a hazard is a decision, not a rule to recite, and watches each dark room light up as its fixes are done.

## Not like
- safety-street (K-2, built): a teacher-led walk with Biscuit, one choice per stop. Here grade 3-5 students search a
  room themselves, tell real hazards from look-alikes, decide whether they need a grown-up first, and do the fix.
- secret-keeper (K): who can see what you share. Here the online room is one room of six, about a stranger and a
  prize trick in a game, with block, report and tell.
- body-systems-tour (3-5, spec): the body's systems. No overlap in content; this is a search-and-decide explorer,
  not a ride.
- recess-upstander (3-5, concept): social choices across a week. Here the hazards are things and messages, not people.
- label-detective (3-5, built): compare labels to solve a case. Here nothing is compared on a chart; you search a
  painted scene.

## Who and how
- Grade 3-5, Health. Module: Safety at Home and Online (health-pe-3-5-safety-at-home-and-online).
- Driver: students (solo by default, BASELINE rule 4); works on a projector with the class voting.
- 20 to 30 minutes for the whole house; one room takes about 3 to 5 minutes. tool.json: driver "students or teacher",
  minutes "20-30", modes [] (pure explore, no score), grades_label "Grades 3-5".
- Standards: NHES.S5 (indicators 5.5.1 to 5.5.5) and NHES.S7 (7.5.1, 7.5.2), NHES 3rd edition (2024).
- Disclosure note (teacher notes and plan.md): fire, poisoning, drowning and online strangers may remind a child of
  something real. Nothing here asks a child to share, but if a child says a stranger online asked for personal
  details, or tells of a fire, poisoning or unsafe home, the teacher follows school procedure (counselor, report as
  required). The tool collects nothing.
- Teacher notes name the sensitive topics the standards touch here (BASELINE rule 8): poisoning, fire, drowning,
  online contact from strangers.

## Standards map
| Code | Student action | What they see | Done when |
|---|---|---|---|
| NHES.S5.5.1 (situations that need a thoughtful decision) | Stop: search the room and tap what looks risky; one look-alike per room is safe | A real hazard opens a decision card; a look-alike opens "Looks fine" with the reason | Tapping each room's look-alike never opens a decision card and says why it is fine |
| NHES.S5.5.2 (is help needed) | Think: tap "Get a grown-up first" or "Act now, then tell a grown-up" | The answer, with the rule: medicine, fire, heat or climbing means a grown-up first | Every hazard asks it before the options show; 6 hazards answer each way |
| NHES.S5.5.3 (compare options and outcomes) | Choose: tap "What could happen?" on any option card before picking | The card flips to its outcome; after the safe pick all three show side by side | All three outcomes are visible together after every safe pick |
| NHES.S5.5.4 (choose a health-promoting option) | Tap an option card | Unsafe: its outcome card shows, choose again. Safe: the fix step opens | No path reaches Check without the safe option |
| NHES.S5.5.5 (reflect on results for self and others) | Check: tap everyone the fix keeps safer (You, Theo, Grandma June, Dad), then Done | The right set lights with one reason line | Sets differ across hazards: Everyone 6, Theo 4, You 2 |
| NHES.S7.5.1 (examine practices) | Read the outcome cards and the safe card's habit line | Each safe card ends with a habit ("Medicine lives up high, out of sight.") | Each of the 12 habits appears on its card and on the Safety card |
| NHES.S7.5.2 (demonstrate practices) | Check: do the fix in the scene (drag, press and hold, tap Block) | The hazard cutout swaps to its fixed art with a green check badge | Each of the 12 fixes is an action the student performs, listed in Content |

## Screens and modes
One screen, no mode buttons. Header (kit): title "Safety Sweep House", small line "Find it. Think. Choose. Check.";
Motion, Sound, Read.

**On load.** The stage shows the house cutaway (art: house-cutaway), six rooms in two floors plus the backyard, each
dimmed by a dark overlay drawn in code, with its name on a code label: Kitchen, Living room, Hallway, Bathroom, Game
room, Backyard. A "Rooms swept 0 of 6" counter sits under the stage. Panel: the hint "Tap a room to start your
safety sweep." and a short four-step strip (Stop, Think, Choose, Check, icons plus words; all grey until a hazard
opens). Nothing plays on load. The first tap on a room goes into it (the welcome queues after that tap's own line,
see Voice; a cut welcome is fine, BASELINE rule 16). The first tap on Read speaks the hint.

**Focus.** House view: the cutaway, centered and as large as the stage allows. Room view: the painted room fills the
stage; it is the biggest thing on screen and the eye searches it. During a decision the stage zooms (about 1.6x,
0.4 s, instant with Motion off) on the hazard, which stays the central picture; outcome cards appear on the stage
beside the hazard, and the panel holds the step's buttons.

**Layout at 1366x768 full screen.** Header 56 px. Stage on the left, about 920 by 518 (16:9), with a room strip below
it (six 120 by 56 tabs with a lamp icon that lights when the room is swept, plus "House"). Panel on the right,
about 410 wide: hint, step strip, then the current step's controls. All of it sits above the fold: stage 518 + strip
64 + gaps fits in 712. The Choose step's three option cards are 96 px tall each, so the panel needs about 520 px.
At 680x425 (preview): stage and panel side by side, stage about 420 wide, panel 250; the room strip folds into one
"Rooms" button that opens the house view; the step strip becomes four dots with the current step's word; option cards
shrink to 64 px with the peek as an icon button (44 px). Under 760 wide, stack the panel over the stage with buttons
first.

**Room view.** The room painting with its hazard and look-alike cutouts placed on it, "Found 0 of 2" on the stage
corner, and a "House" button (house icon). Hazards are in plain sight but small, as in a real room. Tapping anywhere
that is not a hazard or look-alike does nothing (no buzzer). Hover and keyboard focus show a soft ring.

**A hazard, four steps.** The step strip marks the current step.
1. Stop: tapping a hazard zooms the stage on it and shows its situation (two sentences) in the panel. Button "Think"
   (arrow).
2. Think: "Do you need a grown-up first?" Two buttons: "Get a grown-up first" (adult icon) and "Act now, then tell
   a grown-up" (hand plus speech icon). The answer shows with the rule line: "Medicine, fire, heat or climbing:
   get a grown-up first. If you can make it safe without touching those, act now, then tell." A wrong pick shows the
   right one and why; it is not counted. Button "Choose" (arrow).
3. Choose: three option cards in the panel, each with the action in words and a small "What could happen?" button.
   The peek flips that card to its outcome (tap again to flip back). Tapping the card itself chooses it. Unsafe: its
   outcome card (red edge, risk icon drawn in code, the outcome text) appears on the stage beside the hazard, and the
   option card stays flipped and marked "Tried"; choose again. Safe: all three cards flip to their outcomes, the safe
   one with a green edge; the stage outcome card shows the safe result and its habit line. Button "Check" (arrow).
4. Check: the fix prompt names the action and the control (Content lists each). The student does it in the scene;
   when a grown-up is needed, a "Tell Dad" (or "Tell Grandma June") button calls a portrait chip (art) with a speech
   bubble in code, and then the student finishes the step shown. The hazard cutout swaps to its fixed art with a
   green check badge. Then "Who is safer now?": four chips (You, Theo, Grandma June, Dad) and "Everyone"; tap any,
   then "Done". The right set lights with the reason line. Back to the room view, found count up by one.

**Look-alikes.** Tapping one shows a short "Looks fine" card on the stage with why (Content) and a small blue check
on the cutout. It counts nothing.

**Room swept.** When both hazards are done, the room's overlay fades and the room glows warm (lamp gold), its tab
lamp lights, "Rooms swept" goes up, and the hint names the next action: "Tap House, then pick another room."

**What the house shows for every outcome.** 0 rooms: all six dark. Each swept room: lit and warm, its two hazards in
fixed art with check badges, look-alike with its blue check if found. Unfinished rooms stay dark, and a room left
mid-hazard keeps its fixed hazards fixed and its found count. All six: the whole house lit, a porch light on (a
code glow over the cutaway's door), and the Safety card opens on the stage.

**Safety card.** A card over the house: the 12 habits as a list with small icons (two columns of six, no scroll at
1366x768; paged into two pages of six at 680x425 with "Next" and "Back"), then two boxed lines: "Poison Help:
1-800-222-1222 (free, any time, in the US)" and "Fire: get out, stay out, then call 911 from outside." Buttons
"Close" (back to the lit house) and "Sweep again" (resets everything after a confirm: "Start the sweep over?" Yes,
No).

## Content
Household (people art, see Art): You (the student, never shown), Theo (little brother, 2), Grandma June (visiting),
Dad. Habits in quotes appear on the safe card and the Safety card. Options are in display order; S marks the safe
one. Think answers: A = get a grown-up first, N = act now, then tell.

**Kitchen** (look-alike: a pot on the back burner, handle turned toward the back. "Looks fine: the handle points to
the back, so no one can bump it.")
1. Cleaners. Situation: "Your cousin set bleach and a glass cleaner with ammonia next to an empty bucket. 'Let's mix
   them to make super cleaner!'" Think N. Options: (a) "Mix a little to test it": a gas forms that hurts your eyes,
   nose and lungs; people cough and struggle to breathe. (b) S "Say no. Keep them closed and apart, then tell a
   grown-up": no gas forms; the cleaners get used one at a time, as the label says. (c) "Mix them outside where
   there is air": the gas still forms and you still breathe it. Fix: drag the bucket away from the bottles, then tap
   "Tell Dad". Habit: "Never mix cleaners. One at a time." Safer: Everyone.
2. Towel. Situation: "Dad stepped out to answer the door. A dish towel hangs right next to a lit burner." Think A.
   Options: (a) S "Get Dad back to the stove right away": Dad moves the towel and stays with the cooking. (b) "Wait.
   It hasn't caught fire yet": a towel by a flame can catch fire fast, and the fire can spread to the cabinets.
   (c) "Turn the burner up so the food is done sooner": a bigger flame, still next to the towel. Fix: tap "Tell Dad";
   Dad moves the towel; then drag the towel onto its hook across the kitchen (now cool and away). Habit: "Things that
   burn stay away from the stove, and someone stays with the cooking." Safer: Everyone.

**Living room** (look-alike: a battery candle glowing on the shelf. "Looks fine: a battery candle has no flame.")
3. Candle. Situation: "A lit candle sits on the windowsill. The curtain is moving in the breeze, and no one is in the
   room." Think A. Options: (a) "Push the curtain behind the candle": the curtain can blow back into the flame.
   (b) "Leave it. Someone lit it on purpose": a candle left alone near cloth can start a fire. (c) S "Get a grown-up
   to blow it out": the flame is out and no one has to watch it. Fix: tap "Tell Grandma June"; then press and hold the
   candle for 1 s to watch her blow it out (a smoke curl, still frame with Motion off). Habit: "Candles stay a foot
   away from anything that can burn, and go out when you leave the room." Safer: Everyone.
4. Pills. Situation: "Grandma June's pill box is open on the low coffee table. Theo is building blocks right beside
   it." Think A. Options: (a) S "Tell Grandma June now, and keep Theo busy with his blocks": she puts it up high, out
   of sight. (b) "Leave it. Theo can't open pills": this box is open, and even safety caps are not childproof.
   (c) "Hide it under the couch cushion": Theo can still find it; medicine belongs up high and out of sight. Fix: tap
   "Tell Grandma June", then drag the block bin toward Theo so he plays away from the table. Habit: "Medicine lives up
   high, out of sight." Safer: Theo.

**Hallway** (look-alike: the family's fire escape map on the wall. "Looks fine: it shows two ways out of every room
and the meeting spot outside.")
5. Smoke alarm. Situation: "The smoke alarm is on the floor with its battery out. The battery is in a toy car."
   Think A. Options: (a) "Keep the battery in the toy. The alarm only chirps anyway": with no battery the alarm
   cannot warn anyone about smoke. (b) S "Tell a grown-up so they put in a fresh battery and test it": the alarm is
   back on the ceiling and works. (c) "Climb on a chair and stick it back up yourself": you could fall, and no one
   checks that it works. Fix: tap "Tell Dad"; Dad puts it back (fixed art); then press and hold the alarm's Test
   button for 2 s: a short beep plays (Sound on) and the alarm's light flashes. Habit: "A grown-up tests smoke alarms
   every month with the test button." Safer: Everyone.
6. Heater. Situation: "A space heater is running. A blanket is draped over a chair about one foot away." Think N.
   Options: (a) "Drape the blanket over the heater to warm it up": the blanket can catch fire. (b) "Turn the heater
   up": more heat, still close to the blanket. (c) S "Pull the blanket away, at least 3 feet, then tell a grown-up":
   nothing that burns is near the heater. Fix: drag the blanket at least 3 feet away (a code ruler shows feet from
   the heater; the drop counts only at 3 feet or more), then tap "Tell Dad". Habit: "Keep a 3-foot space around
   heaters." Safer: Everyone.

**Bathroom** (look-alike: the medicine cabinet, closed and up high. "Looks fine: up high and closed.")
7. Gummies. Situation: "A bottle of gummy vitamins is open on the counter. They look just like candy." Think A.
   Options: (a) "Eat a couple. They're vitamins": vitamins are medicine; only take them when a grown-up gives them.
   (b) "Leave them. They're only vitamins": too many can make a child very sick, and Theo could find them.
   (c) S "Tell a grown-up so they go up high, out of sight": the bottle is closed and put away. Fix: tap "Tell Dad";
   then drag the closed bottle up to the high cabinet. Habit: "Vitamins are medicine too. Up high, out of sight."
   Safer: Theo.
8. Tub. Situation: "The tub is still full after Theo's bath, and Theo is heading back toward it." Think N. Options:
   (a) "Go get a towel and come right back": a young child can slip under in a few seconds, without a sound.
   (b) S "Stay with Theo, pull the plug, and call a grown-up": the water drains and Theo is never alone near it.
   (c) "Leave it. The water isn't deep": a young child can drown in only a few inches of water. Fix: drag the plug
   chain up (the water level drops in code over 1.5 s), then tap "Tell Dad". Habit: "Empty the tub right after a
   bath, and stay with little kids near water." Safer: Theo.

**Game room** (look-alike: a chat message from Maya, a friend from your class: "gg! that was fun". "Looks fine: you
know Maya in real life, and she isn't asking for anything.")
9. Chat. Situation: a chat message (code, over a blank painted screen) from "CoinKing_77": "what school do you go to?
   I'll send you free coins". Think N. Options: (a) S "Don't answer. Block and report them, then tell a grown-up":
   they can't message you again, and a grown-up knows. (b) "Tell them your school. It's just coins": a stranger now
   knows where to find you every day. (c) "Ask for the coins first, then decide": you keep talking with someone you
   don't know, who wants your details. Fix: tap the chat's "Block" button, then "Report", then "Tell Dad". Habit:
   "Never share your school, address or phone online. Block, report, tell." Safer: You.
10. Pop-up. Situation: a pop-up (code): "YOU WON 10,000 COINS! Type your password to claim." Think N. Options:
   (a) "Type your password. It's a prize": someone else can now get into your account. (b) "Tap the prize to see if
   it's real": tapping can open a trick page that asks for more. (c) S "Close it without typing anything, then tell a
   grown-up": your password stays yours. Fix: tap the pop-up's close button (an X in a 44 px circle), then "Tell Dad".
   Habit: "A message that asks for your password is a trick. Close it and tell." Safer: You.

**Backyard** (look-alike: a life jacket on a hook by the pool. "Looks fine: ready for anyone who needs it.")
11. Gate. Situation: "The pool gate is propped open with a flowerpot. Theo's ball is by the pool." Think N. Options:
   (a) "Leave it open so everyone can get through": Theo can walk straight to the water. (b) S "Move the pot so the
   gate swings shut and latches, then tell a grown-up": the gate is closed and latched. (c) "Run in and get the ball
   by yourself": now you are at the pool with no grown-up watching. Fix: drag the flowerpot off the gate; the gate
   swings shut and a latch click sounds (Sound on); then tap "Tell Dad". Habit: "Pool gates close and latch by
   themselves. Never prop them open." Safer: Theo.
12. Lighter. Situation: "A lighter is on the patio table next to the grill." Think A. Options: (a) S "Don't touch it.
   Tell a grown-up so they put it away": the lighter goes up high, where kids can't reach. (b) "Click it once to see
   if it works": a flame near the table and grill can start a fire. (c) "Put it in your pocket to hand in later": you
   are carrying a fire tool around. Fix: tap "Tell Dad"; Dad's chip appears; tap the lighter to watch it go to the
   high shelf. Habit: "Matches and lighters are grown-up tools. Don't touch, tell." Safer: Everyone.

Reason lines for "Who is safer now?": Everyone: "Fire and fumes spread through a whole house." Theo: "Little kids
can't read labels or swim, so grown-ups and big kids keep things out of reach." You: "Your details and your account
are yours to protect."

## Interactions in detail
- Rooms open in any order. A hazard step can be left with "House" or a room tab: its progress is kept (the step
  resumes where it stopped).
- Controls stay live while anything moves. A tap during the zoom finishes the zoom at once. A tap on an option during
  an outcome card's entrance replaces that card at once. The tub drain, gate swing and candle smoke finish instantly
  when the next step's button is tapped. Motion off: no zoom animation, fades become swaps, same timings for lines.
- Choose: mashing all three cards is allowed; each unsafe pick shows its outcome, so the safe pick still ends the step
  and the student has seen every outcome. The Check button exists only after the safe pick.
- Think: a wrong answer is shown, never scored. Both answers lead to Choose.
- Who is safer: any set may be tapped (none counts as wrong); Done is enabled after at least one chip; the reveal
  marks right chips green with a check and missed ones with an outline and "also safer".
- Drags have tap alternatives (keyboard and touch): select the object (Enter), then tap or Enter on its target spot.
  The 3-foot ruler moves with arrow keys in 6-inch steps.
- Look-alikes: a second tap reopens the same card. Empty taps do nothing.
- Sweep again resets all rooms and steps; how-to lines already heard stay hint only. Nothing is stored; refresh starts over.
- Tab order: header, panel controls, then room hotspots, then the room strip.

## Look
- Accent `--brand` #1d5c8a (porch-light blue), own light `:root`: paper #f6f3ec, ink #1b2430, muted #545e69, line
  #ddd6c8, focus #c2410c (with a white inner ring), panel #fffdf8. Safe green #2e7d32, risk red #a8321e, lamp gold
  #ffc85a for lit rooms, night #141b2a for the dark overlay base (at 62 percent).
- Neighbors: safety-street amber #d98a1c, label-detective teal #1d5c63, germ-spread-sim teal #1f7a6a, body-systems-tour
  burnt orange, growing-up-q-a mauve, playbook field green, fitness-circuit violet. Porch-light blue is new among them.
- Contrast (computed): ink on paper 14.12:1; muted on paper 5.96:1; brand on paper 6.42:1; white on brand 7.12:1;
  white on safe 5.13:1; white on risk 6.69:1; risk on panel 6.58:1; safe on panel 5.04:1; ink on lamp 10.18:1; lamp
  on night 11.2:1; white on night 17.21:1; focus on paper 4.67:1. Safe and risky cards also differ by icon and the
  words "Safe" and "Tried".
- Painting style for every image, asked for in one session: warm, lived-in picture-book illustration, soft daylight,
  slightly cluttered real home, gentle colors, hazards clearly readable but never frightening.

## Art
Local FLUX for places and objects; people with Gemini (`scripts/art.py`), `people: true`, Cory reviews. Every cutout
is drawn at the room's perspective (three-quarter view from a doorway) on a transparent background. Every cutout shows
whole inside the room painting at every size.
- house-cutaway: "A cozy two-story house shown as a cutaway dollhouse, kitchen, living room, hallway with stairs,
  bathroom, a game room with a desk and computer, and a backyard with a fenced pool, warm picture-book style"; 16:9;
  cutout no; people no; house view (room hotspots and labels in code).
- room-kitchen, room-living, room-hallway, room-bathroom, room-gameroom, room-backyard: each "a [room] seen from the
  doorway, lived-in, warm daylight, open counter or floor space at [the hazard spots]"; 16:9; cutout no; people no;
  room backdrops. The game room's monitor shows a plain blank glowing screen (chat and pop-up drawn in code on it).
- Hazard cutouts, before and after (24): cleaners-bucket / cleaners-apart; towel-burner / towel-hook; candle-sill /
  candle-out; pillbox-table / pillbox-gone (empty table spot with blocks); alarm-floor (alarm, battery in a toy car) /
  alarm-ceiling (on the ceiling, small light); heater-blanket / heater-clear; gummies-open / cabinet-high; tub-full /
  tub-empty; screen-glow (blank screen, both chat states in code) / screen-glow-check; gate-propped (flowerpot) /
  gate-latched; lighter-table / lighter-shelf; plus bucket, towel, blanket, plug chain, flowerpot, gummy bottle as
  separate drag cutouts. Each 1:1 or 4:3 to the object's shape; cutout yes; people no.
- Look-alikes (6): pot-back-burner, battery-candle, escape-map (blank paper with a floor plan drawn as simple shapes,
  words in code), medicine-cabinet-high, maya-message (none: code), life-jacket-hook; 1:1 or 3:4; cutout yes.
- theo-blocks (sitting, building), theo-walk (toddling, side view): 3:4; cutout yes; people yes; Theo at the coffee
  table and in the bathroom and backyard, fully on screen.
- chip-dad, chip-grandma (head and shoulders, friendly, looking at the viewer), chip-you (a neutral kid silhouette
  icon drawn in code instead), chip-theo: 1:1; cutout yes; people yes; portrait chips in Check and grown-up bubbles.
- About 44 images. The people set goes to the fresh representation review (BASELINE rule 11).

## Voice
`friendly-dad` (Achird): "Say in a relaxed, friendly way, like a kind dad helping with homework." Different from
safety-street (Puck), body-systems-tour (upbeat-guide), growing-up-q-a (clear-teacher), playbook (lively-host) and
fitness-circuit (big-sister). `Curio.voice`, scope = room plus hazard step, `welcomeAfter: true` (one mode).
Situations, options and outcomes are read on screen (grade 3-5); Read speaks the hint plus the current card.

| Key | Kind | When | Stale when | Text |
|---|---|---|---|---|
| welcome | how | after the first room tap's line | any hazard opens | "This is a safety sweep. In every room, look for things that could hurt someone. Tap anything that looks risky." |
| house | how | house view on load (hint only until first tap) | a room opens | "Tap a room to start your safety sweep." |
| roomIn | how | first room entered | a hazard opens | "Search the room. Tap anything that looks risky." |
| stop | how | first hazard opens | step changes | "You found one. Read what is going on, then tap Think." |
| think | how | first Think step | answered | "Do you need a grown-up first? Tap one of the two buttons." |
| choose | how | first Choose step | a choice is made | "Tap What could happen to peek at any choice. Then tap the safest one." |
| tried | event, at most once per hazard | unsafe pick | another pick | "That could go wrong. Read what could happen, then choose again." |
| safe | event | safe pick | Check tapped | "That's the safe choice. Now tap Check." |
| fix | how | first Check step | fix done | "Now do the fix. The hint shows what to drag or tap." |
| who | how | first Who is safer | Done tapped | "Who is safer now? Tap everyone it helps, then tap Done." |
| lookalike | how | first look-alike | a hazard opens | "That one looks fine. Keep searching." |
| roomDone | event | room swept (whole) | never cut by a tap on House | "Room swept! Tap House, then pick another room." |
| houseDone | event, whole | all six swept | none | "The whole house is swept and every room is lit. Here is your safety card." |
| poison | how, whole | Safety card opens, after houseDone | card closed | "Poison Help is one eight hundred, two two two, one two two two. For a fire, get out, stay out, and call nine one one from outside." |

The fix prompts per hazard (Content) are hint text only, not spoken; Read speaks them. A waiting line never names a
disabled control (Check and Done exist only when live).

## Family engine
none

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NHES S5, S7 and 3-5 indicators wording | SHAPE America, NHES 3rd ed. page (shapeamerica.org/standards/health/new-he-standards/, fetched 2026-11-05) | data/standards/nhes-2024.txt (same source, 2026-10-27) | yes |
| Poison Help 1-800-222-1222, free, 24/7, US | HRSA Poison Help (poisonhelp.hrsa.gov) | America's Poison Centers (poisoncenters.org); CDC Up and Away | yes |
| Never mix bleach with ammonia: chloramine gas, coughing, trouble breathing | Washington State Dept of Health, "Don't mix bleach with ammonia" | NJ Dept of Health, Hazard Alert: Mixing Cleaners (nj.gov PDF); CDC: never mix bleach with other cleaners | yes |
| Mixing outdoors still makes the gas | NJ DOH Hazard Alert (any mixing or nearby use) | Michigan health guidance via A Healthier Michigan (using them near each other forms the gas) | yes |
| Medicine, vitamins and gummies up and away, out of sight | CDC Up and Away (cdc.gov/medication-safety, upandaway.org) | AAFP, "Up and Away offers tips" (2018) | yes |
| Child-resistant caps are not childproof | Up and Away tip sheet | National Capital Poison Center (poison.org) | yes |
| Too many vitamins can make a child very sick (iron) | FDA iron warning, 21 CFR 101.17(e) | poison.org, iron poisoning | yes |
| Candles 12 inches (a foot) from anything that burns; blow out when leaving | NFPA candle safety | USFA candle safety; Kansas State Fire Marshal | yes |
| Flameless (battery) candles are the safer choice | NFPA candle safety | USFA candle safety | yes |
| Keep things that burn away from the stovetop; stay with stovetop cooking | NFPA cooking safety | USFA cooking fire safety | yes |
| Turn pot handles toward the back | NFPA cooking safety | USFA cooking fire safety | yes |
| Space heaters: 3 feet from anything that can burn | USFA heating pictograph 27 | Ready.gov heating fire safety handout | yes |
| Test smoke alarms monthly with the test button | NFPA smoke alarms | USFA smoke alarms | yes |
| Alarms that fail often have missing or dead batteries | NFPA smoke alarm report (relayed by Alameda County FD notice) | USFA smoke alarms | yes |
| Fire escape plan: two ways out, outside meeting spot | NFPA escape planning | American Red Cross home fire escape plan | yes |
| Get out, stay out, call 911 from outside | NFPA escape planning | American Red Cross | yes |
| Young children can drown in a few inches of water, quickly and silently | AAP HealthyChildren water safety | CDC drowning prevention | yes |
| Empty tubs right after use; stay with young children near water | AAP HealthyChildren | Safe Kids Worldwide bath safety | yes |
| Pool gates self-close and self-latch; never prop open | CPSC Pool Safely (poolsafely.gov) | AAP pool fencing guidance; Snohomish Health District checklist | yes |
| Kids who find matches or lighters don't touch, tell an adult | NFPA children and fire tips (via OKC handout) | USFA; Utah State Fire Marshal | yes |
| Don't share school, address or phone with people you don't know online; tell a trusted adult | FTC consumer advice, Protecting Kids Online | NetSmartz (NCMEC) | yes |
| Block and report in games | NetSmartz | FTC kids and gaming guidance (limit contact with people not known in person) | yes |
| A message asking for your password is a trick (phishing) | FTC, How to recognize and avoid phishing | CISA, Recognize and report phishing | yes |

Cut (could not back twice, or sources disagree): hair dryer by a full sink (only manufacturer manuals found), and how
often to change smoke alarm batteries (yearly, twice a year, or 10-year sealed units: sources differ, so the tool only
says a grown-up puts in a fresh battery and tests it). 23 claims backed twice, 2 cut.

Checks run (S:/CurioClass-codex-scratch/specs/safety-sweep-house/check.py): all contrast ratios above (all pass AA,
focus 4.67:1); safe option position 4/4/4 across 1, 2, 3, so "always tap the first card" is safe first try on 4 of 12;
Think answers 6 A and 6 N, so "always grown-up first" or "always act now" is right on 6 of 12, and four of
the six rooms mix them; Who is safer sets Everyone 6, Theo 4, You 2, so "always Everyone" is right on half and the reveal
corrects the rest; 3 feet = 36 inches (one yardstick); taps for the whole house 72 at best, about 114 with every
wrong pick, fitting 20 to 30 minutes. Wrong behaviors: doing nothing leaves the room dark; mashing options shows
every outcome but only the safe pick opens Check; the common wrong answers (mix outside, climb the chair, share your
school, type the password) all fail.

## Done when
1. Focus: in a room the painting is the largest thing on screen; during a decision the hazard is zoomed and central,
   and its outcome card sits beside it, not over it.
2. At 1366x768 the stage, room strip, hint, step strip and all three option cards are visible without scrolling;
   at 680x425 the Rooms button replaces the strip and the panel still shows the current step's controls.
3. A tap during the zoom, an outcome card's entrance, the tub drain or the gate swing takes effect at once.
4. Each room's look-alike opens "Looks fine" with its reason and never a decision card (5.5.1).
5. Every hazard asks "Do you need a grown-up first?" before its options, and the answers split 6 and 6 (5.5.2).
6. After every safe pick, all three outcomes are visible side by side (5.5.3); no path reaches Check without the safe
   pick (5.5.4).
7. Every hazard ends with "Who is safer now?" and the reveal matches Content (5.5.5).
8. All 12 fixes are done by the student in the scene and swap to fixed art with a check (7.5.2); each habit shows on
   its card and on the Safety card (7.5.1).
9. Each swept room lights warm and its tab lamp lights; all six light the porch and open the Safety card with
   1-800-222-1222 and the 911 line, both spoken once and whole.
10. With a 2 s tap pace across one room, every how line is spoken once and then hint only; "tried" plays at most once
    per hazard.

## Open questions
- People art review: Theo, Grandma June and Dad (Gemini) go to Cory's contact sheet and the fresh representation
  check (BASELINE rule 11). No cultural or hard-history content.
