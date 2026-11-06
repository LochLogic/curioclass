# Bus Stop handoff

## Structure
`src.html` uses the kit starter frame, kit CSS, Curio.voice, chimes and Motion/Sound/Read. The tool lays out at real
viewport sizes with CSS instead of scaling a fixed scene. The ART table is the only set of image tokens.
`content.json` is loaded by the bundler and holds the fixed routes, play-area names and Express fact bank.
Drive, Split and Express each keep independent in-memory state. No student work is persisted.

The Drive state machine is choose, show (or Tell first hold), tell, depart, fork, split and end. Done validates the
number of changes, not a displayed total. Async transitions carry a generation token so a mode switch cancels their
continuation. Returning to a paused departure or Express reveal resumes it. Static seat and action elements keep focus.
Split counter buttons retain their DOM identity when they move. Drive also keeps an aboard identity set, so a child
cannot board twice without leaving. The school ending uses all ten wave poses below the recap without covering faces.
Express reserves its result and Show me space so answer tiles stay still. Selecting an already active mode is a no-op.

The art manifest holds 59 separate assets, including 23 marked `people: true`. Generation prompts and original crops
are in `art/prompts.json` and `art/raw/`. Coordinated source atlases were cropped into separate assets. Seven scenes
were repainted individually after the atlas returned tall cells. All were processed with `art.py --rekey` only.
The full prompt set combines `house_style` with each asset prompt. Built-in image generation was used, not CLI drawing.
The people contact sheet is `_scratch/bus-stop/people-contact.png`.

## Spec decisions and contradictions
- There are no open questions for the owner in the spec. The finger strip is omitted as specified.
- The listed art adds to 59, not the printed 45. All listed assets were made; 23 contain people.
- The user's image-tool instruction overrides older Gemini-only wording in the spec and standards. OpenAI images
  carry the requested provenance and people flags.
- BUILD.md says not to draw art. CODEX-BUILD.md and the current user explicitly require it, so art was drawn.
- The spec's full-size stage estimate ignores the kit header height. Layout uses available space and keeps actions in view.
- K.OA.A.4's source covers every starting number one through nine. The prescribed routes only start Ten stops with
  four through eight. No additional number content or mode was invented to fill that spec gap.
- At a Ten stop the initial waiting group is empty seats plus two. Exactly two remain after boarding, and the result
  line says two. The voice template's `w` is ambiguous if read as the initial waiting count.
- The reference tools already had bundled HTML. Those bundles were opened without rebundling their folders because
  this session may write only to bus-stop and its scratch directory.
- Hundred Hop had no handoff/refine files. Snowy Mail Route supplied the built neighbor handoff and refine evidence.
- No audio was recorded, as the Build brief requires. The intended voice is bright-teacher / Autonoe; browser fallback
  is used until the separate voice stage. Every spoken expansion is included in `voice/lines.json`.

## Sensitivity
The rider set includes varied skin tones, hair, everyday clothes and body types, plus a hijab, glasses, hearing aid
and leg brace. No character is assigned an ability or stereotype by appearance. Art is friendly and fully clothed.
The builder inspected every person on the contact sheet. A fresh representation review and the owner's contact-sheet
view remain part of the later review/shipping workflow; this Build makes no claim to that independent review.

## Engine changes wanted
None. No shared kit file was changed.

## Review focus
See `codex-report.md` for test results and remaining limits. Browser speech is environment-dependent. Inspect the
small driver's-window portrait and the compact card speaker targets. Full checks and evidence live in the scratch folder.

## Cold-review repairs
The review first played Park via Duck Bridge, every seven-rider Split and a full Express ride before reading builder files.
Inactive Drive controls now have true disabled states, and departure has a visible keyboard focus destination.
Split keeps at least 100 pixels for an empty play area at intermediate widths, so its place label stays readable.
Counter moves use short FLIP motion, recorded ways stamp in, and the complete list pulses once; Motion off removes these.
Queued kept-way speech is dropped when that grouping changes. Split and Express put their instructions first.
The map has illustrated stop medallions, completion checks and a bus marking the current stop.
The voice manifest now enumerates reachable content rather than broad arithmetic templates with unreachable false praise.
To regenerate it after changing text, the review helper is `_scratch/bus-stop/review-voice-manifest.py`.
At 760 pixels, sentence-card dots use the compact three-pixel pattern so two-digit School sentences fit beside their speakers.
Audit targets are now 60 pixels globally to expose smaller controls at larger sizes; only the spec's 680 preview allows 44.
The final audit exposed 56-pixel Split targets at 1280: five fixed columns now begin at 1340, with automatic wrapping below.
An unpicked fork keeps both roads equally faint and shows an unknown stop instead of suggesting a selected road.
Drive's Split overlay explicitly hides the old bus, window portrait, riders and stop label; the trip tickets remain visible.
It also hides the old counter board from keyboard and assistive-technology navigation.
The review audit completed once with 59 leads. All 57 saved frames were inspected. Its iframe-context lookup failed,
so separate 375-pixel opening, Express, Split and recap checks supply the phone evidence without claiming an automatic pass.
The Drive-Split state was added to audit-states after that audit and received focused visual checks instead of a second audit.

Two specification conflicts remain explicit: sentence-card elimination is permitted by the prescribed retry scaffold,
and fixed Ten stops cover starting numbers four through eight rather than the full one-through-nine standard.
Do not silently add an assessment gate or new number content to resolve those conflicts.
