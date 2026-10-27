# First Aid Responder

## One idea
Race your own ghost through six school emergencies by putting each one's steps in the right order (wrong moves bounce back with the reason and cost seconds), then keep a hands-only CPR rhythm on a live rate gauge until you can hold 100 to 120 a minute for two minutes without the metronome.

## Not like
- fitness-program-designer (9-12 PE, builder): an untimed design bench for training plans. First Aid Responder is timed ordering and rhythm, no planning.
- meal-and-move-planner (9-12 health, builder, same group): a week of meals. Nothing to plan here; you act in sequence against a clock.
- health-claim-checker (9-12 health, mystery, same group): weighs claims with no clock. This one is about acting fast and right.
- fitness-circuit (3-5 PE, race): times exercise stations and counts pulses. Here the timer is on decisions, and the rhythm is chest compressions on a key, not exercise.
- mind-map (9-12 health, built): mental health support. No mental health crisis content here; physical first aid only.

## Who and how
- Grade 9-12, Health, module First Aid and CPR (emergency response basics).
- Driver: students on laptops (alone or in pairs: one taps, one coaches). A teacher can project Scenes and let the class call out the next step.
- Minutes: 15-35 (a scene is 1 to 2 minutes; a CPR round is 2 minutes).
- Standards: NHES.S7 (practice health-enhancing behaviors and avoid or reduce health risks).
- Topic line: "emergency steps and hands-only CPR".
- Modes (tool.json): ["Scenes", "CPR rhythm", "Field guide"].
- Framing on every mode, in the panel footer: "Practice and awareness, not certification. Take a hands-on CPR and first aid class (American Heart Association or American Red Cross) to learn it for real. In an emergency, call 911."

## Screens and modes
Header (theme-912): title "First Aid Responder" with small line "Emergency steps and hands-only CPR", mode buttons **Scenes**, **CPR rhythm**, **Field guide** (keys 1 to 3), **Motion**, **Sound**, **Read**.

### Scenes (opens first)
- Scene picker: six cards in a 3 by 2 grid, each with its backdrop thumbnail, name, a one-line situation, and the best time on this device ("Best 0:38" or "Not run yet").
- Scene screen, stage: the backdrop (Art) dimmed behind a briefing card (2 to 3 sentences, Content) at the top. Below it the **step rail**: numbered empty slots, one per correct step; slots that share a rank are drawn joined with "either order". Under the rail the **deck**: the correct steps and two "Don't" cards, shuffled, as tappable cards (drag also works).
- Panel: the race clock (m:ss.s), **Mistakes: 0** (each adds 5 s), the ghost bar (Interactions), **Timer: On / Off** toggle, **↺ Restart scene**, **◀ All scenes**.
- Finish card (replaces the briefing): time with penalties, mistakes, ghost result ("2.4 s faster than your best" or "Best: 0:38"), and **Why this order**: every step with its one-line reason. Buttons **Run it again**, **Next scene ▶**.

### CPR rhythm
- Stage: a training chest drawn in code (a plain torso outline seen from above, no face, with a hand-position target on the center of the chest, lower half of the breastbone) that dips on each compression. Beside it the rate gauge: a semicircle from 60 to 160 per minute with the band 100 to 120 shaded and labeled "Target 100 to 120", a needle and a big number. Below: a 2-minute strip chart of your rate over time with the band, and the compression count.
- Panel: **Metronome: On / Off** (110 a minute), **▶ Start 2-minute round**, **■ Stop**, **Coach voice: On / Off**, the live coaching line ("Push faster", "Good rate", "A little slower", "Keep going: don't stop"), and the round summary when a round ends.
- Input: press **Space** or **Enter**, or tap or click the chest pad (pointerdown counts, so a held click is one compression). Free practice runs whenever no round is going.
- Round summary: average rate, percent of compressions in 100 to 120, longest pause (seconds), total compressions, and the ghost: best in-band percent on this device with its rate trace drawn faintly on the strip chart. **Clear best times** lives here and in Scenes (one confirm clears both).
- Under the gauge, always: "This practices rate only. Real compressions also need depth (at least 2 inches for an adult) and letting the chest come all the way back up. A class uses a manikin for that."

### Field guide
Explore cards (no clock): **Check, Call, Care**, **When to call 911**, **Hands-only CPR**, **AEDs**, **Good to know** (Content). Each card has a "Practice it" link to the matching scene or to CPR rhythm.

## Content

### Scenes (briefing; steps with rank and reason; Don't cards with reason)
Ranks: steps with the same rank may go in either order. Scene, steps: "rank. Step: reason."
1. **Collapse in the gym** (backdrop gym). Briefing: "During a game, an adult in the bleachers slumps over and slides to the floor. They don't move when people call their name." Steps: 1. Make sure the scene is safe: you can't help if you get hurt too. 2. Tap their shoulders and shout "Are you okay?"; look for normal breathing for no more than 10 seconds (gasping is not normal breathing): you need to know if they are responsive and breathing. 3. Call 911 on speaker and send someone for the AED: the sooner help and the AED come, the better the chance. 4. Push hard and fast in the center of the chest, 100 to 120 a minute: compressions keep blood moving to the brain. 5. When the AED arrives, turn it on and follow its voice prompts: the AED tells you exactly what to do. 6. Keep going until help takes over or the person starts to move or breathe normally: stopping stops the blood flow. Don't: "Wait a minute to see if they wake up before calling" (Every minute counts. Call right away.); "Stop every few compressions to check them" (Keep pauses short; let the AED do the checking).
2. **Choking at lunch** (backdrop cafeteria). Briefing: "Your friend suddenly grabs their throat. They can't talk, cough or breathe." Steps: 1. Ask "Are you choking? Can I help?": a person who can cough hard should keep coughing; one who can't needs help now. 2. Have someone call 911: help should be on the way in case this doesn't work. 3. Give 5 back blows between the shoulder blades, then 5 abdominal thrusts just above the belly button: these push the object out. 4. Keep repeating until the object comes out or they can breathe, cough or talk: it may take several rounds. 5. If they stop responding, lower them to the ground and start CPR: CPR can also help push the object out and keeps blood moving. Don't: "Give them water to wash it down" (They can't swallow past a blocked airway.); "Reach blindly into their mouth" (You can push the object deeper.)
3. **Deep cut in the wood shop** (backdrop shop). Briefing: "A classmate cut their forearm on a tool. It's bleeding a lot, and the teacher is across the room." Steps: 1. Make sure the scene is safe: tools off, nothing else can hurt anyone. 2. Put on gloves from the first aid kit: they protect you both. 3. Press firmly on the wound with a clean cloth or gauze, and 3. send someone to call 911: heavy bleeding needs pressure now and help on the way (either order). 4. If blood soaks through, add more cloth on top and keep pressing: lifting the cloth lets bleeding start again. 5. Keep firm pressure until help takes over: steady pressure is what stops bleeding. Don't: "Lift the cloth every few seconds to check" (Each peek lets the bleeding start again.); "Take off the soaked cloth and start over" (Add more on top instead.)
4. **Burn in the teaching kitchen** (backdrop kitchen). Briefing: "A classmate grabs a hot pan handle. Their palm is red and a blister is starting." Steps: 1. Make sure the scene is safe: turn off the burner. 2. Cool the burn under cool running water for at least 10 minutes, and 2. gently take off rings or anything tight near the burn: cooling limits the damage; swelling can trap a ring (either order). 3. Cover it loosely with a clean, dry, nonstick dressing: it protects the burn. 4. Tell the teacher and school nurse; a burn on the hand should be checked by a health care provider: hands, face and large burns need care. Don't: "Put ice on it" (Ice can damage the skin more.); "Pop the blister" (A blister protects the skin underneath.)
5. **Heat at practice** (backdrop field). Briefing: "Hot August practice. A teammate is confused, stumbling, and their skin is very hot." Steps: 1. Notice the danger signs: confusion and very hot skin can mean heat stroke, an emergency: knowing it's an emergency tells you to act fast. 2. Call 911: heat stroke can be deadly without fast care. 3. Move them to a cooler place, in the shade or inside: get them out of the heat. 4. Cool them fast with cool, wet cloths or a cool bath: lowering their temperature is the goal. 5. Stay with them until help arrives: their condition can change quickly. Don't: "Give them a drink while they're confused" (CDC says not to give a drink to someone with heat stroke.); "Let them rest alone in the locker room" (Never leave them alone.)
6. **Seizure in the hallway** (backdrop hallway). Briefing: "A student falls to the floor. Their body is stiff and jerking." Steps: 1. Stay calm and stay with them: they need someone there until it's over. 2. Ease them to the floor and move hard or sharp things away, and 2. start timing the seizure: keep them from getting hurt and know how long it lasts (either order). 3. Put something soft under their head and gently turn them onto one side: this protects the head and helps them breathe. 4. Call 911 if the seizure lasts longer than 5 minutes: a long seizure is an emergency. 5. Stay until they are fully awake, and talk to them calmly: they may be confused afterward. Don't: "Hold them down" (It can hurt them or you.); "Put something in their mouth" (It can hurt their teeth or jaw; people can't swallow their tongue.)

### Scene picker one-liners
Collapse in the gym: "Someone collapses and doesn't respond." Choking at lunch: "A friend can't breathe or talk." Deep cut in the wood shop: "Heavy bleeding from a cut." Burn in the teaching kitchen: "A hot pan burn." Heat at practice: "A teammate overheats." Seizure in the hallway: "A student has a seizure."

### Field guide cards
- Check, Call, Care: Check that the scene is safe, then check the person. Call 911 (or send someone) when it's serious. Care for the person until help takes over.
- When to call 911: someone isn't responding or isn't breathing normally, can't breathe, has heavy bleeding that won't stop, has signs of heat stroke, has a seizure longer than 5 minutes, or you're not sure. Put the phone on speaker so your hands are free.
- Hands-only CPR: for a teen or adult who suddenly collapses: call 911, then push hard and fast in the center of the chest, 100 to 120 a minute, at least 2 inches deep, letting the chest come all the way up. Don't stop until help takes over. (For infants and young children, a class teaches CPR with breaths.)
- AEDs: An AED is a portable device that can check the heart's rhythm and give a shock if needed. Turn it on and follow its voice prompts; it won't shock someone who doesn't need it. Many schools and gyms have one: find yours.
- Good to know: A class with a manikin teaches depth, hand position and how it feels. The American Heart Association and the American Red Cross offer them, and many schools teach hands-only CPR.

## Interactions in detail
- Scene clock starts on the first card tap (reading the briefing is free) and stops when the last correct step lands. Timer Off hides the clock and ghost; mistakes are still shown with reasons; nothing is recorded.
- Tapping a card: if its rank is the lowest unfilled rank, it slides into the next slot. If not, it shakes back with "Not yet: {reason of the step that comes first}" and +5 s. A Don't card turns over to show ✗ and its reason, +5 s, and moves to a small **Never** tray beside the deck. Keyboard: Tab to a card, Enter to place.
- Ghost: the best run's step times are replayed as a hollow marker moving along the rail; the panel shows "Ghost: step 3 at 0:21". A run with any Timer Off time never becomes the best. Best times and step stamps per scene are saved in localStorage `far-best` (try/catch); **Clear best times** empties it.
- CPR rate: from the last 5 intervals (median, so one stray tap doesn't swing the needle). A pause over 2 s shows "Keep going: don't stop" and is counted as a pause; the round's longest pause is reported. In-band means a compression whose interval-based rate is 100 to 120. The needle eases over 150 ms (instant with Motion off).
- Metronome: a short soft click at 110 a minute via Web Audio, scheduled ahead on the audio clock so it never drifts; every 30th click is slightly higher (the count of 30 is only a reference point here; hands-only CPR doesn't stop). Sound Off silences it.
- Coaching lines update every 3 s; Coach voice speaks them at most once every 8 s, never while the student is between 100 and 120.
- Round end at 2:00 or Stop. Stopping early still shows the summary, marked "Partial round", and cannot become the best.
- Sizes: at 1366x768 the rail, the full deck and the clock are visible together; CPR gauge, chest pad and Start button too. Under 900 px tall the briefing collapses to one line with **More**. At 375 wide (host) the deck becomes a two-column list under the rail and the chest pad is at least 160 px.

## Look
- `kit/theme-912.css` with its own accent `--brand` #3ee0b0 (mint, from the green of first aid signs), `--brand-ink` #0b2a20.
- Contrast: accent on panel #141b25 10.3:1, on sec-bg #18202b 9.76:1; brand-ink on accent 9.14:1; theme ink and muted as in the theme file. Don't cards and ✗ use the theme --warn #ffb8a8 (9.9:1 on sec-bg) with the ✗ glyph and words; ✓ uses --ok.
- Rate band on the gauge: accent fill at 35 percent with the words "Target 100 to 120"; out of band is the panel color, the needle is ink.
- The first aid icon is a white plus on a mint rounded square. Never a red cross on white (a protected emblem).
- Group siblings: body-systems-tour orange, growing-up-q-a mauve, meal-and-move-planner sky blue, health-claim-checker yellow. 9-12 neighbors: fitness-program-designer lime #a3e05a, captain-s-choices coral.

## Art
Scene backdrops (Cloudflare FLUX, `scripts/cfart.py`), empty places with no people, blank surfaces with no lettering, softly lit, used dimmed behind the briefing and as picker thumbnails:
- fa-gym: an empty school gymnasium with wooden bleachers and a polished court, afternoon light; 16:9; cutout no; people no.
- fa-cafeteria: an empty school cafeteria with long tables and lunch trays on one table; 16:9; cutout no; people no.
- fa-shop: a tidy school wood shop with workbenches, clamps and wood pieces, power tools switched off; 16:9; cutout no; people no.
- fa-kitchen: a school teaching kitchen with a stove, a pan on a burner and blank cabinets; 16:9; cutout no; people no.
- fa-field: an empty high school practice field on a hot summer afternoon, bright sun, water cooler on a bench; 16:9; cutout no; people no.
- fa-hallway: an empty school hallway with blank lockers and a tiled floor; 16:9; cutout no; people no.
Chest pad, gauge, AED and icons: drawn in code.

## Voice
`firm-captain` (Alnilam): "Say firmly but kindly, like a ship captain giving clear directions." Different from fitness-program-designer (calm-professor) and captain-s-choices (wise-mentor).
| Key | Kind | Line | Stale when |
|---|---|---|---|
| wScenes | how | Pick a scene. Read the briefing, then tap the steps in the order you'd do them. | mode left |
| wCpr | how | Press Space or tap the chest to the beat. Keep the needle in the green band. | mode left |
| wGuide | how | Tap a card to read it, or Practice it to try. | mode left |
| brief.* | event | each scene briefing (6 lines) | scene left or first card tapped |
| best | event | New best time. | next tap |
| done | event | Scene complete. Check why this order works. | scene left |
| coach.* | event | Push faster. / A little slower. / Keep going. Don't stop. | 3 s after queued (maxAge) |
| roundEnd | event | Round over. {percent} percent of your compressions were on target. | Start pressed |
Step reasons and Field guide cards are read on screen; Read speaks the open card, the finish card or the hint.

## Family engine
none

## Sources
- NHES 2024 (SHAPE America), Standard 7: https://www.shapeamerica.org/standards/health/
- Adult CPR: rate 100 to 120 a minute, depth at least 2 inches, full recoil, minimize pauses; call 911 and get the AED; hands-only CPR for teens and adults who suddenly collapse; AED use: American Heart Association, 2025 Guidelines for CPR and Emergency Cardiovascular Care (Adult Basic Life Support) and Hands-Only CPR: https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines and https://cpr.heart.org/en/courses/hands-only-cpr
- Check, Call, Care; breathing check no more than 10 seconds; CPR steps: American Red Cross, "CPR Steps": https://www.redcross.org/take-a-class/cpr/performing-cpr/cpr-steps
- Choking: back blows and abdominal thrusts in cycles of 5 and 5, no blind finger sweeps, CPR if unresponsive: American Red Cross, "Learn First Aid: Choking" (https://www.redcross.org/take-a-class/resources/learn-first-aid) and AHA 2025 Guidelines (foreign-body airway obstruction).
- Bleeding (gloves, firm direct pressure, add more dressing on top), burns (cool running water at least 10 minutes, remove rings, loose clean dressing, no ice, don't break blisters, get care for hand burns): 2024 American Heart Association and American Red Cross Guidelines for First Aid: https://cpr.heart.org/en/resuscitation-science/first-aid-guidelines; American Red Cross, "Learn First Aid" (bleeding, burns).
- Heat stroke signs, call 911, move to a cooler place, cool cloths or bath, no drink: CDC, "Heat-Related Illnesses": https://www.cdc.gov/extreme-heat/warning-signs/index.html
- Seizure first aid (stay, time it, ease to floor, clear the area, soft under head, on one side, nothing in mouth, don't hold down, 911 over 5 minutes, stay until awake): CDC, "First Aid for Seizures": https://www.cdc.gov/epilepsy/first-aid-for-seizures/index.html
- Tool's own choices, labeled where shown: 5 s penalty, 2 s pause threshold, 5-interval median for the rate, 110 a minute metronome (inside the AHA band), 2-minute round.
- The build agent rechecks every step against the current AHA 2025 and Red Cross pages before building (the choking sequence changed in the 2025 AHA guidelines; use their exact wording).

## Done when
1. Every scene loads its briefing, a rail with the right slot count (6, 5, 6, 5, 5, 6 including shared ranks) and a deck of its steps plus two Don't cards.
2. Same-rank steps place in either order; any other out-of-order tap shakes back with the earlier step's reason and adds 5 s; Don't cards go to Never with ✗, reason and 5 s.
3. The clock starts on the first tap; a best run is saved, replays as the ghost next time, and Clear best times removes it; Timer Off runs are never saved.
4. CPR rhythm: tapping steadily at 110 (scripted with jitter) reads 105 to 115 and over 90 percent in band; at 90 it reads "Push faster"; a 3 s gap counts as a pause.
5. The metronome holds 110 a minute over 2 minutes (220 clicks, plus or minus 1) and is silent with Sound Off.
6. Held clicks (press 120 ms, release) count one compression each; Space held down counts once.
7. The certification and 911 footer shows on all three modes; no red cross emblem appears anywhere.
8. At 1366x768 rail, deck and clock fit; at 375 wide the chest pad is at least 160 px and Start is visible.
9. Briefings and results speak each time; welcome lines once per load; coach lines are dropped when stale and never overlap Read.

## Open questions
1. An opioid overdose scene (recognize it, call 911, give naloxone if available, CPR if needed; CDC and AHA 2025 cover it) is common in high school health now. Add it as a seventh scene, or leave it out so parents and districts aren't surprised?
2. Race framing for emergencies: the clock is optional (Timer Off) and accuracy is required to finish. Is a timed race the right tone, or should Timer Off be the default?
