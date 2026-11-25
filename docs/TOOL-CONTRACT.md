# Tool Contract

How a tool plugs into Curio Class. Every built tool follows this. `python scripts/check_tools.py` enforces the "must" rules.

## Folder

```
tools/<tool-id>/
  <tool-id>.html   the tool: one self-contained file (required)
  tool.json        details the site needs (required)
  notes.md         teacher notes in Markdown (required; opens with What it teaches, Key skills, Support at home)
  plan.md          one-period lesson plan (expected for every tool; docs/LESSON-PLANS.md, scripts/check_plans.py)
  preview.svg      card art, 16:10 (optional; otherwise a format pattern is used)
```

`<tool-id>` is lowercase-with-hyphens and matches the concept title in `data/tools-concepts.csv` (State Quest → `state-quest`). A folder with `tool.json` turns that concept from "On the bench" into a built tool.

## tool.json

```json
{
  "id": "state-quest",
  "status": "beta",
  "hook": "Click a state, name it, fill the map.",
  "outcome": "Locate and name all 50 US states",
  "role": "teach",
  "unit_adds": "",
  "driver": "students or teacher",
  "minutes": "10-20",
  "modes": ["Practice", "Challenge"],
  "grades_label": "Grades 3-8",
  "sources": ["us-atlas v3, from US Census Bureau boundaries (public domain)"],
  "third_party": [],
  "updated": "2026-10-11"
}
```

- `status`: `beta` or `ready`
- `outcome`: only what the student does on the tool's main path. A readout, an optional mode or a teacher note is
  never part of it.
- `role` (BASELINE rule 21): `teach` (passes the teaching test for its codes), `see why` (the student explores the
  idea and predicts; the unit does the rest) or `practice` (assumes the teaching happened elsewhere).
- `unit_adds`: for `see why` and `practice`, one line on what a unit, worksheet or the Reading Room must add for the
  standard to be taught in full. Empty for `teach`. Tools made before 2026-11-10 get both fields as each is fixed
  or next passes through Refine.
- `driver`: `teacher` (projector-led, required for all K-2), `students`, or `students or teacher`
- `modes`: empty list for pure explore tools. Most tools don't need a score.
- `third_party`: bundled libraries with their license, e.g. `"Three.js r128 (MIT)"`
- The concept's topic, grade, subject, format and standards come from the catalog data, not from here. A topic's
  standards are spelled out, never a bare cluster, and each tool carries only the codes it teaches (BASELINE rule 22,
  docs/ECOSYSTEM.md).

## The HTML file must

1. **Be one file.** All CSS, JS, data, images and fonts are inline. The Download button hands over exactly this file.
2. **Make no automatic network requests.** No external `src=`, stylesheets, `@import`, `url(http...)` or fonts. Plain outbound `<a href>` links that a person clicks are fine.
3. **Collect nothing.** No analytics or cookies. `localStorage` only for per-device conveniences (settings, a saved drawing), wrapped in try/catch.
4. **Have** `<html lang>`, `<meta charset>`, `<meta name="viewport">`, a `<title>` and a `<meta name="description">`.
5. **Aim for 2 MB or less.** 2 MB is a goal, not a blocker (Cory, 2026-11-03). Over 6 MB, notes.md needs a line starting `Size:` saying why. (Elements Inspector, with Three.js inside, is 0.8 MB.)
6. **Work embedded and full screen.** It must be usable in a 16:10 iframe on the tool page and fill the window when opened alone.

## The HTML file should

- Be keyboard usable with visible focus, use 44px or larger targets (larger for K-2), and never use color as the only signal.
- Respect `prefers-reduced-motion` as the starting point, with a Motion button in the header that overrides it (remembered in localStorage `curio-motion`, shared across tools). Many school laptops have Windows animation effects off without anyone choosing it. Turning motion off removes movement only: story pacing and timers stay the same, so sound and pictures stay in step.
- Credit sources and licenses in a comment near the top.
- Pass the Polish checklist below (motion, pacing, art, layout, consistency, checking frames) before it is called v1.
- Feel like itself. There is no shared visual template on purpose: tools can each have their own look. The site provides the consistent frame around them.

## How the site uses it

- Tool page: `/tools/<id>/`, with the tool embedded live, Play full screen, Download, Embed code, teacher notes, standards, sources.
- Play and download: `/tools/<id>/<id>.html`, the same file.
- Unbuilt concepts get `/tools/<id>/` as an "On the bench" page (noindex, left out of the sitemap).

## Polish

Lessons from refining Marching Band and Three Pigs Lab (October 2026). Run through this before calling a tool v1. The rest of this contract says what a tool must do; this says what makes it feel finished. (Moved here from docs/POLISH.md, 2026-11-25.)

### Motion and pacing

- **Reduced motion is common by accident.** Many school laptops have Windows "Animation effects" off, which browsers report as `prefers-reduced-motion`. Treat it as the starting point only: put the shared Motion button in the header (localStorage `curio-motion`).
- **Never shorten timing for reduced motion.** It turns a story into fast-forward and the sounds lag the pictures. Calm mode removes movement, not time.
- **Pace for a teacher reading aloud.** Speech bubbles stay up `1400 + 75 ms per character`. Every beat (setup, build-up, the moment, the result) gets its own pause. A 20-second story is fine; a 4-second one is unreadable.
- **Particles start mid-flight.** Use negative animation delays so rain and snow are already falling, not lined up at the top waiting. When motion is off, scatter them in place.

### Art

- **Illustrations from Gemini, motion and diagrams in vector.** See ART.md.
- **Full-length characters need a portrait frame** (`"aspect": "9:16"`) or Gemini crops them. Ask for a clear gap between the legs if they will walk or march.
- **Never crop a character mid-body.** Hard edges read as broken. Split a painting with clip paths instead, and keep the clip windows still while parts move inside them.
- **Check cutouts on magenta.** Holes and haze are invisible on white. Green clothing needs the distance-from-key cutout (the default now).
- **Backgrounds: no characters, and cover wide screens.** Size the background to cover at least 2.9:1 around the action, and add mirrored copies beyond that.
- **Flat white shapes look like holes.** Snow, clouds, paper: give them shading, lumps, a highlight, a little sparkle.

### Layout

- **Nothing overlaps by accident.** Rows of figures stand in perspective (smaller and higher toward the back), with no figure covering another.
- **Keep the action area clear.** If the tool draws things into a painted scene (a Moon in the sky, a line of fans), check the painting has room for them there. A tall tree in the art hid the Moon for a quarter of the sky.
- **Test the extremes.** Smallest and largest counts, the widest and narrowest stage, the compact iframe on the tool page.
- **Ruled lines come from the rows,** never from a repeating background that drifts.

### Consistency

- **Anything shown twice must match.** If the pig shivers in the Inside window, the pig seen through the glass shivers too.
- **Words match the state.** Grammar ("brick walls"), counts, plurals.

### Games and quizzes

- **Nothing on screen gives the answer away.** In a predict or hidden-information mode, check every slider, readout, label, graph area and scene detail. A day slider gave away the Moon's position, and the arena line showed demand before sales opened.

### Sound and voice

- **Sound on by default** for teacher-led tools, with a Sound toggle.
- **Read uses the best voice the browser has** (`bestVoice()` ranking: natural/neural, then Google, then the rest; the Windows desktop voices David, Mark and Zira rank last). Chrome loads its voice list late, so tools hold the first utterance until `voiceschanged`, or it plays in the robotic default. Speak at pitch 1: a raised pitch makes Google's voice sound synthetic.
- **Recorded speech beats any browser voice.** Chrome on Windows offers only Google US English and the old desktop voices, which teachers hear as robotic. For fixed lines, record them: list every line in `voice/lines.json`, run `python scripts/voice.py <tool-id>` (Gemini text-to-speech, MP3 at 24 kbps), and put the token `"voice:*"` in src.html; the bundler turns it into a {text: audio} map. Speak lines that exactly match a recording, and keep names and other variable words on screen rather than in the spoken line. Unrecorded lines fall back to the browser voice. The speech models allow about 100 lines a day each, and a minute of speech adds about 240 KB to the file.
- **Local voice for volume.** `S:\AI\tts\.venv\Scripts\python.exe scripts/localvoice.py <tool-id>` clones the tool's Gemini voice with Qwen3-TTS (Apache 2.0) from one recorded line (it records that line with Gemini if there is none yet), makes every missing line on the GPU and encodes them like Gemini takes. Lines it made are listed in `voice/local.json`; credit "Some narration generated with Qwen3-TTS (Apache 2.0)". Listen to a few before shipping. `"tempo"` in lines.json applies to both.
- **Sounds fit the length of their beat,** so they never run past what is on screen.

### Checking it

- **Render frames headlessly:** `python scripts/shoot.py <tool-id> <name> "<js>"` loads the bundled tool with motion on, runs the JS, freezes animations and saves a PNG to the scratch folder. The in-app browser pane has reduced motion on and stops drawing when hidden, so it can't be trusted for animation.
- **Look at every frame you claim works.** Default state, each test or mode, the extremes, mid-animation.
