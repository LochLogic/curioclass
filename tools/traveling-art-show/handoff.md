# Traveling Art Show build handoff

## Structure

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

## Art and narration

The ten original assets were made during the build with the built-in OpenAI image tool. Prompts are in `art/prompts.json`;
selected raw PNGs are in `art/raw`. Only `art.py --rekey <name>` processed them. The library was edited to empty
the case and pedestal; the museum was edited to remove direct sunlight. Cold review added the eleventh asset, a librarian,
and redrew the bridge photo. The librarian is marked people:true. Hand hazard icons are code. All assets are used.
Source credits name OpenAI gpt-image.

No audio was recorded, as required. The curious-librarian (Aoede) voice choice and fixed lines are in `voice/lines.json`.
The browser voice currently speaks. The cold reviewer should inspect the queue with held input at a two-second pace.

## Decisions and numbers

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

## Storage

Only the current show index and the four shows' progress, selected works, placements, protection, labels, optional label
ideas and completion are saved under `traveling-art-show`. Storage reads and writes are guarded. Explore is unsaved.
Start show over replaces only the current show's saved progress. The kit separately stores shared Motion preference.

## Engine changes wanted

None. No family engine is specified and the shared kit was not edited.

## Next review

Use the final report for evidence and any remaining audit leads. Check whether the material distinctions, seasonal
placement choices and damage feedback make students explain their choices. Do not treat the one-month model as a
forecast for a particular real pigment or object. The supplied spec remains unchanged.

## Build audit closure

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

## Cold review changes, 2026-11-04

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

## Review audit closure

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
