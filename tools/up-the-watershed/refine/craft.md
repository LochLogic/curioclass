# Craft lens: up-the-watershed (round 1)

Bundle `tools/up-the-watershed/up-the-watershed.html` as built (not re-bundled). Shared audit:
`S:/CurioClass-codex-scratch/up-the-watershed/audit-r1/audit.md`. My frames and drive logs:
`S:/CurioClass-codex-scratch/up-the-watershed/craft/` (v1, v3, v5 folders; v3.txt, v4.txt). Not a Curiosity (no
"(Curiosity No. NN)" line), so lesson norms apply.

## Contract (clean)

- One file, 761 KB: under the 2 MB goal. All 22 `art:` tokens are inlined as data URIs; every `<img>` loaded
  (18 of 18 complete, c-contract shot). `performance.getEntriesByType('resource')` is empty; no `http` string, `fetch`,
  XHR or dynamic import in the bundle. No console errors, warnings or exceptions in any of my shots or the audit.
- Kit used: `Curio.voice`, `Curio.tone`, `Curio.wait`, `Curio.reduce`, kit Motion/Sound/Read. Nothing re-implemented.
- Lines: `allLines()` returns 20 strings, identical word for word to `voice/lines.json` (no missing, no extra).
- Art: every token has a `prompts.json` entry; all 22 are `people: false`; the 8 local FLUX images are scenes with no
  people. Credits for both routes are in `tool.draft.json`.
- Words: no em dashes in src, notes, lines, spec or tool.draft.json; "Curio Class" never "Curio" alone on screen.
  Privacy is stated in the footer ("Progress stays on this device. Nothing leaves it.") and Clear my progress confirms.
- Focus is visible (4 px `#b7ecff` outline on map buttons, k-focus-spot.png); panel controls come before map items in
  tab order; Motion off is clean (audit).

## Findings

1. **Restart case wipes a case with one tap, no confirm.** `src.html:583`, `restartCase()` at 1519. It sits beside
   Make claim and clears every sample, the claim and the solved stamp; if that was the only solved case, Fix-it locks
   again. Clear my progress asks first; this does not. Seen: r-stale-kits (8 samples, one tap on Restart case, `n: 0`).
   Better: a confirm dialog like Clear my progress, or an Undo in the hint. **should fix**, general.

2. **The sample result is never announced.** `#map-result` has no `aria-live` and focus stays on Take sample
   (k-focus-spot `live: null`). A keyboard or screen-reader student presses Take sample and hears only the hint; the
   four values, units and the limit bar are silent. Better: `aria-live="polite"` on the result card (or announce a
   one-line summary such as "S9, dry day: E. coli 447 CFU per 100 mL, over the 410 line"). **should fix**, general.

3. **Fix cards drop the price from their accessible name.** `buildFixes()` 1381 and `updateFix()` 1421 set
   `aria-label="Add Fence & troughs"`, which replaces the visible text, so the cost is never read; effect and who pays
   live only in `aria-description`. Cost is the decision in this mode. Seen: k-focus-spot (`fixlabel`, `fixdesc`).
   Better: drop the aria-label and let the visible text plus a state word name it, or put the price in the label.
   **should fix**, general.

4. **The goal gauges' bars are not meters.** `renderGauges()` 1449: `width = met ? 100 : 35`. Every missed goal
   draws the same 35 percent bar whatever the numbers (C + A misses the beach by 22 and the lake by a lot; both show
   35), and an untested plan shows 0. It reads as progress toward the goal. BUILD.md "Honest numbers". Seen:
   audit state-fix-tested-1366x768.png and -680x425.png. Better: scale each bar to real progress (for example the
   creek's percent cut over 50, the lake's dry P against 0.05) with the goal marked, or remove the bar and keep the
   check / cross. **should fix**, general.

5. **The result card hides the map it reports on.** `positionResult()` 1166. At 1366x768 a beach sample (S9) puts
   the card over S8, the treatment plant and part of Outfall; at 680x425 and 375 wide it covers half the map (S6, S7,
   Pipe, Old sewer, Storm drains, plant, S8). Spots under it still take clicks (`pointer-events:none`) but cannot be
   seen. Seen: audit state-sample-result-1366x768, -680x425, -375x812 (confirmed on the frames; the audit's overlap
   rows there are real). Better: dock the card in a map corner away from the spot path, or shrink it to a strip at
   small sizes. **should fix**, general.

6. **Revealed flags look like sampled flags in Sample mode.** `updateMap()` 1065 draws D and S flags at every spot
   whenever `state.reveal` is on, in any mode, and Show the whole creek is not reset when the student presses Sample
   (the reveal hint even sends them there). Sample then shows flags on all 11 spots with "Kits left: 8" and the plain
   sampling hint; Logbook lists 22 entries the student never took. One look, two meanings (BUILD.md lesson). Seen:
   rv-sample-after-reveal.png (24 flags, 8 kits), rv-logbook-after-reveal (22 entries). Better: draw revealed values
   in their own style (hollow flags, "revealed" in the legend) and say so in the Sample hint, or end the reveal when
   leaving Claim. **should fix**, general.

7. **Two how-to lines are sent as events and repeat every time.** `EVENT_LINES` 929: `submitted` ("Read the
   feedback. Change a suspect or its evidence, then press Submit claim again.") spoke 5 of 5 failed submits, and
   `noPlan` ("This plan misses a goal. Compare the gauges, change a fix, or press Save plan and explain your
   priorities.") spoke 5 of 5 Test plans, the last four on an unchanged plan. Both are mostly instructions; the spec
   made noPlan "first Test plan". This is the nag STANDARDS warns about. Better: split each into a short event ("Not
   yet. Two sources need more evidence." / "This plan misses a goal.") and a how-to said once. Seen: v-claim-submit5,
   v-fix-test5 (logs in v1 and v3.txt). **should fix**, general.

8. **The whole creek can be revealed for free.** Submit an empty claim on a fresh case (0 kits used): the feedback
   names every missed culprit with the weather or samples to take ("Missed source. The storm drains only flow in
   storms."), Show the whole creek unlocks and draws every suspect's share, and all 8 kits are still there to collect
   exactly the listed pairs. Seen: rv-sample-after-reveal (empty submit, reveal, Kits left: 8). The spec allows the
   reveal "after a submit"; it does not say an empty one. Lead for the Teaching and Play lenses (BUILD.md "No
   giveaways"); the integrator should weigh it. Better: unlock the reveal only once kits are spent or the case is
   solved, and have a missed source say only "a source is missing" until some evidence is in. **should fix**, general.

9. **Fix-it is disabled with no reason given.** `#m-fix` (555) is disabled until a case is solved; no hint, title
   or Cases step says so, and a disabled button can't take focus, so a keyboard user never finds it. The audit's
   "focus fell to the page after clicking #m-fix" comes from clicking it while disabled. Better: "03 / Change it:
   opens after you solve a case" in the Cases panel, or keep it enabled with an explanatory hint. **polish**, general.

10. **Gauge numbers don't match the rest of the tool.** `renderGauges()` 1439 to 1447: Before shows the creek at
    480.8 (case card and Sample show 481) and the beach at 447 / 739 while After shows 431.5 / 518.5 (spec worked plan:
    432 / 519). Seen: audit state-fix-tested-1366x768. Better: one rounding per quantity everywhere. **polish**,
    general.

11. **"soil" vs "sediment".** Logbook entries read "soil 9.3 mg/L" (1318) and fix effects say "soil −60%" (758 to
    763), while the result card, case card, gauge and Model notes say suspended sediment. Better: "sediment" throughout.
    **nit**, general.

12. **Treatment plant label sits on the creek.** `#suspect-E span { right:110% }` (130) puts "Treatment plant" left
    of its icon, on the creek beside S8, where it reads as a label for S8. Seen: k-focus-spot.png, audit
    state-whole-creek-1366x768. **nit**, general.

13. **"Construction" breaks mid-word in the Claim list at 680x425** ("Construc / tion", `overflow-wrap:anywhere`
    at 441). Seen: audit state-claim-solved-680x425. **nit**, general.

Counts: blockers 0, should fix 8, polish 2, nits 3.

## Standard voice check

Held clicks (0.12 s), Sound on, Motion on, 1366x768, fresh Chrome profile per run where progress mattered
(progress persists in localStorage, so a reused profile suppresses welcomes; those runs were redone).

| line | kind | expected | spoken |
|---|---|---|---|
| wCases | welcome | once | 1 (stage tap, first key, Reset) |
| wSample | welcome | once | 1 of 10 Take sample taps |
| bracket | how | once | 1, then silent |
| lastKit | event | each time | 1 of 1 (7th kit) |
| outOfKits | event | each time | 1 of 1 (8th kit) |
| wClaim | welcome | once | 1 |
| chooseEvidence | how | once | 1 |
| submitted | event in code, how-to in words | once | **5 of 5** (finding 7) |
| solved | event | each time | 1 of 1 |
| wFix | welcome | once | 1 in 5 Add / Remove toggles |
| noPlan | event (spec: first Test plan) | once per new plan | **5 of 5, same plan** (finding 7) |
| overBudget | event | on crossing | 1 (all nine fixes, $4,100,000, Test plan disabled) |

- Stale: fast taps (0.2 s) through Take sample, Claim, Cases and Reset: lastKit cut by the mode change, wClaim cut by
  Reset, the queued bracket line dropped as newer; no line played after its moment. Restart case cut outOfKits.
- First tap: a stage tap and the first Tab key give the welcome within about 0.1 s; Open case gives only wSample;
  Read speaks the hint only; Sound says nothing (audit table rows 4 and 5). No line names a disabled control (outOfKits
  needs Make claim; overBudget needs a selected fix).
- Read: Read during wSample cut it and spoke the hint; the next mode's welcome started 1.4 s later; Read with Sound
  off spoke. Order followed the actions in every log.
- Not driven: saved, compare, why, fixDetails, emptyLog, emptyPlans, emptyBudgetPlans (each is a dialog or a one-off
  how line; their texts match the dialogs they open).

## Audit pilot

- Confirmed: the result card overlaps at 680x425, 800x500, 1366x768 and 375 wide (finding 5); "Restart case: nothing
  changed" is true (an empty case), and the real problem is the missing confirm once there is something to lose
  (finding 1); the 375 wide footer links below the fold are real but are not main controls.
- Wrong or not findings: every logbook "text hidden" row is the modal dialog over its own backdrop; "focus fell to the
  page after clicking #m-fix" is a click on a disabled button (finding 9 is the real issue); the welcome cut by a first
  tap on Model notes or Clear my progress, and by two quick taps on Open case, is allowed by BASELINE rule 16 and the
  hint keeps it.
- Missed: revealed flags shown as sampled in Sample mode (6), the gauge bar that is not a meter (4), the unannounced
  result card and the price missing from fix-card names (2, 3), how-to lines repeating as events (7), and the free
  reveal path (8). These need state, meaning or assistive-tech checks the audit doesn't run.
