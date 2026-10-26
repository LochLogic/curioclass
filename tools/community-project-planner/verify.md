# Verify: community-project-planner

**Verdict: FIX** (no blockers; 4 should-fix, 8 nits)

Checked cold on 2026-10-26 against the draft bundle (community-project-planner.html, built 03:26 from src.html 03:24; art still
draft stand-ins, no voice clips yet, both expected). Muted headless Chrome over CDP on private ports, real held clicks and keys.

## What holds (checked, not assumed)

- **Model (Done when 1, 2, 3, 5):** I wrote my own Python model from spec.md only (points, match, band factor, Push, Planning
  meeting, heat wave, Ask cut, need changes, locks, supplies, money, stepping back, repeat halving, tiers) and replayed 672
  plans through the tool's `replay()`: the careful and two naive policies under all 8 event combinations for all 3 projects,
  plus 600 random plans (random assignments, leads, buys, events). Every week's energy, money, progress, per-volunteer points,
  gains, half flag and Ask cut matched, and every outcome matched. 0 mismatches.
- **Careful path:** strong skills, rest people who start a week Tired, Check in week 1, then Thank and Ask for ideas in turn
  gives every core task Done and the top tier in all 3 projects under all 8 event choices.
- **Naive path (everyone on one task, Push every week):** someone reaches 0 at the end of week 4, so they are Stepping back in
  weeks 5 and 6. That holds in all 3 projects, whether the one task is the first open core task or Fundraise. The one
  exception is the Coat Drive with "Take the week off" in week 4: either nobody reaches 0, or they reach it only at the end of
  week 6. notes.md says so.
- **Judging the builder's reading of "by week 4":** it's right. Using the spec's own numbers, the fastest drain is -24 a week
  (an "other" skill -14, Push -10). From 80 that reaches 0 only at the end of week 4. Being Stepping back *during* week 4
  would need -27 a week, which the spec's numbers can't produce, and needs tuning can't change energy. So "reaches 0 by the
  end of week 4" is the only reading the spec allows, and notes.md words it accurately.
- **Hand-checked weeks:** Map with Mei (4 h strong, 8), Dana (6 h okay, 9) and Tariq (5 h other, 5) is 22, capped at 20. The
  preview shows "+20 (1 extra hour wasted)" and the summary shows "Done". A Tired Tariq on an other-skill task gets
  round(5 x 1 x 0.75) = 4 in my model, and the tool logged 3. Tariq started that week at 10, Running on empty, so the
  factor is 0.5, round(2.5) = 3. That's correct. Energy lines read right, for example "Grace +20 rested; +13 checked in".
- **Events:** I tested each one directly. Lumber +$40: if not bought yet the price becomes $280; if bought, $40 comes off at
  once. Map Done then Re-map: reopened at 20 / 30, and Cleanup stays locked. Send Luis with Sign-up Done: a $30 donation;
  without it, the need drops 15 but never below progress. Sort need +10 reopens a Done task at 45 / 55. Take the week off:
  no task can be taken. The fair-rule option uses up the lead move and gives Mei and Luis +6. "Buy more ($40)" at $30 shows
  "Not enough money", is aria-disabled, and clicking it does nothing ("Not enough money for that one."). Short buy buttons
  read "need $N more" and are disabled.
- **Done when 4, 5:** "Cares about" reads "?" until the first Check in, then stays. Doing Thank twice in a row halves the
  bonus, and the summary line "lands a little softer" appears. A volunteer at 0 is greyed for two weeks, with the select
  disabled and the label "Stepping back, back in 2 weeks", then returns at 40. All five bands show a word and a distinct
  glyph.
- **Done when 6, 7:** localStorage is empty on load (after clearing) and stays empty while typing. Save writes only
  `curio-community-project-planner-plan`. After a reload: "Loaded your saved plan." Clear asks first (focus goes to "Keep
  it"), then empties the form and removes the key. The over-budget, week-crowding, empty-last-week and keep-going notes appear
  only when true. Run a Project has 0 text inputs.
- **Done when 8:** task cards, lead moves and Run week are fully visible with no scroll at 1366x768, 1280x720, 800x500,
  1000x625, 1920x1080 and 760x900. There's no horizontal scroll at any size, including 375 (iframe host). Keys work: 1 to 6
  then Q W E A S D, F, R, L, Enter and Escape (I checked that a supply-locked task refuses an assignment). Event cards trap
  Tab and Shift+Tab and ignore Escape. The Start over card takes Escape and returns focus to Restart. Focus never fell to
  body inside the tool. The focus ring is 4 px white on a dark ground.
- **Done when 9 (voice, held clicks):** if the first tap is picking a project, the intro plays and the welcome is skipped
  unmarked. If the first tap is Motion, the welcome plays. If the first tap is Read, only Read plays. A pick during Read
  stops it and plays the intro. With Sound off nothing plays; turning it back on queues the welcome. A mode switch hushes
  speech. allLines() matches voice/lines.json exactly (15 lines).
- **Done when 10:** no em or en dashes in src.html, notes.md, tool.draft.json, lines.json or prompts.json. "Curio" alone
  appears only as the kit's JS identifier.
- **Print:** I sent three outputs to a Letter PDF and each is exactly one page: Print plan (coat example plus 2 extra rows, 8
  tasks), Print report, and a mid-game board print. All are dark on white with timeline patterns kept.
- **Motion:** the Fired up bob runs with Motion on. With Motion off, animation-name is none and `curio-motion=calm` is
  stored.
- **Contract:** one file, 118 KB, no external src, href or link, and the tool makes no network requests. The only console
  entry was a 404 for my own test server's favicon.
- **Sources:**
  - CASEL: all four phrases match casel.org word for word.
  - SSIR: Eisner, Grimm, Maynard and Washburn, "The New Volunteer Workforce", SSIR Winter 2009. The article lists "Not
    Matching Volunteers' Skills with Assignments" and "Failing to Recognize Volunteers' Contributions" among its five
    reasons volunteers don't return. It says nothing about check-ins.
  - notes.md and tool.draft.json cite it only for skill matching and recognition. notes.md also says Check in is the tool's
    own addition, and no numbers from the article appear on screen. That is the honest way to keep it.
- **Spec deviations (judged):**
  - River Re-map: the spec's play path ("Cleanup weeks 2 to 3") can't happen as written. Either week-2 option blocks Cleanup
    in week 2: A reopens Map, which re-locks Cleanup, and B pauses Cleanup. Moving Cleanup to weeks 3 and 4 is the right fix,
    and core work still ends in week 5. Accept.
  - Three columns at 420 px stage width and up: this is what lets the board fit at 800x500 and 1000x625. Accept, apart from
    a wrapping nit at 760 (see N3).
- **SEL rules:** everything is fictional and ordinary. Run a Project has no text box. Plan Your Own asks for roles, not names.
  Nothing is stored before Save. No score is put on feelings (energy belongs to made-up volunteers). Celebration is minimal.
  notes.md sends an upset student to the school counselor. The copy reads right for grades 9-12.

## Should fix

**S1. Stepping back card text fails contrast.** Where: `.vol.back{opacity:.62}` (src.html:183) with the band word in
`--b-back #8d97a5`.
- Repro: run a volunteer to 0, start the next week (frame: shots/stepping-back).
- The opacity lowers text and card alike. "Stepping back, back in 2 weeks" works out to about 2.7:1 and "Cares: Having a
  say" about 3.5:1 (I computed both with the opacity blended). Both are under AA 4.5:1, and this is the state the spec most
  wants shown kindly.
- Fix: drop the card-wide opacity. Grey only the face and the energy bar (or use a dashed card border), and keep the text at
  full ink or muted (6.8:1).

**S2. Targets under 44 px.**
- Plan Your Own week toggles W1 to W6 are 40 x 44 at every size (`.trow .wbtns .btn{min-width:40px}`).
- Supply buttons (`.task .buy{min-height:40px}`) are 40 px tall at 1280 and up.
- In short compact boxes (680x425, 800x500, 1000x625): volunteer pick buttons are 31 px, "Working on" selects 32 px,
  Fundraise 32 px, buy buttons 34 px and "Lead this project" 40 px.
- Fix: make the toggles and buy buttons min 44 (the toggle row has room; 6 x 44 + gaps fits the 254 px column). For the
  short preview, 36 px or more would be a fair compromise. It's the embed, but it's where a teacher first clicks.

**S3. 680x425: the team row is below the fold.** The stage scrolls 486 / 371 px, so the volunteer selects sit 70 to 100 px
under the bottom edge and the picks are cut off (frame: shots/board-680x425). The builder flagged it. STANDARDS asks for the
main controls without scrolling at every size, and picking a volunteer happens every week. Keys 1 to 6 still work. Fix
ideas, any one:
- At short compact, fold Fundraise into a 7th task card or a slim chip, which saves about 40 px.
- Drop the task progress bar at short compact (the numbers already say it).
- Hide the "Working on" selects at short compact, since the pick buttons and the task cards do the same job.

**S4. 375 wide (phone): Run week is about 1580 px down the page.** In stack layout the whole panel (lead moves, Run week)
comes after the six task cards and six volunteer cards, so every week means a long scroll down and back (frame:
shots/375-board-full). It works, but it's clumsy. Fix: in stack, make the run row (lead summary plus Run week) a sticky bar
at the bottom, or put the lead moves and Run week right after the team row inside the stage.

## Nits

**N1. Plan Your Own timeline at 375 is tiny.** `drawTimeline` uses a minimum W of 480 and the SVG scales to about 343 px, so
task names come out about 9 px and skill labels about 8 px (frame: shots/375-plan-full). Fix: let W follow the host width
below 480 and drop the skill label column when narrow.

**N2. Plan Your Own hint says "Watch the budget on the right."** At 375 the budget is below the form. That's minor, and it's
a recorded line, so only change it if you re-record (for example "Watch the budget as you go").

**N3. 760x900, three columns: the skill word "HANDS-ON" wraps to two lines beside the CORE tag.** The Design bonus card's
pencil icon is also squeezed (frame: shots/board-760x900). Fix: hide `.skw` when a card is under about 150 px (the icon and
stripe still carry the skill), or let `.tag` shrink.

**N4. Coming back to Run a Project mid-project plays the Run welcome ("...Pick one.").** It wasn't said yet because the first
tap was a pick, and now it plays while the board is showing. The same happens when Sound comes back on during a project.
That's within STANDARDS' letter, but it's out of moment. Fix: give the run welcome an ok() of `state.screen === 'picker'`,
or mark it said once a project is picked.

**N5. Print with "Background graphics" on gives the page margins the dark theme background.** It's visible in the PDF
margins. Fix: add `html{background:#fff}` to the print block.

**N6. The careful path is very forgiving.** In every project the careful policy ends with the whole team near 100 energy,
and resting barely comes up, so the "let them rest" idea mostly shows up only on the hard path. This isn't against any
Done-when item; it's for Cory or a later tuning pass to decide. Raising a few needs by 5 to 10 would make rest weeks matter
on the good path too.

**N7. The Coat Drive naive exception.** "Take the week off" in week 4 lets naive play avoid Stepping back entirely. The spec
asked for the naive claim to hold in all three projects. It's documented in notes.md; flagging it as a spec-owner
decision, not a build bug.

**N8. Panel on the report screen holds only the hint line.** Lots of empty space at 1366 (frame: shots/report-coats). It
could repeat "Try it again" and "Print report" there, or show the core-done facts.

Scratch (my model, plans, frames, PDFs):
C:\Users\Cory\AppData\Local\Temp\claude\S--\02b04f0c-dbb4-4764-bf27-ccc7483387d1\scratchpad\cpp-verify

## Re-verify

**Verdict: FIX** (no blockers; 2 should-fix, 5 nits)

Checked cold on 2026-10-26 against a fresh draft bundle (`CURIO_DRAFT=1`, 652 KB, under 2 MB; real FLUX banners, 15 real
clips including the re-recorded h-plan). My own muted headless Chrome (Start-Process, private ports), real held clicks and
keys, my own Python model of the spec. Scratch:
C:\Users\Cory\AppData\Local\Temp\claude\S--\02b04f0c-dbb4-4764-bf27-ccc7483387d1\scratchpad\cpp-rv

### Earlier items

- **S1 fixed.** The Stepping back card has no card-wide opacity now (dashed border; only face and bar at .45). All card
  text renders at opacity 1: band word #8d97a5 on #202a38 is 4.90:1, muted 6.81:1, name 12.31:1.
- **S2 fixed, and 36 px in the short preview is acceptable.** Week toggles and buy buttons are 44 px at full size; nothing
  is under 44 at 1280x720, 1366x768, 1920x1080 or 760x900 (Plan Your Own checkboxes are 20 px but sit in 44 px labels). In
  short boxes (680x425, 800x500, 1000x625) picks, menus, buy buttons and Fundraise are 36 px; lead moves, Run week and the
  header stay 44. For a mouse-driven embed that a student can open full screen, 36 is a fair compromise.
- **S3 fixed.** 680x425 and 800x500: no stage scroll (371/371, 446/446); task cards, lead moves, Run week and all six picks
  are on screen. 1000x625 keeps the menus and banner and also fits.
- **S4 fixed.** 375x812 and 375x667 (iframe host): the lead moves and Run week sit in a sticky bottom bar at every scroll
  position (Run week bottom 804 of 812, 659 of 667). The bar hides on the summary, where Start week sits near the top, and
  goes inert under the event card. Lead moves scroll sideways in the bar; the pressed one is kept in view.
- **N1 fixed** (timeline viewBox follows the width; 13 px text at 375). **N2 fixed** (line and clip now "as you go").
  **N3 fixed** (skill word hidden on narrow cards at 760). **N4 fixed** (back to Run mid-project, or Sound back on, does
  not play the Run welcome). **N8 fixed** (report panel has the questions and a week-by-week list).
- **N5 not fixed.** See N-a below.
- N6, N7 left for Cory, as stated; both still stand as written.

### Do the compact cuts lose anything a student needs?

Mostly no. Under 520 px tall the volunteer menus, banner, task progress bars and the long words go. Each task card still
lists who is on it, the selected volunteer is highlighted, keys and clicks still assign, and the project name moves into
the panel. Two small losses, both nits (N-b, N-c): the volunteer card no longer says what that person is doing or that they
are resting, and the task card's one-line name list truncates when five or six people share a task.

### Regression sweep (holds)

- **Model:** my own Python model from spec.md, replayed through `replay()`: the careful and naive policies for all 3
  projects under all 8 event choices (48 plans) and 300 random plans. Energy, money, progress, per-volunteer points, gains,
  half flag, Ask cut, bands and outcome: 0 mismatches. Careful: top tier everywhere. Naive: someone at 0 by the end of week
  4 everywhere except the Coat Drive with "Take the week off" (N7). A full real-click careful game (Riverside, AAA, Clear
  assignments each week) ends with the same money ($110), energies and top tier as the model, at 680x425 and 1366x768.
- **Sizes:** all nine checked; no horizontal scroll anywhere; main controls in view at every size (phones via the bar).
- **Keyboard:** 1 to 6, Q W E A S D, F, R, L and Escape work; event cards trap Tab both ways and ignore Escape; the Start
  over card takes Escape and returns focus to Restart; focus ring 4 px white. Enter: see S-b.
- **Motion off:** `.bob` animation none, transitions instant, `curio-motion=calm` stored, button aria-pressed false.
- **Print:** Print plan (coat example plus 2 rows, 8 tasks), Print report and a mid-game board each print as one Letter
  page, dark on white, timeline patterns kept, with white margins at default settings.
- **Storage:** only `curio-motion` until Save; typing stores nothing; Save writes `curio-community-project-planner-plan`;
  reload says "Loaded your saved plan."; Clear asks (focus on Keep it) and removes the key. Run a Project has 0 text inputs.
  The four notes appear only when true.
- **Voice (held clicks; every clip a real recording, the browser voice never used):** pick first plays the intro and skips
  the welcome unmarked; Motion first plays the welcome; Read first plays only Read; a pick during Read plays the intro; a
  mode switch cuts the intro and plays the Plan welcome; Sound off is silent and turning it on queues the welcome; Read in
  Plan plays the new h-plan clip; the report tier line plays. allLines() equals lines.json (15 lines); every line has a clip.
- **Console:** no errors or exceptions in any shot (only my test server's favicon 404). No network references in the file.
- **Copy:** no em or en dashes in src.html, notes.md, tool.draft.json, lines.json, prompts.json or the bundle; "Curio"
  alone only as the kit's JS identifier.
- **Art:** the three FLUX banners (river trail, brick library lot, coat racks) show no people, figures, animals or
  lettering.

### Should fix

**S-a. 680x425: text spills and overlaps in the new compact layout.** Where: the `body.tiny` team row and the run row.
- The volunteer pick content is 76 px wide in a 54 px button: the hours ("6 h") hang about 16 px past each card's right
  edge into the gap and the next card, and "Dana", "Tariq", "Grace" are clipped (name 30 px in 24 px).
- "Clear assignments" (96 px of text in an 86 px button) runs under the Run week button.
- Seen in frame shots1/board-680x425 and an overflow scan (scrollWidth over clientWidth). 800x500 is just inside.
- Fix: in tiny, drop the hours from the pick row (or put them under the name) and let the name ellipsize; label the button
  "Clear" or let it wrap inside its box.

**S-b. Enter does not run the week in the normal keyboard flow.** Where: src.html:1177 (`k === 'Enter' && tag !== 'BUTTON'`)
together with src.html:1185 (`VC[vid].pick.focus()` after each key assignment).
- After "1, Q" focus is on Dana's pick button, so Enter re-selects Dana instead of running (checked: screen stays board,
  sel = dana). After a mouse click on a card, focus is on that card, so Enter does the same. Enter runs only when nothing
  is focused, yet the panel says "Enter runs the week."
- Fix: let Enter run the week when focus is on a volunteer pick or a task card (anything except the other panel buttons and
  the overlay), or stop moving focus onto the pick button after a key assignment.

### Nits

**N-a. (was N5) Print with Background graphics on still has dark margins.** html is white in print, but the theme's
`color-scheme:dark` makes Chrome paint the page margins #121212 (print/plan-bg, print/report-bg). Fix:
`:root{color-scheme:light}` in the print block.

**N-b. Tiny mode: the volunteer card no longer shows the assignment.** With the menus gone, nothing on a card says "on
Map" or "Resting"; you read it off the task cards. Fix idea: a one-line label where the menu was (it fits; see N-d).

**N-c. Tiny mode: the task card's name list truncates with 5 or more on one task.** "Dana, Luis, Mei, Tariq, Gr..." at
680 (5 or 6 people), and with 6 at 800. That is the naive play the tool wants students to try. Fix: allow two lines for
`.who` in tiny, or show "6 people" with the names in the aria-label.

**N-d. 800x500 hides more than it needs to.** In tiny the team row ends at 342 of 500 px (158 px spare), and at 680x425 at
342 of 425 (83 px spare), so the menus (about 40 px) would fit at both, and the banner too at 800x500.

**N-e. Summary line "+0 Map the trash hot spots Done (4 extra hours wasted)".** When Ask for ideas' 8-point cut finishes
a task that also had people on it, the summary shows +0 with wasted hours; the "(the team's idea finished it)" wording only
appears when nobody worked it. The numbers are right (they match the model); the wording could credit the idea (frame
shots13/rc-sum3-680).

## Re-verify 2

**Verdict: FIX** (no blockers; 2 should-fix, 3 nits)

Checked cold on 2026-10-26 against a fresh draft bundle (`CURIO_DRAFT=1`, 654 KB). My own muted headless Chrome
(Start-Process, own profile, ports 9691 and 8997), real held clicks and keys. Scratch:
C:\Users\Cory\AppData\Local\Temp\claude\S--\02b04f0c-dbb4-4764-bf27-ccc7483387d1\scratchpad\cpp-rv2

### The builder's claims

- **S-a fixed at the listed sizes.** At 680x425 and 800x500 no volunteer card content spills (0 px on all six), the name
  line and the icons and hours line fit in 62 px (79 px at 800) picks, and the button reads "Clear" (aria-label keeps
  "Clear assignments"). But see S2-1: the same spill is still there in narrow boxes 520 px and taller.
- **S-b fixed.** Enter runs the week after a project picked by a real click (tool focus on Dana), after "1, Q" or "2, W"
  (hotkeys, also at 680x425), after mouse clicks on a volunteer and a task card, and after clicking Clear (focus moves to
  Run week). On a card or lead move reached with Tab, Enter does that control's job (lead set, no run); Shift+Tab back to
  a clicked card counts as Tab-reached. Event cards still take Enter on their option.
- **N-a fixed.** Print plan (coat example plus 2 rows), Print report and a mid-game board each print as one Letter page;
  with Background graphics on, all four corners are white (#fff) and the pages match the plain prints.
- **N-b fixed.** Tiny cards show a "doing" line: the task name with a skill-colored edge, or "Resting" in italic muted
  (also on a Stepping back card). One line, ellipsized, under 470 px tall; two lines from 470.
- **N-c fixed.** Four or more on one task read "Dana, Luis +2" / "Mei, Dana +4" in tiny boxes; nothing truncates at 680 or
  800; the full list stays in the aria-label.
- **N-d fixed.** From 470 px tall the banner and the task progress bars are back (680x470, 700x480, 760x500, 800x500,
  800x519, 999x519); at 680x469 they hide again. The board fits with no stage scroll at every one of those.
- **N-e fixed.** When the idea's cut finishes a task that also had people on it, the summary reads "Map the trash hot
  spots Done (the team's idea finished it, so the 4 hours on it had nothing left to do)" (frame shots13/rc-sum3-680).

### Regression sweep (holds)

- **Model:** the previous re-verify's plans replayed through `replay()`: 48 policy plans (careful and naive, 3 projects,
  8 event choices) and 300 random plans, 0 mismatches in energy, money, progress, points, gains, half flag, Ask cut, bands
  and outcome. The game numbers are unchanged.
- **Sizes:** 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 375x812, 375x667: no horizontal scroll,
  task cards, lead moves, Run week and picks in view (phones via the sticky bar, Run week bottom 804 of 812 and 659 of
  667).
- **Keyboard:** 1 to 6, Q W E A S D, F, R, L, Escape; event cards trap Tab both ways and ignore Escape; the Start over card
  takes Escape and returns focus to Restart; focus ring 4 px white; on phones the bar goes inert under the event card.
- **Motion off:** animation none, transitions instant, `curio-motion=calm`, aria-pressed false.
- **Storage:** only `curio-motion` until Save; Save writes the plan key; reload loads it; Clear asks and removes it.
- **Voice (held clicks):** pick first, Motion first, Read first, pick during Read, Plan Read, Sound off and on, mode
  switch, the report line and the N4 cases all behave as in the last re-verify. allLines() equals lines.json (15).
- **Console:** no errors or exceptions in any shot (only my server's favicon 404). No network references in the bundle.
- **Copy:** no em or en dashes in src.html, notes.md, tool.draft.json, lines.json, prompts.json or the bundle; "Curio"
  alone only as the kit's JS identifier.

### Is the Enter rule understandable?

Mostly yes, because students never have to learn the rule: mouse players click around the board and Enter runs, Tab
players get normal button behavior, and that split is the web's own convention. The one place it reads as broken is
S2-2: the lead move is usually the last thing a mouse player clicks before running, and Enter there does nothing.

### Should fix

**S2-1. The S-a spill is still there in narrow boxes 520 px and taller.** Where: src.html:1490, `tiny` turns on only when
`innerHeight < 520`, so the compact short layout from 520 to about 690 px tall uses the old pick row.
- Measured at 680, 720 and 760 wide by 520, 560, 600 and 640 tall: hours spill 16 / 10 / 6 px past each card into the next,
  names are clipped ("Dana", "Tariq", "Grace" at 680), "Clear assignments" overflows its button (88 in 86 px at 680 and
  720). At 680x520 the stage scrolls (500 / 466) and the menus end at 540, below the fold. 840 wide and up is clean.
- Why it matters: a browser snapped to half of a 1366x768 laptop is about 683 x 640 inside, which is this case (frame
  shotsG/g-680x640).
- Fix: switch to the tiny card layout by card width as well as height (for example when the team row is under about 560
  px wide, or `innerWidth < 800` in compact short), or base it on a container query on `.team`.

**S2-2. Enter after a mouse-clicked lead move does nothing.** Where: src.html:1203 (`CARD` covers only volunteer and task
cards) with src.html:1223.
- Repro: click Dana, click Map, click "Thank the team", press Enter: the screen stays on the board and the lead is
  re-set to Thank (frame shotsE/e-click-lead-enter). The panel says "Enter runs the week."
- Re-pressing the lead that is already on changes nothing, so running there loses nothing. Fix: add `[data-lead]` to
  `CARD` so a click-focused lead move runs on Enter, like the cards.

### Nits

**N2-a. Enter right after picking a volunteer runs the week with that person unassigned.** Click Dana (or press 1) then
Enter: the week runs and Dana rests (the selection is dropped). That is what the rule says, but a stray Enter mid-pick
spends a week. Optional: while a volunteer is picked and not yet placed, let Enter do nothing, or say "Dana is still
waiting for a task" first.

**N2-b. 680x425: the "Keys" line is cut off at the bottom of the panel,** so "Enter runs the week", the only on-screen
mention of Enter, is not visible in the smallest preview (frame shots2/ov-680x425). Fine to leave, or shorten the line in
tiny.

**N2-c. 680x425: the doing line keeps about 9 characters** ("Map the t", "Sign up c"). The skill-colored edge helps, and
800x500 shows two full lines. Acceptable for the preview.

N6 and N7 (careful path forgiving, Coat Drive naive exception) stay with Cory as before.

**Verdict: FIX** (S2-1, S2-2 should fix; N2-a to N2-c optional)

## Integrator fix (Re-verify 2 should-fix S2-1 and S2-2)

- S2-1: the tiny card layout now also turns on in short compact windows under 860 px wide (`innerHeight < 700 && innerWidth < 860`), not only under 520 px tall. Rechecked with the re-verify's own measurement script at 680x520, 680x600, 683x640, 720x560, 760x640, 800x600, 850x650 and 800x699 (tiny), 860x650 and 900x600 (not tiny), plus 680x425, 800x500, 1000x625, 1280x720 and 760x900: no card content spills, no pick button overflows, no stage scroll. Only the intended ellipses on task names remain. Banner and bars still show from 470 px tall.
- S2-2: lead move buttons are added to the Enter-runs set, so clicking a lead and pressing Enter runs the week (checked with a real held click and a real Enter key at 1280x720).
Nits left as they are.
