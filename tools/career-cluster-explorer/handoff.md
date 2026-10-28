# Handoff: career-cluster-explorer

Built 2026-10-28 (BR wave, build agent). Draft: no recorded voice yet (`python scripts/voice.py career-cluster-explorer`
when the lines are final). No art: everything is drawn in code.

## Files

- `src.html`: the tool. Uses `kit:curio` and the careers family engine `kit:careers` (docs/families/careers.md).
- `careers.json`: this tool's own 93 careers (career-match-quiz's 83 plus 10 added in polish round 1) with the Handbook fields (`edu`, `eduNote`,
  `level`, `outlook`, `ooh`, `oohTitle`) and `handbook: {edition: '2025-35'}`. Built in the build agent's scratch
  folder from the live Handbook pages (fetched 2026-10-28); `sources.md` lists every profile URL, the exact wording,
  the seven "See How to Become One" quotes and the larger-profile cases. bls.gov blocks curl (403); fetch pages with a
  browser-like fetch. Never guess a value.
- `sources.md`, `notes.md`, `tool.draft.json`, `voice/lines.json` (upbeat-guide, Zephyr), `art/prompts.json` (empty).

## How src.html is laid out

1. CONTENT: `HOT` (37 hotspots: id, x, y in scene units 2400 x 900, name, line, short name for hints, careers) and
   `TRAILS` (5: id, short, name, end phrase, stops). `HOME` maps career -> hotspot. `__tool.check()` verifies every
   career is in exactly one hotspot, the minimum marker gap in px, and the trail cluster counts (4, 3, 2, 2, 3).
2. LINES and `EVENTS`, then STATE (lanterns, opened careers and opened places are saved in localStorage
   `career-cluster-explorer-lit`, try/catch) and `Curio.voice` with `hint: false` (the tool owns the hint; Read
   speaks `#hint`).
3. The sheet: `Careers.sheet` with theme `night` (colors in the `.cr-sheet.night` rule), facts pay, edu, outlook,
   jobs; `onOpen` -> `careerOpened` lights the lantern (the only place a lantern lights).
4. Lanterns: one row with names when each gets 64 px, two rows of seven in a tall narrow stage, else dots and a
   count (compact). Soft hyphens (`SOFT`) keep long names readable.
5. The scene: `drawScene()` builds the SVG; markers are 44 px buttons in `#marks` inside `#pan`, positioned at
   `x * s, y * s` with `s = town height / 900`. Panning is a translateX on `#pan` (`setPan`, `panTo`), with a 56 px
   pad past both ends so the end markers clear the ◀ ▶ buttons. Drag (inertia only with Motion on), wheel, arrow
   keys, buttons, the minimap. A scroll of the clipped `#town` (scrollIntoView, screen readers) becomes a pan.
   Focusing a marker pans it into view.
6. The card (`openHot`, `placeCard`, `closeCard`): beside the marker, flipping near the edge; a bottom sheet under
   560 px. Esc closes the sheet first (the engine stops the key), then the card, and focus goes back to the marker.
7. Where? (`where(k)`): a hotspot with an unopened career of that cluster, never the last suggestion unless it is
   the only one (Manufacturing: all four are at the Ferris wheel, so the hint says "Still the Ferris wheel: it's the
   only place..."). Compact layouts have one Where? button that walks the dark clusters in turn.
8. Trails: `pickTrail`, `goStop`, `drawTrail` (dim layer, dotted path through the distinct hotspots, numbered
   stops; a hotspot holding several stops shows "3-5"). trailEnd2/3/4 are events with a `valid` that drops them
   when the trail or stop changes; picking a trail drops a queued trailEnd.
9. Clusters: the grid (full names, short names in compact and narrow), the ladder (5 columns from 900 px of board,
   else rows), pay bars on one $0 to $250,000 scale (musician and actor have hourly pay, no bar), outlook arrow,
   percent and word, See it.
10. Panel and hint: `drawPanel` rebuilds the Where? and List buttons only when their set changes and keeps focus.
    `hintText()` is computed from state and set at once on every change.
11. Layout: `relayout()` picks wide / compact / stack (as in fake-or-fact-lab), sets `narrow` under 560 px, sizes the
    stack stage, the lanterns and the scale, and keeps the view centered across resizes. In compact and stack the
    trail controls come before the trail picker; compact and narrow use a select for the picker.

## Tricky parts

- The audit's overlap leads between markers and panel controls are markers clipped by the stage (their boxes run
  past `#town`, which hides them). They are not visible or clickable there.
- `state.trail` can be 0: always test `!== null`.
- The engine sheet's Esc handler stops propagation; the page's own Esc handler then sees nothing while the sheet
  is open, by design.
- `Careers` is a page global, so frames can draw a default sheet (`Careers.sheet({data: __tool.DATA}).open('welder')`)
  to check parity with career-match-quiz.

## What I would do next

- Record the voice. Consider a "nice, you found Manufacturing" style event line per new lantern if Refine finds the
  festival too quiet (the spec has none, so I added none).
- The ladder chips are tall in narrow columns; a denser chip would show more careers at 1280 x 720.
- Move career-match-quiz onto `kit/careers.js` when it is next touched, and teach `scripts/careers_data.py` to write
  the Handbook fields (the open question in the spec).

## Polish round 1

2026-10-28. Checked with scripts/drive.py, using held clicks and real keys, on ports 9950-9954, plus the 375 host on 9951 (host.html deleted). Sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 and 375x812. No console errors. `__tool.check()` shows 93 careers, none missing or duplicated, and a minimum marker gap of 44.6 px at 375. voice/lines.json still matches allLines() (L unchanged). Bundled with CURIO_DRAFT=1.

1. Added 10 Handbook careers through `C_MORE` in scripts/careers_data.py (`--more`; each one checked on its live Handbook page, with O*NET OnLine interests). Edu, Public Service and Health now have ways in at all 5 levels. The ladder line and the panel now say "Careers in this tool: ways in at N of 5 levels" and add that the real cluster has more. Empty columns read "None in this tool (the real cluster may have some)". Notes question 3 is reworded and the spec claim is fixed. Checked: the fin, mgmt, mfg and health ladders at 1366.
2. Hairstylist moved to health and Real Estate Agent to fin in careers_data.py; careers.json rebuilt and counts updated. Checked: the stylist sheet and the fin ladder.
3. Focusing a marker pans only on `:focus-visible`, so a pointer press never pans. Checked: held clicks on a marker 50 px from the right and left edges at 680x425 and 1366, and 30 px from the edge at 375. Each opened the card.
4. Only `ctx.from` 'card' or 'trail' lights a lantern. The sheet's lantern line says "lit" or "not lit yet. Meet this job at the festival to light it." Checked: a held click on a ladder job and on a Similar career (lit 0, line correct) and on a card job (lit 1).
5. "People doing it" now uses the Handbook's number of jobs (`oohJobs`), and the sheet names the profile and says it counts self-employed workers. Checked: Farmer shows 789,000.
6. New psychologist path text. Checked on the sheet.
7. `DEF` holds one plain line per cluster (from careertech.org "The Cluster Defined"). It shows under the ladder heading and on the sheet's lantern line. Spec Sources and sources.md updated. Checked on the ladders and sheets.
8. allLit is queued with `wait`; if it is dropped, allDone is cleared so it comes back. Checked: lit the 14th lantern during the first-tap welcome. Log: welcome spoken, then allLit spoken at 6.5 s.
9. When Next or Back disables itself while focused, focus moves on (Next to Open career, Back to Next). Checked with real Enter (activeElement openCareer / next) and a held click at 375.
10. The clusters grid uses 2 columns at narrow widths and 3 in compact. Checked: no clipped names at 375, 680, 760 or 800.
11. lanternHow plays only in Festival. closeCard queues [lanternHow, panHow] as one sequence. Checked: the log shows lanternHow spoken, then panHow spoken. In Trails, no lanternHow.
12. Esc on the confirm puts focus on Start over. Checked with real Esc.
13. kit/careers.js reads keys on document in the capture phase while the sheet is open (documented). Checked: clicked the sheet text, then Esc, and the sheet closed.
14. The card button reads "✕ Close". New hint: "Tap Close, or press Esc, to close the card." Checked at 680, 800 and 1366.
15. Emoji: doctor 🧑‍⚕️, chef 🧑‍🍳, hairstylist ✂️. Checked on the sheets.
16. The education fact says the level in plain words, with the Handbook phrase and note underneath (`eduPlain`). Checked: machinist, psychologist and farmer.
17. Pay label is now "Median pay for this job, 2025". When the profile's pay differs, the sheet adds "The Handbook page covers a larger group, ...". Checked: machinist, psychologist and stylist.
18. New pilot and ATC path lines in careers_data.py.
19. Police head fill is #c9c3ea. Checked on the SVG.
20. Fashion 🧵, Musician "places of worship" and the new hotel-mgr try line, all in careers_data.py.
21. At the last stop in a stacked layout, the page scrolls so the trail result is in view. Checked: endrow bottom 800 of 812 at 375 and 988 of 1000 at 760.
22. Stacked Clusters let the page scroll (no inner box). Ladder chips are shorter: on rows, See it sits on the name row, and compact uses one-column, two-line chips with no level subtitles. Checked: 375 board 1808/1808, page 2525; 680 Health 369/1365 (was 341/1461).
23. Lanterns use the `big` class when each gets 100 px or more and the screen is 900 px or taller. Checked: 1920x1080.
24. In compact with innerHeight of 600 or more, the Still dark list shows. Checked: 1000x625.
25. The pop and shimmer wait in `state.pops` until the sheet closes (`popLater`). Checked: no pop under the sheet, ln-mfg pops after close.
26. Hint now reads "Stuck? Tap Where?" with no doubled period. Stop header uses non-breaking "Stop N of M". Checked: header is one line (16 px) at 1280 and 1366.
27. Where? by keyboard (detail 0) focuses the circled marker. Checked with real Enter at 680 (Where?) and at 1366 (Still dark): focus lands on mk-ferris. A mouse click leaves focus on the button.
28. A card opened from the List returns focus to its List entry. Checked: Esc gives list:barn.
29. `cardMet()` adds "✓ met" in place. Checked: shows on the welder job while focus stays on it.
30. The scale line now sits above the ladder. Checked at 1366.
31. The family doc covers the fixed ids, the capture-phase Esc and Tab with preventScroll. Also: the sheet header keeps 116 px clear so a long name no longer runs under "✕ Close" (seen at 375).
32. Privacy line: "Your lanterns and the careers and places you opened are saved in this browser on this device only. Nothing leaves it." Notes updated.
Settled calls: Flight Attendant and PR are marked unconfirmed in sources.md. The braids booth, crosswalk officer and help booth are unchanged. career-match-quiz and its careers.json are untouched; the builder still writes to the quiz path by default, and the quiz picks up the fixes when it moves to kit/careers.js.
Not done: the optional nit to hide marker labels while the card is open. Spec open questions are left as they were.
