# Audience Shift Briefing

## One idea
One finding, three rooms: you give the same three-minute briefing about street trees and summer heat to a city board, a neighborhood meeting and a middle school class, and because every room weighs evidence, pictures and words differently, the card that wins the board loses the seventh graders, and you rebuild the briefing for each room while the finding itself never changes.

## Not like
- rhetorical-situation-simulator (ela 11): keeps a famous speech's words fixed and turns the situation dials. Here the student writes nothing famous; they assemble their own briefing from parts and the three rooms are fixed.
- pitch-deck-studio (ela 8, not built): one persuasive slide pitch checked against a checklist. Here there are three audiences at once, and the audience, not a checklist, responds.
- speech-coach (ela 12, not built): delivery practice with pacing and filler counts. Here delivery is only a timed run with a partner; the subject is choosing for an audience.
- argument-builder-pro (ela 9): outlines an argument with counterclaims. Here the claim is settled; what changes is evidence, visuals and register.
- rhetoric-spotter (ela 9): sorts famous lines by appeal. Here the student picks lines and sees who they reach.

## Who and how
- Grade 9 ELA, module Presenting Findings to an Audience (Speaking and Listening).
- Driver: students in pairs on one laptop (one builds, one plays the room in Say it), switching roles per room. 35 to 45 minutes for all three rooms.
- Standards: SL.9-10.4 (present information, findings and evidence clearly and logically, with organization, development, substance and style appropriate to purpose, audience and task): Build and Run. SL.9-10.5 (make strategic use of digital media and visual displays): the Visual choice in each slot. SL.9-10.6 (adapt speech to a variety of contexts and tasks): the register choice and Compare.
- tool.json: driver "students", minutes "35-45", modes ["Build", "Run", "Compare"], grades_label "Grade 9". Kit starter; light theme with its own `:root`.

## Screens and modes
Header: title "Audience Shift Briefing", small line "Same finding. Three rooms."; room tabs **City board**, **Neighborhood meeting**, **Grade 7 class**; mode buttons **Build** (opens first), **Run**, **Compare**; Motion, Sound, Read. The finding (Content) sits in a locked strip under the header in every room and mode, with a padlock glyph and "Same in every room".
Layout: a room scene on the left (drawn in code: a council dais, folding chairs in a community hall, classroom desks; three listeners shown as initial-badges with names); the briefing rail on the right with `#hint`. At 760 wide and below the scene shrinks to a strip of the three badges above the rail.

### Build (opens first)
- The briefing rail has five slots in order: **Opening**, **Point 1**, **Point 2**, **Point 3**, **Close**. A point slot holds one evidence card and, optionally, one visual.
- Tray under the rail with three tabs: **Openings** (three, in three registers), **Evidence** (nine cards), **Visuals** (six plus **No visual**), **Closes** (four). Tap a card, then a slot (or drag; keyboard: Enter, arrows, Enter). Each card shows its words, its source tag (EPA or "Fernvale, made up") and its time in seconds.
- **Time bar** across the top of the rail: total seconds against a 180-second line, with the number "2:35 of 3:00". Over 180 the bar turns warn with "Over time" (word and stripe pattern).
- Each room keeps its own briefing. **Copy from** another room fills the rail with that room's choices as a starting point.
- No meter shows during Build; the room only reacts in Run.

### Run
- **Run the room** plays the briefing slot by slot (about 3 s per slot; **Step** for one at a time). As each slot plays, its card lights and the listeners react: each choice moves the room's **With you** gauge (Content gives every value) and any ±2 choice brings a speech bubble from the named listener (Content).
- Gauge words, from the running total: 8 and up **Leaning in**, 4 to 7 **Listening**, 0 to 3 **Drifting**, below 0 **Lost**. A needle and the word; no color alone.
- At the end: a summary card "Leaning in. Strongest: Local readings (+2). Weakest: Dense table (-2)." and the time line: over 180 the chair says "We need to move on." (board), "Folks, we have one more item." (neighborhood), "Bell's about to ring." (class); under 120 "That's it?" from the first listener.
- **Say it to a partner**: big cue cards one slot at a time with the words to say, a 3:00 countdown, and **Next cue**. The partner holds the laptop and taps one of **With you**, **Lost me**, **Say more** per slot; taps are shown beside the tool's reactions in the summary. No microphone is used.

### Compare
- Three columns, one per room, showing each slot's card. Cards used in all three rooms are marked **Kept**; cards used in one room only are marked **Only here**. Gauges and times sit at the foot of each column.
- Prompts with private text boxes: "Which card did you keep everywhere, and why does it travel?", "Which visual changed most between rooms?", "Write your opening line for a fourth room: the school board."
- **Clear my briefings** (confirm) wipes this tool's storage.

## Content
**The finding** (locked): "East Flats has the fewest street trees in Fernvale and is the hottest neighborhood on summer afternoons. Planting street trees there would cool it." Fernvale, East Flats, Hillcrest and Delmar Street are made up; every local number says "Fernvale, made up" on its card. National numbers come from the U.S. EPA.

**Listeners** (made up)
- City board: Councilor Dana Okafor (budget chair), Councilor Sam Lee (wants proof), City Manager Ruth Bell (chair).
- Neighborhood meeting: Mr. Hector Ruiz (retired, on Delmar Street), Ms. Linh Tran (parent, uses the Delmar bus stop), Jo Adair (renter, chairs the meeting).
- Grade 7 class: Ava, Marcus, Priya, and their teacher Mr. Hale (chair).

**Cards** (id, words, source, seconds; fit for Board / Neighborhood / Class; reaction lines for ±2)
Openings (20 s each):
- O1 Technical: "Our July survey shows a four-degree afternoon gap between East Flats and Hillcrest, and the gap tracks tree canopy." Fernvale, made up. +2 / -1 / -2. Okafor (+2): "Clear and specific. Go on." Ava (-2): "What's canopy?"
- O2 Plain: "East Flats is the hottest part of Fernvale in summer, and it has the fewest trees." +1 / +1 / +1.
- O3 Story: "Stand at the Delmar Street bus stop at three o'clock in July. No shade, hot pavement, and it's four degrees hotter than up the hill." -1 / +2 / +2. Tran (+2): "That's my bus stop." Marcus (+2): "I know that stop."
Evidence:
- E1 Local readings: "On July afternoons East Flats ran 4°F hotter than Hillcrest. Tree cover: 6 percent in East Flats, 31 percent in Hillcrest." Fernvale, made up. 35 s. +2 / +2 / +1. Lee (+2): "Our own numbers. Good." Ruiz (+2): "Four degrees. I believe it."
- E2 Big review: "One review of 308 studies found that, on average, urban forests were 3.0° F (1.6°C) cooler than urban non-green areas." EPA. 30 s. +2 / 0 / -1. Lee (+2): "A review of 308 studies, not one. That I trust."
- E3 How it works: Trees cool the air two ways: shade, and evapotranspiration, which "cools the air by using heat from the air to evaporate water." EPA. 30 s. 0 / +1 / +2. Priya (+2): "So trees kind of sweat? That's cool."
- E4 Energy: "Green infrastructure including urban parks and forestry can reduce ... the energy demand of nearby buildings by 10 percent." EPA. 25 s. +2 / +1 / -1. Okafor (+2): "Lower cooling bills for city buildings too."
- E5 Health: "One analysis estimates that a 10% increase in tree cover would result in approximately 50 fewer deaths per year in Salt Lake City, Utah". EPA. 30 s. +1 / +1 / -2. Mr. Hale (-2): "That's heavy for this group. Maybe another card."
- E6 Hot roofs: "On a warm day, conventional roofing materials may reach as much as 66°F warmer than the surrounding air temperatures." EPA. 20 s. 0 / +1 / +2. Ava (+2): "Sixty-six degrees hotter? On a roof?"
- E7 Rain: "Urban trees can reduce stormwater runoff by absorbing 15 to 27% of annual rainfall." EPA. 20 s. +1 / 0 / 0.
- E8 Cost: "400 street trees at $350 each: $140,000 over two years." Fernvale, made up. 25 s. +2 / -1 / -2. Okafor (+2): "Finally, a number I can budget." Marcus (-2): "Why are you telling us about money?"
- E9 Care plan: "The city waters new trees for three years and sweeps leaves every fall." Fernvale, made up. 25 s. 0 / +2 / 0. Ruiz (+2): "Who rakes? Oh, the city does. Fine."
Visuals (seconds added to their point):
- V1 Bar chart, East Flats against Hillcrest. 15 s. +2 / +1 / +1. Lee (+2): "Two bars. Easy to read."
- V2 Tree cover map by neighborhood. 15 s. +1 / +2 / +1. Adair (+2): "There's my block. No green at all."
- V3 Diagram of a leaf with water going up and out. 20 s. 0 / 0 / +2. Priya (+2): "Oh, that's how it works."
- V4 Drawing: the same street, sunny and shaded. 10 s. -1 / +1 / +2. Marcus (+2): "I'd rather wait for the bus on that one."
- V5 One big number: "3.0°F". 5 s. +1 / +1 / +1.
- V6 Dense table of every number. 25 s. +1 / -2 / -2. Tran (-2): "I can't read that from back here." Ava (-2): "Too many numbers."
- No visual. 0 s. 0 / 0 / -1.
Closes (20 s each):
- K1 Ask for funding: "We recommend funding 400 street trees over two years, East Flats first." +2 / -1 / -2. Bell (+2): "Put it on next month's agenda." Marcus (-2): "We don't have $140,000."
- K2 Ask for support: "Come to the city board meeting and say you want trees on your street." -1 / +2 / 0. Adair (+2): "I'll put it in the newsletter."
- K3 Picture it: "Picture Delmar Street in ten years, with shade over the bus stop." 0 / +1 / +1.
- K4 Something to do: "This week, count the trees on your block and bring your number to class." -1 / 0 / +2. Ava (+2): "I'm doing my street tonight."
Time and gauge examples (for checks): Board with O1, E1 + V1, E2 (no visual), E8 (no visual), K1 = 20 + 35 + 15 + 30 + 25 + 20 = 145 s (2:25); gauge 2 + 2 + 2 + 2 + 0 + 2 + 0 + 2 = 12, Leaning in. The same briefing in the Grade 7 class: -2 + 1 + 1 - 1 - 1 - 2 - 1 - 2 = -7, Lost.

## Interactions in detail
- A point slot with an evidence card but no visual counts as **No visual** (it scores, with 0 s).
- A visual cannot go in a slot without an evidence card ("Add a point first").
- The same evidence card can appear only once per room. Empty point slots are allowed (a two-point briefing is fine) and add nothing.
- Gauge = sum of fit values for the chosen room over Opening, each point's evidence and visual, and Close. Reaction bubbles show only for ±2 choices; each bubble stays 4 s (or until Step), and all of a run's bubbles are listed in the summary.
- Over 180 s still runs; the time line reaction appears. Under 120 s gives the "That's it?" reaction.
- Say it to a partner never records sound. The countdown reaching 0:00 shows "Time" and stops.
- localStorage key `asb.v1` (try/catch): the three briefings, partner taps, Compare notes. Without storage everything works for the session and the hint says so.
- At 680 x 425 the tray becomes one row with tabs; rail, time bar and Run button stay visible.

## Look
Light, a community-hall poster palette. Paper #faf5f9, panel #ffffff, ink #26121f, muted #5e4a58. Accent brand #a61188 (magenta), white text on brand. Room tints are backgrounds only (each room also has its name and scene drawing). Gauge needle in ink; reaction bubbles white with ink text and a listener badge. Positive reaction edge #1d6a3a with a plus glyph, negative #9a3412 with a minus glyph. Over-time stripe #6b5d00. Focus ring #0b6e4f.
Contrast (WCAG): brand on white 6.87, on paper 6.38; white on brand 6.87; ink on paper 16.4; muted on paper 7.51; plus edge 6.14, minus edge 6.78, over-time 6.11 on paper; focus 5.81. Nearest catalog accent: act-it-out #7d2e7f at dE 20.3.

## Art
none: drawn in code (three room scenes in simple shapes, listener initial-badges, the six visuals as small charts and diagrams). No people images.

## Voice
Bank voice `casual-peer`, style "Say it like a friendly classmate who has given this talk before." Not used by a grade 8 to 10 ELA neighbor. `Curio.voice`, `scope: () => state.mode + state.room`. Listener bubbles are read on screen only.
- w-build (how): "Fill the five slots. Watch the time bar. Three minutes is the limit."
- copy (how, first visit to a second room): "New room, same finding. Copy your last briefing or start fresh."
- w-run (how): "Press Run the room and watch who leans in."
- after (event, end of a run; stale on any slot change or room change): "That's how this room heard it. Change one card and run it again."
- partner (how, first Say it): "Say each cue out loud. Your partner taps how it landed."
- w-compare (how): "Here are all three rooms side by side. Find what you kept."

## Family engine
none.

## Sources
- Urban forests 3.0°F (1.6°C) cooler, review of 308 studies; evapotranspiration "cools the air by using heat from the air to evaporate water"; nearby building energy demand reduced by 10 percent; stormwater 15 to 27% of annual rainfall; about 50 fewer deaths per year in Salt Lake City with 10% more tree cover: U.S. EPA, "Benefits of Trees and Vegetation", https://www.epa.gov/heatislands/benefits-trees-and-vegetation, checked 2026-10-27.
- Roofs up to 66°F warmer than surrounding air: U.S. EPA, "What Are Heat Islands?", https://www.epa.gov/heatislands/what-are-heat-islands, checked 2026-10-27.
- Fernvale, its neighborhoods, numbers, costs and people: made up for this tool and labeled so on every card.

## Done when
1. The finding strip is identical in all three rooms and modes and cannot be edited.
2. Building the Board example (O1, E1 with V1, E2, E8, K1) shows 2:25 of 3:00 and runs to Leaning in, with Okafor, Lee and Bell bubbles.
3. Running the same briefing in the Grade 7 class ends Lost, with Ava and Marcus bubbles.
4. Adding V6 in the Neighborhood room brings Ms. Tran's bubble; adding E9 brings Mr. Ruiz's.
5. Going over 180 s shows the room's chair line; under 120 s shows "That's it?".
6. Say it to a partner runs a 3:00 countdown through the cues and records the partner's taps; no microphone permission is ever requested.
7. Compare marks Kept and Only here correctly across the three columns.
8. Briefings and notes survive a reload; Clear my briefings wipes them.
9. At 680 x 425 and 375 wide no horizontal scroll; rail, time bar and Run reachable without scrolling.

## Open questions
- audience-shift-briefing: The finding is locked in every room. Should students be allowed to soften the recommendation for the class (for example "trees help" with no funding ask), or is the lock the point?
- audience-shift-briefing: Keep the Salt Lake City deaths card (E5) at all, given Mr. Hale's reaction already steers the class away from it?
