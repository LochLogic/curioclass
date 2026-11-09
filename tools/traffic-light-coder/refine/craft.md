# Craft lens: traffic-light-coder (round 1)

Cold Craft lens on the built bundle `tools/traffic-light-coder/traffic-light-coder.html` (not re-bundled). Grade 3
lesson tool, not a Curiosity. My frames and logs: `S:/CurioClass-codex-scratch/traffic-light-coder/craft/` (v1, v2,
v3 folders; drive.py with held clicks, port 9851). Shared audit: `S:/CurioClass-codex-scratch/traffic-light-coder/audit-r1/`.

## Contract (clean)

- One file, 443 KB (well under the 2 MB goal). The only URL in the bundle is the SVG namespace; no network requests.
- No console errors or exceptions in any of my 21 driven shots (voice runs, five-test loops, keyboard runs, Motion off,
  picker at three sizes) or in the audit.
- Kit used, not re-implemented: `Robot.program`, `Robot.strip`, `Robot.run` (style rules), `Curio.voice`. Skip to
  report re-runs the check loop by hand (src.html:1173-1184) but in the same order as the kit runner (check, fire,
  then tick; kit/robot.js:117-131), so a skipped test and a watched one give the same report.
- Frame times while a walk cycle plays at 1366x768: 400 frames, median 16.7 ms, p95 16.7, max 16.8
  (`v2` frametimes shot).
- Every `art:` token (12) has a prompts.json entry; the three walkers carry `"people": true`. Cory's people review
  of the three overhead children is still owed (BASELINE rule 11), not a lens finding.
- Words: no em dashes in src.html, notes.md, lines.json or the bundle; "Curio Class" everywhere; classroom-safe.
- `voice/lines.json` and the tool's line table `L` match word for word (16 of 16, checked by script); `allLines` is
  exposed on `__tool`.

## Findings

1. **should fix, general.** src.html:1288-1290 and 1443-1455. The `chip` how line ("Tap a chip in a rule to change it.
   Press Add rule to write a new one.") plays right after the student presses Add rule, so the first thing they
   hear after pressing Add rule is "Press Add rule". It also plays with the picker modal open, where Add rule sits
   inert behind the backdrop, so it names a control that cannot be pressed at that moment (STANDARDS: no line
   names a control that is off). Seen: `v1` v-add-first (first tap on Add rule, log `chip spoken`, focus on Done in
   the open picker); audit "one held click" row 10 shows the same. Better: a line for the open picker that names
   what is in front of the student ("Pick a chip, then press Done."), and the Add rule half kept for the hint after
   Done.

2. **should fix, general.** src.html:275-295 and 1297-1300. The chip picker hides the rule it edits. At 1366x768 the
   centred dialog covers the left of the rule list, including rule 1's light chip; at 680x425 it covers every rule.
   The slot tabs read only "If light / and... / and... / then...", never the current values, so the student
   changes one slot of a sentence they can no longer see (a grade 3 student editing "and..." cannot tell which
   condition is already set without opening each tab). Seen: `audit-r1/state-chip-picker-1366x768.png`,
   `craft/v2/picker-680.png`, `craft/v2/picker-action-1366.png`. Better: put the live sentence at the top of the
   dialog (or the current value inside each tab: "If GREEN", "and button pressed", "and +", "then turn YELLOW"),
   or place the dialog over the street so the card stays visible.

3. **should fix, general.** src.html:155-163 (push buttons fixed at 60 px) at 680x425 and 375 wide. In the preview
   sizes the street is about 100 px tall, and the two 60 px PUSH TO WALK buttons sit on the road: the south button
   hides the east-lane car stopped at the red stop line and the east signal dot, the north one covers the west-lane
   stop line. The moment the tool exists to show (cars stopped at red while a walker crosses) is half hidden there.
   Seen: `craft/v2/red-stop-680.png` (zoom: `craft/v2/zoom-red-680.png`), `audit-r1/size-375x812 (iframe host).png`;
   1366x768 is fine (`craft/v2/red-stop-1366.png`). Better: move the buttons onto the sidewalks clear of the stop
   lines (each curb's far end), or shrink them with the street while keeping a 44 px hit area.

4. **should fix, general.** src.html:393-411 and 473-487, 760x900 (and 375 wide). The stacked layout puts the rule
   list, the card buttons and Add rule below the fold in Street Jobs: the main controls a student edits every few
   seconds need a page scroll (STANDARDS, Sizes: main controls visible without scrolling at every size). Audit
   lead confirmed on `audit-r1/state-mode-street-jobs-760x900.png` (rule 3 and Add rule out of view) and the
   job-report, replay, rush-hour and ambulance rows at 760x900. Better: at 760x900 keep stage and panel side by
   side with the compact panel (as the short-landscape layout already does), or shrink the stage so the rule list
   starts above the fold.

5. **polish, general.** src.html:218-221 (rule-line 12 px, `.word` and `.chip` 11 px). On the main size, 1366x768,
   the rule sentences a grade 3 student reads all lesson are 11 to 12 px, while each card is 70 px tall and about
   a third empty. Seen: `audit-r1/size-1366x768.png`. Better: 14 px chips and words at 1280x720 and up (the 1600 px
   rule already goes to 14 to 15 px).

6. **polish, general.** src.html:1307-1310. Picker options for GREEN, YELLOW, RED and the three "turn" actions all
   use the same plain black dot icon, so the 60 px rows look alike. Seen: `audit-r1/state-chip-picker-1366x768.png`,
   `craft/v2/picker-action-1366.png`. Better: the dot in the lamp color (the word stays, so color is not the only
   signal), and a small arrow or lamp for the "turn" actions.

7. **polish, general.** src.html:595 and 1147-1160. When a test plays to its end (not skipped), the report opens with
   no announcement and focus stays on Run test; the report is marked `role="dialog"` but is not modal and takes no
   focus, and `#hint` is not a live region. A keyboard or screen-reader user gets no sign the result arrived.
   Seen: code read plus `craft/v3` (focus log). Better: focus the report heading (preventScroll) on every finish,
   or make the hint `aria-live="polite"`; drop `role="dialog"` or make it behave like one.

8. **nit, general.** src.html:1101-1103. The fire ribbon tells which light each rule set by a colored dot only (the
   number gives the rule, the tooltip the action, neither on screen). Better: a letter G/Y/R or the trace bar's
   stripe and underline patterns on the dot.

9. **nit, general.** src.html:1443-1447 with 935. Line 16 ("Six rules is the most. Change a rule instead.") can never
   play: Add rule is disabled at six rules, so its click handler never runs. The hint already says it. Drop the line
   from `L` and lines.json so it is not recorded for nothing, or say it from the disabled state another way.

10. **nit, general.** src.html:1405-1414. Reset street in Watch the Street hushes the welcome mid-sentence (marked
    said) and drops the queued "press" how line without queuing it again. The hint still shows the press step, so
    nothing is lost; noted only because it is the one place a mode's how line is lost without a first tap.
    Seen: `craft/v2` stale-fast log.

11. **nit, general.** src.html:195. At 680x425 the job card's grey tab (`.job-card::before`) pokes out above the
    report card's top edge. Seen: `audit-r1/state-job-report-680x425.png`.

## Standard voice check

Sound on, Motion on, held clicks (0.12 s), gaps longer than the lines. Logs in `craft/v1` and `craft/v2` drive output.

| line | kind | action, five times | expected | spoken |
|---|---|---|---|---|
| chip | how | open a rule card, Done (x5, 4 s apart) | 1 | 1 |
| report | how | Job 3: Run test, Skip (x5, 7 s apart) | 1 | 1 |
| unsafe | event | Job 3: Run test, Skip (x5) | 5 | 5 |
| miss | event | Job 1: Run test, Skip (x5, 6 s apart) | 5 | 5 |
| w-jobs | how (welcome) | enter Street Jobs | 1 | 1 |
| job1 brief | how | Run test pressed while it was queued | dropped, said again later | dropped (hush), not marked said |
| w-watch / press | how | push buttons x5, 2.5 s apart | 0 (stale on first push) | 0 |

- Stale lines: fast taps 0.2 s apart (Street Jobs, job 2, job 4, Run test, Skip, Watch the Street, Reset street):
  every line was cut by the next action's hush or dropped unplayed; none played after its moment.
- First tap: the stage gets the welcome about 0.2 s after the tap; Sound says nothing; Tab then Enter gets the
  welcome; Read speaks the hint only (audit row 4); a push button or rule card skips the welcome (rule 16; the
  premise "first rule that fits wins" stays on screen in the panel foot and the ribbon header).
- Read: Read during w-jobs cut it and spoke the hint; Read with Sound off spoke the hint.
- Order: spoken lines followed the actions in every run; no older line after a newer one.
- Every spoken line matched the screen at its time except finding 1.

## Access (clean apart from findings 2, 7, 8)

- Keyboard: Tab order (Street Jobs) is header, Run test, Speed, Start over, rule cards, Add rule, job dots 1-5, as the
  spec asks; every stop showed a 3 px focus outline (`craft/v2` kb-order-jobs). Enter on Add rule opens the picker
  with focus on Done; Tab reaches slot tabs then chips; Escape returns focus to the card; plain ArrowDown on a card
  moves focus, not the rule (`craft/v3`).
- Targets: every control is 44 px or more; picker rows 60 px; push buttons 60 px (audit, all sizes clean).
- Motion off: transitions and blinking stop, timing unchanged (audit "Motion off" clean, `craft/v2/calm-walk.png`).

## Audit pilot

- Leads confirmed: 760x900 rule list and Add rule below the fold (finding 4); the welcome is not heard after a first
  tap on a rule card, Add rule, a push button or Send walker (true, and allowed by rule 16; the premise stays on
  screen, so not reported).
- Leads wrong or not worth a finding: the 375x812 below-the-fold rows are a stacked phone page, which the spec allows;
  "keep region #strip x% inside the window" at 375 and 760 is the same stacking as finding 4; six-rules "choices cut
  short" is the scrolling the spec permits over four rules.
- Missed by the audit: the chip line naming Add rule right after Add rule and behind a modal (1); the picker hiding the
  rule it edits (2); push buttons covering the stopped cars at preview sizes (3); small rule text at 1366x768 (5);
  look-alike picker icons (6); no announcement when a played test ends (7); the dead six-rules line (9).
- Nothing cultural, Native or hard-history here; no sensitivity review needed. The three walker images still need
  Cory's people review.
