# Traveling Art Show: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: traveling-art-show

#### Built

- Built the offline grade 3-5 tool with Look around, three preset Shows, Your show, and Library and museum.
- Eight illustrated works, ten spots, three months, protection, labels, growing damage, repair and saved progress.
- Real dragging, tap-card/tap-spot placement, numbered keyboard navigation, Read, Motion and Sound.
- Source uses the kit and starts from its starter. No family engine is specified.
- All required files are present. Stage is built in tool.draft.json; the tool remains a draft for cold review.
- No commits, publishing, shared-file edits or separate polish round.
- Final JavaScript syntax check and browser smoke: PASS, 50 lines, 10 spots, zero runtime errors.
- Final source formatting was checked to change whitespace only. Maximum line length: 169 characters.
- Temporary host.html removed. Started Chrome instances and servers closed.

#### Numbers check

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

#### Feel check

- Best moment: a bowl cracks while protected paper survives, followed by a repaired six-work show with six fine results.
- Flattest moment 1: reading eight small cards. Expanded the selected illustrated material/subject card,
  added tappable enemy explanations, and made the crate and main action fit compact screens.
- Flattest moment 2: waiting through the month. Calendar and three damage stages show its progress;
  repaired tap-through handling so any tap ends the wait without triggering a second action.
- Played all three preset shows through to six fine works, including a keyboard-only Show 1.
- Snowy Mail Route and Beat Lab were bundled into Scratch and opened. Their folders were untouched.
- Viewed feel-comparison.png: final successful show beside Beat Lab. The painted setting, material textures,
  frames and visible damage meet the graphic bar. Label entry remains the quietest part of play.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

- Builder frames: initial-frames, initial-fixed, size-frames, more-frames, phone-fixed, final-affected,
  functional-frames, voice-frames, post-frames, post-fixed, post-final, last-frames, compare-rest, compare-taps, smoke.
- Full audit: all 35 frames inspected in audit-contact.png; compact fears and both result frames also opened full size.
- Historical post-fixed frames inspected in a contact sheet; final affected frames opened individually.
- Both bar frames, the side-by-side feel comparison, and every finished asset at its saved size were viewed.
- All evidence lives under _scratch/traveling-art-show/.

#### Art made

- Ten final images: library, museum and eight works. Built-in OpenAI image generation; no people.
- Library edited to empty the case and pedestal; museum edited for even light.
- Cutouts rekeyed with edge despill; the heron and weaving also use hole-aware keying.
- 452.6 KiB finished art. Final self-contained bundle: 827,473 bytes, 808.1 KiB.
- Prompts: art/prompts.json. Selected originals: art/raw/. Final assets: art/*.webp.
- Only the free art.py --rekey form was used for processing. All ten images are displayed.

#### Art still to paint

None. No audio was recorded, as required; curious-librarian is selected in the 50-line voice manifest.
Current audible narration uses the browser fallback.

#### Engine changes wanted

None. No kit or family engine changes were made.

#### Left open

- One compact Library Cat caption touches its own artwork; full information is available by selecting the work.
- Compact Your show feedback extremes need a cold layout check beyond the verified initial eight-card state.
- Previous show and Start show over can require scrolling beneath long results. Main actions stay available.
- Short comparison views and phone label entry use vertical scrolling.
- The full audit predates targeted repairs and the expanded audit-state file. It was not rerun.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: traveling-art-show

#### Played

Played cold as a grade 4 student before reading the builder's report, handoff, notes or source.
Explored spots, months, fears and previews; chose, placed, labeled and opened a failed show; inspected every mode and brief.
Then completed all three presets, checked projection layouts, real dragging, repair, held-tap skip and keyboard-only Show 1.
The strongest moment is watching a bowl crack while protected paper survives, then repairing the student's own arrangement.

#### Findings fixed

- Should fix, general, art/w6-photo: Our Bridge looked painted although it teaches inkjet photography.
  Redrew it as a photographic print with a white border and recognizable ducks; preserved the other strong artworks.
- Should fix, general, library scene: the librarian's workplace had no person. Added a painted librarian beside the desk,
  marked people:true, inspected hands and representation, and kept the figure inside the comparison picture at small sizes.
- Should fix, general, src.html narration: spot descriptions, placement refusals and other fixed speech were absent from
  allLines/voice manifest. Registered every fixed variant; both now contain 103 lines.
- Should fix, general, comparison: teaching facts repeated as events. Changed them to how lines, spoken once per page load.
- Should fix, general, Shows Place: tapping an empty spot could expose hazards before Look around this month.
  Kept hazards hidden until the specified reveal action; placement and refusal feedback remain immediate.
- Should fix, general, compact/custom Choose: feedback pushed the last cards out of view.
  Used compact title wrapping and theme badges; moved the duplicate medium-preview brief into the stage.
- Should fix, general, phone Place: the repeat Look around control was below the fold.
  Pinned it beside Make labels and fitted the room so the artwork tray remains visible.
- Polish, general, Label: six entries felt detached from the show. Added artwork thumbnails, an ungraded completion count
  and a complete live label beside the artwork. Measured remaining stage space so all 120 optional characters fit.
- Polish, general, compact captions: enlarged the Shows wall and omitted cramped bylines only where needed.
  Full labels remain available in the editor, live preview and tooltip. No art or damage effects were removed.

Teaching, Play and Craft checks included every BUILD.md wave lesson. Notes retain the required opening sections.
Independent counts: 1,560 / 768 / 336 safe preset placements; every custom combination is solvable.
Window dose: 3.6 million lux hours per month; daily window/gallery ratio: 300. All seven specified contrast ratios match.
Fresh checks of the linked CCI, Library of Congress and NEDCC sources support the supplied conservation model.
Pastel/sleeve smudging, glass failing against sun, seasonal hazards, all themes' misfit reasons and wrong-label notes passed.
Observed damage levels .34, .67 and 1; a held tap during the run reached day 30 immediately without selecting the spot.
Motion off retained the eight-second run. Grayscale, keyboard, real drag, saved progress and repair were checked.

| Voice line | Kind | Expected | Spoken |
|---|---|---|---|
| protectHow across placements | how | 1 | 1 |
| compare-1 in five taps | how | 1 | 1 |
| allFine in two completed runs | event | 2 | 2 |

#### Findings left

No confirmed blocker or should-fix remains. Compact labels and comparison facts use vertical scrolling.
Occasional Previous/Start show over navigation stays below long forms/results; frequent actions remain pinned.
Compact title ellipses are intentional; full accessible names and selected-work details remain available.

#### Flattest moment left

Labeling is still the quietest stretch. The live illustrated label and count now give each entry a visible result.

#### Graphics

Checked all 11 finished assets and final-size scenes. Redrew w6-photo; added librarian with the built-in image tool.
Prompts and provenance: art/prompts.json. Final assets: art/w6-photo.webp and art/librarian.webp.
Art totals 495.1 KiB; the self-contained bundle is 944,614 bytes, about 922.5 KiB.
Kept the painted rooms, material textures, protection reflections and damage overlays.
Viewed the Beat Lab and Snowy Mail Route reference frames; review-bar-comparison.png records the finish comparison.

#### Audit

Ran once, last full audit: Scratch review-audit/audit.md, Chrome 9961, host 8765, 40-minute limit; finished in about 29 minutes.
47 leads: fixed confirmed crate clipping and the phone repeat-reveal control; re-shot only affected states afterward.
Remaining leads describe scrollable forms/navigation, 18 welcomes correctly superseded by a card/spot's own line,
and placeHow becoming stale after Reveal. Fears-card room reflow leaves crate controls stable.
All eight default sizes were clean. No runtime errors, lost focus, repeated how lines, quick-tap failures or resize failures.
Opened all 51 audit frames; final affected desktop/phone frames and logs are in review-final-* and review-follow-phone/.
The full-label resize check passed 760x900 and back to 680x425 after a completed repaint. No second full audit was run.
Final syntax, notes, art-token and metadata checks passed. All started Chrome/server ports are closed; host.html is removed.

#### Left open

The spec's at-least-336 wording has one custom exception: Our Town in June has 240 safe placements. Spec left unchanged.
Recorded narration remains absent as required by the build rules; the browser fallback is used.
No engine changes, commits, publishing or edits outside the tool and its Scratch were made.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Traveling Art Show build handoff

#### Structure

`src.html` starts from the kit starter. It contains the responsive library, crate, comparison, data tables, rules and
state machine in one readable source. `Curio.voice` owns speech, Read, stale queues and heard-line tracking.
The mode and show form its scope. The tool writes its hint synchronously.

`WORKS`, `SPOTS` and `SHOWS` hold the specification's content. `damageFor` is the single damage rule used by previews,
month animation and results. `paintSpots` updates persistent numbered buttons without replacing them.
`renderPanel`, `renderDetail` and `renderCrate` own the contextual controls. Focus is restored with preventScroll.
The wall uses a real responsive 16:9 box. Markers keep 44-pixel targets and move slightly in short previews to separate.
The selected work's protection chips appear in the card immediately below the wall, with its title and picture.

The eight-second month uses a token-cancelled timer. Any tap or Enter/Space/Escape jumps to results; the following
click is swallowed so it cannot immediately start another action. Reduced motion retains the full eight seconds.
Damage overlays are code, over the same painted images: faded colors, yellow cast, curl, streaks, loops, crack and crush.
The two-second exploratory preview is cancelled when a newer preview, month or mode makes it stale.

#### Art and narration

The ten original assets were made during the build with the built-in OpenAI image tool. Prompts are in `art/prompts.json`;
selected raw PNGs are in `art/raw`. Only `art.py --rekey <name>` processed them. The library was edited to empty
the case and pedestal; the museum was edited to remove direct sunlight. Cold review added the eleventh asset, a librarian,
and redrew the bridge photo. The librarian is marked people:true. Hand hazard icons are code. All assets are used.
Source credits name OpenAI gpt-image.

No audio was recorded, as required. The curious-librarian (Aoede) voice choice and fixed lines are in `voice/lines.json`.
The browser voice currently speaks. The cold reviewer should inspect the queue with held input at a two-second pace.

#### Decisions and numbers

- The specification has no open questions.
- Safe placement counts were independently enumerated before building: 1,560, 768 and 336, agreeing with the spec.
  Counting protection variants gives 348,624, 186,624 and 27,864 instead. The spec's counts count each placement once.
- Light-dose computations and all seven specified contrast ratios match. Evidence: Scratch `numbers.json`.
- All nine custom theme/month combinations were also enumerated. Our Town in June has 240 safe placements,
  so the spec's "at least 336" statement applies to the three preset shows, not to every custom combination.
  The other custom counts are in Scratch `custom-solutions.json`. Every combination remains solvable.
- The user's image-tool request overrides the spec's local-FLUX production suggestion.
- The user's stop-on-report instruction overrides the generic early-report instruction. The report is written once,
  at the end. This is Build only, without a polish round, commits or changes outside this tool and its Scratch.
- Reference tools were bundled into Scratch with the original bundler's destination redirected in memory.
  Their source folders were never changed. Python commands use `-B` and disable imported bytecode writes.

#### Storage

Only the current show index and the four shows' progress, selected works, placements, protection, labels, optional label
ideas and completion are saved under `traveling-art-show`. Storage reads and writes are guarded. Explore is unsaved.
Start show over replaces only the current show's saved progress. The kit separately stores shared Motion preference.

#### Engine changes wanted

None. No family engine is specified and the shared kit was not edited.

#### Next review

Use the final report for evidence and any remaining audit leads. Check whether the material distinctions, seasonal
placement choices and damage feedback make students explain their choices. Do not treat the one-month model as a
forecast for a particular real pigment or object. The supplied spec remains unchanged.

#### Build audit closure

The single full mechanical audit completed in about 26 minutes on Chrome 9991 and host 8795. It returned 116 leads,
with no runtime errors, resize exceptions, stuck controls, infinite calm animations or repeated how-to narration.
Its source bundle predates the targeted repairs. The full audit was not rerun.

Repeated badge and label overlaps were reduced with symbol badges and real-pixel packing that also avoids work
buttons and numbered markers. One 11 by 12 pixel contact between the Library Cat caption and its own work remains
at 680 by 425 in the tested arrangement. Captions ignore pointer input so they cannot block spot buttons.
Full titles and artists are available by selecting the numbered work and in the label panel.

The phone spot overlap was fixed by separating S6 and S8. The compact Your show now resets focus and panel scroll to
Check my six and keeps its initial eight choices visible. Its feedback extremes still deserve a cold layout check.
The placement count updates after each move, and edited completed shows lose their current success badge at once.
Object baselines now meet the sill, shelf, pedestal and case. A successful run has a Next show button before its
result list. Previous show and Start show over remain accessible by scrolling the result panel.

The panel's sticky instruction group retains the hint, steps and main button while labels scroll, including on a
phone. Mechanical overlap flags against content passing under that group are intentional scroll occlusion.
The eighteen skipped Look around welcomes are specified behavior after a card or spot supplies its own line.
The queued placement instruction becomes stale when Look around this month is tapped, as the voice spec requires.

The audit's automatic mode discovery only reads header buttons. This tool's modes are in a separate navigation row,
so comparison was checked with drive.py at every required size. An explicit comparison audit state is now included.
The phone size strings in the audit states were corrected for the next review. Those added states were not part
of this full audit. The temporary iframe host generated a favicon 404; the offline tool itself has no resource links.

Evidence: Scratch `audit/audit.md`, `functional.log`, `damage-fixed.log`, `voice.log`, `post-final.log`, `last.log`,
`compare-rest/`, `custom-solutions.json` and `static-checks.json`. All started Chrome instances and servers were closed.

#### Cold review changes, 2026-11-04

Played before opening this handoff or source. Kept the library painting, artwork set, seasonal puzzle and damage rules.
Redrew w6-photo as a photographic inkjet print with recognizable ducks. Added a full-body painted librarian beside
the desk and in comparison, with people:true in prompts.json. Raw generated images are in art/raw; final images were
processed only with the free art.py --rekey form. The character has natural hands and an ordinary welcoming role.

Label entry now shows the selected work and its complete live label below the wall, including the optional sentence.
Label thumbnails and a completion count connect the form to the physical show. This count never grades the material.
Six labels remain a scrollable editing list; the main action stays visible. Narrow wall captions omit the artist only
when needed; the full title, artist and material remain in the label editor, preview and caption tooltip.
Compact custom feedback uses two-line titles and overlay theme checks to keep all eight choices visible.
The compact Shows wall is larger, and caption packing considers the smaller optional byline.
Label editing measures the detail card's actual height and fits the wall into the remaining stage height; this keeps
all 120 optional characters visible in the short preview. Resize observers only adjust this layout during Label.
The duplicate Choose brief moves to the stage at medium preview sizes to keep the full crate visible. The repeat
Look around this month control shares the pinned action row with Make labels, so it is reachable on phones.

All fixed spot descriptions, placement refusals, count feedback and undamaged preview lines are now registered in
allLines and voice/lines.json (103 lines). Comparison facts are how lines rather than repeating event narration.
The Show placement step does not reveal hazards by tapping an empty spot before Look around this month.

Independent recomputation: preset placement counts 1560/768/336, all nine custom combinations solvable, Our Town
in June 240. Contrast ratios 8.59/7.64/14.13/5.93/10.85/6.40/15.89. Window dose 3.6 million lux hours per month.
The spec's at-least-336 wording therefore holds for presets and has a custom-show exception; spec left unchanged.
Fresh CCI, Library of Congress and NEDCC source checks support the light, vent and pastel/glazing explanations.

Review evidence is in Scratch review-* files. Keyboard-only Show 1, repair preserving placements and instant skip
passed with no runtime errors. Voice counts: protection how 1, comparison how 1 in five taps, success event 2 in two runs.
No recordings were made. Narration still uses the browser fallback. No shared files or git commits were made.

#### Review audit closure

The single review audit completed in about 29 minutes on Chrome 9961 and host 8765, with 47 mechanical leads.
All default sizes, calm mode, held-control focus, repetition, quick taps and resize stress had no runtime failures.
Confirmed crate clipping at 1000x625 and the repeat-reveal control below the phone fold were repaired.
The other leads are normal vertical label/result forms, occasional navigation below them, the specified skipped
Look around welcomes after artwork/spot actions, and placeHow becoming stale when Reveal is tapped.
Room controls moving when the larger fears card opens are intentional reflow; crate controls remain stable.

Only affected states were re-shot after the audit. Final desktop/phone logs have no console errors or warnings.
The full 120-character live label fits at 680x425, 1366x768 and on a phone; its completed-frame resize check passes
760x900 and back. A first headless reading before repaint was stale; the completed frame and geometry are correct.
All three preset shows reached six fine works; held skip reached day30 immediately and did not activate the spot.
Wrong labels produce visitor notes and each theme names both misfits. The three damage stages were visible.
Review evidence: review-audit/audit.md, review-final-desktop/, review-final-phone/, review-follow-phone/,
review-label-resize.png and review-keyboard/result.json in Scratch. There was no second full audit.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
