# Codex report: traveling-art-show

## Built

- Built the offline grade 3-5 tool with Look around, three preset Shows, Your show, and Library and museum.
- Eight illustrated works, ten spots, three months, protection, labels, growing damage, repair and saved progress.
- Real dragging, tap-card/tap-spot placement, numbered keyboard navigation, Read, Motion and Sound.
- Source uses the kit and starts from its starter. No family engine is specified.
- All required files are present. Stage is built in tool.draft.json; the tool remains a draft for cold review.
- No commits, publishing, shared-file edits or separate polish round.
- Final JavaScript syntax check and browser smoke: PASS, 50 lines, 10 spots, zero runtime errors.
- Final source formatting was checked to change whitespace only. Maximum line length: 169 characters.
- Temporary host.html removed. Started Chrome instances and servers closed.

## Numbers check

- Preset safe placements: 1,560, 768, 336, independently enumerated before implementation.
- Counting protection variants separately: 348,624, 186,624, 27,864. The spec counts placements once.
- All nine custom combinations are solvable. Our Town in June has 240 safe placements.
  Thus the spec's "at least 336" applies to the presets, not every custom combination. Spec unchanged.
- Window month: 30,000 lux × 4 hours × 30 days = 3,600,000 lux hours.
- Museum day: 50 lux × 8 hours = 400 lux hours; window daily dose is 300 times this.
- Fade-range calculation: 219,000 to 2,920,000 lux hours for 1.5 to 20 years, 365 days/year, 8 hours/day.
- 50 / 500 = 0.1, so the gallery light level is a tenth of the example office level.
- Contrast ratios match: 8.59, 7.64, 14.13, 5.93, 10.85, 6.40 and 15.89 to one.
- Evidence: Scratch numbers.json and custom-solutions.json. Supplied source claims were retained.

## Feel check

- Best moment: a bowl cracks while protected paper survives, followed by a repaired six-work show with six fine results.
- Flattest moment 1: reading eight small cards. Expanded the selected illustrated material/subject card,
  added tappable enemy explanations, and made the crate and main action fit compact screens.
- Flattest moment 2: waiting through the month. Calendar and three damage stages show its progress;
  repaired tap-through handling so any tap ends the wait without triggering a second action.
- Played all three preset shows through to six fine works, including a keyboard-only Show 1.
- Snowy Mail Route and Beat Lab were bundled into Scratch and opened. Their folders were untouched.
- Viewed feel-comparison.png: final successful show beside Beat Lab. The painted setting, material textures,
  frames and visible damage meet the graphic bar. Label entry remains the quietest part of play.

## Done when

1. PASS: library is the largest illustration at 1366×768, 680×425 and 375 wide; spot targets remain at least 44 px.
2. PASS: all 30 spot/month entries match the table. One renderer selects each local loop from that table.
   S3 heat is January only; S9 sun is June only; S8 changes from none to sun to hands.
3. PASS: held-input checks named both misfits and their reasons for each of the three themes.
4. PASS: shared evaluator checks pastel/sleeve on S5, pastel/glass on S4, and every sun-sensitive work
   with every protection on S1. Actual sleeve and window damage also appear in the timed run.
5. PASS: observed damage levels .34 at day 10, .67 at day 21, and 1 at day 30.
   A held tap skipped a new run and stayed at results. Reset/run tokens and voice hush remove stale work.
6. PASS: all three shows completed with six fine results. Fix and run again preserved placements.
7. PASS: a deliberately wrong, available material choice produced the visitor sticky note.
8. PASS: protection how-to spoke once across five placements at a two-second held-click pace;
   the same damage event spoke on both runs. Read checks and audit repetition checks passed.
9. PASS: Show 1 completed using Tab, Enter, arrows and native material-menu keys only.
10. PASS: guarded storage holds show progress and placements, including their protection and labels.
    Actual reset cleared the current show. The kit separately remembers Motion.

## Wave lessons

- Hint and voice: PASS. Hints update synchronously; Read uses the hint; Curio.voice handles heard/stale lines.
  Reopened step 4 now names Open the show; revealed placement steps name the artwork and spot controls.
- Focus and layout: FAIL in one compact visual detail. Focus is stable, but one caption touches its own work
  by 11×12 px at 680×425. Captions ignore pointer input. See Left open.
- Sizes: PASS for target dimensions, readable hints and primary controls at the required sizes.
  Sticky instructions retain the hint, steps and primary button while long label/result lists scroll.
- No giveaways: PASS before Check my six. Theme ticks/crosses appear only after the specified check.
  Hazards appear after Look around this month. Material names are reference information for making labels.
- Honest numbers: PASS. The one-month dose is described as a teaching model; assumptions are in notes.
- Standards: PASS. Students select against criteria, protect/place/label works, and compare the two venues.
- Motion off: PASS. Audit found no infinite animation. The month still takes eight seconds and ends at day 30.
- Short choices stay visible: PASS for initial eight-card crates and five comparison controls.
  FAIL to establish every compact custom-show feedback extreme; that remains a cold-review check.
- Resize mid-animation: PASS. Full audit found no exceptions or controls left disabled.
- Deferred welcome: PASS. No welcomeAfter. Card/spot actions correctly supersede the Look around welcome.
- Unknown shown as unknown: PASS. Unrequested hazards have no safe/unsafe badge.
- One look, one meaning: PASS. Shared enemy icons, gold selected ribbons, and icon-plus-word result chips.
- Badge says what is true: PASS. Placement counts update per move; edited completed shows lose their success badge.
- Hint changes back: PASS. Month/mode/step changes replace hints immediately and invalidate old previews.
- No answer by copying words: PASS for placement. Students test a material against a location and protection;
  the label task deliberately uses the supplied material names as reference information.

## Audit leads

- Ran the full audit once, last in the main check sequence: completed in about 26 minutes, 116 leads.
- No runtime errors, resize exceptions, stuck controls, infinite calm animation, repeat-how or quick-tap failures.
- Phone S3/S6 and S7/S8 overlap leads: separated the markers; final phone default and label snapshots
  have no spot overlap, hidden text, small targets or sideways scroll.
- Repeated hazard-badge overlaps: replaced word badges with small labeled symbols and packed them around targets.
- Repeated caption/number/work overlaps: packing now includes buttons, mounted works and number markers.
  Final laptop labels are clean. Compact labels improved to the one own-work contact recorded above.
- Below-fold Previous/Restart/Next leads: occasional navigation remains scrollable. A successful run now has
  a visible Next show button before the result list; Fix and run again stays the primary action.
- Compact Your show focus lead: show changes reset panel scroll and focus Check my six. Its initial crate is visible.
- Eighteen skipped Look around welcomes: intentional. The spec makes that welcome stale after a card or spot action.
- Dropped placement how-to after Look around this month: intentional stale trigger. The revealed step has a new hint.
- Final phone label-scroll overlap flags describe content passing under the opaque sticky instruction group.
  The hint and Open the show remain visible; the currently edited lower labels remain reachable.
- The temporary outer iframe host requested favicon.ico and received 404. The bundled tool has no external resources.
- Automatic audit mode discovery only finds header modes. Comparison was checked manually at every required size,
  including held taps across its rows. Added an explicit comparison state and corrected phone state size strings.
- Those expanded audit states and targeted repairs were not subjected to another full audit.
- Evidence: Scratch audit/audit.md, post-final.log, last.log, functional.log, damage-fixed.log and voice.log.

## Frames looked at

- Builder frames: initial-frames, initial-fixed, size-frames, more-frames, phone-fixed, final-affected,
  functional-frames, voice-frames, post-frames, post-fixed, post-final, last-frames, compare-rest, compare-taps, smoke.
- Full audit: all 35 frames inspected in audit-contact.png; compact fears and both result frames also opened full size.
- Historical post-fixed frames inspected in a contact sheet; final affected frames opened individually.
- Both bar frames, the side-by-side feel comparison, and every finished asset at its saved size were viewed.
- All evidence lives under _scratch/traveling-art-show/.

## Art made

- Ten final images: library, museum and eight works. Built-in OpenAI image generation; no people.
- Library edited to empty the case and pedestal; museum edited for even light.
- Cutouts rekeyed with edge despill; the heron and weaving also use hole-aware keying.
- 452.6 KiB finished art. Final self-contained bundle: 827,473 bytes, 808.1 KiB.
- Prompts: art/prompts.json. Selected originals: art/raw/. Final assets: art/*.webp.
- Only the free art.py --rekey form was used for processing. All ten images are displayed.

## Art still to paint

None. No audio was recorded, as required; curious-librarian is selected in the 50-line voice manifest.
Current audible narration uses the browser fallback.

## Engine changes wanted

None. No kit or family engine changes were made.

## Left open

- One compact Library Cat caption touches its own artwork; full information is available by selecting the work.
- Compact Your show feedback extremes need a cold layout check beyond the verified initial eight-card state.
- Previous show and Start show over can require scrolling beneath long results. Main actions stay available.
- Short comparison views and phone label entry use vertical scrolling.
- The full audit predates targeted repairs and the expanded audit-state file. It was not rerun.

