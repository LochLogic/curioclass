# Play lens: up-the-watershed (round 1)

Played twice: as a grade 12 student alone at home (no teacher, nothing read first) and as a teacher projecting it at
1366x768. Own frames in `S:/CurioClass-codex-scratch/up-the-watershed/play/f1/` (drive.py, held clicks, port 9901);
shared audit frames in `S:/CurioClass-codex-scratch/up-the-watershed/audit-r1/`. Note: drive.py shots share one Chrome
profile, so localStorage carried between shots (p06 and p07 started with p05's beach samples; p03 started with p02's
claim). The readings below account for that.

What works: the first screen says what to do (hint plus the three numbered steps), the map reads as a real place, the
dry / storm flags and the bracket lines from icon to sample spots are clear, the beach case solves in 5 kits by honest
play (p05), the result card, Compare two ("Up 1,333 CFU/100 mL, From S6 to S7, dry day", p07) and the Fix-it plan
for Done when 6 ($2,955,000, beach "Protected, not cleaned", p08) all behave as the spec says. Motion off and the
mid-action resize are clean (audit).

## Findings

1. **Claim mode: an empty claim names every culprit, with zero kits spent.**
   Where: `src.html:1253-1258` (submitClaim, the "missed" branch). Open Beach closed, go straight to Claim, press
   Submit claim with nothing checked. Feedback: "Missed source. Look for beach closed evidence after a storm near
   pasture. / Missed source. The storm drains only flow in storms. / Missed source. Look for a dry-day jump below
   town." Kits left: 8. Checking all seven suspects and submitting (p02) does the same the other way: each culprit
   reads "right source, but evidence does not bracket it. Sample S1 and S2 after a storm." and each innocent gets its
   share. So the whole investigation (which suspects, which spots, which weather) is handed over before a single
   sample, and the student only has to follow instructions. "Show the whole creek" then also unlocks after that empty
   submit. This is the cheap pass REFINE asks lenses to try, and it works on all three cases. Better: a missed source
   gets a hint that points to a place to look without naming the source ("A source is still missing. Your samples
   don't explain the storm-day number at the beach yet."); accusing a culprit without evidence says "not proven yet"
   without the exact spot recipe until the student has sampled near it; and the whole-creek reveal waits for a claim
   with at least one evidence pair, or for the kits to run out.
   Seen: p01-empty-claim (text in drive output), p02-all-accused.png. Level: **blocker** (gives the answer away in
   the tool's hidden-information mode; POLISH, Games and quizzes). Tag: general.

2. **Claim feedback lands below the fold, with no cue to scroll.**
   Where: Claim panel, 1366x768 and 680x425. After Submit claim the feedback list starts under the buttons: at
   1366x768 with three culprits claimed only the first two items show and the third is cut by the footer
   (p05-beach-solve.png); with more items it runs to y=941 in a 768 tall window (p02, panel scrollHeight 891 vs 655).
   At 680x425 none of it is visible (p03, feedback top 378 under the footer, panel 475 vs 324). The feedback is the
   payoff of the whole claim step and a solo student may never see it. Better: scroll the first feedback item into view
   on submit (preventScroll off for that one element), or put feedback above the suspect list, or collapse the
   suspect list to the checked rows after a submit.
   Seen: p02-all-accused.png, p03-all-accused-680.png, p05-beach-solve.png. Level: **should fix**. Tag: general.
   (Audit missed it: its claim-solved state has one feedback item.)

3. **Fix-it looks enabled while it is locked, and says nothing when tapped.**
   Where: header `#m-fix` (`src.html:555`), Cases at every size. Disabled Fix-it has the same color and opacity as
   the live mode buttons (computed `rgb(232,237,243)`, opacity 1, p04); a tap does nothing and focus falls to the
   page (the audit's "focus fell to the page after clicking #m-fix" lead, confirmed: the cause is that the button is
   disabled). Nothing on screen says "solve a case to open Fix-it" until a case is solved. Better: a visibly locked
   style (dimmed, a small lock), and a title / hint "Solve any case to open Fix-it", or keep it clickable and show
   that sentence in the hint.
   Seen: size-1366x768.png, p04-fix-disabled.png. Level: **should fix**. Tag: general.

4. **Restart case wipes a solved case with one tap, no confirm.**
   Where: `#restart-case` (`src.html:583`, restartCase at 1519), beside Make claim in Sample. In p06 the creek was
   solved, then Sample, Restart case: the samples, the claim and the solved status were gone at once (solved list
   went from beach + creek to beach only), and it is saved that way. Clear my progress asks first; this does not,
   and it sits right next to the button a student presses most after sampling. Better: a confirm dialog like Clear
   my progress ("Restart Beach closed? This clears its 6 samples and your claim."), or only clear the samples and
   leave a solved case solved.
   Seen: p06-restart-after-solve (drive output). Level: **should fix**. Tag: general.

5. **Fix-it gauge bars are not meters: every missed goal shows the same 35 percent bar.**
   Where: `renderGauges`, `src.html:1449` (`g.met[i]?100:35`). The bar under each goal looks like progress toward the
   goal, but beach 431.5 (just over 410) and beach 739 draw the same bar, as does a 18.9 percent lake cut against the
   25 percent target (state-fix-tested-1366x768.png). A student reads "a third of the way" where nothing was
   measured. Better: fill by the real fraction of the goal reached (for example 410 / value for the beach, cut / 25
   percent for the lake, cut / 50 percent for the creek, worst weather), with a tick at the goal line, or drop the bar
   and keep the status words.
   Seen: state-fix-tested-1366x768.png, p08-fix-done6.png. Level: **should fix** (a meter that misleads). Tag: general.

6. **The newest result card covers the spots you need next, at preview sizes most of the map.**
   Where: `positionResult`, `src.html:1166`. At 1366x768 a beach result (S9) covers S8, the Treatment plant icon and
   its label (state-sample-result-1366x768.png); at 680x425 it covers S6, S7, Pipe, Storm drains and Old sewer
   (state-sample-result-680x425.png); at 375 it covers most of the map. The card has `pointer-events:none`, so a tap
   on a hidden spot goes through to it, but the student cannot see what they are tapping. Better: anchor the card in a
   corner of the map away from the sampled spot's downstream neighbours, or shrink it to the case pollutant only with
   "All four tests" in the Logbook, and fade it when another spot is selected.
   Seen: the frames named. Level: **polish**. Tag: general. (Audit overlap leads under sample-result and
   out-of-kits: confirmed as this one issue.)

7. **The default sample spot is the case target, whose numbers are already on the case card.**
   Where: `openCase`, `src.html:1024` (`state.site=CASES[id].target`). A solo student following "Tap a spot, choose
   Dry day or Day after storm, then press Take sample" can just press Take sample and spend a kit on 447, which the
   Beach closed card already showed (the audit's own sample-result state does exactly this). Better: start with no
   spot chosen (Take sample disabled with "Tap a spot on the map first"), or preselect a headwater spot.
   Seen: state-sample-result-1366x768.png, size-1366x768.png. Level: **polish**. Tag: general.

8. **Claim hint is hard to act on alone.**
   Where: `L.wClaim`, `src.html:775`: "Check sources with at least 20 percent at an over-limit target, dry or storm."
   A student alone cannot measure a 20 percent share from concentrations, and "over-limit target" is jargon. The
   action (check a suspect, press Add evidence) is at the end. Better: lead with the action and the evidence idea:
   "Check each suspect you blame, then press Add evidence and pick the samples above and below it." (close to the
   spec's own wClaim line), and leave the 20 percent rule in Model notes. Teaching lens may weigh in on the rule.
   Seen: state-mode-claim-1366x768.png, hint text. Level: **polish**. Tag: general.

9. **Solving a case lands flat on the map view.**
   Where: Claim after a correct submit (p05-beach-solve.png). The only change is the hint text, a chime and the
   spoken line; the third "right" item is below the fold (finding 2) and the "Solved" stamp shows only back on Cases.
   9-12 wants minimal celebration, but the moment should still be visible. Better: a small "Case solved" stamp on the
   case heading in the panel (the same stamp as the Cases card) and the Fix-it button lighting up as it unlocks.
   Level: **polish**. Tag: general.

10. **Creek gauge label collides at 375 wide.**
    Where: Fix-it, 375x812 iframe host: "Change" runs under "0% cut" (zoom of state-fix-tested-375x812.png, saved as
    `S:/CurioClass-codex-scratch/up-the-watershed/play/zoom-creek-375.png`). Better: a shorter row label ("Cut") or
    the 29 px label column widened for that row. Level: **polish**. Tag: general. (Audit missed it.)

11. **Logbook and Compare two open the same dialog.**
    Where: `src.html:1564-1565`. Both buttons open the logbook with "Tap two logbook entries. Then press Compare
    selected."; only the title differs. With one entry (state-logbook-1366x768.png) it still asks for two. Better: one
    "Logbook" button, and the compare prompt only once there are two entries. Level: **nit**. Tag: general.

12. **Projected, the map labels are small.**
    Where: map at 1366x768: suspect names, place names and the legend are 10 px, spot discs 11 px
    (`.map-place`, `.suspect-map span`, `.spot .disc`). Fine on a laptop, hard from the back of a room. Better: 12 px
    labels at 1280 wide and up. Level: **nit**. Tag: general.

Nothing cultural, Native or hard-history: no sensitivity review needed from this lens.

## Counts

blocker 1, should fix 4, polish 5, nit 2.

## Audit pilot

- Leads confirmed: result-card overlaps under sample-result and out-of-kits (finding 6, one issue, by design a popup
  but too large at preview sizes); "focus fell to the page after clicking #m-fix" (finding 3: Fix-it is disabled but
  styled as live).
- Leads wrong or not worth a finding: "Restart case: nothing changed" (expected on a case with no samples; the real
  problem is the opposite, finding 4); footer controls below the fold at 375 (Model notes, Reset, Clear my progress are
  secondary and reachable by scrolling); welcome cut by a first tap on Model notes, Clear my progress or a quick second
  Open case (allowed by BASELINE rule 16; the hint carries it); overlaps of the Logbook dialog over the map (a modal
  over a dimmed page).
- Missed by the audit: the empty-claim giveaway (finding 1), claim feedback below the fold (finding 2, its
  claim-solved state has only one feedback item), the fixed 35 percent gauge bars (finding 5), the "Change" collision at
  375 (finding 10), Restart case with no confirm (finding 4).
