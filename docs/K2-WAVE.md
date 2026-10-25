# K-2 wave (started 2026-10-25)

Thirteen K-2 band tools, coded first, art second, polish third.

## Status

| Tool | State | Art |
|---|---|---|
| Shape Talk | live, awaiting review | none needed (drawn in code) |
| Feelings Faces | live, awaiting review | none needed (faces drawn in code) |
| Wonder Wall | live, awaiting review | none needed (CSS cork board) |
| Calm Corner | draft | 2 of 2 drawn (style test) |
| Sound Elevator | draft | 1 of 1 drawn (style test) |
| Habit Hero | draft | 1 of 2 (town background left) |
| Safety Street | draft | 1 of 9 |
| Animal Moves | draft | 1 of 13 |
| Lunch Tray Builder | draft | 3 of 28 (apple needs a redo, see below) |
| Library Adventure | draft | 0 of 1 |
| Classroom Phrases Game | draft | 0 of 16 |
| I Spy Science | draft | 0 of 28 |
| Community Map Words | draft | 0 of 24 (12 helpers are people: Gemini only) |

About 115 images left: 103 for FLUX overnight, 12 people for Gemini.

A draft keeps `tool.draft.json` instead of `tool.json`: the site leaves it on the bench and check_tools skips it. Build one for testing with `CURIO_DRAFT=1 python scripts/bundle_tool.py <id>` (placeholder circles for missing art; the generated html is gitignored per folder). When its art is in, rename `tool.draft.json` to `tool.json`, delete the folder's `.gitignore`, and it ships with the next deploy.

Voice: every tool has `voice/lines.json` (Puck voice, a style line per tool). Nothing is recorded yet (Gemini credits); tools fall back to the browser voice. I Spy Science has about 250 lines, so it takes a few days of quota.

## Style test (2026-10-25)

Sheet: `shots/style-test.jpg` (not committed). FLUX first picks next to earlier Gemini art.

- Characters and animals (frog, fox, turtle, puppy, mouse) are crisp and friendly: brighter, smoother digital cartoon than Gemini's softer gouache. Fine inside one tool; a tool shouldn't mix the two.
- FLUX adds things: Pip got goggles nobody asked for; the mouse holds the note as asked.
- One calm-corner background candidate drew two small children even with "no people" in the prompt. It was deleted. Classroom and home scenes invite people, so look at every candidate before picking.
- Backgrounds put scribble "posters" with fake text on the walls. Pick plain ones or paint the posters out.
- The apple on the yellow-green key kept its cast shadow as a bright green blob. Red and warm foods need `"key": "magenta"`, or `"shadow": "dark"`.
- The milk carton's white side nearly vanished on the pale key. White objects need a stronger key contrast.

## Order for the art night

1. Fix the apple and milk specs, then run FLUX on every draft tool (`python scripts/localart.py <id> --n 4`).
2. Pick in the morning, rekey, check each tool with real art (layout positions were set by hand, so check the I Spy and town maps).
3. Gemini (after top-up): the 12 community helpers, plus any FLUX misses, recorded in prompts.json with a reason.
