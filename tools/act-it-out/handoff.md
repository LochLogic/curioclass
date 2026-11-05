# Act It Out build handoff

## Files and structure

`src.html` starts from the kit starter and uses kit CSS, controls, audio context, and Curio.voice.
The page has permanent home, story, and Trunk containers. Buttons retain their DOM identities and focus.
`content.json` holds the three exact retellings, beat metadata, costume places, questions, sound names, and every voice line.
`art/prompts.json` retains the six existing backdrops and adds the missing 26 painted assets.
All image tokens occur once in the ART table; static image elements use data-art so the bundle does not duplicate paintings.

`state.outfits` is rebuilt by folding costume assignments from beat 1 through the current beat.
Swapping XORs the role-to-side mapping, including line names, active badges, and later costumes.
Choices are keyed by beat index, retained on Back, and may be changed there.
Trunk outfit and backdrop are independent of story state and persist across mode changes in memory.

## Narration and interruption

The Curio.voice scope is mode plus story. Each beat has a visit revision used by valid checks.
The first story beat starts speaking immediately; its title follows only if that first beat remains open.
Read and Sound also settle any visual transition immediately while preserving their kit handlers.
Every new action stops speech, finishes and cancels transient animations, clears pending visual timers,
and stops tool sound nodes before applying the next state. No UI action waits for a line or animation.
How-to lines use V.heard; story visits and action lines are events. Read speaks the current beat plus its hint.
`voice/lines.json` contains the requested voice and both role-name variants. No narration was recorded, per Build instructions.

## Spec decisions and ambiguities

- Open question: keep the classic Gingerbread Boy ending, gently told, as the supplied beat list leans toward.
- The first Done when says Next only, while Choose explicitly disables Next until a choice. Choose takes precedence:
  all stories finish with Next plus their required choice tap. There is no automatic choice.
- Icing buttons and candy bow tie share the body place. The spec's one-piece-per-place rule means the bow replaces
  the buttons in Gingerbread beat 2. Both are painted and usable individually in Trunk. A separate neck slot would
  require an owner-approved content change; the builder did not introduce one.
- Costume assignments persist in the other places when a role changes. For example, the fox's new head and tail
  do not implicitly remove the earlier apron or pig snout. This follows the cumulative per-place rule; review the
  intended combination before changing it.
- The art list calls the six settings kitchen, road, river, and garden in the beat shorthand. Content uses the exact
  art names cottage-kitchen, country-road, wide-river, and veggie-garden.
- Puppet cutouts are narrow lathe-turned toys. Their natural aspect ratio and face coordinate system are used,
  rather than stretching them into the requested image canvas aspect.
- Nothing saves story progress or outfits. The required shared kit still remembers the Motion preference.
- The six pre-existing backdrop images remain. New cutouts were made with the built-in image tool, per the user's request.
- The report is written last because the user's explicit stop-on-report instruction overrides the brief's early-report advice.

## Engine changes wanted

`kit/curio.js`, init Motion handler: optionally support an in-memory preference for tools whose spec requests no storage.
The current kit always writes curio-motion. This tool follows the standing kit requirement and makes no kit change.

## Validation and remaining work

### Cold review, 2026-11-03

The cold reviewer played all stories and Trunk before reading this handoff or the source.
Review commands use Chrome 9960 to 9967 and host 8765, superseding the builder's ports below.
The one-pass review keeps all changes in tools/act-it-out and _scratch/act-it-out; no commits.

Changes: the current hint is a single visible node moved between home, story footer, and Trunk.
The home hint explains solo parts, classroom sides, and personal-space mime. Acting/dressing use the acting hint.
The selected bear branch now owns the visible card and Read, rather than narrating over a conflicting Choose card.
Piece taps speak on/off event lines; Ask includes a once-per-load next-action cue. All are in both line manifests.
Trunk welcomes may return on a fresh mode entry if an earlier welcome never started.
Inactive toys dim with brightness rather than becoming transparent. Trunk has the same gentle idle sway, stopped by Freeze/Motion.
Mouse ears were redrawn as a plain grey felt headband, without the unrequested bow, and rekeyed through art.py.
The turnip soil now hides its lower half and leaves a dark hole after the pop; calm growth uses the full four seconds.
Sound-effect taps have a visible flash with Motion off. The specified story-start title event follows the immediate first beat.
Sound on after silent dressing can deliver an unheard Trunk welcome. Swap on the growing turnip keeps the settled giant visible.
Garden dressing places the decorative trunk in spare foreground space; the phone Trunk chest clears the puppet's feet.
Background side badges hide during the curtain call, preventing the phone heading overlap.

Still governed by the spec ambiguities above: no extra body slot or automatic costume clearing was introduced.
Those changes would contradict the explicit one-piece-per-place/cumulative rules, so the cold review leaves them open.
The narration manifest is complete but no recordings were made, because CODEX-BUILD forbids recording audio.
Final review evidence and the single audit outcome are in codex-review.md when completed.

The review audit completed once within its 40-minute limit, with 14 machine leads and 89 frames.
The resize stress stage finished without exceptions or controls left disabled. Visual overlap leads were confirmed and fixed.
Welcome suppression after a story's own first-tap line, intentional rapid-tap speech cuts, and unscrolled wardrobe targets
are interpreted against the actual interaction rules, not treated as missing narration or dead buttons.
Only the affected states and voice interruption cases were re-shot afterward; no second full audit was run.

### Original build validation (historical)

The audit reached its 30-minute cap without producing audit.md. Its 73 frames are preserved in Scratch.
After that stop, Read/Sound interruption was checked separately. A clipped compact curtain-call heading was
fixed with a two-column button row and re-shot at 680x425 and 800x500. The full audit was not rerun.
See codex-report.md for the Build evidence, frame paths, and honest limits. Scratch is
S:/CurioClass-codex/_scratch/act-it-out. Only ports 9990 to 9997 and host 8795 are allowed for this work.
Build only. No commit and no polish round. A cold review is the next workflow step.
