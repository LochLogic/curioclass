# Safety Sweep House handoff

## Structure
`src.html` uses the kit frame, Motion, Sound, Read, Curio.voice and tones. `content.json` contains the twelve cases, six room descriptions and fourteen lines.
The ASSETS map references each painting once for efficient offline bundling. The clipboard renders each decision step.
The stage renders the cutaway, searchable room, focused hazard, scene action or Safety card.
Per-hazard progress stores Think, peeks, tried choices, safe choice, adult help, action, reflection and completion.

## Tricky parts
Both the safe option and its scene fix are required. Adult-first cases lock the action until help is called.
Block, Report and Tell are separate ordered actions. The heater uses the actual distance, not rounded display text.
Hold actions cancel on release, blur, leaving the room and Escape. Taps are not accumulated.
Keyboard alternatives select an object and its target; the ruler uses six-inch steps.
The friendly-dad voice is specified in `voice/lines.json`. Recording is intentionally deferred by the Build brief.

## Spec choices and contradictions
- At 680x425 the specific short-landscape instruction wins over the general under-760 stack instruction. Portrait narrow screens stack controls first.
- The Safety card expands over the available viewport in short landscape, keeping its six-item page, emergency lines and buttons readable together.
- The spec describes panel outcomes as stacked, but Done when asks for all three side by side. The stage shows all three side by side, beside the hazard.
- The art list says about 44 images; counting the listed needs plus the block bin yields 46 distinct assets. The shared screen pair serves both online cases.
- The Sources section's 72-tap minimum omits required decisions and actions. The build counts the complete path separately in scratch.
- Generic Think wording mentions heat and fire, but heater blanket and cleaners are act-then-tell cases. Those exact case-specific answers are retained.
- The warm house painting is dimmed per room rather than repainted for each lighting state. Warm light and fixed cutouts appear when swept.
- Medicine storage and alarm testing remain supervised actions. Dad is present before the student helps with the simulated high cabinet or Test button.
- The hallway background's incidental chair and blanket were removed, because leaving them in the painting would contradict the heater's fixed state.
- The open people-review question leans toward drawing the family and reviewing the set. Every people asset is marked `people: true`; contact sheet is in scratch.
- The Theo reason avoids the spec's absolute claim that little kids cannot swim. CDC medicine storage and AAP supervision guidance support the narrower reason shown.

## Sensitivity
Poisoning, fire, drowning and online strangers may connect with a child's lived experience. Notes and plan explain the disclosure procedure.
No cultural or hard-history content. Family depictions must be checked for natural proportions, warm expressions, consistent Theo identity and absence of stereotypes.
The child is never asked about their own family or home. Theo is fully clothed. See the people contact sheet before shipping.

## Engine changes wanted
Tooling request: `scripts/drive.py`, `HOST`: include `<link rel="icon" href="data:,">` in the iframe host.
Chrome otherwise requests a missing favicon, creating a console lead unrelated to the tool. The temporary host was patched locally and removed after its shots.
No shared files were edited.

## Next
Cold review repairs: the heater ruler starts at the heater's edge and uses the same 59-percent travel span for pointer and keyboard input.
The blanket's nearest edge marks its distance, rather than its center. The four-foot position keeps the whole blanket on screen.
The ruler's live display rounds down so a sub-three-foot position cannot be shown as three feet. One foot uses the singular unit.
Read now includes Think explanations, reflection reasons, all visible Safety card habits and the emergency instructions.
Room-completion speech is preserved when entering the next room; state-specific lines have explicit validity checks.
Tap-target fixes briefly show the moved object traveling. Motion off swaps immediately; the next controls remain live.
The cleaner cutout was redrawn with native alpha, so its asset has cutout:false and native_alpha:true to preserve that alpha in art.py.
The online room's message plaques are block elements, so wrapped lines no longer paint over each other.
No shared files or git commits were made during review.
Audit-confirmed compact navigation repair: the existing Rooms button now lives in the header, so portrait scenes cannot push it below the fold.
The kitchen pot and towel hit areas are separate, preserving the rear pot and foreground burner rather than overlapping their buttons.
The portrait Safety card is a viewport overlay beneath the header, keeping Close, page navigation and Sweep again above the fold.
Underlying house and panel content is inert while the card is open; Read and the card's controls remain available.
