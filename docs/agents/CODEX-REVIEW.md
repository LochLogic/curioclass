# Codex review brief, any tool (Curio Class)

You are a fresh, cold reviewer of ONE Curio Class tool that another Codex chat just built. You did not build it and you
owe it nothing. After you finish, three blind Claude lenses check the same tool, and every finding they raise costs far
more to fix than the same finding fixed now. Your job is to find what they would find, fix it, and leave them little to do.

The tool id is in the prompt that sent you here, and `<id>` below means that id. The repo root is `S:\CurioClass-codex`,
shared with other chats. Run every command from there. Scratch means `_scratch/<id>` in it.

## Rules

Every rule in `docs/agents/CODEX-BUILD.md` holds here: Ground rules, Do not hang (a time limit on every command), Images
and the people rule. Read that brief first. In short: write only inside `tools/<id>/` and Scratch, no git commits, use only
the ports your prompt names, and keep the tool folder tidy.

- Keep what is strong. You are here to fix faults and lift weak spots, not to restyle the tool or strip it down. Do not
  make the graphics or the play plainer to clear a check.
- Add no features or topics beyond the spec.
- One pass. Look once, fix once, re-check what you fixed. Do not start a second full review or a polish round.

## 1. Look, before you read what the builder said

Read `docs/agents/STANDARDS.md`, `docs/agents/decisions/BASELINE.md`, `tools/<id>/spec.md`, `docs/POLISH.md`, then in
`docs/agents/REFINE.md` the three lenses (Teaching, Play, Craft) and how a lens reports, and in `docs/agents/BUILD.md`
the wave lessons. Then bundle (`$env:CURIO_DRAFT=1; python scripts/bundle_tool.py <id>`) and play the whole tool once as
a student of that grade, using `scripts/drive.py` as CODEX-BUILD.md shows.

Only then read `codex-report.md`, `handoff.md`, `notes.md` and `src.html`.

## 2. Find

Walk all three lenses, as written in REFINE.md, plus these. Open the frames and look at them.

- **The repeat findings.** Check every BUILD.md wave lesson yourself. Do not trust a PASS in the report.
- **Teaching.** Recompute the spec's numbers. Check that a wrong path teaches, nothing gives the answer away, and the
  notes open with `## What it teaches`, `## Key skills` and `## Support at home`.
- **Play.** Hold it to the Gameplay list in CODEX-BUILD.md. Name the flattest moment.
- **Graphics.** Look at every image at its final size, and hold the scenes to the Graphics list in CODEX-BUILD.md. Is the
  set one style? Is any picture untrue to what the tool teaches? Does any picture show a person? Is any image in
  `art:<name>` still missing that could be made?
- **Craft.** Every STANDARDS size, Motion off, grayscale, keyboard only, the voice checks, every extreme in POLISH.md.

Rank each finding as REFINE.md does: blocker, should fix, polish or nit.

## 3. Fix

Fix every blocker and should fix, in `src.html`, `notes.md`, `voice/lines.json`, `audit-states.json`, `handoff.md` and
the art. Make images that are missing and redraw poor ones as the Images section says. Fix a polish item when it takes a
few minutes. Leave nits.

If you disagree with the spec, or a fix would need a new feature or a kit change, do not make it. Write it under Left open.

## 4. Check

Re-shoot only what your fixes touched. Then run the audit once, last, with the same 40 minute limit:
`python scripts/audit_tool.py <id> <Scratch>/review-audit --port <your second port> --profile <Scratch>/chrome-prof-review`.
Fix what it confirms, re-shoot those frames, and stop. If the audit does not finish, say so and stop.

## Report: `tools/<id>/codex-review.md`

Under 100 lines. Write it as you go, so it survives a stuck command.

```
# Codex review: <id>
## Played                (what you did, as what grade, one line on how it felt)
## Findings fixed        (level, where, what was wrong, what you changed)
## Findings left         (level, where, why it stays)
## Flattest moment left
## Graphics              (images checked, redrawn, added; bundle KB)
## Audit                 (leads fixed, or "audit not finished")
## Left open
```

Be honest: a finding you leave and name is worth more than one you hide. When the report is written, say "Review done"
and stop.
