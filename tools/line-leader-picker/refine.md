OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 0 (general 0, family 0), should fix 12 (general 12, family 0), polish accepted 9
Traced to spec: blockers 0, should fix 6

# Refine: line-leader-picker

Lenses: refine/teaching.md, refine/play.md, refine/craft.md. Shared audit: S:/CurioClass-codex-scratch/line-leader-picker/audit-r1.
No sensitivity review needed (no cultural, Native or hard-history content; all three lenses agree).
Integrator spot-checked in src.html: check() order (1323-1342), recordSummary at month end (1239, 1355-1359),
choose() in the Which step state (1043-1049) and on a re-tap (1051-1069), friendTap beeSick (1253-1255), L.fSummary (617).
All four lens claims held.

## Blocker
None.

## Should fix
1. **Is It Fair?, check feedback plays after the next question and is then dropped.** src.html:1334-1340, `check()`.
   On a first answer the next question's how line is spoken `now:true`, then "The chart agrees." / "Look at the chart
   again." plus the evidence line is queued behind it; the next thumb tap (about 3.5 s later, a child answering the
   question just heard) drops it. Seen: play/out2/fair-A-flow vlog (all three feedback pairs dropped on rule A);
   craft/frames/v4-checkx5 (q1C dropped, "agree" heard after Q2's question); teaching shots2.json t-check-order.
   A pre-reader hears three questions and no answers, and "The chart agrees" lands on the wrong question. Fixed:
   feedback (agree/look + evidence) speaks first, the next question waits for it; a later thumb never drops feedback
   for an earlier check that has not started. Re-run the voice check on a three-answer chain at 3.5 s and 6 s. (general) (build)
2. **Is It Fair?, Our chart answers the checks before the child does.** src.html:1239, 1355-1370. `recordSummary()` runs
   at month end and fills Q1 to Q3 from the data, so opening Our chart right after a rule card shows Yes/Yes/Yes with
   every thumb untouched; Q1 (a rule fact the chart cannot show) is handed over outright. Toggling Bee also records a
   row for a rule nobody checked. Seen: teaching frames/t-summary-before-checks.png; play out2/fair-summary-after.
   Fixed: a cell shows "?" until that check is answered on that rule (then the data's yes/no, as now); a row appears
   only once its first check is answered. Spec said "yes / no icons from the data" with no timing. (general) (spec)
3. **Is It Fair?, a pre-reader cannot see a mismatch, or which verdict they picked.** src.html:1313-1319, CSS .verdict,
   247. The tapped thumb gets the same pressed ring whether it matches the data or not; the only sign is 12 px "× No"
   text, hidden at 680x425 and narrower. Fair / Not fair set aria-pressed but have no pressed style, so after a
   verdict nothing visible changes but the hint. Seen: play out2/fair-A-flow.png. Spec promises "evidence on the chart
   for each check" (rings on zero columns, tallest marked) for pre-readers. Fixed: after each check the chart evidence
   draws (zero rings for Q2, tallest marked plus rings for Q3, the rule card's step pictures highlighted for Q1) and a
   small picture yes/no mark shows by the chip at every size (not a right/wrong mark); verdict buttons get a clear
   pressed look. (general) (build)
4. **Is It Fair?, thumbs mean two things.** src.html:854-855, 861-862. Checks use thumbs up = yes, thumbs down = no;
   the verdict uses thumbs up = Fair. For rule A the matching answers are down, up, up ("yes, a friend was left out")
   beside a thumbs-up Fair button. A K-2 child reads thumbs up as "good", which blurs the line between the chart's
   facts and the child's own fairness call. Seen: teaching frames/t-bee-sick-B-checks.png. Fixed: the checks use
   yes / no pictures (a check mark and a cross, or a nodding and a shaking head, each with its word as the accessible
   name), thumbs stay only on the verdict; update fChecks ("Tap yes or no for each question.") and the q0 to q2 how
   lines to name the new pictures, in voice/lines.json too. (general) (spec)
5. **Is It Fair?, a Q1 mismatch says "Look at the chart again."** src.html:1340 (same agree/look choice for checks 0
   to 2). Q1 is the rule's own fact (spec, Check evidence); for rule C the chart shows 3 stickers beside 0, which
   supports the "no" a child just gave, so sending them back to the chart teaches the opposite of fSame. Fixed: a Q1
   mismatch gets its own line, "Think about the rule, not this month's stickers.", then the q1 rule line; add it to
   L, allLines() and voice/lines.json. (general) (spec)
6. **Is It Fair?, the Q2 evidence line names "that friend".** src.html:1329. Q2 with any zero speaks `left` ("That
   friend waited all month and never led. Being left out feels sad."), the classmate-tap line; no friend is selected
   and rule C usually has 5 to 10 at zero, rule A nineteen. Seen: craft/frames/f1-fair-full (evidence "9 left out"),
   teaching t-fair-C-all-thumbs log. Fixed: Q2 speaks the count line that already exists (`zeroOne` / `zeroN`, "Nine
   friends never got a turn.") then "Being left out feels sad." as its own clip; `left` stays for the classmate tap.
   The spec gave Q1 and Q3 evidence lines but none for Q2. (general) (spec)
7. **Change a Step, Which step: the old tile is called unchanged.** src.html:1043-1047. After "Which step made the
   month change?", tapping the Before tile in the changed slot ("Stays at the front") gets chSame, "That step stayed
   the same.", which is false. Seen: teaching t-which-old-tile log. The spec says the prompt accepts a changed
   *step*. Fixed: judge by slot: any tile in a changed slot gets chYes and the glow on the new tile; only a tile in
   an unchanged slot gets chSame. (general) (build)
8. **Change a Step and Make a Rule, re-tapping the chosen tile wipes the month and changes nothing.** src.html:1051-1069,
   `choose()`. The Change mode opens with "Stays at the front" pressed; tapping it (to hear it, or because it glows)
   turns Ant's 20 into Before outlines with `changed: []`, Run replays the same month and no compare line or Which
   step follows. In Make a Rule it silently clears a finished month. Seen: play out1/change-same-tile.png. Fixed: a
   tap on the tile already chosen only speaks its name (event line, every time); in Change a Step add "That step is
   the same. Tap the other picture to change it." once as a how line (in L, allLines(), lines.json); the month and
   Before are untouched. Spec said any tile tap changes the rule and clears the month. (general) (spec)
9. **Is It Fair? and classmate taps, Bee's sick line claims a cause it did not have.** src.html:1253-1255. With Bee
   sick, tapping Bee at 0 always adds beeSick before `left`, under every rule; under rule A (Ant 20, everyone 0) and
   often rule C, Bee's 0 has nothing to do with the sick day, and E2 is about telling the rule's effect from the
   situation's. Seen: teaching t-bee-sick-A log. Fixed: add beeSick only when the sick day changed Bee's count (Bee 0
   in the sick month and Bee would have led in the same month without the sick day; in practice rule B, and rule C
   only if the day-2 draw was Bee). Spec told the build to add it for any Bee 0 in a sick month. (general) (spec)
10. **Is It Fair?, New month (or re-tapping a card) erases the class's verdict.** src.html:1034, 1239, 1355-1358.
    clearMonth sets verdict null and recordSummary overwrites the row, so Our chart loses a call already made. Seen:
    teaching t-newmonth-wipes-call (C verdict false, then null). notes.md says Our chart keeps "the class's own calls
    for this page load". Fixed: the summary keeps the last verdict per rule row until a new verdict is given for that
    row; the checks on screen reset as now. Notes then stay true. (general) (build)
11. **Our chart, the line says "Tap Close" over a bare ×, and asks to pick before any rule has a row.** L.fSummary
    src.html:617, src.html:894. The spec line has no "Tap Close"; the build added it, and the button shows only "×".
    Opened before any rule is tried it asks "Which one would you pick for our class?" over a table of "?". Seen:
    audit-r1/state-summary-1366x768.png; play finding 4; craft finding 9. Fixed: "Tap the X to go back to the rule
    cards." (and give the × a visible "Close" label at 1366 and up), and speak fSummary only once at least two rows
    have a verdict; before that, a short how line "Check a rule card first. Its row fills in here." Update lines.json.
    (general) (build)
12. **Compact sizes, the gold stars shrink to 7 to 8 px specks.** src.html:229, 348. At 680x425, 800x500 and 375 wide
    the chart reads as faces plus numbers; a 2-star column is two dots in a corner, and Ant's 20 Before outlines
    become a hatched bar. Seen: craft/zoom-fairc-680.png (from audit-r1/state-fair-c-680x425.png),
    craft/zoom-changed-375.png. The chart is the focus of the tool and the 16:10 preview. Fixed: in the 10x2 and 5x4
    banks the star stack uses the cell width the count does not (or stars as short rows of at least 12 px), so each
    sticker reads; check 680x425, 800x500, 375x812. (general) (build)

## Polish accepted
1. **Step 2 tap: tile name first, then "Tap Run".** src.html:1074-1076. Now the how line plays `now` and the tile
   name after it (play out1/make-d-end, craft v2-step2x5). Speak the tile name first, then runReady / chRun queued.
   Keep Done when 9 (runReady once). (general)
2. **Q3 has one wording everywhere.** Chip (src.html:846) "Extra turns while a friend got none?", voice and hint
   "Did someone lead more than once while a friend got none?", Our chart column "Extra / none?" (527). Use the spoken
   question on the chip (wrapped) and the Q3 picture with a short "Led more, one none?" or the picture only in the
   summary header. (general)
3. **The name slip lands beside the jar, not over Week 1.** src.html:57 (.slip left 145 top 30) covers day squares 1-2
   for the whole month (play out1/make-d-day1.png, make-d-day8.png). Place it by the jar or the Leader spot, never over
   a calendar day. (general)
4. **Projector reading size.** At 1920x1080 rule card names stay 12 px, check questions 14 px, evidence 12 px
   (audit-r1/state-fair-c-1920x1080.png). Scale .rule-pick, .check h2, .evidence and .verdict button in the 1600 px
   media query. (general)
5. **Fair mode hint does not name the hidden Turn Machine.** src.html:1285 sets hint('machine') while the machine is
   hidden. Keep the current hint, or a fair line naming the rule card. (general)
6. **Bee's sick day shows on the chart.** src.html:984 shows Bee in bed only while exactly 2 days are done; in a
   finished sick month Bee's column looks like any other zero. Add a small bed mark on Bee's column (or Bee's class
   row cutout) whenever the sick switch is on. The spec already promises "Bee in bed on day 2". (general)
7. **The Who question comes back if closed unanswered.** src.html:1227-1233, 1274. Closing with × loses the only EK
   moment for the page load. Offer it again after the next finished month until answered. (general)
8. **Rule B's Q1 line answers Q1.** L.q1B (638) "Everyone gets a turn, one after another." is the turn-for-everyone
   idea fSame separates from same chance. Use "Every friend comes to the front in turn, so everyone has the same
   chance." in L and lines.json. (general)
9. **Cheap nits taken:** remove the unreachable lines tie11 to tie20, most1 and zero20 from L and voice/lines.json
   (craft finding 7, read from resultParts 1203-1211); add `title` tooltips to the icon-only Fair, Not fair, Our chart
   and New month buttons at short sizes (spec asked for them); make Run's top gradient stop dark enough for 4.5:1 with
   white 15 px bold text (now 4.40:1 at the top, src.html:124). (general)

## Settled calls
- Audit "overlap" rows at 375x812 (count over classmate button) are by design; "text under 10 px" rows on icon-only
  buttons are font-size 0 with names intact. Do not change (Play and Craft agree).
- "Welcome not heard" after a first tile or classmate tap, and a mode welcome cut by a quick second tap: BASELINE 16;
  the premise stays in the hint and Read. Do not change.
- "has not led yet" 4 of 5 at a 2 s pace is the newer tap dropping the older tap's tail, as the spec asks; 5 of 5 at 4 s.
- Q2 line wording: Teaching called it polish, Craft should fix. Settled should fix (item 6): the spoken line is false
  about the screen.
- Thumbs (item 4): settled from the spec's own aim (facts on the chart, verdict the child's) and BASELINE 2; the checks
  change pictures, nothing about what is taught. Verdict stays thumbs plus the cross on Not fair.
- Our chart (item 2): it still shows the data's yes/no once answered; it never shows right/wrong marks for answers and
  never marks the verdict (E2 Done when).
- No score, points or right/wrong marks anywhere in Is It Fair?; the picture yes/no by a chip (item 3) shows the
  chart's fact, not whether the child was right.
- Contract, keyboard, focus, 60 px targets, Motion off pacing, lines table vs lines.json, art tokens: clean (Craft). Leave.

## To the spec's open questions
- None for Cory. For the spec owner: spec.md should be updated to match items 2, 4, 5, 6, 8 and 9 (summary fills from
  answers, yes/no check pictures, Q1 mismatch line, Q2 count line, re-tap of the chosen tile, beeSick only when the sick
  day caused the zero). Codex does not edit spec.md.

## Not taken
- Day-by-day readout in Is It Fair? ("Day 2: Bee away, Cat led..."): the bed mark (polish 6) covers the teacher's need
  without bringing back the day strip the spec removed for this mode.
- Distinct first-in-line step icons at 680x425 (play nit 10): the voice names each card and the rule cards carry their
  letter; an art redraw for a nit is not worth it now.
