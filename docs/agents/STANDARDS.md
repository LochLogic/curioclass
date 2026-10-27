# Standards for every tool agent

Read this with your brief (SPEC.md, BUILD.md or VERIFY.md). It holds what the grade 11 test batch (2026-10-25,
`docs/agents/BATCH-G11-LOG.md`) learned the hard way. Every tool in that batch failed its first verify on something
below, never on the math. Where this file and your brief differ, this file wins.

## Variety (Cory, 2026-10-25)

The grade 11 batch all shared one narrator and one palette, and side by side they felt samey. From now on:

- **Voice:** each tool gets its own voice from the bank (`voices/bank.json`, the voices with status "kept": 23 of 25,
  picked by Cory 2026-10-26; adventure-guide and calm-guide are "dropped", never use them). The spec names it, matched to the tool's mood and audience,
  and different from its nearest neighbors (`python scripts/neighbors.py <id>` shows them; check their
  `voice/lines.json`).
- **Palette:** the band theme (`kit/theme-912.css` for 9-12; other bands set their own `:root` colors) is the base. Each
  tool sets its own accent (`--brand`) and, where it fits, its own scene colors, different from its neighbors'. The spec
  names the accent. Contrast must still pass WCAG AA (say the ratios).
- Don't retrofit the grade 11 batch; it stays as it is.

## Bands

- **K-2:** teacher led on a projector, big targets (60 px), a narrator voices every fixed line.
- **9-12:** students drive on their own laptops. Tools that work like the real thing; minimal celebration (no
  confetti, no mascots). `kit/theme-912.css` and `kit/graphing.js` exist (docs/families/graphing.md).
- Narration for grades 3+ only where it helps: a welcome per mode, short instructions, story beats, and the panel
  hints (so Read can use recordings). Plain sentences under about 200 characters, nothing a voice would misread
  ("x squared", "percent", "meters per second").

## Sizes

Check every one, early, not at the end:

| Size | Why |
|---|---|
| 680x425, 800x500, 1000x625 | the site's 16:10 preview on the tool page (beside "Play full screen") |
| 1280x720, **1366x768** | the main use: a school laptop, full screen. 1366x768 is very common and caught a fold bug |
| 1920x1080 | big screens |
| 760 wide | below the 1000 px stack breakpoint |
| 375 wide | phones, inside an iframe host (`python scripts/drive.py <id> --host`); headless Chrome won't go below ~520 px |

- The main controls (the ones a student uses every few seconds) are visible without scrolling at every size. In short
  landscape boxes keep stage and panel side by side with a compact panel instead of stacking; use the same
  buttons-first order in the wide layout when the window is under about 900 px tall.
- The preview must be readable (scene text about 10 px or more) and inviting, but never at the cost of full screen.
- Draw the stage at real pixel size and re-lay it out per size (as motion-graph-match and collision-lab do) rather
  than scaling one fixed design: a 1100 px scene scaled into the preview has 6 px text.
- Tab order: panel controls before long lists of map items.
- Moving focus on purpose uses `focus({preventScroll: true})`: on a phone a plain focus() scrolled game-remix by about
  1000 px and pushed Play and the pad off screen.
- Fit-to-width guards (shrink type when a table is too wide) re-measure from the loosest step every time and wait for
  running animations to finish first. code-tracer's guard only ever tightened, and a value sliding into its cell
  overflowed for 400 ms, so the table stayed at 12 px type even at 1920x1080.

## Voice behavior

Every tool that narrates needs the same small queue. Copy the pattern from `tools/collision-lab/src.html` (narrate,
hush, readNow, firstTap):

- One welcome per mode, queued when the mode is entered. On the very first tap, decide only after that tap's own click
  handler has run: if the tap queued its own line, or was Read, skip the welcome without marking it said.
- Mark a line said when it starts playing, never when it is queued. A stop (mode switch, Read, Reset) drops lines that
  never started, unmarked, so their trigger can queue them again. Drop a queued line whose moment has passed (a
  different pair or target is showing, the probe left the zero point).
- Read always stops other speech and speaks the current hint; nothing queued may cut Read off; lines triggered during
  Read wait for it. `hush()` must also resolve the pending Read promise: a paused clip never fires `ended`, and the next
  line otherwise waits ~10 s (three tools had this bug).
- Say how to act (Cory, 2026-10-26). Whenever the tool waits for the student, the line and the hint name the next
  action and the control ("Tap the wrong card. Then tap the right move."), not only a question ("Which card is
  wrong?"). VERIFY walks every waiting moment as a student who can't read the screen.
- But don't nag (Cory, 2026-10-26). A how-to line is spoken the first time its step comes up; after that it only
  updates the hint, silently, so the screen still shows it and Read still says it. Repeating "Tap another circle, or
  tap Back to desk." after every selection was annoying. Results, questions and new steps are still spoken. VERIFY
  counts how often each how-to line is spoken in a run of five actions in a row.
- Two kinds of line, so "don't nag" doesn't go too far. How-to and teaching lines are spoken once per page load. Event
  lines (praise, a challenge met, a failed load, a result with new numbers) are spoken every time their event happens,
  and are still dropped when stale. game-remix first made every line once, and its second "You fixed it!" went silent.
  Keep an explicit set of event line ids in the code.
- The spoken line matches the state on screen. A welcome or how-to that assumes something (a remix to share, room to
  change) must not play when the screen says otherwise, and must not be marked said when it was skipped.
- Sound off uses nothing up; turning Sound back on queues the mode's welcome if it was never said.
- Test with held clicks (press, ~120 ms, release): instant scripted clicks hide pointerdown/click races. Log which clips
  actually start (`drive.py` "hold").

## Testing tools

- `python scripts/drive.py <id> shots.json <out>`: muted headless Chrome over CDP with real clicks (held), drags,
  keys, console errors and exceptions. `scripts/shoot.py` makes quick frames but does not report console errors.
- Every Chrome you start uses `--mute-audio` (Cory hears test audio otherwise). Close every Chrome and server you start.
- Drag physics: test with real or whole-pixel, timing-jittered pointer input, never only a smooth scripted pointer
  (motion-graph-match passed with a scripted pointer and was noise under a real mouse).
- Look at every frame. Recompute every number yourself (Python), with units.

## Art (local FLUX, `scripts/localart.py`)

- Never people, faces or hands from a local model: people go to Gemini (`scripts/art.py`) and Cory reviews every one.
- Describe what is in the picture, never what isn't: "no wheel" drew a wheel in all three candidates. Use an `"sd"`
  prompt (local model only) written positively.
- FLUX writes fake lettering on things that normally carry text (coins, signs, newspapers): ask for blank surfaces.
- Say how the image is used (a texture clipped to a shape needs a full-frame texture, not a whole scene).
- Aspects: 1:1, 16:9, 9:16, 3:4, 4:3, 16:10, 4:1, 5:1. Check two tools in the same batch don't ask for the same image.
- The FLUX server holds about 17 GB of RAM even idle: start it for an art session, stop it after.

## Scope

- No features that ask students to move work between devices by hand. Cory removed game-remix's Share (a remix code to
  copy and load, and a print card): "not feasible for a student to pass a code that long and it doesn't have that much
  of a pull." Save on this device is enough; in class, pairs swap laptops.

## Facts

Every number, date and claim on screen has a source in the spec, checked against it. If the spec's own example
contradicts its worked answers, trust the computation and say so. Hard history: explorer formats, no points or win
states.
