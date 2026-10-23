# Polish checklist

Lessons from refining Marching Band and Three Pigs Lab (October 2026). Run through this before calling a tool v1. The tool contract says what a tool must do; this says what makes it feel finished.

## Motion and pacing

- **Reduced motion is common by accident.** Many school laptops have Windows "Animation effects" off, which browsers report as `prefers-reduced-motion`. Treat it as the starting point only: put the shared Motion button in the header (localStorage `curio-motion`).
- **Never shorten timing for reduced motion.** It turns a story into fast-forward and the sounds lag the pictures. Calm mode removes movement, not time.
- **Pace for a teacher reading aloud.** Speech bubbles stay up `1400 + 75 ms per character`. Every beat (setup, build-up, the moment, the result) gets its own pause. A 20-second story is fine; a 4-second one is unreadable.
- **Particles start mid-flight.** Use negative animation delays so rain and snow are already falling, not lined up at the top waiting. When motion is off, scatter them in place.

## Art

- **Illustrations from Gemini, motion and diagrams in vector.** See ART.md.
- **Full-length characters need a portrait frame** (`"aspect": "9:16"`) or Gemini crops them. Ask for a clear gap between the legs if they will walk or march.
- **Never crop a character mid-body.** Hard edges read as broken. Split a painting with clip paths instead, and keep the clip windows still while parts move inside them.
- **Check cutouts on magenta.** Holes and haze are invisible on white. Green clothing needs the distance-from-key cutout (the default now).
- **Backgrounds: no characters, and cover wide screens.** Size the background to cover at least 2.9:1 around the action, and add mirrored copies beyond that.
- **Flat white shapes look like holes.** Snow, clouds, paper: give them shading, lumps, a highlight, a little sparkle.

## Layout

- **Nothing overlaps by accident.** Rows of figures stand in perspective (smaller and higher toward the back), with no figure covering another.
- **Test the extremes.** Smallest and largest counts, the widest and narrowest stage, the compact iframe on the tool page.
- **Ruled lines come from the rows,** never from a repeating background that drifts.

## Consistency

- **Anything shown twice must match.** If the pig shivers in the Inside window, the pig seen through the glass shivers too.
- **Words match the state.** Grammar ("brick walls"), counts, plurals.

## Sound and voice

- **Sound on by default** for teacher-led tools, with a Sound toggle.
- **Read uses the best voice the browser has** (`bestVoice()` ranking: natural/neural, then Google, then the rest).
- **Sounds fit the length of their beat,** so they never run past what is on screen.

## Checking it

- **Render frames headlessly:** `python scripts/shoot.py <tool-id> <name> "<js>"` loads the bundled tool with motion on, runs the JS, freezes animations and saves a PNG to the scratch folder. The in-app browser pane has reduced motion on and stops drawing when hidden, so it can't be trusted for animation.
- **Look at every frame you claim works.** Default state, each test or mode, the extremes, mid-animation.
