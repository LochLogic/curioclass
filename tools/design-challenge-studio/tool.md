# Design Challenge Studio: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: design-challenge-studio

#### Built

Four open stations for three Grade 12 engineering challenges. Two browser simulations, an editable tree and sort, four saved designs, weighted scaling, live Flip finder and a session-only Why box. Own challenge persists locally and has a clear control.
Kit starter, Curio.voice and the 9-12 theme. No network requests, recordings, commits, deployment or polish round. Authored project files stayed in the two authorized folders. Generated images were copied from the image tool's default delivery location.

#### Numbers check

Independent Python: all 256 room sets; all 1,296 four-criterion weight combinations. Browser room values match Python exactly. Worked totals 60.0, 96.1, 95.5, 39.9 and all three specified flips pass.
Insulation rounds to 37.10, versus 37.09 in one spec line. The named art list contains twenty assets, despite saying twenty-one. Spec left unchanged.
0.81 pounds per kWh converts to 0.3674098 kilograms, consistent with rounded 0.367. 6,500 feet converts to 1,981.2 meters, consistent with about 2,000 meters. Social statistics were retained from the supplied spec, not re-derived from source datasets.
Contrast: brand/panel 11.61:1; brand/section 11.00:1; brand-ink/brand 12.18:1; text/card 13.12:1; muted/card 7.25:1.

#### Feel check

Best moment: lower the hours weight from three to two and Design 3 takes the top tag, while Flip finder immediately reveals the changed priorities.
Flat moment 1: cause placement originally just moved text. Added a short snap animation, a matching tone and illuminated intervention chips, without grading student-authored cards.
Flat moment 2: water protection initially changed abruptly and crowded the last bar. Kept stable bar elements for animated fills, added painted ordered steps, and corrected the space budget.
Played the student path through tree placement and checking, sorting, testing options, saving designs and flipping the winner. Later designs require a different trade-off, rather than repeat a fixed quiz.
Compared the 1366 prototype with Beat Lab side by side in S:/CurioClass-codex/_scratch/design-challenge-studio/bar-comparison.jpg. The studio's large painted context and dimensional intervention tiles meet the visual bar while retaining an evidence-focused instrument layout. Snowy Mail Route was also bundled in Scratch and opened as the feedback reference.

#### Done when

1. PASS: baseline 38.6408 degrees, 7.00 hours, 7.30 kWh.
2. PASS: AC 26.5394 degrees, zero hours, 31.0103 kWh. Saved AC row is excluded with named electricity and budget failures.
3. PASS: specified set costs $3,900; 33.8225 indoor, 31.3225 feels-like, 3.55 hours, 6.88 kWh. Trees give 3.50 hours and not ready.
4. PASS: fans 8.98 kWh; fans with lights off 6.88 kWh.
5. PASS: cloudy chlorine [0,0,2,2]; settle then chlorine [1,0,3,3]; microfilter then chemical [4,4,4,4]. Words match the spec's scale.
6. PASS: Design 2 top at 96.1 versus 95.5. Flip targets [2,2,4,none] for hours, feels-like, cost, ready. All-zero tie. Real keyboard flip reaches Design 3.
7. PASS: Check tree explicitly marks Students are too loud as not part of the heat problem.
8. PASS: tree, sort, chart and comparison table dominate their respective stages at 1366 and 680.
9. PASS: thirty immediate option changes peaked at 6.6 ms including redraw. The model has no animation lock; flip highlighting is a replaceable CSS effect.
10. PASS: actual reload retained title, branches, placed custom card, criteria and saved design. Clear removed the localStorage key. Why was absent from storage.
11. PASS for all twenty named images and visible station tabs/main actions at 1366 and 375. FAIL for the literal twenty-one count: no twenty-first asset is named in the spec. All twenty named assets were inspected and contain no people.
12. PASS: held clicks at two-second pace gave each how line once over five changes, all three fail events spoke, and one design used wTradeEmpty, never wTrade. Read interrupted and read the current hint. Browser speech fallback; no listening review of recorded Gacrux clips because recording was prohibited.

#### Wave lessons

- Hint and voice: PASS, immediate hints, state-valid welcome keys, kit Read and queue, current-state event guards, held-input logs.
- Focus and layout: PASS for stable toggles, sort controls and weights. Mode tabs and action buttons stay mounted. Keyboard tree placement and weight changes retain focus. Dialog close is handled by the browser and returns to its connected trigger.
- Sizes and targets: PASS for main controls at all eight required sizes, including a true 375 by 812 iframe. Minimum button and number-field targets are 44 pixels. Compact sliders retain 44-pixel height.
- No giveaways: PASS within the specified explorer format. No hidden-answer quiz or score farming was added. Fit-linked chips are explicitly required by the spec.
- Honest numbers: PASS, model assumptions and invented costs are labeled; unknown custom-design values display No value and cannot set a scale.
- Standards: PASS, a solo student performs decomposition, criteria/constraints, simulation and weighted evaluation. No family engine applies.
- Motion off: PASS, no infinite animations remained in the driven calm state; button timing and voice stay unchanged.
- Short choices: PASS for initial tree decks, classroom interventions and water sources/steps in compact layouts. Longer feedback, model detail and wide custom tables can scroll inside their regions.
- Resize mid-animation: PASS, completed audit reported no exceptions or disabled controls left behind. Room redraws are synchronous and the ResizeObserver reconstructs the chart at actual pixels.
- Welcome after first action: PASS, no welcomeAfter queue; each station welcome has a current-state guard.
- Unknown as unknown: PASS, missing new custom criteria are excluded rather than treated as evidence of zero.
- One look, one meaning: PASS, line dash patterns and word ratings survive grayscale; pass/fail and top/tie always use words.
- True badges: PASS, ready, electricity failure, top and tie come from current numeric state.
- Reversible hints: PASS, tab entry immediately replaces the hint and direct actions name the next available control.
- No answer by copied words: PASS, tree feedback appears after Check; the broader task is constructing and defending an open design decision.

#### Audit leads

The full attempt on Chrome 9981 lost its connection during resize after sixty frames. One smaller retry on unused Chrome 9987 completed with the optional control walk omitted. Both attempts used host port 8785 on loopback address 127.0.0.2; shared audit code was not edited.
Completed report: S:/CurioClass-codex/_scratch/design-challenge-studio/audit-retry/audit.md. Nineteen grouped leads: eighteen fixed and one false positive. Every entry is answered in S:/CurioClass-codex/_scratch/design-challenge-studio/audit-dispositions.md.

- Fixed three phone card overlaps by bounding scrollable card text and giving Start its own row. Briefs are keyboard focusable.
- Fixed Start focus loss in all seven state recipes by focusing the first station tab with preventScroll.
- Fixed the forty-three-pixel constraint input with a hard forty-four-pixel minimum; checked at both 375 and 760.
- Added an explicit Why aria-label matching its existing associated label.
- Fixed six water bar/result overlap leads at 680 and 800 by reserving bar height and compacting step/source controls. All four bars and all treatment choices stay visible; result detail can scroll.
- The phrase Design 1 becomes top is a design identifier, not a count mismatch. This is the one false positive.
Targeted follow-up checks reuse the audit's PAGE_JS for affected states only. Their small-target, overlap and unnamed-control lists are empty, with visible unclipped hints and no page overflow. Final keyboard, Escape and held-click Clear checks pass. The full matrix was not repeated a third time.
S:/CurioClass-codex/_scratch/design-challenge-studio/audit-snapshot-to-final.diff and final-tool.html preserve the completed audit snapshot-to-delivery changes.

#### Frames looked at

Both bar frames; all first, check, functional, extreme, voice, last-functional, matrix, focused-fix, audit, post-audit and valid final phone frames, directly and in labeled contact sheets. S:/CurioClass-codex/_scratch/design-challenge-studio/frames-looked-at.json lists the frame paths. Invalid phone frames from the other build and the file-origin experiment were identified as test-harness failures and are not passes.
The complete size matrix ran once. Only states affected by a fix were re-shot. Final phone result detail may scroll within the stage while all intervention controls and the primary action remain visible. Compact Flip finder scrolls separately so Why stays visible.

#### Art made

Sixteen new named paintings with the built-in image tool; four existing paintings retained. Two treatment images redrawn once for key spill. All fourteen object assets were re-keyed with the approved free art.py form, with despill and holes processing as appropriate.
Twenty final WebPs, 384,148 bytes (375.1 KiB). Bundle 699,463 bytes (683.1 KiB), below 2 MB. Prompts and raw originals are preserved. preview.svg is drawn in code.

#### Art still to paint

None among the named assets. The spec's count discrepancy needs an editorial decision, not an invented extra asset.

#### Engine changes wanted

No kit change. handoff.md also requests checkpoint reports before resize stress so interrupted audits retain completed leads. Optional audit mode-discovery improvement in handoff.md: recognize the spec's station navigation below the header so mode control walks can reach it automatically. Explicit states and separate input tests cover it here.

#### Left open

The full automated control walk has no completed aggregate report because the first audit connection closed during resize; the successful smaller retry omitted that walk. Separate held-input, keyboard, voice, drag and functional checks passed. Cold review can repeat the full walk. Source claims were used as supplied without internet refresh. New recorded narration was intentionally not made. The spec names twenty images while saying twenty-one. Cold review is next; no polish or commit was started.

All build-owned Chrome and host processes are closed; tools/design-challenge-studio/host.html is absent. The other build's 127.0.0.1 host was left alone. Closure evidence: S:/CurioClass-codex/_scratch/design-challenge-studio/closure.json.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: design-challenge-studio



#### Played

Cold, as a Grade 12 solo student: all three briefs and four stations, wrong tree placement, classroom combinations, failed water order, own evidence, saves and trade-offs. Then a projection read of the states. The live winner flip is the strongest moment.
#### Findings fixed

- **Should fix, general, custom tree/Criteria:** implicit text inputs rendered as tiny browser defaults. Added explicit types and common styling, 44 px targets, visible select focus, compact custom Criteria layout with Add item in view.
- **Should fix, general, Reset narration:** a rapid second Reset on the start screen cut the welcome. Reset now leaves an already-reset screen in place; the complete welcome starts once and is not cut.
- **Should fix, general, keyboard/Reset:** moving a card or hiding the studio could lose focus. Placement restores the moved card; Reset focuses the matching Start control with preventScroll.
- **Should fix, general, Criteria:** a typed out-of-range limit could silently differ from the active limit. Invalid values are flagged and explain the retained limit; valid edits recover the instruction. Germ limits show High rather than an unexplained rating number.
- **Should fix, general, hints:** returning to custom/water Prototype named option tiles that do not exist; empty custom evidence invited saving. Contextual hints now name the actual controls and route an empty challenge to Criteria.
- **Should fix and polish, general, saving:** own saved rows stayed absent until leaving the station. Saved rows now update immediately, retain active inputs and show missing evidence as No value. The hint names the saved design and the next action; custom saves have their own matching narration.
- **Should fix, general, water time:** Trade-offs used minimum contact-time estimates without saying so at the comparison. Minimum is now in the criterion name and its assumption is stated beside the table and results.
- **Should fix, general, compact comparison:** a three-digit total could wrap mid-number. Compact totals stay on one line and the phone badge wraps into its own row.
- **Should fix and polish, general, Check sort:** its completion line omitted a next control, compact layouts hid its feedback, and its default result was only a match count. Added an explicit next action and a visible summary of weighted criteria versus hard constraints.
- **Polish, general, graphics:** redrew the microfilter with an identifiable pump, strainer and separated tubing. Kept the rich classroom, cutouts, grid, charts and restrained senior-grade finish.
#### Findings left

- **Should fix, general, specification decision:** clear-source chemical-then-filter receives the same combined rating as filter-then-chemical. This follows the supplied combining rule, but CDC guidance specifies filtering first. Documented in notes and handoff; changing the model needs a spec decision.
- **Nit, specification:** twenty named assets versus the stated twenty-one; insulation computes to 37.10 degrees versus one 37.09 listing. Spec left untouched.
#### Flattest moment left

The default Criteria sort still begins pre-populated. Its Check now exposes how many priorities weigh and how many gate, with a next action; saving also gives a named result. The sharpest discovery remains the earned winner flip.
#### Graphics

All twenty named assets checked at rendered sizes; no people, lettering placeholders or missing art. One asset redrawn and re-keyed; 375.4 KiB of finished art. Bundle 705,384 bytes (688.9 KiB), below 2 MB.
#### Audit

One full audit finished within its 40-minute limit on Chrome 9951 and host 8755: 76 frames, eight sizes, nine explicit states, Motion off, held clicks, repeats, rapid taps and resize stress. All audit frames inspected. Four grouped leads: Reset repaired; explicit input name added; Design 1 grammar and timestamp-ID resize comparisons dismissed with direct evidence. Evidence: _scratch/design-challenge-studio/review-audit/.
Only the touched states were re-shot after the final fixes. Their audit probes show no small targets, missing names, overlaps, clipped text, hidden choices or cut hints. No full audit rerun. The initial phone harness favicon 404 and two scratch probe mistakes were isolated and corrected; final targeted runs report zero console errors.
Independent Python matches fourteen classroom cases, including all single options and worked combinations. Totals 60.0 / 96.1 / 95.5 / 39.9; three specified flips and zero-weight tie verified. AC fails energy and budget and is excluded from normalization.
Voice counts (events at 6 s spacing; water how across five actions at 2 s spacing):

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| flip | event | 5 | 5 |
| fail | event | 5 | 5 |
| wProtoWater | welcome/how | 1 | 1 |

 Read interrupts and uses the current hint; first Read gives only Read, first Sound is silent, first stage tap gives welcome. allLines and lines.json agree.
Keyboard placement and jittered real drag pass; reload retains own challenge and Clear removes storage; Why is absent from persisted work. Motion off has zero infinite animations; grayscale retains line styles and word labels. Phone iframe checked at actual 375 px.
#### Left open

Browser speech fallback remains; recording audio is prohibited in this workflow. No classroom test. The automatic control walk covers the discovered first screen, since shared mode discovery does not recognize the separate station nav. Nine explicit station recipes and targeted input/voice checks cover those paths. Phone model detail scrolls within the stage while intervention controls remain visible.
No commits. Authored changes stay in the two allowed folders. Generated image delivered to the image tool's default folder and copied into tool art. Review-owned Chrome and host processes are closed; temporary host.html is absent.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Design Challenge Studio handoff

Build only. No commits, deployment, or polish round.

#### Source map
src.html starts from the kit starter. It uses kit:curio and kit:theme-912. Styles adapt the studio wall, four stations and painted option tiles. Data, model functions, station renderers and input handlers follow in that order. Only station changes replace whole layouts; live options, sliders and sort buttons remain in place during their input.

The art bank ensures each painting is bundled once and reused by rendered controls. prompts.json preserves the four existing assets and records sixteen generated assets and raw originals. There are twenty named assets in the spec, despite its stated twenty-one count.

window.__tool exposes the required state plus the two model functions, scoring, Flip finder, save action and voice log. Scratch contains independent Python arithmetic, browser recipes and evidence. The kit handles sound, motion and narration. No recordings were made.

#### Tricky parts
The heat model uses explicit Euler steps of sixty seconds for three days. Air conditioning applies only when the current room temperature exceeds 26 degrees and is capped at 10.5 kW and the energy needed to reach 26 after passive gains. This reproduces the spec's 26.54 degrees and 31.01 kWh.

Only passing designs establish each column's normalization range. Full precision is retained until display. The all-equal rule assigns ten, including a one-design scale; the UI still asks for two designs before comparison. A tie changes the Flip finder outcome. The smallest integer distance wins; equal distances search down before up.

Cloudy water chemical protection drops unless a cleaning step precedes it. Microfilter followed by disinfection gets the specified combined rating. The clear-source combination is symmetric. All saved water designs retain their source and step order.

Water totals use the sum of the listed step times, the highest ordinal cost level, any fuel requirement and the least favorable taste category. The spec does not give a complete numerical cost or taste aggregation. These are labeled classroom categories rather than sourced money or measured taste. Chlorine dioxide shows the possible longer contact-time total as well as the minimum batch estimate.

Local storage is guarded with try/catch. Student text is escaped before insertion into markup. The Why explanation is never persisted. Device storage can be unavailable in a managed school browser.

#### Open questions resolved
- Keep Challenge 3 saved locally, as the spec leans. Show that it never leaves the device and provide Clear my challenge. The Why box remains session only.
- Keep the invented, rounded room and option costs. Label these classroom assumptions on screen and in teacher notes rather than substitute real procurement data.
- Keep the water simulation framing, local-guidance note, no nitrate/lead-removal warning, high-altitude boiling note and product-label waiting caveat. This does not claim to validate actual household treatment.

#### Engine changes wanted
No kit engine change is required. Shared kit and scripts were not changed.

Optional audit helper change: scripts/audit_tool.py, MODES_JS. Include .station-nav button[data-station] in mode discovery, retaining the current header selectors. The spec puts station tabs below the header, so automatic mode control walks do not discover them. Seven explicit audit states plus separate held-input runs cover them here.

Optional audit resilience change: scripts/audit_tool.py, run. Save a checkpoint report after size, state, calm and control-walk phases, before resize stress. A later Chrome disconnect currently loses all accumulated lead results even when all sixty screenshots already exist. Preserve completed checks on an interrupted connection.

#### Build verification notes
The named art set is twenty assets: the retained classroom, stream, river and rain-barrel paintings, plus sixteen new assets. The two water treatment paintings with key spill were redrawn once. Finished art totals about 375 KiB.

The independent Python run checked all 256 room combinations and all 1,296 four-criterion weight combinations. Browser room outputs matched Python at full precision. The insulation value rounds to 37.10 degrees, compared with 37.09 in one spec line. The room update and redraw peaked below 7 milliseconds in the thirty-action probe.

Changing the comfort line recalculates every saved room design at the same threshold, so the hours column remains comparable. Existing custom designs missing a newly added item display No value and are excluded until replaced with complete evidence.

The shared host at 127.0.0.1:8785 was serving another build during later phone checks. Invalid phone frames are preserved as failed test evidence. Valid final phone checks use a local srcdoc iframe with the real 375 by 812 viewport. The mechanical audit uses the same assigned host port on 127.0.0.2 via a Scratch wrapper that changes only the test host address. The other build's server was left alone.

#### Final audit handoff
The full attempt on Chrome 9981 lost its connection during resize. One smaller retry on unused Chrome 9987 completed, omitting the optional control walk. It produced nineteen grouped leads: eighteen were fixed and verified in targeted states; the phrase Design 1 becomes top was a false count warning. The automated full control-walk aggregate remains a cold-review check, while separate real-input, voice, keyboard, drag and model checks passed.

Scratch/audit-dispositions.md answers every lead. Scratch/audit-snapshot-to-final.diff preserves the completed audit snapshot-to-final changes. Scratch/build-evidence.json records the final bundle hash and size. Scratch/frames-looked-at.json lists the inspected frames. All Scratch references mean S:/CurioClass-codex/_scratch/design-challenge-studio/.

#### Review next
Cold review against spec.md and codex-report.md. No polish round has started.

#### Cold review changes
Untyped custom inputs now share the 44-pixel input styling; the compact custom Criteria form stays visible. Card placement restores focus; Reset returns focus to its challenge card. Invalid limits keep the last valid value and explicitly say so, with word ratings beside the germ limit. Returning hints name controls for the actual challenge, including an empty custom-evidence state.
Saving now names the saved design immediately and refreshes the custom table without replacing the active input. Missing custom evidence is printed as No value. New narration lines are in voice/lines.json. The microfilter was redrawn for a simpler silhouette and distinct tube paths, with its old WebP preserved in Scratch.
Water time comparisons explicitly use minimum estimates. Spec question left open: clear-source chemical-then-microfilter gets the combination bonus under the supplied rule, while current CDC guidance specifies filter then disinfect. Do not silently change that teaching rule without revising the spec.

#### Cold review final audit
The single full review audit finished on Chrome 9951, host 8755. Four grouped leads: Reset could cut the first welcome on a rapid second tap, now fixed by leaving the already-reset start screen in place; an implicit input label was made explicit; Design 1 becomes top is valid grammar; the custom resize lead compared timestamp IDs between fresh pages. A focused live-iframe resize confirmed the same controls remain connected and enabled.
Final targeted checks cover these changes and the Check sort summary/action, visible compact feedback, single-line compact totals, and phone table badge wrapping. They pass. The full matrix was not repeated after these small repairs. Browser speech remains the fallback; no audio was recorded. See codex-review.md and Scratch/review-audit/audit.md.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
