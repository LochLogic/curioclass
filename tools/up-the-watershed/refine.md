OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 2 (general 2, family 0), should fix 12 (general 12, family 0), polish accepted 9

# Refine: up-the-watershed

Lens files: refine/teaching.md, refine/play.md, refine/craft.md. Shared audit and frames:
S:/CurioClass-codex-scratch/up-the-watershed/audit-r1. Lens frames: S:/CurioClass-codex-scratch/up-the-watershed/teaching/frames,
.../play/f1, .../craft. Not a Curiosity; lesson norms apply. Integrator spot-checked src.html 643, 775, 1176-1189,
1222-1262, 1440-1460 and 1519-1525: blocker 1, blocker 2, should fix 1, 2 and 3 are confirmed in code.

## Blocker
1. **An empty or blanket claim hands over the whole answer key.** src.html:1222-1262 (submitClaim, renderClaim), 1225
   (whole-creek unlock), 1569. Open any case, go to Claim, press Submit claim with nothing checked and 8 kits left:
   every missed culprit is named with its place and weather ("Missed source. Look for beach closed evidence after a
   storm near pasture." / "The storm drains only flow in storms." / "Look for a dry-day jump below town."), and Show
   the whole creek unlocks with every suspect's share. Checking all seven suspects does the same the other way: each
   culprit gets the exact spot recipe ("Sample S1 and S2 after a storm.") and each innocent its share. A student can
   solve all three cases without choosing one sampling stop, which is the tool's one idea. Seen: teaching
   frames/empty-submit.png, empty-submit-reveal.png; play p02-all-accused.png; craft rv-sample-after-reveal.png.
   Fixed looks like: (a) Submit claim stays disabled until at least one suspect is checked and every checked suspect
   has evidence attached (hint: "Add evidence for each suspect you check."); (b) a missed source gets a nudge that names
   the weather and the target but no source, place or spot ("A source is still missing. Your samples don't explain the
   storm-day number at the beach yet."); (c) an accused culprit whose evidence does not bracket it says "Right source,
   not proven yet: you need a sample just above it and just below it, in the same weather" and gives the exact spots
   only when the attached samples are already in the right weather or one stop off; (d) Show the whole creek unlocks
   only when the case is solved or the kits are spent, not after any submit. Check the cheap paths after the fix:
   empty submit, all seven checked, all seven checked with one sample each. (general; Teaching tagged it
   family:hidden-information, the lesson is general: a submit with nothing in it must not return the key)
2. **Fix-it goal bars are a fixed 35 percent for any missed goal, and the goal line vanishes after Test plan.**
   src.html:1449 (`g.met[i]?100:35`), 1458 (`d.detail || d.target`). Beach 431.5 and beach 739 draw the same bar;
   a 18.9 percent lake cut and a 7.3 percent one look alike; after testing, the Lake and Creek captions are replaced by
   "Storm concentration ..." and "Dry remains ...", so the target is gone while students compare. REFINE: a meter
   that misleads is a blocker. Seen: audit-r1/state-fix-tested-1366x768.png, play p08-fix-done6.png. Fixed looks like:
   each bar fills by real progress toward its goal in the worse weather (beach 410 / value capped at 100, lake cut /
   25 percent and dry 0.05 / value, the smaller of the two, creek cut / 50 percent), with a tick at the goal; the
   target line stays on screen under any detail line. (general)

## Should fix
1. **The map draws the storm drains joining below the Main Street bridge (S7), but the model adds them above S7.**
   src.html:643 (`M810 421L612 470`); S7 sits at about (560, 483) and the line ends at (612, 470), downstream. The
   model (859-862), the spec and the evidence rule (D1 bracketed by S6 and S7, or the Pipe) put them above S7. A
   student bracketing from the map would pick S7 and S8 and be told it does not bracket. Seen: teaching
   frames/crop-pipe.png. Fixed: the drain line meets the creek between the Old sewer and the S7 bridge; check the
   Pipe spot and Storm drains icon still sit on it. (general)
2. **The 20 percent culprit rule cannot be checked from anything on screen, and the Claim hint leads with it.**
   src.html:775 (wClaim), 1592; result card, logbook and Compare two. Shares depend on load = concentration x flow, but
   no flow is shown anywhere, so the rule is learned only from feedback; notes.md "Key skills" claims "Distinguish
   concentration, load and dilution". SPEC.md: a skill the tool claims needs a step that does it. Fixed: show flow
   (m3/s) on each result card and logbook row, and a load line in Compare two ("Load up 13.3 billion CFU per second
   from S6 to S7, dry day"), so the rule is checkable from the samples. Restore the spec's wClaim line ("Check each
   suspect you blame, then press Add evidence for each one."), re-recorded, and keep the 20 percent rule in the Claim
   panel's small print and Model notes. If flow and load can't be shown cleanly, drop the key skill from notes.md
   instead (rule 2); showing them is the preferred fix. (general; Play polish 8 merged here)
3. **Attaching every logbook sample to every suspect passes the evidence check.** src.html:1176-1189 (validEvidence
   only asks whether the needed pair is somewhere in the set). Teaching drive: eight beach samples on Pasture, Storm
   drains and Old sewer all return valid. Fixed: evidence holding samples from other reaches gets "Right source; trim
   the evidence to the pair that brackets it"; allowed sets are the bracketing pair, the direct sample, and for D1 the
   storm pair plus its dry contrast pair. (general)
4. **Claim feedback lands below the fold with no cue.** Claim panel. At 1366x768 with three culprits the third item
   is cut by the footer (play p05-beach-solve.png); with seven it runs to y=941 (p02); at 680x425 none of it shows
   (p03-all-accused-680.png). Fixed: on submit, scroll the first feedback item into view, or move feedback above the
   suspect list. (general)
5. **The newest result card hides the spots the student needs next.** src.html:1166 (positionResult). At 1366x768 a
   beach sample covers S8, the plant and its label; at 680x425 and 375 wide it covers S6, S7, Pipe, Storm drains and
   Old sewer; spots under it still take clicks unseen. Seen: audit-r1/state-sample-result-1366x768.png, -680x425.png,
   -375x812.png. Fixed: dock the card in a map corner away from the creek path (a strip at small sizes) and fade it
   when another spot is selected. (general; Play had it as polish, Craft as should fix)
6. **Revealed values look like sampled flags in Sample mode.** src.html:1065 (updateMap draws flags whenever
   state.reveal), reveal not reset on leaving Claim. Sample then shows flags on all 11 spots with "Kits left: 8", and
   Logbook lists 22 entries never taken. Seen: craft rv-sample-after-reveal.png, rv-logbook-after-reveal. Fixed: end
   the reveal when leaving Claim, or draw revealed values in their own style (hollow flags, "revealed" in the legend)
   and keep them out of the Logbook. (general)
7. **Restart case wipes a solved case with one tap.** src.html:583, restartCase 1519. It sits beside Make claim and
   clears samples, claim and the solved stamp (and relocks Fix-it if it was the only solved case). Seen: play
   p06-restart-after-solve, craft r-stale-kits. Fixed: a confirm like Clear my progress ("Restart Beach closed? This
   clears its 6 samples and your claim."). Skip the confirm when the case has no samples. (general)
8. **Fix-it looks live while locked and says nothing when tapped.** #m-fix, src.html:555. Same color and opacity as
   live mode buttons; a tap does nothing and focus drops to the page (the audit's #m-fix lead); a keyboard user never
   reaches it. Seen: audit-r1/size-1366x768.png, play p04-fix-disabled.png. Fixed: a visibly locked style and the
   reason on screen ("Fix-it opens after you solve a case", in the Cases panel steps and as the button's title), and
   it lights up when it unlocks. (general; Craft had it as polish)
9. **Two how-to lines are sent as events and repeat every time.** src.html:929 (EVENT_LINES). `submitted` spoke 5 of 5
   failed submits; `noPlan` spoke 5 of 5 Test plans, four on an unchanged plan, and its words differ from the spec.
   Seen: craft v1 and v3.txt logs. Fixed: noPlan follows the spec (first Test plan that misses a goal, stale on plan
   change, the spec's words "No plan here fixes everything for three million. Pick what matters most, and write
   why."); submitted becomes a how-to said once, with the on-screen hint carrying it after. (general)
10. **The sample result is never announced.** #map-result has no aria-live; focus stays on Take sample. Seen: craft
    k-focus-spot (`live: null`). Fixed: aria-live="polite" with a one-line summary ("S9, dry day: E. coli 447 CFU per
    100 mL, over the 410 line"). (general)
11. **Fix cards drop the price from their accessible name.** src.html:1381 (buildFixes), 1421 (updateFix):
    aria-label="Add Fence & troughs" replaces the visible text, so cost is never read. Fixed: put name, cost and state
    in the label ("Add Fence and troughs, $60,000"), or drop the aria-label. (general)
12. **Builder change notes leaked into notes.md "The modes".** "Use Fix details to read every intervention's effects
    ... The claim instruction states the 20 percent source rule before students submit." and "Field photographs
    preserve the whole scene, including the cattle's feet in the creek." read as fix logs. Fixed: cut them; keep one
    plain sentence that whole-creek shares count only sources upstream of the target. Update the Claim and reveal
    paragraph to match blocker 1. (general)

## Polish accepted
1. **Muddy creek band.** src.html:714, Model notes 1595. 481 mg/L is in EIFAC's fourth band (over 400, poor fisheries
   at best), not "Over 80: unlikely good fisheries". Card: "Over 400: poor fisheries at best"; Model notes list all
   four bands. Goal and case logic unchanged. (general)
2. **Default spot is the target, already on the case card.** src.html:1024. Start with no spot chosen; Take sample
   disabled with "Tap a spot on the map first." (general)
3. **Solving lands flat.** After a right claim, show the Solved stamp on the case heading in the panel (same stamp as
   the Cases card), alongside Fix-it lighting up (should fix 8). (general)
4. **"Change" collides with "0% cut" in the Creek gauge at 375 wide.** Seen: play zoom-creek-375.png. Shorter row label
   ("Cut") or a wider label column. (general)
5. **Gauge rounding differs from the rest of the tool.** src.html:1439-1447: Before creek 480.8 vs 481 on the card;
   After beach 431.5 / 518.5 vs 447 / 739 Before. One rounding per quantity (whole numbers for E. coli and sediment,
   three decimals for P). (general)
6. **"soil" vs "sediment".** Logbook (1318) and fix effects (758-763) say soil; everything else says suspended
   sediment. "sediment" throughout. (nit, general)
7. **Treatment plant label sits on the creek beside S8.** src.html:130 (`#suspect-E span { right:110% }`). Move it off
   the water. Seen: craft k-focus-spot.png. (nit, general)
8. **"Construc / tion" breaks mid-word at 680x425** (overflow-wrap:anywhere, 441). Seen: audit-r1/state-claim-solved-680x425.png.
   (nit, general)
9. **Compare two asks for two entries when there is one.** src.html:1564-1565. With fewer than two samples, Compare
   two says "Take two samples to compare." (nit, general)

## Settled calls
- Blocker 1 changes three spec lines ("missed (a hint naming the weather)" with the drains example, "right but ...
  (with what to sample)", "After a submit, Show the whole creek"). Settled by SPEC.md "Scores and checks reward the
  right thing" (doing nothing and the shortcut must not win) and BUILD.md "No giveaways": the weather hint stays, the
  source name and the spot recipe go until evidence is in. Not a question for Cory.
- Gauge bars: lenses said should fix; REFINE makes a misleading meter a blocker.
- Result card and Fix-it lock: Play and Craft split polish / should fix; taken as should fix (both hide or misstate
  something a solo student needs, rule 4).
- The culprit rule and "concentration, load and dilution": fixed by showing flow and load (rule 2 needs a real step);
  dropping the key skill is the fallback only.
- The spec's three open questions are settled, not sent: the title "Up the Watershed" is already in use; the rain
  advisory stays as an honest real-world option (BASELINE rule 9), already labeled "Protected, not cleaned" with the
  water value; made-up costs, flows and loads stay, and notes.md already says so.
- Audit leads not taken: welcome cut by a first tap (BASELINE rule 16, the hint keeps it); logbook "text hidden"
  overlaps (a modal over its backdrop); footer links below the fold at 375 (secondary, reachable).
- Do not change: the load model and every Sample, share and worked-plan number (Teaching recomputed all; they match);
  the standards (both are really taught); the Why box staying unsaved; the art credits (Craft found both routes
  credited and every image people-free).

## To the spec's open questions
None. Everything above is settled by BASELINE, SPEC.md or REFINE.

## Not taken
- Missed-source wording that splices the case title (Teaching nit 8): moot after blocker 1.
- tool.draft.json lists two art routes (Teaching nit 9): Craft confirmed both are real and credited.
- One Logbook button instead of Logbook and Compare two (Play nit 11): the spec names both; the cheap half is polish 9.
- 12 px map labels at 1280 wide and up (Play nit 12): map layout risk for a projection-only gain; Done when 9's 10 px
  floor holds.
