# Scarf Juggling Ladder

## One idea
Climb a six-rung ladder from one scarf to a three-scarf cascade with real scarves in your hands: watch each rung slowly, practice for one minute, log your best run, and read your own practice chart to find that the dips did not stop the climb, because you kept going.

## Not like
- target-toss (K-2 PE lab): the class compares two ways of throwing at one target and counts hits. Here one student climbs a ladder of a new skill over several days, and the data is their own best runs over time, not a two-way test.
- partner-skill-coach (6-12 PE, concept): spots a missed cue in other players' clips and coaches them. Here the student checks their own tries against cues and nobody else's clip is judged.
- fitness-circuit (3-5 PE race): timed stations, pulse counts and beating round one. Here the one-minute timer is practice time on one skill, there is no race, and nothing is compared to anyone else.
- playbook (3-5 PE builder): team runs and passes on a field. Here it is one person, one skill, steps of difficulty.
- feeling-scarf-dance (K-2 arts, concept): a scarf shows a feeling in a dance. Here the scarf is a juggling prop and the point is a toss-and-catch pattern and practice.
- body-systems-tour, label-detective, germ-spread-sim, growing-up-q-a, recess-upstander, worry-size-sorter, safety-sweep-house (3-5 health): none is a motor skill or a practice log. worry-size-sorter has a one-week coping goal; this goal is a movement goal checked against logged numbers.
- recital-practice-plan (9-12 arts tycoon): budgets practice hours on a plan. Here practice is done, not planned, and the chart is real tries.

## Who and how
- Grade 3-5, Physical Education, module Juggling and Practice Habits. Driver: students (solo default, BASELINE rule 4); also works with a partner counting, or a teacher on a projector leading a class with scarves.
- Minutes: 15-25 per session, over 3 to 10 sessions (a week or two of PE warm-ups). One period alone works: rungs, tries and the sample log.
- Equipment: three light juggling scarves per student. Space: arms out in every direction without touching anyone.
- Standards: SHAPE.S1 (1.5.10 throwing, 1.5.12 catching in practice tasks), SHAPE.S4 (4.5.6 sets observable long-term goals, 4.5.7 identifies movement strengths and opportunities for practice, 4.5.9 recognizes personally effective techniques to manage emotions).
- tool.json modes: ["Ladder", "My log"]. Privacy (BASELINE rule 7): the log is stored in this browser only; the line "Your log stays on this device. It never leaves it." shows under the log in both modes.
- Not personal-disclosure prompts: the reset question is about what helped after a drop, with an "I'd rather not say" option; nothing else asks about feelings.

## Standards map
| Code | Student action | What they see | Done when check |
|---|---|---|---|
| SHAPE.S1 (1.5.10, 1.5.12) | watches each rung slowly (Show me, Step), then tosses and claws real scarves for a one-minute try, self-checking three cues | the juggler and code-drawn scarves doing the rung, the current cue lit; during the try the cue words big enough to read from 2 m | every rung's Show me plays its own pattern with its three cues lit in time, and Step walks it one beat at a time |
| SHAPE.S4 4.5.6 | sets a goal: a rung, a best run and a session number, before seeing results | a dashed goal line on the chart at that number, a flag at that session | the goal card shows "met on session N" or "not yet: best so far X" computed from the log |
| SHAPE.S4 4.5.7 | after tries, picks one cue as a strength and one to practice next, then sees their own cue tally | the tally of Got it / Not yet per cue, revealed only after both picks | both picks are required before the tally shows; the tally matches the saved self-checks |
| SHAPE.S4 4.5.9 | before a try picks a reset for after a drop (Breathe, Shake out, Say "pick it up"); after the try says whether it helped | in My log, each reset with how many tries it helped | the reset card counts "helped" per reset and names the one that helped most, or "try one" when none is logged |
| SHAPE.S4 (practice, reflection) | finds their first and latest session bests on the chart, picks the sentence that matches, then finds a dip | the two numbers filled in only after the taps, a ring on the dip and the session after it | taps must land on the right dots; the sentence is checked against the rule in Interactions |

## Screens and modes
Header: "Scarf Juggling Ladder", mode buttons **Ladder** and **My log** (keys 1, 2), then Motion, Sound, Read. Stage left, panel right.

### On load and first tap
- Opens in Ladder on rung 1 (or the last rung used, from the log). The juggler stands holding one scarf; nothing moves. The hint: "Tap Show me to watch rung 1 slowly." The welcome line is queued for the first tap (BASELINE rule 16 lets a tap cut it).
- First tap on **Show me** plays rung 1 slowly at once. First tap on a rung plays that rung's intro line and selects it. First tap on **Start a try** starts the countdown. Every one of these starts the main path.

### Ladder (focus: the juggler and the scarves; during a try, the timer and cue words)
- Layout at 1366x768: header 56 px. Stage about 900x700: a painted ladder at the left (6 rungs, each a 88 px tall button with the rung number, a small scarf-count icon and a "ready" mark when earned; rung 6 at the top), the gym scene with the juggler in the center (about 520 px tall, all of the figure and the highest toss in view), and a cue strip of three chips under the juggler. Panel about 440 px: rung name and goal-for-this-rung line, **Show me**, **Step**, speed toggle **Slow / Real** (default Slow), hand toggle **Two in right hand / Two in left hand** (mirrors the juggler and the pattern; default right), the reset row (**Breathe**, **Shake out**, **Say "pick it up"**, each an SVG icon plus a word), **Start a try** (big, accent), a **Partner counts** switch, **Set up** (opens the setup card), and the privacy line. Everything above is above the fold.
- 680x425: ladder becomes a row of six numbered chips over the stage; the panel keeps Show me, Start a try and Partner counts; Step, speed, hand and reset fold into a **More** disclosure.
- **Show me**: the rung's pattern plays two cycles at the chosen speed; each cue chip lights when its moment comes and its line is spoken the first time (how). Controls stay live: tapping a cue chip jumps the pattern to that moment and holds; tapping Show me again restarts; Step pauses and moves one beat. Motion off: scarves jump between key positions (start, peak, catch) on the same timing.
- **Step**: one beat per tap (toss, peak, claw...), the beat named under the juggler ("Toss 1", "Scarf 1 at the top: toss 2").
- **Start a try**: a 3-2-1 count, then a 60 s ring timer fills the stage center (about 360 px) over a dimmed juggler, with the rung's three cues cycling in big type (48 px), one every 5 s. Panel: **Done early**, **Stop** (no log), and **+30 s** (once). A try is the reason for the 60 s auto-play: the student is practicing with scarves, not watching. Lines at 30 s and 10 s left, and at the end.
- **Partner counts** on: during the try the stage shows a huge counter with **Catch +1** (or **Round +1** on round rungs), **Drop** (ends the current run: the run is kept, the counter goes to 0, the drop count goes up) and **Undo**. The best run is filled in for the log card.
- **Log card** (after the try, on the stage): "Best run this try" with the rung's unit, a big number with **-** and **+** (0 to 99, also typeable), three cue rows **Got it / Not yet** (optional), and, if a reset was picked, "Did your reset help you start again?" **Yes / A little / No / I'd rather not say**. **Save try** saves and shows the tip for the first "Not yet" cue, then **Start another try** and **See my log**. Tries shorter than 10 s are not logged ("Too short to log. Start a try when you're ready.").
- After saving, if the best run reached the rung's suggested goal for the second time, the rung gets a ready mark and the line "Rung 3 looks ready. Try rung 4 when you want to." Every rung is always open.

### My log (focus: the chart)
- Layout at 1366x768: the chart fills the stage (about 900x640): x is tries in order, grouped into session bands labeled "Session 1, 2, ...", y is best run 0 up to the largest logged value rounded up to 5 (at least 10); one rung's tries at a time (rung picker above the chart: only rungs with data). All dots are the same size, so finding a session's best means reading the heights. Goal: dashed line plus a flag at the goal session. Panel: **Goal** card, **Read my chart** steps, **Strength and next** card, **Reset** card, **Did you know?** card, **Start a new session**, **Show a sample log**, **Clear my log** (asks first), privacy line. The step the student is on sits at the top of the panel; finished steps collapse to one line.
- 680x425: the chart stays; the panel shows only the current step and folds the others into a list of buttons.
- Empty log: the chart area shows "No tries yet. Start in Ladder, or tap Show a sample log." and the sample button is outlined.
- **Show a sample log** swaps the chart to Ren's made-up log (banner "Ren is made up, to show what a practice log can look like"), where every step can be practiced; **Back to my log** returns.
- **Start a new session** is enabled once the current session has 2 or more tries; a new calendar day also starts a new session by itself.

## Content
### Rungs
| # | Name | Scarves | What happens | Unit | Suggested goal | Cues (chip, then the tip shown for "Not yet") |
|---|---|---|---|---|---|---|
| 1 | Toss and claw | 1 | toss up with one hand, claw it with the same hand; switch hands | catches in a row | 10 | Pinch, palm down / Pinch the scarf in its middle, palm facing the floor. ; Lift high, let go / Reach up as high as you can, then let go. ; Claw from above / Reach over the top and grab down, like snatching it from the air. |
| 2 | Cross over | 1 | toss across your body, claw with the other hand, toss it back | catches in a row | 10 | Toss across / Let go on the other side of your body. ; Let go up high / Let go above your head so it floats longer. ; Claw with the other hand / The other hand reaches over the top and grabs down. |
| 3 | Two scarves, X | 2 | throw, throw, catch, catch: one from each hand, crossing | rounds in a row | 5 | Make an X / The two scarves cross in front of you. ; Toss 2 at the top / Wait until scarf 1 is at its highest, then toss scarf 2. ; First up, first caught / Claw scarf 1 first, then scarf 2. |
| 4 | Three tosses | 3 | two in one hand; toss all three in order, let them fall | good rounds in a row (all three crossed, in order) | 5 | Two in one hand / Ring and little finger hold one, the fingertips pinch the other. ; That hand starts / The first toss comes from the hand holding two. ; Every toss crosses / Each scarf lands on the other side from where it started. |
| 5 | One round | 3 | toss 1, toss 2, claw 1, toss 3, claw 2, claw 3 | rounds in a row | 3 | Toss at the top / Each new toss goes when the last scarf is at its highest. ; Claw, then toss / The hand that just threw is free to claw. ; Three up, three caught / Count the catches: one, two, three. |
| 6 | Cascade | 3 | keep the round going: toss, claw, toss, claw | catches in a row | 10 | Keep the X / Every toss still crosses. ; Toss at the top, every time / Watch the top of the scarf in the air, not your hands. ; Throw first / A good toss matters more than a catch. Keep tossing. |
Rung intro lines (spoken when a rung is first selected): see Voice.

### Resets after a drop
Breathe ("Take one slow breath."), Shake out ("Shake out your hands."), Say "pick it up" ("Say: pick it up and go."). No claim is made that one works best; the student finds out which helps them.

### Setup card
"Get three juggling scarves. Find a space where your arms can swing out in every direction without touching anyone or anything. Start on rung 1, even if it looks easy." Picture: the setup art (Art).

### Read my chart steps (one rung, needs 2 sessions on it; otherwise "Practice this rung in 2 sessions to read your chart." and the sample log button)
1. "Tap your best try in session 1." (the highest dot in the session 1 band; a tie accepts either)
2. "Tap your best try in your latest session." Then the numbers fill in: "Session 1: 2. Latest: 7."
3. "Which sentence matches?" Three cards, shuffled: "My best run went up." / "My best run stayed about the same." / "My best run went down." Up means latest at least 2 more than session 1; down means at least 2 fewer; otherwise about the same (within 1).
4. "Tap a dip: a session whose best is lower than the session before." If there is none: "No dips yet. When one comes, look at what happens next." After a right tap, the session after the dip is ringed and the card says what came next (Interactions).
5. Prediction from the Goal card shown beside the result: "You predicted: yes. Your chart: went up."

### Goal card
"My goal: on rung [1-6], a best run of [1-99] by session [2-10]." Plus "Do you think practicing a little every session will grow your best run, even with drops?" **Yes / No / Not sure**. Set before results; editable, but an edited goal shows "changed on session N".

### Strength and next card
"Pick the cue you're best at." then "Pick the cue to practice next." (the current rung's three cue chips), then the tally appears: each cue with Got it and Not yet counts from saved tries. Needs at least 3 tries with self-checks on the rung.

### Did you know? (My log)
"Scientists taught a group of adults to juggle for three months. Brain scans showed changes in areas that track moving things. After they stopped practicing, the changes got smaller." And: "Short practices spread over many days help a movement skill more than one long practice."

### Ren's sample log (made up), rung 3
Session bests from tries: S1 [1, 0, 2], S2 [2, 3, 1], S3 [1, 1, 2], S4 [4, 3, 5], S5 [6, 4, 7]. Bests 2, 3, 2, 5, 7: went up (2 to 7), one dip at session 3, session 4 higher. Ren's goal: rung 3, 5 rounds by session 5 (met on session 4). Ren's cue checks: Make an X got it 13 of 15, Toss 2 at the top 6 of 15, First up first caught 10 of 15. Resets: Breathe helped 5, Shake out helped 2.

## Interactions in detail
- One log per device (localStorage, try/catch; if storage fails the tool still runs and says "This browser can't save. Your tries last until you close the page."). Each try: rung, session, best run, drops (partner only), cue checks, reset and its answer, date.
- Session: a new calendar date or Start a new session. Sessions number from 1 per log, not per rung; the chart shows only sessions with tries on the chosen rung.
- Rung switch during Show me: the pattern stops and the new rung is shown still. During a try the ladder is disabled (the hint says "Finish or stop this try first.") and only Done early, Stop, +30 s and partner buttons are live.
- Ready mark: best run at or above the suggested goal on two saved tries of that rung. It is a suggestion; nothing is locked.
- Read my chart: a wrong dot tap in steps 1 or 2 rings the right dot and says "That one is in session 3. Session 1's best is the highest dot in the first band." and moves on; the sentence (step 3) gets one try, then the right card is outlined with the two numbers and the difference ("up by 5"). Step 4: a tap on a dot that is not a dip says "That session was higher than the one before. A dip is lower." and outlines the dip; on a right tap the next session's best is ringed: if higher, "You kept going, and the next session climbed back to 5."; if not higher yet or no next session, "A dip is part of practice. Keep going and see what comes next."
- New tries after reading the chart reset the Read my chart steps (the numbers changed).
- Clear my log asks "Clear every try on this device? This can't be undone." **Clear** / **Keep it**.
- Motion, Sound and Read are the kit's. Hand toggle mirrors the juggler image, the scarf paths and the words "right/left" in Step labels.
- Extremes: 0 is a valid best run (drawn on the axis line); 99 is the cap; one try in a session is fine; 10 sessions or more scroll the chart sideways inside the stage with the latest session in view.
- Test hook: `window.__tool` exposes state, the voice log and `addSession()` so Refine can test multi-session reading without waiting a day.

## Look
Accent `--brand` #4338ca (juggling indigo), on its own light `:root`: paper #f5f6fd, ink #1c1f33, muted #545a75, line #dcdff3, focus #c2410c, panel #ffffff. Different from neighbors: label-detective #1d5c63, germ-spread-sim #1f7a6a, fitness-circuit #6f2dbd, playbook #1e7a3c, body-systems-tour #c2410c (only as focus ring here), growing-up-q-a #8e4a7a, target-toss #6b3fa0, worry-size-sorter #9a4a1c, safety-sweep-house #1d5c8a. Contrast: ink on paper 15.1, muted on paper 6.3, brand on paper 7.3, white on brand 7.9, focus on paper 4.8, muted on white 6.8. Scarves: orange #ea580c with stripes, blue #2563eb with dots, magenta #db2777 with a plain border band, each with a 2 px ink outline (3.3, 4.8 and 4.3 against paper), so they never rely on color alone. Cue chips: lit chip is brand fill with white text; unlit is white with ink text.

## Art
- juggler-body: a painted 10-year-old in a plain gym t-shirt and shorts, standing facing front, feet apart, arms omitted at the shoulders, warm friendly face, soft gouache style, transparent background; 3:4; cutout; people: true (Gemini, Cory reviews); center of the stage in Ladder, dimmed behind the timer.
- juggler-arm-right-low, -right-high, -right-claw and the same three for the left: a painted child's arm in the same t-shirt sleeve, shoulder joint at the top edge; low (hand at waist, palm down pinching), high (reaching up and across, fingers opening), claw (hand above shoulder, fingers curled down); 3:4 each; cutouts that pivot at the shoulder; people: true. Six poses, so each beat of every rung has a matching pose; all of the figure shows in every pose.
- gym-wall: a bright school gym wall and wooden floor, morning light, a blank painted banner area; 16:9; not a cutout; Ladder stage background.
- setup-scarves: three light juggling scarves (orange, blue, magenta) folded on a gym floor beside open space; 4:3; not a cutout; on the setup card.
- Drawn in code: the scarves (they must flutter and travel along toss arcs), the ladder rungs as buttons, cue chips, timer ring, counter, chart, reset icons.

## Voice
`easy-coach`: "Say in an easy-going, encouraging way, like a relaxed sports coach." Different from fitness-circuit (big-sister), playbook (lively-host), body-systems-tour (upbeat-guide), growing-up-q-a (clear-teacher), worry-size-sorter and safety-sweep-house (friendly-dad), target-toss (bright-teacher), animal-moves (hero-coach). `Curio.voice`, scope = mode, `welcomeAfter: true`. Spoken because during a try the student is moving and can't read.

| Key | Kind | When it plays | Line | Stale when |
|---|---|---|---|---|
| wLadder | how | Ladder welcome | Six rungs, one scarf to three. Tap Show me to watch rung 1 slowly. | a try is running |
| wLog | how | My log welcome | This is your practice chart. Pick a step on the right to read it. | never |
| r1..r6 | how | first select of each rung | (1) Rung 1: one scarf. Toss it up and claw it with the same hand. (2) Rung 2: toss across your body and claw it with the other hand. (3) Rung 3: two scarves. Throw, throw, catch, catch. (4) Rung 4: three scarves. Just toss them in order and let them fall. (5) Rung 5: one full round with three. Three tosses, three catches. (6) Rung 6: the cascade. Keep the round going. | another rung selected |
| cue | how | first time each chip lights in Show me or Step | the chip's cue, e.g. "Claw from above." | the pattern stopped |
| afterShow | how | after the first Show me ends | Grab your scarves. Tap Start a try when you're ready. | a try started |
| go | event, whole | each try, after 3-2-1 | One minute. Go! | never (whole) |
| half | event | 30 s left | Halfway. Keep going. | try ended |
| ten | event | 10 s left | Ten seconds. | try ended |
| time | event, whole | timer ends | Time. Set your scarves down and log your best run. | never (whole) |
| early | event | Done early | Nice. Log your best run. | log saved |
| logHow | how | first log card | Tap plus or minus to set your best run. Then check your cues and tap Save try. | log saved |
| tip | event | after Save, if a cue is Not yet | the tip text for the first Not yet cue | next try started |
| saved | event | after Save, all cues Got it or none checked | Saved. Start another try, or see your log. | next try started |
| ready | event | ready mark earned | Rung N looks ready. Try rung N plus 1 when you want to. (spoken with the number) | another rung selected |
| short | event | try under 10 s | Too short to log. Start a try when you're ready. | a try started |
| dropPartner | how | first Drop tap | Drop. That run is saved. The counter starts again. | try ended |
| chart1, chart2 | how | steps 1, 2 | Tap your best try in session 1. / Now tap your best try in your latest session. | step changed |
| chart3 | how | step 3 | Which sentence matches your chart? Tap one. | step changed |
| right / wrong | event, whole | step 3 result | Yes. Session 1 was 2, and your latest was 7. / Look again. Session 1 was 2, your latest was 7. That's up by 5. (numbers from the log) | never (whole) |
| dip | how | step 4 | Tap a dip: a session lower than the one before. | step changed |
| climb / keep | event, whole | step 4 result | You kept going, and the next session climbed back to 5. / A dip is part of practice. Keep going and see what comes next. | never (whole) |
| noData | how | My log, empty | No tries yet. Start in Ladder, or tap Show a sample log. | a try is saved |
Repeats: how lines once per load, then hint only; half, ten, go, time every try; tip at most once per cue per load, then on screen only.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Best run (self-logged) | type 99 without juggling; doing nothing; mashing + | Not a check: no score, badge, unlock or comparison with anyone; a fake number only fools the student's own chart. Partner counts gives a measured count. Doing nothing logs a real 0, which is valid data. Mashing + stops at 99. |
| Ready mark | enter the goal number twice | Only a suggestion; every rung is open from the start, so there is nothing to win by faking it. |
| Cue self-check | tick Got it on all | Not scored; it only hides the tip. The strength tally then shows no "practice next" cue, which the student sees as their own choice. |
| Read my chart, steps 1-2 (find the dots) | guess a dot; tap the biggest dot; tap the first or last dot | Every dot is the same size and no best is marked, so the student must compare heights in the band (the reading skill); a random tap among about 15 dots on a 5-session log hits 1 in 15; the last dot is often not the latest best (Ren: last try 7 is best, but S2's last try 1 is not). Wrong taps are named and ringed, nothing scores. Numbers appear only after the taps, so they are not on screen before. |
| Read my chart, step 3 (sentence) | guess (1 in 3); always pick "went up"; position | Cards shuffle each time; "went up" fails on a flat or down log (a simulated flat learner was "about the same" 65 percent of runs); the numbers it checks against were found by the student in steps 1-2; one try, then the reason. |
| Read my chart, step 4 (dip) | tap any dot; tap the lowest dot | A dip is defined against the session before, so the lowest dot can be wrong (a low session 1 is never a dip); wrong taps get the definition and the real dip. |
| Goal met | set a goal already reached | The goal is set before results only once; an edit after logging is shown as "changed on session N". The goal is the student's own and not scored. |
| Strength and next | pick at random | Not scored; the tally appears after both picks so the student compares their pick with their own data. |
| Reset helped | always Yes | Not scored; it only counts for the student's own reset card. |

## Heard in order
Grade 3-5, but the try lines must be heard because the student is moving.
- Show me: rN (first select only), then each cue as its chip lights (first time each), then afterShow. A tap on a chip or Show me drops queued cue lines that have not started.
- Try: go (whole; the timer starts as it begins), half at 30 s, ten at 10 s, time (whole) at 0 s; the log card's logHow waits for time to finish. Done early or Stop drops half and ten. Partner Drop plays dropPartner once, over the count beeps (no other lines queue in a try).
- Save: tip or saved, then ready if earned; the next try's go never starts before ready ends.
- Read my chart: chart1, tap, chart2, tap, chart3, pick, right or wrong (whole), then dip; climb or keep (whole) before the prediction line shows. Feedback always plays before the next step's line.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Scarves float down slowly, giving learners time to see the pattern | Gopher Sport, "Tips for Teaching Juggling in PE" (blog.gophersport.com) | juggling-for-beginners.com, "How to juggle scarves" (light, so you drop more than throw; helps learn the cascade) | yes |
| Hold the scarf in the middle, palm down | Alberta Education PE toolbox A(K-3)13 "Juggling with Scarves" | Bethel University, Juggling Progression (scarves: overhand grip, palms down) | yes |
| Lift the arm high and let go up high (above head) | Alberta A(K-3)13 ("as high as you can reach") | Bethel progression ("toss 1 foot above head") | yes |
| Catch palm down, grabbing from above (claw) | Alberta A(K-3)13 (catch palm down) | Bethel progression (overhand, palms down) | yes; catch height differs (waist vs shoulders), so the tool names no height and teacher notes say both |
| Toss across the body; two scarves cross in an X | Alberta A(K-3)13 (release on the opposite side) | Maine State Library scarf kit sheet (throw in an X) | yes |
| Toss the next one when the last is at its peak | Gopher Sport My PE Pack lesson (toss the second as the first reaches its zenith) | Bethel progression (2nd ball at peak) | yes |
| Two scarves: throw, throw, catch the first, catch the second | Maine scarf sheet | Alberta A(K-3)13 two-scarf throws | yes |
| Three: two in one hand, that hand tosses first; hands alternate | Alberta A(K-3)13 (steps A-D) | Bethel progression (begin with 2 in one hand, toss from it, alternate) | yes |
| Learn with fewer objects first (one, then two, then three) | Bethel ("master with 1 less ball") | Gopher Sport My PE Pack (master toss and claw with one scarf first) | yes |
| A good throw matters more than a catch | Circomedia, "Juggling 3 scarves" | Bethel (keep tossing even if not caught, once the cascade is learned) | yes |
| Practice spread over days helps motor learning more than massed practice | Shea, Lai, Black, Park 2000, Human Movement Science 19:737-760 | Lee and Genovese 1988, Research Quarterly 59(4):277-287 (meta-analysis) | yes |
| Adults who learned to juggle for three months showed brain changes in motion areas; they shrank after practice stopped | Draganski et al. 2004, Nature 427:311-312 | E. Chudler, "Juggling Juggles the Brain", University of Washington | yes |
| SHAPE 2024 S1 and S4 wording; indicators 1.5.10, 1.5.12, 4.5.6, 4.5.7, 4.5.9 | SHAPE America National PE Standards 2024 (OAHPERD-hosted PDF, read in full) | Human Kinetics excerpt on the 2024 standards (Standard 4 wording) and data/standards/shape-pe-2024.txt codes | yes |
Backed twice: 13. Cut: paper napkins or plastic bags as scarf substitutes (one source, and bags are unsafe for children); "everyone drops while learning" as a fact (one source; the tool says it only as coaching, "A dip is part of practice"); a catch height (sources disagree). Rung goals (10, 10, 5, 5, 3, 10) and the 60 s try are tool choices, labeled "suggested".
Number checks (Python 3, 2026-11-06): contrast ratios above; Ren's bests 2, 3, 2, 5, 7 give "went up", one dip at S3, goal met at S4 and not by S3; edge cases: [0, 0] same, [0, 2] up, [99, 99] same, [2, 3] same (within 1), [8, 5] down, [0, 99] up, noisy flat [5, 6, 5] same with a dip at S3; 10,000 simulated 5-session learners (3 tries a session, noise sd 1.5): growing 0.8 a session gave up 85 percent, same 15, down 0.2; flat skill gave same 65, up 18, down 18, so "always pick up" fails a flat chart and the teacher note says one chart is noisy evidence.

## Done when
1. On load the hint names Show me, and Show me plays rung 1 slowly with each cue chip lit in time; every rung's pattern matches its row in Content (rung 5: toss, toss, claw, toss, claw, claw).
2. Focus: in Ladder the juggler and the full height of every toss show at 1366x768 with the ladder, Show me and Start a try above the fold; in My log the chart is the largest thing; at 680x425 Show me and Start a try stay visible.
3. A tap while Show me plays (a chip, Show me, Step, another rung) changes the picture at once; during a try Done early and partner Catch +1 respond at once.
4. A try plays go, half, ten, time in order, the log card waits for time, and a try under 10 s is not logged.
5. Partner counts: Catch +1, Drop and Undo give a best run equal to the longest run between drops.
6. Saving a try with a Not yet cue shows and speaks that cue's tip once; reaching the suggested goal twice adds the ready mark, and every rung stays open.
7. Read my chart (Ren's sample): steps 1-2 accept only the session 1 and session 5 best dots, the numbers show only after both taps, step 3 accepts only "went up", step 4 accepts only session 3.
8. The goal card reports met or not yet from the log and marks a goal edited after logging.
9. Strength and next hides the tally until both picks; the tally matches the saved checks. The reset card counts "helped" per reset.
10. The privacy line shows in both modes; with storage blocked the tool still runs and says it can't save.
11. Hand toggle mirrors the juggler, paths and Step words; Motion off keeps timing with jump-cut scarves.

## Open questions
- People art: the juggler body and six arm poses are people images (Gemini, Cory's contact sheet, fresh-agent representation check).
