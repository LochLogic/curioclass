# Fitness Circuit

## One idea
A projected circuit that stops between stations for a quick pulse count and a talk test, then draws the class's own heart chart, so students see heart stations push effort up and stretch stations bring it down, and race to beat their own round one in round two.

## Not like
- animal-moves (K-2 PE, showdown, movement family): copy one animal's move to a beat, with a freeze game. Fitness Circuit times real exercise stations in the three fitness components and measures the body between them; no animals, no freeze game.
- playbook (3-5 PE, builder): strategy on a screen. Fitness Circuit is all body; the screen is the coach and the clipboard.
- habit-hero (K-2 health, creature): a hero's meters show habits. Fitness Circuit's chart shows the class's real effort and pulse.
- body-systems-tour (3-5 health, explorer): rides through the body's systems. Fitness Circuit feels the heart from the outside, with a pulse count, and never tours anatomy.

## Who and how
- Grade 3-5, Physical Education, module Fitness Components (cardio, strength, flexibility and heart rate).
- Driver: teacher on a projector in a gym or classroom (whole class at once, or groups rotating through stations).
- Minutes: 15-30 (the default 6-station circuit with its checks is about 6 minutes per round, about 12 minutes for its two rounds and the cool-down).
- Standards: SHAPE.S2 (applies knowledge of fitness concepts: components, heart rate, effort).
- Topic line: "cardio, strength, flexibility and heart rate".
- Modes (tool.json): ["Go", "Build", "Heart chart"].

## Screens and modes
Header: title "Fitness Circuit" with small line "Cardio, strength, flexibility and heart rate", mode buttons **▶ Go**, **🛠 Build**, **📈 Heart chart** (keys 1 to 3), **Motion**, **Sound**, **Read**. Stage left, panel right (below under 760 px wide).

### Go (opens first, with the default circuit ready)
- Focus: the move card, with the pose figure doing the move, as the biggest thing on the projected screen; the ring is second. On check screens the focus is the three big talk test buttons (or the pulse ring).
- Stage, whole-class layout: the move card fills the left two thirds over the painted gym wall (Art) (component tag with icon, big name, three cues, the pose figure doing the move on a loop); the timer ring on the right with seconds in the middle; a station strip along the bottom (one small tile per station, done ones checked, the current one raised). In round 2 each card shows a ghost badge: "Round 1 effort: 😮‍💨 Hard. Beat your round 1 count!"
- Stage, groups layout: a grid of station tiles (one per station, each with a mini figure and name) and a group badge (1 to 6, each a different shape and color) on the tile where that group works. The timer ring sits in the corner. On **Rotate**, each badge slides to the next tile clockwise.
- Panel: **▶ Start** (becomes **⏸ Pause** / **▶ Resume**), **⏭ Skip**, **■ Stop**, a "Next up" card, and the hint. Pause, Skip and Stop stay live the whole run and act at once.
- Check screens (a talk test after every station; a pulse count when the Pulse count setting calls for one): see Interactions.

### Build
- Focus: the circuit list in the panel as it grows; the tiles are the palette.
- Stage: the 12 station tiles in three rows by component, each with its icon, mini figure and name. Tap a tile to add it to the circuit list (panel); tap a list item to remove it; drag to reorder. 3 to 9 stations.
- Panel: **⚖ Balanced mix** (sets: Jumping jacks, Squats, Butterfly stretch, High knees, Wall push-ups, Reach and lean: the default circuit), **🎲 Surprise mix** (two of each component, shuffled so no two stations in a row share a component), and settings as two- or three-way toggles: **Work** 20 / 30 / 45 s (default 30), **Pulse count** After each station / After each round / Off (default After each round; the talk test comes after every station whatever this says), **Rounds** 1 / 2 (default 2), **Layout** Whole class / Groups, **Groups** 2 to 6 (only with Groups; must not exceed the station count).
- A line under the settings: "About 12 minutes" (computed from the plan and rounded to the minute: per station 5 s ready + work + 10 s talk test + 10 s move on; plus 25 s for each pulse count; times the rounds; plus the 30 s cool-down. The default plan gives 740 s, about 12 minutes).

### Heart chart
- Focus: the chart lines; the summary lines in the panel name what they show.
- Stage: a line chart. X: the stations in order (icons and names), one point per check. Y: effort 1 Easy, 2 Working, 3 Hard. Point markers by component: heart stations a filled circle, muscle stations a filled square, stretch stations a hollow diamond. Round 1 is a solid line; round 2 a dashed line. If any pulse counts were entered, a second panel below shows them as beats per minute with the same markers.
- Panel: three summary lines computed from the data ("Heart stations: average effort 2.7", and so on for muscles and stretch), the station with the highest effort ("Hearts worked hardest at High knees"), four fact cards (Content), **🧽 Clear chart**.
- With no data yet: the chart shows a light sample labelled "Example" and the hint says to run the circuit.

## Content

### Stations (component, beat, poses A and B for the figure, three cues)
| Id | Name | Comp | Beat | Pose A / Pose B | Cues |
|---|---|---|---|---|---|
| jacks | Jumping jacks | heart, bone | 120 | feet together, arms down / feet wide, arms up in a V | Jump feet wide, arms up. Jump feet together, arms down. Land softly. |
| knees | High knees | heart | 150 | left knee up to hip, right arm forward / right knee up, left arm forward | Run in place. Knees up to hip height. Pump your arms. |
| skater | Skater hops | heart, bone | 96 | on left foot leaning left, right leg behind / mirror on right foot | Hop sideways from foot to foot. Swing your arms across. Land softly with a bent knee. |
| rope | Pretend jump rope | heart, bone | 132 | on toes, wrists at hips / small hop, wrists circling | Small jumps on your toes. Turn your wrists like you hold a rope. Stay light and quiet. |
| pushup | Wall push-ups | muscle | 50 | arms straight, hands on wall, body leaning / elbows bent, chest near wall | Hands on the wall, shoulder width. Body straight like a board. Bend your elbows, then push away. |
| squat | Squats | muscle | 50 | standing / hips back and down, arms forward | Feet shoulder width apart. Sit back like into a chair. Chest up, knees over toes. |
| plank | Plank | muscle | hold | forearm plank / same (slow breathing rise) | Forearms down, elbows under shoulders. Straight from head to heels, or to knees. Keep breathing. |
| superman | Superman hold | muscle | hold | lying face down / arms and legs lifted a little | Lie on your tummy. Lift arms and legs a little. Look at the floor and breathe. |
| butterfly | Butterfly stretch | stretch | none | sitting, soles together / knees lower, leaning slightly | Sit tall, soles of your feet together. Let your knees drop gently. Hold still, no bouncing. |
| lean | Reach and lean | stretch | none | right arm up, leaning left / left arm up, leaning right (switch halfway) | Reach one arm up high. Lean gently to the side. Switch sides when you hear it. |
| toes | Seated toe reach | stretch | none | sitting, legs straight / reaching toward toes | Sit with your legs straight. Reach toward your toes. Stop at a gentle pull, not pain. |
| shoulder | Shoulder stretch | stretch | none | right arm across chest / left arm across chest (switch halfway) | Bring one arm across your chest. Hold it with your other hand. Switch arms when you hear it. |
Component tags: **❤ Heart** (cardio: heart and lungs), **💪 Muscles** (strength), **🧘 Stretch** (flexibility), and a small **🦴 Bones** tag on jumping stations. Beat: the drum loop's tempo in beats per minute; 50 is a slow "down, up" count for muscle stations; hold and none play a soft pad instead of drums.

### Check screens
- Talk test (always first in a check): "How did that feel? Show me 1, 2 or 3 fingers." Three big buttons: **😀 1 Easy: I could sing**, **🙂 2 Working: I could talk, not sing**, **😮‍💨 3 Hard: only a few words**. The teacher taps what most hands show.
- Pulse count (when the Pulse count setting calls for one, after the talk test): "Two fingers on the side of your neck, or on your wrist below your thumb. Count every beat until I say stop." A 15-second ring. Then "Stop! Times your number by 4." A times-4 strip shows 10 → 40, 15 → 60, 20 → 80, 25 → 100, 30 → 120, 35 → 140, 40 → 160. Optional stepper **− / +** (5 to 50, default empty) to enter one count (a volunteer's) and **Save count**, or **Skip**.
- Move on: "Walk to the next station. Shake out your arms." 10 s (groups layout: "Rotate!" with the whistle).

### Fact cards (Heart chart)
1. Every day / Kids 6 to 17 need at least 60 minutes of moving every day, mostly heart-pumping activity.
2. Three a week / On at least 3 of those days, do muscle-strengthening and bone-strengthening activity. Jumping counts for bones.
3. Talk test / If you can talk but not sing, you are working at a moderate level. If you can only say a few words, it's vigorous.
4. Resting heart / At rest, a heart of a 7 to 9 year old usually beats about 70 to 110 times a minute. It speeds up when you move and slows down when you rest.

## Interactions in detail
- Station flow: Get ready 5 s (card shows the station, cues spoken, timer grey) → Work (whistle, beat on, figure loops in time with the beat, ring counts down; beeps at 3, 2, 1) → whistle → talk test → pulse count (if due) → Move on 10 s → next station. Halfway through "lean" and "shoulder", the event line "Switch sides!" and the figure mirrors.
- The talk test comes after every station, so every station gets its own effort point (the chart's per-component summaries and the round 2 ghost badges need one per station). Pulse count "After each round" adds one pulse count after the last station of each round; "After each station" after every station; "Off" never. The talk test waits for a tap (no timer) with a **Skip** button; the pulse ring runs on its own once started with **▶ Start count**.
- A whole run is longer than 30 s because it times real exercise; Pause, Skip and Stop stay live throughout, and a tap acts at once (Pause freezes the ring mid-second, Skip mid-line stops the line).
- Pause freezes the ring, beat and figure; Resume continues from the same second. Skip ends the current segment early (a skipped work segment gets no check). Stop ends the run and keeps checks done so far for the chart.
- Round 2 repeats the same stations. Its card shows the round 1 effort for that station (the ghost badge); the chart draws round 1 dashed behind round 2.
- End: "Circuit done!" card with a 30-second cool-down (slow walk in place, beat 60, figure walking), then a button **📈 See the heart chart**.
- Groups layout: groups start on tiles 1 to N; every Rotate moves each group to the next tile. A group that has done every station shows a check on its badge. The talk test in groups layout asks each group in turn ("Group 1, show me your fingers") with one tap per group; the chart then uses the average.
- Motion off: the figure shows Pose A with an arrow to Pose B in place of the loop; ring, beat and timing unchanged.
- Sound off: no beat, whistle or voice; the ring and on-screen words carry the timing.
- Nothing is stored after the page closes except the Build settings (localStorage `fitness-circuit-plan`, with **Reset to default** in Build). Pulse counts and effort taps stay in memory only.
- Sizes: the ring and the Start/Pause button are visible without scrolling at every size; on a projector at 1920x1080 the station name is at least 72 px.

## Look
- Accent `--brand` #6f2dbd (electric violet), on a light theme on its own `:root`: paper #faf6ff, ink #241a2e, muted #5f5470, line #e6dcf3, focus #1f6fb2 (the accent differs from its family sibling animal-moves, blue #1f6fb2, and from pressure-point's deep berry #a3263f; it replaces the old raspberry #c2185b, which sat too close to that berry).
- Contrast: accent on paper 7.07:1, white on accent 7.54:1, ink on paper 15.6:1, muted on paper 6.59:1.
- Component colors (always with icon and word): Heart #bf360c, Muscles #1565c0 (5.75:1 on white), Stretch #2e7d32 (5.13:1). Heart #bf360c is 5.6:1 on white (the first pick #d84315 was 4.44:1, too low).
- The pose figure: a smooth jointed figure drawn in code (rounded limbs, plain oval head with no face, a violet shirt and grey shorts), 2 px darker outline, standing on the painted mat in front of the painted gym wall.

## Art
Local FLUX (`scripts/localart.py`), one style: "bold screen-print poster style, clean shapes". 2 images, none with people.
- fc-gym-wall: "A bright school gym corner in daytime, a pale wall with a wide blank banner, a wooden floor with a long blue exercise mat in front, a rack of colorful balls at the side, bold screen-print poster style"; 16:10; cutout no; people no; the backdrop behind the move card in Go (the figure stands on the mat; the station name sits on the blank banner in code).
- fc-water-break: "A water bottle, a folded towel and a stopwatch on a wooden bench, bold screen-print poster style, plain white background"; 4:3; cutout yes; people no; on the "Circuit done!" card and the Move on screen.
Drawn in code: the pose figure and every tile's mini figure. It is the movement engine's jointed figure (`Move.figure`), which bends joint by joint in time with each station's beat, holds with a breathing rise, and mirrors at halfway; two painted poses per station could not do that, and the dance family shares the same figure. Also code: tiles, ring, check buttons, times-4 strip, the chart, badges and preview.svg.

## Voice
`big-sister` (Leda): "Say in a friendly, youthful way, like a helpful older student", here a peer leading the circuit. Different from animal-moves (`hero-coach`, Puck), body-systems-tour (upbeat-guide), growing-up-q-a (clear-teacher) and playbook (lively-host). Spoken because students are moving and can't read the board.

| Key | Kind | When it plays | Line | Stale when |
|---|---|---|---|---|
| wGo | how | entering Go, first time | Let's do a circuit! Find your space. Teacher, tap Start when everyone is ready. | mode left or run started |
| wBuild | how | entering Build, first time | Tap stations to build your circuit. Or tap Balanced mix for one of each kind. | a tile or mix tapped; mode left |
| wChart | how | entering Heart chart, first time | Here's your class heart chart. Read the lines to see which stations made hearts work hardest. | mode left |
| next.<id> | event | each Get ready | "Next: jumping jacks." (one per station, with its name) | segment changed |
| cues.<id> | event | each Get ready, after next | the station's three cues as one line | segment changed |
| go | event | each Work start | Go! | segment changed |
| switch | event | halfway through lean and shoulder | Switch sides! | segment changed |
| stop | event | each Work end | Stop! | segment changed |
| talk | how | the first talk test of the load | How did that feel? Show me 1, 2 or 3 fingers. Teacher, tap what most hands show. | talk test left |
| group1-6 | event | each group's turn in a groups talk test | "Group 1, show me your fingers." (six lines) | talk test left |
| pulse | how | the first pulse count of the load | Two fingers on your neck or wrist. Teacher, tap Start count. | count started or skipped |
| count | event | each pulse count start | Count every beat until I say stop. Go! | count ended |
| times4 | event | each pulse count end | Stop! Times your number by 4. That's your heart rate. | pulse screen left |
| move | event | each Move on (whole class) | Walk to the next station. Shake out your arms. | segment changed |
| rotate | event | each Move on (groups) | Rotate! Move to the next station. | segment changed |
| round2 | event | round 2 start | Round two! Try to beat your round one count. | run stopped |
| done | event | run end | Circuit done! Walk slowly and breathe. | run stopped |
| hardest | event | opening Heart chart with data | "Hearts worked hardest at high knees." (one per station) | mode left |
After the first talk test and pulse count, their how lines only update the hint (the screen shows the buttons and words). Fact cards are read on screen (Read speaks them).

## Family engine
**movement** (siblings: animal-moves, built; fitness-circuit is the first spec in the family, so it holds the full description). The builder extracts the engine into `kit/movement.js`; animal-moves keeps its own copy until it is next touched. It is the PE figure only: dance has its own figure in `kit/dance.js` (BASELINE w1-21), so nothing is shared with the dance family (integrator note, BR1, 2026-10-28).
- `Move.card(el, {title, tag, cues, color})`: the move card (title, tag chip with icon, up to three cues).
- `Move.figure(el, {poses: [A, B], beat, mirror})`: the jointed pose figure in SVG. A pose is a set of joint angles (shoulders, elbows, hips, knees, trunk lean, body angle for floor moves). Loops A to B to A on the beat (two beats per cycle), or holds A with a slow breathing rise for "hold". Motion off: shows A with an arrow toward B. animal-moves passes an image instead of poses; the card works the same.
- `Move.ring(el, secs, {beepLast: 3})`: the countdown ring; returns a promise; pause and resume aware.
- `Move.beat(bpm | 'pad' | null)`: the synthesized drum loop from animal-moves (kick, snare, hat, bass line) at a tempo, or a soft pad for stretches.
- `Move.whistle()`, `Move.beep()`: two-tone whistle and short beep (silent with Sound off).
- `Move.run(segments, {onSegment})`: the sequencer. A segment is `{kind: 'ready'|'work'|'check'|'move'|'freeze'|'cool', secs, card, bpm, line}`; it handles Pause, Resume, Skip, Stop with a run token so a stopped run never speaks or ticks again, and calls `Curio.voice` lines at segment starts.
Fitness Circuit feeds it: 12 stations (cards, poses, bpm), segment lists built from the Build settings, check segments that wait for taps, and the groups layout (its own, not in the engine).

## Sources
- SHAPE America, National Physical Education Standards (2024), Standard 2: https://www.shapeamerica.org/standards/pe/
- 60 minutes a day for ages 6 to 17, mostly aerobic; muscle- and bone-strengthening at least 3 days a week; jumping as bone-strengthening: U.S. Department of Health and Human Services, Physical Activity Guidelines for Americans, 2nd ed. (2018), chapter 3; CDC "Physical Activity Recommendations for Children": https://www.cdc.gov/physical-activity-basics/guidelines/children.html
- Talk test (talk but not sing is moderate; only a few words is vigorous): CDC, "Measuring Physical Activity Intensity": https://www.cdc.gov/physical-activity-basics/measuring/index.html
- Taking a pulse at the neck or wrist, counting 15 seconds times 4: American Heart Association, "Target Heart Rates Chart": https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates
- Resting heart rate 70 to 110 for ages 7 to 9 (60 to 100 for 10 and older): MedlinePlus Medical Encyclopedia, "Pulse": https://medlineplus.gov/ency/article/003399.htm
- Static stretches held steady without bouncing, to mild tension not pain: American College of Sports Medicine, ACSM's Guidelines for Exercise Testing and Prescription, 11th ed. (2021), flexibility recommendations.
- Exercise cues (form for squats, wall push-ups, plank): ACSM "Resistance Training for Health" infographic and NSCA Youth Resistance Training position statement (Faigenbaum et al., J Strength Cond Res 23(5), 2009).
- Art: original paintings made for this tool with local FLUX (Art).
- Checks run (Python, 2026-10-29): times-4 strip 10, 15, 20, 25, 30, 35, 40 gives 40, 60, 80, 100, 120, 140, 160 (all match). Time estimate: default plan (6 stations, 30 s work, 2 rounds, pulse count after each round) = 2 x (6 x (5 + 30 + 10 + 10) + 25) + 30 = 740 s, about 12 minutes, about 6 minutes per round; the old "about 12 minutes per round" line was wrong and is fixed in Who and how. Pulse count after each station: 990 s, about 16 minutes; 9 stations at 45 s for 2 rounds: 1,340 s, about 22 minutes; 3 stations at 20 s, 1 round: 190 s, about 3 minutes. The old spec ran the talk test only with each pulse check, so the default (after each round) gave one effort point per round: the per-component averages and the round 2 ghost badge per station had nothing to show; the talk test now comes after every station. Contrast in Look recomputed (WCAG 2.1): all match to rounding (#d84315 is 4.44:1 and stays rejected).

## Done when
1. Go works on first open with the default circuit: Start runs Get ready, Work, whistle, talk test, Move on for each station, and a pulse count after the last station of each round; Build shows "About 12 minutes" for it.
2. Every station's figure moves in time with its beat (one cycle per two beats), holds for plank and superman, and mirrors at halfway for lean and shoulder.
3. Pause and Resume keep the same second; Stop silences everything at once and no line or tick follows.
4. Talk test taps and saved pulse counts appear on Heart chart with the right markers; the summary averages match a hand recomputation; Clear chart empties it.
5. Round 2 shows each station's round 1 effort badge and the chart's dashed round 1 line.
6. Groups layout with 4 groups and 6 stations rotates badges clockwise on each whistle; each group's talk test is asked in turn.
7. The times-4 strip numbers are right; no heart rate zone or target is shown for children.
8. At 1366x768 and 1920x1080 the station name, cues, ring and Start are visible together; at 1000x625 the preview stays readable (cue text 12 px or more).
9. How-to lines are spoken once per load; station calls, Go, Stop, Switch sides and times-4 speak every time they happen.
10. Focus: on a projector at 1920x1080 and at 1366x768 the move card with its moving figure is the biggest thing in Go, standing on the painted mat; on a check screen the three talk test buttons are the biggest thing.
11. Tap while it plays: Pause, Skip and Stop act at once in every segment (mid-work, mid-line, mid-count); after Stop no line, beep or tick follows.
12. Heart chart after a default run has one effort point per station per round, and the Heart, Muscles and Stretch averages each use their own stations.

## Open questions
- The pose figure stays the movement engine's jointed figure drawn in code (it bends on the beat and is shared with the dance family). Painting it instead would take 24 images of a child exercising (12 stations, 2 poses), all people: true and waiting on Cory. Keep the code figure?
