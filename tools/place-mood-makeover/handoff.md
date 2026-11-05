# Place Mood Makeover handoff

## Current structure

src.html owns the studio frame, gallery, layered places, SVG compass, stable controls, clue dialog and storage.
content.json is bundled through json:content and contains the supplied weights, detail positions and line catalog.
A template contains each art token once; runtime images reuse its data URI. All 41 images are referenced.
The kit supplies Read, Motion, Sound and the mode-scoped Curio.voice queue. There is no family engine.
window.__tool exposes state, setMode, allLines, vlog, V, activeClues, effective, isDone and content for checks.

## Rules that matter

Every positive weight is a pull. Strong 2 and some 1 branches stay visible; a clue with no goal pull is dashed.
A tag alone never overrides the Reader. A nonempty reason, trimmed to 100 characters, redirects it to that tag.
Reselecting the same tag keeps its reason. Replacing/removing a clue removes its interpretation.
Place changes carry time, light, colors and weather, restore the destination's own details and writing, and clear
interpretations for global clues whose values were replaced. Start over clears only the current place.
Writing opens after agreement, stays open on repeated Write taps, and hides during a conflicting revision while
retaining its saved text. Agreement restores it. Partner view hides goal, compass, clues, mood title and writing.
Every revision clears the old partner result. No sound effects or music are used for this visual-mood lesson.

## Cold review changes, 2026-11-04

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

## Independent checks

All 44 nonzero clue vectors match the spec; all ten supplied contrast ratios match to rounding. Every mood has a
positive option in each treatment category and at least two details per place. The old build-report claim that Light
has no Calm choice is incorrect: Cool has Calm weight 1. The spec needs no correction.
Browser checks complete all 15 place/goal pairs, reject empty reasons, redirect a defended clue, retain a repeated
tag, gate and restore writing, conceal partner clues, reload saved text and reset only the current place.
Keyboard-only gallery play, grayscale, Motion off, a real divider drag and held voice input were inspected.
Final held voice counts: five tug starts, five agreement starts, one compassHow in five repeated actions.

## Audit and evidence

The one final review audit completed within its 40-minute limit: 284 leads, 97 inspected frames. No runtime errors,
stuck resize controls, repeat-voice failures or quick-tap failures were found. Its report precedes the last repairs.
Confirmed phone/compact click obstruction, hint visibility, compass crop and artist/partner fold issues were fixed.
Twelve targeted states, a phone-writing recheck and the final voice recheck verify the affected code. No full rerun.
See Scratch review-audit/audit.md, review-audit-dispositions.md, review-post/, review-writing-recheck/ and
review-voice-final/. review-functional-results.json and review-numbers.json hold independent assertions.
Native modal coverage, divider labels over their track, correct one-clue grammar, and first-tap own-line welcome
skips account for false positives. Every grouped audit lead is answered in the disposition file.

## Known limits and spec conflict

The explicit compact strip scrolls, as do secondary actions/clues and lower phone details. Showing all 44 px choices,
ten details, the 16:9 picture and compass simultaneously conflicts with that prescribed layout. The picture/hint stay
available on the phone; primary laptop/compact controls remain usable. No new navigation or challenge mode was added.
The blank Plain studio remains deliberately open for the student's first artistic choice.
No narration was recorded, as instructed. Browser speech remains the fallback; soft-breath/Enceladus is specified.

## Engine changes wanted

No shared file was changed. The prior request for magenta despill in scripts/art.py cut_out remains an optional
pipeline improvement; clean-alpha regeneration works around it here. No tool engine change is required.
