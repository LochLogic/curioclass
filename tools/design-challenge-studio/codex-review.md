# Codex review: design-challenge-studio



## Played

Cold, as a Grade 12 solo student: all three briefs and four stations, wrong tree placement, classroom combinations, failed water order, own evidence, saves and trade-offs. Then a projection read of the states. The live winner flip is the strongest moment.
## Findings fixed

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
## Findings left

- **Should fix, general, specification decision:** clear-source chemical-then-filter receives the same combined rating as filter-then-chemical. This follows the supplied combining rule, but CDC guidance specifies filtering first. Documented in notes and handoff; changing the model needs a spec decision.
- **Nit, specification:** twenty named assets versus the stated twenty-one; insulation computes to 37.10 degrees versus one 37.09 listing. Spec left untouched.
## Flattest moment left

The default Criteria sort still begins pre-populated. Its Check now exposes how many priorities weigh and how many gate, with a next action; saving also gives a named result. The sharpest discovery remains the earned winner flip.
## Graphics

All twenty named assets checked at rendered sizes; no people, lettering placeholders or missing art. One asset redrawn and re-keyed; 375.4 KiB of finished art. Bundle 705,384 bytes (688.9 KiB), below 2 MB.
## Audit

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
## Left open

Browser speech fallback remains; recording audio is prohibited in this workflow. No classroom test. The automatic control walk covers the discovered first screen, since shared mode discovery does not recognize the separate station nav. Nine explicit station recipes and targeted input/voice checks cover those paths. Phone model detail scrolls within the stage while intervention controls remain visible.
No commits. Authored changes stay in the two allowed folders. Generated image delivered to the image tool's default folder and copied into tool art. Review-owned Chrome and host processes are closed; temporary host.html is absent.
