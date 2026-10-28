# Play lens: career-cluster-explorer

Played cold from spec.md, src.html, notes.md, voice/lines.json and kit/careers.js, on the draft bundle
(`CURIO_DRAFT=1`, 175 KB). Played twice: once as a grade 6-8 student alone at home, once as a teacher projecting a
"who made this?" warm-up. All input through `scripts/drive.py` with held clicks (`hold` 0.12 s), real keys and a
jittered real drag; 375 wide through `drive.py --host`. Frames in my scratch folder `lens-cce-play/shots`.

Counts: blockers 1 (general 1, family 0), should fix 4 (general 4, family 0), polish 7, nits 4.

## Blocker

**B1. Tapping a marker near the edge of the view does nothing (general).** `src.html:683` (marker `focus` runs
`ensureVisible`) and `:740-743`. When you press a marker, the button takes focus. If the marker is within 90 px of
either edge of the town, `ensureVisible` then starts a 420 ms pan, and the marker slides out from under the pointer
before you release, so the click never fires. The scene moves and no card opens; the student has to find the marker
again and tap a second time.
- Seen at 1366x768: `#mk-food` (x about 955 in a 1026 px town). Held click, card null, pan -56 to 385
  (`edge-1366-food.png`).
- Seen at 680x425: `#mk-weather` and `#mk-gate` (`edge-680-weather.png`, `edge-680-gate`). Card null, pan -56 to 62
  and to 102, while `#mk-bridge`, nearer the middle, opened.
- In the 680x425 preview the 90 px bands cover about 180 of the town's 410 px, so close to half the markers you can
  see fail on the first tap. That is the first thing a student does.

This is the BR1 lesson "nothing moves or rebuilds under the pointer". Better: don't pan on a pointer focus (only on
keyboard focus, `:focus-visible`), or pan after the click.

## Should fix

**S1. allLit is lost when the 14th lantern lights during the first-tap welcome (general).** `src.html:497-501`.
- Repro: reload with 13 lit, tap the Ferris wheel, then tap Welder within about 4 s. The lantern lights and the
  panel says all 14, but the log shows only `welcomeFestival` after an 8 s wait. allLit is not spoken, dropped or
  silent (`all14b`).
- The same steps with the job tapped after the welcome ends do speak allLit (`all14-mid`, spoken at 8.5 s).
- When it happens: a student who comes back the next day with 13 lit hits exactly this.
- Spec "Done when" 3 and 9 (allLit once, event lines every time) fail in this case.
- Also, the line never comes back. `allDone` is saved as true, so no later moment replays it.

**S2. Focus falls to the page at a trail's last stop (general).** `src.html:1004`. Pressing Next onto the last stop
disables Next while it has focus, and focus drops to `body`. Seen in `t-kettle-end`, `t-bridge-end` and
`t-lights-end`, where the active element is `body` each time. A keyboard student loses their place right at the
result, and pressing Enter again does nothing. BR1 lesson "focus is kept when controls rebuild": move focus to Back
or Open career, or to the end row.

**S3. Cluster names are clipped in the Clusters grid at 375 wide (general).** `src.html:189-193` (`.cl`
`overflow:hidden`, 4 columns at 375). In `n375-clusters` (montage `m375b.png`):
- Clipped mid-word: "Manufa" (the soft hyphen is cut off), "Constru", "Educati" (Education has no break point).
- Breaks that read badly: "Hospi-", "Market-" and "Manage" on the next row.

BR1 sizes lesson: unclipped text at 375 through `--host`. Better: 2 columns of clusters when the body is `narrow`.

**S4. The lantern line, the core idea, is often lost on the first lantern, and can play in the wrong mode
(general).** `src.html:502-504`, `:836`.
- Lost: a student who opens a job, closes the sheet and closes the card within about 3 s never hears "That lantern
  is a career cluster. Find all fourteen." The welcome is still playing, and closing the card queues panHow, a newer
  how-to that replaces the queued lanternHow. The log shows `lanternHow dropped (newer)` in `startover`, `calm-card`
  and `keys-enter-esc`. It comes back only when a second lantern lights.
- Wrong mode: opening a career from Trails speaks "That lantern... Find all fourteen" (`t-open`). But in Trails the
  lantern row shows "This trail" (2 of 3), not the student's lanterns, so the line names a different thing from the
  one on screen.

Better: give lanternHow priority over panHow (queue panHow only after lanternHow is heard), and add
`state.mode === 'festival'` to its `valid`.

## Polish

- **P1. The trail result needs scrolling on narrow screens (general).** At 375x812 the "These stage lights took 3
  clusters" row starts at y 786 (`n375-trails`). At 760x1000 it runs 940 to 1011 (`tr-end-760x1000`). In stack
  layout, put the end row above the stop box at the last stop, or scroll it into view with `preventScroll` kept for
  focus.
- **P2. The Ways in ladder is a small scroll box at 680x425 and 375 (general).**
  - 680x425: the board is 341 px tall with 1461 px of content (`c-health-680`).
  - 375 wide: 317 px with 1889 px of content, inside a page that also scrolls (`n375-ladder`).
  - A student sees one level at a time and can't compare the levels.
  - Better: shorter chips (put "See it" on the name row, not its own 44 px row), or let the page scroll at 375
    instead of the board.
- **P3. The lanterns are small for a projector (general).** At 1920x1080 the lamps are still 18x24 px with 11 px
  names across a 1580 px stage (`first-1920x1080.png`), while the scene scales up. The class can't read which
  clusters are lit. Scale the lantern row with the stage height.
- **P4. At 1000x625 the panel hides the Still dark list behind one cycling Where? button (general).** The panel is
  half empty (`first-1000x625.png`), but a student can't pick the cluster they want: Where? walks through the dark
  clusters in turn. Show the two-column list in compact when it fits, or at least when the panel is 500 px or taller.
- **P5. The lantern moment is hidden under the sheet (family:careers).** A lantern lights while the career sheet's
  backdrop covers the stage, so its pop, and the allLit shimmer, play unseen (`d-sheet.png`, `all14`). The sheet's
  "lantern: lit" line is the only sign. Better: replay the pop (or the shimmer) on the lantern when the sheet closes.
  That is the moment a student looks up.
- **P6. "Stuck? Tap Where?." (general).** `src.html:1029-1030` doubles the punctuation in compact (`compact-card`
  hint). Drop the template's period when the label ends in "?".
- **P7. The trail stop header wraps at 1366 (general).** "BEHIND THE KETTLE CORN: STOP 5 OF / 5" puts the last "5"
  on its own line (`t-kettle-end.png`). Use the short "Stop 5 of 5" form in the wide panel too, or keep "5 of 5"
  together with a non-breaking space.

## Nits

- A marker's hover label shows cut off at the card edge ("e Ferris wheel", `d-card.png`). Hide labels while a card
  is open.
- The 56 px pan padding at both ends shows as a blank dark bar, and in Trails it is not dimmed with the rest
  (`first-1366x768.png` left edge, `t-kettle-end.png` right edge).
- At 375 wide, neighboring markers' 44 px targets overlap by 4 to 17 px (theater/help, food/first aid,
  clinic/bank). The dots themselves don't touch.
- In compact the count shows twice: "0 of 14 lit" on the stage and "Lanterns lit: 0 of 14" in the panel.

## What worked (checked, no finding)

- **First screen at every size:** names the action ("Tap anything glowing at the fair...") with glowing markers.
  Nothing takes focus on load, no sideways scroll, no console errors in any shot.
- **Every waiting moment names the next control:** card ("Tap a job... Press the ✕"), sheet ("Press Close, or
  Esc"), confirm, Where? ("Tap its circled marker"; "Still the Ferris wheel: it's the only place..."), List, each
  trail step ("Tap Next for stop 2, or tap Open career to meet the Farmer or Rancher"), Clusters and the ladder.
- **A student who skips the reading:** tapping only markers lights nothing. After the first card the hint switches
  to "tap a job to light its lantern", so the rule teaches itself.
- **Where?:** cycles hotspots and never repeats one twice running (Health x3, Arts x5). Manufacturing, which has a
  single hotspot, says so instead of pretending to move.
- **Start over:** asks first, puts focus on No, Yes clears, and focus goes to List.
- **Saving:** lanterns survive a reload. All 14 lit shows "Every lantern is lit" with a fitting hint
  (`all14-reload.png`). The privacy line is on screen.
- **Trails:** step in order with counts 4, 3, 2, 2, 3. Markers are numbered ("3-5" for a shared hotspot), the path
  is dotted, and the end row lists the clusters. Next with no trail picked starts Kettle corn, which matches the hint.
- **Clusters:** the grid shows counts. The ladder has 5 columns at 1280 and wider and rows below 900 px, pay bars on
  one $0 to $250,000 scale, "None in this tool" for empty levels, and "Ways in at N of 5 levels" in the panel, so
  the result is visible without scrolling. See it jumps to Festival and opens the card. All clusters returns focus
  to the cluster.
- **Keyboard:** Tab goes header, panel, then markers left to right. Enter opens, Esc closes the sheet then the
  card, and focus returns to the marker. Arrow keys pan.
- **Drag pans** (jittered real drag, pan -56 to 406). The minimap follows.
- **Motion off:** no running loops, the Where? ring is static, pans jump (`calm-card`; the audit agrees).
- **Sound off:** uses nothing up. Sound on brings the skipped welcome once (`sound-off`).
- **Read:** during the welcome, stops it and speaks the current hint (`read-mid`).

## Voice counts (held clicks)

| line | kind | expected | spoken |
|---|---|---|---|
| welcomeFestival | how | once, on the first tap | 1 per page (every run) |
| welcomeTrails / welcomeClusters | how | once per mode entry | 1 (`t-enter`, `c-grid`) |
| panHow | how | once, then silent | 1 spoken, then silent x3 over 5 hotspots (`d-5hot`) |
| lanternHow | how | once, on the first lantern | spoken in slow runs; dropped `newer` in 3 fast runs (S4) |
| trailEnd2 | event | every arrival | 3 of 3 (`t-end-repeat`) |
| trailEnd3 / trailEnd4 | event | every arrival, dropped when stale | spoken (`t-bridge-end`, `t-kettle-end`); dropped `stale` on a trail switch and a mode switch (`t-stale`, `t-stale2`) |
| allLit | event | when the 14th lights | 1 of 2 runs; missing when lit during the welcome (S1) |

## Frames looked at

- **First screens:** `first-680x425`, `-800x500`, `-1000x625`, `-1280x720`, `-1366x768`, `-1920x1080`,
  `-760x1000`.
- **375 wide:** `n375-first`, `-card`, `-sheet`, `-trails`, `-trails-pick`, `-clusters`, `-ladder`, `-list`
  (montages `m375a`, `m375b`).
- **Festival at 1366:** `d-card`, `d-sheet`, `d-close`, `d-close2`, `d-5hot`.
- **Where?, List and Start over:** `w-mfg1`, `w-mfg2`, `w-health3`, `w-trans`, `w-5x`, `w-then-tap`, `list`,
  `list-new`, `startover`, `startover-yes`.
- **Trails:** `t-enter`, `t-nexttrail`, `t-kettle-end`, `t-end-repeat`, `t-stale`, `t-stale2`, `t-open`,
  `t-bridge-end`, `t-lights-end`, `t-ticket-mid`, `tr-end-*` (5 sizes).
- **Clusters:** `c-grid`, `c-health`, `c-arts`, `c-digital`, `c-see`, `c-open`, `c-back`, `c-health-1280`,
  `c-health-1000`, `c-grid-680`, `c-health-680`, `c-grid-1920`, `c-arts-1920`.
- **All 14 lit:** `lit13`, `all14`, `all14-reload`, `all14b`, `all14-mid`.
- **Motion, Sound, Read, keyboard and drag:** `calm-card`, `sound-off`, `read-mid`, `keys`, `keys-enter-esc`,
  `arrow`, `drag`.
- **Compact and edge taps:** `compact-where`, `compact-card`, `edge-*`.

## Audit pilot

**Confirmed:** at 760x900 and 375, the Where? buttons are below the fold (polish here, P4 and P1 nearby). At 375,
neighboring markers' targets overlap by a few px (nit). Motion off is clean.

**Wrong:**
- Every marker/panel overlap at 680 to 1920 (about 60 rows). Those markers sit past the town's clipped edge
  (`overflow:hidden`), so they can't be seen or hit.
- "Focus lost" on restrooms, firstaid, radio and sponsor at 1366. Those markers are off-screen behind the panel;
  the click landed on the panel.

**Partly wrong:** it marked help, food and field "ok". My held click on `#mk-food` opened no card. The audit checks
focus and movement, not whether the click did anything.

**Missed:**
- the edge-tap blocker (B1);
- allLit lost during the welcome (S1, past one click);
- focus lost at a trail's end (S2, past one click);
- clipped names in Clusters at 375 (S3, a mode the size pass doesn't open);
- lanternHow dropped as `newer` (S4);
- the ladder and the trail result needing a scroll (P1, P2);
- all feel items.
