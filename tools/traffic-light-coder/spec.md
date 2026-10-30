# Traffic Light Coder

## One idea
You program a real-feeling street crossing with if-then rule cards that the light checks from the top, twice every
second, and the first rule that fits wins; then you run the day's traffic and a report names every unsafe moment and
the exact rule that caused it, so a missing yellow or a rule in the wrong place shows up as a car or a walker in
trouble.

## Not like
- snowy-mail-route (1, this group, robot family): a straight list of arrows run once. Here nothing runs in order: the
  same rules are checked again and again, and order only matters when two rules fit at once.
- robot-dance (K) and loop-garden (2), robot family: sequences and repeat blocks; no conditions.
- score-keeper (3, built): watching variables change as a game runs line by line. Here the student writes the
  conditions, and the "variables" are sensors and timers on a street.
- code-tracer (4, built): predicting values in a trace table. Here there is no table to fill; the test report is the
  feedback.
- network-help-desk, internet-journey (3-4): networks and privacy, no programming.

## Who and how
- Grade 3, computer science. Module: If This, Then That (Algorithms and Programming).
- Topic line: if-then rules in a program
- Driver: students in pairs on laptops, or the teacher on a projector for the first street. 20 to 30 minutes.
- tool.json: driver "students or teacher", minutes "20-30", modes ["Watch the Street", "Street Jobs"],
  grades_label "Grade 3".
- Standards (CSTA 2026 ids from the module): E3-ALG-PS-01, E3-PRO-PD-04, E3-PRO-TR-08. 2017 crosswalk: 1B-AP-10
  (programs with sequences, events, loops and conditionals), 1B-AP-15 (test and debug a program), 1B-AP-11 (decompose).

## Screens and modes
Header (kit): title "Traffic Light Coder", small line "If this, then that, on Maple Street"; mode buttons "Watch the
Street" (eye icon) and "Street Jobs" (hard hat icon); Motion, Sound, Read.

Stage (top-down, laid out per size): the painted street strip (art: maple-street) runs left to right with one lane each
way and a crosswalk across the middle. Painted cars (art: car kit) drive in both lanes (turned in code for the other
direction); walkers (art: walker kit) wait on the curbs and cross; the ambulance (art: ambulance) has its light bar
flashed in code. Small top-down signal dots beside each stop line and the two curb push buttons (60 px, controls) are
drawn in code. Above the street: a status strip with the car signal (art: signal-head, the lit lamp drawn in code, the
lit one shown big), the walk sign (art: walk-signal, its walking person, flashing hand or steady hand drawn in code),
and a timer "green for 12 s" (time in the current color). Below the street: a rule-fire ribbon showing the last 8
firings as small numbered chips in the color of the light they set.

Panel: `#hint`, then the rule list (robot family column, up to 6 rules), then buttons. Each rule card reads like a
sentence: "If the car light is [GREEN] and [button pressed] and [ ] then [turn YELLOW]". Tapping a chip slot opens a
picker of chips (60 px tall rows, word plus icon). Card buttons when a rule is selected: Move up, Move down, Delete.
"Add rule" (plus icon) adds a blank rule at the bottom. A rule with an empty light or action slot is skipped and shows
a dashed outline.

### Mode 1: Watch the Street (explore, opens first)
Focus: the crossing at the center of the street strip (signals, crosswalk, the walkers at the curbs), with the rule
list beside it; the rule that fires flashes in the list at the same moment the light changes, so the eye moves between
the two and nothing else. The street strip is the widest thing on screen; the status strip and ribbon stay thin.
The default program (Content) runs live at 1x. Traffic comes on its own (a seeded mix: a car every 3 to 7 s each way).
The student presses either push button on the stage (or "Send walker"), and can press "Send ambulance" (siren icon).
Rules can be edited while it runs; each change counts from the next check. "Pause" and "Reset street" (circular
arrow: clears traffic, light back to GREEN, keeps the rules). "Default rules" restores the starting four.
Each time a rule fires it flashes in the list and its number joins the ribbon. Unsafe moments flash a red triangle on
the street and appear in a small "Watch out" list under the ribbon (the same checks as the report).

### Mode 2: Street Jobs (builder levels)
Focus: while editing, the rule list and the goal card; during a test, the street strip; after a test, the report card,
which slides over the street (not over the rules) so the student reads it beside the rules it names.
Five jobs. Each opens with its starting rules, a goal card ("Goal: every walker crosses, and nothing unsafe") and a
"Run test" button (play icon), plus "Start over" (this job's starting rules) and job dots 1 to 5. Run test plays the
job's traffic script at 4x (about 23 s for a 90 s script, never more than 30 s; "Speed" toggles 4x and 1x; "Skip to
report" (fast-forward icon) finishes it at once). Then the report card slides over the street:
- Safe: "0 unsafe moments" or a list, each with its time, what happened and "Rule 2 did it" (tap a line: the street
  replays from 3 s before that moment, paused on it, and that rule glows).
- Walkers: "3 of 3 crossed", longest wait.
- Cars: shortest green, longest red, longest wait at a red with nobody crossing.
- Ambulance (job 5): "Never stopped" or "Had to stop".
The goal's checks show a check or a cross. All goal checks pass: the job dot fills and "Next job" appears. A small
chime only; no stars.

## Content
Chips. Light (one, required): GREEN, YELLOW, RED, ANY. Extras (zero to two, all must hold): "button pressed" (a walker
pressed and has not had a WALK yet), "walk is done" (walk sign shows the steady hand and the crosswalk is empty),
"ambulance coming" (the detector up the street sees one), "been 3 s", "been 10 s", "been 30 s" (the car light has shown
its current color at least that long). Actions (one, required): turn GREEN, turn YELLOW, turn RED, start WALK, keep
lights (do nothing, but it counts as the rule that fired).

The street's own fixed behavior (not programmable):
- Checks every 0.5 s of street time, rules top to bottom, first that fits fires, at most one per check. A press at
  time t is seen at the next check (t + 0.5), and a sign change at time t is seen from the next check too; a window
  such as "ambulance seen 36 to 46" is true at the checks 36.0 to 45.5. A test runs its script, then keeps going until
  every walker who pressed has crossed (at most 120 s of street time); a green still running when the test ends is not
  counted for the 30 s check.
- start WALK shows WALK for 7 s, then the flashing hand for 10 s, then the steady hand (MUTCD: walk interval at least
  7 s; clearance time from crossing length at 3.5 ft per second, here a 35 ft crosswalk = 10 s). Waiting walkers step
  out when WALK starts and take 10 s to cross. Walkers who arrive while WALK shows step out at once; walkers who arrive
  during the flashing hand wait and press. start WALK while WALK or the flashing hand already shows does nothing (the
  rule still counts as fired).
- Cars stop at the stop line on RED; on YELLOW a car more than 2 s from the line stops, a closer one goes through (the
  tool's own simple driver model).
- Unsafe moments (shown on screen with these words): "Yellow too short": the light went from GREEN to RED, or YELLOW
  lasted under 3 s (MUTCD: a yellow lasts at least 3 s). "Walk while cars go": start WALK while the car light is GREEN
  or YELLOW. "Green while crossing": the light turned GREEN while the walk sign showed WALK or the flashing hand, or
  anyone was on the crosswalk.
- Fairness checks (the tool's own limits, labeled so on the goal card): a walker waits 60 s or more; a green under
  30 s (job 4 only); a red lasting 45 s or more ("cars stuck", job 4 only); cars held at a red 10 s or more with
  nobody crossing (report only).

Default program (Watch the Street and the start of job 4):
1. If GREEN and button pressed then turn YELLOW. 2. If YELLOW and been 3 s then turn RED. 3. If RED and button pressed
then start WALK. 4. If RED and walk is done then turn GREEN.

| # | Job (spoken) | Starting rules | Traffic script (street seconds) | Goal checks | One fix |
|---|---|---|---|---|---|
| 1 | Press to Cross | default 2, 3, 4 only | 90 s; cars each way every 6 s; walkers press at 5, 35, 65 | safe; all cross; no 60 s wait | add rule 1 (top or bottom both work) |
| 2 | Don't Skip Yellow | "If GREEN and button pressed then turn RED", default 3, 4 | same as job 1 | safe; all cross | that action to YELLOW, add default rule 2 |
| 3 | Let Them Finish | default 1, 2, 3, then "If RED and been 10 s then turn GREEN" | same as job 1 | safe; all cross | "been 10 s" to "walk is done" |
| 4 | Rush Hour | default 1 to 4 | 90 s; cars each way every 3 s; walkers press at 3, 13, 23 ... 83 | safe; all cross; every green at least 30 s; no red of 45 s; no 60 s wait | add "been 30 s" to rule 1, and add "been 10 s" to rule 4 and move it above rule 3 |
| 5 | Ambulance! | job 4's fixed rules (four) | 90 s; cars every 4 s; walkers press at 38 and 70; ambulance seen 36 to 46, reaches the crossing at 43 | safe; all cross; ambulance never stops | new top rule: "If GREEN and ambulance coming then keep lights" |

Worked checks (for verify): job 1 fixed: press 5, YELLOW 5.5, RED 8.5, WALK 9 to 16, flash to 26, GREEN 26.5; next
press 35. Job 3 unfixed: RED at 8.5, GREEN at 18.5 while the flashing hand shows: "Green while crossing". Job 4
unfixed: GREEN lasts 3.5 s, then each waiting walker gets a new WALK as soon as the steady hand shows (WALK at 7, 24.5,
42, 59.5, 77): the red lasts 86.5 s. With only "been 30 s" added: green 0 to 30, then the same chain of walks keeps the
light red 63 s ("cars stuck"). With only rule 4 changed and moved: greens of 0.5 s. With both: YELLOW 30, RED 33, WALK
33.5, GREEN 51, YELLOW 81, RED 84, WALK 84.5; greens 30 and 30 s, longest red 18 s, longest walker wait 41.5 s. Job 5
unfixed: the press at 38 is seen at 38.5, green has lasted over 30 s, YELLOW 38.5, RED 41.5, the ambulance reaches a
red at 43: "Had to stop", and the report adds "Rule 1 fired first. Rules are checked from the top." Fixed with the new
rule at the bottom: same failure. At the top: green holds 36 to 46, the ambulance passes at 43, then YELLOW at 46, WALK
at 49.5.

## Interactions in detail
- The light starts GREEN with its timer at 0 in every test and after Reset street.
- Rules with a missing light or action are skipped (dashed). Two identical rules: the lower never fires; it gets a
  grey "never fired" tag after a test (useful, not an error).
- During a test every control stays live: Stop ends the test at once without a report; Speed changes at once; Skip to
  report finishes at once; tapping a rule card stops the test at once and selects the card for editing (a test always
  runs one fixed program). In Watch the Street editing is live and counts from the next check.
- Report replay: tap an unsafe line to scrub to that moment; "Back to report" returns.
- Extremes: 6 rules max (Add rule disabled, hint says so); a test with zero rules runs and reports walkers stuck;
  pressing the stage button many times counts once per walker.
- Keyboard: Tab order mode buttons, header buttons, Run test, Speed, Skip to report, Start over, rule cards (Enter
  opens the first empty chip, arrows move between slots, Enter picks), card buttons, Add rule, stage push buttons. Alt
  plus Up or Down moves a selected rule, Delete removes it.
- Motion off: cars and walkers jump between positions each check instead of gliding; lamp changes and timing stay.
- Sizes: the rule list, Run test and the report must fit without page scrolling at 1366x768 and up; at 680x425 and
  800x500 the street strip shrinks and chips show short words; under 760 wide stack street over rules. The rule list
  may scroll inside its panel only when it has more than 4 rules.
- Saves nothing except the kit settings. Each mode keeps its rules for the page load.

## Look
- Band 3-5, own `:root`: `--paper #f6f5f1`, `--ink #1e2228`, `--muted #5a5f66`, `--line #dcd9d0`, `--brand #2f3640`
  (asphalt charcoal; header and panel headings), accent amber `--gold #f2b705` for Run test, the selected chip and the
  fire ribbon outline, `--focus #1d5fd1`.
- Scene (asked of the painter): grey asphalt, cream lane paint, white crosswalk stripes, pale sidewalks, soft green
  grass edges; code pieces over it use asphalt `#3a3f47`. Lamps: red `#d93a2b`, yellow `#f2b705`, green `#1f9d55`,
  always also named in words on chips and in position (red top, green bottom) on the signal.
- Neighbors: network-help-desk green, score-keeper raspberry, code-tracer pencil orange, internet-journey violet;
  siblings snowy-mail-route post red on snow, spot-the-ai steel navy. Charcoal and amber is a street look none use.
- Contrast (computed): white on header 12.19:1; ink on paper 14.64:1; muted on paper 5.9:1; ink on amber 8.79:1;
  amber on charcoal 6.71:1; white on asphalt 10.6:1; focus on paper 5.33:1.

## Art
Local FLUX (`scripts/localart.py`) unless marked people; one flat, bright top-down town style, asked for in one session.
- maple-street: "A top-down view of a quiet two-lane town street running left to right, grey asphalt with a dashed
  cream center line, a wide white striped crosswalk across the middle, white stop lines on both sides of it, pale
  sidewalks along the top and bottom edges with grass strips, round tree tops and a few roof corners at the edges, flat
  bright illustration"; 4:1; cutout no; people no; the street strip, scaled to the stage width.
- Car kit (5 pieces, one prompt: "A single small [car] seen from straight above, top-down, plain roof, flat bright
  illustration, plain white background"); 16:9; cutout yes; people no; traffic in both lanes (turned 180 degrees in
  code): car-red (a red hatchback), car-blue (a blue sedan), car-yellow (a yellow compact car), van-green (a green
  van), car-white (a white station wagon).
- ambulance: "A white ambulance seen from straight above, top-down, a red stripe along each side and a plain light bar
  on the roof, flat bright illustration, plain white background"; 16:9; cutout yes; people no; Send ambulance and job
  5; the flashing is a code glow over the light bar.
- Walker kit (3 pieces, one prompt: "A child seen from straight above, top-down, the top of the head and shoulders and
  a [color] backpack, flat bright illustration, plain white background"); 1:1; cutout yes; people: true (Gemini,
  `scripts/art.py`, Cory reviews); walkers waiting and crossing (a small bob in code): walker-red, walker-yellow,
  walker-green.
- signal-head: "A black traffic signal housing with three round dark unlit lamps stacked top to bottom, front view, flat
  bright illustration, plain white background"; 9:16; cutout yes; people no; the big car signal in the status strip;
  the lit lamp is drawn in code over its dark lamp.
- walk-signal: "A black square pedestrian signal box with a blank dark face, front view, flat bright illustration,
  plain white background"; 1:1; cutout yes; people no; the walk sign in the status strip; the walking person and the
  hands are drawn in code on its face.
Rule cards, chips, the ribbon, report, signal dots, push buttons, timers, warning triangles and preview.svg (the
crossing with a WALK sign lit and a rule card beside it, built from the cutouts) are drawn in code. 12 images, 3 with
people.

## Voice
Bank voice `firm-captain` (Alnilam), "Say firmly but kindly, like a ship captain giving clear directions": framed as the
city's traffic chief. No neighbor uses it (score-keeper friendly-dad, code-tracer clear-teacher, network-help-desk
upbeat-guide, internet-journey smooth-narrator); no sibling in this group. Grade 3: narration for welcomes, job briefs
and report summaries only; rule text is read on screen (Read speaks the hint). `Curio.voice`, `scope: () =>
state.mode`.
How (spoken the first time its moment comes, then hint only):
1. w-watch (Watch the Street entered; stale on the first push button or chip tap): "Welcome to Maple Street. This light
   follows rules. Every half second it checks them from the top, and the first rule that fits wins."
2. press (queued after 1; stale on the first push button): "Press a walk button on the street and watch which rule
   lights up."
3. chip (first chip tap; stale when a chip is picked): "Tap a chip in a rule to change it. Press Add rule to write a new
   one."
4. w-jobs (Street Jobs entered; stale on Run test): "You're the city's new light coder. Each job has a goal. Change the
   rules, then press Run test."
5. report (first report shown, after its summary line; stale when a report line is tapped or a new test starts): "Tap
   a line in the report to see that moment on the street."
Job briefs (how, once per job per page load; stale on Run test or a job change):
6. "Job one: Press to Cross. Walkers press the button, but the light never changes. Press Add rule and write the rule
   that starts it. Then press Run test."
7. "Job two: Don't Skip Yellow. Drivers need a yellow light to stop safely. Fix rule one, and add a rule for yellow.
   Then press Run test."
8. "Job three: Let Them Finish. The light turns green too soon. Find the rule that does it and change a chip. Then
   press Run test."
9. "Job four: Rush Hour. Walkers press all the time. Give the cars a fair turn too: long greens, and no long reds.
   Then press Run test."
10. "Job five: Ambulance! When an ambulance is coming, keep the light green for it. Add a rule, then press Run test."
Events (every time; stale when a new test starts, the job changes or the mode changes):
11. "Test done. Everything was safe, and every goal is met. Job finished." 12. "Test done. There were unsafe moments.
The report shows which rule caused each one." 13. "Test done. It was safe, but a goal was missed. Check the report."
14. "Two rules fit at once, and the higher one won. Try moving a rule." (job 5 order failure, and job 4 when the
changed rule 4 is still below rule 3) 15. "That's every job. Maple Street is safe and fair. Nice work, coder."
16. (Add rule tapped with six rules; stale on the next tap) "Six rules is the most. Change a rule instead."
Which line when: mode entry queues its welcome, then 2 or the job brief; the first chip tap queues 3; a test ends with
11, 12 or 13 (then 14 when it applies), and the first report queues 5 after them.

## Family engine
Robot family engine `kit/robot.js`, described in full in tools/robot-mouse-mail/spec.md (program model, card list UI,
runner with styles sequence and rules, trace). This tool feeds it: style rules; column layout, max 6; each card is
`{light, extras: [0-2], action}`; `when(card, world)` tests the light and extras against the street state; `exec`
changes the lights, starts a walk (nothing while one is showing) or does nothing (keep lights); beat = one check every
0.5 s of street time; the trace drives the fire ribbon, the "Rule 2 did it" lines and the "never fired" tags. Step (one
check) is offered under Pause in Watch the Street.

## Sources
- MUTCD 2009 edition, Section 4D.26 (yellow change interval at least 3 s, at most 6 s):
  https://mutcd.fhwa.dot.gov/htm/2009/part4/part4d.htm
- MUTCD 2009, Section 4E.06 and Figure 4E-2 (walk interval at least 7 s; pedestrian clearance time from a walking speed
  of 3.5 ft per second; flashing hand during clearance): https://mutcd.fhwa.dot.gov/htm/2009/part4/part4e.htm and
  https://mutcd.fhwa.dot.gov/htm/2009/part4/fig4e_02_longdesc.htm
- MUTCD 2009, Section 4E.08 (pedestrian push buttons) and Section 4D.27 (preemption for emergency vehicles), same Part 4.
- CSTA K-12 CS Standards (2017) 1B-AP-10, 1B-AP-11, 1B-AP-15: https://csteachers.org/k12standards/
- Code.org CS Fundamentals glossary (conditional, event): https://code.org/curriculum/docs/k-5/glossary
- Street layout, scripts, driver model and the 60 s, 45 s, 30 s and 10 s fairness limits are the tool's own choices.
- Checks run (Python, 2026-10-29, a half-second rule simulator of the behavior above, every job's starting and fixed
  rules): jobs 1 to 3 and 5 reproduce the worked checks to the half second; job 1's starting rules leave all three
  walkers waiting to the 120 s cap, and rule 1 works at the top or the bottom; job 2 starting gives three "Yellow too
  short", job 3 starting three "Green while crossing", and the fixes give none; in the default cycle the crosswalk
  sits empty at a red for 7.5 s, under the 10 s check. The first draft's job 4 fix (only "been 30 s" on rule 1) failed:
  walkers pressing every 10 s each got a new WALK before rule 4 could turn the light green, so the cars sat at a red
  for 60 s while every goal check still passed. Two changes fixed the job: a new "no red of 45 s" check (catches
  86.5 s and 63 s reds), and "start WALK" doing nothing while a walk is already showing; the fix now also needs rule 4
  with "been 10 s" above rule 3 (rule 4 changed but left below rule 3 still gives a 63 s red). Job 5 was rerun on the
  new four-rule job 4 program: the same YELLOW 38.5, RED 41.5, stop at 43, and with the new rule on top YELLOW 46, WALK
  49.5, walkers wait 11.5 and 30.5 s. Test lengths at 4x: 22.5 s for 90 s scripts, 23.6 s for job 4 fixed, 27.6 s for
  job 5 fixed, 30 s at the 120 s cap. Every contrast ratio in Look recomputed with the WCAG 2.1 formula and matches.

## Done when
1. Watch the Street: the default rules run; pressing a stage button gives YELLOW, RED, WALK 7 s, flashing hand 10 s,
   then GREEN, with each firing shown in the list and the ribbon at the moment the light changes.
2. Every job's starting rules fail the goal for the reason in the table, and the listed fix passes all its checks.
3. The worked checks hold to the half second (log the light changes and compare), including job 4's three variants.
4. Each unsafe kind can be caused on purpose in Watch the Street and is reported with the right words and rule number.
5. Job 5: the ambulance rule at the bottom fails with line 14; at the top it passes.
6. Report lines replay the right moment; never-fired tags appear on dead rules.
7. Focus: at 1366x768 and 680x425 the street strip with the crossing is the widest thing on screen and the rule list
   sits beside it; the report card covers the street, never the rules.
8. Tap while it plays: during a test, Stop, Speed and Skip to report act at once, and a rule card tap stops the test at
   once; in Watch the Street a chip change counts from the next check and a push button press shows at once.
9. Keyboard only: a job can be edited, tested and finished with focus visible.
10. All sizes in STANDARDS.md: rules, Run test and report visible without page scrolling at 1366x768; nothing cut off
    at 680x425 or 375 wide in the host.
11. Voice: welcomes and briefs once per page load; events 11 to 13 every test and dropped when a new test starts.
12. Motion off keeps timing; console clean through all five jobs.

## Open questions
- Job 4's fix is now two changes (a longer green on rule 1, and rule 4 waiting 10 s and moved above rule 3), because
  the one-change fix let cars sit at a red for 60 s. Fine for grade 3 job four, or should Rush Hour space its walkers
  out more so one change is enough?
- The walkers (three top-down children) are the only people, waiting on Cory.
