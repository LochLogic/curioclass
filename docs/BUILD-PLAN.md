# Build plan: the bench, one fresh agent at a time

Agreed with Cory 2026-10-25. 532 concepts are on the bench. They get built in waves, each tool by its own fresh
agents, so nothing drifts over a long run and the 300th tool gets the same care as the first.

## Why fresh agents

A long session that builds tool after tool starts to blur them: it misremembers what it built, repeats ideas and
invents facts. Here no agent ever sees more than one tool, and everything it needs is in files, not in memory:
the concept catalog, the neighbors script, the kit, the family specs and the briefs below.

## The pipeline for one tool

| Step | Who | Brief | Output |
|---|---|---|---|
| 1. Spec | fresh spec agent | `docs/agents/SPEC.md` | `tools/<id>/spec.md` (one idea, not-like list, content, art, voice, sources, done-when) |
| 2. Spec check | the integrating session (Claude) | this file | a batch read of the wave's specs for overlap and fit; Cory may skim |
| 3. Build | fresh build agent | `docs/agents/BUILD.md` | draft tool: src.html, tool.draft.json, notes.md, art/prompts.json, voice/lines.json |
| 4. Verify | fresh verify agent, cold | `docs/agents/VERIFY.md` | `tools/<id>/verify.md`, PASS or FIX with findings |
| 5. Fix | the build agent again (at most 2 rounds) | its verify.md | then a re-verify |
| 5b. Lesson plan | fresh plan agent, after a PASS | `docs/agents/PLAN.md` | `tools/<id>/plan.md`, checked by `scripts/check_plans.py` (docs/LESSON-PLANS.md) |
| 6. Integrate | the integrating session | this file | commit, board, art and voice queues |
| 7. Art | daily rhythm (docs/ART.md) | | Cloudflare, local FLUX, Codex, Gemini for people |
| 8. Voice | daily rhythm (scripts/voice.py) | | Gemini or the local voice |
| 9. Review | Cory, on the Review Desk | | approve, or notes back to step 5 |
| 10. Live | rename tool.draft.json to tool.json, make the card art (`python scripts/preview.py <id>`, look at it), deploy | | preview.svg |

`python scripts/board.py` shows where every tool is (docs/BUILD-BOARD.md). It reads the files, so it can't drift.

## Overlap: kit, family engine, tool

See `docs/KIT.md`. The kit is what every tool does the same way. A family engine (`docs/families/`) is the shared
mechanic of a collection, designed once; its first tool builds it, its siblings reuse it and differ in content and
framing. The tool is its one idea. The spec agent's "Not like" section, fed by `scripts/neighbors.py`, keeps two
tools from teaching the same thing the same way. Family engines specced so far: number-line, data-desk, graphing.

## Variety

Already enforced by the concept catalog (`scripts/check_concepts.py`): no format above 25% of a subject, at least 8
formats per subject, no three of a format in a row within a grade, unique titles. Cory: no notes.

## Waves

`data/waves.csv` assigns tools to waves.

- **Wave 0 (done 2026-10-25):** the kit, the starter, the briefs, neighbors.py, board.py, three family specs.
- **Wave 1 (pilot, 20 tools):** two from each of the three families (the first builds the engine, the second proves
  reuse) and 14 standalone tools across subjects, grades K-12 and 14 formats. It measures cost per tool, the
  verifier's catch rate and how often Cory sends one back. Decide the wave size after it.
- **Then waves of 30 to 50**, grouped by family and grade band so engines land before their siblings.

Held back from early waves: ASL (needs video by Deaf signers and Deaf educator review), Spanish (needs a
native-speaker review), and hard history (needs extra care and teacher guidance). They get their own waves.

## Review tiers

Cory reviews every K-2 tool and every sensitive one (hard history, health, mental health) in full. For other tools
the verify agent does the deep check and Cory spot-checks about one in four, plus anything the verifier flagged.

## Voice

Gemini's daily quota (about 150 lines a day) can't voice 500 tools, so each tool gets ONE Gemini line in its own
voice and style, and `scripts/localvoice.py` (Qwen3-TTS on this PC, no limit) clones that voice for every other line.
Cory compared them 2026-10-25: the clone of the Gemini voice is good; Qwen's own designed voices sounded wrong for
children's tools and are not used. See docs/POLISH.md (Sound and voice) and docs/ART.md for the art rhythm.

## Running a wave (for the integrating session)

1. `python scripts/board.py --wave N` for the list.
2. Spec agents in parallel (they only write spec.md). Read all the specs together; send back overlaps.
3. Build agents, then verify agents, then plan agents for each PASS, one tool each. Builds only touch their own tool folder, so they can run in
   parallel; a family's first tool runs before its siblings (it writes the engine).
4. Integrate: check_tools, commit, board, queue art and voice, add to the Review Desk when art and voice are in.
