# Antigravity build brief (Curio Class)

You are Google Antigravity running Gemini 4 Argon, building ONE Curio Class tool as a test of a second builder
(owner's decision, 2026-11-08). The pool is Sara's 50 ELA specs (docs/agents/claims/sara.txt, batches 1 to 10).

**Follow `docs/agents/CODEX-BUILD.md` exactly, as if it were written to you,** with only the changes below. Where it
says Codex, read "you". Everything else in it binds: ground rules, Images, People, Size, Do not hang, Read in this
order, Files to make, Check your work and the report.

## Changes for Antigravity

- **Your folder is `S:\CurioClass-agy`** (branch `agy/build`). It replaces `S:\CurioClass-codex` everywhere in the
  briefs. If your workspace is anything else, say so and stop. Never touch `S:\CurioClass` or `S:\CurioClass-codex`.
- **Ports:** use the Chrome and host ports your prompt names, never the defaults (Codex uses those).
- **Images.** Use your own image generation (Gemini). Try hard, as the brief says: the art is the look of the tool.
  - Save each image you generate as `tools/<id>/art/raw/<name>.png` yourself. If your image tool saves into your
    conversation folder (under `~/.gemini/antigravity/brain/`), copy it from there.
  - Then run `python scripts/art.py <id> --rekey <name>` exactly as the brief says (only the `--rekey` form).
  - Mark each asset `"drawn_by": "antigravity"`.
  - Credit in `tool.draft.json` `sources`: `Illustrations generated with Google Gemini, edited for Curio Class`.
- **People: yes.** Draw people wherever the spec or the scene calls for them (students, teachers, families, authors,
  characters), following the brief's People rules: a natural range of skin tones, ages, bodies and abilities, no
  stereotypes, nothing frightening or mocking, `"people": true` on every asset that shows a person. The owner reviews
  every people image on the contact sheet. Only if generation refuses or fails, use the faceless silhouette and list
  it under "Art still to paint".
- **Voice.** You cannot record voice. Write `voice/lines.json` as the brief says; recording happens later.
- **Report:** `tools/<id>/codex-report.md` (same name, so the board and the Self-check find it). Its first line after
  the title says `Built by: Antigravity, Gemini 4 Argon, <thinking level>`. Add `"built_by": "antigravity-argon"` to
  `tool.draft.json`.
- No git commits, no branch changes. Claude merges the folder after the Self-check.

## Self-check (a separate, new chat)

When the prompt says Self-check: follow `docs/agents/CODEX-REVIEW.md` exactly, with the same changes above (folder,
ports, images, people). You did not build the tool; play it before you read the builder's report. The report is
`tools/<id>/codex-review.md`, its first line after the title `Self-checked by: Antigravity, Gemini 4 Argon,
<thinking level>`.
