# Handoff: Roller Coaster Rounding

## Built
Three modes cover rounding, place-value addition and subtraction within 1000, and multiplying tens. Nine Line cards, four clerk checks and seven Train cards are freely selectable. Generated rider cards alternate rounding place and require regrouping on at least two cards in each group of three. No student work or completion counts are saved.

## Source map
`src.html` starts from the shared starter and retains kit CSS, Motion, Sound, Read, tones and `Curio.voice`. Tool CSS defines the fairground and compact controls. The script has the voice table, fixed cards, tool-local number-line adapter, Track rendering, Line state machine and ticket trades, Trains rendering and answer stages, and static control wiring. `window.__tool` exposes state and actions for review. Fixed voice text is in `voice/lines.json`; recordings were intentionally not made.

## Tricky parts
- `stopAction` invalidates asynchronous rolls and laps. A mode, value or card change acts immediately. The line that opens the ride completes before the four-second lap begins.
- Addition needs a correct raw column count before a bundle is available. Next column refuses an unbundled count of ten or more. Subtraction needs a legal Take away before it accepts the remainder. Extra breaks can be reversed with a bundle, so optional correct trades cannot trap the student.
- Breakable ticket columns are large keyboard targets; painted pieces inside are countable but do not create dozens of tiny targets. A strip consists of exactly ten individual ticket images. Source rows are separate until the current count is entered.
- Fixed-card completion uses sets, so replaying a card cannot inflate the board. Practice feedback deliberately permits correction, as the spec requires. The board records activity, not independent mastery.
- Track uses an enlarged adjacent-station segment so a single rounding hill, its car and its two platforms stay readable. Cold review added a ten-hill overview, with the close interval highlighted and a live car marker. Its coordinates use the same local number-line adapter. Overview input is handled separately so it cannot also fire the close-track tap handler.
- SVG redraw preserves a focused element by id. Pointer dragging reads the persistent stage rectangle, not an SVG node that a redraw replaced. Panel controls precede scene controls in DOM tab order.

## Decisions and contradictions
- No open questions are listed in the spec. This unattended build needed no owner response.
- The spec asks for a new shared engine and a shared family-doc correction. The user's two-folder write boundary wins. A tool-local adapter supplies the needed API instead.
- The narrative says an ordinary roll takes about 1.2 seconds; Done when says within one second. The ordinary roll is one second; a halfway roll adds the one-second teeter. Reduced motion retains those timings.
- A 520 by 300 ticket bin cannot fit the 405-pixel preview stage or a 375-pixel phone. The three columns reflow at their available pixel size while the panel controls remain visible.
- The close segment and the full ten-hill window now appear together. Animated Tens/Hundreds zoom remains open; both views redraw synchronously and retain the held value.
- The intro concept mentions 40-seat cars, but the detailed spec consistently makes each car ten seats. The build uses ten seats per car and trains with four cars for forty seats.
- The build brief requests an early report, but the user's final instruction requires stopping when that file is written. The report is therefore written only after checks, as the final build action.
- The no-score, no-lock, corrective-feedback design permits exhaustive guessing. Wrong entries cannot skip stages, and no score or mastery claim can be set by a guessed answer. Blocking all answer enumeration would contradict the specified practice behavior.

## Art made
Eight generated images are copied into `art/raw` and processed only with the free `scripts/art.py --rekey <name>` form. All eight are used in the interface. The first lead car had a rail attached and was redrawn once. The riders image has `people: true`. Prompt provenance is in `art/prompts.json`; the contact sheet is `_scratch/roller-coaster-rounding/art-contact.png`.

## Sensitivity
No cultural, religious, hard-history or body-learning content. The fictional riders show varied ages and skin tones. The people asset still needs the normal fresh review and owner contact-sheet review before shipping. This build makes no shipping or publication claim.

## Engine changes wanted
- `kit/number-line.js`, new `NumberLine`: implement the complete API in `docs/families/number-line.md`, using the tool-local coordinate, marker, span and input adapter as reference. The shared file was missing at build start. Do not promote the adapter without testing it against the other family tools.
- `docs/families/number-line.md`, roller-coaster-rounding table row: replace the incorrect hills-at-tens and nearer-hill wording with stations in valleys at tens or hundreds, midpoint hilltops and the bigger-station convention at ties.
- A future engine should preserve active drag handles through redraw, provide measured tick-label spacing, and support animated zoom without shrinking labels below readable size.

## Review focus
Record upbeat-guide / Zephyr later through the normal voice workflow; browser speech is the present fallback. The cold reviewer inspected the riders for age and skin-tone variety, natural presentation and classroom suitability. The current contact sheet is `_scratch/roller-coaster-rounding/review-art.png`. No commit or release was made.

## Cold review changes
- Preserved the park, car art, ticket trades and halfway teeter. Redrew the station as a timber loading platform with a blank signboard and bell; rekeyed all cutouts with edge despill.
- Correct rounding choices now animate the miniature car on the fixed 0 to 1000 number line. Its destination cannot be relabeled by the next question. The hint records the rounding result, and Motion off shows the same accepted state without movement.
- Shortened the Line welcome and action lines to fit a two-second tap pace. Bundle and break narration checks the exact current step and required control. Capacity, slip selection and corrected-column instructions are recordable. Train steppers let their still-valid welcome finish. Returning to Trains restores the hint for its actual step.
- Enlarged and clarified desktop grouping tags as `10 cars = 100`; added pale row backing to make the array readable over the park. Compact tags retain `100` to preserve every car.
- Independent adversarial scripts and current review frames live only in this tool's Scratch folder. `codex-review.md` is the final disposition, including the conflict between answer-revealing retries and the review's anti-enumeration rule.
- The phone stage uses 48 percent of the available height so guesses, distances, the overview and the result ticket have separate rows. On narrow stages the halfway rule occupies the existing caption during the teeter; wide stages put its sign left of the moving car. The four-digit held value has its own compact type size.
- Wrong estimates, clerk/capacity judgments and slip corrections have a refusal tone. Trying to break an empty tens pile explains how to make strips from a roll. Automatic switches to Hundreds through Tricky drop speak the existing how-to; Read names the current track.
- Compact Train cards show their fixed counts in shorter rows, with the unusable stepper buttons hidden. This keeps Start over visible when Enough and Not enough appear. Exploration retains full-size stepper targets.
- The clerk banner explicitly labels a claim and, after correction, the original claim. It therefore cannot present the old wrong equation as the current result.
- The sneaky-card premise is an event and finishes even if the student selects the column while it speaks. Its separate selection how-to is dropped once the column has been selected. All 28 fixed lines match the voice inventory.

## Build check fixes
The full mechanical audit finished once, with 140 leads on its preserved input bundle in Scratch. Real leads led to wider compact keypad targets, a Close keys control, inert background controls during keypad entry, explicit focus restoration, stable Hundred-track control positions and Sound labels, separated result cars/station choices, and more space under train arrays. The audit was not run a second time; changed areas have targeted drive evidence.

Adversarial checks also found two visual answer leaks. Future unentered column totals now remain question marks, and the result track uses an answer-independent 0 to 1000 range until the estimate is entered. The expanded functional run passed 769 assertions. Switching track now clears a guess made on the old track. A carried piece is outlined so its +1 annotation refers to a piece already shown.

The keypad is a temporary entry overlay. Enter or Close keys closes it, Escape closes it, and widening the window restores ordinary controls while preserving any typed number. Its extra how-to line is included in the final 24-line voice inventory. The board and all numeric answers still store nothing.
