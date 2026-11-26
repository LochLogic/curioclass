# Place Mood Makeover: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: place-mood-makeover

#### Built

Offline Grades 3-5 visual arts studio: three artist readings, three places, five goals, all supplied treatment
weights, thirty painted details, clue tagging and reasons, a live compass, partner guessing, before/after, and
two saved reflection sentences. Uses the kit and Curio.voice. No family engine. No commits or polish round.
Source is readable; no source line exceeds 180 characters. Metadata stage is built; tool remains a draft.

#### Numbers check

All ten supplied contrast ratios match independent WCAG calculations within rounding: 11.031, 9.692, 13.854,
5.658, 15.768, 7.090, 5.927, 6.537, 5.905 and 9.396. See numbers.json in Scratch.
The source's category-wide reachability claim is too strong: Light has no Calm choice. All 15 actual three-clue
completion paths exist and were driven in the browser. The supplied weights and spec were left unchanged.
Every positive weight is a pull; branches show strong (2) and some (1), with a visible conventions statement.

#### Feel check

Played all three artists through Make your own, then built a night scene and defended the lost glove as Cozy:
“Someone will return for it to this warm little stop.” The gold compass recognized that intention, and both
reflection sentences saved. That was the best moment: an unexpected clue can belong when the artist explains it.
The two flattest moments were tiny compass labels in the preview and detail cutouts floating above their places.
I enlarged compact labels to at least 10 rendered pixels and corrected the glove, swing, crow, feeder and lamp
placements. Earlier sky images containing landscapes were redrawn so time changes work as a layered scene.
feel-comparison.png places the final studio beside Beat Lab at the same viewport. Both frames were inspected;
the painted picture, brass compass, immediate transformations and personal clue record meet the visual bar.
Later rounds can change the goal, place, clue combination and defended interpretation without repeating a puzzle.

#### Done when

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

#### Wave lessons

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

#### Audit leads

The single full audit finished with 148 mechanical leads. All 81 frames were inspected. The complete row-by-row dispositions are in _scratch/place-mood-makeover/audit-responses.md.
Fixed overlapping artist hit regions, colliding tug text, the reason input name/label spacing, compact hint cropping, and the compact artist reveal/Next layout. Kept the specified detail strip and intentional modal/wipe overlays.
Phone/compact fold and keep-region limits, plus the compact modal Close scroll, remain open. Five first-tap welcome skips follow STANDARDS; Reset on an already Plain place is intentionally unchanged.
The full held-control walk, repeat/quick-tap samples, Motion off and resize tests had no runtime/focus/stuck-control failures. No full audit was rerun after the scoped fixes.

#### Frames looked at

Both bar frames; four final-art inspection sheets; quick and functional frames; 29 size/extreme/input frames in
frames-sheet-0 through frames-sheet-7; all four student frames; all five final frames; and feel-comparison.png.
Selected 680, 375, full-size artwork and all-detail frames were also opened individually. Failed early driver
recipes were corrected for selector quoting and remembered place; only affected shots were retried.
All 81 full-audit PNGs were inspected in audit-sheets/audit-sheet-0 through audit-sheet-13. Five scoped post-audit frames verify the fixes, reflection card and wipe-label behavior. A writing-card recipe was added for the cold reviewer after the full audit. Phone reason and reflection were also inspected in two clean 375 pixel iframe shots.

#### Art made

41 final generated images, 1,351,270 art bytes (1,319.6 KiB). Bundle: 1,905,500 bytes (1,860.8 KiB), under 2 MB.
All 41 are referenced, all have drawn_by: codex. Six assets were redrawn: four skies and the porch and bus-stop
plates. Built-in imagegen was used; prompts and provenance are in art/prompts.json, PNG originals in art/raw,
and the final assets in art/*.webp. All sizing/keying used the permitted art.py --rekey form.
The bus plate's supplied alpha is preserved through the sizing pipeline after a targeted image-tool edit.

#### Art still to paint

None. No people were generated. The glove is an empty clothing item, not a hand.

#### Engine changes wanted

No family engine change. scripts/art.py cut_out could support magenta scene hue despill and preserve supplied
alpha; tinted glass and wire edges retained magenta in the first keyed bus plate. A local alpha edit works around it.

#### Left open

- Phone lower controls and reflection need scrolling; compact secondary actions and clue chips need local scrolling.
- Browser speech is active; soft-breath/Enceladus is specified in the manifest but no audio was recorded, as instructed.
- The rapid-tap stale-event limit above remains for the cold reviewer. No full audit was repeated.
- Small colored edge flecks remain on the bus plate's distant roof and wire edges; assess them at full size in review.
- The snowy-mail-route reference bundle command regenerated its ignored preview in that tool's folder. This was a
  write outside the requested boundary; all authored source, art, documentation and evidence stayed in this tool/Scratch.
- Known audit findings remain: scroll/fold/keep-region limits, the specified compact detail strip, and a Close button that needs modal scrolling at 680x425 while the reason field is shown. See the exhaustive audit response index.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: place-mood-makeover

#### Played

Cold Grade 4 play before builder notes covered all three wrong artist guesses and clue reveals, all places,
an earned Cozy picture, opposing clue tags, partner guessing, divider and the writing card. Later checks verified
kept reasons and saved writing. Also checked projector framing. The best moment is defending the glove as Cozy.

#### Findings fixed

- **Blocker, general, phone/compact interaction:** a pinned studio covered scrolled controls, so goal/light taps,
  clue cards, Partner guess and Write could miss. Phone scroll insets now protect targets; compact studio pinning is
  removed. The phone picture, compass and hint stay available. Real held-click completion and modal checks pass.
- **Should fix, general, layout:** Weather crowded its label; compact targets were narrow; 1000x625 cut the compass;
  phone Next and compact partner choices crossed the fold. Fixed spacing, widths, scene fitting and compact cards.
- **Should fix, general, clue card:** scrolling the reason hid its title/Close. A sticky heading keeps both accessible.
- **Should fix, general, teaching state:** old partner results survived revisions; writing stayed visible after
  agreement failed; replaced global clues retained old interpretations. Cleared stale results/tags and gated writing
  while preserving saved text. Same-tag taps retain reasons; Write stays open on repeat taps.
- **Should fix, general, guidance/focus:** last artist still named Next; closing the divider kept its old hint;
  artist transitions could leave focus behind. Fixed current hints and deliberate focus with preventScroll.
- **Should fix, general, voice:** tugs could wait behind a welcome, and removed clues could keep speaking. Current
  events take priority and stale speech stops while Read remains protected. Plural subjects and all Read hints are
  cataloged consistently in content.json and voice/lines.json.
- **Should fix, general, art:** floating/overlapping details, a projecting shop window, mismatched lamp head and pink
  plate edges weakened the scene. Redrew four assets and anchored/separated details, chains, ground art and glows.
- **Polish, general, payoff:** the gold compass alone was flat. The student's completed picture now gains its own
  mood title and gold frame. Partner guessing hides those cues. The original paintings and rich studio remain.

#### Findings left

- **Should fix, general, spec conflict:** the explicit compact strip and lower phone/secondary scrolling conflict
  with the standing all-choices-at-once rule. Preserved the prescribed layout and art; a different navigation model
  needs a spec decision. Every control remains reachable. No other confirmed blocker or should-fix remains.

#### Flattest moment left

The Plain studio still waits for the student to choose a mood and make the first clue. A preset or challenge would
change the open sandbox specified here, so none was added.

#### Graphics

Inspected all 41 assets and all three composed detail sets at final size; none shows people or a placeholder.
Regenerated bus-window, bus-broken-lamp, place-porch and place-playground with built-in imagegen, then art.py --rekey.
Prompts/provenance: art/prompts.json; originals: art/raw/. Art 1349.9 KiB; final bundle 1915.0 KiB.
Compared the studio beside Beat Lab and opened Snowy Mail Route. Evidence: Scratch review-feel-comparison.jpg.

#### Audit

One audit completed within 40 minutes: **284 mechanical leads; all 97 frames inspected** in 17 contact sheets.
Confirmed scroll/click obstruction, cropped compass, hidden hint and fold leads were repaired; targeted real inputs
reach the intended controls. Modal/background and divider-label overlap, correct "1 pulls" grammar, and five
first-tap own-line welcome skips are explained in Scratch review-audit-dispositions.md. The specified scrolling
constraint remains above. Resize stress found no exceptions/stuck controls; repeat and quick-tap samples were clean.
Rechecked 12 affected states, phone writing (both fields visible), and the changed voice paths. No second full audit.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Light Cool tug | event | 5 | 5 |
| Every clue points to Cozy | event | 5 | 5 |
| compassHow | how | 1 | 1 |

Independent checks: all 44 clue vectors and ten contrast ratios match; browser paths complete all 15 place/mood
pairs. Empty/kept reasons, tag retention, partner concealment, reload, per-place reset, keyboard-only play,
grayscale, Motion off and a real divider drag pass. Notes have the required opening sections and all four standards
are practiced. Source/resource checks found no external requests; all 41 art tokens resolve. Test Chrome/server
processes are closed and host.html is absent. Evidence is under Scratch review-* and post-*. No commits.

#### Left open

The layout/spec conflict above; optional recorded soft-breath narration (recording forbidden in this pass).
The full audit precedes its targeted repairs, as the one-audit rule requires. No classroom trial was claimed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Place Mood Makeover handoff

#### Current structure

src.html owns the studio frame, gallery, layered places, SVG compass, stable controls, clue dialog and storage.
content.json is bundled through json:content and contains the supplied weights, detail positions and line catalog.
A template contains each art token once; runtime images reuse its data URI. All 41 images are referenced.
The kit supplies Read, Motion, Sound and the mode-scoped Curio.voice queue. There is no family engine.
window.__tool exposes state, setMode, allLines, vlog, V, activeClues, effective, isDone and content for checks.

#### Rules that matter

Every positive weight is a pull. Strong 2 and some 1 branches stay visible; a clue with no goal pull is dashed.
A tag alone never overrides the Reader. A nonempty reason, trimmed to 100 characters, redirects it to that tag.
Reselecting the same tag keeps its reason. Replacing/removing a clue removes its interpretation.
Place changes carry time, light, colors and weather, restore the destination's own details and writing, and clear
interpretations for global clues whose values were replaced. Start over clears only the current place.
Writing opens after agreement, stays open on repeated Write taps, and hides during a conflicting revision while
retaining its saved text. Agreement restores it. Partner view hides goal, compass, clues, mood title and writing.
Every revision clears the old partner result. No sound effects or music are used for this visual-mood lesson.

#### Cold review changes, 2026-11-04

Cold play preceded builder-file reads. The large artist paintings, original studio palette and all content remain.
Four assets were regenerated with built-in imagegen: flat shop-window insert, curved bell lamp head, and clean-alpha
porch and playground plates. Other details were resized, anchored and separated. Puddles and chalk follow the ground
plane; swing chains reach the beam; lamp-glow art is masked to its head. Prompts and provenance are in art/prompts.json.
No people appear because these are intentionally empty places and absence is part of the art-reading lesson.
A completed picture gains a gold frame and its chosen mood in its title; Partner guess conceals both cues.

Phone layout pins the picture, compass and hint. ResizeObserver measures their combined height into --studio-inset,
so nearest scrolling and keyboard focus put controls below them. Do not restore the former extra 335 px scroll margins.
Phone writing scrolls to its card's start, with both fields visible below the picture at 375x812.
Compact landscape keeps the primary rows in the panel, with the specified scrolling detail strip; its smaller hint
sticks while secondary work scrolls. The large compact studio must not be sticky: it formerly blocked clue/partner
clicks. At 1000x625 the scene's responsive width leaves the whole compass in view. Laptop details use three columns.
The compact dialog heading and Close stay visible; partner cards fit. Sound reserves its laptop label width.

Current tug/agree events take priority over older instructions. A removed tug stops; Read remains protected.
How-to lines use V.heard. Artist clue lines expire on reveal; completing all three directs the learner to Make your own.
Next artist and Make your own transfer focus with preventScroll. Closing the divider restores the current action hint.
Plural detail subjects use pull. voice/lines.json includes fixed speech and all finite dynamic Read hints.

#### Independent checks

All 44 nonzero clue vectors match the spec; all ten supplied contrast ratios match to rounding. Every mood has a
positive option in each treatment category and at least two details per place. The old build-report claim that Light
has no Calm choice is incorrect: Cool has Calm weight 1. The spec needs no correction.
Browser checks complete all 15 place/goal pairs, reject empty reasons, redirect a defended clue, retain a repeated
tag, gate and restore writing, conceal partner clues, reload saved text and reset only the current place.
Keyboard-only gallery play, grayscale, Motion off, a real divider drag and held voice input were inspected.
Final held voice counts: five tug starts, five agreement starts, one compassHow in five repeated actions.

#### Audit and evidence

The one final review audit completed within its 40-minute limit: 284 leads, 97 inspected frames. No runtime errors,
stuck resize controls, repeat-voice failures or quick-tap failures were found. Its report precedes the last repairs.
Confirmed phone/compact click obstruction, hint visibility, compass crop and artist/partner fold issues were fixed.
Twelve targeted states, a phone-writing recheck and the final voice recheck verify the affected code. No full rerun.
See Scratch review-audit/audit.md, review-audit-dispositions.md, review-post/, review-writing-recheck/ and
review-voice-final/. review-functional-results.json and review-numbers.json hold independent assertions.
Native modal coverage, divider labels over their track, correct one-clue grammar, and first-tap own-line welcome
skips account for false positives. Every grouped audit lead is answered in the disposition file.

#### Known limits and spec conflict

The explicit compact strip scrolls, as do secondary actions/clues and lower phone details. Showing all 44 px choices,
ten details, the 16:9 picture and compass simultaneously conflicts with that prescribed layout. The picture/hint stay
available on the phone; primary laptop/compact controls remain usable. No new navigation or challenge mode was added.
The blank Plain studio remains deliberately open for the student's first artistic choice.
No narration was recorded, as instructed. Browser speech remains the fallback; soft-breath/Enceladus is specified.

#### Engine changes wanted

No shared file was changed. The prior request for magenta despill in scripts/art.py cut_out remains an optional
pipeline improvement; clean-alpha regeneration works around it here. No tool engine change is required.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
