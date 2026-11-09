# Polish: traffic-light-coder (Codex fix, round 1)

Curiosity override: the user's instruction and CODEX-CURIOSITY.md win over the legacy lesson spec
and Refine's "Not a Curiosity" settled call. Kept the crossing, painted assets, rule engine,
traffic scripts, timing and replay. Replaced jobs with freely selectable setups and observations.
Removed the kit header/CSS, goals, check badges, completion state, Next job and finale.
Added the lower-left Manual, engraved family plate and instrument power panel. No number was
invented: neither the supplied spec nor CURIOSITIES.md assigns this tool a Curiosity number.

Evidence is in `_scratch/traffic-light-coder/`, including `before-src.html` and `before-notes.md`.

## Blocker

1. **FIXED, with the Curiosity override.** Reproduced all three cheap yellow programs in the
   browser before repair: `before-numbers.json` (10 s and 30 s) and `before-third-cheat.json`
   (YELLOW plus ambulance KEEP above the normal yellow rule). All reported success and
   `ambulanceStopped:false` despite stopped vehicle frames beginning at 42.5 s. The result now
   latches the ambulance's own stopped flag each beat until it clears the crossing, including
   queues after detector expiry. `final-numbers.json`: all three true, stop at 42.5 s; original
   setup true; top priority rule false. `additional-cheats.json`: bottom priority rule true.
   `fix-final-detail/final-stopped-ambulance.png`, 1366x768, shows Had to stop, 42.5 s, Rule 1.
   No goal or completion claim remains. The original half-second worked light changes hold. The post-audit any-vehicle check is in `two-ambulances.json`.
2. **FIXED, with the Curiosity override.** Reproduced deletion of rule 4: legacy success,
   longest red 81.5 s (`before-numbers.json`). The record now retains each red's next state,
   distinguishes a still-open red from a return to GREEN, and has no success grade. Internal
   `carsReturn` additionally requires every red to end in GREEN within the existing 45 s model
   reference. Re-ran 64 single edits: before, 12 unsafe/broken or valid variants earned success;
   after, only `extra-3-done` meets safe + everyone crossed + carsReturn (`final-numbers.json`).
   Original starting rules still give three Green while crossing moments; DEFAULT has none and
   carsReturn true. `fix-after/after-held-red.png`, 1366x768, shows the 81.5 s held red without
   congratulation; the later record wording explicitly labels the interval still open. Notes updated.

## Should fix

3. **FIXED, adapted to setups.** `fix-before/before-jobs.png`, 1366x768, had only title and goal.
   Each setup now has a persistent, plain problem line, and its waiting hint repeats that
   observation plus Tap a rule / Run script. No solution is disclosed. `fix-final/final-setup-1.png`
   through `final-setup-5.png` show all five at 1366x768; held Read evidence is `voice-side.json`.
4. **FIXED.** Reproduced the false changed-the-light attribution in `fix-before/before-order.png`,
   1366x768. Ambulance cause now says Rule N fired first. Rush Hour names WALK requests rather
   than a car-light change. `fix-final-detail/final-order-below.png` and
   `final-stopped-ambulance.png`, same size, show the corrected causes.
5. **FIXED.** The 30-only variant had longest red 63 s and `order:false`, so no cause sentence
   (`before-numbers.json`, j4_30only). Counts now come from actual firings in the longest red.
   `fix-after/after-order.png`, 1366x768: Rule 3 requested WALK 34 times, four actual new walks,
   while cars waited 63 s. `final-order-below.png` confirms the same attribution with the timed
   return rule still below WALK. WALK requests during an active walk remain honest no-ops.
6. **FIXED.** At 760x900, before Add rule was y=1017.98..1061.98, outside the viewport
   (`fix-before/before-760.png` and drive output). Side-by-side compact cabinet now keeps it
   y=364..408 in Setups (`fit-760.json`, `fix-behaviour/after-760-setups.png`). Live Add rule
   also fits. The 375-wide page remains stacked.
7. **FIXED.** Reproduced the hidden sentence / generic tabs at 1366x768 and 680x425:
   `fix-before/before-picker.png`, `before-picker-680.png`. The picker now shows the live rule
   sentence, current tab values and updates them after every choice; focus stays on the chosen
   option. `fix-final-detail/final-picker-1366.png`, `final-picker-680.png`; latest dialog with
   its own explicit Read control: `fix-contacts/picker-actions.png`, 680x425, and
   `fix-last/phone-picker-fixed.png`, 375x812 host.
8. **FIXED.** Reproduced the 60 px buttons over the crossing/stop areas in
   `fix-before/before-buttons-680.png` and `fix-phone-models/before-phone.png` (375-wide host).
   Compact buttons now occupy the outer sidewalk corners with 44x44 hit areas. At 680x425 the
   south button is x=332.45..376.45, clear of the central crosswalk and stopped traffic;
   at 375x812 it is x=316.48..360.48, y=181.47..225.47. Evidence: `layout-680.json`,
   `phone-fixed.json`, `fix-last/phone-street-fixed.png`, `fix-behaviour/after-680-fit.png`.
   The 1366x768 60 px positions are retained. Phone street now precedes the editor.
   Final compact text is 10 px and the decorative label is hidden; see `fix-audit-followups/`.
9. **FIXED by removing the goal card.** Reproduced symbolic goal language in
   `fix-before/before-rush.png`, 1366x768. Fair-time references are now plain words in the
   Manual and labelled this tool's own. Empty red is Cars stopped with nobody crossing in the
   record. `fix-final-detail/final-order-below.png`, same size; `fix-last/manual-fixed.png`
   demonstrates the usable Manual at 680x425. No goal was added.
10. **FIXED with the Curiosity voice rule.** `before-voice.json` reproduces the spoken Add rule
    instruction behind the picker. The old line and job speech are removed. Picker hint and its
    explicit Read now say Pick a chip, then press Done. Read is inside the native dialog, so it
    is usable there. After Done the normal hint offers Add rule. Latest `voice-main.json` has
    the curb hint once and exactly two deliberate picker Reads; `allLines()` equals lines.json.
    No automatic picker speech was added. The legacy spec line table is preserved as history;
    it is superseded by the Curiosity rule and the matching runtime/voice table.
11. **FIXED.** Reproduced the false absolute in `before-notes.md`: bottom rule can never get a
    turn. Current notes ask why a rule lower down can lose its turn. The original lower-rule
    behavior is retained; priority only matters when a higher rule also matches.
12. **FIXED within scope.** Reproduced practiced directly in `before-notes.md`. Current notes
    identify authored selection, used events, indirect sequence and inspected fixed iteration,
    rather than claiming full direct coverage. The panel foot names the half-second loop;
    Step's accessible name and Manual do too. The first two setup notes describe constructing
    GREEN, YELLOW, RED, WALK transitions from rules. `fix-contacts/after-1280-fit.png` and
    `fix-final/final-live-1366.png`; keyboard rule edit is in `keyboard.json`. Module reassignment
    stays an owner decision outside the allowed write scope.

## Polish accepted

13. **NOT APPLIED, Curiosity override.** No all-five-jobs finale, dots, completion state or finish
    screen was added. The legacy completion machinery was removed. Every setup remains available.
14. **FIXED.** Compact restore button reads Defaults; Reset street keeps its circular arrow.
    `fix-behaviour/after-680-fit.png`, 680x425.
15. **FIXED, exploratory hint only.** After the first full return to green, a quiet hint invites
    a different action on rule 1 and another curb press. No goal or repeated speech.
    `cycle-hint.json`, `fix-behaviour/cycle-hint.png`, 1366x768; GREEN returned at 22.5 s in that run.
16. **FIXED.** Chips and rule words compute to 14 px at 1366x768 (`additional-cheats.json`).
    Six rules retain the permitted internal scroll, while Add rule and edit controls stay visible:
    `fix-final-detail/final-six-1366.png`. Four-rule cards fit without that scroll.
17. **FIXED.** Options retain words and use actual lamp colors. Turn actions add an arrow.
    `fix-contacts/picker-actions.png`, 680x425: arrow-dot colors rgb(31,157,85),
    rgb(242,183,5), rgb(217,58,43). Current values also remain in the sentence and tabs.
18. **FIXED.** Every scripted observation endpoint focuses `#record-heading` with preventScroll.
    The record is a section, with the false dialog role removed.
    `fix-final-detail/final-unsafe-680.png` and drive result `focus:record-heading`, 680x425.
19. **FIXED.** The setup card's pseudo-element tab is removed. All five setup frames at 1366x768
    and the compact unsafe record frame show no grey drag-handle tab.
20. **FIXED.** Firing tape includes G, Y, R or W inside the dot beside each rule number.
    `fix-behaviour/grayscale.png`, 1366x768, and `fix-last/phone-street-fixed.png`, 375-wide host.

## Settled calls

- Applied: no fourth unsafe kind; no walker spacing or Rush Hour timing change; six-rule internal
  scroll and the 375-wide stacked page retained; unsafe green-while-crossing replay retained.
- Applied cause/wording priorities. Third-setup return-to-green is an observation/diagnostic,
  not a newly added goal check. No curriculum/module file was edited.
- Rejected only the settled statement Not a Curiosity and all implied lesson requirements,
  because the user's explicit instruction takes precedence. Existing people art is unchanged.
- The initial curb hint may be cut by action; its instructions remain visible and available to Read.

## Cheats tried

- Yellow 10 s, yellow 30 s, and YELLOW/ambulance KEEP above the normal yellow transition:
  all originally lied; all now report the observed stop at 42.5 s. Top priority keeps the
  ambulance moving; the same rule at the bottom reports its actual stop.
- Deleted return-to-green rule: 81.5 s red, now explicit, with no success/advance/finale to earn.
- Replaced RED return with YELLOW: six red intervals end in yellow; internal carsReturn false.
- Put ANY/KEEP first: walkers remain waiting; the record exposes that stall, with no reward.
- Expanded the 64-case probe to 96 edits, 77 distinct programs (`before-96.json`, `after-96.json`).
  Before, 16 edit attempts earned success. After, only replacing or augmenting the return rule
  with done yields safe crossings, every walker across and timely green returns (two valid programs).
- 100 presses per curb create two waiting manual walkers total, not 200 (`extremes.json`).
  One Step advances exactly 0.5 s. Empty program observes 0 of 3 crossed at the 120 s cap.

## Voice walk

- Held clicks, 0.12 s holds, 2 s gaps. `voice-main.json`: initial curb hint spoken once;
  Pick a chip, then press Done read twice, only on the two deliberate dialog Read presses.
- Side path: setup problem/next action on Read, then observational record instructions on Read
  (`voice-side.json`). No job welcome, success/failure event or finale. Curiosity's voice rule wins.
- Three bank lines exactly equal `allLines()`. Existing browser fallback is retained; no new recording.
- Keyboard: edited rule 4 from timed condition to walk is done, escaped the picker and returned
  focus to rule 4 (`keyboard.json`). Record focus is checked separately at the endpoint.

## Engine changes wanted

No tool engine change required. Audit limitation: `scripts/audit_tool.py` `MODES_JS` detects only
header mode groups. A future shared audit update should include instrument `[role=group]` mode
selectors outside a header. This run uses explicit audit states and held setup input instead;
no header was added to satisfy the auditor and no shared script was edited.

## Audit

The single 40-minute-limited audit finished: `fix-audit/audit.md`, 92 frames, 581 leads.
No console/runtime errors, infinite Motion-off animation, resize exceptions or stuck controls.
Every lead has an indexed disposition in `audit-responses.md` and `audit-response-index.json`:
115 repeated rows fixed through four causes; 466 accepted as intentional opaque overlays,
the specified phone/six-rule scrolling, or permitted first-hint skips/cuts. No unreviewed row remains.

- Fixed decorative label/curb overlap in compact sizes, preserving the street art and hit areas.
- Fixed 9 px curb text and record headers to 10 px. `fix-audit-followups/audit-fix-680.png`
  through the 800/1000/760 frames and `audit-record-font.png`; Back to rules ends at y=352.19
  in the 680x425 record, above the power row at y=377.
- Fixed the phone's power-panel occlusion at its cause: the 375x812 scrolling work area now
  ends at y=698 and the separate 114 px power row begins there. A scrolled Add rule ends at
  y=637.47; a focused rule ends at y=446.47. `phone-scrolled-rules.png`, `phone-focused-rule.png`
  and `post-audit-verified.json` prove the controls remain above the panel.
- Also guarded the initial hint while Manual is open (`manual-first-voice.json`: no speech),
  and checked two ambulances together: the second vehicle's stop is latched at 0.5 s even
  while the first keeps moving. Original ambulance setup still stops; top-priority setup does not.
- Matched privacy copy to `kit/curio.js`: only Motion persists; Sound and rules are page-lifetime.
  Removed an unnecessary, unconfirmed publication year from the secondary-source reference.

The audit used the frozen `audited-src.html` / `audited-bundle.html`. The four new causes and
small follow-ups were then rechecked in one focused 11-shot drive, zero errors, and visually
inspected. The full audit was not repeated. Final bundle: 451,208 bytes; hashes in `validation.json`.
No external resource attributes or HTTP resource entries in the instrument. Chrome and host
ports 9920..9927 and 8725 are closed (`port-cleanup.json`).

## The real material

- FHWA MUTCD 2009 4D.26, 4D.27: https://mutcd.fhwa.dot.gov/htm/2009/part4/part4d.htm
- FHWA MUTCD 2009 4E.06, 4E.08: https://mutcd.fhwa.dot.gov/htm/2009/part4/part4e.htm
  Public domain, explicitly stated at https://mutcd-dr.fhwa.dot.gov/knowledge/faqs/faq_general.htm.
  Fetched 2026-11-06; originals and record in `data/`. Historical timing facts only, no traffic dataset.
- Independent cross-check: Minnesota DOT Traffic Signals 101 Course Manual,
  https://www.dot.mn.gov/trafficeng/signals/docs/signals-101-manual.pdf. Reference only;
  no text, figures or dataset incorporated. It confirms 7 s WALK, 3.5 ft/s clearance example and
  roughly 3..6 s yellow guidance. No current engineering-compliance claim is made.
- `verify_sources.py` recomputes 35 / 3.5 = 10 s. Half-second loop, fixed-speed driver,
  two-second yellow decision, traffic scripts and fairness references are original Curio Class
  model choices: content CC BY 4.0, code MIT. No external traffic dataset was needed.
- Existing twelve OpenAI-generated illustrations retained, including all three marked people assets.
  Sources/licences are also in the Manual and tool.draft.json. CSTA identifiers remain reference-only
  in notes; no standards text or Code.org glossary wording is incorporated.

## Curiosity check and frames

The crossing is the working material: a curb press changes lamps, moving traffic and the firing tape.
A child can poke it without reading; an adult can explore priority, timing and the detector. The real
first-match controller is central, with explicitly simplified traffic. It works without a score or
finish line. These are assessments from the repair walks, not evidence of a separate timed ten-minute
student/adult study. The original art is preserved; the cabinet has its own controls and finish.

| Traffic Light Coder | Beat Lab reference, opened and played |
|---|---|
| ![Street controller](../../_scratch/traffic-light-coder/fix-latest/latest-default.png) | ![Beat Lab](../../_scratch/traffic-light-coder/fix-phone-models/model-beat-lab.png) |

Looked at all targeted before/after frames directly or on `fix-contacts/` contact sheets, including
every standard size, all five setups at 1366x768, held input, picker, records, replay, zero/six rules,
Motion off and grayscale. Beat Lab was played; Elements Inspector was opened and searched. All 92 audit frames
were also inspected on the 12 `fix-audit-contacts/` contact sheets, plus the 11 focused follow-up frames.
Source and voice lesson-creep searches have zero matches; src.html has no header or em dashes.
Computed text contrast from the actual CSS: ink/panel 12.83:1, muted/panel 5.17:1, plate 6.23:1,
power 11.03:1, firing letters at least 4.57:1 (`contrast.json`, original code/CSS, MIT).
The idle/live browser measured 60 fps (`fps.json`); this is this machine, not a Chromebook benchmark.

## Left open

- Owner assignment of the Curiosity number; the maker's plate omits an unassigned number and metadata plate is null.
- The legacy spec, its voice table and Done when ladder are not rewritten; conflicting lesson requirements are
  explicitly superseded here. The module's combined standards coverage needs the owner decision described in notes.
- No separate timed ten-minute student/adult study, Chromebook hardware run or fresh people-art review was performed.
- Accepted Polish 13 is intentionally omitted. No new Yellow too long unsafe kind or walker-spacing change.
- One earlier phone harness requested its own missing favicon, producing a host 404; that was a harness issue.
  The corrected host has a data favicon, and the final phone drive has zero errors. All tool resources are bundled.
- No commits, no refine.md edits and no shared-engine/docs/other-tool edits. Every substantive command after setup
  used the Scratch timeout wrapper: bundle 120 s, drive 300 s, audit 2400 s; downloads 15 s each.
