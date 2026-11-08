# Spot the AI build handoff

## Structure

src.html starts from the kit starter, using kit CSS, Curio.tone and Curio.voice. A responsive SVG paints the live
bench at its actual pixel size; the DOM shelves and panel controls remain stable during jobs. ART contains each
painted asset once for bundling. MACHINES and ORDER are the content tables. Machine Shop and showdown have separate
page-load states. serial invalidates timers and speech on a newer action. No shared engine is used.

The shelf layout latches to a compact strip on Open, and expands only on Back. Selecting a machine keeps its tile
at the same position, including repeated taps. Clicking the already active mode is a no-op so it cannot cut a welcome.

## Spec decisions and open questions

- Keep the three people assets: the owner, the identical owner in a hat and the diverse face grid. The current
  brief and BASELINE authorize Codex people art and supersede the spec's older Gemini wording.
- Keep all added new-example narration, including hat, cat, rain, puppy and space.
- The spec's listed art count is correct: 30. The seven-line preview initially miscounted 31; the independent
  script confirmed 30 before implementation.
- Build-only instructions require images despite BUILD.md's older instruction not to draw art. Current instructions win.
- Preserve the existing workshop image and add missing art in a compatible bright picture-book style.
- Read the report's validation status before shipping. No recordings are made because the build brief forbids them.
- The fixed showdown order is deliberate. Replaying can be solved by remembering the ten answers. It is a teaching
  sequence with no saved best or claimed mastery score; randomizing would contradict the spec.
- The teddy repeats its same three-phrase cycle. "Same every time" means the same written cycle, rather than one
  identical phrase on every squeeze. The notes explain the input/rule distinction for number-controlled machines.

## Sensitivity

The three marked people paintings show a cheerful brown-skinned child and a grid of twelve people with varied ages,
skin tones and hair, including glasses and a headscarf. Review the full art sheet in Scratch for representation and
the owner/hat match. No culture or religion is taught. Faces are conceptual examples, not captured biometric data.
The space cartoon was redrawn to remove an unrequested astronaut, keeping the three intended people assets.

## Engine changes wanted

None required. Browser speech picks the kit's best available voice; the selected bank identity becomes audible only
when a later authorized recording pass supplies clips.

## Cold review changes, 2026-11-07

- Removed the classification-dependent startup pitch, which gave every answer away. Jobs now start at 480 Hz.
- Short how-to lines take priority on the action that makes their control available. They remain once per load;
  job/reveal events remain repeatable, with serial checks dropping speech after its state changes.
- Questions and answers from the speaker update their visible bubble when the shared voice queue starts them.
- The teddy's picture rule highlights its current phrase, has a return arrow, and says Same three in order.
  Its repeat narration describes the cycle rather than claiming each squeeze says the same sentence.
- Replaced the square phone-lock glyph with a drawn open/closed padlock. Motion privacy is visible in the panel.
- The mop's wrong Dog guess now has a cross rather than a matching check. The displayed AI definition is scoped
  to this shop, and notes distinguish machine learning from the wider field and generic face features from identity matching.
- Shelf painting redrawn with built-in imagegen in the existing house style. See prompts.json for conversion provenance.
- Kept the specified fixed showdown order. Memorization can still light all ten bulbs; removing that shortcut
  requires a spec decision. Notes explicitly prohibit treating bulbs as demonstrated mastery.
- No recordings made, in keeping with the build/review brief. Browser fallback remains an unfinished shipping item.
- The single review audit confirmed rapid re-selection cutting instructions and in-machine voices. An already
  pressed shelf tile now acknowledges the tap without restarting its selected job; the explicit repeat control
  still repeats. Teddy sayings join the speaker's speech-synchronized bubble handling.
- Showdown entry uses the vote instruction as its welcome. No separate greeting is queued behind the action line.
  Post-audit checks are scoped to these voice/selection changes; the full audit was not repeated.

## Audit interpretation

The dedicated inside-picture SVG group contains cropped nested SVG portraits. Its DOM bounding box includes
parts of the source portrait grid that the nested viewports clip away. The mechanical keep-region sampler can
therefore report a giant covered/offscreen region even while all rendered cards and controls fit. Check the
actual ai-open, show-open and cat-lock frames, including the 375 iframe, before treating that warning as a layout bug.
The compact 64 pixel scrolling shelf is specified; the two voting buttons and primary actions never use that scroller.

## Build boundary

Writes stay in tools/spot-the-ai and _scratch/spot-the-ai. No commits, deployment or polish round.
Ports: Chrome 9980 through 9987, host 8785. Scratch holds prompts provenance, commands, frames and validation.
