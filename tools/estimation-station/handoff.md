# Estimation Station handoff

## Build
One offline HTML tool, Freight and Yard. Source starts from the kit starter, uses kit CSS, Curio.voice, Curio.init and kit chimes. No family engine is specified. No commits, publication, recordings or polish round.

## Source map
The source contains responsive station CSS, a persistent header/panel, content and art maps, the Freight state machine, tool suitability and scoring, SVG drawing, and pointer/keyboard input. content.json is loaded through the bundler's json token. Art uses art tokens only. voice/lines.json holds expanded utterances and the requested gravel-ranger / Algenib recording identity; current audio uses browser fallback.

state.offset and state.moved are in the asked unit, so resizing preserves a placement. The native ruler ticks stay in inches or centimeters even when the question asks for feet or meters. Curves use sampled arc length. The first choice fixes a stamp once. Checks require physical readiness as well as a typed reading. A result is committed once; abandoned runs never write storage. The ghost is frozen at run start so saving a finished run cannot change its opponent retroactively.

Short tools on a ribbon pair return to an existing chalk mark when needed to read the shorter ribbon. The initial zero alignment is preserved. The two-unit turn rescales existing mark positions and labels rather than erasing the marks. Yard's Show me demonstrates aligned zero, the asked face and the final measured piece. Read includes the current question and, for an unsolved order, the story and current equation.

## Spec choices and discrepancies
- No unanswered owner questions are listed. No print-and-carry feature was added.
- Two-unit descriptions list fixed directions but Done when asks for both directions. Each chosen two-unit item randomizes direction.
- Under the disclosed uniform-item, uniform-length weighting, ordinary inch and centimeter pools give different guessing averages from the Sources commentary. See Scratch numbers.txt; those narrow pools do not establish the whole-run average. The explicit bands win; very short objects remain intentionally easy.
- Its blanket unit-swap-zero claim conflicts with those bands on tiny lengths. A guess of 3 for a 1-inch item earns 1 star; a guess of 1 for 2 centimeters earns 3. Numeric guesses cannot reveal which unit a child had in mind. The explicit scoring formula is preserved.
- The cold review accepts positive guesses only. All content lengths and the spec's random-guess domain are positive. A zero-only tap shortcut now stays at the guess step without points; the explicit bands are unchanged for accepted guesses. This is the unattended interpretation of the input domain.
- All 15 slips regroup. All answers and ribbon gaps recompute correctly.
- A one-unit square beside a 1-inch object filling most of the scene cannot also fit at that scale. Such cases use an accurate one-unit segment, with no misleading rescaled square. Broad objects keep their aspect ratio, which can reduce the requested 55 to 80 percent width fill.
- A 150-pixel lens at 4 times magnification cannot show both points when zero starts 2 large on-screen units away. It shows local graduations as zero approaches. Exact magnification and placement are preserved; Nudge remains available.
- Ribbon and order jobs follow their explicit flows without an estimate; the generic instruction that every crate begins with a guess applies to the first five jobs and the second-unit estimate.
- Check requires a matching order layout as well as the story answer. Otherwise typing the correct story answer without modeling the story bypasses the number-line action.
- The scene reflows recap cards into rows. Small recap panels scroll while New run and Yard remain available.
- The preview and phone use 44-pixel pad/control targets as the explicit spec permits. The full laptop controls use 60 pixels.
- The five-wrong-Checks voice instruction conflicts with the two-attempt limit within one job. Extra Checks after a result do nothing and cannot add points.
- The tape's nominal end marks are 60 inches and 150 centimeters as specified. Those marks are not exact physical equivalents. Cross-system conversions are not taught.
- BUILD.md's older "Do not draw art" line and the spec's Gemini routing conflict with the user's image-tool request and CODEX-BUILD.md. The user request and CODEX-BUILD.md win: OpenAI gpt-image was used, including for people, as ART.md permits.

## Sensitivity
Mr. Hollis is a friendly older Black station master. All three people assets are marked people: true. He is shown as the knowledgeable guide, with consistent attire and dignified expressions. There are no claims about culture, bodies, religion or history. The three poses are on _scratch/estimation-station/people-contact-sheet.png for the owner and the fresh representation check in the later cold review. This Build does not claim that independent review has happened.

## Art
44 original generated paintings, processed only with art.py --rekey. Snake head was redrawn once to remove an unwanted whole coiled body. All specified images are referenced. Raw originals remain in art/raw as the build brief requests. Final art sheets and the people contact sheet are in Scratch. Art credit is in tool.draft.json and the source comment.

## Engine changes wanted
None. No kit, docs, scripts or other tool was intentionally edited.

## Remaining voice limits
The cold review gives the first number tap its short guess instruction and gives the first result its Next cue before optional result detail. How lines use the kit's heard set; tool names remain repeatable events. Order introduction and placement share a scope so placing a piece does not discard its story. Read still includes the current story and equation. Next interrupts obsolete narration as its new crate appears. The first welcome can be skipped, consistent with BASELINE 16.

See codex-review.md and Scratch review-main-voice.json for the final held-click walk and observed counts. Recorded speech is still absent. Muted Chrome establishes queue behavior, not audible narrator quality or an independently observed child's comprehension. A student listening to an order must have time to hear its story before answering; the review waits for that question while keeping taps two seconds apart.

## Cold review repairs

The second estimate keeps the first unit's markings and hides secondary-unit numerals in both directions. Correct ribbon results retain the ribbons and their comparison arc. Tool icons now have shaded wood, metal, grain and readable capacity captions. Ruler labels thin with scale while every tick remains; standing-tool chalk labels stay beside the ruler. Skipping an outstanding measured piece receives Mark and move feedback instead of a false zero-alignment warning. Yard preserves the focused item across responsive shelf rebuilding and clears its previous answer when another tool is selected. Compact order bars sit below their paper. Resizing ends an active drag while preserving its unit position. Scissors grammar and Back's feedback tone were corrected.

Audit states now include a deterministic measuring fixture, a placed order, a ribbon result and a complete delivery. Test setup uses the existing content and production handlers; the separate voice walk uses held physical input through all eight jobs. No shared engine was changed.

## Next review
See codex-report.md for the builder's checks and codex-review.md for the separate cold review, repairs, evidence and remaining limitations. Keep this at Build until Refine.
