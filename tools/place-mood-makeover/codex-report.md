# Codex report: place-mood-makeover

## Built

Offline Grades 3-5 visual arts studio: three artist readings, three places, five goals, all supplied treatment
weights, thirty painted details, clue tagging and reasons, a live compass, partner guessing, before/after, and
two saved reflection sentences. Uses the kit and Curio.voice. No family engine. No commits or polish round.
Source is readable; no source line exceeds 180 characters. Metadata stage is built; tool remains a draft.

## Numbers check

All ten supplied contrast ratios match independent WCAG calculations within rounding: 11.031, 9.692, 13.854,
5.658, 15.768, 7.090, 5.927, 6.537, 5.905 and 9.396. See numbers.json in Scratch.
The source's category-wide reachability claim is too strong: Light has no Calm choice. All 15 actual three-clue
completion paths exist and were driven in the browser. The supplied weights and spec were left unchanged.
Every positive weight is a pull; branches show strong (2) and some (1), with a visible conventions statement.

## Feel check

Played all three artists through Make your own, then built a night scene and defended the lost glove as Cozy:
“Someone will return for it to this warm little stop.” The gold compass recognized that intention, and both
reflection sentences saved. That was the best moment: an unexpected clue can belong when the artist explains it.
The two flattest moments were tiny compass labels in the preview and detail cutouts floating above their places.
I enlarged compact labels to at least 10 rendered pixels and corrected the glove, swing, crow, feeder and lamp
placements. Earlier sky images containing landscapes were redrawn so time changes work as a layered scene.
feel-comparison.png places the final studio beside Beat Lab at the same viewport. Both frames were inspected;
the painted picture, brass compass, immediate transformations and personal clue record meet the visual bar.
Later rounds can change the goal, place, clue combination and defended interpretation without repeating a puzzle.

## Done when

1. FAIL across all action states: the initial view has a dominant place and visible compass at 1366x768, 680x425
   and 375x812, but reaching lower controls or the divider can scroll the scene out of view on compact/phone sizes.
   Initial evidence: final-frames/gold-final.png, compact-makeover-final.png and phone-clean.png.
2. PASS: all 15 place/goal pairs complete with three clues. functional-results.json records each path.
3. PASS: opposite tags show the Reader's reading; empty reasons are rejected; a kept reason redirects the arrow
   and can complete the goal. functional-results.json and student-makeover.json record both behavior and text.
4. PASS: all five glow details get night glow, Gray desaturates, and Fog covers the far scene. The browser checks
   inspect the selected styles; scene and compass updates run synchronously in the change handler.
5. PASS: all three artists reveal their intention and four clues after two finds even with a wrong Calm guess.
6. PASS: controls work during weather; Motion off has zero running infinite animations in calm-night.
7. FAIL: how-to repetition is prevented, but a tug can go stale during a longer welcome at a two-second tap pace.
   voice-five.json records one how line, one stale tug and two spoken repeats. Event lines are not once-only.
8. PASS: Partner guess hides goal, compass, chips, controls and reflection until a mood is selected, then restores
   the studio and compares readings. Functional assertions and partner.png cover the hidden state.
9. PASS: makeovers, tags, reasons and both sentences reload; Start over clears only the current place.
   reload-results.json checks a retained other-place record and the exact saved reason and sentences.

## Wave lessons

- Hint and voice: FAIL on rapid-event coverage as described above. Hints update synchronously and Read uses them.
- Focus and layout: FAIL for the scrolled scene/hint regions above. Stable main buttons and clue button roots;
  no load focus. Keyboard artist reading reaches
  two finds using only Tab and Enter. Compact hints were moved below the compass so the next action stays visible.
- Sizes: FAIL on the strongest all-controls-without-scrolling rule. All specified sizes were framed, but phone
  lower rows and compact secondary actions need scrolling. The compact ten-detail strip follows the explicit spec.
- No giveaways: PASS. Neutral artist labels; choose a mood before clue finding; intention appears after two finds.
- Honest numbers: PASS. Reader conventions and branch-weight legend are visible, with no measured mood score.
- Standards: PASS. Solo learners try moods, revise or explain, read three artists, and connect to their own place.
- Motion off: PASS. Rain, snow, wind leaves, idle sky and lamp flicker stop; calm-night has no infinite animation.
- Short choice lists: FAIL for compact details as required by this spec's scroll strip; mood choices stay grouped.
- Resize mid-animation: PASS. Full audit: no exceptions and nothing left disabled after every state input and the sampled control clicks..
- Late welcome: PASS. Mode-scoped kit queue; stale welcomes are invalidated and first-action own lines skip the welcome.
- Unknown shown as unknown: PASS. Unfound picture regions have neutral accessible names; no clue text on hover.
- One look, one meaning: PASS. Dashed means tug, thick/thin means strong/some, and an asterisk means your reason.
- Truthful badges: PASS. Gold uses the actual three-clue rule and kept reasons; guesses report the actual selection.
- Hint changes back: PASS. Mode, place, reset and partner transitions set their current next action immediately.
- No copying answer words: PASS. Initial artist cards and neutral region names do not name the intended mood.

## Audit leads

The single full audit finished with 148 mechanical leads. All 81 frames were inspected. The complete row-by-row dispositions are in _scratch/place-mood-makeover/audit-responses.md.
Fixed overlapping artist hit regions, colliding tug text, the reason input name/label spacing, compact hint cropping, and the compact artist reveal/Next layout. Kept the specified detail strip and intentional modal/wipe overlays.
Phone/compact fold and keep-region limits, plus the compact modal Close scroll, remain open. Five first-tap welcome skips follow STANDARDS; Reset on an already Plain place is intentionally unchanged.
The full held-control walk, repeat/quick-tap samples, Motion off and resize tests had no runtime/focus/stuck-control failures. No full audit was rerun after the scoped fixes.

## Frames looked at

Both bar frames; four final-art inspection sheets; quick and functional frames; 29 size/extreme/input frames in
frames-sheet-0 through frames-sheet-7; all four student frames; all five final frames; and feel-comparison.png.
Selected 680, 375, full-size artwork and all-detail frames were also opened individually. Failed early driver
recipes were corrected for selector quoting and remembered place; only affected shots were retried.
All 81 full-audit PNGs were inspected in audit-sheets/audit-sheet-0 through audit-sheet-13. Five scoped post-audit frames verify the fixes, reflection card and wipe-label behavior. A writing-card recipe was added for the cold reviewer after the full audit. Phone reason and reflection were also inspected in two clean 375 pixel iframe shots.

## Art made

41 final generated images, 1,351,270 art bytes (1,319.6 KiB). Bundle: 1,905,500 bytes (1,860.8 KiB), under 2 MB.
All 41 are referenced, all have drawn_by: codex. Six assets were redrawn: four skies and the porch and bus-stop
plates. Built-in imagegen was used; prompts and provenance are in art/prompts.json, PNG originals in art/raw,
and the final assets in art/*.webp. All sizing/keying used the permitted art.py --rekey form.
The bus plate's supplied alpha is preserved through the sizing pipeline after a targeted image-tool edit.

## Art still to paint

None. No people were generated. The glove is an empty clothing item, not a hand.

## Engine changes wanted

No family engine change. scripts/art.py cut_out could support magenta scene hue despill and preserve supplied
alpha; tinted glass and wire edges retained magenta in the first keyed bus plate. A local alpha edit works around it.

## Left open

- Phone lower controls and reflection need scrolling; compact secondary actions and clue chips need local scrolling.
- Browser speech is active; soft-breath/Enceladus is specified in the manifest but no audio was recorded, as instructed.
- The rapid-tap stale-event limit above remains for the cold reviewer. No full audit was repeated.
- Small colored edge flecks remain on the bus plate's distant roof and wire edges; assess them at full size in review.
- The snowy-mail-route reference bundle command regenerated its ignored preview in that tool's folder. This was a
  write outside the requested boundary; all authored source, art, documentation and evidence stayed in this tool/Scratch.
- Known audit findings remain: scroll/fold/keep-region limits, the specified compact detail strip, and a Close button that needs modal scrolling at 680x425 while the reason field is shown. See the exhaustive audit response index.
