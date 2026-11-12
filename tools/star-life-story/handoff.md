# Star Life Story handoff

## Status

Incomplete build. No playable HTML was produced. An automatic content filter blocked the implementation write;
the blocked content was not retried or worked around. This folder contains the generated art and preflight records.
Do not publish or label this tool built. The draft metadata deliberately remains at stage `spec`.

## Preserved work

- `spec.md`: unchanged source specification.
- `art/prompts.json`: ten asset prompts, provenance and people flags.
- `art/raw/`: ten original PNGs copied from the built-in image tool's output.
- `art/*.webp`: ten processed assets, 249,928 bytes total.
- `voice/lines.json`: the six specified lines, smooth-narrator / Algieba. No recordings were made.
- `notes.md`: teaching notes for the intended tool, explicitly labeled as unbuilt.
- `_scratch/star-life-story/numbers.py` and `numbers.json`: independent numerical checks.
- `_scratch/star-life-story/art-contact.jpg` and `art-stats.json`: inspected contact sheet and asset dimensions.
- `_scratch/star-life-story/generated-paths.json`: original image output paths.
- `_scratch/star-life-story/run.py`: subprocess timeout wrapper; use from the repository root.

## Open questions resolved for the intended build

1. Keep the simple tracks restricted to sourced main-sequence duration and fate. No MIST models or invented
   durations. There are seven simple Content cards, despite the open question saying five.
2. Share `sl-giant` between the Sun's giant phases and the 20 solar mass post-hydrogen stages. Keep
   "not to scale" visible. The shared portrait represents appearance schematically, not measured radius.

## Other spec and brief conflicts

- Content lists seven textbook cards, plus a separate Sun and detailed 20 solar mass track: nine total.
  Keep all nine to preserve every supplied content case.
- The required astronomy family doc and shared engine do not exist in this checkout. Orbit Lab has only `spec.md`.
  No usable engine was available to import. Nothing shared was changed.
- The spec requests FLUX. The user explicitly asks for the image tool; all ten assets were generated with
  OpenAI gpt-image through the built-in image tool instead.
- The Sources title for arXiv astro-ph/0211062 is mismatched. The linked paper is Heger et al.,
  "Massive Star Evolution Through the Ages" (submitted 2002). Its Table 1 contains exactly the six supplied
  20 solar mass burning durations. The report links the source actually checked.
- Sun panel's 0.03 percent cumulative mass loss needs the constant-current-luminosity assumption visible.
  It is a calculation at today's power, not a full integration of a changing solar model.
- "Age of the universe 13.8 billion" is the rounded marker; 13.787 billion is the more precise Origins value.
- The 20 solar mass card has no sourced surface temperature in Content. Do not invent one for its numeric panel.

## Art review

All ten exported WebPs were opened at native size. No people or lettering appear.
The portrait set is luminous and coherent, with suitable dark negative space in the nursery.
Most square-requested portraits came back landscape. Keep their actual aspect ratios when drawing;
stretching them into square destinations would distort the stellar disks.
The black hole image includes bright gas beyond the lensing ring. It needs a scientific review or a redraw
for the spec's narrower lensing-only description. White-dwarf surface detail is illustrative, not observational.
The neutron-star beams meet the image edge; allow for this when fitting the portrait.
No in-tool art placement, screen blending, temperature tint or responsive composition was verified.

## Sensitivity

No people appear in any asset. The planned My body filter concerns elemental composition only,
with no body images or personal information. The planned tool should collect no information.

## Engine changes wanted

`kit/astronomy.js` and `docs/families/astronomy.md` are absent. Orbit Lab's Family engine section describes
`Astro.deepTime`, `Astro.SpaceView`, `Astro.starColor`, `Astro.fmt` and physical constants.
Provide a tested implementation when the repository's three-finished-tools promotion rule is satisfied.
No shared change was attempted in this build.

## Validation remaining

All executable acceptance checks remain open: bundle, all modes, phase scrubbing, time scales, death cancellation,
Arrange cheat attempts, storage failure, keyboard, voice at two-second held-click pace, every STANDARDS size,
375-wide iframe, Motion off, grayscale, resize during animation, bar-tool comparison and the final audit.
No Chrome or host process was started; no `host.html` exists.
No commits, branch changes or polish round were made.
