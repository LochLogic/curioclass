# Batch note: grade 11 test batch (2026-10-25)

Cory asked for a test batch of 15 grade 11 tools, made end to end on this PC: code, local art, local voice. He reviews
them all together afterward to find areas for improvement, so do it right rather than fast, and say plainly in your
report what you were unsure of.

The batch (10 after Cory paused five on 2026-10-25; the paused ones are struck below), in build order: rollercoaster-polynomials, imaginary-island, outbreak-model, ferris-wheel, undo-machine,
savings-plan, poll-workshop, motion-graph-match, collision-lab, field-lines, circuit-builder, sound-studio,
satire-decoder, usage-panel, stock-market-1929.

## Rules for this batch (on top of your brief)

- **Band 9-12:** students drive, often on their own laptops. "Tools that work like the real thing: simulators, data
  and models that students run and question." Dark, pro-instrument look; minimal celebration (no confetti, no mascots).
- **9-12 theme:** the first tool built (rollercoaster-polynomials) writes `kit/theme-912.css`: the 9-12 values for the
  kit's color variables (`--paper --ink --muted --line --focus --brand --btn --btn-line --head-ink --panel`) plus
  any instrument-panel basics (readout font, slider style). Contrast must pass WCAG AA. Later tools link it with
  `<link rel="stylesheet" href="kit:theme-912">` after `kit:curio` and may set their own `--brand` accent. Check
  `scripts/bundle_tool.py` inlines any `kit:NAME` css; it does.
- **Family engines:** only graphing has a spec here (`docs/families/graphing.md`); rollercoaster-polynomials builds
  `kit/graphing.js` to that spec, and later tools may reuse it if they plot functions. A family with no doc in
  `docs/families/` (function-machine, sampling, forces) has no engine yet: keep that logic self-contained in one
  clearly marked block of the tool so it can be lifted into a kit file later. Do not write new family docs.
- **Art:** made on this PC by local FLUX models, which must never draw people. So no people, faces or hands in any
  image, at all (not even `people: true`). Prefer drawing in code; most of these tools need 0 to 4 images.
  Good image subjects: textures, objects, places, backgrounds, icons.
- **Voice:** recorded on this PC by Qwen3-TTS cloning one frozen narrator. In `voice/lines.json` set
  `"bank": "hs-narrator"`, `"voice": "Kore"`, `"style": "Read clearly and naturally, at a moderate pace"`.
  Grades 3+ rule: narration only where it truly helps, such as a one-line welcome for each mode, short instructions, or
  a story beat. About 5 to 25 lines per tool. Lines are plain sentences, under about 200 characters each, with no
  symbols a voice would misread (write "x squared", "percent", "meters per second").
- **Facts:** high school content must be correct. Physics and math values get checked against sources, with units.
- **History:** stock-market-1929 is a simulator of a real event: no win screen that makes the crash a game to beat;
  ground it in real figures and primary sources.
- **Sizes to check (learned from the first two tools):** the site's tool page embeds tools in a 16:10 box about
  680x425, so check 680x425, 800x500 and 1000x625 (controls visible without scrolling: keep stage and panel side by side
  with a compact panel in short landscape boxes), 760 px wide (the stack breakpoint is 1000 px), and 375 px wide inside
  an iframe host page (headless Chrome will not go below about 520 px). `scripts/shoot.py` does not print console
  errors: collect them yourself. Tab order: the panel's controls before long lists of map items.
- **About the 16:10 preview:** the tool page (site/templates/tool.html) shows the tool in a 16:10 preview box next to a
  "Play full screen" button. The preview must look inviting, readable (scene text about 10 px or more) and usable, but
  full screen (a laptop window, 1280x720 and up) is the main way students use it. Don't sacrifice the full-size layout.
- **Voice behavior (learned from tools 1 to 6):** one welcome per mode, queued when the mode is entered (or after the
  first unlocking tap). Mark a line said when it starts playing, not when it is queued; a stop drops lines that never
  started, and their trigger can queue them again. Read always stops other speech and speaks the current hint; nothing
  queued may cut Read off. Test this with real clicks, including clicking around during a welcome.
  Test voice with held clicks (press, wait about 120 ms, release): instant scripted clicks hide pointerdown/click races.
- **Mute test browsers:** start every Chrome with `--mute-audio` (Cory hears test sounds otherwise). Clips still play
  silently with normal timing, so voice tests still work.
