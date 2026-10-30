# Build agent brief

You build ONE Curio Class tool from its spec. The spec is the source of truth: build what it says, nothing more.
If the spec is wrong or impossible, stop and report it rather than improvising.

## Read first

0. `docs/agents/STANDARDS.md`: standing rules (variety, sizes, voice behavior, testing, art). It wins over this brief.
1. `tools/<tool-id>/spec.md`: everything you build.
2. `docs/TOOL-CONTRACT.md`, `docs/KIT.md`, `docs/POLISH.md`.
3. `kit/starter/src.html`: start from a copy of it.
4. If the spec names a family engine: `docs/families/<family>.md` and the engine file it points to.
5. One approved tool close to this one in grade and format, as the quality bar (`python scripts/neighbors.py <id>`
   lists built neighbors).

## Make these files in `tools/<tool-id>/`

- `src.html` from the starter: the kit stylesheet and script, the tool's palette, its scene and logic.
  Keep `window.__tool = {state, setMode, allLines, ...}` so frames can be checked.
- `tool.draft.json`: the tool.json fields from the contract, plus `"stage": "built"`. (Draft until its art is in.)
- `notes.md`: teacher notes. Open with these three sections, in this order, then a 5-minute start, the modes, talk
  questions and good to know. Look at `tools/shape-talk/notes.md` for the rest. `scripts/check_tools.py` fails without them.
  - `## What it teaches`: one or two plain sentences on the educational goal, naming what students can do afterward.
    Not a copy of the plan's goal line, which speaks to students.
  - `## Key skills`: 3 to 5 bullets, each something a student practices in this tool, in everyday words, no standard codes.
  - `## Support at home`: 2 or 3 things a family can do this week, tied to this tool's idea, written to a parent or
    caregiver. No screen needed, nothing to buy, no teaching background assumed.
- `art/prompts.json`: the spec's art list in the format of `tools/calm-corner/art/prompts.json`. Do not draw art.
- `voice/lines.json`: voice, style and every line `allLines()` returns. Do not record.
- `audit-states.json`: the states a student reaches beyond the first screen (after a run, every stepper at its
  limits, each mode with work in it, an overlay open), as real clicks, keys and drags, with the regions that must stay
  in view (`keep`, such as the results after a run). `scripts/audit_tool.py` re-checks every size in each state; the
  format is in its header.
- `handoff.md`: a short note for whoever fixes this tool later: how src.html is laid out, the tricky parts, and what
  you would do next. Refine's polish may run after you are gone.

## Rules

- One file, no network requests, under 2 MB. All shapes, charts and diagrams drawn in SVG or canvas.
- Use the kit for motion, sound, speech, chimes and fitting the stage. Never re-implement them.
- Images use `art:<name>` tokens only for names in prompts.json. Draft builds show labeled placeholders.
- Pace for a teacher reading aloud (POLISH.md). Calm mode removes movement, never time.
- Accessible: keyboard, visible focus, 44 px targets (60 px for K-2), never color alone.
- Facts only from the spec's Sources. No em dashes. "Curio Class", never "Curio" alone.

## Check before you report

1. `CURIO_DRAFT=1 python scripts/bundle_tool.py <tool-id>` bundles cleanly.
2. `python scripts/drive.py <tool-id> shots.json <out>` (or shoot.py for quick frames) for the default screen, every mode, and the extremes.
   Look at every PNG. Fix overlaps, clipping, unreadable text and anything the spec's "Done when" fails.
3. No console errors (shoot.py prints them).
4. `python scripts/audit_tool.py <tool-id> <scratch>/audit --port <your port> --profile <absolute dir>`: fix or
   answer every lead in its audit.md (it is mechanical; a clean audit is not a clean tool).
5. The wave lessons below, each one checked. Every BR1 tool needed a second Refine round, and these were the
   repeat findings.

### Wave lessons (BR1, 2026-10-28)

- **Hint and voice.** The hint names the next control, and Read speaks it. On a tab or panel switch the hint
  changes at once, not when a queued line starts. How lines are chosen by `V.heard`, not counters. The first
  action never waits behind a line, no line names a disabled control, and no line is lost at a 2 s tap pace.
- **Focus and layout.** Focus is kept when controls rebuild, and nothing takes focus on load. Nothing rebuilds
  under the pointer. Reserve the hint's height so panels don't jump. Labels and badges never overlap.
- **Sizes.** 44 px targets (60 px for K-2) and an unclipped hint at every STANDARDS size, including 680x425 and
  375 wide through `drive.py --host`.
- **No giveaways.** Badges, meters, flag names, ids and the length or position of the right option reveal nothing.
  No meter or puzzle can be solved by sweeping a slider or trying every option for free.
- **Honest numbers.** A meter or estimate says on screen what it assumes (capture-the-flag's strength meter
  rated "Winter2026!" as safe).
- **Standards.** Every code on the module is taught by something a solo student does, not only a teacher
  question. The family doc matches the engine.
- **Motion off.** No infinite animations (the kit's `.calm` loops them at 0.01 ms). Placeholder art is legible.

### Lessons from the network-help-desk test (2026-10-28)

Three lenses agreed on each of these; the first three are checks the audit now runs, the rest are not.
- **A short set of choices never hides in a scroll panel.** Seven answer cards in three groups lost a whole group
  after a nudge at 1366x768 and two at 680x425. Every choice the student picks from is in view at every size.
- **Resize mid-animation.** A redraw during a ping dropped a node the mover still used: an exception and a call that
  stayed locked. Redraws carry the running animation's state, or wait for it.
- **A welcome put off past a first tap's own line lands late.** `welcomeAfter` is for one-mode tools only.
- **Show unknown as unknown.** A map or scene that hides a clue until it is asked draws that part as unknown, never
  as working (a cable drawn plugged in before the question that shows it is unplugged).
- **One look, one meaning.** A broken link drawn in the Guest link's orange dashes read as Guest. Each style in a
  legend means one thing.
- **The badge says what is true.** "Allowed" on the guest laptop that was refused contradicted the lesson.
- **A hint that changes with a state changes back.** "No bars" stayed after the tablet came back in range.
- **No answer by copying words.** Clue text that repeats the answer card's words turns diagnosis into matching.

Report: what you built, each "Done when" check with pass or fail, the frames you looked at, and anything left open.
Do not commit.
