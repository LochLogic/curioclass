# Codex report: star-life-story

## Built

INCOMPLETE. Ten generated images, source preflight, independent calculations, voice manifest,
draft metadata, notes and handoff are preserved. No `src.html` or playable bundle was produced.

An automatic content filter blocked the implementation write. The blocked content was not retried,
reformatted, split or worked around. The unrelated art and preflight work was completed afterward.
The tool must remain unpublished. `tool.draft.json` stays at stage `spec`, rather than claiming `built`.
This does not meet the requested completed-build outcome.

Workspace was confirmed as `S:\CurioClass-codex`. Writes stayed inside `tools/star-life-story/`
and `_scratch/star-life-story/`. No commits, branch operations or polish round were made.

## Numbers check

PASS, computations only. Evidence: `_scratch/star-life-story/numbers.py`, `numbers.json`,
and assertions in `validate_package.py`. All calculations use the spec's constants.

| Quantity | Recomputed result | Spec comparison |
|---|---|---|
| Solar mass to energy, L/c squared | 4.2592244146e9 kg/s | Rounds to 4.26 million tonnes/s |
| Counter after ten seconds | 42,600,000 tonnes | Exact for the prescribed rounded rate |
| Constant-power loss over 4.57 billion years | 6.1425781476e26 kg | Matches about 6.1e26 |
| Fraction of solar mass | 0.03088275% | Matches about 0.03% |
| Surface to Earth, 1 AU/c | 499.0048 s, 8.31675 min | Matches 499 s, 8.3 min |
| CMB wavelength peak | 1.063291 mm | Matches 1.06 mm |
| Four neutral H atoms versus He atom | 0.711852% mass defect | Matches about 0.7% |
| Neon burning | 219.15 days | Matches 219 days |
| Silicon burning | 11.32275 days | Matches 11 days |
| Solar main sequence remaining | 6.43 billion years | Matches 6.4 rounded |
| Last three massive-star fuel stages | 1.931 years | Matches about 2 years |
| Those stages on a 600 px logarithmic line | 0.000003715 px | Confirms need for phase strip |
| Sun's 11 to 12.4 billion years | 0.052029 log decades | Matches 0.05 decade |
| 40-mass main sequence / Sun main sequence | 0.000090909 | Below 1% |
| Play at two seconds per band | Sun 14 s, massive 18 s, plain 6 s | Matches specification |

No conflicting numerical result was found. The constant-power solar loss estimate needs its assumption visible.
The scripts do not validate an executable simulation, since none exists.

## Facts checked

No facts are displayed by a functioning tool. The following preflight facts were checked live:

- All seven textbook card masses, temperatures and main-sequence lifetimes match
  [OpenStax Astronomy 2e, Table 22.1](https://openstax.org/books/astronomy-2e/pages/22-1-evolution-from-the-main-sequence-to-red-giants).
- Hydrogen to helium fusion and the approximate 0.7% mass conversion are supported by that same chapter.
- The six supplied 20 solar mass fuel stages, products and durations match Table 1 of
  [Heger et al., Massive Star Evolution Through the Ages](https://arxiv.org/pdf/astro-ph/0211062).
  The spec's linked arXiv ID is correct for the data, but its paper title and citation year are mismatched.
- The Heger discussion supports approximate white-dwarf and neutron-star mass boundaries, with model dependence.
- The [Sackmann author page](https://www.cita.utoronto.ca/~boothroy/sun3.html) confirms the paper identity;
  the full detailed solar track was not independently verified.
- The [solar interior chapter](https://openstax.org/books/astronomy-2e/pages/16-3-the-solar-interior-theory)
  was opened; both radius fractions still need verification.
- [Johnson 2019 publication identity](https://pubmed.ncbi.nlm.nih.gov/30705182/) and the
  [NASA periodic-table reference](https://chandra.si.edu/chemistry/images/Periodic_Table.pdf) were located.
  The full element source mapping is still unverified.

Planck age, Fixsen temperature, IAU luminosity, NIST constants, Connelly solar age,
and the eleven body elements remain spec-derived here. Their provenance was not independently rechecked.
Evidence and limits are in `_scratch/star-life-story/source-checks.md`.

## Break it

NOT RUN. No scores, meters, quizzes, storage or reflection gates were implemented.
Do not interpret the numerical assertions as a gameplay cheat test.

Required future Arrange attacks: repeated Check without moving, swapping every pair, reading order from
IDs or labels, Show order then Check, switching tracks after a reveal, reload after assistance,
repeated reshuffling for an already solved order, and storage denial. None was run or fixed in this partial build.
An assisted or brute-force order must not set an independent or best saved result.

## Voice walk

NOT RUN. The six specified lines are in `voice/lines.json`, using smooth-narrator / Algieba.
No audio was recorded, as instructed. No `Curio.voice` implementation or `__tool.vlog` exists to inspect.
Main-path and side-path held-click walks, Read interruption, Sound off/on, and once-per-load how lines remain open.

## Feel check

FAIL: no playable session exists. I cannot honestly name an observed best gameplay moment or two observed flat moments.
The intended payoff was the expanding stellar death scene with element chips landing in the table.
The intended later variation was contrasting long-lived red dwarfs with the massive star's rapidly shortening fuels.
No gameplay changes were verified.

The Snowy Mail Route source, handoff and refine findings were read; Beat Lab source was read.
Neither bar tool was bundled and opened, and no side-by-side gameplay frame was produced.
The ten-image contact sheet shows rich art, but does not establish a finished tool's visual quality.

## Done when

1. FAIL: Sun's 11-billion-year track, now marker and final white dwarf are not implemented.
2. FAIL: massive-star strip, supernova, neutron star and once-per-load iron narration are not implemented.
3. FAIL: 0.4-mass line and universe-age comparison are not implemented.
4. FAIL: Compare interaction is not implemented; only its numerical ratio was checked.
5. FAIL: counter is not implemented; 42,600,000 tonnes at ten seconds was recomputed only.
6. FAIL: CMB card, gold selection and eleven-element body filter are not implemented.
7. FAIL: neither Arrange puzzle is implemented or tested.
8. FAIL: no composed Life Line or Sun scene exists at either required focus size.
9. FAIL: Play, Death and immediate input cancellation are not implemented.
10. FAIL: no voice walk or control visibility checks were possible.
11. FAIL overall: all ten exported images exist and contain no people, but image loading in a bundle,
    layout, all sizes, zero runtime network requests and executable behavior remain untested.

## Wave lessons

- Hint and voice: NOT TESTED; no UI.
- Focus and layout: NOT TESTED; no UI.
- Sizes, targets and hint visibility: NOT TESTED at every STANDARDS size.
- No giveaways: NOT TESTED; no Arrange implementation.
- Honest numbers: PASS for independent calculations; UI assumptions remain unimplemented.
- Standards: NOT MET; no student interactions teach the standards yet.
- Motion off: NOT TESTED.
- Short choices all visible: NOT TESTED.
- Resize mid-animation: NOT TESTED.
- No late welcome: NOT TESTED.
- Unknown shown as unknown: NOT TESTED; intended unresolved stages must remain explicitly unsized.
- One look, one meaning: NOT TESTED in a scene; image set was reviewed independently.
- Badge says what is true: partial metadata deliberately does not say built.
- Hint changes back with state: NOT TESTED.
- No answer by copying words: NOT TESTED.

## Audit leads

Audit not run. No bundle exists for `audit_tool.py` to load. No audit pass is claimed.
The required one final audit, state manifest and every browser check remain open.
No Chrome or server was launched, so no port or process needed closing. No `host.html` exists.
Assigned Chrome ports 9990 through 9997 and host port 8795 were not used by this partial run.

## Frames looked at

- `_scratch/star-life-story/art-contact.jpg`, all ten labeled assets.
- Each of the ten `art/*.webp` files, individually at its exported native size.
- No UI PNGs, grayscale frames, reduced-motion frames, keyboard frames or iframe frames exist.

## Art made

Ten new images generated with the built-in OpenAI gpt-image tool and copied into `art/raw/`.
All ten processed using only the permitted `scripts/art.py star-life-story --rekey <name>` form.
Total art: 249,928 bytes, 244.07 KiB. Recorded voice: 0 KB. Bundle size: unavailable, no bundle.
Budget was 650 KB art and 0 KB recorded voice against the 2 MB goal.
No redraws were performed. Asset dimensions and individual bytes are in `_scratch/star-life-story/art-stats.json`.
Prompts and provenance are in `art/prompts.json`, with `drawn_by: codex` and `people: false` for all ten.

## Art still to paint

No listed image is missing. Black-hole art contains bright gas beyond the lensing ring and should be
reviewed or redrawn to the spec's narrower description. Several square-requested portraits are landscape;
preserve their actual aspect when drawing them. No in-tool placement or tint has been verified.

## Engine changes wanted

No `docs/families/astronomy.md`, `kit/astronomy.js`, or built Orbit Lab implementation exists.
The described Astro helpers need a tested implementation before they can be reused.
Any future shared promotion must follow the baseline's three-finished-tools rule. Shared files were untouched.

## Left open

- The executable build is missing because the implementation write was blocked by an automatic content filter.
- `src.html`, bundled HTML and `audit-states.json` were not produced. Stage remains `spec` intentionally.
- All interactive, accessibility, voice, layout, feel, anti-cheat and audit acceptance checks remain open.
- Both open questions were resolved toward schematic existing tracks and the shared giant portrait in `handoff.md`.
- Nine cards are needed to include seven textbook cards plus the Sun and detailed 20-mass case.
- The spec's Heger citation mismatch and unsupported 20-mass surface temperature are documented in the handoff.
- Initial read commands used the tool's yield setting without a process kill deadline, which did not satisfy
  the explicit command-time-limit rule. Subsequent shell commands used the bounded scratch runner.
- Default Python lacked numpy/Pillow. The alternate Python launcher could not start. Export succeeded by using
  the readable installed site-packages with the default interpreter; no packages or shared files were modified.
- `_scratch/star-life-story/package-validation.json` verifies the partial package and numerical assertions only.
- No commits, polish round, deployment, external messages or audio recordings occurred.
