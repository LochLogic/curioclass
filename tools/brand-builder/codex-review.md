# Codex review: brand-builder

## Played

Cold Grade 10 solo play before builder notes/source: chose a client, explored every section, tested, inspected failures,
used Fix in Design, undo/redo, own business and Sheet. Projection check and two bar tools followed. Strong studio identity.

## Findings fixed

- **Blocker, general, Design:** six specified fonts were unavailable. Embedded ten local WOFF2 weights; all eight faces and 14 weights load offline.
- **Should fix, general, Name:** single-weight faces offered synthetic Bold; Bebas lowercase overrode its capitals-only rule. Corrected both.
- **Blocker, general, rendering/tests:** enlarged marks could paint outside the test's 100-unit window. Lockups now use the same mark window as tests.
- **Should fix, general, Mark:** monogram-only scale/rotation did nothing. Monograms now share the mark transform.
- **Should fix, general, Test:** stale details could open after a mode change, and pending rows kept old verdicts. Added revision/mode guards and Testing feedback.
- **Should fix, general, Design/voice:** repeated section taps rebuilt controls; queued how-to lines could outlive their section. Kept controls/focus and scoped validity.
- **Should fix, general, Test:** kraft contrast-only failures showed a false merged-region diagram. Draw that evidence only for an actual merge.
- **Should fix, general, Sheet:** clear-space box measured renderer padding. It now follows painted bounds, with the stated 25% margin.
- **Should fix, general, typography:** tagline width and small-name notes used rough guesses. Measure the font and both dimensions of each print zone.
- **Should fix, general, typography:** the audit found script descenders sharing the tagline's line box. Reserve the real font descent/ascent and enough lockup height.
- **Should fix, general, own business:** long unbroken names/evidence could spill from the sheet. Added wrapping and a titled compact phone heading.
- **Should fix, general, voice:** Sound on could not recover an unheard all-hold introduction. The welcome now follows the all-hold state.
- **Should fix, general, layouts:** phone client choices were hidden and a long failure could clip the repair action. All six choices fit; detail art leaves action room.
- **Should fix, general, notes/hints:** a container was proposed as an internal-color repair. Corrected the notes and passing-detail/all-hold hints.
- **Polish, general, Test:** flattest proof was the tiny phone icon. Kept its photograph and added an enlarged view of the exact icon.
- **Polish, general, graphics:** redrew the soft, flat kraft bag with paper fibers, folded gussets and directional light. Preserved the other five images.

## Findings left

- **Should fix (spec conflict), general:** the required one-column phone Test wall scrolls; eight large photographs cannot also all fit without scrolling. Kept the explicit layout.
- **Should fix (spec rule), general:** any container passes the van test. Preserved the prescribed rule and labeled its shortcut as insufficient for WCAG compliance.

## Flattest moment left

The brief-fit form remains the quietest step. Its notes become the student's own evidence on the sheet.

## Graphics

Six finished images inspected, one redrawn, none missing; no people in these product mockups. Art 339.4 KiB; offline bundle 953.4 KiB.
Bag redrawn with the built-in imagegen tool; asset `art/bb-bag.webp`, full prompt `art/prompts.json`.
Phone proof enlarged; original studio palette, large artboard, textured surfaces and grayscale-safe verdict icons preserved.
Compared current Beat Lab and Snowy Mail Route frames at 1366x768 without modifying either tool.

## Audit

One final audit completed inside 40 minutes, Chrome 9941 and host 8745: 117 raw leads, 145 frames viewed.
Seven script-spacing rows fixed; 100 caption/modal/form rows intentional; eight skipped welcomes and two no-op flags explained.
Repeated/rapid taps, keyboard paths and resize stress finished with no runtime exceptions or stranded disabled controls.
Eleven scoped post-audit frames passed with no console errors; script/tagline gap is positive at all eight sizes.
Sound recovery and maximum custom text passed. The complete audit predates these final repairs; no second full audit.
Evidence under `_scratch/brand-builder/`: `review-audit/audit.md`, `review-audit-disposition.md`, `review-frames/`, and voice/numerical JSON logs.
Independent checks: 16/16 passing/breaking test cases; all six client priorities; undo/redo; fast changes end on the final revision.
Motion off, grayscale and keyboard checks passed. All six client choices remain visible, including maximum custom text.
Five contrast pairs recomputed: 5.1093, 5.4839, 16.5065, 7.1580, 6.5743. No unresolved art tokens or tool network loads.

| Voice line | Kind | Expected | Spoken |
|---|---|---:|---:|
| nameHow, five repeated taps at 2 seconds | how | 1 | 1 |
| broke-sign, five new failures | event | 5 | 5 |
| allHold, entry plus five repairs | event | 6 | 6 |

Read interrupted speech and worked with Sound off and inside a modal. First stage/key welcomed; first Read only read; first Sound stayed silent.
The 26-line catalog matches allLines. A long voice probe exceeded the driver's 60-second evaluation cap; one smaller retry passed.

## Left open

Recorded narration is not supplied: browser speech remains, as the no-recording build rule requires.
No classroom test. The spec's no-scroll contradiction and van-container shortcut remain documented in handoff.md.
All owned Chrome processes and servers closed; host.html removed. No git commits. The final audience-copy correction only shortens text.
